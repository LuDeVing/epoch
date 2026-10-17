"""Tests for data.py, score.py, arms/ and bench.py (owner: bench). Mock backend only, temporary lab
root via monkeypatched config paths; arc_exec, think and ledger are stubbed so these tests do not
depend on other owners' modules."""
from __future__ import annotations

import json
import re
import sys
import types
from pathlib import Path

import pytest

import harness
from harness import config, llm
from harness import data, score, bench
from harness.arms import run_arm
from harness.arms import plain as plain_mod
from harness.arms import best_of_n as bon
from harness.schemas import Answer, read_json, read_jsonl, strip_key

FLIP = "```python\ndef transform(grid):\n    return [row[::-1] for row in grid]\n```"
IDENT = "```python\ndef transform(grid):\n    return [row[:] for row in grid]\n```"
TEST_IN = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
TEST_OUT_TEXT = "3 2 1\n6 5 4\n9 8 7"
REAL_ARC = Path(r"D:\AGI-lab\data\arc\ARC-AGI-master\data\evaluation")
REAL_BT = Path(r"D:\AGI-lab\data\brainteaser\SP.jsonl")


# ---------------------------------------------------------------- fixtures
def _fake_arc(root: Path) -> None:
    d = root / "arc" / "ARC-AGI-master" / "data" / "evaluation"
    d.mkdir(parents=True)
    for i in range(70):
        size = 25 if i % 7 == 0 else 3
        g = [[5 if c == 0 else 0 for c in range(size)] for _r in range(size)]   # not mirror-symmetric
        train = [{"input": g, "output": [row[::-1] for row in g]} for _ in range(2)]
        test = [{"input": TEST_IN, "output": [row[::-1] for row in TEST_IN]}]
        if i % 10 == 0:
            test = test * 2
        (d / f"{i:08x}.json").write_text(json.dumps({"train": train, "test": test}), encoding="utf-8")


def _fake_bt(root: Path) -> None:
    d = root / "brainteaser"
    d.mkdir(parents=True)
    rows = []
    for g in range(50):
        for k, suffix in enumerate(("", "_SR", "_CR")):
            choices = [f"wrong a{g}", f"RIGHT {g}", f"wrong b{g}", "None of above."]
            rot = (g + k) % 4
            choices = choices[rot:] + choices[:rot]
            rows.append({"id": f"SP-{g}{suffix}", "question": f"Puzzle {g} variant {k}?",
                         "answer": f"RIGHT {g}", "label": choices.index(f"RIGHT {g}"),
                         "choice_list": repr(choices), "choice_order": [0, 1, 2, 3]})
    (d / "SP.jsonl").write_text("\n".join(json.dumps(r) for r in rows) + "\n", encoding="utf-8")


def _run_prog(src, grid):
    ns: dict = {}
    try:
        exec(src, ns)  # noqa: S102 - test stub for arc_exec
        return [[int(c) for c in row] for row in ns["transform"]([list(r) for r in grid])]
    except Exception:  # noqa: BLE001
        return None


def _stub_arc_exec():
    m = types.ModuleType("harness.arc_exec")
    m.predict = lambda src, g: _run_prog(src, g)
    m.demo_match = lambda src, train: {
        "matched": sum(_run_prog(src, p["input"]) == p["output"] for p in train),
        "total": len(train), "diffs": [], "errors": []}
    return m


PROMPTS: list[str] = []


def default_mock(prompt: str, role: str, meta: dict) -> str:
    """ARC: the flip program; BT: the displayed letter of the RIGHT option."""
    PROMPTS.append(prompt)
    if meta.get("benchmark") == "arc":
        return "Rows are mirrored.\n" + FLIP
    for line in prompt.splitlines():
        mt = re.match(r"^([A-D])\. RIGHT", line)
        if mt:
            return f"The trick is wordplay.\nANSWER: {mt.group(1)}"
    return "ANSWER: A"


@pytest.fixture
def lab(tmp_path, monkeypatch):
    root = tmp_path / "lab"
    paths = {"LAB_ROOT": root, "RUNS_DIR": root / "runs", "MEMORY_DIR": root / "memory",
             "VIEWS_DIR": root / "memory" / "views", "LEDGER_PATH": root / "memory" / "ledger.jsonl",
             "DATA_DIR": root / "data", "RESULTS_DIR": root / "results", "RAW_DATA_DIR": root / "raw",
             "SEEDS_PATH": root / "no_seeds.txt"}
    for k, v in paths.items():
        monkeypatch.setattr(config, k, v)
    for k in ("RUNS_DIR", "MEMORY_DIR", "DATA_DIR", "RESULTS_DIR"):
        paths[k].mkdir(parents=True, exist_ok=True)
    _fake_arc(root / "raw")
    _fake_bt(root / "raw")
    stub = _stub_arc_exec()
    monkeypatch.setitem(sys.modules, "harness.arc_exec", stub)
    monkeypatch.setattr(harness, "arc_exec", stub, raising=False)
    monkeypatch.setitem(sys.modules, "harness.ledger", None)   # force the arms' fallback writer
    data._CACHE.clear()
    PROMPTS.clear()
    llm.set_mock(default_mock)
    data.build_items()
    yield root
    llm.set_mock(None)
    data._CACHE.clear()


def _key_free(root: Path) -> None:
    """No prompt and no run file carries a key field or the ARC test output."""
    for p in PROMPTS:
        assert TEST_OUT_TEXT not in p and '"label"' not in p and "test_output" not in p
    for f in (root / "runs").rglob("*"):
        if f.is_file():
            txt = f.read_text(encoding="utf-8")
            assert '"test_output"' not in txt and '"label"' not in txt, f


# ---------------------------------------------------------------- data.py
def test_build_items_fake(lab):
    counts = data.build_items()
    assert counts["arc"] == {"dev-tune": 16, "dev-ablate": 12, "test": 12, "total": 40}
    assert counts["bt"]["total"] == 120
    arc = data.load_items("arc")
    assert all(len(it["train"]) == 2 and len(it["test_input"]) == 3 for it in arc)
    assert len({it["id"] for it in arc}) == 40
    bt = data.load_items("bt")
    by_group: dict = {}
    for it in bt:
        by_group.setdefault(it["group"], set()).add(it["split"])
        assert it["choices"][it["label"]].startswith("RIGHT") and it["family"] == "bt_sp"
    assert all(len(s) == 1 for s in by_group.values())          # variants never cross splits
    ids1 = [it["id"] for it in arc]
    data.build_items()
    assert [it["id"] for it in data.load_items("arc")] == ids1    # deterministic
    assert data.get_item("bt", bt[0]["id"])["question"] == bt[0]["question"]
    assert {it["split"] for it in data.load_items("arc", "test")} == {"test"}


@pytest.mark.skipif(not (REAL_ARC.exists() and REAL_BT.exists()), reason="raw downloads absent")
def test_build_items_real(lab):
    counts = data.build_items(arc_dir=REAL_ARC, bt_path=REAL_BT)
    assert counts["arc"]["total"] == 40 and counts["bt"]["total"] == 120
    for it in data.load_items("arc"):
        task = {"train": it["train"], "test": [{"input": it["test_input"], "output": it["test_output"]}]}
        assert data.arc_total_cells(task) <= 600


# ---------------------------------------------------------------- parsing
def test_parse_letter_and_program():
    assert plain_mod.parse_letter("blah\nANSWER: c") == 2
    assert plain_mod.parse_letter("Final ANSWER: **B**") == 1
    assert plain_mod.parse_letter("I think\nD\n") == 3
    assert plain_mod.parse_letter("so the answer is (A).") == 0
    assert plain_mod.parse_letter("no letter here") is None
    assert "row[::-1]" in plain_mod.parse_program("x\n" + IDENT + "\nthen\n" + FLIP)
    assert plain_mod.parse_program("def transform(g):\n    return g") is not None
    assert plain_mod.parse_program("nothing") is None


# ---------------------------------------------------------------- arms
def test_plain_arms_write_run_folders(lab):
    arc_item, bt_item = data.load_items("arc")[0], data.load_items("bt")[0]
    for item in (arc_item, bt_item):
        ans = run_arm("plain", item, m=20, replicate=0, backend="mock", batch="b0")
        assert score.is_correct(item, ans.answer) and ans.spent_tokens > 0
        rd = config.RUNS_DIR / plain_mod.run_id_for("b0", item["benchmark"], item["id"], "plain", 0)
        assert (rd / "answer.json").exists()
        assert len(list((rd / "prompts").glob("*.txt"))) == 1
        assert len(list((rd / "calls").glob("*.json"))) == 1
        assert len(list((rd / "cands").glob("*.jsonl"))) == 1
    rows = read_jsonl(config.RESULTS_DIR / "b0" / "runs.jsonl")
    assert [r["arm"] for r in rows] == ["plain", "plain"]
    assert set(rows[0]) >= {"batch", "benchmark", "item_id", "arm", "replicate", "run_id", "status",
                            "answer", "spent_tokens", "rounds", "ts"}
    assert len(read_jsonl(config.LEDGER_PATH)) == 2
    _key_free(lab)


def test_bestofn_budget_controls_n(lab):
    item = data.load_items("bt")[0]
    one = run_arm("plain", item, m=20, replicate=0, backend="mock", batch="b1").spent_tokens
    ans = run_arm("bestofn_vote", item, m=20, replicate=0, backend="mock", batch="b1",
                  budget_tokens=int(5.5 * one))
    row = [r for r in read_jsonl(config.RESULTS_DIR / "b1" / "runs.jsonl") if r["arm"] == "bestofn_vote"][0]
    assert row["n_calls"] == 5 and ans.spent_tokens <= 5.5 * one
    ans = run_arm("bestofn_vote", item, m=3, replicate=1, backend="mock", batch="b1")
    assert ans.spent_tokens == 3 * one                              # no budget: N = m


def test_vote_vs_verify_on_arc(lab):
    def mock(prompt, role, meta):
        PROMPTS.append(prompt)
        return IDENT if meta.get("index", 0) < 2 else FLIP
    llm.set_mock(mock)
    item = data.load_items("arc")[0]
    v = run_arm("bestofn_vote", item, m=3, replicate=0, backend="mock", batch="b2")
    assert v.answer == TEST_IN and not score.is_correct(item, v.answer)
    w = run_arm("bestofn_verify", item, m=3, replicate=0, backend="mock", batch="b2")
    assert w.status == "solved" and w.verification_type == "demo_match"
    assert score.is_correct(item, w.answer)
    _key_free(lab)


def test_vote_tie_goes_to_first():
    from harness.schemas import Candidate
    mk = lambda p: Candidate(id=p + "x", text=p, card="bestofn", operator="none", seed="", perm=0,
                             round=0, call_id="c", pred=p)
    assert bon.vote([mk("B"), mk("A"), mk("A"), mk("B")]).pred == "B"
    assert bon.vote([mk("C"), mk("A"), mk("A")]).pred == "A"
    assert bon.vote([]) is None


def test_seeded_bestofn_seeds_and_perms(lab, monkeypatch):
    item = data.load_items("bt")[0]
    ans = run_arm("seeded_bestofn", item, m=4, replicate=0, backend="mock", batch="b3")
    assert score.is_correct(item, ans.answer)                      # perm mapped back to canonical
    rd = config.RUNS_DIR / plain_mod.run_id_for("b3", "bt", item["id"], "seeded_bestofn", 0)
    cands = [read_jsonl(f)[0] for f in (rd / "cands").glob("*.jsonl")]
    assert len(cands) == 4 and all(c["seed"] in bon.DEFAULT_SEEDS for c in cands)
    assert all(score.cand_correct(item, c) for c in cands)
    assert all("Seed word" in p for p in PROMPTS)
    words = lab / "concepts.txt"
    words.write_text("# comment\nalpha\nbeta\n", encoding="utf-8")
    monkeypatch.setattr(config, "SEEDS_PATH", words)
    assert bon.seed_words() == ["alpha", "beta"]
    assert bon.seed_for("x", "seeded_bestofn", 0, 1, ["a", "b", "c"]) == \
        bon.seed_for("x", "seeded_bestofn", 0, 1, ["a", "b", "c"])
    _key_free(lab)


# ---------------------------------------------------------------- score.py
def test_is_correct_and_bootstrap():
    arc = {"benchmark": "arc", "id": "a", "test_output": [[1, 2]]}
    assert score.is_correct(arc, [[1, 2]]) and score.is_correct(arc, "[[1, 2]]")
    assert not score.is_correct(arc, [[2, 1]]) and not score.is_correct(arc, None)
    bt = {"benchmark": "bt", "id": "b", "label": 2}
    assert score.is_correct(bt, "C") and score.is_correct(bt, "c. text") and not score.is_correct(bt, "A")
    assert score.cand_correct(bt, {"pred": "C"})
    same = score.paired_bootstrap([1, 0, 1], [1, 0, 1])
    assert same["mean_diff"] == 0 and same["ci_low"] == 0 and same["ci_high"] == 0
    up = score.paired_bootstrap([1] * 10, [0] * 10)
    assert up["mean_diff"] == 1 and up["ci_low"] == 1 and up["p_le0"] == 0
    cl = score.paired_bootstrap([1, 1, 0, 0], [0, 0, 0, 0], clusters=["g", "g", "h", "h"])
    assert cl["n_clusters"] == 2 and cl["mean_diff"] == 0.5
    assert score.paired_bootstrap([], [])["mean_diff"] is None


# ---------------------------------------------------------------- bench.py end to end
def _stub_think(spent: int):
    m = types.ModuleType("harness.think")

    def think(item, *, m, replicate, backend, batch, flags=None, params=None, arm="scaffold"):
        assert "label" not in item and "test_output" not in item
        return Answer(status="unverified", answer="A" if item["benchmark"] == "bt" else None,
                      verification_type="agreement", cand_id=None, spent_tokens=spent, rounds=1)
    m.think = think
    return m


def test_bench_end_to_end_bt(lab, monkeypatch):
    monkeypatch.setitem(sys.modules, "harness.think", _stub_think(spent=1000))
    rc = bench.main(["--benchmark", "bt", "--arm", "plain,bestofn_vote,seeded_bestofn,scaffold",
                     "--items", "6", "--replicates", "2", "--backend", "mock", "--m", "3",
                     "--batch", "e2e"])
    assert rc == 0
    out = config.RESULTS_DIR / "e2e"
    cost = read_jsonl(out / "cost.jsonl")
    assert len(cost) == 12 and set(cost[0]) == {"benchmark", "backend", "model", "item_id",
                                                 "replicate", "tokens"}
    b = read_json(out / "budget.json")["bt"]["mock"]
    assert b["B"] == round(3 * b["cot_median"])
    runs = read_jsonl(out / "runs.jsonl")
    assert {r["arm"] for r in runs} == {"plain", "bestofn_vote", "seeded_bestofn", "scaffold"}
    assert len(runs) == 4 * 12
    for r in runs:
        if r["arm"] in ("bestofn_vote", "seeded_bestofn"):
            assert r["budget_tokens"] == 1000 and r["spent_tokens"] <= 1000
    summ = read_json(out / "summary.json")["benchmarks"]["bt"]["arms"]
    assert summ["plain"]["solve_rate"] == 1.0 and summ["seeded_bestofn"]["coverage"] == 1.0
    assert summ["bestofn_vote"]["vs_plain"]["mean_diff"] == 0.0
    md = (out / "summary.md").read_text(encoding="utf-8")
    assert "seeded_bestofn" in md and "coverage" in md
    n_runs = len(runs)
    bench.main(["--benchmark", "bt", "--arm", "plain,bestofn_vote", "--items", "6",
                "--replicates", "2", "--backend", "mock", "--m", "3", "--batch", "e2e"])
    assert len(read_jsonl(out / "runs.jsonl")) == n_runs           # reused, not rerun
    _key_free(lab)


def test_bench_arc_without_scaffold_uses_B(lab):
    bench.main(["--benchmark", "arc", "--arm", "bestofn_verify", "--items", "2", "--backend",
                "mock", "--m", "2", "--batch", "arc1"])
    out = config.RESULTS_DIR / "arc1"
    B = read_json(out / "budget.json")["arc"]["mock"]["B"]
    rows = [r for r in read_jsonl(out / "runs.jsonl") if r["arm"] == "bestofn_verify"]
    assert rows and all(r["budget_tokens"] == B and r["spent_tokens"] <= B for r in rows)
    assert read_json(out / "summary.json")["benchmarks"]["arc"]["arms"]["bestofn_verify"]["solve_rate"] == 1.0
    _key_free(lab)


def test_key_fields_only_in_score_and_data():
    root = Path(harness.__file__).parent
    for f in [root / "bench.py", *sorted((root / "arms").glob("*.py"))]:
        src = f.read_text(encoding="utf-8")
        assert "test_output" not in src and '"label"' not in src and "'label'" not in src, f
