"""Runs a candidate trainer under the harness's eye. Every candidate process (build, steps, short
and long runs, the full run) goes through here, never through a bare interpreter.

What the launcher enforces from OUTSIDE the candidate's code (the AI Scientist lesson: limits and
resources live outside agent-writable files):
  - a wall-clock cap: the process is killed at --wall-cap seconds, whatever the script does
  - the data folder: HTSA_DATA_DIR points at a folder that holds the train shards only, so the
    validation split is not reachable from the training process at all (MLE-bench: answers host-only)
  - a tripwire audit hook (PEP 578): network connections, process creation (subprocess, os.system,
    the Windows CreateProcess call used by multiprocessing, os.startfile) and reads of anything named
    like the validation split raise at once; writes outside the run's output folder and the temp
    folders are logged; ctypes loads are logged. Denied imports are refused only for modules torch has
    not already imported (torch pulls in socket, ssl, subprocess and more); the static check in
    nano/boundary.py is the real import rule, this hook is a second net. CPython's docs are
    clear that audit hooks are observation, not a sandbox, so this is one layer of several: the
    boundary check (nano/boundary.py) denies the same modules statically, the exam is computed by the
    harness (nano/exam.py), and the checker fails any candidate whose audit log has a violation.
  - a pre-existing weights file in the output folder is removed before the run

Usage (as the checker calls it):
  python -I nano/launch.py --out OUT --data-dir DIR --wall-cap 900 --audit OUT/audit.json -- SCRIPT [script args]
Exit codes: the script's own; 124 on the wall cap; 125 when a tripwire raised.
"""
from __future__ import annotations

import argparse
import json
import os
import runpy
import sys
import tempfile
import threading
import time
from pathlib import Path

DENIED_MODULES = {"socket", "urllib", "http", "ftplib", "smtplib", "telnetlib", "xmlrpc", "requests", "httpx",
                  "aiohttp", "subprocess", "ctypes", "multiprocessing", "importlib", "pty", "ssl", "asyncio", "paramiko"}
NET_EVENTS = {"socket.connect", "socket.bind", "socket.sendto", "socket.sendmsg", "socket.getaddrinfo",
              "socket.gethostbyname", "socket.gethostbyaddr", "socket.getnameinfo"}
PROC_EVENTS = {"subprocess.Popen", "os.system", "os.exec", "os.spawn", "os.posix_spawn", "os.fork", "os.forkpty",
               "_winapi.CreateProcess", "os.startfile", "_posixsubprocess.fork_exec"}
_state = {"violations": [], "notes": [], "armed": False, "allow_write": [], "project": "", "data_full": ""}


class Tripwire(RuntimeError):
    pass


def _norm(p) -> str:
    try:
        return os.path.normcase(os.path.abspath(os.fsdecode(p)))
    except Exception:  # noqa: BLE001
        return str(p)


def _under(path: str, roots: list[str]) -> bool:
    return any(path.startswith(r.rstrip("\\/") + os.sep) or path == r.rstrip("\\/") for r in roots)


def _hook(event: str, args: tuple) -> None:
    if not _state["armed"]:
        return
    try:
        if event in NET_EVENTS:
            _state["violations"].append({"event": event, "detail": str(args[1:])[:200]})
            raise Tripwire(f"network access is not allowed ({event})")
        if event in PROC_EVENTS or event.startswith("subprocess.") or event.startswith("os.exec") or event.startswith("os.spawn") \
                or event.startswith("_winapi.CreateProcess"):
            _state["violations"].append({"event": event, "detail": str(args)[:200]})
            raise Tripwire(f"spawning processes is not allowed ({event})")
        if event == "import":
            name = str(args[0]).split(".")[0]
            if name in DENIED_MODULES and name not in sys.modules:
                _state["violations"].append({"event": "import", "detail": name})
                raise Tripwire(f"import of {name} is not allowed")
        elif event == "open":
            path, mode = args[0], (args[1] or "r") if len(args) > 1 else "r"
            if not isinstance(path, (str, bytes, os.PathLike)):
                return
            p = _norm(path)
            if not _state.get("allow_val") and ("val.bin" in p.lower() or (_state["data_full"] and _under(p, [_state["data_full"]]) and "train_" not in p.lower())):
                _state["violations"].append({"event": "open", "detail": p[-120:]})
                raise Tripwire("the validation split is not readable from a training process")
            if any(ch in str(mode) for ch in "wax+"):
                if _under(p, _state["allow_write"]):
                    return
                if _state["project"] and _under(p, [_state["project"]]):
                    _state["violations"].append({"event": "write", "detail": p[-120:]})
                    raise Tripwire("writing into the project folder is not allowed")
                _state["notes"].append({"event": "write-outside", "detail": p[-120:]})
        elif event.startswith("ctypes."):
            if len(_state["notes"]) < 50:
                _state["notes"].append({"event": event, "detail": str(args)[:120]})
        elif event in ("os.remove", "os.unlink", "os.rename", "shutil.rmtree", "os.rmdir"):
            p = _norm(args[0]) if args else ""
            if (_state["project"] and _under(p, [_state["project"]])) or (_state["data_full"] and _under(p, [_state["data_full"]])):
                _state["violations"].append({"event": event, "detail": p[-120:]})
                raise Tripwire(f"{event} on protected files is not allowed")
    except Tripwire:
        raise
    except Exception:  # noqa: BLE001   the hook itself must never break the run
        return


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True, help="the run's output folder (the only project-side write target)")
    ap.add_argument("--data-dir", required=True, help="folder with the train shards only")
    ap.add_argument("--data-full", default="", help="the full data folder (never readable from here)")
    ap.add_argument("--wall-cap", type=float, default=0.0, help="seconds; 0 = none")
    ap.add_argument("--audit", required=True, help="where to write the audit record")
    ap.add_argument("--project", default=str(Path(__file__).resolve().parent.parent))
    ap.add_argument("--allow-val", action="store_true", help="the exam may read the validation split")
    ap.add_argument("script")
    ap.add_argument("script_args", nargs=argparse.REMAINDER)
    a = ap.parse_args()
    out = Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    if not a.allow_val:                       # a trainer: no stale weights may survive into the exam
        for stale in ("model.pt",):           # (the exam itself runs with --allow-val and must keep them)
            try:
                (out / stale).unlink()
            except FileNotFoundError:
                pass
    os.environ["HTSA_DATA_DIR"] = a.data_dir
    os.environ.setdefault("PYTHONUNBUFFERED", "1")
    t0 = time.time()
    audit = {"violations": _state["violations"], "notes": _state["notes"], "timed_out": False, "wall": None, "rc": None}

    def write_audit() -> None:
        audit["wall"] = round(time.time() - t0, 1)
        try:
            Path(a.audit).write_text(json.dumps(audit, indent=1), encoding="utf-8")
        except Exception:  # noqa: BLE001
            pass

    if a.wall_cap > 0:
        def watchdog() -> None:
            time.sleep(a.wall_cap)
            audit["timed_out"] = True
            audit["rc"] = 124
            write_audit()
            os._exit(124)
        threading.Thread(target=watchdog, daemon=True).start()

    # torch loads its native libraries through ctypes at import; do that before the tripwire arms
    try:
        import numpy  # noqa: F401
        import torch  # noqa: F401
    except Exception:  # noqa: BLE001
        pass
    _state["allow_write"] = [_norm(out), _norm(tempfile.gettempdir())]
    for var in ("LOCALAPPDATA", "TEMP", "TMP", "TORCHINDUCTOR_CACHE_DIR", "TRITON_CACHE_DIR"):
        if os.environ.get(var):
            _state["allow_write"].append(_norm(os.environ[var]))
    _state["project"] = _norm(a.project)
    _state["data_full"] = _norm(a.data_full) if a.data_full else ""
    _state["allow_val"] = bool(a.allow_val)
    sys.addaudithook(_hook)
    _state["armed"] = True
    sys.argv = [a.script] + [x for x in a.script_args if x != "--"]
    rc = 0
    try:
        runpy.run_path(a.script, run_name="__main__")
    except SystemExit as e:
        rc = int(e.code) if isinstance(e.code, int) else (0 if e.code is None else 1)
    except Tripwire as e:
        print(f"[launch] tripwire: {e}", file=sys.stderr)
        rc = 125
    except Exception as e:  # noqa: BLE001
        import traceback
        traceback.print_exc()
        if _state["violations"]:
            rc = 125
        else:
            rc = 1
    _state["armed"] = False
    audit["rc"] = rc
    write_audit()
    return rc


if __name__ == "__main__":
    raise SystemExit(main())
