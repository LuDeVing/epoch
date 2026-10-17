"""Deterministic feedback records for revise children (ARCHITECTURE.md section 3 /verify step 7;
section 5, "Feedback form for revise" = deterministic record at P0, "Evidence and feedback record
caps" = 1.5k tokens).

Record: {failing_pairs: [{pair_index, expected_shape, got_shape, first_mismatches: [[r, c, exp, got]]
x <= 8}], errors: [tail], passed: n, total: n, truncated: bool}. Built only from train pairs and
the candidate's own outputs; no key, no confidence, no prose. Capped by deterministic truncation.
"""
from __future__ import annotations

import json

from . import config
from .schemas import Candidate

MAX_MISMATCHES = 8
ERROR_TAIL_CHARS = 400
MAX_ERRORS = 4


def est_tokens(rec: dict) -> int:
    """Same estimate as the mock backend: chars / 4."""
    return max(1, len(json.dumps(rec, ensure_ascii=True)) // 4)


def _pair(d: dict) -> dict:
    return {"pair_index": d["pair_index"], "expected_shape": d.get("expected_shape"),
            "got_shape": d.get("got_shape"),
            "first_mismatches": [list(m) for m in d.get("first_mismatches", [])[:MAX_MISMATCHES]]}


def _shrink_steps(rec: dict):
    """Yield in-place reductions in a fixed order until nothing is left to cut."""
    for n in (200, 100):
        rec["errors"] = [e[-n:] for e in rec["errors"]]
        yield
    while len(rec["errors"]) > 1:
        rec["errors"].pop()
        yield
    for n in (4, 2, 1, 0):
        for p in rec["failing_pairs"]:
            p["first_mismatches"] = p["first_mismatches"][:n]
        yield
    while len(rec["failing_pairs"]) > 1:
        rec["failing_pairs"].pop()
        yield
    rec["errors"] = []
    yield


def cap_record(rec: dict, cap_tokens: int) -> dict:
    """Truncate deterministically until the record fits cap_tokens; sets truncated."""
    if est_tokens(rec) <= cap_tokens:
        return rec
    rec["truncated"] = True
    for _ in _shrink_steps(rec):
        if est_tokens(rec) <= cap_tokens:
            break
    return rec


def record_for(cand: Candidate, demo: dict, benchmark: str, cap_tokens: int = 1500) -> dict:
    """README interface. demo is arc_exec.demo_match output (plus an optional test-input error in
    demo["errors"]). BT has no revise and no external check at P0, so its record is empty."""
    cap_tokens = cap_tokens or config.PARAMS["feedback_cap_tokens"]
    if benchmark != "arc" or not demo:
        return {"failing_pairs": [], "errors": [], "passed": 0, "total": 0, "truncated": False}
    errors = [str(e)[-ERROR_TAIL_CHARS:] for e in demo.get("errors", [])][:MAX_ERRORS]
    rec = {"failing_pairs": [_pair(d) for d in demo.get("diffs", [])], "errors": errors,
           "passed": int(demo.get("matched", 0)), "total": int(demo.get("total", 0)),
           "truncated": len(demo.get("errors", [])) > MAX_ERRORS}
    return cap_record(rec, cap_tokens)
