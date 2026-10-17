"""The one writer of the shared research space (docs/MULTIPLAYER_DESIGN.md section 5).

python -m space.server --db D:/AGI-lab/spaces/<space>/space.db --port 8766 --web space/web
    [--memory-dir D:/AGI-lab/memory/_mock/binpack_nobase] [--lan] [--replay FILE --speed N --seek SEQ] [--dump FILE]

Standard library only. ThreadingHTTPServer, allow_reuse_address False (a second bind fails with WinError 10048),
request_queue_size 64, HTTP/1.0, Nagle off, Cache-Control no-store on every JSON answer, the whole POST body read
before any early reply, Content-Type application/json required on POST, 127.0.0.1 unless --lan (then 0.0.0.0 with
a random key required as X-Space-Key on POST and ?key= on the stream). The server never calls a model.

Routes (contract.ROUTES): GET / (static files), GET /api/events, GET /api/stream, POST /api/events,
POST /api/claims, POST /api/presence, GET /api/digest, GET /api/control, GET /api/snapshot, GET /api/memory.
"""
from __future__ import annotations

import argparse
import functools
import http.server
import json
import os
import re
import secrets
import sys
import threading
import time
import traceback
import urllib.parse
from pathlib import Path

from space import contract, control, digest, snapshot
from space.claims import Claims
from space.presence import Presence
from space.replay import Replayer
from space.store import Reject, Store, clean_id, read_db, strip_private, write_ndjson

CLIENT_FIELDS = ("kind", "data", "subject", "label", "op", "base", "round", "stage", "claim", "cause")
INT_FIELDS = ("base", "round", "claim", "cause")
SUBJECT_RE = re.compile(r"^(node|sketch|cluster|idea|obj|cand|question|fact|person|run|agent):.+$")
ACTOR_RE = re.compile(r"^[A-Za-z0-9_.\-]{1,64}$")
BY_KINDS = ("human", "agent", "system")
MAX_BODY = 65536
MAX_READ = 8 << 20
MAX_BATCH = 100
LABEL_CAP = 80
EVENTS_LIMIT, EVENTS_MAX, WAIT_MAX = 500, 2000, 25.0
DIGEST_LOOKBACK = 60
PING_S = 10.0
MEMORY_SECTIONS = ("FACTS", "TRIED", "PRIORS", "CUES", "OPEN QUESTIONS", "FAILED FRAMINGS")
MEMORY_ARCHIVE = "ARCHIVE"
_MEM_LINE = re.compile(r"^- \[(\w+)\] (\S+) \| (.*)$")
_MEM_RUN = re.compile(r"^(.*?)\s+r(\d+)$")
_MEM_USED = re.compile(r"^used (\d+)$")
MIME = {".html": "text/html; charset=utf-8", ".js": "text/javascript; charset=utf-8",
        ".mjs": "text/javascript; charset=utf-8", ".css": "text/css; charset=utf-8",
        ".json": "application/json", ".svg": "image/svg+xml", ".png": "image/png", ".ico": "image/x-icon",
        ".woff2": "font/woff2", ".woff": "font/woff", ".ttf": "font/ttf", ".txt": "text/plain; charset=utf-8",
        ".ndjson": "application/x-ndjson", ".map": "application/json"}


def _lab_root() -> str:
    return os.environ.get("HTSA_LAB_ROOT") or "D:/AGI-lab"


def _int(v, name):
    if v is None:
        return None
    if isinstance(v, bool) or not isinstance(v, int):
        raise Reject(422, "bad_envelope", detail=name)
    return v


# ---------------------------------------------------------------- memory files (GET /api/memory)
def parse_memory_line(line: str):
    """`- [id] date | run rN | source | text | evidence | used n` (TRIED rows carry extra fields inside text)."""
    m = _MEM_LINE.match(line)
    if not m:
        return None
    parts = m.group(3).split(" | ")
    if len(parts) < 3:
        return None
    run_field, source, rest = parts[0], parts[1], parts[2:]
    used = None
    if rest and _MEM_USED.match(rest[-1].strip()):
        used = int(_MEM_USED.match(rest[-1].strip()).group(1))
        rest = rest[:-1]
    rm = _MEM_RUN.match(run_field.strip())
    run, rnd = (rm.group(1), int(rm.group(2))) if rm else (run_field.strip(), None)
    text = " | ".join(rest[:-1]) if len(rest) > 1 else (rest[0] if rest else "")
    evidence = rest[-1] if len(rest) > 1 else ""
    return {"id": m.group(1), "date": m.group(2), "run": run, "round": rnd, "source": source.strip(),
            "text": text, "evidence": evidence, "used": used}


def parse_memory(text: str) -> dict:
    out = {"clock": 0, "sections": {s: [] for s in MEMORY_SECTIONS}, "archive": []}
    cur = None
    for line in text.splitlines():
        line = line.rstrip()
        if line.startswith("CLOCK:"):
            try:
                out["clock"] = int(line.split(":", 1)[1].strip())
            except ValueError:
                pass
        elif line.startswith("## "):
            name = line[3:].strip().upper()
            cur = name if name in out["sections"] or name == MEMORY_ARCHIVE else None
        elif cur and line.startswith("- "):
            e = parse_memory_line(line)
            if e:
                (out["archive"] if cur == MEMORY_ARCHIVE else out["sections"][cur]).append(e)
    return out


# ---------------------------------------------------------------- the space: log, claims, presence, rules
class Space:
    def __init__(self, db_path, space_id=None, memory_dir=None, claim_ttl=contract.CLAIM_TTL_S,
                 presence_ttl=contract.PRESENCE_TTL_S, enforce=None):
        self.store = Store(db_path, space_id)
        self.claims = Claims(self.store, claim_ttl, enforce)
        self.presence = Presence(self.store, presence_ttl)
        self.memory_dir = str(memory_dir) if memory_dir else None
        self.replay = None                       # {"file","speed","seek","total"} when the server runs --replay
        self.replayer = None
        self.restart_expired = self.claims.expire_on_restart()
        if not self.store.log:
            self.store.append("server", "system", {"kind": "space_opened", "owner": "server",
                                                   "data": {"space_id": self.store.space_id, "epoch": self.store.epoch}})

    # ---- shortcuts
    @property
    def epoch(self):
        return self.store.epoch

    @property
    def lock(self):
        return self.store.lock

    @property
    def cond(self):
        return self.store.cond

    @property
    def closing(self):
        return self.store.closing

    def head(self) -> int:
        return self.store.head

    def owner_of(self, by: str) -> str:
        """The person an actor works for: the roster entry's owner, else the part of by before the first dot."""
        return self.presence.owner_of(by) or by.split(".")[0]

    # ---- POST /api/events
    def _envelope(self, e) -> dict:
        if not isinstance(e, dict):
            raise Reject(422, "bad_envelope")
        kind = e.get("kind")
        if not isinstance(kind, str) or kind not in contract.KINDS or kind in contract.SERVER_ONLY:
            raise Reject(422, "unknown_kind", kind=kind if isinstance(kind, str) else None)
        e = {k: e[k] for k in CLIENT_FIELDS if k in e}            # unknown top-level fields are cut
        data = e.get("data", {})
        if data is None:
            data = {}
        if not isinstance(data, dict):
            raise Reject(422, "bad_envelope", detail="data")
        missing = [k for k in contract.KINDS[kind][1] if k not in data]
        if missing:
            raise Reject(422, "bad_envelope", detail="missing data keys", missing=missing)
        e["data"] = strip_private(data)
        s = e.get("subject")
        if s is not None and (not isinstance(s, str) or not SUBJECT_RE.match(s)):
            raise Reject(422, "bad_envelope", detail="subject")
        lab = e.get("label")
        if lab is not None:
            if not isinstance(lab, str):
                raise Reject(422, "bad_envelope", detail="label")
            e["label"] = lab[:LABEL_CAP]
        op = e.get("op")
        if op is not None and (not isinstance(op, str) or not 0 < len(op) <= 128):
            raise Reject(422, "bad_envelope", detail="op")
        st = e.get("stage")
        if st is not None and st not in contract.STAGES:
            raise Reject(422, "bad_envelope", detail="stage")
        for f in INT_FIELDS:
            _int(e.get(f), f)
        return e

    @staticmethod
    def _target_node(e):
        d = e["data"]
        if d.get("node") not in (None, ""):
            return clean_id(d["node"])
        s = e.get("subject") or ""
        if s.startswith("node:"):
            return clean_id(s[5:])
        if e["kind"] == "node_added" and d.get("parent") not in (None, ""):
            return clean_id(d["parent"])
        return None

    def post(self, by: str, by_kind: str, e) -> dict:
        e = self._envelope(e)
        with self.lock:
            dup = self.store.find_op(by, e.get("op"))
            if dup is not None:                                    # look the op up first
                return {"seq": dup, "dup": True}
            if self.closing:
                raise Reject(503, "closing")
            owner = self.owner_of(by)
            kind, d = e["kind"], e["data"]
            node = self._target_node(e)
            warn = None
            cls = contract.actor_class(by, by_kind, owner)
            if node and contract.guard_applies(by, by_kind, owner, kind):
                try:
                    self.claims.guard(by, node, e)
                except Reject as r:
                    if self.claims.enforce or r.body["error"] == "subject_closed":
                        raise
                    warn = r.body["error"]                         # advisory mode: accepted and flagged
            elif node and cls == "delegate" and self.claims.other_holder(node, by, owner):
                warn = "claimed_by_other"                          # a delegate is never blocked, only warned
            if kind == "node_added":                               # validate before the write
                nid = clean_id(d.get("id"))
                if not nid:
                    raise Reject(422, "bad_envelope", detail="node_added needs data.id")
                if nid in self.store.index.parent:
                    raise Reject(409, "id_taken", id=nid)
            over = []
            if kind in ("node_edited", "question_chosen"):         # last writer wins; tell whom it overwrote
                if kind == "node_edited":
                    slots = [(e.get("subject"), f) for f in (d.get("fields") or {})] if isinstance(d.get("fields"), dict) else []
                else:
                    slots = [("slot:next_question", "choose")]
                for key in slots:
                    le = self.store.index.last_edit.get(key)
                    if le and le[1] != by and le[0] > (e.get("base") or 0):
                        over.append({"field": key[1], "seq": le[0], "by": le[1]})
            if over or warn:
                d = dict(d)
                if over:
                    d["overwrote"] = over
                if warn:
                    d["warn"] = warn
            if e.get("label") is None:                             # name the part for the digest and the feed
                if kind == "node_added":
                    e["label"] = str(d.get("name") or d.get("id"))[:LABEL_CAP]
                elif node and node in self.store.index.names:
                    e["label"] = str(self.store.index.names[node])[:LABEL_CAP]
            ev = self.store.append(by, by_kind, dict(e, data=d, owner=owner))
            res = {"seq": ev["seq"], "dup": False}
            if over:
                res["overwrote"] = over
            if warn:
                res["warn"] = warn
            return res

    def post_batch(self, by: str, by_kind: str, items) -> dict:
        if not isinstance(items, list):
            raise Reject(422, "bad_envelope", detail="events")
        if len(items) > MAX_BATCH:
            raise Reject(422, "bad_envelope", detail="at most %d events per batch" % MAX_BATCH)
        res = []
        with self.lock:                                            # consecutive seqs for one batch
            for e in items:
                try:
                    res.append(self.post(by, by_kind, e))
                except Reject as r:
                    res.append(r.body)
        return {"results": res}

    # ---- reads
    def hello(self) -> dict:
        return {"space_id": self.store.space_id, "epoch": self.epoch, "head": self.head(),
                "server_time_ms": int(time.time() * 1000), "claims": self.claims.as_list(),
                "roster": self.presence.as_list(), "replay": self.replay}

    def digest(self, agent, role=None, scope=None, since=0, cap=contract.DIGEST_CAP, mode=None) -> dict:
        if since <= 0:
            since = max(0, self.head() - DIGEST_LOOKBACK)          # a new agent sees the last 60 events
        rows = self.store.since(since, EVENTS_MAX)
        if role:
            if role not in contract.ROLES:
                raise Reject(422, "bad_envelope", detail="role")
            ids = self.store.index.subtree(scope) if scope else None
            text = digest.render_digest(rows, agent, role, scope=ids, cap=cap,
                                        mode=mode or self.store.index.mode or "check_only") if rows else ""
        else:
            text = digest.make_digest(rows, agent, cap)[0] if rows else ""
        return {"text": text or "", "from_seq": since + 1, "to_seq": rows[-1]["seq"] if rows else since, "n": len(rows)}

    def control(self, loop="team.loop", since=0) -> dict:
        since = max(0, since)
        rows = self.store.events()          # the whole log: level keys are a state; since limits only the deltas
        claims = [{"subject": c["subject"], "owner": c["owner"]} for c in self.claims.as_list()]
        out = dict(control.merge(rows, loop=loop, claims=claims, since=since, file_ctl=None))
        out["head"] = rows[-1]["seq"] if rows else 0
        return out

    def snapshot(self, me=None) -> dict:
        return snapshot.build(self.store.events(), me=me, claims=self.claims.as_list(), epoch=self.epoch,
                              replay=self.replay, head=self.head())

    def memory(self, part) -> dict:
        if not self.memory_dir or not part:
            raise Reject(404, "no_memory")
        root = Path(self.memory_dir).resolve()
        p = (root / (re.sub(r"[^A-Za-z0-9_.-]", "_", str(part)) + ".md")).resolve()
        if p.parent != root or not p.is_file():
            raise Reject(404, "no_memory")
        out = parse_memory(p.read_text(encoding="utf-8", errors="replace"))
        return {"part": part, "path": str(p), **out}

    # ---- housekeeping
    def reap(self) -> None:
        if self.closing:
            return
        self.claims.reap()
        self.presence.prune()

    def start_replay(self, path, speed=1.0, seek=0) -> Replayer:
        self.replayer = Replayer(self.store, path, speed, seek)
        self.replay = self.replayer.info()
        self.replayer.start()
        return self.replayer

    def close(self) -> None:
        if self.replayer:
            self.replayer.stop()
        self.store.close()


# ---------------------------------------------------------------- HTTP
def sse_frame(ev: dict) -> bytes:
    return ("id: %d\ndata: %s\n\n" % (ev["seq"], json.dumps(ev, separators=(",", ":"), ensure_ascii=False))).encode("utf-8")


def sse_named(name: str, obj) -> bytes:
    return ("event: %s\ndata: %s\n\n" % (name, json.dumps(obj, separators=(",", ":"), ensure_ascii=False))).encode("utf-8")


class Handler(http.server.SimpleHTTPRequestHandler):           # static files come from directory=
    protocol_version = "HTTP/1.0"                              # no keep-alive traps; the stream sends Connection: close
    disable_nagle_algorithm = True
    extensions_map = dict(http.server.SimpleHTTPRequestHandler.extensions_map, **MIME)
    server: "SpaceServer"

    def log_message(self, *a):
        pass

    def list_directory(self, path):                           # never list a folder
        self.send_error(404, "not found")
        return None

    def _send(self, code: int, obj) -> None:
        b = json.dumps(obj, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(b)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(b)

    def _who(self, q):
        by = self.headers.get("X-Space-Actor") or q.get("me", ["anon"])[0]
        by_kind = self.headers.get("X-Space-Kind") or q.get("kind", ["human"])[0]
        if not ACTOR_RE.match(by or "") or by == "server":
            raise Reject(422, "bad_envelope", detail="actor")
        if by_kind not in BY_KINDS:
            raise Reject(422, "bad_envelope", detail="actor kind")
        return by, by_kind

    def _key(self, q):
        k = self.server.key
        if k and (self.headers.get("X-Space-Key") or q.get("key", [""])[0]) != k:
            raise Reject(403, "bad_key")

    def _read_body(self, n: int) -> bytes:
        """Read the whole body before any reply (a reply sent first resets the connection on Windows)."""
        keep, left = [], n
        while left > 0:
            chunk = self.rfile.read(min(left, 65536))
            if not chunk:
                break
            left -= len(chunk)
            if sum(len(c) for c in keep) <= MAX_BODY:
                keep.append(chunk)
        return b"".join(keep)

    def do_POST(self):
        u = urllib.parse.urlsplit(self.path)
        q = urllib.parse.parse_qs(u.query)
        sp = self.server.space
        try:
            try:
                n = int(self.headers.get("Content-Length") or 0)
            except ValueError:
                raise Reject(422, "bad_envelope", detail="content-length")
            if n > MAX_READ:
                self.close_connection = True
                raise Reject(413, "too_big")
            raw = self._read_body(n)
            self._key(q)
            if self.headers.get_content_type() != "application/json":
                raise Reject(415, "bad_content_type")
            if n > MAX_BODY:
                raise Reject(413, "too_big")
            if sp.closing:
                raise Reject(503, "closing")
            try:
                d = json.loads(raw.decode("utf-8") or "{}")
            except (ValueError, UnicodeDecodeError):
                raise Reject(422, "bad_envelope", detail="json")
            by, by_kind = self._who(q)
            if u.path == "/api/events":
                if isinstance(d, dict) and "events" in d and "kind" not in d:
                    return self._send(200, sp.post_batch(by, by_kind, d["events"]))
                return self._send(200, sp.post(by, by_kind, d))
            if u.path == "/api/claims":
                if not isinstance(d, dict):
                    raise Reject(422, "bad_envelope")
                return self._send(200, sp.claims.handle(by, by_kind, d.get("action", "acquire"), d.get("subject"),
                                                        d.get("token"), d.get("ttl_s"), d.get("purpose"), d.get("cause")))
            if u.path == "/api/presence":
                if not isinstance(d, dict):
                    raise Reject(422, "bad_envelope")
                sp.presence.beat(by, by_kind, d)
                interrupts = sp.claims.renew_listed(by, d.get("claims"))
                return self._send(200, {"head": sp.head(), "interrupts": interrupts,
                                        "claims_ok": not any(i["type"] == "claim_lost" for i in interrupts)})
            raise Reject(404, "no_route")
        except Reject as r:
            self._send(r.code, r.body)
        except OSError:
            raise
        except Exception:                                      # never let one request kill the handler silently
            traceback.print_exc()
            self._send(500, {"error": "server_error"})

    def do_GET(self):
        u = urllib.parse.urlsplit(self.path)
        q = urllib.parse.parse_qs(u.query)
        sp = self.server.space
        if not u.path.startswith("/api/"):
            return super().do_GET()
        try:
            self._key(q)
            one = lambda name, default=None: q.get(name, [default])[0]          # noqa: E731
            if u.path == "/api/events":                        # first load, catch-up, long-poll, agents
                since = max(0, int(one("since", "0")))
                wait = max(0.0, min(WAIT_MAX, float(one("wait", "0"))))
                lim = max(1, min(EVENTS_MAX, int(one("limit", str(EVENTS_LIMIT)))))
                end = time.monotonic() + wait
                while True:
                    rows = sp.store.since(since, lim)
                    if rows or time.monotonic() >= end or sp.closing:
                        break
                    with sp.cond:
                        if sp.head() <= since and not sp.closing:
                            sp.cond.wait(timeout=max(0.0, min(1.0, end - time.monotonic())))
                return self._send(200, {"epoch": sp.epoch, "head": sp.head(), "events": rows})
            if u.path == "/api/stream":
                return self._stream(q)
            if u.path == "/api/digest":
                cap = max(1, min(4 * contract.DIGEST_CAP, int(one("cap", str(contract.DIGEST_CAP)))))
                return self._send(200, sp.digest(one("agent") or self.headers.get("X-Space-Actor") or "anon",
                                                 one("role"), one("scope"), int(one("since", "0")), cap, one("mode")))
            if u.path == "/api/control":
                return self._send(200, sp.control(one("loop", "team.loop"), int(one("since", "0"))))
            if u.path == "/api/snapshot":
                return self._send(200, sp.snapshot(one("me")))
            if u.path == "/api/memory":
                return self._send(200, sp.memory(one("part")))
            raise Reject(404, "no_route")
        except Reject as r:
            self._send(r.code, r.body)
        except ValueError:
            self._send(422, {"error": "bad_envelope"})
        except OSError:
            raise
        except Exception:
            traceback.print_exc()
            self._send(500, {"error": "server_error"})

    def _stream(self, q):
        sp = self.server.space
        try:
            last = int(self.headers.get("Last-Event-ID") or q.get("since", ["0"])[0] or 0)     # the header wins
        except ValueError:
            raise Reject(422, "bad_envelope", detail="since")
        self.send_response(200)
        self.send_header("Content-Type", "text/event-stream; charset=utf-8")
        self.send_header("Cache-Control", "no-cache")
        self.send_header("Connection", "close")
        self.end_headers()
        self.close_connection = True
        w, rv, ping_s = self.wfile.write, -1, self.server.ping_s
        try:
            w(b"retry: 1000\n\n")
            if last > sp.head():
                w(sse_named("reset", {"reason": "since_ahead_of_head"}))
                return
            w(sse_named("hello", sp.hello()))
            while not sp.closing:
                rows = sp.store.since(last, EVENTS_LIMIT)
                if rows:
                    w(b"".join(sse_frame(r) for r in rows))    # one write per batch
                    last = rows[-1]["seq"]
                    continue
                if sp.presence.ver != rv:
                    rv = sp.presence.ver
                    w(sse_named("presence", {"clients": sp.presence.as_list(), "claims": sp.claims.as_list()}))
                    continue
                with sp.cond:                                  # check again under the lock, then wait
                    quiet = sp.head() <= last and sp.presence.ver == rv and not sp.closing
                    if quiet:
                        sp.cond.wait(timeout=ping_s)
                    quiet = quiet and sp.head() <= last and sp.presence.ver == rv and not sp.closing
                if quiet:
                    w(sse_named("ping", {"head": sp.head(), "claims": sp.claims.as_list()}))
        except OSError:
            pass                    # the client went away: ConnectionResetError, ConnectionAbortedError, BrokenPipeError


class SpaceServer(http.server.ThreadingHTTPServer):
    request_queue_size = 64
    allow_reuse_address = False      # on Windows the default (1) lets a second server share the port
    daemon_threads = True
    block_on_close = False

    def __init__(self, addr, space: Space, web_dir=".", key="", ping_s=PING_S):
        self.space, self.key, self.ping_s = space, key, float(ping_s)
        super().__init__(addr, functools.partial(Handler, directory=str(web_dir)))

    def handle_error(self, request, client_address):
        if not isinstance(sys.exc_info()[1], OSError):
            traceback.print_exc()


class Running:
    """A server serving in a background thread (tests, demo). stop() ends the streams, the port and the db."""

    def __init__(self, space: Space, httpd: SpaceServer, reap_s: float):
        self.space, self.httpd = space, httpd
        self.host, self.port = httpd.server_address[:2]
        self.url = "http://%s:%d" % ("127.0.0.1" if self.host == "0.0.0.0" else self.host, self.port)
        self._stop = threading.Event()
        self.reaper = threading.Thread(target=self._reap_loop, args=(reap_s,), name="space-reaper", daemon=True)
        self.thread = threading.Thread(target=httpd.serve_forever, kwargs={"poll_interval": 0.1},
                                       name="space-http", daemon=True)

    def _reap_loop(self, reap_s):
        while not self._stop.wait(reap_s):
            try:
                self.space.reap()
            except Exception:
                traceback.print_exc()

    def start(self) -> "Running":
        self.reaper.start()
        self.thread.start()
        return self

    def stop(self) -> None:
        if self._stop.is_set():
            return
        self._stop.set()
        self.space.store.closing = True
        self.space.store.wake()
        self.httpd.shutdown()
        self.httpd.server_close()
        self.space.close()


def make(db, port=contract.PORT, host=contract.HOST, web_dir=None, key="", memory_dir=None, space_id=None,
         replay=None, speed=1.0, seek=0, reap_s=contract.REAP_S, ping_s=PING_S, claim_ttl=contract.CLAIM_TTL_S,
         presence_ttl=contract.PRESENCE_TTL_S, enforce=None) -> Running:
    """Build the space and bind the port (raises OSError when the port is taken). Call .start() to serve."""
    web_dir = web_dir or str(Path(__file__).resolve().parent / "web")
    httpd = SpaceServer((host, port), None, web_dir, key, ping_s)      # bind first: a taken port changes nothing
    try:
        sp = Space(db, space_id=space_id, memory_dir=memory_dir, claim_ttl=claim_ttl, presence_ttl=presence_ttl,
                   enforce=enforce)
    except BaseException:
        httpd.server_close()
        raise
    httpd.space = sp
    if replay:
        sp.start_replay(replay, speed, seek)
    return Running(sp, httpd, reap_s)


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(prog="python -m space.server", description="HTSA shared space server")
    ap.add_argument("--db", default=os.path.join(_lab_root(), "spaces", "demo", "space.db"))
    ap.add_argument("--port", type=int, default=contract.PORT)
    ap.add_argument("--web", default=str(Path(__file__).resolve().parent / "web"))
    ap.add_argument("--memory-dir", default=None)
    ap.add_argument("--space-id", default=None)
    ap.add_argument("--lan", action="store_true", help="bind 0.0.0.0 and require the printed key")
    ap.add_argument("--replay", default=None, help="load a recorded ndjson log into the database")
    ap.add_argument("--speed", type=float, default=1.0)
    ap.add_argument("--seek", type=int, default=0)
    ap.add_argument("--dump", default=None, help="write the log of --db as ndjson to this file and exit")
    a = ap.parse_args(argv)
    if a.dump:
        if not os.path.exists(a.db):
            print("no database at %s" % a.db, file=sys.stderr)
            return 2
        rows = read_db(a.db)
        write_ndjson(a.dump, rows)
        print("dumped %d events to %s" % (len(rows), a.dump), flush=True)
        return 0
    key = secrets.token_urlsafe(6) if a.lan else ""
    host = "0.0.0.0" if a.lan else contract.HOST
    run = make(a.db, port=a.port, host=host, web_dir=a.web, key=key, memory_dir=a.memory_dir, space_id=a.space_id,
               replay=a.replay, speed=a.speed, seek=a.seek)
    sp = run.space
    print("space on http://%s:%d/  epoch %s  head %d" % (contract.HOST, run.port, sp.epoch, sp.head()), flush=True)
    if sp.restart_expired:
        print("restart: %d open claims expired" % sp.restart_expired, flush=True)
    if key:
        print("lan key: %s  (X-Space-Key on POST, ?key= on the stream)" % key, flush=True)
    if a.replay:
        print("replay of %s at speed %s from seq %d" % (a.replay, a.speed, a.seek), flush=True)
    run.reaper.start()
    try:
        run.httpd.serve_forever(poll_interval=0.25)        # in the main thread, so Ctrl+C stops it
    except KeyboardInterrupt:
        pass
    finally:
        run._stop.set()
        sp.store.closing = True
        sp.store.wake()
        run.httpd.server_close()
        sp.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
