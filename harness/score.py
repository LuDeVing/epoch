"""Harness-side scoring against the answer keys (ARCHITECTURE.md section 8, Metrics and Decision
rule; section 3 /bench steps 2, 4, 7 and 8). This is the only bench-pipeline module that reads
item["test_output"] (ARC) and item["label"] (BRAINTEASER); the standalone scorers are listed in
harness/README.md (Keys).

score_batch(batch) joins results/<batch>/runs.jsonl with the keys and the run folders and writes
results/<batch>/summary.json and summary.md: solve rate per arm (replicates averaged within item),
paired difference vs plain with a cluster bootstrap over items (BRAINTEASER clusters = puzzle
groups), realized tokens per item beside B, coverage (oracle pass@pool) vs selection accuracy,
pass@R over replicates and abstention rate. Also (plan.md sections 4, 5, 7, 8):
- primary comparison: scaffold vs the primary null, the stronger of bestofn_verify and
  seeded_bestofn per benchmark (taken from --null-from <dev batch> when given, else from this
  batch and marked as not preregistered); one-sided superiority gate (lower one-sided 95% bound,
  the 5th bootstrap percentile, > 0) and TOST equivalence within EQUIV_MARGIN (the 90% interval
  inside +-margin). Null runs whose budget is not the scaffold's spend on that item and
  replicate are left out and counted (matched cost, MSR-02).
- keep/drop: every arm named "<base>-minus-<flag>" is a leave-one-out ablation of <base>;
  P(helps) under a Beta(1,1) prior on discordant items, keep if > KEEP_P.
- headroom filter: plain accuracy per item in [20%, 80%] over >= 3 replicates; with fewer
  replicates the summary says it was not applied.
- judge validation (/bench step 4): AUROC, Brier and adaptive-bin ECE of judge p_raw against
  the key on dev-tune runs, item-cluster bootstrap CIs; flagged as blocking when the judge's pick
  does not beat a random pick among the judged candidates.
Every comparison pairs items both arms completed and reports the counts. A run that crashed
without a runs.jsonl row (only in errors.jsonl) is scored as an errored run (wrong).
Pool (coverage) = every candidate row of the run folder, probe candidates included, because the
driver may return a probe program; measure/pruning_regret.py uses the same pool.
CLI: python -m harness.score --batch <name> [--null-from <dev batch>]
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import numpy as np

from . import config, data
from .schemas import option_letter, read_json, read_jsonl, write_json

CHANCE = {"arc": 0.0, "bt": 0.25}
ARM_ORDER = ("plain", "bestofn_vote", "bestofn_verify", "seeded_bestofn", "scaffold")
METHOD_ARM = "scaffold"
NULL_ARMS = ("bestofn_verify", "seeded_bestofn")    # primary null = the stronger (plan.md s5)
EQUIV_MARGIN = 0.03          # plan.md s8: TOST margin, 3 points (placeholder margin)
KEEP_P = 0.95                # plan.md s8: keep a card or flag if P(helps) > 0.95
HEADROOM = (0.2, 0.8)        # plan.md s4: keep items with plain accuracy in [20%, 80%]
HEADROOM_REPS = 3            # plan.md s4: over 3 replicates
MINUS = "-minus-"            # leave-one-out arm name: f"{base}{MINUS}{flag}"


# ---------------------------------------------------------------- correctness
def _grid(g):
    """Normalize to a list of lists of ints, or None if it is not a grid."""
    try:
        return [[int(c) for c in row] for row in g]
    except (TypeError, ValueError):
        return None


def is_correct(item: dict, answer) -> bool:
    """ARC: grid == test_output; BT: letter == option_letter(label)."""
    if answer is None:
        return False
    if item["benchmark"] == "arc":
        if isinstance(answer, str):
            try:
                answer = json.loads(answer)
            except ValueError:
                return False
        g = _grid(answer)
        return g is not None and g == _grid(item["test_output"])
    letter = str(answer).strip().upper()[:1]
    return letter == option_letter(int(item["label"]))


def cand_correct(item: dict, cand) -> bool:
    """Uses cand["pred"] (dict row) or cand.pred (Candidate)."""
    pred = cand.get("pred") if isinstance(cand, dict) else getattr(cand, "pred", None)
    return is_correct(item, pred)


# ---------------------------------------------------------------- statistics
def paired_bootstrap(a: list[float], b: list[float], n: int = 2000, seed: int = 0,
                     clusters: list | None = None) -> dict:
    """Section 8 Metrics: mean of a - b with a 95% bootstrap CI, resampling clusters (items by
    default) with replacement. p_le0 = bootstrap share of differences <= 0 (one-sided).
    ci90_low / ci90_high = 5th and 95th percentiles: ci90_low is the one-sided 95% lower bound
    (superiority gate) and the 90% interval is the TOST interval at alpha 0.05 per side."""
    a_arr, b_arr = np.asarray(a, dtype=float), np.asarray(b, dtype=float)
    if a_arr.shape != b_arr.shape:
        raise ValueError("paired_bootstrap needs equal-length inputs")
    if a_arr.size == 0:
        return {"mean_diff": None, "ci_low": None, "ci_high": None, "ci90_low": None,
                "ci90_high": None, "p_le0": None, "n_items": 0, "n_clusters": 0, "n_boot": n}
    d = a_arr - b_arr
    keys = list(clusters) if clusters is not None else list(range(d.size))
    uniq = {k: i for i, k in enumerate(dict.fromkeys(keys))}
    cid = np.array([uniq[k] for k in keys])
    k = len(uniq)
    sums = np.bincount(cid, weights=d, minlength=k)
    counts = np.bincount(cid, minlength=k).astype(float)
    draws = np.random.default_rng(seed).integers(0, k, size=(n, k))
    boot = sums[draws].sum(axis=1) / counts[draws].sum(axis=1)
    return {"mean_diff": float(d.mean()), "ci_low": float(np.percentile(boot, 2.5)),
            "ci_high": float(np.percentile(boot, 97.5)), "ci90_low": float(np.percentile(boot, 5)),
            "ci90_high": float(np.percentile(boot, 95)), "p_le0": float((boot <= 0).mean()),
            "n_items": int(d.size), "n_clusters": k, "n_boot": n}


def paired_items(a: dict[str, float], b: dict[str, float], groups: dict[str, str],
                 **kw) -> dict:
    """Paired bootstrap on the items both arms completed (item -> replicate-averaged value),
    with the counts: n_a, n_b (items per arm), n_both (paired), n_a_only, n_b_only."""
    common = sorted(set(a) & set(b))
    res = paired_bootstrap([a[i] for i in common], [b[i] for i in common],
                           clusters=[groups.get(i, i) for i in common], **kw)
    res.update({"n_a": len(a), "n_b": len(b), "n_both": len(common),
                "n_a_only": len(set(a) - set(b)), "n_b_only": len(set(b) - set(a))})
    return res


def p_helps(b: int, c: int) -> float:
    """P(theta > 0.5) for theta ~ Beta(1 + b, 1 + c): b discordant items where the full stack
    wins, c where the ablation wins (Beta(1,1) prior on discordant pairs, plan.md s8). Exact for
    integer counts: I_x(a, b) = P(Binomial(a + b - 1, x) >= a)."""
    a1, b1 = 1 + int(b), 1 + int(c)
    n = a1 + b1 - 1
    p_le_half = sum(math.comb(n, j) for j in range(a1, n + 1)) / 2 ** n
    return 1.0 - p_le_half


def keep_drop(full: dict[str, float], minus: dict[str, float]) -> dict:
    """Leave-one-out keep/drop (plan.md s8, MSR-12): items both arms completed, discordant when
    the replicate-averaged solve rates differ; keep iff P(helps) > KEEP_P."""
    common = sorted(set(full) & set(minus))
    b = sum(1 for i in common if full[i] > minus[i])
    c = sum(1 for i in common if full[i] < minus[i])
    p = p_helps(b, c)
    return {"n_both": len(common), "helps": b, "hurts": c, "ties": len(common) - b - c,
            "p_helps": p, "keep": p > KEEP_P}


def keep_drop_pooled(results: list[dict]) -> dict:
    """Accumulate keep_drop results over batches that share one memory and calibration snapshot
    (the batch count is fixed in advance, plan.md s8): discordant counts are summed."""
    b = sum(r["helps"] for r in results)
    c = sum(r["hurts"] for r in results)
    p = p_helps(b, c)
    return {"n_batches": len(results), "helps": b, "hurts": c, "p_helps": p, "keep": p > KEEP_P}


def headroom_filter(plain_rows: list[dict], lo: float = HEADROOM[0], hi: float = HEADROOM[1],
                    min_reps: int = HEADROOM_REPS) -> dict:
    """plan.md s4: keep items whose plain accuracy over replicates is in [lo, hi]. Needs at
    least min_reps replicates per item; otherwise applied=False and the reason says so."""
    reps: dict[str, list[float]] = {}
    for r in plain_rows:
        reps.setdefault(r["item_id"], []).append(float(r["correct"]))
    if not reps:
        return {"applied": False, "replicates": 0, "reason": "headroom filter not applied, no plain runs"}
    n_rep = min(len(v) for v in reps.values())
    if n_rep < min_reps:
        return {"applied": False, "replicates": n_rep,
                "reason": f"headroom filter not applied, replicates={n_rep}"}
    acc = {k: float(np.mean(v)) for k, v in reps.items()}
    keep = sorted(k for k, v in acc.items() if lo <= v <= hi)
    return {"applied": True, "replicates": n_rep, "keep": keep,
            "floor": sorted(k for k, v in acc.items() if v < lo),
            "ceiling": sorted(k for k, v in acc.items() if v > hi),
            "noise_sd": float(np.mean([np.std(v, ddof=1) for v in reps.values()])),
            "reason": f"plain accuracy in [{lo:.0%}, {hi:.0%}] over {n_rep} replicates"}


# ---------------------------------------------------------------- judge validation (/bench step 4)
def auroc(conf: list[float], y: list[int]) -> float | None:
    """Mann-Whitney AUROC (ties count half); None without both classes."""
    pos = [c for c, t in zip(conf, y) if t]
    neg = [c for c, t in zip(conf, y) if not t]
    if not pos or not neg:
        return None
    wins = sum((p > q) + 0.5 * (p == q) for p in pos for q in neg)
    return float(wins / (len(pos) * len(neg)))


def brier(conf: list[float], y: list[int]) -> float | None:
    return float(np.mean([(c - t) ** 2 for c, t in zip(conf, y)])) if conf else None


def adaptive_ece(conf: list[float], y: list[int], n_bins: int = 10) -> float | None:
    """Adaptive-bin (equal-mass) ECE: sort by confidence, split into n_bins equal-count bins."""
    if not conf:
        return None
    order = np.argsort(np.asarray(conf, dtype=float), kind="mergesort")
    c, t = np.asarray(conf, dtype=float)[order], np.asarray(y, dtype=float)[order]
    bins = [b for b in np.array_split(np.arange(len(c)), min(n_bins, len(c))) if b.size]
    return float(sum(b.size * abs(c[b].mean() - t[b].mean()) for b in bins) / len(c))


def _cluster_ci(recs: list[dict], fn, n: int = 2000, seed: int = 0) -> list[float] | None:
    """95% percentile CI of fn(records) resampling item clusters."""
    by: dict[str, list[dict]] = {}
    for r in recs:
        by.setdefault(r["group"], []).append(r)
    keys = list(by)
    if not keys:
        return None
    rng = np.random.default_rng(seed)
    vals = []
    for _ in range(n):
        smp = [x for k in rng.integers(0, len(keys), size=len(keys)) for x in by[keys[k]]]
        v = fn(smp)
        if v is not None:
            vals.append(v)
    if not vals:
        return None
    return [float(np.percentile(vals, 2.5)), float(np.percentile(vals, 97.5))]


def judge_validation(scored: list[dict], items: dict[str, dict], n_boot: int = 2000) -> dict:
    """/bench step 4 on dev-tune runs: every judged candidate (judgments.jsonl p_raw) against
    the key. Selection = the top-p_raw candidate's correctness per run with >= 2 judged
    candidates, against a random pick (mean correctness of the judged candidates); blocking
    when the paired difference's lower 95% bound is <= 0. The self-preference and
    length-invariance probes need model calls and are not run here."""
    recs, sel = [], []
    for s in scored:
        if s.get("split") != "dev-tune" or s.get("error"):
            continue
        rd = Path(config.RUNS_DIR) / s["run_id"]
        judg = {r.get("id"): r for r in read_jsonl(rd / "judgments.jsonl") if r.get("p_raw") is not None}
        if not judg:
            continue
        cands = {c.get("id"): c for c in pool(s["run_id"])}
        item = items[s["item_id"]]
        run_recs = [{"group": s["group"], "item_id": s["item_id"], "p": float(j["p_raw"]),
                     "y": int(cand_correct(item, cands[cid]))}
                    for cid, j in judg.items() if cid in cands]
        recs += run_recs
        if len(run_recs) >= 2:
            top = max(run_recs, key=lambda r: r["p"])
            sel.append({"group": s["group"], "item_id": s["item_id"], "pick": float(top["y"]),
                        "random": float(np.mean([r["y"] for r in run_recs]))})
    if not recs:
        return {"n_judged": 0, "note": "no judged candidates on dev-tune in this batch; judge not validated"}

    def m(fn):
        return lambda rs: fn([r["p"] for r in rs], [r["y"] for r in rs])
    out = {"n_judged": len(recs), "n_items": len({r["item_id"] for r in recs}),
           "auroc": auroc(*zip(*[(r["p"], r["y"]) for r in recs])), "auroc_ci": _cluster_ci(recs, m(auroc), n_boot),
           "brier": brier([r["p"] for r in recs], [r["y"] for r in recs]),
           "brier_ci": _cluster_ci(recs, m(brier), n_boot),
           "ece": adaptive_ece([r["p"] for r in recs], [r["y"] for r in recs]),
           "ece_ci": _cluster_ci(recs, m(adaptive_ece), n_boot),
           "probes": "self-preference and length-invariance probes not run (model calls)"}
    if sel:
        d = paired_bootstrap([r["pick"] for r in sel], [r["random"] for r in sel],
                             clusters=[r["group"] for r in sel], n=n_boot)
        out.update({"n_selection_runs": len(sel), "selection": float(np.mean([r["pick"] for r in sel])),
                    "random_pick": float(np.mean([r["random"] for r in sel])), "selection_vs_random": d,
                    "blocking": d["ci_low"] is None or d["ci_low"] <= 0})
    else:
        out.update({"n_selection_runs": 0, "blocking": True,
                    "note": "no run with two or more judged candidates: selection not testable"})
    return out


# ---------------------------------------------------------------- reading a batch
def batch_dir(batch: str) -> Path:
    return Path(config.RESULTS_DIR) / batch


def crash_row(run_id: str, error: str, batch: str | None = None) -> dict | None:
    """An errored runs.jsonl-style row for a run that has only an errors.jsonl entry; None when
    the run id does not follow the README pattern batch__benchmark__item__arm__r<rep>."""
    parts = run_id.split("__")
    if len(parts) != 5 or not parts[4].startswith("r") or not parts[4][1:].isdigit():
        return None
    return {"batch": batch or parts[0], "benchmark": parts[1], "item_id": parts[2], "arm": parts[3],
            "replicate": int(parts[4][1:]), "run_id": run_id, "status": "error", "answer": None,
            "spent_tokens": 0, "rounds": 0, "error": error, "crash": True, "from_errors_log": True}


def load_runs(batch: str) -> list[dict]:
    """runs.jsonl rows, last row per run_id wins. A run that appears only in errors.jsonl (it
    raised before writing a row, older bench versions) is added as an errored row so the item
    stays in the denominator and counts wrong; logged skips (no matched-cost budget) are not
    runs and are left out."""
    rows = {}
    for r in read_jsonl(batch_dir(batch) / "runs.jsonl"):
        rows[r["run_id"]] = r
    for e in read_jsonl(batch_dir(batch) / "errors.jsonl"):
        rid, msg = e.get("run_id"), str(e.get("error") or "")
        if not rid or rid in rows or "skipped:" in msg:
            continue
        row = crash_row(rid, msg, batch)
        if row is not None:
            rows[rid] = row
    return list(rows.values())


def pool(run_id: str) -> list[dict]:
    """All candidate rows of a run folder (runs/<id>/cands/*.jsonl)."""
    out = []
    for f in sorted((Path(config.RUNS_DIR) / run_id / "cands").glob("*.jsonl")):
        out.extend(read_jsonl(f))
    return out


def score_run(row: dict, item: dict) -> dict:
    """Correct, forced-choice correct (best guess for abstentions), coverage, pool size."""
    ans = read_json(Path(config.RUNS_DIR) / row["run_id"] / "answer.json", {}) or {}
    answer = row.get("answer")
    forced = answer if answer is not None else ans.get("best_guess")
    cands = pool(row["run_id"])
    correct = is_correct(item, answer)
    covered = any(cand_correct(item, c) for c in cands) if cands else correct
    budget_tokens = row.get("budget_tokens")
    return {"run_id": row["run_id"], "benchmark": row["benchmark"], "item_id": row["item_id"],
            "arm": row["arm"], "replicate": int(row.get("replicate", 0)),
            "group": item.get("group", item["id"]), "split": item.get("split"),
            "correct": correct, "forced_correct": is_correct(item, forced), "covered": covered,
            "pool_size": len(cands), "abstain": row.get("status") == "abstain",
            "error": row.get("status") == "error",
            "crash": bool(row.get("crash")),
            "spent_tokens": int(row.get("spent_tokens") or 0),
            "budget_tokens": int(budget_tokens) if budget_tokens else None,
            "overshoot": int(row.get("overshoot") or 0)}


def _item_means(rows: list[dict], field: str) -> dict[str, float]:
    by: dict[str, list[float]] = {}
    for r in rows:
        by.setdefault(r["item_id"], []).append(float(r[field]))
    return {k: float(np.mean(v)) for k, v in by.items()}


def _budget(batch: str, benchmark: str) -> dict:
    """budget.json written by bench.py: {benchmark: {backend: {cot_median, m, B, ...}}}. The
    backend is the one in config_<benchmark>.json (the batch's bench call); with no config and
    several backends the first is used and the record says so."""
    per_bm = (read_json(batch_dir(batch) / "budget.json", {}) or {}).get(benchmark, {})
    if not per_bm:
        return {}
    want = (read_json(batch_dir(batch) / f"config_{benchmark}.json", {}) or {}).get("backend")
    if want in per_bm:
        return per_bm[want]
    rec = dict(next(iter(per_bm.values())))
    if len(per_bm) > 1:
        rec["note"] = f"several backends in budget.json ({', '.join(per_bm)}); showing the first"
    return rec


def arm_stats(rows: list[dict], plain_rows: list[dict], groups: dict[str, str], B) -> dict:
    """Per-arm metrics with the paired cluster bootstrap vs plain (on the items both completed).
    n_failed_spent = errored runs that still consumed tokens (for plain: output-cap and similar
    failures; scored wrong and counted in the cost median); n_crash = runs that raised."""
    solve = _item_means(rows, "correct")
    any_rep = {k: float(v > 0) for k, v in solve.items()}
    covered = [r for r in rows if r["covered"]]
    toks = [r["spent_tokens"] for r in rows]
    budgeted = [r for r in rows if r.get("budget_tokens")]
    out = {"n_items": len(solve), "n_runs": len(rows),
           "solve_rate": float(np.mean(list(solve.values()))),
           "forced_solve_rate": float(np.mean(list(_item_means(rows, "forced_correct").values()))),
           "pass_at_R": float(np.mean(list(any_rep.values()))),
           "coverage": float(np.mean(list(_item_means(rows, "covered").values()))),
           "selection": (sum(r["correct"] for r in covered) / len(covered)) if covered else None,
           "abstain_rate": float(np.mean([r["abstain"] for r in rows])),
           "n_errors": int(sum(1 for r in rows if r.get("error"))),
           "n_failed_spent": int(sum(1 for r in rows if r.get("error") and r["spent_tokens"] > 0)),
           "n_crash": int(sum(1 for r in rows if r.get("crash"))),
           "mean_pool": float(np.mean([r["pool_size"] for r in rows])),
           "tokens_mean": float(np.mean(toks)), "tokens_median": float(np.median(toks)),
           "B": B, "spend_over_B": (float(np.mean(toks)) / B) if B else None,
           "spend_over_budget": (float(np.mean([r["spent_tokens"] / r["budget_tokens"]
                                                for r in budgeted])) if budgeted else None),
           "overshoot_mean": (float(np.mean([r["overshoot"] for r in budgeted])) if budgeted else None),
           "n_over_budget": int(sum(1 for r in budgeted if r["overshoot"] > 0))}
    out["vs_plain"] = (paired_items(solve, _item_means(plain_rows, "correct"), groups)
                       if plain_rows else None)
    return out


def choose_null(arms: dict, benchmark: str, null_from: str | None = None) -> dict:
    """plan.md s5: primary null = the stronger of bestofn_verify and seeded_bestofn per
    benchmark, chosen on dev-tune before the comparison batch. From null_from's summary.json
    when given (preregistered), else from this batch's solve rates (marked as not
    preregistered). Ties go to bestofn_verify."""
    source, rates = None, {}
    if null_from:
        prior = (read_json(batch_dir(null_from) / "summary.json", {}) or {})
        parms = ((prior.get("benchmarks") or {}).get(benchmark) or {}).get("arms") or {}
        rates = {a: parms[a]["solve_rate"] for a in NULL_ARMS if a in parms}
        source = f"batch {null_from} (chosen before this batch)"
    if not rates:
        rates = {a: arms[a]["solve_rate"] for a in NULL_ARMS if a in arms}
        source = ("this batch (not preregistered: pass --null-from <dev-tune batch>)"
                  + (f"; batch {null_from} has no null arm" if null_from else ""))
    if not rates:
        return {"arm": None, "source": None, "rates": {}}
    best = max(rates.values())
    arm = next(a for a in NULL_ARMS if rates.get(a) == best)
    return {"arm": arm, "source": source, "rates": rates}


def primary_comparison(scored: list[dict], arms: dict, groups: dict[str, str], benchmark: str,
                       null_from: str | None = None, margin: float = EQUIV_MARGIN) -> dict:
    """plan.md s7-8 and ARCHITECTURE s8: scaffold minus the primary null, paired on items both
    completed, replicates averaged within item, cluster bootstrap. Gate: one-sided superiority,
    lower one-sided 95% bound (ci90_low) > 0. TOST: equivalent within +-margin iff the 90%
    interval lies inside (-margin, +margin). Null runs not matched to the scaffold's realized
    spend on the same item and replicate are left out and counted."""
    null = choose_null(arms, benchmark, null_from)
    out = {"method": METHOD_ARM, "null": null, "margin": margin}
    if METHOD_ARM not in arms or not null["arm"]:
        out["note"] = ("primary comparison not available: "
                       + ("no scaffold arm" if METHOD_ARM not in arms else "no bestofn_verify or seeded_bestofn arm"))
        return out
    meth = [s for s in scored if s["arm"] == METHOD_ARM]
    spend = {(s["item_id"], s["replicate"]): s for s in meth}
    nrows, unmatched = [], 0
    for s in scored:
        if s["arm"] != null["arm"]:
            continue
        sc = spend.get((s["item_id"], s["replicate"]))
        if s.get("budget_tokens") is not None and (sc is None or sc["error"]
                                                   or sc["spent_tokens"] != s["budget_tokens"]):
            unmatched += 1
            continue
        nrows.append(s)
    d = paired_items(_item_means(meth, "correct"), _item_means(nrows, "correct"), groups)
    out.update(d)
    out["n_null_unmatched"] = unmatched
    out["n_method_error_items"] = len({s["item_id"] for s in meth if s["error"]})
    if d["mean_diff"] is None:
        out.update({"gate_pass": None, "equivalent": None, "note": "no paired items"})
        return out
    out["gate_pass"] = d["ci90_low"] > 0
    out["equivalent"] = d["ci90_low"] > -margin and d["ci90_high"] < margin
    return out


def ablations(scored: list[dict], groups: dict[str, str]) -> dict:
    """Leave-one-out keep/drop for every "<base>-minus-<flag>" arm whose base arm is present."""
    by_arm: dict[str, list[dict]] = {}
    for s in scored:
        by_arm.setdefault(s["arm"], []).append(s)
    out = {}
    for arm in sorted(by_arm):
        if MINUS not in arm:
            continue
        base, flag = arm.split(MINUS, 1)
        if base not in by_arm:
            out[arm] = {"base": base, "flag": flag, "note": f"base arm {base} not in this batch"}
            continue
        res = keep_drop(_item_means(by_arm[base], "correct"), _item_means(by_arm[arm], "correct"))
        reps = min(len([r for r in by_arm[arm] if r["item_id"] == i]) for i in {r["item_id"] for r in by_arm[arm]})
        out[arm] = {"base": base, "flag": flag, "replicates": reps, **res}
    return out


def score_benchmark(batch: str, benchmark: str, rows: list[dict], null_from: str | None = None) -> dict:
    items = {it["id"]: it for it in data.load_items(benchmark)}
    scored, missing = [], []
    for r in rows:
        if r["item_id"] in items:
            scored.append(score_run(r, items[r["item_id"]]))
        else:
            missing.append(r["run_id"])
    groups = {s["item_id"]: s["group"] for s in scored}
    budget = _budget(batch, benchmark)
    plain_rows = [s for s in scored if s["arm"] == "plain"]
    arms = sorted({s["arm"] for s in scored},
                  key=lambda a: (ARM_ORDER.index(a) if a in ARM_ORDER else 99, a))
    table = {a: arm_stats([s for s in scored if s["arm"] == a], plain_rows, groups,
                          budget.get("B")) for a in arms}
    return {"benchmark": benchmark, "chance": CHANCE.get(benchmark), "budget": budget,
            "arms": table,
            "primary": primary_comparison(scored, table, groups, benchmark, null_from),
            "keep_drop": ablations(scored, groups),
            "headroom": headroom_filter(plain_rows),
            "judge_validation": judge_validation(scored, items),
            "missing_items": missing, "runs": scored}


# ---------------------------------------------------------------- reports
def _pct(x) -> str:
    return "-" if x is None else f"{100 * x:.1f}%"


def _ci(d: dict | None) -> str:
    if not d or d.get("mean_diff") is None:
        return "-"
    return (f"{100 * d['mean_diff']:+.1f} [{100 * d['ci_low']:+.1f}, {100 * d['ci_high']:+.1f}]"
            f" p<=0 {d['p_le0']:.3f}")


def _counts_md(res: dict) -> list[str]:
    """Paired counts and failure counts per arm, so unequal n is visible."""
    out = []
    for arm, s in res["arms"].items():
        vp = s.get("vs_plain")
        bits = []
        if arm != "plain" and vp and vp.get("n_both") is not None and (vp["n_a_only"] or vp["n_b_only"]):
            bits.append(f"vs plain paired on {vp['n_both']} items ({vp['n_a_only']} only in {arm}, "
                        f"{vp['n_b_only']} only in plain)")
        if s.get("n_failed_spent"):
            bits.append(f"{s['n_failed_spent']} errored runs that spent tokens (wrong, in the mean tokens"
                        + (" and the cost median)" if arm == "plain" else ")"))
        if s.get("n_crash"):
            bits.append(f"{s['n_crash']} crashed runs (raised before answering; wrong)")
        if bits:
            out.append(f"- {arm}: " + "; ".join(bits) + ".")
    return ([""] + out) if out else []


def _primary_md(p: dict | None) -> list[str]:
    if not p:
        return []
    out = ["", "### Primary comparison (plan.md s7-8)", ""]
    nl = p["null"]
    if nl.get("arm"):
        rates = ", ".join(f"{a} {_pct(v)}" for a, v in nl["rates"].items())
        out.append(f"1. Primary null: {nl['arm']} (stronger of {rates}; chosen from {nl['source']}).")
    else:
        out.append("1. Primary null: none (no bestofn_verify or seeded_bestofn arm).")
    if p.get("note") and p.get("gate_pass") is None and p.get("mean_diff") is None:
        out.append(f"2. Superiority gate: not computed ({p['note']}).")
        out.append("3. TOST equivalence: not computed.")
        return out
    out.append(f"2. Superiority gate, {p['method']} minus {nl['arm']}: {100 * p['mean_diff']:+.1f} pts, "
               f"one-sided 95% lower bound {100 * p['ci90_low']:+.1f} -> "
               f"{'PASS (bound > 0)' if p['gate_pass'] else 'FAIL (bound <= 0)'}; two-sided 95% CI "
               f"[{100 * p['ci_low']:+.1f}, {100 * p['ci_high']:+.1f}].")
    out.append(f"3. TOST equivalence within +-{100 * p['margin']:.0f} pts (preregistered placeholder margin): "
               f"90% interval [{100 * p['ci90_low']:+.1f}, {100 * p['ci90_high']:+.1f}] -> "
               f"{'equivalent' if p['equivalent'] else 'equivalence not shown'}.")
    out.append(f"Paired on {p['n_both']} items ({p['n_a_only']} scaffold-only, {p['n_b_only']} null-only); "
               f"{p['n_null_unmatched']} null runs left out for unmatched cost; "
               f"{p['n_method_error_items']} items with an errored scaffold run.")
    return out


def _keep_drop_md(kd: dict | None) -> list[str]:
    if not kd:
        return []
    out = ["", "### Keep/drop (leave-one-out, Beta(1,1) on discordant items, keep if P(helps) > "
           f"{KEEP_P})", ""]
    for arm, r in kd.items():
        if "p_helps" not in r:
            out.append(f"- {arm}: {r['note']}.")
            continue
        out.append(f"- {r['flag']} (base {r['base']}): helps {r['helps']}, hurts {r['hurts']}, ties "
                   f"{r['ties']} on {r['n_both']} items, {r['replicates']} replicates; P(helps) "
                   f"{r['p_helps']:.3f} -> {'keep' if r['keep'] else 'drop'} (this batch only).")
    return out


def _headroom_md(h: dict | None) -> list[str]:
    if not h:
        return []
    if not h["applied"]:
        return ["", f"Headroom: {h['reason']}."]
    return ["", f"Headroom ({h['reason']}): keep {len(h['keep'])} items, floor {len(h['floor'])}, "
                f"ceiling {len(h['ceiling'])}; plain noise floor (mean replicate SD) {h['noise_sd']:.3f}."]


def _judge_md(j: dict | None) -> list[str]:
    if not j:
        return []
    if not j.get("n_judged"):
        return ["", f"Judge validation: {j.get('note')}."]

    def ci(x):
        return "-" if not x else f"[{x[0]:.3f}, {x[1]:.3f}]"
    auc = "-" if j["auroc"] is None else f"{j['auroc']:.3f}"
    line = (f"Judge validation (dev-tune, {j['n_judged']} judged candidates on {j['n_items']} items): AUROC "
            f"{auc} {ci(j['auroc_ci'])}, Brier {j['brier']:.3f} {ci(j['brier_ci'])}, adaptive ECE "
            f"{j['ece']:.3f} {ci(j['ece_ci'])}")
    if j.get("n_selection_runs"):
        line += (f"; selection {_pct(j['selection'])} vs random pick {_pct(j['random_pick'])} on "
                 f"{j['n_selection_runs']} runs")
    line += f"; {'BLOCKING: judge pick does not beat a random pick' if j['blocking'] else 'not blocking'}. "
    return ["", line + j["probes"] + "."]


def render_md(summary: dict) -> str:
    lines = [f"# Batch {summary['batch']}", ""]
    for bm, res in summary["benchmarks"].items():
        b = res["budget"]
        lines += [f"## {bm}", "",
                  f"chance {_pct(res['chance'])}; backend {b.get('backend', '-')}; "
                  f"model {b.get('model', '-')}; cot_median {b.get('cot_median', '-')}; "
                  f"m {b.get('m', '-')}; B {b.get('B', '-')} tokens", "",
                  "| arm | items | runs | solve | diff vs plain, pts [95% CI] | tokens/item-run | B "
                  "| spend/B | spend/budget (over) | coverage | selection | pass@R | abstain | errors |",
                  "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
        for arm, s in res["arms"].items():
            spend = "-" if s["spend_over_B"] is None else f"{s['spend_over_B']:.2f}"
            sb = ("-" if s.get("spend_over_budget") is None
                  else f"{s['spend_over_budget']:.2f} ({s.get('n_over_budget', 0)})")
            lines.append(
                f"| {arm} | {s['n_items']} | {s['n_runs']} | {_pct(s['solve_rate'])} | "
                f"{_ci(s['vs_plain']) if arm != 'plain' else '-'} | {s['tokens_mean']:.0f} | "
                f"{s['B'] if s['B'] is not None else '-'} | {spend} | {sb} | {_pct(s['coverage'])} | "
                f"{_pct(s['selection'])} | {_pct(s['pass_at_R'])} | {_pct(s['abstain_rate'])} | "
                f"{s.get('n_errors', 0)} |")
        lines += _counts_md(res) + _primary_md(res.get("primary")) + _keep_drop_md(res.get("keep_drop"))
        lines += _headroom_md(res.get("headroom")) + _judge_md(res.get("judge_validation"))
        if b.get("note"):
            lines.append(f"\nBudget: {b['note']}.")
        if res["missing_items"]:
            lines.append(f"\n{len(res['missing_items'])} runs reference unknown items.")
        lines.append("")
    lines += ["Solve = exact match on the key, replicates averaged within item; diff vs plain = "
              "paired cluster bootstrap over items both arms completed (BRAINTEASER clusters = "
              "puzzle groups), p<=0 is the one-sided bootstrap share. Coverage = oracle pass@pool "
              "(probe candidates included); selection = "
              "solved share of covered runs. Abstentions and errored runs (crashes and plain "
              "runs that failed after spending tokens included) count as wrong. "
              "spend/budget = mean realized spend over the run's matched-cost budget (scaffold: B; "
              "best-of-N: the scaffold's spend), with the count of runs over their budget in "
              "parentheses.", ""]
    return "\n".join(lines)


def score_batch(batch: str, null_from: str | None = None) -> dict:
    """Score a batch; write results/<batch>/summary.json and summary.md."""
    rows = load_runs(batch)
    by_bm: dict[str, list[dict]] = {}
    for r in rows:
        by_bm.setdefault(r["benchmark"], []).append(r)
    summary = {"batch": batch, "null_from": null_from,
               "benchmarks": {bm: score_benchmark(batch, bm, rs, null_from)
                              for bm, rs in sorted(by_bm.items())}}
    out = batch_dir(batch)
    out.mkdir(parents=True, exist_ok=True)
    write_json(out / "summary.json", summary)
    (out / "summary.md").write_text(render_md(summary), encoding="utf-8")
    return summary


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Score a results batch against the keys.")
    ap.add_argument("--batch", required=True)
    ap.add_argument("--null-from", default=None,
                    help="dev-tune batch whose summary.json fixes the primary null (plan.md s5)")
    args = ap.parse_args(argv)
    score_batch(args.batch, args.null_from)
    print((batch_dir(args.batch) / "summary.md").read_text(encoding="utf-8"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
