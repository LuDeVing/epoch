# Generic HTSA: one team of researcher agents, any problem

Goal: the loop in `nano/` must run on any problem that has an objective check. The language-model
problem becomes one *profile*. Nothing in the loop's logic changes; the words in the prompts and the
tester come from the profile. `python -m nano.dry_run` (mock backend, no tokens) must still pass on
the LLM profile with the same stages, and a second, far-away profile (bin packing) must run through the
same loop without code changes.

Status: built (commit c0704c7, 2026-10-17). When this spec was written there was no git repository and
agents edited disjoint files (section 5); the repository now exists and later work uses one branch per agent.
A backup of the package as of 2026-10-17 is in `D:\AGI-lab\backup\nano_2026-10-17`. Which profile key
fills which part of problem.md is in docs/PROFILE.md; section 7 lists what landed after this spec.

Environment: Windows, python `D:\AGI-lab\.venv\Scripts\python.exe`, env `HTSA_LAB_ROOT=D:/AGI-lab`,
run from `C:\Users\User\Desktop\AGI`. Never start real training runs; test with the mock backend.

## 1. Profile: a plain dict, loaded by `nano/profile.py`

A profile module `nano/profiles/<name>.py` exports `PROFILE: dict` with these keys. All strings are
plain English; prompts are built from them.

```python
PROFILE = {
  "name": "llm",
  "goal": "...one paragraph: what is being improved and how success is measured...",
  "aim": "...the purpose behind the goal (problem.md PURPOSE)...",
  "score": {"name": "validation loss", "direction": "lower",      # "lower" or "higher"
            "unit": "nats", "margin": 0.005, "alpha": 0.01, "min_seeds": 3},
  "vocab": {                                   # every word a prompt needs; see the list in section 2
      "artifact": "training script", "artifact_file": "train.py", "language": "python",
      "run": "training run", "score_phrase": "lower validation loss at the fixed budget",
      "parts": "parts of the recipe", "recipe": "recipe",
      "cheap_test": "a 1-minute smoke run comparison, a 3-step timing, a parameter count",
      "cost_axes": "the step time, the parameter count, peak memory",
      "first_check": "the first learning check (45 matched steps)",
      "targets": ["loss on rare tokens", "loss at late positions", "...", "validation loss only"],
      "scope_default": "validation loss at 1024",
      "levers": "optimizer, schedule, init, normalisation, attention pattern, embeddings, data order, loss, precision, systems",
      "known_tricks": "...optional: short text or empty...",
  },
  "constraints": ["C1. ...", "C2. ..."],         # hard constraints shown to every agent
  "assumptions": ["...", "..."],                # design assumptions a transform card may flip
  "tree": [ {node}, ... ],                      # default problem tree, same node schema as nano/tree.py
  "lenses": {"parts": "...", "dataflow": "...", ...},   # at least "parts"
  "boundary_all": "everything except evaluate() and the data loader",
  "artifact": {"path": "nano/train.py",         # the baseline artifact the builders modify (relative to repo root)
               "output_format": "...the builder's reply format (OUTPUT_FORMAT) with the artifact's name filled in...",
               "entry": "python train.py --out OUT ..."},
  "checker": "llm",                             # name of the checker in nano/checks/<name>.py
  "checker_args": {...},                        # passed to the checker's constructor
  "docs": {"digest": "nano/docs/frontier_digest.md", "reference": "nano/docs/modern_architectures.md"},  # optional
  "diagnostics": "nano.diagnose:text",          # optional "module:function" returning measured-behaviour text, or ""
}
```

`nano/profile.py` API (Agent A implements exactly this; Agents B and C code against it):

```python
from nano import profile as PF
PF.current() -> Profile          # the active profile; chosen by --profile NAME (loop) or env HTSA_PROFILE, default "llm"
PF.load(name) -> Profile         # import nano.profiles.<name>, validate required keys, return Profile
PF.set_current(profile)          # used by the loop at start-up and by tests
Profile.name, .goal, .aim, .score, .vocab, .constraints, .assumptions, .tree, .lenses, .boundary_all,
Profile.artifact, .checker, .checker_args, .docs, .diagnostics   # attribute access to the dict keys
Profile.v(key, default="") -> str        # vocab lookup
PF.fill(text) -> str             # replaces {v:key} placeholders in a template with vocab, e.g. "{v:score_phrase}"
Profile.lower_is_better -> bool
```

Templates in ideate/deepen/research/critic_check use `{v:key}` placeholders and are rendered with
`PF.fill(...)` at call time (not at import time), so switching profiles needs no reload.

## 2. Vocabulary keys every prompt may use

artifact, artifact_file, language, run, score_phrase (e.g. "lower validation loss at the fixed budget"),
score_name, parts, recipe, cheap_test, cost_axes, first_check, targets (list), scope_default, levers,
known_tricks, boundary_all. Agents add a key when a prompt needs a word that is not there, and record it
in the LLM profile and in this list.

Added by Agent A (tree.py, loop.py): artifact_short ("script"), artifact_long, goal_short, system,
narrow_examples, planner_hint, reference_what, reference_use, digest_title, digest_use, gain_phrase,
boundary_rules, identity_rule. Each has a fallback when a profile leaves it out.

Added by Agent B (prompt modules; LLM values in nano/ideate.py LLM_DEFAULT_VOCAB, copied into
nano/profiles/llm.py): observables, scope_other, tune_examples, viable, win_short, score_short, leap_rules,
leap_operators (dict), field, probe, weak_points, adapt_moves, separations, cheap_words (list),
cost_questions, full_run, ladder_metrics, sources, size_word, setting_words, setup, delta_name,
same_change_example, problem_brief, measured_numbers; optional tune_knobs, tune_default, controls.

Profile keys beyond section 1 that the loop reads when present: spec_id (run folder id; "gpt2_50m" for llm),
title (problem.md heading), directions and off_map (tree texts), artifact.must_contain (markers a builder's
code must contain), baseline_summary (callable: baseline measurement -> problem.md BASELINE line),
baseline_cache ({"real", "mock"} folder names under runs/), docs.reference_note, score.stackable_margin and
score.stackable_alpha, mode, facts (Mode 3 known facts), judge_model (Mode 3), memory_dir (per-part memory
folder; default `<lab>/memory/<profile>/`).

## 3. Checker protocol: `nano/checks/base.py`

```python
class Checker:
    def __init__(self, profile: Profile, **args): ...
    def baseline_profile(self, baseline: Path, out: Path, seeds) -> dict
        # measures the baseline artifact; returns the dict the loop stores as self.profile (seed curves, noise, costs)
    def check(self, candidate: Path, out: Path, baseline: dict, *, rung_max=3, boundary=None,
              baseline_src=None, lenient=False, audit=True) -> dict
        # the cheap-then-expensive ladder, rung 0..3, stop at the first failure; returns the verify record
    def long_run(self, candidate: Path, out: Path, baseline: dict) -> dict
    def final(self, candidate: Path, out: Path, baseline: dict, seeds) -> dict   # the full test / exam
```

Verify record (unchanged shape, so loop.py and verdict.py keep working):
`{"candidate", "rungs": [...], "status": "checked"|"fail", "rung_reached": int, "partial_score": float,
  "feedback": {...}, "metrics": {...}}`.

Metric semantics, generic: `learn_gap` = candidate score minus baseline score at the matched cheap
check, **signed so that negative means better** (a higher-is-better profile negates). `learn_z` = that gap
in units of the baseline's seed spread. `long_gap`, `long_z`, `extrap_z`, `trend` likewise for the long
check. Cost ratios: `step_ratio`, `param_ratio`, `peak_vram_gb` stay for the LLM checker; a generic
checker fills `cost_ratio` (candidate cost / baseline cost, 1.0 when there is no cost) and may leave the
LLM names absent; loop.py treats absent cost metrics as 1.0.

`nano/checks/llm.py`: the existing `nano/check.py` behind this protocol (thin wrapper; check.py itself
is not rewritten). `nano/checks/script.py`: the generic checker: the profile supplies a scorer command
(`checker_args["scorer"]`, e.g. `python nano/profiles/binpack/scorer.py --candidate X --out OUT --level quick|full --seed S`)
that writes `OUT/metrics.json` with `{"score": float, "cost": {...}, "n": int}`; rung 0 = static boundary
check (reuse nano/boundary.py's denied-import logic), rung 1 = import/build (`--level build`), rung 2 =
quick score vs baseline seeds (`learn_gap`, `learn_z`), rung 3 = full score (`long_gap`, `long_z`). Runs go
through `nano/launch.py` (wall cap, audit hook) like the LLM runs.

## 4. The second profile: bin packing (`nano/profiles/binpack.py` + `nano/profiles/binpack/`)

Problem: an online bin-packing heuristic. The artifact is `baseline.py` defining
`def choose_bin(item: float, bins: list[float], capacity: float) -> int` (index of the bin to put the
item in, or -1 to open a new one; bins holds the current fill of each open bin). Baseline = first fit.
Scorer: generates instances from a seed (uniform item sizes in (0, 1], capacity 1.0; quick = 20
instances x 200 items, full = 100 instances x 1000 items), runs the candidate, and writes
`score` = mean over instances of bins_used / lower_bound (ceil of total size), lower is better; `cost`
= wall time per item. The checker denies the same imports as the LLM profile. Tree: parts = choice
rule, bin state kept, when to open a bin, use of item statistics, tie-breaking; lenses analogous to the
LLM ones but in packing words. This is deliberately far from language models.

## 5. Ownership at the time of the build (no git then: disjoint files, no exceptions)

| Agent | Owns (creates or edits) | Must not touch |
|---|---|---|
| A: profile + tree + loop | `nano/profile.py`, `nano/profiles/__init__.py`, `nano/profiles/llm.py`, `nano/tree.py`, `nano/loop.py`, `nano/dry_run.py` (add `--profile`) | everything else |
| B: prompt modules | `nano/ideate.py`, `nano/deepen.py`, `nano/research.py`, `nano/critic_check.py`, `nano/novelty.py`, `nano/compose.py`, `nano/verdict.py`, `nano/predict.py`, `nano/tune.py`, `nano/controls.py`, `nano/diagnose.py`, `nano/anomaly.py` | loop.py, tree.py, check.py, profile.py |
| C: checkers + second profile | `nano/checks/*`, `nano/profiles/binpack.py`, `nano/profiles/binpack/*` | loop.py, tree.py, check.py, ideate.py |

Agent A also moves these constants out of loop.py/tree.py into `nano/profiles/llm.py`: CONSTRAINTS,
ASSUMPTIONS, OUTPUT_FORMAT, DEFAULT_TREE, LENSES, INWARD/OUTWARD/UPWARD texts, INWARD_FREE/OUTWARD_FREE,
the off-map card texts' LLM words, the problem.md goal text, the digest/reference doc paths, the
baseline path (`nano/train.py`), and the checker choice; loop.py reads them from `PF.current()`.
Agent A keeps every CLI flag and every output file name of loop.py as it is, and adds `--profile`.

Function signatures that other modules call stay identical. Each agent runs
`D:\AGI-lab\.venv\Scripts\python.exe -c "import nano.<module>"` for its files and, where it can,
`python -m nano.dry_run --batch mock-generic-<letter> --implement 2 --rounds 1` (A only, after wiring).
Each agent ends with a report: files changed, new vocab keys, anything left for integration.

## 6. Modes: a baseline is not required

`PROFILE["mode"]` is one of `"baseline"`, `"check_only"`, `"no_check"`. When absent it is derived:
`artifact.path` set and a checker -> baseline; `artifact.path` None and a checker -> check_only; checker
`"panel"` -> no_check.

**Mode 1, baseline** (today): ideas modify the baseline artifact; gaps are measured against it.

**Mode 2, check_only**: there is a scorer but nothing solved yet.
- `artifact = {"path": None, "interface": "<text: the signature or file form a candidate must have>",
  "skeleton": "<optional path to an empty template file>", "output_format": "..."}`.
- Round 1 has no baseline profile. Builders write artifacts from the interface and the skeleton; the
  builder prompt says "write the COMPLETE file that implements <interface>" instead of "the complete
  modified <artifact_file>". Rung 0 is the static import rule only (no diff against a baseline source).
- The reference is the best checked candidate so far: `self.reference = {"cand_id", "path", "metrics"}`.
  Once the first candidate is checked, the checker's `baseline_profile` runs on it so later gaps are
  measured against the best so far. When a later candidate beats the reference by the profile's margin,
  the reference moves; earlier gaps are re-labelled relative to the new reference (re-testing the top
  three is a `--retest-on-reference-change` option, default off).
- Diagnostics, the cost card, the anomaly map and fidelity probes are skipped. problem.md says there
  is no baseline and shows the interface.

**Mode 3, no_check**: a design question, a hypothesis, a plan; no objective score.
- `checker = "panel"`; `nano/checks/panel.py` implements the protocol. A candidate is a written
  proposal (markdown) instead of code: the builder writes it from the idea with four sections:
  the claim, the chain from the facts to the idea, the chain from the idea to the result, weak points,
  and a proposed test. `check()` = blind judging: K judge calls (K from `checker_args`, default 3), each
  scoring 1-10 on the profile's criteria (`checker_args["criteria"]`, a list of short sentences) without
  seeing the other candidates, plus people's opinions from `control.json["opinions"]`
  (`[{"cluster" or "candidate", "score": 1-10, "note", "who"}]`) with a bounded weight
  (`checker_args["people_weight"]`, default 0.25). metrics: `panel_score` (mean), `panel_sd`,
  `learn_gap` = reference score minus candidate score so negative = better, `learn_z` from the judges'
  spread. The reference is the best proposal so far, as in Mode 2.
- The run's output is a ranked list of proposals with their justification, weak points, proposed test and
  the panel's notes (report.json and REPORT.md), not a verified artifact.
- Rung 0 for proposals: a lint that every section is present and that the proposal names at least one
  fact from the tree.

Test profiles: `nano/profiles/binpack_nobase.py` (Mode 2: the binpack scorer, `artifact.path` None,
interface "def choose_bin(item, bins, capacity) -> int", skeleton with the signature and a docstring) and
`nano/profiles/review_process.py` (Mode 3: "design a fair review process for a hackathon", criteria:
fairness, cost in reviewer time, resistance to gaming, clarity). Both must run through
`python -m nano.dry_run --profile <name>` with the mock backend; `nano/dry_run.py`'s mock gains replies
shaped for each (a bin-packing function for Mode 2, a four-section proposal for Mode 3).

## 7. What landed after this spec (2026-10-17)

All of it runs on every profile; each item has a flag and a control arm so its effect is measured, not assumed.

| Item | Built in | Flag (default) / control arm |
|---|---|---|
| Per-part memory, curated by script rules | `nano/memory.py`, loop hooks | on / `--no-memory` |
| One anchored reply round between critic and author | `nano/deepen.py` (`run_dialogue`) | on / `--no-dialogue` |
| The team picks its next question | `nano/pick.py`; questions from `tree.add_failure_question` carry `test`, `threshold`, `fails_if`, `enterable` | on / `--no-pick-questions`; `--focus-contexts 2`, `--max-rounds-focus 2` |
| Fetch on demand (NEED lines) | `nano/research.py` `fetch_fact`, build and revise path | on when the web is on / `--no-fetch-on-demand` |
| Evidence tooling | `harness/noveltybench.py` (IQM, paired bootstrap, rejudge, agreement); `nano/experiments/binpack_arms.py` (pre-registered arms, dry mode) | commands, no loop flag |
| Whole-problem preread before the map | `NanoLoop.preread`, `research.preread_prompt` | on / `--no-preread` (also off with `--no-research`) |
| Seed words by function and distance | `nano/seeds.py` | `--seeds function` / `--seeds random` |
| Pre-mortem knowledge | `deepen.failed_pack` (always); `NanoLoop._premortem_web` | pack on; `--premortem-web` off by default |
| A real tree, depth up to 4 | `nano/tree.py` (`enforce_depth`, `deal_contexts`, `promote_win`, `add_failure_question`) | always |
| Integrity layer | `nano/launch.py` (child process, job object, read allowlist, launcher-side token count), `nano/exam.py` (validation sealed before candidate code, parameters recounted from the weights), `nano/boundary.py`, `nano/audit.py` | always |
| Budget-matched control arms | `nano/loop.py` plain and climb arms: same budget, controls, tuning, canonical rule order | `--arm plain`, `--arm climb`; `--n-builds 0` = spend to the budget |
| e-value verdict with a fixed baseline-only sigma, hedge lane | `nano/verdict.py`, `nano/batch_verify.py`, loop | `--hedge-share 0.12`, `--baseline-seeds 6` |
