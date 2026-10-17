"""Pre-registered experiment: does the mapper add value on a problem far from language models?

Bin packing (nano/profiles/binpack_nobase.py: no baseline, a harness scorer, CPU only), three arms at an equal cap
of scorer calls (research_notes/team_gaps/03_generality.md, "What the first real non-LLM run should check"):

  profile_only  the loop on the profile's default tree: --no-planner (no planner call), --no-deepen,
                --off-tree-share 0 (no off-map contexts)
  full          the loop with its defaults (planner, interrogation, off-map contexts)
  best_of_n     no mapper and no critics: N builder calls with the loop's own direct-build prompt (the "formal"
                card: the whole problem statement, the skeleton, the output format), each checked by the
                profile's ScriptChecker through the loop's verify, until the scorer-call cap is reached. This is a
                small driver over NanoLoop (its run_control is replaced), not a new pipeline.

Modes:
  python -m nano.experiments.binpack_arms prereg --out DIR      write DIR/prereg.json (never overwrites a different one)
  python -m nano.experiments.binpack_arms dry --out DIR         prereg, then every arm on the mock backend for one short
                                                                round under DIR/lab, then the report (no model tokens)
  python -m nano.experiments.binpack_arms run --out DIR         prereg, then the real arms x seeds (costs tokens)
  python -m nano.experiments.binpack_arms report --out DIR      DIR/binpack_arms_report.md from DIR/arms.json
  python -m nano.experiments.binpack_arms bestofn ...           the best-of-N driver for one seed (used by run and dry)

The prediction is fixed in PREREG below, so git dates it; prereg.json copies it next to the results before anything runs.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import statistics
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
ARMS = ("profile_only", "full", "best_of_n")
PROFILE = "binpack_nobase"
FORBIDDEN = ("validation loss", "train.py", "tokens", "attention")   # words of the language-model problem

PREREG = {
    "experiment": "binpack_arms",
    "question": "Does the HTSA mapper add value on online bin packing at an equal number of scorer calls?",
    "profile": PROFILE,
    "metric": ("full-level packing score of the arm's best checked candidate: mean bins used / ceil(total size) over "
               "100 instances of 1000 items at the matched seed (nano/profiles/binpack/scorer.py --level full); lower "
               "is better; only candidates whose full scoring started within the arm's first scorer_cap scorer calls count"),
    "arms": {
        "profile_only": "loop on the default tree: --no-planner --no-deepen --off-tree-share 0",
        "full": "loop with its defaults",
        "best_of_n": "N direct builds from the whole problem statement (loop 'formal' prompt), ScriptChecker, no mapper or critics",
    },
    "prediction": {
        "ordering": ["full", "best_of_n", "profile_only"],
        "ordering_text": "full > best-of-N > profile-only on the full-level packing score (better = lower)",
        "margin": 0.002,
        "margin_text": ("A pair counts as ordered when the better arm's mean best score over the seeds is lower by at least "
                        "0.002 (the profile's own margin, constraint C6) and it is lower in at least 2 of the 3 seeds"),
        "failure_rule": ("if full does not beat best-of-N by that rule, report that the mapper added no value on bin "
                         "packing at this budget; no re-run with other settings is counted as a test of this prediction"),
    },
    "seeds": [0, 1, 2],
    "scorer_cap_per_arm": 60,
    "token_budget_per_arm": 400_000,
    "loop_settings": {"rounds": 3, "implement": 10},
    "best_of_n_max_builds": 40,
    "checks": [
        "1 tree differs from default: part names in the full arm's problem_tree.json against the profile tree",
        "2 full beats best-of-N at equal scorer calls (rule above)",
        "3 the checker rejects three planted wrong solutions (and accepts a plain first-fit control)",
        "4 no prompt sent names the language-model problem: 'validation loss', 'train.py', 'tokens', 'attention'",
        "5 spend per accepted improvement: model tokens and scorer calls per reference move, from the ledger",
    ],
}


# ---------------------------------------------------------------------------------------------- prereg
def _git_head() -> str:
    try:
        return subprocess.run(["git", "rev-parse", "HEAD"], cwd=str(ROOT), capture_output=True, text=True,
                              timeout=20).stdout.strip()
    except Exception:  # noqa: BLE001
        return ""


def prereg_hash(p: dict) -> str:
    return hashlib.sha256(json.dumps(p, sort_keys=True).encode()).hexdigest()[:16]


def write_prereg(out: Path, prereg: dict | None = None) -> dict:
    """out/prereg.json with the prediction, before anything runs. An existing file with a different prediction is
    an error (a pre-registration is never edited after the fact); the same one is kept with its first timestamp."""
    prereg = dict(prereg or PREREG)
    out.mkdir(parents=True, exist_ok=True)
    p = out / "prereg.json"
    h = prereg_hash(prereg)
    if p.exists():
        old = json.loads(p.read_text(encoding="utf-8"))
        if old.get("hash") != h:
            raise SystemExit(f"{p} holds a different pre-registration (hash {old.get('hash')} vs {h}); "
                             "use a new --out folder rather than editing a prediction")
        return old
    doc = {**prereg, "hash": h, "written": time.strftime("%Y-%m-%dT%H:%M:%S"), "git_commit": _git_head()}
    p.write_text(json.dumps(doc, indent=1), encoding="utf-8")
    return doc


# ---------------------------------------------------------------------------------------------- command lines
def run_id(batch: str, seed: int, profile: str = PROFILE) -> str:
    """The loop's run folder name (nano/loop.py NanoLoop.__init__)."""
    return f"{batch}__nano__{profile}__scaffold__r{seed}"


def arm_commands(arm: str, seed: int, prefix: str, pre: dict, dry: bool = False, python: str | None = None) -> list[str]:
    """The command line of one arm at one seed. dry: the mock backend (nano.dry_run for the loop arms), one short
    round, few builds and a small scorer cap."""
    py = python or sys.executable
    batch = f"{prefix}-{arm.replace('_', '')}-s{seed}"
    prof = pre.get("profile", PROFILE)
    ls = pre.get("loop_settings", {})
    rounds, implement = (1, 2) if dry else (ls.get("rounds", 3), ls.get("implement", 10))
    budget = pre.get("token_budget_per_arm", 400_000)
    if arm == "best_of_n":
        cap = 9 if dry else pre.get("scorer_cap_per_arm", 60)
        n = 3 if dry else pre.get("best_of_n_max_builds", 40)
        cmd = [py, "-m", "nano.experiments.binpack_arms", "bestofn", "--profile", prof, "--batch", batch,
               "--replicate", str(seed), "--n-max", str(n), "--scorer-cap", str(cap), "--budget", str(budget)]
        return cmd + (["--mock"] if dry else [])
    head = ([py, "-m", "nano.dry_run", "--profile", prof, "--batch", batch, "--implement", str(implement),
             "--rounds", str(rounds), "--budget", str(budget), "--max-sketch-calls", "4"] if dry else
            [py, "-m", "nano.loop", "--profile", prof, "--batch", batch, "--implement", str(implement),
             "--rounds", str(rounds), "--budget", str(budget)])
    head += ["--replicate", str(seed)]
    if arm == "profile_only":
        head += ["--no-planner", "--no-deepen", "--off-tree-share", "0"]
    elif arm != "full":
        raise ValueError(arm)
    return head


# ---------------------------------------------------------------------------------------------- best-of-N driver
class _ScorerCounter:
    """Counts the ScriptChecker's scorer runs (each _score call is one run of the harness scorer)."""

    def __init__(self, impl):
        self.n = 0
        self._orig = impl._score

        def counted(*a, **kw):
            self.n += 1
            return self._orig(*a, **kw)
        impl._score = counted


def run_best_of_n(profile: str, batch: str, replicate: int, n_max: int, scorer_cap: int, budget: int,
                  backend: str | None = None, model: str | None = None, workers: int = 4) -> dict:
    """N builder calls with the loop's direct-build prompt, each verified by the profile's checker until the scorer
    cap; the loop's state, ledger, prompts and answer.json are written as for any arm."""
    from harness import config
    from nano import loop as L
    from nano import profile as PF
    PF.set_current(PF.load(profile))
    loop = L.NanoLoop(batch, replicate, backend or config.default_backend(), budget, 1, 60.0, model)
    loop.arm = "plain"                  # the loop's control-arm path: no tree, no clusters, no critics
    loop.do_research = loop.do_analogy = loop.do_premortem = loop.do_deepen = False
    counter = _ScorerCounter(loop.checker.impl)

    def control(t0: float) -> dict:
        built, stopped = 0, ""
        while built < n_max and not stopped:
            k = min(workers, n_max - built)
            with ThreadPoolExecutor(max_workers=k) as ex:
                res = list(ex.map(lambda i: loop.run_card("formal", 1, "none", f"bon{built + i}", None, None, "first"),
                                  range(k)))
            built += k
            kept = loop.dedup([c for c in res if c], 1)
            loop.cands.extend(kept)
            for c in kept:
                if counter.n >= scorer_cap:
                    stopped = "scorer cap"
                    break
                rec = loop.verify(c, 1)
                print(f"[bon] {c.id} -> {rec['status']} rung {rec['rung_reached']} | scorer calls {counter.n}/{scorer_cap}",
                      flush=True)
            if counter.n >= scorer_cap:
                stopped = "scorer cap"
            elif loop.spent >= loop.B:
                stopped = "token budget"
            elif not any(res):
                stopped = "no parseable build in a batch"
        loop.decisions.append({"round": 0, "step": "control", "arm": "best_of_n", "n_builds": built, "stopped": stopped,
                               "scorer_calls": counter.n, "scorer_cap": scorer_cap, "spent": loop.spent, "ts": L.now_ts()})
        loop._write_state()
        return loop._finish(t0)

    loop.run_control = control           # NanoLoop.run(): state, problem.md, then run_control for a control arm
    ans = loop.run()
    print(json.dumps({"run_dir": str(loop.run_dir), "scorer_calls": counter.n, "n_candidates": ans.get("n_candidates"),
                      "n_checked": ans.get("n_checked"), "spent_tokens": ans.get("spent_tokens")}))
    return ans


# ---------------------------------------------------------------------------------------------- running the arms
def _arm_env(lab: Path | None, dry: bool) -> dict:
    env = {**os.environ, "PYTHONUNBUFFERED": "1", "PYTHONPATH": str(ROOT) + os.pathsep + os.environ.get("PYTHONPATH", "")}
    if lab is not None:
        env["HTSA_LAB_ROOT"] = str(lab)
    if dry:
        env["HTSA_BACKEND"] = "mock"
        env["HTSA_EXEC_PYTHON"] = env.get("HTSA_EXEC_PYTHON") or sys.executable   # the temp lab has no venv
    return env


def run_arms(out: Path, dry: bool, seeds=None, prefix: str | None = None, timeout: float = 3600 * 6) -> dict:
    pre = write_prereg(out)
    seeds = list(seeds if seeds is not None else ([0] if dry else pre["seeds"]))
    prefix = prefix or ("mock-binpack-arms" if dry else "binpack-arms")
    lab = (out / "lab") if dry else Path(os.environ.get("HTSA_LAB_ROOT", r"D:\AGI-lab"))
    lab.mkdir(parents=True, exist_ok=True)
    env = _arm_env(lab, dry)
    manifest = {"dry": dry, "lab_root": str(lab), "profile": pre["profile"], "prereg_hash": pre["hash"],
                "scorer_cap": 9 if dry else pre["scorer_cap_per_arm"], "seeds": seeds, "runs": []}
    (out / "logs").mkdir(exist_ok=True)
    for seed in seeds:
        for arm in ARMS:
            cmd = arm_commands(arm, seed, prefix, pre, dry)
            log = out / "logs" / f"{arm}_s{seed}.log"
            t0 = time.time()
            with log.open("w", encoding="utf-8") as f:
                p = subprocess.run(cmd, cwd=str(ROOT), env=env, stdout=f, stderr=subprocess.STDOUT, timeout=timeout)
            batch = cmd[cmd.index("--batch") + 1]
            row = {"arm": arm, "seed": seed, "batch": batch, "run_id": run_id(batch, seed, pre["profile"]),
                   "cmd": cmd[1:], "rc": p.returncode, "wall_s": round(time.time() - t0, 1), "log": str(log)}
            manifest["runs"].append(row)
            print(f"[arms] {arm} seed {seed}: rc {p.returncode} in {row['wall_s']}s ({log})", flush=True)
            (out / "arms.json").write_text(json.dumps(manifest, indent=1), encoding="utf-8")
    return manifest


# ---------------------------------------------------------------------------------------------- report
def _jsonl(p: Path) -> list[dict]:
    if not p.exists():
        return []
    out = []
    for line in p.read_text(encoding="utf-8").splitlines():
        try:
            out.append(json.loads(line))
        except Exception:  # noqa: BLE001
            continue
    return out


def scorer_calls(run_dir: Path) -> list[tuple[float, str]]:
    """Every scorer run in a run folder, oldest first: each ScriptChecker._score makes OUT/_nodata at its start."""
    calls = []
    for d in (run_dir / "verify").rglob("_nodata") if (run_dir / "verify").exists() else []:
        calls.append((d.stat().st_mtime, str(d.parent.relative_to(run_dir)).replace("\\", "/")))
    return sorted(calls)


def candidate_scores(run_dir: Path, cap: int) -> dict:
    """Checked candidates with a full-level score, in the order their full scoring started, and which of them
    started within the first `cap` scorer calls."""
    calls = scorer_calls(run_dir)
    cutoff = calls[cap - 1][0] if len(calls) >= cap else float("inf")
    rows = {}
    for r in _jsonl(run_dir / "verify.jsonl"):
        m = (r.get("details") or {}).get("metrics") or {}
        if r.get("retested_against") or r.get("status") != "checked" or m.get("long_score") is None:
            continue
        rows.setdefault(r["id"], float(m["long_score"]))
    cands = []
    for cid, score in rows.items():
        nd = run_dir / "verify" / cid / "full" / "_nodata"
        t = nd.stat().st_mtime if nd.exists() else float("inf")
        node = None
        pj = run_dir / "pool" / f"{cid}.json"
        if pj.exists():
            try:
                node = json.loads(pj.read_text(encoding="utf-8")).get("node")
            except Exception:  # noqa: BLE001
                node = None
        cands.append({"id": cid, "score": score, "t": t, "in_cap": t <= cutoff, "node": node})
    cands.sort(key=lambda c: c["t"])
    return {"n_calls": len(calls), "cands": cands}


def ledger_tokens(lab: Path, rid: str) -> int:
    tot = 0
    for r in _jsonl(lab / "memory" / "ledger.jsonl"):
        if r.get("run_id") == rid:
            t = r.get("tokens") or {}
            tot += sum(int(t.get(k) or 0) for k in ("input_tokens", "output_tokens", "cache_read_input_tokens",
                                                    "cache_creation_input_tokens"))
    return tot


def accepted_improvements(cands: list[dict], margin: float) -> int:
    """Reference moves within the cap: the first checked candidate sets the reference (no baseline in this profile);
    a later one counts when it beats the running best by the margin."""
    best, n = None, 0
    for c in cands:
        if not c["in_cap"]:
            continue
        if best is None or c["score"] < best - margin:
            best, n = c["score"], n + 1
    return n


def prompt_hits(run_dir: Path, terms=FORBIDDEN) -> tuple[dict, dict]:
    """Prompt files that name each term (whole word, any case), and up to two distinct snippets per term."""
    hits, snips = {t: [] for t in terms}, {t: [] for t in terms}
    for p in sorted((run_dir / "prompts").glob("*.txt")) if (run_dir / "prompts").exists() else []:
        text = p.read_text(encoding="utf-8", errors="replace")
        for t in terms:
            m = re.search(r"\b" + re.escape(t) + r"\b", text, flags=re.I)
            if m:
                hits[t].append(p.name)
                s = " ".join(text[max(0, m.start() - 50): m.end() + 30].split())
                if s not in snips[t] and len(snips[t]) < 2:
                    snips[t].append(s)
    return hits, snips


def tree_names(run_dir: Path) -> list[str]:
    """Part names on the run's map (failure questions and the off-map node left out)."""
    pt = run_dir / "problem_tree.json"
    if not pt.exists():
        return []
    nodes = json.loads(pt.read_text(encoding="utf-8")).get("nodes", [])
    return [n["name"] for n in nodes if n.get("kind") != "question" and n.get("id") not in ("offtree",)]


PLANTED = {
    "overfills a bin": ("def choose_bin(item, bins, capacity):\n"
                        "    return 0 if bins else -1\n"),
    "returns an index out of range": ("def choose_bin(item, bins, capacity):\n"
                                      "    return len(bins) + 3\n"),
    "reads the scorer's files": ("import os\n\n\ndef choose_bin(item, bins, capacity):\n"
                                 "    os.listdir('.')\n    for i, fill in enumerate(bins):\n"
                                 "        if fill + item <= capacity:\n            return i\n    return -1\n"),
}
CONTROL_OK = ("def choose_bin(item, bins, capacity):\n    for i, fill in enumerate(bins):\n"
              "        if fill + item <= capacity + 1e-9:\n            return i\n    return -1\n")


def planted_check(out: Path, profile: str = PROFILE) -> list[dict]:
    """Three wrong rules and one plain first-fit control through the profile's ScriptChecker (rungs 0-1: static
    rule, then the scorer's build level, which validates every placement)."""
    from nano import profile as PF
    from nano.checks import script
    if not Path(script.PY).exists():
        script.PY = Path(sys.executable)
    pf = PF.load(profile)
    ck = script.ScriptChecker(pf, **dict(pf.checker_args or {}))
    d = out / "planted"
    d.mkdir(parents=True, exist_ok=True)
    res = []
    for i, (name, src) in enumerate(list(PLANTED.items()) + [("control: plain first fit", CONTROL_OK)]):
        f = d / f"planted_{i}.py"
        f.write_text(src, encoding="utf-8")
        rec = ck.check(f, d / f"check_{i}", {}, rung_max=1, boundary=None, baseline_src=None)
        fb = rec.get("feedback") or {}
        res.append({"name": name, "control": name.startswith("control"), "status": rec["status"],
                    "rung": fb.get("rung"), "reason": str(fb.get("reason", ""))[:100]})
    return res


def _fmt(x, nd=4):
    return "-" if x is None else f"{x:.{nd}f}"


def report(out: Path, run_planted: bool = True) -> str:
    from nano import profile as PF
    man = json.loads((out / "arms.json").read_text(encoding="utf-8"))
    pre = json.loads((out / "prereg.json").read_text(encoding="utf-8"))
    lab, cap, margin = Path(man["lab_root"]), int(man["scorer_cap"]), float(pre["prediction"]["margin"])
    default_names = [n["name"] for n in PF.load(man["profile"]).tree]
    per = {}
    for r in man["runs"]:
        rd = lab / "runs" / r["run_id"]
        cs = candidate_scores(rd, cap)
        within = [c for c in cs["cands"] if c["in_cap"]]
        best = min(within, key=lambda c: c["score"]) if within else None
        acc = accepted_improvements(cs["cands"], margin)
        tok = ledger_tokens(lab, r["run_id"])
        hits, snips = prompt_hits(rd)
        per[(r["arm"], r["seed"])] = {
            **r, "run_dir": rd, "n_calls": cs["n_calls"], "n_checked_in_cap": len(within),
            "best": best["score"] if best else None, "best_node": best["node"] if best else None,
            "accepted": acc, "tokens": tok, "calls_used": min(cs["n_calls"], cap),
            "hits": hits, "snips": snips, "tree": tree_names(rd),
            "nodes_with_checked": sorted({c["node"] for c in within if c["node"]})}
    seeds = man["seeds"]
    L = [f"# Bin-packing arms report{' (DRY: mock backend, the numbers only prove the plumbing)' if man['dry'] else ''}", "",
         f"Pre-registration: hash {pre['hash']}, written {pre.get('written')}, commit {pre.get('git_commit', '')[:10]}. "
         f"Profile {man['profile']}; scorer cap {cap} calls per arm and seed; seeds {seeds}.", "",
         f"Prediction: {pre['prediction']['ordering_text']}. {pre['prediction']['margin_text']}.", "",
         "## Runs", "",
         "| arm | seed | rc | scorer calls (used / cap) | checked in cap | best full score | model tokens | accepted improvements | tokens per accepted | scorer calls per accepted |",
         "|---|---|---|---|---|---|---|---|---|---|"]
    for (arm, seed), p in per.items():
        under = " (under cap)" if p["n_calls"] < cap else ""
        tpa = f"{p['tokens'] / p['accepted']:,.0f}" if p["accepted"] else "-"
        cpa = f"{p['calls_used'] / p['accepted']:.1f}" if p["accepted"] else "-"
        L.append(f"| {arm} | {seed} | {p['rc']} | {p['calls_used']} / {cap}{under} (all {p['n_calls']}) | {p['n_checked_in_cap']} | "
                 f"{_fmt(p['best'])} | {p['tokens']:,} | {p['accepted']} | {tpa} | {cpa} |")

    # check 1: the full arm's map against the profile's default tree
    L += ["", "## Check 1: does the mapper's tree differ from the default tree?", ""]
    for seed in seeds:
        f, po = per.get(("full", seed)), per.get(("profile_only", seed))
        if not f:
            continue
        added = [n for n in f["tree"] if n not in default_names]
        removed = [n for n in default_names if n not in f["tree"]]
        same_po = po is not None and sorted(po["tree"]) == sorted(default_names)
        L.append(f"- seed {seed}: full arm map has {len(f['tree'])} parts; {len(added)} not in the default "
                 f"({'; '.join(added[:8]) or 'none'}), {len(removed)} default parts dropped "
                 f"({'; '.join(removed[:8]) or 'none'}). Verdict: {'DIFFERS' if (added or removed) else 'SAME AS DEFAULT'}. "
                 f"Parts with a checked candidate within the cap: {', '.join(f['nodes_with_checked']) or 'none'}; best from "
                 f"{f['best_node'] or '-'}. Profile-only map equals the default: {'yes' if same_po else 'no'}.")

    # check 2: ordering at equal scorer calls
    L += ["", "## Check 2: does full beat best-of-N at equal scorer calls?", ""]
    means = {}
    for arm in ARMS:
        vals = [per[(arm, s)]["best"] for s in seeds if (arm, s) in per and per[(arm, s)]["best"] is not None]
        means[arm] = statistics.mean(vals) if vals else None
        L.append(f"- {arm}: mean best full score {_fmt(means[arm])} over {len(vals)} seed(s)")

    def ordered(a: str, b: str) -> tuple[bool | None, str]:
        pairs = [(per[(a, s)]["best"], per[(b, s)]["best"]) for s in seeds
                 if (a, s) in per and (b, s) in per and per[(a, s)]["best"] is not None and per[(b, s)]["best"] is not None]
        if not pairs:
            return None, "no data"
        wins = sum(1 for x, y in pairs if x < y)
        need = max(1, -(-2 * len(pairs) // 3))          # 2 of 3 seeds
        diff = statistics.mean(y - x for x, y in pairs)
        ok = diff >= margin and wins >= need
        return ok, f"{a} lower by {diff:+.4f} on average, lower in {wins}/{len(pairs)} seeds (needs >= {margin} and {need})"
    order = pre["prediction"]["ordering"]
    verdicts = []
    for a, b in zip(order, order[1:]):
        ok, why = ordered(a, b)
        verdicts.append(ok)
        L.append(f"- {a} better than {b}: {'YES' if ok else ('NO' if ok is False else 'NO DATA')} ({why})")
    fb_ok, fb_why = ordered("full", "best_of_n")
    L.append(f"- Pre-registered claim (full beats best-of-N): {'CONFIRMED' if fb_ok else ('NOT CONFIRMED' if fb_ok is False else 'NO DATA')}. "
             f"Full predicted ordering: {'held' if all(verdicts) else 'did not hold'}.")

    # check 3: planted wrong solutions
    L += ["", "## Check 3: does the checker reject planted wrong solutions?", ""]
    if run_planted:
        pl = planted_check(out, man["profile"])
        bad = [r for r in pl if not r["control"]]
        rej = sum(1 for r in bad if r["status"] != "checked")
        ctl = [r for r in pl if r["control"]]
        for r in pl:
            L.append(f"- {r['name']}: {r['status']} (rung {r['rung']}{': ' + r['reason'] if r['reason'] else ''})")
        L.append(f"- Rejected {rej}/{len(bad)} planted wrong rules; the control was "
                 f"{'accepted' if ctl and ctl[0]['status'] == 'checked' else 'NOT accepted'}.")
    else:
        L.append("- not run")

    # check 4: prompts naming the language-model problem
    L += ["", "## Check 4: does any prompt sent name the language-model problem?", "",
          "Terms (whole word, any case): " + ", ".join(f"'{t}'" for t in FORBIDDEN) + ".", ""]
    total = 0
    for (arm, seed), p in per.items():
        n_files = len(list((p["run_dir"] / "prompts").glob("*.txt"))) if (p["run_dir"] / "prompts").exists() else 0
        found = {t: v for t, v in p["hits"].items() if v}
        total += sum(len(v) for v in found.values())
        L.append(f"- {arm} seed {seed}: {n_files} prompts; "
                 + ("; ".join(f"'{t}' in {len(v)} ({', '.join(v[:3])})" for t, v in found.items()) if found else "no hits"))
        for t in found:
            for s in p["snips"][t]:
                L.append(f"  - '{t}': ...{s}...")
    L.append(f"- Verdict: {'CLEAN' if total == 0 else f'{total} prompt hits; read them before trusting the arms'}."
             + (" In a dry run the mock's replies are written for the language-model profile, and later prompts quote "
                "them, so hits there can come from the mock rather than from the loop's own templates." if man["dry"] and total else ""))

    # check 5: spend per accepted improvement
    L += ["", "## Check 5: spend per accepted improvement", "",
          "An accepted improvement is a reference move within the cap: the first checked rule sets the reference "
          f"(there is no baseline), a later one counts when it beats the running best by {margin}. Tokens are the "
          "model tokens the ledger records for the run (all roles); scorer calls are capped as above. See the Runs "
          "table for the per-run figures.", ""]
    for arm in ARMS:
        tok = sum(per[(arm, s)]["tokens"] for s in seeds if (arm, s) in per)
        acc = sum(per[(arm, s)]["accepted"] for s in seeds if (arm, s) in per)
        calls = sum(per[(arm, s)]["calls_used"] for s in seeds if (arm, s) in per)
        L.append(f"- {arm}: {acc} accepted over {len(seeds)} seed(s); "
                 + (f"{tok / acc:,.0f} tokens and {calls / acc:.1f} scorer calls per accepted improvement" if acc
                    else f"none accepted ({tok:,} tokens, {calls} scorer calls spent)"))
    text = "\n".join(L) + "\n"
    (out / "binpack_arms_report.md").write_text(text, encoding="utf-8")
    return text


# ---------------------------------------------------------------------------------------------- CLI
def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("mode", choices=["prereg", "dry", "run", "report", "bestofn"])
    ap.add_argument("--out", default=str(Path(os.environ.get("HTSA_LAB_ROOT", r"D:\AGI-lab")) / "results" / "binpack_arms"))
    ap.add_argument("--seeds", default="", help="dry/run: comma-separated seeds (default: dry 0, run the pre-registered ones)")
    ap.add_argument("--no-planted", action="store_true", help="report: skip the planted-solution check")
    # bestofn
    ap.add_argument("--profile", default=PROFILE)
    ap.add_argument("--batch", default="binpack-arms-bestofn")
    ap.add_argument("--replicate", type=int, default=0)
    ap.add_argument("--n-max", type=int, default=PREREG["best_of_n_max_builds"])
    ap.add_argument("--scorer-cap", type=int, default=PREREG["scorer_cap_per_arm"])
    ap.add_argument("--budget", type=int, default=PREREG["token_budget_per_arm"])
    ap.add_argument("--backend", default=None)
    ap.add_argument("--model", default=None)
    ap.add_argument("--mock", action="store_true", help="bestofn: the content-aware mock of nano/dry_run.py (no tokens)")
    a = ap.parse_args(argv)
    out = Path(a.out)
    seeds = [int(s) for s in a.seeds.split(",") if s.strip()] or None
    if a.mode == "prereg":
        print(json.dumps(write_prereg(out), indent=1))
    elif a.mode == "bestofn":
        if a.mock:
            from harness import llm
            from nano import dry_run
            llm.set_mock(dry_run.mock)
        run_best_of_n(a.profile, a.batch, a.replicate, a.n_max, a.scorer_cap, a.budget,
                      "mock" if a.mock else a.backend, a.model)
    elif a.mode in ("dry", "run"):
        man = run_arms(out, dry=a.mode == "dry", seeds=seeds)
        bad = [r for r in man["runs"] if r["rc"] != 0]
        print(report(out, run_planted=not a.no_planted))
        if bad:
            print(f"[arms] {len(bad)} arm(s) exited non-zero: " + ", ".join(f"{r['arm']} s{r['seed']} ({r['log']})" for r in bad))
            return 1
    else:
        print(report(out, run_planted=not a.no_planted))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
