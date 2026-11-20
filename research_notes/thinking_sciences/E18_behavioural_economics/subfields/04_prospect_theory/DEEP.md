# Prospect theory: deep document

*Subfield E18.04. Sources: evidence_a-d.jsonl (ids a01-a33, b01-b28, c01-c25, d01-d18), claims.jsonl (K01-K25), critique.md. Status marks follow SCHEMA.md: [E] established, [S] single source, [C] contested. Priority for our agent: background only. The value is calibration and a few cheap tests.*

## 1. What it is

Prospect theory describes how people choose between risky options. It was built to replace expected utility as a description of behaviour. It has four core ideas.

- **Reference point.** People code outcomes as gains or losses from a reference point, not as final wealth.
- **Diminishing sensitivity.** The value curve is concave for gains and convex for losses.
- **Loss aversion.** Losses weigh more than equal gains. The famous coefficient (lambda) is about 2.25.
- **Probability weighting.** Small probabilities are overweighted and large ones underweighted. The weights are decision weights, not probabilities.

Together these give the fourfold pattern: risk averse for likely gains and unlikely losses, risk seeking for unlikely gains and likely losses.

The topic matters to us for three reasons, all background.

1. It is the standard yardstick used to ask whether an LLM is "biased like a human". Many LLM papers fit its parameters.
2. It shows how a description of a problem (frame, reference point, slicing) changes choice. Our schema already guards against this (S1 restate, input hygiene).
3. It is used as an engineering tool in training (KTO). That is not a scaffold idea.

Headline status in 2026. The qualitative 1979 patterns replicate well (K04, [E]). The size of loss aversion is contested. Human lambda is 1.07 to 2.25 depending on design (K01, [E]). LLM lambda is on average low (about 1.26) and very model dependent (K07, K09).

## 2. History and theories in depth

### 2.1 Before 1979
Expected utility was the normative and descriptive default. Markowitz (1952) and Williams (1966) had already shown sign-flip preferences (cited in a04). Allais (1953) had shown certainty-type violations.

### 2.2 Kahneman and Tversky 1979 (a01-a08)
Method: short anonymous questionnaires of hypothetical gambles. At most a dozen problems per booklet. Orders and left-right positions varied. Israeli students and faculty, amounts in Israeli pounds (median monthly family income about 3,000). Some problems repeated in Stockholm and Michigan with "essentially identical" results. Group sizes 64 to 141 per problem. Choices were not paid. The authors say so.

The paper's effects, each with numbers (see section 3):
- **Certainty effect** (Allais type). Problem 1 vs 2.
- **Ratio violation at low probability.** P7 vs P8.
- **Reflection effect.** Flip the sign and preference flips.
- **Isolation effect.** Two-stage framing of the same final odds.
- **Reference dependence.** Different starting bonus, same final states, preferences flip (P11, P12).
- **Probabilistic insurance.** 80% would not buy.

The formal model has two phases.
- **Editing:** coding, combination, segregation, cancellation, simplification, detection of dominance. The order of these operations is under-specified (the authors admit it).
- **Evaluation:** V = pi(p) v(x) + pi(q) v(y) for regular prospects. For strictly positive or negative prospects V = v(y) + pi(p)[v(x) - v(y)]. v(0)=0, pi(0)=0, pi(1)=1. Subcertainty pi(p)+pi(1-p)<1. Small p overweighted.

No numeric lambda appears in 1979. Loss aversion is argued from dislike of symmetric 50-50 bets: v(x) < -v(-x), and v'(x) < v'(-x). Known flaw: the 1979 version can violate first-order stochastic dominance.

### 2.3 Cumulative prospect theory 1992 (a09, a10)
Fixes dominance by rank-dependent cumulative weights. Separate weighting functions for gains and losses. Works for uncertainty and any number of outcomes. Weighting form w(p) = p^g / (p^g + (1-p)^g)^(1/g). Median estimates quoted in citing papers: alpha = beta = 0.88, lambda = 2.25, gamma (gains) 0.61, delta (losses) 0.69 (the 0.61 and 0.69 are not verified in any opened text). Source of the numbers: 25 graduate students from elite west-coast US universities, three unincentivised sessions, only the median reported, no mean or spread (a10, [E] via Brown and KTO). Only the publisher abstract of the 1992 paper was opened.

### 2.4 Endowment effect and the mug study
Kahneman, Knetsch and Thaler (1990): 86% of owners kept their mugs, 10% of chocolate owners chose the mug, 56% of neither-group chose the mug (a31, via Wikipedia, tertiary). This became the best known "field" support for loss aversion.

### 2.5 The critique line
- **Inertia and attention accounts.** Gal (2006) and Gal and Rucker (2018, "The loss of loss aversion"): status quo bias and endowment are better explained by inertia and loss attention than by a loss weight (b05, no numbers, via Wikipedia).
- **Loss attention.** Yechiam and Hochman (2013): losses raise attention and arousal with an inverted-U effect on performance, without a heavier subjective weight (b06).
- **Yechiam (2019).** Only very large losses are overweighted. Smaller ones often are not. Some studies cited as support found no loss aversion (b04, abstract only).
- **Walasek and Stewart (2015).** The loss-gain ratio depends on the range of gains and losses in the choice set (decision by sampling). It can vanish or reverse (b03, opened).
- **Reference point problem.** Koszegi and Rabin (2007). The reference point is hard to define (a30).
- **Competing models.** The priority heuristic predicted majority choices over 260 problems in four data sets better than CPT (a30, tertiary). List: framing effects shrink with market experience.
- **Re-meta-analysis.** Yechiam and Zeif (2025) say loss aversion is not robust.

### 2.6 The LLM era
- 2022-23: Binz and Schulz (GPT-3 replicated 3 of 6 K and T biases). Suri et al. (GPT-3.5 framing).
- 2024: Jia et al. fit PT parameters to commercial LLMs. Ross et al. fit CPT curves. KTO uses PT as a loss.
- 2025-26: Wang et al. (instability), Ge et al. (reasoning vs conversational models), Tarabeih's meta-analysis, Yechiam and Tarabeih (prompt contamination), Kraishan (more thinking does not reduce bias).

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Certainty effect (Allais type) | P1 N=72: 82% take sure 2,400. P2 N=72: 83% take (2,500, .33). 61% modal in both. P3 N=95: 80% sure 3,000 over (4,000,.80). P4 N=95: 65% take (4,000,.20) over (3,000,.25). Non-money tour: P5 78% sure England tour; P6 67% pick 5% three-country tour | a02, K and T 1979 | [E] replicated (K04) |
| Ratio violation at low probability | P7 N=66: 86% (3,000,.90) over (6,000,.45). P8 N=66: 73% (6,000,.001) over (3,000,.002) | a03 | [E] |
| Reflection | P3 80% sure gain vs P3' 92% gamble for loss (-4,000,.80). P4 65% vs P4' 58%. P7 86% vs P7' 92%. P8 73% vs P8' 70%. P13 82% vs P13' 70% | a04 | [E] overall; weakest leg (fails outside money) |
| Isolation | Problem 10, 141 subjects: 78% sure 3,000 branch vs 35% for (3,000,.25) in P4 (N=95) | a05 | [E] (held in the replications) |
| Probabilistic insurance | P9 N=95: 80% would not buy | a05 | [S] |
| Reference dependence | P11 N=70: given 1,000, 84% sure 500. P12 N=68: given 2,000, 69% gamble (-1,000,.50). Same final states | a06 | [E] |
| Lottery vs insurance | P14 N=72: 72% (5,000,.001) over sure 5. P14' N=72: 83% sure loss 5 over (-5,000,.001) | a08 | [E] |
| 1992 parameters | alpha = beta .88, lambda 2.25, gamma .61, delta .69; 25 graduate students, unincentivised, median only | a10, c23 | [E] as description of the source; not a population constant (K02) |
| 2020 multinational replication | N=4,098, 19 countries, 13 languages. 94% of items replicated, attenuated. 12 of 13 contrasts. Some countries 100% | a14, b01 | [E] (K04) |
| Territorial replication | US N=149, UK N=253. Items 69% / 81%. Contrasts 77% / 92%. Reflection not robust. PsyArXiv preprint v2, no journal peer review found | b02, d16 | [S] (K05) |
| Human lambda, largest meta-analysis | 607 estimates, 150 articles. Mean 1.955 [1.824, 2.104]. Raw median 1.69. Raw mean 1.97. 93.9% of estimates above 1. Bias-corrected 1.742 [1.674, 1.811]. Only 14.4% of heterogeneity explained | a11, a12, d11, d12 | [E] (K01, K23) |
| Human lambda, symmetric designs | 1.07 [0.97, 1.18]; about 2.3 for ordered designs with losses smaller than gains. 84 papers, 163 estimates, n=149,218 | a32, b10, d13 | [C] (read via Tarabeih and an abstract) |
| Other human lambda estimates | Neumann and Bockenholt brand choice 1.49 / 1.73 (109 estimates, 33 studies). Walasek, Mullett and Stewart 1.31 (19 estimates, 17 articles). Mrkva five surveys, 17,720 respondents | a13, b09 | [C] |
| Experts' guess of lambda | 37 guesses, mean 1.639, SD 0.599; 24.3% between 1.8 and 2.1 | a12 | [S] |
| Range dependence (human) | Exp 1a N=323: 1.79 (gain range 40, loss 20); 1.00 (20/20); 1.02 (40/40); 0.88 (20/40). Exp 1b N=382: 1.59, 1.01, 1.02, 0.81. Exp 2 N=401: 2.28 (60/20), 1.01 (20/60). Exp 3 lab, real money, N=82: 1.81, 1.23 (symmetric), 0.93 | b03 | [E] for the pattern (two designs plus replication in Exp 1b); one lab group |
| Human curvature and weighting | Curvature about 0.67 [0.66, 0.70], weighting about 0.68 (Imai 2025, second-hand). Tanaka 2010: 0.67, 0.685. Ruggeri ranges: curvature 0.41-0.96, weighting 0.53-0.79 | a33, b26, a14 | [S] (K06) |
| Mug study | 86% of owners kept mugs; 10% of chocolate owners chose mug; 56% of neither chose mug | a31 | [S] tertiary |
| LLM pooled lambda | 1.26 [1.06, 1.46]; 28 estimates, 11 studies, 32 models; t(27)=2.66 p=.013; prediction interval 0.20 to 2.31; range 0.49 to 2.72. With bound-hit estimates added back 1.42 [1.00, 1.84] | a15, b11 | [S] one author (K07) |
| LLM by design | Symmetric (L=G): 1.15 [0.98, 1.32] (18 est., 7 studies) vs human 1.07. Losses smaller (L<G): 1.46 [0.96, 1.96] (10 est., 4 studies) vs about 2.3 (t=-3.81, p=.004). Certainty-equivalent 1.10, direct choice 1.20 | a16 | [S] (K08) |
| LLM curvature and weighting | Curvature about 1.01 (TK fit, human 0.67), 0.52 (Tanaka fit). Weighting 0.81 (TK, p=.028 vs 1), 0.84 (Tanaka). Three reasoning models share 0.81 | a18, b27 | [S] |
| LLM lambda by vendor | GPT-4-Turbo 1.48 (SD 0.35), Claude-3-Opus 6.32 (SD 2.84), Gemini-1.0-Pro 2.33 (SD 0.85); human sample 3.47 (SD 3.92); 300 draws each. Weighting alpha: 1.18, 0.76, 0.88, human 0.69 | a20, b13, c01, c02 | [E] that vendors differ (K09) |
| LLM lambda by version | GPT-3.5 2.72 to GPT-4.1 0.57; ANOVA F=35.87, p<.001, partial eta2 .481. Release year -0.16 per year (R2 .38). Model family R2 .27. Stakes +0.35 per tenfold | a24, b12, a17 | [E] direction, [S] size |
| Lambda instability | Qwen2.5-32B lambda 0.953 to 2.013 across rounds; Llama-3.1-8B 0.010 (R2 .092); Qwen2.5-14B R2 .067; GPT-5-Mini 4.000 (bound); human 2.63. 256 samples per lottery at T=0.7. Reliable fit needs MAE <= 0.20 and R2 >= 0.10 | b14, c03, c04, d14, d15 | [S] (K10, K24) |
| Prompt contamination | ChatGPT-4o lambda 1.09 (no paper); 1.785 after Brown abstract; 1.043 after Yechiam and Zeif abstract; 1.52 after full report. Study 3: ChatGPT 1.257/1.218 (loss-aversion condition) vs 1.072; Qwen 1.742 vs 0.940/0.929. ChatGPT accepted 105% more lotteries after Yechiam and Zeif. 800 sessions in 4a | a26, b20, d09, d10 | [S] (K11, K22) |
| Rating vs choice | Gain rating scale above loss scale in 8 of 9 post-trained models (+1.2 to +24.3, p<.001; gemini-3-flash 24.3). Choice lambda 0.88 to 1.59; gpt-5-nano 1.005-1.04 | a28, b21 | [S] (K18) |
| Profile prompts | Default lambda 1.18 (GPT-4o), 1.12 (4o-mini), 1.90 (Gemini 2.5 Pro), 1.46 (Claude 3.5 Haiku). Biased profile up to 3.00 (d=1.82). 24,000 agent-scenario pairs. Gamble vs disposition correlation 0.42 | b22 | [S] |
| Persona effects | Claude lambda 6.32 to 2.60 (random demographics) to 2.17 (real-world). Gemini 2.33 to 2.94. Openness vs lambda r=-0.55; Agreeableness -0.68; Neuroticism +0.37; Extraversion -0.46 (GPT-4o). Wealth persona: poor 37.39 rounds vs rich 1.11, d=4.15, 6,950 decisions (goal text confounded) | c02, c15, c16, d17 | [E] drift exists (K13); size confounded |
| Framing in LLMs | GPT-3.5 efficacy 5 vs 4 in 11 of 11 trials (humans 5.2 vs 4.6, t(80)=3.86, p<.001). 5-model risk study: Championship +1.40 to +1.84; Career -0.37 to -0.60 (reversed); Merger -0.24 to +0.12; 25 of 35 pairs positive. Drug scenario contradictory answers 57% / 74% / 85% (GPT-4o / Gemma 2 / Llama 3.1). Numeric gambles: o3 chose sure option 399/399 | a25, b18, c09, c10, c21, b24 | [E] (K12) |
| GPT-3 classic biases | 3 of 6 K and T biases replicated: framing, certainty, small-probability differences | b16 | [S] |
| Rationality vs fragility | CCEI (consistency with utility maximisation) 0.998 / 0.997 / 0.997 / 0.999 for GPT vs human 0.980 / 0.985 / 0.967 / 0.963. Price framing cut risk CCEI to 0.901; time 0.884; social 0.698; food 0.894 | b17 | [S] |
| Reasoning vs chat models | 20 LLMs, 360 humans. RM vs expected-payoff agent correlation 0.86-1; CM below 0.5. Best LLM-human correlation 0.42. Human vs EV agent 0.14. RMs near fully invariant to order, frame and explanation | d01, d03, c06 | [E] (K19) |
| Description-history gap | All LLMs move toward humans with outcome histories; small for GPT-5.1 and DeepSeek-R1, large for chat models and open 7B-32B reasoning models. Humans move toward EV. Per-model numbers only in figures | d02, c07 | [S] (K20) |
| Extra thinking tokens | 30 vignettes, 7 models, ceilings 0 / 1,024 / 4,096 / 8,192 tokens, 12,350 calls. Reasoning minus sibling bias +0.031 [-0.010, +0.074], t(29)=1.45, p=.157. Framing reversed d=-2.35 (pHolm .010). Loss aversion M=-0.586, d=-0.88, pHolm .256. Anchor restatement fixed anchoring on 5 of 5 items, p=.057 | d04, d05 | [S] one author |
| Bias test at scale | 45 LLMs, 8 biases, about 2.8 million responses. Prospect-theory resistance by detail level L1-L5: .542, .590, .599, .625, .630. Lowest gemma-2-9b-it .334, highest o4-mini .806. Prompt detail cuts most biases up to 14.9%. Models above 32B reduce bias in 39.5% of cases | c12, c13 | [E] (K14) |
| Prompting to change bias | Direct "be loss averse" and zero-shot CoT no reliable shift (GPT-4, N=10 per setting); one-shot worked; two-shot confused gain and loss; role-play teenager or senior lowered lambda | a22, b15 | [E] (K14) |
| Debias scaffold | SACD average bias FOMC llama3.1-8b 0.3805 to 0.1570; PubMedQA 70b 0.4730 to 0.0560; PubMedQA 8b 0.4425 to 0.1790; LegalBench 8b 0.5570 to 0.1235. PubMedQA 70b loss-aversion score: vanilla 0.3100, CoT 0.9440, few-shot 0.2920, Reflexion 0.4440, debate 0.5380, self-help 0.0340, SACD 0.0320. DeFrame fairness framing disparity -92% (BBQ, 8 models, 4 calls) | d06, d07, d08 | [E] bias scores fall; accuracy not reported (K21) |
| KTO | alpha .88, lambda 2.25 template. Zephyr-beta-SFT GSM8K 53.5 vs DPO 40.0 (+13.5), BBH 52.6 vs 44.1, MMLU 58.6 vs 58.2. Mistral-7B OpenAssistant win rate vs SFT: DPO .600, KTO .652. 90% of desirable examples dropped still beats DPO. Default lambda_D = lambda_U = 1, rule 1 <= lambda_D n_D / (lambda_U n_U) <= 1.5 | a23, c19, c20, d18 | [S] (K15) |
| Simulation use | Route-choice agents with fitted lambda 1.43: total error 0.0682 vs 0.6634 with non-travel parameters (.99/.99/2.25) | c17 | [S] (K16) |
| Anti-gambling claims | Abstract 24.3% vs results 52.4% fewer loss-chasing errors; overconfidence -18.7% vs -33.3% | a29, c18 | [C] do not use (K17) |

## 4. Mechanisms and models

### 4.1 Value function (implementable)
Let x be the outcome relative to a reference point r.
- Gains: v(x) = x^alpha, with alpha about 0.88 (1992) or about 0.67 (2020s human meta-analysis).
- Losses: v(x) = -lambda * (-x)^beta, beta about 0.88.
- lambda is the loss weight. Default 2.25 is not safe (section 5).

### 4.2 Probability weighting
w(p) = p^g / (p^g + (1-p)^g)^(1/g). With g < 1 the curve is inverse-S. Human g about 0.65 to 0.68. Apply separately to gains and losses in CPT. In CPT the weights apply to cumulative probabilities of outcomes ranked from best to worst (gains) and worst to best (losses), so dominance is respected.

### 4.3 Fitting parameters to an LLM (the method most LLM papers use)
1. Build a multiple-price list (Tanaka style, 35 lottery rows in Jia and Wang) or certainty-equivalent ladder (56 prospects in Ross and in the personality paper).
2. Query each row many times. Wang used 256 samples per lottery at T=0.7. Ross used 100 per setting at T=1. The personality paper used 15 runs.
3. Fit risk curvature, lambda and weighting by maximum likelihood or by minimising choice error.
4. Report fit quality. Wang's rule: unreliable if MAE > 0.20 or R2 < 0.10.
5. Flag estimates at the bounds (0.010 and 4.000 in Wang). They mean the model is not fitting, not that lambda is extreme.

Simple alternative (Yechiam and Tarabeih): a ratio of the accepted loss to the win at the indifference point (loss $5 to $10, gain $6). Cheap, but a different quantity.

### 4.4 Decision by sampling (range-frequency) model
Walasek and Stewart (b03): subjective value of an outcome is its rank in the set of outcomes seen. If the loss range is smaller than the gain range, a given loss ranks higher than the equal gain, so it looks larger. Loss aversion then arises from the choice set, not from the person. A design implication for us: the same option can look more or less loss averse depending on the other options shown.

### 4.5 Attention account
Yechiam and Hochman (b06): losses attract attention and arousal. No heavier weight is needed to explain some effects. This predicts effects on performance and learning, not just preference.

### 4.6 What the LLM does instead
Three mechanisms are supported, each with a caveat.
- **Imitation of text** (a26, d10). The measured bias follows what the prompt says about human bias. Self-fulfilling.
- **Expected-value computation** (c10, d01). Reasoning models compute EV and take the sure or indifferent option (o3 399/399; EV in 20.4% to 46.8% of rationales).
- **Surface framing sensitivity** (a25, c09). Words like "lose" and "save" move chat models. Effects depend on the scenario (reversal in Career).

### 4.7 Training use (KTO, a23, c19)
Value function with a reference point z0 (the KL term), sigmoid saturating form, separate weights lambda_D (desirable) and lambda_U (undesirable). This weights binary feedback. It is a loss design, with no claim that the model is loss averse.

## 5. What holds up

### 5.1 Holds up
- **Qualitative 1979 patterns.** 94% of items, 12 of 13 contrasts, 19 countries, N=4,098 (a14). [E]
- **Loss aversion exists on average in humans.** 93.9% of 607 estimates above 1 (a11). [E]
- **Framing flips LLM choices in many scenarios.** 4 independent sources (K12). [E]
- **Models differ widely.** Lambda 0.01 to 6.32 and the 4.0 bound (K09). [E]

### 5.2 Weak or failed
- **2.25 as a constant.** Brown mean 1.955, raw median 1.69, bias-corrected 1.742. Walasek 1.31. Yechiam and Zeif 1.07 (symmetric). Original from 25 students.
- **Symmetric designs.** Lambda about 1.0 when gain and loss ranges are equal (b03 Exp 1a, 1b). Reversal to 0.81 to 0.88 when loss range is larger.
- **Reflection.** Not robust outside money (b02).
- **Territorial replication.** Item level 69% and 81% (preprint).
- **Loss aversion in LLM choice.** Near 1 in rating-vs-choice tests (a28).
- **Publication bias.** Brown's bias parameter 1.434 [1.008, 1.876]. LLM Egger p=.58, Begg p=.37 with k=10 (low power).

### 5.3 Moderators
- **Human.** Field and general samples higher. Lab students and surveys lower. Money vs non-money no clear difference. Value form and reference type matter little. Only 14.4% of heterogeneity explained (d12). Range and order of options matter a lot (b03, d13). Large stakes raise it in LLMs (+0.35 per tenfold).
- **LLM.** Family (R2 .27), release year (-0.16 per year), stake, prompt wording (verbal probability phrases shift lambda and weighting more than risk preference, d15), persona, personality traits, description vs history (d02), temperature and round (0.95 to 2.01).

### 5.4 Interventions that worked
- One-shot worked examples (Ross, b15).
- Detailed prompts (resistance .542 to .630, up to 14.9% bias cut, c12).
- Self-adaptive debiasing (SACD) cut bias scores by up to about 88% in one cell (0.4730 to 0.0560) but at extra calls and with no accuracy measure (d06).
- DeFrame, 4 calls, -92% fairness-framing disparity (d08).
- One-line anchor restatement, 5 of 5 items (d05).
- Giving outcome histories moves chat models toward humans (d02). This is a manipulation, not a fix.

### 5.5 Interventions that did not
- Direct "be loss averse" prompts and zero-shot CoT (b15, a22).
- Two-shot examples (confused gains and losses).
- CoT raised bias in cells (PubMedQA 70b 0.3100 to 0.9440, d07).
- Few-shot raised bias in cells (PubMedQA 8b average 0.4425 to 0.8105).
- Debate raised bias in cells (0.3805 to 0.5020).
- More thinking tokens (d04).
- Asking for a longer rationale often lowered rationality in chat models (d03).
- Anti-gambling RARG numbers are inconsistent (c18).

## 6. Language models

### 6.1 Lambda levels
- Pooled 1.26 [1.06, 1.46], well under human 1.96 but near 1.07 to 1.31 (a15). One author's preprint, independence 1.
- Symmetric designs 1.15 vs human 1.07. Loss-skewed 1.46 vs about 2.3 (a16).
- Vendor spread (Jia): GPT-4-Turbo 1.48, Gemini-1.0-Pro 2.33, Claude-3-Opus 6.32. Yee and Koh: GPT-4o 1.18, 4o-mini 1.12, Gemini 2.5 Pro 1.90, Claude 3.5 Haiku 1.46. Wang: Qwen2.5-32B 1.213, Gemini-2.5-Flash 1.499.
- The Claude 6.32 value is a multiple-price-list outlier (single prompt) and is dropped in the meta-analysis.
- Version trend: GPT-3.5 2.72 to GPT-4.1 0.57. Newer aligned models lose human-like loss bias and drift toward EV (a24).

### 6.2 Reasoning models
- Close to risk-neutral EV maximisers on lotteries (RM-EV correlation 0.86-1). Order, frame and explanation invariant. Further from humans than chat models (d01, d03).
- Numeric gambles: no framing effect. o3 chose the sure option 399/399 (c10).
- But probability weighting is still 0.81 for GPT-5.1, DeepSeek-R1, Qwen3-30B-Thinking (a18).
- More thinking tokens do not reduce vignette bias: Delta +0.031, p=.157 (d04). Framing was reversed (d=-2.35).
- In vignette scenarios (not pure numbers) even reasoning models showed framing (Championship +1.40 to +1.84).

### 6.3 Framing and reference point
- GPT-3.5: 11/11 trials 5 vs 4 (a25).
- Drug scenario: contradiction in 57% to 85% of runs (c21).
- Military: loss frame cut negotiation, e.g. Maritime 24.2% vs 54.6%, Border 25.2% vs 67.5%, with escalation in 1 of over 700 decisions (c11).
- Price framing cut GPT consistency (CCEI) to 0.901 from 0.998 (b17).
- Persona wealth shifted behaviour d=4.15 (confounded with goal text).

### 6.4 What changed it, by how much
| Lever | Effect | Source |
|---|---|---|
| Describe human loss aversion in the prompt | ChatGPT-4o 1.09 to 1.52-1.79 | d10 |
| Describe human gain seeking | 1.043 (vs 1.09 control; Qwen 0.940) | d09, d10 |
| Persona demographics | Claude 6.32 to 2.17; Gemini 2.33 to 2.94 | c02 |
| Biased profile | up to 3.00, d=1.82 | b22 |
| One-shot example | shifts lambda and risk; size not extracted | b15 |
| Direct instruction, zero-shot CoT | no reliable shift | b15 |
| Verbal vs numeric probabilities | shifts lambda and weighting; Qwen-32B 0.95 to 2.01 across rounds | c04, d15 |
| Description vs history | chat models move strongly toward humans | d02 |
| Stake size | +0.35 lambda per tenfold | a17 |
| Release year | -0.16 per year | b12 |
| SACD / DeFrame | bias scores down 60% to 92% | d06, d08 |

### 6.5 Rating vs choice
LLM stated feelings are asymmetric (gains felt more strongly in 8 of 9 post-trained models), yet choice lambda is near 1 (a28). Do not infer behaviour from stated affect.

### 6.6 Measuring lambda is unreliable for small models
Models under 14B gave fits below the reliability rule (Llama-3.1-8B R2 .092, Qwen2.5-14B R2 .067). Several estimates sit at bounds (d14). Authors suggest at least 14B for PT-based systems (c05).

## 7. What our agent should take

The topic is background. There is no evidence that bias vocabulary helps hard-task thinking. Items are cautious. Evidence ids in brackets.

### Add now (established)

| # | Item | Part | Status | Evidence |
|---|---|---|---|---|
| A1 | Do not hard-code 2.25 (or any loss weight) as a human ground truth when scoring or simulating. State the design: 1.07 for symmetric lotteries, 1.8 to 2.0 for loss-skewed designs. | memory / bench notes | [E] | K01, K02, K23; a10, a11, d11, d13 |
| A2 | Framing guardrail: the same options must not change the answer when only gain or loss wording changes. Check by matched reframings; code compares answers. This fits S1 (restate in neutral final-state form; keep original beside it). | G (framing), S1 | [E] | K12, K03; a05, a06, a25, c09, c21 |
| A3 | State the reference point explicitly in the restate step (current state, baseline, what counts as the starting point). | S1 | [E] for the human effect, [S] for the agent gain | K03; a06, b03 |
| A4 | Input-form check: do not assume one backbone's behaviour profile carries over. Any measurement of a bias must be repeated per backbone and per version, with SD. | G (per-backbone tests) | [E] | K09; a20, a24, b12, c01 |
| A5 | Scaffold text hygiene: avoid describing named biases or human tendencies in context unless a test says it helps. A paragraph about human loss aversion raised lambda in two models. | G (prompt hygiene) | [S] (single group); consistent with existing 4b ban on bias instructions | K11, K22; d09, d10 |
| A6 | Do not add "be careful about losses" or bias-awareness instructions. Already in SCHEMA 4b. This research adds that CoT, few-shot and debate raised bias in some cells and extra thinking did not reduce it. | 4b (confirm) | [E] | K14; b15, d04, d07 |
| A7 | Separate stated ratings from choices when measuring anything. Ratings and choice disagree. | G | [S] | K18; a28 |
| A8 | When a decision includes a persona, stake or wealth context, treat it as a possible drift source. Strip it from the task text when it is not part of the problem (S1 input hygiene). | S1 hygiene | [E] that drift exists; [S] that leak occurs on neutral tasks | K13; c02, c16, d17 |

### Test first (not established)

| # | Item | Part | Status | Evidence |
|---|---|---|---|---|
| T1 | Re-frame-and-compare step: restate the task in the opposite frame, run both, flag flips. Count only on flips (G1). Measure flips and accuracy at equal tokens. | O8 / S1, G1 | [S] | K21; d06, d08 |
| T2 | One-line anchor restatement style steps: cheap, 5 of 5 items, p=.057. | S1 | [S] | d05 |
| T3 | Present repeated or frequent-outcome problems both as stated odds and as lists of outcomes; flag disagreement. | G (input-form invariance) | [S] | K20; d02 |
| T4 | Thinking vs non-thinking comparison on lottery and framing items. Do not assume EV-like is right for human-value decisions. | G11 | [E] on lotteries, design judgement elsewhere | K19; d01, d04 |
| T5 | Design-matched lambda of our own agent, repeated at least 5 times with different wordings, report SD and fit quality. Calibration only. | bench | [S] | K07, K10; c03, d14 |
| T6 | Persona or stake leakage guardrail on neutral tasks. | S1 | [S] | K13; d17 |

## 8. Concrete tests on our bench

All arms at equal total tokens. Report per backbone, per run, with at least 5 seeds.

| # | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| B1 | Matched gain/loss reframings of 20 to 30 decisions with equal final outcomes (the Asian-disease type, plus hand-built lottery pairs and a few vignettes) | plain; plain with CoT; scaffold with restate-in-final-state (S1); scaffold with re-frame-and-compare (T1) | Flip rate between frames; accuracy on any items with a keyed answer | Plain flips 20 to 60% (drug scenario 57-85% contradictory); restate and compare should cut flips by half or more. Accuracy should not drop |
| B2 | 1979 problems P1-P14 (and primed variants) | plain vs scaffold | Share of agent choices vs 1979 and 2020 shares; number of the 13 contrasts reproduced | Plain chat models partly match; reasoning mode near EV (picks sure/indifferent). Gap 6 is open, no LLM result exists |
| B3 | Range manipulation (gain range 40, loss range 20 vs symmetric vs reversed) | plain vs scaffold | Fitted lambda per design; spread across designs | Humans 1.79 / 1.00 / 0.88. If agent is more stable than humans, good |
| B4 | Description vs history (same gamble, stated odds vs 20 and 100 sampled outcomes) | plain, thinking, scaffold | Choice flip rate; EV agreement | Chat models move toward humans in history form; frontier reasoning small change |
| B5 | Bias vocabulary in context (no paragraph vs a paragraph describing human loss aversion vs a paragraph describing no loss aversion) | scaffold with and without bias text | Lambda (indifference ratio) or acceptance rate at -$5/+$6 | Replicates the 1.09 vs 1.5-1.8 shift if our backbone is similar. Reasoning models untested |
| B6 | Persona or stake leakage: identical gamble problems with a rich/poor/neutral preamble | plain vs guarded (preamble stripped by S1) | Choice shift (d) | Persona shifts in plain; guard should cut it. Confounded goal text must be removed |
| B7 | Thinking budget sweep (0, 1,024, 4,096 tokens) on 30 bias vignettes | plain at each budget | Bias magnitude | Expect no slope (Delta about 0), replicating d04 |
| B8 | Lambda reliability: one model, 5 wordings, 5 seeds, 35-row price list, 256 samples per row where affordable | none | SD of lambda; R2 of fit | Expect lambda range at least 1.0 for models around 30B; small models unreliable |
| B9 | Probability-weighting probe: stated probabilities 0.001 to 0.99, tasks of equal EV | plain vs scaffold | Estimated weighting; certainty effect (P1/P2 consistency) | Reasoning models about 0.81 weighting, close to human 0.68 |
| B10 | Rating vs choice agreement on the same 20 items | plain | Correlation of stated feeling asymmetry and choice lambda | Low correlation (a28: asymmetry present, lambda about 1) |

## 9. What does not transfer, and why

- **Human lambda as a goal.** A target of 2.25 or 1.96 is not defensible (K01, K02). Design-dependent range 1.07 to 2.3.
- **The value function as advice.** Prospect theory describes intuitive choice. It is not a policy for the agent. The agent's quality criterion is the checked answer, not matching human choices.
- **"EV-like is correct".** On lottery items reasoning models are close to risk neutral. That is correct only where payoffs are money and risk neutrality is the right norm. It is not settled for human-value decisions (gap 4).
- **Loss weighting in a scaffold.** No scaffold-side use found (K25). KTO weights are a training hyperparameter. Do not add a loss weight to S7 select.
- **Bias-name instructions.** 4b already bans them, and prompt contamination adds a reason (d10).
- **Anti-gambling mitigation numbers** (K17) and persona d=4.15 as a clean effect (confounded with goal text).
- **Vendor-specific lambda tables.** Models change by version, so they do not carry over (K09).
- **Human reflection effect as a law.** It fails outside money (b02).
- **Fairness framing (DeFrame, SACD) as a proof for gain/loss framing.** SACD's "loss aversion" is a punishment warning prompt, not lambda; DeFrame measures fairness disparity.
- **KTO's 13.5 point GSM8K gain.** It is a training result with a different baseline, and not evidence that loss aversion helps reasoning.

## 10. Open questions

1. What is the human lambda in a design-matched, incentivised, symmetric, same-scale set? Working rule only (1.07 vs 1.8 to 2.0). Yechiam and Zeif and Brown disagree because of inclusion rules (a32 not opened).
2. Does a re-frame or debias step change accuracy on real tasks at equal tokens? No paper reports it (K21).
3. Does a bias name in a system prompt raise bias in reasoning models and other vendors? Tested only in ChatGPT-4o and Qwen2.5-72B, one author group.
4. Are reasoning models better for human-value decisions if they act like EV maximisers? Design judgement, not a data result.
5. How many runs give a trustworthy lambda for one model? No paper gives a count. Qwen2.5-32B spread 0.95 to 2.01.
6. Do LLMs reproduce the 1979 P1-P14 items and the 2020 battery? No study found. Search budget ran out.
7. What are the per-model decisiveness numbers in Ge et al. (description-history gap)? Only figures.
8. Is the territorial replication peer reviewed? Not found.
9. Does persona or stake context leak to neutral tasks, and can a guardrail stop it?
10. Does the LLM meta-analysis (11 studies, 28 estimates, k=10 for tests) survive independent replication? It is one author's preprint; the paired study is from the same group.
11. Imai 2025 weighting and curvature values are second-hand.
12. The 0.61 and 0.69 weighting medians of 1992 are not verified in any opened text.

## 11. Sources

[V] = opened and read this session (full text or abstract page as noted). [M] = snippet or second-hand only.

- [V] Kahneman and Tversky (1979) Prospect theory: an analysis of decision under risk. https://web.mit.edu/curhan/www/docs/Articles/15341_Readings/Behavioral_Decision_Theory/Kahneman_Tversky_1979_Prospect_theory.pdf (a01-a08)
- [V] Tversky and Kahneman (1992) Advances in prospect theory. https://link.springer.com/article/10.1007/BF00122574 (abstract page only; a09). Parameter numbers [M] via citing papers.
- [V] Brown, Imai, Vieider and Camerer (2024) Meta-analysis of empirical estimates of loss aversion. https://osf.io/hnefr/download and https://epub.ub.uni-muenchen.de/75121/1/275.pdf (a11-a13, d11, d12). Journal record https://doi.org/10.1257/jel.20221698 [M] (b08)
- [V] Ruggeri et al. (2020) Replicating patterns of prospect theory for decision under risk. https://www.nature.com/articles/s41562-020-0886-x (abstract page; a14, b01)
- [V] Territorial prospect theory replication, OSF preprint v2. https://api.osf.io/v2/preprints/z5n9g_v2/ (abstract record; b02, d16)
- [V] Walasek and Stewart (2015) How to make loss aversion disappear and reverse. https://pmc.ncbi.nlm.nih.gov/articles/PMC4312134/ (b03)
- [V] Yechiam (2019) Acceptable losses: the debatable origins of loss aversion. https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A29663131%20AND%20SRC%3AMED&format=json&resultType=core (abstract; b04)
- [M] Gal and Rucker (2018) The loss of loss aversion. https://doi.org/10.1002/jcpy.1047 (via Wikipedia; b05, c24). Not opened.
- [M] Yechiam and Hochman (2013) Losses as modulators of attention (via Wikipedia; b06)
- [M] Mrkva, Johnson, Gaechter and Herrmann (2020) Moderating loss aversion (via Wikipedia; b07)
- [M] Walasek, Mullett and Stewart (2024) meta-analysis of loss aversion (via Tarabeih; b09)
- [M] Yechiam and Zeif (2025) Loss aversion is not robust. https://doi.org/10.1016/j.joep.2025.102801 (not opened; IDEAS abstract page read for d13, https://ideas.repec.org/a/eee/joepsy/v107y2025ics0167487025000133.html)
- [M] Imai et al. (2025) human PT meta-analysis (via Tarabeih; a33, b26)
- [V] Wikipedia Prospect theory and Loss aversion (tertiary). https://en.wikipedia.org/wiki/Prospect_theory ; https://en.wikipedia.org/wiki/Loss_aversion (a30, a31)
- [V] Tarabeih (2026) Prospect theory in large language models: a meta-analysis. https://arxiv.org/abs/2610.33103 (a15-a19, b11, b12, b27, c08, c25)
- [V] Jia, Yuan, Pan, McNamara and Chen (2024) Decision-making behavior evaluation framework for LLMs under uncertain context. https://arxiv.org/abs/2406.05972 (a20, b13, c01, c02)
- [V] Ross, Kim and Lo (2024) LLM economicus? https://arxiv.org/abs/2408.02784 (a21, a22, b15)
- [V] Ethayarajh et al. (2024) KTO. https://arxiv.org/abs/2402.01306 (a23, c19, c20, d18)
- [V] Wang, Liu, Wang and Liu (2026) Developmental trajectories of decision making in LLMs. https://arxiv.org/abs/2601.14268 (a24, b23)
- [V] Suri, Slater, Ziaee and Nguyen (2023) Do LLMs show decision heuristics similar to humans? https://arxiv.org/abs/2305.04400 (a25, b18)
- [V] Yechiam and Tarabeih (2026) Mimicry without understanding. https://arxiv.org/abs/2608.12339 (a26, b20, d09, d10)
- [V] Corazzini, Deriu and Guerzoni (2025) Decision and gender biases in LLMs. https://arxiv.org/abs/2511.12319 (a27)
- [V] Marks and Vollberg (2026) The psychophysics of affect in LLMs. https://arxiv.org/abs/2610.40985 (a28, b21)
- [V] Du (2025) Mitigating gambling-like risk-taking behaviors in LLMs. https://arxiv.org/abs/2506.22496 (a29, c18)
- [V] Wang et al. (2025) Rethinking prospect theory for LLMs. https://arxiv.org/abs/2508.08992 (b14, c03-c05, d14, d15)
- [V] Binz and Schulz (2022) Using cognitive psychology to understand GPT-3. https://arxiv.org/abs/2206.14576 (b16)
- [V] Chen, Liu, Shan and Zhong (2023) The emergence of economic rationality of GPT. https://arxiv.org/abs/2305.12763 (b17)
- [V] Echterhoff et al. (2024) Cognitive bias in decision-making with LLMs. https://arxiv.org/abs/2403.00811 (b19)
- [V] Yee and Koh (2026) LLMs as calibrated measurement instruments for behavioural research. https://arxiv.org/abs/2602.01022 (b22)
- [V] AI decision under risk with framing (GPT-4o, o3, Claude Sonnet 4, Gemini). https://arxiv.org/html/2508.00902 (b24, c09-c11)
- [V] Dubedy (2026) Persona-conditioned risk behavior in LLMs. https://arxiv.org/abs/2603.15831 (b25, c16, d17)
- [V] Ge, Zhang and Vorobeychik (2026) Mind the (DH) gap. https://arxiv.org/abs/2602.15173 (d01-d03; c06, c07 via https://hyper.ai/en/papers/acl__2026__2026.acl-long.479)
- [V] The bias is in the details: an assessment of cognitive bias in LLMs (2025). https://arxiv.org/abs/2509.22856 (c12, c13)
- [V] How personality traits shape LLM risk-taking behaviour (2025). https://arxiv.org/abs/2503.04735 (c14, c15)
- [V] Reproducing human biases in route choice using LLMs (2026). https://arxiv.org/abs/2607.11632 (c17)
- [V] Heuristics and biases in AI decision-making: implications for responsible AI (2024). https://arxiv.org/abs/2410.02820 (c21)
- [V] Kraishan (2026) The long road to the same answer. https://arxiv.org/abs/2610.10049 (d04, d05)
- [V] Lyu et al. (2025) Self-adaptive cognitive debiasing (SACD). https://arxiv.org/abs/2504.04141 (d06, d07)
- [V] Lim, Kim and Whang (2026) DeFrame. https://arxiv.org/abs/2602.04306 (d08)
- [M] Tversky and Kahneman (1992) full text; Kahneman, Knetsch and Thaler (1990) mug study (a31, tertiary); Neumann and Bockenholt (2014), Markowitz (1952), Williams (1966), Allais (1953), Koszegi and Rabin (2007), Tanaka, Camerer and Nguyen (2010): cited in other papers only.

## Source audit (2026-11-20)

Fresh auditors re-opened the sources of 10 established claims: 10 confirmed as written, 0 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **E18.04-K02** (now single-source: only one opened source, code check).
