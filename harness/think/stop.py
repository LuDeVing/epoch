"""Stop-rule helpers (ARCHITECTURE.md section 4 `Pcorrect(...) >= T`, `stop.partial_gain`,
"Progress and stopping"; section 5 rows "T", "T_checked", "eps"; CTL-05).

P(correct | vtype, agreement) is the identity map on agreement at P0 for every vtype. When a
calibration dict is supplied ({vtype: {"x": [...], "y": [...]}}, fit on dev-tune at P1) the map
is piecewise-linear interpolation over those knots.
"""
from __future__ import annotations


def _clip(x: float) -> float:
    return max(0.0, min(1.0, float(x)))


def _interp(x: float, xs: list[float], ys: list[float]) -> float:
    if x <= xs[0]:
        return ys[0]
    for (x0, y0), (x1, y1) in zip(zip(xs, ys), zip(xs[1:], ys[1:])):
        if x <= x1:
            return y0 if x1 == x0 else y0 + (y1 - y0) * (x - x0) / (x1 - x0)
    return ys[-1]


def p_correct(vtype: str, agreement_value: float, calib: dict | None = None) -> float:
    """Identity map at P0 per vtype; calibration knots when given (CTL-05, CTL-06)."""
    a = _clip(agreement_value or 0.0)
    cell = (calib or {}).get(vtype)
    if isinstance(cell, dict) and cell.get("x") and len(cell["x"]) == len(cell.get("y", [])):
        pairs = sorted(zip(cell["x"], cell["y"]))
        return _clip(_interp(a, [p[0] for p in pairs], [p[1] for p in pairs]))
    return a


def partial_gain(prev_best: float, new_best: float) -> float:
    """Improvement of the best verifier partial score this round (graded benchmarks only);
    compared with eps by the driver (CTL-11)."""
    return max(0.0, float(new_best or 0.0) - float(prev_best or 0.0))
