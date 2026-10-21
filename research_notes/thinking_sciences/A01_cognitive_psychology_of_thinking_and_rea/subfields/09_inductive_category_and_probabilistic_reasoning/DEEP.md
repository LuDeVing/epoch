# Inductive, category-based and probabilistic reasoning: deep document

Scope: generalising from cases. Category-based induction (Osherson et al., Heit, Kemp and Tenenbaum), Bayesian concept learning (the number game), rule induction, base-rate neglect and natural frequencies, the conjunction fallacy, probability judgment and its calibration, and what language models do on all of these, including hypothesis-search methods.

Evidence base: 4 evidence files (a, b, c, d; about 100 lines), 36 claims (K01 to K36) and a cross-check critique. Evidence ids below (a01, b15, d07 and so on) point into those files. Claim ids (K..) point into claims.jsonl.

How to read the status marks. [E] means two or more independent sources agree. [S] means one source, or one lab, or one paper counted several times. [C] means contested. Where a number was corrected by the cross-check, the corrected number is used here.

Overlap with earlier documents in this series: content effects (03), belief bias (04) and dual process (05) already cover why famous items are answered from memory and why "slow down" prompts fail. This document refers to them and does not repeat them. What is new here: the induction models, the format and menu effect in Bayesian problems, the conjunction fallacy controls, and the hypothesis-search literature, which is the closest published match to schema states S2 to S4.

---

## 1. What it is

Induction means going from some cases to a claim that goes beyond them. Three families of tasks sit under this name.

1. **Property induction over categories.** "Robins have property X, so do sparrows?" People rate how strong such arguments are. The classic stimuli are Osherson et al. (1990) argument sets over mammals and birds. The question is how premise features (similarity, typicality, diversity, number) change the strength of a conclusion.
2. **Concept and rule induction.** From a few examples, find the rule and predict new cases. Examples: the number game (given 16, 8, 2, 64, is 32 in the set?), list functions, string transformations, ARC grids.
3. **Probability judgment.** Combine a base rate with new evidence (Bayesian updating), or judge the probability of a conjunction. Base-rate neglect and the conjunction fallacy are the standard errors.

All three are the same problem seen from different sides: choose among many hypotheses that fit the data, weigh them, and predict. The Bayesian view says: keep a prior over hypotheses, multiply by the likelihood of the examples, average the predictions. The heuristics-and-biases view says: people use similarity and representativeness in place of that calculation. Both views have solid evidence. The practical question for our agent is where a language model can be trusted to do this inside its prose, and where the scaffold should move the step into code.

Why this matters for the schema. S2 (represent) asks the model to write 1 to 4 candidate rules. S3 to S4 generate and test them. S7 selects among those that pass. G5 says that probability handling is done in code. This subfield supplies the best-tested version of exactly that loop (hypothesis search) and the best-tested failure it must guard against (selecting the wrong hypothesis, or fitting the examples and failing the test).

---

## 2. History and theories in depth

### 2.1 Similarity-coverage and the classic phenomena (1990)

Osherson, Smith, Wilkie, Lopez and Shafir (1990) proposed the similarity-coverage model (SCM). Argument strength depends on two things: how similar the premise categories are to the conclusion category, and how well the premises "cover" the smallest category that contains both premises and conclusion. They listed 13 qualitative phenomena that the model accounts for. The original paper was seen as an abstract only [M] (a25); everything below about it comes from later papers that describe it (a01, a03, a04, a05, a07).

The core phenomena, with the standard examples from Kemp and Tenenbaum (a03) and Heit's review (b05 to b09):

- **Similarity.** More similar premise and conclusion categories give a stronger argument.
- **Typicality.** Typical premise categories are better evidence than atypical ones. Horses support "all mammals" better than seals do.
- **Diversity.** Diverse premises beat similar ones. "Seals and squirrels have it, so all mammals" beats "horses and rhinos have it, so all mammals".
- **Specificity.** Specific conclusions are easier to reach than general ones.
- **Sample size.** More observed members give stronger inductions, still short of certainty. In Heit's review, 1, then 3, then 20 observed members gave stronger and stronger inferences (b09).
- **Non-monotonicity.** Adding a premise can lower strength. "Flies and orangutans, so bees" was judged weaker than "flies, so bees" (b07). Another example: {crow, peacock, rabbit} to birds is weaker than {crow, peacock} to birds.

Sloman (1993) proposed a feature-based model with no category hierarchy: strength depends on feature overlap and falls with the familiarity of the conclusion category (a29).

### 2.2 Heit's Bayesian account (1998, 2000)

Heit (1998; reviewed in Heit 2000, b08) recast induction as Bayesian inference. A new property acts as a cue that retrieves familiar properties. The prior is how widely those retrieved properties are shared. Typicality, similarity and diversity then follow without special rules. Heit's own worked table with four hypotheses is illustrative, not a fitted model (b08). Kemp and Tenenbaum describe the weak point: the model has no formal way to generate the prior (a04, a26). The 1998 chapter itself was not opened [M].

Review notes on robustness (b05 to b09):

- Diversity is the least robust effect. It was found in adults in several studies. It was not found in 9-year-olds with specific conclusions (Gutheil and Gelman; Lopez et al. 1992). Heit and Hahn (1999) found it in children aged 5 to 8 with pictures of dolls and hats: 74% of critical items chose the diverse set.
- Culture and knowledge change diversity. Itzaj Maya adults did not show it for disease-spread arguments on living things and sometimes preferred homogeneous premises. They explained their choices with disease-transmission knowledge that conflicts with diversity. They did show the pattern for a corn-cob sampling problem. Korean students showed it (Choi, Nisbett and Smith 1997).

### 2.3 Structured Bayesian models (Tenenbaum, Kemp and Shafto 2007; Kemp and Tenenbaum 2009)

Kemp and Tenenbaum (a01) pose property induction as inference about a partly observed feature vector over known categories. The learner has a prior over all possible extensions of a new property. The prior comes from structured background knowledge. Four structures were studied: a taxonomic tree, a 2D space, a threshold (ordered) structure, and a causal graph. Different structures give different inductive contexts.

The default model for biological properties is a tree plus a diffusion process (a property changes slowly along branches) plus Bayesian inference. Correlations with human ratings on five datasets: r = .96, .90, .95, .96, .85 (a02). The datasets are Osherson-specific, Osherson-mammals and three Smith sets. The column order was inferred from figure text, so treat the mapping as uncertain.

Tenenbaum, Kemp and Shafto (a05) ran a model comparison on the same five datasets. Fit (r) per dataset:

| Model | D1 | D2 | D3 | D4 | D5 |
|---|---|---|---|---|---|
| Evolutionary (Bayesian tree) | .93 | .92 | .89 | .98 | .80 |
| MaxSim (coverage by best match) | .71 | .79 | .93 | .94 | .84 |
| Raw feature model | .70 | .27 | .77 | .95 | .68 |
| SumSim (summed similarity) | .74 | -.34 | .85 | .92 | -.02 |
| Strict tree | .56 | .50 | .56 | .85 | .67 |

Row order read from figure text. D1 is Osherson specific (36 two-premise arguments, conclusion horses). D2 is Osherson general (45 three-premise arguments, conclusion mammals). The other three are Smith sets.

What the comparison teaches (a05, a06):

- SCM's "coverage" term is the average over category members of the maximum similarity to the premises (MaxSim). SumSim fails on general arguments (r = -.34 on D2, -.02 on D5). Its total strength is linear in the single-premise strengths, so it prefers premises that are each strongest alone, and those are similar to each other (horses, cows, rhinos beat horses, seals, squirrels for "mammals"). That is why it cannot show diversity.
- The strict tree gives 100% to every set spanning the same node, so it cannot give graded diversity. Graded, soft weighting of hypotheses is needed.
- A memory-based raw prior reaches r = .81 to .96 on some sets but fails on diversity (a02). A 2D spatial model is poor on Osherson-mammals (r about .64), which needs diversity.
- The authors state their account is computational-level. They model the content of intuitive theories as priors and are agnostic about process (a30).

Strength and weakness. The fit is strong. But all of it is one lab, fitted to averaged ratings, with hand-chosen structures (K13). Treat it as a good description of what people do, not as a proven mechanism.

### 2.4 Context decides the structure

The same premises point in opposite directions in different contexts (a03). A bear disease is judged more likely in salmon than in moose (ecological reasoning: bears eat salmon). Anatomical properties follow taxonomy. Wu and Gentner (a17) found that when people choose between an inference from a shared attribute and one from a shared causal antecedent, they prefer the causal one: 13 of 16 participants in Experiment 1 and 14 of 16 in Experiment 2 chose predominantly causal. Samples were tiny, and the authors note a salience confound (the causal information was one long sentence).

Hampton and Cannon (a07) added a bias: typicality of the conclusion category raises strength, which SCM does not predict. Exp 1 (36 raters, 22 triplets): per-participant regression with similarity beta = -.34 (t(17) = -8.00) and conclusion typicality beta = -.12 (t(17) = -3.27); premise typicality was not significant. Exp 3 forced choice, N = 48: the typical conclusion was chosen 58% of the time (chance 50%; 34 of 48 people; 17 of 22 items). Familiarity was ruled out (r about .1). The effect is small. The authors note a defence open to SCM: a typical conclusion may cue a narrower superordinate, so coverage rises (a08). So SCM is not cleanly refuted.

### 2.5 Bayesian concept learning and the number game (Tenenbaum 1999, 2001)

The number game is the cleanest test of rule versus similarity generalisation. Given a few numbers from a hidden set (from 1 to 100), people judge which other numbers belong. The Bayesian model has a hypothesis space of maths rules (squares, cubes, primes, powers of 2, multiples, even, odd, endings in a digit) and intervals. Its key idea is the **size principle**: a smaller hypothesis that contains all the examples is more likely than a larger one, and exponentially more so as examples accumulate. Likelihood is P(X|h) = (1/|h|)^n if all n examples are in h, else 0. Prediction is P(y in C | X) = sum over h of P(y in h) P(h|X). This is "strong sampling": examples are assumed drawn from the true concept.

A teaching version (a10) uses 34 maths rules plus 5,050 intervals, prior 2/3 on maths rules. After one example (16): powers of 4 get .33, powers of 2 .16, squares .10, ending in 6 .10. After 16, 8, 2, 64: powers of 2 have likelihood (1/6)^4 = .00077 against even numbers (1/50)^4 = .00000016. That is the "suspicious coincidence" effect: four powers of two in a row are too unlikely if the rule were "even". As examples grow, generalisation moves from similarity-like to rule-like (a09, abstract only [M]). The teaching page is a demonstration, not the human experiment.

### 2.6 Probability judgment: base rates, frequencies, conjunctions

- **Base-rate neglect.** The mammography problem (a24): prevalence 1%, sensitivity 80%, false-positive rate 9.6%. The right posterior is 7.8%. Eddy (1982) reported physician estimates of 70% to 80% (cited, not re-measured). In natural frequencies: 10 of 1,000 have cancer; 8 of those test positive; 95 of the other 990 test positive; so 8 out of 103.
- **Natural frequencies** (Gigerenzer and Hoffrage 1995, a11, a12, a24, d07). Same problem, different format. Section 3 has the numbers. The computational account: counts that carry the base rate make the Bayes step a simple ratio.
- **Rival account for the conjunction fallacy.** Tversky and Kahneman (1983, a14 to a16) found people rank "bank teller and feminist" above "bank teller". The explanation is representativeness. Hertwig and Gigerenzer (1999) argued "probable" is polysemous and the effect is partly conversational (b26, snippet only [M]). Sides et al. (2002, b10 to b12) tested this with betting and hidden-sentence controls and found the fallacy survives.
- **Nested sets.** Neace et al. (2008, d08) argue the frequency benefit in the Linda problem comes from giving a concrete reference class and nested sets, not from the frequency wording.

### 2.7 LLM induction as hypothesis search (2023 to 2026)

The Bayesian view became an engineering recipe: have a language model propose hypotheses in words, turn each into code, run the code on the examples, keep what fits (a20, c10; Ellis 2023, c14; Qiu et al. 2024, c06). Section 6 has the results. The key thread: the proposal step works, the selection step is the bottleneck, and examples that are fitted are not proof.

---

## 3. Core findings with exact numbers

Status uses: established [E], single-source [S], contested [C]. "Source" gives evidence ids.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Natural frequencies raise Bayesian solving vs probabilities (Study 1, 60 Salzburg students, 15 problems, 1,774 coded solutions) | Bayesian algorithms: probability 16% (standard menu), 28% (short menu); frequency 46% (standard), 50% (short). Format effect about 29.9 and 21.6 points. Menu effect 12.1 and 3.7 points. Overall 34.9% Bayesian (620 of 1,774). Mammography: 43.3% gave 8 out of 103. | a11, a24, d07 | [E] (4 independent groups, K01) |
| Relative frequencies (percent) do not help | Study 2, 15 Konstanz students: 60 Bayesian solutions with relative frequencies vs 66 with probabilities. These are counts of coded solutions, not percentages. | a12 | [S] (K03) |
| Frequency benefit is large only for the numerate | Chapman and Liu, 346 students (abstract says 342). High numerates (n = 190) correct with frequencies: 27% (medical), 31% (car); low numerates (n = 156): 7% and 10%. Format x numeracy chi2(1) = 13.29, p = .0003. Numeracy chi2(1) = 17.78; format main effect chi2(1) = 3.61, p = .06. | a13, a27 | [E] |
| Most people still fail with frequencies | Weber et al., N = 180: 20% correct with probabilities, 36% with frequencies. Heroin task 51% vs car task 22% with frequencies. Meta-analysis figure quoted by them: 24% vs 4%. | b01, b02 | [E] (the 24% vs 4% is second-hand from McDowell and Jacobs 2017, not opened) |
| Individual differences dominate | Marginal R2 = .065 (fixed effects), conditional R2 = .685 (with person intercepts). 49% of those shown frequencies still calculated with probabilities; 18% shown probabilities switched to frequencies. Correct by calculation format used: frequencies 61% (shown freq) and 53% (shown prob); probabilities 13% and 9%. | b01, b03, b04 | [S] |
| Switching to probability formulas is habit, not ability | Frequency algorithm used in 32% of solutions by the strong-maths subgroup (n = 42) vs 35% in the rest (p = .613), though accuracy was 50% vs 21%. | b04 | [S] (authors' reading) |
| Menu confound in the frequency effect | Short menu (joint counts) alone lifts probability format from 16% to 28%. The format gap survives at fixed menu (22 to 30 points). | a11, d07 | [S] for LLMs (no study crosses them); [E] for humans |
| Linda frequency benefit may be a reference-class effect | With reference class held fixed, frequency and probability formats did equally well. Exp 1 N = 100 students (full tables not read). | d08 | [S] |
| Conjunction fallacy in rank tests | Violation rates: naive Bill 92%, Linda 89%; informed Bill 86%, Linda 90%; sophisticated (decision science doctoral students) Bill 83%, Linda 85%. Choice T vs T&F: 85% chose T&F (N = 142). 9-point scale (N = 119): T mean 3.5, T&F mean 5.6; 82% rated T&F higher. | a14 | [E] |
| Wording and betting reduce but do not remove the error | Bet on T or T&F: 56% fallacy (n = 60). "Whether or not" wording: T* vs T&F means 3.8 vs 5.1; 57% (n = 75) rated T&F higher, 16% lower. Argument choice: 65% (n = 58) picked the invalid resemblance argument. | a15 | [E] |
| Frequency wording shrinks the conjunction error (heart-attack survey) | Percent version: 65% (N = 147) gave a strictly higher estimate to the conjunction. Frequency version "how many of 100": 25% (N = 117). Estimating both constituents first: 11% (N = 360). | a16 | [C] (K08) |
| Fallacy survives betting and hidden-sentence controls | Exp 1 (N = 45 per cell): probability 3.4 errors of 9 vs betting 3.2; 36 of 45 bettors erred at least once. Exp 3 (92 probability, 60 betting): 90 of 92 erred at least once; 4.33 vs 4.85 errors of 9 (p < .06); item rates correlate r = .96 across conditions. Houston Exp 2: 5.93 vs 4.86, p < .07. | b10, b11, b12 | [E] |
| Category induction cluster (similarity, typicality, specificity, sample size, diversity) | Qualitative; diversity weakest; 74% diverse choices in children aged 5 to 8 (Heit and Hahn). | b05 to b09, a03 | [E] (K11) |
| Conclusion typicality raises strength | beta = -.12 (t(17) = -3.27); forced choice 58% (N = 48; 34 of 48 people; 17 of 22 items). | a07 | [S] |
| Causal structure preferred over shared attributes | 13 of 16 and 14 of 16 participants predominantly causal. | a17 | [S] (tiny samples) |
| Structured Bayesian fits | Tree + diffusion r = .96, .90, .95, .96, .85. Evolutionary .93, .92, .89, .98, .80 (a05). | a02, a05 | [S] (one lab, K13) |
| SumSim fails on general arguments | r = -.34 (Osherson general), -.02 (Smith set 5). MaxSim .79 and .84. | a05 | [S] |
| Hypothesis search on ARC (GPT-4, 100 tasks, top-1) | Direct 17%; program only 23%; summarised hypotheses 30%; human-selected 33%; human-written 45%; Icecuber (non-LLM DSL) 43%. Chain of thought without code 19%. Only 49 of 100 tasks had a correct hypothesis; 33 of 49 (67%) converted by human selection. | a20, a21, b17, b18, c10, c11 | [S] (one paper, K15) |
| Execution feedback rounds plateau | ARC summarised 24, 28, 28, 30 at rounds 0 to 3; human-selected 26, 31, 33, 33; human-written 38, 44, 45, 45. | a21, c11 | [E] with c06, c09 (K18) |
| Easier benchmarks gain more | 1D-ARC (108 tasks): 39.6 / 61.1 / 73.1 (direct / program / full). List Functions (100 tasks): 31 / 59 / 69. SyGuS (89 tasks): 94.3% both with and without hypotheses (CrossBeam 74.8%). | a22, b19 | [S] |
| Pool vs selection (second study) | GPT-4o, 100 list functions, 11 trials, 5 runs: correct hypothesis in generator pool 46.4%; after model summary 34.5% (26% of correct ones dropped, 12.1 points lost). Both ok: test solved 95.9%. Generator ok, summariser failed: 75.3%. Both failed: 1,092 trials rescued (37.0% of that subset, 19.9% of all). Test mean accuracy: hypothesis search .487, humans .521, direct GPT-4o .359. | d01, d02 | [S] (one paper), but agrees with a21 on direction |
| LMs propose rules well, apply them badly | GPT-4: ACRE 28.0 to 45.0 to 48.0; MiniSCAN 0.0 to 46.0; List Functions 39.6 to 52.0 (T=1,N=1; 42.4 at T=3,N=1). Applied by the LM itself, MiniSCAN falls from above 80% to almost 0. Self-refine with the LM as interpreter on ACRE: 32.0. Self-consistency on ACRE: 29.0. | b20, c06, c07 | [S] (one paper, K17) |
| Refinement is shallow | MiniARC: plain 13.8; refinement 3.8 (T=1,N=1), 9.2 (T=1,N=5), 14.6 (T=3,N=5). Edits mostly add if-else exceptions for the failing example. | c06, c09 | [E] on the plateau; MiniARC detail [S] |
| Brute-force program sampling scales with log samples | About 8,000 programs per problem from GPT-4o, 50% on the ARC public test set (72% on a held-out train subset where humans score 85%); about +3 points per doubling of samples; revision fixes about 20% of the remaining wrong. | c12 | [E] with c13 (K20), but blog post |
| Induction and transduction solve different tasks | 2048 induction samples 18.78%; transduction 15.25%; ensemble 26.50%. Best system 56.75% vs average human 60.2%. | c13 | [S] (trained models) |
| Fitting the examples is not proof | About 9% of ARC tasks: program fits train, fails test (c13). CodeARC, 1,114 functions: o3-mini first attempt 67.6% pass the 10 examples, 38.9% pass the oracle, 28.7% (640 problems) fit and are wrong. Wang et al.: one exception in 100 tasks. | c13, d06, a21 | [E] (K22); rate depends on how well examples pin the function down |
| Number game: LLM anchoring on one example | 255 example sets, 10 trials. Rule bias .9 humans vs 1.0 GPT. Mean GPT-human divergence .87. At 4 examples GPT-Bayes divergence is comparable to human-Bayes. GPT best fit by maximum-likelihood without a prior. | c15, d05 | [C] (K23) |
| Noise breaks LLM induction | List Functions, 12.5% / 25% / 50% of 8 exemplars corrupted (1, 2 or 4 examples): accuracy falls from one bad example. SRR (diverse subsets plus code check) best in 10 of 14 cells at 10% noise, 2.1% average gap. | b21, c08, d16 | [S] |
| Recalibration of probabilities | Human experts: single power parameter, relative Brier gain 0.569 (inflation), 0.452 (GDP), 0.574 (unemployment); 1-year horizon 0.621, 0.539, 0.623. LLMs: Platt scaling on 1,614 questions (trained on 7,824), Claude-Sonnet-4 Brier .146 to .129; Llama-3.3-70B .157 to .138 (isotonic .265); Qwen3-32B .158 to .137; Qwen3-8B .185 to .141; AUC .723 to .724; ECE .104 to .038; human crowd Brier .061. | b13, d14 | [C] (K27; ECE gains can hide lost resolution, d15) |

---

## 4. Mechanisms and models

Each model below is written so it can be coded. Inputs and outputs are plain values.

### 4.1 Similarity-coverage (SCM)

Inputs: a similarity function sim(a, b) between categories; premise set P; conclusion c; the lowest category L containing P and c, with members M(L).

Score: strength = alpha * sim(P, c) + (1 - alpha) * coverage(P, L).
- sim(P, c) = max over premises p of sim(p, c) (the max-similarity form).
- coverage(P, L) = average over m in M(L) of max over p in P of sim(p, m).

Notes. One free parameter alpha in the fits (a04). SCM with human similarity ratings did better than with feature covariance. Use MaxSim, never SumSim (a05). It only fits blank properties (a property with no known meaning). It is cheap but needs a similarity function; GPT-4 similarity ratings correlated above .6 with human ratings in all three domains, and feeding them into SCM improved GPT-4's general arguments (a19, c05).

### 4.2 Bayesian property induction with a structured prior

Inputs: categories C1..Cn; a prior P(extension) over which categories have the new property; observed premises.

1. Build the structure for the context: tree (taxonomy), 2D space, threshold, or causal graph (a01).
2. Define the prior by a process on the structure. For a tree with diffusion: the property flips along branches with a small rate; sample or enumerate extensions, weight by that process.
3. Condition on the premises: keep the extensions where all premise categories have the property, renormalise.
4. Answer: P(conclusion has the property) = sum of prior mass of extensions that include it and the premises, over the mass of extensions that include the premises.

Implementation note. With a small category set (under 20), enumerate all 2^n extensions. A soft prior is needed: a strict tree gives 100% to every set that spans the same node, which kills diversity (a06). The model supplies the structure, the program does the inference (a30).

### 4.3 The number game as code (size principle)

Inputs: hypothesis list H with set membership; prior P(h); examples X (n of them).

1. For each h: if all examples are in h, likelihood = (1/|h|)^n. Otherwise 0.
2. Posterior P(h|X) proportional to prior times likelihood.
3. P(y in concept) = sum over h of [y in h] * P(h|X).

Weak sampling (likelihood 1 if consistent) is the contrast model (a10). Ellis (c14) replaced the hand-built hypothesis list with an LLM proposal list: about 50 to 100 proposals matched human data, against over 5,000 hypotheses in the original model. A learned prior and a likelihood re-weigh the proposals. English hypotheses fit better than Python ones. Human data came from 8 participants.

For our agent, this is the "propose then weigh in code" recipe for any rule-induction item: the model proposes hypotheses and their extensions on a probe set, the program applies the size principle. It also gives the "suspicious coincidence" check: if all examples sit inside a small hypothesis that is much narrower than the one the model picked, that is evidence for the narrow one.

### 4.4 Hypothesis search (Wang et al.)

Pipeline (a20, a21):
1. Ask the model for many natural-language hypotheses (64 for ARC and list functions, 16 for 1D-ARC).
2. Optionally summarise down to a shortlist (8 for ARC). Per the second study, this step drops about a quarter of the correct hypotheses (d01).
3. For each hypothesis, ask the model to write Python (8 programs per hypothesis on ARC; 4 on 1D-ARC; 1 on List Functions).
4. Run each program on the training examples. Up to 3 rounds of execution feedback, with the gain plateauing at about 2.
5. Pick a program that fits all training examples. Predict the test input.

Costs: up to $1.5 to test one candidate hypothesis with 8 programs and 2 feedback rounds on ARC (b17). Worst case 257 calls per task in Parab et al. (d01).

Stage-level rates (d01, d02): generator pool has a correct hypothesis 46.4% of the time; implementor succeeds on train and test about 19 and 17 times more often given a correct hypothesis (p < .001); trial-level r = .57 train and .55 test; task-level r = .93 and .79. Program execution can rescue failed front ends: 37.0% of the "both failed" subset.

### 4.5 Brute-force program sampling (Greenblatt)

About 8,000 programs per problem from GPT-4o; keep those correct on all training examples; revise some from the diff against the truth; majority vote over survivors; submit the top 3 (c12). 50% on the ARC public test set. About +3 points per doubling of samples. Two submissions: 48% (test), 70% (train). The log-linear trend cannot continue forever. Compare G12: spend by difficulty.

### 4.6 Induction plus transduction

Induction means writing a program that explains the examples. Transduction means predicting the output directly. On ARC they solve largely different tasks (c13). Induction is better at precise computation and composing concepts. Transduction is better at fuzzy perceptual concepts. Ensemble: induction first, transduction as a fallback. Their systems were trained (Llama 3.1 8B on synthetic data), so only the idea transfers.

### 4.7 Base-rate update as code

Inputs: prior pi, hit rate h, false-alarm rate f.
Posterior = pi*h / (pi*h + (1-pi)*f).

Count form (what the frequency format teaches): pick N (for example 1,000). Positives with condition = N*pi*h. Positives without = N*(1-pi)*f. Posterior = first / (first + second). Mammography test: pi = .01, h = .80, f = .096 must give 7.8% (a24). Keep the count table as a visible object, since the benefit of natural frequencies comes from carrying the base rate and the joint counts (a12).

### 4.8 Conjunction check as code

For any event probabilities the agent states, enforce P(A and B) <= min(P(A), P(B)) and P(A or B) >= max(P(A), P(B)). Exclusive and exhaustive answers must sum to 1; the schema already notes that normalising in code cut error by about 35% (G5). A violation triggers a re-ask, not a silent fix.

### 4.9 Recalibration

Fit on held-out (confidence, outcome) pairs. One-parameter version: transform probability p to p^k / (p^k + (1-p)^k) on log odds, with k fitted to minimise Brier (Han and Budescu, b13). Two-parameter Platt version: logistic of slope times logit(p) plus intercept (d14). Accept only if Brier improves, not just ECE (d15: Platt and Beta scaling drove T-ECE from above 0.400 to below 0.030 while Brier stayed high, a sign of lost resolution). Human results: b13. LLM results: d14. Minimum sample size is unknown.

---

## 5. What holds up

### 5.1 Replications and independent confirmations

- **Natural frequencies help.** Independent confirmations: Gigerenzer and Hoffrage (a11), Chapman and Liu (a13), Weber et al. (b01), and the meta-analysis quoted by Weber (b02, 24% vs 4%, second-hand). Direction holds. Size is far smaller than the headline. The correct-answer level with frequencies is 24% to 36% in later work, not about half.
- **The conjunction fallacy is robust in humans.** Tversky and Kahneman's rates of 83% to 92% in rank tests (a14) and Sides et al. (b10 to b12) agree: the fallacy survives betting and hidden-sentence controls (K07).
- **Category-induction cluster.** Similarity, typicality, specificity and sample size are robust in adults. Han et al. re-ran 11 phenomena with 110 people (c01): humans did not robustly show diversity, asymmetry or the inclusion fallacy, so even the textbook list is uneven.
- **Fitting the examples is not proof.** Three independent sources: c13 (about 9%), d06 (28.7% of first attempts), and a21 (one exception in 100, the lowest rate). The rate depends on how tightly the examples fix the function.
- **Refinement plateaus after about 2 rounds.** a21, c06, c09 agree.

### 5.2 Failures, boundary conditions and competing explanations

- **Frequency benefit is not universal.** Numeracy and person dominate: marginal R2 .065 vs conditional R2 .685 (b03). Low numerates reach only 7% to 10% even with frequencies (a13). Task story matters: heroin 51% vs car 22% (b01).
- **Frequency format is confounded with menu.** Short menu alone adds 12.1 points at probability format (a11, d07). Nested-set account: the Linda benefit disappears when reference class is controlled (d08).
- **Why people still fail with frequencies.** Weber et al. say habit: 49% of people shown frequencies still compute with probabilities (b01, b04). The Einstellung explanation is read from written work, not manipulated.
- **Conjunction fallacy: wording matters but cannot be the whole story.** Frequency wording dropped it from 65% to 25% (a16). Betting and hidden-sentence controls left it at the same level (b10 to b12). The polysemy account (b26) was not opened. The sizes are not comparable across papers.
- **Diversity depends on culture and knowledge.** Itzaj Maya adults did not show it for disease-spread arguments (b06). Children 9 and under give mixed results (b05).
- **Non-monotonicity as a pragmatic effect.** Humans judge {crow, peacock, rabbit} to birds weaker because a helpful speaker would not add rabbit. This is the authors' reading (c02). It was not tested in a model by changing the sampling assumption (K36).
- **SCM is not cleanly refuted by conclusion typicality** (a08).
- **Structured models.** One lab, averaged ratings, hand-chosen structures (K13).
- **Hypothesis search value depends on the task.** On SyGuS, hypotheses add nothing (94.3% both ways, b19) because direct coding already works. On 1D-ARC and List Functions they add 12 to 38 points (a22). With Parsel, human hypotheses reached 47.5% vs 37.5% direct, but LLM hypotheses got worse (b19). Right-but-hard-to-code hypotheses and wording mismatches are failure causes (a23).
- **Different versions of the Wang et al. paper quote different ARC numbers** (27.5% vs 12.5% on 40 tasks in a snippet, c10). The 100-task figures are from the PDF read.

### 5.3 Interventions that worked

- Converting probability problems into absolute counts that carry the base rate (a11, a12, a24; humans).
- Asking for the parent class before the subclass (11% violation, a16).
- Executing candidate rules in a symbolic interpreter (b20, c06) or in real code (a20).
- Keeping the whole hypothesis pool and ranking by code run on the examples (d01, d02).
- A code interpreter for counting frequencies: GPT-4.1-mini was nearly restored to the frequency-provided setting (d13).
- Diverse subsets plus code check against noisy examples (d16).
- Recalibration of confidences, subject to checking Brier (b13, d14).
- Letting the agent query for new inputs and use counterexamples (CodeARC, d06: success rises with more I/O budget and oracle calls).

### 5.4 Interventions that did not work

- **Bias-avoidance prompts for judgment biases.** CogBias (3 models, T=0): response biases +40.5%, judgment accuracy -4.4% (d12, c27). Not frontier models, and the judgment family pools base rate with anchoring, sunk cost and status quo.
- **Telling the model to apply Bayes' rule.** Correlation between posterior and similarity did not change until the most forceful step-by-step prompt (b16, one model, one vignette).
- **Telling the model to use natural frequencies.** Followed only partly, with mixed formats and one wrong 50% answer (b24, c22; one problem, three models). These two lines are one author, about 1.5 sources.
- **Self-consistency and chain of thought for self-applied rules.** They did not close the induction-application gap (c07).
- **Extra refinement rounds.** Plateau; refinement can hurt on hard tasks; edits are shallow exceptions (c06, c09).
- **A model-written shortlist.** Loses a quarter of the correct hypotheses (d01).
- **Telling the model some examples may be wrong.** Helped only partly (b21).
- **Showing a candidate list in the number game.** Did not recover the Bayesian posterior (c16). Note a different prompt, "explicit candidate list" with a shown list, is what Xiong tested; the version where the agent builds its own list and weighs it in code is the Ellis route, which worked (c14).

---

## 6. Language models

### 6.1 Category-based induction

Han et al. (a18, a19, c01 to c05) tested GPT-3.5 and GPT-4 on 11 phenomena with 792 argument pairs (mammals, birds, vehicles); 120 people recruited, 110 kept, about 9.2 human ratings per cell.

- GPT-4 (snapshot 0314) matched the human direction on all but one phenomenon: specific non-monotonicity. There it chose the opposite of people and said "more examples make the conclusion stronger".
- GPT-3.5 was driven by surface features such as which argument came first. The authors' earlier study that balanced argument order had found it capturing similarity, typicality and specificity (c04). So this is a prompt-order artefact.
- GPT-4 showed diversity for general arguments where humans did not (b22).
- Rating experiment: GPT-4 nearly matched the Human-SCM benchmark on specific arguments, but was uncorrelated with humans on single-premise general mammal arguments. GPT-3.5 beat GPT-4 on general arguments. Running SCM on GPT-4's own similarity ratings improved the general arguments. GPT-4 similarity ratings correlated above .6 with human similarity in all three domains (c05).
- Prompt design mattered: 288 combinations, a hand-picked subset tested; the best Exp 1 prompt carried a chain-of-thought direction. Exp 2 best prompt included practice trials (c03). The best prompt was chosen on the same data it was reported on. The prompt tuned for chat models failed on models without instruction tuning.
- The .65 Spearman is a human-versus-1990 replication check (40 people on the 36 Osherson arguments), not a model score.
- Base language models use both taxonomy and similarity when projecting nonce properties across 2,016 taxonomically related pairs. The two are not separable (d17).

Caveats: GPT-3.5 and GPT-4 snapshots from 2023. No test of current models. No follow-up that adds a "why were these premises chosen" prompt was found (d18, K36).

### 6.2 Base rates and probability

- Six LLMs follow Bayes on uncharacteristic descriptions (posterior odds ratio 9 normative; GPT-4o, GPT-4 and Llama-3-70B: 9; Claude-3-Opus 8.86; Gemini-1.5-Pro 6.36; Mistral-Large 3; humans 2.25) and largely ignore base rates when the description is stereotypical (LLM ratios 1.0 to 2.6, humans about 2.0) (b15). The human column is pooled from older replications at different base rates.
- Recall of base rates is inconsistent: GPT-4o gave priors of 2% to 4% when asked directly, and 10% to 30% when judging a posterior (b16).
- GPT-3 did not show base-rate neglect on the cab problem. Small rewrites (15% blue, 85% green cabs and a question about black cabs, it answered 20%) produced non-human errors; option order changed answers (c18). Authors blame training exposure.
- Seven LLMs on 12 classic tasks, each asked 10 times (b23, c20): GPT-4 correct with correct reasoning in 69.2%; Claude 2 in 55.0%; Llama 2 7B incorrect in 77.5%; GPT-3.5 human-like biased answers only 21.7% (50.8% counting human-like correct ones); GPT-4 human-like (correct or biased) 73.3%; Llama 2 13B 8.3%; Llama 2 70B refused 41.7%. Most wrong answers were illogical rather than biased, and answers varied across repeats. CogBias (c27) cites this paper as showing human-like base-rate neglect in GPT-4; that reading does not match the text.
- A weak comparison (c21): conjunction fallacy task LLMs 28%, humans 33.7%; base-rate task humans 56%, online humans 60%, ChatGPT 50%. Scoring unclear. Low value.
- Counting: LLMs lose count of frequencies as context grows, and do worse on conditional than joint distributions, with over 60% degradation at longer context. A code interpreter on GPT-4.1-mini nearly closed the gap (d13). The tasks are mode finding, MLE and sampling over given counts, not Bayes word problems.
- Reasoning models on one base-rate puzzle (Feb 2025): did not pick natural frequencies on their own. When told to, used them partly (c22).

### 6.3 Conjunction fallacy and Linda

- Famous version: strong models pass. On 1,024 fresh Linda/Bill-form items GPT-4 scored Linda .98 and Bill .99; ChatGPT Linda .70; GPT-3 pooled Bill .53, Linda .46; humans Bill .83, Linda .56 (c19, d09; 128 human and 128 model participants, 8 items each). A reasoning prompt raised davinci-003 by +0.39 (Linda) and +0.32 (Bill) but did not change human accuracy.
- Not just memory: Jiang et al. (d10) perturbed conjunction items (names, celebrity names, irrelevant narrative, hint tokens). Swapping Linda for Bob lowered accuracy for all models tested (gpt-3.5, gpt-4-turbo, gpt-4o, claude-3 opus and sonnet, llama-3, mistral-large). H1 n = 400, H2 n = 500, H3 n = 100. GPT-4o few-shot was near 100% and the null was not rejected there (p = 0.159, 1 discordant pair). Paired tests need discordant pairs, so very strong settings give no power.
- Flipped logic: o1 answered a changed problem (where the correct answer is B) as always A, calling it the classic form (d11; one worked example; overall accuracy not extracted).
- ChatGPT and Gemini handled the famous Linda but worse on a new problem of the same form (Mary) (c24, exploratory, abstract and intro only).
- Hashing bias-inducing words: ChatGPT-4 and Gemini 0 of 20 without hashing; ChatGPT-4 with hashing and neutral descriptions 10 of 10; chain-of-thought models on the original text did well (Gemini 2 Flash Thinking 10/10, o3-mini 6/10) (c23). Tiny N, and the hashed words were chosen by looking at which words drove errors on the original prompt, so it is fitted to the test item (K10).
- Conclusion (K09, contested): models pass the famous item and also mostly fresh items of the same form (GPT-4 .98) but fail under token swaps and flipped logic. Nobody tested memory vs pattern matching directly.

### 6.4 Rule induction and hypothesis search

See sections 3 and 4.4. Summary of what changed accuracy and by how much:

- Programs plus hypotheses vs direct prompting: ARC 17% to 30% (GPT-4, 100 tasks); 1D-ARC 39.6% to 73.1%; List Functions 31% to 69% (a20 to a22).
- Symbolic interpreter that runs rules: ACRE 28 to 45 to 48, MiniSCAN 0 to 46, List Functions 39.6 to 52 (b20, c06).
- Brute-force sampling: 50% on ARC public test with about 8,000 programs from GPT-4o (c12). About +3 points per doubling. The 85% human figure is a train-set number; no known human test baseline.
- Induction plus transduction ensembling: 26.50% vs 18.78% and 15.25% (c13).
- GPT-4o hypothesis search on list functions: .487 test accuracy vs direct .359, human .521 (d01).
- The bottleneck is choosing among hypotheses (a21, b18, d01) and writing the program is the lesser cost when a correct hypothesis exists (95.9% solved).
- Noise: one wrong example hurts (b21). SRR kept accuracy within about 2 points at 10% noise (d16). Consistency with clean-data answers can be 70% with 0% accuracy change, so accuracy alone hides instability.
- Error sources in another view: CodeARC (d06) 18 models, best o3-mini 52.7% success (59.5% annotated variant). First synthesised function: 67.6% pass the 10 initial examples, 38.9% pass the oracle.

### 6.5 Number game

- Ellis (c14): LLM proposals plus a learned prior and likelihood reproduce human curves with 50 to 100 proposals. Plain GPT-4 judgments differ from humans.
- Bazigaran and Sohn (c15, d05): GPT-o1-mini stays anchored to the shown number after one example. At 4 examples its divergence from the Bayesian model is comparable to humans'. One reasoning model carries the main analysis; GPT-4o, DeepSeek-V3 and Llama-3-8B were weaker and less structured.
- Xiong (c16, d03, d04), 2026 preprint: eight LLMs show predictions near a two-parameter Bayesian fit with a built-in strong-sampling assumption. Thinking mode and a weak-sampling prompt shift toward the prior but do not remove narrowness. Strong-sampling prompt had the lowest KL from the Bayesian posterior, then Default, then Weak. Evaluation (choosing from a shown list) picks hypotheses that fit examples better than free generation does; generation proposes simpler, narrower ones. Single seed per model.

### 6.6 Training and fine-tuning evidence (out of scope, noted)

Bayesian teaching: fine-tuning on a Bayesian assistant's guesses raised agreement to about 80% on flight recommendation, with 624 simulated users over 5 rounds; chain of thought and 30 rounds did not help off-the-shelf models (c17). Activation steering in CogBias cut bias score 26% to 32% but needs open weights (c27). Neither applies to a no-training scaffold.

### 6.7 Calibration

Platt scaling cut Brier for four LLMs on 1,614 forecasting questions after training on 7,824 (d14). The paper's own learned calibrator did better. Rank-preserving temperature scaling is recommended in a social-science measurement setting where Platt and Beta scaling left Brier high (d15).

### 6.8 Translating to a probabilistic program

Wong et al. (c25): the LLM only translates the problem statement into probabilistic-program code; the program does exact Bayesian inference. Demonstration level; the experiment tables were not read. Needs a generative model for each domain.

---

## 7. What our agent should take

Schema parts: G guardrail, S state, O operator, M memory. Evidence ids as above; claims in brackets.

### 7.1 Add now (established)

| # | Item | Schema part | Status | Evidence | Note |
|---|---|---|---|---|---|
| A1 | **Probability arithmetic is done in code.** Any posterior, conjunction, union or normalisation step is computed by the program from numbers the model extracts. The model never does the division. | G5 | [E] | a13, a27, d13, a11, a12, b01 | Even humans given frequencies fail without arithmetic help (24% to 36% correct). Code removes the arithmetic floor; extraction accuracy is the open part (see T1). |
| A2 | **Coherence checks on every stated probability.** P(A and B) <= min(P(A), P(B)); exclusive answers sum to 1. A violation triggers a re-ask. | G5 | [E] | a14, a15, b10, b11, b12, c19, d10 | Prompt reminders do not cure the human error (a15). A code check does not depend on the model's wording. |
| A3 | **Fitting the given examples is not proof; hold one out and also test on fresh inputs.** Every induced rule is run on all examples, a held-out example and a few newly generated inputs on which candidate rules are compared. | G3, S4, S7 | [E] | c13, d06, a21 | Rate of train-fit and test-fail is 9% (ARC tasks), up to 28.7% of first attempts (CodeARC). Held-out alone will miss under-specification (K22). |
| A4 | **Run proposed rules in an interpreter, not in the model's head.** The model proposes; code applies. | G5, G2 | [E] | b20, c06, c07, a20, c12 | The same model that writes a rule often cannot apply it (MiniSCAN above 80% to near 0). |
| A5 | **Keep the whole hypothesis pool until code ranks it.** Do not let the model shortlist. | S3 to S7 | [E] on direction | a21, b18, d01, d02, c11 | The summariser dropped 26% of correct hypotheses; the pool had a correct one only 46.4% to 49 of 100 of the time. This is the main loss. |
| A6 | **Cap execution-feedback rounds at 2.** | G2, S5 | [E] | a21, c06, c09 | Gains plateau after about 2 rounds; refinement edits are shallow exceptions. Matches the schema. |
| A7 | **State the inductive context before generalising: blank taxonomic property, causal or ecological property, threshold.** The structure comes from a one-line S2 slot. | S2 | [E] for the human phenomenon; the prompt itself [S] | a01, a03, a17, a29, a07 | Same premises point opposite ways by context. Only the prompt effect is untested (K36). |
| A8 | **State the reference class explicitly.** Name the superordinate category or population. | S1, S2 | [E] | a08, a07, d08 | Reference class changes the judgment and may be what the frequency format supplies in Linda. |
| A9 | **Use MaxSim style coverage, never summed similarity, if a similarity score is ever used.** Diverse independent supports count more than many near-duplicate ones. | S2, S7 | [E] on humans | a05, a06, a02 | SumSim r = -.34 and -.02 on general arguments. Fits the schema's idea that same-model samples are not independent (G4). |
| A10 | **Do not add bare "avoid the bias" or "use Bayes' rule" prompts.** | section 4b | [E] with schema | d12, c27, b16, b24, c22 | Judgment accuracy -4.4% in CogBias; Bayes-rule instruction did not change similarity-driven answers until the most forceful prompt. Consistent with the schema's existing ban on debiasing instructions. |
| A11 | **Treat famous-item success as possible memory.** Test induction and probability handling on paraphrased, renamed and flipped-logic items. | G3, S0 | [E] | c18, c19, d09, d10, d11, c24, c23 | Fresh surface alone is not a strong mutation (GPT-4 scored .98). Flipped logic and token swaps still catch models. See also 05 and 03 in this series. |
| A12 | **Log per problem class: pool-contains-correct vs chosen-correct, train-fit vs test-pass, extraction accuracy.** | section 6 logging, M | [E] as method | a21, d01, d06 | Needed to place the bottleneck. |

### 7.2 Test first

| # | Item | Schema part | Status | Evidence | Test (section 8 has details) |
|---|---|---|---|---|---|
| T1 | **Extract-then-compute arm for base-rate items.** The model extracts prior, hit rate and false-alarm rate into JSON; code applies Bayes. | G5, O6 | [S] | K04: d13, a24, a11 (indirect only) | No source tests this exact arm. Versus plain CoT and versus a natural-frequency rewrite, equal tokens. Top priority. |
| T2 | **Count rewrite (O6): "of N cases".** The agent rewrites a probability problem as counts out of a fixed N, then reads the answer from the table in code. | O6 | [S] for LLMs; [E] for humans | a11, a12, a24, b01, d07 | Cross wording (probability vs frequency) with menu (standard vs short) and with and without code. Humans: format effect 22 to 30 points at fixed menu; no LLM study crosses them. |
| T3 | **Percent vs absolute counts.** | O6 | [S] | a12 | Only 15 students. Cheap to include in T2. |
| T4 | **Route by plain-pass first.** Apply the count/code route only where the plain model fails first. | S0 | [S] | a13, a27, b03 | Person differences dominate in humans; for the agent the analogue is per-class plain pass rate. |
| T5 | **Hypothesis search with a code selector.** Propose N hypotheses, write code, rank by run results on examples plus a held-out example, with agreement and shortest-rule as tie-breaks. Compare with best-of-N at equal tokens. | S3, S4, S7 | [S] for the gain; the selector comparison untested | a20, c11, d01, d02 | Held-out vs agreement vs size prior not compared in any source (K16). |
| T6 | **Size-prior weighing in code (number-game recipe).** Model proposes 50 to 100 hypotheses and extensions; code applies (1/|h|)^n and averages predictions. | S2, S7 | [S] | c14, a10 | Ellis used 8 humans, with a tuned prior. Test against free model answers on one-example and few-example items. |
| T7 | **Candidate-list evaluation instead of free generation.** After generating, ask the model to score every candidate against all examples. | S2 | [S] | d03, c16 | Evaluation picked better-fitting hypotheses than free generation, but a candidate list did not recover the Bayesian posterior (c16). Run both. |
| T8 | **Induction plus transduction ensemble.** Route 1: write a program. Route 2: predict directly. Take route 1 first; use route 2 as fallback or when route 1 fails the held-out example. | S3, S7 | [S] | c13 | Their models were trained. Test with a scaffold. |
| T9 | **Noisy-example handling: induce on diverse subsets, keep the rule fitting most examples, flag the misfits.** | G3, S2 | [S] | d16, b21 | Detect an injected bad example. SRR does not name the bad example. |
| T10 | **Recalibrate confidence in code.** Fit slope and intercept (or one power parameter) on held-out logs; keep it only if Brier falls. | G5, M | [C] | b13, d14, d15 | Minimum data unknown; humans and LLM evidence differ (K27). |
| T11 | **Teacher-assumption prompt for premise sets chosen by someone with a goal.** Ask "why was this premise set chosen?" before judging strength. | S1 | [S] | a18, c02, d18 | Untested in any model. Fixes non-monotonicity if the authors are right. |
| T12 | **Name taxonomy or causal link first, for property induction.** | S2 | [S] | a01, a17, d17 | No LLM test exists (K36). |
| T13 | **Separate base-rate recall.** State the base rate in a separate call before seeing the description; combine in code. | S1, G5 | [S] | b15, b16 | Recall differed: 2% to 4% direct vs 10% to 30% inside a posterior. |
| T14 | **Structure-only rewrite for conjunction items.** Strip content words, or name the reference class ("of 100 women like Linda"). | O6, G3 | [S] | c23, d08 | c23 is tiny and fitted to the item. Replicate before use. |
| T15 | **Interactive probing for induction.** Let the agent propose new inputs and see an oracle's answer (when one exists). | S4, S7 | [S] | d06 | Success rises with more I/O budget and oracle calls. Applies only where the task has an oracle. |

---

## 8. Concrete tests on our bench

All arms get equal tokens, counting setup, tool calls and all attempts (G7). Report accuracy, tokens and the discordant pairs (right to wrong and wrong to right) per item (the schema logs each flip). Use at least 100 items per cell; with fewer, report counts and not significance.

**Test 1. Base-rate items: extract and compute (T1, T2, T3, T4).**
- Item type: 100 fresh word problems with prior, hit rate and false-alarm rate (medical, spam, quality control, fraud), several stories each, mammography as a unit test (must give 7.8%). Vary stereotype versus neutral description (b15).
- Arms: (A) plain direct; (B) plain CoT; (C) probability prompt plus "use natural frequencies" instruction; (D) agent rewrites to counts out of N, model reads off the table; (E) model extracts JSON, code computes Bayes; (F) E plus the count table shown for audit. Cross wording (probability vs frequency) with menu (standard vs short) on arms A and B (K31).
- Metric: exact posterior within 1 point; extraction field accuracy; compliance (does the trace contain the counts).
- Expected: E beats B and C if extraction is accurate; the gain should be largest on problems where B fails. C may not beat B (b24, d12). If the short menu helps B, then part of the human frequency effect is a clean statement of the numbers (d07). Predicted order: E > D > B >= C, with large uncertainty. Not measured by any source.

**Test 2. Conjunction and coherence (A2, A11, T14).**
- Item type: 60 Linda-form items with fresh names and domains, 30 flipped-logic items where the conjunction is the right answer (d11), 30 token-swapped copies (d10), and some "of 100 people like X" rewrites (d08).
- Arms: plain; plain plus coherence check in code (the agent returns probabilities; code verifies the inequality and re-asks); structure-only rewrite.
- Metric: correct choice per version; paired original vs mutated; number of coherence violations caught.
- Expected: little gain on fresh Linda items for strong models (GPT-4 was .98); the paired mutated and flipped sets should show the failures. The coherence check should catch violations whenever the model states numbers. How many failures it catches is unmeasured (gap 4).

**Test 3. Hypothesis search with different selectors (T5, A3, A5).**
- Item type: our ARC portfolio (the honest control) plus 1D-ARC-style and list-function tasks; log pool-contains-correct on a sample hand-checked.
- Arms: (A) direct; (B) best-of-N with majority vote at the same tokens; (C) N hypotheses, model shortlist, code run; (D) N hypotheses, full pool, code run, rank by fit on all examples; (E) D with one example held out; (F) E plus generated probe inputs where candidates disagree; (G) F plus agreement and shortest-rule tie-breaks.
- Metric: top-1 test accuracy; pool-contains-correct; chosen-correct given pool-contains-correct; train-fit and test-fail rate.
- Expected: D > C by about 12 points of pool (d01); F > E when examples under-specify (d06 28.7%). Where direct coding is already near 94% (SyGuS-like), hypotheses add nothing (b19), so the route should not be used there (G7, G12).

**Test 4. Number-game style one-example items (T6, T7).**
- Item type: 60 items with 1, 2, 4 examples drawn from rule or interval concepts, with human or Bayes reference curves from the teaching model (a10).
- Arms: free answer; "weak sampling" prompt; candidate list shown; model-proposed 50 to 100 hypotheses weighed by the size principle in code.
- Metric: KL or rank correlation to the Bayesian reference; for held-out numbers, accuracy on true members.
- Expected: the code-weighed arm fits best (c14); the others stay narrow at one example (c15, c16). Unknown whether the effect holds beyond the number game.

**Test 5. Rule induction with one bad example (T9).**
- Item type: 50 list-function or cipher tasks with 8 examples, 0 or 1 or 2 corrupted.
- Arms: plain induction; "some examples may be wrong" line; subset sampling plus code (SRR style); subset sampling plus an outlier report.
- Metric: accuracy; whether the corrupted example is named.
- Expected: plain falls with a single bad example (b21). Subset plus code stays within a few points at 10% noise (d16). Naming the bad example is untested.

**Test 6. Induction with and without a context line (A7, T11, T12).**
- Item type: 11 phenomena from the Han benchmark (a28; code and data public), split into blank-property items and causal or ecological items, plus premise sets chosen by a teacher for non-monotonicity.
- Arms: plain; names the structure first; asks why the premises were chosen; both.
- Metric: agreement with the human direction per phenomenon; non-monotonicity direction.
- Expected: little change on easy phenomena; possible repair on non-monotonicity (the authors' hypothesis). The gain on causal items is the test of A7. Unknown for current models.

**Test 7. Calibration (T10).**
- Item type: a logged set of 500 or more agent answers with confidences and outcomes (our bench).
- Arms: raw confidence; one-parameter recalibration; two-parameter Platt; rank-preserving temperature scaling.
- Metric: Brier and resolution (AUC); not ECE only.
- Expected: Brier falls (d14 gave about 12% for Claude-Sonnet-4) if the stated confidences are informative. Check the sample size at which the gain appears.

---

## 9. What does not transfer, and why

- **The human frequency-format effect as a prompt trick.** It was measured in students who had to do the arithmetic. For an agent, the bottleneck is extraction and the division, which code removes. Telling the model to use natural frequencies was followed only in part (b24, c22). Use the count table as a code object, not as an instruction.
- **Numeracy.** Numeracy explained more variance than format in humans (a13, a27). The model has no stable analogue. Per-class plain pass rate is the nearest thing.
- **Individual-level habit (Einstellung).** The "school-trained switch to probability formulas" account (b04) has no clear model counterpart.
- **Structured Bayesian models of human ratings (Kemp and Tenenbaum).** They fit averaged human ratings. The agent has no use for fitting people. Only the design lesson transfers: soft hypothesis weighting, and structure named by context (K13).
- **SCM as a procedure.** Needs a similarity function and only fits blank properties. GPT-4 already follows the main phenomena (c01), so the hand-coded model is not needed for easy cases.
- **Developmental and cultural findings (children, Itzaj Maya).** Informative about boundary conditions of diversity; not a design input.
- **Human-written or human-selected hypotheses in Wang et al. (33% and 45%).** They use human oracles (LARC). They are upper bounds, not methods (critique).
- **Trained induction and transduction models (c13), Bayesian teaching (c17), activation steering (c27).** They need training or open weights. Outside our scaffold-only scope.
- **Greenblatt's 8,000-sample budget.** It is a cost and a blog post; the +3 points per doubling is a log-linear trend that must flatten. Under G12 the budget should follow difficulty.
- **Hashing meaningless tokens (c23).** Fitted to the test item, tiny N, and strips content the agent often needs.
- **Famous-item LLM results (GPT-3 to GPT-4 on Linda and the cab problem).** Models in these papers are 2023-era. Strong current models may pass them; the tests that matter use mutated items (A11).
- **Cherry-picked domains.** The number game, list functions and ARC are small closed worlds with an oracle or answer key. Real tasks often have none. The held-out check and the probes need an oracle or a simulator to be meaningful.

---

## 10. Open questions

Ordered by decision value.

1. Does extract-then-compute-in-code beat plain CoT and a natural-frequency prompt at equal tokens, on base-rate items, with current models? No source tests this arm. (Gap 1)
2. For a given pool of N hypotheses, which selector in code closes the gap: held-out example, agreement, size prior, or probe inputs? Wang et al. selection gap: pool 49 of 100 vs chosen 30 of 100. Parab et al.: 46.4% pool vs 34.5% after summary. (Gap 2)
3. Does the frequency-format advantage survive for LLMs when menu is held fixed? No LLM study crosses format and menu. (Gap 3)
4. Do current frontier models still fail on freshly written Linda-form and base-rate items, and does a mutated-input check catch the failures? Nobody has measured how many failures the check catches. (Gap 4)
5. Does asking why a premise set was chosen repair non-monotonicity and diversity failures? Only the explanation exists. (Gap 5)
6. How many examples to hold out, and at what token cost, before the train-fit and test-fail rate (9% to 28.7%) falls? (Gap 6)
7. Can one-parameter recalibration of agent confidences beat raw confidence, and at what sample size? Evidence for LLMs uses 7,824 training questions and two parameters. (Gap 7)
8. Is the explicit-candidate-list prompt enough to fix one-example overgeneralisation, and does it transfer beyond the number game? (Gap 8)
9. Can the scaffold detect which example is wrong? SRR keeps accuracy but does not name it. (Gap 9)
10. Do structured priors named in the prompt help LLM property induction over similarity-only prompts? (Gap 10)
11. Is the LLM success on famous items memory or pattern matching? Not tested directly (K09).
12. Do the Wang et al. gains survive on current reasoning models, which may do hypothesis search internally? All the hypothesis-search numbers come from GPT-4 or GPT-4o. (Weak spot in the critique.)
13. Does the "mostly illogical errors" result (b23) hold for current models? Then human-bias fixes would not apply, and failures should be inspected case by case (K26).
14. What is the real human baseline on the ARC test set? The 85% figure is a train-set number.

---

## 11. Sources

[V] opened this session (page or PDF text read). [M] snippet or abstract only, or second-hand.

**Category-based induction**
- [V] Kemp and Tenenbaum (2009), Structured statistical models of inductive reasoning. https://sites.socsci.uci.edu/~lpearl/courses/readings/KempTenenbaum2009_InductiveReasoning.pdf (a01 to a04)
- [V] Tenenbaum, Kemp and Shafto (2007), Theory-based Bayesian models of inductive reasoning. https://www.mit.edu/~jbt/temp/feeney-heit/tenenbaum-kemp-shafto-final.pdf (a05, a06, a30)
- [V] Hampton and Cannon (2004), Category-based induction: an effect of conclusion typicality, Memory and Cognition 32. https://openaccess.city.ac.uk/id/eprint/992/1/Hampton%20Cannon%20M%26C2004.pdf (a07, a08)
- [V] Heit (2000), Properties of inductive reasoning, Psychonomic Bulletin and Review. https://link.springer.com/content/pdf/10.3758/BF03212996.pdf (b05 to b09)
- [V] Wu and Gentner (1998), Structure in category-based induction. https://groups.psych.northwestern.edu/gentner/papers/WuGentner98.pdf (a17, a29)
- [M] Osherson, Smith, Wilkie, Lopez and Shafir (1990), Category-based induction, Psychological Review 97. https://collaborate.princeton.edu/en/publications/category-based-induction/ (a25; abstract only)
- [M] Heit (1998), A Bayesian analysis of some forms of inductive reasoning, in Oaksford and Chater (eds), Rational models of cognition. No URL found (a26; second-hand from a01)
- [M] Tenenbaum (1999) A Bayesian framework for concept learning, PhD thesis MIT; Tenenbaum and Griffiths (2001) BBS 24. https://dspace.mit.edu/handle/1721.1/16714 (a09; abstract only)
- [V] Gureckis lab course notes, Bayesian number game (teaching page for Tenenbaum 1999, 2001). https://teaching.gureckislab.org/ccm/pages/bayes.html (a10)
- [V] Rodriguez, Mueller and Misra (2025), Characterizing the role of similarity in the property inferences of language models. https://arxiv.org/abs/2410.22590 (d17; results tables skimmed only)

**Probability judgment: humans**
- [V] Gigerenzer and Hoffrage (1995), How to improve Bayesian reasoning without instruction: frequency formats, Psychological Review 102. https://pages.ucsd.edu/~scoulson/203/GG_How_1995.pdf (a11, a12, a24, d07)
- [V] Chapman and Liu (2009), Numeracy, frequency, and Bayesian reasoning, Judgment and Decision Making 4. https://www.cambridge.org/core/services/aop-cambridge-core/content/view/7197DAAA5CC39185A3E4E02FD36A6FD0/S1930297500000681a.pdf/numeracy-frequency-and-bayesian-reasoning.pdf (a13, a27)
- [V] Weber, Binder and Krauss (2018), Why can only 24% solve Bayesian reasoning problems in natural frequencies. https://www.frontiersin.org/articles/10.3389/fpsyg.2018.01833/pdf (b01 to b04)
- [M] McDowell and Jacobs (2017), Meta-analysis of the effect of natural frequencies on Bayesian reasoning. No URL (b27; figures 24% vs 4% taken from Weber et al.)
- [V] Tversky and Kahneman (1983), Extensional versus intuitive reasoning, Psychological Review 90. https://pages.ucsd.edu/~mckenzie/TverskyKahneman1983PsychRev.pdf (a14 to a16)
- [V] Sides, Osherson, Bonini and Viale (2002), On the reality of the conjunction fallacy, Memory and Cognition. https://link.springer.com/content/pdf/10.3758/BF03195280.pdf (b10 to b12)
- [M] Hertwig and Gigerenzer (1999), The conjunction fallacy revisited. http://hdl.handle.net/11858/00-001M-0000-0025-9EBC-6 (b26)
- [V] Neace, Michaud, Bolling, Deer and Zecevic (2008), Frequency formats, probability formats, or problem structure? https://dlab.sauder.ubc.ca/sjdm/journal/07002/jdm07002.html (d08; abstract, introduction, discussion read)
- [V] Han and Budescu (2022), Recalibrating probabilistic forecasts to improve their accuracy, Judgment and Decision Making. https://www.cambridge.org/core/services/aop-cambridge-core/content/view/5D8F0DFC90FC1E9B5C38C12992A6C6A7/S1930297500009049a.pdf (b13, b14; tournament papers cited inside were not opened)

**Language models: induction and probability**
- [V] Han, Ransom, Perfors and Kemp (2023/2024), Inductive reasoning in humans and large language models. https://arxiv.org/abs/2306.06548 and https://arxiv.org/pdf/2306.06548 (a18, a19, a28, b22, c01 to c05; d18 was a snippet)
- [V] Li and Rui (2024), Dual traits in probabilistic reasoning of large language models. https://arxiv.org/pdf/2412.11009 (b15, b16)
- [V] Macmillan-Scott and Musolesi (2024), (Ir)rationality and cognitive biases in large language models. https://arxiv.org/abs/2402.09193 (b23, c20)
- [V] Araya (2025), Do chains-of-thought of LLMs suffer from hallucinations, cognitive biases, or phobias in Bayesian reasoning. https://arxiv.org/abs/2503.15268 (b24, c22)
- [V] Binz and Schulz (2022), Using cognitive psychology to understand GPT-3. https://arxiv.org/abs/2206.14576 (c18)
- [V] Yax, Anllo and Palminteri (2023), Studying and improving reasoning in humans and machines. https://arxiv.org/abs/2309.12485 (c19, d09)
- [V] Alsagheer, Karanjai and Shi (2024), Comparing rationality between large language models and humans. https://arxiv.org/abs/2403.09798 (c21; method and results lines only; low value)
- [V] Chadimova, Jursek and Kliegr (2025), Meaningless is better: hashing bias-inducing words. https://arxiv.org/abs/2411.17304 (c23)
- [V] Peruchini and Teixeira (2024), Analyzing LLM chatbots: an experimental approach using a probability test. https://arxiv.org/abs/2407.12862 (c24; abstract and introduction only)
- [V] Jiang et al. (2024), A peek into token bias: LLMs are not yet genuine reasoners. https://arxiv.org/abs/2406.11050 (d10)
- [V] Williams et al. (2025), Frontier LLMs still struggle with simple reasoning tasks (Unpuzzles). https://arxiv.org/abs/2507.07313 (d11; c28 was the snippet pointer to the same paper; one worked example read)
- [V] Huang, Zhang, Kwak and An (2026), CogBias. https://arxiv.org/abs/2604.01366 (c27, d12; abstract, method outline and related work read for c27; d12 gives the numbers)
- [V] Lampinen et al. (2024), Language models, like humans, show content effects on reasoning tasks. https://arxiv.org/abs/2207.07051 (c26; overlaps document 03)
- [M] Hagendorff (2023), Human-like intuitive behavior and reasoning biases emerged in language models, and disappeared in GPT-4. https://arxiv.org/abs/2306.07622 (c29; abstract only, withdrawn version; do not cite for numbers)
- [V] Pournemat et al. (2025), Reasoning under uncertainty: exploring probabilistic reasoning capabilities of LLMs. https://arxiv.org/abs/2509.10739 (d13; exact table not extracted)
- [V] Dai, Teehan, Torabian and Ren (2026), Aligning LLMs with human uncertainty: a Beta-Bernoulli calibrator for LLM forecasting. https://arxiv.org/abs/2605.27668 (d14)
- [V] Wang, Deng and Yang (2026), Assessing and mitigating miscalibration in LLM-based social science measurement. https://arxiv.org/abs/2605.11954 (d15)
- [V] Qiu, Sha, Allen, Kim, Linzen and van Steenkiste (2026), Bayesian teaching enables probabilistic reasoning in LLMs. https://arxiv.org/abs/2503.17523 (c17)
- [V] Wong et al. (2023), From word models to world models. https://arxiv.org/abs/2306.12672 (c25; abstract, introduction and framework only)

**Rule induction and hypothesis search**
- [V] Wang, Zelikman, Poesia, Pu, Haber and Goodman (2024), Hypothesis search: inductive reasoning with language models, ICLR. https://arxiv.org/pdf/2309.05660 and https://arxiv.org/abs/2309.05660 (a20 to a23, b17 to b19, c10, c11)
- [V] Qiu et al. (2024), Phenomenal yet puzzling: testing inductive reasoning capabilities of language models with hypothesis refinement, ICLR. https://arxiv.org/pdf/2310.08559 (b20, b21, c06 to c09; some Table 1 rows garbled by extraction; the human control in appendix C not read in detail)
- [V] Greenblatt (2024), Getting 50% (SoTA) on ARC-AGI with GPT-4o. https://blog.redwoodresearch.org/p/getting-50-sota-on-arc-agi-with-gpt (c12; blog)
- [V] Li, Hu, Larsen et al. (2024), Combining induction and transduction for abstract reasoning. https://arxiv.org/abs/2411.02272 (c13)
- [V] Ellis (2023), Human-like few-shot learning via Bayesian reasoning over natural language. https://arxiv.org/abs/2306.02797 (c14)
- [V] Bazigaran and Sohn (2025), Concept generalization in humans and LLMs: insights from the number game. https://arxiv.org/abs/2512.20162 (c15, d05)
- [V] Xiong (2026), Hypothesis generation and updating in large language models. https://arxiv.org/abs/2605.05851 (c16, d03, d04)
- [V] Parab, Lu, Wu and Gulwani (2025), Analysis of error sources in LLM-based hypothesis search for few-shot rule induction. https://arxiv.org/abs/2509.01016 (d01, d02)
- [V] Wei et al. (2025), CodeARC: benchmarking reasoning capabilities of LLM agents for inductive program synthesis. https://arxiv.org/abs/2503.23145 (d06)
- [V] Li, Wang, Zheng and Song (2025), Patterns over principles: the fragility of inductive reasoning in LLMs under noisy observations. https://arxiv.org/abs/2502.16169 (d16; noise table partly garbled, only the average gap quoted)

Notes on source quality. Many items are 2025 and 2026 preprints not yet peer reviewed. Several LLM claims rest on one paper counted many times: Han et al. (up to nine evidence lines), Qiu et al. (b20 plus c06 to c09), Wang et al. (a20 to a23, b17 to b19, c10, c11), b23 and c20 (same paper), b24 and c22 (same author). Independent sources were counted, not lines. Tenenbaum 1999/2001 and Osherson 1990 were not opened. McDowell and Jacobs (2017) was not opened.
