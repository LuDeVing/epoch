"""Append-only ledger writer and reader (ARCHITECTURE.md section 3 /ledger step 1, section 6).

`memory/ledger.jsonl` is the single cross-run source of truth. Rows are only ever appended,
one JSON object per line; nothing here rewrites, truncates or reorders the file (MEM-11).
Derived views (stats.py) are rebuilt from these rows.

The lock serializes writers inside one process (think.py runs calls on threads). Each row is
written with a single write() of one complete line in append mode, so concurrent processes
do not interleave partial lines on local NTFS in practice; there is no cross-process lock.
"""
from __future__ import annotations

import json
import threading
from pathlib import Path
from typing import Any

from . import config
from .schemas import LedgerRow, now_ts

_lock = threading.Lock()


def path() -> Path:
    """Current ledger path (read at call time so tests can repoint config.LEDGER_PATH)."""
    return Path(config.LEDGER_PATH)


def _to_row(row: Any) -> dict:
    """LedgerRow or dict -> plain dict with a timestamp (section 3 /ledger step 1)."""
    if isinstance(row, LedgerRow):
        d = row.to_dict()
    elif isinstance(row, dict):
        d = dict(row)
    elif hasattr(row, "to_dict"):
        d = dict(row.to_dict())
    else:
        raise TypeError(f"ledger.append expects LedgerRow or dict, got {type(row).__name__}")
    if not d.get("ts"):
        d["ts"] = now_ts()
    return d


def append(row) -> None:
    """Append one row (LedgerRow or dict) to the ledger. Never rewrites (MEM-11).

    Raises TypeError/ValueError before touching the file if the row is not serializable,
    so a bad row can never leave a partial line behind."""
    d = _to_row(row)
    line = json.dumps(d, ensure_ascii=True) + "\n"
    p = path()
    with _lock:
        p.parent.mkdir(parents=True, exist_ok=True)
        with p.open("a", encoding="utf-8") as f:
            f.write(line)
            f.flush()


def append_many(rows_in) -> None:
    """Append several rows under one lock acquisition (same guarantees as append)."""
    lines = [json.dumps(_to_row(r), ensure_ascii=True) + "\n" for r in rows_in]
    if not lines:
        return
    p = path()
    with _lock:
        p.parent.mkdir(parents=True, exist_ok=True)
        with p.open("a", encoding="utf-8") as f:
            f.write("".join(lines))
            f.flush()


def _read_all() -> list[dict]:
    """All parseable rows in file order; a torn last line is skipped, never repaired."""
    p = path()
    if not p.exists():
        return []
    out = []
    with p.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                obj = json.loads(line)
            except json.JSONDecodeError:
                continue
            if isinstance(obj, dict):
                out.append(obj)
    return out


def rows(batch: str | None = None, split: str | None = None, **where) -> list[dict]:
    """Ledger rows filtered by batch, split and any extra exact-match field filters
    (e.g. rows("dev", run_id=..., card="seeded")). A filter value that is a list, tuple or
    set matches any of its members."""
    if batch is not None:
        where["batch"] = batch
    if split is not None:
        where["split"] = split
    return [r for r in _read_all() if _match(r, where)]


def latest_instances(rows_in: list[dict]) -> dict[str, str | None]:
    """run_id -> run_instance of the last row written for it. A re-run of a run_id (think
    --force, or an arm moving an old folder aside) gets a new run_instance; the ledger keeps
    every attempt's rows, and derived views keep only the latest attempt per run_id."""
    out: dict[str, str | None] = {}
    for r in rows_in:
        out[str(r.get("run_id"))] = r.get("run_instance")
    return out


def current_rows(rows_in: list[dict]) -> list[dict]:
    """Rows of the latest instance of each run_id (rows without run_instance are kept)."""
    latest = latest_instances(rows_in)
    return [r for r in rows_in
            if r.get("run_instance") is None or r.get("run_instance") == latest.get(str(r.get("run_id")))]


def _match(r: dict, where: dict) -> bool:
    for k, v in where.items():
        if isinstance(v, (list, tuple, set, frozenset)):
            if r.get(k) not in v:
                return False
        elif r.get(k) != v:
            return False
    return True
