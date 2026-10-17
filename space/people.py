"""People from the page: list who is in the space and whether their agent runs, start a person-agent for a name,
stop it. Routes (registered on the space server next to space/launch.py): GET /api/people, POST /api/people/add
{name, model}, POST /api/people/stop {name}. The agents are detached processes; their records live in
<space folder>/agents/procs.json and their logs next to it. Standard library only."""
from __future__ import annotations

import json
import os
import re
import subprocess
import sys
import threading
from pathlib import Path

from space import contract
from space.launch import PYTHON, REPO, _now, kill_tree, lab_root, pid_alive, proc_created
from space.store import Reject

MODELS = ("mock", "sonnet")


def me_default() -> str:
    """The name the person at this PC joins with when none is given: the OS login, cleaned; else owner."""
    raw = os.environ.get("USERNAME") or os.environ.get("USER") or ""
    if not raw:
        try:
            import getpass
            raw = getpass.getuser()
        except Exception:  # noqa: BLE001
            raw = ""
    n = re.sub(r"[^a-z0-9_-]+", "-", str(raw).strip().lower()).strip("-")[:24]
    return n if n and NAME_RE.match(n) else "owner"


def lan_ip() -> str:
    """This PC's address on the local network (the one other laptops use), or '' when unknown."""
    import socket
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.connect(("10.255.255.255", 1))
            return s.getsockname()[0]
    except OSError:
        return ""
NAME_RE = re.compile(r"^[a-z][a-z0-9_-]{0,23}$")


def clean_name(raw) -> str:
    n = re.sub(r"[^a-z0-9_-]+", "-", str(raw or "").strip().lower()).strip("-")[:24]
    if not n or not NAME_RE.match(n):
        raise Reject(422, "bad_name", hint="letters, digits, - and _ only, 1 to 24 characters")
    return n


class People:
    def __init__(self, space_dir: Path, space_url: str, space_id: str | None, key: str = ""):
        self.dir = Path(space_dir) / "agents"
        self.url, self.space_id, self.key = space_url, space_id, key
        self.lock = threading.Lock()

    # ---- registry
    def _path(self) -> Path:
        return self.dir / "procs.json"

    def _load(self) -> list[dict]:
        try:
            rows = json.loads(self._path().read_text(encoding="utf-8"))
            return rows if isinstance(rows, list) else []
        except (OSError, ValueError):
            return []

    def _save(self, rows: list[dict]) -> None:
        self.dir.mkdir(parents=True, exist_ok=True)
        tmp = self._path().with_suffix(".tmp")
        tmp.write_text(json.dumps(rows, indent=1), encoding="utf-8")
        os.replace(tmp, self._path())

    def join_url(self, name: str) -> str:
        return f"{self.url}/?me={name}" + (f"&key={self.key}" if self.key else "")

    def command(self, name: str, model: str) -> list[str]:
        py = PYTHON if os.path.exists(PYTHON) else sys.executable
        cmd = [py, "-m", "space.agent", "--me", name, "--model", model, "--fallback", "mock", "--space", self.url]
        if self.space_id:
            cmd += ["--space-id", self.space_id]
        if self.key:
            cmd += ["--key", self.key]
        return cmd

    # ---- routes
    def status(self, people_in_log, roster=None) -> dict:
        rows = self._load()
        by = {}
        # an agent started outside this panel (the stage, or by hand) shows as alive while it is in the presence roster
        for r in roster or ():
            who = str((r.get("by") if isinstance(r, dict) else r) or "")
            if who.endswith(".agent"):
                by[who[:-6]] = {"alive": True, "pid": None, "model": "running", "started": None, "ended": None, "log": None}
        changed = False
        for r in rows:
            alive = pid_alive(r.get("pid"), r.get("created"))
            if not alive and not r.get("ended"):
                r["ended"] = _now()
                changed = True
            if alive or r["name"] not in by:
                by[r["name"]] = {"alive": alive, "pid": r.get("pid"), "model": r.get("model"), "started": r.get("started"),
                                 "ended": r.get("ended"), "log": r.get("log")}
        if changed:
            self._save(rows)
        names = []
        for p in people_in_log or []:
            n = p.get("name") if isinstance(p, dict) else p
            if n and n not in names:
                names.append(n)
        for n in by:
            if n not in names:
                names.append(n)
        ip = lan_ip() if self.key else ""
        port = self.url.rsplit(":", 1)[-1]
        invite = f"http://{ip}:{port}/?key={self.key}" if ip and self.key else ""
        return {"url": self.url, "space_id": self.space_id, "lan": bool(self.key), "models": list(MODELS),
                "me_default": me_default(), "invite_url": invite,
                "people": [{"name": n, "join_url": self.join_url(n), "agent": by.get(n)} for n in names]}

    def add(self, raw_name, model) -> dict:
        name = clean_name(raw_name)
        model = str(model or "mock").lower()
        if model not in MODELS:
            raise Reject(422, "bad_model", models=list(MODELS))
        with self.lock:
            rows = self._load()
            for r in rows:
                if r["name"] == name and pid_alive(r.get("pid"), r.get("created")):
                    return {"name": name, "join_url": self.join_url(name), "already": True, "pid": r.get("pid")}
            cmd = self.command(name, model)
            self.dir.mkdir(parents=True, exist_ok=True)
            log = self.dir / f"{name}.proc.log"
            env = dict(os.environ, HTSA_LAB_ROOT=str(lab_root()), PYTHONUNBUFFERED="1", PYTHONIOENCODING="utf-8")
            kw = ({"creationflags": subprocess.CREATE_NEW_PROCESS_GROUP | subprocess.DETACHED_PROCESS} if os.name == "nt"
                  else {"start_new_session": True})
            with open(log, "ab") as out:
                out.write(("$ %s\n" % " ".join(cmd)).encode("utf-8"))
                out.flush()
                try:
                    proc = subprocess.Popen(cmd, cwd=str(REPO), env=env, stdin=subprocess.DEVNULL, stdout=out,
                                            stderr=subprocess.STDOUT, **kw)
                except OSError as e:
                    raise Reject(500, "spawn_failed", detail=str(e)[:300])
            rows = [r for r in rows if r["name"] != name]
            rows.append({"name": name, "pid": proc.pid, "created": proc_created(proc.pid), "model": model,
                         "cmd": cmd, "started": _now(), "log": str(log), "ended": None})
            self._save(rows)
        return {"name": name, "join_url": self.join_url(name), "pid": proc.pid, "model": model}

    def stop(self, raw_name) -> dict:
        name = clean_name(raw_name)
        with self.lock:
            rows = self._load()
            hit = [r for r in rows if r["name"] == name]
            if not hit:
                raise Reject(404, "no_agent", name=name)
            killed = kill_tree(hit[-1].get("pid"))
            hit[-1]["ended"] = _now()
            self._save(rows)
        return {"name": name, "stopped": killed}


def register(httpd) -> People:
    host, port = httpd.server_address[:2]
    url = "http://%s:%d" % ("127.0.0.1" if host in ("0.0.0.0", "") else host, port)
    sp = getattr(httpd, "space", None)
    db = Path(sp.store.path) if sp is not None else Path("space.db")
    pe = People(db.parent, url, getattr(sp.store, "space_id", None) if sp is not None else None, getattr(httpd, "key", "") or "")
    httpd.people = pe

    def people_route(b, q):
        snap = sp.snapshot(None) if sp is not None else {}
        roster = sp.presence.as_list() if sp is not None and hasattr(sp, "presence") else []
        return pe.status(snap.get("people") if isinstance(snap, dict) else [], roster)

    def add_route(b, q):
        if not isinstance(b, dict):
            raise Reject(422, "bad_envelope")
        return pe.add(b.get("name"), b.get("model", "mock"))

    def stop_route(b, q):
        if not isinstance(b, dict):
            raise Reject(422, "bad_envelope")
        return pe.stop(b.get("name"))

    routes = getattr(httpd, "routes", None)
    if routes is None:
        routes = httpd.routes = {}
    routes[("GET", "/api/people")] = people_route
    routes[("POST", "/api/people/add")] = add_route
    routes[("POST", "/api/people/stop")] = stop_route
    return pe
