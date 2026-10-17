"""Fix pass 2026-10-17, section A (card executor and verification layer). Mock backend only;
every run folder is under tmp_path."""
from __future__ import annotations

import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path

os.environ.setdefault("HTSA_LAB_ROOT", tempfile.mkdtemp(prefix="htsa_fixcards_"))

import pytest  # noqa: E402

from harness import config, encode, judge, lint, llm, probe, run_card, verify  # noqa: E402
from harness.run_card import CardSpec  # noqa: E402
from harness.schemas import Candidate, read_jsonl  # noqa: E402

ARC_ITEM = {
    "id": "arc_f1", "benchmark": "arc", "train": [{"input": [[1, 2]], "output": [[2, 1]]},
                                                   {"input": [[3, 4]], "output": [[4, 3]]}],
    "test_input": [[5, 6]], "test_output": [[6, 5]],
}
FLIP = "def transform(grid):\n    return [row[::-1] for row in grid]\n"
BT_ITEM = {
    "id": "bt_f1", "benchmark": "bt",
    "question": "Two men and three cities: a man leaves his city. Which option is right?",
    "choices": ["The ferries stop", "The wolves run", "Both", "None"], "label": 2,
}
ENC_BT = ("GOAL: Choose the option.\nFACTS:\n1. Two men leave their cities.\n2. The ferries stop.\n"
          "RESOURCES:\n1. The options.\nCHECKLIST:\n1. The answer must be one option.\n"
          "NOUNS:\nman\ncity\nferry\nwolf\n")


@pytest.fixture(autouse=True)
def _reset():
    yield
    llm.set_mock(None)


def _mock(log=None, enc=ENC_BT, gen="1. B. The wolves run.\n2. C"):
    def fn(prompt, role, meta):
        if log is not None:
            log.append({"role": role, "prompt": prompt, "meta": dict(meta)})
        if role == "encode":
            return enc
        if role == "defaults":
            return "1. A\n2. A\n3. A\n4. A\n5. A"
        return gen
    llm.set_mock(fn)


def _encode(item, tmp_path):
    run_dir = tmp_path / item["id"]
    return encode.encode(item, run_dir, backend="mock", replicate=0, log_dir=run_dir / "calls"), run_dir


# ---------------------------------------------------------------- A1 low_prior domain lint
def test_lint_domain_catches_irregular_plurals_and_possessives():
    text = "Two men walked to the cities; the wolves' den; a ferry's deck; drivers' seats."
    hits = {f["match"].lower() for f in lint.lint_domain(text, ["man", "city", "wolf", "ferry", "driver"])}
    assert {"men", "cities", "wolves", "ferry", "drivers"} <= hits
    assert lint.lint_domain("X1 and X2 and a woman", ["man"]) == []      # "woman" is not "man"


def test_lint_domain_is_independent_of_neutralize():
    """A neutralizer with the old simple-plural regex leaks "men" and "cities"; the lint must
    see it (it used to share that regex, so it could never fail)."""
    old = {"man": "X1", "city": "X2"}
    leaked = "Two men leave their cities. A man stays."
    import re
    for noun, tok in old.items():
        leaked = re.compile(r"\b" + re.escape(noun) + r"(?:s|es)?\b", re.I).sub(tok, leaked)
    assert "men" in leaked and "cities" in leaked
    found = lint.lint_domain(leaked, list(old))
    assert {f["match"] for f in found} == {"men", "cities"}
    # the fixed neutralizer replaces every form
    assert lint.lint_domain(encode.neutralize("Two men leave their cities.", old), list(old)) == []


def test_low_prior_view_and_prompt_have_no_domain_nouns(tmp_path):
    log: list = []
    _mock(log)
    p, run_dir = _encode(BT_ITEM, tmp_path)
    lp = p.views["low_prior"].lower()
    for w in ("men", "man", "cities", "city", "ferries", "wolves"):
        assert f" {w} " not in f" {lp} ".replace(".", " ").replace(",", " ").replace(":", " ")
    assert p.meta["low_prior_lint"] == [] and p.meta["domain_nouns"]
    r = run_card.run_card(CardSpec(card="low_prior"), p, run_dir, backend="mock", round_no=1,
                          log_dir=run_dir / "calls", replicate=0)
    assert r.cands and lint.lint_domain(log[-1]["prompt"], p.meta["domain_nouns"]) == []


def test_low_prior_prompt_blocks_on_a_leaked_noun(tmp_path, monkeypatch):
    """With neutralize broken, the leaked nouns reach the routed view; the rendered-prompt
    lint against the original item's nouns must block the call."""
    log: list = []
    _mock(log)
    monkeypatch.setattr(encode, "neutralize", lambda text, noun_map: text)
    p, run_dir = _encode(BT_ITEM, tmp_path)
    assert p.meta["low_prior_lint"]                        # the view lint sees the leak too
    n_before = len(log)
    with pytest.raises(run_card.LintError):
        run_card.run_card(CardSpec(card="low_prior"), p, run_dir, backend="mock", round_no=1,
                          log_dir=run_dir / "calls", replicate=0)
    assert len(log) == n_before                            # no model call was made
    rows = read_jsonl(run_dir / "prompts" / "lint.jsonl")
    assert rows[-1]["blocked"] and any(f["pattern"].startswith("domain_noun:") for f in rows[-1]["findings"])


def test_bt_fallback_nouns_include_choices():
    item = {"benchmark": "bt", "question": "Who wins?", "choices": ["The lantern", "A kettle"]}
    nouns = encode.domain_nouns([], item)
    assert "lantern" in nouns and "kettle" in nouns


# ---------------------------------------------------------------- A2 timeouts
def test_timeout_charged_at_real_cap_and_retried_once(monkeypatch):
    monkeypatch.setattr(llm.time, "sleep", lambda s: None)
    n = {"k": 0}

    def fake_cli(prompt, model_id, max_tokens, cwd, timeout, max_turns, tools=None, effort=None):
        n["k"] += 1
        raise llm.CallError("Timeout after 1s (process tree killed)", estimated=True)
    monkeypatch.setattr(llm, "_call_cli", fake_cli)
    res = llm.call("x" * 400, role="judge", backend="cli_json", max_tokens=1500, retries=2)
    assert n["k"] == 2 and res.attempts == 2 and res.usage_estimated
    per = 100 + config.CLI_OVERHEAD_TOKENS_EST + llm.output_cap(1500, "cli_json")
    assert res.usage.total_tokens == 2 * per and llm.output_cap(1500, "cli_json") == 32000
    assert "retried once" in res.retry_reasons[0] and "not retried" in res.retry_reasons[1]


def test_judge_est_cost_reserves_the_real_cap():
    class P:
        benchmark, item_id, problem_md = "bt", "x", "# Problem"
        item = {"benchmark": "bt", "question": "q?", "choices": ["a", "b", "c", "d"]}
    c = Candidate(id="k1", text="A", card="seeded", operator="none", seed="", perm=0, round=1, call_id="c")
    est = judge.est_cost([c], P(), "cli_json")
    assert est >= llm.output_cap(config.PARAMS["max_tokens"]["judge"], "cli_json") + config.CLI_OVERHEAD_TOKENS_EST
    assert judge.est_cost([c], P(), "mock") < est


# ---------------------------------------------------------------- A3 cwd of judge and probe calls
def test_judge_and_probe_calls_run_in_their_sandbox(tmp_path, monkeypatch):
    _mock()
    p, run_dir = _encode(BT_ITEM, tmp_path)
    seen = []
    real = llm.call

    def spy(prompt, **kw):
        seen.append((kw.get("role"), kw.get("cwd")))
        return real(prompt, **kw)
    monkeypatch.setattr(llm, "call", spy)
    c = Candidate(id="k1", text="B", card="seeded", operator="none", seed="", perm=0, round=1, call_id="c")
    judge.judge([c], p, backend="mock", log_dir=run_dir / "calls", replicate=0, run_dir=run_dir)
    probe.run_probe(p, n=2, backend="mock", log_dir=run_dir / "calls", replicate=0, run_dir=run_dir)
    assert {r for r, _ in seen} == {"judge", "probe"}
    for role, cwd in seen:
        assert cwd is not None and Path(cwd).parent.parent == run_dir / "calls" and Path(cwd).name == "in"
        assert Path(cwd).is_dir() and Path.cwd().resolve() not in Path(cwd).resolve().parents
    assert judge.resolve_run_dir(None, run_dir / "calls") == run_dir
    assert judge.resolve_run_dir(None, tmp_path / "logs") is None


# ---------------------------------------------------------------- A4 checklist half of the bar
def test_verify_writes_a_checklist_for_every_item(tmp_path):
    class P:
        item = ARC_ITEM
        checklist = [encode.BASE_CONSTRAINT["arc"], "The output has the input size."]
    h = verify.build(P(), "arc")
    c = Candidate(id="k1", text=FLIP, card="formal", operator="none", seed="", perm=0, round=1,
                  call_id="c", program=FLIP)
    r = verify.run(c, h, attempts=1, benchmark="arc", agreement=None, run_dir=tmp_path)
    assert r.status == "verified" and r.details["checklist"] == {"c1": True, "c2": True}
    assert set(r.details["checklist_basis"]) == {"c1", "c2"}
    bad = Candidate(id="k2", text="x", card="formal", operator="none", seed="", perm=0, round=1,
                    call_id="c", program="def transform(grid):\n    return grid\n")
    r = verify.run(bad, h, attempts=1, benchmark="arc", agreement=None, run_dir=tmp_path)
    assert r.details["checklist"] == {"c1": False, "c2": False}
    b = Candidate(id="k3", text="B", card="seeded", operator="none", seed="", perm=0, round=1,
                  call_id="c", pred="B")
    rb = verify.run(b, verify.build(BT_ITEM, "bt"), attempts=1, benchmark="bt", agreement=1.0, run_dir=tmp_path)
    assert rb.details["checklist"] == {"c1": True}
    assert "P1" in verify.__doc__ and "perturbation" in verify.__doc__


# ---------------------------------------------------------------- A5 env toggles are flags
def test_env_toggles_are_flags_and_recorded(tmp_path, monkeypatch):
    assert "raw_view" in config.FLAGS and "experimental_think_aloud_self_check" in config.FLAGS
    assert config.FLAGS["experimental_think_aloud_self_check"] in ("off", "1", "2")
    res = llm.call("hi", role="generate", backend="mock", log_dir=tmp_path)
    rec = json.loads((tmp_path / f"{res.call_id}.json").read_text(encoding="utf-8"))
    assert set(rec["flags"]) == {"raw_view", "experimental_think_aloud_self_check"}
    assert run_card.format_text("arc", 2, {"experimental_think_aloud_self_check": "off"}) == \
        run_card.format_text("arc", 2, {})
    assert "Work it out in writing" in run_card.format_text("arc", 2, {"experimental_think_aloud_self_check": "1"})
    monkeypatch.setitem(config.FLAGS, "raw_view", True)
    _mock()
    p, _ = _encode(BT_ITEM, tmp_path)
    assert p.views["low_prior"] == p.views["canonical"]


# ---------------------------------------------------------------- A6 / A9 BT parsing
def test_article_is_not_an_option_letter():
    choices = ["Blue", "Red", "Green", "None"]
    assert run_card._bt_item("A man carries a lantern onto the bus.", choices) is None
    assert run_card._bt_item("A. Blue", choices)["pred"] == "A"
    assert run_card._bt_item("(A) man", choices)["pred"] == "A"
    assert run_card._bt_item("Option A is right", choices)["pred"] == "A"
    assert run_card._bt_item("C because green is common.", choices)["pred"] == "C"
    assert run_card._bt_item("Green", choices)["pred"] == "C"


def test_first_sentence_rationale_is_stripped():
    out = run_card.parse_candidates("1. B. The driver is the reader because the question says so.", "bt")
    assert out[0]["text"] == "B. The driver is the reader." and "because" not in out[0]["text"]
    assert run_card.post_check("Bald, since he has no hair. Fine.", "bt") == "Bald. Fine."


# ---------------------------------------------------------------- A7 verifier hash
def test_hash_covers_test_input_and_checklist(tmp_path):
    h = verify.build(ARC_ITEM, "arc")
    assert verify.check_hash(h)
    h.data["test_input"] = [[9, 9]]
    assert not verify.check_hash(h)
    c = Candidate(id="k1", text=FLIP, card="formal", operator="none", seed="", perm=0, round=1,
                  call_id="c", program=FLIP)
    r = verify.run(c, h, attempts=1, benchmark="arc", agreement=None, run_dir=tmp_path)
    assert r.status == "unverified" and r.details["hash_mismatch"] and c.pred is None
    h2 = verify.build(ARC_ITEM, "arc")
    h2.data["checklist"] = ["anything goes"]
    assert not verify.check_hash(h2)


# ---------------------------------------------------------------- A8 long prompts
def test_long_prompt_cut_in_middle_and_recorded(tmp_path, monkeypatch):
    monkeypatch.setattr(config, "MAX_PROMPT_CHARS", 500)
    sent = []
    llm.set_mock(lambda p, r, m: sent.append(p) or "ok")
    prompt = "HEAD" + "x" * 2000 + "TAIL format instruction"
    res = llm.call(prompt, role="generate", backend="mock", log_dir=tmp_path)
    assert len(sent[0]) <= 500 and sent[0].startswith("HEAD") and sent[0].endswith("TAIL format instruction")
    assert "characters removed here by the harness" in sent[0]
    rec = json.loads((tmp_path / f"{res.call_id}.json").read_text(encoding="utf-8"))
    assert rec["prompt_truncated"]["original_chars"] == len(prompt)


def test_prompt_file_matches_what_was_sent(tmp_path, monkeypatch):
    log: list = []
    _mock(log)
    p, run_dir = _encode(BT_ITEM, tmp_path)
    monkeypatch.setattr(config, "MAX_PROMPT_CHARS", 300)
    r = run_card.run_card(CardSpec(card="seeded", seed="anvil"), p, run_dir, backend="mock", round_no=1,
                          log_dir=run_dir / "calls", replicate=0)
    cid = r.call_ids[0]
    assert (run_dir / "prompts" / f"{cid}.txt").read_text(encoding="utf-8") == log[-1]["prompt"]
    assert any(row.get("prompt_truncated") for row in read_jsonl(run_dir / "routing.jsonl"))


# ---------------------------------------------------------------- A11 lint blocks mid-card
def test_lint_error_mid_card_blocks_the_card(tmp_path, monkeypatch):
    log: list = []
    _mock(log, gen="TRANSFORMED PROBLEM:\na new problem")
    p, run_dir = _encode(BT_ITEM, tmp_path)
    real = run_card.load_template

    def bad_second(name):
        text = real(name)
        return text + "\nBe creative." if name == "transform.solver" else text
    monkeypatch.setattr(run_card, "load_template", bad_second)
    r = run_card.run_card(CardSpec(card="transform", operator="vary"), p, run_dir, backend="mock",
                          round_no=1, log_dir=run_dir / "calls", replicate=0)
    assert r.contract.get("lint_blocked") and "LintError" in r.contract["error"]
    assert r.cands == [] and r.call_ids and r.usage.total_tokens > 0     # spend still returned


# ---------------------------------------------------------------- A13 config import, seeds
def test_config_import_does_not_create_the_lab_root(tmp_path):
    root = tmp_path / "no_such_lab"
    env = dict(os.environ, HTSA_LAB_ROOT=str(root))
    code = "import harness.config as c; print(c.RUNS_DIR)"
    out = subprocess.run([sys.executable, "-c", code], cwd=str(config.PROJECT_ROOT), env=env,
                         capture_output=True, text=True, timeout=120)
    assert out.returncode == 0, out.stderr
    assert not root.exists()


def test_seed_loaders_agree_on_comments(tmp_path, monkeypatch):
    f = tmp_path / "seeds.txt"
    f.write_text("# a comment\nriver\n\n  # another\nmirror\n", encoding="utf-8")
    monkeypatch.setattr(config, "SEEDS_PATH", f)
    run_card.load_seeds.cache_clear()
    try:
        assert list(run_card.load_seeds()) == probe.load_seeds() == ["river", "mirror"]
    finally:
        run_card.load_seeds.cache_clear()


# ---------------------------------------------------------------- E4 creativity instructions fail
def test_creativity_instructions_fail_and_templates_pass():
    sev = {f["pattern"]: f["severity"] for f in lint.lint_text(
        "Be creative. Think outside the box. Think creatively.")}
    assert sev == {"creative_be_creative": "fail", "creative_outside_box": "fail",
                   "creative_creatively": "fail"}
    assert lint.lint_templates()["fails"] == []


def test_encode_docstring_states_the_cap():
    assert "32000" in encode.encode.__doc__ and "resolve" in encode.encode.__doc__
