"""Baseline arms of the measurement harness (ARCHITECTURE.md section 8, Arms).

run_arm(arm, item, *, m, replicate, backend, batch, budget_tokens=None) -> Answer
dispatches to plain.py (plain) or best_of_n.py (bestofn_vote, bestofn_verify, seeded_bestofn).
"""
from __future__ import annotations

from ..schemas import Answer

ARMS = ("plain", "bestofn_vote", "bestofn_verify", "seeded_bestofn")


def run_arm(arm: str, item: dict, *, m: int, replicate: int, backend: str, batch: str,
            budget_tokens: int | None = None) -> Answer:
    """Section 8 Arms: route to the module that implements the arm."""
    if arm == "plain":
        from .plain import run_arm as fn
    elif arm in ARMS:
        from .best_of_n import run_arm as fn
    else:
        raise ValueError(f"unknown arm {arm}; expected one of {ARMS}")
    return fn(arm, item, m=m, replicate=replicate, backend=backend, batch=batch,
              budget_tokens=budget_tokens)
