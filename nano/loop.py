"""The HTSA loop pointed at the nano trainer ("nano arm"): generate candidate trainers with the
P0 cards, verify each with the four-rung checker (today: rungs 1-3, script-only), revise the
near misses, and leave a ranked pool of checked candidates for the full training runs.

Same invariants as harness/think.py (ARCHITECTURE.md section 4): one role per call, fresh
context per call, private defaults never routed, every call charged, candidates deduplicated,
free verification never skipped, decision log per cycle, graph written after every cycle.
Not yet merged into think.py; it reuses harness.llm, harness.ledger and harness.graph.

Usage:
  python -m nano.loop --batch nano-1 --replicate 0 --backend cli_json --budget 400000 --rounds 2
Outputs: D:/AGI-lab/runs/<batch>__nano__gpt2_50m__scaffold__r<rep>/ with cands/, verify.jsonl,
state.json, answer.json and pool/<cand_id>.py for every checked candidate.
"""
from __future__ import annotations

import argparse
import hashlib
import math
import json
from collections import Counter
import random
import re
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
from harness import config, llm                                   # noqa: E402
from harness.schemas import Candidate, LedgerRow, Usage, append_jsonl, new_id, now_ts, write_json  # noqa: E402
from nano import profile as PF                                      # noqa: E402
from nano import deepen, ideate                                             # noqa: E402
from nano import tree                                               # noqa: E402
from nano import research                                           # noqa: E402
from nano import version as nano_version                            # noqa: E402
from nano import budget as budget_mod                               # noqa: E402
from nano import predict                                            # noqa: E402
from nano import novelty as NV                                      # noqa: E402
from nano import controls as CT                                     # noqa: E402
from nano import memory as MEM                                      # noqa: E402


class StopRun(Exception):
    """Raised at a stage boundary when control.json asks the run to stop."""

# Everything problem-specific comes from the active profile (nano/profile.py, nano/profiles/<name>.py,
# docs/GENERIC_SPEC.md): the constraints, the design assumptions, the builder's reply format, the baseline
# artifact, the problem statement, the reference docs and the checker. The old module constants BASELINE,
# SPEC_ID, CONSTRAINTS, ASSUMPTIONS and OUTPUT_FORMAT stay readable (module __getattr__ at the end of the file).

# The builder's reply format for a profile that brings none of its own; {v:key} is filled from its vocab.
_GENERIC_OUTPUT_FORMAT = """Reply in exactly this form:
HYPOTHESIS: <one sentence: what you change and why it should give {v:score_phrase}>
CHANGE: <one line naming the components touched>
FIDELITY: <exact | partial | substituted | cannot, then one clause: exact = the idea as specified; partial = a piece left out, say which; substituted = a different mechanism with the same aim, say what; cannot = it could not be built within the rules, say why (then return the file unchanged)>
```{v:language}
<the COMPLETE modified {v:artifact_file}, every line, ready to run>
```
Keep everything not related to your change identical to the given file."""


def baseline_path() -> Path:
    """The baseline artifact the builders modify (profile artifact.path, relative to the repo root). A profile
    without a baseline (Mode 2 or 3) gives its skeleton file instead, or None when it has none."""
    art = PF.current().artifact
    if not art.get("path"):
        return (ROOT / art["skeleton"]) if art.get("skeleton") else None
    return ROOT / art["path"]


def run_mode() -> str:
    """The active profile's mode: baseline, check_only or no_check (docs/GENERIC_SPEC.md section 6)."""
    return PF.current().mode


def start_text() -> str:
    """What builders start from when there is no baseline: the skeleton file, else the interface text."""
    pf = PF.current()
    return pf.skeleton_text() or pf.interface


def spec_id() -> str:
    """Run-folder and ledger item id: 'gpt2_50m' for the LLM profile, else the profile name."""
    return str(PF.current().get("spec_id") or PF.current().name)


def constraints() -> list[str]:
    return list(PF.current().constraints)


def output_format() -> str:
    return PF.fill(PF.current().artifact.get("output_format") or _GENERIC_OUTPUT_FORMAT)


def _doc_path(key: str) -> Path | None:
    rel = (PF.current().docs or {}).get(key)
    return (ROOT / rel) if rel else None


def _doc_text(key: str) -> str:
    """A reference document named by the profile ('' when the profile names none or the file is missing)."""
    path = _doc_path(key)
    try:
        return path.read_text(encoding="utf-8") if path else ""
    except OSError:
        return ""


def _fence() -> str:
    return "```" + PF.current().v("language", "")


def _artifact_word() -> str:
    """'SCRIPT' for the LLM profile: the word the prompts use for the file being changed."""
    return PF.current().v("artifact_short", "") or PF.current().v("artifact", "artifact")


class CheckerAdapter:
    """One call surface over the profile's checker. New checkers follow the protocol in nano/checks/base.py
    (baseline_profile, check, long_run, final); the LLM checker also keeps the older names of nano/check.py
    (refresh_profile, fidelity_probe, LEARN_STEPS, LONG_STEPS). Keyword arguments a checker does not take are
    dropped, so the loop can pass the LLM knobs (learn_steps, long_steps) to any checker."""

    def __init__(self, impl, name: str):
        self.impl, self.name = impl, name

    def __getattr__(self, key):
        return getattr(self.impl, key)

    @staticmethod
    def _call(fn, *args, **kw):
        import inspect
        try:
            sig = inspect.signature(fn)
        except (TypeError, ValueError):
            return fn(*args, **kw)
        if not any(p.kind is p.VAR_KEYWORD for p in sig.parameters.values()):
            kw = {k: v for k, v in kw.items() if k in sig.parameters}
        return fn(*args, **kw)

    def _const(self, *names, default: int = 0) -> int:
        for n in names:
            v = getattr(self.impl, n, None)
            if isinstance(v, (int, float)) and not isinstance(v, bool):
                return int(v)
        return default

    @property
    def LEARN_STEPS(self) -> int:                    # noqa: N802 (the old module constant's name)
        return self._const("LEARN_STEPS", "learn_steps", default=1)

    @property
    def LONG_STEPS(self) -> int:                     # noqa: N802
        return self._const("LONG_STEPS", "long_steps", default=1)

    @property
    def PROFILE_SEEDS(self) -> tuple:                # noqa: N802
        return tuple(getattr(self.impl, "PROFILE_SEEDS", None) or (0, 1, 2))

    def baseline(self, profile_dir: Path, baseline_file: Path, seeds=None, **kw) -> dict:
        if hasattr(self.impl, "refresh_profile"):
            return self._call(self.impl.refresh_profile, profile_dir, **kw)
        return self._call(self.impl.baseline_profile, baseline_file, profile_dir,
                          seeds if seeds is not None else (0, 1, 2), **kw)

    def check(self, candidate: Path, out: Path, baseline: dict, **kw) -> dict:
        return self._call(self.impl.check, candidate, out, baseline, **kw)

    def long_run(self, candidate: Path, out: Path, baseline: dict, **kw) -> dict:
        return self._call(self.impl.long_run, candidate, out, baseline, **kw)

    def fidelity_probe(self, candidate: Path, out: Path, baseline: dict, target: str, **kw) -> dict | None:
        fn = getattr(self.impl, "fidelity_probe", None)
        return self._call(fn, candidate, out, baseline, target, **kw) if fn else None

    def final(self, candidate: Path, out: Path, baseline: dict, seeds, **kw) -> dict:
        """The full test (rung 5) for both kinds of checker; the loop itself does not call it today."""
        return self._call(self.impl.final, candidate, out, baseline, seeds, **kw)

    def measure_reference(self, candidate: Path, out: Path, seeds=None, **kw) -> dict:
        """Mode 2 and 3: the checker's baseline_profile run on the chosen reference candidate (never the
        LLM checker's refresh_profile, which always measures its own fixed baseline)."""
        return self._call(self.impl.baseline_profile, candidate, out,
                          seeds if seeds is not None else self.PROFILE_SEEDS, **kw)


def make_checker(profile=None) -> CheckerAdapter:
    """The checker the profile names (nano/checks/<name>.py via nano.checks.get_checker). Until nano.checks
    exists, the LLM profile falls back to the module-level functions of nano/check.py."""
    pf = profile or PF.current()
    try:
        from nano.checks import get_checker
    except ImportError as e:
        if pf.checker != "llm":
            raise SystemExit(f"profile {pf.name!r} needs checker {pf.checker!r}, but nano.checks is not importable: {e}")
        from nano import check as legacy
        return CheckerAdapter(legacy, "llm (nano.check module)")
    return CheckerAdapter(get_checker(pf), str(pf.checker))


def _norm_source(src: str) -> str:
    lines = []
    for ln in src.splitlines():
        s = ln.split("#", 1)[0].rstrip()
        if s.strip():
            lines.append(re.sub(r"\s+", " ", s))
    return "\n".join(lines)


def _strip_comments(src: str) -> str:
    out = []
    in_doc = False
    for ln in src.splitlines():
        s = ln.strip()
        if s.startswith('"""') or s.startswith("'''"):
            if s.count('"""') == 2 or s.count("'''") == 2:
                continue
            in_doc = not in_doc
            continue
        if in_doc:
            continue
        if s.startswith("#"):
            continue
        out.append(ln.split("  #", 1)[0].rstrip())
    return "\n".join(out)


def _seeds() -> list[str]:
    p = config.SEEDS_PATH
    if p.exists():
        return [w.strip() for w in p.read_text(encoding="utf-8").splitlines() if w.strip()]
    return ["river", "lantern", "harbor", "glacier", "orchard", "compass", "anvil", "meadow"]


def _parse(text: str) -> dict | None:
    m = re.search(r"HYPOTHESIS:\s*(.+)", text)
    c = re.search(r"CHANGE:\s*(.+)", text)
    f = re.search(r"FIDELITY:\s*(exact|partial|substituted|cannot)\b[\s,:;-]*(.*)", text, flags=re.I)
    blocks = re.findall(r"```(?:[\w+-]+)?\s*\n(.*?)```", text, flags=re.S)
    if not blocks:
        return None
    src = max(blocks, key=len)
    if any(mark not in src for mark in (PF.current().artifact.get("must_contain") or [])):
        return None
    return {"hypothesis": (m.group(1).strip() if m else ""), "change": (c.group(1).strip() if c else ""),
            "source": src, "fidelity": (f.group(1).lower() if f else ""), "fidelity_note": (f.group(2).strip()[:200] if f else "")}


_UPWARD_KEYS = (("PROPOSAL", "proposal", 200), ("REFRAMING", "reframing", 600), ("NEW MEASURE", "new_measure", 600),
                ("WHY", "why", 400), ("COST", "cost", 400))


def parse_upward(text: str, *, round_no: int, call_id: str, idgen) -> list[dict]:
    """An upward reply in tree.UPWARD_FORMAT -> proposal records {id, proposal, reframing, new_measure, why, cost,
    round, call_id}. A block counts when it has a PROPOSAL and at least a REFRAMING or a NEW MEASURE."""
    text = str(text or "").replace("**", "")
    keys = "|".join(k for k, _, _ in _UPWARD_KEYS)
    out = []
    for block in re.split(r"(?=^[ \t>*-]*PROPOSAL\s*:)", text, flags=re.M):
        f = {}
        for key, name, cap in _UPWARD_KEYS:
            m = re.search(rf"^[ \t>*-]*{key}\s*:\s*(.+?)(?=\n[ \t>*-]*(?:{keys})\s*:|\Z)", block, flags=re.S | re.M)
            if m:
                f[name] = " ".join(m.group(1).split())[:cap]
        if f.get("proposal") and (f.get("reframing") or f.get("new_measure")):
            out.append({"id": idgen(), **{name: f.get(name, "") for _, name, _ in _UPWARD_KEYS},
                        "round": round_no, "call_id": call_id})
    return out


def keep_upward(capped: list, ups: list) -> list:
    """After the test-mode cap: the root's upward contexts sort last (prio 3, one part among many), so a cap at or
    below the number of parts drops them all (arch-2: capped to 24, all research and diagnosis, none upward). When any context is
    dealt, one upward context stays, in place of the last non-owner context."""
    if not ups or not capped or any(sp[3] == "upward" for sp in capped):
        return capped
    out = list(capped)
    drop = next((i for i in range(len(out) - 1, -1, -1) if out[i][0] != "owner"), None)
    if drop is None:
        out.append(ups[0])
    else:
        out[drop] = ups[0]
    return out


class NanoLoop:
    mode = "baseline"                           # class default; __init__ sets the profile's mode

    def __init__(self, batch: str, replicate: int, backend: str, budget: int, rounds: int,
                 smoke_seconds: float, model: str | None):
        self.batch, self.rep, self.backend, self.B, self.rounds = batch, replicate, backend, budget, rounds
        self.smoke, self.model = smoke_seconds, model
        self.pf = PF.current()                  # the problem profile (nano/profiles/<name>.py)
        self.checker = make_checker(self.pf)    # the profile's checker (nano/checks/<name>.py)
        self.run_id = f"{batch}__nano__{spec_id()}__scaffold__r{replicate}"
        self.run_dir = config.RUNS_DIR / self.run_id
        for d in ("calls", "prompts", "cands", "cands/src", "private", "pool"):
            (self.run_dir / d).mkdir(parents=True, exist_ok=True)
        self.rng = random.Random(f"nano:{spec_id()}:{replicate}")
        self.spent = 0                          # the inventing model's tokens: what the budget B governs
        self.spent_aux = 0                      # the cheap model's retrieval and clerical tokens: metered apart
        self.aux_budget = 10 * budget           # past it the run stops searching the web and goes on with what it has
        self._aux_off_logged = False
        self.cands: list[Candidate] = []
        self.vres: dict[str, dict] = {}
        self.seen: dict[str, str] = {}
        self.decisions: list[dict] = []
        self.mode = self.pf.mode                # baseline | check_only | no_check (docs/GENERIC_SPEC.md section 6)
        self.baseline_src = (baseline_path().read_text(encoding="utf-8") if self.mode == "baseline"
                             else start_text())   # no baseline: the skeleton (or the interface) is the starting text
        self.profile: dict = {}                 # filled by refresh_profile at run start
        self.reference: dict | None = None      # Mode 2/3: the best checked candidate so far {cand_id, path, metrics}
        self.reference_log: list[dict] = []     # every time the reference was set or moved
        self.retest_on_reference_change = False # Mode 2/3: re-check the top three when the reference moves
        if hasattr(self.checker.impl, "set_caller"):
            self.checker.impl.set_caller(self._judge_call)   # Mode 3: the panel's judges go through self._call
        self.used_seeds: set[str] = set()
        self.lock = threading.Lock()
        self.inflight: dict[str, dict] = {}
        self.phase = "starting"
        self.note = ""
        self.sketches: list[dict] = []          # ideation stage (nano/ideate.py)
        self.clusters: list[dict] = []
        self.deepen_nodes: list[dict] = []     # interrogation chains (nano/deepen.py)
        self.deepen_depth, self.deepen_fanout, self.do_deepen = 2, 1, True
        self.deepen_top, self.deepen_generations = 12, 1   # ideas interrogated per generation; extra generations
        self.implemented: set[str] = set()      # sketch ids whose cluster has an implementation
        self.n_ideate = 12                      # (legacy knob; the tree sets contexts per node)
        self.k_impl = 6                         # implementation slots in round 1 (a third later)
        self.tree: list[dict] | None = None     # problem tree (nano/tree.py)
        self.per_node = 1                       # ideation contexts per node x direction in round 1
        self.inward_share = 0.6                 # share of implementation slots for inward ideas
        self.off_tree_share = 0.4               # share of idea contexts that work off the map (blank, gaps, doubt); 0 = off
        self.source_yield: list[dict] = []      # per round: yield per origin (tree / off) and the share chosen next
        self.promoted: set[str] = set()         # off-map winners already turned into branches
        self.contexts_by_node: dict[int, dict[str, int]] = {}   # round -> idea contexts (inward/outward) per part; weights the build slots
        self.human_nodes_seen: set[str] = set() # control.json add_nodes ids already put on the map
        self.plan_with_model = True             # one planner call refines DEFAULT_TREE
        self.upward: list[dict] = []            # root-level reframing proposals (logged only)
        self.briefs: dict[str, dict] = {}       # web research briefs per node (nano/research.py)
        self.do_research = True
        self.research_model = "sonnet"          # retrieval, not invention: the cheap model is fine
        self.cheap_model = "sonnet"             # planner and blind clustering: mechanical roles
        self.ideation_web = True                # sketch contexts may search the web (WebSearch, WebFetch)
        self.web_mode = "delegate"              # delegate: the model asks, the research model searches; self: it searches itself; off
        self.research_max_age_days = 7.0
        self.learn_steps, self.long_steps = self.checker.LEARN_STEPS, self.checker.LONG_STEPS
        self.new_share = 0.5                    # quota of build slots for ideas tagged new
        self.select_weights: dict = {}          # overrides for ideate.WEIGHTS
        self.defaults_lines: list[str] = []     # the private obvious answers (tagging only, never routed)
        self.history: list[dict] = []           # what was built and what happened (fed to later rounds)
        self.interrogated: set[str] = set()     # sketch ids whose cluster was interrogated (persists across rounds)
        self.arm = "scaffold"                   # scaffold | plain | climb (control arms, same ladder and budget)
        self.n_builds = 12                      # builds for the control arms
        self.lens = DEFAULT_LENS                # how the planner draws the map (tree.LENSES); a factor apart from the replicate
        self.lens_design = "fixed"              # fixed = same lens every replicate; by_replicate = --lens-by-replicate
        self.immediate_fix = True               # one same-round fix for rung 0/1 failures
        self.baseline_version = nano_version.baseline_version()
        self.working_src = self.baseline_src    # what direct-build cards see (climb arm advances it)
        self.analogies: dict[str, dict] = {}    # structured analogies per part (nano/research.py)
        self.do_analogy, self.do_diagnostics, self.do_premortem = True, True, True
        self.diagnostics_text = ""              # how the baseline behaves (nano/diagnose.py), fed to agents
        self.max_compose = 3                    # mechanical composites per round (nano/compose.py)
        self.control_note = ""                  # a note from control.json that every later agent reads
        self.skip_nodes: set[str] = set()       # parts excluded by control.json
        self.only_nodes: set[str] = set()       # test mode: only these parts take part (the rest are skipped)
        self.aim = ""                           # the purpose behind the goal, read by every agent (problem.md PURPOSE)
        self.digest_file: Path | None = _doc_path("digest")   # what the strongest open models do now (profile docs.digest)
        self.digest_text = ""
        self.exclude_clusters: set[str] = set() # cluster names excluded by control.json
        self.resume = False
        self.completed_rounds = 0
        self.stop_after = None                  # a stage name: the run stops cleanly after it (test mode)
        self.max_sketch_calls = 0               # cap on idea-sketch agents per round (0 = all; test mode)
        self.diag_steps = 100
        # --- evidence-driven settings (research_notes/idea_generation/00_SYNTHESIS.md)
        self.controls: list[str] | None = ["placebo_order", "zero_init_proj", "lr_x10"]   # ladder controls each run
        self.longshot_share = 0.3               # build slots drawn at random from leap / step-outside / analogy / new clusters
        self.leap_share = 0.25                  # quota: share of each sketch call that must be leaps (0 = off)
        self.anomaly_seeds = 3                  # diagnostics seeds for the anomaly map (1 = no map)
        self.sham_share = 0.1                   # chance that the anomaly rows carry one fabricated row (chasing is measured)
        self.anomaly_text, self.anomalies = "", {}
        self.cost_card = ""                     # computed cost and headroom of the recipe, shown to every agent
        self.seeds_file: str = ""               # owner-written seed mechanisms, one or more per part
        self.owner_seeds: list[dict] = []
        self.family_variants = 2                # near-miss variants built per round from the ambitious lane
        self.tune = True                        # scripted single-knob tuning sweep up the ladder at round 1
        self.effort_by_role = True              # reasoning effort per role (CLI backend)
        self.fact_check = True                  # numeric web claims are checked against their page before a build
        self.stage_shares = dict(budget_mod.SHARES)  # token envelopes per stage; the build share is a protected floor
        self.spent_by_stage: dict[str, int] = {}
        self.round_now = 0
        self._manifest: dict[str, dict] = {}    # per cluster: what its builder saw
        self._control_hash = ""
        self._control_applied: set = set()
        self.tune_knobs: list[str] = []         # empty = nano/tune.py DEFAULT
        self.tune_top = 3                       # tuning candidates kept for the long run and the night
        self.family_queue: list[tuple] = []
        self._leap_counter: dict[str, int] = {}  # per part: which leap operator the next context gets
        self.novelty_threshold = 0.45           # TF-IDF cosine above which a chosen idea is a near-duplicate of a build (paraphrases score ~0.5, unrelated ideas < 0.2)
        self.novelty_audit = 0.1                # share of near-duplicates built anyway, to measure the gate
        self.retire_cards = True                # cards whose sketches keep landing in the same clusters are retired
        self.retired_cards: set[str] = set()
        self.discovery: list[dict] = []
        self.staged_sketch = False              # arm: terse seeds -> bolder -> elaborate, inside one call
        self.exclusion_list = False             # arm: later rounds see the cluster names already covered
        self.cross_family_share = 0.0           # arm: share of sketch contexts sent to the cheap model
        self.premortems = 1                     # independent pre-mortems per interrogated idea (1-3)
        self.identity_init = False              # arm: builders wrap new paths as x + tanh(a) f(x), a = 0
        self.replan = False                     # arm: re-plan the map between rounds from the ledger
        self.weights_from_ledger = False        # selection weights from nano/calibrate.py when enough builds exist
        self.hedge_share = 0.0                  # share of rung-3 gap failures promoted anyway (lane "hedge")
        self.fidelity = True                    # diagnostics on checked candidates: did the named cell move?
        self.program_search: str | None = None  # arm: evolve one named function with continuous fitness
        self.program_k = 4
        self.adapt_card = True                  # port-and-adapt contexts (known techniques, adaptation moves)
        self.contradiction_cards = True         # contexts seeded with measured gain-versus-cost trade-offs
        self.hedged: set[str] = set()
        self.ledger_texts: dict[str, str] = {}  # hypotheses from earlier runs, for the novelty gate
        self.hash_memory: dict = self._load_hash_memory()
        # per-part persistent memory (nano/memory.py; research_notes/team_gaps/02_persistent_expertise.md)
        self.use_memory = True                  # False = the control arm (--no-memory): no block, no curation, no files
        self._memory: MEM.Memory | None = None
        self.memory_free: set[int] = set()      # id() of this round's ignores-memory contexts, one per part
        self.memory_stats = {"parts": set(), "entries_added": 0, "entries_rejected": 0}
        self._cluster_cache: dict[tuple, list[dict]] = {}   # (node, direction, frozenset(sketch ids)) -> groups
        self._tag_cache: dict[tuple, tuple] = {}             # (node, frozenset(members)) -> (prior, match, source)

    # ------------------------------------------------------------ web research per part
    def research_round(self, round_no: int) -> None:
        """One research call per part (web search + fetch enabled), cached under memory/research."""
        cache = config.MEMORY_DIR / "research"
        goal_md = (self.run_dir / "problem.md").read_text(encoding="utf-8")
        nodes = [n for n in (self.tree or []) if n["id"] != "root" and not self._skipped(n["id"])]
        (self.run_dir / "research").mkdir(exist_ok=True)

        def _one(node):
            cached = research.load_cached(cache, node["id"], self.research_max_age_days)
            if cached:
                return node["id"], cached, "cache"
            if not self._aux_ok("research brief: " + node["name"]):
                return node["id"], None, "skipped"
            prompt = research.research_prompt(node, goal_md)
            cid = new_id("c")
            (self.run_dir / "prompts" / f"{cid}.txt").write_text(prompt, encoding="utf-8")
            with self.lock:
                self.inflight[cid] = {"call_id": cid, "role": "research", "card": "research", "operator": node["id"],
                                      "seed": "", "started": time.time(), "note": f"web search: {node['name']}"}
            self._live()
            try:
                r = llm.call(prompt, role="research", call_id=cid, model=self.research_model, max_tokens=4000,
                             backend=self.backend, log_dir=self.run_dir / "calls",
                             meta={"card": "research", "operator": node["id"], "note": f"web search: {node['name']}"},
                             tools=research.RESEARCH_TOOLS, max_turns=40, timeout=1800)
            finally:
                with self.lock:
                    self.inflight.pop(cid, None)
            self._account(self.research_model, {"card": "research"}, r.usage)
            self._live()
            self._ledger("research", node["id"], "", r.call_id, r.usage, round_no, "encode")
            brief = research.parse_brief(r.text or "", node["id"])
            if brief:
                brief["backend"] = self.backend
                if self.backend != "mock":           # mock briefs never enter the shared cache
                    research.save_cache(cache, brief)
            return node["id"], brief, "web"

        with ThreadPoolExecutor(max_workers=4) as ex:
            for node_id, brief, src in ex.map(_one, nodes):
                if brief:
                    self.briefs[node_id] = brief
                    write_json(self.run_dir / "research" / f"{node_id}.json", {**brief, "source": src})
        if self.do_analogy:
            with ThreadPoolExecutor(max_workers=4) as ex:
                for node_id, an, src in ex.map(self._analogy_one, [(n, goal_md, cache, round_no) for n in nodes]):
                    if an:
                        self.analogies[node_id] = an
                        write_json(self.run_dir / "research" / f"{node_id}_analogy.json", {**an, "source": src})
        self.inject_ledger(nodes)
        self._live(note=f"research briefs: {len(self.briefs)}/{len(nodes)} parts")

    def _analogy_one(self, spec) -> tuple:
        """Structured analogies for one part: problems of the same shape in other fields, with sources."""
        node, goal_md, cache, round_no = spec
        cached = research.load_cached(cache, node["id"] + "_analogy", self.research_max_age_days)
        if cached:
            return node["id"], cached, "cache"
        if not self._aux_ok("analogies: " + node["name"]):
            return node["id"], None, "skipped"
        prompt = research.analogy_prompt(node, goal_md)
        r = self._call(prompt, "research", 4000, {"card": "analogy_research", "operator": node["id"],
                                                  "note": f"analogies in other fields: {node['name']}"},
                       model=self.research_model, tools=research.RESEARCH_TOOLS, max_turns=40, timeout=1800)
        self._ledger("analogy_research", node["id"], "", r.call_id, r.usage, round_no, "encode")
        an = research.parse_analogies(r.text or "", node["id"] + "_analogy")
        if an:
            an["backend"] = self.backend
            if self.backend != "mock":
                research.save_cache(cache, an)
        return node["id"], an, "web"

    def inject_ledger(self, nodes: list[dict]) -> None:
        """Previous overnight verdicts (this baseline version) go to EVERY part's brief as known / failed
        entries and a "tried before" block: planner-made part ids differ between runs."""
        ledger = config.MEMORY_DIR / "experiments" / "ledger.jsonl"
        known, failed = research.ledger_entries(ledger, None, self.baseline_version)
        if not (known or failed):
            return
        tried = ([{"name": e["name"], "why": e.get("effect", ""), "url": e["url"]} for e in known]
                 + [{"name": e["name"], "why": e.get("why", ""), "url": e["url"]} for e in failed])
        for node in nodes:
            b = self.briefs.setdefault(node["id"], {"node": node["id"], "known": [], "failed": [], "open": [], "queries": []})
            b["known"] = [e for e in b.get("known", []) if not str(e.get("url", "")).startswith("ledger://")] + known
            b["failed"] = [e for e in b.get("failed", []) if not str(e.get("url", "")).startswith("ledger://")] + failed
            b["tried"] = tried
            cur = json.loads((self.run_dir / "research" / f"{node['id']}.json").read_text(encoding="utf-8")) \
                if (self.run_dir / "research" / f"{node['id']}.json").exists() else {}
            write_json(self.run_dir / "research" / f"{node['id']}.json",
                       {**b, "source": (cur.get("source") or "none") + "+ledger", "ledger_entries": len(known) + len(failed)})

    # ------------------------------------------------------------ ideation stage
    PROGRAM_FAMILIES = ("the structure: a different functional form or a branch that did not exist",
                        "the conditions: when the behaviour switches (phases, thresholds)",
                        "the input: what measured quantity it reads to decide (step, loss, gradient norm, update size)",
                        "the composition: two simpler behaviours combined")

    def _program_family(self, seed: str) -> str:
        """Each parallel program-search variation is told a different thing to change, so they differ by construction."""
        i = int(seed) if str(seed).strip().isdigit() else 0
        return self.PROGRAM_FAMILIES[i % len(self.PROGRAM_FAMILIES)]

    IDEA_CARDS = ("seeded", "low_prior", "transform", "formal", "docs")

    def sketch_prompt(self, card: str, seed: str, operator: str) -> str:
        if card == "seeded":
            return self._common(self.baseline_src, True, "sk:" + seed) + f"Starting point: {seed}\n\n" + ideate.SKETCH_FORMAT
        if card == "low_prior":
            return (self._common(_strip_comments(self.baseline_src), True, "sk:low:" + seed)
                    + f"The {_artifact_word()} above is given without its comments.\n\n" + ideate.SKETCH_FORMAT)
        if card == "transform":
            return (self._common(self.baseline_src, True, "sk:" + operator)
                    + f"The current {_artifact_word()} assumes that {operator}. Sketch ideas that hold under the opposite "
                      f"assumption, keeping every constraint.\n\n" + ideate.SKETCH_FORMAT)
        if card == "docs":
            digest = _doc_text("reference")
            return (self._common(self.baseline_src, True, "sk:docs:" + seed)
                    + PF.fill("REFERENCE MATERIAL ({v:reference_what}; {v:reference_use}):\n\n")
                    + digest + "\n\n" + ideate.SKETCH_FORMAT)
        return self._common(self.baseline_src, False) + ideate.SKETCH_FORMAT      # formal

    # ------------------------------------------------------------ problem tree (nano/tree.py)
    def plan_tree(self, round_no: int) -> None:
        """One planner call refines the default tree; fallback is the hand-written DEFAULT_TREE."""
        nodes = None
        if self.plan_with_model:
            goal = (self.run_dir / "problem.md").read_text(encoding="utf-8")
            r = self._call(tree.planner_prompt(goal, self.baseline_src, self.lens, self.diagnostics_text), "encode", 2500,
                           {"card": "plan", "note": "decomposing the problem into parts"})   # the strong model: the map decides what the search can see
            self._ledger("plan", "none", "", r.call_id, r.usage, round_no, "encode")
            nodes = tree.parse_planner(r.text or "")
        import copy
        self.tree = nodes or copy.deepcopy(tree.DEFAULT_TREE)
        unresolved = sorted(o for o in (self.only_nodes or ()) if nodes and not tree.resolve_scope({o}, nodes))
        if unresolved:
            # repair before falling back: one re-ask that names the unmapped default parts and asks only for "refines"
            r = self._call(tree.repair_prompt(unresolved, nodes), "encode", 2500,
                           {"card": "plan_repair", "note": "mapping the planned parts onto the default parts"})
            self._ledger("plan_repair", "none", "", r.call_id, r.usage, round_no, "encode")
            fixed = tree.parse_planner(r.text or "") or []
            by_id = {n["id"]: n.get("refines") for n in fixed}
            by_name = {n["name"].lower(): n.get("refines") for n in fixed}
            for n in nodes:
                ref = by_id.get(n["id"]) or by_name.get(n["name"].lower())
                if ref and ref != "new" and n["id"] not in ("root", "recipe"):
                    n["refines"] = ref
            still = sorted(o for o in self.only_nodes if not tree.resolve_scope({o}, nodes))
            self.decisions.append({"round": round_no, "step": "plan_repair", "scope_unresolved": unresolved,
                                   "still_unresolved": still, "repair_parsed": bool(fixed)})
        if self.only_nodes and nodes and not tree.resolve_scope(self.only_nodes, nodes):
            # the planner's names no longer match the requested parts: keep the default map, whose ids are known
            self.decisions.append({"round": round_no, "step": "plan", "scope_unresolved": sorted(self.only_nodes),
                                   "planned_ids": [n["id"] for n in nodes], "fallback": "default tree"})
            self.tree = copy.deepcopy(tree.DEFAULT_TREE)
        self._ensure_off_node()
        self._write_tree()

    def _ensure_off_node(self) -> None:
        """The off-map pseudo-node, when the share is on and the run is not restricted to some parts."""
        if self.off_tree_share > 0 and not self.only_nodes and self.tree is not None \
                and not any(n["id"] == tree.OFF_TREE_NODE["id"] for n in self.tree):
            import copy
            self.tree.append(copy.deepcopy(tree.OFF_TREE_NODE))

    def _origin_stats(self) -> dict:
        """Yield per origin: contexts, sketches, distinct clusters, built, checked and wins for ideas that came
        from a branch of the map (tree) and for ideas that came from off the map (off)."""
        out = {}
        for origin in ("tree", "off"):
            sk = [s for s in self.sketches if s.get("origin", "tree") == origin]
            ids = {s["id"] for s in sk}
            built = [c for c in self.cands if not c.card.startswith("control")
                     and (("off" if (c.extra or {}).get("node") == tree.OFF_TREE_NODE["id"] else "tree") == origin)
                     and (c.extra or {}).get("node") not in ("tune", "control", "program")]
            checked = [c for c in built if self.vres.get(c.id, {}).get("status") == "checked"]
            wins = [c for c in checked if self._gain(c) is not None and self._gain(c) < 0]
            ctx = len({s.get("call_id") for s in sk if s.get("call_id")})
            out[origin] = {"contexts": ctx, "sketches": len(sk),
                           "clusters": sum(1 for c in self.clusters if any(m in ids for m in c["members"])),
                           "built": len(built), "checked": len(checked), "wins": len(wins)}
            out[origin]["clusters_per_context"] = round(out[origin]["clusters"] / max(1, ctx), 3)
            out[origin]["wins_per_context"] = round(len(wins) / max(1, ctx), 3)
        # shares of build slots (main and long-shot lanes) and of idea contexts dealt, per origin, over all rounds
        off_id = tree.OFF_TREE_NODE["id"]
        slots = Counter("off" if (c.extra or {}).get("node") == off_id else "tree" for c in self.cands
                        if (c.extra or {}).get("lane") in ("main", "longshot"))
        dealt = Counter()
        for per in self.contexts_by_node.values():
            for nid, v in per.items():
                dealt["off" if nid == off_id else "tree"] += v
        for origin in ("tree", "off"):
            out[origin]["slot_share"] = round(slots[origin] / max(1, sum(slots.values())), 3)
            out[origin]["context_share"] = round(dealt[origin] / max(1, sum(dealt.values())), 3)
        return out

    def _gain(self, c) -> float | None:
        m = self.vres.get(c.id, {}).get("metrics") or {}
        return m.get("learn_z") if m.get("learn_z") is not None else m.get("learn_gap")

    def _shift_off_share(self, round_no: int) -> None:
        """Rule 3 of 'a map, not a fence': if off-map contexts yield more than on-map ones, the next round sends
        more contexts off the map; if less, fewer. Wins decide when there are any; cluster yield otherwise."""
        st = self._origin_stats()
        t, o = st["tree"], st["off"]
        key = "wins_per_context" if (t["wins"] or o["wins"]) else "clusters_per_context"
        before = self.off_tree_share
        if o["contexts"] >= 2 and t["contexts"] >= 2:
            if o[key] > t[key] * 1.1:
                self.off_tree_share = min(0.6, round(self.off_tree_share + 0.1, 2))
            elif o[key] < t[key] * 0.9:
                self.off_tree_share = max(0.2, round(self.off_tree_share - 0.05, 2))
        rec = {"round": round_no, "by": key, "tree": t, "off": o, "share_before": before, "share_next": self.off_tree_share}
        self.source_yield.append(rec)
        write_json(self.run_dir / "source_yield.json", {"rounds": self.source_yield})
        if self.off_tree_share != before:
            self.decisions.append({"round": round_no, "step": "off_tree_share", "from": before, "to": self.off_tree_share, "by": key})

    def _promote_off_wins(self, round_no: int) -> None:
        """Rule 4: an off-map idea that passed its checks with a gain becomes a branch of the map."""
        for c in self.cands:
            if (c.extra or {}).get("node") != tree.OFF_TREE_NODE["id"] or c.id in self.promoted:
                continue
            if self.vres.get(c.id, {}).get("status") != "checked" or self._gain(c) is None or self._gain(c) >= 0:
                continue
            members = set(c.extra.get("members") or [])          # the part the winning sketch named, else the root
            part = next((s.get("part") for s in self.sketches if s.get("id") in members and s.get("part")), "")
            node = tree.promote_win(self.tree, c.id, c.extra.get("cluster", ""), c.extra.get("hypothesis", ""), c.extra.get("change", ""),
                                    part=part or c.extra.get("node", ""))
            self.promoted.add(c.id)
            if node:
                self.decisions.append({"round": round_no, "step": "promote_off_win", "candidate": c.id, "node": node["id"], "name": node["name"],
                                       "parent": node["parent"]})

    def _spawn_fail_questions(self, round_no: int, failed: list) -> None:
        """Maintenance (docs/mapper/03): a final failed check with a reason becomes a child question under the
        node the idea worked on, at most tree.FAIL_QUESTIONS_PER_PART per node per round; same name is skipped."""
        made: Counter = Counter()
        for c in failed:
            rec = self.vres.get(c.id) or {}
            reason = str((rec.get("feedback") or {}).get("reason") or "").strip()
            nid = (c.extra or {}).get("node")
            if rec.get("status") != "fail" or not reason or nid in (None, "root", tree.OFF_TREE_ID) \
                    or not any(n["id"] == nid for n in self.tree or []) or made[nid] >= tree.FAIL_QUESTIONS_PER_PART:
                continue
            node = tree.add_failure_question(self.tree, nid, c.id, c.extra.get("cluster") or c.extra.get("hypothesis", ""), reason)
            if node:
                made[nid] += 1
                self.decisions.append({"round": round_no, "step": "fail_question", "candidate": c.id, "node": node["id"],
                                       "parent": nid, "name": node["name"]})

    def _write_tree(self) -> None:
        for d in tree.enforce_depth(self.tree):          # depth <= 4: a deeper node moves up to its depth-3 ancestor
            self.decisions.append({"round": self.round_now, **d})
        stats = []
        for n in self.tree:
            sk = [s for s in self.sketches + self.upward if s.get("node") == n["id"]]
            cl = [c for c in self.clusters if c.get("node") == n["id"]]
            impl = [c for c in self.cands if (c.extra or {}).get("node") == n["id"]]
            checked = [c for c in impl if self.vres.get(c.id, {}).get("status") == "checked"]
            per_dir = {d: {"sketches": sum(1 for s in sk if s.get("direction") == d),
                           "clusters": sum(1 for c in cl if c.get("direction") == d),
                           "implemented": sum(1 for c in impl if (c.extra or {}).get("direction") == d),
                           "checked": sum(1 for c in checked if (c.extra or {}).get("direction") == d)}
                       for d in n["directions"]}
            ia = tree.idea_assumptions(n)
            per_dir["n_idea_assumptions"] = len(ia)
            row = {**{k: v for k, v in n.items() if k != "assumptions_added"}, "assumptions": list(n.get("assumptions", [])),
                   "idea_assumptions": list(ia), "refines": n.get("refines", "new"), "stats": per_dir}
            if "upward" in n.get("directions", []):    # proposals for a new verifier, shown where people can read and vote
                row["proposals"] = [{k: u.get(k, "") for k in ("id", "proposal", "reframing", "new_measure", "why", "cost", "round", "call_id")}
                                    for u in self.upward if u.get("node", n["id"]) == n["id"] and u.get("proposal")]
            row["depth"], row["path"] = tree.depth(self.tree, n["id"]), tree.path(self.tree, n["id"])
            stats.append(row)
        write_json(self.run_dir / "problem_tree.json", {"nodes": stats, "tree": tree.nested(self.tree), "inward_share": self.inward_share,
                                                         "off_tree_share": self.off_tree_share, "origins": self._origin_stats(),
                                                         "lens": self.lens, "lens_design": self.lens_design,
                                                         "stats": {"n_idea_assumptions": sum(len(s["idea_assumptions"]) for s in stats)}})

    def _skipped(self, node_id) -> bool:
        """A part the owner excluded (control.json skip_nodes) or outside the --only-nodes scope. The scope is
        resolved against the planned map by id or by the default part's name, since the planner renames and
        splits parts (arch-1 lost every context to an id mismatch)."""
        if node_id in self.skip_nodes:
            return True
        if not self.only_nodes or node_id == "root":        # the root's reframing contexts are cheap and always stay
            return False
        return node_id not in tree.resolve_scope(self.only_nodes, self.tree or tree.DEFAULT_TREE)

    # ------------------------------------------------------------ the doubt card: measure, map, read, then doubt
    DOUBT_LIT_CAP = 3000            # characters of literature shown to a doubt card

    @staticmethod
    def _read_entries(brief: dict) -> int:
        """Literature rows in a brief (ledger rows from earlier runs are not reading)."""
        return sum(1 for key in ("known", "failed", "open") for e in (brief or {}).get(key, []) or []
                   if isinstance(e, dict) and not research._is_ledger(e))

    def _doubt_ready(self, round_no: int) -> tuple[bool, int, int]:
        """Doubt cards are dealt only after reading: briefs for at least half of the non-root parts, or a
        later round with any brief. Returns (ready, parts with a brief, parts)."""
        parts = [n for n in (self.tree or []) if n["id"] not in ("root", tree.OFF_TREE_NODE["id"]) and not self._skipped(n["id"])]
        k = sum(1 for n in parts if self._read_entries(self.briefs.get(n["id"])) > 0)
        any_read = any(self._read_entries(b) > 0 for b in self.briefs.values())
        ready = (k > 0 and 2 * k >= len(parts)) or (round_no > 1 and any_read)
        return ready, k, len(parts)

    def _literature_block(self, cap: int | None = None) -> str:
        """What the research briefs say about every part of the map, measured findings first, newest briefs first,
        each line with its source URL, capped to about `cap` characters."""
        cap = self.DOUBT_LIT_CAP if cap is None else cap
        names = {n["id"]: n.get("name", n["id"]) for n in (self.tree or [])}
        tier = {"known": 0, "failed": 1, "open": 2}          # measured effect > reported failure > untested direction
        rows = []
        for nid, b in self.briefs.items():
            ts = str((b or {}).get("ts", ""))
            for key in ("known", "failed", "open"):
                rank = 0
                for e in (b or {}).get(key, []) or []:
                    if not isinstance(e, dict) or research._is_ledger(e):
                        continue
                    if key == "known":
                        body = f"KNOWN: {e.get('name', '')}: {e.get('mechanism', '')} Effect: {e.get('effect', '')} ({e.get('where', '')})"
                    elif key == "failed":
                        body = f"DID NOT HELP: {e.get('name', '')}: {e.get('why', '')}"
                    else:
                        body = f"OPEN: {e.get('direction', '')}: {e.get('why', '')}"
                    body = " ".join(body.split())
                    body = body if len(body) <= 260 else body[:257] + "..."   # one long entry must not crowd out the other parts
                    rows.append((tier[key], rank, ts, f"- [{names.get(nid, nid)}] {body} {e.get('url', '')}"))
                    rank += 1
        rows.sort(key=lambda r: r[2], reverse=True)          # newest brief first ...
        rows.sort(key=lambda r: (r[0], r[1]))                # ... within: highest-confidence tier, every part's first entry before any second
        head = "WHAT THE LITERATURE SAYS ABOUT THIS MAP (from the research briefs):\n"
        out, used = [], len(head)
        for *_, line in rows:
            if used + len(line) + 1 > cap:
                break
            out.append(line)
            used += len(line) + 1
        if len(out) < len(rows):
            out.append(f"(showing {len(out)} of {len(rows)} sourced lines)")
        return head + ("\n".join(out) if out else "(no sourced lines)")

    def _doubt_addendum(self) -> str:
        return ("ORDER OF WORK: This map was drawn from the script and the measurements, then the team read the literature; "
                "you are the first to compare the two.\n\n" + self._literature_block() + "\n\n"
                "Doubt facts of the map against both the measurements and the literature above. Where either disagrees with "
                "the map, that fact is your target. Start each sketch with one line DOUBT: <the fact of the map, what "
                "contradicts it, and the source you lean on: a URL from the list above, or 'measured: <the number>'>.\n\n")

    @staticmethod
    def _doubt_lines(text: str) -> dict:
        """Each sketch's IDEA text -> the DOUBT: line in its block, or else the last DOUBT: line before it."""
        out, last = {}, ""
        for b in re.split(r"\n\s*\n", (text or "").strip()):
            m = re.search(r"^\s*DOUBT:\s*(.+)$", b, flags=re.M)
            if m:
                last = " ".join(m.group(1).split())
            i = re.search(r"IDEA:\s*(.+?)(?=\n[A-Z_]+:|\Z)", b, flags=re.S)
            if i and "MECHANISM:" in b:
                out.setdefault(" ".join(i.group(1).split())[:120], last)
        return out

    def _record_doubts(self, sketches: list[dict], text: str, round_no: int) -> None:
        """Store the DOUBT: line on each doubt sketch and log the disputed fact for the mapper to re-measure."""
        lines = self._doubt_lines(text)
        rows = []
        for s in sketches:
            d = lines.get(str(s.get("idea", ""))[:120], "")
            if not d:
                continue
            s["doubt"] = d[:500]
            nid = self._node_by_name(d.split(":")[0]) or next(
                (n["id"] for n in (self.tree or []) if n["id"] not in ("root", tree.OFF_TREE_NODE["id"])
                 and str(n.get("name", "")).lower() in d.lower()), None)
            rows.append({"round": round_no, "node": nid or s.get("node", tree.OFF_TREE_NODE["id"]),
                         "text": s["doubt"], "sketch_id": s["id"]})
        if rows:
            with self.lock:
                append_jsonl(self.run_dir / "disputed_facts.jsonl", rows)

    def ideate_round(self, round_no: int, seeds: list[str]) -> list[dict]:
        """Node x direction contexts (per_node each), plus upward contexts at the root. Cards cycle
        over the push types so every part is seen from several framings."""
        if self.tree is None:
            self.plan_tree(round_no)
            (self.run_dir / "research").mkdir(exist_ok=True)
            if self.do_research and round_no == 1:
                self._live(f"round {round_no}: researching", "web search per part, newest sources first")
                self.research_round(round_no)
            else:
                self.inject_ledger([n for n in self.tree if n["id"] != "root"])
        if round_no > 1:                             # last round's results are in: move the off-map share, promote winners
            self._promote_off_wins(round_no)
            self._shift_off_share(round_no)
        specs = []
        per = self.per_node if round_no == 1 else 1
        # contexts go to the leaves: a part with children shares its per-part budget with them (tree.deal_contexts),
        # so a deeper map costs no more contexts than a flat one; a flat map gets `per` everywhere, as before
        dealt = tree.deal_contexts(self.tree, per, round_no, self._skipped)
        for node in self.tree:
            if node["id"] == tree.OFF_TREE_NODE["id"] or self._skipped(node["id"]):
                continue
            for direction in node["directions"]:
                n_here = (2 if direction == "upward" else dealt.get((node["id"], direction), 0))
                for i in range(n_here):
                    card = self.IDEA_CARDS[(len(specs) + i) % len(self.IDEA_CARDS)]
                    if card == "transform":          # the node's own assumptions are the transform material
                        card = "formal"
                    seed = self.rng.choice([w for w in seeds if w not in self.used_seeds] or seeds)
                    self.used_seeds.add(seed)
                    specs.append((card, seed, node, direction))
                # one extra context per part x direction reads the research brief; the others do not,
                # so "with research" vs "without" is measured inside every run
                if direction != "upward" and node["id"] in self.briefs:
                    seed = self.rng.choice([w for w in seeds if w not in self.used_seeds] or seeds)
                    self.used_seeds.add(seed)
                    specs.append(("research", seed, node, direction))
            # one analogy context per part (outward: structure from other fields) and one diagnosis context
            # (inward: aim at what the measurements show), in round 1
            if round_no == 1 and node["id"] != "root" and tree.depth(self.tree, node["id"]) <= 1:   # parts only, not their children
                if node["id"] in self.analogies:
                    specs.append(("analogy", "", node, "outward"))
                if self.diagnostics_text:
                    specs.append(("diagnosis", "", node, "inward"))
                if self.adapt_card and len((self.briefs.get(node["id"]) or {}).get("known", [])) >= 2:
                    specs.append(("adapt", "", node, "inward"))
        # the owner's seed mechanisms: one context each, on the part they name, in round 1
        if round_no == 1:
            for sd in self.owner_seeds:
                nid = self._node_by_name(str(sd.get("part", "")))
                node = next((n for n in self.tree if n["id"] == nid), None) if nid else None
                if node is not None and not self._skipped(node["id"]) and str(sd.get("text", "")).strip():
                    specs.append(("owner", str(sd["text"]).strip()[:1500], node, "inward"))
        # measured trade-offs from this run (a gain with a cost) seed up to three "contradiction" contexts
        if self.contradiction_cards and round_no > 1:
            for text, node in self.contradictions()[:3]:
                specs.append(("contradiction", text, node, "inward"))
        if self.retired_cards:
            specs = [(("formal" if sp[0] in self.retired_cards else sp[0]),) + tuple(sp[1:]) for sp in specs]
        # off the map: blank (no map), gaps (what did it miss), doubt (which fact is wrong), a share of all contexts
        off_node = next((n for n in self.tree if n["id"] == tree.OFF_TREE_NODE["id"]), None)
        if off_node is not None and self.off_tree_share > 0:
            n_on = sum(1 for sp in specs if sp[3] != "upward")
            n_off = max(1, round(n_on * self.off_tree_share / max(0.05, 1 - self.off_tree_share)))
            # measure, map, read, then doubt: no doubt card before the map's facts can be compared with the literature
            ready, k_read, m_parts = self._doubt_ready(round_no)
            off_cards = tuple(c for c in tree.OFF_TREE_CARDS if ready or c != "doubt")
            for i in range(n_off):
                seed = self.rng.choice([w for w in seeds if w not in self.used_seeds] or seeds)
                self.used_seeds.add(seed)
                specs.append((off_cards[i % len(off_cards)], seed, off_node, "inward" if i % 2 == 0 else "outward"))
            self.decisions.append({"round": round_no, "step": "off_tree", "on_map": n_on, "off_map": n_off, "share": self.off_tree_share})
            self.decisions.append({"round": round_no, "step": "doubt_cards", "dealt": sum(1 for sp in specs if sp[0] == "doubt"),
                                   "reason": f"briefs for {k_read} of {m_parts} parts"
                                             + ("" if ready else "; doubt waits until the team has read (briefs for half the parts)")})

        if self.max_sketch_calls > 0 and len(specs) > self.max_sketch_calls:
            # test mode: the contexts that read the most (owner, research, diagnosis, analogy) first, dealt round-robin
            # across the parts so a small cap gives every part a context before any part gets a second
            prio = {"owner": -1, "research": 0, "diagnosis": 1, "analogy": 2, "doubt": 2}   # the owner's seeds are never capped away; doubt reads the briefs
            ups = [sp for sp in specs if sp[3] == "upward"]
            specs = ideate.deal_by_part(specs, self.max_sketch_calls, lambda sp: prio.get(sp[0], 3), lambda sp: sp[2]["id"])
            specs = keep_upward(specs, ups)
            self.decisions.append({"round": round_no, "step": "ideate", "capped_to": len(specs),
                                   "upward": sum(1 for sp in specs if sp[3] == "upward")})
        # upward contexts go first, so the ideation budget check (_afford) meets them before the other contexts spend it
        specs.sort(key=lambda sp: sp[3] != "upward")
        # the contexts each part (and the off-map node) got this round: selection deals build slots in the same shares
        self.contexts_by_node[round_no] = dict(Counter(sp[2]["id"] for sp in specs if sp[3] != "upward"))
        specs = self._pick_memory_free(round_no, specs, seeds)

        def _one(spec):
            card, seed, node, direction = spec
            source = _strip_comments(self.baseline_src) if card == "low_prior" else self.baseline_src
            common = self._common(source, True, f"{node['id']}:{direction}:{seed}")
            off = node["id"] == tree.OFF_TREE_NODE["id"]
            prompt = (tree.off_tree_prompt(card, self.tree, common, self.diagnostics_text, direction) if off
                      else tree.node_prompt(node, direction, common, self.tree))
            mem_state = self._memory_state(spec)
            if mem_state == "block":
                prompt += self.memory().block(self._part_of(node["id"]))
            if card == "seeded":
                prompt += f"Starting point: {seed}\n\n"
            elif card == "docs":
                prompt += (PF.fill("REFERENCE MATERIAL ({v:reference_what}):\n\n")
                           + _doc_text("reference") + "\n\n")
            elif card == "research":
                prompt += research.brief_text(self.briefs[node["id"]]) + "\n\nSketch ideas that go beyond what the brief lists as known, or test what it lists as open.\n\n"
            elif card == "analogy":
                prompt += research.analogy_text(self.analogies[node["id"]]) + "\n\n" + ideate.ANALOGY_ADDENDUM
            elif card == "diagnosis":
                prompt += ("HOW THE BASELINE BEHAVES (measured on this card):\n" + self.diagnostics_text + "\n\n"
                           + (ideate.ANOMALY_ADDENDUM.format(text=self.anomaly_text) if self.anomaly_text else "") + ideate.DIAGNOSIS_ADDENDUM)
            elif card == "owner":
                prompt += ideate.OWNER_ADDENDUM.format(text=seed)
            elif card == "adapt":
                known = (self.briefs.get(node["id"]) or {}).get("known", [])[:3]
                prompt += ("KNOWN TECHNIQUES FOR THIS PART (with their measured effects):\n"
                           + "\n".join(f"- {e['name']}: {e.get('mechanism', '')} Effect: {e.get('effect', '')} ({e.get('where', '')}) {e.get('url', '')}" for e in known)
                           + "\n\n" + ideate.ADAPT_ADDENDUM)
            elif card == "contradiction":
                prompt += ideate.CONTRADICTION_ADDENDUM.format(text=seed)
            elif card == "doubt" and off:
                prompt += self._doubt_addendum()
            if self.digest_text and card not in ("docs", "blank"):          # blank gets no hints at all
                prompt += (PF.fill("{v:digest_title} ({v:digest_use}):\n")
                           + self.digest_text + "\n\n")
            if self.exclusion_list and round_no > 1 and self.clusters and card != "blank":
                names = sorted({c["name"] for c in self.clusters if c.get("node") == node["id"]})[:40]
                if names:
                    prompt += ideate.EXCLUSION_ADDENDUM.format(names="\n".join(f"- {n}" for n in names))
            if round_no > 1 and self.history:
                prompt += self.history_text() + "\n\n"
            up = direction == "upward"                  # a proposal for a new verifier, not a sketch: own format, no sketch addenda
            if self.staged_sketch and not up:
                prompt += ideate.STAGED_ADDENDUM
            op = ""
            if self.leap_share > 0 and not up:
                with self.lock:
                    i = self._leap_counter.get(node["id"], 0)
                    self._leap_counter[node["id"]] = i + 1
                ops = list(ideate.LEAP_OPERATORS)
                random.Random(f"leapops:{self.run_id}:{node['id']}").shuffle(ops)
                op = ops[i % len(ops)]
                n_leap = max(2, math.ceil(self.leap_share * 8))
                prompt += ideate.LEAP_ADDENDUM.format(n=n_leap, op_name=op, op_text=ideate.LEAP_OPERATORS[op])
            delegated = self.ideation_web and self.web_mode == "delegate"
            if self.ideation_web and self.web_mode == "self":
                prompt += ideate.WEB_ADDENDUM
            elif delegated:
                prompt += ideate.WEB_DELEGATED_ADDENDUM
            tail = tree.UPWARD_FORMAT if up else ideate.SKETCH_FORMAT
            note = f"{node['name']} / {direction} / {card}" + (f" ({seed})" if card == "seeded" else "")
            est = (len(prompt) // 4) * (2 if delegated else 1) + 1800 + (20000 if self.ideation_web else 0)   # searches add fetched pages
            if not self._afford("ideation", est, note):
                return []
            family = None
            if self.cross_family_share > 0 and random.Random(f"fam:{node['id']}:{direction}:{card}:{seed}").random() < self.cross_family_share:
                family = self.cheap_model                 # arm: another model family for a share of contexts
            meta = {"card": f"sketch:{card}", "operator": direction, "seed": seed, "note": note,
                    "node": node["id"], "web": bool(self.ideation_web), "family": family or (self.model or "default")}
            if mem_state:
                meta.update({"memory": mem_state, "round": round_no})
            max_out = (3500 if self.staged_sketch else (2500 if self.ideation_web else 1800)) + (1500 if self.leap_share > 0 else 0)   # the leap scratch pass
            if self.ideation_web:
                r = self._call_with_web(prompt, "generate", max_out, meta, round_no, "ideate", model=family,
                                        context=f"the part '{node['name']}' of the {self.pf.v('recipe', 'recipe')}, {direction} direction", tail=tail)
            else:
                r = self._call(prompt + tail, "generate", max_out, meta, model=family)
            if up:
                props = parse_upward(r.text or "", round_no=round_no, call_id=r.call_id, idgen=lambda: new_id("u"))
                for s in props:
                    s["node"], s["direction"], s["card"] = node["id"], direction, card
                self._ledger(f"sketch:{card}", f"{node['id']}:{direction}", seed, r.call_id, r.usage, round_no, "ideate")
                return props
            sk = ideate.parse_sketches(r.text or "", card=card, operator=direction, seed=seed, call_id=r.call_id,
                                       idgen=lambda: new_id("s"))
            for s in sk:
                s["node"], s["direction"], s["family"] = node["id"], direction, family or (self.model or "default")
                s["leap_op"] = op if s.get("kind") == "leap" else ""
                s["origin"], s["round"] = ("off" if off else "tree"), round_no
            if card == "doubt" and off:
                self._record_doubts(sk, r.text or "", round_no)
            self._ledger(f"sketch:{card}", f"{node['id']}:{direction}", seed, r.call_id, r.usage, round_no, "ideate")
            return sk

        with ThreadPoolExecutor(max_workers=min(6, max(1, len(specs)))) as ex:
            batches = list(ex.map(_one, specs))
        new = [s for b in batches for s in b]
        upward = [s for s in new if s.get("direction") == "upward"]
        if upward:                                   # proposals for a new verifier; logged, not implemented
            append_jsonl(self.run_dir / "proposals_upward.jsonl", upward)
            self.upward.extend(upward)
        new = [s for s in new if s.get("direction") != "upward"]
        append_jsonl(self.run_dir / "ideas.jsonl", [{**s, "round": round_no} for s in new])
        self.sketches.extend(new)
        self._write_tree()
        return new

    def contradictions(self) -> list[tuple[str, dict]]:
        """Measured trade-offs from this run: candidates that learned better but paid in time, memory or size."""
        out = []
        for c in self.cands:
            m = self.vres.get(c.id, {}).get("metrics") or {}
            gain = m.get("learn_z") if m.get("learn_z") is not None else m.get("learn_gap")
            if gain is None or gain >= 0:
                continue
            costs = []
            if (m.get("step_ratio") or 1.0) > 1.15:
                costs.append(f"step time x{m['step_ratio']}")
            if (m.get("param_ratio") or 1.0) > 1.03:
                costs.append(f"parameters x{m['param_ratio']}")
            if self.profile.get("peak_vram_gb") and (m.get("peak_vram_gb") or 0) > self.profile["peak_vram_gb"] * 1.15:
                costs.append(f"VRAM {m['peak_vram_gb']} GB")
            if (m.get("cost_ratio") or 1.0) > 1.15:            # generic checkers report one cost ratio
                costs.append(f"cost x{m['cost_ratio']}")
            if not costs:
                continue
            node = next((n for n in (self.tree or []) if n["id"] == c.extra.get("node")), None)
            if node:
                out.append((f"'{c.extra.get('hypothesis', '')[:160]}' improved {self.pf.v('gain_phrase', 'the score at the first check')} (z {gain}) but cost {', '.join(costs)}", node))
        return out

    def _discovery(self, round_no: int) -> None:
        """New clusters per context this round and per-card yield; retire attractor cards for the next round."""
        d = NV.discovery(self.clusters, self.sketches, round_no)
        self.discovery.append(d)
        write_json(self.run_dir / "discovery.json", {"rounds": self.discovery})
        if self.retire_cards:
            att = NV.attractor_cards(d)
            if att:
                self.retired_cards.update(att)
                self.decisions.append({"round": round_no, "step": "retire_cards", "cards": att, "ts": now_ts()})

    def _novelty_filter(self, chosen: list[dict], ranked_pool: list[dict]) -> list[dict]:
        """Drop chosen clusters that are near-duplicates of something already built (this run or the
        ledger), build a random audit share anyway, and refill the slots from the next-ranked clusters."""
        built = {c.id: f"{c.extra.get('hypothesis', '')} {c.extra.get('change', '')}" for c in self.cands}
        built.update(self.ledger_texts)
        if not built:
            return chosen
        by_id = {s["id"]: s for s in self.sketches}

        def text(c):
            rep = by_id.get(c["representative"], {})
            return f"{c['name']} {rep.get('idea', '')} {rep.get('mechanism', '')}"
        kept, skipped = [], set()
        for c in chosen:
            g = NV.gate(text(c), built, self.novelty_threshold, self.novelty_audit, self.rng)
            c["novelty_gate"] = {"nearest": g["nearest"], "audit": g["audit"], "built": g["build"]}
            if g["build"]:
                kept.append(c)
            else:
                skipped.add(c["cluster_id"])
                self.decisions.append({"step": "novelty_skip", "cluster": c["cluster_id"], "nearest": g["nearest"]})
        need = len(chosen) - len(kept)
        for c in ranked_pool:
            if need <= 0:
                break
            if c["cluster_id"] in skipped or any(c["cluster_id"] == k["cluster_id"] for k in kept):
                continue
            g = NV.gate(text(c), built, self.novelty_threshold, self.novelty_audit, self.rng)
            if g["build"]:
                c["selected"], c["novelty_gate"] = True, {"nearest": g["nearest"], "audit": g["audit"], "built": True, "refill": True}
                kept.append(c)
                need -= 1
        return kept

    def _select_with_lanes(self, by_node: dict, k: int, done: set) -> list[dict]:
        """Main slots by score (coverage across parts), plus a long-shot lane drawn at random, weighted by
        score, from step-outside, analogy, adapt and new clusters: novelty protected, not enforced."""
        k_long = (max(2, int(round(k * self.longshot_share))) if k >= 3 else (1 if k >= 2 else 0)) if self.longshot_share > 0 else 0
        built = Counter((c.extra or {}).get("node") for c in self.cands if (c.extra or {}).get("lane") in ("main", "longshot"))
        ctx = self.contexts_by_node.get(self.round_now) or {}
        if not ctx:                                   # resumed past ideation: rebuild from the round's sketches on disk
            calls = {(s.get("node"), s.get("call_id")) for s in self.sketches if s.get("round") == self.round_now
                     and s.get("direction") != "upward" and s.get("card") != "deepen" and s.get("call_id") and s.get("node")}
            ctx = dict(Counter(n for n, _ in calls))
            if ctx:
                self.contexts_by_node[self.round_now] = ctx
        main = tree.split_select(by_node, k - k_long, self.inward_share, done, self.sketches, self._select, self.new_share,
                                 counts=dict(built), order_seed=f"{self.run_id}:build:{len(self.cands)}",
                                 weights=dict(ctx) or None)
        for c in main:
            c["lane"] = "main"
        if k_long <= 0:
            self._log_slots_by_origin(main, ctx)
            return main
        taken = {c["cluster_id"] for c in main} | done
        cands = [c for c in self.clusters if c["cluster_id"] not in taken and
                 (c.get("direction") == "outward" or any(x in c["cards"] for x in ("analogy", "adapt", "deepen", "owner")) or c.get("prior") == "new"
                  or float(c.get("leap_share") or 0) >= 0.5)]
        rng = random.Random(f"longshot:{self.rep}:{len(self.cands)}")
        weights = {c["cluster_id"]: math.exp(min(10.0, float(c.get("score") or 0.0))) for c in cands}
        wsum = sum(weights.values()) or 1.0
        picks = ideate.draw_lane(cands, k_long, rng)          # at least half the lane goes to leap clusters when they exist
        for c in picks:
            c["selected"], c["lane"] = True, "longshot"
            c["lane_propensity"] = round(weights.get(c["cluster_id"], 0.0) / wsum, 3)
        self._log_selection(by_node, main, picks, done, weights, wsum)
        self._log_slots_by_origin(main + picks, ctx)
        return main + picks

    def _log_slots_by_origin(self, picks: list, ctx: dict) -> None:
        """Build slots vs idea contexts per origin this round, so the off-map share of each can be compared."""
        off_id = tree.OFF_TREE_NODE["id"]
        off = sum(1 for c in picks if c.get("node") == off_id)
        self.decisions.append({"step": "slots_by_origin", "round": self.round_now, "tree": len(picks) - off, "off": off,
                               "contexts_tree": sum(v for n, v in ctx.items() if n != off_id),
                               "contexts_off": ctx.get(off_id, 0)})

    def cluster_sketches(self, round_no: int) -> None:
        """Blind clustering per part and direction, then one merge call across parts (the same change
        filed under two parts becomes one cluster), then prior-art and obvious-answer tags."""
        self.clusters = []
        groups_by_key: dict[tuple, list[dict]] = {}
        for s in self.sketches:
            groups_by_key.setdefault((s.get("node"), s.get("direction")), []).append(s)
        for (node_id, direction), sks in groups_by_key.items():
            groups = None
            ckey = (node_id, direction, frozenset(s["id"] for s in sks))
            if ckey in self._cluster_cache:
                groups = self._cluster_cache[ckey]
            elif len(sks) >= 4:
                r = self._call(ideate.cluster_prompt(sks), "judge", 2500,
                               {"card": "cluster", "note": f"blind clustering: {node_id}/{direction}, {len(sks)} sketches"}, model=self.cheap_model)
                self._ledger("cluster", f"{node_id}:{direction}", "", r.call_id, r.usage, round_no, "judge")
                groups = ideate.parse_cluster_json(r.text or "", {s["id"] for s in sks})
            if groups is None:
                groups = [{"name": "", "members": g} for g in ideate.lexical_clusters(sks)]
            self._cluster_cache[ckey] = groups
            cl = ideate.build_clusters(groups, sks)
            for c in cl:
                c["cluster_id"] = f"{node_id}-{direction[:2]}-{c['cluster_id']}"
                c["node"], c["direction"] = node_id, direction
            self.clusters.extend(cl)
        by_id = {s["id"]: s for s in self.sketches}
        # cross-part merge: one cheap call over every cluster name
        if len(self.clusters) >= 4:
            r = self._call(ideate.merge_prompt(self.clusters, by_id), "judge", 2500,
                           {"card": "merge", "note": f"same idea filed under different parts? {len(self.clusters)} clusters"},
                           model=self.cheap_model)
            self._ledger("merge", "all", "", r.call_id, r.usage, round_no, "judge")
            groups = ideate.parse_merge(r.text or "", {c["cluster_id"] for c in self.clusters})
            if groups:
                self.clusters = ideate.merge_clusters(self.clusters, groups, self.sketches)
                self.decisions.append({"round": round_no, "step": "merge", "groups": groups})
        # prior-art tags: the model matches clusters against the brief; word overlap is the fallback
        obvious_brief = {"known": [{"name": d, "mechanism": ""} for d in self.defaults_lines], "failed": []}
        for node_id in {c.get("node") for c in self.clusters}:
            cl = [c for c in self.clusters if c.get("node") == node_id]
            brief = self.briefs.get(node_id)
            tags = None
            fresh = [c for c in cl if (node_id, frozenset(c["members"])) not in self._tag_cache]
            if brief and (brief.get("known") or brief.get("failed")) and len(fresh) >= 2:
                r = self._call(research.tag_prompt(fresh, by_id, brief), "judge", 2500,
                               {"card": "prior", "note": f"prior-art tags for {node_id}: {len(fresh)} new clusters"}, model=self.cheap_model)
                self._ledger("prior", node_id, "", r.call_id, r.usage, round_no, "judge")
                tags = research.parse_tags(r.text or "", {c["cluster_id"] for c in fresh}, brief)
            for c in cl:
                rep = by_id.get(c["representative"], {})
                text = f"{c['name']} {rep.get('idea', '')} {rep.get('mechanism', '')}"
                tkey = (node_id, frozenset(c["members"]))
                if tkey in self._tag_cache:
                    c["prior"], c["prior_match"], c["prior_source"] = self._tag_cache[tkey]
                elif tags and c["cluster_id"] in tags:
                    c["prior"], c["prior_match"] = tags[c["cluster_id"]]
                    c["prior_source"] = "model"
                else:
                    c["prior"], c["prior_match"] = research.prior_art_tag(text, brief)
                    c["prior_source"] = "lexical"
                self._tag_cache[tkey] = (c["prior"], c["prior_match"], c["prior_source"])
                ob, match = research.prior_art_tag(text, obvious_brief) if self.defaults_lines else ("new", None)
                c["obvious"] = ob == "known"
                c["obvious_match"] = match

    # ------------------------------------------------------------ deepening stage (nano/deepen.py)
    def knowledge_for(self, cluster: dict) -> str:
        """Facts gathered by interrogating any idea that shares a sketch with this cluster."""
        members = set(cluster.get("members", []))
        roots = {n["id"] for n in self.deepen_nodes if not n.get("parent") and members & set(n.get("members", []))}
        if not roots:
            return ""
        chain = [n for n in self.deepen_nodes if n["id"] in roots or n.get("root") in roots]
        txt = deepen.knowledge_text(chain)
        # objections already resolved by a build of this idea (a revise, or round two) replace the raw list
        resolved = None
        for c in reversed(self.cands):
            if members & set(c.extra.get("members") or []) and (self.vres.get(c.id, {}).get("metrics") or {}).get("objections"):
                resolved = self.vres[c.id]["metrics"]["objections"]
                break
        standing = deepen.standing_classes([n for n in self.deepen_nodes if not n.get("parent")])
        if resolved:
            txt += "\n\n" + deepen.objections_text(resolved, next((n.get("premortem_verdict", "") for n in chain if n.get("objections")), ""), standing)
            return txt
        try:
            from nano import lessons as LS
            pit = LS.render(config.MEMORY_DIR / "lessons.jsonl", part=cluster.get("node"), kind="pitfall", version=self.baseline_version)
            if pit:
                txt += "\n\n" + pit
        except Exception:  # noqa: BLE001
            pass
        for n in chain:
            if n.get("objections"):
                txt += "\n\n" + deepen.objections_text(n["objections"], n.get("premortem_verdict", ""), standing)
        return txt

    def deepen_round(self, round_no: int, chosen: list[dict], gen: int = 0) -> int:
        """One interrogation chain per chosen cluster: root call, then up to `fanout` children per open
        question, down to `depth`. Offshoot sketches join self.sketches with card "deepen"."""
        constraints = "\n".join(f"- {c}" for c in self.pf.constraints)
        web = bool(self.ideation_web)
        web_self = web and self.web_mode == "self"     # only then does the prompt tell the model to search itself
        new_sketches: list[dict] = []
        self._deepen_skipped: set[str] = set()

        def _call_node(cl: dict, parent: dict | None, focus: str | None, depth: int) -> dict | None:
            node = next((n for n in (self.tree or []) if n["id"] == cl.get("node")), None) or {}
            with self.lock:
                sketches_now = list(self.sketches)
            brief = ideate.implement_brief(cl, sketches_now)
            known = (parent.get("known", []) + parent.get("inherited", [])) if parent else []
            rb = self.briefs.get(cl.get("node"))
            research_txt = research.brief_text(rb) if rb else ""
            hist = self.history_text()
            if self.diagnostics_text and parent is None:
                hist = ("HOW THE BASELINE BEHAVES (measured):\n" + self.diagnostics_text
                        + (("\n\nANOMALIES (replicated on several seeds):\n" + self.anomaly_text) if self.anomaly_text else "")
                        + ("\n\n" + hist if hist else ""))
            prompt = (deepen.root_prompt(brief, node.get("name", cl.get("node", "")), node.get("frame", ""), constraints, web_self,
                                         code=self.baseline_src, research=research_txt, history=hist)
                      if parent is None else
                      deepen.child_prompt(brief, focus or "", known, node.get("name", ""), constraints, web_self,
                                          code=self.baseline_src, history=hist,
                                          chain=deepen.chain_text((parent.get("chain_root") or parent.get("chain") or []),
                                                                  parent.get("link_status"))))
            est = (len(prompt) // 4) * (2 if (web and not web_self) else 1) + 3000 + (20000 if web else 0)
            if not self._afford("interrogation", est, cl.get("name", "")):
                with self.lock:
                    self.decisions.append({"round": round_no, "step": "deepen", "budget_skip": cl["cluster_id"], "depth": depth})
                    if depth == 0:
                        self._deepen_skipped.add(cl["cluster_id"])
                return None
            meta = {"card": "deepen", "operator": cl["cluster_id"], "seed": "",
                    "note": f"interrogating '{cl['name']}' gen {gen} depth {depth}" + (f": {focus[:60]}" if focus else ""),
                    "node": cl.get("node"), "depth": depth, "gen": gen}
            if web:
                r = self._call_with_web(prompt, "generate", 6000, meta, round_no, "generate",
                                        context=f"the idea '{cl['name']}' in the part '{node.get('name', '')}'")
            else:
                r = self._call(prompt, "generate", 6000, meta)
            self._ledger("deepen", cl["cluster_id"], "", r.call_id, r.usage, round_no, "generate")
            parsed = deepen.parse(r.text or "")
            sk = ideate.parse_sketches(parsed["sketch_text"], card="deepen", operator=cl.get("direction", ""),
                                       seed="", call_id=r.call_id, idgen=lambda: new_id("s"))
            for x in sk:
                x["node"], x["direction"], x["parent_cluster"] = cl.get("node"), cl.get("direction"), cl["cluster_id"]
                other = self._node_by_name(x.get("part", ""))      # an idea for another part is filed under that part
                if other and other != cl.get("node"):
                    x["node"], x["filed_from"] = other, cl.get("node")
            dn = {"id": new_id("d"), "cluster_id": cl["cluster_id"], "cluster_name": cl["name"], "gen": gen,
                  "members": list(cl.get("members", [])), "depth": depth, "parent": parent["id"] if parent else None,
                  "root": parent.get("root") if parent else None, "focus": focus, "qa": parsed["qa"],
                  "known": parsed["known"], "assumes": parsed["assumes"], "dropped_unsourced": parsed["dropped_unsourced"],
                  "inherited": known, "offshoots": [x["id"] for x in sk],
                  "open": parsed["open"], "call_id": r.call_id, "node": cl.get("node"), "direction": cl.get("direction"),
                  "chain": parsed.get("chain") or [], "weakest": parsed.get("weakest", ""), "link_status": parsed.get("link_status") or [],
                  "known_tagged": parsed.get("known_tagged") or [], "unknown_share": parsed.get("unknown_share", 0.0),
                  "chain_root": (parent.get("chain_root") or parent.get("chain")) if parent else (parsed.get("chain") or []),
                  "stop": deepen.stop_here(parsed, depth)}
            if node and parsed["assumes"]:            # what the idea silently assumed: context for later sketches on the
                with self.lock:                       # part, kept apart from the part's design assumptions
                    ia = node.setdefault("idea_assumptions", tree.idea_assumptions(node))
                    have = {a.lower()[:60] for a in node["assumptions"]} | {x["text"].lower()[:60] for x in ia}
                    for a in parsed["assumes"]:
                        if a.lower()[:60] not in have:
                            ia.append({"from": cl["cluster_id"], "text": a, "round": round_no, "kind": "silent"})
                            have.add(a.lower()[:60])
            if dn["root"] is None:
                dn["root"] = dn["id"]
            if parent is None and self.do_premortem:          # separate calls whose only job is to make the idea fail
                tried = (self.briefs.get(cl.get("node")) or {}).get("tried", [])
                ledger_pack = [f"measured in an earlier run: {e.get('name', '')}: {e.get('why', '')}" for e in tried[:12]]
                ledger_pack += [l for l in self.diagnostics_text.splitlines() if l.strip()][:10]
                if self.anomaly_text:
                    ledger_pack += ["anomaly: " + l.lstrip("- ") for l in self.anomaly_text.splitlines() if l.strip()][:5]
                evidence = [l for l in (research_txt + "\n" + self.diagnostics_text).splitlines() if l.strip()][:30]
                # evidence the builder lacked first (outside view), then the information-poor control, then the idea's own facts
                packs = [("ledger", ledger_pack or evidence), ("script-only", []), ("facts", parsed["known"]), ("evidence", evidence)][: max(1, self.premortems)]
                objections, verdicts = [], []
                for pack_name, known_pack in packs:
                    est2 = len(prompt) // 4 + 2500
                    if not self._afford("interrogation", est2, "pre-mortem"):
                        break
                    pr = self._call(deepen.premortem_prompt(brief, node.get("name", ""), constraints, self.baseline_src, known_pack,
                                                            chain=deepen.chain_text(parsed.get("chain") or [])),
                                    "generate", 2500, {"card": "premortem", "operator": cl["cluster_id"], "seed": pack_name,
                                                       "note": f"pre-mortem ({pack_name}) of '{cl['name']}'", "node": cl.get("node")})
                    self._ledger("premortem", cl["cluster_id"], pack_name, pr.call_id, pr.usage, round_no, "generate")
                    pm = deepen.parse_premortem(pr.text or "")
                    seen_o = {o["text"].lower()[:50] for o in objections}
                    objections += [o for o in pm["objections"] if o["text"].lower()[:50] not in seen_o]
                    if pm["verdict"]:
                        verdicts.append(pm["verdict"])
                dn["objections"], dn["premortem_verdict"] = objections, " | ".join(verdicts)[:400]
            with self.lock:
                self.deepen_nodes.append(dn)
                new_sketches.extend(sk)
                self.sketches.extend(sk)
                with (self.run_dir / "ideas.jsonl").open("a", encoding="utf-8") as f:
                    for x in sk:
                        f.write(json.dumps(x) + "\n")
                write_json(self.run_dir / "deepen.json", {"nodes": self.deepen_nodes})
            return dn

        def _chain(cl: dict) -> None:
            frontier: list[tuple] = [(None, None)]
            for depth in range(0, self.deepen_depth + 1):
                nxt = []
                for parent, focus in frontier:
                    dn = _call_node(cl, parent, focus, depth)
                    if dn is None:
                        return
                    if dn.get("stop"):                                      # the fork test: no deeper when it would add nothing
                        with self.lock:
                            self.decisions.append({"round": round_no, "step": "deepen", "stop": dn["stop"], "idea": cl["cluster_id"], "depth": depth})
                        continue
                    weakest = next((l.get("text", "") + " " + l.get("quantity", "") for l in (dn.get("chain_root") or []) if l.get("id") == dn.get("weakest")), "")
                    for q in deepen.follow(dn["open"], self.deepen_fanout, weakest):   # the weakest link's questions first
                        nxt.append((dn, q))
                frontier = nxt
                if not frontier:
                    return

        with ThreadPoolExecutor(max_workers=min(6, max(1, len(chosen)))) as ex:
            list(ex.map(_chain, chosen))
        self.decisions.append({"round": round_no, "step": "deepen", "gen": gen, "chains": len(chosen),
                               "nodes": len(self.deepen_nodes), "offshoots": len(new_sketches), "ts": now_ts()})
        return len(new_sketches)

    # ------------------------------------------------------------ control file and resume
    # ------------------------------------------------------------ per-part persistent memory (nano/memory.py)
    def memory(self) -> MEM.Memory:
        """<lab>/memory/<profile>/ (the profile's `memory_dir` overrides it); mock runs keep theirs under
        memory/_mock so a dry run never feeds a real one."""
        if self._memory is None:
            md = self.pf.get("memory_dir")
            base = Path(md) if md else (config.MEMORY_DIR / self.pf.name)
            if not base.is_absolute():
                base = config.LAB_ROOT / base
            if self.backend == "mock":
                base = base.parent / "_mock" / base.name
            self._memory = MEM.Memory(base.parent, base.name)
        return self._memory

    def _part_of(self, node_id) -> str | None:
        """The top-level part a node belongs to (sub-parts and failure questions share their part's memory);
        None for the root, the off-map node and anything not on the map."""
        if not node_id or node_id in ("root", tree.OFF_TREE_NODE["id"]) or not any(n["id"] == node_id for n in self.tree or []):
            return None
        chain = tree._chain(self.tree, node_id)
        return chain[-1]["id"] if chain else None

    def _memory_state(self, spec) -> str:
        """"block" (the prompt gets the memory), "free" (this round's ignores-memory context), "empty" (the part
        has no memory yet) or "" (memory off, off-map, upward)."""
        if not self.use_memory or spec[3] == "upward":
            return ""
        part = self._part_of(spec[2]["id"])
        if part is None:
            return ""
        if id(spec) in self.memory_free:
            return "free"
        return "block" if self.memory().read(part) else "empty"

    def _pick_memory_free(self, round_no: int, specs: list, seeds: list[str]) -> list:
        """One ignores-memory context per part per round (anti-fixation guard and an in-run control). It is drawn
        from the part's own contexts when it has two or more; a part with one context gets one extra context,
        so that the single context still reads the memory. Parts with no memory yet are left alone."""
        self.memory_free = set()
        if not self.use_memory:
            return specs
        by_part: dict[str, list] = {}
        for sp in specs:
            part = self._part_of(sp[2]["id"]) if sp[3] != "upward" else None
            if part is not None:
                by_part.setdefault(part, []).append(sp)
        rng = random.Random(f"memfree:{self.run_id}:{round_no}")
        extra = []
        for part, sps in sorted(by_part.items()):
            if not self.memory().read(part):
                continue
            pool = [sp for sp in sps if sp[0] != "owner"] or sps
            if len(sps) >= 2:
                pick = rng.choice(pool)
            else:
                card, _, node, direction = pool[0]
                seed = rng.choice([w for w in seeds if w not in self.used_seeds] or seeds) if seeds else ""
                self.used_seeds.add(seed)
                pick = (card, seed, node, direction)
                extra.append(pick)
            self.memory_free.add(id(pick))
            self.decisions.append({"round": round_no, "step": "memory_free", "part": part, "node": pick[2]["id"],
                                   "card": pick[0], "direction": pick[3], "added": len(sps) < 2})
        if extra:
            per = self.contexts_by_node.setdefault(round_no, {})
            for sp in extra:
                per[sp[2]["id"]] = per.get(sp[2]["id"], 0) + 1
        return specs + extra

    def _memory_artefacts(self) -> dict:
        """What a memory entry may cite: candidate ids in verify.jsonl, sketch ids, measured numbers, brief URLs."""
        cand_ids, numbers = set(), []
        vp = self.run_dir / "verify.jsonl"
        for line in vp.read_text(encoding="utf-8").splitlines() if vp.exists() else []:
            try:
                row = json.loads(line)
            except Exception:  # noqa: BLE001
                continue
            cand_ids.add(row.get("id"))
            for v in ((row.get("details") or {}).get("metrics") or {}).values():
                vals = v.values() if isinstance(v, dict) else [v]
                numbers += [x for x in vals if isinstance(x, (int, float)) and not isinstance(x, bool)]
        urls: set[str] = set()

        def walk(o):
            if isinstance(o, dict):
                for k, v in o.items():
                    if k == "url" and isinstance(v, str) and v.startswith("http"):
                        urls.add(v)
                    else:
                        walk(v)
            elif isinstance(o, list):
                for v in o:
                    walk(v)
        walk(self.briefs)
        walk(self.analogies)
        return {"cand_ids": cand_ids - {None}, "sketch_ids": {s.get("id") for s in self.sketches if s.get("id")},
                "numbers": numbers, "urls": urls}

    def _curate_memory(self, round_no: int) -> None:
        """End of the verify step: one curator call per part with candidates verified this round. The reply is a
        delta in the six headers; nano/memory.py keeps an entry only if it cites an artefact that exists and is
        not a near-duplicate, and appends it with the date, run and round. Never a whole-file rewrite."""
        if not self.use_memory:
            return
        by_part: dict[str, list[dict]] = {}
        seen = set()
        for h in self.history:
            if h.get("round") != round_no or h.get("cand_id") in seen:
                continue
            part = self._part_of(h.get("node"))
            if part is None:
                continue
            seen.add(h["cand_id"])
            cand = next((c for c in self.cands if c.id == h["cand_id"]), None)
            m = (self.vres.get(h["cand_id"]) or {}).get("metrics") or {}
            by_part.setdefault(part, []).append({
                "cand_id": h["cand_id"], "status": h.get("status"), "hypothesis": h.get("hypothesis", ""),
                "reason": str(h.get("reason") or "")[:300],
                "metrics": {k: v for k, v in m.items() if isinstance(v, (int, float)) and not isinstance(v, bool)},
                "sketches": list((cand.extra or {}).get("members") or []) if cand else []})
        if not by_part:
            return
        mem, arte = self.memory(), self._memory_artefacts()
        for part, results in sorted(by_part.items()):
            if not self._aux_ok("memory curator"):
                break
            node = next((n for n in self.tree if n["id"] == part), {"name": part})
            brief = json.dumps(self.briefs.get(part) or {})
            urls = sorted(u for u in arte["urls"] if u in brief)
            prompt = MEM.curator_prompt(node.get("name", part), part, mem.read(part), results, urls)
            r = self._call(prompt, "judge", 1500, {"card": "memory_curator", "operator": part, "seed": "",
                                                   "node": part, "round": round_no}, model=self.cheap_model)
            self._ledger("memory_curator", part, "", r.call_id, r.usage, round_no, "judge")
            delta = MEM.Memory.propose_delta(part, r.text or "")
            res = mem.curate(part, delta, arte, run=self.run_id, round_no=round_no)
            archived = mem.archive(part, unused_rounds=5)
            self.memory_stats["parts"].add(part)
            self.memory_stats["entries_added"] += len(res["added"])
            self.memory_stats["entries_rejected"] += len(res["rejected"])
            append_jsonl(self.run_dir / "memory_log.jsonl", {
                "round": round_no, "part": part, "call_id": r.call_id, "file": str(mem.path(part)),
                "proposed": len(delta["entries"]),
                "added": [{k: e[k] for k in ("id", "section", "source", "text")} for e in res["added"]],
                "rejected": res["rejected"], "bumped": res["bumped"], "archived": archived, "ts": now_ts()})
            self.decisions.append({"round": round_no, "step": "memory", "part": part, "added": len(res["added"]),
                                   "rejected": len(res["rejected"]), "archived": len(archived)})

    def _report_memory(self) -> None:
        """report.json "memory": "off" in the control arm, else the parts curated and entries added or rejected."""
        rj = self.run_dir / "report.json"
        try:
            d = json.loads(rj.read_text(encoding="utf-8")) if rj.exists() else {}
        except Exception:  # noqa: BLE001
            d = {}
        d["memory"] = ("off" if not self.use_memory else
                       {"parts": len(self.memory_stats["parts"]), "entries_added": self.memory_stats["entries_added"],
                        "entries_rejected": self.memory_stats["entries_rejected"]})
        rj.write_text(json.dumps(d, indent=1), encoding="utf-8")

    def _stage(self, round_no: int, name: str) -> None:
        """A stage boundary: record it, then obey control.json (pause, stop, skips, note)."""
        st = json.loads((self.run_dir / "state.json").read_text(encoding="utf-8"))
        st["stage"] = {"round": round_no, "step": name, "ts": now_ts()}
        if name == "verified":
            st["completed_rounds"] = round_no
        write_json(self.run_dir / "state.json", st)
        p = self.run_dir / "control.json"
        while True:
            ctl = {}
            if p.exists():
                try:
                    ctl = json.loads(p.read_text(encoding="utf-8"))
                except Exception:  # noqa: BLE001
                    ctl = {}
            h = hashlib.sha1(json.dumps(ctl, sort_keys=True).encode()).hexdigest()[:10] if ctl else ""
            if h != self._control_hash:
                self._control_hash = h
                if ctl:
                    append_jsonl(self.run_dir / "control_log.jsonl", {"ts": now_ts(), "round": round_no, "stage": name, "control": ctl})
            for key in ("budget_add", "aux_budget_add", "k_impl", "rounds_max", "longshot_share", "leap_share"):
                if key in ctl and (key, str(ctl[key])) not in self._control_applied:
                    self._control_applied.add((key, str(ctl[key])))
                    try:
                        if key == "budget_add":
                            self.B += int(ctl[key])
                        elif key == "aux_budget_add":
                            self.aux_budget += int(ctl[key])
                        elif key == "k_impl":
                            self.k_impl = max(1, int(ctl[key]))
                        elif key == "rounds_max":
                            self.rounds = max(1, int(ctl[key]))
                        elif key == "longshot_share":
                            self.longshot_share = max(0.0, min(0.6, float(ctl[key])))
                        elif key == "leap_share":
                            self.leap_share = max(0.0, min(1.0, float(ctl[key])))
                        self.decisions.append({"round": round_no, "step": "control", "set": key, "value": ctl[key], "ts": now_ts()})
                    except (TypeError, ValueError):
                        pass
            self.control_note = str(ctl.get("note", ""))[:600]
            self.skip_nodes = set(ctl.get("skip_nodes", []) or [])
            self.exclude_clusters = set(ctl.get("exclude_clusters", []) or [])
            self._add_human_nodes(ctl.get("add_nodes") or [], round_no)
            if ctl.get("stop_after_stage") or (self.stop_after and name == self.stop_after):
                raise StopRun(name)
            if not ctl.get("pause"):
                return
            self._live(note=f"paused by control.json after '{name}' (set pause to false to continue)")
            time.sleep(10)

    def _add_human_nodes(self, specs, round_no: int) -> None:
        """control.json "add_nodes": branches people add, in the tree's node schema. Each goes on the map once,
        marked origin "human" (docs/mapper/03_maintenance_and_people.md, "Add problem or branch"); a re-plan
        carries it over (replan_tree). Before the first map exists they wait for the next stage boundary."""
        if self.tree is None or not isinstance(specs, list):
            return
        added = []
        for sp in specs:
            if not isinstance(sp, dict) or not sp.get("id") or not sp.get("name"):
                continue
            nid = re.sub(r"[^a-z0-9_]", "", str(sp["id"]).lower())[:16]
            if not nid or nid in self.human_nodes_seen:
                continue
            self.human_nodes_seen.add(nid)
            if any(n["id"] == nid for n in self.tree):
                continue                                  # already on the map (a resume, or a clash with a planned id)
            asm = sp.get("assumptions") if isinstance(sp.get("assumptions"), list) else []
            node = {**sp, "id": nid, "name": str(sp["name"])[:60], "parent": str(sp.get("parent") or "root"),
                    "frame": str(sp.get("frame", ""))[:400], "assumptions": [str(a)[:160] for a in asm][:5],
                    "boundary": str(sp.get("boundary") or self.pf.boundary_all)[:200],
                    "directions": list(sp.get("directions") or ["inward", "outward"]), "origin": "human"}
            self.tree.append(node)
            added.append(nid)
            self.decisions.append({"round": round_no, "step": "human_node", "node": nid, "name": node["name"], "ts": now_ts()})
        if added:
            self._write_tree()

    def load_state(self) -> None:
        """Resume: reload everything a previous attempt left on disk; the interrupted round is redone from
        its first incomplete stage, with clustering and tags served from the caches."""
        rd = self.run_dir
        st = json.loads((rd / "state.json").read_text(encoding="utf-8")) if (rd / "state.json").exists() else {}
        self.completed_rounds = int(st.get("completed_rounds", 0))
        self.decisions = st.get("decisions", [])
        self.spent = int(st.get("spent", 0))
        self.spent_aux = int(st.get("spent_aux", 0))
        self.interrogated = set()
        pt = json.loads((rd / "problem_tree.json").read_text(encoding="utf-8")) if (rd / "problem_tree.json").exists() else {}
        if pt.get("nodes"):
            self.tree = [tree.migrate_node({k: v for k, v in n.items() if k != "stats"}) for n in pt["nodes"]]
        for p in (rd / "research").glob("*.json") if (rd / "research").exists() else []:
            d = json.loads(p.read_text(encoding="utf-8"))
            if p.stem.endswith("_analogy"):
                self.analogies[p.stem[: -len("_analogy")]] = d
            else:
                self.briefs[p.stem] = d
        if (rd / "private" / "defaults.json").exists():
            self.defaults_lines = ideate.parse_defaults(json.loads((rd / "private" / "defaults.json").read_text(encoding="utf-8")).get("text", ""))
        for line in (rd / "ideas.jsonl").read_text(encoding="utf-8").splitlines() if (rd / "ideas.jsonl").exists() else []:
            try:
                self.sketches.append(json.loads(line))
            except Exception:  # noqa: BLE001
                pass
        icl = json.loads((rd / "idea_clusters.json").read_text(encoding="utf-8")) if (rd / "idea_clusters.json").exists() else {}
        groups_by_key: dict[tuple, list[dict]] = {}
        for c in icl.get("clusters", []):
            self._tag_cache[(c.get("node"), frozenset(c["members"]))] = (c.get("prior"), c.get("prior_match"), c.get("prior_source"))
            if not c.get("merged_from"):
                groups_by_key.setdefault((c.get("node"), c.get("direction")), []).append({"name": c.get("name", ""), "members": list(c["members"])})
        for (node_id, direction), groups in groups_by_key.items():    # the blind clustering is not repeated on resume
            all_ids = frozenset(m for g in groups for m in g["members"])
            self._cluster_cache[(node_id, direction, all_ids)] = groups
        for line in (rd / "proposals_upward.jsonl").read_text(encoding="utf-8").splitlines() if (rd / "proposals_upward.jsonl").exists() else []:
            try:
                self.upward.append(json.loads(line))
            except Exception:  # noqa: BLE001
                pass
        if (rd / "deepen.json").exists():
            self.deepen_nodes = json.loads((rd / "deepen.json").read_text(encoding="utf-8")).get("nodes", [])
            for n in self.deepen_nodes:
                if not n.get("parent"):
                    self.interrogated.update(n.get("members", []))
        verify = {}
        for line in (rd / "verify.jsonl").read_text(encoding="utf-8").splitlines() if (rd / "verify.jsonl").exists() else []:
            try:
                v = json.loads(line)
                verify[v["id"]] = v
            except Exception:  # noqa: BLE001
                pass
        rows = []
        for f in sorted((rd / "cands").glob("*.jsonl")) if (rd / "cands").exists() else []:
            for line in f.read_text(encoding="utf-8").splitlines():
                try:
                    r = json.loads(line)
                except Exception:  # noqa: BLE001
                    continue
                if r.get("id"):
                    rows.append(r)
        # the twin the run actually kept is the one with a verify record; duplicates never got one
        rows.sort(key=lambda r: (r["id"] not in verify, r.get("round", 0), r.get("ts", "")))
        for r in rows:
            if True:
                src_p = rd / "cands" / "src" / f"{r['id']}.py"
                program = src_p.read_text(encoding="utf-8") if src_p.exists() else ""
                c = Candidate(id=r["id"], text=r.get("text", ""), card=r.get("card", ""), operator=r.get("operator", ""),
                              seed=r.get("seed", ""), perm=0, round=r.get("round", 0), call_id=r.get("call_id", ""),
                              parent_ids=r.get("parent_ids") or [], lineage_id=r.get("lineage_id") or r["id"],
                              program=program, extra=r.get("extra") or {})
                key = c.extra.get("src_hash")
                if key and key in self.seen:
                    continue
                if key:
                    self.seen[key] = c.id
                self.cands.append(c)
                self.implemented.update(c.extra.get("members") or [])
                v = verify.get(c.id)
                if v:
                    self.vres[c.id] = {"status": v["status"], "rung_reached": v["details"]["rung_reached"],
                                       "partial_score": v.get("partial_score", 0.0), "feedback": v.get("feedback_record") or {},
                                       "metrics": v["details"].get("metrics", {}), "rungs": []}
                    self.history.append({"round": v.get("round", 0), "cand_id": c.id, "node": c.extra.get("node"),
                                         "hypothesis": c.extra.get("hypothesis", ""), "status": v["status"],
                                         "reason": (v.get("feedback_record") or {}).get("reason", ""),
                                         "learn_gap": v["details"].get("metrics", {}).get("learn_gap")})
        self.history.sort(key=lambda h: (h.get("round", 0), h.get("cand_id", "")))
        self.decisions.append({"step": "resume", "completed_rounds": self.completed_rounds, "cands": len(self.cands),
                               "sketches": len(self.sketches), "unverified": [c.id for c in self.cands if c.id not in self.vres],
                               "ts": now_ts()})

    # ------------------------------------------------------------ live status (read by nano/dashboard.py)
    def _live(self, phase: str | None = None, note: str | None = None) -> None:
        with self.lock:
            if phase is not None:
                self.phase = phase
            if note is not None:
                self.note = note
            data = {"phase": self.phase, "note": self.note, "spent": self.spent, "spent_aux": self.spent_aux,
                    "inflight": sorted(self.inflight.values(), key=lambda x: x["started"]), "ts": time.time()}
            target = self.run_dir / "live.json"
            for attempt in range(5):          # Windows: a reader may hold the file briefly
                try:
                    target.write_text(json.dumps(data), encoding="utf-8")
                    break
                except PermissionError:
                    time.sleep(0.05 * (attempt + 1))

    # ------------------------------------------------------------ setup
    def _load_profile(self) -> dict:
        """Baseline profile: parameter count and loss curves (cached), step time re-measured today."""
        if self.mode != "baseline":
            # Mode 2 and 3: nothing to measure yet. The reference (the best checked candidate) is profiled once it
            # exists; diagnostics, the cost card, the anomaly map and the fidelity probe need a baseline: skipped.
            self.do_diagnostics, self.fidelity = False, False
            self.cost_card, self.diagnostics_text, self.anomaly_text = "", "", ""
            if self.mode == "no_check":
                self.long_steps = 0                 # a proposal is read, not run: no long check
            self.decisions.append({"step": "baseline", "mode": self.mode,
                                   "note": "no baseline; the best checked candidate so far is the reference", "ts": now_ts()})
            return {}
        no_ladder =self.stop_after in ("ideated", "clustered", "deepened")   # nothing will be trained in this run
        if no_ladder:
            self._live("measuring the baseline briefly", "step time and the diagnostics only; no loss curves, since nothing is trained in this run")
        else:
            self._live("timing the baseline", "3 steps on the card today; loss curves at 45 and 240 steps are cached")
        cache = self.pf.get("baseline_cache") or {"real": f"{self.pf.name}_baseline_profile",
                                                  "mock": f"{self.pf.name}_baseline_profile_mock"}
        profile_dir = config.RUNS_DIR / cache["mock" if self.backend == "mock" else "real"]   # mock runs use short step counts: their own cache
        llm_checker = self.pf.checker == "llm"
        if not self.pf.diagnostics:                 # a profile without a diagnostics hook: no instrumented run, no anomaly map
            self.do_diagnostics = False
        prof = self.checker.baseline(profile_dir, baseline_path(),
                                     seeds=(self.pf.checker_args or {}).get("seeds") or self.checker.PROFILE_SEEDS,
                                     learn_steps=self.learn_steps, long_steps=self.long_steps, retime=True,
                                     curves=not no_ladder, diagnostics=self.do_diagnostics,       # ideas need the cost card and the diagnostics; only the ladder needs curves
                                     diag_steps=self.diag_steps, diag_seeds=self.anomaly_seeds)
        paths = [Path(p) for p in (prof.get("diagnostics_jsons") or []) if Path(p).exists()]
        if self.do_diagnostics and llm_checker and len(paths) >= 2:
            from nano import anomaly
            self.anomalies = anomaly.compute(paths, self.run_id, self.sham_share)
            self.anomaly_text = self.anomalies.get("text", "")
            write_json(self.run_dir / "anomalies.json", {k: v for k, v in self.anomalies.items() if k != "sham"})
            if self.anomalies.get("sham"):
                write_json(self.run_dir / "private" / "anomaly_sham.json", self.anomalies["sham"])   # never shown to agents
        try:
            from nano import cost as COST
            self.cost_card = COST.card(self.baseline_src, prof) if llm_checker else ""
        except Exception:  # noqa: BLE001
            self.cost_card = ""
        if self.do_diagnostics and not llm_checker:   # a profile's own "module:function" diagnostics text
            self.diagnostics_text = self._profile_diagnostics(prof)
        if self.do_diagnostics and prof.get("diagnostics_md"):
            try:
                self.diagnostics_text = Path(prof["diagnostics_md"]).read_text(encoding="utf-8")[:6000]
            except Exception:  # noqa: BLE001
                self.diagnostics_text = ""
        if llm_checker:
            failed = not prof.get("params_nonembed") or (not no_ladder and not prof.get("curve_short"))
        else:                                       # a generic checker: it says ok, or it gives a baseline score
            failed = prof.get("ok") is False or not (prof.get("ok") or prof.get("score") is not None
                                                     or prof.get("scores") or prof.get("seed_scores"))
        if failed:
            raise SystemExit("the baseline itself did not build or train; see "
                             f"{profile_dir} (errors: {prof.get('errors')})")
        return prof

    def _profile_diagnostics(self, prof: dict) -> str:
        """Measured-behaviour text from the profile's diagnostics hook ("module:function"); '' on any failure."""
        try:
            import importlib
            mod, _, fn = str(self.pf.diagnostics).partition(":")
            f = getattr(importlib.import_module(mod), fn or "text")
            return str(CheckerAdapter._call(f, baseline=prof) or "")[:6000]   # the hook reads the baseline measurement
        except Exception as e:  # noqa: BLE001
            self.decisions.append({"step": "diagnostics", "error": str(e)[:200]})
            return ""

    def history_text(self) -> str:
        """What was built so far and what happened: the record later rounds and interrogations read."""
        if not self.history:
            return ""
        lines = ["WHAT HAS ALREADY BEEN BUILT IN THIS RUN AND WHAT HAPPENED (do not repeat a failure; build on a success):"]
        for h in self.history[-40:]:
            lines.append(f"- round {h['round']} [{h.get('node') or '?'}] {h['hypothesis'][:110]} -> {h['status']}"
                         + (f": {h['reason'][:120]}" if h.get("reason") else "")
                         + (f" (learn gap {h['learn_gap']:+.3f}, z {h.get('learn_z')})" if h.get("learn_gap") is not None else "")
                         + (f" [prediction check: {h['prediction']}]" if h.get("prediction") else ""))
        if self.control_note:
            lines.append(f"NOTE FROM THE OWNER: {self.control_note}")
        return "\n".join(lines)

    def _call(self, prompt: str, role: str, max_tokens: int, meta: dict, model: str | None = None,
              tools: list[str] | None = None, max_turns: int | None = None, timeout: int | None = None) -> llm.CallResult:
        cid = new_id("c")
        (self.run_dir / "prompts" / f"{cid}.txt").write_text(prompt, encoding="utf-8")
        with self.lock:
            self.inflight[cid] = {"call_id": cid, "role": role, "card": meta.get("card"),
                                  "operator": meta.get("operator"), "seed": meta.get("seed"),
                                  "started": time.time(), "note": meta.get("note", "")}
        self._live()
        try:
            r = llm.call(prompt, role=role, call_id=cid, model=model or self.model, max_tokens=max_tokens,
                         backend=self.backend, log_dir=self.run_dir / "calls", meta=meta,
                         tools=tools, max_turns=max_turns, timeout=timeout, effort=self.effort_for(str(meta.get("card", ""))))
        finally:
            with self.lock:
                self.inflight.pop(cid, None)
        self._account(model, meta, r.usage)
        self._live()
        return r

    def _judge_call(self, prompt: str, meta: dict) -> str:
        """One blind judge call for the panel checker (Mode 3), logged and charged like every other call."""
        model = getattr(self.checker.impl, "judge_model", None)
        r = self._call(prompt, "judge", 1500, dict(meta), model=model)
        self._ledger("panel", str(meta.get("operator", "")), str(meta.get("seed", "")), r.call_id, r.usage,
                     self.round_now, "verify")
        return r.text or ""

    def _account(self, model: str | None, meta: dict, usage) -> None:
        """Only the inventing model's tokens count against the budget. The cheap model's retrieval and clerical
        calls run on their own meter: one web-research call reads its pages again on every search turn and
        counts about half a million tokens, which would otherwise empty the budget before a single build."""
        main = self.model or config.DEFAULT_MODEL
        with self.lock:
            if (model or main) == main:
                self.spent += usage.total_tokens
                st_ = budget_mod.stage_of(str(meta.get("card", "")))
                self.spent_by_stage[st_] = self.spent_by_stage.get(st_, 0) + usage.total_tokens
            else:
                self.spent_aux += usage.total_tokens

    def _aux_ok(self, note: str = "") -> bool:
        """Room on the cheap model's meter for another web call? Past its cap the run stops searching and goes
        on with what it has (logged once), instead of stopping."""
        if self.aux_budget <= 0 or self.spent_aux < self.aux_budget:
            return True
        with self.lock:
            if not self._aux_off_logged:
                self._aux_off_logged = True
                self.decisions.append({"round": self.round_now, "step": "budget", "refused": "web", "why": "aux budget",
                                       "spent_aux": self.spent_aux, "aux_budget": self.aux_budget, "note": note[:80]})
        return False

    EFFORT = {"build": "high", "interrogation": "medium", "judging": "low", "research": "low"}

    def effort_for(self, card: str) -> str | None:
        """Reasoning effort by role: high where the output is code or a repair, low for clerical roles, the
        default for sketching (research_notes/thinking_parts/06_reasoning.md item 8)."""
        if not self.effort_by_role:
            return None
        if card.endswith(":questions") or card.endswith(":findings"):
            return "low"
        return self.EFFORT.get(budget_mod.stage_of(card))

    def _check_web_facts(self, cl: dict) -> None:
        """Numeric claims the interrogation took from the web are checked against their own page by the research
        model before a build; an unsupported claim travels to the builder as a belief, never as a fact."""
        members = set(cl.get("members", []))
        roots = [n for n in self.deepen_nodes if not n.get("parent") and members & set(n.get("members", []))]
        todo = []
        for n in roots:
            for t in n.get("known_tagged") or []:
                if t.get("prov") == "web" and re.search(r"\d", t["text"]) and research.URL_RE.search(t["text"]) and not t.get("check"):
                    todo.append(t)
        todo = todo[:6]
        if not todo or not self._aux_ok("fact check"):
            return
        est = 6000 + 8000 * len(todo)
        if not self._afford("interrogation", est, "fact check"):
            return
        prompt = ("Check each claim against the page its URL points to. Fetch the page; do not search elsewhere. For each claim answer "
                  "SUPPORTED, NOT SUPPORTED or UNCLEAR, then '|' and the exact quote (or the fact on the page) that decides it. "
                  "A number that the page states differently is NOT SUPPORTED. Reply with one line per claim, numbered as given.\n\n"
                  + "\n".join(f"{i + 1}. {t['text']}" for i, t in enumerate(todo)))
        r = self._call(prompt, "research", 2500, {"card": "fact_check", "operator": cl["cluster_id"], "node": cl.get("node"),
                                                   "note": f"checking {len(todo)} web claims for '{cl['name']}'"},
                       model=self.research_model, tools=["WebFetch"], max_turns=2 * len(todo) + 2, timeout=900)
        self._ledger("fact_check", cl["cluster_id"], "", r.call_id, r.usage, self.round_now, "encode")
        verdicts = {}
        for m in re.finditer(r"^\s*(\d+)[.)]\s*(SUPPORTED|NOT SUPPORTED|UNCLEAR)\b\s*\|?\s*(.*)$", r.text or "", flags=re.M | re.I):
            verdicts[int(m.group(1))] = (m.group(2).lower(), m.group(3).strip()[:160])
        for i, t in enumerate(todo):
            v = verdicts.get(i + 1)
            t["check"], t["check_quote"] = (v[0], v[1]) if v else ("unclear", "")
        with self.lock:
            self.decisions.append({"round": self.round_now, "step": "fact_check", "idea": cl["cluster_id"], "n": len(todo),
                                   "not_supported": sum(1 for t in todo if t.get("check") == "not supported"), "ts": now_ts()})
            write_json(self.run_dir / "deepen.json", {"nodes": self.deepen_nodes})

    def _write_commitments(self) -> None:
        """What the run commits to before any idea exists, hashed into the state: a registered-report style record."""
        sc = self.pf.score or {}
        c = {"rules": list(self.pf.constraints),
             "win": {"margin_nats": sc.get("margin", 0.005), "alpha": sc.get("alpha", 0.01), "min_seeds": sc.get("min_seeds", 3)},
             "stackable": {"margin_nats": sc.get("stackable_margin", 0.002), "alpha": sc.get("stackable_alpha", 0.05)},
             "baseline_version": self.baseline_version,
             "baseline_hash": hashlib.sha1(self.baseline_src.encode()).hexdigest()[:12],
             "weights": dict(ideate.WEIGHTS), "weights_calibrated": bool(self.weights_from_ledger),
             "slots": {"k_impl": self.k_impl, "rounds": self.rounds, "per_node": self.per_node, "inward_share": self.inward_share,
                       "longshot_share": self.longshot_share, "leap_share": self.leap_share, "family_variants": self.family_variants},
             "models": {"model": self.model, "cheap": self.cheap_model, "research": self.research_model}, "web_mode": self.web_mode,
             "budget": self.B, "aux_budget": self.aux_budget, "stage_shares": self.stage_shares, "tune": {"on": self.tune, "knobs": self.tune_knobs or "default", "top": self.tune_top},
             "anomaly_seeds": self.anomaly_seeds, "sham_share": self.sham_share, "controls": self.controls, "lens": self.lens,
             "lens_design": self.lens_design,
             "aim": self.aim, "scope": sorted(self.only_nodes), **({"profile": self.pf.name} if self.pf.name != "llm" else {}),
             "digest": (hashlib.sha1(self.digest_text.encode()).hexdigest()[:12] if self.digest_text else None),
             "ts": now_ts()}
        write_json(self.run_dir / "commitments.json", c)
        h = hashlib.sha1(json.dumps(c, sort_keys=True, default=str).encode()).hexdigest()[:12]
        try:
            st = json.loads((self.run_dir / "state.json").read_text(encoding="utf-8"))
            st["commitments_hash"] = h
            write_json(self.run_dir / "state.json", st)
        except Exception:  # noqa: BLE001
            pass

    def _log_selection(self, by_node: dict, main: list, picks: list, done: set, weights: dict, wsum: float) -> None:
        """selection.jsonl: one row per group per round with the reason it was chosen or dropped (why this, not that)."""
        chosen = {c["cluster_id"]: "picked_main" for c in main}
        chosen.update({c["cluster_id"]: "picked_lane" for c in picks})
        cut = {}
        for c in main:
            d = c.get("direction", "")
            cut[d] = min(cut.get(d, 9e9), float(c.get("score") or 0.0))
        rows = []
        for nid, cl in by_node.items():
            for c in cl:
                cid = c["cluster_id"]
                if cid in chosen:
                    reason = chosen[cid]
                elif cid in done:
                    reason = "already built or excluded"
                elif float(c.get("score") or 0.0) >= cut.get(c.get("direction", ""), 9e9):
                    reason = "slots exhausted (scored at or above the cut; the turn went to another part)"
                else:
                    reason = "below the cut"
                rows.append({"round": self.round_now, "cluster_id": cid, "name": c.get("name"), "node": nid, "direction": c.get("direction"),
                             "score": c.get("score"), "rank": c.get("rank"), "kind_share": c.get("leap_share"), "reason": reason,
                             "lane_propensity": round(weights.get(cid, 0.0) / wsum, 3) if cid in weights else None,
                             "cut": cut.get(c.get("direction", ""))})
        for r in rows:
            append_jsonl(self.run_dir / "selection.jsonl", r)

    def _afford(self, stage: str, est: int, note: str = "") -> bool:
        """A call is paid for only if it fits the budget and, for a non-build call, leaves the builds their floor."""
        ok, why = budget_mod.afford(self.spent, est, self.B, stage, self.spent_by_stage.get("build", 0), self.stage_shares)
        if not ok:
            with self.lock:
                self.decisions.append({"round": self.round_now, "step": "budget", "refused": stage, "why": why, "est": est,
                                       "spent": self.spent, "note": note[:80]})
        return ok

    def _call_with_web(self, prompt: str, role: str, max_tokens: int, meta: dict, round_no: int, round_type: str,
                       model: str | None = None, context: str = "", tail: str = "") -> llm.CallResult:
        """A call that needs the web. Mode "delegate" (default): the model lists the questions it would look up,
        the research model answers them with sources, and the model then writes with the findings in front of
        it; the strong model never runs a search turn. Mode "self": one multi-turn call with web tools.
        Mode "off": a plain call. `tail` is the output format, appended after the findings."""
        mode = self.web_mode
        if mode == "delegate" and model and model == self.research_model:
            mode = "self"                              # the research model may search for itself
        if mode != "off" and not self._aux_ok(str(meta.get("card", ""))):
            mode = "off"                               # the cheap model's meter is full: write without the web
        if mode == "off":
            return self._call(prompt + tail, role, max_tokens, meta, model=model)
        if mode == "self":
            return self._call(prompt + tail, role, max_tokens, meta, model=model, tools=research.RESEARCH_TOOLS,
                              max_turns=40, timeout=1800)
        card = str(meta.get("card", ""))
        q = self._call(prompt + research.QUESTIONS_ADDENDUM, role, 1200,
                       {**meta, "card": card + ":questions", "note": "listing what to look up: " + str(meta.get("note", ""))[:80]},
                       model=model)
        self._ledger(card + ":questions", str(meta.get("operator", "")), str(meta.get("seed", "")), q.call_id, q.usage,
                     round_no, round_type)
        questions = research.parse_questions(q.text or "")
        findings = ""
        if questions:
            f = self._call(research.findings_prompt(questions, context), "research", 4000,
                           {**meta, "card": card + ":findings", "operator": str(meta.get("operator", "")),
                            "note": f"web research for {len(questions)} questions: " + str(meta.get("note", ""))[:60]},
                           model=self.research_model, tools=research.RESEARCH_TOOLS, max_turns=40, timeout=1800)
            self._ledger(card + ":findings", str(meta.get("operator", "")), "", f.call_id, f.usage, round_no, "encode")
            findings = (f.text or "").strip()
        block = ("\n\n" + research.FINDINGS_HEADER + "\n" + findings + "\n\n") if findings else "\n\n"
        return self._call(prompt + block + tail, role, max_tokens, {**meta, "questions": len(questions)}, model=model)

    def _ledger(self, card: str, operator: str, seed: str, call_id: str, usage: Usage, round_no: int,
                round_type: str, status: str | None = None, vtype: str | None = None, cand_id=None):
        from harness import ledger
        ledger.append(LedgerRow(run_id=self.run_id, batch=self.batch, benchmark="nano", item_id=spec_id(),
                                split="dev-tune", family="nano", cls="nano", arm="scaffold", card=card,
                                operator=operator, round_type=round_type, round=round_no, seed=seed,
                                perm=0, call_id=call_id, tokens=usage.to_dict(), verification_type=vtype,
                                status=status, cand_id=cand_id))

    def _baseline_line(self) -> str:
        """The BASELINE line of problem.md for a profile without its own baseline_summary."""
        prof = self.profile or {}
        parts = []
        for key in ("quick", "full"):
            if isinstance(prof.get(key), dict) and prof[key].get("mean") is not None:
                parts.append(f"{key} {self.pf.v('score_name', 'score')} {prof[key]['mean']:.4g} (seed sd {prof[key].get('sd')})")
        if prof.get("score") is not None:
            parts.append(f"{self.pf.v('score_name', 'score')} {prof['score']}")
        return "BASELINE (measured): " + ("; ".join(parts) if parts else "see the checker's baseline profile") + "."

    def _facts(self) -> list[dict]:
        """Mode 3: the profile's known facts, with their ids (problem.md lists them; proposals cite them)."""
        return [f for f in (self.pf.get("facts") or []) if isinstance(f, dict) and f.get("text")]

    def _no_baseline_lines(self) -> list[str]:
        """problem.md for Mode 2 and 3: there is no baseline; the interface (and, in Mode 3, the criteria and facts)."""
        pf = self.pf
        if self.mode == "no_check":
            crit = list(getattr(self.checker.impl, "criteria", None) or (pf.checker_args or {}).get("criteria") or [])
            k = getattr(self.checker.impl, "k", (pf.checker_args or {}).get("judges", 3))
            lines = ["BASELINE: none, and there is no objective score. Each proposal is read blind by a panel of "
                     f"{k} judges, each scoring it from 1 to 10 on the criteria below without seeing the other "
                     "proposals. People's opinions count at a bounded weight. The best proposal so far is the reference.",
                     "", "CRITERIA:"] + [f"- {c}" for c in crit]
            lines += ["", "FORM OF A PROPOSAL:", pf.interface]
            facts = self._facts()
            if facts:
                lines += ["", "KNOWN FACTS (cite at least one by its id):"] + [f"[{f.get('id')}] {f['text']}" for f in facts]
            return lines
        return ["BASELINE: none. Nothing has been solved yet, so there is no file to modify. Each candidate is a complete "
                f"new {pf.v('artifact', 'artifact')}. The best checked candidate so far becomes the reference, and later "
                "candidates are measured against it; the reference moves when a candidate beats it by the margin.",
                "", "INTERFACE (every candidate must implement this):", pf.interface]

    def encode(self) -> None:
        """problem.md from the fixed spec; a separate call writes private defaults (never routed)."""
        pf = self.pf
        sc = pf.score or {}
        cons = list(pf.constraints)
        aim = (self.aim or pf.aim or "").strip()
        problem = ["# Problem: " + str(pf.get("title") or pf.v("score_phrase") or pf.name),
                   "", "GOAL: " + str(pf.goal).strip(), ""]
        problem += (["PURPOSE: " + aim, ""] if aim else [])
        problem += ([tree.scope_text(self.only_nodes), ""] if self.only_nodes else [])
        summary = pf.get("baseline_summary")
        if self.mode != "baseline":
            problem += self._no_baseline_lines() + ["", "HARD CONSTRAINTS:"] + cons
        else:
            problem += [summary(self.profile) if callable(summary) else self._baseline_line(),
                        "", "HARD CONSTRAINTS:"] + cons
        (self.run_dir / "problem.md").write_text("\n".join(problem), encoding="utf-8")
        op = ">" if pf.lower_is_better else "better than"
        if self.mode == "no_check":
            bar = {"required_verification": "panel", "rungs_today": 3,
                   "rung_full": (f"blind panel of {getattr(self.checker.impl, 'k', 3)} judges on the profile's criteria, people's "
                                 f"opinions at a bounded weight; ranked against the best proposal so far (margin "
                                 f"{sc.get('margin', 0.5)} {sc.get('unit', 'points')})")}
        elif self.mode == "check_only":
            bar = {"required_verification": "execution", "rungs_today": 4,
                   "rung_full": (f"score by the harness; {op} {sc.get('margin', 0.005)} {sc.get('unit', '')} against the reference "
                                 "(the best checked candidate so far); no baseline exists")}
        else:
            bar = {"required_verification": "execution", "rungs_today": 4,
                   "rung_full": (f"exam by the harness; {op} {sc.get('margin', 0.005)} {sc.get('unit', 'nats')} and Welch "
                                 f"p < {sc.get('alpha', 0.01)} over >= {sc.get('min_seeds', 3)} seeds vs the pooled baseline")}
        write_json(self.run_dir / "constraints.json", {"checklist": cons, "bar": bar})
        if self.mode != "baseline":
            prompt = (f"Below is the goal of {pf.v('goal_short') or 'a good ' + pf.v('artifact', 'artifact')}. Nothing exists yet. "
                      "List the first five designs that come to mind, one per line, numbered, at most twelve words each. "
                      "No explanation.\n\nGOAL AND CONSTRAINTS:\n" + "\n".join(problem))
        else:
            intro = (f"Below is a {pf.v('artifact_long') or pf.v('artifact', 'artifact')} and the goal of "
                     f"{pf.v('goal_short') or 'improving its ' + pf.v('score_name', 'score')}.")
            prompt = (intro + " List the first five changes that come to mind, one per line, "
                      "numbered, at most twelve words each. No explanation.\n\nGOAL AND CONSTRAINTS:\n"
                      + "\n".join(problem) + f"\n\n{_artifact_word().upper()}:\n{_fence()}\n" + self.baseline_src + "\n```")
        r = self._call(prompt, "defaults", 400, {"card": "defaults"})
        write_json(self.run_dir / "private" / "defaults.json",
                   {"text": r.text, "call_id": r.call_id, "note": "never routed to any generator"})
        self.defaults_lines = ideate.parse_defaults(r.text or "")   # used only to tag clusters as obvious
        self._ledger("defaults", "none", "", r.call_id, r.usage, 0, "encode")

    # ------------------------------------------------------------ cards
    def _common(self, source: str, shuffle: bool, order_seed: str = "") -> str:
        cons = list(self.pf.constraints)
        if shuffle:                      # per-call RNG so parallel calls stay deterministic
            random.Random(f"cons:{self.rep}:{order_seed}").shuffle(cons)
        head = f"CURRENT {_artifact_word().upper()} (modify this)"
        if self.mode != "baseline" and source in (self.baseline_src, _strip_comments(self.baseline_src)):
            head = ("FORM OF A PROPOSAL (write every section)" if self.mode == "no_check"
                    else "THERE IS NO BASELINE. SKELETON OF THE FILE TO WRITE (complete it to the interface above)")
        return ((self.run_dir / "problem.md").read_text(encoding="utf-8").split("HARD CONSTRAINTS:")[0]
                + "HARD CONSTRAINTS:\n" + "\n".join(cons)
                + (("\n\n" + self.cost_card) if getattr(self, "cost_card", "") else "")
                + f"\n\n{head}:\n{_fence()}\n" + source + "\n```\n\n")

    def spec_prompt(self, card: str, seed: str, operator: str, parent: Candidate | None,
                    feedback: dict | None) -> str:
        if card == "seeded":
            return self._common(self.working_src, True, seed) + f"Starting point: {seed}\n\n" + self.control_history() + output_format()
        if card == "low_prior":
            return (self._common(_strip_comments(self.working_src), True, "low_prior") + self.control_history()
                    + f"The {_artifact_word()} above is given without its comments. Propose one change to the parts "
                      "of the computation that the constraints do not fix.\n\n" + output_format())
        if card == "transform":
            return (self._common(self.baseline_src, True, operator)
                    + f"The current {_artifact_word()} assumes that {operator}. Design the change under the opposite "
                      f"assumption, keeping every constraint.\n\n" + output_format())
        if card == "formal":
            return self._common(self.working_src, False) + self.control_history() + output_format()
        if card == "implement":     # one file per selected idea cluster (operator = cluster id)
            cl = next(c for c in self.clusters if c["cluster_id"] == operator)
            node = next((n for n in (self.tree or []) if n["id"] == cl.get("node")), None)
            if self.fact_check:
                self._check_web_facts(cl)
            scope = ""
            members_ = set(cl.get("members", []))
            roots_ = [n for n in self.deepen_nodes if not n.get("parent") and members_ & set(n.get("members", []))]
            self._manifest[cl["cluster_id"]] = {
                "members": sorted(members_), "cards": list(cl.get("cards", [])), "node": cl.get("node"), "direction": cl.get("direction"),
                "lane": cl.get("lane", "main"), "lane_propensity": cl.get("lane_propensity"), "score": cl.get("score"), "rank": cl.get("rank"),
                "prior": cl.get("prior"), "obvious": bool(cl.get("obvious")), "leap_share": cl.get("leap_share"),
                "deepen_roots": [n["id"] for n in roots_], "n_facts": sum(len(n.get("known", [])) for n in roots_),
                "n_objections": sum(len(n.get("objections") or []) for n in roots_), "chain_links": sum(len(n.get("chain") or []) for n in roots_),
                "cost_card": bool(self.cost_card), "anomaly_rows": len((self.anomalies or {}).get("anomalies") or []),
                "identity_init": bool(self.identity_init), "round": self.round_now}
            if node and self.mode != "baseline":
                scope = (f"PART: {node['name']} ({cl.get('direction')} direction). The idea centres on this part: "
                         f"{node['boundary']}.\n\n")
            elif node:
                rules = self.pf.v("boundary_rules")
                scope = (f"PART: {node['name']} ({cl.get('direction')} direction). CODE THIS CHANGE MAY TOUCH: "
                         f"{node['boundary']}. Everything outside it stays identical." + (" " + rules if rules else "") + "\n\n")
                if self.identity_init and self.pf.v("identity_rule"):
                    scope += self.pf.v("identity_rule") + "\n\n"
            if self.mode == "no_check":
                return (self._common(self.baseline_src, False) + scope
                        + "Write exactly this idea as a complete proposal with all five sections (CLAIM, FROM THE FACTS TO "
                          "THE IDEA, FROM THE IDEA TO THE RESULT, WEAK POINTS, PROPOSED TEST). Cite at least one known "
                          "fact by its id. Do not write code.\n\n"
                        + ideate.implement_brief(cl, self.sketches, self.knowledge_for(cl)) + "\n\n" + output_format())
            if self.mode == "check_only":
                return (self._common(self.baseline_src, False) + scope
                        + "Implement exactly this idea. There is no baseline to modify: write the COMPLETE file that "
                          f"implements the interface ({self.pf.v('artifact_file', 'the file')}), every line, from the "
                          "skeleton above.\n\n"
                        + ideate.implement_brief(cl, self.sketches, self.knowledge_for(cl)) + "\n\n" + output_format())
            return (self._common(self.baseline_src, False) + scope
                    + f"Implement exactly this idea as a complete modified {_artifact_word()}:\n\n"
                    + ideate.implement_brief(cl, self.sketches, self.knowledge_for(cl)) + "\n\n" + output_format())
        if card == "program":       # arm: evolve one named function with continuous fitness (program-space search)
            sym = operator
            prev = []
            for c in self.cands:
                m = self.vres.get(c.id, {}).get("metrics") or {}
                if c.card == "program" and m.get("learn_z") is not None:
                    prev.append((m["learn_z"], c))
            prev.sort(key=lambda t: t[0])
            shown = "\n\n".join(f"# version with matched-step z {z:+.2f} (lower is better):\n{self._symbol_text(c.program or '', sym)}" for z, c in prev[:2])
            return (self._common(self.baseline_src, False)
                    + f"PROGRAM SEARCH. Change ONLY the function or class `{sym}` (and Config fields it needs). "
                    f"Everything else stays identical. Variation {seed}: propose a new version that differs in mechanism from "
                    f"the versions below, not only in constants. Other variations are being asked for at the same time; "
                    f"yours must change {self._program_family(seed)}.\n\n"
                    + (f"BEST PREVIOUS VERSIONS:\n{shown}\n\n" if shown else "")
                    + output_format())
        if card == "docs":          # SOC-02 / I6: a retrieved-document pack as a seed (structural, no persona)
            digest = _doc_text("reference")
            return (self._common(self.working_src, True, "docs")
                    + PF.fill("REFERENCE MATERIAL ({v:reference_what}; {v:reference_use}):\n\n")
                    + digest + "\n\n" + self.control_history() + output_format())
        if card == "revise":
            assert parent is not None
            fb = json.dumps(feedback or {}, indent=1)[:3000]
            near = bool((feedback or {}).get("near_miss"))
            from nano import lessons as LS
            card = LS.failure_card(feedback)
            know = self.knowledge_for({"members": parent.extra.get("members") or [], "node": parent.extra.get("node")})
            spec_lines = [f"IDEA: {parent.extra.get('hypothesis', '')}"]
            for k, label in (("target", "TARGET"), ("kind", "KIND"), ("kill", "KILL")):
                if parent.extra.get(k):
                    spec_lines.append(f"{label}: {parent.extra[k]}")
            return (self._common(parent.program or self.baseline_src, False)
                    + f"The {_artifact_word()} above is a previous attempt at this idea:\n" + "\n".join(spec_lines) + "\n\n"
                    + ("It passed the first checks, a near miss or better from the ambitious lane.\n" if near
                       else "It failed verification. The record:\n")
                    + card + "\n\n" + (know + "\n\n" if know else "")
                    + f"Apply the operator '{operator}': fix = repair the failure while keeping the idea; "
                      f"specialize = keep the idea but apply it to a smaller part of the {self.pf.v('system', 'system')}; "
                      "recurse = take the idea one step further; "
                      f"variant:narrow = keep the mechanism but apply it to a smaller part ({self.pf.v('narrow_examples', 'a narrower case')}); "
                      "variant:relax = keep the mechanism but let it start at identity and learn its strength, or halve it; "
                      "variant:strengthen = keep the mechanism but apply it more widely or more strongly.\n\n" + output_format())
        raise ValueError(card)

    @staticmethod
    def _symbol_text(src: str, name: str) -> str:
        """The source text of one top-level function or class, or '' if absent."""
        import ast as _ast
        try:
            tree_ = _ast.parse(src)
        except SyntaxError:
            return ""
        lines = src.splitlines()
        for node in tree_.body:
            if getattr(node, "name", None) == name:
                start = min([d.lineno for d in getattr(node, "decorator_list", [])] + [node.lineno]) - 1
                return "\n".join(lines[start: node.end_lineno])
        return ""

    def run_card(self, card: str, round_no: int, operator: str = "none", seed: str = "",
                 parent: Candidate | None = None, feedback: dict | None = None,
                 round_type: str = "first") -> Candidate | None:
        prompt = self.spec_prompt(card, seed, operator, parent, feedback)
        max_out = getattr(self, "max_out", 12000)   # a full train.py is ~5k tokens plus reasoning
        est = len(prompt) // 4 + max_out
        if not self._afford("build", est, card):
            self.decisions.append({"round": round_no, "step": "spawn", "action": "budget_skip",
                                   "card": card, "spent": self.spent, "est": est})
            return None
        note = {"seeded": f"seed word: {seed}", "low_prior": "comments stripped, constraints only",
                "transform": f"opposite of: {operator}", "formal": "direct rewrite",
                "docs": (self.pf.docs or {}).get("reference_note", "reads the reference document"),
                "implement": "writing the file for idea cluster " + (next((c["name"] for c in self.clusters if c["cluster_id"] == operator), operator) if card == "implement" else ""),
                "program": f"program search on {operator}, variation {seed}",
                "revise": f"{operator} on {parent.id if parent else '?'}"}.get(card, "")
        r = self._call(prompt, "generate", max_out, {"card": card, "operator": operator, "seed": seed, "note": note})
        parsed = _parse(r.text or "")
        cand = None
        if parsed:
            cid = new_id("n")
            key = hashlib.sha1(_norm_source(parsed["source"]).encode()).hexdigest()[:12]
            node_tag = {}
            if card == "program":
                node_tag = {"node": "program", "direction": "inward", "cluster": f"program:{operator}", "lane": "program"}
            if card == "revise" and parent is not None:
                node_tag = {k: parent.extra.get(k) for k in ("node", "direction", "cluster", "members", "prediction", "sketch_card") if parent.extra.get(k)}
                if round_type == "fix":
                    card = "fix"                      # a same-round repair of a rung 0/1 failure
                if str(operator).startswith("variant:"):
                    node_tag["lane"], node_tag["kind"], node_tag["leap_op"] = "family", parent.extra.get("kind", ""), parent.extra.get("leap_op", "")
            if card == "implement":   # credit the originating sketch cards; keep the cluster id as operator
                cl = next((c for c in self.clusters if c["cluster_id"] == operator), None)
                card = "impl:" + "+".join(cl["cards"]) if cl else "implement"
                if cl:
                    rep = next((s for s in self.sketches if s["id"] == cl.get("representative")), {})
                    node_tag = {"node": cl.get("node"), "direction": cl.get("direction"), "cluster": cl.get("name"),
                                "members": list(cl.get("members", [])), "prediction": rep.get("prediction", ""),
                                "sketch_card": rep.get("card"), "lane": cl.get("lane", "main"), "target": rep.get("target", ""),
                                "scope": rep.get("scope", ""), "metric_blind": bool(rep.get("metric_blind")),
                                "kind": rep.get("kind", ""), "leap_op": rep.get("leap_op", ""), "kill": rep.get("kill", ""),
                                "manifest": self._manifest.get(operator)}
            node_tag["fidelity"], node_tag["fidelity_note"] = parsed.get("fidelity", ""), parsed.get("fidelity_note", "")
            if parsed.get("fidelity") in ("substituted", "cannot", "partial"):
                self.decisions.append({"round": round_no, "step": "fidelity", "cand": cid, "declared": parsed["fidelity"],
                                       "note": parsed.get("fidelity_note", "")[:120], "ts": now_ts()})
                nid = node_tag.get("node")
                node_ = next((n for n in (self.tree or []) if n["id"] == nid), None)
                if node_ is not None and parsed["fidelity"] == "cannot" and parsed.get("fidelity_note"):
                    node_.setdefault("idea_assumptions", tree.idea_assumptions(node_)).append(
                        {"from": operator if str(card).startswith("impl") else cid, "round": round_no, "kind": "could_not_build",
                         "text": f"could not be built within the rules: {parsed['fidelity_note'][:120]}"})
            cand = Candidate(id=cid, text=f"{parsed['hypothesis']} | {parsed['change']}", card=card,
                             operator=operator, seed=seed, perm=0, round=round_no, call_id=r.call_id,
                             parent_ids=[parent.id] if parent else [],
                             lineage_id=(parent.lineage_id or parent.id) if parent else cid,
                             program=parsed["source"], extra={"hypothesis": parsed["hypothesis"],
                                                              "change": parsed["change"], "src_hash": key, **node_tag})
            (self.run_dir / "cands" / "src" / f"{cid}.py").write_text(parsed["source"], encoding="utf-8")
        row = cand.to_dict() if cand else {"id": None, "card": card, "call_id": r.call_id, "parse_failed": True}
        if cand:
            row["program"] = f"cands/src/{cand.id}.py"      # keep the jsonl small; the source is a file
        append_jsonl(self.run_dir / "cands" / f"{r.call_id}.jsonl", row)
        self._ledger(card, operator, seed, r.call_id, r.usage, round_no, round_type,
                     cand_id=cand.id if cand else None)
        return cand

    # ------------------------------------------------------------ verify
    def verify(self, cand: Candidate, round_no: int) -> dict:
        out = self.run_dir / "verify" / cand.id
        self._live(f"round {round_no}: verifying on the GPU",
                   f"{cand.id} ({cand.card}): boundary diff, build, 3 steps, {self.learn_steps} matched steps")
        node = next((n for n in (self.tree or []) if n["id"] == (cand.extra or {}).get("node")), None)
        boundary = (node or {}).get("boundary") if self.arm == "scaffold" else "everything (control arm)"
        if cand.card == "compose":
            boundary = "everything (composite of two checked candidates)"
        if cand.card == "program" and self.program_search:
            boundary = self.program_search
        if self.mode != "baseline":
            # no baseline: rung 0 is the static rule only (no diff against a baseline source); gaps are measured
            # against the reference (empty until the first candidate is checked); verdicts by hash are not reused,
            # since the reference they were measured against may differ
            rec = self.checker.check(self.run_dir / "cands" / "src" / f"{cand.id}.py", out, self.profile,
                                     learn_steps=self.learn_steps, rung_max=3, boundary=None, baseline_src=None,
                                     lenient=(cand.extra.get("lane") == "longshot"), audit=self.backend != "mock",
                                     facts=self._fact_texts(), opinions=self._opinions_for(cand))
            rec["lane"] = cand.extra.get("lane", "main")
            self._update_reference(cand, rec, round_no)
        else:
            rec = self._recall_hash(cand)
            if rec is not None:
                self.decisions.append({"round": round_no, "step": "verify", "reused": cand.id, "from": rec["reused_from"]})
            else:
                rec = self.checker.check(self.run_dir / "cands" / "src" / f"{cand.id}.py", out, self.profile,
                                         learn_steps=self.learn_steps, rung_max=3,
                                         boundary=boundary, baseline_src=self.baseline_src,
                                         lenient=(cand.extra.get("lane") == "longshot"), audit=self.backend != "mock")
        rec["lane"] = cand.extra.get("lane", "main")
        pc = predict.check_prediction(predict.parse_prediction(cand.extra.get("prediction", "")), rec["metrics"], self.profile)
        rec["prediction_check"] = pc
        self.history.append({"round": round_no, "cand_id": cand.id, "node": (cand.extra or {}).get("node"),
                             "hypothesis": cand.extra.get("hypothesis", ""), "status": rec["status"],
                             "reason": (rec.get("feedback") or {}).get("reason", ""),
                             "learn_gap": rec["metrics"].get("learn_gap"), "learn_z": rec["metrics"].get("learn_z"),
                             "prediction": "; ".join(pc["details"]) if pc.get("checkable") else ""})
        row = {"id": cand.id, "status": rec["status"], "verification_type": "execution",
               "attempts": 1, "partial_score": rec["partial_score"], "surprise": False,
               "repr_change_event": False, "feedback_record": rec["feedback"],
               "details": {"rung_reached": rec["rung_reached"], "metrics": rec["metrics"]},
               "prediction_check": pc, "reused_from": rec.get("reused_from"),
               "call_ids": [], "round": round_no, "ts": now_ts()}
        append_jsonl(self.run_dir / "verify.jsonl", row)
        self._ledger(cand.card, cand.operator, cand.seed, cand.call_id, Usage(), round_no, "verify",
                     status=rec["status"], vtype="execution", cand_id=cand.id)
        self.vres[cand.id] = rec
        if rec["status"] == "checked" and not cand.card.startswith("control"):
            (self.run_dir / "pool" / f"{cand.id}.py").write_text(cand.program or "", encoding="utf-8")
            if self.mode == "no_check":                  # a proposal: also as markdown, for people to read
                (self.run_dir / "pool" / f"{cand.id}.md").write_text(cand.program or "", encoding="utf-8")
            write_json(self.run_dir / "pool" / f"{cand.id}.json",
                       {"id": cand.id, "card": cand.card, "operator": cand.operator, "seed": cand.seed,
                        "lineage_id": cand.lineage_id, "parent_ids": cand.parent_ids,
                        "hypothesis": cand.extra.get("hypothesis"), "change": cand.extra.get("change"),
                        "node": cand.extra.get("node"), "direction": cand.extra.get("direction"),
                        "src_hash": cand.extra.get("src_hash"), "arm": self.arm, "baseline_version": self.baseline_version,
                        "lane": cand.extra.get("lane", "main"), "target": cand.extra.get("target"), "metrics": rec["metrics"],
                        "kind": cand.extra.get("kind", ""), "leap_op": cand.extra.get("leap_op", ""), "manifest": cand.extra.get("manifest")})
        self._remember_hash(cand, rec)
        return rec

    # ------------------------------------------------------------ memory of verdicts by source hash (across runs)
    def _load_hash_memory(self) -> dict:
        p = config.MEMORY_DIR / "experiments" / "verified_by_hash.json"
        try:
            return json.loads(p.read_text(encoding="utf-8"))
        except Exception:  # noqa: BLE001
            return {}

    def _remember_hash(self, cand: Candidate, rec: dict) -> None:
        if self.backend == "mock":
            return
        key = cand.extra.get("src_hash")
        if not key:
            return
        p = config.MEMORY_DIR / "experiments" / "verified_by_hash.json"
        self.hash_memory[key] = {**self.hash_memory.get(key, {}), "ladder": {
            "status": rec["status"], "rung_reached": rec["rung_reached"], "metrics": rec["metrics"],
            "feedback": rec.get("feedback"), "run": self.run_id, "cand_id": cand.id,
            "baseline_version": self.baseline_version, "learn_steps": self.learn_steps, "ts": now_ts()}}
        p.parent.mkdir(parents=True, exist_ok=True)
        write_json(p, self.hash_memory)

    def _recall_hash(self, cand: Candidate) -> dict | None:
        """An identical script already went up the ladder against this baseline: reuse its record."""
        e = (self.hash_memory.get(cand.extra.get("src_hash") or "") or {}).get("ladder")
        if not e or e.get("baseline_version") != self.baseline_version or e.get("run") == self.run_id:
            return None
        if e.get("learn_steps") not in (None, self.learn_steps):
            return None                                   # measured under other settings
        if e.get("status") != "checked" and int(e.get("rung_reached") or 0) >= 2:
            return None                                   # a timing or learning failure is noisy: measure again
        return {"candidate": cand.id, "rungs": [], "status": e["status"], "rung_reached": e["rung_reached"],
                "partial_score": {"checked": 0.75}.get(e["status"], e["rung_reached"] / 4), "feedback": e.get("feedback") or {},
                "metrics": dict(e.get("metrics") or {}), "reused_from": f"{e.get('run')}/{e.get('cand_id')}"}

    # ------------------------------------------------------------ Mode 2 and 3: the reference (docs/GENERIC_SPEC.md 6)
    def _fact_texts(self) -> list:
        """Facts a proposal may name (Mode 3 lint): the interrogation's sourced facts; the checker adds the profile's."""
        out = []
        for n in self.deepen_nodes:
            for k in n.get("known", []) or []:
                t = k if isinstance(k, str) else (k.get("text") or k.get("fact") or "") if isinstance(k, dict) else ""
                if str(t).strip():
                    out.append(str(t)[:300])
        return out[:200]

    def _opinions_for(self, cand: Candidate) -> list[dict]:
        """People's opinions on this candidate from control.json["opinions"] (by candidate id, cluster id or name)."""
        try:
            ctl = json.loads((self.run_dir / "control.json").read_text(encoding="utf-8"))
        except Exception:  # noqa: BLE001
            return []
        keys = {cand.id, str(cand.operator), str((cand.extra or {}).get("cluster") or "")} - {""}
        return [o for o in (ctl.get("opinions") or []) if isinstance(o, dict)
                and (str(o.get("candidate", "")) in keys or str(o.get("cluster", "")) in keys)]

    def _update_reference(self, cand: Candidate, rec: dict, round_no: int) -> None:
        """The reference is the best checked candidate so far. The first checked candidate becomes it; a later one
        replaces it when it beats it by the profile's margin (the full-level gap when there is one)."""
        if rec.get("status") != "checked" or cand.card.startswith("control"):
            return
        m = rec.get("metrics") or {}
        if self.reference is None:
            self._set_reference(cand, rec, round_no, "the first checked candidate")
            return
        gap = m.get("long_gap") if m.get("long_gap") is not None else m.get("learn_gap")
        margin = float((self.pf.score or {}).get("margin", 0.0) or 0.0)
        if gap is not None and gap < -margin:
            self._set_reference(cand, rec, round_no, f"beats the reference {self.reference['cand_id']} by {-gap:.4g} "
                                                     f"(margin {margin:g}; negative gap is better)", gap=gap)

    def _set_reference(self, cand: Candidate, rec: dict, round_no: int, reason: str, gap: float | None = None) -> None:
        src = self.run_dir / "cands" / "src" / f"{cand.id}.py"
        out = self.run_dir / "reference" / cand.id
        self._live(note=f"measuring the new reference {cand.id}")
        seeds = (self.pf.checker_args or {}).get("seeds") or self.checker.PROFILE_SEEDS
        try:
            prof = self.checker.measure_reference(src, out, seeds=seeds, opinions=self._opinions_for(cand))
        except Exception as e:  # noqa: BLE001
            prof = {"ok": False, "errors": [str(e)[:300]]}
        if not prof or prof.get("ok") is False:
            self.decisions.append({"round": round_no, "step": "reference", "action": "measure_failed", "cand": cand.id,
                                   "errors": (prof or {}).get("errors"), "ts": now_ts()})
            print(f"[nano] reference: measuring {cand.id} failed; the reference stays "
                  f"{self.reference['cand_id'] if self.reference else 'unset'}", flush=True)
            return
        prev = self.reference
        self.reference = {"cand_id": cand.id, "path": str(src), "metrics": dict(rec.get("metrics") or {}),
                          "round": round_no, "reason": reason, "hypothesis": (cand.extra or {}).get("hypothesis", ""),
                          "set_at": now_ts()}
        self.profile = prof
        entry = {"round": round_no, "action": "set" if prev is None else "moved",
                 "from": prev["cand_id"] if prev else None, "to": cand.id, "reason": reason, "gap": gap, "ts": now_ts()}
        self.reference_log.append(entry)
        self.decisions.append({"step": "reference", **entry})
        print(f"[nano] reference {entry['action']}: {entry['from'] or '-'} -> {cand.id} | {reason}", flush=True)
        self._relabel_all(rec, cand.id, round_no)
        write_json(self.run_dir / "reference.json", {"reference": self.reference, "log": self.reference_log,
                                                    "profile": {k: v for k, v in prof.items() if k not in ("errors",)}})
        if prev is not None and self.retest_on_reference_change:
            self._retest_top(3, cand.id, round_no)

    def _relabel_all(self, new_rec: dict, new_id_: str, round_no: int) -> None:
        """Earlier gaps re-labelled against the new reference from the scores they already have (nothing is re-run)."""
        from nano.checks.reference import relabel
        lower = self.pf.lower_is_better
        recs = {cid: r for cid, r in self.vres.items()}
        recs[new_id_] = new_rec
        changed = []
        for cid, r in recs.items():
            m = r.get("metrics") or {}
            if m.get("learn_score") is None and m.get("panel_score") is None:
                continue
            upd = relabel(self.checker, m, self.profile, lower)
            if not upd:
                continue
            m.update(upd)
            changed.append(cid)
            for h in self.history:
                if h.get("cand_id") == cid:
                    h["learn_gap"], h["learn_z"] = m.get("learn_gap"), m.get("learn_z")
            pj = self.run_dir / "pool" / f"{cid}.json"
            if pj.exists():
                d = json.loads(pj.read_text(encoding="utf-8"))
                d["metrics"] = m
                write_json(pj, d)
            if cid != new_id_:                         # the new reference's own row is written by verify()
                append_jsonl(self.run_dir / "verify.jsonl",
                             {"id": cid, "status": r["status"], "verification_type": "execution", "attempts": 1,
                              "partial_score": r.get("partial_score", 0.0), "feedback_record": r.get("feedback") or {},
                              "details": {"rung_reached": r.get("rung_reached", 0), "metrics": m},
                              "relabelled_against": new_id_, "round": round_no, "ts": now_ts()})
        self.decisions.append({"round": round_no, "step": "relabel", "reference": new_id_, "candidates": changed, "ts": now_ts()})

    def _retest_top(self, n: int, ref_id: str, round_no: int) -> None:
        """--retest-on-reference-change: the top n other checked candidates are checked again against the new reference."""
        def key(c):
            m = self.vres[c.id].get("metrics") or {}
            g = m.get("long_gap") if m.get("long_gap") is not None else m.get("learn_gap")
            return (g is None, g if g is not None else 0.0)
        top = sorted([c for c in self.cands if c.id != ref_id and self.vres.get(c.id, {}).get("status") == "checked"
                      and not c.card.startswith("control")], key=key)[:n]
        for c in top:
            rec = self.checker.check(self.run_dir / "cands" / "src" / f"{c.id}.py", self.run_dir / "verify" / f"{c.id}_retest_{ref_id}",
                                     self.profile, learn_steps=self.learn_steps, rung_max=3, boundary=None, baseline_src=None,
                                     lenient=(c.extra.get("lane") == "longshot"), audit=self.backend != "mock",
                                     facts=self._fact_texts(), opinions=self._opinions_for(c))
            rec["lane"] = c.extra.get("lane", "main")
            rec["retested_against"] = ref_id
            self.vres[c.id] = rec
            append_jsonl(self.run_dir / "verify.jsonl",
                         {"id": c.id, "status": rec["status"], "verification_type": "execution", "attempts": 2,
                          "partial_score": rec["partial_score"], "feedback_record": rec["feedback"],
                          "details": {"rung_reached": rec["rung_reached"], "metrics": rec["metrics"]},
                          "retested_against": ref_id, "round": round_no, "ts": now_ts()})
            print(f"[nano] retest   {c.id} against {ref_id} -> {rec['status']} gap {rec['metrics'].get('learn_gap')}", flush=True)
        self.decisions.append({"round": round_no, "step": "retest", "reference": ref_id, "candidates": [c.id for c in top], "ts": now_ts()})

    def control_history(self) -> str:
        """For the control arms: what was built and what happened, in the autoresearch style."""
        if self.arm == "scaffold" or not self.history:
            return ""
        return self.history_text() + "\n\n"

    def long_runs(self) -> None:
        """Rung 4 for every checked candidate: the long matched-step gap ranks the pool for the overnight run."""
        pool = [c for c in self.cands if (self.vres.get(c.id, {}).get("status") == "checked" or c.id in self.hedged)
                and not c.card.startswith("control")]
        for i, c in enumerate(pool):
            self._live("long runs on the GPU", f"{i + 1}/{len(pool)}: {c.id}, {self.long_steps} matched steps")
            res = self.checker.long_run(self.run_dir / "cands" / "src" / f"{c.id}.py", self.run_dir / "verify" / c.id,
                                   self.profile, long_steps=self.long_steps)
            if self.fidelity and self.pf.checker == "llm" and c.extra.get("target") and res.get("ok"):
                fid = self.checker.fidelity_probe(self.run_dir / "cands" / "src" / f"{c.id}.py", self.run_dir / "verify" / c.id,
                                                  self.profile, c.extra["target"], steps=min(60, self.diag_steps))
                if fid is not None:                     # a checker without a fidelity probe leaves it out
                    res["fidelity"] = fid
                    self.vres[c.id]["metrics"]["fidelity"] = fid
            self.vres[c.id]["metrics"].update({k: v for k, v in res.items() if k in (
                "long_loss", "long_base", "long_gap", "long_sd", "long_z", "half_gap", "half_z", "trend", "extrap_gap", "extrap_z")})
            self.vres[c.id]["long"] = res
            self._resolve_objections(c, self.vres[c.id])               # long_z, trend and fidelity are known now
            pj = self.run_dir / "pool" / f"{c.id}.json"
            if pj.exists():
                d = json.loads(pj.read_text(encoding="utf-8"))
                d["metrics"] = self.vres[c.id]["metrics"]
                d["long"] = res
                write_json(pj, d)
            rec = self.vres[c.id]
            append_jsonl(self.run_dir / "verify.jsonl",
                         {"id": c.id, "status": rec["status"], "verification_type": "execution", "attempts": 1,
                          "partial_score": rec["partial_score"], "feedback_record": rec["feedback"],
                          "details": {"rung_reached": 4 if res.get("ok") else rec["rung_reached"], "metrics": rec["metrics"]},
                          "prediction_check": rec.get("prediction_check"), "reused_from": rec.get("reused_from"),
                          "long": res, "round": c.round, "ts": now_ts()})

    # ------------------------------------------------------------ loop
    def dedup(self, new: list[Candidate], round_no: int) -> list[Candidate]:
        kept, rows = [], []
        for c in new:
            key = c.extra["src_hash"]
            if key in self.seen:
                rows.append({"cluster_id": self.seen[key], "rule": "source_hash", "members": [c.id],
                             "representative_id": self.seen[key], "round": round_no})
                continue
            self.seen[key] = c.id
            kept.append(c)
        if rows:
            append_jsonl(self.run_dir / "clusters.jsonl", rows)
        return kept

    def run(self) -> dict:
        t0 = time.time()
        self.digest_text = (Path(self.digest_file).read_text(encoding="utf-8").strip()
                            if self.digest_file and Path(self.digest_file).exists() else "")
        if not (self.resume and (self.run_dir / "state.json").exists()):
            write_json(self.run_dir / "state.json", {"run_id": self.run_id, "item_id": spec_id(), "benchmark": "nano",
                       "arm": self.arm, "backend": self.backend, "model": self.model or config.DEFAULT_MODEL,
                       "B": self.B, "aux_budget": self.aux_budget, "rounds": self.rounds, "lens": self.lens,
                       "lens_design": self.lens_design, "baseline_version": self.baseline_version, "decisions": []})
        self._write_commitments()
        if self.resume:
            self.load_state()
        self.profile = self._load_profile()
        if not (self.resume and (self.run_dir / "problem.md").exists() and self.defaults_lines):
            self._live("encoding", "writing problem.md and the private defaults")
            self.encode()
        if self.arm in ("plain", "climb"):
            return self.run_control(t0)
        try:
            return self._rounds(t0)
        except StopRun as e:
            self.decisions.append({"step": "stopped", "after": str(e), "ts": now_ts()})
            return self._finish(t0)

    def _rounds(self, t0: float) -> dict:
        seeds = _seeds()
        revise_queue: list[tuple[Candidate, dict]] = []
        ledger_path = config.MEMORY_DIR / "experiments" / "ledger.jsonl"
        for line in ledger_path.read_text(encoding="utf-8").splitlines() if ledger_path.exists() else []:
            try:
                row = json.loads(line)
                same = row.get("baseline_version", "v1") == self.baseline_version
                keep = same or row.get("status") in ("verified", "stackable")   # an old-version failure does not block its retry
                if row.get("hypothesis") and keep and not str(row.get("run", "")).startswith("mock"):
                    self.ledger_texts[f"ledger:{row.get('run')}/{row.get('cand_id')}"] = str(row["hypothesis"])
            except Exception:  # noqa: BLE001
                pass
        if self.weights_from_ledger:
            from nano import calibrate as CAL
            sug = CAL.suggest_weights(min_rows=100)
            if sug:
                self.select_weights = sug["weights"]
                self.decisions.append({"step": "weights_from_ledger", "n_rows": sug["n"], "weights": sug["weights"]})
        if self.resume:
            pending = [c for c in self.cands if c.id not in self.vres]   # built before the interruption, never verified
            for c in pending:
                rec = self.verify(c, c.round or self.completed_rounds + 1)
                print(f"[nano] resume   {c.card:9s} {c.id} -> {rec['status']} rung {rec['rung_reached']} (verified after resume)", flush=True)
            near = sorted([c for c in self.cands if self.vres.get(c.id, {}).get("status") == "fail"
                           and (self.vres[c.id]["rung_reached"] >= 1 or (self.vres[c.id].get("feedback") or {}).get("rung") in (0, 1))
                           and not any(p.parent_ids and c.id in p.parent_ids for p in self.cands)],
                          key=lambda c: -self.vres[c.id]["rung_reached"])
            revise_queue = [(c, self.vres[c.id]["feedback"]) for c in near]
        for rnd in range(self.completed_rounds + 1, self.rounds + 1):
            # ---- ideation: many short sketches from independent contexts, then a blind clustering
            if self.replan and rnd > 1 and self.tree is not None:
                self.replan_tree(rnd)
            already = {s.get("round") for s in self.sketches} if self.resume else set()
            if rnd in already and self.resume:
                self.decisions.append({"round": rnd, "step": "resume", "skipped": "ideation (sketches on disk)"})
                if self.tree is None:
                    self.plan_tree(rnd)
            else:
                self._live(f"round {rnd}: ideating", "every part of the problem tree, inward and outward, 5-8 sketches per context")
                self.ideate_round(rnd, seeds)
            self._stage(rnd, "ideated")
            self._live(f"round {rnd}: clustering ideas", f"{len(self.sketches)} sketches so far")
            self.cluster_sketches(rnd)
            self.round_now = rnd
            k_impl = self.k_impl if rnd == 1 else max(2, self.k_impl // 3)
            k_aff = budget_mod.affordable_slots(self.spent, self.B, k_impl)
            if k_aff < k_impl:
                self.decisions.append({"round": rnd, "step": "budget", "slots_cut": [k_impl, k_aff], "spent": self.spent})
                k_impl = k_aff
            done = {c["cluster_id"] for c in self.clusters if any(m in self.implemented for m in c["members"])
                    or self._skipped(c.get("node")) or c.get("name") in self.exclude_clusters}
            by_node: dict[str, list[dict]] = {}
            for c in self.clusters:
                by_node.setdefault(c.get("node", "root"), []).append(c)
            self._discovery(rnd)
            chosen = self._select_with_lanes(by_node, k_impl, done)
            write_json(self.run_dir / "idea_clusters.json", {"round": rnd, "clusters": self.clusters,
                                                             "n_sketches": len(self.sketches)})
            self._write_tree()
            self._stage(rnd, "clustered")                 # after the scores, so a test stop shows the ranking
            if self.do_deepen and chosen:
                # ---- interrogate many top ideas, generation by generation: offshoots of one generation are
                # the candidates of the next; every generation re-clusters and re-selects the build slots
                interrogated = self.interrogated         # never question the same idea twice, in any round
                top = self.deepen_top if rnd == 1 else max(4, self.deepen_top // 2)
                for gen in range(self.deepen_generations + 1):
                    skip = done | {c["cluster_id"] for c in self.clusters if interrogated & set(c["members"])}
                    if gen > 0:                         # later generations: only ideas born in the interrogation
                        skip |= {c["cluster_id"] for c in self.clusters if "deepen" not in c["cards"]}
                    asked = Counter(n.get("node") for n in self.deepen_nodes if n.get("parent") is None)
                    targets = tree.split_select(by_node, top, self.inward_share, skip, self.sketches,
                                                self._select, self.new_share, counts=dict(asked),
                                                order_seed=f"{self.run_id}:deepen:{rnd}:{gen}")
                    chosen_ids = {c["cluster_id"] for c in chosen}
                    for c in self.clusters:             # the wide pick is not the build selection
                        c["selected"] = c["cluster_id"] in chosen_ids
                    if not targets:
                        break
                    self._live(f"round {rnd}: interrogating ideas (generation {gen})",
                               f"{len(targets)} ideas, {self.deepen_depth + 1} levels each")
                    n_off = self.deepen_round(rnd, targets, gen)
                    for c in targets:
                        if c["cluster_id"] not in self._deepen_skipped:
                            interrogated.update(c["members"])
                    if not n_off:
                        break
                    self._live(f"round {rnd}: re-clustering", f"{n_off} new ideas from generation {gen}")
                    self.cluster_sketches(rnd)
                    done = {c["cluster_id"] for c in self.clusters if any(m in self.implemented for m in c["members"])
                            or self._skipped(c.get("node")) or c.get("name") in self.exclude_clusters}
                    by_node = {}
                    for c in self.clusters:
                        by_node.setdefault(c.get("node", "root"), []).append(c)
                    chosen = self._select_with_lanes(by_node, k_impl, done)
                    write_json(self.run_dir / "idea_clusters.json", {"round": rnd, "clusters": self.clusters,
                                                                     "n_sketches": len(self.sketches)})
                    self._write_tree()
            ranked_pool = sorted([c for c in self.clusters if c["cluster_id"] not in done], key=lambda c: -(c.get("score") or 0.0))
            chosen = self._novelty_filter(chosen, ranked_pool)
            for c in self.clusters:
                c["selected"] = any(c["cluster_id"] == k["cluster_id"] for k in chosen)
            write_json(self.run_dir / "idea_clusters.json", {"round": rnd, "clusters": self.clusters,
                                                             "n_sketches": len(self.sketches)})
            self._stage(rnd, "deepened")
            # ---- implementation specs: one file per selected cluster, plus revisions of near misses
            specs: list = []
            for parent, fb in revise_queue[:2]:
                # the move follows the failure: build and boundary failures get fixed, resource failures get
                # narrowed to a smaller part, a learning failure gets fixed
                rung = (fb or {}).get("rung", 1)
                specs.append(("revise", "specialize" if rung == 2 else "fix", "", parent, fb))
            revise_queue = revise_queue[2:]
            for parent, fb, op in self.family_queue[: self.family_variants]:    # variants of near misses from the lane
                specs.append(("revise", op, "", parent, fb))
            self.family_queue = self.family_queue[self.family_variants:]
            for c in chosen:
                specs.append(("implement", c["cluster_id"], "", None, None))
            if self.program_search:
                for i in range(self.program_k):
                    specs.append(("program", self.program_search, str(i), None, None))
            self._live(f"round {rnd}: implementing", f"{len(chosen)} ideas from {len(self.clusters)} clusters, {len(specs) - len(chosen)} revisions/programs")

            def _one(spec):
                card, op, seed = spec[0], spec[1], spec[2]
                parent, fb = (spec[3], spec[4]) if len(spec) > 3 else (None, None)
                rt = "revise" if card == "revise" else ("first" if rnd == 1 else "post_reset")
                return self.run_card(card, rnd, op, seed, parent, fb, rt)
            with ThreadPoolExecutor(max_workers=min(6, max(1, len(specs)))) as ex:   # fresh contexts in parallel
                results = list(ex.map(_one, specs)) if specs else []
            new: list[Candidate] = [c for c in results if c]
            for c in chosen:
                self.implemented.update(c["members"])
            kept = self.dedup(new, rnd)
            self._stage(rnd, "built")
            if rnd == 1 and self.controls and self.mode == "baseline":   # controls and tuning edit a baseline
                self.run_controls(rnd)
            if rnd == 1 and self.tune and self.mode == "baseline":
                self.run_tuning(rnd)
            self._live(f"round {rnd}: verifying", f"{len(new)} candidates, {len(kept)} unique")
            self.cands.extend(kept)
            checked, failed = [], []
            for c in kept:                                  # free verification: every candidate, serial (one GPU)
                rec = self.verify(c, rnd)
                self._resolve_objections(c, rec)
                (checked if rec["status"] == "checked" else failed).append(c)
                print(f"[nano] r{rnd} {c.card:9s} {c.id} -> {rec['status']} rung {rec['rung_reached']} "
                      f"| {c.extra.get('change','')[:70]}", flush=True)
                if rec["status"] != "checked":
                    for child, crec in self._immediate_fix(c, rnd):
                        (checked if crec["status"] == "checked" else failed).append(child)
            for comp, crec in self.compose_round(rnd):
                (checked if crec["status"] == "checked" else failed).append(comp)
            self._spawn_fail_questions(rnd, failed)            # every verify record of this round is final here
            self._hedge(failed, rnd)
            self._queue_families(checked)
            children = {}
            for c in self.cands:
                for pid in c.parent_ids:
                    children[pid] = children.get(pid, 0) + 1
            lineage_ok = {c.lineage_id for c in self.cands if self.vres.get(c.id, {}).get("status") == "checked"}
            near = sorted([c for c in failed if self.vres[c.id]["rung_reached"] >= 1 or
                           (self.vres[c.id].get("feedback") or {}).get("rung") in (0, 1)],
                          key=lambda c: (-(1 if c.lineage_id in lineage_ok else 0), -self.vres[c.id]["rung_reached"],
                                         children.get(c.id, 0)))   # productive lineages, closest misses, few children first
            revise_queue = [(c, self.vres[c.id]["feedback"]) for c in near] + revise_queue
            self._write_tree()
            self._curate_memory(rnd)                         # per-part memory: propose, check against artefacts, append
            self.decisions.append({"round": rnd, "step": "cycle", "spawned": [s[0] for s in specs],
                                   "n_raw": len(new), "n_kept": len(kept), "checked": [c.id for c in checked],
                                   "failed": [c.id for c in failed], "spent": self.spent, "ts": now_ts()})
            self._write_state()
            try:
                from harness import graph
                graph.write(self.run_dir)
            except Exception as e:  # noqa: BLE001
                self.decisions.append({"round": rnd, "step": "graph", "error": str(e)[:200]})
            self._stage(rnd, "verified")
            if self.spent >= self.B:
                break
        return self._finish(t0)

    def run_tuning(self, round_no: int) -> None:
        """Single-knob moves of the recipe's constants, by script, up the same ladder; the best few (better
        than the original at the learning check) stay in the pool for the long run and the night, the rest
        are pruned so the card is not spent on them. Tuning and invention both, every run."""
        from nano import tune as TN
        built = TN.build(self.baseline_src, self.tune_knobs or None)
        rows = []
        for name, spec in built.items():
            cid = f"tune_{name}".replace(".", "_")
            key = hashlib.sha1(_norm_source(spec["source"]).encode()).hexdigest()[:12]
            cand = Candidate(id=cid, text=spec["hypothesis"], card="tune", operator=name, seed="", perm=0,
                             round=round_no, call_id="", parent_ids=[], lineage_id=cid, program=spec["source"],
                             extra={"hypothesis": spec["hypothesis"], "change": spec["field"], "src_hash": key, "node": "tune",
                                    "direction": "tune", "lane": "tune", "kind": "tune", "knob": name,
                                    "prediction": f"{spec['field']} {spec['old']:g} -> {spec['new']:g}"})
            (self.run_dir / "cands" / "src" / f"{cid}.py").write_text(spec["source"], encoding="utf-8")
            row = cand.to_dict()
            row["program"] = f"cands/src/{cid}.py"
            append_jsonl(self.run_dir / "cands" / f"tune_{cid}.jsonl", row)
            self.cands.append(cand)
            self._live(f"round {round_no}: tuning", f"{name}: {spec['field']} {spec['old']:g} -> {spec['new']:g}, through the ladder")
            rec = self.verify(cand, round_no)
            rows.append({"id": cid, "knob": name, "field": spec["field"], "old": spec["old"], "new": spec["new"],
                         "status": rec["status"], "rung": rec["rung_reached"], "learn_z": rec["metrics"].get("learn_z"), "kept": False})
            print(f"[nano] tune {name:14s} -> {rec['status']} rung {rec['rung_reached']} | learn z {rec['metrics'].get('learn_z')}", flush=True)
        passed = sorted([r for r in rows if r["status"] == "checked" and r["learn_z"] is not None], key=lambda r: r["learn_z"])
        keep = {r["id"] for r in passed[: self.tune_top] if r["learn_z"] < 0}   # better than the original at 45 steps, best first
        for r in rows:
            r["kept"] = r["id"] in keep
            if r["status"] == "checked" and not r["kept"]:
                self.vres[r["id"]]["status"] = "tune_pruned"       # passed, but not among the best: no long run, no night
                for ext in ("py", "json"):
                    try:
                        (self.run_dir / "pool" / f"{r['id']}.{ext}").unlink()
                    except FileNotFoundError:
                        pass
        write_json(self.run_dir / "tuning.json", {"round": round_no, "knobs": rows, "kept": sorted(keep)})
        self.decisions.append({"round": round_no, "step": "tuning", "swept": len(rows), "kept": sorted(keep), "ts": now_ts()})

    def run_controls(self, round_no: int) -> None:
        """Placebos, known winners and a known loser through the exact ladder: the run's own false-positive
        rate and power. Controls never enter the pool or the selection."""
        built = CT.build(self.baseline_src, self.controls if self.controls != ["all"] else None)
        report = {}
        for name, spec in built.items():
            if not spec.get("source"):
                report[name] = {"ok": None, "note": spec.get("unavailable")}
                continue
            cid = f"ctl_{name}"
            key = hashlib.sha1(_norm_source(spec["source"]).encode()).hexdigest()[:12]
            cand = Candidate(id=cid, text=spec["hypothesis"], card=f"control:{name}", operator="control", seed="", perm=0,
                             round=round_no, call_id="", parent_ids=[], lineage_id=cid, program=spec["source"],
                             extra={"hypothesis": spec["hypothesis"], "change": name, "src_hash": key, "node": "control",
                                    "direction": "control", "control": name})
            (self.run_dir / "cands" / "src" / f"{cid}.py").write_text(spec["source"], encoding="utf-8")
            row = cand.to_dict()
            row["program"] = f"cands/src/{cid}.py"
            append_jsonl(self.run_dir / "cands" / f"control_{cid}.jsonl", row)
            self.cands.append(cand)
            self._live(f"round {round_no}: control", f"{name} ({spec['kind']}) through the ladder")
            rec = self.verify(cand, round_no)
            report[name] = {**CT.judge(name, rec["status"], rung=rec.get("rung_reached")), "kind": spec["kind"], "status": rec["status"],
                            "rung": rec["rung_reached"], "learn_z": rec["metrics"].get("learn_z")}
            print(f"[nano] control {name:14s} -> {rec['status']} rung {rec['rung_reached']} | {report[name]['note']}", flush=True)
        write_json(self.run_dir / "controls.json", report)
        self.decisions.append({"round": round_no, "step": "controls", "report": {k: v.get("ok") for k, v in report.items()}, "ts": now_ts()})

    def _hedge(self, failed: list[Candidate], round_no: int) -> None:
        """Hedge lane: a random share of candidates that failed rung 3 only by the gap tolerance still get the
        long run and the overnight exam, so the ladder's false-reject rate is measured (lane 'hedge')."""
        if self.hedge_share <= 0:
            return
        rng = random.Random(f"hedge:{self.rep}:{round_no}")
        for c in failed:
            fb = self.vres[c.id].get("feedback") or {}
            if fb.get("rung") == 3 and str(fb.get("reason", "")).startswith("at step") and rng.random() < self.hedge_share:
                self.hedged.add(c.id)
                rec = self.vres[c.id]
                (self.run_dir / "pool" / f"{c.id}.py").write_text(c.program or "", encoding="utf-8")
                write_json(self.run_dir / "pool" / f"{c.id}.json",
                           {"id": c.id, "card": c.card, "operator": c.operator, "seed": c.seed, "lineage_id": c.lineage_id,
                            "parent_ids": c.parent_ids, "hypothesis": c.extra.get("hypothesis"), "change": c.extra.get("change"),
                            "node": c.extra.get("node"), "direction": c.extra.get("direction"), "src_hash": c.extra.get("src_hash"),
                            "arm": self.arm, "baseline_version": self.baseline_version, "lane": "hedge", "metrics": rec["metrics"]})
                self.decisions.append({"round": round_no, "step": "hedge", "cand": c.id, "ts": now_ts()})

    def _resolve_objections(self, cand: Candidate, rec: dict) -> None:
        """The pre-mortem's objections against this idea, judged by what the ladder measured on this build."""
        members = set(cand.extra.get("members") or [])
        if not members:
            return
        objs = []
        for n in self.deepen_nodes:
            if not n.get("parent") and members & set(n.get("members", [])):
                objs += n.get("objections") or []
        if not objs:
            return
        resolved = deepen.resolve_objections(objs, rec.get("metrics") or {})
        rec.setdefault("metrics", {})["objections"] = [{k: o.get(k) for k in ("text", "severity", "cls", "link", "if_true", "status", "measured")} for o in resolved]

    def _queue_families(self, checked: list) -> None:
        """A candidate from the ambitious lane that passed the ladder is a near miss or better: queue two
        variants of it (narrower, relaxed) for the next round, outside the quota. Best matched-step gap first."""
        if self.family_variants <= 0:
            return
        queued = {c.id for c, _, _ in self.family_queue}
        parents = [c for c in checked if (c.extra.get("lane") == "longshot" or c.extra.get("kind") == "leap")
                   and not c.card.startswith("control") and not str(c.operator).startswith("variant:") and c.id not in queued]
        parents.sort(key=lambda c: (self.vres.get(c.id, {}).get("metrics") or {}).get("learn_z") or 0.0)
        for c in parents[:2]:
            m = self.vres.get(c.id, {}).get("metrics") or {}
            fb = {"near_miss": True, "status": "checked", "learn_z": m.get("learn_z"), "learn_gap": m.get("learn_gap"),
                  "note": "passed the first checks; a near miss or better from the ambitious lane"}
            for op in ("variant:narrow", "variant:relax"):
                self.family_queue.append((c, fb, op))
        if parents:
            self.decisions.append({"step": "families", "parents": [c.id for c in parents[:2]], "ts": now_ts()})

    def _node_by_name(self, text: str) -> str | None:
        """The map part a free-text name refers to (id or name, case-insensitive), or None."""
        t = " ".join(str(text or "").lower().split())
        if not t:
            return None
        for n in self.tree or []:
            if n["id"] == "root":
                continue
            name = str(n.get("name", "")).lower()
            if t == n["id"] or t == name or (len(t) >= 4 and (t in name or name in t)):
                return n["id"]
        return None

    def replan_tree(self, round_no: int) -> None:
        """Arm: redraw the map from what the run learned (outcomes, objections, discovered assumptions).

        Carry-over rule (docs/TEAM_OF_RESEARCHERS.md, "a map, not a fence", rule 4): a re-plan redraws the map
        but never deletes what the run or people put on it. After the planner's list is parsed, every old node
        that must survive is carried over: promoted off-map wins (origin "offtree"), branches people added
        (origin "human", control.json add_nodes) and any part with implemented candidates (the "implemented"
        count of _write_tree). A carried node the new list matches (same id; the new node `refines` it, or both
        refine the same id; same name; or a name head only that carried node has) is merged: it keeps its id,
        origin and other fields (assumptions_added, idea_assumptions, priority, ...) and takes the planner's
        newer frame text. An unmatched carried node is appended unchanged. A re-plan may lower a carried node's
        priority once a priority mechanism exists (none does yet), never drop it. Other old nodes may be
        dropped. The off-map pseudo-node is re-added by _ensure_off_node. Logged as step "replan_carry"."""
        goal = (self.run_dir / "problem.md").read_text(encoding="utf-8")
        extra = self.history_text()
        objections = [o["text"] for n in self.deepen_nodes for o in (n.get("objections") or [])][:20]
        if objections:
            extra += "\n\nOBJECTIONS RAISED AGAINST IDEAS SO FAR:\n" + "\n".join(f"- {o}" for o in objections)
        r = self._call(tree.planner_prompt(goal + "\n\n" + extra, self.baseline_src, self.lens, self.diagnostics_text), "encode", 2500,
                       {"card": "replan", "note": f"re-planning the map for round {round_no}"})
        self._ledger("replan", "none", "", r.call_id, r.usage, round_no, "encode")
        nodes = tree.parse_planner(r.text or "")
        if not nodes:
            self.decisions.append({"round": round_no, "step": "replan", "result": "planner output unusable; map kept", "ts": now_ts()})
            return
        old_by_name = {n["name"].lower(): n for n in (self.tree or [])}
        old_by_id = {n["id"]: n for n in (self.tree or [])}
        for n in nodes:
            prev = old_by_id.get(n["id"]) or old_by_name.get(n["name"].lower())
            if prev:
                n["id"] = prev["id"]
                # what tested ideas assumed travels with the part by id; the new design assumptions stay as planned
                n["idea_assumptions"] = list(tree.idea_assumptions(prev))
        nodes = self._replan_carry(self.tree or [], nodes, round_no)
        self.tree = nodes
        self._ensure_off_node()
        self.decisions.append({"round": round_no, "step": "replan", "parts": [n["id"] for n in nodes], "ts": now_ts()})
        self._write_tree()

    def _replan_carry(self, old: list[dict], new: list[dict], round_no: int) -> list[dict]:
        """The carry-over rule of replan_tree: `new` with every node that must survive merged in or appended."""
        import copy

        def implemented(n) -> int:                       # the "implemented" count _write_tree writes for this node
            dirs = n.get("directions") or []
            return sum(1 for c in self.cands if (c.extra or {}).get("node") == n["id"] and (c.extra or {}).get("direction") in dirs)

        def head(n) -> str:
            return tree._plain(n.get("name", "")).split(":")[0].strip()

        must = [n for n in old if n["id"] not in ("root", tree.OFF_TREE_ID)
                and (n.get("origin") in (tree.OFF_TREE_ID, "human") or implemented(n) > 0)]
        heads = Counter(head(n) for n in must)
        kept, merged, claimed = [], [], set()
        for o in must:
            def same(n, o=o) -> bool:
                if n["id"] == o["id"] or (n.get("refines") and n["refines"] in (o["id"], o.get("refines"))):
                    return True
                if tree._plain(n.get("name", "")) == tree._plain(o.get("name", "")):
                    return True
                return bool(head(o)) and heads[head(o)] == 1 and head(n) == head(o)
            hit = next((n for n in new if id(n) not in claimed and n["id"] not in ("root", tree.OFF_TREE_ID) and same(n)), None)
            if hit is None:
                new.append(copy.deepcopy(o))
                kept.append(o["id"])
                continue
            claimed.add(id(hit))
            planner_id, frame = hit["id"], hit.get("frame", o.get("frame", ""))
            for k, v in o.items():                       # the carried node's fields win, except the newer frame text
                if k not in hit or k in ("id", "origin", "parent"):
                    hit[k] = copy.deepcopy(v)
            hit["frame"] = frame
            merged.append({"id": o["id"], "planner_id": planner_id, "origin": o.get("origin", "tree")})
        new_ids = {n["id"] for n in new}
        dropped = [n["id"] for n in old if n["id"] not in new_ids and n["id"] != tree.OFF_TREE_ID]
        self.decisions.append({"round": round_no, "step": "replan_carry", "kept": kept, "merged": merged,
                               "dropped": dropped, "ts": now_ts()})
        return new

    def _immediate_fix(self, cand: Candidate, round_no: int) -> list[tuple[Candidate, dict]]:
        """A rung 0 or rung 1 failure is a one-call fix: do it now, in this round, once."""
        fb = self.vres[cand.id].get("feedback") or {}
        if not self.immediate_fix or fb.get("rung") not in (0, 1) or cand.extra.get("fixed"):
            return []
        cand.extra["fixed"] = True
        child = self.run_card("revise", round_no, "fix", "", cand, fb, "fix")
        if not child:
            return []
        kept = self.dedup([child], round_no)
        if not kept:
            return []
        self.cands.extend(kept)
        rec = self.verify(child, round_no)
        print(f"[nano] r{round_no} fix       {child.id} -> {rec['status']} rung {rec['rung_reached']} "
              f"| fixes {cand.id}", flush=True)
        return [(child, rec)]

    def compose_round(self, round_no: int) -> list[tuple[Candidate, dict]]:
        """Pairs of checked candidates with disjoint changed symbols are spliced together by script and sent
        up the ladder as composites (card 'compose', two parents). Zero model cost."""
        from nano import compose as CP
        if self.max_compose <= 0 or self.mode != "baseline":   # splicing needs a common baseline
            return []
        checked = [c for c in self.cands if self.vres.get(c.id, {}).get("status") == "checked" and c.card != "compose"
                   and not c.card.startswith("control")]          # controls never enter the pool, nor a composite
        done_pairs = {tuple(sorted(c.parent_ids)) for c in self.cands if c.card == "compose"}

        def syms(c):
            return set(self.vres[c.id]["metrics"].get("changed_symbols") or [])

        def score(c):
            m = self.vres[c.id]["metrics"]
            return m.get("learn_z") if m.get("learn_z") is not None else (m.get("learn_gap") or 0.0)
        pairs = []
        for i, a in enumerate(checked):
            for b in checked[i + 1:]:
                if tuple(sorted([a.id, b.id])) in done_pairs or a.lineage_id == b.lineage_id:
                    continue
                if syms(a) & syms(b) - {"<module>", "Config"}:
                    continue
                pairs.append((score(a) + score(b), a, b))
        pairs.sort(key=lambda t: t[0])
        out = []
        for _, a, b in pairs[: self.max_compose]:
            r = CP.compose(self.baseline_src, a.program or "", b.program or "")
            if not r:
                continue
            cid = new_id("n")
            key = hashlib.sha1(_norm_source(r["source"]).encode()).hexdigest()[:12]
            cand = Candidate(id=cid, text=f"composite of {a.id} and {b.id}", card="compose", operator=f"{a.id}+{b.id}",
                             seed="", perm=0, round=round_no, call_id="", parent_ids=[a.id, b.id], lineage_id=cid,
                             program=r["source"], extra={"hypothesis": f"{a.extra.get('hypothesis', '')} AND {b.extra.get('hypothesis', '')}"[:300],
                                                         "change": f"from {a.id}: {', '.join(r['from_a'][:6])}; from {b.id}: {', '.join(r['from_b'][:6])}"[:300],
                                                         "src_hash": key, "node": "recipe", "direction": "inward", "cluster": "composite"})
            (self.run_dir / "cands" / "src" / f"{cid}.py").write_text(r["source"], encoding="utf-8")
            row = cand.to_dict()
            row["program"] = f"cands/src/{cid}.py"
            append_jsonl(self.run_dir / "cands" / f"compose_{cid}.jsonl", row)
            kept = self.dedup([cand], round_no)
            if not kept:
                continue
            self.cands.extend(kept)
            self._live(f"round {round_no}: composite", f"{a.id} + {b.id} spliced by script, verifying")
            rec = self.verify(cand, round_no)
            print(f"[nano] r{round_no} compose   {cid} -> {rec['status']} rung {rec['rung_reached']} | {a.id}+{b.id}", flush=True)
            out.append((cand, rec))
        return out

    def run_control(self, t0: float) -> dict:
        """The control arms, same ladder and budget: `plain` = N independent direct builds (best-of-N);
        `climb` = the autoresearch loop, each build from the current best checked script, keep or discard."""
        seeds = _seeds()
        cards = ["seeded", "formal", "docs", "low_prior"]
        best_key = None
        specs = []
        for i in range(self.n_builds):
            seed = self.rng.choice([w for w in seeds if w not in self.used_seeds] or seeds)
            self.used_seeds.add(seed)
            specs.append((cards[i % len(cards)], seed))
        if self.arm == "plain":
            self._live("control arm: plain", f"{len(specs)} independent builds, best-of-N")
            with ThreadPoolExecutor(max_workers=6) as ex:
                results = list(ex.map(lambda s: self.run_card(s[0], 1, "none", s[1], None, None, "first"), specs))
            kept = self.dedup([c for c in results if c], 1)
            self.cands.extend(kept)
            for c in kept:
                rec = self.verify(c, 1)
                print(f"[nano] plain {c.card:9s} {c.id} -> {rec['status']} rung {rec['rung_reached']} | {c.extra.get('change','')[:70]}", flush=True)
                if rec["status"] != "checked":
                    self._immediate_fix(c, 1)
        else:
            self._live("control arm: climb", f"{len(specs)} sequential builds, keep or discard")
            for i, (card, seed) in enumerate(specs, 1):
                if self.spent >= self.B:
                    break
                c = self.run_card(card, i, "none", seed, None, None, "first")
                if not c:
                    continue
                kept = self.dedup([c], i)
                if not kept:
                    continue
                self.cands.extend(kept)
                rec = self.verify(c, i)
                if rec["status"] != "checked":
                    extra = self._immediate_fix(c, i)
                    if extra and extra[0][1]["status"] == "checked":
                        c, rec = extra[0]
                key = rec["metrics"].get("learn_z") if rec["metrics"].get("learn_z") is not None else rec["metrics"].get("learn_gap")
                keep = rec["status"] == "checked" and key is not None and (best_key is None or key < best_key - 0.5)
                print(f"[nano] climb {i:2d} {c.card:9s} {c.id} -> {rec['status']} learn z {key} {'KEEP' if keep else 'discard'}", flush=True)
                if keep:
                    best_key = key
                    self.working_src = c.program or self.working_src
                    self.history[-1]["kept"] = True
                self.decisions.append({"round": i, "step": "climb", "cand": c.id, "keep": keep, "key": key, "spent": self.spent})
                self._write_state()
        self.decisions.append({"round": 0, "step": "control", "arm": self.arm, "n_builds": len(specs), "spent": self.spent, "ts": now_ts()})
        self._write_state()
        return self._finish(t0)

    def _finish(self, t0: float) -> dict:
        if self.long_steps > 0:
            self.long_runs()
        if self.backend != "mock":                   # sourced facts from the interrogation enter the shared brief cache
            cache = config.MEMORY_DIR / "research"
            for node_id in {n.get("node") for n in self.deepen_nodes}:
                facts = [k for n in self.deepen_nodes if n.get("node") == node_id for k in n.get("known", [])]
                research.merge_facts(cache, node_id, facts)

        def rank_key(c):
            m = self.vres[c.id]["metrics"]
            g = m.get("extrap_z")
            if g is None:
                g = m.get("long_z") if m.get("long_z") is not None else (m.get("learn_z") if m.get("learn_z") is not None else m.get("learn_gap"))
            return (g is None, g if g is not None else 0.0)
        pool = sorted([c for c in self.cands if (self.vres.get(c.id, {}).get("status") == "checked" or c.id in self.hedged)
                       and not c.card.startswith("control")], key=rank_key)
        gens = {}
        for n in self.deepen_nodes:
            g = gens.setdefault(n.get("gen", 0), {"calls": 0, "offshoots": 0, "facts": 0, "unsourced_dropped": 0})
            g["calls"] += 1; g["offshoots"] += len(n.get("offshoots", [])); g["facts"] += len(n.get("known", []))
            g["unsourced_dropped"] += n.get("dropped_unsourced", 0)
        controls_report = json.loads((self.run_dir / "controls.json").read_text(encoding="utf-8")) if (self.run_dir / "controls.json").exists() else {}
        answer = {"status": "pool", "arm": self.arm, "baseline_version": self.baseline_version,
                  "lens": self.lens, "lens_design": self.lens_design,
                  "n_candidates": len([c for c in self.cands if not c.card.startswith("control")]), "n_checked": len(pool),
                  "controls": controls_report, "discovery": self.discovery, "retired_cards": sorted(self.retired_cards),
                  "lanes": {lane: {"built": sum(1 for c in self.cands if c.extra.get("lane", "main") == lane and not c.card.startswith("control")),
                                   "checked": sum(1 for c in pool if c.extra.get("lane", "main") == lane)}
                            for lane in sorted({c.extra.get("lane", "main") for c in self.cands})},
                  "origins": self._origin_stats(), "off_tree_share": self.off_tree_share, "source_yield": self.source_yield,
                  "promoted_branches": [n["id"] for n in (self.tree or []) if n.get("origin") == "offtree"],
                  "ranked": [{"id": c.id, "card": c.card, "operator": c.operator, "node": c.extra.get("node"),
                              "hypothesis": c.extra.get("hypothesis"), "change": c.extra.get("change"),
                              "long_gap": self.vres[c.id]["metrics"].get("long_gap"), "long_z": self.vres[c.id]["metrics"].get("long_z"),
                              "extrap_z": self.vres[c.id]["metrics"].get("extrap_z"), "trend": self.vres[c.id]["metrics"].get("trend"),
                              "learn_gap": self.vres[c.id]["metrics"].get("learn_gap"), "learn_z": self.vres[c.id]["metrics"].get("learn_z"),
                              "smoke_drop": self.vres[c.id]["metrics"].get("smoke_drop"),
                              "step_s": self.vres[c.id]["metrics"].get("step_s")} for c in pool],
                  "generations": gens, "n_sketches": len(self.sketches),
                  "obvious_clusters": sum(1 for c in self.clusters if c.get("obvious")),
                  "upward_proposals": [{k: u.get(k, "") for k in ("id", "proposal", "reframing", "new_measure", "why", "cost", "round")}
                                       for u in self.upward if u.get("proposal")][:20],
                  "spent_tokens": self.spent, "budget": self.B, "spent_aux_tokens": self.spent_aux, "aux_budget": self.aux_budget,
                  "wall_s": round(time.time() - t0),
                  "next": "python -m nano.batch_verify --run <this folder>: staged seeds against the pooled baseline"}
        if self.mode != "baseline":
            answer.update({"mode": self.mode, "reference": self.reference, "reference_changes": self.reference_log})
            answer["next"] = ("read the ranked proposals in REPORT.md; add opinions to control.json and run again"
                              if self.mode == "no_check" else
                              "the reference is the best checked candidate; run the full test on it against the next best")
        if self.mode == "no_check":
            answer["status"] = "proposals"
            answer["proposals"] = self._ranked_proposals()
        write_json(self.run_dir / "answer.json", answer)
        self._write_state()
        try:
            from nano import report
            report.write(self.run_dir)
            if self.mode != "baseline":
                self._report_modes(answer)
            self._report_memory()
            try:
                from nano import lessons as LS
                if self.backend != "mock":                       # mock runs teach nothing
                    LS.update_from_run(self.run_dir, config.MEMORY_DIR / "lessons.jsonl", self.baseline_version)
            except Exception as e:  # noqa: BLE001
                print(f"[nano] lessons not updated: {e}", flush=True)
        except Exception as e:  # noqa: BLE001
            self.decisions.append({"step": "report", "error": str(e)[:200]})
            self._write_state()
        self._live("done", f"{len(pool)} checked candidates in pool/")
        return answer

    def _ranked_proposals(self) -> list[dict]:
        """Mode 3: the checked proposals ranked by panel score, with their justification, weak points, proposed
        test and the panel's notes."""
        from nano.checks.panel import sections
        rows = []
        for c in self.cands:
            r = self.vres.get(c.id) or {}
            if r.get("status") != "checked" or c.card.startswith("control"):
                continue
            m = r.get("metrics") or {}
            sec = sections(c.program or "")
            rows.append({"id": c.id, "node": c.extra.get("node"), "cluster": c.extra.get("cluster"),
                         "claim": sec.get("CLAIM", ""), "from_facts": sec.get("FROM THE FACTS TO THE IDEA", ""),
                         "to_result": sec.get("FROM THE IDEA TO THE RESULT", ""), "weak_points": sec.get("WEAK POINTS", ""),
                         "proposed_test": sec.get("PROPOSED TEST", ""), "panel_score": m.get("panel_score"),
                         "panel_sd": m.get("panel_sd"), "judge_scores": m.get("judge_scores"), "criteria": m.get("criteria"),
                         "people_score": m.get("people_score"), "people_n": m.get("people_n", 0),
                         "panel_notes": m.get("panel_notes") or [], "facts_named": m.get("facts_named") or [],
                         "learn_gap": m.get("learn_gap"), "learn_z": m.get("learn_z"),
                         "reference": bool(self.reference and self.reference.get("cand_id") == c.id),
                         "file": f"pool/{c.id}.md"})
        rows.sort(key=lambda d: (-(d["panel_score"] or 0.0), d["panel_sd"] if d["panel_sd"] is not None else 9.0, d["id"]))
        for i, d in enumerate(rows, 1):
            d["rank"] = i
        return rows

    def _report_modes(self, answer: dict) -> None:
        """Mode 2 and 3: the reference and its history in report.json and REPORT.md; in Mode 3 the ranked proposals
        lead the report, since the run's output is a ranked list, not a verified artifact."""
        rj = self.run_dir / "report.json"
        try:
            d = json.loads(rj.read_text(encoding="utf-8"))
        except Exception:  # noqa: BLE001
            d = {}
        d.update({"mode": self.mode, "reference": self.reference, "reference_changes": self.reference_log})
        lines = []
        if self.mode == "no_check":
            props = answer.get("proposals") or []
            d["proposals"] = props
            failed = [(c.id, (self.vres.get(c.id) or {}).get("feedback", {})) for c in self.cands
                      if (self.vres.get(c.id) or {}).get("status") not in (None, "checked") and not c.card.startswith("control")]
            d["proposals_not_ranked"] = [{"id": i, "rung": fb.get("rung"), "reason": fb.get("reason", "")} for i, fb in failed]
            lines += [f"# Ranked proposals: {self.pf.get('title') or self.pf.name}", "",
                      "There is no objective check. Each proposal was read blind by a panel of judges; people's opinions "
                      "count at a bounded weight. Higher panel score is better.", ""]
            for p in props:
                crit = ", ".join(f"{k} {v}" for k, v in (p.get("criteria") or {}).items())
                lines += [f"## {p['rank']}. {p['id']}: panel score {p['panel_score']} (sd {p['panel_sd']})"
                          + (" [reference]" if p.get("reference") else ""), "",
                          f"Judges: {p.get('judge_scores')}; by criterion: {crit}."
                          + (f" People: {p['people_score']} from {p['people_n']}." if p.get("people_n") else ""), "",
                          f"**Claim.** {p['claim']}", "", f"**From the facts to the idea.** {p['from_facts']}", "",
                          f"**From the idea to the result.** {p['to_result']}", "", f"**Weak points.** {p['weak_points']}", "",
                          f"**Proposed test.** {p['proposed_test']}", ""]
                if p.get("panel_notes"):
                    lines += ["**Panel notes.**"] + [f"- {n}" for n in p["panel_notes"]] + [""]
            if d["proposals_not_ranked"]:
                lines += ["## Not ranked", ""] + [f"- {r['id']}: rung {r['rung']}: {r['reason'][:200]}" for r in d["proposals_not_ranked"]] + [""]
        else:
            ref = self.reference or {}
            lines += [f"# Reference (no baseline): {ref.get('cand_id', 'none chosen')}", "",
                      f"{ref.get('hypothesis', '')}", ""]
            for e in self.reference_log:
                lines.append(f"- round {e['round']}: {e['action']} {e['from'] or '-'} -> {e['to']}: {e['reason']}")
            lines.append("")
        rj.write_text(json.dumps(d, indent=1), encoding="utf-8")
        md = self.run_dir / "REPORT.md"
        old = md.read_text(encoding="utf-8") if md.exists() else ""
        md.write_text("\n".join(lines) + "\n\n" + old, encoding="utf-8")

    def _select(self, clusters, k, exclude=None, sketches=None):
        return ideate.select_clusters(clusters, k, exclude=exclude, sketches=sketches, weights=self.select_weights)

    def _write_state(self) -> None:
        st = json.loads((self.run_dir / "state.json").read_text(encoding="utf-8"))
        st["decisions"] = self.decisions
        st["spent"] = self.spent
        st["spent_aux"] = self.spent_aux
        st["completed_rounds"] = max(int(st.get("completed_rounds", 0)), self.completed_rounds)
        write_json(self.run_dir / "state.json", st)


DEFAULT_LENS = "parts"


def choose_lens(lens_arg: str | None, replicate: int, by_replicate: bool, lenses) -> tuple[str, str, str]:
    """The map lens and the design it belongs to. The lens is a factor apart from the replicate: by default every
    replicate uses DEFAULT_LENS (or --lens), so replicates differ only in seed. --lens-by-replicate opts into the
    old pairing (lens = LENSES[replicate % n]) for deliberate lens experiments; analysis then groups by lens.
    Returns (lens, lens_design, note); note is non-empty when the asked lens was missing and a fallback was used."""
    names = list(lenses or {})
    design = "by_replicate" if by_replicate else "fixed"
    if by_replicate and names:
        want = names[replicate % len(names)]
    else:
        want = lens_arg or DEFAULT_LENS
    if want in names or not names:
        return want, design, ""
    return names[0], design, f"lens {want!r} not in the profile's lenses {names}; using the first, {names[0]!r}"


def select_profile(argv: list[str] | None = None) -> PF.Profile:
    """--profile NAME (default: env HTSA_PROFILE, else "llm"), applied before anything else reads the profile."""
    import os
    pre = argparse.ArgumentParser(add_help=False)
    pre.add_argument("--profile", default=os.environ.get("HTSA_PROFILE") or PF.DEFAULT)
    a, _ = pre.parse_known_args(argv)
    return PF.set_current(PF.load(a.profile))


def main() -> int:
    pf = select_profile()
    ck = make_checker(pf)
    ap = argparse.ArgumentParser()
    ap.add_argument("--profile", default=pf.name, help="problem profile: nano/profiles/<name>.py (default: env HTSA_PROFILE, else llm)")
    ap.add_argument("--batch", default="nano-1")
    ap.add_argument("--replicate", type=int, default=0)
    ap.add_argument("--backend", default=None)
    ap.add_argument("--model", default=None)
    ap.add_argument("--budget", type=int, default=400_000, help="token budget for the inventing model (the cheap model's calls are metered apart)")
    ap.add_argument("--aux-budget", type=int, default=0,
                    help="cap for the cheap model's retrieval and clerical tokens (a web-research call counts about half a million, pages re-read per turn); "
                         "0 = ten times --budget; past it the run stops searching the web and continues")
    ap.add_argument("--rounds", type=int, default=2)
    ap.add_argument("--smoke-seconds", type=float, default=60.0, help="(kept for compatibility; rung 3 uses --learn-steps)")
    ap.add_argument("--learn-steps", type=int, default=ck.LEARN_STEPS, help="rung 3: matched steps against the baseline curve")
    ap.add_argument("--long-steps", type=int, default=ck.LONG_STEPS, help="rung 4 for the pool (0 = skip)")
    ap.add_argument("--new-share", type=float, default=0.0, help="old quota of build slots for ideas tagged new (0 = off; the long-shot lane replaces it)")
    ap.add_argument("--longshot-share", type=float, default=0.3, help="build slots drawn at random from step-outside / analogy / adapt / new clusters")
    ap.add_argument("--controls", nargs="*", default=None, help="ladder controls each run (default: placebo_order zero_init_proj lr_x10; 'none' to skip; 'all' for every control)")
    ap.add_argument("--novelty-threshold", type=float, default=0.45, help="TF-IDF cosine above which a chosen idea is a near-duplicate of a build (gate); paraphrases score about 0.5")
    ap.add_argument("--no-retire-cards", action="store_true", help="keep attractor cards instead of retiring them")
    ap.add_argument("--staged-sketch", action="store_true", help="arm: seeds -> bolder -> elaborate inside each sketch call")
    ap.add_argument("--exclusion-list", action="store_true", help="arm: later rounds see the cluster names already covered")
    ap.add_argument("--cross-family-share", type=float, default=0.0, help="arm: share of sketch contexts sent to the cheap model family")
    ap.add_argument("--premortems", type=int, default=1, help="independent pre-mortems per interrogated idea (1-3)")
    ap.add_argument("--identity-init", action="store_true", help="arm: builders wrap new paths as x + tanh(a) f(x), a = 0, with gate read-out")
    ap.add_argument("--replan", action="store_true", help="arm: re-plan the map between rounds from the run's record")
    ap.add_argument("--weights-from-ledger", action="store_true", help="selection weights from nano/calibrate.py when >= 100 builds are on record")
    ap.add_argument("--hedge-share", type=float, default=0.0, help="share of rung-3 gap failures still sent to the long run and the night (lane hedge)")
    ap.add_argument("--no-fidelity", action="store_true", help="skip the diagnostic probe of checked candidates (did the named cell move?)")
    ap.add_argument("--program-search", default=None, help="arm: evolve one named function (e.g. lr_mult) with matched-step fitness")
    ap.add_argument("--program-k", type=int, default=4)
    ap.add_argument("--no-adapt", action="store_true", help="skip the port-and-adapt contexts")
    ap.add_argument("--no-contradictions", action="store_true", help="skip the measured trade-off contexts in later rounds")
    ap.add_argument("--arm", default="scaffold", choices=["scaffold", "plain", "climb"], help="control arms: plain = best-of-N direct builds; climb = sequential keep-or-discard")
    ap.add_argument("--n-builds", type=int, default=12, help="builds for the control arms")
    ap.add_argument("--lens", default=None, help="how the planner draws the map: " + ", ".join(tree.LENSES)
                    + f" (default {DEFAULT_LENS} for every replicate: the lens is a separate factor from the replicate)")
    ap.add_argument("--lens-by-replicate", action="store_true",
                    help="lens experiment: replicate r uses LENSES[r %% n] (recorded as lens_design by_replicate); "
                         "without it lens_design is fixed")
    ap.add_argument("--no-immediate-fix", action="store_true", help="do not fix rung 0/1 failures in the same round")
    ap.add_argument("--no-analogy", action="store_true", help="skip the cross-field analogy research and card")
    ap.add_argument("--no-diagnostics", action="store_true", help="skip the instrumented baseline run and the diagnosis card")
    ap.add_argument("--no-premortem", action="store_true", help="skip the pre-mortem call per interrogated idea")
    ap.add_argument("--no-memory", action="store_true",
                    help="control arm: no per-part memory block in prompts, no curator calls, no memory files")
    ap.add_argument("--max-compose", type=int, default=3, help="mechanical composites per round (0 = off)")
    ap.add_argument("--diag-steps", type=int, default=100)
    ap.add_argument("--resume", action="store_true", help="continue a run folder of the same batch/replicate from its last completed stage")
    ap.add_argument("--stop-after", default=None, choices=["ideated", "clustered", "deepened", "built", "verified"],
                    help="test mode: stop cleanly after this stage of round 1")
    ap.add_argument("--max-sketch-calls", type=int, default=0, help="test mode: at most this many idea agents per round")
    ap.add_argument("--no-tune", action="store_true", help="skip the scripted single-knob tuning sweep at round 1")
    ap.add_argument("--no-effort", action="store_true", help="do not set reasoning effort per role (CLI backend)")
    ap.add_argument("--no-fact-check", action="store_true", help="do not check numeric web claims against their page before a build")
    ap.add_argument("--tune-knobs", default="", help="comma-separated knob names from nano/tune.py (default: its DEFAULT list)")
    ap.add_argument("--tune-top", type=int, default=3, help="tuning candidates kept for the long run and the night")
    ap.add_argument("--anomaly-seeds", type=int, default=3, help="diagnostics seeds for the anomaly map (1 = no map)")
    ap.add_argument("--sham-share", type=float, default=0.1, help="chance that one anomaly row is a fabricated control (chasing is measured)")
    ap.add_argument("--seeds-file", default="", help="owner-written seed mechanisms: JSON list of {part, text}; default memory/owner_seeds.json when it exists")
    ap.add_argument("--family-variants", type=int, default=2, help="near-miss variants built per round from the ambitious lane (0 = off)")
    ap.add_argument("--leap-share", type=float, default=0.25, help="quota: share of each idea agent's sketches that must be leaps (rule breaks); 0 = off")
    ap.add_argument("--only-nodes", default="", help="test mode: only these parts take part (comma-separated ids, e.g. mix); the rest are skipped")
    ap.add_argument("--aim", default="", help="the purpose behind the goal, one or two sentences every agent reads (problem.md PURPOSE)")
    ap.add_argument("--digest-file", default=str(_doc_path("digest") or ""),
                    help="digest of what the strongest open models do now, put in front of every idea context (python -m nano.refresh_digest writes it)")
    ap.add_argument("--no-digest", action="store_true", help="do not show the digest to the idea contexts")
    ap.add_argument("--dashboard", action="store_true", help="serve the live view and open the browser")
    ap.add_argument("--port", type=int, default=8765)
    ap.add_argument("--retest-on-reference-change", action="store_true",
                    help="no-baseline profiles: when the reference moves, check the top three candidates again against it "
                         "(default: only re-label their gaps from the scores they have)")
    ap.add_argument("--per-node", type=int, default=1, help="ideation contexts per part x direction in round 1")
    ap.add_argument("--implement", type=int, default=10, help="implementation slots in round 1 (a third in later rounds)")
    ap.add_argument("--inward-share", type=float, default=0.6, help="share of slots for inward (within-paradigm) ideas")
    ap.add_argument("--off-tree-share", type=float, default=0.4,
                    help="share of idea contexts that work off the problem map (blank / gaps / doubt cards); 0 = off; moves with yield")
    ap.add_argument("--no-planner", action="store_true", help="use the default tree without a planner call")
    ap.add_argument("--no-research", action="store_true", help="skip the web research stage")
    ap.add_argument("--research-model", default="sonnet", help="model for the research role (retrieval)")
    ap.add_argument("--research-max-age", type=float, default=7.0, help="reuse cached briefs younger than N days")
    ap.add_argument("--cheap-model", default="sonnet", help="model for the planner and clustering roles")
    ap.add_argument("--no-ideation-web", action="store_true", help="ideation contexts get no web tools")
    ap.add_argument("--web-mode", default="delegate", choices=["delegate", "self", "off"],
                    help="how idea and questioning agents reach the web: delegate = they list questions and the research model "
                         "searches (default); self = they search themselves (multi-turn); off = no web")
    ap.add_argument("--no-deepen", action="store_true", help="skip the interrogation of chosen ideas")
    ap.add_argument("--deepen-depth", type=int, default=2, help="how many levels of open questions to follow")
    ap.add_argument("--deepen-fanout", type=int, default=1, help="open questions followed per level")
    ap.add_argument("--deepen-top", type=int, default=12, help="ideas interrogated per generation (top-ranked, round-robin across parts)")
    ap.add_argument("--deepen-generations", type=int, default=1, help="extra generations: ideas born in the interrogation get interrogated too")
    a = ap.parse_args()
    if a.lens and a.lens_by_replicate:
        ap.error("--lens and --lens-by-replicate exclude each other")
    loop = NanoLoop(a.batch, a.replicate, a.backend or config.default_backend(), a.budget, a.rounds,
                    a.smoke_seconds, a.model)
    loop.per_node, loop.k_impl, loop.inward_share = a.per_node, a.implement, a.inward_share
    loop.off_tree_share = max(0.0, min(0.6, a.off_tree_share))
    loop.plan_with_model = not a.no_planner
    loop.do_research, loop.research_model, loop.research_max_age_days = (not a.no_research), a.research_model, a.research_max_age
    loop.cheap_model = a.cheap_model
    loop.aux_budget = a.aux_budget if a.aux_budget > 0 else 10 * a.budget
    loop.web_mode = "off" if a.no_ideation_web else a.web_mode
    loop.ideation_web = loop.web_mode != "off"
    loop.do_deepen, loop.deepen_depth, loop.deepen_fanout = (not a.no_deepen), a.deepen_depth, a.deepen_fanout
    loop.deepen_top, loop.deepen_generations = a.deepen_top, a.deepen_generations
    loop.learn_steps, loop.long_steps, loop.new_share = a.learn_steps, a.long_steps, a.new_share
    loop.arm, loop.n_builds, loop.immediate_fix = a.arm, a.n_builds, not a.no_immediate_fix
    loop.do_analogy, loop.do_diagnostics, loop.do_premortem = not a.no_analogy, not a.no_diagnostics, not a.no_premortem
    loop.max_compose, loop.diag_steps = a.max_compose, a.diag_steps
    loop.resume = a.resume
    loop.stop_after, loop.max_sketch_calls = a.stop_after, a.max_sketch_calls
    loop.only_nodes = {x.strip() for x in a.only_nodes.split(",") if x.strip()}
    loop.aim = a.aim
    loop.digest_file = None if (a.no_digest or not a.digest_file) else Path(a.digest_file)
    loop.leap_share = max(0.0, min(1.0, a.leap_share))
    loop.anomaly_seeds, loop.sham_share, loop.family_variants = max(1, a.anomaly_seeds), max(0.0, min(1.0, a.sham_share)), max(0, a.family_variants)
    loop.tune, loop.tune_top = not a.no_tune, max(0, a.tune_top)
    loop.effort_by_role, loop.fact_check = not a.no_effort, not a.no_fact_check
    loop.tune_knobs = [x.strip() for x in a.tune_knobs.split(",") if x.strip()]
    seeds_path = Path(a.seeds_file) if a.seeds_file else (config.MEMORY_DIR / "owner_seeds.json")
    if seeds_path.exists():
        try:
            loop.owner_seeds = [d for d in json.loads(seeds_path.read_text(encoding="utf-8")) if isinstance(d, dict)]
            print(f"[nano] owner seeds: {len(loop.owner_seeds)} from {seeds_path}", flush=True)
        except Exception as e:  # noqa: BLE001
            print(f"[nano] owner seeds file unreadable: {e}", flush=True)
    loop.longshot_share, loop.novelty_threshold, loop.retire_cards = a.longshot_share, a.novelty_threshold, not a.no_retire_cards
    loop.controls = (None if (a.controls == ["none"]) else (a.controls if a.controls is not None else loop.controls))
    loop.staged_sketch, loop.exclusion_list, loop.cross_family_share = a.staged_sketch, a.exclusion_list, a.cross_family_share
    loop.premortems, loop.identity_init, loop.replan = a.premortems, a.identity_init, a.replan
    loop.weights_from_ledger, loop.hedge_share, loop.fidelity = a.weights_from_ledger, a.hedge_share, not a.no_fidelity
    loop.program_search, loop.program_k = a.program_search, a.program_k
    loop.adapt_card, loop.contradiction_cards = not a.no_adapt, not a.no_contradictions
    loop.lens, loop.lens_design, lens_note = choose_lens(a.lens, a.replicate, a.lens_by_replicate, tree.LENSES)
    if lens_note:
        print(f"[nano] {lens_note}", flush=True)
        loop.decisions.append({"step": "lens", "decision": "fallback", "lens": loop.lens, "reason": lens_note})
    loop.retest_on_reference_change = a.retest_on_reference_change
    loop.use_memory = not a.no_memory
    if a.dashboard:
        from nano import dashboard
        threading.Thread(target=dashboard.serve, args=(loop.run_dir, a.port, True), daemon=True).start()
        time.sleep(1.0)
    ans = loop.run()
    print(json.dumps({k: ans[k] for k in ("n_candidates", "n_checked", "spent_tokens", "wall_s")}))
    for r in ans["ranked"]:
        print(f"  {r['id']} {r['card']:9s} extrap z {r['extrap_z']} long z {r['long_z']} learn z {r['learn_z']} step {r['step_s']}s | {r['change']}")
    if ans.get("reference_changes"):
        for e in ans["reference_changes"]:
            print(f"  reference {e['action']}: {e['from'] or '-'} -> {e['to']} (round {e['round']}) | {e['reason']}")
    for p in ans.get("proposals", []):
        print(f"  proposal {p['rank']}. {p['id']} panel {p['panel_score']} sd {p['panel_sd']} | {p['claim'][:90]}")
    for u in ans.get("upward_proposals", [])[:5]:
        print(f"  upward: {u.get('proposal')}")
    print(f"run folder: {loop.run_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())


_COMPAT = {"BASELINE": baseline_path, "SPEC_ID": spec_id, "CONSTRAINTS": constraints,
           "ASSUMPTIONS": lambda: list(PF.current().assumptions), "OUTPUT_FORMAT": output_format}


def __getattr__(name: str):
    """loop.CONSTRAINTS, loop.OUTPUT_FORMAT, ... read the active profile at access time (PEP 562)."""
    if name in _COMPAT:
        return _COMPAT[name]()
    raise AttributeError(f"module 'nano.loop' has no attribute {name!r}")
