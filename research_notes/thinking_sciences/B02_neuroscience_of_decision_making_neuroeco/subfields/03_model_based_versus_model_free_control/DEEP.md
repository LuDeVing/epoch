# Model-based versus model-free control: deep document

*Subfield B02.03. Built from evidence_a-d.jsonl (a01-a28, b01-b28, c01-c29, d01-d20), claims.jsonl (K01-K29) and critique.md in this folder. Evidence ids are quoted in brackets. Search engines were out of quota in the last pass, so recall for LLM gate studies is limited (see section 10).*

## 1. What it is

Two ways to choose an action.

- **Model-free (cached, habit).** The agent stores a value for each action from past reward. Choice is a lookup. It is fast and cheap. It is wrong when the world has changed since the value was stored.
- **Model-based (planned, goal-directed).** The agent keeps a model of the world (what leads to what, what is worth what) and searches it at choice time. It is slow and costly. It adapts at once when the world changes.

The subfield asks one question: **when should a mind pay for planning, and how does it decide?** Three answers exist.

1. Trust whichever system is more certain about value (Daw, Niv and Dayan 2005) [a01, b01].
2. Plan only when the value of perfect information exceeds the cost of the delay, where cost = average reward rate x deliberation time (Keramati, Dezfouli and Piray 2011) [a10, b03, c20].
3. Plan a few steps, then plug in cached values (plan-until-habit; Keramati et al. 2016) [a19, b04, d05].

The standard human test is the **two-step task** (Daw et al. 2011) [a05]. The standard animal test is **outcome devaluation** (Adams and Dickinson 1981; Dickinson 1985) [a23, a24; not opened].

Why it matters for our agent: S0 (the gate) must choose a mode (direct, short reason, step-by-step, checked, open). The cleanest rule from this field is: **use the slow path only when the expected gain exceeds its cost, and price the cost in tokens and time.** The field also supplies warnings. Cached answers go stale when the task changes. The standard human measure is contested. The dual-system split itself may be too coarse.

Status in one paragraph. The theory is simulation only. The human evidence that people trade effort against payoff is good (Kool 2016, 2017, Patzelt 2019). The human evidence for a stable "hybrid" mix is contested (Feher da Silva and Hare 2020). No LLM study tests the Keramati rule itself. LLM studies do show, with measured numbers, that always-slow is not best and that cheap gates give small gains.

## 2. History and theories in depth

### 2.1 Animal roots

- **Adams and Dickinson 1981** [a24, not opened]. Rats trained to press a lever for a pellet, then given the pellet paired with illness, pressed less in extinction. Behaviour used a representation of the outcome.
- **Dickinson 1985** [a23, not opened]. Goal-directed actions depend on the action-outcome link and the current outcome value. Habits are stimulus-response links that ignore outcome value. Extensive training and ratio versus interval schedules shift behaviour toward habit.
- **Sutton and Barto 1998; Sutton 1990 (Dyna)** [a25, not opened]. Model-free methods (TD, Q-learning, SARSA) learn cached values. Model-based methods learn transition and reward models and plan. Dyna mixes real experience with planning updates from a learned model.

### 2.2 Daw, Niv and Dayan 2005: arbitration by uncertainty

[a01-a04, b01; opened; theory with simulation only]

- Two controllers. A prefrontal tree search (model-based) and a dorsolateral striatal TD cache (model-free). Each keeps a Bayesian posterior over action values.
- The agent trusts the controller with the lower posterior variance for each action.
- Why each is uncertain [a02]. The tree is data-efficient: one observation updates values everywhere at once. The cache is slow because bootstrapping delays propagation. So the tree is more certain early. The tree also adds "computational noise" (an assumed term, not measured). So late in training, for actions far from reward, the cache wins. For the action nearest reward the tree stays more certain.
- Predictions [a04]. Over-training and task simplicity favour the cache. Closeness to reward and frequent reversals favour search. Unexpected task change restores tree control. A two-action, two-outcome task splits experience over more states, so the cache is less data-efficient and tree control persists [a03].
- Simulation sizes: Fig 5 means over 250 runs, Fig 6 over 1000 runs [a01].
- Limit. It does not price the time or effort of planning. Neural claims are suggestive only [a04].

### 2.3 Daw et al. 2011: the two-step task

[a05-a08, b02; opened; N = 17 fMRI]

- Stage 1: choose between two options. Each leads to one of two stage-2 states, with a common transition (0.7) and a rare one (0.3). Stage 2 pays with probabilities that drift as Gaussian random walks (SD 0.025, bounds 0.25 to 0.75). 201 trials per person, 50 practice trials.
- Model-free predicts "repeat the stage-1 choice after a reward, whatever the transition." Model-based predicts a cross-over: repeat after reward via a common transition, or after no reward via a rare transition.
- Behaviour. Reward main effect p < 1e-8. Reward x transition p < 5e-5. Transition main effect p = .5. Perseveration p < 5e-12. The reward effect was positive in 14 of 17 people; the interaction in 10 of 17 [a06].
- Hybrid model. Value = w x model-based + (1 - w) x model-free (TD lambda). Median w = 0.39 (IQR .29 to .59). Hybrid -LL 3364 vs TD-only 3418 (log Bayes factor 30.0) vs model-based-only 3501 (82.4). Exceedance probability .92 [a07]. The critique re-opened these numbers and confirmed them.
- fMRI. Ventral striatal prediction error carries both model-free and model-based information. Its model-based part tracks each person's w (r^2 = .28, p = .027 in right ventral striatum) [a08].
- Companion: Gläscher et al. 2010 [a09]. A separate state prediction error (SPE) in lateral PFC and posterior parietal cortex (N = 18; SPE left lateral PFC Z = 5.62; hybrid AIC 2414.56 vs SARSA 2439.88).

### 2.4 Keramati, Dezfouli and Piray 2011: value of information vs time cost

[a10-a12, b03, c20; opened; simulation only]

- Rule. Run the goal-directed system for an action only if VPI (value of perfect information about that action, computed from the habitual system's own uncertainty) exceeds the cost of deliberation = average reward rate x deliberation time.
- Habitual system = Kalman-style TD with a distribution over each Q value. VPI has a closed form (Dearden et al.). Average reward is an exponentially weighted moving average [a10].
- Simulated results. Moderate training (40 trials) gives about a 50% fall in responding after devaluation. Extensive training loses it. In a concurrent schedule with two equal levers, VPI stays above cost after 240 trials and goal-directed control stays. In reversal learning, RT is higher while searching and rises again after reversal. After training, deliberation does not depend on the number of choices [a11].
- Neural mapping [a12]. Phasic dopamine trains habits; tonic dopamine carries the average reward rate that sets the cost of thinking. This is a hypothesis.
- Contrast with Daw 2005 [a12]. Daw predicts a switch to caching with two same-outcome choices. Keramati predicts they stay goal-directed.
- Limits. A fixed non-deliberation time had to be added to match RTs. Linear versus logarithmic mismatch with Hick's law. No fit to individual data [a11]. Assumes VPI is computable, "which is the hard part" [b03].
- Extension: Sezener, Dezfouli and Keramati 2019 [b05, c21, c22]. Expand a tree node when the value of information of the expansion beats its time cost. Leaf values may be cached. Gives depth and direction of search. Gate cost is small because the rule uses quantities already in working memory. Simulation only.

### 2.5 Keramati et al. 2016: plan-until-habit

[a19, b04, d05; opened]

- Three-step task, about 400 trials, 70/30 transitions. Depth k = 0 (pure habit), 1 (plan until a state with trusted cached value), 2 (full plan).
- Groups: high-resource n = 15 (2 s to respond) and low-resource n = 15 (700 ms).
- High-resource group: pure planning effect after rewarded and unrewarded trials, both P < 0.001 (Wilcoxon). Plan-until-habit effect only after unrewarded trials (P < 0.002); after rewarded trials P = 0.073.
- Time pressure: planning effect weaker in the low-resource group (rewarded P = 0.011, unrewarded P = 0.027); plug-in stronger after rewarded trials [b04].
- No larger replication in 137 citing records (Europe PMC scan, 2026-10-31) [d05, d07].

### 2.6 Challenges to the hybrid picture

- **Akam, Costa and Dayan 2015** [a13, a14, b10]. Simulation. Model-free agents with latent states, history or "reward-as-cue" mimic the model-based stay signature. The task has a design conflict: transitions must be random to tell strategies apart, yet determinism is needed for planning to pay off. "Sophisticated habits" exist.
- **Kool, Cushman and Gershman 2016** [a15, a16, b06]. In the original task, model-based control earns almost no extra reward (predicted reward 0.52 at w = 0, up only 0.002 at w = 1). A redesigned task where planning pays: 0.58 at w = 0 rising to 1.25 at w = 1. Median w 0.27 (Daw task) vs 0.48 (novel task), z = 3.31, p < .001. Sample: 406 online (199 novel, 207 Daw), 381 model-fit. Combining the five design changes raised the trade-off strength about 230 times.
- **Feher da Silva and Hare 2020** [b09, c25, d01]. With story-based instructions and a comprehension quiz, people look mostly model-based. Median w (IQR): Daw 2011 N = 17: 0.39 (.29-.59). Kool 2016 re-analysis N = 206: 0.24 (0.00-0.68). Spaceship N = 21: 0.78 (.61-.91). Magic carpet N = 24: 0.79 (.51-.85). Simulated purely model-based agent with correct task model: 0.94 (95% range .74-1.00). Same agent with an "unlucky symbol" wrong model: 0.36 (.24-.48). TDLR wrong-model agent: 0.80. So a hybrid label can come from task misunderstanding. All six headline numbers were confirmed on the bioRxiv v1 PDF; the peer-reviewed version was seen at abstract level.
- **Castro-Rodrigues et al. 2022** [c23]. N = 204 (109 healthy, 46 OCD, 49 other). Transitions 80/20. With minimal instruction, most act model-free; model-based control rises sharply when task structure is explained, in all groups.
- **Action chunks and habit without values.** Dezfouli and Balleine 2013 [b28, not opened]: habits as chunked sequences. Miller, Shenhav and Ludvig 2019 [b14]: habits as direct action strengthening, no value cache. "Model-free RL or action sequences" (2019, authors not verified) [c24]: chunks can mimic model-free reinforcement; both operate.
- **Collins and Cockburn 2020** [b15]. The MB/MF split blurs working memory, episodic memory and other processes. Re-aim questions at components.
- **Dayan and Berridge 2014** [a22]. Pavlovian prediction can also be model-based, so the split reaches beyond instrumental choice.

### 2.7 Moderators and individual differences

- Incentives and stakes (section 3).
- Load and stress: Otto et al. 2013 (Stroop load) [d06]; Otto, Raio et al. 2013 (cold pressor) [b12].
- Compulsivity: Gillan et al. 2016 [a20, b11]. Habit protection: Gillan, Otto, Phelps and Daw 2015 [a21, b13].
- Development: Smid et al. 2023 [b17] (N = 69 aged 6 to 13; metacontrol varies widely); Decker et al. 2016 [b27, not opened].
- Offline replay: Momennejad et al. 2018 [b16] (abstract-level only). Planning can happen away from decision time.

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Humans show both model-free and model-based signatures in the two-step task | Reward p < 1e-8; reward x transition p < 5e-5; reward effect positive 14/17, interaction positive 10/17; N = 17 | Daw 2011 [a06] | Contested (next rows) |
| A hybrid model fits better than either pure system | Median w 0.39 (IQR .29-.59); -LL hybrid 3364 vs TD 3418 vs MB-only 3501; log BF 30.0 and 82.4; exceedance .92 | Daw 2011 [a07] | Contested |
| With story instructions people are mostly model-based | Median w 0.78 (N = 21), 0.79 (N = 24) vs 0.39 (N = 17), 0.24 (N = 206); simulated MB agent 0.94 right model, 0.36 wrong model | Feher da Silva and Hare 2020 [b09, d01] | Established as a threat to the hybrid reading |
| Minimal instruction gives model-free behaviour; explanation raises model-based control | N = 204; effect in healthy, OCD and other groups | Castro-Rodrigues 2022 [c23] | Single group of authors |
| In the original task planning earns almost nothing | Reward 0.52 at w = 0, +0.002 at w = 1; redesigned task 0.58 to 1.25 | Kool 2016 [a16] | Single source |
| Redesigned task raises model-based use | Median w 0.27 vs 0.48, z = 3.31, p < .001; N = 406 | Kool 2016 [a15] | Single source |
| Stakes raise model-based control when planning pays | Exp 1 N = 98, w 0.76 vs 0.54, t(97) = 4.67, d = 0.47; replication N = 93, w 0.62 vs 0.51, d = 0.29 | Kool 2017 [d02] | Established |
| No stakes effect when planning gives no accuracy gain | Exp 2 N = 100, w 0.39 vs 0.41, d = -0.04; behavioural index d = -0.07; between-experiment d = 0.51 | Kool 2017 [d03] | Established (payoff-gap logic) |
| Incentives boost model-based control at scale | N = 839, t(838) = 10.21, d = 0.35 | Patzelt 2019 [b08] | Established (incentives, not a strict replication) |
| Learned regulation by how often planning pays | n = 140 | 2026 Europe PMC abstract [d04] | Single source, abstract only |
| Time pressure makes planning shallower | n = 15 vs 15; 700 ms vs 2 s; plan-until-habit after unrewarded P < 0.002 | Keramati 2016 [a19, d05] | Single source |
| Load reduces model-based signature | Exp 1 N = 25 analysed of 43; Lag 2 weight t(24) = 2.94, p < .01 | Otto 2013 [d06] | Single source plus one stress study |
| Stress and low working memory cut model-based control | N = 48 analysed of 56; cortisol F = 19.99; OSPAN x cortisol x reward x transition P < .01 | Otto, Raio 2013 [b12] | Single source, small N |
| Model-based use protects against habits | Exp 1 N = 90, three-way interaction p = .003; Exp 2 N = 95, p < .001 | Gillan, Otto 2015 [a21, b13] | Single source (one conceptual replication) |
| Model-based deficit tracks a compulsivity dimension | Exp 1 N = 548 OCD beta -0.040 (p = .049); Exp 2 N = 1413 eating disorders -0.037, impulsivity -0.034, OCD -0.026 | Gillan 2016 [a20, b11] | Single source, small effects |
| Model-free agents can mimic the MB signature | Simulations: latent state, history, reward-as-cue | Akam 2015 [a13, b10] | Established |
| Always-plan agents are not best | Crafter, Llama-3.3-70B, 100 seeds: never 0.343 (560 tokens), every 4 steps 0.379 (11,511), always 0.349 (38,836) | Paglieri 2025 [d14] | Established |
| Trained 8B planner matches 70B zero-shot with far fewer tokens | 0.387 vs 0.379; 1,714 vs 11,510 output tokens (85% fewer); SFT only 0.343 | Paglieri 2025 [c06, d14] | Single source for the training result |
| Reasoning models overthink easy items | 1,953% more tokens on "2 plus 3"; first correct solution at 39/901 tokens (4.3%) | Chen 2024 [b21] | Established |
| Learned think/no-think routing cuts length with no loss | 1.5B: -53.0% length, +2.4 acc; 7B: -40.1%, +2.3; lambda 0.1: -64.5%, -0.5; NoThinking share 86.9/76.8/40.4% (GSM8K/MATH500/AIME) | AdaptThink 2025 [c13] | Established with Thinkless [c14] |
| Confidence gate gives about +1 point | 47.90 to 48.92 (+1.02) at 8.20% slow calls; random -1.14; log-prob +0.32; logit gap -0.06; utility 0.4731 vs always-fast 0.4789 | He and Feng 2026 [d09, c12] | Single source (one model pair) |
| Sample-vote gate beats verifier gate on GSM8k | Vote 0.917 at cost 0.235 vs GPT-3.5 verifier 0.884 at 0.253 | Yue 2024 [d10] | Single source |
| Sample agreement as a stopping rule | Up to 7.9x fewer samples, accuracy drop under 0.1%, 17 datasets, 3 LLMs | Aggarwal 2023 [d12] | Single source |
| Rule-triggered fast/slow agent | ScienceWorld 84.7 vs ReAct 36.4, Reflexion 45.3; tokens/action 757 vs 1,971 and 2,983; Swift-only 49.22 vs 62.22 with slow pass (gpt-3.5) | SwiftSage 2023 [b26, c15, d16] | Single source |
| Planning pays in one task, not in another | GPT-4o Event-QA 47.5 to 67.5% at 8 s to 317 s; CMV one-shot best (60 examples per task) | Ghoshal 2026 [c09] | Single source, small |
| Test-time compute pays by difficulty and load | Easy and medium bins win; hardest bin little gain; pretraining wins at R = 22 | Snell 2024 [d13] | Established |
| Value-guided partial search beats voting at equal generations | 39.8 vs 31.6 (majority) vs 37.0 (weighted vote), N = 256; 12% shorter; value model 0.024% of FLOPs | VGS 2025 [d17] | Single source |
| Pattern answers persist after a task change | GSM-NoOp: Phi-3-mini over -65%, o1-preview -17.5, o1-mini -29.1; Ullman P(chocolate) = 95% for transparent bag | Mirzadeh 2025, Wu 2024, Ullman 2023 [d18-d20] | Established as analogy only |

## 4. Mechanisms and models

### 4.1 Hybrid TD model (Daw 2011) [a07]

- Keep a model-free value Q_MF(s1, a) learned by TD(lambda) with learning rate alpha1, and a model-based value computed from the learned transition table and stage-2 values: Q_MB(s1, a) = sum over s2 of P(s2 | s1, a) x max_a2 Q(s2, a2).
- Net value Q_net = w x Q_MB + (1 - w) x Q_MF.
- Choice is softmax with inverse temperature beta and a perseveration bonus p for repeating the last action.
- Fitted medians in Daw 2011: w 0.39, lambda 0.57, alpha1 0.54, beta1 5.19, p 0.11.
- Analysis shortcut: logistic regression of "stay" on previous reward x previous transition. Model-free = reward main effect. Model-based = reward x transition interaction. Akam 2015 shows this is not diagnostic for all agents [a13].

### 4.2 Uncertainty arbitration (Daw 2005) [a01-a03]

1. For each action keep a mean and variance of value under each controller.
2. Cache variance: starts at the prior and shrinks as TD updates arrive. Updates are slow because values propagate by bootstrapping.
3. Tree variance: shrinks fast (one observation updates many states), but add a fixed computational-noise term.
4. Pick the controller with lower variance, per action.
5. Result: tree early, cache late for distal actions; tree persists when experience is split across many states.

### 4.3 Value-of-information arbitration (Keramati 2011) [a10, b03]

1. Habitual system keeps a distribution over each Q(s, a), for example Gaussian from a Kalman filter.
2. For the current state compute VPI for each candidate action: the expected improvement in value if the true Q were revealed, given the current distributions. Closed form for Gaussians (Dearden et al.).
3. Keep a running average reward rate R_bar (exponentially weighted).
4. Estimate deliberation time tau (the time or steps the planner would take).
5. Cost = R_bar x tau.
6. If VPI > cost: run the planner, act on its answer, and use it to update the cache. Else act on the cache.
7. As caches become sharp, VPI falls and the agent moves to habit. When R_bar is high (time is worth more), habit takes over sooner.

Engineer's note. Step 2 needs a calibrated posterior over each cached value. An LLM has none. Section 7 gives proxies (sample disagreement) and says which are untested.

### 4.4 Depth-limited planning with cache plug-in (Keramati 2016, Sezener 2019) [a19, b05]

1. Expand the search tree one level at a time.
2. At each frontier node compare the VOI of expanding it with the time cost of the expansion.
3. When VOI is below cost, stop and use the cached value of the node as its leaf value.
4. Time pressure raises the cost term, so the tree is shallower and more leaves are cached.
5. Gate cost is small because the rule needs only values already in working memory [c22].

### 4.5 LLM agents that already implement the same idea

- **Confidence gate (He and Feng 2026)** [d09]. Fast model answers. A learned head reads the answer's evidence (mean log-prob, logit margin, parseability, cost) and predicts quality gain and slow-token cost. Release the fast answer or call the slow model. Fast pass costs 5.26 tokens on average; routed system about 519.
- **Rule switch (SwiftSage)** [d16]. Go slow if: 5 steps of zero reward, an invalid action, a critical decision, or an unexpected observation. The switch costs no tokens.
- **Learned think/no-think (AdaptThink, Thinkless)** [c13, c14]. RL with a length penalty; the model emits a control token or an empty thinking block.
- **Learned planning frequency (Paglieri)** [d14]. SFT then RL with a token-cost penalty. Prompting "plan only when necessary" did not work zero-shot [c06].
- **Adaptive lookahead (Imagine-then-Plan)** [d15]. A predictor picks the imagination horizon 0 to Kmax each step. Beats fixed-k and random-k on the success-vs-budget curve.
- **Rational metareasoning (De Sabbata et al. 2025)** [d08]. Reward = log P(answer | chain) - log P(answer | question) - lambda x tokens, used for expert iteration. 8B-class: 63.5% accuracy at 146.2 output tokens vs STaR 61.9% at 215.1 and few-shot CoT 56.4% at 253.6; 3B-class: 50.1% at 170.8 vs STaR 47.4% at 222.7. Saves 23 to 45% fewer output tokens.
- **Value-guided search (VGS)** [d17]. A small value model scores partial reasoning blocks (block 4,096 tokens, beam 2) and prunes. Closest LLM version of plan-until-habit; not a truncated-reasoning test.

## 5. What holds up

### 5.1 Replications that held

- **Stakes raise model-based control when planning pays.** Kool 2017: d = 0.47 (N = 98), d = 0.29 (N = 93) [d02]. Patzelt 2019: d = 0.35 (N = 839) [b08]. Null when there is no payoff gap: d = -0.04 (N = 100) [d03]. Three samples and a null control. Cost-benefit versus plain motivation is not separated [b08 limits].
- **Model-based use predicts devaluation sensitivity.** N = 90 then N = 95 [b13]. Count a21 and b13 as ONE source (a21 has the wrong authors).
- **Compulsivity dimension.** N = 548, replicated N = 1413 [b11]. Effects are small (betas about 0.03 to 0.06) and online self-report.
- **Model-free mimicry.** Akam 2015 [a13] and sequence-chunk work [c24] agree the classic signature is not diagnostic.
- **LLM overthinking and routing.** Three independent sources agree that thinking less on easy items loses nothing (Chen, AdaptThink, Thinkless) [b21, c13, c14].
- **Goldilocks planning.** Paglieri [d14] and Imagine-then-Plan [d15] both show a non-monotone curve.

### 5.2 Failures, threats and nulls

- **Hybrid reading threatened.** Story instructions move median w from 0.24-0.39 to 0.78-0.79 [d01]. A model-based agent with the wrong task model looks like a hybrid. Castro-Rodrigues 2022 agrees [c23]. Kool 2017 used extensive instructions with comprehension checks (25 practice trials, step-by-step teaching), not the story format, and still found mean w between 0.40 and 0.65 [d02]. Nobody has combined story instructions with a payoff-gap design.
- **Original task cannot test arbitration.** No payoff gap [a16]. Many "failures to find arbitration" before 2016 are uninformative. A 2025 failed extension of the incentive effect to social learning is known from a title only [a17 limits].
- **Time pressure and load are thin.** Keramati 2016: 15 per group [d05]. Otto 2013: 18 of 43 excluded [d06]. Neither has a larger direct replication in the citing scans (137 and 252 records). A tDCS study (n = 22, within subject) found no effect on model-based or model-free control, with Bayes favouring no effect; it is a different manipulation [d07, abstract only]. Stress replications are "mixed" (not re-checked) [b12 limits].
- **The key rule is untested on people.** Daw 2005, Keramati 2011 and Sezener 2019 are simulations. The only close behavioural test is Keramati 2016 (n = 15 per group) [critique].
- **Rival accounts.** Habits without values [b14], action chunks [b28, c24], and the "too coarse" argument [b15]. Treat the dual-system split as a design metaphor.

### 5.3 Moderators

- Payoff gap between systems (Kool 2016, 2017) [a15, d03].
- Instruction quality [c23, d01].
- Working memory load and stress [d06, b12].
- Age: model-based signature grows from age 5 to 11; metacontrol varies widely [b17].
- Time per decision [a19].
- Training amount and task structure (Daw 2005 simulation) [a03].
- For LLMs: model size, prompt style, task horizon, model-specific Goldilocks shape (section 6).

### 5.4 Interventions that worked and did not

| Intervention | Worked? | Numbers | Source |
|---|---|---|---|
| Higher stakes when planning pays | Yes | d 0.47, 0.29, 0.35 | [d02, b08] |
| Higher stakes when planning does not pay | No | d -0.04 | [d03] |
| Explain the task structure | Yes | w 0.24-0.39 to 0.78-0.79; N = 204 | [d01, c23] |
| Time pressure (700 ms) | Made planning shallower | n = 15 per group | [d05] |
| Stroop load, cold-pressor stress | Cut model-based use | N = 25, N = 48 | [d06, b12] |
| LLM: prompt "plan only when necessary" | No | zero-shot self-gating unreliable | [c06] |
| LLM: SFT then RL with token penalty | Yes | 0.387 at 1,714 tokens | [d14] |
| LLM: RL for think/no-think | Yes | -53.0% length, +2.4 acc | [c13] |
| LLM: separate router model | Weak | misjudges target model's difficulty | [c14] |
| LLM: learned confidence gate | Marginal | +1.02 points; utility below always-fast | [d09] |
| LLM: 8 shots of NoOp examples | No | did not fix GSM-NoOp | [d19] |

## 6. Language models

### 6.1 Do LLMs show model-based behaviour on the two-step task?

- **GPT-3 (Binz and Schulz 2023)** [c01]. Given the task as text, it showed the model-based signature: 200 simulations, 20 repetitions of two stages, 70/30 transitions. Stay probability fell after reward through a rare transition, t(1982) = -6.16, p < .001. Stay rose after a rare unrewarded trial, t(1814) = 2.33, p = .01. Caveat: the history is in the prompt, so the model can reason over all of it. The same paper shows GPT-3 picks the intuitive wrong answer on the CRT.
- **CogBench (Coda-Forno et al. 2024)** [a27, b18, c02, c03]. 35 LLMs, ten metrics from seven experiments, model-basedness normalised so random = 0, human = 1. Models able to solve the task are at least human level; GPT-4 is well above. Parameter count raises model-basedness (beta = 0.481 +/- 0.22, z = 4.2, p < .001). Training-set size and code training had no significant effect. RLHF models are closer to human behaviour. Prompting: chain of thought +64.59% and step-back +118.59% in model-basedness (relative, on normalised scores; large percentages can be small absolute shifts). CoT helped probabilistic reasoning more (+9.01% vs +3.10%).
- **Recall and mimicry.** Centaur (Llama 3.1 70B fine-tuned on Psych-101: over 60,000 participants, over 10,000,000 choices, 160 experiments) fits two-step NLL 0.51 [b19, c26]. LAPITHS (Da Pelo et al. 2026) [c18]: Llama 4 Maverick+RAG about 0.54, GPT-5.1 and GPT-4o about 0.55, Gemini 2.5 Pro about 0.56, DeepSeek R1 about 0.58, a cognitive model 0.61, Llama 3.1 0.63 (150 trials, 300 decisions per model). Their NLL is sampling-based and Centaur's is token-probability based, so the comparison is descriptive. Plain LLMs with retrieval nearly match fine-tuned Centaur. A model-based score on the public two-step task may be partly recall (K18, contested).
- **Interpretability (Demircan et al. 2024)** [a28, c04, c05]. Llama 3 70B learns a simplified two-step-like MDP in context: Q-learning NLL 2729 vs myopic 2864 (100 runs x 30 episodes). A sparse-autoencoder feature correlates with TD error at r = 0.58; switching it off lowers return. Llama 8B stays at chance. Transitions are deterministic, so this cannot separate model-based from model-free. Graph-learning latents track successor-representation codes (numbers not read).
- **NeuroCogMap (Sun et al. 2026)** [c19]. Preprint. A dynamic arbitration weight fitted to human data gives held-out AIC 262.45 vs 268.77 (original dual-system) in one two-step variant and 465.95 vs 478.29 in another. Not shown to be an LLM mechanism.

### 6.2 Planning on structure

CogEval (Momennejad et al. 2023) [a26, b20]. Eight LLMs (GPT-4, GPT-3.5, davinci-003, Bard, Cohere, Claude-1, LLaMA-13B, Alpaca-7B) on planning tasks built from human experiments. Models invented edges and failed systematic tests. Shortest path to a state one cluster away on community graphs: GPT-4 0 of 30 at temperature 0; at temperature 0.5 or 1 not above 10%. Scope: this one task on dense community graphs, not planning in general. 2023 models. BFS/DFS prompting helped some cells (K19).

### 6.3 When should an LLM plan?

**Always-slow is not best.**
- Paglieri et al. 2025 [d14]. Crafter, 100 seeds, Llama-3.3-70B zero-shot. Never plan 0.343 at 559.6 tokens. Plan every 4 steps 0.379 at 11,510.9 tokens. Always plan 0.349 at 38,836.2 tokens: 3.4x the tokens of every-4 for a lower reward. SFT 8B: never 0.286 (991.5 tokens); dynamic 0.343 (1,869.9); SFT+RL dynamic 0.387 at 1,714 tokens. Plan completion 20% vs 16%, adaptive replanning 41% vs 35% (RL 8B vs 70B) [c06]. Human-written plans let the trained agent finish Crafter (diamond), which no agent did alone [c07]. Mechanism hypothesis: an instability cost; the always-plan agent backtracks most and long contexts may dilute attention [c08].
- **Goldilocks is not stable.** Llama-3.1-8B degrades sharply the more it plans. Gemini 2.5 Flash degrades on Crafter and POGS. TextWorld gains are small. No rule predicts the peak; the every-4 optimum was found by sweep [d14]. Imagine-then-Plan says longer-horizon tasks favour larger lookahead [d15] (K28).
- **Imagine-then-Plan** [c16, c17, d15]. ALFWorld, Qwen3-8B, 140 tasks in 14 folds. Removing the RL stage that trains the horizon choice: ALFWorld 88.57 to 71.42, ScienceWorld 59.70 to 46.00. Training-free ITP-I on Qwen2.5-7B ALFWorld 35.71 vs ReAct 27.86. Adaptive beats fixed-k and random on the budget curve (values in plots only). Predictor cost is not separated (imagination 7.8 s of 14.2 s per step).

**Overthinking on easy items.**
- Chen 2024 [b21]: 1,953% more tokens on "2 plus 3"; 39 of 901 tokens to the first correct solution (4.3%). Self-training to trim later solutions kept accuracy (needs a known answer as signal).
- AdaptThink [c13]: DeepSeek-R1-Distill-Qwen-1.5B -53.0% length, +2.4 accuracy; 7B -40.1%, +2.3. At lambda 0.05, NoThinking share 86.9% (GSM8K), 76.8% (MATH500), 40.4% (AIME 2024). At lambda 0.1 length -64.5% but accuracy -0.5. Gain shrinks as NoThinking share rises. Maths only, distilled models.
- Thinkless [c14]: control tokens trained with DeGRPO cut long-chain thinking by 50 to 90%. Reasoning models use 5 to 20x the tokens of concise ones. On GSM8K extended reasoning offers no clear advantage. A separate router (Q-7B) did not see AIME as hard though the reasoning model gets only 28%. Vanilla GRPO collapses.
- Rational metareasoning [d08]: figures in 4.5.
- Wu 2024 [d18]: 0-shot CoT hurt some default tasks (PaLM-2 base-10 addition, chord fingering).

**Break-even by difficulty and cost.**
- Snell 2024 [d13]. MATH, PaLM 2-S. Compute-optimal allocation by difficulty matches best-of-N with up to 4x less test-time compute. FLOPs-matched against a 14x larger model, test-time compute wins on easy and intermediate bins and when inference load is low (R = 0.16); mixed at R = 0.79; pretraining wins at R = 22; little gain on the hardest bin. Difficulty estimation itself needs non-trivial compute.
- Ghoshal and Al-Bustami 2026 [c09, c10]. 60 examples per task (3 splits of 20). GPT-4o Event-QA 47.5% to 67.5% while latency rose from 8 s to 317 s. CMV: GPT-4o-mini one-shot 75% at about 6 s (up to 85% on one split); planning with search 25 to 35x slower. GPT-4o-mini costs 1/16.7 of GPT-4o. Small models degrade when planning needs many tools. The planning stack is mixed with retrieval and tools.

**Gates on a weak first answer.**
- He and Feng 2026 [d09, c11, c12]. 5,000 held-out items (GSM8K plus Mixture-of-Thoughts), fast Qwen2.5-Math-7B, slow OpenR1-Distill-7B, slow rate 8.20% for all routed methods. Always-Fast 47.90% (utility 0.4789, 5.26 tokens). Random same-k 46.76% (-1.14; utility 0.4517; 517.91 tokens; corrective precision 13.41%). Low average log-prob 48.22% (+0.32; precision 21.22%). Low logit gap 47.84% (-0.06; 11.46%). Learned gate 48.92% (+1.02; precision 27.07%; utility 0.4731). Per dataset: GSM8K 60.20 to 60.96, MoT 35.60 to 36.88. Equal slow-call count, not equal total tokens (518 to 715 average tokens). No routed method beat Always-Fast on utility.
- Yue 2024 [d10]. GSM8k, cost relative to GPT-4 = 1.0. GPT-3.5 CoT-SC 0.842 at 0.111. LLM verifier on question 0.884 at 0.253. Fine-tuned verifier 0.892 at 0.340. MoT-1D vote at threshold 0.5: 0.917 at 0.235; at 0.7: 0.951 at 0.425; MoT-Verify 0.947 at 0.401; GPT-4 CoT-SC 0.958. Llama2-13B as the weak model showed no saving on GSM8k and CREPE (K25).
- Aggarwal 2023 [d12]. Stop sampling when a Dirichlet test says the majority will hold: up to 7.9x fewer samples, under 0.1% accuracy drop. Example: 9 of the first 10 samples agree gives over 99% chance the majority holds after 40.
- Tian 2023 [d11]. gpt-3.5-turbo ECE / AUC. TriviaQA: label prob 0.140 / 0.869, verbalised 0.054 / 0.896. SciQ: 0.256 / 0.752 vs 0.132 / 0.766. TruthfulQA: 0.451 / 0.418 vs 0.389 / 0.545. This predicts correctness of one answer, not whether a slow pass would change it. Our schema already refuses verbal confidence as a stop rule (section 4b); sample consistency is the preferred hint.
- SwiftSage [b26, c15, d16]. ScienceWorld, 30 task types: 84.7 vs SayCan 33.8, ReAct 36.4, Reflexion 45.3, Swift alone 49.2. With gpt-3.5 (Table 3): Swift-only 49.22, SayCan 25.22, ReAct 19.76, Reflexion 23.40, SwiftSage 62.22 (slow pass adds +13.0). Tokens per action 757.07 vs 1,855.84, 1,971.03, 2,983.46. Reflexion had up to four rounds, others one. The fast module is fine-tuned on oracle trajectories. Baselines are not equal-compute.
- VGS [d17]. DeepSeek-R1-Distill-1.5B, N = 256 generations: VGS 39.8 on AIME-25 and HMMT-25 (46.7 and 32.8) vs 37.0 weighted voting and 31.6 majority voting. 11,219 vs 12,793 tokens. Value model trained on 2.5 million traces from the same family; competition math only.

**Gate cost** (K27). Small when the gate is a rule or a head: SwiftSage switch 0 tokens; He and Feng fast pass 5.26 tokens vs 519 routed; VGS value model 0.024% of generator FLOPs. Rarely reported as a total-token ledger.

### 6.4 Cached answers when the task changes (devaluation analogue)

- Wu 2024 [d18]. 11 counterfactual task pairs (base-9 arithmetic, 1-based indexing, rotated drawings, altered chess rules); GPT-4, GPT-3.5, Claude, PaLM-2. Above chance but well below default. Example: GPT-3.5 parseable programs fall from 99% to 62%, 71%, 75% under three rotation variants. Per-task figures not extracted.
- GSM-NoOp [d19]. One irrelevant clause: Phi-3-mini over -65%; o1-preview -17.5; Gemma-7b-it -20.6; Mistral-7b-v0.3 -24.0; o1-mini -29.1. 8 shots did not fix it.
- Ullman 2023 [d20]. GPT-3.5 transparent-bag variant: P(chocolate) = 95% although the protagonist can see popcorn; original 99%. A second prompt did not flip (P(popcorn) = 58%). Hand-made vignettes only.
- These are memorised patterns, not an agent's own cache. No study tests an agent's own stored solution after the task changed (K26).

### 6.5 Summary: what changed LLM behaviour and by how much

| Lever | Change | Size |
|---|---|---|
| Parameter count | more model-based on two-step | beta 0.481 |
| Step-back / CoT prompt | more model-based on two-step | +118.59% / +64.59% relative |
| RL with token penalty (Paglieri) | better reward, fewer tokens | 0.343 to 0.387; 1,714 tokens |
| RL for think/no-think (AdaptThink) | shorter, same or better | -53.0% length, +2.4 |
| Learned fast-answer gate (He and Feng) | small accuracy gain | +1.02 points |
| Prompt "plan only when necessary" | no reliable effect | not quantified [c06] |
| Hand-written switch (SwiftSage) | large gain with imitation fast module | 49.22 to 62.22 |
| Sample-vote cascade (Yue) | near-GPT-4 accuracy at lower cost | 0.917 at 0.235 |

## 7. What our agent should take

Status key: [E] established, [S] single-source, [C] contested. The schema already holds G11 (think briefly by default) and G12 (spend by difficulty). This field backs both and adds the points below. Nothing marked "Test first" goes into SCHEMA.md until its test passes (see UNKNOWNS.md).

### Add now (established)

| # | Take | Schema part | Status | Evidence |
|---|---|---|---|---|
| A1 | The default for easy classes is the direct path. Extra reasoning on easy items costs tokens and gains nothing: 1,953% more tokens on "2 plus 3"; first correct answer at 4.3% of the trace; learned no-think routing cut length 40.1 to 53.0% with +2.3 to +2.4 accuracy. This supports G11 and the S0 "direct" mode. | G11, S0 | [E] | b21, c13, c14, d13 |
| A2 | Always-plan is not a safe default. Planning every step cost 3.4x the tokens of planning every 4 steps for a lower reward (0.349 vs 0.379). Tie re-planning to a signal (G1), not to every step. | G1, S0, S5 | [E] | d14, d15, c08 |
| A3 | Do not use a prompt line like "plan only when necessary" as the gate. Zero-shot self-gating was unreliable. The gate must be code on a measured signal, or a trained policy. | S0 | [E] (one paper, consistent with 4b) | c06, d14 |
| A4 | Set budget and break-even per task family from a pilot, not from one global threshold. The break-even moves with difficulty, inference load and model; the best replan frequency differs by model and environment. | S0, G12 | [E] | d13, d14, d15 |
| A5 | Log the gate's own tokens apart from the slow-pass tokens, and report results with the gate included. | G7, logs | [E] | d09, d16, d17 |
| A6 | Do not credit a gate with saving tokens unless total tokens and accuracy are both reported against always-fast. In the one close study every routed method scored below always-fast on utility (0.4731 vs 0.4789) at its token price. | G7 | [E] (one study, but the logic is arithmetic) | d09, c12 |
| A7 | Treat a fast answer that matches a familiar pattern as untrusted when the task has a changed detail. LLM pattern answers fail under small changes (GSM-NoOp up to -65%; counterfactual tasks; transparent-bag P = 95%). This is why direct mode keeps a check (S4, S8) and why G3 asks for unfitted tests. | G3, S4, S8 | [E] for the failure; the fix is in Test first (T5) | d18, d19, d20 |
| A8 | Do not read model-based signatures on a public task as proof the agent plans. Judge planning from outcomes on changed-reward probes. A measurement rule for our bench. | G10 | [E] | a13, c24, c18 |
| A9 | Keep sample consistency, not verbal confidence, as the hint for "should I go slow". In the one head-to-head a learned gate beat mean log-prob, which beat logit gap, which beat random; a sample vote beat a model verifier on GSM8k. | G4, 4b | [E] for the 4b exclusion; the ranking is [S] | d09, d10, d11 |

### Test first

| # | Take | Schema part | Status | Evidence | Test |
|---|---|---|---|---|---|
| T1 | Gate the slow path on expected gain minus token price, with gain estimated from disagreement among 2 to 3 cheap samples. | S0 | [S] theory only; no LLM test | a10, b03, d09, d10, d12 | U1 |
| T2 | Rank cheap signals head to head: sample disagreement vs mean log-prob vs verbalised confidence, scored by whether the slow pass changed the answer. | S0 | [S] | d09, d10, d11 | U2 |
| T3 | Re-check or re-plan on a trigger (zero progress for k steps, invalid action, surprise), not on a schedule or never. | S0, S5, S6 | [S] | d16, d14 | U3 |
| T4 | Sweep the re-plan interval in agent tasks and expect an intermediate peak. | S0, S6 | [E] that a peak exists; [S] that it can be found cheaply | d14, d15 | U4 |
| T5 | Before reusing a stored lesson or answer, diff the new task against the stored case and force the slow path when conditions differ. | memory, S0 | [C] (analogy to devaluation; no direct LLM test) | a21, d18, d19 | U5 |
| T6 | Give the full task model as a plain story before solving (stated transitions, rules, what counts as correct). | S1 | [E] in humans; untested in LLMs | d01, c23, d02 | U6 |
| T7 | Truncate reasoning at k tokens and plug in a cheap value estimate (short vote or learned score) instead of running to the end. | S0, S3 | [S] | d17, a19, d05 | U7 |
| T8 | Add explicit search (BFS or DFS written out) when the task is structure that must be unrolled. | O (search) | [S] | a26, b20 | U8 |
| T9 | Scale the slow budget with the reward at stake only when the slow pass changes accuracy. | S0 | [S] humans only | d02, d03, b08 | U9 |
| T10 | Store a short summary of each solved plan so repeats cost fewer tokens (offline-replay analogue). | memory | [S] | b16 | U10 |
| T11 | Distractor load in context pushes the agent toward shallow cached answers; cap or trim context. | G11, S1 | [S] humans only | d06, b12 | U11 |

## 8. Concrete tests on our bench

All arms get the same total tokens, including the gate's own tokens and setup (G7). Use the existing HTSA bench (harness/bench.py) item types where they exist. Report accuracy, total tokens, and cost-adjusted utility = accuracy - lambda x tokens with lambda fixed before the run.

| Test | Item type | Arms (equal total tokens) | Metric | Expected effect |
|---|---|---|---|---|
| U1 gain-minus-cost gate | mixed-difficulty set with a spread of plain pass rates (easy, medium, hard bins) | (a) always direct; (b) always slow; (c) random routing at the same slow rate; (d) fixed disagreement threshold; (e) gate on estimated gain minus token price | accuracy at fixed total tokens; corrective precision; utility | (e) at or above (a) on utility; about +1 point accuracy as in He and Feng, more if the pass-rate spread is wide; (c) below (a) |
| U2 signal head-to-head | the same items for all signals | gates by sample disagreement, mean log-prob (where available), verbalised confidence, random | corrective precision at fixed slow-call rate (He and Feng: learned 27.07, log-prob 21.22, logit gap 11.46, random 13.41) | disagreement at or above log-prob; verbal confidence no better than disagreement |
| U3 trigger-based re-check | multi-step agent tasks with a check | never re-check; re-check every k steps; re-check on trigger | success at equal tokens | trigger at or above scheduled, above never; SwiftSage-sized gain (+13 points) is an upper bound |
| U4 interval sweep | long-horizon agent tasks | re-plan every k in {1, 2, 4, 8, never} | success vs tokens curve | non-monotone, peak at intermediate k; shape differs by model |
| U5 changed-conditions diff | paired tasks: solved original, then a variant with one changed detail (altered rule, irrelevant clause) | (a) reuse stored lesson or answer; (b) solve fresh; (c) diff check then reuse or solve fresh | accuracy on variants; tokens on unchanged repeats | (c) matches (b) on variants and (a) on repeats; (a) drops on variants |
| U6 task-model clarity | tasks with hidden structure | bare rules vs full plain-story description plus a self-check question | use of structure on a changed-reward probe; accuracy | full description raises use of structure; size unknown |
| U7 depth cap with plug-in | reasoning items with a verifiable answer | full chain of thought; chain truncated at k tokens plus short vote; truncated plus learned score | accuracy at equal total tokens | truncation at least equal at about 50% tokens on easy and medium bins; worse on hard |
| U8 explicit search on graphs | community or maze graph tasks (CogEval style) | free CoT; BFS/DFS scaffold; scaffold plus code check | exact-path success | scaffold lifts the hardest cell from near 0; size unknown |
| U9 stakes line | items with an accuracy-reward line in the prompt | no line; stakes line; with and without a real payoff gap | tokens spent and accuracy | likely null in LLMs; tokens up with no accuracy gain means a bad lever |
| U10 plan memory | repeated task families | no memory; stored plan summary shown after the first attempt | tokens and accuracy on repeats | fewer tokens on repeats, equal accuracy |
| U11 distractor load | items with 0, 1k, 4k tokens of irrelevant context | plain; context trimming in S1 | accuracy | falls with load; trimming recovers part |

## 9. What does not transfer, and why

- **The two-step score as a measure.** It is an interaction beta, not a planning measure, and may be recall of a public task (K18, c18). It does not tell us whether our agent plans.
- **The weight w and "61% model-free".** Contested for humans (d01) and meaningless for a scaffold, which has no stable mixture parameter. In our agent the mix is a per-item mode choice.
- **Time cost as reaction time.** In humans the cost is time x reward rate. For an LLM it is tokens, latency and money, each with its own price. The mapping is an analogy.
- **Uncertainty as the habit system's variance.** An LLM has no calibrated posterior over its own cached answer. The Keramati VPI step has no ready input. Proxies (disagreement, log-prob) are untested for "will a slow pass change the answer".
- **Tonic dopamine as reward rate.** A neural claim; no agent use.
- **Slow caching by repetition.** Human habit forms by repeated reward. An LLM's weights do not change in context. Our analogue is the lessons store and class record, which are explicit and inspectable.
- **Psychiatric, stress and development results (K09, K10, K11, b17).** Background only. The one use is as a warning that load can cut deliberate control.
- **Neural mappings (ventral striatum, SPE in IPS).** Not usable.
- **Sparse-autoencoder TD features (Demircan).** Interpretability only; 70B only; deterministic transitions.
- **The split itself.** If Collins and Cockburn are right, MB/MF is too coarse. Use it as a design metaphor and test the gate on its own merits.

## 10. Open questions

1. Does any LLM study test an explicit expected-gain-versus-token-cost gate against fixed and random routing at equal total tokens with utility reported? None found (K24). The closest (He and Feng) used an equal slow-call count. Search quotas were out, so a missed study is possible.
2. Which cheap signal best predicts that a slow pass will change the answer? Disagreement vs log-prob vs verbalised confidence on the same items has not been run (K23).
3. What is the measured break-even for LLM tasks as token price changes (a Kool-style payoff-gap curve)? Not found (K25).
4. Do humans with story instructions and a payoff-gap design still show cost-benefit arbitration? Not combined (K22).
5. Does an agent over-trust its own cached solution after the task changes? No direct study (K26).
6. Is the Goldilocks replan frequency predictable from task or model features? No rule found (K28).
7. Does truncated reasoning plus a value estimate beat full chain of thought at equal tokens? Open (K29).
8. Do Keramati 2016 and Otto 2013 replicate in larger samples? No direct replication in the citing records (K08, K09).
9. Is the human incentive effect (d 0.29 to 0.47) cost-benefit arbitration or plain motivation? Not separated (b08).
10. Is LLM model-basedness on the two-step task skill or recall? Contested (K18).

## 11. Sources

[V] = opened and read this session (full text or substantial part). [M] = snippet, abstract only, or title only.

**Theory and founding studies**
- Daw, Niv, Dayan (2005) Uncertainty-based competition between prefrontal and dorsolateral striatal systems. [V] https://sites.socsci.uci.edu/~lpearl/courses/readings/DawEtAl2005.pdf and https://www.nature.com/articles/nn1560
- Daw, Gershman, Seymour, Dayan, Dolan (2011) Model-based influences on humans' choices and striatal prediction errors. [V] https://pmc.ncbi.nlm.nih.gov/articles/PMC3077926/
- Glascher, Daw, Dayan, O'Doherty (2010) States versus rewards. [V] https://pmc.ncbi.nlm.nih.gov/articles/PMC2895323/
- Keramati, Dezfouli, Piray (2011) Speed/accuracy trade-off between the habitual and the goal-directed processes. [V] https://pmc.ncbi.nlm.nih.gov/articles/PMC3102758/ and https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1002055
- Keramati, Smittenaar, Dolan, Dayan (2016) Adaptive integration of habits into depth-limited planning. [V] https://pmc.ncbi.nlm.nih.gov/articles/PMC5111694/ and https://www.pnas.org/doi/10.1073/pnas.1609094113
- Sezener, Dezfouli, Keramati (2019) Optimizing the depth and direction of prospective planning. [V] https://pmc.ncbi.nlm.nih.gov/articles/PMC6440644/
- Dayan and Berridge (2014) Model-based and model-free Pavlovian reward learning. [V] https://link.springer.com/content/pdf/10.3758/s13415-014-0277-8.pdf
- Dickinson (1985) Actions and habits. [M] https://doi.org/10.1098/rstb.1985.0010
- Adams and Dickinson (1981) Instrumental responding following reinforcer devaluation. [M] https://doi.org/10.1080/14640748108400816
- Sutton and Barto (1998) Reinforcement Learning: An Introduction; Sutton (1990) Dyna. [M] http://incompleteideas.net/book/the-book-2nd.html
- Renaudo et al. (2015) criteria for shifting between goal-directed and habitual behaviours in robots. [M] https://hal.sorbonne-universite.fr/hal-01250157/document

**Human tests, challenges, moderators**
- Akam, Costa, Dayan (2015) Simple plans or sophisticated habits? [V] https://journals.plos.org/ploscompbiol/article/file?id=10.1371/journal.pcbi.1004648&type=printable and https://pmc.ncbi.nlm.nih.gov/articles/PMC4686094/
- Kool, Cushman, Gershman (2016) When does model-based control pay off? [V] https://pmc.ncbi.nlm.nih.gov/articles/PMC5001643/
- Kool, Gershman, Cushman (2017) Cost-benefit arbitration between multiple reinforcement-learning systems. [V] https://gershmanlab.com/pubs/KoolGershmanCushman17.pdf (also https://doi.org/10.1177/0956797617708288)
- Patzelt, Kool, Millner, Gershman (2019) Incentives boost model-based control. [V] https://pmc.ncbi.nlm.nih.gov/articles/PMC6314918/
- Feher da Silva and Hare (2020) Humans primarily use model-based inference in the two-stage task. [V] preprint https://www.biorxiv.org/content/10.1101/682922v1.full.pdf ; published version at abstract level https://www.nature.com/articles/s41562-020-0905-y
- Castro-Rodrigues et al. (2022) Explicit knowledge of task structure. [V] https://pmc.ncbi.nlm.nih.gov/articles/PMC7613376
- "When models matter: environmental demand guides the arbitration" (2026, PMID 41083652). [M] https://europepmc.org/article/MED/41083652
- Otto, Gershman, Markman, Daw (2013) The curse of planning. [V] https://gershmanlab.com/pubs/Otto13.pdf
- Otto, Raio, Chiang, Phelps, Daw (2013) Working-memory capacity protects model-based learning from stress. [V] https://pmc.ncbi.nlm.nih.gov/articles/PMC3876216/
- Gillan, Kosinski, Whelan, Phelps, Daw (2016) Symptom dimension and goal-directed control. [V] https://elifesciences.org/articles/11305 and https://pmc.ncbi.nlm.nih.gov/articles/PMC4786435/
- Gillan, Otto, Phelps, Daw (2015) Model-based learning protects against forming habits. [V] https://link.springer.com/article/10.3758/s13415-015-0347-6
- Miller, Shenhav, Ludvig (2019) Habits without values. [V] https://pmc.ncbi.nlm.nih.gov/articles/PMC6548181/
- Collins and Cockburn (2020) Beyond dichotomies in reinforcement learning. [V] https://pmc.ncbi.nlm.nih.gov/articles/PMC7800310/
- Momennejad, Otto, Daw, Norman (2018) Offline replay supports planning. [M] (abstract level) https://pmc.ncbi.nlm.nih.gov/articles/PMC6303108/
- Smid et al. (2023) Model-based decision making and metacontrol in childhood. [V] https://pmc.ncbi.nlm.nih.gov/articles/PMC10329104/
- Decker, Otto, Daw, Hartley (2016) From creatures of habit to goal-directed learners. [M] https://doi.org/10.1177/0956797616639301
- Dezfouli and Balleine (2013) Actions, action sequences and habits. [M] https://doi.org/10.1371/journal.pcbi.1003364
- "Model-Free RL or Action Sequences?" (Frontiers in Psychology 2019; authors not verified). [V] https://pmc.ncbi.nlm.nih.gov/articles/PMC6933525
- Citing-literature scan of Keramati 2016 and Otto 2013 (Europe PMC abstracts, PMIDs 24475185, 36701316, 41286251, 40206860). [M] https://europepmc.org/article/MED/24475185

**Language models and agents**
- Binz and Schulz (2023) Using cognitive psychology to understand GPT-3. [V] https://arxiv.org/abs/2206.14576
- Coda-Forno, Binz, Wang, Schulz (2024) CogBench. [V] https://arxiv.org/abs/2402.18225
- Binz et al. (2025) Centaur. [V] https://arxiv.org/abs/2410.20268 ; Nature version [M] https://doi.org/10.1038/s41586-025-09215-4
- Da Pelo et al. (2026) Taming the Centaur(s) with LAPITHS. [V] https://arxiv.org/abs/2604.27927
- Sun et al. (2026) NeuroCogMap. [V] https://arxiv.org/abs/2607.00397
- Demircan et al. (2024) Sparse autoencoders reveal temporal difference learning in LLMs. [V] https://arxiv.org/abs/2410.01280
- Momennejad et al. (2023) CogEval. [V] https://arxiv.org/pdf/2309.15129
- Chen et al. (2024) Do NOT think that much for 2+3=? [V] https://arxiv.org/abs/2412.21187
- Zhang et al. (2025) AdaptThink. [V] https://arxiv.org/abs/2505.13417
- Fang, Ma, Wang (2025) Thinkless. [V] https://arxiv.org/abs/2505.13379
- Paglieri et al. (2025) Learning when to plan. [V] https://arxiv.org/abs/2509.03581
- Ghoshal and Al-Bustami (2026) When do tools and planning help LLMs think? [V] https://arxiv.org/abs/2601.02663
- He and Feng (2026) When to think deeply (IDPR). [V] https://arxiv.org/abs/2606.06745
- Lin et al. (2023) SwiftSage. [V] https://arxiv.org/abs/2305.17390
- Liu et al. (2026) Imagine-then-Plan. [V] https://arxiv.org/abs/2601.08955
- De Sabbata et al. (2025) Rational metareasoning for LLMs. [V] https://arxiv.org/pdf/2410.05563
- Yue et al. (2024) LLM cascades with mixture of thought representations. [V] https://arxiv.org/pdf/2310.03094
- Tian et al. (2023) Just ask for calibration. [V] https://arxiv.org/pdf/2305.14975
- Aggarwal et al. (2023) Adaptive-Consistency. [V] https://arxiv.org/pdf/2305.11860
- Snell et al. (2024) Scaling LLM test-time compute optimally. [V] https://arxiv.org/pdf/2408.03314
- Wang et al. (2025) Value-guided search for efficient chain-of-thought reasoning. [V] https://arxiv.org/pdf/2505.17373
- Wu et al. (2024) Reasoning or reciting? [V] https://arxiv.org/pdf/2307.02477
- Mirzadeh et al. (2025) GSM-Symbolic. [V] https://arxiv.org/pdf/2410.05229
- Ullman (2023) LLMs fail on trivial alterations to theory-of-mind tasks. [V] https://arxiv.org/pdf/2302.08399

## Source audit (2026-11-01)

Fresh auditors re-opened the sources of 12 established claims: 11 confirmed as written, 1 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **B02.03-K15** (reworded: the sources support less). All numbers match He & Feng Table 1, but the +1.02 is the learned IDPR gate, not a confidence-only gate (low avg log-prob +0.32, low logit gap -0.06); the He & Feng figures come from one preprint listed four times. Corrected claim: Gates give small gains: a learned fast-answer controller (IDPR, using confidence, logit margin and cost features) that sends 8.20% of items to slow reasoning lifts accuracy from 47.90 to 48.92 (+1.02) vs 46.76 for random routing at the same slow-call rate, while simple confidence-only selection gives +0.32 (avg log-prob) and -0.06 (logit gap); cost-aware utility of every routed method stays below always-fast (IDPR 0.4731 vs 0.4789). A separate router LLM misjudges the target model's difficulty (Thinkless, AIME). Single-paper preprint evidence for the gate numbers.
- **B02.03-K09** (now single-source: only one opened source, code check).
