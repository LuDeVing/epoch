# The problem of the priors: deep document

*Subfield D02.03. Evidence: evidence_a-d.jsonl (ids a01-a27, b01-b27, c01-c26, d01-d16), claims.jsonl (K01-K35), critique.md. Numbers were checked against opened sources unless marked. Status marks: [E] established, [S] single-source, [C] contested.*

## 1. What it is

Bayesian reasoning needs a starting credence (a prior) before any evidence arrives. The problem of the priors asks where that number comes from and whether anything beyond coherence limits it (a08).

Two camps exist.
- **Subjective Bayesians** (de Finetti, Savage, Jeffrey, van Fraassen) say any coherent prior is allowed. Evidence later washes out the differences (merging of opinions, Blackwell and Dubins 1962; a08, a11).
- **Objective Bayesians** (Laplace, Keynes, Carnap, Jeffreys, Jaynes) say ignorance has a unique correct representation: indifference, invariance under transformations, or maximum entropy (a04, a09, a14).

Why this matters for a scaffolded agent: the S0 gate must say, before any attempt, how likely each mode is to solve this class of problem. That is a prior. The schema's answer is to take it from a measured class record (k passes in n runs), not from the model's feeling. This document tests that answer against theory (Bertrand, Jaynes, Jeffreys, empirical Bayes) and against what LLMs do when asked for, or given, priors.

Three practical questions drive the rest.
1. With no history, what default do we use, and does the choice matter?
2. With a thin history (n below 10), how much do we trust k/n?
3. Can the model supply or use a prior itself, or must code do it?

## 2. History and theories in depth

### 2.1 Indifference and its failure
Laplace and de Moivre: give equal credence to equally possible cases. Rule of succession: after N successes, P(next success) = (N+1)/(N+2), so 4/5 after 3 (a12). Objections: circularity, and dependence on how the cases are carved up.

The cube factory (a13): a cube has side in [0,1] ft. Uniform in side gives P(side <= 1/2) = 1/2. Uniform in face area gives 1/4. Uniform in volume gives 1/8. Same event, three "ignorant" answers. The Stanford entry's square example (a09) makes the same point: three equal 1 cm length bins get 1/3 each, but the area partition gives a different credence. K03 [E].

### 2.2 Bertrand's chord paradox (1889)
A random chord of a circle: what is the chance it is longer than the side of the inscribed equilateral triangle? (a01, opened Jaynes 1973)
- Uniform over chord distance from centre: 1/2.
- Uniform over the angle between endpoints: 1/3.
- Uniform over chord midpoint in the disc: 1/4.

Physical set-ups map to answers (a25, secondary): spinner 1/3, thrown straws 1/2, midpoint by a fly in molasses 1/4. Jaynes lists ten authors who disagree on whether the problem is ill-posed (a01). K01 [E]: "at random" alone does not fix a prior; the sampling process does.

### 2.3 Jaynes: invariance and maximum entropy
Jaynes (1968, a04-a07) gave two rules for ignorance priors.
- **Transformation groups.** The prior must not change under transformations the problem leaves open. Scale parameter sigma: dsigma/sigma. Location parameter: flat. Unknown success probability theta: 1/(theta(1-theta)), the Haldane form (a06). Jeffreys' rule is a special case, and in Jaynes's location-parameter example it gives the wrong answer if applied to the wrong variable (a05).
- **Maximum entropy.** Pick the distribution with the largest H = -integral p log p given the stated constraints (a04). Jaynes argued it is the one most likely to be seen in repeated experiments (a07).

Chemical example (a06): Bayes-Laplace gives only 2/3 that the next sample dissolves after the first did. Jaynes calls this too small; the 1/(theta(1-theta)) prior gives a higher value, closer to intuition for a repeatable property.

Jaynes (1973, a02): demand the answer be unchanged by rotation, scale (circle size) and translation (circle position). Translation invariance gives f(r) = 1/(2 pi R r), solution A, p = 1/2, with a singularity at the centre. B and C fail scale or translation invariance. He tested it with broom straws: 128 successful tosses on a 5-inch circle, chord lengths in 10 bins, and the fit gave "an embarrassingly low" chi-squared (a03). No table or p-value is given; treat as informal.

### 2.4 Drory's challenge (2015)
Drory (b02) shows the same symmetry tools support 1/3 and 1/4 under other generating processes. His experiment: a stick released at a random point on a circle edge. 700 attempts, 363 successes (0.518). Of the successes, 123 chords were longer than the triangle side: 0.339, standard error about 0.025. That fits 1/3, not 1/2. Critique note: this is a different physical process from Jaynes's straws, so it does not contradict Jaynes. It shows the answer follows the process. K02 [C].

### 2.5 Jeffreys, Haldane and the default-prior family
Jeffreys prior is proportional to sqrt(det Fisher information) and is invariant under reparameterisation (a24). Bernoulli: Beta(1/2,1/2). Gaussian mean: flat. Gaussian sd: 1/sigma. Caveats: can be improper, violates the strong likelihood principle, awkward for many parameters.

For an unknown pass rate the live options are Haldane (improper), Jeffreys Beta(1/2,1/2) and uniform Beta(1,1) (K04 [E]). All give 0.5 at n=0 (d07) and differ only when n is 1 to 3 and k=0 or k=n.

### 2.6 Carnap and Keynes: prior strength
Carnap's lambda-continuum (a14): estimate = (s_j + lambda/k)/(s + lambda). Lambda is the prior weight in pseudo-observations. Keynes's two urns (a10): urn a is half white (credence 0.5); urn b has unknown proportions. One credence hides the difference in evidence quality; Keynes would give urn b the interval [0,1]. K07 [E]: a prior needs a strength (lambda, effective sample size, pseudo-counts), not only a value.

### 2.7 The modern statistical view: priors are judged by their predictions
Gelman, Simpson and Betancourt (2017; a15, a16, d03): a prior can only be understood together with the likelihood, through the prior predictive distribution. Flat priors are not harmless. Example: a survey estimate of 8 +/- 3.3 percentage points. Uniform prior: posterior mean 0.08, sd 0.033, 99.2% chance the effect is positive. A weakly informative prior N(0, 0.005) gives posterior mean 0.002. K05 [E].

Winkler, Smith and Fryback (2002; d01, d02): with zero events seen, "noninformative" Beta(a,a) priors disagree. Contrast-agent example, 0 reactions in n=167: the posterior 0.95 fractile runs from near 0 up to 0.018 (a=1). Second finding: a conservative (pessimistic) bound on an input can reverse a downstream result. A Rule-of-Three upper bound as the false-positive rate gave a diagnostic probability of 0.018, against 0.053 from an informative Beta(1,999) prior (posterior mean 1/14,000).

### 2.8 Empirical Bayes: priors from data about similar units
Efron and Morris (1977; a17, re-verified): 18 baseball players, first 45 at-bats. Shrinking each average about 80% of the way to the grand mean (.265) predicted the rest of the season better. Total squared error .022 vs .077 for raw averages (ratio 3.5). Clemente: .265 + .212 x (.400 - .265) = .294. K06 [E] (two sources with Chen and Lei).

Chen and Lei (2025; d09): shrinking binomial rates toward a pooled mean with a data-chosen weight gave the lowest holdout MSE in 3 of 3 datasets, gains of about 1 to 5 percent. The table column mapping is a reading; the text extraction was garbled.

### 2.9 Long-run guarantees and their limit
Merging of opinions and self-correction hold in the limit. The Stanford entry itself notes the long run may be too long (a08, a11). For an agent with classes seen 0 to 10 times, small-sample prior behaviour is the whole game. K08 [S].

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Bertrand chord: three "uniform" readings, three answers | 1/2, 1/3, 1/4 | a01, a25, b02 | [E] K01 |
| Jaynes invariance picks 1/2; Drory's process gives 1/3 | Jaynes 128 tosses, 5-inch circle; Drory 700 attempts, 363 hits, 123 long chords, 0.339 (SE ~0.025) | a03, b02 | [C] K02 |
| Indifference depends on parameterisation | side/area/volume: 1/2, 1/4, 1/8 | a13, a09 | [E] K03 |
| Default prior at small n changes the estimate | rule of succession 4/5 after 3 successes (uniform) | a12, a06, d01 | [E] K04 |
| Flat prior with small data gives false confidence | 8 +/- 3.3 pts: uniform gives 99.2% real effect; N(0,0.005) gives mean 0.002 | a15, d03 | [E] K05 |
| Shrinkage to pooled mean beats raw unit rates | squared error .022 vs .077; ratio 3.5; 80% shrink | a17, d09 | [E] K06 |
| Priors need a strength | Carnap lambda; Keynes urns | a14, a10 | [E] K07 |
| LLMs have built-in priors not overridden by instructions | base models put 60-80% on heads | a22 | [E] K09 |
| Off-the-shelf LLMs plateau in multi-round updating | ~36-58% vs 81% Bayesian Assistant after 5 rounds; 624 simulated users | b09, c20 | [E] K10 |
| Base-rate use with uncharacteristic description | odds ratio 9 (GPT-4o, GPT-4, Llama-3-70B), 8.86 Claude-3-Opus, 6.36 Gemini-1.5-Pro, 3 Mistral-Large; humans 2.25 | b06, c14 | [E] K12 |
| Stereotypical description: base rate ignored | ratios 1.18-2.58 (CS), 1.00-1.60 (humanities) | c15 | [E] K12 |
| Recalled base rates track similarity, not truth | prior-posterior Spearman -0.84 to -0.90; posterior-similarity 0.87-0.94 (to 0.98 with modifications) | b07, c15 | [E] K13 |
| Recalled prior inconsistent | GPT-4o stated 2-4%, used 10-30% | b08 | [E] K13 |
| Wording beats reasoning prompts for base-rate use | "indicate" to "compute": ratio ~1.25 to ~9.5 (GPT-4o, CS); four Bayes prompts left unstructured test unfixed | b08, c16 | [S] K14 |
| "Reason Bayesian" hurts forecasts; "base rate first" helps | Brier +0.025 (adj p 0.036); Base Rate First -0.016 (0.036); Frequency-Based -0.019 (0.022); Step-Back -0.015 (0.036); 38 prompts | c21 | [E] K15 |
| Prompt debiasing backfires on judgment items | Judgment accuracy -4.4%; bias shifts -4.3/-7.7/-2.7 pp; 5,300 instances | b17, d11 | [E] K15 |
| Natural frequencies help humans, size disputed | headline 24% vs 4% (secondary); Weber et al ~36% vs 20%, 49% still convert; N=180 | b12, b13 | [C] K16 |
| LLM-elicited priors differ by model | Cohen's d centre 0.2-0.25; GPT-4 ~0.5; Mistral t(30) always; Llama-70B nu=5 | b18, c05 | [S] K17 |
| LLM priors conflict with data | effective sample size near 0 (~2) on weather; 25 cities | a21, c06 | [S] K18 |
| Leakage inflates LLM prior tests | GPT-3.5 recognised 6 of 11 datasets, Gemini 1.5 Pro 5, Llama 2 70B 2 | c07 | [E] K19 |
| Iterated-learning readout of GPT-4's prior | 100 chains x 12 iterations; converge at iteration 7-8; causal r 0.85 uniform vs 0.86 empirical | b04, c01, c02 | [S] K20 |
| AutoElicit: LLM priors cut labels | ~10x lower MSE after 5 examples (synthetic); equal by 20; UTI same peak accuracy with ~15 labels, saving over 200 days | a18, b20, c08 | [S] K21 |
| 66-patient saving claim is weak | LPD -3.842 +/- 0.294 vs -3.963 +/- 0.464; 80% data -4.093 vs baseline 100% -4.103; all within 1 SD | b21 = c10 (one paper) | [C] K22 |
| Prior-only calibration worsens Bayesian error | rescaling the posterior too lowers it | c12, c13, d14 | [S] K23 |
| Post-training shifts task prior, not knowledge | Bayesian scaling law fits | b24, b23 | [E] K24 |
| Answer-label prior | GPT-2 0.007 when A never correct vs ~0.33; Mistral 0.273 (never A) vs 0.512 (never D) | c19 | [S] K25 |
| LLM forecasting near crowd, below | system Brier 0.179 vs crowd 0.149, random 0.250, best zero-shot 0.208; retrieval 0.206 to 0.186 | b25, c22 | [S] K26 |
| Calibration breaks out of distribution | good on formatted multiple choice only | b26, c23 | [S] K27 |
| Probabilistic answers vary over time and runs | GPT-4 correct with correct reasoning 69.2%, Claude 2 55.0% (12 tasks, 10 runs each) | a23, b15, b16 | [E] K28 |
| Simulation: shrink a thin class record | Brier 0.2339 (Beta(1,1)) vs raw 0.2678; recalled prior 0.2 too high 0.2794; const 0.5 0.250 | d05 | [S] K29, own model |
| Simulation: zero-history default | pooled mean 0.240 vs 0.250 | d07 | [S] K30, own model |
| Simulation: estimating strength needs ~20 classes | EB vs fixed uniform: M=5 0.2397 vs 0.2342; M=20 0.2324 vs 0.2345; M=50 0.2297 vs 0.2339 | d06 | [S] K31, own model |
| Prior-data conflict check | false alarm 0.014-0.051 at alpha 0.05; power 0.33-0.38 at n=5-10 (true 0.2 vs prior mean 0.6) | d04, d08 | [S] K32 |
| Raw outcome lists are hard to use | accuracy at 54 labels 0.21 (Llama3.1-8B), 0.65 (Qwen2.5-7B); order effect 0.011-0.039 bits | d12, d13 | [S] K33 |
| Pessimistic input can flip a decision | 0.018 vs 0.053 | d02 | [S] K35 |

## 4. Mechanisms and models

### 4.1 Beta-binomial class prior (implementable)
Per problem class c and mode, keep (k, n): passes and runs. Prior Beta(a0, b0) with pseudo-count strength s = a0 + b0 and mean m. Posterior mean = (k + s*m) / (n + s). The gate probability is that value.
- n = 0: use the pooled rate m across all classes (d07: Brier 0.240 vs 0.250). Log which default was used.
- 0 < n < 10: use a fixed s of about 2 (Beta(1,1) when m = 0.5). In simulation this beat raw k/n and beat a biased recalled prior (d05).
- At least about 20 classes: fit s by method of moments on (k_c, n_c) across classes (d06). Below 10 classes, fixed s wins. Chen and Lei back data-tuned shrinkage on real data (d09).

### 4.2 Prior-predictive conflict check
Given the class record's prior Beta(a,b) and a new batch of y successes in n trials, the predictive is beta-binomial: p(y) = C(n,y) B(a+y, n-y+b) / B(a,b). The p-value is the sum of p(y') over all y' with p(y') <= p(y_obs) (d04). If it falls below alpha, mark prior-data conflict, treat the class record as unreliable (lower s) or route to the doubt step. Measured: false alarm is at or under alpha; power is weak at n = 5-10 (0.33-0.38; d08), so a non-flag is not proof of agreement.

### 4.3 Effective sample size
ESS = a + b of the prior. Selby (a21, c06) used it as a conflict measure: LLM weather priors had ESS near 0 against data, and some elicited priors had ESS above 1000 (K17). Rule: an LLM-stated prior is accepted only if its ESS is bounded and a prior-predictive check against some data passes.

### 4.4 Invariance step for under-specified "random" tasks
A prompt-plus-code step: (1) code lists the quantities the task statement leaves open (position, scale, parameterisation, sampling process); (2) a slot asks the model to name the generating process; (3) if two parameterisations give different answers, the agent reports the set of answers, not one. Evidence is theory only (K01, K03; K02 contested). No LLM test exists (gap 10).

### 4.5 Iterated in-context learning to read out a model's own prior
Zhu and Griffiths (c01, b04): the model predicts a quantity, data is sampled from the prediction, the model sees the data, repeat. 100 chains, 12 iterations, T=1. Chains converged in 7-8 iterations. Use: compare the agent's implicit pass-rate prior with the measured class record. Assumes the LLM is an approximate Bayesian agent (unproven; c01).

### 4.6 Code-side Bayes update
Off-the-shelf models plateau (b09), drift with example order (d13) and neglect priors under stereotypes (c15). Do the multiplication in code. The model supplies likelihood-relevant features; code applies prior x likelihood. BASIL (c13): fixing the prior alone makes things worse, so the posterior step must be handled too.

### 4.7 Display format
Precompute (k, n, shrunk mean) in one fixed line. Do not give raw outcome lists (d12, d13). Whether "k of n" beats a percentage for LLMs is untested (K33).

## 5. What holds up

**Holds (replicated or multi-source)**
- Indifference depends on parameterisation (3 sources). Defaults disagree at zero events (Winkler, Gelman).
- Shrinkage beats raw small-n rates (Efron-Morris, Chen and Lei, plus our simulation).
- LLMs use stated base rates when the case text is neutral and drop them when it is stereotypical: six models, same direction (b06, c14, c15).
- Data leakage in tests of LLM prior knowledge (c07, b19, a18).
- Off-the-shelf LLMs track Bayesian updating poorly over multiple rounds (b09, c20, d10, d13).

**Contested**
- Jaynes vs Drory on invariance (K02). Both internally consistent.
- Size of the natural-frequency benefit in humans (24% vs 4% headline; about 36% vs 20% in Weber et al.; 49% convert back).
- LLM priors help (AutoElicit) vs fail (Selby: ESS near 0; LLM imputation did not consistently beat kNN or random forest on 64 OpenML-CC18 datasets). Tasks differ: linear weights vs weather facts vs clinical rates.
- Arai et al. 66-patient saving: all gaps inside one SD; MedGemma at T=0.5 was worse than baseline.

**Interventions that worked**
- "Compute" instead of "indicate" (b08).
- Base Rate First (-0.016 Brier), Frequency-Based Reasoning (-0.019), Step-Back (-0.015) (c21).
- Retrieval for forecasting (0.206 to 0.186; c22).
- Calibrating prior and posterior together (c13).

**Interventions that failed**
- Four explicit Bayes-rule prompts on the unstructured base-rate test (c16).
- "Bayesian Reasoning" prompt (+0.025 Brier, worse) (c21).
- Prompt-level debiasing (-4.4% judgment accuracy) (d11).
- Chain of thought on multi-round updating (b09).
- Prior-only calibration (c13).

**Moderators**
Description type (neutral vs stereotypical); task wording; recall vs given base rate; model scale (Pythia 70M-12B did not remove coin bias, a22); number of observations; temperature (Arai: T=1.0 beat T=0.5); answer-option position (c19).

**Caveat.** Schoenegger's raw gains in single-model tables were not significant after correction (adj p 0.128-0.256). The base-rate-first gain is small and model-dependent.

## 6. Language models

**Built-in priors.** Models start with biased P(heads). Base models put 60-80% on heads regardless of instructions. Scale did not fix it, and in-context evidence outweighs a stated bias once enough flips are seen (Gupta et al., Mistral-7B-Instruct decay 0.9107; a22). They also carry an answer-label prior: GPT-2 scores 0.007 on MMLU items where A is never correct, about 0.33 elsewhere (c19). Post-training mostly moves the task prior (b24).

**Base-rate use.** Structured items with all numbers given: frontier models score 1.0 on Q4 vs 0.20 for humans (c14). Jason problem (75% vs 25% base, normative odds ratio 9): GPT-4o, GPT-4, Llama-3-70B reach 9; Claude-3-Opus 8.86; Gemini-1.5-Pro 6.36; Mistral-Large 3; humans 2.25 (b06). With stereotypical descriptions ratios fall to 1.18-2.58. When the model must recall its own base rate, the posterior tracks similarity and runs against the true prior (Spearman -0.84 to -0.90; b07). Stated 2-4%, used 10-30% (b08).

**What changed it.** One word ("compute" for "indicate") raised the GPT-4o ratio from about 1.25 to about 9.5 (c16). Four Bayes-rule prompts did not fix the unstructured test. Forecasting: Base Rate First -0.016 Brier, Frequency-Based -0.019, Bayesian +0.025 (c21). CogBias debiasing prompts lowered judgment accuracy 4.4% (d11).

**Mammography (Bar-Hillel).** Correct PPV is 7.7%. With numbers, models mostly invoke Bayes. In the non-numeric version the GPT models said 10% (incidence), Bard 80% (sensitivity). Answers changed between March and August 2023 (b15, a23).

**Multi-round updating.** In the 5-round flight task, off-the-shelf models reached 36-58% vs 81% for the Bayesian Assistant. Fine-tuning on the Bayesian Assistant's outputs gave about 80% agreement and beat fine-tuning on true labels (b09, b10). That is a training result, out of scope for us. BayesBench: seven models track a Beta(1,1) coin posterior only roughly; large models over-update toward 0 or 1 across 100 flips (d10).

**LLMs as prior sources.** AutoElicit gives about 10x lower MSE at 5 examples (a18) but weak models return uninformative priors and its in-context predictions mismatch its elicited priors (energy gaps 0.15-0.39; c09). Selby: models differ more than tasks; effect-size centres 0.2-0.25 (GPT-4 ~0.5); ESS near 0 on weather (a21). Leakage: GPT-3.5 recognised 6 of 11 datasets (c07). Arai: unconfirmed (K22).

**Forecasting.** Best zero-shot 0.208 Brier, system 0.179, crowd 0.149, random 0.250; retrieval moved 0.206 to 0.186 (c22). Calibration is good on formatted multiple choice and poor out of distribution (b26).

**Stability.** Same prompt, different month, different answer (a23). GPT-4 69.2% and Claude 2 55.0% correct with correct reasoning over 12 tasks x 10 runs (b16).

**Gap.** The newest studies found use 2023-2025 models, small models or R1 distills (d16, K34). No study tests 2025-2026 reasoning models on prior recall or class-record use.

## 7. What our agent should take

### Add now (established)

| Item | Part | Status | Evidence |
|---|---|---|---|
| Store (k, n) per class and mode beside every rate; never a bare percentage in memory | memory/S0 | [E] | K07; a10, a14, a21, d01, d06 |
| Shrink thin records toward the pooled rate; use the pooled rate for n=0 | memory/S0 | [E] theory, [S] size | K06, K04, K30; a17, d09, d05, d07 |
| Do the Bayes arithmetic in code, not in the model's head | G5/S0 | [E] | K10, K13; b09, d13, b07 |
| When a task says "random" or "typical", name the generating process before choosing a prior | G3/S0 | [E] | K01, K03; a01, a13 |
| Do not treat a flat prior as safe on small data; anchor to class history | S0/G1 | [E] | K05; a15, d03 |
| Supply base rates from the stored record, not from model recall, as a numbered line before the case text | S0/S1 | [E] | K12, K13; b06, b07, c15 |
| Never use a model-stated prior without an ESS or prior-predictive check; use private tasks for any elicitation test | S0/G1 | [E] leakage, [S] ESS | K19, K18; c07, a21 |
| Do not try to fix base-rate use by prompt wording alone | G5 | [E] | K15; c21, d11 |

### Test first

| Item | Part | Status | Evidence |
|---|---|---|---|
| Gate Brier with shrunk (k,n) vs raw rate vs model-recalled prior, n below 10 | S0/memory | [S] | K29; d05 |
| Pooled empirical default vs 0.5 for new classes | S0 | [S] | K30; d07 |
| Estimated prior strength vs fixed, by number of classes | S0 | [S] | K31; d06 |
| Beta-binomial conflict flag routes to a doubt step | S0/G1 | [S] | K32; d04, d08 |
| "Start from the class rate" vs "reason Bayesian" prompt | S0/G3 | [S] across models | K15; c21 |
| (k,n) vs percentage display | S0 | [C] humans; no LLM test | K16, K33 |
| Invariance step for under-specified random tasks | G3 | [C] | K02 |
| Posterior mean, not a pessimistic bound, into gate arithmetic | S0/gate | [S] | K35; d02 |
| Shuffle options to measure the label prior | G3 | [S] | K25; c19 |
| Measure the agent's own implicit prior by iterated learning | memory | [S] | K20; c01 |

## 8. Concrete tests on our bench

All arms get equal tokens; setup cost is counted (G7).

1. **Class record vs recalled prior.** Items: replayed run logs, classes with n below 10. Arms: raw k/n; Beta(1,1) shrinkage; pooled empirical Bayes; the model's recalled prior. Metric: Brier of the gate's pass prediction. Expected: shrinkage lowest. Simulation: 0.2339 vs 0.2678 vs 0.2794 (d05); real size unknown.
2. **Zero-history default.** Items: first run of each class. Arms: 0.5; pooled mean; Jeffreys. Metric: Brier. Expected: pooled about 0.01 better (0.240 vs 0.250 in simulation).
3. **Prior strength.** Items: log subsamples with 5, 10, 20, 50 classes. Arms: fixed s=2; method-of-moments s. Metric: Brier. Expected: fixed wins under 10, estimated wins from about 20.
4. **Display format.** Items: gate prompts with the same record as a bare percentage, (k,n), (k,n,ESS). Metric: share of final probabilities within 0.1 of the shrunk posterior; Brier. Expected: (k,n) closer.
5. **Base rate vs stereotype.** Items: Jason-style items with the class record as a line, plus stereotypical case text; 75/25 base-rate flip. Arms: model recall; stored record; code-computed posterior. Metric: odds ratio between base-rate conditions (normative 9) and prior-posterior correlation. Expected: code posterior near 9; model recall near 1-3 with stereotypes.
6. **Prompt wording.** Arms: "start from the stored class rate" vs "reason Bayesian" vs neutral. Items: dated forecast-style questions. Metric: Brier. Expected: about -0.016 and +0.025 vs neutral (c21); may not replicate on our models.
7. **Conflict flag.** Items: logs; flag when beta-binomial p is below 0.05. Metric: accuracy of flagged vs unflagged runs of the same class; false-alarm rate. Expected: flagged accuracy lower.
8. **Pure-noise seed.** Items: tasks whose class history shows no signal. Metric: rate of acting on noise with vs without a history prior. Expected: history prior lowers it (K05).
9. **Invariance step.** Items: Bertrand-style, cube-factory and "random" word problems. Arms: plain; named-process step. Metric: share that name the process and give the set of answers; correctness against the stated process. Expected: higher; may only add tokens.
10. **Repeatability.** Repeat each base-rate item 10 times; report the spread (K28).

## 9. What does not transfer, and why

- **Bertrand's chord and Jaynes's straws** are geometry with a physical process behind them. For the agent they give a procedure (name the process), not a number.
- **Maximum entropy and transformation groups** assume known constraints and a known symmetry group. Our classes have neither.
- **Efron-Morris** covers 18 players with a common rate structure. Our classes may differ in kind. Shrinkage helps only if the pool is a fair reference (d06, d07).
- **Natural frequencies** are a human format effect of unsettled size; the LLM version is untested.
- **Bayesian teaching by fine-tuning** (Qiu) is a training result. The scaffold analogue is a Bayesian helper in code.
- **AutoElicit and the 66-patient claim** cover linear-model weights and one clinical trial, on public datasets with leakage. Our private run logs make a model-stated prior less useful and more likely a hallucination.
- **Iterated-learning prior readout** assumes the model is an approximate Bayesian. We do not know that.
- **Simulation results** (K29-K32) use synthetic data with assumed pool strength 6. They show direction, not size.
- **Model numbers** are from 2023-2025 non-reasoning models. Reasoning models are untested.

## 10. Open questions

1. Does a stored class record (k,n shrunk) beat the model's own prior at the S0 gate on real logs for n below 10, and by how much?
2. Best zero-history default on our logs: Beta(1,1), Jeffreys, Haldane or pooled?
3. Does an explicit (k,n,ESS) display beat a bare percentage for LLMs?
4. Do 2025-2026 reasoning models still show similarity-over-base-rate (correlation about -0.9)? Does a code-computed posterior fix it?
5. Is base-rate-first robust across models and tasks, and does it stack with a stored class record?
6. How many classes are needed before estimated prior strength is safe on real logs?
7. Which conflict rule gives acceptable false-alarm and power at n of 5 to 10?
8. How large is leakage in LLM-stated priors, and do private tasks show smaller gains?
9. Does the 66-patient saving replicate?
10. Does the Jaynes invariance step change agent answers, or only add tokens?
11. Where Jaynes's and Drory's symmetry arguments disagree, which one matters for agent tasks, if any?

## 11. Sources

Marks: [V] opened (full or page text read), [M] snippet or second-hand only. Ids refer to the evidence files.

- [V] Jaynes (1973) The Well-Posed Problem (a01, a02, a03). http://bayes.wustl.edu/etj/articles/well.pdf
- [V] Jaynes (1968) Prior Probabilities (a04, a05, a06, a07). http://bayes.wustl.edu/etj/articles/prior.pdf
- [V] Stanford Encyclopedia of Philosophy: Bayesian Epistemology (a08, a09, a10, a11). https://plato.stanford.edu/entries/epistemology-bayesian/
- [V] Stanford Encyclopedia of Philosophy: Interpretations of Probability (a12, a13, a14). https://plato.stanford.edu/entries/probability-interpret/
- [V] Gelman, Simpson, Betancourt (2017) The prior can generally only be understood in the context of the likelihood (a15, a16, d03). https://arxiv.org/abs/1708.07487
- [V] Efron and Morris (1977) Stein's paradox in statistics (a17). https://www.gwern.net/doc/statistics/bayes/1977-efron.pdf
- [V] Capstick, Krishnan, Barnaghi (2025) AutoElicit, ICML (a18, a19, b20). https://arxiv.org/abs/2411.17284
- [V] Selby et al. (2025) Had enough of experts? Quantitative knowledge retrieval from LLMs (a20, a21, b18, b19). https://arxiv.org/abs/2402.07770
- [V] Gupta et al. (2025) Enough coin flips can make LLMs act Bayesian, ACL (a22). https://aclanthology.org/2025.acl-long.377/
- [V] Talboy and Fuller (2023) Challenging the appearance of machine intelligence: cognitive bias in LLMs (a23, b15). https://arxiv.org/abs/2304.01358
- [V] Jeffreys prior (Wikipedia summary) (a24). https://en.wikipedia.org/wiki/Jeffreys_prior
- [V] Bertrand paradox (Wikipedia summary) (a25). https://en.wikipedia.org/wiki/Bertrand_paradox_(probability)
- [V] Metacognitive Myopia in Large Language Models (a26, d15). https://arxiv.org/abs/2408.05568
- [V] CogBias: Measuring and Mitigating Cognitive Bias in LLMs (a27, b17, d11, d16). https://arxiv.org/abs/2604.01366
- [V] Jaynes (1973) The well-posed problem (b01). https://bayes.wustl.edu/etj/articles/well.pdf
- [V] Drory (2015) Failure and uses of Jaynes' principle of transformation groups (b02). https://arxiv.org/abs/1503.09072
- [M] Shackel (2007) Bertrand's paradox and the principle of indifference; Marinoff (1994) A resolution of Bertrand's paradox (b03). https://philarchive.org/rec/SHABPA
- [V] Zhu and Griffiths (2024) Eliciting the priors of large language models using iterated in-context learning (b04, b05). https://arxiv.org/abs/2406.01860
- [V] Li and Rui (2024) Dual traits in probabilistic reasoning of LLMs: Jason test (b06, b07, b08). https://arxiv.org/abs/2412.11009
- [V] Qiu et al. (2026) Bayesian teaching enables probabilistic reasoning in LLMs: baseline (b09, b10, b11). https://arxiv.org/abs/2503.17523
- [V] Weber, Binder and Krauss (2018) Why can only 24% solve Bayesian reasoning problems in natural frequencies (b12). https://www.frontiersin.org/articles/10.3389/fpsyg.2018.01833/pdf
- [M] McDowell and Jacobs (2017) Meta-analysing the effect of natural frequencies on Bayesian reasoning (b13). https://smdm.confex.com/smdm/16BEC/webprogram/Paper9915.html
- [V] Koehler (1996) The base rate fallacy reconsidered (b14). https://www.cambridge.org/core/journals/behavioral-and-brain-sciences/article/base-rate-fallacy-reconsidered-descriptive-normative-and-methodological-challenges/5C0138815B364140B87110364055683B
- [V] Macmillan-Scott and Musolesi (2024) (Ir)rationality and cognitive biases in LLMs (b16). https://arxiv.org/abs/2402.09193
- [V] Arai et al. (2025) How many patients could we save with LLM priors? (b21). https://arxiv.org/abs/2509.04250
- [V] Huang (2025) LLM-BI: fully automated Bayesian inference with LLMs (b22). https://arxiv.org/abs/2508.08300
- [V] Xie et al. (2022) An explanation of in-context learning as implicit Bayesian inference (b23). https://arxiv.org/abs/2111.02080
- [V] Arora et al. (2025) Bayesian scaling laws for in-context learning (b24). https://arxiv.org/abs/2410.16531
- [V] Halawi et al. (2024) Approaching human-level forecasting with language models (b25). https://arxiv.org/abs/2402.18563
- [V] Kadavath et al. (2022) Language models (mostly) know what they know (b26). https://arxiv.org/abs/2207.05221
- [M] Tversky and Kahneman 1974; Bar-Hillel 1980; Barbey and Sloman 2007 (base-rate respect) (b27). https://doi.org/10.1017/S0140525X07001653
- [V] Zhu & Griffiths (2024) Eliciting the Priors of Large Language Models using Iterated In-Context Learning (c01, c02, c03, c04). https://arxiv.org/html/2406.01860v1
- [V] Selby et al. (2025) Had enough of experts? Quantitative knowledge retrieval from large language models (Stat 14:e70054) (c05, c06, c07). https://arxiv.org/html/2402.07770v2
- [V] Capstick, Krishnan & Barnaghi (2024/2025) AutoElicit: Using Large Language Models for Expert Prior Elicitation in Predictive Modelling (c08, c09). https://arxiv.org/html/2411.17284v4
- [V] Anon (2025) How many patients could we save with LLM priors? (c10). https://arxiv.org/html/2509.04250v2
- [V] Huang (2025) LLM-Prior: A Framework for Knowledge-Driven Prior Elicitation and Aggregation (c11). https://arxiv.org/html/2508.03766v1
- [V] Atwell et al. (2025/2026) BASIL: Bayesian Assessment of Sycophancy in LLMs (c12, c13). https://arxiv.org/pdf/2508.16846
- [V] Dual Traits in Probabilistic Reasoning of Large Language Models (2024) (c14, c15, c16). https://arxiv.org/html/2412.11009
- [V] Metacognitive Myopia in Large Language Models (2024) (c17). https://arxiv.org/pdf/2408.05568
- [V] Huang et al. (2026) CogBias: Measuring and Mitigating Cognitive Bias in Large Language Models (c18, c26). https://arxiv.org/pdf/2604.01366
- [V] The Base-Rate Effect on LLM Benchmark Performance: Disambiguating Test-Taker Strategies from Benchmark Task Performance (2024) (c19). https://arxiv.org/html/2406.11634v1
- [V] Qiu et al. (2025) Bayesian Teaching Enables Probabilistic Reasoning in Large Language Models (c20). https://arxiv.org/html/2503.17523v2
- [V] Schoenegger, Jones, Tetlock & Mellers (2025) Prompt Engineering Large Language Models' Forecasting Capabilities (c21). https://arxiv.org/pdf/2506.01578
- [V] Halawi et al. (2024) Approaching Human-Level Forecasting with Language Models (c22). https://arxiv.org/html/2402.18563
- [V] Paruchuri et al. (2024) What Are the Odds? Language Models Are Capable of Probabilistic Reasoning (c23). https://arxiv.org/html/2406.12830
- [V] Dasgupta et al. (2022/2024) Language models show human-like content effects on reasoning tasks (c24). https://arxiv.org/abs/2207.07051
- [M] Jaynes (2003) Probability Theory: The Logic of Science; Bertrand (1889) paradox (c25). https://en.wikipedia.org/wiki/Principle_of_maximum_entropy
- [V] Winkler, Smith, Fryback (2002) The role of informative priors in zero-numerator problems: being conservative versus being candid (d01, d02). https://jimsmith.host.dartmouth.edu/wp-content/uploads/2022/04/The_Role_of_Informative_Priors_in_Zero_Numerator_Problems.pdf
- [V] Nott, Drovandi, Mengersen, Evans (2020) Checking for prior-data conflict using prior-to-posterior divergences (d04). https://arxiv.org/abs/1611.00113
- [V] Own simulation: Brier score of default priors for small classes (n<10) (d05, d06). D:/research_scratch/D02.03/tmp/D02.03_sim.py
- [V] Own simulation: zero-history default prior (d07, d08). D:/research_scratch/D02.03/tmp/D02.03_sim2.py
- [V] Chen and Lei (2025) Compound estimation for binomials (d09). https://arxiv.org/abs/2512.25042
- [V] Samanta et al. (2026) BayesBench: LLM belief trajectories under multi-turn evidence accumulation (d10). https://arxiv.org/abs/2606.30850
- [V] Pournemat et al. (2025) Reasoning under uncertainty: probabilistic reasoning capabilities of LLMs (d12). https://arxiv.org/abs/2509.10739
- [V] Chlon et al. (2026, v3) LLMs are Bayesian in expectation, not in realization (d13). https://arxiv.org/abs/2507.11768
- [V] Atwell et al. (2026, v6) BASIL: Bayesian assessment of sycophancy in LLMs (re-opened) (d14). https://arxiv.org/abs/2508.16846

## Source audit (2026-11-03)

Fresh auditors re-opened the sources of 13 established claims: 10 confirmed as written, 3 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **D02.03-K04** (reworded: the sources support less). Haldane/Jeffreys/uniform forms and 4/5 rule of succession check out, and Jeffreys is reparameterisation-invariant, but the sources do not support calling it 'the default': Jaynes 1968 argues for 1/(t(1-t)) for total ignorance and Gelman et al. say no default prior is safe independent of the likelihood. Corrected claim: For an unknown pass rate, the choice among Haldane (1/(t(1-t))), Jeffreys Beta(1/2,1/2) and uniform Beta(1,1) changes early estimates (the rule of succession gives 4/5 after 3 successes under uniform). Jeffreys is the choice that is invariant under reparameterisation, but Jaynes argues for Haldane as the ignorance prior and Gelman, Simpson and Betancourt argue that no default is safe without checking its implications for the likelihood.
- **D02.03-K19** (reworded: the sources support less). Numbers 6/5/2 of 11 verified in Selby et al., but that is the only supporting paper (b19 and c07 are the same paper; AutoElicit does not address leakage), and dataset recognition shows possible contamination, not that scores were inflated. Corrected claim: In Selby et al. (2025), given a single row, GPT-3.5 recognised 6 of 11 datasets, Gemini 1.5 Pro 5 and Llama 2 70B 2, so data leakage is a possible contaminant of tests of LLM prior knowledge (single study; inflation of scores not shown).
- **D02.03-K24** (reworded: the sources support less). Arora et al. find that on toy GPT-2/GINC models SFT mostly shifts the task prior while DPO also disrupts task knowledge; the real-model (Llama 3.1) evidence is inferred from fitted parameters and the authors say they do not claim LLMs are Bayesian learners; Xie et al. support only the in-context mixture framing. Corrected claim: Bayesian scaling laws (Arora et al. 2025) find that in toy models SFT mostly shifts the model's task prior rather than its task knowledge (DPO also disturbs task knowledge), and fitted parameters on Llama 3.1 8B Base vs Instruct are read as further, non-conclusive evidence of the same; Xie et al. (2022) frame in-context learning as implicit Bayesian inference over a pretraining mixture of latent concepts with a prior.
- **D02.03-K03** (now single-source: only one opened source, code check).
