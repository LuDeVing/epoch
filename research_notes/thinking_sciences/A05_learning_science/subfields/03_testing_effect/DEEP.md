# Testing effect (retrieval practice): deep document

*Subfield A05.03. Built from evidence_a-d.jsonl (ids a01-a31, b01-b30, c01-c27, d01-d22), claims.jsonl (K01-K35) and critique.md in this folder. Why it matters for our agent: background only. The agent has no forgetting, so the human mechanism does not transfer directly. The useful parts are the feedback result, the warning about self-judged confidence, and the finding that item difficulty cannot be set by asking a model.*

## 1. What it is

The testing effect is the finding that trying to recall material gives better later memory than spending the same time re-reading it. The test itself changes memory. It is not only a way to measure it.

Key terms.
- **Restudy**: read the material again. This is the usual control.
- **Retrieval practice**: try to pull the material out of memory (free recall, cued recall, short answer, multiple choice).
- **Direct testing effect**: the tested item itself is remembered better.
- **Forward (test-potentiated) effect**: a test makes learning of later, new material better.
- **Pretesting**: a test before the material is studied.
- **Feedback**: the correct answer shown after the attempt.

The core pattern is a crossover. Restudy wins on a test a few minutes later. Retrieval wins on a test days later (a01).

Scope claims in the schema row, and their status after this research:
- Retrieval beats restudy: established, but the clean effect is smaller than headline numbers (section 5).
- Harder but successful retrieval helps more: supported. The real moderator is whether retrieval succeeds.
- Feedback helps: established.
- Short answer beats multiple choice: **not supported as a general rule**. Smith and Karpicke 2014 failed to reproduce it in three of four experiments (a26, b15).

For our agent: no forgetting, so the benefit is not expected. No study found tests a testing effect inside an LLM agent (K23, K31). What carries over is the feedback and verification lesson.

## 2. History and theories in depth

**Early work (1909-1991).** Abbott 1909 and Gates 1917 found that recitation helped prose retention. Gates tested recitation from 0 to 90% of study time; about 60% was best for prose. First graders showed no effect (a04). Spitzer 1939 studied 3,605 sixth graders in 91 Iowa schools with 600-word articles and 25 five-option items. A test soon after study nearly stopped forgetting. A first test only on day 21, after forgetting was deep, did not help (a05). Tulving 1967 gave 36-word lists over 24 trials. Replacing study trials with test trials left the learning curves similar, so a test trial can do the work of a study trial (a06). Bangert-Drowns 1991 pooled 35 classroom studies: 29 positive, mean d=0.23 (a04). (Early studies were read through the 2006 review, not the originals.)

**Modern founding studies (2006-2011).** Roediger and Karpicke 2006 is the landmark: prose, one test vs one restudy, delays of 5 minutes, 2 days and 1 week (a01, a02). Karpicke and Roediger 2007 and 2008 added dropout designs showing that after a first success, more retrieval helps and more study does not (a07-a09). Karpicke and Blunt 2011 beat concept mapping, a strong elaborative-study rival (a10). Roediger and Karpicke themselves call the 2006 paper in effect a conceptual replication of a century of work (a29, b22). So it is a clean demonstration with a conservative control, not a new finding.

**Theories.** Four are named in Karpicke's 2025 chapter (a31):
1. **Transfer-appropriate processing.** Memory is best when the practice process matches the test process. A heuristic.
2. **Strength and retrieval effort** (Bjork and Bjork 1992, a17). Each memory has storage strength (lasting) and retrieval strength (current access). Retrieving an item with low retrieval strength raises storage strength more. Karpicke calls this a redescription of the effect, not a mechanism.
3. **Elaborative retrieval.** Searching memory activates related mediators that get stored with the target. Carpenter 2009 found weak cues (basket-bread) gave bigger effects than strong cues (toast-bread) (a20). Direct tests failed: mediator activation was not higher after retrieval than after restudy, and was unrelated or negatively related to later recall (Lehman and Karpicke 2016, a19, b18). Rowland's meta-analysis found only a non-significant trend, QB=1.83, p=.40 (b04). Hausman and Rhodes 2018 found modest activation, so the account is not fully dead (a19).
4. **Episodic context** (Karpicke, Lehman and Aue 2014, a22). Items are stored with temporal context. Retrieval tries to reinstate that context. A successful retrieval updates the item's context with the test context. Later retrieval uses the updated context. Built on SAM and the temporal context model.

**Quantitative rivals.**
- **Bifurcation model** (Kornell, Bjork and Garcia 2011, a18, d10). A test splits items: recalled items get a big boost, unrecalled items get none. Restudy gives every item a modest boost. Forgetting rate is equal. This explains the crossover. Karpicke argues it makes the benefit an item-selection artifact and cites two lines of evidence that retrieval does change forgetting rate. We did not follow those up (d10).
- **Dual memory theory** (Rickard and Pan 2017, b23). Study and test form separate traces. A parameter-free model predicted test-condition accuracy and effect size across 10 lab experiments.
- **Error-driven account** (preprint, d20). Larger errors at practice predict more memory gain (WRAP-E model, color-wheel tasks).
- **Mixed designs.** Mulligan 2026 and a 2025 preprint say about two thirds of "testing effects" mix direct and forward effects (b24, d15).

**Recent trend.** 1,215 peer-reviewed articles 1999-2022, over 100 per year since 2018 (b28). Variants: pretesting, forward testing, successive relearning, interpolated testing. b28 cites no LLM-specific work, and a text search of Karpicke's 2025 chapter found no mention of language models (a31).

## 3. Core findings with exact numbers

Status: **est** = established (claims.jsonl), **single** = single source or one lab, **contested**.

| Finding | Numbers | Source (evidence id) | Status |
|---|---|---|---|
| Crossover: one test vs one restudy of prose | N=120, 40 per delay. 5 min: restudy 81% vs test 75% (d=0.52). 2 days: test 68% vs 54% (d=0.95). 1 week: test 56% vs 42% (d=0.83). Interaction F(2,117)=32.10, partial eta2=.35 | Roediger and Karpicke 2006 Exp 1 (a01, b11) | est (K01) |
| Repeated testing vs repeated study, 1 week | N=180. STTT 61%, SSST 56%, SSSS 40% (STTT vs SSSS d=1.26). At 5 min: SSSS 83%, SSST 78%, STTT 71%. Text read 3.4 vs 14.2 times | Roediger and Karpicke 2006 Exp 2 (a02) | single (K02) |
| Students did not foresee it | Predicted 1-week memory higher after SSSS than STTT (d=0.61); actual 40% vs 61% | Roediger and Karpicke 2006 (a03) | single (K02) |
| Repeated retrieval beats dropping recalled items | Swahili pairs: about 80% (ST, SNT) vs 36% and 33% (STN, SNTN), d=4.03. Repeated study of recalled items: no gain. Predictions about 50% in all conditions | Karpicke and Roediger 2008 (a09, b12) | est (K03); one lab |
| Same on word lists | Items recalled once then dropped from testing: about 20% at 1 week. Recalled 4 or 5 times: about 70%. N=60 | Karpicke and Roediger 2007 Exp 2 (a08, b13) | est (K03) |
| Retrieval beats concept mapping | N=80. 0.67 vs 0.45, d=1.50. Replication d=1.07 (short answer), 1.01 (map test) | Karpicke and Blunt 2011 (a10, b14) | single (K11) |
| Elaboration adds nothing after first recall | Exp 1: retrieval .73, study .52, drop .37. Exp 3: retrieval .62 vs elaboration .48 vs study .45 vs drop .36 | Karpicke and Smith 2012 (a21, b17) | single (K12) |
| Self-regulated learners drop items too early | Chosen strategies: drop .60, test .25, study .15 (N=42). Final recall .46 chosen vs about .78 assigned (cross-experiment) | Karpicke 2009 (a11, b21) | single (K04) |
| Meta-analysis: testing vs restudy | g=0.50 [0.42,0.58], k=159, I2=84%, 81% positive, 18% negative. Unpublished g=0.25 vs published 0.58. High-exposure subset g=0.66 | Rowland 2014 (b01) | contested (K05) |
| Feedback moderator | With feedback g=0.73 vs 0.39 without. Delayed feedback g=1.38 (k=6) vs immediate 0.66 (k=46) | Rowland 2014 (b02) | est for feedback (K08); delayed cell tiny |
| Retention interval moderator | 1 day or more g=0.69 vs under 1 day g=0.41 | Rowland 2014 (b02) | est (K05) |
| Test format as practice | Cued recall g=0.61, free recall 0.29, recognition 0.29 (full set). Confounded with feedback use 44% vs 11% | Rowland 2014 (b03) | contested (K09) |
| Classroom quizzing meta-analysis | 222 studies, 48,478 students, g=0.499 | Yang et al. 2021 (b05) | est (K06); abstract read |
| Third meta-analysis | g about 0.61 fixed, 0.70 random (secondary summary, unverified) | Adesope 2017 (b06) | unverified |
| Classroom review | 50 experiments, n=5,374; 57% medium or large benefits; 6% non-WEIRD | Agarwal et al. 2021 (b07) | abstract only |
| Short answer vs multiple choice | N=372, four experiments. Pooled SA vs MC d about 0.07 [-0.24,0.38]. Exp 3 inference test: MC better, F(1,46)=3.97. Exp 4, with success gap cut to 13% (from 42% and 32%): SA advantage appeared | Smith and Karpicke 2014 (a26, b15) | contested (K10) |
| Format depends on feedback | Kang 2007: initial MC 86% vs SA 54% correct. No feedback: MC wins. With feedback: SA slightly wins (Little 2012) | via Karpicke 2025 (d11) | contested (K29) |
| Feedback on wrong and on unsure-right answers | Test plus feedback .87, test only .41, no test .24 (d=1.77). Initially wrong corrected .82 vs .03 (d=6.08). Low-confidence correct .85 vs .40. N=30 | Butler, Karpicke and Roediger 2008 Exp 1 (a24, b16) | est (K08) |
| Spacing | Spaced vs massed g=0.74 (39 effects). Expanding vs equal g=0.03 (54 effects). Massed retests: about 98% in session, about 20% at 2 days. Delaying the first test: 52% vs 44% | Latimier 2021 via chapter (a14); Karpicke and Roediger 2007 (a12, a13) | single (K14) |
| Pretesting helps if cues are related | Related pairs .73 vs .56; unrelated .24 vs .24. Constrained attempt .39 vs .57 (hurt). Delay between attempt and study: no benefit (.55 vs .56) | Grimaldi and Karpicke 2012 (a23, d21) | est (K15) |
| Pretest vs posttest | Internal meta-analysis vs no-test control: pretest d=1.02, posttest d=0.76. Transfer to untested items d=0.20 and 0.09. n=1,573 | Pan and Sana 2021 (b10) | single (K16) |
| Transfer of testing | 192 effects, 122 experiments, N=10,396, d=0.40 [0.31,0.50]. No response congruency d=0.28. PEESE intercept about 0 (d=0.015) | Pan and Rickard 2018 (b08, d08) | est (K07) |
| Transfer moderators stack | Congruency +0.36, elaborated retrieval +0.18, initial accuracy +0.50 per unit (PEESE). Worst case d about -0.05; best case 0.90 (random) or 0.58 (PEESE) | Pan and Rickard 2018 (d09) | single (K28) |
| Term-definition direction | Term benefit reliable; reverse direction only after repeated practice | Pan and Rickard 2017 (b09) | single |
| Publication bias on forward effect | Chan et al. g=0.44 (k=159) fell to 0.02 (3PSM) or -0.02 (PET). Standard designs 0.75 to 0.52 to -0.08. Published 0.50 vs unpublished 0.19 | Boustani and Shanks 2022 (d07) | est (K27) |
| Mixed designs inflate | 67% mixed, 33% direct; mixed larger | Mulligan et al. 2025/26 (b24, d15) | single (K19); abstract only |
| Test anxiety | g=-0.52, 25 effects, 3,374 participants | Yang et al. 2023 (b27) | single (K18) |
| Field effects are small | Gateway math, n=636/584/571: quiz gain 4 to 5 points; exam gain 8 points in one cohort only | OSF preprint 2026 (d18) | single (K34) |
| Online null results | Prolific: 67 of 169 completed, p=.72; 129 of 426, p=.17 | 2026 paper (b26) | contested (K17) |
| Naturalistic events null | N=122, three pre-registered experiments, no objective retrieval advantage | OSF 2026 (d17) | single (K35) |
| Coherent vs scrambled text | N=111 and 117; effect present for both | OSF 2025 (d16) | single (K34) |
| Testing without prior study matches instruction | Practice with feedback only equalled conditions with a study passage | OSF 2026 (d19) | single (K33) |

## 4. Mechanisms and models

Written so an engineer could code each one.

**4.1 Bifurcation model (Kornell, Bjork and Garcia 2011; a18, d10).**
- State: each item i has strength m_i. All items decay at one shared rate.
- Restudy: m_i += small constant for every item.
- Test: draw success from the current strength. On success, m_i += large constant. On failure, m_i is unchanged (and stays unrepaired if there is no feedback).
- With feedback, a failed item gets a restudy-sized boost.
- Result: after a short delay the uniform restudy boost beats the test. After a long delay the large boost on recalled items dominates. This reproduces the crossover (a01).
- Prediction: benefit rises with initial success. Rowland found effects more robust above about 75% success (a15). Pan and Rickard found initial accuracy adds about 0.0058 d per +0.01, d=0.46 across 0.19-0.98 (b08).
- Weakness: Karpicke says it leaves out a change in forgetting rate (d10).

**4.2 Storage vs retrieval strength (Bjork and Bjork 1992; a17).**
- Two variables per item: S (storage, only rises) and R (retrieval, decays fast, rises on access).
- Gain in S on a retrieval is larger when R is low, as long as the retrieval succeeds.
- Gives "desirable difficulty": delay the first test (52% vs 44%, a13) so R is lower, but keep success high.
- Qualitative. No parameters in the sources.

**4.3 Episodic context account (a22).**
- Items are stored as (item, context vector). Context drifts over time.
- Retrieval cues with the current context. Recall probability depends on similarity to the stored context.
- On a successful retrieval, the stored context is updated to include the test context.
- Implement with SAM or the temporal context model. Explains why recall beats recognition and why spacing helps. Not run in the sources we read.

**4.4 Dual memory model (Rickard and Pan 2017; b23).** Two independent traces: one from study, one from test. Final recall draws on both. A parameter-free version fit 10 experiments, including an upper bound on effect size and a feedback benefit.

**4.5 Error-driven learning (d20).** Gain grows with prediction error at practice. Perceived and predicted errors add terms (WRAP-E, continuous color-wheel tasks).

**4.6 Moderator regression for transfer (Pan and Rickard 2018; b08, d09).**
- d = intercept + 0.36*congruency + 0.18*elaborated_retrieval + 0.50*initial_accuracy (PEESE values; congruency and elaboration 0/1, accuracy 0 to 1).
- The intercept is near 0, so an effect on a changed question type needs all three factors.
- This is a descriptive fit, not a validated predictor. It extrapolates to the edges of the data (accuracy 0.19-0.98).

**4.7 Schedulers built on testing (c13-c15).**
- Half-life regression (Settles and Meeder 2016): p(recall) = 2^(-delay/h), with h predicted from features. MAE 0.128 vs Leitner 0.235 vs Pimsleur 0.445 on 12.9 million traces.
- Memorize (Tabibian et al. 2019): optimal review rate proportional to the forgetting probability, from optimal control.
- MemoryBank (Zhong et al. 2023): R = exp(-t/S). Each recall adds 1 to S and resets t to 0.
- All three need a forgetting process. Our agent has none, so they apply only if we add decaying or truncated memory.

## 5. What holds up

**Replications and agreement.**
- The crossover (restudy wins early, testing wins late) was reproduced inside the founding lab in Exp 1 and 2 (a01, a02), in word lists (a07), in Swahili pairs (a09), in schools (Spitzer 1939, a05) and in a classroom demonstration (Einstein et al. 2012, a29).
- Three meta-analyses agree on a medium effect: Rowland g=0.50 (b01), Yang 2021 g=0.499 (b05), Adesope 2017 about 0.6-0.7 (b06, unverified).
- A 2025 higher-powered replication found the effect for coherent and scrambled text alike (N=111, N=117; d16).
- Five high-powered experiments failed to replicate a *negative* testing effect on relational processing (b25). The plain effect survived.

**Failures and shrinkage.**
- Short answer over multiple choice failed in 3 of 4 experiments (a26).
- Publication bias. Rowland's published g=0.58 vs unpublished 0.25 (b01). The forward-effect literature fell from 0.44 to about zero under correction (d07). Pan and Rickard's transfer intercept fell to about zero (d08). PET over-corrects with high heterogeneity (I2 about 88%), so the truth lies between. Rowland and Adesope themselves were not bias-corrected in anything we could open (d22).
- Mixed designs are about two thirds of the literature and inflate effects (b24, d15).
- Online engagement: two Prolific experiments null, with 60-70% attrition (b26). Not designed as replications.
- Naturalistic event memory: three pre-registered experiments, no objective advantage (d17).
- Field data: gateway math gains 4-5 quiz points, far below lab effects (d18). The lab-vs-meta gap is d=4.03 (a09, unmatched trial counts, non-overlapping score ranges) vs g=0.50.
- No large pre-registered multi-site replication of Roediger and Karpicke 2006 was found (K35).
- Most founding work comes from one lab. Many a-file lines were read through Karpicke's 2025 chapter, not the originals (critique).

**Moderators (what changes the size).**
- Retention interval: longer is better, 0.69 vs 0.41 (b02). Immediate tests can be null or negative.
- Feedback: roughly doubles the effect, 0.73 vs 0.39 (b02). It repairs wrong answers (82% vs 3%) and unsure-right answers (85% vs 40%) (a24).
- Initial success: higher helps. Effects are more robust above 75% initial success (a15). The threshold was not verified and reads better as a slope (d09).
- Format: recall tends to beat recognition, confounded with feedback and success (b03). Short answer vs MC depends on success and feedback (a26, d11).
- Repetitions: repeated retrieval beats one retrieval (39% vs 26% at 2 days, a12). Dropping after one success hurts (a09).
- Spacing: spaced beats massed (g=0.74). Expansion does not beat equal spacing (g=0.03) (a14).
- Relatedness: pretesting works only for related cues with immediate study (a23).
- Working memory: mostly no relation. A few studies find low-WM learners gain more, one the opposite (a31).
- Emotion: practice lowers test anxiety, g=-0.52 (b27).
- Culture: only 6% of classroom experiments are non-WEIRD (b07).
- Material: weaker for rearranged items, untested same-study material and worked examples (b08).

**Interventions that worked.**
- Retrieval with feedback, repeated, at a delay, with high success (K03, K08).
- Retrieval over elaborative concept mapping (a10).
- Pretesting for related material (a23, b10).
- Practice with feedback even without prior study (d19, preprint).

**Interventions that did not work.**
- Elaboration after first correct recall (a21).
- Expanding schedules for long-term retention (a12, a14).
- Forced guesses with unrelated cues, or constrained retrieval (a23).
- Letting learners choose when to stop (a11).
- Massed retesting: 98% in session, worst retention (a12).
- Restudy as the "safe" choice: students felt most confident and remembered least (a03).

## 6. Language models

**Headline: no direct study.** We found no experiment that tests retrieval vs restudy inside an LLM context or agent loop, at equal tokens, with a forgetting event (c26, d14, K23, K31). Cao et al. 2025 tested seven human memory effects in LLMs (list length, list strength, fan, false memory, cross-domain transfer, serial position, meaningful vs nonsense). The testing effect was not among them (d14). Search tools were limited, so absence is not proof.

**A. LLMs as question writers for human students.**

| Study | Result | Evidence |
|---|---|---|
| An et al. 2025, data science, about 60 students | LLM MCQs with feedback: quiz mean 0.89 (n=31) vs 0.73 (n=27) in a no-practice cycle. U=703, p<0.0001, r=0.586. Non-randomised, fixed order, different quiz material, ceiling (median 0.95), no instructor arm | c01, d05 |
| Same paper, generation | Gemini Flash made the items. Roughly two thirds of raw MCQs failed the authors' standards before review | c02 |
| Leong et al. 2026, 700+ students, 30 LLM vs 30 instructor items | LLM items easier (difficulty difference -1.01, probability about 1.0) and less discriminating (-0.19, probability 0.94). Correlation with final exam 0.15 vs 0.20 (Steiger p=0.45). Length and speed looked alike (p=0.63, p=0.18) | c03, c04 |
| An and Wang 2026, 7,888 responses | LLM difficulty label vs real difficulty rho=0.06; Bloom level 0.02. Label vs Bloom 0.90. Perceived deep-learning benefit fell over the term | c07, d06 |
| Elkins et al. 2025, 24 teachers | GPT-3.5 candidates did not lower quiz quality. Unanswerable 0.08-0.12. No learner outcomes | c08 |
| Tullis et al. 2026 (CogSci) | AI questions plus AI feedback beat rereading at a delay. No numbers read | c06 |
| Yusof 2025 | n=64; LLM practice group beat no-practice control. Not opened | c05 |
| Kestin et al. 2025, Harvard physics crossover RCT, N=194 | AI tutor median post-test 4.5 vs 3.5; effect 0.63 (regression), 0.73-1.3 SD (quantile). Not pure retrieval practice | c16 |
| Marketing RAG tutor (AERA 2026) | No significant differences. Snippet only | c21 |

LLM-made practice questions beat no practice in two small quasi-experiments. Nobody has shown them equal to instructor questions on learning. Item difficulty is the weak point, and difficulty is an active ingredient of the effect.

**B. LLM training that looks like testing (analogy only).**
- Jiang et al. 2024, pre-instruction-tuning (PIT), Llama-2 7B/70B, Wikipedia 2023 film data, exact match: closed-book 9.5/17.2; continued pretraining 27.6/41.7; pretrain then instruction-tune 30.3/46.4; PIT 45.4/62.7; PIT++ 48.1 (7B). The "17.8%" is 17.8 points (c09, critique item 6).
- Order matters: QA before documents 38.2 vs after 27.2 (grouped); 45.9 vs 43.2 (interleaved) (d12).
- Gains were not from reduced forgetting or token weighting: mixing test documents into instruction tuning gave 30.2; weighted continued pretraining 27.7 (c10).
- Document perplexity falls near 1 while QA stays low. This resembles "re-reading feels fluent, retrieval works" (c27). The authors do not claim this link.
- Self-Tuning (Zhang et al. 2024/25): self-made comprehension and reflection tasks. Wiki-Bio EM, from a garbled table (moderate confidence): continued pretraining 3.62, instruction tuning 5.13, PIT 11.61, Self-Tuning 31.52. Pattern repeats on Llama2-7B, Qwen2-7B and Mistral-7B (c11, d13). No 2025-2026 frontier model test found.
- Allen-Zhu and Li 2023: without varied rewrites or QA in pretraining, extraction accuracy was 0% even after instruction tuning (b30, abstract only).
- Honest reading: these show format matching (transfer-appropriate processing) more than a retrieval-practice effect (d12). They change weights. Our agent does not.

**C. How LLMs behave as memory (not like people).**
- Memory GAPS (Tulving test, mistral-7b-instruct): immediate recognition of copy cues 1.00, others 0.00; delayed false alarms 0.41-0.50; delayed recall of copy cues 0.00. One model; table and text disagree on one cell (c12).
- Practice in the term direction does not transfer to the reverse direction in people (b09). Allen-Zhu and Li found a similar one-way pattern in LLMs (b30). The two are parallel, not proven the same.

**D. Agent memory and self-improvement.**
- Task2Quiz (Liu et al. 2026): 30 environments, 224 tasks, 1,967 QA pairs. Task success is a poor proxy for world knowledge. Memory systems did not reliably beat keeping the full context (52.41 in-context vs 52.36 Mem0 for one model). The quiz was used only as measurement (d01).
- Yuan et al. 2026, LoCoMo 3x3: accuracy spread about 20 points by retrieval method (BM25 57.1%, cosine 73.4%, hybrid 77.2%), 3-8 points by write strategy. Raw chunks matched costly extraction. Hybrid cut Basic RAG retrieval failures from 35.3% to 11.4% (c17, d02).
- ARISE 2026 (abstract only): learn from failures and accept a rule only if held-out accuracy rises. +10.9 SOP-Bench with teacher, +10.0 with self-diagnosis, +5.8 tau2-bench. 4.0% fewer calls (d03).
- Migration-agent audit 2026 (abstract only): 264 of 367 held-out units (72%) shared a reference with training. Memory effect 0.015 fell to 0.002 [-0.008, 0.011] on 103 leak-free units. A copy baseline (0.222) beat every LLM system (max 0.163) (d04).
- Settles and Meeder, Tabibian et al. and MemoryBank are scheduling and decay systems built on testing logic (c13-c15).

**What changed behaviour, and by how much.**
- Question-first exposure in training: +17.8 points EM (single study, old models).
- Learning from failures with a verifier gate: about +10 points (abstract only).
- Memory system vs plain context: no reliable gain (d01).
- Elaborate storing vs raw storing: 3-8 points. Better retrieval: about 20 points (d02).
- Nothing measures self-quizzing at inference time.

## 7. What our agent should take

Status: [E] established, [S] single-source, [C] contested. Schema parts: G guardrail, S state, O operator, memory.

### Add now (established)

The effect needs forgetting, so little is "add now". These are support for existing parts, plus bench rules. No new schema element.

1. **Feedback must come from a source check, not from the model's opinion.** Part: G2, G3 (already present). [E] K08; evidence a24, b02, b16, d11, d19. Test plus feedback .87 vs .41 test only; wrong answers corrected .82 vs .03. More support for existing guardrails.
2. **Check unsure-right answers as well as failures.** Part: S4/S8. [E] K08; evidence a24, b16. Feedback raised retention of low-confidence correct answers from .40 to .85. This is a human memory result. The agent analogue is verifying answers whose attempts disagreed, which G1 already allows. No change needed.
3. **Never use a model's own difficulty label.** Part: S0 gate. [E] K22, with K29 [C]; evidence c07, d06. LLM difficulty vs empirical difficulty rho=0.06 (n=7,888). S0 already uses the class's measured plain pass rate. Keep that.
4. **Any generated check item needs a filter.** Part: S4, G5. [E] K22; evidence c01-c04, c07, d05. About two thirds of raw LLM items failed review (c02). Already covered by "code selects".
5. **Leak checks on any self-practice test.** Part: G7 and bench logging. [S] K32; evidence d04. 72% held-out overlap faked a memory effect. A test-design rule, not a schema rule.
6. **Do not judge learning by an immediate test.** Part: bench rule. [E] K01; evidence a01, b11. A 5-minute test favours restudy. Measure after a context reset.

### Test first

7. **Reconstruct-before-reread after a context reset.** Part: memory, S9 lessons. [S] K01, K23; no direct LLM evidence. Test T1.
8. **Do not stop checking after one pass.** Part: G6, S8. [S] K04; evidence a11, b21. Test T2.
9. **Predicted vs actual accuracy after re-reading vs retrieving.** Part: G calibration. [S] K02; evidence a03. Test T3.
10. **Attempt before reading a source.** Part: O, S3. [E] for humans (K15; a23, b10, d21), but the LLM analogue is loose (PIT is a training analogue, d12). Test T4.
11. **Generate then check beats recognise then check.** Part: S3. [C] K09; evidence b03, a26. Test T5.
12. **Self-quiz transfers to rephrased questions.** Part: O (transfer of verification). [E] for humans that transfer is weak (K07; b08, b09). Test T6.
13. **Success-rate-binned self-checks.** Part: S9 class record. [S] K28; evidence d09. Test T7.
14. **Gap-detection quiz on world state.** Part: memory. [S] K31; evidence d01. Test T8.
15. **Learn from failures with a held-out gate (ARISE-style).** Part: memory lessons (schema section 5). Fits "trusted only after it helps on two different problems". [S] d03, abstract only. Test T9.

Not recommended: any forgetting or spacing scheduler (K14, K26) until the agent has decaying memory.

## 8. Concrete tests on our bench

All arms get equal total tokens. Items are held out. Include a leak check: no overlap in source, answer or paraphrase between practice and test items.

| # | Item type | Arms (equal tokens) | Metric | Expected effect |
|---|---|---|---|---|
| T1 | Long-document QA with a forced context reset between reading and answering (20 facts, 5 direct and 3 rephrased test questions) | A: re-read the stored note once. B: reconstruct from memory, then check against the note (same tokens). C: no extra step | Accuracy after reset, direct and rephrased | Small or zero for direct questions if the note stays in context. Gain only if the note is truncated or summarised. Rephrased gain at most d 0.1-0.2 |
| T2 | Multi-fact checks where the first pass is right about 70% of the time | A: verify each item once. B: verify again after intervening work. C: re-read | Final accuracy on items that passed first check; late errors caught | Little for a deterministic code check. Some where the model re-judges. Tests K04 |
| T3 | Model predicts its own accuracy on 50 items after (a) re-reading and (b) retrieving | Two arms | Calibration (Brier score), over-confidence gap | Over-confidence larger after re-reading. Size unknown |
| T4 | Closed-book attempt then read a source vs read first then answer | Pretest-then-read vs read-then-answer | Final accuracy, split by whether the attempt was semantically close to the answer; anchoring harm from wrong guesses | Gain only when the attempt is in the right neighbourhood |
| T5 | Questions where options can be supplied | Generate answer then check vs choose from options then check | Accuracy; lure adoption rate | Generate-first better without feedback; similar with a source check (a26, d11) |
| T6 | Fact practice, then test on direct, rephrased, inference and reversed-direction questions | Self-quiz vs re-read | Accuracy per question form | Gain on the practised form; near zero on reversed or inference forms (b08, b09) |
| T7 | Self-made checks in three bins by measured pass rate (under 50%, 50-75%, over 75%) | Same budget per bin | Downstream accuracy gain per bin | Gains rise with success rate; low bin near zero or negative (d09) |
| T8 | Text game or tool environment, 20 grounded questions after exploration | Explore only vs explore then self-quiz and revisit gaps | Quiz score and task success | Quiz score higher if self-quiz exposes gaps; task success may not move (d01) |
| T9 | Held-out agent tasks (SOP-style or our own) | No memory vs raw failures stored vs rule distilled with held-out acceptance | Pass rate, leak-free split | A few points; a leak-free split may erase them (d03, d04) |

## 9. What does not transfer, and why

- **The core mechanism.** Retrieval strengthens a decaying memory trace. An LLM in a context window does not forget between steps. Re-reading is exact and cheap. The condition for the crossover, a forgetting gap, is missing (a01, a18).
- **Desirable difficulty.** In humans a harder successful retrieval gives more storage strength (a17). A frozen model has no storage strength to raise. The model also cannot rate item difficulty (rho 0.06, d06).
- **Spacing and scheduling.** No forgetting means no optimal review rate (c14, c15). Relevant only for a future decaying memory.
- **Test anxiety, motivation, engagement, culture.** Human only (b27, b26, b07).
- **Metacognitive illusions.** The agent may have its own, but not necessarily the human fluency illusion. Untested in LLMs here (K02 is human only).
- **LLM training results (PIT, Self-Tuning).** They change weights. Our agent does not train. The shared lesson is about question-shaped exposure, closer to format matching (d12). Evidence is from Llama-2-era models on Wikipedia.
- **Memory-system results.** They concern store and retrieve for the system, not practice by the learner (c17).
- **LLM quiz-writer classroom evidence.** It shows LLMs can supply questions for humans. It says nothing about the agent learning.
- **Large effect sizes.** d=4.03 (a09) and d=1.50 (a10) come from one lab with strong controls and unmatched trials. Field and meta-analytic effects are far smaller, and bias-corrected values for some sub-effects are near zero (d07, d08, d18).

## 10. Open questions

1. Does self-quizzing inside an LLM agent loop (after context truncation or between sessions) change later accuracy at equal tokens? No direct study found (K23, K31).
2. Does a large pre-registered multi-site replication of Roediger and Karpicke 2006 exist, and how large is the effect? None found (K35).
3. What are Rowland 2014 and Adesope 2017 after publication-bias correction? Neither full text could be opened for this (d22).
4. Is the 75% initial-success threshold real, or a slope (d09)?
5. How much of the benefit is feedback and how much is retrieval? Rowland's delayed-feedback cell is k=6 (b02). The no-study-with-feedback preprint suggests feedback alone may suffice (d19).
6. Do PIT and Self-Tuning reproduce on 2025-2026 frontier models, and is "question exposure first" testing or format matching (d12, d13)?
7. Does a randomised study show LLM-written quizzes equal instructor quizzes in learning gains at equal exposure? None found (c05, d05).
8. For agents without forgetting, does reconstruction-style rehearsal do anything besides compress context, such as exposing gaps?
9. What are the two lines of evidence that retrieval changes forgetting rate beyond bifurcation (d10)?
10. How do Yang 2021's moderators (format match, repeats, feedback) interact? Not opened (b05).
11. Do the Mulligan 2026 effect sizes survive when only direct designs are used (b24)?
12. Is the human fluency illusion (a03) present in LLMs? Are model forecasts of their own accuracy better after re-reading or after retrieval?

## 11. Sources

[V] = opened and read. [M] = snippet, abstract or secondary summary only.

**Founding and lab work (Purdue Learning Lab PDFs)**
1. [V] Roediger and Karpicke 2006, Test-enhanced learning. https://learninglab.psych.purdue.edu/downloads/2006/2006_Roediger_Karpicke_PsychSci.pdf
2. [V] Roediger and Karpicke 2006, The power of testing memory (review). https://learninglab.psych.purdue.edu/downloads/2006/2006_Roediger_Karpicke_Review.pdf
3. [V] Karpicke and Roediger 2007, Repeated retrieval, JML. https://learninglab.psych.purdue.edu/downloads/2007/2007_Karpicke_Roediger_JML.pdf
4. [V] Karpicke and Roediger 2007, Expanding retrieval practice. https://learninglab.psych.purdue.edu/downloads/2007/2007_Karpicke_Roediger_JEPLMC.pdf
5. [V] Karpicke and Roediger 2008, Science. https://learninglab.psych.purdue.edu/downloads/2008/2008_Karpicke_Roediger_Science.pdf
6. [V] Butler, Karpicke and Roediger 2008. https://learninglab.psych.purdue.edu/downloads/2008/2008_Butler_Karpicke_Roediger_JEPLMC.pdf
7. [V] Karpicke 2009, Metacognitive control. https://learninglab.psych.purdue.edu/downloads/2009/2009_Karpicke_JEPGeneral.pdf
8. [V] Karpicke and Blunt 2011, Science. https://learninglab.psych.purdue.edu/downloads/2011/2011_Karpicke_Blunt_Science.pdf
9. [V] Karpicke and Smith 2012. https://learninglab.psych.purdue.edu/downloads/2012/2012_Karpicke_Smith_JML.pdf
10. [V] Grimaldi and Karpicke 2012. https://learninglab.psych.purdue.edu/downloads/2012/2012_Grimaldi_Karpicke_MC.pdf
11. [V, in part] Karpicke and Grimaldi 2012. https://learninglab.psych.purdue.edu/downloads/2012/2012_Karpicke_Grimaldi_EDPR.pdf
12. [V] Smith and Karpicke 2014. https://learninglab.psych.purdue.edu/downloads/2014/2014_Smith_Karpicke_Memory.pdf
13. [V] Lehman and Karpicke 2016. https://learninglab.psych.purdue.edu/downloads/2016/2016_Lehman_Karpicke_JEPLMC.pdf
14. [V] Roediger and Karpicke 2018, Reflections. https://learninglab.psych.purdue.edu/downloads/2018/2018_Roediger_Karpicke_Perspectives.pdf
15. [V] Karpicke 2025, Retrieval-based learning chapter. https://learninglab.psych.purdue.edu/downloads/2025/2025_Karpicke_Retrieval_Based_Learning_Review.pdf
16. [M] Spitzer 1939, Tulving 1967, Gates 1917, Bangert-Drowns 1991, Duchastel and Nungester 1982, Kang et al. 2007 (via source 2)
17. [M] Bjork and Bjork 1992; Kornell, Bjork and Garcia 2011; Karpicke, Lehman and Aue 2014; Carpenter 2009; Hanawalt 1937; Latimier et al. 2021; Marsh et al. 2009; Little 2012; Butler and Roediger 2007 (via source 15)

**Meta-analyses and reviews**
18. [V] Rowland 2014. https://courseware.epfl.ch/assets/courseware/v1/fdde2f0aa590bf3b1324077a6bf1540c/asset-v1%3AEPFL%2BDEMO%2B2020%2Btype%40asset%2Bblock/Rowland2014-meta-analysis.pdf
19. [M] Yang et al. 2021 (abstract). https://doi.org/10.1037/bul0000309
20. [M] Adesope, Trevisan and Sundararajan 2017. https://doi.org/10.3102/0034654316689306
21. [M] Agarwal, Nunes and Blunt 2021. https://doi.org/10.1007/s10648-021-09595-9
22. [V] Pan and Rickard 2018. https://sc-pan.github.io/pdf/PR_2018.pdf ; https://doi.org/10.1037/bul0000151
23. [V] Boustani and Shanks 2022. https://doi.org/10.1525/collabra.31996
24. [V] Yang et al. 2023, test anxiety. https://link.springer.com/article/10.1007/s10648-023-09801-w
25. [V] Pan, Dunlosky, Xu and Ouwehand 2024. https://sc-pan.github.io/pdf/PDXO_2024.pdf
26. [M] Mulligan et al. 2025/26, direct vs forward effects. https://osf.io/preprints/psyarxiv/tw5us_v1/
27. [M] Rowland and Adesope full-text access attempt. https://doi.org/10.1037/a0037559

**Human primary studies and preprints**
28. [V] Pan and Rickard 2017. https://sc-pan.github.io/pdf/PR_JEPA_2017.pdf
29. [V] Pan and Sana 2021. https://sc-pan.github.io/pdf/PS_2021.pdf
30. [V] Rickard and Pan 2017. https://sc-pan.github.io/pdf/RP_PBR_2017.pdf ; [M] https://link.springer.com/10.3758/s13423-017-1298-4
31. [V] Testing the testing effect on Prolific, 2026. https://pmc.ncbi.nlm.nih.gov/articles/PMC12894256/
32. [M] Failed replications of the negative testing effect, 2015 (Europe PMC title search)
33. [V] OSF 2025, coherent and incoherent text. https://osf.io/preprints/psyarxiv/d7pcx_v1/
34. [V] OSF 2026, event memory and review. https://osf.io/preprints/psyarxiv/tgm3w_v1/
35. [V] OSF 2026, gateway math. https://osf.io/preprints/psyarxiv/sj3w7_v1/
36. [V] OSF 2026, testing without prior study. https://osf.io/preprints/psyarxiv/sqjbc_v1/
37. [V] OSF 2025, error magnitudes. https://osf.io/preprints/psyarxiv/htp57_v1/
38. [M] Pan et al. 2019 pretesting (snippet). https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6760123/
39. [M] 2024 artificial-language paper, g=0.50-0.63 (snippet). https://link.springer.com/10.3758/s13421-021-01236-4

**LLM and AI studies**
40. [V] An et al. 2025. https://arxiv.org/abs/2507.05629
41. [V] Leong et al. 2026. https://aclanthology.org/2026.aimecon-main.21.pdf
42. [V, abstract and first page] Tullis et al. 2026. https://escholarship.org/uc/item/4043m5w0
43. [V] An and Wang 2026. https://arxiv.org/abs/2609.27063
44. [V] Elkins et al. 2025. https://arxiv.org/abs/2401.05914
45. [V] Jiang et al. 2024, PIT. https://arxiv.org/abs/2402.12847
46. [V] Zhang et al. 2024/25, Self-Tuning. https://arxiv.org/abs/2406.06326
47. [M] Allen-Zhu and Li 2023. https://arxiv.org/abs/2309.14316
48. [V] Memory GAPS. https://arxiv.org/abs/2402.16505
49. [V] Zhong et al. 2023, MemoryBank. https://arxiv.org/abs/2305.10250
50. [V] Settles and Meeder 2016. https://aclanthology.org/P16-1174.pdf
51. [V] Tabibian et al. 2019. https://arxiv.org/abs/1712.01856
52. [M] Pavlik and Anderson 2008. https://doi.org/10.1037/1076-898X.14.2.101
53. [V] Kestin et al. 2025. https://doi.org/10.1038/s41598-025-97652-6
54. [V] Yuan, Su and Yao 2026. https://arxiv.org/abs/2603.02473
55. [V] Liu et al. 2026, Task2Quiz. https://arxiv.org/abs/2601.09503
56. [V, abstract] ARISE 2026. https://arxiv.org/abs/2611.23588
57. [V, abstract] Migration-agent audit 2026. https://arxiv.org/abs/2611.16143
58. [V] Cao, Schooler and Zafarani 2025. https://arxiv.org/abs/2509.17138
59. [M] Yusof 2025 (via Leong et al.); marketing RAG tutor https://convention2.allacademic.com/one/aera/aera26/online_program_direct_link/view_paper/2282791/ ; NPS report https://faculty.nps.edu/ncrowe/CSCI25_testing_generated_questions_final.pdf ; AI exam field study https://aitopics.org/doc/arxivorg:876F20D4

## Source audit (2026-11-20)

Fresh auditors re-opened the sources of 5 established claims: 3 confirmed as written, 2 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **A05.03-K15** (reworded: the sources support less). Grimaldi & Karpicke 2012: .73 vs .56 for related pairs and no effect for unrelated pairs (Exp 1) are right, but 'not after a delay' misstates Exp 3, where the delay was between the pretest and its study trial (delayed-pretest .55 vs no-pretest .56), not a retention delay; Pan and Sana 2021 shows pretesting helps in applied passage settings but does not test unrelated pairs. Corrected claim: Retrieval attempts before study (pretesting) help for semantically related word pairs when study follows immediately (.73 vs .56 recall), but not for unrelated pairs and not when the study trial is delayed relative to the pretest (delayed pretest .55 vs .56 no pretest); this is a boundary condition on word-pair pretesting, not a statement about long retention delays.
- **A05.03-K22** (now contested: a source does not say this). An et al. 2025 verified (0.89 vs 0.73, n=31/27, about 2/3 of raw MCQs unsuitable by authors' experience), but Leong et al. (700+ students, 30 LLM items) found LLM items easier (-1.01 difficulty) and less discriminating with overall weaker psychometrics, not matching instructor items; An and Wang 2026 shows LLM difficulty labels do not predict empirical difficulty.
- **A05.03-K01** (now single-source: only one opened source, code check).
- **A05.03-K03** (now single-source: only one opened source, code check).
- **A05.03-K06** (now single-source: only one opened source, code check).
- **A05.03-K07** (now single-source: only one opened source, code check).
