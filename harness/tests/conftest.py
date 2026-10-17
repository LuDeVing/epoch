"""Shared test setup (README "tests/" row): every test runs under a temporary lab root on the
mock backend, so nothing lands in the real lab root on D:.

Two layers, because harness.config binds its paths at import time:
1. the environment is set here, before any test module imports harness, so a plain
   `pytest harness/tests` binds config to a temp root even when a test file forgets to;
2. an autouse fixture repoints every config path to this test's tmp_path, so tests cannot see
   each other's run folders or ledger rows (think raises on an existing run folder).
A second autouse fixture saves and restores the active nano profile and the mock LLM responder:
nano.loop.main installs the --profile it is given globally (PF.set_current) and nano.dry_run installs
its mock, so without it one test's profile or mock leaks into the next.
Tests that need the GPU or the real lab are opt-in: they skip unless an environment variable names the
real resource (test_bench: HTSA_REAL_DATA). None runs by default.
"""
from __future__ import annotations

import os
import sys
import tempfile
from pathlib import Path

if not os.environ.get("HTSA_LAB_ROOT") or Path(os.environ["HTSA_LAB_ROOT"]).resolve() == Path(r"D:\AGI-lab").resolve():
    os.environ["HTSA_LAB_ROOT"] = tempfile.mkdtemp(prefix="htsa_tests_")
os.environ.setdefault("HTSA_BACKEND", "mock")
os.environ.setdefault("HTSA_ARC_SET", "arc1")   # tests use the synthetic ARC-1 shaped fixtures

import pytest  # noqa: E402

from harness import config  # noqa: E402
from nano import profile as PF  # noqa: E402

REAL_LAB_ROOT = Path(r"D:\AGI-lab").resolve()
LAB_PATHS = ("LAB_ROOT", "RUNS_DIR", "MEMORY_DIR", "VIEWS_DIR", "LEDGER_PATH", "DATA_DIR",
             "RESULTS_DIR")


@pytest.fixture(autouse=True)
def _temp_lab_root(tmp_path, monkeypatch):
    """Repoint config's lab paths at tmp_path/lab for every test (RAW_DATA_DIR is left alone:
    data.py tests that read the real downloads override it themselves)."""
    root = tmp_path / "lab"
    paths = {"LAB_ROOT": root, "RUNS_DIR": root / "runs", "MEMORY_DIR": root / "memory",
             "VIEWS_DIR": root / "memory" / "views", "LEDGER_PATH": root / "memory" / "ledger.jsonl",
             "DATA_DIR": root / "data", "RESULTS_DIR": root / "results"}
    for name, p in paths.items():
        monkeypatch.setattr(config, name, p)
        if name != "LEDGER_PATH":
            p.mkdir(parents=True, exist_ok=True)
    monkeypatch.setenv("HTSA_LAB_ROOT", str(root))
    monkeypatch.setenv("HTSA_BACKEND", "mock")
    yield root
    for name in LAB_PATHS:        # a test may repoint paths again, but never at the real lab root
        p = Path(getattr(config, name)).resolve()
        t = tmp_path.resolve()
        assert p == t or t in p.parents, f"{name} escaped tmp_path: {p}"


@pytest.fixture(autouse=True)
def _restore_profile(monkeypatch):
    """Every test starts with no profile installed and HTSA_PROFILE unset (so PF.current() is the default
    profile), and any profile it installs is undone afterwards. The same for the mock LLM responder, which
    nano.dry_run installs and never removes, and for the dry-run mock's reply counters (its replies cycle by
    call count, so a test calling dry_run.mock directly would otherwise see what earlier tests left)."""
    from harness import llm
    prev, prev_mock = PF._current, llm._mock_fn
    monkeypatch.delenv("HTSA_PROFILE", raising=False)
    PF._current = None
    dry = sys.modules.get("nano.dry_run")
    if dry is not None:
        dry._counter.clear()
    yield
    PF._current = prev
    llm.set_mock(prev_mock)
