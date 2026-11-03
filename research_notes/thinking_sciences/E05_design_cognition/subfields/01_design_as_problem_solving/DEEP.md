# Design as problem solving: deep document

*Subfield E05.01. Focus: search in ill-structured spaces. Key works: Simon 1969 and 1973; Newell and Simon 1972. Schema link: S6 (impasse and operator tree), background for S0 and G12. Built from evidence_a-d.jsonl (ids a01-a25, b01-b26, c01-c25, d01-d17), claims.jsonl (K01-K32) and critique.md. Sources marked [V] were opened as full text; [M] means snippet, abstract or memory only. Where a number was not read, it is not given.*

## 1. What it is

Design as problem solving is the view that designing is search through a problem space. A problem space has states, operators that move between states, and a test for the goal. The view comes from Newell and Simon (1972) and Simon (1969, 1973). The question for us is narrow. When the task is open, with no single right answer, does the same search machinery still apply? And does an LLM agent gain from running that search in code?

Three terms matter.

- **Well-structured problem (WSP).** Simon (1973) lists six criteria [V, a01]: a definite, mechanical test of any proposed solution; a problem space holding the initial, goal and all reachable states; legal moves as state transitions; all acquirable knowledge representable in the space; state changes that mirror real-world laws; practicable computation. An **ill-structured problem (ISP)** is a residual category: anything that fails one or more of these.
- **Wicked problem.** Rittel and Webber (1973) [M, a10] give ten properties: no definitive formulation, no stopping rule, solutions are good or bad (not true or false), no immediate or ultimate test, every attempt counts, no enumerable set of solutions. This is a rival framing that says design is a different kind of thing.
- **Co-evolution.** Dorst and Cross (2001) [M, a12, b07] studied nine industrial designers. Problem and solution spaces develop together. A creative event is a "bridge" that pairs a framing with a partial solution.

The core dispute has two sides.

1. **Simon (1973): no new process is needed.** An ISP is handled by ordinary search plus memory retrieval, applied to a locally well-structured sub-problem at each moment [V, a02, a05, a07].
2. **Design-specific accounts** (Rittel and Webber; Goel and Pirolli 1992; Dorst and Cross 2001): design spaces differ in kind and need problem framing as a first-class move [M, a10, a11, a12].

Neither side has a direct LLM test. What exists is a body of LLM search work (Tree of Thoughts, RAP, LATS, tree search for web agents) that explicitly cites Newell and Simon, plus a smaller body on LLM design fixation and diversity. Almost all search gains are on tasks with a crisp checker. That gap is the main risk to S6 (K25).

## 2. History and theories in depth

**Newell, Shaw and Simon (1958) and Newell and Simon (1972) [M, a08, c21].** Problem solving is heuristic search through a problem space. The General Problem Solver (GPS) used means-ends analysis: compare current state with goal, find the difference, pick an operator that reduces it. Evidence came from think-aloud protocols in cryptarithmetic, logic and chess. Newell and Simon (1976) stated the heuristic search hypothesis: a physical symbol system solves problems by generating and modifying symbol structures until a solution appears. We did not open this book and give no figures from it. ToT cites it as its own framing [V, a24].

**Reitman (1964, 1965) [M, a09].** First extended treatment of ill-defined problems. One composer's think-aloud protocol while writing a fugue. Few constraints are given; some are "open" and get filled in during the work. Known here only through Simon 1973.

**Simon (1969), The Sciences of the Artificial [M, c22].** Design is satisficing search, not optimising. The designer builds a well-structured sub-problem from what memory supplies and searches that. Not opened.

**Simon (1973), The structure of ill structured problems [V, a01-a07].** The key paper; read in full.

- The boundary is vague and relative to the solver (a01). A problem is ill-structured when the solver lacks the power or resources to treat it as well-structured.
- Even theorem proving and chess are not truly well-structured. The solver may want illegal moves, metalanguage or analogy from another space (a03). If new resources may "occur" during solving, the problem is ill-structured.
- Strong form (a04): there are no WSPs, only ISPs that have been formalised. Much effort goes into structuring the problem, a fraction into solving it.
- Architect model (a05, from Reitman): a design starts from a few open constraints. The task evokes attributes, sub-goals, requirements and alternative generators from long-term memory. The whole decomposes (house to floor plan plus structure, and so on). Each step works on a small immediate problem space that is well-structured.
- Why it looks ill-structured (a07): the solver is serial and long-term memory is huge. Most of memory is irrelevant over a short interval and must be evoked on recognition. The apparent change of the problem space is retrieval, not new reasoning.
- Predicted failures (a06): sub-solution interactions are neglected; earlier solutions are undone when new aspects are attended to; criteria never evoked stay dormant; the final design depends on the order of steps. Named mitigations: split the task into near self-contained components; set global parameters early.
- No experiment. Written before LLMs; assumes a serial symbolic processor.

**Rittel and Webber (1973) [M, a10].** The fetched PDF was a scan with no text layer. The ten properties come from background knowledge. Key contrast with Simon: no stopping rule and no test, so "solved" cannot be defined by a goal test.

**Goel and Pirolli (1992) [M, a11, c23].** Design problem space hypothesis: design spaces share invariant features across domains and differ from non-design spaces. They derived 12 invariants and tested them on protocols from several design domains. Only abstract-level facts seen.

**Dorst and Cross (2001) [M, a12, b07].** Nine experienced industrial designers. Problem and solution spaces co-evolve. Adds default and surprise spaces. A later scoping review (Biskjaer et al. 2026; abstract page opened, b08) covers 16 DRS conference papers from 2001-2025. The model is mostly used to link design theories. The authors ask for it to be tied to the psychology of problem construction.

**Kruger and Cross (2006) [M, b06].** Protocol analysis sorted designers into problem-driven, solution-driven, information-driven and knowledge-driven strategies. Solution-driven designers scored lower on overall quality but higher on creativity. Problem-driven designers gave the best balance. Sample size and scores not seen.

**Design fixation (Jansson and Smith 1991) [M, b04].** Designers shown example solutions repeated the example's features, even when told to avoid them. Tasks: car-mounted bicycle rack, measuring cup for the blind, spill-proof coffee cup. Numbers of the 1991 study not seen. Neroni et al. (2017) rebuilt the effect with an objective task (section 3).

**Sio, Kotovsky and Cagan (2015) [M, b05].** Meta-analysis of 43 studies on examples in design. Examples cut variety of ideas but raise novelty and quality. Effects on novelty and quality were larger with fewer and less common examples. One uncommon example helped most. Pooled effect sizes not seen (paywall).

**The LLM turn, 2022-2026.** Four threads.

1. Search scaffolds that cite Newell and Simon: ToT, RAP, LATS, tree search for web agents, a Sudoku controller.
2. Planning critiques (PlanBench, LLM-Modulo): LLMs plan poorly alone but work paired with an external verifier.
3. Test-time compute studies (Snell, Wu, Brown, Shojaee): which search wins, and at what token cost.
4. Design-specific LLM studies: fixation, diversity, hackathon, reframing, engineering design benchmarks.

## 3. Core findings with exact numbers

Status: established = two or more independent sources agree; single-source; contested. K-ids refer to claims.jsonl.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| ISP is a residual category defined relative to the solver | Six WSP criteria; boundary moves with solver power | Simon 1973 [V] (a01) | single-source (conceptual), K01 |
| No new process needed for ISPs: search plus retrieval on a locally well-structured sub-problem | No experiment | Simon 1973 [V] (a02, a05, a07) | single-source, K01 |
| Adding a code check or tool makes a sub-problem searchable | See verifier rows below | Simon 1973; Huang; Kambhampati; Stechly (a01, a21, b21, c05) | established, K02 |
| Tree search beats flat CoT on Game of 24 (GPT-4, 100 hard games) | IO 7.3%, CoT 4.0%, CoT-SC (k=100) 9.0%, ToT b=1 45%, ToT b=5 74%; best-of-100 CoT 49%, best-of-100 IO 33% | Yao 2023 [V] (a13, b16, c01) | established, K03 |
| Backtracking and pruning carry the crossword gain (5x5, 20 games) | Letter% / word% / games solved%: IO 38.7/14/0; CoT 40.6/15.6/1; ToT 78/60/20 (4 of 20); oracle best state 82.4/67.5/35 (7 of 20); no prune 65.4/41.5/5; no backtrack 54.6/20/5 | Yao 2023 [V] (a15, b17, c02) | established, K03 (small N, noisy ablation) |
| CoT commits early | About 60% of CoT samples already wrong after step 1 of 3 | Yao 2023 [V] (a14) | single-source, K05 |
| Generation, not evaluation, is the bottleneck | GPT-3.5 + ToT 19%; GPT-4 generate + GPT-3.5 evaluate 64%; GPT-3.5 generate + GPT-4 evaluate 31% | Yao 2023 [V], re-opened in critique | single-source |
| ToT near-equal-token comparison | ToT 5.5k completion tokens vs 6.7k for 100 CoT trials; 74% vs 49% | Yao 2023 [V] (c03) | contested, K04 |
| Cost-matched rerun with a sound verifier erases most of ToT's edge | ToT $0.74 per problem = about 150 plain queries ($0.47 per 100); 150 plain queries + sound verifier reach 70% vs ToT 74% | Stechly 2024 [V] (d10) | single-source, K04 |
| MCTS costs far more tokens than sampling plus voting | "dozens of times" more tokens; Llemma-7B with REBASE beat Llemma-34B across strategies | Wu 2025 [V] (d03) | single-source, K04 |
| LATS and RAP gains are not at equal budget | HotpotQA EM (GPT-3.5): CoT 0.34, CoT-SC 0.38, ToT 0.55, RAP 0.60, LATS 0.62; Game of 24 (GPT-3.5): CoT 0.08, ToT 0.20, RAP 0.40, LATS 0.44; HumanEval pass@1 92.7% (GPT-4); WebShop 75.9 | Zhou 2024 [V] (a20, b22, c04) | single-source on budget |
| RAP with a small model beats GPT-4 CoT at short plans only | Blocksworld 2/4/6-step: LLaMA-33B RAP(10) 1.00/0.86/0.26; GPT-4 CoT 0.50/0.63/0.40; RAP(20) 1.00/0.88/0.42 | Hao 2023 [V] (a19) | single-source, K10 |
| Search written out in tokens helps (needs training) | Searchformer: 93.7% of unseen Sokoban, 26.8% fewer search steps than A* | Lehnert 2024 [V] (a22) | single-source, K10 |
| A rule-based controller with a checker and history helps on Sudoku | 3x3: 10/10; 4x4: 9/10; 5x5: 8/10 (10 puzzles per size, cap 100 rounds); one-shot and few-shot about 0.5 on 4x4 | Long 2023 [V] (a23) | single-source |
| Intrinsic self-correction hurts | GPT-3.5 CSQA 75.8 to 38.1 (3 calls) to 41.8 (5 calls); GPT-3.5 GSM8K 75.9 to 74.7; HotpotQA 26.0 to 25.0; GPT-4 GSM8K 95.5 to 91.5 to 89.0; GPT-4 CSQA 82.0 to 80.0 | Huang 2024 [V] (a21, b19) | single-source, K07 (agrees with other sources behind SCHEMA G2) |
| Oracle labels fake a self-correction gain | GPT-3.5 CSQA 89.7 with oracle; GPT-4 GSM8K 97.5 with oracle; GPT-3.5 GSM8K keeps first answer 74.7% | Huang 2024 [V] (b19) | single-source, K07 |
| Self-critique loses, sound verifier gains | GPT-4, 100 instances per domain, standard / LLM critic / sound verifier: Game of 24 5/3/36-38; Graph Coloring 16/2/34-38; Blocksworld 40/55/83-87 | Stechly 2024 [V] (d09) | established, K27 |
| Most of the loop gain comes from the check, not the critique text | Critique-free sampling (k=25) reaches 42% on Game of 24 | Stechly 2024 [V] (d09) | established, K27 |
| Model verifier loses correct answers | Game of 24: accuracy 87.0% (3567/4100); 10.4% (320/3071) wrong accepted; 20.7% (213/1029) correct rejected (column mapping inferred) | Stechly 2024 [V] (d11) | established, K06 |
| External verifier loop lifts planning | Blocksworld 82% within 15 back-prompts; Logistics 70%; Mystery Blocksworld about 10%; TravelPlanner about 6x from 0.6% | Kambhampati 2024 [V] (b21, c05) | established, K08 |
| Plain GPT-4 Blocksworld baseline differs by source | PlanBench 34.3% one-shot (34.6% zero-shot); position paper about 12% | Valmeekam 2023; Kambhampati 2024 (a18, b21, d08) | contradiction; do not quote one number |
| Planning depends on surface form | Pre-reasoning models: Blocksworld 8-63%, Mystery Blocksworld 0-4.3% (one-shot GPT-4 4.3%, Claude 3.5 Sonnet 3.1%, LLaMA 3.1 405B 3.5%) | Valmeekam 2024 [V] (d08, a17) | established, K09 |
| o1-preview helps but the gap remains | Blocksworld 97.8%; Mystery 52.8%; Randomized Mystery 37.3%; 20-40 step plans 23.63%; o1-mini 56.6% and 19.1%; Fast Downward 100% | Valmeekam 2024 [V] (d07) | established, K09 |
| Best search method depends on difficulty | Beam search wins on hard items; best-of-N wins on easy items; lookahead underperforms at equal budget; compute-optimal by difficulty bin matched best-of-N with about 4x less compute (PaLM 2-S*, MATH) | Snell 2024 [V] (d01, d02) | established, K26 |
| Deep search over a learned verifier is over-exploited | Beam degrades on easy questions as budget grows | Snell 2024 [V] (d02) | established, K28 |
| Matched-token regimes for reasoning models | Low complexity: non-thinking equals or beats thinking; medium: thinking wins; high: both collapse to zero (Claude 3.7 Sonnet, DeepSeek-R1/V3, up to 64k tokens, 25 samples) | Shojaee 2025 [V] (d05) | contested, K26/K29 |
| Giving the algorithm does not remove the collapse | Tower of Hanoi, Checker Jumping: no accuracy gain from algorithm in prompt | Shojaee 2025 [V] (d06) | contested, K29 (setup criticised; critiques not opened) |
| Coverage rises log-linearly with samples; accuracy only with a verifier | SWE-bench Lite 15.9% (1 sample) to 56% (250 samples) vs 43% prior SOTA; without a verifier, vote and reward models plateau | Brown 2024 [V] (d04) | established, K27 |
| Tree search on web tasks with an exact final check | VisualWebArena GPT-4o+SoM 18.9 to 26.4% (+39.7% rel.); WebArena 15.0 to 19.2% (+28.0%); Llama-3-70B VWA 7.6 to 16.7% | Koh 2025 [V] (d12) | single-source, K32 |
| Scorer quality bounds search gain (200 VWA tasks) | No value function 24.5%; GPT-4o 28.5%; +SC n=5 32.5%; +SC n=20 37.0%; ground-truth reward 43.5%; LLaVA-34B SC n=20 30.0% | Koh 2025 [V] (d13) | established, K28 |
| Models satisfy single constraints, not all | TravelPlanner test, GPT-4-Turbo: delivery 93.1%; commonsense 63.3% micro / 2.0% macro; hard-constraint 10.5% / 5.5%; final pass 0.6%; other LLMs 0% | Xie 2024 [V] (b20, d14) | single-source, K30 |
| Fixation in humans (bridge game) | N=36 after 4 outliers dropped from 40; costly method kept by 15/18 (83%) vs 8/18 (44%) participants; 34 (47%) vs 13 (18%) of trials; chi2(1)=5.90, p=.01; time 102.5 s vs 74.4 s (d=.70); elements 26.5 vs 19.6 (d=.85); first-design cost d=1.06; "automatic" 9/18 vs 2/18 | Neroni 2017 [V] (b01-b03) | single-source, K11 |
| Examples: less variety, more novelty and quality | 43 studies; pooled effects not seen | Sio 2015 [M] (b05) | single-source, K12 |
| ChatGPT-4 as inventor: second of six teams | 116 prototypes; Nerf launcher distance: winner 37 m, ChatGPT team 14.8 m, others 8.1, 6.6, 5.1, 0.1 m; showed fixation, forgot constraints, dropped a promising concept after a setback | Egea 2024/25 [V] (b09, b10, c10, c11) | established with Chen and Ma, K13 |
| Chair design repeated familiar features | Unique terms: ChatGPT 67.4% vs human Red Dot entries 78.2%; 10 novices; 7 (ChatGPT) and 8 (Midjourney) of 10 noticed repetition; only 2 of 10 edited prompts | Chen 2025 [V] (b11, b12) | established, K13 |
| AI raises individual novelty, lowers group diversity | 293 writers, 600 evaluators; novelty +6.7% (b=0.259, p=.001); usefulness +6.4%; up to 5 AI ideas +8.1% and +9.0%; similarity to AI ideas +5.2% (1 idea), +5.0% (5 ideas) | Doshi and Hauser 2024 [V] (b13, b14) | established, K14 |
| Same pattern in ideation | 36 participants, 4 divergent tasks: more ideas per user, individual diversity equal, group-level diversity lower with ChatGPT than with a card deck | Anderson 2024 [V] (b15) | established, K14 |
| GPT-4 less diverse than crowd under all settings | 4,000 LLM solutions, 5 topics, 8 temperature/top-p pairs, 8 prompt methods, 100 human solutions per topic; best pair temp 1, top-p 1; critique-critique best; "unique" scored lower than "creative" or "novel" | Ma 2024 [V] (c12, c13) | established, K14, K15 |
| Sampling knobs do not fix homogeneity | 25 models x 100 queries x 50 responses; similarity above 0.8 in 79% of cases (top-p 0.9, T=1); still typically above 0.8 at min-p 0.1, T=2; cross-model similarity 71-82% (DeepSeek-V3 vs qwen-max 0.82; vs gpt-4o 0.81) | Jiang 2025 [V] (d15, d16) | established K15; single-source K31 |
| Over-generation hits a ceiling | 4000 seed ideas per topic; about 200 non-duplicates (cosine under 0.8, MiniLM) | Si 2024 [V] (b24) | single-source, K16 |
| LLM research ideas rated more novel by blind experts | 49 ideas per condition, 79 reviewers, 298 reviews; novelty 4.84 human, 5.64 AI, 5.81 AI + human rerank (p<.05 corrected); reviewer agreement 56.1% (chance 50%) vs 66.0% NeurIPS 2021, 71.9% ICLR 2024; best LLM ranker 71.4% | Si 2024 [V] (b23, b25) | contested, K17 |
| LLM stories fail creativity tests | 3 to 10 times less likely to pass TTCW tests than expert stories; Fleiss kappa 0.41; Pearson 0.69 aggregated; 10 experts, 2,000+ tests | Chakrabarty 2024 [V] (b26) | contested, K17 |
| Model-graded open-task wins are weak | ToT writing coherence 6.19 / 6.93 / 7.56 (GPT-4 judge, SD about 0.56); authors preferred ToT over CoT in 41 pairs, CoT over ToT in 21, 38 similar; refine lifts IO 6.19 to 7.67 and ToT to 7.91 | Yao 2023 [V] (a16, b18) | single-source, K18 |
| LLM help in problem reframing gave no gain | N=280 designers, 4 conditions, 3 problems, 15 expert raters; no significant novelty or usefulness difference; time for two frames: manual 23.25 min, direct 21.82, structured 28.35, free-form 20.78; structured users regenerated content (all but one at least once) | Shin 2025 [V] (c14, c15) | single-source, K21 (not re-opened by critique) |
| Open engineering design with simulator feedback | EngDesign: o3 34.38% single-shot, almost 60% after 10 iterations; GPT-4o and Gemini-2.0-Flash about 15%; analog IC 0% for all models even after 10 iterations; CoT on EngDesign-Open 14.29% vs 12.70% pass | Guo 2025 [V] (c06-c08) | single-source, K22 (not re-opened) |
| Difficulty rises with ill-structuredness | EngiBench Level 1 mostly 77-98%; Level 3 (rubric 0-10) GPT-4.1 and Claude 3.7 Sonnet above 6, Mixtral-8x7B below 4; humans beat all models. GraphicBench: 1,079 queries, 4 design types, 6 LLMs, VQA pass about 27.5-39.6% | Gu 2025; Kim 2025 [V] (c09, c19) | established, K23 |
| LLM can write a problem space, unreliably | Water-jug feasibility (GPT-4-0125); on 9 planning domains, 7 LLMs: best valid PDDL 94% of domains, functionally equivalent 25% | Wray 2024; Oswald 2024 [V] (c16, d17) | contested, K24 |
| Search-space theory | Search quality depends on how the domain prior shapes the hypothesis space | Song 2025 [V] (c18) | theory only |
| Simon predicts order-dependence and neglected interactions | Qualitative; LLM hackathon evidence of forgotten constraints | Simon 1973; Egea 2024 (a06, b10) | single-source, K20 |
| No test of search on a truly ill-structured task with outside verdict | All opened search gains have a check | critique, a25 | established as a gap, K25 |

## 4. Mechanisms and models

Each mechanism is described so that code can implement it.

### 4.1 Problem space (Newell and Simon)

A problem space is four things: a state representation, a set of operators (state to state), an initial state and a goal test. Search repeats: pick a state, apply an operator, test.

Implementation: `state` is a plain object or text. `operators(state)` returns a list of moves. `goal(state)` is code where possible. The control loop belongs to the program, not the model (SCHEMA section 1).

Simon's point for ISPs: the goal test and operator set are often missing at the start and are built during work. Our use: S1 and S2 produce a candidate problem space. If a goal test cannot be coded, mark the step "no-check" and use the open path (S0 gate).

### 4.2 Locally well-structured sub-problem (Simon 1973)

At each moment the solver holds a small immediate problem space: current goals, constraints, specifications and alternative generators (a05). Memory supplies new items on recognition. Implementation:

1. Keep a constraint ledger in code: each constraint, its source (brief or derived), status (satisfied, violated, unchecked) and the step that last touched it.
2. At each sub-problem, show the model only the relevant slice plus the ledger summary.
3. After each step, code re-checks every ledger item that can be checked. Order-dependence (a06) then shows as an item that was satisfied and is now violated.
4. Mitigations Simon named: decompose into near self-contained parts; fix global parameters first. These map to O3 (decompose) and an early S2 step.

Untested for LLMs (K20, K30).

### 4.3 Tree of Thoughts (Yao 2023) [V]

Four parts: decompose the task into thought steps; a generator (sample i.i.d. or propose sequentially); a state evaluator (value each state, or vote across states); a search algorithm (BFS with beam b, or DFS with pruning and backtracking). Game of 24: 3 steps, each a partial equation; BFS with b=5; the evaluator labels each state sure/maybe/impossible. Crosswords: DFS; prune states the model labels impossible; backtrack on dead ends. Writing: plan then passage, 5 samples, vote.

Where it breaks: the evaluator. The crossword heuristic lost correct branches (oracle 7 of 20 games vs 4 of 20). A model verifier rejected 20.7% of correct Game of 24 answers (d11). Generation is the second bottleneck (GPT-3.5 generator with GPT-4 evaluator: 31%).

### 4.4 RAP and world-model rollouts (Hao 2023) [V]

The same LLM acts as world model (predict next state after an action) and as agent. MCTS selects actions by reward. Gains were at 2 and 4 step plans. At 6 steps RAP(20) scored 0.42 vs GPT-4 CoT 0.40. Rollouts are expensive; budget is the limit (see Wu).

### 4.5 LATS (Zhou 2024) [V]

MCTS over an agent's trajectory. Selection by UCT, expansion by sampling actions, evaluation by an LLM value function plus self-consistency, simulation, backpropagation, and reflection on failed branches. Reported with more nodes than baselines, so not an equal-budget result.

### 4.6 Best-first tree search for web agents (Koh 2025) [V]

Best-first search over browser states with a model value function. Parameters: depth d, breadth b, number of expanded nodes. Gains grow with budget. Scorer quality is the bottleneck: 24.5% (none), 28.5% (GPT-4o), 37.0% (SC n=20), 43.5% (ground truth).

### 4.7 External-verifier loops (LLM-Modulo, Stechly) [V]

A generator proposes. A sound external critic returns pass or a located failure. Back-prompt up to k rounds (15 in Blocksworld). Critique text adds little; resampling plus a verifier gets most of the gain. The cheapest correct design is generate-many plus a code check, not a clever critic.

### 4.8 Gated search (Snell 2024) [V]

Estimate difficulty per item (for example, bin by a base model's pass rate). Pick a strategy per bin: best-of-N or sequential revision on easy items, beam search against a verifier on hard items. Cap verifier-guided depth to avoid over-exploitation. This matches G12.

### 4.9 Co-evolution as an operator pair

Dorst and Cross describe a bridge: a framing paired with a partial solution. As search: allow a move that edits the problem statement (O8, O4, O6), not only the candidate. The search state becomes (frame, partial solution). Evidence is process-level only (N=9, abstract-level reading). Shin 2025 found no gain from LLM-assisted reframing for humans.

### 4.10 Diversity operators

Sampling parameters do not diversify (d15). Prompt structure does (Ma 2024: critique-critique pass best). Implementation: keep a code-held list of solution families already produced. Each new attempt, in a fresh context, is told to avoid the named families. Dedupe by embedding at cosine 0.8 (Si's threshold). Stop branching when the duplicate rate passes a limit (K16).

## 5. What holds up

**Replicated or multi-source.**
- Verifier beats self-critique (Huang, Stechly, Kambhampati, Brown). Holds across planning, maths and code.
- Search with a good evaluator beats flat CoT on tasks with a crisp check (ToT, Long, RAP, LATS, Koh).
- Surface-form dependence in planning (Valmeekam 2023 and 2024, Kambhampati). The gap shrinks with o1 but remains (52.8% on Mystery).
- LLM homogeneity at group level (Doshi and Hauser, Anderson, Ma, Jiang). Four sources, three task types.
- Scorer quality bounds search (Koh, Stechly, Snell).
- Design fixation appears in LLMs (Egea, Chen, Ma). Qualitative or small-N.

**Contested.**
- ToT's advantage at equal cost: 74% vs 49% against unverified best-of-100, but 70% for 150 plain queries with a sound verifier. MCTS costs dozens of times more than voting (Wu). LATS and RAP are not equal-budget.
- LLM creativity: Si (more novel, but 56.1% reviewer agreement) vs Chakrabarty (3-10x less likely to pass). They may differ by measure: single-item ratings vs expert batteries.
- LLM reframing: Egea saw strong concept generation; Shin found no benefit for reframing (N=280).
- Reasoning-model collapse (Shojaee): methods criticised; critiques not opened.
- Formulation: water jugs worked; 25% functional equivalence on 9 domains.

**Failures and boundary conditions.**
- Intrinsic self-correction hurts (GPT-3.5 CSQA 75.8 to 38.1).
- Multi-agent debate is no better than self-consistency at equal responses (Huang, noted in critique).
- Lookahead search underperforms at equal budget (Snell). Beam search degrades on easy questions as budget grows.
- More samples hit a duplicate ceiling (5% unique of 4000).
- Search lifts only where the base model has some success: analog IC design stayed at 0% after 10 iterations.
- CoT gave a small, uneven gain on open engineering tasks (14.29% vs 12.70%).
- Giving the algorithm did not help in the collapse regime (Shojaee).

**Moderators.** Task has a checker (strongest). Item difficulty (Snell, Shojaee). Scorer quality (Koh). Number and commonness of examples (Sio). User competence: more competent designers got more novel frames (Shin). Model skill in the domain (EngDesign). Obfuscation of surface form (PlanBench).

**Interventions that worked:** external verifier loops; tree search with a good scorer; scorer self-consistency (+8.5 points from n=5 to n=20 on web tasks); critique-critique diversity pass; simulator-feedback iteration (34% to nearly 60%). Asking for alternatives is an Egea recommendation, not a controlled arm.

**Interventions that did not:** self-review without feedback; sampling-parameter sweeps; the word "unique" in prompts; LLM help for reframing; providing the algorithm in the collapse regime; CoT on open design (small).

**Small-sample warnings:** 20 crossword games; 10 Sudoku puzzles per size; N=36 fixation study; N=9 designers; 10 novices in Chen.

## 6. Language models

**Well-structured search tasks.**
- Flat prompting is poor where search is needed. GPT-4 on Game of 24: IO 7.3%, CoT 4.0%; with tree search 74%. About 60% of CoT chains are wrong after the first step.
- The size of the search edge depends on the baseline. With a sound verifier, plain sampling at the same cost gets 70% (d10).
- Most of the gain in loops comes from the check. Critique-free resampling plus a sound verifier recovers most of it (K27).
- Search depends on a scorer. A model scorer drops correct branches (20.7% of correct Game of 24 answers rejected). A ground-truth reward gives 43.5% vs 28.5% for a GPT-4o scorer on 200 web tasks.
- Different methods win at different difficulties (Snell). For reasoning models at matched tokens there are three regimes (Shojaee).
- Test-time compute can stand in for model size in some cases: Llemma-7B with REBASE beat Llemma-34B (Wu).

**Planning.**
- 2023 models: about 3% average autonomous success; GPT-4 Blocksworld 34.3% (PlanBench) or about 12% (position paper); near 0 on obfuscated versions.
- o1-preview: 97.8% plain, 52.8% Mystery, 37.3% Randomized Mystery, 23.63% on 20-40 step plans.
- LLM-Modulo with a verifier: 82% in 15 rounds.

**Open design tasks.**
- Concept generation is strong: second of six teams in a hackathon; novelty ratings above experts in blind review.
- Failure types: fixation on one concept; latching onto the last list item; forgetting earlier constraints; dropping a promising concept after a setback; needless complexity; repeating familiar features.
- Group-level diversity is low (pairwise similarity above 0.8 in 79% of cases; 71-82% across models). Sampling knobs do not fix it. A critique-critique pass is the best prompt method found and still below humans.
- Engineering design with a simulator: iteration lifts success from 34.38% to almost 60%. Without domain skill nothing helps.
- Plans can look right and fail in execution (GraphicBench VQA about 27.5-39.6%).
- Human use: people pass output on unchanged (2 of 10 edited a Midjourney prompt); structured reframing users regenerated content again and again.

**What changed things, by how much.**
- External check: +30 to +45 points on planning and puzzles (Game of 24 5% to 36-38%; Blocksworld 40% to 83-87%).
- Tree structure over verified sampling: about +4 points (74% vs 70%).
- Better scorer: +8.5 points (SC n=5 to n=20), and up to +15 points (ground truth vs GPT-4o).
- Sampling parameters: no clean effect.
- Prompt structure on diversity: critique-critique largest; no method reached human diversity.
- 2025-2026 reasoning models: no opened paper compares them head-to-head with a search scaffold.

**Not known.** No opened study compares a code-held search tree with a strong reasoning model's own long chain of thought at equal tokens on 2025-2026 models. None tests search on an ill-structured task with an outside verdict (K25).

## 7. What our agent should take

Status: [E] established, [S] single-source, [C] contested. Schema parts: G guardrail, S state, O operator, memory = S9 lessons.

### Add now (established)

| # | Item | Schema part | Status | Evidence ids |
|---|---|---|---|---|
| A1 | Make sub-steps checkable. Where an open task has a sub-step with a code or tool check, route it through S4/S5 on real output. Never rely on the model's own review. | G2, G3, S4, S5 | [E] | K02, K06, K07, K08, K27; a21, b19, c05, d09, d11 |
| A2 | Resample plus check before a clever critic. Critique text is optional. | G5, S3, S4 | [E] | K27; d09, d10, d04 |
| A3 | Do not let the model evaluate branches when a code check exists. If a model scorer is unavoidable, use self-consistency on the scorer and log pruned-correct branches. | G5, S6 | [E] | K06, K28; a15, d11, d13, d02 |
| A4 | Gate search by difficulty. Easy: plain or short best-of-N. Hard: tree or beam with a checker. Collapse zone: do not expect search to rescue. | S0, G12 | [E] | K26; d01, d02, d05 |
| A5 | Include obfuscated variants in every planning-like test set. A large gap means recall, not search. | G1 (test hygiene) | [E] | K09; a17, d07, d08 |
| A6 | Do not rely on sampling parameters for diversity. Use prompt structure and a code-held list of tried families. Sibling-model samples are not independent. | S3 open mode, G4 | [E] | K15; d15, c12 (K31 [S]: d16) |
| A7 | Fixation guard in open mode: name distinct solution families first, each attempt in a fresh context. | S3, O | [E] | K13, K14; b09-b11, c10-c13 |
| A8 | Never accept a model-graded win on an open task alone. Use a second judge model and blind human or code scoring. | G8 | [E] | K17, K18; a16, b25, b26 |
| A9 | Compare every addition at equal tokens (LATS and RAP did not). | G7 | [E] | K04; a20, d03, d10 |

Most of these restate existing guardrails; the new evidence is the size of the numbers (A2, A3) and the difficulty gate (A4).

### Test first

| # | Item | Schema part | Status | Evidence ids |
|---|---|---|---|---|
| T1 | S6 tree vs a strong reasoning model's own long CoT vs verified best-of-N at equal tokens | S6, G11 | [C] | K04, K26; d03, d05, d10 |
| T2 | Constraint ledger checked by code (Simon's order-dependence) | S1/S2, G3 | [S] | K20, K30; a06, d14 |
| T3 | Branch at the first decision only (60% of CoT wrong by step 1) | S6 | [S] | K05; a14 |
| T4 | Reframe operator (O8) with a check, vs solution-only search. Expect null without a check | O8 | [S]/[C] | K19, K21; a12, c14 |
| T5 | Forced-alternatives step after the first committed answer | O, G1 | [C] | K29, K11; d06, b01-b03 |
| T6 | Critique-critique diversity pass vs plain resampling | S3 open mode | [S] | K14; c13 |
| T7 | LLM-formulated problem space plus code search | S1/S2, S6 | [C] | K24; c16, d17 |
| T8 | Depth vs breadth ablation at equal calls | S6 | [S] | K32; d12 |
| T9 | Open-task benchmark with delayed outside verdict | S6 risk | [S] | K25, K22; c06 |
| T10 | Visible search record in the output (RAP / Searchformer idea without training) | S6 | [S] | K10; a19, a22 |
| T11 | Example count and commonness for O7 / retrieval (Sio) | O7, memory | [S] | K12; b05 |
| T12 | Stop branching when the duplicate rate passes a threshold | G7, S3 | [S] | K16; b24 |

## 8. Concrete tests on our bench

All arms run at equal total tokens, setup cost included (G7). Report mean with an interval and log the step of first error.

| Test | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 | Game of 24 hard set and a held-out puzzle set (Sudoku, mini crossword) | (a) model's own long CoT, (b) verified best-of-N, (c) S6 tree with code check, (d) unverified best-of-N | Exact-match pass rate | (c) well ahead of (d); (c) ahead of (b) by about 4 points or less. If (c) does not beat (b), drop tree structure and keep the check. |
| T2 | TravelPlanner subset plus 20 multi-constraint briefs | (a) plain, (b) code-checked ledger | Final pass rate; violations per plan; violations when step order is swapped | Final pass above 0.6% base; fewer macro-level violations; less order-dependence. |
| T3 | Game of 24, planning items | (a) uniform branching, (b) all budget at step 1, (c) flat CoT | Pass rate; step of first fatal error | (b) at least level with (a) and cheaper. |
| T4 | Open design briefs scored by simulator or blind raters (EngDesign-style) | (a) solution-only search, (b) search with reframe operator and a check on frame consistency | Rubric score; pass rate | Null without a check; small gain with one. |
| T5 | Items with a planted flawed example (Jansson and Smith style) | (a) plain, (b) forced-alternative step, (c) flawed example removed | Share of outputs repeating the flawed feature; quality | (a) shows fixation; (b) cuts it without losing quality. |
| T6 | Open ideation prompts, 5 topics, 50 outputs per arm | (a) plain resampling, (b) critique-critique pass, (c) code-held family list | Pairwise embedding similarity; unique ideas per 1000 tokens; quality by blind or code score | (b) and (c) lower similarity than (a); quality does not fall. |
| T7 | Word problems and puzzles with verified answers | (a) LLM writes space, code searches, (b) hand-built space plus code search, (c) plain | Pass rate; separate formulation score | (a) below (b); formulation errors counted. |
| T8 | Hard puzzle set | Depth d and breadth b varied at fixed total calls | Pass rate | Shows which of depth or breadth carries the gain. |
| T9 | Delayed-verdict task (simulator) | plain, best-of-N, S6 | Score after verdict | Gain smaller than on crisp tasks. |
| A5 check | Every planning item | plain vs obfuscated names | Gap | Large gap = recall; report scaffold gain on obfuscated items only. |

## 9. What does not transfer, and why

- **Human protocol findings (N=9 to 36).** Fixation in a bridge game is real in humans. Transfer to LLMs in the controlled sense is untested. LLM fixation evidence is qualitative or small-N.
- **Simon's serial-memory account.** LLMs have no serial bottleneck of the type Simon assumed, and "retrieval" is parametric. His order-dependence prediction is plausible for LLMs but unmeasured.
- **Rittel and Webber's wicked-problem properties.** No stopping rule and no test means the agent cannot reach "solved" by code. We can only offer a budget stop and a fallback (G6). Not testable on a bench with known answers.
- **ToT headline numbers.** 2023 GPT-4, exact-check tasks, unverified-sampling baseline. They do not show that search beats a 2026 reasoning model.
- **Model-graded open-task gains.** ToT writing and Si ideas rest on noisy judges (reviewer agreement 56.1%).
- **LATS and RAP gains.** Larger budgets than baselines.
- **Searchformer.** Needs training on A* traces; our agent does not train.
- **Hackathon result.** One team, one run; the model directed human builders.
- **Reframing null result.** Humans using a tool (N=280), not an agent loop.
- **Reasoning-model collapse puzzles.** Hanoi and checker jumping are exactly checkable and unlike the ill-structured part.

## 10. Open questions

1. Does S6 beat a strong reasoning model's own long CoT and verified best-of-N at equal tokens on 2025-2026 models?
2. Does tree search help on an ill-structured task with only a delayed outside verdict? Which sub-steps can get a code check?
3. Which operator carries the gain: branching at step 1, reframing, relaxing a constraint, or backtracking?
4. How much does a weak model evaluator cost in pruned-correct branches, and does a code check remove it, on the same items?
5. Does a code-checked constraint ledger reduce forgotten constraints and order-dependence?
6. Does a forced-diversity step raise group diversity without lowering quality, and does it help or hurt on a verified task?
7. Does example-induced fixation transfer to LLMs with an effect size, and does an alternatives operator remove it?
8. What are the effect sizes and moderators in Sio et al., and the sample sizes in Goel and Pirolli and Dorst and Cross? (Paywalled.)
9. Can an LLM reliably formulate states, operators and a goal test on non-toy tasks? What share of failures comes from formulation?
10. How much of the search gain is pattern recall? Obfuscate all items.
11. Is the Shojaee collapse real once token limits and unsolvable instances are fixed? (Critiques not opened.)
12. Does Simon's "no special process" claim or the design-specific view predict which tasks need a reframe operator?

## 11. Sources

[V] opened as full text; [M] snippet, abstract or memory only.

**Foundations**
- [V] Simon (1973) The structure of ill structured problems. https://ojs.unbc.ca/index.php/design/article/viewFile/1273/1090 (also https://doi.org/10.1016/0004-3702(73)90011-8)
- [M] Newell and Simon (1972) Human Problem Solving. https://archive.org/details/humanproblemsolv0000newe
- [M] Newell and Simon (1976) Computer science as empirical inquiry. https://dl.acm.org/doi/10.1145/360018.360022
- [M] Simon (1969/1996) The Sciences of the Artificial (no URL opened)
- [M] Reitman (1964/1965) Heuristic decision procedures, open constraints, and the structure of ill-defined problems. https://www.worldcat.org/title/cognition-and-thought/
- [M] Rittel and Webber (1973) Dilemmas in a general theory of planning. https://doi.org/10.1007/BF01405730 (scan, no text layer)
- [M] Goel and Pirolli (1992) The structure of design problem spaces. https://doi.org/10.1207/S15516709COG1603_3
- [M] Dorst and Cross (2001) Creativity in the design process. https://doi.org/10.1016/S0142-694X(01)00009-6 ; https://oro.open.ac.uk/3278
- [M] Kruger and Cross (2006) Solution driven versus problem driven design. https://oro.open.ac.uk/7423
- [M] Sio, Kotovsky, Cagan (2015) Fixation or inspiration? https://doi.org/10.1016/j.destud.2015.04.004
- [V, abstract page] Biskjaer, Halskov, de Rooij (2026) Problem-solution co-evolution research in the DRS community. https://dl.designresearchsociety.org/drs-conference-papers/drs2026/researchpapers/240
- [M] Older systems (GPS, Soar, R1/XCON, AM, BACON). https://en.wikipedia.org/wiki/General_Problem_Solver
- [M] Jansson and Smith (1991) Design fixation (seen through Neroni et al.; no URL)

**Human design studies**
- [V] Neroni, Vasconcelos, Crilly (2017) Studying design fixation with a computer-based task. https://cognitive.designsociety.org/download-publication/39819/Studying+design+fixation+with+a+computer-based+task

**LLM search and planning**
- [V] Yao et al. (2023) Tree of Thoughts. https://arxiv.org/abs/2305.10601
- [V] Hao et al. (2023) RAP. https://arxiv.org/pdf/2305.14992
- [V] Zhou et al. (2024) LATS. https://arxiv.org/abs/2310.04406
- [V] Long (2023) LLM guided Tree-of-Thought. https://arxiv.org/pdf/2305.08291
- [V] Lehnert et al. (2024) Searchformer. https://arxiv.org/pdf/2402.14083
- [V] Koh et al. (2025) Tree search for language model agents. https://arxiv.org/abs/2407.01476
- [V] Valmeekam et al. (2023) On the planning abilities of LLMs. https://arxiv.org/pdf/2302.06706
- [V] Valmeekam et al. (2023) PlanBench. https://arxiv.org/pdf/2206.10498
- [V] Valmeekam et al. (2024) LLMs still can't plan; can LRMs? https://arxiv.org/abs/2409.13373
- [V] Kambhampati et al. (2024) LLMs can't plan, but can help planning in LLM-Modulo frameworks. https://arxiv.org/abs/2402.01817
- [V] Stechly, Valmeekam, Kambhampati (2024) On the self-verification limitations of LLMs. https://arxiv.org/abs/2402.08115
- [V] Huang et al. (2024) LLMs cannot self-correct reasoning yet. https://arxiv.org/abs/2310.01798
- [V] Snell et al. (2024) Scaling LLM test-time compute optimally. https://arxiv.org/abs/2408.03314
- [V] Wu et al. (2025) Inference scaling laws. https://arxiv.org/abs/2408.00724
- [V] Brown et al. (2024) Large language monkeys. https://arxiv.org/abs/2407.21787
- [V] Shojaee et al. (2025) The illusion of thinking. https://arxiv.org/abs/2506.06941
- [V] Xie et al. (2024) TravelPlanner. https://arxiv.org/abs/2402.01622
- [V] Song (2025) Where to search. https://arxiv.org/abs/2510.14846
- [V] Wray, Kirk, Laird (2024) Eliciting problem specifications via LLMs. https://arxiv.org/abs/2405.12147
- [V] Oswald et al. (2024) LLMs as planning domain generators. https://arxiv.org/abs/2405.06650
- [M] Kirk et al. (2024) LLM-integrated interactive task learning in Soar (as cited by Wray). https://arxiv.org/abs/2405.12147

**LLM design, creativity and diversity**
- [V] Egea et al. (2024/25) ChatGPT as an inventor. https://arxiv.org/abs/2404.18479
- [V] Chen et al. (2025) Understanding design fixation in generative AI. https://arxiv.org/abs/2502.05870
- [V] Doshi and Hauser (2024) Generative AI enhances creativity but reduces diversity. https://arxiv.org/abs/2312.00506
- [V] Anderson, Shah, Kreminski (2024) Homogenization effects of LLMs. https://arxiv.org/abs/2402.01536
- [V] Ma et al. (2024) Capabilities of LLMs for generating diverse design solutions. https://arxiv.org/abs/2405.02345
- [V] Jiang et al. (2025) Artificial Hivemind. https://arxiv.org/abs/2510.22954
- [V] Si, Yang, Hashimoto (2024) Can LLMs generate novel research ideas? https://arxiv.org/abs/2409.04109
- [V] Chakrabarty et al. (2024) Art or artifice? https://arxiv.org/abs/2309.14556
- [V, not re-opened by checker] Shin et al. (2025) No evidence for LLMs being useful in problem reframing. https://arxiv.org/abs/2503.01631
- [V, not re-opened by checker] Guo et al. (2025) EngDesign. https://arxiv.org/abs/2509.16204
- [V, not re-opened by checker] Gu et al. (2025) EngiBench. https://arxiv.org/abs/2509.17677
- [V, not re-opened by checker] Kim et al. (2025) GraphicBench. https://arxiv.org/abs/2504.11571

## Source audit (2026-11-03)

Fresh auditors re-opened the sources of 13 established claims: 10 confirmed as written, 3 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **E05.01-K02** (reworded: the sources support less). Simon supports solver-relative structure and a mechanizable test as a WSP criterion, and Kambhampati shows verifier loops help, but no source shows that adding a code check turns a sub-problem well-structured and searchable; that is the researcher's inference, and Huang is about self-correction, not structure. Corrected claim: Whether a task counts as ill-structured depends on the solver and its resources (Simon 1973: chess is well-structured in the small, ill-structured in the large). A mechanizable test of solutions is one of Simon's criteria for a well-structured problem, and external verifier loops lift LLM planning where a verifier exists (Kambhampati 2024); this suggests, but no opened source tests, that adding a code check makes a sub-problem more searchable.
- **E05.01-K09** (now single-source: the sources are not independent). Numbers match the PlanBench o1 paper, but every listed source (Valmeekam 2023, Kambhampati 2024, Valmeekam 2024) comes from the same Kambhampati/Valmeekam ASU group, so the surface-form claim rests on one lab.
- **E05.01-K25** (reworded: the sources support less). Numbers for Koh et al. and Brown et al. match, but the ToT paper (opened in the same batch) measured a tree-search gain on open-ended Creative Writing judged by GPT-4 scores and human pairwise preference, so 'all measured search gains are on tasks with a check' is too broad. Corrected claim: Among the opened studies, the tree-search gains on tasks with an exact external check are large (Game of 24, crosswords, VisualWebArena +39.7% relative, WebArena +28.0%); the one open-ended test, ToT creative writing, was judged only by GPT-4 scores (7.56 vs 6.93 CoT) and a human preference comparison, and no opened study measures tree search against an expert verdict on a truly ill-structured brief.
- **E05.01-K19** (now single-source: only one opened source, code check).
