"""Fix pass 2026-10-17, section D (ARC adapter, graph, dedup): D1 dedup keeps a later passing program,
D2 one selection rule (test answer first, augmented outputs only on a tie), D3 scoring after the model
calls, D4 time limit per grid, D5 perturbation detail, D6 option regex, D8/D9 graph, D10 killpg, D11
plain rows. No model calls; programs run through the real sandboxed executor (tiny grids)."""
from __future__ import annotations

import importlib
import json
from pathlib import Path
from types import SimpleNamespace

import pytest

from harness import arc_exec, arc_think, config, graph, portfolio_arc
from harness.schemas import Candidate, VerifyResult
from harness.think import dedup

think = importlib.import_module("harness.think").load_driver()

TRAIN = [{"input": [[3, 4]], "output": [[4, 3]]}, {"input": [[5, 6, 7]], "output": [[7, 6, 5]]}]
TEST = [[1, 2]]
FLIP = "def transform(grid):\n    return [row[::-1] for row in grid]\n"
CONST = "def transform(grid):\n    return [[2, 1]]\n"          # fails the examples, same test grid as FLIP


def cand(cid, program=None, pred=None, text="", card="transform"):
    return Candidate(id=cid, text=text, card=card, operator="none", seed="", perm=0, round=0,
                     call_id="c-" + cid, program=program, pred=pred)


# ---------------------------------------------------------------- D1
def test_drop_keeps_a_later_passing_program_with_the_same_grid():
    a, b, c = cand("a", CONST, [[2, 1]]), cand("b", FLIP, [[2, 1]]), cand("c", CONST, [[2, 1]])
    calls = []

    def demo_of(x):
        calls.append(x.id)
        return x.program == FLIP
    kept, rows = dedup.drop([a, b, c], [], "arc", 0, demo_of=demo_of)
    assert [k.id for k in kept] == ["a", "b"]          # fail first, pass second: both go to verify
    assert rows[0]["members"] == ["a", "b", "c"] and rows[0]["dropped"] == ["c"]
    kept2, _ = dedup.drop([a, b], [], "arc", 0)        # without demo_of: the old exact rule
    assert [k.id for k in kept2] == ["a"]
    kept3, _ = dedup.drop([cand("d", FLIP, [[9]])], [], "arc", 0, demo_of=demo_of)
    assert [k.id for k in kept3] == ["d"]
    assert "d" not in calls                            # demo_of runs only on a grid collision


def test_think_dedup_fail_then_pass_is_not_dropped(tmp_path, monkeypatch):
    monkeypatch.setattr(think, "_MODS", {})
    ctx = SimpleNamespace(benchmark="arc", flags={"dedup": True}, run_dir=tmp_path,
                          P=SimpleNamespace(item={"train": TRAIN, "test_input": TEST}))
    st = SimpleNamespace(all_cands=[], round=0, vres={})
    first = cand("a", CONST)
    think._predict(ctx, [first])
    kept, _ = think._dedup(ctx, st, [first])
    st.all_cands.extend(kept)
    st.vres["a"] = VerifyResult(id="a", status="fail", verification_type="demo_match", attempts=1, partial_score=0.0)
    later = cand("b", FLIP)
    think._predict(ctx, [later])
    assert later.pred == first.pred == [[2, 1]]
    kept, _ = think._dedup(ctx, st, [later])
    assert [k.id for k in kept] == ["b"]                # the old rule dropped it unverified
    again = cand("c", FLIP + "\n")
    think._predict(ctx, [again])
    st.all_cands.extend(kept)
    kept, _ = think._dedup(ctx, st, [again])
    assert kept == []                                   # a passing program with this grid is already in


# ---------------------------------------------------------------- D2
def test_vote_groups_by_test_answer_before_augmented_behaviour():
    right = [{"pred": [[1]], "prog": "x" * 30, "aug": f"r{i}"} for i in range(3)]   # differ on augmented inputs
    wrong = [{"pred": [[2]], "prog": "x" * 10, "aug": "w"} for _ in range(2)]       # identical everywhere
    best, k, n = dedup.vote(wrong + right, lambda c: c["pred"], lambda c: len(c["prog"]), lambda c: c["aug"])
    assert best["pred"] == [[1]] and k == 3 and n == 2


def test_vote_uses_augmented_agreement_only_on_a_tie():
    a = [{"pred": [[1]], "prog": "x", "aug": None}, {"pred": [[1]], "prog": "x", "aug": "a"}]
    b = [{"pred": [[2]], "prog": "xxxx", "aug": "b"}, {"pred": [[2]], "prog": "xxxx", "aug": "b"}]
    best, k, _ = dedup.vote(a + b, lambda c: c["pred"], lambda c: len(c["prog"]), lambda c: c["aug"])
    assert best["pred"] == [[2]] and k == 2             # tie on size; b agrees on the rotations
    best, _, _ = dedup.vote(a + b, lambda c: c["pred"], lambda c: len(c["prog"]))
    assert best["pred"] == [[1]]                        # no augmented key: shortest program


def test_portfolio_and_think_select_by_the_same_rule(monkeypatch):
    cands = [{"kind": "divergent", "name": str(i), "prog": "w" * 5, "passed": 2, "total": 2, "pred": [[2]],
              "behaviour": "same"} for i in range(2)]
    cands += [{"kind": "plain", "name": str(i), "prog": "r" * 9, "passed": 2, "total": 2, "pred": [[1]],
               "behaviour": None if i == 0 else f"b{i}"} for i in range(3)]
    chosen, how, full = portfolio_arc.select(cands)
    assert chosen["pred"] == [[1]] and how == "vote 3 of 5 passing" and len(full) == 5
    monkeypatch.setattr(think, "_MODS", {})
    pool = [cand(f"w{i}", FLIP, [[2, 1]]) for i in range(2)] + [cand("r", CONST, [[5]])]
    st = SimpleNamespace(all_cands=pool, vres={c.id: SimpleNamespace(status="verified", verification_type="demo_match", partial_score=1.0, details={}) for c in pool})
    ctx = SimpleNamespace(benchmark="arc", probe=None, P=SimpleNamespace(item={"train": TRAIN, "test_input": TEST}))
    c, k, n = think._vote_verified(ctx, st)
    assert c.pred == [[2, 1]] and k == 2 and n == 2


# ---------------------------------------------------------------- D3
def _arc_item():
    return {"id": "t1", "benchmark": "arc", "split": "dev-tune", "train": TRAIN, "test_input": TEST,
            "test_output": [[2, 1]]}


def test_portfolio_solve_never_sees_the_key_and_score_uses_is_correct(tmp_path, monkeypatch):
    replies = iter([FLIP, FLIP])
    monkeypatch.setattr(portfolio_arc, "call", lambda prompt, args, tag, log_dir: (
        "```python\n" + next(replies) + "```", 10))
    args = SimpleNamespace(k_plain=2, k_div=0, k_revise=0, early_stop=True)
    item = _arc_item()
    with pytest.raises(AssertionError):
        portfolio_arc.solve(item, args, tmp_path)       # the full item is refused
    rec = portfolio_arc.solve(portfolio_arc.strip_key(item), args, tmp_path)
    assert "solved" not in rec and rec["answer"] == [[2, 1]] and rec["stopped_early"]
    row = portfolio_arc.score(item, rec)
    assert row["solved"] and row["any_right"] and all(a["right"] for a in row["attempts"])
    assert "pred" not in json.dumps(row["attempts"]) and "answer" not in row
    assert not portfolio_arc.score({**item, "test_output": [[9]]}, rec)["solved"]


def test_arc_think_scores_after_the_calls(tmp_path, monkeypatch):
    monkeypatch.setattr(arc_think.llm, "call", lambda prompt, **kw: SimpleNamespace(
        text="```python\n" + FLIP + "```", usage=SimpleNamespace(total_tokens=7)))
    args = SimpleNamespace(thinkers=2, backend="mock", effort="")
    item = _arc_item()
    with pytest.raises(AssertionError):
        arc_think.think(item, args, tmp_path)
    rec = arc_think.think(arc_think.strip_key(item), args, tmp_path)
    assert rec["answer"] == [[2, 1]] and rec["n_full_pass"] == 2
    row = arc_think.score(item, rec)
    assert row["solved"] and all(v["right"] for v in row["strategies"].values())


# ---------------------------------------------------------------- D4
SLOW_ON_SEVEN = ("import time\n"
                 "def transform(grid):\n"
                 "    if grid[0][0] == 7:\n"
                 "        t = time.process_time()\n"
                 "        while time.process_time() - t < 30:\n"
                 "            pass\n"
                 "    return [row[::-1] for row in grid]\n")


def test_time_limit_is_per_grid_and_later_inputs_are_skipped():
    res = arc_exec.execute(SLOW_ON_SEVEN, [[[1, 2]], [[7, 1]], [[3, 4]]], timeout_s=1)
    assert res["outputs"][0] == [[2, 1]] and res["outputs"][1:] == [None, None]
    assert res["timed_out"] and res["errors"][1].startswith("timeout") and res["errors"][2].startswith("timeout")
    assert res["duration_ms"] < 15000


def test_many_grids_each_under_the_limit_all_finish():
    busy = ("import time\n"
            "def transform(grid):\n"
            "    t = time.process_time()\n"
            "    while time.process_time() - t < 0.4:\n"
            "        pass\n"
            "    return grid\n")
    res = arc_exec.execute(busy, [[[i]] for i in range(5)], timeout_s=1)   # 2 s in all, 1 s per grid
    assert res["outputs"] == [[[i]] for i in range(5)] and not res["timed_out"]


def test_slow_only_on_augmented_inputs_keeps_the_test_prediction():
    t = [[1, 7]]
    clean = {"train": TRAIN, "test_input": t}
    # rot90 of [[1, 7]] starts with 1 (runs), the left-right mirror starts with 7 (times out)
    out = portfolio_arc.run_prog(arc_exec, SLOW_ON_SEVEN, clean)
    assert out["passed"] == 2 and out["pred"] == [[7, 1]] and out["behaviour"] is None


# ---------------------------------------------------------------- D5
def test_perturbation_detail_is_informational():
    d = arc_exec.perturbation_detail(FLIP, TRAIN)
    assert {"flip_h", "flip_v", "colour_perm"} <= set(d["consistent"]) and d["n_checked"] == 7
    d2 = arc_exec.perturbation_detail("def transform(grid):\n    return [[4, 3]]\n", TRAIN)
    assert "colour_perm" not in d2["consistent"] and "rot90" not in d2["consistent"]
    assert arc_exec.augmented([[1, 2]]) == [[[1], [2]], [[2, 1]], [[1, 2]], [[1], [2]]]
    assert arc_exec.aug_key([[[1]], None]) is None


# ---------------------------------------------------------------- D6
@pytest.mark.parametrize("text,key", [
    ("A key insight is that the man is bald.", None),
    ("A. because he is bald", "opt:A"),
    ("(c) the doctor is his mother", "opt:C"),
    ("Reasoning first.\nANSWER: B", "opt:B"),
    ("**D**", "opt:D"),
])
def test_option_key_does_not_read_the_word_a_as_option_a(text, key):
    k = dedup.dedup_key(cand("x", text=text), "bt")
    assert (k == key) if key else k.startswith("text:")


# ---------------------------------------------------------------- D8, D9
def _jsonl(p: Path, rows):
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text("".join(json.dumps(r) + "\n" for r in rows), encoding="utf-8")


def _row(cid, card, pred, parents=(), origin="spoken"):
    return {"id": cid, "card": card, "operator": "none", "round": 0, "pred": pred, "origin": origin,
            "parent_ids": list(parents), "lineage_id": cid, "text": "", "seed": "", "perm": 0, "call_id": cid}


def test_graph_probe_pooling_covers_edges_and_dangling_parents(tmp_path):
    rd = tmp_path / "run"
    _jsonl(rd / "cands" / "c0.jsonl", [_row("a1", "transform", [[1]]), _row("a2", "low_prior", [[1]])])
    _jsonl(rd / "cands" / "probe.jsonl", [_row("p1", "probe", [[1]], origin="probe"),
                                         _row("p2", "probe", [[5]], origin="probe")])
    _jsonl(rd / "clusters.jsonl", [{"cluster_id": "k1", "rule": "grid", "members": ["a1", "a2"],
                                    "representative_id": "a1", "round": 0, "dropped": ["a2"]}])
    _jsonl(rd / "verify.jsonl", [{"id": "a1", "status": "verified", "covers": ["c1", "c2"]}])
    graph.write(rd)
    g = [json.loads(x) for x in (rd / "graph.jsonl").read_text(encoding="utf-8").splitlines()]
    nodes = {r["cand_id"]: r for r in g if r["kind"] == "node"}
    assert nodes["p1"]["cluster_id"] == "k1" and nodes["p2"]["cluster_id"] is None
    cl = [r for r in g if r["kind"] == "cluster"][0]
    assert cl["n_independent_roots"] == 2 and cl["n_independent_roots_pooled"] == 3 and cl["probe_members"] == ["p1"]
    assert cl["n_independent_nonseeded"] == 2
    cov = {(r["src"], r["dst"]) for r in g if r["kind"] == "edge" and r["kind2"] == "covers_constraint"}
    assert cov == {("a1", "constraint:c1"), ("a1", "constraint:c2")}
    assert graph.check(rd)["ok"]
    # a dangling parent id: no edge, not a root, and the check fails
    _jsonl(rd / "cands" / "c1.jsonl", [_row("r1", "revise", [[3]], parents=["ghost"])])
    graph.write(rd)
    g = [json.loads(x) for x in (rd / "graph.jsonl").read_text(encoding="utf-8").splitlines()]
    assert not [r for r in g if r["kind"] == "edge" and r["src"] == "ghost"]
    assert {r["cand_id"]: r for r in g if r["kind"] == "node"}["r1"]["root_ids"] == ["r1"]
    res = graph.check(rd)
    assert not res["ok"] and res["n_dangling_parents"] == 1 and res["dangling_parents"] == [["ghost", "r1"]]
    assert res["edge_completeness"] == 100.0


# ---------------------------------------------------------------- D10
def test_posix_tree_kill_uses_the_session_pid(monkeypatch):
    seen = []
    fake_os = SimpleNamespace(name="posix", killpg=lambda pid, sig: seen.append(pid),
                              getpgid=lambda pid: (_ for _ in ()).throw(ProcessLookupError()))
    monkeypatch.setattr(arc_exec, "os", fake_os)        # the module's view only; pathlib keeps the real os
    import signal
    monkeypatch.setattr(signal, "SIGKILL", 9, raising=False)
    proc = SimpleNamespace(pid=4242, kill=lambda: None)
    arc_exec._kill_tree(proc)
    assert seen == [4242]


# ---------------------------------------------------------------- D11
def test_plain_rows_one_per_item_and_effort_defaults(tmp_path, monkeypatch):
    rows = [{"arm": "plain", "item_id": "t1", "replicate": 1, "answer": [[9]], "spent_tokens": 5},
            {"arm": "plain", "item_id": "t1", "replicate": 0, "answer": [[2, 1]], "spent_tokens": 3},
            {"arm": "plain", "item_id": "t1", "replicate": 2, "answer": [[9]], "spent_tokens": 5},
            {"arm": "best_of_n", "item_id": "t1", "replicate": 0, "answer": [[9]]}]
    _jsonl(tmp_path / "runs.jsonl", rows)
    pl = portfolio_arc.plain_rows(tmp_path, [_arc_item()])
    assert list(pl) == ["t1"] and pl["t1"]["replicate"] == 0
    assert portfolio_arc.plain_line(tmp_path, [_arc_item()]).startswith("| plain (one answer) | 1/1 |")
    src_p = Path(portfolio_arc.__file__).read_text(encoding="utf-8")
    src_t = Path(arc_think.__file__).read_text(encoding="utf-8")
    want = 'os.environ.get("HTSA_PLAIN_EFFORT", "")'
    assert want in src_p and want in src_t and '"medium"' not in src_p
    assert config.BENCHMARKS["arc"]["dedup_rule"] == "grid"
