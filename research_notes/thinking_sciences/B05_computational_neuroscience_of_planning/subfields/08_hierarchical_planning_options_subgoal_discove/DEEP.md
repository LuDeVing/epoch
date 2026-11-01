# Hierarchical planning, options, subgoal discovery: deep document

*Subfield B05.08. Written 2026-11-01 from evidence_a-d.jsonl (a01-a31, b01-b25, c01-c28, d01-d18), claims.jsonl (K01-K27) and critique.md in this folder. Evidence ids in brackets. Status marks follow SCHEMA.md: [E] established, [S] single source, [C] contested.*

## 1. What it is

Hierarchical planning means planning with big steps. Instead of choosing one primitive action at a time, the planner chooses a subgoal ("get to the doorway", "solve the left half"), runs a routine that reaches it, and then plans the next subgoal. In reinforcement learning (RL) the routine plus its start and stop rules is called an option. The formal object is: initiation set (where it can start), policy (what it does), termination condition (when it ends). [a30, not opened; used as the standard definition by all opened papers]

The hard problem is subgoal discovery: where do good subgoals come from? Two answers were named in the founding neuroscience review: subgoals found as bottlenecks on rewarded trajectories, or found by analysing the structure of the problem graph. [a21] A third answer, added later, is that a language model proposes them. [a28, a29, c13, c14]

This subfield sits between three bodies of work.
- Computational neuroscience: the successor representation (SR) and its eigenvectors as a basis for chunking experience and finding subgoals. [a27]
- RL: eigenoptions, covering options, bottleneck options, successor options.
- Human behaviour: do people choose bottlenecks and communities as subgoals, and do they pay for it with errors?

For our agent the question is narrow. Our scaffold (SCHEMA.md) has operator O3 Decompose at impasses (S6) and a planned "subgoal library" in the memory section, marked [D]. This document asks what is known about (a) how to find good subgoals, (b) how many to keep, (c) how to admit and retire them, and (d) when decomposing pays at equal tokens.

Scope warning. Almost all of the structural work (eigenvectors, bottlenecks) runs on state graphs of grids and games. Our agent solves reasoning items in text and has no given state graph. The portable parts are the design lessons, not the algorithms.

## 2. History and theories in depth

### 2.1 Options and the first discovery rules (1999 to 2009)

- Sutton, Precup and Singh (1999) defined options and the semi-Markov theory. [a30, not opened]
- Early discovery rules were "top-down" and bottleneck-based: diverse density on successful trajectories (McGovern and Barto 2001), betweenness centrality (Simsek and Barto 2004), and Q-cut (Menache et al. 2002). [a31, second-hand only]
- Botvinick, Niv and Barto (2009) mapped options to prefrontal cortex. Each option has a pseudo-reward for reaching its subgoal. Prediction errors are computed inside the option and again for the whole option. They named the open problem: how are new useful routines found? Two proposed answers were bottlenecks on rewarded trajectories and analysis of the problem graph. They also proposed intrinsic motivation: unexpected salient events become subgoals. [a21, a22] The mapping to cortex is a proposal, not proven.

### 2.2 Human evidence for subgoals (2011 to 2014)

- Ribas-Fernandes et al. (2011): in a delivery game, brain signals tracked change in distance to a subgoal separately from change in distance to the final goal (pseudo-reward prediction error, PPE). [a23, b14]
- Schapiro et al. (2013): people segment a stream at community boundaries even when local transition statistics are equal. [a24, a25]
- Solway et al. (2014): theory of optimal hierarchy (the decomposition that minimises planning cost equals Bayesian model selection over decompositions). Four human experiments show people pick bottlenecks as subgoals. [a19, a20, b12]

### 2.3 The SR and Laplacian line (2017 to 2023)

- The SR approximates the inverse of the graph Laplacian. Its eigenvectors tile the state space and can be used to partition and chunk experience, find subgoals and define eigenoptions. [a27] Momennejad (2020) is the review that states this link. It adds a risk: a policy-dependent SR over-represents bottlenecks and goals, so its eigenvectors depend on how the agent has behaved (a prediction, untested). [a27]
- Machado, Bellemare and Bowling (2017) made the Laplacian idea concrete: each eigenvector gives an intrinsic reward ("eigenpurpose") and a trained option (an eigenoption). No task reward is used. [a01, c01]
- Machado et al. (2018) moved it to stochastic transitions and pixels with the deep SR. [a09, a10, b03]
- Jinnai et al. (2019) proposed covering options (add edges that maximise algebraic connectivity, i.e. the Fiedler vector) and proved that choosing the best option set is NP-hard. [a16, a17, b08, b09]
- Ramesh et al. (2019) proposed successor options: cluster SR vectors, use centroids as subgoals. [a18]
- Wu, Tucker and Nachum (2019) and Gomez, Bowling and Machado (2024, ALLO) worked on learning the eigenfunctions in deep RL. ALLO shows the earlier objective had a rotation problem and needed tuning against the true answer. [b05, b06]
- Machado, Barreto, Precup and Bowling (2023, JMLR) is the long synthesis. It adds the option keyboard (linear mixes of base options). [a11, a12, b04, c19]
- Klissarov and Machado (2023) made the method fully online from pixels (DCEO). [a14, a15, b07, c07]

### 2.4 Doubt about why hierarchy works

- Jong, Hester and Stone (2008), second-hand: option benefits came mainly from exploration and replay. [b11, not opened]
- Nachum et al. (2019): most of the benefit of hierarchical RL comes from better exploration, not easier policy learning. A flat agent trained on the hierarchical agent's data is nearly as good. [b10]

### 2.5 Human option learning and transfer (2020 to 2025)

- Eckstein and Collins (2020): only a hierarchical model reproduced human task-set effects. This is choice abstraction, not temporal abstraction over subgoals. [b16]
- Xia and Collins (2021): people learn reusable options and show negative transfer when the old option no longer fits. [b17]
- Li and Collins (2025, N=1,026): replicates later-block negative transfer, but a meta-learning model fits better than a fully hierarchical model. [b18]

### 2.6 Language-model era (2021 to 2026)

- kSubS (2021): a trained transformer proposes subgoals k steps ahead inside search. [b19, c15, c23, c24]
- Least-to-most prompting (2022/2023): list easy sub-problems, then solve in order. [c16, c25]
- Voyager (2023): a verified code skill library in Minecraft. [c12, c22]
- ADaPT (2023/2024): decompose only when the executor fails. [b20, c10, c11, c21, d05]
- ELLM, CALM, DLLM (2023/2024): an LLM proposes or judges subgoals as reward shaping for RL. [c13, a28, a29]
- LAST (2024): LLM segmentation plus a minimum-description-length (MDL) term to merge skills. [c14]
- 2025 to 2026: Select-Then-Decompose (cost of decomposition), ARISE (subgoal mining from text traces), skill-library lifecycle and staleness studies. [d01-d11]

## 3. Core findings with exact numbers

Status uses the claim file (K ids). Items marked "re-opened" were re-read in full text by the cross-check in critique.md.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Eigenoptions do not find bottlenecks first. In 4-room the 5th eigenoption is the first to end at a doorway. | 5th of the ordered set; one small domain, qualitative figure | Machado 2017 [a02, c02, b01]; re-opened | [E] K01 |
| Bottleneck-only options (go to nearest doorway) raise diffusion time in 4-room. | Direction only, in figures; options work at several timescales | Machado 2017 [a04] | [S] K02 |
| Bottleneck options are competitive when the goal is near a doorway; eigenoptions win when the goal is far. | 64 eigenoptions vs doorway options, 250 episodes, 100 trials | Machado 2017 appendix D [a06] | [S] K02 |
| Random subgoals fail. | 24 random orderings; most raise diffusion time by orders of magnitude until nearly every state has an option; some runs never reach the goal | Machado 2017 appendix C [a07, b02] | [S] K03 |
| Few eigenoptions are enough in later tests. | 4 eigenoptions sped learning and never hurt in 10 sampled 4-room tasks (1,000-step cap, 50 episodes per run, 50 runs). Original paper: best at 64 options (32 plus negations), "fairly robust" to number; Q-learning alpha 0.1, gamma 0.9, 100 trials | Machado 2023 [a12, b04, c05]; Machado 2017 [a05]; re-opened | [E] K04 |
| First few options can hurt exploration in the original paper (diffusion time rises, then falls below the primitive walk once enough are present). A too-small set can create near-unreachable states. | Figures only | Machado 2017, 2023 [a03, b01, c05] | [S] |
| Using the top ten eigenvectors beats using the top one ten times. Median diffusion time is a safer metric than mean (outliers). | 4-room, closed-form options | Machado 2023 [c06] | [S] |
| Covering options beat eigenoptions in their own study. | Cover time 4-room 672.0 vs 1094.8; 9x9 grid 258.6 vs 460.5 (8 options each); algebraic connectivity 0.065 vs 0.023 and 0.24 vs 0.12; reward better or equal in all 6 domains; 5 runs | Jinnai 2019 [a16, a17] (table cells read from layout text) | [C] K05 |
| Covering options gave no gain in the later 10-task test and were brittle with an online SR. | 10 tasks, none helped; option keyboard cut needed eigenoptions by 30% (open room, 10 needed) and 42% (4-room, 12 needed) | Machado 2023 [a12, b04, b22, c20] | [C] K05 |
| Deep SR eigenoptions on pixels worked in 3 of 4 Atari games, failed in Freeway. | Bank Heist, Montezuma, Ms. Pac-Man worked; 500,000 samples per game; 50,000 random-policy steps; qualitative plots, no scores | Machado 2018 [a10, b03, c04] | [E] K06 |
| DCEO online from pixels: Montezuma score 2500 in a few million steps; RND at 2B steps passed DCEO at 200M. | DCEO at least as good as Counts and RND; DIAYN no better than DDQN in Nine rooms; 30 seeds | Klissarov and Machado 2023 [a14, a15, c07] | [E] K06 |
| Choosing the best option set is NP-hard; (log n)-inapproximable in deterministic MDPs. | A-MOMI gives an O(log n) approximation | Jinnai 2019b [b08] | [S] K07 |
| Most of hierarchy's benefit is exploration. | AntMaze family, 5 seeds, 10M steps; shadow flat agent with multi-step rewards matched HRL on all tasks except AntMaze (slight drop) | Nachum 2019 [b10]; Jong 2008 second-hand [b11] | [E] K08 |
| People choose bottlenecks as subgoals. | Exp 1 N=40: 4.4x as often as other locations; Exp 2 N=10 and Exp 3 N=21: bottleneck first and recognised faster (98% accuracy); Exp 4 N=35 Tower of Hanoi: 17 vs 7 vs 11 | Solway 2014 [a19, a20, b12]; re-opened | [E] K09 |
| A Bayesian partition model reproduces this and predicts new biases. | Exp 1 N=87: 58/87, p=0.003. Exp 2 N=241 (78 bad, 87 control, 76 good): 53/78 bad-structure; bad vs control chi2(1,165)=6.52, p=0.01; control vs good p=0.5. Exp 3 N=127: boundary transitions slower, F=121. Exp 4 N=77: 51/77, p=0.0014. The "65% on bottleneck nodes" figure is a model simulation of Solway's N=40 data, not new human data | Tomov 2020 [b13]; re-opened | [E] K09 |
| Segmentation follows community structure with equal local statistics. | Exp 1 N=30 t(29)=2.27, P<0.05 (Hamiltonian blocks t(29)=2.25); Exp 2 N=10 replicated; fMRI N=20 within-community pattern similarity, medial prefrontal cluster tracks boundaries (P<0.05 corrected) | Schapiro 2013 [a24, a25] | [S] K10 |
| Pseudo-reward prediction error for subgoal progress. | EEG N=9 negativity at Cz p<0.01; fMRI N=30 dorsal ACC p<0.01 cluster-corrected; Exp 2 N=14 accumbens p<0.05; behaviour N=22: goal distance predicted package choice (-7.6, p<0.001), subgoal distance did not (p=0.43); Bayes factor 4.31 for HRL | Ribas-Fernandes 2011 [a23, b14] | [E] K11 (small N, one task, one lab) |
| Learned options transfer and interfere. | Xia and Collins: lab n=25, MTurk n=55; Block 8 option-transfer errors t(24)=2.5 p=0.02; MTurk t(54)=4.7 p<0.0001; first-stage negative transfer did not replicate on MTurk (F=0.19, p=0.83). Li and Collins N=1,026 (181 random, 254 mid, 591 best): Block 7 replicated; meta-learning beat hierarchical model by AIC t=24; holds for about 75% of participants | Xia and Collins 2021 [b17]; Li and Collins 2025 [b18] | [C] K12 |
| Humans are partly SR-like. | Exp 1 n=58: reward revaluation .52 vs transition .45, t(57)=2.89, p<0.01. Exp 2 MTurk n=88: .66 vs .47, Z=-2.85, p=.0034. Hybrid SR plus model-based fit best; pure SR failed | Momennejad 2017 [a26, b15] | [S] K13 |
| GPT-4 fails to plan on cluster graphs. | Shortest path one cluster away: 0 of 30 at temperature 0, at most 10% at 0.5 or 1. LLM chi2 2357.87, graph chi2 3431.53 (p<.001); temperature chi2 1.28, p=.53. BFS/DFS prompts helped inconsistently | CogEval 2023 [c08, c09, d14]; re-opened | [S] K14 |
| Bare GPT-4 on Blocksworld plan generation. | 206/600 (34.3%); cost-optimal 198/600; verification 191/600; InstructGPT-3 41/600 (6.8%) | PlanBench [c17] | [S] K15 |
| Subgoal search beats action search (trained generator). | Rubik's cube nearly 100% vs under 10%. Sokoban graph size 50: 12x12 0.66 vs 0.15, 16x16 0.42 vs 0.04, 20x20 0.46 vs 0.02. Expert data 78/67/60%. About 65% of Sokoban subgoals reduce distance, 17% raise it, 5% reach dead states. Best k=3 (INT), k=4 (cube) | Czechowski kSubS [b19, c15, c23, c24]; re-opened | [E] K16 |
| Decompose only on failure (ADaPT, GPT-3.5). | ALFWorld 71.6 vs ReAct 43.3, Plan-and-Execute 43.3, Try-again 47.8, Reflexion 57.5. WebShop 44.0 vs ReAct 32.0, Reflexion 35.0, LATS 38.0. TextCraft (dmax 4) 52.0 vs 19.0, 27.0, 32.0. The headline "28.3 points" is over ReAct and Plan-and-Execute; over Reflexion the gain is 14.1. Pick2: 52.9 vs 5.9 to 11.8. Look task: tie at 61.1. Calls, not tokens, matched | Prasad 2024 [b20, c10, c21, d05]; re-opened | [S] K17 |
| ADaPT gain grows with depth. | TextCraft depth-2 recipes 26.9 (ReAct) to 78.2; depth-3 recipes 1.8 to 38.7; mean max depth used 1.9 and 2.8; weak ALFWorld executor 3.3 to 41.7; biggest step dmax 1 to 2; GPT-4 up to 37 points on TextCraft, LLaMA-2-70B up to 15 | Prasad 2024 [c11, d05] | [S] K17 |
| Plan-first prompting helps beyond example length, little on GSM8K. | SCAN length 99.7 vs 16.2 (16.7 other CoT); last letter length 12: 74.0 vs 31.8 (CoT with more exemplars 37.4 at 4, 38.4 at 8); GSM8K 62.39 vs 60.97; 5+ steps 45.23 vs 39.07 | Zhou 2023 [c16, c25]; re-opened | [S] K18 |
| LLM subgoals help downstream in some settings; judging subgoal reach is weak. | miniF2F 38.9 to 44.3 (45.5 with diffusion-chosen examples). DLLM +27.7% HomeGrid, +21.1% Crafter, +9.9% Minecraft; HomeGrid goal correctness 52.55 / 61.64 / 66.92 with more context; context-insensitive goals 24.30 / 18.34 / 18.95. CALM with subgoal list given F1 0.60 to 0.74 (precision 0.95-0.97, recall about 0.49-0.50); when the LLM invents subgoals Llama-3-70B F1 0.82, recall 0.96, 66 FP vs 19 TN; another table shows 0.16 (not re-derived). ELLM goal conditioning gave no significant pretraining gain | [b21, a29, a28, d16, c13, c27] | [C] K19 |
| Whole-trajectory LLM judges are unreliable. | 1,302 trajectories, 5 benchmarks, 12 judges; best precision under 70%; rule-based recall 55.9% | AgentRewardBench [d15] | [S] (supports K19, K27) |
| A verified skill library compounds. | Voyager: 3.3x unique items, 2.3x distance, tech tree up to 15.3x faster; removing self-verification cut items 73%; GPT-4 gave 5.7x GPT-3.5 items; 3 runs per cell | Voyager [c12, c22, d10] | [S] K20 |
| Compression selects skills. | BabyAI zero-shot: LAST 43, LISA 36, LOVE 37, BC 34; BossLevel 36 vs 25; removing MDL lowers performance | LAST [c14] | [S] K21 |
| Subgoal mining from text traces works (versus other learned memories). | Five-task mean DeepSeek-V3 67.4 vs ReAct 38.8 (best baseline ACE 56.6); Gemini 2.5 Flash 77.7 vs ReAct 68.2, CoT 69.3, AWM 71.6; AIME 2023-24 (43 problems) 79.1 vs ReAct 44.2 (Flash-Lite), 81.4 vs CoT 79.1 (Flash). Single run per cell | ARISE [d01] | [S] K22 |
| Subgoals work best as separate calls. | Gemini Flash: skill-document delivery 66.1, code-tool 69.8, subroutine 77.7, ReAct 68.2. DeepSeek: 51.8, 48.3, 67.4. Generic instruction instead of induced specs 78.4 to 67.7 (generic names too: 64.2). Cost per task ACE $13.14 vs ARISE $3.63 (Gemini) | ARISE [d02] | [S] K23 |
| Library size: 3 to 5. | DeepSeek-V3 K=3/5/10: murder 80.0/75.0/77.0; object 71.7/68.9/51.9; team 61.0/68.0/62.0; NatPlan 49.0/51.0/45.0. 1,000 distractor skills: recall 73.6% to 27.4%; zero-load 9.3% to 51.6%; Pass@3 51.6% to 38.6%; explicit selection 73.9% recall | ARISE [d03]; Liu 2026 [d07] | [E] K24 |
| Stale memories hurt; vote counters are slow. | Qwen3-8B, 30 streams of 200k queries: no retirement 1,290 stale per 10^4; ExpeL-style 967; ACE-style 946; SPRT+LR-CUSUM 54; recommended rule 0 (perfect notices) or 16 (own detector); accuracy 0.648 with 21% fewer calls. Across 5 LLMs counters serve 7.0 to 13.5x more stale answers; 35 to 73x on 521 EvalPlus tasks. With mild staleness counters were 3.5 points better than the strict rule | Zhou 2026 [d08]; Zhu 2026 [d09] | [C] K25 (authors' own preprint; facts memory, not subgoals) |
| Decomposition costs more than it earns on easy items. | GPT-4o-mini GSM8K: CoT 93.17% at 396 tokens; Plan-and-Solve 92.72% at 468; ReAct 91.66% at 2,700; Plan-and-Execute 92.34% at 2,443; P&E(DAG) 90.67% at 1,943; Select-Then-Decompose 93.56% at 517. Executor size matters more than decomposer size | Select-Then-Decompose [d06] | [S] K26 |
| Mined libraries can be readable and useless. | 5 of 8 clusters purity at least 0.95; skill-step accuracy 18.5 to 20.5%; WebArena 55.8% to 44.2%; frequency baseline better at every training size (edit distance 0.485 vs 0.528 at N=2000) | Hao and Li 2026 [d11] | [C] K27 |
| A two-level skill hierarchy beats a flat list in RL. | ALFWorld 89.9%, WebShop 72.7%; no hierarchy -13.1 and -11.3; raw trajectories up to -25; no dynamic evolution -5.5 | SkillRL [d10] | [S] |

## 4. Mechanisms and models

Each mechanism is written so a program could implement it. Items marked "needs a graph" cannot run on our text tasks unless code first builds a graph from attempt traces.

### 4.1 Options (the stored object)
Store each subgoal as: name, start condition (when it applies), body (a routine, a prompt template, or a program), stop condition (a check that code can run), version tag. The stop condition must be checkable. Machado's own Atari validation was "by eye", and the authors link failures to myopic option policies. [c18, c28]

### 4.2 Eigenoptions (needs a graph)
1. Build the state graph (or sample transitions). Form the Laplacian L (or the SR matrix; the SR approximates the inverse of L). [a27]
2. Compute eigenvectors e_i, ordered by eigenvalue.
3. Intrinsic reward for transition s to s' under eigenpurpose i: r_i = e_i(s') - e_i(s).
4. Train an option on r_i with a terminal state where no action gives positive reward.
5. Add the negation (-e_i) as a second option. The tabular full-coverage case equals the combinatorial Laplacian; the sample version uses an incidence matrix T of feature differences plus SVD. [a08]
6. Evaluate with diffusion time: expected steps for a random walk (primitives plus options) between two random states. Report the median. [a03, c06]

Practical limits: needs the graph or a decent SR; an accurate SR is not needed (SR after 100 episodes was enough in rooms). [a09] The deep-learning versions had a rotation problem until ALLO. [b05]

### 4.3 Covering options (needs a graph)
Compute the Fiedler vector of the graph. Add an edge (an option) between its extreme states. Repeat on the augmented graph. Each option lowers expected cover time. Returns are concave in the number of edges added. [a16, a17] Fragile when the SR is online and when the option has a single-state initiation set. [b04, c20]

### 4.4 Bottleneck subgoals
Classical rules: diverse density on successful trajectories, betweenness centrality, Q-cut. [a31] The link between SR eigenvectors and bottlenecks is a different recipe: the sign of an eigenvector gives a normalised-cut partition, and states on the cut are bottlenecks. [a13, a27] Successor options cluster SR vectors and find landmarks inside regions instead. [a18]

### 4.5 Bayesian hierarchy selection (human model)
Solway's criterion: pick the decomposition that minimises expected trial-and-error search cost in the decomposed space. This equals Bayesian model selection over hierarchies. [a19] Tomov's model infers a two-level partition by MCMC (parameters hand-picked, not fit). [b13] Implementation sketch for a graph G: score each candidate partition by the expected number of steps to find a path with region-then-step search, plus a description-length term; keep the best. (The sketch is ours; the papers give the criterion, not this code.)

### 4.6 Pseudo-reward and progress
Each active subgoal has its own progress signal (change in distance to the subgoal) that is separate from the change in distance to the final goal. The model: prediction errors inside the option and again for the whole option. [a21, a23] Implementation: keep two counters per subgoal, one for "closer to this subgoal", one for "closer to the answer". Do not let the first stand in for the second: in the behaviour data, subgoal distance did not predict package choice (p=0.43) while goal distance did. [b14]

### 4.7 Subgoal search (kSubS)
A generator proposes subgoals k steps ahead; a search (best-first) runs over subgoals; a low-level policy checks each is reachable; unreachable ones are dropped (about 50% of INT and Rubik's subgoals were reachable by the low-level policy and the rest were discarded). [c15] Choose k by sweep. [c23]

### 4.8 As-needed decomposition (ADaPT)
1. The executor tries the task.
2. If the executor reports failure, a planner splits the task into sub-tasks with a joining logic (and/or).
3. Each sub-task goes to the executor; recurse on failure up to dmax.
Depth 2 captures most of the gain. [c10, c11] The failure signal is the executor's own judgment, which the paper itself flags as a limit. [d05]

### 4.9 Trace mining (ARISE)
1. Collect correct ReAct traces.
2. An LLM gives each step a short move name.
3. Merge names into 5 to 10 categories, minimum support 3.
4. Rank by frequency, keep the top K (3 to 5).
5. Write a spec for each, and run each as an isolated sub-call with its own context. [d01, d02, d03]
Note it ranks by frequency, not by bottleneck or graph structure.

### 4.10 Compression admission (LAST)
An LLM segments trajectories; a variational step merges pieces into skills; an MDL term penalises long descriptions and rewards reuse. A copyable admission rule: a candidate subgoal must shorten the total description of past solutions. [c14]

### 4.11 Library lifecycle
- Admit only after a code check (Voyager: -73% items without self-verification). [c12, c22]
- Test each skill against a skill-free control episode; harmful skills are removed and blocked from re-admission (TrackRL, RL-trained policies). [d09]
- Retire on a failed re-check or an edit notice, not on a vote tally. [d08]
- Keep the active set near 5 and pre-select explicitly; do not let the agent scan a large library. [d03, d07]

## 5. What holds up

### 5.1 Replicated or multi-source
- Eigenoptions are not bottleneck finders (Machado 2017, the 2023 review, and Momennejad 2020's framing via the sign partition). [K01]
- A small eigenoption set (4) helps in sampled tasks; larger sets are also fine in the original paper. [K04]
- Hierarchy's benefit is mostly exploration in RL (Nachum 2019, plus Jong 2008 second-hand). [K08]
- People choose bottlenecks (Solway 2014, and Tomov 2020 as a model-based extension with new samples). [K09]
- Library size 3 to 5 for language subgoals, with distractor-skill harm at 1,000 added skills. [K24]
- Subgoal search beats action search with trained generators. [K16]

### 5.2 Failures and contradictions
- Covering vs eigen: Jinnai 2019 says covering is better or equal in six domains; Machado 2023 finds covering options give nothing in ten 4-room tasks. Different protocols, option counts (8 vs varied), and whether the graph or the SR was known. The later authors blame the single-state initiation set; untested. [a16, a17, a12, b22, c20; K05]
- "SR eigenvectors help find subgoals" (the framing in the subfield brief) versus Machado 2017: individual eigenoptions deliberately do not seek bottlenecks. The bottleneck link comes through the eigenvector sign partition. Both are true. [critique]
- Nachum 2019 (benefit is exploration) versus Solway and Tomov (hierarchy lowers planning cost). Different regimes: RL exploration versus search cost. Only the second is about an agent that already has a model. [critique]
- Xia and Collins first-stage negative transfer did not replicate on MTurk; Li and Collins replicates later-block transfer only, and finds a meta-learning model fits better than a fully hierarchical one. [b17, b18]
- Eigenoptions in pixels: Freeway failed; the Montezuma key subgoal was missed (blamed on greedy myopic option policy, not tested). DCEO at 200M steps was passed by RND at 2B. [a10, a15, c28]
- ELLM: LLM goals usually match or beat novelty rewards, but goal conditioning gave no significant pretraining gain; high seed variance. [c13, c27]
- Mined GUI skills lost to a frequency baseline. [d11]
- Early deep Laplacian methods were ill-posed (rotation problem) and tuned on the answer, one reason results were hard to reproduce. [b05]

### 5.3 Moderators and boundary conditions
- Goal location relative to chokepoints decides whether bottleneck or eigen options win. [a06]
- Option count: too few can hurt exploration in the original tests; in the later 10-task test four never hurt. Setups differ (diffusion time versus reward; initiation sets). [a03, a12]
- Task length: plan-first prompting helps most beyond example length (SCAN 99.7 vs 16.2), little on GSM8K (62.39 vs 60.97). [c16]
- Task depth: ADaPT gains grow with recipe depth (26.9 to 78.2 at depth 2; 1.8 to 38.7 at depth 3). [c11]
- Executor strength: weak executors gain most; executor size matters more than decomposer size. [c11, d06]
- Problem easiness: decomposition costs 4 to 10x tokens with no gain on easy items. [d06]
- Observation context: DLLM goal correctness rises from 52.55 to 66.92% with more information. [a29]
- Notice quality: stale-memory retirement works best with explicit edit notices; with mild natural staleness counters were 3.5 points more accurate than the strict rule. [d08]

### 5.4 Interventions that worked
- Pre-selecting a small subgoal set explicitly (recall stays 73.9% with 1,000 distractors). [d07]
- An isolated sub-call per subgoal (77.7 vs 66.1 as skill text). [d02]
- Verification before admission (Voyager -73% without). [c22]
- A two-level library of general plus task-specific skills (+11 to 13 points over flat, RL-trained). [d10]
- A router that picks decomposition per task (93.56% at 517 tokens vs 92.34% at 2,443). [d06]
- An edit notice plus likelihood-ratio detector against stale memory (0 stale with perfect notices). [d08]

### 5.5 Interventions that did not work
- Random subgoals. [a07]
- Bottleneck-only subgoals for exploration. [a04]
- Covering options with sparse initiation sets. [c20]
- BFS/DFS instructions for GPT-4 on community graphs (inconsistent). [c09]
- Skill text pasted into the prompt instead of run as a sub-call (can fall below plain ReAct: 66.1 vs 68.2). [d02]
- Ten active subgoals instead of 3 to 5. [d03]
- Cluster-mined skills compared with a frequency prior. [d11]

## 6. Language models

No LLM study in the evidence tests SR/eigen-style or bottleneck subgoal discovery directly. LLM work covers hand-built or prompted decomposition, trained subgoal generators, or mining from traces. [critique]

### 6.1 Graph and cluster structure
- CogEval (2023 models): LLMs list edges well but fail to use them. Three failure types: invented edges, long routes, loops. GPT-4 shortest path one cluster away: 0 of 30 at temperature 0, at most 10% elsewhere. BFS or DFS instructions helped cluster counting at temperatures 0 and 0.5 and within-cluster paths at all temperatures, but one-cluster-away paths improved only with BFS at 0.5. [c08, c09, d14]
- No reasoning-model or external-graph-tool retest was found. The human bottleneck effect (Solway 4.4x) has not been tested on LLMs. [d14]
- The CogEval authors point to schemas and multi-scale planning with memory and executive control as the next step. [c26]

### 6.2 Plain planning
- GPT-4 on Blocksworld plan generation: 34.3%. [c17] Blocksworld has little hierarchy, so this is a baseline, not a test of decomposition.

### 6.3 Decomposition prompts
- Least-to-most on code-davinci-002: very large gains beyond example length; small on GSM8K. Almost every GSM8K failure is solved with a manual decomposition, so the model-written decomposition is the weak part. [c16] The gain is not only extra prompt length (CoT with 8 exemplars: 38.4 vs 74.0). [c25]
- Select-Then-Decompose (GPT-4o-mini, Qwen2.5 1.5B/7B/14B): easy items get no benefit from explicit decomposition at 4 to 10x tokens; a per-task router wins. Distilled R1 models produce more invalid plans at 14B. [d06]

### 6.4 As-needed decomposition
- ADaPT on GPT-3.5: ALFWorld 71.6 vs 43.3 (ReAct) and 57.5 (Reflexion, best baseline). It also lifted GPT-4 (up to 37 points on TextCraft), LLaMA-2-70B (up to 15) and Lemur. [c21, d05] Calls were matched, not tokens. No always-decompose arm. 2023 models only. [d05]

### 6.5 LLM as proposer or judge of subgoals
- DLLM: gains of 27.7, 21.1 and 9.9% over the strongest baseline, but one third to one half of proposed goals are wrong without extra context. [a29]
- CALM: precision is high when the subgoal list is given, recall about 0.5; when the model invents subgoals it says yes too often (recall 0.96, 66 false positives vs 19 true negatives). One table shows F1 0.16. [a28, d16]
- AgentRewardBench: no judge exceeded 70% precision on whole-trajectory success, so about 30% of accepted trajectories were failures. [d15]
- Voyager: self-verification was the most important component (-73% items without it). [c22]
- kSubS (small trained transformer): 17% of generated Sokoban subgoals increase distance and 5% reach dead states. [b19, c15]

### 6.6 Mining subgoals from text traces
- ARISE: +28.6 points over ReAct on DeepSeek-V3 (67.4 vs 38.8), +9.5 on Gemini 2.5 Flash (77.7 vs 68.2). The gain depends on delivery: subroutine > code tool > skill text. A library of 3 to 5 is enough. Generic collection tools matched expert-designed ones (86.0 vs 87.0; 75.5 vs 70.8). Learning from correct traces only helps when the spec is hidden from the main prompt; differences between variants A to D are small and mixed (60 to 75). [d01-d04]
- Counter: cluster-mined GUI skills lost to a frequency baseline; weak 8B policy, boundary detector cut at large action changes, not bottlenecks. [d11]
- Earlier: SDG clustered LLM-proposed subgoal descriptions with k-means and trained one RL skill per cluster; the authors note clustering adds noise. [d12]
- LDSC: LLM-supplied semantic subgoal sequences, reported +55.9% over baselines on hand-built key-door maps; no eigen or covering arm. [d13]

### 6.7 Library growth and staleness
- 1,000 distractor skills: recall 73.6% to 27.4%, Pass@3 51.6% to 38.6%. [d07]
- Stale memory: see section 3. Data are for facts and templates, not subgoals. [d08]
- TrackRL and SkillRL results are for RL-trained policies, not prompt-only agents. [d09, d10]

### 6.8 What changed behaviour, by how much
| Change | Effect | Source |
|---|---|---|
| Subroutine delivery instead of skill text | +11.6 points (Gemini Flash), +15.6 (DeepSeek) | d02 |
| Library of 10 instead of 3 | up to -19.8 points (object task, DeepSeek) | d03 |
| 1,000 distractors, no pre-selection | recall -46.2 points | d07 |
| Self-verification removed | -73% items | c22 |
| Decompose on failure vs fixed plan | +28.3 points on ALFWorld (vs Plan-and-Execute) | d05 |
| Always-decompose on easy GSM8K | about -0.8 points at 6x tokens (Plan-and-Execute) | d06 |
| Router per task | +0.4 points at 1.3x CoT tokens | d06 |

## 7. What our agent should take

Schema parts: G guardrail, S state, O operator, memory. Statuses are from claims.jsonl. Under SCHEMA.md section 8 nothing enters without its equal-token test; "Add now" means the evidence is established enough to adopt the rule as a design constraint, with logging, and G7 still applies.

### Add now (established)

1. **Cap the active subgoal set at about 5 and pre-select with an explicit step, not agent scanning.** Part: memory (subgoal library), S6/O3. [E] K24. Evidence: d03, d07, a12, a17, c23.
2. **Do not cite eigenoptions as bottleneck finders; do not seed a library from bottlenecks alone.** Mix subgoals of different kinds and scales; keep primitive steps always available. Part: memory. [E] K01, K04 for the first half; the "mix kinds" half is [S] K02. Evidence: a02, a04, a06, c02, c05, c06, a12.
3. **Treat a subgoal as a hypothesis that can mislead.** Hierarchy causes planning errors (people take paths with fewer boundaries even when worse). Log each decomposition and keep the flat route available at S5/S6. Part: O3, S6. [E] K09. Evidence: b13, b12.
4. **Always run the plain multi-attempt baseline with the same samples.** Most of RL hierarchy's benefit is exploration, so any library gain must be shown against an equal-token flat control. Part: G7. [E] K08. Evidence: b10, b11.
5. **Log subgoal progress separately from answer progress.** Part: S6 log, S8. [E] K11 (small N; the behavioural link is thin: subgoal distance did not predict choice). Evidence: a23, b14. Logging only; any control use is under Test first.
6. **Keep the library source swappable; do not hard-code one discovery rule.** Part: memory. [C] K05 (listed here as a design constraint, not as a claim that any rule wins). Evidence: a16, a17, a12, b22, c20.

### Test first (single-source, contested, or untested for LLMs)

| # | Item | Part | Status | Evidence |
|---|---|---|---|---|
| T1 | Decompose only on a failure signal (ADaPT style), depth cap 2 | O3 at S6, G1 | [S] K17 | b20, c10, c11, d05, d06 |
| T2 | Gate decomposition by a difficulty check (router) | S0 gate, G12 | [S] K26 | d06 |
| T3 | Run each subgoal as an isolated sub-call, spec kept out of the main prompt | O3, S3 | [S] K23 | d02, d04 |
| T4 | Mine move categories from the agent's own solved traces and rank by frequency | memory, S9 | [S] K22 | d01, d03 |
| T5 | Compare the mined library with a hand-written list and a frequency prior | memory | [C] K27 | d11, d01 |
| T6 | Admit a subgoal only after a re-runnable code check; ablate the gate | memory, G2/G3 | [S] K20 | c12, c22, d09 |
| T7 | Version tag plus re-run check to retire stale subgoals (not vote counts) | memory | [C] K25 | d08, b17, b18 |
| T8 | Subgoal granularity sweep (steps per subgoal) | O3 | [E] for trained generators K16; untested in language | c23, b19 |
| T9 | Code builds an explicit graph of problem states, finds clusters and cuts, hands them to the model | S2, S6 | [S] K14 | c08, c09, d14, a13 |
| T10 | Bottleneck vs spanning vs random subgoals on graph-like items, goal near and far from the chokepoint | memory | [S] K02, K03 | a04, a06, a07 |
| T11 | MDL admission: keep a subgoal only if it shortens the description of many past solutions | memory | [S] K21 | c14 |
| T12 | Community-aware segmentation of long traces before summarising | S2, S9 | [S] K10 | a24, a25 |
| T13 | Subgoal-level verifier arm (is the subgoal reached or still valid?) | S5/S6 | [C] K19 | a28, d15, d16, c22 |
| T14 | A separate subgoal-progress check used for control | S6 | [E] for existence of the signal; benefit untested | a23, b14 |
| T15 | Two-level library (general plus task-specific) vs flat | memory | [S] | d10 |
| T16 | A random-subgoal control arm in every library test | memory, G7 | [S] K03 | a07, b02 |

## 8. Concrete tests on our bench

Rules for all tests. Both arms get the same total token budget (setup and library-building cost counted, per G7). Report mean tokens per item. Use bench items with a code check where the bench has one; the item types below say what to pick. Expected effects are drawn from the cited numbers and may not transfer.

| Test | Item type | Arms (equal tokens) | Metric | Expected effect |
|---|---|---|---|---|
| E1 Decompose-on-failure | Multi-step items where plain pass rate is 30 to 70%, with a check | (a) plain best-of-N; (b) always-decompose then solve; (c) decompose only when the attempt fails the check, depth cap 2 | Pass rate at fixed tokens; tokens per solved item | (c) beats (b) on easy items by cutting tokens; (c) matches or beats (a) on hard items only. If (a) wins everywhere, reject, as G11/G12 predict |
| E2 Difficulty router | Mixed easy and hard items | (a) always-decompose; (b) never; (c) gate at S0 using the class record | Pass rate at fixed tokens | (c) >= (b) with fewer tokens than (a) (d06: 93.56% at 517 tokens vs 92.34% at 2,443) |
| E3 Isolated sub-call vs advice text | Items with 3 to 5 natural sub-steps | (a) same subgoal text inside the main prompt; (b) each subgoal as an isolated call with only its spec and inputs | Pass rate, tokens | (b) higher by several points (d02: +11.6 on one model) |
| E4 Trace-mined library vs hand-written vs frequency prior | A problem class with at least 30 solved items | (a) no library; (b) hand-written list of 5; (c) top-5 mined categories from solved traces; (d) frequency prior (most common first step) | Pass rate on held-out items; total tokens incl. mining | (c) > (a); (c) vs (b) unknown; (c) must beat (d) or be dropped (d11) |
| E5 Library size | Same as E4 | K = 3, 5, 10, 30 with explicit pre-selection and with agent-side scanning | Pass rate; loaded-skill recall | 3 to 5 best; scanning degrades with size (d07) |
| E6 Verification gate | Items with a code check | (a) admit any solved subgoal; (b) admit only if a re-run on a held-out input passes | Held-out pass rate after 50 library updates | (b) higher; Voyager saw -73% without the gate |
| E7 Staleness | Take the library, then change the task rule so some subgoals become wrong | (a) vote counter; (b) version tag plus re-run check; (c) no retirement | Stale-subgoal use rate; pass rate after change | (b) cuts stale use by a large factor (d08 reports 7x to 73x for counters vs a certified rule); measure the damage first |
| E8 Granularity | Long items of 6 to 12 steps | Subgoals every 2, 4, 6 steps (or 2, 3, 4 sub-problems) | Pass rate | A sweet spot at 3 to 4 (c23); plan for a non-monotone result |
| E9 Code-built graph | Items with an explicit state space (puzzles, routes, dependency graphs) | (a) model recalls structure from text; (b) code builds adjacency, clusters and cut nodes and gives the model the cut list | Correct shortest or valid path across clusters | (b) large gain; CogEval GPT-4 got 0/30 on cross-cluster paths |
| E10 Bottleneck vs spanning vs random | Graph-like items with goal near and far from a chokepoint | Subgoals = cut nodes; = spanning set (eigenvector extremes); = random nodes; = none | Success and tokens | Spanning > cut when the goal is far; cut competitive when near; random <= none (a06, a07) |
| E11 MDL admission | Same as E4 | Select by frequency; by MDL gain | Pass rate | MDL >= frequency by a few points (LAST 43 vs BC 34; MDL ablation lowers performance) |
| E12 Subgoal verifier | Items with subgoal-level code checks | (a) model self-judges "subgoal reached"; (b) code or run check; (c) two-sample majority self-judge | Agreement with ground truth (false-accept rate) | Self-judge false accepts near 30% (d15); (b) near 0 |
| E13 Community segmentation | Long traces (more than 20 steps) | (a) fixed-size chunks; (b) chunks cut at community boundaries of the step graph | Summary-then-solve pass rate | Small gain at best (Schapiro effects are just under P<.05) |
| E14 Library-as-explorer control | Same as E4 | (a) library plan; (b) flat agent given the same diverse samples with no structure | Pass rate | If (b) matches (a), the gain is diversity, not structure (b10) |

## 9. What does not transfer, and why

- **Eigenvectors and the Laplacian.** They need a state graph or a learned SR. A reasoning problem has no given state graph, and building one from model attempts is noisy. All eigenoption results are on tabular grids or Atari with qualitative plots. [a01, a10, critique] Only the idea (rank structure in a graph the program builds) is portable.
- **Training options and policies.** We do not train. DCEO, deep SR, TrackRL, SkillRL and ALLO are RL-trained. [c07, d09, d10]
- **Diffusion time and cover time.** These are exploration metrics for random walks. They are not accuracy on a reasoning item. [a03, a16]
- **Trained subgoal generators.** kSubS generators learn from solved domain data; no zero-shot prompt-only analogue was measured. [b19, critique]
- **Human neuroscience of PPE.** EEG N=9 and fMRI in a delivery game. It supports a design cue, not a performance gain. [a23, b14]
- **Human bottleneck preference.** Shown on small known graphs with undergraduates; CogEval shows LLMs do not reliably use cluster structure from a text graph. [a19, c08]
- **ADaPT numbers.** GPT-3.5, text games and shopping, calls matched not tokens; frontier models and our item types untested. [d05]
- **Stale-memory numbers.** Facts and templates in a knowledge-base stream, from the authors' own preprint. [d08]
- **Voyager.** Needs a game engine as a verifier; three runs per cell. [c12]
- **The exploration explanation.** Nachum's finding is for fixed-length options in locomotion; it may or may not apply to prompt-based subgoals. [b10]
- **Policy-dependent SR.** Momennejad's warning means subgoals found from the agent's own traces inherit the agent's habits. Our agent's samples are correlated (G4). [a27]

## 10. Open questions

1. Does automatic subgoal discovery from text traces beat hand-written or prompted decomposition at matched tokens? ARISE beats only other learned memories. (K22, gap 1)
2. Does as-needed decomposition still beat always-decompose and best-of-N at equal tokens on frontier models? (K17, gap 2)
3. What is the right granularity of a language subgoal? The size cap (3 to 5) is measured; the step size is not. (gap 3)
4. How reliable is an LLM at judging "subgoal reached" and "subgoal still valid", and does a verifier fix it? (gap 4)
5. How large is negative transfer from stale stored subgoals in LLM agents, and which rule removes it? Version tag, precondition check and test run were not compared head to head. (gap 5)
6. Do reasoning models or graph tools change CogEval's cross-cluster result? Do Solway's bottleneck effect and Schapiro's community effect appear in LLMs? (gap 6)
7. Covering, eigen and bottleneck options on a learned or noisy graph: unresolved. (gap 7)
8. How much of library benefit is exploration diversity versus structure? SkillRL has no same-sample flat control. (gap 8)
9. At what problem size does hierarchy pay for LLM reasoning? Indirect evidence only: no gain on easy GSM8K, growing gain with ADaPT recipe depth. (gap 9)
10. PPE replication with larger N and tasks beyond the delivery game; its value as a design cue is unproven. (gap 10)
11. Does the covering-versus-eigen dispute come from the single-state initiation set, as Machado conjectures?
12. Does a policy-dependent SR (subgoals from the agent's own habits) give worse subgoals than a random-walk SR, as Momennejad predicts?
13. Search note: gaps 7, 9 and 10 got no new primary source because WebSearch quota and arXiv search ran out. This is absence of evidence under a limited search. [d18]

## 11. Sources

[V] = opened and read by a research agent this run; [M] = snippet or second-hand only. Re-opened in full text by the cross-check in critique.md: Machado 2017, Machado 2023, kSubS, ADaPT, CogEval, Least-to-Most, Solway 2014, Tomov 2020. The others were not re-opened by the cross-check.

| Source | Mark | URL | Evidence ids |
|---|---|---|---|
| Machado, Bellemare, Bowling (2017) A Laplacian Framework for Option Discovery in RL | [V] | https://arxiv.org/abs/1703.00956 | a01-a08, b01, b02, c01-c03, c18 |
| Machado, Rosenbaum, Guo, Liu, Tesauro, Campbell (2018) Eigenoption Discovery through the Deep SR | [V] | https://arxiv.org/abs/1710.11089 | a09, a10, b03, c04, c28 |
| Machado, Barreto, Precup, Bowling (2023) Temporal Abstraction in RL with the SR (JMLR) | [V] | https://arxiv.org/abs/2110.05740 | a11-a13, b04, b22, c05, c06, c19, c20 |
| Klissarov and Machado (2023) Deep Laplacian-based Options (DCEO) | [V] | https://arxiv.org/abs/2301.11181 | a14, a15, b07, c07 |
| Jinnai, Park, Machado, Konidaris (2019) Covering options | [V] | https://arxiv.org/abs/1903.00606 | a16, a17, b09 |
| Jinnai, Abel, Hershkowitz, Littman, Konidaris (2019) Finding Options that Minimize Planning Time | [V] | https://arxiv.org/abs/1810.07311 | b08 |
| Ramesh, Tomar, Ravindran (2019) Successor Options | [V] (partial text) | https://arxiv.org/abs/1905.05731 | a18 |
| Gomez, Bowling, Machado (2024) Proper Laplacian Representation Learning (ALLO) | [V] | https://arxiv.org/abs/2310.10833 | b05 |
| Wu, Tucker, Nachum (2019) The Laplacian in RL | [V] (abstract and method only) | https://arxiv.org/abs/1810.04586 | b06 |
| Machado et al. (2018) Count-based exploration with the SR | [V] (no scores recorded) | https://arxiv.org/abs/1807.11622 | b23 |
| Nachum et al. (2019) Why does hierarchy (sometimes) work so well in RL? | [V] | https://arxiv.org/abs/1909.10618 | b10 |
| Jong, Hester, Stone (2008) The utility of temporal abstraction in RL | [M] second-hand via Nachum | https://arxiv.org/abs/1909.10618 | b11 |
| Sutton, Precup, Singh (1999) Between MDPs and semi-MDPs | [M] not opened | https://doi.org/10.1016/S0004-3702(99)00052-1 | a30 |
| McGovern and Barto (2001); Simsek and Barto (2004); Menache et al. (2002) | [M] second-hand | none recorded | a31 |
| Vezhnevets et al. (2017) FeUdal Networks | [M] title only | https://arxiv.org/abs/1703.01161 | b24 |
| Bacon, Harb, Precup (2017) Option-Critic | [M] title only | https://arxiv.org/abs/1609.05140 | b25 |
| Botvinick, Niv, Barto (2009) Hierarchically organized behavior and its neural foundations | [V] | https://pmc.ncbi.nlm.nih.gov/articles/PMC2783353/ | a21, a22 |
| Ribas-Fernandes et al. (2011) A neural signature of hierarchical RL | [V] (the cross-check saw only the title on cached pages) | https://pmc.ncbi.nlm.nih.gov/articles/PMC3145918/ | a23, b14 |
| Schapiro et al. (2013) Neural representations of events arise from temporal community structure | [V] | https://pmc.ncbi.nlm.nih.gov/articles/PMC3749823/ | a24, a25 |
| Solway et al. (2014) Optimal behavioral hierarchy | [V] | https://pmc.ncbi.nlm.nih.gov/articles/PMC4133163/ ; https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1003779 | a19, a20, b12 |
| Tomov et al. (2020) Discovery of hierarchical representations for efficient planning | [V] | https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1007594 | b13 |
| Momennejad et al. (2017) The SR in human RL | [V] | https://pmc.ncbi.nlm.nih.gov/articles/PMC6941356/ | a26, b15 |
| Momennejad (2020) Learning Structures: Predictive Representations, Replay, and Generalization | [V] | https://pmc.ncbi.nlm.nih.gov/articles/PMC9004662/ | a27 |
| Eckstein and Collins (2020) Computational evidence for hierarchically structured RL in humans | [V] | https://pmc.ncbi.nlm.nih.gov/articles/PMC7703642/ | b16 |
| Xia and Collins (2021) Temporal and state abstractions for efficient learning, transfer and composition | [V] | https://pmc.ncbi.nlm.nih.gov/articles/PMC8485577/ | b17 |
| Li and Collins (2025) Algorithmic account of how humans learn, transfer and compose hierarchical policies | [V] | https://pmc.ncbi.nlm.nih.gov/articles/PMC12052257/ | b18 |
| Czechowski et al. (2021, v4 2026) Subgoal Search for Complex Reasoning Tasks (kSubS) | [V] | https://arxiv.org/abs/2108.11204 | b19, c15, c23, c24 |
| Prasad et al. (2024) ADaPT | [V] | https://arxiv.org/abs/2311.05772 | b20, c10, c11, c21, d05 |
| Zhao, Li, Kong (2023) Decomposing the Enigma | [V] (abstract-level numbers) | https://arxiv.org/abs/2305.16366 | b21 |
| Zhou et al. (2023) Least-to-Most Prompting | [V] | https://arxiv.org/abs/2205.10625 | c16, c25 |
| Momennejad et al. (2023) CogEval | [V] | https://arxiv.org/abs/2309.15129 | c08, c09, c26, d14 |
| Valmeekam et al. (2023) PlanBench | [V] | https://arxiv.org/abs/2206.10498 | c17 |
| Wang et al. (2023) Voyager | [V] | https://arxiv.org/abs/2305.16291 | c12, c22 |
| Du et al. (2023) ELLM | [V] | https://arxiv.org/abs/2302.06692 | c13, c27 |
| Fu et al. (2024) LAST | [V] | https://arxiv.org/abs/2402.16354 | c14 |
| Pignatelli et al. (2024) CALM | [V] | https://arxiv.org/abs/2409.12798 | a28, d16 |
| Liu et al. (2024) DLLM | [V] | https://arxiv.org/abs/2406.07381 | a29 |
| Lei, Yan, Momo, Cohen (2026) ARISE | [V] | https://arxiv.org/abs/2606.02994 | d01-d04 |
| Liu et al. (2025) Select-Then-Decompose | [V] | https://arxiv.org/abs/2510.17922 | d06 |
| Liu, Chen, Zhang (2026) Lost in Implicit Routing | [V] | https://arxiv.org/abs/2610.18522 | d07 |
| Zhou, Rong, Lin, Zhang (2026) Many Steps into One | [V] | https://arxiv.org/abs/2610.17544 | d08 |
| Zhu et al. (2026) TrackRL | [V] | https://arxiv.org/abs/2610.25126 | d09 |
| Xia et al. (2026) SkillRL | [V] | https://arxiv.org/abs/2602.08234 | d10 |
| Hao and Li (2026) Automating SKILL.md Generation | [V] | https://arxiv.org/abs/2606.20363 | d11 |
| Peng et al. (2023) Self-driven Grounding (SDG) | [V] (method and ablation text) | https://arxiv.org/abs/2309.01352 | d12 |
| Shek and Tokekar (2025) LDSC | [V] (abstract and introduction) | https://arxiv.org/abs/2503.19007 | d13 |
| Lu et al. (2025) AgentRewardBench | [V] | https://arxiv.org/abs/2504.08942 | d15 |
| Talk, Evaluate, Diagnose (2026); MobileJudgeBench (2026) | [M] snippet only | https://arxiv.org/abs/2608.11434 | d17 |
| Search coverage note for gaps 7, 9, 10 | [M] no source found | https://arxiv.org/search/ | d18 |
