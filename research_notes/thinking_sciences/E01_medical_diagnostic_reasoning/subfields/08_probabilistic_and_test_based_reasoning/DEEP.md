# Probabilistic and test-based reasoning: deep document

*Subfield E01.08. Key works: Pauker and Kassirer; Sox. Schema hooks: S7 discriminating test, G5 code normalises. Evidence files in this folder: evidence_a-d.jsonl (ids a01-d26), claims.jsonl (K01-K26), critique.md. Status tags: [E] established, [S] single-source, [C] contested.*

## 1. What it is

This subfield asks how a reasoner should turn a test result into a belief, and when a test is worth ordering at all.

Two ideas sit at the core.

1. **Bayesian updating with likelihood ratios (LR).** Start with a pretest probability. Multiply the pretest odds by the LR of the result. Read off the post-test probability. LR+ = sensitivity / (1 - specificity). LR- = (1 - sensitivity) / specificity.
2. **Threshold decision rules.** Pauker and Kassirer (1980) showed that the choice to test is a decision with two cut points. Below the testing threshold: do nothing. Above the test-treatment threshold: act without testing. Between them: test, then act on the result.

Around these sit three bodies of work.

- **Human error.** Clinicians neglect base rates, overestimate pretest and post-test probability, and mis-chain tests.
- **Test-quality evidence.** Published sensitivity and specificity are inflated by study design and shift with the patient mix (spectrum effect).
- **Question and test selection.** Choosing the next test by expected information gain (EIG). In 2024-2026 this moved into LLM work (UoT, BED-LLM, ACTMED, MAI-DxO).

Why it matters for our agent. S7 asks for a discriminating test when two rules still fit. G5 says code does the normalising. This subfield gives the best-worked answer to "when is a test worth running, how do I update on its result, and what goes wrong when the model does the arithmetic itself". It is a human-reasoning field, so most transfer is by analogy. The LLM evidence is thin and mostly single-model vignettes.

Scope. Not covered here: illness scripts and pattern recognition (other E01 subfields), reflective reasoning (E01.07), clinical decision support in general (E01.09). Linked topics researched in parallel: Bayesian and causal learning, expected information gain models, uncertain evidence, optimal stopping, noise and judgement, resource-rational analysis.

## 2. History and theories in depth

### 2.1 Decision-analytic roots (1975-1994)

- **Pauker and Kassirer (1975)**, NEJM 293:229 (a01, abstract only). First therapeutic threshold: treat if the probability of disease is above a level set by the benefit and harm of treatment. Assumes the probability is known and utilities are fixed.
- **Fagan (1975)**, NEJM 293:257 (a24, not read). A one-page nomogram: pretest probability and LR in, post-test probability out, no calculator. Content from memory only.
- **Pauker and Kassirer (1980)**, NEJM 302:1109 (a02, b01, d18; abstract only). The two-threshold model. Values come from sensitivity, specificity, test risk, treatment benefit and risk. No empirical sample. It is a derivation.
- **Eddy (1982)** (a22, not opened). The classic finding that physicians confuse P(positive | disease) with P(disease | positive). Numbers from memory only: prevalence 1%, sensitivity about 79%, false positive about 9.6%, true posterior about 7.5%, most of 100 physicians said about 75%. Not used in any claim.
- **Sox et al. (1986)**, Ann Intern Med 104 (a03; abstract only). Teaches Bayes' theorem to readers of the test literature. Warns about pitfalls in estimating pretest probability and about the limits of sensitivity/specificity studies (the spectrum problem).
- **Sox et al. (1989)**, Med Decis Making (a04; abstract only). Extends thresholds to tests with several outputs (CT for mediastinal and hilar spread in lung cancer). Four thresholds arise. The range of priors where testing is best gets wider. Ignoring part of the test information gives wrong advice.
- **Kassirer (1989)** (a25, not read). Argues that chasing certainty drives low-yield tests. A test only helps if its result could change the action.
- **Berner et al. (1994)** and **Heckerman et al. (1992)** (c23, c24; abstracts only). Old expert systems. DXplain, Iliad, Meditel, QMR listed the right diagnosis in 52-71% of 105 hard cases and added about 2 extra relevant diagnoses per case. Pathfinder did better when it modelled dependencies among findings than when it assumed independence.

### 2.2 The human-error tradition (1978-2021)

- **Casscells, Schoenberger and Graboys (1978)**: prevalence 1 in 1000, false positive rate 5%. What is the chance a positive person has the disease? Only 11 of 60 (18%) answered correctly (about 2%). The modal answer was 95% (27/60).
- **Manrai et al. (2014)** replicated it. 14 of 61 (23%). Difference 5 points, 95% CI -11 to 21. Same modal answer, 95% (27/61). Median answer 66%, about 33 times the truth.
- **Gigerenzer and Hoffrage (1995)** introduced natural frequencies (counts from a reference group). Original numbers not opened (a23). **Hoffrage and Gigerenzer (1998)**: 48 physicians, four tests, 10% correct with probabilities and 46% with natural frequencies. Hemoccult example: 1 of 24 correct with probabilities, 16 of 24 with frequencies.
- **Morgan et al. (2021)** moved from the textbook problem to realistic vignettes, N = 553 practitioners. Overestimation in all four scenarios, before and after the test.
- **Gill, Sabin and Schmid (2005)** (a11) argued clinicians are "natural Bayesians" in practice. This sits against the explicit-estimate data and is a one-line abstract, so it carries little weight.

### 2.3 Why frequencies help: two theories

- **Ecological rationality** (Gigerenzer, Hoffrage): the mind handles counts from natural sampling. Normalised probabilities hide the base rate.
- **Nested sets** (Barbey, Sloman, Sirota): any format that makes the set structure clear helps, and analytic ability matters.

Later exchanges found large overlap (b24). No decisive experiment exists [C]. For an engineer the question is moot. Both predict the same fix: show the counts and the set structure, and do the arithmetic in code.

A newer proposal (Fenwick, Campitelli and Thompson 2026, b23) says training and expertise, not a privileged format, produce Bayesian competence. Trained people do well in probability format too.

### 2.4 Threshold psychology

Djulbegovic et al. (2015, a20, a21) argue that thresholds are not fixed facts. They move with regret and context, and intuitive (type 1) views of benefit and harm can swamp the expected-utility threshold. A 2026 framework (d19) says testing thresholds are dynamic: symptom amplitude, time course, patient values, system cost, test quality. All abstract-level, no data fit.

### 2.5 Test selection by information gain, then LLMs (2024-2026)

- **Uncertainty of Thoughts (UoT)**, Hu et al. 2024 (c14, c15, d02).
- **BED-LLM**, Choudhury et al. 2026 (c16, d03).
- **ACTMED**, 2025 (a17).
- **MAI-DxO / SDBench**, Nori et al. 2025, Science 2026 (a16, c11-c13, d04, d05).
- **MediQ**, Li et al. 2024 (c19, d25): asking questions can hurt unless gated.

Details in sections 4 and 6.

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Clinicians neglect the base rate on the Casscells problem | 1978: 11/60 correct (18%); 2013: 14/61 (23%); diff 5 pts, CI -11 to 21; modal answer 95% in 27/60 and 27/61; median 66% (33x truth) | a05, b02, b03; K01 | [E] |
| Error type in the wrong answers | Answers ranged 0.005% to 96%. Respondents knew to compute PPV but mishandled prevalence ("PPV does not depend on prevalence") | b03 | [E] (qualitative) |
| Practitioners overestimate pretest and post-test probability | N=553 of 723. Pneumonia pretest 80% vs evidence 25-42%. Breast cancer after positive mammogram 50% vs 3-9%. Ischemia after positive stress test 70% vs 2-11%. UTI after positive culture 80% vs 0-8.3%. All P<.001. Overestimates 2 to 10 times | a12, b04; K02 | [E] |
| Same overestimation in an independent sample | 357 complete of 707 emergency physicians (Sweden); first-frame median about 70% vs reference 3-16% for acute coronary syndrome | d20; K02 | [E] (2 sources) |
| The update step is a second error source, test-specific | Imputed LR+ practitioners vs evidence: stress test 21 vs 2.0-2.7; mammography 44.3 vs 13-33; chest X-ray 4.8 vs 2.6; urine culture 9.0 vs 9.0 (correct) | b05 | [E] |
| Inflated probability turns into stated treatment | 551/553 (99.6%) would give antibiotics after positive X-ray; 401/553 (72.5%) even after negative X-ray | b06 | [S] (stated intent) |
| Professional type barely matters | Pneumonia after positive X-ray: residents 95, attendings 95, APPs 95 | b07 | [S] |
| Natural frequencies raise correct answers, most still fail | Meta-analysis, 35 articles, 226 estimates: 24% vs 4% | a08, a09, b17; K05 | [E] |
| Effect in physicians | 48 physicians: 10% vs 46%. Hemoccult: 1/24 vs 16/24 | a06, d21 | [E] (old, small) |
| Effect size varies a lot | Weber replication N=180: 36% vs 20%. Students N=64: mean over 4 tasks 7% vs 45%; task 1 1% vs 59% | b18, d21 | [E] direction; size varies |
| Many people convert frequencies back to probabilities | 49% of those given frequencies calculated with probabilities; frequencies were the calculation format in 34% of 360 tasks | b18 | [S] |
| Format effect reverses for two chained tests | N=329. Single test: 36.2% frequencies vs 21.6% odds/LR (OR 2.41). Two sequential tests: 10.6% odds/LR vs 4.9% frequencies (OR 2.73) | b19; K06 | [C] |
| Frequency benefit moderated by exposure and field | No prior exposure OR 1.74 (CI 1.02-3.04); psychology students OR 1.45 (CI 0.82-2.63, ns) | b20 | [S] |
| Visuals help in many studies, not all | Frequencies + visuals 42% vs 5% probabilities. Khan 2015: only 20% solved, no visual gain | b21, b22 | [C] |
| Teaching beats format change alone | Medical students N=78: Bayes-rule teaching 18% and 22%; frequency tree 73% and 81%. Transfer to complex tasks: 40% three cue values, 81% two cues | a10, d21 | [S] |
| Two theories explain the frequency effect | No decisive test | b23, b24; K07 | [C] |
| GPT-4 beats clinicians on pretest and post-negative probability | 100 runs at temperature 1.0 vs N=553. Less error in all 5 cases after negative; after positive better in 2, similar in 2, worse in 1 | a13, b08, c04; K09 | [E] |
| GPT-4 fails the positive stress test like clinicians | LLM 69 vs clinicians 70 (reference 2-11); MAE 56.5 vs 56.2 | a13, c05 | [E] |
| o1-preview fixes only the stress-test case | Ischemia after positive: 10.9 (o1) / 68.7 (GPT-4) / 70 (clinicians); MAE 5.7 / 56.5 / 56.3. Breast cancer 2.8 / 7.8 / 50 | a14, c06 | [E] |
| Label framing drives the error | Bacteriuria framed as UTI: LLM pretest 26% vs truth 0-1%; post-positive 90% vs 0-8% | b09; K10 | [S] |
| LLM Bayes depends on whether numbers are given | With numbers: Bayes. Without: base rate (10%) or sensitivity (80%) returned. GPT-3.5 failed on retest | b14, c10, a15; K08 | [E] |
| LLMs ignore base rates when priors must be recalled | Jason test: posteriors 0.75 vs 0.25 for GPT-4o, GPT-4, Claude-3-Opus on uncharacteristic descriptions (ratio 9 / 9 / 8.86); representative descriptions give ratio near 1 | a15 | [S] (non-clinical) |
| Medical names break Bayes in ChatGPT | Abstract A,B,C: 19/20 correct. Medical names: sensitivity not conditioned on cough 10/20, pretest 12/20. With "sensitivity/specificity" wording 16/20 and 17/20. Stepwise prompt: errors 0/20 | b12, b13, c01-c03; K11 | [S] |
| Direct pretest probability from records is chance | AUROC 49.9 (CI 47.8-51.9) token logits; 50.9 verbalised; N=660 | c08, c09; K12 | [S] (small open models) |
| LLMs plateau when updating over rounds | Off-the-shelf 36-58% final-round vs Bayesian Assistant 81%; tuning gives about 80% agreement. CoT, numeric formats, 30 rounds gave no gain | a19, b15, c17; K13 | [S] |
| Elicited LRs: no mean bias, large dispersion | 700 LRs, 30 conditions. Mean bias GPT-4o 1.02x, o3 0.99x, GPT-5 0.99x. 95% limits GPT-5 0.26x-3.70x, o3 0.23x-4.28x, GPT-4o 0.23x-4.53x. Calibration slope 0.73-0.88 | d06; K19 | [S] |
| Published test accuracy is inflated | Case-control design RDOR 3.0 (CI 2.0-4.5) over 184 studies, 218 tests; sens/spec shift 0-40 points across prevalence, significant in 8/23 reviews; pooled value overstates community positives by 10.8-19.1% | d08-d11; K20 | [E] |
| Chaining LRs overstates when tests share a driver | Toy: Se=Sp=0.9, prior 0.1. Independent 0.90; covariance 0.03: 0.70; 0.05: 0.614; 0.08 (non-diseased): 0.50; duplicate test 0.50 | d13-d15; K21 | [S] (own calculation plus theory) |
| Dependence cannot be learned from few tests | Needs 4+ tests, or a strong prior, for identifiability | d14 | [S] |
| Without stated costs LLMs over-order | GPT-3.5 radiology sensitivity 0.96-0.98, specificity 0.13-0.23 over four prompts; admission specificity 0.07 to 0.37. Exam precision 22.8-41.8% | d16, d17; K22 | [S] |
| More free turns do not improve test choice | Recall 37.9-43.6%; accuracy R1 71.79% (1-turn) to 76.18% (free) to 89.76% (all results given); loops | d17, d24; K23 | [S] |
| EIG selection beats direct prompting by large margins | UoT +38.1% average success; BED-LLM +37.4 points over Prompt-Only | c14, c16 | [E] vs naive baseline |
| EIG gain over a strong halving heuristic is small on medical tasks, variable on 20Q | GPT-4, equal tokens: medical 85.1 vs 88.4 (4.5k vs 4.7k tokens), 86.7 vs 92.5 (9k); 20Q 33.8 vs 48.1 and 40.9 vs 54.4. BED-LLM vs Split: Animals GPT-4o 93 vs 83; Celebrities 86 vs 63; Things 64 vs 40 | d02, d03; K14 | [C] |
| EIG stop rule cuts tests | ACTMED about 50% fewer tests, comparable or better accuracy; 3 tests, 5 seeds | a17 | [S] |
| Scaffold with Bayesian differential and test chooser lifts sequential diagnosis | 304 NEJM cases. Physicians 19.9% at $2,963; GPT-4o 49.3% at $2,745; o3 78.6% at $7,850; MAI-DxO 79.9% at $2,396; 81.9% at $4,735; ensemble 85.5% at $7,184. Science: 83.2% and 80.3% vs 36.1% and 46.8% | a16, c11, d04, d05; K15 | [S] (bundled, no role ablation) |
| Naive question-asking hurts | -11.3% relative to non-interactive; confidence-gated asking +22.3% over plain interactive, +12.1% over Initial; 10.3% gap to full information | c19, d25; K16 | [S] |
| Counts from corpus are a cheap second signal | MedQA n=719: 46.7% vs 44.1% LLM, hybrid 47.3%. Agreement (38.3% of questions) gives 64.7% correct | a18; K17 | [S] |
| Stated confidence can be uninformative | Gemini 2.5 Pro 9.66 correct vs 9.67 incorrect; ChatGPT-5 9.42 vs 7.80 (p=0.04) | d22; K26 | [S] |
| Giving physicians GPT-4 did not help | 76% vs 74%, diff 2 (CI -4 to 8); LLM alone 16 points above control | c22; K18 | [S] |

## 4. Mechanisms and models

### 4.1 Odds form of Bayes with LRs

```
prior_odds   = p / (1 - p)
LR_pos       = Se / (1 - Sp)
LR_neg       = (1 - Se) / Sp
post_odds    = prior_odds * LR            (one LR per conditionally independent result)
post_p       = post_odds / (1 + post_odds)
```

Worked check. Prevalence 0.001, false-positive rate 0.05, sensitivity assumed 1.0. LR+ = 1/0.05 = 20. Prior odds = 0.001. Post odds = 0.02. Post p = 1.96%. The median clinician said 66% (b02).

Natural-frequency version. Take 1000 people. 1 is sick and tests positive. 999 are healthy and about 50 test positive. So 1 of about 51 positives is sick. Same answer, no formula. In code, always compute the odds form and, if a readable trace is wanted, print the counts.

### 4.2 Two-threshold rule (Pauker-Kassirer, re-derived in d18)

Let B = net benefit of treating the diseased, C = net harm of treating the non-diseased, Rt = test risk (in utility units).

```
treat-no-test threshold   Pt = C / (B + C)          (single-threshold form)
testing threshold         L  = ((1 - Sp) * C + Rt) / ((1 - Sp) * C + Se * B)
test-treatment threshold  U  = (Sp * C - Rt) / (Sp * C + (1 - Se) * B)
action(p):  p < L  -> do nothing
            p > U  -> act without testing
            L <= p <= U -> test, then act on the result
```

Check (d18, symmetric case). Se=Sp=0.9, B=C=1, Rt=0: L=0.10, U=0.90. With Rt=0.05: L=0.15, U=0.85. A worse or riskier test narrows the testing window.

The formulas were re-derived in the research session and checked on the symmetric case only. They were not copied from the 1980 paper, which was read at abstract level. Treat them as a derivation to unit-test, not a citation.

Sox 1989 extension: if a test informs two events, thresholds multiply (four). Use all outputs of the test, not one bit.

### 4.3 Test-value check: "can this result change the action?"

A cheap rule that follows from 4.2 and from Kassirer's argument. Before running a test, compute the post-test probability for each possible result. If every result leaves p on the same side of the action threshold, the test cannot change the action. Skip it. In the agent, S7 should run a discriminating test only if the two leading hypotheses would be ranked differently by some result. For code problems this is "the one input where the two rules differ".

### 4.4 Expected information gain (EIG) selection

```
for each candidate test/question q:
    for each outcome o (with P(o | q) from the hypothesis weights):
        posterior_o = normalise(prior * P(o | hypothesis))
    EIG(q) = H(prior) - sum_o P(o|q) * H(posterior_o)
choose argmax EIG(q)   (optionally divided by cost(q))
stop when max EIG < floor, or posterior margin > threshold, or budget gone
```

Variants in the evidence.

- **UoT** (c14, d02): LLM proposes questions and simulates answers over a possibility set. Reward is information gain over that set. Tree lookahead with pruning.
- **BED-LLM** (c16, d03): uses the LLM's own predictive distribution with a noisy-answer likelihood. Entropy-only selection (deterministic-answer shortcut) is worse than true EIG.
- **ACTMED** (a17): expected KL divergence from prior to a simulated posterior; stops when expected gain is small.
- **Halving / Split heuristic**: pick the question that splits the live hypotheses most evenly. It is the right comparison baseline, and it is strong.

Key caveat. The outcome model P(o | h) is simulated by the LLM and has not been shown to be calibrated. EIG is only as good as those numbers. In code problems the outcome of a test can be run, which removes this weakness. That is the best fit for our agent.

### 4.5 Elicit separately, compute in code

BIRD (d07) and the human-error data (K08, K09, K12) point one way.

1. Ask the model for each ingredient as its own field: prior (or reference class), LR or Se/Sp per finding, and what each finding is conditioned on.
2. Store them with ranges, setting, and study-design flags (4.6).
3. Compute the posterior in code. Normalise over exclusive hypotheses (G5).
4. Show the model the result and let it explain, not recompute.

This is a candidate, not proven. No head-to-head against a one-shot posterior at equal tokens on 2025-2026 models was found (critique gap 1).

### 4.6 LR hygiene

- Store LR as an interval, not a point. GPT-5's 95% limits are 0.26x to 3.70x (d06). Published LRs are inflated by case-control design (RDOR 3.0, d08) and shift with prevalence (d09).
- Flag lab-test LRs as the least reliable elicited type (d06).
- Decision-flip check: recompute the action at both ends of the range. If the action is the same, ignore the uncertainty. If it flips, more information is worth its cost.

### 4.7 Chaining tests

Naive chaining multiplies LRs. That is valid only if results are conditionally independent given the disease state.

- Group tests that share a mechanism (same biomarker, same imaging physics, same history finding).
- Cap the combined LR of a group at the largest member, or at a stated ceiling.
- Widen the interval after each chained step.
- A duplicate test adds nothing (d15 upper limit: 0.50 in the toy).

Dependence is not learnable from fewer than 4 tests (d14), so this must be a prior-based cap, not an estimate.

### 4.8 Stop rules

Candidates, none tested head to head.

- **Posterior margin**: stop when the top posterior exceeds the runner-up by a margin.
- **EIG floor**: stop when the best EIG is below a floor (ACTMED).
- **Certainty threshold**: MAI-DxO commits when certainty passes a threshold, untuned (d04). Certainty there is model-stated, and the schema forbids verbal confidence as a stop signal (4b).
- **Loop guard**: stop on a repeated request. Needed because models loop (d17).

Stopping behaviour depends on case mix and protocol (d24), so any comparison needs a fixed simulator and turn cap.

## 5. What holds up

### 5.1 Replicated and robust

- **Base-rate neglect in clinicians.** 18% (1978) vs 23% (2013) with the same modal answer (b02). An independent second source on realistic vignettes confirms overestimation (d20). Caution: Morgan, Rodman and Brodeur share one dataset and one clinician sample, so they are not independent confirmations of clinician error (critique).
- **Natural frequencies help.** Direction replicates in a meta-analysis (35 articles), in Weber (36 vs 20), in physicians (10 to 46%), in students (7 to 45%), and in Schulz for single tests (36.2 vs 21.6).
- **Spectrum and design bias in test accuracy.** Four independent lines (d08-d12).
- **LLMs obey Bayes when handed all numbers and fail when they must recall them.** Three studies (a15, b14, c10).
- **LLM probability estimates are unreliable at the single-value level.** Three sources (K09).

### 5.2 Moderators

- Short menu format and visual aids raise performance in both formats (a08).
- Numeracy, cognitive reflection, working memory and visuospatial ability predict accuracy in both formats (b23).
- Plain wording and fewer mental steps raise accuracy (b25).
- Prior exposure and field of study (b20).
- Test type: stress-test LR badly inflated, urine-culture LR accurate (b05).
- Task type: two chained tests flip the format effect (b19).

### 5.3 Failures, weak spots and contradictions

- **"Natural frequencies fix it" is wrong.** About three quarters still fail (a08). Physicians: 46% best case. Many convert frequencies back to probabilities (49%, b18).
- **Effect size is not stable.** 4-24% pooled; 20-36% in Weber; 10-46% in physicians.
- **Odds/LR beats frequencies on two chained tests** (10.6% vs 4.9%), but both are poor and the sample is students (b19).
- **Visuals sometimes give no gain** (Khan 2015: 20% solved, no effect) (b21).
- **Gill et al. "natural Bayesians"** is at odds with the explicit-estimate data and has no numbers (a11).
- **Cause of the frequency effect is unresolved** (K07).
- **Counts disagree between sources:** 35 articles / 226 estimates (PubMed abstract, used here) vs a conference snippet of 30 papers / 90 effects (critique).
- **Several originals were never opened:** Eddy 1982, Gigerenzer and Hoffrage 1995, Fagan 1975, Kassirer 1989. No numbers from them are used in claims.
- **No numeric threshold values were captured** from Pauker-Kassirer or Sox. The formulas here are our re-derivation.
- **No LLM study found that tests the threshold rule itself** with measured results.

### 5.4 Interventions that worked and did not

| Intervention | Result | Source |
|---|---|---|
| Natural frequencies | 4% to 24% pooled; 10% to 46% physicians | a06, a08 |
| Frequency-tree teaching | 73% and 81% vs Bayes-rule teaching 18% and 22% (students) | d21 |
| Teaching on simple tasks | Transfers to complex ones (40% three cues, 81% two cues) | a10 |
| Visual aids | 42% vs 5% in some studies; no gain in others | b21 |
| Odds/LR for two chained tests | 10.6% vs 4.9% | b19 |
| Stepwise prompt for LLM Bayes | Conditioning errors 0/20 (from 10/20 and 12/20) | c03 |
| Prompt restraint on test ordering ("only if absolutely required") | Barely helped (specificity 0.13 to 0.23) | d16 |
| More free turns for test requests | +2-5 points accuracy, loops, recall flat | d17 |
| Chain-of-thought and numeric formats for belief updating | No meaningful gain | c17 |
| Fine-tuning on a Bayesian teacher | About 80% agreement; outside our no-training scope | a19, c18 |
| Giving physicians an LLM | 76% vs 74%, no gain | c22 |
| Confidence-gated asking | +22.3% over plain interactive | c19, d25 |

## 6. Language models

### 6.1 Probability estimation in vignettes

- **GPT-4 (Oct 2023, Rodman).** Less error than 553 clinicians after negative tests in all 5 cases. After positive tests, better in 2, similar in 2, worse in 1. Breast cancer after positive mammogram: LLM 8% (IQR 7-8) vs clinicians 50% vs reference 3-9%. Hypothetical test: LLM 2% vs clinicians 95%. Failure: stress test after positive, 69% vs reference 2-11%. The narrow spread across 100 samples partly explains the lower error. Five simple vignettes, simple prompt.
- **o1-preview (Brodeur).** Same as GPT-4 except the stress test (10.9 vs 68.7). Pneumonia pretest MAE 31.6 (o1) vs 39.5 (GPT-4) vs 47.7 (clinicians). The gain was one case, not general calibration.
- **Label framing.** Bacteriuria framed as UTI: LLM assumed disease (26% pretest vs 0-1% truth).
- **Not rechecked on current models.** No study reran the Morgan vignettes on GPT-5, Claude 4+ or Gemini 2.5+ (gap 6).

### 6.2 Elicited numbers

- Direct pretest from records: AUROC about 50 for Mistral-7B and Llama3-70B (c08). Embeddings carry signal. Frontier models untested.
- Elicited LRs (d06): no average bias, but several-fold error on single values, shrinkage toward 1, lab tests worst, memorisation of TheNNT not excluded. The authors did not compare an LR workflow against an end-to-end answer.
- Stated confidence on neurology vignettes: Gemini 2.5 Pro 9.66 correct vs 9.67 incorrect (d22). A conference abstract on 50 vignettes.

### 6.3 Doing the arithmetic

- With all numbers given, models follow Bayes. Without, they give the base rate or the sensitivity (c10, a15).
- ChatGPT in 2023: 19/20 correct with abstract symbols, 50-60% conditioning errors with medical names, 80-85% with sensitivity/specificity wording. A stepwise prompt removed the conditioning errors (0/20). Single model, 20 chats per prompt.
- Version drift: GPT-3.5 passed in March and failed the same prompt in August (b14).
- Textbook counts problems look nearly solved by LLMs, inferred indirectly from online participants (57% scoring 5/5 vs about 24% human ceiling, d23).
- Reasoning LLMs do not adopt natural frequencies unprompted and misapply them when told to (3 models, one problem, qualitative, d01).
- Belief accumulation over rounds: off-the-shelf models plateau after round 1 (36-58% vs 81%). Prompting did not fix it. Tuning did (a19, c17).

### 6.4 Test and question selection

- UoT: +38.1% average success over direct prompting on 5 datasets and 5 LLMs. GPT-4 DX closed set 97.0 vs 91.3. At equal tokens against a halving heuristic, the medical gain is +3.3 to +5.8 points (d02).
- BED-LLM: +37.4 points over Prompt-Only. Against Split: Animals 93 vs 83 (GPT-4o), Celebrities 86 vs 63, Things 64 vs 40 (d03). Entropy-only is worse than true EIG.
- ACTMED: about 50% fewer tests, comparable or better accuracy (tabular tasks, GPT-4o-mini and GPT-4o).
- MediQ: asking without gating cost 11.3% relative; gating gained 22.3% over plain interactive.
- MAI-DxO (K15): roles are hypothesis tracker (Bayesian-style), test chooser (maximally discriminating), challenger (falsification), stewardship, checklist. Gains for every model tested except o3 and o4-mini, where the significant result was cost. Probabilities are written by the LLM in prose, not by code. No single-role ablation exists. It also uses a debate-like panel, which conflicts with G9.
- Over-ordering: GPT-3.5 radiology sensitivity 0.96-0.98 and specificity 0.13-0.23 on real ED visits. Exam precision for reasoning models 22.8-41.8%.

### 6.5 What changed behaviour, by how much

| Change | Effect |
|---|---|
| Handing over all numbers | LLM follows Bayes (a15, c10) |
| Stepwise prompt (name event, write rule, substitute) | Conditioning errors 10-17/20 to 0/20 |
| Reasoning model (o1) | Fixes one miscalibrated case; no general gain on probability estimates |
| Separate elicit-and-compute | F1 59%, over 30% above verbalised GPT-4 (non-medical, older models) |
| Information-gain question choice | +37 to +38 points vs naive; +2 to +28 vs a splitting heuristic |
| Stop rule on EIG | About 50% fewer tests |
| Confidence gating | +22.3% over plain asking |
| Prompt restraint on ordering | Almost none |
| More free turns | +2 to +5 points, loops |

### 6.6 Limits on this evidence

Nearly all LLM studies are single-model vignettes. Results drift between model versions. Most pre-date 2025. The key medical benchmarks (SDBench, MedR-Bench) use hard cases with no healthy patients, so false-positive costs are not measured. Rare-disease benchmarks are enriched, and PPV collapses at realistic prevalence (d12).

## 7. What our agent should take

Schema parts: G = guardrail, S = state, O = operator. Evidence ids refer to the folder's evidence files and claims K01-K26.

### Add now (established)

| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| A1 | **Code does every posterior.** Probability updates, base-rate arithmetic and normalising over exclusive hypotheses run in code, not in the model's head. The model supplies inputs and reads outputs. | G5 | [E] | K01, K02, K08, K09; a05, b02, a12, a15, c10 |
| A2 | **Ask for inputs as separate fields**: prior or reference class, per-finding LR or Se/Sp, what each is conditioned on. Do not ask for a one-shot "probability that" when the number must be recalled. Models follow Bayes when numbers are given and use similarity otherwise. | G5 / S1 | [E] | K08; a15, b14, c10 |
| A3 | **Treat the model's recalled probabilities as noisy.** Never trust a single recalled LR or pretest. Single values can be several-fold off and shrink toward 1. | G5 / S7 | [E] for unreliability (3 lines); the LR dispersion figures are single-source | K09, K19; a13, a14, d06 |
| A4 | **Store any test accuracy number as a range with setting and design flags.** Published sensitivity and specificity are inflated by case-control design (RDOR 3.0) and shift with prevalence (0-40 points). | G5 / S7 / memory | [E] | K20; d08-d11 |
| A5 | **Run a test only if some result could change the action** (compute the post-test position for each outcome against the action threshold). | S7 | [E] for the principle; the threshold formulas are our derivation | K03; a02, b01, d18 |
| A6 | **Do not use the model's stated confidence to stop or to gate.** Already in 4b. | G5 / S7 | [E] | K26; d22 |
| A7 | **Do not add debate to the test chooser.** Reported scaffold gains are bundled with a debate-like panel; G9 stays. | G9 | [E] | K15; a16, d04 |

Note. A prompt form for any probability question (name the event, name the conditioning facts, write the rule with abstract symbols, then substitute) cut ChatGPT's conditioning errors to 0/20 (K11, c03). It is single-source (one 2023 model), so it sits under Test first (T11 below), not here.

### Test first (not yet established)

| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| T1 | Elicit-then-compute vs one-shot posterior at equal tokens | G5 | [S] | K25; d07, d06 |
| T2 | Threshold-gated S7 (compute L and U from stated costs) vs always-test | S7 | [S] | K03, K04, K22; d16, d17, d18 |
| T3 | EIG test choice with run outcomes vs halving heuristic vs model-chosen test | S7 | [C] | K14; d02, d03, a17 |
| T4 | Interval LRs with decision-flip check | G5 / S7 | [S] | K19, K20; d06, d08-d11 |
| T5 | Group correlated tests and cap the combined LR | G5 / S7 | [S] | K21; d13-d15 |
| T6 | Counts format vs probability format in prompts | G5 | [S] | K05, K24; d01, d23 |
| T7 | Odds+LR form vs counts for chained evidence | G5 | [C] | K06; b19 |
| T8 | Belief state kept in code across steps vs model-held | G5 / memory | [S] | K13; a19, c17 |
| T9 | Stop rule: posterior margin vs EIG floor vs loop guard | S7 / S9 | [S] | K23; d04, d17, d24 |
| T10 | Code-gated test request vs always ask vs verbal-confidence gate | S7 | [S] | K16; c19, d25 |
| T11 | Stepwise abstract-symbol setup plus label-match check (named disease vs finding) | S2 / G5 | [S] | K10, K11; b09, c03 |
| T12 | Corpus-count prior as second signal | G5 | [S] | K17; a18 |
| T13 | Test-chooser role ablated alone | S7 | [S] | K15; a16, d04 |

Full test specs in section 8 and UNKNOWNS.md.

## 8. Concrete tests on our bench

All tests use both arms at equal total tokens (setup, retries and code-call overhead counted, G7). Use at least 3 seeds. Report mean, spread, and cost per correct answer. Models: at least one small and one frontier, since results drift and shrinkage differs.

| Test | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 elicit-then-compute | Casscells and Morgan-style vignettes with new numbers (so memory cannot help); text problems with 2-4 evidence items | (a) one-shot posterior in prose; (b) model fills prior and LR fields, code computes | Absolute error vs the true posterior; share within 5 points | b beats a on new numbers; gap smaller on textbook numbers (memorised) |
| T2 threshold gate | Tasks with stated test cost, wrong-answer cost and a fixed simulator | (a) always test until budget; (b) code computes L and U from stated costs and gates | Accuracy, tests ordered, tests that could not change the action, cost | b matches accuracy with fewer tests; stated cost shifts behaviour as predicted (K04) |
| T3 EIG with run outcomes | ARC-style or BRAINTEASER-style items with two candidate rules and a runnable discriminating input | (a) model picks the test; (b) halving heuristic; (c) EIG over candidate outcomes computed by running | Accuracy at equal tokens; number of tests | c at least equal to b; both beat a. If c does not beat b by 3 points, keep b (simpler) |
| T4 interval LRs | Vignettes with table LRs plus perturbed LRs | (a) point LR; (b) interval with decision-flip check | Decision accuracy; share of flips where more evidence is requested | b requests more evidence only on flips and keeps accuracy |
| T5 grouped tests | Items with 2-3 results sharing a driver (two imaging results of one lesion) | (a) multiply all LRs; (b) group and cap | Brier score against a generated truth with known correlation | b is less overconfident when tests correlate; no loss when independent |
| T6 counts vs probability | New-number Bayes problems | (a) probabilities; (b) counts in the prompt; (c) either, with code arithmetic | Accuracy | Smaller gap than in people; c dominates both. Tests whether format matters at all once code is present |
| T7 odds/LR vs counts for chains | Two- and three-test sequential problems | (a) counts; (b) odds+LR; each with and without code | Accuracy | With code, no difference; without code, b better for chains (as Schulz) |
| T8 belief in code | 5-round evidence accumulation tasks | (a) model keeps belief in text; (b) code keeps belief | Agreement with an exact Bayesian reference at round 5 | b near 100%; a plateaus after round 1 (K13) |
| T9 stop rules | Fixed simulator with a turn cap | (a) posterior margin; (b) EIG floor; (c) loop guard only | Accuracy and tests used | One rule wins by 2+ points, or equal accuracy at fewer tests |
| T10 gated asking | Interactive items where extra information costs | (a) always ask; (b) ask if code-computed uncertainty is above a threshold; (c) ask if verbal confidence is low | Accuracy, number of asks | b > a; c not better than b (K26) |
| T11 setup and label check | Vignettes with a mismatched label (bacteriuria described as UTI) plus medical-name Bayes problems | (a) plain; (b) stepwise abstract setup; (c) b plus a check that the named disease matches the finding | Conditioning-error rate; pretest error | b cuts conditioning errors; c cuts mislabel error |
| T12 count prior | Multiple-choice diagnosis | (a) model alone; (b) model plus count prior with agreement flag | Accuracy where the two agree vs disagree | Agreement subset more accurate (64.7% vs about 47% in a18) |
| T13 chooser ablation | SDBench-like or our own sequential items | Full scaffold; scaffold without chooser role; chooser role only | Accuracy and cost | Shows how much of the MAI-DxO gain is the chooser |

Controls. Include a plain-model arm in every test. Include one item set with no signal to catch scaffolds that invent confidence. Record every code call and every ordered test (S9 log).

## 9. What does not transfer, and why

- **Human frequency effects.** The natural-frequency boost is a story about people recoding numbers. With code doing the arithmetic, format is a design choice, not a fix. LLMs also look strong on textbook counts problems (d23), so the human effect size should not be expected.
- **Clinician base-rate neglect numbers.** 18-23% correct is a human figure. GPT-4 matches clinicians on one case and beats them on four, so human rates do not predict model errors. Model errors differ in kind: label framing, recalled numbers, version drift.
- **Pauker-Kassirer cost units.** Utilities for life, harm and regret have no analogue in puzzle tasks. The structure (two cut points on belief) transfers. The units must be replaced with token cost and wrong-answer cost.
- **Test sensitivity and specificity.** For code and puzzle tests, a test is run, not estimated. Outcomes are exact. Spectrum bias, case-control inflation and prevalence shift matter for retrieved medical or factual priors, not for runnable checks.
- **Disease prior.** Most of our tasks have no population prevalence. The prior has to come from the problem class pass rate (S0 gate) or the count of live candidate rules.
- **Independence among tests.** The chaining problem is real for correlated evidence. For runnable tests on separate inputs it mostly disappears.
- **MAI-DxO numbers.** NEJM cases, an LLM gatekeeper, no healthy patients, a bundled panel with debate. Do not read "79.9% at $2,396" as the value of a Bayesian chooser.
- **Clinician-AI interaction results** (K18). Context only.
- **Fine-tuning results** (Bayesian teaching, ALFA). Outside the no-training constraint.
- **20 Questions numbers.** The answerer is a simulated LLM and the target set is closed. EIG gains are likely inflated for open tasks.
- **Pretest from embeddings** (c08). Needs training a classifier.

## 10. Open questions

1. Does computing the posterior in code from separately elicited prior and LRs beat one-shot posteriors at equal tokens on 2025-2026 models? No direct head-to-head.
2. How do current models (GPT-5, Claude 4+, Gemini 2.5+) do on the Morgan vignettes after Rodman 2023?
3. Does a counts format help LLMs when code is not available? Does it matter when code is?
4. Do odds/LR beat counts for chained tests in LLMs, as in students?
5. What error does the independence assumption cause in LLM chained updating? No LLM or human chaining study found.
6. Do LLMs obey a test or treatment threshold when told the costs? What fraction of ordered tests could not change the action?
7. EIG vs a halving heuristic at equal tokens when outcomes are run rather than simulated.
8. Which stop rule is best: posterior margin, EIG floor, or certainty threshold? What does stopping early cost?
9. Does keeping LRs as ranges change decisions in a controlled test? Only the TB yield example exists (10.8-19.1%).
10. What does the test-chooser role contribute inside MAI-DxO alone?
11. Original numbers of Eddy 1982, Gigerenzer and Hoffrage 1995, Fagan 1975 and Kassirer 1989 are unverified. Pauker-Kassirer and Sox have no captured numeric threshold values.
12. Is the off-the-shelf range for belief updating 36-58% or 37-58%? It was read off a figure and is unresolved.
13. Is the LR accuracy in d06 memorisation of TheNNT?

Search limits. WebSearch ran out during the gap search, and the arXiv, Semantic Scholar and OpenAlex APIs were rate-limited. Discovery used Europe PMC and direct opens. Some gaps may be open only because search was limited.

## 11. Sources

[V] = opened this session. "abstract" means only the abstract page was read. [M] = snippet or memory only.

**Foundations**
- [V, abstract] Pauker and Kassirer (1975) Therapeutic decision making: a cost-benefit analysis. https://pubmed.ncbi.nlm.nih.gov/1143303/ (a01)
- [V, abstract] Pauker and Kassirer (1980) The threshold approach to clinical decision making. https://pubmed.ncbi.nlm.nih.gov/7366635/ (a02, b01, b26, d18)
- [V, abstract] Sox et al. (1986) Probability theory in the use of diagnostic tests. https://pubmed.ncbi.nlm.nih.gov/3079637/ (a03)
- [V, abstract] Sox et al. (1989) Threshold analysis using diagnostic tests with multiple results. https://pubmed.ncbi.nlm.nih.gov/2664405/ (a04)
- [M] Eddy (1982) Probabilistic reasoning in clinical medicine. https://doi.org/10.1017/CBO9780511809477.019 (a22)
- [M] Gigerenzer and Hoffrage (1995) How to improve Bayesian reasoning without instruction. https://doi.org/10.1037/0033-295X.102.4.684 (a23)
- [M] Fagan (1975) Nomogram for Bayes's theorem. https://pubmed.ncbi.nlm.nih.gov/1143310/ (a24)
- [M] Kassirer (1989) Our stubborn quest for diagnostic certainty. https://pubmed.ncbi.nlm.nih.gov/2497349/ (a25)
- [M] Berner et al. (1994) Four computer-based diagnostic systems. https://pubmed.ncbi.nlm.nih.gov/8190157/ (c23)
- [M] Heckerman et al. (1992) Pathfinder evaluation. https://pubmed.ncbi.nlm.nih.gov/1547627/ (c24)

**Human base-rate and frequency work**
- [V] Casscells et al. (1978) via Manrai et al. (2014), JAMA Intern Med. https://pmc.ncbi.nlm.nih.gov/articles/PMC4955674/ (a05, b02, b03)
- [V, abstract] Hoffrage and Gigerenzer (1998) Acad Med. https://pubmed.ncbi.nlm.nih.gov/9609869/ (a06)
- [V, abstract] Hoffrage et al. (2000) Science 290:2261. https://pubmed.ncbi.nlm.nih.gov/11188724/ (a07)
- [V, abstract] McDowell and Jacobs (2017) meta-analysis, Psychol Bull. https://pubmed.ncbi.nlm.nih.gov/29048176/ (a08)
- [V, abstract] Why can only 24% solve Bayesian reasoning problems (2018). https://pubmed.ncbi.nlm.nih.gov/30369891/ (a09)
- [V] Hoffrage, Krauss, Martignon, Gigerenzer (2015) Front Psychol. https://pmc.ncbi.nlm.nih.gov/articles/PMC4604268/ (a10, d21)
- [V, abstract] Gill, Sabin and Schmid (2005) BMJ. https://pubmed.ncbi.nlm.nih.gov/15879401/ (a11)
- [V] Weber, Binder and Krauss (2018) Front Psychol. https://pmc.ncbi.nlm.nih.gov/articles/PMC6194348/ (b17, b18)
- [V] Schulz et al. (2025) BMC Med Educ. https://pmc.ncbi.nlm.nih.gov/articles/PMC11980142/ (b19, b20, b27)
- [V] Visualizations to improve Bayesian reasoning: a review (2023). https://pmc.ncbi.nlm.nih.gov/articles/PMC10059693/ (b21, b22)
- [V] Fenwick, Campitelli and Thompson (2026) Psychon Bull Rev. https://pmc.ncbi.nlm.nih.gov/articles/PMC13481750/ (b23-b25)

**Practitioner probability estimates**
- [V, abstract] Morgan et al. (2021) JAMA Intern Med, PubMed page. https://pubmed.ncbi.nlm.nih.gov/33818595/ (a12)
- [V] Morgan et al. (2021), full text. https://pmc.ncbi.nlm.nih.gov/articles/PMC8022260/ (b04-b07)
- [V, abstract] Diagnosis (2026) Accuracy of emergency physicians' probability estimates for ACS. https://doi.org/10.1515/dx-2026-0020 (d20)

**Thresholds**
- [V, abstract] Djulbegovic et al. (2015) threshold hypothesis. https://pubmed.ncbi.nlm.nih.gov/26639018/ (a20)
- [V, abstract] Djulbegovic et al. (2015) dual processing. https://pubmed.ncbi.nlm.nih.gov/26244571/ (a21)
- [V, abstract] Diagnosis (2026) Determining the testing threshold. https://doi.org/10.1515/dx-2025-0146 (d19)

**Test-accuracy bias and dependence**
- [V, abstract] Lijmer et al. (1999) JAMA. https://pubmed.ncbi.nlm.nih.gov/10493205/ (d08)
- [V, abstract] Leeflang et al. (2013) CMAJ. https://pubmed.ncbi.nlm.nih.gov/23798453/ (d09)
- [V, abstract] Mulherin and Miller (2002) Ann Intern Med. https://pubmed.ncbi.nlm.nih.gov/12353947/ (d10)
- [V, abstract] Swab-based TB spectrum-bias modelling preprint (2026). https://doi.org/10.64898/2026.07.02.26357020 (d11)
- [V, abstract] Commentary on spectrum bias in LLM rare-disease diagnostics (2026). https://doi.org/10.21203/rs.3.rs-10042099/v1 (d12)
- [V, abstract] Johnson et al. (2017) Stat Med. https://pubmed.ncbi.nlm.nih.gov/27730659/ (d13)
- [V, abstract] Dendukuri and Joseph (2001) Biometrics. https://pubmed.ncbi.nlm.nih.gov/11252592/ (d14)
- [V] Own calculation, 2026-11-01 (D:/research_scratch/E01.08/tmp/dep_E01.08.py) (d15)

**LLM studies**
- [V] Rodman et al. (2023) JAMA Netw Open. https://pmc.ncbi.nlm.nih.gov/articles/PMC10714249/ (a13, b08-b11, c04, c05)
- [V] Brodeur et al. (2024) o1-preview. https://arxiv.org/abs/2412.10849 (a14, c06, c07)
- [V, abstract] Brodeur et al. (2026) Science. https://doi.org/10.1126/science.adz4433 (d26)
- [V] Li and Rui (2024) Dual traits in probabilistic reasoning. https://arxiv.org/abs/2412.11009 (a15)
- [V] Weisenthal (2023/2024) ChatGPT and post-test probability. https://arxiv.org/abs/2311.12188 (b12, b13, c01-c03)
- [V] Talboy and Fuller (2023). https://arxiv.org/abs/2304.01358 (b14, c10)
- [V] Gao et al. (2024) Next-word probability is not pre-test probability. https://arxiv.org/abs/2411.04962 (c08, c09)
- [V] Paruchuri et al. (2024) What are the odds? https://arxiv.org/abs/2406.12830 (c25)
- [V] Araya (2025) Chains of thought and natural frequencies. https://arxiv.org/abs/2503.15268 (d01)
- [V] Sci Rep (2026) LLM diagnostic likelihood ratios. https://www.nature.com/articles/s41598-026-61766-2 (d06)
- [V] Feng et al. (2025) BIRD. https://arxiv.org/abs/2404.12494 (d07)
- [V] Qiu et al. (2025/2026) Bayesian teaching. https://arxiv.org/abs/2503.17523 (a19, b15, b16, c17, c18)
- [V] Jia et al. (2025) Counting clues. https://arxiv.org/abs/2512.12868 (a18)
- [V] Hu et al. (2024) Uncertainty of Thoughts. https://arxiv.org/abs/2402.03271 (c14, c15, d02)
- [V] Choudhury et al. (2026) BED-LLM. https://arxiv.org/abs/2508.21184 (c16, d03)
- [V] Ruhrberg Estevez et al. (2025) ACTMED. https://arxiv.org/abs/2510.18988 (a17)
- [V] Nori et al. (2025) Sequential diagnosis, MAI-DxO. https://arxiv.org/abs/2506.22405 (a16, c11-c13, d04)
- [V, abstract] Nori et al. (2026) Science. https://doi.org/10.1126/science.aeh7930 (d05)
- [V] Li et al. (2024) MediQ. https://arxiv.org/abs/2406.00922 (c19, d25)
- [M] Li et al. (2025) ALFA. https://arxiv.org/abs/2502.14860 (c20)
- [M] Tu et al. (2024) AMIE. https://arxiv.org/abs/2401.05654 (c21)
- [M] Goh et al. (2024) LLM influence on diagnostic reasoning RCT (abstract via Europe PMC). https://pmc.ncbi.nlm.nih.gov/articles/PMC11519755/ (c22)
- [V] Williams et al. (2024) LLMs for ED recommendations, Nat Commun. https://pubmed.ncbi.nlm.nih.gov/39379357/ (d16)
- [V] Qiu et al. (2025) MedR-Bench. https://arxiv.org/abs/2503.04691 (d17)
- [V, abstract] AAN 2026 abstract, Gemini 2.5 Pro vs ChatGPT-5. https://index.mirasmart.com/AAN2026/PDFfiles/AAN2026-005045.html (d22)
- [V, abstract] Behav Res Methods (2026) LLM canary in online data. https://doi.org/10.3758/s13428-026-03184-w (d23)
- [V, abstract] Cureus (2026) Case mix and protocol in diagnostic LLM conversations. https://doi.org/10.7759/cureus.118344 (d24)

Note on open flags. The evidence files mark several sources opened:true where only the abstract was read (Pauker-Kassirer, Sox, Djulbegovic and others). Full-text opens were Manrai, Morgan (PMC), Rodman, Brodeur 2024, Nori 2025, Weisenthal, Qiu, Hu, Choudhury, Hoffrage 2015, Weber, Schulz and the Sci Rep LR paper. Everything else rests on abstracts.
