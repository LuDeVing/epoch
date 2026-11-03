# Transformational creativity: deep document

*Subfield C04.04. Boden's third type of creativity: changing the rules of the space. Written 2026-11-03 from evidence_a-d.jsonl (a01-a28, b01-b25, c01-c27, d01-d17), claims.jsonl (K01-K28) and critique.md. Evidence ids in brackets. Status marks: [E] established (two or more independent sources), [S] single source, [C] contested.*

*Honest summary up front: the theory is rich, the measurement is thin. No benchmark measures transformation directly (K04). Every LLM result below is a proxy from one author group with no replication. Nothing here should enter SCHEMA.md as established beyond what section 7 "Add now" lists.*

## 1. What it is

Margaret Boden split creativity into three types (a01, c21):

- **Combinational**: put familiar ideas together in a new way.
- **Exploratory**: search the corners of an existing conceptual space, using its rules.
- **Transformational**: change or drop a rule that defines the space, so that new ideas become possible that were impossible before. Her textbook cases are non-Euclidean geometry and the move from a stationary to a moving Earth.

She also split every idea into P-creative (new to the person or system that made it) and H-creative (new to history). Most machine "creativity" results are P-creativity only (a01, b01).

The core point for an agent: **a transformational move does not look for a better answer inside the frame. It edits the frame.** The frame can be a constraint (O4 drop a constraint), the representation (O6 change representation) or the goal itself (O8 reframe the goal). Our schema already names these three operators. This subfield asks what the research says about when they work, how to build them, and whether LLMs can do them.

What the field has settled is mostly vocabulary:

- Wiggins, Ritchie and Toivanen formalised the idea as meta-level search over the rules of the space (a02, a07, a27, a28, b21). All second-hand in our evidence.
- Two 2024-2025 formal papers prove properties of transformation (a03-a06, b20). Theory only.
- A handful of 2024-2026 LLM papers build proxies: OMEGA, T-UoT, EscapeBench, Bhushan's rubric (a11-a19, b01-b05, c01-c04).
- Three 2026 surveys and benchmarks state plainly that transformation is not measured (b08, b10, b18, b22).

## 2. History and theories in depth

### 2.1 Boden (1990 to 2004)

Boden's books (The Creative Mind 1990, second edition 2004; Computer Models of Creativity 1999) give the typology (a01, c21). We only saw them through citations (not opened, c21). Her key claims, as the opened sources repeat them:

- A conceptual space is defined by rules (style, constraints, a theory). Exploration uses the rules. Transformation changes one.
- The transformed space makes some ideas possible that could not have been generated before. Before the change those ideas were not just unlikely; they were outside the space.
- Boden died in July 2025 (a21).

### 2.2 Early machine systems

Lenat's AM and EURISKO (which changed its own heuristics), Cohen's AARON and Langley's BACON (which rediscovered laws) are the classic computer models (c22). **Not opened; unverified.** Treat as background only.

### 2.3 Wiggins' Creative Systems Framework (2006)

Wiggins gave Boden's idea a formal shape (Knowledge-Based Systems 19(7), 449-458) (a02, a28). As described by opened papers: a rule set R defines the conceptual space, a traversal strategy T moves through it, an evaluation E rates results. Exploration is search under R, T, E. **Transformation is search at the meta level over R, T or E.** Santo et al. note that CSF's value rule is binary (a28, a03). Primary text not retrieved.

Ritchie (2006) treats transformation as modification of the conceptual structure; Toivanen et al. (2018) built an architecture where meta-level modules change the constraints governing a song search space (a27, b21). Both second-hand.

### 2.4 DeLeNoX (Liapis et al., 2013, arXiv 2021): the first working loop

The first running system that alternates exploration and transformation (a08, a09, c19):

- Exploration: feasible-infeasible novelty search over CPPN-evolved spaceship sprites (49x49 pixels), 1000 ships per phase.
- Transformation: a denoising autoencoder with 64 hidden features is trained on the ships found so far (1000 epochs). Its features become the new distance measure for the next round of search. The criteria of search change, so the space changes.
- 6 iterations. A static run (features frozen from the first set) was the control.
- Result: in the transforming run the best diversity score for a feature set was usually reached on the next iteration's training set. The static run's features lost power as exploration drifted. The authors treat exploration and transformation as a matter of degree.
- Limit: diversity is measured by the system's own learned metric; no human rating (a08, a09).

### 2.5 Conceptual change in networks (Grachten and Chacon 2017)

Treats transformation as adapting a learned representation to a new task. On MNIST, natural images and classical music, adaptive strategies beat learning from scratch in training effort; for classification, keep first-layer filters and reset the rest (a10). Authors say no single strategy wins. Not applicable to a prompt-only agent (K22).

### 2.6 Formal learning theory (Espirito Santo, Wiggins, Cardoso 2024)

Uses Gold's formal learning theory. A conceptual space is a class of recursively enumerable sets; the agent is a "scientist" mapping data to hypotheses (a03, c20). Three results (a04, a05):

- **Theorem 1**: a novel artefact is not always transformative.
- **Theorem 2**: a transformative artefact is not always novel.
- **Theorem 3**: if the learner is set-driven (ignores data order), novelty IS necessary for transformation, because an artefact already in the inspiring set cannot change the hypothesis.

So novelty is the wrong test for transformation in general (K02). Proofs use toy learners and show logical possibility, not frequency.

### 2.7 Graphical theory of science (Schapiro, Black, Varshney 2025)

A conceptual space is a directed acyclic graph of constraints. Sink nodes are axioms; other nodes are rules that depend on axioms (a06, b20, c18). Transformative potential is the number of dependents. **Theorem 4: an edit to an axiom has the largest transformative potential**, proved by counting: if a rule R has a parent u, then |depends(u)| >= |depends(R)|+1, so the maximum is an axiom (d15). Illustrations: Ptolemaic to heliocentric, Euclidean to non-Euclidean, Newtonian to relativistic. Maps Boden onto Kuhn: normal science is exploratory or combinatorial; anomaly and crisis loosen rules; revolution is a new constraint configuration (a07).

Limits (d15): true by construction; says nothing about whether the edited space gives valid or useful results; real constraint sets are not clean DAGs; large impact may be breakage. Cases chosen after the fact.

### 2.8 Hyperpolation (Ord 2024)

Interpolation stays inside the data, extrapolation goes beyond along the same dimensions, **hyperpolation** estimates a function outside the subspace of the data, by altering, adding or deleting dimensions. Linked to Boden; argues current ML is weak at it (b17). No experiment.

### 2.9 The "LLMs cannot" camp

- Franceschelli and Musolesi (2023, v5 2025; a20, b19, c05): LLMs can reach value and weak novelty and surprise; transformation is out of reach under current training because models follow the training distribution and RLHF/DPO lowers diversity. Output looks creative through B-novelty (new to the beholder).
- Franceschelli and Musolesi (2026; b18): agents show functional creativity (interpolation and extrapolation), not transformation, which would need hyperpolation. Testing for it is "open and maybe unsolvable"; designing such a task is itself a transformational task. Suggests superspace extrapolation (Lucas, Sterling, Kemp 2012) as a possible test.
- Magrin-Chagnolleau (2026; a21): AI is capable in combinatorial, bounded in exploratory, fundamentally incapable of transformational creativity. Missing: chance, serendipity, a subject to recognise it.
- Ismayilzada et al. 2024 survey (c06): treats the topic in a few lines, calls for process-based evaluation.

These are assertions. None ran a test. Some predate reasoning models and scaffolds (K05 contested).

### 2.10 Benchmarks that cover the other two types

CreativeBench (b08, b09) covers only combinational and exploratory. AGC-Bench (b10) names transformation as not covered. KOMBINE (a22) is combinatorial and defers to TwistBench (not retrieved). Nagarajan et al. (a25) test combinational and exploratory tasks on small models. See section 5.

## 3. Core findings with exact numbers

Status: [E] established, [S] single source, [C] contested.

| Finding | Numbers | Source (evidence id) | Status |
|---|---|---|---|
| Novelty is neither necessary nor sufficient for transformation in general | Theorems 1-2; Theorem 3 only for set-driven learners | Santo, Wiggins, Cardoso 2024 (a04, a05) | [S] theory |
| Editing the most upstream constraint has the largest transformative potential | counting proof on a DAG; 3 historical cases; no validity test | Schapiro et al. 2025 (a06, b20, d15) | [S] theory |
| No benchmark measures transformation directly | AGC-Bench 78 datasets; CreativeBench 2 subsets (Combo, Explore); Bhushan 5-level rubric is the only one | b08, b10, b18, b22 | [E] |
| OMEGA: transformative items (new tactic needed) defeat frontier models and RL | base typically below 20 percent; OOD near 0 percent after RL on Qwen2.5-7B; only Setting 7 gains +10 pp; matrix rank OOD base 70 percent, fell 30 pp; in-domain +56 percent | Sun et al. 2025 (a15-a17, c01, d07) | [S] |
| Exploratory contrast in OMEGA: RL works | Zebra Logic base 30 percent, +61 in-distribution, +53 OOD | a16 | [S] |
| RLVR sharpens, does not widen | pass@1 on training set 26.1 to 42.5 while pass@256 fell; more rollouts (8 to 32) or higher temperature did not close the gap; hardest GSM8K items valid CoT: base 24/25, RL 23/25 | Yue et al. 2025 (c07, d08) | [S] |
| Distillation from a stronger teacher does widen pass@k | R1-Distill-Qwen-7B curve consistently above base and RL | d08 | [S] |
| T-UoT (rule-edit procedure) beats matched GPT-4o methods on 2 of 3 narrow tasks | Bridge human creativity 0.680 vs OnePrompt 0.480, CoT 0.590, ToT 0.580, EGoT 0.650; Electricity 0.620 vs 0.540 and 0.560; Society 0.550 vs EGoT 0.560. 10 generations per cell | Suzuki and Banaei-Kashani 2026 (a12, d17) | [S] |
| T-UoT on an independent hypothesis benchmark ranks near the bottom | Qwen3-14B, 100 tasks: E-UoT 1535.4 / 32.7 percent win, ToT 25.5, EGoT 25.3, CoT 18.8, C-UoT 19.5, T-UoT 1484.6 / 17.3 (6th of 7), OnePrompt 1475.7 / 14.3. Top-ranked on 11 of 100 tasks (6 uniquely) | a13, c03 | [S] |
| Backbone changes the ranking | GLM-4-9B: OnePrompt 1560.4 / 46.3 percent first; E-UoT 1542.1 / 40.7. Qwen3-14B: OnePrompt last | d04 | [S] |
| Removing rule transformation costs little; T-UoT is very expensive | ablation: full beats ablated 54.2 percent (chance 50); tokens per task OnePrompt 3.7k, CoT 3.5k, ToT 27.1k, E-UoT 36.7k, C-UoT 134.3k, T-UoT 193.3k (52.5x OnePrompt), 10-task audit | a14 | [S] |
| T-UoT failure has two causes | of 12 largest failures: 7 reasonable edit not converted, 5 weak or misaimed. Lexical stage signals do not separate wins from losses (transform applied 75 vs 83 percent; rule-to-final preservation 0.13 vs 0.16). Forced consequence step: rank 7 to 2.5 on one frozen case (+0.25 over chance 0.5), sister case 4 to 1.5 (+0.28); 4 seeds | c04, d01-d03 | [S] diagnostic |
| LLM judges rank rule-change methods only moderately consistently | pairwise Spearman 0.587-0.616 across three judges; hard flips 2.6-5.4 percent; human vs Gemini 2.5 Pro creativity r=0.708 (n=27 cells), novelty r=0.224 | d05 | [S] |
| Agents refine instead of abandoning a novel but poor approach | 92 episodes top-20 percent novelty and bottom-20 percent impact: 87.0 percent (80/92) REFINE; 53.8 percent of refined lost novelty next episode, median impact change 0.000; ABANDON 6.5 percent for low-impact vs 16.4 percent otherwise | Bhushan et al. 2026 (b03, b05) | [S] |
| Novelty change and score change are unrelated | Spearman: humans -0.111 (p<0.05), AIDE GPT-5 -0.021, AIDE Qwen +0.056, AIRA Qwen -0.026. Greedy, MCTS and evolutionary policies converge to P-creativity below 1 in a few episodes | b04, d14 | [S] |
| Rubric is reliable | 3 annotators, 300 episodes, Krippendorff alpha 0.724; GPT-5 judge vs humans Spearman 0.732 (0.684 without examples, 0.699 without edge rules, 0.712 without procedure) | b01, b02 | [S] |
| Judge beats embeddings on novelty | GLM-5 0.703, DeepSeek V3.2 0.700, Qwen3-235B 0.685, GPT-OSS-120B 0.544 vs embedding nearest-neighbour 0.637, centroid 0.589, graph edit -0.329 | b02 | [S] |
| GPT-5 H-creativity above gold-medal humans, but few runs reach it | 1.423 vs 0.744 (p<1e-15); Qwen configs 0.838, 0.800 (not different from gold). Only 21.25 percent of GPT-5 runs and 10.85 percent of Qwen runs | b04, d14 | [S] |
| LLM ideas more novel than expert ideas before execution | novelty 4.84 (SD 1.79) human, 5.64 (SD 1.76) AI, 5.81 (SD 1.66) AI plus human rerank; N=49 per condition; 79 reviewers, 298 unique reviews; p<0.05 corrected | Si et al. 2024 (b12, c09) | [E] with b14 |
| ...but lose novelty after execution | change in score after execution (1-10): human novelty -0.010, excitement +0.078, effectiveness -0.052; AI -1.049, -1.760, -1.879. 43 experts, over 100 hours each | Si et al. 2025 (b14, b23) | [E] across Si, Bhushan, InnoGym, CreativeBench (b23) |
| Overgeneration saturates | of 4000 seed ideas per topic, about 200 (5 percent) non-duplicate at cosine 0.8; share of non-duplicates kept falling | b13, c09 | [S] |
| LLMs give near-identical open answers | 79 percent of cases mean pairwise similarity above 0.8; min-p same-model pairs 81 percent above 0.7, 61.2 percent above 0.8; open-ended prompts 0.800 vs low-open 0.837 (42 models); 26K queries, 31,250 human annotations, 70+ models | Jiang et al. 2025 (b15, c08, c25) | [C] |
| Reanalysis of that claim | "river" in 80.5 percent of 750 responses, not two clusters; same-prompt pairs above 0.8 cosine 2-3 times as often as different-idea pairs (residual effect); prompt rewording beats baseline in all 12 topics, 25 of 30 sign tests at the floor p=2.4e-4, poet persona effective rank 17.4 to 28.9 (+66.1 percent); 15 models, 50 responses each | Schaeffer et al. 2026 (b16, d09, d10) | [C] |
| Alignment lowers diversity and creativity indices | CREATIVITY INDEX: human authors 66.2 percent higher than LLMs; RLHF lowers by 30.1 percent; aligned Llama-2 clusters more than base | Lu et al. 2025; Mohammadi 2024 (c11, c12, b19) | [E] |
| Asking for creativity moves scores far more than reasoning mode | "be creative" vs "be effective" 18 models dz +1.40 (length-residualised), 99.4 percent of 2,700 generations valid; reasoning on, 10 other models dz +0.34 | Beaty et al. 2026 (b11) | [E] with b07, b09 |
| Mid-range temperature trades gain for novelty | best at 0.5-0.75, 3 runs; gain highest at low temperature | InnoGym (b07) | [S] |
| Temperature weakly linked to novelty | weak positive with novelty, moderate negative with coherence | Peeperkorn et al. 2024 (d12) | [S] |
| Verbalized sampling raises diversity above temperature | diversity 1.6-2.1x over direct; recovers 66.8 percent of base-model diversity; 90 annotators: poem 1.90 to 2.39, story 2.74 to 3.06, joke 1.83 to 3.01 (sequence 2.93) | Zhang et al. 2026 (d11) | [S] |
| Scaling helps correctness and combination, not exploration or novelty | Pass@1 rises with scale while novelty falls or plateaus; reasoning helps exploration, not combination; steering vector EvoRePE: Combo 0.174 to 0.192 | CreativeBench (b09) | [S] |
| One general creativity factor | factor C explains 81.5 percent of variance, omega 0.96; correlation with fluid reasoning 0.55 (n=82), MMLU-Pro 0.62 (n=57); 83 LLMs, 3,101 papers screened, 497 benchmarks, 78 datasets; parameters vs composite rho 0.69 (42 open models) | AGC-Bench (b10) | [S] |
| Open-ended exploration is poor in LLMs | Little Alchemy 2, 500 trials: Llama3.1-8B 9, 70B 25, GPT-4o 35, R1 85, o1 177, humans 42 (29,493 humans, 4,691,033 trials). GPT-4o with CoT, reflection, hints: mean 43, p=0.304 | Pan et al. 2025 (c14, c26) | [S] |
| Unconventional tool use: scaffolds help | EscapeBench GPT-4o 7.17 hints / 593.9 steps to 5.00 / 452.0 with Foresight+Reflection; Llama-3.1-70B 14.67/981 to 7.17/625. Base models reach ~15 percent progress without hints, up to 10x optimal steps | Qian et al. 2025 (a18, a19, d13) | [S] |
| MacGyver | 1,683 problems; GPT-4 73.3 vs humans 79.3 percent (323-problem sample); errors: wrong tool use 42.4, goal not achieved 17.7, unavailable tools 16.9, unfaithful to constraints 9.5; 78 percent solvable | Tian et al. 2024 (c13, c27) | [S] |
| Searching the agent's own design space works | ADAS: DROP F1 +13.6, MGSM +14.4 percent, GSM8K +25.9 percent and GSM-Hard +13.2 percent transferred. DGM: SWE-bench 20.0 to 50.0 percent, Polyglot 14.2 to 30.7 percent; lower without self-improvement or archive | Hu et al. 2025; Zhang et al. 2026 (c15, c16) | [E] |
| Automated creativity tests do not validate for LLM science ideation | DRAT only significant predictor; DAT best for writing | Schapiro et al. 2026 (a23) | [E] with b10 |
| Human experts still ahead on stories | New Yorker stories pass 84.7 percent of 14 Torrance tests (11.9); LLM stories 3 to 10 times less likely to pass each; ChatGPT/Claude pass 9-30 percent | Chakrabarty et al. 2024 (c10) | [S] 2023 models |
| Baba Is AI: composing new rule operations fails | GPT-4o perfect on first four distractor settings; all models drop on object-plus-rule distractor and on novel composition break-make-goto | Cloos et al. 2024 (d06) | [S] 2024 models |
| InnoGym: no agent beats the best human solution | 18 tasks, 3 frameworks; none beat the best on any task; novelty often without gain; CirclePacking Gemini-2.5-Pro 2.49, GPT-5 2.44, DeepSeek-v3.1 2.40, AlphaEvolve 2.65 | b06, b07 | [S] |
| OMNI-EPIC: LLM proposes new tasks | higher task-cell coverage (3 sim runs) and ANNECS-OMNI (5 RL runs), p<0.05 | Faldor et al. 2025 (c17) | [S] |

## 4. Mechanisms and models

Each model below is written so an engineer can build it.

### 4.1 Wiggins CSF as a three-slot program

State: R (rules of the space: a predicate "is this in the space"), T (how to move), E (how to rate). Exploration loop: propose by T, keep if R holds and rate by E. **Transformation = a second loop that edits R, T or E**, then restarts exploration. In an agent: R is the list of constraints extracted from the task, T is the generation prompt or search policy, E is the check. The edit target decides the operator: edit R is O4, edit the representation that R is stated in is O6, edit E or the goal is O8. (K01.)

### 4.2 DeLeNoX loop (alternate explore and transform)

1. Explore: run novelty search on the current feature set, collect N solutions (1000 sprites).
2. Transform: train a model on the collected set to learn new features (64 hidden features, denoising autoencoder).
3. Redefine "distance" through those features, go to 1.

Agent analogue (K21): after an exploration batch, extract features of the solutions found so far (what they share) and instruct the next batch to differ on a feature not yet varied. Feature extraction and the history belong in code, not in the model's judgement. Untested on LLMs. The only evidence is the system's own diversity metric (a09).

### 4.3 T-UoT: rule transformation (the one LLM implementation)

Algorithm (a11, c02):
1. EXTRACTRULES: the LLM splits the problem into mutable rules and immutable requirements H (supplied by the task).
2. GENERATETRANSFORMATIONS: k=5 edits per problem. Edit types: remove, relax, invert, add, replace.
3. Gate: three binary flags b_goal (goal preserved), b_diff (core difficulty preserved), b_space (a new region is opened). Keep an edit only if it passes (soft threshold default 2).
4. REFRAME(P, R): rewrite the problem under the chosen edit.
5. CREATIVESEARCH under the new frame; the LLM scores and votes.

Weakness: the gate and the selection are LLM-judged (conflicts with G4/G8). Consequences of the edit are not carried into the answer. Fix (diagnostic only): after the edit, force one derived mechanistic consequence and require it in the output (c04, d03). Implementable version: the program asserts that the final answer cites the derived consequence, and a code check tests it.

### 4.4 Dependency-graph rule picker (Schapiro)

Build the constraint graph for the task: nodes are constraints, edges are "B depends on A". Score each constraint by number of dependents. For O4 pick the highest-scoring first (potentially most transformative); also the riskiest, since it breaks the most. Combine with a validity check after the edit. Untested (K03). Requires an agent-built graph; the cost of building it is part of the test.

### 4.5 Bhushan's five-level rubric (a measurement tool)

Score each agent step 0 Routine to 4 Transformational. Level 4 is a change of representation, objective, modality or task definition. Score is relative to the agent's own prior episodes (P-creativity) and to a public Kaggle corpus (H-creativity) (b01, b04). A judge sees all prior episodes, so cost grows with run length (b02). Usable as a log, not as a control signal (G5, G8).

### 4.6 Foresight and Reflection (EscapeAgent)

Foresight: before acting, propose unconventional uses of the available objects and check them against the state. Reflection: keep a task list of unsolved sub-tasks. Both are prompt-level modules; each alone gives about half the gain (a19, d13). A hypothesis-check-before-act step is the part that maps to O6/O8.

### 4.7 Search over the agent itself (ADAS, DGM, OMNI-EPIC)

A meta agent writes new agent code into a growing archive, tests it, and keeps variants (c15, c16). OMNI-EPIC uses an LLM to propose the next task and writes its environment code, filtered by an interestingness model (c17). This is transformation of the agent's own rules. Cost: it needs a benchmark with an objective score, a sandbox, and many runs. For us it is an offline schema-tuning method, not an in-run operator (K20).

### 4.8 Diagnosing transformation by pass@k

Yue et al. give a clean test: if a method produces correct solutions the base model never produces at any k, it widens the space; otherwise it only sharpens (c07, d08). Use pass@k curves to credit a transformation scaffold (K07).

## 5. What holds up

### 5.1 Established

1. **Nobody measures transformation directly.** Four independent sources agree (b08, b10, b18, b22, a26). Any claim that an LLM does or does not do it is untested.
2. **Novelty without execution does not make value.** Si 2024 and 2025, Bhushan 2026, InnoGym 2026 and CreativeBench 2026 agree (b23). AI ideas lose 1.05-1.88 points after execution; humans lose about 0.
3. **Cheap prompt levers move novelty.** Asking for creativity (dz +1.40) and mid temperature (0.5-0.75) beat turning on reasoning (dz +0.34) (b11, b07, b09, b24).
4. **Alignment narrows diversity.** Three sources (c11, c12, b19).
5. **Searching over the agent's own design works when a score exists.** ADAS and DGM (c15, c16).
6. **Automatic creativity tests such as DAT and RAT are not valid gauges of LLM scientific ideation** (a23, a22).

### 5.2 Failures and boundary conditions

- **T-UoT does not generalise.** Strong on 10 generations over 3 self-built tasks; 6th of 7 on 100 independent tasks; backbone flips the ranking; cost is 52.5x the plain prompt (a12-a14, d04). The ablation margin is 54.2 percent against a 50 percent chance line.
- **OMEGA's RL result is about training, not prompting.** RL on the familiar tactic did not teach the new one. Nobody tried an O6 prompt on frontier models (K06, d07). The RL used Qwen 7B only.
- **RL narrows.** Pass@1 up, pass@256 down. A better selector is not a wider space (c07).
- **Search policy does not matter much.** Greedy, MCTS and evolutionary agents converge to the same low novelty in a few episodes (d14). The scaffold, not the policy, is the likely lever, but no intervention arm exists.
- **Prompt hints failed in exploration.** Little Alchemy 2 hint prompts: p=0.304 (c14). MacGyver reflection helped GPT-4 only; on Llama2 it blindly flipped the first answer every time (c27).
- **Tiny samples.** T-UoT human ratings: 10 generations per cell, no intervals (a12). EscapeBench: single run averages, same benchmark for design and test (a19).

### 5.3 Contested

- **Hivemind.** The original: models fall into the same clusters; inference fixes are inadequate (b15, c08). The reanalysis: the flagship example does not hold (80.5 percent single vehicle), the null was too weak, prompting raises diversity; but a residual same-prompt effect 2-3 times the null survives (b16, d09, d10). One author group on each side. [C]
- **Can LLMs do it at all?** Position papers say no (a20, a21, b18); T-UoT and EscapeAgent show small gains on narrow tasks. Nobody ran the direct test. [C]
- **Does reasoning help creativity?** AGC-Bench: little (dz +0.34). CreativeBench: helps exploration, not combination. Different tasks.

### 5.4 Moderators found

Backbone model (d04); task constraint level (low-constraint tasks favour T-UoT, d17); model size (helps correctness, not novelty, b09); alignment (c11); whether a check exists (Si, Bhushan); math-only template tasks (OMEGA).

### 5.5 Interventions that worked and did not

Worked (small, single-source unless noted): asking for creativity [E]; mid temperature [S]; verbalized sampling [S]; prompt rewording to anti-modal or persona [S]; Foresight+Reflection [S]; forcing a derived consequence [S, one case]; distillation widens pass@k [S].

Did not work: RL on the familiar tactic (OMEGA); hint prompts in Little Alchemy; reasoning mode on combination tasks; blind self-reflection on Llama2 MacGyver; temperature alone for novelty (weak link, d12); sampling more (5 percent non-duplicates).

## 6. Language models

**How they behave.**

- **Novel on paper, not in use.** Blind experts rated AI ideas 5.64 vs 4.84 on novelty before execution. After execution the AI ideas dropped 1.05 novelty points; human ideas dropped 0.01 (b12, b14).
- **Narrow output.** 4000 seeds gave about 200 distinct ideas (b13). Hivemind reports high similarity across models (b15, c08); the reanalysis weakens but does not remove this (d09).
- **Cannot step outside a tactic.** On OMEGA transformative items, base accuracy is typically under 20 percent; frontier reasoning models degrade with complexity and show early solutions followed by long overthinking (a16, a17).
- **Refine, do not abandon.** 87.0 percent of poor-but-novel episodes got refined (b05). Only 6.5 percent abandoned when impact was low.
- **Explore poorly in open worlds.** Little Alchemy 2: only o1 (177) beats humans (42); GPT-4o 35 (c14). R1 shows human-like cycles of analysis but tries more failed combinations (c26).
- **Tool repurposing near human level.** GPT-4 73.3 vs 79.3 percent; most errors are wrong tool use (c13).
- **Right frame, lost consequences.** T-UoT finds reasonable rule edits but does not carry the consequences into the answer (7 of 12 failures, c04, d01).

**What changed behaviour, by how much.**

| Lever | Effect | Source | Status |
|---|---|---|---|
| Ask "be creative" | dz +1.40 | b11 | [E] |
| Reasoning mode | dz +0.34, none on combination | b11, b09 | [E] |
| Temperature 0.5-0.75 | best trade; weak link to novelty | b07, d12 | [S] |
| Verbalized sampling | diversity x1.6-2.1; joke 1.83 to 3.01 | d11 | [S] |
| Prompt reword (anti-modal, persona) | effective rank +66.1 percent (poet persona) | d10 | [S] |
| Foresight+Reflection | GPT-4o steps 593.9 to 452.0 | a19 | [S] |
| Forced consequence step | rank 7 to 2.5 (one case) | d03 | [S] |
| Rule-edit scaffold (T-UoT) | +0.03 to +0.2 on 0-1 scale (3 tasks); 17.3 vs 14.3 percent win on 100 tasks; 52.5x tokens | a12, a13, a14 | [S] |
| RL (RLVR) | pass@1 26.1 to 42.5, pass@256 down | c07 | [S] |
| Model scaling | correctness up, novelty flat | b09 | [S] |
| Alignment (RLHF) | CREATIVITY INDEX -30.1 percent | c11 | [E] |
| Bigger judge | tracks humans better | b02 | [S] |

**Judging problem.** Most of these results are scored by LLM judges. Judges agree only moderately (0.587-0.616 Spearman), flip 2.6-5.4 percent of hard A/B calls, and track human creativity at r=0.708 but human novelty at only r=0.224 at the cell level (d05). GPT-5 as judge matched humans at 0.732 on the rubric (b01). Our guardrail G8 (novelty judged by running) stands; no study here replaced the LLM judge by execution.

## 7. What our agent should take

Schema parts: G guardrail, S state, O operator, memory. Evidence ids in brackets.

### Add now (established [E])

| # | Item | Part | Status | Evidence |
|---|---|---|---|---|
| A1 | Keep G8 as is: novelty is judged by running. Pre-execution novelty ratings are not value (AI ideas lose 1.05-1.88 points after execution). | G8 | [E] | b12, b14, b23, K12 |
| A2 | In any open-mode comparison include controls: a plain "be creative" prompt and a temperature arm; a new operator must beat both at equal tokens. | G7 | [E] | b11, b07, b09, K16 |
| A3 | Do not use DAT, RAT or embedding diversity alone as an agent-quality gauge. Use execution outcome. | G8 | [E] | a23, a22, K23 |
| A4 | Label every agent edit in the logs as O4 (drop a rule), O6 (change representation) or O8 (reframe goal), using Bhushan-style levels. Log only; no decision depends on it. | log (SCHEMA section 6) | [E] vocabulary | K01, a03, a06, b01 |
| A5 | Keep G4 and G12: more samples saturate (5 percent non-duplicates); do not rely on resampling for new frames. | G4, G12 | [E] in SCHEMA (F05); single here | b13, K13 |
| A6 | Do not use position-paper claims ("LLMs cannot do transformation") as a reason to remove O4/O6/O8: they are untested. | doc | [E] on the absence of tests | K04, K05 |

### Test first ([S] or [C])

| # | Item | Part | Status | Evidence |
|---|---|---|---|---|
| T1 | After an O4/O8 edit, require a derived consequence step, checked by code against the final answer. | O4, O8, S5 | [S] | c04, d01-d03, K09 |
| T2 | O4 aimed at the constraint with most dependents (Schapiro) vs a random constraint. | O4 | [S] theory | a06, d15, K03 |
| T3 | O6 representation change on OMEGA-style transformative items for prompted frontier models. | O6 | [S] | a16, d07, K06 |
| T4 | Impasse-triggered reframe after a flat score (agents refine 87.0 percent, abandon 6.5 percent). | G1, S6, O8 | [S] | b05, d14, K11, K28 |
| T5 | Anti-modal reframe vs temperature vs verbalized sampling for frame diversity. | S3 open mode | [C] | d10, d11, b16, K14, K27 |
| T6 | Hypothesis-check-before-act step (Foresight) in agent tasks. | O6, O8 | [S] | a19, d13, K10 |
| T7 | Pass@k test: does a rule-change scaffold solve items plain sampling at k=N never solves? | G12 | [S] | c07, d08, K07 |
| T8 | Replace the LLM scorer by a code/constraint checker in a T-UoT-style gate. | G5, G8 | [S] | d05, K25 |
| T9 | Base-model sampling for O4 branches (alignment narrows). | S3 | [E] background; untested as operator | c11, c12, K15 |
| T10 | Search over schema settings offline (ADAS style), counted in setup cost. | memory, G7 | [E] gains; not single-agent | c15, c16, K20 |

## 8. Concrete tests on our bench

All arms at equal tokens (G7); setup tokens counted. Judge by code where a check exists; an LLM judge is a secondary column only (G5, G8).

| Test | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| B1 Consequence step | constraint-relaxation puzzles with a code check (Baba Is AI composition splits; hand-built items where the familiar tactic fails) | plain; best-of-N; O4 edit; O4 + forced consequence step | valid-solution rate on unfitted checks | O4+consequence above O4; both above plain only where the familiar frame fails. Small gain expected (rank effect 7 to 2.5 on one case) |
| B2 O6 on OMEGA | OMEGA transformative split (7 categories), 100 samples per level | plain; "be creative"; O6 (symmetry, substitution); best-of-N | exact-match accuracy; pass@k up to 32 | O6 above plain from a base under 20 percent; credit as widening only if pass@k rises |
| B3 Upstream constraint | tasks with a stated constraint list and a code-checked validity | O4 on random constraint; O4 on highest-dependent constraint (agent builds the graph; cost counted) | valid new solutions per token | high-dependency edit gives more new valid solutions, and more invalid ones |
| B4 Impasse reframe | score-per-episode tasks (MLE-Bench style, our ARC and puzzle suites) | no trigger; trigger on flat score for 2 rounds then O8; trigger on schedule (G1 control) | final score; abandon rate on low-impact novel episodes | signal trigger above schedule; abandon rate rises from 6.5 toward 16 percent without score loss |
| B5 Frame diversity | open prompts, embedding plus frame label, matched same-prompt null | plain; temperature 0.5-0.75; verbalized sampling; anti-modal reframe | distinct frames per 100 samples; quality by check where available | anti-modal and VS above temperature; effective-rank gains of tens of percent; quality must be reported |
| B6 Foresight | tool-repurposing items (MacGyver style) or small room-escape games | plain; Foresight; Foresight + Reflection; best-of-N | steps and hints to success; success rate | steps down 20-36 percent as in EscapeBench; may not replicate |
| B7 Pass@k widening | any code-checked set where plain fails | plain at k=32; each scaffold at matched tokens | solved-at-any-k | widening only if the scaffold solves items plain never solves |
| B8 Selector swap | rule-edit tasks with a held-out test | LLM scorer; constraint or execution selector; random | selected candidate pass rate | execution selector at least equals LLM scorer at lower cost |
| B9 Execution gap | ideas with executable tests (small coding or analysis tasks) | rank by LLM novelty; rank by execution result | final score of top-3 | execution ranking wins (the Si finding in small) |
| B10 Base vs instruct | open-mode generation | instruct backbone; base backbone with same few-shot frame | distinct frames; check pass rate | base wider, lower validity |

## 9. What does not transfer, and why

- **Theory papers (Wiggins, Santo, Schapiro, Ord).** Give vocabulary and a picking rule; no evidence an agent gains. The DAG theorem is true by counting and says nothing about validity (d15).
- **Historical transformation (Copernicus, non-Euclidean geometry).** Needs years, a community and a changed value system. Our agent has one problem and a budget. Bhushan's level 4 is relative to the agent's history, not a real rule change (critique).
- **DeLeNoX and CNN conceptual change.** Need a trainable representation and a numeric feature space. A prompt-only agent cannot train an autoencoder; only the loop idea transfers (a08, a10).
- **OMEGA's RL result.** A fine-tuning study on Qwen 7B. It says nothing about prompt scaffolds on frontier models (a16).
- **ADAS and DGM.** Gains need an objective score, a sandbox and many runs. Offline tuning, not an in-run operator (c15, c16).
- **T-UoT as built.** 52.5x the tokens of a plain prompt; self-judging; violates G4/G8 as designed (a14, a11).
- **Hivemind clustering metrics.** Embedding similarity measures wording, not whether the frame changed (b15, c25).
- **Creative-writing results (verbalized sampling, Torrance tests, CREATIVITY INDEX, Pron vs Prompt).** Measure style or rarity of wording, not a rule change (c10, c11, a24, d11).
- **Little Alchemy 2 and escape games.** Explicit finite rules; closer to exploration than to Boden transformation. Game text may be in training data (a18, c14).
- **Position-paper claims.** Asserted, not tested; some predate reasoning models (a20, b19).

## 10. Open questions

1. Does O4 or O8 beat a plain "be creative" prompt, a temperature sweep and best-of-N at equal tokens on a code-checked task? No study has this control.
2. Is the T-UoT null caused by the rule edit or by failing to propagate its consequence? One diagnostic on 12 failures says both.
3. Does O6 rescue OMEGA transformative items for prompted frontier models?
4. Does a scaffold widen pass@k, or only sharpen like RL?
5. Does Hivemind homogeneity survive a matched null, and does a frame-change instruction beat temperature?
6. Do edits to high-dependency constraints yield more valid new solutions than random edits?
7. What triggers abandoning a novel but poor approach?
8. Is there a verifiable benchmark of real rule-change problems where the familiar frame provably fails? TwistBench and Spark were not retrieved.
9. Do EscapeAgent's gains replicate on another environment at equal tokens?
10. Can an execution or constraint selector replace the LLM scorer?
11. Is transformation separable from deep exploration in practice? DeLeNoX's authors call it a matter of degree (a09).
12. Does the Boden typology matter for LLMs at all, or is one general creativity factor enough (AGC-Bench factor C, 81.5 percent of variance, b10)?

## 11. Sources

[V] = opened (full text or page read in this series); [M] = snippet or citation only.

1. [V] Wikipedia, Computational creativity. https://en.wikipedia.org/wiki/Computational_creativity (a01, a02)
2. [M] Boden, The Creative Mind (1990/2004); Computer Models of Creativity (1999), via https://en.wikipedia.org/wiki/Margaret_A._Boden (c21)
3. [M] Wiggins (2006) A Preliminary Framework for Description, Analysis and Comparison of Creative Systems. Knowledge-Based Systems 19(7). Second-hand (a02, a28)
4. [M] Ritchie (2006); Toivanen et al. (2018). Second-hand via https://arxiv.org/abs/2504.18687 (a27, b21)
5. [M] Lenat AM/EURISKO; Cohen AARON; Langley BACON (c22). https://en.wikipedia.org/wiki/Margaret_A._Boden
6. [V] Espirito Santo, Wiggins, Cardoso (2024) Towards a Formal Creativity Theory. https://arxiv.org/abs/2405.02148
7. [V] Schapiro, Black, Varshney (2025) Transformational Creativity in Science: A Graphical Theory. https://arxiv.org/abs/2504.18687 ; ICCC copy https://computationalcreativity.net/iccc25/papers/iccc25-schapiro2025transformational.pdf
8. [V] Liapis, Martinez, Togelius, Yannakakis, Transforming Exploratory Creativity with DeLeNoX. https://arxiv.org/abs/2103.11715
9. [V] Grachten, Chacon (2017) Strategies for Conceptual Change in CNNs. https://arxiv.org/abs/1711.01634
10. [V] Suzuki, Banaei-Kashani (2026) Universe of Thoughts. https://arxiv.org/abs/2511.20471
11. [V] Sun et al. (2025) OMEGA. https://arxiv.org/abs/2506.18880
12. [V] Qian et al. (2025) EscapeBench. https://arxiv.org/abs/2412.13549
13. [V] Franceschelli, Musolesi, On the Creativity of Large Language Models. https://arxiv.org/abs/2304.00008
14. [V] Franceschelli, Musolesi (2026) On the Creativity of AI Agents. https://arxiv.org/abs/2604.13242
15. [V] Magrin-Chagnolleau (2026) Can an AI System Be Creative? https://arxiv.org/abs/2607.20796
16. [V] Schapiro et al. (2026) KOMBINE. https://arxiv.org/abs/2509.21043
17. [V] Schapiro et al. (2026) Assessing the Creativity of LLMs. https://arxiv.org/abs/2605.13450
18. [V] Marco, Gonzalo, Mateo (2024) Pron vs Prompt (results tables not read). https://arxiv.org/abs/2407.01119
19. [V] Nagarajan et al. (2025) Roll the dice and look before you leap (abstract-level numbers). https://arxiv.org/abs/2504.15266
20. [V] Bhushan, Zhang, Wang (2026) Can LLM Agents Discover? https://arxiv.org/abs/2608.30047
21. [V] Zhang et al. (2026) InnoGym. https://arxiv.org/abs/2512.01822
22. [V] Wang et al. (2026) CreativeBench. https://arxiv.org/abs/2603.11863
23. [V] Beaty et al. (2026) AGC-Bench. https://arxiv.org/abs/2607.01152
24. [V] Si, Yang, Hashimoto (2024) Can LLMs Generate Novel Research Ideas? https://arxiv.org/abs/2409.04109
25. [V] Si, Hashimoto, Yang (2025) The Ideation-Execution Gap. https://arxiv.org/abs/2506.20803
26. [V] Jiang et al. (2025) Artificial Hivemind. https://arxiv.org/abs/2510.22954
27. [V] Schaeffer et al. (2026) How Strong Is the Evidence for the Artificial Hivemind? https://arxiv.org/abs/2609.33936
28. [V] Ord (2024) Interpolation, Extrapolation, Hyperpolation. https://arxiv.org/abs/2409.05513
29. [V] Ismayilzada et al. (2024) Creativity in AI: Progresses and Challenges. https://arxiv.org/abs/2410.17218
30. [V] Yue et al. (2025) Does RL Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model? https://arxiv.org/abs/2504.13837
31. [V] Chakrabarty et al. (2024) Art or Artifice? https://arxiv.org/abs/2309.14556
32. [V] Lu et al. (2025) AI as Humanity's Salieri. https://arxiv.org/abs/2410.04265
33. [V] Mohammadi (2024) Creativity Has Left the Chat. https://arxiv.org/abs/2406.05587
34. [V] Tian et al. (2024) MacGyver. https://arxiv.org/abs/2311.09682
35. [V] Pan, Xie, Wilson (2025) LLMs Think Too Fast To Explore Effectively. https://arxiv.org/abs/2501.18009
36. [V] Hu, Lu, Clune (2025) ADAS. https://arxiv.org/abs/2408.08435
37. [V] Zhang et al. (2026) Darwin Godel Machine. https://arxiv.org/abs/2505.22954
38. [V] Faldor et al. (2025) OMNI-EPIC. https://arxiv.org/abs/2405.15568
39. [V] Cloos et al. (2024) Baba Is AI. https://arxiv.org/abs/2407.13729
40. [V] Zhang et al. (2026) Verbalized Sampling. https://arxiv.org/abs/2510.01171
41. [V] Peeperkorn et al. (2024) Is temperature the creativity parameter of LLMs? https://arxiv.org/abs/2405.00492
42. [M] TwistBench and Spark (not retrieved; named in a22, d16)

Note: critique.md re-checked eight papers (Si 2025, Yue, Pan, Jiang, Suzuki, Bhushan, OMEGA, Si 2024) against full PDF text; numbers above for those match. Corrections applied: Si 2024 novelty is p<0.05 (corrected); 4000 seeds is per topic; the Hivemind 79 percent and 61.2/81 percent figures are different statistics and are not merged. Not re-opened: Beaty AGC-Bench, CreativeBench, InnoGym, Chakrabarty, Lu, MacGyver, DGM, ADAS numbers (single reads).
