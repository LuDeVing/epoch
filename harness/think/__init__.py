"""Control helpers of the orchestrator loop (ARCHITECTURE.md section 4): dedup, allocate, admit,
stop, stagnation, tournament.

Name clash: the driver module harness/think.py and this package harness/think/ share a name, and
Python resolves `harness.think` to the package. So `from harness.think import think` (and `main`)
are forwarded here to harness/think.py, loaded under the name `harness._think_driver`.
`python -m harness.think` needs harness/think/__main__.py (integrator; see INTEGRATION_NOTES.md).
"""
from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

_DRIVER_NAMES = {"think", "main", "cli", "build_parser"}
_DRIVER_PATH = Path(__file__).resolve().parent.parent / "think.py"
_DRIVER_MOD = "harness._think_driver"


_LOCK = __import__("threading").RLock()   # parallel workers raced: one saw the half-loaded module


def load_driver():
    """Load harness/think.py as harness._think_driver (relative imports resolve to harness)."""
    with _LOCK:
        return _load_driver()


def _load_driver():
    if _DRIVER_MOD in sys.modules and getattr(sys.modules[_DRIVER_MOD], "think", None) is not None:
        return sys.modules[_DRIVER_MOD]
    if not _DRIVER_PATH.exists():
        raise ImportError(f"driver module not found: {_DRIVER_PATH}")
    spec = importlib.util.spec_from_file_location(_DRIVER_MOD, _DRIVER_PATH)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[_DRIVER_MOD] = mod
    try:
        spec.loader.exec_module(mod)
    except Exception:
        sys.modules.pop(_DRIVER_MOD, None)
        raise
    return mod


def __getattr__(name: str):
    if name in _DRIVER_NAMES:
        try:
            return getattr(load_driver(), name)
        except ImportError as e:
            raise AttributeError(f"harness.think has no attribute {name!r} ({e})") from e
    raise AttributeError(f"module 'harness.think' has no attribute {name!r}")
