"""Team gap B: one anchored reply round between the critic (pre-mortem) and the idea's author.

research_notes/team/team_gaps/01_dialogue.md: the author may only concede (and change the idea), rebut with a quoted fact,
or propose a measurement; the critic marks each objection resolved, revised or standing; at most two exchanges, stop
early when nothing changes; the critic is a checklist, never a gate. `--no-dialogue` is the control arm."""
from __future__ import annotations

import json
import sys

from harness import config, llm
from nano import deepen

OBJS = [
    {"text": "adds a matmul per layer", "severity": "high", "cls": "hidden_cost", "link": "",
     "if_true": {"metric": "step_ratio", "op": "above", "threshold": 1.2}},
    {"text": "within seed noise", "severity": "medium", "cls": "below_noise", "link": "",
     "if_true": {"metric": "learn_z", "op": "above", "threshold": -0.5}},
    {"text": "only helps early", "severity": "low", "cls": "early_only", "link": "",
     "if_true": {"metric": "trend", "op": "above", "threshold": 0.001}},
    {"text": "the exam cannot see it", "severity": "low", "cls": "metric_blind", "link": "", "if_true": None},
]


def test_formats_render_and_name_the_moves():
    for key in ("REPLY <i>: concede | rebut | measure", "CHANGE:", "FACT:", "TEST:", "REVISED IDEA:", "[script|measured|web|belief]"):
        assert key in deepen.REPLY_FORMAT
    assert "UPDATE <i>: resolved | revised | standing | <one reason>" in deepen.CRITIC_UPDATE_FORMAT
    assert "{v:" not in deepen.REPLY_FORMAT
    p = deepen.reply_prompt("THE BRIEF", "MECHANISM CHAIN: L1", OBJS, [2, 4])
    assert "THE BRIEF" in p and "MECHANISM CHAIN" in p and "OBJECTION 2: within seed noise" in p and "OBJECTION 4:" in p
    assert "OBJECTION 1:" not in p and "```" not in p          # sees the idea, its chain and the objections, nothing else
    assert "—" not in deepen.REPLY_FORMAT + deepen.CRITIC_UPDATE_FORMAT + p


def test_parse_replies():
    txt = ("REPLY 1: concede\nCHANGE: only the last two layers\n"
           "REPLY 2: rebut\nFACT: \"spread is 0.004 at 45 steps\" [measured]\n"
           "REPLY 3: measure\nTEST: learn_z above 0.5 at rung 3\n"
           "REPLY 4: Rebut\nFACT: it probably works (belief)\n"
           "REPLY 5: rebut\n"
           "REPLY 6: shrug\n"
           "REVISED IDEA: the change on the last two layers only.")
    pr = deepen.parse_replies(txt)
    r = pr["replies"]
    assert set(r) == {1, 2, 3, 4, 5}
    assert r[1]["kind"] == "concede" and r[1]["change"] == "only the last two layers"
    assert r[2]["kind"] == "rebut" and r[2]["source"] == "measured" and r[2]["fact"] == "\"spread is 0.004 at 45 steps\""
    assert r[3]["test"] == {"metric": "learn_z", "op": "above", "threshold": 0.5, "rung": "rung 3"}
    assert r[4]["source"] == "belief" and r[5]["fact"] == ""
    assert pr["revised"] == "the change on the last two layers only."
    assert deepen.parse_replies("TEST: x")["replies"] == {}
    assert deepen.parse_replies("REPLY 1: measure\nTEST: step_ratio < 1.5")["replies"][1]["test"]["op"] == "below"


def test_parse_updates_and_rules():
    u = deepen.parse_updates("UPDATE 1: revised | changed\nUPDATE 2: Resolved | the number settles it\nUPDATE 3: standing\nUPDATE 4: maybe | x")
    assert u[1]["verdict"] == "revised" and u[2] == {"verdict": "resolved", "reason": "the number settles it"} and u[3]["verdict"] == "standing"
    assert 4 not in u
    R = deepen.apply_rules
    ok = {"kind": "rebut", "fact": "x", "source": "script"}
    assert R(ok, {"verdict": "resolved"}) == "resolved"
    assert R(ok, {"verdict": "standing"}) == "standing"
    assert R({"kind": "rebut", "fact": "", "source": ""}, {"verdict": "resolved"}) == "standing"     # no FACT line
    assert R({"kind": "rebut", "fact": "x", "source": "belief"}, {"verdict": "resolved"}) == "standing"
    assert R({"kind": "measure", "test": {}}, {"verdict": "resolved"}) == "standing"
    assert R({"kind": "concede"}, {"verdict": "standing"}) == "revised"
    assert R(None, {"verdict": "resolved"}) == "standing"


def _fake(replies_by_exchange, updates_by_exchange=None):
    calls = {"author": [], "critic": 0}

    def ask_author(indices):
        calls["author"].append(list(indices))
        return replies_by_exchange[min(len(calls["author"]), len(replies_by_exchange)) - 1]

    def ask_critic(replies):
        calls["critic"] += 1
        if updates_by_exchange:
            return updates_by_exchange[min(calls["critic"], len(updates_by_exchange)) - 1]
        return "\n".join(f"UPDATE {i}: resolved | ok" for i in replies)
    return ask_author, ask_critic, calls


def test_cap_two_exchanges_and_second_only_for_untested_standing():
    first = ("REPLY 1: concede\nCHANGE: smaller\nREPLY 2: rebut\nFACT: \"0.004\" [measured]\n"
             "REPLY 3: measure\nTEST: learn_z above 0.5 at rung 3\nREPLY 4: rebut\nFACT: surely [belief]\nREVISED IDEA: smaller")
    a, c, calls = _fake([first, "REPLY 4: rebut\nFACT: still a hunch [belief]", "REPLY 4: rebut\nFACT: x [belief]"])
    out = deepen.run_dialogue(OBJS, a, c, max_exchanges=5)        # asked for 5, capped at 2
    assert out["exchanges"] == 2 and len(calls["author"]) == 2
    assert calls["author"][1] == [4]                              # only the standing objection with no test at all
    v = [o["dialogue"]["verdict"] for o in out["objections"]]
    assert v == ["revised", "resolved", "standing", "standing"]
    assert out["revised"] == "smaller" and out["stop"] == "nothing changed"
    assert [r["exchange"] for r in out["rows"]] == [1, 1, 1, 1, 2]
    a, c, calls = _fake([first])
    out = deepen.run_dialogue(OBJS, a, c, max_exchanges=1)       # a lower cap: one exchange, objection 4 left open
    assert out["exchanges"] == 1 and out["stop"] == "cap" and len(calls["author"]) == 1


def test_measure_attaches_test_and_ends_round():
    first = "REPLY 1: concede\nCHANGE: a\nREPLY 2: rebut\nFACT: f [web]\nREPLY 3: measure\nTEST: learn_z above 0.5\nREPLY 4: rebut\nFACT: b [belief]"
    a, c, calls = _fake([first, "REPLY 4: measure\nTEST: fidelity below 1 at rung 4"])
    out = deepen.run_dialogue(OBJS, a, c)
    o4 = out["objections"][3]
    assert o4["if_true"] == {"metric": "fidelity", "op": "below", "threshold": 1.0} and o4["dialogue"]["test"] == "fidelity below 1 at rung 4"
    assert out["objections"][2]["if_true"] == OBJS[2]["if_true"]       # an existing if_true is kept, not replaced
    assert out["stop"] == "done" and out["exchanges"] == 2


def test_early_stop_when_nothing_changes():
    a, c, calls = _fake(["REPLY 1: rebut\nFACT: hunch [belief]\nREPLY 2: rebut\nREPLY 3: rebut\nFACT: x [belief]\nREPLY 4: rebut"],
                        ["UPDATE 1: resolved\nUPDATE 2: resolved\nUPDATE 3: resolved\nUPDATE 4: resolved"])
    out = deepen.run_dialogue(OBJS, a, c)
    assert out["exchanges"] == 1 and out["stop"] == "nothing changed" and len(calls["author"]) == 1
    assert all(o["dialogue"]["verdict"] == "standing" for o in out["objections"])


def test_no_gate_nothing_dropped():
    a, c, _ = _fake(["REPLY 1: rebut\nFACT: \"the code shows no matmul\" [script]\nREPLY 2: rebut\nFACT: y [measured]\n"
                     "REPLY 3: rebut\nFACT: z [web]\nREPLY 4: rebut\nFACT: w [script]"])
    out = deepen.run_dialogue(OBJS, a, c)
    assert len(out["objections"]) == len(OBJS)                   # all resolved, none removed
    for before, after in zip(OBJS, out["objections"]):
        assert after["text"] == before["text"] and after["if_true"] == before["if_true"]   # the ladder still measures them
    assert all(o["dialogue"]["verdict"] == "resolved" for o in out["objections"])
    # a budget stop also drops nothing
    out = deepen.run_dialogue(OBJS, lambda idx: None, lambda r: None)
    assert out["stop"] == "budget" and out["exchanges"] == 0 and len(out["objections"]) == 4
    assert all(o["dialogue"]["verdict"] == "standing" for o in out["objections"])
    # the resolved objection still reaches the builder, with the author's fact
    txt = deepen.objections_text(out["objections"])
    assert all(o["text"] in txt for o in OBJS)


def test_summary_counts_and_calibration():
    rows = [{"idea": "a", "objection": 1, "reply": "concede", "verdict": "revised", "exchange": 1},
            {"idea": "a", "objection": 2, "reply": "rebut", "verdict": "resolved", "exchange": 1},
            {"idea": "a", "objection": 3, "reply": "rebut", "verdict": "standing", "exchange": 1},
            {"idea": "a", "objection": 3, "reply": "measure", "verdict": "standing", "exchange": 2}]
    measured = [{"text": "t2", "status": "confirmed", "dialogue": {"idea": "a", "verdict": "resolved"}},
                {"text": "t2", "status": "pending", "dialogue": {"idea": "a", "verdict": "resolved"}},
                {"text": "t4", "status": "refuted", "dialogue": {"idea": "b", "verdict": "resolved"}},
                {"text": "t1", "status": "pending", "dialogue": {"idea": "a", "verdict": "revised"}},
                {"text": "old", "status": "confirmed"}]
    s = deepen.dialogue_summary(rows, measured)
    assert s["objections"] == 3 and s["exchanges"] == 2 and s["ideas"] == 1
    assert s["by_reply"] == {"concede": 1, "rebut": 1, "measure": 1, "none": 0}
    assert s["by_verdict"] == {"resolved": 1, "revised": 1, "standing": 1}
    assert s["resolved_later_confirmed"] == 1 and s["resolved_later_refuted"] == 1 and s["resolved_wrong_share"] == 0.5
    assert s["after_ladder"]["revised"]["pending"] == 1


def _mock_run(monkeypatch, batch, *flags):
    from nano import dry_run
    from nano.checks import script
    monkeypatch.setattr(script, "PY", config.VENV_PYTHON, raising=False)
    monkeypatch.setattr(sys, "argv", ["dry_run", "--profile", "binpack_nobase", "--batch", batch, "--max-sketch-calls", "6",
                                      "--implement", "1", "--rounds", "1", *flags])
    try:
        assert dry_run.main() == 0
    finally:
        llm.set_mock(None)
    runs = [p for p in config.RUNS_DIR.iterdir() if p.name.startswith(batch + "__")]
    assert len(runs) == 1
    return runs[0]


def test_mock_run_records_dialogue(monkeypatch):
    run = _mock_run(monkeypatch, "mock-gap-b")
    rows = [json.loads(x) for x in (run / "dialogue.jsonl").read_text(encoding="utf-8").splitlines() if x.strip()]
    assert rows
    for r in rows:
        assert {"idea", "objection", "cls", "reply", "fact", "test", "verdict", "round", "exchange"} <= set(r)
    first = [r for r in rows if r["exchange"] == 1]
    kinds = {r["reply"] for r in first}
    assert kinds == {"concede", "rebut", "measure"}
    assert any(r["reply"] == "rebut" and r["source"] == "measured" and r["verdict"] == "resolved" for r in first)
    assert any(r["reply"] == "rebut" and r["source"] == "belief" and r["verdict"] == "standing" for r in first)
    assert all(r["verdict"] == "revised" and r["change"] and r["revised_idea"] for r in rows if r["reply"] == "concede")
    assert all(r["exchange"] <= 2 for r in rows)
    second = [r for r in rows if r["exchange"] == 2]
    assert second and all(r["reply"] == "measure" and r["test"] for r in second)
    rep = json.loads((run / "report.json").read_text(encoding="utf-8"))
    d = rep["dialogue"]
    n_ideas = len({r["idea"] for r in rows})
    assert d["ideas"] == n_ideas and d["objections"] == 4 * n_ideas
    assert d["by_reply"]["concede"] == n_ideas and d["by_reply"]["rebut"] == n_ideas and d["by_reply"]["measure"] == 2 * n_ideas
    assert d["by_verdict"] == {"resolved": n_ideas, "revised": n_ideas, "standing": 2 * n_ideas}
    assert "after_ladder" in d and "resolved_later_confirmed" in d
    dj = json.loads((run / "deepen.json").read_text(encoding="utf-8"))
    roots = [n for n in dj["nodes"] if n.get("objections")]
    assert roots and all(len(n["objections"]) == 4 and n.get("revised_idea") for n in roots)   # nothing dropped
    assert all(n["objections"][3]["if_true"] for n in roots)       # the measure reply attached a test


def test_no_dialogue_writes_none(monkeypatch):
    run = _mock_run(monkeypatch, "mock-gap-b-off", "--no-dialogue", "--stop-after", "deepened")
    assert not (run / "dialogue.jsonl").exists()
    rep = json.loads((run / "report.json").read_text(encoding="utf-8"))
    assert rep["dialogue"] == "off"
    dj = json.loads((run / "deepen.json").read_text(encoding="utf-8"))
    assert any(n.get("objections") for n in dj["nodes"])
    assert not any(o.get("dialogue") for n in dj["nodes"] for o in (n.get("objections") or []))
