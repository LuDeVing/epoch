"""Fix pass 2026-10-17, section I (ideation half) plus E5 and E16. Unit level, mock backend, no training.

I1 refines "new" is no shared merge target; I2 sub-parts follow a renamed parent, no duplicate ids; I3 a re-plan
keeps failure questions and sub-parts (lower priority, never dropped); I6 outward sketches name the removed
assumption; I10 planner, repair and re-plan calls go through _afford; I11 parse_planner ids; I12 split_select
shortfall refill; I14 disputed facts marked in the node prompt and shown to the re-plan; I15 contexts counted
after refusals and parse failures; E5 analogy addendum asks for near and far; E16 no "be creative" wording."""
from __future__ import annotations

import json
from types import SimpleNamespace

from harness.schemas import Candidate, Usage


def _llm():
    from nano import profile as PF
    PF.set_current(PF.load("llm"))


def _loop():
    from nano.loop import NanoLoop
    lp = NanoLoop("fixideation", 1, "mock", 100000, 3, 0.0, None)
    (lp.run_dir / "problem.md").write_text("make the score lower", encoding="utf-8")
    lp.plan_with_model = False
    lp.plan_tree(1)
    return lp


def _reply(nodes: list[dict]) -> str:
    return json.dumps([{"frame": "f", "assumptions": ["a"], "boundary": "b", **n} for n in nodes])


def _patch_call(monkeypatch, lp, text, calls=None):
    def call(*a, **k):
        if calls is not None:
            calls.append(a[2] if len(a) > 2 else k)
        return SimpleNamespace(text=text, call_id=f"c{len(calls or [])}", usage=Usage(1, 1, 0, 0))
    monkeypatch.setattr(lp, "_call", call)
    monkeypatch.setattr(lp, "_ledger", lambda *a, **k: None)


def _built(lp, node, cid="cb1"):
    lp.cands.append(Candidate(id=cid, text="x", card="implement", operator="x", seed="", perm=0, round=1, call_id="c0",
                              extra={"node": node, "direction": "inward"}))


# ---------------------------------------------------------------- I11 parse_planner ids
def test_parse_planner_unique_ids_and_reserved_rejected():
    _llm()
    from nano import tree
    arr = [{"id": "depth_block_wiring", "name": "a"}, {"id": "depth_block_wiring_two", "name": "b"},
           {"id": "depth_block_wiring", "name": "c"}, {"id": "root", "name": "second root"},
           {"id": "recipe", "name": "phantom recipe"}, {"id": "offtree", "name": "phantom off map"},
           {"id": "plain", "name": "d"}, {"id": "kid", "name": "e", "parent": "depth_block_wiring_two"}]
    nodes = tree.parse_planner(_reply(arr))
    ids = [n["id"] for n in nodes]
    assert len(ids) == len(set(ids)), ids
    assert ids.count("root") == 1 and ids.count("recipe") <= 1 and "offtree" not in ids
    assert all(len(i) <= tree.ID_LEN for i in ids)
    assert not any(n["name"] in ("second root", "phantom recipe", "phantom off map") for n in nodes)
    b = next(n for n in nodes if n["name"] == "b")
    assert next(n for n in nodes if n["name"] == "e")["parent"] == b["id"]   # the parent follows the suffixed id


# ---------------------------------------------------------------- I1, I2, I3 re-plan carry
def test_refines_new_is_not_a_shared_target(monkeypatch):
    lp = _loop()
    lp.tree.append({"id": "sched", "name": "schedule", "parent": "root", "refines": "new", "frame": "old frame",
                    "assumptions": ["s"], "boundary": "b", "directions": ["inward", "outward"]})
    _built(lp, "sched")
    _patch_call(monkeypatch, lp, _reply([{"id": "warm", "name": "Warmup", "refines": "new"},
                                         {"id": "sched", "name": "schedule", "refines": "new"},
                                         {"id": "c", "name": "C", "refines": "new"}, {"id": "d", "name": "D", "refines": "new"}]))
    lp.replan_tree(2)
    ids = [n["id"] for n in lp.tree]
    assert len(ids) == len(set(ids)) and ids.count("sched") == 1, ids
    assert next(n for n in lp.tree if n["name"] == "Warmup")["id"] == "warm"     # not merged into the old sched


def test_refines_a_real_default_part_merges(monkeypatch):
    lp = _loop()
    _built(lp, "opt")
    _patch_call(monkeypatch, lp, _reply([{"id": "o2", "name": "Optimizer, reworded", "refines": "opt"},
                                         {"id": "o2_sub", "name": "lr", "refines": "new", "parent": "o2"},
                                         {"id": "c", "name": "C", "refines": "new"}, {"id": "d", "name": "D", "refines": "new"}]))
    lp.replan_tree(2)
    by = {n["id"]: n for n in lp.tree}
    assert "o2" not in by and "opt" in by and by["o2_sub"]["parent"] == "opt"


def test_renamed_parent_takes_its_sub_parts_and_ids_stay_unique(monkeypatch):
    lp = _loop()                                         # the planner reuses an old name under a new id (I2)
    _patch_call(monkeypatch, lp, _reply([{"id": "mixing", "name": "sequence mixing (attention)", "refines": "mix"},
                                         {"id": "keys", "name": "keys", "refines": "new", "parent": "mixing"},
                                         {"id": "other", "name": "sequence mixing (attention)", "refines": "new"},
                                         {"id": "c", "name": "C", "refines": "new"}, {"id": "d", "name": "D", "refines": "new"}]))
    lp.replan_tree(2)
    from nano import tree
    ids = [n["id"] for n in lp.tree]
    assert len(ids) == len(set(ids)), ids
    keys = next(n for n in lp.tree if n["id"] == "keys")
    assert keys["parent"] == "mix" and tree.depth(lp.tree, "keys") == 2


def test_replan_keeps_failure_questions_and_sub_parts_at_low_priority(monkeypatch):
    from nano import tree
    lp = _loop()
    lp.tree.append({"id": "kv", "name": "key value cache", "parent": "mix", "frame": "f", "assumptions": ["a"],
                    "boundary": "b", "directions": ["inward", "outward"]})          # an un-built sub-part
    q = tree.add_failure_question(lp.tree, "ffn", "cbad", "wide ffn", "the change reaches outside the boundary")
    _patch_call(monkeypatch, lp, _reply([{"id": f"p{i}", "name": f"P{i}", "refines": "new"} for i in range(5)]))
    lp.replan_tree(2)
    by = {n["id"]: n for n in lp.tree}
    assert q["id"] in by and "kv" in by
    assert by[q["id"]]["parent"] == "ffn" and by["kv"]["parent"] == "mix"           # their parents came along
    assert by["ffn"]["priority"] == "low" and by["mix"]["priority"] == "low"
    carry = [d for d in lp.decisions if d["step"] == "replan_carry"][-1]
    assert q["id"] not in carry["dropped"] and "kv" not in carry["dropped"]
    dealt = tree.deal_contexts(lp.tree, 3)
    assert dealt[("p0", "inward")] == 3                                             # drawn parts: the full share
    assert dealt[("mix", "inward")] + dealt[("kv", "inward")] == 1                  # kept, lower priority


# ---------------------------------------------------------------- I10 planner, repair and re-plan through _afford
def test_planner_and_replan_calls_go_through_afford(monkeypatch):
    lp = _loop()
    calls, asked = [], []
    _patch_call(monkeypatch, lp, _reply([{"id": f"p{i}", "name": f"P{i}"} for i in range(5)]), calls)
    monkeypatch.setattr(lp, "_afford", lambda stage, est, note="": asked.append((stage, note)) or False)
    before = [dict(n) for n in lp.tree]
    lp.replan_tree(2)
    assert not calls and asked == [("research", "replan")]
    assert [n["id"] for n in lp.tree] == [n["id"] for n in before]
    assert any(d.get("step") == "replan" and "not affordable" in d.get("result", "") for d in lp.decisions)
    lp.tree, lp.plan_with_model = None, True
    lp.plan_tree(1)
    assert not calls and ("research", "planner") in asked and lp.tree        # refused: the default map
    lp.tree, lp.only_nodes = None, {"ffn"}
    monkeypatch.setattr(lp, "_afford", lambda stage, est, note="": asked.append((stage, note)) or note == "planner")
    lp.plan_tree(1)
    assert len(calls) == 1 and ("research", "planner repair") in asked       # the repair was refused, not called


# ---------------------------------------------------------------- I12 split_select shortfall
def test_split_select_refills_when_no_outward_cluster():
    from nano import tree
    by_node = {"a": [{"cluster_id": f"a{i}", "direction": "inward", "node": "a", "score": float(i)} for i in range(5)],
               "b": [{"cluster_id": f"b{i}", "direction": "inward", "node": "b", "score": float(i) / 10} for i in range(3)]}
    log: list = []
    sel = tree.split_select(by_node, 4, 0.5, set(), [], lambda c, k, exclude, sketches: sorted(c, key=lambda x: -x["score"]),
                            0.0, log=log)
    assert len(sel) == 4 and len({c["cluster_id"] for c in sel}) == 4
    assert log and log[0]["step"] == "split_shortfall" and log[0]["short"] == {"outward": 2} and log[0]["refilled"] == 2
    refill = [c for c in sel if c.get("refill")]
    assert {c["cluster_id"] for c in refill} == {"a3", "a2"}                     # best score first


# ---------------------------------------------------------------- I6 outward sketches name the removed assumption
def test_outward_sketch_without_removes_is_dropped():
    _llm()
    from nano import ideate
    assert "REMOVES:" in ideate.SKETCH_FORMAT
    text = ("IDEA: a\nMECHANISM: m\nREMOVES: every layer computes the same thing\n\n"
            "IDEA: b\nMECHANISM: m\n\nIDEA: c\nMECHANISM: m\nREMOVES: none")
    ids = iter(["s1", "s2", "s3"]).__next__
    out = ideate.parse_sketches(text, card="formal", operator="outward", seed="", call_id="c", idgen=ids)
    assert [s["idea"] for s in out] == ["a"] and out[0]["removes"] == "every layer computes the same thing"
    ids = iter(["s1", "s2", "s3"]).__next__
    assert len(ideate.parse_sketches(text, card="formal", operator="inward", seed="", call_id="c", idgen=ids)) == 3
    ids = iter(["s1", "s2", "s3"]).__next__
    assert len(ideate.parse_sketches(text, card="deepen", operator="outward", seed="", call_id="c", idgen=ids)) == 3


# ---------------------------------------------------------------- E5, E16 prompt wording
def test_analogy_mix_and_no_creativity_nudges():
    _llm()
    from nano import ideate
    a = ideate.ANALOGY_ADDENDUM
    assert "near" in a and "far" in a and "Prefer analogues whose field is far" not in a
    assert "wild" not in ideate.EXCLUSION_ADDENDUM and "unconventional" not in ideate.EXCLUSION_ADDENDUM


# ---------------------------------------------------------------- I14 disputed facts
def test_disputed_fact_is_marked_next_round_and_shown_to_the_replan(monkeypatch):
    from nano import tree
    lp = _loop()
    sk = [{"id": "s1", "idea": "warmup is not the issue", "node": tree.OFF_TREE_ID}]
    lp._record_doubts(sk, "DOUBT: optimization: the schedule is fine per the map; measured: 6.9\n"
                          "IDEA: warmup is not the issue\nMECHANISM: m", 1)
    opt = next(n for n in lp.tree if n["id"] == "opt")
    assert tree.DISPUTED_HEAD not in tree.node_prompt(opt, "inward", "", lp.tree)   # not in the round that disputed it
    lp._promote_off_wins(2)
    p = tree.node_prompt(opt, "inward", "", lp.tree)
    assert tree.DISPUTED_HEAD in p and "(disputed, re-measure before relying on it)" in p and "measured: 6.9" in p
    lp._promote_off_wins(2)
    assert len(opt["disputed"]) == 1                                                 # once per sketch
    calls = []
    _patch_call(monkeypatch, lp, _reply([{"id": f"p{i}", "name": f"P{i}"} for i in range(5)]), calls)
    seen = []
    monkeypatch.setattr(lp, "_call", lambda prompt, *a, **k: seen.append(prompt) or SimpleNamespace(
        text=_reply([{"id": f"p{i}", "name": f"P{i}"} for i in range(5)]), call_id="c", usage=Usage(1, 1, 0, 0)))
    lp.replan_tree(2)
    assert "FACTS OF THE MAP THE TEAM DISPUTED (disputed, re-measure before relying on it)" in seen[0]
    assert "measured: 6.9" in seen[0]


# ---------------------------------------------------------------- I15 contexts counted after refusals and parse failures
def test_contexts_by_node_counts_contexts_that_ran(monkeypatch):
    from nano import tree
    lp = _loop()
    lp.do_research, lp.use_memory, lp.off_tree_share, lp.leap_share = False, False, 0.0, 0.0
    lp.tree = [n for n in lp.tree if n["id"] in ("root", "mix", "opt")]
    good = "IDEA: x\nMECHANISM: m\nREMOVES: the assumption a"

    def call(prompt, role, max_out, meta, **k):
        return SimpleNamespace(text="no sketches here" if meta.get("node") == "opt" and meta.get("operator") == "outward"
                               else good, call_id=f"c{id(prompt)}{meta.get('seed')}", usage=Usage(1, 1, 0, 0))
    monkeypatch.setattr(lp, "_call", call)
    monkeypatch.setattr(lp, "_ledger", lambda *a, **k: None)
    real = lp._afford
    monkeypatch.setattr(lp, "_afford", lambda stage, est, note="": False if note.startswith(
        next(n["name"] for n in lp.tree if n["id"] == "mix")) and "/ outward /" in note else real(stage, est, note))
    lp.ideate_round(1, [f"w{i}" for i in range(40)])
    ran = lp.contexts_by_node[1]
    st = lp._origin_stats()
    assert sum(ran.values()) == st["tree"]["contexts"]
    dec = [d for d in lp.decisions if d.get("step") == "contexts_ran"]
    assert dec and dec[-1]["ran"] < dec[-1]["dealt"]
    calls = {(s["node"], s["call_id"]) for s in lp.sketches}
    assert ran == {n: sum(1 for m, _ in calls if m == n) for n in {m for m, _ in calls}}
    assert tree.OFF_TREE_ID not in ran
