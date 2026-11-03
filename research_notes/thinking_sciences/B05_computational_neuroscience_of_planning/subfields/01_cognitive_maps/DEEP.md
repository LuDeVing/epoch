# Cognitive maps: deep document

*Subfield B05.01. Built from evidence_a-d.jsonl (a01-a26, b01-b27, c01-c25, d01-d16), claims.jsonl (K01-K33) and critique.md in this folder. Status marks follow SCHEMA.md: [E] established (two or more independent sources), [S] single source, [C] contested. Evidence ids are in brackets. Numbers marked "unverified" were not re-opened by the cross-checker.*

## 1. What it is

A cognitive map is an internal model of how states of the world connect and what moves lead from one to another. The word came from space (Tolman, rats in mazes). It now covers any relational structure: social hierarchies, concept spaces, task graphs, family trees.

Three parts of the idea matter for us.

1. **Content.** States, moves between them, and (in some versions) distances or directions. Not one stored route, but a structure many routes can be read from.
2. **Use.** Planning by reading the map: find a route, find a detour when a move is blocked, infer a relation never seen.
3. **Revision.** The map changes when a move is blocked or a reward moves. How fast it changes tells which kind of map the agent has.

Why it matters for our agent: schema state S2 (represent) should hold a map of states and moves for the task. This document asks what the evidence says about when writing such a map helps a language model, in what format, and with what checks.

The honest headline: the brain evidence is rich but small-sample and partly fragile. The language-model evidence says a model does not build a reliable multi-step map by itself [c01, c02], and that a prompt-only map is not a free win for strong models [d06, K15, K28]. The part that clearly works is a map or graph that is checked outside the model [d01, d02].

## 2. History and theories in depth

### 2.1 Tolman and latent learning (1930s-1948)

Tolman (1948) argued that learning builds a map-like set in the nervous system, not stimulus-response links. His image: the brain is a "map control room", not a telephone exchange [a01]. Maps can be narrow (strip) or broad (comprehensive). A strip map carries one path from start to goal and fails when the route changes. A comprehensive map survives a new start or a blocked route. The test of map type is behaviour after a change [a01].

Five experiment families are cited in the paper: latent learning, vicarious trial and error, searching for the stimulus, hypotheses, spatial orientation [a01].

Latent learning:
- Blodgett (1929), six-unit alley maze. Three groups: control fed daily; Group II first fed on day 7; Group III first fed on day 3. Errors fall sharply after the first reward in the late-fed groups [a02].
- Tolman and Honzik, 14-unit T-maze. Three groups: never rewarded, always rewarded, rewarded from day 11. The late-rewarded group drops errors fast after day 11 [a03].
- Spence and Lippitt, Y-maze with satiated rats, four trials a day for seven days. After testing hungry vs thirsty, the rats chose the side matching their need "statistically more frequently" [a04].

Limits: exact error counts are only in figures, not read. Tolman gives no statistics in the text. A motivation account (reward changes performance, not learning) is not excluded. Status: contested [K01].

### 2.2 Place cells, grid cells, and the map becomes neural (1971-2005)

O'Keefe and Dostrovsky (1971) found hippocampal place cells. Hafting et al. (2005) found entorhinal grid cells with hexagonal firing. O'Keefe and Nadel (1978) built the theory. These were only seen in snippets by the finders [a23, not opened]. They set the frame: hippocampus and entorhinal cortex hold a spatial map.

### 2.3 Maps beyond space (2016-2020)

- **Abstract 2-D concept space.** Constantinescu, O'Reilly, Behrens (2016): people imagined bird shapes changing in neck and leg length. fMRI showed a six-fold (hexagonal) signal in entorhinal cortex and vmPFC [a08].
- **Graph distance.** Garvert, Dolan, Behrens (2017): after learning object sequences from a random walk on a hidden graph, hippocampal-entorhinal adaptation tracked communicability (a sum over future states), close to the successor representation [a10].
- **Non-spatial variable in rats.** Aronov, Nevers, Tank (2017): hippocampal and entorhinal cells formed firing fields along a sound-frequency axis [a11].
- **Inference from pairwise relations.** Park et al. (2020): people built a 2-D hierarchy from pairwise comparisons and inferred unseen ones [a12].
- **Goal skew.** Butler, Hardcastle, Giocomo (2019): remembered reward locations restructured grid maps in rats [b07].

### 2.4 Successor representation (SR) and replay (2016-2018)

The SR stores, for each state, the expected discounted future occupancy of every other state. It is a cached predictive map. Stachenfeld, Botvinick, Gershman (2017) proposed the hippocampus as a predictive map [a24, not opened]. Gershman (2018) is the review [b23, not opened].

Momennejad et al. (2017) tested whether people behave like SR learners. If so, reward changes should be easy (just re-weight) and transition changes (detours) should be hard (the cached structure is stale) [a05, a06]. Russek et al. (2017) showed pure SR-TD fails detours and policy change, and that adding replay (Dyna-like) repairs it [a07].

### 2.5 Computational unification (2018-2022)

Behrens et al. (2018) asked what a cognitive map is, and argued for relational structure with reuse across settings [a25, not opened]. Whittington et al. (2020) built the Tolman-Eichenbaum Machine (TEM): one mechanism learns an abstract structure, separate from the entities in it, and explains place/grid remapping and relational inference [a13, b08]. Whittington, Warren, Behrens (2022) showed a transformer with recurrent position encodings (TEM-t) is far more sample-efficient and relates to the hippocampal model [a14, b09, c12].

### 2.6 Language models and maps (2022-2026)

Four lines:
1. **Behavioural tests** with graphs, mazes and text games: CogEval [a18], MANGO [c18], MazeEval [c20], CheeseBench [c23].
2. **Probing** for internal maps: Othello-GPT [a15], maze transformers [a16], space and time probes [a17, d07], in-context graph geometry [a21].
3. **Scaffolds that write or hold a map**: VoT [a22], External Hippocampus [b22], MAP [b21], map-prompting in Kim 2024 [b12, b13], GAVEL, Hybrid-WM, GraphThink [d01-d05].
4. **Mechanism studies** on small trained models: what training data makes a map appear [b16, b17, c21, c22, b14].

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Latent learning: unrewarded rats, then rewarded, drop errors sharply | Figures only, no stats in text; groups fed from day 3, 7, 11 | Blodgett 1929; Tolman and Honzik via Tolman 1948 [a01-a04] | [C] K01 |
| Broad map survives a changed start or blocked route; strip route does not | Behavioural test of map type; SR-TD model fails detours | Tolman 1948; Russek 2017 [a01, a07] | [E] K02 |
| Humans: reward revaluation easier than transition revaluation (Study I) | N=58 of 69. Reward 0.520 (SEM 0.020), transition 0.450 (0.023), control 0.031. Reward vs transition t(57)=2.89, Bonferroni p=0.016. Transition vs control t(57)=9.05 (critique: 10.14 for reward vs control). Slower RT for transition, t(57)=2.08 | Momennejad 2017 [a05, b05] | [E] K03 |
| Same, Study II (active sequential task) | N=88 of 112 (21% excluded). Switch rate: reward 0.659, transition 0.466, policy 0.500, control 0.080. Reward vs transition Z=-2.85, p=.0034. Reward vs policy Z=-2.61, p=.0043. Policy vs transition p=.577 | Momennejad 2017 [a06, b06] | [E] K03 |
| Cached SR alone fails detours; replay fixes it | Model result | Russek 2017 [a07] | [S] K04 |
| Graph-derived repair beats asking the LLM to replan (4B, symbolic) | 67.7 vs 55.4 success; 1 vs 3.4 LLM calls | GAVEL [d02] | [S] K04 |
| Hexagonal 6-fold signal for abstract concept space | N=28; entorhinal Z=4.41, vmPFC Z=4.09, retrosplenial Z=4.73; no effect at 4, 5, 7, 8-fold (p>0.15); vmPFC strength vs performance r=0.43, p=0.039; accuracy 72.8% | Constantinescu 2016 [a08] | [S] K05 (not re-opened by checker) |
| Grid-like signal in navigation: young yes, old no | Young 6-fold t(19)=3.71, p=0.002; old t(20)=-0.79, p=0.438; young vs old t(39)=-2.66, p=0.011 | Stangl 2018 [a09] | [C] K06 |
| Social-space grid-like evidence partial | N=38; 31 had clustered orientations (all p<0.040) but the pmEC ROI "less consistent" | Wu 2024 [b26] | [C] K06 |
| Passive navigation: no 6-fold signal in a large sample | N=110; right EC t(109)=0.728, p=0.234, BF01=7.31, d=0.07; left EC BF01=8.60 | Kransberg 2026 [d09] | [C] K06 |
| Small positive replications | Park 2021 N=21 (EC and mPFC, stable across days); Theves 2020 N=25 (EC only, mPFC null, pre/post p=0.07) | [d11, d10] | [C] K06 |
| Response time follows communicability, not link or Euclidean distance | RT: communicability t(25)=2.77, p=0.01; link t=-0.40; Euclidean t=-0.85; fMRI N=23 | Garvert 2017 [a10] | [S] K07 |
| Non-spatial variable coded by place/grid cells in rats | 40.0% CA1 (2208 units, 5 rats), 51.3% MEC (1164 units, 9 rats) task-modulated; 25.1% of 295 place cells; 34.3% of 105 grid cells | Aronov 2017 [a11] | [S] K08 |
| Reward location reshapes grid code | 7 rats, 102 grid cells; median rotation 12.53 deg (p=1.1e-12); 49 of 102 changed; control only 3 rats | Butler 2019 [b07] | [S] K09 |
| Humans infer unseen relations from pairwise training | 93.6% (+/-0.77) inference accuracy; 27 analysed of 33 scanned; only 82 of 282 passed training | Park 2020 [a12] | [E] K10 |
| Behavioural transfer of abstract structure is strong; neural map forms slowly | Transfer t(27)=9.54, N=28; mPFC graph code only at scan 2 (1 to 7 days later), N=22, p=0.003; EC null | Baram 2021, 2026 [d12, d13] | [S] K31 |
| Humans use both vector and adjacency maps | N=401; vector choice 73.8% in open grids, 63.6% cluttered; RL agents 73.2% | Lan 2025 [d14] | [S] K30 |
| GPT-4 on cognitive-map tasks | 1-step 0.99, 2-step 0.82, 3-step 0.55, n-step 0.47, policy reval. 0.21, reward reval. 0.67, transition reval. 0.60. Small models 0.04-0.06 at 3 steps | CogEval [c02, a20] | [S] K12 |
| GPT-4 fails shortest path across clusters | Never above 10% (the "0 of 30" figure was not re-found); edge hallucination | CogEval [c03] | [S] K13 |
| BFS/DFS hints and CoT: mixed | CoT: non-teleporting shortcut 1.00, teleporting 0.50 | CogEval [a19, c04] | [S] K14 |
| Writing a map helps only after fine-tuning | Fine-tuned 76.5% optimal plans vs 19.0 (no CoT) and 26.5 (best CoT); prompting a map 0-1%; plain DFS 94.5 reachable vs map 88.5; backtrack ablation 42.3 to 85.2 (forward construction) | Kim 2024 [b12, b13, c06-c08, d16] | [C] K15 |
| Few-shot map prompting fails | 0-4 demos: o1 map prompt 0, 0, 0, 10%; o1 no special prompt 0, 18, 34, 38%; GPT-4o and Llama-3 about 0-1% | Kim 2024 [d06] | [S] K28 |
| Visualising state each step (VoT) | GPT-4 35.50 to 59.00 (+23.5); CoT about 54.00; vs CoT p<0.16 (not significant); state-visualisation accuracy 24-26% | Wu 2024 [a22, c14, c15] | [C] K16 |
| External topological map, 3B model | 64.40 to 81.20% (about 2.52 rounds) vs CoT self-consistency k=5 59.80; 500 problems | Yan 2025 [b22] | [S] K17 |
| Map-then-act (MAP), Qwen3-4B | ReAct to MAP: ALFWorld 31.8 to 61.1, TextCraft 31.8 to 71.9, SciWorld 13.9 to 24.3; strong models near 99 gain little | Liu 2026 [b21] | [E] K18 |
| Benefit shrinks with strength | Hybrid-WM gain +26 (Llama-3-8B) to +4 (GPT-4o-mini) | Song and Cai 2026 [d04] | [C] K27 |
| Checked graph world model lifts frontier models | BEHAVIOR-1K 100 tasks: Claude Sonnet 5 38.6 to 99.4; GPT-5.6 Sol 24.6 to 99.2; Qwen3-8B 23.6 to 89.2; Qwen3-4B 2.4 to 75.2. Time 18.0 vs 18.2 s | GAVEL [d01] | [S] K25 |
| Own imagined states are wrong | Hallucinated-state rate: direct 0.252, CoT 0.225, replan 0.205, verifier 0.193; hybrid with grounding 0.079; success 0.496/0.591/0.668/0.684/0.838. Tokens per success: CoT 21301, Replan 16389, Hybrid-WM 15021. Self-verifier invalid-action rate 0.062 | Hybrid-WM [d03] | [S] K26 |
| Task graph in prompt (trained 7B) | Long-horizon success: full 90.04; no graph prompt 40.69; no GRPO 33.67; no verifier 86.25 | GraphThink [d05] | [S] K33 |
| Perception-built maps are poor | Landmark IoU under 5%, F1 under 35%; planning success 5.54% (target), 3.76% (path) | Zhu 2026 [d08] | [S] K29 |
| Linear coordinates in activations | Llama-2-70b R2: world 0.911 (unverified), NYC 0.359; held-out proximity error 0.164 (c10) vs 0.170 (a17), unresolved; 17 models R2 0.43-0.68 | Gurnee and Tegmark [a17, c09, c10]; Wu 2026 [d07] | [E] K19, K32 |
| Othello-GPT represents board state | Illegal moves 0.01% (trained synthetic), 5.17% (championship data), 93.29% untrained; linear probes weak, non-linear good | Li 2023 [a15, b20, c13] | [E] K20 |
| Maze transformers | Best OOD 70.7% exact, 87.1% valid, 100% reach target; hallway model 24.2% exact | Ivanitskiy 2023 [a16] | [S] K21 |
| In-context graph geometry appears abruptly | Llama-3.1-8B, ring, square grid, hex grid; ~400-1400 tokens; accuracy rises as Dirichlet energy falls | Park 2025 [a21, b15] | [S] K22 |
| Pairwise links composed on demand | About 1% of keys/values sparse binding; no global coordinate map | Qin 2026 [b18, d15] | [C] K23 |
| Aliased rooms, trained transformers | LSTM 99.00% accuracy but beats fallback path only 29.53%; bottleneck variants 96.59-99.55% improvement | Dedieu 2024 [b14] | [S] K24 |

## 4. Mechanisms and models

### 4.1 Strip vs comprehensive map (Tolman)

Data structure: a directed graph G = (states, moves). A strip map is a list of states from start to goal. To test which one an agent holds, change the task: block one move, move the goal, change the start. A graph agent re-runs search. A list agent fails.

Implementation for a prompt scaffold: S2 emits an explicit list "state -> move -> next state" for every move the task text allows, plus the goal and start. S3 plans by reading that list, not by remembering one route.

### 4.2 Successor representation

Define M(s, s') = expected discounted number of future visits to s' starting from s. With transition matrix T and discount g: M = (I - gT)^-1. Value = M times reward vector R.
- Reward change: only R changes. Value updates at once. Easy.
- Transition change: T changes. Cached M is stale. Fix needs relearning or replay. Hard.
- Humans show exactly this ordering [a05, a06]. Pure SR-TD fails detours; adding Dyna-style replay (simulate transitions offline and update M) repairs it [a07].

Engineering reading: a stored value table or plan is cheap to reuse on reward change but breaks on transition change. A re-plan operator must be able to rebuild from the move list, not from the stored plan.

Communicability (Garvert) is a sum over walks of all lengths, weighted by length: C = expm(A) for adjacency A. It rewards many parallel routes, not just the shortest [a10, b04]. A test predictor for "how close are two items on this graph" is therefore C, not path length.

### 4.3 Grid-like code (brain only)

A hexadirectional signal is fMRI signal that varies with movement direction at 60-degree periodicity (6-fold). Analysis: fit cos(6(theta - phi)) per voxel with a quadrature (sin and cos) fit on one half of the data, test on the other half. Control folds are 4, 5, 7, 8. Constantinescu applied this to imagined movement in a 2-D shape space [a08]. Because the evidence is fragile (section 5), nothing in the schema depends on it.

### 4.4 Tolman-Eichenbaum Machine

Two streams: a structural code g (grid-like, learned from transitions, reusable across environments) and a sensory code x (what is seen). A conjunctive memory p binds g and x (hippocampus). New environment with the same structure: reuse g, bind new x. This explains remapping and zero-shot relational inference (family trees) [a13, b08]. TEM-t replaces the recurrence with a transformer with learned position encodings and learns faster [a14, b09].

Engineering reading: keep structure separate from entity names. Test by renaming entities and checking the plan transfers [K11].

### 4.5 Training data decides whether a map forms (small GPT-2)

- Trained on random-walk (foraging) steps: forms a coordinate-like map. Reliance on direction tokens vanishes from layer 8 on. Next-step accuracy 100% at 2-3 steps, 71% near 11 steps, over 96% beyond 30 [b16, b17, c21].
- Trained on shortest paths: stays path-dependent. Accuracy falls from 95% at Manhattan distance 1 to 22% at 8; Hamiltonian-path version 83% to 0% by 7 [c21, c22].
- Hybrid model kept over 97% at long context [b16].

Reading: exploration without goals produces the general map; goal-directed data produces a goal-bound heuristic. This echoes latent learning, but only for small models trained from scratch. Do not transfer to prompts without a test.

### 4.6 Map-then-act scaffolds

- **MAP** (Liu 2026): first build a map of the environment from exploration, then act using it. Gains 61.1 vs 31.8 on ALFWorld for a 4B model [b21].
- **External Hippocampus** (Yan 2025): topological map held outside the model, queried in rounds (about 2.52 refinements) [b22].
- **VoT** (Wu 2024): after each step, the model redraws the current state in text. Raised GPT-4 from 35.50 to 59.00, not significant vs CoT [a22, c14, c15].
- **GAVEL** (Wang 2026): graph of objects, relations, action preconditions and effects. Code rolls the LLM plan forward, finds invalid steps, repairs. Repair is done by the graph, not the LLM [d01, d02].
- **Hybrid-WM** (Song and Cai 2026): a small learned transition model checks each imagined step [d03, d04].
- **GraphThink** (Li 2026): task graph in the prompt plus GRPO training plus verifier [d05].
- **RAP** (Hao 2023): LLM as world model plus MCTS. Blocksworld, LLaMA-33B: CoT 0.17, 0.02, 0.00 at 2, 4, 6 steps; RAP(20) 1.00, 0.88, 0.42 [c25]. Many model calls.

The pattern across these: the gain comes with an external check, a trained component, or a weak backbone. A pure prompt-only written map on a strong model has no positive test.

## 5. What holds up

### 5.1 Holds up

- **Reward vs transition revaluation asymmetry in humans.** Two experiments (N=58, N=88), significant in both. The theory (SR) predicts it. [E]
- **Broad map beats stored route on detours.** Tolman's argument plus the SR/replay modelling [a01, a07]. [E]
- **Relational inference from pairwise training.** 93.6% accuracy, but with heavy attrition (82 of 282 passed training), so the finding is about learners who succeed [a12]. [E]
- **LLMs lose accuracy as multi-step use of the graph grows.** CogEval (one study, but a clear gradient 0.99 to 0.47) [c02]. [S]
- **Maps are decodable inside LLMs.** Linear space and time probes replicate across 17 models, R2 0.43-0.68 [d07]. Othello-GPT [a15]. [E] for presence, silent on use.
- **A checked external graph model raises success a lot, even for frontier models** (GAVEL), but it is one 2026 preprint and the graph is built from known action definitions, not written by the LLM [d01]. [S]

### 5.2 Fragile or failed

- **Grid-like code in abstract space.** Positive: N=28 [a08], N=21 [d11], N=25 [d10]. Mixed or null: older adults null [a09], 2024 social-space ROI "less consistent" [b26], 2019 vmPFC preprint null (not opened) [b25], Kransberg N=110 passive navigation null with BF01 7.3 [d09]. Kransberg tested spatial navigation, not abstract space, so it is not a direct refutation. Verdict: fragile, small N, no abstract-space replication above N=30 [K06].
- **Latent learning.** Second-hand summary, no statistics; motivation account open [K01].
- **Mapping and prompting for strong models.** Prompt-only map-writing gave 0-1% in most models (fine-tuning was required for 76.5%) [b13]. Few-shot: o1 got 38% with no map prompt at 4-shot but 10% with the map prompt [d06]. Plain DFS beat the trained map (94.5 vs 88.5) [d16].
- **VoT.** The +23.5 over plain is real but the gain over CoT is not significant (p<0.16). State visualisation accuracy is only 24-26% [c15].
- **Self-verification.** A model-based self-verifier cut invalid actions to 6.2% but barely cut hallucinated states (0.193 vs 0.205); external grounding cut them to 0.079 [d03].
- **CoT can hurt in map-like tasks.** CheeseBench: Qwen2.5-VL-7B default 46.7%, CoT 31.9%, few-shot 29.6% [c24]. CogEval: CoT helped non-teleporting shortcuts (1.00) but not teleporting (0.50) [c04].

### 5.3 Moderators and boundary conditions

- **Age.** Hexagonal signal absent in older adults (6-fold t(20)=-0.79) [a09].
- **Task type.** Passive vs active navigation (Kransberg) and space vs concept space differ [d09].
- **Model strength.** Gains from map scaffolds shrink with strength: MAP and Yan vanish on strong models [b21, b22]; Hybrid-WM +26 to +4 [d04]. Exception: GAVEL (verification) [d01].
- **Training.** Map benefit appears with fine-tuning [b12], with exploration-type training data [c21], not with a prompt [b13, d06].
- **Language.** MazeEval: English vs Icelandic max solvable maze size: Claude Opus 4 11 vs 8, Claude Sonnet 4 12 vs 8; gap W=273, p<0.001, d=0.50 [c20].
- **Interface.** CheeseBench: same model ranged 20% to 57% by interface parameters alone [c23].
- **Time.** The mPFC abstract graph code appears only at the second scan, 1 to 7 days later [d13].

### 5.4 Interventions that worked / did not

| Worked | Did not work |
|---|---|
| External graph check and repair (GAVEL: 38.6 to 99.4 on Sonnet 5) [d01] | Prompting a map without training (0-1%) [b13] |
| Fine-tuning to write a map (76.5%) [b12] | Few-shot map prompt, 0-4 demos (0-10%) [d06] |
| External topological map, small model (+16.8 points) [b22] | LLM asked to replan from feedback (55.4 vs 67.7 graph repair) [d02] |
| Map-then-act on 4B (+29.3 ALFWorld) [b21] | Model self-verification on hallucinated states [d03] |
| Grounded transition model, weak backbones [d03, d04] | Landmark maps from video (IoU under 5%) [d08] |
| Backtracking in forward construction (42.3 to 85.2) [b12] | CoT on small model in rodent paradigms [c24] |

## 6. Language models

### 6.1 Behaviour on map tasks

**CogEval (2023, Momennejad et al.).** Eight models: GPT-4, GPT-3.5, davinci-003, Claude-1, Bard, Cohere, LLaMA-13B, Alpaca-7B (plus Pythia-20B in tables). Tasks built from human cognitive-map experiments. 30 runs per condition for OpenAI models. Conclusion: "These findings do not support the idea of emergent out-of-the-box planning ability in LLMs" [c01]. GPT-4-32k: 1-step 0.99, 2-step 0.82, 3-step 0.55, n-step 0.47, reward revaluation 0.67, transition revaluation 0.60, policy revaluation 0.21. Best policy revaluation across models 0.28 (Claude-1) [c02]. Failure modes: hallucinated edges, long trajectories instead of shortest paths, loops on community-structured graphs; shortest path across clusters never above 10% [a20, c03]. This is a 2023 study on closed models. No 2025-26 reasoning-model rerun was found.

**MANGO (2024).** 53 text-game mazes. GPT-4 answers about half of route-finding questions; humans 0.82 (n=31) route, 1.00 (n=30) destination [c18]. A map-to-graph-to-search pipeline was "very challenging" [c19].

**MazeEval (2025).** Coordinate-only mazes 5x5 to 15x15. O3 perfect up to 30x30. Others fail past 9x9, and 100% of their failures involve revisiting a cell 10 or more times (loops) [c20]. Loop control is a clear failure mode.

**CheeseBench (2026).** 13 LLMs on nine rodent paradigms as ASCII gridworlds. Claude Opus 4.7 86.7% average vs rodent reference 78.9%, random 38.0%, tabular Q-learning 31.2%. Best open model Qwen2.5-VL-7B 68.0% (32B 64.7%, 72B 58.5%). Radial arm maze (working memory): best open-weight 10.0% vs rodent 70% [c23, c24]. Frontier models now match the rodent reference on these simple paradigms.

**Perception to map (2026).** Frontier multimodal models (GPT-5.1, Gemini-3-Pro): landmark IoU under 5%, planning success 5.54% / 3.76%. An 8B model fine-tuned to write a hierarchical map did much better and the hierarchical map beat a flat grid [d08].

### 6.2 What changed the behaviour, and by how much

| Change | Effect | Strong model? |
|---|---|---|
| Fine-tune to write a map before planning [b12] | 19.0 / 26.5 to 76.5 optimal | Not applicable (training) |
| Prompt a map, no training [b13, d06] | 0-1% (4 demos: 0-10%) | o1 did better with no prompt (38%) |
| BFS/DFS hints [b11] | Task and temperature dependent | Mixed |
| Visualise state each step [a22] | 35.50 to 59.00 (CoT ~54.00, p<0.16) | GPT-4 only |
| External topological map [b22] | 64.40 to 81.20 on 3B | Gain vanishes on strong |
| Map-then-act [b21] | 31.8 to 61.1 etc. on 4B | Strong near 99, little gain |
| Hybrid-WM grounded transition model [d04] | +26 to +4 by backbone | Smaller on stronger |
| GAVEL graph verifier [d01] | 38.6 to 99.4 Sonnet 5; 24.6 to 99.2 GPT-5.6 Sol | Yes, large |
| LLM world model plus MCTS (RAP) [c25] | LLaMA-33B 6-step 0.00 to 0.42 | Many calls |
| GAVEL repair vs LLM replan [d02] | 67.7 vs 55.4; 1 vs 3.4 calls | 4B |

### 6.3 Inside the model

- Space and time are linearly decodable (Llama-2-70b R2 world 0.911, unverified; NYC 0.359); generalisation to held-out blocks is worse [a17, b19, c10]. Across 17 models R2 0.43-0.68 [d07].
- Othello-GPT: board state inside; illegal moves 0.01% vs 93.29% untrained [a15, b20].
- In-context graph structure appears abruptly in activations (Llama-3.1-8B) [a21].
- Qin 2026 finds sparse pairwise binding (about 1% of keys/values) composed on demand, not a global coordinate map [b18, d15]. Hence "LLMs have cognitive maps" does not mean geometry.
- Presence is not use. Steering-style map claims depend on measurement choices; only the linear world map survives every control [d07].

### 6.4 What this means in plain terms

Models do one-step lookups well and multi-step chaining poorly. They hallucinate edges and loop. They do not reliably repair a plan after a transition change. A written map does not fix this by itself. What fixes it: an outside check of each move against the map, graph-derived repair, or training. For a strong model with a short task, plain reasoning may already be as good as a written map. No source tests this at equal tokens.

## 7. What our agent should take

Schema parts: G guardrail, S state, O operator, memory.

### Add now (established)

1. **S2 holds a broad map: states, moves, goal, start, not one route.** Status [E]. Schema part S2. Evidence a01, a07, K02. It costs nothing: list the allowed moves from the task text. Use only for tasks with a state-move structure (routes, puzzles, tool sequences, dependency graphs). Gate by G7: keep only if it pays at equal tokens (see Test first).
2. **A blocked move or moved goal is a signal to re-plan from the map, not from the stored plan.** Status [E] for humans (transition revaluation is the hard case), model support [S]. Schema part O (re-plan) with G1 (signal-driven). Evidence a05, a06, a07, b05, b06, K03. Implement: S4 fail with "move not allowed" triggers S5 using the written move list.
3. **Do not build anything on grid-cell or hexagonal-code details.** Status [E] that the evidence is fragile (K06). Schema part: none.
4. **Weak-backbone map-first mode.** Status [E] (MAP, Hybrid-WM, Yan direction agrees). Schema part S2, S0 (gate by model strength and class). Evidence b21, b22, d04, K18. Strong models gain little, so default off; turn on only if the class's plain pass rate is low and the backbone is small.
5. **Do not make a map-writing step mandatory for strong reasoners.** Status [S] (d06, K28), consistent with G7 [E]. Schema part G7.
6. **Models are reliable at one-step edge lookup and unreliable at multi-step chaining; check each hop.** Status [S] (CogEval), consistent with G2/G3 [E]. Schema part G2, S4. Evidence c02, a20.

### Test first

| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| T1 | Written state-move map vs plain CoT at equal tokens, strong model | S2 | [C] | K15, K27, K28, d06, GAP 1 |
| T2 | Code check of each planned move against the map (legality check) | G, S4 | [S] | K25, d01, d02 |
| T3 | Edge check: compare written map to task text before planning | G | [S] | K13, K26, d03 |
| T4 | Re-plan operator after a changed transition | O | [S] | K04, d02 |
| T5 | Map format: relation list vs adjacency vs coordinates vs both | S2 | [C] | K23, K30, d14, d15 |
| T6 | Goal and predecessor marking in the map | S2 | [S] | K09, b07 |
| T7 | Redraw state after each step (VoT) with a state check | S2/G | [C] | K16, c15 |
| T8 | Rename entities, keep structure (reuse of structure) | S2 | [E] (computational) | K11, a13 |
| T9 | Loop guard: detect revisits and force a different move | G | [S] | c20 |
| T10 | Pairwise vs global layout queries | S2 | [C] | K23, b18 |
| T11 | Relatedness on a graph: multi-path vs shortest path predictors | S2 | [S] | K07, a10 |
| T12 | Many-shot map prompt | S2 | [S] | K28, d06 |

## 8. Concrete tests on our bench

All arms at equal total tokens (count setup and map text). Report the success rate with a confidence interval and tokens per success.

| Test | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 | CogEval-style graph tasks (1-step to n-step paths, shortcut, detour) and gridworld paths, 3 difficulty levels | A: plain CoT. B: write map then plan. C: map optional | Success rate; tokens per success | Small or none for a strong model; gain on 3+ steps and weak model. Add if B beats A by 5 points or more |
| T2 | Same graphs, plus blocked-move variants | A: plan only. B: plan plus code legality check on each move against the map | Invalid-move rate; success | Large cut in invalid moves (GAVEL 38.6 to 99.4 in symbolic setting) |
| T3 | Tasks where the map is built from text | A: map unchecked. B: map plus code edge check vs the task text | Edge hallucination rate; success | Fewer hallucinated edges (weak-backbone 17-32%); frontier rate unknown |
| T4 | Reward, transition and policy change tasks (Momennejad-style) | A: re-ask model after failure. B: re-plan from move list. C: code-derived repair | Success after change; calls | Order reward > transition, policy as in humans; B or C closes gap |
| T5 | Same graph, three formats at equal tokens | Relation list, adjacency plus coordinates, both | Success; multi-hop accuracy | Unknown; prior favours the relation list |
| T6 | Search tasks with a known goal | A: plain map. B: goal and predecessors marked | Steps to goal; success | Fewer steps; no human or LLM prior |
| T7 | Navigation in text, 10+ steps | A: CoT. B: redraw after each move with state check | State accuracy; success | Gain only if redraw accuracy is above chance |
| T8 | Isomorphic tasks with renamed entities | A: map in names. B: map in abstract ids | Transfer success | Equal or better with abstract ids |
| T9 | Mazes up to 15x15 | A: plain. B: visited-set tracking in code | Loop rate (10 or more revisits); success | Loops down (MazeEval: all failures were loops) |
| T10 | Mixed queries: relation lookup vs layout | List vs coordinates | Accuracy by query type | List better for lookup |
| T12 | Maze, 8 to 32 map demos | Many-shot vs zero-shot | Success | Unknown; 0-4 shot gave 0-10% |

## 9. What does not transfer, and why

- **Hexagonal grid code.** An fMRI signal in brains; no counterpart in a prompt. Evidence fragile [K06].
- **Slow consolidation of the map (days).** The mPFC code needs 1 to 7 days [d13]. An agent has one context.
- **Rodent goal skew in grid fields** [b07]. A smooth neural effect with 7 rats; whether marking the goal helps text search is untested.
- **Latent learning without reward.** For a task with no exploration phase (one prompt), there is nothing to learn latently. It holds only if the agent has free exploration steps.
- **Training-regime results.** Kim's 76.5% and the GPT-2 map formation need gradient training. We train nothing. A prompt did not reproduce them [b13, d06].
- **Probe results (Gurnee, Othello).** Information present in activations does not show a written map helps [d07, K19].
- **Perception-built maps** [d08]: our tasks are text; ignore unless images are used.
- **SR parameters (discount, replay budget).** The agent does not learn an M matrix; the useful part is the revaluation asymmetry only.
- **GAVEL's graph** is built from known action definitions by code. If our tasks have no formal action definitions, the same gain is not available.
- **Weak-backbone gains** (MAP, Yan, Hybrid-WM) may vanish for our strong agent.

## 10. Open questions

1. Does a written state-move map beat plain CoT at equal tokens for a strong current model? No source controls tokens (GAP 1).
2. Where is the break-even model strength? Direction known (gain shrinks), size not located (GAP 2).
3. Has CogEval been rerun on reasoning models (o1/o3, Claude, Gemini thinking)? None found (GAP 3). Does the policy-revaluation collapse (0.21) persist?
4. Which format works for prompt-only maps? No comparison exists (GAP 4).
5. What is the frontier model's edge error rate in a written graph, and does an edge check repair planning (GAP 5)?
6. Does goal-skewing help LLM search (GAP 7)?
7. Do grid-code replications above N=30 exist in abstract space (GAP 8)?
8. Does VoT's redraw step help once state accuracy is checked (GAP 9)?
9. Do many-shot map demonstrations transfer the trained-map benefit (GAP 10)?
10. Is the GAVEL gain from the map or from the verifier? The comparison is LLM alone vs LLM plus verifier, so the two are not separated [d01].
11. Do Qin's pairwise links mean a relation list is the right prompt format [d15]?
12. Do hierarchical maps beat flat ones in prompting (d08 shows it for trained models)?

## 11. Sources

[V] = opened and read this session by the finders (critique re-opened some). [M] = snippet only or not opened.

**Primary and brain**
- [V] Tolman (1948) Cognitive maps in rats and men. https://psychclassics.yorku.ca/Tolman/Maps/maps.htm (a01-a04, a26)
- [V] Momennejad et al. (2017) The successor representation in human reinforcement learning. https://pmc.ncbi.nlm.nih.gov/articles/PMC6941356/ (a05, a06, b05, b06)
- [V] Russek et al. (2017) Predictive representations can link model-based RL to model-free mechanisms. https://pmc.ncbi.nlm.nih.gov/articles/PMC5628940/ (a07)
- [V] Constantinescu, O'Reilly, Behrens (2016) Organizing conceptual knowledge in humans with a gridlike code. https://pmc.ncbi.nlm.nih.gov/articles/PMC5248972/ (a08, b01, b02; numbers not re-opened by checker)
- [V] Stangl et al. (2018) Compromised grid-cell-like representations in old age. https://pmc.ncbi.nlm.nih.gov/articles/PMC5887108/ (a09; not re-opened)
- [V] Garvert, Dolan, Behrens (2017) A map of abstract relational knowledge in the human hippocampal-entorhinal cortex. https://pmc.ncbi.nlm.nih.gov/articles/PMC5407855/ (a10, b03, b04)
- [V] Aronov, Nevers, Tank (2017) Mapping of a non-spatial dimension by the hippocampal-entorhinal circuit. https://pmc.ncbi.nlm.nih.gov/articles/PMC5492514/ (a11)
- [V] Park et al. (2020) Map making: constructing, combining and inferring on abstract cognitive maps. https://pmc.ncbi.nlm.nih.gov/articles/PMC7529977/ (a12)
- [V] Butler, Hardcastle, Giocomo (2019) Remembered reward locations restructure entorhinal spatial maps. https://pmc.ncbi.nlm.nih.gov/articles/PMC6516752/ (b07)
- [V] Wu et al. (2024) Distance and grid-like codes support the navigation of abstract social space. https://pmc.ncbi.nlm.nih.gov/articles/PMC11178359/ (b26, b27)
- [V] Kransberg et al. (2026) Failure to detect entorhinal grid-like signals. https://pmc.ncbi.nlm.nih.gov/articles/PMC13058850/ (d09)
- [V] Theves, Fernandez, Doeller (2020) Distance and direction codes. https://pmc.ncbi.nlm.nih.gov/articles/PMC7096136/ (d10)
- [V] Park, Miller, Boorman (2021) Inferences on a multidimensional social hierarchy. https://pmc.ncbi.nlm.nih.gov/articles/PMC8759596/ (d11)
- [V] Baram et al. (2021) Entorhinal and ventromedial prefrontal cortices abstract and generalize the structure of reinforcement learning problems. https://pmc.ncbi.nlm.nih.gov/articles/PMC7889496/ (d12)
- [V] Baram et al. (2026) An abstract relational map emerges in the human medial prefrontal cortex. https://pmc.ncbi.nlm.nih.gov/articles/PMC7619258/ (d13)
- [V] Lan, Hunt, Summerfield (2025) Goal-directed navigation in humans and deep RL agents. https://pmc.ncbi.nlm.nih.gov/articles/PMC12324678/ (d14)
- [M] O'Keefe and Dostrovsky (1971); Hafting et al. (2005); O'Keefe and Nadel (1978). https://doi.org/10.1016/0006-8993(71)90358-1 (a23)
- [M] Stachenfeld, Botvinick, Gershman (2017) The hippocampus as a predictive map. https://doi.org/10.1038/nn.4650 (a24)
- [M] Behrens et al. (2018) What is a cognitive map? https://doi.org/10.1016/j.neuron.2018.10.002 (a25)
- [M] Gershman (2018) The successor representation. https://www.jneurosci.org/content/38/33/7193 (b23)
- [M] 2020 bioRxiv social-hierarchy grid-like code. https://www.biorxiv.org/content/10.1101/2020.05.29.124651 (b24)
- [M] 2019 bioRxiv vmPFC null, "Subjective value, not a gridlike code". https://www.biorxiv.org/content/10.1101/759951 (b25)

**Models and language models**
- [V] Whittington et al. (2020) The Tolman-Eichenbaum Machine. https://pmc.ncbi.nlm.nih.gov/articles/PMC7707106/ (a13, b08)
- [V] Whittington, Warren, Behrens (2022) Relating transformers to models and neural representations of the hippocampal formation. https://arxiv.org/abs/2112.04035 (a14, b09, c12)
- [V] Li et al. (2023) Emergent world representations (Othello-GPT). https://arxiv.org/abs/2210.13382 (a15, b20, c13)
- [V] Ivanitskiy et al. (2023) Structured world representations in maze-solving transformers. https://arxiv.org/abs/2312.02566 (a16)
- [V] Gurnee and Tegmark (2023/2024) Language models represent space and time. https://arxiv.org/abs/2310.02207 (a17, b19, c09-c11; some R2 values unverified)
- [V] Momennejad et al. (2023) CogEval. https://arxiv.org/abs/2309.15129 (a18-a20, b10, b11, c01-c05)
- [V] Park et al. (2025) In-context learning of representations. https://arxiv.org/abs/2501.00070 (a21, b15, c16, c17)
- [V] Wu et al. (2024) Mind's Eye of LLMs: Visualization-of-Thought. https://arxiv.org/abs/2404.03622 (a22, c14, c15)
- [V] Kim et al. (2024) How language models extrapolate outside the training data. https://arxiv.org/abs/2406.15275 (b12, b13, c06-c08, d06, d16)
- [V] Dedieu et al. (2024) Learning cognitive maps from transformer representations. https://arxiv.org/abs/2401.05946 (b14)
- [V] Baumgartner et al. (2025) Cognitive maps in language models: a mechanistic analysis. https://arxiv.org/abs/2511.13371 (b16, b17, c21, c22)
- [V] Qin, Cohen, Reddy (2026) Cognitive maps in large language models. https://arxiv.org/abs/2610.25596 (b18, d15)
- [V] Liu et al. (2026) MAP: map-then-act. https://arxiv.org/abs/2605.13037 (b21)
- [V] Yan (2025) External Hippocampus. https://arxiv.org/abs/2512.18190 (b22)
- [V] Ding et al. (2024) MANGO. https://arxiv.org/abs/2403.19913 (c18, c19)
- [V] Einarsson (2025) MazeEval. https://arxiv.org/abs/2507.20395 (c20)
- [V] Bugaud (2026) CheeseBench. https://arxiv.org/abs/2604.10825 (c23, c24)
- [V] Hao et al. (2023) Reasoning with language model is planning with world model (RAP). https://arxiv.org/abs/2305.14992 (c25)
- [V] Wang et al. (2026) GAVEL. https://arxiv.org/abs/2609.19315 (d01, d02)
- [V] Song and Cai (2026) Hybrid-WM. https://arxiv.org/abs/2606.27806 (d03, d04)
- [V] Li et al. (2026) GraphThink. https://arxiv.org/abs/2608.07905 (d05)
- [V] Wu, Zhao, Chen (2026) When is a steerable concept representation real? https://arxiv.org/abs/2608.08159 (d07)
- [V] Zhu et al. (2026) Mind over Space. https://arxiv.org/abs/2603.21577 (d08)

*Links to parallel subfields: Active inference vs RL; Map versus value replay; MDPs and POMDPs; Chain-of-thought prompting; Monte Carlo tree search; Pruning of decision trees; Distributed cognition. Not covered here.*

## Source audit (2026-11-03)

Fresh auditors re-opened the sources of 3 established claims: 3 confirmed as written, 0 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **B05.01-K03** (now single-source: only one opened source, code check).
- **B05.01-K11** (now single-source: only one opened source, code check).
- **B05.01-K19** (now single-source: only one opened source, code check).
- **B05.01-K20** (now single-source: only one opened source, code check).
- **B05.01-K32** (now single-source: only one opened source, code check).
