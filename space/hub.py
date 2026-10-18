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
                ".mjs": "text/javascript; charset=utf-8", ".json": "application/json", ".woff2": "font/woff2", ".svg": "image/svg+xml", ".ico": "image/x-icon"}


def clean_name(raw) -> str:
    n = re.sub(r"[^a-z0-9_-]+", "-", str(raw or "").strip().lower()).strip("-")[:32]
    if not n or not NAME_RE.match(n):
        raise Reject(422, "bad_name", hint="letters, digits, - and _ only, 1 to 32 characters")
    return n


def _pids_on_port(port: int) -> list[int]:
    """The processes listening on a local port (netstat), for a server the hub did not start itself."""
    if os.name != "nt":
        return []
    try:
        out = subprocess.run(["netstat", "-ano", "-p", "tcp"], capture_output=True, text=True, timeout=10,
                             creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0)).stdout
    except (OSError, subprocess.SubprocessError):
        return []
    pids = []
    for line in out.splitlines():
        parts = line.split()
        if len(parts) >= 5 and parts[3] == "LISTENING" and parts[1].endswith(":%d" % port):
            try:
                pids.append(int(parts[4]))
            except ValueError:
                pass
    return pids


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
            keys = KEY_RE.findall(Path(rec["log"]).read_text(encoding="utf-8", errors="replace"))
            return keys[-1] if keys else ""                      # the log keeps every start: the latest key is the live one
        except OSError:
            return ""

    def _live_ports(self) -> dict:
        """space_id -> port for every space server answering on the usual ports (spaces started outside the hub)."""
        import urllib.request
        out = {}

        def probe(port):
            with socket.socket() as s:
                s.settimeout(0.05)
                try:
                    s.connect(("127.0.0.1", port))
                except OSError:
                    return None
            try:
                with urllib.request.urlopen("http://127.0.0.1:%d/api/people" % port, timeout=0.5) as r:
                    d = json.loads(r.read().decode("utf-8", "replace"))
                sid = d.get("space_id") if isinstance(d, dict) else None
                return (str(sid), port) if sid else None
            except Exception:  # noqa: BLE001
                return None
        from concurrent.futures import ThreadPoolExecutor
        with ThreadPoolExecutor(max_workers=40) as ex:          # all ports at once: a closed port costs its timeout
            for hit in ex.map(probe, range(contract.PORT, contract.PORT + 40)):
                if hit:
                    out[hit[0]] = hit[1]
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
        try:
            import datetime as _dt
            updated = _dt.datetime.fromtimestamp(db.stat().st_mtime).isoformat(timespec="seconds") if db.exists() else None
        except OSError:
            updated = None
        return {"name": r["name"], "port": r["port"], "url": url, "alive": alive, "lan": bool(r.get("lan")), "key": key,
                "db": str(db), "created": r.get("started"), "stopped": r.get("stopped"), "people": people, "updated": updated,
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
            kw = ({"creationflags": subprocess.CREATE_NEW_PROCESS_GROUP | subprocess.CREATE_NO_WINDOW} if os.name == "nt"
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
        if me:
            auth.add_member(name, me)
        self._start_my_agent(port, me, self._key_of(rec) if lan else "")
        return self._row(rec)

    @staticmethod
    def _start_my_agent(port: int, me: str | None = None, key: str = "") -> None:
        """The person who made the space gets their agent as soon as it exists (Sonnet, canned fallback). The agent
        is a local process, so the request goes as the agent itself, which needs no session. A --lan space wants
        its key on the request, or it refuses and the person has no agent."""
        import urllib.request
        from space.people import me_default
        me = me or me_default()
        try:
            body = json.dumps({"name": me, "model": "sonnet"}).encode("utf-8")
            h = {"Content-Type": "application/json", "X-Space-Actor": f"{me}.agent", "X-Space-Kind": "agent"}
            if key:
                h["X-Space-Key"] = key
            req = urllib.request.Request("http://127.0.0.1:%d/api/people/add" % port, data=body, headers=h, method="POST")
            urllib.request.urlopen(req, timeout=5).read()
        except Exception:  # noqa: BLE001
            pass

    def busy(self) -> dict:
        """What would be interrupted by a shutdown: the spaces that are up and the research runs still going
        (a run is a process recorded in <space>/runs/runs.json; alive by pid and creation time)."""
        live = self._live_ports()
        spaces, runs = [], []
        for r in self._load():
            up = pid_alive(r.get("pid"), r.get("created")) or r["name"] in live
            if up:
                spaces.append(r["name"])
            try:
                rows = json.loads((Path(r["db"]).parent / "runs" / "runs.json").read_text(encoding="utf-8"))
            except (OSError, ValueError):
                rows = []
            for run in rows if isinstance(rows, list) else []:
                if pid_alive(run.get("pid"), run.get("created")):
                    runs.append({"space": r["name"], "batch": run.get("batch"), "preset": run.get("preset"), "started": run.get("started")})
        return {"spaces": spaces, "runs": runs}

    def stop_all(self) -> dict:
        """Stop every space server this hub started (their runs and agents go with them: taskkill /T)."""
        stopped = []
        with self.lock:
            rows = self._load()
            for r in rows:
                if pid_alive(r.get("pid"), r.get("created")):
                    if kill_tree(r.get("pid")):
                        stopped.append(r["name"])
                    r["stopped"] = _now()
            self._save(rows)
        return {"stopped": stopped}

    def remove(self, raw_name, me=None) -> dict:
        """Remove a space from this PC: its server is stopped, its folder (log, files, knowledge, run records) moves
        to <lab>/trash/<name>-<time> and its record goes. The hub's owner or the space's first member may do it."""
        name = clean_name(raw_name)
        members = auth.members_of(name) or []
        if me and me != auth.owner_name() and (members and members[0] != me):
            raise Reject(403, "not_yours", hint="only the owner of this PC or the person who made the space can remove it")
        with self.lock:
            rows = self._load()
            hit = [r for r in rows if r["name"] == name]
            folder = self.dir / name
            if not hit and not folder.exists():
                raise Reject(404, "no_space", name=name)
            for r in hit:
                if pid_alive(r.get("pid"), r.get("created")):
                    kill_tree(r.get("pid"))
            live = self._live_ports()
            if name in live:                                   # started outside the hub: stop it through its port owner
                for pid in _pids_on_port(live[name]):
                    kill_tree(pid)
            moved = None
            if folder.exists():
                import shutil
                trash = lab_root() / "trash"
                trash.mkdir(parents=True, exist_ok=True)
                moved = trash / f"{name}-{time.strftime('%Y%m%d-%H%M%S')}"
                for _ in range(20):                            # the server lets go of the database within a moment
                    try:
                        shutil.move(str(folder), str(moved))
                        break
                    except OSError:
                        time.sleep(0.25)
                else:
                    raise Reject(500, "folder_busy", hint="the space's files are still in use; try again in a moment")
            self._save([r for r in rows if r["name"] != name])
        return {"name": name, "moved_to": str(moved) if moved else None}

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

    def start(self, raw_name, me=None) -> dict:
        """Wake a sleeping space (same folder, a free port); the person who wakes it gets their agent."""
        name = clean_name(raw_name)
        rows = self._load()
        hit = [r for r in rows if r["name"] == name]
        lan = bool(hit[-1].get("lan")) if hit else False
        return self.create(name, lan=lan, me=me)


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
            if u.path == "/api/busy" and self.client_address[0] == "127.0.0.1":   # the local launcher asks before a shutdown
                return self._send(200, hub.busy())
            if u.path in ("/api/me", "/api/invites"):
                if self._auth(u.path, {"list": True} if u.path == "/api/invites" else {}):
                    return None
            if u.path == "/api/spaces":
                me = auth.whoami(self.headers, self.client_address)[0]
                if not me:
                    raise Reject(401, "login_required")
                d = hub.list()
                rows = []
                for row in d["spaces"]:
                    row["members"] = auth.members_of(row["name"])
                    row["open_to_all"] = row["members"] is None
                    row["member"] = auth.is_member(row["name"], me)
                    # your own spaces always; an open room (no members list) only while it runs, so old stage
                    # folders do not pile up on the page
                    if row["member"] and (not row["open_to_all"] or row["alive"]):
                        rows.append(row)
                return self._send(200, dict(d, spaces=rows, me=me))
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
            if u.path == "/api/window" and self.client_address[0] == "127.0.0.1":     # a second app window, its own identity
                from space.app import open_window, browser
                n = int(body.get("n") or 2)
                proc = open_window("http://127.0.0.1:%d/" % self.server.server_address[1], profile="app-profile-%d" % n)
                return self._send(200, {"opened": True, "profile": n, "app_window": proc is not None, "browser": bool(browser())})
            if u.path == "/api/shutdown" and self.client_address[0] == "127.0.0.1":   # the local launcher: stop everything
                out = hub.stop_all()
                self._send(200, dict(out, hub="stopping"))
                threading.Thread(target=self.server.shutdown, daemon=True).start()
                return None
            if self._auth(u.path, body):
                return None
            if u.path == "/api/spaces":
                me = self._user()
                return self._send(200, hub.create(body.get("name"), lan=bool(body.get("lan")), memory_dir=body.get("memory_dir"), me=me))
            if u.path == "/api/spaces/stop":
                self._user()
                return self._send(200, hub.stop(body.get("name")))
            if u.path == "/api/spaces/remove":
                return self._send(200, hub.remove(body.get("name"), me=self._user()))
            if u.path == "/api/spaces/start":
                return self._send(200, hub.start(body.get("name"), me=self._user()))
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
