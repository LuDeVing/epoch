"""Bug pass 2026-10-17 (night), the module agent: parsers against malformed replies, objection resolution, research
cache files, the fidelity direction words, the dry-run mock state and the bin-packing arms report."""
from __future__ import annotations

import json
import threading

import pytest

from nano import deepen, ideate, memory, pick, research
from nano import profile as PF


# ---------------------------------------------------------------- parsers: an empty field must not swallow the next line
def test_parse_updates_line_without_reason_keeps_the_next_update():
    out = deepen.parse_updates("UPDATE 1: resolved\nUPDATE 2: revised\r\nUPDATE 3: standing | a test is attached")
    assert set(out) == {1, 2, 3}
    assert out[1] == {"verdict": "resolved", "reason": ""}
    assert out[2]["verdict"] == "revised" and out[2]["reason"] == ""


def test_parse_replies_empty_fact_does_not_take_the_next_line():
    pr = deepen.parse_replies("REPLY 1: rebut\nFACT:\nREVISED IDEA: something else\n")
    r = pr["replies"][1]
    assert r["fact"] == ""
    assert deepen.apply_rules(r, {"verdict": "resolved"}) == "standing"
    pr = deepen.parse_replies("REPLY 1: concede\nCHANGE:\nTEST: learn_z above 0.5\n")
    assert pr["replies"][1]["change"] == ""


def test_parse_chain_empty_link_keeps_the_next_link():
    p = deepen.parse("CHAIN:\nL1:\nL2: a -> b | quantity: loss\nWEAKEST: L2\nQUESTIONS:\n")
    assert [l["id"] for l in p["chain"]] == ["L2"]     # the empty link is dropped, the next one kept whole
    assert p["chain"][0]["text"] == "a -> b"


def test_parse_premortem_empty_verdict_and_two_digit_cite():
    p = deepen.parse_premortem("OBJECTIONS:\n- it is slow | cite: Q12\nVERDICT:\nnext line is not the verdict\n")
    assert p["verdict"] == ""
    assert p["objections"][0]["cite"] == "Q12"


def test_parse_sketches_empty_removes_is_dropped_for_outward():
    text = "IDEA: x\nMECHANISM: y\nREMOVES:\nKIND: leap\n\nIDEA: z\nMECHANISM: w\nSOURCE:\nREMOVES: every item alike"
    out = ideate.parse_sketches(text, card="c", operator="outward", seed="", call_id="", idgen=lambda: "s1")
    assert [s["idea"] for s in out] == ["z"]
    assert out[0]["source"] == "own"                    # an empty SOURCE is not the next field's line


def test_parse_sketches_multiline_value_still_read():
    text = "IDEA: x\nMECHANISM:\n  two lines\n  of mechanism\nTEST: quick"
    out = ideate.parse_sketches(text, card="c", operator="inward", seed="", call_id="", idgen=lambda: "s1")
    assert out[0]["mechanism"] == "two lines of mechanism"


def test_parse_cluster_json_never_raises():
    assert ideate.parse_cluster_json(None, {"a"}) is None
    out = ideate.parse_cluster_json('[{"name": "n", "members": [["a"], {"b": 1}, "a"]}]', {"a"})
    assert out == [{"name": "n", "members": ["a"]}]


def test_parse_fetch_empty_answer_is_not_found():
    r = research.parse_fetch("ANSWER:\nSOURCE: https://example.org/x\nCONFIDENCE: high", "q")
    assert r["answer"] is None


@pytest.mark.parametrize("payload", [
    {"known": None, "failed": 5, "open": "x", "queries": None},
    {"known": [{"name": "a", "url": "https://x.org"}], "queries": 5},
    {"known": [{"name": "a", "url": "https://x.org"}], "queries": "one query"},
])
def test_parse_brief_malformed_sections_never_raise(payload):
    out = research.parse_brief(json.dumps(payload), "n")
    if out is not None:
        assert isinstance(out["queries"], list) and all(isinstance(q, str) for q in out["queries"])


def test_parse_analogies_malformed_queries_never_raise():
    out = research.parse_analogies(json.dumps({"analogues": [{"field": "f", "url": "https://x.org"}], "queries": 3}), "n")
    assert out["queries"] == []


# ---------------------------------------------------------------- objection resolution against ladder metrics
def test_resolve_objections_non_numeric_metric_is_pending():
    objs = [{"text": "a", "if_true": {"metric": "objections", "op": "above", "threshold": 0.5}},
            {"text": "b", "if_true": {"metric": "long_z", "op": "above", "threshold": 0.5}},
            {"text": "c", "if_true": {"metric": "trend", "op": "below", "threshold": 0.0}},
            {"text": "d", "if_true": {"metric": "learn_z"}}]
    out = deepen.resolve_objections(objs, {"objections": [{"x": 1}], "long_z": "n/a", "trend": float("nan")})
    assert [o["status"] for o in out] == ["pending", "pending", "pending", "untestable"]


def test_resolve_objections_absent_metric_is_pending():
    out = deepen.resolve_objections([{"text": "a", "if_true": {"metric": "cost_ratio", "op": "above", "threshold": 1.2}}], {})
    assert out[0]["status"] == "pending"


# ---------------------------------------------------------------- fidelity direction words
def test_fidelity_update_is_not_up():
    from nano import diagnose
    PF.set_current("llm")
    lay = [{"layer": 0, "grad_attn": 1.0, "act_rms": 1.0, "attn_entropy": 0.5}]
    base = {"probes": [{"layers": lay, "update_spread": {"max": 1.0}}]}
    wider = {"probes": [{"layers": lay, "update_spread": {"max": 2.0}}]}
    r = diagnose.fidelity("narrower update-norm spread", wider, base)
    assert r["ok"] is not True                          # "up" inside "update" is no direction
    narrower = {"probes": [{"layers": lay, "update_spread": {"max": 0.5}}]}
    assert diagnose.fidelity("update-norm spread down", narrower, base)["ok"] is True
    assert diagnose.fidelity("raise the update-norm spread", wider, base)["ok"] is True


# ---------------------------------------------------------------- research cache files
def test_merge_facts_concurrent_appends_no_duplicates(tmp_path, monkeypatch):
    import time as _t
    real = research.read_facts

    def slow(*a, **kw):                                 # widen the read-then-append window
        rows = real(*a, **kw)
        _t.sleep(0.05)
        return rows
    monkeypatch.setattr(research, "read_facts", slow)
    research.save_cache(tmp_path, {"node": "n", "known": []}, "k1")
    facts = [f"fact {i} https://example.org/{i}" for i in range(20)]
    ths = [threading.Thread(target=research.merge_facts, args=(tmp_path, "k1", facts, "r")) for _ in range(6)]
    for t in ths:
        t.start()
    for t in ths:
        t.join()
    rows = research.read_facts(tmp_path, "k1")
    assert len(rows) == 20


def test_cache_key_differs_across_profiles():
    node = {"id": "choice", "frame": "f", "assumptions": ["a"]}
    keys = {research.cache_key(node, p) for p in ("llm", "binpack", "binpack_nobase", "review_process")}
    assert len(keys) == 4


# ---------------------------------------------------------------- pick and memory edge cases (locked, no fix needed)
def test_pick_edges():
    assert pick.pick([], 1)["top3"] == []
    q = {"id": "q1", "kind": "question", "text": "why slow", "branch": "q1", "parent": None, "open_children": 0}
    s = pick.score(q, {"cost": {"": 0}, "default_cost": 0})
    assert s["score"] > 0 and s["novelty"] == 1.0


def test_memory_cites_ids_inside_longer_tokens(tmp_path):
    ok, _ = memory.Memory.cites("see xn0123456789a and n0123456789_b", {"cand_ids": {"n0123456789"}})
    assert ok is False
    ok, _ = memory.Memory.cites("see n0123456789.", {"cand_ids": {"n0123456789"}})
    assert ok is True


def test_memory_read_cap_is_deterministic(tmp_path):
    m = memory.Memory(tmp_path, "p", max_tokens=40)
    data = m.load("x")
    for i in range(10):
        data["sections"]["FACTS"].append({"id": f"m{i:06d}", "date": "2026-10-17", "run": "r", "source": "measured",
                                          "text": f"fact number {i} with some words", "used": i % 3})
    m.save("x", data)
    assert m.read("x") == m.read("x")


# ---------------------------------------------------------------- profiles
def test_profiles_load_with_modes():
    modes = {n: PF.load(n).mode for n in ("llm", "binpack", "binpack_nobase", "review_process")}
    assert modes == {"llm": "baseline", "binpack": "baseline", "binpack_nobase": "check_only", "review_process": "no_check"}


def test_profile_missing_key_message():
    with pytest.raises(PF.ProfileError, match="lacks required keys: checker"):
        PF._validate("x", {k: v for k, v in PF.load("binpack").as_dict().items() if k != "checker"})


# ---------------------------------------------------------------- dry run mock state and the arms report
def test_dry_run_mock_need_resets_between_runs(monkeypatch):
    from nano import dry_run
    dry_run._need_sent.append(True)
    monkeypatch.setattr(dry_run.L, "main", lambda: 0)
    monkeypatch.setattr(dry_run.sys, "argv", ["dry_run"])
    dry_run.main()
    assert dry_run._need_sent == []


def test_binpack_arms_report_on_empty_folder(tmp_path):
    from nano.experiments import binpack_arms
    with pytest.raises(SystemExit) as e:
        binpack_arms.main(["report", "--out", str(tmp_path / "empty")])
    assert "arms.json" in str(e.value)


def test_run_dialogue_critic_out_of_budget_stops():
    objs = [{"text": "a", "if_true": None}, {"text": "b", "if_true": None}]
    calls = []

    def author(idx):
        calls.append(idx)
        return "\n".join(f"REPLY {i}: rebut\nFACT: seed spread is 0.004 [belief]" for i in idx)
    out = deepen.run_dialogue(objs, author, lambda replies: None)
    assert out["stop"] == "budget" and len(calls) == 1
    assert [o["dialogue"]["verdict"] for o in out["objections"]] == ["standing", "standing"]
