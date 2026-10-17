"""End-to-end smoke of the whole package on the mock backend (README "tests/" row).

Runs under the temporary lab root of conftest.py with synthetic items only (no D: data):
1. `think` CLI main on one ARC and one BT item, then graph --check / --render on the ARC run;
2. the same through real subprocesses (`python -m harness.think`, `python -m harness.graph`,
   `python -m harness.lint`), with the default mock replies;
3. `bench` main with plain + bestofn_verify + scaffold over two dev-tune items.
Asserts: run folders exist, ledger rows were appended, graph check ok, no key string in any
prompts/*.txt, best-of-N stops at the scaffold's realized spend.
"""
from __future__ import annotations

import importlib
import json
import os
import subprocess
import sys
from pathlib import Path

import pytest

from harness import bench, config, data, graph, llm
from harness.schemas import read_json, read_jsonl

_pkg = importlib.import_module("harness.think")
think = _pkg.load_driver() if hasattr(_pkg, "load_driver") else _pkg

FLIP = "def transform(grid):\n    return [row[::-1] for row in grid]\n"
KEY_GRID = [[9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9, 9, 9, 9]]    # sentinel no program predicts
DEFAULTS_REPLY = "\n".join(f"{i}. zqdflt-{w}" for i, w in enumerate(
    ["alpha", "beta", "gamma", "delta", "epsilon"], 1))
GEN_ROLES = ("generate", "transform", "program", "revise", "formal")
# Plain CoT replies are long in practice; the mock charges len(text) // 4, so a realistic length
# gives a cot_median (and B = m x cot_median) that leaves the scaffold room for its rounds.
REASONING = "\n".join(f"Step {i}: compare row {i % 3} of the input with the output and note the "
                      "cells that moved, then test the rule on the next example." for i in range(1, 41))
BATCH = "e2e-smoke"


# ---------------------------------------------------------------- synthetic items
def arc_items() -> list[dict]:
    out = []
    for n in range(2):
        train = [{"input": [[1 + n, 2, 3], [4, 5, 6 + n]], "output": [[3, 2, 1 + n], [6 + n, 5, 4]]},
                 {"input": [[7, 0, n], [0, 8, 2]], "output": [[n, 0, 7], [2, 8, 0]]}]
        out.append({"id": f"syn_arc_{n}", "benchmark": "arc", "family": "arc", "group": f"syn_arc_{n}",
                    "split": "dev-tune", "train": train,
                    "test_input": [[1, 0, 2, n], [3, 0, 4, 0]], "test_output": KEY_GRID})
    return out


def bt_items() -> list[dict]:
    out = []
    for n in range(2):
        out.append({"id": f"syn_bt_{n}", "benchmark": "bt", "family": "bt_sp", "group": f"syn_bt_{n}",
                    "split": "dev-tune",
                    "question": f"Puzzle {n}: a man shaves many times a day and still has a beard. How?",
                    "choices": ["He forgets.", "He shaves other people.", "He has two faces.",
                                "None of the above."], "label": 1})
    return out


def make_mock(benchmark: str):
    """Correct flip program on ARC (verified), option B on BT; defaults are marked zqdflt."""
    def fn(prompt: str, role: str, meta: dict) -> str:
        if role == "defaults":
            return DEFAULTS_REPLY
        if benchmark == "arc":
            block = f"```python\n{FLIP}```"
            if role == "plain":
                return REASONING + "\nThe rows are mirrored.\n" + block
            if role == "probe":
                return block
            if role in GEN_ROLES:
                return "1. " + block
        else:
            if role == "plain":
                return REASONING + "\nIt is wordplay.\nANSWER: B"
            if role == "probe":
                return "ANSWER: B"
            if role in GEN_ROLES:
                return "1. B"
        return llm._default_mock(prompt, role, meta)
    return fn


@pytest.fixture
def lab(_temp_lab_root, monkeypatch):
    """Synthetic item files in the temp DATA_DIR; real modules; mock cleared afterwards."""
    for b, items in (("arc", arc_items()), ("bt", bt_items())):
        p = data.item_path(b)
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text("".join(json.dumps(it) + "\n" for it in items), encoding="utf-8")
    data._CACHE.clear()
    monkeypatch.setattr(think, "_MODS", {})
    yield _temp_lab_root
    llm.set_mock(None)
    data._CACHE.clear()


# ---------------------------------------------------------------- helpers
def run_dir_of(batch: str, item: dict, arm: str = "scaffold", rep: int = 0) -> Path:
    return Path(config.RUNS_DIR) / think.make_run_id(batch, item["benchmark"], item["id"], arm, rep)


def ledger_rows(run_id: str) -> list[dict]:
    return [r for r in read_jsonl(Path(config.LEDGER_PATH)) if r.get("run_id") == run_id]


def key_needles(item: dict) -> list[str]:
    if item["benchmark"] == "arc":
        k = item["test_output"]
        return [json.dumps(k), json.dumps(k, separators=(",", ":")), " ".join(map(str, k[0])),
                "".join(map(str, k[0])), "test_output"]
    return ["label"]


def assert_no_key_in_prompts(run_dir: Path, item: dict) -> int:
    prompts = sorted((run_dir / "prompts").glob("*.txt"))
    assert prompts, f"no prompts under {run_dir}"
    for p in prompts:
        text = p.read_text(encoding="utf-8")
        for n in key_needles(item):
            assert n not in text, f"key string {n!r} in {p}"
        assert "zqdflt" not in text, f"private defaults leaked into {p}"
    return len(prompts)


def assert_think_run(run_dir: Path, item: dict) -> dict:
    for name in ("state.json", "answer.json", "problem.md", "clusters.jsonl", "graph.jsonl",
                 "private/defaults.json"):
        assert (run_dir / name).exists(), name
    ans = read_json(run_dir / "answer.json")
    rows = ledger_rows(run_dir.name)
    assert rows, "no ledger rows for the run"
    assert sum(r["tokens"]["total_tokens"] for r in rows) == ans["spent_tokens"]
    assert any(r["round_type"] == "first" for r in rows)
    chk = graph.check(run_dir)
    assert chk["ok"], chk
    assert_no_key_in_prompts(run_dir, item)
    return ans


def last_json(text: str) -> dict:
    """The last JSON object printed by a CLI (think prints one line, graph prints indented)."""
    text = text.strip()
    return json.loads(text[text.rindex("\n{") + 1:] if "\n{" in text else text)


# ---------------------------------------------------------------- 1. think CLI main + graph
def test_think_cli_arc_and_bt(lab, capsys):
    arc, bt = arc_items()[0], bt_items()[0]
    for item in (arc, bt):
        llm.set_mock(make_mock(item["benchmark"]))
        rc = think.main(["--benchmark", item["benchmark"], "--item", item["id"], "--m", "20",
                         "--replicate", "0", "--backend", "mock", "--batch", BATCH])
        assert rc == 0
        out = json.loads(capsys.readouterr().out.strip().splitlines()[-1])
        rd = run_dir_of(BATCH, item)
        assert Path(out["run_dir"]).resolve() == rd.resolve() and rd.is_dir()
        ans = assert_think_run(rd, item)
        assert ans["status"] == out["status"]
        if item["benchmark"] == "arc":
            assert ans["status"] == "solved", ans
        else:
            assert ans["status"] in ("unverified", "abstain"), ans
    rd = run_dir_of(BATCH, arc)
    assert graph.main(["--check", str(rd), "--render", str(rd)]) == 0
    capsys.readouterr()
    assert (rd / "graph.html").exists()
    rows = read_jsonl(Path(config.RESULTS_DIR) / BATCH / "runs.jsonl")
    assert {r["item_id"] for r in rows} == {arc["id"], bt["id"]}
    # a second run on the same (item, arm, replicate) refuses to overwrite without --force
    with pytest.raises(FileExistsError):
        think.think(arc, m=20, replicate=0, backend="mock", batch=BATCH)
    assert think.main(["--benchmark", "arc", "--item", arc["id"], "--backend", "mock",
                       "--batch", BATCH, "--force"]) == 0
    capsys.readouterr()


# ---------------------------------------------------------------- 2. the real entry points
def test_module_entry_points_in_subprocess(lab):
    env = {**os.environ, "HTSA_LAB_ROOT": str(lab), "HTSA_BACKEND": "mock",
           "PYTHONIOENCODING": "utf-8"}
    cwd = str(config.PROJECT_ROOT)
    bt = bt_items()[1]

    def run(*args):
        return subprocess.run([sys.executable, "-m", *args], cwd=cwd, env=env, text=True,
                              encoding="utf-8", capture_output=True, timeout=600)

    r = run("harness.think", "--benchmark", "bt", "--item", bt["id"], "--m", "20",
            "--replicate", "0", "--backend", "mock", "--batch", "e2e-cli")
    assert r.returncode == 0, r.stderr[-2000:]
    out = last_json(r.stdout)
    rd = Path(out["run_dir"])
    assert rd.is_dir() and lab.resolve() in rd.resolve().parents
    assert (rd / "answer.json").exists() and ledger_rows(rd.name)
    assert_no_key_in_prompts(rd, bt)
    r = run("harness.graph", "--check", str(rd), "--render", str(rd))
    assert r.returncode == 0, r.stdout + r.stderr[-2000:]
    assert (rd / "graph.html").exists()
    r = run("harness.lint")
    assert r.returncode == 0, r.stdout + r.stderr[-2000:]


# ---------------------------------------------------------------- 3. bench on three arms
def test_bench_three_arms(lab, capsys):
    llm.set_mock(make_mock("arc"))
    rc = bench.main(["--benchmark", "arc", "--arm", "plain", "--arm", "bestofn_verify",
                     "--arm", "scaffold", "--split", "dev-tune", "--items", "2",
                     "--replicates", "1", "--backend", "mock", "--m", "20", "--batch", BATCH])
    capsys.readouterr()
    assert rc == 0
    bdir = Path(config.RESULTS_DIR) / BATCH
    assert not (bdir / "errors.jsonl").exists(), read_jsonl(bdir / "errors.jsonl")
    md = (bdir / "summary.md").read_text(encoding="utf-8")
    for arm in ("plain", "bestofn_verify", "scaffold"):
        assert f"| {arm} |" in md, md
    assert (bdir / "summary.json").exists() and (bdir / "cost.jsonl").exists()
    budget = read_json(bdir / "budget.json")["arc"]["mock"]
    assert budget["cot_median"] and budget["B"] == round(20 * budget["cot_median"])

    rows = read_jsonl(bdir / "runs.jsonl")
    by = {(r["arm"], r["item_id"]): r for r in rows}
    items = {it["id"]: it for it in arc_items()}
    assert {a for a, _ in by} == {"plain", "bestofn_verify", "scaffold"}
    assert len(rows) == 6
    for (arm, item_id), r in by.items():
        rd = Path(config.RUNS_DIR) / r["run_id"]
        assert rd.is_dir() and (rd / "answer.json").exists(), r["run_id"]
        assert ledger_rows(r["run_id"]), f"no ledger rows for {r['run_id']}"
        assert_no_key_in_prompts(rd, items[item_id])
        if arm == "scaffold":
            chk = graph.check(rd)
            assert chk["ok"], chk
            assert r["status"] == "solved"
    # best-of-N stops at the scaffold's realized spend on the same item (MSR-02)
    for item_id in items:
        s, b = by[("scaffold", item_id)], by[("bestofn_verify", item_id)]
        assert b["budget_tokens"] == s["spent_tokens"]
        assert 1 <= b["n_calls"] <= 4 * 20
        # at most one call of overshoot (section 4 spend accounting): N >= 1 always runs
        assert b["n_calls"] == 1 or b["spent_tokens"] <= b["budget_tokens"], (b, s)
        assert b["status"] == "solved"
    for item_id in items:
        st = read_json(Path(config.RUNS_DIR) / by[("scaffold", item_id)]["run_id"] / "state.json")
        assert st["decisions"][-1]["step"] == "final"
        assert st["B"] == budget["B"]
