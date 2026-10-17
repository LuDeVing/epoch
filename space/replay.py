"""Replay a recorded log (docs/MULTIPLAYER_DESIGN.md section 5.4).

`--replay FILE --speed N [--seek SEQ]` loads an ndjson log (from --dump or from --rehearse) into the database:
events up to SEQ (original numbering) are written at once, the rest at the original gaps divided by N. The
replayed events keep their original by, by_kind, owner, data, round, stage and cause; they get new seq and ts.
The op of each event is its original op, or "replay-<original seq>" when it had none, so a second replay of the
same file into the same database adds zero rows. The file's space_opened is skipped (the database has its own).
When the new numbers differ from the old ones, cause, claim, base and control_applied refs are renumbered.
Standard library only.
"""
from __future__ import annotations

import datetime
import os
import threading
import time

from space.store import Reject, Store, read_ndjson, strip_private

SKIP_KINDS = frozenset({"space_opened"})


def _when(ts):
    try:
        return datetime.datetime.strptime(str(ts).rstrip("Z"), "%Y-%m-%dT%H:%M:%S.%f").timestamp()
    except ValueError:
        try:
            return datetime.datetime.strptime(str(ts).rstrip("Z"), "%Y-%m-%dT%H:%M:%S").timestamp()
        except ValueError:
            return None


def plan(events, seek: int = 0, speed: float = 1.0) -> list:
    """[(delay_s, event)] in file order: delay 0 up to seek, then the original gap divided by speed."""
    events = sorted(events, key=lambda e: e.get("seq") or 0)
    out, prev = [], None
    for ev in events:
        t = _when(ev.get("ts"))
        if (ev.get("seq") or 0) <= seek or prev is None or t is None or speed <= 0:
            delay = 0.0
        else:
            delay = max(0.0, (t - prev) / float(speed))
        if t is not None:
            prev = t
        out.append((delay, ev))
    return out


class Replayer:
    def __init__(self, store: Store, path, speed: float = 1.0, seek: int = 0):
        self.store, self.path = store, str(path)
        self.speed, self.seek = float(speed), int(seek or 0)
        self.events = read_ndjson(self.path)
        self.idmap: dict = {}
        self.written = 0
        self.done = threading.Event()
        self.stop_flag = threading.Event()
        self.thread = None

    def info(self) -> dict:
        return {"file": os.path.basename(self.path), "speed": self.speed, "seek": self.seek, "total": len(self.events)}

    def _map(self, v):
        return self.idmap.get(v, v) if isinstance(v, int) else v

    def write_one(self, ev: dict):
        """Write one recorded event; returns the new seq, or None when skipped."""
        if ev["kind"] in SKIP_KINDS:
            return None
        by, by_kind = ev.get("by") or "anon", ev.get("by_kind") or "human"
        op = ev.get("op") or "replay-%s" % ev.get("seq")
        old = ev.get("seq")
        with self.store.lock:
            dup = self.store.find_op(by, op)
            if dup is not None:
                if isinstance(old, int):
                    self.idmap[old] = dup
                return None
            data = strip_private(ev.get("data") or {})
            if ev["kind"] == "control_applied" and isinstance(data.get("refs"), list):
                data = dict(data, refs=[self._map(r) for r in data["refs"]])
            e = {"kind": ev["kind"], "subject": ev.get("subject"), "label": ev.get("label"), "op": op,
                 "base": self._map(ev.get("base")), "owner": ev.get("owner"), "data": data,
                 "round": ev.get("round"), "stage": ev.get("stage"), "claim": self._map(ev.get("claim")),
                 "cause": self._map(ev.get("cause"))}
            new = self.store.append(by, by_kind, e)
            if isinstance(old, int):
                self.idmap[old] = new["seq"]
            self.written += 1
            return new["seq"]

    def run(self, items=None) -> int:
        """Write the file (blocking), or the given planned items. Returns the number of rows written so far."""
        items = plan(self.events, self.seek, self.speed) if items is None else items
        due = time.perf_counter()                    # an absolute schedule: Windows waits tick in 15.6 ms steps,
        try:                                         # so many short gaps must not add up
            for delay, ev in items:
                due += delay
                left = due - time.perf_counter()
                if left > 0.002 and self.stop_flag.wait(left):
                    break
                if self.stop_flag.is_set():
                    break
                try:
                    self.write_one(ev)
                except Reject:                       # the store is closing
                    break
        finally:
            self.done.set()
        return self.written

    def start(self) -> "Replayer":
        """Write the events up to seek now, then the rest at their gaps in a daemon thread."""
        items = plan(self.events, self.seek, self.speed)
        k = 0
        while k < len(items) and (items[k][1].get("seq") or 0) <= self.seek:
            k += 1
        for _, ev in items[:k]:
            self.write_one(ev)
        self.thread = threading.Thread(target=self.run, args=(items[k:],), name="space-replay", daemon=True)
        self.thread.start()
        return self

    def stop(self) -> None:
        self.stop_flag.set()
