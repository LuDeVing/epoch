# Metacognition models: deep document

Subfield C03.09. Focus: confidence and monitoring. Key work: Fleming. Why it matters: a guardrail on stated confidence.
Evidence ids (a01-a25, b01-b25, c01-c28, d01-d19) refer to the evidence_*.jsonl files in this folder. Claim ids (C03.09-K01 to K25) refer to claims.jsonl. Corrections from critique.md are applied here.

## 1. What it is

Metacognition models describe how a system watches its own thinking and uses what it sees to steer that thinking. Two parts matter for us.

- Monitoring: the system forms a judgment about its own state. Examples: confidence in an answer, feeling of knowing, judgment of learning, error detection.
- Control: the system acts on that judgment. Examples: stop, keep going, retry, look something up, ask for help, abstain.

The key technical point is that confidence has three separable parts (a01, b01, K01).

1. Bias: the overall level of confidence. Does the system say "90%" a lot?
2. Sensitivity (discrimination): do high-confidence trials tend to be correct and low-confidence trials wrong? Measured bias-free by the area under the type 2 ROC (AUROC2, called AUROC in LLM papers). Chance is 0.5.
3. Efficiency: sensitivity given how good the task performance is. Measured by meta-d' divided by d' (M-ratio). 1.0 means confidence uses all the evidence the decision used.

Calibration (do 70% claims come true 70% of the time; measured by ECE or Brier) is a fourth, separate idea. A system that says 75% on every trial can be perfectly calibrated with zero discrimination (b02, K01).

For a language-model agent this gives a concrete question. When the agent writes "I am 85% sure", or when code reads a confidence from it, how much should that number change what we do next? The evidence says: very little by itself, unless it is measured on the agent, paired with a second signal, and used only to gate cost. The schema already says "Using a model's verbal confidence to stop" is not to be added (SCHEMA 4b). This document keeps that rule for stopping or submitting on a raw stated number, but finds a narrower, tested role for confidence: ranking answers, and gating a second attempt (section 7).

## 2. History and theories in depth

**Nelson and Narens (1990), metamemory framework (a07, snippet only).** Two levels. The object level does the task. The meta level holds a model of the object level. Information flows up (monitoring: confidence, feeling of knowing, judgment of learning) and down (control: stop, continue, allocate study time, change strategy). This is the shape of every later scaffold that has a "check" and a "decide" step. Not opened this session.

**Koriat (1997), cue-utilization (a08, snippet only).** Judgments of learning are inferences from cues, not direct reads of memory strength. Cues are intrinsic (item difficulty), extrinsic (study conditions) and mnemonic (retrieval fluency). Cues can mislead: fluent items feel known. Later, Koriat (2012) proposed that confidence comes from self-consistency across internally generated answers. This is the human parent of sample-agreement confidence in LLMs (a21). Neither paper could be opened (403, d19).

**Signal-detection tools.** Maniscalco and Lau (2012) introduced meta-d' (a09, snippet only): fit the type 2 ROC given a type 1 signal-detection model, so metacognitive sensitivity is in type 1 d' units. Fleming and Lau (2014) is the opened review (a01, a02, b01). Key points: Pearson phi and Goodman-Kruskal gamma are distorted by response bias and by task performance. "The same individual will appear to have greater metacognitive sensitivity on an easy task compared to a hard task" (a01). Parametric type 2 d' is unsafe (unequal variance, non-Gaussian). AUROC2 is non-parametric but still rises with task accuracy. Only M-ratio is meant to be performance-independent. Fleming (2017) added HMeta-d, a hierarchical Bayesian fit that gives credible intervals and beats point fits when data are few (a04).

**Individual differences (Fleming et al. 2010, d15, opened).** N = 32 adults. Two-interval visual task, staircase holding accuracy near 71% (range 70-74%). Confidence on a 1-6 scale. Aroc ranged 0.55 to 0.75. Aroc was uncorrelated with accuracy (r = -0.11, P = 0.56), so introspective accuracy is not just task skill. Split-half reliability r = 0.69. Right anterior prefrontal grey matter (BA10) correlated with Aroc (tmax 4.8, corrected P < 0.05). No link to d' (r = 0.15) or to confidence level (r = -0.023). Small sample for a brain-structure correlation; a large replication was not checked here.

**Is there a general metacognition ability? (Mazancieux 2020, b03).** N = 181, four 2AFC tasks (episodic memory, semantic memory, executive function, visual perception). Efficiency (meta-d'/d') correlated across tasks: 5 of 6 pairs significant, even where first-order d' did not correlate. Earlier nulls were probably low power. Counter-points: Baird 2013 and Kelemen 2000 found no cross-domain link (a04 notes).

**Confidence as second-order inference (Fleming and Daw 2017, a05, a06).** Confidence is a separate, coupled estimate of the probability that the first-order decision was right, like judging another actor. The agent's own action is used as evidence. The model explains why confidence and accuracy come apart: extra noise in the confidence read-out, evidence that arrives after the decision, and evidence the decision could not reach (error-related negativity, blindsight). It predicts that new evidence after answering should update confidence. Simulation paper; no new large human dataset.

**Confidence versus certainty (Pouget, Drugowitsch and Kepecs 2016, a11, snippet only).** Confidence is the probability a choice is correct given the evidence and the choice. Certainty is the precision of the belief about the stimulus. They can come apart. Not opened.

**The Dunning-Kruger line (a24, b04, b05, K16).** Original claim: low scorers overestimate, top scorers slightly underestimate, because the skill to do the task is the skill to judge it. Magnus and Peresetsky (2022) show a noise-plus-censoring (tobit) model on bounded 0-100 scales reproduces the pattern with no psychological mechanism. The original paper was not opened. Status: contested. Do not use skill-linked overconfidence as a design premise.

**Calibration in neural nets (Guo et al. 2017, b11).** Modern nets are more miscalibrated than old ones. Temperature scaling (one parameter, fitted post hoc) beat other fixes on most datasets. Defines the binned ECE used in nearly all LLM work. ECE depends on binning.

**LLM era, 2022 to 2026.** In order: Kadavath 2022 (models mostly know what they know), Lin 2022 (words as calibrated confidence after fine-tuning), Tian 2023 and Xiong 2024 (prompted confidence for chat models), Kuhn 2023 (semantic entropy), Kapoor 2024 (must be taught), Steyvers 2025 (what readers do with it), Yoon 2025 (reasoning models), then 2025-2026 work on agents, tools, scales, stopping rules and change of mind. Details in sections 3, 5 and 6.

## 3. Core findings with exact numbers

Status key: Est = established (3 or more independent sources or strong design); Single = one source; Contested = sources disagree; Human = human-only.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Confidence has bias, sensitivity, efficiency; ECE alone hides discrimination | A constant 75% is perfectly calibrated with zero discrimination; AUROC2 = 0.5 at chance | a01, b02 (Fleming and Lau 2014) | Est (K01) |
| Raw verbalized LLM confidence is overconfident and weak at ranking | Average ECE above 0.377 (GPT-3, GPT-3.5, Vicuna); GPT-4 average AUROC 62.7%; +22.2% AUROC GPT-3 to GPT-4; 5 models, 8 tasks | c06, a17 (Xiong 2024) | Est (K02) |
| Low ECE can be gamed by accuracy | GPT-4 GSM8K: 93.6% accuracy, ECE 0.064 by saying 100% for everything | a18, b08 (Xiong) | Est (K03) |
| Sampling agreement lifts AUROC (older models, numeric tasks) | GSM8K AUROC 54.8% to 92.7% with 5 samples; cost 5-13 samples | b09, a18 (Xiong) | Est for older models; Contested for reasoning models (K04, K20) |
| Reasoning models: one stated confidence beats agreement at equal small k | Math AUROC: VC@1 71.3; SC@2 70.5 (math), 66.6 (STEM), 63.3 (humanities); SC@8 79.6 vs VC@8 81.4 | d01 (Del 2026) | Single (K19, K20) |
| Best use of a second sample is a hybrid | Math AUROC 71.3 to 84.2 (+12.9) at K=2; STEM 73.8 to 80.2; humanities 68.5 to 74.9; then +2.7 (K2 to K5) and about +1.5 (K5 to K8) | d02 (Del 2026) | Single (K19) |
| Confidence stated with the answer is about as good as a later judge pass | Math AUROC: elicitation 69.4-73.2; judge pass 67.6-73.8; epistemic-marker judge weakest (67.59/72.00/67.97) | d03 (Del 2026) | Single |
| Verbalized can beat token probability for RLHF chat models | TriviaQA ECE 0.140 label-prob vs 0.068 top-1 verbal vs 0.050 top-2; AUC 0.869 vs 0.879 vs 0.894; TruthfulQA AUC only 0.418 vs 0.485 | c08, a16 (Tian 2023) | Est (K06), tone differs from Xiong |
| White-box and black-box close | AUROC gap 0.522 to 0.605 (abstract range) | c07, a18 (Xiong) | Est |
| Fine-tuned confidence beats prompted | About 1000 graded examples enough, gains flatten near 5000; prompted ECE does not improve with base quality; best prompted trails worst fine-tuned (LLaMA-2 7B) | a19, b20, c09 (Kapoor 2024) | Est, training only (K05) |
| Pretrained models are calibrated on multiple choice in the right format | 52B scale; "none of the above" cuts accuracy and calibration a lot; RLHF policies fixed by a temperature | a12, a14, b06, b07 (Kadavath 2022) | Est (older models) |
| Fine-tuned words can be calibrated | CalibratedMath, 21 tasks; Multi-answer MSE about 22.0 vs constant 37.4; Multiply-divide about 10.4 vs 11.7 (about 1 point gain under shift) | c04, a15 (Lin 2022) | Single, old model |
| Users read LLM confidence badly | Model AUC .751/.746/.781 (GPT-3.5, PaLM2, GPT-4o); human AUC .589/.602/.592; 301 participants (284 retained) | a20, b14, c11 (Steyvers 2025) | Est (K07) |
| Longer explanations raise user confidence, not accuracy | BF = 25 for higher confidence; mean participant AUC .54 (long) vs .57 (uncertainty only) | b15, c12 | Est |
| Matching wording to model confidence narrows both gaps | Bayes factors above 100 (Exp 2a, 2c), 6.48 (2b) | c12, b14 | Est |
| First-person hedges change human readers | Agreement 80.9% control vs 74.8% "I'm not sure, but..." vs 77.6% impersonal (n.s.); confidence 3.95 vs 3.66 vs 3.80; N = 404 | d12 (Kim 2024) | Single, human reader (K24) |
| Deployed LMs rarely express doubt | 47% error rate among confident responses; users rely on output whatever the marking | b13 (Zhou 2024) | Single |
| Metacognitive information varies 2-fold across models; domain-specific | 1.98-fold, 4 open 7-9B models, 224,000 trials; rank link to accuracy -0.80 (TriviaQA), 0.00 (Natural Questions) after v3 re-score; weakest in Science and Technology for all four | c14, d13 (Cacioli 2026) | Est by critique rule (K08); preprint |
| Cacioli efficiency table (v3) | Llama-3-Base acc 0.478 / meta 0.300; Mistral-Instruct 0.560 / 0.206; Llama-3-Instruct 0.584 / 0.263; Gemma-2-Instruct 0.627 / 0.151 | d13 | Single |
| Scorer bug flipped a headline | v3 scorer missed 53% and 26% of two models' correct answers (1,200 adjudications) | d13 | Single (caution) |
| M-ratio steadier across tasks than AUC2 for 2 of 3 current models | GPT-5, DeepSeek-V3.2-Exp: M-ratio not significantly different across tasks; AUC2 tracks d' (rs = 0.9); Mistral-Medium differed by 0.13 and 0.20; all M-ratios above 0.5, suboptimal | d14 (Servajean 2026) | Single |
| 0-100 scale collapses onto a few values | Top 3 values hold 78.2% to 92.1% of answers; baseline M-ratio 0.62 (Qwen3-30B) to 0.92 (GPT-5.2); a 0-20 scale gave better efficiency | c15 (Dai and Wang 2026) | Est by critique rule (K09) |
| Coarse confidence can raise AUROC while ECE worsens | TriviaQA minus epistemic markers: ECE 0.042 to 0.109, AUROC 0.782 to 0.837 | b18, b19 (Yoon 2025) | Single (metric quirk) |
| Reasoning chains improve calibration (knowledge QA) | Reasoning beat non-reasoning in 33 of 36 settings; GLM-Z1 vs GLM-4: accuracy -0.07, ECE -0.037, AUROC +0.078 | b17 (Yoon 2025) | Contested (K10) |
| Which part of the chain matters | TriviaQA ECE/AUROC: original 0.042/0.782; minus confidence reasoning 0.063/0.763; minus epistemic markers 0.109/0.837; minus non-linear reasoning 0.161/0.734; no CoT 0.150/0.689 | b18 | Single |
| Reasoning models are overconfident, more so with depth | Verbalized confidence often above 85% even for wrong answers; introspection helps o3-mini and R1, hurts Claude 3.7 Sonnet | c22 (Mei 2025) | Single |
| Reasoning confidence sits on a few high values | Under 5% of responses below 0.5; 70-90% of responses on fewer than 7 values | d06 (Wang 2026) | Single |
| Verbalized confidence ignores the trace (VLMs) | Within 0.02 before and after a hesitation in 78.5% (Qwen3-VL) and 49.0% (VL-Calibration) | d18 (Yang 2026) | Single |
| Longer thinking can worsen calibration | ClimateX: reasoning models 48.7%, non-reasoning 45.0%, search-augmented 89.3% | d05 (Lacombe 2025) | Single, indirect task |
| Tiny-data drift claim | 47 questions, 574 of 1,368 valid responses; 70B inconclusive | d04 | Not usable |
| Calibration training lowers ECE, not reliably AUROC | OOD: ECE 46.94 to 25.49 while AUROC 65.71 to 61.20; CalibSFT over 16 benchmarks ECE 23.41 to 12.49, AUROC 70.49 to 73.95; another setting ECE 23.8-25.8% down to 7.8-14.2% while AUROC fell | d06 | Est (K21) |
| Calibration-aware RL in tool agents | ECE up to 68% lower; SimpleQA: Qwen2.5-3B ECE 0.213 to 0.175, AUROC 0.659 to 0.823; Qwen2.5-7B ECE 0.204 to 0.176, AUROC 0.831 to 0.790; Qwen3-4B ECE 0.140 to 0.034, AUROC 0.825 to 0.765 | c20, d09 (Xuan 2026) | Single, needs RL |
| Tools: search vs code | Search raises mean confidence on incorrect; code interpreter reduces miscalibration; MATH-500 Qwen2.5-3B: direct 63.4, prompted tools 48.6, RL tools 77.0 | c20, d09 | Contested (K14) |
| Beyond binary rewards (RLCR) | Correctness-only RL worsens calibration; Brier term fixes it; ECE 0.37 (HotpotQA) and 0.26 (math) drop in domain | c21 (Damani 2026) | Single, training |
| Post-hoc recalibration is model-dependent | Partial OOD gains for Qwen2.5-7B and Mistral-7B; none significant for Llama 3.1 8B; Platt better on small held-out sets | d17 (Abbasli 2026) | Single (K22) |
| Luo and Jho's headline is against an uncalibrated baseline | Fine-tuned Llama-3-8B ECE 0.224; base after temperature scaling ECE 0.107 (n = 250 held out) | a23 | Single (read with care) |
| Choice-supportive bias | Change of mind 32.5% (answer hidden) vs 13.1% (shown), coefficient -3.4, p < 0.0001; with opposing advice 85.0% hidden vs 39.2% shown; opposing advice weighted 2.58x Bayes, supporting 1.095x | a22, b23, c16 (Kumaran 2025) | Est (K11) |
| The bias vanishes for another LLM's answer | 31.3% hidden vs 33.2% shown, n.s. | d10 | Single |
| Debate inflates confidence | 60 debates, 10 models: 72.9% initial vs rational 50%; final about 83%; both sides at least 75% in 61.7%; identical copies 64.1% to 75.2%; told chance is 50%, still 50.0% to 57.1% | c17 (Prasad and Nguyen 2025) | Single |
| Intrinsic self-correction hurts | GPT-3.5 CommonSenseQA 75.8 to 38.1 (3 calls), 41.8 (5 calls); GPT-4 GSM8K 95.5 to 91.5 to 89.0; oracle labels: GPT-4 GSM8K 97.5 | b24, c25 (Huang 2024) | Single (K12) |
| Confidence-gated retries save cost | BrowseComp: BrowseConf-Zero 41.3 acc / 5.67 attempts vs self-consistency (10) 36.7 / 10; BrowseComp-zh 59.2 / 3.43 vs 59.9 / 10 (no gain) | c19 (Ou 2025) | Single design, part of K13 |
| Agent confidence is overconfident but ranks | Accuracy near zero below 70% confidence; best bin 90-94% only 53.33% accurate; 30.0 reported vs 30.49 reproduced | c18 | Single |
| Adaptive stopping | CAS up to 12.33x budget saving vs majority vote N = 64; 5.19 vs 12.87 samples vs Adaptive-Consistency; untrained Qwen2.5VL-7B AUROC 0.578, ECE 0.386. CGES 16.0 to 6.7 calls (58% fewer) within 0.4 points | d07, d08 | Est (K13); none on ARC or BrainTeaser |
| Agents are overconfident about their own success | All tested LLMs overconfident; overconfidence grows over multi-step tasks | c23 (Barkan 2025) | Single |
| Trajectory-level confidence beats last-step | GPQA baseline ECE 0.41-0.45; SimpleQA HTC ECE 0.077, AUROC 0.69; HLE ECE stays about 0.43 | c24 (Zhang 2026) | Single |
| Semantic entropy beats other uncertainty scores | AUROC roughly 0.68 to 0.80 on TriviaQA, CoQA (read from plots) | b12 (Kuhn 2023) | Single |
| Models know some unanswerables | SelfAware F1: GPT-4 75.47% vs human 84.93% | c26 (Yin 2023) | Single |
| SelfCheckGPT | Sentence-level AUC-PR non-factual 72.96 (random) to 83.21 | c27 (Manakul 2023) | Single |
| P(True) self-judgment | Keeping P(True) > 0.5 answers raises accuracy on all five tasks; works better with several of its own samples shown; zero-shot poorly calibrated | a13, b06, c02 (Kadavath) | Est (older models) |
| Human M-ratio test-retest is poor | r = .168 (50 trials), .235 (100), .293 (200), .422 (400); split-half above .837 at 100 trials; 1,091 subjects, 7 datasets, 17 measures | d16 (Rahnev 2024) | Est, human (K23) |
| Non-normalised measures depend on difficulty | Cohen's d of difficulty effect: meta-d' 2.41, AUC2 2.24, gamma 2.64, phi 1.53, conf 1.80; M-ratio significant in 1 of 4 datasets | d16 | Est, human |
| Distractors and "none of the above" | NOTA lowers accuracy and calibration; distractors can cut ECE up to 90% (best case, abstract only) | a12, b22 (Chhikara 2025) | Contested (K18) |

## 4. Mechanisms and models

Written so an engineer can build them.

**4.1 Measuring confidence quality (the base layer).**
Given N items, each with correct (0/1) and stated confidence c:
- Bias: mean(c) minus mean(correct).
- ECE: bin c into M bins (Guo uses equal-width; Kadavath used 10 equal-mass bins); ECE = sum over bins of (n_bin/N) * |acc_bin - conf_bin|.
- Brier: mean((c - correct)^2).
- AUROC2: probability that a random correct item has higher c than a random wrong item (ties count half). Use rank-based code. 0.5 is chance.
- M-ratio (only for two-choice tasks with ordinal ratings): fit meta-d' with HMeta-d or the Maniscalco-Lau maximum-likelihood fit; M-ratio = meta-d'/d'. Needs hundreds of trials (section 5, Rahnev).
- Rule: report bias, ECE, Brier and AUROC2 together on a fixed item set. Reject any change that improves ECE with flat or lower AUROC (K21, K03).
- Selective-prediction gain: accuracy among answers kept when the lowest-confidence share is dropped. Cacioli found metacognitive information tracked this gain (rho +1.00, n = 4 models, anecdotal).

**4.2 Second-order confidence (Fleming and Daw).**
Treat confidence as a separate estimator z = P(my answer is right | evidence I have, the answer I gave). Implementation sketch: after the answer is produced, run a separate judge call that sees the task and the answer and returns a number. The post-decision variant lets new evidence in (X_conf = X_act + X_new). In an agent this is a re-check step that adds new information (a code run, a held-out example) before the confidence is read. Without new information, a re-read of the same trace adds only read-out noise. The Del 2026 judge-pass result (d03) is consistent: a second pass over the same trace did not clearly beat confidence given with the answer.

**4.3 Verbalized confidence elicitation (prompt-only recipes).**
- Single number with the answer, asked in the same call (Del: as good as a later judge pass, d03).
- Top-k guesses with a probability each, then confidence (Tian "consider the opposite"; top-2 ECE 0.050 vs top-1 0.068, c08).
- Human-inspired prompts (self-probe, step-by-step, top-k) lower ECE but leave AUROC near chance on older models (c07, a18).
- Scale: use a 0-10 or 0-20 scale or a five-level verbal scale. On 0-100 three values carry up to 92.1% of answers (c15). How much AUROC moves for current models is untested (gap 9).
- Parse the number in code; never let the model's tone count.

**4.4 Sample-agreement confidence.**
Draw k answers in separate contexts, cluster equivalent answers in code, set confidence = share of the largest cluster. Semantic entropy (Kuhn, b12) uses meaning clusters rather than strings. Hybrid score SCVC (Del, d02): combine agreement with the stated confidence of each run. A simple version: score(answer) = mean stated confidence of the runs that gave that answer, times agreement share. The exact mix used in the paper is not reproduced here; test a product against a weighted sum. Caveat: samples from one model are not independent (schema G4), so agreement is a hint.

**4.5 Confidence-gated stopping and retry (BrowseConf style).**
Loop: attempt, read confidence, stop if confidence >= threshold, else retry up to a cap; carry a short summary of failed attempts (c19). Threshold choice matters: too strict adds cost without gain. BrowseConf-Zero used 5.67 attempts on average. CGES uses a Bayesian stopping rule on per-sample token confidence (d08). CAS uses RL-trained confidence (d07). For a prompt-only agent the open question is whether the stated number is a good enough gate on our task types.

**4.6 Temperature or Platt recalibration.**
Fit a one-parameter map from stated confidence to observed accuracy on a dev set; apply at run time. Platt (logistic) is better when the set is small (d17). Refit per domain and test on another domain first, because gains are model-dependent (K22). Recalibration changes ECE only. A monotone map keeps the ranking, so it cannot change AUROC.

**4.7 Choice-supportive bias control.**
Mask the agent's own earlier answer in the review step, or attribute it to "another solver". Kumaran's measure: change-of-mind rate with the answer hidden vs shown (d10). Masking is consistent with schema S3 (fresh context, no other attempt shown) and G5 (judge sees no authorship). Untested: whether masking raises final accuracy.

**4.8 Trajectory-level confidence for agents.**
Features from the whole run (number of tool calls, retries, hesitations, step confidences) fed to a small interpretable model fitted on a labelled set (Zhang 2026, c24). Needs labels per agent. Useful only after enough logged runs exist (schema section 6 and S9 logs).

**4.9 Output wording for readers.**
For a human reader, a first-person hedge ("I'm not sure, but...") reduced agreement and raised the reader's accuracy (d12). Matching explanation wording to model confidence narrowed the calibration and discrimination gaps (c12). For a downstream model step, a number is easier to parse; no study tests the wording on a model reader.

## 5. What holds up

**Held up.**
- Three-way split of confidence and the need for AUROC next to ECE (K01, K03). Many sources agree.
- Raw prompted verbalized confidence from LLMs is overconfident and mediocre at ranking, in three independent studies on older models (Xiong, Kapoor, Zhou; K02). Reasoning models still bunch on a few high values (d06, K10).
- Fine-tuned confidence beats prompted (K05). Not usable by a scaffold with no training.
- Calibration fixes that lower ECE do not reliably raise AUROC, and can lower it out of domain (d06, d09, K21).
- Choice-supportive bias in LLMs: three model families, large effect (32.5% vs 13.1%), absent for another model's answer (K11).
- Users misread LLM confidence; explanation length inflates trust (K07).
- Confidence-gated stopping saves cost at near-equal accuracy in QA, math and search (K13): 58% fewer calls (CGES), 12.33x budget (CAS), 5.67 vs 10 attempts (BrowseConf).

**Failed or contradicted.**
- Dunning-Kruger as a psychological law: a statistical account reproduces it (b04). Contested.
- Intrinsic self-correction: no gain, often loss (b24). One main source with a strong design; matches schema 4b and G2.
- Calibration training as a free win: ECE gains with AUROC loss (d06, d09).
- Search tools as an overconfidence cause: Xuan says yes; Lacombe finds retrieval helps on a different task (K14). No replication.
- Human M-ratio as a stable trait: test-retest r = .17 to .42 across 50 to 400 trials (d16). The human "general metacognition factor" (Mazancieux, 5 of 6 correlations) is not matched in LLMs (d13, d14).
- P(IK) out of domain: the authors say the model "struggles with calibration of P(IK) on new tasks" (c03).
- Tiny-sample drift claims (d04) are not usable.

**Moderators and boundary conditions.**
- Answer type: consistency lifts AUROC strongly on numeric answers (54.8 to 92.7 on GSM8K) and weakly on open-ended MMLU (Kapoor). This resolves one contradiction in the critique.
- Model type: verbalized beats token probability for RLHF chat models (Tian); white-box and black-box are close (Xiong); prompted methods do not improve with model quality (Kapoor). These agree only if limited to chat models and prompted-vs-prompted comparisons.
- Reasoning vs non-reasoning: Yoon finds better calibration; Mei and Lacombe find overconfidence grows with depth; Wang finds bunching on a few values. Different metrics, tasks and ablations.
- Domain: efficiency weakest in Science and Technology for all four models (d13); hybrid gains strongest in math (d02).
- Format: calibration depends on options being visible; "none of the above" lowers accuracy and calibration (a12).
- Scale: coarse values lift AUROC and hurt ECE (b19).
- Gate type: CAS and CGES gates use RL-trained or token-level confidence; BrowseConf is verbalized but gave no gain on BrowseComp-zh.
- Measure: AUROC2 tracks accuracy (rs = 0.9 with d'); M-ratio may reverse the ordering (d14). Human non-normalised measures depend on difficulty (Cohen's d 1.5-2.6).
- Trials: M-ratio is unreliable below 200 trials in humans (r = .168 at 50).

**Interventions that worked.**
- Fine-tuning on about 1000 graded answers (needs training).
- Temperature scaling for RLHF-model ECE (a14, b10).
- A second sample mixed into the stated confidence (+12.9 AUROC in math, one source).
- Confidence-gated retry (BrowseComp) and early stopping.
- Masking the earlier answer or attributing it to another model (removes the bias).
- Matching explanation wording to confidence (human readers).
- A 0-20 scale over 0-100 (Dai and Wang).

**Interventions that did not work.**
- Human-inspired prompts for failure prediction on older models (AUROC near chance).
- Unaided self-correction.
- Judge passes over the same trace (no clear gain, d03).
- Telling debaters the true chance (confidence still rose 50.0% to 57.1%).
- Treating high verbalized confidence as safe: the 90-94% bin was 53.33% accurate on BrowseComp.

**Caution on tooling.** The Cacioli preprint changed its headline between v1 and v3 because a scorer missed 53% and 26% of two models' correct answers. Automatic scorers can flip conclusions in LLM metacognition work. Check the scorer on a hand-checked sample before trusting any confidence result.

## 6. Language models

**Base behaviour.** GPT-3, GPT-3.5, Vicuna: average ECE above 0.377. GPT-4: average AUROC 62.7% on eight tasks (c06). GPT-4 GSM8K ECE 0.064 came from saying 100% to everything (K03). Deployed LMs had a 47% error rate among confident responses (b13). Reasoning models put 70-90% of confidences on fewer than 7 values and give under 5% below 0.5 (d06). Search agents: accuracy near zero below 70% confidence, but the 90-94% bin only 53.33% accurate (c18). All tested agents overestimate their own task success, worse as the task goes on (c23).

**What changed it, and by how much.**

| Change | Effect | Needs training? | Source |
|---|---|---|---|
| RLHF chat model, verbal instead of token probability | TriviaQA ECE 0.140 to 0.068 (top-1) to 0.050 (top-2) | no | c08 |
| Model scale GPT-3 to GPT-4 | +22.2% AUROC | no | c06 |
| 5 samples agreement (GSM8K, older models) | AUROC 54.8 to 92.7 | no | b09 |
| Reasoning model vs non-reasoning (GLM-Z1 vs GLM-4) | ECE -0.037, AUROC +0.078 | no | b17 |
| Remove non-linear reasoning from the chain | AUROC 0.782 to 0.734, ECE 0.042 to 0.161 | no | b18 |
| No CoT | ECE 0.150, AUROC 0.689 | no | b18 |
| Second sample mixed in (K=2, math) | AUROC 71.3 to 84.2 | no | d02 |
| Fine-tune on about 1000 graded answers | beats prompts in ECE and AUROC | yes | c09 |
| Fine-tune with Brier term (RLCR) | ECE 0.37 (HotpotQA) and 0.26 (math) fall sharply in domain | yes | c21 |
| CalibSFT, 16 benchmarks | ECE 23.41 to 12.49, AUROC 70.49 to 73.95 | yes | d06 |
| Calibration RL, tool agents | ECE up to 68% lower, AUROC mixed | yes | d09 |
| Wording match, human readers | AUC gap narrows (BF above 100) | no | c12 |
| 0-20 scale vs 0-100 | better M-ratio in tested models | no | c15 |
| Show own answer in review | change of mind 32.5% to 13.1% | no | a22 |
| Attribute visible answer to another LLM | 31.3% vs 33.2%, bias gone | no | d10 |
| Confidence-gated retry | 41.3 vs 36.7 accuracy, 5.67 vs 10 attempts | no | c19 |
| CGES early stop | 16.0 to 6.7 calls, within 0.4 points | no (token probabilities) | d08 |
| Intrinsic self-correction | GPT-3.5 CSQA 75.8 to 38.1 | no | b24 |
| Longer thinking (ClimateX) | accuracy falls with budget | no | d05 |

**Metacognitive efficiency.** Four 7-9B open models differed 1.98-fold in metacognitive information; baseline M-ratio of six current LLMs ranged 0.62 (Qwen3-30B) to 0.92 (GPT-5.2) (c14, c15). Three current models all had M-ratio above 0.5 and below optimal (d14). Temperature changed accuracy but left metacognitive information near flat for three of four models (c14).

**Self-knowledge of unanswerables.** GPT-4 F1 75.47% vs human 84.93% on SelfAware (c26). A medical benchmark found frontier models confident when wrong (a25, snippet only).

**Interaction effects.** Debate pushes confidence up, not down (72.9% to about 83%, c17). Visible earlier answers freeze the model (a22). Opposing advice is overweighted 2.58x vs Bayes; supporting advice 1.095x. So a critic step inside the same context can swing the answer for reasons unrelated to evidence.

**Gap in the evidence.** No study isolates confidence asked before vs after reasoning at equal tokens (K10 contested). No study measures AUROC or confidence-gating on ARC grids or BrainTeaser puzzles (K25). Most older results are GPT-3.5, GPT-4, Llama-2. The current-model sources are mid-size open models (Del, three models), preprints, and single authors.

## 7. What our agent should take

Schema parts: G (guardrail), S (state), O (operator), memory (SCHEMA section 5). Status: [E] established, [S] single-source, [C] contested.

### Add now (established)

1. **Measure confidence on the agent with AUROC and ECE together, never ECE alone.** Part G (G7). [E] K01, K03; a01, b02, a18, b08. A calibration change only counts if AUROC holds or improves on a held-out domain (K21; d06, d09).
2. **Do not read a stated percentage as a probability.** Treat it as a weak rank signal. Part G. [E] K02; c06, a17, b13. Reinforces SCHEMA 4b ("verbal confidence to stop").
3. **Do not plan on prompted-method gains that need training.** Fine-tuned or RL-calibrated confidence is out of scope for the scaffold. Part G. [E] K05; c09, b20, a19.
4. **Do not accept a better ECE with a flat AUROC.** Part G. [E] K21, K03; d06, b19.
5. **Never show a revise or judge step its own earlier answer as its own.** Mask it or attribute it to another solver. Part S3/S5 and G5. [E] for the bias, K11; a22, b23, c16, d10. The accuracy effect of masking is unmeasured, so this only formalises current behaviour (fresh contexts, no authorship). Low cost.
6. **Keep intrinsic self-correction out; revise only from real output.** Part G2. [S] K12 (single source, but matches the existing [E] in schema F07/F11/F12); b24, c25.
7. **Use confidence only to decide whether to spend a further attempt, never to submit or abstain.** Part S (stop/continue), G6, G12. [E] for cost saving in other domains, K13; c19, d07, d08. No gate was tested on ARC or BrainTeaser and two of three studies use trained or token-level confidence, so ship only after test T3. It never overrides G6.
8. **Hedged wording for human-facing final answers is low-risk.** Part G (output, S9). [S] K24; d12, c12. Not a schema rule until tested; recorded for human-facing mode only.

### Test first

1. **Hybrid score: one stated confidence plus one extra sample's agreement (K19).** Part G/S7. [S] d01, d02. Test T2.
2. **Confidence before reasoning vs after vs after a backtrack pass, at equal tokens (K10).** Part S. [C] b17, b18, d03, d05, d06, d18. Test T1.
3. **Confidence-gated second attempt on ARC and BrainTeaser (K13, K25).** Part S6/G12. [S] for our tasks. Test T3.
4. **Scale choice: 0-10, five-level verbal, 0-100 (K09).** Part G. [E] on the collapse, untested on AUROC for current models. Test T4.
5. **Per-domain recalibration map vs none (K22).** Part G/memory. [S] d17. Test T5.
6. **Post-answer evidence step before reading confidence (K17).** Part S4/S8. [S] a05, a06. Test T6.
7. **Masking effect on revise accuracy (K11).** Part S5. Test T7.
8. **Per-domain AUROC profile stored in memory so S0 can pick the mode (K08, K15).** Part memory. [C]. Test T8.
9. **Tool type vs calibration: search vs code (K14).** [C]. Test T9.
10. **Wording for a model reader (K24).** [S]. Test T10.
11. **Top-2 guesses with probabilities (Tian).** Part G. [E] on RLHF chat models, AUC gain small (0.879 to 0.894). Test T11.

Links to other subfields in this run (not covered here): Learned termination, Surprisingly popular method, Falsificationism, Consensus and premature agreement, Learned refinement and self-verification, Metacognitive knowledge (declarative, procedural, conditional), Active inference decision theory.

## 8. Concrete tests on our bench

All arms get the same total tokens (setup, sampling, judge calls and retries counted, G7). Fixed seeds, same item set per test. Report AUROC, ECE, Brier, accuracy and tokens per item. Use at least 200 items per arm for AUROC. M-ratio needs 400 two-choice trials and is optional.

| ID | Item type | Arms (equal tokens) | Metric | Expected effect |
|---|---|---|---|---|
| T1 | BrainTeaser and ARC items with known answers | A: confidence before reasoning. B: reasoning, then confidence in the same call. C: reasoning, backtrack pass, then confidence | AUROC, ECE | B above A by about +0.03 to +0.05 AUROC (Yoon 0.689 vs 0.782 on TriviaQA); C no better than B (d03) |
| T2 | Same items, current backbone | A: 1 run + stated confidence, rest of tokens on a longer single run. B: 2 runs, score = confidence mixed with agreement. C: 5 runs, majority share | AUROC, accuracy of top-confidence half | B above A and C per token; +6 to +13 AUROC in math (d02), likely smaller on puzzles |
| T3 | ARC and BrainTeaser | A: fixed n=3 independent attempts, vote. B: attempt, retry only if confidence below threshold (cap 3). C: fixed n=2. Equal mean tokens | Accuracy at equal tokens, attempts per item | B saves 20-50% of attempts within 1 point of A; if not, no gate |
| T4 | Items from T1 | Scales: 0-100, 0-10, five-level verbal mapped to 0-4 | AUROC, number of distinct values used | 0-10 or verbal raises AUROC a few points; ECE may worsen (b19) |
| T5 | Two domains, fit on one, test on the other | A: raw confidence. B: Platt map fit on the dev domain. C: map refit per domain | ECE, AUROC | B helps ECE only in domain; C needed; AUROC unchanged by design |
| T6 | Code-checkable items (ARC with held-out examples) | A: confidence read before checks. B: confidence read after running the unfitted test (S4) | AUROC | B above A by 0.10 or more, since the check is real evidence (a05) |
| T7 | Revise-step items where the first answer is sometimes wrong | A: revise step sees own earlier answer. B: sees it masked or as "another solver". C: no revise | Final accuracy, switch rate | B above A by 2-5 points if the bias costs accuracy; null possible |
| T8 | Mixed-domain pool, 5+ domains | Per-domain AUROC profile from a dev set, tested on a fresh set | Spearman rank stability of per-domain AUROC across splits | Stable (rho above 0.6) means S0 can use the profile (c14, d14) |
| T9 | Questions answerable by search and by code | A: search tool. B: code tool. C: neither | Mean confidence on incorrect, AUROC | Search raises confidence on incorrect (d09); replicate or refute |
| T10 | Answers passed to a second model that must accept or reject | A: bare answer. B: numeric confidence. C: first-person hedge | Reader AUROC and accuracy | B and C above A; hedge vs number unknown |
| T11 | Chat backbone, factual items | A: single answer + confidence. B: top-2 answers with probabilities, then confidence | ECE, AUROC | ECE lower by about a third; AUROC +0.01 to +0.02 (c08) |

Controls for all tests: hand-check the scorer on a sample (Cacioli lesson); report per-domain results; do not tune thresholds on the test set; log tokens per stage.

## 9. What does not transfer, and why

- **Human metacognition measures need many two-choice trials.** M-ratio on 50 trials had test-retest r = .168 (d16). Our items are open-ended; M-ratio is not well defined there (c28 note). Use AUROC and state the limits.
- **Brain-structure results (Fleming 2010).** About human anterior PFC. No agent analogue. The useful part is that sensitivity is separable from accuracy (r = -0.11).
- **Cross-task human g factor (Mazancieux).** Not supported in LLMs: efficiency is domain-specific (d13) and only partly stable (d14).
- **Dunning-Kruger.** Statistical account; do not build on it.
- **Calibration training and calibration RL.** Strong results, but need training (c09, c21, d06, d09). The scaffold cannot use them.
- **P(IK) heads and probes.** Need weights or labelled data (c03, a19).
- **Token-probability gates (CGES, CAS).** Need open weights or reward models. A prompt-only API agent may lack token probabilities.
- **BrowseComp and QA gains.** Long search tasks, not ARC grids or BrainTeaser riddles. Savings may not carry to short puzzles with a code check, where the check is the better stopper (G1, G3).
- **Older-model numbers.** Xiong, Tian, Kadavath and Huang used GPT-3.5/4, Llama-2 or 52B models. Current reasoning models bunch on a few values (d06) and behave differently under sampling (d01).
- **Debate confidence inflation.** Zero-sum debate; schema already forbids debate (G9).
- **Human readers' hedging effects.** Human trust is not model trust (d12). A model reader may just parse the number.
- **Search overconfidence (Xuan).** Pilot on a 3B model with a local Wikipedia retriever (d09); not shown for frontier models.

## 10. Open questions

1. Does confidence asked before vs after reasoning differ at equal tokens for current reasoning models? (K10, gap 1)
2. At equal tokens, where does k-sample agreement overtake one answer plus confidence? None found up to K=8 (d01).
3. Does a stated-confidence gate beat fixed-n resampling on puzzle tasks that have a code check?
4. Does masking the earlier answer raise revise-step accuracy? Bias is shown, effect on accuracy is not (d10). The AAAI-25 paper on memory-driven choice-supportive bias was seen only as a snippet (d11).
5. Which wording of stated confidence helps a model reader? Only a human study exists (d12).
6. Is there a domain-general LLM metacognition factor? Current evidence says no, from three tasks and three models (d14).
7. Is the tool dichotomy (search overconfidence, code calibration) real? One paper, small models, plus an opposite-direction result on a different task (d05, d09).
8. Does scale granularity change AUROC on current models? Only the collapse onto three values is shown (c15).
9. Do small-dev-set temperature maps persist out of domain? (a23, d17)
10. What do Maniscalco and Lau 2012 and Koriat 1997 report exactly, and has the 2010 brain-structure result been replicated at scale? Neither paper could be opened (403).
11. Would the trajectory-level features (Zhang 2026) transfer to a scaffolded agent with no training?
12. Is the 53.33% accuracy of the 90-94% bin on BrowseComp typical for other agent benchmarks?

## 11. Sources

[V] = opened and read; [M] = snippet or abstract only.

- [V] Fleming and Lau (2014) How to measure metacognition. https://pmc.ncbi.nlm.nih.gov/articles/PMC4097944/ (also https://doi.org/10.3389/fnhum.2014.00443)
- [V] Fleming (2017) HMeta-d. https://www.biorxiv.org/content/10.1101/068601v2.full
- [V] Fleming and Daw (2017) Self-evaluation of decision-making. https://pmc.ncbi.nlm.nih.gov/articles/PMC5178868/
- [V] Fleming, Weil, Nagy, Dolan and Rees (2010) Science. https://pmc.ncbi.nlm.nih.gov/articles/PMC3173849/
- [M] Nelson and Narens (1990) Metamemory. https://doi.org/10.1016/S0079-7421(08)60053-5
- [M] Koriat (1997) Cue-utilization. https://doi.org/10.1037/0096-3445.126.4.349
- [M] Maniscalco and Lau (2012) meta-d'. https://doi.org/10.1016/j.concog.2011.09.021 (page returned 403: https://www.sciencedirect.com/science/article/pii/S1053810011002248)
- [M] Pouget, Drugowitsch and Kepecs (2016) Confidence and certainty. https://doi.org/10.1038/nn.4240
- [M] Dunning and Kruger (1999) Unskilled and unaware of it. https://doi.org/10.1037/0022-3514.77.6.1121
- [V] Magnus and Peresetsky (2022) A statistical explanation of the Dunning-Kruger effect. https://pmc.ncbi.nlm.nih.gov/articles/PMC8992690/
- [V] Mazancieux et al. (2020) Is there a G factor for metacognition? https://pmc.ncbi.nlm.nih.gov/articles/PMC7397761/
- [V] Rahnev (2024) Measuring metacognition: A comprehensive assessment of current methods. https://rahnevlab.gatech.edu/documents/papers/Rahnev_2024.pdf
- [M] Rahnev et al. (2020) The Confidence Database. https://pmc.ncbi.nlm.nih.gov/articles/PMC7565481/
- [V] Guo et al. (2017) On calibration of modern neural networks. https://arxiv.org/abs/1706.04599
- [V] Kadavath et al. (2022) Language models (mostly) know what they know. https://arxiv.org/abs/2207.05221
- [V] Lin, Hilton and Evans (2022) Teaching models to express their uncertainty in words. https://arxiv.org/abs/2205.14334
- [V] Tian et al. (2023) Just ask for calibration. https://arxiv.org/abs/2305.14975
- [V] Xiong et al. (2024) Can LLMs express their uncertainty? https://arxiv.org/abs/2306.13063
- [V] Kuhn, Gal and Farquhar (2023) Semantic uncertainty. https://arxiv.org/abs/2302.09664
- [V] Kapoor et al. (2024) LLMs must be taught to know what they don't know. https://arxiv.org/abs/2406.08391
- [V] Zhou, Jurafsky and Hashimoto (2024) Relying on the unreliable. https://arxiv.org/abs/2401.06730
- [V] Steyvers et al. (2025) What LLMs know and what people think they know. https://arxiv.org/abs/2401.13835
- [V] Steyvers and Peters (2025) Metacognition and uncertainty communication. https://arxiv.org/abs/2504.14045
- [V] Kim et al. (2024) I'm not sure, but... https://arxiv.org/abs/2405.00623
- [V] Yoon et al. (2025) Reasoning models better express their confidence. https://arxiv.org/abs/2505.14489
- [V] Mei et al. (2025) Reasoning about uncertainty. https://arxiv.org/abs/2506.18183
- [M] Chhikara (2025) Mind the confidence gap (abstract numbers only). https://arxiv.org/abs/2502.11028
- [V] Kumaran, Fleming et al. (2025) Overconfidence in initial choices and underconfidence under criticism. https://arxiv.org/abs/2507.03120
- [M] AAAI-25 memory-driven choice-supportive bias in LLM agents. https://ojs.aaai.org/index.php/AAAI/article/view/34843/36998
- [V] Prasad and Nguyen (2025) When two LLMs debate, both think they'll win. https://arxiv.org/abs/2505.19184
- [V] Huang et al. (2024) LLMs cannot self-correct reasoning yet. https://arxiv.org/abs/2310.01798
- [V] Yin et al. (2023) SelfAware. https://arxiv.org/abs/2305.18153
- [V] Manakul, Liusie and Gales (2023) SelfCheckGPT. https://arxiv.org/abs/2303.08896
- [V] Ou et al. (2025) BrowseConf. https://arxiv.org/abs/2510.23458
- [V] Xuan et al. (2026) The Confidence Dichotomy. https://arxiv.org/abs/2601.07264
- [V] Damani et al. (2026) Beyond binary rewards (RLCR). https://arxiv.org/abs/2507.16806
- [V] Barkan et al. (2025) Do LLMs know what they are capable of? https://arxiv.org/abs/2512.24661
- [V] Zhang et al. (2026) Agentic confidence calibration. https://arxiv.org/abs/2601.15778
- [V] Cacioli (2026) Do LLMs know what they know? (v3). https://arxiv.org/abs/2603.25112
- [V] Dai and Wang (2026) Beyond 0-100. https://arxiv.org/abs/2603.09309
- [V] Servajean and Servajean (2026) Measuring (some aspects of) the metacognition of AI. https://arxiv.org/abs/2603.29693
- [V] Del et al. (2026) How uncertainty estimation scales with sampling in reasoning models. https://arxiv.org/abs/2603.19118
- [V] Hiremath and Hiremath (2026) Calibration drift under reasoning. https://arxiv.org/abs/2606.11211
- [V] Lacombe, Wu and Dilworth (2025) Don't think twice. https://arxiv.org/abs/2508.15050
- [V] Wang et al. (2026) Pitfalls of verbalized confidence priors. https://arxiv.org/abs/2609.32470
- [V] Yang et al. (2026) Scaling with confidence (C3RL, CAS). https://arxiv.org/abs/2607.01612
- [V] Aghazadeh et al. (2026) CGES. https://arxiv.org/abs/2511.02603
- [V] Abbasli et al. (2026) Comparing uncertainty measurement and mitigation methods. https://arxiv.org/abs/2504.18346
- [V] Yang et al. (2026) The mirage of calibrated confidence (VLMs). https://arxiv.org/abs/2609.18453
- [V] Luo and Jho (2026) Predictive metacognition. https://pmc.ncbi.nlm.nih.gov/articles/PMC13434765/
- [M] Griot et al. (2025) LLMs lack essential metacognition for reliable medical reasoning. https://doi.org/10.1038/s41467-024-55628-6
