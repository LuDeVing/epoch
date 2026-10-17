"""Promote a verified winner to be the new baseline, so winners compound across runs.

What happens:
  1. the current nano/train.py is archived as nano/baselines/train_<old version>.py
  2. the candidate's script becomes nano/train.py
  3. nano/baselines/VERSION is bumped (v1 -> v2 ...) and BASELINES.md gets the record: date, run,
     candidate, hypothesis, the verdict numbers, the source hash
  4. the baseline profile is removed so the next run rebuilds it (curves, noise, timing); the shared
     full-run baseline seeds of the old version stay where they are, the new version gets its own folder
Every later verdict is recorded against the new version (nano/version.py); the ledger and the hash
memory keep the version with each entry, so nothing from the old recipe is mistaken for the new.

Promotion is manual on purpose (autoresearch's keep rule with the simplicity judgement left to the
human): a verified status is required unless --force is given.

Usage: python -m nano.promote --run D:/AGI-lab/runs/<run> --cand <id> [--force] [--note "..."]
"""
from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LAB = Path(os.environ.get("HTSA_LAB_ROOT", r"D:\AGI-lab"))
TRAIN = ROOT / "nano" / "train.py"
BASELINES = ROOT / "nano" / "baselines"
VERSION_FILE = BASELINES / "VERSION"
PROFILE_DIR = LAB / "runs" / "nano_baseline_profile"


def bump(v: str) -> str:
    m = re.match(r"v(\d+)$", v.strip())
    return f"v{int(m.group(1)) + 1}" if m else v.strip() + "_next"


def main() -> int:
    from nano.version import baseline_version
    ap = argparse.ArgumentParser()
    ap.add_argument("--run", required=True)
    ap.add_argument("--cand", required=True)
    ap.add_argument("--force", action="store_true", help="promote without a verified verdict")
    ap.add_argument("--note", default="")
    a = ap.parse_args()
    run = Path(a.run)
    src = run / "pool" / f"{a.cand}.py"
    meta_p = run / "pool" / f"{a.cand}.json"
    if not src.exists():
        print(f"no pool/{a.cand}.py in {run}")
        return 2
    meta = json.loads(meta_p.read_text(encoding="utf-8")) if meta_p.exists() else {}
    results = {}
    rp = run / "rung5" / "results.json"
    if rp.exists():
        results = json.loads(rp.read_text(encoding="utf-8")).get("candidates", {}).get(a.cand, {})
    if results.get("status") != "verified" and not a.force:
        print(f"{a.cand} is '{results.get('status', 'not examined')}', not verified; use --force to promote anyway")
        return 3
    old = baseline_version()
    if meta.get("baseline_version", old) != old:
        print(f"{a.cand} was built against baseline {meta.get('baseline_version')}, the current one is {old}; refusing")
        return 4
    new = bump(old)
    BASELINES.mkdir(parents=True, exist_ok=True)
    archive = BASELINES / f"train_{old}.py"
    if not archive.exists():
        shutil.copyfile(TRAIN, archive)
    shutil.copyfile(src, TRAIN)
    VERSION_FILE.write_text(new + "\n", encoding="utf-8")
    rec = {"ts": time.strftime("%Y-%m-%dT%H:%M:%S"), "from": old, "to": new, "run": run.name, "cand": a.cand,
           "hypothesis": meta.get("hypothesis"), "change": meta.get("change"), "src_hash": meta.get("src_hash"),
           "verdict": {k: results.get(k) for k in ("status", "n", "mean", "delta", "p", "gain")}, "note": a.note}
    md = BASELINES / "BASELINES.md"
    if not md.exists():
        md.write_text("# Baseline history\n\nEach promotion: the candidate that became the new baseline and the verdict it won on.\n\n", encoding="utf-8")
    with md.open("a", encoding="utf-8") as f:
        f.write(f"## {new} ({rec['ts']}) from {old}\n\n- run: {run.name}, candidate {a.cand}, source hash {meta.get('src_hash')}\n"
                f"- hypothesis: {meta.get('hypothesis')}\n- change: {meta.get('change')}\n"
                f"- verdict: {json.dumps(rec['verdict'])}\n" + (f"- note: {a.note}\n" if a.note else "") + "\n")
    with (BASELINES / "promotions.jsonl").open("a", encoding="utf-8") as f:
        f.write(json.dumps(rec) + "\n")
    if PROFILE_DIR.exists():
        shutil.rmtree(PROFILE_DIR, ignore_errors=True)
    print(f"promoted {a.cand} -> nano/train.py; baseline {old} -> {new}; old script archived at {archive}; profile cleared")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
