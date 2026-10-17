"""The baseline's version. Every verdict is recorded against the baseline it was measured on, so a
promoted winner (nano/promote.py) never gets compared with results from an older recipe."""
from __future__ import annotations

from pathlib import Path

HERE = Path(__file__).resolve().parent
VERSION_FILE = HERE / "baselines" / "VERSION"


def baseline_version() -> str:
    try:
        return VERSION_FILE.read_text(encoding="utf-8").strip() or "v1"
    except FileNotFoundError:
        return "v1"
