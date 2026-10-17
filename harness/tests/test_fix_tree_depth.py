"""Fix 8: the problem tree is a real tree (parts, sub-parts, questions, helper questions; depth <= 4)."""
from __future__ import annotations

import copy
import importlib.util
import json
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]


def _head_tree():
    """nano/tree.py as committed at HEAD, loaded under another module name."""
    src = subprocess.run(["git", "show", "HEAD:nano/tree.py"], cwd=REPO, capture_output=True, text=True,
                         encoding="utf-8", check=True).stdout
    spec = importlib.util.spec_from_loader("tree_head", loader=None)
    mod = importlib.util.module_from_spec(spec)
    exec(compile(src, "tree_head.py", "exec"), mod.__dict__)
    return mod


def _built_tree():
    from nano import profile as PF, tree
    PF.set_current(PF.load("llm"))
    nodes = copy.deepcopy(tree.default_tree())
    nodes.append({"id": "keys", "name": "keys", "parent": "mix", "frame": "keys are a linear map of the input.",
                  "assumptions": ["keys share the query width"], "boundary": "Attention", "directions": ["inward", "outward"]})
    win = tree.promote_win(nodes, "c_win1", "gated residual", "a gate on the residual", "gate", part="state across depth")
    q = tree.add_failure_question(nodes, "keys", "c_bad1", "split keys", "the change reaches outside the part's boundary")
    return tree, nodes, win, q


def test_helpers_depth_path_children_leaves():
    tree, nodes, win, q = _built_tree()
    assert win["parent"] == "depth" and win["kind"] == "win"
    assert q["kind"] == "question" and q["parent"] == "keys" and q["from"] == ["c_bad1"]
    assert q["name"] == "why did split keys fail?" and q["directions"] == ["inward"] and q["boundary"] == "Attention"
    assert tree.add_failure_question(nodes, "keys", "c_bad2", "split keys", "x") is None      # same name: skipped
    assert tree.depth(nodes, "root") == 0 and tree.depth(nodes, "mix") == 1
    assert tree.depth(nodes, "keys") == 2 and tree.depth(nodes, q["id"]) == 3
    assert tree.path(nodes, "keys") == ["sequence mixing (attention)", "keys"]
    assert [n["id"] for n in tree.children(nodes, "mix")] == ["keys"]
    leaf_ids = {n["id"] for n in tree.leaves(nodes)}
    assert q["id"] in leaf_ids and win["id"] in leaf_ids and "keys" not in leaf_ids and "mix" not in leaf_ids
    assert [n["id"] for n in tree.subtree(nodes, "mix")] == ["mix", "keys", q["id"]]
    # an unmatched part puts a win under the root
    w2 = tree.promote_win(nodes, "c_win2", "x", "y", "z", part="no such part anywhere")
    assert w2["parent"] == "root"


def test_depth_cap_reattaches_and_logs():
    tree, nodes, _, q = _built_tree()
    h = {"id": "h1", "name": "helper", "parent": q["id"], "frame": "f", "assumptions": [], "boundary": "", "directions": ["inward"]}
    deep = {"id": "h2", "name": "too deep", "parent": "h1", "frame": "f", "assumptions": [], "boundary": "", "directions": ["inward"]}
    nodes += [h, deep]
    assert tree.depth(nodes, "h1") == 4 and tree.depth(nodes, "h2") == 5
    log = tree.enforce_depth(nodes)
    assert log == [{"step": "tree_depth", "node": "h2", "depth_was": 5, "from_parent": "h1", "to_parent": q["id"]}]
    assert tree.depth(nodes, "h2") == 4 and max(tree.depth(nodes, n["id"]) for n in nodes) == 4


def test_prompts_path_and_flat_identity():
    tree, nodes, _, q = _built_tree()
    head = _head_tree()
    mix = next(n for n in nodes if n["id"] == "mix")
    common = "COMMON\n\n"
    for d in ("inward", "outward"):
        assert tree.node_prompt(mix, d, common, nodes) == head.node_prompt(mix, d, common)
        assert tree.node_prompt(mix, d, common) == head.node_prompt(mix, d, common)
    keys = next(n for n in nodes if n["id"] == "keys")
    p = tree.node_prompt(keys, "inward", common, nodes)
    assert "PART UNDER STUDY: sequence mixing (attention) > keys\nWITHIN: " + " ".join(mix["frame"].split()) + "\n" in p
    flat = copy.deepcopy(tree.default_tree()) + [tree.off_tree_node()]
    assert tree.tree_text(flat, "diag") == head.tree_text(flat, "diag")
    text = tree.tree_text(nodes)
    assert "\n  - keys: " in text and "\n    - why did split keys fail?: " in text and "\n  - from an off-map win" in text


def test_dealing_shares_the_parent_budget():
    tree, nodes, _, q = _built_tree()
    flat = copy.deepcopy(tree.default_tree())
    dealt = tree.deal_contexts(flat, 3)
    assert all(v == 3 for v in dealt.values()) and ("mix", "outward") in dealt
    dealt = tree.deal_contexts(nodes, 3)
    assert dealt[("mix", "inward")] + dealt[("keys", "inward")] + dealt[(q["id"], "inward")] == 3
    assert dealt[(q["id"], "inward")] == 1 and (q["id"], "outward") not in dealt
    assert dealt[("mix", "outward")] + dealt[("keys", "outward")] == 3
    # a budget of one rotates over the node and its children by round
    got = {r: tree.deal_contexts(nodes, 1, r)[("mix", "inward")] for r in (1, 2)}
    assert got == {1: 1, 2: 0}


def test_planner_accepts_sub_parts():
    tree, *_ = _built_tree()
    arr = [{"id": i, "name": i, "frame": "f", "assumptions": ["a"]} for i in ("a", "b", "c", "d")]
    arr.append({"id": "a_sub", "name": "a sub", "frame": "f", "assumptions": ["a"], "parent": "a"})
    arr.append({"id": "mixsub", "name": "mix sub", "frame": "f", "assumptions": ["a"], "parent": "mix"})
    arr.append({"id": "lost", "name": "lost", "frame": "f", "assumptions": ["a"], "parent": "nowhere"})
    nodes = tree.parse_planner(json.dumps(arr))
    by = {n["id"]: n for n in nodes}
    assert by["a_sub"]["parent"] == "a" and by["mixsub"]["parent"] == "mix" and "mix" in by
    assert by["lost"]["parent"] == "root" and tree.depth(nodes, "a_sub") == 2


def test_mock_run_writes_nested_tree_with_a_failure_question(monkeypatch):
    """A tiny mock run (binpack_nobase, CPU scorer): one candidate's check fails with a reason, as the LLM mock's
    boundary breaker does, and the run leaves a question node under that part in problem_tree.json."""
    from harness import config
    from nano import dry_run
    from nano.checks import script

    orig = script.ScriptChecker.check
    state = {"failed": False}

    def check(self, candidate, out, baseline, **kw):
        rec = orig(self, candidate, out, baseline, **kw)
        if not Path(candidate).stem.startswith(("ctl", "tune")):
            state["failed"] = True
            rec = {**rec, "status": "fail", "rung_reached": 0,
                   "feedback": {"rung": 0, "reason": "the change reaches outside the part's boundary"}}
        return rec
    monkeypatch.setattr(script.ScriptChecker, "check", check)
    monkeypatch.setattr(script, "PY", Path(sys.executable))     # the lab root is a temp folder in tests: no venv there
    monkeypatch.setattr(sys, "argv", ["dry_run", "--profile", "binpack_nobase", "--batch", "mock-fix-tree",
                                      "--implement", "2", "--rounds", "1", "--max-sketch-calls", "8"])
    dry_run.main()
    pt = next(config.RUNS_DIR.glob("mock-fix-tree*")) / "problem_tree.json"
    d = json.loads(pt.read_text(encoding="utf-8"))
    assert d["tree"]["id"] == "root" and d["tree"]["children"]
    qs = [n for n in d["nodes"] if n.get("kind") == "question"]
    assert state["failed"] and qs, "no question node from the failed candidate"
    q = qs[0]
    assert q["depth"] == 2 and len(q["path"]) == 2 and q["origin"] == "failure"
    part = next(c for c in d["tree"]["children"] if any(k["id"] == q["id"] for k in c["children"]))
    assert part["id"] == q["parent"]
    assert all("depth" in n and "path" in n for n in d["nodes"])
