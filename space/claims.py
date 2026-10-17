"""Claims on parts of the tree (docs/MULTIPLAYER_DESIGN.md sections 4.2 and 4.6).

Unit: node:<id>, covering the subtree. Server granted. TTL 90 s, renewed by the presence heartbeat that lists the
claims the caller believes it holds. Fencing token = the seq of the claim_granted (or claim_taken_over) event.
A reaper writes claim_expired. Only a person may take over (403 humans_only otherwise). At a restart every open
claim gets claim_expired with reason restart. The claim events are written by the actor "server".
Leases use time.monotonic(); clients get ttl_left_s, never an absolute time. Standard library only.
"""
from __future__ import annotations

import time

from space.contract import CLAIM_TTL_S
from space.store import Reject, Store, clean_id

ENFORCE_CLAIMS = True     # False = advisory for other agents: a claim conflict is accepted with data.warn
MAX_TTL_S = 3600.0


class Claims:
    def __init__(self, store: Store, ttl: float = CLAIM_TTL_S, enforce: bool | None = None):
        self.store, self.ttl = store, float(ttl)
        self.enforce = ENFORCE_CLAIMS if enforce is None else bool(enforce)
        self.live: dict = {}            # "node:<id>" -> {owner, token, exp, ttl}

    # ---- helpers
    def _label(self, subject: str):
        return self.store.index.names.get(subject[5:])

    def _server_write(self, kind: str, subject: str, data: dict, cause=None) -> dict:
        e = {"kind": kind, "subject": subject, "label": self._label(subject), "owner": "server", "data": data}
        if cause is not None:
            e["cause"] = cause
        return self.store.append("server", "system", e)

    def _alive(self, c, now) -> bool:
        return bool(c) and c["exp"] > now

    def holder(self, node, now=None):
        """The live claim on this node or an ancestor, nearest first: (subject, claim) or None."""
        now = time.monotonic() if now is None else now
        for n in self.store.index.chain(node):
            c = self.live.get("node:" + n)
            if self._alive(c, now):
                return "node:" + n, c
        return None

    def _conflict(self, node, by, now):
        """Another actor's live claim on this node, an ancestor or a descendant."""
        idx = self.store.index
        for s, c in self.live.items():
            if self._alive(c, now) and c["owner"] != by:
                other = s[5:]
                if other in idx.chain(node) or node in idx.chain(other):
                    return {"held_by": c["owner"], "subject": s, "ttl_left_s": round(c["exp"] - now, 1)}
        return None

    # ---- the guard for an agent that acts for nobody (contract.guard_applies)
    def guard(self, by: str, node, e: dict) -> None:
        now = time.monotonic()
        if self.store.index.is_closed(node):
            raise Reject(409, "subject_closed", subject="node:" + clean_id(node))
        h = self.holder(node, now)
        if h:
            _, c = h
            if c["owner"] != by:
                raise Reject(409, "claimed_by_other", held_by=c["owner"], ttl_left_s=round(c["exp"] - now, 1))
            if e.get("claim") != c["token"]:
                raise Reject(409, "claim_lost")
            return
        if e.get("claim") is not None:
            raise Reject(409, "claim_lost")

    def other_holder(self, node, by: str, owner: str):
        """For a delegate: the holder of a live claim over this node that is neither it nor its person."""
        h = self.holder(node)
        if not h:
            return None
        holder = h[1]["owner"]
        if holder == by or holder == owner or holder.split(".")[0] == owner:
            return None
        return holder

    # ---- POST /api/claims
    def handle(self, by: str, by_kind: str, action: str, subject, token=None, ttl=None, purpose=None, cause=None) -> dict:
        if not isinstance(subject, str) or not subject.startswith("node:") or not clean_id(subject[5:]):
            raise Reject(422, "bad_envelope", detail="subject must be node:<id>")
        subject = "node:" + clean_id(subject[5:])
        try:
            ttl = self.ttl if ttl is None else float(ttl)
        except (TypeError, ValueError):
            raise Reject(422, "bad_envelope", detail="ttl_s")
        if not 0 < ttl <= MAX_TTL_S:
            raise Reject(422, "bad_envelope", detail="ttl_s")
        with self.store.lock:
            now, c = time.monotonic(), self.live.get(subject)
            live = self._alive(c, now)
            if action == "acquire":
                if live and c["owner"] == by:
                    c["exp"], c["ttl"] = now + ttl, ttl
                    return {"token": c["token"], "ttl_s": ttl}
                other = self._conflict(subject[5:], by, now)
                if other:
                    raise Reject(409, "claimed_by_other", **other)
                data = {"owner": by, "ttl_s": ttl}
                if purpose:
                    data["purpose"] = str(purpose)[:160]
                ev = self._server_write("claim_granted", subject, data, cause)
                self.live[subject] = {"owner": by, "token": ev["seq"], "exp": now + ttl, "ttl": ttl}
                return {"token": ev["seq"], "ttl_s": ttl}
            if action == "takeover":
                if by_kind != "human":
                    raise Reject(403, "humans_only")
                ev = self._server_write("claim_taken_over", subject,
                                        {"from": c["owner"] if live else None, "to": by, "owner": by, "ttl_s": ttl}, cause)
                self.live[subject] = {"owner": by, "token": ev["seq"], "exp": now + ttl, "ttl": ttl}
                return {"token": ev["seq"], "ttl_s": ttl}
            if action not in ("renew", "release"):
                raise Reject(422, "bad_envelope", detail="action")
            if not (live and c["owner"] == by and c["token"] == token):
                raise Reject(409, "claim_lost")
            if action == "renew":
                c["exp"] = now + c["ttl"]
                return {"token": token, "ttl_s": c["ttl"]}
            del self.live[subject]
            self._server_write("claim_released", subject, {"owner": by, "reason": "done"}, cause)
            return {"ok": True}

    # ---- heartbeat renewal (POST /api/presence lists the claims the caller believes it holds)
    def renew_listed(self, by: str, listed) -> list:
        interrupts, now = [], time.monotonic()
        with self.store.lock:
            for item in listed or []:
                if not isinstance(item, dict) or not isinstance(item.get("subject"), str):
                    continue
                subj = item["subject"]
                if subj.startswith("node:"):
                    subj = "node:" + clean_id(subj[5:])
                c = self.live.get(subj)
                if self._alive(c, now) and c["owner"] == by and c["token"] == item.get("token"):
                    c["exp"] = now + c["ttl"]
                    if self.store.index.is_closed(subj[5:]):
                        interrupts.append({"type": "subject_closed", "subject": subj})
                else:
                    interrupts.append({"type": "claim_lost", "subject": subj})
        return interrupts

    # ---- reaper and restart
    def reap(self) -> int:
        n = 0
        with self.store.lock:
            now = time.monotonic()
            for s, c in list(self.live.items()):
                if c["exp"] <= now:
                    del self.live[s]
                    self._server_write("claim_expired", s, {"owner_was": c["owner"], "reason": "ttl"})
                    n += 1
        return n

    def expire_on_restart(self) -> int:
        """Claims do not survive a restart: close every claim still open in the log with reason restart."""
        last = {}
        with self.store.lock:
            for e in self.store.log:
                if e["kind"].startswith("claim_") and e.get("subject"):
                    last[e["subject"]] = e
            n = 0
            for s, e in last.items():
                if e["kind"] in ("claim_granted", "claim_taken_over"):
                    d = e.get("data") or {}
                    self._server_write("claim_expired", s, {"owner_was": d.get("owner") or d.get("to"), "reason": "restart"})
                    n += 1
        return n

    def as_list(self) -> list:
        now = time.monotonic()
        with self.store.lock:
            return [{"subject": s, "owner": c["owner"], "token": c["token"], "ttl_left_s": round(c["exp"] - now, 1)}
                    for s, c in self.live.items() if c["exp"] > now]
