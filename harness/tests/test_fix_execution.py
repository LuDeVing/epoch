"""Fix pass, section F (the loop's execution half): resume keeps the spend, a control arm has its own folder and
labels and spends the same budget, the reference survives a resume, controls and tuning are not re-run on resume,
a retest updates the pool, builds in flight count against the budget, hash memory is keyed on the baseline text,
a malformed control.json keeps the last good one, Mode 3 refuses a same-model judge, outcome lessons land.

Mock backend and tmp_path only (conftest repoints the lab root); the checker is stubbed, nothing is trained."""
from __future__ import annotations

import json
import threading
import time
from concurrent.futures import ThreadPoolExecutor

import pytest

from harness import config, llm
from harness.schemas import Candidate, write_json
from nano import profile as PF


@pytest.fixture(autouse=True)
def _llm_profile():
    prev = PF.current()
    PF.set_current("llm")
    yield
    PF.set_current(prev)
    llm.set_mock(None)


def _loop(batch="fx-exec", budget=1_000_000, arm="scaffold", rep=0):
    from nano.loop import NanoLoop
    lp = NanoLoop(batch, rep, "mock", budget, 2, 0.0, None, arm=arm)
    write_json(lp.run_dir / "state.json", {"run_id": lp.run_id, "arm": lp.arm, "decisions": []})
    (lp.run_dir / "problem.md").write_text("# Problem\n\nGOAL: lower loss\n\nHARD CONSTRAINTS:\nC1. rules\n", encoding="utf-8")
    return lp


def _builder_mock():
    """Each build reply is the baseline plus a distinct comment, so dedup keeps every one."""
    from nano.loop import baseline_path
    base = baseline_path().read_text(encoding="utf-8")
    n = {"i": 0}
    lock = threading.Lock()

    def fn(prompt, role, meta):
        with lock:
            n["i"] += 1
            i = n["i"]
        return f"HYPOTHESIS: variant {i}\nCHANGE: a comment\nFIDELITY: exact\n```python\n{base}\n# variant {i}\n```\n"
    return fn


def _stub_checker(lp, status_of=lambda cid: "checked", calls=None):
    def check(candidate, out, baseline, **kw):
        cid = candidate.stem
        if calls is not None:
            calls.append(cid)
        st = status_of(cid)
        return {"candidate": cid, "rungs": [], "status": st, "rung_reached": 3 if st == "checked" else 2,
                "partial_score": 0.75 if st == "checked" else 0.5, "feedback": {} if st == "checked" else {"rung": 2, "reason": "slow"},
                "metrics": {"learn_gap": -0.01, "learn_z": -1.5, "changed_symbols": ["Block"]}}
    lp.checker.check = check


def _state(lp):
    return json.loads((lp.run_dir / "state.json").read_text(encoding="utf-8"))


# ------------------------------------------------------------------ F2: a crash mid-round keeps the spend
def test_resume_after_mid_round_crash_keeps_spend():
    llm.set_mock(_builder_mock())
    lp = _loop("fx-crash")
    lp.round_now = 1
    c1 = lp.run_card("formal", 1, "none", "", None, None, "first")
    assert c1 is not None and lp.spent > 0
    st = _state(lp)                                   # written after the build, before any stage boundary
    assert st["spent"] == lp.spent and st["spent_by_stage"] == lp.spent_by_stage
    lp.run_card("formal", 1, "none", "x", None, None, "first")
    lp._stage(1, "ideated")
    spent, by_stage, n_dec = lp.spent, dict(lp.spent_by_stage), len(lp.decisions)
    # crash: no round end, no _finish. A new process resumes the same folder.
    from nano.loop import NanoLoop
    lp2 = NanoLoop("fx-crash", 0, "mock", 1_000_000, 2, 0.0, None)
    lp2.resume = True
    lp2.load_state()
    lp2._write_commitments()                          # run() writes the commitments after load_state
    assert lp2.spent == spent and lp2.spent_by_stage == by_stage
    assert len([d for d in lp2.decisions if d.get("step") != "resume"]) == n_dec
    assert _state(lp2)["spent"] == spent and _state(lp2)["commitments_hash"]
    assert _state(lp2)["stage"]["step"] == "ideated"


# ------------------------------------------------------------------ F1 + F7: the plain arm
def test_plain_arm_own_folder_labels_and_budget(monkeypatch):
    from harness import ledger
    rows = []
    monkeypatch.setattr(ledger, "append", lambda row: rows.append(row))
    llm.set_mock(_builder_mock())
    scaf = _loop("fx-arm", arm="scaffold")
    budget = 120_000
    lp = _loop("fx-arm", budget=budget, arm="plain")
    assert "__plain__" in lp.run_id and lp.run_dir != scaf.run_dir and "__scaffold__" in scaf.run_id
    _stub_checker(lp)
    lp.long_steps = 0
    est = len(lp.spec_prompt("formal", "", "none", None, None)) // 4 + 12000
    ans = lp.run_control(time.time())
    builds = [r for r in rows if r.card in ("seeded", "formal", "docs", "low_prior")]
    assert builds and all(r.arm == "plain" for r in rows)
    assert all(r.run_id == lp.run_id for r in rows)
    assert lp.spent <= budget and budget - lp.spent < 2 * est      # spent to the budget, not a fixed 12 builds
    dec = next(d for d in lp.decisions if d.get("step") == "control")
    assert dec["stopped"] in ("budget", "no build was affordable")
    # the same round-1 controls and tuning sweep as the scaffold
    assert (lp.run_dir / "controls.json").exists() and (lp.run_dir / "tuning.json").exists()
    assert ans["arm"] == "plain"
    # builders see the rules in canonical order, like the scaffold's builders
    from nano.loop import constraints
    for card in ("seeded", "low_prior", "docs", "formal"):
        p = lp.spec_prompt(card, "river", "none", None, None)
        assert "HARD CONSTRAINTS:\n" + "\n".join(constraints()) in p


# ------------------------------------------------------------------ F3: Mode 2 resume keeps the reference
def test_reference_restored_on_resume():
    PF.set_current("binpack_nobase")
    lp = _loop("fx-ref")
    ref = {"cand_id": "n_ref1", "path": "x.py", "metrics": {"learn_score": 1.1}, "round": 1, "reason": "the first", "set_at": "t"}
    prof = {"ok": True, "score": 1.1, "seed_scores": {"0": 1.1}}
    write_json(lp.run_dir / "reference.json", {"reference": ref, "log": [{"action": "set", "to": "n_ref1"}], "profile": prof})
    from nano.loop import NanoLoop
    lp2 = NanoLoop("fx-ref", 0, "mock", 1_000_000, 2, 0.0, None)
    lp2.resume = True
    lp2.load_state()
    assert lp2.reference["cand_id"] == "n_ref1" and lp2.reference_log[0]["to"] == "n_ref1"
    assert lp2._load_profile() == prof
    # without a reference on disk, a no-baseline profile still starts empty
    lp3 = NanoLoop("fx-ref-new", 0, "mock", 1_000_000, 2, 0.0, None)
    assert lp3._load_profile() == {} and lp3.reference is None


# ------------------------------------------------------------------ F4: controls and tuning are not re-run on resume
def test_controls_and_tuning_not_rerun_on_resume():
    lp = _loop("fx-ctl")
    calls = []
    _stub_checker(lp, status_of=lambda cid: "fail" if cid == "ctl_lr_x10" else "checked", calls=calls)
    lp.tune_knobs = []
    lp.run_controls(1)
    lp.run_tuning(1)
    first = list(calls)
    assert first and any(c.startswith("ctl_") for c in first)
    from nano.loop import NanoLoop
    lp2 = NanoLoop("fx-ctl", 0, "mock", 1_000_000, 2, 0.0, None)
    lp2.resume = True
    lp2.load_state()
    calls2 = []
    _stub_checker(lp2, calls=calls2)
    n_before = len(lp2.cands)
    lp2.run_controls(1)
    lp2.run_tuning(1)
    assert calls2 == [] and len(lp2.cands) == n_before
    ids = [c.id for c in lp2.cands]
    assert len(ids) == len(set(ids))
    rep = json.loads((lp2.run_dir / "controls.json").read_text(encoding="utf-8"))
    assert rep and all(v.get("resumed") for v in rep.values() if v.get("status"))
    # the resume near-list never queues a control, a tuning knob or a composite for revision
    near = [c for c in lp2.cands if lp2.vres.get(c.id, {}).get("status") == "fail"
            and not c.card.startswith("control") and c.card not in ("tune", "compose")]
    assert "ctl_lr_x10" in lp2.vres and all(c.id != "ctl_lr_x10" for c in near)


# ------------------------------------------------------------------ F8: a retest updates the pool
def test_retest_updates_pool():
    PF.set_current("binpack_nobase")
    lp = _loop("fx-retest")
    for cid in ("n_a", "n_b"):
        c = Candidate(id=cid, text=cid, card="implement", operator="x", seed="", perm=0, round=1, call_id="c",
                      program="x = 1\n", extra={"hypothesis": cid})
        lp.cands.append(c)
        (lp.run_dir / "cands" / "src" / f"{cid}.py").write_text("x = 1\n", encoding="utf-8")
        lp.vres[cid] = {"status": "checked", "rung_reached": 3, "partial_score": 0.75, "feedback": {},
                        "metrics": {"learn_gap": -0.1 if cid == "n_a" else -0.05}}
        (lp.run_dir / "pool" / f"{cid}.py").write_text("x = 1\n", encoding="utf-8")
        write_json(lp.run_dir / "pool" / f"{cid}.json", {"id": cid, "metrics": {"learn_gap": -0.1}})
    _stub_checker(lp, status_of=lambda cid: "fail" if cid == "n_a" else "checked")
    lp._retest_top(3, "n_ref", 2)
    assert not (lp.run_dir / "pool" / "n_a.py").exists() and not (lp.run_dir / "pool" / "n_a.json").exists()
    d = json.loads((lp.run_dir / "pool" / "n_b.json").read_text(encoding="utf-8"))
    assert d["retested_against"] == "n_ref" and d["metrics"]["learn_z"] == -1.5


# ------------------------------------------------------------------ F9: builds in flight count against the budget
def test_afford_counts_builds_in_flight():
    lp = _loop("fx-afford")
    est = len(lp.spec_prompt("formal", "", "none", None, None)) // 4 + 12000
    lp.B = 2 * est + 100                                # room for two builds at their estimate, not six
    started = []
    gate = threading.Event()
    base = _builder_mock()

    def slow(prompt, role, meta):
        started.append(1)
        gate.wait(5)                                    # nobody returns before all six were launched
        return base(prompt, role, meta)
    llm.set_mock(slow)

    def one(i):
        return lp.run_card("formal", 1, "none", str(i), None, None, "first")
    with ThreadPoolExecutor(max_workers=6) as ex:
        futs = [ex.submit(one, i) for i in range(6)]
        t0 = time.time()
        while len(started) < 2 and time.time() - t0 < 5:
            time.sleep(0.01)
        time.sleep(0.2)
        gate.set()
        res = [f.result() for f in futs]
    assert len(started) == 2 and sum(1 for r in res if r) == 2
    assert lp.reserved == 0 and lp.reserved_build == 0 and lp.spent <= lp.B
    assert sum(1 for d in lp.decisions if d.get("action") == "budget_skip") == 4


# ------------------------------------------------------------------ F5 + F14: hash memory
def test_hash_memory_keyed_on_baseline_text_and_keeps_provenance():
    lp = _loop("fx-hash")
    lp.backend = "cli_json"                             # _remember_hash is off on mock; no model is called here
    c = Candidate(id="n_h1", text="t", card="implement", operator="x", seed="", perm=0, round=1, call_id="c",
                  extra={"src_hash": "abc123"})
    rec = {"status": "checked", "rung_reached": 3, "metrics": {"learn_gap": -0.01}, "feedback": {}}
    lp._remember_hash(c, rec)
    p = config.MEMORY_DIR / "experiments" / "verified_by_hash.json"
    disk = json.loads(p.read_text(encoding="utf-8"))
    assert disk["abc123"]["ladder"]["run"] == lp.run_id and disk["abc123"]["ladder"]["baseline_hash"]
    # another process wrote a key meanwhile: the merge keeps it (no whole-file rewrite of a stale copy)
    disk["zzz"] = {"ladder": {"run": "other"}}
    write_json(p, disk)
    c2 = Candidate(id="n_h2", text="t", card="implement", operator="x", seed="", perm=0, round=1, call_id="c",
                   extra={"src_hash": "def456"})
    lp._remember_hash(c2, rec)
    disk = json.loads(p.read_text(encoding="utf-8"))
    assert "zzz" in disk and "def456" in disk and "abc123" in disk
    # a later run reuses it; reuse never overwrites the provenance
    lp2 = _loop("fx-hash2")
    lp2.backend = "cli_json"
    c3 = Candidate(id="n_h3", text="t", card="implement", operator="x", seed="", perm=0, round=1, call_id="c",
                   extra={"src_hash": "abc123"})
    got = lp2._recall_hash(c3)
    assert got and got["reused_from"] == f"{lp.run_id}/n_h1"
    lp2._remember_hash(c3, got)
    disk = json.loads(p.read_text(encoding="utf-8"))
    assert disk["abc123"]["ladder"]["run"] == lp.run_id and disk["abc123"]["ladder"]["cand_id"] == "n_h1"
    # an edited baseline text (same version) is not served the old verdict
    lp2.baseline_src = lp2.baseline_src + "\n# edited\n"
    assert lp2._recall_hash(c3) is None


# ------------------------------------------------------------------ F12: malformed control.json
def test_malformed_control_keeps_last_good(capsys):
    lp = _loop("fx-ctlfile")
    (lp.run_dir / "control.json").write_text(json.dumps({"note": "keep going", "skip_nodes": ["opt"]}), encoding="utf-8")
    lp._stage(1, "ideated")
    assert lp.control_note == "keep going" and lp.skip_nodes == {"opt"}
    (lp.run_dir / "control.json").write_text('{"note": "half writ', encoding="utf-8")
    lp._stage(1, "clustered")
    assert lp.control_note == "keep going" and lp.skip_nodes == {"opt"}
    assert any(d.get("warning", "").startswith("control.json unreadable") for d in lp.decisions)
    assert "WARNING" in capsys.readouterr().out


# ------------------------------------------------------------------ F15: Mode 3 judge model
def test_mode3_judge_must_differ_from_generator():
    PF.set_current("review_process")
    lp = _loop("fx-judge")
    lp.backend = "cli_json"                             # a real backend: no silent fallback (nothing is called here)
    with pytest.raises(SystemExit, match="judge model"):
        lp._resolve_judge_model()
    lp.judge_model = lp.model or config.DEFAULT_MODEL
    with pytest.raises(SystemExit, match="generator"):
        lp._resolve_judge_model()
    lp.judge_model = "some-other-model" if lp.judge_model != "some-other-model" else "another"
    assert lp._resolve_judge_model() == lp.judge_model and lp.checker.impl.judge_model == lp.judge_model


# ------------------------------------------------------------------ F10: outcome lessons from the overnight results
def test_outcome_lessons_from_rung5_and_repeat_safe(tmp_path):
    from nano import lessons as LS
    run = tmp_path / "run1"
    (run / "rung5").mkdir(parents=True)
    write_json(run / "rung5" / "results.json", {"candidates": {
        "n_win": {"status": "verified", "hypothesis": "gated attention helps", "node": "attn", "n": 3, "delta": -0.01},
        "n_lose": {"status": "fail", "hypothesis": "bigger lr helps", "node": "opt", "n": 3, "delta": 0.02},
        "control_lr_x10": {"status": "fail", "hypothesis": "control", "control": "lr_x10", "n": 3}}})
    path = tmp_path / "lessons.jsonl"
    LS.update_from_run(run, path, "v2")
    LS.update_from_run(run, path, "v2")                 # the loop's _finish and batch_verify both call it
    out = [e for e in LS.load(path) if e["kind"] == "outcome"]
    assert {e["scope"]["part"] for e in out} == {"attn", "opt"}
    assert all(e["helpful"] + e["harmful"] == 1 for e in out)
    assert "did not help over 3 seeds" in LS.render(path, "opt", kind="outcome", version="v2")
