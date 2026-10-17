"""Thinking-only test on ARC: several thinkers, each with one human strategy, write a program; every program is run on
the example grids (the objective check); the answer comes from the programs that reproduce every example. No judge,
no setup calls, no budget. The plain answers come from an earlier harness.bench batch on the same puzzles.

    $env:HTSA_LAB_ROOT = "D:\\AGI-lab"; $env:HTSA_MODEL = "haiku"; $env:HTSA_ARC_SET = "arc2"
    python -m harness.arc_think --batch arc2-think --items 10 --plain-from D:\\AGI-lab\\results\\arc2-haiku-plain
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

from . import config, llm
from .arms.plain import arc_data, parse_program
from .schemas import strip_key

STRATEGIES = {
    "describe": "First describe in plain words exactly what changes between each input and its output, cell by cell or region by region. Then turn that description into code.",
    "objects": "Think in terms of objects: find the connected shapes of each colour, and work out how each object is moved, recoloured, copied, resized or removed.",
    "symmetry": "Look for symmetry, repetition and tiling: mirrored halves, repeated patterns, periodic rows or columns, a pattern completed or extended.",
    "counting": "Look at counts and comparisons: how many cells or objects of each colour, which is largest or smallest, which is the odd one out, and how the output size relates to them.",
    "lines": "Look for lines, paths and boundaries: rays drawn from points, cells connected along rows or columns, regions filled up to a boundary.",
    "rules": "Write down two or three candidate rules, check each against every example by hand, and keep the one that explains all of them before writing the code.",
}
FORMAT = ("\n\nGive your final answer as exactly one python code block that defines transform(grid) -> grid. The argument is "
          "the input grid as a list of lists of ints; return the output grid in the same form, using only the python standard "
          "library. It must reproduce every example output from its input.")


def think(item: dict, args, out_dir: Path) -> dict:
    from . import arc_exec as EX
    clean = strip_key(item)
    data = arc_data(clean, list(range(len(clean["train"]))))
    log_dir = out_dir / "calls" / item["id"]
    log_dir.mkdir(parents=True, exist_ok=True)
    cands, tokens = [], 0
    for name in list(STRATEGIES)[: args.thinkers]:
        prompt = ("Task: find the rule that maps each example input grid to its output grid, then write a program that "
                  "applies it to the test input. Each grid is shown as rows of integers 0-9 separated by spaces.\n\n"
                  f"{data}\n\nHow to think about it: {STRATEGIES[name]}{FORMAT}")
        r = llm.call(prompt, role="plain", call_id=f"think_{name}_{int(time.time() * 1000) % 10**9}", backend=args.backend,
                     log_dir=log_dir, meta={"card": f"think_{name}"}, effort=args.effort or None)
        tokens += int(r.usage.total_tokens)
        prog = parse_program(r.text or "")
        if not prog:
            cands.append({"strategy": name, "passed": 0, "total": len(clean["train"]), "pred": None})
            continue
        outs = EX.run_program(prog, [p["input"] for p in clean["train"]] + [clean["test_input"]])
        passed = sum(1 for o, p in zip(outs, clean["train"]) if o == p["output"])
        cands.append({"strategy": name, "passed": passed, "total": len(clean["train"]), "pred": outs[-1]})
    full = [c for c in cands if c["pred"] is not None and c["passed"] == c["total"]]
    pool = full or sorted([c for c in cands if c["pred"] is not None], key=lambda c: -c["passed"])[:1]
    votes = Counter(json.dumps(c["pred"]) for c in pool)
    answer = json.loads(votes.most_common(1)[0][0]) if votes else None
    key = item["test_output"]                                    # read by this scorer only
    return {"id": item["id"], "solved": answer == key, "n_full_pass": len(full), "tokens": tokens,
            "strategies": {c["strategy"]: {"passed": f"{c['passed']}/{c['total']}", "right": c["pred"] == key} for c in cands}}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--batch", required=True)
    ap.add_argument("--items", type=int, default=10)
    ap.add_argument("--split", default="dev-tune")
    ap.add_argument("--thinkers", type=int, default=6)
    ap.add_argument("--backend", default=None)
    ap.add_argument("--effort", default=os.environ.get("HTSA_PLAIN_EFFORT", ""))
    ap.add_argument("--workers", type=int, default=3)
    ap.add_argument("--plain-from", default=None, help="results folder of the plain harness.bench batch on the same puzzles")
    args = ap.parse_args()
    args.backend = args.backend or config.default_backend()
    path = Path(config.BENCHMARKS["arc"]["file"])
    items = [json.loads(l) for l in path.read_text(encoding="utf-8").splitlines() if l.strip()]
    items = [it for it in items if it.get("split") == args.split][: args.items]
    out_dir = Path(config.RESULTS_DIR) / args.batch
    out_dir.mkdir(parents=True, exist_ok=True)
    rows_path = out_dir / "think_runs.jsonl"
    done = {}
    if rows_path.exists():
        for l in rows_path.read_text(encoding="utf-8").splitlines():
            if l.strip():
                r = json.loads(l)
                done[r["id"]] = r
    lock = threading.Lock()
    print(f"[think] {len(items)} puzzles from {path.name}, {args.thinkers} thinkers, model {config.DEFAULT_MODEL}", flush=True)

    def work(it):
        r = think(it, args, out_dir)
        with lock:
            with rows_path.open("a", encoding="utf-8") as f:
                f.write(json.dumps(r) + "\n")
            done[r["id"]] = r
            print(f"[think] {len(done)}/{len(items)} {r['id']}: solved {r['solved']}, programs passing all examples {r['n_full_pass']}, tokens {r['tokens']:,}", flush=True)
    with ThreadPoolExecutor(max_workers=args.workers) as ex:
        list(ex.map(work, [it for it in items if it["id"] not in done]))
    rows = [done[it["id"]] for it in items if it["id"] in done]
    lines = [f"# Thinking test on {path.name} ({len(rows)} puzzles), model {config.DEFAULT_MODEL}", "",
             "| arm | solved | tokens per puzzle |", "|---|---|---|",
             f"| thinking ({args.thinkers} strategies + example check) | {sum(r['solved'] for r in rows)}/{len(rows)} | {sum(r['tokens'] for r in rows) / max(1, len(rows)):,.0f} |"]
    if args.plain_from:
        prow = [json.loads(l) for l in (Path(args.plain_from) / "runs.jsonl").read_text(encoding="utf-8").splitlines() if l.strip()]
        keys = {it["id"]: it["test_output"] for it in items}
        prow = [r for r in prow if r.get("arm") == "plain" and r["item_id"] in keys]
        ok = sum(1 for r in prow if r.get("answer") == keys[r["item_id"]])
        lines.append(f"| plain (one answer) | {ok}/{len(prow)} | {sum(int(r.get('spent_tokens') or 0) for r in prow) / max(1, len(prow)):,.0f} |")
    per = Counter()
    for r in rows:
        for k, v in r["strategies"].items():
            per[k] += v["right"]
    lines += ["", "each strategy alone: " + ", ".join(f"{k} {v}/{len(rows)}" for k, v in per.items())]
    (out_dir / "think_summary.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
