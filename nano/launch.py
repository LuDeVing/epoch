"""Runs a candidate trainer under the harness's eye. Every candidate process (build, steps, short
and long runs, the full run, the reach audit and the exam) goes through here, never through a bare
interpreter.

What the launcher enforces from OUTSIDE the candidate's code (the AI Scientist lesson: limits and
resources live outside agent-writable files; MLE-bench: answers stay host-only):
  - two processes. The launcher process never runs candidate code; it starts a child process that
    does, applies the wall-clock cap from outside (kills the child, exit 124), and writes the audit
    record itself from what the child streamed to a private event file. A child that ends with exit
    code 0 but without its closing record (os._exit, a killed hook) is a violation.
  - the child's environment: secrets (keys, tokens, passwords, proxies) are removed before it starts.
  - process creation, at the operating-system level on Windows: the child puts itself in a job
    object that allows one active process, so CreateProcess fails whatever Python path reaches it.
  - the data folder: HTSA_DATA_DIR points at a folder that must hold only train shards (checked
    before the child starts; a val file there refuses the run), so the validation split is not in
    the training process's folder at all.
  - a tripwire audit hook (PEP 578) in the child, armed after torch is imported:
      network: creating a socket or connecting, binding, resolving names;
      processes: subprocess, os.system, os.exec*, os.spawn*, os.startfile, CreateProcess, os.kill;
      ctypes: every ctypes.* event (loading a library, calling a foreign function, raw memory);
      reads: open(), os.open, np.memmap, np.fromfile and torch.from_file on any path outside the
        run's output folder, the train-only data folder, the Python install, the project code,
        the temp and cache folders and the files the harness named on the command line; anything
        under the full data folder, anything named val.bin, and train shards read other than
        through the harness loader (np.memmap in Shards, counted below);
      writes: into the project or data folders; deleting or renaming protected files;
      introspection that could reach the hook: gc.get_objects / get_referrers / get_referents,
        sys.settrace / setprofile, sys.monitoring callbacks, a traceback frame inside the hook,
        sys.addaudithook.
    Denied imports are refused for modules torch has not already imported. For modules torch did
    import (socket, subprocess, ctypes ...), the dangerous functions are replaced with raising stubs
    after the torch import (os.system, subprocess.Popen, socket.socket, ctypes.CDLL ...), so
    sys.modules['ctypes'], builtins.__import__('subprocess'), from os import system and
    getattr(os, 'sys' + 'tem') all reach a stub; the audit events are the net under the stubs.
  - a token count from the launcher side: train shards opened through np.memmap are counted on
    every slice; tokens = bytes / 4 (uint16 tokens, each window read twice, as inputs and as
    targets shifted by one). A run whose reported tokens differ from the count by more than 2% is a
    violation. The counter can only move forward (an itertools.count).
  - the exam (nano/exam.py) seals the data with sys.audit("htsa.seal") once it has read its
    windows; after that the candidate's model code cannot read the validation split.
  - a pre-existing weights file in the output folder is removed before a training run.
CPython's docs are clear that audit hooks are observation, not a sandbox: this is one layer of
several (the static boundary check in nano/boundary.py, the harness-owned exam, the checker failing
any audit violation). Not covered here and why: network at the OS level needs administrator rights
on Windows (firewall rule) or an AppContainer, which also needs ACL changes on the venv and data and
is untested with CUDA; code that rewrites a numpy class's methods or reads through the memmap's raw
buffer can hide reads from the token count; torch._C.StorageBase.from_file and
torch._C._VariableFunctions.from_file cannot be wrapped (immutable types) and are refused by the
static check only.

Usage (as the checker calls it):
  python -I nano/launch.py --out OUT --data-dir DIR --wall-cap 900 --audit OUT/audit.json -- SCRIPT [script args]
Exit codes: the script's own; 124 on the wall cap; 125 when a tripwire raised or any violation was
recorded; 2 when the data folder is not train-only.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import runpy
import subprocess
import sys
import tempfile
import time
from pathlib import Path

DENIED_MODULES = {"socket", "urllib", "http", "ftplib", "smtplib", "telnetlib", "xmlrpc", "requests", "httpx",
                  "aiohttp", "subprocess", "ctypes", "multiprocessing", "importlib", "pty", "ssl", "asyncio", "paramiko"}
NET_EVENTS = {"socket.__new__", "socket.connect", "socket.bind", "socket.sendto", "socket.sendmsg", "socket.getaddrinfo",
              "socket.gethostbyname", "socket.gethostbyaddr", "socket.getnameinfo", "socket.gethostname"}
PROC_EVENTS = {"subprocess.Popen", "os.system", "os.exec", "os.spawn", "os.posix_spawn", "os.fork", "os.forkpty",
               "_winapi.CreateProcess", "os.startfile", "_posixsubprocess.fork_exec"}
INTROSPECTION_EVENTS = {"gc.get_objects", "gc.get_referrers", "gc.get_referents", "sys.settrace", "sys.setprofile",
                        "sys.addaudithook", "sys.monitoring.register_callback", "sys._current_frames"}
DELETE_EVENTS = {"os.remove", "os.unlink", "os.rename", "os.replace", "shutil.rmtree", "os.rmdir", "os.truncate"}
# functions replaced by raising stubs once torch is imported: module name -> attribute names
STUBS = {
    "os": ["system", "popen", "startfile", "execv", "execve", "execl", "execle", "execlp", "execlpe", "execvp", "execvpe",
           "spawnl", "spawnle", "spawnv", "spawnve", "spawnlp", "spawnlpe", "spawnvp", "spawnvpe", "posix_spawn",
           "posix_spawnp", "fork", "forkpty", "kill", "killpg"],
    "nt": ["system", "startfile", "execv", "execve", "spawnv", "spawnve", "kill"],
    "posix": ["system", "execv", "execve", "fork", "forkpty", "posix_spawn", "posix_spawnp", "kill"],
    "subprocess": ["Popen", "run", "call", "check_call", "check_output", "getoutput", "getstatusoutput"],
    "_winapi": ["CreateProcess", "OpenProcess", "TerminateProcess", "CreatePipe"],
    "socket": ["socket", "create_connection", "create_server", "socketpair", "fromfd", "getaddrinfo", "gethostbyname"],
    "_socket": ["socket", "socketpair", "getaddrinfo", "gethostbyname"],
    "ctypes": ["CDLL", "PyDLL", "WinDLL", "OleDLL", "cdll", "pydll", "windll", "oledll", "pythonapi", "LibraryLoader",
               "memmove", "memset", "string_at", "wstring_at", "cast"],
    "_ctypes": ["LoadLibrary", "FreeLibrary", "dlopen", "dlclose", "dlsym", "call_function", "call_cdeclfunction"],
    "multiprocessing": ["Process", "Pool"],
    "pty": ["spawn", "fork"],
}
SECRET_ENV = re.compile(r"(?i)(key|token|secret|passw|credential|cookie|auth|proxy)")


class Tripwire(RuntimeError):
    pass


def _norm(p: str) -> str:
    return os.path.normcase(os.path.abspath(p))


def _under(path: str, roots) -> bool:
    return any(r and (path == r.rstrip("\\/") or path.startswith(r.rstrip("\\/") + os.sep)) for r in roots)


def _plain_path(p):
    """The path as an exact str without running any code the candidate supplied (a str subclass or a
    custom __fspath__ could otherwise run inside the hook and reach its frame). None: refuse."""
    import pathlib
    if isinstance(p, str):
        return "".__add__(p)
    if isinstance(p, bytes):
        try:
            return b"".__add__(p).decode(sys.getfilesystemencoding(), "surrogateescape")
        except Exception:  # noqa: BLE001
            return None
    if type(p) in (pathlib.Path, pathlib.PurePath, pathlib.WindowsPath, pathlib.PureWindowsPath,
                   pathlib.PosixPath, pathlib.PurePosixPath):
        return pathlib.PurePath.__fspath__(p)
    return None


def _limit_processes() -> str:
    """Windows: put this process in a job object that allows one active process, so no child process
    can be created at the OS level. Returns 'on', or why not."""
    if os.name != "nt":
        return "not windows"
    try:
        import ctypes
        from ctypes import wintypes

        class BASIC(ctypes.Structure):
            _fields_ = [("PerProcessUserTimeLimit", ctypes.c_int64), ("PerJobUserTimeLimit", ctypes.c_int64),
                        ("LimitFlags", wintypes.DWORD), ("MinimumWorkingSetSize", ctypes.c_size_t),
                        ("MaximumWorkingSetSize", ctypes.c_size_t), ("ActiveProcessLimit", wintypes.DWORD),
                        ("Affinity", ctypes.c_size_t), ("PriorityClass", wintypes.DWORD),
                        ("SchedulingClass", wintypes.DWORD)]
        k32 = ctypes.WinDLL("kernel32", use_last_error=True)
        k32.CreateJobObjectW.restype = wintypes.HANDLE
        k32.CreateJobObjectW.argtypes = [ctypes.c_void_p, wintypes.LPCWSTR]
        k32.SetInformationJobObject.argtypes = [wintypes.HANDLE, ctypes.c_int, ctypes.c_void_p, wintypes.DWORD]
        k32.AssignProcessToJobObject.argtypes = [wintypes.HANDLE, wintypes.HANDLE]
        k32.GetCurrentProcess.restype = wintypes.HANDLE
        job = k32.CreateJobObjectW(None, None)
        if not job:
            return f"CreateJobObject failed ({ctypes.get_last_error()})"
        info = BASIC()
        info.LimitFlags = 0x00000008                    # JOB_OBJECT_LIMIT_ACTIVE_PROCESS
        info.ActiveProcessLimit = 1
        if not k32.SetInformationJobObject(job, 2, ctypes.byref(info), ctypes.sizeof(info)):
            return f"SetInformationJobObject failed ({ctypes.get_last_error()})"
        if not k32.AssignProcessToJobObject(job, k32.GetCurrentProcess()):
            return f"AssignProcessToJobObject failed ({ctypes.get_last_error()})"
        _limit_processes.handle = job                   # the job lives while this process does
        return "on"
    except Exception as e:  # noqa: BLE001
        return f"error: {type(e).__name__}: {e}"


def _arm(a, sink, script: str) -> None:
    """Install the stubs, the counted loader and the audit hook. Everything the hook needs lives in
    this closure; nothing is returned, so the caller's frame holds no reference to it."""
    import atexit
    import collections
    import itertools
    import numpy as np

    out = _norm(a.out)
    data_dir = _norm(a.data_dir)
    data_full = _norm(a.data_full) if a.data_full else ""
    project = _norm(a.project)
    allow_val = bool(a.allow_val)
    audit_path = _norm(a.audit)
    sink_dir = _norm(os.path.dirname(sink.name))
    tmp = [_norm(tempfile.gettempdir())]
    for var in ("TEMP", "TMP", "TORCHINDUCTOR_CACHE_DIR", "TRITON_CACHE_DIR", "TORCH_HOME", "CUDA_CACHE_PATH"):
        if os.environ.get(var):
            tmp.append(_norm(os.environ[var]))
    allow_write = tuple([out] + tmp + ([_norm(os.environ["LOCALAPPDATA"])] if os.environ.get("LOCALAPPDATA") else []))
    home = os.path.expanduser("~")
    roots = [out, project, _norm(os.path.dirname(os.path.abspath(script))), _norm(sys.prefix), _norm(sys.base_prefix),
             _norm(sys.exec_prefix), _norm(os.devnull)] + tmp
    roots += [_norm(p) for p in sys.path if p and os.path.isdir(p)]
    roots += [_norm(os.path.join(home, d)) for d in (".cache", ".triton", ".nv")]
    if os.environ.get("SystemRoot"):
        roots.append(_norm(os.environ["SystemRoot"]))
    for x in a.script_args:                              # files the harness named (--candidate, --ckpt, --baseline)
        if isinstance(x, str) and x != "--" and not x.startswith("-") and os.path.exists(x):
            roots.append(_norm(x))
    read_roots = tuple(r for r in roots if not (r and _under(r, [data_dir]) or (data_full and _under(r, [data_full]))))
    st = {"sealed": False, "loader": None, "in_hook": False, "broken": False, "notes": 0, "done": False}
    count = itertools.count()                            # bytes read through the counted loader; only moves forward
    hook_code = []

    def emit(rec: dict) -> None:
        try:
            sink.write((json.dumps(rec) + "\n").encode("utf-8"))
        except Exception:  # noqa: BLE001
            st["broken"] = True

    def violate(event: str, detail: str, msg: str):
        emit({"kind": "violation", "event": event, "detail": detail[-200:]})
        return Tripwire(msg)

    def note(event: str, detail: str) -> None:
        if st["notes"] < 50:
            st["notes"] += 1
            emit({"kind": "note", "event": event, "detail": detail[-200:]})

    def read_problem(p: str) -> str | None:
        val_open = allow_val and not st["sealed"]
        if not val_open and "val.bin" in os.path.basename(p):
            return "the validation split is not readable from a training process"
        if _under(p, [data_dir]):
            if val_open:
                return None
            if allow_val:
                return "the exam sealed the data: model code may not read it"
            if st["loader"] == p:
                st["loader"] = None
                return None
            return "the train shards are read only through the harness loader (np.memmap in Shards)"
        if data_full and _under(p, [data_full]):
            return None if val_open else "the full data folder (with the validation split) is not readable from here"
        if _under(p, read_roots):
            return None
        return "reading outside the run's folders is not allowed"

    def check_open(path, mode, flags) -> None:
        if isinstance(path, int):
            return
        s = _plain_path(path)
        if s is None:
            raise violate("open", type(path).__name__, "only str, bytes and pathlib paths may be opened")
        p = _norm(s)
        if p == audit_path or _under(p, [sink_dir]):
            raise violate("open", p[-120:], "the audit record belongs to the launcher")
        if isinstance(mode, str):
            m = "".__add__(mode)
            reads = "r" in m or "+" in m
            writes = any(ch in m for ch in "wax+")
        else:
            fl = int(flags or 0) if isinstance(flags, int) else 0
            acc = fl & 3
            writes = acc in (1, 2) or bool(fl & (os.O_APPEND | os.O_CREAT | os.O_TRUNC))
            reads = acc != 1
        if reads:
            why = read_problem(p)
            if why:
                raise violate("open", p[-120:], why)
        if writes:
            if _under(p, allow_write):
                return
            if _under(p, [project]) or _under(p, [data_dir]) or (data_full and _under(p, [data_full])):
                raise violate("write", p[-120:], "writing into the project or data folders is not allowed")
            note("write-outside", p[-120:])

    def hook(event: str, args: tuple) -> None:
        if st["in_hook"]:
            return
        st["in_hook"] = True
        try:
            if st["broken"]:
                raise Tripwire("the audit record was lost")
            if event == "open":
                check_open(args[0], args[1] if len(args) > 1 else "r", args[2] if len(args) > 2 else 0)
            elif event in NET_EVENTS:
                raise violate(event, "", f"network access is not allowed ({event})")
            elif event in PROC_EVENTS or event.startswith(("subprocess.", "os.exec", "os.spawn", "_winapi.CreateProcess",
                                                           "os.posix_spawn")):
                raise violate(event, "", f"spawning processes is not allowed ({event})")
            elif event == "os.kill":
                if not args or args[0] != os.getpid():
                    raise violate(event, str(args[:1]), "signalling other processes is not allowed")
            elif event.startswith("ctypes."):
                raise violate(event, event, f"ctypes is not allowed ({event})")
            elif event in INTROSPECTION_EVENTS:
                raise violate(event, "", f"{event} is not allowed in a candidate run")
            elif event == "object.__getattr__":
                if len(args) > 1 and args[1] == "tb_frame":
                    fr = args[0].tb_frame                # reentrant: in_hook is set, so this raises nothing
                    if fr is not None and fr.f_code in hook_code:
                        raise violate(event, "tb_frame", "reading the launcher's frames is not allowed")
            elif event == "import":
                name = str(args[0]).split(".")[0]
                if name in DENIED_MODULES and name not in sys.modules:
                    raise violate("import", name, f"import of {name} is not allowed")
            elif event in DELETE_EVENTS:
                for x in args[:2]:
                    s = _plain_path(x) if not isinstance(x, int) else None
                    if s is None:
                        continue
                    p = _norm(s)
                    if _under(p, [project, data_dir]) or (data_full and _under(p, [data_full])) \
                            or p == audit_path or _under(p, [sink_dir]):
                        raise violate(event, p[-120:], f"{event} on protected files is not allowed")
            elif event == "htsa.stub":
                raise violate(str(args[0]), "stub", f"{args[0]} is not allowed in a candidate run")
            elif event == "htsa.read":                   # torch.from_file and friends, wrapped below
                check_open(args[0], "rb", 0)
            elif event == "htsa.loader":
                s = _plain_path(args[0])
                if s is not None and not allow_val:
                    p = _norm(s)
                    if _under(p, [data_dir]):
                        st["loader"] = p
            elif event == "htsa.seal":
                st["sealed"] = True
        except Tripwire:
            raise
        except Exception:  # noqa: BLE001   the hook itself must never break the run
            return
        finally:
            st["in_hook"] = False

    hook_code.extend([hook.__code__, check_open.__code__, read_problem.__code__, violate.__code__])

    # raising stubs for the dangerous functions of modules torch already imported
    class Stub:
        """Calling it, or reading any attribute of it (ctypes.windll.kernel32), trips the wire."""
        __slots__ = ("_q",)

        def __init__(self, qual: str):
            object.__setattr__(self, "_q", qual)

        def _trip(self, *_a, **_k):
            q = object.__getattribute__(self, "_q")
            sys.audit("htsa.stub", q)
            raise Tripwire(f"{q} is not allowed in a candidate run")

        __call__ = _trip
        __getitem__ = _trip

        def __getattr__(self, _name):
            self._trip()

    def make_stub(qual: str):
        return Stub(qual)

    n_stubs = 0
    for modname, names in STUBS.items():
        mod = sys.modules.get(modname)
        if mod is None:
            continue
        for nm in names:
            if hasattr(mod, nm):
                try:
                    setattr(mod, nm, make_stub(f"{modname}.{nm}"))
                    n_stubs += 1
                except Exception:  # noqa: BLE001
                    pass

    # torch.from_file raises no audit event of its own: route it through the read rule
    try:
        import torch
        orig_from_file = torch.from_file

        def from_file(filename, *args, **kw):
            sys.audit("htsa.read", filename)
            return orig_from_file(filename, *args, **kw)
        torch.from_file = from_file
        for cls in (torch.UntypedStorage, torch.TypedStorage):
            orig = cls.from_file

            def storage_from_file(filename, *args, _orig=orig, **kw):
                sys.audit("htsa.read", filename)
                return _orig(filename, *args, **kw)
            cls.from_file = staticmethod(storage_from_file)
    except Exception:  # noqa: BLE001
        pass

    # the counted loader: np.memmap on a train shard counts every slice read from it
    base_memmap = np.memmap
    counting = {"dir": data_dir, "on": not allow_val}

    class memmap(base_memmap):
        def __new__(cls, filename, *args, **kw):
            sys.audit("htsa.loader", filename)
            obj = base_memmap.__new__(cls, filename, *args, **kw)
            if counting["on"]:
                fn = obj.filename
                obj._htsa_count = bool(fn) and _under(_norm(fn), [counting["dir"]])
            return obj

        def __getitem__(self, idx):
            r = base_memmap.__getitem__(self, idx)
            if self.__dict__.get("_htsa_count"):
                n = int(getattr(r, "nbytes", self.itemsize))
                collections.deque(itertools.islice(count, n), maxlen=0)
            return r
    memmap.__module__ = "numpy"
    memmap.__qualname__ = "memmap"
    np.memmap = memmap

    def final() -> None:
        if st["done"]:
            return
        st["done"] = True
        emit({"kind": "end", "data_bytes": next(count)})
    atexit.register(final)
    emit({"kind": "armed", "stubs": n_stubs})
    sys.addaudithook(hook)


def child_main(a, sink_path: str) -> int:
    sys.dont_write_bytecode = True                       # no .pyc writes into the project from imports
    job = "off" if os.environ.get("HTSA_LAUNCH_NO_JOB") == "1" else _limit_processes()
    try:
        import numpy  # noqa: F401
        import torch  # noqa: F401   torch loads its native libraries through ctypes; before the hook arms
        if torch.cuda.is_available():
            torch.cuda.init()            # CUDA's lazy initialisation also goes through ctypes: do it now
    except Exception:  # noqa: BLE001
        pass
    sink = open(sink_path, "ab", buffering=0)
    sink.write((json.dumps({"kind": "start", "job": job}) + "\n").encode("utf-8"))
    _arm(a, sink, a.script)
    del sink
    sys.argv = [a.script] + [x for x in a.script_args if x != "--"]
    rc = 0
    try:
        runpy.run_path(a.script, run_name="__main__")
    except SystemExit as e:
        rc = int(e.code) if isinstance(e.code, int) else (0 if e.code is None else 1)
    except Tripwire as e:
        print(f"[launch] tripwire: {e}", file=sys.stderr)
        rc = 125
    except BaseException as e:  # noqa: BLE001
        import traceback
        traceback.print_exc()                            # the crash, for the revision feedback
        print(f"[launch] the script raised {type(e).__name__}: {str(e)[:500]}", file=sys.stderr)
        rc = 1
    return rc


def _check_data_dir(a) -> str | None:
    """The training data folder must hold train shards only."""
    if a.allow_val:
        return None
    d = Path(a.data_dir)
    if a.data_full and _norm(a.data_dir) == _norm(a.data_full):
        return f"the data folder {d} is the full data folder; a training run gets the train-only folder"
    if not d.is_dir():
        return None                                      # nothing to read; the script reports the missing shards
    bad = [f.name for f in d.iterdir() if not re.fullmatch(r"train_[\w.-]*\.bin", f.name)]
    if bad:
        return f"the data folder {d} holds files other than train shards: {', '.join(sorted(bad)[:5])}"
    return None


def _child_env(data_dir: str) -> dict:
    env = {k: v for k, v in os.environ.items() if not SECRET_ENV.search(k)}
    env["HTSA_DATA_DIR"] = data_dir
    env.setdefault("PYTHONUNBUFFERED", "1")
    return env


def _kill_tree(proc) -> None:
    """The wall cap ends the child and every process it started (the job object keeps there being none,
    but it may be off or unavailable)."""
    try:
        if os.name == "nt":
            subprocess.run(["taskkill", "/F", "/T", "/PID", str(proc.pid)], capture_output=True, timeout=60)
        else:
            os.killpg(proc.pid, 9)
    except Exception:  # noqa: BLE001
        pass
    try:
        proc.kill()
    except Exception:  # noqa: BLE001
        pass


def parent_main(a, argv: list[str]) -> int:
    out = Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    t0 = time.time()
    audit = {"violations": [], "notes": [], "timed_out": False, "wall": None, "rc": None, "sandbox": {}}

    def write_audit() -> None:
        audit["wall"] = round(time.time() - t0, 1)
        try:
            Path(a.audit).write_text(json.dumps(audit, indent=1), encoding="utf-8")
        except Exception:  # noqa: BLE001
            pass

    problem = _check_data_dir(a)
    if problem:
        print(f"[launch] refused: {problem}", file=sys.stderr)
        audit["violations"].append({"event": "setup", "detail": problem})
        audit["rc"] = 2
        write_audit()
        return 2
    if not a.allow_val:                       # a trainer: no stale weights may survive into the exam
        for stale in ("model.pt",):           # (the exam itself runs with --allow-val and must keep them)
            try:
                (out / stale).unlink()
            except FileNotFoundError:
                pass
    sink_dir = tempfile.mkdtemp(prefix="htsa_launch_")
    sink_path = os.path.join(sink_dir, "events.jsonl")
    Path(sink_path).write_bytes(b"")
    cmd = [sys.executable, "-I", os.path.abspath(__file__), "--_child", sink_path, *argv]
    proc = subprocess.Popen(cmd, env=_child_env(a.data_dir), **({} if os.name == "nt" else {"start_new_session": True}))
    try:
        rc = proc.wait(timeout=a.wall_cap if a.wall_cap > 0 else None)
    except subprocess.TimeoutExpired:
        _kill_tree(proc)
        proc.wait()
        audit["timed_out"] = True
        rc = 124
    events = []
    try:
        for line in Path(sink_path).read_text(encoding="utf-8", errors="replace").splitlines():
            try:
                events.append(json.loads(line))
            except ValueError:
                pass
    except OSError:
        pass
    try:
        os.remove(sink_path)
        os.rmdir(sink_dir)
    except OSError:
        pass
    end = None
    for ev in events:
        k = ev.get("kind")
        if k == "violation":
            audit["violations"].append({"event": ev.get("event"), "detail": ev.get("detail")})
        elif k == "note":
            audit["notes"].append({"event": ev.get("event"), "detail": ev.get("detail")})
        elif k == "start":
            audit["sandbox"]["job_object"] = ev.get("job")
        elif k == "armed":
            audit["sandbox"]["stubs"] = ev.get("stubs")
        elif k == "end":
            end = ev
    if rc == 0 and end is None:
        audit["violations"].append({"event": "exit", "detail": "the run exited 0 without the launcher's closing record "
                                    "(os._exit, or the hook was tampered with)"})
    if end is not None and not a.allow_val:
        audit["data_bytes"] = end.get("data_bytes", 0)
        audit["tokens_counted"] = audit["data_bytes"] // 4
        problem = _token_mismatch(out / "metrics.json", audit["tokens_counted"], t0)
        if problem:
            audit["violations"].append({"event": "tokens", "detail": problem})
    if audit["violations"] and rc != 124:
        rc = 125
    audit["rc"] = rc
    write_audit()
    return rc


TOKEN_TOL = 0.02


def _token_mismatch(metrics: Path, counted: int, t0: float) -> str | None:
    """Reported tokens against the launcher's count; None when they agree within TOKEN_TOL."""
    try:
        if not metrics.exists() or metrics.stat().st_mtime < t0 - 1:
            return None                                   # no report from this run (a build, or a crash)
        m = json.loads(metrics.read_text(encoding="utf-8"))
    except Exception:  # noqa: BLE001
        return None
    rep = m.get("tokens")
    if rep is None or m.get("mode") == "build":
        return None
    rep = float(rep)
    if abs(counted - rep) > TOKEN_TOL * max(rep, 1.0):
        return (f"the run reports {rep:.0f} training tokens but read {counted} through the harness loader "
                f"(bytes / 4: inputs and shifted targets as two uint16 slices); more than {TOKEN_TOL:.0%} apart")
    return None


def main(argv: list[str] | None = None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    sink = None
    if argv[:1] == ["--_child"]:
        sink, argv = argv[1], argv[2:]
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True, help="the run's output folder (the only project-side write target)")
    ap.add_argument("--data-dir", required=True, help="folder with the train shards only")
    ap.add_argument("--data-full", default="", help="the full data folder (never readable from here)")
    ap.add_argument("--wall-cap", type=float, default=0.0, help="seconds; 0 = none")
    ap.add_argument("--audit", required=True, help="where to write the audit record")
    ap.add_argument("--project", default=str(Path(__file__).resolve().parent.parent))
    ap.add_argument("--allow-val", action="store_true", help="the exam may read the validation split until it seals")
    ap.add_argument("script")
    ap.add_argument("script_args", nargs=argparse.REMAINDER)
    a = ap.parse_args(argv)
    if sink is not None:
        return child_main(a, sink)
    return parent_main(a, argv)


if __name__ == "__main__":
    raise SystemExit(main())
