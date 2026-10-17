"""Calibrate the selection weights from the record: which features of an idea cluster predicted that
its build survived the ladder (checked) and the overnight verdict (verified)?

Reads every run folder under the lab's runs/ (idea_clusters.json, cands/, verify.jsonl, rung5/),
joins built candidates to their clusters, and reports survival rates per feature bucket with
counts, plus suggested weights (scaled log-odds relative to the base rate). Nothing is changed
automatically: the owner decides whether to pass the suggestions to the loop (ideate.WEIGHTS).

Usage: python -m nano.calibrate [--runs-dir D:/AGI-lab/runs] [--min-n 5]
"""
from __future__ import annotations

import argparse
import json
import math
import os
from collections import defaultdict
from pathlib import Path
from harness import labroot as _labroot  # noqa: E402  (the lab folder, on any computer)

LAB = _labroot.lab_root()


def _json(p: Path, default):
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except Exception:  # noqa: BLE001
        return default


def _jsonl(p: Path) -> list[dict]:
    if not p.exists():
        return []
    out = []
    for line in p.read_text(encoding="utf-8").splitlines():
        try:
            out.append(json.loads(line))
        except Exception:  # noqa: BLE001
            pass
    return out


def _departure_cards() -> tuple:
    try:
        from nano import ideate
        return tuple(ideate.DEPARTURE_CARDS)
    except Exception:  # noqa: BLE001
        return ("transform", "docs", "low_prior", "research", "deepen", "analogy", "diagnosis", "adapt", "contradiction")


def rows_for(run: Path) -> list[dict]:
    clusters = _json(run / "idea_clusters.json", {}).get("clusters", [])
    by_name = {c.get("name"): c for c in clusters}
    verify = {v["id"]: v for v in _jsonl(run / "verify.jsonl")}
    rung5 = _json(run / "rung5" / "results.json", {}).get("candidates", {})
    out = []
    for f in (run / "cands").glob("*.jsonl") if (run / "cands").exists() else []:
        for r in _jsonl(f):
            if not r.get("id"):
                continue
            ex = r.get("extra") or {}
            cl = by_name.get(ex.get("cluster"))
            if not cl:
                continue
            v = verify.get(r["id"], {})
            out.append({"run": run.name, "id": r["id"], "n_angles": cl.get("n_angles", len(cl.get("cards", []))),
                        "prior": cl.get("prior", "unknown"), "obvious": bool(cl.get("obvious")),
                        "departure": any(x in cl.get("cards", []) for x in _departure_cards()),
                        "n": cl.get("n", 1), "cards": cl.get("cards", []),
                        "checked": v.get("status") == "checked",
                        "verified": rung5.get(r["id"], {}).get("status") == "verified",
                        "examined": r["id"] in rung5})
    return out


def suggest_weights(runs_dir: Path | None = None, min_rows: int = 100, include_mock: bool = False) -> dict | None:
    """Selection weights as log-odds of surviving the ladder relative to the base rate, per feature.
    None when fewer than min_rows built candidates with cluster records exist."""
    runs_dir = runs_dir or (LAB / "runs")
    rows = []
    for run in sorted(Path(runs_dir).glob("*__nano__*")):
        if not include_mock and run.name.startswith("mock"):
            continue
        rows += rows_for(run)
    if len(rows) < min_rows:
        return None
    base = sum(r["checked"] for r in rows) / len(rows)

    from nano import ideate as _ideate
    prior = dict(_ideate.WEIGHTS)

    def lo(sub, key=None):
        if len(sub) < 5:
            return prior.get(key, 0.0)                 # too few rows: keep the hand-set prior, do not zero it
        p = sum(r["checked"] for r in sub) / len(sub)
        p, b = min(max(p, 0.02), 0.98), min(max(base, 0.02), 0.98)
        return round(math.log(p / (1 - p)) - math.log(b / (1 - b)), 3)
    w = {"angle": lo([r for r in rows if r["n_angles"] >= 2], "angle"),
         "new": lo([r for r in rows if r["prior"] == "new"], "new"),
         "known": lo([r for r in rows if r["prior"] == "known"], "known"),
         "failed": min(lo([r for r in rows if r["prior"] == "failed"], "failed"), -2.0),
         "obvious": lo([r for r in rows if r["obvious"]], "obvious"),
         "departure": lo([r for r in rows if r["departure"]], "departure"),
         "cheap": 0.0, "size": -0.05, "metric_blind": -1.0}
    return {"n": len(rows), "base_rate": round(base, 3), "weights": w}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--runs-dir", default=str(LAB / "runs"))
    ap.add_argument("--min-n", type=int, default=5)
    ap.add_argument("--include-mock", action="store_true")
    a = ap.parse_args()
    rows = []
    for run in sorted(Path(a.runs_dir).glob("*__nano__*")):
        if not a.include_mock and run.name.startswith("mock"):
            continue
        rows += rows_for(run)
    if not rows:
        print("no built candidates with cluster records found")
        return 0
    print(f"{len(rows)} built candidates from {len({r['run'] for r in rows})} runs; "
          f"{sum(r['checked'] for r in rows)} checked; {sum(r['examined'] for r in rows)} examined overnight; {sum(r['verified'] for r in rows)} verified")

    def buckets(key, fn):
        groups = defaultdict(list)
        for r in rows:
            groups[fn(r)].append(r)
        return key, groups
    feats = [buckets("angles", lambda r: str(min(r["n_angles"], 3)) + ("+" if r["n_angles"] >= 3 else "")),
             buckets("prior", lambda r: r["prior"]), buckets("obvious", lambda r: str(r["obvious"])),
             buckets("departure", lambda r: str(r["departure"])), buckets("size", lambda r: "1" if r["n"] == 1 else ("2-3" if r["n"] <= 3 else "4+"))]
    base_checked = sum(r["checked"] for r in rows) / len(rows)
    examined = [r for r in rows if r["examined"]]
    base_verified = (sum(r["verified"] for r in examined) / len(examined)) if examined else None

    def lo(p, base):
        p, base = min(max(p, 0.02), 0.98), min(max(base, 0.02), 0.98)
        return math.log(p / (1 - p)) - math.log(base / (1 - base))
    print("\n| feature | bucket | n | checked rate | verified rate (examined) | suggested weight delta (checked) |")
    print("|---|---|---|---|---|---|")
    for key, groups in feats:
        for b, rs in sorted(groups.items()):
            n = len(rs)
            cr = sum(r["checked"] for r in rs) / n
            ex = [r for r in rs if r["examined"]]
            vr = (sum(r["verified"] for r in ex) / len(ex)) if ex else None
            w = lo(cr, base_checked) if n >= a.min_n else None
            print(f"| {key} | {b} | {n} | {cr:.2f} | {('%.2f (%d)' % (vr, len(ex))) if vr is not None else '-'} | {('%+.2f' % w) if w is not None else 'too few'} |")
    print(f"\nbase rates: checked {base_checked:.2f}" + (f", verified {base_verified:.2f}" if base_verified is not None else ""))
    print("Weights are log-odds relative to the base rate; a bucket with too few builds gets none. Apply by hand via ideate.WEIGHTS.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
