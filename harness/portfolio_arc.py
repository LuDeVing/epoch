"""Portfolio method on ARC: both kinds of attempts on every puzzle, one shared check, behaviour-clustered selection.
Design: research_notes/thinking_modes/00_SYNTHESIS.md.

Per puzzle:
  1. Plain attempts (the convergent floor): the plain arm's own prompt, unchanged, k_plain times.
     Early stop: if the first two pass every example and agree on the test answer, finish (probe agreement +
     a passing check = the "feeling of rightness" signal).
  2. Divergent attempts (the safety net): k_div attempts that re-describe the grid in another representation or
     pose a rival rule, using the logical procedure (rival rule + discriminating input, simplicity as a default).
  3. Every candidate is checked on the examples (free). If none passes, one revision per best near miss, shown its
     actual outputs against the expected ones (execution feedback).
  4. Selection (dedup.vote, the same rule think.py uses): passing candidates grouped by test answer; the largest
     group wins, plain and divergent attempts alike; on a tie, agreement on rotated/mirrored copies of the test input,
     then the simplest program (00_IDEAS.md item 16). If nothing passes, the answer of the plain attempts' largest
     group (never worse than plain's own reading).
solve() sees only the key-stripped item; score() reads the answer key after every model call of the puzzle.
The plain arm's answers for the same puzzles come from an earlier harness.bench batch (--plain-from), one row per
puzzle; that batch must use the same HTSA_PLAIN_EFFORT (runs.jsonl does not record the effort).

    $env:HTSA_LAB_ROOT = "D:\\AGI-lab"; $env:HTSA_MODEL = "haiku"; $env:HTSA_ARC_SET = "arc2"
    python -m harness.portfolio_arc --batch arc2-portfolio --items 10 --plain-from D:\\AGI-lab\\results\\arc2-haiku-plain
"""
from __future__ import annotations

import argparse
import json
import os
import threading
import time
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from . import config, llm, score as SC
from .arms.plain import arc_data, build_prompt, parse_program
from .schemas import strip_key
from .think import dedup as DD

FORMAT = ("Give your final answer as exactly one python code block that defines transform(grid) -> grid. The argument is "
          "the input grid as a list of lists of ints; the function returns the output grid in the same form, uses only the "
          "python standard library, and should reproduce every example output from its input.")

HEAD = ("Task: find the rule that maps each example input grid to its output grid, then write a program that applies it "
        "to the test input.\nEach grid is shown as rows of integers 0-9 separated by spaces.\n\n")

PLAIN = ("Reason step by step about the rule that turns each example input into its output. Then " + FORMAT[0].lower() + FORMAT[1:])

DIVERGENT = {
    "rerepresent": ("Describe the grids in a different way than the obvious one: as objects and how each one moves or changes, "
                    "or as lines and paths, or as regions and their boundaries, or as counts and comparisons, or as symmetry "
                    "and repetition. Pick the description under which the change from input to output is simplest, state the "
                    "rule in one sentence, and check it against every example before coding."),
    "rival": ("Write down the rule that first comes to mind, then a rival rule that also fits every example but would give a "
              "different output somewhere. Find the feature of the test input on which the two disagree and decide which rule "
              "the examples really support, preferring the simpler one unless the examples rule it out. Check the chosen "
              "rule against every example before coding."),
    "helper": ("First solve a smaller helper problem: what happens in the smallest example, or to a single object, or along a "
               "single row? Build the full rule from that, check it against every example, and only then write the code."),
}


def call(prompt, args, tag, log_dir):
    r = llm.call(prompt, role="plain", call_id=f"{tag}_{int(time.time() * 1000) % 10**9}", backend=args.backend,
                 log_dir=log_dir, meta={"card": tag}, effort=args.effort or None)
    return (r.text or ""), int(r.usage.total_tokens)


def run_prog(ex, prog, clean):
    ins = [p["input"] for p in clean["train"]]
    t = clean["test_input"]
    res = ex.execute(prog, ins + [t] + ex.augmented(t))
    outs, errs = res["outputs"], res["errors"]
    demo = ex.demo_from_outputs(clean["train"], outs[: len(ins)], errs[: len(ins)])
    return {"passed": demo["matched"], "total": demo["total"], "diffs": demo["diffs"][:2], "pred": outs[len(ins)],
            "behaviour": ex.aug_key(outs[len(ins) + 1:])}


def select(cands):
    """Passing candidates by dedup.vote (test answer, then augmented agreement, then shortest); else plain majority.
    Returns (chosen candidate or None, how, passing candidates)."""
    full = [c for c in cands if c["pred"] is not None and c["passed"] == c["total"]]
    if full:
        chosen, k, _n = DD.vote(full, lambda c: c["pred"], lambda c: len(c["prog"] or ""), lambda c: c["behaviour"])
        return chosen, f"vote {k} of {len(full)} passing", full
    plain = [c for c in cands if c["kind"] == "plain" and c["pred"] is not None]
    votes = Counter(json.dumps(c["pred"]) for c in plain)
    chosen = next((c for c in plain if json.dumps(c["pred"]) == votes.most_common(1)[0][0]), None) if votes else None
    return chosen, "no candidate passed; plain majority", full


def solve(clean, args, out_dir):
    """All model calls and the selection for one puzzle. Sees only the key-stripped item (no test_output)."""
    from . import arc_exec as EX
    assert "test_output" not in clean, "solve() must get the key-stripped item"
    data = arc_data(clean, list(range(len(clean["train"]))))
    log_dir = out_dir / "calls" / clean["id"]
    log_dir.mkdir(parents=True, exist_ok=True)
    cands, tokens = [], 0

    def attempt(kind, name, prompt):
        nonlocal tokens
        text, tok = call(prompt, args, f"{kind}_{name}", log_dir)
        tokens += tok
        prog = parse_program(text)
        c = {"kind": kind, "name": name, "prog": prog, "passed": 0, "total": len(clean["train"]), "pred": None, "behaviour": None}
        if prog:
            c.update(run_prog(EX, prog, clean))
        cands.append(c)
        return c

    plain_prompt = build_prompt(clean, list(range(len(clean["train"]))))   # the plain arm's exact prompt
    # 1. plain attempts, with early stop when the first two pass and agree
    stopped_early = False
    for i in range(args.k_plain):
        attempt("plain", str(i), plain_prompt)
        if i == 1 and args.early_stop:
            a, b = cands[0], cands[1]
            if all(c["pred"] is not None and c["passed"] == c["total"] for c in (a, b)) and a["pred"] == b["pred"]:
                stopped_early = True
                break
    # 2. divergent attempts
    if not stopped_early:
        for name in list(DIVERGENT)[: args.k_div]:
            attempt("divergent", name, HEAD + data + "\n" + DIVERGENT[name] + " Then " + FORMAT[0].lower() + FORMAT[1:])
    # 3. revision from execution feedback when nothing passes
    full = [c for c in cands if c["pred"] is not None and c["passed"] == c["total"]]
    if not full and not stopped_early:
        near = sorted([c for c in cands if c["prog"]], key=lambda c: -c["passed"])[: args.k_revise]
        for c in near:
            fb = json.dumps(c["diffs"])[:3000]
            prompt = (HEAD + data + "\n\nA previous program for this task:\n```python\n" + c["prog"] + "\n```\n"
                      f"It reproduced {c['passed']} of {c['total']} example outputs. Where its outputs differ from the expected "
                      f"ones:\n{fb}\n\nWork out from these differences what the rule really is, check the corrected rule against "
                      "every example, then " + FORMAT[0].lower() + FORMAT[1:])
            attempt("revise", c["kind"] + "_" + c["name"], prompt)
    # 4. selection
    chosen, how, full = select(cands)
    return {"id": clean["id"], "answer": chosen["pred"] if chosen else None, "how": how, "tokens": tokens,
            "stopped_early": stopped_early, "n": len(cands), "n_pass": len(full),
            "attempts": [{"kind": c["kind"], "name": c["name"], "passed": f"{c['passed']}/{c['total']}", "pred": c["pred"]}
                         for c in cands]}


def right(item, pred) -> bool:
    """score.is_correct on an ARC grid (the item rows of the ARC file may lack the benchmark field)."""
    return SC.is_correct({**item, "benchmark": "arc"}, pred)


def score(item, rec):
    """Read the answer key once the puzzle's model calls are done; the written row carries no predicted grids."""
    attempts = [{k: v for k, v in a.items() if k != "pred"} | {"right": right(item, a["pred"])} for a in rec["attempts"]]
    return {k: v for k, v in rec.items() if k not in ("answer", "attempts")} | {
        "solved": right(item, rec["answer"]), "any_right": any(a["right"] for a in attempts), "attempts": attempts}


def plain_rows(plain_from, items) -> dict:
    """One plain-arm row per puzzle from an earlier harness.bench batch: replicate 0 if present, else the first row,
    so replicates do not inflate the denominator. Same rule in arc_think."""
    ids = {it["id"] for it in items}
    last = {}                          # last row per run_id: a retried run replaces its error row
    for l in (Path(plain_from) / "runs.jsonl").read_text(encoding="utf-8").splitlines():
        if not l.strip():
            continue
        r = json.loads(l)
        if r.get("arm") != "plain" or r.get("item_id") not in ids:
            continue
        last[r.get("run_id") or len(last)] = r
    out = {}
    for r in last.values():
        old = out.get(r["item_id"])
        if old is None or (int(r.get("replicate") or 0) == 0 and int(old.get("replicate") or 0) != 0):
            out[r["item_id"]] = r
    return out


def plain_line(plain_from, items) -> str:
    pl = plain_rows(plain_from, items)
    by_id = {it["id"]: it for it in items}
    ok = sum(1 for k, r in pl.items() if right(by_id[k], r.get("answer")))
    return (f"| plain (one answer) | {ok}/{len(pl)} | "
            f"{sum(int(r.get('spent_tokens') or 0) for r in pl.values()) / max(1, len(pl)):,.0f} |")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--batch", required=True)
    ap.add_argument("--items", type=int, default=10)
    ap.add_argument("--split", default="dev-tune")
    ap.add_argument("--k-plain", type=int, default=4)
    ap.add_argument("--k-div", type=int, default=2)
    ap.add_argument("--k-revise", type=int, default=2)
    ap.add_argument("--no-early-stop", dest="early_stop", action="store_false")
    ap.add_argument("--effort", default=os.environ.get("HTSA_PLAIN_EFFORT", ""))   # same default as arms/plain
    ap.add_argument("--backend", default=None)
    ap.add_argument("--workers", type=int, default=2)
    ap.add_argument("--plain-from", default=None)
    args = ap.parse_args()
    args.backend = args.backend or config.default_backend()
    path = Path(config.BENCHMARKS["arc"]["file"])
    items = [json.loads(l) for l in path.read_text(encoding="utf-8").splitlines() if l.strip()]
    items = [it for it in items if it.get("split") == args.split][: args.items]
    out_dir = Path(config.RESULTS_DIR) / args.batch
    out_dir.mkdir(parents=True, exist_ok=True)
    rows_path = out_dir / "portfolio_runs.jsonl"
    done = {}
    if rows_path.exists():
        for l in rows_path.read_text(encoding="utf-8").splitlines():
            if l.strip():
                r = json.loads(l)
                done[r["id"]] = r
    lock = threading.Lock()
    print(f"[portfolio] {len(items)} puzzles, {args.k_plain} plain + {args.k_div} divergent, effort {args.effort or 'default'}, model {config.DEFAULT_MODEL}", flush=True)

    def work(it):
        r = score(it, solve(strip_key(it), args, out_dir))
        with lock:
            with rows_path.open("a", encoding="utf-8") as f:
                f.write(json.dumps(r) + "\n")
            done[r["id"]] = r
            print(f"[portfolio] {len(done)}/{len(items)} {r['id']}: solved {r['solved']} ({r['how']}), any right {r['any_right']}, "
                  f"passing {r['n_pass']}/{r['n']}, tokens {r['tokens']:,}", flush=True)
    with ThreadPoolExecutor(max_workers=args.workers) as ex:
        list(ex.map(work, [it for it in items if it["id"] not in done]))
    rows = [done[it["id"]] for it in items if it["id"] in done]
    lines = [f"# Portfolio method on {path.name} ({len(rows)} puzzles), model {config.DEFAULT_MODEL}", "",
             "| arm | solved | tokens per puzzle |", "|---|---|---|",
             f"| portfolio ({args.k_plain} plain + {args.k_div} divergent, check, vote) | {sum(r['solved'] for r in rows)}/{len(rows)} | "
             f"{sum(r['tokens'] for r in rows) / max(1, len(rows)):,.0f} |"]
    # in-run baseline: the first plain attempt is exactly plain Haiku's single answer at the same effort
    first = sum(1 for r in rows if r["attempts"] and r["attempts"][0]["right"])
    lines.append(f"| plain, one answer (first plain attempt, same run, same effort) | {first}/{len(rows)} | |")
    lines.append(f"| any attempt right (upper bound for selection) | {sum(r['any_right'] for r in rows)}/{len(rows)} | |")
    if args.plain_from:
        lines.append(plain_line(args.plain_from, items))
    kinds = Counter()
    rights = Counter()
    for r in rows:
        for a in r["attempts"]:
            kinds[a["kind"]] += 1
            rights[a["kind"]] += a["right"]
    lines += ["", "right answers per attempt kind: " + ", ".join(f"{k} {rights[k]}/{kinds[k]}" for k in kinds)]
    (out_dir / "portfolio_summary.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
