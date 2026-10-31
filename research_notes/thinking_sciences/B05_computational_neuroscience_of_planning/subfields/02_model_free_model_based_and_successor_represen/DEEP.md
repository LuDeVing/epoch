# Model-free, model-based and successor representation: deep document

*Subfield B05.02. Built from evidence_a-d.jsonl (a01-a28, b01-b33, c01-c29, d01-d16), claims.jsonl (K01-K37) and critique.md in this folder. Written 2026-10-31. Status marks follow SCHEMA.md: [E] established, [S] single source, [C] contested. Ten sources were re-opened in the cross-check; items not opened are marked.*

## 1. What it is

Three ways to turn experience into choices.

- **Model-free (MF).** Store a value for each state-action pair. Update it from prediction errors (temporal difference, TD). Choosing is a lookup. It is cheap at decision time. It is slow to adapt: if the world changes, the value changes only after new experience.
- **Model-based (MB).** Store a model of the world: what each action does, what each outcome is worth. Choosing means simulating forward (tree search) and picking the best branch. It adapts at once to any change the model knows about. It costs compute at every decision.
- **Successor representation (SR).** Store, for each state, the discounted expected number of future visits to every other state, under the current policy. Value is then the SR times a separate reward vector. Choosing is a lookup plus a dot product. A change in reward is one edit. A change in structure or in the best action leaves the stored table stale. The SR sits between MF and MB: part of the planning is done in advance and cached.

Why it matters for our agent: the agent has a memory of past runs and a budget. The question is what to store (values, raw traces, "where does this class of problem lead") and when to pay for simulation instead of using the cache. The field gives a precise vocabulary for the trade: compute at decision time versus staleness. It also gives diagnostics: a gap between how well an agent adapts to a changed reward and to a changed structure tells you which kind of memory it uses (a21).

Scope note. The brain claims (striatum, hippocampus) are background. Only the computation matters for the agent. Several brain-level claims are single-source or contested and are marked as such.

Neighbours (not covered here): model-based versus model-free control as a general theory, exploration versus exploitation, active systems consolidation, language agents as architectures, heuristic search, impasse-driven subgoaling. Links are noted in section 7.

## 2. History and theories in depth

**Tolman (1948), cognitive maps.** Latent learning and detour or shortcut behaviour in rats were taken as evidence that animals build map-like knowledge beyond stimulus-response links. The test logic survives: change the reward or the structure and see whether behaviour adjusts without new experience. (a18; not opened.)

**Sutton (1990), Dyna.** Interleave real experience with replayed simulated transitions from a learned model, so cached values improve between decisions. It is the basis of SR-Dyna and of the "plan offline, act from cache" family. (a17; not opened, described through Russek 2017.)

**Dayan (1993), the SR.** Founding paper (a01, a02, b17, opened). Definition: M = (I - gamma P)^-1, the expected discounted future occupancy. TD can learn M itself, with successor prediction errors. With a linear value function, value = M times expected immediate reward, so the temporal part of the task is factored out. Demonstrated on a grid maze with a barrier against a punctate code and CMAC squares. Two points matter. First, an SR learned in an unrewarded exploration phase (latent learning) speeds later reward learning, and it respects the barrier: states on opposite sides share few predictions even when close in space. Second, the paper itself says the learned SR could hinder learning if the goal moves to a place the old policy rarely visited. The policy dependence was in the founding paper. No human data, single simulations.

**Daw, Niv, Dayan (2005), arbitration by uncertainty.** MB (prefrontal) and MF (dorsolateral striatal) controllers each track their own uncertainty and the more certain one controls the action. (a03; the page could not be opened; described from memory.) Direct tests of this rule have been mixed.

**Daw et al. (2011), the two-step task.** The task that made MF versus MB measurable in humans (a04, a05, b01, d01; opened). A first-stage choice leads to one of two second-stage states with fixed 0.7 / 0.3 transition probabilities. Rewards drift. A pure MF learner repeats a rewarded choice whatever the transition. A pure MB learner repeats it only after a common transition. People showed both signs (numbers in section 3). The ventral striatal prediction-error signal also carried MB information, against a clean split of two learners.

**Dolan and Dayan (2013); Sutton and Barto (2018).** Standard reviews of goals and habits and of RL. (a27, a28; not opened.)

**Akam, Costa, Dayan (2015), the two-step artefact.** By simulation, MF strategies can look MB in the two-step task, because task structure creates correlations between start-of-trial action values and later events (a14, b08; opened, partly). A suggested extra-regressor correction removes part of the problem. This is a warning for any "did it plan?" benchmark.

**Kool, Cushman, Gershman (2016), when does MB pay?** In the standard task, MB control raises reward rate almost not at all, so the supposed accuracy versus effort trade-off is absent (a13, a22, a23, b09; opened). A redesigned task where planning pays raised MB use.

**Russek et al. (2017), SR as a bridge.** Simulations of Tolman-style tasks (a09, a10, a20, b16, c25; opened). SR-TD solves latent learning and reward revaluation. It fails detour (transition change) and policy revaluation, because it cannot update cached successors without new experience. Two repairs: recompute M from a learned one-step model at decision time (SR-MB), or replay stored transitions to update M offline (SR-Dyna). With enough replay samples SR-Dyna and Dyna-Q both pass all three tasks. With too few, Dyna-Q degrades to MF and fails all three; SR-Dyna still passes latent learning but fails transition and policy revaluation. So a cached successor map degrades more gracefully than cached values when compute is short.

**Momennejad et al. (2017), SR in humans.** The key human test (a06-a08, a21, a26, b02, b03, d02, d03; opened). Design: after learning, change either the reward (reward revaluation) or the transitions (transition revaluation). MB predicts equal adaptation to both. MF predicts failure on both. A pure SR predicts success on reward change and failure on transition change. Humans: strong on reward change, weaker but well above zero on transition change. Exp 2 added policy revaluation (a deep new reward changes the best earlier action, transitions unchanged). People behaved as on transition revaluation.

**Stachenfeld, Botvinick, Gershman (2017), hippocampus as predictive map.** Place cells encode SR rows, not position; grid cells reflect an eigendecomposition of the SR (a11, a12, a25, b20; opened, simulations matched qualitatively to published rodent data). The discount sets the horizon. The authors list a mismatch: place fields at reward are not larger, as the SR predicts.

**Barreto et al. (2017), successor features.** Generalise the SR to features: if reward is linear in known features, Q for any new reward weights is the successor features dotted with the weights. With generalised policy improvement (GPI, take the best across stored policies) the agent transfers before learning, with a guarantee (a16, c27). Needs linear reward and fixed dynamics.

**Momennejad et al. (2018), replay.** fMRI, N=24 (a15, a24, b05). Off-task replay of the first-stage cue during rest predicted later replanning; unsigned prediction error predicted replay.

**2019-2024, rivals and critiques.** Feher da Silva and Hare (2020) showed that the "MF part" in humans is largely misunderstanding of the task (b06, b07). Geerts et al. (2024), described in the Carvalho et al. review (b04, b18, b19), offer a Kalman-filter TD account of the SR with non-local updates, which also produces the partial transition effect without simulation. The Carvalho review is the source for Tomov et al. (2021, policy reuse) and de Cothi et al. (2022, rat and human navigation); both second-hand here.

**2023-2026, language models.** Binz and Schulz (c01, c02), CogBench (c03-c05), CogEval (c06-c09, d04), Demircan et al. (c12, c13), RAP and WebDreamer (c16, c17), GAMER, WebATLAS and ProPlay as memory designs (c18, d08, d09). Section 6.

## 3. Core findings with exact numbers

Status column: E established, S single-source, C contested.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| SR defined; TD learns it; value = SR x reward vector | M=(I-gamma P)^-1; single grid-maze simulations, no N | Dayan 1993 (a01, a02) | E |
| Humans mix MF and MB signs in the two-step task | N=17, 201 trials; reward main effect p<1e-8; reward x transition p<5e-5; transition main effect p=.5; median MF weight 61% / MB 39%; reward effect positive 14/17, interaction positive 10/17 | Daw 2011 (a04, d01) | E (but see instruction artefact) |
| Striatal prediction error also carries MB information | same N=17; BOLD signal reflects both in proportions matching choice | Daw 2011 (a05) | S |
| Reward revaluation easier than transition revaluation | Exp 1 N=58 of 69 (11 excluded); scores reward 0.5199 (SE .0203), transition 0.4503 (SE .0229), control 0.0310; F(2,1154)=38.77; reward vs transition t(57)=2.89, Bonferroni p=.016; control not different from 0 (p=.22). The 0.52 vs 0.45 pair is read from a figure, not re-checked | Momennejad 2017 (a06, b02, d02) | E (one lab, two samples) |
| Same asymmetry in a decision task; policy revaluation behaves like transition revaluation | Exp 2 N=88 of 115 (27 excluded, 23%); reward vs policy contrast -0.6592, Z=-2.61, p=.0043; policy vs transition 0.14, Z=0.56, p=.58; each beat control p<.0001 | Momennejad 2017 (a08, d03) | E |
| Response time slowest after transition revaluation | RT main effect F(2,171)=7.74, p<.001; transition slower than reward t(57)=2.08, p<.05 | Momennejad 2017 (a07) | S |
| No MF+MB mix can produce the asymmetry; only an SR component can | Model comparison on group means; hybrid SR+MB fit best; different T and R learning rates and prediction-error arbitration tested and rejected | Momennejad 2017 (a21) | S (rival: Kalman TD SR, b04) |
| SR-TD fails detour and policy revaluation; SR-Dyna needs enough replay | Simulation, median over runs; with few samples SR-Dyna fails transition and policy revaluation | Russek 2017 (a09, a20) | E |
| Standard two-step task gives MB no payoff | Weight-vs-reward-rate relation raised about 230x by five task factors jointly; novel task N=199 vs original structure N=207; w vs reward rate r=0.55 (p<.001) vs r=0.10 (p=.15); group difference t(377)=4.71, p<.001; median w 0.27 vs 0.48, z=3.31 | Kool 2016 (a13, a22, a23, b09) | E |
| With clear instructions humans are mostly MB | Spaceship N=21, carpet N=24 vs N=206 earlier data; reward x transition interaction 5.9x larger (95% HDI 4.5-7.3 and 4.7-7.2); BF 145 (carpet), 51 (spaceship); correct MB agent fits median w 0.94, "unlucky-symbol" agent 0.36; Spearman rho=.19 p=.005 between w and fit; 43% had w<0.1. Abstract re-read only; numbers not re-verified | Feher da Silva and Hare 2020 (b06, b07) | E (with Akam, Kool) |
| MF can masquerade as MB | Simulation; correction restores power | Akam 2015 (a14, b08) | E |
| Offline replay predicts replanning | N=24; replanning t(23)=4.89 p<.0001; control t(23)=-0.10; difference t(23)=4.333 p=.0002; replay vs revaluation behaviour rho=0.54 p=.0068; replay Rest 1 > Rest 2 t(23)=2.07 p=.049 | Momennejad 2018 (a15, a24) | S |
| Right dlPFC stimulation lowers MB control | N=25 within-subject; right dlPFC vs vertex p=.01; left p=.89; right vs left p=.13 (laterality not shown) | Smittenaar 2013 (b11) | S |
| Low MB control tracks compulsivity | Exp 1 N=548: OCD beta -0.040 (SE .02) p=.049, about 14% less MB per SD; depression p=.439; anxiety p=.778. Exp 2 N=1413: OCD -0.026 p=.020, eating -0.037 p<.001, impulsivity -0.034 p=.007 | Gillan 2016 (b10) | S |
| RL parameters are unreliable over time | ICC .02-.52 bandit; .01-.71 reversal; .67-.93 personality and cognition | 2024 test-retest (b12) | S (not the two-step weight) |
| SF + GPI transfers old policies to new reward weights | Two theorems; navigation and 12-task arm domain beat per-task DQN | Barreto 2017 (a16, c27) | E |
| Humans reuse a good old policy on a new reward, even if suboptimal | One test trial per person; second-hand | Tomov 2021 via b18 | S |
| Humans and rats on a maze resemble SR agents most | 10x10 grid, 25 blocked configurations, 10 trials each; no coefficients | de Cothi 2022 via b19 | S |
| SR eigenvectors resemble grid fields; give bottleneck subgoals | Simulation; qualitative fit to Krupic, Carpenter data | Stachenfeld 2017 (a12, b20) | S |
| MB control develops late; the skill of deciding when to use it is separable | N=69 children 6-13, MRI N=44 | b13 | S |
| Levodopa boosts retrospective MB inference for MF credit | Placebo-controlled, N not extracted | b14 | S |
| Macaque: MB signs mainly ACC, MF mainly putamen | unit counts not extracted | b15 | S |

## 4. Mechanisms and models

Written so an engineer can build each piece. The agent version of each is in section 7.

**4.1 MF value cache (TD(0)).** Table Q(s,a). After a transition (s,a,r,s'): delta = r + gamma * max_a' Q(s',a') - Q(s,a); Q(s,a) += alpha * delta. Cost per decision: one lookup. Weakness: a changed reward or structure is learned only by new experience, one state at a time.

**4.2 MB planner.** Store a one-step model T(s'|s,a) and R(s,a). Decide by depth-limited search or value iteration: V(s) = max_a [R + gamma * sum T V(s')]. Cost per decision grows with branching^depth. Strength: any model edit changes the next decision.

**4.3 SR.** Matrix M[s,s'] = expected discounted visits to s' starting in s under policy pi. Closed form: M = (I - gamma P_pi)^-1, where P_pi is the policy's transition matrix. Online rule (Stachenfeld 2017, a11): M(s,s') += alpha * [I(s_t=s') + gamma * M(s_{t+1},s') - M(s_t,s')], alpha=0.1 in their simulations, applied to the row of the state just left. Value: V = M @ r, where r is a reward vector learned separately (r[s] += alpha_r * (reward - r[s])). Decision: for each action, one-step lookahead using V of the successor. Cost: a matrix-vector product. Properties:
- Reward change: edit r. V updates at once. (Supported in humans, a06.)
- Transition change: M is stale until relearned or recomputed. (Failure of SR-TD, a09.)
- Policy change: M was made under the old policy. The best action may change with no transition change. (Policy revaluation, a08.)
- Discount gamma sets the horizon. Eigenvectors do not depend on gamma; eigenvalues do (a25). Keep a short-horizon and a long-horizon M.
- Eigenvectors of M equal graph Laplacian eigenvectors, so low-frequency ones partition the graph. Thresholding gives bottleneck states, usable as subgoals (a12, c28).

**4.4 SR-MB (recompute).** Keep a learned one-step P_pi. At decision time, recompute M = (I - gamma P)^-1. Solves detour. Cost: a matrix inverse after each change. (c25)

**4.5 SR-Dyna (replay).** Store transitions. Between decisions, sample stored (s,a,r,s') and apply the SR update (and the Q update) as if they had just happened. Enough samples fix transition and policy revaluation. (a09) Prioritise by surprise (unsigned prediction error): replay in the brain follows this (a15, a24), but the evidence is N=24 and correlational.

**4.6 Successor features + GPI.** Define features phi(s,a) and reward r = phi . w. Successor features psi^pi(s,a) = expected discounted sum of phi under pi. Q^pi(s,a; w) = psi^pi(s,a) . w. For a new task w', evaluate every stored policy: Q_i = psi_i . w'. Act by max over policies and actions (GPI). The new policy is at least as good as the best stored one. Requires reward linear in known features (a16).

**4.7 Arbitration.** Daw 2005: use whichever controller is more certain (a03, not opened). Kool 2016: use MB when its expected gain in reward rate exceeds the cost of effort (a13). A usable engineering rule: plan only when cache and planner disagree often enough, or when a prediction check fails (a23, a07).

**4.8 The Kalman alternative.** Keep a mean and covariance over each successor row. Update non-locally from prediction errors weighted by uncertainty. Gives partial transition revaluation without a model. Second-hand here (b04).

**4.9 Diagnostics.** (a) Stay-probability regression: stay ~ reward x transition (rare/common). MB sign: the interaction. MF sign: the reward main effect. Caveats in section 5. (b) Revaluation contrast: score on reward change minus score on transition change. Zero gap suggests planning; a positive gap suggests a cache (a21). (c) Policy revaluation is the hard case that separates SR from MB with replay.

## 5. What holds up

**Solid.**
- The SR math and its policy dependence. Stated by Dayan 1993, simulated by Russek 2017. [E]
- Reward-change adaptation beats transition-change adaptation in humans, replicated in a second sample (Momennejad Exp 1 and 2). Two samples from one lab. The effect is small: about 0.07 on a 0-1 scale in Exp 1, p=.016 after correction. Exclusions are large: 11 of 69 in Exp 1, 27 of 115 in Exp 2 (23%), the latter for failing to learn the phase 1 policy, which may select better learners (d03). [E, with caveats]
- Planning payoff matters for how much MB control appears (Kool 2016, r=0.55 vs 0.10). [E]
- A hybrid MF+MB label from the standard task is not a clean finding about the person or the system. Three lines agree: Akam (MF can mimic MB), Kool (no payoff in the task), Feher da Silva and Hare (misunderstood instructions look like MF influence). [E]

**Failures and tensions.**
- Daw 2011 (61% MF, N=17) versus Feher da Silva and Hare 2020 (mostly MB with good instructions). Both are true of their own samples. The 2011 weights are probably inflated by misunderstanding.
- SR as a brain mechanism: Momennejad 2017 favours SR+MB. A Kalman TD SR (Geerts 2024, b04) also fits. The human data do not pick one. The SR+replay design is not forced by the evidence. No independent human test of the Kalman account was found (d16). [C]
- Place-field prediction miss: fields at reward are not larger, as the SR predicts (a11).
- Many SR eigenvectors do not look like canonical grid cells (a12).
- Individual-difference effects are small and noisy: the Gillan OCD effect is p=.049 in Exp 1; test-retest reliability of RL parameters is poor (ICC .02-.52). A single-run MB weight is a weak measure. [S]
- Brain-stimulation lateralisation not shown (right vs left p=.13, b11).

**Moderators that changed results.**
- Task payoff for planning (Kool).
- Instruction clarity (Feher da Silva and Hare: interaction 5.9x larger).
- Time on task raised the revaluation score, F(1,57.3)=9.92, p<.01, with no interaction by condition (a26).
- Age (b13) and dopamine (b14): MB signatures rise with development; levodopa shifts credit assignment.
- Replay budget: too few replay samples degrade Dyna-Q to MF; SR-Dyna degrades more gently (a09).

**Interventions that worked.** Clearer cover story (humans). A task where planning pays (humans). Replay or recomputation after a structure change (models). In LLMs: see section 6.

**Interventions that did not work, or did little.** BFS or DFS prompts in CogEval helped slightly (c08). Code fine-tuning did not raise model-basedness (c05). Temperature had no effect on CogEval (chi2(11)=1.28, p=.53, d04). A hard constraint from a memory graph lost 4.8 points against soft guidance (d09).

**Reading limits.** Opened primary texts: Dayan 1993, Daw 2011, Momennejad 2017 (Exp 1 and 2 statistics from full text), Russek 2017, Kool 2016, Stachenfeld 2017, Barreto 2017. Not opened: Daw 2005, Tolman, Sutton 1990, Gershman 2018, Dolan and Dayan 2013, Geerts 2024, Tomov 2021, de Cothi 2022 (the last three second-hand through the Carvalho review). In the cross-check, the Feher da Silva and Hare numbers were not re-verified beyond the abstract. The Momennejad 0.52 / 0.45 pair is from a figure. Two evidence rows for Momennejad 2017 probably share one reading, so count them as one source.

## 6. Language models

All results below are 2022-2026 studies. Almost none use current frontier or reasoning models with the standard two-step regression (critique, gap 4).

**Two-step task.**
- GPT-3 (text-davinci-002), Binz and Schulz (c01, c02, b21): stay probability fell after a rare transition with reward, t(1982)=-6.16, p<.001, and rose after a rare transition without reward, t(1814)=2.33, p=.01. 200 simulations of 20 trials, only 3 previous trips shown in the prompt. Sign pattern only, no fitted MB weight. The same paper reports failures on the Cognitive Reflection Test and sensitivity to small prompt changes. [S]
- CogBench (c03-c05, b22): 35 LLMs. Model-basedness rises with parameter count (beta=0.481, z=4.2, p<.001). Chain of thought raised it by 64.59% and step-back by 118.59%, relative to base models and averaged over the models tested. Code tuning and data size: not significant. GPT-4 was above human level; proprietary models that solve the task are at least on par with humans. The metric is a regression weight, so the Akam and Feher da Silva caveats apply. Step-back (restate the structure first) beat step-by-step. [S]
- Centaur (c23, b33): Llama 3.1 70B fine-tuned on Psych-101 (160 experiments, over 60,000 people, over 10 million choices) reproduced MF, MB and mixed two-step trajectories and a new cover story. Held-out NLL 0.4998 versus 0.6075 and 0.6043 in the other columns (column labels unclear in extraction). LAPITHS (c24): retrieval-augmented agents given the reward structure matched its likelihood without fine-tuning. A good fit does not show a cognitive mechanism. [C]
- Rigidity (d15): in two-arm bandits LLMs show low learning rates and very high inverse temperatures. Stable across four decoding settings; that is not test-retest reliability.

**Cognitive maps and revaluation (CogEval: c06-c09, d04, b24).**
- 8+ LLMs, 6 graphs, 3 domains, 30 runs per prompt, three temperatures. GPT-4: 1stepPath 0.99, 2step 0.82, 3step 0.55, nstep 0.47, rewardReval 0.67, transReval 0.60, nonteleDetour 0.55, nonteleShortcut 0.56. Smaller models mostly 0.1-0.4.
- Policy revaluation, the case that separates SR-style caching from planning, was hardest: GPT-4 0.21, GPT-3.5 0.18, davinci-003 0.13, Claude-1 0.28, Pythia-20B and Cohere 0.00.
- The human asymmetry does not show as a consistent LLM pattern. Reward minus transition revaluation: +0.07 (GPT-4), -0.02 (GPT-3.5), -0.15 (davinci), -0.07 (Claude-1), SDs near 0.4, no paired test (d04). The large LLM gap is policy revaluation, not reward versus transition.
- Failures: invented edges, long routes, loops. GPT-4 found a shortest path one cluster away in 0 of 30 runs at temperature 0, and at most 10% at other temperatures. BFS or DFS instructions helped little. A worked-example chain of thought gave GPT-4 and GPT-3.5 1.00 on one non-teleporting shortcut but 0.50 on the teleporting version, which looks like a memorised procedure, not map understanding (c09).
- Temperature: no effect (p=.53).
- 2023 models only. [S]

**What LLMs build internally (Demircan et al.: c12, c13, b23).** Llama-3.1-70B watching a random walk on a 15-node, 3-community graph (401 observations, 20 runs). Sparse autoencoder latents correlate with the SR at max r=0.62 versus 0.49 for the transition matrix. TD-error latent r=0.60 versus transition surprise r=0.18 (r=0.58 with the Q-learning TD error in block 34 on the two-step variant). Next-state accuracy 24.3% against a 25% ceiling; lesioning the TD latent cut it to 18.9%. Two-step NLL 2729 (Q-learning) versus 2864 (myopic). The 8B model stayed at chance. Max correlations over many latents inflate r. One lab, one model family. [S]

**Mechanisms in trained transformers.** Linear-attention transformers can implement TD in the forward pass (proved, c14, b31). A meta-trained transformer reached near-max return after one reward exposure and found shortcuts in over 60% of test runs, with predictive-map-like representations and cached intermediate results in memory tokens (c15, b25). GPT-2 trained on random walks formed a map-like code (100% single-step accuracy at 2-3 steps, 71% near 11 steps, over 96% past 30 steps); trained on shortest paths it was 100% in distribution and 0% at other context lengths (c21, d06). Lampinen et al. (c22, b27): without in-context-learning sequences in training, even oracle retrieval left reversals at about 12% and codebooks at about 6%; with them, retrieval gave large gains. All trained from scratch or by the authors. Not prompt tests. [S]

**Using the idea at inference time.**
- World-model planning. RAP (c16, b28), LLaMA-33B, Blocksworld 2/4/6 steps: CoT 0.17/0.02/0.00; RAP(10) 1.00/0.86/0.26; RAP(20) 1.00/0.88/0.42; GPT-4 CoT 0.50/0.63/0.40. Average 64%, 33% relative gain over GPT-4 CoT. Cost: 10-20 search iterations per problem. WebDreamer (c17): VisualWebArena reactive 17.6, tree search 26.2, GPT-4o WebDreamer 23.6; Online-Mind2Web 26.0 vs 37.0; Mind2Web-Live 20.2 vs 25.0. Imagination used about 3x fewer steps and 10x lower latency (Reddit 972 s vs 234 s), and was 4-5x more efficient. Correction from the cross-check: it is below tree search on VWA, not equal; "45 times" in an earlier row was a page number. Dyna-Think (d14): a trained 32B agent matched best-of-n of a 685B R1 at half the tokens; trained, not prompt-only. [E for "simulation beats reactive"; no budget-matched comparison exists]
- Modular planning (MAP: c10, c11, b30). Monitor, state predictor, evaluator, decomposer, orchestrator. Graph traversal: zero invalid actions; Valuepath 100%. Tower of Hanoi 3-disk: nearly seven-fold gain over GPT-4 zero-shot; 4-disk out-of-distribution baselines near 0% while MAP made no invalid moves. PlanBench Logistics 24 versus CoT 17, ICL 12, zero-shot 7; Mystery Blocksworld 27.4 versus 10.6. StrategyQA 87.7 versus CoT 84.7. Removing the monitor raised invalid moves from 0 to 31%. Many LLM calls per problem; best-of-5 numbers are optimistic. [S]
- Memory as cached values (GAMER, c18). Graph of past actions with TD-learned suggestion and avoidance values. Success 31.60 versus vanilla 26.31, averaged over 4 LLMs and 4 benchmarks. Other memories: A-Mem 29.07, Reflexion 20.81, Voyager 22.76, MemoryBank 22.30, ReasoningBank 12.58. About 50% fewer tokens than A-Mem. Several published memories sit below vanilla. One-step values, not an SR. Authors' own preprint. [S]
- Memory as structured map (d08, d09). WebATLAS on WebArena-Lite (Claude-4-Sonnet, one run each): base 47.9, raw map 44.8, structured map 57.4, full stack with look-ahead 63.0; raw map on the Multisite split 19.2 versus 30.8 base. ProPlay on ScienceWorld: 37.4 versus ExpeL 36.3, Reflexion 32.2, ReAct 27.0; without graph 34.8; hard constraint 32.6 (4.8 lower than soft guidance). Not equal-token; the graphs are not discounted occupancies. [S]
- SR on the agent system (Parks and Alharthi 2026: c19, d05). SR of an LLM communication graph, Qwen2.5-7B, 12-step state tracking, 100 trials per topology, 3 topologies. Rank correlations +1.0 (condition number), +0.5 (spectral gap), -1.0 (spectral radius, inverted). Three points only. Error amplification: chain 2094, mesh 1241, star 1184. [S]
- Replay and gates (d10-d13). ECHO (in-context hindsight rewriting) beats Reflexion and AWM on XMiniGrid; up to 80% over vanilla; mixed across five organisations. Prioritised replay exists only in fine-tuning (d11). AdaptThink (trained): length down 50.9/63.5/44.7%, accuracy up 4.1/1.4/1.6 points (1.5B model). DART (training-free draft agreement): thinking tokens down 32-73%, accuracy up to +9.0 (math) and +22.5 (code). [S]
- Latent learning in post-training (d07): modest gains, training-time. Background.
- Search result: no LLM-agent memory built on successor representations was found in about 12 queries and a second pass of about 30 arXiv queries (c29, d16). Absence is weak evidence.

**What changed LLM behaviour and by how much (summary).** Size (beta 0.481), chain of thought (+64.59%), step-back (+118.59%), explicit simulation of outcomes (RAP, WebDreamer), a code-side validity monitor (31% invalid moves without it), a structured instead of raw map (57.4 vs 44.8 on WebArena-Lite). What did not: code tuning, temperature, BFS/DFS prompts (little).

## 7. What our agent should take

Status marks: [E] established, [S] single-source, [C] contested. Schema parts: G guardrail, S state, O operator, memory = SCHEMA section 5. Claim ids K##; evidence ids in brackets. The schema is run by code with the model filling slots (SCHEMA section 1). Everything below keeps that rule.

### Add now (established)

1. **Tag every stored "where does this lead" record with the policy that made it, and invalidate it on a signal.** Record per entry: the operator mix and prompt version used, and the class. Invalidate when (a) the class's best-known action changes, (b) a prediction from the record fails a check, or (c) the operator mix changes. Part: memory. [E] K01, K05; a01, a02, a09, a20, b16, b17. Reason: the SR is tied to its policy; both transition change and policy change leave it stale. This fits G1: the trigger is a signal, not a clock.
2. **Keep what the world does separate from what this task wants.** Store class-level transition facts apart from the rubric or goal. A new goal edits the rubric only. Part: memory. [E] K13, K01; a01, a16, c27. Cheap, because it is only a layout rule for the memory record.
3. **When measuring or labelling the agent's control mode, never use one stay/switch signature.** Add a cache-fail control (a case where a cached shortcut gives the wrong answer) and test prompt ambiguity first. Part: logging and evaluation (SCHEMA section 6), with G3 (a pass must be on something not fitted). [E] K07; a14, b06, b07, b08.
4. **Do not infer planning ability from a likelihood or a fit.** Evaluate by outcome on items where the cache fails. Part: evaluation. [C] K25; c23, c24.
5. **Plan only where planning pays.** Record per class whether simulation beat the plain attempt; skip simulation where it did not. This is G12 with a measured basis. Part: G12. [E] K06; a13, a22, a23, b09. The payoff-aware gate itself is not yet priced for an LLM (see Test first, T8).

### Test first (single-source, contested or untested)

| # | Item | Part | Status | Evidence |
|---|---|---|---|---|
| T1 | Class-transition memory (next-class frequencies, discounted, from past runs) versus no memory and versus raw-trace memory | memory | [S] | K01, K28, K32, K33; a01, d08, d09, c29 |
| T2 | Surprise-ranked retry notes (replay of high-error failures between attempts) versus recency order | S5/S6, memory | [S] | K11, K35; a15, a24, d10 |
| T3 | One-step imagination of each candidate before commit, versus reactive and versus tree search at equal tokens | O (new use of existing operators) | [S] | K19, K20, K36; c16, c17, d14 |
| T4 | Validity monitor guardrail that rejects invalid moves against a code-held graph | G | [S] | K18; c10, c11 |
| T5 | Step-back (restate structure first) before planning items | S1/O6 | [S] | K16; c04 |
| T6 | Cached-strategy reuse with a mismatch check (successor-feature style): pick the best old strategy for the new goal, then refine | memory | [S] | K13, K14; a16, b18 |
| T7 | Bottleneck states of the agent's own state graph as subgoal candidates | S/O3 | [S] | K12; a12, c28 |
| T8 | Draft-agreement gate, then a payoff-aware gate, before expensive planning | G11/G12 | [S] | K34, K06; d13, a13 |
| T9 | Explicit graph state in the prompt (edges and visited list) on CogEval-type items with current models | S2 | [S] | K17, K30, K37; c06, c07, d04 |
| T10 | Memory as soft advice versus forced plan | memory | [S] | K33; d09 |

Notes. T1 is the central unmeasured item: no study of an SR-style class-transition memory in an LLM agent was found. Two training-free agents with structured transition graphs beat Reflexion-style memory (d08, d09), but without matched tokens. T10 follows from ProPlay: advice the agent may override beat a forced plan by 4.8 points. All of these stay out of SCHEMA.md until the tests in UNKNOWNS.md pass.

Links to neighbouring subfields (not covered here): model-based versus model-free control as a general theory; exploration versus exploitation; active systems consolidation (replay); language agents as architectures; heuristic search; impasse-driven subgoaling and chunking; metacognition and control.

## 8. Concrete tests on our bench

All arms get the same token budget (G7). Counted steps in code; the model fills slots. Use at least 5 seeds per item, report intervals. Log per SCHEMA section 6.

| Test | Item type | Arms (equal tokens) | Metric | Expected effect |
|---|---|---|---|---|
| E1 Class-transition memory | Repeated problem classes with 2 to 3 variants each (ARC-style families; multi-step puzzles where an earlier step type predicts the next) | (a) no memory; (b) raw trace of 3 prior runs; (c) class-transition table (next-class counts, discounted, tagged with operator mix) shown after the first attempt | Pass rate at budget; tokens to first pass | (c) above (a) by about 3 to 8 points; (c) above (b) by a few points. The WebATLAS structured-vs-raw gap was 12.6 points, but one run |
| E2 Staleness | Same classes, then change the operator mix or the checker rule midway | (a) memory with policy tag and invalidation; (b) memory without; (c) no memory | Pass rate after the change; drop versus before | (b) falls below (a); (b) may fall below (c) |
| E3 Reward vs structure change | Text graph tasks: change the goal rubric in one set, an edge in another, a distal reward that flips the best first action in a third | Plain; scaffold with code-held edges; scaffold plus replay over stored episodes | Revaluation score per type (as CogEval); paired difference reward minus transition; policy revaluation score | Plain near CogEval levels (policy about 0.2 for 2023 models); scaffold lifts policy revaluation most |
| E4 Imagination vs search | Multi-step planning (Blocksworld, small web or tool tasks) | Reactive; one-step imagination of each candidate then commit; small tree search | Success at equal tokens; invalid-move rate | Imagination above reactive; search above imagination only if the budget allows (direction from c17) |
| E5 Surprise-ranked retry notes | Items where the first attempt fails | Retry with notes ranked by (a) recency, (b) surprise (gap between predicted and actual check output), (c) none | Pass rate on second and third attempt | (b) above (a) by a few points; no gain if few items fail |
| E6 Payoff-gated planning | Mixed set where planning helps in some classes and not others | Always plan; never plan; plan only in classes with measured gain; draft-agreement gate | Pass rate and tokens | Gated arm matches always-plan at 30 to 60% fewer tokens (d12, d13 give the range; trained or best-case) |
| E7 Validity monitor | Graph and puzzle moves | Scaffold with and without a code-side move validator | Invalid-move rate; solves | Without it, invalid moves rise toward 31% on Hanoi-like tasks (c11) |
| E8 Step-back | Planning items | Plain; CoT; step-back | Pass rate | Step-back above plain; CoT gains more on probabilistic items (c04) |
| E9 Mode-label reliability | Same two-step prompt, 20 repeats | Single-run versus 20-run estimate | Variance of the stay regression across repeats | Large run-to-run variance (human ICC .02-.52 for bandit parameters) |
| E10 Soft vs hard memory | E1 tasks | Memory as advice versus as forced plan | Pass rate | Soft above hard by about 5 points (d09) |

## 9. What does not transfer, and why

- **The brain claims.** Place cells, grid cells, striatal prediction errors, dlPFC stimulation, development, dopamine: no use for a scaffold. We take the computation only. And the SR as the brain's mechanism is itself contested (Kalman rival).
- **The MB weight as a trait.** Person-level and model-level scores are unreliable (ICC .02-.52 for bandit parameters) and depend on instructions and payoff. Do not route the agent by a mode score from one run.
- **Stay-probability signatures as proof of planning.** MF strategies mimic MB (Akam); the task rewarded planning very little (Kool); misunderstanding fakes MF (Feher da Silva and Hare).
- **Dense numeric SR tables.** The SR needs a state space. Our problem classes are not states in a fixed MDP. Use class-level next-class counts as a coarse analogue; do not treat M as an exact object. The nearest direct LLM evidence uses a graph of pages or stages, not occupancy matrices (d08, d09).
- **Learning by TD updates inside weights.** Demircan, Wang, Fang and Rajan show in-context TD-like computation in transformers, but the agent cannot rely on it: the 8B model stayed at chance, and the trained-transformer results use meta-trained or small models.
- **Training-regime findings.** Random-walk versus shortest-path training (GPT-2), latent learning in post-training, Dyna-Think, AdaptThink, PPER. They all train. Our agent is frozen. Background only.
- **Centaur's fit.** Fine-tuning on human choices reproduces behaviour; it does not tell us the base model plans. Retrieval agents matched it (c24).
- **Parks and Alharthi's spectrum.** Three topologies, rs of +-1, one 7B model. Not a design rule.
- **Revaluation asymmetry in LLMs.** The human reward-over-transition gap is not found in CogEval (d04). Do not assume the agent shows human-like caching behaviour.
- **Hard routing by cached structure.** ProPlay: forcing the plan lost 4.8 points. A cache should advise, not command (consistent with G1 and G2).

## 10. Open questions

1. Does a class-transition memory built from past runs beat no memory and raw-trace memory (Reflexion, GAMER) at equal tokens? No direct test (critique gap 1).
2. How does such memory fail when the operator mix or prompt changes? No measured LLM case; the nearest is Parks 2026 (gap 2).
3. When is one-step imagination worth its tokens against tree search and plain CoT at matched budget on current models? Dyna-Think is trained; WebDreamer is not budget-matched (gap 3).
4. Do current frontier and reasoning models still fail CogEval policy revaluation (0.21 for GPT-4), and does explicit graph state close the gap? No 2025-2026 re-run found (gap 4).
5. Is the human reward-over-transition asymmetry reproduced in LLMs under a paired test? CogEval shows no consistent pattern, with no paired p value (gap 5).
6. Is there independent human data that favours a Kalman TD SR over SR+MB? Only a 2019 ML paper found (gap 7).
7. Does a payoff-aware gate (Kool-style) cut tokens without losing accuracy in an LLM? Gates exist (AdaptThink, DART); none is payoff-aware (gap 8).
8. Does surprise-ranked replay between attempts help a frozen model? Hindsight replay helps in one setting; prioritised replay exists only in fine-tuning (gap 9).
9. How reliable is an LLM MF/MB index across runs? No ICC for LLMs (gap 10).
10. The exact Momennejad Exp 1 means (0.52 vs 0.45) and the Exp 2 test statistics beyond the contrasts are not re-read from the figures.
11. Do the Feher da Silva and Hare numbers hold on a full-text check? Only the abstract was re-read.

## 11. Sources

[V] opened this session, [M] snippet, abstract only or not opened.

- [V] Dayan (1993) The successor representation. https://www.gatsby.ucl.ac.uk/~dayan/papers/d93b.pdf (a01, a02, a20, b17)
- [M] Daw, Niv, Dayan (2005) Uncertainty-based competition. https://www.nature.com/articles/nn1560 (a03)
- [V] Daw et al. (2011) Model-based influences. https://pmc.ncbi.nlm.nih.gov/articles/PMC3077926/ (a04, a05, b01, d01)
- [V] Momennejad et al. (2017) SR in human RL. https://pmc.ncbi.nlm.nih.gov/articles/PMC6941356/ ; https://www.biorxiv.org/content/10.1101/083824v1.full (a06-a08, a21, a26, b02, b03, d02, d03)
- [V] Russek et al. (2017) Predictive representations. https://journals.plos.org/ploscompbiol/article/file?id=10.1371/journal.pcbi.1005768&type=printable ; https://pmc.ncbi.nlm.nih.gov/articles/PMC5628940/ (a09, a10, a20, b16, c25)
- [V] Stachenfeld, Botvinick, Gershman (2017) Hippocampus as predictive map. https://www.biorxiv.org/content/biorxiv/early/2017/06/07/097170.full.pdf (a11, a12, a25, b20)
- [V] Kool, Cushman, Gershman (2016) When does MB control pay off? https://pmc.ncbi.nlm.nih.gov/articles/PMC5001643/ (a13, a22, a23, b09)
- [V] Akam, Costa, Dayan (2015) https://pmc.ncbi.nlm.nih.gov/articles/PMC4686094/ (a14, b08; parts read)
- [V] Momennejad et al. (2018) Offline replay. https://elifesciences.org/articles/32548 (a15, a24, b05)
- [V] Barreto et al. (2017) Successor features. https://arxiv.org/pdf/1606.05312 (a16, c27)
- [M] Sutton (1990) Dyna. https://www.sciencedirect.com/science/article/pii/B9781558601413500304 (a17)
- [M] Tolman (1948) https://doi.org/10.1037/h0061626 (a18)
- [M] Gershman (2018) https://www.jneurosci.org/content/38/33/7193 (a19)
- [M] Dolan and Dayan (2013) https://doi.org/10.1016/j.neuron.2013.09.007 (a27)
- [M] Sutton and Barto (2018) http://incompleteideas.net/book/the-book-2nd.html (a28)
- [V] Carvalho et al. (2024) Predictive representations review. https://arxiv.org/abs/2402.06590 (b04, b18, b19, c29); Geerts et al. (2024), Tomov et al. (2021), de Cothi et al. (2022) are second-hand through it [M]
- [V] Feher da Silva and Hare (2020) https://www.biorxiv.org/content/10.1101/682922v4 (b06, b07; abstract re-read only in the cross-check)
- [V] Gillan et al. (2016) https://pmc.ncbi.nlm.nih.gov/articles/PMC4786435/ (b10)
- [V] Smittenaar et al. (2013) https://pmc.ncbi.nlm.nih.gov/articles/PMC3893454/ (b11)
- [V] Test-retest reliability of RL parameters (2024) https://pmc.ncbi.nlm.nih.gov/articles/PMC11289054/ (b12)
- [V] Metacontrol in childhood (2023) https://pmc.ncbi.nlm.nih.gov/articles/PMC10329104/ (b13)
- [V] Dopamine and MF credit assignment (2021) https://pmc.ncbi.nlm.nih.gov/articles/PMC8758138/ (b14; abstract level)
- [V] Primate single-neuron MB/MF study (eLife 2026) https://pmc.ncbi.nlm.nih.gov/articles/PMC13286570/ (b15; intro and reply only)
- [V] Binz and Schulz (2023) https://arxiv.org/abs/2206.14576 (b21, c01, c02)
- [V] Coda-Forno et al. (2024) CogBench https://arxiv.org/abs/2402.18225 (b22, c03-c05)
- [V] Demircan et al. (2024) https://arxiv.org/abs/2410.01280 (b23, c12, c13)
- [V] Momennejad et al. (2023) CogEval https://arxiv.org/abs/2309.15129 ; https://arxiv.org/pdf/2309.15129 (b24, c06-c09, d04)
- [V] Fang and Rajan (2025) https://arxiv.org/abs/2506.19686 (b25, c15)
- [V] Baumgartner et al. (2025) https://arxiv.org/abs/2511.13371 (b26, c21, d06)
- [V] Lampinen et al. (2025) https://arxiv.org/abs/2509.16189 (b27, c22)
- [V] Hao et al. (2023) RAP https://arxiv.org/abs/2305.14992 (b28, c16)
- [V] Gu et al. (2024/2025) WebDreamer https://arxiv.org/abs/2411.06559 (b29, c17)
- [V] Mondal, Webb, Momennejad (2025) MAP https://arxiv.org/abs/2310.00194 (b30, c10, c11)
- [V] Wang et al. (2025) Transformers learn TD https://arxiv.org/abs/2405.13861 (b31, c14)
- [V] Parks and Alharthi (2026) https://arxiv.org/abs/2605.11453 ; https://arxiv.org/pdf/2605.11453 (b32, c19, d05)
- [V] Binz et al. (2025) Centaur https://arxiv.org/abs/2410.20268 (b33, c23)
- [V] LAPITHS (2026) https://arxiv.org/abs/2604.27927 (c24)
- [V] Zheng et al. (2026) GAMER https://arxiv.org/abs/2607.27415 (c18)
- [V] Immertreu et al. (2026) neural SRs on language https://arxiv.org/abs/2605.24585 (c20; not an agent study)
- [V] Kulkarni et al. (2016) Deep SR https://arxiv.org/abs/1606.02396 (c26)
- [V] Machado et al. (2017) Laplacian option discovery https://arxiv.org/abs/1703.00956 (c28)
- [V] Xiong et al. (2026) latent learning in LLMs https://arxiv.org/pdf/2601.22474 (d07)
- [V] Cheng et al. (2025) WebATLAS https://arxiv.org/pdf/2510.22732 (d08)
- [V] Ma et al. (2026) ProPlay https://arxiv.org/pdf/2606.12780 (d09)
- [V] Hu et al. (2025) ECHO https://arxiv.org/pdf/2510.10304 (d10)
- [V] Chen et al. (2024) PPER https://arxiv.org/pdf/2410.12236 (d11; abstract and intro)
- [V] Zhang et al. (2025) AdaptThink https://arxiv.org/pdf/2505.13417 (d12)
- [V] Lee et al. (2026) DART https://arxiv.org/pdf/2606.23181 (d13)
- [V] Yu et al. (2025) Dyna-Think https://arxiv.org/pdf/2506.00320 (d14)
- [V] Wang, Ward, Zhang (2026) Rigidity in LLM bandits https://arxiv.org/pdf/2603.07717 (d15)
- [V] Search log 2026-10-31 https://export.arxiv.org/api/query (d16)

## Source audit (2026-11-01)

Fresh auditors re-opened the sources of 5 established claims: 3 confirmed as written, 2 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **B05.02-K05** (now single-source: the sources are not independent). Both the human result (Momennejad et al. 2017, N=88, policy resembles transition revaluation and differs from reward revaluation, p=.0043 / .5771) and the simulation (Russek et al. 2017) come from the same research group (Momennejad, Russek, Botvinick, Daw, Gershman are on both); the Dyna repair is simulation-only, and b03's cited 'Carvalho 2024 review' URL is actually the Momennejad paper.
- **B05.02-K07** (reworded: the sources support less). Akam et al. 2015 show model-free strategies can look model-based (the opposite artefact: false MB signatures), so they do not support 'apparent model-free influence is an artefact'; only Feher da Silva & Hare 2020 supports the false-hybrid / mostly-MB claim, and it is one lab's single study (spaceship N=21, magic carpet N=24). Corrected claim: Two-step task signatures are ambiguous in both directions: model-free strategies can mimic model-based behaviour (Akam et al. 2015, simulations), and pure model-based agents with a wrong task model are labelled hybrid (median w 0.36 or 0.80 vs 0.94 for a correct model); with a detailed story and comprehension checks, humans in one study (Feher da Silva & Hare 2020, N=21 and N=24) were mostly model-based (median w 0.78-0.79).
- **B05.02-K02** (now single-source: only one opened source, code check).
- **B05.02-K03** (now single-source: only one opened source, code check).
- **B05.02-K06** (now single-source: only one opened source, code check).
- **B05.02-K13** (now single-source: only one opened source, code check).
