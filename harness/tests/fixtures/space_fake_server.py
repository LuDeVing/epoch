"""A small fake of the shared-space server for the loop tests (docs/MULTIPLAYER_DESIGN.md section 16.3).

Standard library only: a ThreadingHTTPServer on 127.0.0.1 and a free port. It stores posted events with gap-free
seq numbers (deduped on (by, op)), stamps by, by_kind and owner from the headers, strips the private keys, refuses a
second node_added with a used id (409 id_taken), refuses a POST body over 64 KB (413 too_big, as the real
server does), checks each envelope with the real server's Space._envelope (422, kept in store.rejected),
and answers:
    GET  /api/events?since=N&limit=500   {"epoch", "head", "events"}
    GET  /api/control?loop=ID&since=N    {"head", **space.control.merge(...)}
    GET  /api/digest?agent=ID&role=R     {"text", "from_seq", "to_seq", "n"} from space.digest.render_digest
    POST /api/events                     one event, or {"events": [...]} (answers {"results": [...]})
    POST /api/claims, POST /api/presence minimal answers
It is a test double, not the real server (space/server.py): no SSE, no claims logic, no persistence.
"""
from __future__ import annotations

import json
import re
import threading
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import parse_qs, urlparse

PRIVATE = ("obvious", "obvious_match", "private")
MAX_BODY = 65536                    # the real server refuses a larger POST body with 413 too_big (space/server.py)


def _strip(x):
    if isinstance(x, dict):
        return {k: _strip(v) for k, v in x.items() if k not in PRIVATE}
    if isinstance(x, list):
        return [_strip(v) for v in x]
    return x


class Store:
    FIELDS = ("kind", "subject", "label", "data", "op", "base", "round", "stage", "claim", "cause")

    def __init__(self):
        self.events: list[dict] = []
        self.rejected: list[dict] = []                  # [{kind, by, body}]: envelopes the real server would refuse
        self.ops: dict = {}
        self.lock = threading.Lock()
        self.cond = threading.Condition(self.lock)
        self.posts = 0
        self.bodies: list[int] = []                     # the size of every POST body, in bytes

    def add(self, ev: dict, by: str, by_kind: str) -> tuple[int, dict]:
        with self.lock:
            self.posts += 1
            op = ev.get("op")
            if op and (by, op) in self.ops:
                return 200, {"seq": self.ops[(by, op)], "dup": True}
            if not isinstance(ev.get("data"), dict) or not ev.get("kind"):
                return 422, {"error": "bad_envelope"}
            from space.server import Space                 # the real envelope check: kinds, data keys, subject, stage, ints
            from space.store import Reject
            try:
                Space._envelope(None, ev)
            except Reject as r:
                self.rejected.append({"kind": ev.get("kind"), "by": by, "body": r.body})
                return r.code, r.body
            d = ev["data"]
            if ev["kind"] == "node_added":
                nid = re.sub(r"[^a-z0-9_]", "", str(d.get("id", "")).lower())[:16]
                if any(e["kind"] == "node_added" and e["data"].get("id") == nid for e in self.events):
                    return 409, {"error": "id_taken"}
                d = dict(d, id=nid)
            owner = "team" if by.startswith("team.") and by_kind == "system" else by.split(".")[0]
            rec = {k: ev.get(k) for k in self.FIELDS if k in ev}
            rec.update({"seq": len(self.events) + 1, "ts": time.strftime("%Y-%m-%dT%H:%M:%S.000Z", time.gmtime()),
                        "by": by, "by_kind": by_kind, "owner": owner, "data": _strip(d)})
            self.events.append(rec)
            if op:
                self.ops[(by, op)] = rec["seq"]
            self.cond.notify_all()
            return 200, {"seq": rec["seq"], "dup": False}

    def since(self, n: int, limit: int = 500) -> list[dict]:
        with self.lock:
            return [dict(e) for e in self.events[n:n + limit]]

    def snapshot(self) -> list[dict]:
        with self.lock:
            return [dict(e) for e in self.events]


class Handler(BaseHTTPRequestHandler):
    protocol_version = "HTTP/1.0"

    def log_message(self, *a):
        pass

    def _send(self, code, obj):
        b = json.dumps(obj).encode()
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(b)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(b)

    def do_GET(self):
        u = urlparse(self.path)
        q = {k: v[0] for k, v in parse_qs(u.query).items()}
        st: Store = self.server.store
        if u.path == "/api/events":
            evs = st.since(int(q.get("since", 0)), min(2000, int(q.get("limit", 500))))
            return self._send(200, {"epoch": "fake0001", "head": len(st.events), "events": evs})
        if u.path == "/api/control":
            from space import control
            evs = st.snapshot()
            res = control.merge(evs, loop=q.get("loop", "team.loop"), claims=[], since=int(q.get("since", 0)))
            return self._send(200, {"head": len(evs), **res})
        if u.path == "/api/digest":
            from space import digest
            evs = [e for e in st.snapshot() if e["seq"] > int(q.get("since", 0))][-60:]
            text = digest.render_digest(evs, q.get("agent", ""), q.get("role", "person"), q.get("scope"),
                                        int(q.get("cap", 1200)))
            return self._send(200, {"text": text, "from_seq": evs[0]["seq"] if evs else 0,
                                    "to_seq": evs[-1]["seq"] if evs else 0, "n": len(evs)})
        return self._send(404, {"error": "no_route"})

    def do_POST(self):
        n = int(self.headers.get("Content-Length") or 0)
        body = self.rfile.read(n) if n else b""            # the whole body first, then any answer
        self.server.store.bodies.append(n)
        if n > MAX_BODY:
            return self._send(413, {"error": "too_big"})
        try:
            obj = json.loads(body or b"{}")
        except ValueError:
            return self._send(422, {"error": "bad_envelope"})
        by = self.headers.get("X-Space-Actor") or "anon"
        by_kind = self.headers.get("X-Space-Kind") or "agent"
        st: Store = self.server.store
        if self.path.startswith("/api/events"):
            if isinstance(obj, dict) and isinstance(obj.get("events"), list):
                results = []
                for ev in obj["events"][:100]:
                    code, r = st.add(ev, by, by_kind)
                    results.append(r if code == 200 else dict(r, status=code))
                return self._send(200, {"results": results})
            code, r = st.add(obj, by, by_kind)
            return self._send(code, r)
        if self.path.startswith("/api/claims"):
            return self._send(200, {"token": len(st.events), "ttl_s": 90} if obj.get("action") != "release" else {"ok": True})
        if self.path.startswith("/api/presence"):
            return self._send(200, {"head": len(st.events), "claims_ok": True, "interrupts": []})
        return self._send(404, {"error": "no_route"})


class FakeSpace:
    """with FakeSpace() as fs: fs.url, fs.store, fs.post(kind, data, by="ana", by_kind="human", **fields)."""

    def __init__(self, port: int = 0):
        self.server = ThreadingHTTPServer(("127.0.0.1", port), Handler)
        self.server.daemon_threads = True
        self.server.store = Store()
        self.store = self.server.store
        self.port = self.server.server_address[1]
        self.url = f"http://127.0.0.1:{self.port}"
        self.thread = threading.Thread(target=self.server.serve_forever, kwargs={"poll_interval": 0.05}, daemon=True)

    def start(self):
        self.thread.start()
        return self

    def stop(self):
        self.server.shutdown()
        self.server.server_close()

    def __enter__(self):
        return self.start()

    def __exit__(self, *exc):
        self.stop()

    def post(self, kind, data, by="ana", by_kind="human", **fields) -> dict:
        """Post as a person (in process, no HTTP): the same store path the handler uses."""
        code, r = self.store.add({"kind": kind, "data": data, **fields}, by, by_kind)
        return dict(r, status=code)

    def events(self, kind: str | None = None) -> list[dict]:
        return [e for e in self.store.snapshot() if kind is None or e["kind"] == kind]
