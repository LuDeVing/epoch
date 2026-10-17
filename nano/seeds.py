"""Seed words for the "seeded" idea card (N7): chosen by abstract function and distance, not purely at random.

Rule, per part and round:
- every seeded context on one part gets a different abstract function (flow, storage, feedback, competition,
  decay, symmetry, routing, compression, memory, timing), so the detours point in different directions;
- distances are mixed: about half far (everyday objects, nature), a quarter mid (natural and social sciences),
  a quarter near (engineered control, signal and logistics systems). Far raises variance, not the mean, and the
  benefit of distance levels off, so no band is dropped;
- a seed used on the part before (any round) is not used again while others are left;
- functions are drawn with weight (distinct clusters + 1) / (seeded sketches + 2) from this run's earlier rounds,
  so all start equal and a function whose sketches kept landing in new clusters is drawn more often. The draw stays
  random (seeded by run id, round and part), so no two runs are identical;
- the prompt names the function in one line, so the inventor maps by function rather than by surface.

`choose(..., mode="random")` is the control arm: the old uniform draw over the bare word list.
"""
from __future__ import annotations

import json
import math
import random
from pathlib import Path

FUNCTIONS = ("flow", "storage", "feedback", "competition", "decay", "symmetry", "routing", "compression", "memory", "timing")
BAND_SHARE = {"far": 0.5, "mid": 0.25, "near": 0.25}
CATALOG_NAME = "concepts_tagged.json"


def catalog_path() -> Path:
    from harness import config
    return Path(config.SEEDS_PATH).parent / CATALOG_NAME


def load_catalog(path: Path | None = None) -> dict:
    """{"hints": {function: text}, "seeds": [{word, function, band, domain}]}; empty seeds when missing."""
    p = Path(path) if path else catalog_path()
    try:
        data = json.loads(p.read_text(encoding="utf-8"))
    except Exception:  # noqa: BLE001
        return {"hints": {}, "seeds": []}
    hints = data.get("hints") or {}
    rows = [dict(r, hint=hints.get(r.get("function"), "")) for r in data.get("seeds", [])
            if r.get("word") and r.get("function") and r.get("band")]
    return {"hints": hints, "seeds": rows}


def band_plan(k: int, rng: random.Random) -> list[str]:
    """k distance bands: half far (rounded up), the rest alternating mid and near, in random order."""
    if k <= 0:
        return []
    if k == 1:
        r, acc = rng.random(), 0.0
        for b, p in BAND_SHARE.items():
            acc += p
            if r < acc:
                return [b]
        return ["far"]
    n_far = math.ceil(k / 2)
    rest = ["mid" if i % 2 == 0 else "near" for i in range(k - n_far)]
    if rest and rng.random() < 0.5:     # with an odd remainder, which of mid / near gets the extra one is random
        rest = ["near" if b == "mid" else "mid" for b in rest]
    plan = ["far"] * n_far + rest
    rng.shuffle(plan)
    return plan


def function_weights(history: dict | None) -> dict[str, float]:
    """(distinct clusters + 1) / (seeded sketches + 2) per function; 0.5 each with no history (uniform)."""
    fh = (history or {}).get("function", {})
    return {f: (fh.get(f, {}).get("clusters", 0) + 1) / (fh.get(f, {}).get("sketches", 0) + 2) for f in FUNCTIONS}


def _weighted_order(weights: dict[str, float], rng: random.Random) -> list[str]:
    """All functions in a random order, heavier ones earlier (weighted sampling without replacement)."""
    keyed = []
    for f in FUNCTIONS:
        w = max(1e-9, weights.get(f, 0.5))
        keyed.append((rng.random() ** (1.0 / w), f))       # Efraimidis-Spirakis keys
    return [f for _, f in sorted(keyed, reverse=True)]


def choose(part_id: str, k: int, used, history: dict | None, rng: random.Random,
           catalog: dict | None = None, mode: str = "function", words: list[str] | None = None) -> list[dict]:
    """k seed dicts {word, function, band, domain, hint} for the seeded contexts of one part this round.
    `used`: words already used on this part (excluded while others remain). `history`: from yield_history.
    mode "random": the control arm, a uniform draw from `words` (the plain list), bare words, no function."""
    used = set(used or ())
    if k <= 0:
        return []
    if mode == "random":
        pool = list(words or [])
        out = []
        for _ in range(k):
            w = rng.choice([x for x in pool if x not in used] or pool) if pool else ""
            used.add(w)
            out.append({"word": w, "function": "", "band": "", "domain": "", "hint": ""})
        return out
    cat = catalog if catalog is not None else load_catalog()
    rows = cat.get("seeds", [])
    if not rows:                                            # no tagged list: fall back to the control arm
        return choose(part_id, k, used, history, rng, mode="random", words=words)
    order = _weighted_order(function_weights(history), rng)
    funcs = [order[i % len(order)] for i in range(k)]      # distinct functions up to 10 contexts per part
    bands = band_plan(k, rng)
    near_to = {"far": ("far", "mid", "near"), "mid": ("mid", "far", "near"), "near": ("near", "mid", "far")}
    out = []
    for f, b in zip(funcs, bands):
        pick = None
        for bb in near_to[b]:                               # keep the function, relax the band
            pool = [r for r in rows if r["function"] == f and r["band"] == bb and r["word"] not in used]
            if pool:
                pick = rng.choice(pool)
                break
        if pick is None:                                    # function exhausted on this part: any unused seed
            pool = [r for r in rows if r["word"] not in used] or rows
            pick = rng.choice(pool)
        used.add(pick["word"])
        out.append({"word": pick["word"], "function": pick["function"], "band": pick["band"],
                    "domain": pick.get("domain", ""), "hint": pick.get("hint", "")})
    return out


def prompt_line(seed: dict | None, word: str) -> str:
    """"Starting point: <word> (<function>: <hint>)" for a tagged seed, the bare word otherwise."""
    if seed and seed.get("function") and seed.get("hint"):
        return f"Starting point: {word} ({seed['function']}: {seed['hint']})"
    return f"Starting point: {word}"


def yield_history(sketches: list[dict], clusters: list[dict], seed_info: dict) -> dict:
    """Per function and per seed word: seeded sketches and the distinct clusters they reached.
    `seed_info` maps a word to its seed dict (only words chosen by `choose` count)."""
    where = {}
    for c in clusters or []:
        for m in c.get("members", []):
            where[m] = c.get("cluster_id")
    by_f: dict[str, dict] = {}
    by_w: dict[str, dict] = {}
    for s in sketches or []:
        if s.get("card") != "seeded":
            continue
        info = seed_info.get(s.get("seed", ""))
        if not info or not info.get("function"):
            continue
        cl = where.get(s.get("id"))
        for key, table in ((info["function"], by_f), (s["seed"], by_w)):
            d = table.setdefault(key, {"sketches": 0, "clusters": set()})
            d["sketches"] += 1
            if cl is not None:
                d["clusters"].add(cl)
    fmt = lambda t: {k: {"sketches": v["sketches"], "clusters": len(v["clusters"])} for k, v in sorted(t.items())}  # noqa: E731
    return {"function": fmt(by_f), "seed": fmt(by_w)}
