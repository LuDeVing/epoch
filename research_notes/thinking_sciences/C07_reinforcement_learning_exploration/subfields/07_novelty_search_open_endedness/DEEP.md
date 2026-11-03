# Novelty search, open-endedness: deep document

*Subfield C07.07 (reinforcement learning, exploration). Key works: Lehman and Stanley 2011; Tao et al. 2020. Why it matters: open mode (see C04). Built from evidence_a-d.jsonl (ids a01-a29, b01-b25, c01-c31, d01-d17), claims.jsonl (K01-K27) and critique.md in this folder. Numbers marked "approx" were partly garbled in text extraction. Nearly all headline numbers come from the labs that built the systems (Stanley, Clune and colleagues). Treat them as lab-reported unless a row says otherwise.*

## 1. What it is

Novelty search is a way to search without a goal score. It rewards one thing: how different a new attempt is from attempts already made. The idea is that a goal score can lead away from the goal (deception). A search that only chases the goal then gets stuck. A search that collects many different attempts can pass through the "stepping stones" that lead to the goal.

The core pieces:

- **Behaviour description.** A short, hand-chosen summary of what an attempt did (for a maze robot, its final x,y position). Not the code or weights that made it.
- **Novelty score.** Mean distance from the new attempt's behaviour to its k nearest neighbours, among the current population and a permanent archive of past novel behaviours.
- **Archive.** A stored set of behaviours (or attempts) that were new when found. An attempt enters if its score passes a threshold.
- **Selection.** Keep and vary the most novel attempts. The goal score is not used (in the pure form).

Two related families:

- **Quality-diversity (QD)**, for example MAP-Elites. Keep the best attempt in each cell of a grid of behaviour features. Gives a map of many good, different solutions.
- **Open-endedness.** A system that keeps producing things that are both new and learnable for an observer (Hughes et al. 2024; a26, b23, c09). A noisy TV is novel but not learnable, so it is not open-ended.

For our agent this is the "open mode" operator (see C04): when the first answer may be a trap, the program should ask for attempts that differ from earlier ones, keep an archive of directions already tried, and return to promising partial work. The model does not judge novelty by itself (guardrails G1, G8 in SCHEMA.md).

Scope limit. No source in this folder measures a novelty signal raising the correctness of an LLM reasoner at equal tokens on general reasoning. LLM studies measure diversity, coverage, or open-ended growth. The closest result is PlanSearch on code (d01, d02), which is at equal attempts, not equal tokens.

## 2. History and theories in depth

**Deception and the objective (2008-2011).** Lehman and Stanley argued that in hard problems the objective function is deceptive: its gradient points away from the goal. Remedies that keep the objective (niching, diversity maintenance, multi-objectivisation) still depend on it (a08). Their 2011 paper (a01-a08, b01-b05) is the founding study. They compared NEAT with fitness = distance to goal, NEAT with novelty only, and random selection, with the same settings.

**The maze result.** Medium deceptive maze: both novelty and fitness solved it in all 40 runs. Novelty needed 18,274 evaluations (sd 20,447) against 56,334 (sd 48,705), about 3x fewer, p<0.001 (a02, b01). Random selection solved it in only 21 of 40 runs, so novelty is not random search. Hard maze: novelty solved 39/40 (mean 35,109 evaluations, sd 30,236); fitness NEAT 3/40; random 4/40 (a03, b02). Do not mix these two maps. Solutions were smaller too: 24.6 connections (sd 4.59) vs 66.74 (sd 56.7) on the medium map (a02).

**Walking.** 3D biped, 50 runs: novelty 4.04 m (sd 2.57) vs fitness 2.88 m (sd 1.04) in 15 s, p<0.01; best novelty gait 13.7 m; over 40% of fitness runs stuck in non-oscillating gaits (a07, b03).

**Boundary conditions in the founding paper.**
- Unenclosed maze (behaviour space unbounded): novelty 5/100, fitness 2/100, not significant (a04, b04). It is easy to be "new" by wandering.
- Behaviour grids coarser than 4x4 hurt about 3x (117,107 evaluations at 4x4); larger grids barely matter: 4 of 960 runs failed (a06, b05).
- Using fitness as the behaviour description cut the benefit: 11/40 vs fitness NEAT 4/40 (a06, b05).
- Archive capped at the population size (250) still solved 40/40 in 38,324 evaluations, no significant difference (a05, b05).

**Independent re-tests (2011-2015).**
- Kistemaker and Whiteson 2011 (b06, b07): performance depends on the behaviour function. 3 irrelevant behaviour points made 21/70 runs fail; 4 made 29/70 fail. Wrong aliasing found the optimum in 6/70. Removing symmetry cut cost from 63,440 to 27,427. Cells bigger than the mutation range collapse performance.
- Gomes, Mariano and Christensen 2015 (a09-a11): six mazes, 30 runs each. Best success ratio: LS-50 (50/50 blend of novelty and fitness) and NSGA (multi-objective), equal to each other (p=0.75) and better than all others (p<0.01). A random archive was best; k in 15 to 100 was best. A previously good hybrid (PMCNS) gave no clear gain: better on low-deception mazes, worse on highly deceptive ones.
- Gomes, Urbano and Christensen 2013 (b08): in swarm robots novelty bootstraps evolution, but earlier work found no gain on non-deceptive tasks.

**Quality-diversity (2015-2016).** MAP-Elites (a12, b09, b10, c27): keep the best solution in each cell of a user-chosen feature grid; pick a random filled cell; mutate it; place the child in its cell if it beats the occupant. Better reliability and coverage than controls (p<0.002 in soft robots, p<1e-7 on retina), but no significant gain in the single best solution (p>0.05) and worse precision (p<0.01) in soft robots. Stepping stones: elites descend from a good neighbour a medium distance away (b10). The QD score (sum of best quality over niches) comes from Pugh et al. 2016 (a13, snippet only).

**Deep RL and open-ended systems (2018-2021).**
- Conti et al. 2018 (a14, a15): NS-ES, NSR-ES (average of reward and novelty), NSRA-ES (adaptive weight). Humanoid with a trap, 10 runs: plain ES stuck every run. NSRA-ES beat NS-ES and NSR-ES (p<0.01). Seaquest median: ES 960, NS-ES 1044.5, NSR-ES 2329.7 (5 runs).
- Go-Explore (a16, b13, b25): archive of reached states; return to a promising one; then explore. It names two failures of novelty-driven agents: detachment (forgetting promising areas) and derailment (exploring before returning). Scores differ by version. arXiv: Montezuma mean 43,763 without domain knowledge, 666,474 with; Pitfall mean 59,494, max 107,363. Nature: robustified Montezuma mean 1,731,645; Pitfall mean 102,571. Earlier agents scored 2,500 or less on Montezuma (stochastic tests) and 0 on Pitfall. Do not mix versions.
- POET and Enhanced POET (a17, a18): co-evolve environments and agents, with a minimal criterion (not too easy, not too hard) and transfer between environments. Original POET progress plateaued around 20,000 iterations; Enhanced POET kept rising nearly linearly (5 runs). Controls underperformed (p<0.01).
- Tao, Francois-Lavet and Pineau 2020 (a19, b11, b12, c10): novelty = k-NN distance in a learned low-dimensional latent space. See section 4.
- Lehman et al. 2020 anecdote collection (a20): open search often finds unintended solutions and exploits bugs.
- Taiga et al. 2020 (b14): under one common setup, bonus methods barely beat epsilon-greedy. Rainbow, 200M frames, seven hard games plus the training set: pseudo-count worse on all training games except Seaquest; RND and ICM only matched epsilon-greedy.
- Burda et al. 2018 (d17): surprise-driven curiosity is drawn to pure randomness (noisy TV). Figure-only evidence.

**Foundation-model era (2022-2026).** The stepping-stone idea moved into LLM systems: ELM (an LLM as mutation operator), QDAIF (an LLM judges quality and labels niches), OMNI and OMNI-EPIC (an LLM judges interestingness), Voyager, Intelligent Go-Explore, Rainbow Teaming, Darwin Godel Machine, AlphaEvolve, FunSearch. Details are in sections 3 and 6.

**Theory of the field.** Hughes et al. 2024 (a26, b23, c09) define open-endedness through an observer: artifacts must be novel (hard to predict from the past) and learnable (prediction improves with more history). This explains why pure difference is not enough, and why OMNI added interestingness on top of learning progress. Stanley and Lehman 2015 (a29, c29, book, not opened) is the popular statement of the stepping-stone argument.

## 3. Core findings with exact numbers

Status: E = established (two or more independent sources), S = single source (usually the originating lab), C = contested.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Novelty alone beats goal-fitness on a deceptive hard maze | 39/40 solved vs fitness NEAT 3/40, random 4/40; 35,109 mean evals | a03, b02 (Lehman and Stanley 2011) | S |
| Novelty about 3x faster on medium maze | 18,274 vs 56,334 evals; 40 runs each; p<0.001; random 21/40 | a02, b01 | S |
| Novelty gives farther walking gaits | 4.04 m vs 2.88 m, 50 runs, p<0.01; 87.5 vs 272.9 connections | a07, b03 | S |
| Novelty fails when behaviour space is unbounded | 5/100 vs fitness 2/100, not significant | a04, b04 | S |
| Result depends on the behaviour description | 3-4 irrelevant points: 21/70 and 29/70 runs fail; wrong aliasing 6/70; 4x4 grid about 3x slower; fitness-as-behaviour 11/40 vs 4/40 | a06, b05, b06, b07 | E (2 groups) |
| Blends beat pure novelty and pure fitness in mazes | LS-50 and NSGA best, p<0.01, 180 runs per treatment; random archive and k 15-100 best | a09, a10, a11 (Gomes 2015) | S (one independent group) |
| Archive size matters little in the maze | cap 250: 40/40, 38,324 evals | a05 | S |
| QD gives coverage and reliability, not a better single best | p<0.002 coverage; best solution p>0.05 (soft robots) | a12, b09, b10 | E |
| Adaptive blend escapes deep-RL traps | humanoid trap: ES stuck in 10/10; NSRA-ES > NS-ES, NSR-ES p<0.01; Seaquest ES 960, NSR-ES 2329.7 | a14, a15 | S |
| Bonus-based exploration is weak in standard Atari | pseudo-count worse on nearly all training games; RND, ICM match epsilon-greedy | b14 (Taiga 2020) | S |
| Go-Explore beats intrinsic-motivation agents on hard games | arXiv: 43,763 / 666,474 (Montezuma), 59,494 (Pitfall); Nature: 1,731,645 and 102,571 | a16, b13, b25 | S |
| Latent-space novelty beats random-reward baseline | Acrobot 576.0 vs 1713.3 steps; maze 524.6 vs 1863.3; 5 trials; NOT different from RND on Acrobot (592.5, p=0.85) | a19, b11, c10 | S |
| Growing archives keep improving, controls plateau | POET plateau about 20,000 iters vs Enhanced POET linear; DGM SWE-bench 20.0% to 50.0%, Polyglot 14.2% to 30.7% | a17, a18, a24, c05, a27, c17, d04 | E |
| LLM interestingness model focuses exploration | Crafter: OMNI 82 tasks (14 interesting) vs LP 55 (9); success on interesting 0.78 vs 0.52; AI2-THOR 13 vs 2 tasks at success >=0.6 | a23, b17, c03, c04 | S |
| LLM judges in these loops are only moderately reliable | OMNI-EPIC detector 72.7% vs 50 humans; ACD 92.2% valid; QDAIF human-AI 0.833 vs human-human 0.800; GPT-4 picks own text 73.5%; judge-human agreement lowest on similar items | a24, b18, c06, c02, c24, d13, d14, d15 | E |
| QDAIF: big automatic gain, tiny human-rated gain | human QD 0.772 vs 0.767 (Fixed-Few-Shot); human quality 3.900 vs 4.133 | a22, b16, c01, c02 | C |
| Voyager curriculum plus skill library | 63 items, 3.3x; random curriculum -93%; no skill library: 0/3 diamond vs 1/3; 3 trials | a25, b20, b24, c15, c16 | S |
| Frontier LLMs give few distinct answers | under 3 distinct in 10 samples; Claude-3.5 Sonnet 1.76, gpt-4o 2.88, Gemma-2-2B 5.66, Llama-3.2-1B 6.74; regeneration in context helps most | b22, c11, c12 | S (benchmark), with d11-d13 support |
| Temperature is not exploration | weak link to novelty, moderate to incoherence; embedding similarity above 0.8 even at T=2.0 with min-p | d11, d12, d13 | E (3 sources agree in direction) |
| LLM ideas rated more novel, but saturate | 5.64 vs 4.84, p<0.01, 49 ideas each; about 200 non-duplicates of 4000 | c25, c26 | S |
| Pre-execution novelty overstates value | judged novelty -1.049 for AI ideas after execution vs -0.010 for human, 43 projects | d16 | S |
| Rainbow Teaming archive | about 92-98% attack success at 2000 iterations; fine-tuning cut to 0.3-0.7%; about 50% transfer | a28, b19, c13, c14 | E |
| LLM mutation more robust than random code mutation | GP success zero at 5 bugs; diff mutation degrades only at the 5th bug type | a21, b15, c07, c08 | S |
| Forcing different plans raises correctness at equal attempts | LiveCodeBench pass@200: GPT-4o 60.6 to 73.0; Claude 3.5 Sonnet 55.6 to 77.0; o1-mini 90.8 to 91.3 | d01, d02 | S |
| Answer-novelty bonus with a baseline helps pass@k; goal-only RL narrows coverage | naive UCB fails to generalise; base beats RL at k 128-256 (Minerva 32B about 9 points) | d05, d06, d07 | E |
| Coverage grows with samples; unverified selection stalls | SWE-bench Lite 15.9% to 56% (250 samples); MATH coverage 82.9% to 98.44% but vote 40.50% to 41.41% | d08 | S |
| Return to partial beat restart, at higher cost | Game of 24: ToT b=5 74% ($0.74) vs CoT best of 100 49% ($0.47) | d09, d10 | S |
| Clade-level value predicts later success better than own score | Pearson 0.778 HGM vs DGM 0.285, SICA 0.444 (SWE-Verified-60) | d03 | S |

## 4. Mechanisms and models

**4.1 Novelty search (Lehman and Stanley).**
1. Define a behaviour vector b(x) for each attempt x. Keep it low dimensional.
2. Novelty rho(x) = (1/k) * sum of distance(b(x), b(neighbour_i)) over the k nearest neighbours in population plus archive.
3. If rho(x) > threshold, add b(x) to the archive. Tune the threshold so only a few items enter per generation.
4. Select by rho only. Vary the selected attempts. Repeat.

Settings that worked: k about 15 (15 to 100 best in Gomes 2015); a random archive worked best; an archive capped at population size was fine in the maze.

**4.2 Blends.** Score = w * novelty_rank + (1-w) * goal_rank (LS-50 uses w = 0.5), or multi-objective NSGA with novelty and goal as two objectives. NSRA-ES adapts w: raise the novelty weight when reward has not improved for a set number of steps, lower it when reward improves. Conti et al. note NSRA-ES first fell into the Seaquest trap because it began on reward and moved the weight slowly (a15).

**4.3 MAP-Elites.** Choose feature axes. Make an empty grid. Seed with a few random solutions. Loop: pick a random filled cell, mutate, evaluate, put the child in its cell if the cell is empty or the child is better. Report coverage, QD score and best.

**4.4 Learned latent novelty (Tao et al. 2020).** Encode the observation to a low-dimensional latent with an information bottleneck and a relative-distance loss, so pixel noise is not counted as new. Intrinsic reward = k-NN distance in that latent space, combined with planning. Theorem 1: the score goes to 0 as the whole state space is visited, and it is inversely related to pseudo-count visit probability (b12). Table 1 (5 trials, steps to goal): random reward Acrobot 1713.3 (SE 316), maze 1863.3 (SE 308); novelty 576.0 and 524.6. The text table is partly garbled and critique.md corrected one mislabel: 524.6 is the novelty maze value, not BDQN. Treat as weak (n=5, one group).

**4.5 Go-Explore as an agent loop.** Archive cells of visited states, each with a way to return to it. Loop: choose a cell (weighted toward promising or rarely chosen), return to it, explore from it, add new cells. Intelligent Go-Explore (b21, c21) lets an LLM choose the cell and action instead of hand rules. Game of 24: 100% success, 70.8% faster than the best baseline.

**4.6 Interestingness filter (OMNI).** Give the LLM the list of tasks learned and failed, and candidate new tasks. Ask which are interesting and learnable. Pick among those. OMNI-EPIC adds an archive of tasks including failed ones, a post-generation rejection of dull tasks, and code-written success detectors (72.7% human agreement).

**4.7 LLM-driven QD (QDAIF, ELM, Rainbow Teaming).** The LLM is the mutation operator (diff or rewrite) and the labeller of niches. Rainbow Teaming: grid of risk category x attack style, pairwise LLM preference judge, and a BLEU filter against the parent to keep children different.

**4.8 Prompt-level difference operators.** Two forms exist. (a) In-context regeneration: show the earlier answers and require a different one (NoveltyBench, c12). (b) Plan search: sample many plans in words, then write code from each plan (d01). PlanSearch measures diversity D as 1 minus the fraction of program pairs an LLM calls "same idea" (d02).

**4.9 Open-endedness metrics.** ANNECS (accumulated number of novel environments created and solved), cell coverage in a 2D PCA of text embeddings (OMNI-EPIC), QD score. These measure archive progress, not accuracy.

## 5. What holds up

**Replicated or supported by more than one group.**
- The behaviour description decides everything (Lehman and Stanley, Kistemaker, Gomes). Established.
- Archives of different solutions help over long runs where fixed or no-archive controls plateau (POET, OMNI-EPIC, DGM, Voyager ablation). Established across labs, but all are close to the same research community.
- QD improves coverage and reliability but not the single best (Mouret and Clune, others). Established.
- LLM judges are biased toward their own text and weak where items are close (d13, d14, d15, and the judge-agreement numbers of OMNI-EPIC, QDAIF, Rainbow Teaming). Established.
- Temperature and small-model noise is not useful exploration (d11, d12, d13, and the NoveltyBench small-model result). Established enough.
- Goal-only RL narrows coverage; novelty plus goal, with a baseline, helps (d05, d06, d07).

**Failures, contradictions, and moderators.**
- Pure novelty is not best. Gomes 2015: blends and NSGA beat it on success ratio. PMCNS gave no clear gain. The ordering depends on maze type (deception level).
- Taiga 2020: in standard Atari, bonus methods barely beat epsilon-greedy. Likely causes: hard-exploration vs training-set setups, deterministic restarts. Go-Explore's gains were on hard-exploration games.
- Unenclosed spaces and tasks where novelty is uncorrelated with progress: no advantage (5/100 vs 2/100).
- NoveltyBench: the smallest models are the most diverse. Diversity may track weak tuning, not better exploration. Unexplained.
- QDAIF: automatic QD score rose in all domains, but the human QD margin over Fixed-Few-Shot is 0.005 and human quality was lower. Contested.
- PlanSearch: pass@1 often falls; gain nearly vanishes for o1-mini, a model that already searches. Not shown at equal tokens.
- Tree of Thoughts: the return-to-partial gain costs more tokens (5.5k/1.4k vs 6.7k/2.2k prompt/completion; $0.74 vs $0.47), and return is by LLM value check, not novelty.
- Judged novelty drops after execution (AI ideas -1.049 on a 1-10 scale, 43 projects).
- DGM objective hacking: one run faked the measured behaviour (c18, node 96).
- Noisy TV slowdown confirmed qualitatively (d17), no text-task test.

**Replication status.** Independent replication is thin. Only Kistemaker, Gomes and Taiga re-tested the classic claims. Only HGM (a rival lab) re-ran DGM as a baseline with different backbones: DGM 53.3 on SWE-Verified-60 and 27.1 on Polyglot, HGM 56.7 and 30.5, DGM CPU-hours 2385 vs HGM 347 on Polyglot. Direction reproduced, numbers not comparable (d04). No outside replication of Voyager or OMNI was found.

**Small n.** Tao 5 trials; Voyager 3 trials; Conti 5-10 runs; Enhanced POET 5 runs; OMNI-EPIC 3-5 runs.

**Interventions that worked.** Behaviour descriptors with no irrelevant dimensions; blending a goal term with novelty; a random or capped archive; choosing what to expand by the results of its descendants (d03); a quality floor against diversity; fine-tuning on the archive (Rainbow Teaming).

**Interventions that did not.** Paraphrasing and "be unique" system prompts (NoveltyBench); raising temperature; naive UCB answer bonus; fitness as the behaviour description; self-ranking of ideas by the generating LLM.

## 6. Language models

**Default behaviour is homogeneous.** NoveltyBench (b22, c11, c12): 20 models, 10 samples, T=1. Mean distinct answers: Claude-3.5 Sonnet 1.76, Claude-3.5 Haiku 1.94, Gemini-1.5-pro 1.85, Claude-3 Opus 2.04, Llama-3.3-70B 2.49, gpt-4o-mini 2.65, gpt-4o 2.88, Llama-3.1-405B 3.20, Gemma-2-2B 5.66, Llama-3.2-1B 6.74. Cumulative utility (max 10): gpt-4o 3.27, Claude-3.5 Sonnet 2.36, Gemma-2-2B 4.63. Larger models in a family are often less diverse. The equivalence-class classifier agrees with humans 79% of the time.

**What changed it.** Paraphrasing and "be unique" prompts barely help. In-context regeneration (the model sees its earlier answers and must differ) is best: it roughly matched human writers, and GPT-4o and Gemini 2.0 Pro exceeded human cumulative utility (c12). Our schema's own open-mode number (NoveltyBench 3.18 to 9.63 [O]) fits this.

**Noise is not exploration.** Temperature only weakly raises novelty and moderately raises incoherence (Llama 2-Chat 70B, 100 stories per temperature, 7 temperatures; d11). In Artificial Hivemind (d12, d13; 26,070 open and 8,817 closed queries, 70+ models), same-prompt embedding similarity stays above 0.8 even with min-p at T=2.0. Different models also agree: DeepSeek-V3 vs qwen-max 0.82, vs gpt-4o 0.81. So a second model is a weak source of difference.

**Does difference raise correctness?** Partly.
- PlanSearch (d01, d02) pass@200 on LiveCodeBench (repeated sampling / IdeaSearch / PlanSearch): GPT-4o-mini 53.3 / 59.4 / 64.9; GPT-4o 60.6 / 70.4 / 73.0; DeepSeek-Coder-V2 53.2 / 65.9 / 70.3; Claude-3.5-Sonnet 55.6 / 70.2 / 77.0. HumanEval+ Claude 88.9 / 95.6 / 98.5; MBPP+ Claude 83.0 / 87.8 / 93.7. o1-mini 90.8 / 91.2 / 91.3. Pass@1 often drops. The gain tracks idea-level diversity, not token entropy.
- Outcome-based exploration (d05): Llama-3.1-8B-Instruct and Qwen-2.5-7B-Base on MATH and DAPO data, 3 seeds. A bonus on rare final answers helps pass@k only in versions with a baseline. Gains are small (approx; table rows partly misaligned).
- Rewarding the Unlikely (d06): Lean proving; a rare-but-correct reward adds about 300 correct proofs of 9600 over GRPO variants (approx; rows misaligned).
- Yue et al. (d07): RL models win at k=1, base models win at large k; Minerva 32B base beats RL by about 9 points at k=128. Distillation does expand the boundary.
- Large Language Monkeys (d08): coverage grows log-linearly (SWE-bench Lite 15.9% to 56% at 250 samples; CodeContests Gemma-2B 0.02% to 7.1% at 10,000). Without a verifier, selection plateaus (MATH 40.50% to 41.41%).

**LLM open-ended systems.**
- ELM (a21, b15, c07, c08): 12x12x12 = 1,728 niches; nearly all seeds filled the map from one barely working walker; 80%-cutoff data (95K) gave better models than 50% (280K), at less diversity.
- QDAIF: see section 3. Max QD 20 (100 for the 2D archive). Human quality was lower than the fixed-prompt baseline.
- OMNI: AI2-THOR, 1M steps, 10 seeds: Uniform 0 tasks (CI 0-2), LP 2 (CI 0-3), OMNI 13 (CI 11-17) at success >=0.6. Crafter: uniform 4 tasks (3 interesting, success 0.030); OMNI 82 (CI 80-87), 14 interesting. BabyAI: uniform 1 task, OMNI 8. OMNI vs a human oracle mostly not significant.
- OMNI-EPIC (a24, b18, c05, c06): transfer from a prior task policy: median success 63.2% (CI 42.1-69.5) vs 36.8% from scratch (25 tasks, 5 reps).
- Voyager: 160 iterations, 3 trials; 63 items; wooden tool 15.3x faster, stone 8.5x, iron 6.4x; diamond reached in 1 of 3 runs (102 iterations). One summary (a25) says 3/3 at 19 iterations; critique.md says use 1/3.
- Automated Design of Agentic Systems (c19): DROP F1 +13.6, MGSM +14.4%; after transfer GSM8K +25.9%, GSM-Hard +13.2%.
- Automated Capability Discovery (c24): 92.2% tasks valid; judge F1 0.86 vs humans; about 20% of new tasks still interestingly new after 5000 generations.
- Rainbow Teaming: JailbreakBench with Llama Guard, 66 jailbreaks over 41 behaviours vs PAIR 1 over 1; self-BLEU 0.51 vs 0.74.
- AlphaEvolve (c20, lab report): matched the best known on 75% of 50+ open problems and improved 20%; rank 48 for 4x4 complex matrix multiplication (Strassen recursion gives 49).
- Si et al. (c25, c26, d15, d16): see section 3; LLM judge pairwise accuracy on accepted/rejected papers 61.1 to 71.4% (human reviewer agreement 56.1%).
- HGM (d03, d04): clade-based selection beats own-score selection.

**Takeaway for LLMs.** Difference is cheap to get by showing prior attempts. It is expensive to know whether the difference is useful. The tested gains are at equal attempts, on code and math, and vanish for models that already search.

## 7. What our agent should take

Schema parts: G guardrail, S state, O operator, memory. Status: [E] established, [S] single-source, [C] contested.

### Add now (established [E])

1. **Use in-context regeneration as the difference mechanism in open mode.** A second pass where the model sees labels of earlier answers and must differ. Part: S3 (open mode) and memory. [E] Evidence: b22, c11, c12, d12 (K16). This matches the existing S3 open-mode text.
2. **Do not use temperature, paraphrase prompts or "be unique" instructions as the difference mechanism.** Part: S3 and section 4b (add as a "not to add" line). [E] Evidence: d11, d12, d13, c12 (K16).
3. **Keep a goal term in every score. Never run pure difference scoring.** Part: O and G. [E] Evidence: d05, d06, d07, a09-a11 (K23, K04).
4. **The descriptor of "a different attempt" is the most sensitive choice. Keep it narrow and relevant.** Part: S3 history (what code records as a "direction"). [E] Evidence: b06, b07, a06, b05 (K03). Use the approach label or final-answer class, not raw text distance.
5. **An archive of past attempts or lessons helps over long runs; keep it and ablate it.** Part: memory. [E] Evidence: a17, a18, a24, c05, a27, c17, d04 (K11).
6. **Self-judged novelty is unreliable.** The generating model does not decide whether an attempt is new or good. This restates G8. [E] Evidence: d13, d14, d15, a24, c06 (K13).
7. **QD gives coverage, not a better best answer.** Do not claim a best-answer gain from diversity alone. Part: O. [E] Evidence: a12, b09 (K06).
8. **Adversarial self-testing with a feature-grid archive works for safety checks.** Part: S8 VERIFY (optional, low priority for the reasoning bench). [E] Evidence: a28, b19, c13, c14 (K18).

### Test first ([S] or [C])

1. **Difference-from-prior-attempts operator raises correctness at equal tokens.** Part: O (open mode), S3. [S] Evidence: d01, d02, d05 (K20, K21). Test T1.
2. **Approach-forcing (plans first, then solve) versus plain best-of-k.** Part: S3. [S] d01, d02 (K21). Report pass@1 and pass@k separately; expect pass@1 to drop. Test T2.
3. **Blend a goal score with a difference score; adapt the weight on stall.** Part: O + G. [S] a14, a15, a09 (K04, K07). NSRA-ES rule: raise the difference weight when there is no progress for N steps. Test T4.
4. **Return to a stored partial solution instead of restarting.** Part: S5/S6 and memory. [S] d09, d10, a16, b21 (K09, K25). Tree of Thoughts won but cost more. Test T5.
5. **Skill or insight library and curriculum ablation in a multi-round task.** Part: memory. [S] a25, b24, c16 (K15). Voyager n=3. Test T6.
6. **Ask the model to rate "interesting and learnable" directions, not just new ones.** Part: O. [S] a23, b17, c03, c04 (K12). Must be paired with a code check (G8).
7. **Choose what to expand by the results of its descendants, not its own score.** Part: S6/O tree. [S] d03 (K23). Our tree is capped at 2 expansions (SCHEMA section 4), so probably not usable.
8. **Archive cap and show-versus-filter.** Part: memory. [S] a05, d08 (K05, K24). Untested for context. Test T6.
9. **Pre-execution novelty overstates value; score difference after the check.** Part: G. [S] d16 (K26). Test T10.
10. **LLM-driven variation instead of random edits.** Part: O. [S] a21, c07 (K19). Our agent already uses an LLM to vary; low value.
11. **QDAIF-style diversity-guided search over plain few-shot.** [C] a22, c01, c02 (K14). Low expectation of a human-rated gain.

## 8. Concrete tests on our bench

All tests: both arms use the same total tokens (prompt plus completion, setup cost included, G7). Report pass@1 and the final submitted answer separately. At least 3 seeds. Use items with a code check so G8 holds.

| Test | Item type | Arms (equal tokens) | Metric | Expected effect |
|---|---|---|---|---|
| T1 Difference operator | Items where the first natural answer is often wrong (trap puzzles, BRAINTEASER-style, ARC items where a simple rule fits the examples but fails the held-out case) | A: N independent attempts, code selects. B: N/2 independent attempts, then N/2 attempts shown the first-pass answer labels and told to differ; code selects | Final accuracy after code selection; coverage (correct answer appears in any attempt) | Small gain on trap items (a few points); none or negative on easy items; none on a model that already searches (o1-mini result) |
| T2 Approach-forcing | Same items | A: best-of-k. B: list k distinct approaches in words, then one attempt per approach | pass@1 and pass@k separately; accuracy after selection | pass@k up, pass@1 down (d01) |
| T3 Descriptor | Same items | Three arms: difference judged by approach label, by final-answer class, by embedding distance | Solve rate; count of true duplicates | Approach label or answer class best; embedding worst (d12, b06) |
| T4 Blend and adapt | Mixed deceptive and non-deceptive items | Goal-only; difference-only; fixed 50/50; adaptive (raise difference weight after 2 rounds with no progress) | Accuracy, coverage | Blends beat both pure arms (a09, a14); pure difference loses on non-deceptive items |
| T5 Return vs restart | Multi-step items (Game of 24-like) | A: restart from scratch each try. B: keep the best partial and resume it | Accuracy at equal tokens; tokens per solve | B wins on items with early decisive steps; may lose at equal tokens (d10) |
| T6 Archive ablation | Long multi-round run | With archive of tried directions vs none; cap 5, 20, 80 | Cumulative distinct correct solutions; duplicate rate per round | Archive helps late rounds; cap matters little (a05) |
| T7 Noise distractor | Task plus a random-output tool or irrelevant noisy field | With and without the operator | Share of budget spent on the distractor; accuracy | Operator should not drift to noise (d17); fail if more than 10% of budget is lost |
| T8 Self-judge audit | Candidate directions | Agent self-rated novelty vs external judge vs code-based duplicate test | Agreement rate; archive pollution rate | Self-judge agreement 60-80% (d13-d15); code test needed |
| T9 Distinct counts | NoveltyBench subset | Plain 10 samples vs forced-differ regeneration | Mean distinct of 10; utility | 3 to 6+ distinct (c12; our own 3.18 to 9.63) |
| T10 Post-check scoring | Open-ended generation | Score difference before vs after running the check | Rank change | Pre-check scores inflated (d16) |

## 9. What does not transfer, and why

- **Hand-built behaviour vectors.** Mazes have an (x,y) endpoint. Text answers have no natural low-dimensional space. Embedding distance fails (similarity above 0.8 at T=2.0).
- **Population size and generation counts.** Novelty search uses thousands of evaluations (18,274 to 56,334). Our agent has 2 to 4 short attempts in checked mode and a capped tree (2 expansions). Archive effects need many rounds.
- **Evolutionary mutation.** NEAT, ES and MAP-Elites mutate genomes. An LLM reasoner has no genome; the only analogue is a prompt or plan.
- **Pure novelty.** It works only when novelty correlates with progress. In an unenclosed space it fails (5/100). Many reasoning items have one right answer and no deception; a goal term must stay (G1, G6).
- **Deep RL intrinsic rewards (RND, ICM, pseudo-counts, latent novelty).** They need a trained network and environment steps. The honest result is that they are weak in standard Atari (b14).
- **Go-Explore's big numbers.** The 666,474 and 1.73 million results rely on a resettable simulator and domain-knowledge cells. Text reasoning has no cheap exact return-to-state.
- **Open-ended growth metrics (ANNECS, QD score).** They measure archive growth, not correctness.
- **Interestingness.** Needed for exploration without a goal; our agent always has a task (except in open mode).
- **Cheap self-judging.** LLM judges of interestingness are 73-83% reliable and biased to their own output (G8 limits their use).
- **Human-rated novelty of research ideas.** Not our task, and it falls after execution.

## 10. Open questions

1. Does a "differ from your earlier attempts" operator raise correctness at equal tokens on general reasoning, split by deceptive and non-deceptive items? (K20; PlanSearch is only at equal attempts and only on code.)
2. Best behaviour descriptor for an LLM answer: approach label, answer class, or embedding? No head-to-head found (K22).
3. Adaptive-weight rule (NSRA-ES style) for LLM search: untested (K23).
4. Archive size, and whether to show it in context or filter silently: untested (K24).
5. Error propagation from an imperfect judge through an archive: not measured (K13).
6. Why are the smallest models the most diverse (NoveltyBench)? Weak tuning, or something useful?
7. Does return-to-partial beat restart at equal tokens for reasoning? (K25)
8. Independent replication of Voyager, OMNI and DGM numbers (K27).
9. Text-task noisy TV: does a difference signal chase noise in text? (K26)
10. Do LLM-written success detectors and interestingness judges drift over thousands of steps (DGM objective hacking, c18)?
11. How does a difference operator interact with models that already search (o1-mini: gain of 0.5 points)? This matters for model choice.

## 11. Sources

[V] = opened and read as full text in the evidence phase or critique. [M] = snippet, abstract only, or not read.

1. [V] Lehman and Stanley 2011, Abandoning Objectives. https://www.cs.swarthmore.edu/~meeden/DevelopmentalRobotics/lehman_ecj11.pdf and https://www.cs.swarthmore.edu/~meeden/cs81/f17/papers/lehman_ecj11.pdf (a01-a08, b01-b05). Publisher page https://doi.org/10.1162/EVCO_a_00025 [M] (c28, blocked 403).
2. [V] Kistemaker and Whiteson 2011, Critical factors in the performance of novelty search. https://groups.csail.mit.edu/EVO-DesignOpt/gecco2011Proceedings/proceedings/p965.pdf (b06, b07).
3. [V] Gomes, Urbano and Christensen 2013, Evolution of swarm robotics systems with novelty search. https://arxiv.org/pdf/1304.3362 (b08).
4. [V] Gomes, Mariano and Christensen 2015, Devising effective novelty search algorithms. https://repositorio.iscte-iul.pt/bitstream/10071/23144/1/conferenceObject_26611.pdf (a09-a11).
5. [V] Mouret and Clune 2015, MAP-Elites. https://arxiv.org/abs/1504.04909 (a12, b09, b10; c27 thin).
6. [M] Pugh, Soros and Stanley 2016, Quality diversity. https://doi.org/10.3389/frobt.2016.00040 (a13).
7. [M] Stanley and Lehman 2015, Why Greatness Cannot Be Planned. https://doi.org/10.1007/978-3-319-15524-1 and https://link.springer.com/book/10.1007/978-3-319-15524-1 (a29, c29).
8. [V] Conti et al. 2018, Improving exploration in ES. https://arxiv.org/abs/1712.06560 (a14, a15).
9. [V] Burda et al. 2018, Large-scale study of curiosity-driven learning. https://arxiv.org/abs/1808.04355 (d17; figure-only result).
10. [V] Ecoffet et al. 2019/2021, Go-Explore. https://arxiv.org/abs/2004.12919 and https://arxiv.org/pdf/1901.10995 (a16, b13, b25). Nature page https://doi.org/10.1038/s41586-020-03157-9 [M] (c30).
11. [V] Wang et al. 2019, POET. https://arxiv.org/abs/1901.01753 (a17).
12. [V] Wang et al. 2020, Enhanced POET. https://arxiv.org/abs/2003.08536 (a18).
13. [V] Tao, Francois-Lavet and Pineau 2020, Novelty search in representational space. https://arxiv.org/abs/2009.13579 (a19, b11, b12, c10).
14. [V] Taiga et al. 2020, Bonus-based exploration in the ALE. https://arxiv.org/pdf/1908.02388 (b14).
15. [V] Lehman et al. 2020, Surprising creativity of digital evolution. https://arxiv.org/abs/1803.03453 (a20).
16. [V] Lehman et al. 2022, Evolution through Large Models. https://arxiv.org/abs/2206.08896 (a21, b15, c07, c08).
17. [V] Meyerson et al. 2023, Language Model Crossover. https://arxiv.org/abs/2302.12170 (c22).
18. [V] Bradley et al. 2023, QDAIF. https://arxiv.org/abs/2310.13032 (a22, b16, c01, c02).
19. [V] Zhang et al. 2023/2024, OMNI. https://arxiv.org/abs/2306.01711 (a23, b17, c03, c04).
20. [V] Faldor et al. 2024/2025, OMNI-EPIC. https://arxiv.org/abs/2405.15568 (a24, b18, c05, c06).
21. [V] Wang et al. 2023, Voyager. https://arxiv.org/abs/2305.16291 (a25, b20, b24, c15, c16).
22. [M] Colas et al. 2023, LMA3. https://arxiv.org/abs/2305.12487 (c23; abstract only).
23. [V] Hughes et al. 2024, Open-endedness is essential for ASI. https://arxiv.org/abs/2406.04268 (a26, b23, c09).
24. [V] Lu, Hu and Clune 2025, Intelligent Go-Explore. https://arxiv.org/abs/2405.15143 (b21, c21).
25. [V] Samvelyan et al. 2024, Rainbow Teaming. https://arxiv.org/abs/2402.16822 (a28, b19, c13, c14).
26. [V] Zhang et al. 2025, Darwin Godel Machine. https://arxiv.org/abs/2505.22954 (a27, c17, c18).
27. [V] Hu, Lu and Clune 2024, Automated Design of Agentic Systems. https://arxiv.org/abs/2408.08435 (c19).
28. [V] Novikov et al. 2025, AlphaEvolve. https://arxiv.org/abs/2506.13131 (c20; lab report).
29. [V] Lu, Hu and Clune 2025, Automated Capability Discovery. https://arxiv.org/abs/2502.07577 (c24).
30. [M] Romera-Paredes et al. 2024, FunSearch. https://doi.org/10.1038/s41586-023-06924-6 (c31).
31. [V] Zhang et al. 2025, NoveltyBench. https://arxiv.org/abs/2504.05228 and https://arxiv.org/pdf/2504.05228 (b22, c11, c12).
32. [V] Si, Yang and Hashimoto 2024, Can LLMs generate novel research ideas? https://arxiv.org/abs/2409.04109 (c25, c26, d15).
33. [V] Si, Hashimoto and Yang 2025, The Ideation-Execution Gap. https://arxiv.org/abs/2506.20803 (d16).
34. [V] Wang et al. 2024, PlanSearch. https://arxiv.org/abs/2409.03733 (d01, d02).
35. [V] Wang et al. 2025, Huxley-Godel Machine. https://arxiv.org/abs/2510.21614 (d03, d04).
36. [V] Song, Kempe and Munos 2025, Outcome-based Exploration. https://arxiv.org/abs/2509.06941 (d05; table partly misaligned).
37. [V] He, Fried and Welleck 2025, Rewarding the Unlikely. https://arxiv.org/abs/2506.02355 (d06; table partly misaligned).
38. [V] Yue et al. 2025, Does RL really incentivize reasoning capacity? https://arxiv.org/abs/2504.13837 (d07).
39. [V] Brown et al. 2024, Large Language Monkeys. https://arxiv.org/abs/2407.21787 (d08).
40. [V] Yao et al. 2023, Tree of Thoughts. https://arxiv.org/abs/2305.10601 (d09, d10).
41. [V] Peeperkorn et al. 2024, Is temperature the creativity parameter? https://arxiv.org/abs/2405.00492 (d11).
42. [V] Jiang et al. 2025, Artificial Hivemind. https://arxiv.org/abs/2510.22954 (d12, d13).
43. [V] Panickssery, Bowman and Feng 2024, LLM evaluators recognize and favor their own generations. https://arxiv.org/abs/2404.13076 (d14).
44. [M] "Sampling Is Not Curiosity", NeurIPS 2026 poster listing, https://neurips.cc/virtual/2026/poster/140072 (listed in SUBFIELDS.md, snippet only).

## Source audit (2026-11-03)

Fresh auditors re-opened the sources of 4 established claims: 2 confirmed as written, 2 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **C07.07-K13** (number corrected). Panickssery et al. report GPT-4 is 73.5% accurate at distinguishing its own summaries from other LLMs' and humans' (self-recognition), not that it picks its own text 73.5% of the time; the other numbers (72.7%, 92.2%, 0.833 vs 0.800, 61.1-71.4%) match. Corrected claim: The judges used in LLM open-endedness systems are only moderately reliable: OMNI-EPIC success detector 72.7% agreement with 50 humans; ACD 92.2% of tasks valid; QDAIF human-AI agreement 0.833 vs human-human 0.800. Self-judging adds bias: GPT-4 is 73.5% accurate at recognising its own summaries and self-preference strength is linearly correlated with self-recognition; pairwise LLM judging reaches 61-71% on paper acceptance; judge-human agreement is lowest on similar-quality items.
- **C07.07-K23** (reworded: the sources support less). The sources compare goal-only RL with goal plus novelty/rarity bonuses (Song et al.: bonus needs a baseline, naive UCB did not help test performance; He et al.: GRPO sharpens and underperforms base sampling at large N; Yue et al.: base beats RL at large k), but none tests novelty-only RL, so 'beats either alone' is wider than the evidence. Corrected claim: Adding a novelty bonus to goal-only LLM RL can help: an answer-novelty bonus needed a baseline to improve test pass@k (naive UCB did not), and rewarding rare-but-correct proofs raised pass@N where goal-only GRPO sharpened and lost to base sampling at large N; goal-only RL narrows coverage (base beats RL at large k, e.g. 128-256). Novelty-only LLM RL and adaptive-weight rules (as in NSRA-ES) were not tested in these sources.
- **C07.07-K06** (now single-source: only one opened source, code check).
- **C07.07-K18** (now single-source: only one opened source, code check).
