# Valuation and common currency: deep document

*Subfield B02.01. Source files in this folder: evidence_a-d.jsonl (a01-a29, b01-b25, c01-c30, d01-d20), claims.jsonl (K01-K33), critique.md. Status tags: [E] established, [S] single-source, [C] contested. Background only for the schema, but several LLM results give testable checks.*

## 1. What it is

The idea: the brain turns very different options (money, food, a trinket, a delayed reward, a risky bet) into one subjective value on a shared scale. Then it picks the option with the highest value. The shared scale is called a "common currency".

The main brain sites are the ventromedial prefrontal cortex (vmPFC), the orbitofrontal cortex (OFC) and the ventral striatum. In monkeys, single OFC neurons also code offer value and chosen value.

Why an engineer should care: a language-model agent that compares options must also put unlike things on one scale. Two questions follow.

1. Do LLMs hold a coherent, stable scale of value? The LLM papers test this through behaviour (transitivity, budget consistency, expected utility), and one paper probes hidden states.
2. Should an agent compute an explicit score per option, then rank? Or choose directly? The human evidence cannot settle this. The LLM evidence is thin (one paper, K22).

Scope note. The named key works in the subfield table are Montague, King-Casas and Cohen 2006 and Sharot and Dolan 2011. Montague 2006 is a review with no effect sizes (d04, abstract only). Sharot and Dolan 2011 is about optimism in belief updating, not value as such. We give the human numbers (d01, from the 2011 paper by Sharot, Korn and Dolan) and the single LLM test (Schubert 2024).

## 2. History and theories in depth

**Model-based fMRI (2000s).** Montague, King-Casas and Cohen (2006) reviewed how reward-learning models (prediction-error type) are fitted to behaviour and then used to find regressors in the scanner (d04, a20; abstract only). Rangel, Camerer and Montague (2008, a15) gave a five-process frame: represent the problem, value the actions, choose, evaluate the outcome, learn. They named three valuation systems: Pavlovian, habitual and goal-directed. The goal-directed system updates at once when an outcome loses value (a fed animal). The habit system does not.

**Single-neuron value, monkeys.** Padoa-Schioppa and Assad (2006, a11, b06) recorded 931 OFC neurons while monkeys chose between juices of different amounts. 505 (54%) varied with offer type. Under 5% depended on spatial layout or motor output. Three variables (offer value, chosen value, taste) explained 1085 of 1379 responses (79%, mean R2 0.63). Padoa-Schioppa (2011, a12) built this into the "good-based" model. Values of goods are computed independently, so choices are transitive. Values are computed at choice time. Supporting lesion work: OFC patients broke transitivity in food judgments more than controls (Fellows and Farah 2007, cited in a12).

**Human subjective value tracking.** Kable and Glimcher (2007, a09, a10, b05): 10 scanned people chose $20 now vs a larger delayed reward. Ventral striatum, medial PFC and posterior cingulate followed each person's own discounted value. Chib et al. (2009, a07, a08): vmPFC tracked willingness to pay (WTP) for money, snacks and trinkets in the same spot.

**Common currency synthesis.** Levy and Glimcher (2012, a05, a06) reviewed 13 fMRI studies. A part of vmPFC/OFC tracks subjective value across reward types. Only two studies met their strict "equal-value" test (cross-good exchange rates predicting neural scale): Smith et al. 2010 (money vs faces) and the authors' own study (money vs food).

**Meta-analyses.** Bartra, McGuire and Kable (2013, a01-a04) with 206 studies. Clithero and Rangel (2014, a16, b03, b04) with 81 studies and 104 contrasts. They agree on the core network: vmPFC, ventral striatum, posterior cingulate.

**Relative value.** Louie, Grattan and Glimcher (2011, a13): monkey LIP neurons code value relative to other options (divisive normalisation). Hunt et al. (2012, a14): an attractor network comparing two values matched human MEG in parietal cortex.

**The critique.** Hayden and Niv (2021, a21, a22, b07): a cardinal, per-option value need not be computed. Choosing between an orange and a car needs no value. Many neural "value" correlates may come from heuristics or direct policy learning (Bennett, Niv and Langdon 2021, b23, snippet only). A 2026 reply (b08) defends the common-currency view, with no new data. The neural data cannot separate the two accounts, because value correlates can arise from either. Status: [C].

**Reliability concern.** Botvinik-Nezer et al. (2020, b10): 70 teams analysed the same dataset (108 people). Only one hypothesis got agreement (84.3%). The gain effects in vmPFC and ventral striatum were significant for only 21.4% to 37.1% of teams.

**Beliefs shape value.** Plassmann et al. (2008, a18): a wine labelled dearer raised pleasantness (r = 0.59) and medial OFC activity.

**Optimism and updating.** Sharot, Korn and Dolan (2011, d01): people update more after good news than bad. Disputed by Shah et al. (2016, d03; abstract only) as a statistical artefact, defended by Garrett and Sharot (2017, d02).

**Move into AI (2023-2026).** Behavioural economics tools were applied to LLMs. These cover budget tasks (GARP, CCEI), prospect theory, time discounting, decoys, and utility fits (Chen 2023; Ross 2024; Mazeika 2025; Tarabeih 2026). Section 6 covers them.

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| vmPFC and ventral striatum track value mostly positively (human fMRI) | 206 studies; 200 positive, 77 negative, 71 both; 12981-voxel positive cluster p=0.0002 | Bartra 2013 (a01, a02) | [E] |
| Striatum and vmPFC counts favour positive effects | striatum 145/200 (72.5%) vs 22/77 (28.6%); vmPFC 112/200 (56.0%) vs 12/77 (15.6%); p<0.001 | Bartra 2013 (a02) | [E] |
| Insula, dMPFC, dorsal striatum, thalamus have both signs (salience) | mixed-sign pattern in the same 206-study corpus | Bartra 2013 (a01, b02) | [S] |
| Value is denser at decision than at outcome in vmPFC | 27 decision vs 140 outcome studies; decision>receipt 1580 voxels, p=0.0058, peak pseudo-t 5.29 | Bartra 2013 (a03) | [E] |
| Money and primary rewards share vmPFC and ventral striatum | 82 money, 33 primary studies; five-way conjunction: ventral striatum 500 voxels, vmPFC 449 | Bartra 2013 (a04) | [E] |
| Posterior (food) to anterior (money) gradient in vmPFC | food>money peak (-8,27,-13); money>food peak (-5,60,-9); both p<0.005; 81 studies (money 50, food 24, other 24) | Clithero and Rangel 2014 (a16, b04) | [E] |
| Primary vs secondary reward differences | 87 studies, 1452 subjects: money-specific in anterior OFC; food and erotic stronger in anterior insula (not opened) | Sescousse 2013 (a17) | [M] |
| Same vmPFC spot tracks WTP for money, snacks, trinkets | N=19: money Z=3.42, trinkets Z=5.06, snacks Z=5.00; conjunction p<0.05 FDR. Replication N=13, snack as reference, conjunction Z=3.57 | Chib 2009 (a07, a08) | [E] (small N) |
| Neural value follows own discounting | N=10 scanned; hyperbolic median R2=0.95 (0.84-0.98); k 0.0005 to 0.1189, median 0.0097 | Kable and Glimcher 2007 (a09) | [E] (small N) |
| Monkey OFC neurons code offer or chosen value, not motor | 931 cells; 505 (54%) varied with offer type; under 5% spatial/motor; 79% of responses explained, mean R2 0.63 | Padoa-Schioppa and Assad 2006 (a11) | [E] |
| Value coding is relative (divisive normalisation) | LIP: 12/16 (75%) and 18/27 (66.7%) neurons show extra-RF value effect | Louie 2011 (a13) | [E] |
| Cross-good exchange rate predicts neural scale | only 2 of 13 studies meet the equal-value test | Levy and Glimcher 2012 (a05) | [S] |
| Common currency is not proven | argument, no new data | Hayden and Niv 2021 (a21, b07) | [C] |
| fMRI value results are analysis-fragile | 70 teams, N=108; hypothesis 5 at 84.3%; others 21.4% to 37.1%; three hypotheses significant in 5.7% of teams | Botvinik-Nezer 2020 (b10) | [S] |
| Price label shifts value | pleasantness vs price r=0.59 ($5 vs $45; $10 vs $90 wines); no price effect in blind ratings 8 weeks later | Plassmann 2008 (a18) | [S] |
| Optimistic belief update (human) | N=19; update 11.2 after good vs 7.7 after bad news, t(18)=4.4; 15 of 19 people | Sharot 2011 (d01) | [C] |
| LLM utility fit improves with capability | corr with MMLU: utility accuracy +75.6%, completeness +87.3%, transitivity violations -78.7%; cycles under 1% in the largest models; 500 outcomes, 23 LLMs | Mazeika 2025 (a23, b12, c05) | [C] |
| Linear probes read utilities | near chance at 1B; near the non-parametric fit at 70B; Llama models only | Mazeika 2025 (a24, c07, d11) | [S] |
| Hidden exchange rates | GPT-4o: about 10 US lives for 1 Japanese life | Mazeika 2025 (c08) | [S] |
| GPT-3.5 budget choices very consistent | CCEI 0.998/0.997/0.997/0.999 vs humans 0.980/0.985/0.967/0.963 (N=347); zero GARP violations in 95/89/81/92 of 100 runs; Bronars 99.9% | Chen 2023 (a25, b13, c01, c02) | [S] |
| ...but breaks under reframing | CCEI risk 0.901 (34% below 0.9), time 0.884 (48%), social 0.698 (88%), food 0.894 (49%); invalid answers 4.7% (T=0.5), 9.8% (T=1) | Chen 2023 (c03) | [E] |
| Coherence is model-specific | 39 models: 2 pass at 1%, 7 at 5%, 9 at 10% | Seror 2025 (d10) | [E] |
| Format changes hurt some model families | Llama risk CCEI 0.953 to 0.841 and social 0.968 to 0.756 under single-turn; Qwen 0.980 to 0.739 and 0.994 to 0.889; GPT and DeepSeek flat | Wang 2025 (d08, d09) | [E] |
| LLM loss aversion is modest | pooled lambda 1.26 (CI 1.06-1.46), t(27)=2.66; 28 estimates, 19 models; range 0.49-2.72; 14 loss averse, 5 reversed, 9 none; family explains 27% of variance; human 1.96 | Tarabeih 2026 (a26, d18) | [E] |
| Prospect-theory fit unstable | parameters shift when numbers become words | Wang 2026 (a29) | [C] |
| LLMs are impatient | later reward chosen 22% (GPT-3.5), 16% (GPT-4), 34.5% (GPT-4 with CoT) | Goli and Singh 2023 (c10) | [E] |
| Risk posture shifts with prompting | direct and zero-shot CoT barely move GPT-4; one-shot works; two-shot confounds | Ross 2024 (c15) | [E] |
| Utility-elicit-then-maximise agent | up to 40% accuracy gain; 73.3% vs 33.3% (agriculture) and 64.2% vs 35.0% (stocks) vs o1-preview; tokens 5181 vs 1946 (CoT) | DeLLMa (c24, d15, d16) | [S] |
| Decoy effect in LLMs | GPT-4 decoy-expensive 0.38; Mistral-Instruct 0.24; warning does not remove it (GPT-3.5 t=1.42, GPT-4 t=0.69, ns); gpt-4o t up to -6.85 vs human arm of 617 | d05, d06, d07 | [E] |
| Optimism asymmetry in an LLM | Claude v1.3, asymmetric RW posterior 0.93 +/- 0.04; regret 0.09 to 0.05 | Schubert 2024 (c22, d13) | [S] |
| Pairwise logic breaks | tuning with logically extended data: transitivity 81.1 to 95.2, commutativity 70.2 to 90.5 (Llama-3-8B) | Liu 2025 (a28, d14) | [S] |
| Arithmetic-trained small model predicts human choice | R2 69.3/63.2/64.0/96.1 (uniform) and 70.8/65.5/67.8/95.5 (ecological) over four datasets; ablation cpc18 65.5 to 33.8 | Zhu 2025 (a27, b18) | [E] |

## 4. Mechanisms and models

**4.1 Linear value tracking (fMRI).** Regress the signal on each option's subjective value. Subjective value comes from behaviour: WTP bids (Chib) or a fitted discount function (Kable). Hyperbolic form: SV = A / (1 + kD), where A is the amount, D the delay and k a per-person rate. It fit best (median R2 0.95), but a sum of two exponentials fit as well (a10). Implementation: fit k per person by maximum likelihood on choices, then use SV as a regressor.

**4.2 Good-based choice (Padoa-Schioppa 2011).** Each good has a value computed independently of the alternatives. A comparison step picks the higher. Transitivity is a result of the design, since each good has one number. A software version: score each option alone, store the number, argmax in code.

**4.3 Divisive normalisation (Louie 2011, 2014).** Response to option i is R_i = v_i / (sigma + sum_j v_j), up to a gain constant. Value is relative to the set. Time course (b11): the contextual term arrives later than the initial value signal. Software version: if a score is read in one context, do not compare it with a score read in another context.

**4.4 Attractor comparison (Hunt 2012, a14).** Two pools of units, one per option, receive the values and inhibit each other. The network settles on one. Decision time rises when the values are close. This matches the Hayden and Niv remark that similar options take longer.

**4.5 Thurstonian utility for LLMs (Mazeika 2025).** Each outcome o has U(o) ~ N(mu, sigma^2). The probability that the model prefers A to B is Phi((mu_A - mu_B) / sqrt(sigma_A^2 + sigma_B^2)). Method: sample forced-choice pairs over 500 outcomes, aggregate across framings and samples, fit mu and sigma. Check fit accuracy, cycle probability and completeness (average confidence of stated preference). Then test expected utility by comparing U(lottery) with the expected U of the outcomes. The mean error falls with scale (correlation -87.4% for standard lotteries, -67.6% for implicit ones, c06).

**4.6 Linear probes (Mazeika).** Take the hidden state at the best layer for each outcome description. Fit a linear map to the Thurstonian mu. Test on held-out outcomes. Models: Llama-3.2-1B, 3.1-8B, 3.3-70B only. Exact accuracies are in Figure 8 and were not recorded.

**4.7 Revealed-preference tests (Chen 2023, Wang 2025).** Give the model 25 budget problems (100 points to split between two goods at varying prices). Check GARP: if bundle A was chosen when B was affordable, B must not be chosen when A was affordable. CCEI is the share of budget you must waste to remove all violations; 1.0 is perfect. Bronars power: simulate random choosers; 99.9% violate GARP, so the test has bite. Implementation is straightforward in code and cheap.

**4.8 Utility-elicit-then-maximise (DeLLMa).** Steps: enumerate states and actions; have the LLM rank minibatches of outcomes; turn the rankings into pairwise preferences and fit a utility; estimate the state probabilities; pick the action with the highest expected utility in code. DeLLMa-Pairs(16) used 3 calls, 5181 tokens; Pairs(64) used 10 calls, 20639 tokens (d15). Elicited utilities agreed with human ratings 70.4% (GPT-4), 65.3% (Claude 3), 69.6% (Gemini 1.5) (d16).

**4.9 Asymmetric learning-rate model (Schubert 2024).** Rescorla-Wagner: Q <- Q + alpha_pos * delta if delta > 0, else alpha_neg * delta. In the Claude v1.3 bandit, the asymmetric fit had posterior 0.93 +/- 0.04. The asymmetry vanished without agency, and chosen vs unchosen options had opposite patterns (d13).

**4.10 Prospect-theory fit (Tarabeih, Wang, Jia, Ross).** Value v(x) = x^a for gains, -lambda * (-x)^b for losses, plus a probability weighting function. Fit from binary choices. Wang 2026 (a29): three stages (fit parameters, map each verbal uncertainty marker to an indifference probability, swap markers into prompts). Parameters shift when numbers become words.

## 5. What holds up

**Holds up well**
- The core network (vmPFC, ventral striatum, posterior cingulate) is found in two large meta-analyses with different methods (206 and 81 studies) [E].
- A posterior-to-anterior gradient by reward type is replicated by the Clithero and Rangel direct contrast and partly by Sescousse (not opened) [E].
- Neural value follows each person's own preferences: Chib (N=19, replicated N=13) and Kable (N=10). Small samples, so treat as direction only [E].
- Context dependence of value in neurons (Louie 2011, 2014) [E]. In LLMs, behavioural decoy effects appear and grow with instruction tuning and RLHF (d05); they survive a warning (d06) and exceed humans on credibility ratings in gpt-4o (d07) [E].
- Framing hurts LLM coherence (Chen 2023; Wang 2025) [E].
- LLMs are less patient than humans in several papers [E].

**Failures, doubts and boundary conditions**
- The strict equal-value test of a common currency was met by only 2 of 13 studies (a05). Most evidence is correlational.
- Evidence is mostly from gains. Shared scales for punishments, risk and ambiguity are scarce or mixed (b09; K10) [S].
- Botvinik-Nezer (b10): same data, 70 teams, only one hypothesis near-unanimous. Any one fMRI number is soft.
- The Hayden and Niv critique is unresolved. A 2026 defence has no new data (b08). A testable difference between the two accounts is an open gap (Section 10).
- Sharot 2011 is disputed: Shah 2016 says artefact, Garrett and Sharot 2017 report robustness tests (valence effect F(1,135)=6.29, p<0.02; updating vs a Bayesian agent t(31)=2.53) [C]. Shah was read as abstract only.
- Chen 2023 says GPT is more rational than humans. But the same paper shows collapse under reframing (CCEI 0.698 on social). Seror 2025 finds only 7 of 39 models pass revealed-preference coherence at 5%. Wang 2025 shows format changes hurt Llama and Qwen but not GPT or DeepSeek. Read together: consistency is high within one frame for some model families, low across frames, and model-specific.
- Mazeika is one paper (four evidence lines). "Scale" there is MMLU score, so it means capability. The -97.6% figure is a figure label for utility variance vs scale (Figure 12), not a correlation with MMLU, and should not be cited as a coherence-by-scale result (critique).
- Loss aversion: Jia 2024 gives about 1.48 for ChatGPT (lowest of three); Tarabeih pools to 1.26; Binz and Schulz found 3 of 6 biases. Pooled values hide method effects (curvature 1.01 vs 0.52 by method).
- Probe results are Llama-only with no causal (steering) test.

**Interventions that worked**
- One-shot examples shifted LLM risk posture; direct instruction and zero-shot CoT barely did (c15) [E].
- Chain of thought raised the later-reward share (GPT-4 16% to 34.5%, c10).
- Tuning on logically extended pairs: transitivity 81.1 to 95.2, commutativity 70.2 to 90.5 (d14) [S]. Another data arm gave transitivity 91.9 and commutativity 88.4 (d14).
- Fine-tuning moved Llama-3.1-8B toward assembly preferences from 73.2% to 90.6% agreement (d12).
- Utility elicitation plus code-side expected utility (DeLLMa) beat CoT and self-consistency, but at 2.7 times the tokens of CoT [S].

**Did not work**
- Prompt warnings did not remove the decoy effect (d06).
- Zero-shot CoT did not shift risk parameters (c15). CoT sometimes lowered transitivity (K32).
- Two-shot prompts confounded gains and losses (c15).
- Higher temperature added invalid answers (4.7% at T=0.5, 9.8% at T=1) but changed CCEI little (c03).

## 6. Language models

**Coherence of choice**
- GPT-3.5-Turbo, 25 budget tasks per domain: mean CCEI 0.998 (risk), 0.997 (time), 0.997 (social), 0.999 (food). Humans (347): 0.980, 0.985, 0.967, 0.963. Literature range 0.81-0.99 (a25, b13).
- Wang 2025, plain format: risk CCEI GPT 1.000, DeepSeek 1.000, Llama 0.953, Qwen 0.980; social 0.994, 0.999, 0.968, 0.994 (d08).
- Under single-turn dialogue Llama and Qwen fell to as low as 0.739 to 0.756; GPT and DeepSeek stayed at about 1.0 (d09).
- Alternative price framing in Chen 2023: CCEI down to 0.698 (social) with 88% of runs below 0.9.
- Seror 2025: 39 models, revealed preference on moral dilemmas. 2 pass at 1%, 7 at 5%, 9 at 10% (d10).
- Mazeika 2025: 23 models (18 open, 5 proprietary), 500 outcomes. Cycles under 1% at the top. Utility fit improves with MMLU (+75.6%).
- Liu 2025 (a28): pairwise preferences often break transitivity, commutativity and negation invariance. Consistency tracks robustness and agreement with humans.

**Value structure**
- Linear probes decode Thurstonian utility at 70B, not at 1B (a24, d11).
- Hidden exchange rates: GPT-4o about 10 US lives per Japanese life. One model ranked lives in China below Pakistan while denying it when asked (c08). Stated and revealed preferences often diverge (d17, b16, b15). Claude gave neutral answers to the base (stated) questions about 84% of the time (d17). Medical-diagnosis cost ratios were compared under self-report and revealed estimation (b15, d20; d20 abstract and intro only).
- Han 2025 (c29): in Qwen2.5-7B-Instruct, steering at strength 4.0 in middle layers shifts value expression roughly linearly. Orthogonal directions keep the effect after removing 32-73% of the norm (steering evidence, not a vmPFC test).

**Behavioural economics**
- Loss aversion: pooled 1.26 (28 estimates, 19 models, range 0.49-2.72, prediction interval 0.20-2.31). Jia 2024: risk-aversion mean ChatGPT-4-Turbo 0.6031, Claude-3-Opus 0.4959, human 0.48; ChatGPT probability weighting 1.1819 (c16).
- Framing in reasoning models (o3, Claude-4, Claude-4-Thinking, GPT-4o, Gemini-1.5-Pro): loss-frame BLITZ chosen 85.6% (107/125), gain-frame CONTROL chosen 88.8% (111/125) (b17). Wang 2026 says the pattern is unstable across descriptions.
- Time: GPT-3.5 and GPT-4 choose the later reward 22% and 16% (c10). Ross 2024: all LLMs discount more than humans (M=217 settings, N=100 samples each at T=1, c14). GPT-4 Turbo shows stronger probability distortion for losses than humans.
- Anchoring: ChatGPT low anchor mean 20.83 vs humans 22.50; high anchor 105.97 vs 80.50 (c12). Binz and Schulz 2023: 3 of 6 biases in GPT-3 (c19).
- Decoys: positive and larger after instruction tuning and RLHF; GPT-4 hiring study attraction effect positive in all six occupations (d06).
- Prompt effects: persona shifts risk (Claude-3-Opus more risk averse with minority personas, c17). One-shot shifts, zero-shot CoT does not (c15).
- Optimism: Claude v1.3 learns more from positive prediction errors (0.93 posterior, c22). One model, temperature 0.
- Small-model account: Arithmetic-GPT predicts human risky and intertemporal choices (R2 up to 96.1%, a27). Centaur: choice NLL 0.4274 vs Llama 0.5342 vs cognitive model 0.6563 on choices13k (c21).
- Learning preferences from choice data: GPT learns risk aversion better than disappointment aversion; 5 observations suffice to reproduce a corner-solution pattern (c26).

**Agent loops.** DeLLMa: up to 40% accuracy gain over competing methods; 73.3% vs 33.3% (agriculture) and 64.2% vs 35.0% (stocks) vs o1-preview; calibration 0.062 (GPT-4), 0.142 (Claude 3), 0.064 (Gemini 1.5). It uses 5181 tokens vs 1946 for CoT, so the comparison is not equal-token.

**What nobody has tested.** Divisive normalisation in an LLM (K30). Stable cross-domain exchange rates in the Chib sense. Reasoning-model reframing at equal tokens. Probe causality.

## 7. What our agent should take

Schema parts: G guardrails, S states, O operators. Background only for the subfield, so "Add now" is short and uses only [E] items with a cheap check. "Memory" means no schema part.

### Add now (established)

1. **Rate options together, not alone** (O, used in S3/S7). Value is relative (K08 [E]; a13, b11, a12) and decoys shift LLM choice, not removable by a warning (K29 [E]; d05, d06, d07). Rule: when options are scored, score them in one shared context, in code-randomised order. Do not compare scores made in different contexts.
2. **Check consistency under reframing** (G, S8). Framing cuts CCEI to 0.698-0.901 (K17 [E]; b14, c03, d08, d09). Rule: ask the same valuation in two wordings or orders and require agreement. Code compares; disagreement triggers G1 (doubt on a signal). Cost is a second short answer, and it must be counted under G7.
3. **Order-swap and negation checks on pairwise judgments** (S, S4/S8). Pairwise LLM judgments break transitivity, commutativity and negation (K25 [E]; a28, b16, b15). Rule: swap order; compare; ranking and cycle detection in code (G5).
4. **Do not assume the agent shares human loss aversion or patience** (memory note, G). Measured lambda is 1.26 pooled with wide spread (K18 [E]); LLMs choose the later reward only 16-34.5% (K20 [E]). Rule: measure the backbone on a small probe rather than assume. Whether a long-horizon line helps is Test-first item U12.
5. **Check backbone coherence before relying on utility steps** (S0/S1). Coherence is model-specific (K31 [E]; d08, d09, d10). Rule: run a small GARP-style probe on the chosen backbone, once per backbone, outside the token budget of a problem.
6. **Label and framing caution** (G). Labels like price or prestige shift value in people (K12 [S]) and decoy effects shift LLMs (K29 [E]). Rule: strip prestige or price labels when the item does not depend on them. This is a hygiene rule; confirm with U4 before making it a guardrail.

### Test first (not yet established)

- **Separate value and stakes** (K02 [S]; O/S). Output option score and option importance as two numbers (from the salience pattern in a01). Test U1.
- **Utility-elicit-then-maximise operator** (K22 [S]; O). One paper, not equal-token. Test U2.
- **Score-then-choose vs direct pairwise** (K09 [C]; K13 [C]; O). This tests the Hayden and Niv question directly, and whether fitting a pairwise utility then ranking helps. Test U3.
- **Numeric probabilities over verbal** (K19 [C]; G). Test U6.
- **Hidden exchange-rate audit** (K15 [S]; G). Test U7.
- **Optimistic update guard** (K24 [S], K27 [C]; G). Test U8.
- **Example beats instruction for risk posture** (K21 [E] on GPT-4 only; O). Test U9.
- **Loss-side items consistent separately from gain-side** (K10 [S]). Test U10.
- **Decoy and scaling test of normalisation** (K30 open; O). Test U11.
- **Long-horizon step for time tradeoffs** (K20 [E] for the bias, the fix is untested; G). Test U12.

## 8. Concrete tests on our bench

All arms at equal total tokens (count setup cost, G7). Report the plain model as the control.

| Test | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 (U1) Value and stakes | Multi-option allocation with unequal importance | value-only score vs value plus stakes, then code allocates | Stakes-weighted payoff vs gold; accuracy of top pick | Small gain only on tasks where importance varies; none elsewhere |
| T2 (U2) Elicit then maximise | Open-ended option choice with uncertain states (DeLLMa-style, plus ours) | CoT with k samples and vote vs elicit-utilities-then-expected-utility, equal tokens | Accuracy vs gold choice; regret | Gain is likely smaller than the reported 40% once tokens are matched; add only if it keeps a lead |
| T3 (U3) Score-then-choose vs direct | Choice among 4-8 options | direct pairwise tournament vs score each then rank in code, equal tokens | Accuracy; cycle rate; flip rate under reorder | Unknown; the evidence is contested |
| T4 (U4) Label hygiene | Identical options with price or prestige labels | labelled vs stripped | Score shift; rank flips | Shifts exist (decoy, label); stripping removes them if the item does not depend on the label |
| T5 (U5) Reframe agreement | Budget (CCEI-style) and valuation items, 2-3 reframings | single answer vs answer under two framings with agreement rule, equal tokens | Flip rate; CCEI; accuracy | Lower flip rate; accuracy change is the thing to watch |
| T6 (U6) Numbers vs words | Gambles with numeric or verbal probability | numeric vs verbal | Parameter shift; choice agreement | Verbal shifts choices; numbers stabilise |
| T7 (U7) Exchange-rate audit | Lives-by-group and good-by-good tradeoffs | plain vs scaffold with audit step | Fitted exchange-rate spread | Audit narrows spread (untested) |
| T8 (U8) Optimism | Bandit or evidence streams with symmetric good and bad feedback | plain vs normative-baseline guard | Update asymmetry vs Bayesian | Asymmetry present in some models; guard reduces it |
| T9 (U9) Risk posture | Risk-posture items | instruction vs one-shot example vs both | Risk parameter shift | One-shot wins (GPT-4 data) |
| T10 (U10) Gain vs loss coherence | Loss-side vs gain-side items | consistency checks per side | CCEI per side | Lower coherence on loss side if K10 holds |
| T11 (U11) Decoy and scaling | Option sets with a dominated decoy; scale all values by a constant | rate each alone vs together vs subset | Choice-share change under scaling | Under divisive normalisation shares stay fixed under scaling; LLMs untested |
| T12 (U12) Long-horizon step | Intertemporal items | plain vs add a long-term step, equal tokens | Share of later-reward choice vs gold or policy | Share rises (CoT raised GPT-4 16% to 34.5%) |

## 9. What does not transfer, and why

- **Anatomy** (vmPFC, striatum, voxel counts, MEG timing): no counterpart in a transformer. The only partial analogue is hidden-state probing, tested on three Llama models.
- **Neural value as proof of a single scale.** Correlation with value is also predicted by heuristic or policy-based accounts (Hayden and Niv). So the neural data cannot justify a mandatory scoring step.
- **Human effect sizes** (Chib N=19, Kable N=10, Sharot N=19). Small samples; they do not set targets for an agent.
- **Human loss aversion (1.96) and impatience.** LLM estimates differ (1.26 pooled; less patient). The agent should be measured, not assumed.
- **Rationality as a goal.** High CCEI is a within-frame property; Chen 2023 shows that it collapses under reframing, so it is not evidence of robust value.
- **Optimism bias.** Human result is disputed; LLM result is one model (Claude v1.3, temperature 0) and vanished without agency.
- **Monkey neuron findings** (931 cells, LIP). Different system; relevant only as a motivation for rating options in context.
- **Mazeika's moral exchange rates.** They reflect training data and alignment, not a reward circuit. Useful only as an audit idea.

## 10. Open questions

1. Equal-token comparison of utility elicitation vs CoT on open-ended option choice (only DeLLMa, not equal-token).
2. Framing-induced CCEI drop in 2025-26 reasoning models, and whether a re-ask-and-agree step repairs it.
3. Whether Mazeika-style utilities and probes replicate beyond three Llama models, and whether they predict behaviour on novel items or can be steered (causal test).
4. Divisive normalisation or range effects in LLMs (no direct study; the CogSci 2025 context-effects paper d19 was a snippet).
5. A stable shared scale across goods (money, food, time, social) in the Chib and Levy-Glimcher sense, with cross-domain exchange rates predicting choice.
6. Whether Schubert 2024 optimism replicates on other models, base vs RLHF.
7. What the 2026 common-currency defence (b08) predicts that Hayden and Niv do not, in behavioural form.
8. Whether a numeric score before the choice narrows the stated-revealed gap (Yamin 2026 d20 read only in abstract and intro).
9. Loss-aversion stability across elicitation methods, and whether a scaffold moves it more than a prompt (no scaffold vs prompt contrast exists).
10. Whether hidden exchange rates persist in an agent with tools and an audit step (only fine-tuning evidence, d12).
11. Sharot 2011 and Shah 2016 numbers: Shah was read only as an abstract.

## 11. Sources

[V] opened this session; [M] snippet or abstract only. Evidence ids in brackets.

**Human and animal**
- [V] Bartra, McGuire, Kable 2013 [a01-a04, b01, b02, b25]. https://pmc.ncbi.nlm.nih.gov/articles/PMC3756836/
- [V] Clithero and Rangel 2014 [a16, b03, b04]. https://pmc.ncbi.nlm.nih.gov/articles/PMC4158359/
- [M] Sescousse, Caldu, Segura, Dreher 2013 [a17]. https://europepmc.org/article/MED/23999088
- [V] Levy and Glimcher 2012 [a05, a06]. https://pmc.ncbi.nlm.nih.gov/articles/PMC4093837/
- [V] Chib, Rangel, Shimojo, O'Doherty 2009 [a07, a08]. https://pmc.ncbi.nlm.nih.gov/articles/PMC6666137/
- [V] Kable and Glimcher 2007 [a09, a10, b05]. https://pmc.ncbi.nlm.nih.gov/articles/PMC2845395/
- [V] Padoa-Schioppa and Assad 2006 [a11, b06]. https://pmc.ncbi.nlm.nih.gov/articles/PMC2630027/
- [V] Padoa-Schioppa 2011 [a12]. https://pmc.ncbi.nlm.nih.gov/articles/PMC3273993/
- [V] Louie, Grattan, Glimcher 2011 [a13]. https://pmc.ncbi.nlm.nih.gov/articles/PMC3285508/
- [V] Louie et al. 2014 [b11]. https://pmc.ncbi.nlm.nih.gov/articles/PMC4244470/
- [V] Hunt et al. 2012 [a14]. https://pmc.ncbi.nlm.nih.gov/articles/PMC3378494/
- [V] Rangel, Camerer, Montague 2008 [a15]. https://pmc.ncbi.nlm.nih.gov/articles/PMC4332708/
- [V] Plassmann et al. 2008 [a18]. https://pmc.ncbi.nlm.nih.gov/articles/PMC2242704/
- [M] Tom, Fox, Trepel, Poldrack 2007 [a19]. https://europepmc.org/article/MED/17255512
- [M] Montague, King-Casas, Cohen 2006 [a20, d04]. https://europepmc.org/article/MED/16776594 (d04 gives pmid 16776592; check the id before citing)
- [V] Hayden and Niv 2021 [a21, a22, b07]. https://pmc.ncbi.nlm.nih.gov/articles/PMC12398331/
- [V] Case for value as a common currency, 2026 review [b08]. https://pmc.ncbi.nlm.nih.gov/articles/PMC13281118/
- [V] Review 2025, anticipated rewards and punishments [b09]. https://pmc.ncbi.nlm.nih.gov/articles/PMC11930275/
- [V] Botvinik-Nezer et al. 2020 [b10]. https://pmc.ncbi.nlm.nih.gov/articles/PMC7771346/
- [M] Chib 2009, Levy and Glimcher 2012, Levy et al. 2010, McClure et al. 2004, Bennett, Niv, Langdon 2021 [b19-b23]. No url recorded; named only.
- [V] Sharot, Korn, Dolan 2011 [d01]. https://pmc.ncbi.nlm.nih.gov/articles/PMC3204264
- [V] Garrett and Sharot 2017 [d02]. https://pmc.ncbi.nlm.nih.gov/articles/PMC5380127
- [M] Shah et al. 2016 [d03]. https://europepmc.org/search?query=pessimistic%20view%20of%20optimistic%20belief%20updating

**LLM and AI**
- [V] Mazeika et al. 2025 [a23, a24, b12, b24, c05-c09, d11, d12]. https://arxiv.org/abs/2502.08640
- [V] Chen, Liu, Shan, Zhong 2023 [a25, b13, b14, c01-c04]. https://arxiv.org/abs/2305.12763
- [V] Tarabeih 2026 [a26, d18]. https://arxiv.org/abs/2610.33103
- [V] Zhu, Yan, Griffiths 2025 [a27, b18]. https://arxiv.org/abs/2405.19313
- [V] Liu et al. 2025 [a28, d14]. https://arxiv.org/abs/2410.02205
- [V] Wang et al. 2026 [a29]. https://arxiv.org/abs/2508.08992
- [V] Revealed preferences and LLM alignment 2026 (Yamin et al.) [b15, d20]. https://arxiv.org/abs/2605.08556
- [V] Gu, Wang, Han 2025 [b16, d17]. https://arxiv.org/abs/2506.00751
- [V] Prospect theory in LLMs 2025 [b17]. https://arxiv.org/abs/2508.00902
- [V] Goli and Singh 2023 [c10, c11]. https://arxiv.org/abs/2305.02531
- [V] Suri et al. 2023 [c12, c13]. https://arxiv.org/abs/2305.04400
- [V] Ross, Kim, Lo 2024 [c14, c15]. https://arxiv.org/abs/2408.02784
- [V] Jia et al. 2024 [c16, c17]. https://arxiv.org/abs/2406.05972
- [V] Binz and Schulz 2023 [c18-c20]. https://arxiv.org/abs/2206.14576
- [V] Binz et al. 2025 Centaur [c21]. https://arxiv.org/abs/2410.20268
- [V] Schubert et al. 2024 [c22, c23, d13]. https://arxiv.org/abs/2402.03969
- [V] Liu, Fu, Yogatama, Neiswanger 2024 DeLLMa [c24, c25, d15, d16]. https://arxiv.org/abs/2402.02392
- [V] Kim et al. 2026 [c26]. https://arxiv.org/abs/2401.07345
- [V] Horton 2023 [c27]. https://arxiv.org/abs/2301.07543
- [V] Coletta et al. 2024 [c28]. https://arxiv.org/abs/2402.08755
- [V] Han et al. 2025 [c29]. https://arxiv.org/abs/2509.24319
- [M] Spiegel et al. 2025 [c30]. https://arxiv.org/abs/2506.08966
- [V] Itzhak et al. 2024 [d05]. https://arxiv.org/pdf/2308.00225
- [V] Valkanova and Yordanov 2024 [d06]. https://arxiv.org/html/2409.15299v1
- [V] Liu and He 2024 [d07]. https://arxiv.org/pdf/2411.15396
- [V] Wang et al. 2025 [d08, d09]. https://arxiv.org/pdf/2505.21371
- [V] Seror 2025 [d10]. https://arxiv.org/pdf/2412.04476
- [M] Xie, Huang, Busemeyer 2025 [d19]. https://escholarship.org/uc/item/4fv3t754
