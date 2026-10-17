"""Verifier construction and execution (ARCHITECTURE.md section 3 /verify; section 5 m_verify, k,
feedback caps; section 8 verification types).

build() makes a hashed, read-only verifier handle from the key-stripped item:
  ARC: type demo_match, data {train, test_input}, hash = sha256 of the train pairs.
  BT:  type agreement, data {question, choices}, hash = sha256 of question + choices.
run() checks the hash before every use (REP-03, EVL-18), then:
  ARC: executes the program on the train inputs and the test input in one child process
       (arc_exec). verified iff every train pair matches and a valid test grid was predicted
       (cand.pred is set whenever a valid test grid exists); otherwise fail with
       partial_score = matched / total and a feedback.py record.
  BT:  no external check at P0: status unverified, verification_type agreement,
       partial_score = the agreement value the driver supplies. No LLM calls at P0.
The driver chooses which candidates to verify (m_verify) and the attempt budget k; run() logs k
as details["attempts_budget"] and the attempts actually used in VerifyResult.attempts (ARC: 1,
since execution is deterministic; BT: 0). surprise needs conf, which run() never sees (the
falsifier never sees conf), so the driver sets VerifyResult.surprise and writes surprises.jsonl.
"""
from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass, field
from pathlib import Path

from . import arc_exec, config, feedback
from .schemas import Candidate, VerifyResult, append_jsonl, now_ts, strip_key

# P1 hook (EVL-02): adversarial-LLM falsifier for non-executable items. Off at P0; when built it
# yields status "checked" (never "verified"), and a checked candidate may stop a run only once
# config.FLAGS["llm_falsifier_validated"] is set.
LLM_FALSIFIER_ENABLED = False


@dataclass
class VerifierHandle:
    type: str
    hash: str
    data: dict = field(default_factory=dict)


# ---------------------------------------------------------------- build
def _sha(obj) -> str:
    blob = json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=True)
    return hashlib.sha256(blob.encode("utf-8")).hexdigest()


def _hash_for(vtype: str, data: dict) -> str:
    if vtype == "demo_match":
        return _sha(data["train"])
    return _sha({"question": data["question"], "choices": data["choices"]})


def _item_of(problem) -> dict:
    """Accept an encode.Problem (uses .item) or an item dict; always key-stripped."""
    item = getattr(problem, "item", problem)
    return strip_key(dict(item))


def build(problem, benchmark: str) -> VerifierHandle:
    """Section 3 /verify step 1: build the strongest available check before generation."""
    item = _item_of(problem)
    if benchmark == "arc":
        data = {"train": [{"input": p["input"], "output": p["output"]} for p in item["train"]],
                "test_input": item["test_input"]}
        vtype = "demo_match"
    elif benchmark == "bt":
        data = {"question": item["question"], "choices": list(item["choices"])}
        vtype = "agreement"
    else:
        raise ValueError(f"unknown benchmark {benchmark}")
    return VerifierHandle(type=vtype, hash=_hash_for(vtype, data), data=data)


def check_hash(handle: VerifierHandle) -> bool:
    """REP-03 / EVL-18: the verifier model is read-only; recompute its hash before every use."""
    try:
        return _hash_for(handle.type, handle.data) == handle.hash
    except (KeyError, TypeError):
        return False


# ---------------------------------------------------------------- run
def _program_of(cand: Candidate) -> str | None:
    if cand.program:
        return cand.program
    return cand.text if cand.text and "def transform" in cand.text else None


def _run_arc(cand: Candidate, handle: VerifierHandle, attempts: int) -> VerifyResult:
    """Section 8 demo_match: external type, makes status verified."""
    train, src = handle.data["train"], _program_of(cand)
    details = {"hash": handle.hash, "attempts_budget": attempts}
    if src is None:
        demo = {"matched": 0, "total": len(train), "diffs": [], "errors": ["no program found in candidate"]}
        return VerifyResult(id=cand.id, status="fail", verification_type="demo_match", attempts=0,
                            partial_score=0.0, details=details | {"matched": 0, "total": len(train)},
                            feedback_record=feedback.record_for(cand, demo, "arc", config.PARAMS["feedback_cap_tokens"]))
    res = arc_exec.execute(src, [p["input"] for p in train] + [handle.data["test_input"]])
    outs, errs = res["outputs"], res["errors"]
    demo = arc_exec.demo_from_outputs(train, outs[:-1], errs[:-1])
    pred, test_err = outs[-1], errs[-1]
    if pred is not None:
        cand.pred = pred
    if test_err:
        demo["errors"].append(f"test input: {test_err[-arc_exec.ERROR_TAIL_CHARS:]}")
    total = demo["total"]
    ok = total > 0 and demo["matched"] == total and pred is not None
    details |= {"matched": demo["matched"], "total": total, "pred_shape": arc_exec.shape(pred),
                "test_error": test_err, "timed_out": res["timed_out"], "duration_ms": res["duration_ms"]}
    return VerifyResult(id=cand.id, status="verified" if ok else "fail", verification_type="demo_match",
                        attempts=1, partial_score=(demo["matched"] / total) if total else 0.0,
                        feedback_record=None if ok else feedback.record_for(
                            cand, demo, "arc", config.PARAMS["feedback_cap_tokens"]),
                        details=details)


def llm_falsifier(cand: Candidate, handle: VerifierHandle, *, attempts: int, run_dir: Path) -> VerifyResult:
    """P1 hook (section 3 /verify step 3): k distinct fresh-context falsifier attempts on the bare
    candidate, each with a different evidence seed or constraint focus; status checked when no
    counterexample is found. Not built at P0."""
    raise NotImplementedError("llm_falsifier is a P1 hook; off at P0")


def _run_bt(cand: Candidate, handle: VerifierHandle, attempts: int, agreement: float | None,
            run_dir: Path | None) -> VerifyResult:
    """Section 8: BRAINTEASER has no external check at P0; agreement-only placeholder."""
    if LLM_FALSIFIER_ENABLED:
        return llm_falsifier(cand, handle, attempts=attempts, run_dir=run_dir)
    return VerifyResult(id=cand.id, status="unverified", verification_type="agreement", attempts=0,
                        partial_score=float(agreement) if agreement is not None else 0.0,
                        details={"hash": handle.hash, "attempts_budget": attempts, "pred": cand.pred,
                                 "llm_falsifier": "off (P1 hook)"})


def _log(run_dir: Path | None, res: VerifyResult, benchmark: str) -> None:
    """Append verify.jsonl and evidence.jsonl rows (script-written, no candidate spans)."""
    if run_dir is None:
        return
    run_dir = Path(run_dir)
    append_jsonl(run_dir / "verify.jsonl", res.to_dict() | {"benchmark": benchmark, "ts": now_ts()})
    d = res.details
    obs = (f"demo_match {d.get('matched')}/{d.get('total')} train pairs; test grid "
           f"{'predicted' if d.get('pred_shape') else 'missing'}" if res.verification_type == "demo_match"
           else f"{res.verification_type}: status {res.status}, partial {res.partial_score:.3f}")
    append_jsonl(run_dir / "evidence.jsonl", {"source": res.verification_type, "about": res.id,
                                              "observation": obs, "ts": now_ts()})


def run(cand: Candidate, handle: VerifierHandle, *, attempts: int, benchmark: str,
        agreement: float | None, run_dir: Path) -> VerifyResult:
    """README interface; section 3 /verify steps 1, 3 and 7."""
    if not check_hash(handle):
        res = VerifyResult(id=cand.id, status="unverified", verification_type="none", attempts=0,
                           details={"hash_mismatch": True, "hash": handle.hash})
    elif benchmark == "arc":
        res = _run_arc(cand, handle, attempts)
    elif benchmark == "bt":
        res = _run_bt(cand, handle, attempts, agreement, run_dir)
    else:
        raise ValueError(f"unknown benchmark {benchmark}")
    _log(run_dir, res, benchmark)
    return res
