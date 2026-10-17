"""Presence: who is online and what each one is looking at (docs/MULTIPLAYER_DESIGN.md section 4.4 rule 11).

Memory only, no seq. A 5 s beat, a 20 s TTL, broadcast as the SSE `presence` message once per roster change.
The heartbeat also lists the claims its caller believes it holds; the claims module renews those and reports the
others as interrupts. Presence comes from heartbeats, never from the stream. Standard library only.
"""
from __future__ import annotations

import time

from space.contract import PRESENCE_TTL_S
from space.store import Store

FIELDS = ("view", "focus", "activity", "cursor")


class Presence:
    def __init__(self, store: Store, ttl: float = PRESENCE_TTL_S):
        self.store, self.ttl = store, float(ttl)
        self.roster: dict = {}          # client id -> entry
        self.ver = 0                    # bumped on every roster change; the stream sends presence when it moves

    def owner_of(self, by: str):
        """The owner a roster entry gives this actor, or None."""
        for r in self.roster.values():
            if r["by"] == by and r.get("owner"):
                return r["owner"]
        return None

    def beat(self, by: str, by_kind: str, p: dict) -> bool:
        """Apply one heartbeat. Returns True when the roster changed."""
        with self.store.lock:
            now, cid = time.monotonic(), str(p.get("client") or by)[:64]
            old = self.roster.get(cid, {})
            if p.get("bye"):
                changed = self.roster.pop(cid, None) is not None
            else:
                new = {"client": cid, "by": by, "kind": by_kind,
                       "name": str(p.get("name") or old.get("name") or by)[:40],
                       "owner": str(p.get("owner") or old.get("owner") or by.split(".")[0])[:40]}
                for f in FIELDS:
                    new[f] = p.get(f, old.get(f))
                new["seen"] = now
                changed = {k: v for k, v in new.items() if k != "seen"} != {k: v for k, v in old.items() if k != "seen"}
                self.roster[cid] = new
            if changed:
                self.ver += 1
        if changed:
            self.store.wake()
        return changed

    def prune(self) -> bool:
        with self.store.lock:
            now = time.monotonic()
            gone = [k for k, r in self.roster.items() if now - r["seen"] > self.ttl]
            for k in gone:
                del self.roster[k]
            if gone:
                self.ver += 1
        if gone:
            self.store.wake()
        return bool(gone)

    def as_list(self) -> list:
        now = time.monotonic()
        with self.store.lock:
            return [dict({k: v for k, v in r.items() if k != "seen"}, seen_ms_ago=int((now - r["seen"]) * 1000))
                    for r in self.roster.values() if now - r["seen"] <= self.ttl]
