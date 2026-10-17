"""Accounts, logins and invitations for the spaces on this PC. Standard library only.

Users (name, salted password hash) live in <lab>/auth/users.json, sessions in <lab>/auth/sessions.json and invites
in <lab>/auth/invites.json, so the hub and every space server share one login: the browser's session cookie
(htsa_session) is valid on every port of this PC. The person at this PC (the OS login) is the owner: on
127.0.0.1 they are signed in without a password; anyone else signs in with a password, and a new person joins
only with an invitation code made by a signed-in person. A human event is accepted only when the session's name is
the event's author; agents and the loop are local processes and post without a session."""
from __future__ import annotations

import hashlib
import hmac
import json
import os
import re
import secrets
import threading
import time
from pathlib import Path

from space.store import Reject

COOKIE = "htsa_session"
SESSION_DAYS = 30
INVITE_DAYS = 7
NAME_RE = re.compile(r"^[a-z][a-z0-9_]{0,23}$")
_LOCK = threading.Lock()


def clean_name(raw) -> str:
    n = re.sub(r"[^a-z0-9_]+", "_", str(raw or "").strip().lower()).strip("_")[:24]
    if not n or not NAME_RE.match(n):
        raise Reject(422, "bad_name", hint="letters, digits and _ only, 1 to 24 characters, starting with a letter")
    return n


def owner_name() -> str:
    from space.people import me_default
    try:
        return clean_name(me_default())
    except Reject:
        return "owner"


def _dir() -> Path:
    from space.launch import lab_root
    d = lab_root() / "auth"
    d.mkdir(parents=True, exist_ok=True)
    return d


def _load(name: str) -> dict:
    try:
        d = json.loads((_dir() / name).read_text(encoding="utf-8"))
        return d if isinstance(d, dict) else {}
    except (OSError, ValueError):
        return {}


def _save(name: str, data: dict) -> None:
    p = _dir() / name
    tmp = p.with_suffix(".tmp")
    tmp.write_text(json.dumps(data, indent=1), encoding="utf-8")
    os.replace(tmp, p)


def _hash(password: str, salt: str) -> str:
    return hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), bytes.fromhex(salt), 200_000).hex()


def _now() -> float:
    return time.time()


# ---------------------------------------------------------------- users
def users() -> dict:
    return _load("users.json")


def ensure_owner() -> str:
    """The owner account exists (no password until they set one)."""
    name = owner_name()
    with _LOCK:
        u = users()
        if name not in u:
            u[name] = {"name": name, "salt": None, "hash": None, "owner": True, "created": _now()}
            _save("users.json", u)
    return name


def set_password(name: str, password: str) -> None:
    password = str(password or "")
    if len(password) < 4:
        raise Reject(422, "short_password", hint="4 characters at least")
    with _LOCK:
        u = users()
        if name not in u:
            raise Reject(404, "no_user")
        salt = secrets.token_hex(16)
        u[name].update({"salt": salt, "hash": _hash(password, salt)})
        _save("users.json", u)


def check_password(name: str, password: str) -> bool:
    rec = users().get(name)
    if not rec or not rec.get("salt") or not rec.get("hash"):
        return False
    return hmac.compare_digest(_hash(str(password or ""), rec["salt"]), rec["hash"])


# ---------------------------------------------------------------- sessions
def new_session(name: str) -> str:
    tok = secrets.token_urlsafe(24)
    with _LOCK:
        s = _load("sessions.json")
        cut = _now() - SESSION_DAYS * 86400
        s = {k: v for k, v in s.items() if v.get("at", 0) > cut}
        s[tok] = {"name": name, "at": _now()}
        _save("sessions.json", s)
    return tok


def session_name(token: str | None) -> str | None:
    if not token:
        return None
    rec = _load("sessions.json").get(token)
    if not rec or rec.get("at", 0) < _now() - SESSION_DAYS * 86400:
        return None
    return rec.get("name")


def drop_session(token: str | None) -> None:
    if not token:
        return
    with _LOCK:
        s = _load("sessions.json")
        if token in s:
            del s[token]
            _save("sessions.json", s)


def cookie_of(headers) -> str | None:
    raw = headers.get("Cookie") or ""
    for part in raw.split(";"):
        k, _, v = part.strip().partition("=")
        if k == COOKIE and v:
            return v
    return None


def set_cookie(token: str | None) -> str:
    if token:
        return f"{COOKIE}={token}; Path=/; Max-Age={SESSION_DAYS * 86400}; HttpOnly; SameSite=Lax"
    return f"{COOKIE}=; Path=/; Max-Age=0; HttpOnly; SameSite=Lax"


# ---------------------------------------------------------------- invites
def make_invite(by: str, space: str | None, base_url: str) -> dict:
    code = secrets.token_urlsafe(9)
    with _LOCK:
        inv = _load("invites.json")
        inv[code] = {"code": code, "by": by, "space": space, "created": _now(), "expires": _now() + INVITE_DAYS * 86400,
                     "used_by": None, "used": None}
        _save("invites.json", inv)
    return dict(inv[code], url=f"{base_url}/?invite={code}")


def invites_for(space: str | None) -> list[dict]:
    rows = [v for v in _load("invites.json").values() if space is None or v.get("space") in (None, space)]
    return sorted(rows, key=lambda r: -r.get("created", 0))


def use_invite(code: str, name: str) -> dict:
    with _LOCK:
        inv = _load("invites.json")
        rec = inv.get(str(code or ""))
        if not rec:
            raise Reject(403, "bad_invite", hint="no such invitation")
        if rec.get("used_by"):
            raise Reject(403, "bad_invite", hint="this invitation was already used")
        if rec.get("expires", 0) < _now():
            raise Reject(403, "bad_invite", hint="this invitation expired")
        rec["used_by"], rec["used"] = name, _now()
        _save("invites.json", inv)
    return rec


def register(name_raw, password, code) -> str:
    """A new person joins with an invitation: returns the name."""
    name = clean_name(name_raw)
    if len(str(password or "")) < 4:
        raise Reject(422, "short_password", hint="4 characters at least")
    with _LOCK:
        u = users()
        if name in u and u[name].get("hash"):
            raise Reject(409, "name_taken", hint="that name has a password already; sign in instead")
    use_invite(code, name)
    with _LOCK:
        u = users()
        salt = secrets.token_hex(16)
        u[name] = {"name": name, "salt": salt, "hash": _hash(str(password), salt), "owner": False, "created": _now()}
        _save("users.json", u)
    return name


# ---------------------------------------------------------------- the request-level rules
def is_local(client_address) -> bool:
    try:
        return str(client_address[0]) in ("127.0.0.1", "::1", "::ffff:127.0.0.1")
    except (TypeError, IndexError):
        return False


def whoami(headers, client_address) -> tuple[str | None, str | None]:
    """(name, new_cookie_token). The owner on this PC is signed in without a password: a fresh session is made
    when none is present; the token comes back so the caller can set the cookie."""
    tok = cookie_of(headers)
    name = session_name(tok)
    if name:
        return name, None
    if is_local(client_address):
        owner = ensure_owner()
        return owner, new_session(owner)
    return None, None


def require_human(by: str, headers, client_address) -> None:
    """A human event must come from a session whose name is the author; else 401 login_required."""
    name = session_name(cookie_of(headers))
    if name is None and is_local(client_address) and by == owner_name():
        return                                               # the owner's page before its first GET /api/me
    if name != by:
        raise Reject(401, "login_required", who=name, by=by)


def handle(path: str, body: dict, headers, client_address, space_id: str | None, base_url: str):
    """The auth routes shared by the space server and the hub. Returns (code, body, cookie_header_or_None),
    or None when the path is not an auth route."""
    tok = cookie_of(headers)
    if path == "/api/me":
        name, new_tok = whoami(headers, client_address)
        if not name:
            return 401, {"error": "login_required", "owner": owner_name()}, None
        rec = users().get(name) or {}
        return 200, {"name": name, "owner": bool(rec.get("owner")), "has_password": bool(rec.get("hash"))}, (set_cookie(new_tok) if new_tok else None)
    if path == "/api/login":
        name = clean_name(body.get("name"))
        if not check_password(name, body.get("password")):
            raise Reject(401, "bad_login", hint="wrong name or password")
        return 200, {"name": name}, set_cookie(new_session(name))
    if path == "/api/register":
        name = register(body.get("name"), body.get("password"), body.get("invite"))
        return 200, {"name": name}, set_cookie(new_session(name))
    if path == "/api/logout":
        drop_session(tok)
        return 200, {"ok": True}, set_cookie(None)
    if path == "/api/password":
        name = session_name(tok)
        if not name:
            name, _ = whoami(headers, client_address)
        if not name:
            raise Reject(401, "login_required")
        set_password(name, body.get("password"))
        return 200, {"name": name, "has_password": True}, None
    if path == "/api/invites":
        name = session_name(tok)
        if not name:
            name, _ = whoami(headers, client_address)
        if not name:
            raise Reject(401, "login_required")
        if body is not None and body.get("_method", "POST") == "POST" and "list" not in body:
            return 200, make_invite(name, space_id, base_url), None
        return 200, {"invites": invites_for(space_id)}, None
    return None
