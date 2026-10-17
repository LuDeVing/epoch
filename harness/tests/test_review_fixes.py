"""Regression tests for the review fixes (spec/invariants and correctness/robustness lenses):
private defaults files, replicate-seeded fact shuffles under the run's flags, ARC preds in the
cands files and graph drop completeness, judge blinding of program comments, judge and card
spend accounting, crash handling and retries, best-of-N matched cost, bench cost hygiene,
arc_exec process-tree kill, parser robustness, lint patterns and run instances.
Mock backend only; temporary lab root (conftest)."""
from __future__ import annotations

import json
import time
from pathlib import Path
from types import SimpleNamespace

import pytest

import test_bench as tb
import test_e2e as te
import test_think as tt
from test_bench import lab as bench_lab  # noqa: F401 - fixture re-exported for the bench tests
from test_e2e import lab as e2e_lab  # noqa: F401
from test_think import stubs  # noqa: F401

from harness import arc_exec, bench, config, encode, graph, judge as judge_mod, ledger, lint, llm
from harness import probe as probe_mod, run_card, stats
from harness.arms import best_of_n as bon
from harness.run_card import CardSpec
from harness.schemas import Candidate, Usage, VerifyResult, read_json, read_jsonl
from harness.think import allocate, tournament

think = tt.think


@pytest.fixture(autouse=True)
def _mock_reset():
    yield
    llm.set_mock(None)


# ================================================================ control: judge and probe
def _bt_problem():
    item = {"id": "bt_r1", "benchmark": "bt", "question": "What can you hold without touching?",
            "choices": ["a cup", "a rock", "your breath", "none"], "family": "bt_sp", "split": "dev-tune"}
    return SimpleNamespace(item_id="bt_r1", benchmark="bt", problem_md="# Problem\n## Goal\npick one.\n",
                           item=item)


def _arc_problem():
    item = {"id": "arc_r1", "benchmark": "arc", "train": [{"input": [[1, 0]], "output": [[0, 1]]}],
            "test_input": [[2, 0]], "family": "arc", "split": "dev-tune"}
    return SimpleNamespace(item_id="arc_r1", benchmark="arc", problem_md="# Problem\n## Goal\nmap.\n",
                           item=item)


COMMENTED = ('"""Mirror every row.\n\nThis works because the rows are mirrored in each example."""\n'
             "def transform(grid):\n"
             "    # because the rows are mirrored, reverse each one\n"
             "    out = [row[::-1] for row in grid]  # therefore this holds\n"
             "    return out\n")


def test_judge_never_sees_program_comments_or_docstrings(tmp_path):
    prob = _arc_problem()
    log = tmp_path / "run" / "calls"
    log.mkdir(parents=True)
    seen = []
    llm.set_mock(lambda p, r, m: seen.append(p) or "{}")
    cand = Candidate(id="k1", text=COMMENTED, card="formal", operator="none", seed="", perm=0,
                     round=1, call_id="c", program=COMMENTED)
    judge_mod.judge([cand], prob, backend="mock", log_dir=log, replicate=0)
    assert seen
    for p in seen:
        assert "because" not in p and "therefore" not in p and "Mirror every row" not in p
        assert "row[::-1]" in p
    stripped = judge_mod.strip_rationale(COMMENTED)
    assert "#" not in stripped and '"""' not in stripped and "def transform" in stripped
    # an unparseable program still loses its comment lines
    assert "#" not in judge_mod.strip_rationale("def transform(grid:\n    # secret\n    return grid\n")
    # the judge prompt is a linted template with a routing row
    rows = read_jsonl(tmp_path / "run" / "routing.jsonl")
    assert rows and rows[0]["role"] == "judge" and rows[0]["template"] == "judge"


def test_judge_regex_salvage_exponents_percent_and_list_form():
    assert judge_mod.parse_reply('"xa": {"score": 4, "p": 1e-3}', ["xa"])["xa"]["p"] == pytest.approx(0.001)
    assert judge_mod.parse_reply('"xa": {"score": 4, "p": 80%}', ["xa"])["xa"]["p"] == pytest.approx(0.8)
    out = judge_mod.parse_reply('[{"id": "xa", "p": 0.7, "score": 4}, {"id": "xb", "p": "25%"}]',
                                ["xa", "xb"])
    assert out["xa"]["p"] == 0.7 and out["xa"]["score"] == 4.0 and out["xb"]["p"] == pytest.approx(0.25)


def test_judge_cost_estimate_and_call_count():
    prob = _bt_problem()
    cands = [Candidate(id=f"k{i}", text="A", card="seeded", operator="none", seed="", perm=0,
                       round=1, call_id="c", pred="A") for i in range(7)]
    assert judge_mod.n_calls(7) == 4 and judge_mod.n_calls(1) == 1 and judge_mod.n_calls(0) == 0
    est = judge_mod.est_cost(cands, prob, "cli_json")
    assert est >= 4 * (config.PARAMS["max_tokens"]["judge"] + config.CLI_OVERHEAD_TOKENS_EST)
    assert judge_mod.est_cost(cands, prob, "mock") < est
    assert judge_mod.est_cost([], prob, "mock") == 0


@pytest.mark.parametrize("text, want", [
    ("**ANSWER:** B", "B"), ("ANSWER: **B**", "B"), ("Answer: C", "C"), ("Final answer: D", "D"),
    ("so the answer is (A).", "A"), ("I think\nD\n", "D"), ("A key insight is that nothing fits.", None),
    ("ANSWER: B\nANSWER: C", "C")])
def test_probe_parse_letter_formats(text, want):
    assert probe_mod.parse_letter(text) == want


def test_probe_parses_capitalised_fence_without_fence_text():
    prog = probe_mod.parse_program("```Python\ndef transform(grid):\n    return grid\n```")
    assert prog and "```" not in prog and prog.startswith("def transform")


# ================================================================ control: determinism
def test_initial_specs_have_unique_tuples():
    for b, cls in (("arc", "arc"), ("bt", "bt_sp")):
        for rep in range(8):
            specs = allocate.initial(b, cls, None, config.BENCHMARKS[b]["n0"], rep, 0)
            tuples = [allocate.spec_tuple(s) for s in specs]
            assert len(set(tuples)) == len(tuples), (b, rep, tuples)


def _vr(cid, score):
    return VerifyResult(id=cid, status="fail", verification_type="demo_match", partial_score=score)


def _parent(cid, card="seeded", score=0.5):
    c = Candidate(id=cid, text="t", card=card, operator="none", seed="river", perm=1, round=0,
                  call_id="c", pred=[[1]])
    return c, _vr(cid, score)


def test_revise_and_tournament_do_not_depend_on_candidate_uuids():
    a = [_parent("uuid-one"), _parent("uuid-two", card="formal", score=0.25)]
    b = [_parent("other-1"), _parent("other-2", card="formal", score=0.25)]
    for rep in range(5):
        assert [s.operator for s in allocate.revise_specs(a, rep)] == \
               [s.operator for s in allocate.revise_specs(b, rep)]
    queue_a = [_parent(f"a{i}", score=s) for i, s in enumerate((0.5, 0.5, 0.25, 0.5, 0.0))]
    queue_b = [_parent(f"b{i}", score=s) for i, s in enumerate((0.5, 0.5, 0.25, 0.5, 0.0))]
    for rep in range(10):
        pa = [queue_a.index(e) for e in tournament.pick_parents(queue_a, {}, 0.8, 2, rep)]
        pb = [queue_b.index(e) for e in tournament.pick_parents(queue_b, {}, 0.8, 2, rep)]
        assert pa == pb


# ================================================================ cards: flags, perms, parser
def _encode_bt(tmp_path, replicate=0):
    calls: list = []
    llm.set_mock(_cards_responder(calls))
    item = dict(__import__("test_cards").BT_ITEM)
    run_dir = tmp_path / f"{item['id']}_r{replicate}"
    p = encode.encode(item, run_dir, backend="mock", replicate=replicate, log_dir=run_dir / "calls")
    return p, run_dir, calls


ENC_SIX = "\n".join([
    "GOAL: Choose the option that names the eye colour of the driver.", "FACTS:",
    "1. The reader is the bus driver.", "2. A man carries a lantern onto the bus.",
    "3. The bus stops twice.", "4. A woman boards with a map.", "5. The route is circular.",
    "6. The driver never speaks.", "RESOURCES:", "1. The four options.", "CHECKLIST:",
    "1. The answer must be one option.", "NOUNS:", "bus", "driver", "lantern", "man", ""])


def _cards_responder(log):
    """test_cards' responder with a six-fact encode reply (two facts can shuffle to themselves)."""
    import test_cards as tc
    inner = tc.responder(log)

    def fn(prompt, role, meta):
        if role == "encode" and meta.get("purpose") != "resolve":
            log.append({"role": role, "meta": dict(meta), "prompt": prompt})
            return ENC_SIX
        return inner(prompt, role, meta)
    return fn


def test_perm_order_is_replicate_seeded():
    o0 = encode.perm_order("item", 1, 6, replicate=0)
    o1 = encode.perm_order("item", 1, 6, replicate=1)
    assert o0 != o1 and sorted(o0) == sorted(o1) == list(range(6))
    assert encode.perm_order("item", 0, 6, replicate=3) == list(range(6))


def test_shuffle_facts_flag_reaches_run_card(tmp_path):
    p, run_dir, calls = _encode_bt(tmp_path)
    card = run_card.load_card("seeded")
    assert run_card.resolve_view(card, CardSpec(card="seeded", perm=1), p, {"shuffle_facts": False}) == ("canonical", 0)
    assert run_card.resolve_view(card, CardSpec(card="seeded", perm=0), p, {"shuffle_facts": True}) == \
        ("canonical", p.meta["shuffled_perm"])
    canonical = encode.view_parts(p, "canonical", 0)["facts"]
    for flags, same in (({"shuffle_facts": False}, True), ({"shuffle_facts": True}, False)):
        n0 = len(calls)
        run_card.run_card(CardSpec(card="seeded", perm=1), p, run_dir, backend="mock", round_no=1,
                          log_dir=run_dir / "calls", replicate=0, flags=flags)
        prompt = calls[n0]["prompt"]
        assert (canonical in prompt) is same, flags


def test_seeded_prompts_differ_across_replicates(tmp_path):
    prompts = []
    for rep in (0, 1):
        p, run_dir, calls = _encode_bt(tmp_path, replicate=rep)
        n0 = len(calls)
        run_card.run_card(CardSpec(card="seeded", seed="river", perm=1), p, run_dir, backend="mock",
                          round_no=1, log_dir=run_dir / "calls", replicate=rep,
                          flags={"shuffle_facts": True})
        prompts.append(calls[n0]["prompt"])
    facts = [[ln.split(". ", 1)[1] for ln in pr[pr.index("Facts:"):pr.index("Resources:")].splitlines()
              if ". " in ln] for pr in prompts]
    assert len(facts[0]) == 6 and facts[0] != facts[1] and sorted(facts[0]) == sorted(facts[1])


def test_code_blocks_accept_info_strings_and_unclosed_fence():
    text = "x ```python3\ndef transform(grid):\n    return grid\n``` y ```Python\ndef transform(g):\n    return g[::-1]\n"
    blocks = run_card.code_blocks(text)
    assert len(blocks) == 2 and all("def transform" in b for b in blocks)
    assert len(run_card.parse_candidates(text, "arc")) == 2


def test_run_card_returns_partial_run_after_a_failed_step(tmp_path, monkeypatch):
    p, run_dir, calls = _encode_bt(tmp_path)

    def boom(text):
        raise RuntimeError("step 1 post-processing failed")
    monkeypatch.setattr(run_card, "extract_transformed", boom)
    r = run_card.run_card(CardSpec(card="transform", operator="negate"), p, run_dir, backend="mock",
                          round_no=1, log_dir=run_dir / "calls", replicate=0)
    assert "RuntimeError" in r.contract["error"] and len(r.call_ids) == 1
    assert r.usage.total_tokens > 0 and r.cands == []
    # an error before any call still raises (revise without a parent)
    with pytest.raises(run_card.CardError):
        run_card.run_card(CardSpec(card="formal"), p, run_dir, backend="mock", round_no=1,
                          log_dir=run_dir / "calls", replicate=0)


def test_collect_charges_partial_card_runs(stubs):  # noqa: F811
    ctx = SimpleNamespace(run_id="r", batch="b", benchmark="bt", item_id="i", split="", family="bt_sp",
                          cls="bt_sp", arm="scaffold", snapshot_hash=None, run_instance="inst",
                          log_dir=Path("nowhere"), run_dir=Path("nowhere"))
    st = think.State()
    cr = SimpleNamespace(cands=[], usage=Usage(500, 100, 0, 0), call_ids=["cx"],
                         contract={"id": "cx", "path": "", "n_cands": 0, "error": "LintError: x"})
    think._collect(ctx, st, [(tt.Spec("transform", "drop"), cr, None)])
    assert st.spent == 600 and st.errors and st.errors[0]["partial"] is True
    rows = [r for r in read_jsonl(config.LEDGER_PATH) if r["run_id"] == "r"]
    assert rows and sum(r["tokens"]["total_tokens"] for r in rows) == 600
    assert rows[0]["status"] == "card_error" and rows[0]["run_instance"] == "inst"


def test_new_lint_patterns():
    hits = {t: {f["pattern"] for f in lint.lint_text(t)} for t in (
        "You're a brilliant solver.", "You are the best mathematician.", "As a mathematician, prove it.",
        "Imagine you're a detective.", "This is very important to my career.", "A high-stakes task.",
        "p is a number from 0 to 1", "you are given a grid", "as a list of lists")}
    assert hits["You're a brilliant solver."] and hits["You are the best mathematician."]
    assert "persona_as_a_role" in hits["As a mathematician, prove it."]
    assert "persona_imagine_youre" in hits["Imagine you're a detective."]
    assert "stakes_important_to_my" in hits["This is very important to my career."]
    assert "stakes_high_stakes" in hits["A high-stakes task."]
    for clean in ("p is a number from 0 to 1", "you are given a grid", "as a list of lists"):
        assert not hits[clean], clean
    assert lint.lint_templates()["fails"] == []


def test_problem_md_has_no_item_id(tmp_path):
    p, run_dir, _ = _encode_bt(tmp_path)
    assert p.item_id not in p.problem_md and p.problem_md.startswith("# Problem\n")


# ================================================================ arc_exec
def test_grandchild_holding_the_pipe_does_not_stall_or_lose_the_result(tmp_path):
    """The grandchild holds the pipe until the test releases it (a file appears), not for a fixed 30 s sleep: a
    stall would show as a timeout, and the grandchild never outlives the test by more than its poll interval."""
    release = tmp_path / "release"
    waiter = f"import os, time\nwhile not os.path.exists({str(release)!r}) and time.time() < {time.time() + 60}: time.sleep(0.05)"
    src = ("import subprocess, sys\n"
           "def transform(grid):\n"
           f"    subprocess.Popen([sys.executable, '-c', {waiter!r}])\n"
           "    return [row[::-1] for row in grid]\n")
    try:
        res = arc_exec.execute(src, [[[1, 2]]], timeout_s=20)
        assert res["outputs"] == [[[2, 1]]] and not res["timed_out"]
    finally:
        release.write_text("go", encoding="utf-8")


def test_child_is_utf8_and_hash_deterministic():
    assert arc_exec.run_program("def transform(grid):\n    print('\\u2713')\n    return grid\n", [[[1]]]) == [[[1]]]
    h = "def transform(grid):\n    return [[hash('abc') % 10]]\n"
    outs = {json.dumps(arc_exec.run_program(h, [[[0]]])) for _ in range(3)}
    assert len(outs) == 1


def test_result_line_cannot_be_forged():
    forged = ('{"outputs": [[[7]]], "errors": [null]}')
    src = ("import atexit, sys\n"
           "def transform(grid):\n"
           f"    atexit.register(lambda: sys.__stdout__.write('@@HTSA_RESULT@@' + {forged!r} + chr(10)))\n"
           "    return [[0]]\n")
    assert arc_exec.run_program(src, [[[0]]]) == [[[0]]]
    src2 = ("import sys\n"
            "def transform(grid):\n"
            f"    sys.__stdout__.write('@@HTSA_RESULT@@' + {forged!r} + chr(10))\n"
            "    return [[0]]\n")
    assert arc_exec.run_program(src2, [[[0]]]) == [[[0]]]      # no nonce: not a result line


# ================================================================ best-of-N batch sizing
def test_next_batch_size_is_conservative_near_the_budget():
    assert bon.next_batch_size(0, 0, 1000, 80) == 1
    assert bon.next_batch_size(100, 1, 1000, 80, max_cost=100) == 6
    assert bon.next_batch_size(100, 1, 350, 80, max_cost=100) == 2
    assert bon.next_batch_size(100, 1, 250, 80, max_cost=100) == 1
    assert bon.next_batch_size(100, 1, 199, 80, max_cost=100) == 0
    assert bon.next_batch_size(100, 1, 1000, 80, max_cost=400) == 2     # sized by the largest call


# ================================================================ bench: cost hygiene and matched cost
def test_bench_errored_plain_run_is_retried_and_kept_out_of_cost(bench_lab, monkeypatch):  # noqa: F811
    monkeypatch.setattr(llm.time, "sleep", lambda s: None)
    items = tb.data.load_items("bt", "dev-tune")[:2]
    bad = items[0]["id"]
    state = {"fail": True}

    def flaky(prompt, role, meta):
        if state["fail"] and meta.get("item_id") == bad:
            raise llm.CallError("overloaded 529 for a while", usage=Usage(50, 0, 0, 0))
        return tb.default_mock(prompt, role, meta)
    llm.set_mock(flaky)
    bench.main(["--benchmark", "bt", "--arm", "plain", "--items", "2", "--backend", "mock",
                "--m", "3", "--batch", "flaky"])
    out = config.RESULTS_DIR / "flaky"
    rows = {r["item_id"]: r for r in read_jsonl(out / "runs.jsonl")}
    assert rows[bad]["status"] == "error" and rows[bad]["spent_tokens"] == 150   # 3 attempts charged
    assert {r["item_id"] for r in read_jsonl(out / "cost.jsonl")} == {items[1]["id"]}
    assert read_json(out / "budget.json")["bt"]["mock"]["n"] == 1
    assert any(r["run_id"] == rows[bad]["run_id"] for r in read_jsonl(out / "errors.jsonl"))
    state["fail"] = False
    bench.main(["--benchmark", "bt", "--arm", "plain", "--items", "2", "--backend", "mock",
                "--m", "3", "--batch", "flaky"])
    rows2 = [r for r in read_jsonl(out / "runs.jsonl") if r["item_id"] == bad]
    assert rows2[-1]["status"] != "error" and len(rows2) == 2          # retried, old row kept
    assert len(read_jsonl(out / "cost.jsonl")) == 2
    assert (out / "lint.json").exists() and read_json(out / "lint.json")["n_prompts"] >= 2


def test_bench_refuses_budget_without_a_successful_plain_run(bench_lab):  # noqa: F811
    llm.set_mock(lambda p, r, m: (_ for _ in ()).throw(llm.CallError("fatal", usage=Usage(1, 0, 0, 0))))
    with pytest.raises(SystemExit):
        bench.main(["--benchmark", "bt", "--arm", "plain", "--items", "1", "--backend", "mock",
                    "--m", "3", "--batch", "nocost"])


def test_bench_skips_best_of_n_when_scaffold_run_is_missing(bench_lab, monkeypatch):  # noqa: F811
    import sys as _sys
    import types
    items = tb.data.load_items("bt", "dev-tune")[:2]
    bad = items[1]["id"]
    m = types.ModuleType("harness.think")

    def think_fn(item, *, m, replicate, backend, batch, flags=None, params=None, arm="scaffold"):
        if item["id"] == bad:
            raise RuntimeError("scaffold crashed")
        return tb.Answer(status="unverified", answer="A", verification_type="agreement", cand_id=None,
                         spent_tokens=1000, rounds=1)
    m.think = think_fn
    monkeypatch.setitem(_sys.modules, "harness.think", m)
    bench.main(["--benchmark", "bt", "--arm", "plain,scaffold,bestofn_vote", "--items", "2",
                "--backend", "mock", "--m", "3", "--batch", "skip"])
    out = config.RESULTS_DIR / "skip"
    rows = read_jsonl(out / "runs.jsonl")
    bon_rows = {r["item_id"]: r for r in rows if r["arm"] == "bestofn_vote"}
    assert set(bon_rows) == {items[0]["id"]} and bon_rows[items[0]["id"]]["budget_tokens"] == 1000
    errs = read_jsonl(out / "errors.jsonl")
    assert any("skipped" in e["error"] and "bestofn_vote" in e["run_id"] for e in errs)


# ================================================================ driver: crash, judge budget, bar
def test_think_crash_writes_answer_and_error_row_and_retry_moves_aside(stubs):  # noqa: F811
    item = tt.arc_item("t_crash")
    llm.set_mock(tt.make_mock("arc", tt.CORRECT))
    good_probe = stubs.mods["probe"].run_probe

    def bad_probe(*a, **k):
        raise RuntimeError("probe exploded")
    stubs.mods["probe"].run_probe = bad_probe
    ans = think.think(item, m=20, replicate=0, backend="mock", batch="tc_crash")
    rd = tt.run_dir_of("tc_crash", item)
    assert ans.status == "abstain" and ans.reason.startswith("crash: RuntimeError")
    assert (rd / "error.json").exists() and (rd / "answer.json").exists()
    assert ans.spent_tokens > 0                                    # encode spend charged
    runs = read_jsonl(Path(config.RESULTS_DIR) / "tc_crash" / "runs.jsonl")
    assert runs[-1]["status"] == "error" and runs[-1]["spent_tokens"] == ans.spent_tokens
    st = read_json(rd / "state.json")
    assert st["decisions"][-1]["step"] == "final" and any("crash" in e for e in st["errors"])
    stubs.mods["probe"].run_probe = good_probe
    ans2 = think.think(item, m=20, replicate=0, backend="mock", batch="tc_crash")   # no FileExistsError
    assert ans2.status == "solved"
    assert list(rd.parent.glob(f"{rd.name}.old-*"))
    runs = read_jsonl(Path(config.RESULTS_DIR) / "tc_crash" / "runs.jsonl")
    assert runs[-1]["status"] == "solved" and runs[-1]["run_instance"] != runs[-2]["run_instance"]
    # ledger: both instances are present, derived views keep the latest only
    rows = [r for r in read_jsonl(config.LEDGER_PATH) if r["run_id"] == rd.name]
    assert {r["run_instance"] for r in rows} == {runs[-1]["run_instance"], runs[-2]["run_instance"]}
    cur = ledger.current_rows(rows)
    assert {r["run_instance"] for r in cur} == {runs[-1]["run_instance"]}
    assert sum(r["tokens"]["total_tokens"] for r in cur) == ans2.spent_tokens
    with pytest.raises(FileExistsError):                            # a completed run is protected
        think.think(item, m=20, replicate=0, backend="mock", batch="tc_crash")


def test_judge_is_skipped_when_it_does_not_fit_the_budget(stubs):  # noqa: F811
    item = tt.arc_item("t_jbudget")
    llm.set_mock(tt.make_mock("arc", tt.CORRECT))
    stubs.mods["judge"].est_cost = lambda C, P, b: 10 ** 9
    ans = think.think(item, m=20, replicate=0, backend="mock", batch="tc_jbudget")
    st = read_json(tt.run_dir_of("tc_jbudget", item) / "state.json")
    cyc = [d for d in st["decisions"] if d["step"].startswith("cycle")]
    assert cyc and "judge_skipped" in cyc[0]["signal"]
    assert not [r for r in tt.ledger_rows(st["run_id"]) if r["card"] == "judge"]
    assert ans.status == "solved"
    tt.spent_matches_ledger(st["run_id"], ans.spent_tokens)


def test_clears_checks_required_verification_and_checklist():
    bar = {"required_verification": "demo_match", "all_items": True}
    ok = VerifyResult(id="a", status="verified", verification_type="demo_match", partial_score=1.0)
    why: list = []
    assert think._clears(bar, ok, why) and why == []
    weak = VerifyResult(id="b", status="verified", verification_type="agreement", partial_score=1.0)
    why = []
    assert not think._clears(bar, weak, why) and "below required demo_match" in why[0]
    chk = VerifyResult(id="c", status="verified", verification_type="demo_match", partial_score=1.0,
                       details={"checklist": {"size": True, "colors": False}})
    assert not think._clears(bar, chk)
    assert think._clears({}, weak)                                   # no bar: status decides


# ================================================================ e2e on the real modules
def _ledger_reconciles(rd: Path, spent: int) -> None:
    rows = tt.ledger_rows(rd.name)
    assert sum(r["tokens"]["total_tokens"] for r in rows) == spent
    for r in rows:
        if r.get("cand_id"):            # verification rows carry the candidate's call id
            continue
        if r["call_id"].startswith("c"):
            rec = read_json(rd / "calls" / f"{r['call_id']}.json") or \
                read_json(rd / "private" / "calls" / f"{r['call_id']}.json")
            assert rec, f"no call record for ledger row {r['call_id']}"
            assert rec["total_tokens"] == r["tokens"]["total_tokens"]
            assert rec["usage"]["output_tokens"] <= rec["max_tokens"] or rec["usage_estimated"]
        else:
            assert r["tokens"]["total_tokens"] == 0 or r["card"] in ("encode", "probe", "judge")
    assert all(r["run_instance"] for r in rows)


def test_e2e_private_defaults_stay_private_and_ledger_reconciles(e2e_lab):  # noqa: F811
    arc = te.arc_items()[0]
    program = "def transform(grid):\n    # because the rows are mirrored\n    return [row[::-1] for row in grid]\n"

    def fn(prompt, role, meta):
        if role in te.GEN_ROLES or role == "probe":
            block = f"```python\n{program}```"
            return block if role == "probe" else "1. " + block
        return te.make_mock("arc")(prompt, role, meta)
    llm.set_mock(fn)
    ans = think.think(arc, m=20, replicate=0, backend="mock", batch="e2e-priv",
                      flags={"judge_when_verify_free": True})   # this test audits judge routing
    rd = te.run_dir_of("e2e-priv", arc)
    assert ans.status == "solved"
    # the defaults reply lives only under private/
    for f in rd.rglob("*"):
        if f.is_file() and "private" not in f.relative_to(rd).parts:
            assert "zqdflt" not in f.read_text(encoding="utf-8", errors="replace"), f
    assert "zqdflt" in (rd / "private" / "defaults.json").read_text(encoding="utf-8")
    assert list((rd / "private" / "calls").glob("*.json"))
    # the judge never sees the program comment; probe and judge calls are routed and linted
    routing = read_jsonl(rd / "routing.jsonl")
    judge_ids = [r["call_id"] for r in routing if r.get("role") == "judge"]
    assert judge_ids and any(r.get("role") == "probe" for r in routing)
    for cid in judge_ids:
        text = (rd / "prompts" / f"{cid}.txt").read_text(encoding="utf-8")
        assert "because the rows are mirrored" not in text and "row[::-1]" in text
    # ARC cands files carry the pred the loop used
    rows = [r for f in (rd / "cands").glob("*.jsonl") for r in read_jsonl(f) if r["card"] != "probe"]
    assert rows and all(r["pred"] is not None for r in rows)
    assert graph.check(rd)["ok"]
    _ledger_reconciles(rd, ans.spent_tokens)
    st = read_json(rd / "state.json")
    assert st["run_instance"] and all(r["run_instance"] == st["run_instance"] for r in tt.ledger_rows(rd.name))


def test_e2e_duplicate_programs_are_counted_as_drops(e2e_lab):  # noqa: F811
    arc = te.arc_items()[1]
    wrong = "def transform(grid):\n    return [row[:] for row in grid]\n"

    def fn(prompt, role, meta):
        if role in te.GEN_ROLES:
            return f"1. ```python\n{wrong}```\n2. ```python\n{wrong}\n```"
        if role == "probe":
            return f"```python\n{wrong}```"
        return te.make_mock("arc")(prompt, role, meta)
    llm.set_mock(fn)
    ans = think.think(arc, m=20, replicate=0, backend="mock", batch="e2e-dups")
    rd = te.run_dir_of("e2e-dups", arc)
    assert ans.status == "abstain"
    chk = graph.check(rd)
    assert chk["ok"] and chk["n_drops"] > 0, chk
    dropped = graph.dropped_ids(rd)
    assert dropped and dropped <= set(chk and {r["id"] for f in (rd / "cands").glob("*.jsonl") for r in read_jsonl(f)})


# ================================================================ memory: instances and drops
def test_stats_keep_latest_run_instance(e2e_lab):  # noqa: F811
    base = dict(batch="b", split="train", cls="arc", card="seeded", round_type="first", round=0,
                operator="none", seed="", perm=0)
    ledger.append({**base, "run_id": "r1", "run_instance": "old", "call_id": "c1", "tokens": {"total_tokens": 100}})
    ledger.append({**base, "run_id": "r1", "run_instance": "old", "call_id": "c2", "tokens": {"total_tokens": 100},
                   "status": "verified"})
    ledger.append({**base, "run_id": "r1", "run_instance": "new", "call_id": "c3", "tokens": {"total_tokens": 40}})
    ledger.append({**base, "run_id": "r1", "run_instance": "new", "call_id": "c4", "tokens": {"total_tokens": 40},
                   "status": "fail"})
    stats.rebuild("b")
    c = stats.cell(stats.load_views("b"), "arc", "seeded", "first")
    assert c["pass"] == 0 and c["fail"] == 1 and c["mean_tokens"] == 40.0


def test_expected_drops_include_cluster_dropped_ids():
    cands = [{"id": "a", "card": "seeded", "pred": None}, {"id": "b", "card": "seeded", "pred": None}]
    assert graph.expected_drops(cands, True) == set()
    assert graph.expected_drops(cands, True, {"b"}) == {"b"}
