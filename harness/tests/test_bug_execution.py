"""Bug pass 2026-10-17 (night), the loop's second half: report.json keys survive a later report.write, one failing report section does not skip the rest,
the commitments hash is stable across a resume, a resume keeps tuning prunes and the hedge lane, a resume after
the stage 'built' does not build the round again, and `python -m nano.report` prints on a cp1252 console.

Mock backend and tmp_path only (conftest repoints the lab root); nothing is trained."""
from __future__ import annotations

import io
import json
import sys
import time

import pytest

from harness import config, llm
from harness.schemas import Candidate, append_jsonl, write_json
from nano import loop as L
from nano import profile as PF


class _Crash(BaseException):
    """A hard stop (like a killed process): not an Exception, so no handler in the loop swallows it."""


def _loop(batch: str, profile: str = "llm", resume: bool = False, fresh_state: bool = True) -> L.NanoLoop:
    PF.set_current(profile)
    lp = L.NanoLoop(batch, 0, "mock", 1_000_000, 1, 0.0, None)
    lp.resume = resume
    if fresh_state:
        write_json(lp.run_dir / "state.json", {"run_id": lp.run_id, "arm": lp.arm, "decisions": []})
        (lp.run_dir / "problem.md").write_text("# Problem\n\nGOAL: x\n\nHARD CONSTRAINTS:\nC1. rules\n", encoding="utf-8")
    return lp


def _state(lp) -> dict:
    return json.loads((lp.run_dir / "state.json").read_text(encoding="utf-8"))


# ------------------------------------------------------------------ report.write keeps the loop's keys
def test_report_write_keeps_keys_the_loop_added(tmp_path):
    from nano import report
    run = tmp_path / "run"
    run.mkdir()
    (run / "report.json").write_text(json.dumps({"memory": {"parts": 2}, "dialogue": "off", "fetched_facts": {"requests": 1},
                                                 "questions": [{"round": 2}], "built": 999}), encoding="utf-8")
    report.write(run)                                   # batch_verify rewrites the report after the night
    d = json.loads((run / "report.json").read_text(encoding="utf-8"))
    assert d["memory"] == {"parts": 2} and d["dialogue"] == "off" and d["fetched_facts"] == {"requests": 1}
    assert d["questions"] == [{"round": 2}]
    assert d["built"] == 0                              # collect()'s own keys are refreshed, not kept


# ------------------------------------------------------------------ _finish: one failing section skips nothing else
def test_finish_report_sections_are_independent(monkeypatch):
    lp = _loop("bug-finish")
    lp.long_steps = 0
    with (lp.run_dir / "dialogue.jsonl").open("w", encoding="utf-8") as f:
        f.write(json.dumps({"idea": "k1", "round": 1, "reply": "concede", "verdict": "revised"}) + "\n")
        f.write('{"idea": "k2", "round": 1, "rep')            # a line cut by a crash
    monkeypatch.setattr(L.NanoLoop, "_report_premortem", lambda self: (_ for _ in ()).throw(RuntimeError("boom")))
    lp._finish(time.time())
    rep = json.loads((lp.run_dir / "report.json").read_text(encoding="utf-8"))
    assert "dialogue" in rep and "fetched_facts" in rep and "memory" in rep
    assert any(d.get("step") == "report" and d.get("section") == "premortem" for d in _state(lp)["decisions"])


# ------------------------------------------------------------------ commitments: the same hash after a resume
def test_commitments_hash_stable_across_resume():
    lp = _loop("bug-commit")
    lp._write_commitments()
    h1 = _state(lp)["commitments_hash"]
    c1 = json.loads((lp.run_dir / "commitments.json").read_text(encoding="utf-8"))
    time.sleep(1.1)                                     # now_ts has one-second resolution
    back = _loop("bug-commit", resume=True, fresh_state=False)
    back.load_state()
    back._write_commitments()
    assert _state(back)["commitments_hash"] == h1
    assert json.loads((back.run_dir / "commitments.json").read_text(encoding="utf-8")) == c1


# ------------------------------------------------------------------ resume keeps tuning prunes and the hedge lane
def _cand_row(cid: str, card: str) -> dict:
    c = Candidate(id=cid, text="t", card=card, operator="o", seed="", perm=0, round=1, call_id="", parent_ids=[],
                  lineage_id=cid, program="", extra={"hypothesis": "h", "src_hash": "h_" + cid})
    return {**c.to_dict(), "t": time.time()}


def _vrow(cid: str, status: str) -> dict:
    return {"id": cid, "status": status, "partial_score": 0.5, "feedback_record": {},
            "details": {"rung_reached": 3, "metrics": {"learn_z": -1.0}}, "round": 1}


def test_resume_keeps_tune_prunes_and_hedged():
    lp = _loop("bug-prune")
    for cid, card, st in (("tune_lr", "tune", "checked"), ("tune_wd", "tune", "checked"), ("n_h1", "formal", "fail")):
        append_jsonl(lp.run_dir / "cands" / f"x_{cid}.jsonl", _cand_row(cid, card))
        append_jsonl(lp.run_dir / "verify.jsonl", _vrow(cid, st))
    write_json(lp.run_dir / "tuning.json", {"round": 1, "kept": ["tune_wd"],
                                             "knobs": [{"id": "tune_lr", "status": "checked", "kept": False},
                                                       {"id": "tune_wd", "status": "checked", "kept": True}]})
    write_json(lp.run_dir / "state.json", {"run_id": lp.run_id, "decisions": [{"round": 1, "step": "hedge", "cand": "n_h1"}]})
    back = _loop("bug-prune", resume=True, fresh_state=False)
    back.load_state()
    assert back.vres["tune_lr"]["status"] == "tune_pruned"     # no long run, no composite, not in answer.json ranked
    assert back.vres["tune_wd"]["status"] == "checked"
    assert "n_h1" in back.hedged                                # still gets its long run


# ------------------------------------------------------------------ resume after 'built': no second set of builds
def test_resume_after_built_does_not_build_the_round_again(monkeypatch):
    from pathlib import Path
    from nano import dry_run
    from nano.checks import script
    monkeypatch.setattr(script, "PY", Path(sys.executable))
    batch = "mock-bug-built"
    argv = ["dry_run", "--profile", "binpack_nobase", "--batch", batch, "--implement", "2", "--rounds", "1",
            "--max-sketch-calls", "8"]
    real_verify, real_run_card = L.NanoLoop.verify, L.NanoLoop.run_card

    def crashing_verify(self, cand, round_no):
        raise _Crash()
    monkeypatch.setattr(L.NanoLoop, "verify", crashing_verify)
    monkeypatch.setattr(sys, "argv", argv)
    with pytest.raises(_Crash):
        dry_run.main()
    run = next(config.RUNS_DIR.glob(batch + "__*"))
    st = json.loads((run / "state.json").read_text(encoding="utf-8"))
    assert st["stage"]["step"] == "built"
    monkeypatch.setattr(L.NanoLoop, "verify", real_verify)
    cards: list = []

    def counting_run_card(self, card, *a, **kw):
        cards.append(card)
        return real_run_card(self, card, *a, **kw)
    monkeypatch.setattr(L.NanoLoop, "run_card", counting_run_card)
    monkeypatch.setattr(sys, "argv", argv + ["--resume"])
    try:
        assert dry_run.main() == 0
    finally:
        llm.set_mock(None)
    assert not [c for c in cards if c in ("implement", "program")], cards
    st = json.loads((run / "state.json").read_text(encoding="utf-8"))
    res = next(d for d in st["decisions"] if d.get("step") == "resume" and "unverified" in d)
    verified = {json.loads(x)["id"] for x in (run / "verify.jsonl").read_text(encoding="utf-8").splitlines() if x.strip()}
    assert res["unverified"] and set(res["unverified"]) <= verified
    cycle = [d for d in st["decisions"] if d.get("step") == "cycle" and d.get("round") == 1][-1]
    # the builds verified at the resume belong to the round: hedge lane, fail questions and the record see them
    assert set(res["unverified"]) <= set(cycle["checked"]) | set(cycle["failed"])


# ------------------------------------------------------------------ python -m nano.report on a cp1252 console
def test_report_main_prints_non_ascii_on_cp1252(tmp_path, monkeypatch):
    from nano import report
    run = tmp_path / "run"
    (run / "pool").mkdir(parents=True)
    write_json(run / "pool" / "n1.json", {"id": "n1", "node": "mix", "card": "formal", "hypothesis": "lr → 2x, β ≥ 0.9",
                                         "metrics": {}})
    buf = io.TextIOWrapper(io.BytesIO(), encoding="cp1252")
    monkeypatch.setattr(sys, "stdout", buf)
    monkeypatch.setattr(sys, "argv", ["report", "--run", str(run)])
    assert report.main() == 0


# ------------------------------------------------------------------ answer.json lanes: a hedged failure is not "checked"
def test_answer_lanes_checked_skips_hedged_failures():
    lp = _loop("bug-lanes")
    lp.long_steps = 0
    c = Candidate(id="nhedged2", text="x", card="impl:seeded", operator="k", seed="", perm=0, round=1, call_id="c0",
                  lineage_id="nhedged2", program="x\n", extra={"node": "root", "direction": "inward", "lane": "main"})
    lp.cands.append(c)
    lp.vres[c.id] = {"status": "fail", "rung_reached": 3, "partial_score": 0.75, "feedback": {"rung": 3, "reason": "at step 45"},
                     "metrics": {"learn_gap": 0.01, "learn_z": 1.2}}
    lp.hedged.add(c.id)
    ans = lp._finish(0.0)
    assert ans["lanes"]["main"]["checked"] == 0 and ans["n_checked"] == 0
    assert [r["id"] for r in ans["ranked"]] == ["nhedged2"]     # the hedge lane still gets its place in the pool


# ------------------------------------------------------------------ reference.metrics: the copy after relabelling
def test_reference_metrics_taken_after_relabel(monkeypatch):
    from nano.checks import reference as REF
    lp = _loop("bug-ref")
    monkeypatch.setattr(lp.checker, "measure_reference", lambda *a, **k: {"ok": True}, raising=False)
    monkeypatch.setattr(REF, "relabel", lambda checker, m, prof, lower: {"learn_gap": 0.0, "learn_z": 0.0})
    c = Candidate(id="nref1", text="x", card="impl:seeded", operator="k", seed="", perm=0, round=1, call_id="c0",
                  lineage_id="nref1", program="x\n", extra={"hypothesis": "h"})
    rec = {"status": "checked", "rung_reached": 3, "metrics": {"learn_score": 1.5, "learn_z": None}}
    lp._set_reference(c, rec, 1, "first checked")
    assert lp.reference["metrics"]["learn_z"] == 0.0
    on_disk = json.loads((lp.run_dir / "reference.json").read_text(encoding="utf-8"))
    assert on_disk["reference"]["metrics"]["learn_z"] == 0.0


# ------------------------------------------------------------------ failure card: the script checker's rung-2 gap
def test_failure_card_names_a_script_checker_gap_a_learning_failure():
    from nano import lessons as LS
    fb = {"rung": 2, "reason": "the quick score is 0.91 against the baseline's 0.88 on the same instances "
                               "(gap +0.0300, negative is better; z 2.1; allowed 0.0100)"}
    card = LS.failure_card(fb)
    assert "timing" not in card and "CAUSE TAG: learning failure" in card, card
    slow = LS.failure_card({"rung": 2, "reason": "step time 3.10s is more than 2x the baseline's"})
    assert "timing and memory" in slow


def test_commitments_hash_mismatch_on_resume_is_logged():
    lp = _loop("bug-commit2")
    lp._write_commitments()
    cp = lp.run_dir / "commitments.json"
    c = json.loads(cp.read_text(encoding="utf-8"))
    c["ts"] = "1999-01-01T00:00:00"                     # the file changed after its hash went into state.json
    cp.write_text(json.dumps(c), encoding="utf-8")
    back = _loop("bug-commit2", resume=True, fresh_state=False)
    back.load_state()
    h_before = back.commitments_hash
    back._write_commitments()
    assert h_before and back.commitments_hash != h_before
    assert any(d.get("step") == "commitments" and d.get("previous_hash") == h_before for d in _state(back)["decisions"])
