"""Tests for encode.py, run_card.py and lint.py (owner: cards). Mock backend only."""
from __future__ import annotations

import json
import os
import tempfile
from pathlib import Path

os.environ.setdefault("HTSA_LAB_ROOT", tempfile.mkdtemp(prefix="htsa_cards_"))

import pytest  # noqa: E402

from harness import config, encode, lint, llm, run_card  # noqa: E402
from harness.run_card import CardError, CardSpec, LintError  # noqa: E402
from harness.schemas import Candidate, read_json, read_jsonl  # noqa: E402

ARC_ITEM = {
    "id": "arc_t1", "benchmark": "arc", "family": "arc", "split": "dev-tune",
    "train": [{"input": [[1, 0], [0, 0]], "output": [[0, 1], [0, 0]]},
              {"input": [[0, 2], [0, 0]], "output": [[2, 0], [0, 0]]}],
    "test_input": [[3, 0], [0, 0]],
    "test_output": [[9, 8, 7], [6, 5, 4]],
}
ARC_KEY_STRINGS = ["987\n654", "[9, 8, 7]", "[[9,8,7]"]
BT_ITEM = {
    "id": "bt_t1", "benchmark": "bt", "family": "bt_sp", "split": "dev-tune",
    "question": "You are a bus driver. A man carries a lantern onto the bus. What colour are the driver's eyes?",
    "choices": ["Blue", "Whatever colour your eyes are", "Green", "None of above."],
    "label": 1,
    "answer": "SENTINELKEYTEXT",          # stray raw field: must never be rendered
}
DEFAULT_SENTINEL = "DEFAULTSENTINEL"
PLANTED = "PLANTEDSENTINEL"
ENC_ARC = ("GOAL: Find the rule.\nFACTS:\n1. Each input has one red cell.\n2. Each output moves it.\n"
           "RESOURCES:\n1. Mirror operation.\nCHECKLIST:\n1. The output grid has the input size.\n"
           "2. Every example must be reproduced.\nNOUNS:\ncell\n")
ENC_BT = ("GOAL: Choose the option that names the eye colour of the driver.\nFACTS:\n"
          "1. The reader is the bus driver.\n2. A man carries a lantern onto the bus.\n"
          "RESOURCES:\n1. The four options.\nCHECKLIST:\n1. The answer must be one option.\n"
          "2. The answer must follow from the question text.\nNOUNS:\nbus\ndriver\nlantern\nman\n")
ARC_GEN = ("1. ```python\ndef transform(grid):\n    return [row[::-1] for row in grid]\n```\n"
           "2. ```python\ndef transform(grid):\n    return [row[:] for row in grid]\n```\n"
           "3. ```python\nx = 1\n```")
BT_GEN = "1. B. The driver is the reader.\n2. C because green is common. It is a guess.\n3. A"
TRANSFORMED_BT = ("DEEP CONSTRAINTS:\n1. The reader is the driver.\nTRANSFORMED PROBLEM:\n"
                  "TRANSFORMEDMARK: a pilot flies a plane; which option names the pilot's eyes?")


def responder(log: list, *, encode_b: str | None = None, generate: dict | None = None):
    """Mock fn(prompt, role, meta) that records every call and answers by role."""
    def fn(prompt, role, meta):
        log.append({"role": role, "meta": dict(meta), "prompt": prompt})
        b = meta.get("benchmark")
        if role == "encode":
            if meta.get("purpose") == "resolve":
                return "1. Resolved constraint one.\n2. Resolved constraint two."
            if meta.get("purpose") == "encode_b" and encode_b is not None:
                return encode_b
            return ENC_ARC if b == "arc" else ENC_BT
        if role == "defaults":
            return "\n".join(f"{i}. {'B' if b == 'bt' else 'rule'} {DEFAULT_SENTINEL}" for i in range(1, 6))
        if role == "transform":
            return TRANSFORMED_BT if b == "bt" else "TRANSFORMED PROBLEM:\nTRANSFORMEDMARK grids 10 01"
        if role == "converter":
            return "1. B" if b == "bt" else ARC_GEN
        if generate and meta.get("card") in generate:
            return generate[meta["card"]]
        return ARC_GEN if b == "arc" else BT_GEN
    return fn


@pytest.fixture
def calls():
    log: list = []
    llm.set_mock(responder(log))
    yield log
    llm.set_mock(None)


def _encode(item, tmp_path):
    run_dir = tmp_path / item["id"]
    return encode.encode(item, run_dir, backend="mock", replicate=0, log_dir=run_dir / "calls"), run_dir


def _run(spec, problem, run_dir, **kw):
    return run_card.run_card(spec, problem, run_dir, backend="mock", round_no=kw.pop("round_no", 1),
                             log_dir=run_dir / "calls", replicate=0, **kw)


def _prompts(run_dir: Path) -> list[str]:
    return [p.read_text(encoding="utf-8") for p in sorted((run_dir / "prompts").glob("*.txt"))]


# ---------------------------------------------------------------- lint
def test_lint_fail_and_warn_patterns():
    bad = ("You are a world-class solver. Act as an analyst, as an expert would. Take a deep breath. "
           "Your job depends on it; lives depend on it. Use your subconscious, free-associate, and "
           "say what you are secretly thinking. Be creative and think outside the box.")
    f = lint.lint_text(bad)
    fails = {x["pattern"] for x in f if x["severity"] == "fail"}
    warns = {x["pattern"] for x in f if x["severity"] == "warn"}
    assert {"persona_you_are", "persona_world_class", "persona_act_as", "persona_as_expert",
            "bodily_breath", "stakes_job", "stakes_lives", "hidden_subconscious",
            "hidden_free_associate", "hidden_secretly_thinking",
            "creative_be_creative", "creative_outside_box"} <= fails      # Pr10: creativity nudges fail
    assert not {"creative_be_creative", "creative_outside_box"} & warns
    assert lint.lint_text("If you are able, write the list. Exact as given.") == []


def test_lint_templates_clean():
    res = lint.lint_templates()
    assert res == {"fails": [], "warns": []}
    assert len(list(config.TEMPLATES_DIR.glob("*.txt"))) >= 12


def test_lint_domain_nouns():
    assert lint.lint_domain("X1 carries X2", ["lantern"]) == []
    assert lint.lint_domain("two lanterns", ["lantern"])[0]["match"] == "lanterns"


def test_concepts_200_unique():
    words = run_card.load_seeds()
    assert len(words) == 200 and len(set(words)) == 200
    assert all(w.isalpha() and w.islower() for w in words)


# ---------------------------------------------------------------- cards and rendering
@pytest.mark.parametrize("name", ["seeded", "low_prior", "transform", "formal", "revise"])
def test_cards_valid(name):
    card = run_card.load_card(name)
    assert card["name"] == name and run_card.check_card(card, name) == []


def test_card_schema_rejects_bad():
    bad = {"name": "x", "role": "judge", "steps": [], "operator_choices": ["none"], "applies_to": ["arc"],
           "rubric": "no"}
    errs = run_card.check_card(bad)
    assert any("role" in e for e in errs) and any("rubric" in e for e in errs) and any("steps" in e for e in errs)
    with pytest.raises(CardError):
        run_card.load_card("does_not_exist")


def test_render_spans_and_mismatch():
    text, spans = run_card.render("A {{goal}} B {{seed}}", {"goal": "gg", "seed": "ss"})
    assert text == "A gg B ss"
    assert [(text[a:b], k) for a, b, k in spans] == [("gg", "goal"), ("ss", "seed")]
    with pytest.raises(CardError):
        run_card.render("A {{goal}}", {"goal": "g", "seed": "s"})
    with pytest.raises(CardError):
        run_card.render("A {{goal}} {{facts}}", {"goal": "g"})


def test_lint_blocks_template_text_not_item_text(tmp_path, monkeypatch, calls):
    tdir = tmp_path / "tpl"
    tdir.mkdir()
    (tdir / "bad.txt").write_text("You are a careful solver.\n{{goal}}", encoding="utf-8")
    (tdir / "ok.txt").write_text("Goal: {{goal}}", encoding="utf-8")
    monkeypatch.setattr(config, "TEMPLATES_DIR", tdir)
    kw = dict(role="generate", run_dir=tmp_path / "r", log_dir=None, backend="mock", meta={})
    with pytest.raises(LintError):
        run_card.dispatch("bad", {"goal": "x"}, **kw)
    res = run_card.dispatch("ok", {"goal": "You are a bus driver."}, **kw)
    assert res.error is None
    rows = read_jsonl(tmp_path / "r" / "prompts" / "lint.jsonl")
    assert rows[0]["blocked"] is True and rows[1]["blocked"] is False
    assert rows[1]["findings"][0]["in_input"] is True


# ---------------------------------------------------------------- parsing and post-check
def test_parse_arc_code_blocks():
    out = run_card.parse_candidates(ARC_GEN, "arc")
    assert len(out) == 2
    assert all(c["program"].startswith("def transform") and c["pred"] is None for c in out)
    assert out[0]["text"] == out[0]["program"]
    assert run_card.parse_candidates("def transform(g): return g", "arc") == []


def test_parse_bt_letters_and_choice_text():
    text = ("1. B. The driver is the reader because the question says so.\n2. Option C\n3. **A**\n"
            "4. Whatever colour your eyes are\n5. no letter here")
    out = run_card.parse_candidates(text, "bt", BT_ITEM["choices"])
    assert [c["pred"] for c in out] == ["B", "C", "A", "B"]
    assert out[0]["text"] == "B. The driver is the reader."     # A9: first-sentence rationale stripped
    assert out[1]["text"] == "C" and out[0]["program"] is None


def test_post_check_bt_strips_justification_and_caps():
    t = "The man is bald. This works because he has no hair. He walks home. Since then, fine."
    assert run_card.post_check(t, "bt") == "The man is bald. He walks home."
    long = "word " * 100
    assert len(run_card.post_check(long, "bt")) <= run_card.MAX_BT_CHARS
    assert run_card.post_check("x" * (run_card.MAX_PROGRAM_CHARS + 1), "arc") is None


def test_parse_bt_applies_post_check():
    out = run_card.parse_candidates(BT_GEN, "bt")
    assert out[1]["text"] == "C. It is a guess." and out[1]["pred"] == "C"
    assert run_card.post_check("because it rains", "bt") == ""
    assert [c["pred"] for c in out] == ["B", "C", "A"]


# ---------------------------------------------------------------- encode
def test_encode_arc_files_and_bar(tmp_path, calls):
    p, run_dir = _encode(ARC_ITEM, tmp_path)
    for f in ("problem.md", "constraints.json", "private/defaults.json", "private/noun_map.json",
              "variants/canonical.md", "variants/shuffled.md", "variants/low_prior.md", "encode.json"):
        assert (run_dir / f).exists(), f
    c = read_json(run_dir / "constraints.json")
    assert c["bar"] == {"required_verification": "demo_match", "all_items": True}
    assert c["checklist"][0] == encode.BASE_CONSTRAINT["arc"] and c["checklist"] == p.checklist
    d = read_json(run_dir / "private" / "defaults.json")
    assert len(d["answers"]) == 5 and DEFAULT_SENTINEL in d["answers"][0]
    assert "test_output" not in p.item and p.goal == "Find the rule."
    roles = [c["role"] for c in calls]
    assert roles == ["encode", "encode", "defaults"]          # identical checklists: no resolve
    def _rec(cid):   # the defaults call is a private role: its record lives under private/calls/
        return read_json(run_dir / "calls" / f"{cid}.json") or read_json(run_dir / "private" / "calls" / f"{cid}.json")
    logged = sum(_rec(cid)["total_tokens"] for cid in p.meta["encode"]["call_ids"])
    assert p.encode_tokens == logged > 0
    assert (run_dir / "private" / "calls" / f"{p.meta['encode']['call_ids'][-1]}.json").exists()
    assert not (run_dir / "calls" / f"{p.meta['encode']['call_ids'][-1]}.json").exists()
    # the defaults reply is in no run file outside private/
    for f in run_dir.rglob("*"):
        if f.is_file() and "private" not in f.parts:
            assert DEFAULT_SENTINEL not in f.read_text(encoding="utf-8"), f
    assert "red" not in p.views["low_prior"] and "cell" not in p.views["low_prior"]
    assert p.meta["low_prior_lint"] == []
    assert "Example 1 input:\n10\n00" in p.views["canonical"]
    assert p.views["shuffled"].index("## Goal") > p.views["shuffled"].index("Facts:")


def test_encode_resolves_on_disagreement(tmp_path):
    log: list = []
    other = ENC_ARC.split("CHECKLIST:")[0] + "CHECKLIST:\n1. Colours never change.\n2. Shapes stay whole.\n"
    llm.set_mock(responder(log, encode_b=other))
    try:
        p, run_dir = _encode(ARC_ITEM, tmp_path)
    finally:
        llm.set_mock(None)
    assert [c["meta"].get("purpose") for c in log] == ["encode_a", "encode_b", "resolve", "defaults"]
    assert "Resolved constraint one." in p.checklist and p.meta["encode"]["resolved"] is True
    assert p.meta["encode"]["disagreement"] > 0.5


def test_encode_cap_skips_resolve(tmp_path, monkeypatch):
    log: list = []
    other = ENC_ARC.split("CHECKLIST:")[0] + "CHECKLIST:\n1. Colours never change.\n"
    monkeypatch.setitem(config.PARAMS, "max_tokens", dict(config.PARAMS["max_tokens"], plain=1))
    llm.set_mock(responder(log, encode_b=other))
    try:
        p, _ = _encode(ARC_ITEM, tmp_path)
    finally:
        llm.set_mock(None)
    assert p.meta["encode"]["cap_hit"] is True
    assert [c["role"] for c in log] == ["encode", "encode", "defaults"]


def test_merge_checklists_normalizes():
    merged, d = encode.merge_checklists(["The answer is one option.", "Keep size."],
                                        ["the answer is one option", "Colours fixed."])
    assert merged == ["The answer is one option.", "Keep size.", "Colours fixed."]
    assert d == pytest.approx(2 / 3)


def test_encode_bt_low_prior_view(tmp_path, calls):
    p, run_dir = _encode(BT_ITEM, tmp_path)
    lp = p.views["low_prior"]
    for noun in ("lantern", "driver", "bus"):
        assert noun not in lp.lower()
    assert "X1" in lp and p.meta["low_prior_lint"] == []
    assert read_json(run_dir / "constraints.json")["bar"]["required_verification"] == "agreement"
    assert read_json(run_dir / "private" / "defaults.json")["answers"] == ["B"] * 5
    assert "A. Blue" in p.views["canonical"]


# ---------------------------------------------------------------- cards
def test_seeded_card_bt(tmp_path, calls):
    p, run_dir = _encode(BT_ITEM, tmp_path)
    r = _run(CardSpec(card="seeded", seed="anvil"), p, run_dir)
    prompt = calls[-1]["prompt"]
    assert prompt.count("anvil") == 1 and "Starting point: anvil\n" in prompt
    assert calls[-1]["role"] == "generate"
    assert [c.pred for c in r.cands] == ["B", "C", "A"]
    assert all(c.card == "seeded" and c.seed == "anvil" and c.perm == p.meta["shuffled_perm"] for c in r.cands)
    assert r.contract == {"id": r.call_ids[0], "path": str(run_dir / "cands" / f"{r.call_ids[0]}.jsonl"),
                          "n_cands": 3}
    assert len(read_jsonl(Path(r.contract["path"]))) == 3
    assert (run_dir / "prompts" / f"{r.call_ids[0]}.txt").read_text(encoding="utf-8") == prompt
    assert (run_dir / "calls" / r.call_ids[0] / "in" / "seed.txt").exists()


def test_seed_and_operator_are_scripted(tmp_path, calls):
    p, _ = _encode(BT_ITEM, tmp_path)
    s1 = run_card.pick_seed(CardSpec(card="seeded"), p, 0, 1)
    assert s1 == run_card.pick_seed(CardSpec(card="seeded"), p, 0, 1) and s1 in run_card.load_seeds()
    card = run_card.load_card("transform")
    op = run_card.pick_operator(card, CardSpec(card="transform"), p, 0, 1)
    assert op in ("drop", "negate", "vary", "oppose")
    assert run_card.pick_operator(card, CardSpec(card="transform", operator="vary"), p, 0, 1) == "vary"


def test_low_prior_card_has_no_domain_nouns(tmp_path, calls):
    p, run_dir = _encode(BT_ITEM, tmp_path)
    r = _run(CardSpec(card="low_prior"), p, run_dir)
    prompt = calls[-1]["prompt"].lower()
    assert "lantern" not in prompt and "driver" not in prompt and "x1" in prompt
    assert r.cands and all(c.extra["variant"] == "low_prior" for c in r.cands)


def test_transform_card_dag(tmp_path, calls):
    p, run_dir = _encode(BT_ITEM, tmp_path)
    n0 = len(calls)
    r = _run(CardSpec(card="transform", operator="negate"), p, run_dir)
    steps = calls[n0:]
    assert [c["role"] for c in steps] == ["transform", "generate", "generate"]
    assert "negate:" in steps[0]["prompt"]
    solver = steps[1]["prompt"]
    assert solver.startswith("TRANSFORMEDMARK") and "lantern" not in solver and "Starting point" not in solver
    assert "fix:" in steps[2]["prompt"] and "lantern" in steps[2]["prompt"]
    assert "No feedback record." in steps[2]["prompt"]
    solver_ids = [c.id for c in r.cands if c.extra["step"] == "solver"]
    revised = [c for c in r.cands if c.extra["step"] == "revise"]
    # step 3 gets one scripted parent (Pr18): the first solver candidate
    assert solver_ids and revised and all(c.parent_ids == solver_ids[:1] for c in revised)
    assert len(r.call_ids) == 3 and r.contract["n_cands"] == len(r.cands)
    assert list((run_dir / "variants").glob("transformed_*.md"))


def test_formal_card_arc(tmp_path, calls):
    p, run_dir = _encode(ARC_ITEM, tmp_path)
    r = _run(CardSpec(card="formal"), p, run_dir)
    prompt = calls[-1]["prompt"]
    assert "Example 1 input = [[1, 0], [0, 0]]" in prompt and "transform(grid) -> grid" in prompt
    assert len(r.cands) == 2 and all(c.program and c.pred is None for c in r.cands)
    meta = read_json(run_dir / "calls" / f"{r.call_ids[0]}.json")
    assert meta["meta"]["card"] == "formal"
    pb, rb = _encode(BT_ITEM, tmp_path)
    with pytest.raises(CardError):
        _run(CardSpec(card="formal"), pb, rb)


def test_revise_card_arc(tmp_path, calls):
    p, run_dir = _encode(ARC_ITEM, tmp_path)
    parent = Candidate(id="par1", text="def transform(grid):\n    return grid", card="seeded",
                       operator="none", seed="", perm=0, round=1, call_id="c0", lineage_id="root0",
                       program="def transform(grid):\n    return grid")
    fb = {"failing_pairs": [{"pair": 0, "diff": "cell (0,0)"}]}
    r = _run(CardSpec(card="revise", operator="specialize"), p, run_dir, round_no=2, parent=parent, feedback=fb)
    prompt = calls[-1]["prompt"]
    assert "```python\ndef transform(grid):\n    return grid\n```" in prompt
    assert "failing_pairs" in prompt and "specialize:" in prompt
    assert all(c.parent_ids == ["par1"] and c.lineage_id == "root0" and c.round == 2 for c in r.cands)
    with pytest.raises(CardError):
        _run(CardSpec(card="revise"), p, run_dir)


def test_converter_runs_once_on_parse_failure(tmp_path):
    log: list = []
    llm.set_mock(responder(log, generate={"seeded": "I would go with the second one, B, I think."}))
    try:
        p, run_dir = _encode(BT_ITEM, tmp_path)
        r = _run(CardSpec(card="seeded"), p, run_dir)
    finally:
        llm.set_mock(None)
    assert [c["role"] for c in log].count("converter") == 1
    assert "I would go with the second one" in log[-1]["prompt"]
    assert [c.pred for c in r.cands] == ["B"] and len(r.call_ids) == 2


def test_no_private_key_or_graph_content_reaches_prompts(tmp_path, calls):
    for item, cards in ((ARC_ITEM, ["seeded", "low_prior", "transform", "formal"]),
                        (BT_ITEM, ["seeded", "low_prior", "transform"])):
        p, run_dir = _encode(item, tmp_path)
        for f in ("graph.jsonl", "clusters.jsonl", "private/extra.json"):
            (run_dir / f).parent.mkdir(parents=True, exist_ok=True)
            (run_dir / f).write_text(json.dumps({"x": PLANTED}), encoding="utf-8")
        for name in cards:
            _run(CardSpec(card=name), p, run_dir)
        if item["benchmark"] == "arc":
            par = Candidate(id="p", text="def transform(g):\n    return g", card="seeded", operator="none",
                            seed="", perm=0, round=1, call_id="c", program="def transform(g):\n    return g")
            _run(CardSpec(card="revise"), p, run_dir, round_no=2, parent=par, feedback={"d": 1})
        texts = _prompts(run_dir) + [f.read_text(encoding="utf-8") for f in (run_dir / "calls").glob("*/in/*")]
        gen_texts = [c["prompt"] for c in calls if c["role"] not in ("encode", "defaults")]
        assert texts and gen_texts
        for t in texts:
            assert PLANTED not in t and "SENTINELKEYTEXT" not in t
            assert not any(k in t for k in ARC_KEY_STRINGS)
        for t in gen_texts:
            assert DEFAULT_SENTINEL not in t
        for name in ("problem.md", "constraints.json", "variants/canonical.md", "variants/low_prior.md"):
            body = (run_dir / name).read_text(encoding="utf-8")
            assert not any(k in body for k in ARC_KEY_STRINGS) and "SENTINELKEYTEXT" not in body
        routed = {i for r in read_jsonl(run_dir / "routing.jsonl") for i in r.get("inputs", [])}
        assert routed <= {"problem", "checklist_a", "checklist_b", "goal", "facts", "resources",
                          "constraints", "operator", "seed", "parent", "feedback", "format",
                          "transformed", "raw"}


def test_run_card_rejects_keyed_problem(tmp_path, calls):
    p, run_dir = _encode(ARC_ITEM, tmp_path)
    p.item = dict(ARC_ITEM)
    with pytest.raises(CardError):
        _run(CardSpec(card="seeded"), p, run_dir)
