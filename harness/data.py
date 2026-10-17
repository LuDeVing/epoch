"""Benchmark item files for the HTSA harness (ARCHITECTURE.md section 8, Benchmarks and Splits;
section 9 step 1).

Builds two item files under config.DATA_DIR from the raw downloads:
- arc_agi1_eval_le600.jsonl: 40 ARC-AGI-1 evaluation tasks with <= 600 cells in total and exactly
  one test pair (sorted by file name, shuffled with the seed, first 40).
- brainteaser_sp.jsonl: 120 BRAINTEASER rows. Rows come in groups (original, _SR semantic
  reconstruction, _CR context reconstruction); whole groups are sampled and split together so a
  reconstruction variant never lands in a different split from its original.

Splits: dev-tune 40%, dev-ablate 30%, test 30%, assigned by a fixed seed over units (ARC task,
BRAINTEASER group). Item files carry the key fields; only score.py reads them, every other module
works on schemas.strip_key(item).
CLI: python -m harness.data [--seed 7]
"""
from __future__ import annotations

import argparse
import ast
import json
import random
import sys
from pathlib import Path

from . import config
from .schemas import read_jsonl, write_json

ARC_N = 40
BT_N = 120
ARC_MAX_CELLS = 600
SPLITS = (("dev-tune", 0.4), ("dev-ablate", 0.3), ("test", 0.3))
SPLIT_NAMES = tuple(s for s, _ in SPLITS)
# Splits whose ledger rows may build memory views (stats.rebuild). ARCHITECTURE section 8 names a
# train split that writes views only; P0 has none, so dev-tune (the tuning split) stands in.
# dev-ablate and test are held out: they never build views (MSR-11), and think refuses a
# snapshot whose splits include the item's own split (Pr11).
TRAIN_SPLITS = ("train", "dev-tune")


# ---------------------------------------------------------------- paths (read config at call time)
def item_path(benchmark: str) -> Path:
    """Item file for a benchmark; the name comes from config.BENCHMARKS, the folder from DATA_DIR."""
    return Path(config.DATA_DIR) / Path(config.BENCHMARKS[benchmark]["file"]).name


def raw_arc_dir() -> Path:
    return Path(config.RAW_DATA_DIR) / "arc" / "ARC-AGI-master" / "data" / "evaluation"


def raw_arc2_dir() -> Path:
    return Path(config.RAW_DATA_DIR) / "arc2" / "ARC-AGI-2-main" / "data" / "evaluation"


ARC2_MAX_CELLS = 2400   # ARC-AGI-2 eval: 41 tasks have <= 2400 cells and one test pair
ARC2_N = 41


def raw_bt_path() -> Path:
    return Path(config.RAW_DATA_DIR) / "brainteaser" / "SP.jsonl"


# ---------------------------------------------------------------- splits
def assign_splits(units: list[str], seed: int, tag: str) -> dict[str, str]:
    """Section 8 Splits: dev-tune 40%, dev-ablate 30%, test 30% by a fixed seed over units."""
    order = sorted(units)
    random.Random(f"split:{tag}:{seed}").shuffle(order)
    n = len(order)
    n_tune = round(n * SPLITS[0][1])
    n_ablate = round(n * SPLITS[1][1])
    out = {}
    for i, u in enumerate(order):
        out[u] = "dev-tune" if i < n_tune else ("dev-ablate" if i < n_tune + n_ablate else "test")
    return out


# ---------------------------------------------------------------- ARC
def _cells(grid) -> int:
    return sum(len(row) for row in grid)


def arc_total_cells(task: dict) -> int:
    """All cells of all train inputs/outputs plus the test input/output."""
    n = 0
    for pair in task.get("train", []) + task.get("test", []):
        n += _cells(pair.get("input", [])) + _cells(pair.get("output", []))
    return n


def select_arc(arc_dir: Path, seed: int, n: int = ARC_N, max_cells: int = ARC_MAX_CELLS,
               tag: str = "arc") -> list[dict]:
    """Section 8 Benchmarks: ARC subset with <= max_cells cells and exactly one test pair.
    tag keys the split assignment (arc = ARC-AGI-1 <= 600 cells; arc2 = ARC-AGI-2 <= 2400)."""
    files = sorted(Path(arc_dir).glob("*.json"), key=lambda p: p.name)
    eligible = []
    for f in files:
        task = json.loads(f.read_text(encoding="utf-8"))
        if len(task.get("test", [])) == 1 and arc_total_cells(task) <= max_cells:
            eligible.append((f.stem, task))
    random.Random(seed).shuffle(eligible)
    chosen = eligible[:n]
    if len(chosen) < n:
        print(f"[data] warning: only {len(chosen)} eligible ARC tasks (wanted {n})", file=sys.stderr)
    splits = assign_splits([stem for stem, _ in chosen], seed, tag)
    items = []
    for stem, task in chosen:
        test = task["test"][0]
        items.append({"id": stem, "benchmark": "arc", "train": task["train"],
                      "test_input": test["input"], "test_output": test["output"],
                      "family": "arc", "split": splits[stem], "group": stem})
    return items


# ---------------------------------------------------------------- BRAINTEASER
def bt_group(row_id: str) -> str:
    """'SP-12_SR' -> 'SP-12'; reconstruction variants share the group of their original."""
    return row_id.split("_")[0]


def bt_family(row_id: str) -> str:
    """bt_sp for sentence puzzles, bt_wp for word puzzles (taken from the row id prefix)."""
    prefix = row_id.split("-")[0].lower()
    return f"bt_{prefix}" if prefix in ("sp", "wp") else "bt_sp"


def bt_item(row: dict, split: str) -> dict:
    """Choices in the row's choice_list order; label = index of the correct choice in that list."""
    raw = row["choice_list"]
    choices = list(ast.literal_eval(raw)) if isinstance(raw, str) else list(raw)
    label = int(row["label"])
    if len(choices) != 4 or not 0 <= label < 4:
        raise ValueError(f"bad BRAINTEASER row {row.get('id')}")
    rid = str(row["id"])
    return {"id": rid, "benchmark": "bt", "question": row["question"], "choices": choices,
            "label": label, "family": bt_family(rid), "split": split, "group": bt_group(rid)}


def select_bt(bt_path: Path, seed: int, n: int = BT_N) -> list[dict]:
    """Sample whole groups with the seed until n rows are reached; split by group."""
    rows = read_jsonl(bt_path)
    groups: dict[str, list[dict]] = {}
    for r in rows:
        groups.setdefault(bt_group(str(r["id"])), []).append(r)
    names = sorted(groups)
    random.Random(seed).shuffle(names)
    chosen, total = [], 0
    for g in names:
        if total >= n:
            break
        chosen.append(g)
        total += len(groups[g])
    splits = assign_splits(chosen, seed, "bt")
    items = [bt_item(r, splits[g]) for g in chosen for r in groups[g]][:n]
    if len(items) != n:
        print(f"[data] warning: BRAINTEASER selection has {len(items)} rows (wanted {n})",
              file=sys.stderr)
    if items and all(it["family"] != "bt_sp" for it in items):
        print("[data] warning: the BRAINTEASER file holds no SP rows (check the raw download)",
              file=sys.stderr)
    return items


# ---------------------------------------------------------------- build / load
def _write_items(path: Path, items: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        for it in items:
            f.write(json.dumps(it, ensure_ascii=True) + "\n")


def _counts(items: list[dict]) -> dict:
    out = {s: 0 for s in SPLIT_NAMES}
    for it in items:
        out[it["split"]] = out.get(it["split"], 0) + 1
    out["total"] = len(items)
    return out


def build_items(seed: int = 7, arc_dir: Path | None = None, bt_path: Path | None = None) -> dict:
    """Write both item files; return counts per split (section 9 step 1)."""
    arc = select_arc(Path(arc_dir) if arc_dir else raw_arc_dir(), seed)
    bt = select_bt(Path(bt_path) if bt_path else raw_bt_path(), seed)
    _write_items(Path(config.DATA_DIR) / config.ARC_FILES["arc1"].name, arc)
    _write_items(item_path("bt"), bt)
    counts = {"seed": seed, "arc": _counts(arc), "bt": _counts(bt),
              "bt_families": sorted({it["family"] for it in bt})}
    arc2_dir = raw_arc2_dir()
    if arc2_dir.exists():          # ARC-AGI-2 eval subset (the gate set; see config.ARC_SET)
        arc2 = select_arc(arc2_dir, seed, n=ARC2_N, max_cells=ARC2_MAX_CELLS, tag="arc2")
        _write_items(Path(config.DATA_DIR) / config.ARC_FILES["arc2"].name, arc2)
        counts["arc2"] = _counts(arc2)
    elif not item_path("arc").exists():
        # no ARC-AGI-2 raw data on this machine: the configured 'arc' file falls back to the
        # ARC-1 selection so load_items('arc') is never empty (warned, never silent)
        print("[data] warning: ARC-AGI-2 raw data missing; 'arc' falls back to the ARC-1 subset",
              file=sys.stderr)
        _write_items(item_path("arc"), arc)
    write_json(Path(config.DATA_DIR) / "items_manifest.json", counts)
    _CACHE.clear()
    return counts


_CACHE: dict[str, list[dict]] = {}


def _all_items(benchmark: str) -> list[dict]:
    path = item_path(benchmark)
    key = f"{benchmark}:{path}"
    if key not in _CACHE:
        if not path.exists():
            build_items()
        _CACHE[key] = read_jsonl(path)
    return _CACHE[key]


def load_items(benchmark: str, split: str | None = None) -> list[dict]:
    """Items of one benchmark (with keys; callers other than score.py must strip_key)."""
    if benchmark not in config.BENCHMARKS:
        raise ValueError(f"unknown benchmark {benchmark}")
    items = _all_items(benchmark)
    if split is not None:
        if split not in SPLIT_NAMES:
            raise ValueError(f"unknown split {split}")
        items = [it for it in items if it["split"] == split]
    return [dict(it) for it in items]


def get_item(benchmark: str, item_id: str) -> dict:
    for it in _all_items(benchmark):
        if it["id"] == item_id:
            return dict(it)
    raise KeyError(f"{benchmark} item {item_id} not found")


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Build the HTSA benchmark item files.")
    ap.add_argument("--seed", type=int, default=7)
    args = ap.parse_args(argv)
    print(json.dumps(build_items(args.seed), indent=1))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
