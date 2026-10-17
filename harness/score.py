"""Harness-side scoring against the answer keys (ARCHITECTURE.md section 8, Metrics and Decision
rule; section 3 /bench step 7). This is the ONLY module that reads item["test_output"] (ARC) and
item["label"] (BRAINTEASER).

score_batch(batch) joins results/<batch>/runs.jsonl with the keys and the run folders and writes
results/<batch>/summary.json and summary.md: solve rate per arm (replicates averaged within item),
paired difference vs plain with a cluster bootstrap over items (BRAINTEASER clusters = puzzle
groups), realized tokens per item beside B, coverage (oracle pass@pool) vs selection accuracy,
pass@R over replicates and abstention rate.
CLI: python -m harness.score --batch <name>
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np

from . import config, data
from .schemas import option_letter, read_json, read_jsonl, write_json

CHANCE = {"arc": 0.0, "bt": 0.25}
ARM_ORDER = ("plain", "bestofn_vote", "bestofn_verify", "seeded_bestofn", "scaffold")


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
    default) with replacement. p_le0 = bootstrap share of differences <= 0 (one-sided)."""
    a_arr, b_arr = np.asarray(a, dtype=float), np.asarray(b, dtype=float)
    if a_arr.shape != b_arr.shape:
        raise ValueError("paired_bootstrap needs equal-length inputs")
    if a_arr.size == 0:
        return {"mean_diff": None, "ci_low": None, "ci_high": None, "p_le0": None,
                "n_items": 0, "n_clusters": 0, "n_boot": n}
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
            "ci_high": float(np.percentile(boot, 97.5)), "p_le0": float((boot <= 0).mean()),
            "n_items": int(d.size), "n_clusters": k, "n_boot": n}


# ---------------------------------------------------------------- reading a batch
def batch_dir(batch: str) -> Path:
    return Path(config.RESULTS_DIR) / batch


def load_runs(batch: str) -> list[dict]:
    """runs.jsonl rows, last row per run_id wins."""
    rows = {}
    for r in read_jsonl(batch_dir(batch) / "runs.jsonl"):
        rows[r["run_id"]] = r
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
            "spent_tokens": int(row.get("spent_tokens") or 0),
            "budget_tokens": int(budget_tokens) if budget_tokens else None,
            "overshoot": int(row.get("overshoot") or 0)}


def _item_means(rows: list[dict], field: str) -> dict[str, float]:
    by: dict[str, list[float]] = {}
    for r in rows:
        by.setdefault(r["item_id"], []).append(float(r[field]))
    return {k: float(np.mean(v)) for k, v in by.items()}


def _budget(batch: str, benchmark: str) -> dict:
    """budget.json written by bench.py: {benchmark: {backend: {cot_median, m, B, ...}}}."""
    per_bm = (read_json(batch_dir(batch) / "budget.json", {}) or {}).get(benchmark, {})
    return next(iter(per_bm.values()), {}) if per_bm else {}


def arm_stats(rows: list[dict], plain_rows: list[dict], groups: dict[str, str], B) -> dict:
    """Per-arm metrics with the paired cluster bootstrap vs plain."""
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
           "mean_pool": float(np.mean([r["pool_size"] for r in rows])),
           "tokens_mean": float(np.mean(toks)), "tokens_median": float(np.median(toks)),
           "B": B, "spend_over_B": (float(np.mean(toks)) / B) if B else None,
           "spend_over_budget": (float(np.mean([r["spent_tokens"] / r["budget_tokens"]
                                                for r in budgeted])) if budgeted else None),
           "overshoot_mean": (float(np.mean([r["overshoot"] for r in budgeted])) if budgeted else None),
           "n_over_budget": int(sum(1 for r in budgeted if r["overshoot"] > 0))}
    base = _item_means(plain_rows, "correct")
    common = sorted(set(solve) & set(base))
    out["vs_plain"] = paired_bootstrap([solve[i] for i in common], [base[i] for i in common],
                                       clusters=[groups[i] for i in common]) if plain_rows else None
    return out


def score_benchmark(batch: str, benchmark: str, rows: list[dict]) -> dict:
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
            "arms": table, "missing_items": missing, "runs": scored}


# ---------------------------------------------------------------- reports
def _pct(x) -> str:
    return "-" if x is None else f"{100 * x:.1f}%"


def _ci(d: dict | None) -> str:
    if not d or d.get("mean_diff") is None:
        return "-"
    return (f"{100 * d['mean_diff']:+.1f} [{100 * d['ci_low']:+.1f}, {100 * d['ci_high']:+.1f}]"
            f" p<=0 {d['p_le0']:.3f}")


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
        if res["missing_items"]:
            lines.append(f"\n{len(res['missing_items'])} runs reference unknown items.")
        lines.append("")
    lines += ["Solve = exact match on the key, replicates averaged within item; diff vs plain = "
              "paired cluster bootstrap over items (BRAINTEASER clusters = puzzle groups), "
              "p<=0 is the one-sided bootstrap share. Coverage = oracle pass@pool; selection = "
              "solved share of covered runs. Abstentions and errored runs count as wrong. "
              "spend/budget = mean realized spend over the run's matched-cost budget (scaffold: B; "
              "best-of-N: the scaffold's spend), with the count of runs over their budget in "
              "parentheses.", ""]
    return "\n".join(lines)


def score_batch(batch: str) -> dict:
    """Score a batch; write results/<batch>/summary.json and summary.md."""
    rows = load_runs(batch)
    by_bm: dict[str, list[dict]] = {}
    for r in rows:
        by_bm.setdefault(r["benchmark"], []).append(r)
    summary = {"batch": batch,
               "benchmarks": {bm: score_benchmark(batch, bm, rs) for bm, rs in sorted(by_bm.items())}}
    out = batch_dir(batch)
    out.mkdir(parents=True, exist_ok=True)
    write_json(out / "summary.json", summary)
    (out / "summary.md").write_text(render_md(summary), encoding="utf-8")
    return summary


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Score a results batch against the keys.")
    ap.add_argument("--batch", required=True)
    args = ap.parse_args(argv)
    score_batch(args.batch)
    print((batch_dir(args.batch) / "summary.md").read_text(encoding="utf-8"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
