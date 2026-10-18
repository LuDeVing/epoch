"""space/app.py: Epoch as a Windows application.

Double-click Epoch.bat (or the shortcut scripts/install_shortcut.ps1 makes): this starts the hub when it is not
running (python -m space.hub, no console window, same lab root) and opens the dashboard in its own window,
an Edge or Chrome "app" window with no address bar, its own profile under the lab folder (so sign-ins persist),
and its own taskbar entry. Spaces open in that window; the top bar's Dashboard button comes back.

    python -m space.app                 start the hub if needed and open the window
    python -m space.app --no-window     only make sure the hub runs (for a scheduled start)
    python -m space.app --url URL       open another page in the app window (a space's join link)

The hub keeps running after the window closes, so the spaces and the runs in them go on; "Sleep" on the
dashboard stops a space. Standard library only."""
from __future__ import annotations

import argparse
import os
import socket
import subprocess
import sys
import time
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
HUB_PORT = 8760
BROWSERS = [
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
]


def lab_root() -> Path:
    sys.path.insert(0, str(REPO))
    from harness.labroot import lab_root as lr
    return lr()


def port_open(port: int, host: str = "127.0.0.1") -> bool:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.3)
    try:
        s.connect((host, port))
        return True
    except OSError:
        return False
    finally:
        s.close()


def python_exe() -> str:
    """The Python the hub runs on: the lab's venv when there is one, else a portable build under the lab's
    python folder, else the Python running this launcher. Everything Epoch needs is in the standard library."""
    lab = lab_root()
    venv = lab / ".venv" / "Scripts" / "python.exe"
    if venv.exists():
        return str(venv)
    for p in sorted((lab / "python").glob("*/python.exe")):
        return str(p)
    return sys.executable


def start_hub(port: int) -> bool:
    """Start the hub as a detached, windowless process; True once its port answers (up to 15 s)."""
    if port_open(port):
        return True
    env = dict(os.environ, HTSA_LAB_ROOT=str(lab_root()), PYTHONUNBUFFERED="1", PYTHONIOENCODING="utf-8")
    log = lab_root() / "spaces" / "hub.log"
    log.parent.mkdir(parents=True, exist_ok=True)
    flags = 0
    if os.name == "nt":
        flags = subprocess.CREATE_NEW_PROCESS_GROUP | getattr(subprocess, "CREATE_NO_WINDOW", 0) | getattr(subprocess, "DETACHED_PROCESS", 0)
    with open(log, "ab") as out:
        subprocess.Popen([python_exe(), "-m", "space.hub", "--port", str(port)], cwd=str(REPO), env=env,
                         stdin=subprocess.DEVNULL, stdout=out, stderr=subprocess.STDOUT, creationflags=flags)
    for _ in range(150):
        if port_open(port):
            return True
        time.sleep(0.1)
    return False


def browser() -> str | None:
    for b in BROWSERS:
        if os.path.exists(b):
            return b
    return None


def open_window(url: str) -> None:
    """An app window: no address bar, its own profile and taskbar entry. Falls back to the default browser."""
    b = browser()
    if not b:
        import webbrowser
        webbrowser.open(url)
        return
    profile = lab_root() / "app-profile"
    profile.mkdir(parents=True, exist_ok=True)
    args = [b, f"--app={url}", f"--user-data-dir={profile}", "--window-size=1500,920", "--no-first-run",
            "--no-default-browser-check", "--disable-features=TranslateUI"]
    subprocess.Popen(args, cwd=str(REPO), stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
                     creationflags=getattr(subprocess, "DETACHED_PROCESS", 0) if os.name == "nt" else 0)


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="Epoch as a Windows application: the hub in the background, the dashboard in its own window")
    ap.add_argument("--port", type=int, default=HUB_PORT, help="the hub's port (8760)")
    ap.add_argument("--url", default="", help="open this page instead of the dashboard")
    ap.add_argument("--no-window", action="store_true", help="start the hub only")
    a = ap.parse_args(argv)
    if not start_hub(a.port):
        print("the hub did not answer on port %d; see %s" % (a.port, lab_root() / "spaces" / "hub.log"), file=sys.stderr)
        return 1
    if not a.no_window:
        open_window(a.url or "http://127.0.0.1:%d/" % a.port)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
