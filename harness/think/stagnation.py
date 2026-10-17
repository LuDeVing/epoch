"""Stagnation reset guard (ARCHITECTURE.md section 4 `if R_max > 2 and (state.stale >= R_stale or
dup_rate > d_max)`; section 5 rows "R_max", "R_stale, d_max"; CTL-04, CTL-11).

A reset replaces the next round's specs with unused (card, operator, seed, perm) tuples
(allocate.fresh_tuples); it never extends the run. CTL-04: no reset when R_max <= 2.
"""
from __future__ import annotations


def should_reset(stale: int, dup_rate: float, R_max: int, R_stale: int, d_max: float) -> bool:
    """True iff R_max > 2 and (stale >= R_stale or dup_rate > d_max)."""
    if R_max <= 2:
        return False
    return stale >= R_stale or float(dup_rate) > d_max
