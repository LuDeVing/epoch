"""Population admission (ARCHITECTURE.md section 4 `state.pop = admit.update(...)`; section 5
row "k_pop, elite slots; theta_admit"; CTL-09).

Admit a candidate iff it is verified or its confidence c >= theta_admit. Verified candidates are
always kept; the remaining slots up to k_pop go to the highest-confidence admitted candidates.
"""
from __future__ import annotations

from ..schemas import Candidate

_TOL = 1e-9          # same tolerance as think._at_least: 2 of 3 meets a 2/3 threshold


def update(pop: list[Candidate], cands: list[Candidate], conf: dict, verified_ids: set,
           k_pop: int, theta: float) -> list[Candidate]:
    """New population: all verified, then the top unverified by conf >= theta, up to k_pop."""
    pool: dict[str, Candidate] = {}
    for c in list(pop) + list(cands):
        pool.setdefault(c.id, c)
    key = lambda c: -float(conf.get(c.id, 0.0))                     # noqa: E731
    verified = sorted((c for c in pool.values() if c.id in verified_ids), key=key)
    others = sorted((c for c in pool.values() if c.id not in verified_ids
                     and float(conf.get(c.id, 0.0)) >= float(theta) - _TOL), key=key)
    return verified + others[:max(0, k_pop - len(verified))]
