"""Bug pass 2026-10-17 (night), ideation half of nano/loop.py plus nano/tree.py. Unit level, mock backend."""
from __future__ import annotations

from types import SimpleNamespace

from harness.schemas import Usage


def _loop():
    from nano import profile as PF
    PF.set_current(PF.load("llm"))
    from nano.loop import NanoLoop
    lp = NanoLoop("bugideation", 1, "mock", 100000, 3, 0.0, None)
    (lp.run_dir / "problem.md").write_text("make the score lower", encoding="utf-8")
    lp.plan_with_model = False
    lp.plan_tree(1)
    return lp


def _node(lp, nid):
    return next(n for n in lp.tree if n["id"] == nid)


# ---------------------------------------------------------------- scope: a part's children follow the part
def test_children_of_a_skipped_part_are_skipped_and_children_of_a_scoped_part_are_in_scope():
    from nano import tree
    lp = _loop()
    q = tree.add_failure_question(lp.tree, "ffn", "cand1234", "wide mlp", "loss went up",
                                  feedback={"rung": 2, "reason": "gap allowed 0.0"})
    lp.skip_nodes = {"ffn"}
    assert lp._skipped(q["id"])                      # the owner excluded the part: its question goes too
    lp.skip_nodes, lp.only_nodes = set(), {"ffn"}
    assert not lp._skipped(q["id"])                  # the run is scoped to the part: its question is inside the scope
    assert lp._skipped("mix")


def test_deal_contexts_reaches_a_live_child_of_a_skipped_parent():
    from nano import tree
    nodes = [{"id": "root", "parent": None, "directions": ["upward"]},
             {"id": "a", "parent": "root", "directions": ["inward", "outward"]},
             {"id": "b", "parent": "a", "directions": ["inward", "outward"]}]
    dealt = tree.deal_contexts(nodes, 2, 1, lambda nid: nid == "a")
    assert dealt.get(("b", "inward"), 0) == 2 and dealt.get(("b", "outward"), 0) == 2, dealt
    assert ("a", "inward") not in dealt


# ---------------------------------------------------------------- the ignores-memory extra context keeps text seeds
def test_memory_free_extra_keeps_the_owner_and_contradiction_text(monkeypatch):
    lp = _loop()
    monkeypatch.setattr(lp, "memory", lambda: SimpleNamespace(read=lambda part: "an entry"))
    for card, text in (("owner", "OWNER: gate the mlp by depth"), ("contradiction", "'x' improved but cost step time x1.3")):
        specs = [(card, text, _node(lp, "ffn"), "inward")]
        out = lp._pick_memory_free(2, specs, ["river", "lantern"])
        assert len(out) == 2
        assert out[1][0] == card and out[1][1] == text, out[1]


# ---------------------------------------------------------------- a doubt line naming the off-map node is not lost
def test_record_doubts_never_files_a_dispute_under_the_off_map_node():
    from nano import tree
    lp = _loop()
    off = next(n for n in lp.tree if n["id"] == tree.OFF_TREE_ID)
    text = f"DOUBT: {off['name']}: the map says per-token computation is fine, measured: 0.3\nIDEA: wider mlp\nMECHANISM: m\n"
    sk = [{"id": "s1", "idea": "wider mlp", "node": tree.OFF_TREE_ID}]
    lp._record_doubts(sk, text, 1)
    rows = (lp.run_dir / "disputed_facts.jsonl").read_text(encoding="utf-8")
    assert '"node": "ffn"' in rows, rows


# ---------------------------------------------------------------- origin yield counts idea contexts only
def test_origin_stats_count_idea_contexts_not_deepen_calls():
    from nano import tree
    lp = _loop()
    lp.sketches = [{"id": "s1", "node": "ffn", "call_id": "c1", "card": "seeded", "origin": "tree"},
                   {"id": "s2", "node": "ffn", "call_id": "d1", "card": "deepen"},
                   {"id": "s3", "node": "ffn", "call_id": "d2", "card": "deepen"},
                   {"id": "s4", "node": tree.OFF_TREE_ID, "call_id": "c2", "card": "blank", "origin": "off"},
                   {"id": "s5", "node": tree.OFF_TREE_ID, "call_id": "d3", "card": "deepen"}]
    st = lp._origin_stats()
    assert st["tree"]["contexts"] == 1 and st["off"]["contexts"] == 1, st
    assert st["tree"]["sketches"] == 3 and st["off"]["sketches"] == 2      # an off-map idea's offshoot stays off-map


# ---------------------------------------------------------------- focus contexts never go to a skipped part
def test_focus_contexts_skip_a_part_the_owner_excluded(monkeypatch):
    lp = _loop()
    lp.do_research, lp.ideation_web, lp.use_memory, lp.leap_share = False, False, False, 0
    lp.skip_nodes = {"ffn"}
    monkeypatch.setattr(lp, "_pick_question", lambda r: {"id": "q1", "node": "ffn", "kind": "question", "test": {}})
    seen = []

    def call(prompt, role, max_tokens, meta, model=None, **k):
        seen.append(meta)
        return SimpleNamespace(text="", call_id=f"c{len(seen)}", usage=Usage(1, 1, 0, 0))
    monkeypatch.setattr(lp, "_call", call)
    monkeypatch.setattr(lp, "_ledger", lambda *a, **k: None)
    lp.ideate_round(2, ["river", "lantern", "harbor"])
    assert not [m for m in seen if m.get("card") == "sketch:focus"], [m for m in seen if m.get("node") == "ffn"]


# ---------------------------------------------------------------- interrogation offshoots carry origin and round
def test_deepen_offshoots_carry_the_parent_origin_and_the_round():
    from harness import llm
    from nano import dry_run as D
    from nano import tree
    lp = _loop()
    lp.do_premortem, lp.ideation_web, lp.deepen_depth = False, False, 0
    off = tree.OFF_TREE_ID
    lp.sketches = [{"id": "s2", "idea": "b", "mechanism": "m", "prediction": "p", "test": "t", "card": "blank", "call_id": "c2",
                    "node": off, "direction": "inward", "origin": "off", "round": 2}]
    llm.set_mock(D.mock)
    try:
        cl = {"cluster_id": f"{off}-in-k00", "name": "b", "node": off, "direction": "inward", "members": ["s2"],
              "representative": "s2", "cards": ["blank"]}
        assert lp.deepen_round(2, [cl], 0) > 0
    finally:
        llm.set_mock(None)
    offs = [s for s in lp.sketches if s.get("card") == "deepen"]
    assert offs and all(s.get("origin") == "off" and s.get("round") == 2 for s in offs), offs


# ---------------------------------------------------------------- the last round's yield is written
def test_close_yields_writes_the_last_round():
    import json
    lp = _loop()
    lp.round_now = 2
    lp.sketches = [{"id": "s1", "node": "ffn", "call_id": "c1", "card": "seeded", "origin": "tree", "round": 2, "seed": "x"}]
    lp._close_yields()
    sy = json.loads((lp.run_dir / "source_yield.json").read_text(encoding="utf-8"))["rounds"]
    assert sy[-1]["final"] and sy[-1]["round"] == 2 and sy[-1]["tree"]["contexts"] == 1, sy
    lp._close_yields()                                   # idempotent: one final record
    sy = json.loads((lp.run_dir / "source_yield.json").read_text(encoding="utf-8"))["rounds"]
    assert sum(1 for r in sy if r.get("final")) == 1
    if lp.seed_mode != "random":
        sd = json.loads((lp.run_dir / "seed_yield.json").read_text(encoding="utf-8"))["rounds"]
        assert sum(1 for r in sd if r.get("final")) == 1


# ---------------------------------------------------------------- doubt readiness counts parts, not failure questions
def test_doubt_ready_ignores_failure_question_nodes():
    from nano import tree
    lp = _loop()
    parts = [n["id"] for n in lp.tree if n["id"] not in ("root", tree.OFF_TREE_ID)]
    _, _, m0 = lp._doubt_ready(1)
    tree.add_failure_question(lp.tree, parts[0], "cand1234", "wide mlp", "loss went up", feedback={"rung": 2, "reason": "r"})
    _, _, m1 = lp._doubt_ready(1)
    assert m1 == m0, (m0, m1)


# ---------------------------------------------------------------- selection rows without a long-shot lane
def test_selection_rows_written_without_a_longshot_lane(monkeypatch):
    import json
    from nano import loop as L
    lp = _loop()
    lp.round_now, lp.longshot_share = 1, 0.0
    cl = [{"cluster_id": "ffn-in-k00", "name": "a", "node": "ffn", "direction": "inward", "cards": ["seeded"], "score": 1.0,
           "members": ["s0"], "representative": "s0"}]
    lp.clusters = cl
    monkeypatch.setattr(L.tree, "split_select", lambda by_node, k, *a, **kw: [cl[0]])
    lp._select_with_lanes({"ffn": cl}, 2, set())
    lp._select_with_lanes({"ffn": cl}, 2, set())
    rows = [json.loads(x) for x in (lp.run_dir / "selection.jsonl").read_text(encoding="utf-8").splitlines()]
    assert [r["reason"] for r in rows] == ["picked_main"], rows
    assert sum(1 for d in lp.decisions if d.get("step") == "slots_by_origin") == 1


# ---------------------------------------------------------------- the doubt decision counts the contexts after the cap
def test_doubt_decision_counts_after_the_cap(monkeypatch):
    lp = _loop()
    lp.do_research, lp.ideation_web, lp.use_memory, lp.leap_share = False, False, False, 0
    lp.max_sketch_calls, lp.off_tree_share = 3, 0.5
    monkeypatch.setattr(lp, "_doubt_ready", lambda r: (True, 1, 1))
    seen = []

    def call(prompt, role, max_tokens, meta, model=None, **k):
        seen.append(meta)
        return SimpleNamespace(text="IDEA: x\nMECHANISM: m\n", call_id=f"c{len(seen)}", usage=Usage(1, 1, 0, 0))
    monkeypatch.setattr(lp, "_call", call)
    monkeypatch.setattr(lp, "_ledger", lambda *a, **k: None)
    lp.ideate_round(1, [f"w{i}" for i in range(40)])
    dec = next(d for d in lp.decisions if d.get("step") == "doubt_cards")
    assert dec["dealt"] == sum(1 for m in seen if m.get("card") == "sketch:doubt"), (dec, seen)


# ---------------------------------------------------------------- under a full test cap the guard replaces a spare context
def test_memory_free_guard_takes_a_spare_slot_under_a_full_cap(monkeypatch):
    lp = _loop()
    monkeypatch.setattr(lp, "memory", lambda: SimpleNamespace(read=lambda part: "an entry" if part == "ffn" else ""))
    mix = _node(lp, "mix")
    specs = [("seeded", "river", _node(lp, "ffn"), "inward"), ("seeded", "lantern", mix, "inward"),
             ("blank", "harbor", mix, "outward")]
    out = lp._pick_memory_free(1, specs, ["apple", "pear"], room=0)
    assert len(out) == 3, out                           # the cap holds
    assert sum(1 for sp in out if sp[2]["id"] == "ffn") == 2 and sum(1 for sp in out if sp[2]["id"] == "mix") == 1
    assert len(lp.memory_free) == 1
    out = lp._pick_memory_free(1, specs[:2], ["apple", "pear"], room=0)
    assert len(out) == 2 and not lp.memory_free         # no part can spare one: no guard, the cap still holds
