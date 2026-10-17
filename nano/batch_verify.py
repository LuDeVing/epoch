"""Rung 5: full fixed-budget training of every checked candidate in a run's pool, examined by the
harness, against a pooled baseline, with staged seeds and a statistical verdict.

Every training run goes through nano/launch.py (train shards only, no network, wall-clock cap from
the baseline's own full-run time times the candidate's step ratio) and is then examined by
nano/exam.py on the saved weights: the candidate's own number is only a self-report, compared with
the exam and failed on mismatch.

Baseline seeds live in <lab>/runs/nano_baseline_full/<baseline version>/seed<N>/ and are shared by
every run, so the spread estimate grows over time. `--baseline-seeds N` makes sure N exist.

Seeds per candidate (serial on the single GPU), best extrapolated long-run z first:
  seed 0 for every candidate; a pre-declared futility stop after seed 1 (both seeds worse than the
  baseline's worst); then seeds up to `--max-seeds` as long as the candidate is still "promising" or
  "close_call" and time remains. Adding or stopping seeds on the evidence is SAFE because the verdict
  is an anytime-valid e-process (nano/verdict.py sequential_verdict), not a p-value.
Tiers: verified (E >= 1/alpha for the margin, >= 3 seeds); stackable (smaller margin, E >= 20, rung
gaps of one sign: composition and promotion-by-accumulation only); close_call; promising; fail.
e-BH across the night's candidates controls the false-discovery rate. Controls (placebos, known
winners, a known loser; nano/controls.py) can be sent through the same verdict with `--controls`,
which measures the night's own false-positive rate and power. `--hours` stops starting new runs.
Composites of disjoint verified/stackable winners are queued for the next night with `--compose`.

Usage:
  python -m nano.batch_verify --run D:/AGI-lab/runs/<run> [--baseline-seeds 5] [--max-seeds 5] [--hours 9]
Writes <run>/rung5/results.json, summary.md, REPORT.md (via nano/report.py), appends to
memory/experiments/ledger.jsonl and updates memory/experiments/verified_by_hash.json.
"""
from __future__ import annotations

import argparse
import json
import os
import statistics
import subprocess
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LAB = Path(os.environ.get("HTSA_LAB_ROOT", r"D:\AGI-lab"))
PY = Path(os.environ.get("HTSA_EXEC_PYTHON", str(LAB / ".venv" / "Scripts" / "python.exe")))
BASELINE = ROOT / "nano" / "train.py"
EXAM = ROOT / "nano" / "exam.py"
BASELINE_FULL = LAB / "runs" / "nano_baseline_full"
EXP_LEDGER = LAB / "memory" / "experiments" / "ledger.jsonl"
HASH_MEMORY = LAB / "memory" / "experiments" / "verified_by_hash.json"


def _exam(script: Path, out: Path) -> dict:
    """The exam runs the candidate's model code too, so it goes through the launcher as well: the
    validation split is allowed, network and processes are not, and a wall cap applies."""
    from nano import check as C
    ckpt = out / "model.pt"
    if not ckpt.exists():
        return {"error": "no model.pt was saved (the trainer must save its weights for the exam)"}
    e = out / "exam.json"
    try:
        e.unlink()
    except FileNotFoundError:
        pass
    cmd = [str(PY), "-I", str(C.LAUNCH), "--out", str(out), "--data-dir", str(C.DATA_FULL), "--data-full", str(C.DATA_FULL),
           "--allow-val", "--wall-cap", "1500", "--audit", str(out / "audit_exam.json"),
           str(EXAM), "--candidate", str(script), "--ckpt", str(ckpt), "--out", str(out)]
    try:
        p = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=1800,
                           cwd=str(out), env={**os.environ})
    except subprocess.TimeoutExpired:
        return {"error": "exam timed out"}
    if e.exists():
        return json.loads(e.read_text(encoding="utf-8"))
    return {"error": f"exam did not run (rc {p.returncode}): {p.stderr[-400:]}"}


def train_with_args(script: Path, out: Path, seed: int, tokens: float, timeout_s: int, extra: list[str],
                    wall_cap: float = 0.0) -> dict:
    """train() with extra command-line arguments for the script (used by the tuned-baseline duel)."""
    return train(script, out, seed, tokens, timeout_s, wall_cap=wall_cap, extra=extra)


def train(script: Path, out: Path, seed: int, tokens: float, timeout_s: int, wall_cap: float = 0.0,
          extra: list[str] | None = None) -> dict:
    """One full run plus the exam. Resumable: an existing exam.json with a val_loss is reused."""
    from nano import check as C
    out.mkdir(parents=True, exist_ok=True)
    ex = out / "exam.json"
    if ex.exists():
        d = json.loads(ex.read_text(encoding="utf-8"))
        m = C._metrics(out) or {}
        if d.get("val_loss") is not None and not d.get("mismatch") and not d.get("error") \
                and float(m.get("tokens", 0)) >= tokens * 0.98:   # same budget and a clean exam, or redo
            return {**d, "wall_s": m.get("wall_s"), "tokens": m.get("tokens"), "step_s": (m.get("wall_s") or 0) / max(1, m.get("steps") or 1)}
    r = C._run(script, ["--seed", str(seed), "--tokens", str(tokens), "--out", str(out), *(extra or [])], out, timeout_s, wall_cap=wall_cap)
    (out / "stdout.txt").write_text(r["stdout"], encoding="utf-8")
    (out / "stderr.txt").write_text(r["stderr"], encoding="utf-8")
    if r.get("violations"):
        return {"error": "integrity: " + "; ".join(r["violations"][:4]), "wall_s": r["wall"]}
    if r["timed_out"]:
        return {"error": "wall-clock cap", "wall_s": r["wall"]}
    m = C._metrics(out)
    if m is None:
        return {"error": f"no metrics (rc {r['rc']})", "stderr": r["stderr"][-800:], "wall_s": r["wall"]}
    if float(m.get("tokens", 0)) > tokens * 1.02:
        return {"error": f"trained on {m.get('tokens')} tokens, over the budget {tokens:.0f}", "wall_s": r["wall"]}
    e = _exam(script, out)
    if e.get("error"):
        return {"error": "exam: " + str(e["error"])[:300], "wall_s": r["wall"]}
    if e.get("mismatch"):
        return {"error": f"self-reported val_loss {e.get('self_report')} disagrees with the exam {e.get('val_loss')}",
                "wall_s": r["wall"]}
    return {**e, "wall_s": m.get("wall_s"), "tokens": m.get("tokens"),
            "step_s": (m.get("wall_s") or 0) / max(1, m.get("steps") or 1)}


def summarize(name: str, runs: list[dict]) -> dict:
    vals = [r["val_loss"] for r in runs if r.get("val_loss") is not None]
    return {"name": name, "n": len(vals), "mean": statistics.mean(vals) if vals else None,
            "sd": statistics.stdev(vals) if len(vals) > 1 else 0.0, "vals": vals,
            "errors": [r.get("error") for r in runs if "error" in r],
            "wall_s": sum(r.get("wall_s") or 0 for r in runs)}


def baseline_dir(version: str) -> Path:
    return BASELINE_FULL / version


def baseline_runs(version: str, tokens: float) -> list[dict]:
    """Every finished, examined baseline seed at this token budget and baseline version."""
    out = []
    for d in sorted(baseline_dir(version).glob("seed*")):
        e = d / "exam.json"
        m = d / "metrics.json"
        if e.exists() and m.exists():
            ex, mt = json.loads(e.read_text(encoding="utf-8")), json.loads(m.read_text(encoding="utf-8"))
            if ex.get("val_loss") is not None and float(mt.get("tokens", 0)) >= tokens * 0.98:
                out.append({**ex, "wall_s": mt.get("wall_s"), "tokens": mt.get("tokens")})
    return out


def _load_hash_memory() -> dict:
    try:
        return json.loads(HASH_MEMORY.read_text(encoding="utf-8"))
    except Exception:  # noqa: BLE001
        return {}


def main() -> int:
    from nano import report as R
    from nano import verdict as V
    from nano.version import baseline_version
    ap = argparse.ArgumentParser()
    ap.add_argument("--run", required=True, help="nano loop run folder with pool/")
    ap.add_argument("--tokens", type=float, default=50e6)
    ap.add_argument("--timeout", type=int, default=3 * 3600, help="seconds per training run (backstop)")
    ap.add_argument("--baseline-seeds", type=int, default=5, help="baseline seeds to have in the shared folder")
    ap.add_argument("--max-seeds", type=int, default=5, help="most seeds a candidate may get")
    ap.add_argument("--min-seeds", type=int, default=3, help="seeds before any tier is granted")
    ap.add_argument("--margin", type=float, default=0.005, help="nats a verified win must beat the baseline mean by")
    ap.add_argument("--alpha", type=float, default=0.01, help="verified when the e-value reaches 1/alpha")
    ap.add_argument("--stackable-margin", type=float, default=0.002, help="nats for the stackable tier")
    ap.add_argument("--stackable-alpha", type=float, default=0.05, help="stackable when its e-value reaches 1/this")
    ap.add_argument("--controls", nargs="*", default=None, help="control names to run overnight (default none; 'all' for every available)")
    ap.add_argument("--compose", action="store_true", help="queue composites of disjoint verified/stackable winners into pool/")
    ap.add_argument("--duel", action="store_true", help="tuned-baseline duel for optimiser/schedule/init candidates before their verdict")
    ap.add_argument("--scale-check", action="store_true", help="train verified/stackable winners and the baseline at 2x tokens (seed 0): does the gain hold?")
    ap.add_argument("--hours", type=float, default=None, help="stop starting new runs after this many hours")
    ap.add_argument("--only", nargs="*", default=None, help="candidate ids to run (default: all in pool)")
    ap.add_argument("--max-candidates", type=int, default=None)
    ap.add_argument("--scaling-curve", action="store_true", help="train the baseline at 1.25x, 1.5x and 2x tokens (seed 0) for compute-matched deltas")
    a = ap.parse_args()
    run = Path(a.run)
    out = run / "rung5"
    out.mkdir(parents=True, exist_ok=True)
    version = baseline_version()
    t_start = time.time()

    def time_left() -> bool:
        return a.hours is None or (time.time() - t_start) < a.hours * 3600

    # ---- the pool, best extrapolated long-run z first
    pool = []
    for p in sorted(run.glob("pool/*.py")):
        meta_p = p.with_suffix(".json")
        meta = json.loads(meta_p.read_text(encoding="utf-8")) if meta_p.exists() else {}
        if meta.get("baseline_version", "v1") != version:
            print(f"[rung5] skip {p.stem}: built against baseline {meta.get('baseline_version')} (now {version})")
            continue
        pool.append((p, meta))
    if a.only:
        pool = [(p, m) for p, m in pool if p.stem in set(a.only)]

    def rank(pm):
        m = pm[1].get("metrics", {})
        key = m.get("extrap_z") if m.get("extrap_z") is not None else (m.get("long_gap") if m.get("long_gap") is not None else m.get("learn_gap"))
        return (key is None, key or 0.0)
    pool.sort(key=rank)
    from nano import cost as COST
    pool = COST.interleave_lane(pool, lambda pm: pm[1].get("lane") in ("longshot", "family") or pm[1].get("kind") == "leap", every=5)
    if a.max_candidates:
        pool = pool[: a.max_candidates]
    print(f"[rung5] {len(pool)} candidates at {a.tokens:.0f} tokens; baseline {version}, seeds wanted {a.baseline_seeds}", flush=True)

    # ---- pooled baseline (its own runs also go through the launcher and the exam)
    bdir = baseline_dir(version)
    for s in range(a.baseline_seeds):
        if not time_left():
            break
        train(BASELINE, bdir / f"seed{s}", s, a.tokens, a.timeout, wall_cap=0.0)
    base_list = baseline_runs(version, a.tokens)
    base = summarize("baseline", base_list)
    base_wall = statistics.median([r["wall_s"] for r in base_list if r.get("wall_s")]) if base_list else 0.0
    print(f"[rung5] baseline: n {base['n']} mean {base['mean']} sd {base['sd']} median wall {base_wall:.0f}s", flush=True)
    results: dict = {"tokens": a.tokens, "baseline_version": version, "baseline": base, "candidates": {},
                     "margin": a.margin, "alpha": a.alpha}
    # optional: the baseline's loss-versus-tokens curve, for a compute-matched comparison (N-vium style iso-FLOP
    # baseline trained for proportionally more tokens); one seed per point, so it is a delta, not a verdict
    curve = {1.0: base["mean"]} if base["mean"] is not None else {}
    if a.scaling_curve:
        for mult in (1.25, 1.5, 2.0):
            if not time_left():
                break
            r = train(BASELINE, bdir / f"scale_{mult}", 0, a.tokens * mult, int(a.timeout * mult), wall_cap=0.0)
            if r.get("val_loss") is not None:
                curve[mult] = r["val_loss"]
    results["scaling_curve"] = curve

    def compute_matched_base(ratio: float) -> float | None:
        """Baseline loss at ratio x tokens, log-linear between the measured points."""
        if ratio <= 1.0 or len(curve) < 2:
            return base["mean"]
        import math as _m
        pts = sorted(curve.items())
        for (m0, v0), (m1, v1) in zip(pts, pts[1:]):
            if m0 <= ratio <= m1:
                t = (_m.log(ratio) - _m.log(m0)) / (_m.log(m1) - _m.log(m0))
                return v0 + t * (v1 - v0)
        return pts[-1][1]
    hash_mem = _load_hash_memory()

    def cap_for(meta: dict) -> float:
        ratio = (meta.get("metrics") or {}).get("step_ratio") or 2.0
        return (base_wall * max(1.0, ratio) * 1.25 + 300) if base_wall else 0.0

    def sign_ok(meta: dict) -> bool | None:
        m = meta.get("metrics") or {}
        gaps = [m.get("learn_gap"), m.get("long_gap")]
        gaps = [g for g in gaps if g is not None]
        return (all(g < 0 for g in gaps)) if gaps else None

    def record(cid: str, meta: dict, runs: list[dict], stage: int) -> dict:
        s = summarize(cid, runs)
        v = V.sequential_verdict(s["vals"], base["vals"], margin=a.margin, alpha=a.alpha,
                                 stackable_margin=a.stackable_margin, stackable_alpha=a.stackable_alpha,
                                 min_seeds=a.min_seeds, sign_consistent=sign_ok(meta))
        s.update({"status": v["status"], "p": v.get("p"), "t": v.get("t"), "gain": v.get("gain"), "e": v.get("e"),
                  "e_stack": v.get("e_stack"), "sd_diff_used": v.get("sd_diff_used"),
                  "delta": (s["mean"] - base["mean"]) if (s["mean"] is not None and base["mean"] is not None) else None,
                  "stage": stage, "control": meta.get("control")})
        s.update({k: meta.get(k) for k in ("hypothesis", "card", "operator", "lineage_id", "parent_ids", "node", "arm", "src_hash")})
        s["extrap_z"] = (meta.get("metrics") or {}).get("extrap_z")
        ratio = (meta.get("metrics") or {}).get("step_ratio") or 1.0
        cmb = compute_matched_base(ratio)
        s["step_ratio"] = ratio
        s["cm_delta"] = (s["mean"] - cmb) if (s["mean"] is not None and cmb is not None) else None
        results["candidates"][cid] = s
        (out / "results.json").write_text(json.dumps(results, indent=1), encoding="utf-8")
        if meta.get("src_hash"):
            hash_mem[meta["src_hash"]] = {**hash_mem.get(meta["src_hash"], {}), "rung5": {
                "status": s["status"], "n": s["n"], "mean": s["mean"], "delta": s["delta"], "p": s.get("p"),
                "run": run.name, "cand_id": cid, "baseline_version": version, "ts": time.strftime("%Y-%m-%dT%H:%M:%S")}}
            HASH_MEMORY.parent.mkdir(parents=True, exist_ok=True)
            HASH_MEMORY.write_text(json.dumps(hash_mem, indent=1), encoding="utf-8")
        print(f"[rung5] stage {stage} {cid}: n {s['n']} mean {s['mean']} delta {s['delta']} p {s.get('p')} -> {s['status']} | {s['hypothesis']}", flush=True)
        return s

    # ---- controls go through the same verdict as everything else
    if a.controls is not None:
        from nano import controls as CT
        cdir = run / "controls"
        cdir.mkdir(exist_ok=True)
        wanted = None if (not a.controls or a.controls == ["all"]) else a.controls
        for name, spec in CT.build(BASELINE.read_text(encoding="utf-8"), wanted).items():
            if not spec.get("source"):
                continue
            cp = cdir / f"control_{name}.py"
            cp.write_text(spec["source"], encoding="utf-8")
            (cdir / f"control_{name}.json").write_text(json.dumps({"id": f"control_{name}", "control": name, "hypothesis": spec["hypothesis"],
                                                                   "card": "control", "node": "control", "metrics": {}}), encoding="utf-8")
            pool.append((cp, json.loads((cdir / f"control_{name}.json").read_text(encoding="utf-8"))))

    # ---- optional: tuned-baseline duel for optimiser / schedule / init ideas
    if a.duel:
        from nano import duel as D
        for p, meta in pool:
            if D.is_optimizer_idea(meta):
                meta["duel"] = D.run(p, BASELINE, out / p.stem / "duel", a.tokens, a.timeout)

    # ---- sequential seeds: seed 0 for all, futility stop, then more seeds while still promising
    runs_by: dict[str, list[dict]] = {}
    for p, meta in pool:
        if not time_left():
            break
        runs_by[p.stem] = [train(p, out / p.stem / "seed0", 0, a.tokens, a.timeout, wall_cap=cap_for(meta))]
        record(p.stem, meta, runs_by[p.stem], 1)
    for seed in range(1, a.max_seeds):
        for p, meta in pool:
            s = results["candidates"].get(p.stem)
            if not s or not time_left():
                continue
            if seed == 1 and (s["mean"] is None or (base["mean"] is not None and s["mean"] > max(base["vals"]))):
                continue                                                 # worse than the worst baseline seed: stop
            if seed >= 2 and V.futility(s["vals"], base["vals"]):
                continue
            if seed >= 2 and s["status"] not in ("promising", "close_call", "stackable"):
                continue                                                 # verified or failed: done
            runs_by[p.stem].append(train(p, out / p.stem / f"seed{seed}", seed, a.tokens, a.timeout, wall_cap=cap_for(meta)))
            record(p.stem, meta, runs_by[p.stem], seed + 1)

    # ---- false-discovery control across the night, and the controls' report
    evals = {cid: (s.get("e") or 0.0) for cid, s in results["candidates"].items() if s["n"] >= a.min_seeds}
    passed = V.e_bh(evals, a.alpha)
    for cid, s in results["candidates"].items():
        s["ebh"] = cid in passed
        if s["status"] == "verified" and not s["ebh"]:
            s["status"] = "close_call"                                   # verified alone, not after multiplicity control
    if a.controls is not None:
        from nano import controls as CT
        results["controls"] = {}
        for cid, s in results["candidates"].items():
            if s.get("control"):
                results["controls"][s["control"]] = CT.judge_overnight(s["control"], s["status"])
        (out / "results.json").write_text(json.dumps(results, indent=1), encoding="utf-8")

    # ---- scale-transfer check: a winner must hold at double the budget (seed 0, both sides)
    if a.scale_check:
        b2 = train(BASELINE, bdir / "scale_2.0", 0, a.tokens * 2, int(a.timeout * 2), wall_cap=0.0)
        for p, meta in pool:
            s = results["candidates"].get(p.stem)
            if not s or s["status"] not in ("verified", "stackable") or meta.get("control") or not time_left():
                continue
            c2 = train(p, out / p.stem / "scale_2.0", 0, a.tokens * 2, int(a.timeout * 2), wall_cap=cap_for(meta) * 2)
            if b2.get("val_loss") is not None and c2.get("val_loss") is not None:
                s["scale_delta_2x"] = round(c2["val_loss"] - b2["val_loss"], 5)
                s["scale_holds"] = s["scale_delta_2x"] < 0
                (out / "results.json").write_text(json.dumps(results, indent=1), encoding="utf-8")
                print(f"[rung5] scale check {p.stem}: delta at 2x tokens {s['scale_delta_2x']} -> {'holds' if s['scale_holds'] else 'does not hold'}", flush=True)

    # ---- composites of disjoint winners for the next night
    if a.compose:
        from nano import compose as CP
        wins = [(p, m) for p, m in pool if results["candidates"].get(p.stem, {}).get("status") in ("verified", "stackable") and not m.get("control")]
        made = 0
        for i, (pa, ma) in enumerate(wins):
            for pb, mb in wins[i + 1:]:
                sa = set((ma.get("metrics") or {}).get("changed_symbols") or [])
                sb = set((mb.get("metrics") or {}).get("changed_symbols") or [])
                if sa & sb - {"<module>", "Config"}:
                    continue
                r = CP.compose(BASELINE.read_text(encoding="utf-8"), pa.read_text(encoding="utf-8"), pb.read_text(encoding="utf-8"))
                if not r:
                    continue
                cid = f"{pa.stem}_{pb.stem}"
                (run / "pool" / f"{cid}.py").write_text(r["source"], encoding="utf-8")
                (run / "pool" / f"{cid}.json").write_text(json.dumps({"id": cid, "card": "compose", "node": "recipe",
                    "hypothesis": f"{ma.get('hypothesis')} AND {mb.get('hypothesis')}"[:300], "parent_ids": [pa.stem, pb.stem],
                    "src_hash": None, "arm": ma.get("arm"), "baseline_version": version, "metrics": {}, "queued_by": "batch_verify --compose"}), encoding="utf-8")
                made += 1
        print(f"[rung5] queued {made} composites of disjoint winners into pool/ for the next night", flush=True)

    # ---- ledger, summary, report
    EXP_LEDGER.parent.mkdir(parents=True, exist_ok=True)
    with EXP_LEDGER.open("a", encoding="utf-8") as f:
        for cid, s in results["candidates"].items():
            f.write(json.dumps({"ts": time.strftime("%Y-%m-%dT%H:%M:%S"), "run": run.name, "cand_id": cid,
                                "arm": s.get("arm"), "card": s.get("card"), "operator": s.get("operator"),
                                "lineage_id": s.get("lineage_id"), "parent_ids": s.get("parent_ids"), "node": s.get("node"),
                                "hypothesis": s.get("hypothesis"), "src_hash": s.get("src_hash"), "tokens": a.tokens,
                                "n_seeds": s["n"], "vals": s["vals"], "mean": s["mean"], "sd": s["sd"],
                                "baseline_version": version, "baseline_mean": base["mean"], "baseline_sd": base["sd"],
                                "baseline_n": base["n"], "delta": s["delta"], "gain": s.get("gain"), "p": s.get("p"),
                                "e": s.get("e"), "e_stack": s.get("e_stack"), "ebh": s.get("ebh"), "control": s.get("control"),
                                "extrap_z": s.get("extrap_z"), "step_ratio": s.get("step_ratio"), "cm_delta": s.get("cm_delta"),
                                "status": s["status"], "errors": s.get("errors")}) + "\n")
    lines = [f"# Rung 5 results: {run.name}", "",
             f"tokens per run {a.tokens:.0f}; baseline {version}: val_loss mean {base['mean']} sd {base['sd']} (n={base['n']}, pooled, examined by the harness)",
             f"verified = e-value >= {1 / a.alpha:.0f} for a margin of {a.margin} nats with >= {a.min_seeds} seeds (anytime-valid; e-BH across the night); "
             f"stackable = e-value >= {1 / a.stackable_alpha:.0f} for {a.stackable_margin} nats with rung gaps of one sign", "",
             "| candidate | arm | part | seeds | mean val_loss | delta | compute-matched delta | e | p | status | hypothesis |", "|---|---|---|---|---|---|---|---|---|---|---|"]
    for cid, s in sorted(results["candidates"].items(), key=lambda kv: (kv[1]["mean"] is None, kv[1]["mean"] or 9)):
        lines.append(f"| {cid} | {s.get('arm')} | {s.get('node')} | {s['n']} | {s['mean']} | {s['delta']} | {s.get('cm_delta')} | {s.get('e')} | {s.get('p')} | {s['status']} | {s.get('hypothesis')} |")
    if results.get("controls"):
        lines += ["", "## Controls", ""] + [f"- {k}: {'ok' if v['ok'] else 'PROBLEM'}: {v['note']}" for k, v in results["controls"].items()]
    (out / "summary.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines))
    try:
        R.write(run)
    except Exception as e:  # noqa: BLE001
        print(f"[rung5] report failed: {e}")
    try:                                    # outcome lessons: the overnight verdicts are what they are made from
        from nano import lessons as LS
        n = LS.update_from_run(run, LAB / "memory" / "lessons.jsonl", version)
        print(f"[rung5] lessons: {n}")
    except Exception as e:  # noqa: BLE001
        print(f"[rung5] lessons not updated: {e}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
