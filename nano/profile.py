"""The active problem profile (docs/GENERIC_SPEC.md section 1).

A profile is a plain dict exported as PROFILE by nano/profiles/<name>.py. It holds every word the prompts
need, the hard constraints, the default problem tree, the baseline artifact and the checker's name. The loop
logic never changes between profiles; only these words and the checker do.

    from nano import profile as PF
    PF.current()            # the active profile: set_current(), else env HTSA_PROFILE, else "llm"
    PF.load(name)           # import nano.profiles.<name>, validate, return a Profile
    PF.set_current(p)       # the loop calls this at start-up (--profile NAME), tests call it too
    PF.fill(text)           # replaces {v:key} placeholders with the active profile's vocabulary
    p.mode                  # "baseline" | "check_only" | "no_check" (explicit or derived; GENERIC_SPEC.md section 6)
"""
from __future__ import annotations

import copy
import importlib
import os
import re
import threading

REQUIRED = ("name", "goal", "aim", "score", "vocab", "constraints", "assumptions", "tree", "lenses",
            "boundary_all", "artifact", "checker")
OPTIONAL = {"checker_args": {}, "docs": {}, "diagnostics": ""}
VOCAB_KEYS = ("artifact", "artifact_file", "language", "run", "score_phrase", "score_name", "parts", "recipe",
              "cheap_test", "cost_axes", "first_check", "targets", "scope_default", "levers", "known_tricks",
              "boundary_all")
DEFAULT = "llm"
_PLACEHOLDER = re.compile(r"\{v:([A-Za-z0-9_]+)\}")


class ProfileError(ValueError):
    """A profile module is missing or lacks a required key."""


class Profile:
    """Attribute access to the profile dict: p.name, p.vocab, p.tree, ... plus a few helpers."""

    def __init__(self, data: dict):
        object.__setattr__(self, "_d", data)

    def __getattr__(self, key: str):
        d = object.__getattribute__(self, "_d")
        if key in d:
            return d[key]
        raise AttributeError(key)

    def __setattr__(self, key, value):
        raise AttributeError("a Profile is read-only; build a new one with PF.load or Profile(dict)")

    def __getitem__(self, key: str):
        return self._d[key]

    def __contains__(self, key: str) -> bool:
        return key in self._d

    def get(self, key: str, default=None):
        return self._d.get(key, default)

    def as_dict(self) -> dict:
        return copy.deepcopy(self._d)

    def v(self, key: str, default: str = "") -> str:
        """One vocabulary word as text; a list (targets) is joined with commas."""
        val = self._d.get("vocab", {}).get(key)
        if val is None:
            return default
        if isinstance(val, (list, tuple)):
            return ", ".join(str(x) for x in val)
        return str(val)

    @property
    def mode(self) -> str:
        """"baseline", "check_only" or "no_check" (docs/GENERIC_SPEC.md section 6): the explicit PROFILE["mode"],
        else derived: checker "panel" -> no_check; artifact.path None -> check_only; otherwise baseline."""
        return derive_mode(self._d)

    @property
    def interface(self) -> str:
        """Mode 2 and 3: the text of the form a candidate must have (artifact["interface"]); '' when absent."""
        return str((self._d.get("artifact") or {}).get("interface") or "")

    def skeleton_text(self) -> str:
        """The empty template file named by artifact["skeleton"] (relative to the repo root), or ''."""
        rel = (self._d.get("artifact") or {}).get("skeleton")
        if not rel:
            return ""
        from pathlib import Path
        path = Path(rel) if Path(rel).is_absolute() else Path(__file__).resolve().parent.parent / rel
        try:
            return path.read_text(encoding="utf-8")
        except OSError:
            return ""

    @property
    def lower_is_better(self) -> bool:
        return str((self._d.get("score") or {}).get("direction", "lower")).lower() != "higher"

    def __repr__(self) -> str:
        return f"Profile({self._d.get('name')!r})"


MODES = ("baseline", "check_only", "no_check")


def derive_mode(d: dict) -> str:
    """The profile's mode: explicit, else panel checker -> no_check, no artifact path -> check_only, else baseline."""
    m = d.get("mode")
    if m:
        return str(m)
    if str(d.get("checker", "")).strip() == "panel":
        return "no_check"
    if not (d.get("artifact") or {}).get("path"):
        return "check_only"
    return "baseline"


def _validate(name: str, data: dict) -> dict:
    if not isinstance(data, dict):
        raise ProfileError(f"nano.profiles.{name}.PROFILE is not a dict")
    missing = [k for k in REQUIRED if k not in data]
    if missing:
        raise ProfileError(f"profile {name!r} lacks required keys: {', '.join(missing)}")
    d = dict(data)
    for k, default in OPTIONAL.items():
        d.setdefault(k, copy.deepcopy(default))
    if not isinstance(d["vocab"], dict):
        raise ProfileError(f"profile {name!r}: vocab must be a dict")
    vocab = dict(d["vocab"])
    vocab.setdefault("boundary_all", d["boundary_all"])               # one source for both places
    vocab.setdefault("score_name", (d.get("score") or {}).get("name", "score"))
    d["vocab"] = vocab
    if "parts" not in (d.get("lenses") or {}):
        raise ProfileError(f"profile {name!r}: lenses must include 'parts'")
    if not isinstance(d.get("artifact"), dict) or "path" not in d["artifact"]:
        raise ProfileError(f"profile {name!r}: artifact must be a dict with a 'path'")
    mode = derive_mode(d)
    if mode not in MODES:
        raise ProfileError(f"profile {name!r}: mode must be one of {', '.join(MODES)}, not {mode!r}")
    if mode == "baseline" and not d["artifact"].get("path"):
        raise ProfileError(f"profile {name!r}: mode 'baseline' needs artifact.path")
    if mode != "baseline" and not (d["artifact"].get("interface") or d["artifact"].get("skeleton")):
        raise ProfileError(f"profile {name!r}: mode {mode!r} needs artifact.interface (or a skeleton)")
    if mode == "no_check" and str(d.get("checker")) != "panel":
        raise ProfileError(f"profile {name!r}: mode 'no_check' needs checker 'panel'")
    return d


_cache: dict[str, Profile] = {}
_current: Profile | None = None
_lock = threading.Lock()


def load(name: str) -> Profile:
    """Import nano.profiles.<name>, validate its PROFILE and return it (cached by name)."""
    name = str(name or DEFAULT).strip() or DEFAULT
    with _lock:
        if name in _cache:
            return _cache[name]
    try:
        mod = importlib.import_module(f"nano.profiles.{name}")
    except ModuleNotFoundError as e:
        if e.name in (f"nano.profiles.{name}", "nano.profiles"):
            raise ProfileError(f"no profile named {name!r} (expected nano/profiles/{name}.py)") from e
        raise
    p = Profile(_validate(name, getattr(mod, "PROFILE", None)))
    with _lock:
        _cache[name] = p
    return p


def set_current(profile: Profile | str) -> Profile:
    global _current
    if isinstance(profile, str):
        profile = load(profile)
    _current = profile
    return profile


def current() -> Profile:
    global _current
    if _current is None:
        _current = load(os.environ.get("HTSA_PROFILE") or DEFAULT)
    return _current


def fill(text: str, profile: Profile | None = None) -> str:
    """Replace {v:key} placeholders with vocabulary of the given (default: active) profile. An unknown key is
    left as it is, so a missing word shows in the prompt file instead of silently vanishing."""
    p = profile or current()
    vocab = p.vocab

    def sub(m: re.Match) -> str:
        return p.v(m.group(1)) if m.group(1) in vocab else m.group(0)
    return _PLACEHOLDER.sub(sub, str(text))
