"""Issue 6: a re-plan must not drop what promotion (origin "offtree") or people (origin "human") put on the map."""
import json
from types import SimpleNamespace

from harness.schemas import Candidate, Usage


def _loop():
    from nano.loop import NanoLoop
    lp = NanoLoop("fixreplan", 1, "mock", 100000, 3, 0.0, None)
    (lp.run_dir / "problem.md").write_text("make the score lower", encoding="utf-8")
    return lp


def _planner_reply(n_parts: int = 5, extra: list[dict] | None = None) -> str:
    arr = [{"id": f"p{i}", "name": f"Fresh part {i}", "frame": f"frame {i}", "assumptions": ["a", "b", "c"],
            "boundary": "everything"} for i in range(n_parts)]
    return json.dumps(arr + (extra or []))


def _patch_planner(monkeypatch, lp, text):
    monkeypatch.setattr(lp, "_call", lambda *a, **k: SimpleNamespace(text=text, call_id="c1", usage=Usage(1, 1, 0, 0)))
    monkeypatch.setattr(lp, "_ledger", lambda *a, **k: None)


def _seed_tree(lp):
    from nano import tree
    lp.plan_with_model = False
    lp.plan_tree(1)
    win = tree.promote_win(lp.tree, "cand0001", "a winning cluster", "an off-map hypothesis", "change x")
    win["idea_assumptions"] = ["kept field"]
    lp.cands.append(Candidate(id="cand0001b", text="built under the win", card="implement", operator="x", seed="", perm=0,
                              round=1, call_id="c0", extra={"node": win["id"], "direction": "inward"}))
    lp._add_human_nodes([{"id": "Human_1", "name": "A part people care about", "frame": "people's frame",
                          "assumptions": ["h1"]}], 1)
    return win


def test_replan_carries_promoted_and_human_nodes(monkeypatch):
    from nano import tree
    lp = _loop()
    win = _seed_tree(lp)
    assert any(n["id"] == "human_1" and n["origin"] == "human" for n in lp.tree)
    assert any(d["step"] == "human_node" and d["node"] == "human_1" for d in lp.decisions)
    lp._write_tree()                                            # the promoted node counts one implemented candidate
    pt = json.loads((lp.run_dir / "problem_tree.json").read_text(encoding="utf-8"))
    st = next(n for n in pt["nodes"] if n["id"] == win["id"])["stats"]
    assert sum(v["implemented"] for v in st.values()) == 1

    _patch_planner(monkeypatch, lp, _planner_reply())
    lp.replan_tree(2)
    by_id = {n["id"]: n for n in lp.tree}
    assert by_id[win["id"]]["origin"] == "offtree" and by_id[win["id"]]["idea_assumptions"] == ["kept field"]
    assert by_id["human_1"]["origin"] == "human"
    assert {"p0", "p4"} <= set(by_id)
    assert tree.OFF_TREE_ID in by_id                            # the pseudo-node is back after the re-plan
    carry = [d for d in lp.decisions if d["step"] == "replan_carry"][-1]
    assert win["id"] in carry["kept"] and "human_1" in carry["kept"]
    assert win["id"] not in carry["dropped"] and "human_1" not in carry["dropped"]
    pt = json.loads((lp.run_dir / "problem_tree.json").read_text(encoding="utf-8"))
    assert {win["id"], "human_1"} <= {n["id"] for n in pt["nodes"]}


def test_replan_merges_duplicate_of_carried_node(monkeypatch):
    lp = _loop()
    win = _seed_tree(lp)
    dup = {"id": "newwin", "name": "Other wording", "refines": win["id"], "frame": "the planner's newer frame",
           "assumptions": ["z"], "boundary": "everything"}
    _patch_planner(monkeypatch, lp, _planner_reply(extra=[dup]))
    monkeypatch.setattr("nano.tree.parse_planner", _parse_keep_refines)
    lp.replan_tree(2)
    ids = [n["id"] for n in lp.tree]
    assert "newwin" not in ids and ids.count(win["id"]) == 1
    node = next(n for n in lp.tree if n["id"] == win["id"])
    assert node["origin"] == "offtree" and node["frame"] == "the planner's newer frame"
    carry = [d for d in lp.decisions if d["step"] == "replan_carry"][-1]
    assert {"id": win["id"], "planner_id": "newwin", "origin": "offtree"} in carry["merged"]


from nano import tree as _tree  # noqa: E402
_ORIG_PARSE = _tree.parse_planner


def _parse_keep_refines(text):
    """parse_planner as is, plus the `refines` field a planner may give (the parser does not keep it today)."""
    nodes = _ORIG_PARSE(text)
    ref = {str(n["id"]).lower(): n["refines"] for n in json.loads(text) if n.get("refines")}
    for n in nodes:
        if n["id"] in ref:
            n["refines"] = ref[n["id"]]
    return nodes
