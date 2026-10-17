"""Pruning regret: correct-but-pruned rate by cause and late-winner rate.

Implements ARCHITECTURE.md section 8 (Pruning regret paragraph and metric bullet), the
section 5 close rule and section 11 v0.3 entry I4 (diagnostic only, P0, 0 tokens). Offline,
keyed items only, never fed back into any run. Keys are reached only through
harness.score.cand_correct; this module never reads an item's key field itself.

Per run (default arm "scaffold"):
  pool      = every cands row of the run folder, probe candidates included (n_probe counts
              them). One definition across the harness: score.py coverage uses the same pool,
              and the driver's vote can return a probe program, so a probe candidate is a
              candidate that could have been returned.
  covered   = some pool candidate is key-correct
  returned  = the answer's candidate (answer.json cand_id, else the answer value) is key-correct
  pruned    = covered and not returned
Causes of a pruned run (flags may overlap; `primary` assigns the first that holds, in
pipeline order a -> b -> c, so primary rates sum to the pruned rate):
  (a) never_verified : no key-correct candidate has a verify.jsonl row
  (b) evicted        : a key-correct candidate was in state.pop at one cycle and absent at a
                       later one (needs pop ids per cycle in state.json; None when absent)
  (c) never_revised  : no key-correct candidate is a parent of any candidate (None on
                       benchmarks where revise is not allowed)
Late winner (runs whose answer is verified status "solved" and key-correct): the final
candidate's lineage roots do not include any lineage top-ranked by conf among the
first-round candidates. conf comes from state.json cycle rows ("conf": {cand_id: c}),
falling back to the ledger agreement of the run's rows (identity calibration at P0).

Rates are per item (replicates averaged within item), then averaged over items, with a
95% item-cluster bootstrap CI (ARCHITECTURE section 8): clusters are item groups (BRAINTEASER
puzzle groups; an ARC task is its own cluster), resampled with replacement, the rate of a
resample being the mean over the items it contains. Output: results/<batch>/pruning_regret.json.
CLI: python -m harness.measure.pruning_regret --batch <name> [--arm scaffold]
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Callable

import numpy as np

from .. import config, graph, ledger
from ..schemas import read_json, read_jsonl, write_json

SOLVED = ("solved", "verified")


# ---------------------------------------------------------------- run folder readers
def state_cycles(run_dir: Path) -> list[dict]:
    """Decision-log rows of state.json (list, {cycles|log|rows|decisions: [...]}, a single
    row, or JSON lines)."""
    p = Path(run_dir) / "state.json"
    if not p.exists():
        return []
    try:
        st = json.loads(p.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return [r for r in read_jsonl(p) if isinstance(r, dict)]
    if isinstance(st, list):
        return [r for r in st if isinstance(r, dict)]
    if isinstance(st, dict):
        for k in ("cycles", "log", "rows", "decisions"):
            if isinstance(st.get(k), list):
                return [r for r in st[k] if isinstance(r, dict)]
        return [st] if "pop" in st else []
    return []


def _ids(seq) -> set[str]:
    out = set()
    for x in seq or []:
        if isinstance(x, dict):
            x = x.get("id") or x.get("cand_id")
        if x:
            out.add(str(x))
    return out


def pop_history(cycles: list[dict]) -> list[set[str]] | None:
    """Population ids per cycle, or None when no cycle row carries a pop field."""
    hist = [_ids(r["pop"]) for r in cycles if "pop" in r]
    return hist or None


def conf_map(cycles: list[dict], run_id: str, batch: str) -> dict[str, float]:
    """conf per candidate: state.json cycle rows, else ledger agreement (identity map)."""
    conf: dict[str, float] = {}
    for r in cycles:
        if isinstance(r.get("conf"), dict):
            conf.update({k: float(v) for k, v in r["conf"].items() if v is not None})
    if conf:
        return conf
    for r in ledger.rows(batch=batch, run_id=run_id):
        if r.get("cand_id") and r.get("agreement") is not None:
            conf[r["cand_id"]] = float(r["agreement"])
    return conf


def _answer(row: dict, run_dir: Path) -> dict:
    a = read_json(Path(run_dir) / "answer.json", default=None)
    if isinstance(a, dict):
        return a
    return {"status": row.get("status"), "answer": row.get("answer"), "cand_id": None}


# ---------------------------------------------------------------- per-run analysis
def _is_probe(c: dict) -> bool:
    return c.get("card") == "probe" or c.get("origin") == "probe"


def _returned_correct(ans: dict, by_id: dict, correct: set, item: dict, correct_fn) -> bool:
    if ans.get("status") == "abstain":
        return False
    cid = ans.get("cand_id")
    if cid and cid in by_id:
        return cid in correct
    if ans.get("answer") is None:
        return False
    return bool(correct_fn(item, {"pred": ans.get("answer")}))


def _evicted(correct: set, hist: list[set[str]] | None) -> bool | None:
    """(b): a correct id present at cycle i and missing at some cycle j > i."""
    if hist is None:
        return None
    for i, pop in enumerate(hist):
        for cid in correct & pop:
            if any(cid not in later for later in hist[i + 1:]):
                return True
    return False


def causes(correct: set, cands: list[dict], verified_ids: set, hist, revise_ok: bool) -> dict:
    """Cause flags (a), (b), (c) and the primary cause in pipeline order."""
    parents = {p for c in cands for p in (c.get("parent_ids") or [])}
    flags = {"never_verified": not (correct & verified_ids),
             "evicted": _evicted(correct, hist),
             "never_revised": (not (correct & parents)) if revise_ok else None}
    primary = "other"
    for k, name in (("never_verified", "a"), ("evicted", "b"), ("never_revised", "c")):
        if flags[k]:
            primary = name
            break
    flags["primary"] = primary
    return flags


def late_winner(final_id: str | None, pool: list[dict], conf: dict) -> bool | None:
    """True when the final candidate's lineage was not top-ranked by conf after round 1."""
    by_id = {c["id"]: c for c in pool}
    if not final_id or final_id not in by_id or not pool:
        return None
    first = min(int(c.get("round") or 0) for c in pool)
    scored = [c for c in pool if int(c.get("round") or 0) == first and c["id"] in conf]
    if not scored:
        return None
    top = max(conf[c["id"]] for c in scored)
    top_lineages = {c.get("lineage_id") or c["id"] for c in scored if conf[c["id"]] == top}
    final_roots = set(graph.root_ids(by_id)[final_id]) | {by_id[final_id].get("lineage_id")}
    return not (final_roots & top_lineages)


def analyse_run(row: dict, item: dict, correct_fn: Callable, batch: str) -> dict:
    """One run's coverage, pruning causes and late-winner flag (section 8, Pruning regret)."""
    run_dir = Path(config.RUNS_DIR) / row["run_id"]
    pool = list(graph.load_cands(run_dir))           # probe candidates included (module docstring)
    by_id = {c["id"]: c for c in pool}
    correct = {c["id"] for c in pool if correct_fn(item, c)}
    ans = _answer(row, run_dir)
    ret = _returned_correct(ans, by_id, correct, item, correct_fn)
    rec = {"run_id": row["run_id"], "benchmark": row["benchmark"], "item_id": row["item_id"],
           "group": str(item.get("group") or row["item_id"]),
           "n_pool": len(pool), "n_probe": sum(1 for c in pool if _is_probe(c)),
           "n_correct": len(correct), "covered": bool(correct),
           "returned_correct": ret, "pruned": bool(correct) and not ret}
    cycles = state_cycles(run_dir)
    if rec["pruned"]:
        revise_ok = config.BENCHMARKS.get(row["benchmark"], {}).get("revise_allowed", True)
        rec.update(causes(correct, pool, set(graph.load_verify(run_dir)), pop_history(cycles),
                          revise_ok))
    rec["solved"] = ret and ans.get("status") in SOLVED
    rec["late_winner"] = (late_winner(ans.get("cand_id"), pool,
                                      conf_map(cycles, row["run_id"], batch))
                          if rec["solved"] else None)
    rec["has_pop"] = pop_history(cycles) is not None
    return rec


# ---------------------------------------------------------------- aggregation
def bootstrap_ci(values: list[float], n: int = 2000, seed: int = 0,
                 clusters: list | None = None) -> list[float] | None:
    """95% percentile CI of the mean over items, resampling clusters of items (each item its
    own cluster when clusters is None); a resample's value is the mean over its items."""
    if not values:
        return None
    v = np.asarray(values, dtype=float)
    keys = list(clusters) if clusters is not None else list(range(v.size))
    uniq = {k: i for i, k in enumerate(dict.fromkeys(keys))}
    cid = np.array([uniq[k] for k in keys])
    k = len(uniq)
    sums = np.bincount(cid, weights=v, minlength=k)
    counts = np.bincount(cid, minlength=k).astype(float)
    draws = np.random.default_rng(seed).integers(0, k, size=(n, k))
    means = sums[draws].sum(axis=1) / counts[draws].sum(axis=1)
    return [round(float(np.percentile(means, 2.5)), 4), round(float(np.percentile(means, 97.5)), 4)]


def item_rate(recs: list[dict], fn: Callable[[dict], float | None], n_boot: int) -> dict:
    """Per-item mean of fn over runs (None skipped), then mean over items with an item-cluster
    CI (clusters = item groups)."""
    per_item: dict[str, list[float]] = {}
    group: dict[str, str] = {}
    for r in recs:
        x = fn(r)
        if x is not None:
            per_item.setdefault(r["item_id"], []).append(float(x))
            group[r["item_id"]] = r.get("group") or r["item_id"]
    ids = list(per_item)
    vals = [sum(per_item[i]) / len(per_item[i]) for i in ids]
    return {"rate": round(sum(vals) / len(vals), 4) if vals else None,
            "ci95": bootstrap_ci(vals, n=n_boot, clusters=[group[i] for i in ids]),
            "n_items": len(vals), "n_clusters": len(set(group[i] for i in ids))}


def _cause(key: str):
    """Run indicator for one cause flag: 0 when not pruned, None when the flag is unknown."""
    def f(r: dict) -> float | None:
        if not r["pruned"]:
            return 0.0
        v = r.get(key)
        return None if v is None else float(bool(v))
    return f


def _primary(name: str):
    return lambda r: 1.0 if r["pruned"] and r.get("primary") == name else 0.0


def summarize(recs: list[dict], n_boot: int = 2000) -> dict:
    """Benchmark-level report. Cause rates are over keyed items (denominator = all items,
    a non-pruned run counts 0); (b) is computed over runs with pop data only."""
    out = {"n_runs": len(recs), "n_items": len({r["item_id"] for r in recs}),
           "n_runs_with_pop": sum(1 for r in recs if r["has_pop"]),
           "coverage": item_rate(recs, lambda r: float(r["covered"]), n_boot),
           "correct_but_pruned": item_rate(recs, lambda r: float(r["pruned"]), n_boot)}
    out["cause_a_never_verified"] = item_rate(recs, _cause("never_verified"), n_boot)
    out["cause_b_evicted"] = item_rate([r for r in recs if r["has_pop"]], _cause("evicted"), n_boot)
    if recs and not config.BENCHMARKS.get(recs[0]["benchmark"], {}).get("revise_allowed", True):
        out["cause_c_never_revised"] = {"rate": None, "ci95": None, "n_items": 0,
                                        "note": "revise not allowed on this benchmark"}
    else:
        out["cause_c_never_revised"] = item_rate(recs, _cause("never_revised"), n_boot)
    out["primary"] = {k: item_rate(recs, _primary(k), n_boot) for k in ("a", "b", "c", "other")}
    abc = [out["primary"][k]["rate"] or 0.0 for k in ("a", "b", "c")]
    out["primary_abc_sum"] = round(sum(abc), 4)
    out["late_winner"] = item_rate(recs, lambda r: None if r["late_winner"] is None
                                   else float(r["late_winner"]), n_boot)
    out["n_solved_runs"] = sum(1 for r in recs if r["solved"])
    return out


def _default_loaders():
    from .. import data, score   # bench-owned; imported lazily so tests can inject fakes
    return data.get_item, score.cand_correct


def compute(batch: str, *, arm: str = "scaffold", item_loader: Callable | None = None,
            correct_fn: Callable | None = None, n_boot: int = 2000) -> dict:
    """Pruning regret over results/<batch>/runs.jsonl; writes results/<batch>/pruning_regret.json."""
    if item_loader is None or correct_fn is None:
        dl, dc = _default_loaders()
        item_loader, correct_fn = item_loader or dl, correct_fn or dc
    runs = [r for r in read_jsonl(Path(config.RESULTS_DIR) / batch / "runs.jsonl")
            if arm is None or r.get("arm") == arm]
    items: dict[tuple, dict] = {}
    recs = []
    for row in runs:
        key = (row["benchmark"], row["item_id"])
        if key not in items:
            items[key] = item_loader(*key)
        recs.append(analyse_run(row, items[key], correct_fn, batch))
    report = {"batch": batch, "arm": arm, "n_boot": n_boot, "per_benchmark": {}, "runs": recs}
    for b in sorted({r["benchmark"] for r in recs}):
        report["per_benchmark"][b] = summarize([r for r in recs if r["benchmark"] == b], n_boot)
    write_json(Path(config.RESULTS_DIR) / batch / "pruning_regret.json", report)
    return report


def main(argv: list[str] | None = None) -> int:
    """CLI: print the per-benchmark summary."""
    ap = argparse.ArgumentParser(prog="python -m harness.measure.pruning_regret")
    ap.add_argument("--batch", required=True)
    ap.add_argument("--arm", default="scaffold")
    ap.add_argument("--n-boot", type=int, default=2000)
    a = ap.parse_args(argv)
    rep = compute(a.batch, arm=a.arm, n_boot=a.n_boot)
    print(json.dumps(rep["per_benchmark"], indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
