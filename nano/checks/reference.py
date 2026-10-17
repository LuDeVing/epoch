"""Re-labelling gaps against a moving reference (Mode 2 and Mode 3, docs/GENERIC_SPEC.md section 6).

Without a baseline, the reference is the best checked candidate so far. When it moves, the gaps of earlier
candidates are recomputed against it from the scores they already have, without running anything again.

    relabel(checker, metrics, ref_profile, lower_is_better) -> dict of updated metric names

A checker with its own relabel(metrics, baseline) method (nano/checks/panel.py) is used as it is. Otherwise the
reference profile is read in the shape nano/checks/script.py writes: {"quick": {"scores": {seed: s}, "mean", "sd",
"costs"}, "full": {...}}, and the candidate's learn_score (quick) and long_score (full) at the checker's matched seed.
Every gap is signed so that negative means better.
"""
from __future__ import annotations

from nano import verdict as V


def _level_gap(score, prof: dict, level: str, seed, sign: float) -> dict:
    lv = (prof or {}).get(level) or {}
    base = (lv.get("scores") or {}).get(str(seed))
    if base is None:
        base = lv.get("mean")
    sd = lv.get("sd")
    if score is None or base is None:
        return {"base": base, "gap": None, "sd": sd, "z": None}
    gap = round(sign * (float(score) - float(base)), 6)
    return {"base": round(float(base), 6), "gap": gap, "sd": None if sd is None else round(sd, 6),
            "z": V.z_of(gap, sd, floor=1e-6)}


def _cost_ratio(metrics: dict, prof: dict, seed, key: str | None) -> float | None:
    cost = metrics.get("cost")
    if not isinstance(cost, dict) or not cost:
        return None
    k = key or next(iter(cost))
    lv = (prof or {}).get("quick") or {}
    base = (lv.get("costs") or {}).get(str(seed)) or lv.get("cost_mean")
    c = cost.get(k)
    if not isinstance(c, (int, float)) or not base:
        return None
    return round(float(c) / float(base), 3)


def relabel(checker, metrics: dict, ref_profile: dict, lower_is_better: bool = True) -> dict:
    impl = getattr(checker, "impl", checker)
    own = getattr(impl, "relabel", None)
    if callable(own):
        return dict(own(metrics, ref_profile) or {})
    sign = 1.0 if lower_is_better else -1.0
    seed = getattr(impl, "check_seed", None)
    if seed is None:
        seed = (ref_profile or {}).get("check_seed", 0)
    out: dict = {}
    q = _level_gap(metrics.get("learn_score"), ref_profile, "quick", seed, sign)
    if metrics.get("learn_score") is not None:
        out.update({"learn_base": q["base"], "learn_gap": q["gap"], "learn_sd": q["sd"], "learn_z": q["z"]})
        cr = _cost_ratio(metrics, ref_profile, seed, getattr(impl, "cost_key", None))
        if cr is not None:
            out["cost_ratio"] = cr
    if metrics.get("long_score") is not None:
        f = _level_gap(metrics.get("long_score"), ref_profile, "full", seed, sign)
        half = q["gap"]
        trend = None if (f["gap"] is None or half is None) else round(f["gap"] - half, 6)
        extrap = None if trend is None else round(f["gap"] + trend, 6)
        quick_sd = ((ref_profile or {}).get("quick") or {}).get("sd")
        out.update({"long_base": f["base"], "long_gap": f["gap"], "long_sd": f["sd"], "long_z": f["z"],
                    "half_gap": half, "half_z": V.z_of(half, quick_sd, floor=1e-6), "trend": trend,
                    "extrap_gap": extrap, "extrap_z": V.z_of(extrap, f["sd"], floor=1e-6)})
    return out
