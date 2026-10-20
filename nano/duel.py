"""Tuned-baseline duel for optimiser, schedule and initialisation ideas.

Evidence (research_notes/team/idea_generation/12_ml_research_practice.md): claimed 2x optimiser speed-ups
fall to about 1.1-1.4x against a tuned AdamW; tuning the baseline's weight decay and learning rate
alone moved a speedrun record as much as the proposed change. So before an optimiser-family candidate
gets its verdict, both sides get the same small tuning at half budget (weight decay first, then the
learning rate), and the verdict then compares the two tuned configurations. The duel is opt-in
(`batch_verify --duel`), because it costs about a dozen half-length runs per candidate.

run(candidate, baseline, out, tokens, timeout) -> {"baseline_best": {...}, "candidate_best": {...},
                                                  "baseline_args": [...], "candidate_args": [...]}
"""
from __future__ import annotations

import json
from pathlib import Path

OPT_SYMBOLS = {"Muon", "Muon.step", "Muon.__init__", "newton_schulz5", "build_optimizers", "lr_mult", "GPT._init", "GPT.__init__"}
GRID_WD = (0.05, 0.1, 0.2)
GRID_LR = (0.7, 1.0, 1.4)


def is_optimizer_idea(meta: dict) -> bool:
    syms = set((meta.get("metrics") or {}).get("changed_symbols") or [])
    node = meta.get("node") or ""
    return bool(syms & OPT_SYMBOLS) or node == "opt"


def _run(script: Path, out: Path, tokens: float, timeout: int, extra: list[str]) -> float | None:
    from nano import batch_verify as BV
    r = BV.train_with_args(script, out, 0, tokens, timeout, extra)
    return r.get("val_loss")


def tune(script: Path, out: Path, tokens: float, timeout: int) -> dict:
    """Weight decay first at the default LR, then LR multipliers at the best weight decay; half budget, seed 0."""
    best = {"wd": None, "lr_mult": 1.0, "val": None}
    half = tokens / 2
    for wd in GRID_WD:
        v = _run(script, out / f"wd{wd}", half, timeout, ["--weight-decay", str(wd)])
        if v is not None and (best["val"] is None or v < best["val"]):
            best = {"wd": wd, "lr_mult": 1.0, "val": v}
    if best["wd"] is None:
        return best
    for m in GRID_LR:
        if m == 1.0:
            continue
        v = _run(script, out / f"wd{best['wd']}_lr{m}", half, timeout, ["--weight-decay", str(best["wd"]), "--lr-mult-both", str(m)])
        if v is not None and v < best["val"]:
            best = {"wd": best["wd"], "lr_mult": m, "val": v}
    return best


def run(candidate: Path, baseline: Path, out: Path, tokens: float, timeout: int) -> dict:
    out.mkdir(parents=True, exist_ok=True)
    b = tune(baseline, out / "baseline", tokens, timeout)
    c = tune(candidate, out / "candidate", tokens, timeout)
    res = {"baseline_best": b, "candidate_best": c,
           "baseline_args": (["--weight-decay", str(b["wd"])] if b.get("wd") else []) + (["--lr-mult-both", str(b["lr_mult"])] if b.get("lr_mult", 1.0) != 1.0 else []),
           "candidate_args": (["--weight-decay", str(c["wd"])] if c.get("wd") else []) + (["--lr-mult-both", str(c["lr_mult"])] if c.get("lr_mult", 1.0) != 1.0 else [])}
    (out / "duel.json").write_text(json.dumps(res, indent=1), encoding="utf-8")
    return res
