"""Scripted tuning of the recipe's constants.

Single-knob moves around the current values, each a one-line change of a Config default in the baseline
script, built and sent up the same ladder as every idea; the best few go on to the long comparison and the
night like any candidate. A script chooses these, not a model (models do not ration a search well; the
evidence is in research_notes/team/creative_genius/04_raising_the_ceiling.md). Agents may still propose a tuning idea with a reason
(KIND: tune). Values are read from the baseline as it is now, so the sweep follows the recipe when it is
promoted. The overnight duel (batch_verify --duel) separately re-tunes the original's learning rates when an
optimiser idea is judged.
"""
from __future__ import annotations

import re

from nano.ideate import fill, vword

# The LLM profile's knobs (Config fields of nano/train.py). Another profile may supply its own in vocab "tune_knobs"
# ({name: [field, value, "mul"|"abs"]}) and "tune_default" ([names]); a knob whose field line is absent is skipped.
# name: (Config field, value, how): "mul" multiplies the current value, "abs" sets it
KNOBS = {
    "lr_x0.7": ("lr", 0.7, "mul"),
    "lr_x1.4": ("lr", 1.4, "mul"),
    "lr_adam_x0.5": ("lr_adam", 0.5, "mul"),
    "lr_adam_x2": ("lr_adam", 2.0, "mul"),
    "wd_x0.3": ("weight_decay", 0.3, "mul"),
    "wd_x3": ("weight_decay", 3.0, "mul"),
    "warmup_0.05": ("warmup_frac", 0.05, "abs"),
    "warmup_0": ("warmup_frac", 0.0, "abs"),
    "cooldown_0.15": ("cooldown_frac", 0.15, "abs"),
    "cooldown_0.45": ("cooldown_frac", 0.45, "abs"),
    "clip_0.5": ("grad_clip", 0.5, "abs"),
    "clip_2": ("grad_clip", 2.0, "abs"),
    "rope_theta_50k": ("rope_theta", 50000.0, "abs"),
}
DEFAULT = ["lr_x0.7", "lr_x1.4", "lr_adam_x0.5", "lr_adam_x2", "wd_x0.3", "wd_x3", "warmup_0.05",
           "cooldown_0.15", "cooldown_0.45", "clip_0.5", "rope_theta_50k"]


def knobs() -> dict:
    k = vword("tune_knobs", {})
    return {n: tuple(v) for n, v in k.items()} if isinstance(k, dict) and k else KNOBS


def default_names() -> list[str]:
    d = vword("tune_default", [])
    if isinstance(d, (list, tuple)) and d:
        return list(d)
    return DEFAULT if knobs() is KNOBS else list(knobs())


def _line_re(field: str) -> re.Pattern:
    return re.compile(rf"^(\s+{re.escape(field)}: (?:float|int) = )([0-9.eE+-]+)(.*)$", re.M)


def current(src: str, field: str) -> float | None:
    m = _line_re(field).search(src)
    if not m:
        return None
    try:
        return float(m.group(2))
    except ValueError:
        return None


def _fmt(v: float, was_int: bool) -> str:
    if was_int:
        return str(int(round(v)))
    s = f"{v:.6g}"
    return s if ("." in s or "e" in s) else s + ".0"


def build(src: str, names: list[str] | None = None) -> dict[str, dict]:
    """{name: {"source", "hypothesis", "field", "old", "new"}} for every knob whose line exists and whose
    new value differs from the current one."""
    out = {}
    table = knobs()
    for name in (names or default_names()):
        spec = table.get(name)
        if not spec:
            continue
        field, value, how = spec
        m = _line_re(field).search(src)
        if not m:
            continue
        old = float(m.group(2))
        new = old * value if how == "mul" else float(value)
        if abs(new - old) <= 1e-12 * max(1.0, abs(old)):
            continue
        was_int = "." not in m.group(2) and "e" not in m.group(2).lower()
        line = m.group(1) + _fmt(new, was_int) + m.group(3)
        new_src = src[:m.start()] + line + src[m.end():]
        out[name] = {"source": new_src, "field": field, "old": old, "new": new,
                     "hypothesis": f"tune: {field} {old:g} -> {new:g} " + fill("(a single-knob move of the {v:recipe}'s constants)")}
    return out
