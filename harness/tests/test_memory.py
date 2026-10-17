"""Tests for the memory owner's modules: ledger, stats, graph, measure.pruning_regret.

No model calls are made; every path points into a temporary lab root."""
from __future__ import annotations

import json
import os
import tempfile
import threading
from pathlib import Path

os.environ.setdefault("HTSA_LAB_ROOT", tempfile.mkdtemp(prefix="htsa_lab_"))

import pytest  # noqa: E402

from harness import config, graph, ledger, stats  # noqa: E402
from harness.measure import pruning_regret  # noqa: E402
from harness.schemas import LedgerRow, Usage  # noqa: E402


@pytest.fixture
def lab(tmp_path, monkeypatch):
    """Repoint every lab path at a fresh temp dir."""
    monkeypatch.setattr(config, "LAB_ROOT", tmp_path)
    monkeypatch.setattr(config, "RUNS_DIR", tmp_path / "runs")
    monkeypatch.setattr(config, "MEMORY_DIR", tmp_path / "memory")
    monkeypatch.setattr(config, "VIEWS_DIR", tmp_path / "memory" / "views")
    monkeypatch.setattr(config, "LEDGER_PATH", tmp_path / "memory" / "ledger.jsonl")
    monkeypatch.setattr(config, "RESULTS_DIR", tmp_path / "results")
    for d in ("runs", "memory/views", "results"):
        (tmp_path / d).mkdir(parents=True, exist_ok=True)
    return tmp_path


def _jsonl(p: Path, rows: list[dict]) -> None:
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text("".join(json.dumps(r) + "\n" for r in rows), encoding="utf-8")


def cand(cid, card, rnd, pred, parents=(), lineage=None, operator="none", **kw) -> dict:
    d = {"id": cid, "text": "t", "card": card, "operator": operator, "seed": "", "perm": 0,
         "round": rnd, "call_id": f"call{rnd}", "origin": "probe" if card == "probe" else "spoken",
         "parent_ids": list(parents), "island_id": "main", "lineage_id": lineage or cid,
         "program": None, "pred": pred, "extra": {}}
    d.update(kw)
    return d


def make_run(root: Path, run_id: str, cands_by_file: dict, verify=(), judgments=(),
             clusters=(), state=None, answer=None) -> Path:
    rd = root / "runs" / run_id
    for name, rows in cands_by_file.items():
        _jsonl(rd / "cands" / f"{name}.jsonl", rows)
    _jsonl(rd / "verify.jsonl", list(verify))
    _jsonl(rd / "judgments.jsonl", list(judgments))
    _jsonl(rd / "clusters.jsonl", list(clusters))
    if state is not None:
        (rd / "state.json").write_text(json.dumps(state), encoding="utf-8")
    if answer is not None:
        (rd / "answer.json").write_text(json.dumps(answer), encoding="utf-8")
    return rd


def lrow(**kw) -> LedgerRow:
    base = dict(run_id="r", batch="b", benchmark="arc", item_id="i", split="train", family="arc",
                cls="arc", arm="scaffold", card="seeded", operator="none", round_type="first",
                round=0, seed="", perm=0, call_id="c", tokens=Usage(10, 5).to_dict())
    base.update(kw)
    return LedgerRow(**base)


# ---------------------------------------------------------------- ledger
def test_ledger_append_and_filter(lab):
    ledger.append(lrow(run_id="r1"))
    ledger.append({"run_id": "r2", "batch": "b", "split": "dev-tune", "card": "low_prior"})
    ledger.append({"run_id": "r3", "batch": "other", "split": "train"})
    all_rows = ledger.rows()
    assert len(all_rows) == 3 and all(r.get("ts") for r in all_rows)
    assert [r["run_id"] for r in ledger.rows(batch="b")] == ["r1", "r2"]
    assert [r["run_id"] for r in ledger.rows(split="train")] == ["r1", "r3"]
    assert [r["run_id"] for r in ledger.rows("b", card=["low_prior", "x"])] == ["r2"]


def test_ledger_is_append_only_and_thread_safe(lab):
    ledger.append(lrow(run_id="first"))
    before = config.LEDGER_PATH.read_text(encoding="utf-8")
    with pytest.raises(TypeError):
        ledger.append({"run_id": "bad", "obj": object()})
    assert config.LEDGER_PATH.read_text(encoding="utf-8") == before

    def worker(k):
        for i in range(50):
            ledger.append({"run_id": f"t{k}_{i}", "batch": "b"})

    ts = [threading.Thread(target=worker, args=(k,)) for k in range(8)]
    for t in ts:
        t.start()
    for t in ts:
        t.join()
    text = config.LEDGER_PATH.read_text(encoding="utf-8")
    assert text.startswith(before)
    lines = text.splitlines()
    assert len(lines) == 401 and all(json.loads(x) for x in lines)
    assert text.isascii()


# ---------------------------------------------------------------- stats
def test_stats_rebuild_train_only(lab):
    ledger.append(lrow(round_type="first", tokens={"total_tokens": 100}))
    ledger.append(lrow(round_type="first", tokens={"total_tokens": 300}, status="verified"))
    ledger.append(lrow(round_type="first", tokens={"total_tokens": 200}, status="fail"))
    ledger.append(lrow(card="revise", round_type="revise", status="verified"))
    ledger.append(lrow(split="dev-tune", status="verified"))          # excluded by default
    ledger.append(lrow(batch="other", status="verified"))             # other batch
    assert stats.load_views("b") is None and stats.load_views(None) is None
    p = stats.rebuild("b")
    assert p == config.VIEWS_DIR / "b" / "strategy_stats.json"
    v = stats.load_views("b")
    assert v["calibration"] is None and v["batch"] == "b"
    sv = v["strategy_stats"]
    assert sv["splits"] == ["train"] and sv["n_rows"] == 4
    c = stats.cell(v, "arc", "seeded", "first")
    assert {k: c[k] for k in ("pass", "fail", "n", "n_calls", "mean_tokens", "mean_verify_tokens",
                              "beta_a", "beta_b")} == {
        "pass": 1, "fail": 1, "n": 2, "n_calls": 1, "mean_tokens": 100.0,
        "mean_verify_tokens": 250.0, "beta_a": 2, "beta_b": 2}
    assert stats.cell(v, "arc", "revise", "revise")["pass"] == 1
    old_hash = sv["content_hash"]
    ledger.append(lrow(status="fail"))
    stats.rebuild("b")
    assert stats.load_views("b")["strategy_stats"]["content_hash"] != old_hash
    assert (config.VIEWS_DIR / "b" / "history" / f"strategy_stats.{old_hash[:12]}.json").exists()
    v2 = json.loads(stats.rebuild("b", splits=("train", "dev-tune")).read_text(encoding="utf-8"))
    assert v2["n_rows"] == 6


# ---------------------------------------------------------------- graph
def graph_run(lab: Path) -> Path:
    r0 = [cand("a1", "seeded", 0, [[1]]), cand("a2", "low_prior", 0, [[2]]),
          cand("a3", "transform", 0, [[1]], operator="drop"), cand("p1", "probe", 0, [[1]])]
    r1 = [cand("r1", "revise", 1, [[3]], parents=["a2"], lineage="a2", operator="fix")]
    r2 = [cand("r2", "revise", 2, [[1]], parents=["r1"], lineage="a2", operator="fix")]
    return make_run(
        lab, "g1", {"c0": r0, "c1": r1, "c2": r2},
        verify=[{"id": "a1", "status": "fail", "verification_type": "demo_match", "partial_score": 0.5},
                {"id": "a2", "status": "verified", "verification_type": "demo_match", "partial_score": 1.0},
                {"id": "r1", "status": "fail", "verification_type": "demo_match", "partial_score": 0.25}],
        judgments=[{"id": "a1", "p_raw": 0.4}],
        clusters=[{"cluster_id": "k1", "rule": "grid", "members": ["a1", "a3"],
                   "representative_id": "a1", "round": 0},
                  {"cluster_id": "k1", "rule": "grid", "members": ["r2"],
                   "representative_id": "a1", "round": 2}])


def test_graph_write_and_check(lab):
    rd = graph_run(lab)
    counts = graph.write(rd)
    assert counts["nodes"] == 6 and counts["clusters"] == 1
    g = [json.loads(x) for x in (rd / "graph.jsonl").read_text(encoding="utf-8").splitlines()]
    nodes = {r["cand_id"]: r for r in g if r["kind"] == "node"}
    assert nodes["a2"]["status"] == "verified" and nodes["a3"]["status"] == "unverified"
    assert nodes["r2"]["root_ids"] == ["a2"] and nodes["a3"]["cluster_id"] == "k1"
    assert nodes["a1"]["p_raw"] == 0.4 and nodes["a1"]["matches_default"] is False
    edges = {(r["src"], r["dst"], r["kind2"]) for r in g if r["kind"] == "edge"}
    assert ("a2", "r1", "parent_of") in edges and ("r1", "r2", "parent_of") in edges
    assert ("a1", "a3", "same_cluster") in edges and ("a1", "r2", "same_cluster") in edges
    cl = [r for r in g if r["kind"] == "cluster"][0]
    assert cl["n_members"] == 3
    assert cl["n_independent_roots"] == 3          # lineages a1, a3, a2
    assert cl["n_independent_nonseeded"] == 2      # a3 (transform), a2 (low_prior)
    res = graph.check(rd)
    assert res["ok"] and res["node_completeness"] == 100.0 and res["edge_completeness"] == 100.0
    assert res["n_drops"] == 3                     # a1, a3, r2; probe p1 not counted
    assert graph.main(["--check", str(rd)]) == 0


def test_graph_check_detects_gaps(lab):
    rd = graph_run(lab)
    graph.write(rd)
    rows = [json.loads(x) for x in (rd / "graph.jsonl").read_text(encoding="utf-8").splitlines()]
    kept = [r for r in rows if not (r["kind"] == "node" and r["cand_id"] == "a3")
            and not (r["kind"] == "edge" and r["dst"] == "r2" and r["kind2"] == "parent_of")]
    _jsonl(rd / "graph.jsonl", kept)
    res = graph.check(rd)
    assert not res["ok"]
    assert res["node_completeness"] == round(100 * 5 / 6, 2)
    assert res["edge_completeness"] == 50.0 and res["missing_edges"] == [["r1", "r2"]]
    # a dedup drop missing from clusters.jsonl is caught after a rewrite
    _jsonl(rd / "clusters.jsonl", [{"cluster_id": "k1", "rule": "grid", "members": ["a1", "a3"],
                                    "representative_id": "a1", "round": 0}])
    graph.write(rd)
    res = graph.check(rd)
    assert res["cluster_completeness"] < 100.0 and res["missing_drops"] == ["r2"]
    assert graph.main(["--check", str(rd)]) == 1


def test_graph_render_self_contained(lab):
    rd = graph_run(lab)
    p = graph.render(rd)
    html = p.read_text(encoding="utf-8")
    assert html.isascii() and "<script src" not in html and "<link" not in html
    assert "http://" not in html.replace("http://www.w3.org/2000/svg", "")
    assert '"cand_id": "r2"' in html and "partial score" in html


def test_memory_modules_never_read_keys():
    root = Path(graph.__file__).parent
    for name in ("ledger.py", "stats.py", "graph.py", "measure/pruning_regret.py"):
        src = (root / name).read_text(encoding="utf-8")
        assert "test_output" not in src and '"label"' not in src and "'label'" not in src


# ---------------------------------------------------------------- pruning regret
KEYS = {"i1": [[7]], "i2": [[7]], "i3": [[7]], "i4": [[7]]}


def fake_item(benchmark, item_id):
    return {"id": item_id, "benchmark": benchmark, "secret": KEYS[item_id]}


def fake_correct(item, c):
    return c.get("pred") == item["secret"]


def regret_batch(lab: Path) -> None:
    runs = []

    def add(item, rep, **kw):
        run_id = f"b1__arc__{item}__scaffold__r{rep}"
        make_run(lab, run_id, **kw)
        runs.append({"batch": "b1", "benchmark": "arc", "item_id": item, "arm": "scaffold",
                     "replicate": rep, "run_id": run_id, "status": kw["answer"]["status"],
                     "answer": kw["answer"]["answer"], "spent_tokens": 0, "rounds": 1})

    # i1 r0: correct x never verified, wrong y returned -> pruned, cause (a)
    add("i1", 0, cands_by_file={"c0": [cand("x", "low_prior", 0, [[7]]), cand("y", "seeded", 0, [[1]])]},
        verify=[{"id": "y", "status": "fail", "verification_type": "demo_match"}],
        answer={"status": "unverified", "answer": [[1]], "cand_id": "y"})
    # i1 r1: correct s solved, top conf after round 1 -> not a late winner
    add("i1", 1, cands_by_file={"c0": [cand("s", "seeded", 0, [[7]]), cand("t", "formal", 0, [[2]])]},
        verify=[{"id": "s", "status": "verified", "verification_type": "demo_match"}],
        state={"cycles": [{"round": 0, "pop": ["s"], "conf": {"s": 0.9, "t": 0.2}}]},
        answer={"status": "solved", "answer": [[7]], "cand_id": "s"})
    # i2: correct z verified-fail, in pop then evicted -> cause (b)
    add("i2", 0, cands_by_file={"c0": [cand("z", "transform", 0, [[7]]), cand("w", "seeded", 0, [[3]])],
                                "c1": [cand("z2", "revise", 1, [[4]], parents=["w"], lineage="w")]},
        verify=[{"id": "z", "status": "fail", "verification_type": "demo_match"}],
        state={"cycles": [{"round": 0, "pop": ["z", "w"]}, {"round": 1, "pop": ["w", "z2"]}]},
        answer={"status": "abstain", "answer": None, "cand_id": None})
    # i3: correct v verified-fail, never in pop, never a parent -> cause (c)
    add("i3", 0, cands_by_file={"c0": [cand("v", "transform", 0, [[7]]), cand("u", "seeded", 0, [[3]])]},
        verify=[{"id": "v", "status": "fail", "verification_type": "demo_match"}],
        state={"cycles": [{"round": 0, "pop": ["u"]}]},
        answer={"status": "unverified", "answer": [[3]], "cand_id": "u"})
    # i4 r0: no correct candidate at all
    add("i4", 0, cands_by_file={"c0": [cand("n1", "seeded", 0, [[5]])]},
        answer={"status": "unverified", "answer": [[5]], "cand_id": "n1"})
    # i4 r1: solved by a revise child of the low-conf lineage q2 -> late winner (conf via ledger)
    add("i4", 1, cands_by_file={"c0": [cand("q1", "seeded", 0, [[5]]), cand("q2", "formal", 0, [[6]])],
                                "c1": [cand("q3", "revise", 1, [[7]], parents=["q2"], lineage="q2")]},
        verify=[{"id": "q3", "status": "verified", "verification_type": "demo_match"}],
        answer={"status": "solved", "answer": [[7]], "cand_id": "q3"})
    rid = "b1__arc__i4__scaffold__r1"
    ledger.append(lrow(batch="b1", run_id=rid, cand_id="q1", agreement=0.9, round_type="verify"))
    ledger.append(lrow(batch="b1", run_id=rid, cand_id="q2", agreement=0.3, round_type="verify"))
    _jsonl(lab / "results" / "b1" / "runs.jsonl", runs)


def test_pruning_regret_arithmetic(lab):
    regret_batch(lab)
    rep = pruning_regret.compute("b1", item_loader=fake_item, correct_fn=fake_correct, n_boot=500)
    a = rep["per_benchmark"]["arc"]
    assert a["n_runs"] == 6 and a["n_items"] == 4
    assert a["coverage"]["rate"] == 0.875                       # (1 + 1 + 1 + 0.5) / 4
    assert a["correct_but_pruned"]["rate"] == 0.625             # (0.5 + 1 + 1 + 0) / 4
    assert a["primary"]["a"]["rate"] == 0.125
    assert a["primary"]["b"]["rate"] == 0.25
    assert a["primary"]["c"]["rate"] == 0.25
    assert a["primary"]["other"]["rate"] == 0.0
    assert a["primary_abc_sum"] == pytest.approx(a["correct_but_pruned"]["rate"])
    assert a["late_winner"]["rate"] == 0.5 and a["late_winner"]["n_items"] == 2
    lo, hi = a["correct_but_pruned"]["ci95"]
    assert 0.0 <= lo <= 0.625 <= hi <= 1.0
    # cause (b) only over runs with pop data: i1 r1 (0), i2 (1), i3 (0) -> items i1 0, i2 1, i3 0
    assert a["n_runs_with_pop"] == 3 and a["cause_b_evicted"]["rate"] == pytest.approx(1 / 3, abs=1e-4)
    by_run = {r["run_id"]: r for r in rep["runs"]}
    assert by_run["b1__arc__i2__scaffold__r0"]["never_verified"] is False
    assert by_run["b1__arc__i2__scaffold__r0"]["evicted"] is True
    assert by_run["b1__arc__i1__scaffold__r0"]["evicted"] is None
    out = lab / "results" / "b1" / "pruning_regret.json"
    assert json.loads(out.read_text(encoding="utf-8"))["per_benchmark"]["arc"]["primary_abc_sum"] == 0.625
