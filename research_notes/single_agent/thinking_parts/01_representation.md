# 01. Representation: how the problem is encoded and re-encoded

*2026-10-13. Part 1 of `00_DECOMPOSITION.md`. Grades per claim: A replicated or multi-lab; B one controlled study, peer-reviewed benchmark or ablation; C vendor, practitioner, competition, contested or abstract-only; D model. Source tags: [F] full text consulted, [A] abstract or record only, [N] repo note, not re-fetched. The shared web-search budget was already spent at my first call, so this rests on direct fetches of named sources, not a systematic search; Wiley, ScienceDirect and Royal Society pages returned 403, so classics are checked against Crossref and Semantic Scholar records.*

## 1. What is known

**Humans: representation sets difficulty, and a good one can be searched for.**
- Isomorphs of Tower of Hanoi differ greatly in difficulty through how they are represented [S1, B]. Diagrams and sentences can be informationally equivalent yet not computationally equivalent: location indexing lets inference proceed with little search [S2, B].
- Experts and novices "begin their problem representations with specifiably different problem categories" [S3, B]. In Kaplan and Simon's mutilated-checkerboard work, insight requires discovering an effective representation, and difficulty tracks how available the generators and constraints are in that search [S4, B]. Chess players beat controls on the mutilated checkerboard because square colour is the right representation, and not on a problem without it [S5, B].
- Representational change theory (Ohlsson; constraint relaxation, chunk decomposition [S6, B]) is qualified by 2023-25 work: impasse is not necessary (4 preregistered experiments, N=856) [S7, B]; fixation cues cut accuracy 53.8% to 39.5%, d=-0.80 [S8, B].
- Describing parts by function, not name (generic-parts technique), solved 67% more problems [S9, B]; one search found no independent replication.

**AI problem solving: the representation is worth orders of magnitude; abstraction is not free.**
- Without finite-domain state variables, abstraction heuristics degrade "by several orders of magnitude" and BDD planning is "prohibitively bad" [S10, A]. Whether a hierarchy pays depends on the probability that an abstract solution can be refined [S11, B]; our analogue is the share of selected sketches that survive rungs 0-1.
- Translating to PDDL and calling a planner gives optimal plans where LLMs alone fail [S12, B]; but obfuscating the vocabulary drops o1-preview from 97.8% to 52.8% and Claude 3.5 Sonnet from 54.8% to 0% [S13, B].

**LLM agents, 2024-2026.**
- Encoding moves scores, less for stronger models: format-only changes swing accuracy up to 76 points, persist with scale and rank differently across models [S14, B]; Anthropic expects formatting to matter less [S15, C]. Graph encoder choice moves accuracy 4.8-61.8% by task [S16, B].
- Code or text per sub-task: CodeSteer guidance lifted GPT-4o's average on 37 symbolic tasks from 53.3 to 86.4, above o1 (82.7) [S17, B]; an earlier study found "no optimal method" and code not always better [S18, B]. FunSearch argues programs are more compact than raw solutions but shows no ablation against them in the text I read [S19, C]. A tool-built object representation nearly doubled GPT-4 on ARC (13/50 as text) [S20, B].
- Structure, not the whole file: for localisation a skeleton beat the complete file (58.33% vs 53.67%) at $0.02 vs $0.15 [S21, B]; a 100-line viewer beat a full-file viewer (18.0 vs 12.7 resolved) [S22, B]; length alone costs 13.9-85% even with perfect retrieval [S23, B].
- The spec is an evaluator plus marked regions. AlphaEvolve ablations: prompt context, meta-prompt evolution and full-file (not loss-only) evolution each matter; "stochastic formatting" randomises templates for diversity; its authors report that different abstraction levels (raw solution, constructor function, search algorithm) suit different problems and only hypothesize why [S24, B]. JSON task lists are overwritten less than Markdown [S25, C]; subagents need "an objective, an output format, guidance on the tools and sources to use, and clear task boundaries" [S26, C]. Forced JSON output hurt reasoning in one study [S27, C]; a vendor rebuttal disputes it [S28, C].
- Narrative feedback can beat scalar rewards: GEPA beat GRPO by 6% on average with up to 35x fewer rollouts [S29, B]; training on execution-trace rationales added 26.1 and 14.3 fix-rate points on PaLM 2 [S30, B].
- "Representation engineering" steers activations of open-weight models [S31, B]; no black-box analogue found, so it does not apply to an API loop.

**Diagnostics first.** Inspect data and curves before changing models [S32, S33, C]. Norm-scaling diagnostics predicted two instabilities at small scale [S34, B]. MLE-STAR picks the block to refine from an ablation summary (any-medal 43.9% vs 25.8% for AIDE, same model); the text I read has no ablation isolating that step [S35, C]. Text and image views of a series are complementary: text wins on point anomalies, images on range and variate anomalies (GPT-4o 5.71 to 2.61 and 11.95 to 29.88, text to image) [S36, B].

**Different encodings for different agents.** Induction and transduction solve different ARC tasks; their ensemble nears human level [S37, B]. Summing log-probs over 8 re-encodings of each ARC task lifted 51.5 to 63.5 and 60.5 to 72.5 on 100 tasks [S38, C]. In a formal model, random diverse teams beat teams of the best individuals [S39, D], but this is sensitive to the landscape [S40, B]. Against: the best format is model-specific [S14]; pseudo-code was the best builder hint only for o3-mini (0.40-0.43 vs 0.12-0.26 of speedup recovered) [S41, B]. I found no controlled study showing that encoding diversity raises idea diversity.

## 2. Where the loop stands (code read)

Problem file: prose goal, three baseline numbers (parameters, step time, smoke-loss drop), seven rules shuffled in most sketch calls (`loop.encode`, `_common`). Map: nine nodes (frame, assumptions, boundary) from one JSON-only planner call, one lens per run chosen by replicate, `replan` arm off. Diagnostics: bullets, a layer table, five curve points, probes at steps 0, 50, 100; they reach the planner, the diagnosis card and interrogation roots, never the builder. Script: full text (18 KB, about 4.6k tokens) in every call, about 80% of a median dry-run prompt; the builder re-emits the whole file. Have: lens rotation, comment-stripped and docs cards, `diagnose.fidelity`, typed analogy lint, three-pack pre-mortem (arm). A gap, from a 60-step dry-run table (`runs/mock-dry14`, `diag/diagnostics.md`): the rarest-token bucket reads 12.06 nats where uniform guessing is ln 50304 = 10.83, and ranks 1k-10k carry about 36% of the loss from 26% of tokens; the table shows neither.

## 3. Improvement ideas for this part

All are additions or arms judged by the unchanged verifier; status is new, partial, or have (Section 2). Protocol for each: equal contexts and replicate seeds; report `new_per_context`, top-2 share, TARGET validity, prediction ok-rate and rung 0-1 survival; adopt only if two improve at matched cost and verified wins do not fall. No real multi-round run exists to give baseline rates (the one real run has 2 verify rows), so log them first. Order: R1, R5, R7, R8, R9, then arms R2, R3, R4, R6. Weak points addressed: one encoding for every agent (R2, R3, R9), no alternative encodings (R1, R3, R7), no re-encoding when stuck (R4).

**R1. Cost and dataflow card by script (new, medium; extends catalogue REP-03).** `nano/cost.py` on the meta device writes per-module parameters, forward FLOPs per token, activation bytes, a 5-step profiler time share, the one-token dataflow with shapes, and slack against C3/C4 (21.24M of 23.37M parameters, VRAM, step ratio). Planner, interrogators, pre-mortems and builders get it; `SKETCH_FORMAT` gains a `COST:` line a script checks against slack before any build. Why: a computed second view [S2, S20], numeric sub-questions routed to code [S17]. Expect: fewer rung 1-2 failures, better parameter and step-time predictions. Measure: `predict.py` checkable-and-ok share, rung 1-2 failures by cause, `dropped_unsourced`.

**R2. Skeleton-first prompts (new, small).** `skeleton(src)`: signatures, Config values, forward order, one-line comments (about 1k tokens). Sketch, interrogation and pre-mortem calls get skeleton + cost card + bodies of the part's boundary symbols; only the builder sees the full file. Why: [S21, S22], indirect for one 400-line file; the penalty at 5k tokens is unknown [S23]. Expect: equal or higher cluster diversity, less anchoring on code detail, some infeasible sketches. Measure: protocol plus tokens per call.

**R3. Encoding classes as logged arms (partial, medium).** Lens rotation exists per replicate, but every agent reads the same text. Each sketch context gets an `encoding` from {skeleton (control), one-token dataflow narrative, phase timeline with lr schedule and curve knee, pathology list without code, ledger interaction table of composed pairs}, all script-made; `novelty.discovery` reports yield per encoding as it does per card. Why: views can be complementary [S37, S38] but format rankings do not transfer across models [S14], so measure, do not choose. Measure: per-encoding cluster yield, pairwise overlap (falsifier: above 0.7), verified-win rate.

**R4. Re-encode on stall (partial, small).** `replan_tree` exists but is off, keeps the lens and runs on schedule. Trigger it when `new_per_context` falls under a floor or three builds fail the same rung; move to the next lens; give the planner the assumptions shared by failed ideas (to relax) and ask it to split the part holding most failures. Why: constraint relaxation and chunk decomposition [S6], search for a representation [S4]; impasse is not required [S7], so trigger on yield. Measure: next-round clusters and verified builds vs no-replan and same-lens-replan replicates.

**R5. Typed problem spec with units (partial, small).** `problem.json`, rendered to prose per call: exam baseline mean and seed spread, spread at each rung's steps, the 0.005-nat margin as percent of steps via the baseline slope, the slack table, win tiers if adopted; sketches state effects in these units. Why: the evaluator and rendered scores are AlphaEvolve's spec [S24]; JSON survives edits better [S25]; subagent briefs need objective, output, tools, boundaries [S26]; evidence is practitioner-level. Measure: `predict.py` loss-claim calibration; share of built ideas whose claimed gain is below the margin.

**R6. Function-neutral part descriptions for outward sketches (partial: REP-09 catalogued, not in nano; small).** Planner adds `generic` per node (what the part does, in shapes and operations, no paradigm names); `tree.node_prompt` uses it for OUTWARD contexts only. Why: [S9], single lab; fixation cues cost accuracy [S8]. Caution: renaming collapses LLM planning [S13], so never in build or verify. Measure: outward clusters' distance from ledger texts and rung 0-1 survival, generic vs named.

**R7. Diagnostics in three views, over phases (partial, small to medium).** Keep the exact table; add contrast (bucket loss minus ln V, share of tokens times loss as share of total, layer over median layer), pattern (12-character strips per layer metric and a shape word), and trajectory (probes at 10%, 50%, 100% of one full baseline run per baseline version: 1,526 steps at about 1.2 s, half an hour). Sketchers get the top-3 contrasts, not the panel, to protect diversity. Why: [S36, S34, S33]. Measure: valid TARGET share, `diagnose.fidelity` ok-rate, diagnosis-card build and win rate.

**R8. Post-mortem card instead of a JSON dump (partial, small).** For each failed or flat build a script writes claim (PREDICTION, TARGET), measured (prediction check, cell moved, rung, margin), cause tag (no-op knob, wrong sign, below noise, cost violation, bug, unknown) and a lesson; the revise branch of `spec_prompt` and `history_text` use it instead of `json.dumps(feedback)[:3000]`. Why: [S29, S30]. Measure: `revise` fix rate; near-duplicate hits against failed builds.

**R9. Pseudo-diff `PLAN:` from interrogation (new, small).** `DEEPEN_FORMAT` gains `PLAN:` (at most 12 lines: symbols changed, shapes, init, cost line); `implement_brief` passes it; the builder keeps whole-file output, since unified diffs need line counts [S42]; per-symbol patches (parts 4, 6) may avoid that, so compare. Why: hint format is model-specific [S41]; self-planning gave up to 25.4% relative Pass@1 on 2023-era models [S43]. Measure: paired rung 0-1 survival and fidelity with and without PLAN, same ideas.

**Overlaps to merge, not duplicate:** R1 slack with part 4 G3; R2 with part 2 #9; R4 with parts 2 #6, 9 C4, 11 #4; R6 with part 5 #1; R7 feeds part 4 G1; R8 with parts 6 #6, 7 C8; R9 with parts 4 G5, 6 #5.

**Hold:** leave `boundary` alone. AlphaEvolve's loss-only ablation was worse [S24], but our boundary already allows new functions, Config fields and wiring; first log boundary rejections and the `recipe` node's yield.

## 4. Gaps and negative results

No systematic 2025-26 sweep was possible. Unchecked: replications of Chi 1981, the Kaplan-Simon cue effects and the generic-parts technique. Null or contested: no program-versus-raw ablation in FunSearch; none isolating MLE-STAR's ablation step; forced-JSON harm disputed [S27, S28]; code is not always better than text [S18]; format and hint winners are model-specific; the diversity theorem depends on the landscape [S40]; format effects shrink with model strength [S15]. Every "Expect" above is a hypothesis.

## Sources

- S1 Kotovsky, Hayes, Simon 1985, Why are some problems hard: https://doi.org/10.1016/0010-0285(85)90009-X [A]
- S2 Larkin, Simon 1987, Why a diagram is worth ten thousand words: https://doi.org/10.1111/j.1551-6708.1987.tb00863.x [A]
- S3 Chi, Feltovich, Glaser 1981, experts and novices: https://doi.org/10.1207/s15516709cog0502_2 [A]
- S4 Kaplan, Simon 1990, In search of insight: https://doi.org/10.1016/0010-0285(90)90008-R [A]
- S5 Bilalic et al. 2019, chess experts, mutilated checkerboard: https://doi.org/10.1111/cogs.12771 [A]
- S6 Knoblich et al. 1999, constraint relaxation and chunk decomposition: https://doi.org/10.1037/0278-7393.25.6.1534 [A]
- S7 Ross, Arfini 2024, impasse: https://repository.londonmet.ac.uk/9186/ [A]
- S8 Chao et al. 2025, fixation cues: https://pmc.ncbi.nlm.nih.gov/articles/PMC11947100 [N]
- S9 McCaffrey 2012, generic parts: https://doi.org/10.1177/0956797611429580 [A]
- S10 Helmert 2009, finite-domain representations: https://ai.dmi.unibas.ch/papers/helmert-aij2009.pdf [F]
- S11 Bacchus, Yang 1994, downward refinement: https://doi.org/10.1016/0004-3702(94)90062-0 [A]
- S12 Liu et al. 2023, LLM+P: https://arxiv.org/abs/2304.11477 [A]
- S13 Valmeekam et al. 2024, PlanBench and o1: https://arxiv.org/abs/2409.13373 [F]
- S14 Sclar et al. 2023, prompt-format sensitivity: https://arxiv.org/abs/2310.11324 [A]
- S15 Anthropic, context engineering: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents [F]
- S16 Fatemi et al. 2023, graph encodings: https://arxiv.org/abs/2310.04560 [A]
- S17 Chen et al. 2025, CodeSteer: https://arxiv.org/abs/2502.04350 [A]
- S18 Chen et al. 2025, steering code vs text: https://arxiv.org/abs/2410.03524 [A]
- S19 Romera-Paredes et al. 2023, FunSearch: https://www.nature.com/articles/s41586-023-06924-6 [F]
- S20 Xu et al. 2023, ARC object representations: https://arxiv.org/abs/2305.18354 [A]
- S21 Xia et al. 2024, Agentless: https://arxiv.org/abs/2407.01489 [F]
- S22 Yang et al. 2024, SWE-agent: https://arxiv.org/abs/2405.15793 [F]
- S23 Du et al. 2025, context length: https://arxiv.org/abs/2510.05381 [A]
- S24 Novikov et al. 2025, AlphaEvolve: https://arxiv.org/abs/2506.13131 [F]
- S25 Anthropic, long-running agents: https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents [F]
- S26 Anthropic, multi-agent research: https://www.anthropic.com/engineering/multi-agent-research-system [F]
- S27 Tam et al. 2024, format restrictions: https://arxiv.org/abs/2408.02442 [A]
- S28 .txt, rebuttal to S27: https://blog.dottxt.ai/say-what-you-mean.html [F]
- S29 Agrawal et al. 2025, GEPA: https://arxiv.org/abs/2507.19457 [A]
- S30 Ni et al. 2024, NExT: https://arxiv.org/abs/2404.14662 [A]
- S31 Zou et al. 2023, representation engineering: https://arxiv.org/abs/2310.01405 [A]
- S32 Karpathy 2019, training recipe: http://karpathy.github.io/2019/04/25/recipe/ [F]
- S33 Google, Tuning Playbook: https://github.com/google-research/tuning_playbook [F]
- S34 Wortsman et al. 2023, training instabilities: https://arxiv.org/abs/2309.14322 [A]
- S35 Nam et al. 2025, MLE-STAR: https://arxiv.org/abs/2506.15692 [F]
- S36 Xu et al. 2025, multimodal time-series anomalies: https://arxiv.org/abs/2502.17812 [F]
- S37 Li et al. 2024, induction and transduction: https://arxiv.org/abs/2411.02272 [A]
- S38 Franzen et al. 2024, ARChitects: https://da-fr.github.io/arc-prize-2024/the_architects.pdf [F]
- S39 Hong, Page 2004, diverse solvers: https://doi.org/10.1073/pnas.0403723101 [A]
- S40 Grim et al. 2019, sensitivity of S39: https://doi.org/10.1086/701070 [A]
- S41 Zhao et al. 2025, speedrun benchmark: https://arxiv.org/abs/2506.22419 [F]
- S42 Anthropic, building effective agents: https://www.anthropic.com/engineering/building-effective-agents [F]
- S43 Jiang et al. 2023, self-planning: https://arxiv.org/abs/2303.06689 [A]
