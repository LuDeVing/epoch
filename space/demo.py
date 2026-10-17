"""The demo kit (docs/MULTIPLAYER_DESIGN.md section 13; runbook in docs/DEMO_RUNBOOK.md).

    python -m space.demo --check                      the pre-stage checks; exits non-zero when one fails
    python -m space.demo --stage [--live-agents]      server, two person-agents, the loop in step mode, three windows,
                                                      then a console with the Go, Replay and restart hotkeys
    python -m space.demo --rehearse [--drill restart|none] [--pace 1.0]
                                                      the same processes without browsers; drives the script of 13.3
                                                      through the agents' chat, asserts every row of 13.5, saves
                                                      space/recorded/stage_round.ndjson, .hash.json and .beats.json
    python -m space.demo --replay --speed N --seek SEQ [--exit-when-done]
                                                      a fresh server on the recorded log; prints each beat as it lands

Load rules (section 12.5): CPU only, mock backend, one loop process, two agents on --model mock (Sonnet with
--fallback mock only with --live-agents on --stage), no browser during --rehearse, a 3 GB free-memory gate
(GlobalMemoryStatusEx) before --check, --stage and --rehearse, logs per process under
<lab>/spaces/<space>/logs/, and every child process tree ended with taskkill /T /F on exit.
Standard library only.
"""
from __future__ import annotations

import argparse
import atexit
import datetime
import json
import os
import re
import shutil
import socket
import subprocess
import sys
import threading
import time
import urllib.error
import urllib.request
from pathlib import Path

from space import contract as C
from harness import labroot as _labroot  # noqa: E402  (the lab folder, on any computer)

REPO = Path(__file__).resolve().parent.parent
HERE = REPO / "space"
WEB = HERE / "web"
RECORDED = HERE / "recorded"
LOG_NAME, HASH_NAME, BEATS_NAME = "stage_round.ndjson", "stage_round.hash.json", "stage_round.beats.json"
HASH_MJS = WEB / "tests" / "replay" / "hash.mjs"
REPLAY_TESTS = WEB / "tests" / "replay"
MIN_FREE_GB = 3.0
TIME_LIMIT_S = 300.0
POST_MS, ACK_S, PEER_S = 200.0, 2.0, 2.0
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
EDGE = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
NODE_FALLBACK = r"C:\Program Files\nodejs\node.exe"
PROFILE = "binpack_nobase"
PEOPLE = ("ana", "ben")
GO_AS = "ben"                       # the console Go hotkey and the rehearsal's Go press act as Ben (13.3)
POSITIVE, NEGATIVE = {"win", "preferred"}, {"loss", "not_preferred", "failed_check"}
NETSH = ('netsh advfirewall firewall add rule name="HTSA space {port}" dir=in action=allow protocol=TCP '
         'localport={port} profile=private')

# ---------------------------------------------------------------- the run of show (section 13.3)
# t: the scripted time; who; do: what the person does (a slash command or a Go); say: the line to say.
SCRIPT = [
    {"t": "0:00", "who": "Ana", "do": "stands", "beat": "open",
     "say": "HTSA is a team of AI researchers. Two of us steer one run, each through our own agent. People steer, tests decide."},
    {"t": "0:15", "who": "Ana", "do": '/branch root "item order": how items are sorted before packing --claim', "beat": "branch",
     "say": "Ben's agent already knows. No lock, no refresh, and the claim says who works there."},
    {"t": "0:35", "who": "Ben", "do": "/note check tie-breaking before the choice rule", "beat": "note",
     "say": "Everything a person does is queued first. The screen says so."},
    {"t": "0:50", "who": "Ben", "do": "Go (planned r1)", "beat": "go_planned_1",
     "say": "That is the other agent being told what changed. The text on the screen is the text the agent saw."},
    {"t": "1:15", "who": "Ben", "do": "Go (ideated r1)", "beat": "go_ideated_1",
     "say": "Same picture on every screen, so we can point at a bubble and mean the same thing."},
    {"t": "1:30", "who": "Ben, Ana", "do": "/vote up <cluster A>, /vote up <cluster B>", "beat": "votes",
     "say": "Votes are shown by name. They do not decide anything. Tests do."},
    {"t": "1:45", "who": "Ben", "do": "Go (clustered r1)", "beat": "go_clustered_1",
     "say": "The critics argue with the authors. Nothing is dropped."},
    {"t": "2:05", "who": "Ana", "do": "/reply <cluster> 2 rebut: the quick check at seed 0 gave bins ratio 0.91 measured",
     "beat": "reply", "say": "People argue with evidence tags. A reply never skips a test."},
    {"t": "2:20", "who": "Ben", "do": "Go (deepened r1), then Go (built r1)", "beat": "go_built_1",
     "say": "Real rounds take minutes to hours. This run uses the mock backend with the real scoring code, so the "
            "numbers are real checks on mock code."},
    {"t": "2:55", "who": "", "do": "results land", "beat": "win",
     "say": "People steer. Tests decide. The vote is scored against the test, by name."},
    {"t": "3:10", "who": "", "do": "the verified boundary posts the preview", "beat": "preview", "say": ""},
    {"t": "3:15", "who": "Ben", "do": "/veto <Q1>", "beat": "veto", "say": ""},
    {"t": "3:25", "who": "Ana, then Ben", "do": "/choose <Q2>, /choose <Q3>", "beat": "choose",
     "say": "Last writer wins, and nobody loses silently."},
    {"t": "3:40", "who": "Ben", "do": "Go (verified r1)", "beat": "pick", "say": ""},
    {"t": "3:50", "who": "Ana", "do": "close", "beat": "close",
     "say": "Two people, two agents, one shared run. Every change is shown, named, delivered to the other agent at a "
            "safe point and receipted. The limits: real rounds are slow, so this run was the mock backend, and the "
            "person-agents answered on the canned path."},
]
REPLY_TEXT = "the quick check at seed 0 gave bins ratio 0.91 measured"
DRILL_AT = "3:30"

# The rows of section 13.5, in print order. "log" rows are read back from the log (also from the recording);
# "live" rows are measured while the rehearsal runs.
ROWS = [
    ("post_200ms", "live", "a seq returns within 200 ms of every human POST"),
    ("ack_2s", "log", "an ack within 2 s of each chat"),
    ("peer_2s", "log", "Ben's agent's peer line within 2 s of Ana's node_added"),
    ("applied_item_order", "log", "control_applied for item_order at planned r1, by on the node"),
    ("sketch_item_order", "log", "sketch_batch with node item_order in round 1"),
    ("digests_both", "log", "digest_taken by both agents after every boundary"),
    ("preview_before_pick", "log", "a question_preview before the round 2 pick"),
    ("overwrote", "log", "question_chosen carrying overwrote after the double choose"),
    ("win_and_won", "log", "a test_result with status win and one cluster marked won"),
    ("voters_hit_or_miss", "log", "hit or miss derived for both voters"),
    ("vetoed_in_pick", "log", "the vetoed id in question_picked.vetoed of round 2"),
    ("drill_restart", "live", "kill and restart: contiguous readers, claim_expired restart, outboxes flushed"),
    ("beats_in_order", "log", "every beat of the script is in the log, in order"),
    ("time_limit", "live", "the whole run under 5 minutes"),
    ("no_claude", "live", "no claude process started"),
    ("free_memory", "live", "at least 3 GB free at start"),
    ("no_child_left", "live", "no child process left after the stop"),
]
ROW_NAMES = [r[0] for r in ROWS]
LOG_ROWS = [r[0] for r in ROWS if r[1] == "log"]


def secs(t: str) -> float:
    m, s = t.split(":")
    return int(m) * 60 + int(s)


def _say(msg: str = "") -> None:
    print(msg, flush=True)


# ---------------------------------------------------------------- paths and environment
def lab_root() -> str:
    return str(_labroot.lab_root()).replace("\\", "/").rstrip("/")


def python_exe() -> str:
    return sys.executable


def node_exe() -> str | None:
    return shutil.which("node") or (NODE_FALLBACK if os.path.exists(NODE_FALLBACK) else None)


def child_env(mock_backend: bool = True) -> dict:
    env = dict(os.environ, HTSA_LAB_ROOT=lab_root(), PYTHONUNBUFFERED="1", PYTHONIOENCODING="utf-8")
    if mock_backend:
        env["HTSA_BACKEND"] = "mock"
    else:
        env.pop("HTSA_BACKEND", None)
    if not env.get("HTSA_EXEC_PYTHON"):                 # candidate scripts run under this interpreter
        env["HTSA_EXEC_PYTHON"] = python_exe()
    return env


def fresh_space_name(prefix: str) -> str:
    """<prefix>-HHMM (section 13.1), or <prefix>-HHMMSS when that space folder already exists, so a stage restarted
    in the same minute never opens the last one's log or reuses its loop batch."""
    spaces = Path(lab_root()) / "spaces"
    name = f"{prefix}-{time.strftime('%H%M')}"
    if (spaces / name).exists():
        name = f"{prefix}-{time.strftime('%H%M%S')}"
        while (spaces / name).exists():
            time.sleep(0.5)
            name = f"{prefix}-{time.strftime('%H%M%S')}"
    return name


# ---------------------------------------------------------------- the stage command lines (section 13.1, exactly)
def server_argv(name: str, port: int = C.PORT, lab: str | None = None, py: str | None = None) -> list[str]:
    lab = lab or lab_root()
    argv = [py or python_exe(), "-m", "space.server", "--db", f"{lab}/spaces/{name}/space.db",
            "--memory-dir", f"{lab}/memory/_mock/{PROFILE}"]
    return argv + (["--port", str(port)] if port != C.PORT else [])


def agent_argv(me: str, name: str, port: int = C.PORT, live: bool = False, py: str | None = None) -> list[str]:
    model = ["--model", "sonnet", "--fallback", "mock"] if live else ["--model", "mock"]
    return [py or python_exe(), "-m", "space.agent", "--me", me, *model,
            "--space", f"http://{C.HOST}:{port}", "--space-id", name]


def loop_argv(batch: str, port: int = C.PORT, py: str | None = None) -> list[str]:
    return [py or python_exe(), "-m", "nano.dry_run", "--batch", batch, "--profile", PROFILE, "--implement", "3",
            "--rounds", "2", "--space", f"http://{C.HOST}:{port}", "--me", "team.loop", "--step",
            "--control-poll-seconds", "1"]


def browser_argv(base: str, space_dir: str) -> list[tuple[str, list[str]]]:
    return [("chrome.ana", [CHROME, "--new-window", f"{base}/?me=ana"]),
            ("edge.ben", [EDGE, "--new-window", f"{base}/?me=ben"]),
            ("projector", [CHROME, f"--user-data-dir={space_dir}/projector-profile", "--no-first-run",
                           "--no-default-browser-check", f"--app={base}/?stage=1&follow=ana"])]


# ---------------------------------------------------------------- memory, ports, processes (Windows first)
def free_memory_gb() -> float | None:
    """Free physical memory in GB from GlobalMemoryStatusEx (Windows); /proc/meminfo elsewhere; None if unknown."""
    if os.name == "nt":
        import ctypes
        from ctypes import wintypes

        class MEMORYSTATUSEX(ctypes.Structure):
            _fields_ = [("dwLength", wintypes.DWORD), ("dwMemoryLoad", wintypes.DWORD),
                        ("ullTotalPhys", ctypes.c_ulonglong), ("ullAvailPhys", ctypes.c_ulonglong),
                        ("ullTotalPageFile", ctypes.c_ulonglong), ("ullAvailPageFile", ctypes.c_ulonglong),
                        ("ullTotalVirtual", ctypes.c_ulonglong), ("ullAvailVirtual", ctypes.c_ulonglong),
                        ("ullAvailExtendedVirtual", ctypes.c_ulonglong)]
        m = MEMORYSTATUSEX()
        m.dwLength = ctypes.sizeof(MEMORYSTATUSEX)
        if not ctypes.WinDLL("kernel32").GlobalMemoryStatusEx(ctypes.byref(m)):
            return None
        return m.ullAvailPhys / float(1 << 30)
    try:
        for line in Path("/proc/meminfo").read_text().splitlines():
            if line.startswith("MemAvailable:"):
                return int(line.split()[1]) / float(1 << 20)
    except OSError:
        pass
    return None


def memory_gate(free_gb: float | None, need: float = MIN_FREE_GB) -> tuple[bool, str]:
    if free_gb is None:
        return True, "free memory unknown on this system"
    if free_gb < need:
        return False, f"{free_gb:.1f} GB free, {need:.0f} GB needed: close browsers or other programs first"
    return True, f"{free_gb:.1f} GB free"


def port_free(port: int, host: str = C.HOST) -> bool:
    """True when nothing listens on host:port (bind without SO_REUSEADDR, as the server does)."""
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.bind((host, port))
        return True
    except OSError:
        return False
    finally:
        s.close()


def process_table() -> list[tuple[int, int, str]]:
    """[(pid, parent pid, exe name)] of every process, through CreateToolhelp32Snapshot. [] off Windows."""
    if os.name != "nt":
        return []
    import ctypes
    from ctypes import wintypes

    class PROCESSENTRY32W(ctypes.Structure):
        _fields_ = [("dwSize", wintypes.DWORD), ("cntUsage", wintypes.DWORD), ("th32ProcessID", wintypes.DWORD),
                    ("th32DefaultHeapID", ctypes.c_size_t), ("th32ModuleID", wintypes.DWORD),
                    ("cntThreads", wintypes.DWORD), ("th32ParentProcessID", wintypes.DWORD),
                    ("pcPriClassBase", ctypes.c_long), ("dwFlags", wintypes.DWORD), ("szExeFile", ctypes.c_wchar * 260)]
    k32 = ctypes.WinDLL("kernel32", use_last_error=True)
    k32.CreateToolhelp32Snapshot.restype = wintypes.HANDLE
    k32.CreateToolhelp32Snapshot.argtypes = (wintypes.DWORD, wintypes.DWORD)
    k32.Process32FirstW.argtypes = (wintypes.HANDLE, ctypes.POINTER(PROCESSENTRY32W))
    k32.Process32NextW.argtypes = (wintypes.HANDLE, ctypes.POINTER(PROCESSENTRY32W))
    k32.CloseHandle.argtypes = (wintypes.HANDLE,)
    h = k32.CreateToolhelp32Snapshot(0x2, 0)                   # TH32CS_SNAPPROCESS
    if h in (None, 0, ctypes.c_void_p(-1).value):
        return []
    out = []
    try:
        pe = PROCESSENTRY32W()
        pe.dwSize = ctypes.sizeof(PROCESSENTRY32W)
        ok = k32.Process32FirstW(h, ctypes.byref(pe))
        while ok:
            out.append((int(pe.th32ProcessID), int(pe.th32ParentProcessID), str(pe.szExeFile)))
            ok = k32.Process32NextW(h, ctypes.byref(pe))
    finally:
        k32.CloseHandle(h)
    return out


def process_start(pid: int) -> int | None:
    """When a process started (FILETIME ticks, from GetProcessTimes), or None when it cannot be read or off Windows."""
    if os.name != "nt":
        return None
    import ctypes
    from ctypes import wintypes
    k32 = ctypes.WinDLL("kernel32", use_last_error=True)
    k32.OpenProcess.restype = wintypes.HANDLE
    k32.OpenProcess.argtypes = (wintypes.DWORD, wintypes.BOOL, wintypes.DWORD)
    k32.GetProcessTimes.argtypes = (wintypes.HANDLE,) + (ctypes.POINTER(wintypes.FILETIME),) * 4
    k32.CloseHandle.argtypes = (wintypes.HANDLE,)
    h = k32.OpenProcess(0x1000, False, int(pid))                 # PROCESS_QUERY_LIMITED_INFORMATION
    if not h:
        return None
    try:
        t = [wintypes.FILETIME() for _ in range(4)]
        if not k32.GetProcessTimes(h, *(ctypes.byref(x) for x in t)):
            return None
        return (t[0].dwHighDateTime << 32) | t[0].dwLowDateTime
    finally:
        k32.CloseHandle(h)


def descendants(pid: int, table=None, started=None) -> list[tuple[int, str]]:
    """Every process under pid (children, grandchildren, ...) as (pid, exe).

    Windows keeps a dead parent's pid as th32ParentProcessID and reuses pids, so an unrelated program can name our pid
    as its parent. A child never starts before its parent: with `started` (pid -> start time; the live table uses
    process_start) such a process is left out, so it is neither reported nor killed."""
    if table is None:
        table = process_table()
        started = process_start if started is None else started
    kids: dict[int, list[tuple[int, str]]] = {}
    for p, pp, exe in table:
        if p != pp:
            kids.setdefault(pp, []).append((p, exe))
    times: dict[int, int | None] = {}

    def when(p):
        if p not in times:
            times[p] = started(p)
        return times[p]

    out, seen, todo = [], {pid}, [pid]
    while todo:
        parent = todo.pop()
        for p, exe in kids.get(parent, []):
            if p in seen:
                continue
            if started is not None and when(parent) is not None and (when(p) is None or when(p) < when(parent)):
                continue
            seen.add(p)
            out.append((p, exe))
            todo.append(p)
    return out


def is_claude(exe: str) -> bool:
    return exe.lower().startswith("claude")


def kill_tree(pid) -> bool:
    from space.launch import kill_tree as kt                  # taskkill /T /F /PID on Windows
    return kt(pid)


class Procs:
    """The child processes of one demo session, each with its own log under logs/."""

    def __init__(self, log_dir: Path, env: dict, say=None):
        self.log_dir, self.env, self.say = Path(log_dir), env, say or _say
        self.log_dir.mkdir(parents=True, exist_ok=True)
        self.procs: dict[str, subprocess.Popen] = {}
        self.order: list[str] = []
        self.argv: dict[str, list[str]] = {}

    def start(self, name: str, argv: list[str], env: dict | None = None, window: bool = False,
              log: bool = True) -> subprocess.Popen:
        flags = 0
        if os.name == "nt":
            flags = subprocess.CREATE_NEW_PROCESS_GROUP | (0 if window else subprocess.CREATE_NO_WINDOW)
        out = open(self.log_dir / f"{name}.log", "ab") if log else subprocess.DEVNULL
        try:
            if log:
                out.write(("$ %s\n" % " ".join(argv)).encode("utf-8"))
                out.flush()
            p = subprocess.Popen(argv, cwd=str(REPO), env=env or self.env, stdin=subprocess.DEVNULL, stdout=out,
                                 stderr=subprocess.STDOUT, creationflags=flags)
        finally:
            if log:
                out.close()
        self.procs[name], self.argv[name] = p, list(argv)
        if name not in self.order:
            self.order.append(name)
        return p

    def alive(self, name: str) -> bool:
        p = self.procs.get(name)
        return p is not None and p.poll() is None

    def stop(self, name: str, timeout: float = 10.0) -> None:
        p = self.procs.get(name)
        if p is None:
            return
        if p.poll() is None:
            kill_tree(p.pid)
            try:
                p.wait(timeout=timeout)
            except subprocess.TimeoutExpired:
                p.kill()
        self.procs.pop(name, None)

    def stop_all(self) -> None:
        for name in reversed(list(self.order)):
            self.stop(name)

    def tail(self, name: str, n: int = 8) -> str:
        from space.launch import tail
        return "\n".join(tail(str(self.log_dir / f"{name}.log"), n))


class Monitor(threading.Thread):
    """Samples this process's descendants every second and remembers any claude process among them."""

    def __init__(self, every: float = 1.0):
        super().__init__(name="demo-monitor", daemon=True)
        self.every, self.claude, self.stop_ev = every, set(), threading.Event()

    def run(self):
        while not self.stop_ev.wait(self.every):
            try:
                for pid, exe in descendants(os.getpid()):
                    if is_claude(exe):
                        self.claude.add(f"{exe} (pid {pid})")
            except Exception:  # noqa: BLE001 - a monitor never stops the demo
                pass

    def stop(self):
        self.stop_ev.set()


# ---------------------------------------------------------------- HTTP to the space
class Api:
    def __init__(self, base: str, key: str = ""):
        self.base, self.key = base.rstrip("/"), key

    def call(self, method: str, path: str, body=None, actor: str | None = None, kind: str = "human",
             timeout: float = 3.0):
        """(status, json). A dead server raises OSError."""
        h = {}
        if body is not None:
            h["Content-Type"] = "application/json"
        if actor:
            h["X-Space-Actor"], h["X-Space-Kind"] = actor, kind
        if self.key:
            h["X-Space-Key"] = self.key
        data = None if body is None else json.dumps(body).encode("utf-8")
        req = urllib.request.Request(self.base + path, method=method, data=data, headers=h)
        try:
            with urllib.request.urlopen(req, timeout=timeout) as r:
                raw = r.read()
                return r.status, (json.loads(raw) if raw else {})
        except urllib.error.HTTPError as e:
            raw = e.read()
            try:
                return e.code, (json.loads(raw) if raw else {})
            except ValueError:
                return e.code, {"error": raw[:200].decode("utf-8", "replace")}

    def up(self) -> bool:
        try:
            return self.call("GET", "/api/events?since=0&limit=1&wait=0", timeout=1.0)[0] == 200
        except (OSError, ValueError):
            return False

    def wait_up(self, timeout: float = 20.0) -> bool:
        end = time.monotonic() + timeout
        while time.monotonic() < end:
            if self.up():
                return True
            time.sleep(0.2)
        return False

    def all_events(self) -> list[dict]:
        """The whole log by paging GET /api/events (a fresh reader)."""
        out, since = [], 0
        while True:
            st, d = self.call("GET", f"/api/events?since={since}&limit=2000&wait=0", timeout=10.0)
            if st != 200:
                raise OSError(f"GET /api/events answered {st}")
            evs = d.get("events") or []
            out += evs
            if not evs or evs[-1]["seq"] >= int(d.get("head") or 0):
                return out
            since = evs[-1]["seq"]


class Reader(threading.Thread):
    """One long-poll reader that keeps the whole log in order, survives a server restart, and records any gap or
    duplicate (the contiguity check of the drill)."""

    def __init__(self, api: Api, wait_s: int = 5):
        super().__init__(name="demo-reader", daemon=True)
        self.api, self.wait_s = api, wait_s
        self.events: list[dict] = []
        self.cond = threading.Condition()
        self.stop_ev = threading.Event()
        self.gaps, self.dups, self.epochs = [], 0, set()
        self.down_s = 0.0

    @property
    def head(self) -> int:
        return self.events[-1]["seq"] if self.events else 0

    def run(self):
        while not self.stop_ev.is_set():
            try:
                st, d = self.api.call("GET", f"/api/events?since={self.head}&limit=500&wait={self.wait_s}",
                                      timeout=self.wait_s + 5)
            except (OSError, ValueError):
                self.down_s += 0.3
                self.stop_ev.wait(0.3)
                continue
            if st != 200:
                self.stop_ev.wait(0.3)
                continue
            if d.get("epoch"):
                self.epochs.add(d["epoch"])
            with self.cond:
                for ev in d.get("events") or []:
                    s = int(ev.get("seq") or 0)
                    if s <= self.head:
                        self.dups += 1
                        continue
                    if s != self.head + 1:
                        self.gaps.append((self.head, s))
                    self.events.append(ev)
                self.cond.notify_all()

    def stop(self):
        self.stop_ev.set()
        with self.cond:
            self.cond.notify_all()

    def snapshot(self) -> list[dict]:
        with self.cond:
            return list(self.events)

    def find(self, pred, after: int = 0):
        with self.cond:
            for ev in self.events:
                if ev["seq"] > after and pred(ev):
                    return ev
        return None

    def wait_for(self, pred, timeout: float, after: int = 0):
        end = time.monotonic() + timeout
        with self.cond:
            while True:
                for ev in self.events:
                    if ev["seq"] > after and pred(ev):
                        return ev
                left = end - time.monotonic()
                if left <= 0 or self.stop_ev.is_set():
                    return None
                self.cond.wait(min(left, 0.5))


# ---------------------------------------------------------------- reading the log: beats and the rows of 13.5
def _ts(ev) -> float | None:
    t = str(ev.get("ts") or "").rstrip("Z")
    for fmt in ("%Y-%m-%dT%H:%M:%S.%f", "%Y-%m-%dT%H:%M:%S"):
        try:
            return datetime.datetime.strptime(t, fmt).replace(tzinfo=datetime.timezone.utc).timestamp()
        except ValueError:
            pass
    return None


def _cls(ev) -> str:
    return C.actor_class(ev.get("by") or "", ev.get("by_kind") or "", ev.get("owner") or "")


def _d(ev) -> dict:
    return ev.get("data") or {}


def _is_stage(ev, rnd=None, stage=None, waiting=None) -> bool:
    if ev.get("kind") != "stage_entered" or _cls(ev) != "team":
        return False
    d = _d(ev)
    return ((rnd is None or d.get("round") == rnd) and (stage is None or d.get("stage") == stage)
            and (waiting is None or bool(d.get("waiting")) == waiting))


def _is_step(ev, rnd, stage) -> bool:
    return ev.get("kind") == "run_step" and _d(ev).get("round") == rnd and _d(ev).get("stage") == stage


def _first(events, pred):
    return next((e for e in events if pred(e)), None)


def _human(ev) -> bool:
    return _cls(ev) in ("person", "delegate")


# beat name -> (scripted time, finder). A finder returns the event that marks the beat in the log.
def _beat_finders():
    def votes(evs):
        by = {}
        for e in evs:
            if e["kind"] == "vote_cast" and _human(e) and e.get("owner") in PEOPLE:
                by.setdefault(e["owner"], e)
        return max(by.values(), key=lambda e: e["seq"]) if len(by) == 2 else None

    def choose(evs):
        first = _first(evs, lambda e: e["kind"] == "question_chosen" and e.get("owner") == "ana")
        return first and _first(evs, lambda e: e["kind"] == "question_chosen" and e.get("owner") == "ben"
                                and e["seq"] > first["seq"])

    return [
        ("open", "0:00", lambda evs: _first(evs, lambda e: _is_stage(e, 1, "planned"))),
        ("branch", "0:15", lambda evs: _first(evs, lambda e: e["kind"] == "node_added" and _human(e)
                                              and _d(e).get("id") == "item_order")),
        ("note", "0:35", lambda evs: _first(evs, lambda e: e["kind"] == "note_posted" and e.get("owner") == "ben"
                                            and "tie-breaking" in str(_d(e).get("text")))),
        ("go_planned_1", "0:50", lambda evs: _first(evs, lambda e: _is_step(e, 1, "planned"))),
        ("go_ideated_1", "1:15", lambda evs: _first(evs, lambda e: _is_step(e, 1, "ideated"))),
        ("votes", "1:30", votes),
        ("go_clustered_1", "1:45", lambda evs: _first(evs, lambda e: _is_step(e, 1, "clustered"))),
        ("reply", "2:05", lambda evs: _first(evs, lambda e: e["kind"] == "reply_posted" and _human(e)
                                             and e.get("owner") == "ana" and _d(e).get("kind") == "rebut")),
        ("go_deepened_1", "2:20", lambda evs: _first(evs, lambda e: _is_step(e, 1, "deepened"))),
        ("go_built_1", "2:20", lambda evs: _first(evs, lambda e: _is_step(e, 1, "built"))),
        ("win", "2:55", lambda evs: _first(evs, lambda e: e["kind"] == "test_result" and _d(e).get("status") in POSITIVE)),
        ("preview", "3:10", lambda evs: _first(evs, lambda e: e["kind"] == "question_preview"
                                               and _d(e).get("round_next") == 2)),
        ("veto", "3:15", lambda evs: _first(evs, lambda e: e["kind"] == "question_vetoed" and e.get("owner") == "ben")),
        ("choose", "3:25", choose),
        ("drill", DRILL_AT, lambda evs: _first(evs, lambda e: e["kind"] == "claim_expired"
                                               and _d(e).get("reason") == "restart")),
        ("go_verified_1", "3:40", lambda evs: _first(evs, lambda e: _is_step(e, 1, "verified"))),
        ("pick", "3:40", lambda evs: _first(evs, lambda e: e["kind"] == "question_picked" and _d(e).get("round") == 2)),
    ]


OPTIONAL_BEATS = {"drill"}


def find_beats(events) -> list[dict]:
    """The script's beats as found in a log: [{beat, t, seq, kind}] in script order (seq None when absent)."""
    evs = sorted(events, key=lambda e: e.get("seq") or 0)
    out = []
    for name, t, fn in _beat_finders():
        e = fn(evs)
        out.append({"beat": name, "t": t, "seq": e["seq"] if e else None, "kind": e["kind"] if e else None})
    return out


def beat_seqs(beats) -> list:
    return [(b["beat"], b["seq"]) for b in beats if b["seq"] is not None]


def beats_ok(beats, drill: bool = True) -> tuple[bool, str]:
    need = [b for b in beats if b["beat"] not in OPTIONAL_BEATS or drill]
    missing = [b["beat"] for b in need if b["seq"] is None]
    if missing:
        return False, "missing beats: " + ", ".join(missing)
    seqs = [b["seq"] for b in need]
    order = [n["beat"] for n, m in zip(need, need[1:]) if m["seq"] <= n["seq"]]
    if order:
        return False, "out of order after: " + ", ".join(order)
    return True, f"{len(need)} beats, seqs {seqs[0]} to {seqs[-1]}"


def _voters_py(evs) -> dict:
    """{owner: [hit|miss|open]} from the log alone: a vote's cluster_id, the candidate built from it, its result."""
    votes = {}
    for e in evs:
        if e["kind"] == "vote_cast" and _human(e):
            votes[(e.get("owner"), _d(e).get("idea"))] = _d(e).get("value")
    built = {}
    for e in evs:
        if e["kind"] == "candidate_built":
            built.setdefault(_d(e).get("idea"), _d(e).get("cand"))
    status = {}
    for e in evs:
        if e["kind"] == "test_result":
            status[_d(e).get("cand")] = _d(e).get("status")
    out = {}
    for (owner, idea), v in votes.items():
        st = status.get(built.get(idea))
        word = ("hit" if v > 0 else "miss") if st in POSITIVE else (("miss" if v > 0 else "hit") if st in NEGATIVE else "open")
        out.setdefault(owner, []).append(word)
    return out


def check_log(events, reduced: dict | None = None, drill: bool = True) -> dict:
    """The log rows of section 13.5: {row: (ok, detail)}. `reduced` is the Node reducer's summary of the same log
    (hash.mjs: voters, won); without it the voters and the won cluster are derived here by cluster id."""
    evs = sorted(events, key=lambda e: e.get("seq") or 0)
    rows: dict[str, tuple[bool, str]] = {}

    # ack_2s
    chats = [e for e in evs if e["kind"] == "chat_posted" and _cls(e) == "person"]
    late = []
    for c in chats:
        to = _d(c).get("to")
        ack = _first(evs, lambda e: e["kind"] == "agent_said" and e.get("by") == to and _d(e).get("kind") == "ack"
                     and e.get("cause") == c["seq"])
        if ack is None or (_ts(ack) or 0) - (_ts(c) or 0) > ACK_S:
            late.append(c["seq"])
    rows["ack_2s"] = (bool(chats) and not late,
                      f"{len(chats)} chats, slowest ack {_slowest_ack(evs, chats):.2f} s" if not late
                      else f"no ack within 2 s for chats {late}")

    # peer_2s
    node = _first(evs, lambda e: e["kind"] == "node_added" and _human(e) and _d(e).get("id") == "item_order")
    if node is None:
        rows["peer_2s"] = (False, "no node_added item_order")
    else:
        peer = _first(evs, lambda e: e["seq"] > node["seq"] and e["kind"] == "agent_said" and e.get("by") == "ben.agent"
                      and _d(e).get("kind") == "peer")
        dt = (_ts(peer) or 0) - (_ts(node) or 0) if peer else None
        rows["peer_2s"] = (peer is not None and dt <= PEER_S,
                           f"e{peer['seq']} after {dt:.2f} s: {str(_d(peer).get('text'))[:70]}" if peer else "no peer line")

    # applied_item_order
    if node is None:
        rows["applied_item_order"] = (False, "no node_added item_order")
    else:
        ca = _first(evs, lambda e: e["kind"] == "control_applied" and node["seq"] in (_d(e).get("refs") or []))
        ok = (ca is not None and _d(ca).get("round") == 1 and _d(ca).get("stage") == "planned"
              and node.get("owner") == "ana"
              and "item_order" in ((_d(ca).get("keys") or {}).get("add_nodes") or []))
        rows["applied_item_order"] = (ok, f"control_applied e{ca['seq']} at {_d(ca).get('stage')} r{_d(ca).get('round')}, "
                                          f"node by {node.get('owner')}" if ca else "no control_applied lists it")

    # sketch_item_order
    sk = _first(evs, lambda e: e["kind"] == "sketch_batch" and _d(e).get("node") == "item_order"
                and _d(e).get("round") == 1)
    rows["sketch_item_order"] = (sk is not None, f"e{sk['seq']}, {_d(sk).get('count')} sketches" if sk else "none")

    # digests_both
    stages = [e for e in evs if _is_stage(e)]
    missing = []
    for s in stages:
        for me in PEOPLE:
            if not _first(evs, lambda e: e["kind"] == "digest_taken" and e.get("by") == f"{me}.agent"
                          and e.get("cause") == s["seq"]):
                missing.append(f"{me}@e{s['seq']}")
    rows["digests_both"] = (bool(stages) and not missing,
                            f"{len(stages)} boundaries x 2 agents" if not missing else "missing " + ", ".join(missing[:6]))

    # preview_before_pick
    pv = _first(evs, lambda e: e["kind"] == "question_preview" and _d(e).get("round_next") == 2)
    pk = _first(evs, lambda e: e["kind"] == "question_picked" and _d(e).get("round") == 2)
    rows["preview_before_pick"] = (bool(pv and pk and pv["seq"] < pk["seq"]),
                                   f"preview e{pv['seq'] if pv else '-'}, pick e{pk['seq'] if pk else '-'}")

    # overwrote: the server stamps it when Ben's base is older than Ana's choice; the reducer derives it on the
    # screen ("Ben's choice replaced yours") from the order of the two choices. Either one passes; the detail says
    # which, so a run where only the screen shows it is visible as such.
    first_ch = _first(evs, lambda e: e["kind"] == "question_chosen" and e.get("owner") == "ana")
    ch = first_ch and _first(evs, lambda e: e["kind"] == "question_chosen" and e.get("owner") == "ben"
                             and e["seq"] > first_ch["seq"])
    stamped = (_d(ch).get("overwrote") or []) if ch else []
    shown = []
    if reduced is not None and ch:
        c = reduced.get("chosen") or {}
        if c.get("seq") == ch["seq"]:
            shown = [o for o in c.get("overwrote") or [] if o.get("seq") == first_ch["seq"]]
    elif ch and not any(e["kind"] == "question_picked" and first_ch["seq"] < e["seq"] < ch["seq"] for e in evs):
        shown = [{"field": "choose", "seq": first_ch["seq"], "by": first_ch.get("owner")}]   # the reducer's rule
    if not ch:
        rows["overwrote"] = (False, "no question_chosen by ben after ana's")
    else:
        rows["overwrote"] = (bool(stamped or shown),
                             f"e{ch['seq']} after ana's e{first_ch['seq']}: "
                             + (f"server overwrote {stamped}" if stamped else
                                f"the screen shows overwrote {shown}; no server stamp (base e{ch.get('base')} had seen "
                                f"e{first_ch['seq']})"))

    # win_and_won
    win = _first(evs, lambda e: e["kind"] == "test_result" and _d(e).get("status") == "win")
    if reduced is not None:
        won = int(reduced.get("won") or 0)
    else:
        built_ideas = {_d(e).get("cand"): _d(e).get("idea") for e in evs if e["kind"] == "candidate_built"}
        won = int(bool(win and built_ideas.get(_d(win).get("cand"))))
    rows["win_and_won"] = (bool(win) and won >= 1,
                           f"test_result win e{win['seq']} ({_d(win).get('cand')}), clusters won: {won}" if win
                           else "no test_result with status win")

    # voters_hit_or_miss
    voters = (reduced or {}).get("voters") if reduced is not None else _voters_py(evs)
    voters = voters or {}
    bad = [p for p in PEOPLE if not any(w in ("hit", "miss") for w in voters.get(p) or [])]
    rows["voters_hit_or_miss"] = (not bad, ", ".join(f"{p}: {'/'.join(voters.get(p) or ['none'])}" for p in PEOPLE))

    # vetoed_in_pick
    vt = _first(evs, lambda e: e["kind"] == "question_vetoed" and e.get("owner") == "ben")
    q = _d(vt).get("question") if vt else None
    rows["vetoed_in_pick"] = (bool(vt and pk and q in (_d(pk).get("vetoed") or [])),
                              f"{q} in vetoed {_d(pk).get('vetoed')}, chosen by {_d(pk).get('by')}" if (vt and pk)
                              else "no veto or no round 2 pick")

    # beats_in_order
    beats = find_beats(evs)
    rows["beats_in_order"] = beats_ok(beats, drill)

    # the log part of the drill
    if drill:
        ex = [e for e in evs if e["kind"] == "claim_expired" and _d(e).get("reason") == "restart"]
        rows["drill_log"] = (bool(ex), f"{len(ex)} claim_expired with reason restart" if ex else "no claim_expired restart")
    return rows


def _slowest_ack(evs, chats) -> float:
    worst = 0.0
    for c in chats:
        ack = _first(evs, lambda e: e["kind"] == "agent_said" and e.get("by") == _d(c).get("to")
                     and _d(e).get("kind") == "ack" and e.get("cause") == c["seq"])
        if ack:
            worst = max(worst, (_ts(ack) or 0) - (_ts(c) or 0))
    return worst


def private_hits(events) -> list[str]:
    """Where a private key (obvious, obvious_match, private) appears at any depth of any event."""
    hits = []

    def walk(x, where):
        if isinstance(x, dict):
            for k, v in x.items():
                if k in C.PRIVATE_KEYS:
                    hits.append(f"{where}.{k}")
                walk(v, f"{where}.{k}")
        elif isinstance(x, list):
            for i, v in enumerate(x):
                walk(v, f"{where}[{i}]")
    for e in events:
        walk(e, f"e{e.get('seq')}")
    return hits


def read_ndjson(path) -> list[dict]:
    out = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                out.append(json.loads(line))
    return out


def node_reduce(log_path) -> dict:
    """The Node reducer with the real layout over a log (hash.mjs): layout_hash, state_hash, voters, won."""
    node = node_exe()
    if not node:
        raise RuntimeError("node is not installed")
    r = subprocess.run([node, str(HASH_MJS), str(log_path)], cwd=str(REPO), capture_output=True, timeout=180,
                       creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0))
    if r.returncode != 0:
        raise RuntimeError("hash.mjs failed: " + r.stderr.decode("utf-8", "replace")[-600:])
    return json.loads(r.stdout.decode("utf-8"))


def print_table(rows: dict, out=None) -> None:
    out = out or sys.stdout
    w = max(len(n) for n in ROW_NAMES)
    print("%-*s  %-4s  %s" % (w, "row (13.5)", "ok", "detail"), file=out)
    for name, _src, what in ROWS:
        ok, detail = rows.get(name, (None, "not run"))
        word = "ok" if ok else ("--" if ok is None else "FAIL")
        print("%-*s  %-4s  %s" % (w, name, word, detail or what), file=out)
    out.flush()


def print_beats(beats, out=None) -> None:
    out = out or sys.stdout
    for b in beats:
        print("  %s  %-15s %s" % (b["t"], b["beat"], ("e%d %s" % (b["seq"], b["kind"])) if b["seq"] else "-"), file=out)
    out.flush()


# ---------------------------------------------------------------- --check
def run_check(port: int = C.PORT, out=None) -> int:
    out = out or sys.stdout
    rows = []
    rows.append(("port", port_free(port), f"127.0.0.1:{port} is {'free' if port_free(port) else 'in use'}"))
    try:
        man = json.loads((WEB / "vendor" / "MANIFEST.json").read_text(encoding="utf-8"))
        bad = []
        for f in man.get("files") or []:
            p = WEB / "vendor" / f["file"]
            size = p.stat().st_size if p.exists() else None
            if size != f.get("bytes"):
                bad.append(f"{f['file']} {size} != {f.get('bytes')}")
        rows.append(("vendor", not bad, "every vendor file has its pinned size" if not bad else "; ".join(bad)))
    except (OSError, ValueError) as e:
        rows.append(("vendor", False, f"no manifest: {e}"))
    for name, path in (("chrome", CHROME), ("edge", EDGE)):
        rows.append((name, os.path.exists(path), path))
    spaces = Path(lab_root()) / "spaces"
    try:
        spaces.mkdir(parents=True, exist_ok=True)
        rows.append(("spaces", spaces.is_dir(), str(spaces)))
    except OSError as e:
        rows.append(("spaces", False, f"{spaces}: {e}"))
    ok, why = memory_gate(free_memory_gb())
    rows.append(("memory", ok, why))
    rec = [RECORDED / LOG_NAME, RECORDED / HASH_NAME]
    rows.append(("recorded", all(p.exists() for p in rec), ", ".join(p.name for p in rec)))
    if all(p.exists() for p in rec):
        hits = private_hits(read_ndjson(RECORDED / LOG_NAME))
        rows.append(("private", not hits, "no private key in the recorded log" if not hits else ", ".join(hits[:5])))
    node = node_exe()
    if node:
        r = subprocess.run([node, "--test", str(REPLAY_TESTS.relative_to(REPO)).replace("\\", "/")], cwd=str(REPO),
                           capture_output=True, timeout=300, creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0))
        tail = r.stdout.decode("utf-8", "replace").strip().splitlines()[-8:]
        summary = ", ".join(m.group(1) for x in tail if (m := re.search(r"\b((?:tests|pass|fail) \d+)\s*$", x.strip())))
        rows.append(("replay test", r.returncode == 0, "node --test space/web/tests/replay: " + (summary or f"rc {r.returncode}")))
    else:
        rows.append(("replay test", False, "node is not installed"))
    w = max(len(r[0]) for r in rows)
    for name, ok, detail in rows:
        print("%-*s  %-4s  %s" % (w, name, "ok" if ok else "FAIL", detail), file=out)
    print("for --lan, once, in an admin shell:  " + NETSH.format(port=port), file=out)
    failed = [r[0] for r in rows if not r[1]]
    print("check: " + ("all passed" if not failed else "FAILED: " + ", ".join(failed)), file=out)
    out.flush()
    return 0 if not failed else 1


# ---------------------------------------------------------------- the console Go and the current beat
def go_now(api: Api, who: str = GO_AS):
    """Post run_step for the boundary the loop waits at (from the snapshot). Returns the answer, or None when the
    loop is not waiting (a Go is never posted ahead of its stage_entered)."""
    st, snap = api.call("GET", "/api/snapshot")
    run = (snap or {}).get("run") or {}
    if st != 200 or not run.get("waiting") or run.get("stage") not in C.STAGES:
        return None
    rnd, stage = int(run.get("round") or 1), run["stage"]
    body = {"kind": "run_step", "subject": "run:main", "label": f"Go {stage} r{rnd}", "round": rnd, "stage": stage,
            "data": {"round": rnd, "stage": stage}, "op": f"{who}-go-{int(time.time() * 1000)}"}
    st, d = api.call("POST", "/api/events", body, actor=who, kind="human")
    return dict(d, status=st, round=rnd, stage=stage)


def current_beat_seq(live_events, recorded_beats) -> int:
    """The recorded seq of the last beat the live run reached (the Replay hotkey seeks there)."""
    live = {b["beat"]: b["seq"] for b in find_beats(live_events) if b["seq"]}
    seq = 0
    for b in recorded_beats:
        if b["beat"] in OPTIONAL_BEATS:                   # a k press on stage is not the recorded 3:30 drill
            continue
        if b["beat"] in live and b.get("seq"):
            seq = b["seq"]
    return seq


# ---------------------------------------------------------------- --rehearse
class Abort(Exception):
    pass


class Rehearsal:
    def __init__(self, port: int = C.PORT, drill: str = "restart", pace: float = 1.0, out_dir: Path | None = None,
                 say=None):
        self.port, self.drill, self.pace = port, drill == "restart", float(pace)
        self.out_dir = Path(out_dir) if out_dir else RECORDED
        self.say = say or _say
        self.base = f"http://{C.HOST}:{port}"
        self.api = Api(self.base)
        self.rows: dict[str, tuple[bool, str]] = {}
        self.posts: list[tuple[str, float]] = []
        self.ids: dict = {}
        self.t0 = None
        self.n = 0
        self.ms0 = int(time.time() * 1000)

    # ---- small steps
    def log(self, msg):
        t = "" if self.t0 is None else "[%5.1f s] " % (time.monotonic() - self.t0)
        self.say(f"rehearse {t}{msg}")

    def at(self, t: str):
        if self.t0 is None:
            return
        left = self.t0 + secs(t) * self.pace - time.monotonic()
        if left > 0:
            time.sleep(left)

    def post(self, who: str, body: dict) -> int:
        self.n += 1
        body = dict(body, op=f"{who}-{self.ms0}-{self.n}")
        t = time.perf_counter()
        st, d = self.api.call("POST", "/api/events", body, actor=who, kind="human")
        ms = (time.perf_counter() - t) * 1000.0
        self.posts.append((f"{body['kind']} by {who}", ms))
        if st != 200 or "seq" not in d:
            raise Abort(f"POST {body['kind']} by {who} answered {st} {d}")
        return int(d["seq"])

    def chat(self, who: str, text: str, ack_timeout: float = 10.0) -> int:
        seq = self.post(who, {"kind": "chat_posted", "subject": f"person:{who}", "label": text[:80],
                              "data": {"to": f"{who}.agent", "text": text, "shared": True}})
        ack = self.reader.wait_for(lambda e: e["kind"] == "agent_said" and e.get("by") == f"{who}.agent"
                                   and _d(e).get("kind") == "ack" and e.get("cause") == seq, ack_timeout)
        if ack is None:
            raise Abort(f"no ack from {who}.agent for chat e{seq}")
        self.log(f"{who}: {text}  ->  e{seq}, ack e{ack['seq']}: {str(_d(ack).get('text'))[:90]}")
        if str(_d(ack).get("text", "")).startswith("Not done"):
            raise Abort(f"{who}.agent refused: {_d(ack).get('text')}")
        return seq

    def wait_stage(self, rnd, stage, timeout) -> dict:
        ev = self.reader.wait_for(lambda e: _is_stage(e, rnd, stage), timeout)
        if ev is None:
            raise Abort(f"the loop never reached {stage} r{rnd} within {timeout:.0f} s")
        return ev

    def go(self, rnd: int, stage: str, timeout: float) -> int:
        ev = self.wait_stage(rnd, stage, timeout)
        if not _d(ev).get("waiting"):
            raise Abort(f"stage_entered {stage} r{rnd} is not waiting for a Go")
        seq = self.post(GO_AS, {"kind": "run_step", "subject": "run:main", "label": f"Go {stage} r{rnd}",
                                "round": rnd, "stage": stage, "data": {"round": rnd, "stage": stage}, "cause": ev["seq"]})
        self.log(f"Go ({stage} r{rnd}) -> e{seq}")
        return seq

    def wait_event(self, pred, timeout: float, what: str, after: int = 0) -> dict:
        ev = self.reader.wait_for(pred, timeout, after)
        if ev is None:
            raise Abort(f"timed out waiting for {what}")
        return ev

    def latest_clusters(self) -> list[dict]:
        last = {}
        for e in self.reader.snapshot():
            if e["kind"] == "cluster_snapshot":
                last[(_d(e).get("node"), _d(e).get("direction"))] = e
        out = []
        for e in sorted(last.values(), key=lambda x: x["seq"]):
            out += [dict(c, node=_d(e).get("node")) for c in _d(e).get("clusters") or []]
        return out

    # ---- the script of 13.3
    def script(self):
        r = self.reader
        nodes = [e for e in r.snapshot() if e["kind"] == "node_added" and _cls(e) == "team"]
        self.log(f"0:00 the loop waits at planned r1; {len(nodes)} parts on the map")
        self.at("0:15")
        self.chat("ana", '/branch root "item order": how items are sorted before packing --claim')
        node = self.wait_event(lambda e: e["kind"] == "node_added" and _d(e).get("id") == "item_order", 5, "node_added item_order")
        self.ids["item_order_seq"] = node["seq"]
        self.wait_event(lambda e: e["kind"] == "claim_granted" and e.get("subject") == "node:item_order", 5, "the claim")
        self.wait_event(lambda e: e["kind"] == "agent_said" and e.get("by") == "ben.agent" and _d(e).get("kind") == "peer",
                        5, "Ben's agent's peer line", after=node["seq"])

        self.at("0:35")
        self.chat("ben", "/note check tie-breaking before the choice rule")
        self.at("0:50")
        self.go(1, "planned", 60)
        self.wait_event(lambda e: e["kind"] == "control_applied" and node["seq"] in (_d(e).get("refs") or []), 30,
                        "control_applied for item_order")

        self.at("1:15")
        self.go(1, "ideated", 120)
        self.wait_stage(1, "clustered", 120)

        self.at("1:30")
        # Vote on what the team is most likely to build: the selected clusters, main lane first (a longshot pick
        # can change when the clusters are re-selected after the critics), then the rest by rank.
        live = self.latest_clusters()
        sel = sorted([c for c in live if c.get("selected")], key=lambda c: c.get("lane") != "main")
        rest = sorted([c for c in live if not c.get("selected")],
                      key=lambda c: (c.get("rank") is None, c.get("rank") or 0))
        pool = sel + rest
        if len(pool) < 2:
            raise Abort("fewer than two clusters to vote on")
        a_ben, a_ana = pool[0], next(c for c in pool[1:] if c.get("cluster_id") != pool[0].get("cluster_id"))
        self.ids.update(vote_ben=a_ben.get("cluster_id"), vote_ben_name=a_ben.get("name"),
                        vote_ana=a_ana.get("cluster_id"), vote_ana_name=a_ana.get("name"))
        self.chat("ben", f"/vote up {a_ben['cluster_id']}")
        time.sleep(1.0)
        self.chat("ana", f"/vote up {a_ana['cluster_id']}")

        self.at("1:45")
        self.go(1, "clustered", 120)
        self.wait_stage(1, "deepened", 180)

        self.at("2:05")
        live = {c.get("cluster_id") for c in self.latest_clusters()}
        objs = [e for e in r.snapshot() if e["kind"] == "objection_raised" and _d(e).get("objection") == 2
                and _d(e).get("idea") in live]
        if not objs:
            objs = [e for e in r.snapshot() if e["kind"] == "objection_raised" and _d(e).get("idea") in live]
        if not objs:
            raise Abort("no objection on a live cluster to reply to")
        tgt = _d(objs[0])
        self.ids.update(reply_idea=tgt.get("idea"), reply_objection=tgt.get("objection"),
                        reply_name=next((c.get("name") for c in self.latest_clusters()
                                         if c.get("cluster_id") == tgt.get("idea")), None))
        self.chat("ana", f"/reply {tgt['idea']} {tgt['objection']} rebut: {REPLY_TEXT}")

        self.at("2:20")
        self.go(1, "deepened", 60)
        self.go(1, "built", 180)

        self.at("2:55")
        # results land one by one; a win found by a same-round fix is posted with the verified boundary
        win = self.wait_event(lambda e: (e["kind"] == "test_result" and _d(e).get("status") in POSITIVE)
                              or _is_stage(e, 1, "verified"), 240, "a winning test_result or the verified boundary")
        self.log(f"first result: {_d(win).get('cand')} {_d(win).get('status')} (e{win['seq']})"
                 if win["kind"] == "test_result" else f"verified r1 reached (e{win['seq']})")

        self.at("3:10")
        self.wait_stage(1, "verified", 180)
        pv = self.wait_event(lambda e: e["kind"] == "question_preview" and _d(e).get("round_next") == 2, 10,
                             "the round 2 preview")
        top3 = [q.get("id") for q in _d(pv).get("top3") or [] if isinstance(q, dict)]
        if len(top3) < 2:
            raise Abort(f"the preview has {len(top3)} questions; the double choose needs two")
        q1, q2, q3 = top3[0], top3[1], (top3[2] if len(top3) > 2 else top3[1])
        self.ids.update(q1=q1, q2=q2, q3=q3, preview_seq=pv["seq"])

        self.at("3:15")
        self.chat("ben", f"/veto {q1}")
        self.at("3:25")
        self.chat("ana", f"/choose {q2}")
        time.sleep(1.5)
        self.chat("ben", f"/choose {q3}")

        if self.drill:
            self.at(DRILL_AT)
            self.run_drill()

        self.at("3:40")
        self.go(1, "verified", 60)
        pk = self.wait_event(lambda e: e["kind"] == "question_picked" and _d(e).get("round") == 2, 120,
                             "the round 2 pick")
        self.log(f"pick of round 2: chosen {(_d(pk).get('chosen') or {}).get('id') if isinstance(_d(pk).get('chosen'), dict) else _d(pk).get('chosen')}"
                 f" by {_d(pk).get('by')}, vetoed {_d(pk).get('vetoed')}")
        st = self.wait_stage(2, "ideated", 60)
        for me in PEOPLE:
            self.wait_event(lambda e, me=me: e["kind"] == "digest_taken" and e.get("by") == f"{me}.agent"
                            and e.get("cause") == st["seq"], 15, f"{me}'s digest at ideated r2")
        self.at("3:50")
        self.log("3:50 close")

    # ---- the kill-and-restart drill
    def run_drill(self):
        open_claims = [c for c in (self.api.call("GET", "/api/snapshot")[1].get("claims") or [])]
        head_before = self.reader.head
        self.log(f"drill: killing the server at head {head_before} with {len(open_claims)} open claim(s)")
        self.procs.stop("server")
        if self.api.up():
            raise Abort("the server still answers after the kill")
        self.outbox_seen = self.outbox_lines()
        started = False
        for _ in range(20):
            p = self.procs.start("server", self.server_cmd)
            if self.api.wait_up(8.0):
                started = True
                break
            if p.poll() is None:
                self.procs.stop("server")
            time.sleep(0.5)
        if not started:
            raise Abort("the server did not come back after the kill:\n" + self.procs.tail("server"))
        exp = self.reader.wait_for(lambda e: e["kind"] == "claim_expired" and _d(e).get("reason") == "restart", 15,
                                   head_before)
        flushed = self.wait_outboxes(15.0)
        time.sleep(1.0)
        fresh = self.api.all_events()
        mine = self.reader.snapshot()
        fresh_seqs = [e["seq"] for e in fresh]
        read_seqs = [e["seq"] for e in mine]
        contiguous = fresh_seqs == list(range(1, len(fresh_seqs) + 1))
        same = read_seqs == fresh_seqs[:len(read_seqs)]
        ok = bool(exp) and flushed and contiguous and same and not self.reader.gaps and not self.reader.dups \
            and len(self.reader.epochs) == 1 and len(open_claims) >= 1
        self.rows["drill_restart"] = (ok, f"head {head_before} -> {fresh_seqs[-1] if fresh_seqs else 0}, "
                                          f"contiguous {contiguous}, reader gaps {len(self.reader.gaps)} dups {self.reader.dups}, "
                                          f"epochs {len(self.reader.epochs)}, claim_expired restart "
                                          f"{'e%d' % exp['seq'] if exp else 'none'}, outboxes flushed {flushed} "
                                          f"({self.outbox_seen} line(s) were pending)")
        self.log("drill: " + self.rows["drill_restart"][1])

    def outbox_lines(self) -> int:
        return sum(_count_lines(self.agent_dir / f"{me}.outbox.ndjson") for me in PEOPLE)

    def wait_outboxes(self, timeout: float) -> bool:
        """True once both agents' outboxes are empty. The agents post only in answer to events, so while the server is
        down they usually queue nothing; the drill's detail says how many lines were pending (outbox_seen)."""
        end = time.monotonic() + timeout
        while True:
            self.outbox_seen = max(getattr(self, "outbox_seen", 0), self.outbox_lines())
            left = [me for me in PEOPLE if _nonempty(self.agent_dir / f"{me}.outbox.ndjson")]
            if not left:
                return True
            if time.monotonic() > end:
                return False
            time.sleep(0.3)

    # ---- the whole rehearsal
    def run(self) -> int:
        t_start = time.monotonic()
        free = free_memory_gb()
        ok, why = memory_gate(free)
        self.rows["free_memory"] = (ok, why)
        if not ok:
            self.say("rehearse refused: " + why)
            print_table(self.rows)
            return 3
        if not port_free(self.port):
            self.say(f"rehearse refused: 127.0.0.1:{self.port} is in use")
            return 4
        stamp = time.strftime("%H%M%S")
        name = f"rehearse-{stamp}"
        space_dir = Path(lab_root()) / "spaces" / name
        self.agent_dir = space_dir / "agents"
        logs = space_dir / "logs"
        self.procs = Procs(logs, child_env(mock_backend=True))
        atexit.register(self.procs.stop_all)
        self.server_cmd = server_argv(name, self.port)
        mon = Monitor()
        mon.start()
        self.reader = Reader(self.api)
        failure = None
        self.say(f"rehearse: space {space_dir}, logs in {logs}, {why}")
        try:
            self.procs.start("server", self.server_cmd)
            if not self.api.wait_up(20):
                raise Abort("the server did not start:\n" + self.procs.tail("server"))
            self.reader.start()
            for me in PEOPLE:
                self.procs.start(f"{me}.agent", agent_argv(me, name, self.port))
            end = time.monotonic() + 30
            while not all(_agent_ready(self.agent_dir / f"{me}.json") for me in PEOPLE):
                if time.monotonic() > end:
                    raise Abort("the agents did not start:\n" + self.procs.tail("ana.agent") + "\n" + self.procs.tail("ben.agent"))
                time.sleep(0.2)
            self.procs.start("loop", loop_argv(name, self.port))
            self.wait_stage(1, "planned", 180)
            self.t0 = time.monotonic()
            self.script()
        except Abort as e:
            failure = str(e)
            self.log("ABORT: " + failure)
            for n in ("loop", "server"):
                if n in self.procs.procs:
                    self.say(f"--- last lines of {n}.log\n" + self.procs.tail(n))
        except KeyboardInterrupt:
            failure = "interrupted"
        finally:
            self.procs.stop_all()
            self.reader.stop()
            mon.stop()
        time.sleep(0.5)
        left = descendants(os.getpid())
        left = [x for x in left if not x[1].lower().startswith("conhost")] if left else left
        self.rows["no_child_left"] = (not left, "none" if not left else ", ".join(f"{e} ({p})" for p, e in left))
        for p, _e in left:
            kill_tree(p)
        self.rows["no_claude"] = (not mon.claude, "none seen among the child processes" if not mon.claude
                                  else ", ".join(sorted(mon.claude)))
        slow = max((ms for _w, ms in self.posts), default=0.0)
        worst = max(self.posts, key=lambda x: x[1])[0] if self.posts else "-"
        self.rows["post_200ms"] = (bool(self.posts) and slow <= POST_MS,
                                   f"{len(self.posts)} human POSTs, slowest {slow:.0f} ms ({worst})")
        if not self.drill:
            self.rows["drill_restart"] = (True, "skipped (--drill none)")
        self.rows.setdefault("drill_restart", (False, "the drill did not run"))

        # the recording: dump with the server's --dump, then the Node reducer with the real layout
        db = space_dir / "space.db"
        tmp_log = space_dir / LOG_NAME
        from space import server as S
        if not db.exists() or S.main(["--db", str(db), "--dump", str(tmp_log)]) != 0:
            self.say("rehearse: no database to dump")
            print_table(self.rows)
            return 2
        events = read_ndjson(tmp_log)
        try:
            reduced = node_reduce(tmp_log)
        except (RuntimeError, OSError, ValueError, subprocess.SubprocessError) as e:
            reduced = None
            self.say(f"rehearse: the Node reducer failed: {e}")
        for k, v in check_log(events, reduced, self.drill).items():
            if k == "drill_log":
                if self.drill and not v[0]:
                    self.rows["drill_restart"] = (False, self.rows["drill_restart"][1] + "; " + v[1])
                continue
            self.rows[k] = v
        if reduced is None:
            self.rows["voters_hit_or_miss"] = (False, "no Node reducer summary")
        hits = private_hits(events)
        if hits:
            self.rows["beats_in_order"] = (False, "private keys in the log: " + ", ".join(hits[:4]))
        elapsed = time.monotonic() - t_start
        self.rows["time_limit"] = (elapsed <= TIME_LIMIT_S, f"{elapsed:.0f} s (limit {TIME_LIMIT_S:.0f} s)")
        beats = find_beats(events)
        all_ok = failure is None and all(self.rows.get(n, (False,))[0] for n in ROW_NAMES)
        dest = self.out_dir if all_ok else space_dir
        dest.mkdir(parents=True, exist_ok=True)
        if dest != space_dir:
            shutil.copyfile(tmp_log, dest / LOG_NAME)
        if reduced is not None:
            hash_doc = {"log": LOG_NAME, "events": reduced.get("events"), "head": reduced.get("head"),
                        "layout_hash": reduced.get("layout_hash"), "state_hash": reduced.get("state_hash")}
            (dest / HASH_NAME).write_text(json.dumps(hash_doc, indent=1, sort_keys=True) + "\n", encoding="utf-8",
                                          newline="\n")
        beats_doc = {"log": LOG_NAME, "space": name, "batch": name, "pace": self.pace, "drill": self.drill,
                     "elapsed_s": round(elapsed, 1), "ids": self.ids, "beats": beats,
                     "rows": {k: {"ok": bool(v[0]), "detail": v[1]} for k, v in self.rows.items()},
                     "voters": (reduced or {}).get("voters"), "won": (reduced or {}).get("won")}
        (dest / BEATS_NAME).write_text(json.dumps(beats_doc, indent=1, sort_keys=True) + "\n", encoding="utf-8",
                                       newline="\n")
        self.say("")
        print_table(self.rows)
        self.say("beats:")
        print_beats(beats)
        if failure:
            self.say("rehearse FAILED: " + failure)
        self.say(("rehearse passed; recorded to " if all_ok else "rehearse FAILED; the log and tables are in ") + str(dest))
        return 0 if all_ok else 1


def _agent_ready(path: Path) -> bool:
    try:
        return json.loads(path.read_text(encoding="utf-8")).get("cursor") is not None
    except (OSError, ValueError, AttributeError):
        return False


def _nonempty(path: Path) -> bool:
    return _count_lines(path) > 0


def _count_lines(path: Path) -> int:
    try:
        return sum(1 for line in path.read_text(encoding="utf-8", errors="replace").splitlines() if line.strip())
    except OSError:
        return 0


# ---------------------------------------------------------------- --replay
def run_replay(file=None, speed: float = 50.0, seek: int = 0, port: int = C.PORT, exit_when_done: bool = False,
               say=None) -> int:
    """A fresh server on the recorded log. Prints each beat as the replay reaches it and compares the beat seqs with
    the recording. With exit_when_done it returns at once (0 when the beats match); else it serves until Ctrl-C."""
    from space import server as S
    say = say or _say
    log = Path(file) if file else RECORDED / LOG_NAME
    if not log.exists():
        say(f"replay: no recorded log at {log}; run python -m space.demo --rehearse first")
        return 2
    events = read_ndjson(log)
    ref = find_beats(events)
    total = 1 + sum(1 for e in events if e.get("kind") != "space_opened")
    name = "replay-" + time.strftime("%H%M%S")
    db = Path(lab_root()) / "spaces" / name / "space.db"
    db.parent.mkdir(parents=True, exist_ok=True)
    run = S.make(str(db), port=port, memory_dir=f"{lab_root()}/memory/_mock/{PROFILE}", replay=str(log),
                 speed=speed, seek=seek).start()
    span = (_ts(events[-1]) or 0) - (_ts(events[0]) or 0) if events else 0
    say(f"replay of {log.name} on {run.url}/ at speed {speed:g} from seq {seek}: {total} events, "
        f"about {span / max(speed, 0.001):.0f} s. The page shows the banner 'Replay of a recorded round'.")
    api = Api(run.url)
    reader = Reader(api, wait_s=2)
    reader.start()
    rc = 1
    try:
        seen = set()
        end = time.monotonic() + span / max(speed, 0.001) + 60
        while time.monotonic() < end:
            evs = reader.snapshot()
            for b in find_beats(evs):
                if b["seq"] and b["beat"] not in seen:
                    seen.add(b["beat"])
                    say("  beat %-15s (%s) at e%d" % (b["beat"], b["t"], b["seq"]))
            if reader.head >= total:
                break
            time.sleep(0.2)
        got = find_beats(reader.snapshot())
        same = beat_seqs(got) == beat_seqs(ref)
        ordered = beats_ok(got, drill=any(b["beat"] == "drill" and b["seq"] for b in ref))[0]
        rc = 0 if (same and ordered and reader.head >= total) else 1
        say(f"replay reached e{reader.head} of {total}; beat seqs {'match' if same else 'DIFFER from'} the recording"
            f"{'' if ordered else ' (out of order)'}")
        if not same:
            say("  recorded: %s\n  replayed: %s" % (beat_seqs(ref), beat_seqs(got)))
        if not exit_when_done:
            say("serving the replay until Ctrl-C")
            while True:
                time.sleep(0.5)
    except KeyboardInterrupt:
        pass
    finally:
        reader.stop()
        run.stop()
    return rc


# ---------------------------------------------------------------- --stage
HELP = ("keys: g = Go (posts run_step for the boundary the loop waits at), r = Replay (the recorded round from the "
        "current beat), k = kill and restart the server (the drill), s = status, q = quit")


class Stage:
    def __init__(self, port: int = C.PORT, live_agents: bool = False, browsers: bool = True, say=None):
        self.port, self.live, self.browsers, self.say = port, live_agents, browsers, say or _say
        self.base = f"http://{C.HOST}:{port}"
        self.api = Api(self.base)
        self.replaying = False

    def start(self) -> int:
        ok, why = memory_gate(free_memory_gb())
        if not ok:
            self.say("stage refused: " + why)
            return 3
        if not port_free(self.port):
            self.say(f"stage refused: 127.0.0.1:{self.port} is in use")
            return 4
        self.name = fresh_space_name("stage")
        self.space_dir = Path(lab_root()) / "spaces" / self.name
        self.procs = Procs(self.space_dir / "logs", child_env(mock_backend=True))
        atexit.register(self.procs.stop_all)
        self.server_cmd = server_argv(self.name, self.port)
        self.procs.start("server", self.server_cmd)
        if not self.api.wait_up(20):
            self.say("the server did not start:\n" + self.procs.tail("server"))
            self.procs.stop_all()
            return 2
        for me in PEOPLE:
            self.procs.start(f"{me}.agent", agent_argv(me, self.name, self.port, live=self.live),
                             env=child_env(mock_backend=not self.live))
        time.sleep(2.0)                                   # the agents start at the head before the loop's first event
        self.procs.start("loop", loop_argv(self.name, self.port))
        if self.browsers:
            for name, argv in browser_argv(self.base, str(self.space_dir).replace("\\", "/")):
                if os.path.exists(argv[0]):
                    self.procs.start(name, argv, env=dict(os.environ), log=False)
        self.say(f"stage {self.name}: {self.base}/  logs in {self.space_dir / 'logs'}  ({why})")
        self.say(HELP)
        return self.console()

    def key(self, k: str) -> bool:
        """One hotkey. Returns False to quit."""
        k = (k or "").strip().lower()[:1]
        if k == "q":
            return False
        if k == "g":
            if self.replaying:
                self.say("Go: the replay runs on its own; there is no loop to release")
                return True
            try:
                r = go_now(self.api)
            except (OSError, ValueError) as e:
                self.say(f"Go: server offline ({e})")
                return True
            self.say("Go: the loop is not waiting at a boundary" if r is None
                     else f"Go ({r['stage']} r{r['round']}): e{r.get('seq')}")
        elif k == "r":
            self.replay()
        elif k == "k":
            self.restart()
        elif k == "s":
            alive = {n: self.procs.alive(n) for n in self.procs.order}
            try:
                run = (self.api.call("GET", "/api/snapshot")[1] or {}).get("run")
            except (OSError, ValueError):
                run = "server offline"
            self.say(f"processes {alive}; run {run}")
        else:
            self.say(HELP)
        return True

    def restart(self):
        self.say("drill: killing the server; it comes back on the same database")
        self.procs.stop("server")
        for _ in range(20):
            self.procs.start("server", self.server_cmd)
            if self.api.wait_up(8.0):
                self.say("drill: the server is back; the browsers reconnect with ?since=<last>")
                return
            self.procs.stop("server")
            time.sleep(0.5)
        self.say("drill: the server did not come back:\n" + self.procs.tail("server"))

    def replay(self, speed: float = 30.0):
        log = RECORDED / LOG_NAME
        if not log.exists():
            self.say("Replay: no recorded log")
            return
        try:
            live = self.api.all_events()
        except (OSError, ValueError):
            live = []
        seek = current_beat_seq(live, find_beats(read_ndjson(log)))
        self.say(f"Replay: stopping the loop, the agents and the server; replaying from e{seek} at speed {speed:g}. "
                 "Say it out loud: this is a replay of a recorded round.")
        for n in ("loop", "ana.agent", "ben.agent", "server"):
            self.procs.stop(n)
        name = self.name + "-replay-" + time.strftime("%H%M%S")
        cmd = server_argv(name, self.port) + ["--replay", str(log), "--speed", f"{speed:g}", "--seek", str(seek)]
        self.server_cmd = cmd
        self.procs.start("server", cmd)
        self.say("Replay: on " + self.base + "/ " + ("(up)" if self.api.wait_up(15) else "(did not start)"))
        self.replaying = True

    def console(self) -> int:
        try:
            if os.name == "nt" and sys.stdin and sys.stdin.isatty():
                import msvcrt
                while True:
                    if msvcrt.kbhit():
                        if not self.key(msvcrt.getwch()):
                            break
                    else:
                        time.sleep(0.05)
            else:
                for line in sys.stdin:
                    if not self.key(line):
                        break
        except KeyboardInterrupt:
            pass
        finally:
            self.say("stopping every process of the stage")
            self.procs.stop_all()
        return 0


# ---------------------------------------------------------------- main
def main(argv=None) -> int:
    ap = argparse.ArgumentParser(prog="python -m space.demo", description="The HTSA shared-space demo kit (section 13).")
    mode = ap.add_mutually_exclusive_group(required=True)
    mode.add_argument("--check", action="store_true", help="the pre-stage checks")
    mode.add_argument("--stage", action="store_true", help="start everything for the stage, with the hotkey console")
    mode.add_argument("--rehearse", action="store_true", help="run the script without browsers and record it")
    mode.add_argument("--replay", action="store_true", help="serve the recorded round")
    ap.add_argument("--port", type=int, default=C.PORT)
    ap.add_argument("--live-agents", action="store_true", help="--stage: agents on Sonnet with --fallback mock")
    ap.add_argument("--no-browsers", action="store_true", help="--stage: do not open the three windows")
    ap.add_argument("--drill", choices=("restart", "none"), default=None,
                    help="--rehearse: the kill-and-restart drill at 3:30 (default restart)")
    ap.add_argument("--pace", type=float, default=1.0, help="--rehearse: 1.0 keeps the scripted seconds, 0.5 halves them")
    ap.add_argument("--out", default=None, help="--rehearse: where the recording goes (default space/recorded)")
    ap.add_argument("--file", default=None, help="--replay: the log (default space/recorded/stage_round.ndjson)")
    ap.add_argument("--speed", type=float, default=50.0, help="--replay: speed factor")
    ap.add_argument("--seek", type=int, default=0, help="--replay: write events up to this seq at once")
    ap.add_argument("--exit-when-done", action="store_true", help="--replay: exit after the last event")
    a = ap.parse_args(argv)
    if a.drill and not a.rehearse:
        ap.error("--drill goes with --rehearse (on --stage the k key runs the drill)")
    if a.live_agents and not a.stage:
        ap.error("--live-agents goes with --stage only: the rehearsal never calls a model")
    if a.check:
        return run_check(a.port)
    if a.rehearse:
        return Rehearsal(a.port, a.drill or "restart", a.pace, a.out).run()
    if a.replay:
        return run_replay(a.file, a.speed, a.seek, a.port, a.exit_when_done)
    return Stage(a.port, a.live_agents, not a.no_browsers).start()


if __name__ == "__main__":
    sys.exit(main())
