# Schoenfeld episodes and episode analysis of reasoning models: deep document

*Subfield E06.04. Built from evidence_a-d.jsonl (ids a01-a30, b01-b28, c01-c28, d01-d16), claims.jsonl (K01-K29) and critique.md in this folder. Schema references are to `research_notes/single_agent/SCHEMA.md` v0.2. Status marks: [E] established (two or more independent sources), [S] single source, [C] contested.*

*Reading rule for this document: where an early evidence line was corrected later, the corrected number is used. Two corrections matter. (1) The ThinkARM gold set is 7,067 sentences from 9 problems, not 99 (b01 was wrong). (2) In ThinkARM Table 5 the columns are Read, Analyze, Plan, Implement, Explore, Verify, Answer, Monitor. The values 8.52, 7.31 and 4.63 are the Answer share, not Monitor (d14). There is no Monitor rise under length penalties.*

---

## 1. What it is

Schoenfeld episode analysis splits a problem-solving protocol into time-ordered segments. Each segment gets one label that says what the solver is doing: Read, Analyze, Explore, Plan, Implement, Verify. The labels are not about the content. They are about the kind of act. The point of the scheme is to see control: when the solver stops one activity and starts another, and whether anyone checks that the switch was a good idea.

The core claim of the human theory is that expert skill rests on control (planning, monitoring, evaluating) more than on extra domain knowledge. Weak solvers read, pick a path fast, and never reassess. This is the "wild goose chase". (a01, a02, c27; all second-hand, see section 5.)

Since 2025 the same scheme is applied to the visible reasoning traces of language models. Two papers from one group (Li, Fan, Cheng, Feizi, Zhou) do the main work:

- **Li et al. 2025, arXiv 2509.14662.** First hand-labelled corpus. 38 DeepSeek-R1 responses to SAT maths, 915 paragraphs, 3,087 sentences. Seven sentence labels (the six plus Monitor, a short hesitation or self-check sentence) and three paragraph labels (General, Explore, Verify). (a05, c01)
- **ThinkARM, arXiv 2512.19995.** Scales to 15 models, 100 Omni-MATH problems, 1,500 responses, 410,991 sentences. Eight labels (adds Answer). GPT-5 is the annotator. (a10, b01, c05)

Around them sits a larger body of work that does not use Schoenfeld labels but studies the same phenomena in reasoning models: wandering (many thought switches), underthinking (dropping a correct thought), overthinking (too much work after the answer), failed branches, rumination loops, and early-exit rules. This document covers all of it, because the labels alone do not yet predict much (section 5), and the practical question for our agent is: what can code cheaply count in a trace to know that the agent is stuck, wandering or wasting tokens, and what should it do then?

What this subfield is NOT: it is not a theory of how to solve problems (see Polya heuristics, Means-ends analysis, Problem-solving cycle, run in parallel), and not a theory of monitoring accuracy (see Accuracy and dissociation of monitoring, Progress monitoring theory, Adaptive stopping and metareasoning). Links only. Here the focus is the empirical trace record and the coded detector.

---

## 2. History and theories in depth

### 2.1 Human work (second-hand only)

**Schoenfeld 1985, Mathematical Problem Solving.** Built on hundreds of hours of videotaped think-aloud sessions on non-routine problems. Separates four things a solver brings: resources (knowledge), heuristics, control, and beliefs. Episodes (Read, Analyze, Explore, Plan, Implement, Verify) are the unit used to draw timeline graphs of a session. (a01)

**Main findings as relayed by later papers.** Weak solvers start exploring without adequate analysis or planning, which sends them down unproductive paths. Success depends on control at episode boundaries. Novices hurry to an answer, apply procedures without checking, and wander. General heuristics such as means-ends analysis were reported as close to useless in content-rich maths. (a02, c27)

**Extensions.** Artzt and Armour-Thomas (1992) extended the scheme to small groups: read, understand, explore, analyze, plan, implement, verify, watch and listen, each coded cognitive or metacognitive. An ERIC abstract reports 27 seventh-grade students working in groups on one problem. (a03, b22) Harskamp and Suhre (2007) used it in a student-controlled learning environment; cited by both LLM papers. (a04)

**What is missing.** No source in this folder opened the 1985 book, the 1992 chapter, or the two extension papers. The much-quoted figure that most student attempts "pick a path and never monitor it" was searched for and not confirmed (c27, d15). Berkeley file paths returned 404 and Harskamp and Suhre returned 403. So no human percentage is in this document, and none should go into the schema (K23, K28).

### 2.2 The step to language models (2025)

Before 2025, episode coding was done by trained humans at about segment level and was slow. Three things made it feasible for models:

1. Reasoning models (o1-like: QwQ, DeepSeek-R1, R1 distills, Qwen3 thinking) print long visible traces of 5,000 to 15,000 tokens.
2. Strong LLMs can label sentences if given a written guidebook (section 3).
3. The traces already show surface cues that map to episodes: "Let me double-check" (Verify), "Alternatively" (switch to Explore), "Wait" (Monitor).

**Li et al. 2025** adapted the scheme. Monitor was added because reasoning traces contain many short sentences of hesitation between episodes that Schoenfeld's scheme has no place for. (c01) **ThinkARM** added Answer and moved to sentence-level only. It reports the "heartbeat" shape and two case studies: correctness and efficiency. (a11, a14, a15)

### 2.3 Parallel lines that study the same thing without the labels

These grew at the same time and give most of the predictive evidence.

- **Overthinking (Chen et al. 2024, 2412.21187).** Coined "overthinking" for o1-like models. Defines outcome efficiency and process efficiency. (a20, c10)
- **Underthinking (Wang et al. 2025, 2501.18585).** The mirror image: switching away from correct thoughts too early. Defines the underthinking score UT. (a17, a18)
- **Failed-Step Fraction (Feng et al. 2025, 2509.19284).** Builds a graph of reasoning steps and labels failed branches. The strongest within-question predictor. (a24, b13)
- **Wandering explorers (Lu et al. 2025, 2505.20296).** A formal depth-first search account of why failures appear as depth grows. (b15, b28)
- **Reflection audits (Kang et al. 2025, 2510.08308).** Most reflection after a first answer is confirmatory. (b17)
- **Test-time scaling limits (Ghosal/Ma et al. 2506.04210; Muennighoff et al. s1).** More thinking helps then hurts, or not. (b11, c23)
- **Structural and operator features (LCoT2Tree, Bloom profiling, ReasonOps).** Tree and step-type features predict correctness. (a22, d04, d05)
- **White-box detectors (probing, DEER, WordSaladChopper, ROM).** Cheap stop rules based on hidden states or trial answers. (c14, c15, d11, d12)
- **Causal sentence importance (Thought Anchors).** Which sentence types steer the final answer. (a28, b19)
- **Cognitive taxonomies (Kargupta et al., Gandhi et al., Thoughtology).** What behaviours reasoning models show and which matter under RL. (a25, a26, a27)

### 2.4 Competing explanations that run through the literature

1. **Difficulty confound.** Hard problems produce longer, more exploratory, more switchy traces and also more errors. Pooled correlations (Wang's 225 percent, ThinkARM's Lasso) cannot separate this. Within-question designs (Feng, Hassid, ReasonOps WP-AUC) can. (b26, d05)
2. **Reflection is wasted vs reflection is a safety net.** Kang says over 90 percent of reflections are confirmatory. Chen says a second solution repairs most of the loss from keeping only the first. Both can be true: low yield but non-zero value on hard items. (b17, a21, d06)
3. **Switching is the cause vs switching is a symptom.** Wang's TIP reduces switches and raises accuracy a little. SmartSwitch shows that intervening on every switch hurts. So a switch is a weak sign of a problem, not the problem itself. (a19, d10)
4. **Extra thinking is a variance effect.** Ma et al. argue the early gain of forced "Wait" is noise that happens to help. Muennighoff report gains on a different model. Unresolved. (b11, b24, c23)

---

## 3. Core findings with exact numbers

Status column uses [E]/[S]/[C] as in the claims file. "Same group" means all Schoenfeld-label results come from one lab.

### 3.1 Labelling and the episode record

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Hand-labelled R1 corpus | 38 R1 responses (2 per skill, 19 skills of 1,385 SAT maths items), 915 paragraphs, 3,087 sentences, 3 trained annotators after a 5-response pilot | Li 2025 (a05, c01) | [S] |
| Best LLM labeller on the 30% test subset | GPT-4.1 + examples + guidebook: 0.805 accuracy, kappa 0.764 (about 11 responses, no interval) | Li 2025 Table 4 (a08, c03, d01) | [S] |
| Same labeller on all data | 0.681 sentence, 0.757 paragraph (Table 2). Table 2 = all data; Table 4 = 30% test subset. Different evaluation sets | Li 2025 (d01) | [S] |
| Prompt ablation, GPT-4.1 sentence accuracy | base 0.595, examples 0.604, guidebook 0.676, both 0.681. GPT-4o 0.475/0.504/0.577/0.609. Gemini-2.0 0.590/0.628/0.655/0.626 | Li 2025 Table 2 (a07, c02) | [S] |
| Cheap labellers | BERT 0.732 / kappa 0.671; RoBERTa 0.730 / 0.670; SVM on Gemini embeddings 0.704 / 0.632; MLP 0.684 / 0.613; KNN 0.587 / 0.490 | Li 2025 Table 4 (a08, d02) | [S] |
| Verify is the weak boundary | GPT-4.1 confusion, percent of all sentences: Analyze to Verify 4.8, Implement to Verify 3.2, Analyze to Explore 2.3. Diagonal: Read 11.3, Analyze 16.6, Plan 5.7, Implement 17.1, Explore 6.1, Verify 18.5, Monitor 5.2 | Li 2025 (a09, b07) | [S] |
| Large gold set | 7,067 hand-labelled sentences from 9 of the 100 problems. Accuracy / kappa: GPT-4.1 86.10 / 82.74, GPT-5 86.33 / 82.85, Gemini-2.5-Flash 82.90 / 78.67, Gemini-2.5-Pro 80.89 / 75.96. Reasoning traces: GPT-5 86.02, non-reasoning 89.34 | ThinkARM (a10, c05, d03) | [S] |
| Sentence transitions are sticky and ordered | Implement to Implement .63; Analyze to Analyze .54; Verify to Verify .51; Plan to Implement .40; Read to Read .34, Read to Analyze .29; Explore to Explore .34, Explore to Analyze .25, Explore to Verify .12, Explore to Monitor .10; Implement to Verify .18 | Li 2025 Fig 1 (a06, c04) | [S] |
| The "heartbeat" | Early: Read, Analyze, Plan, Explore (falling). Middle: Implement peak. Late: Verify rises, Monitor U-shaped, Answer near 0 until the end. Seen in R1, Phi-4-Reasoning, Qwen3-32B, QwQ-32B, R1-Distill-Qwen-32B | ThinkARM (a11) | [S] |

### 3.2 Token allocation

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Reasoning vs instruction models | Percent of tokens Implement / Explore / Verify (avg tokens): R1 36.35 / 9.21 / 10.16 (9,250); QwQ-32B 35.71 / 13.98 / 11.05 (12,504); Qwen3-32B reasoning 36.86 / 11.56 / 10.54 (12,931); R1-Distill-1.5B 34.39 / 13.23 / 11.43 (9,897). GPT-4o 40.77 / 2.58 / 4.84 (690); Phi-4 64.12 / 0.21 / 4.27 (1,316); Qwen3-32B non-thinking 65.76 / 0.97 / 3.42 (2,649) | ThinkARM Table 2 (a12, b02, c06) | [S] |
| Distilled models copy the teacher's mix | R1-Distill-1.5B profile is close to R1 | ThinkARM (a12) | [S] |
| Easy items (50 GSM8K) | Qwen3-32B reasoning: Verify 55.89%. DeepSeek-R1: Verify 8.19%, Explore 6.88%. Non-thinking Qwen3 and Gemini-2.0-Flash: Explore about 0, Verify 0 to 1.35 | ThinkARM (a16, c09) | [S] |
| Signature patterns of reasoning models | Mutual information, reasoning vs own answer: Explore-Monitor .2862, Verify-Explore .2815, Monitor-Explore .2771. Vs non-reasoning: Explore-Monitor .2510 | ThinkARM Table 3 (a13, b05) | [S] |
| Efficiency methods remove different episodes (R1-Distill-1.5B) | Baseline 9,897 tokens, Verify 11.43, Analyze 26.93, Answer 3.80, Monitor 1.84. L1: 2,437 tokens, Verify 6.99, Analyze 18.34, Answer 8.52, Monitor 1.64. ThinkPrune: 4,054, Verify 8.37, Answer 7.31, Monitor 1.80. Arora-Zanette: 5,312, Verify 9.94, Answer 4.63, Monitor 1.64. Largest lost pattern (Neutral-Verify-Neutral MI): L1 .3762, ThinkPrune .1506 | ThinkARM Table 5 (a15, c08, d14) | [S] |
| Answer share rises only because answer-writing is a fixed cost | Answer tokens 376 (baseline) vs 208 (L1) over a trace about four times shorter | ThinkARM (d14) | [S] |

### 3.3 Episodes and correctness

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Lasso on episode features (association only) | 500 stratified traces, 5 open models, 64 transition + 8 ratio + 3 global features, z-scored, C = 0.5. Positive: Explore to Monitor +0.41, Explore to Analyze +0.31, Monitor to Analyze +0.28, Read to Verify +0.27, Answer to Verify +0.22, Verify ratio +0.21. Negative: Explore ratio -0.54, Explore to Verify -0.45, Explore to Answer -0.41, total count -0.36, Implement to Read -0.32, Implement to Implement -0.28. No AUC, no held-out score, no interval | ThinkARM Table 4 (a14, b03, c07) | [C] |
| Step-type features vs length, held-out (Bloom labels, not Schoenfeld) | Nested CV (5 outer, 3 inner), 9,132 balanced samples, 43 features. AUC 0.676 +/- 0.012 vs length-only 0.613 +/- 0.008. Accuracy 0.631 vs 0.623, F1 0.667 vs 0.666. Total tokens strongest negative (-0.4373). Evaluate-to-Analyze -0.1271 and Analyze-to-Evaluate -0.1236 (oscillation) | Zoumpoulidi 2026 (d04) | [S] |
| Operator features within problem (ReasonOps, clustering-derived, not Schoenfeld) | 44,662 traces, 12 models, 8 benchmarks, problem-level 5-fold CV. Within-problem AUC: length 0.551, backtrack count 0.594, wait count 0.603, self-judge by same model 0.512, operator XGBoost 0.701 cross-dataset / 0.723 within. AIME 0.838, LiveCodeBench 0.795. BBH and HumanEval near chance | Lee 2026 (d05) | [S] |
| Early prediction | WP-AUC 0.605 at 10% of trace, 0.664 at 50%, 0.701 at 100% (AIME 0.645, 0.740, 0.801) | Lee 2026 (d06) | [S] |
| Difficulty flips the signal | Easy (more than 2/3 of models solve): committal-minus-reflective gap +44.2% correct vs +7.5% incorrect, AUC 0.76 [0.74, 0.78]. Hard (under 1/3 solve): +30.4% vs +34.9%, p = 0.15, AUC 0.48 [0.44, 0.51] | Lee 2026 (d06) | [S] |
| Tree structure | Length-only classifier about 58-60% on MMLU-Pro. Tree GNN adds +5.58, +5.72, +4.69, +3.89, +8.27 points across five models. Four error shapes: over-branching, step redundancy, direct reasoning, skipped thinking | LCoT2Tree (a22, a23) | [S] |

### 3.4 Wandering, underthinking, failed branches

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Wrong answers are longer and switch more | 225% more tokens and 418% more thought switches in incorrect vs correct (QwQ-32B-Preview, R1-Preview in the intro; R1-671B added later). Test sets: MATH500 Level 5, GPQA Diamond (198), AIME 2024 + 60 AIME 2022-23 items (90 total) | Wang 2025 (a17, b08, c11) | [E] with b13, b12 |
| A correct thought is often dropped | Over 70% of incorrect responses hold at least one correct thought; over 50% have more than 10% correct thoughts. One trace: 25 thoughts, 7,270 extra tokens after a correct first thought. Thought judge 82.9% (correct) and 81.8% (incorrect) on 90 items | Wang 2025 (a17) | [E] with c13 |
| Underthinking score UT (share of tokens after first correct thought, wrong answers) | MATH500-Hard: QwQ 58.2 (acc 84.3), R1-Preview 61.5 (83.6), R1-671B 65.4 (92.5). AIME2024: R1 37.0, QwQ 65.0. On AIME2024 R1-671B has higher accuracy and lower UT | Wang 2025 (a18, b23, c11) | [S] |
| Switch penalty at decoding (TIP) | AIME2024: QwQ 38.3 to 44.1; R1-Distill-32B 61.4 to 64.1; R1 73.8 to 74.8 (R1 + prompt only 72.4). MATH500-Hard QwQ 83.1 to 83.7. GPQA QwQ 57.6 to 59.1. R1 switch tokens 13.8 to 5.7. Pass@4 QwQ 43.7 to 51.4. Tuned on AIME 2022-23 | Wang 2025 (a19, b09, c11) | [S] |
| Within a question, longer chains and more review go with lower accuracy | 10 models, HARP 300 questions x 16 traces, GPQA-Diamond 198, AIME 2025 30 x 64. Review ratio negative for most models; Claude 3.7 Sonnet on maths is the exception. Strongest on HARP levels 4-6 | Feng 2025 (a24, b13, b26) | [E] with b12 |
| Shorter chain of the same question wins | Up to 34.5% more accurate than the longest sampled chain; short-1@k matches majority vote with up to 40% fewer thinking tokens | Hassid 2025 (b12) | [S], abstract only |
| Failed-Step Fraction is the strongest predictor | Top-1 of 64 by FSF: about +5 to +13% on AIME 2025 over random. Depth of the first failed step has little correlation: it is amount, not timing | Feng 2025 (a24, b14, critique) | [E] with a23 |
| Deleting failed branches helps (R1) | First failed branch removed: 20.89 +/- 1.36 to 29.42 +/- 1.66; last branch 9.72 to 23.75. GPT-oss-120B: 28.05 to 36.41; 16.50 to 27.33. 80 and 160 incorrect traces, 8 continuations each, 11,520 total | Feng 2025 (b14, d07) | [S] |
| Summarising the failed branch keeps most of the gain for R1, less for GPT-oss | R1: 28.14 and 22.57 (85% and 92% of delete gain). GPT-oss: 29.51 and 25.22 (17% and 81%) | Feng 2025 Table 1 (d07) | [S] |
| Wandering search model | Success of a depth-first wanderer falls exponentially with depth; with m greater than 1 targets, a plateau above 0.995 can hide it on easy items | Lu 2025 (b15, b28) | [S], toy model |
| Rumination | Rises with difficulty, independent of total time; correct thoughts are on average shorter than incorrect ones (pooled, so confounded) | Thoughtology (a26, b18) | [S] |

### 3.5 Overthinking, reflection, stopping

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Overthinking on easy items | 1,953% more tokens than conventional models on "2+3"; 13 solutions, 7 strategies, 901 tokens, first correct at token 39; outcome efficiency 4.3%, process efficiency 35.8%. First round correct in over 92% of cases, under 60% of tokens (QwQ on ASDIV: 287 tokens, 38.7%). 2-4 rounds in 76-80% of QwQ cases and 59-63% of R1 | Chen 2024 (a20, b10, c10) | [E] with c19, a29 |
| Compute on easy tasks | Thinking mode uses 5-20x more compute on simple tasks, 14 models, 6 domains. Qwen3-235B GSM8K 74.75% non-thinking vs 91.50% thinking, 118.1 vs 1,021.7 words; about 80% of extra compute gives no gain | TRACE (c19) | [S] |
| Self-training to shorten | MATH500 QwQ: 93.0 acc, 2,407.9 tokens to 92.8, 1,330.7 (44.7% fewer; text also says 48.6%). AIME24 46.7 to 43.3, 9,480.9 to 5,154.5 tokens. First-correct + reflection beats first-correct only by 1.4% on hard MATH500 | Chen 2024 (a21, c10) | [S] (needs fine-tuning) |
| Reflection after the first answer is mostly confirmatory | 8 models (7B to 685B), 5 maths sets, 3,427 rollouts per model. Over 90% confirmatory; corrective (wrong to right) under 2%. Post-first-answer reflection uses 16.8-47.8% of tokens for 1.4-3.5% accuracy. Candidate extraction 94% correct | Kang 2025 (b17, b27) | [E] with a21 |
| Early stop by reflection confidence | Qwen3-8B: 1-point accuracy drop allows 12.0% fewer tokens; 8.12-point drop allows 40.7%. Also 29.9% fewer tokens for a 3.8-point drop | Kang 2025 (b17, b27) | [S] |
| Forced "Wait": helps then hurts | R1-Distill-1.5B GSM8K: 82.2% at 385 tokens, 87.3% at about 1,100, 70.3% at about 15,980; entropy 0.23 to 2.79. MATH500 83.2% to 78.3% at 16,109. Parallel thinking up to 22% above extended thinking at 16K | Ghosal/Ma 2025 (b11, c16, b24) | [C] |
| Budget forcing helps on one model | s1-32B on 1,000 examples: AIME24 50% to 57% | Muennighoff 2025 (c23) | [C] |
| Missing premise makes models wander | MiP-GSM8K 582, MiP-SVAMP 300 items. Non-reasoning about 200 tokens; R1 from about 1,000 to over 3,000. MiP-Formula abstain: GPT-o1 78.0%, GPT-4o 70.0%, R1 6.0%, QwQ 0.0% (QwQ avg 7,937 tokens). Suspicion noticed in 83.3-100% of traces at step 1.16-1.42 | Fan 2025 (a29) | [S] |
| Stop probes (white-box) | Hidden-state probe AUC above 0.7, above 0.9 for R1-Distill-32B on AIME; threshold 0.85 on R1-Distill-Llama-8B MATH keeps 88.2% accuracy with about 24% fewer tokens. DEER: threshold 0.95; R1-Distill-7B accuracy 64.2 to 69.2 with 61.5% of tokens; Qwen3-14B 82.8 to 83.7 (57.1%); QwQ-32B 82.6 to 84.0 (80.9%) | Zhang 2025; Yang 2025 (c14, c15) | [E] two groups |
| Loop and word-salad detectors (white-box) | Qwen-7B distill accuracy / AUROC: GSM8K 92.72 / 98.63, MATH-500 92.31 / 95.95, AIME25 89.77 / 95.84, GPQA 93.52 / 97.89; AIME25 at temp 0.6 drops to 77.96 / 80.15. ROM boundary probe 85.9% accuracy, AUROC 0.928, length cut 28-77% (mean 45%), best accuracy in 19 of 25 settings | WordSaladChopper; ROM (d11, d12) | [S] each |
| Selective switch intervention | R1-Distill-1.5B AIME24: vanilla 28.9, prompt rule 29.0, TIP 31.3, SmartSwitch 40.0. AIME25: none 20.0, intervene at every switch 18.9, with PRM-72B 24.8, Universal-PRM-7B 36.7 | SmartSwitch (d09, d10) | [S] |
| Agentic overthinking | 4,018 SWE-bench Verified trajectories. Pick lowest overthinking of k: k=2 low effort 27.3% resolved at 43% lower cost; k=3 30.3% with 15% lower cost. Judge checked on 20 traces by 4 experts, correlation plot only | Cuadron 2025 (c18, d13) | [S] |
| Causal weight of sentence type | R1-Distill-Qwen-14B, 20 MATH problems (25-75% solve rate), 40 traces, 144.2 sentences each, 100 rollouts per sentence. Shares: computation 32.7, fact retrieval 20.1, plan 15.5, uncertainty management 14.0. Plan and uncertainty sentences have most counterfactual effect; forced-answer importance points the other way | Bogdan 2025 (a28, b19, c20) | [S] |
| Behaviours that decide RL success | Verification, backtracking, subgoal setting, backward chaining. Priming on wrong but well-structured solutions works as well as correct ones. Countdown RL transferred to MATH: Qwen backtracking 0.15 to 0.59, verification 0.02 to 0.29 | Gandhi 2025 (a27, b20, c21) | [S] |
| Cognitive taxonomy at scale | 192,709 traces, 18 models, 54 human think-aloud traces. Forward chaining probability 0.748; models under-use elements that correlate with success | Kargupta 2025 (a25) | [S] |

---

## 4. Mechanisms and models

This section explains how each tool works so an engineer can build it. Everything runs in code outside the model, which fits schema section 1.

### 4.1 The episode labeller

**Inputs.** A reasoning trace split into sentences (on full stops, newlines; skip code fences) and grouped into paragraphs (double newline).

**Labels.** Read, Analyze, Plan, Implement, Explore, Verify, Monitor, Answer (eight). Definitions in plain words:

- Read: restates or re-reads the problem.
- Analyze: reasons about the structure, constraints, relations, without yet computing.
- Plan: states what to do next ("First I will...").
- Implement: carries out a calculation or step.
- Explore: tries an idea that is not yet committed to; guesses, "maybe", "what if", "alternatively".
- Verify: explicit check phrases ("Let me double-check", "Is there any mistake?", "Let's try another way to verify").
- Monitor: short sentence of hesitation or self-talk between episodes ("Wait", "Hmm").
- Answer: a declarative final or provisional answer. Provisional answers also get Answer. (d16)

**Prompt design.** Use a written guidebook with explicit definitions and contrast rules. The guidebook added 0.07-0.09 to GPT-4.1 sentence accuracy; examples alone added about 0.01 (a07). Put the Verify indicator phrases and the Verify-vs-Implement and Verify-vs-Answer contrast rules in the guidebook, since that is where labellers fail (a09, d16).

**Accuracy to plan for.** About 0.81 to 0.86 for a strong LLM on reasoning-model traces (a08, d03). About 0.73 for a fine-tuned BERT (a08). Our gating bar is kappa 0.75, so BERT (0.671) is a logger, not a gate (d02). Per-boundary kappa for Verify is not reported and is probably lower.

**Cost trade.** One LLM call per sentence is expensive. Cheaper: label per paragraph (0.757 best, a07), or use cue phrases for the sentences where cues are clear and call the LLM only on ambiguous ones. This hybrid is our own design and untested.

### 4.2 Episode statistics

From a labelled trace compute:

- **Ratios**: share of sentences or tokens per label (8 numbers).
- **Transition matrix**: counts of label i followed by label j (64 numbers). Normalise rows for the sticky-chain view (a06).
- **Global**: total sentence count, token count.
- **Time profile**: bin the trace into 25 bins by progress and average label shares per bin to see the heartbeat (a11, b05).
- **Pattern mutual information**: for short label n-grams (Explore-Monitor, Verify-Explore), MI between "pattern present" and trace class (reasoning vs answer, or model A vs B) (a13).

### 4.3 The correctness model, and why not to trust it yet

ThinkARM fits a Lasso logistic regression on about 75 z-scored features, C = 0.5, liblinear, 500 traces from 5 models (critique item 6). It prints a coefficient table and no held-out score. Treat as a hypothesis generator, not a detector.

A sound version for our bench:

1. Collect N runs of our agent on items with known answers.
2. Features: the 8 ratios, the 64 transitions, token count, wait count, backtrack count, switch count.
3. Split by problem, never by trace: all runs of one problem on the same side. (d04 probably did not; d05 did.)
4. Report within-problem AUC against length-only and wait-count baselines (d05 method).
5. Keep a feature only if it beats the baselines on held-out problems.

Expected size: AUC 0.68-0.72 at best (d04, d05). That is an advisory signal, not a gate.

### 4.4 Cheap stuck-signal composite

No source validates a detector built from Schoenfeld labels (K22). The evidence supports a composite of cheap counts. Each is defined so code can compute it from text.

| Signal | How to compute | Evidence |
|---|---|---|
| Thought-switch rate | Count of cue words ("Alternatively", "Another approach", "Let me try a different") per 1,000 tokens; thoughts split on them | Wang (a17), TIP (a19) |
| Switch-without-deepen | A thought shorter than a threshold (for example under 150 tokens, tuned) followed by a switch | Wang UT; SmartSwitch cue (d10) |
| Wait and backtrack count | Count of "Wait", "Hold on", "Actually" and "backtrack" phrases | d05: AUC 0.603 and 0.594 within problem vs length 0.551 |
| Repeated n-gram rate | Share of 5-grams that occurred before in the last window; or sub-thought self-loop count | Thoughtology (a26), TRACE K=2 (c19) |
| Revisit count | Number of times the same intermediate state, sub-goal, or candidate answer string reappears | Lu formal model (b15); our own addition |
| Failed-branch share | Share of steps inside branches later abandoned. Needs a graph labeller (LLM) | Feng (a24); heavy |
| Evaluate/Analyze oscillation | Count of Verify to Analyze to Verify cycles with no new Implement between them | d04 coefficients; ThinkARM Neutral-Verify-Neutral (a15) |
| Answer-confirmed-then-continue | A candidate answer was stated and a later check agreed, yet tokens continue | Kang (b17), Wang UT (a18), TRACE Late Landing (c19) |
| Missing-premise flag | Model notes early that the premise may be missing but continues | Fan (a29) |

**Wiring rule.** The flag is advisory. It starts a second check (code-run test, or a trial-answer probe), and only the second check triggers a state change. Reason: intervening on every switch lowered AIME25 from 20.0 to 18.9 (d10), and switch-based correlations are confounded by difficulty (b26).

### 4.5 Failed-branch pruning

Feng et al. show that removing a failed branch from the context and continuing raises accuracy (R1 20.89 to 29.42). Mechanism: earlier mistakes bias what follows. A scaffold cannot delete text from a model's own stream, but it can control what goes into the next call. Three options, in rising cost of information kept:

1. Delete the failed branch from the context passed to the next call.
2. Replace it with a one-line dead-end note ("Tried X; failed because Y").
3. Replace it with a short summary (Feng's third arm; kept 85-92% of the gain for R1, 17-81% for GPT-oss).

Option 2 is untested (K08). It matters because a scaffold also wants to remember why something failed.

### 4.6 Stop rules

| Rule | Needs | Evidence |
|---|---|---|
| Fixed token cap by difficulty | A difficulty estimate | Thoughtology budgets 64-1,024 cut GSM8K output by about half with little loss (a26); schema G12 |
| First-checked-answer stop on easy items | A check or a second sample | Chen: first round correct over 92% (a20) |
| Trial-answer stability (DEER style) | Ability to ask for a trial answer at a switch cue; works as a black-box call, though the paper used token confidence above 0.95 | c15 |
| Loop stop | Repetition detector | TRACE K=2 loop-stop: Temporal-L3 62.23% with length 2,722 to 1,315 words (235B) (c19) |
| Hidden-state probe | White-box | c14, d11, d12 |
| Shortest-of-k | Parallel runs; stop when the first m finish | Hassid: short-3@k beats majority voting at all budgets, wall time down up to 33% (b12) |

### 4.7 Why Verify is placed where it is: a reconciliation model (untested)

ThinkARM: Verify ratio +0.21, Read-to-Verify +0.27, Answer-to-Verify +0.22 go with success; Explore-to-Verify -0.45 goes with failure. Feng: review ratio negative within question. Kang: most post-answer reflection is confirmatory. These agree under one model: the useful check is (a) at the start (re-read against the problem), (b) once at the end, after an Answer, and (c) short. The harmful check is repeated mid-trace, before a hypothesis is consolidated, or in a loop. Feng's Review is also broader than Verify (it includes restating, deleting, rewinding; labeller agreement 90%) (d08), so the "conflict" is partly a definition issue. Nobody has varied check position under control (K26). That is test E06.04-U2 in UNKNOWNS.md.

---

## 5. What holds up

### 5.1 Replications and independent agreement

- **Wrong answers are longer and switch more: holds.** Wang's raw difference (225% more tokens, 418% more switches) does not control for difficulty. But Feng's within-question design (10 models) and Hassid's same-question comparison (up to 34.5% more accurate than the longest chain) find the same sign. Exceptions: Claude 3.7 on maths for review ratio; GPQA mostly length. Status [E]. (a17, a24, b12, b26)
- **Overthinking on easy items: holds.** Chen (first round correct over 92%), TRACE (about 80% of extra compute gives no gain), Kang (over 90% of reflections confirmatory), Thoughtology (budgets halve output with little loss). Four-plus independent groups. [E]. (a20, c19, b17, a26)
- **Reflection mostly confirms: holds.** Kang's 8 models plus Chen's 1.4% gain of reflection over first-correct. [E]. (b17, a21)
- **Correct thought dropped: holds qualitatively.** Wang's 70% plus injected-correct-answer test (c13, few models, no aggregate rates). [E] on direction, the 70% figure is one paper. (a17, c13)
- **Failed branches matter: holds.** Feng measured it; LCoT2Tree independently finds over-branching and redundancy in wrong traces. [E]. (a24, a23)
- **Early stop from internal or trial-answer signals: holds.** Probing (AUC above 0.7) and DEER, two groups. [E] but white-box or confidence-based. (c14, c15)

### 5.2 What has NOT been replicated

- **Everything labelled with Schoenfeld episodes.** Both papers are from one group. The correctness result is a 500-trace Lasso with no held-out score. No third party reproduced it (c24, b25). [S].
- **The 0.805 label accuracy.** Same group, same data. The first paper's own all-data number is 0.681. The larger gold set gives about 86% for the same model, so the level is not wild, but the Verify boundary stays weak. (d01, d03)
- **Human baseline numbers.** Not verified (d15).
- **Thought Anchors.** One main model (R1-Distill-Qwen-14B), 20 problems, replicated on R1-Distill-Llama-8B with 40 solutions. CI on accuracy about +/-10% with 100 rollouts. The forced-answer measure points the other way. (b19, c20)

### 5.3 Failures and tensions

- **Verify direction.** ThinkARM says more Verify goes with correct; Feng says more review goes with wrong. Likely a definition issue plus position effect (section 4.7). Not tested. [C]. (a14, a24, d08)
- **Wait and budget forcing.** s1 gains 7 points on AIME24; Ma/Ghosal lose accuracy past about 1,100 tokens on GSM8K. Different base models (s1-32B vs 1.5B-8B distills) and budgets. Early gain may be variance (b24). [C]. (c23, b11)
- **TIP gains are small and model-dependent.** R1 gains one point (73.8 to 74.8). A prompt-only rule did not help (R1 plus prompt 72.4; 1.5B model 29.0 vs vanilla 28.9). (a19, d09)
- **Underthinking is not simply "more switching is worse".** On AIME2024 the stronger model R1-671B has higher accuracy and lower UT; on MATH500-Hard it has higher accuracy and higher UT (65.4). (b23)
- **Selective vs blanket intervention.** SmartSwitch: intervene at every switch 18.9 vs none 20.0. Only a gated intervention with a good scorer helps (36.7 with Universal-PRM-7B). Gain depends on the scorer: Qwen2.5-Math-PRM-7B only 21.1. (d10)
- **Predictive gains are modest.** Bloom features AUC 0.676 vs 0.613; ReasonOps within-problem AUC 0.701 vs 0.551. Near chance on BBH and HumanEval for ReasonOps. A model judging its own trace is at chance (0.512). (d04, d05)
- **Length alone is partly a difficulty effect.** Pooled correlations (Thoughtology: correct thoughts shorter) are confounded. (b26)
- **Efficiency methods cut Verify, but nobody linked cut to accuracy loss.** ThinkARM does not report per-method accuracy in the sections read. (a15)

### 5.4 Moderators

| Moderator | Effect | Evidence |
|---|---|---|
| Item difficulty | On easy items correct traces are forward-stepping (AUC 0.76); on hard items that signal vanishes (0.48). Switching, rumination and review effects are strongest on harder items (HARP levels 4-6) | d06, b13, a26 |
| Model size and type | Smaller models loop more and overthink more; distilled students loop even when teachers rarely do; large models can still wander (o3, Claude Sonnet 3.7 degrade with depth) | c12, d13, b15 |
| Temperature | Loops more frequent at greedy or low temperature; word-salad probe accuracy falls from 89.77 to 77.96 at temp 0.6 on AIME25 | c12, d11 |
| Task domain | Predictive signal holds on maths and LiveCodeBench (0.795), fails on BBH and HumanEval | d05 |
| Starting budget | Forced-Wait gain depends on how short the base answer was | b11, c23 |
| Answer-writing cost | Short traces show a higher Answer share because answer text is a fixed cost | d14 |

### 5.5 Interventions that worked and did not

| Worked | Size | Did not work | Size |
|---|---|---|---|
| Delete failed branch in context | R1 +8.5 / +14.0 points; GPT-oss +8.4 / +10.8 | Prompt-only "explore thoroughly before moving on" | 29.0 vs 28.9 (1.5B, AIME24); R1 + prompt 72.4 vs 73.8 |
| Summary of failed branch | R1 keeps 85-92% of delete gain | Intervene at every thought switch | AIME25 20.0 to 18.9 |
| Select trace with lowest Failed-Step Fraction | +5 to +13% (AIME25, 64 samples) | Wait forcing at long extension | GSM8K 87.3% down to 70.3% |
| Select shortest of k | up to 34.5% better than longest; 40% fewer tokens at equal accuracy to majority | Self-judging the trace | WP-AUC 0.512 |
| Gated switch intervention with strong PRM | AIME25 20.0 to 36.7 | Cheap PRM as scorer | 21.1 |
| Early exit on confidence (DEER) | +0.9 to +5.0 points with 19-43% fewer tokens | Early exit at aggressive thresholds | Kang: 8.12-point drop for 40.7% savings |
| Lowest-overthinking-of-k in agents | 27.3-30.3% resolved on SWE-bench Verified | Fine-tuning for fewer reflections (training based, not for us) | n/a |
| Parallel thinking at fixed budget | up to 22% above Wait-extension at 16K | | |

---

## 6. Language models

### 6.1 How reasoning models behave on these tasks

- **They spread effort over Analyze, Explore, Verify.** Reasoning models put 9-14% of tokens in Explore and 10-11% in Verify; instruction models put 0.2-2.6% in Explore and 3-5% in Verify, and 36-66% in Implement. (a12)
- **They follow a heartbeat.** Plan and Read first, Implement in the middle, Verify and Monitor at the end. (a11) The shape is the same across five open reasoning models.
- **Their signature is Explore-Monitor loops.** Short cycles through Explore, Monitor, Verify; answers are feed-forward. (a13)
- **Easy items get over-verified.** Qwen3-32B reasoning spends 55.89% of tokens on Verify on GSM8K; the same model in non-thinking mode spends 0%. R1 spends 8.19%. The spread between models is large and has one number each. (a16, critique)
- **Wrong answers wander.** 225% more tokens, 418% more switches; over 70% of wrong answers had a correct thought. (a17)
- **Missing premises make them wander.** 2-4x longer answers; they notice the problem early (83-100% of traces) and keep going. R1 abstains 6.0% and QwQ 0.0% where o1 abstains 78.0%. (a29)
- **Reflection is mostly confirmation.** Under 2% of reflections fix a wrong answer. (b17)
- **They hold correct thoughts and lose them.** Even with the correct answer injected into the chain, models keep generating and rarely accept it. (c13)
- **Length is miscalibrated to difficulty.** Overthink easy, underthink hard. (b21, a29) Rumination (5-gram repetition) rises with difficulty. (a26)
- **Agents.** Three forms: Analysis Paralysis, Rogue Actions, Premature Disengagement. Reasoning models score higher than non-reasoning ones; smaller models score higher. (c18, d13)

### 6.2 What changed behaviour, and by how much

| Change | Effect | Source |
|---|---|---|
| Written guidebook for the labeller | +0.08 sentence accuracy for GPT-4.1 (0.595 to 0.676) | a07 |
| Decoding switch penalty (TIP) | +0.5 to +5.8 points (R1 +1.0; QwQ +5.8 on AIME24) | a19 |
| Selective switch intervention with scorer | AIME24 28.9 to 40.0 (1.5B) | d09 |
| Remove failed branch before continuing | +8 to +14 points on incorrect traces | b14 |
| Pick lowest Failed-Step Fraction of 64 | +5 to +13 on AIME25 | b14 |
| First-checked answer then stop (via self-training) | 44.7% fewer tokens at 93.0 to 92.8 on MATH500 | c10 |
| Confidence early exit (DEER) | 19-43% fewer tokens, accuracy +0.9 to +5.0 | c15 |
| Length-penalised or pruned reasoning (L1, ThinkPrune) | 2,437 and 4,054 tokens from 9,897; Verify 11.43 to 6.99 and 8.37 | a15, d14 |
| Parallel instead of extended thinking | up to 22% above at 16K | b11 |
| RL on Countdown with priming of four behaviours | Qwen 3B about 60%, Llama 3B about 30%; priming closes the gap | a27 |
| Hidden-state stop probe | about 24% fewer tokens at equal accuracy | c14 |
| Word-salad chop | accuracy 78.0 to 88.1 (Qwen3-8B), more than 55% of tokens in R1-distill GPQA outputs are word salad | d11 |

### 6.3 What this means for a model used through an API

Most large gains need weights (probes, TIP, self-training, RL). A scaffold sees only text and can choose: what to put into the next context, when to stop a call, when to run a check, and which sample to keep. The transferable ideas are: (1) prune failed branches from context, (2) pick the shortest or lowest-wander trace of k, (3) stop on trial-answer stability, (4) gate any intervention on a second check, (5) flag missing premises early. Everything else is motivation.

---

## 7. What our agent should take

Schema parts: G guardrail, S state, O operator, M memory. Status: [E] established, [S] single-source, [C] contested.

### Add now (established)

| # | Item | Schema part | Status | Evidence ids |
|---|---|---|---|---|
| A1 | **Log length, switch count and wait count per run.** Code counts tokens, switch cues ("Alternatively", "Wait") and answer candidates. Use as inputs to the stop-or-replan rule, never alone. Wrong runs carry more of both; the sign holds in within-question designs. | G (stuck signal), S6 trigger | [E] | a17, a24, b12, b26, d05, K06 |
| A2 | **Harvest candidates before dropping them.** Code extracts every candidate answer stated in a trace and tests it. Models often hold a correct thought and abandon it. This agrees with S4 as written. | S4 | [E] | a17, c13, b17, K07 |
| A3 | **Difficulty-aware stop on easy items.** After the first checked answer on an easy item, stop. First round is correct in over 92% of cases and extra rounds add little. Matches G11 and G12. | G11, G12, S8 | [E] | a20, b10, c19, a21, K09 |
| A4 | **Verification is conditional, not routine.** Over 90% of post-answer reflections are confirmatory; corrective under 2%. Run the final check once, on something the answer was not fitted to (G3), and add a second check only on a risk signal. This sharpens G1. | G1, S8 | [E] | b17, a21, K10 |
| A5 | **Prefer short parallel attempts to one long one.** Same-question shorter chains are more often correct; parallel thinking beats extended thinking at equal budget. Already in G11; this adds the "pick shortest" tie-break for S7. | G11, S3, S7 | [E] | b12, b11, K06 |
| A6 | **Flag a missing premise early.** Models notice it in 83-100% of traces by step 1.4 and keep going. Put a premise check in S1 and an abstain-or-flag path for unsolvable items. G6 says never abstain on the first pass; the flag should record the doubt and still submit the best attempt. | S1, G6 | [S] on the numbers, [E] on overthinking under missing premises (K17) | a29, a17, a20 |
| A7 | **Prune failed branches from the context passed to the next call.** The Failed-Step Fraction effect is the best causal evidence in this subfield: R1 +8.5 to +14.0 points, GPT-oss +8.4 to +10.8. Delete the failed text and keep a short record in code (not in the prompt) of what was tried (S5 history). Rated [E] for the direction (Feng plus LCoT2Tree); the one-line-note variant is Test first. | S5, M (history) | [E] direction | a24, b14, d07, a23, K08 |
| A8 | **Treat the episode labeller as a logger, not a gate.** Use a written guidebook with contrast rules. Do not gate any action on Verify labels. | G (monitor labels) | [S] but conservative | a07, a09, d02, K02-K04 |

### Test first (not yet established)

| # | Item | Schema part | Status | Evidence ids |
|---|---|---|---|---|
| T1 | **Composite stuck-signal detector.** Switch rate + wait/backtrack count + repeated n-gram + revisit count + Evaluate/Analyze oscillation, judged within problem against length alone. Advisory only; the action needs a second check. Expect AUC 0.68-0.72, not more. | S6 trigger | [S] | d04, d05, d10, K22, K24 |
| T2 | **Where the check sits (three-arm Verify test).** No check vs one final check vs up to K mid-trace checks, at equal tokens. | G (Verify placement), S8 | [C] | a14, a24, b17, d08, K12, K26 |
| T3 | **One-line dead-end note vs summary vs delete vs keep full text.** | S5, M | [S] | b14, d07, K08 |
| T4 | **Prompt-level finish-or-abandon rule with a code check of the dropped thought.** A bare prompt rule failed (29.0 vs 28.9); the version with a scored second check is untested at scaffold level. | G (switch limit) | [S] | a19, d09, d10, K19 |
| T5 | **Answer-stability stop (DEER style) as a black-box call.** | G (stopping) | [S] | c15, c14, K18, K29 |
| T6 | **Difficulty-dependent review cap.** Cap review loops by estimated difficulty (pass rate over N cheap samples). | G11, G12, S0 | [S] | d06, K25 |
| T7 | **Freeze an independently checked intermediate answer as a candidate; require a stated reason to drop it.** | S4, S7 | [S] | a17, c13, K07 |
| T8 | **Episode log of our own agent**: transition matrix of our agent vs the published R1 one. Descriptive; sanity check that our states map to the seven labels. | S log | [S] | a06, K01 |
| T9 | **Impasse type record** (Analysis Paralysis, Rogue Actions, Premature Disengagement) on failures in code or agent tasks. | S6, M | [S] | c18, d13, K20, K27 |
| T10 | **Ablate each operator on a fixed set.** Gandhi's four behaviours (verification, backtracking, subgoal setting, backward chaining) predict RL success; do the same for O1-O8 at equal tokens. | O | [S] | a27, a25, K15 |
| T11 | **Resample-after-plan check.** Do our plan and replan steps change the final answer more than ordinary steps? | O, S6 | [S] | a28, K14 |
| T12 | **Budget extension 1x/2x/4x by difficulty.** Find where extra turns stop paying. | G11, G12 | [C] | b11, c23, K11 |

**Not for the schema:** any Schoenfeld human percentage (unverified, K28); a switch-penalty decoder (needs logits); a Verify-label gate (kappa too low); a model self-judge of its own trace (AUC 0.512). Section 4b of SCHEMA.md already bars "unstructured self-reflection" and "verbal confidence to stop"; the evidence here (b17, d05) supports both entries and adds numbers.

---

## 8. Concrete tests on our bench

All arms run at equal total tokens (count every call, including labelling and probe calls). Metric is accuracy on held-out items unless stated. Items are the bench's SAT-style and puzzle items with a ground-truth check; use 50 items for logging tests, 100 or more for intervention tests.

| Test | Item type | Arms (equal tokens) | Metric | Expected effect |
|---|---|---|---|---|
| **B1 Within-problem logging** (K24) | 200 runs: 20 problems x 10 runs (mixed correct/wrong), our agent plain and scaffold | None (observational). Features: tokens, wait count, backtrack count, switch count, repeated n-gram rate, revisit count, Evaluate/Analyze oscillation, 8 episode ratios | Within-problem AUC, problem-grouped folds, vs length-only and wait-count | Combined features 0.65-0.72 vs length about 0.55. If under 0.60, drop the detector |
| **B2 Three-arm Verify placement** (K26) | Items with a code check, medium difficulty | (a) no check; (b) one final check after Answer; (c) up to K=3 mid-trace checks | Accuracy and tokens | (b) at least equal to (a); (c) lower than (b) at equal tokens. If (c) wins, T2 is wrong |
| **B3 Dead-end note** (K08) | Items where the first attempt fails (about 30% of runs) | (a) full failed text kept; (b) deleted; (c) one-line note; (d) short summary | Accuracy of the continuation | (b) +8 points over (a); (c) between (b) and (d) |
| **B4 Finish-or-abandon rule** (K19) | Medium-hard items | (a) plain; (b) prompt rule only; (c) rule + code flag when a thought is dropped under N tokens + second check of dropped thought | Accuracy; switch count | (b) = (a) within 1 point (as in d09); (c) +2 to +4 |
| **B5 Easy-item stop** (K09) | Easy items (plain pass rate above 90%) | (a) always continue; (b) stop after first checked answer | Accuracy, tokens | Same accuracy, 40% or more fewer tokens |
| **B6 Answer-stability stop** (K18, K29) | 100 mixed items | (a) fixed cap; (b) n-gram repetition stop; (c) trial answer at each switch cue, stop when stable twice | Accuracy per token | (c) 20-30% fewer tokens at same accuracy; weaker on hard items (DEER limits) |
| **B7 Conditional verify** (K10) | Mixed items | (a) verify always; (b) verify only on risk signal (low agreement or composite flag) | Accuracy; share of verifies that change the answer | Under 5% of verifies change the answer in (a); (b) saves 15-40% tokens at equal accuracy |
| **B8 Difficulty-dependent review cap** (K25) | Items spanning easy to hard | (a) fixed cap; (b) cap from difficulty estimate (pass rate over 5 cheap samples) | Accuracy at equal tokens | (b) +2 points |
| **B9 Labeller check** (K02) | 200 of our traces | Cheap labeller (cue rules or BERT) vs strong LLM with guidebook | Cohen kappa; per-class kappa for Verify | Gate only if kappa above 0.75 overall and Verify above 0.70. Expect it to fail for Verify |
| **B10 Transfer** (K27) | 50 coding + 50 planning runs | Same labeller on each | Transition matrix distance to the math matrix; B1 AUC per domain | Verify-heavy tails hold; predictive AUC lower on code/planning |
| **B11 Missing premise** (K17) | 30 unsolvable items mixed with 100 solvable | (a) plain; (b) S1 premise check with flag | Tokens on unsolvable items; accuracy on solvable | 50% fewer tokens on unsolvable; no loss on solvable |
| **B12 Shortest-of-k vs vote** (K06) | Medium-hard items | (a) majority vote of k; (b) shortest of k; (c) vote among the shortest m | Accuracy at equal tokens | (b) or (c) equals vote with 20-40% fewer tokens (Hassid) |
| **B13 Operator ablation** (K15) | Fixed impasse items | Remove one of O1-O8 at a time | Accuracy at equal tokens | A few operators carry most gain; Gandhi-type behaviours (verify, backtrack, subgoal, backward) rank high |
| **B14 Budget extension** (K11) | Easy, medium, hard items | 1x, 2x, 4x allowed turns | Accuracy by difficulty | Gain on hard items at 2x, loss at 4x on easy items |

---

## 9. What does not transfer, and why

- **Human timeline statistics.** Schoenfeld's counts were never verified, and the subjects were students on non-routine problems. Do not import any percentage.
- **Decoding-time fixes** (TIP, logit penalties, word-salad probes, ROM, hidden-state stop probes). They need logits or hidden states. A text-only scaffold sees none. Only the idea transfers.
- **Training-based gains** (self-training to shorten, RL with priming, SFT with long reflection). We do not train. They show what to ask the model for, not what to do.
- **Schoenfeld-label predictors as a gate.** Label noise (0.81-0.86 accuracy, Verify weakest) times a modest signal (AUC 0.68-0.72 best case, d04, d05) gives a flag, not a decision rule.
- **Open-model o1-like traces of 2025 as a model of our agent.** The results come from QwQ-32B-Preview, R1-Preview, R1 and small distills with long visible chains. A frontier API model with hidden or summarised reasoning may show different shapes (o1-mini and o3-mini traces were not visible and looked non-reasoning; a12). Our scaffold's own steps are short calls, not one 10,000-token stream.
- **Single-stream switch counts.** In our design each attempt is a fresh short call (S3). "Thought switches inside one trace" becomes "attempts that change direction," which is a different object. The switch-rate idea transfers to the within-call part only.
- **Review ratio from Feng.** Their Review label covers restating, deleting and rewinding; ours is a code-run check. Do not apply their coefficient to our Verify.
- **Agentic overthinking score.** Judge validated on 20 traces with no kappa (d13). A ranking score for runs, not an online stop.
- **Maths-only evidence.** The predictive signal failed on BBH and HumanEval and held on LiveCodeBench (d05). Do not assume it for planning and agent tasks.
- **Theory of wandering (Lu).** A toy model with an assumed wandering parameter, tested on computation tasks, not fitted to real traces. It motivates a revisit counter; it gives no thresholds.

---

## 10. Open questions

1. Does any Schoenfeld-label feature predict failure on a held-out, problem-grouped set better than length and wait count? (Decides whether an episode labeller is worth building beyond logging.) No test exists.
2. What are precision and recall of a text-only stuck detector against human-labelled stuck points? Only white-box probes have measured accuracy, with machine-made labels.
3. Which Verify helps: early re-read, final check, or mid-trace loops? Nobody varied position under control.
4. Is the useful action on a stuck flag "switch operator" (our S6), "prune and retry", or "stop and submit"? No source compares actions.
5. Do episode statistics transfer to code, planning and agents? Only descriptive Bloom profiles and one agent project page.
6. Does a one-line dead-end note keep the pruning gain? Feng's summary arm is a partial answer only.
7. Does a bare prompt rule plus code-checked dropped thought reproduce TIP at equal tokens on a frontier model?
8. When does extra thinking help? s1 vs Ma/Ghosal. Needs a study varying difficulty, model and budget together.
9. Human baseline: what share of novice attempts never monitor? The book and 1992 chapter must be read.
10. Is the Table 2 vs Table 4 gap (0.681 vs 0.805) a split effect or a prompt effect? Mostly closed (d01, d03), but "easy subset" is untested.
11. Do visible traces tell the truth about the process? Capable yet Parsimonious (c25) warns extracted reasoning may be post-hoc; schema G10 already says reasoning text is not evidence. Episode labels are of the text, not of the computation.
12. Why does the difficulty flip happen (AUC 0.76 easy vs 0.48 hard)? Is "hypothesizing" the only helpful operator on hard items (d06)?
13. Forward-citation search from ThinkARM was not done (search quota). Replications and rebuttals since 2025 may exist.

---

## 11. Sources

[V] = opened this session (page or PDF text read, by the evidence agents or the critique). [M] = snippet or abstract only. A note after the mark gives the limit.

**Schoenfeld episodes and labelling**

- [V] Li, Zhang, Fan, Jiao et al. (2025) Understanding the Thinking Process of Reasoning Models: A Perspective from Schoenfeld's Episode Theory. https://arxiv.org/abs/2509.14662 and https://arxiv.org/pdf/2509.14662 (a05-a09, b06, b07, c01-c04, d01, d02, d16). Numbers re-checked in the critique.
- [V] Li, Fan, Cheng, Feizi, Zhou (2025/2026) Schoenfeld's Anatomy of Mathematical Reasoning by Language Models (ThinkARM). https://arxiv.org/abs/2512.19995 , https://arxiv.org/html/2512.19995v1 , https://arxiv.org/pdf/2512.19995 (a10-a16, b01-b05, b25, c05-c09, c24, d03, d14, d16). Gold set 9 problems; Table 5 column order corrected.
- [M] Schoenfeld (1985) Mathematical Problem Solving, Academic Press. Cited via Li et al. only (a01, c27).
- [M] Schoenfeld (1992) Learning to think mathematically. https://mathed.net/wiki/Schoenfeld_(1992) (a02). Summaries only. Berkeley PDFs 404 (d15).
- [M] Artzt and Armour-Thomas (1992) Development of a cognitive-metacognitive framework for protocol analysis of mathematical problem solving in small groups. https://doi.org/10.1207/s1532690xci0902_3 ; listing https://www.bibsonomy.org/bibtex/e6dbd147f50de65dc380b2549c5f1bd0 (a03, b22).
- [M] Harskamp and Suhre (2007) Schoenfeld's problem solving theory in a student controlled learning environment. https://doi.org/10.1016/j.compedu.2005.11.010 (a04); 403 on access (d15).
- [M] Capable yet Parsimonious: Extracting and Characterizing Hidden Chain-of-Thought in Frontier Models (2026). https://arxiv.org/abs/2609.26637 (c25). Abstract only.

**Wandering, underthinking, overthinking**

- [V] Wang et al. (2025) Thoughts Are All Over the Place: On the Underthinking of o1-Like LLMs. https://arxiv.org/abs/2501.18585 , https://arxiv.org/pdf/2501.18585 , https://arxiv.org/html/2501.18585 (a17-a19, b08, b09, b23, c11).
- [V] Chen et al. (2024) Do NOT Think That Much for 2+3=? On the Overthinking of o1-Like LLMs. https://arxiv.org/abs/2412.21187 (a20, a21, b10, c10).
- [V] Feng et al. (2025) What Characterizes Effective Reasoning? Revisiting Length, Review, and Structure of CoT. https://arxiv.org/abs/2509.19284 , https://arxiv.org/html/2509.19284v1 (a24, b13, b14, b26, d07, d08).
- [V] Lu, Xu, Kankanhalli (2025) Reasoning LLMs are Wandering Solution Explorers. https://arxiv.org/pdf/2505.20296 (b15, b28). Position paper.
- [V] Hassid et al. (2025) Don't Overthink It: Preferring Shorter Thinking Chains. https://arxiv.org/abs/2505.17813 (b12). Abstract page only; marked [V] in the evidence file but only the abstract was read.
- [V] Kang et al. (2025) First Try Matters: Revisiting the Role of Reflection in Reasoning Models. https://arxiv.org/html/2510.08308v1 (b17, b27).
- [V] Ghosal et al. / Ma et al. (2025) Does Thinking More Always Help? Understanding Test-Time Scaling in Reasoning Models. https://arxiv.org/abs/2506.04210 , https://arxiv.org/html/2506.04210 (b11, b24, c16).
- [V] Muennighoff et al. (2025) s1: Simple test-time scaling. https://arxiv.org/abs/2501.19393 (c23). Abstract page.
- [V] Fan et al. (2025) Missing Premise exacerbates Overthinking. https://arxiv.org/abs/2504.06514 (a29). Read through a summarising reader.
- [M] Su, Healey, Nakov, Cardie (2025) Between Underthinking and Overthinking. https://arxiv.org/abs/2505.00127 (b21). Abstract, no numbers.
- [V] TRACE authors (2025) Do LLMs Really Need 10+ Thoughts for "Find the Time 1000 Days Later"? https://arxiv.org/html/2510.07880v2 (c19). First 100,000 of 135,100 characters.
- [V] Marjanovic et al. (2025) DeepSeek-R1 Thoughtology. https://arxiv.org/abs/2504.07128 , https://arxiv.org/html/2504.07128 (a26, b18, c17). First 100,000 of about 400,000 characters.
- [M] Pipis et al. (2025) Wait, Wait, Wait... Why Do Reasoning Models Loop? https://arxiv.org/abs/2512.12895 (c12). Abstract only.
- [V] Cuesta-Ramirez, Beaussant, Mounsif (2025) Large Reasoning Models are not thinking straight. https://arxiv.org/html/2507.00711 (c13).
- [M] Chen and Wang (2026) A Comprehensive Anatomy of Human and DeepSeek-R1 Reasoning. https://arxiv.org/abs/2606.07410 (b16). Abstract only.

**Structure, prediction, causal importance**

- [V] Jiang et al. (2025) LCoT2Tree. https://arxiv.org/abs/2505.22148 (a22, a23).
- [V] Zoumpoulidi, Paraskevopoulos, Potamianos (2026) Cognitive Profiling of LRMs' Reasoning Traces Using Bloom's Taxonomy. https://arxiv.org/pdf/2608.23205 (d04).
- [V] Lee, Queen, Zou (2026) ReasonOps: Operator Segmentation for LLM Reasoning Traces. https://arxiv.org/pdf/2605.29192 (d05, d06).
- [V] Bogdan, Macar, Nanda, Conmy (2025) Thought Anchors. https://arxiv.org/abs/2506.19143 , https://arxiv.org/html/2506.19143v4 (a28, b19, c20). Not re-opened in the critique.
- [V] Kargupta et al. (2025) Cognitive Foundations for Reasoning and Their Manifestation in LLMs. https://arxiv.org/abs/2511.16660 (a25). First 100,000 of 243,635 characters.
- [V] Gandhi et al. (2025) Cognitive Behaviors that Enable Self-Improving Reasoners. https://arxiv.org/abs/2503.01307 (a27, b20, c21). Abstract page for b20 and c21.
- [V] Venhoff et al. (2025) Understanding Reasoning in Thinking Language Models via Steering Vectors. https://arxiv.org/html/2506.18167 (c22).

**Detectors, early exit, intervention**

- [V] Zhang et al. (2025) Reasoning Models Know When They're Right. https://arxiv.org/html/2504.05419 (c14).
- [V] Yang et al. (2025) Dynamic Early Exit in Reasoning Models (DEER). https://arxiv.org/html/2504.15895 (c15).
- [V] Zhang et al. (2025) SmartSwitch. https://arxiv.org/html/2510.19767v1 (d09, d10).
- [V] Xie et al. (2025) WordSaladChopper. https://arxiv.org/html/2511.00536v1 (d11).
- [V] ROM: Real-time Overthinking Mitigation via Streaming Detection and Intervention (2026). https://arxiv.org/html/2603.22016v3 (d12).
- [V] Cuadron et al. (2025) The Danger of Overthinking: Examining the Reasoning-Action Dilemma in Agentic Tasks. https://arxiv.org/html/2502.08235v1 and https://sky.cs.berkeley.edu/project/agentthink/ (c18, d13).
- [M] Pi Loop Police and Pi Antiloop (2026). https://pi.dev/packages/pi-loop-police (c26). Search snippet; no evaluation.
- [M] Survey: Towards a Mechanistic Understanding of Large Reasoning Models (2026). https://arxiv.org/pdf/2601.19928 (c28). The "41 to 52 percent after commitment" figure is second-hand; not used as a finding.

**Not re-opened by the critique (numbers as the first agents reported them):** Thought Anchors, Gandhi, Kargupta, Thoughtology, Lu et al., DEER, probing paper, TRACE, AgentThink, Chen and Wang 2026, s1.
