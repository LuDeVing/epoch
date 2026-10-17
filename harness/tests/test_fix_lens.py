"""Issue 1: the map lens is a factor separate from the replicate.

By default every replicate uses the lens "parts" (lens_design "fixed"); --lens-by-replicate opts into the old
pairing (lens = LENSES[replicate % n], lens_design "by_replicate"). Both fields reach state.json,
problem_tree.json, answer.json and report.json. Mock backend only.
"""
from __future__ import annotations

import json
import sys

import pytest

from harness import config
from nano import loop as L
from nano import tree


class _Stop(Exception):
    def __init__(self, nano_loop):
        super().__init__("stopped before run")
        self.loop = nano_loop


def _parsed(monkeypatch, *flags, replicate=0):
    """Run nano.loop.main up to loop.run() and return the configured NanoLoop."""
    def fake_run(self):
        raise _Stop(self)
    monkeypatch.setattr(L.NanoLoop, "run", fake_run)
    monkeypatch.setattr(sys, "argv", ["loop", "--profile", "llm", "--backend", "mock", "--batch", "mock-fix-lens-args",
                                      "--replicate", str(replicate), *flags])
    with pytest.raises(_Stop) as e:
        L.main()
    return e.value.loop


def test_default_lens_is_fixed_parts_for_every_replicate(monkeypatch):
    for r in range(5):
        lp = _parsed(monkeypatch, replicate=r)
        assert (lp.lens, lp.lens_design) == ("parts", "fixed"), r


def test_lens_by_replicate_cycles(monkeypatch):
    names = list(tree.LENSES)
    got = [_parsed(monkeypatch, "--lens-by-replicate", replicate=r) for r in range(5)]
    assert [g.lens for g in got] == [names[r % len(names)] for r in range(5)]
    assert {g.lens_design for g in got} == {"by_replicate"}
    assert len({g.lens for g in got}) > 1


def test_explicit_lens_is_fixed_and_excludes_by_replicate(monkeypatch):
    lp = _parsed(monkeypatch, "--lens", "dynamics", replicate=3)
    assert (lp.lens, lp.lens_design) == ("dynamics", "fixed")
    monkeypatch.setattr(sys, "argv", ["loop", "--profile", "llm", "--lens", "dynamics", "--lens-by-replicate"])
    with pytest.raises(SystemExit):
        L.main()


def test_missing_lens_falls_back_to_first_with_note():
    lenses = {"shape": "a", "flow": "b"}                 # a profile without "parts"
    lens, design, note = L.choose_lens(None, 4, False, lenses)
    assert (lens, design) == ("shape", "fixed") and "parts" in note
    assert L.choose_lens(None, 1, True, lenses) == ("flow", "by_replicate", "")
    assert tree.planner_prompt.__defaults__[0] == "parts"


def test_profiles_have_default_lens():
    from nano import profile as PF
    for name in ("llm", "binpack", "binpack_nobase", "review_process"):
        assert L.DEFAULT_LENS in PF.load(name).lenses, name


def _mock_run(monkeypatch, batch, *flags):
    """A tiny dry run through nano.dry_run (mock replies). binpack_nobase checks on the CPU in seconds."""
    from nano import dry_run
    from nano.checks import script
    monkeypatch.setattr(script, "PY", config.VENV_PYTHON, raising=False)
    monkeypatch.setattr(sys, "argv", ["dry_run", "--profile", "binpack_nobase", "--batch", batch, "--max-sketch-calls", "6",
                                      "--implement", "1", "--rounds", "1", *flags])
    assert dry_run.main() == 0
    runs = [p for p in config.RUNS_DIR.iterdir() if p.name.startswith(batch + "__")]
    assert len(runs) == 1
    return runs[0]


def test_mock_run_records_lens(monkeypatch):
    run = _mock_run(monkeypatch, "mock-fix-lens", "--replicate", "1")     # one small run (load rule)
    for f in ("state.json", "problem_tree.json", "answer.json", "report.json", "commitments.json"):
        d = json.loads((run / f).read_text(encoding="utf-8"))
        assert (d.get("lens"), d.get("lens_design")) == ("parts", "fixed"), f
