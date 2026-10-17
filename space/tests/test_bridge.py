"""P3 space-bridge tests (docs/MULTIPLAYER_DESIGN.md section 12.1 row P3 and brief 16.4).

Everything runs under tmp_path against an in-process fake server on 127.0.0.1 that records POSTs and answers
seqs; its routes come from contract.ROUTES. No model call, no other part's server code."""
from __future__ import annotations

import json
import os
import random
import shutil
import socket
import threading
import time
import urllib.parse
from datetime import datetime
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

import pytest

from space import bridge as B
from space import contract as C
from space import control as CTRL

FIXTURE = Path(__file__).parent / "fixtures" / "run_mock"
REAL_RUN = Path(r"D:\AGI-lab\runs\mock-after-bugpass__nano__binpack_nobase__scaffold__r0")
R = {name: path for name, (method, path) in C.ROUTES.items()}


# ---------------------------------------------------------------- the fake server

class FakeSpace:
    """Records every POST, numbers events gap-free, dedupes on (by, op), merges control with space.control."""

    MAX_BODY = 65536                                       # the real server answers 413 too_big above this

    def __init__(self, control_route: bool = True, key: str = ""):
        self.events: list[dict] = []
        self.posts: list[list[dict]] = []
        self.refused: list[tuple[int, int]] = []               # (status, body bytes) of refused POSTs
        self.key = key
        self.presence: list[dict] = []
        self.ops: dict[tuple, int] = {}
        self.control_route = control_route
        self.lock = threading.Lock()
        fake = self

        class H(BaseHTTPRequestHandler):
            def log_message(self, *a):
                pass

            def _send(self, code, obj):
                b = json.dumps(obj).encode()
                self.send_response(code)
                self.send_header("Content-Type", "application/json")
                self.send_header("Content-Length", str(len(b)))
                self.end_headers()
                self.wfile.write(b)

            def do_GET(self):
                u = urllib.parse.urlparse(self.path)
                q = dict(urllib.parse.parse_qsl(u.query))
                if u.path == R["events"]:
                    since, limit = int(q.get("since", 0)), int(q.get("limit", 500))
                    with fake.lock:
                        evs = [e for e in fake.events if e["seq"] > since][:limit]
                        head = len(fake.events)
                    return self._send(200, {"epoch": "e1", "head": head, "events": evs})
                if u.path == R["control"] and fake.control_route:
                    with fake.lock:
                        res = CTRL.merge(list(fake.events), loop=q.get("loop", "team.loop"),
                                         since=int(q.get("since", 0)))
                    return self._send(200, {"head": len(fake.events), **res})
                return self._send(404, {"error": "no_route"})

            def do_POST(self):
                raw = self.rfile.read(int(self.headers.get("Content-Length") or 0))
                if fake.key and self.headers.get("X-Space-Key") != fake.key:
                    fake.refused.append((403, len(raw)))
                    return self._send(403, {"error": "bad_key"})
                if len(raw) > FakeSpace.MAX_BODY:
                    fake.refused.append((413, len(raw)))
                    return self._send(413, {"error": "too_big"})
                body = json.loads(raw or b"{}")
                u = urllib.parse.urlparse(self.path)
                actor, kind = self.headers.get("X-Space-Actor", ""), self.headers.get("X-Space-Kind", "")
                if u.path == R["presence"]:
                    fake.presence.append(body)
                    return self._send(200, {"head": len(fake.events), "claims_ok": True, "interrupts": []})
                if u.path != R["post"]:
                    return self._send(404, {"error": "no_route"})
                batch = body.get("events") if isinstance(body.get("events"), list) else [body]
                fake.posts.append(batch)
                res = [fake.add(e, actor, kind) for e in batch]
                return self._send(200, {"results": res} if "events" in body else res[0])

        self.httpd = ThreadingHTTPServer(("127.0.0.1", 0), H)
        self.url = "http://127.0.0.1:%d" % self.httpd.server_address[1]
        threading.Thread(target=self.httpd.serve_forever, daemon=True).start()

    def add(self, e: dict, by: str, by_kind: str, owner: str | None = None) -> dict:
        with self.lock:
            op = e.get("op")
            if op and (by, op) in self.ops:
                return {"seq": self.ops[(by, op)], "dup": True}
            seq = len(self.events) + 1
            ev = {"seq": seq, "ts": "2026-10-17T00:00:00.000Z", "by": by, "by_kind": by_kind,
                  "owner": owner or (by.split(".")[0] if by_kind != "system" else "team"), **{
                      k: e.get(k) for k in ("kind", "subject", "label", "data", "op", "round", "stage", "cause")}}
            self.events.append(ev)
            if op:
                self.ops[(by, op)] = seq
            return {"seq": seq, "dup": False}

    def human(self, kind, by, data, subject=None, by_kind="human", owner=None):
        return self.add({"kind": kind, "data": data, "subject": subject}, by, by_kind, owner)["seq"]

    def posted(self, kind=None) -> list[dict]:
        return [e for b in self.posts for e in b if kind is None or e["kind"] == kind]

    def close(self):
        self.httpd.shutdown()
        self.httpd.server_close()


@pytest.fixture
def fake():
    f = FakeSpace()
    yield f
    f.close()


def copy_run(tmp_path, name="run") -> Path:
    dst = tmp_path / name
    shutil.copytree(FIXTURE, dst)
    return dst


def bridge(run, fake, **kw):
    kw.setdefault("pull", False)
    kw.setdefault("presence", False)
    return B.Bridge(run, fake.url, **kw)


def kinds(evs):
    out = {}
    for e in evs:
        out[e["kind"]] = out.get(e["kind"], 0) + 1
    return out


def tree_order(run) -> list[str]:
    t = json.loads((run / "problem_tree.json").read_text(encoding="utf-8"))
    order = []

    def walk(n):
        order.append(n["id"])
        for c in n.get("children") or []:
            walk(c)
    walk(t["tree"])
    return order


def forbidden(evs) -> list[str]:
    bad = []

    def keys(o, path):
        if isinstance(o, dict):
            for k, v in o.items():
                if k in ("obvious", "obvious_match", "private", "spent", "spent_aux", "spent_by_stage", "decisions"):
                    bad.append(f"{path}.{k}")
                keys(v, f"{path}.{k}")
        elif isinstance(o, list):
            for i, v in enumerate(o):
                keys(v, f"{path}[{i}]")
    for e in evs:
        keys(e, e["kind"])
        s = json.dumps(e)
        for w in ("obvious_match", "prompts/", "prompts\\\\", "calls/", "private/"):
            if w in s:
                bad.append(f"{e['kind']} contains {w}")
    return bad


# ---------------------------------------------------------------- the fixture round trip

def test_fixture_round_trip(tmp_path, fake):
    run = copy_run(tmp_path)
    b = bridge(run, fake)
    n = b.pass_once()
    evs = fake.posted()
    assert n == len(evs) > 0
    assert fake.refused == []                              # every body under 64 KB
    assert all(len(p) <= B.POST_BATCH for p in fake.posts)
    assert all(len(json.dumps({"events": p})) <= B.POST_CAP for p in fake.posts)
    k = kinds(evs)
    # 9 node_added in tree order
    nodes = [e["data"]["id"] for e in evs if e["kind"] == "node_added"]
    assert len(nodes) == 9 and nodes == tree_order(run)
    root = next(e for e in evs if e["kind"] == "node_added")
    assert root["data"]["parent"] is None and root["data"]["origin"] == "map"
    assert {e["data"]["kind"] for e in evs if e["kind"] == "node_added"} <= {"part", "question", "win"}
    q = next(e for e in evs if e["kind"] == "node_added" and e["data"]["id"] == "q_n44a9d66")
    assert q["data"]["origin"] == "failure" and q["data"]["kind"] == "question" and q["data"]["fails_if"]
    # one cluster_snapshot per (node, direction)
    cl = json.loads((run / "idea_clusters.json").read_text(encoding="utf-8"))["clusters"]
    groups = {(c["node"], c["direction"]) for c in cl}
    snaps = [e for e in evs if e["kind"] == "cluster_snapshot"]
    assert len(snaps) == len(groups) and {(e["data"]["node"], e["data"]["direction"]) for e in snaps} == groups
    assert sum(len(e["data"]["clusters"]) for e in snaps) == len(cl)
    for e in snaps:
        for c in e["data"]["clusters"]:
            assert set(c) == {"cluster_id", "name", "members", "n", "rank", "score", "selected", "lane", "prior"}
    # sketch batches of 50 at most, every sketch once
    sk = [e for e in evs if e["kind"] == "sketch_batch"]
    assert sk and all(1 <= e["data"]["count"] == len(e["data"]["items"]) <= 50 for e in sk)
    ids = [i["id"] for e in sk for i in e["data"]["items"]]
    assert len(ids) == len(set(ids)) == 200
    assert all(set(i) == {"id", "idea", "card", "kind"} for e in sk for i in e["data"]["items"])
    # arguments: one reply and one mark per dialogue row; objections from the 6 deepen roots
    n_dialogue = sum(1 for ln in (run / "dialogue.jsonl").read_text(encoding="utf-8").splitlines() if ln.strip())
    assert n_dialogue == 180
    assert k["reply_posted"] == k["objection_marked"] == n_dialogue
    roots = [n for n in json.loads((run / "deepen.json").read_text(encoding="utf-8"))["nodes"] if n.get("parent") is None]
    assert len(roots) == 6 and k["objection_raised"] == sum(len(r["objections"]) for r in roots) == 24
    rp = next(e for e in evs if e["kind"] == "reply_posted")
    assert rp["data"]["node"] == "state" and rp["data"]["kind"] in ("concede", "rebut", "measure") and rp["data"]["text"]
    # 16 test results with Mode 2 words; the reference decides the win
    tr = [e for e in evs if e["kind"] == "test_result"]
    assert len(tr) == 16
    assert {e["data"]["status"] for e in tr} <= set(C.STATUS_WORDS["check_only"])
    first = {}
    for e in tr:
        first.setdefault(e["data"]["cand"], e["data"])
    assert first["n67b58279e0"]["status"] == "failed_check"
    assert first["nbcd037208c"]["status"] == "win" and first["nbcd037208c"]["reference"] is True
    assert first["n09d50f5801"]["status"] == "tie"
    assert first["nf1a4803fd7"]["status"] == "loss"
    assert first["nf1a4803fd7"]["node"] == "choice" and set(first["nf1a4803fd7"]["metrics"]) <= set(B.METRIC_KEYS)
    assert k["memory_added"] == 4 and k["candidate_built"] == 9 and k["question_picked"] == 1
    assert k["stage_entered"] == 1
    se = next(e for e in evs if e["kind"] == "stage_entered")
    assert se["data"] == {"round": 2, "stage": "verified", "waiting": False, "step_mode": False, "mode": "check_only"}
    # every kind is a contract kind a team actor may write; every op is unique
    assert all(e["kind"] in C.KINDS and "team" in C.KINDS[e["kind"]][0].split() for e in evs)
    assert all(all(key in e["data"] for key in C.KINDS[e["kind"]][1]) for e in evs)
    assert len({e["op"] for e in evs}) == len(evs)
    assert all(fake.events[i]["by"] == "team.bridge" and fake.events[i]["by_kind"] == "system"
               for i in range(len(fake.events)))
    assert forbidden(evs) == []
    # a second pass emits nothing; a restarted bridge reads its cursor and emits nothing
    assert b.pass_once() == 0
    assert bridge(run, fake).pass_once() == 0
    assert len(fake.posted()) == n
    assert (run / B.CURSOR_FILE).exists()


def test_cluster_keys_identical_for_a_shuffled_copy(tmp_path, fake):
    a = copy_run(tmp_path, "a")
    b_ = copy_run(tmp_path, "b")
    p = b_ / "idea_clusters.json"
    obj = json.loads(p.read_text(encoding="utf-8"))
    random.Random(7).shuffle(obj["clusters"])
    p.write_text(json.dumps(obj), encoding="utf-8")

    def snaps(run):
        before = len(fake.posted())
        bridge(run, fake).pass_once()
        out = []
        for e in fake.posted()[before:]:
            if e["kind"] == "cluster_snapshot":
                d = dict(e["data"])
                d.pop("stage")
                out.append((e["subject"], json.dumps(d, sort_keys=True)))
        return out
    sa, sb = snaps(a), snaps(b_)
    assert sa and sa == sb


def test_one_appended_verify_line_gives_one_test_result(tmp_path, fake):
    run = copy_run(tmp_path)
    b = bridge(run, fake)
    b.pass_once()
    row = json.loads((run / "verify.jsonl").read_text(encoding="utf-8").splitlines()[1])
    row.update(id="n0123456789", round=3, ts="2026-10-17T19:40:00")
    with open(run / "verify.jsonl", "a", encoding="utf-8") as f:
        f.write(json.dumps(row) + "\n")
    before = len(fake.posted())
    assert b.pass_once() == 1
    new = fake.posted()[before:]
    assert [e["kind"] for e in new] == ["test_result"] and new[0]["data"]["cand"] == "n0123456789"


def test_torn_last_line_is_skipped_then_emitted(tmp_path, fake):
    run = copy_run(tmp_path)
    b = bridge(run, fake)
    b.pass_once()
    line = json.dumps({"round": 3, "part": "ties", "added": [{"id": "m1234567", "section": "FACTS", "source": "measured",
                                                               "text": "ties broken by index cost nothing"}],
                       "rejected": [], "archived": [], "ts": "2026-10-17T19:41:00"})
    with open(run / "memory_log.jsonl", "a", encoding="utf-8") as f:
        f.write(line[:40])
    assert b.pass_once() == 0
    assert b.pass_once() == 0
    with open(run / "memory_log.jsonl", "a", encoding="utf-8") as f:
        f.write(line[40:] + "\n")
    before = len(fake.posted())
    assert b.pass_once() == 1
    e = fake.posted()[before]
    assert e["kind"] == "memory_added" and e["data"]["node"] == "ties" and e["data"]["added"][0]["id"] == "m1234567"


def test_cut_json_file_is_retried_next_pass(tmp_path, fake):
    run = copy_run(tmp_path)
    b = bridge(run, fake)
    b.pass_once()
    p = run / "next_questions.json"
    full = json.loads(p.read_text(encoding="utf-8"))
    full["round"], full["chosen"]["id"] = 3, "u0000000001"
    text = json.dumps(full)
    p.write_text(text[: len(text) // 2], encoding="utf-8")
    assert b.pass_once() == 0
    p.write_text(text, encoding="utf-8")
    before = len(fake.posted())
    assert b.pass_once() == 1
    e = fake.posted()[before]
    assert e["kind"] == "question_picked" and e["data"]["chosen"] == "u0000000001" and e["data"]["round"] == 3


def test_deepen_rewrite_emits_only_new_objections(tmp_path, fake):
    run = copy_run(tmp_path)
    b = bridge(run, fake)
    b.pass_once()
    p = run / "deepen.json"
    obj = json.loads(p.read_text(encoding="utf-8"))
    root = next(n for n in obj["nodes"] if n.get("parent") is None)
    root["objections"].append({"text": "it breaks on tiny items", "severity": "low", "cls": "scale_only",
                               "if_true": None})
    random.Random(3).shuffle(obj["nodes"])
    p.write_text(json.dumps(obj), encoding="utf-8")
    before = len(fake.posted())
    assert b.pass_once() == 1
    e = fake.posted()[before]
    assert e["kind"] == "objection_raised" and e["data"]["objection"] == 5 and e["data"]["text"] == "it breaks on tiny items"


def test_reference_moving_later_corrects_the_status_once(tmp_path, fake):
    run = copy_run(tmp_path)
    b = bridge(run, fake)
    b.pass_once()
    p = run / "reference.json"
    ref = json.loads(p.read_text(encoding="utf-8"))
    ref["log"].append({"round": 1, "action": "moved", "from": "nbcd037208c", "to": "nf1a4803fd7", "reason": "test",
                       "gap": -0.01, "ts": "2026-10-17T19:34:40"})
    p.write_text(json.dumps(ref), encoding="utf-8")
    before = len(fake.posted())
    assert b.pass_once() == 1
    e = fake.posted()[before]
    assert e["kind"] == "test_result" and e["data"]["cand"] == "nf1a4803fd7" and e["data"]["status"] == "win"
    assert e["data"]["reference"] is True
    assert b.pass_once() == 0


# ---------------------------------------------------------------- pull: control.json and control_applied

SIX = [("node_added", "ana", "human", None, "node:item_order",
        {"id": "item_order", "name": "item order", "parent": "root", "frame": "how items are sorted before packing",
         "assumptions": [], "directions": ["inward", "outward"], "origin": "human"}),
       ("node_skipped", "ben", "human", None, "node:stats", {"reason": "no time"}),
       ("question_vetoed", "ana.agent", "agent", "ana", "question:u3d885a4738",
        {"question": "u3d885a4738", "text": "judge by loss on rare tokens"}),
       ("question_chosen", "ben", "human", None, "question:q_n44a9d66",
        {"question": "q_n44a9d66", "text": "why did worst fit fail?"}),
       ("note_posted", "ben", "human", None, None, {"text": "check tie-breaking before the choice rule"}),
       ("opinion_given", "ana", "human", None, "cluster:best fit", {"target": "best fit", "score": 7,
                                                                    "note": "fair and cheap"})]

EXPECTED = {"add_nodes": [{"id": "item_order", "name": "item order", "parent": "root",
                           "frame": "how items are sorted before packing", "assumptions": [],
                           "directions": ["inward", "outward"], "origin": "human", "by": "ana", "by_seq": 1}],
            "skip_nodes": ["stats"], "veto": ["u3d885a4738"], "choose": "q_n44a9d66",
            "note": "ben: check tie-breaking before the choice rule",
            "opinions": [{"cluster": "best fit", "score": 7, "note": "fair and cheap", "who": "ana"}],
            "pause": False, "findings": [], "budget_add": 500}


def post_six(fake):
    return [fake.human(kind, by, data, subject, by_kind=bk, owner=owner) for kind, by, bk, owner, subject, data in SIX]


@pytest.mark.parametrize("route", [True, False], ids=["control_route", "local_merge"])
def test_control_json_from_six_human_events(tmp_path, route):
    fake = FakeSpace(control_route=route)
    try:
        run = tmp_path / "run"
        run.mkdir()
        (run / "control.json").write_text(json.dumps({"budget_add": 500, "note": "an old hand-written note"}),
                                          encoding="utf-8")
        assert post_six(fake) == [1, 2, 3, 4, 5, 6]
        b = bridge(run, fake, pull=True)
        b.pass_once()
        exp_file = tmp_path / "expected_control.json"
        exp_file.write_text(json.dumps(EXPECTED, indent=1), encoding="utf-8")
        rendered = tmp_path / "rendered_expected.json"
        CTRL.render_control_json(str(rendered), json.loads(exp_file.read_text(encoding="utf-8")))
        assert (run / "control.json").read_bytes() == rendered.read_bytes()
        mtime = (run / "control.json").stat().st_mtime_ns
        b.pass_once()                                      # same state: the file is not rewritten
        assert (run / "control.json").stat().st_mtime_ns == mtime
        assert fake.posted() == []                         # an empty run folder pushes nothing
    finally:
        fake.close()


def test_no_control_json_when_the_space_has_nothing_to_say(tmp_path, fake):
    run = tmp_path / "run"
    run.mkdir()
    bridge(run, fake, pull=True).pass_once()
    assert not (run / "control.json").exists()


def test_control_log_row_gives_one_control_applied(tmp_path, fake):
    run = tmp_path / "run"
    run.mkdir()
    seqs = post_six(fake)
    b = bridge(run, fake, pull=True)
    b.pass_once()
    ctl = json.loads((run / "control.json").read_text(encoding="utf-8"))
    with open(run / "control_log.jsonl", "a", encoding="utf-8") as f:     # what the loop logs at its boundary
        f.write(json.dumps({"ts": "2026-10-17T19:50:00", "round": 1, "stage": "ideated", "control": ctl}) + "\n")
    assert b.pass_once() == 1
    ca = fake.posted("control_applied")
    assert len(ca) == 1 and ca[0]["data"]["refs"] == seqs
    assert ca[0]["data"]["round"] == 1 and ca[0]["data"]["stage"] == "ideated"
    assert ca[0]["data"]["keys"]["add_nodes"] == ["item_order"] and ca[0]["data"]["keys"]["choose"] == "q_n44a9d66"
    # a later human event, then a row that holds it: only that seq is named
    s7 = fake.human("node_unskipped", "ben", {"reason": "back"}, "node:stats")
    b.pass_once()
    ctl = json.loads((run / "control.json").read_text(encoding="utf-8"))
    assert ctl["skip_nodes"] == []
    with open(run / "control_log.jsonl", "a", encoding="utf-8") as f:
        f.write(json.dumps({"ts": "2026-10-17T19:51:00", "round": 1, "stage": "clustered", "control": ctl}) + "\n")
        f.write(json.dumps({"ts": "2026-10-17T19:51:01", "round": 1, "stage": "clustered", "warning": "unreadable"}) + "\n")
    b.pass_once()
    ca = fake.posted("control_applied")
    assert len(ca) == 2 and ca[1]["data"]["refs"] == [s7]
    # a restarted bridge rebuilds the queue from the log and names nothing twice
    b2 = bridge(run, fake, pull=True)
    with open(run / "control_log.jsonl", "a", encoding="utf-8") as f:
        f.write(json.dumps({"ts": "2026-10-17T19:52:00", "round": 1, "stage": "deepened", "control": ctl}) + "\n")
    b2.pass_once()
    ca = fake.posted("control_applied")
    assert len(ca) == 3 and ca[2]["data"]["refs"] == []


def test_presence_beat_carries_live_json_and_is_not_an_event(tmp_path, fake):
    run = copy_run(tmp_path)
    b = bridge(run, fake, presence=True)
    b.pass_once()
    assert len(fake.presence) == 1
    act = fake.presence[0]["activity"]
    assert act["phase"] == "done" and act["inflight"] == 0 and "checked" in act["text"]
    assert "spent" not in json.dumps(fake.presence[0])
    assert all(e["kind"] != "presence" for e in fake.posted())


def _closed_port() -> int:
    s = socket.socket()
    s.bind(("127.0.0.1", 0))
    port = s.getsockname()[1]
    s.close()
    return port


def test_outbox_when_the_server_is_down_then_flushed_once(tmp_path, fake):
    run = copy_run(tmp_path)
    down = B.Bridge(run, "http://127.0.0.1:%d" % _closed_port(), pull=True, presence=True, timeout=1.0)
    t0 = time.perf_counter()
    n = down.pass_once()
    assert time.perf_counter() - t0 < 6.0                  # one failed connect, then the pass skips the network
    box = run / B.OUTBOX_FILE
    assert n > 0 and len(box.read_text(encoding="utf-8").splitlines()) == n
    up = bridge(run, fake)
    assert up.pass_once() == 0                             # the cursor moved; the outbox is flushed
    assert len(fake.events) == n and box.read_text(encoding="utf-8") == ""
    with open(box, "w", encoding="utf-8") as f:            # a second flush of the same events adds nothing
        f.write("".join(json.dumps(e) + "\n" for e in fake.posted()[:5]))
    up.pass_once()
    assert len(fake.events) == n


def test_exit_2_when_the_loop_has_space_mode(tmp_path, fake, capsys):
    run = copy_run(tmp_path)
    (run / "space_mode.json").write_text(json.dumps({"space": fake.url, "actor": "team.loop", "step": True}),
                                         encoding="utf-8")
    assert B.main(["--run", str(run), "--space", fake.url, "--once"]) == 2
    assert "space_mode.json" in capsys.readouterr().err
    assert fake.posts == []
    assert B.main(["--run", str(run), "--space", fake.url, "--once", "--force", "--no-pull"]) == 0
    assert len(fake.posted("node_added")) == 9


def test_control_log_row_waits_while_the_queue_cannot_be_read(tmp_path, fake):
    run = tmp_path / "run"
    run.mkdir()
    seqs = post_six(fake)
    bridge(run, fake, pull=True).pass_once()
    ctl = json.loads((run / "control.json").read_text(encoding="utf-8"))
    with open(run / "control_log.jsonl", "a", encoding="utf-8") as f:
        f.write(json.dumps({"ts": "2026-10-17T19:50:00", "round": 1, "stage": "ideated", "control": ctl}) + "\n")
    # a restarted bridge while the space is down: the row must wait, not be matched to an empty queue
    down = B.Bridge(run, "http://127.0.0.1:%d" % _closed_port(), pull=True, presence=False, timeout=1.0)
    down.pass_once()
    box = run / B.OUTBOX_FILE
    assert "control_applied" not in (box.read_text(encoding="utf-8") if box.exists() else "")
    bridge(run, fake, pull=True).pass_once()
    ca = fake.posted("control_applied")
    assert len(ca) == 1 and ca[0]["data"]["refs"] == seqs


def test_mode_is_detected_again_until_the_run_names_it(tmp_path, fake):
    run = copy_run(tmp_path)
    hold = tmp_path / "hold"
    hold.mkdir()
    for name in ("state.json", "reference.json", "verify.jsonl"):     # a loop that has not reached a boundary yet
        shutil.move(str(run / name), str(hold / name))
    b = bridge(run, fake)
    b.pass_once()
    for name in ("state.json", "reference.json", "verify.jsonl"):
        shutil.move(str(hold / name), str(run / name))
    before = len(fake.posted())
    b.pass_once()
    new = fake.posted()[before:]
    se = next(e for e in new if e["kind"] == "stage_entered")
    assert se["data"]["mode"] == "check_only"
    win = next(e for e in new if e["kind"] == "test_result" and e["data"]["cand"] == "nbcd037208c")
    assert win["data"]["status"] == "win" and win["data"]["reference"] is True


def test_cut_state_json_keeps_the_last_good_state(tmp_path, fake):
    run = copy_run(tmp_path)
    b = bridge(run, fake)
    b.pass_once()
    p = run / "idea_clusters.json"
    obj = json.loads(p.read_text(encoding="utf-8"))
    obj["clusters"][0]["selected"] = not obj["clusters"][0].get("selected")
    p.write_text(json.dumps(obj), encoding="utf-8")
    s = run / "state.json"
    text = s.read_text(encoding="utf-8")
    s.write_text(text[: len(text) // 2], encoding="utf-8")         # the loop is rewriting state.json
    t = p.stat().st_mtime + 1
    os.utime(s, (t, t))
    before = len(fake.posted())
    b.pass_once()
    new = [e for e in fake.posted()[before:] if e["kind"] == "cluster_snapshot"]
    assert len(new) == 1 and new[0]["data"]["round"] == 2 and new[0]["data"]["stage"] == "deepened"


def test_a_refused_key_keeps_the_events_in_the_outbox(tmp_path):
    locked = FakeSpace(key="k1")
    try:
        run = copy_run(tmp_path)
        n = B.Bridge(run, locked.url, pull=False, presence=False).pass_once()
        box = run / B.OUTBOX_FILE
        assert n > 0 and locked.events == [] and len(box.read_text(encoding="utf-8").splitlines()) == n
        assert B.Bridge(run, locked.url, pull=False, presence=False, key="k1").pass_once() == 0
        assert len(locked.events) == n and box.read_text(encoding="utf-8") == ""
    finally:
        locked.close()


# ---------------------------------------------------------------- import at the original pace

def _pin_mtimes(run: Path, when: str = "2026-10-17T19:33:40") -> None:
    t = datetime.fromisoformat(when).timestamp()
    for p in run.rglob("*"):
        if p.is_file():
            os.utime(p, (t, t))


def _span(run: Path) -> float:
    ts = []
    for rel in ["verify.jsonl", "memory_log.jsonl"] + ["cands/" + p.name for p in (run / "cands").glob("*.jsonl")]:
        for ln in (run / rel).read_text(encoding="utf-8").splitlines():
            ts.append(datetime.fromisoformat(json.loads(ln)["ts"]).timestamp())
    ts.append(datetime.fromisoformat(json.loads((run / "next_questions.json").read_text(encoding="utf-8"))["ts"]).timestamp())
    ts.append(datetime.fromisoformat(json.loads((run / "state.json").read_text(encoding="utf-8"))["stage"]["ts"]).timestamp())
    return max(ts) - min(ts)


def _check_import(run, fake, res):
    evs = fake.posted()
    assert res["events"] == len(evs) > 0 and res["errors"] == 0
    assert all("orig_ts" in e["data"] for e in evs)
    t = [datetime.fromisoformat(e["data"]["orig_ts"]).timestamp() for e in evs]
    assert t == sorted(t)
    k = kinds(evs)
    assert k["node_added"] == 9 and k["test_result"] == 16 and k["memory_added"] == 4
    assert k["reply_posted"] == k["objection_marked"] == 180 and k["candidate_built"] == 9
    snaps = [e for e in evs if e["kind"] == "cluster_snapshot"]
    assert {e["data"]["round"] for e in snaps} == {1, 2}       # round 1 rebuilt from selection.jsonl
    assert evs[0]["kind"] == "node_added" and evs[0]["data"]["id"] == "root"
    order = [e["kind"] for e in evs]
    assert order.index("sketch_batch") < order.index("cluster_snapshot") < order.index("candidate_built")
    assert order.index("candidate_built") < order.index("test_result")
    # within round 1, a candidate is built before it is tested, and memory comes after the tests of its round
    first_tr = {e["data"]["cand"]: i for i, e in reversed(list(enumerate(evs))) if e["kind"] == "test_result"}
    for i, e in enumerate(evs):
        if e["kind"] == "candidate_built" and e["data"]["cand"] in first_tr:
            assert i < first_tr[e["data"]["cand"]]
    assert forbidden(evs) == []
    assert not (run / B.CURSOR_FILE).exists()                   # a finished folder is not written to


def test_import_fast(tmp_path, fake):
    run = copy_run(tmp_path)
    _pin_mtimes(run)
    res = B.import_run(run, fake.url, pace="fast")
    _check_import(run, fake, res)
    assert res["slept_s"] == 0.0 and res["finished"] is True
    assert fake.refused == [] and all(len(p) <= B.POST_BATCH for p in fake.posts)
    assert len(fake.posts) == len(B._chunks(fake.posted()))


def test_import_original_pace_at_speed_1000(tmp_path, fake):
    run = copy_run(tmp_path)
    _pin_mtimes(run)
    span = _span(run)
    assert 60 < span < 90
    res = B.import_run(run, fake.url, pace="original", speed=1000)
    _check_import(run, fake, res)
    assert abs(res["slept_s"] - span / 1000) < 0.002
    assert res["wall_s"] >= span / 1000 * 0.9 and res["wall_s"] < 10
    # one POST per distinct original second at least, every batch at most 100
    assert len(fake.posts) > 10 and all(len(p) <= B.POST_BATCH for p in fake.posts)


def test_import_cli_and_a_live_folder_is_tailed(tmp_path, fake):
    run = copy_run(tmp_path)
    _pin_mtimes(run)
    (run / "live.json").write_text(json.dumps({"phase": "verify", "note": "", "inflight": [{}]}), encoding="utf-8")
    stop = threading.Event()
    res = {}
    th = threading.Thread(target=lambda: res.update(B.import_run(run, fake.url, pace="fast", every=0.05, stop=stop)))
    th.start()
    deadline = time.monotonic() + 10
    while not (run / B.CURSOR_FILE).exists() and time.monotonic() < deadline:
        time.sleep(0.02)
    n0 = len(fake.posted())
    with open(run / "memory_log.jsonl", "a", encoding="utf-8") as f:
        f.write(json.dumps({"round": 3, "part": "open", "added": [], "rejected": [], "archived": [],
                            "ts": "2026-10-17T19:45:00"}) + "\n")
    while len(fake.posted()) == n0 and time.monotonic() < deadline:
        time.sleep(0.02)
    stop.set()
    th.join(5)
    assert not th.is_alive() and res["finished"] is False
    new = fake.posted()[n0:]
    assert [e["kind"] for e in new] == ["memory_added"] and "orig_ts" not in new[0]["data"]
    fake2 = FakeSpace()
    try:
        run2 = copy_run(tmp_path, "done")
        assert B.main(["--import", str(run2), "--space", fake2.url, "--pace", "original", "--speed", "1000"]) == 0
        assert len(fake2.posted("test_result")) == 16
    finally:
        fake2.close()


# ---------------------------------------------------------------- the real mock run (read only)

@pytest.mark.skipif(not REAL_RUN.is_dir(), reason="the mock run folder is absent")
def test_warm_full_pass_over_the_real_mock_run(tmp_path, fake):
    def full_pass():
        b = B.Bridge(REAL_RUN, fake.url, cursor_path=tmp_path / "c.json", outbox_path=tmp_path / "o.ndjson",
                     control_path=tmp_path / "control.json", pull=False, presence=False, fresh=True, persist=False)
        t0 = time.perf_counter()
        n = b.pass_once()
        return n, time.perf_counter() - t0
    n1, _ = full_pass()                                   # cold: fills the OS file cache
    n2, dt = full_pass()                                  # warm: the same full pass again
    assert n1 == n2 > 500
    assert dt < 0.300, f"warm full pass took {dt * 1000:.0f} ms"
    assert forbidden(fake.posted()) == []
    assert not (REAL_RUN / B.CURSOR_FILE).exists() and not (REAL_RUN / B.OUTBOX_FILE).exists()
