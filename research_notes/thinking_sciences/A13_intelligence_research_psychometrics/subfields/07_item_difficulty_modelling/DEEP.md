# Item difficulty modelling: deep document

*Subfield A13.07 (intelligence research, psychometrics). Key works: Embretson; Carpenter, Just and Shell. Why it matters for our agent: S0 (cheap difficulty estimate) and G12 (spend by difficulty). Built from evidence_a-d.jsonl (ids a01-a25, b01-b27, c01-c26, d01-d20), claims.jsonl (K01-K27) and critique.md in this folder. Corrections from critique.md are applied here; where a raw evidence line is wrong, this file says so. Status marks follow SCHEMA.md: [E] established, [S] single-source, [C] contested.*

---

## 1. What it is

Item difficulty modelling asks one question. Can we predict how hard a test item is before anyone answers it?

"Hard" has to be pinned to a number. The studies use different targets:

- Classical p-value: the share of test takers who get the item right.
- Rasch or IRT b parameter: difficulty on a latent scale.
- Error rate or response time in a lab study.
- For LLM work: the pass rate of a model, or of a pool of models.

"Predict" also has several meanings:

- **Explain.** Fit a model on items you already have, and see how much variance the features account for. This is the old psychometric goal (Carpenter 1990, Embretson 1998).
- **Generate to target.** Build new items whose difficulty is known in advance, with no pretest. This is the Embretson Cognitive Design System (CDS) and automatic item generation.
- **Screen.** Predict difficulty of existing items from text (2015-2026 NLP work).
- **Allocate.** Use a difficulty signal to decide how much compute to spend on a problem (2025-2026 LLM test-time work).

For our agent only the last meaning matters in the end. S0 is a gate that runs before the solve. It looks up the problem class and picks a mode: direct, short reason, step-by-step, checked, or open. G12 says to spend budget by difficulty. This subfield is the psychometric basis for both, and it tells us how good a cheap difficulty estimate can be, how it fails, and what it costs.

The main message, in short:

1. Difficulty is a function of countable task features. Rule count in matrices is the founding case. [E]
2. Such models explain about half the variance on real items, not most of it. [E]
3. Asking a model "how hard is this?" is a weak signal. Having a model fill named feature slots, or sampling a few cheap attempts and counting, is much better. [E]
4. Difficulty for humans is not difficulty for models. The target must be the solver in use. [E]
5. A pre-solve difficulty signal improves accuracy at equal budget, but only by a few points, and only if the probe cost is counted. [E for the gain, S for agent loops]

Links to parallel subfields (not covered here): Value of information; Expected value of control; Intrinsic load and element interactivity (the cognitive-load side of "rule count"); Ecological rationality, adaptive toolbox; Planning by tree search with pruning; Structure mapping (SME); MDL program synthesis on ARC; Outside view and base rates (the class-level pass rate in S0 is an outside-view prior).

---

## 2. History and theories in depth

### 2.1 Before Embretson: difficulty as a fact about items

Classical test theory treats difficulty as the item p-value. IRT (Rasch 1960, Lord 1980) puts item difficulty and person ability on one scale. Both are measured by giving the item to people. Neither says why an item is hard. Expert ratings of difficulty were the usual stand-in, and they are poor: content experts correlated with IRT difficulty as low as r = .38 (Conejo et al. 2014, cited in Peters et al. 2025; a12, b02). This is the first reason to model difficulty at all. [E]

### 2.2 Carpenter, Just and Shell (1990): the founding process model

The paper "What one intelligence test measures" (Psych Review 97:404-431) gave the first full process account of one item type, the Raven Progressive Matrices (a01-a07, d15).

The theory:

- Solving a matrix means finding the rules that govern change across rows, then applying them to fill the gap.
- There are five rule types: constant in a row, quantitative pairwise progression, figure addition or subtraction, distribution of three values, distribution of two values.
- Each separate rule instance is a **rule token**. A problem with three tokens needs three sub-goals held and managed at once.
- The authors argue that more tokens tax **goal management** in working memory, not rule induction. Their quote: "a larger number of rule tokens taxes not so much the processes that induce the rules, but the goal-management processes."

The data:

- Exp 1a: 12 college students, 34 of 48 Raven items shown, 32 classified. Rule tokens accounted for **57%** of variance in mean error rate (45% if constant rules are counted).
- Error by token count: one-token problems about 16% error; three- or four-token problems about 59%. Table 3 rows: pairwise progression 1 token 6% (Exp 1a) and 9% (Exp 1b); two different rules 48% and 54%; distribution of 3 values with 3 tokens 66% and 77%. Exp 1b used 22 students.
- Mean correct response time correlated r = .87 with error rate across items. This matters for us: **cost spent on an item is a difficulty readout.**
- Item ordering is stable across samples: the college sample versus Forbes (1964) norms r(25) = .91; a control group of 19 without eye tracking matched at r(25) = .93 (errors) and .89 (times). Absolute error depends on the sample (25-33% here).
- A separate goal-management task predicted Raven errors: Tower of Hanoi errors versus Raven errors r(43) = .77 (45 students); among subjects within 1 SD of the Raven mean, r(32) = .57.
- Error trials omitted a critical attribute 59% of the time versus 20% on correct trials. The authors attribute about half of errors to incomplete encoding or analysis. So there are two difficulty sources: encoding completeness and goal management.

The models:

- FAIRAVEN (production system) solved 23 of 34 problems, the median of the 12 students. Per-problem point-biserial of human error with FAIRAVEN success r(32) = .67.
- BETTERAVEN adds abstraction (distribution-of-two-values) and a goal monitor (15 productions). It solved all but the 2 unclassifiable problems, like the best subject.
- Lesion runs: limiting BETTERAVEN to 4 rule types cost 8 problems; limiting to 5 types cost 4. Failures fell mainly on many-token problems.

Limits, from critique.md: the 57% and r = .87 are confirmed in the 1990 text (d15), but rest on 12 students and 32 items. The models were built on the same problems they were scored on, so there is no held-out test. We found no larger-sample replication of the 57% figure. Treat "rule count is a major driver" as well supported in direction and shaky in magnitude.

### 2.3 Embretson: from explanation to design

Susan Embretson turned the explanatory model into a design method, the **Cognitive Design System** (CDS) (a09, a10, b20, b21, d14):

1. Model the solving process (for matrices, reuse the Carpenter model).
2. Derive stimulus features that the model says affect difficulty.
3. Fit a psychometric difficulty model (the LLTM: linear logistic test model) that sets item difficulty as a weighted sum of feature scores.
4. Use it to predict difficulty of new items, generate items to target difficulty (software ITEMGEN), then recalibrate.

For her matrix work Embretson added three binary perceptual features to the Carpenter set: object overlay, fusion, distortion. The reason: the 1990 model has no perceptual-encoding or decision stage. An early student-written bank had three cognitive-operation dimensions explaining roughly 40% of difficulty, 60% unexplained (that 40% is the early bank, not CDS). The review (Yang et al. 2022) also notes that Embretson (1998) and Carpenter (1990) disagree on how much type-of-rule and perceptual organisation matter.

What we could open:

- **Embretson and Daniel (2008)**, GRE quantitative items (d14): 534 undergraduates, 101 analysed Problem Solving items. A five-stage model (encoding, integration, planning, execution, decision) gave hierarchical-regression R2 = .451 (bank difficulty) and .435 (sample difficulty). Encoding alone: .126 and .107. LLTM delta fit .724. Sample vs bank difficulty r = .834. Only "generating equations" and "extensive processing of distractors" were significant in both difficulty estimates. The authors say higher prediction is reported only for items generated by varying features of an item model.
- **Embretson's own 1995, 1998 and 2004 papers were NOT opened.** All CDS content for those is second-hand via Yang et al. (critique.md, weak spot). The "attrition up to 50%" (Embretson 2004) is second-hand (a22).

### 2.4 Rule-structured items: when features work best

Sun, Liu and Luo (2019, b19): 92 generated number-series items (7 dropped), 466 students. An LLTM with 10 features explained **77%** of variance (r = .88) in-sample; at the 18 item-model level r = .97. Two-step items had mean difficulty 1.28 versus -0.70 for one-step.

Contrast: a 23-item generated matrix set given to 307 participants in three countries had difficulty "partly predicted from the number and type of rules ... but far from enough for psychometric applications" (a10). In another generator, items with distracting attributes were "much more difficult" than the Advanced Progressive Matrices items.

Reading of the contrast (ours, not tested): when every item comes from a few item models with few free parameters, features fit very well. When items are made by hand or from open rule spaces, distractors, perception and idiosyncrasy leave about half unexplained. ARC-style tasks are in the second group.

### 2.5 The text-based era (2010s to 2025)

With NLP, difficulty prediction moved from process features to text features. Peters et al. (2025) review 37 studies to May 2025 (a11, b01, b22, b23, b25):

- Pearson r over 17 values: .04 to .87, mean .545, SD .225.
- R2 over 13 values: .208 to .788, mean **.478**.
- RMSE on p-value: .165-.268 (mean .216, 6 studies). On Rasch b: .354-1.295 (mean .740, 8 studies).
- Exact classification accuracy: .325-.806 (mean .567, 3 studies). Adjacent accuracy .65 and .982 (2 studies). Errors are usually off by one level.
- Loukina et al. (2016): over 100 linguistic features with a random forest gave r = .50 with CTT delta.
- One study: engineered features RMSE .302 versus fine-tuned BERT embeddings .614 (small data). Another: 5-7% RMSE gain over BERT baselines on large maths item sets.
- Metric mess: RMSE in 31.8% of metric uses, Pearson 19.3%, R2 about 14.8%, Spearman 4.5%; 18 unique metrics. Studies cannot be compared directly.
- LLM-generated features appeared only 6 times (4.55% of feature uses). Earlier reviews stop at 2022.

Plain reading: a typical text predictor explains about half the variance. The best published numbers are ceilings from small or in-sample sets.

### 2.6 The 2024-2026 LLM wave

Four threads (details in sections 3 and 6):

1. **Ask the LLM directly.** Weak to moderate, often near zero within a level.
2. **Have the LLM extract features, then fit a regressor.** Better.
3. **Simulate students and fit IRT.** Works with aggregation or alignment; weak zero-shot.
4. **Use the model's own signals** (uncertainty, hidden state, sampling disagreement, reasoning cost). Small but real, and the base for equal-budget allocation.

The newest thread connects difficulty to compute allocation (UAB, AdaCompute, Predictive Scheduling, Liu et al.). This is the thread S0 and G12 actually need.

---

## 3. Core findings with exact numbers

Status: [E] established (two or more independent sources), [S] single-source, [C] contested. Claim ids K01-K27 refer to claims.jsonl.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Rule tokens drive Raven difficulty | 57% of error variance (45% with constant rules); error about 16% at one token vs about 59% at three or four; 12 students, 32 items | Carpenter et al. 1990 (a01, a02, d15); Webb et al. 2023 (c20); Yang et al. 2023 (a08) | [E] direction, [S] magnitude (K01) |
| Response time tracks error rate across items | r = .87 across problems; norms r(25) = .91; control group r(25) = .93 | Carpenter et al. 1990 (a03) | [S] (K16, partly) |
| Goal management is the limiter | Tower of Hanoi vs Raven errors r(43) = .77; r(32) = .57 in middle band; N about 45 | Carpenter et al. 1990 (a07) | [S] |
| Encoding failures cause about half of errors | error trials omitted a critical attribute 59% vs 20% on correct trials | Carpenter et al. 1990 (a05) | [S] |
| Process model predicts which items are hard | FAIRAVEN solved 23/34, point-biserial with human error r(32) = .67; no held-out items | Carpenter et al. 1990 (a04) | [S] |
| Rule count and type are not enough | 23-item generated set, 307 people: "far from enough"; early bank about 40% of variance | Yang et al. 2022 (a09, a10) | [E] (K02) |
| Cognitive-complexity model on real GRE items | R2 .451 / .435 in-sample, 101 items, 534 students; delta fit .724 | Embretson and Daniel 2008 (d14) | [E] with text reviews (K02) |
| Rule-structured generated items fit well in-sample | LLTM 10 features R2 .77 (r .88), 92 items, 466 students | Sun et al. 2019 (b19) | [S] (in-sample) |
| Text-based difficulty prediction is moderate | r mean .545 (.04-.87, N=17); R2 mean .478 (N=13); RMSE on Rasch b mean .74 (N=8); accuracy mean .567 (N=3) | Peters et al. 2025 (a11, b01) | [E] (K03) |
| Expert ratings are weak | experts vs IRT r as low as .38 | Conejo 2014 via Peters (a12) | [E] with LLM direct ratings (K04) |
| Direct LLM rating: weak, varies by setting | ENEM rho .31-.37 (best prompt, 10 LLMs, 1,031 items); NAEP math r -.14 to .14; 20-model mean rho under .50; course questions rho .06 | Brant 2026; Acquaye 2026; Li 2026; An and Wang 2026 | [E] (K04) |
| Direct rating can look good when pooled | K-5 pooled r .83 math, .81 reading (N = 5,170) vs within-grade R2 .003-.23 | Razavi and Powers 2025 (a13, c03) | [E] that pooling flatters; [S] on size (K06) |
| LLM fills feature slots, code regresses | math RMSE .83 vs .91 direct vs 1.01 dummy; r .87 vs .83; GBM -18.5% RMSE vs dummy | Razavi and Powers 2025 | [E] (K05) |
| LLM features lift over embeddings | holdout Pearson .7791 with LLM features vs .6822 embeddings only; 250,000+ responses | Hoyl 2026 (c16) | [E] with Razavi (K05) |
| One cheap feature family carries most signal | Kapoor: linguistic r .76, embeddings r .76, all r .77, RMSE .59 vs .92 baseline (1,076 items) | Kapoor et al. 2026 v2 (a15, c01) | [E] (K14) |
| Within-level prediction is much weaker | grade K worse than dummy; grade 1 math R2 .003; within-grade r .37-.70 | Razavi and Powers 2025 (a23, c03) | [S] (K06) |
| LLM uncertainty is a small cue | RMSE gain .02-.03: Biopsychology .1361 vs dummy .1667; USMLE .2868 vs .3110; CMCQRD .1654 vs .1833 | Zotos et al. 2025 (a16, b06) | [E] (K08) |
| Uncertainty vs student answer distributions | present but weak; every model distribution differs from students (451 questions) | Zotos et al. 2025 (a17, b07) | [E] (K08) |
| Hidden-state probe reads model failure | ScienceQA ROC-AUC 93.09, Macro-F1 79.48 (7B model); cross-domain drop | Zhu et al. 2025 (b17, c09, c10) | [S] white-box |
| Probes: human vs model difficulty | human IRT Spearman .83-.87; model's own pass rate .40-.64; IRT vs model difficulty .65 to .45 as reasoning rises; probe AUROC .78 to .64 | Lugoloobi et al. 2026 (d08) | [E] with Li (K10) |
| Stronger models call more items easy | GPT-5 labelled 89.3% of medium items easy and none of the hard items hard (56.9% of hard called easy); GPT-4.1 QWK .578 (temp 0); fine-tuned ConvBERT QWK .625 | Wang et al. 2026 (a18, a24, b14); corrected per critique.md | [E] (K09) |
| Bigger is not better | GPT-5 rho .34 vs GPT-4.1 .44; Gemma beat Llama and Qwen at simulation | Li 2026; Acquaye 2026 | [E] (K09) |
| Human vs model difficulty differ | Savant rate 70.4% USMLE, 32.2% SAT Math (hard-for-human items solved by over 90% of models); open multimodal LLMs within -8.7% to +7.3% of chance on matrices humans solve at 95.9% | Li 2026 (b09); arXiv 2401.12117 (c21) | [E] (K10) |
| Simulated classrooms, aggregated | NAEP r up to .75 / .76 / .82 (grades 4/8/12); 300 students; n = 50 enough for iteration | Acquaye et al. 2026 (b10, b11, c07, c08) | [C] (K07) |
| Zero-shot simulation is weak; alignment helps | SMART PCC .649 vs zero-shot .265 (Smarter Balanced); CodeWorkout .308-.393; kNN baseline PCC .596 | Scarlatos et al. 2025 (a19, b12, c05, c06) | [S] / [C] (K07) |
| Persona prompting unstable alone | persona changed accuracy under 1%; ensemble averages help | Li 2026 (b09, b27) | [C] (K07) |
| Own labels reflect formatting | label vs empirical rho .06; label vs Bloom rho .90 (378 authored, 311 deployed, 7,888 responses) | An and Wang 2026 (c17) | [S] with Easy2Hard (K12) |
| GPT-4 pairwise vs IRT | Spearman .612 GSM8K, .218 ARC, .164 Winogrande; matching accuracy .922/.825/.771 on large-gap pairs | Ding et al. 2025 (c14) | [E] (K12) |
| Pairwise beats absolute for ranking | most configurations, 3 LLMs, 6 maths domains | Kolesnikova et al. 2026 (b16) | [S] (K13) |
| Rank metric vs error metric | mean predictor RMSE 1.19, rho 0 | Brant 2026 (b15, c11) | [E] (K17) |
| Averaging correlated raters | professors averaged: no gain; model ensemble SAT Math .56 to .66 peak, dilutes after K = 14 | Zotos 2025 (b26); Li 2026 (b08) | [E] (K18) |
| Probe/estimator needs per-domain and per-model fit | agent difficulty model AUC .67-.74 on held-out benchmark vs base rate .57-.64, oracle .91; BEA USMLE RMSE .29 vs .31 | Ge et al. 2026 (d16); Zhu 2025; Yaneva 2024 via Kapoor (c02) | [E] (K19) |
| Absolute pass-rate thresholds | easy 50-100%, medium 10-50%, hard 0-10% Pass@1; Qwen2.5-72B Pass@1 above 80% on 76.2% of MATH-500 | Liu et al. 2025 (c19) | [E] (K11) |
| Equal-budget gain from a pre-solve signal | UAB +2.3 average (up to +5.5), none significant at N = 16; AdaCompute +4 to +6 on MATH; Predictive Scheduling +7.9 on GSM8K | d01, d05, d07 | [E] (K21) |
| Probe can cost more than it saves | k = 10 routing 1.38x always-large; k = 5 dominates (cost 9.8-11.6 vs 12.0; accuracy .508-.520 vs .484) | Pishehvar et al. 2026 (d03, d04) | [S] (K22) |
| Few samples suffice | K = 2 vote entropy AUROC .780; k = 5 AUROC .865 vs k = 10 .862; k = 3 lost about .07 | d02, d04 | [E] (K23) |
| Process cost of a first attempt is a signal | trace length vs human item time rho .16-.30; within item d > 0 for all five thinking models (humans d = -0.10); interaction -0.66 log units; Epi2Diff +8.1% relative gain | Wang 2026 (b13, d12) | [E] (K16, K25) |
| Mid-run state predicts success (symbolic ARC solvers) | held-out AUC .765; early stop saves 33.6% compute at 98.9% solve rate kept | Pendharkar 2026 (d13) | [S] non-LLM (K25) |
| Follow-up questions read finished-answer reliability | AUROC .73-.79 (GSM8K, CodeContests); verbal confidence .42-.55 | Sam et al. 2025 (d18) | [S] (K27) |
| Free baseline must be scored | regex difficulty AUROC .839/.830 vs entropy .830/.867 on synthetic arithmetic | d04 | [S] (K26) |
| ARC human difficulty is weakly tied to simple features | grid size vs difficulty r(398) = -.16 (training), -.02 (evaluation); 784 and 948 participants | LeGris et al. 2024 (d11) | [S] (K24) |
| No published ARC-AGI-2 human vs model per-task correlation | 407 participants, 13,405 attempts, 62% solved; models 0.9-3.0% | Chollet et al. 2025 (c22, d10) | [S] absence (K24) |
| Feasibility of simulating adaptive testing | LLTM needs R2 about 75% to match calibrated Rasch at RMSE .4 | Luo and Yang 2024 (a21, b24) | [S] (K15) |

---

## 4. Mechanisms and models

This section explains each mechanism so that an engineer can implement it. The agent's difficulty gate (S0) is the target.

### 4.1 The LLTM (linear logistic test model)

The LLTM sets the Rasch difficulty of item i as a weighted sum of feature values:

    b_i = sum_k (q_ik * eta_k) + c

- q_ik is how much of feature k item i has (a count or a 0/1 flag), set by the item designer or by a coder.
- eta_k is the difficulty contribution of one unit of feature k, estimated from response data.
- Fit quality is reported as R2 or the delta fit index.

For engineering: this is a linear regression of measured item difficulty on a feature matrix. In our setting the "measured difficulty" is the agent's own pass rate on each item, and the features are the ones in section 4.2. The LLTM adds nothing mathematically over a ridge regression on logit(pass rate); the value is the **discipline of choosing features from a process model**.

### 4.2 Feature set for S0 (from the matrix tradition)

Candidates (a01, a08, a09, d14):

- Number of rule tokens or sub-goals to hold at once (Carpenter). Count in code if the task is structured; ask the model to list distinct rules and count the list in code if not.
- Rule type mix (for example pairwise progression is easy, distribution-of-three is hard).
- Number of elements per cell (Mulholland 1980).
- Perceptual organisation: overlay, fusion, distortion (Embretson).
- Distractor load and irrelevant attributes (Embretson and Daniel; Yang 2022).
- Encoding stage: the number of attributes that must all be noticed (Carpenter: 59% of errors omitted one).
- Equation generation, extensive processing of distractors (the two variables significant in both of Embretson and Daniel's difficulty estimates).

Count features in code where possible. Where the feature needs reading, ask the model to fill a named slot and let code regress (section 4.3).

### 4.3 Slot-fill then regress (the pattern with the best evidence)

Razavi and Powers (c04) and Hoyl (c16):

1. Define named slots (for example: steps required, concepts used, likely misconceptions, number of distinct rules, amount of distraction).
2. For each item, call the LLM at temperature 0 to fill the slots. The model does no scoring.
3. Fit a random forest, GBM or ridge on the slot values, against measured difficulty, on a labelled set.
4. Predict new items with the fitted regressor. Code, not the model, outputs the number.

Evidence: math RMSE .83 (RF) and .81 (GBM) versus .91 direct versus 1.01 dummy; r .87 versus .83. Hoyl: LLM features lift holdout Pearson from .682 to .779. Metadata-only (grade) RF scored 1.12 and TF-IDF RF 1.01, so surface text counts do not carry the gain. Caveat: Razavi's numbers are pooled across grades; within-grade r was .37-.70.

This pattern matches our rule that the model fills slots and code decides.

### 4.4 Pass-rate probe (measure instead of judge)

Instead of predicting from features, run the solver a few times and count. This is the Liu et al. and UAB approach (c19, d01, d02, d04):

1. Draw K cheap samples of the problem (K = 2 to 5).
2. Compute pass rate if a check exists, or vote entropy (disagreement among answers) if not.
3. Bin by absolute thresholds: easy 50-100% Pass@1, medium 10-50%, hard 0-10% (Liu).
4. Route: easy -> direct or short; medium -> best-of-N or checked; hard -> tree search or open mode, but only if there is a foothold (G12).

Key facts for implementation:

- Reuse the probe samples in the final vote. UAB gets its gain partly because phase-1 samples still count.
- K = 2 gave AUROC .780 versus phase-1 correctness; K = 5 matched K = 10 (.865 vs .862); K = 3 lost about .07 in one test (so K = 3 and K = 5 are not interchangeable; test).
- Cost accounting is mandatory: at k = 10 on a 12x model pair routing cost 1.38x always-large (d03).
- The signal measures difficulty **for this model**, not for humans.
- Hardest items gain least: when the right answer never appears in the samples, extra samples do not help. UAB gains were +2.3 (L1), +3.4 (L2), +1.6 (L3), +1.1 (L4), +1.5 (L5).

### 4.5 Text-feature classifier for allocation (AdaCompute)

A gradient-boosted classifier on 16 cheap text features (length, numbers, fractions, multi-step words, one entropy estimate from a single call) predicts the best sample count (d05). It trains in under a second on N = 200, tracks a Lagrangian oracle within about 1 point, and gained +4 to +6 points over uniform on MATH. A prompt-length heuristic gained only +0.3 to +1.2. Requires offline labelled data from the same task family. It is the API-friendly version of a trained difficulty prior.

### 4.6 Process-cost signals from the first attempt

- Tokens used by a first attempt: across items only rho .16-.30 with human item time (d12), but within an item a longer trace means failure (wrong-minus-right d > 0 for all five thinking models).
- Failed traces had 0.43 more hedge words after controls.
- Mid-run grid structure in symbolic ARC solvers: held-out AUC .765; early stop at 50% of the run saved 33.6% of beam-search compute at 98.9% of solve rate (d13). This is not an LLM result.
- Epi2Diff (b13): features of how a reasoning trace is spread over problem-solving states gave +8.1% relative gain over supervised fine-tuning for human difficulty classification. Needs a full solve.

Implementation: log tokens per attempt and revision loops. Use "this attempt has run past the item's median first-attempt length" as an escalate or restart trigger (to be tested; K25).

### 4.7 Follow-up question probe (API-only reliability)

Sam et al. (d18): after the model answers, ask a fixed bank of follow-up questions, collect the answers' features, and train a linear predictor of correctness. AUROC .73-.79 on reasoning tasks for GPT-3.5 and GPT-4o-mini versus verbal confidence at .42-.55. It predicts the correctness of a finished answer, not the difficulty of a new problem, and needs training per model.

### 4.8 Simulated students plus IRT

Acquaye et al. (b10, c07, c08): prompt a model to play a class of students (300: 75/105/75/45 by proficiency, with diverse names), collect their answers, fit IRT on the simulated responses, read item difficulty. Pooled correlations up to .75 / .76 / .82 for grades 4 / 8 / 12; direct prompting -0.139 to 0.137. Small classes (n = 50) suffice for iteration; ensembling raises correlation; a weaker model (Gemma) beat a stronger one (Llama-3.3-70B at 92% accuracy simulated poorly). For our agent this is just "run many varied cheap attempts" with an IRT or pass-rate readout.

SMART (a19): align the simulator to IRT with DPO. Zero-shot simulation PCC .265; SFT .562; SMART .649. It needs real response data, so it is not a scaffold-only method.

### 4.9 Difficulty by propagation (EIP)

Zhang et al. (c18): 30 models, 35,550 questions. A question is hard if many strong models fail it, and a model is strong if it passes hard questions; the two scores propagate until stable. 90% agreement with human judgments; compute 0.006 versus 1,783 for 1PL-IRT. Relative to the model pool. Useful if we keep a table of results across many past items.

### 4.10 Adaptive-testing view: the estimate is a prior

Luo and Yang (a21, b24): when difficulty comes only from features (LLTM), extra items are needed to reach the precision of a calibrated Rasch model. The extra-item cost falls as R2 rises (fit y = 100x^2 - 206x + 106.5 at RMSE target .4). To keep test length at or below 30 with 8 extra items, R2 of at least 75% is needed. Typical text models (R2 about .48) are below that. Practical reading: S0's feature estimate is a prior; update it with outcomes of the first attempt and the checks.

---

## 5. What holds up

### 5.1 Replications and meta-analyses

- **Meta-level:** Peters et al. (2025) is a systematic review of 37 studies, not a meta-analysis with a pooled effect. It gives ranges and means (r mean .545, R2 mean .478), but no pooled effect size and no moderator test (b22). [E] that text-based prediction is moderate.
- **Embretson-style explanation:** Embretson and Daniel (2008) on GRE items found R2 .435-.451, near the text-review mean. This is independent of Carpenter's matrix data. [E] that about half the variance is explainable.
- **Rule count:** the Carpenter finding is supported in direction by Webb et al. (2023): GPT-3 shows human-like effects of rule number (more unique rules harder, human OR 0.61) and relation type (progression harder, OR 0.41), but the human-vs-model pattern match is modest, r(30) = .39, p = .027 (c20). The review by Yang et al. (2023) lists number of elements and rules as drivers in several human studies. No large-sample direct replication of 57% was found. [E] direction, [S] size.
- **Direct LLM difficulty is weak:** six independent sources (K04). Razavi's high pooled r is the exception, and critique.md reads it as a pooling artefact (not tested directly).
- **Slot-fill beats direct:** two sources (Razavi, Hoyl). Within-level reproduction is not found (gap 3 open).
- **Stronger models call more items easy:** five sources. This is a ceiling effect, not an understanding effect (critique.md).
- **Equal-budget allocation gains:** three independent methods. All use math sets.

### 5.2 Failures and boundary conditions

| Boundary | Evidence |
|---|---|
| Pooling over levels inflates correlation | Razavi: pooled r .81-.87 vs within-grade R2 .003-.23 (the .003-.23 are for the direct estimate, not the feature model; the feature model's within-grade r is .37-.70). Math grade K: RMSE after rescaling worse than the dummy, yet regression R2 .132. Both true; do not quote one as the other (critique). |
| Knowledge-heavy items | BEA 2024 USMLE: best RMSE .29 vs dummy .31 (c02); top 10 teams within .009 of each other |
| Generated item sets | 23-item set, 307 people: "far from enough"; some APM transformations could not be generated |
| Hand-built item banks | Embretson 2004 attrition up to 50% (second-hand, a22) |
| Visual items | RMSE +1.26 (SD .95) on image items in 56/76 model-prompt pairs, Hedges g = -.17; may be transcription loss (c12) |
| Cross-domain transfer | probe AUROC .78 to .64 across reasoning level; agent difficulty model AUC .67-.74 on new benchmark vs oracle .91 |
| Extremes | Jain: estimates compressed toward the middle, extremes under-represented; UAB gains smallest at the hardest level |
| Ceiling | GPT-4o and o1 got 98.8% and 99.1% on SARA reading items vs humans 87.6%; no difficulty variance to read (c15) |
| Constant shift | fixing bias on ENEM reduced RMSE but did not change rank (c12) |
| Probe cost | k = 10 routing 1.38x always-large (d03) |
| Large budgets | UAB: at N = 16 no setting significantly favours UAB |
| White-box requirement | hidden-state probes (Zhu, Lugoloobi, Predictive Scheduling) cannot be used with a closed API |

### 5.3 Moderators

- **Item type:** structured, rule-governed items give higher R2 than free-text knowledge items.
- **Aggregation:** simulated classes work when aggregated (n = 50 to 300 students) and fail when single (Li: persona changes accuracy under 1%).
- **Model strength:** stronger models are worse at simulating students and judging difficulty (ceiling).
- **Prompt and temperature:** GPT-4.1 at temperature 0 gave QWK .578 versus .447 at default settings (accuracy .618 versus .535). Same-skill in-context examples helped GPT-5 but not GPT-4.1. Prompt wording shifted results as much as switching model on ENEM.
- **Reasoning effort:** raising it lowers agreement between human IRT difficulty and the model's own difficulty (.65 to .45).
- **Reasoning prompts:** raised rho by up to .19 for open-weight models, not for GPT-4o (b15).
- **Thinking mode:** Qwen3-32B thinking scored lower than non-thinking on cognitive feature labels (62.6/56.3 vs 65.4/58.6; a20).

### 5.4 What worked and what did not (interventions)

Worked:

- Slot-fill then regress (Razavi, Hoyl).
- Fixing temperature to 0 and using same-skill examples (Wang).
- Aggregating many varied attempts (Acquaye).
- Reusing probe samples in the final answer (UAB).
- Absolute pass-rate thresholds for routing (Liu).
- Pairwise comparison for ranking (Kolesnikova; single source).
- Token-probability soft ratings plus labelled examples: Raina lifted rho from .41 to .48 (cited in b16).
- Training a small SVM on ~40 items with LLM uncertainty (b05).

Did not work or only weakly:

- Asking the model for a number or label directly.
- Self-assigned Easy/Medium/Hard labels (rho .06).
- Zero-shot student simulation without alignment (PCC .265).
- Persona prompting alone.
- Averaging correlated raters (professors; models after K = 14).
- A prompt-length heuristic for allocation (+0.3 to +1.2).
- Stacking estimators (embeddings add little over linguistic features; basic text features add nothing once embeddings exist).
- Constant-shift recalibration for rank (fixes bias only).

### 5.5 Methodological cautions from the critique

- Many evidence lines are the same paper (Razavi x4, Wang x3, Acquaye x4, Peters x6). Independent-source counts in claims.jsonl count papers, not lines.
- Three Zotos papers are one lab. Wang, Jiao, Li, Peters, Zhou share authors.
- The professor study has about 10 test items per exam; Spearman .853 is unstable (b05).
- Difficulty targets differ by study (p-value, Rasch b, human pass rate, model pass rate). Cross-study r comparison is loose.
- Evidence a18 misreads the Wang et al. confusion table (see section 6). GPT-5.4 hit rates were not rechecked.
- c26 is a synthesis line, not a source.
- Seen only at abstract or snippet level: Webb r(30) = .39 (grep), Kolesnikova tables, Jain correlations, RIDE human validation, Hoyl (single dataset), EIP "90% agreement" definition.

---

## 6. Language models

### 6.1 How LLMs behave when asked about difficulty

Direct judgment, summarised (c26 corrected):

| Setting | Result |
|---|---|
| ENEM, 1,031 items, 10 LLMs | best-prompt Spearman about .10-.37; o3 .37, Claude-4-Sonnet .33, GPT-4o .31, Gemini-2.0-Flash .31 (Gemini-2.0-Flash reaches .37 only in the math subset; "Gemini-2.5-Flash .35" in b15 could not be found in Table 3 and is unverified) |
| ENEM mean predictor | RMSE 1.19, rho 0. Model RMSE 1.70-2.25. Low RMSE can hide zero rank power. |
| NAEP math, 631 items | direct prompting -0.139 to 0.137 |
| 20 models, 4 datasets (Li) | zero-shot Spearman average under .50; SAT Math about .41; USMLE about .13; predictions bunch low (variance collapse) |
| Reading and Writing, 3 levels (Wang) | GPT-4.1 QWK .578 at temperature 0 (accuracy .618); .447 and .535 at default settings; ConvBERT .625; best feature model .549 |
| K-5 pooled (Razavi) | direct math r .83, RMSE .91 (dummy 1.01) |
| Course questions (An and Wang) | label vs empirical rho .06 |
| Pairwise (Ding) | GPT-4 vs IRT Spearman .612 GSM8K, .218 ARC, .164 Winogrande |
| Epi2Diff baselines | prompted LLMs gave negative R2: GPT-5 zero-shot on Cambridge R2 -10.8 (RMSE 33.7); GPT-4o zero-shot on USMLE R2 -0.25 |

### 6.2 Correction to the Wang et al. confusion table (critique.md)

In Wang et al. (2026) rows are the true level and columns are the predicted level (easy, medium, hard). For GPT-5 the rows read: easy 100/0/0; medium 89.33/10.67/0; hard 56.92/43.08/0. So GPT-5 labelled **89.3% of medium items easy and none of the hard items as hard**. The evidence line a18 says "medium 89.3%, hard 43.1%" as hit rates. That is wrong. The hit rate on hard is 0% and on medium 10.7%. GPT-4.1's hard hit rate of 43.1% and medium hit rate of 85.3% are right. The GPT-5.4 figures (easy 96.1%, medium 92.0%) were not re-checked and are probably also the share predicted easy. The conclusion (stronger models call most items easy) stands and is stronger than first written. [E] (K09)

### 6.3 Why stronger models judge worse

- Items that are hard for humans are easy for models (Savant rate 70.4% USMLE; 32.2% SAT Math, rho .386). The model's own correctness-based difficulty matches human difficulty even worse than its stated estimates (b09).
- Models cannot be role-played down to a weaker student: a proficiency persona changed accuracy by under 1%.
- Models agree with each other more than with humans (machine consensus).
- The explanation in the critique is a ceiling effect: if the solver passes nearly everything, its pass rate has no spread (SARA: 98.8% and 99.1% accuracy; c15). This is not a deeper failure of understanding.
- Model AUROC of confidence for its own errors is mostly .50-.60, with highs of .73 (GPT-5, Cambridge) and .64 (DeepSeek-R1, USMLE).

### 6.4 What changed LLM results, and by how much

| Change | Effect |
|---|---|
| Slot-fill + RF instead of direct number | RMSE .91 to .83 (-9%); r .83 to .87 (pooled) |
| LLM-extracted features added to embeddings | Pearson .682 to .779 (+.097) |
| Temperature 0 instead of default | QWK .447 to .578 (GPT-4.1) |
| Simulation + aggregation instead of direct | r about 0 to .75-.82 |
| DPO alignment of simulator | PCC .265 to .649 |
| Add first-token uncertainty to text features | RMSE -.02 to -.03 |
| Ensemble of 14 models | SAT Math rho .56 to .66; dilutes after K = 14; USMLE falls at once |
| Pairwise instead of absolute | better in most configurations (no table recorded) |
| Reasoning prompts | up to +.19 rho for open-weight models; none for GPT-4o |
| Higher reasoning effort in the solver | human-IRT vs model difficulty correlation .65 to .45 |
| Image items (converted to text) | RMSE +1.26 |

### 6.5 LLMs on rule-structured puzzle items

- Webb et al. (2023, c20): GPT-3 on digit matrices (40 UCLA undergraduates as comparison) beat average humans: generative OR 1.88 (CI 1.21-2.91), multiple choice OR 6.27. Human-like difficulty effects (more unique rules harder, progression harder, spatially permuted logic harder). Pattern match r(30) = .39, p = .027. Modest.
- Open multimodal LLMs near chance on matrix puzzles in 2024: within -8.7% to +7.3% of random on IQ50, -1.0% to +0.6% on RAVEN-S, -5.6% to +6.4% on CCSE, versus humans 95.9% (SD 6.92) on 20% of IQ50 (c21). 2024-era models.
- ARC-AGI-2: difficulty is human pass rate (407 participants, 515 sessions, 1,848 test pairs, 13,405 attempts, 62% solved, median 2.3 min per attempt; public, semi-private and private sets matched to within 1 point; every kept task solved by at least 2 humans). At release model scores were 0.9-3.0% (o3 medium 3.0%, o4-mini 2.4%, ARChitects 2.5%, Claude 3.7 8K 0.9%), so there was no variance to correlate with human pass rate (K24). [S] absence.
- ARC-AGI-1 (H-ARC): 784 and 948 participants, success in 3 attempts 76.2% (training), 64.2% (evaluation), 98.8% of tasks solved by at least one person. Output grid size vs difficulty r(398) = -.16 and -.02. Error divergence vs success rate r = -.81 and -.88. People's and machines' error profiles correlate about .25 (GPT-4o .19, Claude 3.5 .20): they make different errors.
- Reasoning-trace length vs human item time rho .16-.30 across 400 items (4,091 human trials); DeepSeek-V3 non-thinking -.05.

Nobody has tested Carpenter-style rule counts against model pass rates on ARC (gap 2). That is the most direct test for our bench.

### 6.6 Equal-budget allocation results with LLMs

| Method | Signal | Access | Gain at equal budget |
|---|---|---|---|
| UAB (d01, d02) | vote entropy, K = 2 | black-box | +2.3 avg (up to +5.5); none significant at N = 16; 14 of 15 settings positive for main models; beats ASC no longer on two larger models |
| AdaCompute (d05) | 16 text features + 1 entropy call | API OK (DeepSeek-V3, GPT-4o-mini) | MATH DeepSeek-V3 B = 2.0: .562 vs .517 (cost 1.87 vs 2.00), oracle .571; B = 3.0: .575 vs .517 (cost 2.73 vs 2.00, not equal cost); GPT-4o-mini .512 vs .474; Qwen2.5-7B .554 vs .491; GSM8K DeepSeek-V3 .965 vs .946 |
| Predictive Scheduling (d07) | MLP on hidden states | white-box (text LoRA version API-compatible) | GSM8K up to +7.9 points; closes over 50% of gap to oracle |
| Warm-up allocation (d06) | 1 sample per question | API OK | token efficiency highest on all five benchmarks; numbers only in figures |
| Probe-guided routing (d09) | linear probe | white-box | MATH: matches GPT-OSS-20B-high accuracy (92%) at 70% lower cost; AIME 2025 37% lower cost |
| IRT-Router (d17) | IRT on query embeddings | black-box route over 20 LLMs | +3% over GPT-4o alone at 1/30 cost in-distribution |
| CODA (d19), Learning When to Think (d20) | pass rate during RL | training | CODA: over 60% fewer tokens on easy tasks; d20: -41% length on MATH500, accuracy .782 vs .796 |
| Pishehvar (d03, d04) | semantic entropy, k samples | black-box | k = 5 dominates always-large; k = 10 costs 1.38x |

No study gates depth inside a multi-step agent loop (K21, K22).

### 6.7 Transfer and staleness

- Agent Psychometrics (Ge et al. 2026, d16): new tasks AUC .825 (embedding) and .842 (LLM judge) on SWE-bench Verified versus baseline .718, oracle .945. Held-out benchmark: SWE-bench Pro baseline .571, embedding .667, LLM-judge .696, combined .674, oracle .913. GSO baseline .637; .724 / .743 / .719; oracle .912. The authors call it "a coarse first estimate."
- Probe transfer: one setting scores .739 on MATH after training on MATH but .515 on GSM8K and .643 on AIME (row labels garbled in extraction; d09).
- No measurement of staleness across model versions was found (gap 8).

---

## 7. What our agent should take

Each item lists schema part (G / S / O / memory), status, and evidence ids. "Add now" means established by two or more independent sources and consistent with the existing guardrails. "Test first" means single-source, contested, human-only, or older-model-only; it does not enter SCHEMA.md until its test (UNKNOWNS.md) passes.

### 7.1 Add now

| # | Take | Part | Status | Evidence |
|---|---|---|---|---|
| N1 | Never use the model's own "how hard is this?" number or label as a routing input. At most use it as a coarse easy-vs-hard flag and log its error. | S0, G12 (guard) | [E] | a12, b02, b05, b08, b15, c07, c11, c17, c14 (K04, K12) |
| N2 | Define difficulty by the solver in use: the agent's own pass rate on the class, not human difficulty. | S0, memory (class record) | [E] | b09, c15, c21, d08, d10 (K10) |
| N3 | Use absolute pass-rate thresholds (easy 50-100%, medium 10-50%, hard 0-10%) in the class record, not quantile bins. | S0, memory | [E] | c19 (K11); Liu plus UAB, AdaCompute, Predictive Scheduling (K21) |
| N4 | If the model must contribute difficulty information, have it fill named feature slots and let code decide. | S0 | [E] | a13, b03, c03, c04, c16 (K05) |
| N5 | Evaluate every difficulty estimator within a task family and against a family-mean baseline. Report Spearman rho and RMSE, and include a mean-predictor baseline and a free text-only baseline. | G7 (test rule) | [E] for rank vs error (K17); [S] for within-family (K06) and free baseline (K26) | b15, c11, b23, a23, c03, d04 |
| N6 | Count probe cost in the budget. Prefer 2 to 5 probe samples. Reuse them in the final vote. | S0, G7, G12 | [E] for few samples (K23); [S] for cost break-even (K22) | d01, d02, d03, d04 |
| N7 | Treat a feature-only estimate as a prior, not a measurement. Update it with first-attempt outcomes and checks. | S0 -> S4/S5 | [S] (K15), but consistent with G2/G3 | a21, b24, a11 |
| N8 | Calibrate the S0 estimator per task family and re-calibrate when the family or base model changes. | S0, memory | [E] | c10, c02, a23, d08, d09, d16 (K19) |
| N9 | Do not stack estimators or average correlated raters. Stop adding when rank rho stops moving. | G4, S0 | [E] | a15, c01, c16, b26, b08 (K14, K18) |
| N10 | Keep an easy-item cap: do not search harder on a class with no foothold. Where all probe answers disagree, mark "maybe unreachable", do not add more of the same sampling. | G12 | [E] G12; [E] for probe at the hardest items (K23) | d02 |
| N11 | Stronger base model means re-check the S0 thresholds; a stronger model calls more items easy and its pass rate saturates. | S0 | [E] | a18 (corrected), a24, b08, b14, b15, c15 (K09) |

None of these changes a guardrail. N1 and N8 support G12; N6 sets how S0 may be built under G7.

### 7.2 Test first

| # | Candidate | Part | Status | Evidence | Why not yet |
|---|---|---|---|---|---|
| T1 | S0 gate by a 2-to-5-sample probe, then routing to shallow / checked / open, versus fixed depth at equal total tokens (probe included). | S0, G12 | [S] for agent loops (K21 is [E] on math sets) | d01, d02, d03, d05, c19 | No study in a multi-step agent loop; gains are 2-6 points, vanish at large N |
| T2 | Slot-fill difficulty (6 slots, code regress) versus a single model number versus a 3-sample pass rate, inside one task family. | S0 | [E] (K05) pooled, [S] within level (K06) | a13, b03, c16 | Razavi's gain is pooled across grades |
| T3 | Rule-count and perceptual features as predictors of the agent's own pass rate on ARC tasks, versus grid size and a length-only baseline. | S0 | [S] human-only (K01, K24) | a01, a02, c20, d11 | No test on model pass rates |
| T4 | First-attempt cost (tokens, revision loops) as an escalate-or-restart trigger. | S0/S5/S6 | [E] direction (K16, K25); [S] as rule | d12, d13, a03 | Humans and models diverge; symbolic solver only |
| T5 | Follow-up-question reliability probe before commit. | S6, S8 | [S] (K27) | d18 | Needs per-model training; older models |
| T6 | Pairwise comparison counted in code to order sub-problems. | S0, O3 | [S] (K13) | b16 | One source |
| T7 | Persona or varied-prompt probe samples versus repeated samples. | S0 | [C] (K07) | b10, b27, c08 | Contested |
| T8 | Class-level difficulty prior from the class record (outside-view prior) combined with first-attempt outcome. | S0 memory | [S] | a21, d05 | No direct agent test |
| T9 | Counting distractors and irrelevant attributes as an S0 slot. | S0, S1 | [E] for effect (K02); [S] for use in agent | a10, d14 | Not tested on model difficulty |
| T10 | A cheap free baseline for S0: regex or length-based difficulty. | S0 | [S] (K26) | d04 | Single paper |

---

## 8. Concrete tests on our bench

All arms run at equal total tokens (probe and gate tokens counted). Metrics: accuracy per 1,000 tokens; Spearman rho between estimate and measured pass rate; RMSE against a mean predictor; per-class and pooled results reported separately. Where the bench has ARC-style and BrainTeaser-style item types, use both; record the item ids with the estimate for later correlation.

| ID | Item type | Arms (equal tokens) | Metric | Expected effect |
|---|---|---|---|---|
| B1 (T1) | ARC tasks and BrainTeaser items, one held-out set per family | A: fixed depth. B: 3-sample probe, absolute thresholds route to direct / checked / open. C: random routing at the same mix as B. | Accuracy per 1k tokens; share of items escalated; miss rate on items rated easy that fail | B beats A by 2 to 6 points on the mid band; no gain on the hardest; no gain at large N. If B only ties A once probe cost is counted, drop the gate. |
| B2 (T2) | One family (for example BrainTeaser), 60+ items with known agent pass rate | A: model gives one number. B: model fills 6 slots, code regresses on a 40-item train split. C: 3-sample pass rate. D: free length baseline. | Spearman rho and RMSE vs measured pass rate on held-out items, within family | C > B > A about equal to D. Expect rho about .5 for B, about 0 for A. |
| B3 (T3) | ARC tasks with logged pass rates | Features: rule count (code or listed rules), grid size, number of objects, length-only. | Spearman with the agent's own pass rate; compare to human pass rate if H-ARC ids are available | Rule count gets rho above grid size (r about -.16 for human). If not, the Carpenter transfer fails for ARC. |
| B4 (T4) | Any checked item type | A: fixed budget per attempt. B: escalate or restart when a trace passes the item's first-attempt median. | Solved per 1k tokens; flips right-to-wrong and wrong-to-right | B saves tokens on failing long traces with no loss on solved ones; guard that G1 is satisfied by the trigger being a count, not a schedule. |
| B5 (T7) | A single family | k = 2, 3, 5 samples from the same prompt vs from 3 varied prompts | AUROC of vote entropy vs full-run correctness; probe cost | Varied prompts at least tie repeated samples; the smallest k that keeps AUROC within .02 of k = 10 |
| B6 (T5) | Checked items | Commit directly vs follow-up bank then commit or retry | Accuracy per 1k tokens; AUROC of the follow-up predictor vs verbal confidence | AUROC .7 or higher vs about .5 for verbal confidence |
| B7 (N11) | Same items, two base models (or two model versions) | Re-use the estimator fitted on model 1; refit for model 2 | Spearman and AUROC drop | Drop of .1 or more shows staleness; sets a re-calibration rule |
| B8 (T6) | Sub-problems from O3 decompositions | Absolute score vs pairwise comparison counted in code | Agreement with measured sub-problem pass rate | Pairwise better by at least .05 rho |
| B9 (T9) | Items with and without added distractors | Rule count alone vs rule count + distractor slot | Gain in rho over rule count alone | Gain of .05 or more |
| B10 (N5) | All of the above | Add a free text-only baseline and a mean predictor to each test | Estimator must beat both | Anything that does not beat the free baseline adds nothing |

Logging for each test follows SCHEMA section 6: mode chosen, path, tokens per state, transitions, doubt-step flips, operators tried, final result. Add: probe cost, estimate, and measured pass rate per item.

---

## 9. What does not transfer, and why

- **Human difficulty to model difficulty.** ARC-AGI-2 difficulty is the human pass rate. Items hard for humans are often trivial for models (Savant rate 70.4%, 32.2%); error profiles of people and machines correlate only about .25 on ARC (d11). Rule count was fitted to human error on 12 students. Test it against the agent's pass rate, never assume.
- **Working-memory interpretation.** Carpenter's account says rule tokens tax a limited goal-management store. Our agent has no fixed working memory and no eye fixations. The stack should be explicit in code. The count may still predict difficulty for models for different reasons (context length, interference), and Webb's r = .39 is only modest.
- **Time as a difficulty readout.** Humans spend longer on harder items and the correlation with error is .87. For reasoning models, trace length across items correlates only .16-.30 with human item time, and inside one item a longer trace means failure while the human relation reverses (d = -0.10). Do not read "more tokens = harder item" as a general rule.
- **Human sample-size results.** Class sizes, calibration samples and CAT simulations (R2 of 75% needed) are for testing people with pretests. Our agent can measure by running; the translation is open (gap 10).
- **Item generation to target difficulty.** Embretson's use case (generate items at a target b) is the opposite of ours. Our agent does not write test items. Attrition up to 50% (second-hand) is a caution if it ever does (generated probes or test cases).
- **IRT calibration.** IRT needs response matrices from many persons. A single agent has one "person." The alternatives (pass rate, EIP-style propagation over past results, vote entropy) are the usable analogues.
- **White-box probes.** Zhu, Lugoloobi, Brown et al. need hidden states. The text-only LoRA version and the sampling version are the API options; the former still needs per-model training.
- **Math results.** Every equal-budget gain is on MATH, GSM8K or similar. Whether routing helps multi-step agent loops, open-ended tasks or ARC is not measured.
- **Reading-test text features.** Most text models (Kapoor, Razavi, Wang, BEA) are for reading, maths MCQs or medical items with knowledge load. They do not carry to rule-induction puzzles, where grid size predicted human difficulty with r = -.16 and -.02.
- **Simulated students.** Acquaye's class simulation is evaluated against population success rates on NAEP MCQs. The agent's use is solver pass rate, so the sim reduces to "run varied attempts."
- **Ensembles of raters.** Gains from combining 14 models do not apply: one agent, one model, correlated samples (G4).

---

## 10. Open questions

1. Does a cheap pre-solve gate save tokens at equal accuracy inside a multi-step agent loop, probe cost included? (Gap 1 for agent tasks; nothing found.)
2. How well do rule-count and perceptual features predict frontier-model pass rates on ARC-AGI-1/2? Is there any per-task human-vs-model correlation on ARC-AGI-2 now that model scores are higher? (Gap 2.)
3. Are Razavi's feature-model gains reproduced within a level? (Gap 3; no replication found.)
4. Do varied prompts beat repeated samples for the probe? How many samples give a stable pass-rate rank for the model itself beyond UAB's K = 2 and Pishehvar's k = 5? (Gap 4.)
5. What do Embretson 1995, 1998 and 2004 report in numbers (variance explained, cross-validation, attrition), and has Carpenter's 57% been replicated with larger samples? (Gap 5; not opened.)
6. Can the first-pass cost (tokens, revision loops) of an API-only agent beat a feature count? (Gap 6; follow-up probes predict answer correctness, not difficulty.)
7. What is the miss rate on items rated easy that fail? Do extremes break the gate? (Gap 7.)
8. How fast does a difficulty estimate go stale when the base model changes? (Gap 8; no measurement.)
9. Is IRT or Glicko difficulty used to allocate reasoning budget in agents? (Gap 9: not found; abstract-level NeurIPS 2026 reasoning-aware IRT is evaluation only.)
10. What R2 or rho makes a difficulty prior worth its cost versus a standard budget? The CAT figure (R2 about 75%) has not been translated. A weak prompt-length heuristic (+0.3 to +1.2) versus a 16-feature classifier (+4 to +6) suggests rank quality, not R2, is the working measure (inference only). (Gap 10.)
11. Does the persona / varied-prompt finding reconcile (Acquaye vs Li)? Critique's reading (aggregation plus weak models) is not tested.
12. Is the pooled-over-levels explanation of Razavi vs Acquaye vs Brant correct? Not tested.
13. Does high stated confidence plus easy-class label hide a miss rate high enough to matter? (Wang: hard items mislabelled easy.)

---

## 11. Sources

[V] = opened and read this session (by the research agents, per evidence files); [M] = snippet, abstract or second-hand only.

**Founding and process models**

- [V] Carpenter, Just and Shell (1990) What one intelligence test measures. Psych Review 97:404-431. https://kilthub.cmu.edu/articles/journal_contribution/What_one_intelligence_test_measures_A_theoretical_account_of_the_processing_in_the_Raven_Progressive_Matrices_Test/6619121 ; https://doi.org/10.1037/0033-295X.97.3.404 (a01-a07, d15). Note: the 57% and r = .87 were confirmed in the 1990 text by the gap searcher; the first pass read the kilthub page.
- [V] Embretson and Daniel (2008) Understanding and quantifying cognitive complexity level in mathematical problem solving items. Psychology Science Quarterly 50(3):328-344 (local copy; d14).
- [M] Embretson (1995, 1998, 2004), via Yang et al. reviews. Not opened.
- [V] Sun, Liu and Luo (2019) Automatic generation of number series reasoning items of high difficulty. https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2019.00884/full (b19)
- [V] Luo and Yang (2024) Efficiency of computerized adaptive testing with a cognitively designed item bank. Front. Psychol. 15:1353419. https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2024.1353419/full (a21, b24)
- [V] Yang et al. (2023) Computational Models of Solving Raven's Progressive Matrices. https://arxiv.org/abs/2302.04238 (a08, a22)
- [V] Yang, Sanyal, Michelson, Ainooson and Kunda (2022) Automatic Item Generation of Figural Analogy Problems. https://arxiv.org/abs/2201.08450 (a09, a10, b20, b21)

**Text-based difficulty prediction and reviews**

- [V] Peters, Zhang, Jiao, Li, Zhou and Lissitz (2025) Text-Based Approaches to Item Difficulty Modeling. https://arxiv.org/abs/2509.23486 (a11, a12, a25, b01, b02, b22, b23, b25)
- [V] Kapoor, Truong, Haber, Ruiz-Primo and Domingue (2026 v2) Prediction of Item Difficulty for Reading Comprehension Items. https://arxiv.org/abs/2502.20663 (a15, c01)
- [M] Yaneva et al. (2024) BEA shared task on USMLE item difficulty, via Kapoor (c02, opened: false).
- [M] Conejo et al. (2014); Loukina et al. (2016), via Peters (b02).

**LLM difficulty estimation**

- [V] Razavi and Powers (2025) Estimating Item Difficulty Using LLMs and Tree-Based ML. https://arxiv.org/abs/2504.08804 (a13, a14, a23, b03, b04, c03, c04)
- [V] Zotos, van Rijn and Nissim (2025) Are You Doubtful? https://arxiv.org/abs/2412.11831 (a16, b06)
- [V] Zotos, van Rijn and Nissim (2025) Can Model Uncertainty Function as a Proxy for MCQ Difficulty? https://arxiv.org/abs/2407.05327 (a17, b07)
- [V] Zotos et al. (2025) NLP Methods May Actually Be Better Than Professors. https://arxiv.org/abs/2508.03294 (b05, b26)
- [V] Wang, Jiao, Li, Peters, Choi, Zhou and Xu (2026) Can LLMs Really Understand Item Difficulty Levels? https://arxiv.org/abs/2607.28634 (a18, a24, b14; a18 corrected)
- [V] Li, Chen, Xiao, Chen, Jiao and Zhou (2026) Can LLMs Estimate Student Struggles? https://arxiv.org/abs/2512.18880 (b08, b09)
- [V] Acquaye, Huang, Carpuat and Rudinger (2026) Take Out Your Calculators. https://arxiv.org/abs/2601.09953 (b10, b11, b27, c07, c08)
- [V] Scarlatos, Fernandez, Ormerod, Lottridge and Lan (2025) SMART. https://arxiv.org/abs/2507.05129 (a19, b12, c05, c06)
- [V] Hwang, Kim and Lee (2026 v2) Can LLMs Estimate Cognitive Complexity of Reading Comprehension Items? https://arxiv.org/abs/2510.25064 (a20)
- [V] Wang, Li, Zeng, Li, Jiao, Zhou and Zhou (2026) Epi2Diff. https://arxiv.org/abs/2606.28186 (b13)
- [V] Brant, Kuhn and Pang (2026) Estimating Exam Item Difficulty with LLMs: ENEM. https://arxiv.org/abs/2602.06631 (b15, c11, c12)
- [V] Kolesnikova, Fedyanin, Hofman, Brinkhuis and Bolsinova (2026) LLMs as Experts. https://arxiv.org/abs/2605.18562 (b16; exact tables not recorded)
- [V] Jain, Hollander, He, Tang, Zhang and Sabatini (2025) Reading Comprehension Question Difficulty. https://arxiv.org/abs/2502.17785 (b18, c15; no correlation recorded)
- [V] Hoyl (2026) Synthetic Student Responses. https://arxiv.org/abs/2602.00034 (c16)
- [V] An and Wang (2026) Student Use of LLMs and the Limits of AI-Generated Question Difficulty. https://arxiv.org/abs/2609.27063 (c17)
- [V] Zhang et al. (2026) EIP. https://arxiv.org/abs/2602.12424 (c18)
- [V] Ding et al. (2025) Easy2Hard-Bench. https://arxiv.org/abs/2409.18433 (c13, c14)
- [V] RIDE (2025) https://arxiv.org/abs/2511.04120 (c24; no human validation checked)

**Hidden-state and probe signals**

- [V] Zhu, Liu, Lin, Tong, Zhong and Shao (2025) The LLM Already Knows. https://arxiv.org/abs/2509.12886 (b17, c09, c10)
- [V] Lugoloobi, Foster, Bankes and Russell (2026) LLMs Encode Their Failures. https://arxiv.org/abs/2602.09924 (d08, d09)
- [V] Brown, Muppidi and Shahout (2026) Predictive Scheduling. https://arxiv.org/abs/2602.01237 (d07)
- [V] Sam, Finzi and Kolter (2025) Predicting the Performance of Black-box Language Models with Follow-up Queries. https://arxiv.org/abs/2501.01558 (d18)

**Compute allocation by difficulty**

- [V] Liu et al. (2025) Can 1B LLM Surpass 405B LLM? https://arxiv.org/abs/2502.06703 (c19)
- [V] Nguyen, Gupta and Le (2026) Uncertainty-Aware Budget Allocation (UAB). https://arxiv.org/abs/2605.26849 (d01, d02)
- [V] Pishehvar, Morandi and Viswanathan (2026) Evaluating Escalation Signals for LLM Routing. https://arxiv.org/abs/2610.07354 (d03, d04)
- [V] Zhai, Li, Xiao, Li and Wang (2026) AdaCompute. https://arxiv.org/abs/2604.14853 (d05)
- [V] Zuo, Zhou and Zhu (2026) Adaptive Test-Time Compute Allocation with Evolving In-Context Demonstrations. https://arxiv.org/abs/2604.21018 (d06; numbers from figures not extracted)
- [V] Song et al. (2025) IRT-Router. https://arxiv.org/abs/2506.01048 (d17; tables not extracted)
- [V] Wu, Xie, Zhang and Xiao (2026) CODA. https://arxiv.org/abs/2603.08659 (d19; accuracy tables not extracted)
- [V] Kassenaar, Yang and Francois-Lavet (2026) Learning When to Think. https://arxiv.org/abs/2608.20256 (d20)
- [V] Ge, Kryvosheieva, Fried, Girit and Hariharan (2026) Agent Psychometrics. https://arxiv.org/abs/2604.00594 (d16)

**ARC and matrix puzzles**

- [V] Chollet, Knoop, Kamradt, Landers and Pinkard (2025) ARC-AGI-2. https://arxiv.org/abs/2505.11831 (c22, c23, d10)
- [V] LeGris, Vong, Lake and Gureckis (2024) H-ARC. https://arxiv.org/abs/2409.01374 (d11)
- [V] Wang (2026) Humans Disengage, Reasoning Models Persist. https://arxiv.org/abs/2606.26502 (d12)
- [V] Pendharkar (2026) Structural Grid Descriptors Predict Within-Task Solver Success on ARC-AGI. https://arxiv.org/abs/2606.09026 (d13)
- [V] Webb, Holyoak and Lu (2023) Emergent analogical reasoning in large language models. https://arxiv.org/abs/2212.09196 (c20; r(30) = .39 seen by grep only)
- [V] The Curious Case of Nonverbal Abstract Reasoning with Multi-Modal LLMs (2024). https://arxiv.org/abs/2401.12117 (c21)

**Search-gap notes**

- [M] Search gap record: no Embretson-style CDS in an LLM agent loop found (c25). Under a limited search; the web quota ran out twice. Not a source.
- Evidence c26 is a synthesis line, not a source.
