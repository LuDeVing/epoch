"""Measurement harness CLI (ARCHITECTURE.md section 3 /bench steps 1, 5 and 7; section 8 Cost and
Arms; section 9 step 1).

Order of work for one benchmark:
0. Template lint (section 3: blocking, before every batch): lint.lint_templates() must report no
   fails, else the batch does not start.
1. Plain CoT on the chosen items x replicates (this is the plain arm and the cost measurement):
   results/<batch>/cost.jsonl rows {benchmark, backend, model, item_id, replicate, tokens} and
   results/<batch>/budget.json {benchmark: {backend: {model, cot_median, m, B, n}}}.
   B = m x median plain-CoT tokens per item (or the cot_median of --budget-from <batch>). Every
   plain run that spent tokens enters the median, including runs that failed after spending
   them (for example the CLI output-token cap): those are final plain failures, scored wrong
   and never retried. Cost rows carry split and model and the median uses only rows of this
   call's benchmark, backend, model and split. B = max(m x cot_median, HTSA_MIN_B), the floor
   recorded in budget.json (min_B, B_unfloored). Plain runs with zero tokens (no call made)
   are retried; with no usable plain run and no --budget-from the batch stops with an error.
   HTSA_FIXED_B=<tokens> skips plain and runs the other arms at that budget; budget.json then
   records source "HTSA_FIXED_B".
2. Requested arms. The scaffold runs first (harness.think.think); best-of-N arms then stop at the
   scaffold's realized spend on the same item and replicate (MSR-02). When the scaffold arm was
   requested but that (item, replicate) has no successful scaffold run, the best-of-N run is
   skipped and logged to errors.jsonl (never silently run at B). Without the scaffold arm in
   this call, scaffold runs already in the batch still set the match (an errored one means
   skip); pairs with no scaffold run at all run at B.
3. score.score_batch(batch) -> summary.json and summary.md, then a lint over every rendered
   prompt of the batch's run folders -> results/<batch>/lint.json (hit rate per pattern).
Runs already present in runs.jsonl with a non-error status are reused, so a batch can be
extended arm by arm; errored runs are retried. Reuse is decided after the matched-cost check:
a best-of-N run is reused only when its recorded budget_tokens equals the budget it would get
now, else it is re-run at the new budget (a run made at another B is not matched cost). A run
that raises gets a runs.jsonl row with status "error" (crash true), so it counts wrong and is
retried next time instead of vanishing from the denominator. The row keeps the tokens an
llm.CallError carries; a plain run that raised after spending is a final plain failure instead.

python -m harness.bench --benchmark arc --arm plain,bestofn_vote --split dev-tune --items 10
    --replicates 1 --backend mock --m 20 --batch dev0
"""
from __future__ import annotations

import argparse
import os
import importlib
import statistics
import sys
import threading
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from . import config, data, lint, llm, score
from .arms import run_arm
from .arms.plain import run_id_for
from .schemas import append_jsonl, now_ts, read_json, read_jsonl, strip_key, write_json

ALL_ARMS = ("plain", "bestofn_vote", "bestofn_verify", "seeded_bestofn", "scaffold")
_LOCK = threading.Lock()


# ---------------------------------------------------------------- batch files
def bdir(batch: str) -> Path:
    return Path(config.RESULTS_DIR) / batch


def final_failure(row: dict) -> bool:
    """A plain run that errored after spending tokens (for example the output-token cap): a
    real plain failure, kept as is, never retried (retrying would resample until success)."""
    return (row.get("arm") == "plain" and row.get("status") == "error" and not row.get("crash")
            and int(row.get("spent_tokens") or 0) > 0)


def existing_runs(batch: str, include_errors: bool = False) -> dict[str, dict]:
    """Last runs.jsonl row per run_id; errored runs are left out (so they are retried) unless
    include_errors, except final plain failures (final_failure)."""
    rows = {r["run_id"]: r for r in read_jsonl(bdir(batch) / "runs.jsonl")}
    if include_errors:
        return rows
    return {k: r for k, r in rows.items() if r.get("status") != "error" or final_failure(r)}


def log_crash(batch: str, item: dict, arm: str, replicate: int, run_id: str, err: Exception,
              before: dict | None) -> None:
    """runs.jsonl row with status error for a run that raised, unless the run already wrote an
    error row during this attempt (think() does on its own crashes). The usage an llm.CallError
    carries is the row's spent_tokens; a plain run that raised after spending is a final plain
    failure (crash false), so it is not resampled and enters the cost median (B9). Returns the
    row written, or None."""
    last = existing_runs(batch, include_errors=True).get(run_id)
    if last is not None and last != before and last.get("status") == "error":
        return None
    spent = int(err.usage.total_tokens) if isinstance(err, llm.CallError) else 0
    row = {"batch": batch, "benchmark": item["benchmark"], "item_id": item["id"], "arm": arm,
           "replicate": replicate, "run_id": run_id, "status": "error", "answer": None,
           "spent_tokens": spent, "rounds": 0, "ts": now_ts(), "crash": not (arm == "plain" and spent > 0),
           "error": f"{type(err).__name__}: {str(err)[:800]}"}
    with _LOCK:
        append_jsonl(bdir(batch) / "runs.jsonl", row)
    return row


def log_error(batch: str, run_id: str, err: Exception) -> None:
    with _LOCK:
        append_jsonl(bdir(batch) / "errors.jsonl",
                     {"run_id": run_id, "error": f"{type(err).__name__}: {str(err)[:800]}",
                      "ts": now_ts()})


# ---------------------------------------------------------------- running one (item, arm, replicate)
def run_scaffold(item: dict, *, m: int, replicate: int, backend: str, batch: str) -> dict:
    """Scaffold arm via harness.think.think; adds the runs.jsonl row if think did not."""
    think_mod = importlib.import_module(".think", __package__)
    run_id = run_id_for(batch, item["benchmark"], item["id"], "scaffold", replicate)
    before = existing_runs(batch, include_errors=True).get(run_id)
    ans = think_mod.think(item, m=m, replicate=replicate, backend=backend, batch=batch,
                          arm="scaffold")
    ans = ans.to_dict() if hasattr(ans, "to_dict") else dict(ans)
    if existing_runs(batch, include_errors=True).get(run_id) == before:   # think wrote no row this time
        row = {"batch": batch, "benchmark": item["benchmark"], "item_id": item["id"],
               "arm": "scaffold", "replicate": replicate, "run_id": run_id,
               "status": ans.get("status"), "answer": ans.get("answer"),
               "spent_tokens": ans.get("spent_tokens", 0), "rounds": ans.get("rounds", 0),
               "ts": now_ts()}
        with _LOCK:
            append_jsonl(bdir(batch) / "runs.jsonl", row)
    return existing_runs(batch, include_errors=True).get(run_id, {"spent_tokens": ans.get("spent_tokens", 0)})


SKIP = object()      # budget_of marker: no matched-cost budget, skip this run


def run_one(arm: str, item: dict, *, m: int, replicate: int, backend: str, batch: str,
            budget: int | None, done: dict[str, dict]) -> dict | None:
    """Run (or reuse) one run; returns its runs.jsonl row, or None on failure or skip. The
    matched-cost check comes first: a skip is never covered by an old run, and a done run is
    reused only at the same budget."""
    item = strip_key(item)
    run_id = run_id_for(batch, item["benchmark"], item["id"], arm, replicate)
    if budget is SKIP:
        log_error(batch, run_id, RuntimeError("skipped: no successful scaffold run to match cost "
                                              "(scaffold arm requested)"))
        print(f"[bench] {run_id} skipped: no scaffold spend to match", file=sys.stderr)
        return None
    if run_id in done:
        old = done[run_id]
        if budget is None or old.get("budget_tokens") == budget:
            return old
        print(f"[bench] {run_id} re-run: recorded budget {old.get('budget_tokens')} != {budget}",
              file=sys.stderr)
    before = existing_runs(batch, include_errors=True).get(run_id)
    try:
        if arm == "scaffold":
            return run_scaffold(item, m=m, replicate=replicate, backend=backend, batch=batch)
        ans = run_arm(arm, item, m=m, replicate=replicate, backend=backend, batch=batch,
                      budget_tokens=budget)
        row = existing_runs(batch, include_errors=True).get(run_id)
        if row is None:
            row = {"run_id": run_id, "spent_tokens": ans.spent_tokens, "status": ans.status}
        if row.get("status") == "error":
            log_error(batch, run_id, RuntimeError(f"run errored: {row.get('error') or ans.reason}"))
            return row if final_failure(row) else None
        return row
    except Exception as e:  # noqa: BLE001 - one failed run must not stop the batch
        log_error(batch, run_id, e)
        row = log_crash(batch, item, arm, replicate, run_id, e, before)
        print(f"[bench] {run_id} failed: {e}", file=sys.stderr)
        return row if row is not None and final_failure(row) else None


def run_arm_over(arm: str, items: list[dict], *, replicates: int, m: int, backend: str,
                 batch: str, budget_of, workers: int) -> dict[tuple[str, int], dict]:
    """One arm over items x replicates; budget_of(item_id, replicate) gives budget_tokens."""
    done = existing_runs(batch)
    jobs = [(it, r) for it in items for r in range(replicates)]

    def job(pair):
        it, r = pair
        return (it["id"], r), run_one(arm, it, m=m, replicate=r, backend=backend, batch=batch,
                                      budget=budget_of(it["id"], r), done=done)

    with ThreadPoolExecutor(max_workers=max(1, workers)) as ex:
        return {k: v for k, v in ex.map(job, jobs) if v is not None}


# ---------------------------------------------------------------- cost measurement (step 1)
def _cost_key(r: dict) -> tuple:
    return (r["benchmark"], r["backend"], r.get("model"), r["item_id"], r["replicate"])


def write_cost(batch: str, benchmark: str, backend: str, plain: dict[tuple[str, int], dict],
               splits: set[str] | None = None) -> list[int]:
    """Append cost.jsonl rows (plan.md s10 schema) for plain runs that spent tokens and are not
    yet recorded, failed runs that spent tokens included; return the token counts of the
    recorded rows of this benchmark, backend and model whose item lies in `splits` (the splits
    of this call's items; None = any), so rows of another split or model are not pooled."""
    path = bdir(batch) / "cost.jsonl"
    model = config.DEFAULT_MODEL
    seen = {_cost_key(r) for r in read_jsonl(path)}
    new = []
    for (item_id, rep), row in sorted(plain.items()):
        if int(row.get("spent_tokens") or 0) <= 0:
            continue
        rec = {"benchmark": benchmark, "backend": backend, "model": model,
               "item_id": item_id, "replicate": rep, "tokens": int(row["spent_tokens"])}
        if _cost_key(rec) not in seen:
            new.append(rec)
    if new:
        append_jsonl(path, new)
    split_of = ({it["id"]: it.get("split") for it in data.load_items(benchmark)}
                if splits is not None else {})
    return [int(r["tokens"]) for r in read_jsonl(path)
            if r["benchmark"] == benchmark and r["backend"] == backend
            and r.get("model", model) == model
            and (splits is None or split_of.get(r["item_id"]) in splits)
            and int(r.get("tokens") or 0) > 0]


def _prior_cot(budget_from: str | None, benchmark: str, backend: str):
    """cot_median of --budget-from for this benchmark and backend, or None when it has none."""
    if not budget_from:
        return None
    prior = (read_json(bdir(budget_from) / "budget.json", {}) or {}).get(benchmark, {})
    return (prior.get(backend) or {}).get("cot_median")


def set_budget(batch: str, benchmark: str, backend: str, m: int, tokens: list[int],
               budget_from: str | None, split: str | None = None, n_failed: int = 0) -> dict:
    """B = max(m x median plain-CoT tokens per item, HTSA_MIN_B) (section 8 Cost); written to
    budget.json with the floor (min_B), the unfloored value, the split and the number of failed
    plain runs that entered the median (n_failed)."""
    src = "this batch"
    cot = statistics.median(tokens) if tokens else None
    prior_cot = _prior_cot(budget_from, benchmark, backend)
    if prior_cot:                      # a prior batch without a measured median (HTSA_FIXED_B) is no source
        cot, src = prior_cot, f"batch {budget_from}"
    if not cot:
        raise SystemExit(f"[bench] no successful plain-CoT run for {benchmark}/{backend} in batch "
                         f"{batch} and no --budget-from: cannot set B (see errors.jsonl)")
    min_b = int(os.environ.get("HTSA_MIN_B", "0") or 0)    # floor so setup cannot eat the budget
    rec = {"benchmark": benchmark, "backend": backend, "model": config.DEFAULT_MODEL,
           "cot_median": cot, "m": m, "B": max(int(round(m * cot)), min_b),
           "B_unfloored": int(round(m * cot)), "min_B": min_b, "split": split,
           "n": len(tokens), "n_failed": n_failed, "source": src, "ts": now_ts()}
    path = bdir(batch) / "budget.json"
    with _LOCK:
        allb = read_json(path, {}) or {}
        allb.setdefault(benchmark, {})[backend] = rec
        write_json(path, allb)
    return rec


# ---------------------------------------------------------------- CLI
def parse_args(argv: list[str] | None) -> argparse.Namespace:
    ap = argparse.ArgumentParser(description="HTSA measurement harness (plain cost first, then arms).")
    ap.add_argument("--benchmark", required=True, choices=sorted(config.BENCHMARKS))
    ap.add_argument("--arm", action="append", default=None, metavar="ARM",
                    help="repeatable or comma-separated: " + ",".join(ALL_ARMS)
                         + " (plain always runs)")
    ap.add_argument("--split", default="dev-tune", choices=list(data.SPLIT_NAMES))
    ap.add_argument("--items", type=int, default=None, help="first N items of the split")
    ap.add_argument("--item-ids", default=None, help="comma-separated item ids (overrides --items)")
    ap.add_argument("--replicates", type=int, default=1)
    ap.add_argument("--backend", default=None, choices=sorted(config.MODEL_IDS))
    ap.add_argument("--m", type=int, default=config.PARAMS["m"])
    ap.add_argument("--batch", required=True)
    ap.add_argument("--budget-from", default=None, help="take cot_median from this batch")
    ap.add_argument("--null-from", default=None,
                    help="dev-tune batch that fixes the primary null for scoring (plan.md s5)")
    ap.add_argument("--workers", type=int, default=2, help="concurrent runs per arm")
    args = ap.parse_args(argv)
    args.arms = [a.strip() for chunk in (args.arm or ["plain"]) for a in chunk.split(",") if a.strip()]
    args.arm = ",".join(args.arms)
    bad = [a for a in args.arms if a not in ALL_ARMS]
    if bad:
        ap.error(f"unknown arm(s) {bad}")
    args.backend = args.backend or config.default_backend()
    return args


def choose_items(args) -> list[dict]:
    items = data.load_items(args.benchmark, args.split)
    if args.item_ids:
        want = [s.strip() for s in args.item_ids.split(",") if s.strip()]
        by_id = {it["id"]: it for it in data.load_items(args.benchmark)}
        chosen = [by_id[i] for i in want]
        other = [it["id"] for it in chosen if it.get("split") != args.split]
        if other:                      # --item-ids searches every split, test included
            print(f"[bench] warning: {len(other)} of {len(chosen)} --item-ids are not in split "
                  f"{args.split} (first: {', '.join(other[:3])}; splits "
                  f"{sorted({str(by_id[i].get('split')) for i in other})})", file=sys.stderr)
        return chosen
    return items[: args.items] if args.items else items


def lint_batch_prompts(batch: str) -> dict:
    """Section 3: lint every rendered prompt of the batch's run folders after the batch;
    writes results/<batch>/lint.json with the per-pattern hit rate over prompts."""
    prompts = sorted(Path(config.RUNS_DIR).glob(f"{batch}__*/prompts/*.txt"))
    hits: dict[str, int] = {}
    n_hit, n_fail_hit = 0, 0
    for p in prompts:
        found = lint.lint_text(p.read_text(encoding="utf-8"))
        if found:
            n_hit += 1
        if any(f["severity"] == "fail" for f in found):
            n_fail_hit += 1
        for f in found:
            hits[f["pattern"]] = hits.get(f["pattern"], 0) + 1
    res = {"batch": batch, "n_prompts": len(prompts), "n_prompts_with_hits": n_hit,
           "n_prompts_with_fail_hits": n_fail_hit,
           "hit_rate": (n_hit / len(prompts)) if prompts else 0.0,
           "fail_hit_rate": (n_fail_hit / len(prompts)) if prompts else 0.0,
           "hits_per_pattern": dict(sorted(hits.items())), "ts": now_ts()}
    write_json(bdir(batch) / "lint.json", res)
    return res


def run_bench(args) -> dict:
    """Section 3 /bench: template lint, plain cost first, scaffold, best-of-N at matched spend,
    then score and the rendered-prompt lint."""
    tl = lint.lint_templates()
    if tl["fails"]:
        raise SystemExit("[bench] template lint failed, batch not started: "
                         + "; ".join(f"{f['file']}:{f['pattern']}" for f in tl["fails"]))
    items = [strip_key(it) for it in choose_items(args)]
    common = dict(replicates=args.replicates, m=args.m, backend=args.backend, batch=args.batch,
                  workers=args.workers)
    write_json(bdir(args.batch) / f"config_{args.benchmark}.json",
               {k: v for k, v in vars(args).items()} | {"item_ids": [it["id"] for it in items]})
    if os.environ.get("HTSA_FIXED_B"):            # method only, at a fixed budget; plain is measured in another batch
        plain = {}
        budget = {"benchmark": args.benchmark, "backend": args.backend, "model": config.DEFAULT_MODEL,
                  "B": int(os.environ["HTSA_FIXED_B"]), "cot_median": None, "m": args.m,
                  "source": "HTSA_FIXED_B", "ts": now_ts()}
        with _LOCK:
            allb = read_json(bdir(args.batch) / "budget.json", {}) or {}
            allb.setdefault(args.benchmark, {})[args.backend] = budget
            write_json(bdir(args.batch) / "budget.json", allb)
    else:
        plain = run_arm_over("plain", items, budget_of=lambda i, r: None, **common)
        splits = {it.get("split") for it in items}
        tokens = write_cost(args.batch, args.benchmark, args.backend, plain, splits)
        if not any(not final_failure(r) and int(r.get("spent_tokens") or 0) > 0 for r in plain.values()) and not _prior_cot(args.budget_from, args.benchmark, args.backend):
            raise SystemExit(f"[bench] no successful plain-CoT run for {args.benchmark}/{args.backend} in batch "
                             f"{args.batch} and no --budget-from: cannot set B (failed runs join the median only "
                             "next to successes; see errors.jsonl)")
        budget = set_budget(args.batch, args.benchmark, args.backend, args.m, tokens, args.budget_from,
                            ",".join(sorted(s for s in splits if s)),
                            sum(1 for r in plain.values() if final_failure(r)))
    print(f"[bench] {args.benchmark}: cot_median {budget['cot_median']} -> B {budget['B']}")
    scaffold = {}
    if "scaffold" in args.arms:
        scaffold = run_arm_over("scaffold", items, budget_of=lambda i, r: None, **common)
    else:                                # scaffold runs already in the batch still set the match
        scaffold = {(r["item_id"], int(r.get("replicate", 0))): r
                    for r in existing_runs(args.batch, include_errors=True).values()
                    if r.get("arm") == "scaffold" and r.get("benchmark") == args.benchmark}

    def budget_of(item_id: str, rep: int):
        s = scaffold.get((item_id, rep))
        if s and s.get("status") != "error" and s.get("spent_tokens"):
            return int(s["spent_tokens"])
        if "scaffold" not in args.arms and (item_id, rep) not in scaffold:
            return budget["B"]           # no scaffold in this batch for the pair: run at B
        return SKIP                      # never fall back to B silently (matched cost, MSR-02)

    for arm in args.arms:
        if arm not in ("plain", "scaffold"):
            run_arm_over(arm, items, budget_of=budget_of, **common)
    summary = score.score_batch(args.batch, getattr(args, "null_from", None))
    res = lint_batch_prompts(args.batch)
    print(f"[bench] prompt lint: {res['n_prompts']} prompts, fail-pattern hit rate "
          f"{res['fail_hit_rate']:.3f} -> {bdir(args.batch) / 'lint.json'}")
    return summary


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    run_bench(args)
    md = bdir(args.batch) / "summary.md"
    print(md.read_text(encoding="utf-8"))
    print(f"[bench] wrote {md}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
