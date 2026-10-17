"""Agreement probe and identity calibration (ARCHITECTURE.md section 3 /judge step 3; section 4
`probe = run_probe(P, n=n_probe)`, `agreement(probe, C)`, `calibrate(...)`; section 5 rows
"Agreement probe size" and "p_raw entry"; CTL-06, EVL-08).

The probe makes n seeded-card-like calls (role "probe") ONCE per item before round 1, with one
fixed template (strategies/templates/probe.<benchmark>.txt, rendered and linted through
run_card.render_prompt) over the key-stripped item; only the seed word differs between calls,
drawn by a replicate-seeded RNG. Each reply is parsed into one answer (ARC: program ->
predicted grid via arc_exec.predict; BT: option letter), clustered by the benchmark dedup key,
and stored as candidates with origin "probe" in run_dir/cands/probe.jsonl. Its tokens are
charged to the run; ProbeResult.calls lists every call's id and usage for the ledger.
"""
from __future__ import annotations

import random
from dataclasses import dataclass, field
from pathlib import Path

from . import config, llm
from .judge import item_data
from .schemas import Candidate, Usage, append_jsonl, new_id
from .think.dedup import dedup_key

ARM = "scaffold"
FALLBACK_SEEDS = ["river", "mirror", "ladder", "harvest", "orbit", "knot", "lantern", "tide",
                  "frame", "echo", "seed", "bridge"]


@dataclass
class ProbeResult:
    clusters: dict[str, int]            # dedup key -> number of probe calls with that answer
    n: int                              # number of probe calls (the agreement denominator)
    usage: Usage
    cands: list[Candidate] = field(default_factory=list)
    calls: list[dict] = field(default_factory=list)   # [{call_id, usage, error, seed}] per call


# ---------------------------------------------------------------- seeds and prompt
def load_seeds() -> list[str]:
    """Concept seeds from strategies/seeds/concepts.txt (cards owner), read by the same
    reader as the card runner (blank and "#" lines skipped), else a fixed fallback."""
    from .run_card import read_seed_file
    p = Path(config.SEEDS_PATH)
    words = list(read_seed_file(p)) if p.exists() else []
    return words or list(FALLBACK_SEEDS)


def probe_seeds(item_id: str, n: int, replicate: int) -> list[str]:
    """Seed words for the n probe calls, replicate-seeded (README Determinism)."""
    rng = random.Random(f"{item_id}:{ARM}:{replicate}:probe")
    pool = load_seeds()
    return rng.sample(pool, n) if n <= len(pool) else [rng.choice(pool) for _ in range(n)]


def template_for(benchmark: str) -> str:
    return f"probe.{benchmark if benchmark in ('arc', 'bt') else 'bt'}"


def prompt_values(problem, seed: str) -> dict:
    return {"problem_md": problem.problem_md, "data": item_data(problem, problem.benchmark),
            "seed": seed}


def build_prompt(problem, seed: str) -> str:
    """Fixed probe template over problem.md and the key-stripped item (Pr14), no files written."""
    from .run_card import load_template, render
    return render(load_template(template_for(problem.benchmark)), prompt_values(problem, seed))[0]


# ---------------------------------------------------------------- parsing
def parse_program(text: str) -> str | None:
    """First fenced code block defining transform(grid) (any info string, unclosed final fence
    allowed); else the text from 'def transform' on."""
    from .run_card import code_blocks
    for block in code_blocks(text):
        if "def transform" in block:
            return block.strip()
    i = (text or "").find("def transform")
    return text[i:].strip() if i >= 0 else None


def parse_letter(text: str) -> str | None:
    """Option letter of a reply: 'ANSWER: X' in any markdown dressing ('**ANSWER:** B',
    'Answer: **b**', 'Final answer - D'), else a lone-letter line, else 'the answer is X'.
    Shares the parser of the plain arm; no first-line fallback (an 'A key insight...' line is
    not an answer)."""
    from .arms.plain import parse_letter as _plain_letter
    j = _plain_letter(text or "")
    return "ABCD"[j] if j is not None else None


def _predict(program: str, test_input):
    """ARC predicted grid through the verify owner's sandboxed executor."""
    from . import arc_exec
    return arc_exec.predict(program, test_input)


def parse_answer(text: str, problem) -> tuple[str, str | None, object] | None:
    """(text, program, pred) for one probe reply, or None when no answer can be parsed."""
    if problem.benchmark == "arc":
        prog = parse_program(text)
        if prog is None:
            return None
        return prog, prog, _predict(prog, problem.item.get("test_input"))
    letter = parse_letter(text)
    return (letter, None, letter) if letter else None


# ---------------------------------------------------------------- probe
def _specs(problem, seeds, backend, log_dir, run_dir) -> list[dict]:
    """One call spec per seed; each call runs in its own sandbox calls/<call_id>/in/ (Pr1: no
    repo or git context reaches the probe)."""
    from .run_card import render_prompt, write_sandbox
    specs = []
    for i, seed in enumerate(seeds):
        cid = new_id("c")
        meta = {"benchmark": problem.benchmark, "item_id": problem.item_id, "probe_index": i,
                "seed": seed}
        values = prompt_values(problem, seed)
        prompt = render_prompt(template_for(problem.benchmark), values,
                               role="probe", run_dir=run_dir, call_id=cid, meta=meta)
        cwd = write_sandbox(Path(run_dir) / "calls", cid, values)
        specs.append(dict(prompt=prompt, role="probe", call_id=cid, backend=backend, log_dir=log_dir,
                          max_tokens=config.PARAMS["max_tokens"]["probe"], meta=meta, cwd=cwd))
    return specs


def run_probe(problem, *, n: int, backend: str, log_dir: Path, replicate: int,
              run_dir: Path) -> ProbeResult:
    """n probe calls once per item, clustered by the benchmark dedup key (CTL-06)."""
    seeds = probe_seeds(problem.item_id, n, replicate)
    results = llm.call_many(_specs(problem, seeds, backend, log_dir, run_dir))
    usage, cands, clusters, calls = Usage(), [], {}, []
    for seed, res in zip(seeds, results):
        usage = usage.add(res.usage)
        calls.append({"call_id": res.call_id, "usage": res.usage.to_dict(), "error": res.error,
                      "seed": seed})
        parsed = None if res.error else parse_answer(res.text, problem)
        if parsed is None:
            continue                                    # counts in n, joins no cluster
        text, prog, pred = parsed
        c = Candidate(id=new_id("p"), text=text, card="probe", operator="none", seed=seed, perm=0,
                      round=0, call_id=res.call_id, origin="probe", program=prog, pred=pred)
        cands.append(c)
        k = dedup_key(c, problem.benchmark)
        clusters[k] = clusters.get(k, 0) + 1
    if cands:
        append_jsonl(Path(run_dir) / "cands" / "probe.jsonl", [c.to_dict() for c in cands])
    return ProbeResult(clusters=clusters, n=len(seeds), usage=usage, cands=cands, calls=calls)


def agreement(probe: ProbeResult, cand: Candidate, benchmark: str) -> float:
    """Share of probe calls whose answer key equals the candidate's key."""
    if not probe or probe.n <= 0:
        return 0.0
    return probe.clusters.get(dedup_key(cand, benchmark), 0) / probe.n


def calibrate(agreement_value: float, p_raw: float | None, flags: dict) -> float:
    """Confidence c. P0: identity map on agreement (CTL-06). p_raw is ignored unless
    flags["p_raw_validated"] (EVL-08 gate); then a placeholder equal-weight mean is used until
    the dev-tune logistic map (calibration.json, P1) replaces it."""
    a = max(0.0, min(1.0, float(agreement_value or 0.0)))
    if p_raw is None or not (flags or {}).get("p_raw_validated", False):
        return a
    return max(0.0, min(1.0, 0.5 * a + 0.5 * float(p_raw)))
