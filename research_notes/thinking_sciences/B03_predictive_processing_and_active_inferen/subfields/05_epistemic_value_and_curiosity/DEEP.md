# Epistemic value and curiosity: deep document

*Subfield B03.05. Sources: evidence_a-d.jsonl (a01-a29, b01-b28, c01-c26, d01-d17), claims.jsonl (K01-K27), critique.md. Evidence ids in brackets refer to those files. Status tags: [E] established, [S] single-source, [C] contested.*

## 1. What it is

Epistemic value is the part of an agent's choice rule that rewards actions for what they will teach the agent. In active inference, the agent scores each possible policy by its expected free energy (EFE), written G. G has two parts. Extrinsic (pragmatic) value is how likely the outcomes are to be the preferred ones. Epistemic value is the expected information gain: how much the outcome is expected to reduce uncertainty about hidden states or model parameters [a01, a19]. The theory calls this term curiosity.

The key claim for us: the switch from exploring to exploiting is not a separate module. Information gain is a KL divergence. It shrinks as the posterior stops changing. When it is equal for all policies, preferences decide [a02, d05]. So "explore until information gain runs out, then exploit" is a property of the maths, not a schedule.

Three things must be kept apart:
1. The theory (Friston 2015, 2017). Simulation only. No human or LLM test in those papers [d05, d06, K26].
2. Human exploration data (Horizon task). Two mechanisms: an information bonus and decision noise [b20, d07].
3. Engineering uses in LLM agents: expected information gain (EIG) computed by code to pick questions or probes; curiosity filters for open-ended learning; bandit studies of whether LLMs explore at all.

For our agent this maps to S3 open mode (generate probes and ideas when no check exists), the stop test that ends probing, and the code-side tally that tracks what has been tried. The most useful finding of this research is a split of labour: the LLM proposes probes and hypotheses; code tallies, scores information gain and decides when to stop [d04, d11, d01, K23].

## 2. History and theories in depth

**Ancestors.** Optimal Bayesian experimental design and active learning pick the query with the highest expected information gain. Itti and Baldi (2009) defined Bayesian surprise as KL between posterior and prior and reported it predicts gaze [a22, M]. Sun, Gomez and Schmidhuber (2011) formulated optimal Bayesian exploration with information-gain curiosity [a23, M]. Kakade and Dayan (2002) gave a novelty-bonus account of dopamine [a26, M]. Da Costa 2020 notes that epistemic affordance is mathematically the same as optimal Bayesian design and active learning [a19].

**The dark-room worry.** Schwartenbeck, FitzGerald, Dolan and Friston (2013) argued that free-energy minimisation does not mean agents hide in dark rooms. Minimising surprise over future outcomes means matching likely outcomes to desired ones while keeping entropy over visited states, so new states raise a path's value [a08].

**Friston et al. 2015, "Active inference and epistemic value" (opened, d05).** Choice is minimising EFE, which splits into extrinsic value (expected utility) and epistemic value (expected information gain). Expected-utility choice and KL control come out as special cases. Tested only in a simulated T-maze: 128 trials per setting, six levels of prior preference, four schemes (active inference, KL control, expected-utility RL, fixed-precision dopamine). When arm utilities are zero, expected-utility and KL schemes fall below chance. The active-inference scheme still reaches the reward by using the informative cue. An ambiguity term, not only novelty, is part of epistemic value. That term guards against noisy outcomes.

**Friston et al. 2017, process theory (opened, a01-a05).** Same maths, with a message-passing implementation. T-maze over 32 trials, 10 policies: the first about 20 trials are epistemic (visit cue, then reward arm). After that the agent goes straight to the reward. Setting the precision of preferences to zero gives pure epistemic foraging (Figure 10). Physiology links (repetition suppression, phasic dopamine as policy confidence, place cells) are model outputs, not new data [a05].

**Friston et al. 2017, "Curiosity and insight" (opened, d06).** A simulated agent learns an abstract colour rule. Novelty (information gain about parameters) draws it to ambiguous locations early. Once the rule is learned it avoids them. Bayesian model reduction (pruning the hypothesis space after the fact) produces an "aha" step. One agent: 32 trials of 6 epochs, change from ignorance to understanding after trial 14. 64 artificial agents: with model reduction nearly all reach 100% around trial 10; chance is about 30%. The hypothesis space was hand-made and contained the true rule. No human experiment.

**Schwartenbeck et al. 2019 (eLife, a10, b18, b19).** Splits information gain in two. Hidden-state exploration seeks unambiguous observations to know the current state (salience). Model-parameter exploration seeks novel outcomes to learn task structure (novelty). They can conflict. Prediction: an ambiguous option attracts while the agent is unsure what it maps to, and repels once it is sure it is ambiguous. Random exploration becomes adaptive only when directed uncertainty reduction fails. Simulated risky-vs-safe bandit: curious early, confident after about ten trials.

**Parr and Friston 2017 (a09).** Epistemic foraging depends on believed precision and volatility. Salience falls where precision is low. The salience of an unchanged location grows slowly as uncertainty about it grows, which gives inhibition of return. Higher believed volatility gives shorter inhibition of return.

**Critiques and variants.** Millidge, Tschantz and Buckley (2021, "Whence the expected free energy?") show epistemic value does not fall out of extending variational free energy into the future. The natural future free energy (FEF) has the information term with the opposite sign, so it penalises information seeking. EFE is FEF minus expected information gain, so the bonus is added by design. They offer FEEF (free energy of the expected future), which keeps the information gain and adds an entropy term [a14, a15, b01, b02, c16]. Millidge, Seth and Buckley (2021) split objectives into evidence objectives (no built-in exploration) and divergence objectives (match expected to desired future, which contain an information-gain term) [b03]. Sajid et al. (2021) reject a variant that subtracts ambiguity, because it would stop information seeking, and keep ambiguity in G [a13]. Da Costa et al. (2023) say directed exploration emerges from risk and ambiguity in EFE [b07]. Both views hold at different levels: it emerges once you accept EFE, but EFE is a choice [a27, K03].

**Depth of planning.** Standard active inference is Bellman-optimal only for planning horizon 1. Deeper horizons need recursive "sophisticated" inference [b06]. Sophisticated inference is a tree search over beliefs. In the T-maze (horizon 2, path search cut at predictive probability under 1/16, preferences -2 and +2, reward arm paid 95%) it makes the epistemic choice more confident. The one-step agent underestimates the cue's epistemic value. An agent with Bayesian risk only (no epistemic value) skips the cue and exposes itself to risk [a17, a18].

**Hafner et al. 2022 (a20).** One KL objective unifies exploration objectives. Latents over states give state information gain. Latents over parameters give model learning (VIME, MAX, Plan2Explore). Plain input entropy gives density exploration, which rewards rare inputs and so is vulnerable to unlearnable noise [a29].

**Human exploration science (separate tradition).** Wilson et al. 2014 showed with the Horizon task that people use directed exploration (information bonus) and random exploration (decision noise), both rising with the number of free choices left [b20]. Gershman (2018) found a hybrid of uncertainty bonus and sampling fits best [b23, M]. Zajkowski 2017 showed a causal role for right frontopolar cortex in directed exploration [d07]. Somerville 2017 (N=149, ages 12-28) showed directed exploration emerges in adolescence [b25, M]. Sadeghiyeh 2020 linked temporal discounting to less directed exploration [b24, M]. Wilson 2021 reviews the field [b26, M].

**Curiosity in machine learning.** Pathak et al. 2017 used forward-model prediction error in a learned feature space, to avoid the white-noise trap [c18]. Tschantz 2020 (two papers) brought information gain into model-based deep RL [a16, c17]. Voyager, ELLM and OMNI use an LLM to say what is worth trying [c10, c11, d12].

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| EFE = extrinsic value + epistemic value (expected information gain) | G = -(mutual information of states and outcomes) - E[ln P(outcome)] | Friston 2017 [a01], Friston 2015 [d05], Da Costa 2020 [a19] | [E] theory |
| Switch is built in: information gain cannot go below zero and falls as posterior settles | T-maze: about 20 of 32 trials epistemic, then direct reward | a02, a03 | [E] simulation only |
| With zero arm utility, utility-only schemes fall below chance; active inference still finds the reward via the cue | 128 trials per setting, 6 preference levels, 4 schemes | Friston 2015 [d05] | [E] simulation only |
| Rule learning: insight after model reduction | 64 agents, near 100% around trial 10, chance about 30% | Friston 2017 [d06] | [S] simulation only |
| Epistemic term is added, not derived | FEF sign positive on information gain; EFE negative | Millidge 2021 [a14, b01] | [E] algebra |
| FrozenLake deterministic | AI 99.88 [99.64,100]; Bayes RL 99.76; Q-learning (eps 0.1) 97.79 | Sajid 2021 [b04] | [E] simulation |
| FrozenLake stochastic | AI 98.90 [98.00,99.79]; Bayes RL 64.39; Q-learning 66.08 [63.28,68.88]; 200 trials x 500 episodes | Sajid 2021 [b04] | [E] simulation |
| No reward at all | Q-learning 0.00 (15 moves); Bayes RL 39.94 (9.17 moves); AI 44.00 (8.67 moves); null-preference AI 50.03 / 50.22 | Sajid 2021 [b05] | [E] simulation |
| Sparse Mountain Car solved in one trial by epistemic agent; no gain on Cup Catch | 25 episodes, 5 seeds; Half Cheetah beats SAC at 100 episodes | Tschantz 2020 [a16] | [C] |
| Epistemic variant fails dSprites; reward-only variants solve it | 5 EFE definitions, 3 action rules | Champion 2023 [c15] | [C] |
| Humans: information bonus rises with horizon | N=30 (31 recruited), 320 games, t(29)=5.05, 25 of 30 | Wilson 2014 [b20] | [S] human lab |
| Humans: decision noise rises with horizon | F(1,119)=65.97, 28 of 30 | Wilson 2014 [b20] | [S] |
| Measured bonus larger than optimal; no difference horizon 6 vs 11 | supplement; F(2,89)=0.09 for reward vs information | Wilson 2014 [b21] | [S] |
| TMS over right frontopolar cortex cuts the information bonus, not noise | N=31, bonus at horizon 6 down about 4.8 points, 99% of posterior below zero | Zajkowski 2017 [d07] | [S] same lab |
| Human eye movement favours epistemic models | pooled log evidence about 888; N not recorded | Mirza 2018 [a21] | [S] |
| GPT-4 basic prompt: suffix failure | above 60% of replicates at T=500 (Fig. 1); main runs T=100, K=5, gap 0.2; 3 of 72 GPT-4 configs avoid suffix failure, 2 of those fail uniform-like, 1 succeeds | Krishnamurthy 2024 [b08, b09, c01, c02] | [E] older models |
| The one working config: summary stats from code + CoT + hint | suffix failure about 15% or less at T/2; same prompt with raw history fails | Krishnamurthy 2024 | [E] |
| EVOLvE win-rate (MAB) | Flash raw 27.7, summarised 34.8, guided 32.2; Pro raw 45.5, summarised 60.0, guided 59.6; UCB 90.6 | Nie 2025 [b10, c03] | [E] |
| EVOLvE contextual bandit | Flash raw 0.0, guided 46.4; Pro raw 7.1, guided 64.3; LinUCB 96.4 | Nie 2025 | [E] |
| EVOLvE best-arm fraction barely rises | Flash 9.3 to 10.7; UCB 32.7 to 65.0 | Nie 2025 [b11] | [E] |
| EVOLvE few-shot demos | Flash raw-history demos 27.5 vs summarised-history demos 50.2; fine-tuned Flash raw 65.6 vs summarised 28.3 | Nie 2025 [c04, critique] | [S] table garbled |
| GPT-3 on Horizon task: no directed exploration | horizon beta=-0.15, z=-0.56, p=.58; regret 2.72 vs human 3.24, t(38878)=-5.03 | Binz and Schulz 2023 [b13, c05] | [S] GPT-3 only |
| GPT-3 repeats the more-seen option | value effect beta=0.18, z=14.48 | Binz and Schulz [b14] | [S] |
| Meta-ICL makes GPT-3 greedier, not more curious | greedy-level after about 4 tasks; UCB use +0.046 only | Coda-Forno 2023 [b15] | [C] |
| Gemma2 stops exploring early | 10 arms: coverage 40% (2B), 65% (9B, 27B) with CoT, 25% without; 20 arms: 45% for largest | Schmied 2025 [d01] | [E] Gemma only |
| Frequency bias vs greed by size | 96% repeat share at 2B vs 14% at 27B | Schmied 2025 | [S] |
| Knowing-doing gap | 87% rationales correct; greedy action 58% vs optimal 21% (intro says 64%) | Schmied 2025 | [S] |
| Try-all sweep closes most of the gap to UCB for 27B | RL fine-tuning on 2B: coverage +12%; with +1 untried bonus 50% to 70% | Schmied 2025 | [E] with d04, d16 |
| Thinking raises directed exploration in a 2-armed task, not enough in 4-armed non-stationary | o3-mini high thinking above human directed level; Gemini-2.5-flash up to human level; humans N=45 and N=31 | Zhang 2025 [d02] | [E] |
| LLM posterior sampling beats in-context RL | o1-mini turns LLM-PSRL from near-linear to sub-linear regret on RiverSwim; in-context RL optimal in just over 25% of trials | Arumugam and Griffiths 2026 [d03] | [S] small tasks |
| One-step information-directed probe recovers probe-first strategy | informative-action bandit K=10, 10 trials; LLM-PSRL cannot | Arumugam 2026 [d03] | [S] appendix pilot |
| Labels and reward sign bias exploration | negative rewards trigger more exploration; 8B models explore too little in pilot; Qwen3-14B matched 32B | Austin 2026 [d14] | [S] |
| UoT: EIG-scored questions | +38.1% average (relative or points not stated); Llama3-70B 20Q-Things 15.0 to 25.0, DX 83.7 to 90.4, MedDG 60.2 to 64.3, FloDial 28.8 to 47.1; GPT-4 troubleshooting 43.7 to 67.3 | Hu 2024 [b16, c06] | [E] closed sets |
| UoT shortens dialogues | Llama3-70B DX 3.5 to 1.0 turns; MedDG 3.5 to 1.4 | Hu 2024 [b17] | [S] |
| DPO on EIG pairs | INLG 56.7 to 68.9, Things 51.1 to 61.1; questions 7.1 to 5.2; mean EIG 0.34 to 0.45; plain fine-tuning hurt (46.6, 42.2) | Mazzaccara 2024 [c07] | [S] 7B model |
| LIPS: sample k, score EIG, pick best | humans mean 1.27 bits (N=40, 605 pairs); k=1 raw 0.65-0.66; k=10 above human mean | Grand 2024 [c08] | [S] |
| Open-set EIG: sample about 20 hypotheses, equal weights | EIG-uniform beat implicit questioning; EIG-logprobs clearly worse; 15 animals, 10 rounds, 5 seeds | Kobalczyk 2025 [d11] | [S] |
| Information per question falls toward zero | 150 shopping tasks, 10 items, 8 candidate questions; 3 scored questions beat 4 baseline questions | Piriyakulkij 2023 [d15] | [S] |
| Stop rule beats fixed budget (answer sampling) | up to 7.9x fewer samples, under 0.1% accuracy drop, threshold 0.95, 17 datasets; code-davinci-002 100 samples 61.4% vs 23.6 samples 63.4% | Aggarwal 2023 [d09] | [E] other task type |
| Answer-convergence stop | over 40% fewer tokens on NQ with accuracy up; unstable on MATH-500 and GPQA | Liu and Wang 2025 [d10] | [C] |
| Interest filter on learnability | Crafter: LP alone 55 tasks, 9 interesting; BabyAI LP only 4 tasks; OMNI beats LP and uniform | Zhang 2024 OMNI [c09, d12] | [S] |
| LLM goals beat novelty-only | Crafter: ELLM about 6 achievements, oracle 9, novelty methods under 3; 64.9% of goals good | Du 2023 [c11] | [S] |
| LLM curriculum | 63 items, 3.3x baselines, 2.3x map distance, 15.3x/8.5x/6.4x faster tools, diamond in 1 of 3 runs; random curriculum -93% | Voyager [c10] | [S] 3 runs |
| Novelty term in red teaming | 196 toxic prompts from LLaMA2-7b-chat; RL alone high diversity but few high-toxicity | Hong 2024 [c12] | [S] |
| EFE-driven LLM counsellor | Qwen3-8B Lift 1.62 vs 1.07 vs 0.62; 12.2 vs 13.1 turns; ablations -0.17 to -0.28 | PUMA 2026 [c14] | [S] many parts changed |

## 4. Mechanisms and models

**4.1 Expected free energy, written for an engineer.** For each candidate policy pi, compute G(pi) = risk + ambiguity. Risk is KL between predicted outcomes and preferred outcomes (extrinsic value, negated). Ambiguity is the expected entropy of outcomes given states. Equivalent form: G = -(information gain) - (expected log preference). Pick policies by softmax of -G. Information gain is the mutual information between hidden states and outcomes [a01]. Pure epistemic foraging is the case where preference precision is zero [a04].

**4.2 A simple loop for an LLM agent.**
1. Hold a set H of candidate hypotheses (rules, answers, causes).
2. Get k candidate probes (questions, test inputs, experiments) from the model.
3. For each probe, predict the answer under each hypothesis. Group hypotheses by predicted answer. EIG = entropy of the answer distribution (for a deterministic answer model), which equals the entropy reduction over H.
4. Score = lambda_e * EIG + lambda_p * (expected progress toward the goal). Pick the max. PUMA used lambda_e=0.4, lambda_p=0.6 [c14].
5. Run the probe. Filter H by the result. Repeat.
6. Stop when the best EIG is under a threshold, or the leading hypothesis passes a confidence test, with a minimum probe count [d09, d10, d15].

**4.3 Hypotheses when the space is open.** Ask the model for about 20 compatible hypotheses at each step. Drop the ones that contradict the evidence. Treat the rest as equally likely. Compute EIG in code. Do not weight by the model's own token probabilities [d11]. Posterior sampling by the LLM (sample one hypothesis, act on it, update) also works in small spaces but spends more tokens [d03].

**4.4 Directed versus random exploration (Horizon-task model).** Choice value = expected reward + information bonus (directed) + noise (random). Both bonus and noise rise with the number of free choices remaining [b20]. For the agent: the horizon is a number that code can hand to the model, and the stop test can scale with it. In LLMs this link is unproven (GPT-3 null [b13]).

**4.5 Code-side bandit scaffolding that worked.** Counts and mean per probe, computed by code and given as summary statistics [c02]. A forced first sweep of every candidate probe [d01]. An untried-action bonus of +1 during RL fine-tuning [d01]. Neutral probe labels and a fixed reward frame [d14].

**4.6 Interest and relevance filters.** OMNI asks an LLM which learnable tasks are interesting. ELLM asks an LLM for goals that fit the scene. Voyager asks for the next task that is novel yet achievable [c09, c10, c11]. The common point: raw novelty or raw learning progress drifts to trivia or noise.

**4.7 Diversity term.** A novelty reward as negative SelfBLEU plus embedding cosine distance against past attempts prevents repeats [c12]. It needs a tuned weight so it does not swamp the goal.

**4.8 Lookahead.** One-step EIG is myopic. Recursive scoring (sophisticated inference) is a tree search over beliefs [a17]. No LLM test compares one-step with lookahead at equal tokens [critique gap 8].

**4.9 Guard against the noisy TV.** Information gain about a latent falls to zero when nothing can be learned, so a gain-based stop rule avoids unlearnable noise. Input-entropy curiosity does not [a29, a20]. Prediction error in a learned feature space is another guard [c18].

## 5. What holds up

**Theory.** The algebra is solid: EFE contains an information-gain term; the term is added by design, not derived [a14]. The switch behaviour (information gain decays, preferences take over) is a mathematical property, shown in two Friston simulations and in Sajid's FrozenLake comparison [a02, b04, d05, d06]. These are not empirical proof that agents should explore this way.

**Active inference simulations.** Epistemic agents explore without a hand-tuned bonus in small grid and control tasks; with no reward Q-learning stalls while belief-based agents keep exploring [b05, a16, c17]. Active inference and Bayesian model-based RL behave nearly the same once preferences are treated as rewards [b04]. This is expected: they are close relatives.

**Failures and contest.** Cup Catch: no benefit of directed exploration because random actions reach reward. dSprites: the epistemic variant keeps picking one action and fails, reward-maximising variants solve it [a16, c15]. So the bonus depends on whether reward is sparse. We mark K05 as contested. Almost all active-inference evidence is simulation from the originating lab in toy tasks [critique].

**Human data.** Wilson 2014 (N=30) and Zajkowski 2017 (N=31, same lab) both show a horizon-driven information bonus. Gershman 2018 (N=45) and Chakroun 2020 (N=31) were re-fitted by Zhang 2025 [d02]. No failed replication of the Horizon task was found. No independent-lab effect sizes were read. Zajkowski extended its sample from 16 to 31 after a first look (optional stopping risk) [d07]. A 2025 tDCS null (N=43) used a different task, so it is not a failed replication [d08]. Mirza 2018 has an unrecorded N and needed hand-added heuristics [a21].

**LLM exploration: what holds.** Off-the-shelf LLMs under-explore, lock onto early options and ignore horizon [c22]. This appears in four independent studies (Krishnamurthy, EVOLvE, Binz, Schmied) plus the 2025-26 follow-ups [d02, d03, d14]. All of them are bandit-style.

**Interventions that worked.**
- Code-computed summary statistics: Pro 45.5 to 60.0; the only working GPT-4 config used them [b10, c02].
- Forced try-all sweep: largest single gain, 27B nearly at UCB [d01].
- Few-shot demonstrations of good exploration: Flash 27.5 to 50.2 with summarised-history demos [c04].
- EIG scoring of candidate probes with code: UoT, DPO, LIPS, Handa, Piriyakulkij, Kobalczyk [b16, c07, c08, d13, d15, d11].
- Stop on a confidence threshold: Adaptive-Consistency, 7.9x fewer samples [d09].
- Sampling past episodes at random (Stochastic ICRL) raised exploration more than temperature [b12].
- Thinking budget on easy bandits [d02].

**Interventions that did not work, or hurt.**
- Basic prompting, chain of thought with raw history [c01, c02].
- Guidance for small models: Gemma 2B/9B gained nothing, and Pro contextual-bandit guided scored 25.0 vs Flash 60.7 [c03, c04]. Contested because a try-all sweep helped across Gemma sizes [d01].
- Meta in-context learning: more greed, not more curiosity [b15].
- Plain fine-tuning on questions: success fell to 46.6 and 42.2 [c07]. Fine-tuning on summarised history: 28.3 vs 65.6 raw [c04].
- Raw novelty and raw learning progress [c09, c11].
- Prediction-error curiosity helped only with narrow training data [d17].
- Using the LLM's own log-probabilities as hypothesis weights [d11].
- Answer-convergence stop on hard sets (MATH-500, GPQA) [d10].

**Moderators.** Closed versus open hypothesis set (gain is largest when closed, and the gap shrinks with stronger models [d11, d15]). Model size (frequency bias at small size, greed at large [d01]). Labels and reward sign [d14]. Stationary versus non-stationary bandit [d02]. Whether random actions find reward [a16].

## 6. Language models

**Bandit studies (2023-2026).**
- GPT-3 (Binz and Schulz): lower overall regret than humans (2.72 vs 3.24) but no directed exploration (beta=-0.15, p=.58) and no noise scaling with horizon. Matched humans at short horizon (p=.97). In long-horizon tasks GPT-3 regret was significantly lower than humans (t(5550)=-4.07), though humans improved more within a task [b13, critique].
- GPT-3 meta-ICL (Coda-Forno): matched greedy after about 4 tasks; avoids uncertain options by default [b15].
- GPT-3.5, GPT-4, Llama2 (Krishnamurthy): suffix failure above 60% for basic GPT-4 at T=500; one working configuration of 72 [b08].
- Gemini 1.5 Flash and Pro (EVOLvE): Pro 45.5 raw to 60.0 with summaries; UCB 90.6. Contextual: Pro 7.1 raw to 64.3 guided; LinUCB 96.4 [b10].
- Gemma2 2B/9B/27B (Schmied): coverage 25% to 65%; greedy; knowing-doing gap (87% of rationales right, greedy action 58%) [d01].
- 2025-26 reasoning models (Zhang 2025): thinking on moves LLMs toward the human mix; o3-mini at high thinking has directed exploration above human level in a stationary 2-armed task; no thinking model reaches effective directed exploration in a non-stationary 4-armed task [d02].
- Arumugam and Griffiths: with o1-mini, LLM-PSRL goes sub-linear on RiverSwim. DeepSeek-R1 improves all agents, but the best baseline with R1 is not significantly better than LLM-PSRL with GPT-4o [d03].
- Austin 2026: labels and reward sign bias exploration; Gemini 3.1 Flash Lite with unlimited thinking explored fast and matched the reward-normative pattern on most tasks; OLMo-3.1-32B barely explored unless told it was a bandit task [d14].
- Harris and Slivkins 2026: LLMs are weak exploitation oracles and good exploration oracles (candidate proposers); the GPT-5 family does best but is slow and costly [d04]. No single headline number extracted.
- Berdica 2026: plain numerical bandits on text embeddings match or beat LLM solutions at lower cost [d16] (abstract and intro only).

**Information-gain question selection.** UoT +38.1% average (5 datasets); GPT-4 troubleshooting 43.7 to 67.3 [b16]. DPO on EIG pairs +10 to +12 points on a 7B model [c07]. LIPS: the LLM proposes, a program scores; at k=10 above the human mean EIG of 1.27 bits [c08]. Handa 2024: 39-48 users per condition; EIG-scored questions beat LM-only elicitation [d13]. Piriyakulkij: 3 scored questions beat 4 baseline questions [d15]. Kobalczyk: EIG-uniform on sampled hypotheses beats implicit reasoning, with a smaller gap for stronger models [d11]. In every case EIG is computed by code, so this is not "the model being curious".

**Curiosity filters in open-ended agents.** Voyager 3.3x items [c10]; ELLM 6 vs under 3 achievements [c11]; OMNI beats LP and uniform [d12]; Hong 2024 red-teaming 196 toxic prompts [c12]. All use an LLM as interest judge, which is circular.

**Active-inference wrappers around LLMs.** Prakki 2024: qualitative only, no baseline [c13]. PUMA 2026: Lift 1.62 vs 1.07 (Qwen3-8B), 1.76 on Llama-3.1-8B; ablations -0.17 to -0.28 but many parts change together [c14]. F-Explorer: the snippet says pragmatic value dominated and led to confirmation bias [c20, M]. Safer-AGI framework: conceptual, not read [c21, M]. None isolates the epistemic term at equal compute [c26].

**Stop rules.** Adaptive-Consistency and answer-convergence work for answer sampling, not for information gain over probes [d09, d10].

**What changed behaviour, ranked by size of evidence.** (1) Coded coverage and tally (largest; d01, c02). (2) Algorithm-guided summaries (about +15 points; b10). (3) EIG scoring by code (+10 to +38%). (4) Thinking budget (mixed; d02). (5) Model size (swaps bias for greed; d01).

## 7. What our agent should take

### Add now (established)

| Item | Schema part | Status | Evidence | Note |
|---|---|---|---|---|
| Code keeps the probe tally and outcomes; the model never tracks them in raw transcript | S3 and memory | [E] | b08, c02, b10, d01, d04, d16 | Per candidate probe: count, outcome. Pass summary stats in the prompt. |
| Forced first sweep: try every candidate probe (or each hypothesis family) once before narrowing | S3 open mode | [E] | d01, K23 | Largest single gain in Schmied. Cap by budget (G7, G12). |
| LLM proposes candidate probes and hypotheses; code scores and chooses | S3, S7, G5, G8 | [E] | b16, c07, c08, d11, d13, d15, d04 | Matches G5 and G8. Sample k probes (about 5 to 10), code picks by score. |
| Where the hypothesis set is closed and answers countable, score probes by expected information gain in code | S7 (discriminating test), S3 | [E] | K12, K13 | The S7 "run the one input where two rules differ" step is the same idea. |
| Judge probes against the goal: a relevance gate (does the answer bear on the task?) | S3 | [E] | c09, c10, c11, c12, d12 | Pair with G8: judged by running. |
| Stop probing on a coded test (leading hypothesis passes a confidence test, or best-probe gain under a threshold) plus a minimum probe count | S3 to S4 hand-off, G7, G12 | [E] for answer sampling; [S] for probes | d09, d10, d15, d05 | Threshold must be tuned on our bench. Keep a minimum probe count because answer-convergence is unstable on hard sets [d10]. |
| Neutral probe labels and a fixed reward frame | S1 input hygiene, S3 | [S] but cheap | d14 | Labels change exploration; costs nothing. |
| Do not use the model's token probabilities as weights | G5 | [S] | d11 | Use equal weights over filtered samples. |

The stop test is [E] for answer sampling and in theory, but its use on open-ended probes is untested, so the threshold value belongs in "Test first".

### Test first (not yet established for our setting)

| Item | Schema part | Status | Evidence | Why test |
|---|---|---|---|---|
| Stop open mode on best-probe information gain under a threshold instead of a fixed probe budget | S3, G12 | [S] | d09, d10, d15, K21 | Nobody tested it on open-ended probes. |
| Sample about 20 hypotheses, filter, equal weights, EIG in code, for open tasks | S3, S7 | [S] | d11, d03 | Single study; gap shrinks with stronger models. |
| Tell the agent the remaining budget as a number; check that probe share rises with it | S3, S6 | [C] | b20, d07, b13 | Human effect real, GPT-3 null; no test on 2025-26 models. |
| LLM relevance filter vs raw novelty vs gain-to-zero stop, with an unlearnable distractor | S3 | [S] | d12, c11, a29, d17 | Noisy-TV case not tested for LLMs. |
| Epistemic weight on or off (lambda_e 0 vs 0.4) in an EFE loop at equal tokens | S3 | [S] | c14, c26 | PUMA changed many parts at once. |
| Lookahead (two-step) probe score vs one-step | S3 | [S] | a17, d03 | No LLM comparison at equal tokens. |
| Skip the S3 scaffold below a model-size floor | S0 gate | [C] | d01, d14, c03 | Size floor unmeasured. |
| Few-shot demonstrations of exploration traces | S3 | [S] | c04 | Format-dependent: summarised vs raw flips the fine-tuning result. |
| Random subsampling of past attempts as a diversity source | S3 | [S] | b12 | Qwen2.5 bandit tasks only. |

## 8. Concrete tests on our bench

All arms get equal total tokens, with setup cost counted (G7). Include the plain model as a control arm.

1. **Stop rule vs fixed budget (open mode).** Items: open-hypothesis tasks, for example ARC-style rule discovery where probes are test inputs, or BRAINTEASER-type items where each probe is a question to an oracle. Arms: (A) fixed probe budget; (B) stop when best-probe gain is under a threshold, with a minimum probe count; (C) plain single attempt. Metric: accuracy at equal mean tokens, and tokens saved at equal accuracy. Expected: B saves 20 to 40% of tokens at equal accuracy, as in d09 and d10. Those were answer-sampling studies, so this is a guess.
2. **Coded tally and forced sweep.** Items: bandit-style probe tasks (K=5 to 10 probes, gap 0.2, T=100) and probe-selection items with a hidden best option. Arms: raw transcript; coded summary; coded summary plus forced first sweep. Metric: suffix-failure rate, share of best-option pulls, final reward. Expected: summary raises win-rate by about 15 points (b10); the sweep adds more (d01).
3. **EIG-scored probe selection with sampled hypotheses.** Items: closed-set 20-questions and diagnosis items, plus open ones. Arms: first-sample probe; k=8 samples with code picking max EIG; k=8 samples with the LLM picking. Metric: success at N questions; mean questions to success. Expected: +10 to +30% relative on closed sets, less on open sets, less with stronger models (b16, c07, d11).
4. **Horizon information.** Items: same bandit and probe tasks with the remaining budget stated as a number (1, 6, 11) or hidden. Metric: share of probes on the least-known option as a function of horizon; regret. Expected: small or null for non-reasoning models (b13); possibly a positive slope for 2025-26 thinking models. A null is fine; it removes the item.
5. **Noisy-TV distractor.** Items: tasks with one probe class whose answers are random. Arms: novelty-only; gain-to-zero stop; LLM relevance gate; both. Metric: share of budget spent on the distractor; accuracy. Expected: novelty-only wastes over 30% of probes; gain-based arms under 10%.
6. **Epistemic weight ablation.** Arms: lambda_e = 0, 0.4, 1.0 with the same belief state. Metric: accuracy and tokens. Expected: 0.4 beats 0 on sparse-feedback items and ties on dense-feedback items (a16 vs c15).
7. **One-step vs lookahead.** Arms: one-step EIG; two-step EIG over the top 3 probes. Metric: accuracy at equal tokens. Expected: lookahead wins only when one probe unlocks others, and otherwise loses on tokens.
8. **Size floor.** Run test 2 at two or three model sizes. Metric: gain from the scaffold. Expected: near zero gain below about 8B (d14, d01); sign unknown.

## 9. What does not transfer, and why

- **Friston simulations.** Toy T-maze and abstract rule tasks, with hand-made hypothesis spaces containing the true rule, simulated by the originating lab [d05, d06]. They justify the shape of the stop test, not a threshold. Do not cite them as evidence the schema works.
- **The free-energy principle as a whole.** The epistemic term is a design choice [a14]. We do not need the formalism. We use EIG only.
- **Dopamine, repetition suppression, place cells.** Model outputs, not data [a05].
- **Human Horizon-task data.** Small samples, student populations, same lab; GPT-3 showed no horizon effect [b13]. Human directed exploration serves a creature with a body and a lifetime. The agent's horizon is a token budget.
- **Bandit results.** Stateless, small K, older models (GPT-3 to Gemini 1.5, Gemma2). Probe tasks in S3 have structure and hypotheses, not just arms.
- **EIG question selection.** Needs a closed or well-sampled hypothesis set and a clean answer model (yes/no). Gain shrinks in open spaces and with stronger models [d11, d15]. Soft or overlapping answers are untested.
- **Voyager, ELLM, OMNI.** Embodied game worlds (Minecraft, Crafter); 3 runs per method for Voyager; an LLM as interest judge is circular and conflicts with G8 if used as the final selector [c10, d12].
- **PUMA and Prakki.** Counselling dialogue, or no baseline [c13, c14].
- **Fine-tuning results** (DPO on EIG pairs, RLFT on Gemma2, oracle-trajectory fine-tuning). We do not train; only scaffold effects count [c07, d01, c04].
- **Answer-sampling stop rules.** They stop on agreement of final answers, which under G4 is only a hint when samples come from one model. Use them as design precedent, not as the exact rule [d09].
- **Curiosity as a drive.** The agent has no drive. "Curiosity" here is a coded selection rule.

## 10. Open questions

1. Does stopping on estimated information gain of open-ended probes beat a fixed budget at equal tokens? (K21; no study.)
2. Do 2025-26 reasoning models still show suffix failure with and without a coded tally? No study measured suffix-failure rate there.
3. Which estimator keeps the information gain when hypotheses overlap: sampled hypotheses or LLM-estimated partitions? No head-to-head found.
4. Does an LLM relevance filter beat raw novelty at equal tokens on unlearnable distractors?
5. Does telling an LLM its remaining budget change exploration as it does in people? Only GPT-3 was tested (null).
6. What is the effect of lambda_e alone in an LLM expected-free-energy loop?
7. Where is the size floor for the scaffold? "8B too weak, 14B fine" is a pilot remark [d14].
8. Do lookahead scores beat one-step scores for the extra tokens?
9. Independent-lab effect sizes for the Horizon task were not read. Gershman 2018, Sadeghiyeh 2020 and Somerville 2017 are snippet-only here.
10. Friston-style insight (prune the hypothesis space, then commit) has no LLM test.
11. Does thinking budget substitute for a coded tally, or add to it?
12. Is the 38.1% in UoT relative or in points? The paper does not say.

Links to parallel subfields (not covered here): Search over thoughts; Tree of Thoughts; Language-guided exploration; Cognitive conflict and impasse; Calibration and overconfidence; Belief updating; Compression at inference time; Diagnosability.

## 11. Sources

[V] opened and read this session; [M] snippet or abstract only.

**Theory and active inference**
- [V] Friston, FitzGerald, Rigoli, Schwartenbeck, Pezzulo (2017) Active inference: a process theory. https://openaccess.city.ac.uk/id/eprint/16683/1/NECO_a_00912.pdf
- [V] Friston, Rigoli, Ognibene, Mathys, FitzGerald, Pezzulo (2015) Active inference and epistemic value. https://www.fil.ion.ucl.ac.uk/~karl/Active%20inference%20and%20epistemic%20value.pdf (DOI 10.1080/17588928.2015.1020053)
- [V] Friston, Lin, Frith, Pezzulo, Hobson, Ondobaka (2017) Active inference, curiosity and insight. https://www.fil.ion.ucl.ac.uk/~karl/Active%20Inference%20Curiosity%20and%20Insight.pdf
- [V] Schwartenbeck, FitzGerald, Dolan, Friston (2013) Exploration, novelty, surprise, and free energy minimization. https://pmc.ncbi.nlm.nih.gov/articles/PMC3791848/
- [V] Parr and Friston (2017) Uncertainty, epistemics and active inference. https://pmc.ncbi.nlm.nih.gov/articles/PMC5721148/
- [V] Schwartenbeck et al. (2019) Computational mechanisms of curiosity and goal-directed exploration (eLife). https://pmc.ncbi.nlm.nih.gov/articles/PMC6510535/
- [V] Sajid, Ball, Parr, Friston (2021) Active inference: demystified and compared. https://arxiv.org/abs/1909.10863
- [V] Millidge, Tschantz, Buckley (2021) Whence the expected free energy? https://arxiv.org/abs/2004.08128
- [V] Millidge, Seth, Buckley (2021) Understanding the origin of information-seeking exploration. https://arxiv.org/abs/2103.06859
- [V] Tschantz, Millidge, Seth, Buckley (2020) Reinforcement learning through active inference. https://arxiv.org/abs/2002.12636
- [V] Tschantz, Baltieri, Seth, Buckley (2020) Scaling active inference. https://arxiv.org/abs/1911.10601
- [V] Friston, Da Costa, Hafner, Hesp, Parr (2021) Sophisticated inference. https://arxiv.org/abs/2006.04120
- [V] Da Costa, Sajid, Parr, Friston, Smith (2023) Reward maximisation through discrete active inference. https://arxiv.org/abs/2009.08111
- [V] Da Costa, Parr, Sajid et al. (2020) Active inference on discrete state-spaces. https://arxiv.org/abs/2001.07203
- [V] Hafner, Ortega, Ba, Parr, Friston, Heess (2022) Action and perception as divergence minimization. https://arxiv.org/abs/2009.01791
- [V] Champion, Grzes, Bonheme, Bowman (2023) Deconstructing deep active inference. https://arxiv.org/abs/2303.01618
- [V] Pathak, Agrawal, Efros, Darrell (2017) Curiosity-driven exploration by self-supervised prediction. https://arxiv.org/abs/1705.05363
- [M] Itti and Baldi (2009) Bayesian surprise attracts human attention. https://doi.org/10.1016/j.visres.2008.09.007
- [M] Sun, Gomez, Schmidhuber (2011) Planning to be surprised. https://doi.org/10.1007/978-3-642-22887-2_5
- [M] Kakade and Dayan (2002) Dopamine: generalization and bonuses. https://doi.org/10.1016/S0893-6080(02)00048-5

**Human exploration**
- [V] Wilson, Geana, White, Ludvig, Cohen (2014) Humans use directed and random exploration to solve the explore-exploit dilemma. https://pmc.ncbi.nlm.nih.gov/articles/PMC5635655/
- [V] Zajkowski, Kossut, Wilson (2017) A causal role for right frontopolar cortex in directed, but not random, exploration. https://elifesciences.org/articles/27430
- [V] Mirza, Adams, Friston, Parr (2018) Human visual exploration reduces uncertainty about the sensed world. https://pmc.ncbi.nlm.nih.gov/articles/PMC5755757/
- [V] Timokhov, Timashkov, Zinchenko (2025) No effect of cathodal HD-tDCS over frontopolar cortex. https://www.nature.com/articles/s41598-025-22016-z
- [M] Gershman (2018) Deconstructing the human algorithms for exploration. https://europepmc.org/article/MED/29289795
- [M] Sadeghiyeh et al. (2020) Temporal discounting correlates with directed exploration. https://europepmc.org/article/MED/32132573
- [M] Somerville et al. (2017) Charting the expansion of strategic exploratory behavior. https://europepmc.org/article/MED/27977227
- [M] Wilson, Bonawitz, Costa, Ebitz (2021) Balancing exploration and exploitation with information and randomization. https://europepmc.org/article/MED/33184605

**Language models and AI**
- [V] Krishnamurthy, Harris, Foster, Zhang, Slivkins (2024) Can large language models explore in-context? https://arxiv.org/abs/2403.15371
- [V] Nie et al. (2025) EVOLvE: Evaluating and optimizing LLMs for exploration. https://arxiv.org/abs/2410.06238
- [V] Binz and Schulz (2023) Using cognitive psychology to understand GPT-3. https://arxiv.org/abs/2206.14576
- [V] Coda-Forno, Binz, Akata et al. (2023) Meta-in-context learning in LLMs. https://arxiv.org/abs/2305.12907
- [V] Monea, Bosselut, Brantley, Artzi (2025) LLMs are in-context bandit reinforcement learners. https://arxiv.org/abs/2410.05362
- [V] Schmied et al. (2025) LLMs are greedy agents. https://arxiv.org/abs/2504.16078
- [V] Zhang et al. (2025) Comparing exploration-exploitation strategies of LLMs and humans. https://arxiv.org/abs/2505.09901
- [V] Arumugam and Griffiths (2026) Toward efficient exploration by LLM agents. https://arxiv.org/abs/2504.20997
- [V] Harris and Slivkins (2026) Should you use your LLM to explore or exploit? https://arxiv.org/abs/2502.00225
- [V] Austin, Suleman, Cheung (2026) Semantic bandits. https://arxiv.org/abs/2608.16707
- [V] Berdica et al. (2026) When do we need LLMs? (abstract and introduction only). https://arxiv.org/abs/2604.05859
- [V] Yang and Chen (2025) In-context curiosity. https://arxiv.org/abs/2510.00347
- [V] Hu et al. (2024) Uncertainty of Thoughts. https://arxiv.org/abs/2402.03271
- [V] Mazzaccara, Testoni, Bernardi (2024) Learning to ask informative questions. https://arxiv.org/abs/2406.17453
- [V] Grand, Pepe, Andreas, Tenenbaum (2024) Loose LIPS sink ships. https://arxiv.org/abs/2402.19471
- [V] Kobalczyk et al. (2025) Active task disambiguation with LLMs. https://arxiv.org/abs/2502.04485
- [V] Handa et al. (2024) Bayesian preference elicitation with language models. https://arxiv.org/abs/2403.05534
- [V] Piriyakulkij, Kuleshov, Ellis (2023) Active preference inference using language models and probabilistic reasoning. https://arxiv.org/abs/2312.12009
- [V] Aggarwal et al. (2023) Let's sample step by step: Adaptive-Consistency. https://arxiv.org/abs/2305.11860
- [V] Liu and Wang (2025) Answer convergence as a signal for early stopping. https://arxiv.org/abs/2506.02536
- [V] Zhang, Lehman, Stanley, Clune (2024) OMNI. https://arxiv.org/abs/2306.01711
- [V] Wang et al. (2023) Voyager. https://arxiv.org/abs/2305.16291
- [V] Du et al. (2023) Guiding pretraining in RL with LLMs (ELLM). https://arxiv.org/abs/2302.06692
- [V] Hong et al. (2024) Curiosity-driven red-teaming. https://arxiv.org/abs/2402.19464
- [V] Prakki (2024) Active inference for self-organizing multi-LLM systems. https://arxiv.org/abs/2412.10425
- [V] PUMA (2026) user-state modeling with expected free energy for LLM counselors. https://arxiv.org/abs/2605.24647
- [M] F-Explorer, cognitive LLM web-exploration agent. https://escholarship.org/content/qt1vp251h4/qt1vp251h4.pdf
- [M] Framework for inherently safer AGI through language-mediated active inference (2025). https://arxiv.org/abs/2508.05766
