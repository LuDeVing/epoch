# Theory comparison: deep document

*Subfield A12.05. Scope: the head-to-head tests of representational change theory (RCT) and progress monitoring theory (PMT, also called the criterion for satisfactory progress, CSP) in insight problems. Key paper: Jones (2003), JEP:LMC 29(5):1017-1027. Evidence ids (a01-a25, b01-b29, c01-c27, d01-d17) point to the evidence_*.jsonl files in this folder. Claim ids (K01-K24) point to claims.jsonl. Related subfields researched in parallel are only linked, not covered: progress monitoring theory (sibling 04), insight as a process, gestalt roots and fixation, working memory and Gf, confidence and metacognition.*

## 1. What it is

Two theories explain why insight problems are hard and what breaks the impasse.

- **Representational change theory (RCT; Knoblich, Ohlsson, Haider and Rhenius 1999, Ohlsson).** The solver builds a wrong problem representation from prior knowledge. Two repairs exist: constraint relaxation (drop an assumed rule) and chunk decomposition (split a perceptual unit). Difficulty is set by how strong the wrong constraint is or how tight the chunk is. The theory is about knowledge.
- **Progress monitoring theory (PMT / CSP; MacGregor, Ormerod and Chronicle 2001).** The solver climbs a hill: take the move that looks most like progress (maximising). The solver also checks progress against a criterion, for example remaining items divided by remaining moves. When the criterion fails, the solver looks for other moves. Difficulty is set by how well the hill-climbing move fits the criterion. The theory is about strategy.

Jones (2003) put the two head to head on an unlimited-move problem (a car-park sliding puzzle) to which neither theory had been applied. Both got support. His manipulations pointed to RCT as the better indicator of performance. He also argued that eye-movement data are a good way to test insight theories (a01, abstract only).

Why this matters for our agent. The theories give two different triggers and two different repairs. PMT says: fire a change of approach when progress stalls (a code-side signal). RCT says: the fix is a new representation (a model-side operator, S2 and O4/O6). The evidence weight decides whether our schema needs a stall trigger, a reframe operator, or both, and in what order.

The honest summary: the founding "RCT wins" result rests on one 39-person experiment. Later direct tests (Ormerod and MacGregor 2020; Ollinger et al. 2017) show both factors matter, and a staged hybrid fits most data. No LLM study runs the head-to-head (K09, a25, c25).

## 2. History and theories in depth

**Gestalt and Ohlsson background.** Insight problems are hard because of fixation on a wrong structure (see the Gestalt-roots sibling). Ohlsson's RCT turned this into mechanisms: selective activation of knowledge, impasse, then constraint relaxation or chunk decomposition, then re-encoding.

**Knoblich et al. 1999 (c23, snippet only).** Matchstick arithmetic. Problem classes ordered by how strong the broken constraint is. Value changes are easiest, operator changes harder, tautologies hardest. Chunk decomposition: loose chunks (an operator made of sticks) are easier than tight chunks (parts of a numeral). This difficulty order is the standard RCT prediction.

**MacGregor, Ormerod and Chronicle 2001 (a02).** Nine-dot and related problems. Two heuristics: maximising (take the move that cancels the most dots) and progress monitoring with lookahead. These heuristics cause the difficulty and, once the criterion fails, start the search for other moves. Five experiments. A first line inside the array (diagonal) helped more than a line outside (47% vs 28% in Expt 4, N=134; 65% vs 43% in Expt 5, N=103; a11, second-hand). A pure knowledge or perceptual-block view predicts the opposite, because an outside line should cue the solution.

**Ormerod, MacGregor and Chronicle 2002; Chronicle et al. 2004 (a03, a04).** Eight-coin and six/ten-coin problems. Moves that look like progress but guarantee failure lower solution rates. Solvers follow hill-climbing. The difficulty is conceptual, not procedural.

**Jones 2003 (a01, d16).** Car-park (sliding block) problem, unlimited moves. Only the abstract was opened. Counts come from sibling folder 04 and are reconstructed: normal board 7 of 13 solved unaided (54%) versus rotated board 12 of 13 (92%) and easy-practice 12 of 13, N=39, Fisher p=.01 (K02, b28). These counts are provisional. The PsycNet page returned nothing (d16). Weak spots: tiny N, one task, impasse threshold set by the author, predictions for both theories set by the same author, and lookahead inferred from the same impasse data as the outcome (K18).

**Kershaw and Ohlsson 2004 (a05).** Nine-dot is hard for several reasons at once (perception, knowledge, process). Removing one cause gives small gains. This "multiple causes" view supports a hybrid.

**Ollinger, Jones and Knoblich 2006 and 2014 (b13, b14; not opened).** Two-move matchstick problems. Factorial test: representational change had a strong effect on solving, heuristics a minimal one; the authors propose representational change as a necessary condition for useful heuristics. The 2014 hint-group study gives a staged account: search first, then representational change, then search again in the larger space.

**Ash and Wiley 2006 (b08).** Working-memory span predicts success when the initial search space is large, but little when the search space is small and restructuring is isolated. Read as: WM matters for search; restructuring is automatic redistribution of activation.

**Ormerod, Fioratou, Chronicle and MacGregor 2006 (a11, a12).** Non-naive nine-dot solvers often remember "go outside the array" but cannot rebuild the solution, and revert to hill-climbing. Of 40 non-naive participants, 16 failed in two 30-s tries and 11 failed in 10 tries. A "destroy to create" necklace hint did not help.

**Chein and Weisberg 2014 (b10); Lv 2015 (b09).** Verbal remote-associates work. Chein and Weisberg read WM and attention control as evidence against a special insight process. Lv found that search-phase duration relates to WM span and restructuring duration does not (Exp 1: 87 tested, 79 valid, 64 solved; Exp 2: N=119); inhibition effects flipped sign across experiments.

**Ormerod, Rusconi, Banks and MacGregor 2015 (a09, d04).** An executable ACT-R model of CSP for the nine-dot problem. Stage 1: maximisation; accept a line if cancelled dots exceed remaining dots divided by remaining lines; otherwise mark it exhausted (criterion failure). Stage 2: relax minimisation, compare failed moves' properties (line length, angle, invariants), and extend the move space. 50 runs gave a solution rate under 5%, matching humans.

**Ollinger, Fedor, Brodt and Szathmary 2017 (a13, a14, b06, b07).** Ten-penny problem, a hybrid test (section 3).

**Ormerod and MacGregor 2020 (a06-a08, b01-b05, d17).** The cleanest factorial head-to-head: chunk tightness (RCT) crossed with equation value size (PMT). See section 3.

**Ormerod et al. 2022 (a10).** A third account, "idea discovery": after impasse, solvers compare failed attempts, extract properties (angle, line length) and recode them as variables, looking first in the problem statement and their own attempts. The 3-line nine-dot variant was solved more than the 4-line (24/69, 35% vs 9/67, 12%).

**Graf, Danek, Vaci and Bilalic 2023 (a15, b11, b12, d03).** Eye tracking on matchstick arithmetic. The restructuring shift is abrupt and late (about the 90% time bin), visible only with nonlinear methods (GAMs, change-point models). A hint produces a different pattern.

**Spiridonov et al. 2025/2026 (d01, d02).** A conceptual replication of an embodiment claim. Physical interaction did not reliably raise matchstick solving.

**Nasvytis and Fan 2026 (a20, a21, b15-b17, c09, c10, d15).** Large online think-aloud sample. The Knoblich order reproduces. Frame transfer is type-specific.

**Where the field stands.** Neither theory wins outright. Four stable facts: (1) knowledge sets baseline difficulty (RCT); (2) cues about distance to the goal change solving (PMT); (3) the two effects can interact; (4) reframing alone often fails and reframing plus a search criterion works (ten-penny). The staged view (progress monitoring fixes when the search for alternatives begins, representational change fixes how it succeeds) is the best current fit but is itself contested (K06).

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Jones 2003: car-park, RCT manipulations predicted performance better than PMT ones | Normal board 7/13 (54%) vs rotated 12/13 (92%) vs easy-practice 12/13; N=39; Fisher p=.01. Counts derived, not read from a clean table | Jones 2003 (a01, b28, d16) | Single source, provisional |
| Matchstick algebra: both chunk tightness and value size change solving | N=121. Low value loose 23/30 (77%); low value tight 13/30 (43%); high value loose 28/31 (90%); high value tight 24/31 (77%). Chi2(3)=21.6, p=.001; chunking Wald 8.12 p=.004; value Wald 8.65 p=.003; interaction ns | Ormerod and MacGregor 2020 Expt 1 (a06, b01) | Single source |
| First moves follow both forces | Loose-chunk first move: low value 28/30 (93%) vs tight 22/29 (76%); high value 21/31 (63%) vs 16/31 (52%). Chi2(3)=15.03 p=.002; value Wald 8.86 p=.003; chunking Wald 4.71 p=.030 | Ormerod and MacGregor 2020 (b02) | Single source |
| Large value gap lifts the hardest class (standard tautology) | N=133. Standard tautology low value 4/32 (12%) vs high value 21/34 (62%); reverse tautology 23/32 (72%) vs 28/35 (77%). Chi2(3)=39.30 p<.001; tautology Wald 19.33; value Wald 11.12 p=.001; interaction Wald 5.26 p=.022 | Ormerod and MacGregor 2020 Expt 2 (a07, b03) | Single source; may hinge on one numeral (LI, 51) on the solution path |
| Reframe hint alone fails; reframe plus search criterion works (ten-penny) | N=116 analysed of 120. Control 3/30 (10%); line hint 2/29 (7%); intersection hint 6/28 (21%); maximisation hint 21/29 (72%). Chi2(1,59)=23.80, phi .64; vs line group phi .67; vs intersection group phi .51; all p<.0001. 28% of maximisation group still failed | Ollinger et al. 2017 (a13, b06) | Single source; verified in critique |
| Variation of attempts separates solvers | Variation rate .59 vs .43, t(114)=3.10, d=.67; attempts 8.41 vs 10.93, t(114)=2.74; intersection use before hint 47% of solvers vs 26% of non-solvers, chi2=4.56 p<.05; Nagelkerke R2=.61, OR 3.99 for variation. Pennies-only after 5 min: control 10/30 (33%), line 1/29, intersection 2/28, maximisation 0/29 | Ollinger et al. 2017 (a14, b07) | Single source; post hoc predictors |
| First line inside the array helps nine-dot | 47% vs 28% (Expt 4, N=134); 65% vs 43% (Expt 5, N=103) | MacGregor et al. 2001 via a11 | Second-hand |
| ACT-R CSP model reproduces nine-dot | 50 runs, under 5% solved; 13-dot variant within 2 runs; 12- and 11-dot within under 10 runs; inside-first-line fewer runs, p<.01 | Ormerod et al. 2015 (a09, d04) | Model, single group |
| Idea discovery: easier source problem transfers | 3-line 24/69 (35%) vs 4-line 9/67 (12%); chi2(3)=11.35 p=.01; source Wald 7.63 p<.006 | Ormerod et al. 2022 (a10) | Single source |
| Non-naive solvers cannot rebuild the solution | Of 40, 16 failed two 30-s tries, 11 failed 10 tries; 13 of those 16 tried outside the array. Necklace hint: standard 1 hint vs 2 control of 44 | Ormerod et al. 2006 (a12) | Small samples |
| WM predicts success mainly with a large search space | Few-moves n=61, many-moves n=54; WM beta=.27 p<.01; WM x type delta R2=.046, F(1,111)=5.81 p<.05 | Ash and Wiley 2006 (b08) | Contested |
| Search and restructuring phases uncorrelated; WM links to search only | Exp 1: 79 valid, 64 solved; Exp 2: N=119; inhibition sign flips | Lv 2015 (b09) | Contested |
| Dual-task WM load: insight problems load WM less than non-insight | 32 experimental + 32 control; stage and stage x task interactions significant | Korovkin et al. 2018 (d12) | Single source |
| Matchstick difficulty order reproduces | N=189 analysed (202 recruited), 945 trials, 47.5% correct (449/945); value-loose-chunk 80.7%, tautology 19.2% | Nasvytis and Fan 2026 (a20, b15) | Established (K08, 3 sources) |
| Same order in a failed embodiment replication | Exp 1: static N=51 vs interactive N=54: A .91/.94, B .87/.80, C .59/.59, D .67/.69. Baseline about 86%. Only VR interactive credible: +0.67 log-odds [0.22, 1.15], about +6pp (92%) | Spiridonov et al. 2025/2026 (d01) | Single source; ceiling |
| Movement hurts constraint relaxation | Problem A no effect; B (operator) and C (tautology) more movements, lower success per problem; pooled coefficient -0.015 [-0.042, 0.014] | d02 | Post hoc |
| Frame discovery transfers only within type | Same: accuracy .32 (trial 1) to .75 (trial 5); Different .32 to .39; trial x group beta=-0.524, p<.001. After first success: 83.7% vs 44.0% later correct; 89.9 s vs 179.0 s | Nasvytis and Fan 2026 (a20, b16, d15) | Single source (human) |
| Fewer candidates considered at first success | Same beta=-2.11 [-2.97, -1.18]; Different -2.24 [-3.07, -1.41]; post-success Same -0.58 [-1.06, -0.13], Different +0.05 | c10 | Single source |
| Eye tracking: abrupt late shift | 34% solved unaided, +11% after hint; change point near 90% bin; N=61 | Graf et al. 2023 (a15, b11, d03) | Single source |
| Hints change the dynamics | After hint: non-solvers burst then fade; solvers gradual | b12 | Single source |
| Motor profile: solvers slower and pause more in final third | Three experiments; no headline rate | Spiridonov et al. 2019 (a16) | Single source |
| Situation puzzles: unstructured two-agent GPT-4o teams do worse | N=82; 47% protocol, 53% residual convergence; direct effect beta=-0.415, SE .146, p=.005 | Qiu, Zhou and Schooler 2026 (a19, d10) | Single source |
| LLMs far below humans on representational-shift riddles | Humans 52.9% (n=126, CI 46.6-59.2). 120-item subset: non-reasoning 7.6% (n=16), reasoning 17.6% (n=19). All 201 items: 9.42% vs 19.25%, Welch t(24.093)=2.976 p=.00655, d=0.946 (model level), pooled OR 2.29 [1.99, 2.64]. Size r=-0.017; release date Spearman .402 p=.0123 (n=38) | Mizumoto et al. 2025 (a17, b18, c01, c02, d08) | Single source (preprint) |
| Verification failure | Gold answer in thought log but not endorsed: 5.23% (Gemini 2.5 Flash Preview) to 39.34% (Grok 4) of wrong answers; R1-0528 30.57%; Opus 4 25.00% | b19, d07 | Single source |
| Thinking language | Grok-4 Japanese 29.5% vs English 48.8% p=.0071; Opus 4 36.7% vs 28.7% p=.356; Gemini 0/12 vs 22/188 | b20, c05 | Single source |
| Matchstick puzzles hard for VLMs | 400-item test; with text o3 60.00%, Gemini 2.5 Pro 45.25%, Gemini 2.5 Flash 26.50%, o4-mini 24.75%, Seed-1.6-Thinking 21.50%, Sonnet 4 2.25%, GPT-4o 0.00%; humans 91.72% (n=3). o3 without text 38.50% | Ji et al. 2025 (b21, b22) | Single source |
| Spontaneous Aha shifts are rare and go with lower accuracy | 6.31% of traces shifted; accuracy 2.57% vs 16.44%; Math -19.78pp; crosswords -6.24pp; Math high-entropy -7.40pp, low-entropy -22.88pp; formal Aha detector 1.79% of samples | d'Aliberti and Horta Ribeiro 2026 (b23, b24, c17, c19) | Single source; verified |
| Externally added reconsideration cue helps math, not puzzles | Math N=320,000: 32.21% to 40.62% (+8.41pp; 50,574 wrong-to-right vs 23,500 right-to-wrong). Crosswords N=83,200: 9.70% to 10.15% (+0.45pp). Rush Hour N=320,000: 0.0233% to 0.0363% (+0.01pp; 100 vs 58) | b25, c18, d05 | Single source; floor effect on puzzles |
| Entropy-shift link flips sign by domain | Pooled OR 0.77 (p=.070, N=723,200); crosswords 2.05; Rush Hour 1.19; math 0.58 | d06 | Single source |
| Red herrings fixate LLMs | GPT-4 original walls: single-digit number solved of 494 (humans 285/494); randomised walls up to about 68; WordNet walls (no herrings) up to 471; connection F1 about 41-45% vs about 80% human. Misformatted 4.4%, hallucinated clues 6.6% | Naeini et al. 2023 (c11, c12) | Single source; table rows jumbled |
| Mental set in LLMs | Six items per cell. GPT-4o exact match SP/SP+CPF/CP/CP+SPF .66/.66/.83/.83 (d11); a22 reports different values (.33/.66/.66/.83) | Haq et al. 2025 (a22, d11) | Anecdotal; the two lines disagree |
| Classic verbal insight items: ChatGPT near typical human | 12 of 30 (practice 7/15, transfer 5/15); human reference N=20. GPT-4 4.5 of 5 in one run; GPT-3.5 1.5 to 3.5 of 5; humans 44-61% per item | Orru 2023; Speed 2023 (c13, c14) | Contested; contamination likely |
| BRAINTEASER | Random 25%; ChatGPT 53% (word) and 63% (sentence); humans 91.67% (3 experts, 102 items). GPT-4 with metacognitive prompting above 98% (second-hand) | Jiang et al. 2023 (c15, c16) | Contested; saturated |
| Far-candidate sampling helps on RAT | n=349 and n=105; Aha vs fixation-cue distance beta=-0.13 [-0.21, -0.05], p=.0012 | Chao et al. 2025 (d13) | Single source; different task |

## 4. Mechanisms and models

Each mechanism is described so an engineer can code it.

**4.1 The CSP / PMT detector (code side).**
- State: the problem has a measurable gap to goal G (dots not yet covered, tests not yet passed) and a move budget B (lines left, rounds left).
- Maximising step: choose the candidate that reduces G most.
- Criterion: accept a move only if its gain is at least G / B (required average gain per remaining move). In the nine-dot model: cancelled dots greater than remaining dots divided by remaining lines (a09, d04).
- Criterion failure: if no candidate meets the criterion, mark the current move type exhausted. This is the trigger.
- On failure: widen the move space. Compare the properties of the failed moves (length, angle, type) and treat each property as a variable that may take other values. This is "idea discovery" (a10).
- Unlimited-move tasks have no B. Define a surrogate: no new fact, no change in the candidate set, or no drop in the gap in k steps (K18). The relative form is better than a fixed step cap.
- Token entropy is domain-dependent and flips sign (d06), so it must be fitted per task family and not used as a global rule.

**4.2 The RCT repair (model side).**
- Diagnose which constraint is active: a value rule, an operator rule, a tautology or scope rule, or a tight chunk.
- Repair types: relax a constraint (O4, "what if this rule is not true?") or decompose a chunk (O6, re-describe the object in smaller parts).
- Difficulty ladder from Knoblich: value change < operator change < tautology; loose chunk < tight chunk (a20, d01).
- The broader the constraint, the harder. Use as a difficulty ladder for items (K08).

**4.3 The staged hybrid (what to implement).**
1. Search under the maximising rule with an explicit criterion (code-checked).
2. When the criterion fails (PMT), fire a reframe operator (RCT) and pair it with a search criterion for the new space.
3. After the reframe, reset the criterion for the new space. Ten-penny shows that a reframe without a new criterion left 79-93% unsolved (b06).
4. Check variation. If consecutive attempts repeat one strategy (similarity above a threshold), force a different one (K04).
5. After a candidate is found, run an endorse step to stop verification failure (K11, K24). Not yet tested.

**4.4 The interaction.** In matchstick algebra a large value gap acts as a distance-to-goal cue that points at the right move, so it can stand in for knowledge restructuring on the hardest class (standard tautology 12% to 62%). Engineering reading: an informative progress signal can substitute for an expensive reframe. Before spending a reframe operator, check if a goal-distance cue already points at the move.

**4.5 Frame memory.** After a first success, store the frame with a problem-type tag. Same-type later accuracy 83.7% vs 44.0% (a20). The tag matters: transfer is type-specific.

**4.6 Idea discovery (alternative to relaxation).** Impasse, compare failed attempts, extract properties, recode as variables, look first in the statement and own attempts, then in memory (a10). In code: a function over the log of failed attempts that returns the properties that never varied.

## 5. What holds up

**Replications.**
- The Knoblich difficulty order holds in three data sets: Ormerod 2020, Nasvytis and Fan 2026 (N=189, value-loose-chunk 80.7% vs tautology 19.2%), and Spiridonov 2025/2026 (A easiest, C hardest, three experiments). This is the best-replicated result in the folder (K08, established).
- Hint-based staged results (Ollinger 2014, 2017) agree in direction: reframe-only hints do little, hint plus search criterion helps.

**Failed or weakened results.**
- Embodiment: physical interaction did not reliably raise matchstick solving (d01). One VR cell gave +6pp, at a ceiling (baseline about 86%). Movements went with worse results on operator and tautology problems (d02, post hoc).
- Spontaneous Aha in RL-tuned LLMs: not more frequent with training, linked to lower accuracy (b23, c17).
- The necklace "destroy to create" hint did not help nine-dot (a12).
- Classic English insight item results for LLMs vary widely (c13, c14 vs c15), likely contamination.
- WM and insight: Ash and Wiley, Lv and Chein and Weisberg disagree on what WM means for restructuring (K05, contested).

**Moderators.**
- Search-space size (WM effect appears only in large spaces, b08).
- Value gap size (large gap lifts standard tautology, interaction p=.022).
- Problem-type repetition (transfer only within type).
- Inhibition (sign flips across experiments, b09).
- Perception vs reasoning in matchstick items (o3 60.0% with text vs 38.5% pure visual, b22).
- Domain for the entropy-shift link (OR 2.05 crosswords, 0.58 math).

**Interventions.**
- Worked: reframe plus explicit search criterion (72% vs 7-21%); within-type practice; externally added reconsideration cue on math (+8.41pp); easier source problem for 4-line nine-dot (35% vs 12%).
- Did not work or unclear: reframe-only hints (7% and 21% vs control 10%); physical interaction; thinking in another language; the necklace hint; few-shot examples against red-herring fixation (small gains only); chain-of-thought for mental set (changes step counts, little exact-match change).

**Weak spots in the base.**
- Jones 2003: one experiment, N=39, one task, the same author set both theories' predictions (K18). Per-cell numbers not opened.
- Ormerod and MacGregor 2020: authors favour CSP, one problem per cell, between subjects, 5 minutes, internal inconsistency (low-value tight 13/30 in the outcome table, 11/29 in the first-move table; unresolved).
- Ollinger 2017: hints relax several constraints at once, so groups are not single-factor tests; 28% of the maximisation group still failed.
- Ormerod 2024 (PRODIGI) questions whether Jones discriminated between models; seen only as a search summary.
- The theories are not mutually exclusive; most results fit a staged hybrid. A head-to-head "winner" may be the wrong target.
- Source counting: Ormerod 2020, Nasvytis and Fan, and Mizumoto each appear as many evidence lines but are one paper each. Independent-source counts in claims.jsonl count papers.

## 6. Language models

**No LLM study runs an RCT vs PMT head-to-head** (K09, a25, c25). All evidence below is indirect.

**Humans vs models on representational-shift items.** Mizumoto et al. (a17, c01, c02): 38 LLMs on 201 Japanese children's riddles that need puns, phonetic play or kanji decomposition. Humans 52.9%. Non-reasoning 7.6%, reasoning 17.6% (120-item subset). Over all 201 items 9.42% vs 19.25%, d=0.946, OR 2.29. Only GPT-5 and some search-augmented models neared humans. Size did not predict accuracy (r=-0.017); release date did (Spearman .402). Do not quote d=0.946 with the 7.6/17.6 pair; they come from different subsets (critique).

**Verification failure.** Models write the right candidate in the thought log and then reject it: 5.23% to 39.34% of wrong answers, depending on model (b19). This is a convergence failure, not a generation failure. A similar pattern appears in situation puzzles: two-agent teams explored more but converged worse; 53% of the deficit was residual convergence cost (d10). No study adds an endorse step.

**Matchstick equations.** MathSticks (b21, b22): the best model o3 reaches 60.00% with text input, 38.50% from pictures; humans 91.72% (n=3). Reasoning models are far above base models (o3 60.00 vs GPT-4o 0.00; Seed-1.6-Thinking 21.50 vs base 3.25). Accuracy falls with level (text 73/56/56/55%; visual 69/37/30/18%). 82% of items need two-stick moves, so this is not the single-move Knoblich task, and perception mixes in. Text input isolates restructuring.

**Spontaneous Aha does not help.** d'Aliberti and Horta Ribeiro (b23-b25, c17-c19, d05, d06): 1M+ traces from small GRPO-tuned Qwen2.5 and Llama models on math, crosswords and Rush Hour. Mid-trace "wait" shifts occur in 6.31% of traces and go with lower accuracy (2.57% vs 16.44%). They do not rise with training. An external cue for a second pass raised math accuracy +8.41pp (N=320,000), crosswords +0.45pp, Rush Hour +0.01pp. The puzzle nulls sit on a floor (base 9.70% and 0.0233%; models of 1.5B to 8B), so they do not show that gating fails on puzzles. Pass 2 also adds extra sampling, so the cue is not isolated. The authors label crosswords as representational change and math as progress monitoring, but no condition varies tightness vs distance. Our own note (SCHEMA G1): forced doubt on word puzzles gave 75% vs 92% plain.

**Fixation and mental set.** LLMs are fixated by red herrings (c11: GPT-4 solves far more walls when herrings are removed; F1 about 41-45% vs about 80% human). Few-shot examples help a little, not enough. Einstellung tests on three models show CoT changes step counts (d11, a22), but with six items per cell this is anecdotal.

**Classic items conflict.** ChatGPT matched typical humans on 30 verbal insight items (12/30; d09) and GPT-4 solved 4.5 of 5 (c13), while BRAINTEASER shows 53-63% against 91.67% humans (c15). Metacognitive prompting above 98% is second-hand (c16). Public English items are likely contaminated or saturated; hashed fresh items (NazoNazo items 1-159) show a large human gap (d08).

**Language of thought.** Reasoning in Japanese did not help riddles (b20, c05).

**What changed performance, by how much.** Reasoning training: about +9.8pp on riddles; o3 60.00 vs GPT-4o 0.00 on MathSticks. Text vs picture: +21.5pp for o3. External reconsideration cue: +8.41pp on math. Removing red herrings: large. Spontaneous shifts: -19.78pp raw on math. Model size: no effect. Thinking language: no reliable effect.

## 7. What our agent should take

Status marks: [E] established (two or more independent sources), [S] single-source, [C] contested. Schema parts: G guardrail, S state, O operator, memory.

### Add now (established)

| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| N1 | Use the Knoblich-ordered item classes (value < operator < tautology; loose < tight chunk) as a difficulty ladder for benchmark design. It reproduces in three data sets. | Bench design | [E] | K08; a07, b03, b15, a20, c09, d01 |
| N2 | Do not rely on the model's own "wait" or spontaneous shift as a trigger. Triggers come from code (G1 stands). The effect size itself is single-source, the guard direction agrees with G1 and G10. | G1, S6 | [E] as a guard; [S] for size | K12; b23, c17, c19; our own 92% vs 75% |
| N3 | Fixation is real in LLMs: red herrings hurt, few-shot examples do not remove it. Keep the isolated fresh-context attempt (S3) and the input hygiene step (S1). | S1, S3 | [E] | K14; c11, c12, a22, b26 |
| N4 | Use fresh or hashed items when comparing trigger arms. Public classic insight items are saturated or contaminated. The rule costs nothing. | Bench rules | [C] on how much; rule adopted | K16, K23; c13-c16, d08 |

### Test first

| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| T1 | Reframe operator paired with an explicit search criterion beats reframe-only at equal tokens (ten-penny: 72% vs 7-21%). | O4/O6 + S6 | [S] | K03; a13, b06, b07 |
| T2 | Relative stall rule (gap divided by remaining budget, or no new facts in k steps) beats a fixed step cap. | S6 trigger | [S] | K21, K18; d04, a09 |
| T3 | Variation tracker: force a different strategy when attempt similarity exceeds a threshold. | G anti-repetition, S3 | [S] | K04; a14, b07 |
| T4 | Endorse step after generation: re-check any candidate that appeared in the trace. | S4 harvest, S8 | [S] | K11, K24; b19, d10 |
| T5 | Gated second pass (gate by disagreement or low consistency, not by schedule). | S5/S6 | [S] | K13; b25, c18, d05 |
| T6 | Check for a goal-distance cue before spending a reframe (a value gap lifted standard tautology 12% to 62%). | S2 + S6 | [S] | K01; a07, b03 |
| T7 | Frame memory keyed by problem type (same-type 83.7% vs 44.0%). Lessons stay shown after the first attempt (SCHEMA section 5). | Memory | [S] | K07; a20, b16, d15 |
| T8 | More actions (tool calls) do not replace a constraint-relaxing restatement. | O4 | [S] | K19; d01, d02 |
| T9 | Staged ablation: stall trigger only, operators only, both. | S6 + O | [C] | K06; b13, b14 |
| T10 | Branching-factor reading: stall trigger helps more where the search space is small. | S6 | [C] | K05; b08, b09, b10, d12 |

## 8. Concrete tests on our bench

All arms get the same token budget (setup cost counted, G7). Use fresh items written for the bench. Report solve rate with a binomial interval and paired win/loss counts.

1. **Reframe with and without criterion (T1).**
   - Items: 40 constrained-construction items with a computable gap (matchstick-style text items, Rush Hour variants, ten-penny style items); 10 with a known reframe.
   - Arms: (a) plain; (b) stall trigger plus reframe-only operator; (c) stall trigger plus reframe plus a stated criterion for the new space.
   - Metric: solve rate; tokens per solve.
   - Expected: (c) above (b) by 15pp or more on items that need a reframe; (b) near (a). Human analogue 72% vs 7-21%.
2. **Relative stall rule vs step cap (T2).**
   - Items: same set plus unlimited-move items (sliding blocks).
   - Arms: fixed step cap; relative criterion (gap divided by remaining budget); no-progress-in-k surrogate.
   - Metric: solve rate; wasted tokens before the trigger fires.
   - Expected: relative rule fires earlier on hard items at equal or fewer tokens.
3. **Factorial chunk x value (K01).**
   - Items: matchstick-style text items crossing loose/tight chunk with small/large value gap, plus standard vs reverse tautology; 20 or more fresh items per cell.
   - Arms: plain; reframe only; distance cue only; both.
   - Metric: solve rate per cell; test the interaction.
   - Expected: if the LLM mirrors humans, a large gap lifts standard tautology and the cue arm approaches the reframe arm in that cell.
4. **Variation tracker (T3).**
   - Arms: no tracker; tracker forcing a different strategy above a similarity threshold.
   - Metric: solve rate; distinct strategies per item.
   - Expected: gain on items where plain attempts repeat; no loss on easy items.
5. **Endorse step (T4).**
   - Arms: harvest and test all candidates (S4) vs the same plus an explicit endorse step on any dropped candidate.
   - Metric: gold-in-trace-but-rejected rate; solve rate; tokens.
   - Expected: lower verification failure than the 5-39% of wrong answers seen on riddles. Add only if the gain per token beats one extra plain sample.
6. **Gated vs scheduled vs spontaneous second pass (T5).**
   - Arms: spontaneous only; scheduled second pass; second pass gated by sample disagreement.
   - Items: math with headroom and puzzle items run with a stronger model (the published nulls were at a floor).
   - Metric: wrong-to-right minus right-to-wrong.
   - Expected: gated beats scheduled; scheduled hurts on easy items.
7. **Frame memory by type tag (T7).**
   - Items: sequences of five problems, same type vs mixed.
   - Arms: no memory; untagged memory; type-tagged memory shown after the first attempt.
   - Metric: accuracy on trials 2-5.
   - Expected: tagged memory lifts same-type sequences; no effect or harm on mixed ones.
8. **Action vs restatement (T8).**
   - Arms: more tool calls vs restate-and-relax at equal tokens on tautology-class items.
   - Expected: restatement wins.

## 9. What does not transfer, and why

- **Eye-movement and gaze signals (Graf 2023, Jones 2003).** The LLM has no gaze. The nearest analogue (candidate-set change per step) is untested (K20). Human change points near the 90% bin do not map to token positions.
- **Embodied interaction.** Physical manipulation (d01) is a human perceptual route. The agent has text and tool calls. The lesson that survives: acting does not replace relaxing a constraint (K19).
- **Perception effects.** Matchstick failures of vision-language models are partly parsing (o3 60.0% vs 38.5%, b22). They say little about restructuring. Use text items.
- **One problem per participant, 5 minutes, between subjects.** Human data use single items and a one-time impasse. An agent repeats items and can be re-run, so single-item effect sizes may not carry.
- **Feeling of insight and Aha.** Human metacognitive signals have no reliable analogue in model output. The R1 "aha" claim is not supported (c17).
- **Roman-numeral pre-test and open-day students.** Specific to the human paradigm (a08).
- **Working-memory span findings.** Span limits a human; a model's context is a different constraint. Whether branching factor plays the same role is untested (K05).
- **Incubation and unconscious work.** Not supported (SCHEMA section 4b).
- **Mizumoto riddles (Japanese wordplay).** Phonetic and kanji puzzles may not map onto matchstick restructuring, and some models are disadvantaged by language, so absolute rates do not measure restructuring ability.
- **Small-cell numbers.** Jones's cells (13 each) and Haq's six items per cell support direction only, not size.

## 10. Open questions

1. Does any LLM show the Ormerod interaction (a large value gap lifts the hardest class) in matchstick items? No test exists.
2. What are Jones 2003's published per-cell numbers? Does the RCT advantage hold in a Rush Hour variant for LLMs?
3. What does PRODIGI (Ormerod 2024) replace in CSP, and does it change the stall rule?
4. Does reframe plus criterion replicate on other multi-step insight tasks and in LLMs?
5. What gate makes a second pass pay on puzzles? The published nulls sit on a floor with 1.5B to 8B models (d05).
6. Is there an LLM analogue of eye-fixation impasse, such as step time above the mean plus 2 SD?
7. Does an endorse step reduce verification failure, and at what token cost?
8. Do WM-search findings predict anything about context length or branching?
9. Which public insight items are contaminated for current models? Release date predicts accuracy but no per-item or pre/post-cutoff split exists (d08).
10. Does frame transfer by type tag work for agent memory at equal tokens?
11. Is the staged account (PMT decides when, RCT decides how) falsifiable with a clean design, or is any outcome compatible?
12. Is the interaction an item artefact? One numeral (LI, 51) lies on the solution path of the high-value tautology item (b03).

## 11. Sources

[V] = opened and read this session (full text or substantial pages). [M] = snippet or abstract only.

- [M] Jones (2003) Testing two cognitive theories of insight. JEP:LMC 29(5):1017-1027. https://pubmed.ncbi.nlm.nih.gov/14516232/ ; https://doi.org/10.1037/0278-7393.29.5.1017 (a01, c21, d16; abstract only, full text not obtained)
- [M] MacGregor, Ormerod and Chronicle (2001) Information processing and insight. JEP:LMC 27(1):176-201. https://pubmed.ncbi.nlm.nih.gov/11204097 (a02; abstract only)
- [M] Ormerod, MacGregor and Chronicle (2002) Dynamics and constraints in insight problem solving. https://pubmed.ncbi.nlm.nih.gov/12109769/ (a03)
- [M] Chronicle, MacGregor and Ormerod (2004) What makes an insight problem? https://pubmed.ncbi.nlm.nih.gov/14736293/ (a04)
- [M] Kershaw and Ohlsson (2004) Multiple causes of difficulty in insight. https://pubmed.ncbi.nlm.nih.gov/14736292 (a05)
- [V] Ormerod and MacGregor (2020) The complementary roles of knowledge and strategy in insight problem solving. https://escholarship.org/uc/item/8m02w9c6 (a06-a08, b01-b05, d17)
- [V] Ormerod, Rusconi, Banks and MacGregor (2015) Modelling insight: the case of the nine-dot problem. https://iccm-conference.neocities.org/2015/proceedings/papers/0046/paper0046.pdf (a09, d04)
- [V] Ormerod, MacGregor, Banks and Rusconi (2022) Conceptual recoding of new ideas. https://escholarship.org/uc/item/82j4p09f (a10)
- [V] Ormerod, Fioratou, Chronicle and MacGregor (2006) The remnants of insight. https://escholarship.org/uc/item/509348f5 (a11, a12)
- [V] Ollinger, Fedor, Brodt and Szathmary (2017) Insight into the ten-penny problem. https://pmc.ncbi.nlm.nih.gov/articles/PMC5533865 (a13, a14, b06, b07)
- [V] Graf, Danek, Vaci and Bilalic (2023) Tracing cognitive processes in insight problem solving. https://eprints.whiterose.ac.uk/id/eprint/199182/ ; https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10219327/ (a15, b11, b12, d03; c24 snippet)
- [V] Spiridonov, Loginov, Ivanchei and Kurgansky (2019) Role of motor activity in insight problem solving. https://pmc.ncbi.nlm.nih.gov/articles/PMC6352738 (a16; tables not read)
- [V] Spiridonov, Erofeeva, Klowait, Morozov and Ardislamov (2025/2026) Matchstick conceptual replication on source of interaction. https://pmc.ncbi.nlm.nih.gov/articles/PMC12862482/ (d01, d02)
- [V] Mizumoto et al. (2025) Japanese children's riddles as a benchmark for machine insight and metacognition (NazoNazo / The Metacognitive Bottleneck). https://arxiv.org/pdf/2509.14704v2 (a17, a18, b18-b20, c01-c05, c16, c22, c26, d07, d08)
- [V] Qiu, Zhou and Schooler (2026) The cost of coordination. https://escholarship.org/uc/item/2sh4x44p (a19, d10)
- [V] Nasvytis and Fan (2026) Leveraging speech to identify signatures of insight and transfer. https://arxiv.org/pdf/2605.12970 ; https://cogtoolslab.github.io//pdf/nasvytis_cogsci_2026.pdf (a20, a21, b15-b17, c09, c10, d15)
- [V] Haq, Chhaya, Pandey and Bhattacharya (2025) Is your LLM trapped in a mental set? https://arxiv.org/pdf/2501.11833 (a22, b26, d11)
- [V] Ollinger, Szathmary and Fedor (2023) Search and insight processes in card sorting games. https://pmc.ncbi.nlm.nih.gov/articles/PMC10196050 (a23; tables not extracted)
- [V] Korovkin, Vladimirov, Chistopolskaya and Savinova (2018) How working memory provides representational change. https://pmc.ncbi.nlm.nih.gov/articles/PMC6174229/ (a24, d12)
- [V] Ash and Wiley (2006) The nature of restructuring in insight. https://link.springer.com/content/pdf/10.3758%2FBF03193814.pdf (b08)
- [V] Lv (2015) Working memory and inhibition in phases of insight. https://link.springer.com/content/pdf/10.3758/s13421-014-0498-7.pdf (b09)
- [M] Chein and Weisberg (2014) Working memory and insight in verbal problems. https://link.springer.com/content/pdf/10.3758/s13421-013-0343-4.pdf (b10; abstract and introduction only)
- [M] Ollinger, Jones and Knoblich (2006) Heuristics and representational change in two-move matchstick problems. https://irep.ntu.ac.uk/id/eprint/25198/ (b13)
- [M] Ollinger, Jones and Knoblich (2014) Dynamics of search, impasse and representational change. https://irep.ntu.ac.uk/id/eprint/13600/ (b14)
- [M] Webb, Little and Cropper (2016) Insight is not in the problem. https://frontiersin.org/articles/10.3389/fpsyg.2016.01424/pdf (b27; abstract and introduction)
- [V] Ji et al. (2025) MathSticks. https://arxiv.org/pdf/2510.00483 (b21, b22, c06-c08)
- [V] d'Aliberti and Horta Ribeiro (2026) The illusion of insight in reasoning models. https://arxiv.org/pdf/2601.00514 (b23-b25, c17-c19, c27, d05, d06)
- [V] Guo et al. (2025) DeepSeek-R1. https://arxiv.org/pdf/2501.12948 (c20)
- [V] Naeini et al. (2023) LLMs are fixated by red herrings (Only Connect Wall). https://arxiv.org/pdf/2306.11167 (c11, c12)
- [V] Speed (2023) Assessing the nature of large language models. https://arxiv.org/pdf/2309.07683 (c13)
- [V] Orru et al. (2023) Human-like problem-solving abilities in LLMs using ChatGPT. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10244637/ (c14, d09)
- [V] Jiang et al. (2023) BRAINTEASER. https://arxiv.org/pdf/2310.05057 (c15)
- [V] Chao, Hsieh and Wu (2025) Long-distance exploration in insightful problem-solving. https://pmc.ncbi.nlm.nih.gov/articles/PMC11947100/ (d13)
- [M] Fedor et al. (2017) Cognitive architecture with evolutionary dynamics solves insight problem. https://pmc.ncbi.nlm.nih.gov/articles/PMC5370243/ (d14; abstract only)
- [M] Knoblich, Ohlsson, Haider and Rhenius (1999) Constraint relaxation and chunk decomposition. https://research.ceu.edu/en/publications/constraint-relaxation-and-chunk-decomposition-in-insight-problem-/ (c23)
- [M] Bai et al. (2025, AAAI) metacognitive prompting on BRAINTEASER, via Mizumoto (c16); Latif et al. (2024) via Mizumoto (c22). Second-hand only.
- Search notes (not sources): a25, c25.
