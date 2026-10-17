"""Best-of-N arms at matched cost (ARCHITECTURE.md section 8, Arms and Cost; section 3 /bench
step 5; MSR-02).

- bestofn_vote: N independent plain calls, majority vote on pred (ties go to the first seen).
- bestofn_verify: N independent plain calls; ARC picks the first candidate whose program passes
  every train pair (demo_match), else the majority pred; BRAINTEASER falls back to the vote.
- seeded_bestofn: plain calls each with a seed word and a shuffled fact order (ARC train-pair
  order, BRAINTEASER option order mapped back to canonical letters), selected like
  bestofn_verify ("seeded best-of-N with the same /verify").

N is derived from budget_tokens: the first call always runs; later calls are spawned while
realized spend plus the largest call cost seen so far stays within the budget, in batches of
up to MAX_WORKERS while the room is at least two such calls and one at a time after that, so
the overshoot above the budget is bounded by one call's deviation. With no budget, N = m.
The runs.jsonl row records overshoot = max(0, spent - budget_tokens).
"""
from __future__ import annotations

import json
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from .. import config
from ..schemas import Answer, Candidate, new_id, strip_key
from .plain import (answer_from, finish_run, plain_call, prepare_run_dir, rng_for, run_id_for)

POOL_ARMS = ("bestofn_vote", "bestofn_verify", "seeded_bestofn")
MAX_WORKERS = 6
MAX_N_MULT = 4          # hard cap: N <= MAX_N_MULT * m, whatever the budget says
MAX_FAILED_START = 3    # stop if this many calls fail before any call returns text

DEFAULT_SEEDS = (
    "river", "ladder", "mirror", "garden", "bridge", "candle", "window", "anchor", "basket",
    "compass", "feather", "harbor", "island", "kettle", "lantern", "magnet", "needle", "orchard",
    "pebble", "quilt", "ribbon", "saddle", "tunnel", "umbrella", "valley", "wheel", "yarn",
    "zipper", "bottle", "cloud", "drum", "engine", "fence", "glove", "hammer", "jar", "key",
    "leaf", "map", "nest", "oven", "pillow", "rope", "shell", "tower", "violin", "wagon", "clock",
    "sponge", "thread",
)


# ---------------------------------------------------------------- seeds
def seed_words() -> list[str]:
    """Seed concepts from strategies/seeds/concepts.txt, else the built-in 50 nouns."""
    path = Path(config.SEEDS_PATH)
    if path.exists():
        words = [w.strip() for w in path.read_text(encoding="utf-8").splitlines()]
        words = [w for w in words if w and not w.startswith("#")]
        if words:
            return words
    return list(DEFAULT_SEEDS)


def seed_for(item_id: str, arm: str, replicate: int, index: int, words: list[str]) -> str:
    return rng_for(item_id, arm, replicate, f"seed:{index}").choice(words)


# ---------------------------------------------------------------- spawning under the budget
def next_batch_size(spent: int, n_done: int, budget: int | None, n_cap: int,
                    max_cost: int | None = None) -> int:
    """How many calls to launch now: 1 first; then, sized by the largest call cost seen (the
    mean when no per-call costs are known), as many as fit up to MAX_WORKERS while at least
    two more fit, and one at a time once the remaining room is under two calls."""
    room_n = n_cap - n_done
    if room_n <= 0:
        return 0
    if n_done == 0:
        return 1
    if budget is None:
        return min(MAX_WORKERS, room_n)
    unit = float(max_cost if max_cost else spent / n_done)
    if unit <= 0:
        return min(MAX_WORKERS, room_n)
    fit = int((budget - spent) // unit)
    if fit < 2:
        return min(fit, room_n) if fit > 0 else 0
    return max(0, min(fit, MAX_WORKERS, room_n))


def spawn_pool(item: dict, *, arm: str, run_dir: Path, backend: str, replicate: int, batch: str,
               m: int, budget: int | None, run_instance: str | None = None) -> tuple[list[Candidate], int, list[str]]:
    """Run plain calls until the budget rule stops; returns (cands in index order, spent, errors)."""
    seeded = arm == "seeded_bestofn"
    check_demo = arm in ("bestofn_verify", "seeded_bestofn") and item["benchmark"] == "arc"
    words = seed_words() if seeded else []
    n_cap = max(1, MAX_N_MULT * m) if budget is not None else max(1, m)
    cands: list[Candidate] = []
    spent, errors, ok, max_cost = 0, [], 0, 0

    def one(index: int):
        seed = seed_for(item["id"], arm, replicate, index, words) if seeded else ""
        return plain_call(item, arm=arm, run_dir=run_dir, backend=backend, replicate=replicate,
                          batch=batch, index=index, seed_word=seed, shuffle=seeded,
                          card="bestofn", check_demo=check_demo, run_instance=run_instance)

    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as ex:
        while True:
            k = next_batch_size(spent, len(cands), budget, n_cap, max_cost)
            if k <= 0:
                break
            for cand, res in ex.map(one, range(len(cands), len(cands) + k)):
                cands.append(cand)
                spent += res.usage.total_tokens
                max_cost = max(max_cost, res.usage.total_tokens)
                ok += 1 if res.text else 0
                if res.error:
                    errors.append(res.error)
            if ok == 0 and len(errors) >= MAX_FAILED_START:
                break
    return cands, spent, errors


# ---------------------------------------------------------------- selection
def pred_key(pred) -> str:
    return json.dumps(pred, sort_keys=True)


def vote(cands: list[Candidate]) -> Candidate | None:
    """Majority vote on pred; ties go to the key seen first; None preds do not vote."""
    counts: dict[str, int] = {}
    first: dict[str, Candidate] = {}
    for c in cands:
        if c.pred is None:
            continue
        k = pred_key(c.pred)
        counts[k] = counts.get(k, 0) + 1
        first.setdefault(k, c)
    if not counts:
        return None
    best = max(counts.values())
    for k in first:                       # dict order = first-seen order
        if counts[k] == best:
            return first[k]
    return None


def passes_demo(cand: Candidate) -> bool:
    demo = cand.extra.get("demo") or {}
    return cand.pred is not None and demo.get("total", 0) > 0 and demo["matched"] == demo["total"]


def select(arm: str, item: dict, cands: list[Candidate], spent: int) -> Answer:
    """Arm-specific choice of the returned candidate."""
    if arm == "bestofn_vote":
        return answer_from(vote(cands), spent=spent)
    if item["benchmark"] == "arc":
        for c in cands:
            if passes_demo(c):
                return answer_from(c, spent=spent, status="solved", vtype="demo_match",
                                   reason="first candidate passing all train pairs")
        return answer_from(vote(cands), spent=spent, vtype="demo_match",
                           reason="no candidate passed all train pairs; majority pred")
    return answer_from(vote(cands), spent=spent, vtype="agreement", reason="majority vote")


def run_arm(arm: str, item: dict, *, m: int, replicate: int, backend: str, batch: str,
            budget_tokens: int | None = None) -> Answer:
    """Best-of-N arms (section 8 Arms); N set by budget_tokens (scaffold spend or B)."""
    if arm == "plain":
        from .plain import run_arm as plain_run_arm
        return plain_run_arm(arm, item, m=m, replicate=replicate, backend=backend, batch=batch,
                             budget_tokens=budget_tokens)
    if arm not in POOL_ARMS:
        raise ValueError(f"unknown arm {arm}")
    item = strip_key(item)
    backend = backend or config.default_backend()
    run_dir = prepare_run_dir(run_id_for(batch, item["benchmark"], item["id"], arm, replicate))
    inst = new_id("i")
    cands, spent, errors = spawn_pool(item, arm=arm, run_dir=run_dir, backend=backend,
                                      replicate=replicate, batch=batch, m=m, budget=budget_tokens,
                                      run_instance=inst)
    answer = select(arm, item, cands, spent)
    if errors and not answer.reason:
        answer.reason = f"{len(errors)} call errors"
    all_failed = bool(errors) and not any(c.text for c in cands)
    return finish_run(item, arm=arm, replicate=replicate, batch=batch, run_dir=run_dir,
                      answer=answer, n_calls=len(cands), budget_tokens=budget_tokens,
                      run_instance=inst, error=(errors[-1] if all_failed else None))
