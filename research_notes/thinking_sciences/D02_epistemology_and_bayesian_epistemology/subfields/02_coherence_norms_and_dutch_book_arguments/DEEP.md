# Coherence norms and Dutch book arguments: deep document

*Subfield D02.02. Evidence ids (a01-a29, b01-b27, c01-c26, d01-d15) are in evidence_a-d.jsonl; claim ids (D02.02-K01 to K32) are in claims.jsonl; checks and corrections are in critique.md. Short ids like K03 mean D02.02-K03.*

## 1. What it is

Coherence norms say that a set of degrees of belief (credences) should obey the laws of probability. For our agent the key case is this. If the answers to one question are mutually exclusive and exhaustive, the probabilities on them should sum to 1.

A Dutch book argument says why. If your credences break the laws, a bookie can offer bets you regard as fair that lose money in every possible world. Ramsey (1926) sketched this. De Finetti (1937) made it a theorem. Kemeny and Lehman (1955) proved the converse: if the credences obey the laws, no sure-loss book exists (a05, a04, b24).

A second route, accuracy dominance, needs no bettor. If credences break the laws, a coherent set exists that is closer to the truth in every world, under a strictly proper score such as Brier (a09, d12).

Coherence is a floor, not a goal. Ramsey said so: the laws are "laws of consistency, an extension to partial beliefs of formal logic" (a02). A dogmatic, wrong credence set can be coherent. Coherence says nothing about which credence is right.

Why it matters for our agent: guardrail G5 already says code normalises probabilities over exclusive answers (cited as "about 35% error cut", which comes from one human study, K05). This document checks what stands behind that rule and what the LLM evidence says.

Links to other subfields (not covered here): conditionalization (D02.01), the problem of the priors (D02.03), uncertain evidence (D02.04), belief revision (D02.06), heuristics and biases, Bayesian models of cognition, Good Judgment Project, surprisingly popular method, Shannon information.

## 2. History and theories in depth

### 2.1 Ramsey (1926)
- Ramsey derives the probability laws from preferences over bets. Degree of belief is measured by the odds a person would just take. Laws derived: belief in p plus belief in not-p is 1; a multiplication law for p and q given p. No experiments (a01).
- The Dutch book is one line: such a person "could have a book made against him by a cunning better" and lose in any event (a01).
- He calls the laws consistency, not truth-guidance (a02).
- He lists limits of bet measurement: love or hatred of excitement, diminishing marginal utility of money, "reluctance to bother about trifles". Stakes should be small, but then trifles distort (a03). Hajek and Maher extend these objections.

### 2.2 De Finetti (1937, 1974) and the converse
- Coherence means no bet set loses in every outcome. Theorem: forecasts on a finite event set are coherent iff they extend to a probability measure (a04; known only via secondary text).
- Converse (Kemeny 1955, Lehman 1955): quotients that obey the axioms allow no sure-loss book. It holds only for finitely many bets. It fails once other norms (Reflection, countable additivity) are added (a05).
- Shimony (1955) gave a related strict-coherence result (a05).

### 2.3 Objections
- The link from credence to accepting bets is loose. Sure loss is not clearly irrational (Maher). Hajek's "Czech book": an incoherent agent can get a sure gain, so the argument proves too much unless bets must be fair or favourable (a06, a29, d11).
- Stakes, risk attitude and utility of money distort (a03, a06).
- Countable additivity needs infinitely many bets, so the loss is only theoretical (a08).

### 2.4 Depragmatized versions
Christensen (1996), Howson and Urbach (1993), Hellman (1997): incoherent credences give conflicting evaluations of the same bet, so they are inconsistent. No bet need be taken. Maher (1997) replies that "fair" cannot be defined without utility. These versions still lean on value judgements about bets (a07, d11).

### 2.5 Diachronic books
Teller (1973) and Lewis (1999) give a four-bet book that punishes any update rule other than conditionalization. The bets are priced Pr1(A and E), Pr1(A|E)Pr1(not E), [Pr1(A|E)-Pr2(A)]Pr1(E), Pr2(A) (d11). Van Fraassen (1989): the book works only if the agent commits in advance to the deviant rule, so it is weaker (a08). Detail belongs to D02.01.

### 2.6 Accuracy dominance
Joyce (1998) and Leitgeb and Pettigrew (2010): with a continuous strictly proper additive score, every non-probabilistic credence function is strongly dominated by a probabilistic one, and no probabilistic one is even weakly dominated (a09, d12). Worked example: 0.6 on X and 0.6 on not-X gives Brier inaccuracy 0.52 in both worlds; 0.5 and 0.5 gives 0.50 in both (d12). Objections: different measures give different dominators (Bronfman); Levinstein's world-varying weights break dominance; Easwaran and Fitelson's trick-coin case; Carr (2015, 2017) (a09, d12, d13). The original proofs were not opened.

### 2.7 Descriptive psychology: support theory and the Bayesian Sampler
- Support theory (Tversky and Koehler 1994): probability attaches to descriptions, P(A,B) = s(A)/(s(A)+s(B)). Unpacking an implicit hypothesis raises its judged probability, so exclusive parts can sum above 1. Binary complements add to 1 by construction (a28, via a27 and a25). The primary paper was not opened.
- Probability Theory plus Noise (PT+N) says people hold coherent beliefs and add read-out noise. The Bayesian Sampler (Zhu, Sanborn, Chater 2020) says people take a few samples and shrink toward a generic prior. Mean judgment is E = (N p + beta)/(N + 2 beta), so identities with an extra positive term are biased by beta/(N+2 beta) (a11, b22).

## 3. Core findings with exact numbers

Status: E established, S single-source, C contested (as in claims.jsonl).

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Probability laws follow from betting preferences; Ramsey calls them consistency | No experiments | Ramsey 1926 (a01, a02) | E (K01) |
| Dutch book theorem and converse hold for finitely many bets only | Converse fails with Reflection or countable additivity | SEP (a05, a08, b24) | C (K02) |
| Accuracy dominance: coherent set beats incoherent one in every world under a strictly proper score | Example Brier 0.52 vs 0.50 | SEP reviews (a09, d12, d13) | E (K03); proofs not opened |
| Analysts' sums over 4 exclusive hypotheses exceed 1 | Control M=1.54 [1.33, 1.76]; ACH M=1.77 [1.56, 1.97]; binary complements 0.98 and 0.95; N=50 | Mandel et al. 2018 (a25, b17) | E (K04) |
| Physicians' 4 prognoses sum to 164% | 14+26+55+69; CI 134 to 194%; binary 78+21=99% (CI 94 to 104), n=149 students | Redelmeier et al. 1995 (a27) | E (K04); not re-opened |
| Coherentizing cuts analyst error | MAE 0.23 to 0.15, d=0.96, t(49)=6.77; average of 50 coherentized: 0.09 (61% cut) | Mandel et al. 2018 (a25, b18) | S (K05) |
| Plain normalisation does as well as the fancy projection | MAE 0.13 vs 0.15 | Mandel et al. 2018 (b18) | S (K06) |
| Coherentizing needs signal | Random responses coherentized: MAE 0.21; analysts better, d=0.64 | Mandel et al. (b18, a26) | S (K07) |
| ACH did not help | Raw MAE 0.21 vs 0.26, p=.14 (trend only); error share from sum violation .73 vs .50, p=.04; after coherentizing diff 0.01 [-0.04, 0.07]; coherentizing effect d=1.37 vs 0.69 | Mandel et al. (b19, a26) | S (K07) |
| Unpacking raises judged probability | Gastroenteritis 31% vs 16%; residual 69% unpacked vs 50% (p<0.005) | Redelmeier 1995 (a27) | S (K08) |
| Bayesian Sampler fits human incoherence better than PT+N | Exp 1: 40/59 = 67.8% vs 18/59 = 30.5%, p=.005; Exp 2: 52/84 = 61.9%, p=.038; Exp 2 identity tests for cold/rainy, windy/cloudy null (p .35 to .81) | Zhu, Sanborn, Chater 2020 (b22, b23) | C (K10) |
| LLMs break identities like P(A)+P(not A)=1; bigger is better but never zero | 4 models, 24 event pairs, T=0 and 1; identities with 2 extra positive terms deviate about 2x | Zhu and Griffiths 2024 (a10, b01, b02) | S (K09) |
| LLM forecasters fail consistency checks | GPT-3.5 negation 52.6%, paraphrase 30.8%, monotonicity 42.0%, Bayes 68.6%; GPT-4 10.9%, 12.5%, 16.0%, 58.8% (strong = gap above 0.2; 380 questions, 1220 variants) | Fluri et al. 2023 (a13, b12, c09) | E (K11) |
| Resampling does not cure it | Randomness explains under 20% of strong violations; 95% of answers identical over 5 passes | Fluri (b12); Andrews and Sarkar (a20) | E (K12) |
| Consistency prompting fixes one check, worsens others | GPT-4 negation 10.9% to 2.9%, paraphrase 12.5% to 17.3%, Bayes 58.8% to 68.6%; GPT-3.5 negation 52.6% to 37.1%, paraphrase 30.8% to 41.3%, Bayes 51.0% | Fluri (b13, c10) | E (K13) |
| Consistency tracks forecast error, but per check | Scraped set: Cond 0.92 (arbitrage), 0.87 (frequentist); aggregate 0.62 / 0.85. NewsAPI: Cond 0.71, aggregate 0.49 / 0.66; Negation -0.36, Or -0.24 | Paleka et al. 2025 (a14, b09) | E (K14) |
| Reasoning model still violates | o1-mini negation violated in 58% (scraped), 52% (NewsAPI) | Paleka (a15) | S |
| Training on arbitrage does not raise accuracy | gpt-4o-mini, depth 0 to 4; no reliable Brier gain, no gain on untargeted checks | Paleka (a16, b11, c08) | E (K15) |
| Arbitrage profit separates models far more than Brier | 0.002067 to 0.1994 (100x) vs Brier 0.1966 to 0.2157; Spearman 0.9143; 101 of 105 pairs vs 32; 15 models, 365,100 elicitations | Andrews and Sarkar 2026 (a18, b05) | S (K16) |
| Irrelevant context raises incoherence | Up to 10x; gut "70%" and positive emotion largest; statistics arm lowers it | Andrews and Sarkar (a21, b08, c06) | S (K17) |
| Richer logical structure exposes more | 16 joint cells: +0.00244 [0.001971, 0.002961], 50 dates | Andrews and Sarkar (a19) | S (K18) |
| Full-panel elicitation removes most incoherence | Near rounding level for GPT-OSS-120B; complement pairs lower, unrelated pairs raise | Andrews and Sarkar (a20, b07) | S (K17, K19) |
| Frontier ensembles still incoherent | 4-LLM mid-tier: residual > 0 on 33 to 94% of 1,876 cliques; frontier panel 97.8% of 268 bets, mean residual 0.118 to 0.072; coupling visible: 0.519 to 0.298, 16 of 20 | Kotawala 2026 (a22, a23) | S (K19) |
| Bayes-update axioms break across chats | Over 50% of 30 scenarios for nearly all model-axiom pairs; within one dialogue 10% (Gemini), 1 of 30 (Gemma) | Filbry et al. 2026 (b14, c14) | S (K20) |
| Non-reasoning updates cost success | Over 30% loss on 20Q and ProteinWorld; reasoning plus code near exact | Filbry (b15, c15) | S (K20) |
| Bayes-consistency scales weakly | BCC vs log params r=0.906; Llama 3 1.24B 0.658, 8.03B 0.739; direction agreement 64 to 76% | Imran et al. 2025 (c13) | E (K21) with Williamson (c19) |
| Verbal probability words nearly complementary | 19 LLMs, 11 expressions; "possible" 51 vs human 37 | Petridis et al. 2026 (b16) | S (K22) |
| Small models near-coherent on median, tails bad | Median Inc 0.024 (1.5B), 0.000 (3B), 0.0001 (7B), 0.019 (SmolLM3); 25.0% of propositions at 1.5B had profit above 0.25; negation exploitability down about 100x by training, half of runs collapsed | Dragonevskiy 2026 (c16, c17) | S (K23) |
| Normalising LLM complement judgments cuts incoherence | Gemma-2-9b: 0.13/0.14 to near 0; MSE roughly unchanged (t=-2.54, p=.01 train; p=.09 test); r with truth 0.80/0.73 | Zhu, Yan, Griffiths 2025 (a12) | S |
| Complementarity failures persist under CoT | Share off by >5%: direct 0.856, CoT 0.863, ArgLLM 0.833 (400 pairs per task) | Freedman and Toni 2025 (c12) | S |
| Coherence-based aggregation weights | "More than 30%" over simple mean, second-hand | Mellers et al. 2017 on Predd et al. (b21) | S (K24) |
| Argument-coherence filter | GPT-4o 69% to 80% but 1207 of 2923 questions dropped | Gorur et al. 2025 (b25) | S (K25) |
| Consistency-as-signal | Up to +4% claimed; stress test paired p>=0.28 on 4 new domains | Jiang 2025; Cho and Kweon 2026 (b26, b27) | C (K26) |
| Multiple-choice renormalised max probability ranks right above wrong | 15 chat LLMs, 280 AUROC points, above chance in 245; accuracy explains R2=0.94 of AUROC, R2=0.07 of calibration error | Plaut et al. 2025 (d01) | S (K27) |
| Abstain below a threshold | 20 labelled items set the threshold; beat never-abstain for most of 15 models | Plaut (d02) | S |
| Joint options beat separate scoring | Multiple-choice prompt beats cloze on 16 of 20 datasets, mean +9.7, max +44 | Robinson and Wingate 2023 (d10) | E (K28) |
| Prefilling puts mass on valid options | +3.4 to +25.9 accuracy points; ACE Llama-3.1-8B MMLU 0.206 to 0.129 | Poppi et al. 2025 (d03) | E (K28) |
| Option-ID bias survives renormalisation | gpt-3.5-turbo MMLU 67.2 to 60.9 with gold at D; llama-30b +15.2 with gold at A; contextual calibration up to +30.0 on GPT-3 | Zheng et al. 2024; Zhao et al. 2021 (d04, d05) | E (K29) |
| Residual option under-used | 52B model: accuracy and calibration fall when option D becomes "none of the above" | Kadavath et al. 2022 (d07) | S (K30) |
| Top-k elicitation lowers ECE | gpt-3.5-turbo TruthfulQA ECE 0.389, 0.361, 0.203 for k=1, 2, 4 | Tian et al. 2023; Xiong et al. 2024 (d08, d09) | E (K31) |

## 4. Mechanisms and models

### 4.1 Normalisation and projection
Given raw probabilities p_i over n exclusive, exhaustive options:
- Normalise: q_i = p_i / sum(p). Cheap. Fixes the sum, not the shape. In Mandel et al. it reached MAE 0.13 (b18).
- Project: find the coherent vector closest to p in Euclidean distance. For one partition, this is the projection onto the probability simplex (a few lines of code). Mandel's "coherentization" is this family and reached 0.15, no better than normalising (b18).
- Multi-constraint case (A, not A, A and B, A or B, conditionals): project onto the set of coherent vectors by a linear or quadratic program. Dykstra-type alternating projection works (Kotawala, a22). Andrews and Sarkar use a linear program for the largest guaranteed profit, which equals the sup-norm distance from the forecast to the coherent set (a17).

### 4.2 Measuring incoherence without labels
- Raw sum deviation: |sum(p) - 1|.
- Pairwise identity error: |P(A) + P(not A) - 1|, or P(A) + P(B) - P(A and B) - P(A or B) (a10).
- Arbitrage score: solve the LP "max guaranteed profit per unit stake" over the stated probabilities (a17). Needs no outcome labels.
- Paleka et al. use check tuples (Negation, Paraphrase, Cond, And, Or, ...) and score the arbitrage available across the tuple (a14).

### 4.3 Why LLMs are incoherent
Zhu and Griffiths propose the Bayesian Sampler analogy. The model acts like a few-sample estimator shrunk toward a prior. With zero samples and a symmetric prior the expected identity deviation is 0.5 for one-extra-positive-term identities and 1 for two-extra (b03). The LLM data do not separate this from PT+N (b03). The cause is a conjecture (autoregressive training).

Other contributors with evidence:
- Elicitation context. Asking events one by one hides the links. Putting the whole partition in one query drives incoherence to near zero (a20), and showing the coupling cut a residual from 0.519 to 0.298 (a23).
- Irrelevant context pushes incoherence up (a21).
- Option-ID and position priors skew which option gets mass (d04).
- Format validity: first-token mass leaks to non-option tokens (d03).

### 4.4 Implementable multiple-choice guardrail
1. Show all options in one prompt, labelled (d10).
2. Prefill the answer prefix so mass lands on option tokens (d03).
3. Read option-letter probabilities, renormalise (d01).
4. Optionally permute option order and average the renormalised vectors, or divide out an estimated ID prior (PriDe, d04).
5. Add an explicit residual option and say so in the instructions; models under-use it by default (d07).
6. Use max renormalised probability as a rank signal and abstain threshold, not as a calibrated probability (d01, d02).

For API models without logprobs: ask for verbal probabilities for all options in one response, then normalise in code. Ask for top-k with probabilities (d08). Use numeric, not verbal, scales (b16).

### 4.5 Coherence-weighted aggregation (second-hand)
Score each sample by its own distance from coherence. Weight by that score when averaging. Reported +30% over the simple mean in human forecasting (b21). Not reproduced. Originals not opened.

## 5. What holds up

Holds up (two or more sources, or large and clear):
- Humans give sums above 1 over 3 or more exclusive options, and near 1 over binary complements (a25, b17, a27).
- LLMs, including frontier ones, are incoherent on consistency checks (a13, a14, a22, a23). Larger models are less incoherent but not coherent (b02, c13; frontier cut the residual 39%, did not remove it, a23).
- Resampling the same prompt does not fix it (b12, a20).
- Training or prompting that targets one check leaves other checks alone or worse (b13, c08, a16).
- Accuracy dominance is a sound non-bettor argument given a strictly proper score (a09, d12, d13).
- Listing all options together beats separate scoring (d10) and prefilling valid tokens helps (d03).
- The option-ID prior survives renormalisation (d04, d05).

Failures, nulls and caveats:
- ACH did not improve coherence or accuracy (a26, b19). The raw "ACH hurt" is a trend (p=.14), not established (critique).
- Normalisation beat the fancier projection (0.13 vs 0.15) (b18).
- Coherentizing random responses gave MAE 0.21, so it does not create accuracy (b18).
- Arbitrage-trained forecasters had no Brier gain (a16). Dragonevskiy: half of runs collapsed to an uninformative equilibrium until a calibration term was added; near-zero incoherence at 7B coincided with near-maximal confidence (c16, c17).
- Consistency correlates with accuracy only on some checks and weakens out of sample: aggregate 0.62 to 0.85 on scraped data, 0.49 to 0.66 on NewsAPI (b09). Part of the link is that better models do both (a14).
- Prompt-based repair hurt already-coherent quotes (9 of 10 worsening cases had baseline under 0.05) (a23).
- Argument-coherence filter: the gain is partly selection (b25). Consistency-as-signal: paired p>=0.28 on new domains (b27).
- The Bayesian Sampler wins overall but not on every Exp 2 identity (b23). In raw-response fits it wins only for small N (<=17) (b22).
- The Mandel et al. d=0.96 for coherentization and the d=0.96 for the control sum exceeding 1 are two different effects with the same number (critique).

Moderators:
- Number of alternatives: binary near-coherent, 4-way far off (a27, b17).
- Context: irrelevant text up to 10x worse, statistics lower it (a21).
- Single dialogue vs separate chats (b14).
- Reasoning and code tools help Bayes updating (b15, c15) but CoT did not reduce complementarity violations (c12).
- Model size: modest gain (c13: 0.658 to 0.739 for 1.24B to 8B).

Interventions that worked: normalising in code; full-partition elicitation; showing the coupling; prefilled option tokens; top-k verbal probabilities; adding a statistics block; reasoning plus code for updates.
Interventions that did not: resampling the same prompt; consistency instructions; ACH; arbitrage fine-tuning (for accuracy); retrieval (residual 0.260 to 0.283); an LLM aggregator (7 of 100 regressions).

## 6. Language models

### 6.1 Behaviour on probability identities
- 2023-2024 models, one number per query: large violations. GPT-3.5 strong violations 30 to 69%, GPT-4 11 to 59% by check (c09). Bayes-rule checks are worst for both.
- Zhu and Griffiths: all four models deviate on every identity; error grows with plus-minus imbalance, as in humans (b01).
- Gemma-2-9b complement sums miss by 0.13 on dice events (a12). Llama-3 direct: 96.5% of complementarity predictions off by more than 5% (c12).

### 6.2 What changed it, by how much

| Change | Effect | Source |
|---|---|---|
| Negation prompt | GPT-4 negation 10.9% to 2.9%; paraphrase 12.5% to 17.3%; Bayes 58.8% to 68.6% | b13 |
| GPT-3.5 to GPT-4 | Negation 52.6% to 10.9%; Bayes 68.6% to 58.8% | c09 |
| Scale in open base models | Llama 3 1.24B to 8B: BCC 0.658 to 0.739 | c13 |
| Full-panel prompt | Near-zero incoherence (one model, one panel) | a20 |
| Coupling visible | Residual 0.519 to 0.298; 16 of 20 partitions better | a23 |
| Frontier models | Residual down 39%, still >0 on 97.8% of bets | a23 |
| Code projection | Reaches the QP floor with no extra call | a23 |
| Irrelevant detail | Up to 10x worse | a21 |
| Reasoning plus code (updates) | Near-exact posteriors; non-reasoning cost over 30% success | c15 |
| Same dialogue vs separate chats | Over 50% of scenarios down to 10% (Gemini) | b14 |
| CoT on complementarity | 0.856 to 0.863 off by >5%: no help | c12 |
| Normalise complement pairs | Incoherence 0.13 to near 0, MSE about the same | a12 |
| More reasoning tokens (vNM axioms) | "Substantially improve" (second-hand) | c25 |

### 6.3 Coherence and accuracy
Across models, more coherent means more accurate (Spearman 0.9143, b05; check-dependent r in a14). Within a model, repair gives little accuracy (a16). Reading: coherence is a symptom of a better model, and fixing the symptom alone does not give the skill. Normalisation is still safe because the dominance theorem says it cannot raise Brier loss (K03), but the gain depends on signal in the raw numbers (b18).

### 6.4 Multiple-choice use (our guardrail)
- Renormalised option-letter probability (MSP) ranks correct above wrong in 245 of 280 cases; accuracy explains R2=0.94 of AUROC (d01). It is not calibrated: ECE x100 ARC-C 13.6, HellaSwag 19.6, MMLU 24.1, TruthfulQA 30.6, WinoGrande 24.2 (d01).
- Examples (accuracy / AUROC): Llama 3.1 70B 80.6/83.4; GPT-3.5 Turbo 67.5/76.1; Falcon 7B 30.1/52.0 (d01).
- Format validity: valid-token rate up over 60 points for Gemma-2-9B and Llama-3.1-8B with prefilling (d03).
- Option-ID bias: gold at D drops gpt-3.5-turbo MMLU by 6.3 points (d04).
- RLHF models are better calibrated verbally than by token (d08); large base models are well calibrated with visible options (d06).
- Not found: any study comparing forced sum-to-one with independent per-option probabilities at equal tokens (critique, gap 1). Almost all LLM coherence work is on forecasting, not answer choice.

### 6.5 Scope warning
Most 2026 items (Andrews and Sarkar, Kotawala, Dragonevskiy, Filbry et al., Williamson et al.) are preprints from single groups, not replicated.

## 7. What our agent should take

### Add now (established)

| Item | Schema part | Status | Evidence |
|---|---|---|---|
| Keep G5: normalise per-answer probabilities over exclusive answers in code (divide by the sum). Cheap, safe by accuracy dominance. Do not promise an accuracy gain; the 35% figure is human data from one study. | G5 | [E] for safety and coherence; gain [S] | K03, K04, K06, a09, d12, b18 |
| Justify the guardrail as consistency plus Brier accuracy, not as bet protection. | G5 (note) | [E] | K01, K03, K32, a02, d12 |
| Elicit all exclusive options together in one prompt, with option labels, not one prompt per option. | S3/S4 prompts | [E] | K28, K19, d10, a20, a23 |
| Make mass land on valid options (prefill the answer prefix when logprobs are available). | S3/S4 | [E] | K28, d03 |
| Do not rely on a "be consistent" instruction. Fix coherence in code. | G5 | [E] | K13, b13, c10 |
| Do not spend tokens resampling the same prompt to fix incoherence. | S3 budget (G12) | [E] | K12, b12, a20 |
| Measure coherence on more than one check type; never treat one check as proof of accuracy. | G3 | [E] | K14, K15, a14, a16 |
| Correct for option-ID position bias (shuffle and average, or divide out the prior) before using the renormalised number. | S4/S7 | [E] | K29, d04, d05 |
| Prefer top-k verbal probabilities in one response when logprobs are absent. | S3 | [E] | K31, d08, d09 |
| Treat max renormalised probability as a rank signal, not a calibrated probability. | S0/S8 | [S], consistent across 15 models | K27, d01 |
| Keep irrelevant text out of probability prompts (S1 input hygiene). | S1 | [S] | K17, a21 |

### Test first (see section 8 and UNKNOWNS.md)

| Item | Schema part | Status | Evidence |
|---|---|---|---|
| Forced sum-to-one vs independent per-option probabilities at equal tokens | G5 | [S], indirect | K27, K28, gap 1 |
| Raw sum of independent per-option probabilities as a doubt signal (G1) | G1/S0 | [C], check-dependent | K14 |
| Explicit residual option "other" with instruction | S1/S3 | [S], older model | K30, d07 |
| Coherence-weighted aggregation of samples | G5/S7 | [S], second-hand | K24, b21 |
| Re-ask in negated and paraphrased form as a consistency check | S4/G3 | [E] that violations exist; value [S] | K11, K15 |
| Batch evidence into one update instead of sequential updates | O (update) | [E] direction, older models | K21, c19 |
| Reasoning or code for numeric updates | O | [S] | K20, c15 |
| Complement and partition pairing in elicitation | S3 | [S] | K17, a20 |
| Pair any coherence objective with an accuracy term | G7 | [S] | K23, c17 |
| Least-squares projection beyond plain normalisation | G5 | [S], human only | K06, K29 |

## 8. Concrete tests on our bench

All arms get equal tokens (G7). Setup tokens count.

1. Forced partition vs independent options.
   - Items: exclusive-choice items (4 to 5 options) from our bench classes.
   - Arms: (a) one prompt, all options, prefilled letter, renormalise; (b) one P(True) query per option, then normalise in code; (c) per-option, raw, no normalise.
   - Metric: accuracy of argmax, Brier, ECE, raw-sum deviation.
   - Expected: (a) at least equal to (b) on accuracy and Brier; (c) worst on Brier. Dominance says (b) beats (c) on Brier whenever raw sums differ from 1.
2. Normalise vs projection. Same samples, normalise vs Euclidean simplex projection. Expected: no difference (K06).
3. Raw-sum signal. On arm (c), correlate |sum - 1| with per-item error; AUROC for predicting a wrong answer. Expected: weak and check-dependent.
4. Order averaging. Single order vs average over cyclic shuffles of option order at the same total tokens (fewer attempts per order). Metric: accuracy, Brier. Expected: gain on smaller models (d04).
5. Residual option. Add "none of the above" (true share 0, 10, 30%) with and without an explicit instruction. Metric: sum of named options vs 1 minus the true residual rate; use of the residual option. Expected: under-use without the instruction (d07).
6. Consistency repair at equal tokens. Re-ask in negated and paraphrased form (arm A) vs same-prompt resampling (arm B) vs plain. Metric: strong-violation rate on three check types and Brier. Expected: A cuts the targeted check, Brier little; B nothing (K12, K15).
7. Irrelevant-context drift. Add a stated guess or emotion line to the probability prompt. Metric: change in raw-sum deviation. Expected: higher drift (K17).
8. Coherence-weighted vote. Weight samples by their own sum-to-one deviation vs equal weights, same number of samples. Expected: gain only if raw deviation tracks error.
9. Partition-visible elicitation for event probabilities: separate vs joint prompt (K19). Metric: LP arbitrage score on a 3 to 4 event panel.
10. Update task. Evidence batched in one update vs sequential; chain-of-thought vs code tool at equal tokens. Metric: distance to the true posterior.

## 9. What does not transfer, and why

- Betting. Our agent places no bets. Pragmatic Dutch books need bets accepted (a06, d11). Use accuracy dominance instead.
- Human unpacking effect. LLMs under-use a residual option rather than over-fill it, at least in a 2022 52B model (d07). The human 164% sum is not a guide to LLM sums.
- Forecasting numbers. Almost all LLM coherence evidence is forecasting or event probability, not answer choice (critique).
- Cross-model correlation (Spearman 0.9143). It is across models. It does not show that raising coherence in one model raises its accuracy (a16).
- Mandel et al. results. 50 novice human analysts, accuracy against a model-derived target, not real outcomes (b17).
- Diachronic books. They support a pre-committed update rule, but have not been shown to predict LLM update failures (gap 10).
- Training results (Dragonevskiy, Qiu et al. Bayesian teaching, ArbitrageForecaster). Our agent does not train (c17, c20).
- Old-model calibration findings (d05, d06 on GPT-3 and 2022 base models) may not hold on current reasoning models.
- Countable and infinite-bet versions. Irrelevant to a finite answer set (a08).

## 10. Open questions

1. Does forced sum-to-one beat independent per-option probabilities at equal tokens on multiple choice? No direct study.
2. Does a coherence projection add anything over plain normalisation for LLM samples?
3. Does the raw sum of independent per-option probabilities predict correctness per item?
4. Does an explicit residual option behave differently in current models?
5. Does reasoning reduce probability-identity violations at equal tokens versus resampling? CoT did not help complementarity (c12); for Bayes updates, reasoning helped (c15).
6. Does incoherence grow with scaffold length and memory load?
7. Which Dutch book version should justify the guardrail for a non-betting agent? We take accuracy dominance (K32, contested).
8. Can coherence-based sample weighting be reproduced with LLM samples?
9. Do anti-exploitability gains survive without the uninformative collapse?
10. Do diachronic books predict LLM update failures better than one-shot identities?
11. Do the 2026 preprints replicate?

## 11. Sources

[V] opened, [M] snippet or second-hand only.

- [V] Ramsey (1926) Truth and Probability. https://fitelson.org/probability/ramsey.pdf (a01-a03)
- [M] de Finetti (1937, 1974), via SEP and Andrews and Sarkar. https://plato.stanford.edu/entries/dutch-book/ (a04)
- [V] Vineberg, SEP Dutch Book Arguments. https://plato.stanford.edu/entries/dutch-book/ (a05-a08, b24, d11; last part of page not read)
- [V] Pettigrew, SEP Epistemic Utility Arguments. https://plato.stanford.edu/entries/epistemic-utility/ (a09, d12; first 100000 of 140410 characters)
- [V] SEP Formal Epistemology. https://plato.stanford.edu/entries/formal-epistemology/ (d13)
- [M] Hajek (2008) Arguments for or against Probabilism?, via SEP (a29)
- [M] Tversky and Koehler (1994) Support theory. https://www.cambridge.org/core/books/heuristics-and-biases/support-theory-a-nonextensional-representation-of-subjective-probability/8DABDF6C7AC2E0FD1289642DBCE7F939 (a28)
- [V] Redelmeier, Koehler, Liberman, Tversky (1995). https://zenodo.org/record/1066958/files/article.pdf (a27; numbers re-checked only by arithmetic)
- [V] Mandel, Karvetski, Dhami (2018). https://doi.org/10.1017/S1930297500006628 (a25, a26, b17-b19)
- [M] Mandel et al. 2018 HTML copy. https://dlab.sauder.ubc.ca/sjdm/journal/18/18803/jdm18803.html (c22)
- [V] Mellers, Baker, Chen, Mandel, Tetlock (2017). https://journal.sjdm.org/17/17408/jdm17408.pdf (b20); b21 is second-hand about Predd et al. 2008, Wang et al. 2011, Tsai and Kirlik 2012, Karvetski et al. 2013, all [M]
- [V] Zhu, Sanborn, Chater (2020) The Bayesian Sampler. https://pmc.ncbi.nlm.nih.gov/articles/PMC7571263 (b22, b23; sample sizes not re-opened)
- [V] Zhu and Griffiths (2024/2025). https://arxiv.org/abs/2401.16646 (a10, a11, b01-b03, c11)
- [V] Zhu, Yan, Griffiths (2025). https://arxiv.org/pdf/2505.07883 (a12)
- [V] Fluri, Paleka, Tramer (2023). https://arxiv.org/abs/2306.09983 (a13, b12, b13, c09, c10)
- [V] Paleka et al. (2025). https://arxiv.org/abs/2412.18544 (a14-a16, b09-b11, c07, c08)
- [V] Andrews and Sarkar (2026). https://arxiv.org/abs/2609.02797 (a17-a21, b04-b08, c01-c06)
- [V] Kotawala (2026). https://arxiv.org/abs/2605.30335 (a22, a23)
- [V] Betz and Richardson (2023). https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9910757/ (a24; c21 abstract level only)
- [V] Filbry, Melo, Gal (2026). https://arxiv.org/abs/2610.29331 (b14, b15, c14, c15)
- [V] Petridis et al. (2026). https://arxiv.org/abs/2608.26327 (b16)
- [V] Gorur, Rago, Toni (2025). https://arxiv.org/abs/2507.23163 (b25)
- [M] Jiang et al. (2025). https://arxiv.org/abs/2506.21590 (b26)
- [M] Cho and Kweon (2026). https://arxiv.org/abs/2608.08514 (b27)
- [V] Freedman and Toni (2025). https://arxiv.org/abs/2504.13644 (c12)
- [V] Imran et al. (2025). https://arxiv.org/abs/2507.17951 (c13)
- [V] Dragonevskiy (2026). https://arxiv.org/abs/2609.39341 (c16, c17)
- [V] Andrews (2026) Revealed Rationality. https://arxiv.org/abs/2608.05015 (c18)
- [V] Williamson, Foti et al. (2026). https://arxiv.org/abs/2605.06915 (c19; per-model numbers not extracted)
- [V] Qiu et al. (2026). https://arxiv.org/abs/2503.17523 (c20)
- [M] Li and Sreedhar (2026). https://openreview.net/forum?id=U27ZfUx7JE (c23)
- [M] Matta, Naphade, Zou (2026). https://openreview.net/forum?id=TAhXHpa2nW (c24)
- [M] Tak et al. (2026), via Andrews (c25); [M] Chadwick, Kahng, Kipper (2025), via Andrews and Sarkar (c26; paper not located)
- [V] Plaut, Nguyen, Trinh (2025). https://arxiv.org/abs/2402.13213 (d01, d02)
- [V] Poppi et al. (2025). https://arxiv.org/abs/2505.15323 (d03)
- [V] Zheng et al. (2024). https://arxiv.org/abs/2309.03882 (d04)
- [V] Zhao et al. (2021). https://arxiv.org/abs/2102.09690 (d05)
- [V] Kadavath et al. (2022). https://arxiv.org/abs/2207.05221 (d06, d07, d14)
- [V] Tian et al. (2023). https://arxiv.org/abs/2305.14975 (d08)
- [V] Xiong et al. (2024). https://arxiv.org/abs/2306.13063 (d09)
- [V] Robinson and Wingate (2023). https://arxiv.org/abs/2210.12353 (d10)
- d15 is a search-status line, not a source.
