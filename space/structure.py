"""From a folder of research material to a structured problem. The person shares their files (notes, data, papers
as text, drafts); one model call reads them and drafts the spec the loop needs: title, goal, situation, criteria,
known facts with sources, limits, parts, field, scope. The person then edits the draft on the page.
Route: POST /api/run/structure {file_ids: [...], notes: "..."} (space/launch.py registers it)."""
from __future__ import annotations

import json
import re
from pathlib import Path

from space.store import Reject

MAX_CHARS = 90_000          # of file text in one call
PER_FILE = 24_000
MODEL = "sonnet"

PROMPT = """You are preparing a research problem for a team of AI researchers. Below are files a person shared
from their own research folder, with their names. Read them and write the problem the team should work on, in
the person's own terms, as JSON with exactly these keys:

title: a few words.
goal: 3 to 6 sentences: what they want to find out or improve, why, and what the current state is. Plain words.
context: 2 to 5 sentences on the situation: what is done today, who is involved, what was tried, what the files are.
criteria: 3 to 6 objects {name, how}: how to tell a good answer; name is one or two words, how is one sentence a judge can check.
facts: up to 25 objects {text, source}: concrete facts, numbers, results and claims found in the files; source is the file name and where in it.
limits: up to 8 strings: what must stay fixed, what must never happen, limits on time, money, people, tools.
parts: 3 to 8 strings of two to five words each: the parts the problem naturally splits into (names, like "the paper forms" or "queue order", not sentences).
subparts: an object, one key per part name above, each a list of 2 to 4 strings of two to five words: the smaller questions inside that part (like "which fields to drop" under "the paper forms"). Every part gets sub-parts.
field: the field in two or three words.
scope: one sentence: what is in and what is out.
open_questions: up to 6 strings: what the files leave unanswered, the questions the team should chase first.

Rules: use only what the files say or clearly imply; mark a guess with "(guess)"; keep the person's vocabulary; no
headings, no markdown, no text outside the JSON object.

FILES:
%s

%s"""


def _ascii(s: str) -> str:
    return s.encode("utf-8", "replace").decode("utf-8")


def gather(files_store, file_ids: list, notes: str = "") -> tuple[str, list[dict]]:
    """The file texts for the prompt (text files in full up to a cap; binary files by name only) and a manifest."""
    parts, manifest, used = [], [], 0
    for fid in list(file_ids or [])[:40]:
        try:
            rec, data = files_store.get(str(fid))
        except Reject:
            continue
        name = rec.get("name") or fid
        if rec.get("text"):
            text = data.decode("utf-8", "replace")
            take = text[: min(PER_FILE, MAX_CHARS - used)]
            used += len(take)
            parts.append(f"=== {name} ({len(text)} characters{', cut' if len(take) < len(text) else ''}) ===\n{take}")
            manifest.append({"id": fid, "name": name, "chars": len(text), "used": len(take)})
        else:
            parts.append(f"=== {name} ({rec.get('bytes')} bytes, {rec.get('type')}; not readable as text, name only) ===")
            manifest.append({"id": fid, "name": name, "chars": 0, "used": 0})
        if used >= MAX_CHARS:
            break
    extra = f"NOTES FROM THE PERSON:\n{str(notes or '').strip()[:4000]}" if str(notes or "").strip() else ""
    return _ascii("\n\n".join(parts)), manifest, extra


def parse_json(text: str) -> dict:
    """The JSON object in a model reply, with or without fences."""
    t = str(text or "").strip()
    m = re.search(r"\{.*\}", t, flags=re.S)
    if not m:
        raise Reject(502, "no_json", hint="the model's reply had no JSON object")
    try:
        d = json.loads(m.group(0))
    except ValueError as e:
        raise Reject(502, "bad_json", hint=str(e)[:120])
    if not isinstance(d, dict):
        raise Reject(502, "bad_json", hint="not an object")
    return d


def _short(t: str, n: int) -> str:
    """Cut at a word boundary, never mid-word."""
    t = " ".join(str(t).split())
    if len(t) <= n:
        return t
    cut = t[:n].rsplit(" ", 1)[0]
    return (cut or t[:n]).rstrip(",;:")


def _parts_list(d: dict) -> list[dict]:
    """Parts with their sub-parts: [{name, sub: "a, b, c"}]; the wizard edits both as text."""
    subs = d.get("subparts") if isinstance(d.get("subparts"), dict) else {}
    norm = {" ".join(str(k).lower().split()): v for k, v in subs.items()}
    out = []
    for t in (d.get("parts") or [])[:9]:
        name = _short(str(t).strip(), 48)
        if not name:
            continue
        raw = norm.get(" ".join(name.lower().split())) or norm.get(" ".join(str(t).lower().split())) or []
        names = [_short(str(x).strip(), 40) for x in (raw if isinstance(raw, list) else []) if str(x).strip()][:4]
        out.append({"name": name, "sub": ", ".join(n for n in names if n)})
    return out


def to_spec(d: dict) -> dict:
    """The draft in the shape the wizard and space/launch.py use."""
    def lst(x):
        return [str(v).strip() for v in x if str(v).strip()] if isinstance(x, list) else []
    crit = [{"name": str(c.get("name") or "")[:60], "how": str(c.get("how") or "")[:400]} for c in (d.get("criteria") or []) if isinstance(c, dict) and c.get("name")]
    facts = [{"text": str(f.get("text") or "")[:400], "source": str(f.get("source") or "")[:120]} for f in (d.get("facts") or []) if isinstance(f, dict) and f.get("text")]
    return {
        "title": str(d.get("title") or "")[:120],
        "goal": str(d.get("goal") or "")[:4000],
        "context": str(d.get("context") or "")[:2000],
        "criteria": crit[:8],
        "facts": facts[:40],
        "limits": [{"text": t[:400]} for t in lst(d.get("limits"))[:12]],
        "partsList": _parts_list(d),
        "field": str(d.get("field") or "")[:80],
        "scope": str(d.get("scope") or "")[:400],
        "open_questions": lst(d.get("open_questions"))[:8],
    }


def structure(files_store, file_ids: list, notes: str = "", model: str = MODEL) -> dict:
    """One model call over the shared files; returns {spec, manifest, model, error?}."""
    from harness import llm
    body, manifest, extra = gather(files_store, file_ids, notes)
    if not body and not extra:
        raise Reject(422, "nothing_to_read", hint="share at least one readable file, or write some notes")
    prompt = PROMPT % (body or "(no readable files)", extra)
    r = llm.call(prompt, role="structure", model=model, max_tokens=4000, timeout=240, retries=1)
    if r.error or not (r.text or "").strip():
        raise Reject(502, "model_failed", hint=str(r.error or "empty reply")[:200])
    d = parse_json(r.text)
    return {"spec": to_spec(d), "manifest": manifest, "model": model, "tokens": int(getattr(r.usage, "total_tokens", 0) or 0)}
