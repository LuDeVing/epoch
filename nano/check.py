"""The ladder of cheap checks for candidate trainers. The full training (rung 5) runs separately in
nano/batch_verify.py.

A candidate is a complete python file with the same CLI as nano/train.py. Every candidate process is
started through nano/launch.py: train shards only, no network, no subprocesses, a wall-clock cap,
and an audit record; a violation fails the candidate at the rung where it happened ("integrity").

Rungs, cheapest first:
  0 boundary : free; the candidate changes only what its part may change, imports nothing denied,
               and adds no reference to the validation split (nano/boundary.py)
  1 build    : --build-only runs; non-embedding parameters at most +10% over the baseline (fewer is fine)
  2 steps    : --smoke-steps 4 on real data, the first step discarded as warm-up; step time <= 2x the
               baseline timed the same way today (both re-timed once if the candidate looks slow); VRAM <= cap
  3 learn    : --smoke-steps N (default 45, seed 0): the loss must fall, and the gap to the baseline's
               curve at the same step and seed must not exceed max(LEARN_TOL, Z_TOL x seed spread)
  4 long     : --smoke-steps M (default 240): gap at M and at M/2, the trend between them, and the
               extrapolated gap in units of the seed spread rank the pool (long_run(), called by the loop)
  5 full     : nano/batch_verify.py: external exam, pooled baseline, Welch test and margin

The baseline profile holds the parameter count, the step time measured at the start of every run,
and loss curves from several seeds at both step counts; the spread across seeds at every step is the
noise floor the gaps are measured against (nano/verdict.py).
"""
from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import time
from pathlib import Path

LAB = Path(os.environ.get("HTSA_LAB_ROOT", r"D:\AGI-lab"))
PY = Path(os.environ.get("HTSA_EXEC_PYTHON", str(LAB / ".venv" / "Scripts" / "python.exe")))
HERE = Path(__file__).resolve().parent
BASELINE = HERE / "train.py"
LAUNCH = HERE / "launch.py"
DATA_FULL = LAB / "data" / "fineweb"
DATA_TRAIN = LAB / "data" / "fineweb_train_only"
VRAM_CAP_GB = 5.6
PARAM_TOL = 0.10          # at most this much MORE than the baseline; any reduction is allowed
STEP_TIME_TOL = 2.0
MIN_DROP = 0.05
LEARN_TOL = 0.5           # nats worse than the baseline at matched steps = not learning properly
Z_TOL = 4.0               # or this many seed spreads, whichever is larger
LEARN_STEPS = 45          # about one minute of baseline time
LONG_STEPS = 240          # about five minutes of baseline time
PROFILE_SEED = 0
PROFILE_SEEDS = (0, 1, 2)
SHORT_WINDOW, LONG_WINDOW = 5, 10


def ensure_train_only_dir() -> Path:
    """A folder with hard links to the train shards and nothing else: what a training process may see."""
    DATA_TRAIN.mkdir(parents=True, exist_ok=True)
    for f in sorted(DATA_FULL.glob("train_*.bin")):
        target = DATA_TRAIN / f.name
        if target.exists():
            continue
        try:
            os.link(f, target)
        except OSError:
            shutil.copyfile(f, target)
    return DATA_TRAIN


def _run(script: Path, args: list[str], out: Path, timeout: int, *, wall_cap: float = 0.0,
         audit_name: str = "audit.json") -> dict:
    """Run a candidate through the launcher. Returns rc/stdout/stderr/wall/timed_out/audit."""
    t0 = time.time()
    out.mkdir(parents=True, exist_ok=True)
    audit_path = out / audit_name
    cmd = [str(PY), "-I", str(LAUNCH), "--out", str(out), "--data-dir", str(ensure_train_only_dir()),
           "--data-full", str(DATA_FULL), "--wall-cap", str(wall_cap), "--audit", str(audit_path),
           str(script), *args]
    try:
        p = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace",
                           timeout=timeout, cwd=str(out), env={**os.environ, "PYTHONUNBUFFERED": "1"})
        res = {"rc": p.returncode, "stdout": p.stdout[-4000:], "stderr": p.stderr[-4000:],
               "wall": round(time.time() - t0, 1), "timed_out": p.returncode == 124}
    except subprocess.TimeoutExpired as e:
        res = {"rc": None, "stdout": (e.stdout or "")[-2000:] if isinstance(e.stdout, str) else "",
               "stderr": (e.stderr or "")[-2000:] if isinstance(e.stderr, str) else "",
               "wall": round(time.time() - t0, 1), "timed_out": True}
    audit = {}
    if audit_path.exists():
        try:
            audit = json.loads(audit_path.read_text(encoding="utf-8"))
        except Exception:  # noqa: BLE001
            audit = {}
    res["audit"] = audit
    res["violations"] = [f"{v.get('event')}: {v.get('detail')}" for v in audit.get("violations", [])]
    return res


def _metrics(out: Path) -> dict | None:
    p = out / "metrics.json"
    return json.loads(p.read_text(encoding="utf-8")) if p.exists() else None


def _tail(s: str, n: int = 12) -> str:
    return "\n".join(s.strip().splitlines()[-n:])


def _mean(xs: list[float]) -> float | None:
    xs = [x for x in xs if x == x]
    return sum(xs) / len(xs) if xs else None


def matched_gap(cand_curve: list[float], base_curve: list[float], steps: int, window: int = 5,
                noise: list | None = None) -> dict:
    """Candidate minus baseline mean loss over the last `window` of the first `steps` steps (same seed),
    and the same gap in units of the seed spread at that step when the profile has one."""
    c, b = cand_curve[:steps], base_curve[:steps]
    n = min(len(c), len(b))
    if n < window:
        return {"steps_compared": n, "cand": None, "base": None, "gap": None, "sd": None, "z": None}
    cm, bm = _mean(c[n - window:n]), _mean(b[n - window:n])
    if cm is None or bm is None:                       # a diverged candidate (NaN) has no gap
        return {"steps_compared": n, "cand": cm, "base": bm, "gap": None, "sd": None, "z": None}
    sd = None
    if noise and n - 1 < len(noise) and noise[n - 1] is not None:
        sd = noise[n - 1]
    from nano import verdict as V
    gap = cm - bm
    return {"steps_compared": n, "cand": round(cm, 4), "base": round(bm, 4), "gap": round(gap, 4),
            "sd": None if sd is None else round(sd, 4), "z": V.z_of(gap, sd)}


def _integrity_fail(rec: dict, rung: int, r: dict) -> bool:
    if r.get("violations"):
        rec["feedback"] = {"rung": rung, "reason": "integrity: the run did something a training process may not do",
                           "violations": r["violations"][:8]}
        return True
    return False


TIMING_STEPS = 4          # the first is warm-up (CUDA context, kernel autotune) and is not counted
STEP_METHOD = "warmup_excluded"   # the profile's step_s was measured this way; an older one is re-measured
_FIRST_STEP_RE = re.compile(r"\[nano\] step 1/\d+ .*?([0-9.]+)k tok/s")


def _first_step_s(stdout: str, tokens_per_step: float) -> float | None:
    """Seconds of the first step, from the trainer's own step-1 line (tokens per second since the start)."""
    m = _FIRST_STEP_RE.search(stdout or "")
    if not m or float(m.group(1)) <= 0:
        return None
    return tokens_per_step / (float(m.group(1)) * 1e3)


def _step_time(candidate: Path, out: Path) -> tuple[float | None, dict | None, dict]:
    """Seconds per optimizer step after warm-up: TIMING_STEPS smoke steps, the first one subtracted (read
    from the trainer's step-1 line, or else timed by a separate one-step run). Candidate and baseline go
    through this same function, so both sides are measured the same way."""
    r = _run(candidate, ["--smoke-steps", str(TIMING_STEPS), "--out", str(out)], out, 300, wall_cap=280)
    m = _metrics(out)
    if not (r["rc"] == 0 and m is not None and (m.get("steps") or 0) >= TIMING_STEPS and m.get("wall_s") is not None):
        return None, m, r
    steps, wall = m["steps"], float(m["wall_s"])
    first = _first_step_s(r.get("stdout", ""), float(m.get("tokens") or 0) / max(1, steps))
    if first is None or not 0 < first < wall:
        r1 = _run(candidate, ["--smoke-steps", "1", "--out", str(out / "warmup")], out / "warmup", 300, wall_cap=280)
        if r1.get("violations"):                        # the warm-up run is a candidate run too
            r = {**r, "violations": list(r.get("violations") or []) + list(r1["violations"])}
        m1 = _metrics(out / "warmup")
        first = float(m1["wall_s"]) if r1["rc"] == 0 and m1 and m1.get("wall_s") is not None else None
    if first is not None and 0 < first < wall:
        m["step_timing"] = "warm-up step excluded"
        return (wall - first) / (steps - 1), m, r
    m["step_timing"] = "warm-up step included (could not be separated)"
    return wall / steps, m, r


def check(candidate: Path, out: Path, baseline: dict, *, learn_steps: int = LEARN_STEPS,
          rung_max: int = 3, boundary: str | None = None, baseline_src: str | None = None,
          lenient: bool = False, audit: bool = True) -> dict:
    """Run rungs 0-3 in order; stop at the first failure. Returns the verify record."""
    out.mkdir(parents=True, exist_ok=True)
    rec: dict = {"candidate": str(candidate), "rungs": [], "status": "fail", "rung_reached": 0,
                 "partial_score": 0.0, "feedback": {}, "metrics": {}}

    # rung 0: the boundary, denied imports, validation references (free)
    if baseline_src is not None:
        from nano import boundary as bnd
        b = bnd.check_boundary(baseline_src, candidate.read_text(encoding="utf-8"), boundary)
        detail = {"rung": 0, "ok": b["ok"], "changed": b["changed"], "added": b["added"], "removed": b["removed"]}
        rec["rungs"].append(detail)
        rec["metrics"]["changed_symbols"] = b["changed"] + b["added"]
        if not b["ok"]:
            rec["feedback"] = {"rung": 0, "reason": "the change reaches outside the part's boundary or touches protected code",
                               "violations": b["violations"][:12], "boundary": boundary,
                               "changed": b["changed"][:30]}
            return rec

    # rung 1: build
    r = _run(candidate, ["--build-only", "--out", str(out / "build")], out / "build", 180, wall_cap=150)
    m = _metrics(out / "build")
    ok = r["rc"] == 0 and m is not None
    detail = {"rung": 1, "ok": ok, "wall": r["wall"]}
    if _integrity_fail(rec, 1, r):
        rec["rungs"].append(detail)
        return rec
    if not ok:
        rec["feedback"] = {"rung": 1, "reason": "build failed", "stderr": _tail(r["stderr"]),
                           "stdout": _tail(r["stdout"]), "timed_out": r["timed_out"]}
        rec["rungs"].append(detail)
        return rec
    if m.get("params_nonembed") is None:
        rec["feedback"] = {"rung": 1, "reason": "metrics.json has no params_nonembed (the metrics format must stay)"}
        rec["rungs"].append(detail)
        return rec
    base_p, cand_p = baseline["params_nonembed"], int(m["params_nonembed"])
    rel = (cand_p - base_p) / max(1, base_p)
    detail.update({"params_nonembed": cand_p, "rel_delta": round(rel, 4)})
    rec["metrics"]["params_nonembed"] = cand_p
    rec["metrics"]["param_ratio"] = round(cand_p / max(1, base_p), 4)
    rec["rungs"].append(detail)
    rec["rung_reached"] = 1
    rec["partial_score"] = 1 / 4
    if rel > PARAM_TOL:
        rec["feedback"] = {"rung": 1, "reason": f"parameter count {cand_p:,} is {rel:+.1%} vs baseline "
                           f"{base_p:,}; at most +{PARAM_TOL:.0%} is allowed (fewer is always allowed)"}
        return rec
    if audit:
        # rung 1b, the reach audit: no card time; a dead parameter or a no-op model change fails here
        changed = rec["metrics"].get("changed_symbols") or []
        ra = _run(HERE / "audit.py", ["--candidate", str(candidate), "--baseline", str(BASELINE), "--out", str(out / "reach"),
                                      "--changed", ",".join(changed)], out / "reach", 300, wall_cap=240)
        try:
            aj = json.loads((out / "reach" / "reach.json").read_text(encoding="utf-8"))
        except Exception:  # noqa: BLE001
            aj = {"verdict": "error", "error": _tail(ra.get("stderr", ""))}
        rec["metrics"]["reach"] = {k: aj.get(k) for k in ("verdict", "new_params", "dead_params", "forward_identical", "error") if k in aj}
        if aj.get("verdict") == "dead_path":
            rec["feedback"] = {"rung": 1, "reason": "new parameters receive no gradient, so they are never trained (not used in the "
                               "forward pass, or detached): " + ", ".join(aj.get("dead_params", [])[:5])}
            return rec
        if aj.get("verdict") == "no_effect_suspect":
            rec["feedback"] = {"rung": 1, "reason": aj.get("reason") or "the model code changed but the forward pass at initialisation "
                               "is identical to the original's and no parameter was added: the change does nothing (a path never taken, "
                               "or a value never read)"}
            return rec
    if rung_max < 2:
        rec["status"] = "checked"
        return rec

    # rung 2: a few optimizer steps on real data; speed and memory
    step_s, m, r = _step_time(candidate, out / "steps")
    if _integrity_fail(rec, 2, r):
        rec["rungs"].append({"rung": 2, "ok": False, "wall": r["wall"]})
        return rec
    if step_s is None:
        rec["feedback"] = {"rung": 2, "reason": "smoke steps failed", "stderr": _tail(r["stderr"]),
                           "stdout": _tail(r["stdout"]), "timed_out": r["timed_out"]}
        rec["rungs"].append({"rung": 2, "ok": False, "wall": r["wall"]})
        return rec
    detail = {"rung": 2, "ok": True, "wall": r["wall"], "step_timing": m.get("step_timing")}
    base_step = baseline.get("step_s") if baseline.get("step_s_method") == STEP_METHOD else None
    if not base_step:
        # the profile has no step time measured the same way: time the baseline now, so the 2x rule is real
        base_step, _, _ = _step_time(BASELINE, out / "base_steps")
        detail["base_step_source"] = "timed with this candidate (the profile had no comparable step time)"
    if base_step and step_s > STEP_TIME_TOL * base_step:
        # a slow first measurement is often the card, not the code: measure both sides once more and keep each
        # side's faster time, so candidate and baseline are measured the same number of times
        step_s2, m2, r2 = _step_time(candidate, out / "steps2")
        if _integrity_fail(rec, 2, r2):                 # the re-timing run is a candidate run too
            rec["rungs"].append({"rung": 2, "ok": False, "wall": r2["wall"]})
            return rec
        base_step2, _, _ = _step_time(BASELINE, out / "base_steps2")
        detail.update({"step_s_first": round(step_s, 2), "base_step_first": round(base_step, 2)})
        if step_s2 is not None and step_s2 < step_s:
            step_s, m = step_s2, m2
        if base_step2 is not None and base_step2 < base_step:
            base_step = base_step2
    if not base_step:
        # no baseline time at all: the timing rule cannot be applied; say so instead of comparing with itself
        detail["timing_rule"] = f"not applied: the baseline step time could not be measured ({STEP_TIME_TOL}x rule skipped)"
    detail.update({"step_s": round(step_s, 2), "base_step_s": round(base_step, 3) if base_step else None,
                   "peak_vram_gb": m.get("peak_vram_gb"), "tok_per_s": m.get("tok_per_s")})
    rec["metrics"].update({"step_s": round(step_s, 2), "peak_vram_gb": m.get("peak_vram_gb"),
                           "step_ratio": round(step_s / base_step, 2) if base_step else None})
    base_step = base_step or step_s                     # only for the wall caps below, never for the 2x rule
    rec["rungs"].append(detail)
    rec["rung_reached"] = 2
    rec["partial_score"] = 2 / 4
    if (m.get("peak_vram_gb") or 0) > VRAM_CAP_GB:
        rec["feedback"] = {"rung": 2, "reason": f"peak VRAM {m['peak_vram_gb']} GB exceeds cap {VRAM_CAP_GB} GB"}
        return rec
    if rec["metrics"]["step_ratio"] is not None and step_s > STEP_TIME_TOL * base_step:
        rec["feedback"] = {"rung": 2, "reason": f"step time {step_s:.2f}s is more than {STEP_TIME_TOL}x "
                           f"the baseline {base_step:.2f}s measured today (same token budget means a slower run)"}
        return rec
    if rung_max < 3:
        rec["status"] = "checked"
        return rec

    # rung 3: learn, compared with the baseline at matched steps and the same seed
    cap = learn_steps * STEP_TIME_TOL * base_step + 120
    r = _run(candidate, ["--smoke-steps", str(learn_steps), "--seed", str(PROFILE_SEED), "--out", str(out / "learn")],
             out / "learn", int(cap) + 120, wall_cap=cap)
    m = _metrics(out / "learn")
    ok = r["rc"] == 0 and m is not None and (m.get("steps") or 0) >= learn_steps
    detail = {"rung": 3, "ok": ok, "wall": r["wall"]}
    if _integrity_fail(rec, 3, r):
        rec["rungs"].append(detail)
        return rec
    if not ok:
        rec["feedback"] = {"rung": 3, "reason": "short training run failed or stopped early",
                           "steps": (m or {}).get("steps"), "stderr": _tail(r["stderr"]), "timed_out": r["timed_out"]}
        rec["rungs"].append(detail)
        return rec
    curve = m.get("loss_curve") or []
    first, last = m.get("loss_first"), m.get("loss_last")
    nan = first is None or last is None or not (last == last) or not (first == first)
    drop = 0.0 if nan else (first - last)
    gap = matched_gap(curve, baseline.get("curve_short") or [], learn_steps, SHORT_WINDOW, baseline.get("noise_short"))
    detail.update({"steps": m["steps"], "loss_first": first, "loss_last": last,
                   "drop": round(drop, 4), **{f"matched_{k}": v for k, v in gap.items()}})
    rec["metrics"].update({"smoke_steps": m["steps"], "smoke_loss_first": first,
                           "smoke_loss_last": last, "smoke_drop": round(drop, 4),
                           "learn_loss": gap["cand"], "learn_base": gap["base"], "learn_gap": gap["gap"],
                           "learn_sd": gap["sd"], "learn_z": gap["z"], "tok_per_s": m.get("tok_per_s")})
    rec["rungs"].append(detail)
    rec["rung_reached"] = 3
    if nan or drop < MIN_DROP:
        rec["feedback"] = {"rung": 3, "reason": f"loss did not fall: first {first} -> last "
                           f"{last} over {m['steps']} steps (need a drop >= {MIN_DROP}; NaN counts as no fall)"}
        return rec
    base_curve = (baseline.get("curve_short") or [])[:learn_steps]
    if base_curve and len(curve) >= len(base_curve) and all(abs(c - b) < 1e-6 for c, b in zip(curve, base_curve)):
        # the silent no-op: code changed, training did not (the speedrun log has such a "record")
        rec["metrics"]["no_effect"] = True
        rec["feedback"] = {"rung": 3, "reason": "the change has no effect on training: the loss curve is identical to the "
                           "baseline's at every step (a value the code never reads, or a path that is never taken)"}
        return rec
    tol = max(LEARN_TOL, Z_TOL * (gap["sd"] or 0.0))
    if lenient:
        tol *= 3.0                                  # the long-shot lane: it only has to learn, not to keep up
    if gap["gap"] is not None and gap["gap"] > tol:
        rec["feedback"] = {"rung": 3, "reason": f"at step {gap['steps_compared']} the loss is {gap['cand']} against the "
                           f"baseline's {gap['base']} with the same seed (gap {gap['gap']:+.3f}, z {gap['z']}; allowed {tol:.3f})"}
        return rec
    rec["partial_score"] = 3 / 4
    rec["status"] = "checked"
    return rec


def long_run(candidate: Path, out: Path, baseline: dict, *, long_steps: int = LONG_STEPS) -> dict:
    """Rung 4: a longer matched-step run (same seed). Gap at the end and at the half, the trend between
    them, and the extrapolated gap (end + (end - half), i.e. the linear projection to twice the steps)
    in units of the seed spread. The pool is ranked by the extrapolated z."""
    base_step = baseline.get("step_s") or 1.5
    cap = long_steps * STEP_TIME_TOL * base_step + 240
    r = _run(candidate, ["--smoke-steps", str(long_steps), "--seed", str(PROFILE_SEED), "--out", str(out / "long")],
             out / "long", int(cap) + 120, wall_cap=cap)
    m = _metrics(out / "long")
    ok = r["rc"] == 0 and m is not None and (m.get("steps") or 0) >= long_steps
    if r.get("violations"):
        return {"ok": False, "reason": "integrity", "violations": r["violations"][:8], "wall": r["wall"]}
    if not ok:
        return {"ok": False, "reason": "long run failed or stopped early", "stderr": _tail(r["stderr"]),
                "timed_out": r["timed_out"], "wall": r["wall"]}
    curve, base_curve, noise = m.get("loss_curve") or [], baseline.get("curve_long") or [], baseline.get("noise_long")
    full = matched_gap(curve, base_curve, long_steps, LONG_WINDOW, noise)
    half = matched_gap(curve, base_curve, long_steps // 2, LONG_WINDOW, noise)
    trend = None if (full["gap"] is None or half["gap"] is None) else round(full["gap"] - half["gap"], 4)
    extrap = None if trend is None else round(full["gap"] + trend, 4)
    from nano import verdict as V
    return {"ok": True, "steps": m["steps"], "wall": r["wall"], "long_loss": full["cand"], "long_base": full["base"],
            "long_gap": full["gap"], "long_sd": full["sd"], "long_z": full["z"],
            "half_gap": half["gap"], "half_z": half["z"], "trend": trend,
            "extrap_gap": extrap, "extrap_z": V.z_of(extrap, full["sd"]), "tok_per_s": m.get("tok_per_s")}


def fidelity_probe(candidate: Path, out: Path, baseline: dict, target: str, steps: int = 60) -> dict:
    """Diagnose the candidate (nano/diagnose.py --script) and compare the cell its sketch named with the
    baseline's diagnostics. Returns diagnose.fidelity(...) plus the paths."""
    from nano import diagnose as DG
    base_md = baseline.get("diagnostics_md")
    base_json = Path(base_md).with_suffix(".json") if base_md else None
    if not base_json or not base_json.exists():
        return {"checkable": False, "note": "no baseline diagnostics"}
    folder = out / "diag"
    try:
        r = subprocess.run([str(PY), "-I", str(HERE / "diagnose.py"), "--script", str(candidate), "--out", str(folder),
                            "--steps", str(steps)], capture_output=True, text=True, encoding="utf-8", errors="replace",
                           timeout=1200, env={**os.environ, "HTSA_DATA_DIR": str(ensure_train_only_dir())})
    except subprocess.TimeoutExpired:
        return {"checkable": False, "note": "diagnostics timed out"}
    cj = folder / "diagnostics.json"
    if r.returncode != 0 or not cj.exists():
        return {"checkable": False, "note": f"diagnostics failed: {r.stderr[-200:]}"}
    try:
        cand_d = json.loads(cj.read_text(encoding="utf-8"))
        base_d = json.loads(base_json.read_text(encoding="utf-8"))
        res = DG.fidelity(target, cand_d, base_d)
        res["steps"] = steps
        return res
    except Exception as e:  # noqa: BLE001
        return {"checkable": False, "note": f"fidelity error: {e}"}


def refresh_profile(profile_dir: Path, *, learn_steps: int = LEARN_STEPS, long_steps: int = LONG_STEPS,
                    retime: bool = True, seeds: tuple = PROFILE_SEEDS, diagnostics: bool = True,
                    diag_steps: int = 100, curves: bool = True, diag_seeds: int = 1) -> dict:
    """Load baseline_profile.json; compute what is missing (parameter count, loss curves from several
    seeds at both step counts, the seed spread per step); re-measure the step time today. Curves from an
    older baseline version are discarded. Writes the file back."""
    from nano import verdict as V
    from nano.version import baseline_version
    profile_dir.mkdir(parents=True, exist_ok=True)
    p = profile_dir / "baseline_profile.json"
    prof = json.loads(p.read_text(encoding="utf-8")) if p.exists() else {}
    ver = baseline_version()
    if prof.get("baseline_version") != ver:
        prof = {"baseline_version": ver}
    if not prof.get("params_nonembed"):
        _run(BASELINE, ["--build-only", "--out", str(profile_dir / "base_build")], profile_dir / "base_build", 180, wall_cap=150)
        m = _metrics(profile_dir / "base_build")
        if m:
            prof["params_nonembed"] = int(m["params_nonembed"])
    if retime or not prof.get("step_s") or prof.get("step_s_method") != STEP_METHOD:
        step_s, m, _ = _step_time(BASELINE, profile_dir / "base_steps")
        if step_s is not None:
            prof["step_s"], prof["peak_vram_gb"], prof["tok_per_s"] = step_s, m.get("peak_vram_gb"), m.get("tok_per_s")
            prof["step_s_measured"] = time.strftime("%Y-%m-%dT%H:%M:%S")
            prof["step_s_method"] = STEP_METHOD if m.get("step_timing") == "warm-up step excluded" else "warmup_included"
    for key, steps, window in ((("short", learn_steps, SHORT_WINDOW), ("long", long_steps, LONG_WINDOW)) if curves else ()):
        # curves=False: a run that trains nothing (stops before the ladder) must not pay for them
        curves = prof.setdefault(f"curves_{key}", {})
        for seed in seeds:
            if len(curves.get(str(seed)) or []) >= steps:
                continue
            folder = profile_dir / f"base_{key}_s{seed}"
            cap = steps * 3 * (prof.get("step_s") or 1.5) + 240
            r = _run(BASELINE, ["--smoke-steps", str(steps), "--seed", str(seed), "--out", str(folder)], folder,
                     int(cap) + 120, wall_cap=cap)
            m = _metrics(folder)
            if m and m.get("loss_curve"):
                curves[str(seed)] = m["loss_curve"]
            else:
                prof.setdefault("errors", []).append(f"{key} seed {seed}: {r['stderr'][-300:]}")
        have = [curves[str(s)][:steps] for s in seeds if len(curves.get(str(s)) or []) >= steps]
        if curves.get(str(PROFILE_SEED)):
            prof[f"curve_{key}"] = curves[str(PROFILE_SEED)][:steps]
        prof[f"noise_{key}"] = V.noise_curve(have, window) if len(have) >= 2 else None
        prof[f"noise_{key}_seeds"] = len(have)
    if prof.get("curve_short"):
        prof.update({"smoke_steps": len(prof["curve_short"]), "smoke_loss_first": round(_mean(prof["curve_short"][:5]), 4),
                     "smoke_loss_last": round(_mean(prof["curve_short"][-5:]), 4)})
    if diagnostics:
        # seed 0 in diag/, further seeds in diag_s<k>/ (the anomaly map needs the seed spread); all redone when
        # the step count changes, so seeds are never compared across different horizons
        stale = prof.get("diag_steps") not in (None, diag_steps)
        for s_ in range(max(1, diag_seeds)):                  # a json from an older panel (missing metrics) is stale too
            jp = (profile_dir / ("diag" if s_ == 0 else f"diag_s{s_}")) / "diagnostics.json"
            try:
                layers = json.loads(jp.read_text(encoding="utf-8"))["probes"][-1]["layers"]
                if layers and "max_logit" not in layers[0]:
                    stale = True
            except Exception:  # noqa: BLE001
                pass
        for s in range(max(1, diag_seeds)):
            folder = profile_dir / ("diag" if s == 0 else f"diag_s{s}")
            if (folder / "diagnostics.json").exists() and not stale:
                continue
            try:
                r = subprocess.run([str(PY), "-I", str(HERE / "diagnose.py"), "--out", str(folder),
                                    "--steps", str(diag_steps), "--seed", str(s)], capture_output=True, text=True,
                                   encoding="utf-8", errors="replace", timeout=1800, env={**os.environ})
                if r.returncode != 0:
                    prof.setdefault("errors", []).append(f"diagnostics seed {s}: {r.stderr[-300:]}")
            except subprocess.TimeoutExpired:
                prof.setdefault("errors", []).append(f"diagnostics seed {s}: timed out")
        prof["diag_steps"] = diag_steps
        prof["diagnostics_jsons"] = [str(f / "diagnostics.json") for f in
                                     [profile_dir / "diag"] + [profile_dir / f"diag_s{s}" for s in range(1, max(1, diag_seeds))]
                                     if (f / "diagnostics.json").exists()]
    if (profile_dir / "diag" / "diagnostics.md").exists():
        prof["diagnostics_md"] = str(profile_dir / "diag" / "diagnostics.md")
    p.write_text(json.dumps(prof, indent=1), encoding="utf-8")
    return prof


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("candidate", nargs="?", help="candidate train.py; omit with --profile-baseline")
    ap.add_argument("--out", required=True)
    ap.add_argument("--baseline-profile", default=None, help="baseline_profile.json path")
    ap.add_argument("--profile-baseline", action="store_true", help="(re)build the baseline profile in --out")
    ap.add_argument("--learn-steps", type=int, default=LEARN_STEPS)
    ap.add_argument("--long-steps", type=int, default=LONG_STEPS)
    ap.add_argument("--rung-max", type=int, default=3)
    ap.add_argument("--boundary", default=None)
    ap.add_argument("--long", action="store_true", help="also run the long matched-step comparison")
    a = ap.parse_args()
    out = Path(a.out)
    if a.profile_baseline:
        prof = refresh_profile(out, learn_steps=a.learn_steps, long_steps=a.long_steps)
        print(json.dumps({k: v for k, v in prof.items() if not k.startswith("curve") and not k.startswith("noise_")}, indent=1))
        return 0
    base = json.loads(Path(a.baseline_profile).read_text(encoding="utf-8")) if a.baseline_profile else {}
    if not base.get("params_nonembed"):
        print("need --baseline-profile with params_nonembed (run --profile-baseline first)", file=sys.stderr)
        return 2
    rec = check(Path(a.candidate), out, base, learn_steps=a.learn_steps, rung_max=a.rung_max,
                boundary=a.boundary, baseline_src=BASELINE.read_text(encoding="utf-8"))
    if a.long and rec["status"] == "checked":
        rec["long"] = long_run(Path(a.candidate), out, base, long_steps=a.long_steps)
    (out / "verify.json").write_text(json.dumps(rec, indent=1), encoding="utf-8")
    print(json.dumps({k: rec[k] for k in ("status", "rung_reached", "partial_score", "feedback")}, indent=1))
    return 0 if rec["status"] == "checked" else 1


if __name__ == "__main__":
    raise SystemExit(main())
