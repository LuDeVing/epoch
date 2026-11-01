# Progress monitoring: deep document

*Subfield A02.07. Source files in this folder: evidence_a-d.jsonl (ids a01-d31), claims.jsonl (K01-K29), critique.md. Status marks: [E] established, [S] single-source, [C] contested.*

**Honesty note up front.** The focus line says "anagram solvability judgments improve." We could not support that. The key papers (MacGregor, Ormerod and Chronicle 2001; Ormerod 2002 full text; Novick and Sherman 2003) were paywalled and not opened. What we did read says the opposite for anagrams (Smith and Kounios 1996: little or no partial information). The human core of this document rests on one 1987 study, one failed replication, one partial replication and a handful of follow-ups. The LLM half is much richer.

## 1. What it is

Progress monitoring is the solver checking, during the solve, how far it is from the goal and whether the current approach is working. It has two jobs. First, read a signal (a felt "warmth", a count of dots left, a repeated screen). Second, act on it (keep going, switch approach, stop).

Three meanings are mixed in the literature. We keep them apart.

1. **Felt nearness.** The solver rates how close it feels (warmth, feeling of knowing, solvability). A graded, subjective signal. Human data: Metcalfe and Wiebe 1987 and what followed.
2. **Rule-based progress check.** A fixed criterion computed from the problem (nine-dot: dots remaining over lines available). When no move meets it, the criterion "fails" and the solver widens its search. Binary, not felt. Human theory: MacGregor, Ormerod and Chronicle (CSPT, progress monitoring theory).
3. **Engineered stall detection in LLM agents.** Counts of repeated actions, repeated observations, unchanged answers, low confidence, hidden-state probes. Code decides. This is what our S6 trigger is.

Why it matters for our agent: S6 (IMPASSE) fires on code-set conditions (no pass, two rounds with no change, same error twice, budget fraction). The questions are whether that rule is right, how to set its thresholds, what false-stop rate to expect, and what the response should be. Related guardrails: G1 (doubt only on a signal), G2 (revise from real output), G10 (reasoning text is not evidence), G11 (think briefly), G12 (spend by difficulty).

Not covered here, only linked: representational change theory, metacognitive regulation, meta-reasoning, overthinking, optimal stopping, bandit allocation, test-time compute scaling, fault localisation and repair, self-correction, confidence and signal-detection measures, and the Gestalt insight debate. Those subfields are researched in parallel.

## 2. History and theories in depth

**Difference reduction (Simon, Newell and Shaw 1979).** Search is directed by comparing the current state with the goal. A move that makes the state more like the goal is kept. If this guides human solving, the feeling of being close should climb steadily. [a05]

**Metcalfe 1986 and Metcalfe and Wiebe 1987: the founding studies.** Metcalfe (1986b, described second-hand) had solvers rate warmth every 10 s on a 10-point scale. 78% of correct insight problems and anagrams rose by 1 point or less over the whole interval, and wrong answers showed the incremental rise. [a04] Metcalfe and Wiebe (1987, opened) found warmth rose gradually before correct answers on multistep and algebra problems, but changed little before classic insight answers. They proposed using suddenness to define insight. They also found that predicting in advance whether one will solve (feeling of knowing) worked for algebra, not for insight problems. [a01, a02, a03]

**Metcalfe's reading of wrong answers.** High confidence just before an answer on insight problems predicted an error; people talk themselves into a wrong answer. Incremental warmth before a wrong answer may be satisficing. [a09, a26]

**Progress monitoring theory / CSPT (MacGregor, Ormerod and Chronicle 2001; Ormerod, MacGregor and Chronicle 2002).** Solvers use hill climbing or maximisation to reduce the gap to the goal. They monitor progress against a Criterion for Satisfactory Progress: a fixed ratio from the problem statement. On the nine-dot problem it is dots remaining over lines available. When no available move meets the criterion ("criterion failure"), the solver drops the current approach and widens the search. That is the source of insight on this account. Lookahead of 1 to 4 line segments is part of the model. [a27, d01, d03, d04] Important: this is a binary trigger from a computed ratio, not a felt gradual warmth. That is the same shape as our code-set rule.

**Rival: representational change theory (Ohlsson; Knoblich).** Insight comes from changing the problem representation, largely unconscious. Reviews name no experiment that cleanly separates the two accounts. [b15] Eight-coin data (Ollinger et al. 2013) found two further sources of difficulty (the 2-D assumption and perceptual grouping), and moves came from the existing representation, not from heuristics. That favours representational change. [d06] See the sibling subfield "Representational change theory."

**Non-insight accounts.** Aha ratings may be metacognitive judgments built after the fact from fluency and a correct first move, not a readout of progress (Wiley and Miller 2026). Aha belongs to the solver and the outcome, not the problem (Webb et al. 2016). [a21, a23, b10]

**Machine lineage.** Self-monitoring navigation agents (Ma et al. 2019) built a learned progress estimate directly on this idea. [c18, c19] Tree of Thoughts (2023) used a sure/maybe/impossible state value as a progress monitor. [c09] Reflexion (2023) used a hard count rule. [c10] From 2024 the overthinking and underthinking literature and many early-exit methods use confidence and convergence signals. 2026 work shows that models judge "no progress" but do not act on it unless code forces it. [d18]

## 3. Core findings with exact numbers

Status is [E], [S] or [C] as in claims.jsonl. Human rows are mostly single-source.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Warmth rises gradually before multistep/algebra solutions, flat/abrupt before classic insight | Exp 1: 19 usable of 26; gamma .26 (angular, t(18)=2.02), .23 (differential, t(18)=1.63, one-tailed). Exp 2: 39 usable; gamma .35 (t(37)=3.10), .32 (t(37)=2.56) | Metcalfe and Wiebe 1987 [a01, a02] | [S] |
| Feeling of knowing predicts success for algebra, not insight | gamma algebra .40 (t(46)=4.6); insight .08 (t(46)=.8); difference F(1,46)=6.46 | M and W 1987 [a03] | [S] |
| Normative difficulty beats solvers' own predictions | norm predicted success r=.77 insight, .60 algebra | M and W 1987 [a03] | [S] |
| Failed replication of the warmth contrast (magic tricks, insight = Aha report) | N=51, 971 trials; differential warmth 2.92 vs 0.30, t(210)=0.79, p=.429, d=.12; angular d=.22 | Hedne et al. 2016 [a06] | [C] |
| Partial replication when insight = Aha report (verbal riddles) | N=36, 27 usable; last-minus-third-to-last warmth 2.59 vs 1.43, t(26)=4.27, d=.82; interaction F(2,52)=15.63 | Kizilirmak et al. 2018 [a12] | [S] |
| Warmth on unsolved items stays low | unsolved n=34, ratings 0 to 1 on 0-4 scale; Aha vs not p=.207 | Kizilirmak 2018 [a13, b27] | [S] |
| Warmth-defined and report-defined insight agree across people, not item by item | per person r=.61 (n=51); per item r=.08 (n=182, p=.235); only 180 of 631 solved items had 2+ ratings; sudden warmth had self-report insight 75.6%, gradual still 50.8% | Laukkonen and Tangen 2018 [a10, a11] | [S] |
| Insight-labelled solutions more accurate and confident, but confidence discriminates correctness poorly | accuracy .57 vs .37 (d=.51); confidence 78.3 vs 69.0 (d=.50); AUC 0.56 (n.s. vs chance) vs 0.63; contrary: AUC 0.90 (N=10, Mooney images) | Hedne 2016 [a07, a08]; Ishikawa 2019 [b11] | [C] |
| "I am stuck" button does not match behaviour | presses by 33% of solvers (8/24) vs 79% of nonsolvers (34/43); no solve-rate cost (55% vs 49%, p=.70) | Fedor et al. 2015 [a18] | [S] |
| Behaviour separates solvers: position repetition | nonsolvers 0.5 vs solvers 0.3, t(99)=5.13, d=1.03 | Fedor 2015 [a19] | [S] |
| Relatedness structure changes in two steps before the solution | N=10; intermediate step t(9)=2.55, then high t(9)=3.41; solver vs nonsolver graph r=.00 | Durso, Rea and Dayton 1994 [a14-a16] | [S] |
| Anagram solving shows little or no partial information | 2 experiments, speed-accuracy decomposition; no N or accuracy read | Smith and Kounios 1996 [d07, d08] | [S] (abstract only) |
| Aha rating follows correctness and first move | N=377, 1,164 obs; F(1,1091)=112.17, partial R2=.09; solve rates 33/48/34/17% | Wiley and Miller 2026 [a23, b10] | [E] (3 sources) |
| Aha correlates with accuracy in insight problems, ~0 in non-insight | r .50/.40/.495 insight; .02/.24/.19 non-insight; N=184/74/117 | Webb et al. 2016 [a21] | [S] |
| Aha tracks a drop in perceived difficulty | correct solutions beta=0.18, p<.001; incorrect 0.03, p=.734 | Moroshkina 2024 [b09] | [S] |
| Progress cues change solve rates (matchstick) | Exp 2 standard tautology 12% (4/32) low-value vs 62% (21/34) high-value; reverse 72% vs 77%. Exp 1 (N=121): 77/43/90/77% | Ormerod and MacGregor 2020 [d02] | [C] |
| Maximisation hint solves ten-penny problem | 72% (21/29) vs control 10% (3/30); chi2(1,59)=23.80 | Ollinger et al. 2016 [b12] | [S] |
| Nine-dot: nobody solved the plain version in Exp 1; 80-93% solved simpler variants | second-hand | MacGregor 2001 via Spiridonov [d04] | [C] |
| Hidden-state probe predicts intermediate-answer correctness | R1-Distill-Llama-8B in-domain acc .77 GSM8K, .80 MATH, .85 AIME; ECE .03-.10; to AIME out of domain ECE .25-.31 | Zhang et al. 2025 [c01, c02] | [E] |
| Probe-based early exit | threshold 0.85: 88.2% acc, ~24% fewer tokens (static exit ~82.5%) | Zhang 2025 [c03] | [S] |
| Large models know what they know | P(IK) AUROC 52B: .928 code, .864 LAMBADA, .687 GSM8K (TriviaQA-trained) | Kadavath 2022 [c04] | [E] |
| Intrinsic self-correction lowers accuracy | GPT-3.5 CommonSenseQA 75.8 to 38.1 (3 calls); GPT-4 GSM8K 95.5 to 91.5 to 89.0; oracle labels help (GPT-3.5 GSM8K 75.9 to 84.3) | Huang et al. 2023 [c05] | [E] |
| Overthinking | first solution correct >92%; mitigation -44.7% tokens at 93.0 to 92.8 (MATH500) | Chen et al. 2024 [c06] | [E] |
| Underthinking | >70% of incorrect responses hold a correct thought; wrong answers use 225% more tokens, 418% more switches; Tip penalty QwQ AIME24 38.3 to 44.1 | Wang et al. 2025 [c07] | [E] |
| Confidence/convergence early stopping cuts tokens | DEER: R1-Distill-Qwen-7B 64.2 to 69.2, 38.5% shorter; Qwen3-14B 82.8 to 83.7, 42.9% shorter. CoDE-Stop: -19 to -43% cost, accuracy -1.5 to -5.2. Answer convergence: ~40% fewer tokens on NQ | [c11, c12, b22] | [E] |
| Single-signal stoppers can fall below vanilla | Qwen3-8B AIME24 vanilla 72.22, DEER 70.00, CyclicReflex 65.55, UPAIR 77.78 | UPAIR 2026 [b20] | [S] |
| Combined uncertainty + progress monitor | higher accuracy in 15/15 settings; flags 64.3% of natural errors, 5.4% of correct; QwQ-32B AIME25 15/30 to 20/30 (5 fixed, 0 broken) | UPAIR 2026 [b19, b21] | [S] |
| Tree of Thoughts value prompt | Game of 24: IO 7.3, CoT 4.0, CoT-SC 9.0, ToT b=1 45, b=5 74 | Yao et al. 2023 [c09] | [E] |
| Reflexion hard stall rule (3 repeats or 30 actions) | AlfWorld 130 of 134 solved, +22%; HotPotQA 0.39 to 0.51 | Shinn et al. 2023 [c10] | [E] (thresholds not ablated) |
| Self-monitoring navigation | R2R val-unseen SR beam 0.49 vs 0.57 with progress monitor | Ma et al. 2019 [c18] | [S] |
| Metacognitive harness (confidence between attempts) | Sonnet-4.6 pooled 48.3 to 56.9 (+8.6, N=1,859), 2.4 attempts, $0.78/q; LCB v6 74.3 to 84.3 | Cao et al. 2026 [c14, d22] | [S] |
| Within-solve confidence has no resolution | within-problem SD 0.048 vs across problems 0.270 (5.6x) | Cao 2026 [c15, d22] | [S] |
| Humans vs LLMs on insight riddles | humans 52.9% (n=126); non-reasoning 7.6%, reasoning 17.6%; verification failures 5.23-39.34% of wrong answers | Nazonazo 2025 [b17] | [S] |
| Loops: common in some setups, rare in others | MAST: step repetition 15.7%, unaware of termination 12.4%; Meta production: loops 2.18% (Sonnet 4.5), 3.59% (Opus 4.5); CodeGym under compression 26-57% | [c17, d12, d16] | [E] |
| Enforced "answer after 5 useless results" works; advice does not | success +0.026 to +0.097; pre-registered replication on 300 fresh questions; running count in prompt delta -0.14 to -0.24 | Judged Useless 2026 [d18, d19] | [E] (with Wink) |
| Loop Breaker helps loop-prone backbones only | Gemini 3 Flash 63.14 vs 58.90 (50 steps), 68.77 vs 66.95 (100); Sonnet 4.6 71.67 vs 71.63 | VLAA-GUI 2026 [d17] | [E] with d14, d16 |
| False stops are large | OnTrack shipped point interrupts 13-21% of benign traces; reference-free 29-32 of 40 benign flagged | OnTrack 2026 [d15] | [E] |
| Hidden-state probes predict agent failure from round 1 | AUC .86 and .81 round 1 (TextCraft); tokens saved at 90% recall up to 60.2%; behaviour-only 9.9% vs probe 41.6% | Ruan et al. 2026 [d23] | [S] |
| Spontaneous text-level "aha" shifts do not predict success | N=723,200: accuracy 2.57% with shift vs 16.44% without | d'Aliberti and Ribeiro 2026 [d24] | [S] |
| Forced second pass under high entropy | Math 0.3221 to 0.4062 (+8.41 pp); Crosswords +0.45 pp | same [d25] | [S] |
| Rewind alone is mixed; rewind plus carried lessons large | MineSweeper 58.8 / 63.5 / 95.3% | ReTRAIL 2026 [d28] | [S] |
| Nudge recovery | single 90.93%, multiple 79.07%; 37% of non-recoveries ignored the guidance | Wink 2026 [c16, d13] | [S] |

## 4. Mechanisms and models

Each mechanism is written so it could be coded.

**4.1 Criterion for Satisfactory Progress (human theory, binary).**
- Input: a current state and a count of moves left (nine-dot: lines available).
- Compute ratio = distance_to_goal / moves_left (nine-dot: dots remaining / lines remaining). Compare with a fixed criterion set from the problem statement.
- If the best available move meets the criterion, take it (maximisation / hill climbing, lookahead 1 to 4).
- If no move meets it, criterion failure: relax the current constraint or widen the search (ACT-R model: relaxation of the minimisation heuristic). [d01, d03]
- Model output: solution rate under 5% in 50 runs on nine-dot; 13-dot variant solved within 2 runs; 12 and 11 dot variants within 10 runs. [d03]
- Engineering reading: the trigger is a computed ratio on the problem, with a known number of steps. Our agent seldom has a ratio like this. It can borrow only the shape: a pre-set criterion, a binary trip, then a widened search.

**4.2 Warmth monitor (human, graded).** Sample a nearness rating every k seconds. Gradual rise predicts a stepwise solve; flat then jump predicts a restructuring solve. Differential warmth needs two ratings (last minus earlier). Weaknesses: needs many ratings per problem (40 in 1987, 5 in 2016), per-item agreement with Aha reports is r=.08, and rating may disturb the solve. [a06, a10, b07] Do not implement as a trigger.

**4.3 Exact-repeat / stall rule (code).**
- Loop = same tool call and same observation, i.e. a step with no new information (DeLoop). [d16]
- Reflexion: same action and same response for more than 3 cycles, or more than 30 actions. [c10]
- VLAA-GUI Loop Breaker, tiered: tier 1, same action with no visible change twice, force a different interaction mode; tier 2, same screen 3 times, force a different overall strategy; tier 3, an external judge says keep or switch, and the repeated action is blacklisted. [d17]
- OnTrack: loops, stalls, repeated tool calls without new results. Simple loop and stall rules matched the full monitor's recall. [d14]
- Cost: near zero. Value depends on how loop-prone the backbone is.

**4.4 Count of useless results (code-enforced).** Ask a cheap judge (or a lexical detector) whether each result added information. After 5 consecutive "useless" results, code forces the answer or disables the failing tool. Do not rely on the model to act on its own judgment. A cheap lexical detector (few shared content words) did about as well as the agent at flagging useless results. [d18, d19]

**4.5 Answer-stability / convergence stop.**
- At each "Wait" or chunk boundary, force a trial answer (DEER). Stop if geometric-mean token confidence is above 0.95. [c12]
- Or count identical intermediate answers; k=10 matching chunks gave over 40% fewer tokens on NQ. Late stop is the main error (63.6% of stops late on GPQA with R1-Qwen-32B). [c11]
- CoDE-Stop: trend-aware confidence indicator; stop threshold ramped 0.9 to 0.95; steps split at Wait tokens. [b22, b23]
- Needs token log-probs or a forced answer step.

**4.6 Graded state value inside search (ToT).** Prompt the model to rate each partial solution sure / maybe / impossible. Prune "impossible", expand "sure" first. Gain: Game of 24 45% (b=1) to 74% (b=5). Known flaw: marks rare-but-valid items impossible. Keep a safety rule: do not prune on this alone. [c09]

**4.7 Hidden-state probe (needs open weights).** Train a small probe on activations at intermediate-answer positions. It predicts correctness of that answer (accuracy to .85). It predicts agent failure from round 1 (AUC .86). Calibration breaks out of distribution (ECE up to .31), so recalibrate per domain. Not usable with a closed API. [c01-c03, d23, d26]

**4.8 Metacognitive harness (between attempts).** Read feeling-of-knowing before solving and judgment-of-learning after each attempt. Threshold in code, then trust, retry with compact feedback, or aggregate. Diagnose each model first: pass thresholds AUROC >= 0.60 and ECE <= 0.15. Of 9 models only Opus-4.6 besides Sonnet-4.6 reached "adequate metacognition". Re-feeding the full failed context hurt (40.0 vs 45.0 with no prior state; compact feedback best). [c14, c15, d21]

**4.9 Uncertainty-progress alignment (UPAIR).** Combine answer uncertainty (entropy from a small proxy model) with a hidden-state progress measure. Classify healthy / stagnant / ready. Act: continue, switch strategy or stop. Monitoring overhead 0.88% of decode time. [b19, b21]

**4.10 Response after the trigger.** Options in the literature: inject guidance (Wink), force a switch by disabling the tool (Judged Useless), escalating forced switches (Loop Breaker), rewind with carried lessons (ReTRAIL), retry with compact feedback (Cao). No controlled comparison of switch vs restart vs ask vs stop exists. [d13, d17-d19, d21, d28]

## 5. What holds up

**Replications and failures.**
- Warmth contrast: one founding study (small usable N: 19 and 39; one-tailed tests), one non-replication (d=.12, N=51), one partial replication when insight is redefined as an Aha report (d=.82, 27 usable). Net: [C]. The shape depends on how insight is defined and how many ratings are taken. Hedne's explanation (100% confidence rule and 40 vs 5 ratings) was never directly re-tested; we found no re-test. [b26, d31]
- Metacognitive discrimination: Az .56 (chance) for insight solutions in magic tricks vs AUC .90 in Mooney images (N=10). Different tasks. [C]
- Stuck reports unreliable: one study, N=101 after exclusions. [S]
- Anagram nearness: no support found; the one anagram study read (abstract) says all-or-none. [S]
- Nine-dot and eight-coin: eight-coin data attribute difficulty to representation and grouping as well. The progress-criterion account is [C]. [d06]

**Moderators.**
- How insight is defined (problem type vs solver report). [a21, a12, a10]
- Rating density and confidence requirement. [b26]
- Whether the solver is correct. Aha follows correctness more than restructuring. [a23]
- Backbone strength for machine loops: Loop Breaker helped Gemini 3 Flash, nothing for Sonnet 4.6. [d17]
- Budget and context compression: loops 57.3% for Qwen3-8B under compression. [d16]
- Domain shift: probes and thresholds do not transfer (ECE .25-.31). [c02]
- Task difficulty: convergence stops come later on hard tasks (convergence point ~0.9 on GPQA/AIME vs ~0.8 on GSM8K/MATH). [c11]

**Interventions that worked.**
- Code-enforced response to repeated no-progress (Judged Useless; replicated pre-registered). [d18]
- Loop Breaker escalation on loop-prone backbones. [d17]
- Confidence-based early stop on math (token cuts 19-85%, accuracy flat or small loss). [c12, c13, b22]
- Compact feedback on retry. [d21]
- Rewind plus reflection-guided retries. [d28]
- Uncertainty-plus-progress combination. [b19]
- Thought-switch penalty against underthinking. [c07]
- Forced reconsideration gated by entropy (math only). [d25]
- Hard stall rule inside a live loop (Reflexion). [c10]

**Interventions that did not work, or hurt.**
- Intrinsic self-correction with no external signal (GPT-3.5 CommonSenseQA 75.8 to 38.1 at 3 calls; GPT-4 CommonSenseQA stayed 82.0 / 79.5 / 80.0, so do not generalise the collapse). [c05]
- Prompted stopping rules, price cues, budgets and an LLM-written running count (delta -0.14 to -0.24 for three small models). [d18, d19]
- A backup tool alone did not make agents leave (delta at most +0.02). [d19]
- Bare rewind: mixed or lower. [d28]
- Re-feeding the full failed trace. [d21]
- Single-signal baselines on some benchmarks (DEER, CyclicReflex, Think-or-Not below vanilla in places). [b20]
- Aggressive DeepConf filtering lost points in 8 of 20 offline settings (-0.31 to -4.69 pp). [c13]
- Detectors trained on injected faults fall to chance on organic failures. [d29]
- Task-generic trajectory signals: length-controlled AUROC 0.526. [d15]
- Spontaneous text "aha" reflection: nearly half of R1-Zero reflective responses were no more accurate. [c20, d24]

**False-trigger cost.** OnTrack aborts saved 17-18% of compute on failing runs at about 83% precision, but the shipped point interrupted 13-21% of benign traces. UPAIR's stagnation flag caught 64.3% of natural errors and flagged 5.4% of correct samples. [d14, d15, b19]

## 6. Language models

**What they can do.**
- Judge their own state with signal: P(IK) AUROC to .93 on code and .69 on GSM8K for a 52B model, rising with scale; zero-shot P(True) is poorly calibrated. [c04]
- Models mark a failing source useless 97 to 100% of the time. [d18]
- Hidden states hold an early answer. Probes decode the final answer far before text shows it (up to 80% token cut on MMLU, 30% on GPQA-D). [d26]
- Confidence trajectories carry information. Correct runs reach high confidence early. Premature confidence (early commitment then rationalising) predicts flawed reasoning. [b22, d27]

**What they cannot do.**
- Act on their own judgment. Seven agents rarely stopped on "useless" judgments. Reasoning mode and larger models largely still failed. Only Claude Sonnet 5 partly stopped without prompting. [d18, d19]
- Revise correctly without external feedback. [c05]
- Read their own progress within a solve. Within-problem confidence SD is 0.048. [d22]
- Report drivers in text. Hints acknowledged 25% (Claude 3.7 Sonnet) and 39% (R1). [c22]
- Pick the right answer they already wrote. Verification failures 5.23% to 39.34% of wrong answers. [b17]
- Match humans on insight riddles. 7.6% and 17.6% against 52.9%. GPT-5 fell inside the human CI. CresOWLve: best Gemini-3.1-Pro 51.29% exact match English. [b17, c23]

**Failure modes in both directions.**
- Overthinking: first solution correct >92%; keep going afterwards. [c06]
- Underthinking: abandon promising lines. [c07]
- Collapse at high complexity: effort falls before accuracy collapses; fixation on an early wrong attempt. [c08] (methods contested)
- Agent loops: 2.18-3.59% of production trajectories at Meta, 5.21% in the Wink dataset, 15.7% of annotated multi-agent failure modes, up to 57% of small-model CodeGym episodes under compression. [c16, c17, d12, d16]

**What changed behaviour, by how much.**
- Code-enforced stop after 5 useless results: +0.026 to +0.097 success; unaided agents lose 6-13 points against the best fixed cap in hindsight. [d18]
- Loop Breaker: +4.2 (50 steps) on Gemini 3 Flash OSWorld; +5.2 on Windows Agent Arena at 100 steps; ~0 on Sonnet 4.6. [d17]
- Metacognitive harness: +8.6 pooled on Sonnet-4.6. [c14]
- Early exit: token cuts of 19-85% with accuracy within -5.2 to +5.8. [c12, c13, b22]
- Hard stall rule: +22% AlfWorld. [c10]
- Probe cascade: up to 60.2% tokens saved at 90% recall of successes. [d23]

**Gaps.** No study gives LLMs the human paradigms (anagram solvability, warmth, magic tricks). No study asks a model for warmth mid-solve and checks the curve. [c24, d31] The two negative searches ran under a depleted search budget, so this is absence under limited search.

## 7. What our agent should take

### Add now (established)

| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| N1 | Trigger S6 on external, code-computed signals (repeat count, unchanged error, unchanged answer, test result), never on the model's statement that it is stuck or close | S6, G1, G10 | [E] | K05, K14; c05, c22, a18, a19, d18 |
| N2 | Enforce the S6 response in code (disable the failing tool, force the next operator, block the repeated action). Do not leave it as advice in the prompt | S6, O | [E] | K20; d18, d19, d17, d13 |
| N3 | Add a cheap exact-repeat rule (same call plus same observation twice or three times) as a first-tier stall signal; log how often it fires | S6 | [E] | K21; d16, d17, d14, c10 |
| N4 | Set thresholds from our own benign traces and price a false stop against the savings; never copy a threshold from the literature | S6, G7 | [E] | K22; d15, d12, d29 |
| N5 | Do not use verbal confidence or a within-solve "closeness" score as a trigger. Use self-rated confidence only between attempts, or to size effort per problem | S0, G12, 4b | [E] | K24, K14; d22, c15, c05 |
| N6 | Guard both ways: a stop-too-late guard (answer stable, first solution passes) and a switch-too-early guard (do not leave a line a check rates as promising) | S6, G11 | [E] | K12; c06, c07, c11 |

N1, N5 and the "verbal confidence to stop" row in SCHEMA 4b agree. N2 and N3 are the new additions to S6; the schema already has code-fired S6.

### Test first

| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| T1 | Count rule vs graded confidence trigger vs both, at equal tokens, on our items | S6 | [C] | K23; d20, d21, d14 |
| T2 | Answer-stability stop (same candidate answer in the last k attempts or chunks) | S3, S4, S6 | [E] on math, untested on agent tasks | K10; c11, c12, b22 |
| T3 | Which response after the trigger: forced switch, restart, ask, stop | S6, O | [S] | K29; d13, d19, d28 |
| T4 | Compact failure summary carried to the next attempt (vs none, vs full trace) | S5, S6, memory | [S] | K29; d21, d28 |
| T5 | Prior difficulty from class pass rate sets the budget and the S6 threshold | S0, G12 | [S] human | K08; a03 |
| T6 | Early-commitment flag: a very early jump to certainty marks a risk | S6, G1 | [S] | K28; d27 |
| T7 | Process-score guard against abandoning promising lines | S6 | [S] | K27; c07, d30 |
| T8 | Escalating tiers (action, then strategy, then judge) vs single tier | S6 | [S] | K21; d17 |
| T9 | Treat text-level "wait, aha, actually" as noise (do not count as progress) | G10 | [S] large N | K28; d24, c20 |
| T10 | Warmth-style closeness probe mid-solve | S6 | [C] human only | K02, K03; a06, a12 |

## 8. Concrete tests on our bench

All arms get the same total token budget (including monitor calls, retries and setup). Report accuracy, tokens and false-stop rate with 95% intervals. Use at least 100 items per arm per cell; Cao's 100-item ablation had intervals about 20 points wide, so smaller sets decide nothing. [d21]

| Test | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| B1 Count vs graded trigger | multi-step code and tool items with a check; ARC-style and brainteaser items | (a) no trigger; (b) exact-repeat / no-new-output count; (c) graded confidence between attempts; (d) b plus c | pass rate at equal tokens; false-stop rate on items the plain run solves | (b) matches (c) at lower cost on loop-prone runs; (d) best by 1 to 3 points; if (b) equals (d), drop (c) |
| B2 Advice vs enforcement | items where the first operator fails | prompt says "switch if stuck"; code forces the next operator after the trip | pass rate; share of trips followed by a changed approach | forced beats advice (Judged Useless: +0.03 to +0.10) |
| B3 Threshold sweep | same items; repeat limits 2, 3, 5 | each limit | pass rate, tokens, false-stop rate | knee near 3 for exact repeats; false stops rise below 3 |
| B4 Answer-stability stop | single-exact-answer items | no stop; stop when same answer in k=2 or 3 attempts | accuracy at equal tokens; late-stop share | 20 to 40% token cut, accuracy within 1 point on easy items; no gain on hard |
| B5 Response comparison | items that trip S6 | forced switch; switch plus compact failure summary; restart from scratch; stop and submit best | pass rate among tripped items at equal tokens | switch plus summary beats bare switch; restart weakest unless lessons carried |
| B6 Within-solve rating | all items | log a 0-10 closeness rating each step; no action | AUROC of the rating at step k vs final pass; compare with repeat count and test-pass count | rating near chance within a solve; external signals AUROC 0.6 to 0.8 |
| B7 Underthinking guard | long-reasoning items | trigger only; trigger plus "do not abandon if the last check improved" | pass rate; switch count | small gain where the backbone switches often |
| B8 Early-commitment flag | items with a check | log first-attempt certainty and step of first full answer | AUROC for failure | flag predicts wrong answers |
| B9 Prior-difficulty budget | mixed-difficulty set | uniform budget vs budget by class pass rate | accuracy at equal total tokens | small gain; G12 already claims over 4x efficiency |

## 9. What does not transfer, and why

- **Warmth curves.** Humans rate warmth while solving; per-item agreement with Aha reports is r=.08 and the contrast failed to replicate once. Our model's within-solve rating barely moves (SD .048). [a10, a06, d22]
- **Anagram all-or-none finding.** A limit on human partial information in a task where the answer pops. LLMs have token probabilities that do carry partial information. [d07]
- **The nine-dot criterion ratio.** Needs a known goal distance and move count. Open-ended tasks have neither. Only the shape (preset criterion, binary trip) carries over. [d01]
- **Human threshold values.** Humans overharvest and persevere. LLMs both loop and abandon too soon. Thresholds cannot be copied. [d10, d11, c07]
- **"Feeling close often marks a wrong answer" (Metcalfe).** Single-source and tied to human insight problems. Premature confidence in LLMs is a separate result. [a26, d27]
- **Hidden-state probes and attention-state stops.** Strong results, but need open weights and per-domain recalibration (ECE up to .31). If the agent runs on a closed API, skip. [c02, d23, b24]
- **Token-saving early exit on math.** Gains are token savings, not new accuracy. It does not test a no-progress trigger in open-ended agent work. Math has a single exact answer to converge on. [c11, c12]
- **Navigation progress monitor.** Trained regression to ground-truth distance, which text tasks lack. [c18]
- **Trained fixes** (Tip penalty, DeLoop training, ReTRAIL policy, premature-confidence RL, MERA). They change the model. We change the scaffold. Only the idea transfers. [c07, d16, d28, d27, c21]
- **Human stuck button.** Asking the model "are you stuck?" is the LLM equivalent and is as unreliable. [a18, d18]

## 10. Open questions

1. Does a code-set repeat/count rule beat a graded confidence trigger at equal tokens on open-ended agent tasks? No head-to-head exists. [K23]
2. What did MacGregor, Ormerod and Chronicle 2001 and 2002 actually report (N, solve rates, criterion numbers)? Not read.
3. Do anagram solvability judgments change with time (Novick and Sherman 2003)? Not read. Smith and Kounios (abstract) point the other way.
4. What is the false-trigger rate of a pure repeat-count rule on long non-coding traces?
5. Which response after a trip works best: switch, restart, ask or stop?
6. Is there a human analogue to LLM underthinking? None found; humans overharvest. [d10]
7. Would a direct re-test of Hedne (100% confidence rule, 40 vs 5 ratings) resolve the warmth dispute? None found. [d31]
8. What happens when a model rates warmth mid-solve? Nobody asked. [d31]
9. Does enforced stopping still help with larger reasoning models? Only Sonnet 5 partly stopped unaided. [d19]
10. Do thresholds hold across backbone changes? Loop Breaker helped weak backbones only. [d17]

## 11. Sources

[V] = opened and read this session (page or PDF text). [M] = snippet, or second-hand only. Entries marked "abstract page" were opened but only the abstract was read.

**Human studies**
- [V] Metcalfe and Wiebe (1987) Intuition in insight and noninsight problem solving. https://link.springer.com/content/pdf/10.3758/BF03197722.pdf (a01-a05)
- [M] Metcalfe (1986b) as described in the above (a04); Metcalfe 1986 as read by Hedne (a09); b01 summary only.
- [V] Hedne, Norman and Metcalfe (2016) Magic tricks. https://pmc.ncbi.nlm.nih.gov/articles/PMC5005374/ (a06-a09, b02-b04, b26)
- [V] Laukkonen and Tangen (2018) How to detect insight moments. https://www.frontiersin.org/articles/10.3389/fpsyg.2018.00282/full ; https://pmc.ncbi.nlm.nih.gov/articles/PMC5854655 (a10, a11, b06, b07)
- [V] Kizilirmak et al. (2018) Feelings of warmth. https://www.frontiersin.org/articles/10.3389/fpsyg.2018.01404/full ; https://pmc.ncbi.nlm.nih.gov/articles/PMC6099077/ (a12, a13, b05, b27)
- [V] Durso, Rea and Dayton (1994) Graph-theoretic confirmation of restructuring. https://shareok.org/bitstreams/8d38153e-1c56-4b12-be21-b0d1848d888b/download (a14-a17)
- [V] Fedor, Szathmary and Ollinger (2015) Five square problem. https://www.frontiersin.org/articles/10.3389/fpsyg.2015.01050/full (a18-a20)
- [V] Webb, Little and Cropper (2016) Insight is not in the problem. https://www.frontiersin.org/articles/10.3389/fpsyg.2016.01424/full (a21, a22; Davidson 1995 second-hand [M])
- [V] Wiley and Miller (2026) Aha ratings as metacognitive judgments. https://pmc.ncbi.nlm.nih.gov/articles/PMC13608503/ (a23, b10)
- [V] Chandolia et al. (2026) Aha in problem solving and ideation. https://pmc.ncbi.nlm.nih.gov/articles/PMC13514830/ (a24)
- [V] Working memory and representational change (2018). https://www.frontiersin.org/articles/10.3389/fpsyg.2018.01864/full (a25)
- [V] Ishikawa, Toshima and Mogi (2019). https://pmc.ncbi.nlm.nih.gov/articles/PMC6538685/ (b11; a26 abstract and intro only)
- [V] Graf et al. (2023) change point analysis. https://pmc.ncbi.nlm.nih.gov/articles/PMC10219327/ (b08)
- [V] Moroshkina et al. (2024). https://pmc.ncbi.nlm.nih.gov/articles/PMC10844378/ (b09)
- [V] Ollinger et al. (2016) ten-penny problem. https://pmc.ncbi.nlm.nih.gov/articles/PMC5533865/ (b12)
- [V] Spiridonov et al. (2019) nine-dot motor activity. https://pmc.ncbi.nlm.nih.gov/articles/PMC6352738/ (b13, d04)
- [V] Doulfoukar et al. (2026) active inference account. https://pmc.ncbi.nlm.nih.gov/articles/PMC13585804/ (b14)
- [V] 2021 insight review. https://pmc.ncbi.nlm.nih.gov/articles/PMC8715918/ (b15)
- [V] Friedlander and Fine (2018) cryptic crosswords. https://pmc.ncbi.nlm.nih.gov/articles/PMC6037892/ (b16)
- [V] Ormerod and MacGregor (2020) CogSci. https://cognitivesciencesociety.org/cogsci20/papers/0067/0067.pdf (d01, d02)
- [V] Ormerod, Rusconi and Banks (2015) ICCM. https://iccm-conference.neocities.org/2015/proceedings/papers/0046/paper0046.pdf (d03)
- [V] Harhen and Bornstein (2023) overharvesting. https://pmc.ncbi.nlm.nih.gov/articles/PMC10068834/ (d10)
- [V] Incubation and interactivity (2020). https://pmc.ncbi.nlm.nih.gov/articles/PMC6994426/ (d11)
- [V, abstract page] Ormerod, MacGregor and Chronicle (2002). https://eprints.lancs.ac.uk/id/eprint/3613/ (d05)
- [V, abstract page] Ollinger et al. (2013) eight-coin. https://pubmed.ncbi.nlm.nih.gov/22799283/ (d06)
- [V, abstract page] Smith and Kounios (1996). https://researchdiscovery.drexel.edu/esploro/outputs/journalArticle/Sudden-Insight-All-or-None-Processing-Revealed-by/991020548387304721 (d07)
- [V] Smith and Healy (1998). https://link.springer.com/content/pdf/10.3758/BF03211376.pdf (d08)
- [M] MacGregor, Ormerod and Chronicle (2001). https://doi.org/10.1037/0278-7393.27.1.176 (a27; not read)
- [M] Novick and Sherman (2003). https://doi.org/10.1080/02724980244000288 (d09, a28; not read)
- [M] Chu, Dewald and Chronicle (2007), Davidson (1995), Metcalfe (1986), Bowers et al. (1990): cited in other papers only.

**LLM and AI studies**
- [V] Zhang et al. (2025) Reasoning models know when they are right. https://arxiv.org/abs/2504.05419 (c01-c03)
- [V] Kadavath et al. (2022). https://arxiv.org/abs/2207.05221 (c04)
- [V] Huang et al. (2023). https://arxiv.org/abs/2310.01798 (c05)
- [V] Chen et al. (2024) overthinking. https://arxiv.org/abs/2412.21187 (c06)
- [V] Wang et al. (2025) underthinking. https://arxiv.org/abs/2501.18585 (c07)
- [V] Shojaee et al. (2025). https://arxiv.org/abs/2506.06941 (c08; first 100k characters)
- [V] Yao et al. (2023) Tree of Thoughts. https://arxiv.org/abs/2305.10601 (c09)
- [V] Shinn et al. (2023) Reflexion. https://arxiv.org/abs/2303.11366 (c10)
- [V] Answer convergence (2025). https://arxiv.org/abs/2506.02536 (c11)
- [V] DEER (2025). https://arxiv.org/abs/2504.15895 (c12)
- [V] DeepConf (2025). https://arxiv.org/abs/2508.15260 (c13)
- [V] Cao et al. (2026) metacognitive harness. https://arxiv.org/abs/2605.14186 (c14, c15, d21, d22)
- [V] Wink (2026). https://arxiv.org/abs/2602.17037 (c16, d12, d13)
- [V] Cemri et al. (2025) MAST. https://arxiv.org/abs/2503.13657 (c17)
- [V] Ma et al. (2019) self-monitoring navigation. https://arxiv.org/abs/1901.03035 (c18)
- [V, abstract page] Ma et al. (2019) Regretful Agent. https://arxiv.org/abs/1903.01602 (c19)
- [V] Liu et al. (2025) R1-Zero. https://arxiv.org/abs/2503.20783 (c20)
- [V] MERA (2025). https://arxiv.org/abs/2508.04460 (c21)
- [V] Chen et al. (2025) reasoning models don't always say what they think. https://arxiv.org/abs/2505.05410 (c22)
- [V] CresOWLve (2026). https://arxiv.org/abs/2604.03374 (c23)
- [V] Japanese riddles / Nazonazo (2025-26). https://arxiv.org/abs/2509.14704 (b17, b18)
- [V] UPAIR (2026). https://arxiv.org/html/2607.17188v2 (b19-b21)
- [V] CoDE-Stop (2026). https://arxiv.org/html/2604.04930v2 (b22, b23)
- [V] OnTrack (2026). https://arxiv.org/abs/2610.12375 (d14, d15)
- [V] DeLoop (2026). https://arxiv.org/abs/2610.19376 (d16)
- [V] VLAA-GUI (2026). https://arxiv.org/abs/2604.21375 (d17)
- [V] Judged Useless, Queried Anyway (2026). https://arxiv.org/abs/2610.06191 (d18, d19)
- [V] EAT (2025). https://arxiv.org/abs/2509.26522 (d20)
- [V] Doomed from the Start (2026). https://arxiv.org/abs/2607.06503 (d23)
- [V] Illusion of Insight (2026). https://arxiv.org/abs/2601.00514 (d24, d25)
- [V] Reasoning Theater (2026). https://arxiv.org/abs/2603.05488 (d26)
- [V, abstract page] Premature confidence (2026). https://arxiv.org/abs/2605.24396 (d27)
- [V] ReTRAIL (2026). https://arxiv.org/abs/2610.13058 (d28)
- [V, abstract page] Real-time detection and repair (2026). https://arxiv.org/abs/2608.02464 (d29)
- [V, abstract page] SmartSwitch (2025). https://arxiv.org/abs/2510.19767 (d30)
- [M] ASAG (2026). https://arxiv.org/abs/2606.15070 (b24, abstract only)
- [M] Early-exit family LYNX, PUMA, STACK, ReCo, search listing only. https://arxiv.org/search/?query=overthinking+reasoning+models+early+stopping+confidence&searchtype=all (b25)
- [M] Negative searches c24 and d31 (absence under limited search). c25 is our own synthesis, not a source.

## Source audit (2026-11-01)

Fresh auditors re-opened the sources of 12 established claims: 6 confirmed as written, 6 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **A02.07-K05** (reworded: the sources support less). The sources study post-solution Aha! ratings and perceived difficulty, not felt closeness/warmth during solving; Webb even notes warmth ratings were a different measure. Corrected claim: Aha! ratings (post-solution judgments of insight) behave like inferred metacognitive judgments built from cues such as processing fluency, solution correctness and a correct first move, rather than direct readouts of the underlying problem-solving process (Wiley & Miller 2026, N=377; Moroshkina 2024; Webb 2016).
- **A02.07-K09** (reworded: the sources support less). Numbers match R1-Distill-Llama-8B, but ECE reaches 0.13 for other reasoning models, and the non-reasoning result is a probe trained on Llama-3.1-8B-Instruct performing much worse, not a transfer of the reasoning-model probe. Corrected claim: In long-CoT reasoning models (mainly R1-Distill-Llama-8B), hidden-state probes predict correctness of intermediate answers with in-distribution ROC-AUC above 0.7 (about 0.82-0.84) and ECE mostly below 0.1 (0.03-0.10 for Llama-8B; up to 0.13 for other models); transfer between GSM8K and MATH is good but calibration is poor on harder AIME (ECE 0.25-0.31), and a probe trained on the non-reasoning Llama-3.1-8B-Instruct performs much worse.
- **A02.07-K10** (reworded: the sources support less). Token cuts (19-85%) check out, but accuracy changes are not all small: UPAIR reports up to +16.67 points and DeepConf up to about +6 points (86.7 to 92.5), with other methods losing some accuracy. Corrected claim: Confidence/answer-convergence based early stopping and selection methods (DEER, DeepConf, CoDE-Stop, answer convergence, UPAIR) cut tokens by roughly 19-85% depending on method and model, with accuracy about unchanged for some, small losses for others, and gains for several (up to +16.67 points for UPAIR on QwQ-32B AIME 2025).
- **A02.07-K12** (now single-source: the sources are not independent). Both supporting papers (overthinking, underthinking) are from the same Tencent AI Lab group with heavily overlapping authors (Chen, Xu, Liang, He, Liu, Tu, Mi, Yu); the numbers (>92%, >70%) are correct.
- **A02.07-K16** (number corrected). Wink 5.21%, 2.18%/3.59% and MAST 15.7%/12.4% check out, but DeLoop's compressed-history loop rates are 38.5% (32B), 42.9% (14B) and 57.3% (8B); 26% is not a compressed-baseline rate. Corrected claim: Real agent loops are common: step repetition 15.7% and unaware-of-termination 12.4% of multi-agent failures (MAST); loops 5.21% of coding-agent trajectories at Meta (Wink), but infinite loops only 2.18% (Sonnet 4.5) and 3.59% (Opus 4.5) in the same paper, so the rate depends strongly on the setup; under context compression exact-repeat loops reached 38.5-57.3% of CodeGym episodes (DeLoop, Qwen3-32B/14B/8B).
- **A02.07-K17** (reworded: the sources support less). Nazonazo numbers are right, but GPT-5 fell within the human 95% CI, CresOWLve has no human comparison, and a universal 'no study' absence claim cannot be established from these sources. Corrected claim: Most evaluated models fall well below humans on insight-riddle benchmarks (Nazonazo: non-reasoning models average 7.6% and reasoning models 17.6% vs a human mean of 52.9%, with GPT-5 inside the human 95% CI); we found no study that gives LLMs the classic human progress-monitoring paradigms (anagram solvability, warmth, magic tricks).
