"""Shared record schemas and JSON helpers for the HTSA harness.

Every module reads and writes the records defined here. Fields follow ARCHITECTURE.md
section 2 (workspace layout) and section 3 (/ledger). Keep records flat and JSON-friendly.
"""
from __future__ import annotations

import json
import sys
import threading
import time
import uuid
from dataclasses import dataclass, field, asdict
from pathlib import Path
from typing import Any, Iterable, Iterator

# One process-wide lock for every JSONL append: on Windows O_APPEND is a seek-then-write per
# handle, so unlocked concurrent appends from the driver's card threads tear lines.
_APPEND_LOCK = threading.Lock()


# ---------------------------------------------------------------- ids and time
def new_id(prefix: str = "") -> str:
    return f"{prefix}{uuid.uuid4().hex[:10]}"


def now_ts() -> str:
    return time.strftime("%Y-%m-%dT%H:%M:%S", time.localtime())


# ---------------------------------------------------------------- json helpers
def read_json(path: Path, default: Any = None) -> Any:
    path = Path(path)
    if not path.exists():
        return default
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, obj: Any) -> None:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=1), encoding="utf-8")


def append_jsonl(path: Path, row: dict | Iterable[dict]) -> None:
    """Append rows as complete lines under one lock and one write() call, so concurrent
    writers in this process never interleave partial lines (serialized before the file is
    opened; a row that cannot be serialized never leaves a partial line behind)."""
    path = Path(path)
    rows = [row] if isinstance(row, dict) else list(row)
    if not rows:
        return
    blob = "".join(json.dumps(r, ensure_ascii=False) + "\n" for r in rows)
    with _APPEND_LOCK:
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("a", encoding="utf-8") as f:
            f.write(blob)
            f.flush()


def read_jsonl(path: Path, strict: bool = False) -> list[dict]:
    """Rows of a JSONL file. A line that does not decode (a torn write from another process)
    is skipped with a warning on stderr unless strict=True, so one bad line never takes a
    whole batch down with it."""
    path = Path(path)
    if not path.exists():
        return []
    out = []
    with path.open("r", encoding="utf-8") as f:
        for n, line in enumerate(f, 1):
            line = line.strip()
            if not line:
                continue
            try:
                out.append(json.loads(line))
            except json.JSONDecodeError as e:
                if strict:
                    raise
                print(f"[schemas] skipping undecodable line {n} of {path}: {e}", file=sys.stderr)
    return out


def iter_jsonl(path: Path) -> Iterator[dict]:
    yield from read_jsonl(path)


# ---------------------------------------------------------------- usage and cost
@dataclass
class Usage:
    input_tokens: int = 0
    output_tokens: int = 0
    cache_read_input_tokens: int = 0
    cache_creation_input_tokens: int = 0

    @property
    def total_tokens(self) -> int:
        """Cost unit: input + cached input (at full price) + output (section 8, Cost)."""
        return (self.input_tokens + self.cache_read_input_tokens
                + self.cache_creation_input_tokens + self.output_tokens)

    def add(self, other: "Usage") -> "Usage":
        return Usage(self.input_tokens + other.input_tokens,
                     self.output_tokens + other.output_tokens,
                     self.cache_read_input_tokens + other.cache_read_input_tokens,
                     self.cache_creation_input_tokens + other.cache_creation_input_tokens)

    def to_dict(self) -> dict:
        d = asdict(self)
        d["total_tokens"] = self.total_tokens
        return d


# ---------------------------------------------------------------- records
@dataclass
class Candidate:
    """One row of runs/<id>/cands/<call>.jsonl."""
    id: str
    text: str                      # the candidate as the generator wrote it (post-check applied)
    card: str                      # seeded | low_prior | transform | formal | revise | plain | bestofn | probe
    operator: str                  # card operator, e.g. "none", "drop", "fix"
    seed: str                      # seed id or "" (concept word for seeded cards)
    perm: int                      # fact-order permutation id (0 = canonical)
    round: int
    call_id: str
    origin: str = "spoken"         # spoken | unspoken | probe | default
    testable_claim: str | None = None
    parent_ids: list[str] = field(default_factory=list)
    island_id: str = "main"
    lineage_id: str = ""           # root candidate id of the lineage (self if no parents)
    program: str | None = None     # ARC: python source defining transform(grid) -> grid
    pred: Any = None               # ARC: predicted test-output grid; BT: option letter "A".."D"
    extra: dict = field(default_factory=dict)   # decomp_id, pack_id, gap_ids (P1), free-form

    def to_dict(self) -> dict:
        d = asdict(self)
        if not d["lineage_id"]:
            d["lineage_id"] = self.id
        return d


@dataclass
class Judgment:
    """One row of judgments.jsonl (blind judge)."""
    id: str                        # candidate id
    p_raw: float                   # 0..1, logged, steers nothing at P0
    rubric: dict = field(default_factory=dict)
    perm_a: float | None = None
    perm_b: float | None = None
    spread: float | None = None    # |perm_a - perm_b|
    call_ids: list[str] = field(default_factory=list)

    def to_dict(self) -> dict:
        return asdict(self)


@dataclass
class VerifyResult:
    """One row of verify.jsonl."""
    id: str                        # candidate id
    status: str                    # verified | checked | fail | unverified
    verification_type: str         # demo_match | execution | agreement | llm_falsifier | llm_consensus | none
    attempts: int = 0
    partial_score: float = 0.0     # ARC: fraction of train pairs matched; BT: agreement fraction
    surprise: bool = False         # conf > hi and fail
    repr_change_event: bool = False
    feedback_record: dict | None = None   # harness/feedback.py record (<= cap tokens)
    details: dict = field(default_factory=dict)
    call_ids: list[str] = field(default_factory=list)

    def to_dict(self) -> dict:
        return asdict(self)


@dataclass
class LedgerRow:
    """One row of memory/ledger.jsonl. Append-only; written only by think.py / arms."""
    run_id: str
    batch: str
    benchmark: str
    item_id: str
    split: str
    family: str
    cls: str
    arm: str
    card: str
    operator: str
    round_type: str                # first | revise | post_reset | verify | encode | probe | judge
    round: int
    seed: str
    perm: int
    call_id: str
    tokens: dict                   # Usage.to_dict()
    p_raw: float | None = None
    agreement: float | None = None
    verification_type: str | None = None
    status: str | None = None
    ground_truth: bool | None = None   # only for splits where the key may be read (train, dev-tune)
    snapshot_hash: str | None = None
    origin: str = "spoken"
    cand_id: str | None = None
    run_instance: str | None = None    # unique per think()/run_arm() attempt (a re-run of the
                                       # same run_id gets a new one; stats keep the latest)
    ts: str = field(default_factory=now_ts)

    def to_dict(self) -> dict:
        return asdict(self)


@dataclass
class Answer:
    """runs/<id>/answer.json."""
    status: str                    # solved | checked | unverified | abstain
    answer: Any                    # ARC grid | BT option letter | text
    verification_type: str | None
    cand_id: str | None
    spent_tokens: int
    rounds: int
    best_guess: Any = None
    reason: str = ""

    def to_dict(self) -> dict:
        return asdict(self)


# ---------------------------------------------------------------- items (benchmark records)
# ARC item (data/arc_agi1_eval_le600.jsonl):
#   {"id", "benchmark": "arc", "train": [{"input": grid, "output": grid}], "test_input": grid,
#    "test_output": grid (KEY: scorer only), "family": "arc", "split": "dev"|...}
# BRAINTEASER item (data/brainteaser_sp.jsonl):
#   {"id", "benchmark": "bt", "question", "choices": [4 strings], "label": int (KEY: scorer only),
#    "family": "bt_sp", "split": ...}
KEY_FIELDS = {"arc": "test_output", "bt": "label"}


def strip_key(item: dict) -> dict:
    """Return a copy of the item with the answer key removed. Every run file and prompt is built
    from the stripped item; only the harness scorer reads the key (Pr14)."""
    key = KEY_FIELDS.get(item.get("benchmark", ""), None)
    return {k: v for k, v in item.items() if k != key}


def option_letter(i: int) -> str:
    return "ABCD"[i]
