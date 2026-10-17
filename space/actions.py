"""The person-agent actions: one table for the prompt list, the JSON schema, the validator and the
action-to-event mapping (docs/MULTIPLAYER_DESIGN.md section 6.7, research note 03 section 7.8).

Everything here is pure: no network, no model, no clock. space/agent.py does the IO.

A SpaceView wraps one GET /api/snapshot answer and resolves the ids a person or the model names
(parts, ideas, questions, facts). `to_ops` turns one validated action into ops for the agent to run:
  {"op": "event", "kind", "subject", "label", "data"}           POST /api/events by <me>.agent
  {"op": "claim", "action": "acquire"|"release", "subject", "purpose"}   POST /api/claims
  {"op": "say", "text"}                                         a line to the person, no event
`parse_slash` turns a slash command (contract.SLASH) into the same ops with no model call.
The agent never writes a result or a status: OUT_KINDS is the whole list of kinds it may post.
Standard library only.
"""
from __future__ import annotations

import difflib
import json
import re

from . import contract as C

ENUMS = {
    "evidence_tag": ["measured", "script", "web", "belief"],
    "value": ["up", "down"],
    "answerer": ["agents", "people", "either"],
    "kind": ["evidence", "objection"],
    "confidence": ["clear", "guess"],
}
# (type, what it does, how the service applies it, fields)
ACTIONS = [
    ("add_branch", "add a part or sub-part to the tree", "auto",
     [("parent", "string"), ("name", "string"), ("frame", "string"), ("assumptions", "string[]"), ("claim", "boolean")]),
    ("add_problem", "start a new top-level problem", "confirm", [("name", "string"), ("goal", "string"), ("success", "string")]),
    ("dispute_fact", "mark a fact on the map as disputed", "confirm",
     [("fact", "string"), ("reason", "string"), ("evidence_tag", "enum:evidence_tag"), ("evidence_ref", "string")]),
    ("vote", "vote on an idea", "auto", [("idea", "string"), ("value", "enum:value")]),
    ("claim_branch", "mark a part as yours for a while", "auto", [("branch", "string"), ("takeover", "boolean")]),
    ("release_branch", "remove your claim on a part", "auto", [("branch", "string")]),
    ("ask_team", "put an open question to the agents or to the other people", "auto",
     [("question", "string"), ("branch", "string"), ("answerer", "enum:answerer"), ("test", "string"), ("threshold", "string"), ("fails_if", "string")]),
    ("run_round", "ask the team to run more rounds now", "confirm", [("rounds", "integer"), ("focus", "string[]")]),
    ("seed_idea", "give the idea agents a mechanism of your own to explore on a part", "auto", [("part", "string"), ("text", "string")]),
    ("comment", "attach evidence or an objection to an idea, part or fact", "auto",
     [("target", "string"), ("kind", "enum:kind"), ("text", "string")]),
    ("note", "leave a note that every agent reads", "auto", [("text", "string")]),
]
COMMON = [("confidence", "enum:confidence"), ("why", "string")]
APPLY = {name: how for name, _, how, _ in ACTIONS}
MAX_ACTIONS = 3

# The kinds a person-agent may post. Never a result, a status, a pick or a server kind.
OUT_KINDS = frozenset({"node_added", "node_skipped", "node_unskipped", "seed_added", "vote_cast", "reply_posted",
                       "note_posted", "fact_disputed", "question_vetoed", "question_unvetoed", "question_chosen",
                       "run_paused", "run_resumed", "run_step", "agent_said", "intent_proposed", "digest_taken"})
assert OUT_KINDS <= set(C.KINDS)
NAME_CAP, FRAME_CAP, ASSUMPTION_CAP, ASSUMPTIONS_KEPT, REASON_CAP = 60, 400, 160, 5, 600
DUP_RATIO = 0.85


# ---------------------------------------------------------------- schema, prompt list, validator (note 03 7.8)
def prop(t):
    if t.startswith("enum:"):
        return {"type": "string", "enum": ENUMS[t[5:]]}
    if t == "string[]":
        return {"type": "array", "items": {"type": "string"}}
    return {"type": t}


def schema():
    branches = []
    for name, _, _, fields in ACTIONS:
        props = {"type": {"type": "string", "enum": [name]}}
        props.update({f: prop(t) for f, t in fields + COMMON})
        branches.append({"type": "object", "properties": props, "required": list(props), "additionalProperties": False})
    return {"type": "object",
            "properties": {"reply": {"type": "string"}, "ask": {"type": "string"},
                           "actions": {"type": "array", "items": {"anyOf": branches}}},
            "required": ["reply", "ask", "actions"], "additionalProperties": False}


def prompt_lines():
    return "\n".join(f"{n}: {d}. Fields: {', '.join(f for f, _ in fields)}." for n, d, _, fields in ACTIONS)


def validate(out):
    """[errors] for one model reply; an empty list means the reply has the right shape."""
    if not isinstance(out, dict):
        return [f"reply is {type(out).__name__}, not an object"]
    errs = []
    if set(out) != {"reply", "ask", "actions"}:
        errs.append(f"envelope keys {sorted(out)}")
    for k in ("reply", "ask"):
        if k in out and not isinstance(out[k], str):
            errs.append(f"{k} not str")
    acts = out.get("actions", [])
    if not isinstance(acts, list):
        return errs + ["actions not a list"]
    by = {n: [f for f, _ in fields] + [f for f, _ in COMMON] for n, _, _, fields in ACTIONS}
    types = {n: dict(fields + COMMON) for n, _, _, fields in ACTIONS}
    for a in acts:
        if not isinstance(a, dict):
            errs.append("action not an object"); continue
        t = a.get("type")
        if t not in by:
            errs.append(f"unknown type {t}"); continue
        if set(a) != set(by[t]) | {"type"}:
            errs.append(f"{t}: fields {sorted(set(a) ^ (set(by[t]) | {'type'}))}")
        for f, ty in types[t].items():
            v = a.get(f)
            if ty.startswith("enum:") and v not in ENUMS[ty[5:]]:
                errs.append(f"{t}.{f}={v!r}")
            if ty == "boolean" and not isinstance(v, bool):
                errs.append(f"{t}.{f} not bool")
            if ty == "integer" and (isinstance(v, bool) or not isinstance(v, int)):
                errs.append(f"{t}.{f} not int")
            if ty == "string[]" and not (isinstance(v, list) and all(isinstance(x, str) for x in v)):
                errs.append(f"{t}.{f} not list of str")
            if ty == "string" and not isinstance(v, str):
                errs.append(f"{t}.{f} not str")
    if len(acts) > MAX_ACTIONS:
        errs.append(f"more than {MAX_ACTIONS} actions")
    return errs


def parse_last_json(text):
    """The last top-level JSON object in a model reply, or None (note 03 section 7.6)."""
    dec, found, i = json.JSONDecoder(), None, 0
    text = text or ""
    while True:
        i = text.find("{", i)
        if i < 0:
            return found
        try:
            obj, end = dec.raw_decode(text, i)
        except ValueError:
            i += 1
            continue
        if isinstance(obj, dict):
            found = obj
        i = end


def needs_ok(action):
    """Policy (6.7): confirm actions, any guess, and a takeover wait for the person's Apply."""
    return (APPLY.get(action.get("type")) == "confirm" or action.get("confidence") == "guess"
            or (action.get("type") == "claim_branch" and action.get("takeover") is True))


# ---------------------------------------------------------------- text helpers
def clean_text(s, cap=None):
    """People's text as data: angle brackets removed, whitespace folded, cut."""
    s = re.sub(r"\s+", " ", re.sub(r"[<>]", "", str(s or ""))).strip()
    return s[:cap] if cap else s


def clean_text_block(s, cap=None):
    """Like clean_text, but keeps the line breaks (for the digest block)."""
    lines = [re.sub(r"[ \t]+", " ", ln).strip() for ln in re.sub(r"[<>]", "", str(s or "")).splitlines()]
    s = "\n".join(ln for ln in lines if ln)
    return s[:cap] if cap else s


def clean_id(name):
    """The loop's id cleaning (nano/loop.py _add_human_nodes) after spaces become underscores."""
    s = re.sub(r"\s+", "_", str(name or "").strip().lower())
    return re.sub(r"[^a-z0-9_]", "", s)[:16].strip("_")


def display(owner):
    owner = str(owner or "").split(".")[0]
    return owner[:1].upper() + owner[1:]


def _norm(s):
    return re.sub(r"[^a-z0-9]+", " ", str(s or "").lower()).strip()


# ---------------------------------------------------------------- the space, from GET /api/snapshot
class SpaceView:
    def __init__(self, snap, me):
        snap = snap if isinstance(snap, dict) else {}
        self.snap, self.me = snap, me
        self.run = snap.get("run") or {}
        self.nodes = {}
        for n in snap.get("nodes") or []:
            if isinstance(n, dict) and n.get("id"):
                self.nodes[str(n["id"])] = n
        self.clusters = {}
        for c in snap.get("clusters") or []:
            if isinstance(c, dict) and (c.get("key") or c.get("cluster_id")):
                self.clusters[str(c.get("key") or c.get("cluster_id"))] = c
        self.facts = {}
        for f in snap.get("facts") or []:
            if isinstance(f, dict) and f.get("id"):
                self.facts[str(f["id"])] = {"node": f.get("node") or f.get("part") or "", "text": str(f.get("text") or ""),
                                            "state": f.get("state") or "ok"}
        for nid, n in self.nodes.items():           # a node's assumptions are its facts: id <node>:<n>
            for i, a in enumerate(n.get("assumptions") or [], 1):
                self.facts.setdefault(f"{nid}:{i}", {"node": nid, "text": str(a), "state": "ok"})
        q = snap.get("questions") or {}
        self.preview = list(((q.get("preview") or {}).get("top3")) or [])
        self.questions = {}
        for row in self.preview:
            if isinstance(row, dict) and row.get("id"):
                self.questions[str(row["id"])] = row
        for row in ((q.get("picked") or {}).get("top3")) or []:
            if isinstance(row, dict) and row.get("id"):
                self.questions.setdefault(str(row["id"]), row)
        self.vetoed = {str(v.get("question")): v.get("by") for v in q.get("vetoed") or [] if isinstance(v, dict)}
        self.chosen = q.get("chosen") or None

    # ---- resolving what a person or the model names
    def node(self, tok):
        """A node id from an id, a cleaned name or an exact name; None when absent."""
        t = str(tok or "").strip().strip('"')
        if t.startswith("node:"):
            t = t[5:]
        if t in self.nodes:
            return t
        low = t.lower()
        for nid, n in self.nodes.items():
            if nid.lower() == low or _norm(n.get("name")) == _norm(t):
                return nid
        cid = clean_id(t)
        return cid if cid in self.nodes else None

    def idea(self, tok):
        """A cluster key from a key, a cluster_id or a name (exact, or a unique part of one)."""
        t = str(tok or "").strip().strip('"')
        if t.startswith("cluster:"):
            t = t[8:]
        if t in self.clusters:
            return t
        for k, c in self.clusters.items():
            if t and t in (str(c.get("cluster_id") or ""), str(c.get("key") or "")):
                return k
        hits = [k for k, c in self.clusters.items() if _norm(c.get("name")) == _norm(t)]
        if len(hits) == 1:
            return hits[0]
        hits = [k for k, c in self.clusters.items() if _norm(t) and _norm(t) in _norm(c.get("name"))]
        return hits[0] if len(hits) == 1 else None

    def question(self, tok):
        """A question id; Q1, Q2, Q3 name the preview's top 3 in order."""
        t = str(tok or "").strip().strip('"<>')
        if t.startswith("question:"):
            t = t[9:]
        if t in self.questions:
            return t
        m = re.fullmatch(r"[qQ]([1-3])", t)
        if m and len(self.preview) >= int(m.group(1)):
            return str(self.preview[int(m.group(1)) - 1].get("id"))
        return None

    def fact(self, tok):
        t = str(tok or "").strip().strip('"')
        if t.startswith("fact:"):
            t = t[5:]
        return t if t in self.facts else None

    def name_of(self, nid):
        n = self.nodes.get(nid) or {}
        return str(n.get("name") or nid)

    def idea_name(self, key):
        return str((self.clusters.get(key) or {}).get("name") or key)

    def question_text(self, qid):
        return str((self.questions.get(qid) or {}).get("text") or qid)

    def claim_on(self, nid):
        """{holder, ttl_left_s} when someone holds node nid, else None."""
        n = self.nodes.get(nid) or {}
        c = n.get("claim")
        if isinstance(c, dict) and c.get("holder"):
            return c
        for c in self.snap.get("claims") or []:
            if isinstance(c, dict) and c.get("subject") == f"node:{nid}":
                return {"holder": c.get("holder") or c.get("owner"), "ttl_left_s": c.get("ttl_left_s")}
        return None

    def children(self, parent):
        return [nid for nid, n in self.nodes.items() if n.get("parent") == parent]

    # ---- boundaries (6.6 and 4.7)
    def boundary(self):
        """(round, stage) where a queued item is used: the boundary the loop waits at, else the next one."""
        return next_boundary(self.run)

    def boundary_text(self):
        r, s = self.boundary()
        return f"{s}, round {r}"

    def pick_round(self):
        return int(self.run.get("round") or 1) + 1


def next_boundary(run):
    run = run or {}
    stage, r = run.get("stage"), int(run.get("round") or 1)
    if stage not in C.STAGES:
        return (r, "planned")
    if run.get("waiting"):
        return (r, stage)
    if stage == "verified":
        return (r + 1, "ideated")
    return (r, C.STAGES[C.STAGES.index(stage) + 1])


def boundary_after(rnd, stage):
    if stage == "verified":
        return (rnd + 1, "ideated")
    return (rnd, C.STAGES[C.STAGES.index(stage) + 1])


# ---------------------------------------------------------------- the <space> block (note 03 section 7.4)
SPACE_CAP, TREE_LINES, TREE_DEPTH, FACTS_MAX, IDEAS_MAX, QUESTIONS_MAX = 6000, 60, 4, 30, 15, 5


def render_space(view, open_intent=None, held=()):
    """The <space> block: fixed order, fixed columns, under 6000 characters. Never obvious, obvious_match,
    private, spend or a model name: only the listed fields are read."""
    me, run = view.me, view.run
    problem = clean_text(view.snap.get("problem") or run.get("problem") or "-", 40)
    head = (f"problem: {problem} | round {run.get('round') or 1} | stage: {run.get('stage') or 'not started'}"
            f"{' (waiting for Go)' if run.get('waiting') else ''} | you: {me}")
    lines = [head, "TREE (id | name | made by | held by | state)"]
    n_clusters = {}
    for c in view.clusters.values():
        n_clusters[c.get("node")] = n_clusters.get(c.get("node"), 0) + 1
    disputed = {}
    for f in view.facts.values():
        if str(f.get("state", "")).startswith("disputed"):
            disputed[f["node"]] = disputed.get(f["node"], 0) + 1
    order = list(view.nodes)
    kids = {}
    for nid in order:
        kids.setdefault(view.nodes[nid].get("parent"), []).append(nid)
    roots = [nid for nid in order if view.nodes[nid].get("parent") not in view.nodes]
    tree_lines = []

    def walk(nid, depth):
        if depth > TREE_DEPTH or len(tree_lines) >= TREE_LINES:
            return
        n = view.nodes[nid]
        made = "map" if n.get("origin") in (None, "map") else clean_text(n.get("owner") or n.get("by") or n.get("origin"), 20)
        c = view.claim_on(nid)
        held_by = "-"
        if c:
            ttl = c.get("ttl_left_s")
            held_by = clean_text(c.get("holder"), 24) + (f", {int(float(ttl))} s left" if ttl is not None else "")
        state = []
        k = n_clusters.get(nid, 0)
        if k:
            state.append(f"{k} cluster" + ("s" if k > 1 else ""))
        elif n.get("origin") not in (None, "map"):
            state.append("new, no ideas yet")
        else:
            state.append("no clusters yet")
        if n.get("kind") == "question":
            state.append("question")
        if n.get("status") in ("pending", "queued", "rejected"):
            state.append(str(n["status"]))
        nd = disputed.get(nid, 0) + len(n.get("disputed") or [])
        if nd:
            state.append(f"{nd} disputed fact" + ("s" if nd > 1 else ""))
        if n.get("skipped_by"):
            state.append(f"skipped by {clean_text(n['skipped_by'], 20)}")
        if n.get("lowered"):
            state.append("lowered")
        tree_lines.append(f"{'  ' * depth}{nid} | {clean_text(n.get('name'), NAME_CAP)} | {made} | {held_by} | {', '.join(state)}")
        for kid in kids.get(nid, []):
            walk(kid, depth + 1)

    for r in roots:
        walk(r, 0)
    lines += tree_lines or ["(no parts yet)"]
    facts = sorted(view.facts.items(), key=lambda kv: (not str(kv[1].get("state", "")).startswith("disputed"),))
    lines.append("FACTS (id | part | text | state)")
    for fid, f in facts[:FACTS_MAX]:
        lines.append(f"{fid} | {f['node']} | {clean_text(f['text'], 160)} | {clean_text(f.get('state') or 'ok', 40)}")
    ideas = sorted(view.clusters.items(), key=lambda kv: (not kv[1].get("selected"), -int(kv[1].get("n") or 0)))
    lines.append("IDEAS (id | part | name | state)")
    for key, c in ideas[:IDEAS_MAX]:
        st = str(c.get("status") or "open")
        if st not in ("open", "built"):
            st = f"tested, {st}"
        lines.append(f"{key} | {c.get('node')} | {clean_text(c.get('name'), 80)} | {st}")
    lines.append("QUESTIONS (id | text | asked by | state)")
    qrows = []
    chosen = (view.chosen or {}).get("question") if isinstance(view.chosen, dict) else None
    for i, row in enumerate(view.preview[:3], 1):
        qid = str(row.get("id"))
        st = "open"
        if qid in view.vetoed:
            st = f"vetoed by {view.vetoed[qid]}"
        elif qid == chosen:
            st = f"chosen by {(view.chosen or {}).get('by')}"
        qrows.append(f"{qid} (Q{i}) | {clean_text(row.get('text'), 160)} | team | {st}")
    for nid, n in view.nodes.items():
        if n.get("kind") == "question" and n.get("origin") == "human":
            qrows.append(f"{nid} | {clean_text(n.get('name'), 160)} | {clean_text(n.get('owner') or n.get('by'), 20)} | open")
    lines += qrows[:QUESTIONS_MAX]
    lines.append("YOURS")
    mine = [nid for nid in view.nodes if (view.claim_on(nid) or {}).get("holder") in (me, f"{me}.agent")]
    mine += [s[5:] for s in held if s.startswith("node:") and s[5:] not in mine]
    lines.append(f"held by you: {', '.join(mine) if mine else '-'}")
    lines.append(f"waiting for your OK: {open_intent or 'nothing'}")
    text = "\n".join(lines)
    while len(text) > SPACE_CAP and len(lines) > 8:     # drop from the middle of the longest list
        lines.pop(len(lines) // 2)
        text = "\n".join(lines)
    return text[:SPACE_CAP]


# ---------------------------------------------------------------- action -> ops (the 6.7 mapping)
class Dropped(Exception):
    """An action that names something not in the space, or misses a needed detail. The text says which."""


def _ev(kind, subject, label, data):
    assert kind in OUT_KINDS, kind
    return {"op": "event", "kind": kind, "subject": subject, "label": clean_text(label, 80) or None, "data": data}


def _say(text):
    return {"op": "say", "text": text}


def _node_or_drop(view, tok, what):
    nid = view.node(tok)
    if not nid:
        raise Dropped(f'{what}: no part "{clean_text(tok, 60)}" in the space')
    return nid


def branch_ops(view, parent, name, frame, assumptions=(), claim=False):
    pid = _node_or_drop(view, parent, "add_branch")
    name = clean_text(name, NAME_CAP)
    nid = clean_id(name)
    if not nid:
        raise Dropped("add_branch: the part needs a name")
    for kid in view.children(pid):           # same parent and a close name: merge into the older part
        if difflib.SequenceMatcher(None, _norm(view.name_of(kid)), _norm(name)).ratio() >= DUP_RATIO:
            return [_say(f'"{view.name_of(kid)}" is already under {view.name_of(pid)} as {kid}, so I did not add a copy. '
                         f"I can comment on it or claim it for you.")]
    if nid in view.nodes:
        return [_say(f'dropped: id in use. "{nid}" is already on the map ({view.name_of(nid)}). '
                     f"I can comment on it instead.")]
    data = {"id": nid, "name": name, "parent": pid, "frame": clean_text(frame, FRAME_CAP),
            "assumptions": [clean_text(a, ASSUMPTION_CAP) for a in (assumptions or [])][:ASSUMPTIONS_KEPT],
            "directions": ["inward", "outward"], "origin": "human", "kind": "part"}
    ops = [_ev("node_added", f"node:{nid}", name, data)]
    if claim:
        ops.append({"op": "claim", "action": "acquire", "subject": f"node:{nid}", "purpose": f"ideas for {name}"})
    return ops


def run_step_ops(view, rounds=1):
    r, s = view.boundary()
    ops = [_ev("run_step", "run:main", f"{s} r{r}", {"round": r, "stage": s})]
    if rounds >= 2:
        r2, s2 = boundary_after(r, s)
        ops.append(_ev("run_step", "run:main", f"{s2} r{r2}", {"round": r2, "stage": s2}))
    return ops


def to_ops(action, view):
    """The ops for one validated action. Raises Dropped when an id is unknown or a detail is missing."""
    t = action.get("type")
    if t == "add_branch":
        return branch_ops(view, action["parent"], action["name"], action["frame"], action["assumptions"], action["claim"])
    if t == "add_problem":
        text = clean_text(f"new problem proposed: {action['name']}. Goal: {action['goal']}. Success: {action['success']}", C.NOTE_CAP)
        return [_ev("note_posted", None, "note", {"text": text})]
    if t == "dispute_fact":
        fid = view.fact(action["fact"])
        if not fid:
            raise Dropped(f'dispute_fact: no fact "{clean_text(action["fact"], 40)}" in the space')
        if not clean_text(action["reason"]):
            raise Dropped("dispute_fact: a dispute needs a reason")
        f = view.facts[fid]
        return [_ev("fact_disputed", f"fact:{fid}", view.name_of(f["node"]),
                    {"node": f["node"], "fact": clean_text(f["text"], 300), "reason": clean_text(action["reason"], REASON_CAP),
                     "tag": action["evidence_tag"], "ref": clean_text(action["evidence_ref"], 300)})]
    if t == "vote":
        key = view.idea(action["idea"])
        if not key:
            raise Dropped(f'vote: no idea "{clean_text(action["idea"], 40)}" in the space')
        c = view.clusters[key]
        return [_ev("vote_cast", f"cluster:{c.get('cluster_id') or key}", view.idea_name(key),
                    {"idea": key, "value": 1 if action["value"] == "up" else -1})]
    if t == "claim_branch":
        nid = _node_or_drop(view, action["branch"], "claim_branch")
        if action["takeover"]:
            return [_say(f"Your browser takes {view.name_of(nid)} over when you press Apply. A takeover is yours to send.")]
        return [{"op": "claim", "action": "acquire", "subject": f"node:{nid}", "purpose": clean_text(action.get("why"), 120)}]
    if t == "release_branch":
        nid = _node_or_drop(view, action["branch"], "release_branch")
        return [{"op": "claim", "action": "release", "subject": f"node:{nid}"}]
    if t == "ask_team":
        q = clean_text(action["question"], 300)
        if not q:
            raise Dropped("ask_team: the question is empty")
        bid = view.node(action["branch"]) if clean_text(action["branch"]) else None
        if clean_text(action["branch"]) and not bid:
            raise Dropped(f'ask_team: no part "{clean_text(action["branch"], 60)}" in the space')
        if all(clean_text(action[k]) for k in ("test", "threshold", "fails_if")):
            nid = clean_id("q_" + q)
            n = 2
            while nid in view.nodes:
                nid = clean_id(f"q{n}_" + q); n += 1
            return [_ev("node_added", f"node:{nid}", q[:NAME_CAP],
                        {"id": nid, "name": q[:NAME_CAP], "parent": bid or "root", "frame": q, "assumptions": [],
                         "directions": ["inward", "outward"], "origin": "human", "kind": "question",
                         "test": clean_text(action["test"], 200), "threshold": clean_text(action["threshold"], 100),
                         "fails_if": clean_text(action["fails_if"], 200), "answerer": action["answerer"]})]
        where = f" on {view.name_of(bid)}" if bid else ""
        return [_ev("note_posted", f"node:{bid}" if bid else None, "question",
                    {"text": clean_text(f"question for {action['answerer']}{where}: {q}", C.NOTE_CAP)})]
    if t == "run_round":
        return run_step_ops(view, max(1, min(2, int(action["rounds"] or 1))))
    if t == "seed_idea":
        nid = _node_or_drop(view, action["part"], "seed_idea")
        text = clean_text(action["text"], C.SEED_CAP)
        if not text:
            raise Dropped("seed_idea: the seed is empty")
        return [_ev("seed_added", f"node:{nid}", view.name_of(nid), {"node": nid, "text": text})]
    if t == "comment":
        text = clean_text(action["text"], C.NOTE_CAP)
        key = view.idea(action["target"])
        if key:
            c = view.clusters[key]
            data = {"node": c.get("node"), "idea": c.get("cluster_id") or key, "objection": 0, "text": text}
            if action["kind"] == "objection":
                data.update(kind="objection")
            else:
                data.update(kind="rebut", fact=text, source="belief")
            return [_ev("reply_posted", f"cluster:{c.get('cluster_id') or key}", view.idea_name(key), data)]
        nid = view.node(action["target"])
        fid = view.fact(action["target"])
        if not nid and not fid:
            raise Dropped(f'comment: no idea, part or fact "{clean_text(action["target"], 40)}" in the space')
        on = view.name_of(nid) if nid else f"fact {fid}"
        return [_ev("note_posted", f"node:{nid or view.facts[fid]['node']}", "comment",
                    {"text": clean_text(f"{action['kind']} on {on}: {text}", C.NOTE_CAP)})]
    if t == "note":
        text = clean_text(action["text"], C.NOTE_CAP)
        if not text:
            raise Dropped("note: the note is empty")
        return [_ev("note_posted", None, "note", {"text": text})]
    raise Dropped(f"unknown action {t}")


# ---------------------------------------------------------------- intent cards (note 04 section 6.2)
def intent_card(action, view, me):
    t = action.get("type")
    who = f"{display(me)}'s agent"
    on, will = "the space", t
    if t == "dispute_fact":
        f = view.facts.get(view.fact(action.get("fact")) or "", {})
        on = view.name_of(f.get("node")) if f else str(action.get("fact"))
        will = f'mark the fact "{clean_text(f.get("text") or action.get("fact"), 120)}" as disputed ({action.get("evidence_tag")})'
    elif t == "run_round":
        r, s = view.boundary()
        n = max(1, min(2, int(action.get("rounds") or 1)))
        will = f"press Go for {s}, round {r}" + (" and the boundary after it" if n == 2 else "")
        on = "the run"
    elif t == "add_problem":
        will = "leave a note: a new top-level problem is not on day one"
        on = clean_text(action.get("name"), 60)
    elif t == "claim_branch":
        nid = view.node(action.get("branch"))
        on = view.name_of(nid) if nid else str(action.get("branch"))
        will = "take this part over (your browser sends the takeover)" if action.get("takeover") else "claim this part for you"
    elif t == "add_branch":
        will = f'add the part "{clean_text(action.get("name"), 60)}"'
        nid = view.node(action.get("parent"))
        on = view.name_of(nid) if nid else str(action.get("parent"))
    elif t == "vote":
        key = view.idea(action.get("idea"))
        will, on = f"vote {action.get('value')}", view.idea_name(key) if key else str(action.get("idea"))
    elif t == "seed_idea":
        nid = view.node(action.get("part"))
        will, on = f'seed "{clean_text(action.get("text"), 80)}"', view.name_of(nid) if nid else str(action.get("part"))
    elif t in ("note", "comment", "ask_team", "release_branch"):
        will = {"note": "leave a note", "comment": f"post a {action.get('kind')}", "ask_team": "put a question to the team",
                "release_branch": "release your claim"}[t]
        on = clean_text(action.get("target") or action.get("branch") or "the team", 60)
    because = clean_text(action.get("why"), 160) or "you asked"
    if action.get("confidence") == "guess":
        because += " (I chose between two readings)"
    return {"will": f"{who} will {will}", "on": on, "because": because,
            "apply_at": "on your Apply; the team reads it at " + view.boundary_text()}


# ---------------------------------------------------------------- slash commands (6.7), no model
SLASH_HELP = {
    "branch": '/branch <parent> "<name>": <frame> [--claim]', "vote": "/vote up|down <cluster key or name>",
    "claim": "/claim <node>", "release": "/release <node>", "dispute": "/dispute <node>: <fact> | <reason> [measured|script|web|belief]",
    "ask": "/ask <node>: <question> [| <test> | <threshold> | <fails if>]", "skip": "/skip <node>", "unskip": "/unskip <node>",
    "veto": "/veto <question id or Q1..Q3>", "unveto": "/unveto <question id or Q1..Q3>", "choose": "/choose <question id or Q1..Q3>",
    "note": "/note <text>", "reply": "/reply <cluster key> <objection n> concede|rebut|measure: <text> [tag]",
    "seed": "/seed <node>: <text>", "pause": "/pause [reason]", "resume": "/resume [reason]", "go": "/go",
}
assert set(SLASH_HELP) == set(C.SLASH)
TAGS = ("measured", "script", "web", "belief")
SLASH_RX = {
    "branch": re.compile(r'^(?P<parent>\S+)\s+"(?P<name>[^"]+)"\s*:?\s*(?P<frame>.*?)\s*(?P<claim>--claim)?\s*$', re.S),
    "vote": re.compile(r"^(?P<value>up|down)\s+(?P<idea>.+?)\s*$", re.I),
    "claim": re.compile(r"^(?P<node>\S.*?)\s*$"), "release": re.compile(r"^(?P<node>\S.*?)\s*$"),
    "dispute": re.compile(r"^(?P<node>[^:]+?)\s*:\s*(?P<fact>.+?)\s*\|\s*(?P<reason>.+?)\s*(?:\[?\b(?P<tag>measured|script|web|belief)\]?)?\s*$", re.S | re.I),
    "ask": re.compile(r"^(?P<node>[^:]+?)\s*:\s*(?P<rest>.+?)\s*$", re.S),
    "skip": re.compile(r"^(?P<node>\S.*?)\s*$"), "unskip": re.compile(r"^(?P<node>\S.*?)\s*$"),
    "veto": re.compile(r"^(?P<q>\S+)\s*$"), "unveto": re.compile(r"^(?P<q>\S+)\s*$"), "choose": re.compile(r"^(?P<q>\S+)\s*$"),
    "note": re.compile(r"^(?P<text>\S.*?)\s*$", re.S),
    "reply": re.compile(r"^(?P<idea>\S+)\s+(?P<n>\d+)\s+(?P<kind>concede|rebut|measure)\s*:\s*(?P<text>.+?)\s*(?:\[?\b(?P<tag>measured|script|web|belief)\]?)?\s*$", re.S | re.I),
    "seed": re.compile(r"^(?P<node>[^:]+?)\s*:\s*(?P<text>.+?)\s*$", re.S),
    "pause": re.compile(r"^(?P<reason>.*?)\s*$", re.S), "resume": re.compile(r"^(?P<reason>.*?)\s*$", re.S),
    "go": re.compile(r"^\s*$"),
}


def is_slash(text):
    return str(text or "").lstrip().startswith("/")


def parse_slash(text, view):
    """(ops, ack) for one slash command. Raises Dropped with a usage line when it does not parse or names
    something that is not in the space."""
    m = re.match(r"^\s*/(\w+)\s*(.*)$", str(text or ""), re.S)
    cmd = (m.group(1).lower() if m else "")
    if cmd not in SLASH_RX:
        raise Dropped(f"I do not know /{cmd}. Commands: " + ", ".join("/" + c for c in C.SLASH) + ".")
    g = SLASH_RX[cmd].match(m.group(2).strip())
    if not g:
        raise Dropped(f"Usage: {SLASH_HELP[cmd]}")
    a = g.groupdict()
    at = view.boundary_text()
    if cmd == "branch":
        ops = branch_ops(view, a["parent"], a["name"], a["frame"], (), bool(a["claim"]))
        if ops[0]["op"] == "say":
            return ops, ops[0]["text"]
        d = ops[0]["data"]
        ack = f"Queued: {d['name']} under {d['parent']}. The team reads it at {at}."
        return ops, ack + (" I am claiming it for you." if a["claim"] else "")
    if cmd == "vote":
        action = {"type": "vote", "idea": a["idea"], "value": a["value"].lower()}
        ops = to_ops(action, view)
        return ops, f"Vote {action['value']} on {ops[0]['label']}. Votes are shown by name; tests decide."
    if cmd in ("claim", "release"):
        nid = _node_or_drop(view, a["node"], cmd)
        purpose = f"{display(view.me)} works here"
        ops = [{"op": "claim", "action": "acquire" if cmd == "claim" else "release", "subject": f"node:{nid}", "purpose": purpose}]
        return ops, (f"Claiming {view.name_of(nid)} for you." if cmd == "claim" else f"Releasing {view.name_of(nid)}.")
    if cmd == "dispute":
        nid = _node_or_drop(view, a["node"], "dispute")
        fact = clean_text(a["fact"], 300)
        fid = view.fact(fact) or next((k for k, f in view.facts.items()        # an id like choice:1, or the text
                                       if f["node"] == nid and _norm(f["text"]) == _norm(fact)), None)
        if fid:
            fact = clean_text(view.facts[fid]["text"], 300)
        tag = (a.get("tag") or "belief").lower()
        ev = _ev("fact_disputed", f"fact:{fid}" if fid else f"node:{nid}", view.name_of(nid),
                 {"node": nid, "fact": fact, "reason": clean_text(a["reason"], REASON_CAP), "tag": tag, "ref": ""})
        return [ev], f'Disputed on {view.name_of(nid)}: "{fact[:80]}" ({tag}). It stays on the map, marked. The team reads it at {at}.'
    if cmd == "ask":
        parts = [p.strip() for p in a["rest"].split("|")]
        q, test, thr, fails = (parts + ["", "", ""])[:4]
        action = {"type": "ask_team", "question": q, "branch": a["node"], "answerer": "either",
                  "test": test, "threshold": thr, "fails_if": fails}
        ops = to_ops(action, view)
        kind = "a question on the map" if ops[0]["kind"] == "node_added" else "a question note"
        return ops, f"Queued: {kind}. The team reads it at {at}."
    if cmd in ("skip", "unskip"):
        nid = _node_or_drop(view, a["node"], cmd)
        ev = _ev("node_skipped" if cmd == "skip" else "node_unskipped", f"node:{nid}", view.name_of(nid), {"reason": ""})
        return [ev], f"Queued: {cmd} {view.name_of(nid)}. The team reads it at {at}."
    if cmd in ("veto", "unveto", "choose"):
        qid = view.question(a["q"])
        if not qid:
            raise Dropped(f'{cmd}: no question "{clean_text(a["q"], 40)}" in the space')
        kind = {"veto": "question_vetoed", "unveto": "question_unvetoed", "choose": "question_chosen"}[cmd]
        text = clean_text(view.question_text(qid), 160)
        ev = _ev(kind, f"question:{qid}", text, {"question": qid, "text": text})
        return [ev], f"Queued: {cmd} {qid}. It acts at the next pick, round {view.pick_round()}."
    if cmd == "note":
        text = clean_text(a["text"], C.NOTE_CAP)
        return [_ev("note_posted", None, "note", {"text": text})], f"Queued: your note. The team reads it at {at}."
    if cmd == "reply":
        key = view.idea(a["idea"])
        if not key:
            raise Dropped(f'reply: no idea "{clean_text(a["idea"], 40)}" in the space')
        c = view.clusters[key]
        tag = (a.get("tag") or "belief").lower()
        text = clean_text(a["text"], C.NOTE_CAP)
        data = {"node": c.get("node"), "idea": c.get("cluster_id") or key, "objection": int(a["n"]),
                "kind": a["kind"].lower(), "text": text, "source": tag}
        if tag != "belief" or a["kind"].lower() == "measure":
            data["fact"] = text
        ev = _ev("reply_posted", f"cluster:{c.get('cluster_id') or key}", view.idea_name(key), data)
        return [ev], f"Posted your {data['kind']} on {view.idea_name(key)}, objection {data['objection']}. A reply never gates a build."
    if cmd == "seed":
        ops = to_ops({"type": "seed_idea", "part": a["node"], "text": a["text"]}, view)
        r, s = view.boundary()
        when = (f"The inventors get it at {at}." if (r, s) in ((1, "planned"), (1, "ideated"))
                else "It is logged; seeds reach the inventors only in round 1.")
        return ops, f"Queued: your seed on {ops[0]['label']}. {when}"
    if cmd in ("pause", "resume"):
        kind = "run_paused" if cmd == "pause" else "run_resumed"
        ev = _ev(kind, "run:main", cmd, {"reason": clean_text(a["reason"], 200)})
        if cmd == "pause":
            return [ev], f"Queued: pause. The run holds at {at} until you resume."
        return [ev], "Queued: resume. Your pause is lifted."
    if cmd == "go":
        ops = run_step_ops(view, 1)
        d = ops[0]["data"]
        return ops, f"Go: releasing {d['stage']}, round {d['round']}."
    raise Dropped(f"Usage: {SLASH_HELP[cmd]}")
