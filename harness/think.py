"""The orchestrator (ARCHITECTURE.md section 4; parameters from section 5; launched by the
/think skill of section 3).

Every branch is code; the LLM calls are the leaves run_card, judge, probe and verify. One call
of think() is one run folder runs/<run_id>/ with state.json (header + one decision row per
cycle), clusters.jsonl (this module is its only writer), judgments.jsonl, surprises.jsonl,
answer.json, and one results/<batch>/runs.jsonl row. Ledger rows are appended per card call,
per verification and for encode / probe / judge spend.

Gate configuration: every P1 hook of the section 4 pseudocode is present below as a no-op
guarded by its flag; a requested hook is counted in state.json ("p1_hooks_skipped").

Selection switches (environment, recorded as "select" in state.json and runs.jsonl):
HTSA_SELECT=vote groups the candidates that cleared the bar (_clears) by test answer and takes
the largest group, shortest program on ties (research_notes/thinking_modes/00_SYNTHESIS.md step
4); probe candidates join only after their own verify.run clears the bar (free checks only).
HTSA_SELECT_AUG=1 groups by behaviour on rotated and flipped copies of the ARC test input.

A live run holds run.lock (pid, run_instance) in its folder until answer.json is written; a
second launch of the same run_id refuses to move a folder whose lock names a live process.

Module layout note: harness/think/ holds the control submodules (dedup, allocate, admit, stop,
stagnation, tournament). With harness/think/__init__.py present (current layout) this file is
loaded as harness._think_driver and `from harness.think import think, main` forwards here; if
that __init__.py is ever removed, this file is harness.think itself and sets a __path__ so
harness.think.<sub> still resolves. Top-level imports stay limited to config and schemas.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib
import inspect
import json
import os
import math
import shutil
import statistics
import sys
import time
import traceback
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass, field
from fractions import Fraction
from pathlib import Path
from typing import Any

from . import config
from .schemas import (Answer, Candidate, LedgerRow, Usage, VerifyResult, append_jsonl, new_id,
                      now_ts, read_json, read_jsonl, strip_key, write_json)

if __name__.endswith(".think"):        # loaded as harness.think (no package __init__.py)
    __path__ = [str(Path(__file__).with_name("think"))]

_PKG = __package__ or "harness"
_DEP_NAMES = {
    "encode": "encode", "verify": "verify", "probe": "probe", "judge": "judge",
    "run_card": "run_card", "ledger": "ledger", "graph": "graph", "stats": "stats",
    "dedup": "think.dedup", "allocate": "think.allocate", "admit": "think.admit",
    "stop": "think.stop", "stagnation": "think.stagnation", "tournament": "think.tournament",
    "arc_exec": "arc_exec",
}
_MODS: dict[str, Any] = {}    # resolved dependency modules; tests may preload stand-ins here


def _m(name: str):
    """Resolve a harness dependency lazily (README interfaces)."""
    if name not in _MODS:
        _MODS[name] = importlib.import_module(f"{_PKG}.{_DEP_NAMES[name]}")
    return _MODS[name]


def _log(msg: str) -> None:
    print(f"[think] {msg}", file=sys.stderr, flush=True)


# ---------------------------------------------------------------- run context and state
@dataclass
class Ctx:
    """Run-level constants (section 4 header: B, flags, params, P, V, probe, cls, views)."""
    run_id: str
    run_dir: Path
    log_dir: Path
    item_id: str
    benchmark: str
    arm: str
    backend: str
    batch: str
    replicate: int
    m: int
    B: int
    flags: dict
    params: dict
    split: str
    family: str
    cls: str
    views: dict | None
    snapshot_hash: str | None
    header: dict
    run_instance: str = ""
    P: Any = None
    V: Any = None
    probe: Any = None


@dataclass
class State:
    """Section 4 `state`, plus the per-candidate bookkeeping the loop needs."""
    spent: int = 0
    round: int = 0
    cycles: int = 0
    epoch: int = 0                                   # increments on every reset
    best: Candidate | None = None
    best_checked: Candidate | None = None
    best_partial: float = 0.0                        # best verifier partial score at last cycle end
    best_partial_seen: float = 0.0                   # best verifier partial score so far
    stale: int = 0
    pop: list = field(default_factory=list)
    used_tuples: set = field(default_factory=set)
    conf: dict = field(default_factory=dict)
    agree: dict = field(default_factory=dict)
    p_raw: dict = field(default_factory=dict)
    p_raw_calib: dict = field(default_factory=dict)  # calibration-only judge (never steers)
    calib_spent: int = 0                             # its tokens, outside B and st.spent
    respawned: set = field(default_factory=set)      # tuples spawned in the respawn slot
    vres: dict = field(default_factory=dict)         # cand id -> VerifyResult
    rtype: dict = field(default_factory=dict)        # cand id -> round_type of its spawn
    revise_queue: list = field(default_factory=list) # (Candidate, VerifyResult), failed only
    surprises: list = field(default_factory=list)
    variants: list = field(default_factory=list)
    lemma_pool: list = field(default_factory=list)   # flags.lemmas (P1, I1)
    frontier: Any = None                             # flags.frontier (P1, I4)
    all_cands: list = field(default_factory=list)    # kept generator candidates, all rounds
    parents: dict = field(default_factory=dict)      # cand id -> (Candidate, VerifyResult)
    verify_tokens: int = 0
    verify_attempts: int = 0
    decisions: list = field(default_factory=list)
    hooks_skipped: dict = field(default_factory=dict)
    errors: list = field(default_factory=list)


# ---------------------------------------------------------------- small helpers
def _usage(obj) -> Usage:
    """Usage from a Usage, a dict, or an object carrying .usage / details["usage"]."""
    if obj is None:
        return Usage()
    if isinstance(obj, Usage):
        return obj
    if isinstance(obj, dict):
        if "usage" in obj:
            return _usage(obj["usage"])
        return Usage(int(obj.get("input_tokens", 0) or 0), int(obj.get("output_tokens", 0) or 0),
                     int(obj.get("cache_read_input_tokens", 0) or 0),
                     int(obj.get("cache_creation_input_tokens", 0) or 0))
    if getattr(obj, "usage", None) is not None:
        return _usage(obj.usage)
    for attr in ("details", "data"):
        d = getattr(obj, attr, None)
        if isinstance(d, dict) and "usage" in d:
            return _usage(d["usage"])
    return Usage()


def _parse_value(text: str):
    low = text.strip().lower()
    if low in ("true", "false"):
        return low == "true"
    if low in ("none", "null"):
        return None
    for conv in (int, float):
        try:
            return conv(text)
        except ValueError:
            pass
    return text


def _merge(base: dict, over: dict | None, what: str) -> dict:
    unknown = sorted(set(over or {}) - set(base))
    if unknown:
        raise ValueError(f"unknown {what}: {unknown}")
    return {**base, **(over or {})}


def _p1(st: State, name: str) -> None:
    """A requested P1 hook: not built at P0, so it does nothing but is counted."""
    st.hooks_skipped[name] = st.hooks_skipped.get(name, 0) + 1


def _kwcall(fn, *args, **opt):
    """Call fn with the optional keywords it accepts (stand-ins and older modules may lack them)."""
    try:
        params = inspect.signature(fn).parameters
    except (TypeError, ValueError):
        return fn(*args)
    if any(p.kind is inspect.Parameter.VAR_KEYWORD for p in params.values()):
        return fn(*args, **opt)
    return fn(*args, **{k: v for k, v in opt.items() if k in params})


THRESHOLDS = ("T", "T_checked", "optout", "theta_admit", "hi")
_TOL = 1e-9


def _fraction(v):
    """A threshold as a float; "a/b" strings (CLI --param T=2/3) are exact fractions."""
    if isinstance(v, str) and "/" in v:
        return float(Fraction(v.strip()))
    return float(v)


def _at_least(x: float, thr: float) -> bool:
    """x >= thr with a float tolerance, so 2 of 3 agreement (0.666...) meets T = 2/3."""
    return float(x) >= float(thr) - _TOL


def make_run_id(batch: str, benchmark: str, item_id: str, arm: str, replicate: int) -> str:
    return f"{batch}__{benchmark}__{item_id}__{arm}__r{replicate}"


# ---------------------------------------------------------------- budget (section 4 line 1)
def _row_tokens(row: dict) -> int | None:
    for k in ("total_tokens", "tokens", "usage"):
        v = row.get(k)
        if isinstance(v, (int, float)):
            return int(v)
        if isinstance(v, dict) and isinstance(v.get("total_tokens"), (int, float)):
            return int(v["total_tokens"])
    return None


def cot_median(batch: str, benchmark: str, backend: str) -> tuple[float, str]:
    """Median plain-CoT tokens per item (README cost unit): results/<batch>/budget.json
    cot_median (bench.py), else the median of results/<batch>/cost.jsonl rows, else the
    cold-start proxy PARAMS max_tokens["plain"] x 1.5 (logged as such)."""
    bdir = Path(config.RESULTS_DIR) / batch
    budget = read_json(bdir / "budget.json", default={}) or {}      # bench.py, incl. --budget-from
    cell = (budget.get(benchmark) or {}).get(backend) or {}
    if isinstance(cell, dict) and cell.get("cot_median"):
        return float(cell["cot_median"]), f"budget.json cot_median ({cell.get('n', '?')} items)"
    path = bdir / "cost.jsonl"
    vals = [t for r in read_jsonl(path)
            if r.get("benchmark") == benchmark and r.get("backend", backend) == backend
            and r.get("arm", "plain") == "plain"
            for t in [_row_tokens(r)] if t]
    if vals:
        return float(statistics.median(vals)), f"cost.jsonl median over {len(vals)} items"
    proxy = config.PARAMS["max_tokens"]["plain"] * 1.5
    return proxy, "cold-start proxy: PARAMS.max_tokens.plain x 1.5 (no cost.jsonl rows)"


# ---------------------------------------------------------------- run folder, state.json, ledger
LOCK_NAME = "run.lock"
_LIVE: set[str] = set()                # run ids live in this process (bench runs threads)
_LIVE_LOCK = __import__("threading").Lock()


def _pid_alive(pid: int) -> bool:
    """True if a process with this pid exists. Windows: OpenProcess + exit code (os.kill(pid, 0)
    would send CTRL_C_EVENT there); POSIX: signal 0."""
    if pid <= 0:
        return False
    if os.name == "nt":
        import ctypes
        k32 = ctypes.windll.kernel32
        h = k32.OpenProcess(0x1000, False, int(pid))          # PROCESS_QUERY_LIMITED_INFORMATION
        if not h:
            return ctypes.GetLastError() == 5                 # access denied: it exists
        try:
            code = ctypes.c_ulong()
            ok = k32.GetExitCodeProcess(h, ctypes.byref(code))
            return bool(ok) and code.value == 259             # STILL_ACTIVE
        finally:
            k32.CloseHandle(h)
    try:
        os.kill(pid, 0)
    except ProcessLookupError:
        return False
    except PermissionError:
        return True
    return True


def _lock_live(run_dir: Path, run_id: str) -> bool:
    """Whether run.lock names a live owner: this process with the run id in flight, or another
    live process."""
    lock = read_json(run_dir / LOCK_NAME, default=None)
    if not isinstance(lock, dict):
        return False
    pid = int(lock.get("pid") or 0)
    if pid == os.getpid():
        return run_id in _LIVE
    return _pid_alive(pid)


def _release(run_id: str, run_dir: Path) -> None:
    with _LIVE_LOCK:
        _LIVE.discard(run_id)
    try:
        (run_dir / LOCK_NAME).unlink()
    except OSError:
        pass


def _make_run_dir(run_id: str, run_instance: str = "") -> Path:
    """Fresh run folder. A completed run (answer.json without error.json) is never overwritten
    (CLI --force removes it first); a crashed or interrupted one (state.json but no answer.json,
    or an error.json) is moved aside as <run_id>.old-<ts> so a retry can proceed, unless its
    run.lock names a live process (then RuntimeError: never move a live run). The new folder
    gets run.lock {pid, run_instance, ts}; _finish removes it."""
    run_dir = Path(config.RUNS_DIR) / run_id
    with _LIVE_LOCK:
        if run_id in _LIVE:
            raise RuntimeError(f"run {run_id} is already live in this process")
        if (run_dir / "state.json").exists():
            crashed = (run_dir / "error.json").exists() or not (run_dir / "answer.json").exists()
            if not crashed:
                raise FileExistsError(f"run folder exists: {run_dir} (CLI --force removes it)")
            if _lock_live(run_dir, run_id):
                raise RuntimeError(f"run folder {run_dir} is live ({LOCK_NAME}); not moved")
            aside = run_dir.with_name(f"{run_id}.old-{time.strftime('%Y%m%d-%H%M%S')}")
            n = 0
            while aside.exists():
                n += 1
                aside = run_dir.with_name(f"{run_id}.old-{time.strftime('%Y%m%d-%H%M%S')}-{n}")
            try:
                run_dir.rename(aside)
            except PermissionError as e:       # Windows: a file in it is still open elsewhere
                raise RuntimeError(f"cannot move crashed run folder {run_dir} aside: {e}") from e
            _log(f"moved crashed run folder aside: {aside.name}")
        for sub in ("prompts", "calls", "cands", "private", "variants"):
            (run_dir / sub).mkdir(parents=True, exist_ok=True)
        write_json(run_dir / LOCK_NAME, {"pid": os.getpid(), "run_instance": run_instance,
                                         "ts": now_ts()})
        _LIVE.add(run_id)
    return run_dir


def _save_state(ctx: Ctx, st: State) -> None:
    """state.json: run header + decision log (section 2 workspace layout)."""
    write_json(ctx.run_dir / "state.json", {**ctx.header, "spent": st.spent,
                                            "calibration_tokens": st.calib_spent,
                                            "p1_hooks_skipped": st.hooks_skipped,
                                            "errors": st.errors, "decisions": st.decisions})


def _decide(ctx: Ctx, st: State, step: str, action: str, signal: dict) -> None:
    """One script-written decision row per cycle (section 4: 'log_decision')."""
    st.decisions.append({"step": step, "action": action, "signal": signal, "spent": st.spent,
                         "B": ctx.B, "round": st.round, "epoch": st.epoch,
                         "T": ctx.params["T"], "pop": [c.id for c in st.pop],
                         "conf": dict(st.conf),
                         "verifier_hash": ctx.header.get("verifier_hash"),
                         "snapshot_hash": ctx.snapshot_hash, "ts": now_ts()})
    _save_state(ctx, st)


_ROW_FIELDS = set(LedgerRow.__dataclass_fields__)


def _ledger(ctx: Ctx, *, card: str, round_type: str, round_no: int, call_id: str, tokens: dict,
            operator: str = "none", seed: str = "", perm: int = 0, **extra) -> None:
    """One ledger row. Keys LedgerRow lacks (parent_id of a revise spawn, calibration_only)
    are added to the row dict, which ledger.append accepts."""
    more = {k: extra.pop(k) for k in list(extra) if k not in _ROW_FIELDS}
    row = LedgerRow(
        run_id=ctx.run_id, batch=ctx.batch, benchmark=ctx.benchmark, item_id=ctx.item_id,
        split=ctx.split, family=ctx.family, cls=ctx.cls, arm=ctx.arm, card=card, operator=operator,
        round_type=round_type, round=round_no, seed=seed, perm=perm, call_id=call_id, tokens=tokens,
        snapshot_hash=ctx.snapshot_hash, run_instance=ctx.run_instance or None, **extra)
    _m("ledger").append({**row.to_dict(), **more} if more else row)


def _charge(ctx: Ctx, st: State, usage: Usage, **row) -> None:
    """Spend accounting (section 4): add a returned call's usage and write its ledger row."""
    st.spent += usage.total_tokens
    _ledger(ctx, tokens=usage.to_dict(), **row)


def _call_usage(ctx: Ctx, call_id: str) -> Usage | None:
    """Usage of one logged call from runs/<id>/calls/<call_id>.json (or private/calls/)."""
    for d in (ctx.log_dir, ctx.run_dir / "private" / "calls"):
        rec = read_json(Path(d) / f"{call_id}.json", default=None)
        if isinstance(rec, dict):
            return _usage(rec)
    return None


def _charge_calls(ctx: Ctx, st: State, total: Usage, call_ids: list[str], *, label: str,
                  charge: bool = True, **row) -> None:
    """Charge `total` and write one ledger row per call id with that call's logged usage
    (calls/<id>.json), so the ledger reconciles per call. Any remainder the logs do not
    account for (missing record, estimate mismatch) goes in one extra row named `label`, so
    the per-run sum of ledger tokens always equals the spend. charge=False (calibration-only
    judge calls) writes the rows without adding to st.spent."""
    if charge:
        st.spent += total.total_tokens
    seen = Usage()
    for cid in call_ids:
        u = _call_usage(ctx, cid)
        if u is None:
            continue
        seen = seen.add(u)
        _ledger(ctx, call_id=cid, tokens=u.to_dict(), **row)
    rest = Usage(total.input_tokens - seen.input_tokens, total.output_tokens - seen.output_tokens,
                 total.cache_read_input_tokens - seen.cache_read_input_tokens,
                 total.cache_creation_input_tokens - seen.cache_creation_input_tokens)
    if rest.total_tokens != 0 or not call_ids:
        tokens = rest.to_dict() if rest.total_tokens >= 0 and min(
            rest.input_tokens, rest.output_tokens, rest.cache_read_input_tokens,
            rest.cache_creation_input_tokens) >= 0 else {"total_tokens": total.total_tokens - seen.total_tokens}
        _ledger(ctx, call_id=label, tokens=tokens, **row)


# ---------------------------------------------------------------- setup: encode, verifier, probe
def _setup(ctx: Ctx, st: State, item: dict) -> None:
    """Section 4 before the loop: encode (charged), verify.build, probe (once per problem)."""
    ctx.P = _m("encode").encode(strip_key(item), ctx.run_dir, backend=ctx.backend,
                                replicate=ctx.replicate, log_dir=ctx.log_dir)
    enc_ids = list(((getattr(ctx.P, "meta", None) or {}).get("encode") or {}).get("call_ids") or [])
    _charge_calls(ctx, st, Usage(0, 0, 0, 0).add(_encode_usage(ctx, enc_ids, int(ctx.P.encode_tokens))),
                  enc_ids, label="encode", card="encode", round_type="encode", round_no=-1)
    ctx.V = _m("verify").build(ctx.P, ctx.benchmark)
    vu = _usage(ctx.V)
    if vu.total_tokens:
        _charge(ctx, st, vu, card="verifier_build", round_type="encode", round_no=-1,
                call_id="verifier_build")
    ctx.header["verifier_hash"] = ctx.V.hash
    ctx.header["verification_type"] = ctx.V.type
    ctx.probe = _m("probe").run_probe(ctx.P, n=ctx.params["n_probe"], backend=ctx.backend,
                                      log_dir=ctx.log_dir, replicate=ctx.replicate, run_dir=ctx.run_dir)
    probe_ids = [c.get("call_id") for c in (getattr(ctx.probe, "calls", None) or []) if c.get("call_id")]
    _charge_calls(ctx, st, _usage(ctx.probe), probe_ids, label="probe", card="probe",
                  round_type="probe", round_no=-1)


def _encode_usage(ctx: Ctx, call_ids: list[str], total_tokens: int) -> Usage:
    """Encode reports a token total; rebuild the Usage from the call logs when they add up to
    it, else charge the total as input tokens."""
    seen = Usage()
    for cid in call_ids:
        u = _call_usage(ctx, cid)
        if u is None:
            return Usage(total_tokens, 0, 0, 0)
        seen = seen.add(u)
    return seen if seen.total_tokens == total_tokens else Usage(total_tokens, 0, 0, 0)


# ---------------------------------------------------------------- spawn and collect
def _round_type(spec, st: State) -> str:
    """first | revise | post_reset (ledger round types of section 5 card allocation)."""
    if getattr(spec, "parent_id", None):
        return "revise"
    return "post_reset" if st.epoch > 0 else "first"


def _mean_gen_tokens(ctx: Ctx) -> float | None:
    """Realized mean total tokens per generator call in this run (from calls/<id>.json)."""
    tot, n = 0, 0
    try:
        for p in Path(ctx.log_dir).glob("*.json"):
            rec = json.loads(p.read_text(encoding="utf-8"))
            if rec.get("role") in ("generate", "transform"):
                tot += int(rec.get("total_tokens") or rec.get("usage", {}).get("total_tokens", 0))
                n += 1
    except Exception:  # noqa: BLE001
        return None
    return (tot / n) if n else None


def _within_budget(ctx: Ctx, st: State, specs: list) -> tuple[list, list[int]]:
    """Budget checked before every spawn, counting the estimates of specs already chosen.
    Departs from the section 4 pseudocode on purpose: a spec that does not fit is skipped and
    cheaper specs behind it may still run, where the pseudocode breaks. Pilot-1 evidence: a
    3-call transform ahead of two 1-call cards ended the round with budget left. No research
    note argues for the break, so this docstring records the code's rule."""
    chosen, ests, pending = [], [], 0
    mean_gen = _mean_gen_tokens(ctx)
    for s in specs:
        est = int(_kwcall(_m("allocate").est_cost, s, ctx.views, ctx.benchmark, cls=ctx.cls,
                          round_type=_round_type(s, st)))
        steps = 3 if s.card == "transform" else 1
        if mean_gen:                       # this run's realized mean per generator call
            est = max(est, int(mean_gen * steps))
        else:                              # cold start: the real prompt size, not the 3k constant
            est += max(0, len(ctx.P.problem_md) // 4 - 3000) * steps
        if st.spent + pending + est > ctx.B:
            continue          # skip the spec that does not fit; cheaper specs behind it may still
        chosen.append(s)
        ests.append(est)
        pending += est
    return chosen, ests


def _run_one(ctx: Ctx, st: State, spec):
    parent, fb = st.parents.get(getattr(spec, "parent_id", None) or "", (None, None))
    kw = dict(backend=ctx.backend, round_no=st.round, log_dir=ctx.log_dir, replicate=ctx.replicate,
              parent=parent, feedback=getattr(fb, "feedback_record", None))
    try:
        return _m("run_card").run_card(spec, ctx.P, ctx.run_dir, flags=ctx.flags, **kw)
    except TypeError as e:                 # a run_card without the flags keyword
        if "flags" not in str(e):
            raise
        return _m("run_card").run_card(spec, ctx.P, ctx.run_dir, **kw)


def _spawn(ctx: Ctx, st: State, specs: list) -> list[tuple[Any, Any, str | None]]:
    """Spawn every spec of the round concurrently; returns (spec, CardRun | None, error)."""
    for s in specs:
        st.used_tuples.add((s.card, s.operator, s.seed, s.perm))
    out = []
    with ThreadPoolExecutor(max_workers=max(1, min(6, len(specs)))) as ex:
        futs = [(s, ex.submit(_run_one, ctx, st, s)) for s in specs]
        for s, f in futs:
            try:
                out.append((s, f.result(), None))
            except Exception as e:  # noqa: BLE001 - a failed card must not stop the run
                out.append((s, None, f"{type(e).__name__}: {str(e)[:300]}"))
    return out


def _collect(ctx: Ctx, st: State, runs: list) -> list[Candidate]:
    """collect(): charge every card call, write its ledger row, tag candidates by round type."""
    C: list[Candidate] = []
    for spec, cr, err in runs:
        rt = _round_type(spec, st)
        if cr is None:
            st.errors.append({"round": st.round, "card": spec.card, "error": err})
            continue
        card_err = (getattr(cr, "contract", None) or {}).get("error")
        if card_err:                       # a step failed after earlier calls returned
            st.errors.append({"round": st.round, "card": spec.card, "error": card_err,
                              "partial": True, "n_cands": len(cr.cands)})
        pid = getattr(spec, "parent_id", None)
        _charge_calls(ctx, st, _usage(cr), list(cr.call_ids or []), label=f"{spec.card}:rest",
                      card=spec.card, operator=spec.operator, seed=spec.seed, perm=spec.perm,
                      round_type=rt, round_no=st.round,
                      **({"parent_id": pid} if pid else {}),
                      **({"status": "card_error"} if card_err else {}))
        for c in cr.cands:
            st.rtype[c.id] = rt
            C.append(c)
    return C


def _write_preds(runs: list, C: list[Candidate]) -> None:
    """Rewrite each card's cands/<id>.jsonl with the preds filled by _predict, so the run
    files carry what the loop used (graph.check drop completeness, score coverage)."""
    pred = {c.id: c for c in C}
    for _spec, cr, _err in runs:
        path = (getattr(cr, "contract", None) or {}).get("path") if cr is not None else None
        if not path or not Path(path).exists():
            continue
        rows = read_jsonl(Path(path))
        changed = False
        for r in rows:
            c = pred.get(r.get("id"))
            if c is not None and c.pred is not None and r.get("pred") is None:
                r["pred"], changed = c.pred, True
        if changed:
            Path(path).write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in rows),
                                  encoding="utf-8")


def _predict(ctx: Ctx, C: list[Candidate]) -> None:
    """ARC: fill cand.pred from the program on the key-stripped test input (0 tokens), so dedup
    and probe agreement compare predicted grids (README candidate contract; run_card leaves
    pred None)."""
    todo = [c for c in C if ctx.benchmark == "arc" and c.pred is None and c.program]
    if not todo:
        return
    test_input = ctx.P.item.get("test_input")
    ax = _m("arc_exec")
    with ThreadPoolExecutor(max_workers=max(1, min(6, len(todo)))) as ex:
        preds = list(ex.map(lambda c: _safe_predict(ax, c.program, test_input), todo))
    for c, pred in zip(todo, preds):
        c.pred = pred


def _safe_predict(ax, src: str, test_input):
    try:
        return ax.predict(src, test_input)
    except Exception:  # noqa: BLE001 - an unrunnable program simply has no prediction
        return None


def _p1_collect_hooks(ctx: Ctx, st: State, C: list[Candidate]) -> list[Candidate]:
    """Section 4 hooks right after collect(); all P1, all no-ops at P0."""
    if ctx.flags["harvest_unspoken"] != "off":   # I5: harvest.py thinking.txt -> unspoken cands
        _p1(st, "harvest_unspoken")
    if ctx.flags["lemmas"]:                      # I1: lemma_check.py proves claims by script
        _p1(st, "lemmas.lemma_check")
    if ctx.flags["card_decompose"]:              # I2: compose_parts.py assembles part candidates
        _p1(st, "card_decompose.compose_parts")
    return C


# ---------------------------------------------------------------- dedup, judge, agreement
def _dedup(ctx: Ctx, st: State, C: list[Candidate]) -> tuple[list[Candidate], float]:
    """Rate before drop; cluster rows appended to clusters.jsonl (sole writer, I3)."""
    dd = _m("dedup")
    dup_rate = float(dd.rate(C, st.all_cands, ctx.benchmark))
    if not ctx.flags["dedup"]:
        return C, dup_rate
    try:                          # ARC: a same-grid program that passes the examples is never dropped unverified
        kept, rows = dd.drop(C, st.all_cands, ctx.benchmark, st.round, demo_of=_demo_pass(ctx, st))
    except TypeError:             # a stand-in drop without the demo_of keyword
        kept, rows = dd.drop(C, st.all_cands, ctx.benchmark, st.round)
    if rows:
        append_jsonl(ctx.run_dir / "clusters.jsonl", [{**r, "round": r.get("round", st.round)}
                                                      for r in rows])
    return kept, dup_rate


def _demo_pass(ctx: Ctx, st: State):
    """demo_of for dedup.drop on ARC (0 tokens): True when the program reproduces every train pair.
    Uses a finished demo_match verification when there is one; dedup calls it only on a grid collision."""
    if ctx.benchmark != "arc":
        return None
    cache: dict[str, bool] = {}

    def f(c: Candidate) -> bool:
        r = st.vres.get(c.id)
        if r is not None and getattr(r, "verification_type", None) == "demo_match":
            return r.status == "verified"
        if c.id not in cache:
            src = c.program or (c.text if "def transform" in (c.text or "") else None)
            try:
                d = _m("arc_exec").demo_match(src, ctx.P.item["train"]) if src else {}
            except Exception:  # noqa: BLE001 - an unrunnable program does not pass
                d = {}
            cache[c.id] = bool(d.get("total")) and d.get("matched") == d.get("total")
        return cache[c.id]
    return f


def _est_judge(ctx: Ctx, C: list[Candidate]) -> int:
    fn = getattr(_m("judge"), "est_cost", None)
    if fn is None or not C:
        return 0
    try:
        return int(fn(C, ctx.P, ctx.backend))
    except Exception:  # noqa: BLE001 - a stand-in judge without an estimate
        return 0


def _judge(ctx: Ctx, st: State, C: list[Candidate], sig: dict | None = None) -> None:
    """Blind judge; p_raw logged in judgments.jsonl (the caller writes it), charged. Its cost
    is estimated and checked against B first (section 4 Spend accounting: every call is
    budget-checked); when it does not fit the round is not judged (p_raw steers nothing at
    P0) and the decision row says so."""
    if not C:
        return
    if (getattr(ctx.V, "type", None) in SCRIPT_VTYPES
            and not ctx.flags.get("judge_when_verify_free", False)):
        # p_raw steers nothing at P0 and every candidate gets the free check anyway; in pilot-2
        # the judge cost 114k of 219k tokens re-reading full programs. Kept behind a flag.
        if sig is not None:
            sig["judge_skipped"] = {"reason": "verification is free", "n": len(C)}
        if _calib_sampled(ctx):
            _judge_calibration(ctx, st, C, sig)
        return
    est = _est_judge(ctx, C)
    if st.spent + est > ctx.B:
        if sig is not None:
            sig["judge_skipped"] = {"est": est, "spent": st.spent, "n": len(C)}
        return
    if sig is not None:
        sig["judge_est"] = est
    J, usage = _judge_call(ctx, C)
    ids = list(dict.fromkeys(cid for j in J for cid in j.call_ids))
    _charge_calls(ctx, st, _usage(usage), ids, label="judge", card="judge", round_type="judge",
                  round_no=st.round)
    if J:
        append_jsonl(ctx.run_dir / "judgments.jsonl",
                     [{**j.to_dict(), "round": st.round, "ts": now_ts()} for j in J])
    for j in J:
        st.p_raw[j.id] = j.p_raw


def _judge_call(ctx: Ctx, C: list[Candidate]):
    """judge.judge with run_dir as a keyword when the judge module takes it."""
    return _kwcall(_m("judge").judge, C, ctx.P, backend=ctx.backend, log_dir=ctx.log_dir,
                   replicate=ctx.replicate, run_dir=ctx.run_dir)


def _calib_sampled(ctx: Ctx) -> bool:
    """Whether this item (hashed with the replicate) is in the judge calibration sample."""
    share = float(ctx.flags.get("judge_calibration_sample") or 0.0)
    if share <= 0.0:
        return False
    h = hashlib.sha256(f"{ctx.item_id}:{ctx.replicate}:judge_calibration".encode("utf-8"))
    return int(h.hexdigest()[:8], 16) / 0x100000000 < share


def _judge_calibration(ctx: Ctx, st: State, C: list[Candidate], sig: dict | None) -> None:
    """EVL-08 / Pr17 calibration pairs on script-verified items: judge C, log p_raw to
    judgments.jsonl (calibration_only) and to the verification ledger rows, never into
    st.p_raw, the stop rule or B. Tokens go to st.calib_spent and ledger rows marked
    calibration_only, reported beside the run's spend."""
    J, usage = _judge_call(ctx, C)
    u = _usage(usage)
    st.calib_spent += u.total_tokens
    ids = list(dict.fromkeys(cid for j in J for cid in j.call_ids))
    _charge_calls(ctx, st, u, ids, label="judge", charge=False, card="judge", round_type="judge",
                  round_no=st.round, calibration_only=True)
    if J:
        append_jsonl(ctx.run_dir / "judgments.jsonl",
                     [{**j.to_dict(), "round": st.round, "calibration_only": True, "ts": now_ts()}
                      for j in J])
    for j in J:
        st.p_raw_calib[j.id] = j.p_raw
    if sig is not None:
        sig["judge_calibration"] = {"n": len(J), "tokens": u.total_tokens}


def _score(ctx: Ctx, st: State, C: list[Candidate]) -> None:
    """Agreement with the cached probe and calibrated conf per candidate (p_raw gated)."""
    pr = _m("probe")
    for c in C:
        a = float(pr.agreement(ctx.probe, c, ctx.benchmark))
        p_raw = st.p_raw.get(c.id) if ctx.flags["p_raw_validated"] else None
        st.agree[c.id] = a
        st.conf[c.id] = float(pr.calibrate(a, p_raw, ctx.flags))


# ---------------------------------------------------------------- verify
VTYPE_RANK = {"demo_match": 3, "execution": 3, "llm_falsifier": 2, "llm_consensus": 1,
              "agreement": 1, "none": 0}


def _clears(bar: dict | None, r: VerifyResult, why: list | None = None) -> bool:
    """clears(P.bar, r): the absolute solve bar, checked by script (Pr14). A verified or
    checked status whose verification type ranks at or above bar.required_verification, with
    partial_score at or above the bar's floor, and (when the bar demands all checklist items)
    a details["checklist"] map from verify with every item holding; a missing map fails.
    Reasons go to `why`."""
    bar = bar or {}
    reasons = []
    if r.status not in ("verified", "checked"):
        reasons.append(f"status {r.status}")
    need = bar.get("required_verification")
    if need and VTYPE_RANK.get(r.verification_type, 0) < VTYPE_RANK.get(need, 0):
        reasons.append(f"verification {r.verification_type} below required {need}")
    floor = float(bar.get("min_partial_score", 0.0))
    if r.partial_score < floor:
        reasons.append(f"partial {r.partial_score} < {floor}")
    details = getattr(r, "details", None)
    chk = details.get("checklist") if isinstance(details, dict) else None
    if bar.get("all_items"):
        if not isinstance(chk, dict):
            reasons.append("checklist missing")
        elif not all(bool(v) for v in chk.values()):
            reasons.append("checklist item failed")
    if why is not None:
        why.extend(reasons)
    return not reasons


def _stratum(st: State, cid: str) -> int:
    """best_key stratum: verified > checked > not yet failed > failed."""
    r = st.vres.get(cid)
    status = r.status if r else "unverified"
    return {"verified": 3, "checked": 2, "unverified": 1}.get(status, 0)


def _key(st: State, c: Candidate) -> tuple:
    """best_key: stratum, then the probe agreement, then the partial score. Section 4 says
    "calibrated P from state.conf"; at P0 conf is the identity map on agreement, so the two
    agree. Once p_raw_validated folds p_raw into conf, ordering by conf would let the judge
    choose among verified candidates, which Pr7 forbids, so the key stays on agreement. The
    unverified opt-out in _final compares state.conf with optout (section 4, Pr17)."""
    r = st.vres.get(c.id)
    return (_stratum(st, c.id), st.agree.get(c.id, st.conf.get(c.id, 0.0)),
            r.partial_score if r else 0.0)


def _pick(st: State, cur: Candidate | None, cand: Candidate) -> Candidate:
    """pick(best, cand, key=best_key): stratum first, agreement second, never p_raw."""
    return cand if cur is None or _key(st, cand) > _key(st, cur) else cur


def _verify_queue(ctx: Ctx, st: State, C: list[Candidate]) -> list[Candidate]:
    queue = sorted(C, key=lambda c: -st.conf.get(c.id, 0.0))
    # m_verify caps verification that costs tokens; a free script check verifies every candidate
    if _mean_verify(ctx, st) != 0.0 or not ctx.params.get("verify_all_when_free", True):
        queue = queue[: ctx.params["m_verify"]]
    if ctx.flags["verify_order"] == "top_conf_plus_explore":   # I4: 2 by conf + 1 uniform draw
        _p1(st, "verify_order.top_conf_plus_explore")          #   (P1; top_conf used at P0)
    return queue


def _attempts(ctx: Ctx, c: float) -> int:
    p = ctx.params
    return int(min(p["k_max"], p["k_base"] + math.ceil(p["alpha"] * c)))


SCRIPT_VTYPES = ("demo_match", "execution", "agreement")   # 0-token checks at P0


def _mean_verify(ctx: Ctx, st: State) -> float | None:
    """Run mean tokens per verify attempt; 0.0 for script-only checks, None at cold start."""
    if st.verify_attempts:
        return st.verify_tokens / st.verify_attempts
    return 0.0 if getattr(ctx.V, "type", None) in SCRIPT_VTYPES else None


def _verify_one(ctx: Ctx, st: State, cand: Candidate, k: int) -> VerifyResult:
    r = _m("verify").run(cand, ctx.V, attempts=k, benchmark=ctx.benchmark,
                         agreement=st.agree.get(cand.id), run_dir=ctx.run_dir)
    u = _usage(r)
    st.verify_tokens += u.total_tokens
    st.verify_attempts += max(1, int(r.attempts or 0))
    _charge(ctx, st, u, card=cand.card, operator=cand.operator, seed=cand.seed, perm=cand.perm,
            round_type=st.rtype.get(cand.id, "first"), round_no=st.round,
            call_id=r.call_ids[-1] if r.call_ids else cand.call_id, cand_id=cand.id,
            p_raw=st.p_raw.get(cand.id, st.p_raw_calib.get(cand.id)),
            agreement=st.agree.get(cand.id),
            verification_type=r.verification_type, status=r.status, origin=cand.origin)
    return r


def _verify_round(ctx: Ctx, st: State, C: list[Candidate]) -> tuple[bool, dict]:
    """Verify the top m_verify by conf with k attempts each; surprises and revise queue."""
    progress, sig = False, {"verified": [], "failed": [], "surprises": [], "budget_cut": False}
    allocate = _m("allocate")
    for cand in _verify_queue(ctx, st, C):
        c = st.conf.get(cand.id, 0.0)
        k = _attempts(ctx, c)
        mean = _mean_verify(ctx, st)
        est_v = int(allocate.est_verify(k, mean))
        if est_v > 0 and st.spent + est_v > ctx.B:   # a free check (script-only vtype) never
            sig["budget_cut"] = True                  #   skips: pilot-2 lost 2/3 solves this way
            break
        r = _verify_one(ctx, st, cand, k)
        st.vres[cand.id] = r
        why: list = []
        if _clears(ctx.P.bar, r, why):
            progress = True
            sig["verified"].append(cand.id)
            if r.status == "verified":
                st.best = _pick(st, st.best, cand)
            if r.status == "checked":
                st.best_checked = _pick(st, st.best_checked, cand)
        elif r.status in ("verified", "checked"):
            sig.setdefault("not_cleared", {})[cand.id] = why
        if r.status == "fail":
            _queue_failure(ctx, st, cand, r, c, sig)
        if config.BENCHMARKS[ctx.benchmark]["graded"]:
            st.best_partial_seen = max(st.best_partial_seen, r.partial_score)
    return progress, sig


def _queue_failure(ctx: Ctx, st: State, cand: Candidate, r: VerifyResult, c: float, sig: dict) -> None:
    """Failed candidates join the revise queue; conf > hi and fail is a surprise (goes first)."""
    sig["failed"].append(cand.id)
    st.parents[cand.id] = (cand, r)
    if c > ctx.params["hi"]:
        r.surprise = True
        st.surprises.append(cand.id)
        sig["surprises"].append(cand.id)
        append_jsonl(ctx.run_dir / "surprises.jsonl", {"id": cand.id, "conf": c, "round": st.round,
                                                      "status": r.status, "ts": now_ts()})
        st.revise_queue.insert(0, (cand, r))
    else:
        st.revise_queue.append((cand, r))


# ---------------------------------------------------------------- admit, stop, progress
def _admit(ctx: Ctx, st: State, C: list[Candidate]) -> None:
    verified = {cid for cid, r in st.vres.items() if r.status == "verified"}
    st.pop = list(_m("admit").update(st.pop, C, st.conf, verified, ctx.params["k_pop"],
                                     ctx.params["theta_admit"]))


def _calib(ctx: Ctx):
    return (ctx.views or {}).get("calibration") if isinstance(ctx.views, dict) else None


def _early_stop(ctx: Ctx, st: State) -> str | None:
    """Return 'verified' or 'checked' when that track clears its threshold (flags.early_stop)."""
    if not ctx.flags["early_stop"]:
        return None
    stop = _m("stop")
    if st.best and _at_least(stop.p_correct("verified", st.agree.get(st.best.id, 0.0), _calib(ctx)),
                             ctx.params["T"]):
        return "verified"
    if (ctx.flags["llm_falsifier_validated"] and st.best_checked and
            _at_least(stop.p_correct("checked", st.agree.get(st.best_checked.id, 0.0), _calib(ctx)),
                      ctx.params["T_checked"])):
        return "checked"                                    # weakest stratum (EVL-02)
    return None


def _progress(ctx: Ctx, st: State, progress: bool) -> float:
    """Partial gain on graded benchmarks only; stale counter update (section 4 'Progress')."""
    gain = 0.0
    if config.BENCHMARKS[ctx.benchmark]["graded"]:
        new_best = max(st.best_partial, st.best_partial_seen)
        gain = float(_m("stop").partial_gain(st.best_partial, new_best))
        st.best_partial = new_best
    st.stale = 0 if (progress or gain > ctx.params["eps"]) else st.stale + 1
    return gain


# ---------------------------------------------------------------- next round: reset or reallocate
def _should_reset(ctx: Ctx, st: State, dup_rate: float) -> bool:
    if not ctx.flags["reset_on_stagnation"] or st.round >= ctx.params["R_max"]:
        return False
    p = ctx.params
    return bool(_m("stagnation").should_reset(st.stale, dup_rate, p["R_max"], p["R_stale"], p["d_max"]))


def _reset(ctx: Ctx, st: State) -> list:
    """Stagnation -> reset, never extend: fresh unused tuples, no failed candidates carried."""
    if ctx.flags["restructure"]:          # P1: restructure(P, masked_evidence) -> variants
        _p1(st, "restructure")
    S = list(_kwcall(_m("allocate").fresh_tuples, ctx.benchmark, ctx.cls, st.used_tuples,
                     st.variants, ctx.replicate, st.round, _n0(ctx), item_id=ctx.item_id))
    st.revise_queue = []
    st.frontier = None                    # P1 (I4): a frontier lives within one epoch
    if ctx.flags["lemmas"]:               # P1 (I1): cross_lint keeps predicates only, cosine < 0.8
        _p1(st, "lemmas.cross_lint")
    st.stale = 0
    st.epoch += 1
    return S


def _n0(ctx: Ctx) -> int:
    return int(config.BENCHMARKS[ctx.benchmark]["n0"])


def _max_spawns(ctx: Ctx) -> int:
    return _n0(ctx) + int(ctx.params["max_spawns_extra"])


def _revise(ctx: Ctx, st: State) -> list:
    """Revise children from the tournament over verifier partial scores (<= 2 per round)."""
    if ctx.flags["frontier"] != "tournament":   # I4: frontier.resample (beam_topK | smc), P1;
        _p1(st, f"frontier.{ctx.flags['frontier']}")   # the P0 tournament runs instead
    picked = list(_m("tournament").pick_parents(st.revise_queue, st.conf, ctx.params["hi"], 2,
                                                ctx.replicate))
    ids = {c.id for c, _ in picked}
    st.revise_queue = [(c, r) for c, r in st.revise_queue if c.id not in ids]
    return list(_m("allocate").revise_specs(picked, ctx.replicate)) if picked else []


def _refresh(ctx: Ctx, st: State, specs: list, sig: dict | None = None) -> list:
    """Swap a reallocated spec whose (card, operator, seed, perm) was already spawned for an
    unused tuple of the same card, keeping the card mix (allocate.reallocate is the identity
    at P0). A spec whose card has no unused tuple left is dropped, never re-spawned (Pr8: a
    repeat is the same prompt again), and logged as pool_exhausted in the decision row."""
    out, used = [], set(st.used_tuples)
    for s in specs:
        t = (s.card, s.operator, s.seed, s.perm)
        if t in used:
            try:
                new = _kwcall(_m("allocate").fresh_tuples, ctx.benchmark, ctx.cls, used,
                              st.variants, ctx.replicate, st.round, 1, cards=[s.card],
                              item_id=ctx.item_id)
            except TypeError:              # fresh_tuples without the cards= keyword
                new = []
            if not new:
                if sig is not None:
                    sig.setdefault("pool_exhausted", []).append(s.card)
                continue
            s = new[0]
        used.add((s.card, s.operator, s.seed, s.perm))
        out.append(s)
    return out


def _respawn(ctx: Ctx, st: State, S: list) -> list:
    """The allocated respawn slot (section 5: n0 + 3 = 2 revise + 1 respawn): one unused tuple
    whose card memory picks (allocate.respawn: Thompson with the pooled back-off and the floor,
    round-robin at cold start). Skipped when the round is full or the allocator has none."""
    fn = getattr(_m("allocate"), "respawn", None)
    if fn is None or len(S) >= _max_spawns(ctx):
        return []
    used = set(st.used_tuples) | {(s.card, s.operator, s.seed, s.perm) for s in S}
    rt = "post_reset" if st.epoch > 0 else "first"
    new = list(_kwcall(fn, ctx.benchmark, ctx.cls, ctx.views, used, st.variants, ctx.replicate,
                       st.round, 1, item_id=ctx.item_id, round_type=rt))
    st.respawned.update((s.card, s.operator, s.seed, s.perm) for s in new)
    return new


def _next_specs(ctx: Ctx, st: State, S: list, sig: dict | None = None) -> list:
    """Reallocate, add revise, the respawn slot and P1 specs, cap at max_spawns_per_round
    (section 4 loop tail). Revise and respawn specs are one-shot: they never carry into the
    next round's base list."""
    base = [s for s in S if not getattr(s, "parent_id", None)
            and (s.card, s.operator, s.seed, s.perm) not in st.respawned]
    mult = 1.0   # P1 (CTL-08): within-run LP multiplier on graded benchmarks; 1.0 at P0
    S = _refresh(ctx, st, list(_m("allocate").reallocate(base, mult)), sig)
    if config.BENCHMARKS[ctx.benchmark]["revise_allowed"] and st.revise_queue:
        S = S + _revise(ctx, st)
    S = S + _respawn(ctx, st, S)
    if ctx.flags["lemmas"]:               # P1 (I1): lemma_claims_spec from round 2, build_spec
        _p1(st, "lemmas.claims_and_build_specs")   #   (<= 1 build call per round)
    if ctx.flags["card_decompose"]:       # P1 (I2): decompose_spec, from round 2, never BT
        _p1(st, "card_decompose.decompose_spec")
    if ctx.flags["gap_pack"] != "off":    # P1 (I6): gap_pack_specs(select_packs(gaps, ...))
        _p1(st, "gap_pack.specs")
    return S[: _max_spawns(ctx)]


def _p_success(ctx: Ctx, spec, st: State) -> float:
    """p_s for the value stop: mean of Beta(pass+1, fail+1) for the spec's cell in the frozen
    strategy_stats view (allocate.stats_rows format), else the Beta(1,1) prior mean 0.5."""
    rows_fn = getattr(_m("allocate"), "stats_rows", None)
    rows = rows_fn(ctx.views) if rows_fn and ctx.views else []
    rt = _round_type(spec, st)
    for r in rows:
        if r.get("cls") == ctx.cls and r.get("card") == spec.card and r.get("round_type", rt) == rt:
            return (int(r.get("pass", 0)) + 1) / (int(r.get("pass", 0)) + int(r.get("fail", 0)) + 2)
    return 0.5


def _value_stop(ctx: Ctx, st: State, S: list) -> bool:
    """Stop when no spec is worth its cost: all(p_s * V_tokens < est_cost(s)), V_tokens = B."""
    est = _m("allocate").est_cost
    return all(_p_success(ctx, s, st) * ctx.B
               < _kwcall(est, s, ctx.views, ctx.benchmark, cls=ctx.cls, round_type=_round_type(s, st))
               for s in S)


# ---------------------------------------------------------------- the round loop
def _cycle(ctx: Ctx, st: State, S: list) -> tuple[str, list]:
    """One cycle of section 4. Returns (action, next specs); action names the decision."""
    spawn, ests = _within_budget(ctx, st, S[: _max_spawns(ctx)])
    if not spawn:
        return "budget_stop", []
    runs = _spawn(ctx, st, spawn)
    C = _p1_collect_hooks(ctx, st, _collect(ctx, st, runs))
    _predict(ctx, C)
    _write_preds(runs, C)
    n_raw = len(C)
    C, dup_rate = _dedup(ctx, st, C)
    st.all_cands.extend(C)
    jsig: dict = {}
    _judge(ctx, st, C, jsig)
    _score(ctx, st, C)
    progress, vsig = _verify_round(ctx, st, C)
    _admit(ctx, st, C)
    if ctx.flags["gap_pack"] != "off":    # P1 (I6): gaps.write(run, coverage(C)), script-built
        _p1(st, "gap_pack.gaps_write")
    sig = {"spawned": [f"{s.card}:{s.operator}:{s.seed}:{s.perm}" for s in spawn], "est": ests,
           "n_raw": n_raw, "n_kept": len(C), "dup_rate": dup_rate, **vsig, **jsig,
           "agreement": {c.id: st.agree.get(c.id) for c in C}}
    st.cycles += 1
    stop_kind = _early_stop(ctx, st)
    if stop_kind:
        return _log_cycle(ctx, st, f"stop_{stop_kind}", sig), []
    sig["gain"] = _progress(ctx, st, progress)
    sig["stale"] = st.stale
    st.round += 1
    if _should_reset(ctx, st, dup_rate):
        S = _reset(ctx, st)
        return _log_cycle(ctx, st, "reset", sig), S
    S = _next_specs(ctx, st, S, sig)
    action = "value_stop" if _value_stop(ctx, st, S) else "continue"
    return _log_cycle(ctx, st, action, sig), S


def _graph_write(ctx: Ctx, st: State) -> None:
    """graph.write (flags.graph, I3, 0 tokens); a diagnostic never stops a run."""
    if ctx.flags["graph"]:
        try:
            _m("graph").write(ctx.run_dir)
        except Exception as e:  # noqa: BLE001
            st.errors.append({"round": st.round, "graph_write": f"{type(e).__name__}: {e}"})


def _log_cycle(ctx: Ctx, st: State, action: str, sig: dict) -> str:
    """Decision row, then graph.write after every cycle."""
    _decide(ctx, st, f"cycle{st.cycles - 1}", action, sig)
    _graph_write(ctx, st)
    return action


def _loop(ctx: Ctx, st: State, S: list) -> str:
    action = "round_cap"
    while st.round < ctx.params["R_max"]:
        action, S = _cycle(ctx, st, S)
        if action in ("budget_stop", "value_stop") or action.startswith("stop_"):
            return action
    return "round_cap" if action in ("continue", "reset") else action


# ---------------------------------------------------------------- answer
def _impasse(ctx: Ctx, st: State, cause: str) -> str:
    """impasse_report_from_fields(state): script-written, no candidate text."""
    k = sum(1 for r in st.vres.values() if r.status == "verified")
    return (f"impasse ({cause}): rounds={st.cycles}, stale={st.stale}, spent={st.spent}/{ctx.B}, "
            f"candidates={len(st.all_cands)}, verified={k}"
            + (" (none cleared the bar)" if k else "") + f", pop={len(st.pop)}")


def _mk(ctx: Ctx, st: State, cand: Candidate | None, status: str, reason: str,
        best_guess=None) -> Answer:
    r = st.vres.get(cand.id) if cand else None
    return Answer(status=status, answer=cand.pred if cand and status != "abstain" else None,
                  verification_type=(r.verification_type if r else ctx.header.get("verification_type")),
                  cand_id=cand.id if cand else None, spent_tokens=st.spent, rounds=st.cycles,
                  best_guess=best_guess, reason=reason)


def _vote_verified(ctx: Ctx, st: State):
    """Among the candidates whose verify.run is "verified" and clears the bar (_clears, Pr14), group by test
    answer, take the largest group, break ties by agreement on augmented test inputs, then by the shortest
    program (dedup.vote, the rule portfolio_arc uses too): self-consistency over independent attempts (Wang et
    al. 2022), behaviour clustering (AlphaCode, Li et al. 2022), Occam. ARC probe programs join only after the
    same verify.run (charged, with its ledger row) clears the bar, and only while that check is free."""
    bar = getattr(ctx.P, "bar", None) or {}
    pool = [c for c in st.all_cands
            if st.vres.get(c.id) is not None and getattr(st.vres[c.id], "status", None) == "verified"
            and _clears(bar, st.vres[c.id])]
    if (ctx.benchmark == "arc" and getattr(ctx, "probe", None) is not None
            and _mean_verify(ctx, st) == 0.0):
        for c in getattr(ctx.probe, "cands", []) or []:
            if not c.program or c.pred is None:
                continue
            r = st.vres.get(c.id)
            if r is None:
                st.rtype[c.id] = "probe"
                r = _verify_one(ctx, st, c, 1)
                st.vres[c.id] = r
            if r.status == "verified" and _clears(bar, r):
                pool.append(c)
    pool = [c for c in pool if c.pred is not None]
    if not pool:
        return None, 0, 0
    aug_of = None
    ex = _m("arc_exec") if ctx.benchmark == "arc" else None
    test_input = (getattr(ctx.P, "item", None) or {}).get("test_input") if ctx.benchmark == "arc" else None
    if ex is not None and test_input is not None and hasattr(ex, "augmented") and hasattr(ex, "aug_key"):
        # same rule as the portfolio: test answer first, augmented outputs only break ties
        variants = ex.augmented(test_input)

        def aug_of(c):
            try:
                return ex.aug_key(ex.run_program(c.program, variants)) if c.program else None
            except Exception:  # noqa: BLE001
                return None
    return _m("dedup").vote(pool, lambda c: c.pred, lambda c: len(c.program or ""), aug_of)


def _final(ctx: Ctx, st: State, cause: str) -> Answer:
    """Section 4 end: verified > checked > unverified best guess if conf >= optout > abstain."""
    if (ctx.header.get("select") or {}).get("HTSA_SELECT") == "vote":
        c, k, n = _vote_verified(ctx, st)
        if c is not None:
            return _mk(ctx, st, c, "solved", f"verified, vote {k} of {n} distinct answers ({cause})")
    if st.best:
        return _mk(ctx, st, st.best, "solved", f"verified ({cause})")
    if st.best_checked:                    # labelled checked, never verified
        return _mk(ctx, st, st.best_checked, "checked", f"checked, not verified ({cause})")
    b = None
    for c in st.pop:
        b = _pick(st, b, c)
    if b and _stratum(st, b.id) == 2:
        return _mk(ctx, st, b, "checked", f"checked best of population ({cause})")
    if b and _stratum(st, b.id) == 1 and _at_least(st.conf.get(b.id, 0.0), ctx.params["optout"]):
        return _mk(ctx, st, b, "unverified", f"unverified best guess, conf {st.conf[b.id]:.2f} ({cause})")
    if b is None:
        for c in st.all_cands:
            b = _pick(st, b, c)
    return _mk(ctx, st, b, "abstain", _impasse(ctx, st, cause), best_guess=b.pred if b else None)


def _finish(ctx: Ctx, st: State, ans: Answer, cause: str, error: str | None = None) -> Answer:
    write_json(ctx.run_dir / "answer.json", ans.to_dict())
    _graph_write(ctx, st)              # final graph; also covers a run that stopped before any cycle
    _decide(ctx, st, "final", ans.status, {"cause": cause, "cand_id": ans.cand_id,
                                           "overshoot": max(0, st.spent - ctx.B), "error": error})
    append_jsonl(Path(config.RESULTS_DIR) / ctx.batch / "runs.jsonl", {
        "batch": ctx.batch, "benchmark": ctx.benchmark, "item_id": ctx.item_id, "arm": ctx.arm,
        "replicate": ctx.replicate, "run_id": ctx.run_id, "status": "error" if error else ans.status,
        "answer": ans.answer, "spent_tokens": st.spent, "rounds": st.cycles, "ts": now_ts(),
        "budget_tokens": ctx.B, "overshoot": max(0, st.spent - ctx.B),
        "run_instance": ctx.run_instance or None, "error": error,
        "select": ctx.header.get("select"), "calibration_tokens": st.calib_spent})
    return ans


# ---------------------------------------------------------------- entry point
def _snapshot(batch: str | None, split: str) -> tuple[dict | None, str | None]:
    """Frozen views of flags.snapshot, built from that batch's train-split ledger rows on first
    use (stats.ensure_views; plain load_views for a module without it). Pr11 / MSR-11: memory
    is credited only on held-out items, so a view whose splits include the item's own split
    (or that records no splits, or an item with no split) is refused (ValueError) before any
    run folder exists."""
    if not batch:
        return None, None
    st_mod = _m("stats")
    loader = getattr(st_mod, "ensure_views", None) or st_mod.load_views
    views = loader(batch)
    if views is None:
        return None, None
    splits = ((views.get("strategy_stats") or {}).get("splits")) if isinstance(views, dict) else None
    if not split or not splits or split in splits:
        raise ValueError(f"snapshot {batch!r} was built from splits {splits}; item split "
                         f"{split or '(none)'!r} is not disjoint from them (Pr11)")
    blob = json.dumps(views, sort_keys=True, default=str).encode("utf-8")
    return views, hashlib.sha256(blob).hexdigest()[:16]


def _context(item: dict, m: int, replicate: int, backend: str, batch: str, flags: dict,
             params: dict, arm: str) -> Ctx:
    benchmark = item["benchmark"]
    if os.environ.get("HTSA_FIXED_B"):                 # a fixed budget, plain measured elsewhere
        B = int(os.environ["HTSA_FIXED_B"])
        cot, source = None, "fixed"
        _log(f"B = {B} tokens (fixed)")
    else:
        cot, source = cot_median(batch, benchmark, backend)
        B = max(int(round(m * cot)), int(os.environ.get("HTSA_MIN_B", "0") or 0))   # floor: setup cannot eat it
        _log(f"B = max({m} x {cot:.0f}, floor) = {B} tokens ({source})")
    run_id = make_run_id(batch, benchmark, item["id"], arm, replicate)
    views, snap_hash = _snapshot(flags["snapshot"], item.get("split", ""))
    inst = new_id("i")
    run_dir = _make_run_dir(run_id, inst)
    family = item.get("family", benchmark)
    cls = family                       # P1 (REP-01): signature_class(P) when flags.signature
    header = {"run_id": run_id, "run_instance": inst, "item_id": item["id"], "benchmark": benchmark,
              "arm": arm, "backend": backend, "model": config.DEFAULT_MODEL, "m": m, "B": B,
              "B_source": source, "cot_median": cot, "flags": flags, "params": params,
              "replicate": replicate, "batch": batch, "split": item.get("split", ""),
              "family": family, "cls": cls, "snapshot_hash": snap_hash,
              "snapshot_splits": ((views or {}).get("strategy_stats") or {}).get("splits"),
              "select": {"HTSA_SELECT": os.environ.get("HTSA_SELECT") or None,
                         "HTSA_SELECT_AUG": os.environ.get("HTSA_SELECT_AUG") or None},
              "ts_start": now_ts()}
    return Ctx(run_id=run_id, run_dir=run_dir, log_dir=run_dir / "calls", item_id=item["id"],
               benchmark=benchmark, arm=arm, backend=backend, batch=batch, replicate=replicate,
               m=m, B=B, flags=flags, params=params, split=item.get("split", ""), family=family,
               cls=cls, views=views, snapshot_hash=snap_hash, header=header, run_instance=inst)


def think(item: dict, *, m: int, replicate: int, backend: str, batch: str, flags: dict | None = None,
          params: dict | None = None, arm: str = "scaffold") -> Answer:
    """Section 4 think(problem, m, flags): encode -> verifier -> probe -> rounds -> answer.json."""
    flags = _merge(config.FLAGS, flags, "flags")
    params = _merge(config.PARAMS, params, "params")
    params.update({k: _fraction(params[k]) for k in THRESHOLDS if k in params})
    ctx = _context(item, m, replicate, backend, batch, flags, params, arm)
    try:
        return _run(ctx, item, replicate)
    finally:
        _release(ctx.run_id, ctx.run_dir)          # answer.json is written; the run is no longer live


def _run(ctx: Ctx, item: dict, replicate: int) -> Answer:
    st = State()
    if ctx.flags["signature"]:
        _p1(st, "signature")
    _save_state(ctx, st)
    try:
        _setup(ctx, st, item)
        S = list(_kwcall(_m("allocate").initial, ctx.benchmark, ctx.cls, ctx.views, _n0(ctx),
                         replicate, 0, item_id=ctx.item_id))
        cause = _loop(ctx, st, S)
    except Exception as e:  # noqa: BLE001 - a crashed run still leaves answer.json and its rows
        err = f"{type(e).__name__}: {str(e)[:500]}"
        _log(f"crash: {err}")
        st.errors.append({"round": st.round, "crash": err})
        write_json(ctx.run_dir / "error.json", {"error": err, "traceback": traceback.format_exc(),
                                                 "spent": st.spent, "ts": now_ts()})
        ans = Answer(status="abstain", answer=None,
                     verification_type=ctx.header.get("verification_type"), cand_id=None,
                     spent_tokens=st.spent, rounds=st.cycles, best_guess=None, reason=f"crash: {err}")
        return _finish(ctx, st, ans, "crash", error=err)
    return _finish(ctx, st, _final(ctx, st, cause), cause)


def _kv(pairs: list[str] | None) -> dict:
    out = {}
    for p in pairs or []:
        if "=" not in p:
            raise SystemExit(f"expected name=value, got {p!r}")
        k, v = p.split("=", 1)
        out[k.strip()] = _parse_value(v)
    return out


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(prog="python -m harness.think", description=__doc__.splitlines()[0])
    ap.add_argument("--benchmark", required=True, choices=sorted(config.BENCHMARKS))
    ap.add_argument("--item", required=True)
    ap.add_argument("--m", type=int, default=config.PARAMS["m"])
    ap.add_argument("--replicate", type=int, default=0)
    ap.add_argument("--backend", default=config.default_backend(),
                    choices=["mock", "cli_json", "messages_api"])
    ap.add_argument("--batch", default="dev")
    ap.add_argument("--arm", default="scaffold")
    ap.add_argument("--flag", action="append", metavar="name=value")
    ap.add_argument("--param", action="append", metavar="name=value")
    ap.add_argument("--force", action="store_true", help="remove an existing run folder first")
    a = ap.parse_args(argv)
    item = importlib.import_module(f"{_PKG}.data").get_item(a.benchmark, a.item)
    run_dir = Path(config.RUNS_DIR) / make_run_id(a.batch, a.benchmark, item["id"], a.arm, a.replicate)
    if a.force and run_dir.exists():
        shutil.rmtree(run_dir)
    ans = think(item, m=a.m, replicate=a.replicate, backend=a.backend, batch=a.batch,
                flags=_kv(a.flag), params=_kv(a.param), arm=a.arm)
    print(json.dumps({"run_dir": str(run_dir), **ans.to_dict()}, default=str))
    return 0


if __name__ == "__main__":
    sys.exit(main())
