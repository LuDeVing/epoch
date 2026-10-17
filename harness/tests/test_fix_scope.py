"""Issue 5: --only-nodes scope resolution no longer relies on an untold naming convention. The planner is told
the default parts and fills "refines" per node; resolve_scope uses it first, then the old id/name matching;
plan_tree re-asks once with the unresolved ids named before it falls back to the default tree."""
from __future__ import annotations

import json
from types import SimpleNamespace

import pytest

from nano import profile as PF
from nano import tree


@pytest.fixture(autouse=True)
def _llm_profile():
    prev = PF.current()
    PF.set_current("llm")
    yield
    PF.set_current(prev)


def _node(i, name, refines=None):
    n = {"id": i, "name": name, "frame": "f", "assumptions": ["a", "b", "c"], "boundary": "b"}
    if refines is not None:
        n["refines"] = refines
    return n


# renamed parts, ids and names share nothing with the defaults: only "refines" can resolve them
WITH_REFINES = json.dumps([
    _node("p1", "Token interface and tied head", "io"),
    _node("p2", "Positional geometry of attention", "mix"),
    _node("p3", "Head layout and KV sharing", "MIX"),
    _node("p4", "Gated feed-forward", "ffn"),
    _node("p5", "Residual stream and norms", "depth"),
    _node("p6", "A brand new memory module", "something-else"),
])
NAME_CONVENTION = json.dumps([
    _node("p1", "Inputs and outputs: tied embedding"),
    _node("p2", "Sequence mixing: rotary positions"),
    _node("p3", "Sequence mixing (attention): KV sharing"),
    _node("p4", "Per-token computation: SwiGLU"),
    _node("p5", "State across depth: pre-norm"),
])
NEITHER = json.dumps([
    _node("p1", "Token interface"),
    _node("p2", "Positional geometry"),
    _node("p3", "Head layout"),
    _node("p4", "Gated feed-forward"),
])


def test_planner_prompt_lists_default_parts_and_asks_for_refines():
    text = tree.planner_prompt("GOAL", "print(1)")
    assert '"refines": "<default part id this node refines or splits, or \\"new\\" if it is none of them>"' in text
    assert "DEFAULT PARTS (id: name):\n- io: inputs and outputs\n- mix: sequence mixing (attention)\n" in text
    assert "- recipe:" not in text and "- root:" not in text
    assert "starts its name with that part's name, then a colon" in text


def test_refines_resolves_renamed_parts():
    nodes = tree.parse_planner(WITH_REFINES)
    by_id = {n["id"]: n["refines"] for n in nodes}
    assert by_id["p2"] == "mix" and by_id["p3"] == "mix" and by_id["p6"] == "new"   # validated; unknown -> new
    assert by_id["root"] == "root" and by_id["recipe"] == "recipe"                  # copied from the profile tree
    got = tree.resolve_scope({"mix"}, nodes)
    assert isinstance(got, set) and got == {"p2", "p3"}
    assert tree.resolve_scope({"io", "depth"}, nodes) == {"p1", "p5"}


def test_name_convention_still_resolves_without_refines():
    nodes = tree.parse_planner(NAME_CONVENTION)
    assert all(n["refines"] == "new" for n in nodes if n["id"].startswith("p"))
    assert tree.resolve_scope({"mix"}, nodes) == {"p2", "p3"}


def test_neither_resolves_to_nothing_and_repair_names_the_id():
    nodes = tree.parse_planner(NEITHER)
    assert tree.resolve_scope({"mix"}, nodes) == set()
    text = tree.repair_prompt(["mix"], nodes)
    assert "These default parts were not mapped: mix (sequence mixing (attention))" in text
    assert '"refines" filled' in text and '"p2"' in text


def test_default_trees_carry_refines():
    for name in ("llm", "binpack", "binpack_nobase", "review_process"):
        for n in PF.load(name).tree:
            assert n["refines"] == n["id"], (name, n["id"])


def _fake_loop(tmp_path, replies):
    from nano import loop as L
    (tmp_path / "problem.md").write_text("GOAL", encoding="utf-8")
    prompts = []

    def call(prompt, role, max_tokens, meta, **kw):
        prompts.append((meta["card"], prompt))
        return SimpleNamespace(text=replies.pop(0), call_id="c", usage=None)

    fake = SimpleNamespace(plan_with_model=True, run_dir=tmp_path, baseline_src="x = 1", lens="parts",
                           diagnostics_text="", only_nodes={"mix"}, decisions=[], tree=None,
                           _call=call, _ledger=lambda *a, **k: None, _ensure_off_node=lambda: None,
                           _write_tree=lambda: None)
    return L.NanoLoop.plan_tree, fake, prompts


def test_plan_tree_repairs_before_falling_back(tmp_path):
    fixed = json.loads(NEITHER)
    fixed[1]["refines"] = "mix"
    plan, fake, prompts = _fake_loop(tmp_path, [NEITHER, json.dumps(fixed)])
    plan(fake, 1)
    assert [c for c, _ in prompts] == ["plan", "plan_repair"]
    assert "not mapped: mix" in prompts[1][1]
    assert tree.resolve_scope({"mix"}, fake.tree) == {"p2"}                       # planned map kept, repaired
    rep = [d for d in fake.decisions if d["step"] == "plan_repair"]
    assert rep and rep[0]["scope_unresolved"] == ["mix"] and rep[0]["still_unresolved"] == []


def test_plan_tree_falls_back_when_repair_fails(tmp_path):
    plan, fake, prompts = _fake_loop(tmp_path, [NEITHER, "no"])
    plan(fake, 1)
    assert [c for c, _ in prompts] == ["plan", "plan_repair"]
    assert [n["id"] for n in fake.tree] == [n["id"] for n in tree.DEFAULT_TREE]  # the existing fallback
    steps = [d["step"] for d in fake.decisions]
    assert steps == ["plan_repair", "plan"] and fake.decisions[1]["fallback"] == "default tree"


def test_plan_tree_no_repair_when_scope_resolves(tmp_path):
    plan, fake, prompts = _fake_loop(tmp_path, [WITH_REFINES])
    plan(fake, 1)
    assert [c for c, _ in prompts] == ["plan"] and fake.decisions == []
