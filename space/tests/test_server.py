"""P1 space-server checks (docs/MULTIPLAYER_DESIGN.md section 12.1 row P1).

Everything runs under tmp_path with in-process server threads on ports chosen by the OS, http.client for the
stream, no browser, no model call, no network beyond 127.0.0.1. Merge and digest are checked twice: once through a
fake (what the server passes in and returns), once through the real P0 functions (only fields the contract fixes).
"""
from __future__ import annotations

import ast
import http.client
import json
import random
import sqlite3
import sys
import threading
import time
from pathlib import Path

import pytest

from space import contract
from space import server as S
from space.store import Store, read_ndjson, write_ndjson

SPACE_DIR = Path(__file__).resolve().parents[1]

MEMORY_MD = """# Memory: choice
CLOCK: 15
## FACTS
- [m666c0c] 2026-10-17 | mock-gapA-1__nano__binpack_nobase__scaffold__r0 r1 | measured | candidate nbd68a153de ended with status checked on this part | nbd68a153de | used 15
## TRIED
- [mae4e79] 2026-10-17 | mock-gapA-1__nano__binpack_nobase__scaffold__r0 r1 | measured | the rule in nbd68a153de | 1.156774 | it passed the quick score | nbd68a153de | used 14
- [m702734] 2026-10-17 | mock-after-bugpass__nano__binpack_nobase__scaffold__r0 r2 | measured | the rule in n44a9d66bbb | 1.192903 | it failed the quick score | n44a9d66bbb | used 15
## PRIORS
- [m963cf1] 2026-10-17 | mock-gapA-1__nano__binpack_nobase__scaffold__r0 r1 | measured | simple greedy rules pass the quick score about 3 in 4 times here | nbd68a153de | used 15
## CUES
- [m141349] 2026-10-17 | mock-gapA-1__nano__binpack_nobase__scaffold__r0 r1 | measured | when a rule ties the reference -> try a different tie-break first | nbd68a153de | used 15
## OPEN QUESTIONS
- [m75c66e] 2026-10-17 | mock-gapA-1__nano__binpack_nobase__scaffold__r0 r1 | measured | does the gain hold on larger instances? | nbd68a153de | used 15
## FAILED FRAMINGS
## ARCHIVE
- [m0000aa] 2026-10-16 | old-run r3 | belief | (FACTS) an old belief nobody confirmed | used 2
"""


# ---------------------------------------------------------------- helpers
def call(port, method, path, body=None, actor="ana", kind="human", headers=None, raw=None,
         ctype="application/json", timeout=10.0):
    c = http.client.HTTPConnection("127.0.0.1", port, timeout=timeout)
    h = {"Content-Type": ctype} if method == "POST" else {}
    if actor:
        h["X-Space-Actor"] = actor
    if kind:
        h["X-Space-Kind"] = kind
    h.update(headers or {})
    data = raw if raw is not None else (json.dumps(body).encode() if body is not None else None)
    try:
        c.request(method, path, data, h)
        r = c.getresponse()
        b = r.read()
        try:
            return r.status, json.loads(b)
        except ValueError:
            return r.status, b
    finally:
        c.close()


def post(port, kind, data=None, actor="ana", by_kind="human", **env):
    return call(port, "POST", "/api/events", dict({"kind": kind, "data": data or {}}, **env), actor, by_kind)


def node(port, nid, parent, actor="team.loop", by_kind=None, **extra):
    by_kind = by_kind or ("system" if actor.startswith("team.") else "human")
    return post(port, "node_added", dict({"id": nid, "name": nid.replace("_", " "), "parent": parent,
                                          "origin": "map" if actor.startswith("team.") else "human"}, **extra),
                actor, by_kind)


def claim(port, action, subject, actor, by_kind="agent", **kw):
    return call(port, "POST", "/api/claims", dict({"action": action, "subject": subject}, **kw), actor, by_kind)


def events(port, since=0, limit=2000):
    st, b = call(port, "GET", "/api/events?since=%d&limit=%d" % (since, limit))
    assert st == 200
    return b["events"]


def wait_until(pred, timeout=10.0, step=0.02):
    end = time.monotonic() + timeout
    while time.monotonic() < end:
        if pred():
            return True
        time.sleep(step)
    return bool(pred())


class SSEReader(threading.Thread):
    """Reads /api/stream with http.client, reconnecting with Last-Event-ID like a browser."""

    def __init__(self, port_ref, since=0, drop_after=None, deadline=60.0):
        super().__init__(daemon=True)
        self.port_ref = port_ref                          # a list holding the current port (restart may move it)
        self.since, self.drop_after, self.deadline = since, drop_after, deadline
        self.seqs, self.named, self.target, self.stop_flag = [], {}, None, threading.Event()
        self.connects, self.dropped = 0, False
        self.ready = threading.Event()

    def done(self):
        return self.target is not None and self.seqs and self.seqs[-1] >= self.target

    def run(self):
        end = time.monotonic() + self.deadline
        last = self.since
        while time.monotonic() < end and not self.stop_flag.is_set() and not self.done():
            conn = http.client.HTTPConnection("127.0.0.1", self.port_ref[0], timeout=5)
            try:
                h = {"Last-Event-ID": str(last)} if self.connects else {}
                conn.request("GET", "/api/stream?since=%d" % last, headers=h)
                resp = conn.getresponse()
                self.connects += 1
                event, data = None, []
                while not self.stop_flag.is_set():
                    line = resp.readline()
                    if not line:
                        break
                    line = line.decode("utf-8").rstrip("\r\n")
                    if line == "":
                        if data:
                            obj = json.loads("\n".join(data))
                            if event in (None, "message"):
                                self.seqs.append(obj["seq"])
                                last = obj["seq"]
                            else:
                                self.named.setdefault(event, []).append(obj)
                                if event == "hello":
                                    self.ready.set()
                        event, data = None, []
                        if self.done():
                            break
                        if self.drop_after and not self.dropped and len(self.seqs) >= self.drop_after:
                            self.dropped = True                    # drop the connection mid-stream, resume after
                            break
                    elif line.startswith("event:"):
                        event = line[6:].strip()
                    elif line.startswith("data:"):
                        data.append(line[5:].lstrip())
            except (OSError, http.client.HTTPException):
                time.sleep(0.05)
            finally:
                conn.close()


@pytest.fixture
def mk(tmp_path):
    """Make and start servers; every one is stopped at the end."""
    running = []

    def _mk(db=None, **kw):
        kw.setdefault("port", 0)
        kw.setdefault("web_dir", str(tmp_path / "web"))
        kw.setdefault("reap_s", 0.1)
        kw.setdefault("ping_s", 0.3)
        r = S.make(db or str(tmp_path / "sp" / "space.db"), **kw).start()
        running.append(r)
        return r

    yield _mk
    for r in running:
        try:
            r.stop()
        except Exception:
            pass


# ---------------------------------------------------------------- the log: stress, resume, idempotency
def test_stress_four_writers_four_readers(mk, tmp_path):
    r = mk()
    port = [r.port]
    readers = [SSEReader(port), SSEReader(port, drop_after=100)]
    for t in readers:
        t.start()
    for t in readers:
        assert t.ready.wait(5)
    polled, paged, stop = [], [], threading.Event()

    def long_poll():
        last = 0
        while not stop.is_set():
            st, b = call(r.port, "GET", "/api/events?since=%d&wait=2" % last)
            for ev in b["events"]:
                polled.append(ev["seq"])
                last = ev["seq"]

    def pager():
        last = 0
        while not stop.is_set():
            st, b = call(r.port, "GET", "/api/events?since=%d&limit=37" % last)
            for ev in b["events"]:
                paged.append(ev["seq"])
                last = ev["seq"]
            time.sleep(0.01)

    bg = [threading.Thread(target=long_poll, daemon=True), threading.Thread(target=pager, daemon=True)]
    for t in bg:
        t.start()
    errors, retries = [], []

    def writer(i):
        rng, mine = random.Random(i), {}
        for n in range(80):
            op = "w%d-1700000000000-%d" % (i, n)
            st, b = post(r.port, "note_posted", {"text": "note %d from w%d" % (n, i)}, actor="w%d" % i, op=op)
            if st != 200 or b["dup"]:
                errors.append((st, b))
            mine[op] = b["seq"]
            if n % 5 == 4:                                 # 16 retries per writer, 64 in all
                old = rng.choice(sorted(mine))
                st, b2 = post(r.port, "note_posted", {"text": "retry"}, actor="w%d" % i, op=old)
                retries.append((b2.get("seq") == mine[old], b2.get("dup")))

    ws = [threading.Thread(target=writer, args=(i,)) for i in range(4)]
    for t in ws:
        t.start()
    for t in ws:
        t.join(60)
    assert not errors
    assert len(retries) == 64 and all(ok and dup for ok, dup in retries)
    head = r.space.head()
    assert head == 321                                     # space_opened plus 320 posted events
    for t in readers:
        t.target = head
    assert wait_until(lambda: all(t.done() for t in readers) and len(polled) >= head and len(paged) >= head, 30)
    stop.set()
    want = list(range(1, head + 1))
    assert readers[0].seqs == want
    assert readers[1].seqs == want and readers[1].dropped and readers[1].connects >= 2
    assert polled[:head] == want and paged[:head] == want
    con = sqlite3.connect(str(tmp_path / "sp" / "space.db"))
    try:
        assert con.execute("SELECT COUNT(*) FROM events WHERE by LIKE 'w%'").fetchone()[0] == 320
        assert con.execute("SELECT COUNT(DISTINCT by || op) FROM events WHERE op IS NOT NULL").fetchone()[0] == 320
    finally:
        con.close()


def test_since_ahead_of_head_gets_reset(mk):
    r = mk()
    c = http.client.HTTPConnection("127.0.0.1", r.port, timeout=5)
    c.request("GET", "/api/stream?since=999")
    body = c.getresponse().read().decode()
    c.close()
    assert body.startswith("retry: 1000") and "event: reset" in body and "since_ahead_of_head" in body


def test_repeated_op_returns_first_seq(mk):
    r = mk()
    st, a = post(r.port, "note_posted", {"text": "one"}, op="ana-1-1")
    st2, b = post(r.port, "note_posted", {"text": "two"}, op="ana-1-1")
    assert (st, a["dup"]) == (200, False) and (st2, b) == (200, {"seq": a["seq"], "dup": True})
    st3, c = post(r.port, "note_posted", {"text": "same op, other actor"}, actor="ben", op="ana-1-1")
    assert c["seq"] == a["seq"] + 1 and not c["dup"]


def test_envelope_rules(mk):
    r = mk()
    st, b = call(r.port, "POST", "/api/events", {"kind": "note_posted", "data": {"text": "x"}}, ctype="text/plain")
    assert (st, b["error"]) == (415, "bad_content_type")
    big = json.dumps({"kind": "note_posted", "data": {"text": "x" * 70000}}).encode()
    st, b = call(r.port, "POST", "/api/events", raw=big)
    assert (st, b["error"]) == (413, "too_big")
    st, b = post(r.port, "no_such_kind", {})
    assert (st, b["error"]) == (422, "unknown_kind")
    st, b = post(r.port, "claim_granted", {"owner": "ana", "ttl_s": 90})
    assert (st, b["error"]) == (422, "unknown_kind")
    st, b = post(r.port, "space_opened", {"space_id": "x", "epoch": "y"})
    assert (st, b["error"]) == (422, "unknown_kind")
    st, b = post(r.port, "note_posted", {})                  # a required data key is missing
    assert (st, b["error"]) == (422, "bad_envelope") and b["missing"] == ["text"]
    st, b = post(r.port, "note_posted", {"text": "x"}, stage="nowhere")
    assert (st, b["error"]) == (422, "bad_envelope")
    st, b = call(r.port, "POST", "/api/events", raw=b"{not json")
    assert (st, b["error"]) == (422, "bad_envelope")
    st, b = call(r.port, "GET", "/api/nothing")
    assert (st, b["error"]) == (404, "no_route")
    # the server owns seq, ts, by, by_kind and owner; unknown top-level fields are cut
    st, b = call(r.port, "POST", "/api/events", {"kind": "note_posted", "data": {"text": "hi"}, "by": "ben",
                                                 "by_kind": "system", "owner": "zed", "seq": 99, "evil": 1,
                                                 "cause": 1, "round": 1, "stage": "planned"}, actor="ana.agent",
                 kind="agent")
    ev = events(r.port)[-1]
    assert (ev["by"], ev["by_kind"], ev["owner"], ev["seq"]) == ("ana.agent", "agent", "ana", b["seq"])
    assert "evil" not in ev and ev["cause"] == 1 and ev["round"] == 1 and ev["stage"] == "planned"
    st, b = call(r.port, "POST", "/api/events", {"kind": "note_posted", "data": {"text": "x"}}, actor="server",
                 kind="system")
    assert (st, b["error"]) == (422, "bad_envelope")


def test_private_keys_stripped_at_depth(mk):
    r = mk()
    data = {"text": "ok", "private": {"secret": 1},
            "deep": {"obvious": "a", "keep": 1, "rows": [{"obvious_match": "b", "fine": 2}, {"x": {"private": 3}}]}}
    st, b = post(r.port, "note_posted", data)
    assert st == 200
    raw = json.dumps(events(r.port)[-1])
    for word in ("obvious", "obvious_match", "private", "secret"):
        assert word not in raw
    ev = events(r.port)[-1]
    assert ev["data"]["deep"] == {"keep": 1, "rows": [{"fine": 2}, {"x": {}}]}


def test_batch_gets_consecutive_seqs(mk):
    r = mk()
    st, b = call(r.port, "POST", "/api/events", {"events": [
        {"kind": "note_posted", "data": {"text": "a"}, "op": "b-1"},
        {"kind": "bogus", "data": {}},
        {"kind": "note_posted", "data": {"text": "c"}, "op": "b-2"},
        {"kind": "note_posted", "data": {"text": "a again"}, "op": "b-1"}]})
    res = b["results"]
    assert res[0]["seq"] + 1 == res[2]["seq"] and res[1]["error"] == "unknown_kind"
    assert res[3] == {"seq": res[0]["seq"], "dup": True}
    st, b = call(r.port, "POST", "/api/events", {"events": [{"kind": "note_posted", "data": {"text": "x"}}] * 101})
    assert (st, b["error"]) == (422, "bad_envelope")


# ---------------------------------------------------------------- rules: id_taken, last writer wins
def test_node_added_id_taken(mk):
    r = mk()
    assert node(r.port, "root", None)[0] == 200
    st, a = node(r.port, "item_order", "root", actor="ana")
    st2, b = node(r.port, "Item_Order", "root", actor="ben")
    assert st == 200 and (st2, b["error"], b["id"]) == (409, "id_taken", "item_order")
    st3, c = node(r.port, "item_order", "root", actor="team.loop", by_kind="system")
    assert (st3, c["error"]) == (409, "id_taken")
    assert events(r.port)[-1]["label"] == "item order"            # the label is filled from the name


def test_last_writer_wins_with_overwrote(mk):
    r = mk()
    st, a = post(r.port, "question_chosen", {"question": "q2"}, actor="ana", subject="question:q2")
    st, b = post(r.port, "question_chosen", {"question": "q3"}, actor="ben", subject="question:q3", base=a["seq"] - 1)
    assert b["overwrote"] == [{"field": "choose", "seq": a["seq"], "by": "ana"}]
    assert events(r.port)[-1]["data"]["overwrote"] == b["overwrote"]
    st, c = post(r.port, "question_chosen", {"question": "q2"}, actor="ana", subject="question:q2", base=b["seq"])
    assert "overwrote" not in c                                    # ana had seen ben's choice
    st, d = post(r.port, "question_chosen", {"question": "q4"}, actor="ana", subject="question:q4")
    assert "overwrote" not in d                                    # her own earlier choice does not count
    node(r.port, "choice", None)
    st, e1 = post(r.port, "node_edited", {"fields": {"name": "the choice"}}, actor="ana", subject="node:choice")
    st, e2 = post(r.port, "node_edited", {"fields": {"name": "choice rule", "priority": "low"}}, actor="ben",
                  subject="node:choice")
    assert e2["overwrote"] == [{"field": "name", "seq": e1["seq"], "by": "ana"}]


# ---------------------------------------------------------------- claims
def test_claim_race_one_winner(mk):
    r = mk()
    node(r.port, "choice", None)
    out, barrier = [], threading.Barrier(8)

    def racer(i):
        barrier.wait()
        out.append(claim(r.port, "acquire", "node:choice", "bot%d" % i))

    ts = [threading.Thread(target=racer, args=(i,)) for i in range(8)]
    for t in ts:
        t.start()
    for t in ts:
        t.join(10)
    wins = [b for st, b in out if st == 200]
    losses = [b for st, b in out if st == 409]
    assert len(wins) == 1 and len(losses) == 7
    assert all(b["error"] == "claimed_by_other" and b["ttl_left_s"] > 0 for b in losses)
    ev = [e for e in events(r.port) if e["kind"] == "claim_granted"]
    assert len(ev) == 1 and ev[0]["seq"] == wins[0]["token"] and ev[0]["by"] == "server"


def test_claim_expiry_fencing_and_takeover(mk):
    r = mk()
    node(r.port, "choice", None)
    node(r.port, "choice_a", "choice")
    st, a = claim(r.port, "acquire", "node:choice", "bot1", ttl_s=0.5, purpose="ideas for choice")
    assert st == 200 and a["ttl_s"] == 0.5
    assert wait_until(lambda: any(e["kind"] == "claim_expired" for e in events(r.port)), 5)
    exp = [e for e in events(r.port) if e["kind"] == "claim_expired"][-1]
    assert exp["data"] == {"owner_was": "bot1", "reason": "ttl"} and exp["subject"] == "node:choice"
    st, b = claim(r.port, "acquire", "node:choice", "bot2")
    assert st == 200 and b["token"] > a["token"]
    assert claim(r.port, "renew", "node:choice", "bot1", token=a["token"]) == (409, {"error": "claim_lost"})
    sk = {"node": "choice_a", "direction": "inward", "round": 1, "count": 1, "items": [{"id": "s1", "idea": "x"}]}
    st, c = post(r.port, "sketch_batch", sk, actor="bot1", by_kind="agent", claim=a["token"])
    assert (st, c["error"], c["held_by"]) == (409, "claimed_by_other", "bot2")
    st, c = post(r.port, "sketch_batch", sk, actor="bot2", by_kind="agent", claim=a["token"])
    assert (st, c["error"]) == (409, "claim_lost")                 # the holder with a stale token
    st, c = post(r.port, "sketch_batch", sk, actor="bot2", by_kind="agent", claim=b["token"])
    assert st == 200
    assert claim(r.port, "renew", "node:choice", "bot2", token=b["token"])[0] == 200
    st, t = claim(r.port, "takeover", "node:choice", "ana.agent")
    assert (st, t["error"]) == (403, "humans_only")
    st, t = claim(r.port, "takeover", "node:choice", "ana", by_kind="human")
    assert st == 200 and t["token"] > b["token"]
    ev = events(r.port)[-1]
    assert ev["kind"] == "claim_taken_over" and ev["data"]["from"] == "bot2" and ev["data"]["to"] == "ana"
    assert claim(r.port, "release", "node:choice", "bot2", token=b["token"])[0] == 409
    assert claim(r.port, "release", "node:choice", "ana", by_kind="human", token=t["token"]) == (200, {"ok": True})
    st, c = post(r.port, "sketch_batch", sk, actor="bot1", by_kind="agent", claim=a["token"])
    assert (st, c["error"]) == (409, "claim_lost")                 # no live claim, but a token was sent


def test_actor_classes_under_a_claim(mk):
    r = mk()
    node(r.port, "root", None)
    node(r.port, "choice", "root")
    node(r.port, "choice_a", "choice")
    st, cl = claim(r.port, "acquire", "node:choice", "ana.agent", purpose="ideas for choice")
    assert st == 200
    sk = {"node": "choice_a", "direction": "inward", "round": 1, "count": 1, "items": [{"id": "s1", "idea": "x"}]}
    st, b = post(r.port, "sketch_batch", sk, actor="bot9", by_kind="agent")             # other agent: refused
    assert (st, b["error"], b["held_by"]) == (409, "claimed_by_other", "ana.agent")
    st, b = node(r.port, "choice_b", "choice_a", actor="ben", by_kind="human")             # person: never blocked
    assert st == 200 and "warn" not in b
    st, b = post(r.port, "sketch_batch", sk, actor="team.loop", by_kind="system")       # team: never checked
    assert st == 200 and "warn" not in b
    rp = {"node": "choice_a", "idea": "c1", "objection": 1, "kind": "rebut", "text": "measured 0.91"}
    st, b = post(r.port, "reply_posted", rp, actor="ben.agent", by_kind="agent")         # delegate: warned
    assert st == 200 and b["warn"] == "claimed_by_other"
    assert events(r.port)[-1]["data"]["warn"] == "claimed_by_other"
    st, b = post(r.port, "reply_posted", rp, actor="ana.agent", by_kind="agent")         # its own claim: no warn
    assert st == 200 and "warn" not in b


def test_advisory_mode_accepts_with_warn(mk):
    r = mk(enforce=False)
    node(r.port, "choice", None)
    claim(r.port, "acquire", "node:choice", "bot1")
    sk = {"node": "choice", "direction": "inward", "round": 1, "count": 0, "items": []}
    st, b = post(r.port, "sketch_batch", sk, actor="bot2", by_kind="agent")
    assert st == 200 and b["warn"] == "claimed_by_other"


def test_skipped_node_closes_it_for_other_agents_only(mk):
    r = mk()
    node(r.port, "choice", None)
    node(r.port, "choice_a", "choice")
    assert post(r.port, "node_skipped", {"reason": "not now"}, actor="ana", subject="node:choice")[0] == 200
    tr = {"node": "choice_a", "cand": "n0123456789", "idea": "c1", "status": "win"}
    st, b = post(r.port, "test_result", tr, actor="bot9", by_kind="agent")
    assert (st, b["error"], b["subject"]) == (409, "subject_closed", "node:choice_a")
    assert post(r.port, "test_result", tr, actor="team.loop", by_kind="system")[0] == 200
    assert post(r.port, "node_unskipped", {}, actor="ana", subject="node:choice")[0] == 200
    assert post(r.port, "test_result", tr, actor="bot9", by_kind="agent")[0] == 200


# ---------------------------------------------------------------- presence
def test_presence_ttl_and_stream_message(mk):
    r = mk(presence_ttl=0.5)
    node(r.port, "choice", None)
    st, cl = claim(r.port, "acquire", "node:choice", "ana.agent")
    rd = SSEReader([r.port], deadline=10)
    rd.start()
    assert rd.ready.wait(5)
    beat = {"client": "c-7f3a", "name": "Ana's agent", "owner": "ana", "view": "clusters",
            "focus": {"type": "node", "id": "choice"}, "activity": {"state": "thinking", "text": "reading"},
            "cursor": 3, "claims": [{"subject": "node:choice", "token": cl["token"]},
                                    {"subject": "node:other", "token": 1}]}
    st, b = call(r.port, "POST", "/api/presence", beat, actor="ana.agent", kind="agent")
    assert st == 200 and b["head"] >= 3 and b["claims_ok"] is False
    assert b["interrupts"] == [{"type": "claim_lost", "subject": "node:other"}]

    def seen(pred):
        return any(pred(m) for m in rd.named.get("presence", []))

    assert wait_until(lambda: seen(lambda m: [c["client"] for c in m["clients"]] == ["c-7f3a"]
                                   and m["claims"] and m["claims"][0]["subject"] == "node:choice"), 5)
    m = [m for m in rd.named["presence"] if m["clients"]][-1]
    assert m["clients"][0]["owner"] == "ana" and m["clients"][0]["focus"] == {"type": "node", "id": "choice"}
    assert wait_until(lambda: seen(lambda m: m["clients"] == []) and
                      [m for m in rd.named["presence"]][-1]["clients"] == [], 5)      # dropped after the TTL
    assert rd.named.get("ping"), "an idle stream sends ping"
    rd.stop_flag.set()


# ---------------------------------------------------------------- digest, control, snapshot, memory
def _seed(port):
    node(port, "root", None)
    node(port, "choice", "root")
    node(port, "ties", "root")
    a = node(port, "item_order", "root", actor="ana")[1]["seq"]
    n = post(port, "note_posted", {"text": "check tie-breaking before the choice rule"}, actor="ben")[1]["seq"]
    s = post(port, "run_step", {"round": 1, "stage": "planned"}, actor="ben")[1]["seq"]
    return a, n, s


def test_digest_route_passes_role_scope_and_mode(mk, monkeypatch):
    r = mk()
    _seed(r.port)
    post(r.port, "stage_entered", {"round": 1, "stage": "planned", "waiting": True, "mode": "no_check"},
         actor="team.loop", by_kind="system")
    seen = {}

    def fake(events, me, role, scope=None, cap=1200, mode="check_only"):
        seen.update(n=len(events), me=me, role=role, scope=scope, cap=cap, mode=mode)
        return "FAKE"

    monkeypatch.setattr(S.digest, "render_digest", fake)
    st, b = call(r.port, "GET", "/api/digest?agent=ben.agent&role=critic&scope=root&since=2&cap=800")
    assert st == 200 and b["text"] == "FAKE" and b["from_seq"] == 3 and b["to_seq"] == r.space.head()
    assert b["n"] == r.space.head() - 2 and seen["n"] == b["n"]
    assert (seen["me"], seen["role"], seen["cap"], seen["mode"]) == ("ben.agent", "critic", 800, "no_check")
    assert set(seen["scope"]) == {"root", "choice", "ties", "item_order"}
    st, b = call(r.port, "GET", "/api/digest?agent=ben.agent&role=nobody")
    assert (st, b["error"]) == (422, "bad_envelope")


def test_digest_route_real_renderer(mk):
    r = mk()
    a, n, s = _seed(r.port)
    for role in ("person", "critic"):
        st, b = call(r.port, "GET", "/api/digest?agent=ana.agent&role=%s&since=0" % role)
        assert st == 200 and b["from_seq"] == 1 and b["to_seq"] == r.space.head()
        assert "[e%d]" % n in b["text"] and contract.CLOSING[role] in b["text"]
        assert len(b["text"]) <= contract.DIGEST_CAP
    st, b = call(r.port, "GET", "/api/digest?agent=ben&since=0")                 # no role: make_digest
    assert st == 200 and "[e%d]" % a in b["text"] and "[e%d]" % n not in b["text"]
    st, b = call(r.port, "GET", "/api/digest?agent=ben&role=person&since=%d" % r.space.head())
    assert b["text"] == "" and b["n"] == 0


def test_control_route_is_the_merge(mk, monkeypatch):
    r = mk()
    a, n, s = _seed(r.port)
    st, cl = claim(r.port, "acquire", "node:ties", "team.loop2")
    seen = {}

    def fake(events, *, loop="team.loop", claims=(), since=0, file_ctl=None):
        seen.update(seqs=[e["seq"] for e in events], loop=loop, claims=list(claims), since=since, file_ctl=file_ctl)
        return {"control": {"note": "x"}, "refs": [n], "steps": []}

    monkeypatch.setattr(S.control, "merge", fake)
    st, b = call(r.port, "GET", "/api/control?loop=team.loop&since=4")
    assert st == 200 and b["control"] == {"note": "x"} and b["head"] == r.space.head()
    assert seen["seqs"] == list(range(1, r.space.head() + 1)) and seen["since"] == 4 and seen["file_ctl"] is None
    assert seen["claims"] == [{"subject": "node:ties", "owner": "team.loop2"}] and seen["loop"] == "team.loop"
    monkeypatch.undo()
    st, b = call(r.port, "GET", "/api/control?loop=team.loop&since=0")             # the real merge
    assert st == 200 and b["head"] == r.space.head()
    assert {"control", "refs", "steps"} <= set(b)
    assert a in b["refs"] and n in b["refs"]
    assert [x["id"] for x in b["control"]["add_nodes"]] == ["item_order"]
    assert b["steps"] == [{"seq": s, "round": 1, "stage": "planned", "by": "ben"}]


def test_control_since_keeps_level_keys(mk):
    """The merge folds the whole log; since only limits refs, steps, disputes and seeds (section 6.2 rule 11)."""
    r = mk()
    a, n, s = _seed(r.port)
    post(r.port, "node_skipped", {}, actor="ben", subject="node:ties")
    post(r.port, "question_vetoed", {"question": "q1"}, actor="ana", subject="question:q1")
    post(r.port, "run_paused", {"reason": "look"}, actor="ana")
    cursor = r.space.head()
    late = post(r.port, "note_posted", {"text": "after the cursor"}, actor="ana")[1]["seq"]
    st, b = call(r.port, "GET", "/api/control?loop=team.loop&since=%d" % cursor)
    assert st == 200 and b["head"] == r.space.head()
    c = b["control"]
    assert c["skip_nodes"] == ["ties"] and c["veto"] == ["q1"] and c["pause"] is True
    assert [x["id"] for x in c["add_nodes"]] == ["item_order"]
    assert c["note"].startswith("ana: after the cursor") and "ben: check tie-breaking" in c["note"]
    assert b["refs"] == [late] and b["steps"] == []


def test_snapshot_counts(mk):
    r = mk()
    a, n, s = _seed(r.port)
    lp = lambda **k: dict(actor="team.loop", by_kind="system", **k)      # noqa: E731
    post(r.port, "stage_entered", {"round": 1, "stage": "planned", "waiting": True, "step_mode": True,
                                   "mode": "check_only"}, **lp())
    post(r.port, "control_applied", {"refs": [a, n], "round": 1, "stage": "planned"}, **lp())
    post(r.port, "cluster_snapshot", {"node": "choice", "direction": "inward", "round": 1, "stage": "clustered",
                                      "clusters": [{"cluster_id": "c1", "name": "best fit", "members": ["s1", "s2"],
                                                    "n": 2, "selected": True, "obvious": True},
                                                   {"cluster_id": "c2", "name": "worst fit", "members": ["s3"], "n": 1}]},
         **lp())
    post(r.port, "candidate_built", {"node": "choice", "cand": "n0123456789", "idea": "c1", "hypothesis": "h",
                                     "round": 1}, **lp())
    post(r.port, "test_result", {"node": "choice", "cand": "n0123456789", "idea": "c1", "status": "win"}, **lp())
    post(r.port, "vote_cast", {"idea": "v1", "value": 1}, actor="ana")
    post(r.port, "vote_cast", {"idea": "v1", "value": -1}, actor="ana")
    post(r.port, "vote_cast", {"idea": "v1", "value": 1}, actor="ben.agent", by_kind="agent")
    post(r.port, "question_vetoed", {"question": "q1"}, actor="ben", subject="question:q1")
    post(r.port, "question_chosen", {"question": "q2"}, actor="ana", subject="question:q2")
    post(r.port, "fact_disputed", {"node": "choice", "fact": "f", "reason": "r", "tag": "measured"}, actor="ana")
    post(r.port, "node_skipped", {}, actor="ben", subject="node:ties")
    post(r.port, "run_paused", {"reason": "look"}, actor="ana")
    claim(r.port, "acquire", "node:choice", "ana.agent")
    st, b = call(r.port, "GET", "/api/snapshot?me=ana")
    assert st == 200 and b["head"] == r.space.head() and b["epoch"] == r.space.epoch and b["replay"] is None
    assert b["run"] == {"round": 1, "stage": "planned", "waiting": True, "paused_by": ["ana"], "mode": "check_only",
                        "step_mode": True}
    assert b["people"] == [{"name": "ana", "hue": "a"}, {"name": "ben", "hue": "b"}]
    nodes = {x["id"]: x for x in b["nodes"]}
    assert len(nodes) == 4 and nodes["root"]["status"] == "map"
    assert nodes["item_order"]["status"] == "applied" and nodes["item_order"]["by"] == "ana"
    assert nodes["item_order"]["applied_at"]["round"] == 1 and nodes["item_order"]["applied_at"]["stage"] == "planned"
    assert nodes["ties"]["skipped_by"] == "ben" and nodes["choice"]["claim"]["holder"] == "ana.agent"
    assert nodes["choice"]["disputed"][0]["by"] == "ana"
    assert len(b["clusters"]) == 2 and {c["status"] for c in b["clusters"]} == {"win", "open"}
    assert "obvious" not in json.dumps(b)
    assert b["questions"]["vetoed"] == [{"question": "q1", "by": "ben"}]
    assert b["questions"]["chosen"]["question"] == "q2" and len(b["notes"]) == 1
    assert sorted((v["by"], v["value"]) for v in b["votes"]) == [("ana", -1), ("ben", 1)]
    assert len(b["claims"]) == 1 and len(b["mine"]["actions"]) == 3
    assert [x["kind"] for x in b["mine"]["actions"]] == ["question_chosen", "fact_disputed", "run_paused"]


def test_memory_route(mk, tmp_path):
    mem = tmp_path / "memory"
    mem.mkdir()
    (mem / "choice.md").write_text(MEMORY_MD, encoding="utf-8")
    r = mk(memory_dir=str(mem))
    st, b = call(r.port, "GET", "/api/memory?part=choice")
    assert st == 200 and b["part"] == "choice" and b["clock"] == 15 and b["path"].endswith("choice.md")
    assert list(b["sections"]) == ["FACTS", "TRIED", "PRIORS", "CUES", "OPEN QUESTIONS", "FAILED FRAMINGS"]
    assert [len(v) for v in b["sections"].values()] == [1, 2, 1, 1, 1, 0]
    f = b["sections"]["FACTS"][0]
    assert f == {"id": "m666c0c", "date": "2026-10-17", "run": "mock-gapA-1__nano__binpack_nobase__scaffold__r0",
                 "round": 1, "source": "measured", "text": "candidate nbd68a153de ended with status checked on this part",
                 "evidence": "nbd68a153de", "used": 15}
    t = b["sections"]["TRIED"][1]
    assert t["round"] == 2 and t["text"] == "the rule in n44a9d66bbb | 1.192903 | it failed the quick score"
    assert t["evidence"] == "n44a9d66bbb" and t["used"] == 15
    assert len(b["archive"]) == 1 and b["archive"][0]["text"].startswith("(FACTS)") and b["archive"][0]["evidence"] == ""
    (mem / "choice.md").write_text(MEMORY_MD.replace("CLOCK: 15", "CLOCK: 16"), encoding="utf-8")
    assert call(r.port, "GET", "/api/memory?part=choice")[1]["clock"] == 16          # re-read on every call
    for part in ("ties", "../choice", "..%2Fchoice", ""):
        st, b = call(r.port, "GET", "/api/memory?part=" + part)
        assert (st, b["error"]) == (404, "no_memory")


def test_memory_route_without_memory_dir(mk):
    r = mk()
    assert call(r.port, "GET", "/api/memory?part=choice") == (404, {"error": "no_memory"})


# ---------------------------------------------------------------- replay, restart, dump
def _record(tmp_path, n=300):
    """A 300-event ndjson log with 50 ms gaps, recorded through a real Space (no HTTP)."""
    sp = S.Space(str(tmp_path / "rec" / "space.db"))
    kinds = []
    sp.post("team.loop", "system", {"kind": "node_added", "data": {"id": "root", "name": "root", "parent": None,
                                                                   "origin": "map"}})
    i = 0
    while sp.head() < n:
        i += 1
        if i % 3 == 0:
            sp.post("ana", "human", {"kind": "note_posted", "data": {"text": "note %d" % i}, "op": "ana-1-%d" % i})
        elif i % 3 == 1:
            sp.post("team.loop", "system", {"kind": "sketch_batch", "subject": "node:root",
                                            "data": {"node": "root", "direction": "inward", "round": 1, "count": 1,
                                                     "items": [{"id": "s%d" % i, "idea": "x"}]}})
        else:
            sp.post("ben.agent", "agent", {"kind": "agent_said", "data": {"kind": "peer", "text": "line %d" % i},
                                           "cause": sp.head()})
    rows = sp.store.events()
    sp.close()
    base = time.time() - 100
    for k, ev in enumerate(rows):
        t = base + 0.05 * k
        ev["ts"] = time.strftime("%Y-%m-%dT%H:%M:%S", time.gmtime(t)) + ".%03dZ" % (int(t * 1000) % 1000)
    path = tmp_path / "rec.ndjson"
    write_ndjson(path, rows)
    return path, rows


def test_replay_speed_hello_and_idempotency(mk, tmp_path):
    path, rows = _record(tmp_path)
    assert len(rows) == 300
    db = str(tmp_path / "play" / "space.db")
    t0 = time.perf_counter()
    r = mk(db=db, replay=str(path), speed=100)
    assert wait_until(lambda: r.space.replayer.done.is_set(), 20)
    took = time.perf_counter() - t0
    assert 0.1 <= took < 3.0, took                                  # 299 gaps of 50 ms at speed 100 = 0.15 s
    got = r.space.store.events()
    assert [(e["kind"], e["subject"], e["by"]) for e in got] == [(e["kind"], e["subject"], e["by"]) for e in rows]
    assert [e["seq"] for e in got] == list(range(1, 301))
    keep = ("by", "by_kind", "owner", "data", "round", "stage", "cause")
    assert [{k: e.get(k) for k in keep} for e in got[1:]] == [{k: e.get(k) for k in keep} for e in rows[1:]]
    assert got[1]["ts"] != rows[1]["ts"]                            # new ts
    rd = SSEReader([r.port], deadline=5)
    rd.target = 300
    rd.start()
    assert rd.ready.wait(5)
    hello = rd.named["hello"][0]
    assert hello["replay"] == {"file": "rec.ndjson", "speed": 100.0, "seek": 0, "total": 300}
    rd.join(5)
    r.stop()
    sp = S.Space(db)                                                 # a second replay of the same file adds nothing
    try:
        rp = sp.start_replay(str(path), speed=1000)
        rp.thread.join(10)
        assert rp.written == 0 and sp.head() == 300
    finally:
        sp.close()


def test_replay_seek_loads_the_first_n_at_once(mk, tmp_path):
    path, rows = _record(tmp_path)
    r = mk(db=str(tmp_path / "seek" / "space.db"), replay=str(path), speed=0.001, seek=150)
    assert r.space.head() == 150                                     # written before the port serves
    time.sleep(0.3)
    assert r.space.head() == 150                                     # the rest waits for the original gaps
    st, b = call(r.port, "GET", "/api/snapshot")
    assert b["replay"]["seek"] == 150 and b["replay"]["total"] == 300


def test_replay_of_a_log_without_seq_writes_every_event(mk, tmp_path):
    path = tmp_path / "noseq.ndjson"
    rows = [{"kind": "note_posted", "by": "ana", "by_kind": "human", "owner": "ana", "data": {"text": "n%d" % i}}
            for i in range(5)]
    write_ndjson(path, rows)
    r = mk(db=str(tmp_path / "ns" / "space.db"), replay=str(path), speed=1000)
    assert wait_until(lambda: r.space.replayer.done.is_set(), 10)
    assert [e["data"]["text"] for e in r.space.store.events()[1:]] == ["n0", "n1", "n2", "n3", "n4"]


def test_dump_reads_a_path_with_hash_and_space(mk, tmp_path):
    db = str(tmp_path / "a b#c" / "space.db")
    r = mk(db=db)
    post(r.port, "note_posted", {"text": "x"})
    r.stop()
    out = tmp_path / "dump2.ndjson"
    assert S.main(["--db", db, "--dump", str(out)]) == 0
    assert [e["seq"] for e in read_ndjson(out)] == [1, 2]
    assert not (tmp_path / "a b").exists()                           # read only: no stray database is made


def test_restart_keeps_epoch_expires_claims_and_readers_stay_contiguous(mk, tmp_path):
    db = str(tmp_path / "rs" / "space.db")
    r1 = mk(db=db)
    port = [r1.port]
    node(r1.port, "root", None)
    node(r1.port, "choice", "root")
    for i in range(20):
        post(r1.port, "note_posted", {"text": "before %d" % i}, op="ana-1-%d" % i)
    st, cl = claim(r1.port, "acquire", "node:choice", "ana.agent", purpose="ideas for choice")
    claim(r1.port, "acquire", "node:root", "ben.agent")          # a conflict: refused, so one open claim only
    before = SSEReader(port, deadline=30)
    before.start()
    assert before.ready.wait(5)
    epoch = r1.space.epoch
    assert wait_until(lambda: before.seqs and before.seqs[-1] == r1.space.head(), 5)
    r1.stop()                                                        # the kill
    r2 = None
    end = time.monotonic() + 5
    while r2 is None:
        try:
            r2 = mk(db=db, port=port[0])
        except OSError:
            if time.monotonic() > end:
                r2 = mk(db=db)                                       # the port did not come back: move the readers
                port[0] = r2.port
            else:
                time.sleep(0.1)
    assert r2.space.epoch == epoch
    exp = [e for e in r2.space.store.events() if e["kind"] == "claim_expired"]
    assert [(e["subject"], e["data"]) for e in exp] == [("node:choice", {"owner_was": "ana.agent", "reason": "restart"})]
    after = SSEReader(port, deadline=30)
    after.start()
    for i in range(20):
        post(port[0], "note_posted", {"text": "after %d" % i}, op="ana-2-%d" % i)
    st, again = post(port[0], "note_posted", {"text": "retry"}, op="ana-1-3")
    assert again["dup"] is True                                      # ops survive the restart
    head = r2.space.head()
    before.target = after.target = head
    assert wait_until(lambda: before.done() and after.done(), 20)
    want = list(range(1, head + 1))
    assert before.seqs == want and after.seqs == want and before.connects >= 2
    assert after.named["hello"][0]["epoch"] == epoch
    assert not [e for e in r2.space.store.events() if e["kind"] == "space_opened" and e["seq"] > 1]


def test_second_bind_of_the_port_fails(mk, tmp_path):
    r = mk()
    with pytest.raises(OSError) as ei:
        S.make(str(tmp_path / "other" / "space.db"), port=r.port)
    if sys.platform == "win32":
        assert getattr(ei.value, "winerror", None) == 10048


def test_dump_writes_ndjson(mk, tmp_path):
    db = str(tmp_path / "d" / "space.db")
    r = mk(db=db)
    post(r.port, "note_posted", {"text": "x", "private": 1})
    out = tmp_path / "dump.ndjson"
    assert S.main(["--db", db, "--dump", str(out)]) == 0               # read only, while the server is live
    rows = read_ndjson(out)
    assert [e["seq"] for e in rows] == [1, 2] and rows[1]["data"] == {"text": "x"}
    assert r.space.head() == 2


# ---------------------------------------------------------------- static files, lan key, stdlib only
def test_static_files_and_traversal(mk, tmp_path):
    web = tmp_path / "web"
    web.mkdir()
    (web / "index.html").write_text("<!doctype html><title>space</title>", encoding="utf-8")
    (web / "app.mjs").write_text("export const x = 1;\n", encoding="utf-8")
    (tmp_path / "secret.txt").write_text("nope", encoding="utf-8")
    r = mk(web_dir=str(web))
    c = http.client.HTTPConnection("127.0.0.1", r.port, timeout=5)
    c.request("GET", "/")
    resp = c.getresponse()
    assert resp.status == 200 and b"<title>space</title>" in resp.read()
    c.close()
    c = http.client.HTTPConnection("127.0.0.1", r.port, timeout=5)
    c.request("GET", "/app.mjs")
    resp = c.getresponse()
    resp.read()
    assert resp.status == 200 and resp.getheader("Content-Type").startswith("text/javascript")
    c.close()
    for path in ("/../secret.txt", "/%2e%2e/secret.txt", "/..%5csecret.txt", "/sub/"):
        c = http.client.HTTPConnection("127.0.0.1", r.port, timeout=5)
        c.request("GET", path)
        resp = c.getresponse()
        assert resp.status in (301, 404) and b"nope" not in resp.read(), path
        c.close()


def test_lan_key_required(mk):
    r = mk(key="k3y")
    assert post(r.port, "note_posted", {"text": "x"})[1]["error"] == "bad_key"
    st, b = call(r.port, "POST", "/api/events", {"kind": "note_posted", "data": {"text": "x"}},
                 headers={"X-Space-Key": "k3y"})
    assert st == 200 and b["seq"] == 2
    assert call(r.port, "GET", "/api/events?since=0")[0] == 403
    assert call(r.port, "GET", "/api/events?since=0&key=k3y")[0] == 200


def test_routes_match_the_contract():
    text = (SPACE_DIR / "server.py").read_text(encoding="utf-8")
    for name, (method, path) in contract.ROUTES.items():
        assert '"%s"' % path in text or path == "/", name


def test_space_imports_only_the_standard_library():
    allowed = set(sys.stdlib_module_names) | {"space", "__future__"}
    bad = []
    for p in sorted(SPACE_DIR.rglob("*.py")):
        rel = p.relative_to(SPACE_DIR).parts
        if rel[0] in ("tests", "web"):
            continue
        tree = ast.parse(p.read_text(encoding="utf-8"))
        for n in ast.walk(tree):
            if isinstance(n, ast.Import):
                names = [a.name for a in n.names]
            elif isinstance(n, ast.ImportFrom) and not n.level:
                names = [n.module or ""]
            else:
                continue
            # The person-agent makes its one model call through harness.llm (design 16, P6).
            ok = allowed | ({"harness"} if rel == ("agent.py",) else set())
            bad += ["%s: %s" % ("/".join(rel), m) for m in names if m.split(".")[0] not in ok]
    assert not bad, bad


def test_store_reload_is_contiguous(tmp_path):
    db = tmp_path / "x" / "space.db"
    st = Store(db)
    for i in range(5):
        st.append("ana", "human", {"kind": "note_posted", "owner": "ana", "data": {"text": str(i)}, "op": "o%d" % i})
    epoch = st.epoch
    st.close()
    st2 = Store(db)
    try:
        assert st2.epoch == epoch and st2.head == 5 and st2.find_op("ana", "o3") == 4 and not st2.new_epoch
    finally:
        st2.close()
