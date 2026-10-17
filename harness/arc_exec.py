"""Execution of untrusted ARC candidate programs (ARCHITECTURE.md section 3 /verify, steps 1 and 3;
section 8, verification type demo_match).

A candidate is python source defining transform(grid) -> grid. It runs in a fresh child process:
the venv python with -s -P (no user site, no script dir on sys.path), -B (no bytecode files)
and -X utf8, a scrubbed environment (no API keys or other secrets inherited; PYTHONHASHSEED=0
so set and dict iteration over strings is deterministic), cwd and TEMP set to a throw-away
directory, a time limit per input grid (PARAMS["exec_timeout_s"], see below) and a stdout size cap. On Windows
the child is placed in a Job Object with KILL_ON_JOB_CLOSE, so a timeout (or the end of the
run) kills every descendant too; a grandchild that keeps the pipes open cannot stall the
readers, which hand over whatever arrived. Inputs go in as JSON on stdin; a small fixed runner
imports the candidate module and calls transform once per input inside try/except, writing
one result line marked with a per-execution nonce to stdout and leaving with os._exit (no
atexit handlers or candidate threads can write after it).

Time limit: each input grid (and the module import) gets its own limit of exec_timeout_s seconds
of process CPU time, plus a wall-clock guard of WALL_FACTOR times that for programs that sleep or
block. CPU time hardly depends on how many executions run side by side, so the outcome does not
change with --workers or the predict pool. After the first input that runs out of time the
remaining inputs are not run (each gets a "timeout" error). Inputs come in a fixed order (train
first), so the verifier and the portfolio control see the same result on the inputs they share,
and a program slow only on extra inputs (augmented copies) keeps its earlier outputs. The parent
kills the process tree only as a last resort, after STARTUP_S + (n + 1) wall-clock guards.

Isolation at P0 is process isolation ONLY. The child can still read and write any file the
user account can reach, open network sockets, spawn processes and allocate memory up to the
timeout. Nothing is forbidden beyond the timeout, the output cap, the scrubbed environment and
the process-tree kill. OS-level sandboxing (no-network, memory limits) is a P1 item.
"""
from __future__ import annotations

import json
import os
import secrets
import subprocess
import sys
import tempfile
import threading
import time
from pathlib import Path

from . import config

MAX_SIDE = 30
STDOUT_CAP_BYTES = 1_000_000
STDERR_CAP_BYTES = 20_000
ERROR_TAIL_CHARS = 600
MAX_MISMATCHES = 8
_MARK = "@@HTSA_RESULT@@"
WALL_FACTOR = 4          # wall-clock guard per input = WALL_FACTOR x the CPU-time limit
STARTUP_S = 10           # interpreter start-up allowance in the parent's last-resort timeout
_DEFAULT_PYTHON = Path(r"D:\AGI-lab\.venv\Scripts\python.exe")

# Fixed runner. The candidate path is argv[1]; the payload {"inputs": [...]} arrives on stdin.
# Candidate prints go to os.devnull; only the runner writes the marked result line.
_RUNNER = r'''
import copy, json, os, sys, threading, time, traceback, importlib.util
TAIL = 600
threading.stack_size(64 * 1024 * 1024)
def _tail(path):
    et, ev, tb = sys.exc_info()
    frames = [f for f in traceback.extract_tb(tb) if f.filename == path]
    for f in frames:
        f.filename = "candidate.py"
    text = "".join(traceback.format_list(frames)) + "".join(traceback.format_exception_only(et, ev))
    return text.replace(path, "candidate.py").replace(os.path.dirname(path), ".")[-TAIL:]
def _default(o):
    if hasattr(o, "tolist"):
        return o.tolist()
    raise TypeError("not JSON serializable: %s" % type(o).__name__)
def _timed(work, cpu_s, wall_s):
    """Run work() in a daemon thread; True when it finished within cpu_s of process CPU time and
    wall_s of wall time. A thread that runs on is ended by os._exit at the end of main."""
    t = threading.Thread(target=work, daemon=True)
    c0, w0 = time.process_time(), time.monotonic()
    t.start()
    while t.is_alive():
        t.join(0.02)
        if t.is_alive() and (time.process_time() - c0 > cpu_s or time.monotonic() - w0 > wall_s):
            return False
    return True
def main():
    path = sys.argv[1]
    real_out = sys.stdout
    payload = json.loads(sys.stdin.read())
    mark = "@@HTSA_RESULT@@" + payload.pop("nonce") + "@@"
    inputs = payload.pop("inputs")
    cpu_s, wall_s = float(payload.pop("grid_cpu_s")), float(payload.pop("grid_wall_s"))
    del payload
    res = {"outputs": [], "errors": [], "import_error": None, "timed_out": False}
    sys.stdout = open(os.devnull, "w", encoding="utf-8")
    box = {"fn": None}
    def _import():
        try:
            spec = importlib.util.spec_from_file_location("candidate", path)
            mod = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(mod)
            box["fn"] = getattr(mod, "transform")
        except BaseException:
            res["import_error"] = _tail(path)
    if not _timed(_import, cpu_s, wall_s):
        res["import_error"], res["timed_out"], box["fn"] = "timeout after %gs (module import)" % cpu_s, True, None
    fn = box["fn"]
    for g in inputs:
        if res["timed_out"]:
            res["outputs"].append(None)
            res["errors"].append(res["import_error"] or "timeout: not run after a timeout on an earlier input")
            continue
        if fn is None:
            res["outputs"].append(None)
            res["errors"].append(res["import_error"])
            continue
        one = {}
        def _one():
            try:
                one["out"] = json.loads(json.dumps(fn(copy.deepcopy(g)), default=_default))
            except BaseException:
                one["err"] = _tail(path)
        if not _timed(_one, cpu_s, wall_s):
            res["timed_out"] = True
            res["outputs"].append(None)
            res["errors"].append("timeout after %gs on this input" % cpu_s)
        elif "out" in one:
            res["outputs"].append(one["out"])
            res["errors"].append(None)
        else:
            res["outputs"].append(None)
            res["errors"].append(one.get("err", "no result"))
    sys.stdout = real_out
    real_out.write(mark + json.dumps(res) + "\n")
    real_out.flush()
    os._exit(0)
main()
'''


# ---------------------------------------------------------------- grids
def valid_grid(g) -> bool:
    """Rectangular list of lists of ints 0-9, 1..30 per side (section 8, ARC item format)."""
    if not isinstance(g, list) or not 1 <= len(g) <= MAX_SIDE:
        return False
    width = None
    for row in g:
        if not isinstance(row, list) or not 1 <= len(row) <= MAX_SIDE:
            return False
        if width is None:
            width = len(row)
        elif len(row) != width:
            return False
        for v in row:
            if type(v) is not int or not 0 <= v <= 9:
                return False
    return True


def shape(g) -> list | None:
    """[rows, cols] of a valid grid, else None."""
    return [len(g), len(g[0])] if valid_grid(g) else None


# ---------------------------------------------------------------- process plumbing
def python_exe() -> Path:
    """Candidate interpreter: HTSA_EXEC_PYTHON, config.VENV_PYTHON, the D: venv, else sys.executable."""
    for cand in (os.environ.get("HTSA_EXEC_PYTHON"), config.VENV_PYTHON, _DEFAULT_PYTHON):
        if cand and Path(cand).exists():
            return Path(cand)
    return Path(sys.executable)


def _child_env(sandbox: Path, exe: Path) -> dict:
    """Minimal environment: no inherited secrets; TEMP points into the sandbox."""
    env = {"PATH": str(exe.parent), "TEMP": str(sandbox), "TMP": str(sandbox),
           "PYTHONIOENCODING": "utf-8", "PYTHONHASHSEED": "0", "PYTHONUTF8": "1"}
    for k in ("SYSTEMROOT", "WINDIR", "COMSPEC"):
        if os.environ.get(k):
            env[k] = os.environ[k]
    return env


# ---------------------------------------------------------------- Windows job object (tree kill)
class _Job:
    """A Windows Job Object with KILL_ON_JOB_CLOSE: closing the handle kills the child and
    every process it spawned. A no-op elsewhere or when the job cannot be created."""

    def __init__(self):
        self.handle = None
        if os.name != "nt":
            return
        try:
            import ctypes
            from ctypes import wintypes
            k32 = ctypes.windll.kernel32
            k32.CreateJobObjectW.restype = wintypes.HANDLE
            job = k32.CreateJobObjectW(None, None)
            if not job:
                return

            class _BasicLimit(ctypes.Structure):
                _fields_ = [("PerProcessUserTimeLimit", ctypes.c_int64),
                            ("PerJobUserTimeLimit", ctypes.c_int64),
                            ("LimitFlags", wintypes.DWORD), ("MinimumWorkingSetSize", ctypes.c_size_t),
                            ("MaximumWorkingSetSize", ctypes.c_size_t), ("ActiveProcessLimit", wintypes.DWORD),
                            ("Affinity", ctypes.c_size_t), ("PriorityClass", wintypes.DWORD),
                            ("SchedulingClass", wintypes.DWORD)]

            class _IoCounters(ctypes.Structure):
                _fields_ = [(n, ctypes.c_uint64) for n in ("ReadOperationCount", "WriteOperationCount",
                            "OtherOperationCount", "ReadTransferCount", "WriteTransferCount",
                            "OtherTransferCount")]

            class _ExtLimit(ctypes.Structure):
                _fields_ = [("BasicLimitInformation", _BasicLimit), ("IoInfo", _IoCounters),
                            ("ProcessMemoryLimit", ctypes.c_size_t), ("JobMemoryLimit", ctypes.c_size_t),
                            ("PeakProcessMemoryUsed", ctypes.c_size_t), ("PeakJobMemoryUsed", ctypes.c_size_t)]

            info = _ExtLimit()
            info.BasicLimitInformation.LimitFlags = 0x2000    # JOB_OBJECT_LIMIT_KILL_ON_JOB_CLOSE
            if not k32.SetInformationJobObject(job, 9, ctypes.byref(info), ctypes.sizeof(info)):
                k32.CloseHandle(job)
                return
            self.k32, self.handle = k32, job
        except Exception:  # noqa: BLE001 - fall back to taskkill on timeout
            self.handle = None

    def assign(self, proc: subprocess.Popen) -> bool:
        if not self.handle:
            return False
        try:
            return bool(self.k32.AssignProcessToJobObject(self.handle, int(proc._handle)))
        except Exception:  # noqa: BLE001
            return False

    def close(self) -> None:
        """Kills the whole tree (KILL_ON_JOB_CLOSE) and releases the handle."""
        if self.handle:
            try:
                self.k32.CloseHandle(self.handle)
            finally:
                self.handle = None


def _kill_tree(proc: subprocess.Popen) -> None:
    """Fallback tree kill when no job object is available."""
    try:
        if os.name == "nt":
            subprocess.run(["taskkill", "/T", "/F", "/PID", str(proc.pid)], capture_output=True,
                           timeout=15)
        else:
            import signal                  # start_new_session: the group id is the child's pid; it
            os.killpg(proc.pid, signal.SIGKILL)   # stays valid after the child exits, getpgid would not
    except Exception:  # noqa: BLE001
        pass
    try:
        proc.kill()
    except OSError:
        pass


def _reader(stream, cap: int, sink: dict) -> None:
    """Read a pipe to EOF, keeping at most cap bytes and counting the rest. The sink is updated
    after every chunk, so a reader that never sees EOF (a grandchild holding the pipe) still
    leaves everything that arrived."""
    kept, total = bytearray(), 0
    sink["data"], sink["total"] = b"", 0
    fd = stream.fileno()
    while True:
        try:
            chunk = os.read(fd, 65536)      # returns as soon as any bytes arrive (read(n) would
        except (OSError, ValueError):       # block for n bytes or EOF while a grandchild holds the pipe)
            break
        if not chunk:
            break
        total += len(chunk)
        if len(kept) < cap:
            kept += chunk[: cap - len(kept)]
        sink["data"], sink["total"] = bytes(kept), total
    sink["data"], sink["total"] = bytes(kept), total


def _run_capped(cmd: list, stdin: bytes, cwd: Path, env: dict, timeout_s: float) -> dict:
    """Run cmd without a shell; bounded stdout/stderr; kill the whole tree on timeout and
    after the child exits (job object), so the readers never wait on a grandchild."""
    t0 = time.time()
    popen_kw: dict = {}
    if os.name == "nt":
        popen_kw["creationflags"] = getattr(subprocess, "CREATE_NEW_PROCESS_GROUP", 0)
    else:
        popen_kw["start_new_session"] = True
    proc = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE, cwd=str(cwd), env=env, shell=False, **popen_kw)
    job = _Job()
    in_job = job.assign(proc)
    out, err = {}, {}
    threads = [threading.Thread(target=_reader, args=(proc.stdout, STDOUT_CAP_BYTES, out), daemon=True),
               threading.Thread(target=_reader, args=(proc.stderr, STDERR_CAP_BYTES, err), daemon=True)]
    for t in threads:
        t.start()
    try:
        proc.stdin.write(stdin)
        proc.stdin.close()
    except OSError:
        pass
    timed_out = False
    try:
        proc.wait(timeout=timeout_s)
    except subprocess.TimeoutExpired:
        timed_out = True
        if in_job:
            job.close()
        else:
            _kill_tree(proc)
        proc.wait()
    # the child is gone; whatever it spawned dies with the job (or the fallback tree kill)
    if in_job:
        job.close()
    else:
        _kill_tree(proc)
    for t in threads:
        t.join(timeout=2)
    for t in threads:
        if t.is_alive():                 # a reader still blocked on a pipe held open elsewhere
            try:
                proc.stdout.close()
                proc.stderr.close()
            except OSError:
                pass
    return {"rc": proc.returncode, "stdout": out.get("data", b""), "stdout_total": out.get("total", 0),
            "stderr": err.get("data", b""), "timed_out": timed_out,
            "duration_ms": int((time.time() - t0) * 1000)}


def _fail_all(n: int, msg: str) -> dict:
    return {"outputs": [None] * n, "errors": [msg] * n, "fatal": msg}


def _parse(raw: dict, n: int, timeout_s: float, mark: str) -> dict:
    """Turn the child's raw output into per-input outputs and errors. Exactly one line must
    carry the nonce-marked result; the candidate cannot forge it after os._exit."""
    if raw["timed_out"]:
        return _fail_all(n, f"timeout after {timeout_s:g}s")
    if raw["stdout_total"] > STDOUT_CAP_BYTES:
        return _fail_all(n, f"stdout cap exceeded ({raw['stdout_total']} > {STDOUT_CAP_BYTES} bytes)")
    text = raw["stdout"].decode("utf-8", errors="replace")
    lines = [ln for ln in text.splitlines() if ln.startswith(mark)]
    if not lines:
        tail = raw["stderr"].decode("utf-8", errors="replace")[-ERROR_TAIL_CHARS:]
        return _fail_all(n, f"no result (rc={raw['rc']}): {tail}".strip())
    if len(lines) != 1:
        return _fail_all(n, f"{len(lines)} result lines (expected exactly one)")
    try:
        res = json.loads(lines[0][len(mark):])
    except json.JSONDecodeError:
        return _fail_all(n, "unparseable result line")
    outs = (list(res.get("outputs", [])) + [None] * n)[:n]
    errs = (list(res.get("errors", [])) + ["missing output"] * n)[:n]
    for i, g in enumerate(outs):
        if g is not None and not valid_grid(g):
            outs[i] = None
            errs[i] = errs[i] or "invalid grid: need a rectangular list of lists of int 0-9, <= 30x30"
    return {"outputs": outs, "errors": errs, "fatal": None, "grid_timeout": bool(res.get("timed_out"))}


def execute(src: str, inputs: list, timeout_s: float | None = None) -> dict:
    """Run transform on every input in one child process (section 3 /verify step 3).
    timeout_s is the CPU-time limit per input grid (module docstring). Returns
    {"outputs": [grid|None], "errors": [str|None], "fatal", "timed_out", "duration_ms"}."""
    timeout_s = float(timeout_s or config.PARAMS["exec_timeout_s"])
    wall_s = WALL_FACTOR * timeout_s
    n = len(inputs)
    tmp_root = config.LAB_ROOT / "tmp"
    tmp_root.mkdir(parents=True, exist_ok=True)
    nonce = secrets.token_hex(8)
    mark = _MARK + nonce + "@@"
    with tempfile.TemporaryDirectory(prefix="exec_", dir=tmp_root, ignore_cleanup_errors=True) as d:
        sandbox = Path(d)
        (sandbox / "runner.py").write_text(_RUNNER, encoding="utf-8")
        (sandbox / "candidate.py").write_text(src or "", encoding="utf-8")
        exe = python_exe()
        cmd = [str(exe), "-s", "-P", "-B", "-X", "utf8", str(sandbox / "runner.py"),
               str(sandbox / "candidate.py")]
        payload = json.dumps({"inputs": inputs, "nonce": nonce, "grid_cpu_s": timeout_s,
                              "grid_wall_s": wall_s}).encode("utf-8")
        raw = _run_capped(cmd, payload, sandbox, _child_env(sandbox, exe), STARTUP_S + (n + 1) * wall_s)
    res = _parse(raw, n, timeout_s, mark)
    res["timed_out"] = bool(raw["timed_out"] or res.pop("grid_timeout", False))
    res["duration_ms"] = raw["duration_ms"]
    return res


def run_program(src: str, inputs: list, timeout_s: float | None = None) -> list:
    """README interface: grid or None per input."""
    return execute(src, inputs, timeout_s)["outputs"]


# ---------------------------------------------------------------- demo match
def first_mismatches(exp: list, got: list, cap: int = MAX_MISMATCHES) -> list:
    """[[r, c, expected, got]] for the first cap differing cells of two same-shape grids."""
    out = []
    for r, (er, gr) in enumerate(zip(exp, got)):
        for c, (ev, gv) in enumerate(zip(er, gr)):
            if ev != gv:
                out.append([r, c, ev, gv])
                if len(out) >= cap:
                    return out
    return out


def pair_diff(i: int, exp: list, got, err: str | None) -> dict | None:
    """Diff of one train pair, or None if it matched."""
    if got is not None and got == exp:
        return None
    same = got is not None and shape(got) == shape(exp)
    return {"pair_index": i, "expected_shape": shape(exp),
            "got_shape": shape(got) if got is not None else None, "shape_mismatch": not same,
            "first_mismatches": first_mismatches(exp, got) if same else [], "error": err}


def demo_from_outputs(train: list[dict], outputs: list, errors: list) -> dict:
    """Score outputs against train outputs: {"matched", "total", "diffs", "errors"}."""
    diffs, errs, matched = [], [], 0
    for i, pair in enumerate(train):
        d = pair_diff(i, pair["output"], outputs[i], errors[i])
        if d is None:
            matched += 1
            continue
        diffs.append(d)
        if errors[i]:
            errs.append(f"pair {i}: {errors[i][-ERROR_TAIL_CHARS:]}")
    return {"matched": matched, "total": len(train), "diffs": diffs, "errors": errs}


def demo_match(src: str, train: list[dict]) -> dict:
    """README interface: run on the train inputs and compare with the train outputs (demo_match)."""
    res = execute(src, [p["input"] for p in train])
    return demo_from_outputs(train, res["outputs"], res["errors"])


def predict(src: str, test_input) -> list | None:
    """README interface: predicted test-output grid or None."""
    return run_program(src, [test_input])[0]


# ---------------------------------------------------------------- augmentation and perturbation
def _rot(g):
    return [list(r) for r in zip(*g[::-1])]


SYMMETRIES = {"rot90": _rot, "rot180": lambda g: _rot(_rot(g)), "rot270": lambda g: _rot(_rot(_rot(g))),
              "flip_h": lambda g: [r[::-1] for r in g], "flip_v": lambda g: g[::-1],
              "transpose": lambda g: [list(r) for r in zip(*g)]}


def augmented(test_input) -> list:
    """The four augmented copies of a test input used as a selection tie-break by think and the
    portfolio: rotate 90, mirror left-right, mirror top-bottom, transpose."""
    s = SYMMETRIES
    return [s["rot90"](test_input), s["flip_h"](test_input), s["flip_v"](test_input), s["transpose"](test_input)]


def aug_key(outputs: list) -> str | None:
    """Hashable key of the outputs on the augmented inputs; None if any of them crashed."""
    return None if any(o is None for o in outputs) else json.dumps(outputs, separators=(",", ":"))


def colour_permutation(train: list[dict]) -> dict[int, int]:
    """A fixed cycle over the non-background colours used in the examples (each goes to the next
    used one; 0 stays). Deterministic, so the check needs no seed."""
    used = sorted({v for p in train for g in (p["input"], p["output"]) for row in g for v in row} - {0})
    return dict(zip(used, used[1:] + used[:1])) if len(used) > 1 else {}


def perturbation_detail(src: str, train: list[dict], timeout_s: float | None = None) -> dict:
    """Perturbation checks of ARCHITECTURE.md section 3 /verify step 1 (EVL-18) as a detail only:
    P0 status stays plain demo_match (section 8 schedules perturbation for P1), so nothing here may
    change "verified". One extra execution, 0 tokens. For each of the six rotations and mirrors and
    one colour permutation it reports whether the program commutes with it on every train input,
    f(s(x)) == s(f(x)). Not every task is equivariant, so a low count is a signal, not a failure
    (offline replay, research_notes/portfolio_improvements/03_SYNTHESIS.md: passing right programs
    commute with 3.4 of 6 symmetries on average, passing wrong ones with 1.5)."""
    ops = dict(SYMMETRIES)
    perm = colour_permutation(train)
    if perm:
        ops["colour_perm"] = lambda g: [[perm.get(v, v) for v in row] for row in g]
    ins = [p["input"] for p in train]
    names = list(ops)
    res = execute(src, ins + [ops[k](x) for k in names for x in ins], timeout_s)
    outs, n = res["outputs"], len(ins)
    base = outs[:n]
    consistent = [k for j, k in enumerate(names)
                  if all(b is not None and g == ops[k](b) for b, g in zip(base, outs[n * (j + 1): n * (j + 2)]))]
    return {"checked": names, "consistent": consistent, "n_checked": len(names),
            "n_consistent": len(consistent)}
