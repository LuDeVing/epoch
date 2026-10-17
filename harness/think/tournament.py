"""Revise-parent selection (ARCHITECTURE.md section 4 `tournament(state.revise_queue,
surprises_first=True, n=2)`; section 3 /generate revise card; section 5 rows "hi" and
"Revise spawns per round"; GEN-14, MSR-08, SOC-05).

Surprises first (conf > hi and the verifier failed), highest conf first; remaining slots by
size-2 tournaments on the verifier partial_score only (never conf or p_raw), with a
replicate-seeded RNG. Ties are broken uniformly at random.
"""
from __future__ import annotations

import random

from ..schemas import Candidate, VerifyResult

ARM = "scaffold"


def is_surprise(cand: Candidate, vr: VerifyResult, conf: dict, hi: float) -> bool:
    return vr.status == "fail" and (float(conf.get(cand.id, 0.0)) > hi or bool(vr.surprise))


def _duel(a, b, rng: random.Random):
    sa, sb = a[1].partial_score, b[1].partial_score
    if sa == sb:
        return a if rng.random() < 0.5 else b
    return a if sa > sb else b


def pick_parents(queue: list[tuple[Candidate, VerifyResult]], conf: dict, hi: float, n: int,
                 replicate: int) -> list[tuple[Candidate, VerifyResult]]:
    """Up to n parents: surprises first, then size-2 tournaments on partial_score."""
    if n <= 0 or not queue:
        return []
    # keyed on the queue's shape (length, partial scores in queue order), never on candidate
    # uuids, so a replicate reproduces its draws (README Determinism)
    shape = ",".join(f"{float(vr.partial_score):.4f}" for _, vr in queue)
    rng = random.Random(f"{len(queue)}:{shape}:{n}:{ARM}:{replicate}:tournament")
    surprises = sorted((e for e in queue if is_surprise(e[0], e[1], conf, hi)),
                       key=lambda e: -float(conf.get(e[0].id, 0.0)))
    picked = surprises[:n]
    rest = [e for e in queue if all(e is not p for p in picked)]
    while len(picked) < n and rest:
        if len(rest) == 1:
            win = rest[0]
        else:
            a, b = rng.sample(rest, 2)
            win = _duel(a, b, rng)
        picked.append(win)
        rest = [e for e in rest if e is not win]
    return picked
