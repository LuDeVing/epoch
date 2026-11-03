# Confidence and metacognition: deep document

*Subfield B02.10. Focus: reading one's own certainty. Key works: Fleming. Why it matters for our agent: use sample consistency, not self-report (SCHEMA 4b). Evidence ids (a01 to d19) and claim ids (B02.10-K01 to K27) refer to the jsonl files in this folder. Numbers were re-opened in critique.md unless marked otherwise.*

## 1. What it is

Confidence is a system's estimate of how likely its own answer is to be right. Metacognition is the wider skill: watching and judging one's own thinking. This document uses "confidence" in the narrow sense: a number or a signal that should go up when the answer is right and down when it is wrong.

Three quantities must be kept apart (a01, a02, a03, c17):

- **Bias (calibration).** Do claims of 70% come true 70% of the time? Over- and under-confidence live here. Measured by ECE or calibration curves. Needs many trials per bin.
- **Sensitivity (discrimination).** Does confidence separate right from wrong trials? Measured by the type 2 ROC area (AUROC2; in LLM papers just "AUROC" or "AUC"). A system can be calibrated overall and still have no sensitivity: a constant 50% on a coin-flip task has perfect ECE (c06).
- **Efficiency.** Sensitivity after correcting for task performance: meta-d'/d'. 1 is ideal. 0.7 means 30% of the decision evidence is lost when judging confidence (a01).

Why it matters for the agent. The agent must decide, many times per task, whether to stop, revise, sample more, run a check, or hand over. Each is a decision about its own certainty. The question for this subfield: which certainty signal is worth reading? The evidence gives a clear ranking for 2022 to 2024 models (agreement beats self-report), a partly reversed ranking for 2026 reasoning models (a single verbalized number is competitive, and a mix is best), and one rule that stays stable: an external check beats every internal signal.

Position in the schema. SCHEMA 4b says "Using a model's verbal confidence to stop" is not to be added (F09, F07). G4 says agreement is a hint, never proof. G10 says reasoning text is not evidence. This document adds exact numbers behind those lines and finds one place where the 4b wording should be softened (section 7).

Links to other subfields (not covered here): Chain-of-thought prompting; Learned termination; Learned refinement and self-verification; Metacognition models; Metacognitive knowledge; Good Judgment Project; Bayesian models of cognition; Surprisingly popular method; Pruning of decision trees; Debiasing by structure.

## 2. History and theories in depth

**Signal detection frame (background, not in the evidence files).** The modern frame is signal detection theory. A type 1 task is the decision (left or right). A type 2 task is "was I right?", scored with a type 2 ROC. Galvin et al. (2003) showed the type 2 AUROC depends on type 1 sensitivity d' and on the type 1 criterion (a02). So raw type 2 AUROC is not a clean measure of metacognitive skill.

**Fleming and Lau (2014) (a01, a02, a03).** This review fixed the vocabulary above and promoted meta-d': the d' an ideal observer would need to produce the observed confidence ratings. Efficiency is meta-d'/d'. It makes people with different task accuracy comparable. Phi (Pearson r between accuracy and confidence) is another measure.

**Fleming et al. (2010), the founding study (a04, a05, b01, b02).** N=32 healthy adults did a visual two-choice task. A staircase held accuracy near 71% (range 70 to 74%). They rated confidence 1 to 6. Metacognitive ability (A_roc) ranged 0.55 to 0.75. It did not correlate with task accuracy (r=-0.11, p=0.56) and was reliable within person (split-half r=0.69, p=0.00001). Grey matter volume in right anterior prefrontal cortex (BA10, peak [24,65,18], tmax=4.8, p<0.05 corrected) predicted A_roc but not d' (r=0.15, p=0.42) and not overall confidence bias (r=-0.023, p=0.90). A negative correlation appeared in left inferior temporal gyrus (tmax=4.66). Left aPFC did not survive correction. Message: knowing how well you know is a trait apart from how well you do. Limits: one lab, one visual task, small N; the dissociation rests on non-significant correlations in N=32.

**Neural code in animals (a06).** Kiani and Shadlen (2009): monkeys saw random-dot motion and could opt out for a small sure reward. Opt-out rate tracked difficulty. Parietal LIP neurons that carry the decision variable also carried certainty (70 neurons from two monkeys in the population average; 19 with a sure-bet target in the receptive field). A three-parameter model fit the choices. Confidence can be read from the same evidence accumulation that drives the choice.

**Confidence as probability (a07, snippet only).** Meyniel, Sigman and Mainen (2015) frame confidence as the Bayesian probability of being correct given the evidence. Not opened.

**Second-order models (a08, a09).** Fleming and Daw (2017): confidence is a second-order inference. A separate system judges the first, like judging another actor. The model uses one's own action as evidence, so confidence can be biased by what was chosen. It accounts for confidence and error detection together, and for cases where metacognition is better or worse than task performance. Simulations only. The choice-supportive bias found in LLMs (Kumaran, Fleming et al. 2025, a25) tests this prediction in models.

**Domain generality (b03, b04, d17, d18).**
- Mazancieux et al. (2020), N=181, four two-choice tasks (episodic memory, semantic memory, executive function, visual perception): 5 of 6 cross-task correlations in meta-d'/d' significant. Accuracy correlations across tasks r=-0.08 to 0.25. Efficiency higher for the two memory tasks.
- Rahnev and Fleming (2019), reanalysis of N=31: staircases that vary difficulty inflate every common measure. All-contrast vs 1-contrast type-2 AUC +0.034, t(30)=3.18, p=0.003, d=0.57; meta-d' minus d' difference 0.253, d=0.63; 3-contrast vs all-contrast d>0.66 on every measure. First-order d' did not differ (F(2,60)=0.71, p=0.49).
- Fleming, Ryu, Golfinopoulos and Rees (2014), lesion study: aPFC lesion n=7, temporal lesion n=11, healthy n=19. Perceptual meta-d'/d' group effect F(2,34)=5.78, p=0.007; aPFC below controls t(24)=3.67, p=0.001. Memory group effect F(2,34)=0.75, p=0.48. Group by domain interaction p=0.010. The aPFC role is causal but domain-specific.
- Molenberghs et al. (2016), N=308 fMRI (abstract only): better metacognitive accuracy goes with lower anterior medial PFC activation. A different measure from grey matter volume. No direct large-N structural replication of the 2010 finding was found.

**Field state (b05).** Rahnev et al. (2022), a consensus of 26 researchers: few confidence findings have been independently replicated, and effect sizes for factors affecting confidence are rarely compared.

**Clinical angle (a10).** Rollwage, Dolan and Fleming (2018): people with radical beliefs showed lower metacognitive sensitivity on a neutral perceptual task and smaller confidence updates after disconfirming evidence. Study 1 n=344, study 2 n=381, study 3 n=417 replicated key findings. Post-decision evidence set to 80% performance. Questionnaire-defined, correlational, US online samples.

**Calibration in machine learning (a11).** Guo et al. (2017): modern deep nets are overconfident; temperature scaling (one parameter fitted on held-out data) fixes most of it. Example ECE 12.67 before, 0.96 to 2.46 after; typical ECE 4 to 10% before. Closed-class classification on a fixed distribution.

**The LLM line, 2022 to 2026.**
1. 2022: base models know what they know in the right format (Kadavath; a12, a13, b06 to b09, c01 to c03). Finetuned verbal confidence works (Lin; a14, b25, c04, c05).
2. 2022 to 2023: sample agreement as a confidence signal (Wang self-consistency; a15, b26, c10. Kuhn semantic entropy; a21, b20, c11).
3. 2023 to 2024: RLHF chat models, black-box elicitation. Tian (a17, b15, b16, c06): verbalized beats token probability. Xiong (a18 to a20, b10 to b14, c07 to c09): verbalized confidence barely discriminates; agreement is far better. Kapoor (a22, b17 to b19, c18): prompting is not enough; about 1000 graded examples fix it.
4. 2023 to 2025: self-correction and human trust. Huang (c13, c14): intrinsic self-correction hurts. Steyvers (a23, b23, b24, c16, c17) and Zhou (c15): people over-trust confident-sounding text.
5. 2024 to 2025: introspection. Binder (c19), Anthropic (c20), Ji-An (a26).
6. 2025 to 2026: reasoning models and agents. Yoon (b21, b22), Mei (d03), Del (d01, d02), Kaddour (d09, d10), Cacioli (d04), CISC and DeepConf (c21, c23), long-output and agent work (d06, d15, d16).

## 3. Core findings with exact numbers

Status: established = 2 or more independent sources; single = one paper; contested = sources point different ways.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Bias, sensitivity, efficiency are different; raw AUROC depends on task difficulty | Efficiency = meta-d'/d'; 0.7 means 30% of evidence lost | Fleming and Lau 2014 (a01 to a03, c17) | established (K01) |
| Human introspective accuracy is a stable trait apart from task accuracy | N=32; A_roc 0.55 to 0.75; accuracy 70 to 74%; r with accuracy -0.11; split-half r=0.69 | Fleming 2010 (a04, b01) | single sample (K02) |
| aPFC grey matter predicts it | BA10 peak [24,65,18], tmax=4.8, p<0.05 corr.; vs d' r=0.15; vs bias r=-0.023 | Fleming 2010 (a05, b02) | single; later work says domain-specific (d17, d18) |
| aPFC role is causal but domain-specific | lesion n=7: perceptual p=0.007, memory p=0.48, interaction p=0.010 | Fleming 2014 (d17) | single, small N |
| Metacognitive efficiency partly general across tasks | N=181; 5 of 6 cross-task correlations significant | Mazancieux 2020 (b03) | established with b04 (K03) |
| Staircase procedure inflates every measure | N=31; AUC +0.034, d=0.57; meta-d'-d' +0.253, d=0.63 | Rahnev and Fleming 2019 (b04) | single reanalysis (K03) |
| Radical beliefs go with low sensitivity and small updates | n=344, 381, 417 | Rollwage 2018 (a10) | single group, replicated in paper (K17) |
| Neural confidence in monkeys | 70 LIP neurons, 2 monkeys | Kiani and Shadlen 2009 (a06) | single lab (K18) |
| Deep nets overconfident; temperature scaling fixes it | ECE 12.67 to 0.96-2.46 | Guo 2017 (a11) | established for classifiers |
| Large base LMs calibrated on lettered multiple choice; P(True) with own samples; P(IK) | 52B P(IK) AUROC/Brier 0.864/0.151 (Lambada), 0.928/0.194 (Python), 0.606/0.431 (worst); RLHF fix T=2.5 | Kadavath 2022 (a12, a13, b06 to b09, c01 to c03) | single source, base models (K09) |
| Finetuned verbalized confidence generalises | Multi-answer MSE 22.0 vs constant 37.4; multiply-divide 10.4 vs 11.7 | Lin 2022 (a14, b25, c04) | established with Kapoor (K11) |
| Prompting alone does not calibrate; ~1000 graded examples do | LLaMA-2 7B/13B, Mistral 7B; best prompted lags worst finetuned; user study N=181 | Kapoor 2024 (a22, b17 to b19, c18) | established with Lin (K11) |
| Verbalized beats token probability for RLHF models on trivia | gpt-3.5 TriviaQA ECE 0.140 to 0.054 (top-4), AUC 0.869 to 0.896; SciQ ECE 0.256 to 0.065 | Tian 2023 (a17, b15, c06) | single (K10) |
| ... but not on adversarial misconception items | TruthfulQA token AUC 0.418, entropy AUC 0.236; verbalized 0.455 to 0.55 | Tian 2023 (b16) | single (K10) |
| Vanilla verbalized confidence discriminates weakly | GPT-4 mean AUROC 62.7% (chance 50); weaker models ECE >0.377; GPT-3 to GPT-4 about +22.2% AUROC; values cluster 80 to 100% | Xiong 2024 (a18, b10, b14, c07) | single (K04) |
| Low ECE can hide zero discrimination | GPT-4 GSM8K 93.6% accuracy, ECE 0.064 by saying 100% | Xiong 2024 (a19, b11, c09) | single (K05) |
| Agreement across samples beats one stated number (2023 models) | GSM8K AUROC 54.8% (Top-K, M=1, GPT-3.5) to 92.7% (M=5 consistency); Prompt (M=5) avg AUROC 73.0, ECE 18.7; saturates M=1 to 13; law/strategy only ~60 to 66 | Xiong 2024 (a20, b12, c08) | contested (K06) |
| Semantic entropy beats counting distinct answers | AUROC 0.83 vs 0.79 TriviaQA; 0.77 vs 0.66 CoQA; distinct meanings wrong vs right 3.89 vs 1.89, 1.77 vs 1.27 | Kuhn 2023 (a21, b20, c11) | single, mid-size open model (K06) |
| Self-consistency raises accuracy | GSM8K +17.9% (best model), LaMDA-137B 17.1 to 27.7 (+10.6); imperfect prompt greedy 17.1 to 14.9, 40 paths 23.4; SVAMP +11.0, AQuA +12.2 | Wang 2022 (a15, b26, c10) | established (K07) |
| SC accuracy grows with samples | GPT-3.5 GSM8K standard 76.7; SC 82.5/85.3/88.2 at 3/6/9 | Huang 2024 (c14) | established (K07) |
| Confidence-weighted voting saves samples | CISC over 40% fewer paths; P(True) SC needs 18.6 samples to match CISC at 10 (46%); 9 models, 4 datasets | Taubenfeld 2025 (c21) | established (K08) |
| Adaptive stopping on answer counts | up to 7.9x fewer samples, accuracy drop <0.1%; 17 datasets, 3 LLMs | Aggarwal 2023 (c22) | established (K08) |
| Token-confidence filtering | GPT-OSS-120B AIME 2025 99.9% vs 97.0% majority vs 91.8% pass@1; up to 84.7% fewer tokens | Fu 2025 DeepConf (c23) | established (K08); needs logprobs |
| Bayesian early stopping with a scalar confidence | calls 16.0 to 6.7 (-58%), accuracy within 0.4 points | Aghazadeh 2026 CGES (d07) | single; needs logprobs or reward model (K24) |
| Reasoning models: one verbalized confidence beats SC at equal samples | VC@1 AUROC 78.8 math, 73.8 STEM, 68.5 humanities; SC@2 70.5 math vs VC@2 73.5; VC math 71.3 (K=1) to 81.4 (K=8) | Del 2026 (d01) | single, 3 models (K19, K06) |
| Hybrid VC plus SC | up to +12 AUROC at K=2 (+12.9 math, +6.4 STEM/humanities); saturates near K=5 outside math | Del 2026 (d02) | single (K19) |
| In small open models SC beats VC | probe 0.95; SC 0.82; VC 0.67; CCS 0.72; text classifier 0.59; 65% of wrong traces confident | Yuan 2026 (d05) | single (K06, K27) |
| Reasoning models better calibrated than non-reasoning | 33 of 36 settings; TriviaQA ECE 0.042 vs 0.150 no-CoT vs 0.161 no non-linear reasoning; NonambigQA AUROC 0.749 vs 0.618 | Yoon 2025 (b21, b22) | contested (K12) |
| Reasoning models still overconfident on wrong answers | wrong-answer confidence often >85%; o3-Mini ECE +7 points low to high effort, Claude +2 | Mei 2025 (d03) | single (K20) |
| Confidence quality varies by domain | 33 models, 1,500 MMLU items, 47,151 obs; AUROC .498 to .806; Applied/Professional .742, Formal Reasoning .658, Natural Science .652; median CI width .199 | Cacioli 2026 (d04) | single (K21) |
| Coding agents near chance on own success | true 22 to 35%, predicted up to 77%; AUROC 0.51 to 0.64 with CIs including 0.5; 100 SWE-Bench Pro tasks | Kaddour 2026 (d09) | single (K22) |
| Execution clustering gates answers | LiveCodeBench returned-answer error 65% to 2%; 0% error at 15.6% coverage; 2% error at 36.8% | Ravuri 2025 (d11) | single, older models (K22) |
| Bug-finding review framing helps | overconfident-failure 72% to 45%; Claude AUROC 0.55 to 0.64; Gemini 0.51 to 0.57; GPT unchanged 0.55 | Kaddour 2026 (d10) | single (K23) |
| Intrinsic self-correction, 2023 models | GPT-3.5 CSQA 75.8 to 38.1 to 41.8; GPT-4 GSM8K 95.5 to 91.5 to 89.0; GPT-4 CSQA 82.0 to 79.5 to 80.0 | Huang 2024 (c13) | contested (K13) |
| Intrinsic self-correction, 2026 models | SAT: Haiku 75.64 to 93.59; Mistral 34.62 to 64.96; Gemini Pro 97.00 to 100; avg 65.66% of errors removed; BBEH non-choice Mistral 17.04 to 25.67; correct answers flipped up to 13.25% on open reasoning | Stav 2026 (d08) | contested (K13) |
| Choice-supportive bias in LLMs | change of mind 32.5% (answer hidden) vs 13.1% (shown), coeff -3.4, p<0.0001; opposite-advice weight -0.58 shown vs -0.41 hidden; overweight ratios 0.77/0.92/0.96 at advice accuracy 50/60/70% | Kumaran 2025 (a25) | single (K14) |
| Multi-turn self-anchoring drift is model-specific | Sonnet 4.6 drift -0.032, t(14)=-2.43, p=.029, d=-0.627; ECE drift F(4,56)=22.77 | Harshavardhan 2026 (d12) | single, 15 items per cell (K14, K23) |
| Humans over-trust confident-sounding LLM text | human AUC .589/.602/.592 vs model .751/.746/.781; long vs short explanation BF=25 | Steyvers 2025 (a23, b23, b24) | established with Zhou (K15) |
| Deployed LLMs rarely hedge | 47% error among confident answers; uncertainty phrases 5.02% of rejected vs 4.47% of chosen alignment texts | Zhou 2024 (c15) | established (K15) |
| Wording does not track internal confidence | cMFG 0.52 to 0.57 vs 0.5 chance, 5 models; best prompted 0.70, 0.63 | Yona 2024 (d13) | single (K25) |
| Models do not act on stated confidence | confidence flat as penalty rises 0 to 100; almost never abstain | Wang 2026 (d14) | single (K25) |
| Self-prediction beats cross-prediction | Llama-3-70B 48.5% vs GPT-4o 31.8% (+17 points absolute) | Binder 2024 (c19) | contested (K16) |
| Injected-concept introspection | about 20% detection at best layer, 0 false positives in 100 trials in production models | Anthropic 2025 (c20) | contested (K16) |
| Long-output confidence collapses at atomic level | usable at line level; logit-based beat verbalized (p<0.05); 50+ LLMs | Amit 2026 (d15) | single (K26) |
| Claim-level semantic entropy | Llama-3.1-8B +15.3% AUROC over semantic entropy; DeepSeek-V3.1 +5.21% | Zhao 2026 SeSE (d16) | single (K26) |
| Per-step agreement saves calls in an agent loop | TrACE-4 matches SC-4 with 33% (GSM8K n=50) and 39% (n=30 tasks x 3 seeds) fewer calls; TrACE-8 55% and 65% fewer | Sethi 2026 (d06) | single, 3B model (K24, K26) |

**Corrections to carry (critique.md).** "+17.9%" is the best model in Wang; LaMDA is +10.6. In Xiong, 54.8% to 92.7% is GSM8K, GPT-3.5, Top-K (M=1) versus M=5 consistency. The 62.7% is a GPT-4 mean over datasets. Do not mix them. The earlier "88.6 to 92.7" start point was not found; treat as wrong. Binder's "+17%" is absolute points. The "about 83" debate figure in c14 was not re-checked. Kuhn's model identity was not re-opened; the entropy numbers are from a mid-size open model, not a frontier chat model.

## 4. Mechanisms and models

Each item is written so it can be coded.

**4.1 Metrics (the measurement layer; build this first).**
- Log per item: correct (0/1), the confidence signal(s), task type, difficulty bin, tokens spent.
- Discrimination: AUROC of signal vs correct. Compute with a rank formula (probability a random correct item has higher signal than a random wrong one; ties count half). Report a bootstrap CI. Cacioli's median cell CI width is .199 (d04), so 100 items per cell gives wide intervals; pool across cells for decisions.
- Calibration: ECE with 10 bins, plus the share of items at the modal confidence value. Flag the signal as degenerate if one value holds more than 80% of items (the GPT-4 GSM8K case: ECE 0.064 with constant 100%, a19).
- Efficiency (optional): meta-d'/d' needs a type 1 d' and a hit/false-alarm model; for LLMs the papers opened used plain AUC (c17). Substitute: compare AUROC within matched difficulty bins (Rahnev and Fleming's staircase warning, b04).
- Selective prediction curve: sort items by signal, plot accuracy against coverage (as in Ravuri: 0% error at 15.6% coverage, d11). This is the decision-relevant plot for abstain/escalate rules.

**4.2 Signals the agent can compute, with black-box cost.**
1. *Verbalized confidence (VC).* One extra sentence: "give a probability 0 to 100 that your answer is correct". 1 sample. Vanilla GPT-4 AUROC 62.7% (a18); frontier reasoning models 78.8 math, 73.8 STEM, 68.5 humanities (d01). Variants that help: ask for the top 4 guesses first, then confidence (Tian: AUC 0.879 to 0.896, a17); show the model its own samples before it rates one (Kadavath P(True), b08).
2. *Answer agreement (SC).* Draw K independent samples, each in a fresh context. Agreement = share of samples whose normalised final answer equals the modal answer. Cost K times. Xiong GSM8K AUROC 92.7% at M=5 for GPT-3.5 (b12). Gain saturates M=1 to 13. For frontier reasoning models SC@2 trails VC@2 (d01) and gains saturate near K=5 outside math (d02).
3. *Semantic agreement.* When answers are free text, cluster samples by bidirectional entailment (needs a judge model or small NLI model) and take entropy over clusters (Kuhn, c11). Gain over distinct-count is modest (+0.04 to +0.11 AUROC). Greedy decoding gives no signal; sample at temperature.
4. *Hybrid VC plus agreement.* Score = w * VC + (1 - w) * agreement. Del: +12 AUROC at K=2 (d02). The weight was tuned on their data, so tune w on our own held-out items.
5. *Token-probability confidence.* Needs logprobs. DeepConf slides a window over the chain, drops weak traces early, weights votes by confidence (c23). CGES uses it for Bayesian stopping (d07). Not available on every API.
6. *External check.* Run the code, the unit test, the verifier. The only strong gate found (d11: 65% to 2% error; d08: checkable constraints removed 65.66% of errors). Not a confidence signal; a ground-truth signal, with its own coverage limits.
7. *Hidden-state probe.* AUROC 0.95 vs VC 0.67 (d05). Needs weights. Not for a black-box agent (K27).

**4.3 Stopping rules (how the signals are used).**
- Fixed K voting: draw K, take the mode. Accuracy rises with K (82.5/85.3/88.2 at 3/6/9, c14).
- Adaptive-Consistency (c22): after each sample, compute the probability that the current leader stays the leader given counts so far (a Dirichlet or Beta posterior); stop when it exceeds a threshold. Up to 7.9x fewer samples, under 0.1% accuracy loss. Failure: early samples agreeing on a wrong answer.
- Confidence-weighted vote (CISC, c21): weight each sample by its own confidence (P(True) or VC), softmax with a temperature. Over 40% fewer paths. Standard calibration metrics did not predict who benefits, so test per model.
- Per-step agreement (TrACE, d06): at each agent step sample several next actions; if agreement is at or above a threshold (0.8 in the paper), take the action and spend nothing more; otherwise sample more. 33 to 65% fewer calls at equal accuracy in a 3B model.
- Selective answering (Ravuri, d11): score = mass of the largest behaviour cluster; answer only above threshold.

**4.4 Review and revise gates.**
- Revise only on a signal (G1, G2). The signal should be an external failure first, a low agreement score second, a low VC third.
- Do not show the reviewer its own earlier answer where an independent re-solve is possible. Kumaran: change-of-mind 32.5% hidden vs 13.1% shown (a25). Not isolated in an agent loop (gap 4).
- Frame review as bug-finding: overconfident-failure 72% to 45% (d10).
- Allow intrinsic revise only where constraints are checkable by reading (SAT-like). On open reasoning, up to 13.25% of correct answers get flipped (d08).

**4.5 Calibration memory.** Keep a small table per coarse task type and per model: n, accuracy, AUROC of each signal, best threshold. Cacioli (d04) shows the profile moves by domain and cells are noisy, so use 4 coarse types and refit on a model change. A table that fails split-half stability must not be used.

**4.6 Thresholds live in code.** Models do not use their own confidence to abstain, even when penalties make it optimal (d14), and their hedging words do not track internal certainty (d13). So the scaffold reads the number or agreement, and code applies the threshold (G5).

## 5. What holds up

**Holds up (two or more independent sources, or replicated).**
- Sensitivity, bias and efficiency are separate, and raw AUROC moves with difficulty (a01, a02, b04, c17). Report AUROC and ECE separately.
- More samples raise accuracy, with a knee. Wang +10.6 to +17.9; Huang 82.5/85.3/88.2 at 3/6/9; saturation in Xiong between M=1 and 13 (a15, c14, b12).
- Confidence-weighted voting and adaptive stopping cut cost at equal accuracy: CISC over 40%, Adaptive-Consistency up to 7.9x, DeepConf up to 84.7% tokens, CGES 58% (c21, c22, c23, d07). Three of four independent of each other.
- Finetuning on graded examples calibrates; prompting alone does not (Lin, Kapoor). Not usable for a black-box agent, but it tells us a per-task calibration log is the right substitute.
- People over-trust confident LLM text, and rewriting wording to match true confidence narrows the gap (Steyvers, Zhou).
- An external check beats internal signals (d11, d08, d09).

**Replications and failed or partial replications.**
- Fleming 2010 BA10: no direct large-N structural replication found. Lesion work (n=7) supports a causal but domain-specific role (d17). An N=308 fMRI study found a prefrontal link as an activation decrease, a different measure (d18, abstract only). Treat as partly supported, small N.
- Cross-task generality: partly supported (5 of 6 correlations, N=181, b03). Earlier null results are attributed in that paper to low reliability.
- Rollwage 2018 replicated within the paper across three samples (a10); no outside replication collected.
- Xiong's "agreement beats self-report" did NOT hold for 2026 reasoning models in Del (VC@2 73.5 vs SC@2 70.5 on math; d01), but did hold in small open models (SC 0.82 vs VC 0.67, d05). Ordering depends on model class and on how verbalized confidence is elicited (a 1-to-5 scale in d05 vs a probability).
- Huang's "self-correction hurts" held for 2023 models. For 2026 models it holds only on open reasoning; checkable constraint tasks gain strongly (d08).
- Yoon (reasoning improves calibration, 33 of 36 settings) vs Xiong (CoT leaves confidence at 80 to 100%): the likely difference is whether the chain revises itself (ablation: remove non-linear reasoning, ECE 0.042 to 0.161). But Mei finds reasoning models overconfident on wrong answers and more so at high effort (o3-Mini +7 ECE), and Amit finds reasoning raises accuracy but lowers confidence ranking quality on long outputs (d15). Contested.
- Introspection: Binder +17 points absolute and Anthropic about 20% detection, versus failure on long outputs and prompted confidence lagging. Self-prediction of short behaviours works; judging a long solution does not.

**Moderators.**
- Model class: base, RLHF chat, reasoning.
- Task: arithmetic with one checkable answer gives the biggest agreement gain; law, ethics and strategy give AUROC about 60 to 66 for all methods (a20, a18).
- Adversarial items: on TruthfulQA, token confidence is below chance (AUC 0.418, entropy 0.236, b16). Common misconceptions are shared by all samples, so agreement also fails (shared systematic errors, b26, c08).
- Format: lettered multiple choice calibrates; "none of the above" hurts (c01).
- Domain: AUROC .742 vs .652 inside one model set (d04).
- Output length: atomic-claim ranking collapses; line-level works (d15).
- Elicitation scale: the 1-to-5 scale used in d05 may depress VC.

**Interventions that worked.**
Top-K guesses before confidence (Tian); showing own samples before P(True) (Kadavath); few-shot (Kadavath); temperature scaling (Guo; T=2.5 for RLHF policies, b07); finetune on about 1000 graded examples (Kapoor); hybrid VC plus SC (d02); bug-finding framing (d10); execution clustering (d11); matching explanation wording to true confidence for human readers (b24).

**Interventions that did not.**
"Be careful" prompts and human-inspired prompts beyond modest gains (c09); plain CoT for discrimination (a19); intrinsic self-correction on open reasoning (c13, d08); debate over matched-budget sampling (c14); prompting for hedges (d13); asking the model to abstain under penalty (d14); a self-review pass (helps some models, hurts others, d19); more reasoning effort (raises overconfidence on wrong answers, d03 though d19 is thin: 574 valid responses of 1,368 calls).

## 6. Language models

**Base models, 2022 (Kadavath).** 52B models were well calibrated on lettered multiple choice and true/false. Calibration improved with size and few-shot. P(True) was near 50% and poorly calibrated zero-shot; showing 5 of its own samples at T=1 improved it a lot, and filtering to P(True)>0.5 raised accuracy on all five tasks. P(IK) AUROC 0.864 (Lambada), 0.928 (Python), 0.606 (worst). It breaks out of distribution. RLHF policies looked miscalibrated, fixed largely by T=2.5.

**Finetuned verbalized confidence (Lin 2022; Kapoor 2024).** GPT-3 trained on add-subtract was calibrated on multiply-divide and multi-answer (MSE 22.0 vs 37.4 constant). About 1000 graded examples with LoRA gave better ECE and AUROC than any prompt on LLaMA-2 and Mistral. Estimators transferred across models (Mistral 7B on LLaMA-2 7B beat LLaMA-2 on itself). Part of the learned skill is question difficulty (training on wrong answers only still did well). In a user study (N=181) people tracked calibrated scores and ignored random ones.

**RLHF chat models, 2023 to 2024.**
- Tian: verbalized confidence beat token probability on TriviaQA and SciQ; ECE halved or better. On TruthfulQA both failed.
- Xiong: GPT-4 vanilla AUROC 62.7%, weaker models ECE above 0.377, confidences in 80 to 100% in multiples of 5. White-box vs best black-box AUROC 0.522 vs 0.605. Best aggregation lowered ECE to 0.028. GPT-3 to GPT-4 about +22.2% AUROC.
- Agreement: GPT-3.5 GSM8K 54.8% to 92.7% AUROC. Semantic entropy 0.83 TriviaQA, 0.77 CoQA.
- Zhou: 47% error among confident answers. Yona: hedge wording cMFG 0.52 to 0.57, near the 0.5 random baseline.
- Huang: intrinsic self-correction lowered accuracy (GPT-3.5 CSQA 75.8 to 38.1; GPT-4 GSM8K 95.5 to 89.0). GPT-3.5 keeps its GSM8K answer 74.7% of the time.
- Bias: Gemma 3, GPT-4o and o1-preview change their mind 32.5% of the time when their earlier answer is hidden and only 13.1% when shown, and overweight opposing advice (Kumaran).

**Reasoning models, 2025 to 2026.**
- Yoon: 6 reasoning models, 6 datasets, better calibrated in 33 of 36 settings. GLM-Z1 was 0.07 less accurate than GLM-4 on NonambigQA yet 0.037 lower ECE and 0.078 higher AUROC. Calibration improves as the chain unfolds. Removing slow thinking (backtracking, alternatives) hurt most (TriviaQA ECE 0.042 to 0.161); explicit reasoning about confidence mattered little. Non-reasoning models improved when guided to slow-think in context.
- Mei: o3-Mini, R1, Claude 3.7 Sonnet and Gemini remain overconfident, over 85% on many wrong answers; ECE correlates negatively with accuracy (Claude r=-0.69); o3-Mini ECE +7 points from low to high effort.
- Del: VC@1 AUROC 78.8 math; SC@2 below VC@2; hybrid +12 AUROC at K=2; VC math 71.3 to 81.4 from K=1 to 8 (+10.1), +4.6 STEM, +4.1 humanities.
- Cacioli: 33 models; Opus 4.6 AUROC .806; Gemma 3 1B .498 (chance). Profile shape varies even within Anthropic generations.
- Kaddour: coding agents predict success up to 77% where truth is 22%; AUROC 0.51 to 0.64. Not seeing the patch (pre-execution) discriminated at least as well as seeing it.
- Stav: revise helps on SAT (65.66% of errors removed) and BBEH non-choice (Mistral 17.04 to 25.67) but flips correct answers up to 13.25% on open reasoning.
- Wang 2026: models keep answering when abstaining is optimal.
- Yuan: probe AUROC 0.95, 0.79 from the first reasoning step; 65% of wrong traces carry high stated confidence and a high internal error score. The signal could not be used to repair errors.

**What changed the numbers, by how much (summary).**
| Change | Effect |
|---|---|
| Add 4 more samples and aggregate (2023) | GSM8K AUROC +37.9 points (54.8 to 92.7) |
| Hybrid VC plus SC at K=2 (2026) | up to +12 AUROC |
| Top-4 guesses before confidence | TriviaQA ECE 0.068 to 0.054, AUC 0.879 to 0.896 |
| Finetune 1000 graded examples | beats best prompt on ECE and AUROC |
| Bug-finding framing | overconfident failures 72% to 45% |
| Hide own earlier answer | change of mind 13.1% to 32.5% |
| Execution clustering | error 65% to 2% |
| Confidence-weighted vote | over 40% fewer paths |
| Adaptive stopping | up to 7.9x fewer samples |
| Reasoning chain that revises | TriviaQA ECE 0.150 to 0.042 |
| Raise reasoning effort | o3-Mini ECE +7 points |

**Caveats.** Almost all LLM numbers are from 2022 to 2024 models (GPT-3.5, LLaMA-2, 52B Anthropic). Frontier reasoning evidence is thin (Yoon, Del, Mei, DeepConf, Cacioli). Several 2026 results are single-author preprints with small n for agents (d06 n=30 to 50; d12 15 items per cell; d19 574 valid responses).

## 7. What our agent should take

Status: [E] established, [S] single-source, [C] contested. Schema part: G guardrail, S state, O operator, M memory.

### Add now (established)

1. **Report discrimination and calibration separately, always.** AUROC and ECE per signal, with a degenerate-signal flag. Schema: G (reporting), S9 log. [E] K01, K05. Evidence a01, a02, a03, c17, b11. Note: K05 is single-source, K01 is established; the rule costs nothing.
2. **Never use the model's stated confidence alone to stop, accept, or skip a check.** Keep 4b wording but add the numbers: vanilla GPT-4 AUROC 62.7%, coding agents AUROC 0.51 to 0.64, models do not act on their own confidence. Schema: G10, 4b. [E] across Xiong, Zhou, Kaddour, Wang 2026, Yona (K04, K15, K22, K25). Evidence a18, c15, d09, d13, d14.
3. **Agreement among independent samples is a usable hint, never proof.** Already G4. New numbers: shared systematic errors mean wrong answers can agree (b26, c08); on adversarial misconception items confidence ranking is below chance (b16). Schema: G4, S3, S4. [E] K07. Evidence a15, b12, c14, b26.
4. **Stop sampling by answer counts, not on a schedule.** Adaptive-Consistency style rule: stop when the leader is a safe majority. Up to 7.9x fewer samples, accuracy drop below 0.1%. Needs no logprobs. Schema: O (stop rule), G12 (spend by difficulty). [E] K08. Evidence c22, c21, c23.
5. **Prefer the external check to any internal signal.** Run tests; use confidence only to decide how much extra sampling to buy when no check exists. Schema: G2, G3, S4, S8. [E] K22 partly (single on agents, but G2 and G3 already established). Evidence d11, d08, d09.
6. **Thresholds are set in code on measured signals, not by asking the model whether to abstain.** Schema: G5, G6. [E] K25 (two sources, d13, d14) plus G5. Note: G6 still holds: never abstain on first pass; the signal chooses extra work, not refusal.
7. **Humans reading the output need calibrated wording.** If the final answer is shown to a person, tie the hedging to measured agreement, not to the model's tone. Schema: G (output hedging). [E] K15. Evidence a23, b24, c15.
8. **Keep a per-task-type calibration table in memory, coarse and per model, after a split-half stability check.** Schema: M class record (already holds agreement record). [E] for the need (K11, K21 single for the shape). Evidence d04, a22.
9. **Soften one line in 4b.** The rule "using a model's verbal confidence to stop" stays, but the reason should read: "stated certainty alone discriminates weakly (AUROC about 63% for GPT-4 vanilla; 0.51 to 0.64 for coding agents); for 2026 reasoning models it is moderate (about 69 to 79) and works best combined with 2 sample agreement". [E]/[C] on the second half. Do not flip the rule until U1 passes.

### Test first

1. **VC, agreement and hybrid as the trigger for S5/S6 and for extra sampling, on our bench.** [C] K06, K19. Evidence d01, d02, d05, b12. See U1.
2. **Confidence-weighted vote vs plain vote at fixed token budget.** [E] in the literature (CISC, DeepConf) but with logprobs or P(True); black-box VC weighting untested. K08, K24. See U2.
3. **Hide the earlier answer in S8 verify / review.** [S] K14, K23. Evidence a25, d10, d12. See U3.
4. **Bug-finding framing for review.** [S] K23. Evidence d10. See U4.
5. **Per-step agreement (TrACE-style) as a compute allocator inside the loop.** [S] K24, K26. Evidence d06. See U5.
6. **Revise-without-new-evidence only on checkable-constraint tasks.** [C] K13. Evidence c13, d08. See U6.
7. **Gate S0 mode choice on a pre-answer confidence ("will I get this right?").** [S] K09 (P(IK)), K22 (agents near chance). Evidence b09, d09. See U7.
8. **Low-confidence-after-contrary-evidence update check.** [S] K17. Evidence a10. See U10.
9. **Calibration table stability across task types.** [S] K21. See U8.
10. **Line-level confidence for long outputs.** [S] K26. See U9.

## 8. Concrete tests on our bench

All arms get the same total tokens. Report AUROC with bootstrap CI, ECE, selective accuracy at 50% and 80% coverage, and accuracy at equal tokens. Use at least 100 items per domain; with the cell CI width .199 from Cacioli (d04), differences below about 0.05 AUROC cannot be resolved at 100 items.

| Test | Item type | Arms (equal tokens) | Metric | Expected effect |
|---|---|---|---|---|
| T1 Signal ranking | 100 items each: math (exact answer), short factual, open-ended, code with tests | (a) VC@1; (b) SC agreement K=5; (c) hybrid, VC plus agreement K=2 (w tuned on a split); (d) hybrid K=5 | AUROC vs correctness; accuracy at 80% coverage | Hybrid K=2 beats VC@1 by about +6 to +12 AUROC (Del). SC alone loses to VC at K=2 for reasoning models; wins for small models |
| T2 Weighted vs plain vote | Math and short factual, hard subset where plain accuracy is 30 to 70% | plain majority K; VC-weighted vote K; adaptive stop on counts K_max; each capped at same tokens | accuracy at equal tokens; tokens to reach plain-K accuracy | Weighted vote saves 20 to 40% of samples (CISC over 40%); adaptive stop saves more, loss under 1 point |
| T3 Hide own answer | Items where first attempt is wrong 30 to 50% of the time, with a verify state | verify with own answer shown; verify by independent re-solve with answer hidden, compare in code; same token budget | error rate of final answer; change-of-mind rate; rate of correct-to-wrong flips | Hidden arm: more changes of mind (13% to 32% in Kumaran) and fewer anchored errors; measure whether net accuracy rises |
| T4 Review framing | Code repair or short proofs with known bugs | neutral review; bug-finding review; no-patch pre-review | overconfident-failure rate; AUROC | Failure rate 72% to 45%; AUROC +0.05 to +0.09 for Claude-like models (d10) |
| T5 Step agreement | Multi-step agent tasks (tool use, grids) | fixed K samples every step; adaptive K by per-step agreement threshold 0.8; plain single sample | task success; calls per task | 30 to 60% fewer calls at equal success (d06, 3B model; frontier may differ) |
| T6 Revise gate | Two item sets: constraint-checkable (SAT-like, formal rules) and open reasoning | no revise; blind revise; revise only with a located failing output (G2); sample-and-vote at the same tokens | accuracy; correct-to-wrong flips | Blind revise: big gain on constraint set (d08, up to +30 points for weak models), up to 13% flips on open set; located-failure revise and sampling safest |
| T7 Pre-answer self-forecast | 100 tasks per type | S0 forecast "success probability" before work; post-work VC; agreement | AUROC of each; cost saved by routing | Forecast near chance for agents (0.51 to 0.64); useful only if AUROC >= 0.70 |
| T8 Check-versus-confidence pricing | Code or math with cheap verifier | (a) always check; (b) check only if confidence below t; (c) never check | accuracy per token | Fills gap 3: expect (b) wins only when check cost exceeds about the cost of K=2 agreement |
| T9 Table stability | 4 coarse task types, two halves | build table on half A; test calibration on half B | split-half r of per-type AUROC; ECE shift | Table usable only if split-half r above 0.6 |
| T10 Line-level confidence | Long solutions with per-line verifiable steps | per-line agreement among K=4 re-derivations; verbalized per-line | AUROC for first-failing-line localisation | Line-level works; atomic-claim level does not (d15) |
| T11 Contrary evidence | Items with a planted contrary hint (true and false) | none; located; confidence-update check | confidence shift on true vs false hint; accuracy | Radical-belief pattern (small updates) is the failure to look for (a10) |

Run order and priorities are in UNKNOWNS.md.

## 9. What does not transfer, and why

- **Gray-matter and lesion findings (Fleming 2010, 2014).** The brain-structure link has no counterpart in a scaffold. It tells us only that confidence quality can be a separable skill, which matches the LLM finding that discrimination is not a by-product of accuracy (lower ECE from higher accuracy, a19; Yoon: GLM-Z1 less accurate yet better calibrated).
- **meta-d'/d'.** Needs a signal detection type 1 model with a continuous stimulus. LLM papers used AUC (c17). Use matched-difficulty bins instead.
- **Human staircase effects (Rahnev and Fleming).** There is no staircase in our items, but the same inflation arises when easy and hard items mix: raw AUROC rises just because the system can tell easy from hard (Kapoor's wrong-answers-only ablation points to this, b18). Always bin by difficulty.
- **Monkey LIP neurons.** No analogue in an API agent.
- **Hidden-state probes (Yuan, d05) and logit methods (DeepConf, CGES).** Need weights or logprobs. Substitute: sample agreement and verbalized confidence.
- **Finetuned calibration (Lin, Kapoor).** Needs training. The scaffold substitute is the calibration log.
- **Artificial concept injection (Anthropic 2025, c20).** Not a natural use case; authors say transfer to normal use is unclear and details may be confabulated.
- **Radical-belief questionnaire (Rollwage).** The underlying pattern (low update after contrary evidence) transfers as a test (T11), not the population finding.
- **Human over-trust (Steyvers, Zhou).** Matters only when the agent's output is read by a person. It does not change the agent's internal decisions.
- **2023 numbers for reasoning models.** Xiong's 54.8% to 92.7% and Huang's self-correction collapse came from non-reasoning models and do not carry to 2026 reasoning models (d01, d08).
- **Debate.** Out (G9); c14 shows no gain over sampling at matched cost.

## 10. Open questions

1. Does the sample-agreement edge return on hard open tasks, code agents and multi-step work for frontier reasoning models? Del covered three models and 17 tasks; equal-token comparison beyond gpt-oss-20b is missing.
2. End-of-chain verbalized confidence versus agreement on open-ended and code chains for frontier models. Code agents sit near chance (d09), but no head-to-head with agreement exists.
3. Does an external check beat any internal confidence, and can confidence gate when a check is worth its cost? No paper found that prices a check against a confidence-gated trigger.
4. Does hiding the model's own earlier answer reduce anchoring in an agent loop, and by how much? Only Kumaran and indirect support.
5. Semantic entropy for multi-step trajectories: only TrACE (3B, n=30 to 50).
6. Do per-type calibration tables transfer between models and task types? Evidence says not evenly (d04).
7. Is human BA10 efficiency a replicated, separable skill at large N? Only small-N lesion and an activation study.
8. Black-box early stopping with verbalized scalars: loss untested (CGES needs logprobs or a reward model).
9. Do hedging and tone track internal uncertainty after 2025 post-training? Yona's metric has not been re-run on current models.
10. Why do reasoning models disagree across studies (Yoon better, Mei worse, Amit lower ranking)? Probable factors: ECE vs AUROC, model family, task length.
11. Is VC's advantage for reasoning models a function of RLVR training in math (d02: gains largest in math)? Would predict weak VC in non-verifiable domains.
12. Does extra reasoning effort increase overconfidence on wrong answers in general? d03 supports, d19 is too thin.

## 11. Sources

[V] = opened (read page or PDF text). [M] = snippet or abstract only, or not readable.

- [V] Fleming and Lau (2014) How to measure metacognition. https://pmc.ncbi.nlm.nih.gov/articles/PMC4097944/ (a01, a02, a03)
- [V] Fleming et al. (2010) Relating introspective accuracy to individual differences in brain structure. https://pmc.ncbi.nlm.nih.gov/articles/PMC3173849/ (a04, a05, b01, b02)
- [V] Kiani and Shadlen (2009) Representation of confidence associated with a decision by neurons in the parietal cortex. https://pmc.ncbi.nlm.nih.gov/articles/PMC2738936/ (a06)
- [M] Meyniel, Sigman and Mainen (2015) Confidence as Bayesian probability. https://pubmed.ncbi.nlm.nih.gov/26447574/ (a07)
- [V] Fleming and Daw (2017) Self-evaluation of decision-making. https://pmc.ncbi.nlm.nih.gov/articles/PMC5178868/ (a08, a09)
- [V] Rollwage, Dolan and Fleming (2018) Metacognitive failure as a feature of those holding radical beliefs. https://pmc.ncbi.nlm.nih.gov/articles/PMC6303190/ (a10)
- [V] Guo et al. (2017) On calibration of modern neural networks. https://arxiv.org/abs/1706.04599 (a11)
- [V] Kadavath et al. (2022) Language models (mostly) know what they know. https://arxiv.org/abs/2207.05221 (a12, a13, b06 to b09, c01 to c03)
- [V] Lin, Hilton and Evans (2022) Teaching models to express their uncertainty in words. https://arxiv.org/abs/2205.14334 (a14, b25, c04, c05)
- [V] Wang et al. (2022) Self-consistency improves chain of thought reasoning. https://arxiv.org/abs/2203.11171 (a15, b26, c10)
- [V, abstract and intro only] Yin et al. (2023) Do LLMs know what they don't know? https://arxiv.org/abs/2305.18153 (a16)
- [V] Tian et al. (2023) Just ask for calibration. https://arxiv.org/abs/2305.14975 (a17, b15, b16, c06)
- [V] Xiong et al. (2024) Can LLMs express their uncertainty? https://arxiv.org/abs/2306.13063 (a18 to a20, b10 to b14, c07 to c09, c24)
- [V] Kuhn, Gal and Farquhar (2023) Semantic uncertainty. https://arxiv.org/abs/2302.09664 (a21, b20, c11)
- [V] Kapoor et al. (2024) Large language models must be taught to know what they don't know. https://arxiv.org/abs/2406.08391 (a22, b17 to b19, c18)
- [V] Steyvers et al. (2025) What LLMs know and what people think they know. https://arxiv.org/abs/2401.13835 (a23, b23, b24, c16, c17)
- [V, no data in parts read] Steyvers and Peters (2025) Metacognition and uncertainty communication in humans and LLMs. https://arxiv.org/abs/2504.14045 (a24)
- [V] Kumaran, Fleming et al. (2025) Overconfidence in initial choices and underconfidence under criticism. https://arxiv.org/abs/2507.03120 (a25)
- [V] Ji-An et al. (2025) Language models are capable of metacognitive monitoring and control of their internal activations. https://arxiv.org/abs/2505.13763 (a26)
- [V] Mazancieux et al. (2020) Is there a G factor for metacognition? https://pmc.ncbi.nlm.nih.gov/articles/PMC7397761/ (b03)
- [V] Rahnev and Fleming (2019) How experimental procedures influence estimates of metacognitive ability. https://pmc.ncbi.nlm.nih.gov/articles/PMC6556214/ (b04)
- [V] Rahnev et al. (2022) Consensus goals in the field of visual metacognition. https://pmc.ncbi.nlm.nih.gov/articles/PMC9633335/ (b05)
- [M] Geng et al. (2024) A survey of confidence estimation and calibration in LLMs. https://arxiv.org/abs/2311.08298 (b27)
- [V] Yoon et al. (2025) Reasoning models better express their confidence. https://arxiv.org/abs/2505.14489 (b21, b22)
- [M] Farquhar et al. (2024) Detecting hallucinations in LLMs using semantic entropy. https://www.nature.com/articles/s41586-024-07421-0 (c12, page not readable)
- [V] Huang et al. (2024) Large language models cannot self-correct reasoning yet. https://arxiv.org/abs/2310.01798 (c13, c14)
- [V] Zhou et al. (2024) Relying on the unreliable. https://arxiv.org/abs/2401.06730 (c15)
- [V] Binder et al. (2024) Looking inward. https://arxiv.org/abs/2410.13787 (c19)
- [V, first 100k of 403k characters] Anthropic (2025) Emergent introspective awareness in large language models. https://transformer-circuits.pub/2025/introspection/index.html (c20)
- [V] Taubenfeld et al. (2025) Confidence improves self-consistency in LLMs. https://arxiv.org/abs/2502.06233 (c21)
- [V] Aggarwal et al. (2023) Let's sample step by step: Adaptive-Consistency. https://arxiv.org/abs/2305.11860 (c22)
- [V] Fu et al. (2025) Deep Think with Confidence. https://arxiv.org/abs/2508.15260 (c23)
- [M] Griot et al. (2025) Large language models lack essential metacognition for reliable medical reasoning. https://www.nature.com/articles/s41467-025-59153-5 (c25, page not readable)
- [V] Del et al. (2026) How uncertainty estimation scales with sampling in reasoning models. https://arxiv.org/abs/2603.19118 (d01, d02)
- [V] Mei et al. (2025) Reasoning about uncertainty: do reasoning models know when they don't know? https://arxiv.org/abs/2506.18183 (d03)
- [V] Cacioli (2026) Domain-level metacognitive monitoring in frontier LLMs. https://arxiv.org/abs/2605.06673 (d04)
- [V] Yuan et al. (2026) Hidden error awareness in chain-of-thought reasoning. https://arxiv.org/abs/2605.09502 (d05)
- [V] Sethi (2026) Do not overthink it: inter-rollout action agreement (TrACE). https://arxiv.org/abs/2604.08369 (d06)
- [V] Aghazadeh et al. (2026) CGES: confidence-guided early stopping. https://arxiv.org/abs/2511.02603 (d07)
- [V] Stav et al. (2026) When does intrinsic self-correction help? https://arxiv.org/abs/2606.23196 (d08)
- [V] Kaddour et al. (2026) Agentic uncertainty reveals agentic overconfidence. https://arxiv.org/abs/2602.06948 (d09, d10)
- [V] Ravuri and Amarasinghe (2025) Eliminating hallucination-induced errors in code generation with functional clustering. https://arxiv.org/abs/2506.11021 (d11)
- [V] Harshavardhan (2026) Self-anchoring calibration drift in LLMs. https://arxiv.org/abs/2603.01239 (d12)
- [V] Yona, Aharoni and Geva (2024) Can LLMs faithfully express their intrinsic uncertainty in words? https://arxiv.org/abs/2405.16908 (d13)
- [V] Wang et al. (2026) Are LLM decisions faithful to verbal confidence? https://arxiv.org/abs/2601.07767 (d14)
- [V] Amit, Galil and El-Yaniv (2026) Evaluating LLM uncertainty in long-form generation. https://arxiv.org/abs/2607.03870 (d15)
- [V] Zhao et al. (2026) SeSE. https://arxiv.org/abs/2511.16275 (d16)
- [V] Fleming, Ryu, Golfinopoulos and Rees (2014) Domain-specific impairment in metacognitive accuracy following anterior prefrontal lesions. https://pmc.ncbi.nlm.nih.gov/articles/PMC4163038/ (d17)
- [M, abstract only] Molenberghs et al. (2016) Neural correlates of metacognitive ability and of feeling confident. https://pmc.ncbi.nlm.nih.gov/articles/PMC5141950/ (d18)
- [V] Hiremath and Hiremath (2026) Calibration drift under reasoning. https://arxiv.org/abs/2606.11211 (d19)

Note: a16, a24, b27, c05 and c16 carry little or no extracted data; a07, c12, c25 and d18 were not read in full. Do not cite numbers from them.
