"""The byte lock (docs/MULTIPLAYER_DESIGN.md section 12.2): under prompt_style v1 and with no shared-space event,
every template and prompt builder renders exactly what the code at commit 74abcaf rendered.

Primary, fast, deterministic: each of nano/ideate.py, tree.py, deepen.py, research.py, memory.py and loop.py is loaded
from `git show 74abcaf:<file>` under another module name (the pattern of test_fix_assumptions.py) and compared on
fixed inputs: every *_FORMAT, *_ADDENDUM, *_HEAD, *_NOTE string and ideate.TEMPLATES; the tree, deepen and research
prompt builders; the memory block; and, on two NanoLoop objects (the current class and the one of 74abcaf) built the
same way in the test's temp lab, spec_prompt, history_text, _common, _focus_addendum and the idea-agent prompts.

Secondary, slow, opt-in (HTSA_SLOW_BYTELOCK=1): one mock dry run compared with a stored set of normalised prompt
hashes made by the owner from a worktree of 74abcaf (harness/tests/fixtures/bytelock_74abcaf.json). Skipped when the
variable or the fixture is missing.
"""
from __future__ import annotations

import copy
import hashlib
import importlib.util
import json
import os
import re
import subprocess
import sys
from pathlib import Path

import pytest

from harness import llm
from harness.schemas import Candidate
from nano import profile as PF
from nano import prompt_style as PS

REPO = Path(__file__).resolve().parents[2]
HEAD = "74abcaf"
SUFFIXES = ("_FORMAT", "_ADDENDUM", "_HEAD", "_NOTE")
_CACHE: dict = {}


def _head(name: str):
    """nano/<name>.py as committed at 74abcaf, loaded under another module name, so the comparison is not vacuous."""
    if name not in _CACHE:
        src = subprocess.run(["git", "show", f"{HEAD}:nano/{name}.py"], cwd=REPO, capture_output=True, text=True,
                             encoding="utf-8", check=True).stdout
        spec = importlib.util.spec_from_loader(f"{name}_head_{HEAD}", loader=None)
        mod = importlib.util.module_from_spec(spec)
        mod.__file__ = str(REPO / "nano" / f"{name}.py")
        exec(compile(src, f"{name}_head.py", "exec"), mod.__dict__)
        _CACHE[name] = mod
    return _CACHE[name]


@pytest.fixture(autouse=True)
def _v1():
    PS.reset()
    PS.set_style("v1")
    yield
    PS.reset()


def _use(profile: str):
    PF.set_current(PF.load(profile))
    return PF.current()


# ---------------------------------------------------------------- constants
@pytest.mark.parametrize("name", ["ideate", "tree", "deepen", "research", "memory", "loop"])
@pytest.mark.parametrize("profile", ["binpack_nobase", "llm"])
def test_template_constants_identical(name, profile):
    _use(profile)
    import importlib
    new, old = importlib.import_module(f"nano.{name}"), _head(name)
    names = [k for k in dir(old) if k.endswith(SUFFIXES) and isinstance(getattr(old, k, None), str)]
    if name == "deepen":
        names += list(old._RENDERED)                       # rendered for the active profile on access
    assert names or name in ("memory", "research", "loop")
    for k in names:
        assert getattr(new, k) == getattr(old, k), f"{name}.{k} changed under v1"
    if name == "ideate":
        assert new.TEMPLATES == old.TEMPLATES
        for t in old.TEMPLATES:
            assert new.render(t) == old.render(t)


# ---------------------------------------------------------------- tree prompt builders
def _trees():
    out = []
    for prof in ("binpack_nobase", "llm"):
        p = _use(prof)
        nodes = copy.deepcopy(p.tree)
        part = next(n for n in nodes if n.get("parent") == "root")
        child = {"id": "sub1", "name": "a sub part", "parent": part["id"], "frame": "a narrower frame",
                 "assumptions": ["one"], "boundary": part.get("boundary", ""), "directions": ["inward", "outward"]}
        part = dict(part, idea_assumptions=[{"from": "c1", "text": "an idea assumed this", "round": 1, "kind": "silent"}],
                    disputed=[{"round": 1, "text": "a fact (disputed by ana: no [measured])", "sketch_id": "e5"}])
        nodes = [part if n["id"] == part["id"] else n for n in nodes] + [child]
        out.append((prof, nodes))
    return out


def test_tree_builders_identical():
    from nano import tree
    old = _head("tree")
    for prof, nodes in _trees():
        _use(prof)
        assert tree.tree_text(nodes) == old.tree_text(nodes)
        assert tree.tree_text(nodes, "diag") == old.tree_text(nodes, "diag")
        for d in ("inward", "outward", "upward", "inward_free", "outward_free"):
            assert tree.direction_text(d) == old.direction_text(d)
        for n in nodes:
            for d in n.get("directions", []):
                assert tree.node_prompt(dict(n), d, "COMMON\n", nodes) == old.node_prompt(dict(n), d, "COMMON\n", nodes)
                assert tree.node_prompt(dict(n), d, "C\n") == old.node_prompt(dict(n), d, "C\n")
        for card in old.OFF_TREE_CARDS:
            for d in ("inward", "outward"):
                assert tree.off_tree_prompt(card, nodes, "C\n", "diag", d) == old.off_tree_prompt(card, nodes, "C\n", "diag", d)
        for lens in old.LENSES:
            assert tree.planner_prompt("GOAL", "src = 1", lens, "diag") == old.planner_prompt("GOAL", "src = 1", lens, "diag")
        assert tree.repair_prompt({"x", "y"}, nodes) == old.repair_prompt({"x", "y"}, nodes)


# ---------------------------------------------------------------- deepen prompt builders
OBJS = [{"text": "it adds a hidden cost", "if_true": {"metric": "step_ratio", "op": "above", "threshold": 1.2}, "cls": "hidden_cost"},
        {"text": "within noise", "if_true": None, "cls": "below_noise"}]
REPLIES = {1: {"kind": "rebut", "fact": "0.004 spread", "source": "measured", "change": "", "test": None},
           2: {"kind": "measure", "fact": "", "source": "", "change": "",
               "test": {"metric": "learn_z", "op": "above", "threshold": 0.5, "rung": "rung 3"}}}


@pytest.mark.parametrize("profile", ["binpack_nobase", "llm"])
def test_deepen_builders_identical(profile):
    _use(profile)
    from nano import deepen
    old = _head("deepen")
    for web in (False, True):
        a = ("IDEA: x", "the part", "a frame", "- rule", web)
        assert deepen.root_prompt(*a, code="src", research="R", history="H") == old.root_prompt(*a, code="src", research="R", history="H")
        assert deepen.root_prompt(*a) == old.root_prompt(*a)
        b = ("IDEA: x", "why?", ["k1", "k2"], "the part", "- rule", web)
        assert deepen.child_prompt(*b, code="s", history="H", chain="L1") == old.child_prompt(*b, code="s", history="H", chain="L1")
    pm = ("IDEA: x", "the part", "- rule", "src", ["fact 1"])
    assert deepen.premortem_prompt(*pm) == old.premortem_prompt(*pm)
    assert (deepen.premortem_prompt(*pm, chain="L1: a", failed=["f http://x"], findings="Q1: y")
            == old.premortem_prompt(*pm, chain="L1: a", failed=["f http://x"], findings="Q1: y"))
    assert deepen.premortem_prompt(*pm, peer="") == old.premortem_prompt(*pm)
    assert deepen.reply_prompt("IDEA", "CHAIN", OBJS) == old.reply_prompt("IDEA", "CHAIN", OBJS)
    assert deepen.reply_prompt("IDEA", "", OBJS, [2], peer="") == old.reply_prompt("IDEA", "", OBJS, [2])
    assert deepen.critic_update_prompt(OBJS, REPLIES) == old.critic_update_prompt(OBJS, REPLIES)
    assert (deepen.premortem_questions_prompt("IDEA", "part", "- rule", chain="L1")
            == old.premortem_questions_prompt("IDEA", "part", "- rule", chain="L1"))


@pytest.mark.parametrize("profile", ["binpack_nobase", "llm"])
def test_research_builders_identical(profile):
    p = _use(profile)
    from nano import research
    old = _head("research")
    node = dict(next(n for n in p.tree if n.get("parent") == "root"))
    assert research.preread_prompt("GOAL") == old.preread_prompt("GOAL")
    assert research.research_prompt(node, "GOAL") == old.research_prompt(node, "GOAL")
    assert research.analogy_prompt(node, "GOAL") == old.analogy_prompt(node, "GOAL")
    assert research.findings_prompt(["q1", "q2"], "ctx") == old.findings_prompt(["q1", "q2"], "ctx")
    assert research.fetch_prompt("what?", node) == old.fetch_prompt("what?", node)
    assert research.fetch_prompt("what?") == old.fetch_prompt("what?")


def test_memory_block_identical(tmp_path):
    from nano import memory
    old = _head("memory")
    d = tmp_path / "mem" / "binpack_nobase"
    d.mkdir(parents=True)
    (d / "choice.md").write_text("# Memory: choice\nCLOCK: 3\n## FACTS\n- [m1a2b3c] 2026-10-17 | run7 r1 | measured | "
                                 "best fit beat first fit | used 2\n## TRIED\n- [m2b3c4d] 2026-10-17 | run7 r1 | belief | "
                                 "worst fit | used 0\n", encoding="utf-8")
    assert memory.Memory(tmp_path / "mem", "binpack_nobase").block("choice") == old.Memory(tmp_path / "mem", "binpack_nobase").block("choice")
    assert memory.Memory(tmp_path / "mem", "binpack_nobase").block("choice")


# ---------------------------------------------------------------- the loop: spec_prompt, history, _common, focus, idea agents
class _QuietSpace:
    """A space with no events: every slot must render the empty string."""
    notes: list = []

    def digest_for(self, role, node):
        return ""

    def comments_on(self, idea):
        return []

    def objections_from_people(self, idea):
        return []

    def disputes_on(self, node):
        return []


def _sk(i, node, kind="port"):
    return {"id": f"s{i:010x}", "idea": f"idea {i}", "mechanism": f"mechanism {i}", "prediction": "fewer bins",
            "test": "score", "node": node, "direction": "inward", "card": "seeded", "kind": kind, "round": 1,
            "target": "t" if i % 2 else "", "breaks": "b", "keeps": "k", "kill": "x"}


def _setup(lp, prof):
    from nano import tree
    (lp.run_dir / "problem.md").write_text("GOAL: pack well\n\nPURPOSE: test\n\nHARD CONSTRAINTS:\n- one\n- two\n", encoding="utf-8")
    nodes = copy.deepcopy(prof.tree)
    lp.tree = nodes
    lp._ensure_off_node()
    part = next(n["id"] for n in nodes if n.get("parent") == "root")
    lp.sketches = [_sk(i, part, "leap" if i == 0 else "port") for i in range(4)]
    lp.clusters = [{"cluster_id": f"{part}-in-1", "name": "a cluster", "members": [s["id"] for s in lp.sketches],
                    "representative": lp.sketches[0]["id"], "node": part, "direction": "inward", "cards": ["seeded"],
                    "score": 1.0, "rank": 1, "lane": "main"}]
    lp.deepen_nodes = [{"id": "d1", "cluster_id": f"{part}-in-1", "members": [lp.sketches[0]["id"]], "parent": None,
                        "known": ["k1 [script]"], "objections": [dict(o, severity="high") for o in OBJS],
                        "premortem_verdict": "noise", "chain": []}]
    lp.history = [{"round": 1, "cand_id": "n0000000001", "node": part, "hypothesis": "first fit", "status": "fail",
                   "reason": "rung 0", "learn_gap": 0.01}]
    lp.control_note = "look at ties first"
    lp._focus_q = {"id": "q1", "text": "does order matter?", "test": {"metric": "learn_gap", "what": "the gap"},
                   "threshold": 0.0, "fails_if": "no change", "requires_human": False}
    lp.baseline_src = lp.working_src = "def choose_bin(item, bins, capacity):\n    return -1\n"
    lp.fact_check = False
    lp.use_memory = False
    lp.leap_share = 0.0
    lp.ideation_web = False
    lp.web_mode = "off"
    lp.max_sketch_calls = 6
    lp.pick_questions = False
    lp.contradiction_cards = False
    return part


def _pair(prof_name, batch):
    from nano import loop as L
    prof = _use(prof_name)
    old = _head("loop")
    a = L.NanoLoop(batch, 0, "mock", 100_000, 2, 60.0, None)
    b = old.NanoLoop(batch, 0, "mock", 100_000, 2, 60.0, None)
    part = _setup(a, prof)
    _setup(b, prof)
    return a, b, part


@pytest.mark.parametrize("profile", ["binpack_nobase", "llm"])
def test_loop_prompts_identical(profile):
    a, b, part = _pair(profile, f"bytelock-{profile}")
    cid = a.clusters[0]["cluster_id"]
    parent = Candidate(id="n0000000001", text="t", card="impl:seeded", operator=cid, seed="", perm=0, round=1, call_id="c1",
                       program=a.baseline_src, extra={"hypothesis": "first fit", "node": part, "members": a.clusters[0]["members"],
                                                      "target": "t", "kind": "port"})
    fb = {"rung": 1, "reason": "it raised", "status": "fail"}
    for card, op, parent_, fb_ in (("implement", cid, None, None), ("revise", "fix", parent, fb), ("revise", "variant:narrow", parent, fb),
                                   ("seeded", "none", None, None), ("formal", "none", None, None),
                                   ("low_prior", "none", None, None), ("transform", "the rule is greedy", None, None)):
        want = b.spec_prompt(card, "a seed", op, parent_, fb_)
        assert a.spec_prompt(card, "a seed", op, parent_, fb_) == want, f"spec_prompt {card} changed under v1"
        a.space = _QuietSpace()                            # a space with nothing to say changes no byte
        assert a.spec_prompt(card, "a seed", op, parent_, fb_) == want
        a.space = None
    assert a.history_text() == b.history_text()
    assert a._common(a.baseline_src, True, "x:y:z") == b._common(b.baseline_src, True, "x:y:z")
    assert a._common(a.baseline_src, False) == b._common(b.baseline_src, False)
    assert a._focus_addendum() == b._focus_addendum()


@pytest.mark.parametrize("round_no", [1, 2])
def test_idea_agent_prompts_identical(round_no):
    """The idea-agent prompt assembly (ideate_round's _one) on both classes: the same contexts, the same prompts."""
    a, b, _ = _pair("binpack_nobase", f"bytelock-ideas-{round_no}")
    seen: dict = {"cur": None}
    got: dict = {"a": [], "b": []}

    def mock(prompt, role, meta):
        got[seen["cur"]].append((str(meta.get("card")), str(meta.get("node")), str(meta.get("seed")), prompt))
        return ""
    try:
        llm.set_mock(mock)
        from nano.loop import _seeds
        for key, lp in (("a", a), ("b", b)):
            seen["cur"] = key
            lp.ideate_round(round_no, _seeds())
    finally:
        llm.set_mock(None)
    assert got["a"] and sorted(got["a"]) == sorted(got["b"])


# ---------------------------------------------------------------- the slow dry-run comparison (opt-in)
_NORM = [(re.compile(r"\b[snucd][0-9a-f]{10}\b"), "<id>"), (re.compile(r"q_[0-9a-f]{8}"), "<q>"),
         (re.compile(r"win_[0-9a-f]{8}"), "<win>"), (re.compile(r"u[0-9a-f]{10}"), "<u>"),
         (re.compile(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(\.\d+)?Z?"), "<ts>")]


def normalised_hash(text: str) -> str:
    for rx, rep in _NORM:
        text = rx.sub(rep, text)
    return hashlib.sha1(text.encode("utf-8")).hexdigest()


@pytest.mark.skipif(os.environ.get("HTSA_SLOW_BYTELOCK") != "1"
                    or not (Path(__file__).parent / "fixtures" / "bytelock_74abcaf.json").exists(),
                    reason="slow opt-in (HTSA_SLOW_BYTELOCK=1) and the owner's fixture bytelock_74abcaf.json")
def test_dry_run_prompt_hashes_identical(monkeypatch):
    from harness import config
    from nano import dry_run
    from nano.checks import script
    monkeypatch.setattr(script, "PY", Path(sys.executable))
    monkeypatch.setattr(sys, "argv", ["dry_run", "--batch", "bytelock", "--profile", "binpack_nobase", "--implement", "2",
                                      "--rounds", "1", "--max-sketch-calls", "12", "--stop-after", "built"])
    try:
        assert dry_run.main() == 0
    finally:
        llm.set_mock(None)
    run = next(config.RUNS_DIR.glob("bytelock__*"))
    got = sorted(normalised_hash(p.read_text(encoding="utf-8")) for p in (run / "prompts").glob("*.txt"))
    want = json.loads((Path(__file__).parent / "fixtures" / "bytelock_74abcaf.json").read_text(encoding="utf-8"))["hashes"]
    assert got == sorted(want)
    assert "prompt_style" not in json.loads((run / "commitments.json").read_text(encoding="utf-8"))
