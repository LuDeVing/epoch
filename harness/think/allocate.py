"""Card allocation (ARCHITECTURE.md section 4 `allocate.initial`, `allocate.fresh_tuples`,
`allocate.reallocate`, `revise_specs`, `est_cost`, `est_verify`; section 3 /generate
"Directed-card minimum"; section 5 rows "n0", "Card allocation", "est_cost(s), est_verify(cand)";
GEN-17, CTL-07, CTL-11, CTL-14).

Round 1 = seeded + memory-blind (a uniformly random applicable card, random operator) + every
applicable P0 directed card (low_prior, transform; formal on formalizable benchmarks). Directed
cards are ordered round-robin until every cell has N_min train rows in strategy_stats; then by
Thompson sampling on Beta(pass+1, fail+1) / mean_tokens with a 10 percent exploration floor.
Spec order returned by initial(): [seeded, memory_blind, directed...] (MEMORY_BLIND_INDEX).
"""
from __future__ import annotations

import math
import random

from .. import config
from ..schemas import Candidate, VerifyResult

try:                                   # cards owner; fallback keeps this module importable alone
    from ..run_card import CardSpec
except ImportError:                    # pragma: no cover - replaced once run_card.py exists
    from dataclasses import dataclass

    @dataclass
    class CardSpec:                    # mirrors README: run_card.CardSpec
        card: str
        operator: str = "none"
        seed: str = ""
        perm: int = 0
        variant: str | None = None
        parent_id: str | None = None

ARM = "scaffold"
MEMORY_BLIND_INDEX = 1
N_PERMS = 4                            # perm ids 0 (canonical) .. 3; 1 = the encode shuffled view
OPERATORS = {
    "seeded": ["none"],
    "low_prior": ["none"],
    "transform": ["drop", "negate", "vary", "oppose"],
    "formal": ["none"],
    "revise": ["fix", "specialize", "recurse"],
}
SEEDED_CARDS = {"seeded"}              # cards that take a concept seed
STEPS = {"transform": 3}               # calls per card (3-call DAG); others 1
INPUT_EST = {"arc": 3000, "bt": 800}   # cold-start routed-input estimate, tokens
REVISE_EXTRA = 2000                    # parent artifact + feedback record (cap 1500)
VERIFY_INPUT_EST = 2000


def spec_tuple(spec: CardSpec) -> tuple:
    """The (card, operator, seed, perm) tuple the driver records in state.used_tuples."""
    return (spec.card, spec.operator, spec.seed, spec.perm)


def _rng(cls: str, replicate: int, purpose: str) -> random.Random:
    # The allocator is not given item_id (README signature), so the class key stands in for it.
    return random.Random(f"{cls}:{ARM}:{replicate}:{purpose}")


def _seeds() -> list[str]:
    from ..probe import load_seeds
    return load_seeds()


def directed_cards(benchmark: str) -> list[str]:
    """Applicable P0 directed cards for round 1 (GEN-17); revise enters via revise_specs."""
    cards = ["low_prior", "transform"]
    if config.BENCHMARKS.get(benchmark, {}).get("formalizable"):
        cards.append("formal")
    return cards


def applicable_cards(benchmark: str) -> list[str]:
    return ["seeded"] + directed_cards(benchmark)


# ---------------------------------------------------------------- strategy_stats access
def stats_rows(views: dict | None) -> list[dict]:
    """Rows {cls, card, round_type, n, pass, fail, mean_tokens} from views["strategy_stats"].
    Accepts a list of rows, {"rows": [...]}, or a dict keyed "cls|card|round_type"."""
    st = (views or {}).get("strategy_stats")
    if not st:
        return []
    if isinstance(st, dict) and isinstance(st.get("rows"), list):
        st = st["rows"]
    if isinstance(st, dict):
        rows = []
        for k, v in st.items():
            parts = (k.split("|") if isinstance(k, str) else list(k)) + ["", "", ""]
            rows.append({"cls": parts[0], "card": parts[1], "round_type": parts[2], **v})
        st = rows
    out = []
    for r in st:
        p, f = int(r.get("pass", 0)), int(r.get("fail", 0))
        out.append({**r, "pass": p, "fail": f, "n": int(r.get("n", p + f))})
    return out


def _cell(rows: list[dict], cls: str, card: str, round_type: str) -> dict | None:
    for r in rows:
        if r.get("cls") == cls and r.get("card") == card and r.get("round_type", round_type) == round_type:
            return r
    return None


# ---------------------------------------------------------------- ordering
def order_round_robin(cards: list[str], replicate: int, round_no: int) -> list[str]:
    """Rotate the directed cards so the leading card changes with replicate and round."""
    if not cards:
        return []
    k = (replicate + round_no) % len(cards)
    return cards[k:] + cards[:k]


def order_thompson(cards: list[str], cells: dict[str, dict], rng: random.Random) -> list[str]:
    """Sort by p ~ Beta(pass+1, fail+1) divided by mean_tokens; with probability
    exploration_floor the order is a uniform shuffle instead (section 5 Card allocation)."""
    if rng.random() < config.PARAMS["exploration_floor"]:
        out = list(cards)
        rng.shuffle(out)
        return out
    score = {}
    for c in cards:
        cell = cells[c]
        p = rng.betavariate(cell["pass"] + 1, cell["fail"] + 1)
        score[c] = p / max(1.0, float(cell.get("mean_tokens") or 1.0))
    return sorted(cards, key=lambda c: -score[c])


def order_directed(cards, cls, views, replicate, round_no, round_type="first") -> list[str]:
    """Thompson once every cell has >= N_min rows, else round-robin."""
    rows = stats_rows(views)
    cells = {c: _cell(rows, cls, c, round_type) for c in cards}
    if rows and all(v and v["n"] >= config.PARAMS["N_min"] for v in cells.values()):
        return order_thompson(cards, cells, _rng(cls, replicate, f"thompson:{round_no}"))
    return order_round_robin(cards, replicate, round_no)


# ---------------------------------------------------------------- spec builders
def _spec(card: str, rng: random.Random, seeds: list[str], perm: int = 0) -> CardSpec:
    op = rng.choice(OPERATORS.get(card, ["none"]))
    seed = rng.choice(seeds) if card in SEEDED_CARDS else ""
    return CardSpec(card=card, operator=op, seed=seed, perm=perm)


def initial(benchmark: str, cls: str, views: dict | None, n0: int, replicate: int,
            round_no: int) -> list[CardSpec]:
    """Round-1 specs: seeded, memory-blind, then every applicable directed card (GEN-17).
    n0 above the base adds seeded specs with new seeds; below it, seeded + 2 directed are kept."""
    rng, seeds = _rng(cls, replicate, f"initial:{round_no}"), _seeds()
    seeded = _spec("seeded", rng, seeds, perm=1)
    mb_card = rng.choice(applicable_cards(benchmark))                 # memory-blind: uniform card
    directed = [_spec(c, rng, seeds) for c in order_directed(directed_cards(benchmark), cls, views,
                                                              replicate, round_no)]
    # the memory-blind spec is drawn from the tuples the seeded and directed specs do not use,
    # so round 1 never spawns the same (card, operator, seed, perm) twice
    taken = {spec_tuple(s) for s in [seeded] + directed}
    drawn = fresh_tuples(benchmark, cls, taken, [], replicate, round_no, 1, cards=[mb_card])
    blind = drawn[0] if drawn else _spec(mb_card, rng, seeds, perm=0)
    full = [seeded, blind] + directed
    if n0 >= len(full):
        used = {spec_tuple(s) for s in full}
        extra = fresh_tuples(benchmark, cls, used, [], replicate, round_no, n0 - len(full),
                             cards=["seeded"])
        return full + extra
    required = [seeded] + directed[:2]
    rest = [blind] + directed[2:]
    return required + rest[:max(0, n0 - len(required))]


def _candidate_tuples(card: str, seeds: list[str]) -> list[tuple]:
    seed_list = seeds if card in SEEDED_CARDS else [""]
    return [(card, op, s, p) for op in OPERATORS.get(card, ["none"]) for s in seed_list
            for p in range(N_PERMS)]


def fresh_tuples(benchmark: str, cls: str, used: set, variants: list, replicate: int,
                 round_no: int, n: int, cards: list[str] | None = None) -> list[CardSpec]:
    """n specs whose (card, operator, seed, perm) tuple is unused, spread round-robin across
    cards; each gets variants[i % len] as s.variant (base views when empty) (CTL-11, CTL-14)."""
    rng, seeds = _rng(cls, replicate, f"fresh:{round_no}"), _seeds()
    pools = {}
    for c in cards or applicable_cards(benchmark):
        pool = [t for t in _candidate_tuples(c, seeds) if t not in used]
        rng.shuffle(pool)
        pools[c] = pool
    order = order_round_robin(list(pools), replicate, round_no)
    out, taken = [], set(used)
    while len(out) < n and any(pools.values()):
        for c in order:
            while pools[c] and pools[c][-1] in taken:
                pools[c].pop()
            if not pools[c] or len(out) >= n:
                continue
            t = pools[c].pop()
            taken.add(t)
            v = variants[len(out) % len(variants)] if variants else None
            out.append(CardSpec(card=t[0], operator=t[1], seed=t[2], perm=t[3], variant=v))
    return out


def reallocate(specs: list[CardSpec], multiplier: float) -> list[CardSpec]:
    """Scale the spec list by the within-run LP multiplier (P1, CTL-08); at P0 the multiplier
    is 1.0 and the list is returned unchanged. Never drops below seeded + 2 directed."""
    specs = [s for s in specs if s.card != "revise"]
    if not specs or multiplier == 1.0:
        return list(specs)
    floor_n = min(len(specs), 3)
    target = max(floor_n, int(round(len(specs) * multiplier)))
    return [specs[i % len(specs)] for i in range(target)]


def revise_specs(parents: list[tuple[Candidate, VerifyResult]], replicate: int) -> list[CardSpec]:
    """One revise spec per parent with parent_id set; operator from the P0 set (GEN-14).
    The RNG is keyed on stable parent fields (card, operator, seed, perm, round) and the
    parent's position, never on its uuid, so a replicate reproduces its operator choices."""
    out = []
    for i, (cand, _vr) in enumerate(parents):
        key = f"{cand.card}:{cand.operator}:{cand.seed}:{cand.perm}:{cand.round}:{i}"
        rng = random.Random(f"{key}:{ARM}:{replicate}:revise")
        out.append(CardSpec(card="revise", operator=rng.choice(OPERATORS["revise"]), seed="",
                            perm=0, parent_id=cand.id))
    return out


# ---------------------------------------------------------------- cost estimators
def _cell_mean_tokens(views: dict | None, card: str, round_type: str) -> float | None:
    rows = [r for r in stats_rows(views) if r.get("card") == card
            and r.get("round_type", round_type) == round_type and r.get("mean_tokens")]
    n = sum(max(1, r["n"]) for r in rows)
    if not rows or n == 0:
        return None
    return sum(float(r["mean_tokens"]) * max(1, r["n"]) for r in rows) / n


def est_cost(spec: CardSpec, views: dict | None, benchmark: str) -> int:
    """Cell mean tokens per card call from strategy_stats, else cold start: per step the role
    max_tokens + routed-input estimate + CLI overhead (section 4 Spend accounting)."""
    round_type = "revise" if spec.card == "revise" else "first"
    mean = _cell_mean_tokens(views, spec.card, round_type)
    if mean is not None:
        return int(math.ceil(mean))
    role = "program" if benchmark == "arc" else "generate"
    per_step = (config.PARAMS["max_tokens"][role] + INPUT_EST.get(benchmark, 1500)
                + config.CLI_OVERHEAD_TOKENS_EST)
    extra = REVISE_EXTRA if spec.card == "revise" else 0
    return STEPS.get(spec.card, 1) * per_step + extra


def est_verify(k: int, mean_per_attempt: float | None) -> int:
    """k x the run's mean tokens per verify attempt; cold start uses the verify max_tokens plus
    an input estimate and overhead. Pass 0.0 for script-only checks (ARC demo_match)."""
    if mean_per_attempt is not None:
        return int(math.ceil(k * float(mean_per_attempt)))
    return k * (config.PARAMS["max_tokens"]["verify"] + VERIFY_INPUT_EST
                + config.CLI_OVERHEAD_TOKENS_EST)
