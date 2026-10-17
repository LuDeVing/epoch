"""ISSUE 2: a node's design assumptions stay as planned; what tested ideas assumed lives in idea_assumptions.

Mock backend only (no tokens, no real training)."""
from __future__ import annotations

import importlib.util
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parents[2]
LAB = Path(os.environ.get("HTSA_REAL_LAB_ROOT", "D:/AGI-lab"))
BATCH = "mock-fix-assume"


def _llm():
    from nano import profile as PF
    PF.set_current(PF.load("llm"))
    return PF


def _head_tree():
    """nano/tree.py as committed at HEAD, loaded under another module name."""
    src = subprocess.run(["git", "show", "HEAD:nano/tree.py"], cwd=REPO, capture_output=True, text=True, check=True).stdout
    spec = importlib.util.spec_from_loader("tree_head", loader=None)
    mod = importlib.util.module_from_spec(spec)
    exec(compile(src, "tree_head.py", "exec"), mod.__dict__)
    return mod


def test_node_prompt_unchanged_without_idea_assumptions():
    PF = _llm()
    from nano import tree
    old = _head_tree()
    for n in PF.current().tree:
        for d in n["directions"]:
            assert tree.node_prompt(dict(n), d, "COMMON\n") == old.node_prompt(dict(n), d, "COMMON\n")
            assert tree.node_prompt({**n, "idea_assumptions": []}, d, "C\n") == old.node_prompt(dict(n), d, "C\n")


def test_node_prompt_idea_block_separate_newest_first_capped():
    PF = _llm()
    from nano import tree
    n = dict(next(x for x in PF.current().tree if x["id"] == "mix"))
    n["idea_assumptions"] = [{"from": f"c{i}", "text": f"idea text {i}", "round": 1, "kind": "silent"} for i in range(10)]
    p = tree.node_prompt(n, "outward", "")
    design = p.index("ASSUMPTIONS OF THIS PART:")
    block = p.index(tree.IDEA_ASSUMPTIONS_HEAD)
    assert design < block < p.index(tree.direction_text("outward"))
    assert "idea text 9" in p and "idea text 2" in p and "idea text 1" not in p
    assert p.index("idea text 9") < p.index("idea text 2")
    for a in n["assumptions"]:
        assert design < p.index(a) < block
    assert "idea text" not in tree.tree_text([n])        # the map text (gaps/doubt) shows design assumptions only


def test_old_files_migrate():
    _llm()
    from nano import tree
    old = {"id": "x", "assumptions": ["design a", "design b", "idea said c", "could not be built within the rules: z"],
           "assumptions_added": [{"from": "k1", "text": "idea said c"},
                                 {"from": "n1", "text": "could not be built within the rules: z"}]}
    tree.migrate_node(old)
    assert old["assumptions"] == ["design a", "design b"]
    assert [x["kind"] for x in old["idea_assumptions"]] == ["silent", "could_not_build"]
    assert "assumptions_added" not in old


@pytest.mark.skipif(not Path("D:/AGI-lab/.venv").exists(), reason="needs the lab's venv and mock baseline cache")
def test_mock_run_keeps_design_assumptions():
    PF = _llm()
    original = {n["id"]: len(n["assumptions"]) for n in PF.current().tree}
    for old in (LAB / "runs").glob(BATCH + "__*"):
        shutil.rmtree(old, ignore_errors=True)
    env = {**os.environ, "HTSA_LAB_ROOT": str(LAB), "HTSA_BACKEND": "mock", "PYTHONIOENCODING": "utf-8"}
    r = subprocess.run([sys.executable, "-m", "nano.dry_run", "--batch", BATCH, "--max-sketch-calls", "8",
                        "--implement", "2", "--rounds", "1"]
                       + ([] if os.environ.get("HTSA_FIX_FULL_RUN") else ["--stop-after", "deepened"]),   # no GPU checks by default
                       cwd=REPO, env=env, capture_output=True, text=True,
                       encoding="utf-8", errors="replace", timeout=3000)
    assert r.returncode == 0, r.stdout[-3000:] + r.stderr[-3000:]
    run = next((LAB / "runs").glob(BATCH + "__*"))
    pt = json.loads((run / "problem_tree.json").read_text(encoding="utf-8"))
    deep = json.loads((run / "deepen.json").read_text(encoding="utf-8")) if (run / "deepen.json").exists() else {}
    for n in pt["nodes"]:
        if n["id"] in original:                       # the mock planner keeps the default parts
            assert len(n["assumptions"]) == original[n["id"]], n["id"]
        assert "assumptions_added" not in n
        assert isinstance(n["idea_assumptions"], list)
        for x in n["idea_assumptions"]:
            assert x["kind"] in ("silent", "could_not_build") and x["text"] and "from" in x and "round" in x
    found_any = "the gate is applied after attention" in json.dumps(deep)
    total = sum(len(n["idea_assumptions"]) for n in pt["nodes"])
    if found_any:
        assert total > 0
    assert pt["stats"]["n_idea_assumptions"] == total
