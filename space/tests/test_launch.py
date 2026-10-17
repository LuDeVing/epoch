"""Start a research from the page (part P8, start-run; space/launch.py and space/web/start.js).

Every test runs under tmp_path (HTSA_LAB_ROOT and the space db), talks only to 127.0.0.1 and never calls a model.
One test runs ONE mock dry run (small preset, implement 1, max sketch calls 4, binpack_nobase: nothing trains).
"""
from __future__ import annotations

import http.client
import json
import subprocess
import sys
import time
from pathlib import Path

import pytest

from space import launch as LA
from space import server as S

PY = LA.PYTHON
WEB = Path(__file__).resolve().parent.parent / "web"


def call(port, method, path, body=None, timeout=30):
    conn = http.client.HTTPConnection("127.0.0.1", port, timeout=timeout)
    try:
        data = None if body is None else json.dumps(body).encode("utf-8")
        hdr = {"Content-Type": "application/json", "X-Space-Actor": "ana", "X-Space-Kind": "human"} if body is not None else {}
        conn.request(method, path, body=data, headers=hdr)
        r = conn.getresponse()
        raw = r.read()
        ctype = r.getheader("Content-Type") or ""
        return r.status, (json.loads(raw.decode("utf-8")) if ctype.startswith("application/json") else raw.decode("utf-8"))
    finally:
        conn.close()


@pytest.fixture
def lab(tmp_path, monkeypatch):
    root = tmp_path / "lab"
    root.mkdir()
    monkeypatch.setenv("HTSA_LAB_ROOT", str(root))
    monkeypatch.setenv("HTSA_BACKEND", "mock")
    return root


@pytest.fixture
def srv(tmp_path, lab):
    run = S.make(str(tmp_path / "spaces" / "demo" / "space.db"), port=0, reap_s=0.1, ping_s=0.3).start()
    yield run
    run.stop()


@pytest.fixture
def no_spawn(monkeypatch):
    """Any spawn or kill in a test that must not start a process fails the test."""
    def boom(*a, **k):
        raise AssertionError("no process may start here")
    monkeypatch.setattr(LA.subprocess, "Popen", boom)
    monkeypatch.setattr(LA, "kill_tree", boom)


# ---------------------------------------------------------------- presets, commands, estimate
def test_presets_are_the_brief():
    assert LA.PRESETS == {
        "small": {"rounds": 1, "implement": 2, "max_sketch_calls": 8, "budget": 600000},
        "medium": {"rounds": 2, "implement": 4, "max_sketch_calls": 16, "budget": 2000000},
        "big": {"rounds": 3, "implement": 10, "max_sketch_calls": None, "budget": 5000000},
    }
    assert PY == r"D:\AGI-lab\.venv\Scripts\python.exe"


def test_presets_map_to_the_exact_commands():
    url = "http://127.0.0.1:8766"
    mock = lambda i, r, s: [PY, "-m", "nano.dry_run", "--profile", "binpack_nobase", "--batch", "b1", "--implement", i,  # noqa: E731
                            "--rounds", r, "--max-sketch-calls", s, "--space", url]
    assert LA.command("small", "binpack_nobase", "mock", "b1", url) == mock("2", "1", "8")
    assert LA.command("medium", "binpack_nobase", "mock", "b1", url) == mock("4", "2", "16")
    assert LA.command("big", "binpack_nobase", "mock", "b1", url) == mock("10", "3", "22")
    real = "-m nano.loop --profile llm --batch b2 --implement".split()
    assert LA.command("small", "llm", "real", "b2", url) == [PY] + real + [
        "2", "--rounds", "1", "--max-sketch-calls", "8", "--budget", "600000", "--space", url]
    assert LA.command("medium", "llm", "real", "b2", url) == [PY] + real + [
        "4", "--rounds", "2", "--max-sketch-calls", "16", "--budget", "2000000", "--space", url]
    assert LA.command("big", "llm", "real", "b2", url) == [PY] + real + [
        "10", "--rounds", "3", "--budget", "5000000", "--space", url]          # no sketch cap
    assert LA.command("small", "binpack_nobase", "mock", "b1", url, {"implement": 1, "max_sketch_calls": 4}) == mock("1", "1", "4")
    with pytest.raises(S.Reject):
        LA.command("huge", "llm", "mock", "b", url)
    with pytest.raises(S.Reject):
        LA.command("small", "llm", "fast", "b", url)


def test_estimate_numbers_for_small():
    e = LA.estimate("small", "binpack_nobase")
    # 8 sketches, min(6, 8) = 6 chains, 2 builds: calls 2 + 8 + 18 + 4; tokens 8*65k + 6*40k + 2*35k = 830k, capped
    assert (e["sketches"], e["chains"], e["builds"], e["rounds"]) == (8, 6, 2, 1)
    assert e["calls"] == 32
    assert e["tokens_uncapped"] == 830000 and e["tokens"] == 600000 and e["capped"] is True
    assert e["minutes"] == 13                                   # 32 calls * 2.5 min / 6 in parallel
    big = LA.estimate("big")
    assert big["sketches"] == 22 and big["tokens"] == 5000000
    words = LA.estimate_words(e)
    assert "32 model calls" in words and "600,000 Fable tokens" in words and "13 minutes" in words
    assert words.isascii()


def test_profiles_list_the_folder_with_goal_short():
    ps = {p["name"]: p for p in LA.profiles()}
    assert {"llm", "binpack", "binpack_nobase", "review_process"} <= set(ps)
    assert ps["binpack_nobase"]["goal_short"].startswith("writing a packing rule")
    assert "validation loss" in ps["llm"]["goal_short"] and "GPU" in ps["llm"]["note"]


def test_space_name_and_paths(lab):
    assert LA.space_name("D:/AGI-lab/spaces/demo/space.db") == "demo"
    assert LA.space_name("C:/tmp/x.db") == "x"
    la = LA.Launcher("D:/AGI-lab/spaces/demo/space.db", "http://127.0.0.1:1")
    assert la.runs_dir == lab / "spaces" / "demo" / "runs"


# ---------------------------------------------------------------- the routes without a process
def test_routes_profiles_and_estimate(srv, no_spawn):
    st, b = call(srv.port, "GET", "/api/run/profiles")
    assert st == 200 and b["default_profile"] == "binpack_nobase" and b["order"] == ["small", "medium", "big"]
    assert b["presets"]["small"]["estimate"]["calls"] == 32 and "32 model calls" in b["presets"]["small"]["words"]
    st, b = call(srv.port, "GET", "/api/run/estimate?preset=medium&profile=llm")
    assert st == 200 and b["preset"] == "medium" and b["profile"] == "llm" and b["words"]
    st, b = call(srv.port, "GET", "/api/run/estimate?preset=huge")
    assert st == 422 and b["error"] == "bad_preset"
    st, b = call(srv.port, "GET", "/api/run/status")
    assert st == 200 and b == {"runs": [], "alive": False}


def test_real_start_without_confirm_gives_400(srv, lab, no_spawn):
    for body in ({"preset": "small", "profile": "llm", "mode": "real"},
                 {"preset": "small", "profile": "llm", "mode": "real", "confirm": "yes"},
                 {"preset": "small", "profile": "llm", "mode": "real", "confirm": 1}):
        st, b = call(srv.port, "POST", "/api/run/start", body)
        assert st == 400 and b["error"] == "confirm_needed"
        assert b["estimate"]["calls"] == 32 and b["estimate"]["tokens"] == 600000
        assert "32 model calls" in b["words"]
    st, b = call(srv.port, "POST", "/api/run/start", {"preset": "small", "profile": "nope", "mode": "mock"})
    assert st == 422 and b["error"] == "bad_profile"
    st, b = call(srv.port, "POST", "/api/run/start", {"preset": "small", "profile": "llm", "mode": "fast"})
    assert st == 422 and b["error"] == "bad_mode"
    assert not (lab / "spaces" / "demo" / "runs" / "runs.json").exists()
    st, b = call(srv.port, "GET", "/api/events?since=0")
    assert [e["kind"] for e in b["events"]] == ["space_opened"]          # no run_started written


def test_stop_on_a_dead_pid_is_harmless(lab, srv, monkeypatch):
    p = subprocess.Popen([sys.executable, "-c", "pass"])
    p.wait()
    la = srv.httpd.launcher
    la._save([{"batch": "old", "pid": p.pid, "created": 1, "preset": "small", "profile": "binpack_nobase",
               "mode": "mock", "cmd": [], "started": "2026-10-17T00:00:00", "log": str(lab / "none.log"),
               "run_dir": None, "rc": None, "finished": None, "stopped": False}])
    real_kill = LA.kill_tree
    kills = []
    monkeypatch.setattr(LA, "kill_tree", lambda pid: kills.append(pid) or True)
    st, b = call(srv.port, "POST", "/api/run/stop", {"batch": "old"})
    assert st == 200 and b == {"ok": True, "batch": "old", "was_alive": False, "killed": False}
    assert kills == []                                          # a dead (or reused) pid is never signalled
    st, b = call(srv.port, "GET", "/api/run/status")
    assert st == 200 and b["alive"] is False
    r = b["runs"][0]
    assert r["alive"] is False and r["state"] == "failed" and r["rc"] is None and r["finished"] and r["tail"] == []
    st, b = call(srv.port, "POST", "/api/run/stop", {"batch": "nope"})
    assert st == 404 and b["error"] == "no_run"
    assert real_kill(0) is False and real_kill(None) is False and real_kill("x") is False
    assert LA.pid_alive(0) is False and LA.pid_alive(None) is False
    assert LA.pid_alive(p.pid, created=1) is False
    st, b = call(srv.port, "GET", "/api/events?since=0")
    fin = [e for e in b["events"] if e["data"].get("event") == "run_finished"]
    assert len(fin) == 1 and fin[0]["by"] == "server" and fin[0]["subject"] == "run:old"


def test_pid_alive_sees_this_process():
    import os
    assert LA.pid_alive(os.getpid()) is True
    created = LA.proc_created(os.getpid())
    assert LA.pid_alive(os.getpid(), created) is True
    if created is not None:
        assert LA.pid_alive(os.getpid(), created + 1) is False      # a reused pid counts as dead


def test_tail_keeps_the_last_lines(tmp_path):
    f = tmp_path / "x.log"
    f.write_text("".join("line %d\n" % i for i in range(100)), encoding="utf-8")
    assert LA.tail(f) == ["line %d" % i for i in range(80, 100)]
    assert LA.tail(tmp_path / "missing.log") == [] and LA.tail(None) == []


# ---------------------------------------------------------------- the page
def test_page_has_the_button_and_the_module(srv):
    st, page = call(srv.port, "GET", "/")
    assert st == 200 and 'id="start-run"' in page and 'href="start.css"' in page
    st, js = call(srv.port, "GET", "/start.js")
    assert st == 200 and "Start a research" in js and "/api/run/status" in js and "export function mountStart" in js
    app = (WEB / "app.js").read_text(encoding="utf-8")
    assert "import { mountStart } from './start.js';" in app and "mountStart(document.getElementById('start-run'), viewApi);" in app


def test_page_files_are_ascii_and_use_tokens_only():
    import re
    hexre = re.compile(r"(?<![\w&])#(?:[0-9a-fA-F]{8}|[0-9a-fA-F]{6}|[0-9a-fA-F]{3,4})\b")
    for name in ("start.js", "start.css"):
        text = (WEB / name).read_text(encoding="utf-8")
        assert text.isascii(), name
        assert not hexre.search(text), name
        assert not re.search(r"\brgba?\(|\bhsla?\(", text), name
        assert "http://" not in text and "https://" not in text, name
    for p in (Path(LA.__file__), Path(__file__)):
        assert p.read_text(encoding="utf-8").isascii()


# ---------------------------------------------------------------- the one mock dry run
def test_mock_start_small_runs_to_rc_0(srv, lab):
    la = srv.httpd.launcher
    la.overrides = {"implement": 1, "max_sketch_calls": 4}           # the smallest run the loop allows
    st, b = call(srv.port, "POST", "/api/run/start", {"preset": "small", "profile": "binpack_nobase", "mode": "mock"})
    assert st == 200, b
    batch = b["batch"]
    assert b["cmd"] == [PY, "-m", "nano.dry_run", "--profile", "binpack_nobase", "--batch", batch, "--implement", "1",
                        "--rounds", "1", "--max-sketch-calls", "4", "--space", srv.url]
    assert b["log"] == str(lab / "spaces" / "demo" / "runs" / (batch + ".log"))
    rows = json.loads((lab / "spaces" / "demo" / "runs" / "runs.json").read_text(encoding="utf-8"))
    assert [r["batch"] for r in rows] == [batch]
    assert {"batch", "pid", "preset", "profile", "mode", "cmd", "started", "log", "run_dir"} <= set(rows[0])
    st, s = call(srv.port, "GET", "/api/run/status")
    assert st == 200 and s["alive"] is True and s["runs"][0]["alive"] is True and s["runs"][0]["state"] == "running"
    st, b2 = call(srv.port, "POST", "/api/run/start", {"preset": "small", "profile": "binpack_nobase", "mode": "mock"})
    assert st == 409 and b2["error"] == "run_alive" and b2["batch"] == batch          # one run at a time
    end = time.monotonic() + 420
    while time.monotonic() < end:
        st, s = call(srv.port, "GET", "/api/run/status")
        if not s["runs"][0]["alive"] and s["runs"][0]["finished"]:
            break
        time.sleep(1.0)
    r = s["runs"][0]
    assert r["alive"] is False, "the mock run did not finish in 7 minutes"
    assert r["rc"] == 0 and r["state"] == "finished", r["tail"]
    assert r["run_dir"] and Path(r["run_dir"]).is_dir() and Path(r["run_dir"]).name.startswith(batch + "__")
    assert r["tail"] and len(r["tail"]) <= 20
    st, ev = call(srv.port, "GET", "/api/events?since=0&limit=2000")
    kinds = [e["kind"] for e in ev["events"]]
    marks = [e["data"].get("event") for e in ev["events"] if e["by"] == "server" and e["kind"] == "note_posted"]
    assert marks == ["run_started", "run_finished"]
    fin = [e for e in ev["events"] if e["data"].get("event") == "run_finished"][0]
    assert fin["data"]["rc"] == 0 and fin["data"]["state"] == "finished"
    assert "stage_entered" in kinds                                  # the loop posted to this space
