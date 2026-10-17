"""The hub: one page that lists the spaces on this PC, makes a new one, opens or stops one. Each space is its own
server process (python -m space.server) on its own port, started here as a detached process; the registry is
<lab>/spaces/hub.json and each server's output goes to <lab>/spaces/<name>/server.log.
Run: python -m space.hub (http://127.0.0.1:8760/). Standard library only."""
from __future__ import annotations

import argparse
import json
import os
import re
import socket
import subprocess
import sys
import threading
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlparse

from space import auth, contract
from space.launch import PYTHON, REPO, _now, kill_tree, lab_root, pid_alive, proc_created
from space.store import Reject

HUB_PORT = 8760
WEB = Path(__file__).resolve().parent / "web"
NAME_RE = re.compile(r"^[a-z0-9][a-z0-9_-]{0,31}$")
KEY_RE = re.compile(r"lan key: (\S+)")
STATIC_TYPES = {".html": "text/html; charset=utf-8", ".css": "text/css; charset=utf-8", ".js": "text/javascript; charset=utf-8",
                ".mjs": "text/javascript; charset=utf-8", ".json": "application/json", ".woff2": "font/woff2", ".svg": "image/svg+xml"}


def clean_name(raw) -> str:
    n = re.sub(r"[^a-z0-9_-]+", "-", str(raw or "").strip().lower()).strip("-")[:32]
    if not n or not NAME_RE.match(n):
        raise Reject(422, "bad_name", hint="letters, digits, - and _ only, 1 to 32 characters")
    return n


def free_port(start: int = contract.PORT) -> int:
    for p in range(start, start + 40):
        with socket.socket() as s:
            try:
                s.bind(("127.0.0.1", p))
                return p
            except OSError:
                continue
    raise Reject(500, "no_free_port")


class Hub:
    def __init__(self, spaces_dir: Path):
        self.dir = Path(spaces_dir)
        self.lock = threading.Lock()

    def _path(self) -> Path:
        return self.dir / "hub.json"

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

    @staticmethod
    def _key_of(rec: dict) -> str:
        if not rec.get("lan"):
            return ""
        try:
            m = KEY_RE.search(Path(rec["log"]).read_text(encoding="utf-8", errors="replace"))
            return m.group(1) if m else ""
        except OSError:
            return ""

    def _live_ports(self) -> dict:
        """space_id -> port for every space server answering on the usual ports (spaces started outside the hub)."""
        import urllib.request
        out = {}
        for port in range(contract.PORT, contract.PORT + 40):
            with socket.socket() as s:
                s.settimeout(0.05)
                try:
                    s.connect(("127.0.0.1", port))
                except OSError:
                    continue
            try:
                with urllib.request.urlopen("http://127.0.0.1:%d/api/people" % port, timeout=0.5) as r:
                    d = json.loads(r.read().decode("utf-8", "replace"))
                sid = d.get("space_id") if isinstance(d, dict) else None
                if sid:
                    out[str(sid)] = port
            except Exception:  # noqa: BLE001
                continue
        return out

    def _row(self, r: dict, live: dict | None = None) -> dict:
        alive = pid_alive(r.get("pid"), r.get("created"))
        if not alive and live and r["name"] in live:          # started outside the hub (the stage, or by hand)
            r = dict(r, port=live[r["name"]])
            alive = True
        key = self._key_of(r) if alive else ""
        url = "http://127.0.0.1:%d" % r["port"]
        db = Path(r["db"])
        people = []
        try:
            if db.exists():
                import sqlite3
                con = sqlite3.connect(f"file:{db}?mode=ro", uri=True, timeout=1)
                try:
                    cur = con.execute("select distinct owner from events where by_kind='human' and owner is not null order by owner")
                    people = [x[0] for x in cur.fetchall()]
                except sqlite3.Error:
                    people = []
                finally:
                    con.close()
        except Exception:  # noqa: BLE001
            people = []
        return {"name": r["name"], "port": r["port"], "url": url, "alive": alive, "lan": bool(r.get("lan")), "key": key,
                "db": str(db), "created": r.get("started"), "stopped": r.get("stopped"), "people": people,
                "join": url + "/?me=" + "{name}" + (f"&key={key}" if key else "")}

    def list(self) -> dict:
        rows = self._load()
        seen = {r["name"] for r in rows}
        # folders made by hand (python -m space.server --db .../<name>/space.db) show too, as not started here
        try:
            for d in sorted(self.dir.iterdir()):
                if d.is_dir() and (d / "space.db").exists() and d.name not in seen:
                    rows.append({"name": d.name, "port": 0, "db": str(d / "space.db"), "pid": None, "created": None,
                                 "lan": False, "log": "", "started": None, "stopped": None, "external": True})
        except OSError:
            pass
        live = self._live_ports()
        out = [self._row(r, live) for r in rows]
        out.sort(key=lambda x: (not x["alive"], x["name"]))
        from space.people import me_default
        return {"spaces": out, "hub": {"port": HUB_PORT, "lab": str(lab_root()), "me_default": me_default()}}

    def create(self, raw_name, lan=False, memory_dir=None, me=None) -> dict:
        name = clean_name(raw_name)
        with self.lock:
            rows = self._load()
            for r in rows:
                if r["name"] == name and pid_alive(r.get("pid"), r.get("created")):
                    return dict(self._row(r), already=True)
            rows = [r for r in rows if r["name"] != name]
            port = free_port()
            folder = self.dir / name
            folder.mkdir(parents=True, exist_ok=True)
            py = PYTHON if os.path.exists(PYTHON) else sys.executable
            cmd = [py, "-m", "space.server", "--db", str(folder / "space.db"), "--space-id", name, "--port", str(port)]
            if lan:
                cmd.append("--lan")
            if memory_dir:
                cmd += ["--memory-dir", str(memory_dir)]
            log = folder / "server.log"
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
            rec = {"name": name, "port": port, "db": str(folder / "space.db"), "pid": proc.pid,
                   "created": proc_created(proc.pid), "lan": bool(lan), "log": str(log), "started": _now(), "stopped": None}
            rows.append(rec)
            self._save(rows)
        # wait up to 8 s for the server to answer, so the page can open it at once
        for _ in range(80):
            with socket.socket() as s:
                s.settimeout(0.2)
                try:
                    s.connect(("127.0.0.1", port))
                    break
                except OSError:
                    time.sleep(0.1)
        self._start_my_agent(port, me)
        return self._row(rec)

    @staticmethod
    def _start_my_agent(port: int, me: str | None = None) -> None:
        """The person who made the space gets their agent as soon as it exists (Sonnet, canned fallback). The agent
        is a local process, so the request goes as the agent itself, which needs no session."""
        import urllib.request
        from space.people import me_default
        me = me or me_default()
        try:
            body = json.dumps({"name": me, "model": "sonnet"}).encode("utf-8")
            req = urllib.request.Request("http://127.0.0.1:%d/api/people/add" % port, data=body,
                                         headers={"Content-Type": "application/json", "X-Space-Actor": f"{me}.agent",
                                                  "X-Space-Kind": "agent"}, method="POST")
            urllib.request.urlopen(req, timeout=5).read()
        except Exception:  # noqa: BLE001
            pass

    def stop(self, raw_name) -> dict:
        name = clean_name(raw_name)
        with self.lock:
            rows = self._load()
            hit = [r for r in rows if r["name"] == name]
            if not hit:
                raise Reject(404, "no_space", name=name)
            killed = kill_tree(hit[-1].get("pid"))
            hit[-1]["stopped"] = _now()
            self._save(rows)
        return {"name": name, "stopped": killed}

    def start(self, raw_name) -> dict:
        """Start again a space that was stopped (same folder, a free port)."""
        name = clean_name(raw_name)
        rows = self._load()
        hit = [r for r in rows if r["name"] == name]
        lan = bool(hit[-1].get("lan")) if hit else False
        return self.create(name, lan=lan)


class Handler(BaseHTTPRequestHandler):
    server_version = "HTSAHub/1"

    def log_message(self, fmt, *args):  # quiet
        pass

    def _send(self, code: int, body, ctype="application/json", cookie=None):
        data = body if isinstance(body, bytes) else json.dumps(body).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(data)))
        self.send_header("Cache-Control", "no-store")
        if cookie:
            self.send_header("Set-Cookie", cookie)
        self.end_headers()
        self.wfile.write(data)

    def _auth(self, path, body) -> bool:
        res = auth.handle(path, body if isinstance(body, dict) else {}, self.headers, self.client_address, None,
                          "http://127.0.0.1:%d" % self.server.server_address[1])
        if res is None:
            return False
        code, obj, cookie = res
        self._send(code, obj, cookie=cookie)
        return True

    def _user(self) -> str:
        name, _ = auth.whoami(self.headers, self.client_address)
        if not name:
            raise Reject(401, "login_required")
        return name

    def do_GET(self):
        u = urlparse(self.path)
        hub: Hub = self.server.hub
        try:
            if u.path in ("/", "/index.html"):
                return self._send(200, (WEB / "hub.html").read_bytes(), "text/html; charset=utf-8")
            if u.path in ("/api/me", "/api/invites"):
                if self._auth(u.path, {"list": True} if u.path == "/api/invites" else {}):
                    return None
            if u.path == "/api/spaces":
                return self._send(200, dict(hub.list(), me=auth.whoami(self.headers, self.client_address)[0]))
            p = (WEB / u.path.lstrip("/")).resolve()
            if WEB.resolve() in p.parents and p.is_file():
                return self._send(200, p.read_bytes(), STATIC_TYPES.get(p.suffix, "application/octet-stream"))
            self._send(404, {"error": "no_route"})
        except Reject as r:
            self._send(r.code, r.body)

    def do_POST(self):
        u = urlparse(self.path)
        hub: Hub = self.server.hub
        try:
            n = int(self.headers.get("Content-Length") or 0)
            body = json.loads(self.rfile.read(n) or b"{}") if n else {}
            if not isinstance(body, dict):
                raise Reject(422, "bad_envelope")
            if self._auth(u.path, body):
                return None
            if u.path == "/api/spaces":
                me = self._user()
                return self._send(200, hub.create(body.get("name"), lan=bool(body.get("lan")), memory_dir=body.get("memory_dir"), me=me))
            if u.path == "/api/spaces/stop":
                self._user()
                return self._send(200, hub.stop(body.get("name")))
            if u.path == "/api/spaces/start":
                self._user()
                return self._send(200, hub.start(body.get("name")))
            self._send(404, {"error": "no_route"})
        except Reject as r:
            self._send(r.code, r.body)
        except ValueError:
            self._send(422, {"error": "bad_json"})


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="HTSA hub: the spaces on this PC")
    ap.add_argument("--port", type=int, default=HUB_PORT)
    ap.add_argument("--spaces", default=str(lab_root() / "spaces"))
    ap.add_argument("--open", action="store_true", help="open the hub page in the default browser")
    a = ap.parse_args(argv)
    httpd = ThreadingHTTPServer(("127.0.0.1", a.port), Handler)
    httpd.daemon_threads = True
    httpd.hub = Hub(Path(a.spaces))
    print("hub on http://127.0.0.1:%d/  spaces in %s" % (a.port, a.spaces), flush=True)
    if a.open:
        try:
            import webbrowser
            webbrowser.open("http://127.0.0.1:%d/" % a.port)
        except Exception:  # noqa: BLE001
            pass
    try:
        httpd.serve_forever(poll_interval=0.25)
    except KeyboardInterrupt:
        pass
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
