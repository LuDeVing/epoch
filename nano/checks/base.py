"""The checker protocol (docs/GENERIC_SPEC.md section 3).

A checker turns a candidate artifact into a verify record. The loop never knows what the artifact is;
it only reads the record and a few metrics, so every checker fills the same names with the same meaning.

Verify record (the shape loop.py and verdict.py already read):
    {"candidate": str, "rungs": [ {"rung": int, "ok": bool, ...}, ... ],
     "status": "checked" | "fail", "rung_reached": int, "partial_score": float,
     "feedback": {"rung": int, "reason": str, ...},      # empty when checked
     "metrics": {...}}

Metric semantics (generic; every checker uses these names):
    learn_gap   candidate score minus baseline score at the matched cheap check (same seed, same
                instances or steps). SIGNED SO THAT NEGATIVE MEANS BETTER: a higher-is-better
                profile negates the raw difference.
    learn_sd    the baseline's spread across seeds at that check (sample SD), in score units.
    learn_z     learn_gap / learn_sd (nano/verdict.py z_of): the gap in units of seed noise.
    long_gap, long_sd, long_z
                the same at the long (or full) check, again negative = better.
    half_gap, half_z
                the gap at the half-way point of the long check, or the cheap gap when the
                checker has no half-way point.
    trend       long_gap minus half_gap: negative = the candidate pulls further ahead with scale.
    extrap_gap, extrap_z
                long_gap + trend (a linear projection one step further) and its z; the pool is
                ranked by extrap_z, lowest first.
    cost_ratio  candidate cost / baseline cost on the profile's main cost axis; 1.0 when the
                profile has no cost. A generic checker fills this one.
    step_ratio, param_ratio, peak_vram_gb, params_nonembed
                LLM cost names; optional. loop.py treats an absent cost metric as 1.0.

partial_score is rung_reached / 4 (0.75 when a three-rung ladder passes), as in nano/check.py.
"""
from __future__ import annotations

from pathlib import Path
from typing import Any, Protocol, runtime_checkable


@runtime_checkable
class Checker(Protocol):
    """What the loop calls. Constructed as Checker(profile, **profile.checker_args)."""

    LEARN_STEPS: int          # size of the cheap check (steps, or a level name's size); shown in prompts
    LONG_STEPS: int           # size of the long check
    PROFILE_SEEDS: tuple      # the seeds the baseline is measured on

    def baseline_profile(self, baseline: Path, out: Path, seeds, **kw: Any) -> dict:
        """Measure the baseline artifact in folder `out` over `seeds`. Returns the dict the loop keeps as
        self.profile and passes back as `baseline` below: per-seed scores (or curves) at the cheap and the
        long check, their means and spreads (the noise floor for every z), and the baseline's costs.
        May cache in `out` and reuse a cache measured on the same baseline."""
        ...

    def check(self, candidate: Path, out: Path, baseline: dict, *, rung_max: int = 3, boundary: str | None = None,
              baseline_src: str | None = None, lenient: bool = False, audit: bool = True, **kw: Any) -> dict:
        """The cheap-then-expensive ladder, rung 0 to rung_max, stopping at the first failure. Returns the
        verify record. rung 0 is static (boundary, denied imports), rung 1 builds, rung 2 and up run.
        `lenient` widens the learning tolerance (the long-shot lane); `audit` enables optional extra
        audits. Every run goes through nano/launch.py; an audit violation fails the candidate."""
        ...

    def long_run(self, candidate: Path, out: Path, baseline: dict, **kw: Any) -> dict:
        """The long check for a checked candidate. Returns {"ok": bool, "reason"?, "long_gap", "long_sd",
        "long_z", "half_gap", "half_z", "trend", "extrap_gap", "extrap_z", ...}."""
        ...

    def final(self, candidate: Path, out: Path, baseline: dict, seeds, **kw: Any) -> dict:
        """The full test over `seeds` with the statistical verdict (nano/verdict.py sequential_verdict).
        Returns {"status": "verified"|"stackable"|"close_call"|"promising"|"fail"|"error", "cand_vals",
        "base_vals", "verdict": {...}}; values are in the profile's score units, raw (not negated)."""
        ...


def lower_is_better(profile) -> bool:
    """profile.lower_is_better when present, else score["direction"] != "higher"."""
    v = getattr(profile, "lower_is_better", None)
    if isinstance(v, bool):
        return v
    score = getattr(profile, "score", None) or {}
    return str(score.get("direction", "lower")).lower() != "higher"
