"""Lessons: short itemised claims with evidence, derived by script from what runs recorded, merged by script,
never written or rewritten by an agent.

Two speeds (research_notes/thinking_parts/10_learning.md, I7 and I8; creative_genius/00_SYNTHESIS.md):
- pitfalls: what builders got wrong at the cheap rungs (boundary, build, size, speed), per part; plentiful, fast,
  and actionable, so they reach the builder of the next idea in the same part (at most five);
- outcomes: what the overnight verdict settled (helped, did not help), per baseline version; slow and rare.

A lesson's state follows its evidence: hypothesis (seen once), supported (seen in two runs), rule (three or
more). Raw entries are append-only; a wrong lesson is contradicted by new evidence, never edited by hand.
Stored at memory/lessons.jsonl.
"""
from __future__ import annotations

import hashlib
import json
import re
import time
from pathlib import Path


def _jsonl(p: Path) -> list[dict]:
    if not p.exists():
        return []
    out = []
    for line in p.read_text(encoding="utf-8").splitlines():
        try:
            out.append(json.loads(line))
        except Exception:  # noqa: BLE001
            pass
    return out


def load(path: Path) -> list[dict]:
    return _jsonl(path)


def save(path: Path, entries: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("".join(json.dumps(e) + "\n" for e in entries), encoding="utf-8")


def _state(entry: dict) -> str:
    runs = len(set(entry.get("runs") or []))
    return "rule" if runs >= 3 else ("supported" if runs >= 2 else "hypothesis")


def pitfall_key(reason: str, violations: list[str] | None = None) -> str | None:
    """A failure reason reduced to a reusable category; None when it is not a lesson (noise, no reason)."""
    r = (reason or "").lower()
    v = " ".join(violations or []).lower()
    # the rung-0 reason names both causes at once; the violation lines say which one it was
    if "is protected" in v or (not v and "protected" in r and "outside" not in r):
        return "touched protected code (the exam, the data loader or the parameter count)"
    if "outside" in v or "boundary" in v or "outside" in r or "boundary" in r:
        return "changed code outside the part's boundary"      # the symbol stays in the evidence, not in the lesson
    if "does not parse" in v or "syntax" in r:
        return "the script did not parse"
    if "import" in r and "not allowed" in (r + v):
        return "imported a forbidden module"
    if "param" in r and ("cap" in r or "more than" in r or "+10" in r):
        return "grew the model past the parameter cap"
    if "step" in r and ("slow" in r or "time" in r):
        return "step time over the cap"
    if "memory" in r or "vram" in r or "out of memory" in r:
        return "ran out of card memory"
    if "did not start" in r or "rc=" in r or "traceback" in r:
        return "the script crashed on start"
    return None


def is_gap_failure(fb: dict | None) -> bool:
    """The checker's record says the build ran but lost the score gap to the baseline (or reference): the LLM
    checker's rung-3 "at step N the loss is X against the baseline's Y (gap ...)" and the script checker's rung-2
    "the quick score is X against the baseline's Y ... (gap ...)". Read from the reason, not the rung number."""
    return bool(re.search(r"against the baseline's .*\(gap [+-]?\d", str((fb or {}).get("reason", ""))))


def failure_card(fb: dict | None) -> str:
    """A failed build's record as a short card for the repairing agent: which check, why, where, the cause tag.
    Replaces the raw JSON dump (research_notes/thinking_parts/06_reasoning.md item 6, 01_representation.md R8)."""
    fb = fb or {}
    if fb.get("near_miss"):
        return ("RECORD: passed the first checks (a near miss or better from the ambitious lane)"
                + (f"; matched-step gap z {fb.get('learn_z')}" if fb.get("learn_z") is not None else "") + ".")
    names = {0: "boundary", 1: "build", 2: "timing and memory", 3: "learning", 4: "long comparison"}
    gap = is_gap_failure(fb)                     # the script checker reports the learning gap at rung 2
    lines = [f"CHECK FAILED: rung {fb.get('rung')} ({'learning' if gap else names.get(fb.get('rung'), '?')})",
             f"WHY: {str(fb.get('reason', ''))[:400]}"]
    where = list(fb.get("violations") or [])[:4]
    stderr = str(fb.get("stderr") or "").strip().splitlines()
    if stderr:
        where += [l for l in stderr if l.strip()][-6:]
    if where:
        lines.append("WHERE: " + " | ".join(w[:160] for w in where))
    cause = pitfall_key(fb.get("reason", ""), fb.get("violations"))
    lines.append("CAUSE TAG: " + (cause or ("learning failure" if fb.get("rung") == 3 or gap else "unknown")))
    return "\n".join(lines)


def update_from_run(run_dir: Path, path: Path, baseline_version: str = "v1") -> dict:
    """Read a finished run's records and merge what they teach into the lessons file. Returns counts.

    Called twice per run: by the loop's _finish (pitfalls; rung5/ does not exist yet) and by nano/batch_verify.py
    after the overnight verdicts land in rung5/results.json (outcomes). Calling it again is safe: a piece of
    evidence counts once, so the helpful and harmful counters do not grow on a repeat call."""
    entries = load(path)
    by_id = {e["id"]: e for e in entries}
    cands = [r for f in sorted((run_dir / "cands").glob("*.jsonl")) for r in _jsonl(f)] if (run_dir / "cands").exists() else []
    verify = {}
    for v in _jsonl(run_dir / "verify.jsonl"):
        verify[v["id"]] = v
    rung5 = {}
    try:
        rung5 = json.loads((run_dir / "rung5" / "results.json").read_text(encoding="utf-8")).get("candidates", {})
    except Exception:  # noqa: BLE001
        pass
    run = run_dir.name
    added, touched = 0, 0

    def upsert(kind: str, scope: dict, text: str, evidence: str, helpful: bool | None = None) -> None:
        nonlocal added, touched
        eid = hashlib.sha1(f"{kind}|{scope.get('part')}|{scope.get('version')}|{text.lower()}".encode()).hexdigest()[:12]
        e = by_id.get(eid)
        if e is None:
            e = {"id": eid, "kind": kind, "scope": scope, "text": text, "evidence": [], "runs": [], "helpful": 0, "harmful": 0,
                 "state": "hypothesis", "ts": time.strftime("%Y-%m-%dT%H:%M:%S")}
            by_id[eid] = e
            entries.append(e)
            added += 1
        if run not in e["runs"]:
            e["runs"].append(run)
        if evidence in e["evidence"]:
            return                              # already counted (a repeat call on the same run)
        e["evidence"].append(evidence)
        touched += 1
        if helpful is True:
            e["helpful"] += 1
        elif helpful is False:
            e["harmful"] += 1
        e["state"] = _state(e)

    # pitfalls: cheap-rung failures, per part; a same-round fix that passed marks the lesson as actionable
    children = {}
    for r in cands:
        for pid in r.get("parent_ids") or []:
            children.setdefault(pid, []).append(r)
    for r in cands:
        v = verify.get(r.get("id"))
        if not v or v.get("status") == "checked":
            continue
        fb = v.get("feedback_record") or {}
        if (fb.get("rung") or 0) > 2:
            continue
        key = pitfall_key(fb.get("reason", ""), fb.get("violations"))
        if not key:
            continue
        part = (r.get("extra") or {}).get("node") or "any"
        fixed = any(verify.get(c.get("id"), {}).get("status") == "checked" for c in children.get(r.get("id"), []))
        upsert("pitfall", {"part": part, "version": baseline_version}, f"builders for the part '{part}' have {key}", r["id"],
               helpful=True if fixed else None)
    # outcomes: the overnight verdict (batch_verify's results.json names the part "node" and the seed count "n")
    for cid, s in rung5.items():
        st = s.get("status")
        hyp = str(s.get("hypothesis") or "")[:120]
        if not hyp or s.get("control") or str(cid).startswith("control") or str(cid).startswith("tune"):
            continue
        part = s.get("part") or s.get("node") or "any"
        n_seeds = s.get("n_seeds") if s.get("n_seeds") is not None else s.get("n")
        if st in ("verified", "stackable"):
            upsert("outcome", {"part": part, "version": baseline_version},
                   f"helped ({st}, delta {s.get('delta')}): {hyp}", str(cid), helpful=True)
        elif st == "fail" and (n_seeds or 0) >= 3:
            upsert("outcome", {"part": part, "version": baseline_version},
                   f"did not help over {n_seeds} seeds: {hyp}", str(cid), helpful=False)
    save(path, entries)
    return {"added": added, "touched": touched, "total": len(entries)}


def render(path: Path, part: str | None = None, kind: str = "pitfall", max_n: int = 5, version: str | None = None) -> str:
    """The few lessons a builder (pitfalls) or an idea agent (outcomes) should see for a part: most evidence first,
    rules before hypotheses, this part before any part. Empty when there is nothing."""
    rows = []
    for e in load(path):
        if e.get("kind") != kind:
            continue
        sc = e.get("scope") or {}
        if version and sc.get("version") not in (None, version):
            continue
        if part and sc.get("part") not in (None, "any", part):
            continue
        rank = {"rule": 0, "supported": 1, "hypothesis": 2}.get(e.get("state"), 3)
        rows.append((rank, -len(e.get("evidence") or []), 0 if sc.get("part") == part else 1, e))
    rows.sort(key=lambda t: t[:3])
    chosen = [t[3] for t in rows[:max_n]]
    if not chosen:
        return ""
    head = ("PITFALLS RECORDED IN EARLIER BUILDS (each with how often it was seen; avoid them):" if kind == "pitfall"
            else "WHAT EARLIER OVERNIGHT VERDICTS SETTLED (measured, not opinion):")
    lines = [head]
    for e in chosen:
        n = len(e.get("evidence") or [])
        lines.append(f"- {e['text']} [{e.get('state')}, seen {n} time{'s' if n != 1 else ''}"
                     + (f", fixed {e['helpful']}x" if kind == "pitfall" and e.get("helpful") else "") + "]")
    return "\n".join(lines)
