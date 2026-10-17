"""Fix pass 2026-10-17, section C (orchestrator): thresholds, allocation, memory views, judge
calibration sample, vote selection, run lock. Mock backend, temp lab root, no GPU."""
from __future__ import annotations

import itertools
import json
import os
import random
from pathlib import Path
from types import SimpleNamespace

import pytest

import test_think as tt
from test_think import lab_root, stubs  # noqa: F401 - fixtures

from harness import config, ledger, llm, stats
from harness.probe import ProbeResult, agreement
from harness.schemas import Candidate, VerifyResult, read_json, read_jsonl, write_json
from harness.think import allocate

think = tt.think


def _two_of_three_mock():
    """Probe: correct, correct, wrong; generators: correct."""
    n = itertools.count()

    def fn(prompt, role, meta):
        if role == "defaults":
            return tt.DEFAULTS_REPLY
        if role == "probe":
            prog = tt.CORRECT if next(n) % 3 < 2 else tt.WRONG
            return f"```python\n{prog}```"
        if role in tt.GEN_ROLES:
            return f"1. ```python\n{tt.CORRECT}```"
        return llm._default_mock(prompt, role, meta)
    return fn


# ---------------------------------------------------------------- C1 thresholds
def test_two_of_three_meets_default_thresholds():
    assert think._at_least(2 / 3, config.PARAMS["T"])
    assert think._at_least(2 / 3, config.PARAMS["optout"])
    assert not think._at_least(1 / 3, config.PARAMS["T"])
    assert think._fraction("2/3") == 2 / 3 and think._fraction(0.5) == 0.5


def test_early_stop_fires_at_two_of_three(stubs):  # noqa: F811
    item = tt.arc_item("t_23")
    llm.set_mock(_two_of_three_mock())
    ans = think.think(item, m=20, replicate=0, backend="mock", batch="tc_23", params={"T": "2/3"})
    st = read_json(tt.run_dir_of("tc_23", item) / "state.json")
    cyc = [d for d in st["decisions"] if d["step"].startswith("cycle")]
    assert ans.status == "solved" and cyc[0]["action"] == "stop_verified"
    assert st["params"]["T"] == 2 / 3


def test_probe_parse_failures_not_in_denominator():
    from harness.think.dedup import dedup_key
    c = Candidate(id="x", text="B", card="seeded", operator="none", seed="", perm=0, round=0,
                  call_id="c", pred="B")
    pr = ProbeResult(clusters={dedup_key(c, "bt"): 2}, n=2, usage=None, n_calls=3)
    assert agreement(pr, c, "bt") == 1.0


# ---------------------------------------------------------------- C2, C4, C10, C11 allocation
def test_rng_keyed_per_item():
    a = [allocate.initial("bt", "bt_sp", None, 4, 0, 0, item_id=f"i{k}") for k in range(12)]
    assert len({s[0].seed for s in a}) > 1                         # seed word varies by item
    again = allocate.initial("bt", "bt_sp", None, 4, 0, 0, item_id="i3")
    assert again == a[3]                                           # deterministic per item


def _rows(cls, good_n, bad_n, pass_good=None):
    return [{"cls": cls, "card": "low_prior", "round_type": "first", "pass": pass_good or good_n,
             "fail": 0, "n": good_n, "mean_tokens": 100},
            {"cls": cls, "card": "transform", "round_type": "first", "pass": 0, "fail": bad_n,
             "n": bad_n, "mean_tokens": 100}]


def test_pooled_backoff_below_n_min():
    views = {"strategy_stats": _rows("other", 30, 30) + _rows("mine", 3, 3)}
    cells = allocate.posterior_cells(["low_prior", "transform"], "mine", views)
    assert cells["low_prior"]["cls"] == "*" and cells["low_prior"]["n"] == 33
    assert allocate.posterior_cells(["low_prior", "transform"], "mine",
                                    {"strategy_stats": _rows("mine", 3, 3)}) is None


def test_respawn_follows_memory_and_floor(monkeypatch):
    views = {"strategy_stats": _rows("c", 40, 40)
             + [{"cls": "c", "card": "seeded", "round_type": "first", "pass": 0, "fail": 40,
                 "n": 40, "mean_tokens": 100}]}
    monkeypatch.setitem(config.PARAMS, "exploration_floor", 0.0)
    picks = [allocate.respawn("bt", "c", views, set(), [], 0, r, item_id=f"i{r}")[0].card
             for r in range(20)]
    assert set(picks) == {"low_prior"}                             # memory decides the card
    cold = {allocate.respawn("bt", "c", None, set(), [], 0, r)[0].card for r in range(6)}
    assert len(cold) > 1                                           # round-robin at cold start
    monkeypatch.setitem(config.PARAMS, "exploration_floor", 1.0)
    floor = {allocate.respawn("bt", "c", views, set(), [], 0, r, item_id=f"i{r}")[0].card
             for r in range(30)}
    assert len(floor) > 1                                          # floor spreads uniformly
    cells = allocate.posterior_cells(["low_prior", "transform"], "c", views)
    monkeypatch.setitem(config.PARAMS, "exploration_floor", 0.0)
    two = allocate.pick_cards(["low_prior", "transform"], cells, random.Random(1), 2)
    assert "low_prior" in two                                      # posterior mode gets a slot


def test_est_cost_uses_class_cell():
    views = {"strategy_stats": [
        {"cls": "a", "card": "low_prior", "round_type": "first", "n": 5, "n_calls": 5,
         "pass": 1, "fail": 4, "mean_tokens": 1000},
        {"cls": "b", "card": "low_prior", "round_type": "first", "n": 5, "n_calls": 5,
         "pass": 1, "fail": 4, "mean_tokens": 3000}]}
    s = allocate.CardSpec(card="low_prior")
    assert allocate.est_cost(s, views, "bt", cls="a") == 1000
    assert allocate.est_cost(s, views, "bt", cls="b") == 3000
    assert allocate.est_cost(s, views, "bt") == 2000                # pooled without a class
    assert allocate.est_cost(s, views, "bt", cls="a", round_type="post_reset") == 1000


def test_exhausted_pool_is_dropped_not_respawned(stubs):  # noqa: F811
    stubs.mods["allocate"].fresh_tuples = lambda *a, **k: []
    ctx = SimpleNamespace(benchmark="bt", cls="bt", replicate=0, item_id="i")
    st = think.State(used_tuples={("low_prior", "none", "", 0)})
    sig: dict = {}
    out = think._refresh(ctx, st, [tt.Spec("low_prior"), tt.Spec("seeded", seed="w")], sig)
    assert [s.card for s in out] == ["seeded"] and sig["pool_exhausted"] == ["low_prior"]


# ---------------------------------------------------------------- C3, C7, C8, C9 memory
def _lrow(**kw):
    base = dict(run_id="r1", batch="b", benchmark="bt", item_id="i", split="dev-tune",
                family="bt", cls="bt", arm="scaffold", card="seeded", operator="none",
                round_type="first", round=0, seed="", perm=0, call_id="c",
                tokens={"total_tokens": 100}, run_instance="x")
    return {**base, **kw}


def test_stats_counts_only_true_failures_and_splits_revise_children():
    rows = [_lrow(status="verified"), _lrow(status="fail"), _lrow(status="unverified"),
            _lrow(status="checked"),
            _lrow(card="revise", operator="fix", round_type="revise", round=1, parent_id="p1",
                  call_id="c1"),
            _lrow(card="revise", operator="fix", round_type="revise", round=1, parent_id="p2",
                  call_id="c2")]
    cells = {(c["card"], c["round_type"]): c for c in stats.compute(rows)}
    seeded = cells[("seeded", "first")]
    assert (seeded["pass"], seeded["fail"], seeded["n"]) == (1, 1, 2)
    rev = cells[("revise", "revise")]
    assert rev["n_calls"] == 2 and rev["mean_tokens"] == 100.0


def test_revise_ledger_rows_carry_parent_id(stubs):  # noqa: F811
    item = tt.arc_item("t_par")
    llm.set_mock(tt.make_varied_mock())
    think.think(item, m=20, replicate=0, backend="mock", batch="tc_par")
    rows = [r for r in tt.ledger_rows(tt.run_dir_of("tc_par", item).name)
            if r["round_type"] == "revise" and r.get("cand_id") is None]
    assert rows and all(r.get("parent_id") for r in rows)


def test_snapshot_built_from_dev_tune_and_refused_on_same_split(stubs):  # noqa: F811
    stubs.mods["stats"] = stats
    for _ in range(3):
        ledger.append(_lrow(batch="snap", status="verified"))
    item = tt.bt_item("t_snap")
    llm.set_mock(tt.make_mock("bt", letter="B"))
    with pytest.raises(ValueError, match="not disjoint"):
        think.think(item, m=20, replicate=0, backend="mock", batch="tc_snap",
                    flags={"snapshot": "snap"})
    assert not tt.run_dir_of("tc_snap", item).exists()           # refused before any folder
    held = dict(item, split="dev-ablate")
    think.think(held, m=20, replicate=0, backend="mock", batch="tc_snap", flags={"snapshot": "snap"})
    st = read_json(tt.run_dir_of("tc_snap", held) / "state.json")
    assert st["snapshot_hash"] and st["snapshot_splits"] == list(stats.TRAIN_SPLITS)
    assert stats.view_path("snap").exists()


# ---------------------------------------------------------------- C5 judge calibration
def test_judge_calibration_sample_logs_without_steering(stubs):  # noqa: F811
    item = tt.arc_item("t_cal")
    llm.set_mock(tt.make_mock("arc", tt.CORRECT))
    ans = think.think(item, m=20, replicate=0, backend="mock", batch="tc_cal")
    rd = tt.run_dir_of("tc_cal", item)
    js = read_jsonl(rd / "judgments.jsonl")
    assert js and all(j["calibration_only"] for j in js)
    rows = tt.ledger_rows(rd.name)
    cal = [r for r in rows if r.get("calibration_only")]
    assert cal and read_json(rd / "state.json")["calibration_tokens"] == sum(
        r["tokens"]["total_tokens"] for r in cal)
    tt.spent_matches_ledger(rd.name, ans.spent_tokens)
    assert any(r.get("p_raw") is not None for r in rows if r.get("status") == "verified")


def test_judge_calibration_off_by_default(stubs, monkeypatch):  # noqa: F811
    monkeypatch.setitem(config.FLAGS, "judge_calibration_sample", 0.0)
    item = tt.arc_item("t_cal0")
    llm.set_mock(tt.make_mock("arc", tt.CORRECT))
    think.think(item, m=20, replicate=0, backend="mock", batch="tc_cal0")
    assert not (tt.run_dir_of("tc_cal0", item) / "judgments.jsonl").exists()


# ---------------------------------------------------------------- C6 vote selection
def test_select_env_recorded(stubs, monkeypatch):  # noqa: F811
    monkeypatch.setenv("HTSA_SELECT", "vote")
    item = tt.arc_item("t_vote")
    llm.set_mock(tt.make_mock("arc", tt.CORRECT))
    ans = think.think(item, m=20, replicate=0, backend="mock", batch="tc_vote")
    st = read_json(tt.run_dir_of("tc_vote", item) / "state.json")
    assert st["select"]["HTSA_SELECT"] == "vote"
    runs = read_jsonl(Path(config.RESULTS_DIR) / "tc_vote" / "runs.jsonl")
    assert runs[-1]["select"]["HTSA_SELECT"] == "vote" and ans.status == "solved"


def _cand(cid, pred, origin="spoken"):
    return Candidate(id=cid, text="t", card="seeded", operator="none", seed="", perm=0, round=0,
                     call_id="c", program=f"def transform(g):\n    return {pred!r}\n", pred=pred,
                     origin=origin)


def test_vote_respects_clears_and_verifies_probe(stubs):  # noqa: F811
    good, low = _cand("g", [[1]]), _cand("l", [[2]])
    pc_ok, pc_bad = _cand("p1", [[2]], "probe"), _cand("p2", [[2]], "probe")
    st = think.State(all_cands=[good, low])
    st.vres = {"g": VerifyResult(id="g", status="verified", verification_type="demo_match",
                                 partial_score=1.0, details={"checklist": {"a": True}}),
               "l": VerifyResult(id="l", status="verified", verification_type="demo_match",
                                 partial_score=1.0, details={"checklist": {"a": False}})}
    seen = []

    def v_run(cand, handle, *, attempts, benchmark, agreement, run_dir):
        seen.append(cand.id)
        ok = cand.id == "p1"
        return VerifyResult(id=cand.id, status="verified" if ok else "fail",
                            verification_type="demo_match", partial_score=1.0 if ok else 0.0,
                            details={"checklist": {"a": ok}})
    stubs.mods["verify"].run = v_run
    ctx = SimpleNamespace(benchmark="arc", P=SimpleNamespace(bar={"all_items": True}, item={}),
                          V=SimpleNamespace(type="demo_match"), probe=SimpleNamespace(cands=[pc_ok, pc_bad]),
                          header={"select": {}}, run_dir=Path("."), run_id="r", batch="b",
                          item_id="i", split="dev-tune", family="arc", cls="arc", arm="scaffold",
                          snapshot_hash=None, run_instance="x")
    c, k, n = think._vote_verified(ctx, st)
    assert set(seen) == {"p1", "p2"}                               # probe cands went through verify
    # pool = g (clears) + p1 (verified probe); l fails the checklist, p2 failed verify
    assert {c.id} <= {"g", "p1"} and n == 2 and k == 1


# ---------------------------------------------------------------- C14, C15, clears
def test_live_lock_blocks_move_and_dead_lock_moves(lab_root):  # noqa: F811
    rid = "tc_lock__arc__i__scaffold__r0"
    rd = Path(config.RUNS_DIR) / rid
    rd.mkdir(parents=True)
    write_json(rd / "state.json", {})
    write_json(rd / think.LOCK_NAME, {"pid": os.getppid() or os.getpid()})
    if think._pid_alive(os.getppid()):
        with pytest.raises(RuntimeError, match="live"):
            think._make_run_dir(rid)
        assert rd.exists() and not list(rd.parent.glob(f"{rid}.old-*"))
    write_json(rd / think.LOCK_NAME, {"pid": 2 ** 30})              # no such process
    think._make_run_dir(rid, "inst")
    try:
        assert list(rd.parent.glob(f"{rid}.old-*"))
        assert read_json(rd / think.LOCK_NAME)["pid"] == os.getpid()
        with pytest.raises(RuntimeError):
            think._make_run_dir(rid)                               # live in this process
    finally:
        think._release(rid, rd)
    assert not (rd / think.LOCK_NAME).exists()


def test_impasse_counts_verified_and_clears_needs_checklist():
    st = think.State()
    st.vres = {"a": VerifyResult(id="a", status="verified", verification_type="demo_match",
                                 partial_score=1.0)}
    ctx = SimpleNamespace(B=10)
    assert "verified=1" in think._impasse(ctx, st, "round_cap")
    why: list = []
    assert not think._clears({"all_items": True}, st.vres["a"], why) and "checklist missing" in why
    assert think._clears({}, st.vres["a"])
    ok = VerifyResult(id="b", status="verified", verification_type="demo_match", partial_score=1.0,
                      details={"checklist": {"x": True}})
    assert think._clears({"all_items": True}, ok)
