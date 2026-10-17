"""Card allocation (ARCHITECTURE.md section 4 `allocate.initial`, `allocate.fresh_tuples`,
`allocate.reallocate`, `revise_specs`, `est_cost`, `est_verify`; section 3 /generate
"Directed-card minimum"; section 5 rows "n0", "Card allocation", "est_cost(s), est_verify(cand)";
GEN-17, CTL-07, CTL-11, CTL-14).

Round 1 = seeded + memory-blind (a uniformly random applicable card, random operator) + every
applicable P0 directed card (low_prior, transform; formal on formalizable benchmarks). GEN-17
runs every directed card every round, so memory never removes one. Memory decides (a) the order
of the directed cards, which decides what a tight budget cuts (think._within_budget), and (b)
the card of the respawn slot rounds 2+ add (section 5: max_spawns_per_round = n0 + 3 = 2 revise
children + 1 respawn; `respawn`).

Posterior per card (CTL-07, MEM-05): the (class, card, round_type) cell of the frozen
strategy_stats view when it has N_min rows; below that, back-off to the pooled cell over every
class for that card and round type; when the pooled cell is short too for any card, cold-start
round-robin. Score = p ~ Beta(pass+1, fail+1) divided by est_cost (the cell's mean tokens per
card run, class cell first). Exploration floor (CTL-07: 10% of the budget spread uniformly over
cards): each allocated slot is, with probability exploration_floor, a uniformly random card
instead of the Thompson pick. With two or more slots the posterior mode is guaranteed one.

RNG: keyed f"{item_id}:{ARM}:{replicate}:{purpose}" (README Determinism), so items of one class
get independent draws while the statistics stay pooled per class; cls stands in only when a
caller passes no item_id.
Spec order returned by initial(): [seeded, memory_blind, directed...] (MEMORY_BLIND_INDEX).
"""
from __future__ import annotations

import hashlib
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


def _rng(key: str, replicate: int, purpose: str) -> random.Random:
    """README Determinism: key is the item id (the class only when no item id is given)."""
    return random.Random(f"{key}:{ARM}:{replicate}:{purpose}")


def _offset(item_id: str | None) -> int:
    """Stable per-item rotation offset for round-robin (0 without an item id)."""
    if not item_id:
        return 0
    return int(hashlib.sha256(str(item_id).encode("utf-8")).hexdigest()[:8], 16)


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


def _weight(r: dict) -> int:
    """Card runs behind a cell's mean_tokens (n_calls), else its outcome count."""
    return max(1, int(r.get("n_calls") or r.get("n") or 0))


def _pooled(rows: list[dict], card: str, round_type: str) -> dict | None:
    """The cell pooled over every class for one card and round type (MEM-05 back-off)."""
    sel = [r for r in rows if r.get("card") == card and r.get("round_type", round_type) == round_type]
    if not sel:
        return None
    tok = [r for r in sel if r.get("mean_tokens")]
    w = sum(_weight(r) for r in tok)
    return {"cls": "*", "card": card, "round_type": round_type,
            "pass": sum(r["pass"] for r in sel), "fail": sum(r["fail"] for r in sel),
            "n": sum(r["n"] for r in sel),
            "mean_tokens": (sum(float(r["mean_tokens"]) * _weight(r) for r in tok) / w) if w else 0.0}


def posterior_cells(cards: list[str], cls: str, views: dict | None,
                    round_type: str = "first") -> dict[str, dict] | None:
    """Per card the class cell when it has N_min rows, else the pooled cell over every class
    (MEM-05); None (cold start, round-robin) when any card is short in both."""
    rows = stats_rows(views)
    if not rows or not cards:
        return None
    n_min, out = config.PARAMS["N_min"], {}
    for c in cards:
        cell = _cell(rows, cls, c, round_type)
        if not cell or cell["n"] < n_min:
            cell = _pooled(rows, c, round_type)
        if not cell or cell["n"] < n_min:
            return None
        out[c] = cell
    return out


def _costs(cards, views, benchmark, cls, round_type) -> dict[str, float]:
    return {c: float(est_cost(CardSpec(card=c), views, benchmark, cls=cls, round_type=round_type))
            for c in cards}


def _draw(cell: dict, cost: float, rng: random.Random) -> float:
    return rng.betavariate(cell["pass"] + 1, cell["fail"] + 1) / max(1.0, float(cost or 1.0))


# ---------------------------------------------------------------- ordering
def order_round_robin(cards: list[str], replicate: int, round_no: int,
                      item_id: str | None = None) -> list[str]:
    """Rotate the cards so the leading card changes with item, replicate and round."""
    if not cards:
        return []
    k = (replicate + round_no + _offset(item_id)) % len(cards)
    return cards[k:] + cards[:k]


def order_thompson(cards: list[str], cells: dict[str, dict], rng: random.Random,
                   costs: dict[str, float] | None = None) -> list[str]:
    """One draw p ~ Beta(pass+1, fail+1) per card, scored p / est_cost (cell mean_tokens when no
    costs are given). Each position in turn is, with probability exploration_floor, a uniform
    pick among the cards left, else the best-scoring card left (section 5 Card allocation)."""
    costs = costs or {c: float(cells[c].get("mean_tokens") or 1.0) for c in cards}
    score = {c: _draw(cells[c], costs[c], rng) for c in cards}
    left, out = sorted(cards, key=lambda c: -score[c]), []
    while left:
        pick = rng.choice(left) if rng.random() < config.PARAMS["exploration_floor"] else left[0]
        out.append(pick)
        left.remove(pick)
    return out


def pick_cards(cards: list[str], cells: dict[str, dict], rng: random.Random, n: int,
               costs: dict[str, float] | None = None) -> list[str]:
    """n allocated slots, cards may repeat: each slot is a uniform card with probability
    exploration_floor (the CTL-07 floor), else the Thompson pick (fresh draws per slot). With
    n >= 2 the posterior mode (highest mean pass per token) is guaranteed one slot (MEM-05)."""
    if not cards or n <= 0:
        return []
    costs = costs or {c: float(cells[c].get("mean_tokens") or 1.0) for c in cards}
    out = []
    for _ in range(n):
        if rng.random() < config.PARAMS["exploration_floor"]:
            out.append(rng.choice(cards))
            continue
        score = {c: _draw(cells[c], costs[c], rng) for c in cards}
        out.append(max(cards, key=lambda c: score[c]))
    mean = {c: (cells[c]["pass"] + 1) / (cells[c]["pass"] + cells[c]["fail"] + 2)
            / max(1.0, costs[c]) for c in cards}
    mode = max(cards, key=lambda c: mean[c])
    if n >= 2 and mode not in out:
        out[-1] = mode
    return out


def order_directed(cards, cls, views, replicate, round_no, round_type="first", *,
                   benchmark: str = "", item_id: str | None = None) -> list[str]:
    """Thompson once every card has a posterior cell (class cell, or pooled back-off) with
    N_min rows, else round-robin."""
    cells = posterior_cells(cards, cls, views, round_type)
    if cells is None:
        return order_round_robin(cards, replicate, round_no, item_id)
    rng = _rng(item_id or cls, replicate, f"thompson:{round_no}")
    return order_thompson(cards, cells, rng, _costs(cards, views, benchmark, cls, round_type))


# ---------------------------------------------------------------- spec builders
def _spec(card: str, rng: random.Random, seeds: list[str], perm: int = 0) -> CardSpec:
    op = rng.choice(OPERATORS.get(card, ["none"]))
    seed = rng.choice(seeds) if card in SEEDED_CARDS else ""
    return CardSpec(card=card, operator=op, seed=seed, perm=perm)


def initial(benchmark: str, cls: str, views: dict | None, n0: int, replicate: int,
            round_no: int, item_id: str | None = None) -> list[CardSpec]:
    """Round-1 specs: seeded, memory-blind, then every applicable directed card (GEN-17).
    n0 above the base adds seeded specs with new seeds; below it, seeded + 2 directed are kept."""
    rng, seeds = _rng(item_id or cls, replicate, f"initial:{round_no}"), _seeds()
    seeded = _spec("seeded", rng, seeds, perm=1)
    mb_card = rng.choice(applicable_cards(benchmark))                 # memory-blind: uniform card
    directed = [_spec(c, rng, seeds) for c in order_directed(
        directed_cards(benchmark), cls, views, replicate, round_no, benchmark=benchmark,
        item_id=item_id)]
    # the memory-blind spec is drawn from the tuples the seeded and directed specs do not use,
    # so round 1 never spawns the same (card, operator, seed, perm) twice
    taken = {spec_tuple(s) for s in [seeded] + directed}
    drawn = fresh_tuples(benchmark, cls, taken, [], replicate, round_no, 1, cards=[mb_card],
                         item_id=item_id)
    blind = drawn[0] if drawn else _spec(mb_card, rng, seeds, perm=0)
    full = [seeded, blind] + directed
    if n0 >= len(full):
        used = {spec_tuple(s) for s in full}
        extra = fresh_tuples(benchmark, cls, used, [], replicate, round_no, n0 - len(full),
                             cards=["seeded"], item_id=item_id)
        return full + extra
    required = [seeded] + directed[:2]
    rest = [blind] + directed[2:]
    return required + rest[:max(0, n0 - len(required))]


def _candidate_tuples(card: str, seeds: list[str]) -> list[tuple]:
    seed_list = seeds if card in SEEDED_CARDS else [""]
    return [(card, op, s, p) for op in OPERATORS.get(card, ["none"]) for s in seed_list
            for p in range(N_PERMS)]


def fresh_tuples(benchmark: str, cls: str, used: set, variants: list, replicate: int,
                 round_no: int, n: int, cards: list[str] | None = None,
                 item_id: str | None = None) -> list[CardSpec]:
    """n specs whose (card, operator, seed, perm) tuple is unused, spread round-robin across
    cards; each gets variants[i % len] as s.variant (base views when empty) (CTL-11, CTL-14).
    Never re-uses a tuple: when the pools run out, fewer than n specs come back."""
    rng, seeds = _rng(item_id or cls, replicate, f"fresh:{round_no}"), _seeds()
    pools = {}
    for c in cards or applicable_cards(benchmark):
        pool = [t for t in _candidate_tuples(c, seeds) if t not in used]
        rng.shuffle(pool)
        pools[c] = pool
    order = order_round_robin(list(pools), replicate, round_no, item_id)
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


def respawn(benchmark: str, cls: str, views: dict | None, used: set, variants: list,
            replicate: int, round_no: int, n: int = 1, *, item_id: str | None = None,
            round_type: str = "first") -> list[CardSpec]:
    """The allocated respawn slot(s) of rounds 2+ (section 5 max_spawns_per_round: 1 respawn).
    Cards come from pick_cards over the applicable cards (posterior cells with the pooled
    back-off, floor, mode slot), or round-robin at cold start; each slot gets an unused tuple of
    its card and falls to the next card in round-robin order when that card's pool is empty."""
    cards = applicable_cards(benchmark)
    rr = order_round_robin(cards, replicate, round_no, item_id)
    cells = posterior_cells(cards, cls, views, round_type)
    if cells is None:
        picks = [rr[i % len(rr)] for i in range(n)]
    else:
        rng = _rng(item_id or cls, replicate, f"respawn:{round_no}")
        picks = pick_cards(cards, cells, rng, n, _costs(cards, views, benchmark, cls, round_type))
    out, taken = [], set(used)
    for card in picks:
        for c in [card] + [x for x in rr if x != card]:
            got = fresh_tuples(benchmark, cls, taken, variants, replicate, round_no, 1, cards=[c],
                               item_id=item_id)
            if got:
                out.append(got[0])
                taken.add(spec_tuple(got[0]))
                break
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
def _cell_mean_tokens(views: dict | None, card: str, round_type: str,
                      cls: str | None = None) -> float | None:
    """Mean tokens per card run of the class cell; pooled over classes (weighted by card runs)
    when the class has no row or no cls is given."""
    rows = [r for r in stats_rows(views) if r.get("card") == card
            and r.get("round_type", round_type) == round_type and r.get("mean_tokens")]
    own = [r for r in rows if cls is not None and r.get("cls") == cls]
    rows = own or rows
    if not rows:
        return None
    w = sum(_weight(r) for r in rows)
    return sum(float(r["mean_tokens"]) * _weight(r) for r in rows) / w


def est_cost(spec: CardSpec, views: dict | None, benchmark: str, cls: str | None = None,
             round_type: str | None = None) -> int:
    """Cell mean tokens per card run from strategy_stats (the class cell, else pooled; a
    post_reset spec without post_reset rows uses the first-round cell), else cold start: per
    step the role max_tokens + routed-input estimate + CLI overhead (section 4 Spend accounting)."""
    round_type = round_type or ("revise" if spec.card == "revise" else "first")
    mean = _cell_mean_tokens(views, spec.card, round_type, cls)
    if mean is None and round_type == "post_reset":
        mean = _cell_mean_tokens(views, spec.card, "first", cls)
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
