# Prospect theory and risky choice: deep document

*Subfield A03.03. Relevance to our agent: background only. No schema change is justified by this subfield alone. Evidence ids (a01, b05, c01, d04 and so on) point to evidence_a-d.jsonl; claim ids (K01 to K37) point to claims.jsonl. Status marks follow SCHEMA.md: [E] established (two or more independent sources), [S] single source, [C] contested.*

## 1. What it is

Prospect theory is a descriptive theory of how people choose between risky options. It was built to explain choices that expected utility theory cannot. Its core claims:

- People judge outcomes as gains or losses from a **reference point** (usually the status quo), not as final wealth.
- The value function is concave for gains, convex for losses, and steeper for losses than gains (**loss aversion**).
- Probabilities are not used as stated. They are turned into **decision weights**. Small probabilities are overweighted. Moderate and high probabilities are underweighted. Sure things get extra weight (**certainty effect**).
- Choice has two phases. An **editing phase** reframes the options (coding, combining, cancelling shared parts, simplifying, spotting dominance). An **evaluation phase** scores the edited prospects and picks the highest value.

The critics' main point: the theory fits choices, not the process that produces them. The editing phase is described but was never formally tested (a07). Newer critics also say loss aversion may not be a general preference at all (K10, K35).

Why this matters for a thinking agent, in plain terms:

1. It is the standard yardstick of "human-like" bias in decisions. Many papers now ask whether language models show it.
2. It gives clean test items (sure-versus-gamble pairs, gain-versus-loss wording) for checking whether an agent's choice depends on wording rather than substance.
3. It warns that fitted "risk parameters" for a model are not traits. They move with prompt, elicitation method and what the model just read.

## 2. History and theories in depth

### 2.1 Kahneman and Tversky (1979)

Source: a01-a07 (opened, MIT PDF). The paper starts from problems, answered by small groups of students and faculty, with hypothetical money. It reports percent choosing each option.

- **Certainty effect (Allais type).** Problem 1: 82% took 2,400 for sure over (2,500 at .33; 2,400 at .66; 0 at .01), N=72. Problem 2: 83% took (2,500 at .33) over (2,400 at .34), N=72. Together these break the independence axiom of expected utility.
- **Common ratio.** Problem 3: 80% took 3,000 for sure over (4,000, .80), N=95. Problem 4: 65% took (4,000, .20) over (3,000, .25), N=95. Problems 7 and 8 do the same with small probabilities: 86% took (3,000, .90) over (6,000, .45), but 73% took (6,000, .001) over (3,000, .002), N=66.
- **Non-money prizes.** Problem 5: 78% took a sure one-week tour over a 50% chance of a three-week tour, N=72. Problem 6 with 5% versus 10% chances: 67% chose the bigger prize with lower odds. The certainty effect is not only about money.
- **Reflection effect.** Problem 3': (-4,000, .80) versus -3,000 sure: 92% chose the gamble, N=95. Same numbers as Problem 3 with signs flipped. Risk-averse for gains, risk-seeking for losses. Problem 13 (gains): 82% took the split (4,000 at .25; 2,000 at .25) over (6,000 at .25), N=68. Problem 13' (losses): 70% took the single (-6,000, .25), N=64.
- **Isolation effect.** Problem 10, a two-stage game with a .25 chance to reach stage two: 78% chose the sure 3,000 branch, N=141. Final outcomes equal Problem 4, where only 35% chose the 3,000-at-.25 option. People ignore what is shared by both branches and judge the second stage alone. Problems 11 and 12 (bonus of 1,000 or 2,000 added first): 84% took a sure +500 (N=70), but 69% took the gamble at -1,000 (N=68), though final wealth is identical.
- **Small probabilities.** Problem 14: 72% took a 1-in-1000 chance of 5,000 over a sure 5, N=72. Problem 14': 83% took a sure loss of 5 over a 1-in-1000 chance of -5,000, N=72. Lottery tickets and insurance are both attractive. Problem 9 (probabilistic insurance): 80% said no, N=95.

Theory structure (a07):

- Editing operations: coding, combination, segregation, cancellation, simplification, dominance detection.
- Evaluation for regular prospects: V(x,p; y,q) = pi(p) v(x) + pi(q) v(y).
- The paper gives no numeric parameters. Loss aversion is argued from rejection of symmetric 50-50 bets: v(x) < -v(-x).
- Weights are not well behaved near 0 and 1.

### 2.2 Cumulative prospect theory (Tversky and Kahneman 1992)

Source: a08, d23, b03 (not opened directly; the primary text was not retrieved).

- Rank-dependent cumulative weights. This fixes the 1979 problem of violating stochastic dominance, and extends to many outcomes and to uncertainty.
- Parametric form: value x^alpha for gains, -lambda (-x)^beta for losses. Weight w(p) = p^g / (p^g + (1-p)^g)^(1/g).
- Fitted to certainty equivalents from 25 graduate students, unincentivised. Median alpha = beta = 0.88 and lambda = 2.25 are confirmed through Brown et al. (b03). Gamma 0.61 for gains and delta 0.69 for losses are from memory. Tarabeih uses 0.65 as the weighting benchmark, the mean of the two (d23). Treat 0.61 and 0.69 as likely, not verified.
- It predicts the **fourfold pattern**: risk aversion for likely gains and unlikely losses, risk seeking for likely losses and unlikely gains.

A second human benchmark is Tanaka et al. (2010): alpha 0.670, lambda 2.630, gamma 0.685. Wang et al. use it to score models (b11).

### 2.3 Critiques and rival accounts

- **Decisions from experience** (Hertwig et al. 2004; a11, d19). When people learn outcomes by sampling, rare events are underweighted. This is the reverse of the description pattern.
- **Range and decision-by-sampling** (Walasek and Stewart 2015; b05). Loss aversion depends on the spread of gains versus losses in the task.
- **Loss aversion is not general** (Gal and Rucker 2018; Yechiam 2019; Mukherjee 2019; b07, d20, d21). Rival explanations: status quo bias, inertia, attention to losses, a risky-bet premium. Small losses often are not overweighted.
- **Complexity heuristics** (Oprea 2024; d18). The same anomalies appear when payments are deterministic but split up to look like lotteries.
- **Process critique.** The editing phase is not tested as a process (a07).

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Certainty effect (Allais type) | Prob 1: 82% sure option (N=72). Prob 2: 83% for 33% gamble (N=72) | a01, K01 | [E] |
| Common ratio effect | Prob 3: 80% sure; Prob 4: 65% gamble over 25% (N=95). Prob 7/8: 86% vs 73% (N=66) | a02 | [E] |
| Same effect with non-money prizes | 78% sure tour (N=72); 67% for lower odds, larger prize | a03 | [E] |
| Reflection effect | Prob 3: 80% sure gain. Prob 3': 92% gamble for losses (N=95). Prob 13/13': 82% vs 70% | a04, K02 | [E] |
| Isolation effect | Prob 10: 78% sure branch (N=141) vs 35% for same final prospect | a05, K03 | [S] |
| Overweighting of tiny probabilities | Prob 14: 72% lottery; 14': 83% insurance (N=72 each) | a06, K04 | [E] |
| Multinational replication of 1979 items | N=4,098, 19 countries, 13 languages; 94% of items, 12 of 13 contrasts; effects attenuated; country heterogeneity | a10, b04, K05 | [S] (one large study) |
| Mean human loss aversion | 1.955 [1.820, 2.105], 607 estimates, 150 articles | a09, b01, K06 | [E] |
| Bias-corrected loss aversion | 1.742 [1.674, 1.811]; unpublished papers about 0.25 lower; covariates explain 15.5% of variance | b02, b03, K07 | [S] |
| Original lambda 2.25 | median of 25 unincentivised graduate students | a08, b03 | [E] about the origin |
| Skew of loss-aversion estimates | aggregate mean 1.95, median 1.52 (n=281); individual mean 2.94, median 1.80 (n=160); range 0.04 to 23.46 | b25, K08 | [S] |
| Range dependence | Gain-wide ranges lambda 1.6-2.3; symmetric about 1.0; loss-wide 0.81-0.93. Exp 1a N=358, 1b N=423, 2 N=429, 3 N=88 (real money) | b05, b06, K09 | [E] |
| Money vs non-money, functional form, reference point | little difference in the meta-analysis | b02 | [S] |
| Accountability does not reduce loss aversion | two new experiments plus a direct replication with nearly double the sample; Bayesian evidence for no difference | a12, K11 | [S] |
| Description-experience gap | rare events overweighted from description, underweighted from experience; over 70,000 choices, over 6,000 people; persists when sampling error is removed | a11, d19, K12 | [E] |
| Concrete events shrink the certainty effect | shift -39 points with percentages vs -12 with a 00-99 draw (z=2.34, p=.019) | d22, K36 | [S] |
| Pattern extends to non-monetary information | gamble less likely under information-loss frame; endowment effect for trivia; fact version of Asian disease | b08, K14 | [E] |
| Loss aversion as a general preference | critics: small losses often not overweighted; no balance toward losses | b07, d20, d21, K35 | [C] |
| Anomalies appear without risk | deterministic disaggregated payments give equal-strength anomalies | d18, K13 | [C] |

## 4. Mechanisms and models

Written so that an engineer could score an agent against it.

### 4.1 Value function

- v(x) = x^alpha for x >= 0.
- v(x) = -lambda * (-x)^beta for x < 0.
- alpha and beta below 1 mean diminishing sensitivity. 1992 median 0.88 for both. Tanaka: alpha 0.670.
- lambda above 1 means losses weigh more. 1992: 2.25. Meta-analytic mean 1.955. Bias-corrected 1.742. Tanaka 2.630.
- Reference point r: outcomes are x - r. The reference point is a free input. In lab tasks it is zero. In real tasks it can be status quo, expectation, peak or purchase price (K32). Set it explicitly or the model will guess.

### 4.2 Probability weighting

w(p) = p^g / (p^g + (1-p)^g)^(1/g). With g below 1 the curve is an inverse S. Small p is overweighted and large p underweighted. Tanaka g = 0.685. 1992 values about 0.61 (gains) and 0.69 (losses), not verified.

### 4.3 CPT evaluation, step by step

1. Edit the prospect. Merge equal outcomes, drop shared components, drop dominated options.
2. Split outcomes into gains and losses relative to r.
3. Rank gains from best to worst and losses from worst to best.
4. Decision weight of outcome i = w(cumulative probability up to and including i) minus w(cumulative probability before i). Do this separately for gains and losses.
5. Value of prospect = sum of weight times v(outcome).
6. Choose the higher value. To fit data, add logit noise: P(A) = 1 / (1 + exp(-theta (V_A - V_B))).

### 4.4 Fitting parameters to an agent (as used for LLMs)

Two designs appear in the LLM work:

- **TK-style certainty equivalents.** Ask for the sure amount that makes the model indifferent. Fit alpha, lambda, gamma (Ross et al.; a15).
- **Tanaka-style choice lists.** Series of binary choices with switching points (Jia et al.; Wang et al.; a17, b11).

Rules we can borrow:

- A competence screen first: switching points must be monotone (a15). Only GPT-4 and GPT-4 Turbo passed it in that study.
- A reliability rule: mean absolute error at most 0.20 and McFadden R2 at least 0.10 (b11). Llama-3.1-8B and Qwen2.5-14B failed it.
- Fits at the optimiser bound (lambda 0.010 or 4.000) are failures of the fit, not findings (b11, d12).
- Report medians with intervals, not means (b25).

### 4.5 Why the fits are fragile

- The same model gives curvature 1.01 under a TK fit and 0.52 under a Tanaka fit (K17).
- Verbal probability words ("likely") shift parameters, most of all lambda (b12).
- Between-model lambda spans 0.01 to 4.0 in one study (d12). Within-model repeat stability is good for lambda at temperature up to 0.7 (coefficient of variation under 0.15) and poor at 1.0 (above 0.30). Probability weighting repeats poorly (intra-class correlation 0.62) (d13).

### 4.6 Process-level mechanisms

- **Editing as input transformation.** The isolation effect and framing effects are editing effects. They suggest a rewrite step: express every option in final outcomes before scoring. In people, concrete events shrink the certainty effect (d22). For models, a maths-form rewrite removes framing flips (d02).
- **Decision by sampling.** Value is relative rank within the range of outcomes in context (b05). An agent's "lambda" will move with whichever range of gains and losses is in its context.
- **Complexity heuristic.** If anomalies come from complexity rather than preferences, a deterministic control arm removes them (d18). This is untested in models (K34).

## 5. What holds up

### 5.1 Strong

- **The 1979 core patterns replicate.** One preregistered multinational test: 94% of items and 12 of 13 contrasts, N=4,098 (a10, b04). Effects are attenuated and vary by country. The failing contrast is not named in the abstract.
- **Loss aversion is real on average, but about 1.7 to 2.0, not 2.25.** 607 estimates (a09, b01). Publication bias is modest (b03). Covariates explain little (15.5%, b02). Estimates are very skewed (b25).
- **The description-experience gap is robust** (a11, d19). Problem structure moderates it. Small samples are the largest driver, but it persists without sampling error.

### 5.2 Failures and boundary conditions

- **Range effect.** Loss aversion vanishes (about 1.0) or reverses (0.81-0.93) when losses have the wider range (b05, replicated b06). In Exp 2 the reversed condition was about 1.01, not below 1.
- **Stake and design effects.** Small losses are often not overweighted (d20, d21). Field and general-population samples give higher lambda than student labs (b02). One survey found median lambda 0.99 in a US representative sample vs 1.84 in a college sample (b02, Chapman et al.).
- **Accountability does not reduce loss aversion.** Vieider's result failed in two new experiments and a direct replication (a12).
- **Oprea's no-risk mirror.** Same anomalies appear with deterministic payments (d18). A reply says participants were confused (K13). Contested.
- **Feelings are not choices.** In affect studies, losses did not hurt as predicted when experienced (b07).

### 5.3 Moderators

Range of gains and losses; stake size; elicitation (certainty equivalent, choice list, survey); sample type; description versus experience; wording of probabilities; concreteness of the event format (d22).

### 5.4 Interventions

Worked in people:

- Concrete event format (00-99 draw) cut the certainty-effect shift from -39 to -12 points (d22, single source).

Did not work in people:

- Accountability for loss aversion (a12).

Worked in LLMs:

- Stripping a narrative to final-outcome maths removed framing flips (o3 200/200, GPT-4o 196/200 indifferent; d02, single source).
- A short rationale moved conversational models toward expected value (d06).
- A joint-evaluation prompt reduced priming by "humans are loss averse" text, except when gains equal losses (d09, single source).
- Few-shot examples moved GPT-4 more than labels (a16, single source).

Did not work in LLMs:

- Telling GPT-4 to be risk or loss averse barely moved it. On losses curvature moved the wrong way (a16).
- Zero-shot chain of thought did not move GPT-4 toward rational (K19).
- Math explanations did not help conversational models and often hurt (d06).
- Longer rationales sometimes reduced rationality (c16).
- 100 simulated draws did not remove the description-history gap (d05).
- This agrees with SCHEMA.md section 4b: "slow down" and bias-checklist instructions are not added.

## 6. Language models

### 6.1 Overview

Almost all evidence is from hypothetical choices, and mostly from models older than 2026. Behaviour depends on model class, prompt, elicitation and format. There is no single "LLM prospect-theory profile".

### 6.2 Early full-bias test (GPT-3)

Binz and Schulz (a18): over 13,000 problems. GPT-3 showed 3 of the 6 Kahneman-Tversky biases: framing, certainty effect, overweighting of small probability differences (1% vs 2% counted more than 41% vs 42%). Only the largest model beat chance on choices13k: t(29134) = -16.85, but below humans: t(29134) = -11.50. This is the only full six-bias test, and it is GPT-3 only (K15, [S]).

### 6.3 Loss aversion in LLMs

- **Pooled estimate** (Tarabeih 2026; c01, c02, d10): lambda 1.26 [1.06, 1.46], 102 estimates, 11 studies, 32 models. Prediction interval 0.20 to 2.31, so very wide. Egger p=.58, Begg p=.37.
- **By design:** symmetric designs (18 estimates, 7 studies) 1.15 [0.98, 1.32] vs human 1.07. Losses smaller than gains (10 estimates, 4 studies) 1.46 [0.96, 1.96] vs human about 2.3 (p=.004).
- **Release year:** within a family, lambda falls about 0.16 per year. GPT-3.5 2.72, GPT-4.1 0.57. Stake: +0.35 per tenfold rise (p=.030). Persona not significant. Gemini about +0.69 over GPT.
- The human benchmark matters. Against 1.07 or 1.31 (conservative meta-analyses), LLMs look human-like. Against 2.25 they look weak. "LLMs are less loss averse than humans" depends on which human number is used.
- Ross et al. (a15, b09): 56 game settings, 100 samples each, temperature 1. Only GPT-4 and GPT-4 Turbo passed the competence test. LLMs had weaker loss aversion and similar risk aversion. GPT-4 Turbo was risk seeking for losses like humans. GPT-4 was risk averse for losses.
- Jia et al. (a17): ChatGPT-4-Turbo, Claude-3-Opus, Gemini-1.0-pro, 300 repetitions. All risk averse. ChatGPT had the lowest loss aversion and a weighting parameter above 1 (opposite to humans). Claude overweighted small probabilities. Older model versions.
- Wang et al. (b11, d12): 35 lottery pairs, 8,960 choices per condition, temperature 0.7. Lambda: Llama-3.1-8B 0.010 (bound), Qwen2.5-7B 0.010 (bound), Mistral-7B 0.570, Qwen2.5-14B 1.909, Qwen2.5-32B 1.213, Gemini-2.5-Flash 1.499, GPT-5-Mini 4.000 (bound). Human benchmark 2.630. Larger models fit better. Loss aversion stays unstable.
- Current reasoning models (Marks and Vollberg, d16): 10 LLMs. Higher-EV gamble on 94.3-99.9% of trials for gpt-5-nano, gpt-5.2, grok-4.3, gemini-3-flash and kimi-k2.5. claude-sonnet-4.5 83.5%. llama-3.1-70b 73.0%. gpt-4o-mini took the lower-EV gamble 53.6% of the time. Lambda 0.88-1.59 across models. At equal EV most took the sure option (gamble 10.8-38.1%).
- Feeling ratings run the other way. Gains were rated stronger than losses in 8 of 9 post-trained models (+1.2 to +24.3), linearising to 0.98-0.99 when outcomes are rated jointly. Choices show no such asymmetry (d16, single source).

### 6.4 Rationality versus bias by model class

- **Reasoning models track expected value.** Ge et al. (d04): 20 LLMs, 360 Prolific humans, 324 questions per model, 10 queries each at temperature 1. Correlation with an expected-payoff maximiser: reasoning models (GPT-5.1, DeepSeek-R1, Gemini-2.5-Pro) 0.86 to 1.0. Conversational models below 0.5. Humans 0.14. Highest LLM-human correlation 0.42 (Claude-4.5-Haiku). Math-trained twin vs instruct: Qwen2.5-Math-7B 1.00 vs Qwen2.5-7B-Instruct 0.64. Olmo-3-7B-Think 1.00 vs Instruct 0.73.
- **Conversational models are order- and frame-sensitive** (d04).
- **LLMs predict human gambles as more rational than humans** (Liu et al., c17): GPT-4o Spearman 0.94 with max-EV when predicting, vs humans 0.48 on choices13k. Chain-of-thought simulation 0.90. This is a different question from how the model chooses as itself: zero-shot, GPT-4-Turbo and GPT-4o reach 0.41 and 0.28 (K21; the critique corrected this mix-up). Do not treat the two as one number.
- **Budget tasks.** GPT is more internally consistent than people (Chen et al., a20, c11). 95, 89, 81 and 92 of 100 GPT observations had no GARP violations in risk, time, social and food tasks. Human sample 347. GPT's score was higher in all four domains (p<.01). Consistency breaks under language reframing (K24, [S]).
- **Personality prompts.** Hartley et al. (c10): GPT-4o is close to risk neutral on non-mixed prospects. Openness correlation with risk taking for gains 0.63, with risk aversion for losses 0.44. It could not be made risk seeking for gains.

### 6.5 Framing

- ChatGPT (GPT-3.5; Suri et al., a19, b16): drug efficacy rated 5 in all 11 positive-frame trials and 4 in all 11 negative-frame trials. Humans 5.2 vs 4.6, t(80)=3.86. The output had no variance. Anchoring: ChatGPT t(58)=8.78, humans t(58)=5.55.
- Payne 2025 (c04, d01-d03): GPT-4o, o3, Claude Sonnet 4 with and without thinking, Gemini 1.5 Pro. 25 runs per condition, 2,550 decisions. Equal-EV three-option items.
  - Championship: loss frame 85.6% chose risky BLITZ vs 0.8% in the gain frame. Effect size +1.40 to +1.84 on a 0-2 scale.
  - Career transition: reversed in all five. Loss frame 87.2% safe vs 41.6% in the gain frame (-0.37 to -0.60).
  - Business merger: near zero (65.6% vs 62.4%).
  - Pure symbols: o3 200/200 and GPT-4o 196/200 indifferent. If forced, always the sure option.
  - Framing size was not tied to how often the model computed EV.
  - Single-scenario figures cannot be pooled.
- Reconciling Ge and Payne: reasoning models follow EV on numbers (Ge 0.86-1.0; Marks and Vollberg 94-99.9%) but flip with story framing (Payne). The difference is format, numbers versus narrative (K27, K28). Different tasks, not pooled.
- Echterhoff et al. (a21, c14): awareness prompting reduced biased framing and status-quo effects in admission decisions. The numbers (17.2% and 8.5%) were read from two-column text and are uncertain (K25).

### 6.6 Description versus experience

Ge et al. (d05): all 20 LLMs move toward human-like and away from EV-like choice when prospects are shown as histories of 20 or 100 simulated payoffs. The gap is modest for frontier reasoning models (GPT-5.1 and DeepSeek-R1 correlation with the EV agent about 0.98 on implicit prospects; Gemini-Pro 0.94), large for conversational models (0.45-0.58; humans 0.53) and large for small open reasoning models. 100 draws do not remove the gap. Context length is not the cause. Per-model numbers for 20 vs 100 are in an appendix we did not read. Hintze et al. (d17, abstract only): GPT-3.5 risk seeking, Claude 3.0 strong recency, GPT-4 underweighted small and overweighted large probabilities, resembling decisions from experience.

### 6.7 Prompt and literature priming

Yechiam and Tarabeih (c18, d07-d09), ChatGPT-4o and Qwen:

- Baseline lambda for ChatGPT 1.09. After the Brown abstract 1.785. After Yechiam and Zeif 1.043. Full Brown report 1.519 vs 1.082 for full Yechiam and Zeif. ChatGPT accepted 105% more lotteries after Yechiam and Zeif than after Brown. Qwen 1.170 vs 1.047. McFadden R2 .58 (abstracts), .33 (full text).
- Being told humans are loss averse raises lambda (ChatGPT 1.257 and 1.218 vs 1.072 when told gain seeking; Qwen 1.742 vs 0.940 and 0.929).
- Sample size does not matter: n=43 vs 10,583, interaction p=.75.
- A joint-evaluation prompt (judge all six lotteries together) cut the effect, except when gains equal losses. Details are in the supplement, not read.
- Yechiam and Tarabeih and Tarabeih share an author.

Other prompt effects:

- Wang et al. (b12): verbal probability words shift parameters, mostly lambda. Larger models were more robust.
- Ross et al. (a16): a "be loss averse" label barely moved GPT-4. One-shot examples did. Role-playing a teenager lowered loss aversion.
- Dubedy (c19): GPT-4.1 with Rich, Middle and Poor personas played 1.11, 7.83 and 37.39 slot rounds on average. Kruskal-Wallis H=393.5. Cohen's d=4.15 on the risk score. 6,950 decisions.
- Yee and Koh (d13): baseline lambda 1.12 under a rational profile (range 1.12-1.90 across baselines). A loss-averse profile gave 3.00 (+1.88, d=1.82). 19,200 agent-scenario pairs.

### 6.8 Training effects

- Itzhak et al. (b19, d11): certainty-effect bias score for pretrained bases 0.00 (DaVinci), 0.09 (T5), 0.03 (Mistral). Tuned: 0.24 (DaVinci-002), 0.67 (DaVinci-003), 0.17 (Flan-T5), 0.29 (Mistral-Instruct). RLHF amplifies, and instruction tuning alone is enough. Product-choice templates, 2023 models. No lambda contrast exists (K23, [S]).
- Within families, lambda falls with release year (c02). The cause is not resolved.
- Prospect theory as a training signal, not a behaviour: KTO (c21) uses the Kahneman-Tversky value function with a loss-aversion weight to align LLMs from binary feedback. Risk-neutral value function GSM8K 42.0 vs default 53.5. Concave log 42.5. Swapping DPO for KTO on Zephyr-SFT raised GSM8K by 13.5 points. This is about training, not our scaffold.
- Du (c20): a training framework with a loss-aversion mechanism cut loss-chasing 24.3% and overconfidence 18.7% (reported, one preprint).

### 6.9 Agents and reference points

- Hashimoto et al. (d14): a GPT-4o trading agent sold 97 of 100 when price was above purchase and below its peak (G+) and 85 of 100 in G-. It bought 90 of 100 in L- and 87 in L+. Qwen-2.5-7B kept selling gains even after a fall from the peak. In 500 simulated days the LLM agents reproduced a price-near-high anomaly that rule agents could not.
- Li et al. (d15): year-long stock simulations. Prompted strong-loss-aversion agents switch style less in all four models (rank-biserial 0.47 to 0.67; GPT-4o-mini p=.0003). Other drivers align poorly.
- Han et al. (c23): 3,000 route-choice agents with reference points inferred from expected travel time. Behaviour reported as consistent with CPT.
- Niimi (c24): giving reference points (prior rating, expectations) as structured input improved sentiment prediction for a 3B model. Macro-F1 +1.6% and +4%, RMSE -16% and -9.1%.
- Horton (a13, c26) and Centaur (c27) frame LLMs as simulated economic agents. Not read for numbers.

## 7. What our agent should take

Overall: this subfield is background. It gives us (a) test items, (b) a reference for what wording sensitivity looks like, and (c) cautions against reading fitted parameters as traits. Nothing here changes a state or operator without a test.

### Add now (established)

| Item | Schema part | Status | Evidence |
|---|---|---|---|
| Do not assume the model's choice follows stated numbers when a sure option or framing is present. Check consistency on a reworded variant | G (supports G3: a pass must be on something not fitted, here a reworded variant) | [E] | K22: a19, b16, c04, d01; K27: d04, d16 |
| Keep literature-reported effect sizes and "humans are biased this way" text out of the attempt context on decision tasks | G / S1 input hygiene (extends the existing marked-block rule) | [E] | K18: c03, c18, d07, d08 |
| Prefer numeric probabilities over verbal ones in anything the agent must compute from | G / S1 | [E] | K17: b11, b12, c06, d12 |
| State the reference point and range explicitly in any gain-versus-loss task | G / S1 restate | [E] | K09: b05, b06; K32: d14, d15 |
| Do not treat one fitted parameter (lambda, gamma) as a stable fact about a model. Report medians with intervals and repeat | memory / S9 logging | [E] | K33: d12, d13; K17 |
| Use a human lambda reference of 1.7 to 2.0, never 2.25, when comparing | memory (benchmarks) | [E] | K06: a09, b01, a08 |
| Do not use the agent as a simulator of human risky choice without calibration | memory (do-not-use note) | [S], low cost | K21: c17 |
| Keep "do not add": generic "be careful" or bias-awareness prompts | 4b (already there) | [E] | K19: a16; SCHEMA 4b |

None of these needs new machinery. Most are a one-line input-hygiene or logging rule. Because G7 says every element must pay for itself, the first two should still be confirmed by the bench tests below.

### Test first

| Item | Schema part | Status | Evidence |
|---|---|---|---|
| A "restate in final outcomes, neutral wording" step before choosing, to cut framing flips | O6 (change representation) or S1 restate | [S] | K29: d02; K03: a05; K36: d22 |
| An expected-value check step on numeric items (code computes EV, model sees it) | S4 TEST on numeric items | [S]. That reasoning models follow EV is [E] (K27); that the step helps an agent is untested | K20, K27: d04, d16 |
| Joint evaluation (judge all options together) as a guard against priming by described bias | G5-style code selection | [S] | K31: d09 |
| Reference-point statement guard in multi-step tasks | G / S1 | [S] | K32: d14, d15 |
| Stripping narrative from decision items before scoring | S1 input hygiene | [S] | K28, K29: d01, d02 |
| Do not let the agent learn risk from a few simulated draws. Give stated probabilities | G (for experience-style inputs) | [S] | K30: d05 |

## 8. Concrete tests on our bench

All tests: both arms at equal tokens (G7), setup cost counted. Use at least 40 items per arm and at least 10 repeats at temperature 0.7. Report medians with intervals. Gap numbers refer to critique.md.

| # | Item type | Arms (equal tokens) | Metric | Expected effect |
|---|---|---|---|---|
| T1 | Verbatim 1979 problems (1, 2, 3, 3', 4, 7, 8, 10, 14, 14') plus matched variants, on the model our bench uses (gap 1) | plain direct answer vs plain short reasoning | Share of human-pattern choices (certainty reversals, reflection flips, isolation gaps) | A reasoning-capable model is near EV on pure numbers (K27), so few reversals. If many remain, the effect is real for this model |
| T2 | Same item in gain wording, loss wording and final-outcome wording, narrative versions like Payne's (championship, career, merger) (gap 2) | A: plain short chain of thought. B: neutral final-outcome restatement, then choose, same total tokens | Framing flip rate (share of items whose choice differs across gain and loss wording) | B cuts flips on narrative items vs A. No change on pure numeric items (K28, K29) |
| T3 | 20 numeric items with a sure option | A: model alone. B: code-computed EV shown before the choice | Share of EV-maximising choices | Small gain for conversational-class models, none for reasoning models (K20) |
| T4 | Prospect described in words vs listed as 20 or 100 sampled draws (gap 3) | description vs 20 draws vs 100 draws, same tokens | Correlation with EV; choice gap between formats | Gap present, shrinks at 100 draws, does not vanish (K30) |
| T5 | Mixed 50-50 gambles with gain-wide, symmetric and loss-wide ranges (K09) | same model, three range conditions | Fitted lambda per condition (medians) | If lambda follows range as in people, the agent uses range-relative value. If flat, it does not |
| T6 | Context holds a paper abstract saying humans are loss averse vs one saying not. Then a lambda elicitation (gap 4) | A: no guard. B: abstract in a marked block plus joint evaluation of all options | Fitted lambda difference between conditions | B cuts the difference by at least half (K31) |
| T7 | Same lambda elicitation repeated 10 times at T=0, 0.7 and 1.0 (gap 9) | single run vs median of repeats at equal total tokens | Coefficient of variation; sign stability | CV under 0.15 for T up to 0.7 (K33) |
| T8 | Oprea mirror: deterministic payments split to look like lotteries vs real lotteries (gap 6) | lottery vs deterministic disaggregated | Fourfold-pattern strength in each | If the pattern persists in the deterministic arm, LLM weighting is a complexity artefact (K34) |
| T9 | Multi-step task with a changing reference point (purchase price, peak, expectation) (gap 7) | reference stated vs unstated | Choice shift and consistency | Choices follow the stated reference point (K32) |
| T10 | Awareness prompt vs none on framing items (K25) | A: none. B: awareness prompt | Flip rate | Small drop at best. SCHEMA 4b predicts a null. Run only as a control |

## 9. What does not transfer, and why

- **Fitted CPT parameters are not agent traits.** They move with prompt, elicitation, temperature, model release and what the model just read (K17, K18, K33). Do not log "agent lambda" as a stable fact.
- **Human loss-aversion numbers are uncertain.** 2.25, 1.95, 1.74, or 1.07 and 1.31 depending on the source (critique). They are design- and stake-dependent (K35).
- **Hypothetical stakes.** Every LLM test is hypothetical. Models have no real stakes, so stake arguments from the human literature do not map directly.
- **Loss aversion for a model has no hedonic meaning.** Feeling ratings and choices disagree (d16).
- **Models as simulated humans.** LLMs predict human gambles as more rational than humans do (c17). Simulating human bias needs calibration.
- **Old-model evidence.** Most LLM studies used GPT-3 to GPT-4o, Claude 3 to 3.5, Llama 2 and 3. Newer reasoning models behave differently (d04, d16).
- **Training, not scaffold.** KTO and the loss-aversion training framework (c20, c21) use prospect theory as a training objective. They give us no scaffold operator.
- **Single-scenario flips.** Payne's 85.6% vs 0.8% is scenario-specific. It shows wording sensitivity exists, not its size on our tasks.
- **Process claims.** The editing phase is described, not tested. A rewrite step (O6) is an engineering idea inspired by it, not a finding about the theory.

## 10. Open questions

1. Do current reasoning models (o3, Claude 4-class, Gemini 2.5, GPT-5) show the 1979 certainty, reflection and isolation effects on the verbatim items? Still open (gap 1).
2. Does a neutral "final outcomes" restatement beat plain chain of thought at equal tokens? Only a maths-form control exists (gap 2).
3. Per-model size of the description-history gap for 20 vs 100 draws. The appendix was not read (gap 3).
4. Does delayed priming (the agent reads a paper many steps earlier) shift decisions? Only same-context priming has been measured (gap 4).
5. Effect sizes in Wulff et al. 2018, Gal and Rucker 2018 and Yechiam 2019. Abstracts only (gap 5).
6. Does the Oprea mirror pattern appear in LLMs? Untested (gap 6).
7. Do LLMs show expectation-based or status-quo reference shifts in multi-step tasks beyond trading simulations with 2024 models? (gap 7).
8. Why does lambda fall with release year: training data, RLHF or safety training? (gap 8). Itzhak's certainty-effect result points the other way: tuning raises that bias.
9. How stable is lambda across elicitation methods? Only one preprint appendix addresses repeat stability (gap 9).
10. Verify CPT gamma 0.61 and delta 0.69 from the 1992 primary text (gap 10).
11. Is the fourfold pattern a probability-weighting effect or a complexity effect, in people and in models? (K13).

## 11. Sources

[V] = opened and read (page or PDF text). [M] = abstract or snippet only, or recalled from memory.

- [V] Kahneman and Tversky (1979) Prospect theory: an analysis of decision under risk. https://web.mit.edu/curhan/www/docs/Articles/15341_Readings/Behavioral_Decision_Theory/Kahneman_Tversky_1979_Prospect_theory.pdf (a01-a07)
- [M] Tversky and Kahneman (1992) Advances in prospect theory. https://doi.org/10.1007/BF00122574 (a08, c28; values recalled, partly checked via Brown et al.)
- [V] Brown, Imai, Vieider, Camerer (2020, 2022 version) Meta-analysis of empirical estimates of loss aversion. https://osf.io/download/hnefr/ (a09, b01-b03, b25)
- [V] Ruggeri et al. (2020) Replicating patterns of prospect theory for decision under risk. https://www.nature.com/articles/s41562-020-0886-x (a10, b04; abstract page)
- [M] Hertwig, Barron, Weber, Erev (2004) Decisions from experience and the effect of rare events. https://doi.org/10.1111/j.0956-7976.2004.00715.x (a11)
- [M] Accountability and loss aversion, direct replication of Vieider. https://doi.org/10.1177/17470218251369493 (a12)
- [M] Adam-Troian, Bonetto, Arciszewski (2025) territorial extension of the replication. https://doi.org/10.31234/osf.io/z5n9g_v2 (a22, title only)
- [V] Walasek and Stewart (2015) How to make loss aversion disappear and reverse. https://pmc.ncbi.nlm.nih.gov/articles/PMC4312134/ (b05)
- [V] Rakow, Cheung, Restelli (2020) Losing my loss aversion. https://pmc.ncbi.nlm.nih.gov/articles/PMC7704442/ (b06)
- [V] Mukherjee (2019) Revise the belief in loss aversion. https://pmc.ncbi.nlm.nih.gov/articles/PMC6902077/ (b07)
- [V] Litovsky, Loewenstein, Horn, Olivola (2022) Loss aversion, the endowment effect, and gain-loss framing for information. https://pmc.ncbi.nlm.nih.gov/articles/PMC9407664/ (b08)
- [M] Wulff, Mergenthaler-Canseco, Hertwig (2018) A meta-analytic review of two modes of learning and the description-experience gap. https://doi.org/10.1037/bul0000115 (b21, d19; abstract)
- [M] Gal and Rucker (2018) The loss of loss aversion. https://doi.org/10.1002/jcpy.1047 (b22, d20; abstract)
- [M] Yechiam (2019) Acceptable losses: the debatable origins of loss aversion. https://doi.org/10.1007/s00426-018-1013-8 (b23, d21; abstract)
- [M] Hertwig, Wulff, Mata (2019) Three gaps and what they may mean for risk preference. https://doi.org/10.1098/rstb.2018.0140 (b24)
- [M] Oprea (2024) Decisions under risk are decisions under complexity, AER. https://doi.org/10.1257/aer.20221227 (a14, d18; abstract)
- [V] SSRN 7174959 (2026) Framing moves the paradox: concrete numbers attenuate the Allais pattern. https://doi.org/10.2139/ssrn.7174959 (d22)
- [V] Binz and Schulz (2023) Using cognitive psychology to understand GPT-3. https://arxiv.org/abs/2206.14576 (a18)
- [V] Suri, Slater, Ziaee, Nguyen (2023) Do large language models show decision heuristics similar to humans? https://arxiv.org/abs/2305.04400 (a19)
- [V] Chen, Liu, Shan, Zhong (2023) The emergence of economic rationality of GPT. https://arxiv.org/abs/2305.12763 and https://pmc.ncbi.nlm.nih.gov/articles/PMC10740389/ (a20)
- [V] Echterhoff et al. (2024) Cognitive bias in decision-making with LLMs. https://arxiv.org/abs/2403.00811 (a21; numbers uncertain)
- [V] Ross, Kim, Lo (2024) LLM economicus? https://arxiv.org/abs/2408.02784 (a15, a16)
- [V] Jia, Yuan, Pan, McNamara, Chen (2024) Decision-making behavior evaluation framework for LLMs. https://arxiv.org/abs/2406.05972 (a17)
- [V] Wang, Lin, Liu et al. (2025/2026) Rethinking prospect theory for LLMs. https://arxiv.org/abs/2508.08992 (b11, b12, d12)
- [V] Corazzini, Deriu, Guerzoni (2025) Decision and gender biases in LLMs. https://arxiv.org/abs/2511.12319 (b14)
- [V] Saeedi, Goodarzi, Canbaz (2025) Heuristics and biases in AI decision-making. https://arxiv.org/abs/2410.02820 (b15)
- [V] Itzhak, Stanovsky, Rosenfeld, Belinkov (2024) Instructed to bias. https://arxiv.org/abs/2308.00225 (b19, d11)
- [V] Ge, Zhang, Vorobeychik (2026) Mind the (DH) gap: risky choices of reasoning and conversational LLMs. https://arxiv.org/abs/2602.15173 (b20, c15, c16, d04-d06)
- [V] Tarabeih (2026) Prospect theory in large language models: a meta-analysis. https://arxiv.org/abs/2610.33103 (c01-c03, d10, d23)
- [V] Payne (2025) An analysis of AI decision under risk. https://arxiv.org/abs/2508.00902 (c04, c05, d01-d03)
- [V] Hartley et al. (2025) How personality traits shape LLM risk-taking behaviour. https://arxiv.org/abs/2503.04735 (c10)
- [V] Liu, Gu, Griffiths et al. (2024) Large language models assume people are more rational than we really are. https://arxiv.org/abs/2406.17055 (c17)
- [V] Yechiam and Tarabeih (2026) Mimicry without understanding. https://arxiv.org/abs/2608.12339 (c18, d07-d09)
- [V] Dubedy (2026) Persona-conditioned risk behavior in LLMs. https://arxiv.org/abs/2603.15831 (c19)
- [V] Du (2025) Mitigating gambling-like risk-taking behaviors in LLMs. https://arxiv.org/abs/2506.22496 (c20)
- [V] Ethayarajh et al. (2024) KTO. https://arxiv.org/abs/2402.01306 (c21)
- [V] Han et al. (2026) Reproducing human biases in route choice using LLMs. https://arxiv.org/abs/2607.11632 (c23)
- [V] Niimi (2025) Reference points in LLM sentiment analysis. https://arxiv.org/abs/2508.11454 (c24)
- [V] Hans, Gurney, Marsella, Hirschmann (2025) Quantifying loss aversion in cyber adversaries. https://arxiv.org/abs/2508.13240 (c25; qualitative)
- [M] Horton (2023) Large language models as simulated economic agents. https://arxiv.org/abs/2301.07543 (a13, c26)
- [M] Binz et al. (2025) Centaur. https://arxiv.org/abs/2410.20268 (c27)
- [V] Yee and Koh (2026) LLMs as calibrated measurement instruments for behavioural economics. https://arxiv.org/abs/2602.01022 (d13)
- [V] Hashimoto, Takayanagi, Suzuki, Izumi (2025) Agent-based market simulation. https://arxiv.org/abs/2510.12189 (d14)
- [V] Li et al. (2026) Behavioural consistency validation for LLM agents. https://arxiv.org/abs/2602.07023 (d15)
- [V] Marks and Vollberg (2026) The psychophysics of affect in large language models. https://arxiv.org/abs/2610.40985 (d16)
- [M] Hintze, Bisht, Schossau, Hertwig (2025) Nonlinear transformation of probabilities in LLMs. https://doi.org/10.21203/rs.3.rs-5874467/v1 (d17; abstract only)
