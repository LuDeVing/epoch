# Single-process versus two-process accounts of induction and deduction: deep document

Scope: whether judgments of "is this argument valid?" (deduction) and "is this argument plausible or strong?" (induction) come from one process with two cutoffs, or from two processes. Built from evidence files a-d (ids a01-a27, b01-b29, c01-c27, d01-d18), the claims file (K01-K27) and the cross-check (critique.md). Evidence ids in brackets point to those files. Related deep documents in this series (mental models, Wason, content effects, belief bias, dual process) are not repeated; the overlaps are noted where they arise.

Reading note on honesty: three central papers were never opened in full (Rips 2001; Stephens, Dunn and Hayes 2018 in Psychological Review; Heit and Rotello 2010). Their content is known through papers that were opened. This is marked throughout.

## 1. What it is

The question is simple. Show people the same argument. Ask one group "is the conclusion necessarily true?" Ask another "is it plausible?" Do the two questions tap one underlying sense of argument strength, with a stricter cutoff for "necessary"? Or do they tap two different kinds of thinking?

Two camps:

- **Single process (one strength scale, criterion shift).** There is one evidence variable. "Necessary" and "plausible" are two cutoffs on it. Moving the question word moves the cutoff.
- **Two process (two dimensions).** There is a logic-like signal (does the form guarantee the conclusion) and an associative or knowledge-like signal (does the conclusion fit what I know). Instructions set how much weight each gets.

Why a builder should care. Our agent will sometimes be asked, or will ask itself, "does this follow?" and sometimes "is this likely?" If these are one dial, a validity check by the same model is contaminated by plausibility, and the fix is to change the cutoff and the surrounding procedure. If they are two engines, the fix is to run two separate checks and combine them. The practical answer from the evidence is a hybrid: treat it as one shared signal with two cutoffs, but do not trust the model's own sense of validity, and get validity from a separate, content-stripped or code-run step.

The question is not settled in humans. It is partly open in models. The most useful result for the agent is not the winner of the debate. It is a set of tested facts about what moves accept rates: wording, base rates, time and token pressure, premise count, content, and model ability.

## 2. History and theories in depth

### 2.1 Rips (2001): the starting point

Rips gave two groups the same arguments. One judged deductive correctness (necessarily true). The other judged inductive strength (plausible). He found that the ordering of argument types flipped across groups. Under deduction instructions, valid-but-causally-inconsistent arguments were endorsed more. Under induction instructions, invalid-but-causally-consistent arguments were endorsed more. He tried three wordings per condition and found no differences between wordings. He read this as incompatible with a single strength scale plus shifted cutoff. [a01, b24, b03]

Status: Rips (2001) was never opened here. Hayes et al. (2018) describe the pattern as close to a single dissociation, not a true crossover: a large gap between valid-unbelievable and invalid-believable under deduction, near zero gap under induction. A state-trace re-analysis of Rips data was consistent with one dimension. So the famous crossover is weaker than its reputation. [a02, b03, b24, K20]

### 2.2 Heit and Rotello (2005, 2010): signal detection

Heit and Rotello gave the idea a testable form. If both instructions use one scale and only the cutoff differs, then sensitivity (d') should be the same under both. They call this the criterion-shift account. [a03]

They removed background knowledge in Exp 1 (letters instead of meaningful content) so that "induction subjects bring extra knowledge" could not explain the result. [b03] Details in section 3. Core result: d' was higher under deduction instructions in both experiments, ROC slopes differed, and valid items were accepted about equally often under both wordings. The wording mostly changed how many invalid items got through. [a04, a05, a06, b01, b02]

Heit and Rotello (2010) extended the design: deduction is more sensitive to validity, induction more to similarity and argument length. A two-dimension model fit and a one-dimension model did not (Monte Carlo fits). This paper was not opened; the description comes from reviews. [a11, b25, b16]

Rotello and Heit (2009), three-premise arguments, via Lassiter and Goodman: deduction hit .94 and false alarm .06 (d' 3.31); induction hit .95 and false alarm .17 (d' 2.56). [a08, b14]

The key assumption behind their rejection of one dimension: Gaussian strength distributions with equal shape for induction and deduction. Hayes et al. say there is no reason to assume this. [a13, b09]

### 2.3 Lassiter and Goodman (2012): one scale, bent by the word

They argue the modal word ("necessary", "plausible") acts as a non-linear power function of one conditional probability. Model: P(yes) = P(C|P)^beta_M x (1 - eps) + eps/2, with one exponent per modal word and eps (random responding) near .12. [a07, b14]

They ran a within-subject version: the conclusion carried the modal word, so the same people judged "necessary" and "plausible". The sensitivity gap appeared inside one person. Numbers in section 3. [a08, b13, d01]

Process story: people sample possible worlds and say yes only if the conclusion holds in every sample. "Necessary" needs more samples than "plausible", so under time pressure "necessary" looks like "plausible". The authors connect this to speeded deduction looking like induction in Heit and Rotello (2010). This was proposed, not tested there. [a10]

The authors themselves say the result "does not rule out a qualitative distinction". [d02]

### 2.4 Stephens, Dunn and Hayes: state-trace analysis

State-trace analysis (STA) plots mean induction endorsement against mean deduction endorsement over many conditions. If the points lie on one increasing curve, one latent dimension is enough. Reliable departures need two or more. The only assumption is monotonicity. A dissociation (an interaction in a standard analysis) cannot by itself prove two processes, because one latent variable mapped through different monotone functions produces the same pattern, including double dissociations. [a13, a14]

Stephens, Dunn and Hayes (2018, Psychological Review): signed difference analysis over a family of signal detection models on three data sets (including Singmann and Klauer 2011). Almost every model was rejected, including every two-dimensional model. The only model that fit all three was one argument-strength dimension with independent decision criteria for induction and deduction. They also reviewed 26 earlier studies and ran a new experiment where beliefs about base rates of valid and plausible items moved the two criteria in opposite directions. Status: abstract plus the account in Hayes et al.; the paper itself was not opened. [a19, b09, b10, d03, d17]

Hayes, Stephens, Ngo and Dunn (2018): three experiments with causal conditional arguments. Conventional analysis found the classic dissociation (validity matters more under deduction, belief more under induction). STA needed one dimension in each. Numbers in section 3. [a15-a18, b04-b08]

Stephens, Matzke and Hayes (2019): re-ran 16 datasets from 9 papers cited by Evans and Stanovich (2013) in favour of dual-process accounts. Most dissociations vanish under STA. [b11]

Stephens, Dunn, Hayes and Kalish (2020): a training test. Logic training improved discrimination of valid from invalid arguments, with different effects on induction and deduction in Exp 2, yet a one-dimension signal detection model still fit. Abstract only. [b22]

### 2.5 The critics and the rivals

- **Ashby (2019).** STA was not designed to count systems. A monotone (null) result favours neither side. The single-system conclusion was preordained by a parsimony claim. His focus is the category-learning half of the Stephens et al. database (63 studies in 28 articles), not the reasoning data. [b12]
- **Singmann and Klauer (2011).** Crossed deduction versus probabilistic instructions with validity and plausibility, looking for a double dissociation; reported as support for two modes. Stephens et al. re-analysed it: a one-dimension model with two independent criteria still fits. The dispute is whether criteria move independently, not only whether there is one scale. Not opened. [b23, a19]
- **Singmann and Kellen (2014) and Klauer and Kellen.** The signal-detection reading of belief effects depends on assumptions that cannot be identified; mean-strength shifts and criterion shifts trade off. [b20, b15]
- **Dube, Rotello and Heit (2010).** ROC analysis of syllogisms: believability changes where people put the bar, not their ability to separate valid from invalid. The classic interaction index is invalid because ROCs are curved. Contested by Klauer and Kellen (2011). Snippet only. [b26, a12]

### 2.6 Related mixing models

- **Dual-source model** (Klauer, Beller and Hutter 2010; Singmann, Klauer and Over 2014). A judgment is a weighted mix of background-knowledge probability and form-based warrant. One weight lambda. It is a mixing model, not two separate judgment systems. [a20, a21]
- **New paradigm** (Evans, Thompson and Over 2015). Drops "assume the premises are true". Norm is probabilistic: p-validity and coherence. Validity becomes a bound on uncertainty. [a23, a24]
- **Parallel processing** (Trippas, Thompson and Handley 2017). Logic and belief signals run in parallel. Which one interferes with the other depends on problem difficulty. [a25, b19]
- **Dual strategy** (Markovits 2024). Individuals prefer counterexample (model-based) or statistical reasoning. Covered by subfield 07; only noted here. [a27]
- **Memory parallels.** The same one-versus-two debate exists in recognition memory (familiarity and recollection). Recognition memory and induction fit one exemplar model under speeded judgments (Hayes and Heit 2013, N=140). [a12, a26]

### 2.7 Where the debate stands (summary)

Dissociations are real and replicable in humans. Whether they need two dimensions is contested. The most formal tests (STA, signed difference analysis) favour one dimension with two independently movable criteria. Their null results cannot rule out two latent variables with parallel effects, and the test populations are narrow (causal conditionals). Even proponents of two dimensions call the debate unsettled. [b16, K04, K05]

## 3. Core findings with exact numbers

Status key: established = two or more independent sources; single-source; contested; unverified = known only second-hand.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Heit-Rotello Exp 1 (letters): deduction wording separates correct from incorrect better than induction wording | N=40 per condition, 8 arguments. Deduction .89 correct, .22 incorrect; induction .93 / .55. d' 1.68 vs 0.93, t(78)=3.11, p<.01. Interaction F(1,78)=9.67. zROC slopes .84 vs .60 | Heit and Rotello 2005 [a04, a06, b01] | Verified in text; effect contested as proof of two processes |
| Heit-Rotello Exp 2 (category inclusion): same pattern | N=48 per condition, 16 arguments. Correct .92 vs .88; incorrect .24 vs .57. d' 1.69 vs 0.78, t(94)=4.39. Interaction F(1,94)=19.22. Typicality F(1,94)=6.91. zROC slopes .82 vs .71. Incorrect-typical .60 vs incorrect-atypical .53 under induction | Heit and Rotello 2005 [a05, b02, critique] | Verified in text |
| Wording changes the false-alarm rate far more than the hit rate | Valid accepted .88-.94 under both wordings; invalid accepted .22-.24 (deduction) vs .55-.57 (induction) | [a04, a05, b01, b02] | Established across two sources (K01) |
| Rips (2001) crossover | Not read. Reported as: deduction favours valid-unbelievable, induction favours invalid-believable. Hayes et al.: close to a single dissociation, consistent with one dimension on state-trace re-analysis | Rips 2001 via [a02, b24] | Unverified, weaker than its reputation |
| Gap reproduced within one person by one modal word | 507 recruited, 485 analysed, 10,185 judgments, 21 arguments each from a pool of 63 (36 invalid, 27 valid). Necessary: valid .82, invalid .41, d' 1.15 +/- .19. Plausible: valid .94, invalid .82, d' 0.63 +/- .27. Difference p<.05. Rips crossover not reproduced | Lassiter and Goodman 2012 [a08, b13, d01] | Single-source, full text read |
| One-scale model with word-specific exponent fits | R2 certain .60, likely .55, necessary .57, plausible .42, possible .32, probable .41. Split-half ceilings .66, .57, .70, .37, .34, .47. Best-fit noise .12 | [a09, d02] | Single-source; model incomplete (necessary .57 < .70 ceiling) |
| Rank order of arguments across modal frames | Mean Spearman .53; permutation p<.0001; model-plus-noise 95% range .49-.64 (mean .57) | [a09, d02] | Single-source; inside the one-scale prediction |
| Three-premise lab version | Deduction hit .94, FA .06, d' 3.31; induction hit .95, FA .17, d' 2.56 | Rotello and Heit 2009 via [a08, b14] | Second-hand |
| Dissociation in conditionals under standard analysis (Exp 1) | N=122, 4 groups, 16 targets. Validity x instruction chi2(1)=18.79; belief x instruction chi2(1)=13.64; both p<.001. Load no effect (all p>=.14); recall .89 low load vs .68 high. Capacity x validity chi2(1)=28.30; three-way chi2(1)=6.23, p<.01 | Hayes et al. 2018 [a15, b05] | Verified |
| State-trace needs one dimension (Exp 1) | CMR tests: load p=.25, capacity p=.43. Combined 24-condition plots p=.17 and p=.16 | [b04] | Verified; contested meaning |
| Exp 2 (verbal load) | N=110 (106 analysed). Validity chi2(1)=205.69; validity x instruction chi2(1)=19.57 (also reported 20.06), p<.001; belief x validity chi2(1)=15.51; belief x instruction marginal chi2(1)=3.27, p=.07. Load effects all p>=.10. One dimension again | [a16, b06] | Verified; load possibly too weak |
| Exp 3 (5.5 s deadline) | N=122; deadline slower than 80% of 20 pilots; prompt at 4 s. Validity effect deduction .27 vs induction .09, chi2(1)=21.15. Belief effect deduction .12 vs induction .23, chi2(1)=10.75. Unspeeded .25 vs speeded .11, chi2(1)=13.65. CMR p=.10 (partial-order p=.06). One dimension retained | [a17, b07] | Verified; partial-order p=.06 is borderline |
| Power check | Simulated true two-dimension structure (30 per cell, 8 conditions): CMR statistic 12.78, p<.001, so STA can detect that structure. Real data per-response binomial tests did not reject (Exp 1 p=.74, .75; Exp 2 p=.95, .47; Exp 3 p=.11) | [a14, b08] | Verified; other two-process structures stay invisible |
| Dual-process dissociations mostly vanish under STA | 16 datasets, 9 papers. At assumed SD .10: 6 of 16 (37.5%) significant. At SD .20 or .30: none. The 3 datasets with known SDs: all non-significant | Stephens, Matzke, Hayes 2019 [b11, critique] | Single-source (re-analysis by the same school) |
| Belief bias as criterion shift | Exp 1 N=38; Exp 2 N=40 believable, 39 unbelievable. Constant-discriminability G2(1)=0.23 p=.63 and 0.001 p=.97. Constant-criterion G2(1)=47.89 and 77.75, p<.001. Validity eta2 .35, .40 | Stephens, Dunn, Hayes 2017 [b15] | Contested (Klauer and Kellen; Singmann and Kellen) |
| ROC shape for conditionals | Pooled linear R2=99.9%; MP/AC and MT/DA curved. Linear aggregate fit better than curvilinear: G2(3)=7.95 p=.05; 10.63 p=.01; curvilinear 13.51 p<.01 | Trippas et al. 2014; Singmann and Kellen 2014 [b20, b21] | Contested |
| Disfluent font lowers accuracy | N=76. d_a 0.51 (Az 64%) vs fluent 0.92 (Az 74%), F(1,74)=6.22, p=.015, BF 3.30. Ability on accuracy F(1,72)=21.01, omega2 .23; on belief bias F(1,72)=9.59, omega2 .12 | Trippas, Verde, Handley 2014 [b18] | Single-source |
| Logic and belief interference depends on complexity | Exp 1 (N=43): MP conflict cost .30 (belief) vs .24 (logic), p=.02; MT symmetric. Exp 2 (N=82): complex syllogisms conflict hurt logic .21 vs belief .09, p=.03. Logic RT 10,718 ms vs belief 8,217 ms, d=0.42 | Trippas, Thompson, Handley 2017 [b19] | Single-source; N and cost values differ between the two extractions (a25 vs b19), so treat as unverified |
| Dual-source weight | N=30; 81% used form info (lambda>0), range .02-.70, mean .31. Model effect F(2,50)=9.79, p<.001; dual-source vs BL z=1.48, p=.14; baseline worse z=-4.17 | Singmann, Klauer, Over 2014 [a20, a21] | Single-source small N |
| Respect for validity differs by form | MP confidence-preserving; MT not. 54% gave too-large P(q|not-p); median scaling .95, mean 1.13, SD 1.18 | [a22] | Single-source |
| Showing premise and conclusion together improves validity-like checks | Hit rates in Inference group on affirmative inferences well over 80% (p-validity), ~75% (coherence); Belief group worse | Evans, Thompson, Over 2015 [a23] | Single-source |
| Property induction: length and similarity move induction more; validity moves deduction more | Qualitative summary; no new numbers | Hayes and Heit 2018; Hayes, Heit, Rotello 2014 [a11, b17] | Review level |
| Speeded induction matches recognition | N=140, 4 groups, 10 study pictures, 50 test items | Hayes and Heit 2013 [a26] | Single-source |

## 4. Mechanisms and models

Each model below is written so an engineer can code it.

### 4.1 Equal-variance signal detection (the Heit-Rotello test)

Inputs: for each wording W in {necessary, plausible}, hit rate H_W (valid items accepted) and false-alarm rate F_W (invalid items accepted). Optionally 1-7 confidence ratings.
- d' = z(H) - z(F).
- Criterion c = -0.5 x (z(H) + z(F)).
- One scale plus cutoff shift predicts d'_necessary = d'_plausible. A significant gap rejects pure criterion shift under the Gaussian equal-variance assumption.
- With ratings, build an ROC by cumulating from the strictest rating. Fit zROC slope. A slope different from 1 means unequal variance and invalidates plain d'. Use d_a or AUC instead.
- Worked example (Exp 1): H=.89, F=.22 gives d' about 1.68 (reported). H=.93, F=.55 gives about 0.93 (reported).
Caveat: d' gap plus unequal slopes can come from non-Gaussian or unequal-shape distributions. [a06, a13, b09]

### 4.2 Lassiter-Goodman one-scale modal model

- Compute p = P(C | premises) for each argument (probability the conclusion holds given premises).
- P(yes | word M) = p^beta_M x (1 - eps) + eps / 2.
- Fit one beta per word and a shared eps (about .12). beta greater than 1 makes the word stricter (necessary, certain). beta less than 1 makes it laxer (possible, plausible).
- Implied threshold density on the strength scale is beta x theta^(beta - 1).
- Prediction: rank order of arguments is the same in every frame. Test it with the mean pairwise Spearman against a simulated range from the fitted model (.49-.64 here; observed .53).
- Prediction: wording matters little for very strong arguments (valid ones, p near 1) and most for mid-strength invalid ones. Observed. [a07, b14, d02]
Implementation note: the exponent is free per word, so this is a flexible fit, not a hard test. [critique]

### 4.3 Sampling story for "necessary"

Sample k possible worlds consistent with the premises. Say yes only if the conclusion holds in all k. "Necessary" needs larger k than "plausible". With small k, "necessary" behaves like "plausible". For an agent, k maps to the number of samples or tokens spent on the check. [a10]

### 4.4 State-trace analysis

1. Build many conditions by crossing factors (validity x believability x length x premises x load or time). Aim for 12 to 24 conditions.
2. For each condition compute mean endorsement under wording A (x) and wording B (y).
3. Fit conjoint monotonic regression (Kalish, Dunn, Burdakov, Sysoev 2016): find the best monotone-increasing curve through the points under measurement error.
4. Bootstrap (10,000 samples, alpha .05) to see whether the fit is rejected.
5. If not rejected, one latent dimension suffices. If rejected, two or more are needed.
Sanity check used by the authors: simulate a two-dimension structure and confirm rejection (statistic 12.78, p<.001). Always do this power check before trusting a null. [a14, b08]

### 4.5 Signed difference analysis and the winning model

Test many signal detection models against order constraints on data across conditions. The surviving model: one strength scale S; induction response = S > c_ind; deduction response = S > c_ded; c_ind and c_ded set independently (base-rate beliefs move them in opposite directions in the new experiment). Implementation for an agent: keep one score per argument, two thresholds as parameters, and let stakes or stated base rates set each. [a19, b09, d03]

### 4.6 Two-dimension model (Heit-Rotello)

Two orthogonal evidence variables: logical correctness L and associative consistency A. Decision value = w_L x L + w_A x A, with weights set by instruction (deduction: high w_L; induction: higher w_A, plus sensitivity to length and similarity). Fit by Monte Carlo against ROC data. In an agent: two separate checks (a form-only check and a plausibility check) and a code-side weighted combination. [a11, b16]

### 4.7 Dual-source model

Prediction = lambda x {tau(x) + (1 - tau(x)) x kappa(C, x)} + (1 - lambda) x kappa(C, x). kappa is knowledge-based probability. tau is form-based warrant. lambda is the weight on form. Fit lambda per person or per item type. In the study 81% of 30 people had lambda above 0, mean .31. [a20]
Code check for valid forms (p-validity): u(conclusion) <= u(premise 1) + u(premise 2). MP and MT are p-valid; AC and DA are not. [a24]

### 4.8 Two-step SDT for belief bias

Stage 1 builds a validity evidence value. Stage 2 applies a criterion shifted by believability. A constant-discriminability model fits (G2 0.23, 0.001). Constant-criterion does not (G2 47.89, 77.75). The agent analogue: believability should move the verdict threshold only, so put a believability-blind step before the final verdict. [b15]

### 4.9 What the representation looks like in a language model

- Linear probes find a validity direction and a plausibility direction in the residual stream. Their cosine similarity is 0.48-0.64 (text) or 0.53-0.64 (figure caption; the paper contradicts itself), versus 0.10-0.13 and -0.12 to -0.17 for control concepts. [c01, critique item 8]
- Similarity predicts behavioural content effect: beta .557, p=.017, 57 model-prompt points. Prompt style beta .188, p<.001. [c01, c04]
- Cross-task steering: adding the plausibility vector flips validity judgments, and the reverse. [c02]
- Subtracting the plausibility part of the validity direction: Qwen2.5-32B content effect 0.348 to 0.072 (accuracy 81.62 to 82.21); Qwen3-14B 0.213 to 0.043 (accuracy 86.54 to 96.70); scale 1.5, layers 43 and 26. Best layer and scale were picked on the same data. [c03, critique]
- Interpretation: one shared signal that can be partly subtracted. That is not a clean single process and not two clean processes. [critique]

## 5. What holds up

### 5.1 Replicated or consistent

1. **Wording moves the false-alarm rate most.** Two separate experiments by Heit and Rotello (letters and categories) plus Lassiter and Goodman's within-subject version all show valid items accepted at high rates under both wordings and invalid items accepted far more under "plausible". This is the most solid result. [K01, a04, a05, a08]
2. **Capacity and speed.** Low capacity lowers validity sensitivity and raises reliance on belief, most under induction wording. Speeding cut validity sensitivity in both tasks. Concurrent load itself had little effect in two experiments. [K08, b05, b07, b18]
3. **Belief acts like a threshold shift.** Constant-discriminability models fit belief bias in syllogisms. LLMs show the same response-bias pattern. [K07, b15, c05]
4. **Yes-bias in models is large and prompt-dependent.** Raw-likelihood scoring made several models answer "valid" to everything. Precision 99.2% with recall 42.8% for one 80B model against precision 61.0% with recall 93.1% for another. [K22, d09, d11]

### 5.2 Disputed or failing

1. **Rips' crossover.** Not reproduced by Lassiter and Goodman (footnote). Hayes et al. call it close to a single dissociation. [d01, a02]
2. **d' gap as proof of two processes.** Reproduced by one word in one person, and fit by a one-scale model with a word-specific exponent (R2 .32-.60). But the model is flexible and incomplete (necessary R2 .57 below its .70 ceiling). [K02, K03]
3. **State-trace evidence for one dimension.** Three experiments plus a database re-analysis (6 of 16 significant at SD .10, none at .20 or .30). Weakened by: nulls favour neither side (Ashby); only causal conditionals tested; load manipulations did nothing; same research group did the re-analysis. [K04, K05, K06]
4. **ROC curvature.** Linear aggregate ROCs fit better than curved ones in one commentary; curved ROCs in another. Equal-variance Gaussian assumption is the weak link on the two-process side. [b20, b21]
5. **Dual-process dissociations in the wider literature** mostly disappear under STA at assumed SDs of .20-.30. Not exhaustive; summary statistics only; some studies had four conditions. [b11]

### 5.3 Moderators

- Problem difficulty: easy forms (MP) show logic hurting belief judgments more; the hardest (three-term syllogisms) show belief hurting logic more. [b19, K09]
- Form type: people keep validity for MP and drop it for MT. Negative-form inferences (MT, DA) are where plausibility-minded reasoners fail most. [a22, b21]
- Argument length and item similarity move induction more than deduction. [a11, b17]
- Natural predicates (enzymes, bones) pushed invalid acceptance far above novel-property stimuli and lowered d' in both wordings. [d01]
- Cognitive ability raises accuracy and lowers belief-based bias. [b18]
- Showing premises and conclusion together as one inference improves validity-like checks. [a23]

### 5.4 Interventions that worked

- Logic training improved valid-invalid discrimination, without breaking the one-dimension fit (abstract only). [b22]
- In LLMs: written chain of thought cut content effect strongly in open Qwen models (see section 6). Form-first two-stage prompts and fabricated-word few-shot examples helped. A solver helped on deep problems. [c04, c10, c09, d04, d05]

### 5.5 Interventions that did not work or are doubtful

- Disfluent font did not make people more analytic; it lowered accuracy (d_a 0.51 vs 0.92). [b18]
- Cognitive load did not shift reasoning in two experiments (but may have been too weak). [a15, a16]
- Plain instruction and few-shot reduce LLM belief bias only modestly on syllogisms and Wason. [c06, K13]
- Zero-shot "think step by step" with a one-word answer showed no change across 14 models (McNemar p=.612). [c07, d09]
- Temperature is not a clean criterion lever for models. [d14]

## 6. Language models

### 6.1 Headline: nobody has run the real design

No study found runs an LLM through the Rips / Heit-Rotello design (same arguments, deduction versus induction wording, ROC, d' or STA). Two limited searches (web and arXiv, both ended when the search quota ran out) found none. The nearest work is belief-by-validity interaction under one wording (Lampinen), accuracy gaps (Poddar), task framing with converted items (Abe), and a signal detection study on factual QA (Cacioli). [K18, c23, d18]

### 6.2 Content effects are criterion-like and human-like

- Language models and humans both say "valid" more often when the conclusion is believable and "invalid" more often when it clashes. Human baseline cited: about 90% wrongly accept invalid believable syllogisms. Models: Chinchilla, PaLM 2 (S/M/L), Flan-PaLM 2, GPT-3.5. Wason realistic-rule advantage in humans, Chinchilla, PaLM 2-L, GPT-3.5 (all z>2.2, p<0.03). [c05]
- Belief x validity interaction: significant in humans, PaLM 2-L, Flan-PaLM 2 and GPT-3.5 (all z>5.9, p<.001). Belief-consistent conclusions get "valid" regardless of logic; belief-violating ones are judged with more validity sensitivity. [d11]
- Few-shot examples take Chinchilla on natural language inference from heavily biased to near ceiling, but give only mild gains on syllogisms and Wason. Removing the instruction text did not change the overall result. Instruction-tuned Flan-PaLM 2 and GPT-3.5-instruct showed no consistent drop in content effects. [c06]
- Instruction tuning and RLHF can make belief bias stronger (Flan-T5, Mistral-Instruct, GPT-3.5, GPT-4). Few-shot examples with fabricated words give a noticeable drop; format-only few-shot gives little. [c09, K13]
- Human Wason accuracy rises with response time (z=4.44). Authors argue a single transformer can show both biased and consistent behaviour without a dual-system add-on; no mechanistic evidence of conflict arbitration in models. [c25]

### 6.3 Ability scales with form accuracy

Across 14 LLMs (160 syllogisms: 76 valid, 84 invalid; 3 temperatures; 4 prompting strategies): [c07, d09, d10]

| Measure | Value |
|---|---|
| Syntax (form) accuracy | 81.7% mean |
| Believability accuracy | 56.2% mean |
| Models with positive belief bias | 12 of 14 |
| Mean belief bias (congruent minus incongruent accuracy) | +10.81 points (SD 16.32; t13=2.47, p=0.028, d=0.66) |
| Syntax accuracy vs bias size | Spearman -0.565 (p=0.035) |
| Syntax accuracy vs consistency across content variants | Pearson r=0.877 |
| Strongest models | Gemini 2.5 Flash 99.6% syntax, 47.9-point syntax-minus-believability gap, bias under 2 points |
| Weakest | Llama 3.2 3B gap -14.5; Llama 3.2 1B -8.5; worst bias +46.9 |

Limit: only 38 of 160 items (23.8%) have believable conclusions. Accuracy gap is the type of index Heit and Rotello criticise. [d10, c24]

### 6.4 Criterion varies more by model than sensitivity

From reported precision, recall and the 47.5% valid base rate (derived by the earlier agent, not by the paper): Qwen3-Next 80B Thinking d' about 2.55, c about +1.46 (very strict); Gemma 3 27B d' about 1.39, c about -0.79 (lenient). The agent should measure its own cutoff, not assume one. [d09]

### 6.5 Chain of thought: conflicting results

- Bertolazzi et al.: Qwen2.5-32B accuracy 81.62 (zero-shot) to 94.60 (CoT), content effect 0.348 to 0.096. Qwen3-14B 86.54 to 96.70, content effect 0.213 to 0.014. That is a cut of about 72% and 93%. Alignment between validity and plausibility directions does not differ by prompt style (Mann-Whitney p=.625). So CoT acts like a criterion adjustment on top of an unchanged strength signal. Authors cannot explain why CoT helps while the representation stays entangled. [c04, b29, K12]
- Poddar et al.: zero-shot CoT versus zero-shot, McNemar chi2=1, p=.612 (389 vs 374 discordant, N=6,720 per comparison) across 14 models. Few-shot was below zero-shot by 3.57 points (p_adj=.0495; Wilcoxon p_raw=.0195, p_adj=.0584 in another table). [c27, d09]
- Why they differ: Poddar's cue was only "think step by step" with a one-word answer; Bertolazzi used open Qwen models and a different measure. No equal-token, closed-model study exists. Status contested. [d09, K12]
- Abstract-space work: models conflate plausibility with validity even when they write step-by-step explanations, so the rationale inherits the shortcut. [c12]

### 6.6 Form-first scaffolds

Two-stage prompt (name the logical form from the premises, then check validity on that form). Content effect, baseline to Boethius: Llama3-8B 73.2 to 50.7; Llama3-70B 63.5 to 49.3; GPT-4o 61.8 to 50.2; Gemma2-9B 62.8 to 56.7; Llama3-1B 76.1 to 64.9. A deductive-only prompt moved CE only a few points (GPT-4o 61.8 to 59.2). Small models needed the two stages as separate prompts. CE stays near 50 for the best setup. Column labels in the extract were unclear. [c10, K14]

### 6.7 Solvers and code

- Logic-LM average gain 39.2% over standard prompting and 18.4% over CoT across five datasets. GPT-4 (standard / CoT / Logic-LM): ProofWriter 52.67 / 68.11 / 79.66; FOLIO 69.11 / 70.58 / 78.92; LogicalDeduction 71.33 / 75.25 / 87.63; AR-LSAT 33.33 / 35.06 / 43.04; PrOntoQA 77.40 / 98.79 / 83.20 (CoT better). [c20, d04]
- Executable-formula rate for GPT-4: PrOntoQA 100%, ProofWriter 99.0%, LogicalDeduction 100%, FOLIO 79.9%, AR-LSAT 32.6%. Self-refinement raised executable rate by 5.01 points on average. [d04]
- Solver edge by ProofWriter depth (0, <=1, <=2, <=4, <=5 hops): +7.1, +5.0, +12.7, +20.0, +39.4 points. [d05]
- LINC: FOLIO GPT-4 CoT 75.3% vs LINC 72.5% (McNemar p=0.58). ProofWriter LINC with GPT-3.5 96.4%, with GPT-4 98.3%. Premises per question 5.3 (FOLIO) vs 18.8 (ProofWriter). FOL syntax errors 38% StarCoder+, 24% GPT-3.5, 13% GPT-4. On FOLIO the solver says "Uncertain" 57% of the time against 41% for CoT. [d06]
- SatLM (code-davinci-002): ProofWriter depth-5 CoT 80.1 vs 99.7; LSAT 23.5 vs 35.0; BoardgameQA 60.7 vs 79.4; CLUTRR 40.8 vs 68.3; GSM on par (71.8 vs 72.7). Can abstain on UNSAT or AMBIG. [d07]
- Small models are the weak point of translation; two-stage translation (predicates, then formulas) plus an arity verifier reduces errors (abstract only). [d08]
- All of these are 2023-era models; no token-matched comparison; none for current reasoning models. [K15]

### 6.8 Induction in models

- GPT-4 matches human property-induction on most of 11 phenomena (792 argument pairs, 110 participants after excluding 10). It fails premise non-monotonicity: an odd added premise should weaken the argument; the model says stronger, and its own explanation argues for monotonicity. GPT-4 is strongly wrong on Specific items and uncorrelated with humans on single-premise General Mammals arguments. GPT-3.5 matched humans better on General arguments; authors link this to RLHF. gpt-4-0314 at temperature 0, 400-token cap. [c13, c14, d13]
- Cheng et al. (SolverLearner): when the model writes a function from examples and an interpreter applies it, GPT-4 scores 1.0 in all cases. Zero-shot rule application collapses in counterfactual settings (GPT-4 base 9 0.697, base 11 0.551, spatial max 0.119, Caesar 0). GPT-3.5 as executor: base 8 0.398, base 9 0.196, base 10 0.934, base 11 0.152, base 16 0.64; interpreter as executor 1.0 in all bases. Table mapping partly garbled. Note "deduction" here means applying a rule, not judging validity. [c15, b28]
- Liu et al.: rule-following, learning from examples, and stating the rule are weakly linked. Agreement between a model's own proposed rule and its few-shot accuracy is at chance (0.0013 for GPT-3.5-turbo). GPT-4-turbo linear functions 96% with the true instruction vs 30% baseline. [c16]
- MIRAGE: models often answer new cases correctly without the correct rule (neighbour-based). Example-inference accuracy beats rule-induction accuracy by 16% on average under self-refine. On GPT-4o, CoT-like methods cut accuracy by up to 18% and 22%. [c17]
- Hypothesis search (GPT-4, ARC 100-problem subset): direct 17%; programs only 23%; LLM-summarised hypotheses 30%; human-selected 33%; human-written 43%. Natural-language intermediate without programs 19%. SyGuS 94.3% with 8 programs. [c18]
- Error sources in hypothesis search: generator 46.4%, summarizer 34.5%, implementor 61.2%. Summarizing drops 26% of correct generator hypotheses (12.1% absolute loss). Overall solve rate 62.0%. Implementor rescues 1092 trials (19.9%; 37.0% of double failures). [c19]
- Parsimony: in a multi-hypothesis setting, accuracy of all models except GPT-4o falls from above 80% to below 50% when ontology tree height goes from 1 to 2. [c22]

### 6.9 Other model facts

- Premise count hurts: LLaMA-3 8B zero-shot CoT 44.64 (2 premises), 39.64 (3), 31.79 (4). Pythia 1.4B 18.21, 11.07, 7.86. Supervised fine-tuning held 99.05, 94.17, 85.36. Zero-shot CoT in LLaMA-3 rarely says "nothing follows"; instruction tuning partly fixes this at the cost of valid items. Generation task, open small models. [d12, K21]
- "Nothing follows" is hard. GPT-4 zero-shot deduction overall 72.22%, "Neither" 44.44%; few-shot 95.83% (Neither 94.44%). GPT-3.5 few-shot 46.30% (Neither 2.78%). Llama-3-70B few-shot deduction 84.72% vs abduction 75.46%. Different items for the two framings. [d15]
- PaLM 2 models exceed human accuracy on 27 conclusion-licensing syllogisms (humans about 50%, best model about 75%) but are sure on the fallacy items and rarely answer "nothing follows" though it is correct for 37 of 64 types. [c08]
- Signal detection of LLMs (Cacioli 2026, factual QA, pre-registered): 168,000 confidence trials, 6,000 forced-choice, Llama-3-8B-Instruct, Mistral-7B-Instruct-v0.3, Llama-3-8B-Base, seven temperatures. Temperature raised AUC by 0.071-0.146 while shifting criterion. z-ROC slopes 0.52-0.84 (instruct 0.52-0.63; base 0.77-0.87; human recognition memory about 0.80). Plain equal-variance d' is unsafe for models. [d14, K24]
- Training on deduction, induction and abduction trajectories separately transfers to realistic tasks, up to 14.60 points (abstract only). Not relevant to a scaffold-only build. [c21]
- Steering (K-CAST) can fix some unresponsive models, up to 15 points of formal accuracy gain (search summary only). [c11]

### 6.10 Caveats for the whole section

Most LLM work is on open-weight or 2023-era models and small syllogism sets. The agent's model is none of these. LLM studies measure accuracy gaps, not ROC or d'. Poddar's own method ignores token probabilities that could serve as confidence ratings. [critique]

## 7. What our agent should take

Format: item | schema part | status | evidence ids. Status is [E] established, [S] single-source, [C] contested.

### Add now (established)

1. **Treat "does it follow?" and "is it plausible?" as different questions with different error profiles, and name which one is being asked.** Plausibility wording lets invalid items through (.55-.57 accepted vs .22-.24). Schema part: G4/O3. [E]. Evidence: a04, a05, b01, b02, a08, b13 (K01).
2. **Never let the generating model's feeling of validity be the validity check.** Validity must come from a content-stripped restatement, a counterexample test or code. Models conflate the two; written rationales inherit the shortcut. Schema part: G2/G10, reinforces O3. [E for the human-and-model pattern of belief pulling validity; mechanism [S]]. Evidence: c05, c12, K13, c07, d11, K07 (K07 is [C] on the mechanism).
3. **Measure and remove the global yes-bias before comparing any wordings or checkers.** Schema part: G4 and logging (section 6 of the schema). [E]. Evidence: d09, d11, d12, d15 (K22).
4. **Report hit rate and false-alarm rate (or d_a / AUC), never one difference score, when judging a verifier.** Schema part: logging. [E]. Evidence: a12, b26, c24, d14.
5. **Give validity checks enough budget; they degrade first under pressure.** Speeding and low capacity cut validity sensitivity before belief sensitivity. This is a caution against G11's thinking cap on the validity step. Schema part: G11/G12. [E]. Evidence: a11, a17, b05, b07, b18, b27 (K08).
6. **Route validity checks by proof depth and translation success.** Shallow, short, forward-chaining or hard-to-formalise goes to model reasoning. Deep, clean, many-premise goes to a solver or code, with CoT fallback when the formula fails. Keep an "undecided" outcome. Schema part: O3 and S4/S8. [E]. Evidence: c20, d04, d05, d06, d07, b28 (K15, K27). All 2023 models.
7. **Keep "undecided" as a third outcome of the check route.** The solver says "Uncertain" 57% vs 41% for CoT; SatLM abstains on UNSAT and AMBIG. Do not force yes/no. Schema part: O3, with G6 (never abstain on the first pass) governing the final answer, not the check. [E]. Evidence: d06, d07 (K27).
8. **Induction by hypotheses plus execution beats direct prediction; the bottleneck is hypothesis generation.** Keep a wide hypothesis set and let execution, not a summary step, prune. Schema part: O2/O3, S3/S4. [E]. Evidence: c18, c19, c22 (K17). (Largely overlaps existing S3/S4/G3.)
9. **Do not add bias checklists or "be careful/analytic" instructions as a fix for plausibility pull.** Consistent with schema 4b. Plain instruction is a modest remedy; instruction tuning can worsen belief bias. Schema part: 4b. [E]. Evidence: c06, c09 (K13).

### Test first

Each of these is [S] or [C]. All must beat the plain model at equal tokens (G7) before entering the schema.

1. **Explicit "assume premises true, ignore plausibility" or "name the form first" step before a validity verdict.** Schema part: O3/S4. [S]. Evidence: c10, d15, c09 (K14). Nearest support: two-stage prompt cut content effect to near 50; fabricated-word few-shot cut belief bias. No token-matched study.
2. **Short written derivation before the verdict, rather than a bare yes/no.** Schema part: O3, interacts with G11. [C]. Evidence: c04, b29 vs c27, d09 (K12). Bertolazzi says content effect falls 72-93% in open models; Poddar finds nothing from a minimal cue.
3. **Same item judged under two wordings in separate calls ("necessarily follows" vs "plausibly follows"), then compare rank order in code.** Disagreement in rank order, beyond what resampling noise explains, flags that something other than strength is at work. Schema part: S4/S7. [S]. Evidence: a09, d02 (K03).
4. **Set the validity and plausibility thresholds separately from stated stakes or base rates (cost of false accept; expected share of valid items).** Human support exists (base-rate experiment moved the two criteria in opposite directions), but only second-hand and for causal conditionals. No LLM test. Schema part: G4 / S0. [S]. Evidence: d03, d17, b09, a19 (K25).
5. **Form-first step on weak or small sub-models only; skip it for strong models.** Measure the congruent-minus-incongruent gap once per sub-model. Schema part: S0 gate / O3. [S]. Evidence: d10, d09 (K26).
6. **Mixing score for conditional or plausibility-heavy judgments: P(conclusion) with and without "assume the premises", then fit a form weight per item type.** Schema part: G4. [S]. Evidence: a20, a21, a22 (K10).
7. **Treat added premises as possibly weakening.** Ask for the effect of an odd premise by name, and record in code how each piece of evidence was gathered. Schema part: S2/G4. [S]. Evidence: c14, d13, d12 (K19, K21).
8. **"Nothing follows" example in few-shot to shift the validity criterion.** Schema part: S1/S4. [S]. Evidence: d15.
9. **Put premises and conclusion side by side for the validity check.** Schema part: S4. [S]. Evidence: a23.
10. **Two-checker disagreement as a flag** (model and solver, or two differently framed model calls); the items where they disagree get the extra attention. Schema part: S4/S7, G4-compatible because the checkers differ in method. [S]. Evidence: d06, c20.

### Memory

- Per problem class, record the plain model's hit and false-alarm rates under each wording, its measured criterion, and the congruent-minus-incongruent gap. Schema part: memory class record (section 5). [S]. Evidence: d09, d10, K22, K26.

## 8. Concrete tests on our bench

Principles for all tests: equal total tokens in both arms (G7). Five samples per cell. Collect a 1 to 6 confidence rating or a token probability. Use d_a or AUC and fit z-ROC slope, never plain d' unless the slope is near 1. Remove global yes-bias first (K22). Use wording, not temperature, as the criterion lever (K24). Bootstrap over items.

### Test 1: wording sensitivity and criterion (closes gaps 1, 2, 4)

- Item type: 48 items crossed validity x believability x premise count (1, 2, 4).
- Arms: (A) "necessarily follows" wording; (B) "plausibly follows" wording; (C) the same as A with a base-rate cue (20% vs 80% valid).
- Metric: accept rates by cell; d_a and z-ROC slope per wording; Spearman across wordings with a split-half ceiling; state-trace plot with a monotone fit.
- Expected effect: invalid-item accept rate higher under B than A, hit rate similar (matches K01). If d_a differs between A and B, that is a sensitivity effect; the one-scale model predicts the same rank order within the noise ceiling (Lassiter-Goodman: observed .53 vs .49-.64). Base-rate cue moves the false-alarm rate with discrimination unchanged, if the criterion account holds. [K01, K02, K03, K25, critique]

### Test 2: state-trace for the agent (gap 2)

- Item type: 12 to 24 conditions (belief x validity x length x premises).
- Arms: A vs B wording as above.
- Metric: mean accept rate under A against under B per condition; conjoint monotone regression with bootstrap; power check by simulating a two-dimension structure.
- Expected effect: a monotone plot would support one shared scale with two cutoffs as a valid agent design. A reliable non-monotone departure would argue for running two separate checks and combining them in code. Uncertain; no LLM prior exists. [a14, b08, K04]

### Test 3: explicit form-first step versus plausibility-first answer (gap 3)

- Item type: believable-invalid, unbelievable-valid, neutral valid and invalid syllogisms and conditionals, plus a matched set of plausibility items.
- Arms at equal total tokens: (A) plain "is it valid?"; (B) abstract the form first, then check validity; (C) "assume the premises are true, ignore plausibility" instruction. Also run each arm on plausibility items to measure what the step costs there.
- Metric: congruent-minus-incongruent accuracy gap, false-accept rate on believable-invalid items, d_a, plus accuracy on plausibility items.
- Expected effect: B reduces the gap (published prompt-only effect: content effect from about 62 to 50 for GPT-4o); C a smaller effect (plain instruction is a modest remedy). B costs nothing or little on plausibility items. [c10, c06, K14]

### Test 4: chain of thought at equal tokens (gap 7)

- Item type: matched believable and unbelievable syllogisms.
- Arms: (A) bare verdict; (B) short written validity derivation; (C) same tokens spent on 3 short independent bare-verdict samples and a vote (G11).
- Metric: content effect; accuracy; token cost.
- Expected effect: B below A on content effect (Bertolazzi: 0.348 to 0.096); the Poddar null suggests B may do nothing with a weak cue. C tests G11's claim that parallel short attempts beat one long one. [c04, c27, K12]

### Test 5: solver or code versus own judgment (gap 6)

- Item type: syllogisms and rule-chains by proof depth (1, 3, 5+) and by ease of formalisation (clean synthetic vs real natural-language).
- Arms: (A) model-only reasoning; (B) model translates to formal statements, code or solver judges, CoT fallback if the translation fails, "undecided" kept.
- Metric: accuracy, undecided rate, translation success rate, tokens.
- Expected effect: B wins from depth 3 or more on clean items (published gap +20.0 to +39.4 at depth 4-5 for 2023 models); A ties or wins on shallow and hard-to-formalise items. For current models the crossover may be shallower. [d05, d04, d06]

### Test 6: premise count and odd premise (gap 10)

- Item type: induction items with 1 to 5 premises; items where an added odd premise should lower strength.
- Arms: plain vs "record how evidence was collected, then rate".
- Metric: share of odd-premise items where strength falls; accuracy by premise count.
- Expected effect: at least some failure to lower strength (GPT-4 failed non-monotonicity). Accuracy falls with premise count on validity items (44.64 to 31.79 for LLaMA-3 8B). Decomposition or a solver step at high counts should help. [d12, d13, K21]

### Test 7: budget pressure on validity versus plausibility

- Item type: matched validity and plausibility items.
- Arms: tight token cap (G11-like) vs generous cap.
- Metric: accuracy by item type and cap.
- Expected effect: validity accuracy drops more than plausibility accuracy under the tight cap (human speeding result: validity effect .25 to .11). If true, exempt validity steps from the global cap. [b07, K08]

### Test 8: wording, few-shot "nothing follows" (cheap)

- Item type: syllogisms with a large share of "nothing follows" items.
- Arms: zero-shot vs 2 to 3 same-task examples including a "nothing follows" case, equal tokens.
- Metric: "nothing follows" recall and false-accept rate.
- Expected effect: large gain in "nothing follows" accuracy (GPT-4 44.44% to 94.44% in the older study). [d15, K13]

### Test 9: per-sub-model belief gap

- Item type: congruent versus incongruent syllogisms, each sub-model the agent calls.
- Metric: congruent-minus-incongruent gap.
- Expected effect: strong sub-models under 2 points; small ones large (up to +46.9 in the weakest study models). Turn the form-first step on only where the gap is large. [d10, K26]

## 9. What does not transfer, and why

1. **Human working memory and load results.** Concurrent load did not change reasoning in two experiments even in humans; there is no analogue to a digit-recall load for a model. The transferable idea is token budget and sample count, not load. [a15, a16]
2. **Time pressure literally.** A 5.5 s deadline has no clean model analogue. A token cap is the nearest, and the chain of reasoning is different: a model deciding fast is not sampling fewer worlds. The Lassiter-Goodman world-sampling story is a proposal, untested even in humans. [a10, a17]
3. **Individual differences in strategy.** Counterexample versus statistical reasoners (Markovits) are traits of people; the agent has one model per call and chooses strategy by prompt. Covered by subfield 07. [a27]
4. **Fluency manipulations.** Disfluent font lowering accuracy has no model equivalent. [b18]
5. **Training results.** Cao et al. (training on separate deduction, induction and abduction trajectories) and fine-tuned premise-count results (99.05 on SFT) need training, which this project does not do. [c21, d12]
6. **Steering and probe results.** Cosine alignments, steering vectors and the debiasing subtraction need white-box access. A closed API agent cannot do them. The prompt-level analogue (separate calls for form and believability, joined in code) is untested. [c01-c03, c11]
7. **The human d' gap taken as proof of two processes.** A one-word change reproduces it within one judge, with one scale and a word-specific exponent. For our agent a wording effect on d' is expected; it does not prove two modules. [d01, K03]
8. **Equal-variance d'.** Models show unequal-variance evidence (z-ROC slopes 0.52-0.63 for instruct models) and strong global yes-bias. Human d' formulas do not carry over unchanged. [d14]
9. **Causal conditional results.** All STA evidence on one dimension is about modus ponens versus accepting the consequent on causal conditionals. Syllogisms may recruit more analytic processing. Do not generalise to longer or real-world arguments. [a18, K05]
10. **2023-era model benchmarks.** Logic-LM, LINC, SatLM and Han et al. used models that are not the agent's. Rules of thumb (shallow to model, deep to solver) are hypotheses for the current model until re-measured. [K15, K19]
11. **Open-weight small-model syllogism sets.** Bertolazzi (Qwen), Poddar (14 mostly open or small models) and Ranaldi (Llama, Gemma) bear on a different capability range than the agent's. Poddar's finding that strong models separate form from belief suggests the agent may need less scaffolding than weak models; this is unmeasured. [d10, K26]

## 10. Open questions

The ten gaps from the cross-check, with their state after the gap search:

1. **d' versus criterion in an LLM under "necessary" vs "plausible" wording.** Closed to no study. OPEN. Method warnings: use d_a or AUC; remove yes-bias; wording not temperature as the lever. [d18, d14, d09, d11]
2. **Is the LLM state-trace plot monotone?** No LLM data. Needs 12 to 24 conditions. OPEN. This decides whether one scale with two cutoffs is a valid design. [d03, a14]
3. **Explicit "assume premises true" step at equal tokens versus plausibility-first answer?** No token-matched study. OPEN. Nearest: c10, d15, d09. [d18]
4. **Does the criterion shift between wordings track base-rate beliefs in an LLM?** Human support only (second-hand). OPEN for LLMs. [d03, K25]
5. **Is the Heit-Rotello effect stable beyond causal conditionals and short categories?** Search hit the quota. Only a11 (length and similarity move induction more) and d01 (natural predicates raised invalid acceptance to .82 and lowered d' in both wordings) bear on it. OPEN.
6. **When should the agent route a check to a solver or code?** Mostly closed for 2023 models (model wins short forward-chaining; solver wins with depth and premise count). No result for current reasoning models or at equal tokens. [d04-d08]
7. **Does CoT reduce content effect on closed API models at equal total tokens?** Conflict between Bertolazzi and Poddar is a difference of design. OPEN. [d09]
8. **Is the Lassiter-Goodman one-scale model right?** Verified as a reading (d01, d02); model incomplete (necessary R2 .57 below .70 ceiling); authors do not rule out a qualitative distinction. Still open: the same rank-order test on the agent.
9. **Does the dual-source mixing weight vary by item type enough to set a per-item rule for when to check form?** Not advanced. OPEN.
10. **Do premise-count and odd-premise effects damage strength estimates in the agent's induction steps?** Two weak-to-moderate sources. OPEN for the current model. [d12, d13]

Further open points:

- Does the single-process result survive outside causal conditionals (syllogisms, multi-premise real-world arguments)? [a18]
- Can any STA experiment separate one latent variable with two criteria from two latent variables with parallel effects? [b04, b12]
- Why does CoT reduce content effect when the internal alignment of validity and plausibility stays high? (c04: authors cannot explain.) [c04]
- Is the plausibility pull in models a training-text artefact (valid arguments in text are usually sound), as the authors guess? [c01]
- Rips (2001), Stephens, Dunn and Hayes (2018), Heit and Rotello (2010), Singmann and Klauer (2011) and Stephens et al. (2020) full text should be read to confirm numbers now held second-hand.
- Trippas, Thompson and Handley (2017): N and conflict-cost figures differ between two extractions (45 vs 43 and 82 participants; .68 vs .83 vs .21 vs .09); needs a clean read. [critique]
- Cheng et al. Table 13 row/column mapping not verified. [critique]

## 11. Sources

[V] = opened and read this study (full or substantial text). [M] = abstract, snippet or second-hand only.

**Human studies and models**

1. [M] Rips (2001) Two kinds of reasoning. Psychological Science 12(2), 129-134. https://doi.org/10.1111/1467-9280.00322 (also https://www.psychologicalscience.org/journals/psychological-science/1467-9280.00322/)
2. [V] Heit and Rotello (2005) Are there two kinds of reasoning? https://escholarship.org/uc/item/58k5m8k3 (numbers re-confirmed in cross-check)
3. [M] Heit and Rotello (2010) Relations between inductive reasoning and deductive reasoning. JEP:LMC 36, 805-812. https://doi.org/10.1037/a0018784
4. [M] Rotello and Heit (2009), three-premise arguments (via Lassiter and Goodman). No separate URL opened.
5. [V] Lassiter and Goodman (2012) How many kinds of reasoning? Inference, probability, and natural language semantics. CogSci 34. https://escholarship.org/uc/item/2tw9x8t6
6. [V] Hayes, Stephens, Ngo and Dunn (2018) The dimensionality of reasoning: Inductive and deductive inference can be explained by a single process. https://unsworks.unsw.edu.au/bitstreams/a0fb61bb-6830-4fe8-8ed3-0275093ab60e/download (alt: https://unsworks.unsw.edu.au/server/api/core/bitstreams/a0fb61bb-6830-4fe8-8ed3-0275093ab60e/content)
7. [M] Stephens, Dunn and Hayes (2018) Are there two processes in reasoning? The dimensionality of inductive and deductive inferences. Psychological Review 125(2), 218-244. https://doi.org/10.1037/rev0000088
8. [V] Stephens, Dunn and Hayes (2017) A two-step signal detection model of belief bias. https://escholarship.org/uc/item/5189w557
9. [V] Stephens, Matzke and Hayes (2019) Disappearing dissociations in experimental psychology: state-trace analysis to test for multiple processes. https://pure.uva.nl/ws/files/52597080/1_s2.0_S0022249618300701_main.pdf
10. [M] Stephens, Dunn, Hayes and Kalish (2020) A test of two processes: the effect of training on deductive and inductive reasoning. Cognition 199, 104223. https://doi.org/10.1016/j.cognition.2020.104223
11. [V] Ashby (2019) State-trace analysis misinterpreted and misapplied: Reply to Stephens, Matzke, and Hayes. https://labs.psych.ucsb.edu/ashby/gregory/sites/labs.psych.ucsb.edu.ashby.gregory/files/pubs/ashby2019.pdf
12. [M] Singmann and Klauer (2011) Deductive and inductive conditional inferences: two modes of reasoning. Thinking and Reasoning 17, 247-281. https://doi.org/10.1080/13546783.2011.572718
13. [V] Singmann, Klauer and Over (2014) New normative standards of conditional reasoning and the dual-source model. https://doi.org/10.3389/fpsyg.2014.00316
14. [V] Evans, Thompson and Over (2015) Uncertain deduction and conditional reasoning. https://doi.org/10.3389/fpsyg.2015.00398
15. [V] Trippas, Thompson and Handley (2017) When fast logic meets slow belief: evidence for a parallel-processing model of belief bias. https://doi.org/10.3758/s13421-016-0680-1 (full text: https://pmc.ncbi.nlm.nih.gov/articles/PMC5432582)
16. [V] Trippas, Verde and Handley (2014) The SDT model of belief bias: complexities, complications, and a new set of indices. https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2014.00631/full
17. [V] Singmann and Kellen (2014) Concerns with the SDT approach to causal conditional reasoning: comment on Trippas et al. https://pmc.ncbi.nlm.nih.gov/articles/PMC4030140/
18. [V] Trippas et al. (2014) Modeling causal conditional reasoning data using SDT: caveats and new insights. https://pmc.ncbi.nlm.nih.gov/articles/PMC3950845/
19. [M] Dube, Rotello and Heit (2010) Assessing the belief bias effect with ROCs: it's a response bias effect. Psychological Review 117, 831-863. https://doi.org/10.1037/a0019634
20. [M] Howarth, Handley and Walsh (2016) The logic-bias effect. https://pearl.plymouth.ac.uk/handle/10026.1/12528
21. [V] Hayes, Heit and Rotello (2014) Memory, reasoning, and categorization: parallels and common mechanisms. https://doi.org/10.3389/fpsyg.2014.00529 (https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2014.00529/full)
22. [V] Hayes and Heit (2018) Inductive reasoning 2.0. WIREs Cognitive Science. https://course-resources.minerva.edu/uploaded_files/mke/00231149-5644/hayes-and-heit--2018.pdf
23. [V] Hayes and Heit (2013) How similar are recognition memory and inductive reasoning? https://doi.org/10.3758/s13421-013-0297-6
24. [V] Markovits (2024) Are there two kinds of reasoners? https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10971091/

**Language-model studies**

25. [V] Bertolazzi, Pezzelle and Bernardi (2026; arXiv 2510.06700) How Language Models Conflate Logical Validity with Plausibility: A Representational Analysis of Content Effects. https://arxiv.org/abs/2510.06700 (v2 html: https://arxiv.org/html/2510.06700v2). Counted once (a29/c01 duplicates).
26. [V] Lampinen, Dasgupta, Chan et al. (2024) Language models show human-like content effects on reasoning tasks. https://arxiv.org/abs/2207.07051 (pdf: https://arxiv.org/pdf/2207.07051)
27. [V] Poddar, Sahoo and Ghosh (2025) Understanding Syllogistic Reasoning in LLMs from Formal and Natural Language Perspectives. https://arxiv.org/abs/2512.12620 (pdf: https://arxiv.org/pdf/2512.12620)
28. [V] Eisape et al. (2024) A Systematic Comparison of Syllogistic Reasoning in Humans and Language Models. https://arxiv.org/abs/2311.00445
29. [V] Itzhak, Stanovsky, Rosenfeld and Belinkov (2024) Instructed to Bias. https://arxiv.org/abs/2308.00225
30. [V] Ranaldi, Ranaldi, Zanzotto and Cohen (2026) Thinking in Schemas: Robust Syllogistic Reasoning in LLMs (Boethius). https://aclanthology.org/2026.acl-long.1897/
31. [M] Valentino et al. (2026) Mitigating Content Effects on Reasoning in Language Models Through Fine-Grained Activation Steering. https://ojs.aaai.org/index.php/AAAI/article/view/40617
32. [V] Abstract Activation Spaces for Content-Invariant Reasoning in Large Language Models (2026), abstract and introduction. https://arxiv.org/abs/2602.02462
33. [V] Han, Ransom, Perfors and Kemp (2024) Inductive reasoning in humans and large language models. https://arxiv.org/abs/2306.06548 (pdf: https://arxiv.org/pdf/2306.06548)
34. [V] Cheng et al. (2024) Inductive or Deductive? Rethinking the Fundamental Reasoning Abilities of LLMs. https://arxiv.org/abs/2408.00114 (html: https://arxiv.org/html/2408.00114v2). Table mapping partly verified.
35. [V] Liu, Neubig and Andreas (2024) An Incomplete Loop. https://arxiv.org/abs/2404.03028
36. [V] Li et al. (2025) MIRAGE: Evaluating and Explaining Inductive Reasoning Process in Language Models. https://arxiv.org/abs/2410.09542
37. [V] Wang, Zelikman, Poesia, Pu, Haber and Goodman (2024) Hypothesis Search. https://arxiv.org/abs/2309.05660
38. [V] Parab et al. (2025) Analysis of Error Sources in LLM-based Hypothesis Search for Few-Shot Rule Induction. https://arxiv.org/abs/2509.01016
39. [V] Pan, Albalak, Wang and Wang (2023) Logic-LM. https://arxiv.org/abs/2305.12295 (pdf: https://arxiv.org/pdf/2305.12295)
40. [V] Olausson et al. (2023) LINC. https://arxiv.org/pdf/2310.15164
41. [V] Ye et al. (2023) SatLM. https://arxiv.org/pdf/2305.09656
42. [V] Thatikonda, Han, Buntine and Shareghi (2026) Improving Symbolic Translation of Language Models for Logical Reasoning (abstract and introduction). https://arxiv.org/pdf/2601.09446
43. [V] Bertolazzi, Gatt and Bernardi (2024) A Systematic Analysis of LLMs as Soft Reasoners: The Case of Syllogistic Inferences. https://arxiv.org/pdf/2406.11341
44. [V] Cacioli (2026) LLMs as Signal Detectors: Sensitivity, Bias, and the Temperature-Criterion Analogy. https://arxiv.org/pdf/2603.14893
45. [V] Abe et al. (2026) Abductive Reasoning with Syllogistic Forms in Large Language Models. https://arxiv.org/pdf/2603.06428
46. [V] Chan, Gaizauskas and Zhao (2026) Position: Logical soundness is not a reliable criterion for neurosymbolic fact-checking with LLMs. https://arxiv.org/pdf/2604.04177 (position paper, no experiments)
47. [V] Do Language Models Follow Occam's Razor? (2025), abstract, introduction and part of results. https://arxiv.org/abs/2509.03345
48. [M] Cao et al. (2026) Fundamental Reasoning Paradigms Induce Out-of-Domain Generalization in Language Models (abstract and introduction only). https://arxiv.org/abs/2602.08658

**Search records**

49. [M] Gap search note, no LLM version of Rips / Heit-Rotello / STA design found. https://digital.library.adelaide.edu.au/items/0650dbc6-287a-4c36-b391-356f7d78c8a0 and https://arxiv.org/ . Absence from a limited search (the quota ran out partway), not proof of absence.
