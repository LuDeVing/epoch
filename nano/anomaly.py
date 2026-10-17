"""Anomalies in how the baseline behaves, with a noise firewall.

A measured cell (loss by token-frequency bucket, loss by position bucket, a per-layer metric) is an anomaly when
its residual against a smooth expectation drawn from the rest of its family is large in units of the seed
spread, has the same sign on every seed, and survives a false-discovery filter across all cells. The top rows
are rendered as concrete sentences an idea agent can start from; with a small probability a sham row (a
fabricated deviation on a quiet cell) is mixed in, recorded privately, so the share of sketches that chase
noise can be measured. Design: research_notes/creative_genius/00_SYNTHESIS.md D6; brief 07 (N1, N2, N9).
Pure python: no torch, no model calls. The cells are the language-model diagnostics (nano/diagnose.py); on a
profile without diagnostics compute() returns no rows and an empty text, and cell_of() names no cell.
"""
from __future__ import annotations

import json
import math
import random
import re
from pathlib import Path

from nano.ideate import has_diagnostics

Z_MIN = 2.0          # residual in seed-spread units
FDR_Q = 0.10         # Benjamini-Hochberg level across cells
MAX_ROWS = 5
LAYER_METRICS = ("grad_attn", "grad_mlp", "act_rms", "attn_entropy", "max_logit", "first_token_mass")
CELL_WORDS = {"rare": ("rare", "frequency", "infrequent"), "late": ("late", "position", "far"), "entropy": ("entropy",),
              "rms": ("rms", "residual"), "grad": ("gradient", "grad"), "logit": ("logit",),
              "first": ("first-token", "first token", "sink"), "recall": ("recall", "bigram", "copy"),
              "update": ("update", "norm spread")}


def cell_of(target: str) -> str | None:
    """The diagnostic cell a sketch's TARGET names (same vocabulary as nano/diagnose.py)."""
    if not has_diagnostics():
        return None
    t = (target or "").lower()
    for cell, words in CELL_WORDS.items():
        if any(w in t for w in words):
            return cell
    return None


def _range(name: str) -> tuple[float, float]:
    nums = [float(x) for x in re.findall(r"\d+", name)]
    return (nums[0], nums[1]) if len(nums) >= 2 else (0.0, 1.0)


def cells(d: dict) -> dict[str, tuple[str, float, float]]:
    """key -> (family, value, x) from one diagnostics json; x is the coordinate the family's trend runs over."""
    last = d["probes"][-1]
    out: dict[str, tuple[str, float, float]] = {}
    for name, v in (last.get("by_frequency") or {}).items():
        lo, hi = _range(name)
        out[f"freq:{name}"] = ("frequency", float(v["loss"] if isinstance(v, dict) else v), math.log10(math.sqrt((lo + 1) * max(hi, lo + 2))))
    for name, v in (last.get("by_position") or {}).items():
        lo, hi = _range(name)
        out[f"pos:{name}"] = ("position", float(v), math.log10(math.sqrt((lo + 1) * max(hi, lo + 2))))
    for l in last.get("layers") or []:
        for m in LAYER_METRICS:
            if l.get(m) is not None:
                out[f"layer{l['layer']}:{m}"] = (m, float(l[m]), float(l["layer"]))
    return out


def _fit_line(xs: list[float], ys: list[float]) -> list[float]:
    n = len(xs)
    if n < 2:
        return list(ys)
    mx, my = sum(xs) / n, sum(ys) / n
    sxx = sum((x - mx) ** 2 for x in xs)
    b = sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / sxx if sxx > 0 else 0.0
    return [my + b * (x - mx) for x in xs]


def residuals(per_seed: list[dict[str, tuple[str, float, float]]], vocab: int = 50304) -> list[dict]:
    """Per cell: the residual against its neighbours, the seed spread of that residual, z, and sign agreement.

    Families with many cells (the twelve layers): the expectation for an interior cell is the chord between
    its two neighbours at the cell's coordinate; an end cell is extrapolated from the two nearest and marked
    `edge` (a higher bar applies). Families with three or four cells (loss by position, by frequency) have no
    trend to speak of, so they get absolute rules only: a frequency bucket whose loss is above uniform
    guessing (ln vocab) is an anomaly in itself."""
    keys = sorted(set.intersection(*[set(c) for c in per_seed])) if per_seed else []
    fam_of = {k: per_seed[0][k][0] for k in keys}
    by_family: dict[str, list[str]] = {}
    for k in keys:
        by_family.setdefault(fam_of[k], []).append(k)
    rows = []
    for fam, fkeys in by_family.items():
        fkeys = sorted(fkeys, key=lambda k: per_seed[0][k][2])
        n_seeds = len(per_seed)
        scale = sum(abs(seed[k][1]) for seed in per_seed for k in fkeys) / max(1, n_seeds * len(fkeys))
        floor = 1e-6 + 0.02 * scale
        if len(fkeys) >= 6:
            for i, k in enumerate(fkeys):
                res = []
                for seed in per_seed:
                    xs = [seed[kk][2] for kk in fkeys]
                    ys = [seed[kk][1] for kk in fkeys]
                    if 0 < i < len(fkeys) - 1:
                        a, b = i - 1, i + 1
                    elif i == 0:
                        a, b = 1, 2
                    else:
                        a, b = len(fkeys) - 3, len(fkeys) - 2
                    slope = (ys[b] - ys[a]) / (xs[b] - xs[a]) if xs[b] != xs[a] else 0.0
                    res.append(ys[i] - (ys[a] + slope * (xs[i] - xs[a])))
                mean = sum(res) / n_seeds
                sd = math.sqrt(sum((v - mean) ** 2 for v in res) / (n_seeds - 1)) if n_seeds > 1 else 0.0
                rows.append({"key": k, "family": fam, "cell": _to_cell(fam, k, fkeys), "value": round(sum(sd_[k][1] for sd_ in per_seed) / n_seeds, 4),
                             "residual": round(mean, 4), "sd": round(sd, 4), "z": round(mean / max(sd, floor), 2), "n_seeds": n_seeds,
                             "same_sign": all(v > 0 for v in res) or all(v < 0 for v in res), "edge": i in (0, len(fkeys) - 1), "idx": i})
        elif fam == "frequency":
            ln_v = math.log(vocab)
            for k in fkeys:
                vals = [seed[k][1] for seed in per_seed]
                excess = [v - ln_v for v in vals]
                mean = sum(excess) / n_seeds
                if mean <= 0:
                    continue
                sd = math.sqrt(sum((v - mean) ** 2 for v in excess) / (n_seeds - 1)) if n_seeds > 1 else 0.0
                floor = 0.01                                    # a hundredth of a nat is the practical resolution here
                rows.append({"key": k, "family": "frequency", "cell": _to_cell(fam, k, fkeys), "value": round(sum(vals) / n_seeds, 4),
                             "residual": round(mean, 4), "sd": round(sd, 4), "z": round(mean / max(sd, floor), 2), "n_seeds": n_seeds,
                             "same_sign": all(v > 0 for v in excess), "edge": False, "absolute": f"above uniform guessing (ln V = {ln_v:.2f})"})
    return rows


def _to_cell(fam: str, key: str, fkeys: list[str]) -> str:
    if fam == "frequency":
        return "rare" if key == fkeys[-1] else "frequency"
    if fam == "position":
        return "late" if key == fkeys[-1] else "position"
    return {"attn_entropy": "entropy", "act_rms": "rms", "grad_attn": "grad", "grad_mlp": "grad",
            "max_logit": "logit", "first_token_mass": "first"}.get(fam, fam)


def _p_two_sided(z: float) -> float:
    return math.erfc(abs(z) / math.sqrt(2.0))


def select(rows: list[dict], z_min: float = Z_MIN, q: float = FDR_Q, max_rows: int = MAX_ROWS) -> list[dict]:
    """Same sign on every seed, |z| above the floor (a higher one for extrapolated end cells), and
    Benjamini-Hochberg at level q across all cells."""
    # a bump makes its neighbours' chords miss too, with the opposite sign: the neighbours are shadows, not anomalies
    by_fam: dict[str, dict[int, dict]] = {}
    for r in rows:
        if r.get("idx") is not None:
            by_fam.setdefault(r["family"], {})[r["idx"]] = r
    shadow = set()
    for fam, cells_ in by_fam.items():
        for i, r in cells_.items():
            for nb in (cells_.get(i - 1), cells_.get(i + 1)):
                if not nb or nb["z"] * r["z"] >= 0:
                    continue
                # the neighbour with the larger deviation is the anomaly; this one is its shadow
                if abs(nb["z"]) > abs(r["z"]) or (abs(nb["z"]) == abs(r["z"]) and abs(nb["residual"]) > abs(r["residual"])):
                    shadow.add((fam, i))
    cand = [r for r in rows if r["same_sign"] and abs(r["z"]) >= (z_min + 1.0 if r.get("edge") else z_min) and r["n_seeds"] >= 2
            and (r["family"], r.get("idx")) not in shadow]
    if not cand:
        return []
    m = len(rows)
    ranked = sorted(cand, key=lambda r: _p_two_sided(r["z"]))
    keep_upto = 0
    for i, r in enumerate(ranked, start=1):
        if _p_two_sided(r["z"]) <= q * i / m:
            keep_upto = i
    kept = ranked[:keep_upto]
    return sorted(kept, key=lambda r: -abs(r["z"]))[:max_rows]


def describe(r: dict) -> str:
    fam, key = r["family"], r["key"]
    what = {"frequency": f"loss on tokens of {key.split(':', 1)[1]}", "position": f"loss at positions {key.split(':', 1)[1]}"}.get(fam)
    if what is None:
        layer = key.split(":")[0].replace("layer", "layer ")
        what = f"{fam.replace('_', ' ')} in {layer}"
    direction = "above" if r["residual"] > 0 else "below"
    if r.get("absolute"):
        return (f"{what}: {r['value']} is {abs(r['residual'])} {r['absolute']} "
                f"(z {r['z']}, on all {r['n_seeds']} seeds) [cell: {r['cell']}]")
    where = "what its two neighbours predict" + (" (extrapolated at the end of the range)" if r.get("edge") else "")
    return (f"{what}: {r['value']} is {abs(r['residual'])} {direction} {where} "
            f"(z {r['z']}, same sign on {r['n_seeds']} seeds) [cell: {r['cell']}]")


def make_sham(rows: list[dict], rng: random.Random) -> dict | None:
    """A fabricated deviation on a quiet cell, to measure how often agents chase a stated anomaly that is noise."""
    quiet = [r for r in rows if abs(r["z"]) < 1.0 and r["n_seeds"] >= 2]
    if not quiet:
        return None
    r = dict(rng.choice(quiet))
    sign = rng.choice((1, -1))
    size = max(3.0 * max(r["sd"], 1e-3), 0.05 * abs(r["value"]) + 1e-3)
    r["residual"] = round(sign * min(size, 0.3 * abs(r["value"]) + 1e-3), 4)   # believable: never larger than a third of the value
    r["z"] = round(sign * rng.uniform(2.6, 3.4), 2)
    r["same_sign"] = True
    return {"key": r["key"], "cell": r["cell"], "text": describe(r)}


def compute(paths: list[Path], run_id: str = "", sham_share: float = 0.1) -> dict:
    """Load diagnostics jsons (one per seed), flag anomalies, render them, maybe add a sham row."""
    if not has_diagnostics():
        return {"anomalies": [], "text": "", "n_seeds": 0, "sham": None}
    ds = []
    for p in paths:
        try:
            ds.append(json.loads(Path(p).read_text(encoding="utf-8")))
        except Exception:  # noqa: BLE001
            continue
    per_seed = [cells(d) for d in ds if d.get("probes")]
    if len(per_seed) < 2:
        return {"anomalies": [], "text": "", "n_seeds": len(per_seed), "sham": None}
    rows = residuals(per_seed)
    flagged = select(rows)
    lines = [describe(r) for r in flagged]
    rng = random.Random(f"sham:{run_id}")
    sham = make_sham(rows, rng) if rng.random() < sham_share else None
    if sham:
        lines.insert(rng.randrange(len(lines) + 1), sham["text"])
    text = "\n".join(f"- {l}" for l in lines)
    return {"anomalies": flagged, "n_cells": len(rows), "text": text, "n_seeds": len(per_seed), "sham": sham}


def chased(sketches: list[dict], sham: dict | None) -> int:
    """How many sketches aimed at the sham's cell (their TARGET names it)."""
    if not sham:
        return 0
    return sum(1 for s in sketches if cell_of(s.get("target", "")) == sham.get("cell"))


def aimed(sketches: list[dict], anomalies: list[dict]) -> int:
    cells_ = {a["cell"] for a in anomalies}
    return sum(1 for s in sketches if cell_of(s.get("target", "")) in cells_)
