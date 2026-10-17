"""Tests for the control modules: judge, probe, think/{dedup, allocate, admit, stop, stagnation,
tournament}. Mock backend only; temporary lab root; no tokens spent."""
from __future__ import annotations

import json
import os
import re
import tempfile
from pathlib import Path
from types import SimpleNamespace

if "HTSA_LAB_ROOT" not in os.environ:
    os.environ["HTSA_LAB_ROOT"] = tempfile.mkdtemp(prefix="htsa_lab_")

import pytest

from harness import config, judge as judge_mod, llm, probe as probe_mod
from harness.schemas import Candidate, VerifyResult, read_jsonl
from harness.think import admit, allocate, dedup, stagnation, stop, tournament

ARC_KEY = [[7, 7], [7, 7]]
BT_LABEL = 2


@pytest.fixture(autouse=True)
def _mock_reset():
    yield
    llm.set_mock(None)


def arc_problem():
    item = {"id": "arc_t1", "benchmark": "arc", "train": [{"input": [[1, 0]], "output": [[0, 1]]}],
            "test_input": [[2, 0]], "test_output": ARC_KEY, "family": "arc", "split": "dev-tune"}
    stripped = {k: v for k, v in item.items() if k != "test_output"}
    return SimpleNamespace(item_id="arc_t1", benchmark="arc", problem_md="GOAL: map grids.\n",
                           item=stripped), item


def bt_problem():
    item = {"id": "bt_t1", "benchmark": "bt", "question": "What can you hold without touching?",
            "choices": ["a cup", "a rock", "your breath", "none"], "label": BT_LABEL,
            "family": "bt_sp", "split": "dev-tune"}
    stripped = {k: v for k, v in item.items() if k != "label"}
    return SimpleNamespace(item_id="bt_t1", benchmark="bt", problem_md="GOAL: pick one option.\n",
                           item=stripped), item


def cand(cid, text="A", pred="A", card="seeded", seed="river", program=None, **kw):
    return Candidate(id=cid, text=text, card=card, operator="none", seed=seed, perm=0, round=1,
                     call_id="c0", program=program, pred=pred, **kw)


def run_dirs(tmp_path):
    rd = tmp_path / "run"
    (rd / "calls").mkdir(parents=True)
    return rd, rd / "calls"


# ---------------------------------------------------------------- judge
def _aliases(prompt):
    return re.findall(r'"id": "(x[a-z0-9]+)"', prompt)


def test_judge_batches_permutations_and_blindness(tmp_path):
    prob, _ = bt_problem()
    rd, log = run_dirs(tmp_path)
    seen = []

    def responder(prompt, role, meta):
        assert role == "judge"
        seen.append(prompt)
        ids = _aliases(prompt)
        return json.dumps({a: {"score": 3, "p": 0.8 if i == 0 else 0.2} for i, a in enumerate(ids)})

    llm.set_mock(responder)
    cands = [cand(f"cand_secret_{i}", text="ABCD"[i % 4], card="transform", seed="zebraseed")
             for i in range(7)]
    js, usage = judge_mod.judge(cands, prob, backend="mock", log_dir=log, replicate=0)
    assert [j.id for j in js] == [c.id for c in cands]
    assert len(seen) == 4                              # 7 -> batches of 4 and 3, two perms each
    assert all(len(_aliases(p)) <= judge_mod.BATCH_MAX for p in seen)
    for p in seen:
        assert "cand_secret" not in p and "zebraseed" not in p and "transform" not in p
        assert "your breath" in p                     # choices visible, key absent
        assert '"label"' not in p
    for j in js:
        assert j.perm_a is not None and j.perm_b is not None
        assert j.p_raw == pytest.approx((j.perm_a + j.perm_b) / 2, abs=1e-4)
        assert len(j.call_ids) == 2
    assert any(j.spread and j.spread > 0 for j in js)
    assert usage.total_tokens > 0
    assert len(list((rd / "prompts").glob("*.txt"))) == 4
    assert len(list(log.glob("*.json"))) == 4


def test_judge_pointwise_and_fallback(tmp_path):
    prob, _ = bt_problem()
    _, log = run_dirs(tmp_path)
    llm.set_mock(lambda p, r, m: "not json at all")
    js, _ = judge_mod.judge([cand("a1")], prob, backend="mock", log_dir=log, replicate=0)
    assert len(js) == 1 and js[0].p_raw == 0.5 and js[0].perm_b is None and js[0].spread is None
    assert len(js[0].call_ids) == 1
    llm.set_mock(None)                                  # default mock: {"score": 3, "p": 0.5}
    js, _ = judge_mod.judge([cand("a2")], prob, backend="mock", log_dir=log, replicate=0)
    assert js[0].rubric["parse_a"] is True
    assert judge_mod.judge([], prob, backend="mock", log_dir=log, replicate=0)[0] == []


def test_judge_parse_reply_salvage():
    out = judge_mod.parse_reply('```json\n{"xa": {"score": 9, "p": 1.7}, "xb": {"p": 0.3}\n```',
                                ["xa", "xb", "xc"])
    assert out["xa"]["p"] == 1.0 and out["xa"]["score"] == 5.0
    assert out["xb"]["p"] == 0.3 and out["xc"]["p"] == 0.5 and not out["xc"]["ok"]
    broken = 'here: "xa": {"score": 4, "p": 0.9}, "xb": {"score": 2 "p": 0.1'
    assert judge_mod.parse_reply(broken, ["xa"])["xa"]["p"] == 0.9


def test_judge_deterministic_by_replicate(tmp_path):
    prob, _ = bt_problem()
    _, log = run_dirs(tmp_path)
    prompts = {0: [], 1: []}
    for rep in (0, 0, 1):
        got = []
        llm.set_mock(lambda p, r, m: got.append(p) or "{}")
        judge_mod.judge([cand(f"c{i}") for i in range(4)], prob, backend="mock", log_dir=log,
                        replicate=rep)
        prompts.setdefault(rep, []).append(sorted(got))
    assert prompts[0][0] == prompts[0][1]


# ---------------------------------------------------------------- probe
def test_probe_bt_clusters_agreement_and_files(tmp_path):
    prob, _ = bt_problem()
    rd, log = run_dirs(tmp_path)
    replies = iter(["thinking\nANSWER: C", "1. C\n2. A", "ANSWER: B"])
    prompts = []

    def responder(prompt, role, meta):
        assert role == "probe"
        prompts.append(prompt)
        return next(replies)

    llm.set_mock(responder)
    pr = probe_mod.run_probe(prob, n=3, backend="mock", log_dir=log, replicate=0, run_dir=rd)
    assert pr.n == 3 and pr.clusters == {"opt:C": 2, "opt:B": 1}
    assert pr.usage.total_tokens > 0
    assert all(c.origin == "probe" and c.card == "probe" for c in pr.cands)
    rows = read_jsonl(rd / "cands" / "probe.jsonl")
    assert len(rows) == 3 and {r["pred"] for r in rows} == {"B", "C"}
    assert probe_mod.agreement(pr, cand("x", text="C", pred="C"), "bt") == pytest.approx(2 / 3)
    assert probe_mod.agreement(pr, cand("y", text="D", pred="D"), "bt") == 0.0
    for p in prompts:
        assert '"label"' not in p and "label" not in p
    seeds = [c.seed for c in pr.cands]
    assert len(set(seeds)) == 3


def test_probe_arc_uses_predict_and_hides_key(tmp_path, monkeypatch):
    prob, item = arc_problem()
    rd, log = run_dirs(tmp_path)
    monkeypatch.setattr(probe_mod, "_predict",
                        lambda src, grid: [[0, 2]] if "[::-1]" in src else [[2, 0]])
    prompts = []
    replies = iter(["```python\ndef transform(grid):\n    return [r[::-1] for r in grid]\n```",
                    "```python\ndef transform(grid):\n    return [r[::-1] for r in grid]\n```",
                    "no code here"])
    llm.set_mock(lambda p, r, m: prompts.append(p) or next(replies))
    pr = probe_mod.run_probe(prob, n=3, backend="mock", log_dir=log, replicate=0, run_dir=rd)
    assert pr.n == 3 and len(pr.cands) == 2
    assert pr.clusters == {"grid:[[0,2]]": 2}
    key_str = json.dumps(item["test_output"], separators=(",", ":"))
    for p in prompts + [(rd / "cands" / "probe.jsonl").read_text(encoding="utf-8")]:
        assert key_str not in p and "test_output" not in p
    c = cand("q", text="prog", pred=[[0, 2]], program="def transform(g): return g")
    assert probe_mod.agreement(pr, c, "arc") == pytest.approx(2 / 3)


def test_calibrate_identity_and_gate():
    assert probe_mod.calibrate(0.67, 0.1, {"p_raw_validated": False}) == 0.67
    assert probe_mod.calibrate(0.67, None, {"p_raw_validated": True}) == 0.67
    assert probe_mod.calibrate(0.6, 0.2, {"p_raw_validated": True}) == pytest.approx(0.4)
    assert probe_mod.agreement(probe_mod.ProbeResult({}, 0, None), cand("z"), "bt") == 0.0


# ---------------------------------------------------------------- dedup
def test_dedup_keys():
    g = cand("g", text="def transform(g): return g", pred=[[1, 2]], program="x")
    assert dedup.dedup_key(g, "arc") == "grid:[[1,2]]"
    p1 = cand("p1", text="", pred=None, program="def transform(g):\n    return g\n")
    p2 = cand("p2", text="", pred=None, program="def transform(g):\n    return g   \n\n")
    assert dedup.dedup_key(p1, "arc") == dedup.dedup_key(p2, "arc")
    assert dedup.dedup_key(p1, "arc").startswith("prog:")
    assert dedup.dedup_key(cand("b", text="B. because", pred=None), "bt") == "opt:B"
    assert dedup.dedup_key(cand("b2", text="whatever", pred="b"), "bt") == "opt:B"


def test_dedup_rate_and_drop():
    prior = [cand("o1", pred="A")]
    new = [cand("n1", pred="A"), cand("n2", pred="B"), cand("n3", pred="B"), cand("n4", pred="C")]
    assert dedup.rate(new, prior, "bt") == pytest.approx(0.5)
    assert dedup.rate([], prior, "bt") == 0.0
    kept, rows = dedup.drop(new, prior, "bt", round_no=2)
    assert [c.id for c in kept] == ["n2", "n4"]
    by_rep = {r["representative_id"]: r for r in rows}
    assert by_rep["o1"]["members"] == ["o1", "n1"] and by_rep["o1"]["dropped"] == ["n1"]
    assert by_rep["n2"]["members"] == ["n2", "n3"] and by_rep["n2"]["round"] == 2
    assert all(r["rule"] == "option" and r["cluster_id"].startswith("k") for r in rows)
    dropped = {i for r in rows for i in r["dropped"]}
    assert dropped == {"n1", "n3"}


# ---------------------------------------------------------------- allocate
def test_initial_arc_and_bt():
    arc = allocate.initial("arc", "arc", None, config.BENCHMARKS["arc"]["n0"], 0, 1)
    assert len(arc) == 5 and arc[0].card == "seeded" and arc[0].seed
    assert {s.card for s in arc[2:]} == {"low_prior", "transform", "formal"}
    assert arc[allocate.MEMORY_BLIND_INDEX].card in allocate.applicable_cards("arc")
    tr = [s for s in arc[2:] if s.card == "transform"][0]
    assert tr.operator in allocate.OPERATORS["transform"]
    bt = allocate.initial("bt", "bt_sp", None, config.BENCHMARKS["bt"]["n0"], 0, 1)
    assert len(bt) == 4 and "formal" not in {s.card for s in bt[2:]}
    assert allocate.initial("arc", "arc", None, 5, 0, 1) == arc            # deterministic
    small = allocate.initial("arc", "arc", None, 3, 0, 1)
    assert len(small) == 3 and small[0].card == "seeded"
    big = allocate.initial("bt", "bt_sp", None, 6, 0, 1)
    assert len(big) == 6 and len({allocate.spec_tuple(s) for s in big}) == 6


def test_round_robin_rotates_and_thompson_used():
    a = allocate.order_directed(["low_prior", "transform"], "c", None, 0, 1)
    b = allocate.order_directed(["low_prior", "transform"], "c", None, 1, 1)
    assert a != b
    rows = [{"cls": "c", "card": "low_prior", "round_type": "first", "pass": 30, "fail": 0,
             "mean_tokens": 100},
            {"cls": "c", "card": "transform", "round_type": "first", "pass": 0, "fail": 30,
             "mean_tokens": 100}]
    views = {"strategy_stats": rows}
    firsts = [allocate.order_directed(["transform", "low_prior"], "c", views, r, 1)[0]
              for r in range(40)]
    assert firsts.count("low_prior") >= 30                 # Thompson favours, floor explores
    thin = {"strategy_stats": [dict(r, pass_=0, n=3) for r in rows]}
    assert allocate.order_directed(["transform", "low_prior"], "c", thin, 0, 1) == \
        allocate.order_round_robin(["transform", "low_prior"], 0, 1)
    keyed = {"strategy_stats": {"c|low_prior|first": {"pass": 1, "fail": 1}}}
    assert allocate.stats_rows(keyed)[0]["card"] == "low_prior"


def test_fresh_tuples_unused_and_variants():
    first = allocate.initial("bt", "bt_sp", None, 4, 0, 1)
    used = {allocate.spec_tuple(s) for s in first}
    fresh = allocate.fresh_tuples("bt", "bt_sp", used, ["v1", "v2"], 0, 2, 6)
    assert len(fresh) == 6
    ts = [allocate.spec_tuple(s) for s in fresh]
    assert not set(ts) & used and len(set(ts)) == 6
    assert [s.variant for s in fresh[:2]] == ["v1", "v2"]
    assert len({s.card for s in fresh}) >= 3


def test_est_cost_verify_revise_reallocate():
    s = allocate.CardSpec(card="transform", operator="drop")
    cold = allocate.est_cost(s, None, "arc")
    assert cold == 3 * (config.PARAMS["max_tokens"]["program"] + allocate.INPUT_EST["arc"]
                        + config.CLI_OVERHEAD_TOKENS_EST)
    views = {"strategy_stats": [{"cls": "x", "card": "transform", "round_type": "first",
                                 "n": 10, "pass": 2, "fail": 8, "mean_tokens": 1234.2}]}
    assert allocate.est_cost(s, views, "arc") == 1235
    assert allocate.est_verify(2, 100.0) == 200
    assert allocate.est_verify(3, 0.0) == 0
    assert allocate.est_verify(1, None) > config.PARAMS["max_tokens"]["verify"]
    parent = cand("par1")
    vr = VerifyResult(id="par1", status="fail", verification_type="demo_match")
    rs = allocate.revise_specs([(parent, vr)], 0)
    assert rs[0].card == "revise" and rs[0].parent_id == "par1"
    assert rs[0].operator in allocate.OPERATORS["revise"]
    specs = allocate.initial("arc", "arc", None, 5, 0, 1) + rs
    assert allocate.reallocate(specs, 1.0) == specs[:5]
    assert len(allocate.reallocate(specs[:5], 0.1)) == 3


# ---------------------------------------------------------------- admit, stop, stagnation
def test_admit_update():
    pop = [cand("p1"), cand("p2")]
    new = [cand("n1"), cand("n2"), cand("n3")]
    conf = {"p1": 0.9, "p2": 0.1, "n1": 0.7, "n2": 0.65, "n3": 0.95}
    out = admit.update(pop, new, conf, {"p2"}, k_pop=3, theta=0.6)
    assert [c.id for c in out] == ["p2", "n3", "p1"]
    out = admit.update([], new, conf, {"n1", "n2", "n3"}, k_pop=2, theta=0.6)
    assert len(out) == 3                                    # verified are always kept


def test_stop_and_stagnation():
    assert stop.p_correct("verified", 0.67) == 0.67
    assert stop.p_correct("checked", 1.4) == 1.0
    calib = {"verified": {"x": [0.0, 1.0], "y": [0.2, 0.8]}}
    assert stop.p_correct("verified", 0.5, calib) == pytest.approx(0.5)
    assert stop.p_correct("verified", 0.0, calib) == pytest.approx(0.2)
    assert stop.p_correct("unverified", 0.3, calib) == 0.3
    assert stop.partial_gain(0.5, 0.75) == 0.25 and stop.partial_gain(0.8, 0.5) == 0.0
    assert stop.partial_gain(None, 0.4) == 0.4
    assert stagnation.should_reset(5, 0.9, R_max=2, R_stale=2, d_max=0.5) is False
    assert stagnation.should_reset(2, 0.0, R_max=3, R_stale=2, d_max=0.5) is True
    assert stagnation.should_reset(0, 0.6, R_max=3, R_stale=2, d_max=0.5) is True
    assert stagnation.should_reset(1, 0.5, R_max=3, R_stale=2, d_max=0.5) is False


# ---------------------------------------------------------------- tournament
def _q(cid, status, score, surprise=False):
    return (cand(cid), VerifyResult(id=cid, status=status, verification_type="demo_match",
                                    partial_score=score, surprise=surprise))


def test_pick_parents_surprises_first_then_scores():
    queue = [_q("a", "fail", 0.9), _q("b", "fail", 0.1), _q("s", "fail", 0.0), _q("c", "fail", 0.5)]
    conf = {"a": 0.2, "b": 0.3, "s": 0.95, "c": 0.1}
    got = tournament.pick_parents(queue, conf, hi=0.8, n=2, replicate=0)
    assert got[0][0].id == "s" and len(got) == 2
    assert got[1][0].id != "s"
    assert tournament.pick_parents(queue, conf, 0.8, 2, 0) == got        # deterministic
    wins = {"a": 0, "b": 0, "c": 0}
    for rep in range(30):
        top = tournament.pick_parents(queue[:2] + queue[3:], conf, 0.8, 1, rep)
        wins[top[0][0].id] += 1
    assert wins["b"] == 0 and wins["a"] > wins["c"]
    assert tournament.pick_parents([], conf, 0.8, 2, 0) == []
    assert len(tournament.pick_parents(queue, conf, 0.8, 10, 0)) == 4


# ---------------------------------------------------------------- package shim
def test_think_package_does_not_load_driver_for_submodules():
    import sys
    import harness.think as pkg
    assert pkg.dedup is dedup
    assert "harness._think_driver" not in sys.modules or callable(getattr(pkg, "think", None))
