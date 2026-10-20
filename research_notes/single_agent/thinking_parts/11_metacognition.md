# 11. Metacognition: knowing what one does not know

*2026-10-13. Research brief for part 11 of `00_DECOMPOSITION.md`. Grades: **A** peer-reviewed and replicated, large-N, or a theorem; **B** one controlled study or peer-reviewed benchmark; **C** preprint, abstract-level, or one benchmark; **D** engineering practice or my own simulation. (neg) marks a negative result. Sources marked * were read in full text (some in part); the rest at abstract level. Framing only: monitoring and control, after Nelson and Narens [14].*

## Bottom line

A model's own confidence is weak evidence (AUROC 0.5 to 0.65 in most reports), and reflection without new information does little. What works: signals computed from measurements, control rules scripted outside the model, and reflection triggered by an external result. The loop already measures more than most agent systems: log probabilities, compute stagnation from outcomes, decide in code, reflect only on measured failures.

## 1. Evidence

**LLM confidence and abstention**
- Verbalized confidence is overconfident; failure-prediction AUROC 0.52 to 0.61 by access level; sampling and aggregation help a little; professional-level tasks stay bad [1] B (neg).
- Semantic entropy (cluster sampled answers by entailment): AUROC 0.79 vs 0.69 naive over 30 task-model pairs, but blind to systematic errors [2]* A. On hard or long outputs the edge goes: no gain on SimpleQA, one baseline below chance on GSM8K, multi-step outputs "under-explored" [3]* B (neg).
- Reasoning models: better calibrated in 33 of 36 settings [4] B; yet confidence above 85% on wrong answers, rising with depth, and introspection helped o3-mini and R1 but hurt Claude 3.7 [5] C (neg).
- Agents (2026): post-run predicted success 73% vs 35% actual on SWE-bench Pro, AUROC 0.51 to 0.64; an adversarial "find the bugs" framing cut ECE 28 to 35% at twice the steps; mid-run confidence drops were uninformative [6]* C. Reasoning models predict no better [7] C; self-confidence did not beat a step-index baseline [8]* C (neg).
- Training helps: a Brier-score reward kept accuracy and improved calibration [9] B; code models are uncalibrated out of the box, Platt scaling fixes it when correctness labels exist [10] B. Frontier models are at chance on which of two AI-research ideas wins; a fine-tuned system reached 77% (63.6% on unpublished ideas) [11] B.
- Abstention helps when confidence is informative: the 20% of GSM8K answers that entailment-based scores rated most confident were all correct [3]; people opt out at a stable 30 to 47% confidence and opted-out items had lower success (N=596) [12]* B. People under-use it (7 to 25% opt-outs at 35 to 55% success) [12]; over-abstention and prompt sensitivity are documented [13]* B (neg).

**Human metacognition**
- Monitoring is cue-based; fluency is a pervasive, misleading cue; reconsideration rarely changes answers [14]* A. The confidence criterion for stopping falls with time [15] B; the opt-out criterion does not, against sunk-cost predictions [12].
- People leave a patch when its rate drops below the long-run average; larger deviation gave fewer items (B=-5.35, N=141) [16]* B. A random-walk model fits the same data [17] B (neg). In creative foraging people left a category after exploring 6.8% of it [18]* B (neg); forced iteration beat sequential work by broadening search, the edge narrowing over time [19] C.
- Insight: confidence separated right from wrong non-insight answers (Az 0.64) but not insight answers (0.56, n.s.; N=51) [20]* B (neg); warmth rises only at the end for Aha solutions and stays flat for unsolved ones [21]* B. Inference: progress ratings say little until late when the solution is a restructuring.

**Reflection and "metacognitive" prompting**
- Prompted self-correction without external feedback fails or degrades [22] A (neg); "no prior work demonstrates" it except on suited tasks [23] A (neg). With test feedback it works: Reflexion 91% vs 80% pass@1 [24] B; trained, SCoRe +15.6% MATH, +9.1% HumanEval [25] B.
- Models fix an error in a user's text but not the same error in their own output (64.5% blind spot); appending "Wait" removes 89.3% [26] B.
- Metacognitive prompting beats CoT on NLU [27] B; telling a model it has good metacognition raised faithful calibration up to 61% [28] B. The 2026 survey: conflicting evidence on meta-reflective prompts, and models cannot yet decide when to persist or move on [29]* B (neg). Stated reasoning is a poor monitor: a used hint was named in under 20% of cases in many settings [30] C (neg); "aha" behaviour exists in base models [31] C (neg); CoT, reflection and "ignore the anchor" did not remove anchoring [32] C (neg).
- Control from signals works: a harness routing feeling-of-knowing (pre-solve) and judgement-of-learning (post-solve) signals to trust, retry or aggregate lifted pooled accuracy 48.3 to 56.9 [33] C; difficulty-adaptive compute beat best-of-N by over 4x but needed a verifier and extra compute [34]* B.

**Homogenisation and anchoring**
- 219,655 agent-generated ideas were more concentrated and nearer the seed literature than human work [35] C; models repeat themselves and each other [36] A. Verbalized sampling raised diversity 1.6 to 2.1x [37] C; RL gains at k=1 vanish at large k [38] B. Evaluators favour their own output [39] B.

**Stagnation, restarts, changing the problem**
- Soar's impasses: no operator proposed, tie or conflict, same operator without progress; resolved in a substate and compiled into a rule [40]*.
- "Stuck midway" was 42 to 49% of web-agent failures; replanning against a subgoal checklist cut it 48.4 to 39.9% and lifted success 23.0 to 32.1% [41]* C. OpenHands loop rules (4 identical action-observation pairs, 3 identical errors, 3 monologue messages, 6 ping-pong) falsely stopped intended polling [42] D (neg). A plateaued agent does not call diagnostics unprompted; ReASearch inserts an advisory after 3+ and 7+ flat evaluations, broke a 120-turn plateau by relaxing a constraint, and scored 50.0 vs 39.2 on ARC-AGI-2 test with persistent lessons [43]* C.
- A counter threshold C(n,s)ln R bounds the chance of missing an improvement by 1/R, yet can miss the right strength [45]* A. Restarts removed heavy tails (orders-of-magnitude speedups) but blocks-world had none (30 to 23 min) [46]* A (neg). A "5% new themes" saturation rule stopped with only 62 to 82% of themes [47]* B (neg). Good-Turing: unseen mass is about f1/n, Chao1 a lower bound [49]*; no LLM validation found.
- Changing the problem: per-goal learning-progress prediction [50] B and learnable-and-interesting filters [51] B exist in open-ended RL; none is tested on research loops. Reformulation without a trigger (Step-Back) added 7 to 27 points on PaLM-2L [48] B; no trigger was tested.
- Used in the ideas: pooled forecasts of 208 experts beat 96% of individuals, credentials did not help [44] A; calibration metrics mix sensitivity and bias [54] C; "100 events and 100 non-events" is too small for calibration (one example needed 949 patients, 408 events, for a slope CI of width 0.3) [52]* B; dense progress signals, not generation, are argued to be auto-research's bottleneck [53] C.

## 2. Own simulations (D)

Stdlib Monte Carlo (scratchpad `m11/sim`). (a) A confidence with AUROC about 0.60 and a 40% event rate gives power 0.50, 0.75, 0.97 at N=100, 200, 400 to detect any signal (slope SD 0.27, 0.20, 0.13); at 10% power is 0.27, 0.44, 0.65, 0.90 at N=100 to 800; at 4% (AUROC 0.71) 0.46, 0.66, 0.90 at N=100, 200, 400; slopes are unusable below 200. The repository holds 7 real verified builds. (b) With Zipf-distributed clusters, m·f1/n forecasts new clusters per 40 sketches within 2 to 3 (14.0 vs 12.4 actual at n=72; 5.6 vs 5.3 at n=300). A clusterer that over-splits 20% of sketches keeps that forecast accurate but inflates unseen mass to 0.51 vs 0.35: "new clusters" can look healthy while ideas are exhausted.

## Improvement ideas for this part

Have: discovery curve, top-2 share, attractor-card retirement (`novelty.py`); PREDICTION per sketch, checked in `predict.py`; "unknown" answers and dropped unsourced numbers (`deepen.py`); pre-mortems; novelty gate with 10% audit; controls; long-shot and hedge lanes; logged "upward" reframing proposals. But `check_prediction` counts a predicted gain smaller than two seed-spreads as held even when the candidate does nothing.

**1. Forecast fields and a null-forecaster scorecard (partial).** *Mechanism:* add `P_PASS` (clears rung 3), `P_WIN` (stackable or better), `GAP80` (80% interval of the matched-step gap) to the sketch format, `P_FAIL` to the pre-mortem; average independent contexts proposing a cluster (pooled forecasts beat individuals [44]); show the forecaster its recent hits (some models recalibrate in context [7]); score with Brier and interval score, AUROC and slope separately [54]; always print a null (card and part rate) and a cheap-feature forecaster. *Effect:* learn whether any self-report has skill; expect little. *Cost:* small, no extra calls. *Measure:* AUROC and slope with CIs at the N in section 2; use for selection only if the lower AUROC CI exceeds 0.55 and beats the null.

**2. Fact confidence, contested claims, unknown-count stop (partial).** *Mechanism:* KNOWN lines carry `[src][conf]`; uncited numeric claims are re-asked three times by the cheap model and disagreement moves them to a CONTESTED block (claim-level semantic entropy, as in [2]); script-checkable facts are verified at rungs 1 to 2. Stop a chain when 'unknown' is at least half of build-relevant answers or a child adds fewer new facts than the average call. *Effect:* fewer builds on false premises; shared misconceptions stay invisible. *Cost:* about 36 cheap calls in round 1. *Measure:* precision of CONTESTED against facts the build contradicts; facts per call by depth.

**3. Impasse panel, `nano/impasse.py` (partial).** *Mechanism:* per part and round: (a) no-change: Good-Turing forecast of new clusters, per card, on fine and coarse clusterings; (b) operator no-change: three flat builds in a lineage or one (rung, reason-hash) three times, thresholds configurable [42]; (c) tie: top scores within noise, settle with the cheap TEST; (d) rate: leave a part when its dense progress per token (best z-gap gain, stackable gains) falls below the run average, minimum six builds [16][53]. *Effect:* earlier than waiting for sparse wins. *Cost:* small. *Measure:* backtest false-stop rate (wins after a flag); forecast error of next-round clusters.

**4. Scripted widen / narrow / reframe / stop controller (new).** *Mechanism:* one decision per round in `_rounds`: NARROW (revise, compose) when a lineage improves; WIDEN (more contexts, new lens, cross-family) when generation is open but outcomes flat; REFRAME (idea 8) when both are exhausted; STOP after two such rounds, keeping a 10% hedge because stop rules miss tails [47]. Each decision stores a falsifiable forecast scored next round. Scripted because models do not decide persistence well [29][43]. *Effect:* budget follows yield; verifier-backed allocation paid 4x in [34]. *Cost:* medium; overlaps part 9. *Measure:* A/B against fixed rounds at matched tokens on stackable-or-better per 1M tokens; share of STOPs followed by a later win.

**5. Builder honesty channel, lineage stop, gated expensive rungs (new).** *Mechanism:* output gains `FIDELITY: exact|partial|substituted|cannot` and a pre-code `FEASIBILITY`; a diff check audits it; `cannot` and `substituted` log as discovered assumptions, not failed ideas. Two failures at one rung with one reason-hash retire a lineage. Before overnight and hedge runs, require P_WIN (updated with the rung-3 z) above a cut plus a 10% audit stratum below it, in shadow mode (`would_skip` logged) until idea 1's test passes; rungs 0 to 3 stay ungated. *Effect:* cleaner ledger, fewer wasted hours. *Cost:* small. *Measure:* risk-coverage curve; audit stratum vs above-cut pass rate; declared vs diffed fidelity; Platt recalibration [10].

**6. Critic calibration ledger (new).** *Mechanism:* tag each pre-mortem objection with a checkable type (step time, params, early-only, noise-sized, interaction); after the build mark hit or miss; show the critic its hit rate by severity and type; rank WATCH FOR lines by realised hits; adversarial framing [6]. *Effect:* turns forwarded objections into measured warnings. *Cost:* small. *Measure:* hits per severity (30+ tagged objections), Brier of P_FAIL against the null.

**7. Bias monitors (partial).** *Mechanism:* (a) hivemind index: pairwise similarity within and across contexts vs a round-1 bootstrap [35][36]; (b) anchor A/B: 20% of round-2 contexts get no history or exclusion block, compare the share whose nearest neighbour is a shown item (instructions do not cure anchoring [32]); (c) survival by sketch position (fluency [14]); (d) tags (`obvious`, `prior`) vs outcomes and writer family [39]. *Effect:* settles whether history helps or anchors (open item X5). *Cost:* small. *Measure:* inject a duplicate card to test sensitivity; effect on new clusters per context.

**8. Diagnose-and-reframe call with persistent lessons (partial).** *Mechanism:* on REFRAME, or three and seven flat builds in a part [43], one call reads the failure ledger (reason-hashes, falsified assumptions, objection hits, contradictions) and outputs the binding constraint, one constraint to relax or representation to change (new lens, `replan_tree`, metric-validity, scale or data), and a test runnable at rung 3 or below; results append to a `lessons` file all later contexts read. Today `replan_tree` is a manual flag and upward proposals are never acted on. *Effect:* a different problem instead of more of the same; evidence is thin, run as an arm. *Cost:* medium. *Measure:* share of reframes yielding a checked candidate in a new cluster vs a WIDEN-only arm at matched cost.

Order: 1 (logging only), 3, 5 and 7(a,b) first, about a day; 2 and 6 next; 4 and 8 as arms once 1 and 3 hold data. Overlaps: 1 and 6 with brief 07 (C5, C1); 3, 4 and 8 with brief 09 (C2, C3, C4); build each once. New here: the sample-size table, the clusterer-granularity guard, Soar impasse types, the FIDELITY channel, contested facts, the anchor A/B.

## Sources

[1] Xiong 2024, https://arxiv.org/abs/2306.13063
[2] Farquhar 2024, https://pmc.ncbi.nlm.nih.gov/articles/PMC11186750
[3] Xia 2025, https://aclanthology.org/2025.findings-acl.1101.pdf
[4] Yoon 2025, https://arxiv.org/abs/2505.14489
[5] Mei 2025, https://arxiv.org/abs/2506.18183
[6] Kaddour 2026, https://arxiv.org/html/2602.06948
[7] Barkan 2025, https://arxiv.org/abs/2512.24661
[8] Lin 2026, https://arxiv.org/html/2609.07395v1
[9] Damani 2026, https://arxiv.org/abs/2507.16806
[10] Spiess 2025, https://arxiv.org/abs/2402.02047
[11] Wen 2025, https://arxiv.org/abs/2506.00794
[12] Ackerman 2026, https://ackerman.net.technion.ac.il/files/2026/06/Ackerman-2026-Pre-publication-Version-Its-Time-to-Opt-Out.pdf
[13] Wen 2025 abstention, https://arxiv.org/html/2407.18418v3
[14] Ackerman and Thompson 2017, https://www.psicologia.ulisboa.pt/wp-content/uploads/2020/03/Ackerman-Thompson-2017.pdf
[15] Ackerman 2013, https://escholarship.org/uc/item/8pb5j26h
[16] Hills 2012, https://warwick.ac.uk/fac/sci/psych/people/thills/thills/2012hillsetalpsychrev2012.pdf
[17] Austerweil 2012, https://proceedings.nips.cc/paper_files/paper/2012/file/14d9e8007c9b41f57891c48e07c23f57-Paper.pdf
[18] Hart 2017, https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0182133
[19] Kagan 2026, https://arxiv.org/abs/2603.00722
[20] Hedne 2016, https://pmc.ncbi.nlm.nih.gov/articles/PMC5005374/
[21] Kizilirmak 2018, https://www.frontiersin.org/articles/10.3389/fpsyg.2018.01404/full
[22] Huang 2024, https://arxiv.org/abs/2310.01798
[23] Kamoi 2024, https://arxiv.org/abs/2406.01297
[24] Shinn 2023, https://arxiv.org/abs/2303.11366
[25] Kumar 2024, https://arxiv.org/abs/2409.12917
[26] Tsui 2026, https://arxiv.org/abs/2507.02778
[27] Wang and Zhao 2024, https://arxiv.org/abs/2308.05342
[28] Liu 2025, https://arxiv.org/abs/2505.24858
[29] Liu 2026 survey, https://arxiv.org/abs/2607.11881
[30] Chen 2025, https://arxiv.org/abs/2505.05410
[31] Liu 2025, https://arxiv.org/abs/2503.20783
[32] Lou and Sun 2024, https://arxiv.org/abs/2412.06593
[33] Cao 2026, https://arxiv.org/abs/2605.14186
[34] Snell 2024, https://arxiv.org/html/2408.03314
[35] Tang and Yang 2026, https://arxiv.org/abs/2605.27905
[36] Jiang 2025, https://arxiv.org/abs/2510.22954
[37] Zhang 2025, https://arxiv.org/abs/2510.01171
[38] Yue 2025, https://arxiv.org/abs/2504.13837
[39] Panickssery 2024, https://arxiv.org/abs/2404.13076
[40] Laird 2022, https://arxiv.org/abs/2205.03854
[41] Wang 2026, https://arxiv.org/html/2603.19685v1
[42] OpenHands, https://docs.openhands.dev/sdk/guides/agent-stuck-detector and https://github.com/OpenHands/software-agent-sdk/issues/762
[43] Li 2026, https://arxiv.org/html/2608.06714
[44] DellaVigna and Pope 2018, https://nber.org/papers/w22566
[45] Rajabi and Witt 2021, https://ar5iv.labs.arxiv.org/html/2101.12054
[46] Gomes 1998, https://cdn.aaai.org/AAAI/1998/AAAI98-061.pdf
[47] Guest 2020, https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0232076
[48] Zheng 2024, https://arxiv.org/abs/2310.06117
[49] Chao 2017, https://www.uvm.edu/~ngotelli/manuscriptpdfs/Chao_et_al-2017-Ecology.pdf
[50] Gaven 2025, https://arxiv.org/abs/2502.07709
[51] Zhang 2024, https://arxiv.org/abs/2306.01711
[52] Riley 2024, https://pmc.ncbi.nlm.nih.gov/articles/PMC11778934
[53] He 2026, https://arxiv.org/abs/2608.09855
[54] Cacioli 2026, https://arxiv.org/abs/2603.14893
