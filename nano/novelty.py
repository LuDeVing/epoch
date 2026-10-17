"""Novelty gate and discovery curve, with no dependency beyond the standard library.

The gate: before a chosen idea is built, its mechanism text is compared (TF-IDF cosine) with every
candidate already built in this run and with the hypotheses in the experiments ledger. Above the
threshold it is a near-duplicate and is not built, except for a random audit share that is built
anyway so the gate's false-reject rate is measured (ShinkaEvolve-style rejection, with the audit
the evolutionary brief asks for).

The discovery curve: after each ideation round, how many clusters were new per context, and per
card how many distinct clusters its sketches landed in. Cards whose sketches keep landing in the
same few clusters are "attractor" cards and can be retired for the next round. The yield of new
clusters per context is reported per round; it does not change the number of contexts.
"""
from __future__ import annotations

import math
import random
import re
from collections import Counter

STOP = set("the a an of to in and or for with on at by is are be that this it as from into its than via "
           "we our use using used each per all any one two more less than then so if not no but can may".split())


def _tokens(text: str) -> list[str]:
    toks = re.findall(r"[a-z][a-z0-9_-]{2,}", (text or "").lower())
    out = []
    for t in toks:
        if t in STOP:
            continue
        for suf in ("ization", "isation", "ing", "ed", "es", "s"):
            if t.endswith(suf) and len(t) - len(suf) >= 3:
                t = t[: -len(suf)]
                break
        out.append(t)
    return out


class Index:
    """A tiny TF-IDF index over short texts."""

    def __init__(self, texts: dict[str, str]):
        self.docs = {k: Counter(_tokens(v)) for k, v in texts.items()}
        df = Counter()
        for c in self.docs.values():
            df.update(c.keys())
        n = max(1, len(self.docs))
        self.idf = {t: math.log((n + 1) / (d + 1)) + 1.0 for t, d in df.items()}
        self.vecs = {k: self._vec(c) for k, c in self.docs.items()}

    def _vec(self, c: Counter) -> dict[str, float]:
        v = {t: (1 + math.log(n)) * self.idf.get(t, math.log(2) + 1.0) for t, n in c.items()}
        norm = math.sqrt(sum(x * x for x in v.values())) or 1.0
        return {t: x / norm for t, x in v.items()}

    def similar(self, text: str, top: int = 3) -> list[tuple[str, float]]:
        q = self._vec(Counter(_tokens(text)))
        scores = []
        for k, v in self.vecs.items():
            s = sum(q.get(t, 0.0) * x for t, x in v.items())
            scores.append((k, round(s, 3)))
        scores.sort(key=lambda kv: -kv[1])
        return scores[:top]


def gate(text: str, built: dict[str, str], threshold: float = 0.8, audit_share: float = 0.1,
         rng: random.Random | None = None) -> dict:
    """Return {"build": bool, "nearest": (id, sim) | None, "audit": bool}."""
    if not built:
        return {"build": True, "nearest": None, "audit": False}
    idx = Index(built)
    nearest = idx.similar(text, 1)
    nid, sim = nearest[0] if nearest else (None, 0.0)
    if sim < threshold:
        return {"build": True, "nearest": (nid, sim), "audit": False}
    rng = rng or random.Random(text)
    audit = rng.random() < audit_share
    return {"build": audit, "nearest": (nid, sim), "audit": audit}


def discovery(clusters: list[dict], sketches: list[dict], round_no: int) -> dict:
    """New clusters per context this round, per-card yield, and the share of sketches in the two
    largest clusters (a collapse alarm)."""
    this = [s for s in sketches if s.get("round") == round_no or (round_no == 1 and s.get("round") is None)]
    ids = {s["id"] for s in this}
    contexts = {s.get("call_id") for s in this if s.get("call_id")}
    new_clusters = [c for c in clusters if c["members"] and all(m in ids for m in c["members"])]
    by_card: dict[str, dict] = {}
    for c in clusters:
        for m in c["members"]:
            s = next((x for x in this if x["id"] == m), None)
            if not s:
                continue
            d = by_card.setdefault(s.get("card", "?"), {"sketches": 0, "clusters": set()})
            d["sketches"] += 1
            d["clusters"].add(c["cluster_id"])
    yield_by_card = {k: {"sketches": v["sketches"], "distinct_clusters": len(v["clusters"]),
                         "yield": round(len(v["clusters"]) / max(1, v["sketches"]), 3)} for k, v in by_card.items()}
    sizes = sorted((len(c["members"]) for c in clusters), reverse=True)
    top2 = sum(sizes[:2]) / max(1, sum(sizes)) if sizes else 0.0
    return {"round": round_no, "contexts": len(contexts), "sketches": len(this), "new_clusters": len(new_clusters),
            "new_per_context": round(len(new_clusters) / max(1, len(contexts)), 2), "top2_share": round(top2, 3),
            "by_card": yield_by_card}


def attractor_cards(disc: dict, min_sketches: int = 8, yield_floor: float = 0.35) -> list[str]:
    """Cards whose sketches keep landing in the same clusters (low distinct-cluster yield)."""
    out = []
    for card, d in disc.get("by_card", {}).items():
        if d["sketches"] >= min_sketches and d["yield"] < yield_floor and card not in ("research", "diagnosis", "analogy", "adapt"):
            out.append(card)
    return out
