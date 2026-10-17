"""Fix pass 2026-10-17, section B (bench harness and statistics). Mock backend only, temporary lab
root (the `lab` fixture of test_bench.py), no model calls."""
from __future__ import annotations

import argparse
import json
import re
import sys
import types
from pathlib import Path

import pytest

import harness
from harness import bench, config, data, llm, score
from harness.arms import best_of_n as bon
from harness.measure import pruning_regret
from harness.schemas import Answer, Usage, append_jsonl, read_json, read_jsonl
from harness.tests.test_bench import PROMPTS, _stub_think, default_mock, lab  # noqa: F401  (fixture)


def _bench(*argv):
    return bench.main(["--backend", "mock", "--m", "3", *argv])


def _raising_think(exc: Exception):
    m = types.ModuleType("harness.think")

    def think(item, **kw):
        raise exc
    m.think = think
    return m


# ---------------------------------------------------------------- B1 primary comparison, TOST
def _s(arm, item, correct, rep=0, spent=100, budget=None, error=False, group=None):
    return {"run_id": f"b__bt__{item}__{arm}__r{rep}", "arm": arm, "item_id": item, "replicate": rep,
            "group": group or item, "correct": correct, "error": error, "spent_tokens": spent,
            "budget_tokens": budget}


def test_paired_bootstrap_reports_the_90_interval():
    d = score.paired_bootstrap([1, 0, 1, 1, 0, 1], [0, 0, 1, 0, 0, 1])
    assert d["ci_low"] <= d["ci90_low"] <= d["mean_diff"] <= d["ci90_high"] <= d["ci_high"]


def test_primary_null_gate_and_tost():
    items = [f"i{k}" for k in range(40)]
    scored = []
    for k, i in enumerate(items):
        scored.append(_s("scaffold", i, True, spent=500))
        scored.append(_s("bestofn_verify", i, k % 2 == 0, budget=500))
        scored.append(_s("seeded_bestofn", i, k % 4 == 0, budget=500))
    arms = {a: {"solve_rate": float(sum(s["correct"] for s in scored if s["arm"] == a)) / 40}
            for a in ("scaffold", "bestofn_verify", "seeded_bestofn")}
    p = score.primary_comparison(scored, arms, {i: i for i in items}, "bt")
    assert p["null"]["arm"] == "bestofn_verify" and "not preregistered" in p["null"]["source"]
    assert p["gate_pass"] is True and p["equivalent"] is False and p["n_both"] == 40
    # equal arms: equivalent within 3 points, gate fails
    same = [_s("scaffold", i, k % 2 == 0, spent=500) for k, i in enumerate(items)] + \
           [_s("bestofn_verify", i, k % 2 == 0, budget=500) for k, i in enumerate(items)]
    p2 = score.primary_comparison(same, {"scaffold": {"solve_rate": .5}, "bestofn_verify": {"solve_rate": .5}},
                                  {i: i for i in items}, "bt")
    assert p2["gate_pass"] is False and p2["equivalent"] is True
    md = "\n".join(score._primary_md(p2))
    assert "Primary null: bestofn_verify" in md and "Superiority gate" in md and "TOST" in md


def test_primary_comparison_drops_unmatched_null_runs():
    scored = [_s("scaffold", "a", True, spent=500), _s("bestofn_verify", "a", False, budget=500),
              _s("scaffold", "b", True, spent=700), _s("bestofn_verify", "b", True, budget=900)]
    p = score.primary_comparison(scored, {"scaffold": {"solve_rate": 1}, "bestofn_verify": {"solve_rate": .5}},
                                 {"a": "a", "b": "b"}, "bt")
    assert p["n_null_unmatched"] == 1 and p["n_both"] == 1 and p["n_a_only"] == 1


def test_null_from_dev_batch(lab):
    from harness.schemas import write_json
    write_json(config.RESULTS_DIR / "dev" / "summary.json",
               {"benchmarks": {"bt": {"arms": {"bestofn_verify": {"solve_rate": .4},
                                               "seeded_bestofn": {"solve_rate": .6}}}}})
    nl = score.choose_null({"bestofn_verify": {"solve_rate": .9}, "seeded_bestofn": {"solve_rate": .1}}, "bt", "dev")
    assert nl["arm"] == "seeded_bestofn" and "dev" in nl["source"]


# ---------------------------------------------------------------- B2 keep/drop, headroom, judge validation
def test_p_helps_beta_binomial():
    assert score.p_helps(0, 0) == pytest.approx(0.5)
    assert score.p_helps(5, 0) == pytest.approx(1 - 0.5 ** 6)        # Beta(6, 1): 1 - 0.5^6
    assert score.p_helps(3, 3) == pytest.approx(0.5)
    kd = score.keep_drop({"a": 1, "b": 1, "c": 0, "d": 1}, {"a": 0, "b": 0, "c": 0, "d": 1})
    assert (kd["helps"], kd["hurts"], kd["ties"]) == (2, 0, 2) and kd["keep"] is False
    pooled = score.keep_drop_pooled([kd, kd, kd])
    assert pooled["helps"] == 6 and pooled["keep"] is True


def test_ablation_arms_get_keep_drop():
    scored = [_s("scaffold", f"i{k}", True) for k in range(6)] + \
             [_s("scaffold-minus-revise", f"i{k}", False) for k in range(6)]
    out = score.ablations(scored, {})
    r = out["scaffold-minus-revise"]
    assert r["flag"] == "revise" and r["helps"] == 6 and r["keep"] is True
    assert "keep" in "\n".join(score._keep_drop_md(out))


def test_headroom_filter_says_when_not_applied():
    one = [_s("plain", "a", True), _s("plain", "b", False)]
    h = score.headroom_filter(one)
    assert h["applied"] is False and h["reason"] == "headroom filter not applied, replicates=1"
    assert "replicates=1" in "\n".join(score._headroom_md(h))
    three = [_s("plain", i, c, rep=r) for i, cs in (("a", (1, 1, 1)), ("b", (1, 0, 0)), ("c", (0, 0, 0)))
             for r, c in enumerate(cs)]
    h = score.headroom_filter(three)
    assert h["applied"] and h["keep"] == ["b"] and h["ceiling"] == ["a"] and h["floor"] == ["c"]


def test_judge_validation_metrics(lab):
    item = data.load_items("bt", "dev-tune")[0]
    rid = "jv__bt__" + item["id"] + "__scaffold__r0"
    rd = config.RUNS_DIR / rid
    (rd / "cands").mkdir(parents=True)
    right = "ABCD"[int(item["label"])]
    wrong = "ABCD"[(int(item["label"]) + 1) % 4]
    append_jsonl(rd / "cands" / "c.jsonl", [{"id": "k1", "pred": right}, {"id": "k2", "pred": wrong}])
    append_jsonl(rd / "judgments.jsonl", [{"id": "k1", "p_raw": 0.9}, {"id": "k2", "p_raw": 0.2}])
    s = {"run_id": rid, "item_id": item["id"], "split": "dev-tune", "group": item["group"], "error": False}
    j = score.judge_validation([s], {item["id"]: item}, n_boot=50)
    assert j["n_judged"] == 2 and j["auroc"] == 1.0 and j["selection"] == 1.0 and j["random_pick"] == 0.5
    assert j["brier"] == pytest.approx((0.1 ** 2 + 0.2 ** 2) / 2)
    assert score.judge_validation([], {})["n_judged"] == 0
    assert score.adaptive_ece([0.5, 0.5], [1, 0], n_bins=1) == 0.0
    assert score.adaptive_ece([0.5, 0.5], [1, 0]) == 0.5                # one item per bin


# ---------------------------------------------------------------- B3 crash rows; B15 SKIP path
def test_crash_inside_run_one_writes_an_error_row(lab, monkeypatch):
    monkeypatch.setitem(sys.modules, "harness.think", _raising_think(AttributeError("no attribute think")))
    _bench("--benchmark", "bt", "--arm", "scaffold,bestofn_vote", "--items", "3", "--batch", "crash")
    out = config.RESULTS_DIR / "crash"
    rows = [r for r in read_jsonl(out / "runs.jsonl") if r["arm"] == "scaffold"]
    assert len(rows) == 3 and all(r["status"] == "error" and r["crash"] for r in rows)
    assert not [r for r in read_jsonl(out / "runs.jsonl") if r["arm"] == "bestofn_vote"]   # SKIP: no row
    skips = [e for e in read_jsonl(out / "errors.jsonl") if "skipped:" in e["error"]]
    assert len(skips) == 3
    summ = read_json(out / "summary.json")["benchmarks"]["bt"]
    assert summ["arms"]["scaffold"]["n_items"] == 3 and summ["arms"]["scaffold"]["solve_rate"] == 0.0
    assert summ["arms"]["scaffold"]["n_crash"] == 3
    # a retry with a working think replaces the crash rows; best-of-N then runs at the scaffold spend
    monkeypatch.setitem(sys.modules, "harness.think", _stub_think(spent=800))
    _bench("--benchmark", "bt", "--arm", "scaffold,bestofn_vote", "--items", "3", "--batch", "crash")
    last = {r["run_id"]: r for r in read_jsonl(out / "runs.jsonl")}
    assert {r["status"] for r in last.values() if r["arm"] == "scaffold"} == {"unverified"}
    assert all(r["budget_tokens"] == 800 for r in last.values() if r["arm"] == "bestofn_vote")


def test_legacy_crash_only_in_errors_log_counts_wrong(lab):
    out = config.RESULTS_DIR / "old"
    item = data.load_items("bt", "dev-tune")[0]
    other = data.load_items("bt", "dev-tune")[1]
    append_jsonl(out / "runs.jsonl", {"batch": "old", "benchmark": "bt", "item_id": item["id"], "arm": "scaffold",
                                      "replicate": 0, "run_id": f"old__bt__{item['id']}__scaffold__r0",
                                      "status": "solved", "answer": "ABCD"[int(item["label"])], "spent_tokens": 10})
    append_jsonl(out / "errors.jsonl", [
        {"run_id": f"old__bt__{other['id']}__scaffold__r0", "error": "AttributeError: no think"},
        {"run_id": f"old__bt__{other['id']}__bestofn_vote__r0", "error": "RuntimeError: skipped: no scaffold"}])
    summ = score.score_batch("old")["benchmarks"]["bt"]["arms"]
    assert set(summ) == {"scaffold"}
    assert summ["scaffold"]["n_items"] == 2 and summ["scaffold"]["solve_rate"] == 0.5
    assert "1 crashed runs" in (out / "summary.md").read_text(encoding="utf-8")


# ---------------------------------------------------------------- B4 reuse after the budget check; B15 extension
def test_extension_with_scaffold_reruns_best_of_n_at_the_new_budget(lab, monkeypatch):
    _bench("--benchmark", "bt", "--arm", "bestofn_vote", "--items", "2", "--batch", "ext")
    out = config.RESULTS_DIR / "ext"
    B = read_json(out / "budget.json")["bt"]["mock"]["B"]
    first = [r for r in read_jsonl(out / "runs.jsonl") if r["arm"] == "bestofn_vote"]
    assert first and all(r["budget_tokens"] == B for r in first)
    monkeypatch.setitem(sys.modules, "harness.think", _stub_think(spent=B // 2))
    _bench("--benchmark", "bt", "--arm", "scaffold,bestofn_vote", "--items", "2", "--batch", "ext")
    last = {r["run_id"]: r for r in read_jsonl(out / "runs.jsonl")}
    bon_rows = [r for r in last.values() if r["arm"] == "bestofn_vote"]
    assert bon_rows and all(r["budget_tokens"] == B // 2 for r in bon_rows)
    n = len(read_jsonl(out / "runs.jsonl"))
    _bench("--benchmark", "bt", "--arm", "bestofn_vote", "--items", "2", "--batch", "ext")   # same budget: reused
    assert len(read_jsonl(out / "runs.jsonl")) == n


def test_skip_is_not_covered_by_an_old_run(lab, monkeypatch):
    monkeypatch.setitem(sys.modules, "harness.think", _stub_think(spent=500))
    _bench("--benchmark", "bt", "--arm", "scaffold,bestofn_vote", "--items", "1", "--batch", "sk")
    out = config.RESULTS_DIR / "sk"
    item = data.load_items("bt", "dev-tune")[0]
    rid = f"sk__bt__{item['id']}__bestofn_vote__r0"
    done = bench.existing_runs("sk")
    assert rid in done
    got = bench.run_one("bestofn_vote", item, m=3, replicate=0, backend="mock", batch="sk",
                        budget=bench.SKIP, done=done)
    assert got is None and "skipped:" in read_jsonl(out / "errors.jsonl")[-1]["error"]


# ---------------------------------------------------------------- B9 plain failures that spent tokens; B12 cost
def test_plain_failure_with_tokens_is_final_and_in_the_median(lab):
    def mock(prompt, role, meta):
        if meta.get("item_id", "").endswith("_CR"):
            raise llm.CallError("API Error: Claude's response exceeded the 8000 output token maximum",
                                usage=Usage(1000, 8000))
        return default_mock(prompt, role, meta)
    llm.set_mock(mock)
    _bench("--benchmark", "bt", "--arm", "plain", "--items", "6", "--batch", "cap")
    out = config.RESULTS_DIR / "cap"
    runs = read_jsonl(out / "runs.jsonl")
    failed = [r for r in runs if r["status"] == "error"]
    assert failed and all(r["spent_tokens"] > 0 for r in failed)
    cost = read_jsonl(out / "cost.jsonl")
    assert len(cost) == 6 and any(r["tokens"] >= 9000 for r in cost)
    b = read_json(out / "budget.json")["bt"]["mock"]
    assert b["n"] == 6 and b["n_failed"] == len(failed)
    assert read_json(out / "summary.json")["benchmarks"]["bt"]["arms"]["plain"]["n_failed_spent"] == len(failed)
    n = len(runs)
    _bench("--benchmark", "bt", "--arm", "plain", "--items", "6", "--batch", "cap")   # not retried
    assert len(read_jsonl(out / "runs.jsonl")) == n


def test_cost_median_not_pooled_across_splits_and_min_b_recorded(lab, monkeypatch):
    monkeypatch.setenv("HTSA_MIN_B", "999999")
    _bench("--benchmark", "bt", "--arm", "plain", "--items", "3", "--batch", "sp")
    _bench("--benchmark", "bt", "--arm", "plain", "--items", "2", "--split", "test", "--batch", "sp")
    b = read_json(config.RESULTS_DIR / "sp" / "budget.json")["bt"]["mock"]
    assert b["n"] == 2 and b["split"] == "test"
    assert b["min_B"] == 999999 and b["B"] == 999999 and b["B_unfloored"] < 999999


def test_fixed_b(lab, monkeypatch):
    monkeypatch.setenv("HTSA_FIXED_B", "5000")
    _bench("--benchmark", "bt", "--arm", "bestofn_vote", "--items", "2", "--batch", "fx")
    out = config.RESULTS_DIR / "fx"
    rows = read_jsonl(out / "runs.jsonl")
    assert {r["arm"] for r in rows} == {"bestofn_vote"}
    assert all(r["budget_tokens"] == 5000 and r["spent_tokens"] <= 5000 for r in rows)
    b = read_json(out / "budget.json")["bt"]["mock"]
    assert b["B"] == 5000 and b["source"] == "HTSA_FIXED_B"
    assert not (out / "cost.jsonl").exists()


def test_item_ids_from_another_split_warn(lab, capsys):
    test_id = data.load_items("bt", "test")[0]["id"]
    args = bench.parse_args(["--benchmark", "bt", "--item-ids", test_id, "--batch", "w", "--backend", "mock"])
    got = bench.choose_items(args)
    assert [it["id"] for it in got] == [test_id]
    assert "not in split dev-tune" in capsys.readouterr().err


# ---------------------------------------------------------------- B8 spawning rule (plan.md s2)
def test_next_batch_size_follows_the_plan():
    assert bon.next_batch_size(0, 0, 1000, 80) == 1
    assert bon.next_batch_size(100, 1, 1000, 80) == 6          # fit 9, reserve one, cap 6
    assert bon.next_batch_size(100, 1, 350, 80) == 1           # fit 2: one launched, one in reserve
    assert bon.next_batch_size(200, 2, 300, 80) == 1           # fit 1: the last call alone
    assert bon.next_batch_size(100, 1, 199, 80) == 0           # spend + mean > budget: stop
    assert bon.next_batch_size(100, 1, 1000, 3) == 2           # N cap


def test_spawn_overshoot_at_most_one_call(lab):
    item = data.load_items("bt")[0]
    one = bon.run_arm("bestofn_vote", item, m=20, replicate=0, backend="mock", batch="ov",
                      budget_tokens=10 ** 9).spent_tokens   # just to size; capped by 4 x m
    per = one // 80
    ans = bon.run_arm("bestofn_vote", item, m=20, replicate=1, backend="mock", batch="ov",
                      budget_tokens=int(7.5 * per))
    assert ans.spent_tokens <= 7.5 * per and ans.spent_tokens >= 6.5 * per


# ---------------------------------------------------------------- B10 counts on unequal n
def test_vs_plain_on_intersection_with_counts():
    a = {"x": 1.0, "y": 0.0, "z": 1.0}
    b = {"x": 0.0, "y": 0.0}
    d = score.paired_items(a, b, {})
    assert d["n_both"] == 2 and d["n_a_only"] == 1 and d["n_b_only"] == 0 and d["mean_diff"] == 0.5


# ---------------------------------------------------------------- B5 portfolio_v2 independent baseline
def _v2_item():
    g = [[1, 2], [3, 4]]
    return {"id": "p1", "benchmark": "arc", "train": [{"input": g, "output": g}] * 2, "test_input": g,
            "test_output": [[9]], "split": "fresh"}


def test_portfolio_v2_baseline_draws_its_own_samples(lab, monkeypatch, tmp_path):
    from harness import portfolio_v2 as v2
    calls = []

    def fake_call(prompt, args, tag, log_dir):
        calls.append(tag)
        return "```python\ndef transform(grid):\n    return [[9]]\n```", 100
    monkeypatch.setattr(v2, "call", fake_call)
    monkeypatch.setattr(v2, "run_prog", lambda ex, prog, clean: {"passed": 2, "total": 2, "diffs": [],
                                                                 "pred": [[9]], "sym": 0})
    ns = argparse.Namespace(k_plain=4, early_stop=True, k_div=2, k_revise=2, anchored=True, k_base_max=10,
                            reuse_method_plain=False)
    r = v2.solve(_v2_item(), ns, tmp_path)
    assert r["stopped_early"] and r["n_base_reused"] == 0 and r["identical_arms"] is False
    assert r["n_base"] == 2 and r["base_tokens"] == r["method_tokens"] == 200
    assert sum(t.startswith("plainextra") for t in calls) == 2
    ns.reuse_method_plain = True
    old = v2.solve(_v2_item(), ns, tmp_path)
    assert old["identical_arms"] is True and old["base_mode"] == "reuse"
    legacy = {k: v for k, v in old.items() if k not in ("identical_arms", "base_mode", "n_base_reused")}
    assert v2.identical_arms(legacy) is True
    text = v2.summary([r, legacy], Path("x.jsonl"))
    assert "stopped early (two agreeing plain attempts) on 2 of 2" in text and "identical attempts on 1 of 2" in text


# ---------------------------------------------------------------- B6, B11 NoveltyBench
def test_noveltybench_unparsed_partition_is_unscored(lab, monkeypatch, tmp_path):
    nb = pytest.importorskip("harness.noveltybench")
    monkeypatch.setenv("HTSA_BACKEND", "mock")
    llm.set_mock(lambda prompt, role, meta: "These responses are all quite similar in spirit.")
    row = {"id": "q1", "prompt": "Name a colour.", "generations": [f"g{i}" for i in range(10)], "gen_tokens": 10}
    out = nb.judge_one(row, "opus", tmp_path)
    assert out["unscored"] is True and out["distinct"] is None and out["utility"] is None
    d1, d2 = tmp_path / "x-plain", tmp_path / "x-method"
    for d, rows in ((d1, [{"id": "q1", "distinct": 3, "utility": 4.0, "gen_tokens": 100},
                          {"id": "q2", "distinct": 2, "utility": 3.0, "gen_tokens": 100}]),
                    (d2, [out | {"gen_tokens": 130}, {"id": "q2", "distinct": 9, "utility": 5.0, "gen_tokens": 130}])):
        d.mkdir()
        (d / "scores.jsonl").write_text("\n".join(json.dumps(r) for r in rows) + "\n", encoding="utf-8")
    text = nb.summary([d1, d2], "x-method", n_boot=200)
    assert "| x-method | 1 | 1 |" in text                         # one scored, one unscored
    assert "NOT run at matched generation tokens" in text and "+30%" in text
    assert "temperature 1.0" in text
    assert re.search(r"\| x-plain \| 1 \|", text.split("minus each baseline")[1])   # paired on q2 only


# ---------------------------------------------------------------- B7 lite_bt --plain-from
def test_lite_bt_plain_from_does_not_rerun_plain(lab, tmp_path):
    from harness import lite_bt
    src = tmp_path / "prior"
    src.mkdir()
    (src / "runs.jsonl").write_text("\n".join(json.dumps(r) for r in [
        {"run_id": "p__bt__x__plain__r1", "arm": "plain", "item_id": "x", "replicate": 1, "answer": "C", "spent_tokens": 7},
        {"run_id": "p__bt__x__plain__r0", "arm": "plain", "item_id": "x", "replicate": 0, "answer": "B", "spent_tokens": 5},
        {"run_id": "p__bt__x__scaffold__r0", "arm": "scaffold", "item_id": "x", "replicate": 0, "answer": "A"}]) + "\n",
        encoding="utf-8")
    answers, tokens, ids = lite_bt.load_plain(src)
    assert ids == ["x"] and answers == {"x": "B"} and tokens == {"x": 5}
    tags = []
    llm.set_mock(lambda prompt, role, meta: (tags.append(meta.get("card")), "ANSWER: B")[1])
    args = argparse.Namespace(backend="mock", effort=None, vote=False, plain_answers=answers, plain_tokens=tokens)
    item = {"id": "x", "question": "q?", "choices": ["a", "b", "c", "d"], "label": 1}
    res = lite_bt.run_item(item, args, tmp_path / "out")
    assert res["plain"] == "B" and res["plain_reused"] and "plain" not in tags and len(tags) == 5


# ---------------------------------------------------------------- B14 pruning regret clusters
def test_pruning_regret_bootstrap_clusters_groups():
    ci = pruning_regret.bootstrap_ci([1, 1, 0, 0], n=500, clusters=["g", "g", "h", "h"])
    assert set(ci) <= {0.0, 0.5, 1.0}
    recs = [{"item_id": i, "group": g, "pruned": p} for i, g, p in (("a", "g", 1), ("b", "g", 1), ("c", "h", 0))]
    r = pruning_regret.item_rate(recs, lambda x: float(x["pruned"]), 200)
    assert r["n_items"] == 3 and r["n_clusters"] == 2


# ---------------------------------------------------------------- B13 who reads the keys
KEY_READERS = {"score.py", "data.py", "schemas.py", "config.py", "portfolio_arc.py", "portfolio_v2.py",
               "portfolio_offline.py", "arc_think.py", "lite_bt.py"}


def test_key_fields_only_in_the_listed_modules():
    root = Path(harness.__file__).parent
    readers = set()
    for f in root.rglob("*.py"):
        if "tests" in f.parts:
            continue
        src = f.read_text(encoding="utf-8")
        if "test_output" in src or '"label"' in src or "'label'" in src:
            readers.add(f.relative_to(root).as_posix())
    assert readers <= KEY_READERS, readers - KEY_READERS
    readme = (root / "README.md").read_text(encoding="utf-8")
    for name in KEY_READERS - {"schemas.py", "config.py"}:
        assert name in readme, name
