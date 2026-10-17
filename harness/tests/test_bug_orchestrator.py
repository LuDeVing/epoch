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


# ---------------------------------------------------------------- coordinator follow-up
import json  # noqa: E402
import os  # noqa: E402

import pytest  # noqa: E402

from harness import config, data  # noqa: E402
from harness import encode as encode_mod  # noqa: E402
from harness.schemas import read_json, write_json  # noqa: E402
from harness.think import dedup  # noqa: E402


def test_dedup_vote_weights_groups():
    pred = {"a": [[1]], "b1": [[2]], "b2": [[2]]}
    w = {"a": 3, "b1": 1, "b2": 1}
    assert dedup.vote(["a", "b1", "b2"], pred.get, len, None, w.get) == ("a", 3, 2)
    assert dedup.vote(["a", "b1", "b2"], pred.get, len)[:2] == ("b1", 2)    # default weight 1


def test_dedup_records_cluster_members_and_vote_counts_them(monkeypatch):
    """Same-grid candidates dropped by dedup are the same answer: the vote counts them."""
    monkeypatch.setattr(think, "_MODS", {"dedup": dedup, "arc_exec": SimpleNamespace()})
    g, d1, d2, h = _cand("g", [[1]]), _cand("d1", [[1]]), _cand("d2", [[1]]), _cand("h", [[2]])
    st = think.State()
    st.vres = {x: VerifyResult(id=x, status="fail", verification_type="demo_match") for x in ("d1", "d2")}
    p = _cand("p1", [[2]], "probe")
    ctx = _ctx([p])
    ctx.flags = {"dedup": True}
    ctx.run_dir = Path(config.RUNS_DIR) / "r"
    kept, _ = think._dedup(ctx, st, [g, d1, d2, h])
    assert [c.id for c in kept] == ["g", "h"]
    st.all_cands = kept
    ok = {"checklist": {"c1": True}}
    st.vres = {x: VerifyResult(id=x, status="verified", verification_type="demo_match",
                               partial_score=1.0, details=ok) for x in ("g", "h", "p1")}
    c, k, n = think._vote_verified(ctx, st)     # [[1]]: g + 2 dropped = 3; [[2]]: h + probe = 2
    assert c.id == "g" and (k, n) == (3, 2)


def _stale_dir(rid):
    rd = Path(config.RUNS_DIR) / rid
    rd.mkdir(parents=True)
    write_json(rd / "state.json", {})
    return rd


def test_force_refuses_to_delete_a_live_run(monkeypatch):
    item = tt.arc_item("t_force")
    monkeypatch.setattr(data, "get_item", lambda b, i: dict(item))
    rid = think.make_run_id("tc_force", "arc", item["id"], "scaffold", 0)
    rd = _stale_dir(rid)
    write_json(rd / think.LOCK_NAME, {"pid": 12345})
    monkeypatch.setattr(think, "_pid_alive", lambda pid: True)
    with pytest.raises(SystemExit, match="live"):
        think.main(["--benchmark", "arc", "--item", item["id"], "--batch", "tc_force", "--force"])
    assert (rd / "state.json").exists()


@pytest.mark.parametrize("body", ['{"pid": 12', '{"pid": "x"}', "[1, 2]"])
def test_unparsable_lock_is_stale(body):
    rid = "tc_torn__arc__i__scaffold__r0"
    rd = _stale_dir(rid)
    (rd / think.LOCK_NAME).write_text(body, encoding="utf-8")
    think._make_run_dir(rid, "inst")
    try:
        assert list(rd.parent.glob(f"{rid}.old-*"))
        assert read_json(rd / think.LOCK_NAME)["pid"] == os.getpid()
    finally:
        think._release(rid, rd)


def test_cli_env_flags_are_honoured_and_recorded(stubs):  # noqa: F811
    seen = []
    orig = stubs.mods["encode"].encode

    def enc(*a, **k):
        seen.append(encode_mod.raw_view())
        return orig(*a, **k)
    stubs.mods["encode"].encode = enc
    item = tt.arc_item("t_envflag")
    think.think(item, m=20, replicate=0, backend="mock", batch="tc_envflag",
                flags={"raw_view": True, "experimental_think_aloud_self_check": "1"})
    assert seen == [True] and not config.FLAGS["raw_view"] and encode_mod.raw_view() is False
    recs = [json.loads(p.read_text(encoding="utf-8"))
            for p in (tt.run_dir_of("tc_envflag", item) / "calls").glob("*.json")]
    assert [r for r in recs if r["role"] == "generate"]
    for r in recs:     # encode, probe and the card calls made on spawn threads
        assert r["flags"] == {"raw_view": True, "experimental_think_aloud_self_check": "1"}
