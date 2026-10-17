"""GET /api/snapshot: a pure Python reduce of the log (docs/MULTIPLAYER_DESIGN.md section 5.1).

Used for the page's first paint and for the person-agent's <space> view, so the Python agent keeps no copy of
the JS reducer. `build` is a pure function of the events, the live claims and the server facts it is given.
Status words follow section 4.7: a person's part is queued until a control_applied lists its seq, then applied;
a veto or choose turns applied only when a question_picked lists it. Standard library only.
"""
from __future__ import annotations

from space.contract import HUMAN_KINDS, actor_class
from space.store import clean_id

HUES = ("a", "b", "c")
MINE_KEPT = 3


def _cls(ev) -> str:
    return actor_class(ev.get("by") or "", ev.get("by_kind") or "", ev.get("owner") or "")


def _short(ev) -> str:
    d = ev.get("data") or {}
    for k in ("text", "name", "question", "fact", "target", "idea", "node"):
        v = d.get(k)
        if isinstance(v, str) and v:
            return v[:160]
    return ev.get("label") or ev.get("subject") or ev["kind"]


def _subject_id(ev, prefix: str):
    s = ev.get("subject") or ""
    return s[len(prefix):] if s.startswith(prefix) else None


def build(events, *, me=None, claims=(), epoch="", replay=None, head=None) -> dict:
    events = sorted(events, key=lambda e: e["seq"])
    applied = {}                                         # seq -> {round, stage, seq}
    for ev in events:
        if ev["kind"] == "control_applied":
            d = ev.get("data") or {}
            for r in d.get("refs") or []:
                applied.setdefault(r, {"round": d.get("round"), "stage": d.get("stage"), "seq": ev["seq"]})
    run = {"round": None, "stage": None, "waiting": False, "paused_by": [], "mode": None, "step_mode": False}
    people, nodes, clusters = [], {}, {}
    built, results = {}, {}                              # (node, idea) -> cand ; cand -> status
    questions = {"preview": None, "picked": None, "vetoed": [], "chosen": None}
    vetoes, picks, notes, votes, paused, mine = {}, [], [], {}, {}, []

    for ev in events:
        k, d, cls = ev["kind"], ev.get("data") or {}, _cls(ev)
        owner = ev.get("owner") or ""
        if cls in ("person", "delegate") and owner and owner not in people:
            people.append(owner)
        if k == "stage_entered":
            run.update(round=d.get("round"), stage=d.get("stage"), waiting=bool(d.get("waiting")),
                       step_mode=bool(d.get("step_mode", run["step_mode"])))
            if d.get("mode"):
                run["mode"] = d["mode"]
        elif k == "node_added" and d.get("id") is not None:
            nid = clean_id(d["id"])
            human = cls in ("person", "delegate")
            status = ("applied" if ev["seq"] in applied else "queued") if human else "map"
            nodes[nid] = {"id": nid, "name": d.get("name") or nid,
                          "parent": clean_id(d["parent"]) if d.get("parent") not in (None, "") else None,
                          "kind": d.get("kind") or "part", "origin": d.get("origin"), "by": owner,
                          "seq": ev["seq"], "status": status, "applied_at": applied.get(ev["seq"]) if human else None,
                          "skipped_by": None, "lowered": False, "claim": None, "disputed": []}
            for f in ("test", "threshold", "fails_if"):
                if d.get(f) is not None:
                    nodes[nid][f] = d[f]
        elif k == "node_edited":
            nid = _subject_id(ev, "node:")
            n = nodes.get(clean_id(nid)) if nid else None
            f = d.get("fields") or {}
            if n:
                if f.get("name"):
                    n["name"] = f["name"]
                if "priority" in f:
                    n["lowered"] = str(f["priority"]).lower() in ("low", "lowered", "down")
        elif k in ("node_skipped", "node_unskipped"):
            nid = _subject_id(ev, "node:") or d.get("node")
            n = nodes.get(clean_id(nid)) if nid else None
            if n:
                n["skipped_by"] = owner if k == "node_skipped" else None
        elif k == "fact_disputed":
            n = nodes.get(clean_id(d.get("node") or ""))
            if n:
                n["disputed"].append({"by": owner, "reason": d.get("reason"), "tag": d.get("tag"), "seq": ev["seq"]})
        elif k == "cluster_snapshot":
            key = (d.get("node"), d.get("direction"))
            clusters[key] = [dict(c, node=d.get("node"), direction=d.get("direction")) for c in d.get("clusters") or []
                             if isinstance(c, dict)]
        elif k == "candidate_built":
            built[(d.get("node"), d.get("idea"))] = d.get("cand")
        elif k == "test_result":
            results[d.get("cand")] = d.get("status")
        elif k == "question_preview":
            questions["preview"] = dict(d, seq=ev["seq"])
        elif k == "question_picked":
            questions["picked"] = dict(d, seq=ev["seq"])
            picks.append((ev["seq"], d))
        elif k in ("question_vetoed", "question_unvetoed"):
            q = d.get("question") or _subject_id(ev, "question:")
            if k == "question_vetoed":
                vetoes[q] = owner
            else:
                vetoes.pop(q, None)
        elif k == "question_chosen":
            questions["chosen"] = {"question": d.get("question") or _subject_id(ev, "question:"), "by": owner,
                                   "seq": ev["seq"], "overwrote": d.get("overwrote") or []}
        elif k == "note_posted":
            notes.append({"by": owner, "text": d.get("text"), "seq": ev["seq"]})
        elif k == "vote_cast":
            votes[(owner, d.get("idea"))] = d.get("value")
        elif k == "run_paused":
            paused[owner] = True
        elif k == "run_resumed":
            paused.pop(owner, None)
        if me and owner == me and cls in ("person", "delegate") and k in HUMAN_KINDS:
            mine.append(ev)

    run["paused_by"] = [p for p in paused]
    for c in claims or []:
        n = nodes.get(clean_id(str(c.get("subject", ""))[5:]))
        if n:
            n["claim"] = {"holder": c.get("owner"), "ttl_left_s": c.get("ttl_left_s"), "token": c.get("token")}

    out_clusters = []
    for (node, _direction), cl in clusters.items():
        for c in cl:
            cand = built.get((node, c.get("cluster_id")))
            status = (results.get(cand) or "built") if cand else "open"
            out_clusters.append({"node": c.get("node"), "direction": c.get("direction"), "cluster_id": c.get("cluster_id"),
                                 "name": c.get("name"), "n": c.get("n"), "members": c.get("members") or [],
                                 "selected": c.get("selected"), "lane": c.get("lane"), "prior": c.get("prior"),
                                 "status": status})
    questions["vetoed"] = [{"question": q, "by": b} for q, b in vetoes.items()]

    def mine_status(ev):
        d = ev.get("data") or {}
        if ev["kind"] in ("question_vetoed", "question_chosen"):
            q = d.get("question")
            later = [p for s, p in picks if s > ev["seq"]]
            if ev["kind"] == "question_vetoed" and any(q in (p.get("vetoed") or []) for p in later):
                return "applied"
            if ev["kind"] == "question_chosen" and any(p.get("chosen") == q for p in later):
                return "applied"
            return "queued"
        return "applied" if ev["seq"] in applied else "queued"

    return {"head": head if head is not None else (events[-1]["seq"] if events else 0), "epoch": epoch,
            "replay": replay, "run": run,
            "people": [{"name": p, "hue": HUES[i % len(HUES)]} for i, p in enumerate(people)],
            "nodes": list(nodes.values()), "clusters": out_clusters, "questions": questions,
            "notes": notes, "votes": [{"idea": i, "by": b, "value": v} for (b, i), v in votes.items()],
            "claims": list(claims or []),
            "mine": {"actions": [{"seq": e["seq"], "kind": e["kind"], "status": mine_status(e), "text": _short(e)}
                                 for e in mine[-MINE_KEPT:]]}}
