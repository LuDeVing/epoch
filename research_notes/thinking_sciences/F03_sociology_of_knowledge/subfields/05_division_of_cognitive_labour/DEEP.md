# Division of cognitive labour: deep document

*Subfield F03.05 of the sociology of knowledge. Sources: evidence_a-d.jsonl (ids a01-a29, b01-b31, c01-c29, d01-d23), claims.jsonl (K01-K28), critique.md, all in this folder. Written 2026-11-01. Evidence ids are cited in brackets. Status marks: [E] established (two or more independent sources), [S] single source, [C] contested, [M] model-only (our own toy simulation, not literature).*

Read this first: the theory papers (Kitcher 1990, Strevens 2003) were never opened by us. We know them through critics and reviews. The LLM evidence is strong on one point (agents that see only scores crowd onto the leader) and thin on the main question (does a code-set allocation of untried directions beat free attempts at equal tokens). No source runs that ablation. Our own toy simulations (d21-d23) are predictions, not evidence.

## 1. What it is

The division of cognitive labour asks one question. When a community faces several rival approaches to a problem, how should effort be spread over them?

- If everyone works on the approach that looks most likely to succeed, the community puts all its eggs in one basket. If that approach is wrong or saturates, the rest of the field has nothing.
- If effort is spread too evenly, many workers sit on poor approaches.
- The best spread is a mix. It depends on each approach's chance of success, how fast that chance saturates with more workers, and the cost of being wrong.

Four model families study this [a03]:

1. **Marginal contribution / reward (MCR) models.** Kitcher 1990 and Strevens 2003. Each approach has a success function: chance of success as a function of the number of workers. The best spread is a constrained maximisation. Reward rules (credit to the first finisher, or credit for marginal contribution) push self-interested workers toward that spread.
2. **Epistemic network models.** Zollman, Grim, Rosenstock, Bruner, O'Connor. Bandit-style learning on a communication graph. The question is how much workers should see of each other's results.
3. **Epistemic landscape models.** Weisberg and Muldoon 2009, Thoma 2015, Wu 2024. Workers walk on a landscape of approaches. The question is which movement rules (follow, avoid, climb) give the best coverage.
4. **Cognitive diversity models.** Hong and Page 2004. A random group with different search heuristics may beat a group of the individually best workers.

For our agent, "workers" are attempts (or sub-agents) and "approaches" are directions. The schema state S3 in open mode says: code keeps a history of directions tried and assigns untried ones. This subfield asks whether that is the right rule, and what the human and LLM evidence says about how to set it.

## 2. History and theories in depth

### 2.1 Kitcher 1990: the founding model
- Treats the spread of scientists over rival approaches as a resource-allocation problem [a01, a02].
- Each approach has a return function: P(success) as a function of the number of workers n.
- A community of purely truth-seeking agents piles onto the most likely approach. A community whose members also seek credit can do better as a group, because credit-seekers weigh two things: the chance the approach works, and the chance of being first. The second pushes toward under-staffed approaches [a03].
- Motivating example, second hand from a blog summary [a29, a01]: before Lavoisier's experiment of 23 April 1787, phlogiston had 0.51 and the new chemistry 0.49. After the experiment the numbers swapped to 0.49 and 0.51. The blog may be inaccurate.
- Primary text not opened (paywalled). Our knowledge is from reviews and critics only.

### 2.2 Strevens 2003: the priority rule
- Explains the priority rule in science (all credit to the first finisher) as a reward scheme that yields a near-optimal spread without a planner [a04, a03].
- Compares it with a marginal-contribution scheme ("Marge"). In his analysis the form of the success function cancels (per a02).
- Critics: Schneider and Rubin 2021 (priority disputes are idealised away); Heesen and Zollman (under some readings of the rule results are very bad). Both seen only as snippets [a04].
- Primary text not opened.

### 2.3 Muldoon and Weisberg 2011: robustness test (the first big challenge)
They rebuilt Strevens' scheme as an agent-based model [a06]: NetLogo 3.1.4, 500 agents, two projects with equal maximum success chance and payoff, project 2 harder (easiness r = 0.02 vs 0.03), logistic success function P = K/(1+e^(-rN)), agents on a 35 x 35 torus, random-order re-decisions, 10 rounds to equilibrium.
- With full information the model reproduced Kitcher and Strevens qualitatively: few agents all take the easier project; more agents put a minority on the harder one; many agents put more on it.
- **Break 1: local vision [a07].** When agents see only neighbours within a radius, a majority pile onto the easier project at radius 12 or less, and none work on the harder project below radius 7.
- **Break 2: noisy beliefs about easiness [a08].** With the same mean and rising variance in beliefs about how easy each project is, the community misallocates toward the easier project. Zero variance gives the original result.
- Their philosophical argument: success probabilities can only be subjective, since a project is either right or wrong (phlogiston chance must be zero, DNA one).
- Four idealisations they list [a02]: utility maximisers; a fixed set of predefined projects; everyone knows the current distribution of workers; everyone knows the true success function.

### 2.4 Weisberg and Muldoon 2009: epistemic landscapes
A 101 x 101 torus (10,201 patches) with two Gaussian peaks (centres (25,25) amplitude 0.75 and (5,5) amplitude 0.7). Visiting a patch reveals its significance at no cost. Three agent types [a09]:
- **Control**: hill climbing with experimentation (2% chance of a random step on a plateau).
- **Follower**: moves toward the best visited neighbour.
- **Maverick**: avoids visited patches; climbs only when no unvisited neighbour exists.

Results are in section 3. The authors concluded that mixed populations are best (a few mavericks lift many followers).

### 2.5 The counter-literature on landscapes
- **Alexander, Himmelreich and Thompson 2015** [a14, d14]: a novelty-seeking strategy need not be optimal; W&M did not show an epistemic reason for division of labour; errors named. Abstract only.
- **Thoma 2015** [a15, b04-b07, d16]: in the original model homogeneous mavericks beat every mixed group, so the mixed-is-ideal claim is not supported by their own data. In Thoma's own model diversity helps only with medium or long movement range.
- **Fernandez Pinto and Fernandez Pinto 2018** [b03]: reimplementation in FreePascal. The code logic was correct but small changes to agent rules changed results a lot. Abstract only.
- **Poyhonen 2017** [a16]: with heterogeneous learning heuristics, diversity pays only when the problem is hard enough. Abstract only.
- **Bedessem 2019** [a17]: models miss hierarchical goal levels and the nature of the object. Abstract only.
- **Wu 2024 "Better than Best"** [b08-b10]: copying a random better neighbour beats copying the best on NK landscapes.

### 2.6 Network epistemology and transient diversity
- Zollman 2007 and 2010 [a25, a26, b12]: in bandit-style learning, less connected networks reach the right consensus more often but slower. Diversity should be transient, not permanent.
- Rosenstock, Bruner and O'Connor 2017 [a24, d15]: this is not robust. With more nodes or a bigger gap between arm success rates, the dense network's chance of wrong consensus falls near zero [a28, d13].
- Wu and O'Connor 2023 [a22, a23]: review of mechanisms to keep diversity (stubbornness, mild confirmation bias, individual exploration, not sharing). None tracks the optimal bandit rule (Gittins index, shrinking epsilon-greedy). Peptic ulcer story: Palmer 1954 convinced the field that bacteria cannot live in the stomach; overturned by Warren and Marshall 1983.
- Smaldino et al. 2024 [d19]: any mechanism that keeps solutions diverse longer raises final quality at the cost of time. Exceptions: easy problems and misaligned incentives.

### 2.7 Hong and Page 2004 and its limits
Diverse random groups can beat groups of the best individuals [a18]. Grim et al. 2019 [d17] show this is sensitive to landscape randomness (abstract only). Reijula, Kuorikoski and MacLeod 2023 [a19] separate cognitive diversity (all work on the whole problem with different heuristics) from true division of labour (parts of the problem go to different workers) and show splitting pays only when the problem is partly modular.

### 2.8 The agent-era turn (2024-2026)
Evolutionary program-search systems (AlphaEvolve, ShinkaEvolve, Darwin Godel Machine) hard-code the division (islands, MAP-Elites, weighted parent sampling). Multi-agent research systems (CORAL, Coral Discovery, ASCollab) leave it to agents who share state. The first direct test of Kitcher's idea in LLM agents is Coral Discovery [c01, c08].

## 3. Core findings with exact numbers

Status key: [E] established, [S] single source, [C] contested, [M] our own toy model.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Kitcher/Strevens: best spread is a mix; credit rules approximate it | No numbers recovered. Phlogiston example 0.51 vs 0.49 (second hand) | a01, a02, a04, a29 | [E] in kind (2 independent descriptions); theory only |
| MCR result breaks with local vision | Majority on easier project at radius <= 12; zero on harder project at radius < 7 (500 agents, 35x35 torus) | a07 | [S] |
| MCR result breaks with noisy beliefs about easiness | Same mean, rising variance moves allocation to the easier project; zero variance matches Kitcher | a08 | [S] |
| Controls (hill climbers) find peaks slowly, luck-dominated | 10 controls: both peaks in 95/100 runs; time to both peaks min 553, max 43,004, mean 6,075 (SD 8,518), median 2,553 | a10 | [S] model |
| Controls: coverage rises linearly with team size | 400 controls: 0.24 progress at 500 cycles, 0.69 at 10,000; gains for peak-finding small beyond 30 | a10 | [S] model |
| Followers do worse than controls | 10 followers: zero runs found both peaks. 200 followers: one peak 60%, both 12%. 400 followers: progress 0.17 | a11 | [S] model |
| Mavericks beat controls and followers | 10 mavericks: both peaks in 99% of runs, mean 80 cycles; 100: 37; 200: 33. Progress at 200 cycles: 10 = 0.10, 100 = 0.55, 200 = 0.75, 400 = 0.90 | a12 | [C] (see next rows) |
| A few mavericks lift followers more than their own work | 400 followers + 1 maverick: +0.02 progress (t=5.74, p<.001), +232 approaches (t=10.8). 100 followers 0.07 -> 0.15 with 10 mavericks (+214%); 400 followers 0.17 -> 0.28 (+165%) | a13 | [C] |
| In the original model pure mavericks beat every mix | 400 mavericks find >90% of significant approaches in 200 periods; 400 followers 17% | b02, b04 | [C] (Thoma vs W&M) |
| Mix beats pure groups only at medium movement range | Medium range (10): mix beats both pure groups, p<0.0001. Local movement, groups of 40: after 50 rounds pure explorers 15% found vs 50/50 mix 8%; mix wins by a tiny margin by round 300 when 90% already found | b05 | [S] |
| Mixes cut variance | After 150 steps at medium range, SD 12.5 points (pure extractors) vs 3.1 (mix with 40% explorers) | b06 | [S] |
| Better-than-best copying | Copy a random better neighbour beats copy-the-best in over 74% of parameter combinations and 100% when social learning is less frequent than every round. NK N=20, 2 communities of 100 agents, 1000 sims per setting | b08 | [C] (fails when learning every round; toy) |
| Hong-Page: diverse beats best | 10 agents, l=12: best 92.56 (diversity 70.98%) vs random 94.53 (90.99%). 20 agents: 93.78 vs 94.72. 10 agents, l=20: 93.52 vs 96.08. 50 trials, 2,000-point random landscape | a18 | [C] (Grim 2019; Reijula 2021-22) |
| Partial connectivity raises human cultural accumulation | 144 students, groups of 6. Level-3 A3: 50% full vs 91.7% partial; B3: 33.3% vs 66.7%; both: 0% vs 58.3%. Full groups ahead early, peak at about 35 of 72 trials | a20 | [S] human; small group count |
| Efficient networks win on a single-peak landscape | 256 web experiments, groups of 16, 15 rounds; 232 sessions analysed; peak found in 138/232 (59.5%). Score if found: networked 68 vs independent 39. Path length beta = -4.63 | a21 | [S] human |
| Connectivity effect is task dependent | Derex and Boyd (less contact better) vs Mason and Watts (more contact better) | a20, a21, a22 | [C] |
| Sparse networks better (Zollman) not robust | Larger networks or bigger arm gaps drive dense-network wrong-consensus near zero | a24, a28, d13 | [C] (numbers not opened) |
| Division of labour pays only if the problem is partly modular | N=12, two blocks of 6: reductionist split leads early then plateaus; 6/6 split reaches optimum; 5/7 split almost as good | a19 | [S] model |
| Field data: scientists choose conservatively | 30 years MEDLINE: inferred strategy peaks in efficiency at 13% of network discovered; over 3x more costly than best alternative for the bulk; best 50% strategy nearly 10x more efficient than random | d20 | [S] |
| LLM agents with score-only sharing crowd onto the leader | Last-third HHI baseline vs direction board: 1.00 vs 0.66 (Signal), 1.00 vs 0.36 (Circle-Pack), 0.82 vs 0.29 (Erdos). 3 of 4 agents in one direction for most of the run | c01 | [E] (with b13, b14, c15) |
| LLM peer selection locks in | Two-armed, pA=0.6 vs pB=0.5, T=50, 30 runs: counts bimodal (near 0 or near 50) | b13 | [S] preprint |
| Code removes lock-in | Qwen-7B inferior-peer lock-in (pA 0.6 vs pB 0.4): prompt-only 50.0%, UCB formula in prompt 23.3%, UCB calculator tool 0.0%, algorithmic UCB 0.0%. Regret 20.0 / 13.5 / 9.9 / 9.8 | b14 | [E] with b17 |
| LLMs fail in-context bandits | GPT-4 basic prompt: suffix failure (best arm never chosen again) in over 60% of replicates; only 1 config (CoT + exploration hint + external summary stats) works robustly | b17, b18 | [E] older models |
| Direction board plus claim check wins against shared leaderboard | 6 wins, 1 tie, 2 losses over 9 tasks (best of 3 runs). Against published MIT CORAL numbers: 4 wins, 2 ties, 3 losses. Directions opened 68 vs 41; after first third 34 vs 15 | c02, c04, c07 | [S] |
| Gain comes from directions the baseline never entered | Kernel: 25 Discovery-only directions, 7 with records; Polyominoes 8 (4); Signal 6 (4); Circle-Pack 4 (1); Erdos 6 (4). Polyominoes 91.78 vs 80.55 (prior SOTA 87.0). Kernel 1095 vs 1138 | c04, c02 | [S] |
| More agents alone do not help | 4-agent shared-leaderboard baseline beat single agent on 3 of 9 tasks | c03 | [S] |
| Local records only appear with the board | Discovery vs baseline: 9 vs 0 (Signal), 4 vs 0 (Circle-Pack), 15 vs 4 (Erdos) | c05 | [S] |
| After a record, effort concentrates | 76% of the remaining 38 evals went to the Signal champion | c05 | [S] |
| Spreading has a cost | LLM-SQL: 7 directions vs 2; 15% of evals in directions that never produced a record; best 0.732704 vs baseline 0.733963 vs single agent 0.735769. Txn Sched 4566 vs single 4608 (baseline 4367) | c07 | [S] |
| Shared notes beat independent runs on some tasks | Kernel 1103 vs 1180 (best of 4 independent); Polyominoes 84.2 vs 80.8; Txn Sched 4694 vs 4629. Kernel 1103 vs single 1350 (18.3%) | c09 | [C] |
| Removing notes hurts | Kernel 1350 -> 1601 (18.6% regression); Polyominoes 80.2 -> 77.3; Txn Sched 4566 -> 4444 | c12 | [S] |
| Agents cover different ground, build across agents | Jaccard overlap 0.43 (Kernel), 0.31 (Polyominoes); 36% of Kernel attempts used another agent's commit and improved 17% vs 9% overall; 66% of new records had a cross-agent parent | c10, c11 | [S] correlational |
| Independent agents duplicate each other | Almost half of top findings overlapped substantially in the independent baseline; ASCollab top 25 had no duplicates | c15 | [S] |
| Keeping non-leader branches alive beats follow-the-best | DGM (80 iterations): open-ended parents 50.0% SWE-bench / 38.0% Polyglot; always-best-parent 39.7% / 30.0%; no archive 23.0% / 14.0%; start 20.0% | d01, d02 | [E] with d06 |
| Weighted parent sampling beats hill climbing | ShinkaEvolve circle packing, about 150 evals; hill climbing plateaus early; novelty filter at similarity 0.95 helps | d06, c20 | [E] with d01 (curves only) |
| Better exploration needs better operators | AIRA-dojo MLE-bench Lite, 20 seeds: AIDE operators with MCTS (UCT 0, 0.25, 0.75) or EVO stayed near greedy (35.0-39.8). AIRA greedy 45.5 vs AIDE greedy 39.8; AIRA MCTS 47.0 | d03 | [S] |
| Memory of own earlier attempts did not help | AIDE with vs without Memory operator: nearly identical medal rate | d04 | [C] with c12 |
| Own score misleads allocation | Validation medal rate keeps rising, test rate plateaus; picking final node closes over 60% of gap; top-3 submissions add about 10% | d05 | [S] |
| Coverage grows with samples, selection does not | SWE-bench Lite 15.9% (1 sample) -> 56% (250); MATH Llama-3-8B coverage 82.9% (100) -> 98.44% (10,000); majority vote or reward model 40.50% -> 41.41% | b23 | [S] |
| One model's samples are near duplicates | 4000 generated ideas -> about 200 non-duplicate (about 5%) at cosine 0.8 | b25, c17 | [E] with b26, c21 |
| Different models are also alike | 42 models: within-prompt similarity mean 0.821 (26K prompts); 70+ models usually above 0.8; with min-p at T=2.0: 81% of pairs above 0.7, 61.2% above 0.8. Most of 20 models give under 3 distinct answers in 10 queries | b26, c22, c21 | [E] |
| Verbalized sampling raises diversity | 1.6x-2.1x; human diversity rating poem 1.90 -> 2.39, story 2.74 -> 3.06, joke 1.83 -> 3.01; recovers 66.8% of base-model diversity | c23, d07 | [E] for creative writing only |
| Prompt diversity lifted a downstream score | Math student accuracy: baseline 32.8; direct 30.6; sequence 33.7; multi-turn 34.3; VS-standard 36.1; VS-CoT 37.5 | d08 | [S] |
| Approach-diverse prompting beats same-prompt sampling | GPT-4 Blocksworld 3: CoT 70%, SC-10 73%, DIV-SE 94%. Graph colouring: CoT 15%, SC-10 23%, DIV-SE 97% (external verifier). Blocksworld 4/5: 40 / 41.2 / +29.6 pts | b19, b20 | [C] |
| Mixed models vs same-model samples | MoA multi-proposer 61.3 vs single 56.7 (n=6); three-model debate 91% vs same-model triple 82% on GSM8K (individual starts 78/64/70). Self-MoA beats Mixed-MoA by 6.6 (AlpacaEval 2.0) and 3.8 (avg of MMLU/CRUX/MATH) | b21, c24, d09 | [C] |
| Quality outweighs diversity | Regression on about 70 mixtures per dataset: alpha(quality)/beta(diversity) 2.558/1.841 (MMLU, R2 0.771), 4.548/1.421 (CRUX, 0.685), 4.719/2.839 (MATH, 0.760); all p<0.001 | d10 | [S] |
| Branch diversity from heterogeneous model pool | 4 unique branches: above 80% (3 models) vs under 20% (1 model) on MBPP. Ablations cut HotpotQA 0.59 -> 0.45-0.51 | b30, b31 | [S] |
| Multi-agent debate does not reliably beat single agent + self-consistency | MMLU SC 0.78 vs single 0.76 vs Society of Mind 0.73; GPQA single 0.33 vs SoM 0.27; MedQA Medprompt 0.65, SoM 0.64, SC 0.60, single 0.60 | d11, c25 | [C] |
| Multi-agent systems fail often | 1600+ traces, 7 frameworks, failure 41%-86.7%; design 41.8%, inter-agent misalignment 36.9%, verification 21.3%; verification step +15.6% on ProgramDev | b28, d12 | [S] |
| Debate for divergent thinking | Counter-intuitive arithmetic (200 q): GPT-3.5 26.0, CoT 28.0, SC 29.5, self-reflect 27.5, MAD 37.0; GPT-4 51.0 | b27 | [S] |
| Co-Scientist tournament | 203 goals, Elo of top hypotheses rises across 10 time buckets | b29, c26 | [S] (self-judged) |
| Own toy: credit-seeking vs equal split under noise | % of optimum, a=0.02, noise sd 0/0.25/0.5/1/2/chance: credit 98.1/90.5/81.9/72.7/66.0/70.4; equal split 83.4-83.6 flat | d21 | [M] |
| Own toy: free vs quota vs cap in sequence | Score, rho 0/0.3/0.6: free 0.695/0.884/1.066; quota 0.793/0.772/0.774; cap 2 then exploit 0.940/0.961/0.956; cap 3 0.683/0.678/0.668 | d22 | [M] |
| Own toy: pivot and explore share | Pivot m=1,2,3,5,8,12 (tau 3): 0.862/0.923/0.859/0.809/0.674/0.523. Explore share 0.2/0.33/0.5/0.7/1.0: 0.687/0.780/0.901/0.986/0.666 | d23 | [M] |

## 4. Mechanisms and models

Each mechanism is written so an engineer can code it.

### 4.1 Kitcher/Strevens allocation (MCR)
State: projects i = 1..m, each with a success function p_i(n) that rises with workers n and saturates. A planner picks n_i with sum n_i = N to maximise sum p_i(n_i).
- Planner optimum: add workers one at a time to the project with the highest marginal gain p_i(n_i+1) - p_i(n_i). A hard project with low ceiling but fast saturation gets a small team; a high-ceiling slow-saturating project gets a large one.
- Decentralised version: each worker joins the project with the highest personal expected credit. Under the priority rule, credit goes to the first finisher, so expected credit for joining project i is roughly p_i(n_i+1) times the chance of being first. More workers on i lower each worker's chance of being first, so workers spill to under-staffed projects. (This formula is our reading of the reviews, not copied from the primary.)
- Needs: the success functions, and the current worker distribution. Both are idealisations [a02]. Muldoon and Weisberg break it with local vision (a07) and with noisy beliefs (a08).

Engineer's version for our agent: directions are projects; attempts are workers. Estimate each direction's yield from its attempts so far; add a bonus for fewer attempts. This is what Coral Discovery's formula does (4.4).

### 4.2 Epistemic landscape
- Grid of approaches; height = significance. Agent types:
  - Control: move to the highest neighbour if higher than here; otherwise stay (2% random step on a plateau).
  - Follower: move toward the best already-visited neighbour among 8.
  - Maverick: move to an unvisited neighbour if one exists; otherwise climb.
- Progress = share of significant patches visited. Mix ratio is the main parameter.
- Why followers fail: they cluster and circle each other's trails [a11]. Why a few mavericks help: they pull followers off stuck trails [a13].
- Thoma's refinement [b05]: add movement range. Explorers jump to an unvisited point within the range; extractors climb. Mix gain appears at medium range (10) only.
- Wu's NK variant [b08]: agents copy a random better neighbour (not the best). Keeps variety alive longer; fails if learning happens every round.

### 4.3 Bandit and network epistemology
- Arms with unknown success rates; agents pull arms and share results with neighbours on a graph. Dense graph: fast consensus, may lock onto a wrong arm. Sparse graph: slower, more reliable in some parameter ranges; not robust (a24).
- Normative baseline: Gittins index or decaying epsilon-greedy [a23]. None of the human mechanisms matches it.
- Implementation hint: the same structure appears in LLM peer selection [b13-b16]. A code-side UCB score removes lock-in (b14).

### 4.4 Coral Discovery's direction board (the one working LLM instance)
From c06, c05:
1. Label every submission with a direction (an LLM reads diffs; no inter-rater check).
2. Per direction, track yield: the shrunken mean credit per evaluation. Credit is earned only against the direction's own best, so a lagging direction can still set local records.
3. Score each direction with yield plus a UCB-like bonus c * ln N / (n_all + 1).
4. Add a NEW arm that prices opening one more direction. NEW = y+ before any opening, y+/(j+1) after j fruitless openings.
5. Seats go in proportion to potential, by largest remainder.
6. Rules: at most 2 agents per direction; a claim check rejects duplicate methods; each agent gets a distinct direction in round 1; after 5 scored evals without a personal best a Diagnose block fires.
7. The board is advisory. The agent decides. No sweep of constants and no ablation of any single rule.

### 4.5 CORAL heartbeat (the contrast) [c13]
Timing rules, not allocation: Pivot after 5 non-improving evals, Reflect every eval, Consolidate every 10. Direction choice is left to the agent. Shared notes and skills carry knowledge across agents.

### 4.6 Parent sampling with a soft cap (DGM, ShinkaEvolve)
DGM [d02]: weight of an archived agent = sigmoid(score; lambda = 10) / (1 + n_children). More children, lower chance to be a parent. ShinkaEvolve [d06]: weighted by fitness and number of offspring; novelty rejection if embedding similarity above 0.95. Both keep non-leaders alive without a hard quota.

### 4.7 Modular split [a19]
Divide-and-conquer only pays if the problem has block structure. Wrong split points give weak signals but can look nearly right (5|7 vs 6|6). Splitting differs from diversity: in splitting each worker sees part of the problem.

### 4.8 Own toy models (not literature) [d21-d23]
- d21: 5 projects, 50 researchers, return = sum q_i(1 - exp(-a n_i)). Credit-seeking by noisy estimates drops under an equal split at log-noise sd 0.25-0.5.
- d22: 10 directions, ceilings ~N(0,1), value = ceiling * (1 - exp(-n/3)), observed noise sd 0.5, 30 sequential attempts. Cap 2 then exploit was the best code rule; cap 3 (explore to the end) was worse.
- d23: pivot after m fruitless attempts to a code-chosen untried direction; best m = 2 when directions improve fast; flat when slow. Explore share best at 70%.

All three depend on assumptions chosen by us (learning time constant, noise, return curve). They give a design for a real run, not a result.

## 5. What holds up

### 5.1 Holds
- **Score-only sharing makes agents follow the leader.** Coral Discovery (HHI up to 1.00 in the last third) [c01], independent agents duplicating one another [c15], and LLM peer selection locking in [b13, c27] agree. Three sources, [E]. Human parallel: Weisberg-Muldoon followers circle one trail [a11].
- **Code-held exploration removes lock-in.** A UCB calculator tool took inferior-peer lock-in from 50.0% to 0.0% [b14]; prompting the formula only halves it (23.3%). GPT-4 fails in-context bandits [b17]. [E], but small models and simple bandits.
- **Keeping non-leader branches alive beats always following the best.** DGM 50.0 vs 39.7 [d01], ShinkaEvolve hill-climb plateau [d06]. [E] but at equal iterations, not equal tokens.
- **One model's samples are alike, so spread must be imposed.** 5% unique of 4000 ideas [b25]; mean pair similarity 0.821 across 42 models [b26]; under 3 distinct answers in 10 queries [c21]. [E]
- **Separate coverage from selection.** Coverage 56% vs picked 41% [b23].

### 5.2 Does not hold, or is contested
- **Kitcher's result is not robust to its idealisations.** Local vision and noisy beliefs break it [a07, a08]. One replication family (the same authors).
- **Maverick dominance and mixed-is-best.** Thoma shows pure mavericks beat every mix in the original model, and the mix wins only at medium movement range [b04, b05]. Alexander et al. contest the original [a14]. Fernandez Pinto: result sensitive to small rule changes [b03].
- **Less connection is better.** Zollman's result is not robust [a24]; human data go both ways [a20 vs a21].
- **Diversity beats ability.** Sensitive to landscape randomness [d17]; gap only 1-2.5 points in the original [a18]; in LLMs, quality beats diversity in a regression [d10] and one strong model sampled many times beats a mix [d09].
- **Debate.** Not reliably better than single agent + self-consistency [d11, c25]; matches schema G9.
- **Memory of own attempts.** No effect for AIDE [d04], but CORAL's ablation hurts when notes are removed [c12]. [C]

### 5.3 Moderators
- Movement range (local vs medium vs global) [b05].
- Problem hardness: diversity pays only when the problem is hard enough [a16]; easy problems are an exception [d19].
- Problem modularity [a19].
- Frequency of social learning [b08] and connectivity [a20, a21, a24].
- Landscape randomness [d17].
- Quality of the attempt-generating operators [d03]: weak operators make exploration settings irrelevant.
- Model scale: bigger models gain more from verbalized sampling [d07]; bigger models are less diverse by default in the same family [c21].
- Task type: Coral Discovery lost on two tasks where a single agent keeps whole process history [c07].

### 5.4 Interventions that worked
- Direction board with claim check and per-direction credit [c01, c02].
- External UCB calculator [b14].
- Soft-cap parent sampling [d01, d06].
- Approach-diverse prompting with a checker (DIV-SE) [b19].
- Verbalized sampling for creative diversity [c23, d07].
- Embedding novelty rejection at 0.95 [d06, c20].
- Verification step in a multi-agent system (+15.6%) [d12].
- Submitting top-3 candidates (about +10%) [d05].

### 5.5 Interventions that did not work
- Giving a UCB formula in the prompt only (23.3% lock-in left) [b14].
- Better UCT constants with weak operators [d03].
- Min-p or adversarial prompting for diversity: 61.2% of pairs still above 0.8 [b26]; marginal gain for SYMPHONY [b30].
- More agents without allocation: 3 of 9 tasks [c03].
- Prompting the model to list earlier ideas and avoid repeats: still 5% unique [b25].
- Debate beyond self-consistency [d11].

### 5.6 Where the evidence is weak
- Core theory papers not opened; numbers second-hand [critique.md].
- Most agent results are best-of-3 on 9 tasks; some margins in the third decimal (Erdos 0.380984 vs 0.381264) [c02].
- Equal-token accounting missing in most LLM papers. Coral Discovery matches eval budget, not tokens.
- Two very recent preprints (Coral Discovery 2610.33281; Choi 2607.11250), not peer reviewed.
- Evidence lines seen only as snippet or abstract (do not cite numbers): a01, a04, a05, a14-a17, a24-a27, b01, b03, b11, b12, b24, c27-c29.

## 6. Language models

### 6.1 Behaviour on these tasks
- **They do not spread by themselves.** In a two-peer delegation game, Qwen2.5-7B, GPT-4 and GPT-5 lock onto one peer; selection counts are near 0 or near 50 of 50 rounds [b13]. GPT-4 on bandits: suffix failure in over 60% of basic-prompt replicates; one config works [b17]. A second failure is uniform picking with no narrowing [b18]. So both too little and too much spread occur.
- **They crowd onto the leader when they see scores.** Four Claude Opus 4.6 agents with a leaderboard: 3 of 4 in one direction for most of the run; HHI 1.00 in the last third [c01].
- **One model repeats itself.** 5% unique ideas in 4000 [b25]. Within-prompt similarity 0.821 across 42 models [b26]. Bigger models less diverse in the same family [c21].
- **Different models do not fix it much.** Across-model similarity 71-82% [b26]. SYMPHONY found that a three-model pool gives over 80% four-unique-branch expansions vs under 20% for one model [b30], so model mixing does add branch variety. Self-MoA argues quality matters more [d09, d10].
- **Self-ranking of directions is unreliable (G8).** AIRA-dojo: the agent's own validation score rises while held-out score plateaus [d05].

### 6.2 What changed behaviour, by how much
| Change | Effect | Id |
|---|---|---|
| Direction board + claim check + credit per direction | HHI last third 1.00 -> 0.66 / 0.36 (Signal, Circle) and 0.82 -> 0.29 (Erdos); directions 41 -> 68; 6 wins 1 tie 2 losses vs reproduced baseline | c01, c02, c04 |
| External UCB tool vs prompt-only (Qwen-7B) | Lock-in 50.0% -> 0.0%; regret 20.0 -> 9.9 | b14 |
| Formula in prompt | Lock-in 50.0% -> 23.3% | b14 |
| Chain of thought + hint + summary stats (GPT-4) | Only config that avoids suffix failure robustly | b17 |
| Soft-cap parent sampling (DGM) | 39.7 -> 50.0 (SWE-bench), 30.0 -> 38.0 (Polyglot) | d01 |
| Approach-diverse prompting (GPT-4) | Blocksworld 3: 73 -> 94; colouring 23 -> 97 | b19 |
| Verbalized sampling | Diversity 1.6-2.1x; math student score 30.6 -> 36.1 / 37.5 | c23, d08 |
| Better operators (AIRA) | Greedy 39.8 -> 45.5; MCTS 47.0 | d03 |
| Three-model pool | 4 unique branches in over 80% vs under 20% of expansions; GSM8K 91 vs 82 | b30, c24 |
| Notes and skills shared | Kernel 1601 (single, no notes) -> 1350 (single with notes) -> 1103 (4 agents sharing); lower is better | c09, c12 |
| Verification step in multi-agent system | +15.6% task success on ProgramDev | d12 |
| Top-3 submission | About +10% | d05 |

### 6.3 Costs
- Spreading costs: on LLM-SQL and Txn Sched Discovery lost; 15% of evals went to directions with no record [c07].
- Multi-agent failure rates 41%-86.7%; 36.9% of failures are inter-agent misalignment [b28, d12]. A sequential single-agent scaffold avoids at most that category, but no single-agent baseline exists in MAST.
- AIRA operators use about 2x the completion tokens of AIDE's [d04].
- Verbalized sampling costs more tokens per call [d07].

### 6.4 What nobody has measured
- Code quota vs free choice at equal tokens.
- Pivot threshold sweep.
- Hard cap vs soft cap vs quota for one agent in sequence.
- Explore-share schedule.
- Whether direction diversity (not text diversity) predicts final score.

## 7. What our agent should take

### Add now (established)

| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| A1 | In open mode, code keeps a history of directions tried (a short label per attempt) and assigns untried directions to attempts. Do not let the model choose "what next" alone. | S3 (already in SCHEMA.md; this confirms it) | [E] | K07, K08, K14; c01, b13, b14, b17, b25, b26, c21 |
| A2 | Any "which direction or peer next" rule runs in code (UCB-like or a quota), not in the model's head or only as a formula in the prompt. | S3, G5 | [E] | K08; b14, b16, b17 |
| A3 | Never show attempts a score-only leader board. If attempts see anything about earlier work, show directions tried and outcomes, not a ranked leader. | S3 | [E] for the leader-board harm; the "directions only" form is [S] | K07; c01, c15, b13 |
| A4 | Do not allocate by pure follow-the-best. Keep non-leader directions alive (soft crowding weight such as score / (1 + attempts in direction)). | S3, S6 | [E] at equal iterations | K20; d01, d02, d06 |
| A5 | Do not count several samples from one model as several directions. Count distinct directions by code (embedding or label); expect about 5% unique without help. | G4, S3 | [E] | K14, K15; b25, b26, c21, c22 |
| A6 | Report coverage and selected accuracy separately for every allocation rule. Selection stays in code. | S3, S7, G5 | [S] for the numbers; the principle is [E] under G5 | K13; b23 |
| A7 | Log per run: directions opened, share of attempts per direction (HHI by thirds of the run), local records, and the share of budget in directions with no record. | Section 6 of SCHEMA (logging) | [E] as method (HHI used by c01) | K07, K09; c01, c05, c07 |
| A8 | Do not adopt debate or model-run Elo tournaments for allocation. | G8, G9 | [E] | K17, K18, K27; d11, c25, b28, b29 |

### Test first

| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| T1 | Code quota or per-direction cap (start at 2) over a free sequence of attempts. | S3 | [S] (plus toy [M]) | K01, K09, K26; c01, c02, d22 |
| T2 | Pivot to a code-chosen untried direction after m fruitless attempts (sweep 1, 2, 3, 5, 8). Both CORAL systems use 5 with no sweep. | S6 | [S] | K19; c13, c06, d23, d03 |
| T3 | Explore share: untried directions first, then exploit the best-so-far (0.33, 0.5, 0.7). | S3, G12 | [S] | K11, K26; c05, d23 |
| T4 | Soft crowding weight vs hard cap vs quota. | S3, S6 | [C] | K20; d02, d06 |
| T5 | Code floor quota on untried directions when the model's own ranking of directions is noisy. | S3, G8 | [S]/[M] | K02, K23, K26; a07, a08, d05, d21 |
| T6 | Strategy-diverse prompts for attempts on tasks with a check (DIV-SE style), selection by code. Tension with G4. | S3 | [C] | K12; b19, d09, d10 |
| T7 | Code novelty filter on proposed directions (embedding similarity above 0.95 rejected). | S3 | [E] in kind, numbers missing | K16, K24; c20, d06 |
| T8 | Verbalized-sampling style proposal (list of directions with probabilities), then code dedupe. | S3 | [E] for creative text; untested for directions | K15, K24; c23, d07, d08 |
| T9 | Scoped memory: only the list of directions tried and their outcomes, vs none, vs full history. | S5, S3 | [C] | K22; d04, c12 |
| T10 | Carry the top-3 candidates to selection instead of one. | S7, G5 | [S] | K23; d05 |
| T11 | A verify step after each allocated attempt. | S4, S8 | [S] | K27; d12 |
| T12 | Hold a share for a mix of explorer and extractor attempts (e.g. 40% explorers), and vary how far an attempt may jump from prior attempts. | S3 | [C] | K03, K04, K25; b05, b06, b04 |
| T13 | Check that the direction-proposal step produces genuinely different attempts before tuning thresholds or caps. | S3 | [S] | K21; d03 |
| T14 | Split a problem into parts only if it looks modular (O3 Decompose); check the split on a held-out part. | O3 | [S] | a19 |

Notes. T1 to T5 are the core S3 test. Evidence for them is one LLM paper plus our toy. The toy predicts that code spread wins when the model's own ranking is weak and loses when it is strong (rho 0.6). Measure rho first.

## 8. Concrete tests on our bench

All tests: both arms use the same token budget (prompt plus completion tokens, including the cost of direction labelling). Report mean and SD over at least 10 seeds (AIRA-dojo shows 3 seeds can reverse rankings [d03]). Use the bench's open-mode items with a code grader, and checked items where a held-out check exists.

| Test | Item type | Arms (equal tokens) | Metric | Expected effect |
|---|---|---|---|---|
| B1 Quota vs free | Open tasks with a code grader; 30 attempts, 10 candidate directions | Free attempts; one-per-direction quota then exploit; cap 2 then exploit | Final best score; distinct directions | Cap 2 above free if rho is weak. Toy says 0.94 vs 0.70 at rho 0; real effect likely smaller. Add if +0.2 SD |
| B2 Rho probe | Same tasks | Ask the model to rank directions before running; compare with realised values | Spearman rho of model ranking vs realised value | If rho < 0.3, code allocation justified; if >= 0.6, free choice may do |
| B3 Pivot sweep | One open task, 10+ seeds | m = 1, 2, 3, 5, 8 | Final score | Flat or best at 2-3 (toy). 5 not expected best |
| B4 Explore share | Same | Explore share 0.33, 0.5, 0.7, 1.0 | Final score; SD across seeds | Peak at 0.5-0.7 (toy); never-exploit worst |
| B5 Crowding weight | Same | Follow-best; soft weight score / (1 + n); hard cap 2 | Final score | Soft or cap beats follow-best (DGM 50.0 vs 39.7) |
| B6 Score-visible vs directions-only | Multi-attempt runs where later attempts see earlier ones | See ranked scores; see directions tried and outcomes only; see nothing | HHI last third; best score | Ranked scores push HHI toward 1; directions-only keeps it lower |
| B7 Distinct-direction yield | Open prompts | Same prompt N times; verbalized sampling; code seed list of directions; seed list plus 0.95 similarity filter | Distinct directions per N (embedding clusters); downstream score | Same prompt about 5% unique; seeds and filter higher |
| B8 Diverse approach prompts | Items with a check (planning, colouring, code with tests) | N same-prompt attempts; N approach-diverse attempts; both selected by code | Selected accuracy and coverage | DIV-SE-style gain on hard planning items; no gain on easy ones. Keep G4 intact |
| B9 Memory scope | Multi-attempt open tasks | No memory; directions-and-outcomes list; full transcript | Final score; HHI | Directions-only matches or beats full transcript (AIDE: no benefit from full memory) |
| B10 Top-3 carry | Items where own score is a proxy | Pick top-1; top-3 to verify | Held-out score | About +10% (AIRA) |
| B11 Noisy-prior robustness | Items with a hidden true yield | Allocation by model self-rating; allocation by code floor quota | Share of optimum | Floor quota stable at 83-91% of optimum; self-rating falls at noise sd 0.25-0.5 (toy) |
| B12 Overhead | Same items | One agent role-playing all directions in sequence; direction board with separate calls | Spec-violation rate; tokens; score | Sequential single agent has fewer coordination failures; compare with MAST categories |

## 9. What does not transfer, and why

- **Credit and priority rules.** Human scientists respond to credit. A single LLM has no career. A code allocation stands in for the credit rule; there is no reason to import the priority rule itself. No LLM study tests a priority or credit rule directly [critique.md]. Coral Discovery's per-direction credit is a bookkeeping device.
- **Many workers.** Kitcher and Weisberg-Muldoon use hundreds of agents. Our agent has one thread of attempts with a small token budget. Saturation curves and cap sizes from 400-agent models will not carry over (a10: gains small beyond 30 controls).
- **Network structure.** Zollman's sparse-network advantage depends on hiding results from neighbours. For one agent, attempts are already isolated in S3. The question becomes what to show, not graph design. Zollman's result is also not robust [a24].
- **Landscapes with free visits and no depletion.** W&M landscapes give perfect knowledge of visited patches and zero cost per visit [a09]. Real attempts cost tokens and are noisy.
- **Hong-Page diversity.** Based on a random-value landscape and heuristics with limited power [a18]. A strong LLM is not a limited-power heuristic. Quality outweighs diversity in the mixture regression [d10].
- **Human field studies.** Rzhetsky et al. is model inference on MEDLINE [d20]. There are no counts of researchers per approach for peptic ulcer or funding portfolios.
- **Four parallel agents with shared state.** Coral Discovery and CORAL run four agents in parallel. A single-agent scaffold gets the direction board but not parallel exploration. Whether the gain survives sequential execution is open. Coral Discovery's own conjecture is that a single agent's whole-history advantage explains its loss on Txn Sched [c07].
- **Persona or strategy voters.** DIV-SE-style diversity conflicts with G4, which bans persona or strategy voters on single-answer problems. Reconciliation: diversity in attempts can help coverage in open or checked tasks, but selection stays in code and agreement is never proof.
- **Model-run Elo selection** (Co-Scientist). G8 forbids model selectors [b29].
- **Prompt-only exploration instructions.** They fail [b14, b17].

## 10. Open questions

1. Does a code-set allocation of untried directions beat the same number of free attempts at equal tokens? No source runs the ablation.
2. What is the best pivot threshold? Both CORAL systems use 5 with no sweep; our toy says 2 under fast improvement and flat under slow.
3. Hard cap, soft weight or quota for a single agent in sequence? DGM's soft weight is untested against a hard cap.
4. How should the explore share shrink over a run? Toy says exploit the last 30%; no real schedule exists.
5. Does the Kitcher result survive noisy LLM self-ratings? Toy says no at log-noise sd 0.25-0.5; there is no real measurement of an LLM's ranking skill rho.
6. Can a single model be made to propose genuinely different directions? Verbalized sampling works for creative text. Seed lists and forced negative prompts have no source. Whether direction diversity predicts final score is untested.
7. Do shared notes help a single agent across its own attempts without causing follower collapse? CORAL and Coral Discovery disagree (K22).
8. What do the full texts of Alexander et al. 2015, Rosenstock et al. 2017, Grim et al. 2019, Fernandez Pinto 2018 and Thompson 2014 say, numerically?
9. Are there human field data with real counts of researchers per approach?
10. How large is the coordination overhead when one agent simulates division of labour in sequence?
11. Is the Coral Discovery gain robust to variance? Best-of-3 on 9 tasks with third-decimal margins is thin.
12. Does model mixing help in open search once quality is held fixed? SYMPHONY says yes for branch variety; Self-MoA says no for aggregation.

## 11. Sources

[V] = opened by the research agents; [M] = abstract, snippet or second-hand only.

Theory and models
- [M] Kitcher (1990) The Division of Cognitive Labor. J Philosophy 87(1):5-22. https://doi.org/10.2307/2026796 [a01]
- [V] Muldoon and Weisberg (2011) Robustness and idealization in models of cognitive labor. https://repository.upenn.edu/bitstreams/97e04188-38b4-4233-b3ba-fde93a48d0c0/download [a02, a06-a08]
- [M] Muldoon and Weisberg (2011), abstract via PhilPapers. https://philpapers.org/rec/RAI [b01]
- [V] Weisberg (2010) New approaches to the division of cognitive labor. https://repository.upenn.edu/philosophy_papers/ [a03]
- [M] Strevens (2003) The Role of the Priority Rule in Science. J Philosophy 100(2):55-79. https://doi.org/10.5840/jphil2003100224 [a04]
- [M] Strevens (2011) Economic approaches to understanding scientific norms. Episteme 8(2). https://doi.org/10.3366/epi.2011.0015 [a05]
- [V] Weisberg and Muldoon (2009) Epistemic landscapes and the division of cognitive labor. https://repository.upenn.edu/philosophy_papers/7 [a09-a13]
- [M] Weisberg and Muldoon 2009 page. https://web.sas.upenn.edu/weisberg/?p=106 [b02, b11, c29]
- [M] Alexander, Himmelreich and Thompson (2015) Philosophy of Science 82(3). https://doi.org/10.1086/681766 [a14, d14]
- [V] Thoma (2015) The epistemic division of labor revisited. https://researchonline.lse.ac.uk/id/eprint/88129/1/Thoma_Division%20of%20Labour_Accepted.pdf [b04-b07]; [M] journal abstract https://doi.org/10.1086/681768 [a15, d16]
- [M] Fernandez Pinto and Fernandez Pinto (2018) Epistemic Landscapes Reloaded. https://catalog.comses.net/publications/234067 [b03]
- [M] Poyhonen (2017) Value of cognitive diversity in science. https://doi.org/10.1007/s11229-016-1147-4 [a16]
- [M] Bedessem (2019) The division of cognitive labor: two missing dimensions. https://doi.org/10.1007/s13194-018-0230-8 [a17]
- [V] Hong and Page (2004) PNAS 101. https://pmc.ncbi.nlm.nih.gov/articles/PMC528939/ [a18]
- [M] Grim et al. (2019) Diversity, ability, and expertise in epistemic communities. https://doi.org/10.1086/701070 [d17]
- [V] Reijula, Kuorikoski and MacLeod (2023) Synthese 201:214. https://link.springer.com/content/pdf/10.1007/s11229-023-04193-4.pdf [a19]
- [V] Wu (2024) Better than Best. https://cambridge.org/core/services/aop-cambridge-core/content/view/1125693C6EFCD39D13E3108840B87305/S0031824823001290a.pdf/better-than-best-epistemic-landscapes-and-diversity-of-practice-in-science.pdf [b08-b10]
- [M] Zollman (2007) https://doi.org/10.1086/525605 [a25]; (2010) https://doi.org/10.1007/s10670-009-9194-6 [a26, b12]; (2013) https://doi.org/10.1111/j.1747-9991.2012.00534.x [a27]
- [M] Rosenstock, Bruner and O'Connor (2017) https://doi.org/10.1086/690717 [a24, d15]
- [V] Wu and O'Connor (2023) https://link.springer.com/content/pdf/10.1007/s11229-023-04037-1.pdf [a22, a23]; [M] abstract https://doi.org/10.1007/s11229-023-04037-1 [d18]
- [V] Smaldino et al. (2024) https://pmc.ncbi.nlm.nih.gov/articles/PMC10913329/ [d19]
- [V] Stanford Encyclopedia, social dimensions of scientific knowledge. https://plato.stanford.edu/entries/scientific-knowledge-social/ [a28, d13]
- [V] Blog summary of Kitcher 1990. https://www.greaterwrong.com/posts/Lr2pF6i3nedL2fsBN/research-motivations-and-the-division-of-cognitive-labor [a29]

Human experiments and field data
- [V] Derex and Boyd (2016) PNAS 113. https://pmc.ncbi.nlm.nih.gov/articles/PMC4801235/ [a20]
- [V] Mason and Watts (2012) PNAS 109. https://pmc.ncbi.nlm.nih.gov/articles/PMC3271930/ [a21]
- [V] Rzhetsky et al. (2015) PNAS 112. https://pmc.ncbi.nlm.nih.gov/articles/PMC4664375/ [d20]
- [M] From Individual to Social Imitation (2026). https://arxiv.org/abs/2609.28675 [c28]

LLM and agent studies
- [V] Ren et al. (2026) Coral Discovery. https://arxiv.org/abs/2610.33281 [c01-c08]
- [V] Qu et al. (2026) CORAL. https://arxiv.org/abs/2604.01658 [c09-c13]
- [V] Liu et al. (2025) ASCollab. https://arxiv.org/abs/2510.08619 [c14-c16]
- [V] Si, Yang and Hashimoto (2024). https://arxiv.org/abs/2409.04109 [b25, c17, c18]
- [V] Novikov et al. (2025) AlphaEvolve. https://arxiv.org/abs/2506.13131 [c19]
- [V] Lange et al. (2025) ShinkaEvolve. https://arxiv.org/abs/2509.19349 [c20, d06]
- [V] Zhang et al. (2025) NoveltyBench. https://arxiv.org/abs/2504.05228 [c21]
- [V] Jiang et al. (2025) Artificial Hivemind. https://arxiv.org/abs/2510.22954 [b26, c22]
- [V] Zhang et al. (2026) Verbalized Sampling. https://arxiv.org/abs/2510.01171 [c23, d07, d08]
- [V] Hegazy (2024). https://arxiv.org/abs/2410.12853 [c24]
- [V] Zhang et al. (2025) Stop Overvaluing Multi-Agent Debate. https://arxiv.org/abs/2502.08788 [c25]
- [V] Gottweis et al. (2025) Co-Scientist. https://arxiv.org/abs/2502.18864 [b29, c26]
- [M] Multi-Agent LLMs Fail to Explore Each Other (NeurIPS 2026). https://neurips.cc/virtual/2026/166881 [c27]
- [V] Choi et al. (2026) Do Multi-Agent LLMs Explore Each Other? https://arxiv.org/pdf/2607.11250 [b13-b16]
- [V] Krishnamurthy et al. (2024) Can LLMs Explore In-Context? https://arxiv.org/pdf/2403.15371 [b17, b18]
- [V] Wang et al. (2024) DIV-SE. https://arxiv.org/pdf/2310.07088 [b19, b20]
- [V] Wang et al. (2024) Mixture-of-Agents. https://arxiv.org/pdf/2406.04692 [b21, b22]
- [V] Brown et al. (2024) Large Language Monkeys. https://arxiv.org/pdf/2407.21787 [b23]
- [M] Li et al. (2024) More Agents Is All You Need. https://arxiv.org/pdf/2402.05120 [b24]
- [V] Liang et al. (2024) Multi-Agent Debate for divergent thinking. https://arxiv.org/pdf/2305.19118 [b27]
- [V] Cemri et al. (2025) MAST. https://arxiv.org/pdf/2503.13657 [b28, d12]
- [V] Zhu et al. (2026) SYMPHONY. https://arxiv.org/pdf/2601.22623 [b30, b31]
- [V] Zhang et al. (2026) Darwin Godel Machine. https://arxiv.org/abs/2505.22954 [d01, d02]
- [V] Toledo et al. (2025) AIRA-dojo. https://arxiv.org/abs/2507.02554 [d03-d05]
- [V] Li et al. (2025) Rethinking Mixture-of-Agents. https://arxiv.org/abs/2502.00674 [d09, d10]
- [V] Smit et al. (2024) Should we be going MAD? https://arxiv.org/abs/2311.17371 [d11]

Our own models (not literature)
- D:/research_scratch/F03.05/tmp/F03.05_kitcher_sim2.py [d21]; F03.05_seq_sim.py [d22, d23]

## Source audit (2026-11-01)

Fresh auditors re-opened the sources of 7 established claims: 4 confirmed as written, 3 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **F03.05-K08** (reworded: the sources support less). Numbers match, but 'removes in-context exploration failure' generalises from one Qwen-7B two-armed setup (pA=0.6 vs 0.4, a single table) to exploration failure in general; the lock-in rate was 0.0% only for that setup. Corrected claim: Supplying the allocation from code removed inferior-peer lock-in in one Qwen-7B two-armed delegation test: 50.0% prompt-only, 23.3% with the UCB formula in the prompt, 0.0% with an external UCB calculator, 0.0% with algorithmic UCB; separately, GPT-4 with a basic prompt showed suffix failure (best arm never chosen again) in more than 60% of replicates in a multi-armed bandit test, and only one GPT-4 configuration (with hint, chain-of-thought and externally summarised statistics) explored well.
- **F03.05-K15** (now contested: a source does not say this). NoveltyBench says in-context regeneration is the most successful approach, roughly matching human-writer diversity (3 models tested) and GPT-4o and Gemini 2.0 Pro even surpass humans in cumulative utility; so 'does not reach humans' is contradicted. Also 66.8% is the share of base-model diversity VS retains after the DPO stage in a creative-writing ablation (direct prompting retains 23.8%).
- **F03.05-K16** (now single-source: the sources are not independent). Only ShinkaEvolve ablates novelty rejection, weighted parent sampling and bandit ensembles (on circle packing); AlphaEvolve's ablations cover evolution, prompt context, meta-prompt, model size and full-file evolution, not these three, so there is one system, not several.
