# Overthinking: deep document

*Subfield C01.10. Key work: Zhou et al. 2026, arXiv 2604.10739. Evidence: evidence_a-d.jsonl (ids a01-a25, b01-b28, c01-c27, d01-d23), claims K01-K26, critique.md. Schema parts: G11 (think briefly), G12 (spend by difficulty), S4, S5, S6, S8, O-stop.*

## 1. What it is

Overthinking means a reasoning model keeps thinking after it has the answer, and the extra thinking does no good or does harm. The word covers three different things. Do not mix them.

1. **Waste.** The extra tokens change nothing. Chen et al. (2024): for "2+3" o1-like models used 1,953% more tokens than conventional models. The first solution was correct in more than 92% of correct cases. Cost goes up, accuracy does not move. (a10, a11, b12, c09)
2. **Harm by flipping.** The extra tokens make the model drop a correct answer. Zhou et al. (2026) call this a negative flip. This is the "extra tokens lower accuracy" claim of this subfield. (a01-a06, b01-b06, c01-c04)
3. **Harm by task design.** On tasks with distractors, spurious features or big constraint sets, longer reasoning pulls the model off course. Gema et al. (2025) call it inverse scaling. (a07-a09, b07-b11, c05-c08)

A fourth, related thing is the opposite failure, underthinking: the model jumps between ideas and never finishes one (Wang et al. 2025). Wrong answers carry more thought switches. Length alone is a poor proxy for either failure. (a22, b22, c14)

The honest size of the effect: it is small on natural benchmarks (about 1 point of accuracy at the far end of the budget range), large only on built-to-fail tasks, and model-specific. Closed frontier models showed a plateau, not a decline, at coarse effort steps. (K02, K20)

Why it matters for our agent: guardrail G11 says "think briefly by default" and G12 says "spend by difficulty". This document checks how much of G11 stands on overthinking evidence and which stop rules or gates are safe to add.

## 2. History and theories in depth

**Before reasoning models (CoT harm).** Sprague et al. (2025) combined a meta-analysis of over 100 papers with their own tests on 20 datasets and 14 models. Chain of thought helps mainly on math and symbolic tasks: +14.2 symbolic, +12.3 math, +6.9 logical. On MMLU it adds almost nothing unless the question or answer contains an equals sign. This is "no benefit", not harm. (a19) Liu et al. (2025, "Mind Your Step") used psychology (verbal overshadowing, deliberation costs) to predict where CoT hurts, and found harm: artificial grammar learning, GPT-4o direct 94.0% vs o1-preview 57.7% (a 36.3 point drop); GPT-4o with CoT 87.5% to 64.4%; Claude 3.5 Sonnet -1.8 (no effect, p=0.969). Label-learning with exceptions took up to 331% more trials. Other task types gave mixed or no harm. (a18)

**Name and first study (Dec 2024).** Chen et al. defined outcome efficiency (share of tokens up to the first correct answer) and process efficiency (share of tokens in distinct strategies). QwQ-32B-Preview on ASDIV: first solution 287 tokens, 38.7% of the response; outcome efficiency 41.9%, process efficiency 66.5%, 3.5 solutions, 741.8 tokens, accuracy 96.9. On MATH500 Level 1 outcome efficiency was under 50%. Key point: this was a waste finding. Accuracy was mostly unchanged. (a10-a12, b12, c09)

**Underthinking (Jan 2025).** Wang et al.: incorrect responses of QwQ and R1 use 225% more tokens and 418% more thought switches than correct ones. Over 70% of incorrect responses contain at least one correct thought. Conventional LLMs show no such length gap. A decode-time penalty on switch words (TIP) raised QwQ-32B-Preview AIME24 pass@1 from 38.3 to 44.1 (pass@16 62.7 to 74.0). Smaller gains on stronger models: R1-Distill-32B 61.4 to 64.1, DeepSeek-R1 73.8 to 74.8. A prompt-only instruction gave 72.4 on R1, slightly worse. Too strong or too long a penalty lowers accuracy (strength 20, duration over 300). (a22, b22, b23, c14, d21)

**Simple test-time scaling (Jan 2025).** Muennighoff et al. (s1) introduced budget forcing: append "Wait" to extend, force the end-of-thinking token to cut. s1-32B AIME24 50.0 to 53.3 with 2x Wait, up to 57% at the largest budget. But MATH500 fell 93.0 to 90.2 in the 2x-no-string setting, and gains flattened at about six extensions. Suppressing stops too often causes loops. This is the method Zhou later pushes to its limit. (a23, b25, c25)

**Agent version (Feb 2025).** Cuadron et al. defined overthinking in agents as preferring internal simulation to acting on environment feedback. Three patterns: analysis paralysis, rogue actions, premature disengagement. Claude Sonnet 3.5 judged 3,908 scored SWE-bench Verified trajectories (4,018 analysed); the judge agrees with human experts at Spearman 0.800. (a15, b16, b17, c11, c12)

**Theory of length (Feb 2025).** Wu et al.: accuracy is an inverted U in CoT length. Toy model A(N) proportional to ((1-E(N,M,T))(1-eps(T)))^N: each added step adds a chance of error but makes steps easier. Optimal length N* rises with difficulty T and falls with model ability M. (a13, b14, c15)

**Variance theory (Jun 2025).** Ghosal et al.: extra thinking raises output variance. Early on, more variance covers the right answer more often, which looks like gain. Later it lowers precision. (a14, b18, b19, c13, d06)

**Skipping thought (2025).** Ma et al.: an empty thinking block (NoThinking) beats Thinking at small matched budgets. (a20, b26, c17, d09)

**Short is better inside a question (May 2025).** Hassid et al.: for the same question, shorter samples are right more often. (b20, b21, c16, d07, d08)

**Collapse debate (Jun 2025).** Shojaee et al. (Illusion of Thinking): three regimes by puzzle size. Lawsen replied that output limits, scoring and unsolvable River Crossing instances (N>=6) drive part of the collapse. Treat as contested, not as overthinking proof. (a16, a17, b24, c24)

**Key work (Apr 2026).** Zhou et al. measure the budget curve directly at 500-token steps and add flip analysis. This is the paper the subfield is named for. As of Nov 2026 no paper replicates or fails to replicate its flip ratio; 21 citing papers were listed and the five closest cite it as motivation only. (a01-a06, b01-b06, c01-c04, d19)

**2026 follow-ups.** DEER and answer-convergence stop rules (math wins, outside-math losses), learned stop heads in agents (StreamStop), MetaCtrl, a pre-registered confound study (Bulut), switching statistics across 16 models (ADT), a self-selection failure study (DIA). See sections 5 and 6.

**Competing explanations for "more tokens lower accuracy".**
- Real second-guessing: the model rejects a correct answer. Zhou's audit: 67.5% of 80 negative flips (a04).
- Variance: extra thinking widens the output distribution (Ghosal). Not proven causal.
- Difficulty selection: long traces are long because the problem is hard (Hassid terciles, Zhou natural samples). Within each difficulty tercile, correct chains are still shorter (d08), so length is at least a symptom of going wrong.
- Distraction and framing: Gema's tasks.
- Artefact of the forcing method (Wait loops, degradation). In Zhou's audit, 12.5% of negative flips are degradation (repetition).
- Error accumulation per step: Wu's model.

## 3. Core findings with exact numbers

Status key: established / single-source / contested / disputed. Source ids are in the evidence files.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| R1-32B AIME accuracy by budget (60 problems, greedy, budget forcing) | 2K 37.8, 4K 46.5, 6K 50.2, 8K 53.8, 12K 55.8 (peak), 16K 54.9 | Zhou 2026 (b01, c01) | single-source |
| s1-32B same setup | 2K 33.2, 4K 41.8, 6K 44.5, 8K 47.1, 12K 47.6, 16K 45.8 | Zhou 2026 (c01) | single-source |
| Marginal gain per 500 tokens (R1) | +3.2 (0.5-2K), +1.8, +0.9, +0.9, +0.1 (8-12K), -0.3 (12-16K); s1 -0.6 | Zhou (b01, c01) | single-source |
| 12K to 16K drop | -0.9 points, reported CI [-1.4,-0.4]. About half of one problem of 60. No paired test, no seeds | Zhou (a01, d01) | single-source, tiny |
| Negative/positive flip ratio (R1, AIME, cumulative from threshold) | 1K 0.22, 2K 0.32, 4K 0.60, 5K 0.71, 6K 0.87 (CI [0.71,1.05]), 7K 1.09, 8K 1.42 (CI [1.21,1.68], p=0.014), 12K 3.29 (CI [2.87,3.82]), 16K 7.55 (CI [6.12,9.24], p<0.001) | Zhou (a02, b02, c02) | single-source. The p=0.038 for 7K quoted in two lines is not in the paper's table; ignore it |
| Crossover where ratio exceeds 1 | R1 about 7K, s1 about 5K. Accuracy still rises to 12K, so ratio above 1 is not "accuracy falling" | Zhou (a02, critique) | single-source |
| Flip ratio rises because positive flips shrink | positive flips 83 to 11 while negative stay low in absolute terms. Flip ratio vs marginal utility Spearman 0.89 | Zhou (critique, c02) | single-source |
| Optimal budget by MATH-500 level (R1-32B) | L1 about 1.0K, L2 about 1.5-3.0K, L3 4.5K, L4 5.0K, L5 7.5K (7.5x range). Crossover L1-2 at 2K vs L5 at 8K. Mid values read from a figure | Zhou (a03, b03, c03) | single-source |
| Hand audit of 80 R1 negative flips | 54 genuine abandonment (67.5%), 16 exploration divergence (20.0%), 10 degradation (12.5%). Authors coded, single coder | Zhou (a04, b04) | single-source |
| Trace indicators vs negative flips (R1 AIME) | hesitation 0.71, oscillation 0.78, confidence drop 0.63, combined 0.82; precision 76.3% at 80% recall (oscillation 71.5%). Same sample defined and tested them | Zhou (b05, c04) | contested (K05) |
| Natural long traces (no forcing, N=312 over 8K tokens) | accuracy 54.2% (6-8K), 52.1, 49.8, 47.3% (12-16K) vs forced 53.8, 52.4, 50.1, 48.2; flip ratio 1.31 natural vs 1.42 forced | Zhou (a05, b06, c03) | single-source, difficulty-confounded |
| GPQA Diamond (R1-32B) | 2K 41.4, 8K 54.8, 10K 55.6 (peak), 12K 54.9, 16K 53.1; flip ratio 0.28 (2K), 0.51 (4K), 0.93 (8K), 1.18 (10K), 2.84 (16K) | Zhou (a05, b06, c03) | single-source |
| Cost-aware stop | lambda=0.5: stop at 6K, 50% compute cut, about 6 points loss. lambda=1.0 favours 2K. Indicator stop: 97% of peak accuracy at 60% compute. In-sample | Zhou (a06, d01) | single-source, in-sample |
| Wait-forcing on distilled small models | GSM8K: 82.2% to 87.3% (385 to 1,100 tokens) then 70.3% at 15,980; 1.5B sequential -11.8 points at 16K; entropy rises | Ghosal 2025 (a14, b18, b19) | single-source for decline size |
| Parallel vote vs extended thinking at equal budget | up to 20% (abstract) or 22% (intro) higher at 16K; GSM8K 1.5B +10.1 vs -11.8; 47% higher than exact-token | Ghosal (a14, b19, c13) | established direction (K08) |
| Inverse scaling, counting with distractors | Opus 4: near 100% to about 85-90% (Math), about 80% (Python/paradox variant); R1 natural: 70% to 30% with 5 distractors; o3 stable controlled, weak decline natural. 2,500 questions per task, distractors n=1..5 | Gema 2025 (a08, b07, c05) | single-source, adversarial |
| Grades regression (spurious features) | zero-shot inverse scaling in Sonnet 3.7, Opus 4, o3-mini; Qwen3-32B positive; few-shot examples lower RMSE for all models; study-hours correlation 0.73 | Gema (a09, b09, c06) | single-source |
| Zebra puzzles (up to 119 clues) | all models degrade with longer reasoning; natural stronger than controlled; a "cautioned" prompt still shows inverse scaling | Gema (b10, c07) | single-source |
| Survival-instinct item | Sonnet 4 willing-to-be-turned-off 60% to 47% (budgets up to 16,384); o3 72% to 76%; R1 71-72%. 3 seeds, five budgets. Item chosen after seeing the pattern | Gema (a09, c08, d02) | single-source |
| Closed frontier models on basic maths, effort raised | GPT-5 97% medium and high; o3 97% low/medium/high (8% more tokens at high); Gemini-2.5-Flash 92/93/92; Gemini-2.5-Pro peaks at its lowest budget (128 tokens, 90%). Plateau, no decline. 53 models, 14 tasks; reasoning models use about 18x more tokens | Srivastava 2026 (d03) | single-source |
| Qwen3-235B budget curve | smooth gains to 32K on four benchmarks (vendor figure) | Qwen team 2025 (d04) | single-source, vendor |
| Waste on trivial questions | 1,953% more tokens on 2+3; first round correct in over 92% of correct cases; 287 tokens = 38.7% of response on ASDIV | Chen 2024 (a10-a11, b12, c09) | single-source |
| Self-training cuts length | QwQ + SimPO FCS+Reflection: ASDIV 741.8 to 381.6 tokens, 96.9 to 96.8 accuracy, outcome efficiency 41.9% to 77.6%; MATH500 -48.6% (abstract); SimPO -22.3% in another comparison | Chen (a12, b13, c10) | single-source; training, out of scope |
| Optimal CoT shrinks with model size | Qwen2.5 on MATH L5, 30 questions per model: 14 steps (1.5B) to 4 steps (72B) | Wu 2025 (a13, b14) | established direction (K03), small N |
| Shortest vs longest sample, same question (GPQA-D) | LN-Super-49B 69.1% (2,790 tok) vs 57.6% (8,763); R1-32B 64.7 vs 57.1; QwQ-32B 64.7 vs 54.5; R1-670B 75.8 vs 63.1. AIME24 first model: 76.7% vs 33.3% (random 58.8%). Up to 34.5 points | Hassid 2025 (b20) | established (K07) |
| Gap persists within difficulty terciles | LN-Super-49B tokens (K) correct/incorrect: easy 5.3/11.1, medium 11.4/17.1, hard 12.4/16.8; R1-32B medium 14.8/21.6, hard 19.1/22.8; QwQ hard 23.0/31.7 | Hassid Table 2 (d08) | established |
| short-m@k | short-1@k matches or beats majority with up to 40% fewer thinking tokens; short-3@k beats majority at all budgets, up to 33% less wall time; QwQ-32B at 80k tokens short-3@k +2%; R1-670B at 100k about +4%; short-1@k loses to majority at high compute in 3 of 4 models | Hassid (b21, d07) | established, with compute boundary |
| NoThinking vs Thinking at small matched budget | AMC23 at 700 tokens 51.3 vs 28.9 pass@1; Thinking wins at about 3,500 tokens pass@1; parallel NoThinking comparable to Thinking at up to 9x lower latency (7x with perfect verifier) | Ma 2025 (a20, b26, d09) | single-source (one model family) |
| Agent overthinking vs resolution | reasoning models score about 3x higher on overthinking; o1 high 29.1% at about $1,400, o1 low 21.0% at about $400; best-of-2 low by lowest score 27.3% at $800 (43% cheaper than high); 3 samples 30.3%. Regression slope -7.894 (reasoning), -15.938 (non-reasoning) | Cuadron 2025 (a15, b16, b17, c11) | single-source, correlational |
| Wrong answers longer, with more switches | +225% tokens, +418% thought switches | Wang 2025 (b22) | single-source |
| Early exit DEER | 11 models, 10 benchmarks: CoT shorter by 19.1% to 80.1%, accuracy +0.3 to +5.0; Qwen3-14B 83.7 at 57.1% tokens vs 82.8; QwQ-32B 84.0 at 80.9% vs 82.6; R1-Distill-7B 69.2 at 61.5% vs 64.2 | Yang 2025 (c20, d11) | contested |
| Independent test of DEER and Dynasor (7 benchmarks) | Qwen3-4B average CoT 70.77; DEER 67.76 at 0.87 tokens; Dynasor 69.33 at 1.52x. Qwen3-8B CoT 72.50; DEER 70.64; Dynasor 70.46 at 1.26x. MMLU-Pro 68.00 to 63.14; MuSiQue 59.00 to 51.67 | Shen and Yao 2026 (d12) | contested (authors have a rival method) |
| Self-selection between own earlier and later answer | picks later in over 95% of disagreements (MuSR 97.7%, MMLU-Pro 95.1%); right when earlier was correct 0.0% / 6.7%; wrong-choice confidence 100% | Shen and Yao (d13) | single-source |
| Forced revision | share of revisions that stay on the original wrong answer: R1-32B 72%, R1-14B 70%, R1-1.5B 58%, LIMO 54%, QwQ 32%; revision success under 10% for strong models | Zeng 2025 (d10) | single-source |
| Learned stop head in agent loops | WebShop Qwen3.8-27B: full 43.0 at 5,945 tok/ep; StreamStop 42.8 at 3,464; constant budget 35.0 at 1,519. Nemotron: 37.0 vs 34.5. Within about one seed SD | Oh and Lee 2026 (d14) | single-source |
| Meta-controller | R1-Distill-7B +4.7 points, -53.3% length; unseen Qwen3-14B +2.9, -50.3%; unseen R1-Distill-32B 62.1 vs 62.3, -45.6% | Wen 2026 MetaCtrl (d15) | single-source; needs RL |
| Pooled probe scores can be pure difficulty | trace-blind difficulty proxy AUROC 0.873 on 192K R1 generations; reconstructed probe 0.849 pooled vs 0.496 within problem | Bulut 2026 (d16) | single-source |
| Switching and commitment across 16 models | high-accuracy pairs: switching -0.68 SD, commitment time -0.53 SD, accuracy 78.8%; short-CoT pairs +1.03 SD, accuracy 18.6% | Gonzalez i Catala 2026 (d17) | single-source |
| Illusion of Thinking | low complexity: non-thinking matches or beats thinking; high: collapse to zero at 64k max tokens. Reply: token limits, unsolvable instances | Shojaee 2025, Lawsen 2025 (a16, a17) | disputed |
| CoT harm on some tasks | grammar learning 94.0 vs 57.7 (o1-preview); exceptions task up to +331% trials | Liu 2025 (a18) | established that CoT can hurt; narrow task types |
| CoT gains are in math and symbols | symbolic +14.2, math +12.3, logic +6.9 | Sprague 2025 (a19) | established (K16) |

## 4. Mechanisms and models

Each is written so it can be built.

### 4.1 Marginal utility and flip accounting (measurement)
Run the same items at budgets t = 500, 1000, ..., T. Store correctness per item per budget as a matrix C[item][t]. Then:
- Accuracy(t) = mean over items of C[item][t].
- MU(t) = Accuracy(t+500) - Accuracy(t).
- Negative flip at transition t to t+500: C goes 1 then 0. Positive flip: 0 then 1.
- Zhou's ratio at threshold t: total negative flips over all transitions from t to T, divided by total positive flips over the same range. It is cumulative, so one item can count many times. Use an item-level bootstrap (resample items, not transitions) for the CI.
- Do not read "ratio above 1" as "stop here". In Zhou's own data the ratio crosses 1 at 7K while accuracy still climbs to 12K.

Implement a version we trust: pair items across budgets, run several seeds at temperature above 0, report the accuracy difference with a paired item-level CI, and report rescued vs harmed counts (the RCCM style of accounting, d22).

### 4.2 Budget forcing (the intervention being tested)
Generate thinking up to the budget. If the model tries to stop earlier and we want more, strip the end-of-thinking token and append "Wait". If it runs to the budget, append the end-of-thinking token plus a fixed phrase and let it answer. Known side effects: loops when stops are suppressed too often (Muennighoff), degradation in 12.5% of Zhou's negative flips, and models that ignore prompt-only budgets (Gema). Hard truncation and prompt budgets are different interventions. A prompt-only TALE-style budget is followed loosely (c19).

### 4.3 Error-accumulation model (Wu)
Accuracy A(N) is proportional to ((1 - E(N)) * (1 - eps))^N. E falls as steps get easier with more decomposition; eps is per-step error; N is step count. The product gives an inverted U. N* rises with task difficulty and falls with model ability. Engineering use: a stronger model needs fewer steps, so a budget tuned on a weak model is too long for a strong one. Weakness: fitted to arithmetic with clean steps; backtracking is not modelled.

### 4.4 Variance model (Ghosal)
Treat the model output as a 1-D distribution over the answer. More thinking widens it (entropy rises). A wider distribution first puts more mass on the correct value (looks like improvement), then lowers mass at the mode. Test it directly: sample the answer k times at each budget and log the entropy of the answer distribution. If the accuracy gain tracks the entropy rise rather than a sharper mode, the early gain is variance, and voting will do better than extension. A toy model; not proven for real transformers.

### 4.5 Answer-trajectory monitor
Log every intermediate answer the model states in its trace (code extracts them). Compute:
- oscillation count: times the stated answer changes;
- commitment time: first position after which the answer never changes;
- switch rate: thought-switch markers ("Alternatively", "Wait") per 1K tokens.

Zhou: oscillation correlates 0.78 with negative flips (in-sample). ADT: higher-accuracy pairs switch less (-0.68 SD). Bulut: pooled probe scores can be difficulty alone, so judge any monitor by lift within the same problem (many samples of one item), against a difficulty-only baseline.

### 4.6 Stop rules (O-stop)
Three families, with tested conditions:
- **Confidence at transition (DEER).** At a reasoning transition, force a trial answer; if the mean token probability of the answer exceeds 0.95, stop. Needs token probabilities. Wins in math; lost on knowledge and multi-hop tasks in the independent test.
- **Answer stability (Dynasor, answer convergence).** Stop when probed answers agree several times. Models converge after about 60% of reasoning steps on math (c21). Cost: extra probe tokens (1.26 to 1.52x in d12).
- **Learned stop (StreamStop, MetaCtrl, probes).** A small trained head reads the trace prefix. Won in agent tasks; needs training and held-out tuning. Hidden-state probes (24% fewer tokens, c22) need model internals, which a text-only scaffold does not have.

Rule from the evidence: simple rules win in math only; wins elsewhere need training or per-task tuning.

### 4.7 Parallel short selection (short-m@k)
Launch k chains. Stop when the first m finish. Vote among those m. This uses fewer tokens than waiting for all k, and the shortest chains are right more often within a question. Compute boundary: short-1@k beats majority at low compute and loses at high compute in 3 of 4 models; short-3@k holds across budgets. This is a selection rule in code (G5 compliant), not a model judgment.

### 4.8 Verify-before-revise gate
Idea: a stable intermediate answer should not be overwritten without new evidence. The gate must be external. A same-model judge shown both answers picks the later one over 95% of the time at near 100% confidence (d13). Safe gates: (a) a check that runs on the fresh unfitted part (G3); (b) an independent re-solve in a fresh context (about 2.6x tokens in the reported test); (c) log rescued vs harmed answers per revision. Nobody has tested the gate itself.

### 4.9 Difficulty-based allocation
Optimal length rises with difficulty (7.5x range across MATH levels). A gate estimates difficulty first (S0), then sets a budget. Weakness: Zhou's per-level optima are oracle choices, picked after seeing results. A deployed gate must guess the level, and the guess has error.

## 5. What holds up

**Holds up (several directions agree).**
- Shape: gain, plateau, mild decline, with the peak earlier for easy items and stronger models. Six studies agree on shape (c27). Sizes differ: about 1 point (Zhou, 12K to 16K), about 17 points (Ghosal, Wait-forced small models), 15 to 40 points on distractor tasks (Gema).
- Within one question, shorter chains are right more often, also inside each difficulty tercile (Hassid, Zeng; d07, d08, d10). This is a symptom: a chain goes long because it is going wrong. No paper separates symptom from cause with matched difficulty and forced extension together.
- At equal tokens, parallel sampling plus vote beats extending one chain (Ghosal, Hassid, Zeng). Boundary: majority wins at high compute over short-1@k.
- Optimal length rises with difficulty and falls with model size (Zhou, Wu).
- CoT helps mainly on math and symbolic tasks (Sprague, 100+ papers).

**Contested.**
- Early-exit rules. DEER and answer convergence win in math; an independent 7-benchmark test with Qwen3-4B/8B found DEER and Dynasor did not raise accuracy (d12). Those authors have a rival method, so baselines may be weak. Both test small models.
- Trace indicators (K05). Zhou's r=0.78 is in-sample. Bulut shows pooled scores can be pure difficulty (0.849 pooled vs 0.496 within problem), though for early-window probes, not oscillation counters.
- Illusion of Thinking collapse. Partly a token-limit and scoring artefact.

**Failed or absent replications.**
- No replication and no failed replication of Zhou's flip ratio exists (d19).
- Closed frontier models do not show a decline at coarse effort steps (GPT-5, o3, Gemini-2.5-Flash), only a plateau (d03). The effort steps are too coarse to see a 12K to 16K change.
- Qwen3-235B improves smoothly to 32K on vendor plots (d04).
- o3 and R1 do not show the Sonnet survival-instinct shift (d02). No outside group has replicated Gema.
- Jurayj's budget range stops at 8K, below Zhou's peak, so it neither supports nor refutes the decline (d05).

**Weak points in the key paper.**
- 0.9 points is about half of one AIME problem of 60. Greedy decoding, one pass, no seeds, no paired accuracy test.
- Flip ratios are cumulative; one problem can count many times; bootstrap CIs probably understate uncertainty.
- Two models, both 32B, one forcing method.
- The 80-case audit and indicator correlations come from one model; the same sample defined and tested the indicators.
- The early-stopping test (97% of peak at 60% compute) is in-sample.
- Natural-long samples are selected by being long, which tracks difficulty. "Natural equals forced" does not remove the confound.
- The 7K "p=0.038" is not in the table. The 2K ratio is 0.32; 0.22 is at 1K.

**Interventions that worked.** short-m@k (Hassid); parallel vote at equal tokens (Ghosal); NoThinking at under about 2K tokens on a 32B distill (Ma); lowest-overthinking pick of 2 low-effort agent runs (27.3% at $800 vs 29.1% at $1,400; Cuadron); learned stop heads in WebShop (Oh and Lee); few-shot examples against spurious-feature drift (Gema); training on shortened traces (Chen, out of scope); a switch penalty on QwQ-32B-Preview (Wang, no budget sweep).

**Interventions that did not work or did harm.** Same-model self-comparison of earlier vs later answer (d13). Forced revision for weak models: failed revision beats success (d10). A cautioned prompt ("you need not use the budget") against inverse scaling (Gema). A prompt-only anti-switching instruction on R1 (72.4, slightly worse). DEER and Dynasor outside math (d12). A strong switch penalty (strength 20, long duration).

**Moderators.** Task difficulty; model size and training; distractors or famous framings; decoding (greedy vs temperature 0.6-1.0); how length is forced; math vs knowledge vs agent tasks; presence of an external check.

## 6. Language models

**Open reasoning models (R1-distill, s1, QwQ).** Gain, plateau, decline on AIME and GPQA. R1-32B peaks at 12K on AIME and 10K on GPQA; s1-32B peaks near 12K with flip crossover near 5K. The drop is 0.9 points on AIME from 12K to 16K and 2.5 points on GPQA from 10K to 16K (55.6 to 53.1). Small distills with Wait-forcing drop far more (82.2 to 87.3 to 70.3 on GSM8K, 17 points from the peak). Probable reason: forcing "Wait" many times on a model that has finished produces variance and loops (Ghosal's account; not proven).

**Frontier closed models.** On basic maths GPT-5 (97% at medium and high), o3 (97% at all three efforts) and Gemini-2.5-Flash (92/93/92) plateau. They waste tokens (o3 8% more at high effort) but do not lose accuracy at these coarse steps. Reasoning models use about 18x more tokens than non-reasoning models on these tasks (d03).

**Constructed tasks.** Claude models get pulled by distractors (Opus 4 near 100% to 85-90%). OpenAI o-series resist distractors but over-apply familiar framings (o3 does worse on a trivial question styled like the Birthday Paradox). R1 natural setup falls 70% to 30% with five distractors. Few-shot examples fix much of the regression drift. Causes are read from traces, not from interventions.

**Agents.** SWE-bench: reasoning models score about 3x higher on overthinking; higher scores go with fewer resolved issues (correlational). Selecting the less-overthinking run saved 43% of cost at a 1.8 point loss against high effort. In closed-loop WebShop, a trained stop head matched full thinking at 42% fewer reasoning tokens, within seed noise.

**Small models.** Wu: optimal CoT length 14 steps at 1.5B vs 4 at 72B. Zeng: forced revision keeps the wrong answer 54 to 72% of the time for R1 and LIMO sizes (QwQ 32%). Small agents in LangGraph over-reason in 68 to 89% of MATH-500 cases (descriptive, no controls).

**What changed it, and by how much.** Stop rules, parallel selection, trained length control, training on short traces. Tokens cut 19 to 80% (DEER range) at roughly equal accuracy in math; 40% fewer tokens (short-1@k); 43% cheaper (Cuadron pick); about 50% fewer tokens (MetaCtrl). All except short-m@k and the Cuadron pick rely on tuned or trained components.

**Other non-math failures.** Deterministic state tracking (d20, abstract only, not opened): twelve models, tool-integrated reasoning 76-94% vs neural CoT 17-42% on PermutationProbe. A pointer, not evidence.

## 7. What our agent should take

Status: [E] established, [S] single-source, [C] contested. Schema parts: G guardrail, S state, O operator, M memory.

### Add now (established)

1. **Cap thinking length per mode; do not use one huge budget.** G11. [E] a01, a05, a13, a14, a07, c27; K01. The decline is small on natural tasks, but cost rises with no gain after the plateau. Set the cap from our own sweep (Test first T1), not from Zhou's 12K.
2. **Prefer several short independent attempts and a code vote over one long chain at equal tokens.** G11, S3, G5. [E] b19, b21, d07, d06; K08. Boundary: at high compute plain majority beats short-1@k; use short-3@k or majority at high budgets.
3. **Keep difficulty-based allocation.** G12, S0. [E] a03, a13, b14; K03. Easy items get a small budget; hard items get more. Caveat: per-level optima were chosen after the fact.
4. **Gate CoT by task type.** S0. [E] a19, a18; K16. Expect little CoT gain outside math, symbols and logic; CoT can hurt on implicit-statistics and visual tasks.
5. **Revision needs external evidence; never let the same model arbitrate between its earlier and later answer.** G2, S5. [E] for the principle (G2); the 95% later-answer bias is [S] (d13).
6. **Log flips.** Schema section 6. Record per revision or extension whether a correct answer turned wrong and the reverse. [E] as logging practice (d22); it supports every test below.
7. **Do not rely on the Illusion of Thinking collapse.** [E] that it is disputed (a17).

### Test first

| # | Item | Schema part | Status | Evidence ids |
|---|---|---|---|---|
| T1 | Budget sweep of our own model at 4+ levels per task class; find the peak with paired items and several seeds | G11, G12, S0 | [S] shape known, our peak unknown | a01, b01, d01, d03; K20, K25 |
| T2 | Answer-convergence stop (stop when the intermediate answer is stable across k probes) vs fixed budget | O-stop, S3 | [C] | c20-c22, d11, d12; K06, K21 |
| T3 | Oscillation counter as stop or escalate trigger, evaluated within problem | S4, S6 | [C] | a04, b05, d16, d17; K05, K23 |
| T4 | Verify-before-revise gate using an external check or independent re-solve | S5, S8, G2 | [S] untested | d13, d10, d22; K04, K22 |
| T5 | NoThinking-first pass for easy items | S0, S3 | [S] one model family | a20, d09; K09 |
| T6 | Share of tokens after the first correct answer in our agent | G11, S0 | [S] | a10, a11; K10 |
| T7 | Cap on planning-only turns in tool loops | G11, S6 | [S] | a15, b17; K12 |
| T8 | Switch cap plus stop rule across a budget sweep | S6, O-stop | [S] | a22, d17, d21; K13, K26 |
| T9 | Harvest all intermediate answers in the trace and test them, instead of trusting the final answer | S4 | [S] here (schema already marks harvesting [E] from F03) | a04, b04 |
| T10 | Lowest-flagged pick among several short agent runs, with an external test as selector | S7 | [S] | a15, b17 |
| T11 | Entropy of the answer distribution across budgets as a monitor | S-monitor | [S] | a14, c13; K18 |
| T12 | Wait-style extension on hard vs easy slices separately | G11 | [C] | a23, b25, a01; K14 |
| T13 | Few-shot examples on regression-like and spurious-feature tasks | S1, S2 | [S] | b09, c06 |

## 8. Concrete tests on our bench

All arms at equal tokens: total tokens of every call per item, including probes, vote samples and setup, are matched, or the cheaper arm is reported with its token deficit (G7).

| Test | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 sweep | 60+ items per class; math and non-math; ARC and BRAINTEASER classes | one agent at 4 to 6 caps (for example 1K, 2K, 4K, 8K, 16K), 3 seeds at temperature above 0 | accuracy per cap with paired item-level CI; MU per step; negative and positive flips | plateau at some cap; decline of 0 to 3 points, likely inside the CI. Treat a decline as real only if the paired CI excludes 0 |
| T2 convergence stop | items with a check and items without | full run vs stop when the stated answer is identical across 3 probes, plus a fixed cap set to the stop arm's mean tokens | accuracy at equal mean tokens; probe-token overhead | tokens cut 20 to 40% at equal accuracy in math; no gain outside math |
| T3 oscillation | 16+ samples per item, many items | counter vs difficulty-only baseline (past pass rate of the class) | within-problem AUROC for "this sample ends wrong"; lift over baseline | keep only if within-problem AUROC is above 0.60 |
| T4 gate | tasks where S5 revises | (a) revise freely (b) revise only on external check failure (c) independent re-solve | harmed answers (correct to wrong) and rescued answers (wrong to correct) per 100 items | (b) cuts harm; rescued loss must be smaller than harm saved |
| T5 NoThinking first | easy and medium items | thinking at cap vs NoThinking with 2 to 4 parallel samples and a vote | accuracy | NoThinking wins below about 2K tokens per item; thinking wins above about 3.5K |
| T6 post-answer waste | all runs | measure only | share of tokens after the first correct intermediate answer, by class | 40 to 60% on easy classes (Chen-style) |
| T7 planning cap | tool-using or code-repair items | unrestricted vs at most N consecutive planning-only turns | resolved rate per dollar | modest gain; Cuadron saw up to 43% cost cut |
| T8 switch cap | hard math items | vanilla; stop rule only; switch cap only; both; each over a cap sweep | accuracy at each mean token level | one control addressing both failures; report if curves cross |
| T9 harvest | items where the trace states several candidates | final answer only vs test all candidates in the trace | accuracy | recovers part of the abandonments |
| T10 agent pick | 2 to 3 short agent runs per issue | random pick vs lowest judged score vs externally tested pick | resolved rate at equal cost | external test beats judge score (G5) |
| T11 entropy | 10+ samples per cap | entropy of the answer distribution vs cap | correlation of entropy rise with accuracy change | supports Ghosal if early gain tracks entropy |
| T12 slice | hard vs easy slices | extension vs none | accuracy per slice | gain on hard slices, loss or none on easy |
| T13 few-shot | regression-like items | zero-shot vs few-shot, both at several caps | RMSE or accuracy | few-shot flattens the inverse trend |

Reporting rule for every test: paired items, 3 or more seeds, rescued vs harmed counts, CI on the difference, tokens per arm.

## 9. What does not transfer, and why

- **Zhou's thresholds (7K crossover, 12K peak).** Unreplicated, two 32B open models, greedy, math and GPQA only. Our model, prompts and tasks differ. Use the method, not the numbers.
- **Self-training on short traces (Chen), L1 length control, AdaptThink, MetaCtrl, StreamStop.** They need training. Our agent is scaffold-only. Use only as target length profiles.
- **Hidden-state probes (c22).** Need model internals. A text scaffold has none.
- **DEER's token-probability confidence.** Needs logprobs, and models can be confident on wrong paths (DeepConf note). Schema section 4b already rejects verbal confidence as a stop signal.
- **Gema's inverse-scaling magnitudes.** Tasks were built to fail. Real frequency unknown. Useful for the distractor mechanism (S1 input hygiene), not for rates.
- **Survival-instinct drift.** One model, a stated preference, item chosen after seeing the pattern. Not a scaffold concern.
- **Illusion of Thinking.** Contested design.
- **Flip ratio as a stop signal.** The ratio is cumulative from a threshold and needs the full future to 16K. At run time we do not have the future. It is a post-hoc diagnostic only.
- **Cuadron's overthinking score as a selector.** Judged by a model with no outcome access; G5 and G10 say not to select on such a score without an external check. Use it to diagnose; use tests to select.
- **The Wait-forcing decline in small distills.** Our agent does not force Wait. The decline shows a danger of naive extension, not of normal use.
- **Human overthinking research.** Not used here. This subfield is LLM-only; the human link appears only in Liu et al. (a18).

## 10. Open questions

1. Does the 12K to 16K drop survive a paired test over several seeds and at temperature above 0? On models other than R1-32B and s1-32B (Qwen3, o-series, Claude)?
2. How much of the natural decline is difficulty selection and how much is length? A matched-difficulty natural experiment with forced extension is missing.
3. Does any scaffold with a stop rule beat a fixed budget at equal mean tokens on held-out data outside math?
4. Does a verify-before-revise gate cut negative flips, and what does it cost in positive flips?
5. What is the real equal-token comparison of one long chain, k short chains with vote, short-m@k and NoThinking-first, all on one model and benchmark?
6. Are trace indicators (oscillation r=0.78) predictive within problem and on other models?
7. Do overthinking effects appear in code repair, planning and open-ended judgment with matched controls?
8. How do over- and underthinking trade off in one budget sweep, and can one control address both?
9. Do Gema's behaviour shifts replicate outside Anthropic's evaluation?
10. Does any 2026 paper replicate Zhou's flip ratio? None found as of November 2026. The check used 21 citing papers from one API snapshot; titles of all 21 were not opened.
11. Is Hassid's within-question short-wins effect partly "the model was confident" (selection)? Would forcing a short chain on a hard item help?
12. How fine must effort steps be to see a decline in closed models? Srivastava's steps are too coarse.

## 11. Sources

[V] = full text or full page opened. [M] = snippet or abstract page only.

- [V] Zhou et al. (2026) When More Thinking Hurts: Overthinking in LLM Test-Time Compute Scaling. https://arxiv.org/abs/2604.10739 (pdf: https://arxiv.org/pdf/2604.10739)
- [V] Gema et al. (2025) Inverse Scaling in Test-Time Compute (TMLR). https://arxiv.org/abs/2507.14417
- [V] Ghosal et al. (2025) Does Thinking More Always Help? Mirage of Test-Time Scaling in Reasoning Models. https://arxiv.org/abs/2506.04210
- [V] Chen et al. (2024/25) Do NOT Think That Much for 2+3=? On the Overthinking of o1-Like LLMs. https://arxiv.org/abs/2412.21187
- [V] Wu et al. (2025) When More is Less: Understanding Chain-of-Thought Length in LLMs. https://arxiv.org/abs/2502.07266
- [V] Cuadron et al. (2025) The Danger of Overthinking: Examining the Reasoning-Action Dilemma in Agentic Tasks. https://arxiv.org/abs/2502.08235
- [V] Shojaee et al. (2025) The Illusion of Thinking. https://arxiv.org/abs/2506.06941
- [V] Lawsen (2025) The Illusion of the Illusion of Thinking. https://arxiv.org/abs/2506.09250
- [V] Liu et al. (2025) Mind Your Step (by Step): Chain-of-Thought can Reduce Performance on Tasks where Thinking Makes Humans Worse. https://arxiv.org/abs/2410.21333
- [V] Sprague et al. (2025) To CoT or not to CoT? https://arxiv.org/abs/2409.12183
- [V] Ma et al. (2025) Reasoning Models Can Be Effective Without Thinking. https://arxiv.org/abs/2504.09858
- [V] Zhang et al. (2025) AdaptThink: Reasoning Models Can Learn When to Think. https://arxiv.org/abs/2505.13417
- [V] Wang et al. (2025) Thoughts Are All Over the Place: On the Underthinking of o1-Like LLMs. https://arxiv.org/abs/2501.18585
- [V] Muennighoff et al. (2025) s1: Simple test-time scaling. https://arxiv.org/abs/2501.19393 (critique lists s1 as not re-opened for findings; numbers from a23 and b25, which were opened)
- [V] Sui et al. (2025) Stop Overthinking: A Survey on Efficient Reasoning for Large Language Models. https://arxiv.org/abs/2503.16419 (survey; no numbers used)
- [V] Jurayj, Cheng, Van Durme (2025) Is That Your Final Answer? Test-Time Scaling Improves Selective Question Answering. https://arxiv.org/abs/2502.13962 (read in full in the gap search, d05)
- [V] Hassid et al. (2025) Don't Overthink it: Preferring Shorter Thinking Chains for Improved LLM Reasoning. https://arxiv.org/abs/2505.17813
- [V] Aggarwal and Welleck (2025) L1: Controlling How Long a Reasoning Model Thinks. https://arxiv.org/abs/2503.04697
- [M] Han et al. (2024) Token-Budget-Aware LLM Reasoning (TALE). https://arxiv.org/abs/2412.18547 (abstract only)
- [V] Yang et al. (2025) Dynamic Early Exit in Reasoning Models (DEER). https://arxiv.org/abs/2504.15895
- [V] Answer Convergence as a Signal for Early Stopping in Reasoning (2025). https://arxiv.org/abs/2506.02536 (author list not verified)
- [V] Reasoning Models Know When They're Right: Probing Hidden States for Self-Verification (2025). https://arxiv.org/abs/2504.05419 (author list not verified)
- [V] Marjanovic et al. (2026) DeepSeek-R1 Thoughtology. https://arxiv.org/abs/2504.07128 (magnitudes not re-checked)
- [V] Srivastava et al. (2026 v3) Do LLMs Overthink Basic Math Reasoning? LLMThinkBench. https://arxiv.org/abs/2507.04023
- [V] Qwen Team (2025) Qwen3 Technical Report. https://arxiv.org/abs/2505.09388
- [V] Zeng et al. (2025) Revisiting the Test-Time Scaling of o1-like Models. https://arxiv.org/abs/2502.12215
- [V] Shen and Yao (2026) Not All Test-Time Compute Is Evidence (DIA). https://arxiv.org/abs/2610.23213
- [V] Oh and Lee (2026) Adaptive Stopping of Streamed Reasoning for Language Model Agents. https://arxiv.org/abs/2610.27981
- [V] Wen et al. (2026) MetaCtrl. https://arxiv.org/abs/2609.37304
- [V] Bulut (2026) It's the Problem, Not the Path. https://arxiv.org/abs/2609.03436
- [V] Gonzalez i Catala et al. (2026) Answer-Distribution Trajectories. https://arxiv.org/abs/2609.09030
- [V] Fu et al. (2025) Deep Think with Confidence (DeepConf). https://arxiv.org/abs/2508.15260
- [V] Zhang and Zhang (2026) RCCM. https://arxiv.org/abs/2610.19872
- [V] Mia and Amini (2026) Don't Overthink, Don't Underthink. https://arxiv.org/abs/2608.26442 (descriptive, weak)
- [M] Guo, Wu, Yiu (2026) The Deterministic Horizon. https://arxiv.org/abs/2606.00376 (abstract page only)
- [V] Citation scan of Zhou 2604.10739 via the Semantic Scholar graph API. https://api.semanticscholar.org/graph/v1/paper/arXiv:2604.10739/citations (21 papers listed; five opened)

## Source audit (2026-11-01)

Fresh auditors re-opened the sources of 6 established claims: 4 confirmed as written, 2 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **C01.10-K01** (reworded: the sources support less). Gemini-2.5-Pro in LLMThinkBench is best at its lowest budget (90% at 128 tokens, 88% at max, with a dip to 71% at one setting), so it is not a clean plateau; also Zhou reports a bootstrap CI [-1.4,-0.4] for the 12K-16K drop (so 'no paired test' is only partly right: no seeds, greedy only). Corrected claim: Past a task- and model-specific length, extra sequential reasoning tokens lower accuracy (gain, plateau, mild decline). Seen in R1-32B/s1-32B on AIME and GPQA (budget forcing, temperature 0), R1-distill models on GSM8K with Wait forcing, Qwen2.5 on MATH Level 5 (CoT steps), and 9 models on constructed tasks. Gap search 2026-11: on basic maths in LLMThinkBench, GPT-5 and o3 plateau and Gemini-2.5-Flash is flat, while Gemini-2.5-Pro is best at its lowest budget (90% at 128 tokens, 88% at max, with a dip to 71% at one setting); Qwen3-235B improves smoothly to 32K on the vendor's plots. The drop is model- and task-specific. Zhou used greedy decoding, a single run with no seeds, though it reports a bootstrap CI for the 12K-16K drop.
- **C01.10-K02** (reworded: the sources support less). Zhou does report a bootstrap 95% CI [-1.4%,-0.4%] for the 0.9-point 12K-16K drop (though from one deterministic greedy run, so it is not seed-based or a paired test); numbers 55.8/54.9, Opus 4 100 to 85-90, R1 70 to 30, 87.3 to 70.3 are all correct. Corrected claim: The decline is small in the best-measured natural-difficulty setting (R1-32B AIME: 55.8 at 12K to 54.9 at 16K, about 0.5 problem of 60) but large in constructed tasks (Opus 4 nearly 100 to 85-90, R1 70 to 30 with five distractors) and Wait-forcing on small R1-distill models (87.3 to 70.3 on the GSM8K panel). Magnitude depends on setup. Zhou ran one greedy (temperature 0) pass per model; it reports a bootstrap CI for the 0.9-point drop, but no seeds or paired test over repeated runs back it.
