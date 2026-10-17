"""Bug pass 2026-10-17 (night), cross-cutting seams. Each test proves one bug where two areas meet; each fails
on master. The fixes belong to the area owners (docs/BUG_PASS_SEAMS.md names the owner per test).

Mock backend and tmp_path only (conftest repoints the lab root); no training, no model calls."""
from __future__ import annotations

import json
from types import SimpleNamespace

import pytest

from harness import llm
from harness.schemas import Candidate, Usage, write_json
from nano import profile as PF


@pytest.fixture(autouse=True)
def _llm_profile():
    prev = PF.current()
    PF.set_current("llm")
    yield
    PF.set_current(prev)
    llm.set_mock(None)


def _loop(batch="seams", profile=None):
    from nano.loop import NanoLoop
    if profile:
        PF.set_current(profile)
    lp = NanoLoop(batch, 0, "mock", 1_000_000, 2, 0.0, None)
    write_json(lp.run_dir / "state.json", {"run_id": lp.run_id, "arm": lp.arm, "decisions": []})
    (lp.run_dir / "problem.md").write_text("# Problem\n\nGOAL: lower the score\n", encoding="utf-8")
    lp.plan_with_model = False
    lp.plan_tree(1)
    return lp


def _memory_with_content(lp, monkeypatch):
    """Every part already has memory, so the memory-free context is dealt (nano/memory.py is not under test)."""
    mem = SimpleNamespace(read=lambda part: "FACTS:\n- something measured", block=lambda part: "MEMORY BLOCK\n\n")
    monkeypatch.setattr(lp, "memory", lambda: mem)


def _first_part(lp):
    return next(n for n in lp.tree if lp._part_of(n["id"]) is not None)


def _quiet_ideation(lp, monkeypatch, calls):
    lp.do_research, lp.ideation_web, lp.web_mode, lp.leap_share = False, False, "off", 0.0
    good = "IDEA: x\nMECHANISM: m\nREMOVES: the assumption a"

    def call(prompt, role, max_out, meta, **k):
        calls.append(dict(meta))
        return SimpleNamespace(text=good, call_id=f"c{len(calls)}", usage=Usage(1, 1, 0, 0))
    monkeypatch.setattr(lp, "_call", call)
    monkeypatch.setattr(lp, "_ledger", lambda *a, **k: None)


# ---------------------------------------------------------------- S1 (ideation half): the test cap is exceeded
def test_max_sketch_calls_cap_holds_with_memory_free_contexts(monkeypatch):
    """--max-sketch-calls is "at most this many idea agents per round", but _pick_memory_free runs after the cap
    and adds one context per part that has a single one. The dry run (cap 10) ran 12 and 15 contexts."""
    lp = _loop()
    lp.off_tree_share, lp.max_sketch_calls = 0.0, 3
    _memory_with_content(lp, monkeypatch)
    calls: list = []
    _quiet_ideation(lp, monkeypatch, calls)
    lp.ideate_round(1, [f"w{i}" for i in range(40)])
    sketch_calls = [m for m in calls if str(m.get("card", "")).startswith("sketch:")]
    assert len(sketch_calls) <= 3, f"{len(sketch_calls)} idea contexts ran under --max-sketch-calls 3"


# ---------------------------------------------------------------- S2 (ideation half): the memory-free copy loses its text
@pytest.mark.parametrize("card", ["owner", "contradiction"])
def test_memory_free_copy_keeps_the_context_text(monkeypatch, card):
    """For owner and contradiction contexts the spec's seed slot carries the text the prompt is built from
    (OWNER_ADDENDUM / CONTRADICTION_ADDENDUM .format(text=seed)). A part with one such context gets an extra
    memory-free copy, and _pick_memory_free puts a random seed word in that slot: the copy's prompt reads
    'apple' instead of the owner's mechanism or the measured trade-off."""
    lp = _loop()
    _memory_with_content(lp, monkeypatch)
    node = _first_part(lp)
    text = "zero-init the gate on the attention output" if card == "owner" else "'gated mlp' improved the score but cost step time x1.3"
    out = lp._pick_memory_free(1, [(card, text, node, "inward")], ["apple", "pear"])
    assert len(out) == 2, out
    extra = out[1]
    assert extra[0] == card
    assert extra[1] == text, f"the memory-free {card} context was given {extra[1]!r} as its text"


# ---------------------------------------------------------------- S3 (ideation half -> source_yield.json): interrogation calls counted as contexts
def test_origin_stats_count_idea_contexts_not_interrogation_calls(monkeypatch):
    """_origin_stats counts "contexts" as distinct call_ids of sketches whose origin is tree (the default). The
    interrogation's offshoots carry no "origin" (nor "round"), so every deepen call counts as a tree context and
    every offshoot of an off-map idea counts as a tree sketch. In the dry run source_yield.json said 83 tree
    contexts where discovery.json counted 27 idea contexts, so the rule-3 share shift compares unlike things.
    contexts_by_node and the resume rebuild in _select_with_lanes both exclude card "deepen"."""
    from nano import dry_run as D
    from nano import tree
    lp = _loop()
    lp.do_premortem, lp.ideation_web, lp.deepen_depth = False, False, 0
    part = _first_part(lp)["id"]
    off = tree.OFF_TREE_NODE["id"]
    lp.sketches = [
        {"id": "s1", "idea": "a", "mechanism": "m", "prediction": "p", "test": "t", "card": "seeded", "call_id": "c1", "node": part,
         "direction": "inward", "origin": "tree", "round": 1},
        {"id": "s2", "idea": "b", "mechanism": "m", "prediction": "p", "test": "t", "card": "blank", "call_id": "c2", "node": off,
         "direction": "inward", "origin": "off", "round": 1}]
    llm.set_mock(D.mock)
    cl = {"cluster_id": f"{off}-in-k00", "name": "b", "node": off, "direction": "inward", "members": ["s2"],
          "representative": "s2", "cards": ["blank"]}
    n_off = lp.deepen_round(1, [cl], 0)
    assert n_off > 0, "the mock interrogation produced no offshoots"
    st = lp._origin_stats()
    assert st["tree"]["contexts"] == 1, f"tree contexts {st['tree']['contexts']}: the interrogation call was counted"
    assert st["tree"]["sketches"] == 1, f"tree sketches {st['tree']['sketches']}: offshoots of an off-map idea counted as tree"


# ---------------------------------------------------------------- S4 (execution half x checks): the hedge lane is LLM-only
def test_hedge_lane_fires_for_a_script_checker_gap_failure():
    """_hedge looks for feedback rung 3 with a reason starting "at step" (nano/check.py, the LLM checker). The
    script checker (nano/checks/script.py) reports its score-gap failure at rung 2 ("the quick score is ..."),
    so on every generic profile --hedge-share is a silent no-op and the false-reject rate is never measured."""
    lp = _loop("seams-hedge", profile="binpack_nobase")
    c = Candidate(id="nhedge01", text="x", card="impl:seeded", operator="k", seed="", perm=0, round=1, call_id="c0",
                  program="def choose_bin(): return -1\n", extra={"node": _first_part(lp)["id"], "direction": "inward"})
    lp.cands.append(c)
    lp.vres[c.id] = {"status": "fail", "rung_reached": 2, "partial_score": 0.5, "metrics": {"learn_gap": 0.09},
                     "feedback": {"rung": 2, "reason": "the quick score is 1.172 against the baseline's 1.081 on the same "
                                                       "instances (gap +0.0906, negative is better; z 9.88; allowed 0.0200)"}}
    lp.hedge_share = 1.0
    lp._hedge([c], 1)
    assert c.id in lp.hedged, "a script-checker gap failure is never hedged"


# ---------------------------------------------------------------- S5 (execution half x checks): a learning failure gets "specialize"
def test_revise_move_for_a_script_checker_learning_failure_is_fix(monkeypatch):
    """_rounds picks the revise move from the feedback rung: rung 2 -> "specialize" (narrow a resource failure),
    else "fix" (the comment: "a learning failure gets fixed"). In the LLM checker rung 2 is VRAM / step time; in
    the script checker rung 2 is the score gap, so a learning failure on a generic profile is narrowed instead."""
    lp = _loop("seams-revise", profile="binpack_nobase")
    c = Candidate(id="nrev01", text="x", card="impl:seeded", operator="k", seed="", perm=0, round=1, call_id="c0",
                  program="x\n", extra={"node": _first_part(lp)["id"], "direction": "inward", "src_hash": "h1"})
    lp.cands.append(c)
    lp.vres[c.id] = {"status": "fail", "rung_reached": 2, "partial_score": 0.5, "metrics": {},
                     "feedback": {"rung": 2, "reason": "the quick score is 1.17 against the baseline's 1.08 on the same "
                                                       "instances (gap +0.09, negative is better; z 9.9; allowed 0.02)"}}
    lp.resume, lp.rounds, lp.do_deepen, lp.family_variants, lp.use_memory = True, 1, False, 0, False
    moves = []
    for name in ("ideate_round", "cluster_sketches", "_discovery", "_write_tree", "_curate_memory", "_stage"):
        monkeypatch.setattr(lp, name, lambda *a, **k: [])
    monkeypatch.setattr(lp, "_select_with_lanes", lambda *a, **k: [])
    monkeypatch.setattr(lp, "compose_round", lambda *a, **k: [])
    monkeypatch.setattr(lp, "_finish", lambda t0: {})
    monkeypatch.setattr(lp, "run_card", lambda card, rnd, op, *a, **k: moves.append((card, op)))
    lp._rounds(0.0)
    assert ("revise", "fix") in moves, f"moves {moves}: a score-gap (learning) failure was sent to 'specialize'"


# ---------------------------------------------------------------- S6 (ideation half -> report): selection counted per generation
def test_selection_rows_are_written_once_per_round(monkeypatch):
    """_select_with_lanes runs once before the interrogation and once after every generation (_rounds), and each
    call appends a full set of selection.jsonl rows and a slots_by_origin decision. report.collect counts every
    row, so the dry run reported picked_main 6 + picked_lane 9 for 5 builds."""
    from nano import loop as L
    from nano import report
    lp = _loop()
    lp.round_now = 1
    part = _first_part(lp)["id"]
    clusters = [{"cluster_id": f"{part}-ou-k0{i}", "name": f"idea {i}", "node": part, "direction": "outward",
                 "cards": ["seeded"], "score": 1.0 - i / 10, "members": [f"s{i}"], "representative": f"s{i}",
                 "prior": "new", "leap_share": 0.0} for i in range(5)]
    lp.clusters = clusters
    monkeypatch.setattr(L.tree, "split_select", lambda by_node, k, *a, **kw: [clusters[0]])
    by_node = {part: clusters}
    for _ in range(3):                      # before the interrogation, after generation 0 and after generation 1
        lp._select_with_lanes(by_node, 3, set())
    rows = [json.loads(x) for x in (lp.run_dir / "selection.jsonl").read_text(encoding="utf-8").splitlines()]
    keys = [(r["round"], r["cluster_id"]) for r in rows]
    assert len(keys) == len(set(keys)), f"{len(keys)} rows for {len(set(keys))} groups in one round"
    sel = report.collect(lp.run_dir)["selection"]
    assert sel.get("picked_main") == 1, f"report.selection {sel}: one main pick counted several times"


# ---------------------------------------------------------------- S7 (execution half): resume forgets the yield records
def test_resume_keeps_the_moved_off_tree_share():
    """The off-map share moves with yield (_shift_off_share) and is written to problem_tree.json, but load_state
    never reads it back: a resumed run goes on with the command-line share."""
    from nano.loop import NanoLoop
    lp = _loop("seams-resume")
    lp.off_tree_share = 0.5
    lp._write_tree()
    lp2 = NanoLoop("seams-resume", 0, "mock", 1_000_000, 2, 0.0, None)
    lp2.resume = True
    lp2.load_state()
    assert lp2.off_tree_share == 0.5, f"resumed share {lp2.off_tree_share}"


def test_resume_keeps_source_yield_and_discovery_history():
    """source_yield.json, seed_yield.json and discovery.json hold one row per round, rewritten from lists kept only
    in memory. load_state does not reload them, so the first write after a resume drops every earlier round
    (report.json "discovery" reads discovery.json)."""
    from nano.loop import NanoLoop
    lp = _loop("seams-resume2")
    lp.source_yield = [{"round": 2, "by": "clusters_per_context", "share_before": 0.4, "share_next": 0.5}]
    write_json(lp.run_dir / "source_yield.json", {"rounds": lp.source_yield})
    lp.discovery = [{"round": 1, "contexts": 12, "sketches": 60, "new_clusters": 47, "by_card": {}}]
    write_json(lp.run_dir / "discovery.json", {"rounds": lp.discovery})
    lp.seed_yield = [{"round": 2, "function": {"f": {"sketches": 5, "clusters": 5}}, "seed": {}}]
    write_json(lp.run_dir / "seed_yield.json", {"rounds": lp.seed_yield, "mode": "function"})
    lp2 = NanoLoop("seams-resume2", 0, "mock", 1_000_000, 2, 0.0, None)
    lp2.resume = True
    lp2.load_state()
    assert len(lp2.source_yield) == 1 and len(lp2.discovery) == 1 and len(lp2.seed_yield) == 1, \
        (lp2.source_yield, lp2.discovery, lp2.seed_yield)


# ---------------------------------------------------------------- S8 (execution half): the commitments hash changes on resume
def test_commitments_hash_is_stable_across_a_resume(monkeypatch):
    """run() calls _write_commitments on every start, a resume included. The hashed record carries "ts", so the
    resumed run gets a new hash and overwrites commitments.json and state.json's commitments_hash: the
    registered-report record no longer shows what the run committed to before any idea existed."""
    from nano import loop as L
    lp = _loop("seams-commit")
    monkeypatch.setattr(L, "now_ts", lambda: "2026-10-17T10:00:00")
    lp._write_commitments()
    h1 = lp.commitments_hash
    lp2 = L.NanoLoop("seams-commit", 0, "mock", 1_000_000, 2, 0.0, None)
    lp2.resume = True
    lp2.load_state()
    assert lp2.commitments_hash == h1
    monkeypatch.setattr(L, "now_ts", lambda: "2026-10-17T11:30:00")
    lp2._write_commitments()                 # what run() does right after load_state
    assert lp2.commitments_hash == h1, "the same commitments got a new hash on resume"


# ---------------------------------------------------------------- S9 (ideation half): decisions logged before the cap
def test_off_tree_decision_matches_the_contexts_dealt(monkeypatch):
    """The "off_tree" and "doubt_cards" decisions are logged before the --max-sketch-calls cap, so they report
    contexts that were cut (dry run: off_map 20, doubt dealt 6, one off-map context ran)."""
    from nano import tree
    lp = _loop()
    lp.max_sketch_calls, lp.use_memory, lp.off_tree_share = 4, False, 0.4
    calls: list = []
    _quiet_ideation(lp, monkeypatch, calls)
    lp.ideate_round(1, [f"w{i}" for i in range(60)])
    dec = next(d for d in lp.decisions if d.get("step") == "off_tree")
    ran_off = lp.contexts_by_node[1].get(tree.OFF_TREE_NODE["id"], 0)
    assert dec["off_map"] == ran_off, f"decision says {dec['off_map']} off-map contexts, {ran_off} ran"


# ---------------------------------------------------------------- S10 (modules: report): analogy files listed as briefs
def test_report_briefs_are_parts_not_analogy_files(tmp_path):
    """report.collect (and dashboard.snapshot) read every research/*.json as a brief, so each part also shows a
    "<part>_analogy" brief with 0 known / 0 failed / 0 open (dry run: 12 briefs for 6 parts)."""
    from nano import report
    run = tmp_path / "run"
    (run / "research").mkdir(parents=True)
    write_json(run / "research" / "mix.json", {"node": "mix", "known": [{"name": "k"}], "failed": [], "open": [], "source": "web"})
    write_json(run / "research" / "mix_analogy.json", {"node": "mix_analogy", "analogies": [{"field": "x"}], "source": "web"})
    write_json(run / "state.json", {"decisions": []})
    briefs = report.collect(run)["briefs"]
    assert set(briefs) == {"mix"}, briefs


# ---------------------------------------------------------------- S11 (execution half): n_checked counts hedged failures
def test_answer_n_checked_counts_checked_candidates_only(monkeypatch):
    """_finish builds `pool` from checked candidates plus the hedge lane (failures sent on to the long run) and
    writes answer["n_checked"] = len(pool); report.json "checked" counts verify status only, so the two disagree
    whenever a candidate is hedged (the dashboard and nano/experiments/binpack_arms.py print n_checked)."""
    lp = _loop("seams-nchecked")
    lp.long_steps = 0
    c = Candidate(id="nhedged1", text="x", card="impl:seeded", operator="k", seed="", perm=0, round=1, call_id="c0",
                  program="x\n", extra={"node": _first_part(lp)["id"], "direction": "inward"})
    lp.cands.append(c)
    lp.vres[c.id] = {"status": "fail", "rung_reached": 3, "partial_score": 0.75, "feedback": {"rung": 3, "reason": "at step 45"},
                     "metrics": {"learn_gap": 0.01, "learn_z": 1.2}}
    lp.hedged.add(c.id)
    ans = lp._finish(0.0)
    assert ans["n_checked"] == 0, f"n_checked {ans['n_checked']} with no checked candidate (one hedged failure)"
