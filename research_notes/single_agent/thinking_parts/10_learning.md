# 10. Learning and adaptation

*2026-10-14. Part 10 of the thinking decomposition. Grades: **strong** = meta-analysis or two or more independent controlled studies; **medium** = one controlled study with ablations; **weak** = single run, no ablation, self-reported metric, or theory carried over by analogy. Every source was fetched this session unless marked (R), relayed from an earlier brief. Web search ran out of budget mid-session, so 2026 coverage is limited to papers surfaced by earlier briefs or known by ID; a follow-up search on lesson stores and incident post-mortems is still owed.*

## Bottom line

The loop records outcomes but does not learn from them. Written lessons help when they are small, itemised, scoped, and scored by later verified outcomes. They do nothing, or harm, when the model writes them from its own judgement, when they are bulky, or when a whole document is rewritten. Credit to processes (cards, questions, analogies) cannot be read off by an LLM and cannot be tested on verified wins at our volumes. It has to come from logged provenance, continuous rung metrics, shrinkage and an exploration floor, then be checked by run-level A/B. Structured reviews on objective data work for human teams; the same shape fits a script-first review here.

## 1. Where the loop stands (code)

- **Within a run:** `history_text` (last 40 builds with status, gap, prediction check) feeds later sketches and interrogations; assumptions found by questioning flow back into the map.
- **Across runs:** ledger verdicts become "tried before" lines in every brief (`inject_ledger`); `verified_by_hash.json` skips repeats per baseline version; the novelty gate reads ledger texts; `promote.py` archives a winner with hypothesis, change, hash and verdict, but not how it was found.
- **Calibration:** `calibrate.py` gives log-odds per cluster feature (angles, prior, obvious, departure, size) against *checked* (a rung-3 pass), from five builds per bucket, with no shrinkage or interval; it acts only with `--weights-from-ledger` and 100 builds. `novelty.attractor_cards` retires cards on distinct-cluster yield (diversity), never on outcome, with four cards hard-coded exempt.
- **Data today:** the ledger holds two mock rows; the two real runs hold seven ladder records and no overnight verdict.
- **Absent:** lessons as lessons; item-level provenance (which questions, facts, analogue and objections the builder saw; selection probabilities); credit per card, lens, question or analogue; a post-run review; transfer between problems.

## 2. What the evidence says

**Lessons without weight updates**
- Itemised, outcome-anchored memory helps. ExpeL (ADD/EDIT/UPVOTE/DOWNVOTE rule counts): HotpotQA 28 to 39%, ALFWorld 40 to 59%; insights alone (36/50%) and recalled trajectories alone (31/55%) each trail both; hand-written insights reach only 32%; retrieval by task similarity beats random (59 vs 42.5%) [S2, medium]. ACE keeps bullets with helpful/harmful counters, merged by non-LLM code: +10.6% on agents, +8.6% on finance [S1, medium]. AWM +24.6% and +51.1% relative [S8, medium]. ReasoningBank gains 4.6 to 8.3 points on WebArena; failures help it (46.5 to 49.7) but hurt AWM (44.4 to 42.2), so the memory form matters [S9, medium].
- Without a reliable external signal it fails. Intrinsic self-correction can degrade reasoning [S4]; it works with reliable external feedback or fine-tuning [S5] (together strong). Reflexion reached 91% on HumanEval, where unit tests exist, but not on WebShop, nor with a weak model (0.26 to 0.26); its test evaluator had 16.3% false positives on MBPP [S3, medium]. Self-written skills gave no benefit (24.3% none, 40.6% curated, 21.5% self-generated; 7,308 trajectories); 2 to 3 focused skills gave +18.6 points against +5.9 for four or more [S6, medium]. Repository context files did not generally raise success and added over 20% cost [S7, medium]. ACE without labels fell on FiNER (70.7 to 67.3) [S1].
- Lessons rot. Rewriting the whole context collapsed 18,282 tokens (66.7%) to 122 (57.1%), below the 63.7% of no adaptation [S1]. Wrong memories propagate, and later outcomes can label stored memories [S14, medium]. In autoresearch logs the share of helpful changes fell from 70% to 43% by iteration 6+, and a judge's selective accuracy from 82.8% to 56.9%; a focused memory of similar past attempts restored 83.5% [S31, medium], endpoint 8.4 to 10.7% (R: 09_llm_ideation.md).

**Prompt optimisation from outcomes.** OPRO beat hand prompts by up to 8% on GSM8K, yet training accuracy ran 5 to 20 points above test, near-paraphrases scored 49.4 vs 71.8, and error cases were not exploited [S16, medium]. TextGrad lifted GPT-4o on GPQA from 51 to 55% [S17, medium]. GEPA beat GRPO by 6% (up to 20%) with up to 35 times fewer rollouts; Pareto parent selection beat always-best (+12.4 vs +6.1 aggregate), and merge hurt IFBench (38.6 to 28.2) [S18, medium]. A bilevel loop that writes search mechanisms reached -0.045 vs -0.009 val_bpb; parameter-only tweaks gave no reliable gain; one benchmark [S30, weak].

**Credit assignment**
- LLM attribution is poor: best 53.5% (agent) and 14.2% (step) on Who&When, some methods below chance [S19, medium]; counterfactual replay plus fault injection raised it by up to 18% over frontier models [S20, medium]. Monte Carlo step labels trail judge and human labels [S26, medium].
- Structural credit worked in single-lab results. HGM scores an agent by its clade's success counts and picks by Thompson sampling: correlation with descendants' best 0.51 to 0.87, against 0.27 to 0.44 for own score in DGM and SICA, with 2.4 to 6.9 times fewer CPU hours than DGM [S21, medium]. RD-Agent(Q)'s Thompson scheduler: 14.21% ARR vs 10.09% LLM-chosen and 8.97% random, single runs [S23, weak]. MLE-STAR refines the block whose ablation moves the score most: 43.9% medals vs AIDE 25.8% on the same model, component not ablated alone [S25, weak]. Theory: hindsight credit [S27] and counterfactual baselines [S28] (both RL, theory-grade here).
- Volume is the constraint. DeepScientist: about 5,000 ideas, 1,100 validated, three tasks past the state of the art [S29, weak]. My arithmetic (one-sided alpha 0.05, power 0.8): a 2x lift on a 3% win rate needs about 590 builds per arm; 1.5x on a 30% pass rate needs 128; a continuous outcome at 0.5 SD needs 49 [own calculation, theory].

**Transfer.** ExpeL HotpotQA to FEVER 63 to 70% [S2]; AWM's edge grows from 8.9 to 14.0 points as train-test distance grows [S8, medium]; a DGM agent evolved on one model lifted Claude 3.7 from 19 to 59.5% and o3-mini from 23 to 33%, but an agent evolved on Python only lost ground on non-Python tasks against the all-language agent [S22, medium]. SkillsBench gains run from +4.5 to +51.9 points by domain, with 16 of 84 tasks negative [S6]. Inference: how to search transfers better than what works where.

**Reviews.** Debriefs and AARs: d = 0.79 over 61 studies (915 teams, 3,499 individuals), d = 0.67 for task performance; team alignment and objective review media were the consistent moderators, and structure helped in the military but not in healthcare [S38, S39; strong for humans, untested for LLM loops]. Doctrine is intended vs actual, sustain/improve, no blame; the page cites no effect data [S44, weak]. Small samples invite over-interpretation [S40, theory]. Sleep-time compute (precomputing between queries) matched accuracy with about 5 times less test-time compute on stateful benchmarks, with gains tracking how predictable the query was [S37, medium]. A loop using immutable prediction-plus-outcome cards did not drift, though the cards were not ablated [S35, weak].

**Goodhart and noise.** Standard estimators stay valid for only a linear number of adaptively chosen queries on one holdout; perturbed answers stretch that exponentially [S41, theory]; validation-based selection in long searches overfit through evaluation noise, fixed by hidden consistent evaluation [S32, medium]; pushing a proxy past a critical point lowers the true objective [S42, S43; strong in RL, by analogy here].

## 3. Improvement ideas for this part

Already have, not repeated: version-keyed ledger lines, hash memory, in-run history, novelty gate, diversity retirement, hedge lane, placebo and positive controls. Cost: small = hours, medium = a day.

**I1. Build manifest and selection propensities** [partial: `pool/<id>.json` holds card, lane, target]. *Mechanism:* each build writes `inputs.json`: sketch ids with card, lens, seed, family; analogue id; brief-item, question, fact and objection ids shown to the builder; lane; and the probability with which selection chose it. *Effect:* every later credit step becomes a join, not a guess; propensities allow weighting out selection bias. *Cost:* small. *Measure:* every pool row has a manifest; a past run's prompt inputs can be rebuilt from it.

**I2. Process-credit table with shrinkage** [partial: `calibrate.py`]. *Mechanism:* `credit.py` joins manifests to outcomes and reports, per card, lens, part, lane, analogue band and question type: builds, checked, stackable, verified, mean extrapolated z, tokens per build, with a partially pooled posterior and 90% interval. Target is continuous rung z (validated against overnight rank once about 30 pairs exist), not `checked`; features enter jointly. *Effect:* "no evidence yet" instead of five-build log-odds. *Cost:* medium. *Measure:* leave-one-run-out: does the ranking predict the held-out run's per-card yield, with calibrated intervals, better than uniform?

**I3. Question and chain credit by lineage** [new]. *Mechanism:* credit a question to the offshoot sketches it spawned (`focus`, `parent_cluster`) and their builds; score chains by clade counts over all descendants (revisions, compositions) and choose which to deepen by Thompson sampling. No LLM judges "which question mattered". *Effect:* depth and fan-out follow yield instead of fixed 2 by 1. *Cost:* small to medium. *Measure:* stackable builds per million tokens against fixed depth at matched budget.

**I4. Outcome-driven card allocation with a floor** [partial: round-robin cards, diversity retirement, random long-shot lane]. *Mechanism:* contexts per card by Thompson sampling on posterior stackable yield per million tokens, at least 40% uniform, long-shot lane untouched; retire a card only if diversity *and* outcome yield are low. *Effect:* spend moves to productive cards; the floor limits narrowing and Goodhart on diversity. *Cost:* small. *Measure:* A/B against round-robin at matched budget; regret on logged propensities. Zero influence until intervals separate.

**I5. Counterfactual audit of wins** [new]. *Mechanism:* for each stackable or verified candidate (rare, so cheap), rebuild with one input removed (interrogation facts, analogue, objections; the plain `formal` card) and run rung 3 on the same seeds; record credit as the z change in units of rebuild noise, only if beyond 2 SD. *Effect:* the only causal evidence per input at tiny N. *Cost:* medium (3 to 4 builds per win). *Measure:* agreement between two repeats of one ablation; share of audits crediting an input.

**I6. Post-run review, script first** [partial: `report.py`]. *Mechanism:* `review.py` follows the AAR questions on objective data: expected (selection scores, predictions), happened (funnel, rungs, verdicts), why (surprises beyond 2 SD, objections vs actual failure reasons, novelty-gate and hedge audit rates, placebo false-positive rate), change (at most 5 lesson deltas citing row ids, proposed by one strong-model call, validated and merged by script). Promotion appends a "how found" dossier from the manifest. *Effect:* human debriefs d about 0.7 to 0.8; for LLM loops unproven, expect value from the deltas. *Cost:* medium. *Measure:* pre-registered: share of deltas whose next-run metric moves as predicted, against deltas drawn from shuffled outcomes.

**I7. Lessons ledger with discipline** [partial: ledger lines, history]. *Mechanism:* `lessons.jsonl` of itemised claims with scope (part, baseline version, regime), evidence (cand ids), helpful/harmful counters, state (hypothesis, then supported after two independent builds or one replicated verdict, then rule) and expiry; merged by script, never rewritten by agents. Rendered as numbers for selection, at most 5 implementation pitfalls for the builder, and outcome-only lines for ideation (keeps the no-early-lineage rule). *Effect:* ExpeL- or ACE-type gains if verdict-anchored; otherwise harmless. *Cost:* small. *Measure:* three-way arm: lessons, length-matched shuffled placebo, none; repeat-failure rate; verified per million tokens.

**I8. Two-speed learning** [partial: `_immediate_fix`, revise queue]. *Mechanism:* implementation failures (rung 0 to 2: minutes, hundreds of samples, test-like signal) feed persisted pitfall lessons keyed by failure reason and part, Reflexion-style. Idea-value lessons (rungs 3 to 5) update slowly under I2's intervals. Reflective prompt evolution (GEPA-style) only on script-checkable proxies: sketch parse rate, mapping-lint pass, near-duplicate rate; never on "idea quality". *Effect:* fewer wasted builds. *Cost:* small to medium. *Measure:* rung 0 to 1 failures per 100 builds across runs; tokens spent on failed builds.

**I9. Prediction and critic calibration** [partial: `predict.py`, pre-mortems]. *Mechanism:* score only informative claims (loss gap, not "params unchanged") with an interval score; keep per-card and per-critic tables (did objections anticipate the recorded failure reason?); shrink a card's predicted gain by its past over-prediction before selection; store prediction and outcome append-only. *Effect:* blocks Goodhart on "prediction accuracy" and the confidence cliff [S31]. *Cost:* small. *Measure:* calibration slope of predicted vs measured gap; rank correlation of corrected score with rung z.

**I10. Transfer protocol and guardrails** [new]. *Mechanism:* tag each lesson *content* (baseline- and regime-specific; expires on promotion, then re-queue near-misses against the new baseline) or *process* (cross-problem). A new problem receives process lessons and the store schema, not content. Test transfer on a held-out regime (smaller model, more tokens) with lessons on and off. A lesson needs a fresh-seed or hidden-split confirmation; cap at 12 per part. *Effect:* avoids crediting gains to the distribution that produced them. *Cost:* medium. *Measure:* held-out-regime yield with and without process lessons; stale-lesson rate after promotion.

## 4. Order and rules

Build I1, then I7 with I8's pitfalls, then I6, then I2 and I9. Add I4 and I3 once at least three runs and about 30 overnight pairs exist; run I5 and I10 as arms. A learned component gains influence only when its intervals separate, it beats uniform leave-one-run-out, and a matched-budget A/B is non-inferior. Never let agents edit lessons, never ask an LLM which question or analogy caused a win, never weight cards on `checked` alone.

## Sources

S1 ACE, Zhang et al. 2025: https://arxiv.org/abs/2510.04618 (full text https://arxiv.org/html/2510.04618v3)
S2 ExpeL, Zhao et al. 2024: https://arxiv.org/abs/2308.10144
S3 Reflexion, Shinn et al.: https://arxiv.org/abs/2303.11366
S4 Huang et al. 2024, self-correction: https://arxiv.org/abs/2310.01798
S5 Kamoi et al. 2024: https://arxiv.org/abs/2406.01297
S6 SkillsBench 2026: https://arxiv.org/abs/2602.12670
S7 Evaluating AGENTS.md 2026: https://arxiv.org/abs/2602.11988
S8 Agent Workflow Memory: https://arxiv.org/abs/2409.07429
S9 ReasoningBank: https://arxiv.org/abs/2509.25140
S14 Xiong et al., memory and experience-following: https://arxiv.org/abs/2505.16067
S16 OPRO: https://arxiv.org/abs/2309.03409 (limits: https://arxiv.org/html/2309.03409)
S17 TextGrad: https://arxiv.org/abs/2406.07496
S18 GEPA: https://arxiv.org/abs/2507.19457 (tables: https://arxiv.org/html/2507.19457v2)
S19 Who&When: https://arxiv.org/abs/2505.00212
S20 AgenTracer: https://arxiv.org/abs/2509.03312
S21 Huxley-Godel Machine: https://arxiv.org/abs/2510.21614 (https://arxiv.org/html/2510.21614v3)
S22 Darwin Godel Machine: https://arxiv.org/abs/2505.22954 (https://arxiv.org/html/2505.22954v3)
S23 RD-Agent(Q): https://arxiv.org/abs/2505.15155 (https://arxiv.org/html/2505.15155v2)
S25 MLE-STAR: https://arxiv.org/abs/2506.15692 (https://arxiv.org/html/2506.15692v3)
S26 PRM lessons: https://arxiv.org/abs/2501.07301
S27 Hindsight credit assignment: https://arxiv.org/abs/1912.02503
S28 COMA: https://arxiv.org/abs/1705.08926
S29 DeepScientist: https://arxiv.org/abs/2509.26603
S30 Bilevel Autoresearch: https://arxiv.org/abs/2603.23420
S31 Rehearse: https://arxiv.org/abs/2607.27687
S32 AIRA_2: https://arxiv.org/abs/2603.26499
S35 An AI Scientist that Doesn't Drift: https://arxiv.org/abs/2608.07542
S37 Sleep-time compute: https://arxiv.org/abs/2504.13171
S38 Keiser and Arthur 2021, AAR meta-analysis: https://doi.org/10.1037/apl0000821 (abstract via https://api.semanticscholar.org/graph/v1/paper/DOI:10.1037/apl0000821?fields=title,year,abstract)
S39 Tannenbaum and Cerasoli 2013, debrief meta-analysis: https://doi.org/10.1177/0018720812448394 (d = 0.67 as cited in S38; abstract not retrievable)
S40 March, Sproull, Tamuz 1991: https://doi.org/10.1287/orsc.2.1.1
S41 Dwork et al., adaptive data analysis: https://arxiv.org/abs/1411.2664
S42 Goodhart's Law in RL: https://arxiv.org/abs/2310.09144
S43 Reward model overoptimization: https://arxiv.org/abs/2210.10760
S44 After-action review overview: https://en.wikipedia.org/wiki/After-action_review
Fetched, not used in the text (abstract-level, weak): Memento https://arxiv.org/abs/2508.16153; Dynamic Cheatsheet https://arxiv.org/abs/2504.07952; Training-Free GRPO https://arxiv.org/abs/2510.08191; Voyager https://arxiv.org/abs/2305.16291; Misevolve https://arxiv.org/abs/2509.26354; ShinkaEvolve https://arxiv.org/abs/2509.19349; GEAR https://arxiv.org/abs/2605.13874; ForeAgent https://arxiv.org/abs/2601.05930
Project files read: nano/calibrate.py, promote.py, loop.py, novelty.py, predict.py, report.py, research.py; research_notes/team/idea_generation/09_llm_ideation.md (R).
