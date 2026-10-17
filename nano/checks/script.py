"""The generic checker: any artifact whose score comes from a scorer command (docs/GENERIC_SPEC.md 3).

The profile supplies, in checker_args:
    scorer    a command template, e.g.
              "python nano/profiles/binpack/scorer.py --candidate {candidate} --out {out} --level {level} --seed {seed}"
              The first token may be "python" (dropped: the launcher is the interpreter); the next is the
              scorer script, relative to the repo root. It must write OUT/metrics.json with
              {"score": float, "cost": {axis: float, ...}, "n": int} and exit 0; a non-zero exit is a failure
              and its stderr goes back to the builder. Levels: build, quick, full.
    seeds     the seeds the baseline is measured on (the first one is the matched seed for candidates)
    wall_cap  seconds per scorer run (the launcher kills the run at this cap)
  optional:
    z_tol (4.0), learn_tol (0.0)  rung 2 fails when learn_gap > max(learn_tol, z_tol x baseline seed SD)
    cost_tol (2.0), cost_key      rung 2 fails when cost on cost_key (default: the first cost axis) is above
                                  cost_tol x the baseline's
    deny_imports, deny_names      static denials on top of nano/boundary.py's (see DEFAULT_DENY_*)
    allow_imports                 names removed from the deny lists

Every scorer run goes through nano/launch.py (wall cap, PEP 578 tripwire, audit log); the candidate
runs inside the scorer's process, so the tripwire covers it, and an audit violation fails it.

Ladder (stop at the first failure):
  0 static : boundary of the part, denied imports and calls (nano/boundary.py), introspection names that
             would let the artifact read the scorer's state. A file that does not parse passes here and fails
             at rung 1 with the interpreter's own message.
  1 build  : scorer --level build
  2 quick  : scorer --level quick at the matched seed; learn_gap = (cand - base) at that seed, negated when
             higher is better, so negative is always better; learn_z in units of the baseline's seed SD
             across the quick scores; cost_ratio against the baseline's cost at that seed
  3 full   : scorer --level full at the matched seed; long_gap, long_z; half_gap = learn_gap; trend =
             long_gap - learn_gap; extrap_gap = long_gap + trend. Only a failed run fails here.
long_run() reuses rung 3's result when it exists. final() runs full over the given seeds and applies
nano/verdict.py sequential_verdict with the profile's margin and alpha.
"""
from __future__ import annotations

import ast
import hashlib
import json
import math
import os
import shlex
import statistics
import subprocess
import time
from pathlib import Path

from nano import boundary as bnd
from nano import verdict as V
from nano.checks.base import lower_is_better
from harness import labroot as _labroot  # noqa: E402  (the lab folder, on any computer)

CHECKER = "ScriptChecker"
ROOT = Path(__file__).resolve().parent.parent.parent
HERE_NANO = ROOT / "nano"
LAUNCH = HERE_NANO / "launch.py"
LAB = _labroot.lab_root()
PY = Path(os.environ.get("HTSA_EXEC_PYTHON", str(LAB / ".venv" / "Scripts" / "python.exe")))
PY_NAMES = {"python", "python3", "python.exe", "python3.exe", "py", "{python}"}

# modules a scored artifact has no use for: introspection, the process, files, and the heavy libraries
DEFAULT_DENY_IMPORTS = ("torch", "numpy", "inspect", "gc", "sys", "os", "traceback", "threading", "_thread",
                        "builtins", "signal", "atexit", "tracemalloc", "faulthandler", "io", "pathlib", "tempfile",
                        "glob", "shutil", "pickle", "marshal", "runpy", "importlib", "socket", "subprocess", "ctypes")
# names that reach the caller's frames or the interpreter's state
DEFAULT_DENY_NAMES = ("_getframe", "f_back", "f_locals", "f_globals", "f_code", "gi_frame", "cr_frame", "tb_frame",
                      "__globals__", "__builtins__", "__subclasses__", "__code__", "__import__", "globals", "locals",
                      "vars", "open", "exec", "eval", "compile", "breakpoint", "setattr", "delattr")


def _tail(s: str, n: int = 12) -> str:
    return "\n".join((s or "").strip().splitlines()[-n:])


def _sha(*parts: str) -> str:
    h = hashlib.sha256()
    for p in parts:
        h.update(p.encode("utf-8", "replace"))
        h.update(b"\0")
    return h.hexdigest()[:16]


def _sd(xs: list[float]) -> float | None:
    return statistics.stdev(xs) if len(xs) >= 2 else None


class ScriptChecker:
    LEARN_STEPS = 1            # informational only: the cheap check is the scorer's "quick" level
    LONG_STEPS = 1             # the long check is the "full" level; non-zero so the loop runs it
    PROFILE_SEEDS = (0, 1, 2)

    def __init__(self, profile=None, *, scorer: str, seeds=(0, 1, 2), wall_cap: float = 120.0,
                 z_tol: float = 4.0, learn_tol: float = 0.0, cost_tol: float = 2.0, cost_key: str | None = None,
                 deny_imports=None, deny_names=None, allow_imports=(), **extra):
        self.profile = profile
        self.scorer = scorer
        self.seeds = tuple(int(s) for s in seeds)
        self.PROFILE_SEEDS = self.seeds
        self.check_seed = self.seeds[0]
        self.wall_cap = float(wall_cap)
        self.z_tol, self.learn_tol, self.cost_tol, self.cost_key = float(z_tol), float(learn_tol), float(cost_tol), cost_key
        allow = set(allow_imports or ())
        self.deny_imports = set(DEFAULT_DENY_IMPORTS if deny_imports is None else deny_imports) - allow
        self.deny_names = set(DEFAULT_DENY_NAMES if deny_names is None else deny_names)
        self.extra = extra
        self.sign = 1.0 if (profile is None or lower_is_better(profile)) else -1.0
        art = dict(getattr(profile, "artifact", None) or {})
        self.baseline_path = (ROOT / art["path"]) if art.get("path") else None
        self._script, self._args = self._parse_scorer(scorer)

    # ------------------------------------------------------------ running the scorer
    @staticmethod
    def _parse_scorer(template: str) -> tuple[Path, list[str]]:
        toks = shlex.split(template, posix=True)
        if toks and Path(toks[0]).name.lower() in PY_NAMES:
            toks = toks[1:]
        if not toks:
            raise ValueError(f"scorer command has no script: {template!r}")
        script = Path(toks[0])
        if not script.is_absolute():
            script = ROOT / script
        return script, toks[1:]

    def _score(self, candidate: Path, out: Path, level: str, seed: int) -> dict:
        """One scorer run through the launcher. Returns rc/stdout/stderr/wall/timed_out/violations/metrics."""
        out = Path(out)
        out.mkdir(parents=True, exist_ok=True)
        mp = out / "metrics.json"
        try:
            mp.unlink()
        except FileNotFoundError:
            pass
        nodata = out / "_nodata"
        nodata.mkdir(exist_ok=True)
        audit_path = out / "audit.json"
        subs = {"{candidate}": str(Path(candidate).resolve()), "{out}": str(out.resolve()), "{level}": level,
                "{seed}": str(seed)}
        args = []
        for a in self._args:
            for k, v in subs.items():
                a = a.replace(k, v)
            args.append(a)
        cmd = [str(PY), "-I", str(LAUNCH), "--out", str(out.resolve()), "--data-dir", str(nodata.resolve()),
               "--wall-cap", str(self.wall_cap), "--audit", str(audit_path.resolve()), str(self._script), *args]
        t0 = time.time()
        try:
            p = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace",
                               timeout=self.wall_cap + 60, cwd=str(out), env={**os.environ, "PYTHONUNBUFFERED": "1"})
            res = {"rc": p.returncode, "stdout": p.stdout[-4000:], "stderr": p.stderr[-4000:],
                   "wall": round(time.time() - t0, 2), "timed_out": p.returncode == 124}
        except subprocess.TimeoutExpired:
            res = {"rc": None, "stdout": "", "stderr": "", "wall": round(time.time() - t0, 2), "timed_out": True}
        audit = {}
        try:
            audit = json.loads(audit_path.read_text(encoding="utf-8"))
        except Exception:  # noqa: BLE001
            pass
        res["violations"] = [f"{v.get('event')}: {v.get('detail')}" for v in audit.get("violations", [])]
        m = None
        if mp.exists():
            try:
                m = json.loads(mp.read_text(encoding="utf-8"))
                if not isinstance(m.get("score"), (int, float)) or not math.isfinite(m["score"]):
                    res["bad_metrics"] = "metrics.json has no numeric score"
                    m = None
            except Exception as e:  # noqa: BLE001
                res["bad_metrics"] = f"metrics.json unreadable: {e}"
                m = None
        res["metrics"] = m if res["rc"] == 0 else None
        if mp.exists() and (res["metrics"] is None or res["violations"]):
            mp.replace(out / "metrics.rejected.json")    # long_run() reuses a metrics.json: only a clean run's
        return res

    def _cost(self, m: dict | None) -> float | None:
        c = (m or {}).get("cost") or {}
        if not isinstance(c, dict) or not c:
            return None
        key = self.cost_key or next(iter(c))
        v = c.get(key)
        return float(v) if isinstance(v, (int, float)) else None

    @staticmethod
    def _fail_reason(r: dict, what: str) -> dict:
        if r.get("violations"):
            return {"reason": "integrity: the run did something the artifact may not do", "violations": r["violations"][:8]}
        if r.get("timed_out"):
            return {"reason": f"{what} hit the wall-clock cap", "stderr": _tail(r.get("stderr", ""))}
        return {"reason": f"{what} failed" + (f" ({r['bad_metrics']})" if r.get("bad_metrics") else ""),
                "rc": r.get("rc"), "stderr": _tail(r.get("stderr", "")), "stdout": _tail(r.get("stdout", ""), 4)}

    # ------------------------------------------------------------ rung 0
    def static_check(self, baseline_src: str | None, cand_src: str, boundary: str | None) -> dict:
        try:
            tree = ast.parse(cand_src)
        except SyntaxError as e:
            return {"ok": True, "unparsed": f"{e.msg} (line {e.lineno})", "changed": [], "added": [], "removed": [],
                    "violations": []}
        if baseline_src is not None:
            b = bnd.check_boundary(baseline_src, cand_src, boundary)
        else:
            b = {"ok": True, "changed": [], "added": [], "removed": [], "violations": []}
        viol = list(b["violations"])
        mods = bnd.imports(cand_src)
        for m in sorted(mods & self.deny_imports):
            line = f"import of {m} is not allowed for this artifact"
            if not any(f"import of {m} " in v for v in viol):
                viol.append(line)
        names = set()
        for node in ast.walk(tree):
            if isinstance(node, ast.Name) and node.id in self.deny_names:
                names.add(node.id)
            elif isinstance(node, ast.Attribute) and node.attr in self.deny_names:
                names.add(node.attr)
        for n in sorted(names):
            viol.append(f"uses {n}, which is not allowed (no introspection, files or dynamic code)")
        return {"ok": not viol, "changed": b["changed"], "added": b["added"], "removed": b["removed"], "violations": viol}

    # ------------------------------------------------------------ baseline
    def _cache_key(self, baseline_src: str, seeds) -> str:
        try:
            scorer_src = self._script.read_text(encoding="utf-8")
        except Exception:  # noqa: BLE001
            scorer_src = ""
        return _sha(baseline_src, scorer_src, self.scorer, ",".join(map(str, seeds)))

    def baseline_profile(self, baseline: Path | None, out: Path, seeds=None, **kw) -> dict:
        """Build check, then quick and full scores for every seed; means, seed SDs and costs. Cached in
        out/baseline_profile.json under a key of the baseline source, the scorer source and the seeds."""
        baseline = Path(baseline) if baseline is not None else self.baseline_path
        seeds = tuple(int(s) for s in (seeds if seeds is not None else self.seeds))
        out = Path(out)
        out.mkdir(parents=True, exist_ok=True)
        src = baseline.read_text(encoding="utf-8")
        key = self._cache_key(src, seeds)
        pj = out / "baseline_profile.json"
        if pj.exists():
            try:
                prof = json.loads(pj.read_text(encoding="utf-8"))
                if prof.get("key") == key and prof.get("ok"):
                    return prof
            except Exception:  # noqa: BLE001
                pass
        prof: dict = {"checker": "script", "key": key, "baseline": str(baseline), "seeds": list(seeds),
                      "check_seed": seeds[0], "lower_is_better": self.sign > 0, "errors": [],
                      "measured": time.strftime("%Y-%m-%dT%H:%M:%S")}
        r = self._score(baseline, out / "base_build", "build", seeds[0])
        prof["build_ok"] = r["metrics"] is not None and not r["violations"]
        if not prof["build_ok"]:
            prof["errors"].append("build: " + json.dumps(self._fail_reason(r, "baseline build"))[:400])
        for level in ("quick", "full"):
            scores, costs = {}, {}
            for s in seeds:
                r = self._score(baseline, out / f"base_{level}_s{s}", level, s)
                if r["metrics"] is None or r["violations"]:
                    prof["errors"].append(f"{level} seed {s}: " + json.dumps(self._fail_reason(r, f"baseline {level}"))[:400])
                    continue
                scores[str(s)] = float(r["metrics"]["score"])
                c = self._cost(r["metrics"])
                if c is not None:
                    costs[str(s)] = c
            vals = list(scores.values())
            prof[level] = {"scores": scores, "mean": statistics.mean(vals) if vals else None, "sd": _sd(vals),
                           "costs": costs, "cost_mean": statistics.mean(costs.values()) if costs else None}
        prof["ok"] = bool(prof["build_ok"] and len(prof["quick"]["scores"]) >= 2 and len(prof["full"]["scores"]) >= 2)
        pj.write_text(json.dumps(prof, indent=1), encoding="utf-8")
        return prof

    def refresh_profile(self, profile_dir: Path, seeds=None, **_ignored) -> dict:
        """The LLM checker's name for baseline_profile; the LLM-only keyword arguments are ignored."""
        return self.baseline_profile(self.baseline_path, profile_dir, seeds)

    # ------------------------------------------------------------ gaps
    def _gap(self, cand: float, baseline: dict, level: str, seed: int) -> dict:
        lv = baseline.get(level) or {}
        base = (lv.get("scores") or {}).get(str(seed))
        if base is None:
            base = lv.get("mean")
        sd = lv.get("sd")
        if base is None:
            return {"cand": cand, "base": None, "gap": None, "sd": sd, "z": None}
        gap = self.sign * (cand - base)
        return {"cand": round(cand, 6), "base": round(base, 6), "gap": round(gap, 6),
                "sd": None if sd is None else round(sd, 6), "z": V.z_of(gap, sd, floor=1e-6)}

    def _cost_ratio(self, m: dict, baseline: dict, level: str, seed: int) -> float:
        c = self._cost(m)
        lv = baseline.get(level) or {}
        b = (lv.get("costs") or {}).get(str(seed)) or lv.get("cost_mean")
        if c is None or not b:
            return 1.0
        return round(c / b, 3)

    def _long_metrics(self, m: dict, baseline: dict, learn_gap: float | None) -> dict:
        g = self._gap(float(m["score"]), baseline, "full", self.check_seed)
        half = learn_gap
        trend = None if (g["gap"] is None or half is None) else round(g["gap"] - half, 6)
        extrap = None if trend is None else round(g["gap"] + trend, 6)
        quick_sd = (baseline.get("quick") or {}).get("sd")
        return {"long_score": g["cand"], "long_base": g["base"], "long_gap": g["gap"], "long_sd": g["sd"],
                "long_z": g["z"], "half_gap": half, "half_z": V.z_of(half, quick_sd, floor=1e-6),
                "trend": trend, "extrap_gap": extrap, "extrap_z": V.z_of(extrap, g["sd"], floor=1e-6),
                "long_cost_ratio": self._cost_ratio(m, baseline, "full", self.check_seed)}

    # ------------------------------------------------------------ the ladder
    def check(self, candidate: Path, out: Path, baseline: dict, *, rung_max: int = 3, boundary: str | None = None,
              baseline_src: str | None = None, lenient: bool = False, audit: bool = True, **_ignored) -> dict:
        candidate, out = Path(candidate), Path(out)
        out.mkdir(parents=True, exist_ok=True)
        rec: dict = {"candidate": str(candidate), "rungs": [], "status": "fail", "rung_reached": 0,
                     "partial_score": 0.0, "feedback": {}, "metrics": {}}
        seed = self.check_seed

        # rung 0: static
        cand_src = candidate.read_text(encoding="utf-8")
        if baseline_src is None and self.baseline_path is not None and self.baseline_path.exists():
            baseline_src = self.baseline_path.read_text(encoding="utf-8")
        st = self.static_check(baseline_src, cand_src, boundary)
        rec["rungs"].append({"rung": 0, "ok": st["ok"], "changed": st["changed"], "added": st["added"],
                             "removed": st["removed"], **({"unparsed": st["unparsed"]} if st.get("unparsed") else {})})
        rec["metrics"]["changed_symbols"] = st["changed"] + st["added"]
        if not st["ok"]:
            rec["feedback"] = {"rung": 0, "reason": "the change reaches outside the part's boundary or uses something not allowed",
                               "violations": st["violations"][:12], "boundary": boundary, "changed": st["changed"][:30]}
            return rec

        # rung 1: build
        r = self._score(candidate, out / "build", "build", seed)
        ok = r["metrics"] is not None and not r["violations"]
        rec["rungs"].append({"rung": 1, "ok": ok, "wall": r["wall"]})
        if not ok:
            rec["feedback"] = {"rung": 1, **self._fail_reason(r, "build")}
            return rec
        rec["rung_reached"], rec["partial_score"] = 1, 1 / 4
        rec["metrics"]["build_score"] = r["metrics"]["score"]
        if rung_max < 2:
            rec["status"] = "checked"
            return rec

        # rung 2: quick score at the matched seed
        r = self._score(candidate, out / "quick", "quick", seed)
        ok = r["metrics"] is not None and not r["violations"]
        detail = {"rung": 2, "ok": ok, "wall": r["wall"]}
        if not ok:
            rec["rungs"].append(detail)
            rec["feedback"] = {"rung": 2, **self._fail_reason(r, "quick scoring")}
            return rec
        m = r["metrics"]
        cr = self._cost_ratio(m, baseline, "quick", seed)
        if cr > self.cost_tol:                     # timing noise: measure once more, keep the cheaper
            r2 = self._score(candidate, out / "quick2", "quick", seed)
            if r2["violations"]:
                rec["rungs"].append(detail)
                rec["feedback"] = {"rung": 2, **self._fail_reason(r2, "quick scoring")}
                return rec
            if r2["metrics"] is not None:
                cr2 = self._cost_ratio(r2["metrics"], baseline, "quick", seed)
                detail["cost_ratio_first"] = cr
                if cr2 < cr:
                    m, cr = r2["metrics"], cr2
        g = self._gap(float(m["score"]), baseline, "quick", seed)
        detail.update({"score": g["cand"], "base": g["base"], "gap": g["gap"], "z": g["z"], "cost_ratio": cr})
        rec["rungs"].append(detail)
        rec["metrics"].update({"learn_score": g["cand"], "learn_base": g["base"], "learn_gap": g["gap"],
                               "learn_sd": g["sd"], "learn_z": g["z"], "cost_ratio": cr, "cost": m.get("cost"),
                               "n_quick": m.get("n")})
        rec["rung_reached"], rec["partial_score"] = 2, 2 / 4
        if cr > self.cost_tol:
            rec["feedback"] = {"rung": 2, "reason": f"cost is {cr:.2f}x the baseline's (at most {self.cost_tol}x is allowed)",
                               "cost": m.get("cost")}
            return rec
        tol = max(self.learn_tol, self.z_tol * (g["sd"] or 0.0))
        if lenient:
            tol *= 3.0
        if g["gap"] is not None and g["gap"] > tol:
            rec["feedback"] = {"rung": 2, "reason": f"the quick score is {g['cand']} against the baseline's {g['base']} "
                               f"on the same instances (gap {g['gap']:+.4f}, negative is better; z {g['z']}; allowed {tol:.4f})"}
            return rec
        if rung_max < 3:
            rec["status"] = "checked"
            return rec

        # rung 3: full score at the matched seed
        r = self._score(candidate, out / "full", "full", seed)
        ok = r["metrics"] is not None and not r["violations"]
        detail = {"rung": 3, "ok": ok, "wall": r["wall"]}
        if not ok:
            rec["rungs"].append(detail)
            rec["feedback"] = {"rung": 3, **self._fail_reason(r, "full scoring")}
            return rec
        lm = self._long_metrics(r["metrics"], baseline, g["gap"])
        detail.update({k: lm[k] for k in ("long_score", "long_base", "long_gap", "long_z")})
        rec["rungs"].append(detail)
        rec["metrics"].update(lm)
        rec["long"] = {"ok": True, "wall": r["wall"], **lm}
        rec["rung_reached"], rec["partial_score"], rec["status"] = 3, 3 / 4, "checked"
        return rec

    def long_run(self, candidate: Path, out: Path, baseline: dict, **_ignored) -> dict:
        """The full-level gap at the matched seed; reuses rung 3's run when it is newer than the candidate."""
        candidate, out = Path(candidate), Path(out)
        mp = out / "full" / "metrics.json"
        if mp.exists() and mp.stat().st_mtime >= candidate.stat().st_mtime:
            m, wall = json.loads(mp.read_text(encoding="utf-8")), 0.0
        else:
            r = self._score(candidate, out / "full", "full", self.check_seed)
            if r["violations"] or r["metrics"] is None:
                return {"ok": False, **self._fail_reason(r, "full scoring"), "wall": r["wall"]}
            m, wall = r["metrics"], r["wall"]
        learn_gap = None
        qp = out / "quick" / "metrics.json"
        if qp.exists():
            try:
                learn_gap = self._gap(float(json.loads(qp.read_text(encoding="utf-8"))["score"]), baseline, "quick",
                                      self.check_seed)["gap"]
            except Exception:  # noqa: BLE001
                learn_gap = None
        return {"ok": True, "wall": wall, **self._long_metrics(m, baseline, learn_gap)}

    def fidelity_probe(self, candidate: Path, out: Path, baseline: dict, target: str, steps: int = 60) -> dict:
        return {"checkable": False, "note": "a script-scored profile has no diagnostics probe"}

    # ------------------------------------------------------------ the full test
    def final(self, candidate: Path, out: Path, baseline: dict, seeds=None, **_ignored) -> dict:
        """Full level over `seeds` for the candidate (and for the baseline where its profile lacks a seed),
        then the sequential verdict; values are raw, and nano/verdict.py orients them by the profile direction."""
        seeds = tuple(int(s) for s in (seeds if seeds is not None else self.seeds))
        out = Path(out)
        full = dict((baseline.get("full") or {}).get("scores") or {})
        cand_vals, base_vals, errors = [], [], []
        for s in seeds:
            r = self._score(Path(candidate), out / f"full_s{s}", "full", s)
            if r["metrics"] is None or r["violations"]:
                errors.append(f"seed {s}: " + json.dumps(self._fail_reason(r, "full scoring"))[:300])
                if r["violations"]:
                    break
                continue
            cand_vals.append(float(r["metrics"]["score"]))
            if str(s) not in full and self.baseline_path is not None:
                rb = self._score(self.baseline_path, out / f"base_full_s{s}", "full", s)
                if rb["metrics"] is not None:
                    full[str(s)] = float(rb["metrics"]["score"])
            base_vals.append(full.get(str(s)))
        pairs = [(c, b) for c, b in zip(cand_vals, base_vals) if b is not None]
        score = dict(getattr(self.profile, "score", None) or {})
        # raw scores: nano/verdict.py orients them itself (told the direction explicitly, never pre-negated here)
        v = V.sequential_verdict([c for c, _ in pairs], [b for _, b in pairs],
                                 margin=score.get("margin", 0.0), alpha=score.get("alpha", 0.01),
                                 min_seeds=score.get("min_seeds", 3), lower_is_better=self.sign > 0)
        if errors and any("integrity" in e for e in errors):
            v["status"] = "fail"
        return {"status": v["status"], "cand_vals": [c for c, _ in pairs], "base_vals": [b for _, b in pairs],
                "verdict": v, "errors": errors}
