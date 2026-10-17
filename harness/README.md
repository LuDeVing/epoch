# HTSA harness: module map and contracts

Spec: `../ARCHITECTURE.md` v0.3 (sections 2, 3, 4, 5, 8, 9). This file pins the module split,
file ownership and the interfaces every module must honour. Python 3.12, venv at
`D:\AGI-lab\.venv` (`python.exe` at `D:\AGI-lab\.venv\Scripts\python.exe`). Dependencies:
stdlib, `anthropic`, `numpy`, `pyyaml`, `pytest`. No other packages without a note here.

Run everything as a package from the project root: `python -m harness.<module> ...`
(e.g. `python -m harness.bench --help`). Imports inside the package are relative (`from . import config`).

## Where things live

| What | Where | Note |
|---|---|---|
| Code, cards, templates, tests | `C:\Users\User\Desktop\AGI\harness\` | this tree |
| Runs, memory, data, results | `D:\AGI-lab\{runs,memory,data,results}` | `config.LAB_ROOT`; C: has 3 GB free |
| Raw downloads | `D:\AGI-lab\data\arc\ARC-AGI-master\data\{training,evaluation}\*.json`, `D:\AGI-lab\data\brainteaser\{SP,WP}.jsonl` | built into item files by `data.py` |

## Shared contracts (do not change without updating this file)

- `config.py`: paths, `MODEL_IDS`, `FLAGS` (gate config), `PARAMS` (section 5), `BENCHMARKS`.
  Lab paths follow `HTSA_LAB_ROOT` (default `D:\AGI-lab`); `VENV_PYTHON` (candidate interpreter
  for `arc_exec`) is fixed: `HTSA_EXEC_PYTHON`, else the D: venv, else `sys.executable`, so a
  temp lab root in tests still points at a real python.
- `schemas.py`: `Usage`, `Candidate`, `Judgment`, `VerifyResult`, `LedgerRow`, `Answer`, item
  formats, `strip_key()`, JSON/JSONL helpers. Record field names are fixed.
- `llm.py`: `call(prompt, role=..., call_id=..., model=None, max_tokens=None, cwd=None,
  backend=None, log_dir=None, meta=None) -> CallResult{text, usage: Usage, cost_usd, error,
  max_tokens, usage_estimated, attempt_errors}`.
  Backends: `cli_json` (default without an API key), `messages_api`, `mock` (tests; `set_mock(fn)`,
  which may raise `llm.CallError(msg, usage=...)` to simulate an error that consumed tokens).
  No tools at P0 for any role. Every call is charged by `usage.total_tokens`: usage is parsed
  before an error is raised and summed over retry attempts; a timeout is charged by estimate
  (prompt chars / 4 + max_tokens + CLI overhead, `usage_estimated` true). The CLI backend runs
  without a shell in its own process group (timeout kills the tree), passes the output cap as
  `CLAUDE_CODE_MAX_OUTPUT_TOKENS`, adds `config.CLI_EXTRA_ARGS` (`--safe-mode --strict-mcp-config`)
  and charges the larger of the record's `usage` and the sum over `modelUsage`. Every call record
  logs `max_tokens` and `over_cap`.
- Cost unit: `Usage.total_tokens` = input + cache_read + cache_creation + output. B = m x median
  plain-CoT tokens per item on dev (per benchmark, per backend; successful plain calls only).
  Best-of-N arms stop at the scaffold's realized spend per item (plan.md section 2: sized by the
  mean call cost, one mean call kept in reserve per parallel batch, the last call alone;
  `overshoot` recorded per run). When the scaffold arm is
  requested and an (item, replicate) has no successful scaffold run, the best-of-N run is
  skipped and logged to `errors.jsonl`, never run at B silently. In the driver, every spend
  (spawn, judge, verify) is estimated and checked against B before the call; a judge round
  that does not fit is skipped (`judge_skipped` in the decision row).
- Keys: `item["test_output"]` (ARC) and `item["label"]` (BT) are read in the bench pipeline only
  by `score.py`; the standalone scorers `portfolio_arc.py`, `portfolio_v2.py`,
  `portfolio_offline.py`, `arc_think.py` (after every model call of the item) and `lite_bt.py`
  (keeps the key in its result row, never in a prompt) read them too, and `data.py` builds them.
  Every prompt, view and run file is built from `strip_key(item)`. Tests assert this:
  `tests/test_fix_bench.py` scans every harness module and fails on any other reader.
- Private roles (`config.PRIVATE_ROLES`, the defaults call): their call record, sandbox and
  reply live under `runs/<id>/private/calls/`, never beside the generator calls (Pr5). Tests
  grep every run file outside `private/` for the defaults reply. `problem.md` carries no item id.
- Run folder: `runs/<run_id>/` per (item, arm, replicate) with the files of ARCHITECTURE section 2.
  `run_id = f"{batch}__{benchmark}__{item_id}__{arm}__r{replicate}"`.
- Call ids: `new_id("c")`; every call's prompt is written to `runs/<id>/prompts/<call_id>.txt` and
  its usage record to `runs/<id>/calls/<call_id>.json` (`log_dir`). Sandboxed inputs are inlined
  into the prompt; `cwd` for CLI calls is `runs/<id>/calls/<call_id>/in/` holding only routed files.
  Every prompt of every role comes from a file in `strategies/templates/` (cards: `<card>.<step>.txt`;
  `judge.txt`, `probe.<benchmark>.txt`, `plain.<benchmark>.txt` for the judge, probe and plain
  arms) rendered through `run_card.render_prompt`, so `lint_templates()` and the per-render lint
  cover them and each call has a `routing.jsonl` row.
- Ledger rows are one per model call (`call_id` = the call's id, `tokens` = that call's
  `Usage.to_dict()`); verification rows keep the candidate's call id and `cand_id`. Every row and
  every `runs.jsonl` row carries `run_instance`, a fresh id per `think()` / `run_arm()` attempt;
  `ledger.current_rows()` keeps the latest instance per `run_id` and `stats.rebuild` uses it.
  JSONL appends go through `schemas.append_jsonl` (one lock, one write per append) and
  `read_jsonl` skips a torn line with a warning (`strict=True` raises).
- Run instances and crashes: `think()` never leaves a run folder without `answer.json`. A crash
  writes `error.json`, an abstain `answer.json` (reason `crash: ...`) and a `runs.jsonl` row with
  status `error`; `bench` retries runs whose last row is `error`, and `think` moves such a folder
  aside as `<run_id>.old-<ts>` instead of raising. A completed run still raises `FileExistsError`
  without `--force`.
- Candidate text for ARC is a python program defining `transform(grid) -> grid`; `arc_exec.py`
  runs it on the train pairs (demo_match, partial_score = matched/total) and on the test input to
  get `pred` (used for dedup, probe agreement and harness scoring; the test output never enters
  the loop). For BT a candidate is an option letter A-D with optional one-line text.
- Determinism: `replicate` (int) seeds every random choice (seed words, permutations, probe) via
  `random.Random(f"{item_id}:{arm}:{replicate}:{purpose}")`; fact permutations are
  `encode.perm_order(item_id, perm, n, replicate)`, so perm ids give a different order per
  replicate, and `flags.shuffle_facts = False` forces perm 0 everywhere (`run_card` receives the
  run's flags). RNGs never key on candidate uuids (tournament: queue shape; revise: stable
  parent fields). Model nondeterminism is noise.

## Modules and owners (each owner also writes `tests/test_<module>.py` against the mock backend)

| Module | Owner | Responsibility |
|---|---|---|
| `data.py` | bench | Build `data/arc_agi1_eval_le600.jsonl` (40 ARC eval tasks with <= 600 cells and one test, fixed seed 7) and `data/brainteaser_sp.jsonl` from the raw downloads; assign splits (dev-tune, dev-ablate, test, by fixed seed); `load_items(benchmark, split=None)`. |
| `score.py` | bench | Harness-side scoring against keys: ARC exact grid match, BT option match; coverage (oracle pass@pool) vs selection; paired difference with cluster bootstrap over items; summary tables. The only key reader in the bench pipeline (the standalone scorers listed under Keys above also read them). |
| `arms/plain.py`, `arms/best_of_n.py` | bench | Plain CoT arm (one call, parse final answer); best-of-N by majority vote; best-of-N with the same verifier (N capped by the scaffold's realized spend on that item); seeded best-of-N. Each arm writes a run folder with `answer.json`, `calls/`, `prompts/` and ledger rows. |
| `bench.py` | bench | CLI: `--benchmark arc|bt --arm plain|bestofn_vote|bestofn_verify|seeded_bestofn|scaffold --split dev-tune --items N --replicates R --backend ... --m 20 --batch <name>` (`--arm` is repeatable or comma-separated); lints the templates first (blocking); measures plain CoT cost first (writes `results/<batch>/cost.jsonl`, successful calls only); runs arms; scores; writes `results/<batch>/summary.json` and `summary.md`; lints every rendered prompt of the batch into `results/<batch>/lint.json`. `plan.md` draft with the cost definition, splits and arms. |
| `arc_exec.py` | verify | Safe execution of candidate programs: subprocess with the venv python, `-s -P -B -X utf8`, scrubbed env (`PYTHONHASHSEED=0`), Windows job object (the whole process tree dies on timeout and after the run), nonce-marked result line and `os._exit`, a CPU-time limit of `PARAMS.exec_timeout_s` per input grid (and the import) with a 4x wall-clock guard, later inputs skipped after a timeout, output size cap; `run_program(src, grids) -> list[grid|None]`; `demo_match(src, train) -> (matched, total, diffs)`; `predict(src, test_input) -> grid|None`; grid validation (rectangular ints 0-9, <= 30x30). |
| `verify.py`, `feedback.py` | verify | `build(problem) -> VerifierHandle{hash, type}`; `run(cand, handle, attempts, benchmark) -> VerifyResult` (ARC: demo_match + predicted grid; BT: agreement-only placeholder returning `unverified` with partial_score = agreement supplied by the driver); `feedback.py` deterministic records (failing pair diffs capped). Verification types and status strata exactly as in schemas. |
| `run_card.py`, `strategies/*.yaml`, `strategies/templates/*.txt`, `strategies/schema.json`, `strategies/seeds/concepts.txt`, `encode.py`, `lint.py`, `lint_patterns.yaml` | cards | Card loader and executor (`run_card(spec, run_dir, problem, backend) -> list[Candidate]` plus return contract `{id, path, n_cands}`); templates rendered with routed files only; numbered-list and code-block parsing; post-check that strips justification markers; the five P0 cards (seeded, low_prior, transform 3-call DAG, formal, revise 1-parent). `encode.py`: two checklist calls + script merge (+ resolve call on disagreement), `problem.md`, `constraints.json`, `private/defaults.json` (separate call), views (canonical, shuffled, low_prior), `encode_tokens` with cap. `lint.py`: blocking patterns (personas, stakes, bodily imperatives, "subconscious"/hidden-reasoning wording) and warnings (be-creative wording). |
| `judge.py`, `probe.py`, `think/dedup.py`, `think/allocate.py`, `think/admit.py`, `think/stop.py`, `think/stagnation.py`, `think/tournament.py` | control | Blind judge (pointwise or batch <= 5 under two permutations, p_raw logged; ARC programs stripped of comments and docstrings; `est_cost` for the budget check); agreement probe (n_probe seeded calls once per item, cluster by benchmark rule, `agreement(cand) -> fraction`), identity calibration map at P0; dedup by exact rule with `clusters.jsonl` rows; allocation (round-robin with the directed-card minimum; Thompson once N_min rows exist); admission; stop rule (fixed T, opt-out, abstain); stagnation (unused tuples, reset); tournament on verifier partial scores. |
| `ledger.py`, `stats.py`, `graph.py`, `measure/pruning_regret.py` | memory | Append-only ledger writer; `stats.py` rebuilds `memory/views/<batch>/strategy_stats.json` from train rows; `graph.py --write|--render|--check <run_dir>` (nodes, edges, cluster root counts, HTML view, completeness check); `measure/pruning_regret.py` offline diagnostic over a batch (keyed items, uses score.py). |
| `think.py` | driver | The orchestrator of ARCHITECTURE section 4 with the gate flags (P1 hooks present but off): encode -> verifier build -> probe -> rounds (spawn cards in parallel, a thread pool over `run_card`, dedup, judge, agreement, verify top m_verify, ledger rows, graph write after every cycle and at the end, stop/stagnation/reset) -> `answer.json`. CLI: `python -m harness.think --benchmark arc --item <id> --m 20 --replicate 0 --backend mock|cli_json|messages_api --batch dev [--force]`. Layout: `harness/think/` (control submodules) shadows `think.py`; `think/__init__.py` forwards `think`, `main` to the driver and `think/__main__.py` runs it. |
| `tests/` | all | pytest; `conftest.py` sets `HTSA_LAB_ROOT` to a temp dir and backend `mock` before any harness import, and an autouse fixture repoints every `config` lab path at the test's `tmp_path`; `test_e2e.py` runs `think` (ARC and BT), `graph --check/--render`, the module entry points as subprocesses and `bench` with plain + bestofn_verify + scaffold on synthetic items, asserting run folders, ledger rows, graph check, no key string in any prompt and best-of-N stopping at the scaffold's spend. |
| `.claude/skills/think/SKILL.md`, `.claude/skills/bench/SKILL.md` | driver | Thin launchers: run the python entry point and summarize `answer.json` / `summary.md`. No control logic. |

## Conventions

- Plain ASCII in prompts and files; no em-dashes; no personas or role-play anywhere (lint).
- Generator templates are loose: goal, facts, constraints, operator, seed, output format. No rubric,
  no evaluative language, no mention of judging. Judge and verify templates are tight.
- Never write the key, `private/*`, failed candidates, `graph.jsonl`, `clusters.jsonl` or any
  lineage view into a generator prompt or sandbox.
- Every record is one JSON object per line; never rewrite the ledger; derived views are rebuilt.
- Windows: use `pathlib`, `encoding="utf-8"` everywhere, no shell pipelines in subprocess calls.
- Keep modules small and testable; functions over classes unless state is real.

## Interfaces (exact signatures; implement these names)

```python
# data.py (bench)
def build_items(seed: int = 7) -> dict            # writes both item files; returns counts per split
def load_items(benchmark: str, split: str | None = None) -> list[dict]
def get_item(benchmark: str, item_id: str) -> dict
# splits: "dev-tune", "dev-ablate", "test" assigned by fixed seed; ARC subset = 40 items, BT = 120 items

# score.py (bench)  -- the only key reader in the bench pipeline (see Keys above for the standalone scorers)
def is_correct(item: dict, answer) -> bool        # ARC: grid == test_output; BT: letter == option_letter(label)
def cand_correct(item: dict, cand: dict) -> bool  # uses cand["pred"]
def score_batch(batch: str) -> dict               # reads results/<batch>/runs.jsonl + run folders; writes summary.json/.md
def paired_bootstrap(a: list[float], b: list[float], n: int = 2000, seed: int = 0) -> dict  # mean diff, 95% CI

# arc_exec.py (verify)
def valid_grid(g) -> bool
def run_program(src: str, inputs: list, timeout_s: float | None = None) -> list      # grid or None per input
def demo_match(src: str, train: list[dict]) -> dict   # {"matched", "total", "diffs": [...], "errors": [...]}
def predict(src: str, test_input) -> list | None

# verify.py / feedback.py (verify)
@dataclass class VerifierHandle: type: str; hash: str; data: dict
def build(problem, benchmark: str) -> VerifierHandle
def run(cand: Candidate, handle: VerifierHandle, *, attempts: int, benchmark: str,
        agreement: float | None, run_dir: Path) -> VerifyResult
def record_for(cand: Candidate, demo: dict, benchmark: str, cap_tokens: int = 1500) -> dict   # feedback.py

# encode.py (cards)
@dataclass class Problem: item_id: str; benchmark: str; goal: str; facts: list[str]; resources: list[str];
    checklist: list[str]; bar: dict; views: dict[str, str]; problem_md: str; encode_tokens: int;
    item: dict  # key-stripped item (train pairs / question + choices)
    meta: dict = {}  # shuffled_perm, low_prior parts, encode log (cards; additive)
def encode(item: dict, run_dir: Path, *, backend: str, replicate: int, log_dir: Path) -> Problem
    # writes problem.md, constraints.json, private/defaults.json, variants/*.md

# run_card.py (cards)
@dataclass class CardSpec: card: str; operator: str = "none"; seed: str = ""; perm: int = 0;
    variant: str | None = None; parent_id: str | None = None
@dataclass class CardRun: cands: list[Candidate]; usage: Usage; call_ids: list[str]; contract: dict
def load_card(name: str) -> dict
def run_card(spec: CardSpec, problem: Problem, run_dir: Path, *, backend: str, round_no: int,
             log_dir: Path, replicate: int, parent: Candidate | None = None,
             feedback: dict | None = None, flags: dict | None = None) -> CardRun
    # flags = the run's flag dict (shuffle_facts); an error after a call returned is reported in
    # contract["error"] with the completed steps' cands, usage and call_ids (never lost spend);
    # a multi-step card routes one scripted parent (first candidate of the previous step) with
    # its deterministic feedback record to the next step
def parse_candidates(text: str, benchmark: str) -> list[dict]   # [{"text", "program"|None, "pred"|None}]
def code_blocks(text: str) -> list[str]           # shared fenced-code parser (any info string, unclosed final fence)
def render_prompt(template: str, values: dict, *, role: str, run_dir: Path, call_id: str,
                  meta: dict | None = None) -> str # render + prompts/<id>.txt + lint + routing row (judge, probe, plain)

# lint.py (cards)
def lint_text(text: str) -> list[dict]            # [{"pattern", "severity": "fail"|"warn", "span"}]
def lint_templates() -> dict                      # {"fails": [...], "warns": [...]}

# judge.py (control)
def judge(cands: list[Candidate], problem: Problem, *, backend: str, log_dir: Path,
          replicate: int) -> tuple[list[Judgment], Usage]
def est_cost(cands: list[Candidate], problem: Problem, backend: str | None = None) -> int
def strip_rationale(src: str) -> str              # program without comments and docstrings

# probe.py (control)
@dataclass class ProbeResult: clusters: dict[str, int]; n: int; usage: Usage; cands: list[Candidate];
    calls: list[dict]   # [{call_id, usage, error, seed}] per probe call (ledger rows per call)
def run_probe(problem: Problem, *, n: int, backend: str, log_dir: Path, replicate: int, run_dir: Path) -> ProbeResult
def agreement(probe: ProbeResult, cand: Candidate, benchmark: str) -> float   # share of probe calls in cand's cluster
def calibrate(agreement_value: float, p_raw: float | None, flags: dict) -> float   # identity map at P0

# think/dedup.py (control)
def dedup_key(cand: Candidate, benchmark: str) -> str
def rate(new: list[Candidate], prior: list[Candidate], benchmark: str) -> float
def drop(new: list[Candidate], prior: list[Candidate], benchmark: str, round_no: int) -> tuple[list[Candidate], list[dict]]

# think/allocate.py (control)
def initial(benchmark: str, cls: str, views: dict | None, n0: int, replicate: int, round_no: int) -> list[CardSpec]
def fresh_tuples(benchmark: str, cls: str, used: set, variants: list, replicate: int, round_no: int, n: int) -> list[CardSpec]
def reallocate(specs: list[CardSpec], multiplier: float) -> list[CardSpec]
def est_cost(spec: CardSpec, views: dict | None, benchmark: str) -> int
def est_verify(k: int, mean_per_attempt: float | None) -> int
def revise_specs(parents: list[tuple[Candidate, VerifyResult]], replicate: int) -> list[CardSpec]

# think/admit.py, think/stop.py, think/stagnation.py, think/tournament.py (control)
def update(pop: list[Candidate], cands: list[Candidate], conf: dict, verified_ids: set, k_pop: int, theta: float) -> list[Candidate]
def p_correct(vtype: str, agreement_value: float, calib: dict | None = None) -> float
def partial_gain(prev_best: float, new_best: float) -> float
def should_reset(stale: int, dup_rate: float, R_max: int, R_stale: int, d_max: float) -> bool
def pick_parents(queue: list[tuple[Candidate, VerifyResult]], conf: dict, hi: float, n: int, replicate: int) -> list[tuple[Candidate, VerifyResult]]

# ledger.py, stats.py, graph.py, measure/pruning_regret.py (memory)
def append(row) -> None                            # LedgerRow or dict
def rows(batch: str | None = None, split: str | None = None) -> list[dict]
def rebuild(batch: str) -> Path                    # stats.py -> memory/views/<batch>/strategy_stats.json
def load_views(batch: str | None) -> dict | None   # stats.py -> {"batch", "strategy_stats": {"rows": [...]}, "calibration"}
def write(run_dir: Path) -> dict                   # graph.py -> graph.jsonl; returns counts
def render(run_dir: Path) -> Path                  # graph.py -> graph.html
def check(run_dir: Path) -> dict                   # graph.py -> {"node_completeness", "edge_completeness",
                                                   #   "cluster_completeness", "cluster_rows_completeness", "ok"}; 0..100
                                                   # expected drops = pred groups + clusters.jsonl "dropped" ids
def current_rows(rows: list[dict]) -> list[dict]  # ledger.py -> rows of the latest run_instance per run_id
def compute(batch: str) -> dict                    # pruning_regret.py

# think.py (driver)
def think(item: dict, *, m: int, replicate: int, backend: str, batch: str, flags: dict | None = None,
          params: dict | None = None, arm: str = "scaffold") -> Answer
# arms/plain.py, arms/best_of_n.py (bench)
def run_arm(arm: str, item: dict, *, m: int, replicate: int, backend: str, batch: str,
            budget_tokens: int | None = None) -> Answer      # arm in {plain, bestofn_vote, bestofn_verify, seeded_bestofn}
```

Each arm and the scaffold write `results/<batch>/runs.jsonl` rows:
`{batch, benchmark, item_id, arm, replicate, run_id, status, answer, spent_tokens, rounds, ts,
budget_tokens, overshoot, run_instance, error}` (`status` is `error` for a crashed or
reply-less run; the arms add `n_calls`). `score.py` joins these with the keys and reports
spend/budget and the error count per arm.

Integration notes: if you need something from another owner's module that is not listed here,
code against the name you need and append a dated note to `harness/INTEGRATION_NOTES.md`
(one section per owner, append-only) so the integrator can reconcile it.
