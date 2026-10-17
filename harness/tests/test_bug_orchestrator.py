"""Bug pass 2026-10-17 (night), orchestrator area. Mock backend, temp lab root, no model calls."""
from __future__ import annotations

from pathlib import Path
from types import SimpleNamespace

import test_think as tt
from test_think import lab_root, stubs  # noqa: F401 - fixtures

from harness import encode, lint
from harness.schemas import Candidate, VerifyResult
from harness.think import admit

think = tt.think


def _cand(cid, pred, origin="spoken"):
    return Candidate(id=cid, text="t", card="probe" if origin == "probe" else "seeded",
                     operator="none", seed="s", perm=0, round=0, call_id="c",
                     program=f"def transform(g):\n    return {pred!r}\n", pred=pred, origin=origin)


def _ctx(probe_cands):
    return SimpleNamespace(benchmark="arc", P=SimpleNamespace(bar={"all_items": True}, item={}),
                           V=SimpleNamespace(type="demo_match"), probe=SimpleNamespace(cands=probe_cands),
                           header={"select": {"HTSA_SELECT": "vote"}}, run_dir=Path("."), run_id="r",
                           batch="b", item_id="i", split="dev-tune", family="arc", cls="arc",
                           arm="scaffold", snapshot_hash=None, run_instance="x")


def _verified_state():
    good = _cand("g", [[1]])
    st = think.State(all_cands=[good])
    st.vres = {"g": VerifyResult(id="g", status="verified", verification_type="demo_match",
                                 partial_score=1.0, details={"checklist": {"c1": True}})}
    return st


def test_vote_survives_verify_raising_on_a_probe_candidate(stubs):  # noqa: F811
    """A probe candidate whose verify.run raises must not crash _final (the run would end
    with no answer.json and no runs.jsonl row); it is skipped and logged in st.errors."""
    st = _verified_state()

    def v_run(cand, handle, *, attempts, benchmark, agreement, run_dir):
        raise OSError("sandbox folder vanished")
    stubs.mods["verify"].run = v_run
    c, k, n = think._vote_verified(_ctx([_cand("p1", [[2]], "probe")]), st)
    assert c is not None and c.id == "g" and (k, n) == (1, 1)
    assert any("p1" in str(e) for e in st.errors)


def test_vote_with_probe_without_cands(stubs):  # noqa: F811
    st = _verified_state()
    c, k, n = think._vote_verified(_ctx([]), st)
    assert c.id == "g" and (k, n) == (1, 1)


def test_neutralize_keeps_function_words_readable():
    """A plural noun must not reduce to a function word ("bees" -> "be", "notes" -> "not",
    "canes" -> "can", "toes" -> "to") that neutralize then replaces everywhere."""
    noun_map = {"bees": "X1", "notes": "X2", "canes": "X3", "toes": "X4"}
    text = "It must be one of the notes, not the canes; we can see bees next to the toes."
    out = encode.neutralize(text, noun_map)
    assert out == "It must be one of the X2, not the X3; we can see X1 next to the X4."
    assert encode.neutralize("a bee, a note, a cane and a toe", noun_map) == "a X1, a X2, a X3 and a X4"


def test_lint_domain_does_not_flag_function_words():
    nouns = ["bees", "notes", "canes", "toes"]
    assert lint.lint_domain("It must be one of them, not that; we can go to it.", nouns) == []
    hits = {f["match"] for f in lint.lint_domain("a bee, a note, canes, toes", nouns)}
    assert hits == {"bee", "note", "canes", "toes"}


def test_plural_rules_still_cover_sibilant_and_o_stems():
    forms = (lint.plural_forms("box") | lint.plural_forms("bus") | lint.plural_forms("church")
             | lint.plural_forms("hero"))
    assert {"boxes", "buses", "churches", "heroes"} <= forms
    assert "box" in lint.base_forms("boxes") and "hero" in lint.base_forms("heroes")


def test_admit_threshold_has_the_float_tolerance():
    """theta_admit is one of think.THRESHOLDS, compared with a 1e-9 tolerance everywhere else."""
    a, b = _cand("a", [[1]]), _cand("b", [[2]])
    theta = 2 / 3
    pop = admit.update([], [a, b], {"a": theta - 1e-12, "b": 0.1}, set(), 5, theta)
    assert [c.id for c in pop] == ["a"]
