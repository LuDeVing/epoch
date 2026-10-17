"""Tests for arc_exec.py, verify.py and feedback.py (owner: verify). No model calls."""
from __future__ import annotations

import os
import tempfile

os.environ.setdefault("HTSA_LAB_ROOT", tempfile.mkdtemp(prefix="htsa_lab_"))
os.environ.setdefault("HTSA_BACKEND", "mock")

import json  # noqa: E402

import pytest  # noqa: E402

from harness import arc_exec, feedback, verify  # noqa: E402
from harness.schemas import Candidate, read_jsonl  # noqa: E402

FLIP = "def transform(grid):\n    return [row[::-1] for row in grid]\n"
IDENT = "def transform(grid):\n    return [row[:] for row in grid]\n"
CRASH = "def transform(grid):\n    return 1 // 0\n"
LOOP = "def transform(grid):\n    while True:\n        pass\n"
NOISY = "import sys\nprint('hello')\ndef transform(grid):\n    print('x' * 1000)\n    return [row[::-1] for row in grid]\n"

ITEM = {"id": "t1", "benchmark": "arc", "family": "arc", "split": "dev-tune",
        "train": [{"input": [[1, 2], [3, 4]], "output": [[2, 1], [4, 3]]},
                  {"input": [[5, 6, 7]], "output": [[7, 6, 5]]}],
        "test_input": [[8, 9]], "test_output": [[9, 8]]}
BT_ITEM = {"id": "b1", "benchmark": "bt", "family": "bt_sp", "split": "dev-tune",
           "question": "What has keys but opens no locks?",
           "choices": ["a piano", "a door", "a map", "none of the above"], "label": 0}


def cand(program=None, cid="k1", text=""):
    return Candidate(id=cid, text=text or (program or ""), card="seeded", operator="none", seed="",
                     perm=0, round=0, call_id="c0", program=program)


# ---------------------------------------------------------------- grid validation
@pytest.mark.parametrize("g,ok", [
    ([[0, 1], [2, 9]], True), ([[0]], True), ([[0] * 30] * 30, True),
    ([], False), ([[]], False), ([[1, 2], [3]], False), ([[10]], False), ([[-1]], False),
    ([[1.0]], False), ([[True]], False), ([["1"]], False), ([(1, 2)], False), ((([1],)), False),
    ([[0] * 31], False), ([[0]] * 31, False), (None, False), ("[[1]]", False),
])
def test_valid_grid(g, ok):
    assert arc_exec.valid_grid(g) is ok


# ---------------------------------------------------------------- arc_exec
def test_correct_program():
    demo = arc_exec.demo_match(FLIP, ITEM["train"])
    assert demo == {"matched": 2, "total": 2, "diffs": [], "errors": []}
    assert arc_exec.predict(FLIP, ITEM["test_input"]) == [[9, 8]]


def test_wrong_program_diffs():
    demo = arc_exec.demo_match(IDENT, ITEM["train"])
    assert demo["matched"] == 0 and demo["total"] == 2
    d0 = demo["diffs"][0]
    assert d0["pair_index"] == 0 and d0["expected_shape"] == [2, 2] and d0["got_shape"] == [2, 2]
    assert d0["first_mismatches"][0] == [0, 0, 2, 1] and not d0["shape_mismatch"]
    assert len(demo["diffs"][1]["first_mismatches"]) == 2   # middle cell matches


def test_shape_mismatch():
    src = "def transform(grid):\n    return [[0]]\n"
    d = arc_exec.demo_match(src, ITEM["train"])["diffs"][0]
    assert d["shape_mismatch"] and d["got_shape"] == [1, 1] and d["first_mismatches"] == []


def test_crashing_program():
    demo = arc_exec.demo_match(CRASH, ITEM["train"])
    assert demo["matched"] == 0 and len(demo["errors"]) == 2
    assert "ZeroDivisionError" in demo["errors"][0]
    assert "candidate.py" in demo["errors"][0] and "exec_" not in demo["errors"][0]   # path masked


def test_syntax_error_and_missing_transform():
    assert arc_exec.run_program("def transform(:\n", [[[1]]]) == [None]
    res = arc_exec.execute("x = 1\n", [[[1]]])
    assert res["outputs"] == [None] and "AttributeError" in res["errors"][0]


def test_infinite_loop_timeout():
    res = arc_exec.execute(LOOP, [[[1]], [[2]]], timeout_s=1.5)
    assert res["timed_out"] and res["outputs"] == [None, None]
    assert res["errors"][0].startswith("timeout")
    assert res["duration_ms"] < 10000


def test_invalid_output_rejected():
    res = arc_exec.execute("def transform(grid):\n    return [[1, 2], [3]]\n", [[[1]]])
    assert res["outputs"] == [None] and "invalid grid" in res["errors"][0]


def test_prints_do_not_corrupt_result():
    assert arc_exec.run_program(NOISY, [[[1, 2]]]) == [[[2, 1]]]


def test_numpy_output_accepted():
    src = "import numpy as np\ndef transform(grid):\n    return np.fliplr(np.array(grid))\n"
    assert arc_exec.run_program(src, [[[1, 2]]]) == [[[2, 1]]]


def test_stdout_cap():
    src = ("import os\ndef transform(grid):\n    os.write(1, b'x' * 3000000)\n    return grid\n")
    res = arc_exec.execute(src, [[[1]]])
    assert res["outputs"] == [None] and "stdout cap" in res["errors"][0]


def test_secrets_not_inherited(monkeypatch):
    monkeypatch.setenv("ANTHROPIC_API_KEY", "sk-test-not-real")
    src = "import os\ndef transform(grid):\n    return [[1 if 'ANTHROPIC_API_KEY' in os.environ else 0]]\n"
    assert arc_exec.run_program(src, [[[0]]]) == [[[0]]]


def test_file_read_outside_sandbox_is_not_blocked(tmp_path):
    """Documents P0 behaviour: isolation is process-only, so a candidate CAN read files the user
    can read (here a file outside its temp sandbox). It cannot see the key through the harness
    (the verifier never passes test_output), but OS-level sandboxing is a P1 item."""
    secret = tmp_path / "outside.txt"
    secret.write_text("7", encoding="utf-8")
    src = f"def transform(grid):\n    return [[int(open({str(secret)!r}).read())]]\n"
    assert arc_exec.run_program(src, [[[0]]]) == [[[7]]]


def test_cwd_is_sandbox():
    src = "import os\ndef transform(grid):\n    return [[len(os.listdir('.'))]]\n"
    assert arc_exec.run_program(src, [[[0]]]) == [[[2]]]    # runner.py + candidate.py only


# ---------------------------------------------------------------- verify
def test_build_strips_key_and_hashes():
    h = verify.build(ITEM, "arc")
    assert h.type == "demo_match" and len(h.hash) == 64
    assert "test_output" not in json.dumps(h.data) and "[[9, 8]]" not in json.dumps(h.data["train"])
    assert verify.build(dict(ITEM, test_output=[[0]]), "arc").hash == h.hash
    hb = verify.build(BT_ITEM, "bt")
    assert hb.type == "agreement" and "label" not in hb.data


def test_build_accepts_problem_object():
    class P:
        item = ITEM
    assert verify.build(P(), "arc").hash == verify.build(ITEM, "arc").hash


def test_run_arc_verified(tmp_path):
    c = cand(FLIP)
    r = verify.run(c, verify.build(ITEM, "arc"), attempts=2, benchmark="arc", agreement=None, run_dir=tmp_path)
    assert r.status == "verified" and r.verification_type == "demo_match" and r.partial_score == 1.0
    assert c.pred == [[9, 8]] and r.feedback_record is None and r.attempts == 1
    assert r.details["attempts_budget"] == 2
    rows = read_jsonl(tmp_path / "verify.jsonl")
    assert rows[0]["id"] == "k1" and rows[0]["status"] == "verified"
    assert read_jsonl(tmp_path / "evidence.jsonl")[0]["source"] == "demo_match"


def test_run_arc_fail_partial(tmp_path):
    src = "def transform(grid):\n    return [row[::-1] for row in grid] if len(grid) > 1 else grid\n"
    c = cand(src)
    r = verify.run(c, verify.build(ITEM, "arc"), attempts=1, benchmark="arc", agreement=None, run_dir=tmp_path)
    assert r.status == "fail" and r.partial_score == 0.5 and c.pred == [[8, 9]]
    fb = r.feedback_record
    assert fb["passed"] == 1 and fb["failing_pairs"][0]["pair_index"] == 1
    assert fb["failing_pairs"][0]["first_mismatches"] == [[0, 0, 7, 5], [0, 2, 5, 7]]


def test_run_arc_all_train_pass_but_test_crashes(tmp_path):
    src = "def transform(grid):\n    if grid == [[8, 9]]:\n        raise ValueError('boom')\n    return [r[::-1] for r in grid]\n"
    c = cand(src)
    r = verify.run(c, verify.build(ITEM, "arc"), attempts=1, benchmark="arc", agreement=None, run_dir=tmp_path)
    assert r.status == "fail" and r.partial_score == 1.0 and c.pred is None
    assert any("test input" in e for e in r.feedback_record["errors"])


def test_run_arc_crash_and_timeout(tmp_path, monkeypatch):
    h = verify.build(ITEM, "arc")
    r = verify.run(cand(CRASH), h, attempts=1, benchmark="arc", agreement=None, run_dir=tmp_path)
    assert r.status == "fail" and r.partial_score == 0.0 and r.feedback_record["errors"]
    monkeypatch.setitem(verify.config.PARAMS, "exec_timeout_s", 1)
    r = verify.run(cand(LOOP, "k2"), h, attempts=1, benchmark="arc", agreement=None, run_dir=tmp_path)
    assert r.status == "fail" and r.details["timed_out"]


def test_run_arc_program_from_text_and_missing(tmp_path):
    h = verify.build(ITEM, "arc")
    r = verify.run(cand(None, text=FLIP), h, attempts=1, benchmark="arc", agreement=None, run_dir=tmp_path)
    assert r.status == "verified"
    r = verify.run(cand(None, text="no code"), h, attempts=1, benchmark="arc", agreement=None, run_dir=tmp_path)
    assert r.status == "fail" and r.attempts == 0


def test_hash_mismatch(tmp_path):
    h = verify.build(ITEM, "arc")
    h.data["train"][0]["output"] = [[0, 0], [0, 0]]
    r = verify.run(cand(FLIP), h, attempts=1, benchmark="arc", agreement=None, run_dir=tmp_path)
    assert r.status == "unverified" and r.details["hash_mismatch"]


def test_run_bt_agreement_only(tmp_path):
    from harness import llm
    calls = []
    llm.set_mock(lambda p, role, meta: calls.append(role) or "x")
    try:
        c = cand(None, text="A")
        c.pred = "A"
        r = verify.run(c, verify.build(BT_ITEM, "bt"), attempts=3, benchmark="bt", agreement=0.67, run_dir=tmp_path)
    finally:
        llm.set_mock(None)
    assert r.status == "unverified" and r.verification_type == "agreement"
    assert r.partial_score == 0.67 and r.attempts == 0 and calls == []


# ---------------------------------------------------------------- feedback
def test_feedback_deterministic_and_capped():
    big = [{"input": [[0] * 30] * 30, "output": [[1] * 30] * 30} for _ in range(40)]
    demo = arc_exec.demo_from_outputs(big, [[[0] * 30] * 30] * 40, ["Traceback " + "e" * 2000] * 40)
    a = feedback.record_for(cand(IDENT), demo, "arc", cap_tokens=1500)
    b = feedback.record_for(cand(IDENT), demo, "arc", cap_tokens=1500)
    assert a == b and a["truncated"] and feedback.est_tokens(a) <= 1500
    assert all(len(p["first_mismatches"]) <= 8 for p in a["failing_pairs"])
    small = feedback.record_for(cand(IDENT), demo, "arc", cap_tokens=100)
    assert feedback.est_tokens(small) <= 100 and small["truncated"] and small["failing_pairs"]


def test_feedback_fields():
    demo = arc_exec.demo_match(IDENT, ITEM["train"])
    rec = feedback.record_for(cand(IDENT), demo, "arc")
    assert set(rec) == {"failing_pairs", "errors", "passed", "total", "truncated"}
    assert set(rec["failing_pairs"][0]) == {"pair_index", "expected_shape", "got_shape", "first_mismatches"}
    assert feedback.record_for(cand(None), {}, "bt")["failing_pairs"] == []
