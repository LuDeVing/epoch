# Framing and preference construction: deep document

*Scope: wording changes choices ("25% fat" versus "75% lean"). Founding studies, replications, boundary conditions, and every LLM study found that tests or uses it (2020-2026). Built from evidence_a-d.jsonl, claims.jsonl and critique.md in this folder. Ids like a01 and K02 point to those files. Schema parts: G1-G12 guardrails, S0-S9 states, O1-O8 operators (SCHEMA.md). Our hook is S1: neutral restatement and paraphrase stability.*

## 1. What it is

A framing effect is a change in judgment or choice caused by a change in wording that leaves the facts the same. Three kinds are usually separated (Levin, Schneider, Gaeth 1998; a06, a07):

- **Risky-choice framing.** Same outcomes, described as gains ("200 saved") or losses ("400 die"). People pick the sure option in the gain wording and the gamble in the loss wording.
- **Attribute framing.** One feature, described positively or negatively ("75% lean" versus "25% fat"). The rating or evaluation moves.
- **Goal / message framing.** A message stresses what you gain by acting or what you lose by not acting. The evidence is weak and mixed (K23).

Preference construction is the wider idea behind it. People do not read a stored preference from memory. They build one on the spot from the cues in the question, the response mode, and the context (Slovic 1995; a14-a16). Wording, response mode (choose, price, rate), option order and reference point are all inputs to that build. A frame is one cue among them.

Why it matters for our agent: the agent is a language model that reads a prompt and builds an answer. If equivalent wordings give different answers, the answer depends on surface form, not on the problem. S1 (neutral restatement) is meant to cut that dependence. This document asks four questions. How big is the effect in humans? How big is it in current LLMs? Does restating neutrally help? Does it cost accuracy?

Short answer. The human effect is real and medium sized. LLMs show it, but it depends strongly on model class, on the numbers, and on the story around them. Reasoning models are close to invariant on bare two-option choices, but not on choice-versus-price, negation, or story-wrapped items. A model-run rewrite helped a strong model on consistency. Nobody has measured whether it keeps accuracy. Nobody has compared it with a code-side rendering at equal tokens.

## 2. History and theories in depth

**Founding studies: Tversky and Kahneman (1981), Science.** All ten problems were read in full (a01-a05).
- Asian disease. 600 people expected to die. Problem 1 (N=152, gain wording): Program A (200 saved for sure) chosen by 72%; Program B (1/3 chance all 600 saved) by 28%. Problem 2 (N=155, loss wording): Program C (400 die for sure) chosen by 22%; Program D (1/3 chance nobody dies) by 78%. Between-subjects, hypothetical (a01).
- Concurrent decisions. Problem 3 (N=150): sure gain of $240 over 25% chance of $1000 chosen by 84%; for losses, the gamble (75% chance to lose $1000) over a sure loss of $750 chosen by 87%. Problem 4 (N=86): when the combined options are shown in one list, 100% pick the dominant combination B&C and 0% the dominated A&D. When the two choices are made separately, many end up with the dominated pair. A paid version (N=126, one in ten played for real, outcomes scaled down) gave 67% A and 86% D. Pay did not remove the effect (a02).
- Pseudo-certainty. Problem 5 (N=77): sure $30 78% vs 80% chance of $45 22%. Problem 6 (N=85, two-stage game, 25% chance to reach stage 2): sure $30 74%. Problem 7 (N=81): 25% for $30 42% vs 20% for $45 58%. In a within-subject group (N=205), over 75% made compatible choices on problems 5 and 6, and under half were compatible across the equivalent forms. The inconsistency exists inside one person (a03).
- Mental accounting. Problem 8 (N=183): after losing a $10 bill, 88% still buy a $10 ticket. Problem 9 (N=200): after losing the ticket itself, only 46% buy another. Problem 10: 68% drive 20 minutes to save $5 on a $15 calculator, 29% on a $125 calculator (a04).
- Same logic elsewhere: the race-track bettor who has lost $140, cash discount versus credit surcharge, calling a sure loss an insurance premium (a05).

The paper's own limits: single scenarios, hypothetical, effects "large and systematic but not universal". The sure option "200 saved" is incompletely described, which mattered later.

**Theory 1: prospect theory (Kahneman and Tversky 1979; Tversky and Kahneman 1992).** Outcomes are coded as gains or losses against a reference point. The value function is concave for gains, convex for losses, and steeper for losses (alpha = beta = 0.88, lambda = 2.25 in the 1992 fit; a11). Wording sets the reference point, so the same outcome is coded differently. A later meta-analysis of loss aversion: over 600 estimates, mean lambda = 1.955 (Brown et al. 2021; a11, b04). Limits: the theory predicts a reversal of the frame effect at low probabilities, and Kuhberger et al. (1999) found none (b04). Kuhberger and Gradl (2013) found that framing changed the evaluation of the riskless option only (b04). The theory fits curves but does not say where the reference point comes from (a11).

**Theory 2: construction of preference (Slovic, Lichtenstein, Payne, Bettman, Johnson).** Preference is built at the moment of choice with a toolbox of strategies, picked by an effort and accuracy trade-off (a16). Response-mode reversals are the clean evidence:
- Lichtenstein and Slovic (1973, Las Vegas casino). A P-bet (11/12 to win 12 chips) and a $-bet (2/12 to win 79 chips) were chosen about equally often, yet the $-bet got the higher selling price about 88% of the time. Of people who chose the P-bet, 87% priced the $-bet higher (a14).
- Tversky, Slovic and Kahneman (1990). Reversal rate 40 to 50%. Only about 10% of reversal patterns were intransitive. About 90% violated procedure invariance. Overpricing of the low-probability bet explained nearly two thirds (a15).
- Compatibility: a quantity weighs more when the response is in the same units (price). Prominence: the most important attribute dominates choice (a15).
- Highway safety problem: 67% chose the program saving more lives. Irwin et al. (1993): 41% reversed between choice and pricing (a15).
We read these through Slovic's review, not the originals (a16 says so).

**Theory 3: inference from the speaker's choice of frame (McKenzie and Nelson 2003; Sher and McKenzie 2006; Leong et al. 2017).** The frame is information. "Made 40%" versus "missed 60%" leaks what the speaker thinks is typical. Leong et al. (a17, b15, b16): Exp 1 (N=414), a basketball player described by made versus missed free throws, ratings 4.93 vs 3.42, t(136)=4.75, d=0.81. Modelers in the "made" frame estimated the typical player lower: 55% (38/69) vs 28% (17/61) below 40%. Yoked recipients, who saw only the inferred typical value and not the frame, still showed d=0.40. Correlation of inferred typical value with rating r(128) = -.767. Exp 2 (N=364): framing effect b=2.27 at zero basketball knowledge, frame x quiz b=-0.28, p=.036; predicted gap 2.27 at no knowledge versus 0.56 at top knowledge. A medical framing effect in an unrelated domain did not shrink with basketball knowledge. Knowledge shrinks the effect only inside its domain. Single-source (K06).

**Theory 4: others, briefly.** Fuzzy-trace theory (gist coding), venture theory (Hogarth and Einhorn 1990), the Advantage model (Shafir et al. 1993), and motivation accounts. No single theory explains all variants (a11).

**Typology.** Levin et al. (1998) split framing into risky, attribute and goal types and argued they are not one phenomenon. The meta-analytic sizes agree: d 0.44, 0.26 and 0.44 in 2005 (a07).

**Mandel (2014) and the "exactly" argument.** Mandel argued that part of the Asian-disease effect comes from people reading "200 saved" as "at least 200". Making it explicit ("exactly 200") should then remove the effect. Mandel's Study 2 (about 38 per cell): original wording 58% vs 26%; "exactly" 59% vs 43%; the reduction was not significant (p=.293) (b10). A replication of about 98 per cell showed a strong effect with "exactly" (p<.001) (b10, Data Colada). Mandel and Kapler (2018) reconciled it: the difference between the new effect and Mandel's Exp 2 was 0.003, 95% CI [-0.115, 0.127] (b12). We hold Mandel 2014 only through secondary sources (a12, c28; snippet only). Verdict: the sure-option ambiguity may matter at the margin, but disambiguation does not remove the effect (K04).

## 3. Core findings with exact numbers

Status: established = 2+ independent sources opened; single-source; contested = sources disagree. Second-hand means we read it through a review.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Asian disease flips human choice | Gain wording 72% sure option (N=152); loss wording 22% sure option (N=155) | T&K 1981 (a01); Many Labs 1 (d06) | established |
| Many Labs 1 replication | Pooled d=0.60 (95% CI .53 to .67) vs original 1.13 (.89 to 1.37); 62.2% vs 33.5% choose the sure option; chi-square(1)=516.41; N=6,271 analysed, 36 samples; 86% of samples significant in same direction, 14% ns, 0% opposite; Q(35)=37.01, p=.69, I-squared 0. Vignette dropped "Asian" and used local country | Klein et al. 2014 (d05, d06) | established |
| Meta-analytic sizes, 2005 | 51 studies, 151 effect sizes, about 13,500 people: d=0.437 risky, 0.260 attribute, 0.444 goal. Asian disease 47.7% of tasks (d=0.43); 83% student samples | Pinon and Gambara 2005 (a07, b06) | established |
| Meta-analytic sizes, bias-corrected | Kuhberger 1998 (100+ studies, about 30,000 people): d=0.31 uncorrected. Steiger and Kuhberger 2018: d=0.52 corrected, 0.56 for 2016-only studies, range 0.16 to 0.91 | Kuhberger 2023 (a08, b01, b02) | established, second-hand |
| Size in percentage points | 63% sure choice as gain vs 41% as loss (22 points, 40+ studies); DeKay et al. 2022 metastudy over domain, magnitude (x0.1 to x10), 13 probabilities: about 26 points | a09, b02 | established, second-hand |
| Attribute framing is smallest | d=0.26 (multiple options 0.37, single 0.19, within-subject 0.18). Food meta-analysis: 25 studies, 76 effect sizes, d=0.47 overall, attitudes d=0.82, intentions d=0.05 | a07, b05, b07, b08 | established |
| Message framing weak | About d=0.10 (O'Keefe and Jensen); conflicts with goal d=0.444 in 2005 | a10, b03 | contested (K23) |
| Cognitive style, numeracy, age do not explain it | N=506: CRT r=.02, numeracy -.05, AOT .08, NFC .08; age small (18 studies, 3,000+ people) | Mandel and Kapler 2018; Best and Charness 2015 (b03, b11) | established |
| Strict within-person frame consistency is small | Exp 1 N=190: 62% frame-consistent, d=0.20. Exp 2 N=316: 58.2%, d=0.17 (between-groups d=0.34). Option order: 63.1% first vs 56.1% last, one-sided p=.057 | Mandel and Kapler 2018 (b11, b12) | established |
| "Exactly" does not remove the effect | Mandel ~38/cell: 59% vs 43% ns; replication ~98/cell strong, p<.001 | b10, b12 | established |
| Calculator problem replicates | Original 68% vs 29% (N=181, OR=4.96). Many Labs 2: N=7,228, 49% vs 32%, d=0.40 [.35, .45], OR=2.06; tau=0.00, I-squared 6% | Klein et al. 2018 (a13, b13) | established |
| Choice vs price reversal (humans) | Reversal rate 40 to 50%; about 90% break procedure invariance, 10% intransitive; $-bet priced higher about 88% | Slovic 1995 (a14, a15) | established, second-hand |
| Inference route in attribute framing | d=0.81 direct vs 0.40 yoked; inferred value vs rating r=-.767 | Leong et al. 2017 (a17, b15, b16) | single-source |
| Foreign-language and fluency levers | 4 of 5 foreign-language studies not valid; hard-to-read font null in 4 scenarios | Wickelmaier 2015 and others (b28, snippet) | single-source (K22) |
| GPT-3 risky choice (base model) | Risky option chosen: save frame 45.4%, die frame 74.1% (human 28% and 78%). Save prob below .5: 11.3% vs 60.0%; at .5: 21.9% vs 46.9%; above .5: 84.4% vs 93.8% | Jones and Steinhardt 2022 (a20, c01) | established |
| ChatGPT rating framing | Efficacy 5 in all 11 gain runs, 4 in all 11 loss runs; humans 5.2 vs 4.6, t(80)=3.86 | Suri et al. 2023 (a23, b20) | established |
| GPT-3 in PNAS | 3 of 6 effects found, incl. framing; 6 of 12 vignettes correct and human-like | Binz and Schulz 2023 (a22, c05) | established |
| GPT-4 admit vs reject wording | Admission rate 0.375 vs 0.780 (gap -0.405); GPT-3.5 0.685 vs 0.520 (+0.165); Llama-2-13b 0.002 vs 0.062. Sign differs by model | Echterhoff et al. 2024 (a24) | established |
| Contradictions in chat models | Contradictory answers to positive vs negative framing of one scenario: GPT-4o 57%, Gemma 2 74%, Llama 3.1 85% (1,500 experiments, 9 biases) | Saeedi et al. 2024 (a26) | established |
| Framing bias across 20 models | Mean bias score 0.41 (random baseline 0.01), range 0.10 to 0.55; 30,000 cases, 30 biases | Malberg et al. 2025 (a27, b24) | established |
| Story context changes LLM framing | Championship: loss frame 85.6% BLITZ vs gain 0.8% (gain frame 88.8% CONTROL); career transition reversed (loss frame 87.2% safe; apply 87.2% vs 41.6%); business merger minimal; abstract math no effect; 5 models, 25 runs per cell | Payne 2025 (a28, b22, c12, c13) | established, single-author preprint |
| Syntactic fragility | 39,975 decisions, 23 models; mean SVI 0.52 [.42, .63]; 45.2% of model-scenario pairs high, 41.8% moderate, 13.0% robust; US open-source 0.81 vs SOTA US 0.36 vs SOTA China 0.36 | Elkins and Chun 2026 (b17, c21, critique) | established |
| Fragility and temperature | 3-model check: mean SVI 0.67 default vs 0.80 at T=0, Wilcoxon p=0.875, not significant | b18, critique | established (null) |
| Cooperative vs instrumental framing | Option B chosen 4.3% vs 68.8% of 1,640 trials (includes non-compliant); Claude 0.000 vs 0.714; GPT 0.000 vs 0.850; rules differ between prompts | Wang and Zhang 2026 (b19, c11) | single-source, confounded |
| Reasoning models frame-invariant on bare risky choice | 20 LLMs, 360 humans, 3 prospects; wording-check correlation among reasoning models 0.82 to 0.99 (mean 0.91); humans nearer reasoning models | Ge et al. 2026 (d01) | single-source |
| Choice-price reversal in frontier LLMs | 25,920 calls, 4 models, 28 gamble pairs: inconsistency 48.4% (lowest reasoning) to 30.7% (highest); classic direction 38.9% to 25.4%; opposite 9.5% to 5.3%; output 47.3 to 452.4 tokens | Anonymous 2026 blog (b27, d02) | single-source, not peer reviewed |
| Logic-item rewrites | GPT-5.4-mini: base 98.9%, family consistency 60.3%, contrapositive 72.4%, double negation 84.6%, passive 98.7%; passive consistency 94.0% to 99.7% across models | Gu and Chen 2026 (d04) | single-source |
| Cue words pull answers | Neutral prompt, error toward "more" 26% (Sonnet) to 93% (Qwen-3B); "equal" cue up to 94%; GPT-4o and Sonnet 3.7 under 55% except one variant; free CoT brings most errors under 30% | More or Less Wrong 2025 (c17, d03) | established |
| Option position drift | First option chosen 77.1% to 79.0% (chance 36.8%); order bias 30% (GPT-4o-mini), 56% (Llama), 66% (Qwen) | CogBias 2026 (c16) | single-source |
| Format changes alone | Up to 76 accuracy points (LLaMA-2-13B), about 10 on average; GPT-3.5 median 6.4, up to 56 | Sclar et al. 2024 (a29, c24) | single-source |
| Value-tinted rewrites vs paraphrase | Flip rates 39.9% / 36.3% / 47.2% vs paraphrase 18.0% / 21.4% / 21.5% (LLaMA-3.1-8B, Mistral-7B, Qwen2.5-7B); gap over paraphrase +0.213 value-tinted, +0.086 temporal, 0.000 vividness | FRAGILE 2026 (c19, d11) | single-source |
| Affect adds no drift on rule-bound items | Cohen's h=0.003 (human 0.3 to 0.8); 8 models, 16,564 valid responses; drift -0.1% (CI -1.7 to +1.4); evidence-change control 82.2% pass | Chun and Elkins 2026 (d10) | single-source |
| Medical QA framing | Agreement on evidence direction 76.2% same frame vs 72.0% positive vs negative (beta=-0.219, p<.001); multi-turn 78.4% vs 70.7%; 6,614 pairs, 8 LLMs | Yun et al. 2026 (c22, d13) | single-source |
| Loss aversion in LLMs is modest | 102 fits, 11 studies, 32 models: lambda=1.26 (1.06 to 1.46) vs human 1.07, 1.31 or 1.96; symmetric designs 1.15 vs 1.07 human; smaller-loss designs 1.46 vs 2.3 | Tarabeih 2026 (d09) | single-source |
| Single token drives the frame | P(stock B) 0.9744 positive vs 0.0868 negative (GPT-4o); the word "loss" had the largest Shapley pull | CBEval 2024 (c14) | single-source |
| Self-rewrite fix | GPT-4 gap -0.405 to -0.010; GPT-3.5 +0.165 to -0.080 (overshoot); biasing prompt elements cut to 2.7% (GPT-4) | Echterhoff 2024 (a25, c08) | established, consistency only |
| Rephrase and Respond / S2A | GPT-4 10-task mean 64.95% to 89.77%; coin flip 74.55% to 99.09%; S2A opinion-inserted TriviaQA 62.8% to 80.3% (oracle 82.0%) | c25, c26 | established |
| DeFrame | Framing disparity down 92%, bias score down 93% on BBQ (8 models, 3B to 14B); LLaMA-3.1-8b disability: 6.984 to 1.542 (+revision) to 0.514 (+guidelines) to 0.171 | Lim et al. 2026 (c18, d07, d08) | single-source |
| Generic debias prompts unreliable | GPT-4 gap -0.405 baseline, -0.470 awareness, -0.570 counterfactual (worse); CogBias framing +5.8 but hyperbolic discounting -13.4; FRAGILE CoT +13.4 to +26.7 flips in 7B-8B models | c07, c15, d12, d14 | established |

The Many Labs 1 effect (d=0.60) is about half the original (1.13). Original effect sizes are inflated, as usual. Even so, 86% of 36 samples replicate in the same direction and none reverse.

## 4. Mechanisms and models

Each mechanism is stated so it can be turned into code or a test.

**M1. Reference-point coding (prospect theory).**
- Input: a list of options, each with outcomes and probabilities, plus a reference point r.
- Value v(x) = (x-r)^0.88 for x >= r; v(x) = -2.25 * (r-x)^0.88 for x < r. Option value = sum of weight(p) * v(outcome).
- The wording shifts r. "Saved" sets r to the worst case (all 600 die). "Die" sets r to the best case (nobody dies).
- For an engineer: code can restate outcomes in absolute terms (final state, for example "expected survivors out of 600") and drop the relative words. If the option set is rendered as final states, there is no reference point left to shift. This is the best-motivated code-side neutralisation. It is untested in LLMs (gap 4).

**M2. Inference from frame (leakage).**
- A speaker picks the frame that matches their reference point. The listener decodes it: "missed 60%" says the speaker thinks 40% is low (a17).
- Implication: stripping the frame removes information when the frame carries a real signal. A neutral restatement should add the base rate or typical value, not only flip valence (K06 test).
- Implementation: the S1 restatement lists numbers in both polarities (X% yes, Y% no) and, if a typical value exists in the prompt, keeps it.

**M3. Response-mode compatibility.**
- Price responses weight the dollar attribute. Choice weights probability. One preference gives different outputs by mode (a15).
- Implementation: ask for a choice and for a score or price on the same options. Compute disagreement in code. Escalate on disagreement. Frontier LLMs show the reversal at 48.4% down to 30.7% (d02), so the check will fire often at low reasoning settings.

**M4. Adaptive strategy selection (Payne, Bettman, Johnson).**
- The decision maker picks among strategies (weighted additive, elimination, satisficing) by an effort and accuracy trade-off (a16).
- Implementation: before reading the framed text, the agent fixes one rule (expected value, dominance check, constraint check). Dominance checks show low inconsistency in LLMs (d02), so dominance is a reliable anchor. The Payne-Bettman-Johnson primary papers were not opened.

**M5. Token-level and statistics-level pull in LLMs.**
- LLM framing looks less like loss aversion and more like word statistics. The word "loss" had the largest Shapley contribution; P(stock B) 0.9744 vs 0.0868 (c14). Pooled lambda is only 1.26 (d09). Cue words ("more", "equal") pull errors even when the answer is objective (d03).
- Implementation: screen a restatement by token ablation. Delete or swap valence words and see whether the answer moves.

**M6. Information difference versus pure valence.**
- Many LLM "framing" prompts change more than valence: Wang and Zhang rules, Payne story text, FRAGILE narration, Robinson and Burden vignettes (K19).
- Implementation: build frame pairs from one structured form so only valence words differ. Ge et al. did this for three prospects (d01).

**M7. Noise floor.**
- Paraphrase alone flips small open models 18% to 22% (c19, d11). Frontier surface paraphrase on logic items is 94% to 99.7% consistent (d04). Same-frame disagreement in medical QA is about 24% (d13).
- Implementation: always report flip rate minus paraphrase-only flip rate.

**M8. S1 as a pipeline (proposal, untested).**
1. Code extracts options, numbers, entities and the question into a fixed form. Or a model does it and code checks that every number and entity appears in both.
2. Code renders the form in a neutral template: both polarities, fixed or shuffled option order (answer mapped back), no direction words, no negation.
3. The agent answers the original and the neutral version.
4. Code compares. Agree: accept. Disagree: escalate (G1, G2) or report the conflict.
5. Reject the restatement if code finds any number, entity or condition changed.
The model-run self-rewrite variant (a25) skips steps 1 and 2. It worked for GPT-4 and overshot for GPT-3.5.

## 5. What holds up

**Holds up in humans.**
- The Asian-disease effect replicates. Many Labs 1: d=0.60 (CI .53 to .67), 86% of 36 samples significant, none reversed, no heterogeneity (d05, d06). Bias-corrected meta-analysis: 0.52 to 0.56 (a08).
- The 49-country h=0.612 appears in the Kuhberger review, but the critique could not confirm its attribution (Im and Chen / COVIDiSTRESS) in that text. Treat as unconfirmed.
- The calculator problem replicates (d=0.40, N=7,228; a13).
- Response-mode reversals are old and robust (a14, a15).

**Smaller than first reported, or weakened.**
- Original effect size (1.13) was about double the replicated one (0.60).
- Strict within-person consistency effects are small (d 0.17 to 0.20; b11).
- Attribute framing is smallest (d=0.26). In food it moves attitudes (d=0.82) but not intentions (d=0.05) (b05).
- Goal framing: d=0.444 in 2005, "no consistent effect" in the 2023 review (K23, contested).

**Failures and non-levers.**
- "Exactly" disambiguation: Mandel's null came from about 38 per cell. A replication at about 98 per cell and Mandel-Kapler found the effect (b10, b12).
- Cognitive style, numeracy, age: weak or null (b03, b11).
- Foreign language and fluency: failed replications (K22; snippet only).
- Incentives: the paid T&K version still showed the effect (a02).

**Moderators.**
- Task type: d from 0.16 to 0.91 (b02).
- Probability and magnitude: in GPT-3 the effect appears near the classic probability and vanishes where both wordings give the same answer (a20).
- Domain knowledge: shrinks attribute framing only inside the domain (b16).
- Option order: 63.1% vs 56.1% frame-consistent, first versus last (b12).
- Response mode and presentation format (a15, b02).

**Interventions in humans.** Showing the combined options in one list removed the dominance violation entirely (100% pick the dominant pair in Problem 4; a02). That is the best evidence that re-rendering into one integrated form works. Domain expertise helps only inside the domain.

**Interventions in LLMs.**
- Worked: model-run neutral rewrite for GPT-4 (-0.405 to -0.010; a25); Rephrase and Respond (c25); System 2 Attention (c26); DeFrame, a chain of answer, opposite-frame rewrite, guidelines and self-revision (92% disparity cut, small models, fairness items; c18, d07, d08; most of the gain came from self-revision and guidelines); VALIGN, a training-time method (39.9% to 11.9% on LLaMA; c20), out of scope for us; free chain of thought on cue-word drift (c17).
- Did not work or backfired: awareness and counterfactual prompts (GPT-4 gap grew; c07); a single debias prompt (+5.8 framing, -13.4 discounting; c15, d14); CoT, instruction prompt and CAA steering in 7B-8B models (flips up 13 to 27 points; d12); system prompts and anchors (c20); persona prompts (c23); naming a bias in the prompt (b26, d16); resampling and temperature (identical outputs in 11 runs; p=0.875; a23, b18).
- Overshoot: self-rewrite on GPT-3.5 flipped the sign (+0.165 to -0.080; a25).

**Contradictions left open (critique).**
- Goal framing d=.444 (Pinon) versus no effect (Kuhberger).
- Reasoning helps in some families (Grok SVI 0.48 to 0.23) and hurts in some slices (b18). Reasoning removes bare risky-choice framing (d01) but not choice-price reversal (d02), logical negation for GPT-5.4 (d04) or CoT-driven flips in 7B models (d12).
- Self-rewrite fixes GPT-4 and overshoots GPT-3.5.

**Weak spots.** Many LLM framing tests change more than valence. Fixes are scored for consistency, not accuracy. No equal-token cost test exists. Frontier evidence is thin (Elkins, Payne, Malberg, one blog post). Several 2026 papers are preprints. d15, d16 and d18 were read in part only.

## 6. Language models

**Older and base models (2022-2023).**
- GPT-3 reproduces the gain/loss pattern near the classic numbers (45.4% vs 74.1% risky; a20). The effect disappears where the numbers make both wordings agree. Binz and Schulz found framing among three of six effects reproduced (a22).
- ChatGPT (3.5) shows a fully deterministic framing effect on a 7-point rating: 5 in all 11 gain runs, 4 in all 11 loss runs (a23). Resampling cannot reveal the flip. This is the strongest argument for varying the frame, not the seed (K12).
- GPT-4 flips admissions by 40 points between "admit" and "reject" questions (0.375 vs 0.780; a24). The sign differs by model, so there is no fixed direction to correct for.

**Chat models of 2024-2025.**
- Contradictory answers to positive versus negative versions: 57% (GPT-4o), 74% (Gemma 2), 85% (Llama 3.1) (a26). The output is "support or not", looser than a forced choice.
- Average framing-bias score 0.41 across 20 models, range 0.10 to 0.55 (a27).
- Payne's story-wrapped decisions: loss frame 85.6% risky vs gain 0.8% in the championship scenario, reversed in career transition, minimal in the merger, none in abstract math (a28, c12). Narrative content decides which way the frame pushes. In a trade-route scenario ESCALATE was chosen in 1 of over 700 valid decisions (c13).
- Position and cues: first-option choice 77% to 79% (chance 37%; c16). "More/less/equal" cues pull errors up to 94% for small models, under 55% for GPT-4o and Sonnet 3.7 (d03).
- Format alone: up to 76 points for LLaMA-2-13B (a29).

**Frontier and reasoning models (2025-2026).**
- Syntactic fragility audit: 23 models, mean 0.52; US open-source 0.81 vs SOTA US 0.36 and SOTA China 0.36 (b17, critique). Most robust model SVI 0.00 (Gemini 3 Flash); Claude Haiku 4.5 0.71; Sonnet 4.5 0.44 (b18).
- Reasoning on bare two-option choices: nearly invariant to gain/loss wording and option order (20 LLMs; wording-check correlation 0.82 to 0.99; d01). Reasoning pushes toward expected-value choice (d18, partly read).
- Reasoning elsewhere: choice-price inconsistency 48.4% down to 30.7%, not removed. The high setting wrote about 10x more output (d02). Logical-negation consistency is unchanged for GPT-5.4 (86.6% with and without reasoning), while GPT-5.4-mini rose to 85.4% with high reasoning (d04).
- Rule-bound decisions: emotional narrative adds no drift in aligned models (h=0.003; d10). But story context moves cooperation 0.72 (allies) vs 0.44 (enemies) for GPT-4o with the payoff unchanged (d17), and Wang and Zhang found near-total reversals when rules differ (b19). These are information effects, not valence.
- Medical QA: positive versus negative question framing lowers agreement on evidence direction 76.2% to 72.0%, worse in multi-turn (78.4% to 70.7%; d13).
- Loss aversion: pooled lambda 1.26. Models match people when gains and losses are symmetric (1.15 vs 1.07) and fall short when losses are smaller (1.46 vs 2.3) (d09).

**What changed the effect, and by how much.**

| Lever | Effect | Source |
|---|---|---|
| Reasoning mode on, bare risky choice | Near invariance (mean correlation 0.91 across wordings) | d01 |
| Highest reasoning setting, choice vs price | 48.4% to 30.7% inconsistency | d02 |
| Chain of thought, 7B-8B, value-tinted rewrites | Flips up 13.4 to 26.7 points | d12 |
| Free CoT, cue-word drift | Most errors under 30% | c17 |
| Self-rewrite, GPT-4 | Gap -0.405 to -0.010 | a25 |
| Self-rewrite, GPT-3.5 | +0.165 to -0.080 (overshoot) | a25 |
| DeFrame, small models | Disparity -92% (BBQ) | c18 |
| Debias prompt, three mid-size models | Framing +5.8, discounting -13.4 | d14 |
| Awareness prompt, GPT-4 | Gap -0.405 to -0.470 (worse) | c07 |
| Temperature T=0 vs default | SVI 0.67 vs 0.80, p=0.875, ns | b18 |
| System prompt (FRAGILE) | Flips reduced 7.8, 0.9, 10.3 points | c20 |
| Persona ("Economist") | No reliable change | c23 |
| Scale or CoT, product choice | Did not reliably cut context sensitivity | d15 (partly read) |

**Reading across the studies.**
1. Bare wording on a two-option forced choice: reasoning models are mostly fine.
2. Story, differing rules, negation, multi-turn, or a second response mode: not fine, even at the frontier.
3. Small open models: fragile in almost every test, and the usual fixes (CoT, instruction, steering) make some of it worse.
4. The human yardstick is d about 0.5. LLM effects are often far larger (85.6% vs 0.8%) or zero, because LLM outputs are near-deterministic given the text.

## 7. What our agent should take

Status: [E] established, [S] single-source, [C] contested. Schema parts: G guardrail, S state, O operator, memory. Evidence ids in brackets.

### Add now (established)

1. **Vary the frame, not the seed, when testing stability** (G4, S1). [E] Eleven identical ChatGPT runs per frame (a23, b20); fragility unchanged by temperature (b18). Agreement among samples of one wording says nothing about frame sensitivity. Evidence: a23, b18, K12.
2. **Do not add generic "be unbiased" text or persona prompts to fix framing** (G4, G7). [E] Awareness and counterfactual prompts worsened GPT-4 (c07). A debias prompt gave +5.8 on framing and -13.4 on discounting (c15, d14). CoT and instruction prompts raised flips in small models (d12). Persona is unreliable (c23). Adopt a prompt change only if a held-out paraphrase set improves. Evidence: c07, c15, c23, d12, d14, K15.
3. **Treat a changed answer after a meaning-preserving rewrite as a defect signal** (S1, G1). [E] Human effect d about 0.5 (d05, a08). LLM contradictions 57% to 85% (a26). GPT-4 40-point swing (a24). Evidence: K01, K08, K10.
4. **If a model rewrites to neutral form, check the rewrite in code** (S1, G5). [E that rewriting helps consistency; the code check is our design.] GPT-4 fixed, GPT-3.5 overshot (a25). Code confirms every number and entity of the original appears in the restatement. Evidence: a25, c08, c25, c26, K13.
5. **Shuffle option order and strip direction words in code** (S1, G5). [E] First-option choice 77% to 79% against chance 37% (c16). Cue words pull answers up to 94% for small models (d03). Human order effect 63.1% vs 56.1% (b12). Evidence: c16, d03, K16.
6. **Do not rely on disambiguating quantifiers alone** (S1). [E] "Exactly" does not remove the effect (b10, b12). Evidence: K04.
7. **Report flip rate against a paraphrase-only baseline, over several equivalent formats** (G7). [E that format sensitivity is large; the baseline rule is ours.] Format alone moves accuracy up to 76 points, about 10 on average (a29). Paraphrase flips small models 18% to 22% (d11). Evidence: a29, d11, K17, K18.
8. **Do not expect "think harder" to fix framing everywhere** (G11, G12). [C] Reasoning removes bare risky-choice framing (d01) but not choice-price reversal, negation or CoT-driven flips (d02, d04, d12). Measure per item type. Evidence: K11, K05.
9. **No negation, contrapositive or double negation in the restatement template** (S1). [S, kept as a template constraint] Contrapositive 72.4% and double negation 84.6% consistency vs passive 98.7% (d04). Evidence: d04, K25.

### Test first

| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| T1 | Code-side neutral rendering from a structured form beats a model-run rewrite at equal tokens | S1, G5 | [S] untested | M1, M8, K13, K14 |
| T2 | Answer original, neutral and opposite frame; compare in code; escalate on disagreement | S1, G1, G2 | [S] | c18, d07, d08, K14 |
| T3 | S1 keeps accuracy where the framed answer is right | S1, G7 | [S] open gap 1 | a25, d03, d10 |
| T4 | Strip frame only on rule-fixed items; keep it on reference-dependent items | S1 | [S] | d10, d17, K26 |
| T5 | Neutral restatement adds base rate or typical value, not just flipped valence | S1 | [S] | a17, b15, K06 |
| T6 | Choice-versus-score check in code, reasoning on and off | S1, G12 | [S] | d02, K24 |
| T7 | Token-level ablation of valence words as a cheap pre-screen | S1 | [S] | c14, K20 |
| T8 | Per-model flip-rate gate that decides where S1 is worth its tokens | G7, G12 | [S] | b17, c19, d11 |
| T9 | Debias text transfer to held-out item types | G4 | [S] | d14, d16, K29 |
| T10 | Memory: store the neutral form of each problem, not the framed text | memory | [S] idea only | M8 |

Details in UNKNOWNS.md.

## 8. Concrete tests on our bench

Rules for all tests: both arms at equal total tokens (extra restatement calls count as spent tokens, G7). At least 3 models if possible. 100+ items per cell. Items built from one structured form so only wording differs. Every number reported beside the paraphrase-only baseline.

| Test | Item type | Arms (equal tokens) | Metric | Expected effect |
|---|---|---|---|---|
| B1. Flip-rate baseline | Asian-disease-style pairs over 13 probabilities and 4 domains (lives, money, animals, crops); an attribute set ("75% lean"/"25% fat" style) | Plain model on both wordings; plain model with paraphrase-only control | Flip rate minus paraphrase-only flip rate; risky-choice gap in points | Human gap about 22 to 26 points (a09, b02); reasoning-on frontier near 0 (d01); reasoning-off larger |
| B2. Code vs model rewrite | Same pairs plus story-wrapped versions | (a) model rewrite to neutral; (b) code-rendered neutral from a structured form; (c) plain with extra resamples | Flip rate; accuracy on items with a computable best answer | (b) at or below (a) on flip rate with zero number drift; (a) overshoots on weaker models (a25) |
| B3. Accuracy kept | Items where the framed answer is correct, and items where it is wrong | Plain vs S1 restatement vs original+neutral reconciliation | Accuracy and consistency, reported separately | S1 lowers accuracy by no more than 1 point; if more, S1 is not free |
| B4. Reconciliation | Gain/loss items plus yes/no decision items | Original, neutral, opposite answered; code votes; escalate on disagreement | Flip rate after reconciliation; escalation rate; tokens | Lower flip rate than a model-run DeFrame-style chain at same tokens; escalation under 20% |
| B5. Choice vs score | 28 gamble pairs, 8 dominance checks, three formats (as d02) | Reasoning low vs high, each with and without a code check | Inconsistency rate; share caught by the check; dominance violations | Reasoning alone 48.4% to 30.7% (d02); the check catches the rest for one extra call |
| B6. Valence vs information | One structured form per scenario with only valence words differing, versus pairs where facts differ | Plain model on each | Flip rate valence-only vs fact-different | Valence-only small for reasoning models, fact-different large |
| B7. Order and negation | Forced-choice items with shuffled order, negation, direction cues | Plain vs code-normalised (shuffle, strip cues, no negation) | Drift per source: valence, order, negation, cue | Negation drift above valence drift (d04); order drift large in small models (c16) |
| B8. Rule-fixed vs reference-dependent | Rule-bound decisions vs items where the frame signals a reference point | Strip frame vs keep frame | Accuracy per class | Strip neutral or helpful on rule-fixed (d10); strip hurts on reference-dependent (a17) |
| B9. Held-out debias | Framing, discounting and anchoring sets | Debias text tuned on one type, tested on the others vs plain | Change per item type | Gain on the tuned type, none or negative elsewhere (d14) |
| B10. Flip-rate gate | All item types, per model | Measure flip rate over paraphrase and polarity variants once per model | Gate: run S1 only above a threshold | Saves tokens on robust models (SVI 0.00 for Gemini 3 Flash vs 0.81 for open-source; b17, b18) |

## 9. What does not transfer, and why

- **Human loss aversion as a feeling.** LLM pooled lambda is 1.26, not 2 (d09). The pull comes from words like "loss" (c14). Do not model the agent as risk averse. Model it as sensitive to surface tokens.
- **The human d of 0.5 as a target.** LLM outputs are near-deterministic given the text. Effects are very large (85.6% vs 0.8%) or zero (identical ratings in all runs). The human d is only a yardstick (K02).
- **Between-subjects design.** A human sees one wording. The agent can see all wordings. That is the opening for S1. It also means human data on single-wording exposure does not say how a model behaves when it sees both.
- **Individual-difference moderators.** Numeracy, CRT, age and thinking style do not predict framing in humans (b11) and have no analogue in a single model (K05).
- **Foreign-language and fluency effects.** Failed replications in humans (K22). No reason to expect an LLM analogue worth testing.
- **Goal and message framing.** Weak in humans (d about 0.10; K23) and about persuasion, not reasoning. Low priority.
- **Hypothetical one-shot lives-and-money stakes.** Paid T&K versions showed the same effect (a02), so incentives are not the issue. But the agent's tasks are mostly objective (math, code, puzzles). Framing matters most where there is no gold answer. Where there is one, cue words and negation matter more than valence (d03, d04).
- **Training-time fixes.** VALIGN (c20) and activation steering (d12) need weights. We do not train.
- **Fairness-benchmark results (DeFrame on BBQ).** The disparity cut is on bias items, with small models, with model-run steps. It does not show gain/loss choice items or code-side reconciliation (K14).
- **Prompt-context contamination (Codex framing line).** Jones and Steinhardt's code "framing" (a21, c02) is priming by irrelevant text, not equivalent wording. It supports dropping irrelevant context and says nothing about valence.

## 10. Open questions

1. Does a neutral restatement keep accuracy where the framed answer is correct? No study measures consistency and accuracy together on such items (gap 1).
2. How much LLM flipping is pure valence versus information? Ge et al. is close (3 prospects). Nobody has run Asian-disease wording in frontier models from one structured form (gap 2).
3. What is the paraphrase-only flip rate for frontier models on framed forced-choice items? Only logic items (94% to 99.7%) and small open models (18% to 22%) are known (gap 3).
4. Does code-side neutral rendering beat a model-run rewrite at equal tokens? Nothing found (gap 4).
5. Does original / neutral / opposite reconciliation in code work on gain/loss items? DeFrame is model-run, small models, fairness items (gap 5).
6. Do order and negation cause more drift than valence in frontier models, in one study? No head-to-head (gap 7).
7. Does choice-price reversal occur in reasoning models in a peer-reviewed setting, and does a code check remove it? The only source is a blog post with separate stateless calls (gap 8).
8. When does the frame carry real information, so that stripping it hurts? Human evidence only (Leong 2017); no LLM test (gap 9).
9. Do debias prompts hold on held-out domains of the same bias? Leans no, untested (gap 10).
10. Unresolved source details: Payne 2,550 (table) vs 2,150 (c12) decisions; Kuhberger h=0.612 attribution; the Mandel 2014 paper was not opened.
11. Does reasoning reduce framing because it computes expected value, or because it ignores the frame? This matters when the right answer is not the expected-value one (d01, d18).
12. Does multi-turn use amplify framing (78.4% to 70.7%; d13), and does the agent's own earlier wording act as a frame on later steps?

## 11. Sources

[V] = opened and read this run. [M] = snippet or secondary report only.

**Founding and human work**
- [V] Tversky and Kahneman (1981) The framing of decisions and the psychology of choice. https://www.csc2.ncsu.edu/faculty/mpsingh/local/Social/f24/wrap/readings/Tversky+Kahneman-framing-1981.pdf (a01-a05). DOI record https://doi.org/10.1126/science.7455683 [M] (c27)
- [V] Sher and McKenzie (2008) Framing effects (encyclopedia entry). https://pages.ucsd.edu/~mckenzie/SHERMCKENZIEFRAMINGEFFECTSFINAL1.pdf (a06, b09)
- [V] Pinon and Gambara (2005) A meta-analytic review of framing effect. https://www.psicothema.com/pdf/3107.pdf (a07, b06, b07)
- [V] Kuhberger (2023) A systematic review of risky-choice framing effects, EXCLI Journal. https://excli.de/excli/article/view/6169/4721 (a08-a11, b01-b05)
- [V] Dolgopolova, Li, Pirhonen, Roosen (2021) Attribute framing and food attitudes and intentions. https://ageconsearch.umn.edu/record/320229/files/Dolgopolova (b08)
- [V] Slovic (1995) The construction of preference. https://scholarsbank.uoregon.edu/bitstreams/c3007eab-451e-4e14-936a-ea (a14-a16)
- [V] Leong, McKenzie, Sher, Muller-Trede (2017) The role of inference in attribute framing effects. https://pages.ucsd.edu/~mckenzie/Leongetal2017JBDM.pdf (a17, b15, b16)
- [M] McKenzie and Nelson (2003) What a speaker's choice of frame reveals (a18); seen through citations only
- [M] Levin, Schneider, Gaeth (1998) All frames are not created equal. https://digitalcommons.usf.edu/psy_facpub/1886/ (a19)
- [M] Mandel (2014) Do framing effects reveal irrational choice? https://doi.org/10.1037/a0034431 and https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10620856/ (a12, c28)
- [V] Mandel and Kapler (2018) Cognitive style and frame susceptibility in decision-making, Frontiers in Psychology. https://www.frontiersin.org/journals/psychology/ (b11, b12; full URL truncated in evidence file)
- [V] Data Colada (Simonsohn) "Exactly": the most famous framing effect is robust to precise wording. https://datacolada.org/11 (b10)
- [V] Klein et al. (2014) Many Labs 1, manuscript https://osf.io/download/ebmf8/ (d05) and supplement https://osf.io/download/y36m8/ (d06). Journal record https://econtent.hogrefe.com/doi/10.1027/1864-9335/a000178 [M] (b14)
- [V] Klein et al. (2018) Many Labs 2. https://osf.io/download/9654g/ (a13)
- [V] FORRT Replication Atlas, T&K 1981 entry. https://forrt.org/flora-replication-atlas/ (b13)
- [M] Foreign-language effect critiques (Wickelmaier 2015 and others). https://refubium.fu-berlin.de/bitstream/fub188/24622/1/QJEP2 (b28)

**LLM studies**
- [V] Jones and Steinhardt (2022) Capturing failures of LLMs via human cognitive biases. https://arxiv.org/abs/2202.12299 (a20, a21, c01, c02)
- [V] Binz and Schulz (2023) Using cognitive psychology to understand GPT-3. https://arxiv.org/pdf/2206.14576 and https://pmc.ncbi.nlm.nih.gov/articles/9963545/ (a22, c05)
- [V] Suri et al. (2023) Do LLMs show decision heuristics similar to humans? https://arxiv.org/abs/2305.04400 (a23, b20, c03, c04)
- [V] Echterhoff et al. (2024) Cognitive bias in decision-making with LLMs. https://arxiv.org/abs/2403.00811 (a24, a25, c07, c08)
- [V] Saeedi, Goodarzi, Canbaz (2024) Heuristics and biases in AI decision-making. https://arxiv.org/abs/2410.02820 (a26)
- [V] Malberg et al. (2025) A comprehensive evaluation of cognitive biases in LLMs. https://arxiv.org/abs/2410.15413 (a27, b24)
- [V] Macmillan-Scott and Musolesi (2024) (Ir)rationality and cognitive biases in LLMs. https://ar5iv.labs.arxiv.org/html/2402.09193 (c06)
- [V] Itzhak et al. (2024) Instructed to Bias. https://arxiv.org/abs/2308.00225 (c09)
- [V] Lore and Heydari (2024) Strategic behavior of LLMs. https://pmc.ncbi.nlm.nih.gov/articles/PMC11316122/ (c10)
- [V] Payne (2025) An analysis of AI decision under risk. https://arxiv.org/abs/2508.00902 (a28, b22, c12, c13)
- [V] Sclar, Choi, Tsvetkov, Suhr (2024) Quantifying language models' sensitivity to spurious features in prompt design. https://arxiv.org/abs/2310.11324 (a29, b23, c24)
- [V] Shaikh et al. (2024) CBEval. https://arxiv.org/abs/2412.03605 (c14)
- [V] Elkins and Chun (2026) Syntactic framing fragility. https://arxiv.org/abs/2601.09724 (b17, b18, c21)
- [V] Wang and Zhang (2026) Framing effects in independent-agent LLMs. https://arxiv.org/abs/2603.19282 (b19, c11)
- [V] Lior, Naccache, Stanovsky (2026) Comparing the framing effect in humans and LLMs on narrative texts. https://arxiv.org/abs/2502.17091 (b21)
- [V] CogBias (2026) Measuring and mitigating cognitive bias in LLMs. https://arxiv.org/abs/2604.01366 (c15, c16, d14)
- [V] More or Less Wrong (2025) directional bias benchmark. https://arxiv.org/abs/2506.03923 (c17, d03)
- [V] Lim, Kim, Whang (2026) DeFrame. https://arxiv.org/abs/2602.04306 (c18, d07, d08)
- [V] Hwang et al. (2026) FRAGILE. https://arxiv.org/abs/2605.28188 (c19, c20, d11, d12)
- [V] Yun et al. (2026) This treatment works, right? https://arxiv.org/abs/2604.05051 (c22, d13)
- [V] Liu, Shang, Jin (2025) CoBRA. https://arxiv.org/abs/2509.13588 (c23)
- [V] Deng et al. (2023) Rephrase and Respond. https://arxiv.org/abs/2311.04205 (c25)
- [V] Weston and Sukhbaatar (2023) System 2 Attention. https://arxiv.org/abs/2311.11829 (c26)
- [V] Ge, Zhang, Vorobeychik (2026) Mind the (DH) gap. https://arxiv.org/abs/2602.15173 (d01)
- [V, blog, not peer reviewed] LLMs choose the safer gamble yet price the riskier one higher (2026). https://www.lesswrong.com/posts/Cc4vdpTpDv3DZLahs/llms-choos (b27, d02)
- [V] Gu and Chen (2026) Controlled reformulation testing for logical consistency. https://arxiv.org/abs/2607.14528 (d04)
- [V] Tarabeih (2026) Prospect theory in LLMs: a meta-analysis of loss aversion. https://arxiv.org/abs/2610.33103 (d09)
- [V] Chun and Elkins (2026) The paradox of robustness. https://arxiv.org/abs/2601.21439 (d10)
- [V, partial] Sun, Shleifer, Belinkov (2026) Do LLMs choose like humans? https://arxiv.org/abs/2609.22225 (b25, d15)
- [V, partial] Yechiam and Tarabeih (2026) Mimicry without understanding. https://arxiv.org/abs/2608.12339 (b26, d16)
- [V] Robinson and Burden (2025) Framing the game. https://arxiv.org/abs/2503.04840 (d17)
- [V, partial] Tak et al. (2026) Sparks of rationality. https://arxiv.org/abs/2601.22329 (d18)
- [M] Cross-study synthesis by the research agent (Payne, Wang and Zhang, Hwang) (c29)
