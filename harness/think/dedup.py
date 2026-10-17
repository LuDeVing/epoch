"""Exact-rule dedup (ARCHITECTURE.md section 4, `dedup.rate` / `dedup.drop`; section 5 row
"Dedup rule and threshold"; CTL-10).

Keys per benchmark rule (config.BENCHMARKS[b]["dedup_rule"]):
- grid (ARC): JSON of the predicted test-output grid; program hash when pred is None.
- option (BT): the option letter.
Other benchmarks fall back to a hash of whitespace-normalized text (embedding rule is P1).
The rate is measured before dropping; drop keeps the first candidate per key and emits one
cluster row per key seen this round (think.py is the only writer of clusters.jsonl).
"""
from __future__ import annotations

import hashlib
import json
import re

from .. import config
from ..schemas import Candidate

_LETTER = re.compile(r"^\s*(?:\d+[.)]\s*)?\(?([A-Da-d])\b")


def _hash(s: str) -> str:
    return hashlib.sha1(s.encode("utf-8")).hexdigest()[:16]


def _norm_code(src: str) -> str:
    """Whitespace-normalized program text, so trivial reformatting maps to one key."""
    lines = [ln.rstrip() for ln in (src or "").strip().splitlines()]
    return "\n".join(ln for ln in lines if ln.strip())


def option_of(cand: Candidate) -> str | None:
    """BT option letter from pred, else from the start of the text."""
    p = cand.pred
    if isinstance(p, str) and p.strip().upper() in ("A", "B", "C", "D"):
        return p.strip().upper()
    m = _LETTER.match(cand.text or "")
    return m.group(1).upper() if m else None


def rule_of(benchmark: str) -> str:
    return config.BENCHMARKS.get(benchmark, {}).get("dedup_rule", "text")


def dedup_key(cand: Candidate, benchmark: str) -> str:
    """Exact dedup key for one candidate under the benchmark rule (CTL-10)."""
    rule = rule_of(benchmark)
    if rule == "grid":
        if cand.pred is not None:
            return "grid:" + json.dumps(cand.pred, separators=(",", ":"))
        return "prog:" + _hash(_norm_code(cand.program or cand.text))
    if rule == "option":
        letter = option_of(cand)
        return f"opt:{letter}" if letter else "text:" + _hash(" ".join((cand.text or "").split()).lower())
    return "text:" + _hash(" ".join((cand.text or "").split()).lower())


def cluster_id(key: str) -> str:
    """Stable across rounds, so graph.py can join rows of the same cluster."""
    return "k" + _hash(key)[:12]


def rate(new: list[Candidate], prior: list[Candidate], benchmark: str) -> float:
    """Share of new candidates whose key already exists among prior or earlier new ones."""
    if not new:
        return 0.0
    seen = {dedup_key(c, benchmark) for c in prior}
    dups = 0
    for c in new:
        k = dedup_key(c, benchmark)
        dups += k in seen
        seen.add(k)
    return dups / len(new)


def drop(new: list[Candidate], prior: list[Candidate], benchmark: str,
         round_no: int) -> tuple[list[Candidate], list[dict]]:
    """Keep the first candidate per key (prior candidates win); return kept and cluster rows
    {cluster_id, rule, members, representative_id, round} for every key seen in `new`."""
    rule = rule_of(benchmark)
    rep: dict[str, str] = {}
    for c in prior:
        rep.setdefault(dedup_key(c, benchmark), c.id)
    kept: list[Candidate] = []
    members: dict[str, list[str]] = {}
    for c in new:
        k = dedup_key(c, benchmark)
        if k not in rep:
            rep[k] = c.id
            kept.append(c)
        members.setdefault(k, []).append(c.id)
    rows = []
    for k, ids in members.items():
        mem = ids if rep[k] in ids else [rep[k]] + ids
        rows.append({"cluster_id": cluster_id(k), "rule": rule, "key": k, "members": mem,
                     "representative_id": rep[k], "round": round_no,
                     "dropped": [i for i in ids if i != rep[k]]})
    return kept, rows
