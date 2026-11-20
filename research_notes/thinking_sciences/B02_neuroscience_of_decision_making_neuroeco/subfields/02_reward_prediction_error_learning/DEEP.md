# Reward prediction error learning: deep document

*Subfield B02.02. Scope: dopamine as a prediction-error signal in model-free learning, and every LLM or AI study that tests or uses the idea. Evidence ids (a01 to d20) and claim ids (B02.02-K01 to K26) refer to evidence_a-d.jsonl and claims.jsonl in this folder. Status tags: [E] established, [S] single-source, [C] contested. Only lines marked opened:true in the evidence files were read in full; see section 11.*

## 1. What it is

Reward prediction error (RPE) learning is the idea that the brain learns values by comparing what it got with what it expected. The gap is the error. Positive error: better than expected. Negative error: worse. The error then updates the stored value.

The formal version is temporal difference (TD) learning. The error at time t is:

delta(t) = r(t) + gamma * V(t+1) - V(t)

V is the stored value of a state. r is the reward just received. gamma is a discount (Maes 2020 simulations used gamma = 0.95 and learning rate alpha = 0.05; a26). The update is V(t) <- V(t) + alpha * delta. This is "model-free": it stores cached values and never builds a map of how states lead to each other.

The neuroscience claim (Montague, Dayan, Sejnowski 1996; Schultz, Dayan, Montague 1997; a01, a02) is that phasic firing of midbrain dopamine neurons carries delta. Burst for an unpredicted reward. No change for a fully predicted reward. A dip when a predicted reward is missing. After learning, the burst moves to the cue that predicts the reward. These three cases come from the abstracts and background knowledge. The original 1990s neuron counts were not opened in this run (section 10).

Why it matters for us. Our agent is a language model inside a scaffold. It does not update weights while it works. So RPE learning as a biological mechanism sits outside the thinking loop. Three things still cross over:

1. The formal idea of "surprise relative to expectation" as a gate for what to remember or reconsider (D-MEM, PreCoMem).
2. The finding that LLMs, given reward feedback in context, behave like asymmetric reward learners, plus the practical limits of in-context reward learning (Schubert, Monea, Song, Kwon).
3. The model-free versus model-based split (Daw 2011; Doll 2012), which shows up in LLM behaviour on the two-step task and in how much a planning step helps.

Honest reading: this is background for the schema, with a few usable cautions about how to feed outcome feedback back to the model.

## 2. History and theories in depth

**1990s: the founding.** Schultz and colleagues recorded single dopamine neurons in monkeys. Mirenowicz and Schultz 1994 (d15, abstract only): two monkeys; about three quarters of dopamine neurons gave a short burst to unpredicted liquid, and the response moved to the conditioned stimulus once the task was learned. Montague, Dayan and Sejnowski 1996 (a01) and Schultz, Dayan and Montague 1997 (a02, d16) tied these recordings to TD learning. The 1997 paper is a synthesis and reports no new neuron counts (d16). Europe PMC lists about 6,081 citations. The numbers sit in earlier recording papers (Schultz 1993; Mirenowicz and Schultz 1994), not read in full here.

**2000s: quantitative tests and adaptive coding.**
- Nakahara et al. 2004 (a05, abstract only): the response to a reward-indicating light rose with the number of earlier unrewarded trials in a fixed-probability task, as a conventional TD model predicts. In a task where reward probability rose with each unrewarded trial, the pattern fitted a context-dependent error instead.
- Bayer and Glimcher 2005 (d14, opened): 2 rhesus monkeys, saccade task, reward 0.2 to 0.28 ml. 81 neurons recorded, 50 analysed (at least 100 trials, mean 292). 44 of 50 were modulated by reward history at p<0.01, mean R-squared 0.29 (SD 0.15). Mean response to unpredicted reward 26 Hz (SD 9, n=46). Firing tracked current reward minus a recency-weighted average of past rewards, but only for better-than-expected outcomes. Below-baseline firing carried no history signal. So the rate code is one-sided.
- Tobler, Fiorillo, Schultz 2005 (a04, abstract only): response gain adapts to reward variance.

**2011 to 2012: the model-based turn.** Daw, Gershman, Seymour, Dayan, Dolan 2011 (a06 to a08, b01, b02) ran the two-step task in fMRI. N=17, 201 trials each, reward probabilities drifting (SD 0.025, bounds .25 to .75). Reward main effect p<1e-8. Reward-by-transition interaction p<5e-5, which pure model-free learning cannot produce. Median model-free weight 61% (model-based 39%). Hybrid model exceedance probability 92%; 48% of the population hybrid, 18% pure TD. Ventral striatal BOLD error signals were not pure model-free: a difference regressor (hybrid error minus model-free error) added explanatory power in right ventral striatum, and neural and behavioural model-based weights correlated across subjects (p<.01, small-volume corrected). Doll, Simon, Daw 2012 (a09, a10, b03) reviewed why model-based signatures turn up in regions once seen as model-free. Their diagnostic is revaluation: behaviour that adapts at once to a devalued outcome is goal-directed.

**2016 to 2020: rodent causal tests and anomalies.**
- Sadacca, Jones, Schoenbaum 2016 (b04): rat dopamine neurons responded to the inferred value of a cue never paired with reward (sensory preconditioning). 14 rats, 304 putative dopamine neurons in conditioning; probe test 52 putative dopamine neurons; A>C inferred t(51)=5.02, p<.001. Standard TD cannot do this.
- Eshel et al. 2016 (a12): mouse dopamine neurons share a common response function, scaled copies of one curve. Light-identified n=40 and n=31.
- Sharpe et al. 2017 (a15, a16): activating dopamine at the C-to-X transition in sensory preconditioning reversed blocking with no reward. ChR2 n=18, eYFP n=19. Group by cue interaction F(1,35)=4.154, p=0.049. So dopamine is sufficient to drive value-free associations.
- Sharpe et al. 2020 (a17, b05, b24): in three experiments, activation did not give cues cached value. Exp 1 ChR2 n=8, eYFP n=8; conditioned reinforcement cue by group F(1,14)=0.004, p=0.952. Exp 3: 280 stimulated trials, no value gain. Reading: transients are not model-free errors.
- Maes et al. 2020 (a18, a19, b06): shunting cue-evoked dopamine blocked second-order conditioning (z=1.9, p=0.03, r=0.34) but left blocking intact (z=0.05, p=0.48). That fits a TD error at the cue. n=16 rats. This conflicts with Sharpe 2020 (different manipulations; one lab family; modest effects).
- Dabney et al. 2020 (a13, a14, b08, b25): distributional RL. See section 4.
- Kim et al. 2020 (a20) and Jeong et al. 2022 (a21, b07): ramps and causal-contingency accounts. See sections 4 and 5.

**2019 to 2024: reviews and extensions.** Gershman and Uchida 2019 (d18, opened): backward blocking is not explained by a simple TD error, and dopamine also reflects uncertainty over states, values and policy. Gershman et al. 2024 (d17, abstract and figure titles only): the original RPE theory is probably too simple; three challenges are ramping, sensory and motor responses, and action selection; a generalised prediction error answers each, but some findings need other explanations. Deserno et al. 2021 (d19): N=62, 150 mg levodopa, within-subject; the drug boosted model-based guidance of model-free credit assignment without a direct effect on either system.

**Field state in one line:** classic TD-RPE is a good first account of phasic firing in simple conditioning. Every extension (belief states, distributions, causal contingency, successor-like features) is a patch or a rival that explains some anomalies. No single replacement has won (claims K05, K25).

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Humans mix model-free and model-based control | N=17; median model-free weight 61%; hybrid exceedance prob 92%; 48% hybrid, 18% pure TD; reward x transition p<5e-5 | Daw 2011 (a06, b01) | [E] K01 |
| Ventral striatal error is not purely model-free | Difference regressor adds signal; neural-behavioural model-based weight correlation p<.01 (small-volume corrected) | Daw 2011 (a08); Doll 2012 (b03) | [S] K02 |
| Monkey dopamine tracks reward minus recent average, positive side only | 2 monkeys; 44 of 50 neurons p<0.01; mean R2 0.29; 26 Hz mean burst | Bayer and Glimcher 2005 (d14) | [C] K24 |
| Mouse dopamine neurons have diverse reversal points (distributional code) | 40 cells, 5 mice; split-half R=0.58, p=1.8e-5; 13/40 above and 10/40 below baseline at 5 uL; control partitions p=0.32 and p=0.78 | Dabney 2020 (a13, a14) | [C] K04 |
| Common response function across neurons | n=40 and n=31 light-identified | Eshel 2016 (a12) | [C] (rival to K04) |
| Dopamine transients drive value-free association learning | ChR2 n=18 vs eYFP n=19; F(1,35)=4.154, p=0.049 | Sharpe 2017 (a15) | [C] K03 |
| Stimulation does not act as a model-free error | ChR2 n=8 vs 8; conditioned reinforcement F(1,14)=0.004 | Sharpe 2020 (b05) | [C] K03 |
| Silencing cue dopamine blocks second-order learning, not blocking | z=1.9, p=0.03, r=0.34; blocking z=0.05 | Maes 2020 (b06) | [C] K03 |
| Dopamine responds to inferred value | 52 putative DA neurons; t(51)=5.02; r(50)=0.63 | Sadacca 2016 (b04) | [S] |
| Ramps follow RPE with value change, not value | Calcium ramp R=0.18 +/- 0.04 (n=16 mice); spiking fit RPE weight 0.91 +/- 0.20 over 78 neurons (critique, PMC7736562) | Kim 2020 (a20) | [C] K05 |
| Release fails several TD predictions; fits ANCCR | n=7 to 8 mice; unpredicted-reward response rises with experience t(7)=4.40, p=0.0031 | Jeong 2022 (b07) | [C] K05 |
| Accumbens core release behaves as general excitation | 9 rats; backward conditioning reward release grows, cue release shrinks | Taira 2024 (b09, b26) | [S] K05 |
| Fitted RL parameters are poorly reliable | Bandit N=69, reversal N=47, 5 weeks; ICC .02 to .52 and .01 to .71; win-stay ICC .53 to .62 | Test-retest 2024 (b10) | [S] K06 |
| Levodopa boosts MB guidance of MF credit assignment | N=62, 150 mg; MF repetition x drug b=0.07, p=0.500; model-agnostic partly null | Deserno 2021 (d19) | [S] K26 |
| LLM in-context learning is asymmetric (optimism) | Claude v1.3: alpha+ 0.87 vs alpha- 0.10, t(49)=20.1; regret 0.09 to 0.05; four chat models confirmatory 0.483 vs disconfirmatory 0.166 | Schubert 2024 (c01); Hayes 2024 (c05) | [E] K08 |
| Asymmetry depends on scaffold | Reverses for unchosen option under full feedback; gone for forced choices; regret 0.07 to 0.02, t(143)=2.5 | Schubert 2024 (c02, c03, d07, d08) | [S] K21 |
| LLMs encode relative value | GPT-4 Turbo ~99% locally optimal by trial 5; relative-value choice .829 vs .698 with explicit comparisons, F(1,1159)=440.88; expected-outcome prompt almost removed the bias (GPT-4 Turbo, Llama-2-70B) | Hayes 2024 (c04, c05) | [S] K09 |
| Llama-3 70B has a TD-like SAE latent | Best latent r=0.58 (block 34); lesion 24.3% to 18.9%; SR r=0.62 vs transition matrix 0.49; TD error r=0.60 vs surprise r=0.18 | Demircan 2024 (a24, b11 to b14) | [S] K07 |
| Value and TD-error neurons in open LLMs | Zero 1% value neurons: MATH500 75.2% to 37.0%; TD-neuron PRM best-of-4 72.3 avg vs random 66.1 | Zou 2026 (d09, d10) | [S] K22 |
| Bandit ICRL works, size matters | Qwen2.5-7B Banking77 6.2% to 72.2% | Monea 2025 (b15, b16) | [E] part of K10 |
| Self-judged ICRL beats best-of-N on Game of 24 | GPT-4.1: ICRL 90/84 vs best-of-N 49, Reflexion 44, Self-Refine 47, Long-CoT 47, CoT 6 | Song 2026 (c08, b17) | [C] K10 |
| Gain comes from earlier attempts, not reward labels | Reward-sensitive cells 3.3% (HumanEval+, 6 of 180) and 4.4% (MBPP+, 8 of 180); flipped or random reward keeps most gain | Kwon 2026 (d01, d02) | [S] K18 |
| Raw failures are replayed, not avoided | Replay 0.7% to 3.1%; with low label 2.5%; moving best trajectory last 3.0% to 13.2% | Kwon 2026 (d03) | [E] K19 |
| Verbal reflection plus a reliable test helps | HumanEval Rust hard 50: base 0.60; no tests 0.52; no reflection 0.60; full 0.68; HotPotQA +8 points | Reflexion (d06) | [E] K19 |
| Pseudo-label reward loop beats best-of-16 | Qwen2.5-7B: MATH 71.0 vs 69.6; AMC 53.0 vs 43.4 | TR-ICRL 2026 (d04) | [S] K20 |
| Unaided LLMs explore poorly in bandits | GPT-4 basic: suffix failure >60% (T=500, N=20); only 1 of 48 to 72 configs worked | Krishnamurthy 2024 (c13, c23) | [E] K13 |
| External statistics help strong models, hurt small ones | Gemini Pro raw 45.5 to summarised 60.0; contextual 7.1 to 64.3; Gemma-2B 7.6 to 4.9; UCB 90.6 to 96.4 | EVOLvE (c14, d11) | [E] K13; [S] K23 |
| Scale and prompting raise model-basedness | 35 LLMs; beta=0.481; CoT +64.59%; step-back +118.59% | CogBench (c16) | [S] K15 |
| Surprise-gated memory cuts tokens | D-MEM: 319K vs 1,648K tokens (-80%); F1 .369 vs .336 noisy; single-hop 21.6 vs 44.7 | D-MEM (c18, d12) | [S] K16 |
| Another surprise gate keeps single-hop | PreCoMem LoCoMo 73.57 overall, single-hop 81.41 at 3.3k tokens/query | PreCoMem (d13) | [S] K16 |
| Reward-aware attention heads | 597 of 2,048 heads (29.1%) vs 102 expected; 249 positive, 348 negative | Song 2026 (c09) | [S] K12 |
| Transformers can implement TD(0) in a forward pass | Theorem: L-layer linear transformer equals preconditioned batch TD(0) | Wang 2025 (c07) | [S] K14 |
| Fine-tuned human-choice model | Centaur NLL 0.44 vs domain models 0.56; horizon task worse (0.4032 vs 0.3595) | Binz 2025 (c17) | [S] K17 |

## 4. Mechanisms and models

**4.1 TD(0) (implementable in a few lines).**
```
V = defaultdict(float)
for each step (s, r, s2, done):
    target = r + (0 if done else gamma * V[s2])
    delta  = target - V[s]
    V[s]  += alpha * delta
```
Typical values: alpha 0.05 to 0.3, gamma 0.95. Eligibility traces (lambda) spread delta to earlier states; Daw 2011 fitted lambda median 0.57 (b01). The same delta can serve as a "surprise" signal.

**4.2 Q-learning for choices.** Q[s,a] <- Q[s,a] + alpha * (r + gamma * max_a' Q[s2,a'] - Q[s,a]). Choice by softmax with inverse temperature beta, or epsilon-greedy. Demircan 2024 used a Q-learning agent as the reference for correlating latents (a24).

**4.3 Asymmetric Rescorla-Wagner (what LLMs fit).** Two learning rates: Q <- Q + alpha_plus * delta if delta > 0, else Q + alpha_minus * delta. Humans show alpha_plus > alpha_minus for chosen options (optimism); with full feedback the unchosen option flips (the confirmatory vs disconfirmatory form). Claude v1.3 fit alpha+ 0.87 and alpha- 0.10 (c01). To measure it on any LLM: run a two-armed bandit with partial feedback, fit the two-rate model by maximum likelihood to the model's choices, compare against a one-rate model (the papers report posterior probability, 0.93 for the asymmetric model).

**4.4 Hybrid model-free and model-based (two-step task).** Stage-1 value = w * Q_mb + (1 - w) * Q_mf. Q_mb comes from planning over a learned transition model: Q_mb(s1, a) = sum over s2 of P(s2 | s1, a) * max Q(s2). Daw's median model-based weight was 0.39 (b01). Diagnostic without fitting: the stay-probability signature. A pure model-free learner repeats a rewarded first-stage choice regardless of transition type. A model-based learner repeats it after a common transition and switches after a rare one. A reward x transition interaction in stay probability means model-based control (a07, b02).

**4.5 Distributional TD (Dabney 2020).** Keep many value predictors, each with its own pair (alpha_i+, alpha_i-). Optimism tau_i = alpha_i+ / (alpha_i+ + alpha_i-). Each predictor converges to the tau_i-th expectile of the reward distribution, so together they encode the whole distribution. Mouse data: mean asymmetry tau = 0.48; 10 of 31 optimistic and 9 of 31 pessimistic cells against about 3 of 31 by chance; ANOVA F(30,3335)=4.31, p=6e-14 (b08). Engineering use: keep a low, middle and high estimate per option instead of one mean.

**4.6 Successor representation view.** In a graph task with no reward, Llama latents fit an SR-based TD signal better than a transition-matrix surprise (r=0.62 vs 0.49; TD error 0.60 vs surprise 0.18; b12). SR: M(s, s') = expected discounted future visits to s' from s; V(s) = sum over s' of M(s, s') * R(s').

**4.7 ANCCR (Jeong 2022; a21).** A retrospective rival: dopamine signals the adjusted net contingency of causal relations, computed by looking back from a meaningful event to see which earlier cues preceded it more than base rate. It reproduces blocking, unblocking, overexpectation, conditioned inhibition and probability and magnitude responses. Engineering use: credit assignment by looking back from outcomes, not forward from cues.

**4.8 Ramps as value-change error (Kim 2020; a20).** The ramp toward a goal is delta computed from moment-to-moment change in value. A teleport that jumps value gives a phasic response larger than the normal ramp peak (peak ratio 2.25 +/- 0.31, n=11 mice, p=0.0010; short teleport ratio 1.35).

**4.9 In-context RL (ICRL) loop for LLMs.** Prompt = task + list of (earlier answer, scalar reward) pairs. The model writes the next answer. Run N episodes. Variants: Naive ICRL (all pairs); Explorative ICRL with stochastic prompt sampling (p_keep = 0.1, temperature 1.0) and positive-only context (Monea; b15, b16). Song 2026 "Preset" gives a numeric score each round; "Autonomous" has the model judge itself on 0 to 3 (b17). Kwon 2026 (d01) shows the earlier attempts do most of the work.

**4.10 Surprise-gated memory.** D-MEM (c18, d12): score = surprise x utility; below threshold 0.3 skip memory work; above 0.7 deep knowledge-graph update. The surprise is an embedding distance, not a reward error. PreCoMem (d13): "Effective Surprisal" with a two-threshold gate (maintain, profile, correct).

**4.11 Transformer TD in theory.** An L-layer linear transformer forward pass can implement batch TD(0) with a preconditioner; training on policy-evaluation tasks ends at that solution for L=2,3,4 (c07). Synthetic Markov reward processes only.

**4.12 Probing for TD in an LLM.** Train SAEs on residual-stream activations (Demircan: 18,000 representations, regularisation 1e-5, 30 epochs; a24). Correlate each latent with the TD error of a reference Q-learner. Lesion the best latent and compare with lesioning the least correlated one. Zou 2026: train probes for state value, zero the top 1% neurons, compare with random neurons (d09).

## 5. What holds up

**Replications and agreement.**
- The mixed model-free and model-based picture in humans is the best supported. The Daw task became standard and Doll 2012 collates follow-ups. But the sample opened here is N=17 (K01).
- Dopamine release as RPE-like in simple conditioning is not seriously challenged. Hart et al. 2014 (a11, abstract only): bidirectional RPE in rat accumbens voltammetry with symmetric scaling of positive and negative errors.
- LLM optimism asymmetry: found in one Claude model (Schubert) and again as confirmatory over disconfirmatory learning rates across four chat models in 1,200 runs (Hayes). Same research family (Schulz, Binz, Palminteri link). [E] with that caveat.
- Plain prompting fails at directed exploration in bandits: Krishnamurthy 2024 and EVOLvE 2024 agree. Reasoning models change it (Zhang 2025), but without a common metric.

**Failures, disputes and contradictions.**
- Sharpe 2020 vs Maes 2020 (K03): stimulation does not give cached value; silencing impairs second-order conditioning. Sufficiency versus necessity; one lab family; modest effects.
- Dabney 2020 vs Eshel 2016 (K04): diverse reversal points against a common response function. Dabney reanalysed related data; 5 mice, 40 cells. Avvisati 2024 (a22; 52 neurons, 30 mice; DLS-projecting group n=10) found extra structure by projection target.
- Original TD vs ramps (Kim 2020), contingency (Jeong 2022), inferred value (Sadacca 2016), backward blocking (Gershman and Uchida 2019), backward conditioning (Taira 2024). Each rival fits some data. Keep this wording: "classic TD fits only with extra state-space or ramp assumptions", not "classic TD fails" (critique).
- Bayer and Glimcher positive-only coding was contested later (K24); the later papers were not opened.
- Human reliability: fitted learning rates ICC .02 to .52 (bandit, N=69) and .01 to .71 (reversal, N=47), five weeks apart. Win-stay steadier (ICC .53 to .62). A fitted alpha describes one session, not a trait (K06).
- Pharmacology: Deserno 2021 is one study; model-agnostic tests partly null; no replication found (K26).
- Samples are small: 5 mice (Dabney), 7 to 8 mice per test (Jeong), 8 rats per group (Sharpe 2020), 17 humans (Daw).

**LLM-side moderators.**
- Reward label versus earlier attempts: Kwon 2026 shows the improvement comes mostly from showing earlier attempts. Flipped, random or removed rewards keep most of it (HumanEval+ and MBPP+: 50 episodes, 40 tasks, 3 seeds, Qwen-3.5-9B; ScienceWorld 10 episodes; six models). Reward-sensitive cells: 6 of 180 (3.3%) and 8 of 180 (4.4%). So Song 2026's 90% vs 49% on Game of 24 must be read next to this (K10 contested). Song's reward was the model's own 0 to 3 judgment.
- Failures: raw failed attempts in context are replayed (0.7% to 3.1%); a low label cuts this only to 2.5%. Reflexion: verbalised reflection with a real test signal helps (0.60 to 0.68); with no test signal 0.52 (K19). Position matters: best trajectory last raises its replay from 3.0% to 13.2% (d03).
- Negative reward: Monea found learning from negatives weak; positive-only and stochastic sampling work best; robust to 10% inverted rewards.
- Spurious reward: TR-ICRL says spurious rewards lower accuracy and later rounds degrade as context grows (d04).
- Model size: ICRL gain scales with size, 0.5B to 72B (Monea). External statistics hurt Gemma-2B (7.6 to 4.9) and Gemma-9B (10.5 to 4.1) but help Gemini Pro (EVOLvE, d11).
- Feedback framing: asymmetry gone for another agent's forced choices and reversed for counterfactual outcomes (Schubert).

**Interventions that worked.**
- Code-computed summary statistics or UCB-style guidance in bandits (Gemini Pro 45.5 to 60.0 multi-armed; 7.1 to 64.3 contextual; Krishnamurthy: only GPT-4 + CoT + hint + external summary worked).
- Observed forced-choice outcomes from another agent: regret 0.07 to 0.02.
- Chain of thought and step-back raised model-basedness (+64.59% and +118.59%, CogBench).
- Reflection plus a reliable test (Reflexion).
- Asking the model to estimate expected outcomes before choosing almost removed relative-value bias in GPT-4 Turbo and Llama-2-70B (Hayes, c04). Not retested in the later paper (c05). Single-source.

**Interventions that did not work, or were not found.**
- No prompt found that corrects alpha+ > alpha-.
- Explicit outcome-comparison text raised relative-value bias (.698 to .829) and lowered transfer accuracy (.734 vs .771; c05).
- Raw failed trajectories shown without reflection.
- Reward label alone (Kwon).

## 6. Language models

**Do they learn from reward in context?** Yes in simple settings. Claude v1.3 on a two-option slot machine: regret fell from 0.09 to 0.05 (t(199)=3.1, p=.002) with partial feedback, 50 runs, temperature 0 (c01). With full feedback, final regret 0.02 vs 0.07 for partial (t(191)=2.9, p=.004; 24 runs; c02). Banking77 with Qwen2.5-7B: 6.2% zero-shot to 72.2% with stochastic ICRL; Llama gains 28.6 to 74.4 points and Qwen 29.2 to 68.4 over zero-shot (Monea; b15).

**How do they learn?** Asymmetrically. Free-choice outcomes: alpha+ 0.87 vs alpha- 0.10 (c01). Across four chat models and five bandit tasks (1,200 runs), confirmatory rate 0.483 vs disconfirmatory 0.166 (c05). A small meta-RL transformer trained from scratch showed the same three signatures, so the authors read it as a property of idealised in-context learners (d08). CogBench (35 LLMs) found a strong optimism bias and high learning rates in almost all models; RLHF models were closer to human behaviour (c16).

**Relative value.** GPT-4 Turbo ~99% locally optimal by trial 5 (d=10.77), Llama-2-70B ~82% (d=1.46), GPT-3.5-Turbo 71%, Llama-2-13B 58% (not above chance). Bias showed in GPT-4 Turbo only when the payoff gap was small. A standard prompt gave a significant relative value bias in 2 of 5 tasks, explicit comparisons in 4 of 5 (c04, c05). Estimating expected outcomes first almost removed it (c04).

**Exploration.** GPT-3 had no directed exploration but beat humans on mean horizon regret (2.72 vs 3.24; Binz and Schulz 2023; c11). GPT-3.5, GPT-4 and Llama2 did not explore robustly in bandits; one configuration worked (c13). EVOLvE: UCB 90.6 to 96.4 win rate vs raw history 27.7 to 45.5 (c14). Reasoning versions of GPT, Gemini and DeepSeek raised directed exploration in a 2-armed task, some above human level; in 4-armed tasks directed-exploration coefficients stayed negative (Zhang 2025; c15).

**Model-free vs model-based.** GPT-3 showed signs of model-based reasoning on the two-step task (qualitative; c12). Parameters raise model-basedness (beta=0.481, z=4.2); CoT +64.59%, step-back +118.59% (c16). No reasoning-versus-base comparison found (K15 [S]; NeuroCogMap, d20, does not make it). Centaur (Llama 3.1 70B fine-tuned on Psych-101: 160 experiments, 60,092 participants, 10,681,650 choices) has NLL 0.44 vs 0.56 for domain models, but is worse on the horizon task (c17).

**Is there an RPE inside?** Demircan 2024 (Llama 3 70B): SAE latents track TD errors and Q-values; best r=0.58 in block 34; lesioning cuts next-state accuracy 24.3% to 18.9% (ceiling 25%); the model predicts a Q-learner's actions better with true than with randomised rewards (b13). Larger task: latents r >= 0.75 from block 40 (b11). Zou 2026: sparse value neurons in Qwen and Llama; zeroing the top 1% in layer 2 drops MATH500 75.2% to 37.0%, GSM8K 93.0 to 52.8, ARC 82.2 to 66.2; random neurons cost 0.6 to 1.8 points (d09). TD-error neurons as a process reward model for best-of-4: 72.3 average vs random 66.1, greedy 61.3, majority 65.0, P(true) 67.3 (d10). The authors call the causal evidence preliminary. Song 2026: 597 of 2,048 heads (29.1%) track reward labels (c09). All of this is correlational or lesion-only. No steering study and no replication of the SAE latent (critique gap 4).

**Using RPE ideas in agents.** Reflexion (verbal reinforcement; d06). ICRL (Song; Monea; Kwon; TR-ICRL). D-MEM and PreCoMem (memory gating). Wang 2024 (d05, abstract only): frontier models (gpt-4o, gpt-4o-mini, o1-preview, o1-mini) can discover specification gaming from in-context reflection on reward feedback alone. Safety note: a loop that shows the model a reward invites gaming.

**Net for LLMs.** Once earlier attempts are shown, a reward number adds little (Kwon). What helps: code-computed statistics, symmetric or counterfactual feedback, verbalised failures with a reliable test, and a planning step. That is a practical rule set, not a TD mechanism.

## 7. What our agent should take

Schema map: G = guardrails, S = states, O = operators, memory = section 5 of SCHEMA.md. The schema's O3 is "Decompose", not a retry loop. A retry loop with feedback lives in S4, S5 and S9. Some claims.jsonl entries say "O3 (iterate)"; here they are mapped to S4/S5/S9.

### Add now (established)

1. **Keep counts and success tallies in code, not in the model's head.** Code computes per-option counts, means and win rates and writes them into the prompt on repeated-choice or multi-attempt steps. Part: G5, S4, S7. [E] K13, K08. Evidence: c13, c14, c15, c23, d11, c01, c05. Caveat: bandit evidence only; small models were hurt (K23 is [S]), so apply with a strong model.
2. **Do not show raw failed attempts as examples. Show a one-line statement of what failed, located by code, plus the verifier output.** Part: S5 (already specified), S9 lesson. [E] K19. Evidence: d03, d06. Consistent with section 4b (unstructured self-reflection fails); the difference is a reliable external test signal.
3. **Do not let the model summarise outcomes of its own free choices unaided.** The asymmetry is limited to free choices, so a model-written tally is biased toward its own picks. Part: G2, G5. [E] K08. Evidence: c01, c02, c03, c05, d07. No prompt fix is known.
4. **Keep the verifier external. Do not rely on a model-judged score.** Part: G5, G8, G10. [E] K11, K19. Evidence: b15, b16, d01, d03, d06, d04. Song's self-judged gains are not evidence for a self-judged loop.
5. **Do not expect avoidance from negative-reward labels.** Keep best-so-far and positive examples in context. Part: G6, S5. [E] K11. Evidence: b15, b16, d03.

### Test first (not yet established)

6. **Reward label versus no label in a retry loop.** If the label is irrelevant, drop it and keep attempts plus verifier text. Part: S5, S9. [S] K18. Evidence: d01, d02.
7. **Reward-annotated multi-attempt loop vs best-of-N at equal tokens with a hard verifier.** Part: S3, S4, S5. [C] K10, K20. Evidence: c08, b17, d04, d01. Note: S3 requires fresh independent contexts (G4); an ICRL loop breaks that, so data must settle the conflict.
8. **Observed or counterfactual outcomes in the prompt** (what the other options would have returned). Part: S4, G2. [S] K21. Evidence: c02, c03, d07, d08.
9. **Planning or step-back step before choice in sequential tasks.** Part: S1, S3, S6. [S] K15. Evidence: c16, c12.
10. **Spread of estimates (low, middle, high) per option for repeated-choice items.** Part: memory, S0 class record. [C] K04. Evidence: a13, b08, b25, a22, a12.
11. **Surprise-gated memory writes (lessons).** Part: memory, S9. [S] K16. Evidence: c18, d12, d13. Score single-hop and multi-hop separately.
12. **Score arms by behavioural indices (win-stay, regret), not fitted learning rates.** Part: G7, bench scoring. [S] K06. Evidence: b10.
13. **"Estimate the expected outcome of each option first" before a choice from repeated feedback; avoid explicit side-by-side outcome comparison text.** Part: S1, S3. [S] K09. Evidence: c04, c05.

## 8. Concrete tests on our bench

All arms get the same total token budget (G7), counting setup. Use at least 3 seeds; report mean and interval.

| # | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 | Verifiable retry tasks (ARC-like with held-out check; code with unit tests) | (a) true score label + attempt, (b) flipped label + attempt, (c) attempt only, (d) no history | Pass rate on held-out check | (a) about (c) > (d); label effect under 2 points (Kwon: 3.3 to 4.4% of cells) |
| T2 | Same items | (a) raw failed attempts, (b) one-line failure note from verifier output, (c) nothing | Pass rate; repeat-of-failed-answer rate | (b) > (a) and (c); (a) shows replay near 3% vs 0.7% |
| T3 | Same items | ICRL-style one-context loop vs 4 to 16 independent samples + code selection | Pass rate at equal tokens | Unknown; best-of-N may win with a hard verifier. Song's 90 vs 49 is a self-judged case |
| T4 | Text bandit (2 to 10 arms, 100 to 200 pulls) | (a) raw history, (b) code-computed counts and means, (c) UCB-style hint | Regret; share of pulls on best arm; suffix-failure rate | (b), (c) > (a) with a strong model; (a) may win for a small model |
| T5 | Text bandit with partial feedback | (a) own outcomes only, (b) plus counterfactual outcomes, (c) plus another agent's forced-choice outcomes | Regret; fitted alpha+ / alpha- gap | Regret 0.07 to about 0.02 in (b) or (c) |
| T6 | Same bandit | Instruction "weight failures equally" vs none | Regret; alpha- / alpha+ | Expected null (no known prompt fix); a gain would be new |
| T7 | Two-step text task | (a) plain, (b) explicit transition table in prompt, (c) step-back planning | Stay-probability reward x transition interaction; reward | (b), (c) raise the interaction |
| T8 | Long multi-session QA | write-all memory vs surprise gate vs random gate at equal tokens | F1 split into single-hop and multi-hop | Gate saves tokens; single-hop may drop (D-MEM) |
| T9 | Bandit with relative payoff framing | (a) plain, (b) explicit comparisons, (c) estimate-expected-outcome-first | Choice accuracy on absolute-best option | (b) lowers accuracy, (c) raises it |
| T10 | Bandit with drifting payoffs | one mean per arm vs low/mid/high estimates | Regret; calibration | Small, unproven gain |

## 9. What does not transfer, and why

- **The dopamine anatomy and firing code.** Our agent has no neurons to record. Burst, dip, ramps and projection-target findings (Schultz, Bayer and Glimcher, Kim, Jeong, Avvisati) change no prompt.
- **Weight updates.** TD learning changes stored values. A prompted LLM changes nothing between calls. In-context RL conditions on earlier text, which is a different mechanism. Wang 2025 shows a forward-pass TD is possible in theory, only in small linear models.
- **Hidden-state probes.** Demircan and Zou need activations. A black-box API run cannot do this (K22). Note only.
- **Human pharmacology and fMRI.** Levodopa and ventral striatum BOLD say nothing about a scaffold.
- **Fitted learning rates as traits.** Human ICC .02 to .52 means a rate fitted on one session does not predict the next (K06).
- **Self-judged reward.** Song's Game of 24 reward is the model's own 0 to 3 score. G8 and G10 already say model judgment is not evidence.
- **Model-based versus model-free as a fixed trait.** In LLMs it moves with size and prompt (CogBench), so it is a setting, not a property to diagnose.
- **Memory gating as RPE.** D-MEM's gate is an embedding surprise times utility, not a reward error. The word "dopamine" adds nothing; judge it as a surprise gate.

## 10. Open questions

1. Does a reward-annotated loop beat best-of-N at equal tokens when the reward comes from a hard external verifier? No matched-token test found. TR-ICRL uses a majority-vote pseudo-label.
2. Is there a prompt or scaffold rule that corrects alpha+ > alpha-, and does fixing it lower regret on current models? The framing result is from Claude v1.3 at temperature 0 only.
3. Is the Demircan TD latent replicated in other open models, and does steering it change behaviour? Zou 2026 converges with a different method and preliminary causal evidence.
4. Do externally computed statistics help in multi-step reasoning scaffolds, not only bandits?
5. Do surprise-gated memories beat write-all at equal tokens on multi-session tasks, and does single-hop recall systematically drop? D-MEM says yes; PreCoMem says no. Neither has a write-all baseline at equal tokens in the main table. ReSuME was not found.
6. Do reasoning-trained LLMs show more model-based behaviour in the two-step task than base models at equal tokens? Only the CogBench CoT result exists.
7. What exactly did the 1990s monkey recordings show (neuron counts, effect sizes)? Schultz 1993 and Mirenowicz and Schultz 1994 full text were not read.
8. What does the body text of Gershman et al. 2024 list as the main failures of RPE? Only abstract and figure titles were read.
9. Other levodopa studies were not opened; no replication of Deserno 2021.
10. Does the reward label matter for frontier models in a verifiable loop? Kwon used six small models, plus GPT-5-mini and GPT-5-nano in part.
11. Is dopamine diversity (Dabney) robust to projection target and more animals? Avvisati 2024 says structure depends on target.
12. Does the expected-outcome-first prompt (Hayes 2024) still work on current models? It was not retested in the later paper.

## 11. Sources

[V] = opened and read this session (full text or PDF/HTML); [M] = snippet or abstract only. Ids are evidence lines.

- [M] Mirenowicz and Schultz (1994) Importance of unpredictability for reward responses in primate dopamine neurons (1994). https://pubmed.ncbi.nlm.nih.gov/7983508/  (d15)
- [M] Montague, Dayan, Sejnowski (1996) A framework for mesencephalic dopamine systems based on predictive Hebbian learning (1996). https://doi.org/10.1523/jneurosci.16-05-01936.1996  (a01)
- [M] Schultz, Dayan, Montague (1997) A neural substrate of prediction and reward (1997). https://doi.org/10.1126/science.275.5306.1593  (a02, a26, b20)
- [M] Schultz, Dayan, Montague (1997) A neural substrate of prediction and reward (1997). https://www.science.org/doi/10.1126/science.275.5306.1593  (c20)
- [M] Schultz, Dayan, Montague (1997) A neural substrate of prediction and reward (1997). https://pubmed.ncbi.nlm.nih.gov/9054347/  (d16)
- [M] Nakahara et al. (2004) Dopamine neurons can represent context-dependent prediction error (2004). https://doi.org/10.1016/s0896-6273(03)00869-9  (a05)
- [M] Bayer and Glimcher (2005) Midbrain dopamine neurons encode a quantitative reward prediction error signal (2005). https://doi.org/10.1016/j.neuron.2005.05.020  (a03)
- [V] Bayer and Glimcher (2005) Midbrain dopamine neurons encode a quantitative reward prediction error signal (2005). https://pmc.ncbi.nlm.nih.gov/articles/PMC1564381/  (d14)
- [M] Tobler, Fiorillo, Schultz (2005) Adaptive coding of reward value by dopamine neurons (2005). https://doi.org/10.1126/science.1105370  (a04)
- [V] Daw, Gershman, Seymour, Dayan, Dolan (2011) Model-based influences on humans' choices and striatal prediction errors (2011). https://pmc.ncbi.nlm.nih.gov/articles/PMC3077926/  (a06, a07, a08, b01, b02)
- [V] Doll, Simon, Daw (2012) The ubiquity of model-based reinforcement learning (2012). https://pmc.ncbi.nlm.nih.gov/articles/PMC3513648/  (a09, a10, b03)
- [M] Hart, Rutledge, Glimcher, Phillips (2014) Phasic dopamine release in the rat nucleus accumbens symmetrically encodes a reward prediction err (2014). https://pmc.ncbi.nlm.nih.gov/articles/PMC3891951/  (a11)
- [M] Wilson, Geana, White, Ludvig, Cohen (2014) Humans use directed and random exploration to solve the explore-exploit dilemma (2014). https://doi.org/10.1037/a0038199  (c21)
- [V] Eshel, Tian, Bukwich, Uchida (2016) Dopamine neurons share common response function for reward prediction error (2016). https://pmc.ncbi.nlm.nih.gov/articles/PMC4767554/  (a12)
- [V] Sadacca, Jones, Schoenbaum (2016, eLife) Midbrain dopamine neurons compute inferred and cached value prediction errors in a common framework (2016). https://pmc.ncbi.nlm.nih.gov/articles/PMC4805544/  (b04)
- [V] Sharpe, Chang, Liu, et al. (2017) Dopamine transients are sufficient and necessary for acquisition of model-based associations (2017). https://pmc.ncbi.nlm.nih.gov/articles/PMC5413864/  (a15, a16)
- [V] Gershman and Uchida (2019) Believing in dopamine (2019). https://pmc.ncbi.nlm.nih.gov/articles/PMC7472313/  (b19, d18)
- [V] Dabney, Kurth-Nelson, Uchida, et al. (2020) A distributional code for value in dopamine-based reinforcement learning (2020). https://pmc.ncbi.nlm.nih.gov/articles/PMC7476215/  (a13, a14, b08, b25)
- [V] Kim, Malik, Mikhael, et al. (2020) A unified framework for dopamine signals across timescales (2020). https://pmc.ncbi.nlm.nih.gov/articles/PMC7736562/  (a20)
- [V] Maes, Sharpe, Usypchuk, et al. (2020) Causal evidence supporting the proposal that dopamine transients function as temporal difference predi (2020). https://pmc.ncbi.nlm.nih.gov/articles/PMC7007380/  (a18, a19, b06)
- [V] Sharpe, Batchelor, Mueller, et al. (2020) Dopamine transients do not act as model-free prediction errors during associative learning (2020). https://pmc.ncbi.nlm.nih.gov/articles/PMC6949299/  (a17, a27, b05, b24)
- [M] Alexander and Gershman (2021) Representation learning with reward prediction errors (2021). https://arxiv.org/abs/2108.12402  (b23)
- [V] Deserno, Moran, Michely, et al. (2021) Dopamine enhances model-free credit assignment through boosting of retrospective model-based inferenc (2021). https://pmc.ncbi.nlm.nih.gov/articles/PMC8758138/  (a23, d19)
- [V] Jeong, Taylor, Floeder, et al. (2022) Mesolimbic dopamine release conveys causal associations (2022). https://pmc.ncbi.nlm.nih.gov/articles/PMC9910357/  (a21, b07)
- [M] Palminteri and Lebreton (2022) The computational roots of positivity and confirmation biases in reinforcement learning (2022). https://doi.org/10.1016/j.tics.2022.04.005  (c22)
- [V] Binz, Schulz (2023) Using cognitive psychology to understand GPT-3 (2023). https://arxiv.org/abs/2206.14576  (c11, c12)
- [M] Le et al. (2023) Beyond surprise: improving exploration through surprise novelty (2023). https://arxiv.org/abs/2308.04836  (c25)
- [V] Shinn et al. (2023) Reflexion: language agents with verbal reinforcement learning (2023). https://arxiv.org/abs/2303.11366  (c19, d06)
- [V] Avvisati, Kaufmann, Young, et al. (2024) Distributional coding of associative learning in discrete populations of midbrain dopamine neurons (2024). https://pmc.ncbi.nlm.nih.gov/articles/PMC7616095/  (a22)
- [V] Coda-Forno, Binz, Wang, Schulz (2024) CogBench: a large language model walks into a psychology lab (2024). https://arxiv.org/abs/2402.18225  (c16)
- [V] Demircan, Saanum, Jagadish, Binz, Schulz (2024) Sparse autoencoders reveal temporal difference learning in large language models (2024). https://arxiv.org/abs/2410.01280  (a24, a25, b11, b12, b13, b14, c06)
- [M] Gershman et al. (2024) Explaining dopamine through prediction errors and beyond (2024). https://www.nature.com/articles/s41593-024-01705-4  (d17)
- [M] Gershman et al. (2024, Nat Neurosci) Explaining dopamine through prediction errors and beyond (2024). https://www.nature.com/articles/s41593-023-01567-2  (b18)
- [V] Hayes, Yax, Palminteri (2024) Relative value biases in large language models (2024). https://arxiv.org/abs/2401.14530  (c04)
- [V] Hayes, Yax, Palminteri (2024/2025) Large language models are biased reinforcement learners (relative value encoding, multi-task) (2024). https://arxiv.org/html/2405.11422v1  (c05)
- [M] Jacob et al. (2024, Nat Neurosci) dopamine RPE and perceived locus of control (2024). https://www.nature.com/search?q=dopamine+locus+of+control  (b22)
- [V] Krishnamurthy, Harris, Foster, Zhang, Slivkins (2024) Can large language models explore in-context? (2024). https://arxiv.org/abs/2403.15371  (c13)
- [V] Nie et al. (2024/2025) EVOLvE: evaluating and optimizing LLMs for in-context exploration (BanditBench) (2024). https://arxiv.org/abs/2410.06238  (c14, d11)
- [V] Schubert, Jagadish, Binz, Schulz (2024) In-context learning agents are asymmetric belief updaters (2024). https://arxiv.org/abs/2402.03969  (c01, c02, c03, d07, d08)
- [V] Taira et al. (2024, J Neurosci) Dopamine release in the nucleus accumbens core encodes the general excitatory components of learning (2024). https://pmc.ncbi.nlm.nih.gov/articles/PMC11358529  (b09, b26)
- [V] Test-retest reliability of reinforcement learning parameters (Behav Res Methods 2024) (2024). https://pmc.ncbi.nlm.nih.gov/articles/PMC11289054/  (b10)
- [M] The Transmitter (2024) Does a new theory of dopamine replace the classic model? (2024). https://www.thetransmitter.org/dopamine/does-a-new-theory-of-dopamine-replace-the-classic-model/  (b21)
- [M] Wang et al. (2024) Honesty to Subterfuge: In-Context Reinforcement Learning Can Make Honest Models Reward Hack (2024). https://arxiv.org/abs/2410.06491  (d05)
- [V] Binz et al. (2025) A foundation model to predict and capture human cognition (Centaur) (2025). https://arxiv.org/abs/2410.20268  (c17)
- [V] Monea, Bosselut, Brantley, Artzi (2025, COLM) LLMs are in-context bandit reinforcement learners (2025). https://arxiv.org/abs/2410.05362  (b15, b16)
- [V] Reward Is Enough: LLMs are in-context reinforcement learners (arXiv 2506.06303) (2025). https://arxiv.org/abs/2506.06303  (b17, c08, c09, c10)
- [V] Wang, Blaser, Daneshmand, Zhang (2025) Transformers can learn temporal difference methods for in-context reinforcement learning (2025). https://arxiv.org/abs/2405.13861  (c07)
- [V] Zhang, Wang, Chen, Mansur, Sarhangian (2025) Comparing exploration-exploitation strategies of LLMs and humans on standard multi-armed bandit (2025). https://arxiv.org/abs/2505.09901  (c15, c23)
- [V] Jiang, Zuo et al. (2026) TR-ICRL: Test-Time Rethinking for In-Context Reinforcement Learning (2026). https://arxiv.org/abs/2604.00438  (d04)
- [V] Kwon, Koh, Baek, Bae, Kim (2026) Do LLMs Learn from Rewards in Context? Rethinking the role of reward in In-Context RL (2026). https://arxiv.org/abs/2610.11152  (d01, d02, d03)
- [V] NeuroCogMap (2026) Reveals Cognitive Organization of Large Language Models (2026). https://arxiv.org/abs/2607.00397  (d20)
- [M] Other 2026 agent-memory work gated by surprise or prediction error (ReSuME, PreCoMem, belief-based memory 2606.22030) (2026). https://arxiv.org/abs/2606.22030  (c24)
- [V] PreCoMem (2026) Predictive Cognitive Memory for Self-Evolving Long-Term Dialogue Agents (2026). https://arxiv.org/abs/2610.29467  (d13)
- [V] Song and Xin (2026) D-MEM: dopamine-gated agentic memory via reward prediction error routing (2026). https://arxiv.org/abs/2603.14597  (c18, d12)
- [V] Zou group (2026) Sparse Reward Subsystem in Large Language Models, value neurons (2026). https://arxiv.org/abs/2602.00986  (d09, d10)

## Source audit (2026-11-20)

Fresh auditors re-opened the sources of 5 established claims: 4 confirmed as written, 1 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **B02.02-K01** (now single-source: the sources are not independent). Daw 2011 confirms N=17 and median model-free weight 61%, but the other source (Doll, Simon, Daw 2012) is a review from the same lab with no new data, and it presents the model-based interpretation as partly unresolved (some effects may be model-free generalization); the three Daw entries are one paper.
- **B02.02-K25** (now single-source: only one opened source, code check).
