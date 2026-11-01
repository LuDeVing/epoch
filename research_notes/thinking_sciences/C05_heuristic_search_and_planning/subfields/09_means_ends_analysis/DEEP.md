# Means-ends analysis: deep document

*Subfield C05.09. Reduce the difference between state and goal. Schema link: O5 (work backwards / means-ends), subgoal choice at S6. Sources: evidence_a-d.jsonl (a01-a34, b01-b33, c01-c31, d01-d21), claims.jsonl (K01-K30), critique.md. Read this first: the founding human studies (Newell and Simon 1959/1961/1972, Ernst and Newell 1969, Sweller 1982-88, Owen and Sweller 1985, Vollmeyer 1996 full text, Kotovsky 1985, Atwood and Polson 1976) were NOT opened this session (publisher pages returned 403, RAND PDF 403, archive text unusable). Everything about them below is marked [M] and carries no numbers. Do not quote protocol match rates or effect sizes for them. The LLM evidence is mostly opened and re-checked.*

## 1. What it is

Means-ends analysis (MEA) is a way to solve a problem by looking at the gap between where you are and where you want to be.

The loop has four steps.
1. Measure the difference between the current state and the goal.
2. Pick an operator (a move) that is known to reduce that kind of difference.
3. If the operator cannot be applied yet, because a precondition is false, make that precondition a new subgoal and recurse.
4. Apply the operator, check the new state, repeat.

It is a "weak method". It needs no domain expertise beyond a table that links difference types to operators. It works best when differences are few, operators are clear and goals do not interfere. It fails when reducing the difference means first making it larger (river crossing, the one move that goes back), and when achieved subgoals are undone by later ones (Sussman anomaly).

For our agent MEA is the engine behind operator O5 and the "make the blocked step a subgoal" part of S6. The schema calls O5 "work backwards"; strictly, MEA is gap-driven, not just backward. Status in the schema today: [S].

Three things people mean by "MEA". Keep them apart, because the evidence differs for each:
- **GPS-style difference reduction** (choose the operator by the type of gap). Human and classical-AI literature. Almost no direct LLM test.
- **Recursive subgoaling on blocked preconditions.** Tested by MEDAKA, MAP, ADaPT, least-to-most (as decomposition).
- **Backward or goal-directed search** (LAMBADA, work backwards). Related but not the same.

## 2. History and theories in depth

All items in this section from 1959 to 1988 are [M] (recalled or snippet), not opened. Treat them as context.

**GPS (1959-1969).** Newell, Shaw and Simon (1959, IFIP, pp 256-264) wrote the General Problem Solver. A problem is a start state and a goal state. GPS finds the difference, picks an operator tied to that difference type, and sets an unmet precondition as a subgoal (a01, [M]). Newell and Simon (1961, Science) compared GPS traces with thinking-aloud protocols on logic problems and argued the goal types and subgoal structure were similar (a02, [M]). The match was judged by the authors on few protocols, not by blind raters. No numbers were recovered (critique gap 2, unresolved). Ernst and Newell (1969) rewrote GPS so task knowledge (objects, operators, difference table) is data and the solver is fixed; it ran on roughly ten task environments such as symbolic integration, Missionaries and Cannibals, Tower of Hanoi and parsing (a03, [M]; the count "about 10 to 11" is not verified). Wikipedia (a04, opened) confirms GPS was written in IPL at RAND, was the first program to separate problem knowledge from a generic solver, and solved toy problems but not real-world ones because search spaces blow up. Newell and Simon (1972) Human Problem Solving is the book that consolidates the work.

**STRIPS and planning (1971-1987).** Fikes and Nilsson (1971) formalised operators as preconditions, add-lists and delete-lists (a06, [M]). That is the form modern planners use. Sussman (1973/75) and Chapman (1987) showed that linear subgoal-by-subgoal MEA fails on interacting goals. In the Sussman anomaly (blocks world: C on A; want A on B and B on C), achieving A-on-B first and then B-on-C undoes the first, and the reverse order fails too (a07, b30, c23; c23 Wikipedia opened). Fix: non-linear planning, goal ordering, protect achieved goals. This is the oldest named boundary of the method.

**Soar (1987).** Laird, Newell and Rosenbloom: MEA is a weak method that appears when the system hits an impasse and makes a subgoal for it; chunking turns solved subgoals into rules so the search is not repeated (a08, [M]). This is the closest classical match to our S6 (impasse, subgoal) and S9 (lesson).

**Human expertise studies.** Larkin, McDermott, Simon and Simon (1980): physics novices work backward from the unknown with MEA-like steps, experts work forward from the givens with known principles and mostly do not search (a09, [M]). Atwood and Polson (1976) modelled water-jug moves as "pick the move that gets closest to the goal" with very limited look-ahead plus memory for recent states, and it fit people better than full search (a14, [M]). Jeffries et al. (1977) did the same for Missionaries and Cannibals (a15, [M]). Thomas (1974, hobbits-orcs) and Goel and Grafman (1995): people stall at the step where the correct move increases the apparent distance to the goal; frontal-lobe patients were mainly impaired on that counterintuitive move (b28, b29, [M]; later work disputes how specific the Hanoi deficit is). Simon (1975): Tower of Hanoi has several strategies that give the same output (goal-recursive, perceptual, move-pattern), and people shift from MEA to perceptual strategies with practice (a16, b26, [M]). Kotovsky, Hayes and Simon (1985): isomorphs of Hanoi differ by roughly a factor of 16 in solution time, so the same state space is not the same problem (a17, b27, [M]; the factor is recalled, unverified).

**Cognitive load theory (1982-1988).** Sweller and colleagues argued that MEA is a costly general strategy: it uses working memory on the gap and operator choice and leaves little for learning rules. Evidence lines: Sweller, Mawer and Ward (1983) (a10, [M]); Sweller (1988) (a11, d07, [M]); Sweller and Levine (1982) (b22, [M]); Owen and Sweller (1985) (a12, [M]): goal-free geometry problems ("find as many angles as you can") gave faster learning than specific-goal problems; Ayres (1993) (b24, [M]). No effect sizes obtained. A 2023-2025 position article (a32, opened) argues the opposite side: MEA is a general method for new domains that may itself need explicit teaching, disputing the load view that general strategies need no teaching. No new data.

**The Vollmeyer correction.** Vollmeyer, Burns and Holyoak (1996) (a13, b25, d06; abstract and references read, full text blocked). Two experiments on a complex dynamic system. A specific goal pushed difference reduction and less systematic hypothesis testing; the specific-goal group did well on the first problem and worse on a transfer problem with a different goal. Instruction in systematic rule induction helped under both goal types. So the mediator is strategy, not goal-freedom alone. No group means or N available.

**Revival in LLM work (2023-2026).** The MEA idea returned under other names: decomposition (least-to-most, ADaPT), subgoal planning (MAP, MiRA), search (ToT, RAP), LLM-Modulo (planner plus external checker). The first direct test of an MEA prompt is Li and Kingsford (2026), MEDAKA (c01-c05, d01-d03). A historical reproduction (c21, Shrager et al. 2026) reran Simon's 1961 Heuristic Compiler and reproduced the code in Simon (1963); Simon (1984) said MEA alone is not enough for programming, you also need indexed operators and many high-level strategies. That reproduction shows behaviour was reproduced, not that the theory is right.

## 3. Core findings with exact numbers

Status key: E = established (two or more independent sources, claims.jsonl), S = single source, C = contested, M = human founding study not opened, no numbers, D = dropped.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| MEA prompt (measure gap, pick operator, recurse on blocked precondition, track state) beats CoT on continuous planning | Total pass@1 CoT / AoT+ / MEDAKA, 189 problems, 3 rollouts, thinking off: Claude-Sonnet-4.6 77.8 / 85.0 / 94.5; Gemini-3-Flash 65.6 / 71.6 / 82.0; GPT-4o 25.7 / 19.8 / 36.9; LLaMA-3.3-70B 26.6 / 17.6 / 40.6; Gemma4-4B 55.7 / 52.7 / 61.0; Gemma4-2B 26.3 / 23.8 / 30.5 | Li and Kingsford 2026 (c01, d01) | S (K01) |
| No gain on one frontier model | GPT-5.4 74.3 / 78.5 / 78.5; nonlinear MEDAKA 46.5 below AoT+ 49.1 | c01, c02, d03 | S (K02) |
| Gain is largest on hard structure | Nonlinear pass@1 Claude 33.3 / 55.3 / 87.4; Gemini 16.4 / 21.4 / 50.9; multi-goal Claude 50.4 to 89.5; distractor Claude 73.8 to 94.0, GPT-4o 10.7 to 42.9; linear Claude 95.1 / 96.6 / 97.3 (saturated). Open-weight Gemma4-4B nonlinear 14.5 / 15.1 / 12.6 (no gain) | c02 | S |
| State tracking and recursion are load-bearing | Claude full 94.5, no state tracking 90.5 (-4.0), no recursion 91.0 (-3.5). Gemini full 82.0; ablated 76.0 (-6.0) and 75.1 (-6.9). Gemini nonlinear 50.9 / 36.5 / 28.9. Ablated variants still beat CoT (77.8; 65.6) | c03, d01 | S (K03) |
| Operator choice by gap size never ablated; no discrete-domain test | Untested in the paper | d01 | S (K28) |
| MEDAKA beats CoT pass@3 for some models, at higher token cost | Claude CoT pass@3 86.8 vs MEDAKA pass@1 94.5; Gemini 67.2 vs 82.0; fails for GPT-5.4 and both Gemma4. Median tokens: Claude 2185 vs 6857 (3.1x), Gemini 1989 vs 4053 (2.0x), GPT-5.4 1859 vs 7013 (3.8x). Range 1.8x-3.8x. MEDAKA pass@3: Claude 97.9, Gemini 84.1, GPT-5.4 89.4 | c05, d02 | S (K04). Not a true equal-token test (pass@3 is any-of-3) |
| Thinking mode was off for all models | GPT-5.4 tie with AoT+ is the only hint of "little gain on strong models" | d03 | S (K02) |
| Plain LLMs plan poorly on Blocksworld | GPT-4 206/600 = 34.3% plain; Mystery (deceptive) 26/600 = 4.3%; randomised 12/600 = 2%; InstructGPT-3 41/600; GPT-3 6/600; BLOOM 4/250. Human baseline 39/50 = 78% valid plans | a22, a23, b01, b02, c24, d15 | E (K05, K18) |
| Reasoning models changed the plain picture but not the obfuscated one | o1-preview 587/600 = 97.8% on 3-5 block Blocksworld; Mystery 317/600 = 52.8%; randomised 224/600 = 37.3%; Fast Downward 100% in 0.265 s | b03, c25, b31 | E (K06, K18) |
| Step-specific CoT helps only when matched to the class | GPT-4 table-to-stack 3.83% zero-shot; 59.3% stacking-specific CoT; 51.3% universal-algorithm CoT; 6.89% progression-proof CoT; self-consistency lowered accuracy | Stechly et al. 2024 (b04) | S (K07) |
| LLM-Modulo / exact external checker works | Blocksworld 41/50 (82%), Logistics 35/50 (70%), Mystery 5/50 (10%) within 15 rounds. o1-preview hard Blocksworld 23.65% to 98.2% with verifier loop, 7 iterations, $52 to $139 per 100 instances (about 2.7x cost) | c25, c26, d13, d14 | S (K22); all lines trace to one group |
| Majority vote beats LLM generative verifier at equal compute | GenRM matches self-consistency only at about 8x SC compute (Llama-3.1-8B, MATH); beats it by +3.8% at about 128x | Singhi et al. 2025 (d11) | E (K26) when combined with exact-check evidence |
| Search with an evaluator beats linear CoT | Game of 24, GPT-4: IO 7.3, CoT 4.0, CoT-SC(100) 9.0, ToT b=1 45, ToT b=5 74 | Yao et al. 2023 (a27, b09, c30 are one paper) | S (K08) |
| LLM as world model plus planner | RAP(10) 2/4/6-step Blocksworld: 1.00 / 0.86 / 0.26 vs CoT GPT-4 0.50 / 0.63 / 0.40; RAP best 64% on one setting | Hao et al. 2023 (a24, c27) | S (K09). 6-step success still low |
| As-needed decomposition helps agents | ADaPT ALFWorld 71.6 vs ReAct 43.3; WebShop 44.0 vs 32.0; TextCraft 52.0 vs 19.0. Least-to-most SCAN length split 99.7% vs CoT 16.2% | Prasad et al. 2023-24 (a28, c28, d16); Zhou et al. 2023 (b10) | E (K10) for "decomposition helps"; ADaPT has no always-decompose ablation and no token cost, single run per model |
| Modular planner with monitor on Tower of Hanoi | 3-disk solve 11% (GPT-4 zero-shot) to 74% (MAP); no monitor 27% with 31% invalid moves; no decomposer 50%; Mystery 27.4% | Webb, Mondal, Momennejad (b08, c06-c09: one paper) | S (K11) |
| Subgoal framework for web agents | Gemini-2.5-pro WebArena-Lite 23.0% to 32.1%; stuck-midway errors 48.41% to 39.87%; wrong terminations 9.52% to 12.03%; Gemma3-12B + milestone reward 6.4% to 43.0% | Wang et al. 2026 (c19, c20) | S (K12) |
| Hanoi collapse is partly an output limit | Apple: N=5 needs 31 moves; River Crossing N=3 11 moves; collapse near N=8-10. Lawsen: about 10 tokens per move; 12-13 disks fit 64k; N=15 needs 32,767 moves but a generator function fits in under 5,000 tokens; River Crossing N>=6 unsolvable | a18, a20, b05, b06, c10, c11, d20 | C (K13). Lawsen preliminary, not peer reviewed |
| Algorithm given, still collapse | DeepSeek-R1 at temperature 0 collapsed at N=8 even with algorithm | a19, c10 | C (K14) |
| Million-step execution is possible with per-step voting | 1,048,575 steps, zero errors, gpt-4.1-mini, per-step error 0.0022, k_min=3, projected $3.5K; haiku-4.5 per-step error 0.1839, $71.2K; llama-3.2-3B cannot vote | Meyerson et al. 2025 (a21, b07, c14, c15, d10: one paper) | S (K15). No equal-compute test against more reasoning budget |
| Policy drift and memory reuse on Hanoi | At n=8 about 40% of the time the model reused previously seen continuations; Hanoi (template-friendly) held up longest; accuracy drops over 50 points beyond a task threshold | Su et al. 2025 (c16); Utsho et al. 2026 (c17) | E (K17) |
| Internal state decoded but not used | Probe decodes Hanoi state; steering raises optimal solves 41% to 73% on 81 configs (Qwen3.6-27B, best strength); R1-Distill-32B fixed 6/72 failures | Pereira and Zuidema 2026 (c12, c13) | S (K16). Needs weights; motivation only |
| Code-defined operators | LLM writes successor and goal-test once, ordinary search runs: 100% on 24 Game, crosswords, Blocksworld (4-5 blocks), PrOntoQA with about 2-4 model calls vs projected 200K-560K calls for tree methods on Blocksworld | Katz et al. 2024 (a29, d17) | S (K29) |
| CoT adds little on reasoning models | GPQA Diamond, 4,950 runs per prompt per model: CoT +2.9 (o3-mini), +3.1 (o4-mini), -3.3 (Gemini Flash 2.5), with 20-80% more time. Thinking vs non-thinking at matched tokens: no edge at low complexity | Meincke et al. 2025 (d04); Shojaee et al. (d05) | E (K27) |
| Obfuscation / counterfactual lowers plain results | GPT-3.5 parseable programs 99% to 62% (vertical flip), 71% (90 degree), 75% (180 degree); default and counterfactual correlated | Wu et al. 2023 (d18) | E (K30) |
| Backward chaining on proofs | ProofWriter depth 5 (50 samples): CoT correct proof chains 28%, hallucination 48% of errors; reported gains at depth 5 of 44% over CoT and 56% over SI | LAMBADA (a25, c29) | S. Proof search, not difference reduction |
| Behaviours that enable RL gains | After RL on Countdown, Qwen-2.5-3B about 60% vs Llama-3.2-3B about 30%; priming with wrong solutions that had the right behaviours matched correct-solution priming; on GPQA subgoal setting rose to 6.5 vs 0.7 per question with no score gain (both about 12%) | Gandhi et al. 2025 (a26) | S. Training, 3B models |
| Multi-constraint planning is out of reach | TravelPlanner: GPT-4 final pass rate 0.6% of 1,225 intents; others 0% | Xie et al. 2024 (b11) | S. Constraint heavy, not pure MEA |
| LLMs on Tower of London | Raw score of 36: GPT-3.5 7, GPT-4 8, Claude 2 2, Llama2 0; failures were rule-violating moves and wrong descriptions of reached state | Loconte et al. 2024 (b12) | S. 2023 models, text adaptation |
| Human subgoal choice at bottlenecks | With two shortest Hanoi paths people chose the one-bottleneck path in 72% of cases; subgoaling model also 72%. Subgoal choices fit betweenness centrality; N=806, 30 random graphs, 11,117 graph tasks. Initial plan depth matches minimum subgoals needed (1 to 8) | Donnarumma 2016 (b13, d19); Correa 2023 (b15); Eluchans 2025 (b14) | E (K20) |
| Goal-free problems reduce MEA and improve schema learning in humans | No effect sizes obtained. Classroom study N=111: higher far transfer and higher acquisition load for goal-free | b22, a12, b24, a10, d06, d08 | M, thin (K19) |
| MEA teaching-model meta-analyses (1.431; 0.920 over 18 articles) | Teaching packages, quality unknown, full text not opened | b20, b21, d21 | D (K23): do not use |
| GPS protocol match rates, 16x isomorph ratios | Recalled, not read | a01-a03, a17, b27 | M (K24): unverified |

## 4. Mechanisms and models

Each mechanism is written so an engineer can build it as code plus one model slot (SCHEMA section 1: code decides, model fills slots).

**4.1 GPS / STRIPS core.** State = set of facts. Operator = (preconditions, add list, delete list). Difference = goal facts not true in the current state. Difference table = map from difference type to candidate operators.
```
solve(state, goal, depth):
  while diff = goal - state:
     d = pick(diff)            # which difference first: code (largest, or bottleneck-first, see 4.4)
     for op in table[d]:
        if preconds(op) subset of state: state = apply(op, state); break
        else: sub = solve(state, preconds(op) - state, depth+1)   # recurse on blocked precondition
              if sub ok: state = apply(op, sub.state); break
     if no op works: return fail
     if achieved goals were deleted: flag / undo   # Sussman protection
```
In an LLM setting the model proposes the difference and operator in one slot each; code applies the operator to the state when the domain is formal.

**4.2 MEDAKA (Li and Kingsford 2026), the only direct LLM test.** The prompt asks for three things: recursive goal decomposition, algebraic derivation of the needed action (gap size to action size), and per-step state tracking (restate every vessel's content after each action). Domain: liquid mixing with continuous quantities, 189 problems, tags linear / nonlinear / coupling / multi-goal / distractor. Failure modes it fixes in search-style prompts (AoT+): trial-and-error parameter guessing, state hallucination and drift, locally correct but globally inconsistent arithmetic (fixing one component, disturbing another; example: goal 4 L at (36.71, 26.67, 36.62)% reached (36.7, 40.0, 23.3)%; another trace emptied a vessel and reused it as if full) (c04). Implement: (a) after every action, code or model rewrites the full state; (b) a "derive the action from the gap" slot; (c) if the action is blocked, new subgoal. Costs 1.8-3.8x CoT tokens.

**4.3 MAP (modular planner).** Modules: subgoal decomposer, monitor (validates each move against rules), tree search (look-ahead), state evaluator. Ablation on 3-disk Hanoi: full 74%; no monitor 27% (31% invalid moves); no decomposer 50%; zero-shot GPT-4 11%. Implement the monitor as plain code: reject illegal moves, return the reason.

**4.4 Subgoal choice rules.** Three candidate rules for "which subgoal next":
- nearest difference (classic GPS; fails on Sussman and on river crossing where the right move increases distance);
- bottleneck-first (humans do it 72% of the time on Hanoi; betweenness centrality fits subgoal choice, N=806). Compute betweenness on the state graph when it is small enough; otherwise ask the model to name the step "every solution must pass through";
- ordering with protection: choose subgoals so earlier achieved goals are not deleted; check after each move that achieved goals still hold (Sussman fix).
No LLM study compares these rules. All three are untested as selection rules for LLMs.

**4.5 ADaPT as-needed recursion.** Try the task. On failure, decompose into subtasks, run each, recurse only on subtasks that fail. Avoids decomposing what works. No always-decompose ablation, no token cost published (d16).

**4.6 Search with evaluator (ToT, RAP).** Generate k next states, evaluate each (value prompt), keep best b. ToT b=5 74% vs CoT 4.0% on Game of 24. RAP uses the model as world model and runs MCTS. Cost is many calls.

**4.7 Operators as code (Thought of Search).** The model writes `successors(state)` and `is_goal(state)` once. Search runs outside the model. 100% on four tasks with about 2-4 model calls. Needs a formal state.

**4.8 Per-step voting and red flags (MAKER).** Split the task into minimal steps. At each step sample until one answer leads another by k_min=3 votes. Discard answers that are too long or badly formatted ("red flags"). Per-step error rate p sets cost: gpt-4.1-mini p=0.0022 projected $3.5K for 1,048,575 steps.

**4.9 External verifier loop (LLM-Modulo).** Model proposes a plan, a checker returns the first violated step, model revises, up to 15 rounds. Blocksworld 82%, Logistics 70%, Mystery 10%.

**4.10 Why the Hanoi results are hard to read.** Output length (10 tokens per move), tokenizer and format change outcomes (d20). Memory of seen continuations (c16, c17). Obfuscation drops results (d15, d18). Treat Hanoi as a test of execution plus memory, not of pure planning.

## 5. What holds up

**Holds (E).**
- Plain, non-reasoning LLMs are poor at Blocksworld-type planning, much worse once symbols are renamed (GPT-4 34.3% to 4.3% to 2%; o1-preview 97.8% to 52.8% to 37.3%). Three sources.
- Obfuscated or counterfactual variants lower scores; scores correlate with default scores, so success mixes recall and reasoning.
- Decomposition into subgoals and as-needed recursion help agents (ADaPT, least-to-most). Caveat: ADaPT has no always-decompose ablation or cost.
- Exact external checks beat soft self-checks on rule-checkable steps (82% Blocksworld; 23.65% to 98.2%), and at equal compute majority vote beats LLM generative verification until about 8x compute.
- Pure difference reduction fails on interacting goals (Sussman). Subgoal order and protecting achieved goals are required.
- Structured prompting adds little on top of native long reasoning (GPQA: +2.9, +3.1, -3.3).
- Humans pick subgoals at bottlenecks (72%).

**Contested (C).** The Apple "collapse" and the Lawsen reply. Output budget explains N>=12; Apple saw collapse near N=8-9, so early stopping or an execution limit also exists. Giving the algorithm did not help in Apple's test, but a generator-function request succeeded in Lawsen's; these test different things (full move list vs program). MAKER shows execution is possible with voting. No clean verdict. GPT-5.4 gains nothing from MEDAKA while Claude and Gemini gain 10-50 points on hard tags; the cause is unexplained (possibly a stronger default reasoning style, or a ceiling).

**Failures and non-replications.** There is no independent replication of MEDAKA, ADaPT or MAP in what we read. No replication of the human goal-free effect could be read for effect sizes. A classroom study (d08, N=111) found far-transfer gain but higher load, which conflicts with the pure load-reduction story. Vollmeyer shows the strategy, not the goal type, carries the effect.

**Moderators.**
- Model strength: gains are largest where the CoT baseline is weak. Total gains over CoT (computed from c01): Claude +16.7, Gemini +16.4, LLaMA-3.3 +14.0, GPT-4o +11.2, Gemma4-4B +5.3, GPT-5.4 +4.2, Gemma4-2B +4.2. Open-weight small models did not gain on nonlinear problems.
- Problem structure: linear problems are saturated (Claude 95.1 to 97.3); gains sit on nonlinear, coupled, multi-goal and distractor items.
- Domain: only continuous water-vessel tasks measured for MEA. Discrete-domain transfer untested.
- Prompt-to-class match: GPT-4 stacking-specific CoT 59.3% vs 6.89% for a progression-proof CoT (b04). Generalising instructions across sizes fails.
- Thinking mode: never tested for MEA.
- Budget: MEA costs 1.8-3.8x tokens.

**Interventions that worked.** Explicit state restatement; recursion on blocked steps; a validity monitor (decomposer + monitor + search took 3-disk Hanoi from 11% to 74%); external exact verifier; per-step voting for long execution; model-written code for operators; decomposition only when needed.

**Interventions that did not.** Step-specific CoT outside its class; self-consistency on the table-to-stack task (lowered accuracy, b04); generative-verifier scaling at low compute; CoT on reasoning models; giving the algorithm in Apple's Hanoi test (collapse stayed).

## 6. Language models

**Baselines, non-reasoning.** GPT-4 on plain Blocksworld 206/600 (34.3%); InstructGPT-3 41/600; GPT-3 6/600. Mystery (deceptive) GPT-4 26/600 (4.3%), randomised 12/600 (2%). Versions differ: the later Planning Abilities paper (c24) gives 1/600 for GPT-4 on Mystery; never merge the two. One PlanBench table version prints a typo (14/600 as 0.23%; correct is 2.3%); the cross-check could not find it in the version re-read (d15). Human baseline: 39/50 (78%). GPT-4 TravelPlanner 0.6% of 1,225. Tower of London: GPT-4 8 of 36, other tests normal.

**Reasoning models.** o1-preview 587/600 on 3-5 block problems, Mystery 317/600 (52.8%), randomised 224/600 (37.3%), falls on larger instances. Fast Downward is 100% in 0.265 s, so a classical planner is the reference for solvable formal items. With an external verifier o1-preview hard Blocksworld goes 23.65% to 98.2% at about 2.7x cost.

**What MEA prompting changed.** Only one study: Claude-Sonnet-4.6 77.8 to 94.5, Gemini-3-Flash 65.6 to 82.0, GPT-4o 25.7 to 36.9, LLaMA-3.3-70B 26.6 to 40.6, Gemma4-4B 55.7 to 61.0, Gemma4-2B 26.3 to 30.5, GPT-5.4 74.3 to 78.5 (same as AoT+). Synthetic tasks, thinking off, one group, no replication. Pass@1 beats CoT pass@3 for Claude (94.5 vs 86.8) and Gemini (82.0 vs 67.2) at 2.0-3.1x tokens. Pass@3 is an any-of-3 metric, not equal-token: a real test should use majority vote.

**Decomposition and subgoal agents.** ADaPT (ALFWorld 71.6 vs 43.3), MAP (Hanoi 3-disk 11% to 74%), MiRA/SGO (WebArena-Lite 23.0% to 32.1%), least-to-most (99.7% vs 16.2%), ToT (74% vs 4.0%), RAP (6-step 0.26 vs 0.40 for CoT GPT-4: RAP loses in that cell; it wins at 2 and 4 steps). ALFRED top subgoal prediction alone: 20% (c31, headline only).

**Long execution.** MAKER 1,048,575 steps with zero errors via voting; cost scales with per-step error (haiku-4.5 0.1839, $71.2K; llama-3.2-3B cannot vote). A per-step error of 1 in 1,000 would fail a million-step task.

**Internals.** Probes decode Hanoi state but the model fails to use it; steering helps (41% to 73%). We cannot do this through an API. It motivates writing the state out each step.

**Memorisation.** At n=8 Hanoi, about 40% of the time the model reused earlier continuations. Hanoi is template-friendly. A scaffolded vs plain comparison on renamed Hanoi does not exist.

**Training angle.** Chain-of-computation transformers get over 99% on Blocksworld and Pancake and Hanoi to 20 disks (c18): the failure is missing procedure, not architecture. Out of scope for a scaffold.

**Reasoning-model interaction.** GPT-5.4 gain is zero over AoT+; CoT on reasoning models +2.9, +3.1, -3.3 (GPQA); at matched tokens non-thinking is as good or better at low complexity. Prior: gap-driven prompting helps weak or non-thinking models and little on thinking ones. Untested for MEA directly.

## 7. What our agent should take

Status marks follow SCHEMA: [E] established, [S] single source, [C] contested. Evidence ids are claims.jsonl K-numbers with evidence ids in brackets.

### Add now (established)

1. **Exact check after every operator on rule-checkable subgoals; return the first violated step.** Part: G2/G3, S4/S5. [E] K26, K22 (d11, d13, d14). Soft self-check per step is not worth adding. Caveat: the K22 lines are one research group.
2. **Protect achieved subgoals: after each move, code checks that earlier achieved subgoals still hold; order subgoals so they do not undo each other.** Part: O5 / S6 subgoal step. [E] K21 (a07, b30, c23) as a classical result. No LLM measurement of the gain, so it is a cheap code check, not a prompt claim.
3. **Decompose blocked steps into subgoals.** Part: O3/O5 at S6. [E] K10 (a28, c28, b10, d16). The "as-needed over always" part is untested: see Test first.
4. **Do not stack structured step prompts on top of a reasoning model's native thinking.** Part: G11. [E] K27 (d03-d05). Consistent with G7.
5. **Run each O5 test on a symbol-renamed twin; treat Hanoi/Blocksworld wins on plain names as possibly memory.** Part: G (test hygiene). [E] K17, K18, K30 (a22, b03, d15, d18, c16, c17).
6. **Floor and reference arms for planning items: plain agent, and a classical planner or checker where the item is formal.** Part: G7. [E] K05, K06 (a22, b03, c25).
7. **When the solution is long, ask for a compact procedure or program, not the full move list.** Part: G budget/format. [C] K13 (Lawsen is preliminary), but it costs nothing; add it as a format rule and measure it.

### Test first

| Item | Part | Status | Evidence | Why test |
|---|---|---|---|---|
| Gap-driven O5 step: write the gap, derive an operator for it, recurse on a blocked precondition | O5 | [S] | K01, K02 (c01, d01, d03) | One group, synthetic task, thinking off, no equal-token test, GPT-5.4 gain zero |
| Explicit full-state restatement after every operator | S4/S5, O5 | [S] | K03 (c03, d01) | Cheapest piece, worth 3.5-7 points in the paper |
| Operator choice by gap size vs arbitrary operator order | O5 | untested | K28 (d01) | Core of MEA, never ablated |
| Monitor (invalid-move reject) and decomposer split | G2, O3/O5 | [S] | K11 (b08, c06-c08) | 27% vs 74% on Hanoi, one paper |
| Gap-driven O5 vs majority vote at equal tokens | G7, G11 | [S] | K04 (c05, d02) | pass@3 is any-of-3; MEDAKA costs 1.8-3.8x |
| One-step lookahead check of predicted state after each operator | O5 | [S] | K09 (a24, c27) | RAP loses to CoT at 6 steps in one cell |
| Operators as code with exact search | O5 | [S] | K29 (a29, d17) | 100% on four tasks, formal states only |
| Per-step voting on the weakest operator | G5/G12 | [S] | K15 (a21, d10, d11) | No equal-compute test against more reasoning |
| Progress check against subgoals to detect stuck state | S6 trigger | [S] | K12 (c19, c20) | Stuck errors 48.41% to 39.87% |
| Bottleneck rule for subgoal choice | O5/S6 | human [E], LLM none | K20 (b13, b15, d19) | Never tried on LLMs |
| As-needed vs always-decompose | O3/O5 | [S] | K10 (d16) | ADaPT has no ablation or cost |
| Instruction generality across sizes (O5 text vs tuned exemplars) | O5 | [S] | K07 (b04) | 59.3% vs 6.89% by prompt match |

Dropped: classroom MEA meta-analyses (1.431, 0.920) K23; GPS protocol match rates K24 (unverified); human goal-free effect sizes K19 (unread). The probing/steering and training results (K16, K25) are out of scope for an API scaffold.

## 8. Concrete tests on our bench

Rule for all tests: both arms get the same total token budget (counting setup, G7). The scaffold arm spends part of it on the MEA step; the plain arm spends all of it on CoT or a vote. Use pass@1 with majority vote, not any-of-k. Each test also runs on a renamed-symbol twin. Run with thinking off and with thinking on. Expected effects below are priors from the paper numbers, not measurements.

| Test | Item type | Arms (equal tokens) | Metric | Expected effect |
|---|---|---|---|---|
| T1 Gap step vs vote | Blocksworld 3-6 blocks, water-jug, liquid mixing, Hanoi 3-6 disks, with validator | (a) CoT x3 + majority vote; (b) O5 with gap/operator/recurse, one try, same total tokens | validated solve rate | Thinking off: +5 to +15 points on nonlinear or multi-goal items, near zero on easy items. Thinking on: about 0 (prior from GPT-5.4) |
| T2 State restatement ablation | Same items | O5 with vs without full-state rewrite each step | solve rate; invalid-move rate | -3 to -7 points without it, mostly on multi-step items |
| T3 Operator-choice ablation | Items with a difference table (Blocksworld, jugs) | gap-chosen operator vs arbitrary operator order, both with state tracking | solve rate; moves per solution | Unknown; if gap choice matters, 5+ points |
| T4 Exact check vs soft check vs more samples | Rule-checkable planning items | (a) more samples + vote; (b) model self-check per step; (c) code check per step with first violation fed back | solve rate at equal tokens | (c) > (a) > (b) per K26; large gain for (c) if the checker is sound |
| T5 As-needed vs always decompose | Mixed easy/hard items | recurse only on failure vs always decompose | solve rate; tokens | As-needed saves tokens at equal accuracy |
| T6 Achieved-goal protection | Sussman-style and interacting-goal items | O5 with vs without protect-achieved code check | solve rate on interacting items | Large gain on interacting items; none on independent ones |
| T7 Bottleneck vs nearest-difference subgoal | Graph or Hanoi-like items with two equal paths | model-named bottleneck first vs nearest gap first | solve rate; steps | Unknown; the 72% human prior suggests better |
| T8 Renamed twin | All above | plain vs scaffold on renamed symbols | gap between plain and renamed score | Scaffold narrows the gap if it carries reasoning, not recall |
| T9 Long-solution format | Hanoi 8-15 disks | full move list vs generator function | validated correctness | Function format wins at N>=12 (Lawsen) |
| T10 Per-step vote on the weakest operator | Long execution items | one sample per step vs k=3 vote vs one longer reasoning pass at equal tokens | steps to first error | Vote wins when per-step error is low enough to converge (MAKER) |

## 9. What does not transfer, and why

- **Human protocol-match claims.** GPS matched thinking-aloud protocols on a few protocols judged by the authors. This says nothing about which prompt helps an LLM. [M]
- **Goal-free learning effects.** They concern people acquiring schemas under working-memory limits. An LLM does not learn during a single problem; our agent only has the memory lines. The Vollmeyer result (strategy, not goal type, is the cause) also warns against reading them as "remove the goal".
- **Classroom MEA meta-analyses.** Teaching packages of unknown quality. Dropped.
- **Working-memory-based hardness (Hanoi isomorphs, 16x).** The difference came from human working-memory load on rules. An LLM's load is context and output length, which is not the same.
- **Hanoi collapse numbers.** Dependent on tokenizer, output format and memory of seen continuations. Do not read them as planning ability.
- **MEDAKA numbers on continuous vessels.** Algebraic derivation of action sizes suits continuous quantities. It may not carry to discrete symbolic or open-ended tasks. Untested.
- **RL behaviour studies (Gandhi), probe/steering, chain-of-computation training.** Need weights or training. Out of scope for a scaffold on an API model.
- **MEA with only a nearest-difference rule.** Fails when the right move increases the gap and when goals interact. The schema must not use difference size as the only selection rule.
- **Search-heavy methods (ToT, RAP, LATS).** Hundreds of thousands of calls on Blocksworld in projection. Conflicts with G7 and G11 unless the operators are code.

## 10. Open questions

1. Does the gap-driven step help when the base model already thinks at length? (Only indirect evidence: GPT-5.4 tie, CoT +2.9/+3.1/-3.3.)
2. What are the real GPS protocol numbers (Newell and Simon 1961/1972, Ernst and Newell 1969)? Not retrievable this session.
3. What are the effect sizes and N for Sweller and Levine 1982, Owen and Sweller 1985, Ayres 1993? Unread.
4. Which MEDAKA piece matters: operator choice by gap size, or only state tracking and recursion? Does it transfer to discrete domains (Blocksworld, Hanoi, code)?
5. Does protecting achieved goals or goal ordering help LLMs? No study measures it. About 39% of GPT-4 Blocksworld plans miss the goal even under relaxed checks (d15), but the cause is not separated.
6. Per-step voting or exact verification versus more reasoning budget, by step type, at equal compute (partly answered: vote beats generative verifier; exact check wins on rule-checkable steps).
7. How much of Hanoi/Blocksworld success is memory? No scaffolded-vs-plain comparison on renamed Hanoi.
8. Does ADaPT as-needed beat always-decompose, and at what token cost? No independent replication.
9. Does a bottleneck rule improve LLM subgoal choice?
10. Why does GPT-5.4 not gain while Claude and Gemini gain 10-50 points on hard tags?
11. Is the Apple collapse a reasoning limit or a budget and format artefact? (Both appear true at different N.)
12. Does MEA prompting hold up outside the authors' own synthetic testbed and group?

## 11. Sources

Marks: [V] opened this session (full text, HTML or page text), [M] snippet or recalled only.

**Founding and human work**
- Newell, Shaw, Simon (1959) Report on a general problem-solving program. [M] https://www.rand.org/pubs/papers/P1584.html (RAND PDF 403)
- Newell and Simon (1961) GPS, a program that simulates human thought. [M] https://www.science.org/doi/10.1126/science.134.3495.2011
- Ernst and Newell (1969) GPS: a case study in generality and problem solving. [M] (book, no URL)
- Wikipedia, General Problem Solver. [V] https://en.wikipedia.org/wiki/General_Problem_Solver
- Wikipedia, Means-ends analysis. [V] https://en.wikipedia.org/wiki/Means%E2%80%93ends_analysis
- Wikipedia, Sussman anomaly. [V] https://en.wikipedia.org/wiki/Sussman_anomaly
- Fikes and Nilsson (1971) STRIPS. [M] https://doi.org/10.1016/0004-3702(71)90010-5
- Sussman anomaly and non-linear planning (Sussman 1975; Chapman 1987). [M] https://doi.org/10.1016/0004-3702(87)90092-0 and https://doi.org/10.1016/0004-3702(87)90092-7
- Laird, Newell, Rosenbloom (1987) Soar. [M] https://doi.org/10.1016/0004-3702(87)90050-6
- Larkin, McDermott, Simon, Simon (1980). [M] https://doi.org/10.1126/science.208.4450.1335
- Sweller, Mawer, Ward (1983). [M] https://doi.org/10.1037/0096-3445.112.4.639
- Sweller (1988) Cognitive load during problem solving. [M] https://doi.org/10.1207/s15516709cog1202_4
- Sweller and Levine (1982). [M] https://doi.org/10.1037/0278-7393.8.5.463
- Owen and Sweller (1985). [M] https://doi.org/10.1037/0022-0663.77.3.272
- Ayres (1993). [M] https://doi.org/10.1006/ceps.1993.1027
- Vollmeyer, Burns, Holyoak (1996). [M for full text; abstract and references read, d06] https://doi.org/10.1207/s15516709cog2001_3 (a13 lists cog2003_3, likely a wrong suffix)
- Atwood and Polson (1976). [M] https://doi.org/10.1016/0010-0285(76)90004-9
- Jeffries et al. (1977). [M] https://doi.org/10.1016/0010-0285(77)90018-8
- Simon (1975) Functional equivalence of problem solving skills. [M] https://doi.org/10.1016/0010-0285(75)90003-1 (evidence also lists .../90012-2)
- Kotovsky, Hayes, Simon (1985). [M] https://doi.org/10.1016/0010-0285(85)90009-X
- Thomas (1974). [M] https://doi.org/10.1016/0010-0285(74)90013-9
- Goel and Grafman (1995). [M] https://doi.org/10.1016/0028-3932(95)90966-2
- Donnarumma, Maisto, Pezzulo (2016). [V] https://pmc.ncbi.nlm.nih.gov/articles/PMC4830581/ and https://doi.org/10.1371/journal.pcbi.1004864
- Eluchans et al. (2025) Adaptive planning depth. [V] https://pmc.ncbi.nlm.nih.gov/articles/PMC11978448/
- Correa et al. (2023) Humans decompose tasks. [V] https://pmc.ncbi.nlm.nih.gov/articles/PMC10234566/
- Goal-free problems, collaboratively or individually (2019). [V, abstract] https://doi.org/10.21831/cp.v38i3.26914
- Cognitive load restatement of MEA (2023). [V] https://pmc.ncbi.nlm.nih.gov/articles/PMC10796771/ ; Biological evolution and human cognition (2024). [V] https://doi.org/10.3389/fpsyg.2023.1330345
- Human cognitive architecture as an intelligent natural information processing system (2025). [V] https://pmc.ncbi.nlm.nih.gov/articles/PMC11939522/
- Desirable difficulties vs cognitive load (2025). [V] https://pmc.ncbi.nlm.nih.gov/articles/PMC12432286/
- Example-free instruction and worked examples (2021). [V] https://pmc.ncbi.nlm.nih.gov/articles/PMC8379662/
- Clinical reasoning processes review (2019). [V] https://doi.org/10.3946/kjme.2019.140
- Two Markov solution process models (Psychometrika 2026). [V, intro only] https://pmc.ncbi.nlm.nih.gov/articles/PMC13121837/
- Meta-analyses of MEA learning model (2023), dropped: [M] https://doi.org/10.24042/djm.v6i2.18137 ; [M] https://doi.org/10.33487/edumaspul.v7i1.6490

**LLM and AI studies**
- Li and Kingsford (2026) MEDAKA. [V] https://arxiv.org/abs/2610.24928 ; https://arxiv.org/html/2610.24928v1
- Valmeekam et al. (2022) PlanBench. [V] https://arxiv.org/abs/2206.10498
- Valmeekam et al. (2023) On the planning abilities of LLMs. [V] https://arxiv.org/abs/2302.06706
- Valmeekam et al. (2023) critical investigation. [V] https://arxiv.org/abs/2305.15771 ; https://arxiv.org/html/2305.15771
- Valmeekam, Stechly, Kambhampati (2024) LLMs still can't plan; can LRMs? [V] https://arxiv.org/abs/2409.13373
- Valmeekam et al. (2024) Planning in Strawberry Fields. [V via d14; b32 snippet] https://arxiv.org/abs/2410.02162 ; https://arxiv.org/html/2410.02162
- Stechly, Valmeekam, Kambhampati (2024) Chain of thoughtlessness. [V] https://arxiv.org/abs/2405.04776
- Stechly et al. (2023) GPT-4 doesn't know it's wrong. [M] https://arxiv.org/abs/2310.12397
- Kambhampati et al. (2024) LLMs can't plan, but can help planning in LLM-Modulo. [V] https://arxiv.org/abs/2402.01817 ; https://arxiv.org/html/2402.01817
- Shojaee et al. (2025) The Illusion of Thinking. [V] https://arxiv.org/abs/2506.06941 ; https://ml-site.cdn-apple.com/papers/the-illusion-of-thinking.pdf ; https://machinelearning.apple.com/research/illusion-of-thinking
- Lawsen (2025) The Illusion of the Illusion of Thinking. [V] https://arxiv.org/abs/2506.09250 ; https://arxiv.org/html/2506.09250
- Meyerson et al. (2025) MAKER, million-step task. [V] https://arxiv.org/abs/2511.09030 ; https://arxiv.org/html/2511.09030
- Webb, Mondal, Momennejad (2025) Modular Agentic Planner. [V] https://pmc.ncbi.nlm.nih.gov/articles/PMC12485071/ ; https://arxiv.org/abs/2310.00194
- Hao et al. (2023) RAP. [V] https://arxiv.org/abs/2305.14992
- Kazemi et al. (2023) LAMBADA. [V] https://arxiv.org/abs/2212.13894
- Gandhi et al. (2025) Cognitive behaviors. [V] https://arxiv.org/abs/2503.01307
- Yao et al. (2023) Tree of Thoughts. [V] https://arxiv.org/abs/2305.10601
- Prasad et al. (2023-24) ADaPT. [V] https://arxiv.org/abs/2311.05772 ; https://arxiv.org/html/2311.05772
- Zhou et al. (2023) Least-to-most. [V] https://arxiv.org/abs/2205.10625
- Katz et al. (2024, v3 2026) Thought of Search. [V] https://arxiv.org/abs/2404.11833 ; https://arxiv.org/html/2404.11833
- Xie et al. (2024) TravelPlanner. [V, abstract and intro] https://arxiv.org/abs/2402.01622
- Loconte et al. (2024) Tower of London in LLMs. [V] https://pmc.ncbi.nlm.nih.gov/articles/PMC11490853/
- Pereira and Zuidema (2026) Transformers struggle to use their emergent world model. [V] https://arxiv.org/abs/2608.07077
- Su et al. (2025) Limits of emergent reasoning in agentic frameworks. [V] https://arxiv.org/abs/2510.15974
- Utsho et al. (2026) Complexity-induced limits. [V] https://arxiv.org/abs/2604.13371
- Futuhi and Sturtevant (2026) Planning with transformers: chain of computation. [V, abstract and outline] https://arxiv.org/abs/2607.17710
- Wang et al. (2026) Subgoal-driven framework for long-horizon agents (MiRA). [V] https://arxiv.org/abs/2603.19685
- Shrager, Pitman, Golec (2026) Executable archaeology. [V] https://arxiv.org/abs/2610.36341
- Logeswaran et al. (2022) Few-shot subgoal planning. [V, one figure only] https://arxiv.org/abs/2205.14288
- Meincke, Mollick, Mollick, Shapiro (2025) Prompting Science Report 2. [V] https://arxiv.org/abs/2506.07142
- Singhi et al. (2025) When to solve, when to verify. [V] https://arxiv.org/html/2504.01005
- Snell et al. (2024) Scaling test-time compute. [V] https://arxiv.org/abs/2408.03314
- Wu et al. (2023) Reasoning or reciting. [V] https://arxiv.org/html/2307.02477
