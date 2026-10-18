"""Start a research from the page (part P8, start-run). Standard library only.

A person picks a profile, a size preset and Mock or Real; the server spawns the loop detached, writes its output to
HTSA_LAB_ROOT/spaces/<space>/runs/<batch>.log, records the run in runs.json next to the log, and posts a
run_started and a run_finished event (as note_posted by the server while contract.KINDS has no run kinds).

Routes (added to the server by register(httpd)):
    GET  /api/run/profiles                      the profiles, the presets and their estimates
    GET  /api/run/estimate?preset=&profile=     calls, Fable tokens and minutes for one preset
    POST /api/run/start {preset, profile, mode, confirm}
    GET  /api/run/status                        every run: alive, rc, run_dir, the last 20 log lines
    POST /api/run/stop {batch}                  ends the process tree (taskkill /T /PID)

A real run needs confirm true in the body (else 400 with the estimate). One run at a time (else 409 run_alive),
because the owner's PC crashed under parallel load.
"""
from __future__ import annotations

import json
import os
import re
import subprocess
import sys
import threading
import time
from pathlib import Path

from space import contract
from space.store import Reject
from harness import labroot as _labroot  # noqa: E402  (the lab folder, on any computer)

REPO = Path(__file__).resolve().parent.parent
PYTHON = r"D:\AGI-lab\.venv\Scripts\python.exe"
if not os.path.exists(PYTHON):          # another computer: the interpreter that runs the server
    PYTHON = sys.executable
PROFILES_DIR = REPO / "nano" / "profiles"
MODES = ("mock", "real")
TAIL_LINES = 20
TAIL_BYTES = 32768

# rounds, builds per round, idea agents per round (None: no cap), the inventing model's token budget
PRESETS = {
    # demo: the whole loop on Haiku in a few minutes, to show the team at work; not research quality
    "demo": {"rounds": 1, "implement": 1, "max_sketch_calls": 4, "budget": 300_000, "model": "haiku",
             "note": "Demo only: every role runs on Haiku, one round, four idea agents, one build. Fast and cheap; "
                     "the ideas and the judging are not research quality. Use it on stage, not for results."},
    "small": {"rounds": 1, "implement": 2, "max_sketch_calls": 8, "budget": 600_000},
    "medium": {"rounds": 2, "implement": 4, "max_sketch_calls": 16, "budget": 2_000_000},
    "big": {"rounds": 3, "implement": 10, "max_sketch_calls": None, "budget": 5_000_000},
}
PRESET_ORDER = ("demo", "small", "medium", "big")
REAL_MODEL = "fable"           # the inventing model of a real run; the loop's own default would be the cheap model
JUDGE_MODEL = "opus"                      # the blind panel of a folder profile: a model apart from the inventing one

# Measured on past runs: Fable tokens per call kind, minutes per call, calls in parallel.
SKETCH_TOKENS, CHAIN_TOKENS, BUILD_TOKENS = 65_000, 40_000, 35_000
MINUTES_PER_CALL, PARALLEL = 2.5, 6
UNCAPPED_SKETCHES = 22                 # what the loop sends per round without a sketch cap (the big preset)
MAX_CHAINS = 6                         # critic chains per round

PROFILE_NOTES = {"llm": "trains a small model on the GPU, also in mock mode"}
DEFAULT_PROFILE = "binpack_nobase"

_GOAL_RE = re.compile(r"""["']goal_short["']\s*:\s*\(?\s*["']([^"']*)["']""")


# ---------------------------------------------------------------- pure parts: profiles, estimate, command
def profiles() -> list[dict]:
    """The profiles under nano/profiles with their goal_short (read as text: importing llm.py would load torch)."""
    out = []
    for p in sorted(PROFILES_DIR.glob("*.py")):
        if p.name.startswith("_"):
            continue
        try:
            m = _GOAL_RE.search(p.read_text(encoding="utf-8", errors="replace"))
        except OSError:
            m = None
        out.append({"name": p.stem, "goal_short": m.group(1) if m else "", "note": PROFILE_NOTES.get(p.stem, ""),
                    "custom": p.stem.startswith("custom_")})
    out.sort(key=lambda r: (r["custom"], r["name"]))
    return out


def profile_names() -> list[str]:
    return [p["name"] for p in profiles()]


def _preset(preset) -> dict:
    if not isinstance(preset, str) or preset not in PRESETS:          # a list or dict body value is no preset
        raise Reject(422, "bad_preset", preset=preset if isinstance(preset, str) else None, presets=list(PRESET_ORDER))
    return PRESETS[preset]


def estimate(preset, profile=None, overrides=None) -> dict:
    """Calls, Fable tokens and minutes for one preset. Per round: `sketches` idea agents, min(6, sketches) critic
    chains of three calls and `builds` builds of two calls; plus two planning calls per run. Tokens stop at the
    preset's budget. Minutes: 2.5 per call with 6 calls in parallel."""
    p = dict(_preset(preset), **(overrides or {}))
    rounds, builds = p["rounds"], p["implement"]
    sketches = p["max_sketch_calls"] or UNCAPPED_SKETCHES
    chains = min(MAX_CHAINS, sketches)
    calls = 2 + rounds * (sketches + chains * 3 + builds * 2)
    raw = rounds * (sketches * SKETCH_TOKENS + chains * CHAIN_TOKENS + builds * BUILD_TOKENS)
    tokens = min(raw, p["budget"])
    model = p.get("model") or REAL_MODEL
    minutes = round(calls * MINUTES_PER_CALL / PARALLEL * (0.4 if p.get("model") == "haiku" else 1.0))
    return {"preset": preset, "profile": profile, "rounds": rounds, "sketches": sketches, "chains": chains,
            "builds": builds, "calls": calls, "tokens": tokens, "tokens_uncapped": raw, "capped": raw > p["budget"],
            "budget": p["budget"], "minutes": max(1, minutes), "model": model, "demo": bool(p.get("model")),
            "note": p.get("note", "")}


def estimate_words(e: dict) -> str:
    """The estimate in one sentence (the confirm step and the 400 answer repeat it)."""
    cap = " (the budget stops it there)" if e["capped"] else ""
    if e.get("demo"):
        return ("A demo run on Haiku: about %d model calls, a few minutes, %d round, %d idea agents and %d build. "
                "For showing the team at work, not for results." % (e["calls"], e["rounds"], e["sketches"], e["builds"]))
    return ("A real run makes about %d model calls, spends up to %s Fable tokens%s and takes about %d minutes "
            "(%d round%s, %d idea agents and %d builds per round)."
            % (e["calls"], "{:,}".format(e["tokens"]), cap, e["minutes"], e["rounds"], "" if e["rounds"] == 1 else "s",
               e["sketches"], e["builds"]))


def clean_overrides(o) -> dict:
    """{rounds, pause_every} from a request body: ints in range, or nothing."""
    out = {}
    if isinstance(o, dict):
        r = o.get("rounds")
        if isinstance(r, (int, float)) and not isinstance(r, bool) and 1 <= int(r) <= 12:
            out["rounds"] = int(r)
        pe = o.get("pause_every")
        if isinstance(pe, (int, float)) and not isinstance(pe, bool) and 0 <= int(pe) <= 12:
            out["pause_every"] = int(pe)
    return out


def command(preset, profile, mode, batch, space_url, overrides=None) -> list[str]:
    """The exact argv of a run. Mock: nano.dry_run (no model, no spend). Real: nano.loop with the preset's budget.
    overrides: rounds (replaces the preset's) and pause_every (a wait for Go after every Nth round)."""
    p = dict(_preset(preset), **(overrides or {}))
    pause = ["--pause-every-rounds", str(int(p["pause_every"]))] if p.get("pause_every") else []
    if mode == "mock":
        cap = p["max_sketch_calls"] or UNCAPPED_SKETCHES
        return [PYTHON, "-m", "nano.dry_run", "--profile", profile, "--batch", batch, "--implement", str(p["implement"]),
                "--rounds", str(p["rounds"]), "--max-sketch-calls", str(cap), "--space", space_url] + pause
    if mode == "real":
        cmd = [PYTHON, "-m", "nano.loop", "--profile", profile, "--batch", batch, "--implement", str(p["implement"]),
               "--rounds", str(p["rounds"])]
        if p["max_sketch_calls"]:
            cmd += ["--max-sketch-calls", str(p["max_sketch_calls"])]
        model = p.get("model") or REAL_MODEL
        cmd += ["--model", model]
        if p.get("model"):                                   # a demo run: the cheap roles on it too; the judges on another
            cmd += ["--research-model", model, "--cheap-model", model, "--judge-model", "sonnet" if model != "sonnet" else "haiku"]
        else:                                                # a real run: the panel judges (a folder profile has no objective
            cmd += ["--judge-model", JUDGE_MODEL if model != JUDGE_MODEL else "sonnet"]   # check) must not be the inventing model
        return cmd + ["--budget", str(p["budget"]), "--space", space_url] + pause
    raise Reject(422, "bad_mode", mode=mode if isinstance(mode, str) else None, modes=list(MODES))


# ---------------------------------------------------------------- processes (Windows first, POSIX fallback)
def _win_proc(pid: int):
    """(exists, still running, creation time as an int or None) through kernel32."""
    import ctypes
    from ctypes import wintypes
    k32 = ctypes.WinDLL("kernel32", use_last_error=True)
    k32.OpenProcess.restype = wintypes.HANDLE
    k32.OpenProcess.argtypes = (wintypes.DWORD, wintypes.BOOL, wintypes.DWORD)
    k32.GetExitCodeProcess.argtypes = (wintypes.HANDLE, ctypes.POINTER(wintypes.DWORD))
    k32.GetProcessTimes.argtypes = (wintypes.HANDLE,) + (ctypes.POINTER(wintypes.FILETIME),) * 4
    k32.CloseHandle.argtypes = (wintypes.HANDLE,)
    h = k32.OpenProcess(0x1000, False, int(pid))          # PROCESS_QUERY_LIMITED_INFORMATION
    if not h:
        return False, False, None
    try:
        code = wintypes.DWORD()
        running = bool(k32.GetExitCodeProcess(h, ctypes.byref(code))) and code.value == 259     # STILL_ACTIVE
        ft = [wintypes.FILETIME() for _ in range(4)]
        created = None
        if k32.GetProcessTimes(h, *[ctypes.byref(f) for f in ft]):
            created = (ft[0].dwHighDateTime << 32) | ft[0].dwLowDateTime
        return True, running, created
    finally:
        k32.CloseHandle(h)


def proc_created(pid) -> int | None:
    """The creation time of a live process (Windows), so a reused pid is never taken for the run."""
    if not pid or os.name != "nt":
        return None
    try:
        return _win_proc(pid)[2]
    except (OSError, AttributeError, ValueError):
        return None


def pid_alive(pid, created=None) -> bool:
    """True while the process runs. With `created`, a reused pid (another process) counts as dead."""
    try:
        pid = int(pid or 0)
    except (TypeError, ValueError):
        return False
    if pid <= 0:
        return False
    if os.name == "nt":
        try:
            exists, running, ctime = _win_proc(pid)
        except (OSError, AttributeError, ValueError):
            return False
        if not (exists and running):
            return False
        return created is None or ctime is None or ctime == created
    try:
        os.kill(pid, 0)
    except OSError:
        return False
    return True


def kill_tree(pid) -> bool:
    """End a process and its children (taskkill /T /F /PID). Harmless on a dead pid: returns False."""
    try:
        pid = int(pid or 0)
    except (TypeError, ValueError):
        return False
    if pid <= 0:
        return False
    if os.name == "nt":
        try:
            r = subprocess.run(["taskkill", "/T", "/F", "/PID", str(pid)], capture_output=True, timeout=20,
                               creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0))
            return r.returncode == 0
        except (OSError, subprocess.SubprocessError):
            return False
    try:
        os.killpg(pid, 15)
        return True
    except OSError:
        return False


def tail(path, n: int = TAIL_LINES) -> list[str]:
    """The last n lines of a log (read from its last 32 KB)."""
    if not path:
        return []
    try:
        with open(path, "rb") as f:
            f.seek(0, 2)
            size = f.tell()
            f.seek(max(0, size - TAIL_BYTES))
            data = f.read()
    except OSError:
        return []
    lines = data.decode("utf-8", errors="replace").replace("\r\n", "\n").replace("\r", "\n").split("\n")
    if size > TAIL_BYTES:
        lines = lines[1:]                                   # the first line may be cut
    while lines and not lines[-1].strip():
        lines.pop()
    return lines[-n:]


# ---------------------------------------------------------------- the launcher: one per server
def space_name(db_path) -> str:
    """spaces/<name>/space.db gives <name>; any other file gives its stem."""
    p = Path(str(db_path))
    name = p.parent.name if p.stem == "space" and p.parent.name else p.stem
    return re.sub(r"[^A-Za-z0-9_.-]", "_", name) or "space"


def lab_root() -> Path:
    return _labroot.lab_root()


def live_of(run_dir) -> dict | None:
    """The loop's live.json: phase, note, spent, spent_aux, how many calls are in flight, and how old it is."""
    if not run_dir:
        return None
    try:
        d = json.loads(open(os.path.join(run_dir, "live.json"), encoding="utf-8").read())
    except (OSError, ValueError):
        return None
    if not isinstance(d, dict):
        return None
    inflight = d.get("inflight") if isinstance(d.get("inflight"), list) else []
    age = None
    try:
        age = max(0, int(time.time() - float(d.get("ts") or 0))) if d.get("ts") else None
    except (TypeError, ValueError):
        age = None
    return {"phase": d.get("phase"), "note": d.get("note"), "spent": d.get("spent"), "spent_aux": d.get("spent_aux"),
            "inflight": len(inflight), "roles": sorted({str(c.get("role")) for c in inflight if isinstance(c, dict)}),
            "age_s": age}


def elapsed_s(started, finished=None) -> int | None:
    try:
        t0 = time.mktime(time.strptime(str(started)[:19], "%Y-%m-%dT%H:%M:%S"))
        t1 = time.mktime(time.strptime(str(finished)[:19], "%Y-%m-%dT%H:%M:%S")) if finished else time.time()
        return max(0, int(t1 - t0))
    except (TypeError, ValueError):
        return None


def error_line(tail_lines, stopped=False) -> str:
    """The line of the log that says why a run failed, or a plain sentence."""
    if stopped:
        return "stopped by a person"
    lines = [str(x) for x in (tail_lines or []) if str(x).strip()]
    for line in reversed(lines):
        low = line.lower()
        if any(k in low for k in ("error", "traceback", "exception", "quota", "rate limit", "budget", "killed", "refused")):
            return line.strip()[:300]
    return (lines[-1].strip()[:300] if lines else "the run ended without a report")


def _now() -> str:
    return time.strftime("%Y-%m-%dT%H:%M:%S")


class Launcher:
    """Starts, watches and stops the runs of one space. Paths are resolved at call time (HTSA_LAB_ROOT)."""

    def __init__(self, db_path, space_url: str, space=None):
        self.db_path, self.space_url, self.space = str(db_path), space_url, space
        self.lock = threading.RLock()
        self.procs: dict[str, subprocess.Popen] = {}
        self.overrides: dict = {}          # tests only, e.g. {"implement": 1, "max_sketch_calls": 4}

    # ---- files
    @property
    def runs_dir(self) -> Path:
        return lab_root() / "spaces" / space_name(self.db_path) / "runs"

    def _load(self) -> list[dict]:
        try:
            rows = json.loads((self.runs_dir / "runs.json").read_text(encoding="utf-8"))
        except (OSError, ValueError):
            return []
        return [r for r in rows if isinstance(r, dict) and r.get("batch")] if isinstance(rows, list) else []

    def _save(self, rows: list[dict]) -> None:
        d = self.runs_dir
        d.mkdir(parents=True, exist_ok=True)
        tmp = d / "runs.json.tmp"
        tmp.write_text(json.dumps(rows, indent=1), encoding="utf-8")
        os.replace(tmp, d / "runs.json")

    # ---- events (note_posted by the server until contract.KINDS has run_started and run_finished)
    def _post(self, what: str, rec: dict, text: str) -> None:
        sp = self.space
        if sp is None:
            return
        kind = what if what in contract.KINDS else "note_posted"
        data = {"text": text[:contract.NOTE_CAP], "event": what, "batch": rec["batch"], "preset": rec.get("preset"),
                "profile": rec.get("profile"), "mode": rec.get("mode")}
        if what == "run_finished":
            data["rc"] = rec.get("rc")
            data["state"] = self._state(rec, False)
        try:
            sp.store.append("server", "system", {"kind": kind, "owner": "server", "subject": "run:" + rec["batch"],
                                                 "label": what.replace("_", " "), "data": data})
        except Exception:                                   # a closing server never fails the run
            pass

    # ---- start
    def start(self, preset, profile, mode="mock", confirm=False, problem=None, overrides=None) -> dict:
        overrides = clean_overrides(overrides)
        if isinstance(problem, dict) and str(problem.get("goal") or problem.get("title") or "").strip():
            from nano.profiles._custom import write_profile
            from space.knowledge import Knowledge
            spec = {k: str(problem.get(k) or "")[:6000] for k in ("title", "goal", "success", "known", "fixed", "parts", "field", "deep")}
            try:
                kn = Knowledge(Path(self.db_path).parent) if getattr(self, "db_path", None) else None
                if kn is not None:
                    paths = kn.write_problem(problem)
                    spec["knowledge_facts"] = paths["facts"]
                    spec["knowledge_problem"] = paths["problem"]
                profile = write_profile(spec)
            except OSError as e:
                raise Reject(500, "profile_not_written", detail=str(e)[:200])
        est = estimate(preset, profile, overrides)
        if mode not in MODES:
            raise Reject(422, "bad_mode", mode=mode if isinstance(mode, str) else None, modes=list(MODES))
        if profile not in profile_names():
            raise Reject(422, "bad_profile", profile=profile if isinstance(profile, str) else None,
                         profiles=profile_names())
        if mode == "real" and confirm is not True:
            raise Reject(400, "confirm_needed", estimate=est, words=estimate_words(est))
        with self.lock:
            live = [r["batch"] for r in self.status()["runs"] if r["alive"]]
            if live:
                raise Reject(409, "run_alive", batch=live[0])
            batch = self._new_batch(preset)
            cmd = command(preset, profile, mode, batch, self.space_url, dict(self.overrides or {}, **overrides))
            d = self.runs_dir
            d.mkdir(parents=True, exist_ok=True)
            log = d / (batch + ".log")
            env = dict(os.environ, HTSA_LAB_ROOT=str(lab_root()), PYTHONUNBUFFERED="1", PYTHONIOENCODING="utf-8")
            if mode == "mock":
                env["HTSA_BACKEND"] = "mock"
            if not env.get("HTSA_EXEC_PYTHON"):                # candidate scripts: a temp lab root has no venv
                env["HTSA_EXEC_PYTHON"] = PYTHON if os.path.exists(PYTHON) else sys.executable
            if os.name == "nt":
                kw = {"creationflags": subprocess.CREATE_NEW_PROCESS_GROUP | subprocess.CREATE_NO_WINDOW}
            else:
                kw = {"start_new_session": True}
            with open(log, "ab") as out:
                out.write(("$ %s\n" % " ".join(cmd)).encode("utf-8"))
                out.flush()
                try:
                    proc = subprocess.Popen(cmd, cwd=str(REPO), env=env, stdin=subprocess.DEVNULL, stdout=out,
                                            stderr=subprocess.STDOUT, **kw)
                except OSError as e:                    # the server re-raises OSError: answer here, not with silence
                    raise Reject(500, "spawn_failed", detail=str(e)[:300])
            rec = {"batch": batch, "pid": proc.pid, "created": proc_created(proc.pid), "preset": preset,
                   "profile": profile, "mode": mode, "cmd": cmd, "started": _now(), "log": str(log), "overrides": overrides,
                   "run_dir": None, "rc": None, "finished": None, "stopped": False, "estimate": est}
            rows = self._load()
            rows.append(rec)
            self._save(rows)
            self.procs[batch] = proc
        self._post("run_started", rec, "Run %s started: %s, %s preset, profile %s, about %d calls and %d minutes." % (
            batch, mode, preset, profile, est["calls"], est["minutes"]))
        threading.Thread(target=self._watch, args=(batch, proc), name="run-" + batch, daemon=True).start()
        return self._view(rec)

    def _new_batch(self, preset: str) -> str:
        used = {r["batch"] for r in self._load()}
        stem = "space-%s-%s" % (preset, time.strftime("%m%d-%H%M%S"))
        batch, n = stem, 1
        while batch in used or (self.runs_dir / (batch + ".log")).exists():
            n += 1
            batch = "%s-%d" % (stem, n)
        return batch

    # ---- finish
    def _watch(self, batch: str, proc: subprocess.Popen) -> None:
        self._finish(batch, proc.wait())

    def _finish(self, batch: str, rc) -> None:
        with self.lock:
            rows = self._load()
            rec = next((r for r in rows if r["batch"] == batch), None)
            if rec is None or rec.get("finished"):
                return
            rec["rc"], rec["finished"] = rc, _now()
            rec["run_dir"] = rec.get("run_dir") or self._run_dir(batch)
            self._save(rows)
            self.procs.pop(batch, None)
        state = self._state(rec, False)
        self._post("run_finished", rec, "Run %s %s%s." % (
            batch, state, " (exit code unknown)" if rc is None else " (exit code %s)" % rc))

    def report(self, batch) -> dict:
        """The run's REPORT.md as text, with its path."""
        with self.lock:
            rec = next((r for r in self._load() if r["batch"] == batch), None)
        if rec is None:
            raise Reject(404, "no_run", batch=batch)
        rd = rec.get("run_dir") or self._run_dir(batch)
        path = os.path.join(rd, "REPORT.md") if rd else None
        if not path or not os.path.exists(path):
            raise Reject(404, "no_report", batch=batch)
        try:
            text = open(path, encoding="utf-8", errors="replace").read()
        except OSError as e:
            raise Reject(500, "unreadable", detail=str(e)[:200])
        return {"batch": batch, "path": path, "text": text[:400_000]}

    @staticmethod
    def _run_dir(batch: str) -> str | None:
        try:
            hits = sorted((lab_root() / "runs").glob(batch + "__*"))
        except OSError:
            hits = []
        return str(hits[0]) if hits else None

    @staticmethod
    def _state(rec: dict, alive: bool) -> str:
        if alive:
            return "running"
        if rec.get("stopped"):
            return "stopped"
        return "finished" if rec.get("rc") == 0 else "failed"

    def _alive(self, rec: dict) -> bool:
        proc = self.procs.get(rec["batch"])
        if proc is not None:
            return proc.poll() is None
        return pid_alive(rec.get("pid"), rec.get("created"))

    def _view(self, rec: dict) -> dict:
        alive = self._alive(rec)
        v = dict(rec, alive=alive, state=self._state(rec, alive), tail=tail(rec.get("log")))
        if not v.get("run_dir"):
            v["run_dir"] = self._run_dir(rec["batch"])
        v["live"] = live_of(v.get("run_dir"))
        v["report"] = bool(v.get("run_dir")) and os.path.exists(os.path.join(v["run_dir"], "REPORT.md"))
        v["elapsed_s"] = elapsed_s(rec.get("started"), rec.get("finished"))
        v["error"] = None if alive or rec.get("rc") == 0 else error_line(v.get("tail"), rec.get("stopped"))
        return v

    # ---- status and stop
    def status(self) -> dict:
        with self.lock:
            rows = self._load()
            out = []
            for rec in rows:
                if not rec.get("finished") and rec["batch"] not in self.procs and not self._alive(rec):
                    self._finish(rec["batch"], None)        # ended while no server watched it: exit code unknown
                    rec = next((r for r in self._load() if r["batch"] == rec["batch"]), rec)
                out.append(self._view(rec))
        out.reverse()                                       # newest first
        return {"runs": out, "alive": any(r["alive"] for r in out)}

    def _mark_stopped(self, batch: str, value: bool) -> None:
        with self.lock:
            rows = self._load()
            for r in rows:
                if r["batch"] == batch and not r.get("finished"):
                    r["stopped"] = value
            self._save(rows)

    def resume(self, batch) -> dict:
        """Continue a failed or stopped run from its last saved stage: the same command with --resume, the same
        run folder. The loop redoes the interrupted round from its first incomplete stage; nothing done is lost."""
        with self.lock:
            rows = self._load()
            rec = next((r for r in rows if r["batch"] == batch), None)
            if rec is None:
                raise Reject(404, "no_run", batch=batch)
            if self._alive(rec):
                raise Reject(409, "run_alive", batch=batch)
            if any(self._alive(r) for r in rows):
                raise Reject(409, "run_alive", batch=next(r["batch"] for r in rows if self._alive(r)))
            cmd = list(rec.get("cmd") or [])
            if not cmd:
                raise Reject(422, "no_command", batch=batch)
            if "--resume" not in cmd:
                cmd.append("--resume")
            if "--space" in cmd and cmd.index("--space") + 1 < len(cmd):            # the space may have woken on another port
                cmd[cmd.index("--space") + 1] = self.space_url
            if "nano.loop" in cmd and "--judge-model" not in cmd and "--model" in cmd:   # a run recorded before the judge flag
                gen = cmd[cmd.index("--model") + 1]
                cmd += ["--judge-model", JUDGE_MODEL if gen != JUDGE_MODEL else "sonnet"]
            log = Path(rec.get("log") or (self.runs_dir / (batch + ".log")))
            env = dict(os.environ, HTSA_LAB_ROOT=str(lab_root()), PYTHONUNBUFFERED="1", PYTHONIOENCODING="utf-8")
            if rec.get("mode") == "mock":
                env["HTSA_BACKEND"] = "mock"
            if not env.get("HTSA_EXEC_PYTHON"):
                env["HTSA_EXEC_PYTHON"] = PYTHON if os.path.exists(PYTHON) else sys.executable
            kw = ({"creationflags": subprocess.CREATE_NEW_PROCESS_GROUP | subprocess.CREATE_NO_WINDOW} if os.name == "nt"
                  else {"start_new_session": True})
            log.parent.mkdir(parents=True, exist_ok=True)
            with open(log, "ab") as out:
                out.write(("\n$ %s   (continued %s)\n" % (" ".join(cmd), _now())).encode("utf-8"))
                out.flush()
                try:
                    proc = subprocess.Popen(cmd, cwd=str(REPO), env=env, stdin=subprocess.DEVNULL, stdout=out,
                                            stderr=subprocess.STDOUT, **kw)
                except OSError as e:
                    raise Reject(500, "spawn_failed", detail=str(e)[:300])
            rec.update({"pid": proc.pid, "created": proc_created(proc.pid), "cmd": cmd, "rc": None, "finished": None,
                        "stopped": False, "resumed": int(rec.get("resumed") or 0) + 1, "resumed_at": _now()})
            self._save(rows)
            self.procs[batch] = proc
        self._post("run_started", rec, "Run %s continues from its last saved stage." % batch)
        threading.Thread(target=self._watch, args=(batch, proc), name="run-" + batch, daemon=True).start()
        return self._view(rec)

    def stop(self, batch) -> dict:
        with self.lock:
            rec = next((r for r in self._load() if r["batch"] == batch), None)
        if rec is None:
            raise Reject(404, "no_run", batch=batch)
        alive = self._alive(rec)
        if alive:                                           # mark first: the watcher's run_finished must say stopped
            self._mark_stopped(batch, True)
        killed = kill_tree(rec["pid"]) if alive else False   # never signal a pid that is no longer this run
        if alive and not killed and self._alive(rec):
            self._mark_stopped(batch, False)                # the kill failed and the run goes on
        if alive:
            proc = self.procs.get(batch)
            if proc is not None:
                try:
                    proc.wait(timeout=10)
                except subprocess.TimeoutExpired:
                    pass
        return {"ok": True, "batch": batch, "was_alive": alive, "killed": killed}


# ---------------------------------------------------------------- the server hook
def _one(q, name: str, default=None):
    v = (q or {}).get(name)
    if isinstance(v, list):
        return v[0] if v else default
    return v if isinstance(v, str) else default


def register(httpd) -> Launcher:
    """Add the /api/run/* routes to a SpaceServer: httpd.routes[(method, path)] = fn(body, query) -> dict.
    A handler raises Reject for an error answer."""
    host, port = httpd.server_address[:2]
    url = "http://%s:%d" % ("127.0.0.1" if host in ("0.0.0.0", "") else host, port)
    sp = getattr(httpd, "space", None)
    la = Launcher(sp.store.path if sp is not None else "space.db", url, sp)
    httpd.launcher = la

    def body_of(b) -> dict:
        if not isinstance(b, dict):
            raise Reject(422, "bad_envelope")
        return b

    def profiles_route(b, q):
        return {"profiles": profiles(), "default_profile": DEFAULT_PROFILE, "modes": list(MODES),
                "order": list(PRESET_ORDER),
                "presets": {k: dict(PRESETS[k], estimate=estimate(k), words=estimate_words(estimate(k)))
                            for k in PRESET_ORDER}}

    def estimate_route(b, q):
        ov = {}
        for k in ("rounds", "pause_every"):
            v = _one(q, k)
            if v not in (None, ""):
                try:
                    ov[k] = int(v)
                except ValueError:
                    pass
        e = estimate(_one(q, "preset", "small"), _one(q, "profile"), clean_overrides(ov))
        return dict(e, words=estimate_words(e))

    def start_route(b, q):
        b = body_of(b)
        return la.start(b.get("preset", "small"), b.get("profile") or DEFAULT_PROFILE, b.get("mode", "mock"),
                        b.get("confirm") is True, b.get("problem") if isinstance(b.get("problem"), dict) else None,
                        b.get("overrides") if isinstance(b.get("overrides"), dict) else None)

    def status_route(b, q):
        return la.status()

    def report_route(b, q):
        return la.report(str(_one(q, "batch") or ""))

    TEXT_OK = (".md", ".txt", ".jsonl", ".json", ".py", ".log", ".csv", ".yaml", ".yml", ".toml", ".ini", ".html")

    def files_route(b, q):
        batch = str(_one(q, "batch") or "")
        with la.lock:
            rec = next((r for r in la._load() if r["batch"] == batch), None)
        if rec is None:
            raise Reject(404, "no_run", batch=batch)
        rd = rec.get("run_dir") or la._run_dir(batch)
        if not rd or not os.path.isdir(rd):
            raise Reject(404, "no_run_dir", batch=batch)
        root = Path(rd).resolve()
        rel = str(_one(q, "path") or "").replace("\\", "/").lstrip("/")
        if rel:
            p = (root / rel).resolve()
            if root not in p.parents or not p.is_file():
                raise Reject(404, "no_file")
            if p.suffix.lower() not in TEXT_OK:
                raise Reject(415, "not_text")
            try:
                text = p.read_text(encoding="utf-8", errors="replace")
            except OSError as e:
                raise Reject(500, "unreadable", detail=str(e)[:200])
            return {"batch": batch, "path": rel, "bytes": p.stat().st_size, "text": text[:400_000], "cut": len(text) > 400_000}
        out = []
        skip = {"private", "__pycache__"}
        for p in sorted(root.rglob("*")):
            parts = p.relative_to(root).parts
            if any(x in skip for x in parts) or not p.is_file():
                continue
            if p.suffix.lower() not in TEXT_OK:
                continue
            out.append({"path": p.relative_to(root).as_posix(), "bytes": p.stat().st_size})
            if len(out) >= 2000:
                break
        return {"batch": batch, "run_dir": str(root), "files": out}

    def _run_root(batch: str) -> Path:
        with la.lock:
            rec = next((r for r in la._load() if r["batch"] == batch), None)
        if rec is None:
            raise Reject(404, "no_run", batch=batch)
        rd = rec.get("run_dir") or la._run_dir(batch)
        if not rd or not os.path.isdir(rd):
            raise Reject(404, "no_run_dir", batch=batch)
        return Path(rd).resolve()

    def cand_route(b, q):
        """The built artifact of one candidate and every test record about it."""
        batch, cand = str(_one(q, "batch") or ""), re.sub(r"[^A-Za-z0-9_-]", "", str(_one(q, "cand") or ""))
        root = _run_root(batch)
        if not cand:
            raise Reject(422, "no_cand")
        arts = []
        for pth in sorted((root / "cands").rglob(f"*{cand}*")) if (root / "cands").is_dir() else []:
            if pth.is_file() and pth.suffix.lower() in TEXT_OK and pth.suffix.lower() != ".jsonl":
                try:
                    arts.append({"path": pth.relative_to(root).as_posix(), "text": pth.read_text(encoding="utf-8", errors="replace")[:200_000]})
                except OSError:
                    continue
        tests = []
        vf = root / "verify.jsonl"
        if vf.is_file():
            for line in vf.read_text(encoding="utf-8", errors="replace").splitlines():
                try:
                    row = json.loads(line)
                except ValueError:
                    continue
                if row.get("id") != cand:
                    continue
                fb = row.get("feedback_record") if isinstance(row.get("feedback_record"), dict) else {}
                tests.append({"status": row.get("status"), "rung": fb.get("rung") if fb else row.get("rung"), "reason": fb.get("reason") or row.get("reason"),
                              "rc": fb.get("rc"), "stderr": str(fb.get("stderr") or "")[-3000:], "stdout": str(fb.get("stdout") or "")[-3000:],
                              "metrics": fb.get("metrics") or row.get("metrics") or {}, "partial_score": row.get("partial_score"),
                              "attempts": row.get("attempts"), "ts": row.get("ts")})
        hyp = None
        for pth in (root / "cands").glob("*.jsonl") if (root / "cands").is_dir() else []:
            try:
                for line in pth.read_text(encoding="utf-8", errors="replace").splitlines():
                    if cand in line:
                        row = json.loads(line)
                        hyp = {k: row.get(k) for k in ("hypothesis", "change", "fidelity", "node", "idea", "round", "lane") if row.get(k) is not None}
                        break
            except (OSError, ValueError):
                continue
            if hyp:
                break
        return {"batch": batch, "cand": cand, "artifacts": arts, "tests": tests, "record": hyp}

    def plan_route(b, q):
        """How the map was drawn: the planner's prompt and reply, and the reading before it."""
        batch = str(_one(q, "batch") or "")
        root = _run_root(batch)
        out = {"batch": batch, "plan": None, "preread": None, "repair": None}
        for pth in sorted((root / "calls").glob("*.json")) if (root / "calls").is_dir() else []:
            try:
                j = json.loads(pth.read_text(encoding="utf-8", errors="replace"))
            except (OSError, ValueError):
                continue
            card = str((j.get("meta") or {}).get("card") or "")
            key = {"plan": "plan", "preread": "preread", "plan_repair": "repair"}.get(card)
            if not key or out[key] is not None:
                continue
            prompt = ""
            pp = root / "prompts" / f"{j.get('call_id')}.txt"
            if pp.is_file():
                try:
                    prompt = pp.read_text(encoding="utf-8", errors="replace")[:60_000]
                except OSError:
                    prompt = ""
            out[key] = {"call_id": j.get("call_id"), "model": j.get("model"), "reply": str(j.get("text") or "")[:60_000], "prompt": prompt,
                        "error": j.get("error"), "duration_ms": j.get("duration_ms")}
        tree = root / "problem_tree.json"
        if tree.is_file():
            try:
                out["tree"] = json.loads(tree.read_text(encoding="utf-8", errors="replace"))
            except (OSError, ValueError):
                out["tree"] = None
        return out

    def knowledge_route(b, q):
        from space.knowledge import Knowledge
        if sp is None:
            raise Reject(503, "no_space")
        kn = Knowledge(Path(sp.store.path).parent)
        rel = _one(q, "path")
        if rel:
            return kn.read(rel)
        return kn.rebuild(sp.store.events())

    def structure_route(b, q):
        b = body_of(b)
        from space import files as filestore, structure as structurer
        fs = filestore.Files(Path(sp.store.path).parent) if sp is not None else None
        if fs is None:
            raise Reject(503, "no_space")
        ids = b.get("file_ids") if isinstance(b.get("file_ids"), list) else []
        return structurer.structure(fs, [str(x) for x in ids][:40], str(b.get("notes") or ""))

    def stop_route(b, q):
        return la.stop(str(body_of(b).get("batch") or ""))

    def resume_route(b, q):
        return la.resume(str(body_of(b).get("batch") or ""))

    routes = getattr(httpd, "routes", None)
    if routes is None:
        routes = httpd.routes = {}
    routes.update({("GET", "/api/run/profiles"): profiles_route, ("GET", "/api/run/estimate"): estimate_route,
                   ("POST", "/api/run/start"): start_route, ("GET", "/api/run/status"): status_route,
                   ("POST", "/api/run/stop"): stop_route, ("POST", "/api/run/resume"): resume_route, ("GET", "/api/run/report"): report_route,
                   ("POST", "/api/run/structure"): structure_route, ("GET", "/api/knowledge"): knowledge_route,
                   ("GET", "/api/run/files"): files_route, ("GET", "/api/run/cand"): cand_route,
                   ("GET", "/api/run/plan"): plan_route})
    return la


if __name__ == "__main__":                                  # python -m space.launch prints the presets and estimates
    for k in PRESET_ORDER:
        print(k, json.dumps(estimate(k)), file=sys.stdout)
