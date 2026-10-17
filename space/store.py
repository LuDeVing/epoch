"""The event log of the shared space (docs/MULTIPLAYER_DESIGN.md sections 4.1, 4.4, 4.5).

SQLite in WAL mode on disk, mirrored in a Python list (index = seq - 1). The server is the only writer.
Handlers read the list, never the writer connection. Writes: look the (by, op) up first, then BEGIN IMMEDIATE
under one lock, insert, commit, append to the list, notify after the commit. Never ON CONFLICT DO NOTHING
(it burns a sequence number). A new epoch is made only for a new database. Standard library only.
"""
from __future__ import annotations

import datetime
import json
import os
import re
import secrets
import sqlite3
import threading
import urllib.parse

from space.contract import PRIVATE_KEYS

ROW_KEYS = ("seq", "ts", "by", "by_kind", "kind", "subject", "label", "base", "op")
BODY_KEYS = ("owner", "data", "round", "stage", "claim", "cause")


class Reject(Exception):
    """An error answer: HTTP code plus a JSON body {"error": ..., ...}."""

    def __init__(self, code: int, error: str, **extra):
        super().__init__(error)
        self.code, self.body = code, {"error": error, **extra}


def strip_private(x):
    """Remove PRIVATE_KEYS at any depth."""
    if isinstance(x, dict):
        return {k: strip_private(v) for k, v in x.items() if k not in PRIVATE_KEYS}
    if isinstance(x, list):
        return [strip_private(v) for v in x]
    return x


def clean_id(x) -> str:
    """Node ids are cleaned the way the loop cleans them: lower case, a-z0-9_, 16 characters."""
    return re.sub(r"[^a-z0-9_]", "", str(x).lower())[:16]


def now_ts() -> str:
    t = datetime.datetime.now(datetime.timezone.utc)
    return t.strftime("%Y-%m-%dT%H:%M:%S.") + "%03dZ" % (t.microsecond // 1000)


class Index:
    """What the server derives from the log to enforce its rules: the node tree, closed subjects, last edits."""

    def __init__(self):
        self.parent: dict = {}          # cleaned node id -> cleaned parent id
        self.names: dict = {}           # cleaned node id -> display name
        self.closed: set = set()        # "node:<id>" skipped and "question:<id>" vetoed
        self.last_edit: dict = {}       # (slot, field) -> (seq, by)
        self.mode = None                # the latest stage_entered.data.mode

    def fold(self, ev: dict) -> None:
        d, k = ev.get("data") or {}, ev["kind"]
        if k == "node_added" and d.get("id") is not None:
            nid = clean_id(d["id"])
            par = d.get("parent")
            self.parent[nid] = clean_id(par) if par not in (None, "") else None
            self.names[nid] = d.get("name") or nid
        elif k == "node_edited":
            for f in d.get("fields") or {}:
                self.last_edit[(ev.get("subject"), f)] = (ev["seq"], ev["by"])
            name = (d.get("fields") or {}).get("name")
            subj = ev.get("subject") or ""
            if name and subj.startswith("node:"):
                self.names[clean_id(subj[5:])] = name
        elif k == "question_chosen":
            self.last_edit[("slot:next_question", "choose")] = (ev["seq"], ev["by"])
        elif k in ("node_skipped", "question_vetoed") and ev.get("subject"):
            self.closed.add(self._norm(ev["subject"]))
        elif k in ("node_unskipped", "question_unvetoed") and ev.get("subject"):
            self.closed.discard(self._norm(ev["subject"]))
        elif k == "stage_entered" and d.get("mode"):
            self.mode = d["mode"]

    @staticmethod
    def _norm(subject: str) -> str:
        return "node:" + clean_id(subject[5:]) if subject.startswith("node:") else subject

    def chain(self, node) -> list:
        """The node and its ancestors, nearest first (cycle safe)."""
        out, node = [], clean_id(node) if node is not None else None
        while node is not None and node not in out:
            out.append(node)
            node = self.parent.get(node)
        return out

    def subtree(self, node) -> list:
        """The node and every node under it, in first-seen order."""
        root = clean_id(node)
        return [n for n in [root] + [n for n in self.parent if n != root] if root in self.chain(n)]

    def is_closed(self, node) -> bool:
        return any("node:" + n in self.closed for n in self.chain(node))


class Store:
    """The log. `lock` guards every write and every in-memory structure of the server; `cond` wakes readers."""

    def __init__(self, path, space_id: str | None = None):
        self.path = str(path)
        d = os.path.dirname(os.path.abspath(self.path))
        os.makedirs(d, exist_ok=True)
        self.space_id = space_id or os.path.basename(d) or "space"
        self.db = sqlite3.connect(self.path, isolation_level=None, check_same_thread=False, timeout=5.0)
        self.db.execute("PRAGMA journal_mode=WAL")
        self.db.execute("PRAGMA synchronous=NORMAL")
        self.db.execute("CREATE TABLE IF NOT EXISTS events(seq INTEGER PRIMARY KEY AUTOINCREMENT, ts TEXT NOT NULL, "
                        "by TEXT NOT NULL, by_kind TEXT NOT NULL, kind TEXT NOT NULL, subject TEXT, label TEXT, "
                        "base INTEGER, op TEXT, body TEXT NOT NULL, UNIQUE(by, op))")
        self.db.execute("CREATE TABLE IF NOT EXISTS meta(k TEXT PRIMARY KEY, v TEXT)")
        row = self.db.execute("SELECT v FROM meta WHERE k='epoch'").fetchone()
        self.new_epoch = row is None
        if row is None:
            self.epoch = secrets.token_hex(4)
            self.db.execute("INSERT INTO meta VALUES('epoch', ?)", (self.epoch,))
        else:
            self.epoch = row[0]
        self.db.execute("PRAGMA wal_checkpoint(TRUNCATE)")
        self.lock = threading.RLock()
        self.cond = threading.Condition()
        self.closing = False
        self.log: list = []
        self.ops: dict = {}
        self.index = Index()
        for r in self.db.execute("SELECT seq,ts,by,by_kind,kind,subject,label,base,op,body FROM events ORDER BY seq"):
            ev = row_to_event(r)
            if ev["seq"] != len(self.log) + 1:
                raise RuntimeError("log is not contiguous at seq %d" % ev["seq"])
            self.index.fold(ev)
            self.log.append(ev)
            if ev["op"]:
                self.ops[(ev["by"], ev["op"])] = ev["seq"]

    # ---- reads (the in-memory list only)
    @property
    def head(self) -> int:
        return len(self.log)

    def since(self, n: int, limit: int = 500) -> list:
        n = max(0, int(n))
        with self.lock:
            return self.log[n:n + max(0, int(limit))]

    def events(self) -> list:
        with self.lock:
            return list(self.log)

    def find_op(self, by: str, op) -> int | None:
        return self.ops.get((by, op)) if op else None

    # ---- the one write path
    def append(self, by: str, by_kind: str, e: dict) -> dict:
        """Write one event. `e` holds kind and any of subject, label, base, op and the BODY_KEYS."""
        with self.lock:
            if self.closing:
                raise Reject(503, "closing")
            ts = now_ts()
            body = {k: e[k] for k in BODY_KEYS if e.get(k) is not None}
            body.setdefault("data", {})
            self.db.execute("BEGIN IMMEDIATE")
            try:
                cur = self.db.execute(
                    "INSERT INTO events(ts,by,by_kind,kind,subject,label,base,op,body) VALUES(?,?,?,?,?,?,?,?,?)",
                    (ts, by, by_kind, e["kind"], e.get("subject"), e.get("label"), e.get("base"), e.get("op"),
                     json.dumps(body, separators=(",", ":"), ensure_ascii=False)))
                seq = cur.lastrowid
                self.db.execute("COMMIT")
            except BaseException:
                self.db.execute("ROLLBACK")
                raise
            if seq != len(self.log) + 1:
                raise RuntimeError("seq %d does not follow head %d" % (seq, len(self.log)))
            ev = {"seq": seq, "ts": ts, "by": by, "by_kind": by_kind, "kind": e["kind"], "subject": e.get("subject"),
                  "label": e.get("label"), "base": e.get("base"), "op": e.get("op"), **body}
            self.index.fold(ev)
            self.log.append(ev)
            if e.get("op"):
                self.ops[(by, e["op"])] = seq
        self.wake()                                   # notify only after the commit
        return ev

    def wake(self) -> None:
        with self.cond:
            self.cond.notify_all()

    # ---- dump and close
    def dump(self, path) -> int:
        """Write the log as ndjson (one event per line, in seq order). Returns the number of lines."""
        rows = self.events()
        write_ndjson(path, rows)
        return len(rows)

    def close(self) -> None:
        with self.lock:
            self.closing = True
            try:
                self.db.close()
            except sqlite3.Error:
                pass
        self.wake()


def row_to_event(r) -> dict:
    ev = dict(zip(ROW_KEYS, r[:9]))
    ev.update(json.loads(r[9]))
    ev.setdefault("data", {})
    return ev


def read_db(path) -> list:
    """Read a space database without writing to it (for --dump while a server may be live)."""
    uri = "file:%s?mode=ro" % urllib.parse.quote(os.path.abspath(str(path)).replace("\\", "/"), safe="/:")
    con = sqlite3.connect(uri, uri=True)
    try:
        return [row_to_event(r) for r in
                con.execute("SELECT seq,ts,by,by_kind,kind,subject,label,base,op,body FROM events ORDER BY seq")]
    finally:
        con.close()


def write_ndjson(path, rows) -> None:
    d = os.path.dirname(os.path.abspath(str(path)))
    os.makedirs(d, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        for ev in rows:
            f.write(json.dumps(ev, separators=(",", ":"), ensure_ascii=False) + "\n")


def read_ndjson(path) -> list:
    """Read an ndjson log; a blank or torn line is skipped."""
    out = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                ev = json.loads(line)
            except ValueError:
                continue
            if isinstance(ev, dict) and ev.get("kind"):
                out.append(ev)
    return out
