# Human Thought Simulation Architecture (HTSA)

Status: draft v0.1, 2026-10-08
Goal: a set of Claude Code skills that orchestrate agents through the same
phases and search dynamics the 2023-2026 research says the human brain uses
to produce new ideas, plus a benchmark harness that measures whether this
beats plain chain-of-thought on novel problems.

Research basis: `reports/How the brain generates new ideas.md` and the five
note files in `research_notes/`.

---

## 1. Design principles (each traces to a finding)

| # | Principle | Finding it comes from |
|---|-----------|------------------------|
| P1 | Generation and evaluation are separate phases run by separate agents. The generator never evaluates. The evaluator never sees the generator's reasoning. | Kenett 2025: brain reconfigures differently for generation vs evaluation. MemiC 4-stage model. |
| P2 | Generation runs in two search modes, persistent (dig deep in one cluster) and flexible (jump across clusters), and the results are merged. | Ovando-Tellez 2025; Nath, Dayan & Stevenson 2024: humans use both, LLMs are biased to one. |
| P3 | The orchestrator switches between free generation and executive control a bounded number of times. Not once, not endlessly. | Chen et al. 2025 (N=2,433): DMN-ECN switch count predicts creativity with an inverted U. |
| P4 | Novelty is filtered by a semantic-distance window, not maximised. Ideas that are too near the obvious or too far to integrate are discarded. | Orwig et al. 2025: creativity ratings rise with cosine distance only up to ~0.9-1.0. |
| P5 | Before generating, the agent lists the default schema (assumptions, conventional uses, fixated cues) and then explicitly suspends it. | He et al. 2025: hippocampal ripples loosen mPFC schema during original ideation. Kutsche 2025: frontal pole suppresses novelty. |
| P6 | Spontaneous thought is simulated as a trajectory: clumps of ~3 related thoughts, then a jump, with concrete detail right after each jump. | Mildner & Tamir 2024; Su et al. 2025. |
| P7 | A strong "this is obviously right" signal triggers verification, never acceptance. | Laukkonen 2023 Eureka heuristic; Grimmer: false insights are inducible and resist warnings. |
| P8 | Incubation is a real phase: park the problem, do unrelated work, return with a fresh agent that does not see the failed attempts. | Liu et al. 2024 meta-analysis d=0.39, strongest when initial cues were misleading. |
| P9 | Analogy sources are deliberately remote and transfer structure, not surface features. | Liu et al. 2026: LLMs benefit from analogy only when the source is very remote. George et al. 2025: relational mindset raises metaphor output. |
| P10 | Diversity comes from different seeds (domains, constraints, random concepts), never from personas. | Huang et al. 2025 NHB: "creative genius" prompts make models worse. Wenger & Kenett: LLMs homogenise. |
| P11 | Every run writes to a memory store that future runs retrieve from, separated into semantic (abstractions) and episodic (what happened). | MemiC; Thakral 2026: semantic scaffold explains 36% of divergent-thinking variance. |
| P12 | Everything is measured against a baseline with ablations. | Every prior creativity-architecture paper reports gains against weak baselines. |

---

## 2. System overview

```
                 +------------------------------------------+
                 |  /think  (orchestrator skill)            |
                 |  owns the phase schedule, switch budget, |
                 |  and the workspace (blackboard)          |
                 +-------+----------------------------------+
                         |
   +---------+-----------+-----------+------------+-----------+
   v         v           v           v            v           v
/encode   /forage     /wander    /analogize  /restructure  /incubate
(problem  (generate,  (spont.    (remote     (re-encode    (park, do
 map +    2 modes,    thought    structure   the problem)  unrelated
 schema)  parallel)   walk)      transfer)                 work, return)
                         |
                         v
               +------------------+     +------------------+
               | /evaluate        | --> | /insight-check   |
               | (fresh agent,    |     | (aha guard:      |
               |  distance window,|     |  verify, never   |
               |  integration,    |     |  accept)         |
               |  effectiveness)  |     +--------+---------+
               +------------------+              |
                                                 v
                                        +------------------+
                                        | /consolidate     |
                                        | (write semantic +|
                                        |  episodic memory)|
                                        +------------------+
```

Workspace (the "global workspace" / working memory), one folder per run:

```
runs/<run-id>/
  problem.md        # output of /encode: goal, constraints, resources, schema list
  trajectory.md     # output of /wander: the thought walk
  ideas.jsonl       # output of /forage and /analogize: one idea per line
  evaluations.jsonl # output of /evaluate: scores per idea
  insight.log       # output of /insight-check: what was verified and how
  state.json        # orchestrator state: phase, switch count, budget
memory/
  semantic/         # abstractions, reusable framings, analogy maps
  episodic/         # per-run logs: what worked, what failed, why
```

---

## 3. The skills

Each skill is a `SKILL.md` under `.claude/skills/<name>/`. The orchestrator
invokes them in sequence and spawns subagents where the skill says so.

### /encode  (problem representation)
Input: the raw problem.
Steps:
1. Restate the goal in one sentence. List hard constraints and available resources.
2. Write the **default schema**: the obvious approach, the conventional use of every resource, the assumptions an expert would make without noticing. This is the list P5 will suspend.
3. Mark **fixated cues**: any element of the problem statement that suggests a specific solution path.
4. Retrieve from `memory/semantic/` any framings that matched similar problems.
Output: `problem.md`.
Mechanism simulated: prefrontal schema activation, so it can be loosened later.

### /forage  (idea generation, two modes)
Runs as parallel subagents. Each gets `problem.md`, a **seed**, and a **mode**.
- Seed: a domain (e.g. "marine biology", "medieval logistics") or a random concept, drawn from a seed list. Never a persona.
- Mode `persistent`: stay in one cluster, produce 6-8 ideas that go deeper into it before moving on. (Ovando-Tellez: slow clustering predicts originality.)
- Mode `flexible`: produce 1-2 ideas per cluster across 6-8 clusters. (Fast switching predicts remote combination.)
Rules: generation only. No scoring, no "but this wouldn't work". The schema from `problem.md` is explicitly off-limits as a source of ideas in the first half of the output.
Output: appended to `ideas.jsonl` with `{id, text, mode, seed, cluster}`.
Default fan-out: 2 persistent + 2 flexible agents, 4 seeds. Tunable.

### /wander  (spontaneous thought simulation)
A single agent runs a thought walk of 12-15 steps starting from the problem or from an unrelated seed (incubation use).
Trajectory rules (P6):
- Stay on a topic for ~3 thoughts, then jump to a semantically distant topic.
- The first thought after a jump is concrete and specific (an image, a memory, an example). Subsequent thoughts in the clump abstract from it.
- One recurring "concern" (the problem's goal) acts as an attractor: roughly every third jump returns toward it.
- A constraint level 0-3 set by the orchestrator controls jump distance (the entropy knob from Hills & Kenett).
At the end, the agent marks any step that unexpectedly touches the problem as a **serendipity candidate** and writes it to `ideas.jsonl`.
Output: `trajectory.md`.

### /analogize  (remote structure transfer)
1. Build the relational structure of the problem: what acts on what, what is conserved, what is the bottleneck.
2. Retrieve 3 source domains that share the structure but are maximally far in surface content (P9).
3. For each, map the structure explicitly (source role -> target role), then transfer the source's known solution.
Output: ideas appended to `ideas.jsonl` with `{mode: "analogy", source_domain, mapping}`.

### /evaluate  (executive control phase)
A fresh subagent that receives only `problem.md` and `ideas.jsonl`, not any generator reasoning (P1).
Scores each idea on:
- **Distance**: cosine distance from the default-schema solutions, computed with an embedding model. Keep ideas inside the window [0.5, 1.0]; flag below 0.5 as "obvious", above 1.0 as "unintegrated" (P4). Thresholds are tunable and will be calibrated on the benchmark.
- **Integration**: does the idea actually connect to the constraints and resources, or is it just remote?
- **Effectiveness**: would it solve the problem if it worked?
- **Testability**: can it be verified with a concrete check?
Output: `evaluations.jsonl`, plus a ranked shortlist and a verdict: `solved`, `promising`, or `impasse`.

### /insight-check  (the aha guard)
Triggered for any idea the evaluator rates with high confidence and that arrived suddenly (an idea that none of the preceding ideas in its cluster led to).
1. Log the confidence and the suddenness.
2. Verification, mandatory: run the idea against a concrete test, a counterexample search, or a simulation. Never accept on the feeling (P7).
3. Record outcome as `true insight` or `false insight`. The false-insight rate is a tracked metric.
Output: `insight.log`.

### /restructure  (representational change)
Called on `impasse` or when the shortlist is all "obvious".
1. Reread `problem.md`. Drop the fixated cues. Rewrite the goal in a different vocabulary (e.g. physical -> social -> informational).
2. Propose 3 alternative problem framings. The orchestrator picks one and overwrites `problem.md` with it (the old one is kept as `problem.v1.md`).
Impasse is not required for this to run (Ross & Arfini 2024), so the orchestrator may call it proactively once per run.

### /incubate  (break and fresh return)
1. Save state. Run `/wander` from an unrelated seed with constraint level 0 for 15 steps, or run a genuinely unrelated task if one is queued.
2. Return by spawning a **fresh** generator that receives the restructured `problem.md` and the serendipity candidates only. It does not receive the earlier failed ideas (P8: incubation works best when misleading cues are dropped).

### /consolidate  (memory write)
At the end of every run:
- `memory/episodic/<run-id>.md`: the problem, the path taken, what solved it, what was a false insight.
- `memory/semantic/`: any reusable framing or analogy mapping, written as a one-paragraph abstraction with no run-specific detail (P11).
Retrieval: `/encode` searches semantic memory by embedding similarity; episodic is searched only when the semantic hit points to it.

### /think  (orchestrator)
The controller. Holds the **switch budget** (default 4, inverted U per P3) and runs this schedule:

```
encode
loop (until solved, or switch budget exhausted):
    forage (parallel, both modes)  +  analogize        # generation
    evaluate                                            # control
    if verdict == solved:    insight-check -> consolidate -> stop
    if verdict == promising: forage again, seeded from shortlist
    if verdict == impasse:   restructure -> incubate, then loop
consolidate (even on failure)
```

Each pass through the loop is one DMN-ECN switch. The orchestrator also sets
the `/wander` constraint level: high (2-3) early, low (0-1) during incubation.

---

## 4. Measurement harness (built before the skills are tuned)

Benchmarks:
- **MacGyver** (unconventional tool use, functional-fixedness heavy).
- **BRAINTEASER** (lateral-thinking puzzles).
- **Custom set** of 30 open-ended design problems with rubric scoring, so we are not only measuring puzzle-solving.

Conditions:
- Baseline: plain chain-of-thought, same model, same token budget.
- Full HTSA.
- Ablations: HTSA minus one skill at a time (minus forage-persistent, minus forage-flexible, minus wander, minus analogize, minus incubate, minus insight-check, minus distance window).

Metrics:
- Solve rate / rubric score.
- Novelty: mean embedding distance of HTSA answers from baseline answers.
- Diversity: pairwise distance across 10 runs of the same problem (homogenisation check, P10).
- False-insight rate from `insight.log`.
- Cost: tokens and wall-clock per problem.

Decision rule: a skill stays in the architecture only if its ablation shows a measurable drop. Faithfulness to the brain is the hypothesis, not the goal.

---

## 5. Build order

1. Workspace layout and `/think` with a trivial schedule (encode -> forage -> evaluate -> consolidate).
2. Benchmark harness and baseline numbers. Nothing else until this exists.
3. `/forage` two modes, `/evaluate` with the distance window. First ablation.
4. `/wander`, `/incubate`, `/restructure`.
5. `/analogize`, `/insight-check`.
6. Memory (`/consolidate` and retrieval in `/encode`).
7. Tune switch budget and distance thresholds on the benchmark.

---

## 6. Known limits and open questions

- Skills shape the model's trajectory through what it already knows. They do not add capacity. The target is better novel problem solving and less homogenised output, not general intelligence.
- Claude Code does not expose sampling temperature. The entropy knob is implemented through prompt constraint level and seeds, which is an approximation.
- The distance window numbers (0.9-1.0 in the human data) were measured on human raters and specific tasks. The thresholds here are starting points to calibrate, not facts.
- Hippocampal ripple and locus-coeruleus findings are mechanism-level and only loosely inspire P5 and the jump rule in P6. We are borrowing the behavioural signature, not the biology.
- Open: whether a "real" unrelated task during incubation does anything a fresh context window does not. The ablation will tell us.
