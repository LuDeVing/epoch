"""HTSA harness configuration: paths, models, backends, flags and control parameters.

Single source of truth for every module. Code lives on C: (this tree); runs, memory,
data and results live under the lab root on D: (ARCHITECTURE.md section 2, storage note).
Nothing here reads benchmark keys or run files.
"""
from __future__ import annotations

import contextvars
import os
import sys
from pathlib import Path

# ---------------------------------------------------------------- paths
PROJECT_ROOT = Path(__file__).resolve().parent.parent          # C:\Users\User\Desktop\AGI
HARNESS_DIR = PROJECT_ROOT / "harness"
LAB_ROOT = Path(os.environ.get("HTSA_LAB_ROOT", r"D:\AGI-lab"))
RUNS_DIR = LAB_ROOT / "runs"
MEMORY_DIR = LAB_ROOT / "memory"
VIEWS_DIR = MEMORY_DIR / "views"
LEDGER_PATH = MEMORY_DIR / "ledger.jsonl"
DATA_DIR = LAB_ROOT / "data"
RESULTS_DIR = LAB_ROOT / "results"
RAW_DATA_DIR = LAB_ROOT / "data"                                 # raw downloads (arc/, brainteaser/)
# Strategy cards and templates are code, so they live in the harness tree (not under memory/ on D:).
STRATEGIES_DIR = HARNESS_DIR / "strategies"
TEMPLATES_DIR = STRATEGIES_DIR / "templates"
SEEDS_PATH = STRATEGIES_DIR / "seeds" / "concepts.txt"
LINT_PATTERNS_PATH = HARNESS_DIR / "lint_patterns.yaml"
# Interpreter for candidate programs (arc_exec). Fixed, not derived from LAB_ROOT, so a temp lab
# root in tests still points at a real python: HTSA_EXEC_PYTHON, else the D: venv, else this one.
_DEFAULT_VENV_PYTHON = Path(r"D:\AGI-lab\.venv\Scripts\python.exe")
VENV_PYTHON = Path(os.environ.get("HTSA_EXEC_PYTHON")
                   or (_DEFAULT_VENV_PYTHON if _DEFAULT_VENV_PYTHON.exists() else sys.executable))



def ensure_lab_dirs() -> None:
    """Create the lab folders on first use, never at import (an import must not need D:).
    The JSON and JSONL writers in schemas.py create parent folders as well."""
    for d in (RUNS_DIR, MEMORY_DIR, VIEWS_DIR, DATA_DIR, RESULTS_DIR):
        d.mkdir(parents=True, exist_ok=True)


# ---------------------------------------------------------------- models and backends
# Logical model names map to backend-specific ids. All roles in all arms use the same logical model.
DEFAULT_MODEL = os.environ.get("HTSA_MODEL", "sonnet")   # e.g. HTSA_MODEL=haiku for a cheap benchmark run
MODEL_IDS = {
    "cli_json":     {"sonnet": "sonnet", "opus": "opus", "haiku": "haiku", "fable": "claude-fable-5-1"},
    "messages_api": {"sonnet": "claude-sonnet-5-5", "opus": "claude-opus-5-5", "haiku": "claude-haiku-5-5",
                     "fable": "claude-fable-5-1"},
    "mock":         {"sonnet": "mock", "opus": "mock", "haiku": "mock", "fable": "mock"},
}
# USD per million tokens (list price, used only for reporting; tokens are the cost unit).
# fable: estimated from one measured CLI call (2026-10-11: 48,614 cache-creation tokens cost $0.97).
PRICE_PER_M = {
    "sonnet": {"input": 3.0, "output": 15.0, "cache_read": 0.30, "cache_create": 3.75},
    "opus":   {"input": 15.0, "output": 75.0, "cache_read": 1.50, "cache_create": 18.75},
    "fable":  {"input": 16.0, "output": 80.0, "cache_read": 1.60, "cache_create": 20.0},
    "haiku":  {"input": 1.0, "output": 5.0, "cache_read": 0.10, "cache_create": 1.25},
}
# Measured CLI system-prompt overhead per call with --tools "": sonnet ~3k tokens, fable ~48k.
CLI_BIN = os.environ.get("HTSA_CLAUDE_BIN", "claude")
# Isolation flags for claude -p: --safe-mode disables CLAUDE.md, hooks, plugins, MCP servers and
# other customizations; --strict-mcp-config skips every MCP server not passed explicitly.
# (Listed in `claude --help` 2.1.296; the effect on the init context is not yet verified on a
# real call.) Override with HTSA_CLI_EXTRA_ARGS (space-separated).
CLI_EXTRA_ARGS = (os.environ["HTSA_CLI_EXTRA_ARGS"].split()
                  if os.environ.get("HTSA_CLI_EXTRA_ARGS") is not None
                  else ["--safe-mode", "--strict-mcp-config"])
# Roles whose replies are private run files (Pr5): their call records, sandbox and reply go
# under runs/<id>/private/calls/, never beside the generator calls.
PRIVATE_ROLES = ("defaults",)
# Measured 2026-10-10: claude -p with --tools "" carries about 3k tokens of fixed system-prompt
# overhead per call (about 26k with tools enabled). Counted in cost like every other token.
CLI_OVERHEAD_TOKENS_EST = 3000


def default_backend() -> str:
    """messages_api when an API key is present, else the Claude Code CLI in JSON mode."""
    forced = os.environ.get("HTSA_BACKEND")
    if forced:
        return forced
    return "messages_api" if os.environ.get("ANTHROPIC_API_KEY") else "cli_json"


# ---------------------------------------------------------------- benchmarks
# ARC item sets. The headroom scan of 2026-10-11 found plain Sonnet solves 36/40 of the ARC-AGI-1
# <= 600-cell subset (ceiling), so the gate set is ARC-AGI-2 public evaluation (section 8:
# "ARC-AGI-2 public eval preferred over ARC-1"). Select with HTSA_ARC_SET=arc1|arc2.
ARC_SET = os.environ.get("HTSA_ARC_SET", "arc2")
ARC_FILES = {
    "arc1": DATA_DIR / "arc_agi1_eval_le600.jsonl",     # 40 tasks, <= 600 cells, 1 test pair
    "arc2": DATA_DIR / "arc_agi2_eval_le2400.jsonl",    # ARC-AGI-2 eval, <= 2400 cells, 1 test pair
    "arc1mid": DATA_DIR / "arc_agi1_eval_mid.jsonl",    # 40 ARC-AGI-1 eval tasks, 601-2400 cells, 1 test pair, seed 11, split "mid"
    "arc1fresh": DATA_DIR / "arc_agi1_eval_fresh.jsonl",  # 60 further ARC-1 eval tasks, 601-2400 cells, disjoint from arc1/arc1mid, seed 12, split "fresh"
    "arc1large": DATA_DIR / "arc_agi1_eval_large.jsonl",  # up to 60 ARC-1 eval tasks, > 2400 cells, 1 test pair, disjoint from other sets, seed 13, split "large"
}
BENCHMARKS = {
    "arc": {
        "file": ARC_FILES.get(ARC_SET, ARC_FILES["arc2"]),
        "dedup_rule": "grid",            # exact predicted test-output grid
        "verification_type": "demo_match",
        "revise_allowed": True,
        "graded": True,                  # partial score = fraction of train pairs matched
        "formalizable": True,
        "cands_per_generator": 3,        # programs: 1-3 per call
        "n0": 5,                         # seeded + memory-blind + low_prior + transform + formal
        "key_field": "test_output",      # read by the harness scorer only
    },
    "bt": {
        "file": DATA_DIR / "brainteaser_sp.jsonl",
        "dedup_rule": "option",          # exact option letter
        "verification_type": "agreement",
        "revise_allowed": False,
        "graded": False,
        "formalizable": False,
        "cands_per_generator": 8,
        "n0": 4,                         # seeded + memory-blind + low_prior + transform
        "key_field": "label",            # read by the harness scorer only
    },
}

# ---------------------------------------------------------------- flags (gate configuration = all P1 off)
FLAGS = {
    "graph": True,                       # I3, P0 diagnostic (0 tokens)
    "pruning_regret": True,              # I4 step 1, P0 diagnostic (offline)
    "restructure": False,                # P1
    "lemmas": False,                     # I1, P1
    "card_decompose": False,             # I2, P1
    "gap_pack": "off",                   # I6, P1: off | goal_keyed | gap_keyed
    "frontier": "tournament",            # I4, P1: tournament | beam_topK | smc
    "verify_order": "top_conf",          # I4, P1: top_conf | top_conf_plus_explore
    "harvest_unspoken": "off",           # I5: off | capture (P1) | merge (P2)
    "seed_type": "concept",              # SOC-02: concept | doc_pack (P1)
    # memory views batch id; None = empty memory. HTSA_SNAPSHOT sets it for a bench batch; think
    # builds the view from that batch's train-split ledger rows on first use (stats.rebuild).
    "snapshot": os.environ.get("HTSA_SNAPSHOT") or None,
    "signature": False,                  # REP-01, P1
    "p_raw_validated": False,            # EVL-08 entry gate
    "llm_falsifier_validated": False,    # EVL-02
    "shuffle_facts": True,               # REP-08 (pre-gate flag 4)
    "dedup": True,                       # CTL-10 (pre-gate flag 3)
    "early_stop": True,                  # CTL-05 (pre-gate flag 2)
    "reset_on_stagnation": True,         # CTL-11 (pre-gate flag 1)
    "judge_when_verify_free": False,     # pilot-2: judge cost 114k/219k on ARC while steering nothing
    # Environment toggles, recorded here so the run header (state.json) and every call record carry them.
    "raw_view": bool(os.environ.get("HTSA_RAW_VIEW")),   # no decomposition: every view is the raw item
    # EXPERIMENTAL, off in the gate configuration: "1" or "2" swaps format.arc for
    # format_think[2].arc, which asks the generator to check its rule against the examples.
    # That is generator self-checking, which Pr1 bans for generators; it exists only as a
    # measured arm (research_notes/thinking_modes/00_SYNTHESIS.md), never as a default.
    "experimental_think_aloud_self_check": os.environ.get("HTSA_THINK_ALOUD", "") or "off",
    # EVL-08 / Pr17: share of items (hashed on item id and replicate) whose candidates are judged
    # for calibration only when the check is a free script. p_raw is logged to judgments.jsonl and
    # the ledger (calibration_only), never steers the run and is not charged to B. 0 = off.
    "judge_calibration_sample": 0.0,
}
# The flags above that come from the environment; llm.call copies them into every call record.
ENV_FLAGS = ("raw_view", "experimental_think_aloud_self_check")

# The effective flags of the run in progress: think() sets FLAGS merged with its --flag overrides
# here, so encode.raw_view() and the call-record flag copy read what the run really uses. A
# context variable keeps concurrent runs (bench threads) apart; think's worker pools and
# llm.call_many copy the context into their threads. Outside a run, flags() is FLAGS.
_RUN_FLAGS: contextvars.ContextVar = contextvars.ContextVar("htsa_run_flags", default=None)


def flags() -> dict:
    """The effective flag dict: the current run's merged flags, else FLAGS."""
    return _RUN_FLAGS.get() or FLAGS


def use_flags(merged: dict):
    """Set the effective flags for this context; returns the token for reset_flags."""
    return _RUN_FLAGS.set(merged)


def reset_flags(token) -> None:
    _RUN_FLAGS.reset(token)

# ---------------------------------------------------------------- control parameters (section 5)
PARAMS = {
    "m": 20,                     # cost multiplier over plain CoT
    "R_max": 3,                  # round cap
    "max_spawns_extra": 3,       # max_spawns_per_round = n0 + 3
    "m_verify": 3,               # candidates verified per round when verification costs tokens
    "verify_all_when_free": True,  # script-only checks (ARC demo_match) verify every candidate
    "k_base": 1, "k_max": 3, "alpha": 1.0,   # attempts k = base + ceil(alpha * c), capped
    "hi": 0.8,                   # surprise threshold on c
    "R_stale": 2, "d_max": 0.5,  # stagnation rules
    "k_pop": 5, "theta_admit": 0.6,
    # Thresholds are exact fractions; think compares them with a 1e-9 tolerance and also accepts
    # "a/b" strings (CLI --param T=2/3). 0.67 would exclude 2 of 3 (2/3 = 0.6667 < 0.67).
    "T": 2 / 3,                  # identity-map acceptance: 2 of 3 probe agreement (placeholder)
    "T_checked": 0.9,            # inactive until llm_falsifier_validated
    "optout": 2 / 3,             # opt-out level for an unverified best guess (placeholder)
    "eps": 0.01,                 # minimum partial-score gain that counts as progress
    "n_probe": 3,                # agreement probe calls, once per item
    "N_min": 20,                 # ledger rows per cell before Thompson allocation
    "exploration_floor": 0.10,
    "encode_cap_mult": 2.0,      # encode cap = this x max_tokens["plain"] (32000); checked only before the optional resolve call
    # Raised 2026-10-11 after a plain ARC run hit the 4000-token output cap (headroom-test errors).
    # Raised again 2026-10-11: 9/32 plain ARC-2 runs exceeded 8000 output tokens (long reasoning
    # before the program). A truncated plain answer would understate the baseline unfairly.
    "max_tokens": {"encode": 3000, "generate": 6000, "program": 8000, "judge": 1500,
                   "probe": 8000, "verify": 1500, "plain": 16000},
    "max_turns": 1,              # no tool loops at P0; the runner executes programs itself
    "call_timeout_s": int(os.environ.get("HTSA_CALL_TIMEOUT", "600")),   # long-thinking calls (ARC-2 at high effort) need more
    "exec_timeout_s": 10,        # ARC: seconds of CPU time per input grid (and the import); wall guard 4x (arc_exec.WALL_FACTOR)
    "feedback_cap_tokens": 1500,
}

# HTSA_PARAMS: a JSON object that overrides PARAMS for a smaller run, e.g. {"R_max": 1, "n_probe": 1}
if os.environ.get("HTSA_PARAMS"):
    import json as _json
    PARAMS.update(_json.loads(os.environ["HTSA_PARAMS"]))

# ---------------------------------------------------------------- roles (templates are tight or loose by role)
ROLES = ("encode", "defaults", "generate", "transform", "judge", "probe", "verify", "plain", "converter")

# Guard against runaway views (routed inputs are inlined into prompts). A longer prompt is cut
# in the middle with a visible marker by llm.fit_prompt, before prompts/<id>.txt is written, and
# the cut is recorded in the call record (prompt_truncated); never silently.
MAX_PROMPT_CHARS = int(os.environ.get("HTSA_MAX_PROMPT_CHARS", "60000"))
