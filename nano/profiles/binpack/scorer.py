"""The bin-packing scorer, owned by the harness. The candidate never sees this file.

Usage (the checker runs it through nano/launch.py):
  python nano/profiles/binpack/scorer.py --candidate CAND.py --out OUT --level build|quick|full --seed S

Instances come from the seed: item sizes uniform in (0, 1], bin capacity 1.0.
  build : 2 instances x 50 items (the rule loads, returns valid indices, packs everything)
  quick : 20 instances x 200 items
  full  : 100 instances x 1000 items
Each instance gets a fresh copy of the candidate module (its top-level state starts clean), and
choose_bin(item, bins, capacity) receives a copy of the bin fills, so it can neither see the rest of
the instance nor change the harness's state. An index out of range, a non-integer, or an item that
does not fit fails the run.

Writes OUT/metrics.json:
  {"score": mean over instances of bins_used / ceil(total size)   (lower is better, 1.0 is optimal or better),
   "cost": {"time_per_item_s": seconds inside choose_bin per item}, "n": instances,
   "level", "seed", "items_per_instance", "score_sd": SD across instances, "bins_mean"}
Standard library only; no imports from the project (the launcher runs Python with -I).
"""
from __future__ import annotations

import argparse
import builtins
import json
import math
import random
import statistics
import sys
import time
from pathlib import Path

LEVELS = {"build": (2, 50), "quick": (20, 200), "full": (100, 1000)}
CAPACITY = 1.0
EPS = 1e-9


class BadChoice(Exception):
    pass


def instance(level: str, seed: int, i: int, n_items: int) -> list[float]:
    rng = random.Random(f"binpack/{level}/{seed}/{i}")
    return [1.0 - rng.random() for _ in range(n_items)]          # uniform in (0, 1]


def fresh_rule(code, path: str):
    g = {"__name__": "candidate", "__file__": path, "__builtins__": builtins}
    exec(code, g)
    fn = g.get("choose_bin")
    if not callable(fn):
        raise BadChoice("the candidate defines no callable choose_bin(item, bins, capacity)")
    return fn


def pack(fn, items: list[float]) -> tuple[int, float]:
    bins: list[float] = []
    spent = 0.0
    clock = time.perf_counter
    for k, item in enumerate(items):
        view = list(bins)
        t0 = clock()
        j = fn(item, view, CAPACITY)
        spent += clock() - t0
        if isinstance(j, bool) or not isinstance(j, int):
            raise BadChoice(f"item {k}: choose_bin returned {j!r} ({type(j).__name__}); it must return an int")
        if j == -1:
            bins.append(item)
            continue
        if not 0 <= j < len(bins):
            raise BadChoice(f"item {k}: choose_bin returned {j}, but there are {len(bins)} open bins (use -1 to open one)")
        if bins[j] + item > CAPACITY + EPS:
            raise BadChoice(f"item {k}: size {item:.4f} does not fit in bin {j} (fill {bins[j]:.4f}, capacity {CAPACITY})")
        bins[j] += item
    return len(bins), spent


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--candidate", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--level", choices=sorted(LEVELS), default="quick")
    ap.add_argument("--seed", type=int, default=0)
    a = ap.parse_args()
    out = Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    path = str(Path(a.candidate).resolve())
    src = Path(path).read_text(encoding="utf-8")
    code = compile(src, path, "exec")
    n_inst, n_items = LEVELS[a.level]
    ratios, bins_used, spent, items_total = [], [], 0.0, 0
    for i in range(n_inst):
        items = instance(a.level, a.seed, i, n_items)
        fn = fresh_rule(code, path)
        used, t = pack(fn, items)
        lower = max(1, math.ceil(sum(items) - EPS))
        ratios.append(used / lower)
        bins_used.append(used)
        spent += t
        items_total += len(items)
    res = {"score": round(statistics.mean(ratios), 6),
           "cost": {"time_per_item_s": spent / max(1, items_total)},
           "n": n_inst, "level": a.level, "seed": a.seed, "items_per_instance": n_items,
           "score_sd": round(statistics.stdev(ratios), 6) if len(ratios) > 1 else 0.0,
           "bins_mean": round(statistics.mean(bins_used), 2)}
    (out / "metrics.json").write_text(json.dumps(res, indent=1), encoding="utf-8")
    print(json.dumps(res))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except BadChoice as e:
        print(f"[scorer] invalid packing: {e}", file=sys.stderr)
        raise SystemExit(3)
