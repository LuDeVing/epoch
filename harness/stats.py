"""Derived strategy statistics view (ARCHITECTURE.md section 3 /ledger step 2, section 6).

`rebuild(batch)` reads ledger rows of one batch whose split is in TRAIN_SPLITS and writes
`memory/views/<batch>/strategy_stats.json` = {batch, splits, n_rows, built_ts, content_hash,
rows: [{cls, card, round_type, pass, fail, n, mean_tokens, n_calls, mean_verify_tokens,
beta_a, beta_b}]}. `load_views(batch)` returns {"batch", "strategy_stats": <that file>,
"calibration": <calibration.json or None>}, the shape think/allocate.stats_rows reads.
No LLM writes any view (MEM-16, CTL-07).

Split choice: TRAIN_SPLITS = data.TRAIN_SPLITS = ("train", "dev-tune"). Section 6 says strategy
stats come from train rows only and held-out items never enter memory (MSR-11). data.py has no
"train" split at P0, so dev-tune (the tuning split) stands in; dev-ablate and test never build a
view. The splits used are recorded in the view, and think refuses a snapshot whose splits
include the item's split (Pr11). Reached from a real batch by `python -m harness.stats <batch>`
(section 7 step 1) or by think on first use of flags.snapshot (HTSA_SNAPSHOT for a bench run).

Counting per cell: outcome rows are rows with a non-null status other than "card_error" (one
per verification); pass = status "verified"; fail = status "fail" only. "unverified" and
"checked" rows rest on no script check, so they update no statistics (EVL-10); n = pass + fail.
Call rows (no status) are one per model call and are grouped by
their spawn key (run_id, round, card, operator, seed, perm, round_type, parent_id) into card runs
(parent_id keeps two revise children of one round apart);
n_calls = card runs; mean_tokens = mean tokens.total_tokens per card run (the est_cost input;
all rows when the cell has no call rows); mean_verify_tokens = mean over outcome rows. Only the
latest run_instance of each run_id counts (ledger.current_rows). Verification rows carry the candidate's round_type (think.py), so a cell
joins a card's calls with the verifications of its candidates.

The view is rebuilt, never edited: a previous file with different content is copied to
views/<batch>/history/strategy_stats.<hash>.json before the new one replaces it atomically.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import threading
from pathlib import Path

from . import config, ledger
from .data import TRAIN_SPLITS
from .schemas import now_ts

VIEW_NAME = "strategy_stats.json"


def view_path(batch: str) -> Path:
    return Path(config.VIEWS_DIR) / batch / VIEW_NAME


def _tokens(r: dict) -> int:
    t = r.get("tokens")
    if isinstance(t, dict):
        if "total_tokens" in t:
            return int(t.get("total_tokens") or 0)
        return int(sum(int(t.get(k) or 0) for k in ("input_tokens", "output_tokens",
                       "cache_read_input_tokens", "cache_creation_input_tokens")))
    if isinstance(t, (int, float)):
        return int(t)
    return 0


def _mean(xs: list[int]) -> float | None:
    return round(sum(xs) / len(xs), 2) if xs else None


def _cell_stats(group: list[dict]) -> dict:
    """Counts, token means and Beta parameters for one (cls, card, round_type) cell."""
    outcomes = [r for r in group if r.get("status") not in (None, "card_error")]
    calls = [r for r in group if r.get("status") in (None, "card_error")]
    n_pass = sum(1 for r in outcomes if r.get("status") == "verified")
    n_fail = sum(1 for r in outcomes if r.get("status") == "fail")    # EVL-10: true failures only
    # one ledger row per model call; a card run (one spawn) may span several calls, so the
    # est_cost input is the mean over card runs = call rows grouped by their spawn key
    runs: dict[tuple, int] = {}
    for r in calls:
        k = (r.get("run_id"), r.get("round"), r.get("card"), r.get("operator"), r.get("seed"),
             r.get("perm"), r.get("round_type"), r.get("parent_id"))
        runs[k] = runs.get(k, 0) + _tokens(r)
    mean_tokens = _mean(list(runs.values())) if runs else _mean([_tokens(r) for r in group])
    return {"pass": n_pass, "fail": n_fail, "n": n_pass + n_fail, "n_calls": len(runs) or len(calls),
            "mean_tokens": mean_tokens or 0.0,
            "mean_verify_tokens": _mean([_tokens(r) for r in outcomes]),
            "beta_a": 1 + n_pass, "beta_b": 1 + n_fail}


def compute(rows_in: list[dict]) -> list[dict]:
    """Cell rows [{cls, card, round_type, ...stats}] from ledger rows, sorted (section 6)."""
    groups: dict[tuple, list[dict]] = {}
    for r in rows_in:
        key = (str(r.get("cls") or "unknown"), str(r.get("card") or "unknown"),
               str(r.get("round_type") or "unknown"))
        groups.setdefault(key, []).append(r)
    return [{"cls": cls, "card": card, "round_type": rt, **_cell_stats(g)}
            for (cls, card, rt), g in sorted(groups.items())]


def _archive_previous(p: Path, new_hash: str) -> None:
    old = None
    try:
        old = json.loads(p.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return
    old_hash = old.get("content_hash") if isinstance(old, dict) else None
    if old_hash and old_hash != new_hash:
        hist = p.parent / "history" / f"strategy_stats.{old_hash[:12]}.json"
        hist.parent.mkdir(parents=True, exist_ok=True)
        if not hist.exists():
            hist.write_text(p.read_text(encoding="utf-8"), encoding="utf-8")


def rebuild(batch: str, splits: tuple[str, ...] = TRAIN_SPLITS) -> Path:
    """Rebuild memory/views/<batch>/strategy_stats.json from ledger rows (section 3 step 2)."""
    rs = [r for r in ledger.current_rows(ledger.rows(batch=batch)) if r.get("split") in splits]
    cells = compute(rs)
    body = json.dumps(cells, sort_keys=True, ensure_ascii=True)
    content_hash = hashlib.sha256(body.encode("utf-8")).hexdigest()
    view = {"batch": batch, "splits": list(splits), "n_rows": len(rs), "built_ts": now_ts(),
            "content_hash": content_hash, "rows": cells}
    p = view_path(batch)
    p.parent.mkdir(parents=True, exist_ok=True)
    if p.exists():
        _archive_previous(p, content_hash)
    tmp = p.with_suffix(".json.tmp")
    tmp.write_text(json.dumps(view, indent=1, ensure_ascii=True), encoding="utf-8")
    os.replace(tmp, p)
    return p


def _read(p: Path):
    try:
        return json.loads(p.read_text(encoding="utf-8")) if p.exists() else None
    except (OSError, json.JSONDecodeError):
        return None


def load_views(batch: str | None) -> dict | None:
    """Views of a snapshot batch {"batch", "strategy_stats", "calibration"}, or None when the
    batch is None or has no strategy_stats view (empty memory, section 6)."""
    if not batch:
        return None
    st = _read(view_path(batch))
    if st is None:
        return None
    return {"batch": batch, "strategy_stats": st,
            "calibration": _read(Path(config.VIEWS_DIR) / batch / "calibration.json")}


def cell(views: dict | None, cls: str, card: str, round_type: str) -> dict | None:
    """Convenience lookup of one cell in loaded views; None if absent."""
    rows = ((views or {}).get("strategy_stats") or {}).get("rows") or []
    for r in rows:
        if (r.get("cls"), r.get("card"), r.get("round_type")) == (cls, card, round_type):
            return r
    return None


_BUILD_LOCK = threading.Lock()


def ensure_views(batch: str | None, splits: tuple[str, ...] = TRAIN_SPLITS) -> dict | None:
    """load_views(batch), building the view first when it does not exist yet and the ledger
    holds rows of that batch in `splits` (section 7 step 1 on first use). An existing view is
    never rebuilt here, so a snapshot stays frozen once written; rebuild it with the CLI."""
    if not batch:
        return None
    with _BUILD_LOCK:
        if not view_path(batch).exists():
            if not any(r.get("split") in splits for r in ledger.rows(batch=batch)):
                return None
            rebuild(batch, splits)
    return load_views(batch)


def main(argv: list[str] | None = None) -> int:
    """CLI: python -m harness.stats <batch> [--splits train,dev-tune] (section 7 step 1)."""
    ap = argparse.ArgumentParser(prog="python -m harness.stats", description=main.__doc__)
    ap.add_argument("batch")
    ap.add_argument("--splits", default=",".join(TRAIN_SPLITS))
    a = ap.parse_args(argv)
    splits = tuple(s.strip() for s in a.splits.split(",") if s.strip())
    p = rebuild(a.batch, splits)
    v = _read(p) or {}
    print(json.dumps({"view": str(p), "splits": list(splits), "n_rows": v.get("n_rows"),
                      "cells": len(v.get("rows") or []), "content_hash": v.get("content_hash")}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
