"""The bridge: a run folder of a loop that runs WITHOUT --space, mirrored into the shared space, and the space's
human events rendered back into that folder's control.json (docs/MULTIPLAYER_DESIGN.md sections 8 and 16.4).

    python -m space.bridge --run <dir> --space http://127.0.0.1:8766 --every 0.5
    python -m space.bridge --import <dir> --space http://127.0.0.1:8766 --pace original|fast --speed N

Push: the run files are tailed into the event kinds of section 6.9, posted as team.bridge (by_kind system),
100 events per POST, with 3 s timeouts and an outbox file when the server does not answer. JSONL files are read
by byte offset (a line that is not whole yet waits for the next pass), whole-file JSON by content hash (a cut
file is retried at the next pass). Cursors persist in <dir>/space_bridge_cursor.json.

Pull: control.json is rendered from GET /api/control (or from space.control.merge over the log when the server
has no such route) with space.control.render_control_json; the file's own run keys (contract.FILE_ONLY_KEYS)
are kept. Each new control_log.jsonl row gives exactly one control_applied naming the queued human events that
the row's control state contains.

Import: a finished run folder is replayed in the order of the timestamps found in its files (a row with no
timestamp takes its round's first known time, else the file's mtime), each event carrying data.orig_ts, posted at
the original gaps divided by --speed (or at once with --pace fast). A folder still being written is then tailed.

Never mirrored: state.json spend or decisions, private/, calls/, prompts/, obvious, obvious_match.
Standard library only. The bridge never calls a model."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime
from pathlib import Path

from space import contract as C

ACTOR, ACTOR_KIND = "team.bridge", "system"
CURSOR_FILE, OUTBOX_FILE, MODE_FILE = "space_bridge_cursor.json", "space_bridge_outbox.ndjson", "space_mode.json"
POST_BATCH, SKETCH_BATCH = 100, 50
METRIC_KEYS = ("learn_gap", "learn_z", "long_z", "extrap_z", "cost_ratio")
NEVER_KEYS = frozenset(C.PRIVATE_KEYS | {"spent", "spent_aux", "spent_by_stage", "decisions"})
# human kinds the bridge can carry through control.json (their control key is one the loop reads)
QUEUE_KINDS = frozenset(k for k, v in C.KINDS.items() if v[2] in C.CONTROL_KEYS and "person" in v[0].split())
KEEP_KINDS = QUEUE_KINDS | {"control_applied", "claim_granted", "claim_released", "claim_expired", "claim_taken_over",
                            "fact_disputed", "seed_added", "run_step"}
# sort rank inside one timestamp when importing (the order the loop produces things within a round)
RANK = {"control_applied": 0, "node_added": 0, "question_picked": 1, "sketch_batch": 1, "cluster_snapshot": 2,
        "objection_raised": 3, "reply_posted": 3, "objection_marked": 3, "candidate_built": 4, "test_result": 5,
        "memory_added": 6, "node_edited": 7, "stage_entered": 8}


# ---------------------------------------------------------------- small helpers

def _clean_id(i) -> str:
    return re.sub(r"[^a-z0-9_]", "", str(i or "").lower())[:16]


def _strip(obj):
    """Drop the never-mirrored keys at any depth."""
    if isinstance(obj, dict):
        return {k: _strip(v) for k, v in obj.items() if k not in NEVER_KEYS}
    if isinstance(obj, list):
        return [_strip(v) for v in obj]
    return obj


def _sha(b: bytes) -> str:
    return hashlib.sha1(b).hexdigest()[:16]


def _ts(s) -> float | None:
    """A loop timestamp ('2026-10-17T19:33:18', local, naive) or epoch seconds, as epoch seconds."""
    if isinstance(s, (int, float)) and not isinstance(s, bool):
        return float(s)
    if not isinstance(s, str) or not s:
        return None
    try:
        dt = datetime.fromisoformat(s.replace("Z", "+00:00"))
    except ValueError:
        return None
    return dt.timestamp()


def _iso(t: float) -> str:
    dt = datetime.fromtimestamp(t)
    ms = int((t % 1) * 1000)
    return dt.strftime("%Y-%m-%dT%H:%M:%S") + (".%03d" % ms if ms else "")


def _node_of(cluster_id: str) -> str:
    """'choice-in-k03' -> 'choice' (node ids hold no hyphen: they are cleaned to a-z0-9_)."""
    m = re.match(r"^(.*)-(in|ou)-k\d+$", str(cluster_id or ""))
    return m.group(1) if m else ""


def _cut(s, n) -> str:
    s = re.sub(r"\s+", " ", str(s or "")).strip()
    return s if len(s) <= n else s[: n - 3] + "..."


def _write_atomic(path: Path, text: str, give_up_s: float = 3.0) -> None:
    tmp = path.with_name(path.name + ".tmp")
    tmp.write_text(text, encoding="utf-8")
    t0 = time.monotonic()
    while True:
        try:
            os.replace(tmp, path)
            return
        except PermissionError:                      # a reader holds the target open on Windows
            if time.monotonic() - t0 > give_up_s:
                raise
            time.sleep(0.05)


# ---------------------------------------------------------------- the HTTP client

class Client:
    """POST and GET to the space with 3 s timeouts. A failed call marks the server down for the rest of the
    pass, so a closed port costs one timeout per pass; events that could not be sent wait in the outbox."""

    def __init__(self, base: str, outbox: Path, timeout: float = 3.0, key: str = ""):
        self.base, self.outbox, self.timeout, self.key = base.rstrip("/"), outbox, timeout, key
        self.down = False
        self.posted = self.errors = 0
        self._open = urllib.request.build_opener(urllib.request.ProxyHandler({})).open   # never a proxy

    def call(self, method: str, path: str, body=None):
        """(status, json). Raises OSError or ValueError when the server cannot be reached or answers junk."""
        if self.down:
            raise OSError("space marked down for this pass")
        h = {"Content-Type": "application/json", "X-Space-Actor": ACTOR, "X-Space-Kind": ACTOR_KIND}
        if self.key:
            h["X-Space-Key"] = self.key
        data = None if body is None else json.dumps(body).encode("utf-8")
        req = urllib.request.Request(self.base + path, method=method, data=data, headers=h)
        try:
            try:
                with self._open(req, timeout=self.timeout) as r:
                    return r.status, json.loads(r.read() or b"{}")
            except urllib.error.HTTPError as e:      # 4xx and 5xx come back as data
                try:
                    return e.code, json.loads(e.read() or b"{}")
                except ValueError:
                    return e.code, {}
        except (OSError, ValueError):
            self.down = True
            raise

    def post(self, events: list[dict]) -> None:
        for i in range(0, len(events), POST_BATCH):
            chunk = events[i:i + POST_BATCH]
            try:
                st, d = self.call("POST", C.ROUTES["post"][1], {"events": chunk})
            except (OSError, ValueError):
                st, d = 0, {}
            if st == 0 or st >= 500:
                self._to_outbox(chunk)
                continue
            if st != 200:
                self.errors += len(chunk)
                print(f"[bridge] batch refused {st}: {str(d)[:160]}", file=sys.stderr, flush=True)
                continue
            res = d.get("results") or []
            self.posted += len(chunk)
            self.errors += sum(1 for r in res if isinstance(r, dict) and r.get("error") and r.get("error") != "id_taken")

    def _to_outbox(self, events: list[dict]) -> None:
        with open(self.outbox, "a", encoding="utf-8") as f:
            f.write("".join(json.dumps(e) + "\n" for e in events))

    def flush_outbox(self) -> int:
        """Send what waited; safe to repeat (the server dedupes on (by, op))."""
        try:
            lines = [ln for ln in self.outbox.read_text(encoding="utf-8").splitlines() if ln.strip()]
        except OSError:
            return 0
        if not lines:
            return 0
        evs = []
        for ln in lines:
            try:
                evs.append(json.loads(ln))
            except ValueError:
                pass
        sent, left = 0, []
        for i in range(0, len(evs), POST_BATCH):
            chunk = evs[i:i + POST_BATCH]
            try:
                st, _ = self.call("POST", C.ROUTES["post"][1], {"events": chunk})
            except (OSError, ValueError):
                st = 0
            if st == 0 or st >= 500:
                left += chunk
            else:
                sent += len(chunk)
        _write_atomic(self.outbox, "".join(json.dumps(e) + "\n" for e in left))
        return sent


# ---------------------------------------------------------------- the bridge

def _new_cursor() -> dict:
    return {"v": 1, "off": {}, "tail": {}, "hash": {}, "tree": {}, "cg": {}, "dr": {}, "cands": {}, "tr": {},
            "ref_n": 0, "stage": None}


class Bridge:
    def __init__(self, run_dir, space: str = C.BASE_URL, *, cursor_path=None, outbox_path=None, control_path=None,
                 pull: bool = True, presence: bool = True, mode: str | None = None, timeout: float = 3.0,
                 key: str = "", fresh: bool = False, persist: bool = True, timed: bool = False):
        self.rd = Path(run_dir)
        self.cursor_path = Path(cursor_path) if cursor_path else self.rd / CURSOR_FILE
        self.control_path = Path(control_path) if control_path else self.rd / "control.json"
        self.client = Client(space, Path(outbox_path) if outbox_path else self.rd / OUTBOX_FILE, timeout, key)
        self.pull, self.presence, self.mode_arg, self.persist, self.timed = pull, presence, mode, persist, timed
        self.tag = _sha(self.rd.resolve().name.encode())[:6]    # ops are per run folder, so two bridges never clash
        self.cur = _new_cursor()
        if not fresh:
            try:
                c = json.loads(self.cursor_path.read_text(encoding="utf-8"))
                if isinstance(c, dict) and c.get("v") == 1:
                    self.cur.update(c)
            except (OSError, ValueError):
                pass
        # server side (memory only: re-read from seq 0 at every start)
        self.ev_cursor, self.epoch = 0, None
        self.human: dict[int, dict] = {}         # seq -> human event that control.json can carry
        self.kept: list[dict] = []               # events for the local merge fallback
        self.applied: set[int] = set()           # seqs some control_applied already named
        self.last_beat = 0.0
        self.idea_round: dict[str, int] = {}
        self.cl_names: dict[str, str] = {}
        self._out: list = []
        self._ref_log: list = []
        self._mode = None
        self._margin = None
        self.state: dict = {}
        self.round_start: dict[int, float] = {}
        self.deep_start: dict[int, float] = {}
        self.run_start = self.run_end = None
        self.cand_vts: dict[str, float] = {}

    # ---------------------------------------------------------- reading files

    def _jsonl(self, rel: str, final: bool = False) -> list[tuple[int, dict]]:
        """New whole rows of a JSONL file since the saved byte offset, as (offset, row). A last line with no
        newline is taken only when it parses and the file has not grown since the previous pass (or final)."""
        p = self.rd / rel
        off = int(self.cur["off"].get(rel, 0))
        try:
            with open(p, "rb") as f:
                f.seek(off)
                data = f.read()
        except OSError:
            return []
        out, pos, start = [], off, 0
        while start < len(data):
            nl = data.find(b"\n", start)
            if nl < 0:
                tail = data[start:]
                size = off + len(data)
                row = None
                if tail.strip():
                    try:
                        row = json.loads(tail)
                    except ValueError:
                        row = None
                if row is not None and (final or self.cur["tail"].get(rel) == size):
                    if isinstance(row, dict):
                        out.append((pos, row))
                    pos = size
                    self.cur["tail"].pop(rel, None)
                else:
                    self.cur["tail"][rel] = size
                break
            line = data[start:nl]
            if line.strip():
                try:
                    row = json.loads(line)
                    if isinstance(row, dict):
                        out.append((pos, row))
                except ValueError:
                    print(f"[bridge] skipped a bad line in {rel} at byte {pos}", file=sys.stderr, flush=True)
            pos = off + nl + 1
            start = nl + 1
        self.cur["off"][rel] = pos
        return out

    def _json(self, rel: str):
        """(hash, obj) when the file changed since the last pass and parses; None otherwise (a cut file is
        retried next pass because its hash is not stored)."""
        try:
            b = (self.rd / rel).read_bytes()
        except OSError:
            return None
        h = _sha(b)
        if self.cur["hash"].get(rel) == h:
            return None
        try:
            obj = json.loads(b)
        except ValueError:
            return None
        self.cur["hash"][rel] = h
        return h, obj

    def _read_any(self, rel: str):
        try:
            return json.loads((self.rd / rel).read_text(encoding="utf-8"))
        except (OSError, ValueError):
            return None

    def _rows_all(self, rel: str) -> list[dict]:
        try:
            text = (self.rd / rel).read_text(encoding="utf-8")
        except OSError:
            return []
        out = []
        for ln in text.splitlines():
            try:
                r = json.loads(ln)
            except ValueError:
                continue
            if isinstance(r, dict):
                out.append(r)
        return out

    def _mtime(self, rel: str) -> float | None:
        try:
            return (self.rd / rel).stat().st_mtime
        except OSError:
            return None

    # ---------------------------------------------------------- emitting

    def _ev(self, kind: str, op: str, subject, label, data: dict, *, round_no=None, stage=None, t=None) -> None:
        ev = {"kind": kind, "op": f"br-{self.tag}-{op}", "subject": subject,
              "label": _cut(label, 80) if label else None, "data": _strip(data)}
        if isinstance(round_no, int):
            ev["round"] = round_no
        if stage in C.STAGES:
            ev["stage"] = stage
        self._out.append((t, round_no if isinstance(round_no, int) else 0, RANK.get(kind, 5), len(self._out), ev))

    def _t_round(self, round_no, rel: str | None = None, deep: bool = False):
        """Import time for a row with no timestamp: its round's first known time (for the arguments, the round's
        first interrogation decision when state.json has one), else the file's mtime."""
        if not self.timed:
            return None
        if deep and isinstance(round_no, int) and round_no in self.deep_start:
            return self.deep_start[round_no]
        if isinstance(round_no, int) and round_no in self.round_start:
            return self.round_start[round_no]
        return self._t_mtime(rel)

    def _t_mtime(self, rel: str | None):
        if not self.timed:
            return None
        m = self._mtime(rel) if rel else None
        if m is None:
            return self.run_end
        if self.run_start is not None and self.run_end is not None:
            m = min(max(m, self.run_start), self.run_end)       # a copied or checked-out folder has new mtimes
        return m

    def _t_row(self, row: dict, rel: str):
        if not self.timed:
            return None
        t = _ts(row.get("ts"))
        return t if t is not None else self._t_round(row.get("round"), rel)

    # ---------------------------------------------------------- context

    def _context(self) -> None:
        st = self._read_any("state.json")
        self.state = st if isinstance(st, dict) else {}
        if self._margin is None:
            com = self._read_any("commitments.json") or {}
            try:
                self._margin = float(((com.get("win") or {}).get("margin_nats")) or 0.0)
            except (TypeError, ValueError, AttributeError):
                self._margin = 0.0
        if self._mode is None:
            self._mode = self._detect_mode()

    def _detect_mode(self) -> str:
        if self.mode_arg in C.STATUS_WORDS:
            return self.mode_arg
        for d in self.state.get("decisions") or []:          # read only: decisions are never mirrored
            if isinstance(d, dict) and d.get("step") == "baseline" and d.get("mode") in C.STATUS_WORDS:
                return d["mode"]
        if (self.rd / "reference.json").exists():
            for r in self._rows_all("verify.jsonl")[:50]:
                if "panel_score" in ((r.get("details") or {}).get("metrics") or {}):
                    return "no_check"
            return "check_only"
        return "baseline"

    def _round_now(self):
        s = self.state.get("stage") or {}
        return s.get("round") if isinstance(s.get("round"), int) else None

    def _name(self, nid: str) -> str:
        return (self.cur["tree"].get(nid) or {}).get("name") or nid

    def _anchors(self) -> None:
        """Import only: the first known time of each round, the run's span, each candidate's first verify time
        and each sketch's round, from every file that carries a timestamp."""
        per_round: dict[int, list[float]] = {}
        allt: list[float] = []

        def add(t, r):
            if t is None:
                return
            allt.append(t)
            if isinstance(r, int):
                per_round.setdefault(r, []).append(t)
        st = self._read_any("state.json") or {}
        deep: dict[int, list[float]] = {}
        for d in st.get("decisions") or []:
            if isinstance(d, dict):
                add(_ts(d.get("ts")), d.get("round"))
                if d.get("step") in ("deepen", "dialogue") and _ts(d.get("ts")) and isinstance(d.get("round"), int):
                    deep.setdefault(d["round"], []).append(_ts(d["ts"]))
        self.deep_start = {r: min(v) for r, v in deep.items()}
        self.cand_vts: dict[str, float] = {}
        for r in self._rows_all("verify.jsonl"):
            t = _ts(r.get("ts"))
            add(t, r.get("round"))
            if t is not None and r.get("id") and r["id"] not in self.cand_vts:
                self.cand_vts[r["id"]] = t
        for rel in ["memory_log.jsonl", "control_log.jsonl"] + \
                   sorted("cands/" + p.name for p in (self.rd / "cands").glob("*.jsonl")):
            for r in self._rows_all(rel):
                add(_ts(r.get("ts")), r.get("round"))
        nq = self._read_any("next_questions.json") or {}
        add(_ts(nq.get("ts")), nq.get("round"))
        for e in (self._read_any("reference.json") or {}).get("log") or []:
            add(_ts(e.get("ts")), e.get("round"))
        stg = st.get("stage") or {}
        add(_ts(stg.get("ts")), stg.get("round"))
        self.round_start = {r: min(v) for r, v in per_round.items()}
        self.run_start = min(allt) if allt else None
        self.run_end = max(allt) if allt else None
        for r in self._rows_all("ideas.jsonl"):
            if r.get("id") and isinstance(r.get("round"), int):
                self.idea_round[r["id"]] = r["round"]

    # ---------------------------------------------------------- push: one source each

    def _tree(self) -> None:
        got = self._json("problem_tree.json")
        if not got:
            return
        obj = got[1]
        nodes = {n["id"]: n for n in obj.get("nodes") or [] if isinstance(n, dict) and n.get("id")}
        order: list[str] = []

        def walk(t):
            if isinstance(t, dict):
                if t.get("id") in nodes and t["id"] not in order:
                    order.append(t["id"])
                for ch in t.get("children") or []:
                    walk(ch)
        walk(obj.get("tree"))
        order += [i for i in nodes if i not in order]
        for nid in order:
            n = nodes[nid]
            seen = self.cur["tree"].get(nid)
            now = {"name": n.get("name", ""), "frame": n.get("frame", ""), "priority": n.get("priority"),
                   "parent": n.get("parent")}
            if seen is None:
                kind = n.get("kind") or ("root" if n.get("parent") is None else "part")
                data = {"id": nid, "name": n.get("name", ""), "parent": n.get("parent"),
                        "origin": n.get("origin") or "map", "kind": kind}
                for k in ("frame", "assumptions", "boundary", "directions", "depth", "test", "threshold", "fails_if"):
                    if n.get(k) not in (None, "", []):
                        data[k] = n[k]
                if n.get("disputed"):
                    data["disputed"] = n["disputed"]
                t = None
                if self.timed:
                    vt = [self.cand_vts[c] for c in n.get("from") or [] if c in self.cand_vts]
                    if not vt and nid.startswith(("win_", "q_")):
                        stem = nid.split("_", 1)[1]
                        vt = [v for c, v in self.cand_vts.items() if stem and c.startswith(stem)]
                    if vt:
                        t = max(vt)
                    elif now["parent"] is None or n.get("origin") in (None, "map", "human"):
                        t = self.run_start
                    else:
                        t = self._t_mtime("problem_tree.json")
                self._ev("node_added", f"na-{nid}", f"node:{nid}", n.get("name") or nid, data, t=t)
            else:
                changed = {k: now[k] for k in ("name", "frame", "priority") if seen.get(k) != now[k]}
                if changed:
                    h = _sha(json.dumps(changed, sort_keys=True).encode())[:10]
                    self._ev("node_edited", f"ne-{nid}-{h}", f"node:{nid}", n.get("name") or nid,
                             {"fields": changed}, t=self._t_mtime("problem_tree.json"))
            self.cur["tree"][nid] = now

    def _ideas(self, final: bool) -> None:
        rows = self._jsonl("ideas.jsonl", final)
        groups: dict[tuple, list] = {}
        for off, r in rows:
            if r.get("id") and isinstance(r.get("round"), int):
                self.idea_round[r["id"]] = r["round"]
            deep = r.get("card") == "deepen"
            key = (r.get("node") or "", r.get("direction") or "", r.get("round"), deep)
            groups.setdefault(key, []).append((off, r))
        for (node, direction, rnd, deep), items in groups.items():
            for i in range(0, len(items), SKETCH_BATCH):
                chunk = items[i:i + SKETCH_BATCH]
                its = [{"id": r.get("id"), "idea": _cut(r.get("idea"), 120), "card": r.get("card", ""),
                        "kind": r.get("kind", "")} for _, r in chunk]
                data = {"node": node, "direction": direction, "round": rnd, "count": len(its), "items": its}
                t = self._t_round(rnd, "ideas.jsonl", deep=deep)
                if self.timed and deep and t is not None:
                    t = t + 0.001                        # offshoots follow the arguments that made them
                self._ev("sketch_batch", f"sk-{chunk[0][0]}", f"node:{node}", self._name(node), data,
                         round_no=rnd, t=t)

    @staticmethod
    def _cl(c: dict) -> dict:
        return {"cluster_id": c.get("cluster_id"), "name": c.get("name", ""), "members": list(c.get("members") or []),
                "n": c.get("n", len(c.get("members") or [])), "rank": c.get("rank"), "score": c.get("score"),
                "selected": bool(c.get("selected")), "lane": c.get("lane"), "prior": c.get("prior")}

    def _group_order(self, keys):
        tree_ids = list(self.cur["tree"])
        return sorted(keys, key=lambda k: (tree_ids.index(k[0]) if k[0] in tree_ids else len(tree_ids), k[0], k[1]))

    def _cluster_stage(self) -> str | None:
        """clustered or deepened: the boundary these clusters belong to (state.json written after the clusters
        names it; written before, the clusters are for the next boundary)."""
        step = (self.state.get("stage") or {}).get("step")
        if step not in C.STAGES:
            return "clustered"
        ms, mc = self._mtime("state.json"), self._mtime("idea_clusters.json")
        if ms is not None and mc is not None and ms >= mc:
            return step if step in ("clustered", "deepened") else "deepened"
        nxt = C.STAGES[min(C.STAGES.index(step) + 1, len(C.STAGES) - 1)]
        return nxt if nxt in ("clustered", "deepened") else "clustered"

    def _clusters(self) -> None:
        got = self._json("idea_clusters.json")
        if not got:
            return
        obj = got[1]
        cls = [c for c in obj.get("clusters") or [] if isinstance(c, dict) and c.get("cluster_id")]
        for c in cls:
            self.cl_names[c["cluster_id"]] = c.get("name", "")
        rnd = obj.get("round") if isinstance(obj.get("round"), int) else self._round_now()
        if self.timed:
            self._cluster_history(cls, rnd)
        groups: dict[tuple, list] = {}
        for c in cls:
            groups.setdefault((c.get("node") or _node_of(c["cluster_id"]), c.get("direction") or ""), []).append(c)
        stage = self._cluster_stage()
        for key in self._group_order(groups):
            node, direction = key
            items = sorted((self._cl(c) for c in groups[key]), key=lambda c: _natural(c["cluster_id"]))
            h = _sha(json.dumps(items, sort_keys=True).encode())
            gk = f"{node}|{direction}"
            if self.cur["cg"].get(gk) == h:
                continue
            self.cur["cg"][gk] = h
            data = {"node": node, "direction": direction, "round": rnd, "stage": stage, "clusters": items}
            self._ev("cluster_snapshot", f"cs-{node}-{direction}-{h[:10]}", f"node:{node}", self._name(node), data,
                     round_no=rnd, stage=stage, t=self._t_mtime("idea_clusters.json"))

    def _cluster_history(self, final: list[dict], final_round) -> None:
        """Import only: earlier rounds' groupings rebuilt from selection.jsonl (one row per cluster and round)
        and the final clusters' members of that round or earlier, so a replay shows round 1's islands too."""
        sel: dict[int, list] = {}
        for r in self._rows_all("selection.jsonl"):
            if isinstance(r.get("round"), int) and (final_round is None or r["round"] < final_round):
                sel.setdefault(r["round"], []).append(r)
        by_name: dict[tuple, list] = {}
        for c in final:
            by_name.setdefault((c.get("node"), c.get("direction"), c.get("name")), []).append(c)
        for rnd in sorted(sel):
            groups: dict[tuple, dict] = {}
            for r in sel[rnd]:
                key = (r.get("node") or _node_of(r.get("cluster_id")), r.get("direction") or "")
                cands = by_name.get((key[0], key[1], r.get("name"))) or []
                members = []
                for c in cands:
                    members = [m for m in c.get("members") or [] if self.idea_round.get(m, 0) <= rnd]
                    if members:
                        break
                reason = str(r.get("reason") or "")
                item = {"cluster_id": r.get("cluster_id"), "name": r.get("name", ""), "members": members,
                        "n": len(members), "rank": r.get("rank"), "score": r.get("score"),
                        "selected": reason.startswith("picked"),
                        "lane": "main" if reason == "picked_main" else ("longshot" if reason == "picked_lane" else None),
                        "prior": cands[0].get("prior") if cands else None}
                groups.setdefault(key, {})[item["cluster_id"]] = item
            for key in self._group_order(groups):
                node, direction = key
                items = sorted(groups[key].values(), key=lambda c: _natural(c["cluster_id"]))
                data = {"node": node, "direction": direction, "round": rnd, "stage": "deepened", "clusters": items}
                self._ev("cluster_snapshot", f"csh-{rnd}-{node}-{direction}", f"node:{node}", self._name(node), data,
                         round_no=rnd, stage="deepened", t=self._t_round(rnd, "selection.jsonl"))

    def _members_round(self, members) -> int | None:
        rs = [self.idea_round[m] for m in members or [] if m in self.idea_round]
        return max(rs) if rs else self._round_now()

    def _deepen(self) -> None:
        got = self._json("deepen.json")
        if not got:
            return
        for n in got[1].get("nodes") or []:
            if not isinstance(n, dict) or n.get("parent") is not None or not n.get("id"):
                continue
            objs = [o for o in n.get("objections") or [] if isinstance(o, dict)]
            done = int(self.cur["dr"].get(n["id"], 0))
            cid = n.get("cluster_id") or ""
            node = n.get("node") or _node_of(cid)
            rnd = self._members_round(n.get("members"))
            for i in range(done, len(objs)):
                o = objs[i]
                data = {"node": node, "idea": cid, "members": list(n.get("members") or []), "objection": i + 1,
                        "cls": o.get("cls", ""), "severity": o.get("severity", ""), "text": _cut(o.get("text"), 400),
                        "if_true": o.get("if_true")}
                self._ev("objection_raised", f"ob-{n['id']}-{i + 1}", f"cluster:{cid}", n.get("cluster_name") or cid,
                         data, round_no=rnd, t=self._t_round(rnd, "deepen.json", deep=True))
            self.cur["dr"][n["id"]] = len(objs)

    def _dialogue(self, final: bool) -> None:
        for off, r in self._jsonl("dialogue.jsonl", final):
            cid = str(r.get("idea") or "")
            node = _node_of(cid)
            kind = r.get("reply") or ""
            text = {"concede": r.get("change") or r.get("revised_idea"), "rebut": r.get("fact"),
                    "measure": r.get("test")}.get(kind) or r.get("reason") or kind
            label = self.cl_names.get(cid) or cid
            rnd = r.get("round") if isinstance(r.get("round"), int) else None
            t = self._t_round(rnd, "dialogue.jsonl", deep=True)
            base = {"node": node, "idea": cid, "objection": r.get("objection")}
            self._ev("reply_posted", f"rp-{off}", f"cluster:{cid}", label,
                     {**base, "kind": kind, "text": _cut(text, 400), "fact": r.get("fact", ""),
                      "source": r.get("source", ""), "test": r.get("test", ""), "change": r.get("change", ""),
                      "exchange": r.get("exchange")}, round_no=rnd, t=t)
            self._ev("objection_marked", f"om-{off}", f"cluster:{cid}", label,
                     {**base, "verdict": r.get("verdict", ""), "reason": _cut(r.get("reason"), 300),
                      "exchange": r.get("exchange")}, round_no=rnd, t=t)

    def _cands(self, final: bool) -> None:
        try:
            files = sorted((self.rd / "cands").glob("*.jsonl"))
        except OSError:
            files = []
        for p in files:
            rel = "cands/" + p.name
            for off, r in self._jsonl(rel, final):
                cid = r.get("id")
                if not cid:
                    continue
                ex = r.get("extra") or {}
                hyp = ex.get("hypothesis") or str(r.get("text") or "").split(" | ")[0]
                info = {"node": ex.get("node", ""), "idea": r.get("operator", ""), "name": ex.get("cluster", "")}
                self.cur["cands"][cid] = info
                rnd = r.get("round") if isinstance(r.get("round"), int) else None
                data = {"node": info["node"], "cand": cid, "idea": info["idea"], "cluster_name": info["name"],
                        "members": list(ex.get("members") or []), "lane": ex.get("lane", ""),
                        "hypothesis": _cut(hyp, 300), "round": rnd}
                self._ev("candidate_built", f"cb-{cid}", f"cand:{cid}", info["name"] or hyp or cid, data,
                         round_no=rnd, t=self._t_row(r, rel))

    def _reference(self) -> None:
        """reference.json decides win in Modes 2 and 3. A row already sent before the reference moved to its
        candidate gets one corrective test_result."""
        got = self._json("reference.json")
        if not got:
            return
        log = [e for e in (got[1].get("log") or []) if isinstance(e, dict)]
        self._ref_log = log
        for e in log[int(self.cur.get("ref_n", 0)):]:
            to, rnd = e.get("to"), e.get("round")
            prev = self.cur["tr"].get(to or "")
            if prev and prev[0] == rnd and prev[1] not in ("win", "preferred"):
                word = "preferred" if self._mode == "no_check" else "win"
                info = self.cur["cands"].get(to) or {}
                self.cur["tr"][to] = [rnd, word]
                self._ev("test_result", f"trc-{to}-{rnd}", f"cand:{to}", info.get("name") or to,
                         {"node": info.get("node", ""), "cand": to, "idea": info.get("idea", ""), "status": word,
                          "rung": prev[2] if len(prev) > 2 else None, "metrics": {}, "reason": _cut(e.get("reason"), 200),
                          "reference": True, "corrects": True},
                         round_no=rnd if isinstance(rnd, int) else None, t=_ts(e.get("ts")) if self.timed else None)
        self.cur["ref_n"] = len(log)

    def _status(self, r: dict) -> tuple[str, bool]:
        mode = self._mode or "check_only"
        if r.get("status") != "checked":
            return "failed_check", False
        cid, rnd = r.get("id"), r.get("round")
        became = any(e.get("to") == cid and e.get("round") == rnd and e.get("action") in ("set", "moved")
                     for e in self._ref_log)
        m = (r.get("details") or {}).get("metrics") or {}
        gap = m.get("long_gap") if m.get("long_gap") is not None else m.get("learn_gap")
        margin = self._margin or 0.0
        if mode == "no_check":
            return ("preferred" if became else "not_preferred"), became
        if mode == "check_only":
            if became:
                return "win", True
            return ("tie" if gap is None or gap <= margin else "loss"), False
        if gap is None or abs(gap) <= margin:            # baseline (Mode 1): the gap to the baseline decides
            return "tie", False
        return ("win" if gap < 0 else "loss"), False

    def _verify(self, final: bool) -> None:
        if not self._ref_log:
            self._ref_log = (self._read_any("reference.json") or {}).get("log") or []
        for off, r in self._jsonl("verify.jsonl", final):
            cid = r.get("id")
            if not cid:
                continue
            info = self.cur["cands"].get(cid) or {}
            status, ref = self._status(r)
            det = r.get("details") or {}
            m = det.get("metrics") or {}
            rnd = r.get("round") if isinstance(r.get("round"), int) else None
            rung = det.get("rung_reached")
            data = {"node": info.get("node", ""), "cand": cid, "idea": info.get("idea", ""), "status": status,
                    "rung": rung, "metrics": {k: m[k] for k in METRIC_KEYS if isinstance(m.get(k), (int, float))},
                    "reason": _cut((r.get("feedback_record") or {}).get("reason"), 200), "reference": ref}
            self.cur["tr"][cid] = [rnd, status, rung]
            self._ev("test_result", f"tr-{off}", f"cand:{cid}", info.get("name") or cid, data, round_no=rnd,
                     t=self._t_row(r, "verify.jsonl"))

    def _questions(self) -> None:
        got = self._json("next_questions.json")
        if not got:
            return
        h, q = got
        ch = q.get("chosen") if isinstance(q.get("chosen"), dict) else {}
        top3 = [{"id": x.get("id"), "kind": x.get("kind"), "text": _cut(x.get("text"), 200), "score": x.get("score")}
                for x in q.get("top3") or [] if isinstance(x, dict)]
        vet = [v if isinstance(v, str) else (v or {}).get("id") for v in q.get("vetoed") or []]
        rnd = q.get("round") if isinstance(q.get("round"), int) else None
        data = {"round": rnd, "top3": top3, "chosen": ch.get("id"), "by": q.get("by", "default"), "vetoed": vet}
        subj = f"question:{ch['id']}" if ch.get("id") else None
        self._ev("question_picked", f"qp-{h[:10]}", subj, ch.get("text") or "none left", data, round_no=rnd,
                 t=self._t_row(q, "next_questions.json"))

    def _memory(self, final: bool) -> None:
        for off, r in self._jsonl("memory_log.jsonl", final):
            part = r.get("part") or ""
            rnd = r.get("round") if isinstance(r.get("round"), int) else None

            def n_of(v):
                return len(v) if isinstance(v, list) else (int(v) if isinstance(v, (int, float)) else 0)
            added = [{"id": a.get("id"), "section": a.get("section"), "source": a.get("source"),
                      "text": _cut(a.get("text"), 300)} for a in r.get("added") or [] if isinstance(a, dict)]
            data = {"node": part, "round": rnd, "added": added, "rejected": n_of(r.get("rejected")),
                    "archived": n_of(r.get("archived"))}
            self._ev("memory_added", f"ma-{off}", f"node:{part}", self._name(part), data, round_no=rnd,
                     t=self._t_row(r, "memory_log.jsonl"))

    def _stage(self) -> None:
        s = self.state.get("stage") or {}
        rnd, step = s.get("round"), s.get("step")
        if step not in C.STAGES:
            return
        key = f"{rnd}|{step}"
        if self.cur.get("stage") == key:
            return
        self.cur["stage"] = key
        self._ev("stage_entered", f"se-{rnd}-{step}", "run:main", None,
                 {"round": rnd, "stage": step, "waiting": False, "step_mode": False, "mode": self._mode},
                 round_no=rnd if isinstance(rnd, int) else None, stage=step, t=_ts(s.get("ts")) if self.timed else None)

    def _control_log(self, final: bool) -> None:
        """Each new control_log.jsonl row (a whole control state, no author) gives one control_applied naming
        the queued human events whose effect the row contains."""
        for off, r in self._jsonl("control_log.jsonl", final):
            ctl = r.get("control")
            if not isinstance(ctl, dict):
                continue                                   # a warning row holds no control state
            queued = [e for s, e in sorted(self.human.items()) if s not in self.applied]
            refs = [e["seq"] for e in queued if _in_control(e, ctl)]
            self.applied.update(refs)
            rnd = r.get("round") if isinstance(r.get("round"), int) else None
            stage = r.get("stage") if r.get("stage") in C.STAGES else None
            data = {"refs": refs, "round": rnd, "stage": stage, "keys": _keys_summary(ctl), "dropped": []}
            self._ev("control_applied", f"cl-{off}", "run:main", None, data, round_no=rnd, stage=stage,
                     t=self._t_row(r, "control_log.jsonl"))

    # ---------------------------------------------------------- pull

    def _fetch_events(self) -> None:
        """Read the log since the last seq seen (from 0 at every start), keeping only what the pull needs."""
        while True:
            st, d = self.client.call("GET", f"{C.ROUTES['events'][1]}?since={self.ev_cursor}&limit=2000")
            if st != 200:
                return
            if self.epoch is not None and d.get("epoch") not in (None, self.epoch):
                self.ev_cursor, self.human, self.kept, self.applied = 0, {}, [], set()
                self.epoch = d.get("epoch")
                continue
            self.epoch = d.get("epoch", self.epoch)
            evs = d.get("events") or []
            for e in evs:
                s = int(e.get("seq") or 0)
                self.ev_cursor = max(self.ev_cursor, s)
                k = e.get("kind")
                if k not in KEEP_KINDS:
                    continue
                self.kept.append(e)
                if k == "control_applied":
                    self.applied.update(int(x) for x in (e.get("data") or {}).get("refs") or [] if str(x).isdigit())
                elif k in QUEUE_KINDS and C.actor_class(e.get("by", ""), e.get("by_kind", ""),
                                                        e.get("owner", "")) in ("person", "delegate"):
                    self.human[s] = e
            head = int(d.get("head") or 0)
            if not evs or self.ev_cursor >= head:
                return

    def _render_control(self) -> bool:
        """control.json from the merged control; the file's own run keys stay. True when the file was written."""
        st, d = self.client.call("GET", f"{C.ROUTES['control'][1]}?loop={ACTOR}&since=0")
        if st == 200 and isinstance(d.get("control"), dict):
            ctl, refs = d["control"], d.get("refs") or []
        elif st in (404, 501):
            from space import control as CTRL           # the server has no control route: merge here
            res = CTRL.merge(self.kept, loop=ACTOR)
            ctl, refs = res["control"], res.get("refs") or []
        else:
            return False
        disk = None
        try:
            disk = json.loads(self.control_path.read_text(encoding="utf-8"))
        except (OSError, ValueError):
            disk = None
        file_ctl = disk if isinstance(disk, dict) else {}
        out = {k: file_ctl[k] for k in C.FILE_ONLY_KEYS if k in file_ctl}
        out.update({k: v for k, v in ctl.items() if k not in C.FILE_ONLY_KEYS})
        if out == disk:
            return False
        if disk is None and not refs and not any(out.get(k) for k in C.CONTROL_KEYS):
            return False                                   # nothing to say yet: do not create the file
        from space import control as CTRL
        CTRL.render_control_json(str(self.control_path), out)
        return True

    def _beat(self) -> None:
        now = time.monotonic()
        if now - self.last_beat < C.HEARTBEAT_S:
            return
        self.last_beat = now
        live = self._read_any("live.json") or {}
        inflight = len(live.get("inflight") or []) if isinstance(live, dict) else 0
        phase = str(live.get("phase") or "") if isinstance(live, dict) else ""
        body = {"client": ACTOR, "name": "team bridge", "owner": "team", "view": "run",
                "activity": {"state": "finished" if phase == "done" else ("executing" if inflight else "waiting"),
                             "phase": phase, "text": _cut(live.get("note") if isinstance(live, dict) else "", 160),
                             "inflight": inflight},
                "cursor": self.ev_cursor, "claims": [], "bye": False}
        try:
            self.client.call("POST", C.ROUTES["presence"][1], body)
        except (OSError, ValueError):
            pass

    # ---------------------------------------------------------- passes

    def collect(self, final: bool = False) -> list:
        """Read every source once; return the new events as (t, round, rank, n, event)."""
        self._out = []
        self._context()
        if self.timed:
            self._anchors()
        self._control_log(final)
        self._tree()
        self._questions()
        self._ideas(final)
        self._clusters()
        self._deepen()
        self._dialogue(final)
        self._cands(final)
        self._reference()
        self._verify(final)
        self._memory(final)
        self._stage()
        return self._out

    def save(self) -> None:
        if not self.persist:
            return
        try:
            _write_atomic(self.cursor_path, json.dumps(self.cur, sort_keys=True))
        except OSError as e:
            print(f"[bridge] could not save the cursor: {e}", file=sys.stderr, flush=True)

    def pass_once(self, final: bool = False) -> int:
        """One pass: flush the outbox, pull (events, control.json), push the new run rows, save the cursor."""
        self.client.down = False
        self.client.flush_outbox()
        if self.pull:
            try:
                self._fetch_events()
                self._render_control()
            except (OSError, ValueError):
                pass
        out = self.collect(final)
        evs = [x[4] for x in out]
        if evs:
            self.client.post(evs)
        self.save()
        if self.presence:
            self._beat()
        return len(evs)

    def run(self, every: float = 0.5, stop=None, max_passes: int | None = None) -> None:
        n = 0
        while True:
            t0 = time.perf_counter()
            self.pass_once()
            n += 1
            if max_passes is not None and n >= max_passes:
                return
            wait = max(0.0, every - (time.perf_counter() - t0))
            if stop is not None:
                if stop.wait(wait):
                    return
            else:
                time.sleep(wait)


# ---------------------------------------------------------------- control_log matching

def _in_control(e: dict, ctl: dict) -> bool:
    k, d = e.get("kind"), e.get("data") or {}
    subj = str(e.get("subject") or "")
    sid = subj.split(":", 1)[1] if ":" in subj else ""
    if k == "node_added":
        ids = {_clean_id(a.get("id")) for a in ctl.get("add_nodes") or [] if isinstance(a, dict)}
        return _clean_id(d.get("id")) in ids
    if k in ("node_skipped", "node_unskipped"):
        nid = str(d.get("node") or d.get("id") or sid)
        inside = nid in set(ctl.get("skip_nodes") or [])
        return inside if k == "node_skipped" else not inside
    if k in ("question_vetoed", "question_unvetoed"):
        q = str(d.get("question") or sid)
        inside = q in set(ctl.get("veto") or [])
        return inside if k == "question_vetoed" else not inside
    if k == "question_chosen":
        return bool(ctl.get("choose")) and str(ctl.get("choose")) == str(d.get("question") or sid)
    if k == "note_posted":
        text = re.sub(r"\s+", " ", str(d.get("text") or "")).strip()[:60]
        return bool(text) and text in re.sub(r"\s+", " ", str(ctl.get("note") or ""))
    if k == "opinion_given":
        tgt = str(d.get("target") or "")
        return any(isinstance(o, dict) and o.get("who") == e.get("owner") and tgt in (o.get("cluster"), o.get("candidate"))
                   for o in ctl.get("opinions") or [])
    if k == "run_paused":
        return bool(ctl.get("pause"))
    if k == "run_resumed":
        return not ctl.get("pause")
    return False


def _keys_summary(ctl: dict) -> dict:
    return {"add_nodes": [_clean_id(a.get("id")) for a in ctl.get("add_nodes") or [] if isinstance(a, dict)],
            "skip_nodes": list(ctl.get("skip_nodes") or []), "veto": list(ctl.get("veto") or []),
            "choose": ctl.get("choose"), "notes": len([x for x in str(ctl.get("note") or "").split("\n") if x.strip()]),
            "opinions": len(ctl.get("opinions") or []), "pause": bool(ctl.get("pause")), "disputes": 0}


def _natural(cid) -> tuple:
    return tuple(int(p) if p.isdigit() else p for p in re.split(r"(\d+)", str(cid or "")))


# ---------------------------------------------------------------- import

def is_finished(run_dir) -> bool:
    run = Path(run_dir)
    if (run / "answer.json").exists():
        return True
    try:
        return json.loads((run / "live.json").read_text(encoding="utf-8")).get("phase") == "done"
    except (OSError, ValueError, AttributeError):
        return False


def order_events(out: list) -> list[dict]:
    """Sort by original time (then round, then the loop's order inside a round) and stamp data.orig_ts."""
    known = [x[0] for x in out if x[0] is not None]
    fallback = max(known) if known else time.time()
    rows = sorted(((x[0] if x[0] is not None else fallback, x[1], x[2], x[3], x[4]) for x in out),
                  key=lambda x: x[:4])
    evs = []
    for t, _, _, _, ev in rows:
        ev["data"]["orig_ts"] = _iso(t)
        ev["_t"] = t
        evs.append(ev)
    return evs


def post_paced(client: Client, evs: list[dict], pace: str = "original", speed: float = 1.0,
               max_gap: float | None = None, sleep=time.sleep) -> float:
    """Post in order. Pace fast: at once, 100 per POST. Pace original: events of one original second together,
    sleeping the original gap divided by speed (cut to max_gap when given) between them. Returns seconds slept."""
    if pace == "fast":
        for e in evs:
            e.pop("_t", None)
        client.post(evs)
        return 0.0
    slept, prev, group = 0.0, None, []
    for e in evs:
        t = e.pop("_t", None)
        if prev is not None and t is not None and t != prev:
            client.post(group)
            group = []
            gap = max(0.0, (t - prev) / max(speed, 1e-9))
            if max_gap is not None:
                gap = min(gap, max_gap)
            if gap > 0:
                sleep(gap)
                slept += gap
        if t is not None:
            prev = t
        group.append(e)
    if group:
        client.post(group)
    return slept


def import_run(run_dir, space: str = C.BASE_URL, *, pace: str = "original", speed: float = 1.0,
               max_gap: float | None = None, every: float = 0.5, tail: bool | None = None, mode: str | None = None,
               key: str = "", cursor_path=None, outbox_path=None, control_path=None, stop=None,
               max_passes: int | None = None) -> dict:
    """Replay a run folder into the space at its original pace (or fast). A folder still being written is then
    tailed like --run. Returns counts."""
    finished = is_finished(run_dir)
    b = Bridge(run_dir, space, cursor_path=cursor_path, outbox_path=outbox_path, control_path=control_path,
               pull=False, presence=False, mode=mode, key=key, fresh=True, persist=False, timed=True)
    b.client.flush_outbox()
    evs = order_events(b.collect(final=finished))
    t0 = time.perf_counter()
    slept = post_paced(b.client, evs, pace, speed, max_gap)
    res = {"events": len(evs), "posted": b.client.posted, "errors": b.client.errors, "slept_s": round(slept, 3),
           "wall_s": round(time.perf_counter() - t0, 3), "finished": finished}
    if tail if tail is not None else not finished:
        b.timed, b.persist, b.pull, b.presence = False, True, True, True
        b.save()
        b.run(every, stop=stop, max_passes=max_passes)
    return res


# ---------------------------------------------------------------- command line

def main(argv=None) -> int:
    ap = argparse.ArgumentParser(prog="python -m space.bridge", description=__doc__.split("\n\n")[0])
    src = ap.add_mutually_exclusive_group(required=True)
    src.add_argument("--run", help="the run folder of a loop that runs without --space (tailed)")
    src.add_argument("--import", dest="import_dir", help="a run folder to replay in the order of its timestamps")
    ap.add_argument("--space", default=C.BASE_URL)
    ap.add_argument("--every", type=float, default=0.5, help="seconds between passes")
    ap.add_argument("--pace", choices=("original", "fast"), default="original")
    ap.add_argument("--speed", type=float, default=1.0, help="original gaps are divided by this")
    ap.add_argument("--max-gap", type=float, default=None, help="cap one sleep of the import, in seconds")
    ap.add_argument("--mode", choices=sorted(C.STATUS_WORDS), default=None, help="status words (default: detected)")
    ap.add_argument("--key", default=os.environ.get("HTSA_SPACE_KEY", ""), help="X-Space-Key for a --lan server")
    ap.add_argument("--once", action="store_true", help="one pass, then exit")
    ap.add_argument("--no-pull", action="store_true", help="do not render control.json")
    ap.add_argument("--force", action="store_true", help=f"run even when {MODE_FILE} says the loop has --space")
    a = ap.parse_args(argv)
    run_dir = Path(a.run or a.import_dir)
    if not run_dir.is_dir():
        print(f"[bridge] no such run folder: {run_dir}", file=sys.stderr)
        return 1
    if (run_dir / MODE_FILE).exists() and not a.force:
        print(f"[bridge] {run_dir / MODE_FILE} exists: the loop pushes and pulls the space itself. "
              f"Not starting (use --force to override).", file=sys.stderr)
        return 2
    try:
        if a.import_dir:
            res = import_run(run_dir, a.space, pace=a.pace, speed=a.speed, max_gap=a.max_gap, every=a.every,
                             mode=a.mode, key=a.key, max_passes=1 if a.once else None)
            print(f"[bridge] imported {res['events']} events ({res['errors']} refused) in {res['wall_s']} s", flush=True)
            return 0
        b = Bridge(run_dir, a.space, pull=not a.no_pull, mode=a.mode, key=a.key)
        print(f"[bridge] {run_dir} -> {a.space} every {a.every} s", flush=True)
        b.run(a.every, max_passes=1 if a.once else None)
    except KeyboardInterrupt:
        pass
    return 0


if __name__ == "__main__":
    sys.exit(main())
