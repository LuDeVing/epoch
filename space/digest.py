"""The peer digest: what teammates changed since a reader's last step (docs/MULTIPLAYER_DESIGN.md section 6.3).

Built by code, never by a model, so it cannot invent a change and it lands in milliseconds. `render_digest` is the
per-role text for prompt slots, `check_digest` is its checker, and `make_digest` is the generic panel text of
research_notes/multiplayer/02_realtime_sync.md Appendix A.1, kept for the page. Standard library only.
"""
from __future__ import annotations

import re

from space.contract import (CLOSING, DIGEST_CAP, DIGEST_HEAD, GLOBAL_KINDS, IDEA_SKIPS, KINDS, NO_DIGEST, PRIVATE_KEYS,
                            QUOTE_CAP, actor_class)

FIRST_FOR = {"critic", "author"}                   # rule 5: these roles read people's comments first
FIRST_KINDS = ("reply_posted", "fact_disputed")
LABEL_KEYS = {                                     # where a label comes from when the event carries none
    "opinion_given": ("target",), "vote_cast": ("idea",), "candidate_built": ("cluster_name", "cand", "idea"),
    "test_result": ("cluster_name", "cand", "idea"), "objection_raised": ("cluster_name", "idea"),
    "reply_posted": ("cluster_name", "idea"), "objection_marked": ("cluster_name", "idea"),
    "question_vetoed": ("text", "question"), "question_unvetoed": ("text", "question"),
    "question_chosen": ("text", "question"), "question_picked": ("text",), "finding_posted": ("title",),
}
CLAIM_WHO = {"claim_granted": "owner", "claim_released": "owner", "claim_taken_over": "to"}
SENTENCE_FIRST_WORDS = frozenset(v[4].split()[0] for v in KINDS.values() if v[4])
_PRIVATE_RE = re.compile(r"\b(" + "|".join(sorted(PRIVATE_KEYS, key=len, reverse=True)) + r")\b")
_PLACEHOLDER_RE = re.compile(r"\{(\w+)\}")


class _Missing(dict):
    def __missing__(self, k):
        return "?"


def q(s, n=QUOTE_CAP) -> str:
    """A quote from a person: tags stripped, whitespace folded, cut to n characters with '...'."""
    s = re.sub(r"<[^>]*>", "", str("" if s is None else s)).replace("<", "").replace(">", "")
    s = re.sub(r"\s+", " ", s).strip()
    return s if len(s) <= n else s[: n - 3].rstrip() + "..."


def strip_private(x):
    """A copy of x with every PRIVATE_KEYS key removed at any depth."""
    if isinstance(x, dict):
        return {k: strip_private(v) for k, v in x.items() if k not in PRIVATE_KEYS}
    if isinstance(x, (list, tuple)):
        return [strip_private(v) for v in x]
    return x


def _owner(ev: dict) -> str:
    by = str(ev.get("by") or "")
    return str(ev.get("owner") or by.split(".")[0])


def _class(ev: dict) -> str:
    return actor_class(str(ev.get("by") or ""), str(ev.get("by_kind") or ""), _owner(ev))


def _subject_node(subject) -> str | None:
    s = str(subject or "")
    if s.startswith("node:"):
        return s[5:]
    if s.startswith("fact:"):
        return s[5:].rsplit(":", 1)[0]
    return None


def _in_scope(ev: dict, scope: set[str]) -> bool:
    if ev.get("kind") in GLOBAL_KINDS:
        return True
    d = ev.get("data") if isinstance(ev.get("data"), dict) else {}
    names = {str(d[k]) for k in ("node", "parent") if d.get(k) not in (None, "")}
    sn = _subject_node(ev.get("subject"))
    if sn:
        names.add(sn)
    return bool(names & scope)


def _label(ev: dict, d: dict) -> str:
    if ev.get("label"):
        return str(ev["label"])
    ch = d.get("chosen") if ev.get("kind") == "question_picked" else None
    if isinstance(ch, dict):                       # the loop's pick record: chosen is the question itself
        ch = ch.get("text") or ch.get("id")
    elif ch not in (None, ""):                     # or its id: the text comes from top3
        top = [t for t in (d.get("top3") or []) if isinstance(t, dict) and t.get("id") == ch and t.get("text")]
        ch = top[0]["text"] if top else ch
    if ch not in (None, ""):
        return str(ch)
    for k in LABEL_KEYS.get(ev.get("kind"), ()) + ("name", "node"):
        if d.get(k) not in (None, ""):
            return str(d[k])
    s = str(ev.get("subject") or "")
    return s.split(":", 1)[1] if ":" in s else (s or "?")


def _metric(d: dict) -> str:
    mt = d.get("metrics") if isinstance(d.get("metrics"), dict) else {}
    nums = [(k, v) for k, v in mt.items() if isinstance(v, (int, float)) and not isinstance(v, bool)][:2]
    return ", ".join(f"{k} {round(v, 2)}" for k, v in nums) or q(d.get("reason", ""), 60)


def _who(ev: dict) -> str:
    cls = _class(ev)
    if cls == "person":
        return f"HUMAN {_owner(ev)}"
    if cls == "delegate":
        return f"{_owner(ev)} via agent"
    if cls == "team":
        return "the team"
    if cls == "server":                            # the server is never named; a claim line names its holder
        k = CLAIM_WHO.get(ev.get("kind"))
        d = ev.get("data") if isinstance(ev.get("data"), dict) else {}
        return str(d.get(k) or "") if k else ""
    return str(ev.get("by") or "")                 # an agent that acts for nobody is named by its id


def _sentence(ev: dict, mode: str) -> str:
    kind = ev["kind"]
    d = ev.get("data") if isinstance(ev.get("data"), dict) else {}
    f = _Missing({k: (q(v) if isinstance(v, str) else v) for k, v in d.items()})
    f["label"] = q(_label(ev, d), 80)
    f["parent"] = q(d.get("parent", "root"), 80)
    f["frame"] = q(d.get("frame", ""))
    f["node"] = q(d.get("node", ""), 80)
    f["why"] = f": {q(d['purpose'])}" if d.get("purpose") else ""
    f["metric"] = _metric(d) if kind == "test_result" else ""
    f["note"] = q(d.get("note", ""))
    if kind == "cluster_snapshot":
        f["n"] = d.get("n") if isinstance(d.get("n"), int) else len(d.get("clusters") or [])
    if kind == "memory_added":
        add = d.get("added")
        f["n_added"] = len(add) if isinstance(add, list) else (add if isinstance(add, int) else 0)
    if kind == "vote_cast":
        v = d.get("value")
        f["value"] = f"+{v}" if isinstance(v, int) and not isinstance(v, bool) and v > 0 else v
    if kind == "test_result":                     # the status word is the mode's own word (contract.STATUS_WORDS)
        f["status"] = q(d.get("status", "?"), 40)
    text = KINDS[kind][4].format_map(f)
    text = text.replace(' ()', '').replace(': ""', '')   # an empty note or frame leaves no empty brackets
    return text.rstrip()


def _kept(events, me: str, role: str, scope) -> list[dict]:
    team_reader = str(me).startswith("team.")
    sc = None if scope in (None, "") else ({str(scope)} if isinstance(scope, str) else {str(s) for s in scope})
    out = []
    for ev in events or ():
        if not isinstance(ev, dict) or not isinstance(ev.get("seq"), int):
            continue
        kind = ev.get("kind")
        if kind not in KINDS or kind in NO_DIGEST or ev.get("by") == me:
            continue
        if team_reader and _class(ev) == "team":
            continue
        if role == "idea" and kind in IDEA_SKIPS:
            continue
        if sc is not None and not _in_scope(ev, sc):
            continue
        out.append({**ev, "data": strip_private(ev.get("data") if isinstance(ev.get("data"), dict) else {})})
    return out


def render_digest(events, me, role, scope=None, cap=DIGEST_CAP, mode="check_only") -> str:
    """The digest text for one reader (`me`, an actor id) in one role, or '' when nothing qualifies.
    `scope` is a node id or the ids of a subtree; None keeps every part. `mode` is the run's mode; the status
    words of a test_result are already the mode's words, so it is kept for the callers and the page."""
    kept = _kept(events, me, role, scope)
    if not kept:
        return ""
    groups: dict[tuple, dict] = {}
    for ev in sorted(kept, key=lambda e: e["seq"]):
        k = (ev.get("by"), ev["kind"], ev.get("subject"))
        g = groups.setdefault(k, {"n": 0})
        g["n"] += 1
        g["ev"] = ev                               # the newest of the group, by seq
    first_roles = role in FIRST_FOR

    def key(g):
        ev = g["ev"]
        first = first_roles and ev["kind"] in FIRST_KINDS and _class(ev) in ("person", "delegate")
        return (0, 0, -ev["seq"]) if first else (1, KINDS[ev["kind"]][3], -ev["seq"])   # comments: newest first

    lines, human = [], []
    for g in sorted(groups.values(), key=key):
        ev = g["ev"]
        who = _who(ev)
        extra = f" (x{g['n']})" if g["n"] > 1 else ""
        lines.append(f"- {who + ' ' if who else ''}{_sentence(ev, mode)}{extra} [e{ev['seq']}]")
        human.append(_class(ev) == "person")
    seqs = [e["seq"] for e in kept]
    head = DIGEST_HEAD.format(first=min(seqs), last=max(seqs))
    close = CLOSING.get(role, CLOSING["person"])
    fixed = len(head) + 1 + len(close)
    if fixed + sum(len(ln) + 1 for ln in lines) <= cap:
        return "\n".join([head] + lines + [close])
    # The cap bites. HUMAN lines get the room first, then the rest in print order; a line that does not fit is
    # skipped and a shorter one after it may still fit. The kept lines print in the rule 5 order.
    room = len(f"({len(lines)} more changes are in the log.)") + 1
    keep, used = set(), fixed + room
    for i in sorted(range(len(lines)), key=lambda i: (not human[i], i)):
        if used + len(lines[i]) + 1 <= cap:
            keep.add(i)
            used += len(lines[i]) + 1
    foot = f"({len(lines) - len(keep)} more changes are in the log.)"
    return "\n".join([head] + [lines[i] for i in sorted(keep)] + [foot, close])


def _authors(events) -> set[str]:
    names = set()
    for ev in events or ():
        if not isinstance(ev, dict):
            continue
        names.add(str(ev.get("by") or ""))
        names.add(_owner(ev))
        d = ev.get("data") if isinstance(ev.get("data"), dict) else {}
        for k in ("owner", "to", "from", "owner_was"):
            if d.get(k):
                names.add(str(d[k]))
    return names - {""}


def _line_name(line: str) -> str | None:
    """The name a digest line starts with, or None (the team, or a server line with no name)."""
    body = line[2:]
    if body.startswith("HUMAN "):
        body = body[6:]
    if body.startswith("the team "):
        return None
    tok = body.split(" ", 1)[0]
    if not tok or tok in SENTENCE_FIRST_WORDS:
        return None
    return tok


def check_digest(text, events) -> dict:
    """Every [eN] exists in the slice, every name at the start of a line is an author in the slice, no private
    word appears. `chars` is the length; the caller checks it against its cap."""
    text = str(text or "")
    ids = {e.get("seq") for e in events or () if isinstance(e, dict)}
    cited = re.findall(r"\[e(\d+)\]", text)
    unknown_ids = sorted({f"e{c}" for c in cited if int(c) not in ids}, key=lambda s: int(s[1:]))
    authors = _authors(events)
    names = [n for ln in text.splitlines() if ln.startswith("- ") for n in [_line_name(ln)] if n]
    unknown_names = sorted({n for n in names if n not in authors})
    private_words = sorted(set(_PRIVATE_RE.findall(text)))
    return {"unknown_ids": unknown_ids, "unknown_names": unknown_names, "private_words": private_words,
            "chars": len(text)}


def placeholders(kind: str) -> list[str]:
    """The {names} a kind's digest sentence uses (for the contract tests)."""
    s = KINDS[kind][4] or ""
    return _PLACEHOLDER_RE.findall(s)


# ---- make_digest: the generic panel text of note 02 Appendix A.1 (no roles), kept for the page.
# Add a sentence per event kind in MD_FMT and the tier in MD_TIER to teach it a new kind.
MD_TIER = {"question_vetoed": 0, "question_chosen": 0, "node_skipped": 0, "node_unskipped": 0, "opinion_given": 0, "note_posted": 0,
           "comment_posted": 0, "node_added": 0, "claim_granted": 1, "claim_taken_over": 1, "claim_released": 1, "claim_expired": 1,
           "test_result": 1, "question_picked": 1, "objection_marked": 2, "objection_raised": 2, "reply_posted": 2,
           "cluster_snapshot": 3, "sketch_batch": 3, "memory_added": 3}
MD_FMT = {"node_added": 'added part "{label}"', "node_skipped": 'skipped part "{label}"', "node_unskipped": 'un-skipped part "{label}"',
          "question_vetoed": 'vetoed question "{label}"', "question_chosen": 'chose question "{label}" as next',
          "opinion_given": 'scored "{label}" {score}/10 ({note})', "note_posted": "left a note: {text}",
          "comment_posted": 'commented on "{label}": {text}', "claim_granted": 'is working on part "{label}"{why}; do not touch it',
          "claim_released": 'released part "{label}"', "claim_expired": 'claim of {owner_was} on part "{label}" ended (expired)',
          "claim_taken_over": 'took over part "{label}"', "test_result": 'test of "{label}": {status} {metric}',
          "question_picked": 'team question is now "{label}"', "objection_raised": 'raised a {severity} objection on "{label}"',
          "reply_posted": 'replied ({kind}) on "{label}"', "objection_marked": 'marked an objection on "{label}" {verdict}',
          "cluster_snapshot": 'regrouped part "{label}" into {n} clusters', "sketch_batch": 'added {count} sketches to part "{label}"',
          "memory_added": 'added a memory entry to part "{label}"'}


def make_digest(events, me, cap=1200):
    rows = [e for e in events if e["by"] != me and e["kind"] in MD_FMT]
    if not rows:
        return "", (events[-1]["seq"] if events else 0)
    merged = {}
    for e in rows:
        k, c = (e["by"], e["kind"], e.get("subject")), (e.get("data") or {}).get("count", 0)
        if k in merged:
            m = merged[k]; m["n"] += 1; m["last"] = e["seq"]; m["count"] += c; m["e"] = e       # show the newest
        else:
            merged[k] = {"e": e, "n": 1, "last": e["seq"], "count": c}

    def render(m):
        e = m["e"]; d = _Missing(e.get("data") or {})
        d["label"] = e.get("label") or e.get("subject") or "?"
        if e["kind"] == "sketch_batch":
            d["count"] = m["count"]
        d["why"] = (": " + d["purpose"]) if d.get("purpose") else ""
        if e["kind"] == "test_result":
            mt = d.get("metrics") or {}
            d["metric"] = ", ".join("%s %s" % (k, round(v, 2)) for k, v in list(mt.items())[:2] if isinstance(v, (int, float))) or d.get("reason", "")
        who = "" if e.get("by_kind") == "system" else ("HUMAN " if e.get("by_kind") == "human" else "") + e["by"]
        extra = " (x%d)" % m["n"] if m["n"] > 1 and e["kind"] != "sketch_batch" else ""
        return "- %s%s%s [e%d]" % (who + " " if who else "", MD_FMT[e["kind"]].format_map(d), extra, m["last"])
    order = sorted(merged.values(), key=lambda m: (MD_TIER.get(m["e"]["kind"], 5), -m["last"]))
    first, last_ = events[0]["seq"], events[-1]["seq"]
    head = "TEAM UPDATE: events e%d to e%d since your last step" % (first, last_)
    chosen, used = [], len(head) + 90
    for m in order:
        line = render(m)
        if used + len(line) + 1 <= cap:
            chosen.append((m["last"], line)); used += len(line) + 1
    left = len(order) - len(chosen)
    foot = ["(+%d more lines left out; GET /api/events?since=%d for all)" % (left, first - 1)] if left else []
    return "\n".join([head] + [l for _, l in sorted(chosen)] + foot), last_
