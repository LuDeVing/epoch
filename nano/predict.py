"""Prediction tracking: every sketch carries a PREDICTION; when its build is measured, the claim is
compared with the numbers. The comparison goes into the verify record (prediction_check), into the
history that later agents read ("you predicted X, the measurement was Y"), the dashboard and the
scorecard. This is the one place the run learns which cards and kinds of idea are trustworthy.

parse_prediction(text) -> {"params": {...} | None, "step": {...} | None, "loss": {...} | None}
check_prediction(pred, metrics, profile) -> {"checkable": bool, "ok": bool | None, "details": [str]}
Only claims with a number are checkable; "about the same" style claims are checked loosely.
The parameter, step-time and loss patterns are the LLM profile's; any profile's claims about its own score
("<score name> lower/higher by X") are read too, in the profile's direction (gaps are signed negative = better).
"""
from __future__ import annotations

import re

NUM = r"([-+]?\d[\d,]*\.?\d*)\s*(k|m|%)?"


def _score_claim(t: str) -> dict | None:
    """A claim about the active profile's score: "<score name> lower by 0.01" (or higher, for a
    higher-is-better profile), as a signed gap (negative = better)."""
    try:
        from nano.ideate import _as_text, lower_is_better, vword
        name = _as_text(vword("score_name")).lower().strip() or "score"
        low = lower_is_better()
    except Exception:  # noqa: BLE001
        name, low = "score", True
    better = r"lower|better|down|drop|reduc\w*|improv\w*" if low else r"higher|better|up|rais\w*|increas\w*|improv\w*"
    m = re.search(rf"(?:{re.escape(name)}|score)[^.]{{0,40}}?(?:{better})[^.]{{0,20}}?by\s*(?:~|about|around|≈|roughly)?\s*" + NUM, t)
    if not m or m.group(2) == "%":
        return None
    v = _num(m.group(1), m.group(2))
    sm = re.search(r"(?:at|after|by)\s+(\d+)\s*(?:matched\s+)?steps", t)
    return {"gap": -abs(v), "steps": int(sm.group(1)) if sm else None, "claim": m.group(0)[:80]}


def _num(s: str, unit: str | None) -> float:
    v = float(s.replace(",", ""))
    if unit == "k":
        v *= 1e3
    elif unit == "m":
        v *= 1e6
    return v


def parse_prediction(text: str) -> dict:
    t = (text or "").lower()
    out: dict = {"params": None, "step": None, "loss": None, "raw": (text or "")[:300]}
    # parameters
    if re.search(r"param(eter)?s?\b[^.]{0,30}(unchanged|same|identical|no change)|no (new|extra|additional) param", t):
        out["params"] = {"ratio_max": 1.005, "ratio_min": 0.995, "claim": "unchanged"}
    m = re.search(r"([-+])\s*" + NUM + r"\s*(?:non-?embedding\s+)?param", t) or re.search(r"(adds?|removes?)\s+" + NUM + r"\s*(?:non-?embedding\s+)?param", t)
    if m:
        sign = -1.0 if m.group(1) in ("-", "removes", "remove") else 1.0
        out["params"] = {"delta_abs": sign * _num(m.group(2), m.group(3)), "claim": m.group(0)[:60]}
    m = re.search(NUM + r"\s*%\s*(more|fewer|less)\s+param", t)
    if m:
        v = _num(m.group(1), None) / 100.0
        out["params"] = {"ratio_max": 1 + v + 0.01, "ratio_min": 1 - v - 0.01, "claim": m.group(0)[:60]}
    # step time
    if re.search(r"step[ -]time[^.]{0,30}(unchanged|same|identical|no change)|no slower|(same|identical) (speed|throughput)", t):
        out["step"] = {"ratio_max": 1.1, "claim": "unchanged"}
    m = re.search(r"(?:at most|up to|<=|≤|about|~|around)?\s*" + NUM + r"\s*%\s*(slower|more step time|longer step|step[ -]time)", t)
    if m:
        out["step"] = {"ratio_max": 1 + _num(m.group(1), None) / 100.0 + 0.05, "claim": m.group(0)[:60]}
    m = re.search(NUM + r"\s*%\s*faster", t)
    if m:
        out["step"] = {"ratio_max": 1.0 + 0.05, "claim": m.group(0)[:60]}
    # loss
    m = re.search(r"(loss|val(?:idation)? loss|perplexity)[^.]{0,40}?(lower|better|down|drop|reduc\w*|improv\w*)[^.]{0,20}?by\s*(?:~|about|around|≈|roughly)?\s*" + NUM, t) \
        or re.search(NUM + r"\s*(?:nats?)?\s*(lower|better) (?:validation |val )?loss", t)
    if m:
        groups = [g for g in m.groups() if g]
        num_m = re.search(r"by\s*(?:~|about|around|≈|roughly)?\s*" + NUM, m.group(0)) or re.search(NUM, m.group(0))
        if num_m:
            v = _num(num_m.group(1), num_m.group(2))
            if num_m.group(2) == "%":
                v = None                                   # relative loss claims are not comparable to a gap
            steps = None
            sm = re.search(r"(?:at|after|by)\s+(\d+)\s*(?:matched\s+)?steps", t)
            if sm:
                steps = int(sm.group(1))
            if v is not None:
                out["loss"] = {"gap": -abs(v), "steps": steps, "claim": m.group(0)[:80]}
    if out["loss"] is None:
        out["loss"] = _score_claim(t)
    return out


def check_prediction(pred: dict, metrics: dict, profile: dict) -> dict:
    details, checks = [], []
    base_p = profile.get("params_nonembed") or 0
    pr = pred.get("params")
    if pr and metrics.get("params_nonembed") is not None and base_p:
        ratio = metrics["params_nonembed"] / base_p
        if "delta_abs" in pr:
            want = (base_p + pr["delta_abs"]) / base_p
            ok = abs(ratio - want) <= max(0.002, abs(pr["delta_abs"]) * 0.25 / base_p)
            details.append(f"params: predicted {pr['delta_abs']:+.0f}, measured {metrics['params_nonembed'] - base_p:+.0f} -> {'ok' if ok else 'off'}")
        else:
            ok = pr["ratio_min"] <= ratio <= pr["ratio_max"]
            details.append(f"params: predicted {pr['claim']}, measured ratio {ratio:.4f} -> {'ok' if ok else 'off'}")
        checks.append(ok)
    st = pred.get("step")
    step_ratio = metrics.get("step_ratio") if metrics.get("step_ratio") is not None else metrics.get("cost_ratio")
    if st and step_ratio is not None:
        ok = step_ratio <= st["ratio_max"]
        details.append(f"step time: predicted {st['claim']}, measured ratio {step_ratio} -> {'ok' if ok else 'off'}")
        checks.append(ok)
    lo = pred.get("loss")
    if lo and metrics.get("learn_gap") is not None:
        gap, sd = metrics["learn_gap"], metrics.get("learn_sd") or 0.0
        if metrics.get("long_gap") is not None and (lo.get("steps") or 0) > 100:
            gap, sd = metrics["long_gap"], metrics.get("long_sd") or 0.0
        if sd > 0 and abs(lo["gap"]) < 2 * sd:
            details.append(f"loss: predicted gap {lo['gap']:+.3f} is below the noise floor (2 sd = {2 * sd:.3f}) at this rung: untestable here")
        else:
            ok = gap <= lo["gap"] + 2 * sd
            details.append(f"loss: predicted gap {lo['gap']:+.3f}" + (f" at {lo['steps']} steps" if lo.get("steps") else "")
                           + f", measured {gap:+.3f} (sd {sd:.3f}) -> {'ok' if ok else 'off'}")
            checks.append(ok)
    if not checks:
        return {"checkable": False, "ok": None, "details": details or ["no checkable number in the prediction"], "raw": pred.get("raw", "")}
    return {"checkable": True, "ok": all(checks), "n": len(checks), "n_ok": sum(1 for c in checks if c),
            "details": details, "raw": pred.get("raw", "")}
