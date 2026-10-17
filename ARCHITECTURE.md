# Human Thought Simulation Architecture (HTSA)

Status: v0.3, 2026-10-10, revised after the review of the six owner ideas I1-I6 (`IDEAS.md`) and the project lead's decisions on them. Supersedes v0.2 of 2026-10-10, which is preserved unchanged at `ARCHITECTURE_v0.2.md`; v0.1 of 2026-10-08 is preserved unchanged at `ARCHITECTURE_v0.1.md`.
Goal: a set of Claude Code skills that execute explicit, externally controlled thinking procedures over isolated, sandboxed subagent calls driven by a python controller, verify every candidate with an external check, learn from an append-only ledger which procedures work on which kinds of problems, and a harness that tests whether this beats best-of-N sampling at a defined, matched token cost.

Research basis: `reports/` (rounds 1 and 2), `research_notes/` (14 note files in two folders), `research_notes/mechanism_catalog.md` (137 catalog entries, cited below by id), `SYNTHESIS.md` (v0.3 decision tables including the Owner proposals (v0.3) table, design notes, and the appendix of objections and resolutions), `EXPERIMENT_PLAN.md` (nano-replica testbed), `IDEAS.md` (the six owner ideas I1-I6 with verdicts, metrics, ablations, costs and risks; cited below by I-id, which are owner-idea ids, not catalog ids). Where a catalog id is cited for an engineering choice, SYNTHESIS.md states whether the id is evidence or motivation.

---

## 0. Thesis

Claim under test. Humans can decide how to think: they choose a procedure for approaching a problem, notice when it fails, switch, decide when to stop, and pass methods on to others. Current LLMs hold vast knowledge but their thinking is text generation inside one context, with strategy control baked in by training and not steerable from outside. The strongest current systems, as far as public descriptions go (this claim is unsourced in the research basis), amount to generating many candidates and selecting with a verifier. The bet is that explicit, externally controlled thinking procedures, plus a memory of which procedures worked on which kinds of problems, are the missing link, and that they beat an equal budget of unguided sampling.

Caveat the design respects. Humans control the conditions of thought (representation, attention, breaks, tests), not the ideas themselves. People have little insight into the quality of their own ideas (self-assessment vs rated performance r about 0.1 to 0.3 on the Alternate Uses task, EVL-03; the task is named in the source note, not the catalog row, see SYNTHESIS.md Unifying picture item 5), and judging others' ideas is better but often near chance at selection (EVL-04). So the architecture controls procedures and tests, verifies rather than trusts, and never lets a confidence signal accept a candidate.

Design hypothesis. Procedures executed structurally (separate sandboxed contexts, routed files, scripts, verifiers, ledger) beat the same procedures described in a prompt. No catalog entry supports or refutes this; OTH-02 supports only "no dedicated creativity prompt". The hypothesis is tested by the described-strategies ladder (section 8).

Prediction. At matched token cost (defined in section 8), the scaffold produces a higher ground-truth solve rate than the stronger of two best-of-N nulls that use the same verifier for selection, and on fixed held-out items the solve rate rises with the size of the frozen strategy-memory snapshot built from the train split.

Falsification. H0: scaffold solve rate <= the stronger best-of-N null at matched cost, on the test split of the keyed Stage 3 benchmarks, over 5-10 replicates, with a cluster bootstrap over items. If the 95% CI of the paired difference includes 0, the thesis is not supported at this scale. Secondary nulls: the scaffold does no better than rung L1 of the described-strategies ladder (structure vs instruction), and solve rate does not rise with memory snapshot size against an empty-memory arm (memory vs no memory).

## Targets and staging

| Stage | Deliverable | Go/no-go gate |
|---|---|---|
| 1 | SYNTHESIS.md v0.2 (now v0.3), this design, `harness/plan.md` preregistration draft | Every adopted component has an operational definition, a flag, a null and an ablation with a slot in the ablation schedule (section 8), or is marked exempt there |
| 2 | Scaffold P0, python driver, harness with arms: plain, best-of-N (vote), best-of-N (same verifier), seeded best-of-N (same verifier), instruction-only, scaffold, ladder rung L1 | Harness runs all arms at matched cost on dev; headroom pilot done; judge validated against dev ground truth; lint and return contract pass |
| 3 | Keyed benchmarks (ARC-style, BRAINTEASER after headroom check) with per-card ablations, family-interleaved train sequences and memory snapshots; MacGyver as secondary on a human-labelled subset | Scaffold beats the stronger best-of-N null at matched cost, CI excluding 0 on test, outside replicate noise |
| 4 | Nano-scale rediscovery of known NanoGPT speedrun code changes via /experiment, with and without hints, on the local GPU | Validation-loss improvement of rediscovered diffs at a fixed 100M-token budget, measured against the project's own plain-agent and best-of-N-agent baselines at matched LLM tokens; population search with recombination working |
| 5 | Improve nano-scale replicas of DeepSeek-V4.1 and MiMo-V2.6 (`research_notes/architectures/nano_specs.md`) where training runs are the verifier | A breakthrough = a verified improvement under the anytime-valid e-value verdict (docs/VERDICT.md, `nano/verdict.py`: e-value >= 1/alpha = 100 for a 0.005-nat margin over >= 3 paired seeds, noise fixed from the baseline runs alone, e-BH across the night's candidates) whose diff survives one step of scaling. The earlier "> 2 seed SD over 3+ seeds, 5 for close calls" rule is retired: adding seeds on the results so far is optional stopping (research_notes/idea_generation/00_SYNTHESIS.md X3, 11_decision_science.md M3) |

Stage 4 is restated from the pre-review draft: the published speedrun records are wall-clock records on 8xH100 and cannot be reproduced on an RTX 4050 with 6 GB, so the target is the code change, not the record.

Priority definitions. P0: required to run the Stage 3 go/no-go. P1: built during Stage 3 as flagged additions, required before Stage 4. P2: after the Stage 3 gate. Deferred: returns only as a flagged arm with a prior of no effect. Rejected: not built. "Placeholder" marks a numeric default with no source, tuned on dev-tune.

---

## 1. Design principles

Each principle traces to catalog ids; SYNTHESIS.md says whether the id is evidence or motivation. Principles are labelled Pr1-Pr19 so they cannot be read as the priority labels P0-P2. v0.1 principles that survive keep their number (P1 in v0.1 is Pr1 here); dropped ones are listed in the changelog.

| # | Principle | Catalog ids |
|---|---|---|
| Pr1 | One role per call. Generators never judge or verify; judges and verifiers never propose. Roles are enforced by per-role tool allowlists and sandboxed inputs, and change only by spawning a fresh call. | CTL-01, STA-01 (loose-generation half only; 2x2 in the section 8 schedule), EVL-03, GEN-09 |
| Pr3 | Rounds are bounded by a hard cap and an explicit stop rule computed by script; stopping is tied to verification type and agreement, never to judge confidence. | CTL-04; CTL-05 as motivation only (CTL-05 is a human stop on a declining confidence threshold; here the threshold is on verification type and agreement, and agreement is itself a confidence proxy, so this principle does not follow from CTL-05) |
| Pr5 | Default answers are elicited by a separate call into a private file and withheld from every generator; they are used downstream by script to route near-default candidates to a prime-check falsifier. The low_prior view carries no domain cues (script-linted). | GEN-03, REP-02 |
| Pr7 | A strong judge probability triggers earlier verification and more diverse counterexample attempts. It never accepts, never enters the stop rule, and never chooses among verified candidates. | EVL-01 (felt certainty is no evidence of correctness). CTL-06 is not a basis: there a LOW feeling of rightness triggers deliberation, the opposite cue |
| Pr8 | Default on stagnation: reset into a fresh call that never saw the failed candidates, with an unused (card, operator, seed, permutation) tuple and masked evidence. Same-context extension is an ablation arm, reported separately for ARC-style items where deliberation may correct. | CTL-11, CTL-14, CTL-02, CTL-18 |
| Pr9 | Analogy transfers structure through code re-encoding or a script-checked typed-triple mapping; sources come from a fixed domain corpus by goal-text similarity, as a mix of near and far analogues. "Farther is better" is not monotonic: far sources raise novelty and variance, not the mean (research_notes/idea_generation/02_analogy.md bottom line 2), and working labs use near-domain analogies (GEN-08). | GEN-08, REP-15 |
| Pr10 | Diversity comes from inputs (card, seed, fact order, transformed problem, retrieved-document pack), never from personas or creativity instructions; each lever is measured against a permutation null and kept only if it raises coverage at equal quality. A lint on templates and rendered prompts enforces the ban. Lint rule (I5 part D): templates and design text must not use "subconscious", "free-associate" or hidden-reasoning framing ("reveal your hidden reasoning", "what you really think"); candidates that appear in a generator's thinking summary or scratch text but not in its numbered list are called unspoken candidates, and they are new samples, never readouts. | GEN-11, SOC-02, SOC-07, REP-08 |
| Pr11 | Memory is an append-only ledger written only by the driver; all views are script-derived and versioned per batch; no LLM writes memory text before P2; only verified outcomes update statistics; memory is credited only on held-out items against frozen snapshots. | MEM-11, MEM-16, EVL-10, MSR-11 |
| Pr12 | Everything is measured at a defined matched cost against active controls with a preregistered keep/drop rule, coverage and selection decomposed, cluster bootstrap over items. | MSR-02, MSR-05, MSR-18 |
| Pr13 | Structural over instructional, as a hypothesis: a procedure is a card the driver executes as sandboxed calls with routed inputs from fixed templates; a prompt that describes the procedure is a ladder rung, not a component. | project hypothesis; OTH-02 for "no creativity prompt" only; GEN-17 |
| Pr14 | An absolute solve bar (checklist conjunction plus required verification type per item class) is written before generation and checked by script; the run may abstain. Nothing is returned as solved without clearing it. Answer keys and held-out test outputs never enter the loop; the harness alone scores against them. | EVL-15, CTL-05 |
| Pr15 | "Verified" requires an external artifact: executed code, solver, exact demo match, or a sourced fact. A same-model falsifier that finds no counterexample, or a three-context consensus on a premise, makes a candidate "checked", logged in its own stratum, never "verified"; checked candidates enter the stop rule only behind `flags.llm_falsifier_validated`, with their own threshold T_checked. Narrated simulation is not a type. | EVL-02, EVL-11, REP-03 |
| Pr16 | Strategies are allocated by verified pass per token, learned from the train split per problem class with an exploration floor and one memory-blind call whose card is uniform random. | CTL-07, CTL-08; MEM-17 as motivation (a contested bibliometric trend; agent analogy only) |
| Pr17 | The P0 confidence signal is agreement from a fixed seeded probe; judge probabilities are logged and enter calibration only after dev validation; calibration is reported per defined difficulty bin with minimum cell sizes. | EVL-08, MSR-04 (standard practice) |
| Pr18 | Ideas are built on: a fresh child gets one parent artifact (two for P1 operators) plus a deterministic verifier record and applies one named operator. Parents are chosen by a script tournament on verifier scores, as a guard against self-preference; chosen-vs-assigned parent is an ablation. | GEN-14, EVL-03; STA-04 and SOC-05 as motivation (STA-04's agent rule is an analogy) |
| Pr19 | No component is justified by brain fidelity. Each has an operational definition, a flag and an ablation; numeric defaults with no source are placeholders. | MSR-18 |

---

## 2. System overview

```
   +--------------------------------------------------------------------------+
   |  harness/think.py  (the orchestrator, python)                            |
   |  steps: allocate | dedup | admit | stop | stagnation                     |
   |  reads runs/<id>/*.jsonl + state.json, writes next action + signal       |
   |  checks budget before every spawn; appends ledger rows after returns     |
   |  dedup appends clusters.jsonl; after every cycle graph.py -> graph.jsonl |
   |  (0 tokens, never routed to any call); P1 hooks: lemma pool, frontier,   |
   |  harvest of unspoken candidates, all behind flags                        |
   +------------------------------------+-------------------------------------+
                                        |
                                        v
   +--------------------------------------------------------------------------+
   |  harness/run_card.py  (card executor)                                    |
   |  renders fixed templates with routed files -> runs/<id>/prompts/        |
   |  copies only allowed inputs to runs/<id>/calls/<call>/in/               |
   |  claude -p --output-format json, fresh session, cwd = sandbox,          |
   |  per-role tool allowlist; return contract {id, path, n_cands}           |
   +----+-------------+--------------+--------------+--------------+----------+
        |             |              |              |              |
        v             v              v              v              v
    /encode      /generate        /judge        /verify     /restructure (P1)
   problem.md,  one card per    blind, fresh,  validated     script-computed
   checklist    sandboxed call; pointwise or   model exec,   dropped elements,
   (2 calls     P0: seeded,     <=5 batch x2   demo + pert.  relabel, transform;
   merged),     low_prior,      shuffles;      checks,       fresh variants
   bar, private transform(3),   p_raw logged   checklist,
   defaults,    formal, revise  only           diverse
   verifier     P1: analogy,                   falsifier
   model (hash) relabel,                       attempts;
                compose,                       types split
                decompose,
                lemma, gap_pack
                                        |
                                        v
   +--------------------------------------------------------------------------+
   |  /ledger (P0) + /consolidate (offline)                                   |
   |  append-only rows; harness/stats.py rebuilds versioned views:           |
   |  memory/views/<batch>/{strategy_stats, calibration, traps, seed_counts} |
   +--------------------------------------------------------------------------+
                                        |
                                        v
   +--------------------------------------------------------------------------+
   |  /experiment (Stage 4-5): edit, run, parse, seed protocol, diff ledger,  |
   |  islands + tournament (harness/think/tournament.py), hunk contributions  |
   +--------------------------------------------------------------------------+

   /bench (harness, built first): cost definition, splits, replicates, lint,
   headroom pilot, judge validation, arms incl. ladder, coverage/selection
   decomposition, ablation flags, snapshot memory arms; offline diagnostics
   at 0 tokens: graph.py --check, measure/pruning_regret.py (late-winner and
   correct-but-pruned rates), harvest.py unspoken_correct_rate.
```

Workspace layout (one folder per run, plus cross-run memory):

```
runs/<run-id>/
  problem.md               # /encode: goal, numbered self-contained facts, numbered
                           #   resources, merged hard-constraint checklist, solve bar
  constraints.json         # checklist as data; per-item required verification type
  private/defaults.json    # /encode: 5 default answers; never copied into any sandbox
  verifier/problem_model.py# /encode: validated executable model; sha256 in state.json;
                           #   read-only to every generator
  signature.json           # /encode (P1): enum-schema signature; class key
  components.json          # /encode (P1): physical-property table, no uses
  dropped.json             # script after round 1: elements no candidate referenced
  variants/<call>.md       # shuffled, low_prior (linted), relabelled, transformed views
  calls/<call-id>/in/      # sandbox: only the files this call may read
  calls/<call-id>/out.jsonl# full output; return contract carries only the path
  calls/<call-id>/thinking.txt  # P1 (flags.harvest_unspoken, I5): summarized thinking of a
                           #   generator call; private, never copied into any sandbox
  prompts/<call-id>.txt    # every rendered prompt (linted after the batch)
  cands/<call>.jsonl       # {id, text, testable_claim, card, operator, seed, perm,
                           #   parent_ids, island_id, lineage_id, origin (spoken|unspoken|
                           #   probe|default), decomp_id (I2), pack_id, gap_ids (I6)}
  cands/<call>.unspoken.jsonl   # P1 (I5): harvested unspoken candidates {id, text,
                           #   origin: unspoken, source_call, span_hash}; diagnostic at P1
  graph.jsonl              # P0 (I3): harness/graph.py after every cycle, 0 tokens: nodes
                           #   {cand_id, card, operator, round, island_id, lineage_id,
                           #   root_ids, status, vtype, cluster_id, matches_default},
                           #   edges {src, dst, kind: parent_of|same_cluster|covers_constraint}
                           #   and per-cluster rows {cluster_id, n_members, n_independent_roots,
                           #   n_independent_nonseeded} derived from clusters.jsonl;
                           #   never copied into any sandbox
  clusters.jsonl           # P0 (I3): dedup membership {cluster_id, rule, members[cand_id],
                           #   representative_id, round}, appended by think.py at the dedup
                           #   step (its only writer); root counts live in graph.jsonl
  graph.html               # P0 (I3): graph.py --render output, owner view only;
                           #   never copied into any sandbox
  lemmas.jsonl             # P1 (flags.lemmas, I1): {id, claim, predicate_path, scope,
                           #   status, vtype, discrim, implied_by, source_call, parent_ids}
  decomp/<call>/           # P1 (flags.card_decompose, I2): plan.json, parts/<part_id>.jsonl,
                           #   combos.jsonl {combo_id, part_cand_ids, part_test_pass, status}
  frontier.jsonl           # P1 (flags.frontier, I4): {epoch, round, particle_id, lineage_id,
                           #   cand_id, parent_particle_id, partial_score, log_weight, weight,
                           #   ess, resample_seed, alive}; verifier scores only
  gaps.json                # P1 (flags.gap_pack, I6): {round, uncovered_constraint_ids,
                           #   dropped_ids, query_text}, script-built from /verify coverage
  private/prior_map.json   # P2 (flags.prior_map, I5): {cluster_id, count, sources,
                           #   exemplar_hash} from plain samples + probe; replaces
                           #   defaults.json only after the 90% routing-agreement check
  judgments.jsonl          # {id, rubric, p_raw, perm_a, perm_b}
  verify.jsonl             # {id, status: verified|checked|fail|unverified,
                           #   verification_type, attempts, surprise, repr_change_event,
                           #   feedback_record}
  evidence.jsonl           # {source, about, observation}; candidate spans masked by script
  surprises.jsonl          # high confidence then fail
  state.json               # decision log: one row per cycle {step, action, signal, spent,
                           #   round, T, pop, verifier_hash, snapshot_hash}; run header carries
                           #   backend (cli_json | messages_api), a per-batch setting
  answer.json              # answer or abstention; status; verification type; best guess
memory/
  ledger.jsonl             # append-only, written only by the driver
  views/<batch>/           # versioned derived views (never overwritten in place)
    strategy_stats.json    #   Beta(pass) and mean tokens per (class, card, round-type)
    calibration.json       #   P(correct | agreement[, p_raw], vtype) per stratum
    traps.jsonl            #   script-built high-confidence failures
    seed_counts.json       #   (P2)
  strategies/<card>.yaml   # versioned executable procedures against schema.json
  strategies/schema.json   # steps[{id, template, inputs[], model, max_tokens, n, parser,
                           #   foreach (P1, I2: a parsed list the step fans out over)}]
  strategies/templates/<card>.<step>.txt
  domains.jsonl            # fixed corpus of about 200 domain descriptions + embeddings
  domain_packs.jsonl       # P1 (I6): about 50 field packs {field_id, text <= 1.5k tokens,
                           #   third person: methods, standard components, failure modes,
                           #   typical constraints; source_urls, embedding, corpus_hash};
                           #   linted against role and identity phrasing
  seeds/concepts.txt       # fixed seed word list
  seeds/docs.jsonl         # P1 (SOC-02): fixed corpus of retrieved documents; a pack of
                           #   2-3 documents chosen by script is a seed type, ids logged
  cases/<id>.json          # P1: script-built bundle (goal, card, operator, candidate,
                           #   verifier command and output, run link), <= 800 tokens
  experiments/ledger.jsonl # Stage 4-5: every diff with hypothesis, lineage, island,
                           #   hunks and contributions, seed stats, verdict
data/                      # benchmark item files; never copied into any sandbox
  arc_agi1_eval_le600.jsonl#   the 40-item ARC-AGI-1 evaluation subset (<= 600 cells): train
                           #   pairs are routed, test outputs are read by the harness scorer only
  brainteaser_sp.jsonl     #   BRAINTEASER SP items; the key field is read by the scorer only
harness/
  plan.md                  # preregistration: cost definition, arms, metrics, splits,
                           #   item counts, power, keep/drop rule, batch schedule
  think.py, run_card.py, stats.py, feedback.py, embed.py, lint.py
  arc_exec.py              # P0: runs candidate programs transform(grid) -> grid on train pairs
                           #   (demo_match) and on the test input (predicted grid for dedup, probe
                           #   agreement and harness scoring); used by every arm on ARC
  graph.py                 # P0 (I3): --write after each cycle, --render (HTML), --check (CI);
                           #   flags.graph default on, exempt diagnostic
  think/{allocate,dedup,admit,stop,stagnation,tournament}.py
  think/frontier.py        # P1 (I4, flags.frontier): tournament | beam_topK | smc resampler
  harvest.py               # P1 (I5): thinking.txt -> cands/<call>.unspoken.jsonl
  lemma_check.py           # P1 (I1): proves lemmas by execution, permutation null, implication
  compose_parts.py         # P1 (I2): assembles part candidates into whole candidates, 0 tokens
  measure/pruning_regret.py# P0 (I4): late-winner and correct-but-pruned rates, offline, keyed items;
                           #   flags.pruning_regret default on, exempt diagnostic
  arms/{described.py, menu_from_cards.py}
  metrics/originality.py
  lint_patterns.yaml, cues/, regression/ (30 fixed dev items)
  results/<batch>/{*.jsonl, cost.jsonl}
```

Storage note (EXPERIMENT_PLAN section 2, measured 2026-10-10): C: has 3.2 GB free, so `runs/`, `memory/ledger.jsonl`, `harness/results/` and the benchmark item files under `data/` live under `D:\AGI-lab\`, with only code and docs on C:. The paths above are relative to that lab root; the code tree resolves them through one configured root, never by absolute path in a template.

---

## 3. The skills

Each skill is a `SKILL.md` under `.claude/skills/<name>/` that launches the corresponding python entry point and summarizes its output; no SKILL.md contains control logic. Generator templates are loose (no checklists, no evaluative language); judge and verify templates are tight (rubric, tests, no proposals). Role tool access is not set by agent definition files: there is no `.claude/agents/` directory. Every harness role runs with no tools (`harness/llm.py`: the CLI backend passes `--tools ""` and `--max-turns 1`; the API backend has no tools), and the runner, not the model, executes candidate programs. The only exceptions are explicit: the nano research role gets WebSearch and WebFetch, and `HTSA_PLAIN_TOOLS` can give the plain arm tools for an experiment. The lint runs over templates before every batch and over rendered prompts after it.

### /bench (harness) [P0, built first]
Input: benchmark items with train, dev-tune, dev-ablate, test, transfer and OOD splits; `harness/plan.md`; arm and flag configs; cost multiplier m.
Steps:
1. Measure the plain chain-of-thought token cost per item on dev; set B = m x median CoT tokens (m in {5, 10, 20, 40}; 20 primary). Cost = input plus output tokens of every model call including system-prompt overhead, cached input at full price, encode tokens, and offline tokens amortized per item; read per call from the CLI JSON usage into `results/<batch>/cost.jsonl`. plan.md also defines the estimators the driver checks before each spawn and verification, est_cost and est_verify (section 5). Best-of-N arms stop at the scaffold's realized spend per item (MSR-02).
2. Headroom pilot: run the plain arm on dev; keep items with accuracy between 20% and 80%; substitute BRAINTEASER reconstruction variants or fresh paraphrases and ARC-AGI-2 public eval items as needed; report chance level; fix the item set and the power calculation in plan.md before any other arm runs.
3. Lint templates (blocking) and rendered prompts (logged): personas and stakes phrasing fail; be-creative wording warns; bodily-state imperatives directed at the agent fail; "subconscious", "free-associate" and hidden-reasoning wording fail (I5 part D; these also avoid reasoning_extraction refusals); `memory/domain_packs.jsonl` rows are linted against role and identity phrasing (I6); MacGyver allowlist must pass (GEN-11, STA-02, OTH-01). In the first dev batch, run the pressure-wrapper arm (neutral vs high-pressure wrapper, same items and seeds, paired, two-sided) that tests the stakes rule (STA-02).
4. Validate /judge on dev-tune ground truth: AUROC, Brier, adaptive-bin ECE with CIs; self-preference probe (human reference vs model solutions); length-invariance probe on un-normalized inputs; block the batch if selection accuracy is near chance (EVL-08, MSR-04).
5. Run the arms at matched cost: plain; best-of-N (majority vote); best-of-N with the same /verify; seeded best-of-N with the same /verify (random seeds and permutations, no cards); instruction-only (seeded plus one fixed broadening line); scaffold; ladder L1 (N contexts with the menu); from P1: ladder L0 and L2, per-card generic-instruction substitution, memory snapshot arms at 0/100/300/600 train rows and empty memory (GEN-17, OTH-02, MSR-11).
6. Sweep m for the scaffold and the primary null only; sweep R_max for the scaffold at the largest m only, logging termination cause (CTL-03, CTL-04).
7. Score: ground-truth solve rate on keyed benchmarks, paired against the stronger null, cluster bootstrap over items with replicates averaged within item; coverage (oracle pass@pool, keyed benchmarks) and selection accuracy; pass@k from replicates; first-answer (round-0 top candidate) to final transition matrix against a two-replicate churn null (MSR-07); accuracy-coverage curve with abstentions scored apart (CTL-05); calibration per defined difficulty bin (MSR-04); diversity on candidate pools with four measures against a permutation null (MSR-14, SOC-07); role-leakage rate, return-contract violations, routing-invariant violations, decision-log completeness, verifier hash mismatches (all must be 0); graph completeness from `harness/graph.py --check` (100% of cands rows as nodes, 100% of parent_ids as edges, every dedup drop in a cluster row; I3); pruning regret from `harness/measure/pruning_regret.py` on keyed items, offline, never fed back (late-winner rate, correct-but-pruned rate split by cause; I4); unspoken_correct_rate and unverified_correct_rate from `harness/harvest.py` output scored offline with the key (P1, I5).
8. Ablations on dev-ablate at 1x, R_max fixed, 3 replicates: leave-one-out per P0 card and the 4 pre-gate flags named in the ablation schedule (section 8) before the gate, every other ablation at the slot the schedule gives it, removed share reallocated proportionally, seeded never ablated; pairs as base+A+B vs base+A and base+B; keep/drop by Beta(1,1) on discordant pairs, P(helps) > 0.95, fixed batch count, accumulated only within one memory and calibration snapshot (MSR-12, MSR-18).
Output: `harness/results/<batch>/*.jsonl`, `cost.jsonl`, report with CIs, calibration tables, ablation table, realized spend beside the cap.
Mechanisms: MSR-01, MSR-02, MSR-04, MSR-05, MSR-07, MSR-11, MSR-12, MSR-13, MSR-14, MSR-18, GEN-11, GEN-17, OTH-01, OTH-02, CTL-03, CTL-04, CTL-14, SOC-07, STA-02.

### /encode [P0]
Input: the raw problem; at P1 trap notes and up to 2 case bundles retrieved by class.
Steps:
1. Restate the goal in one sentence. Write facts and resources as self-contained numbered items with pronouns resolved. Two independent fresh calls each write a hard-constraint checklist; a script merges them and a third call resolves differences; recall is validated on 30 hand-constrained dev items (EVL-11).
2. Write `constraints.json` with the absolute solve bar: checklist items plus the required verification type for the item class (ARC: demo_match on all train demos; perturbation checks are P1, see section 8; BRAINTEASER: llm_consensus on the chosen option's premises or llm_falsifier, both "checked", or agreement only where neither runs; MacGyver: all items covered plus at least llm_falsifier) (EVL-15). No answer key and no held-out test output is written to any run file or copied into any sandbox; the harness scores `answer.json` against the key after the run. A key in the loop would make every arm that shares /verify an oracle selector.
3. A separate fresh call writes the first 5 answers that come to mind to `private/defaults.json`. No generator ever receives them or their labels. A script marks fixating cues as problem-text spans that also appear in the defaults (GEN-03, REP-02, REP-10).
4. If the item is in the pre-tagged formalizable subset, write `verifier/problem_model.py`; validate it (ARC: train pairs; otherwise a second fresh formalizer and agreement on 20 script-generated probe inputs, else the verification type falls to checklist); log its hash; set it read-only (REP-03).
5. A script writes per-call views: shuffled fact order with goal and constraints last, one canonical-order view always kept, permutation id logged; low_prior view from a fixed schema, linted against a per-item domain-noun list (REP-08, REP-02).
6. Encode tokens are logged as `encode_tokens`, capped at `encode_cap_mult` x the plain arm's `max_tokens` (2 x 16000 = 32000 tokens; the cap is checked before the optional resolve call), and charged to every arm that uses the outputs.
7. P1: `signature.json` against `signature_schema.json` (closed enums, ARC fields computed from grids), class = hash of coarse fields with back-off to family below N_min (REP-01); `components.json` with physical properties only, built in per-object fresh calls (GEN-13); retrieve at most 2 trap notes into the cue list and at most 2 case bundles for one generator (MEM-05, MEM-14).
Output: `problem.md`, `constraints.json`, `private/defaults.json`, `verifier/problem_model.py`, `variants/`, `signature.json`, `components.json`.
Mechanisms: REP-02, REP-03, REP-08, GEN-03, EVL-11, EVL-15, REP-10, REP-01, GEN-13, MEM-05, MEM-14.

### /generate (card executor) [P0]
Executes exactly one strategy card through `harness/run_card.py`. Replaces v0.1 /forage and absorbs /analogize as a card.
Input: the card's YAML, the card-specific view, a seed (sampled by script, id logged) of one of two types: a concept seed from `memory/seeds/concepts.txt` (P0), or, behind `flags.seed_type = doc_pack` (P1, SOC-02; the flag takes concept, the P0 default, or doc_pack), a retrieved-document pack of 2-3 documents from the fixed corpus `memory/seeds/docs.jsonl` chosen by script by goal-text similarity, with no role or identity text; and for revise one parent artifact plus its deterministic feedback record. The P1 cards add their own routed inputs (lemma predicates, a part spec, a gap list plus field pack), listed under each card below. Never routed to any generator: `graph.jsonl`, `clusters.jsonl`, any lineage view, `calls/*/thinking.txt`, `private/*`, failed candidates (enforced by the run_card.py copy step and audited from the routing log).
Steps:
1. The runner resolves the card's steps: which files are copied into the sandbox, which template is rendered, which tools the role may use. No LLM composes a generator prompt (Pr13).
2. The generator receives goal, hard constraints, the card's operator and the seed. No rubric, no instruction to judge. Output is a numbered list; a script splits it; an LLM converter runs only on parse failure and copies text verbatim; /verify derives the testable claim. The formal card has flag exec_feedback in {none, final-only, iterative}; under final-only the runner executes programs after the call returns (GEN-09).
3. Candidates per generator: default 8 (placeholder, swept 4/8/16 at fixed total tokens); 1-3 for programs (design default). Extra budget buys new calls, not longer lists (GEN-06).
4. The runner writes `cands/<call>.jsonl` with card, operator, seed, perm, parent_ids and origin = spoken (P1 cards add decomp_id, pack_id, gap_ids; lemma-build children carry lemma ids in parent_ids); a deterministic post-check strips justification markers and enforces a length cap (EVL-16). Return contract `{id, path, n_cands}` (REP-16). P1 (I5 part A, `flags.harvest_unspoken = capture`): the runner requests summarized thinking on generator calls and writes it to `calls/<id>/thinking.txt`; `harness/harvest.py` copies candidate-shaped spans (option letters, grids, code blocks, numbered items) verbatim from thinking.txt and from the visible non-list text of the output, strips justification and confidence markers with the same post-check, dedups them against the spoken list and writes `cands/<call>.unspoken.jsonl` with origin = unspoken. At P1 these rows are a diagnostic only and never enter the candidate set (section 4). Whether `claude -p` exposes thinking text is unverified; the fallback is the Messages API backend.
P0 cards:
- seeded: seed plus shuffled fact order; the undirected control share of the scaffold (the same input seeded best-of-N gets).
- low_prior: schema view with no domain cues, script-linted (REP-02).
- transform: a 3-call DAG. (1) A fresh transformer labels deep constraints (two-labeller agreement logged), applies one operator chosen uniformly at random by script (drop, negate, vary, oppose; P1: counterfactual-condition and remove-X operators, REP-11), and writes `transformed.md`; (2) a fresh solver works on `transformed.md` only; (3) a revise child applies "fix" against the original constraints with the feedback record. All three calls count in the card's tokens and count as one card toward the directed-card minimum. Drops to P1 if the first dev batch shows a zero pass rate against ground truth, harness-scored (GEN-12).
- formal: edit a scratch copy of the model in the sandbox and run it in the shell; program hypotheses for ARC; the verifier copy is never writable (REP-03).
- revise: a fresh child receives one parent artifact plus the feedback record from `harness/feedback.py` and applies one named operator: fix, specialize, recurse (P0, 1 parent); generalize, recombine (P1, 2 script-chosen parents). Runs only after an independent first round; the driver takes at most 2 parents per round from its revise queue (surprises first, then a script tournament on verifier scores; section 4). Feedback per benchmark: ARC = failing train-pair diffs; MacGyver = failed checklist item ids; BRAINTEASER = no revise, since its key never enters the loop (GEN-14, STA-07). The card is also where REP-04 (externalise, then re-perceive the artifact) is credited; a stand-alone fresh-reader card is P2.

Directed-card minimum (GEN-17): every round runs every P0 directed card that applies to the benchmark and round (low_prior and transform everywhere; formal on the pre-tagged formalizable subset; revise from the second round where allowed), at least 2 per round, lowered to 1 on BRAINTEASER if transform drops to P1 (recorded in plan.md). A card counts once however many calls it makes; the memory-blind call does not count. Round 1 is therefore seeded + memory-blind + low_prior + transform (n0 = 4) on BRAINTEASER, and the same plus formal (n0 = 5) on ARC-style items.
P1 cards: analogy (2 far sources from `memory/domains.jsonl` by goal-text embedding, near-for-repair as a sub-arm; code re-encoding arm or script-checked typed-triple mapping; GEN-08, REP-15), relabel (property-writer schema with no use field, script lint, id map; REP-09), compose (physical-property table, script-ordered slots, order flag; GEN-13). Stage 4 only: abduce-probe (executable hypotheses; script picks the probe with maximal output disagreement; GEN-15). P2: sparse (script-chosen keywords, constraints kept; GEN-01).

Owner-idea cards, all P1 post-gate: off in the gate configuration, built during Stage 3 behind their flags, each with a preregistered prior of no effect at matched compute, and each displacing seeded calls under matched B rather than adding to it.
- decompose (I2; `memory/strategies/decompose.yaml`, `flags.card_decompose`). Three steps. (1) plan: one fresh call that sees `problem.md` and the checklist writes `decomp/<call>/plan.json` = {parts: [{part_id, goal, inputs, outputs, interface, depends_on, checklist_ids, part_tests}], mode in {independent, sequential}}, P_max = 4, depth 1, nothing recurses into think(). (2) solve_part: K = 2 fresh calls per part through a new schema step field `foreach: <parsed_list>` in `strategies/schema.json`; each call sees `problem.md`, its own part spec and, in sequential mode, its parents' outputs only. (3) assemble: `harness/compose_parts.py` lists combinations at 0 LLM tokens on ARC and Stage 4 diffs (one fresh composer call for MacGyver prose), prunes them with part_tests and checklist_ids coverage, caps them at 16, writes `decomp/<call>/combos.jsonl`, and emits each combination as an ordinary row in `cands/<call>.jsonl` with parent_ids = the part candidate ids and decomp_id. Acceptance is only by the whole-problem /verify (demo_match plus perturbation on ARC; full checklist plus the negative-emergent check on MacGyver, that is, the assembled whole violates no constraint that no single part violated); model-written part_tests may prune or order combinations but never accept one, and no /judge score ever picks a "best part". Eligible from round 2 and in the stagnation reset's `fresh_tuples`, at most 1 instance per round; scope ARC formalizable subset, MacGyver and Stage 4 multi-hunk diffs, never BRAINTEASER (recorded in plan.md like the revise exclusion). Ledger rows gain n_parts, mode, K, combos_run, combo_pass, comp_gap. A decomposition is itself a frame (REP-13), so it stays inside one card and never moves into /encode.
- lemma (I1; `memory/strategies/lemma.yaml`, templates lemma.claims.txt and lemma.build.txt, `flags.lemmas`). Runs from round 2 only on ARC-style items and the pre-tagged formalizable subset. (1) claims: one fresh generator with shell receives goal, hard constraints and the train demos and writes up to 5 lemmas, each a short executable predicate over (input, output) or a sub-function with unit tests, to `lemmas.jsonl`. (2) `harness/lemma_check.py`, pure script, 0 tokens: a lemma becomes status verified (vtype execution) only if it holds on every train pair, fails on at least 30% of permuted mismatched pairs (input_i, output_j) (placeholder, logged as discrim), is not implied by an earlier verified lemma on the demo set, and passes the EVL-18 perturbation checks where they apply. The model never proves its own lemmas; unverified, LLM-checked or model-asserted lemmas never enter the pool. (3) build: the driver keeps `state.lemma_pool` (verified lemmas only) and spawns at most one fresh build call per round with the goal, the constraints and up to 3 pool lemmas chosen by highest discrim, as predicate source only, with no rationale and no parent candidate text; its whole candidates go through the normal /verify. Reset-crossing rule: the pool crosses a stagnation reset as predicates only, after the /restructure cosine < 0.8 lint against failed candidates. Sub-flag `flags.lemma_progress` (default off) lets a new verified discriminative lemma count as progress in the stall counter. Harness-only diagnostic, never in the loop: the rate of verified lemmas that fit the demos but not the test pair. Not built: LLM or PRM step scoring, lemmas on BRAINTEASER.
- gap_pack (I6 step B; `memory/strategies/gap_pack.yaml`, template gap_pack.gen.txt, `flags.gap_pack` in {off, goal_keyed, gap_keyed}). One step. After each /verify round the driver writes `gaps.json` (uncovered constraint ids from the /verify step 5 coverage mapping, dropped ids, a script-built query_text). The script picks a pack from `memory/domain_packs.jsonl`: top-k by cosine(query_text, pack embedding), then the least-used field among them, id logged (goal_keyed uses the goal text as the query instead). A fresh generator receives goal, constraints, the gap ids with their text and the pack text; it never receives candidates, so it is a generator, not a reviewer (Pr1, GEN-10), and the pack carries no profession label or persona. Runs from round 2, allocated like revise, does not count toward the directed-card minimum; scope MacGyver and the design set, never ARC (no fields) or BRAINTEASER (no computable gaps, REP-02 predicts harm). cands and ledger rows gain pack_id, gap_ids, gap_key_mode. Step C is an ablation arm, not a component: the same card with a profession label and no pack text ("label_only"), run under a harness-only lint exemption that never ships, tests the MSR-03 vs Pr10 conflict under the project's verifier (section 8). Optional P1 extension: the SOC-09 critic brief may also draw on domain_packs.jsonl entries ("pack-brief" arm).
Output: `cands/<call>.jsonl`, `prompts/<call-id>.txt`.
Mechanisms: GEN-06, GEN-07, GEN-09, GEN-10, GEN-12, GEN-14, GEN-17, REP-02, REP-04, REP-07, REP-11, SOC-01, SOC-02, CTL-01, STA-04, STA-07, GEN-08, REP-09, REP-15, GEN-13, GEN-15, GEN-01, CTL-13, CTL-17.

### /judge [P0]
Replaces v0.1 /evaluate. A fresh call that scores blind.
Input: candidates stripped to {id, text, testable_claim}, deterministically truncated; `problem.md`; the checklist as a feature source only.
Steps:
1. Score pointwise (one candidate per call) or in batches of at most 5 under two permutations averaged, positions hidden; the spread between permutations is logged as a stability feature (MSR-13, EVL-03).
2. Output the rubric score and p_raw. p_raw is logged; at P0 it steers nothing (EVL-08).
3. The confidence signal c is computed by script: agreement from a fixed probe of 3-5 seeded-card calls with the same input, run once per problem before round 1 and cached, its tokens charged to the run (clusters per benchmark: option letter; ARC predicted test-output grid; embedding cluster plus judge-confirmed equivalence for free text), with "matches an encode default" as a covariate; mapped through `calibration.json` to P(correct | c, vtype). p_raw enters as a logistic feature only once dev-tune has >= 300 labelled pairs and it improves held-out Brier (CTL-06, EVL-08). P1 (I3, `flags.lineage_independence_feature`): n_independent_roots and n_independent_nonseeded of the candidate's cluster (derived by `harness/graph.py` into `graph.jsonl` from the `clusters.jsonl` membership, pooled with the probe clusters; a child agreeing with its own parent is not a second vote, and no candidate contributes more than one independent vote) enter the same logistic map under the same >= 300 pair and held-out-Brier gate, beside agreement and the "matches an encode default" covariate. The feature changes only state.conf, hence verification order and k; it never touches acceptance or the stop rule (Pr7), and a cluster converging on an encode default keeps the defaults routing and gets no bonus (Pr5).
4. P1: for open-ended and secondary items, return the top-k lineages (k swept 1/2/3) for development rather than a winner (EVL-04). P2: after a restructure, re-score dormant candidates (never verified, not duplicates), top 10 by p_raw, as an ordering key only (MEM-06).
Rules: never proposes; never sees rationales, arm labels, serial position or generator identity (EVL-03, EVL-16, MSR-13, MSR-04). Distance from cue and from defaults are logged separately as diagnostics (EVL-09).
Output: `judgments.jsonl`.
Mechanisms: EVL-03, EVL-08, EVL-16, MSR-04, MSR-13, EVL-04, EVL-09, MEM-06, CTL-06.

### /verify (includes verifier construction) [P0]
Replaces v0.1 /insight-check.
Input: a bare candidate (no confidence, no rationale), `problem.md`, `constraints.json`, the hashed verifier model, and the confidence c used only to set attempt count and never shown to any falsifier.
Steps:
1. Before generation, build and validate the strongest available check (step 4 of /encode): executable model, exact demo match and a program-length prior; otherwise the merged checklist plus a falsifier. Perturbation checks (colour permutation, rotation equivariance where allowed) are P1 (section 8): `verify.py` does demo_match only, and `harness/arc_exec.py` `perturbation_detail` computes rotations, mirrors and colour permutations as detail only, never as part of the verdict. Check the verifier hash before every call (REP-03, EVL-18).
2. Order the queue by c (and p_raw where validated); verify only the top m_verify = 3 per round; attempts k = base + ceil(alpha x c), capped at k_max = 3 (EVL-01). P1 (I4, `flags.verify_order` in {top_conf (default), top_conf_plus_explore}): under the explore setting 2 of the 3 slots go to the top by c and 1 to a uniform draw from the unverified remainder, seed logged; m_verify is unchanged so cost is matched. Built only if the pruning-regret diagnostic (section 8) shows that cause (a), never verified, dominates.
3. Run the check and log the verification type. External types: execution, solver, demo_match, sourced_fact; these make status "verified". Adversarial-LLM types: llm_falsifier (no counterexample after k distinct fresh-context attempts, each with a different evidence seed or constraint focus, outputting a concrete counterexample claim that is executed or sourced where possible; distinct by embedding), llm_consensus (3 fresh contexts agree on a commonsense premise); these make status "checked", and a checked candidate that clears the bar can stop a run only once `flags.llm_falsifier_validated` is set (section 4). Narrated self-check is not a type (EVL-02, Pr15).
4. Candidates near a seed-injected cue go to a falsifier that never saw the seed; in-problem cues are handled by giving the falsifier a script-relabelled problem copy (EVL-01).
5. Coverage: score the checklist item by item; the converter, not the generator, maps each candidate to the constraints it addresses (EVL-11).
6. P1: for non-executable items, extract at most 5 premises the testable claim depends on; sourceable premises need a quoted span plus URL matched by a second fresh call (sourced_fact); commonsense premises get three fresh judgments (llm_consensus); a winner on an unchecked premise is at most "checked" (EVL-10). P1: structural counterexample check in place of a debate: a critic outputs a concrete counterexample or violated item, a fresh tool-using checker confirms it, a judge may only demote (SOC-09). P1: discriminating test between rivals (theory-grade).
7. Write `feedback_record` through `harness/feedback.py` (failing checklist ids, first k mismatched cells, stderr tail, counterexample verbatim; <= 1.5k tokens, design cap). Log surprise = 1[c > hi and fail] and repr_change_event as separate fields (MSR-08). Write schema-conformant rows to `evidence.jsonl` with candidate spans masked (MEM-13).
Output: `verify.jsonl`, `evidence.jsonl`, `surprises.jsonl`.
Mechanisms: EVL-01, EVL-02, EVL-10, EVL-11, EVL-18, REP-03, REP-15, SOC-09, MSR-08, MEM-13, STA-07.

### /restructure [P1]
Input: `problem.md`, `constraints.json`, `dropped.json`, masked `evidence.jsonl`, a script-generated impasse summary from structured fields (violated constraint ids, types tried, counts). Never the failed candidates; the reset input is linted for cosine < 0.8 to any failed candidate.
Steps:
1. Apply one operator per fresh generator: re-add one dropped element (REP-05); relabel resources (REP-09); transform a deep constraint (GEN-12).
2. Write each result as a new variant, logged in `framings.jsonl` with {operator, new_space}; old versions kept.
3. Hand the variants to fresh generators with unused (card, operator, seed, permutation) tuples (CTL-11, CTL-14).
4. P2: a fresh judge re-scores dormant candidates (MEM-06).
Output: `problem.vN.md`, `framings.jsonl`.
Mechanisms: CTL-11, CTL-14, GEN-12, REP-05, REP-09, MEM-06, MEM-13.

### /incubate [P2 flag]
Reduced to one testable ingredient. The within-run fresh return is merged into the stagnation reset (one flag, owned by CTL-11). What remains is "retry after memory update": unsolved train and dev items are re-attempted by a fresh agent after the next view rebuild, with traps and cases from the same item id excluded, retry tokens summed into the item's budget, reported under pass@k only, against a control that retries with frozen memory at the same position (STA-13). No filler at P0; undemanding filler vs none is a P1 flag of the reset family (CTL-02); other filler types are P2 flags (CTL-18, STA-05).
Mechanisms: STA-13, CTL-02, CTL-15, CTL-18, STA-05.

### /ledger [P0] and /consolidate [offline, P1 views]
Input: `runs/<id>/*`, ground truth for train and dev-tune only.
Steps:
1. P0: after the parallel calls of a cycle return, the driver appends one row per card call and per verification to `memory/ledger.jsonl`: run, split, family, class, card, operator, round-type (first, revise, post-reset), seed, perm, tokens, p_raw, agreement, verification type, status, ground truth where allowed, snapshot hash; origin (spoken, unspoken, probe, default) from v0.3; under their flags the P1 cards add n_parts, mode, K, combos_run, combo_pass, comp_gap (decompose), lemma ids and discrim (lemma), pack_id, gap_ids, gap_key_mode (gap_pack), and frontier rows add particle_id and weight. Nothing is overwritten (MEM-11). `clusters.jsonl` (membership rows appended by think.py at the dedup step) and `graph.jsonl` (nodes, edges and per-cluster root counts written by `harness/graph.py` from cands, verify and clusters.jsonl) are per-run derived files, not ledger rows; each has one writer, and both are rebuilt from those sources, so they add no second source of truth.
2. P0: `harness/stats.py` rebuilds `memory/views/<batch>/strategy_stats.json` from train rows only: Beta(pass) and mean tokens per (class, card, round-type). No LLM writes any view (MEM-16, CTL-07).
3. P1: refit `calibration.json` on dev-tune pairs (uniform set; traps are not added as extra data); build `traps.jsonl` by script from high-confidence failures joined to cands and verify rows; build `cases/<id>.json` bundles by script with no principle; lint every card and case for name, docstring, example and applicability (MEM-14, MEM-08, MEM-10).
4. P1: rerun the fixed 30-item regression set at 1x, 1 replicate; block = revert to the previous view snapshot when P(drop > 5 points) > 0.8 under a beta-binomial model; tokens reported as amortized offline cost (MEM-11).
5. P2: LLM-written case principles audited by a fresh agent against source rows; schema library from clusters of 3+ verified runs as canonical relation tables, MDL by script over those tables, plateau-gated merging, anti-unification; suppression trials for over-used cards (MEM-02, MEM-09, MEM-15, MEM-16, MEM-17).
Output: `memory/ledger.jsonl`, `memory/views/<batch>/*`, `memory/cases/`.
Mechanisms: MEM-11, MEM-16, CTL-07, MEM-14, MEM-05, MEM-08, MEM-10, MEM-13, MEM-17, MEM-02, MEM-09, MEM-15, EVL-10, MSR-11.

### /experiment [P1, Stage 4-5 prerequisite]
Input: baseline script, candidate diff, seed list, fixed budget (EXPERIMENT_PLAN section 4).
Steps:
1. Apply the diff; launch the fixed-budget training run on D:; parse `metrics.json`.
2. Accept only under the e-value verdict of docs/VERDICT.md (`nano/verdict.py` `sequential_verdict`, `nano/batch_verify.py`): e-value >= 100 for a 0.005-nat margin over >= 3 seeds paired by seed number with a shared baseline set, noise fixed from the baseline runs alone, e-BH across the night. The "2 seed SD, 5 for close calls" rule is retired (optional stopping). Report wall-clock, VRAM and parameter count.
3. Append to `memory/experiments/ledger.jsonl`: {diff_hash, hypothesis, card, island_id, lineage_id, parent_ids, hunks with contributions, seeds, mean, sd, status}.
4. Population search (Stage 4): islands keyed by card with frozen assignment and per-island pools; `harness/think/tournament.py` runs size-2 tournaments on verifier scores (val-loss delta), uniform fallback logged; hub cap per generation = ceil(0.3 x children) per parent (placeholder, swept); migration at least twice per run (interval swept); children receive at most 6 hunk rows with measured contribution (from component ablation where it exists, else "unmeasured") in randomized order, never a ranked table (SOC-03, SOC-04, SOC-05).
5. Component ablation for winning multi-part diffs only: leave-one-component-out, at most 4 components, 3 seeds (EVL-05).
6. Hypotheses via the abduce-probe card: executable predictions; a script picks the probe with maximal disagreement; one config key changed per probe, checked on the diff (GEN-15).
Output: run folders on D:, ledger rows, candidate findings with diff, metrics and decision trace.
Mechanisms: GEN-15, GEN-14, EVL-05, SOC-03, SOC-04, SOC-05, MEM-08, MEM-13, MSR-02.

### /think (orchestrator) [P0]
A SKILL.md that launches `harness/think.py` with the problem, m and flags, waits, and summarizes `answer.json`. It holds no control logic and no candidate text. See section 4.

Deferred, not built in v0.2: /wander (GEN-04, GEN-05, MEM-12, MSR-06) exists only as a flagged harness arm on the open-ended design set.

---

## 4. The orchestrator

`harness/think.py`, python. Every branch below is code; LLM calls are the leaves `run_card`, `judge`, `verify`.

```
think(problem, m, flags):
  B = m * cot_tokens(problem.benchmark)          # cost definition in plan.md
  state = {spent: 0, round: 0, best: None, best_checked: None, stale: 0, pop: [],
           used_tuples: set(), conf: {}, agree: {}, revise_queue: [], variants: [],
           lemma_pool: [], frontier: None}      # lemma_pool: flags.lemmas (P1, I1), verified lemmas
                                                  #   only; frontier: flags.frontier (P1, I4)
  P = encode(problem)                             # 2-call checklist merged, bar, private defaults,
                                                  #   validated hashed verifier model, views; no answer
                                                  #   key or test output ever enters P or any sandbox
  state.spent += P.encode_tokens                  # charged before the loop (and to every arm using P)
  V = verify.build(P); state.spent += usage(V); state.verifier_hash = V.hash
  cls = family(P) if not flags.signature else signature_class(P)   # family key at P0
  views_snapshot = load_views(flags.snapshot)     # train-built, frozen; never written during a run
  probe = run_probe(P, n=n_probe)                 # 3-5 seeded-card calls, ONCE per problem, cached
  state.spent += usage(probe)
  S = allocate.initial(cls, views_snapshot, n0)   # seeded + memory-blind (uniform-random card) + every
                                                  #   applicable P0 directed card, >= 2 (GEN-17);
                                                  #   round-robin until N_min rows per cell, then
                                                  #   Thompson: p ~ Beta(cell), score p / est_cost,
                                                  #   10% total exploration floor
  while state.round < R_max:
    for s in S[:max_spawns_per_round]:
      if state.spent + est_cost(s) > B: break     # budget checked before every spawn
      spawn(run_card(s, view(P, s, s.variant), seed(s)))   # sandboxed, fresh session, return
      state.used_tuples.add(tuple(s))             #   contract; tuple = (card, operator, seed, perm)
    C = collect(); state.spent += usage(C)        # generator calls, incl. converter on parse failure
    if flags.harvest_unspoken != 'off':           # P1 (I5): harvest.py reads calls/<id>/thinking.txt
      U = harvest(calls)                          #   -> cands/<call>.unspoken.jsonl, 0 tokens;
      if flags.harvest_unspoken == 'merge':       #   'capture' (P1) = diagnostic only, U never
        C += dedup.drop(U, C + all_prior_cands)[:u_max]   #   enters C; 'merge' is P2, only after
                                                  #   unspoken_correct_rate >= 3 points on dev
    if flags.lemmas:                              # P1 (I1): lemma claims are proved by script
      state.lemma_pool += lemma_check(claims(C), P)   #   (lemma_check.py, 0 tokens); verified only
    if flags.card_decompose:                      # P1 (I2): compose_parts.py turns part outputs
      C += compose_parts(parts(C), P)             #   into whole candidates, 0 tokens on ARC/diffs
    dup_rate = dedup.rate(C, all_prior_cands)     # measured BEFORE dropping, logged
    C, clusters = dedup.drop(C, benchmark_rule)   # exact option / ARC output / embedding for text;
    append(clusters_jsonl, clusters)              #   think.py appends membership rows {cluster_id,
                                                  #   rule, members, representative_id, round} (I3);
                                                  #   it is the only writer of clusters.jsonl
    state.spent += usage(dedup)                   # embedding calls (0 for the pinned local model)
    J = judge(C); state.spent += usage(J)         # pointwise or <=5 x 2 permutations; J.p_raw logged
    a = agreement(probe, C)                       # cached probe clusters, per-benchmark rule
    for cand in C:                                # kept in state per candidate id, across rounds
      state.agree[cand.id] = a[cand.id]
      state.conf[cand.id] = calibrate(a[cand.id], J.p_raw[cand.id] if flags.p_raw_validated else None)
    progress = False
    queue = top(C, by=state.conf, n=m_verify)     # m_verify = 3
    if flags.verify_order == 'top_conf_plus_explore':      # P1 (I4): 2 by conf + 1 uniform draw
      queue = top(C, by=state.conf, n=m_verify - 1) \
              + uniform(C - queue, n=1, seed_logged=True)  #   from the unverified remainder
    for cand in queue:
      if state.spent + est_verify(cand) > B: break
      k = min(k_max, base + ceil(alpha * state.conf[cand.id]))
      r = verify.run(cand, V, attempts=k)         # falsifier never sees conf; attempts diverse
      state.spent += usage(r)                     # every attempt, premise and checker call
      ledger.append(row(run, cls, cand, r, state.conf[cand.id], snapshot_hash))
      if clears(P.bar, r):
        progress = True
        if r.status == 'verified': state.best = pick(state.best, cand, key=best_key)
        if r.status == 'checked':  state.best_checked = pick(state.best_checked, cand, key=best_key)
      if r.status == 'fail':
        state.revise_queue.append((cand, r.feedback_record))         # parent pool for revise
        if state.conf[cand.id] > hi: surprises.append(cand)          # surprises go first
    state.pop = admit.update(state.pop, C, J, k_pop)     # admit iff verified or conf >= theta_admit
    log_decision(state, signal)                          # one row per cycle, script-written
    graph.write(run)                                     # P0 (I3): harness/graph.py -> graph.jsonl only
                                                         #   (nodes, edges, per-cluster root counts derived
                                                         #   from clusters.jsonl); 0 tokens; read by no call
                                                         #   in the loop; never copied into any sandbox
    if flags.gap_pack != 'off': gaps.write(run, coverage(C))   # P1 (I6): gaps.json, script-built
    if state.best and Pcorrect('verified', state.agree[state.best.id]) >= T:
      return answer(state.best, 'verified')
    if flags.llm_falsifier_validated and state.best_checked \
       and Pcorrect('checked', state.agree[state.best_checked.id]) >= T_checked:
      return answer(state.best_checked, 'checked')       # weakest stratum (EVL-02), never 'verified'
    gain = stop.partial_gain(state) if graded(P) else 0  # partial score exists on graded items only
    state.stale = 0 if (progress or gain > eps) else state.stale + 1
    state.round += 1
    if R_max > 2 and (state.stale >= R_stale or dup_rate > d_max):   # CTL-04: no reset if R_max <= 2
      if flags.restructure:                              # stagnation -> reset, never extend
        state.variants = restructure(P, masked_evidence); state.spent += usage(state.variants)
      S = allocate.fresh_tuples(cls, state.used_tuples, variants=state.variants)
                                                         # unused (card, operator, seed, perm) tuples;
                                                         #   each reset generator gets one variant as
                                                         #   s.variant (base views if no restructure);
                                                         #   decompose is eligible in this pool (I2)
      state.revise_queue = []                            # reset inputs never carry failed candidates
      state.frontier = None                              # P1 (I4): a frontier lives within one epoch
      if flags.lemmas:                                   # P1 (I1) reset-crossing rule: predicates
        state.lemma_pool = cross_lint(state.lemma_pool)  #   only, cosine < 0.8 to any failed candidate
      state.stale = 0; continue
    S = allocate.reallocate(S, lp_multiplier if graded(P) else 1.0)  # never below the floor
    if revise_allowed(P.benchmark):                      # never on BRAINTEASER; round >= 1 here
      if flags.frontier == 'tournament':                 # v0.2 default
        parents = tournament(state.revise_queue, surprises_first=True, n=2)   # verifier scores only
      else:                                              # P1 (I4): beam_topK | smc, think/frontier.py;
        parents = frontier.resample(state, K=2, weights='verifier_partial_score')
                                                         #   never conf or p_raw (lint on inputs);
                                                         #   writes frontier.jsonl; built only if the
                                                         #   pruning-regret diagnostic shows regret
      S = S + revise_specs(parents); state.revise_queue.remove_all(parents) # revise spawns <= 2
    if flags.lemmas and eligible('lemma', P, state.round):   # P1 (I1): claims call from round 2 on
      S = S + [lemma_claims_spec()]                      #   ARC-style and formalizable items only;
                                                         #   its output feeds lemma_check in collect
    if flags.lemmas and state.lemma_pool:                # P1 (I1): at most ONE build call per round;
      S = S + [build_spec(top(state.lemma_pool, by='discrim', n=3))]   #   predicate source only
    if flags.card_decompose and eligible('decompose', P, state.round):  # P1 (I2): from round 2,
      S = S + [decompose_spec()]                         #   <= 1 per round; never BRAINTEASER
    if flags.gap_pack != 'off' and eligible('gap_pack', P, state.round):   # P1 (I6): MacGyver and
      S = S + gap_pack_specs(select_packs(gaps, flags.gap_pack, n=gap_pack_max))
                                                         #   the design set only, from round 2;
                                                         #   gap_pack_max = 2 (section 5), one pack
                                                         #   per spec; generator sees no candidates
    S = S[:max_spawns_per_round]
    if all(p_s * V_tokens < est_cost(s) for s in S): break           # V_tokens = B
  # round cap, budget or value stop reached
  if state.best: return answer(state.best, 'verified')
  if state.best_checked: return answer(state.best_checked, 'checked')   # labelled, never 'verified'
  b = best(state.pop)                              # order: (vtype stratum verified > checked >
                                                   #   unverified, then calibrated P from state.conf)
  if b and checked(b): return answer(b, 'checked')
  if b and state.conf[b.id] >= optout: return answer(b, 'unverified')
  return abstain(impasse_report_from_fields(state), best_guess=b)
  # ledger rows are already written each cycle; consolidate runs offline between batches only
```

Each cycle is one script-written decision with the signal that drove it (agreement, surprise, stagnation, allocation). The driver never asks a call to try harder; it changes what enters the candidate set (CTL-11, CTL-14). Impasse routing is explicit: budget left and stale < R_stale gives more generation; stale gives restructure or reset; no budget gives abstain (EVL-15).

Spend accounting. `state.spent` adds the usage of every call when it returns: encode before the loop, the verifier build, the agreement probe (once per problem), generators and the converter, embedding calls, the judge, every verify attempt with its premise and checker calls, and restructure. est_cost(s) and est_verify(cand) are defined in plan.md: est_cost is the cell's mean tokens per call from `strategy_stats.json`, or during cold start the sum over the card's steps of max_tokens plus the measured size of the routed inputs plus the measured subagent system-prompt overhead; est_verify is k times the run's mean tokens per verify attempt, or at cold start the falsifier template's max_tokens plus its inputs. A call whose realized cost exceeds its estimate is still charged in full, so realized spend can exceed B by at most one call; the overshoot is reported beside the cap.

Owner-idea hooks (v0.3). `graph.write` runs after every cycle at 0 LLM tokens and is the only P0 addition; its output is a view for the owner and, at P1, a calibration feature, and it is never routed into any generator, judge or falsifier prompt. Every other hook above is P1 or P2, off in the gate configuration, and keeps the invariants of this section: the lemma pool holds only script-verified predicates and feeds at most one build call per round; decompose combinations are accepted only by the whole-problem /verify; frontier weights come from verifier partial scores only and a frontier never crosses a reset; harvested unspoken candidates are a diagnostic at P1 and compete for the same m_verify slots only under the P2 merge setting; gap_pack generators never see candidates. The P2 prior_map fold (I5 part C) replaces the /encode defaults call with `private/prior_map.json` built from the plain samples and the probe clusters, only after its near-default routing agrees with `defaults.json` on at least 90% of items; Pr5 holds either way.

Progress and stopping. On ungraded benchmarks (BRAINTEASER) there is no partial score, so a round counts as progress only if it yields a new verified or bar-clearing candidate; a round with neither raises `stale`. Checked candidates have their own track (`best_checked`, threshold T_checked) and can stop a run early only after llm_falsifier has passed its dev false-acceptance test (EVL-02); before that they are returned at the end, labelled "checked". `best_key` and `best()` order by verification stratum first and calibrated P second, never by p_raw alone.

---

## 5. Control parameters

Provenance: "evidence" if a catalog row supplies the value, "placeholder" otherwise. Every parameter is logged in `state.json` and tuned on dev-tune only.

| Parameter | Default | Provenance | Signal that sets it | Mechanism |
|---|---|---|---|---|
| m, cost multiplier over plain CoT | 20; swept {5, 10, 20, 40} for scaffold and primary null | design | harness | CTL-03, MSR-02 |
| n0, first-round fan-out | 4 on BRAINTEASER, 5 on ARC-style: seeded + memory-blind + every applicable P0 directed card (minimum 2) | derived from the GEN-17 rule | benchmark and round | GEN-10, GEN-17, SOC-01 |
| max_spawns_per_round | n0 + 3 (2 revise children + 1 respawn) | placeholder | cost | GEN-10, GEN-14 |
| Candidates per generator | 8; swept 4/8/16 at fixed tokens; 1-3 for programs | placeholder | dev-tune | GEN-06 |
| R_max, round cap | 3; swept {1, 2, 4, 8} at the largest m only | placeholder | solve-per-token with termination cause | CTL-04 |
| T, acceptance threshold on P(correct given vtype = verified, agreement) | fixed; dev-tune; declining schedule as P1 arm | design | calibration | CTL-05 |
| T_checked, threshold for the checked track | fixed on dev-tune; inactive until `flags.llm_falsifier_validated` | placeholder | calibration of the checked stratum | EVL-02, CTL-05 |
| llm_falsifier validation level | maximum dev false-acceptance rate written in plan.md before the first dev batch | placeholder | dev ground truth | EVL-02 |
| eps, minimum partial-score gain that counts as progress | 0.01 of the graded score; unused on ungraded benchmarks | placeholder | dev-tune | CTL-11 |
| est_cost(s), est_verify(cand) | cell mean tokens from `strategy_stats.json`; cold start from card max_tokens plus routed-input size plus measured subagent overhead; est_verify = k x run mean per attempt | design | plan.md | CTL-07, Decision 3 |
| Agreement probe size | 3-5 seeded-card calls, once per problem, cached | placeholder | dev-tune | CTL-06, EVL-08 |
| Opt-out level | where best-candidate precision falls below the plain arm's accuracy | design | dev-tune | CTL-05, EVL-15 |
| m_verify, candidates verified per round | 3 | design cap | cost | EVL-01 |
| k = base + ceil(alpha x c), k_max | base 1, k_max 3; alpha from the false-acceptance curve on ARC dev | design bet (direction) | confidence | EVL-01 |
| hi, surprise threshold | 0.8 | placeholder | dev-tune | CTL-06, MSR-08 |
| Dedup rule and threshold | exact option; ARC output; embeddings for text, threshold tuned on labelled pairs | placeholder | hand-labelled dev pairs | CTL-10, CTL-11 |
| R_stale, d_max | 2; 0.5; swept 1/2/3 and 0.3/0.5/0.7 | placeholder | dev-tune | CTL-11 |
| k_pop, elite slots; theta_admit | 5 (preprint-derived toy result); dev-tune | placeholder | dev-tune; P1 sweep 2/5/10 | CTL-09 |
| Card allocation | round-robin until N_min = 20 rows per (class, card, round-type); Thompson on p / mean_tokens; 10% total floor; 1 memory-blind uniform-random card | engineering | train-built views, frozen | CTL-07, MEM-17 |
| V_tokens, value of a solve | B | design | stop rule | CTL-07 |
| Within-run LP multiplier (P1) | smoothed softmax over recent partial gain; graded benchmarks only; never below the floor | engineering | verifier partial scores | CTL-08 |
| Lineage leave rule (P1) | MVT-style or swept 1/2/3 children; graded benchmarks only | placeholder | dev-tune | GEN-02 |
| Revise spawns per round | <= 2 | design cap | cost | GEN-14 |
| Parents per revise operator | 1 (P0 ops), 2 (P1 ops); swept {1, 2, 4} | placeholder | dev-tune | REP-07 |
| Feedback form for revise | deterministic record (P0); arms: pass/fail bit, none, praise, prose summary (P1) | design | ground truth on executable items | STA-07 |
| Per-agent context bound (P1) | max tool calls per card; exact token loop for tool-using cards; cap 40k swept to 64k | placeholder | script | STA-04 |
| Encode token cap | 2x one CoT call | design cap | script | SYNTHESIS Representation design notes; Decision 3 (cost); REP-03, REP-08 |
| Memory injection cap (P1) | 2 items per run total, 1 generator; arm 0/2/5-10 | placeholder | paired diversity CI | MEM-17, MEM-01 |
| Hub cap, migration interval (Stage 4) | ceil(0.3 x children) per parent; >= 2 migrations per run; both swept | placeholder | tournament script | SOC-03, SOC-05 |
| Seed weight (P2) | 1/sqrt(1+count) x cosine(seed, goal) | design | seed_counts.json | CTL-13 |
| Keep/drop | Beta(1,1) on discordant pairs; P(helps) > 0.95; fixed batch count; snapshot-aligned | design | dev-ablate | MSR-18 |
| TOST equivalence margin | 3 points | placeholder | dev noise floor | OTH-02 |
| Signature stability | field agreement >= 80% over 3 /encode runs | placeholder | dev | REP-01 |
| Verifier-model agreement probe inputs | 20 script-generated inputs | placeholder | dev | REP-03 |
| Checklist recall set | 30 hand-constrained dev items | placeholder | dev | EVL-11 |
| p_raw entry | >= 300 labelled dev-tune pairs and improved held-out Brier | placeholder | dev-tune | EVL-08 |
| Calibration cell minimum | 50 items per difficulty-bin cell | placeholder | dev-tune | MSR-04 |
| Length-invariance probe set | 50 answers, short and long justification each | placeholder | dev | MSR-04 |
| Reset-input lint; evidence masking | cosine < 0.8 to any failed candidate; mask spans with cosine > 0.8 | placeholder | dev-tune | CTL-11, MEM-13 |
| Evidence and feedback record caps | 1.5k tokens each | design cap | script | MEM-13, STA-07 |
| Trap failure_output cap | 300 tokens | design cap | script | MEM-14 |
| Case bundle cap (P1) | 800 tokens | design cap | script | MEM-08 |
| Regression set and block rule (P1) | R = 30 dev items; revert when P(drop > 5 points) > 0.8 | placeholder | beta-binomial model | MEM-11 |
| Graph write (I3, P0) | after every cycle; `graph.py --check` requires 100% node and edge completeness | design (diagnostic, exempt) | script | I3; GEN-14, CTL-10 |
| Lineage-independence feature entry (I3, P1) | same gate as p_raw: >= 300 dev-tune pairs and improved held-out Brier against agreement-only and agreement plus raw cluster size | placeholder | dev-tune | I3; EVL-08, CTL-06 |
| Pruning-regret close rule (I4, P0 diagnostic) | close I4 step 2 if causes (a)+(b)+(c) sum to < 5% of keyed items on dev-tune (ARC-style and MacGyver-labelled) | placeholder | offline key check | I4; MSR-05, CTL-09, EVL-01 |
| Frontier K, beta, epsilon, resample trigger (I4, P1) | K = 2 (tied to the revise cap); beta and epsilon placeholders; systematic resampling when ESS < K/2; weights from verifier partial score only; wiped on reset; off on BRAINTEASER | placeholder | dev-tune | I4; SOC-05, GEN-02 |
| verify_order explore slots (I4, P1) | 1 of m_verify = 3 slots, uniform from the unverified remainder, seed logged | design | script | I4; EVL-01 |
| u_max, harvested candidates per call (I5) | 2; the P2 merge setting only when unspoken_correct_rate >= 3 points on dev | placeholder | offline key check | I5; GEN-06, EVL-16 |
| prior_map fold check (I5, P2) | near-default routing agreement >= 90% of items between prior_map.json and defaults.json | placeholder | dev | I5; GEN-03 |
| Lemma caps (I1, P1) | <= 5 lemmas per claims call; discrim >= 30% of permuted mismatched pairs; <= 3 pool lemmas per build call by highest discrim; <= 1 build call per round; lemma_progress off | placeholder | dev-tune | I1; REP-03, EVL-18 |
| Decompose caps (I2, P1) | P_max = 4, depth 1; K = 2, swept {1, 2, 3} at equal tokens; combination cap 16; <= 1 instance per round, from round 2 | placeholder | dev-tune | I2; GEN-13, EVL-11 |
| gap_pack retrieval (I6, P1) | pack text <= 1.5k tokens; top-k by cosine(query_text, pack embedding), then the least-used field; from round 2; <= 2 calls per round | placeholder | dev-tune | I6; SOC-02, GEN-08 |
| Document pack size (SOC-02, P1; `flags.seed_type` in {concept, doc_pack}) | 2-3 documents per call, chosen by goal-text similarity | placeholder | dev-tune | SOC-02 |

---

## 6. Memory design

Per run: the `runs/<id>/` folder is immutable once the run ends.

Across runs, one source of truth and versioned derived views:
- `memory/ledger.jsonl`: append-only, written only by the driver after a cycle's calls return; one row per card call and per verification with the fields in /ledger step 1 (MEM-11).
- `memory/views/<batch>/strategy_stats.json`: Beta(pass) and mean tokens per (class, card, round-type) from train rows; frozen snapshots at increasing row counts are the memory arms (CTL-07, MSR-11). Never LLM-written (MEM-16).
- `memory/views/<batch>/calibration.json`: logistic or per-stratum isotonic map from (agreement[, p_raw], verification_type) to P(correct), fit on dev-tune only, minimum cell sizes, agreement-only fallback (EVL-08).
- `memory/views/<batch>/traps.jsonl`: script-built {class, testable_claim, confidence, failing constraint id, failure_output <= 300 tokens}; retrieved by exact class then claim embedding, top-2, into /encode cues and judge and falsifier briefs, never generators; a match raises verification priority only (MEM-14).
- `memory/strategies/<card>.yaml` against `schema.json`: name, docstring, applicability signature, steps with template ids and parsers, parameters, example, provenance, version (MEM-10, Pr13).
- `memory/cases/<id>.json` (P1): script-built bundles capped at 800 tokens; at most 2 per run into 1 generator (MEM-05, MEM-08). LLM-written principles only at P2, audited (MEM-16).
- `memory/domains.jsonl`, `memory/seeds/concepts.txt`: fixed inputs for analogy sources and seeds.
- `memory/experiments/ledger.jsonl` (Stage 4-5): diffs with islands, lineages, hunks and contributions, seed statistics and verdicts; raw logs on D:.

Routing table (enforced by the driver's copy step and audited from the prompt-routing log):

```
  item              -> encode | generator | judge | falsifier | reset/restructure
  private defaults  ->   w    |    -      |   -   |    -      |   -
  trap notes        ->   r    |    -      |   r   |    r      |   -
  case bundles      ->   -    |  r (1)    |   -   |    -      |   -
  evidence (masked) ->   -    |    -      |   -   |    -      |   r
  parent artifact   ->   -    | r (revise)|   -   |    -      |   -
  failed candidates ->   -    |    -      |   -   |    -      |   -
  answer key, test  ->   -    |    -      |   -   |    -      |   -     (harness scorer only)
  lemma predicates  ->   -    | r (build) |   -   |    -      |   r     (I1, P1: predicates only, linted)
  part spec (I2)    ->   -    | r (part)  |   -   |    -      |   -     (own part + parents' outputs)
  gap ids + pack    ->   -    | r (gap)   |   -   |    -      |   -     (I6, P1: no candidates, no label)
  document pack     ->   -    | r (seed)  |   -   |    -      |   -     (SOC-02, P1 seed type)
  graph, clusters   ->   -    |    -      |   -   |    -      |   -     (I3: owner view; calibration
                                                                        feature at P1, never a prompt)
  thinking.txt      ->   -    |    -      |   -   |    -      |   -     (I5: harvest.py only)
```

Rules: episodic rows inform control only; case bundles may supply content under the cap; past-run text never reaches generators otherwise (MEM-01, MEM-17). Only verified outcomes, or validated-judge outcomes where no verifier exists, update statistics; entries resting on unchecked premises are not promoted (EVL-10). One memory-blind generator with a uniform-random card runs in every scaffold run (MEM-17). Held-out items never enter memory; memory is credited by the slope of held-out solve rate against snapshot size, with empty memory as the null (MSR-11). The regression set is rerun after every rebuild and a drop reverts the snapshot (MEM-11).

---

## 7. Offline phase

Between batches, never inside a run, no LLM in the loop for statistics:
1. Rebuild `strategy_stats.json` from train rows into a new `views/<batch>/` (CTL-07).
2. Refit `calibration.json` on dev-tune pairs; report Brier and adaptive-bin ECE drift per difficulty bin with CIs (EVL-08, MSR-04).
3. Build `traps.jsonl` and case bundles by script (MEM-14, MEM-08).
4. Rerun the 30-item regression set; revert on a preregistered drop (MEM-11).
5. Lint templates, cards, `memory/domain_packs.jsonl` and the batch's rendered prompts, including the unspoken-candidates wording rule under Pr10 (GEN-11, STA-02, OTH-01, MEM-10, I5, I6).
6. Revalidate /judge on dev-tune, including the self-preference and length probes (EVL-08).
7. Update `harness/plan.md` before any test-split use; record the snapshot hash (MSR-02).
8. P2 flags, each its own arm (MSR-18): retry after memory update (STA-13); audited case principles; schema induction with MDL and anti-unification (MEM-02, MEM-09, MEM-15); suppression trials (MEM-17); corrupted-variant replay (STA-12); episode blending (GEN-05); filler types other than undemanding filler (CTL-18, STA-05).

There is no sleep, dream or filler simulation at P0. The no-filler default departs from the human incubation meta-analysis (undemanding filler helped) because of the LLM disanalogy; undemanding filler vs none is a P1 flag of the reset family, and other filler types are P2. Offline token cost is reported separately and amortized into per-item cost.

---

## 8. Measurement harness

Benchmarks. Gate: ARC-style (program induction; executable; ARC-AGI-2 public eval preferred over ARC-1) and BRAINTEASER (4-way multiple choice; the exact key is used only by the harness scorer and never enters the loop, so the in-loop bar uses checked types or agreement only, EVL-15; reconstruction variants or fresh paraphrases where the headroom pilot shows ceiling). Secondary: MacGyver (functional fixedness; no ground truth for model-written solutions; scored by an evaluation judge separate from /judge on a human-labelled subset of 100-150 scaffold and best-of-N outputs with a second rater on part, kappa reported, premise labels for EVL-10). Later: a 30-item open-ended design set with rubric scoring; then the nano-scale rediscovery ladder and nano replicas.

Cost. Defined in plan.md: input plus output tokens of every model call (orchestrator-side scripts cost nothing; every judge, verifier, converter, probe and embedding call counts), system-prompt overhead included, cached input at full price, encode tokens, offline tokens amortized per item. B = m x median plain-CoT tokens. Best-of-N arms stop at the scaffold's realized spend per item. Realized spend is reported beside the cap.

Arms at matched cost: plain; best-of-N (majority vote); best-of-N with the same /verify; seeded best-of-N with the same /verify (primary null is the stronger of these two, chosen per benchmark on dev); instruction-only; scaffold; described-strategies ladder (L0 one context with the menu, multi-turn with a fixed "continue" message, unused budget logged; L1 N contexts with the menu; L2 N contexts with assigned card text and no routed views; L3 the scaffold; all with the same tools, converter and /verify selection, in-context winner choices discarded; menu rendered from the card YAML with shuffled order per replicate); per-card generic-instruction substitution (P1); memory snapshot arms at 0/100/300/600 train rows and empty memory (P1); retrieved-document pack seed arm (SOC-02, P1: concept seed vs document pack vs none); profession-label vs content-only pack arm (I6 step C, P1, harness-only lint exemption).

Pruning regret (I4, P0 diagnostic, next to the MSR-05 coverage vs selection decomposition). `harness/measure/pruning_regret.py` reads the ledger and the run's candidate files, checks every generated candidate against the key offline on keyed items only, and never feeds anything back into a run. Per benchmark it reports the correct-but-pruned rate (items where a key-correct candidate existed in the pool but was not returned, divided by keyed items), split by cause: (a) never verified (outside top-m_verify by conf), (b) evicted from `state.pop` by k_pop, (c) never chosen as a revise parent; and the late-winner rate (verified final solves whose lineage was not top-ranked after round 1); item-cluster bootstrap CIs. Rule: if (a)+(b)+(c) is below 5% of items on dev-tune for ARC-style and MacGyver-labelled items, I4 step 2 (frontier, verify_order) is not built. Its late-winner rate is also the first evidence on whether the I3 convergence feature can carry signal.

Ablation schedule. Every P0 and P1 ablation named in SYNTHESIS.md has one slot; `harness/plan.md` copies this table. Stage 2 arm: runs with the arm set before the gate, not under the leave-one-out cap. Pre-gate: leave-one-out on dev-ablate under the MSR-12 cap (P0 cards plus the 4 named flags) and the keep/drop rule. Post-gate: after the Stage 3 go/no-go and before Stage 4, under the same keep/drop rule; P1 flags stay off in the gate configuration. Sweep: tuned on dev-tune, not a keep/drop decision. Exempt: convention or integrity rule, metric must be 0 or 100%.

| Mechanism | Ablation or arm | Priority | Slot |
|---|---|---|---|
| low_prior card (REP-02) | portfolio minus low_prior at equal tokens | P0 | pre-gate (card) |
| transform card (GEN-12) | portfolio minus transform | P0 | pre-gate (card) |
| formal card (REP-03) | formal plus prose vs prose only on the formalizable subset | P0 | pre-gate (card) |
| revise card (GEN-14; REP-04, REP-07 via revise) | scaffold minus revise | P0 | pre-gate (card) |
| seeded card (GEN-17) | never ablated; seeded best-of-N is its contrast | P0 | Stage 2 arm |
| Stagnation reset (CTL-11) | fresh reset without failures vs no reset | P0 | pre-gate flag 1 |
| Stop rule (CTL-05) | stop rule vs no early stop | P0 | pre-gate flag 2 |
| Dedup (CTL-10) | dedup off; threshold sweep | P0 | pre-gate flag 3 (sweep on dev-tune) |
| Fact shuffle (REP-08) | shuffled vs canonical order | P0 | pre-gate flag 4 |
| Pressure lint (STA-02) | neutral vs high-pressure wrapper | P0 (lint) | Stage 2 arm, first dev batch |
| Best-of-N nulls, instruction-only, ladder L1 (MSR-02, GEN-11, OTH-02) | arms | P0 | Stage 2 arms |
| Budget and round cap (CTL-03, CTL-04) | m sweep; R_max sweep at the largest m | P0 | sweep (Stage 3) |
| Candidates per generator (GEN-06) | 4/8/16 at fixed tokens; 1-per-context arm | P0 | sweep |
| Role separation (CTL-01, STA-01) | merged generate-and-critique context; 2x2 checklist in generator x separate judge context | P0 | post-gate |
| Blind judge (EVL-03) | same-context self-critique | P0 | post-gate |
| Loose generator template (GEN-09) | rubric shown to generators; exec_feedback none/final-only/iterative | P0 | post-gate |
| Isolation and distinct inputs (SOC-01, SOC-02, GEN-10) | isolated vs sequential-shared at fan-out 4; 4 cards vs 4 copies of one card (round 1 only); sequential list | P0 | post-gate |
| Defaults routing (GEN-03) | no defaults list; labels in prompt vs none vs post-hoc routing | P0 | post-gate |
| Confidence use before verification (EVL-01) | warning-only; accept top-ranked unverified; fixed k; peaked k; p_raw in acceptance | P0 | post-gate |
| Verification types (EVL-02) | narrated self-check counts | P0 | post-gate (the llm_falsifier validation itself runs on dev before the gate) |
| Judge and calibration (EVL-08) | random pick among verified vs judge pick; agreement-only vs p_raw-only vs both | P0 | post-gate (judge validation runs in /bench step 4) |
| Checklist (EVL-11) | holistic judge without checklist | P0 | post-gate |
| Absolute bar (EVL-15) | argmax-only | P0 | post-gate |
| Rationale stripping (EVL-16) | judge with vs without rationales | P0 | post-gate |
| Surprise trigger (CTL-06) | surprise-triggered revise vs random revise target vs discriminating probe | P0 | post-gate |
| Admission (CTL-09) | fixed schedule; k_pop sweep 2/5/10 (P1) | P0 | post-gate |
| Fresh revise children (STA-04) | fresh-child chain vs single growing context | P0 (P1 cap) | post-gate |
| Reset family rest (CTL-14, CTL-18) | continue same context; fresh plus failures; verbatim vs restructured prompt | P1 | post-gate |
| Undemanding filler (CTL-02) | undemanding filler vs none | P1 | post-gate |
| Incubation guard (CTL-15) | incubate ablation on convergent items | P1 | post-gate |
| Declining threshold (CTL-05) | declining T vs fixed T | P1 | post-gate |
| Feedback form (STA-07) | deterministic record vs pass/fail bit vs none vs praise vs prose summary | P1 | post-gate |
| Shell access (STA-10) | same card and seed with vs without shell, ARC dev | P1 | post-gate |
| Learned allocation, within-run LP, leave rule (CTL-07, CTL-08, GEN-02) | snapshot curve vs empty memory; reallocation vs static; adaptive vs fixed split | P1 | Stage 3 memory arms (secondary null); the rest post-gate |
| Signature key (REP-01) | family vs signature vs signature plus table vs full text | P1 | post-gate |
| Restructure operators (REP-05, REP-09, REP-11) | each operator removed; relabel vs none | P1 | post-gate |
| Analogy (GEN-08, REP-15) | portfolio minus analogy; far vs near; filter vs none; code vs triple arm | P1 | post-gate |
| Compose (GEN-13) | 2x2 table x compose card; order flag | P1 | post-gate |
| Parent count (REP-07) | 1/2/4/pool parents | P1 | sweep |
| Develop-then-select (EVL-04) | select-then-develop vs develop-top-k-then-select | P1 | post-gate |
| Premise check (EVL-10) | no premise check | P1 | post-gate (MacGyver labelled subset) |
| Perturbation checks (EVL-18) | demos only, no perturbation | P1 | post-gate |
| Counterexample check (SOC-09) | check vs single falsifier; shared vs divergent brief | P1 | post-gate |
| Memory content (MEM-01, MEM-05, MEM-08, MEM-13, MEM-14, MEM-17) | cap 0/2/5-10; case injection on/off; bundle vs none; evidence masked vs raw vs none; traps on/off; paired snapshot deltas and memory-blind share | P1 | post-gate |
| Ladder rungs (OTH-02) | L0, L2, generic-instruction substitution | P1 | Stage 3 arms after L1 (secondary null), outside the cap |
| Population search (SOC-03, SOC-04, SOC-05, GEN-15, EVL-05) | islands vs pooled; record vs none; chosen vs assigned parent; random vs discriminating probe; component ablation | P1/P2 | Stage 4 |
| Retrieved-document pack seed (SOC-02; I6 step A; `flags.seed_type` in {concept, doc_pack}) | concept seed vs document pack vs none at equal tokens, same selector | P1 | post-gate |
| Graph view and persisted clusters (I3; GEN-14, CTL-10) | none; `graph.py --check` must give 100% node and edge completeness | P0 | exempt (diagnostic) |
| Lineage-independence feature (I3; EVL-08, CTL-06) | agreement-only vs agreement + raw cluster size vs agreement + n_independent_roots (+ nonseeded), held-out Brier and AUROC per vtype and bin; keep only if it beats both | P1 | post-gate (EVL-08 slot); expect a null at Stage 3, rerun at Stage 4 before dropping |
| Complementary parents (I3; SOC-05, REP-07) | largest coverage-union pair vs tournament pair for recombine | P1 | post-gate |
| Pruning regret (I4; MSR-05, CTL-09, EVL-01) | diagnostic: correct-but-pruned rate by cause (a)/(b)/(c) and late-winner rate | P0 | exempt (offline diagnostic on keyed items); gates the next two rows |
| Frontier (I4; SOC-05, GEN-02) | tournament vs smc vs beam_topK at m = 5 and m = 20, graded items only; BRAINTEASER as negative control | P1 | post-gate, only if regret >= 5% with (b) or (c) dominant |
| Verify order (I4; EVL-01) | top_conf vs top_conf_plus_explore at m_verify = 3 | P1 | post-gate, only if regret >= 5% with (a) dominant |
| Unspoken candidates (I5; GEN-06, EVL-16, SOC-07) | P1 diagnostic: unspoken_correct_rate, unverified_correct_rate; P2 arm: harvest off vs on vs extra seeded calls at the same tokens vs instructional control ("also list 3 options you set aside") | P1 diagnostic, P2 flag | post-gate; the P2 arm only if the rate >= 3 points |
| prior_map fold (I5; GEN-03) | routing agreement with defaults.json >= 90%; then defaults call vs fold at equal tokens | P2 | after the gate |
| Lemma pool (I1; MEM-02, REP-07, CTL-07 motivation) | scaffold minus lemma; (a) no lemma_check, (b) placebo lemmas from a same-family item, (c) discrim filter off, (d) lemma_progress on vs off, (e) lemma card vs the same share given to revise | P1 | post-gate (ARC and the formalizable subset); prior of no effect |
| Decompose (I2; CTL-07, GEN-13, EVL-11) | portfolio with vs without the card; single-context decompose-then-solve rung (Pr13); on-failure vs always-eligible trigger; MacGyver 2x2 with compose; sweeps K {1, 2, 3}, P_max {2, 4}, script vs random combination pick | P1 | post-gate (ARC formalizable subset, MacGyver, Stage 4 diffs); prior of no effect |
| gap_pack (I6; SOC-02, GEN-08, REP-02) | off vs gap_keyed; gap_keyed vs goal_keyed (decisive); 2x2 pack content (gap-matched vs random field of equal length) x gap list (shown vs hidden); pack-brief critics (SOC-09 extension) | P1 | post-gate (MacGyver labelled subset, design set); prior of no effect |
| Profession label vs content-only pack (I6 step C; MSR-03 vs Pr10) | pack only vs pack + field label vs label_only, harness-only lint exemption that never ships | P1 | post-gate, same slot as gap_pack |
| P2 items (GEN-01, CTL-13, CTL-17, EVL-09, MEM-02, MEM-06, MEM-09, MEM-15, MEM-16 principle, REP-04 stand-alone, REP-10 cues, STA-13, CTL-18 other filler types, GEN-18) | as in their SYNTHESIS rows | P2 | after the gate, each its own arm |
| GEN-07, MEM-10, REP-16, MEM-11 ledger | none | P0/P1 | exempt (routing invariant, lint, return contract, append-only ledger) |
| Pr10 unspoken-candidates wording lint (I5 part D) | none; lint pass 100% on templates, runtime hit rate on rendered prompts logged | P0 | exempt (lint) |

Splits: train (family-interleaved; writes views only), dev-tune (calibration, parameters), dev-ablate (keep/drop), test (used once), transfer (different families), OOD (structurally deeper than any memory entry). Replicate = an index that sets input seeds and permutations for every arm; model nondeterminism is noise. 3 replicates on dev, 5-10 on test. Dev subset about 150 items stratified by difficulty. Total run count and token budget written in plan.md: m sweep for scaffold and primary null only; R_max sweep for the scaffold at the largest m only; ladder at 1x only, 0.5x and 2x added if the 1x CI excludes 0; ablations at 1x with 3 replicates.

Metrics:
- Primary: ground-truth solve rate on keyed benchmarks, paired difference vs the stronger null, 95% cluster-bootstrap CI over items with replicates averaged within item (MSR-01, MSR-02).
- Solve-vs-cost curves across m (CTL-03).
- Coverage (oracle pass@pool, keyed benchmarks; 20% MacGyver subsample with the evaluation judge) vs selection accuracy; pass@k from replicates; share clearing a fixed high bar; P90 on rubric-scored items only (MSR-05).
- Pruning regret (I4): correct-but-pruned rate by cause (a) never verified, (b) k_pop evicted, (c) never revised, and late-winner rate, as defined above; expected to fall under the frontier and explore arms if they are built.
- Unspoken candidates (I5, P1): unspoken_correct_rate (items whose correct answer appears only in unspoken spans) and unverified_correct_rate (items whose correct answer was spoken but never got an m_verify slot) as a third term of the coverage/selection decomposition; dedup rate of unspoken against spoken; refusal rate (reasoning_extraction).
- Graph (I3): node and edge completeness (must be 100%); per cluster n_members, n_independent_roots, n_independent_nonseeded; lineage depth per solve.
- Owner-idea cards (P1): lemma: share of verified answers whose lineage contains a verified lemma, discrim distribution of accepted lemmas, rate of verified lemmas that fit the demos but not the test pair (harness-only); decompose: comp_gap rate (all part_tests passed, whole check failed), plan parse-failure and P_max-overflow rates, stratified by a pre-tagged compositional item flag; gap_pack: gap closure (share of round-r uncovered constraint ids covered by a passing candidate in round r+1) per 1k tokens, functional diversity against the Pr10 permutation null, and the "matches an encode default" covariate per arm; for the pack-brief critics, AUROC of confirmed-objection count on the labelled MacGyver subset.
- False-acceptance rate by verification type, with llm_falsifier and llm_consensus in their own strata (EVL-01, EVL-02).
- Calibration: AUROC, Brier, adaptive-bin ECE of agreement and of p_raw per difficulty bin (0, 1-4, 5 of 5 plain solves), minimum 50 items per cell; length-invariance probe on un-normalized inputs; self-preference probe (EVL-08, MSR-04, EVL-03).
- Selective accuracy: accuracy-coverage curve, abstention precision, forced-choice items scored both ways (CTL-05).
- Transition matrix from the scaffold's round-0 candidate to its final answer, net correction above the two-replicate churn null, per benchmark (MSR-07).
- Per-card and per-operator verified win share by class and round-type; directed-card share of wins (GEN-17).
- Transfer: held-out solves per token vs snapshot size; empty-memory null; OOD delta; share of held-out items whose class has N_min rows (test uninformative below about 30%); paired diversity and coverage delta snapshot vs empty; memory-blind wins per call vs 1/n (MSR-11, MEM-17).
- Diversity on candidate pools: distinct answer clusters (BRAINTEASER, MacGyver), distinct test-output grids (ARC), pairwise embedding distance (pinned local model), cluster count, length-normalized distinct-2, each vs a permutation null over agent labels; agree = 3 of 4 with p < 0.05; per-lever report (shuffle, seed, card) (MSR-14, SOC-07, MSR-03).
- Surprise precision and repr_change policy effect (MSR-08).
- P2: originality = mean embedding distance of each deduplicated candidate to the plain-arm pool for the same item, and fluency = distinct count after dedup (`harness/metrics/originality.py`), reported beside verified solve rate on keyed benchmarks and beside judge-panel score on the design set (STA-16).
- P2, design set only: disposition profile per ablation, fertility = distinct ideas after dedup, originality = distance from the /encode defaults, non-copying = 1 minus max overlap with retrieved memory items or seeds, motivation = share of lineages developed through >= 2 passing revise steps (MSR-10).
- Integrity: role-leakage rate, return-contract violations, routing-invariant violations, verifier hash mismatches, decision-log completeness (all must be 0 or 100%), lint pass.
- Cost: realized tokens and wall-clock per item and per solve, encode and offline tokens separately.
- Stage 4: validation-loss gain of rediscovered diffs per GPU-hour and per LLM token vs the project's own baselines. Stage 5: a verified improvement under the e-value verdict (docs/VERDICT.md) that survives one scale step.

Decision rule: a card or flag stays only if its leave-one-out ablation on dev-ablate gives P(helps) > 0.95 under a Beta(1,1) prior on discordant pairs, "helps" = ground-truth solve rate per item at matched cost vs the full stack minus the flag, accumulated only across batches that share a memory and calibration snapshot, with the number of batches fixed in advance; pairs stay only if they beat each component (MSR-12, MSR-18). Superiority tests are one-sided; equivalence claims require a TOST within a preregistered margin (3 points, placeholder). Fidelity to the brain is never a reason.

---

## 9. Build order

1. `harness/plan.md`, cost definition, splits, replicate scheme, result and cost schemas, `harness/lint.py` with patterns (including the Pr10 unspoken-candidates wording rule, I5 part D), `harness/embed.py` with a pinned local model. Plain and best-of-N (vote) arms. Headroom pilot; baseline numbers and noise floor; power calculation.
1b. Free items, 0 LLM tokens, built before any card: `harness/graph.py` with `--write`, `--render` and `--check` plus persisted `clusters.jsonl` from dedup (I3, P0); `harness/measure/pruning_regret.py` (I4 step 1, P0 diagnostic; it decides whether frontier.py is built at all); the SOC-02 retrieved-document pack written into /generate's input, the layout and the ablation schedule (I6 step A, documentation only).
2. `harness/run_card.py` with sandboxing, tool allowlists, templates, return contract, prompt logging. `/encode` (merged checklist, bar as data, private defaults, validated hashed verifier model, self-contained facts, views, encode cap) and `/verify` (model execution, demo match (perturbation checks at P1), checklist, diverse falsifier attempts, verification-type split, `feedback.py`). Best-of-N and seeded best-of-N with the same verifier; instruction-only arm; pressure-wrapper arm in the first dev batch, beside the lint (STA-02).
3. `/judge` (pointwise or doubly-permuted batches, deterministic truncation, p_raw logged); agreement probe; validation on dev-tune; self-preference and length probes; first calibration map on agreement only.
4. `harness/think.py` with allocate, dedup (pre-dedup rate), admit, stop (fixed T, opt-out, abstention), stagnation (unused tuples, masked evidence); `/generate` with P0 cards (seeded, low_prior, transform 3-call, formal with exec_feedback, revise 1-parent). Scaffold arm; ladder rung L1. Pre-gate ablations on dev-ablate: P0 card leave-one-outs and the 4 named flags of the section 8 schedule.
5. Ledger and `harness/stats.py`; Thompson allocation per cell once N_min rows exist; versioned views; snapshot arms; family-interleaved train sequences; regression set.
6. P1: the /verify step 6 discriminating test between rivals first, moved ahead of the other P1 items for ungraded items (I4 decision); then analogy (code arm and triple-check arm), relabel, compose, revise 2-parent operators, `/restructure`, premise check, counterexample check, traps, case bundles, signature with its key ablation, ladder rungs L0 and L2 and the substitution ablation, reset ablation family, undemanding-filler-vs-none arm, feedback-form arms, same-card shell ablation (STA-10), context bounds. MacGyver human labelling. Their ablations run post-gate per the section 8 schedule.
6b. P1 owner-idea items, after the gate configuration is frozen and each behind its flag with a prior of no effect: `flags.lineage_independence_feature` in calibration and `flags.complementary_parents` in tournament.py (I3); thinking capture to `calls/<id>/thinking.txt`, `harness/harvest.py` and the unspoken_correct_rate diagnostic (I5 part A); the decompose card with the `foreach` schema step and `harness/compose_parts.py` (I2); the lemma card with `harness/lemma_check.py` and `state.lemma_pool` (I1, arm (e) against revise-with-recurse first); `harness/think/frontier.py` and `flags.verify_order` (I4 step 2, only if the pruning-regret diagnostic shows >= 5% regret); `memory/seeds/docs.jsonl` and the document pack seed arm (SOC-02); `memory/domain_packs.jsonl`, `gaps.json`, the gap_pack card and the profession-label vs content-only arm (I6 steps B and C, arm gap_keyed vs goal_keyed first).
7. Stage 3 go/no-go on the test split.
8. `/experiment` with islands, tournament and hunk contributions on the nano-scale rediscovery ladder (Stage 4), then nano replicas (Stage 5).
9. P2 flags only after the gate: audited case principles, schema library, suppression trials, retry after memory update, wander arm on the design set, seed counts, other filler-type arms (CTL-18, STA-05), sparse card, dormant re-scoring, originality and disposition metrics (STA-16, MSR-10); the `flags.harvest_unspoken = merge` setting (I5 part B, only if unspoken_correct_rate >= 3 points); the prior_map fold of the defaults call (I5 part C, after the 90% routing-agreement check). Interpretability tools (logprobs, lenses, probes, attribution graphs) are not in any stage; see the Stage 5 note in section 10.

---

## 10. Known limits and open questions

- Skills shape the model's trajectory through what it already knows; they add control and verification, not capacity. The target is verified novel problem solving at matched cost, not general intelligence.
- Claude Code exposes no sampling temperature or seed. Diversity comes only from inputs; whether that breaks same-model homogeneity is measured per lever (SOC-07), not assumed. Replicates are input-seed indices, and model nondeterminism is treated as noise.
- Same-model judges, falsifiers and critics share priors with the generator. Fresh contexts remove authorship but not bias; the judge is probed against human reference solutions, adversarial-LLM verification is its own stratum, and executable checks override it wherever they exist.
- The driver assumes the CLI reports per-call usage in JSON output and honours per-role tool allowlists; if either is missing the fallback is direct Messages API calls. `claude -p --output-format json` is verified working (2026-10-10), with about 26k tokens of fixed system-prompt overhead per call; the Messages API backend via the anthropic SDK is preferred when `ANTHROPIC_API_KEY` is set and is the backend under which the matched-cost comparison is cheapest.
- The Claude API exposes no logprobs, no activations and no raw chain of thought, only summarized thinking. Nothing in this design reads model internals; "unspoken candidates" are new text samples harvested from a thinking summary, not readouts of a computation, and the faithfulness literature (IDEAS.md I5) says self-reports are often unfaithful. Whether `claude -p` exposes thinking text at all is unverified and must be checked before I5 part A is built; the fallback is the Messages API backend. Interpretability tools (logit or tuned lens, probes, SAEs, attribution graphs, forking-token resampling) belong to a separate open-weight-generator study after Stage 5, outside every gate (Stage 5 note).
- The owner-idea items I1-I6 start from a preregistered prior of no effect at matched compute: budget-matched studies find that tree or graph structure, decomposition, lemma libraries and inspiration sources often lose their gains once the baseline gets the same budget and verifier (IDEAS.md evidence grades). They are off in the gate configuration and decided only by the section 8 keep/drop rule.
- The pruning-regret diagnostic may show near-zero headroom, in which case the frontier resampler and the explore slot (I4 step 2) are never built; an early null on the lineage-independence feature (I3) is expected because trees are shallow before Stage 4 and must not be read as a drop decision.
- The rendered graph page invites feeding lineage or convergence information back into generator prompts; the routing table and the run_card.py copy lint forbid it, and the invariant is audited at 0 violations.
- Benchmark headroom is unknown until the pilot runs; BRAINTEASER and ARC-1 may be near ceiling or contaminated, and the gate item set and power calculation are provisional.
- MacGyver cannot be scored without human labels; until the subset is labelled, its metrics are unmeasured and it is secondary.
- The realized cost of a scaffold run under the caps, including subagent system-prompt overhead, has not been measured; the caps bound it and the harness reports it.
- The calibration map is fitted on a dev-tune split that may be too small per verification type and bin; the fallback is agreement-only confidence, and p_raw is never used below the preregistered AUROC.
- Strategy posteriors per class may stay flat at the ledger volume one benchmark supplies; the family key at P0, the class-coverage share and the snapshot curve make this visible rather than hidden.
- Open-ended design problems have no ground truth; the evaluation judge plus premise check is the only selector there, and the design set is not part of the Stage 3 gate.
- Abstention can lower headline accuracy on forced-choice items; both scorings are reported.
- Whether any incubation mechanism beyond a context wipe helps an LLM is unknown; the reset family tests the components, each with a prior of no effect.
- Population search mechanics (islands, tournament, hub cap) are untested below Stage 4; the nano-scale rediscovery ladder is their first test.
- Stage 5 gains at 20M parameters may be below seed noise; null results are reported as null results (EXPERIMENT_PLAN section 7).
- The synthesis grades about forty catalog rows lower or narrower than `mechanism_catalog.md` does; the catalog has not been edited and the two disagree until it is.

---

## 11. Changelog

### v0.3 (2026-10-10): owner ideas I1-I6

Decisions by the project lead on the six owner ideas reviewed in `IDEAS.md`; where they differ from IDEAS.md, the decisions here win. v0.2 is preserved at `ARCHITECTURE_v0.2.md`.

- I3 graph: adopted now (P0). think.py appends `runs/<id>/clusters.jsonl` (membership) at the dedup step instead of keeping only dup_rate; `harness/graph.py` writes `runs/<id>/graph.jsonl` (nodes, edges, per-cluster root counts) after every cycle at 0 LLM tokens and renders `graph.html`; each file has one writer; convergence counted by independent roots enters calibration only, behind `flags.lineage_independence_feature` (P1), under the p_raw entry gate; `flags.complementary_parents` tournament rule is P1. The graph is never routed into any generator prompt (routing table row, copy lint). Ablation rows and section 5 rows added; the view itself is exempt with a 100% completeness metric.
- I4 superposition: the diagnostic is adopted now (P0, 0 tokens). `harness/measure/pruning_regret.py` reports the late-winner rate and the correct-but-pruned rate by cause from existing run data on keyed items, offline, never fed back. The frontier resampler (`harness/think/frontier.py`, verifier partial scores only, `flags.frontier` and `flags.verify_order`) is P1 post-gate and is built only if the diagnostic shows at least 5% regret; K stays tied to the revise cap, a frontier never crosses a reset. Tree of Thoughts with LLM-scored steps stays rejected; no card text asks the model to hold hypotheses in superposition.
- I6 professionals: step A now, the SOC-02 retrieved-document pack is written in as a seed type in /generate's input, as `memory/seeds/docs.jsonl` in the layout, as a routing row and as a section 8 ablation row (documentation drift fix). Step B is P1 behind `flags.gap_pack`: `memory/domain_packs.jsonl` (about 50 fields, third person, linted against role phrasing), `gaps.json` from /verify coverage, and the gap_pack card retrieved against what the candidate pool fails to cover, MacGyver and design set only. Step C is a P1 ablation arm, profession label vs content-only pack, under a harness-only lint exemption. No persona, no new role.
- I5 unspoken candidates: part D now, the Pr10 lint fails "subconscious", "free-associate" and hidden-reasoning wording in templates and design text, and the design text calls the object unspoken candidates. Part A is P1: thinking capture to `calls/<id>/thinking.txt`, `harness/harvest.py` producing `cands/<call>.unspoken.jsonl` with an origin field, the cands schema field origin, and the unspoken_correct_rate and unverified_correct_rate diagnostics; thinking.txt is private in the routing table. Part B (`flags.harvest_unspoken = merge`) is P2, gated on a 3-point rate. Part C is P2: fold the defaults call into `private/prior_map.json` after the 90% routing-agreement check. Interpretability tools are a Stage 5 note only.
- I2 decompose: P1 post-gate card `memory/strategies/decompose.yaml` with a `foreach` schema step, `harness/compose_parts.py`, K = 2 attempts per part, script assembly with a combination cap of 16, acceptance only on whole-problem verification, part_tests prune but never accept; eligible from round 2 and in `fresh_tuples`; ARC formalizable subset, MacGyver and code diffs only, never BRAINTEASER; cost reallocated within B; ledger fields n_parts, mode, K, combos_run, combo_pass, comp_gap; ablation row with the single-context rung and the trigger contrast.
- I1 lemmas: P1 post-gate card `memory/strategies/lemma.yaml`, `harness/lemma_check.py`, `runs/<id>/lemmas.jsonl`, `state.lemma_pool` with at most one build call per round and the reset-crossing rule (predicates only, cosine lint); ARC and the formalizable subset only; the model never proves its own lemmas; a preregistered prior of no effect at matched compute; ablation row with arms (a)-(e) and the test-pair diagnostic.
- Elsewhere: section 1 Pr10 adds the retrieved-document pack to the input list and carries the I5 part D lint rule text; section 2 diagram and layout list the new files and scripts (graph.html, arc_exec.py, data/, the foreach schema field, the backend field in state.json, the D: storage note); section 3 /bench step 3 lints domain_packs and step 7 adds graph completeness, pruning regret and the unspoken metrics, /ledger step 1 lists the origin and per-card fields, and the cands schema gains decomp_id, pack_id, gap_ids and origin; section 4 carries the graph write, the lemma claims and build hooks, the frontier and verify_order hooks, the harvest step in collect and the gap writer, all flagged; section 5 gains one row per new parameter, provenance placeholder unless IDEAS.md gives a source; section 6 routing table gains rows for lemma predicates, part spec, gap ids plus pack, document pack, graph and clusters, and thinking.txt; section 7 offline step 5 lints domain_packs and the unspoken wording rule; section 8 adds the pruning-regret paragraph, the document-pack and profession-label arms, the I3, I4, I5 and owner-card metric bullets, and the schedule rows for the owner ideas and the Pr10 lint; section 9 inserts the free items at 1b and the cards at 6b; section 10 adds the no-internals, thinking-exposure, prior-of-no-effect limits; the research basis cites IDEAS.md and states that I1-I6 are owner-idea ids, not catalog ids.

### Consistency pass (2026-10-10)

Loop: `state.spent` now adds the usage of encode (before the loop), the verifier build, the agreement probe, the judge, every verify attempt and restructure, not only generators; the probe runs once per problem and is cached; est_cost and est_verify are defined in plan.md and section 5. The revise queue is merged into the spawn list after round 1 (at most 2, surprises first, then a tournament); restructure variants reach reset generators through `fresh_tuples`; `used_tuples` is updated at every spawn. A `best_checked` track behind `flags.llm_falsifier_validated` with threshold T_checked gives checked candidates a stop path; stagnation on ungraded benchmarks counts only new verified or bar-clearing candidates. conf and agreement are kept per candidate id; p_raw comes from J; `best()` orders by stratum then calibrated P; the CTL-04 guard (no reset for R_max <= 2) is in the code; the invalid `finally` is a comment; eps and max_spawns_per_round are in section 5.

Bar and benchmarks: the BRAINTEASER answer key is removed from every in-loop input and used only by the harness scorer; its bar uses checked types or agreement only; the routing table gains an answer-key row; transform's drop rule is scored against ground truth by the harness.

Rules and schedule: the GEN-17 directed-card rule is restated per benchmark (all applicable P0 directed cards, at least 2) and n0 derived from it; an ablation schedule in section 8 gives every P0 and P1 ablation a slot, names the 4 pre-gate flags and marks exempt mechanisms; STA-01, STA-16, MSR-10 and REP-04 are cited; the filler arm is P1 for undemanding filler vs none and P2 for other types; the pressure-wrapper arm moves to Stage 2; the STA-10 citation leaves /generate step 2 and its shell ablation is a P1 arm; unmarked numeric defaults are added to section 5 as placeholder or design cap; the encode cap is credited to the Representation design notes and Decision 3; the table pipe in the T row is removed; principles are renamed Pr1-Pr19.

### From the pre-review v0.2 draft (2026-10-10) to this version

Control loop: `/think` is now a SKILL.md that launches `harness/think.py`; every decision (allocation, dedup, admission, stop, stagnation, verification order) is python over the run's jsonl files. Cards are executed by `harness/run_card.py` from fixed templates with per-call sandboxes, per-role tool allowlists, a return contract and prompt logging. The 100-word pointer workspace file is removed; the orchestrator holds no context.

Verification: types split into external (verified) and adversarial-LLM (checked); a falsifier pass never makes "verified"; attempts are diverse fresh contexts capped at 3; judge confidence is used only before verification; acceptance and the stop rule depend on verification type and agreement; the suddenness flag is dropped; the checklist is built from two merged encode calls; the verifier model is validated, hashed and read-only; ARC uses perturbation checks instead of leave-one-demo-out re-induction; premise checks distinguish sourceable from commonsense premises; the critic-defender-judge exchange is replaced by a tool-checked counterexample test.

Cost: B defined as m x plain-CoT tokens with a full cost definition, per-spawn budget checks, m_verify = 3, k_max = 3, revise spawns <= 2 per round, R_max default 3, encode cap, offline amortization; best-of-N arms stop at the scaffold's realized spend.

Generation: defaults withheld from all generators and used by script downstream; transform is a 3-call DAG with a back-mapping revise step and script-chosen operators; revise operators split by parent count (1 at P0, 2 at P1) with per-benchmark feedback and no revise on BRAINTEASER; the seeded card is the undirected control share; exec_feedback flag on the formal card; output as a numbered list split by script; abduce-probe restricted to interactive domains; analogy from a fixed domain corpus with a code re-encoding arm; relabel and compose use physical-property schemas with lints; candidate count is a swept parameter.

Memory: cases are script-built bundles at P1 and LLM principles move to P2 under audit; traps are script-built views, never training data, and never reach generators; a routing table is enforced by the driver; the injection cap is 2 per run in one generator; the memory-blind generator's card is uniform random; views are versioned per batch; the transfer metric is a snapshot curve on fixed held-out items against empty memory; an explicit train split exists and dev is split into dev-tune and dev-ablate; the regression set is sized and its block test preregistered; evidence has a schema and candidate spans are masked.

Measurement: primary outcome restricted to keyed benchmarks, MacGyver secondary on a human-labelled subset; headroom pilot; go/no-go against the stronger of two best-of-N nulls; cluster bootstrap over items; Beta(1,1) on discordant pairs with P(helps) > 0.95, fixed batch count, snapshot-aligned accumulation; diversity on pools only with a permutation null; first answer from the scaffold's own round 0 against a churn null; difficulty bins and cell minimums defined; answers extracted rather than rewritten; described-strategies arm rebuilt as a four-rung ladder with superiority and equivalence tests; instruction-only and generic-substitution arms restored; total run count bounded.

State and social: pressure lint narrowed and its arm moved to the first dev batch; feedback to revise children is a deterministic script record with information-content arms; context bound by construction; STA-13 is a P2 flag everywhere; islands, tournament and hunk-contribution rows moved to Stage 4 with schema fields; SOC-05's chosen-vs-assigned contrast is an arm; Stage 3 social test limited to isolated vs sequential-shared at fan-out 4.

Staging: Stage 4 restated as nano-scale rediscovery of record diffs against the project's own baselines; ladder rung L1 added to the Stage 2 deliverable; principles Pr1, Pr7, Pr8, Pr13, Pr15, Pr17, Pr18 rewritten; the thesis caveat corrected; the frontier-system claim marked unsourced; every unsourced numeric default marked placeholder with a provenance column.

### From v0.1 (2026-10-08)

Thesis and staging: new section 0 states the claim, design hypothesis, prediction and falsification; new Targets and staging section lists the five stages and gates.

Principles (v0.1 numbers, renamed Pr here): Pr2 (two foraging modes as instructions) dropped, replaced by budget allocation between fresh and revise children, credited to CTL-08 (GEN-02's task-type routing was dropped, not replaced). Pr4 (distance window as filter) dropped to a diagnostic (EVL-09). Pr6 (spontaneous-thought trajectory) deferred to a harness arm (GEN-04). Pr5, Pr7, Pr8, Pr9, Pr11 rewritten in structural form. New Pr13 to Pr19.

Skills renamed or changed:
- /forage renamed /generate: executes one strategy card per sandboxed call; persistent and flexible modes removed; no rubric; revise card added.
- /analogize removed as a skill; it is the analogy card inside /generate at P1.
- /evaluate renamed /judge: blind, pointwise, p_raw logged; distance window removed; never the final word when a verifier exists.
- /insight-check renamed /verify: builds and validates the verifier, splits verification types, diversifies falsifier attempts, checks premises.
- /wander deferred (not built); exists as a flagged arm.
- /restructure kept in name, moved to P1, operators changed to re-add dropped elements, relabel, transform, with script-computed inputs.
- /incubate reduced to a P2 flag (retry after memory update); the within-run fresh return is the stagnation reset.
- /consolidate kept in name as the offline phase; writes only script-derived versioned views; no LLM-written memory text before P2.
- /think kept in name; now a launcher for the python driver.
- New: /bench (harness as the first deliverable), /ledger (P0 rows), /experiment (Stage 4-5), strategy cards as versioned YAML procedures with templates.

Harness: arms expanded from baseline plus full HTSA to the arm list in section 8, including two best-of-N nulls, instruction-only, the ladder and snapshot memory arms; coverage vs selection decomposition; transition matrix; calibration per bin; preregistered keep/drop rule; family-interleaved train sequences with OOD splits.

Memory: v0.1 semantic and episodic prose stores replaced by an append-only ledger with versioned numerical views, traps, calibration map and card library; verified-only writes; memory-blind agent and injection cap; credit only on held-out snapshots.

Removed as uncalibrated priors: the [0.5, 1.0] distance window and the fixed 2+2 forage split.

Other v0.1 content replaced or dropped:
- Switch budget (default 4, one count per DMN-ECN pass of the loop): replaced by the round cap R_max (default 3, placeholder, swept) plus the stagnation reset; switches are no longer counted, since every round's allocation is a logged script decision.
- /evaluate verdicts solved / promising / impasse, with "promising -> forage again seeded from shortlist": replaced by verification status (verified, checked, fail, unverified), the script stop rule and the admitted population; re-foraging from a shortlist is replaced by revise children built on failed candidates with their feedback record (GEN-14).
- Evaluation criteria integration, effectiveness and testability: replaced by the checklist conjunction bar (effectiveness = clears the bar, EVL-15) and a testable claim that /verify derives for every candidate (testability); integration is dropped as a judged criterion because its neural support is weak (EVL-11) and constraint coverage is scored item by item instead.
- Proactive once-per-run /restructure (Ross & Arfini 2024): dropped; /restructure (P1) runs only on the stagnation trigger, because a proactive call has no driving signal to log and no catalog-backed ablation; it can return as a flagged arm.
- /wander constraint-level schedule (high early, low during incubation): dropped with /wander's deferral; a constraint level has no operational definition without temperature control, and the loose-generation question is tested by the STA-01 2x2 instead.
- False-insight rate: replaced by false-acceptance rate by verification type, with llm_falsifier and llm_consensus in their own strata (EVL-01, EVL-02).
