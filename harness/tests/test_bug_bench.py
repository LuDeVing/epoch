"""Bug pass 2026-10-17 (night), bench area: bench, score, arms, portfolio scripts, pruning regret, arc_exec.
Mock backend only, temporary lab root (the `lab` fixture of test_bench.py), no model calls."""
from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest

from harness import bench, config, llm, score
from harness.arms import best_of_n as bon
from harness.measure import pruning_regret
from harness.schemas import Usage, read_json, write_json
from harness.tests.test_bench import default_mock, lab  # noqa: F401  (fixture)


def _bench(*argv):
    return bench.main(["--backend", "mock", "--m", "3", *argv])


def _jsonl(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(json.dumps(r) for r in rows) + "\n", encoding="utf-8")


# ---------------------------------------------------------------- bench: budget needs a successful plain run
def _all_plain_fail_with_tokens(prompt, role, meta):
    if role == "plain" and meta.get("arm") == "plain":
        raise llm.CallError("API Error: output token maximum exceeded", usage=Usage(1000, 8000))
    return default_mock(prompt, role, meta)


def test_budget_from_without_this_backend_does_not_set_b_from_failures(lab):
    """--budget-from a batch that has no budget for this backend is no budget at all: with only failed plain
    runs the batch must stop, not derive B from the failures."""
    llm.set_mock(_all_plain_fail_with_tokens)
    with pytest.raises(SystemExit):
        _bench("--benchmark", "bt", "--arm", "plain", "--items", "2", "--batch", "bf", "--budget-from", "nothing")
    assert "bt" not in (read_json(config.RESULTS_DIR / "bf" / "budget.json", {}) or {})


def test_budget_from_a_fixed_b_batch_keeps_this_batch_median(lab, monkeypatch):
    """A --budget-from batch run under HTSA_FIXED_B records cot_median None; it must not wipe out this batch's
    own measured median."""
    write_json(config.RESULTS_DIR / "fixed" / "budget.json",
               {"bt": {"mock": {"B": 5000, "cot_median": None, "source": "HTSA_FIXED_B"}}})
    _bench("--benchmark", "bt", "--arm", "plain", "--items", "2", "--batch", "own", "--budget-from", "fixed")
    b = read_json(config.RESULTS_DIR / "own" / "budget.json")["bt"]["mock"]
    assert b["cot_median"] and b["source"] == "this batch" and b["B"] == round(3 * b["cot_median"])


# ---------------------------------------------------------------- best-of-N boundaries (regression locks)
def test_next_batch_size_boundaries():
    assert bon.next_batch_size(0, 0, None, 3) == 1
    assert bon.next_batch_size(10, 1, None, 3) == 2              # no budget: up to the cap
    assert bon.next_batch_size(0, 2, 1000, 8) == 6               # unit 0: no cost signal, workers cap
    assert bon.next_batch_size(300, 3, 10 ** 6, 3) == 0          # n_cap reached
    assert bon.next_batch_size(100, 1, 300, 80) == 1             # fit 2: one call, one kept in reserve
    assert bon.next_batch_size(500, 1, 300, 80) == 0             # over budget


# ---------------------------------------------------------------- score: gate and TOST edge cases (regression locks)
def _s(arm, item, correct, rep=0, spent=100, budget=None, error=False):
    return {"run_id": f"b__bt__{item}__{arm}__r{rep}", "arm": arm, "item_id": item, "replicate": rep,
            "group": item, "correct": correct, "error": error, "spent_tokens": spent, "budget_tokens": budget}


def test_primary_zero_discordant_and_replicates():
    items = [f"i{k}" for k in range(10)]
    scored = []
    for k, i in enumerate(items):
        for rep in (0, 1):
            scored.append(_s("scaffold", i, k % 2 == 0, rep=rep, spent=400 + rep))
            scored.append(_s("bestofn_verify", i, k % 2 == 0, rep=rep, budget=400 + rep))
    arms = {"scaffold": {"solve_rate": .5}, "bestofn_verify": {"solve_rate": .5}}
    p = score.primary_comparison(scored, arms, {i: i for i in items}, "bt")
    assert p["n_both"] == 10 and p["n_null_unmatched"] == 0 and p["mean_diff"] == 0.0
    assert p["gate_pass"] is False and p["equivalent"] is True
    # replicate 1 of the null matched to replicate 0's spend: unmatched, left out
    bad = [dict(s, budget_tokens=400) if s["arm"] == "bestofn_verify" and s["replicate"] == 1 else s for s in scored]
    assert score.primary_comparison(bad, arms, {i: i for i in items}, "bt")["n_null_unmatched"] == 10
    # one arm missing
    only = [s for s in scored if s["arm"] == "scaffold"]
    p2 = score.primary_comparison(only, {"scaffold": {"solve_rate": .5}}, {}, "bt")
    assert p2["null"]["arm"] is None and "no bestofn_verify" in p2["note"]
    assert "not computed" in "\n".join(score._primary_md(p2))


def test_keep_drop_without_discordant_items_drops():
    r = score.keep_drop({"a": 1.0, "b": 0.0}, {"a": 1.0, "b": 0.0})
    assert r["helps"] == r["hurts"] == 0 and r["p_helps"] == 0.5 and r["keep"] is False


# ---------------------------------------------------------------- portfolio_arc.plain_rows: last row per run wins
def test_plain_rows_take_the_retried_run_not_the_stale_error_row(tmp_path):
    from harness import portfolio_arc as PA
    rid = "p__arc__t1__plain__r0"
    _jsonl(tmp_path / "runs.jsonl", [
        {"run_id": rid, "arm": "plain", "item_id": "t1", "replicate": 0, "status": "error", "crash": True,
         "answer": None, "spent_tokens": 0},
        {"run_id": rid, "arm": "plain", "item_id": "t1", "replicate": 0, "status": "unverified",
         "answer": [[1]], "spent_tokens": 50}])
    rows = PA.plain_rows(tmp_path, [{"id": "t1"}])
    assert rows["t1"]["status"] == "unverified" and rows["t1"]["answer"] == [[1]]
    assert "1/1" in PA.plain_line(tmp_path, [{"id": "t1", "test_output": [[1]]}])


# ---------------------------------------------------------------- portfolio_offline: plain one answer = first plain attempt
def test_portfolio_offline_plain_one_answer_is_a_plain_attempt(tmp_path, monkeypatch, capsys):
    from harness import portfolio_offline as PO
    g = [[1, 2], [3, 4]]
    item = {"id": "t1", "train": [{"input": g, "output": g}], "test_input": g, "test_output": [[7]]}
    arc_file = tmp_path / "arc.jsonl"
    _jsonl(arc_file, [item])
    monkeypatch.setitem(config.BENCHMARKS, "arc", dict(config.BENCHMARKS["arc"], file=str(arc_file)))
    batch = tmp_path / "batch"
    _jsonl(batch / "portfolio_runs.jsonl", [{"id": "t1", "solved": False}])
    calls = batch / "calls" / "t1"
    calls.mkdir(parents=True)
    # the divergent attempt is right, the plain attempt is wrong; file names sort divergent first
    for name, out in (("divergent_rival_1", [[7]]), ("plain_0_2", [[0]])):
        (calls / f"{name}.json").write_text(json.dumps(
            {"text": f"```python\ndef transform(grid):\n    return {out}\n```"}), encoding="utf-8")

    def fake_execute(prog, inputs, timeout_s=None):
        out = [[7]] if "[[7]]" in prog else [[0]]
        return {"outputs": [g] + [out] + [None] * (len(inputs) - 2), "errors": [None] * len(inputs)}
    monkeypatch.setattr(PO.EX, "execute", fake_execute)
    monkeypatch.setattr(sys, "argv", ["portfolio_offline", str(batch)])
    PO.main()
    first = capsys.readouterr().out.splitlines()[0]
    assert "plain one answer 0" in first


# ---------------------------------------------------------------- pruning regret: one record per run id
def test_pruning_regret_counts_a_retried_run_once(lab):
    rows = [{"run_id": "pr__bt__x__scaffold__r0", "benchmark": "bt", "item_id": "x", "arm": "scaffold",
             "replicate": 0, "status": "error", "crash": True, "answer": None, "spent_tokens": 0},
            {"run_id": "pr__bt__x__scaffold__r0", "benchmark": "bt", "item_id": "x", "arm": "scaffold",
             "replicate": 0, "status": "solved", "answer": "A", "spent_tokens": 10}]
    _jsonl(config.RESULTS_DIR / "pr" / "runs.jsonl", rows)
    rep = pruning_regret.compute("pr", item_loader=lambda b, i: {"id": i, "group": i},
                                 correct_fn=lambda item, c: False, n_boot=50)
    assert rep["per_benchmark"]["bt"]["n_runs"] == 1 and len(rep["runs"]) == 1


# ---------------------------------------------------------------- arc_exec helpers (regression locks)
def test_augmented_and_aug_key_shapes():
    from harness import arc_exec as EX
    assert EX.augmented([[5]]) == [[[5]]] * 4
    rect = [[1, 2, 3], [4, 5, 6]]
    rot, fh, fv, tr = EX.augmented(rect)
    assert rot == [[4, 1], [5, 2], [6, 3]] and fh == [[3, 2, 1], [6, 5, 4]]
    assert fv == [[4, 5, 6], [1, 2, 3]] and tr == [[1, 4], [2, 5], [3, 6]]
    assert EX.aug_key([[[1]], None, [[1]], [[1]]]) is None
    assert EX.aug_key([[[1]]] * 4) == EX.aug_key([[[1]]] * 4)


def test_dedup_vote_ties():
    from harness.think import dedup as DD
    xs = [{"p": [[1]], "n": 5, "a": None}, {"p": [[2]], "n": 3, "a": "k"}, {"p": [[3]], "n": 1, "a": None}]
    best, k, n = DD.vote(xs, lambda x: x["p"], lambda x: x["n"], lambda x: x["a"])
    assert (best["p"], k, n) == ([[2]], 1, 3)                  # aug support breaks the size-1 tie
    best, _, _ = DD.vote(xs, lambda x: x["p"], lambda x: x["n"])
    assert best["p"] == [[3]]                                  # then the shortest program


# ---------------------------------------------------------------- lite_bt summary: empty arms print n/a
def test_lite_summary_vote_arm_with_no_vote_rows_prints_na():
    from harness import lite_bt as LB
    rows = [{"id": "a", "group": "g1", "key": "A", "plain": "A", "lite": "B", "plain_tokens": 10, "lite_tokens": 20},
            {"id": "b", "group": "g2", "key": "B", "plain": "B", "lite": "B", "plain_tokens": 10, "lite_tokens": 20}]
    text = "\n".join(LB.summary_lines(rows, ["plain", "lite", "vote"]))
    assert "| vote | n/a | n/a |" in text and "vote minus plain: n/a" in text and "lite minus vote: n/a" in text
    empty = "\n".join(LB.summary_lines([], ["plain", "lite"]))
    assert "| plain | n/a | n/a |" in empty and "lite minus plain: n/a" in empty


# ---------------------------------------------------------------- crash rows keep the usage a CallError carries
def _plain_raises_call_error(monkeypatch, arm_name):
    real = bench.run_arm

    def boom(arm, item, **kw):
        if arm != arm_name:
            return real(arm, item, **kw)
        raise llm.CallError("API Error: output token maximum exceeded", usage=Usage(1000, 8000))
    monkeypatch.setattr(bench, "run_arm", boom)


def test_bestofn_crash_row_carries_call_error_tokens(lab, monkeypatch):
    _plain_raises_call_error(monkeypatch, "bestofn_vote")
    _bench("--benchmark", "bt", "--arm", "bestofn_vote", "--items", "1", "--batch", "ce")
    rows = [json.loads(l) for l in (config.RESULTS_DIR / "ce" / "runs.jsonl").read_text(encoding="utf-8").splitlines()
            if '"bestofn_vote"' in l]
    assert rows and rows[-1]["crash"] and rows[-1]["spent_tokens"] == 9000


def test_plain_crash_with_call_error_tokens_enters_the_cost_median(lab, monkeypatch):
    _plain_raises_call_error(monkeypatch, "plain")
    with pytest.raises(SystemExit):     # only failures: no budget can be set, but the spend is recorded
        _bench("--benchmark", "bt", "--arm", "plain", "--items", "2", "--batch", "cp")
    rows = [json.loads(l) for l in (config.RESULTS_DIR / "cp" / "runs.jsonl").read_text(encoding="utf-8").splitlines()]
    assert len(rows) == 2 and all(r["spent_tokens"] == 9000 and bench.final_failure(r) for r in rows)
    cost = [json.loads(l) for l in (config.RESULTS_DIR / "cp" / "cost.jsonl").read_text(encoding="utf-8").splitlines()]
    assert sorted(c["tokens"] for c in cost) == [9000, 9000]


# ---------------------------------------------------------------- noveltybench: --rejudge-unscored, last row wins
def test_noveltybench_rejudge_unscored_replaces_the_row(tmp_path, monkeypatch):
    from harness import noveltybench as nb
    out = tmp_path / "x-plain"
    _jsonl(out / "generations.jsonl", [{"id": "p1", "gen_tokens": 5}, {"id": "p2", "gen_tokens": 5}])
    _jsonl(out / "scores.jsonl", [{"id": "p1", "gen_tokens": 5, "unscored": True, "distinct": None, "utility": None},
                                  {"id": "p2", "gen_tokens": 5, "distinct": 3, "utility": 2.0}])
    seen = []

    def fake_judge(row, judge_model, out, seed=0, log_name="judge_calls"):
        seen.append(row["id"])
        return {**row, "distinct": 7, "utility": 6.0}
    monkeypatch.setattr(nb, "judge_one", fake_judge)
    monkeypatch.setattr(sys, "argv", ["nb", "judge", "--out", str(out)])
    nb.main()
    assert seen == []                                           # default: unscored counts as done
    monkeypatch.setattr(sys, "argv", ["nb", "judge", "--out", str(out), "--rejudge-unscored"])
    nb.main()
    assert seen == ["p1"]
    got = {r["id"]: r for r in nb.load_scores(out / "scores.jsonl")}
    assert got["p1"]["distinct"] == 7 and not got["p1"].get("unscored") and got["p2"]["distinct"] == 3
    assert "| x-plain | 2 | 0 |" in nb.summary([out], n_boot=50)


# ---------------------------------------------------------------- arc_exec: the CPU timer limit is documented
def test_arc_exec_docstring_names_the_c_level_loop_limit():
    from harness import arc_exec as EX
    doc = " ".join(EX.__doc__.split())
    assert "C-level loop" in doc and "wall guard is the backstop" in doc
