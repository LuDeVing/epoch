"""Resume (NanoLoop.load_state, --resume) and the stage boundary (--stop-after, control.json), on the mock backend in
the test's temp lab. The documented behaviour these tests hold the loop to:
- the spend is written at every stage boundary and after every build, so a crash mid-round resumes with it;
- Mode 2 (no baseline): the reference and its measured profile survive a resume (reference.json);
- controls that already went up the ladder before the interruption are not run again;
- --stop-after stops cleanly after the named stage; control.json can stop, add budget once, and a malformed file
  keeps the last good control.
Nothing here trains a model or needs the GPU: Mode 2 checks the bin-packing scorer on the CPU, and the Mode 1 tests
stub the checker."""
from __future__ import annotations

import json
import sys

import pytest

from harness import config, llm
from nano import loop as L
from nano import profile as PF


def _loop(profile: str, batch: str, resume: bool = False) -> L.NanoLoop:
    PF.set_current(profile)
    lp = L.NanoLoop(batch, 0, "mock", 100_000, 1, 60.0, None)
    lp.resume = resume
    return lp


def _state(run_dir) -> dict:
    return json.loads((run_dir / "state.json").read_text(encoding="utf-8"))


# ---------------------------------------------------------------- stage boundary and control.json
def test_stage_writes_the_spend_and_load_state_reads_it_back():
    lp = _loop("binpack_nobase", "mock-resume-unit")
    lp.spent, lp.spent_aux, lp.spent_by_stage = 1234, 56, {"ideate": 1000, "build": 234}
    lp._stage(1, "ideated")
    st = _state(lp.run_dir)
    assert (st["spent"], st["spent_aux"], st["spent_by_stage"]) == (1234, 56, {"ideate": 1000, "build": 234})
    assert st["stage"]["step"] == "ideated" and st["stage"]["round"] == 1
    back = _loop("binpack_nobase", "mock-resume-unit", resume=True)
    back.load_state()
    assert (back.spent, back.spent_aux, back.spent_by_stage) == (1234, 56, {"ideate": 1000, "build": 234})
    assert back.completed_rounds == 0                       # "ideated" does not complete a round
    back._write_state()                                     # the next write carries the spend, never a reset to 0
    assert _state(back.run_dir)["spent"] == 1234


def test_stop_after_raises_only_at_its_stage():
    lp = _loop("binpack_nobase", "mock-stop-unit")
    lp.stop_after = "clustered"
    lp._stage(1, "ideated")                                 # another stage: no stop
    with pytest.raises(L.StopRun):
        lp._stage(1, "clustered")
    assert _state(lp.run_dir)["stage"]["step"] == "clustered"   # the boundary was recorded before the stop


def test_control_file_stop_budget_once_and_malformed_keeps_last_good():
    lp = _loop("binpack_nobase", "mock-control-unit")
    ctl = lp.run_dir / "control.json"
    b0 = lp.B
    ctl.write_text(json.dumps({"budget_add": 500, "note": "look at packing order", "skip_nodes": ["x"]}), encoding="utf-8")
    lp._stage(1, "ideated")
    lp._stage(1, "clustered")                              # the same file again: the budget is added once
    assert lp.B == b0 + 500 and lp.control_note == "look at packing order" and lp.skip_nodes == {"x"}
    ctl.write_text('{"stop_after_stage": true, ', encoding="utf-8")   # half-written: the last good control holds
    lp._stage(1, "deepened")
    assert lp.B == b0 + 500 and lp.skip_nodes == {"x"}
    assert any("unreadable" in d.get("warning", "") for d in lp.decisions if d.get("step") == "control")
    ctl.write_text(json.dumps({"stop_after_stage": True}), encoding="utf-8")
    with pytest.raises(L.StopRun):
        lp._stage(1, "built")
    log = [json.loads(x) for x in (lp.run_dir / "control_log.jsonl").read_text(encoding="utf-8").splitlines()]
    assert any(r.get("control", {}).get("budget_add") == 500 for r in log)


def test_stop_after_on_a_mock_run(monkeypatch):
    """--stop-after ideated through nano.dry_run: the run stops cleanly, writes its files and says why."""
    from nano import dry_run
    monkeypatch.setattr(sys, "argv", ["dry_run", "--profile", "binpack_nobase", "--batch", "mock-stop-run",
                                      "--implement", "1", "--rounds", "1", "--max-sketch-calls", "6",
                                      "--stop-after", "ideated"])
    assert dry_run.main() == 0
    run = next(config.RUNS_DIR.glob("mock-stop-run__*"))
    st = _state(run)
    assert any(d.get("step") == "stopped" and d.get("after") == "ideated" for d in st["decisions"])
    assert st["stage"]["step"] == "ideated"
    assert (run / "ideas.jsonl").exists() and not list((run / "cands").glob("*.jsonl"))   # nothing was built


# ---------------------------------------------------------------- Mode 2: a crash mid-round, then --resume
class _Crash(BaseException):
    """A hard stop (like a killed process): not an Exception, so no handler in the loop swallows it."""


def test_mode2_crash_mid_round_then_resume_keeps_spend_and_reference(monkeypatch):
    from pathlib import Path
    from nano import dry_run
    from nano.checks import script
    monkeypatch.setattr(script, "PY", Path(sys.executable))   # the lab root is a temp folder in tests: no venv there
    batch = "mock-resume-mode2"
    argv = ["dry_run", "--profile", "binpack_nobase", "--batch", batch, "--implement", "2", "--rounds", "1",
            "--max-sketch-calls", "8"]
    real_verify = L.NanoLoop.verify
    seen: dict = {}

    def crashing_verify(self, cand, round_no):
        if (self.run_dir / "reference.json").exists():     # the reference is set: crash on the next check
            seen["spent"], seen["reference"] = self.spent, self.reference["cand_id"]
            raise _Crash()
        return real_verify(self, cand, round_no)
    monkeypatch.setattr(L.NanoLoop, "verify", crashing_verify)
    monkeypatch.setattr(sys, "argv", argv)
    with pytest.raises(_Crash):
        dry_run.main()
    run = next(config.RUNS_DIR.glob(batch + "__*"))
    assert seen["spent"] > 0, "the crash came before any model call was paid for"
    assert _state(run)["spent"] == seen["spent"]           # the spend at the crash is on disk
    ref_before = json.loads((run / "reference.json").read_text(encoding="utf-8"))
    assert ref_before["reference"]["cand_id"] == seen["reference"]

    # resume: the spend and the reference come back before anything new is paid for or checked
    monkeypatch.setattr(L.NanoLoop, "verify", real_verify)
    real_load_state, real_load_profile = L.NanoLoop.load_state, L.NanoLoop._load_profile
    after: dict = {}

    def load_state(self):
        real_load_state(self)
        after["spent"], after["reference"] = self.spent, (self.reference or {}).get("cand_id")

    def load_profile(self):
        prof = real_load_profile(self)
        after["profile"] = prof
        return prof
    monkeypatch.setattr(L.NanoLoop, "load_state", load_state)
    monkeypatch.setattr(L.NanoLoop, "_load_profile", load_profile)
    monkeypatch.setattr(sys, "argv", argv + ["--resume"])
    try:
        assert dry_run.main() == 0
    finally:
        llm.set_mock(None)
    assert after["spent"] == seen["spent"] and after["reference"] == seen["reference"]
    assert after["profile"] == ref_before["profile"]       # the reference's measured profile, not re-measured
    st = _state(run)
    assert st["spent"] >= seen["spent"]
    res = next(d for d in st["decisions"] if d.get("step") == "resume" and "unverified" in d)
    assert res["unverified"], "the candidate whose check crashed is waiting"
    verified = {json.loads(x)["id"] for x in (run / "verify.jsonl").read_text(encoding="utf-8").splitlines() if x.strip()}
    assert set(res["unverified"]) <= verified                # and is checked after the resume
    assert any(d.get("step") == "baseline" and "resume" in d.get("note", "") for d in st["decisions"])
    ref_log = json.loads((run / "reference.json").read_text(encoding="utf-8"))["log"]
    assert ref_log[0] == ref_before["log"][0]              # the history before the crash is kept, not restarted


def test_mode2_unreadable_reference_on_resume_falls_back():
    lp = _loop("binpack_nobase", "mock-resume-badref")
    (lp.run_dir / "reference.json").write_text("{not json", encoding="utf-8")
    back = _loop("binpack_nobase", "mock-resume-badref", resume=True)
    back.load_state()
    assert back.reference is None
    assert back._load_profile() == {}                       # no reference: the next checked candidate becomes it


# ---------------------------------------------------------------- Mode 1: controls are not run twice
def _fake_check(calls: list):
    def check(src, out, profile, **kw):
        name = str(src).replace("\\", "/").rsplit("/", 1)[-1][:-3]
        calls.append(name)
        status = "checked" if name == "ctl_zero_init_proj" else "fail"
        return {"status": status, "rung_reached": 3, "partial_score": 0.5,
                "feedback": {"rung": 3, "reason": "at step 12 the gap was 0.1"} if status == "fail" else {},
                "metrics": {"learn_z": 1.5 if status == "checked" else -0.2}}
    return check


def test_controls_are_not_rerun_after_a_resume():
    batch = "mock-resume-controls"
    first = _loop("llm", batch)
    calls: list = []
    first.checker.check = _fake_check(calls)                # no training: a canned ladder record per control
    first.run_controls(1)
    report1 = json.loads((first.run_dir / "controls.json").read_text(encoding="utf-8"))
    assert sorted(calls) == ["ctl_lr_x10", "ctl_placebo_order", "ctl_zero_init_proj"]
    assert all(r["ok"] for r in report1.values()), report1

    back = _loop("llm", batch, resume=True)
    again: list = []
    back.checker.check = _fake_check(again)
    back.load_state()
    assert {"ctl_lr_x10", "ctl_placebo_order", "ctl_zero_init_proj"} <= set(back.vres)
    back.run_controls(1)
    assert again == []                                       # nothing went up the ladder a second time
    report2 = json.loads((back.run_dir / "controls.json").read_text(encoding="utf-8"))
    assert set(report2) == set(report1)
    for name, r in report2.items():
        assert r.get("resumed") is True and r["status"] == report1[name]["status"] and r["ok"] == report1[name]["ok"]
    assert len([c for c in back.cands if c.id.startswith("ctl_")]) == 3   # no duplicate control candidates
