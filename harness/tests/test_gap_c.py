"""Gap C: the team picks its next question (nano/pick.py, tree.add_failure_question test fields, the loop hook)."""
from __future__ import annotations

import json
import sys
from pathlib import Path

from nano import pick as PK
from nano import tree


def _tree():
    nodes = [{"id": "root", "name": "goal", "parent": None, "frame": "", "assumptions": [], "boundary": "", "directions": ["upward"]},
             {"id": "a", "name": "part a", "parent": "root", "frame": "", "assumptions": [], "boundary": "x", "directions": ["inward"]},
             {"id": "b", "name": "part b", "parent": "root", "frame": "", "assumptions": [], "boundary": "x", "directions": ["inward"]}]
    fb_gap = {"rung": 2, "reason": "the quick score is 1.17 against the baseline's 1.08 (gap +0.09, negative is better; allowed 0.0367)"}
    tree.add_failure_question(nodes, "a", "nAAA111", "bigger bins first", "too many bins", feedback=fb_gap,
                              metrics={"learn_gap": 0.09})
    tree.add_failure_question(nodes, "b", "nBBB222", "cache the fills", "build failed", feedback={"rung": 1, "reason": "build failed"})
    return nodes


def test_enterable_rule():
    nodes = _tree()
    qa = next(n for n in nodes if n["id"] == "q_naaa111")
    assert qa["enterable"] and qa["test"] == {"metric": "learn_gap", "rung": 2, "op": "<=", "what": "the quick score (rung 2)"}
    assert qa["threshold"] == 0.0367 and "learn_gap above 0.0367" in qa["fails_if"]
    qb = next(n for n in nodes if n["id"] == "q_nbbb222")
    assert qb["enterable"] and qb["test"]["metric"] == "rung_reached" and qb["threshold"] == 2
    cost = tree.add_failure_question(nodes, "a", "nC", "x", "cost", feedback={"rung": 2, "reason": "cost is 3.1x the baseline's (at most 2.0x is allowed)"})
    assert cost["test"]["metric"] == "cost_ratio" and cost["threshold"] == 2.0
    # no rung in the feedback (or no feedback): created, but never picked
    bad = tree.add_failure_question(nodes, "b", "nDDD444", "mystery", "it broke")
    assert bad["enterable"] is False and bad["test"] is None
    ids = {c["id"] for c in PK.candidates(nodes, [], [])}
    assert {"q_naaa111", "q_nbbb222"} <= ids and "q_nddd444" not in ids


def test_upward_is_a_pseudo_question_that_needs_a_person():
    ups = [{"id": "u1", "proposal": "judge by the tail", "reframing": "the mean hides the tail", "new_measure": "loss on rare tokens"},
           {"id": "u2", "proposal": "judge by the tail", "reframing": "the mean hides the tail", "new_measure": "loss on rare tokens"},
           {"id": "u3", "proposal": "no measure", "reframing": "r", "new_measure": ""}]
    c = [q for q in PK.candidates(_tree(), ups, []) if q["kind"] == "upward"]
    assert [q["id"] for q in c] == ["u1"]                     # duplicate and measure-less proposals dropped
    assert c[0]["requires_human"] and c[0]["test"]["metric"] == "loss on rare tokens" and c[0]["node"] == "root"


def test_score_formula_and_beta_prior():
    nodes = _tree()
    q = next(c for c in PK.candidates(nodes, [], []) if c["id"] == "q_naaa111")
    stats = PK.branch_stats(nodes, [], {}, [], default_cost=1000, round_no=2)
    s = PK.score(q, stats)
    assert s["p_resolve"] == 0.5 and s["gain"] == 1.0 and s["novelty"] == 1.0 and s["cost"] == 1000
    assert abs(s["score"] - 0.5) < 1e-9                       # 0.5 x 1 x 1 / (1000 / 1000)
    builds = [{"node": "a", "round": 1, "status": "checked", "tokens": 2000}] * 3 + [{"node": "a", "round": 1, "status": "fail", "tokens": 2000}]
    stats = PK.branch_stats(nodes, builds, {"a": 2, "b": 4}, [], default_cost=1000, round_no=2)
    s = PK.score(q, stats)
    assert abs(s["p_resolve"] - (1 + 3) / (2 + 4)) < 1e-4 and s["cost"] == 2000 and abs(s["gain"] - 0.5) < 1e-9
    # an open child question it would unblock raises the gain
    nodes.append({"id": "h1", "name": "helper", "parent": "q_naaa111", "kind": "question", "frame": "", "assumptions": [],
                  "boundary": "", "directions": ["inward"]})
    q2 = next(c for c in PK.candidates(nodes, [], []) if c["id"] == "q_naaa111")
    assert PK.score(q2, stats)["gain"] == 2 * s["gain"]


def test_novelty_and_learning_progress():
    q = {"id": "x", "text": "why did bigger bins first fail", "branch": "a"}
    assert PK.novelty(q, []) == 1.0
    assert PK.novelty(q, [(1, "y", "why did bigger bins first fail")]) == 0.0
    assert PK.novelty(q, [(1, "x", "why did bigger bins first fail")]) == 1.0      # its own past pick is not counted
    assert 0.0 < PK.novelty(q, [(1, "y", "bigger bins later")]) < 1.0
    assert PK.lp_bonus([0, 1, 3])[0] == 1.5 and PK.lp_bonus([2, 2, 2])[0] == PK.LP_FLAT and PK.lp_bonus([1])[0] == 1.0
    assert PK.lp_bonus([3, 2, 0])[0] == 1.5                  # getting worse also earns attention (absolute change)


def _cands():
    return [{"id": "q1", "kind": "question", "score": 0.9, "novelty": 0.2, "reason": "r1"},
            {"id": "q2", "kind": "question", "score": 0.5, "novelty": 0.5, "reason": "r2"},
            {"id": "q3", "kind": "question", "score": 0.3, "novelty": 0.4, "reason": "r3"},
            {"id": "u1", "kind": "upward", "score": 0.1, "novelty": 0.9, "reason": "r4", "requires_human": True}]


def test_pick_top3_and_exploration_slot():
    r = PK.pick(_cands(), 2)
    assert [q["id"] for q in r["top3"]] == ["q1", "q2", "q3"] and not r["explore"]
    r5 = PK.pick(_cands(), 5, explore_every=5)
    assert r5["explore"] and r5["top3"][0]["id"] == "u1" and r5["top3"][0]["slot"] == "explore"
    assert "exploration" in r5["top3"][0]["reason"]


def test_veto_and_choose():
    top = PK.pick(_cands(), 2)["top3"]
    assert PK.apply_veto(top, {})["chosen"]["id"] == "q1"
    v = PK.apply_veto(top, {"veto": ["q1"]})
    assert v["chosen"]["id"] == "q2" and v["vetoed"] == ["q1"]
    assert PK.apply_veto(top, {"choose": "q3"})["chosen"]["id"] == "q3"
    assert PK.apply_veto(top, {"veto": ["q1", "q2", "q3"]})["chosen"] is None


def test_budget_cap_and_answered():
    nodes = _tree()
    hist = [{"round": 2, "chosen": {"id": "q_naaa111"}}, {"round": 3, "chosen": {"id": "q_naaa111"}}]
    assert "q_naaa111" not in {c["id"] for c in PK.candidates(nodes, [], hist, max_rounds_focus=2)}
    assert "q_naaa111" in {c["id"] for c in PK.candidates(nodes, [], hist, max_rounds_focus=3)}
    hist = [{"round": 2, "chosen": {"id": "q_nbbb222"}, "answered": True}]
    assert "q_nbbb222" not in {c["id"] for c in PK.candidates(nodes, [], hist)}


def test_mock_run_picks_a_question_and_focuses_it(monkeypatch):
    """Two mock rounds (binpack_nobase, CPU scorer): the mock breaks one build in round 1, so round 2 has an
    enterable question; next_questions.json names it and its node received the focus contexts."""
    from harness import config
    from nano import dry_run
    from nano.checks import script
    monkeypatch.setattr(script, "PY", Path(sys.executable))
    monkeypatch.setattr(sys, "argv", ["dry_run", "--profile", "binpack_nobase", "--batch", "mock-gap-c",
                                      "--implement", "2", "--rounds", "2", "--max-sketch-calls", "8"])
    assert dry_run.main() == 0
    run = next(config.RUNS_DIR.glob("mock-gap-c__*"))
    pt = json.loads((run / "problem_tree.json").read_text(encoding="utf-8"))
    qs = [n for n in pt["nodes"] if n.get("kind") == "question" and n.get("enterable")]
    assert qs and all(n["test"] and n["threshold"] is not None and n["fails_if"] for n in qs)
    nq = json.loads((run / "next_questions.json").read_text(encoding="utf-8"))
    assert nq["round"] == 2 and nq["chosen"] and 1 <= len(nq["top3"]) <= 3
    ch = nq["chosen"]
    assert ch["path"][0] == "goal" and ch["path_ids"][-1] == ch["node"] and "reason" in ch
    ideas = [json.loads(x) for x in (run / "ideas.jsonl").read_text(encoding="utf-8").splitlines()]
    focus = [s for s in ideas if s.get("card") == "focus" and s.get("round") == 2]
    assert focus and {s["node"] for s in focus} == {ch["node"]}
    prompts = "".join(p.read_text(encoding="utf-8") for p in (run / "prompts").glob("*.txt"))
    assert "THE TEAM'S CURRENT QUESTION: " + ch["text"] in prompts
    st = json.loads((run / "state.json").read_text(encoding="utf-8"))
    assert any(d.get("step") == "pick_question" and d.get("chosen") == ch["id"] for d in st["decisions"])
    rep = json.loads((run / "report.json").read_text(encoding="utf-8"))
    assert rep["questions"][0]["chosen"] == ch["id"] and "answered" in rep["questions"][0]
    assert "## Questions the team chose" in (run / "REPORT.md").read_text(encoding="utf-8")
