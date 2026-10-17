"""Portfolio method v2 on ARC, with a plain best-of-n baseline at equal tokens in the same run.
Design: research_notes/portfolio_improvements/03_SYNTHESIS.md.

Method v2, per puzzle:
  1. Plain attempts (plain arm's exact prompt), up to k_plain; stop as soon as any two passing attempts agree on the
     test answer (adaptive consistency).
  2. If not stopped: inventive attempts (re-describe, rival rule).
  3. Check every program on the examples. If none passes: one revision per best near miss with the real diffs.
  4. Selection: passing programs (test answer != test input) grouped by test answer; groups ranked by symmetry
     consistency (number of rotations/mirrors s with f(s(x)) == s(f(x)) on all example and test inputs), then group
     size, then shortest program. If the top two groups are still level, an anchored check: the model predicts the
     test output directly from the examples (without seeing candidates); the group closest to it wins.
  5. Two answers (official ARC scoring): the top two groups. Nothing passes: the two most common plain answers.
Baseline, same puzzle: its own independent plain samples (plain arm's prompt) until its tokens reach the method's,
never the method's attempts; selection = standard majority among passing programs, two answers. Also reported: plain
one answer (the baseline's first sample). --reuse-method-plain restores the earlier baseline (the method's plain
attempts plus extra samples), kept only to reproduce arc1fresh-v2 and arc1large-v2: when the method stops early
after two agreeing plain attempts that baseline selects from the identical attempts, so the tie is tautological.
v2_summary.md reports how many puzzles stopped early and on how many the two arms saw identical attempts.

    HTSA_MODEL=haiku HTSA_ARC_SET=arc1fresh python -m harness.portfolio_v2 --batch arc1fresh-v2 --split fresh --items 60
"""
from __future__ import annotations

import argparse
import json
import os
import re
import threading
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from . import config
from .arms.plain import arc_data, build_prompt, parse_program
from .portfolio_arc import DIVERGENT, FORMAT, HEAD, call
from .schemas import strip_key


def _rot(g):
    return [list(r) for r in zip(*g[::-1])]


SYMS = [_rot, lambda g: _rot(_rot(g)), lambda g: _rot(_rot(_rot(g))), lambda g: [r[::-1] for r in g],
        lambda g: g[::-1], lambda g: [list(r) for r in zip(*g)]]


def run_prog(ex, prog, clean):
    ins = [p["input"] for p in clean["train"]] + [clean["test_input"]]
    n = len(ins)
    allin = ins + [s(x) for s in SYMS for x in ins]
    res = ex.execute(prog, allin)
    o, errs = res["outputs"], res["errors"]
    demo = ex.demo_from_outputs(clean["train"], o[: n - 1], errs[: n - 1])
    base = o[:n]
    sym = 0
    for j, s in enumerate(SYMS):
        so = o[n * (j + 1): n * (j + 2)]
        try:
            sym += all(b is not None and x == s(b) for b, x in zip(base, so))
        except Exception:  # noqa: BLE001  (malformed output grid)
            pass
    return {"passed": demo["matched"], "total": demo["total"], "diffs": demo["diffs"][:2], "pred": base[-1], "sym": sym}


def parse_grid(text):
    blocks = re.findall(r"```[a-z]*\n(.*?)```", text or "", re.S)
    src = blocks[-1] if blocks else (text or "")
    rows = []
    for line in src.strip().splitlines():
        nums = re.findall(r"\d", line)
        if nums and re.fullmatch(r"[\d\s,\[\]]+", line.strip()):
            rows.append([int(x) for x in nums])
    return rows or None


def similarity(a, b):
    if not a or not b or len(a) != len(b) or any(len(x) != len(y) for x, y in zip(a, b)):
        return 0.0
    cells = sum(len(r) for r in a)
    return sum(p == q for x, y in zip(a, b) for p, q in zip(x, y)) / max(1, cells)


def groups_of(cands, test_input, key):
    g = {}
    for c in cands:
        if c["passed"] == c["total"] and c["pred"] is not None and c["pred"] != test_input:
            g.setdefault(json.dumps(c["pred"]), []).append(c)
    return sorted(g.values(), key=key)


def solve(item, args, out_dir):
    from . import arc_exec as EX
    clean = strip_key(item)
    t_in = clean["test_input"]
    data = arc_data(clean, list(range(len(clean["train"]))))
    log_dir = out_dir / "calls" / item["id"]
    log_dir.mkdir(parents=True, exist_ok=True)
    cands = []

    def attempt(kind, name, prompt):
        text, tok = call(prompt, args, f"{kind}_{name}", log_dir)
        prog = parse_program(text)
        c = {"kind": kind, "name": name, "len": len(prog or ""), "tokens": tok, "passed": 0, "total": len(clean["train"]),
             "pred": None, "sym": 0, "prog": prog}
        if prog:
            c.update(run_prog(EX, prog, clean))
        cands.append(c)
        return c

    def agree2(cs):
        cnt = Counter(json.dumps(c["pred"]) for c in cs if c["passed"] == c["total"] and c["pred"] is not None
                      and c["pred"] != t_in)
        return bool(cnt) and cnt.most_common(1)[0][1] >= 2

    plain_prompt = build_prompt(clean, list(range(len(clean["train"]))))
    stopped = False
    for i in range(args.k_plain):
        attempt("plain", str(i), plain_prompt)
        if args.early_stop and agree2(cands):
            stopped = True
            break
    if not stopped:
        for name in list(DIVERGENT)[: args.k_div]:
            attempt("divergent", name, HEAD + data + "\n" + DIVERGENT[name] + " Then " + FORMAT[0].lower() + FORMAT[1:])
    if not any(c["passed"] == c["total"] and c["pred"] is not None for c in cands):
        for c in sorted([c for c in cands if c["prog"]], key=lambda c: -c["passed"])[: args.k_revise]:
            prompt = (HEAD + data + "\n\nA previous program for this task:\n```python\n" + c["prog"] + "\n```\n"
                      f"It reproduced {c['passed']} of {c['total']} example outputs. Where its outputs differ from the expected "
                      f"ones:\n{json.dumps(c['diffs'])[:3000]}\n\nWork out from these differences what the rule really is, "
                      "check the corrected rule against every example, then " + FORMAT[0].lower() + FORMAT[1:])
            attempt("revise", c["kind"] + "_" + c["name"], prompt)

    # method selection
    G = groups_of(cands, t_in, key=lambda g: (-max(c["sym"] for c in g), -len(g), min(c["len"] for c in g)))
    how, anchored = "", None
    if len(G) >= 2:
        s0 = (max(c["sym"] for c in G[0]), len(G[0]))
        s1 = (max(c["sym"] for c in G[1]), len(G[1]))
        if s0 == s1 and args.anchored:
            text, tok = call(HEAD + data + "\nWork out the rule from the examples, check it against every example, then "
                             "write the output grid for the test input as rows of digits separated by spaces inside one "
                             "code block.", args, "anchored", log_dir)
            cands.append({"kind": "anchored", "name": "direct", "tokens": tok, "pred": None, "passed": 0, "total": 1,
                          "len": 0, "sym": 0, "prog": None})
            anchored = parse_grid(text)
            tied = [g for g in G if (max(c["sym"] for c in g), len(g)) == s0]
            rest = [g for g in G if g not in tied]
            tied.sort(key=lambda g: -similarity(g[0]["pred"], anchored))
            G = tied + rest
            how = "anchored tie-break; "
    if G:
        answers = [G[0][0]["pred"]] + ([G[1][0]["pred"]] if len(G) > 1 else [])
        how += f"top group sym {max(c['sym'] for c in G[0])}, size {len(G[0])} of {sum(len(g) for g in G)} passing"
    else:
        pl = Counter(json.dumps(c["pred"]) for c in cands if c["kind"] == "plain" and c["pred"] is not None)
        answers = [json.loads(a) for a, _ in pl.most_common(2)]
        how += "nothing passed; plain answers"
    m_tokens = sum(c["tokens"] for c in cands)

    # baseline: plain samples only, up to the method's tokens, standard majority among passing; its own draws
    reuse = bool(getattr(args, "reuse_method_plain", False))
    base = [c for c in cands if c["kind"] == "plain"] if reuse else []
    n_reused = len(base)
    while sum(c["tokens"] for c in base) < m_tokens and len(base) < args.k_base_max:
        base.append(attempt("plainextra", str(len(base)), plain_prompt))
        cands.remove(base[-1])
    identical = n_reused > 0 and len(base) == n_reused     # baseline saw exactly the method's plain attempts
    BG = groups_of(base, t_in, key=lambda g: (-len(g), min(c["len"] for c in g)))
    if BG:
        b_answers = [BG[0][0]["pred"]] + ([BG[1][0]["pred"]] if len(BG) > 1 else [])
    else:
        bc = Counter(json.dumps(c["pred"]) for c in base if c["pred"] is not None)
        b_answers = [json.loads(a) for a, _ in bc.most_common(2)]

    key = item["test_output"]                                   # read by this scorer only
    first = base[0]["pred"] if base else None
    return {"id": item["id"], "how": how, "stopped_early": stopped, "base_mode": "reuse" if reuse else "independent",
            "n_base_reused": n_reused, "identical_arms": identical,
            "method_top1": bool(answers) and answers[0] == key, "method_top2": key in answers,
            "base_top1": bool(b_answers) and b_answers[0] == key, "base_top2": key in b_answers,
            "plain_one": first == key, "any_right": any(c["pred"] == key for c in cands + base),
            "method_tokens": m_tokens, "base_tokens": sum(c["tokens"] for c in base), "n_base": len(base),
            "anchored_right": anchored == key if anchored is not None else None,
            "attempts": [{"kind": c["kind"], "name": c["name"], "passed": f"{c['passed']}/{c['total']}", "sym": c["sym"],
                          "right": c["pred"] == key, "tokens": c["tokens"]} for c in cands],
            "base_attempts": [{"name": c["name"], "passed": f"{c['passed']}/{c['total']}", "right": c["pred"] == key}
                              for c in base]}


def identical_arms(r) -> bool:
    """The baseline saw exactly the method's plain attempts (no draws of its own). Rows written before the field
    existed were all in reuse mode: identical when n_base equals the method's plain attempt count."""
    if "identical_arms" in r:
        return bool(r["identical_arms"])
    return r.get("n_base") == sum(1 for a in r.get("attempts", []) if a.get("kind") == "plain")


def summary(rows, path):
    n = len(rows)

    def s(k):
        return sum(1 for r in rows if r[k])

    def tok(k):
        return sum(r[k] for r in rows) / max(1, n)
    w = sum(1 for r in rows if r["method_top2"] and not r["base_top2"])
    l = sum(1 for r in rows if r["base_top2"] and not r["method_top2"])
    lines = [f"# Portfolio v2 vs plain at equal tokens ({n} puzzles, {path.name}), model {config.DEFAULT_MODEL}", "",
             "| arm | solved, two answers | solved, one answer | tokens per puzzle |", "|---|---|---|---|",
             f"| method v2 | {s('method_top2')}/{n} | {s('method_top1')}/{n} | {tok('method_tokens'):,.0f} |",
             f"| plain best-of-n, same tokens, majority vote | {s('base_top2')}/{n} | {s('base_top1')}/{n} | {tok('base_tokens'):,.0f} |",
             f"| plain, one answer | | {s('plain_one')}/{n} | |",
             f"| any attempt right | {s('any_right')}/{n} | | |", "",
             f"Paired, two answers: method right and baseline wrong on {w} puzzles; the reverse on {l}."]
    stopped = sum(1 for r in rows if r.get("stopped_early"))
    same = sum(1 for r in rows if identical_arms(r))
    modes = sorted({r.get("base_mode", "reuse") for r in rows})
    lines += ["", f"Method stopped early (two agreeing plain attempts) on {stopped} of {n} puzzles. Baseline mode: "
              f"{', '.join(modes)}. The two arms saw identical attempts on {same} of {n} puzzles"
              + (" (baseline reused the method's plain attempts: on those puzzles a tie is by construction, not "
                 "evidence)." if same else ".")]
    return "\n".join(lines) + "\n"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--batch", required=True)
    ap.add_argument("--items", type=int, default=60)
    ap.add_argument("--split", default="fresh")
    ap.add_argument("--k-plain", type=int, default=4)
    ap.add_argument("--k-div", type=int, default=2)
    ap.add_argument("--k-revise", type=int, default=2)
    ap.add_argument("--k-base-max", type=int, default=10)
    ap.add_argument("--no-early-stop", dest="early_stop", action="store_false")
    ap.add_argument("--no-anchored", dest="anchored", action="store_false")
    ap.add_argument("--reuse-method-plain", action="store_true",
                    help="old baseline: start from the method's plain attempts (reproduces the earlier v2 batches)")
    ap.add_argument("--summary-only", action="store_true", help="rewrite v2_summary.md from v2_runs.jsonl, no calls")
    ap.add_argument("--effort", default=os.environ.get("HTSA_PLAIN_EFFORT", "medium"))
    ap.add_argument("--backend", default=None)
    ap.add_argument("--workers", type=int, default=3)
    args = ap.parse_args()
    args.backend = args.backend or config.default_backend()
    path = Path(config.BENCHMARKS["arc"]["file"])
    items = [json.loads(l) for l in path.read_text(encoding="utf-8").splitlines() if l.strip()]
    items = [it for it in items if it.get("split") == args.split][: args.items]
    out_dir = Path(config.RESULTS_DIR) / args.batch
    out_dir.mkdir(parents=True, exist_ok=True)
    rows_path = out_dir / "v2_runs.jsonl"
    done = {}
    if rows_path.exists():
        for l in rows_path.read_text(encoding="utf-8").splitlines():
            if l.strip():
                r = json.loads(l)
                done[r["id"]] = r
    lock = threading.Lock()
    print(f"[v2] {len(items)} puzzles, model {config.DEFAULT_MODEL}, effort {args.effort}", flush=True)

    def work(it):
        try:
            r = solve(it, args, out_dir)
        except Exception as e:  # noqa: BLE001
            print(f"[v2] {it['id']} error {type(e).__name__}: {e}", flush=True)
            return
        with lock:
            with rows_path.open("a", encoding="utf-8") as f:
                f.write(json.dumps(r) + "\n")
            done[r["id"]] = r
            rows = list(done.values())
            print(f"[v2] {len(done)}/{len(items)} {r['id']}: method {r['method_top2']} base {r['base_top2']} "
                  f"plain1 {r['plain_one']} | totals method {sum(x['method_top2'] for x in rows)} base "
                  f"{sum(x['base_top2'] for x in rows)} plain1 {sum(x['plain_one'] for x in rows)} | tokens "
                  f"{r['method_tokens']:,}/{r['base_tokens']:,} ({r['how']})", flush=True)
    if not args.summary_only:
        with ThreadPoolExecutor(max_workers=args.workers) as ex:
            list(ex.map(work, [it for it in items if it["id"] not in done]))
    rows = [done[it["id"]] for it in items if it["id"] in done]
    text = summary(rows, path)
    (out_dir / "v2_summary.md").write_text(text, encoding="utf-8")
    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
