"""The one merge of people's events into the loop's control (docs/MULTIPLAYER_DESIGN.md section 6.2).

Used by GET /api/control (the loop pulls it), by nano/space.py (overlay_file) and by the bridge renderer
(render_control_json). Standard library only.

Level keys (skip_nodes, veto, choose, note, opinions, add_nodes, pause) are computed over every event passed in,
because they are a state, not a delta. The one-shot lists (steps, disputes, seeds), `refs` and `dropped` look only
at events after `since`, so each boundary reports what is new since the loop's cursor.
"""
from __future__ import annotations

import json
import os
import re
import time

from space.contract import CONTROL_KEYS, FILE_ONLY_KEYS, KINDS, NOTE_CAP, NOTES_KEPT, actor_class

NOTE_LINE_CAP = 300                               # rule 5: each note is cut to 300 characters before the join
CAND_RE = re.compile(r"^n[0-9a-f]{10}$")          # rule 6: a candidate id is n plus 10 hex
SIDE_KEYS = ("disputes", "seeds", "step")         # KINDS control keys that are lists beside `control`, not inside it


def clean_id(raw) -> str:
    """The loop's id cleaning (nano/loop.py _add_human_nodes): lower case, a-z0-9_, 16 characters."""
    return re.sub(r"[^a-z0-9_]", "", str(raw or "").lower())[:16]


def _owner(ev: dict) -> str:
    by = str(ev.get("by") or "")
    return str(ev.get("owner") or by.split(".")[0])


def _class(ev: dict) -> str:
    return actor_class(str(ev.get("by") or ""), str(ev.get("by_kind") or ""), _owner(ev))


def _data(ev: dict) -> dict:
    d = ev.get("data")
    return d if isinstance(d, dict) else {}


def _subject_id(ev: dict, prefix: str, *data_keys: str) -> str:
    """The id an event is about: a data key first, else the subject after its prefix (node:, question:)."""
    d = _data(ev)
    for k in data_keys:
        if d.get(k) not in (None, ""):
            return str(d[k])
    s = str(ev.get("subject") or "")
    return s[len(prefix):] if s.startswith(prefix) else ""


def _counts(ev: dict) -> bool:
    """Rule 1: only a person's or a delegate's event counts, and only when the contract lets that class write it."""
    kind = ev.get("kind")
    if kind not in KINDS:
        return False
    cls = _class(ev)
    return cls in ("person", "delegate") and cls in KINDS[kind][0].split()


def _claim_holder(ev: dict) -> tuple[str, str | None]:
    """(node id, new holder or None when the claim ends) for a server claim_* event."""
    node = _subject_id(ev, "node:")
    d, kind = _data(ev), ev.get("kind")
    if kind == "claim_granted":
        return node, str(d.get("owner") or "")
    if kind == "claim_taken_over":
        return node, str(d.get("to") or "")
    return node, None


def _other_loop(owner: str, loop: str) -> bool:
    return owner.startswith("team.") and owner != loop


def merge(events, *, loop="team.loop", claims=(), since=0, file_ctl=None) -> dict:
    """Fold people's events into the control dict of section 6.2. `events` may come in any order."""
    evs = sorted((e for e in events or () if isinstance(e, dict) and isinstance(e.get("seq"), int)),
                 key=lambda e: e["seq"])
    since = int(since or 0)

    skip_last: dict[str, tuple[str, int]] = {}       # node -> (kind, seq) of the latest skip or unskip
    veto_last: dict[str, tuple[str, int]] = {}       # question -> (kind, seq)
    chooses: list[dict] = []                         # every question_chosen, in seq order
    notes: list[dict] = []
    opinions: dict[tuple[str, str], dict] = {}       # (owner, target) -> latest
    add_nodes: dict[str, dict] = {}
    pause_last: dict[str, tuple[str, int]] = {}      # owner -> (kind, seq)
    holders_live: dict[str, str] = {}                # node -> holder, from the live claims then the claim events
    claim_refs: list[int] = []
    steps, disputes, seeds, dropped, refs = [], [], [], [], []
    findings: list[dict] = []                        # rule 13: every finding_posted, state like skip_nodes

    for c in claims or ():
        if isinstance(c, dict):
            s = str(c.get("subject") or "")
            if s.startswith("node:") and c.get("owner"):
                holders_live[s[5:]] = str(c["owner"])

    for ev in evs:
        kind, seq, d = ev.get("kind"), ev["seq"], _data(ev)
        new = seq > since
        if kind in ("claim_granted", "claim_taken_over", "claim_released", "claim_expired"):
            if _class(ev) != "server":
                continue
            node, holder = _claim_holder(ev)
            if not node:
                continue
            before = holders_live.get(node)
            if holder:
                holders_live[node] = holder
            else:
                holders_live.pop(node, None)
            if new and (_other_loop(before or "", loop) or _other_loop(holder or "", loop)):
                claim_refs.append(seq)                # rule 11: an other loop's claim changed skip_nodes
            continue
        if not _counts(ev):
            continue
        folded = True
        if kind in ("node_skipped", "node_unskipped"):
            node = _subject_id(ev, "node:", "node")
            if not node:
                continue
            skip_last[node] = (kind, seq)
        elif kind in ("question_vetoed", "question_unvetoed"):
            q = _subject_id(ev, "question:", "question")
            if not q:
                continue
            veto_last[q] = (kind, seq)
        elif kind == "question_chosen":
            q = _subject_id(ev, "question:", "question")
            if not q:
                continue
            chooses.append({"seq": seq, "by": _owner(ev), "question": q})
        elif kind == "note_posted":
            notes.append({"seq": seq, "by": _owner(ev), "text": str(d.get("text") or "")})
        elif kind == "finding_posted":
            findings.append({"seq": seq, "by": _owner(ev), "ts": ev.get("ts"), "part": d.get("part") or None,
                             "title": str(d.get("title") or "")[:120], "text": str(d.get("text") or "")[:4000],
                             "kind": str(d.get("kind") or "note"), "source": str(d.get("source") or "own work")[:200],
                             "values": d.get("values") if isinstance(d.get("values"), dict) else {},
                             "replaces": d.get("replaces") if isinstance(d.get("replaces"), int) else None})
        elif kind == "opinion_given":
            target = str(d.get("target") or "")
            if not target:
                continue
            opinions[(_owner(ev), target)] = {"seq": seq, "target": target, "score": d.get("score"),
                                              "note": d.get("note", ""), "who": _owner(ev)}
        elif kind == "node_added":
            nid = clean_id(d.get("id"))
            if not nid:
                if new:
                    dropped.append({"seq": seq, "reason": "bad_id"})
                continue
            if nid in add_nodes:
                if new:
                    dropped.append({"seq": seq, "reason": "id_taken"})
                continue
            add_nodes[nid] = {**d, "id": nid, "by": _owner(ev), "by_seq": seq}
        elif kind in ("run_paused", "run_resumed"):
            pause_last[_owner(ev)] = (kind, seq)
        elif kind == "run_step":
            folded = False                            # the loop adds the step it consumes (consume_step)
            if new:
                steps.append({"seq": seq, "round": d["round"] if d.get("round") is not None else ev.get("round"),
                              "stage": d.get("stage") or ev.get("stage"), "by": ev.get("by")})
        elif kind == "fact_disputed":
            if new:
                disputes.append({"seq": seq, "node": d.get("node"), "fact": d.get("fact"), "reason": d.get("reason"),
                                 "tag": d.get("tag"), "by": _owner(ev)})
        elif kind == "seed_added":
            if new:
                seeds.append({"seq": seq, "node": d.get("node"), "text": d.get("text"), "by": _owner(ev)})
        else:
            folded = False                            # a kind with no control key (vote_cast, node_edited, chat...)
        if folded and new:
            refs.append(seq)

    holders = sorted(o for o, (k, _) in pause_last.items() if k == "run_paused")
    other_claims = {n for n, h in holders_live.items() if _other_loop(h, loop)}
    note_lines = [f"{n['by']}: {n['text'][:NOTE_LINE_CAP]}" for n in reversed(notes[-NOTES_KEPT:])]
    chosen = chooses[-1] if chooses else None
    ops = []
    for o in sorted(opinions.values(), key=lambda o: o["seq"]):
        slot = "candidate" if CAND_RE.match(o["target"]) else "cluster"
        ops.append({slot: o["target"], "score": o["score"], "note": o["note"], "who": o["who"]})

    server = {
        "add_nodes": sorted(add_nodes.values(), key=lambda s: s["by_seq"]),
        "skip_nodes": sorted({n for n, (k, _) in skip_last.items() if k == "node_skipped"} | other_claims),
        "veto": sorted(q for q, (k, _) in veto_last.items() if k == "question_vetoed"),
        "choose": chosen["question"] if chosen else None,
        "opinions": ops,
        "note": "\n".join(note_lines)[:NOTE_CAP],
        "pause": bool(holders),
        "findings": _findings_out(findings),
    }
    assert tuple(server) == CONTROL_KEYS
    control = {k: v for k, v in file_ctl.items() if k in FILE_ONLY_KEYS} if isinstance(file_ctl, dict) else {}
    control.update(server)                            # rule 12: a server key replaces the file key
    overwrote = [{"seq": c["seq"], "by": c["by"]} for c in chooses[:-1] if chosen and c["by"] != chosen["by"]]
    return {"control": control, "refs": sorted(set(refs) | set(claim_refs)), "steps": steps, "holders": holders,
            "disputes": disputes, "seeds": seeds, "overwrote": {"choose": overwrote}, "dropped": dropped}


def _findings_out(findings: list[dict]) -> list[dict]:
    """Newest first; a finding named by a later replaces is marked replaced_by, and both stay (nothing is deleted)."""
    by_seq = {f["seq"]: dict(f, replaced_by=None) for f in findings}
    for f in findings:
        if f["replaces"] in by_seq:
            by_seq[f["replaces"]]["replaced_by"] = f["seq"]
    return [by_seq[f["seq"]] for f in reversed(findings)]


def consume_step(merged: dict, round_no, stage) -> dict | None:
    """The first step in `merged["steps"]` that names this boundary, or None. Its seq joins `merged["refs"]`
    (rule 11: control_applied names the consumed step). A step for another boundary stays and is ignored."""
    for st in merged.get("steps") or []:
        if str(st.get("stage")) == str(stage) and str(st.get("round")) == str(round_no):
            merged["refs"] = sorted(set(merged.get("refs") or []) | {st["seq"]})
            return st
    return None


def overlay_file(ctl: dict, file_ctl: dict | None) -> dict:
    """Put the FILE_ONLY_KEYS of the disk control.json under the server's control. Returns a new dict.
    `ctl` is the control dict, or a whole merge result (then its inner `control` is overlaid and the rest kept).
    Any other file key (note, skip_nodes, veto, choose, opinions, add_nodes, pause) is ignored."""
    if isinstance(ctl, dict) and isinstance(ctl.get("control"), dict) and "refs" in ctl:
        return {**ctl, "control": overlay_file(ctl["control"], file_ctl)}
    out = dict(ctl or {})
    if isinstance(file_ctl, dict):                    # the disk file is the only source of the file-only keys
        for k in FILE_ONLY_KEYS:
            out.pop(k, None)
            if k in file_ctl:
                out[k] = file_ctl[k]
    return out


def ignored_file_keys(file_ctl: dict | None) -> list[str]:
    """The file keys that --space ignores (for the loop's one log line)."""
    return sorted(k for k in (file_ctl or {}) if k not in FILE_ONLY_KEYS)


def render_control_json(path, ctl, retries_ms=50, give_up_s=3.0) -> None:
    """Write `ctl` to `<path>.tmp`, then os.replace it onto `path`. On Windows a reader that holds the target open
    makes os.replace raise PermissionError: retry every `retries_ms` ms for up to `give_up_s` s, then re-raise."""
    path = os.fspath(path)
    tmp = path + ".tmp"
    body = (json.dumps(ctl, indent=1, sort_keys=True, ensure_ascii=True) + "\n").encode("ascii")
    deadline = time.monotonic() + float(give_up_s)
    while True:
        try:
            with open(tmp, "wb") as f:
                f.write(body)
            os.replace(tmp, path)
            return
        except PermissionError:
            if time.monotonic() >= deadline:
                try:
                    os.remove(tmp)
                except OSError:
                    pass
                raise
            time.sleep(max(0.001, retries_ms / 1000.0))
