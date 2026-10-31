# Risky-choice framing: deep document

*Subfield A15.01. Sources: evidence_a-d.jsonl (ids a01-a31, b01-b26, c01-c27, d01-d15), claims.jsonl (K01-K24), critique.md. Schema parts refer to research_notes/single_agent/SCHEMA.md (G1-G12, S0-S9, O1-O8, section 4b).*

## 1. What it is

Risky-choice framing is a change in choice caused only by how equivalent options are described. The classic case: the same outcomes are worded as lives saved (gain) or lives lost (loss). People pick the sure option in the gain wording and the gamble in the loss wording. The outcomes did not change. Only the words did.

Three kinds of valence framing exist (Levin, Schneider and Gaeth 1998, b26, snippet only). This document is about the first.
- Risky-choice framing: a sure option against a gamble, each worded as gain or loss. This is the Asian disease problem.
- Attribute framing: one item rated under a positive or negative label ("70 of 100 improved" against "30 of 100 did not improve").
- Goal framing: the consequence of acting against the consequence of not acting.

Why it matters for our agent. The broken rule is invariance (also called extensionality): equal descriptions must give equal choices. An agent that reads a task through its wording alone will answer differently when the wording changes. The schema already has S1 UNDERSTAND with input hygiene and "keep the original wording beside it". This subfield says what a second, neutral wording must do and how big the gain could be. It also warns that some tempting fixes (an "ignore the frame" instruction, extra thinking) do little or backfire.

Scope note. Most LLM studies below test related framing (attribute, advice, fairness, admissions), not the exact sure-versus-gamble choice. Each section says which one was used.

## 2. History and theories in depth

### 2.1 Founding experiments (Tversky and Kahneman 1981, a01-a07)

Asian disease problem. A disease is expected to kill 600 people.
- Gain wording, N=152: Program A saves 200 for sure (72% chose it). Program B has a 1/3 chance that 600 are saved and a 2/3 chance that none are saved (28%).
- Loss wording, N=155: Program C, 400 die for sure (22%). Program D, 1/3 chance nobody dies and 2/3 chance 600 die (78%).
- Between subjects, hypothetical. The paper says the reversal also appeared in university faculty and physicians (no group numbers). It calls the effects "large and systematic, although by no means universal" and "not eliminated by monetary incentives".

Other 1981 problems:
- Concurrent decisions, Problem 3 (N=150). Sure gain $240 chosen by 84%. Sure loss $750 chosen by 13% (87% took the gamble). The combination A and D (dominated) was chosen by 73%. The dominant pair B and C was chosen by 3%. Problem 4 (N=86): when the combined options were shown side by side, 100% chose B and C. Showing the integrated form removed the error.
- Paid version (footnote, N=126, outcomes cut by a factor of 50, one in ten paid): 67% took the sure gain, 86% the risky loss. Dominated pair 60%, dominant pair 6%.
- Pseudocertainty (Problems 5-7). Problem 5 (N=77): sure $30, 78%. Problem 6 (N=85, two-stage game with 25% chance to reach stage 2): sure $30 in stage 2, 74%. Problem 7 (N=81, same final odds written directly): 25% chance of $30, 42%; 20% chance of $45, 58%. Problems 6 and 7 have identical final outcomes and probabilities, yet choices flip.
- Mental accounting (riskless, a06). Drive 20 minutes to save $5: 68% if the item costs $15 (N=93), 29% if it costs $125 (N=88). Lost $10 cash, buy a $10 ticket: 88% yes (N=183). Lost the ticket, buy again: 46% yes (N=200).

The authors list four aspects (a07): another frame may flip preference; people are unaware of other frames; people want frame-independent preferences; people do not know how to settle the conflict. In Asian disease no frame is "correct", so the flip cannot be repaired by choosing the right wording. In the concurrent-decision and ticket problems one frame is clearly better once compared.

### 2.2 Prospect theory (Kahneman and Tversky 1979; 1992; a08-a12)

1979 base data (hypothetical money, majority patterns):
- Reflection: sure 3,000 over (4,000, .80): 80% (N=95). With losses, the risky (-4,000, .80) chosen by 92% (N=95).
- Certainty effect (Allais): sure 2,400 over (2,500 .33; 2,400 .66): 82% (N=72). Yet (2,500, .33) over (2,400, .34): 83%. 61% made both modal choices, which violates expected utility.
- Isolation and editing: a two-stage game with a shared .75 chance of nothing gave 78% for the sure 3,000 (N=141), against 65% for (4,000, .20) in the direct form (N=95). Bonus problems: with a 1,000 bonus 84% take the sure 500 (N=70); with a 2,000 bonus 69% take the loss gamble (N=68). Final states are identical.
- Overweighting of small p: 72% prefer a .001 chance of 5,000 to a sure 5 (N=72). 83% prefer a sure loss of 5 to a .001 chance of -5,000 (N=72).

Model. Value V = sum of pi(p_i) times v(x_i). v is defined on changes from a reference point, concave for gains, convex for losses, steeper for losses. pi is a decision weight, not a probability. Two phases: editing, then evaluation. The 1979 version fits no parameters.

1992 cumulative version (a12; read from a calculator page, 1992 PDF not opened): alpha = 0.88, beta = 0.88, lambda = 2.25, gamma = 0.61 (gains), delta = 0.69 (losses). One other source gives delta 0.65 (unresolved).

How prospect theory explains the Asian disease flip: the gain wording puts the reference point at "600 die", so outcomes are gains and the concave v makes the sure option attractive. The loss wording puts the reference at "nobody dies", so outcomes are losses and the convex v makes the gamble attractive.

### 2.3 Later accounts

- Accessibility (Kahneman, Nobel lecture 2002, a14-a18). Wordings make different attributes salient. People passively accept the formulation they are given. "The certainty of saving people is disproportionately attractive, and the certainty of deaths is disproportionately aversive." People who compare both versions "almost always conclude that the same action should be taken in both". Framing is defined as discrepancy between problems that people on reflection consider effectively identical (a15). McNeil, Pauker, Sox and Tversky (1982): surgery versus radiation described as survival or mortality; survival framing raised preference for surgery, "no less pronounced among experienced physicians" (lecture summary only, no figures). Wealth-versus-change: people do not compute final wealth from stated gains and losses (a18, informal data).
- Thoughtfulness (a16). "Thoughtfulness confers no advantage in the absence of a relevant cue." LeBoeuf and Shafir did not replicate the claim by Smith and Levin (1996) that need for cognition reduces between-subject framing. More thoughtful people were more consistent only when they saw both versions.
- Fuzzy-trace theory (Reyna and Brainerd, a19-a21, b08). People keep a verbatim trace (numbers) and a gist trace (some versus none). Gain wording gist: "some saved for sure" against "some saved or none saved". Loss wording gist: "some die" against "some die or none die". Predictions that prospect theory does not make: (i) framing is largest when all numbers are replaced by "some" (90% chose the sure option in gain, 86% the gamble in loss; Reyna and Brainerd 1991); (ii) putting the zero complement of the gamble out of focus removes framing; (iii) when told the choice repeats many times, framing declines (Keren 1991); (iv) framing emerges in early adolescence; autistic people show attenuated framing. All are from a review by the theory's authors.
- Formal fuzzy-trace model (Broniatowski and Reyna 2018, b08): fitted to 88 published gain-loss pairs, predicted 82 (93%); 153 of 170 eligible conditions (90%); Asian disease between-subjects, 27 replications, predicted log-odds differed from reported in 1 (4%); 36 of 39 standard Asian disease experiments matched (92%); within-subjects 2 of 3. Low-PISA countries showed stronger effects (t(30)=2.06, p=.048). Authors are proponents and the model has free parameters. Only the first 100,000 of about 278,000 characters were read.
- Lower-bound reading (Mandel 2014, b25, second-hand). "Save 200" is read as "at least 200", so the frames are not logically equivalent for the reader. In Mandel and Kapler (b04) the framing effect appeared only for lower-bound readers. The Data Colada replication (b03) disputes the "exactly" fix. See section 5.
- Representation framing beyond choice: Simon and Hayes (1976) found Tower of Hanoi isomorphs varied greatly in difficulty. People adopt "the representation that constitutes the most straightforward translation" (a17). Shafir (1993): a richly described custody parent was favoured under both "accept" and "reject" instructions.

### 2.4 Where the debate stands

- The human effect is real and replicable (Many Labs 1, Many Labs 2, a 47-country test).
- Its cause is not settled. The structure of the options (which complements are stated) matters more than the words "gain" and "loss" (Zhou 2021), which favours fuzzy-trace over prospect theory.
- For our agent the cause matters less than the control: change what is stated (both complements, final states) and the effect shrinks.

## 3. Core findings with exact numbers

Status: E = established (three or more independent sources or a large replication); S = single-source; C = contested.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Gain wording favours sure option, loss wording favours gamble | 72% sure (gain, N=152) vs 22% sure (loss, N=155) | T&K 1981 (a01) | E, human |
| Replication is smaller | Many Labs 1: 62.2% vs 33.5% sure; chi2(1)=516.41; N=6,271; d=.60; 36 samples, 6,344 participants; 73 invalid; 0 samples opposite-significant; about 86% same-direction significant (31 of 36 per blog) | Klein 2014 (d01, d02) | E, human |
| Swing size | about 29 points in Many Labs vs about 50 in 1981 (72/22) | d02 | E |
| Many Labs 2 | d=0.40 [0.35, 0.45]; OR 2.06 [1.87, 2.27]; N=7,228 | b05 (secondary page) | E, secondary |
| 47-country test | N=88,181; log-odds B=1.24 (SE .04); d=.69; US d=.75; frame x country chi2(46)=314.51, p<.001 | Rachev 2021 (b06) | E, human |
| Pooled effect, first meta-analysis | d=0.31 (136 studies, 230 effects, about 30,000 people) | Kuhberger 1998 (via d03; paper not opened) | E, second-hand |
| Bias-corrected pooled effect | d=0.52 after p-curve; 2016 studies d=0.56; no strong sign of p-hacking | Steiger and Kuhberger 2018 (d03, abstract only) | E |
| Meta-analysis 1997-2003 | risky d=0.437 (k=87), attribute 0.260, goal 0.444; 51 studies, 151 effects, about 13,500 people; Asian disease 47.7% of tasks (d=0.43); 83.4% students; 88.7% between-subjects | Pinon and Gambara 2005 (b01, d04) | E |
| Between vs within design | between d=0.50 (k=72); within d=0.18 (k=15) | b01 | E |
| Moderators in meta-analysis | more women, larger effect (R2=.191); more options, smaller (beta -0.40, p=.046); product tasks d=0.89 (k=4) | b01 | S |
| Seeing both wordings cuts the effect | d 0.18 within vs 0.50 between (about two thirds) | b01 | E |
| Real money does not remove it | N=126, small stakes: 67% A, 86% D | a04 | S |
| Concurrent choice error | dominated A and D 73% (N=150); integrated side by side 0% (N=86) | a03 | S |
| Pseudocertainty | 74% sure in stage-2 form (N=85) vs 42% in direct form with the same final odds (N=81) | a05 | S |
| Zero outcome removed from the gamble removes the effect | classic task 44.05% risky (gain) vs 64.71% (loss), F(1,1113)=37.55, eta2p=.033; zero removed 57.22% vs 53.63% (F=1.14, p=.286); non-zero removed 30.65% vs 76.46% (F=185.80, eta2p=.143); N=1,119 | Zhou 2021 (b02) | E (replicates Kuhberger and Tanner 2010) |
| Numbers deleted, framing largest | 90% sure (gain) vs 86% gamble (loss) | Reyna and Brainerd 1991 via review (a19) | S |
| Cognitive style does not predict | N=506, r=0.02 to 0.08 with frame-consistent choice, all ns; 75% vs 49% (Exp 1, N=190); 65% vs 52% (Exp 2, N=316) | Mandel and Kapler 2018 (b04) | C (see Peters and Levin) |
| Numeracy as moderator | N=108, frame x numeracy F(1,104)=3.9, p=.05; framing significant for low numeracy (p<.001), not high | Peters and Levin 2008 (b09) | C |
| Age moderates only in gain frame | 18 studies, 3,232 people; gain g=-0.25 [-0.33,-0.18], I2=86%; loss g=-0.02 ns; gain large mortality g=-0.96 | Best and Charness 2015 (b07) | E for the pattern, high heterogeneity |
| Stress and concern raise the effect | stress x frame B=.03, p=.03 (BF 256.7); coronavirus concern B=.05, p<.001; trust in government p=.16 ns | Rachev 2021 (b06) | S |
| Foreign language reduces it only partly | N=132; reduced for a financial-crisis problem, not for Asian disease | Nakamura 2016 (b10) | C |
| Cognitive load raises it | h=0.205 (simple dialogue, ns) vs 0.730 (complex, p=.001); z=3.53; N=1,648 (548 valid in framing study); h values read from a garbled table | Pilli and Nallur 2026 (b19, d11) | S, human |
| Time pressure | reduces (Svenson and Benson 1993) or raises (Guo 2017, Diederich 2018) | b23 (not opened) | C, unverified |
| GPT-3 reproduces the flip near p=1/3 | risky 60.0% (die) vs about 22% (save) at the p=1/3 regime; overall 74.1% vs 45.4% | Jones and Steinhardt 2022 (b11) | E, old model |
| Four 2025 LLMs flip on classic text | reversal rate 27-42%; mean about 33%; 100 runs per frame | Puutio and Do (c07) | S, preprint, labels ambiguous |
| Advice category changes with frame | 32.41% of 6,644 groups [30.48, 34.36]; direct yes/no reversal 0.63%; 98.1% of changes involve "uncertain"; 7 models | FrameBench-HPS (a29, b15, c01, d09) | S, preprint |
| Repeat noise | same-frame disagreement 7.12% [5.56, 8.68] vs cross-frame 34.32% [31.45, 37.09] (3 models) | c02 | S |
| Effect falls with probability | risk shift 0.535 at 20% to 0.109 at 80% | c01 | S |
| Per-model category change | GPT-4o-mini 63.33; GPT-5 33.40; Gemini 2.5 Pro 32.56; GPT-4.1-mini 29.17; Gemini 3 Flash 23.38; Claude Sonnet 4.6 22.81; Qwen3-VL-235B 21.58 | c01 | S |
| Scenario domain sets size and sign | championship loss-minus-gain: o3 +1.640, Claude-4 +1.800, Claude-4-Thinking +1.680, GPT-4o +1.840, Gemini-1.5-Pro +1.400 (max 2); career -0.37 to -0.60; business -0.24 to +0.12 | Payne 2025 (b13, c04, d08) | S |
| Reasoners flip on stories | o3 significant in 4 of 7 scenarios, Claude-4-Thinking in 6 of 7, 25 runs per cell | d08 | S |
| Reasoners ignore frame on explicit gambles | correlation with expected payoff 0.86-1.0 for reasoning models, below 0.5 for conversational; best LLM-human correlation 0.42 | Ge et al. 2026 (b14, d13) | S |
| Canonical rewrite works | category change 34.20% to 6.68% [5.12, 8.51]; paired drop 27.52 pts [24.13, 30.82]; risk shift 0.363 to -0.010; direct reversal 0.35% | FrameBench-HPS (b16, c03, d10) | S |
| "Ignore the frame" instruction works less | 22.83% [19.88, 25.87]; drop 11.37 pts; risk shift 0.154; direct reversals 1.56% (c03) vs 0.52% baseline | b16, c03 | S |
| Symbolic rewrite plus forced EV removes it | o3 200/200 indifferent in both frames; GPT-4o 100% | Payne (c05, d15) | S |
| Model-written neutral rewrite | GPT-4 admit-rate gap -0.405 to -0.010; GPT-3.5 +0.165 to -0.080; residual biased prompts 2.7% (GPT-4), 0% (Llama-2 13B), 1.4% (Llama-2 7B) | Echterhoff 2024 (b17, c14, d07) | E for admissions attribute framing |
| Awareness, contrastive, counterfactual prompts | GPT-4 deltas -0.470, -0.410, -0.570 vs baseline -0.405 (no help) | d07 | S |
| Generic debias prompt | framing accuracy 35.6% to 41.4% (+5.8 pts); other biases worse | CogBias (b18, c15) | S |
| CoT in small models raises flips | LLaMA-3.1-8B 28.6% to 57.1%; instruction 50.7%; CAA steering 34.4%; VALIGN 13.2% | FRAGILE (c18) | S |
| Reasoning-trained 14-70B open models resist more | QwQ-32B .818 vs Qwen2.5-32B .602; R1-Qwen-14B .826 vs Qwen2.5-14B .365; R1-Llama-70B .717 vs Llama-3.3-70B .697 | Knipper 2025 (d12) | S |
| LLM loss aversion is weak | pooled lambda 1.26 [1.06, 1.46] vs human 1.96 (also 1.31, 1.07); curvature 1.01 vs 0.67; weighting 0.81, 0.84; 102 estimates, 11 studies, 32 models | Tarabeih 2026 (a27, b21) | E |
| Parallel agents share a wording's bias | option B 4.3% vs 68.8% of 1,640 responses (valid only 4.5% vs 76.5%); 82 models, 11 families | Wang and Zhang 2026 (a30, d06) | S, not gain-loss |
| Attribute framing in LLMs | mean absolute bias 0.41 over 20 models (range 0.10 to 0.55); ChatGPT rates 5 vs 4 in 11 of 11 trials each | Malberg 2025 (c13); Suri 2023 (b12) | E for existence |
| Multi-turn accumulation | evidence-direction agreement 78.4% vs 70.7% multi-turn; 75.4% vs 72.4% single-turn | Yun 2026 (c17) | S |

## 4. Mechanisms and models

Written so an engineer can build each one.

### 4.1 Prospect-theory value function (human model)

For outcome x relative to a reference point r:
- gain: v(x) = x^alpha; loss: v(x) = -lambda * (-x)^beta.
- Decision weight: w(p) = p^g / (p^g + (1-p)^g)^(1/g), with g = gamma for gains and delta for losses.
- Choice rule: compare sum of w(p_i) * v(x_i) across options.
- Standard values (a12): alpha=beta=0.88, lambda=2.25, gamma=0.61, delta=0.69.

What decides the frame: the reference point r. Gain wording sets r at the worst state, loss wording at the best state. To get a framing effect in a simulation, put r in the wording. To remove it, evaluate all options against final states (see 4.4). Fitted to LLMs (a27, a28): lambda near 1.26, curvature near 1.0, weighting near 0.8. Prospect theory is an unstable fit for some models (Llama-3.1-8B and Qwen2.5-14B fail MAE above 0.20 or pseudo-R2 below 0.10). Do not use it as a model of the agent.

### 4.2 Fuzzy-trace model (gist plus verbatim)

- Encode each option as a gist: "some / none" versions of the outcomes, ordinal only.
- Gain wording: sure option gist = "some saved"; gamble gist = "some saved or none saved". Prefer the option with the better categorical outcome (certain "some").
- Loss wording: sure option gist = "some die"; gamble gist = "some die or none die". Prefer the option whose gist contains the best categorical outcome ("none die").
- Verbatim numbers are used only when the gist does not decide.
- Implementation hook for prompts: the flip depends on which complements are stated. If the zero outcome of the gamble is not written, there is no "none" in the gist and the flip vanishes (Zhou, b02). If the non-zero outcome is not written, the flip about doubles.

### 4.3 Attention and accessibility (Kahneman)

Different wording makes different attributes salient and the reader does not re-derive the other description. For a language model the same mechanism reads: the answer is a function of the tokens in context, and valence words ("save", "die", "loss") shift the output distribution. Evidence: one word swap from "profit 70% of the time" to "loss 30% of the time" moved GPT-4o stock preference from 0.9744 to 0.0868 (CBEval, c16, single toy prompt, token logits). Shapley attribution put the shift on the word "loss".

### 4.4 Canonicalisation: remove the reference point

Procedure, as tested in FrameBench-HPS (d10) and extended with the code step suggested by Payne (d15):
1. Parse the stated probabilities and outcomes with code.
2. Fill in every missing complement (p and 1-p, saved and not saved, die and survive).
3. Express each option as a final-state table: for each outcome, the probability and the final result (for example, "expected survivors: 200 for sure; 600 with p=1/3, 0 with p=2/3").
4. Compute expected values in code.
5. Present the table, not the story, to the choice step.

Tested pieces: (i) a one-sentence rule-based rewrite stating both complements cut category change from 34.20% to 6.68% (near the 7.12% noise floor). It was one added sentence, three models, 32 scenarios. (ii) A symbolic rewrite with forced EV calculation gave 200/200 indifference for o3 (Payne). (iii) A model-written neutral rewrite removed GPT-4's gap. Nobody ran the three side by side at equal tokens (critique gap 1, K24).

### 4.5 Two-wording consistency check (S1 second wording)

Procedure: generate the opposite-valence wording (or the canonical form), answer under each, and compare in code. Agreement is a signal; disagreement means the answer depends on the words and the canonical answer should be used. Human anchor: seeing both wordings cuts the effect by about two thirds (d 0.18 vs 0.50), and thoughtful people are consistent only when both are visible (a16, b01). For LLMs this is untested (K24). Risk: the model may copy the first wording's answer.

### 4.6 Repeat-noise baseline

A frame effect is meaningful only against same-wording repeat disagreement. FrameBench: 7.12% repeat noise against 34.32% cross-frame. Payne used 25 runs per cell and Mann-Whitney tests. The bench must report both.

## 5. What holds up

### 5.1 Replications

- Many Labs 1 (d01, d02): replicated in the predicted direction in about 86% of 36 samples, with none opposite-significant. Effect is about 53% to 67% of the original size (a24, review claim). The primary text gives 62.2%/33.5% sure.
- Many Labs 2 (b05): d=0.40, less than half the original standardised size (secondary page).
- 47 countries (b06): d=.69, but frame x country chi2(46)=314.51, p<.001, so the size varies by country.
- Meta-analyses: d=0.31 (1998), 0.437 (2005), 0.52 (corrected), 0.56 (2016 studies), 0.60 (Many Labs 1). The "small to moderate" reading of K02 is too low. The critique corrects it.
- Correction note: Rachev gives the Many Labs reference as d=.60 in Results and .62 in the Introduction (verification pass).

### 5.2 Failed or partial replications and disputes

- Mandel (2001), Fagley and Miller (1987), Takemura (1992, 1993) are listed as cases where the classic effect did not fully replicate (a26, citation list only).
- "At least 200" reading (b03, b25, c26). Mandel study 2 (about 38 per cell): original wording 58% vs 26%; with "exactly" 59% vs 43% (drop not significant, p=.293). Data Colada replication (about 98 per cell, mTurk): strong effect with "exactly", p<.001. Class data, N=250: 63% vs 25%. Mandel and Kapler's own experiments used "exactly" wording and still found frame-consistent choice 75% vs 49% (b04). Status: contested; one side is a blog.
- Foreign language effect: partial (b10).
- Numeracy: Peters and Levin positive (p=.05, N=108), Mandel and Kapler null. Contested.
- Time pressure: opposite results across papers, not opened.
- Within-subject designs: smaller (d=0.18). Within-subject fuzzy-trace model matched 2 of 3.

### 5.3 What moderates the human effect

- Option structure (which complements are shown) is the strongest moderator (Zhou: eta2p .143 vs ns).
- Domain: lives and large mortality stakes produce larger effects. Age effect g=-0.96 in gain frame with large mortality, nearly zero for large financial stakes.
- Design: between subjects larger than within.
- Alarm, stress, concern raise it (b06). Cognitive load raises it (h .205 to .730).
- Number of options: more options, smaller effect (beta -0.40).
- Low PISA countries: stronger (b08).
- Cognitive style and numeracy: little, contested.

### 5.4 Interventions that worked (humans)

- Showing both versions (about two thirds reduction).
- Showing the integrated combination (Problem 4, 0% dominated).
- Announcing that the choice repeats many times (Keren 1991, via a20).
- Pros-and-cons listing and icon arrays (Almashat 2008; Garcia 2013 with 60 senior police officers). Snippet only (b24), no numbers.

### 5.5 Interventions that did not work (humans)

- Real stakes (small).
- Thoughtfulness or need for cognition, without the other frame (a16).
- A warning alone (Akbulut 2015, thesis, snippet; b24).
- Expertise: physicians showed the effect.

### 5.6 What worked and failed in LLMs (details in section 6)

- Worked: rule-based canonical restatement of both complements (34.20% to 6.68%); symbolic form with forced EV; model-written neutral rewrite (GPT-4 gap -0.405 to -0.010); representation steering in small open models (28.6% to 13.2%, needs weights).
- Did not work: "ignore the frame" instruction (22.83% left, direct reversals rose to 1.56%); awareness, contrastive and counterfactual prompts for GPT-4; generic debias prompt (+5.8 pts on framing and worse on other biases); prompted CoT in 7-8B models (28.6% to 57.1%); few-shot debiasing (pushed models to admit or reject everyone).

## 6. Language models

### 6.1 The effect exists

- GPT-3 (Jones and Steinhardt 2022, b11): at p=1/3 risky choice was 60.0% under die wording and about 22% under save. Across probability ranges, risky was 11.3% (p<0.5), 21.9% (p=0.5), 84.4% (p>0.5) under save and 60.0%, 46.9%, 93.8% under die (74.1% vs 45.4% overall). Human reference: 28% (save) and 78% (die). Prompt: 600 people, "Exactly 400 people will die". (The critique notes that these are averages over probability ranges, not Binz and Schulz numbers.)
- Binz and Schulz (2023, c10): GPT-3 showed 3 of the 6 prospect-theory biases (framing, certainty, overweighting). No per-frame percentage in the text read.
- Talboy and Fuller (2023, d05): qualitative only. Three chatbots, one prompt per frame, two sessions, no counts. Do not cite a rate (K22).
- Puutio and Do (c07): GPT-3.5, GPT-4o, GPT-Mini, DeepSeek; 100 stateless runs per frame; reversal rate 27-42%, mean about 33%; risky share in the table 29-37% (gain) vs 63-71% (loss). Table labels are inconsistent in the preprint.
- Payne 2025 (b13, c04, d08): 5 models, 25 runs per condition, 2,550 decisions, three-option story scenarios. Championship loss-minus-gain +1.40 to +1.84 (max 2); GPT-4o loss-frame BLITZ 85.6% vs 0.8% in gain. Career -0.37 to -0.60 (reverse sign). Business -0.24 to +0.12. Effect size not significantly correlated with EV-calculation attempts. o3 significant in 4 of 7 scenarios; Claude-4-Thinking 6 of 7. Single author; scenario options not exactly equal in all respects.
- FrameBench-HPS (Zhang 2026): 2,880 prompts, 240 scenarios, 4 domains (healthcare, finance, education/career, legal), 4 probability levels, 7 models, temperature 0. Category changed in 32.41%; direct reversal 0.63%. The sensitivity is mostly a move to or from "uncertain", not a flip of the recommendation. A test that counts only direct reversals would miss 98% of it.
- Per-model rates differ between the full set (GPT-4o-mini 63.33%) and the robustness subset (56.5%) because the data differ. Model-specific repeat noise was not reported.
- Echterhoff 2024: admit vs reject wording, 13,465 prompts (abstract; an earlier note said 16,800). GPT-4 admit rate .375 vs .780 (delta -.405, human-opposite direction); GPT-3.5 .685 vs .520 (+.165). Direction is model-dependent.

### 6.2 Related framing in LLMs (not gain-loss risky choice)

- Attribute framing: Malberg 2025 mean absolute bias 0.41 over 20 models; range 0.10 (Llama 3.2 1B) to 0.55 (Llama 3.1 405B); GPT-4o 0.48, GPT-4o mini 0.43, GPT-3.5 Turbo 0.40, Claude 3 Haiku 0.44, Gemini 1.5 Pro 0.38, Mistral Large 0.47, Qwen2.5 72B 0.37. Random baseline 0.01. Larger models are not immune. Suri 2023: ChatGPT rating 5 vs 4 on all 11 trials each, humans 5.2 vs 4.6 (N=82, t(80)=3.86).
- WildFrame (c12): eleven LLMs respond to positive and negative reframing of 1,000 real sentences like humans (r at least 0.52); GPT models least human-like.
- Question stance in medical QA (Yun 2026, c17): evidence-direction agreement 76.2% (same stance) vs 72.0% (opposite), beta -0.219, z=-14.72; multi-turn 78.4% vs 70.7%. A few points, not a reversal.
- FramingQA (c25): strict all-variant pass rate 0.0% for every model in one setting; bias effects 1.4% to 35.2%; robot success 66% neutral vs 59% under incorrect-bias framing.
- Fairness: DeFrame (a31, c19): alternative framing then revision cut framing disparity 92% and bias score 93% on BBQ (8 LLMs, author claim).
- Agent loop: Szeider 2026 (c24): four frontier models changed self-reports when a tool was described in relief-framed words, although nothing changed. An explicit "ignore the framing" instruction did not stop it. The tool description was the main channel.
- Code analogy (c22): "framing" there means irrelevant preceding context. Codex accuracy fell from 32.9% to 2.4-10.6%. Same name, different mechanism; not used here.

### 6.3 What changed the effect, and by how much

| Change | Size | Where |
|---|---|---|
| Reasoning-class model, explicit two-option money prospects | correlation with expected payoff 0.86-1.0 vs below 0.5 for conversational; humans less frame-affected than conversational models | Ge 2026 (d13) |
| Reasoning-class model, story scenarios | still significant in 4 of 7 (o3) and 6 of 7 (Claude-4-Thinking) | Payne (d08) |
| Reasoning-trained open models, attribute templates | .818 vs .602; .826 vs .365; .717 vs .697; Phi-3.5-mini .262 | Knipper (d12) |
| Prompted CoT, 7-8B | 28.6% to 57.1% flips; Mistral-7B base 21.9% to 61.3% with CoT | FRAGILE (c18) |
| Instruction "be frame-robust" | 34.20% to 22.83% | FrameBench (c03) |
| Rule-based canonical sentence | 34.20% to 6.68% | FrameBench (d10) |
| Symbolic plus EV | to 0 (100% indifference) | Payne (d15) |
| Self-written neutral rewrite | -0.405 to -0.010 (GPT-4) | Echterhoff (d07) |
| More detailed prompts | small help for framing (TELeR levels L1 to L5, resistance .473, .509, .56...) | Knipper (d12) |
| Explanations requested | change decisions for all models, more for conversational ones | Ge (d14) |
| Complex dialogue before the choice | role-playing LLM effect rose 1.770 to 2.447 (z 4.53) and 1.252 to 2.299 (z 7.04); third prompt 0.690 to 0.810 (ns); 3 to 9 times human size | Pilli and Nallur (d11) |
| Verbal probability markers in place of numbers | change choices and fitted parameters | Wang 2025 (a28) |

### 6.4 The reconciling reading (K11)

Reasoning models look frame-invariant on explicit prospects because they can compute expected value from the numbers. On story scenarios the numbers are not given in a computable form, so they still follow the frame. This reading is plausible but no single study varies format with the model held fixed.

### 6.5 Caveats on the LLM literature

- Nearly all LLM framing studies are preprints, many from 2026, several single-author.
- The classic Asian disease text is probably in the training data. Only Suri et al. avoided it deliberately.
- Several studies test attribute framing, fairness or admissions, not the gain-loss choice.
- No study measured a full agent loop or a mitigation at equal tokens.
- Tarabeih shows that fitted human-style parameters do not describe LLMs well. The LLM is not a small human.

## 7. What our agent should take

Status: [E] established, [S] single-source, [C] contested. Evidence ids as in the files (claim ids in brackets).

### Add now (established)

| Item | Schema part | Status | Evidence |
|---|---|---|---|
| Treat wording as an input variable that can change the answer. Models flip with gain/loss wording on old and new models, across domains and sizes. Supports the existing S1 rule "keep original wording beside it". | G / S1 | [E] | b11, c07, b13, d08, d09, a29 [K09, K21] |
| Do not rely on a generic "ignore the framing / be unbiased" instruction as the fix. It helped little or none (22.83% left; awareness no help for GPT-4; +5.8 pts; can raise direct reversals; failed in an agent-loop test). | G1 / S1 | [E] | b16, c03, d07, c15, c24 [K13] |
| Do not use prompted CoT as a framing remedy for small models. It doubled flips in 7-8B models. (In line with G11.) | G11 | [E] for small models | c18 [K13] |
| Measure frame sensitivity as cross-wording disagreement above same-wording repeat noise, not by direct reversals alone. | S0 / bench | [E] as measurement practice | c02, b15 [K21] |
| Do not treat parallel samples of one wording as independent evidence about frame robustness. Same wording shares its bias. (Matches G4.) | G4 | [E] in direction, single source for size | a30, d06 [K17] |
| Do not model the agent as a human value function or as a rational agent: lambda 1.26 vs 1.96, weights near human. | none | [E] | a27, b21 [K15] |

These items change nothing in SCHEMA.md beyond what is already there. They are checks on proposals.

### Test first (not yet added)

| Item | Schema part | Status | Evidence |
|---|---|---|---|
| Code-run canonical restatement: state both complements, final-state table, EV computed in code, before S2. | S1 input hygiene | [S] | a29, b16, d10, d15 [K12, K20] |
| Model-written neutral rewrite with a code check that all numbers were preserved. | S1 second wording | [E] on admissions framing in GPT-4; [S] for risky choice | b17, d07, a31 [K14] |
| Second wording within one context (both frames shown) and compare to the first answer. Humans: about two thirds reduction. | S1 second wording | [E] human; untested for LLMs | b01, a16, a03 [K03, K24] |
| Different canonical wordings for different attempts, then vote in code, against same-wording sampling. | S3 / S7 voting | [S] | a30, d06 [K17, K24] |
| Re-derive the question neutrally at each loop step; do not carry original wording through the loop. | S1 / memory | [C] | c17, c24, c22 [K16] |
| Strip alarm, stakes and valence words in the rewrite (lives, deaths, urgency). | S1 | [E] human (strong moderators); untested for LLMs | b06, b07, b19 [K08] |
| Thinking on/off and short/long reasoning budget on a fixed frontier model. | G11 / S0 mode | [C] | d08, d12, d13, c18 [K11, K23] |
| Context padding with demanding text, own-judgment version. | G | [C] | b19, d11 [K18] |
| Token budget vs frame sensitivity. | S0 mode | untested | b23 [K19] |
| Missing-complement manipulation: remove the zero outcome of the risky option. | S1 canonical restatement | [E] human; no LLM data | b02 [K05] |

## 8. Concrete tests on our bench

All arms at equal total tokens (count the added rewrite or code step against the arm). Report flip rate = cross-frame disagreement, and the same-wording repeat disagreement alongside. At least 20 repeats per cell. Use at least four domains and some novel wordings to avoid memorised text.

| Test | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 Canonicalisation | Asian disease, a two-stage pseudocertainty item, two story items in each of four domains | plain; instruction only; self-written neutral rewrite; one-sentence canonical; code-run final-state table | flip rate gain vs loss minus repeat noise | One-sentence canonical near noise (about 7%); instruction about 23% from about 34%; code table at or below canonical. If self-rewrite equals the others at lower cost, prefer it. |
| T2 Both wordings in one context | same items | single wording; both wordings shown, one answer asked | flip rate across frames; whether the answer follows the first wording | Human anchor: about two thirds cut. An LLM may just copy the first frame; check with order swap. |
| T3 Thinking on/off, budget | same items, explicit-prospect and story formats | thinking off; thinking on; low and high budget | flip rate by format | Explicit prospects near zero; story format shows residual (Payne: 4 of 7 and 6 of 7 scenarios). |
| T4 Voting | same items | 5 samples of one wording; 5 samples, each with a different canonical wording | flip rate of the vote; agreement with canonical answer | Different wordings should cut the shared-bias swing (Wang and Zhang, 4.3% to 68.8%). |
| T5 Zero-outcome removal | classic-structure item | zero stated; zero removed; non-zero removed | flip rate | Humans: removed zero erases the effect (57.22 vs 53.63); removed non-zero doubles it. Check whether the model matches. |
| T6 Valence stripping | alarm-loaded story items | original; neutral rewrite with alarm and stakes words removed | flip rate | Smaller flip if alarm and mortality language drive it. |
| T7 Loop carry | multi-step task with one framed premise | carry original wording; re-derive neutral question each step | final-answer drift | Yun: multi-turn gap 70.7% vs 78.4%; expect less drift with re-derivation. |
| T8 Context padding | same items | none; 5k tokens of demanding text; 20k | flip rate | Human load effect h .205 to .730; role-play LLM rose in 2 of 3. Own-judgment effect unknown. |
| T9 Instruction-only control | same items | plain; "ignore the frame"; awareness | flip rate | Expect small reduction and possible rise in direct reversals. |
| T10 Order | two-option items | sure first vs gamble first | flip rate | Ge: conversational models are order-sensitive; reasoning models are not. Separates frame from order. |

Include items with more than two options (as Payne did) and forced-choice items, because FrameBench shows the sensitivity mostly moves into "uncertain".

## 9. What does not transfer, and why

- Human loss-aversion values (lambda 2.25) and curvature. LLMs fitted at lambda 1.26, curvature about 1.0 (a27). Prospect-theory parameters do not fit every model (Llama-3.1-8B, Qwen2.5-14B fail).
- Individual-difference protection (numeracy, need for cognition). Not reliable even in humans (r 0.02 to 0.08). No reason to add a "be numerate" instruction.
- Expertise. Physicians and faculty showed the effect; it cannot be assumed that a strong model removes it. Reasoning models are still affected on stories.
- Real money and stakes. Human stakes do not matter; the model has no stakes. Telling the model "this is real" is untested (K07).
- Foreign-language effect. Partial in humans; not a candidate lever.
- Age, gender, stress and trust moderators. They describe people, not agents.
- Repeated-choice announcement (Keren 1991) as a prompt: untested for LLMs and risks sounding like an instruction, which was weak.
- Hanoi isomorphs and custody framing: framing of problem representation. These belong to S2/O6 (change representation) rather than to valence framing.
- Persona prediction results (Pilli and Nallur): the LLM was predicting a human, with effects 3 to 9 times human size. They do not describe the agent's own decisions.
- Code "framing" (Jones and Steinhardt 2022, c22): different mechanism.
- Fairness and BBQ results (DeFrame): fairness framing; the 92% figure is the authors' average on a different task.
- Old-model numbers (GPT-3, GPT-3.5): direction is model-dependent (GPT-4 flipped opposite to GPT-3.5).

## 10. Open questions

1. Does a code-run canonical table beat a self-written neutral rewrite and an instruction-only prompt at equal tokens on a current reasoning model (K24, gap 1)?
2. Does the flip rate of a reasoning-class model on story problems exceed its own repeat noise across at least four domains? Partly closed (FrameBench pooled 7.12% noise vs 33.40% for GPT-5) but model-specific noise and per-domain results are missing.
3. Does showing both wordings in one context cut LLM flips, or does the model copy the first wording?
4. Does context length or mental-demand padding amplify the frame in the model's own judgment?
5. Does token budget change frame sensitivity? Human time-pressure results disagree.
6. Do votes with different canonical wordings beat same-wording sampling at equal tokens?
7. Does removing the zero outcome of the risky option remove the flip in LLMs?
8. Does CoT raise or lower flips in frontier models, same weights, thinking on/off?
9. Why is GPT-4's admissions flip opposite to GPT-3.5's?
10. Primary numbers still missing: Kuhberger 1998 (abstract unreadable), Steiger and Kuhberger 2018 (abstract only), Zhou 2021 (could not be re-opened in the gap pass), McNeil 1982, Keysar 2012, Many Labs 2 primary text.
11. Is delta 0.69 or 0.65 in the 1992 weighting for losses?
12. Does the canonicalisation result hold beyond single stated probabilities (multi-stage items, pseudocertainty)?
13. Do the preprint results survive peer review and independent re-run?

## 11. Sources

[V] = opened and read this session. [M] = snippet or secondary page only. Evidence ids in brackets.

1. [V] Tversky and Kahneman (1981) The framing of decisions and the psychology of choice. Science 211:453-458. https://www.science.org/doi/10.1126/science.7455683 [a01-a07]
2. [V] Kahneman and Tversky (1979) Prospect theory. Econometrica. https://www.jstor.org/stable/1914185 [a08-a11]
3. [V] Tversky and Kahneman (1992) Cumulative prospect theory, parameter values via calculator page. https://personal.eur.nl/wakker/miscella/calculate.cpt.kobb/index.htm [a12] (PDF not opened)
4. [V] Wikipedia: Framing effect (psychology). https://en.wikipedia.org/wiki/Framing_effect_(psychology) [a13]
5. [V] Kahneman (2003) Maps of bounded rationality, Nobel lecture. https://www.nobelprize.org/uploads/2018/06/kahnemann-lecture.pdf [a14-a18]
6. [V] Reyna and Brainerd (2011) Dual processes in decision making and developmental neuroscience. https://pmc.ncbi.nlm.nih.gov/articles/PMC3214669 [a19-a21]
7. [V] Pinon and Gambara (2005) A meta-analytic review of framing effect. https://www.psicothema.com/pdf/3107.pdf [a22, b01, d04]
8. [M] Kuhberger (1998) The influence of framing on risky decisions: a meta-analysis. https://ideas.repec.org/a/eee/jobhdp/v75y1998i1p23-55.html and https://doi.org/10.1006/obhd.1998.2781 [a23, b22]
9. [V] Klein et al. (2014) Many Labs replication project, manuscript and web supplement. https://osf.io/wx7ck/ [d01, d02]; a24 was a snippet from the same project.
10. [V] FORRT replication atlas for Many Labs 1 and 2. https://forrt.org/flora-replication-atlas/doi/10.1126/science.7455683/ [b05] (secondary summary page)
11. [M] Zhou, Liu, Liao and Li (2021) JDM summary page. https://dlab.sauder.ubc.ca/sjdm/journal/20/200630a/jdm200630a.html [a25]
12. [V] Zhou et al. (2021) Risky choice framing with various problem descriptions. https://doi.org/10.1017/S1930297500008615 [b02]
13. [M] Mandel (2001) Gain-loss framing and choice. https://ideas.repec.org/a/eee/jobhdp/v85y2001i1p56-76.html [a26]
14. [V] Tarabeih (2026) Prospect theory in LLMs: a meta-analysis. https://arxiv.org/abs/2610.33103 [a27, b21]
15. [V] Wang et al. (2025) Rethinking prospect theory for LLMs. https://arxiv.org/abs/2508.08992 [a28]
16. [V] Zhang et al. (2026) FrameBench-HPS. https://arxiv.org/abs/2610.29294 and https://arxiv.org/pdf/2610.29294 [a29, b15, b16, c01-c03, d09, d10]
17. [V] Wang and Zhang (2026) Framing effects in independent-agent LLMs. https://arxiv.org/abs/2603.19282 and https://arxiv.org/pdf/2603.19282 [a30, b20, c20, d06]
18. [V] Lim, Kim and Whang (2026) DeFrame. https://arxiv.org/abs/2602.04306 [a31, c19]
19. [V] Simmons, Nelson and Simonsohn (2015) Data Colada [11]. https://datacolada.org/11 [b03]
20. [V] Mandel and Kapler (2018) Cognitive style and frame susceptibility. https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2018.01461/full [b04]
21. [V] Rachev et al. (2021) Replicating the Disease framing problem during the 2020 COVID-19 pandemic. https://pmc.ncbi.nlm.nih.gov/articles/PMC8432807 [b06]
22. [V] Best and Charness (2015) Age differences in the effect of framing on risky choice. https://pmc.ncbi.nlm.nih.gov/articles/PMC4556535 [b07]
23. [V] Broniatowski and Reyna (2018) A formal model of fuzzy-trace theory. https://pmc.ncbi.nlm.nih.gov/articles/PMC6176745/ [b08] (first 100,000 characters)
24. [V] Peters and Levin (2008) Dissecting the risky-choice framing effect: numeracy. https://doi.org/10.1017/S1930297500000012 [b09]
25. [V] Nakamura (2016) Foreign language effect. https://escholarship.org/uc/item/61m0k50b [b10]
26. [V] Jones and Steinhardt (2022) Capturing failures of LLMs via human cognitive biases. https://arxiv.org/pdf/2202.12299 [b11, c22]
27. [V] Suri et al. (2023) Do LLMs show decision heuristics similar to humans? https://arxiv.org/pdf/2305.04400 [b12, c11]
28. [V] Payne (2025) An analysis of AI decision under risk. https://arxiv.org/pdf/2508.00902 [b13, c04, c05, c26, d08, d15]
29. [V] Ge, Zhang and Vorobeychik (2026) Mind the (DH) gap. https://arxiv.org/pdf/2602.15173 [b14, c06, d13, d14]
30. [V] Echterhoff et al. (2024) Cognitive bias in decision-making with LLMs. https://arxiv.org/pdf/2403.00811v3 [b17, c14, d07]
31. [V] Huang et al. (2026) CogBias. https://arxiv.org/pdf/2604.01366 [b18, c15]
32. [V] Pilli and Nallur (2026) Predicting biased human decision-making with LLMs. https://arxiv.org/pdf/2601.11049 [b19, c21, d11]
33. [M] Diederich, Wyszynski and Ritov (2018) Moderators of framing effects. https://doi.org/10.1017/S1930297500006896 [b23]
34. [M] Thomas and Millar (2012); Almashat et al. (2008); Garcia (2013); Akbulut (2015), debiasing, via https://pmc.ncbi.nlm.nih.gov/articles/PMC6176745/ [b24]
35. [M] Mandel (2014) Do framing effects reveal irrational choice? https://www.researchgate.net/profile/David-Mandel-4/publication/256117998_Do_Framing_Effects_Reveal_Irrational_Choice [b25]
36. [M] Levin, Schneider and Gaeth (1998) All frames are not created equal. https://econpapers.repec.org/RePEc:eee:jobhdp:v:76:y:1998:i:2:p:149-188 [b26]
37. [V] Puutio and Do (2025/2026) Can we trust the machine? https://www.researchsquare.com/article/rs-7313765/v1.pdf [c07]
38. [V] Thorstad (2023) Cognitive bias in LLMs. https://arxiv.org/abs/2311.10932 [c08]
39. [M] Talboy and Fuller (2023) via Scholar search [c09]; [V] arXiv version https://arxiv.org/abs/2304.01358 [d05]
40. [V] Binz and Schulz (2023) Using cognitive psychology to understand GPT-3. https://arxiv.org/abs/2206.14576 [c10]
41. [V] Lior, Naccache and Stanovsky (2025) WildFrame. https://arxiv.org/abs/2502.17091 [c12]
42. [V] Malberg et al. (2025) Comprehensive evaluation of cognitive biases in LLMs. https://arxiv.org/abs/2410.15413 [c13]
43. [V] Shaikh et al. (2024) CBEval. https://arxiv.org/abs/2412.03605 [c16]
44. [V] Yun et al. (2026) This treatment works, right? https://arxiv.org/abs/2604.05051 [c17]
45. [V] Hwang et al. (2026) FRAGILE and VALIGN. https://arxiv.org/abs/2605.28188 [c18]
46. [V] Horton (2023) Homo Silicus (partial read). https://arxiv.org/abs/2301.07543 [c23]
47. [V] Szeider (2026) LLM self-explanations fail semantic invariance (abstract and intro). https://arxiv.org/abs/2603.01254 [c24]
48. [V] Kim et al. (2026) FramingQA (abstract, intro, some results). https://arxiv.org/abs/2609.07448 [c25]
49. [V] Steiger and Kuhberger (2018) A meta-analytic re-appraisal of the framing effect (abstract only). https://doi.org/10.1027/2151-2604/a000321 [d03]
50. [V] Knipper et al. (2025) The bias is in the details. https://arxiv.org/pdf/2509.22856 [d12]
51. Not found: no pre-2020 AI system built on gain-loss framing surfaced in the searches (c27, absence is not proof).
