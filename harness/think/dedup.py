"""Exact-rule dedup (ARCHITECTURE.md section 4, `dedup.rate` / `dedup.drop`; section 5 row
"Dedup rule and threshold"; CTL-10).

Keys per benchmark rule (config.BENCHMARKS[b]["dedup_rule"]):
- grid (ARC): JSON of the predicted test-output grid; program hash when pred is None.
- option (BT): the option letter.
Other benchmarks fall back to a hash of whitespace-normalized text (embedding rule is P1).
The rate is measured before dropping; drop keeps the first candidate per key and emits one
cluster row per key seen this round (think.py is the only writer of clusters.jsonl).
Under the grid rule drop can take demo_of(cand) -> bool (all train pairs reproduced): a later
candidate with the same predicted grid is then kept when it passes the examples and no earlier
one with that grid did, so dedup never drops a passing program in favour of a failing one.
vote() is the one selection rule for verified ARC programs, shared by think.py and the
portfolio scripts: group by test answer, augmented outputs only as a tie-break.
"""
from __future__ import annotations

import hashlib
import json
import re
from collections import Counter

from .. import config
from ..schemas import Candidate

# An option label at the very start of the text: "B.", "(c)", "D)", "A:" or a lone letter. The letter must be
# followed by a label delimiter or the end of the line, so prose such as "A key insight" is not option A.
_LETTER = re.compile(r"^\s*(?:\d+[.)]\s*)?\**\(?([A-Da-d])(?:[.):]|\)?\**\s*$)", re.M)


def _hash(s: str) -> str:
    return hashlib.sha1(s.encode("utf-8")).hexdigest()[:16]


def _norm_code(src: str) -> str:
    """Whitespace-normalized program text, so trivial reformatting maps to one key."""
    lines = [ln.rstrip() for ln in (src or "").strip().splitlines()]
    return "\n".join(ln for ln in lines if ln.strip())


def option_of(cand: Candidate) -> str | None:
    """BT option letter from pred, else the plain arm's answer parser (the probe uses the same one),
    else an option label at the very start of the text."""
    p = cand.pred
    if isinstance(p, str) and p.strip().upper() in ("A", "B", "C", "D"):
        return p.strip().upper()
    from ..arms.plain import parse_letter
    j = parse_letter(cand.text or "")
    if j is not None:
        return "ABCD"[j]
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
         round_no: int, demo_of=None) -> tuple[list[Candidate], list[dict]]:
    """Keep the first candidate per key (prior candidates win); return kept and cluster rows
    {cluster_id, rule, members, representative_id, round} for every key seen in `new`.
    demo_of (grid rule only): a later same-grid candidate that passes the examples is kept when
    no earlier one with that grid passed. demo_of is called only on such collisions."""
    rule = rule_of(benchmark)
    rep: dict[str, str] = {}
    seen: dict[str, list[Candidate]] = {}
    for c in prior:
        k = dedup_key(c, benchmark)
        rep.setdefault(k, c.id)
        seen.setdefault(k, []).append(c)
    kept: list[Candidate] = []
    members: dict[str, list[str]] = {}
    for c in new:
        k = dedup_key(c, benchmark)
        if k not in rep:
            rep[k] = c.id
            kept.append(c)
        elif (demo_of is not None and rule == "grid" and k.startswith("grid:")
              and not any(demo_of(x) for x in seen[k]) and demo_of(c)):
            kept.append(c)                 # first passing program for this grid: verify it too
        seen.setdefault(k, []).append(c)
        members.setdefault(k, []).append(c.id)
    kept_ids = {c.id for c in kept}
    rows = []
    for k, ids in members.items():
        mem = ids if rep[k] in ids else [rep[k]] + ids
        rows.append({"cluster_id": cluster_id(k), "rule": rule, "key": k, "members": mem,
                     "representative_id": rep[k], "round": round_no,
                     "dropped": [i for i in ids if i != rep[k] and i not in kept_ids]})
    return kept, rows


def vote(items: list, pred_of, length_of, aug_of=None):
    """Selection among verified ARC programs (00_IDEAS.md item 16): group by test answer; the largest
    group wins. Only when groups tie on size, aug_of(item) -> hashable or None (outputs on rotated and
    mirrored copies of the test input; None when the program crashes there) breaks the tie: the group
    with the largest sub-group of identical augmented outputs wins. Then the shortest program.
    Returns (chosen item, size of its group, number of distinct answers); (None, 0, 0) if empty."""
    groups: dict[str, list] = {}
    for x in items:
        p = pred_of(x)
        if p is not None:
            groups.setdefault(json.dumps(p, separators=(",", ":")), []).append(x)
    if not groups:
        return None, 0, 0
    top = max(len(g) for g in groups.values())
    tied = [g for g in groups.values() if len(g) == top]

    def support(g) -> int:
        if aug_of is None or len(tied) == 1:
            return 0
        c = Counter(k for k in (aug_of(x) for x in g) if k is not None)
        return max(c.values(), default=0)

    best = max(tied, key=lambda g: (support(g), -min(length_of(x) for x in g)))
    return min(best, key=length_of), len(best), len(groups)
