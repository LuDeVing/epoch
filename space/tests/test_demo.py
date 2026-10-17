"""The demo kit (docs/MULTIPLAYER_DESIGN.md sections 13 and 16.8; space/demo.py).

Every test runs under tmp_path (HTSA_LAB_ROOT), talks only to 127.0.0.1 and never calls a model. The recorded
round in space/recorded/ comes from `python -m space.demo --rehearse`; these tests read it back. The full rehearsal
is a mock dry run, so it runs here only with HTSA_SLOW_REHEARSE=1 (one dry run at a time, section 12.5).
"""
from __future__ import annotations

import importlib.util
import json
import os
import re
import socket
import subprocess
import sys
import time
from pathlib import Path

import pytest

from space import contract as C
from space import demo as D
from space import server as S

REPO = Path(__file__).resolve().parents[2]
LOG = D.RECORDED / D.LOG_NAME
HASH = D.RECORDED / D.HASH_NAME
BEATS = D.RECORDED / D.BEATS_NAME
DESIGN = (REPO / "docs" / "MULTIPLAYER_DESIGN.md").read_text(encoding="utf-8")


def _docs_check():
    spec = importlib.util.spec_from_file_location("check_space_docs", REPO / "docs" / "check_space_docs.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def free_port() -> int:
    s = socket.socket()
    s.bind(("127.0.0.1", 0))
    port = s.getsockname()[1]
    s.close()
    return port


def flat(text: str) -> str:
    return re.sub(r"\s+", " ", text)


@pytest.fixture
def lab(tmp_path, monkeypatch):
    root = tmp_path / "lab"
    root.mkdir()
    monkeypatch.setenv("HTSA_LAB_ROOT", str(root).replace("\\", "/"))
    monkeypatch.setenv("HTSA_BACKEND", "mock")
    return root


@pytest.fixture(scope="module")
def recorded():
    assert LOG.exists() and HASH.exists() and BEATS.exists(), "run python -m space.demo --rehearse first"
    return D.read_ndjson(LOG)


@pytest.fixture(scope="module")
def reduced():
    return D.node_reduce(LOG)


# ---------------------------------------------------------------- the runbook and the script
def test_the_runbook_names_every_beat_with_a_time():
    chk = _docs_check()
    beats = chk.design_beats(DESIGN)
    assert len(beats) == 15
    runbook = (REPO / "docs" / "DEMO_RUNBOOK.md").read_text(encoding="utf-8")
    assert chk.check_runbook(runbook, beats) == []


def test_the_script_matches_section_13_3():
    chk = _docs_check()
    beats = chk.design_beats(DESIGN)
    assert [t for t, _ in beats] == [b["t"] for b in D.SCRIPT]
    for (t, does), row in zip(beats, D.SCRIPT):
        for tok in chk.beat_tokens(does):
            assert tok in row["do"], (t, tok)


def test_the_stage_command_lines_are_those_of_section_13_1():
    sec = flat(DESIGN.split("### 13.1 Setup")[1].split("### 13.2")[0])
    loop = " ".join(["python"] + D.loop_argv("stage-<HHMM>", py="python")[1:])
    assert loop in sec
    srv = D.server_argv("stage-<HHMM>", lab="D:/AGI-lab", py="python")
    assert " ".join(srv[3:]) in sec                       # --db ... --memory-dir ...
    assert srv[1:3] == ["-m", "space.server"]
    for me in D.PEOPLE:
        a = D.agent_argv(me, "stage-0930", py="python")
        assert a[1:5] == ["-m", "space.agent", "--me", me] and "--model" in a and a[a.index("--model") + 1] == "mock"
        live = D.agent_argv(me, "stage-0930", live=True, py="python")
        assert " ".join(live[live.index("--model"):live.index("--model") + 4]) == "--model sonnet --fallback mock"
        assert f"--me {me}" in sec
    assert "--model sonnet --fallback mock" in sec and "--live-agents" in sec
    b = dict(D.browser_argv("http://127.0.0.1:8766", "D:/AGI-lab/spaces/stage-0930"))
    assert b["chrome.ana"][-1].endswith("?me=ana") and b["edge.ben"][-1].endswith("?me=ben")
    assert any(x.startswith("--user-data-dir=") for x in b["projector"])
    assert b["projector"][-1].endswith("?stage=1&follow=ana") and b["projector"][-1].startswith("--app=")
    assert "?me=ana" in sec and "?me=ben" in sec and "?stage=1&follow=ana" in sec and "--user-data-dir" in sec


def test_the_rows_of_13_5_are_all_in_the_table():
    want = {"post_200ms", "ack_2s", "peer_2s", "applied_item_order", "sketch_item_order", "digests_both",
            "preview_before_pick", "overwrote", "win_and_won", "voters_hit_or_miss", "vetoed_in_pick", "drill_restart",
            "beats_in_order", "time_limit", "no_claude", "free_memory", "no_child_left"}
    assert set(D.ROW_NAMES) == want and len(D.ROW_NAMES) == len(want)


# ---------------------------------------------------------------- the recording
def test_the_recorded_log_contains_no_private_key(recorded):
    assert D.private_hits(recorded) == []
    raw = LOG.read_text(encoding="utf-8")
    for key in ("obvious", "obvious_match", "private"):
        assert f'"{key}":' not in raw
        assert not re.search(r"\b%s\b" % key, raw), key


def test_the_recorded_log_is_one_contiguous_run(recorded):
    assert [e["seq"] for e in recorded] == list(range(1, len(recorded) + 1))
    assert recorded[0]["kind"] == "space_opened"
    assert all(e["kind"] in C.KINDS for e in recorded)


def test_the_recorded_log_passes_every_log_row_of_13_5(recorded, reduced):
    rows = D.check_log(recorded, reduced)
    bad = {k: v for k, v in rows.items() if not v[0]}
    assert not bad, bad
    assert set(D.LOG_ROWS) <= set(rows)


def test_the_rehearsal_that_made_the_recording_passed_every_row(recorded):
    doc = json.loads(BEATS.read_text(encoding="utf-8"))
    assert set(doc["rows"]) == set(D.ROW_NAMES)
    assert all(r["ok"] for r in doc["rows"].values()), {k: v for k, v in doc["rows"].items() if not v["ok"]}
    assert doc["elapsed_s"] <= D.TIME_LIMIT_S
    assert doc["drill"] is True
    assert doc["beats"] == D.find_beats(recorded)
    for k in ("q1", "q2", "q3", "vote_ben", "vote_ana", "reply_idea", "item_order_seq"):
        assert doc["ids"].get(k), k


def test_the_hash_file_comes_from_the_node_reducer(recorded, reduced):
    h = json.loads(HASH.read_text(encoding="utf-8"))
    assert h["layout_hash"] == reduced["layout_hash"] and h["state_hash"] == reduced["state_hash"]
    assert h["events"] == len(recorded) and h["head"] == recorded[-1]["seq"]


def test_check_log_catches_a_missing_ack_a_missing_vote_and_a_late_peer_line(recorded):
    no_ack = [e for e in recorded if not (e["kind"] == "agent_said" and e["data"].get("kind") == "ack")]
    assert D.check_log(no_ack)["ack_2s"][0] is False
    first = next(e for e in recorded if e["kind"] == "node_added" and e["data"].get("id") == "item_order")
    late = []
    for e in recorded:
        if e["kind"] == "agent_said" and e["by"] == "ben.agent" and e["data"].get("kind") == "peer" and e["seq"] > first["seq"]:
            e = dict(e, ts="2099-01-01T00:00:00.000Z")
        late.append(e)
    assert D.check_log(late)["peer_2s"][0] is False
    no_votes = [e for e in recorded if e["kind"] != "vote_cast"]
    rows = D.check_log(no_votes)
    assert rows["voters_hit_or_miss"][0] is False and rows["beats_in_order"][0] is False


# ---------------------------------------------------------------- --replay
def test_replay_at_speed_50_reaches_the_same_beat_seqs_in_order(lab, recorded):
    assert D.run_replay(speed=50, seek=0, port=0, exit_when_done=True, say=lambda *_: None) == 0


def test_replay_with_seek_at_a_beat_reaches_the_same_beat_seqs(lab, recorded):
    seek = next(b["seq"] for b in D.find_beats(recorded) if b["beat"] == "votes")
    lines = []
    assert D.run_replay(speed=50, seek=seek, port=0, exit_when_done=True, say=lines.append) == 0
    assert any("beat seqs match the recording" in x for x in lines)


def test_replay_cli_without_a_log_says_so(lab, tmp_path):
    lines = []
    assert D.run_replay(file=str(tmp_path / "none.ndjson"), port=0, exit_when_done=True, say=lines.append) == 2
    assert "no recorded log" in lines[0]


# ---------------------------------------------------------------- --check
def test_check_exits_0_on_this_pc(lab, capsys):
    """Every check passes on this PC. The free-memory gate depends on what else runs at that moment: with less
    than 3 GB free --check must exit 1 with memory as its only failure (the gate doing its job)."""
    rc = D.run_check(free_port())
    out = capsys.readouterr().out
    failed = re.search(r"check: FAILED: (.*)", out)
    if D.memory_gate(D.free_memory_gb())[0]:
        assert rc == 0, out
    else:
        assert rc == 1 and failed and failed.group(1).strip() == "memory", out
    for name in ("port", "vendor", "chrome", "edge", "spaces", "recorded", "private", "replay test"):
        assert re.search(r"^%s\s+ok\b" % re.escape(name), out, re.M), (name, out)
    assert "netsh advfirewall firewall add rule" in out
    assert (lab / "spaces").is_dir()


def test_check_fails_when_the_port_is_taken(lab, capsys):
    s = socket.socket()
    s.bind(("127.0.0.1", 0))
    s.listen(1)
    try:
        assert D.run_check(s.getsockname()[1]) == 1
        assert re.search(r"port\s+FAIL", capsys.readouterr().out)
    finally:
        s.close()


def test_the_memory_gate():
    assert D.memory_gate(2.9)[0] is False and "3 GB needed" in D.memory_gate(2.9)[1]
    assert D.memory_gate(3.5)[0] is True
    assert D.memory_gate(None)[0] is True
    if os.name == "nt":
        g = D.free_memory_gb()
        assert isinstance(g, float) and 0 < g < 1024


# ---------------------------------------------------------------- processes
def test_procs_start_log_and_kill_the_whole_tree(tmp_path, lab):
    p = D.Procs(tmp_path / "logs", D.child_env())
    child = p.start("sleeper", [sys.executable, "-c",
                                "import subprocess, sys, time; subprocess.Popen([sys.executable, '-c', 'import time; time.sleep(60)']); "
                                "print('up', flush=True); time.sleep(60)"])
    end = time.monotonic() + 10
    while time.monotonic() < end and "up" not in (tmp_path / "logs" / "sleeper.log").read_text(encoding="utf-8"):
        time.sleep(0.1)
    if os.name == "nt":
        kids = D.descendants(os.getpid())
        assert child.pid in [k for k, _ in kids]
        assert not any(D.is_claude(e) for _, e in kids)
    p.stop_all()
    assert child.poll() is not None
    if os.name == "nt":
        time.sleep(0.5)
        assert [k for k in D.descendants(os.getpid()) if not k[1].lower().startswith("conhost")] == []
    assert (tmp_path / "logs" / "sleeper.log").read_text(encoding="utf-8").startswith("$ ")


def test_port_free():
    s = socket.socket()
    s.bind(("127.0.0.1", 0))
    s.listen(1)
    try:
        assert D.port_free(s.getsockname()[1]) is False
    finally:
        s.close()
    assert D.port_free(free_port()) is True


# ---------------------------------------------------------------- the Go hotkey and the Replay seek
@pytest.fixture
def srv(tmp_path, lab):
    run = S.make(str(tmp_path / "spaces" / "t" / "space.db"), port=0, reap_s=0.2, ping_s=0.5).start()
    yield run
    run.stop()


def test_go_posts_run_step_only_for_the_boundary_the_loop_waits_at(srv):
    api = D.Api(srv.url)
    assert D.go_now(api) is None                            # no stage_entered yet: nothing is posted
    loop = {"kind": "stage_entered", "subject": "run:main", "data": {"round": 1, "stage": "planned", "waiting": True,
                                                                      "step_mode": True}}
    assert api.call("POST", "/api/events", loop, actor="team.loop", kind="system")[0] == 200
    r = D.go_now(api)
    assert r["status"] == 200 and (r["round"], r["stage"]) == (1, "planned")
    ev = api.all_events()[-1]
    assert ev["kind"] == "run_step" and ev["by"] == "ben" and ev["by_kind"] == "human"
    assert ev["data"] == {"round": 1, "stage": "planned"}
    moving = dict(loop, data={"round": 1, "stage": "ideated", "waiting": False, "step_mode": True})
    api.call("POST", "/api/events", moving, actor="team.loop", kind="system")
    assert D.go_now(api) is None                            # not waiting: no Go


def test_the_replay_hotkey_seeks_to_the_last_beat_the_live_run_reached(recorded):
    beats = D.find_beats(recorded)
    by = {b["beat"]: b["seq"] for b in beats}
    upto = [e for e in recorded if e["seq"] <= by["go_ideated_1"]]
    assert D.current_beat_seq(upto, beats) == by["go_ideated_1"]
    assert D.current_beat_seq([], beats) == 0


def test_the_cli_refuses_a_model_in_the_rehearsal_and_a_drill_on_stage():
    with pytest.raises(SystemExit):
        D.main(["--rehearse", "--live-agents"])
    with pytest.raises(SystemExit):
        D.main(["--stage", "--drill", "restart"])
    with pytest.raises(SystemExit):
        D.main([])


# ---------------------------------------------------------------- the full rehearsal (one mock dry run, opt-in)
@pytest.mark.skipif(os.environ.get("HTSA_SLOW_REHEARSE") != "1",
                    reason="the full rehearsal is a mock dry run: set HTSA_SLOW_REHEARSE=1 and run it alone")
def test_rehearse_exits_0_within_5_minutes_with_every_row(tmp_path, lab):
    out = tmp_path / "recorded"
    env = dict(os.environ, HTSA_LAB_ROOT=str(lab).replace("\\", "/"))
    t = time.monotonic()
    r = subprocess.run([sys.executable, "-m", "space.demo", "--rehearse", "--port", str(free_port()), "--out", str(out)],
                       cwd=str(REPO), env=env, capture_output=True, text=True, timeout=420)
    assert r.returncode == 0, r.stdout[-4000:] + r.stderr[-2000:]
    assert time.monotonic() - t < 330
    doc = json.loads((out / D.BEATS_NAME).read_text(encoding="utf-8"))
    assert set(doc["rows"]) == set(D.ROW_NAMES) and all(v["ok"] for v in doc["rows"].values())
    for name in D.ROW_NAMES:
        assert re.search(r"^%s\s+ok\b" % name, r.stdout, re.M), name
