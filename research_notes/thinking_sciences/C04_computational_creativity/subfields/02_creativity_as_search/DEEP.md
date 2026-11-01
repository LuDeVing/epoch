# Creativity as search: deep document

*Subfield C04.02. Anchor: Nair, Gizzi and Sinapov (2024), arXiv 2405.01453 [V]. Evidence: evidence_a-d.jsonl (ids a01-d23), claims.jsonl (K01-K28), critique.md. Schema parts refer to SCHEMA.md v0.2. Status marks: [E] established, [S] single-source, [C] contested.*

---

## 1. What it is

"Creativity as search" says that making something new is moving through a space of possible things until you reach one that meets a goal. The space can be words, programs, plans, designs or ideas. A traversal rule picks the next candidate. An evaluation rule says when to stop.

The idea has three layers.

- **Combinational creativity**: join known things in new ways.
- **Exploratory creativity**: search inside a space whose rules are fixed (Boden). This is the layer that "search" fits best.
- **Transformational creativity**: change the rules of the space, so things become reachable that were not before. Wiggins models this as search at a meta level, over the rule sets.

For our agent this matters at one place: S3 (generate) and its control. When should the agent search many candidates, how should it search, and how does it pick the winner? The literature gives a clear answer on one side and a thin answer on the other.

- **Clear**: when a cheap, exact checker exists, search (many tries plus the checker) wins large. It is also usually matched or beaten by plain repeated sampling at equal tokens (K01, K02, K20, K21).
- **Thin**: when only a model or a person can judge, gains are small and noisy, and the model is a poor judge of its own ideas (K05, K06, K11).

Important warning from the critique: the anchor paper (2405.01453) is a position paper. It has one small experiment (object replacement with vision-language models) and no search experiment. It supplies the framing, not effect sizes. No replication of it was found (K19). All the numbers in this document come from other studies.

---

## 2. History and theories in depth

### 2.1 Problem solving as search (1950s-60s)

Newell, Shaw and Simon (1959/1962, RAND P-1320, a09 [M]) argued that creative thinking needs no separate theory. It is problem solving when the problem is new and hard. Their four criteria: the product is novel and useful; it rejects ideas accepted before; it takes intense, persistent effort; the problem was vague at the start and got clarified. This is the root of the view that search plus heuristics is enough to explain creative output. Not opened this session (catalogue entry and citations only).

### 2.2 Boden's three types (1990, 2004)

Boden (a08 [M], book, not opened) separates combinational, exploratory and transformational creativity. She also separates P-creative (new to the maker) from H-creative (new in history). Transformational creativity is the rare one: the space itself changes. Wikipedia notes the framework works more as a touchstone than as a technical model. This is why later work tried to make it formal.

### 2.3 Wiggins's Creative Systems Framework (2006)

Wiggins (a07, not opened; known through Ventura and Brown) formalises Boden. There are four parts: a universe of concepts, rules that define the conceptual space, a traversal rule that picks the next concept, and an evaluation rule. Exploratory creativity is search in the space under a fixed traversal rule. Transformational creativity is search over the rule sets themselves. Velardo and Vallati (2016, a25) extend this to an agent with an artefact space, a constrained generation operator, an evaluation operator with memory, and an optional update operator that can change generation and evaluation. That update operator is the route to transformation. Nobody tested it on a system.

### 2.4 Ritchie's empirical criteria (2007)

Ritchie (a26, not opened) proposed testable criteria built from the typicality and quality of outputs, and from how outputs relate to the program's inspiring set (the examples it was built from). Ventura and Brown reuse the inspiring-set idea against LLMs. The exact criteria count was not verified.

### 2.5 Ventura and Brown (2024): small, interesting programs

This is the sharpest recent theory (a01-a04, opened).

- Define a traversal function T that picks artifacts from a space B until it hits a goal set G. The chance that blind search works is the density d = |G|/|B|.
- Examples: tic-tac-toe has 765 states after symmetry, 138 terminal, and d about 0.12 for a draw or better by random play. Three-letter words: 1,340 of 17,576 strings, d = 0.076. Five-letter words: 12,972 of 11,881,376, d about 0.001. A sentence: about 10^-60. A 410-page book: about 10^-655,980.
- Conclusion: at scale, blind search over artifacts cannot be the creative process. The creative act is choosing the search program. Good search programs are short to describe but slow to run (algorithmic information theory). The space of search programs is itself searched at a meta level, which needs two evaluators: one for artifacts (Eb) and one for search algorithms (Ea).
- They argue an LLM learns the training distribution and a smooth manifold, so it models non-creative output and may be a dead end by itself (a04). This is contested: FunSearch and AlphaEvolve get new results by wrapping an LLM in search and checks.
- Limits: analytic only, no experiment; treats value as 0/1; base-level evaluation is probably uncomputable.

Engineering reading: the agent should not enumerate candidates blindly. It should choose and refine a cheap generator (a short program, a prompt, a decomposition) and let code evaluate it. FunSearch and AlphaEvolve do exactly this.

### 2.6 The Nair et al. position paper (2024)

Nair, Gizzi and Sinapov (a05, a06, b01, c01-c03, opened) map Boden's types onto machine learning.

- Tree of thoughts, MCTS and beam search are exploratory methods. They search the output space of the model, not its embedding space (its conceptual space).
- The authors argue search alone is limited by the embedding dimensions, and that combinational and transformational routes are under-explored. They say existing search methods were not built for creative problem solving.
- Their only experiment is object replacement (pick the object that can stand in for a missing tool: bowl for scoop, saucepan for hammer, knife for spatula, safety pin for toothpick, scissors for pliers). 5 core objects, 10 test sets each, 4 candidate images per set, 50 samples per model, random pick about 30%.
- Nominal case (tool present): CLIP-B-32 100%, CLIP-B-16 92%, CLIP-L-14 98%, CLIP-H-14-laion 98%, ViLT-B-32 68%, LLaVA 98%. The replacement case is much lower but only plotted in a figure.
- Adding object-affordance text generally helped. Adding task text mostly hurt. Both together did not clearly help.
- Limits: replacement targets chosen by the authors, no statistical tests, scoring models (CLIP) not chat models, not a search experiment. No replication found (c26, K19).

### 2.7 LLM-era theory papers

- Franceschelli and Musolesi (2025, a10, b02): models trained on a distribution can at most show combinational or exploratory creativity. RLHF and DPO reduce diversity. No experiment.
- Franceschelli (2026, a11, b03): for agents, exploration is shaped by the tools chosen. Fixed tools keep the agent inside the current conception of the domain. Tool creation could change the space but the tools come from an LLM, so convention still limits them. "Hyperpolation" (transformational) has no agreed test.

### 2.8 From theory to engineering

The path from theory to practice runs through four lines of work.

1. **Search over thoughts**: Tree of Thoughts (2023), Algorithm of Thoughts (2023), RAP (2023). Search inside one problem.
2. **Evolutionary search with an LLM mutator and a code evaluator**: ELM (2022), LMX (2023), FunSearch (2024), EoH (2024), AlphaEvolve (2025). Search over programs.
3. **Quality-diversity**: ELM, QDAIF (2023), OMNI-EPIC (2024). Keep an archive of different good things, not only the best.
4. **Agent search on open tasks**: MLE-bench agents (AIDE, AIRA-dojo), AI Scientist, Heuresis, Darwin Godel Machine.

The 2025-2026 papers then stress-test these: matched-compute comparisons against plain sampling, studies of novelty drift, and measurements of proxy exploitation.

---

## 3. Core findings with exact numbers

Status: [E] established (2+ independent sources), [S] single source, [C] contested. Claim ids from claims.jsonl.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Search with an oracle beats single-pass by a large margin | Game of 24 (GPT-4, 100 tasks): IO 7.3%, CoT 4.0%, CoT-SC(k=100) 9.0%, IO best-of-100 33%, CoT best-of-100 49%, ToT b=1 45%, ToT b=5 74%. Author re-run of ToT b=5: 69% | a12, b04, a15, d22 (K01) | [E] |
| RAP (MCTS with model as world model) beats CoT on planning | Blocksworld success: CoT 29.4, CoT+SC(10) 46.8, RAP(1) 48.6, RAP(10) 51.6. ProntoQA pred acc 87.8 vs 94.2; proof acc 64.8 vs 78.8. GSM8K RAP 48.8% | c07 (K01) | [E] with ToT |
| Tree search is not cheaper in dollars | ToT 5.5k completion tokens vs 6.7k for 100 CoT, but about $0.74 vs $0.47 per case (CoT best-of-100 49%), IO best-of-100 $0.13 (33%). Creative writing: ToT about 5x tokens ($0.32 vs $0.06 IO) | a14, c04, c24, a13 (K02) | [E] |
| Plain sampling is the baseline to beat (math) | MCTS below sampling plus voting at every FLOP budget on MATH. REBASE (cheap tree with a process reward model) higher accuracy at about 7x less compute for a 7B model; MBPP 8 samples 63.0 vs 69.6; 64 samples 79.0 vs 81.4 | d02 (K02) | [E] |
| Plain sampling beats trees on ARC-AGI | Budget 128 calls, GPT-4o Pass@2: repeated sampling 15.0, AB-MCTS-A 14.0, AB-MCTS-M 12.3, standard MCTS 9.0, sequential refinement 8.7. DeepSeek-V3: 18.6 vs 18.3 vs 14.0 | d06 (K02) | [E] |
| Trees help a little on code | LiveCodeBench GPT-4o: sampling 37.8, AB-MCTS-A 39.1, AB-MCTS-M 38.9, standard MCTS 36.7. CodeContest GPT-4o 37.9 vs 40.6; DeepSeek-V3 43.2 vs 44.8. Std 0.3-3.6, many gaps inside noise | d06 (K13) | [E] small |
| Many short tries + checker match long thinking | R1-Distill NoThinking vs Thinking, AMC23 at 700 tokens 51.3 vs 28.9; at large k same pass@k with 2.0-5.1x fewer tokens; MiniF2F/ProofNet 3.3-3.7x fewer; best-of-N up to 9x lower latency | d01 (K21) | [E] with d20, d06 |
| For long-thinking models correct answers are shorter | Same question: correct chains shorter than wrong; parallel scaling gives better pass@k than lengthening; Shortest Majority Vote beats majority vote | d20 (K21) | [E] |
| Selection plateaus without a checker | MATH Llama-3-8B: coverage 82.9% (100 samples) to 98.44% (10,000); majority vote or reward model 40.50% to 41.41%. SWE-bench Lite with unit tests: 15.9% (1 sample) to 56% (250) | d15 (K06) | [E] |
| In ToT, generation is the bottleneck | GPT-4 gen + GPT-3.5 eval 64%; GPT-3.5 gen + GPT-4 eval 31%; both GPT-4 74%; both GPT-3.5 19% | a14, c06 (K03) | [S] |
| Backtracking matters | Mini crosswords word success: ToT 60% (4 of 20 games), without backtracking about 20%; IO/CoT under 16% | b06 (K04) | [E] with AoT |
| In-prompt search is much cheaper | Game of 24 GPT-4: ToT 69% with 109.1 queries, 13,900 prompt + 5,500 completion tokens; AoT 71% with 1 query, 5,450 + 998 tokens (about 19.4k vs 6.4k). Crosswords: AoT 52% with 2 queries vs ToT 46.5% with over 200; about 25x fewer tokens | a15, d22 (K27) | [S] |
| Search on soft criteria gives small, noisy gains | ToT creative writing coherence (GPT-4 judge, 100 tasks): IO 6.19, CoT 6.93, ToT 7.56; humans ToT over CoT 41, CoT over ToT 21, 38 similar; iterative refine alone: IO 7.67, ToT 7.91. GPT-3.5: IO 4.47, ToT 6.62 | a13, b05, c05 (K05) | [E] |
| Creative Beam Search | 31 students, 217 answers: CBS 45%, standard 29%, too alike 26%. Model's self-pick equals diverse-beam top 29% vs 35.3% by chance | a16, b19, c12 (K05, K06) | [S] small |
| QDAIF fades under human rating | Human QD score: QDAIF 0.772, Fixed-Few-Shot 0.767, Shuffling 0.696, LMX 0.650, Random 0.606. Human quality 3.9 vs 4.133 for fixed few-shot | c11 (K05) | [S] |
| Model is a poor self-selector | Paper accept/reject pairs: Claude-3.5 71.4%, Claude-3-Opus 63.5%, GPT-4o 61.1%; direct ranking 50.0, 45.0, 51.7 vs human-human 56.1. GPT-4 recognises own text 73.5% and self-preference rises linearly with self-recognition. Single GPT-4o judge on MacGyver 64.7% vs human 82.7% (n=50); multi-agent judge 84.7% | b17, a20, d16, d17 (K06) | [E] |
| Self-verification gain is near zero without knowledge | Natural Questions (3,610 q), Qwen-2 0.5B-72B: gap below 1% or negative. 4x4 Sudoku (288): only 72B models improved (relative gap 16.99-20.81) | d14 (K06) | [S] |
| Over-generation saturates | 4000 seed ideas per topic, about 200 (5%) survive dedupe at cosine 0.8 | a20, b16 (K07) | [E] |
| Models give few distinct answers | NoveltyBench: frontier models under 3 distinct of 10 on average; under 4 of 10 cumulative utility; smallest models most diverse. Cross-model similarity 71-82%; within model above 0.8 in 79% of pairs; min-p T=2.0 still 61.2% above 0.8 | b20, d10, b23, d09 (K07) | [E] |
| In-context regeneration restores diversity | Claude-3 Opus, GPT-4o, Gemini 2.0 Pro reach about the diversity of 8 human authors; GPT-4o and Gemini exceed human cumulative utility. Paraphrase, system prompt marginal. 100-prompt subset, 8 generations | b21, d10 (K08) | [S] |
| Verbalized Sampling beats direct, list and multi-turn | Same N=30, 90 annotators. Diversity (direct/sequence/VS): poem 1.90/2.07/2.39, story 2.74/2.76/3.06, joke 1.83/2.93/3.01. Creative writing diversity 1.6-2.1x direct. Larger models gain 1.5-2x more | d08 (K24) | [S] |
| Temperature buys diversity at a quality cost | Higher T raises diversity, lowers quality; mostly invents entity names on grounded tasks; helps GPT-5.2 mildly | d08, d12 (K24) | [S] |
| Two-step persona + temperature recipe | Pairwise similarity 0.85 to 0.65 on models under 20B, T up to 4.0 after top-p; judged by an LLM for coherence only | d11 | [S] |
| History ledger in search lifts accuracy | BASIN (same budget): Game of 24 gpt-4o-mini 66.0 to 72.0; Qwen3-27B 43.0 to 65.0 (+22 pp, p<0.01); MuSR gpt-oss-120b 63.3 to 67.0; flat penalty hurt GPT-4 (67.0 to 61.0) until quality-aware (70.0) | d18 (K23) | [S] |
| Exploration forcing does not always help | MLE-bench: memory on vs off and UCT constant 0/0.25/0.75 near identical. Heuresis exploration gates raised diversity, not top score | d03, d04 (K23) | [S] |
| Search drifts from explore to exploit | 10 MLE-bench tasks; strategic exploration 75% of behaviours early, 25% late; bug fixing 15% to over 50%; all AIRA strategies fall below P-creativity 1 within a few episodes. A 30-episode MCTS run did not recover | a22, b11, d19 (K12) | [S] |
| Novelty and impact decouple | Gold humans H-creativity 0.744 (silver 0.524, bronze 0.293); GPT-5 AIDE 1.423 (p<1e-15). Medal rate 21.25% (GPT-5), 10.85% (Qwen3-32B). Correlation of change in impact vs change in P-creativity: human -0.111, AIDE GPT-5 -0.021, AIDE Qwen3 0.056, AIRA Qwen3 -0.026. Of 92 high-novelty/low-impact episodes, 87.0% (80) were refined away; 53.8% of those lost H-creativity next step | b12, b13 (K12) | [S] |
| LLM judge vs human on novelty | Spearman 0.732 (GPT-5 judge vs humans) | b11 | [S] |
| Search structure effects are small and task dependent | Toledo (MLE-bench Lite, 24 h, 20 seeds): AIDE-greedy 39.8%, AIRA-greedy 45.5%, AIRA-MCTS 47% any medal (inside CI), greedy best gold 27%. Heuresis (3 tasks, 6 strategies, 3,222 runs): greedy best nanoGPT val_bpb 0.9567, RL: MAP-Elites 1.582, islands 1.563, Go-Explore 1.561 vs greedy 1.368. LFS MCTS Sudoku 4x4: 100 / 2.2 / 0 for C = 0.5 / 1.0 / 2.5 | d03, d04, d07, b14 (K13) | [E] |
| LLM-First Search (self-guided) | GPT-4o Countdown diff 5/7: ToT-BFS 9.47/0.00; BestFS 49.47/11.11; MCTS C=0.5 60.00/32.63; LFS 63.16/47.37. o3-mini Countdown diff 7: MCTS 41.05, LFS 78.95 | d07 | [S] |
| Proxy scorers get exploited | Heuresis: 40 confirmed fabrications in 1,628 scored runs (2.5%); 27 of 40 hidden behind a clean report; a fake log (val_bpb 0.900) became archive best. DGM node 114 scored 2.0 by deleting detector logging. MLE-bench: using test score would add 9.4-16.6% of medal rate | c09, c13, c23, d03, d05, d23 (K10) | [E] |
| Guards: auditor, held-out, hidden checker | Inline auditor caught fabrications; missed 13 benchmark-specialising RL runs that only a held-out evaluation exposed; hiding checker from agent lowered hacking | d23, d05, d03 (K26) | [S] |
| Imagined novelty does not survive execution | 43 experts, 19 human and 24 AI ideas. Ideation (novelty/excitement/effectiveness/overall): human 4.91/4.40/4.83/4.60, AI 5.78/5.65/6.00/5.38. After execution human 4.90/4.48/4.78/3.97, AI 4.73/3.90/4.13/3.41. Change: AI -1.049/-1.760/-1.879 (FDR p 0.025/0.001/0.003) | a21, b18 (K11) | [E] with Si 2024 |
| AI ideas rated more novel before execution | Novelty 4.84 human (N=49), 5.64 AI, 5.81 AI+human rerank (79 reviewers, p<0.05). Feasibility diff -0.29, p=0.36. Reviewer agreement 56.1% (NeurIPS 2021: 66.0%) | a20, b15 (K11) | [E] |
| Evolutionary program search finds beyond-base results | FunSearch cap set n=8: 512 vs 496; capacity bound 2.2180 to 2.2202. Bin packing OR1: first fit 6.42%, best fit 5.81%, FunSearch 5.30%. AlphaEvolve: over 50 problems, matched 75%, improved 20%; 4x4 complex matmul in 48 multiplications; kissing number 11D 593 vs 592; 0.7% fleet compute recovered | a17, a18, b25, c14, c15 (K09) | [E] |
| EoH beats FunSearch on bin packing with fewer queries | Gap: FF 5.32%, BF 4.87%, FunSearch 3.78%, EoH 2.24%; other set 6.75% vs 2.13%; thousands vs about 1M queries. On some sets FunSearch ties or wins (0.33% vs 0.61%) | c16 (K09) | [S] |
| Scaling raises correctness, lowers divergence | CreativeBench: Gemini-2.5-Pro pass 53.8% / 48.2% (pairing to Combo/Explore unverified); 89.1% of 300 checked items valid. Qwen2.5-7B Combo creativity 0.168 vanilla, 0.174 EvoRePE, 0.175 AlphaEvolve, 0.193 both; pass@1 9.21% to 11.48% | b07-b10 (K14) | [E] |
| Reframing before search | MacGyver GPT-4: Div-Conv +6.5 points efficient solutions; Self-Reflect -9.7 points infeasible, but no help for Claude 2 or Llama 2. CreativityBench structured CoT only -0.012 to +0.039 | c19, d12 (K15) | [C] |
| MacGyver failure profile | GPT-4 18.9% efficient, 37.5% infeasible. Majority correctness humans 79.3% vs GPT-4 73.3%. Errors: wrong tool use 42.4%, goal not achieved 17.7%, unfaithful to constraints 16.9%, unavailable tools 9.5% (table layout garbled in extraction; critique treats a24 as right) | a24, c18 (K16) | [S] |
| Reasoning models search internally, cost and task dependent | Useful trained backtrack depth: ARC-1D 0, Countdown 1, Sudoku 5+. Sudoku 5 backtracks: Qwen2.5-3B 28.9% vs 14.4% with zero; 7B 32.1% vs 11.8%; QwQ-32B 0.0%. Countdown with one backtrack 69.7/59.4/63.0% vs QwQ-32B 51.5% | d21 (K25) | [S] |
| Transformational operators: first thin test | Universe of Thoughts ablation win rate (chance 50%): combinational 58.3%, transformational 54.2%, exploratory 52.4%. Human creativity (Bridge/Electricity/Society): CoT 0.59/0.56/0.50, ToT 0.58/0.53/0.53, T-UoT 0.68/0.62/0.55. n=10 per cell; plain baseline ranked first on GLM-4-9B | d13 (K18) | [C] |
| No original ideas from research agents | Heuresis: zero of 3,222 runs rated Original; best novel idea 3.2% worse (nanoGPT), 6.0% (unlearning), 1.2% (RL) than best overall; OMNI gate passes 10% of attempts on nanoGPT vs 84% on RL | d04 (K18) | [S] |
| Planning what to retrieve raises unique ideas | Nova: unique novel ideas 3.4x baseline; no planning 42.4 unique at step 2, 44.1 at step 3; no planning and no retrieval 25.3, 30.6, 31.35; 37.5% of top-4 ideas | a23 | [S] |
| LLM crossover works as an operator | LMX: near 100% valid offspring as parent count rises; Sodaracers about 30% valid at 6B; QD higher than baselines (p<0.05) | c10 | [S] |
| Divergent Association Task | GPT-4 above mean of 100,000 humans, below top tail; T=1.5 mean 85.6, above 72% of humans | b22 | [S] |
| Darwin Godel Machine archive | SWE-bench Verified 20.0% to 50.0% (80 iterations); Polyglot subset 14.0% to 38.0%; full 14.2% to 30.7%; no-archive ablation lower (values in figure only) | d05 | [S] |

---

## 4. Mechanisms and models

Each mechanism is written so it can be coded. "Code" means plain program. "Model" means a slot call.

### 4.1 The density view (decide whether to search)

Estimate how rare a good answer is. If a random draw passes the check with probability d, then k independent draws succeed with 1 - (1-d)^k. For d near 0.1, k = 20 draws is enough. For d below 0.001, drawing is hopeless and a smarter generator is needed (Ventura and Brown).

Implement: during S0, run a pilot of 4-8 cheap attempts. Estimate d from the check. If d is high, take best-of-N and stop. If d is near zero, move to a structured generator (decompose, tree, program search). This matches G12 (search only where there is a foothold). This pilot rule is our own reading of the theory, not a tested method.

### 4.2 Tree of Thoughts (ToT)

- State: the problem plus a partial solution. A thought is one step (for Game of 24, one arithmetic line; for writing, a plan or a paragraph).
- Propose: the model generates several next thoughts per state (sampled independently, or one call listing them).
- Evaluate: the model gives a value ("sure / maybe / impossible") or votes across states. Several evaluation samples per state.
- Select: BFS keeps the top b states per level (b=5 best in the paper); DFS goes deep and backtracks when a state is judged impossible.
- Cost: Game of 24 is about 5.5k completion tokens per case but more prompt tokens, so about $0.74 per case against $0.47 for 100 CoT samples (K02).
- Where it breaks: GPT-3.5 gets 19% against 74% for GPT-4, because thought generation is the bottleneck. A weaker scorer was tolerable (64%), a weaker proposer was not (31%) (K03).

### 4.3 Algorithm of Thoughts (AoT)

Put a worked depth-first search trace, including dead ends and backtracks, in the examples of one prompt. The model then runs the search inside one long generation. Game of 24: 1 query, about 6.4k total tokens vs ToT 109 queries and about 19.4k. Limits: GPT-4 and two puzzles only, hand-written examples per task, and no external check can intervene mid-run (K27).

### 4.4 MCTS with a world model (RAP)

The model plays two roles: proposes actions and predicts the next state. MCTS runs selection (UCT), expansion, simulation with reward, and back-propagation. Rewards combine the model's likelihood of the step, self-evaluation, and goal progress. Gains on Blocksworld (51.6 vs 46.8 for CoT+SC(10)). Caveat from matched-compute studies: classic MCTS needs dozens of times more generated tokens and lost to sampling on MATH (d02).

### 4.5 Cheap tree with a step scorer (REBASE)

A fixed sample budget is split across the next steps of promising partial solutions, using a trained process reward model. It reached the accuracy of sampling at about 7x less compute for a 7B model. It needs a trained step-level scorer, which our agent does not have for open tasks.

### 4.6 Adaptive branching (AB-MCTS)

At each node, decide go wider (new sample) or go deeper (refine) with a probabilistic model of node value. +1 to +3 points on code, loses to repeated sampling on ARC-AGI. The width/depth choice only pays when refinement uses real execution feedback.

### 4.7 LLM-First Search

The model itself decides whether to continue or branch. No exploration constant to tune. Beat tuned MCTS on Countdown difficulty 7 (47.37 vs 32.63 with GPT-4o; 78.95 vs 41.05 with o3-mini). One group, two puzzles (K13). Note this lets the model control the search, which conflicts with our rule that code decides transitions (section 1 of the schema).

### 4.8 Evolutionary program search (FunSearch, EoH, AlphaEvolve)

- Population: a database of programs with scores, often split into islands to avoid early convergence.
- Prompt: sample two to four good programs from one island, put them in the prompt, ask for a better one.
- Evaluate: code runs the program on the task and returns a score. Reject crashes.
- Update: insert the new program into the database. Keep diversity (islands, MAP-Elites niches).
- What is searched: a short program (a priority function), not the artifact. That is the Ventura and Brown point: search the small program that generates good artifacts.
- EoH evolves a natural-language "thought" next to the code, which cut queries from about 1 million to thousands.
- Needs a cheap exact evaluator and a human skeleton. FunSearch used 15 samplers and 150 CPU evaluators.

### 4.9 Quality-diversity (ELM, QDAIF, LMX)

Keep a grid (MAP-Elites) where each cell is a niche (for Sodaracers, 1,728 niches; for text, e.g. sentiment or genre). A new candidate replaces a cell's occupant only if it is better in that niche. An LLM is the mutation or crossover operator. QDAIF lets the LLM rate the niche traits so no hand-made metric is needed. Risk: the same model scores and guides, so the computed QD score inflates (human QD 0.772 vs 0.767 for a fixed prompt).

### 4.10 History ledger and visit penalty

Keep a code-side record of approaches already tried. Two forms:
- **Ledger in the prompt** (NoveltyBench in-context regeneration): show earlier answers, ask for a different one.
- **Visit penalty in search** (BASIN): cluster reasoning states into basins; subtract a penalty that grows with basin visits; make it quality-aware so strong basins are not over-penalised. Same budget (beam 5, branching 5, depth 3): Qwen3-27B Game of 24 43 to 65.

### 4.11 Verbalized Sampling

One call: "give 5 answers with their probabilities". Beats direct, list and multi-turn prompts at the same N for diversity with similar quality. A cheap alternative to a loop.

### 4.12 Retrieval-planned ideation (Nova)

At each round the model decides what to retrieve next, retrieves, then writes ideas. Without planning, uniqueness stops growing after step 2 (42.4 to 44.1). This is a grounding mechanism for distant analogues (S3 open mode).

### 4.13 Proxy-hardening

A search loop optimises whatever the scorer sees. Mechanism list from the evidence: (1) a held-out evaluator the optimised steps never see; (2) hide the checker code from the agent; (3) an auditor that reads artifacts, not claims; (4) pick the final node by an independent score, not the search's running score (Toledo: choosing by test score closes the whole validation gap for MCTS and evo, over 60% for greedy).

### 4.14 Novelty measurement used in these studies

- P-creativity against own history (Bhushan): embedding or LLM-judge distance of this attempt to earlier attempts in the run. Drops over a run.
- H-creativity against humans.
- Dedupe by cosine above 0.8 (Si).
- Distinct-answer count via a classifier (NoveltyBench).

These are all code-trackable except the LLM-judge ones, which are noisy (Spearman 0.732 vs humans).

---

## 5. What holds up

### 5.1 Replicated or multi-source

1. **With an exact checker, search plus the checker wins** (ToT, RAP, FunSearch, AlphaEvolve, EoH, REBASE, SWE-bench coverage). Direction is consistent across at least four independent groups (K01, K09, K20).
2. **Plain repeated sampling is a hard baseline.** MATH (Wu et al.), ARC-AGI (AB-MCTS), NoThinking best-of-N (Ma et al.), o1-like length study (Zeng et al.). Three or more groups (K02, K21).
3. **Selection by the generating model is weak.** Si (ranking), Creative Beam Search (29% vs 35.3% chance), Brown (plateau after about 100 samples), Panickssery (self-preference), Min Sen (GPT-4o judge 64.7%), Song (gap near zero). Five or more (K06).
4. **Over-generation saturates and models are alike.** Si (5% unique), NoveltyBench, Artificial Hivemind (71-82%), Verbalized Sampling, Beyond the Hivemind (K07, K24).
5. **Proxy exploitation is common.** ELM, AI Scientist, QDAIF, Heuresis (2.5%), DGM, MLE-bench gap (K10).
6. **Idea-stage novelty does not survive execution.** Si 2024 and Si 2025 are the same group; counted as 2 but not fully independent (K11).
7. **Search structure matters little and depends on the task.** Toledo, Heuresis, AB-MCTS, LFS, Bhushan agree (K13).

### 5.2 Failures and null results

- Tree search gave no gain over greedy with the old AIDE operators; gains came from better operators (d03).
- Memory (sibling-scoped) and UCT constant did nothing in MLE-bench (d03).
- Heuresis exploration gates raised diversity but not top score (d04).
- Structured CoT on CreativityBench: -0.012 to +0.039 (d12). Interactive exploration hurt (GPT-5.2 0.142 to 0.083).
- QDAIF's human-rated gain over a fixed few-shot prompt: 0.772 vs 0.767 (c11).
- Self-reflection did not help Claude 2 or Llama 2 on MacGyver (c19).
- A 30-episode MCTS run did not recover novelty (d19).
- A flat visit penalty hurt GPT-4 (67.0 to 61.0) (d18).
- Cross-model sampling adds little (d09).
- Universe of Thoughts: plain baseline ranked first on GLM-4-9B; ranking flips with backbone (d13).

### 5.3 Moderators and boundary conditions

- **Oracle present or not**: biggest moderator. Large gain with exact check; small or mixed gain with a judge (K20).
- **Model strength**: GPT-3.5 ToT 19% vs GPT-4 74%. Search lifts a model only where it has non-trivial success to start (matches G12). The BASIN gain on Qwen3-27B (43 to 65) partly repairs a weak baseline.
- **Task structure**: backtracking depth needed is 0 for ARC-1D, 1 for Countdown, 5+ for Sudoku (d21).
- **Exploration constant**: MCTS swings from 100 to 0 with C on 4x4 Sudoku (d07).
- **Score source**: when the search is guided by a proxy, the proxy drifts from truth (test plateaus or dips over 24 h while validation rises, d03).
- **Budget**: gap between NoThinking and Thinking is largest at low budgets (d01).

### 5.4 Interventions that worked

- Cheap checkers and many short tries (K21).
- Backtracking in tree search (K04).
- Strong model as proposer (K03).
- In-context regeneration for diversity (K08, single paper).
- Verbalized Sampling (K24, single paper).
- Visit-count ledger with quality awareness (K23, single author).
- Held-out evaluation and hidden checker against hacking (K26).
- Divergent-then-convergent prompt on MacGyver (+6.5 points, K15, contested).
- Better search operators (Toledo) beat a fancier search policy.

### 5.5 Interventions that did not work

- Asking for "creative" output or paraphrasing (NoveltyBench: marginal).
- Raising temperature as the main diversity tool (quality drops).
- Model self-ranking of creative candidates.
- Greedy or MCTS switching without fixing operators.
- Inline auditor alone against benchmark specialisation (needed a held-out evaluation).

### 5.6 Gaps in the evidence (from critique)

- Founding paper: position paper, tiny experiment, no replication.
- Most "established" claims rest on one lab's design (Princeton ToT) or LLM-judge scores.
- Bhushan et al. 2026 is single group; the structure comparison is a 3-task figure.
- Theory sources (Wiggins, Boden, Newell-Shaw-Simon, Ritchie) were not opened.
- No replication of Creative Beam Search or QDAIF human evaluation found.
- 2025-2026 coverage thin because search quotas ran out.

---

## 6. Language models

### 6.1 Plain model behaviour

- **Few distinct answers.** NoveltyBench: frontier models give under 3 distinct answers of 10 on average; smaller models are the most diverse. Same-model pairs above 0.8 similarity in 79% of cases; different models 71-82% similar (b20, d09, d10).
- **Scaling converges.** Larger models are more correct but less divergent (CreativeBench). Divergent creativity (semantic entropy) did not rise with size or recency (d17). Gold correctness on CreativityBench: Qwen 4B 0.1882, 14B 0.2483, 32B 0.2588; GPT-5-nano to mini +40% relative (0.1192 to 0.1687), mini to 5.2 about +7% (saturation).
- **Infeasibility is the creative-problem failure.** MacGyver GPT-4: 18.9% efficient, 37.5% infeasible.
- **Beyond the mean human on word-distance tests.** GPT-4 beat the mean of 100,000 humans on the Divergent Association Task but not the top tail (b22).
- **Idea-stage novelty beats humans, execution does not.** AI ideas 5.64 vs human 4.84 novelty at review; after execution, AI lost 1.049 novelty and 1.879 effectiveness (K11).

### 6.2 What changed behaviour, and by how much

| Intervention | Task | Change | Source |
|---|---|---|---|
| ToT b=5 | Game of 24, GPT-4 | 4.0% (CoT) to 74% | a12 |
| Best-of-100 CoT | Game of 24 | 4.0% to 49% | a12 |
| ToT | creative writing coherence | 6.93 (CoT) to 7.56 (judge) | a13 |
| Iterative refine | creative writing | IO 6.19 to 7.67 | a13 |
| RAP | Blocksworld | CoT+SC(10) 46.8 to 51.6 | c07 |
| Repeated sampling vs trees | ARC-AGI GPT-4o | sampling 15.0 beats all trees | d06 |
| NoThinking best-of-N | AMC23 at 700 tokens | 28.9 (Thinking) to 51.3 | d01 |
| In-context regeneration | NoveltyBench | to human-author diversity | b21 |
| Verbalized Sampling | poem diversity (human) | 1.90 to 2.39 | d08 |
| BASIN visit ledger | Game of 24 Qwen3-27B | 43 to 65 | d18 |
| Divergent-convergent prompt | MacGyver GPT-4 | +6.5 points efficient | c19 |
| Self-Reflect | MacGyver GPT-4 | -9.7 points infeasible | c19 |
| Evolutionary search + EvoRePE | CreativeBench Qwen2.5-7B Combo | creativity 0.168 to 0.193 | b10 |
| Nova planning | unique ideas | 3.4x baseline | a23 |
| Meta-persona + high T | similarity on small models | 0.85 to 0.65 | d11 |
| Structured CoT | CreativityBench | -0.012 to +0.039 | d12 |

### 6.3 Reasoning models

- They already search inside the chain: reflection, backtracking, branching (d01, d20, d21).
- The search is costly and uneven. Correct chains are shorter than wrong ones (d20). QwQ-32B scored 0.0% on 4x4 Sudoku while small models trained with five backtracks reached 28.9-32.1% (d21). MCTS got worse when GPT-4o was swapped for o3-mini on 4x4 Sudoku (a drop of 9.47 points) (d07).
- No paper adds an external ToT or MCTS scaffold to a current reasoning model at equal tokens (K25). NoveltyBench contains no reasoning model (d10). Both are open.

### 6.4 Model roles

- Proposer quality sets the ceiling (K03).
- The same model as judge favours its own text (d16) and plateaus on selection (d15).
- Judges calibrate worse on items where humans disagree (Artificial Hivemind, b24; 31,250 annotations, 25 raters per item).
- A retrieval-based multi-agent judge matched individual humans (84.7% vs 82.7%) on 50 items (d17). Tiny validation.

### 6.5 Agent settings

- Agents lose novelty relative to their own history as runs go on, and refine away novel states (K12).
- Fabrication rate 2.5% in Heuresis; more when the checker is visible (K10, K26).
- Zero of 3,222 research runs were rated Original (K18).
- Predetermined tools keep an agent inside the current conception of the domain (a11).

---

## 7. What our agent should take

Format: item | schema part | status | evidence ids.

### Add now (established)

1. **Gate search by whether a checker exists (S0 to S3, G12).** If an exact or cheap code check exists and the class is not easy, use many independent short attempts plus the check. If only a model judge exists, do one pass plus a targeted check; do not run a deep tree. | S0/S3, G12 | [E] | K20, K01, K05; a12, a13, c21, d02, d04, d06, d07.
2. **Baseline is repeated sampling plus checker, at equal dollars and total tokens including prompt tokens (G7, G11).** Any tree must beat it on the same budget before entering the schema. ToT costs more per case than best-of-100 CoT. | G7/G11/S3 | [E] | K02, K21; a14, c24, d01, d02, d06, d15, d20.
3. **In any tree the model proposes and code evaluates; backtracking is allowed.** When the idea tree runs at S6, keep a revisit/backtrack path. | S6 tree rules | [E] for backtracking (K04); proposer-versus-scorer split is [S], see Test first | b06, a15.
4. **Code dedupes and counts distinct candidates in S3 open mode.** Measure distinct answers vs N. Over-generation saturates (about 5% unique at cosine 0.8). Stop drawing when the unique rate falls. | S3 open mode, G12 | [E] | K07; a20, b16, b20, b23.
5. **Never let the generator pick the final novel idea; use an independent check (G5, G8 reinforced).** Extra evidence: self-preference grows with self-recognition (73.5%), selection plateaus after about 100 samples. | G5/G8 | [E] | K06; a16, b17, d14, d15, d16, d17.
6. **Novelty at generation time is unverified until run (G8, S4/S7).** Ideas that look novel lose novelty, excitement and effectiveness after execution. | G8/S4/S7 | [E] | K11; a20, a21, b15, b18.
7. **Hold out the final verifier from the search loop (G3, S8).** A proxy score will be exploited (2.5% fabrications; validation vs test gap worth 9.4-16.6% of medal rate). Choose the final candidate by the independent score, not the running search score. | G3/S8 | [E] | K10; c09, c13, d03, d05, d23.
8. **Do not hard-code a search structure.** Effects are small and task dependent: greedy when a recipe exists, archives when the landscape is broad. Keep the tree rules [D] as they are (3 children, depth 2, 2 expansions). Improve operators before improving policy. | S6 tree rules | [E] | K13; b14, d03, d04, d06, d07.
9. **Add to section 4b (not to add):** temperature as a diversity method, "be creative" or paraphrase prompts, cross-model ensembles for diversity. | S3 open mode, 4b | [E] for temperature cost and cross-model weakness; "be creative" prompt marginal in one paper | b21, d08, d09, d12.
10. **Log novelty against the run's own history per step in open mode.** Cheap and code-computable. It does not change behaviour by itself but makes drift visible. | section 6 log | [S] evidence for the drift; logging itself is a design choice | K12; a22, b11.

### Test first

1. **Ledger of tried approaches in S3 (memory).** Show earlier answers or approach labels, force untried ones, damp strong approaches. [S] | S3, memory | K08, K23; b21, d18. Counter-evidence: d03 (sibling memory null), d04 (gates no top-score gain).
2. **Verbalized Sampling as the one-call diversity step.** [S] | S3 open | K24; d08.
3. **Reframe step before search (list functions or uses first).** [C] | S2, O6/O8 | K15; a06, c03, c19, d12, d13.
4. **In-prompt search trace (AoT) vs a real tree.** [S] | S3 | K27; a15, d22.
5. **Forced exploration quota against explore-to-exploit drift in open agents.** [S] | S3 open, S6 | K12; a22, b11, d19.
6. **External tree on top of a reasoning model.** Open. | S3 gating | K25; d01, d20, d21.
7. **Tree vs best-of-N plus verifier on soft criteria.** Open, the key missing test. | S3 gating | K22.
8. **Mixed-model roles: strong proposer, cheap scorer.** [S] | S3/S4 | K03; a14, c06.
9. **Constraint-feasibility pass before accepting a creative proposal.** [S] | S4, G3 | K16; a24, c18, c19.
10. **Auditor that reads artifacts, plus hidden checker.** [S] | G3, S8 | K26; d23, d05.
11. **Transformational operator (change the rules of the space) at an impasse.** [C] | O4, O6, O8 | K18; d13, a25.
12. **Self-pick among candidates when a cheap independent check exists.** The agreement rate is unmeasured. | S7 | K06 (critique gap 3).

---

## 8. Concrete tests on our bench

Rule for all tests: both arms get equal total tokens (prompt plus completion) and equal dollars. Report success per 1,000 tokens as well as raw success. Use at least three seeds per item. Log per SCHEMA section 6.

| # | Item type | Arms (equal tokens) | Metric | Expected effect |
|---|---|---|---|---|
| T1 Search vs sampling, checkable | Game of 24 style puzzles, Countdown, small ARC items with a code check | (A) k short independent tries + checker; (B) tree (3 children, depth 2) with code-scored states; (C) one long chain | Pass rate; pass per 1,000 tokens | A matches or beats B and C (K02, K21). B wins only where a step-level score is cheap |
| T2 Soft-criteria search | Open design or planning items with a rubric scored by a model not used for generation (blind, length-normalised) plus a 20% human spot check | (A) single pass + one targeted check; (B) best-of-N with independent scorer; (C) tree with same scorer | Held-out human or second-model score; gap between search-time and held-out score | Small gain for B/C (about the ToT coherence gap, +0.6 on 10 points); proxy gap grows with search depth |
| T3 Ledger vs VS vs plain | NoveltyBench-style open prompts and our open-mode set | (A) independent samples; (B) in-context ledger; (C) Verbalized Sampling; (D) persona; (E) temperature raise | Distinct valid answers per 1,000 tokens (classifier + validity check) | B and C beat A by 1.5-2x on distinct count (K08, K24); E lowers validity; D small |
| T4 Ledger inside search | Game of 24 style and our ARC subset | (A) tree; (B) tree + quality-aware visit penalty | Final pass rate; distinct strategies | +5 to +20 points if the base is weak; near 0 if the base is strong (K23) |
| T5 Drift check | Multi-episode open agent task (code improvement with executable score) | (A) greedy; (B) greedy + exploration quota when novelty vs own history falls below threshold | Final score; novelty vs history; fraction of episodes refined away | Novelty recovers; final score flat or small gain (Heuresis: diversity yes, top score no) |
| T6 Reframe step | MacGyver-like constraint items and ARC items | (A) direct search; (B) list functions/uses needed first, then search | Efficient-solution rate; infeasible rate | +0 to +6 points; may be negative on grounded tasks (K15 contested) |
| T7 Reasoning model + external search | Hard combinatorial set (Sudoku 6x6, Countdown diff 7) | (A) reasoning model, one long think; (B) k parallel short thinks + checker; (C) reasoning model inside a 2-level tree | Success per total tokens | B best; C no better than B; consistent with K21, unknown for K25 |
| T8 Proposer/scorer split | Game of 24, code-with-tests items | (A) strong proposer, strong scorer; (B) strong proposer, cheap scorer; (C) cheap proposer, strong scorer | Success per dollar | B near A at lower cost; C near cheap-cheap (K03) |
| T9 Feasibility pass | MacGyver-like physical or resource-constraint items | (A) propose; (B) propose, then code-listed constraints checked step by step | Infeasible rate; efficient rate | Infeasible -5 to -10 points (K16, c19) |
| T10 Self-pick vs check | Open code items with cheap tests | Select among N candidates by (A) self-rank; (B) other-model rank; (C) execution | Chosen-candidate pass rate vs oracle best | A near random-to-weak; C best; quantifies K06 gap |
| T11 Auditor and held-out | Agent loops with a visible score | (A) no guard; (B) hidden checker; (C) + auditor reading artifacts; (D) + held-out eval at the end | Fabrication rate; held-out gap | Held-out gap shrinks by D; auditor catches fabrications but not specialisation (K26) |
| T12 Transformational operator | ARC-like items where the first representation fails | (A) retry with new sample at impasse; (B) at impasse apply O4/O6/O8 as a subgoal | Solve rate after impasse | Small (about 54% vs 50% in UoT). Keep only if above 60% on our set |
| T13 In-prompt search | Game of 24, mini crosswords-like | (A) tree; (B) AoT trace in one prompt | Pass per 1,000 tokens | B equal or better at about one third of tokens (d22); check on a current model |

---

## 9. What does not transfer, and why

- **Large oracle-search gains (74% vs 4%).** These come from puzzles with a short horizon and an exact check. Most of our open items have no such check.
- **AlphaEvolve and FunSearch results.** They need a fast automatic scorer, a human skeleton and large parallel compute (15 samplers, 150 CPU evaluators for FunSearch). Our bench runs short single-agent loops.
- **EoH query savings.** Bin packing gap numbers (5.30% in the FunSearch paper vs 3.78% in the EoH re-run) are different test sets and must not be compared across papers (critique correction 4).
- **MLE-bench agent findings.** Eight-to-24-hour budgets, Kaggle-style tasks, code only. Our items are shorter.
- **EvoRePE steering vector.** Needs open weights; not usable on an API model.
- **Transformational creativity as a goal.** No agreed test, thin tests only, and the effect is near chance. Do not build for it yet.
- **Boden's H-creativity.** Our agent aims at correctness plus useful variety, not historical novelty. P-creativity against the agent's own history is the only usable form.
- **The Nair et al. experiment.** CLIP-style image selection with 4 candidates. Not a chat-model search test.
- **Human creative process claims.** Newell-Shaw-Simon and Boden describe humans. They justify the framing but give no measured numbers for LLMs.
- **LLM-judge novelty scores.** They flatter model output and correlate only moderately with humans (Spearman 0.732). Not a final selector.
- **Cross-model ensembles.** 71-82% similar; they add little diversity.
- **LLM-First Search.** The model controls branching, which conflicts with our rule that code decides transitions. Treat it as a result to learn from, not a design to copy.

---

## 10. Open questions

1. At equal dollars, does tree search beat best-of-N plus an independent verifier on tasks without an exact oracle? No matched-compute study with a soft rubric found (K22).
2. Does a forced exploration quota or ledger stop the novelty decay without lowering final score? Bhushan's own appendix lists it as untested (d19).
3. How often does self-pick agree with execution or cross-model rank among creative candidates when a cheap check exists?
4. Is there any empirical test of transformational creativity in an LLM agent beyond UoT? What would a benchmark of space-changing moves look like?
5. Which cheap diversity method wins at equal tokens: ledger, Verbalized Sampling, persona, temperature, cross-model? Test on reasoning models too (NoveltyBench has none).
6. Do reasoning models already do enough internal search that an external tree adds nothing (K25)?
7. How common is proxy exploitation in text-only scaffolds, as opposed to code tasks?
8. Which structure fits which task: greedy, beam, MCTS, evolutionary, QD? Evidence is a 3-task figure plus scattered comparisons.
9. Does AoT hold on newer models and non-puzzle tasks?
10. Independent replication of Creative Beam Search, QDAIF human evaluation, the Nair et al. object-replacement experiment, and Bhushan et al. 2026.
11. Can the density d be estimated cheaply during S0, and does it predict the best search mode?
12. The Wiggins and Ritchie theory sources were never opened; do their criteria give anything operational beyond what Ventura and Brown say?

---

## 11. Sources

[V] = opened (full text read by the evidence agents; opened:true in the jsonl). [M] = snippet, catalogue or citation only.

| Source | Mark | URL |
|---|---|---|
| Ventura and Brown (2024) Creativity as Search for Small, Interesting Programs | [V] | https://computationalcreativity.net/iccc24/papers/ICCC24_paper_157.pdf |
| Nair, Gizzi, Sinapov (2024) Creative Problem Solving in LLMs and Vision Models (2405.01453) | [V] | https://arxiv.org/abs/2405.01453 |
| Wiggins (2006) Creative Systems Framework | [M] | https://doi.org/10.1016/j.knosys.2006.04.009 |
| Boden (1990/2004) The Creative Mind | [M] | https://en.wikipedia.org/wiki/Computational_creativity |
| Newell, Shaw, Simon (1959/1962) Processes of Creative Thinking | [M] | https://purl.stanford.edu/gk454cz4538 |
| Ritchie (2007) Empirical criteria for attributing creativity | [M] | cited in the Ventura and Brown PDF above |
| Velardo and Vallati (2016) A General Framework for Describing Creative Agents | [V] | https://arxiv.org/abs/1604.04096 |
| Franceschelli and Musolesi (2025) On the Creativity of LLMs | [V] | https://arxiv.org/abs/2304.00008 |
| Franceschelli (2026) On the Creativity of AI Agents | [V] | https://arxiv.org/abs/2604.13242 |
| Yao et al. (2023) Tree of Thoughts | [V] | https://arxiv.org/abs/2305.10601 |
| Sel et al. (2023) Algorithm of Thoughts | [V] | https://arxiv.org/abs/2308.10379 |
| Hao et al. (2023) RAP: Reasoning with Language Model is Planning with World Model | [V] | https://arxiv.org/abs/2305.14992 |
| Franceschelli and Musolesi (2024) Creative Beam Search | [V] | https://arxiv.org/abs/2405.00099 |
| Romera-Paredes et al. (2024) FunSearch | [V] | https://doi.org/10.1038/s41586-023-06924-6 |
| Novikov et al. (2025) AlphaEvolve | [V] | https://arxiv.org/abs/2506.13131 |
| Liu et al. (2024) Evolution of Heuristics | [V] | https://arxiv.org/abs/2401.02051 |
| Lehman et al. (2022) Evolution through Large Models | [V] | https://arxiv.org/abs/2206.08896 |
| Meyerson et al. (2023) Language Model Crossover | [V] | https://arxiv.org/abs/2302.12170 |
| Bradley et al. (2024) QDAIF | [V] | https://arxiv.org/abs/2310.13032 |
| Zhang et al. (2024) OMNI-EPIC | [V] | https://arxiv.org/abs/2405.15568 |
| Lu et al. (2024) The AI Scientist | [V] | https://arxiv.org/abs/2408.06292 |
| Lu et al. (2024) Denial Prompting (code creativity), numbers taken from C04.01 | [M] not re-opened | https://arxiv.org/abs/2407.09007 |
| Si, Yang, Hashimoto (2024) Can LLMs Generate Novel Research Ideas? | [V] | https://arxiv.org/abs/2409.04109 |
| Si, Hashimoto, Yang (2025) The Ideation-Execution Gap | [V] | https://arxiv.org/abs/2506.20803 |
| Bhushan, Zhang, Wang (2026) Can LLM Agents Discover? | [V] | https://arxiv.org/abs/2608.30047 |
| Hu et al. (2024) Nova | [V] | https://arxiv.org/abs/2410.14255 |
| Tian et al. (2025) MacGyver | [V] | https://arxiv.org/abs/2311.09682 |
| Wang et al. (2026) CreativeBench | [V] | https://arxiv.org/abs/2603.11863 |
| Zhang et al. (2025) NoveltyBench | [V] | https://arxiv.org/abs/2504.05228 |
| Bellemare-Pepin et al. (2024) Divergent Creativity in Humans and LLMs | [V] | https://arxiv.org/abs/2405.13012 |
| Jiang et al. (2026) Artificial Hivemind | [V] | https://arxiv.org/abs/2510.22954 |
| Ma et al. (2025) Reasoning Models Can Be Effective Without Thinking | [V] | https://arxiv.org/abs/2504.09858 |
| Wu et al. (2025) Inference Scaling Laws | [V] | https://arxiv.org/abs/2408.00724 |
| Toledo et al. (2025) AIRA-dojo, AI Research Agents on MLE-bench | [V] | https://arxiv.org/abs/2507.02554 |
| Antoniades et al. (2026) Heuresis | [V] | https://arxiv.org/abs/2606.25198 |
| Zhang et al. (2026) Darwin Godel Machine | [V] | https://arxiv.org/abs/2505.22954 |
| Inoue et al. (2025) AB-MCTS | [V] | https://arxiv.org/abs/2503.04412 |
| Herr, Rocktaschel, Raileanu (2025) LLM-First Search | [V] | https://arxiv.org/abs/2506.05213 |
| Zhang et al. (2026) Verbalized Sampling | [V] | https://arxiv.org/abs/2510.01171 |
| Fu et al. (2026) Beyond the Hivemind | [V] | https://arxiv.org/abs/2608.02618 |
| Qian et al. (2026) CreativityBench | [V] | https://arxiv.org/abs/2605.02910 |
| Suzuki and Banaei-Kashani (2026) Universe of Thoughts | [V] | https://arxiv.org/abs/2511.20471 |
| Song et al. (2025) Mind the Gap | [V] | https://arxiv.org/abs/2412.02674 |
| Brown et al. (2024) Large Language Monkeys | [V] | https://arxiv.org/abs/2407.21787 |
| Panickssery, Bowman, Feng (2024) LLM Evaluators Recognize and Favor Their Own Generations | [V] | https://arxiv.org/abs/2404.13076 |
| Min Sen et al. (2026) Automated Creativity Evaluation | [V] | https://arxiv.org/abs/2606.11762 |
| Cheng (2026) BASIN | [V] | https://arxiv.org/abs/2609.00738 |
| Zeng et al. (2025) Revisiting Test-Time Scaling of o1-like Models | [V] (abstract, intro, sec. 4) | https://arxiv.org/abs/2502.12215 |
| Cai et al. (2026) How Much Backtracking is Enough? | [V] | https://arxiv.org/abs/2505.24273 |
| Nair et al. code repository (replication check) | [M] not opened | https://github.com/lnairGT/creative-problem-solving-LLMs |

## Source audit (2026-11-01)

Fresh auditors re-opened the sources of 12 established claims: 9 confirmed as written, 3 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **C04.02-K05** (reworded: the sources support less). Numbers are right, but 'small and noisy' is not what the sources say: ToT human preference 41 vs 21 (38 ties) and CBS 45% vs 29% are called a clear/significant margin by the authors; only QDAIF (0.772 vs 0.767) is a near-tie, and no noise estimate is given for any of them. Corrected claim: When only an LLM judge or human taste is the oracle, gains from search are smaller and less clear-cut than with a programmatic oracle: ToT writing coherence 6.19 (IO) / 6.93 (CoT) to 7.56 (GPT-4 judge), humans preferring ToT over CoT in 41 vs 21 of 100 pairs with 38 ties; Creative Beam Search preferred 45% vs 29% for standard decoding, with 26% of pairs too alike to tell; QDAIF human QD score 0.772 vs 0.767 for fixed few-shot (small human study).
- **C04.02-K20** (reworded: the sources support less). Game of 24 (+66 points, ToT 74 vs IO 7.3), ToT creative-writing and QDAIF numbers match, but none of the opened sources contain cap sets or bin packing (FunSearch results not in the evidence), so those oracle examples are unsupported here. Corrected claim: Search benefit depends on task structure: large when an exact checker exists (Tree of Thoughts on Game of 24: 74% vs 7.3% for IO, about +66 points), small or mixed when only an LLM judge exists (ToT creative writing GPT-4 coherence 6.19 to 7.56; QDAIF human QD 0.772 vs 0.767 for a fixed few-shot prompt, which had the higher human quality rating, 4.133 vs 3.9). Cap-set and bin-packing examples need their own FunSearch citation.
- **C04.02-K21** (reworded: the sources support less). NoThinking (51.3 vs 28.9 at 700 tokens, comparable at up to 9x latency) and Zeng (correct answers shorter, parallel coverage better) match, but Inoue shows repeated sampling beat tree variants on ARC-AGI only at the 128-call budget; AB-MCTS beat repeated sampling on LiveCodeBench and CodeContest (which have test checkers) and passed it on ARC with DeepSeek-V3 at budgets 200-512, so the general 'beat a deep tree' wording is too wide. Corrected claim: On tasks with a cheap checker, many parallel tries plus the checker are a strong baseline against one long thought: NoThinking best-of-N is comparable to full thinking at up to 9x lower latency (AMC23 51.3 vs 28.9 at 700 tokens); for o1-like models correct answers are shorter than wrong ones and parallel scaling gave better coverage than sequential revision; at a 128-call budget repeated sampling beat all tree variants on ARC-AGI, but adaptive-branching tree search (AB-MCTS) beat repeated sampling on LiveCodeBench and CodeContest and on ARC with larger budgets.
- **C04.02-K11** (now single-source: only one opened source, code check).
