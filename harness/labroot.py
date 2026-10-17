"""Where the lab folder is (runs, spaces, memory, results, data), on any computer.

Order: the HTSA_LAB_ROOT environment variable; else the old fixed place D:\\AGI-lab when it exists (this PC);
else a folder named AGI-lab next to the project folder, created on first use. The result is written back into
HTSA_LAB_ROOT so every child process (the loop, the agents, the servers) sees the same folder.
Standard library only; imported by harness.config and by the modules that read the lab root at import time."""
from __future__ import annotations

import os
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
LEGACY = Path(r"D:\AGI-lab")
SUBDIRS = ("runs", "spaces", "memory", "results", "data")
_resolved: Path | None = None


def lab_root(create: bool = True) -> Path:
    """The lab folder as a Path. With create (the default) its sub-folders exist afterwards."""
    global _resolved
    env = os.environ.get("HTSA_LAB_ROOT")
    if env:
        p = Path(env)
    elif _resolved is not None:
        p = _resolved
    elif LEGACY.exists():
        p = LEGACY
    else:
        p = PROJECT_ROOT.parent / "AGI-lab"
    if create:
        ensure(p)
    _resolved = p
    os.environ.setdefault("HTSA_LAB_ROOT", str(p))
    return p


def ensure(p: Path) -> Path:
    """Create the lab folder and its sub-folders; harmless when they exist. A failure (read-only disk) is left to
    the first writer, which reports it with its own path."""
    try:
        for sub in SUBDIRS:
            (p / sub).mkdir(parents=True, exist_ok=True)
    except OSError:
        pass
    return p
