# Hierarchical task networks: deep document

*Subfield C05.08. Written from evidence_a-d.jsonl, claims.jsonl (K01-K28) and critique.md in this folder. Evidence ids (a01..d22) point to those files. Status marks: [E] established, [S] single-source, [C] contested.*

## 1. What it is

Hierarchical task network (HTN) planning solves a problem by splitting tasks into smaller tasks using known recipes.

- A **primitive task** is something you can do directly (an operator with preconditions and effects).
- A **compound task** cannot be done directly. It has one or more **methods**.
- A **method** is a pair (task, task network): "to do this task, do these subtasks, in this order, if this condition holds".
- Planning starts from an initial task network and replaces compound tasks by method bodies until only primitive tasks remain. That list is the plan. (a01)

The knowledge sits in the method library, written by a person who knows the domain. The planner does not invent the split. It looks it up and checks the conditions.

For our agent this maps to operator O3 (decompose into 2-4 sub-problems). The schema question: when should O3 use a library of known methods, when may the model improvise, and what must be checked after each split?

## 2. History and theories in depth

**Roots.** Splitting a goal by known procedures goes back to Newell and Simon and early planners such as NOAH. The formal account came in 1994.

**Erol, Hendler, Nau 1994 (AAAI) and 1996 (Annals of Math and AI).** (a01-a04, b01-b03, a05)
- Three task types: goal, primitive, compound. A method is m = (t, d).
- Whether a plan exists depends mostly on restrictions on non-primitive tasks and on ordering.
- No restrictions, not totally ordered: undecidable, even with no variables (two unordered non-primitive tasks can encode the intersection of two context-free languages). Holds even for a fixed domain.
- Totally ordered, no variables: EXPTIME, PSPACE-hard. With variables: EXPSPACE-hard, in double-EXPTIME.
- "Regular" methods (at most one non-primitive task, and it comes last): PSPACE-complete without variables, EXPSPACE-complete with them. Regular methods give STRIPS-equivalent power, like a regular grammar.
- Extra power: some HTN domains cannot be written as any finite STRIPS operator set (Theorem 7). In the journal version no computable translation exists in general (Theorem 9). The authors reject the view that HTN is only an efficiency trick.

**Practical systems.**
- **SHOP (Nau et al. 1999).** Plans tasks in the order they will run, so it always knows the full current state. That allows rich preconditions (arithmetic, axioms) and keeps the algorithm simple. Logistics methods are a short ordered list of else-if rules. On log002: Blackbox 95.98 s, SHOP 0.19 s. SHOP matches or beats TLplan on plan length. (a06-a08, b28)
- **SHOP2 (Nau et al. 2003, JAIR).** Distinguished performance award at IPC-2002 (14 planners). Solved 899 of 904 problems (99%). TLPlan 894, TALPlanner 610. Allows interleaved subtasks and ordered alternative methods. (a09, a11)
- **Methods are error-prone.** At AIPS-2000 SHOP was disqualified from two domains because wrong hand-written methods produced incorrect plans. For SHOP2 the team wrote a translator from PDDL operators to methods to cut this risk. (a10)

**Later theory.**
- Bercher, Alford, Holler 2019 survey: plain HTN is undecidable; task insertion (TIHTN, free repair steps) makes it decidable but covers fewer procedures. Reasons people use hierarchy: inject expert knowledge, give several abstraction levels for explanation, involve users, model plan libraries. (a12, a13)
- Alford, Bercher, Aha 2015 tight bounds: no recursion, total order, no variables is PSPACE; variables add an exponential step; limiting recursion helps more than total ordering. Range reaches 2-NEXPTIME and 2-EXPSPACE. (b05, b06)
- Alford, Kuter, Nau 2009: restricted HTNs compile to PDDL, and partial methods with the planner choosing the order still speed search by orders of magnitude. (d19)
- IPC-2020 HTN track: the winner (HYPERTENSION) won by fast recursion and bookkeeping, not by a domain-independent heuristic. Secondhand. (b28)
- **Contested.** A critique (Lekavy and Navrat) says the 1994 expressivity edge holds only if the translation must be decidable, and the proof assumes infinitely many task labels. Seen only in a Wikipedia talk snippet; the current Wikipedia article does not mention it. Unresolved. (b04, d20)

**LLM line (2022-2026).**
- Prompting forms: Least-to-Most, Decomposed Prompting, Plan-and-Solve.
- Agent forms: ADaPT, TDAG, Plan-and-Act, ReAcTree, HyperTree Planning.
- Hybrids with real planners: ChatHTN, online method learning, LLM-written HTN heuristics.
- Skill libraries as method libraries: Voyager, Agent Workflow Memory, ASI, SkillWeaver, SkillsBench.

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Unrestricted HTN planning is undecidable; bounded forms are far cheaper | Undecidable with two unordered non-primitive tasks; regular, no variables: PSPACE-complete; no recursion, total order, no variables: PSPACE | Erol 1994/96; Alford 2015 (a02, a04, b05) | [E] K01 |
| A hand-written method library makes planning fast and near-complete | SHOP 0.19 s vs Blackbox 95.98 s (log002); SHOP2 899/904, TLPlan 894, TALPlanner 610 | Nau 1999, 2003 (a07, a09) | [E] K03 |
| Curated procedures help LLM agents on natural tasks | SkillsBench 33.9 to 50.5 (+16.6), 87 tasks, 18 configurations; +4.1 to +25.7 per configuration; natural science +28.8, software +11.6, math +9.7; 13 of 87 tasks worse | Li 2026 (d12, d14) | [S] K21 |
| Self-written skills made before solving can hurt | -8.1, -11.3, -11.5 points on three frontier configurations; curated +18.2 to +24.8 on the same | Li 2026 (d13) | [S] K22 |
| Keep the active method set small | 1 skill +18.0, 2-3 skills +19.0, 4 or more +10.1; compact +19.0 / +21.5, comprehensive +0.7 | Li 2026 (d14) | [S] K23 |
| Hand-written methods are often wrong; extra methods interact | SHOP disqualified in two AIPS-2000 domains for incorrect plans; extra methods give plans that miss effects | Nau 2003; Munoz-Avila 2025 (a10, b08) | [E] K04 |
| Plain LLM does not decompose by method | Llama-3.1-Nemotron-70B: 3-4% correct plans, 0% correct decompositions (IPC-2023 total-order HTN) | Puerta-Merino 2025 (b24) | [S] K05 |
| Decompose on demand beats up-front plan-and-execute | ADaPT (GPT-3.5) ALFWorld: ReAct 43.3, Plan-and-Execute 43.3, ADaPT 71.6; Pick2 11.8 vs 52.9; WebShop ReAct 32.0, P&E 17.0, ADaPT 44; TextCraft depth 2: 26.9 vs 78.2 | Prasad 2024 (a20-a22, b13) | [E] K06 |
| Gain grows with difficulty, shrinks where the model copes | TextCraft depth 3: 1.8 to 38.7; weak executor 3.3 to 41.7; SCAN length 16.2 to 99.7; GSM8K about 61 to 62.4; GSM8K 5+ steps 39.07 to 45.23 | Prasad 2024; Zhou 2023 (a14, a16, a22, b14, b18) | [E] K07 |
| Least-to-Most length generalisation | SCAN length: standard 16.7, CoT 16.2, L2M 99.7; last letters L=12: L2M 74.0 (2 shots) vs CoT 38.4 (8 shots) | Zhou 2023 (a14, a15, b16, b17) | [E] K07 |
| Part of the benefit is answer extraction | Decomposed Prompting MultiArith 78 to 95 (+17), GSM8K 36 to 50.6 (+14) from an extraction handler | Khot 2023 (a18) | [S] K08 |
| Plan-and-Solve sketch adds nothing after correction | GPT-4o 75.0 vs CoT 77.5 vs direct 57.5 | Miro-Lopez-Feliu 2026 (d02) | [S] K08 |
| Leaf execution, not decomposition, is the usual failure | Web agents match human subgoals 60.6-67.7% but finish 36.4% (best case, human plans); illegal steps are 89% of failed toy plans; DecomP errors are single-hop sub-answers | Aghzal 2026; Khot 2023; d03 (b27, c24, b20, d03) | [E] K09 |
| Verified LLM gap-filling in a symbolic planner is sound | 0-2 LLM calls per hidden method; unsolvable tasks rejected by verifiers; demo scale, no success rates | Munoz-Avila 2025 (a28, a29, b07, b09) | [S] K10 |
| LLMs invent plans for impossible tasks | o1-preview flagged 27% (Blocksworld) and 16% (randomized mystery) of unsolvable; 8.9% (32 of 360 episodes) in a 2026 test, best configuration 4 of 10; 1 of 1,440 solvable episodes falsely declared impossible | Valmeekam 2024; Miro-Lopez-Feliu 2026 (a26, d01) | [E] K11, K26 |
| Frontier models refuse missing-information cases less than contradictions | Missing info 19-65% vs contradictions 65-80% (GPT-5 40% vs 80%; Sonnet 4.5 19% vs 72%) | Sun 2026 (d06) | [E] K26 |
| Storing verified decompositions helps | AWM +12.0 points WebArena; ASI 40.4 vs AWM 36.3 vs static 32.7; shopping 32.6 unverified vs 36.4-40.1 verified; 84% of induction attempts rejected; SkillWeaver +31.8% relative over 160 iterations; ReAcTree +13 to +30 from retrieved subgoal examples | Wang 2024; Wang 2025; Zheng 2025; Choi 2026 (c22, d15, d16, d22) | [E] K12, K24 |
| Top-level method matters most | Removing TPM2 (logistics) or SAR2 (search and rescue) sharply lowers success; 10 problems per domain, figures only | Xu 2025 (b12) | [S] K13 |
| Task tree helps long constraint planning for strong models | TravelPlanner: HTP GPT-4o 20.0 vs CoT 4.4; Gemini 36.1 vs EvoAgent 8.9; 36.1 to 7.2 without the division step; GPT-3.5 HTP 1.7; Blocksworld 54.7 vs 35.5; Mystery 8.7 vs 0.0; Trip 36.9 vs 15.6 | Gui 2025 (a30, c15, c16) | [S] K14 |
| Task tree vs a reasoning model | HTP on GPT-4o vs o1-preview: TravelPlanner 20.0 vs 10.0; Trip 36.9 vs 31.1; at 8.7-13% of the cost; Blocksworld 54.8 vs 97.8 (loss) | Gui 2025 (d18) | [S] K28 |
| Replanning limits cascading failure | TDAG cascading-failure share 4.35% vs ReAct 32.61% (authors' benchmark); TextCraft 73.5; WebShop 64.5/45.0 | Wang 2025 (c13, c14) | [E] K15 |
| LLM critics are poor verifiers | Critic 1.8x ReAct tokens, no gain (violations 66% vs 67%), timeouts 15.0% vs 0.6%; ToT about 22x direct tokens, no corrected gain; whole-plan taxonomy critic (APB) 22% to 60% | Miro-Lopez-Feliu 2026; Sun 2026 (d02, d04, d07) | [S] K25 |
| Direct LLM planning is weak and name-dependent | GPT-4 Blocksworld 206/600 (34.3%); Instruct-GPT3 41/600 (6.8%); about 12% executable on average; back-prompting reaches 82% Blocksworld in 15 rounds; obfuscated about 10% | Valmeekam 2023; Kambhampati 2024 (a24, a25, a27, b21) | [E] K16 |
| LLM-written HTN heuristics | 780 candidates, 419 passed selection, 347 viable, 72 broke on every problem (60 of 72 assumed the wrong state type); coverage 131/139 vs best planner 134; LLM wins on nodes in 104 of 125 | Meneguzzi 2026 (b25, b26, c06) | [S] K17 |
| Knowing the algorithm is not enough | Reasoning models collapse on Hanoi near N=10 even when given the algorithm; disputed as an output-length artefact | Shojaee 2025; Lawsen 2025 (c25, d21) | [C] K19 |
| Gains depend on the executor model | ADaPT TextCraft: GPT-4o 0.58, Mistral Small 3 0.58, GPT-3.5 0.52, GPT-4o mini 0.43, R1-distill-32B 0.13, Claude-3 Haiku 0.00; ReAcTree 7B 2% vs ReAct 7%; fallback path worth 10-22 points (36 vs 58, LLaMA 70B) | d08, d10, d11 | [S] K27, K23 |

## 4. Mechanisms and models

### 4.1 Classical HTN loop (SHOP style)
1. Keep a state and an ordered task list.
2. Pop the first task.
3. If primitive and its preconditions hold: apply the operator, update the state, append it to the plan.
4. If compound: try its methods in order. For the first whose precondition holds in the current state, replace the task by the method body. If none applies, backtrack.
5. Stop when the list is empty (plan found) or all methods fail (no plan).

Planning in execution order means the state is known at every decision. That is why preconditions can be rich and the algorithm simple (a06).

Implementation notes:
- Methods are ordered if-then rules. Order is a heuristic: first applicable wins.
- Hard limits are needed because unrestricted recursion is undecidable. Use a depth cap and a node budget (K01).
- A free repair step (task insertion) makes search decidable but covers fewer procedures (K20).

### 4.2 ADaPT: decompose when the executor fails
(a20-a22, b13-b15)
1. The executor tries the task directly.
2. A code check says pass or fail. On pass, return.
3. On fail, a planner splits the task into subtasks joined by AND or OR.
4. Recurse on each subtask with a depth cap dmax (3 on ALFWorld).
5. Mean depth used tracks need: 1.9 on TextCraft depth-2 recipes, 2.8 on depth-3.

Going from dmax 1 to 2 gives most of the gain. A strong planner can help a weak executor (ALFWorld dev: executor alone 38.4, planner plus executor 58.3). The authors claim comparable LLM-call counts, not equal tokens.

### 4.3 Least-to-Most and Decomposed Prompting
- Least-to-Most: stage 1 lists simpler sub-questions. Stage 2 solves them in order, each prompt holding earlier answers (a14).
- Decomposed Prompting: a decomposer writes a program of sub-task calls to a handler library. Handlers are prompts, trained models or code. Recursive splitting (halve a list, solve, merge) generalises to longer inputs. Handlers can be swapped and tested alone (a17, a19).
- Lesson: put exact work (extraction, counting, merging) in code handlers (a18).

### 4.4 Verified gap filling (ChatHTN)
(a28, a29, b07-b09, c01-c03)
1. The symbolic planner runs with the method library.
2. When no method applies to a compound task, ask the LLM for a decomposition into primitive tasks.
3. Append a **verifier task** that checks the claimed effects in the state.
4. If the verifier fails, reject and backtrack. An unsolvable task ends with no verified decomposition, so it is rejected.
5. Learner variant (Xu and Munoz-Avila): generalise each accepted decomposition into a method, so later LLM calls drop (b10, b11).

### 4.5 Task tree with constraint separation (HyperTree Planning)
Stages: select a node, expand by rule-like decomposition, prune, decide. The active ingredient is the division step (TravelPlanner 36.1 to 7.2 without it). It needs a strong model (a30, c16).

### 4.6 Method library with an admission test
(d15-d17)
- Induce a candidate method from a trajectory.
- Admit it only if it passes an outcome test on held-out items.
- ASI rejected 84% of attempts and still beat unchecked induction.
- A weak check (no exception means verified) lets broken skills in.

### 4.7 Generate-test-select for ordering rules
Ask many models for heuristic code, run it on training problems, drop what crashes or never helps, keep survivors. 72 of 419 deployed candidates broke on every problem, so the test step is not optional (b26).

## 5. What holds up

**Holds up (several sources).**
- Theory: undecidability and restriction results are proofs, later tightened (Erol, Alford) (K01).
- A good method library makes search fast. The gain is the knowledge, not the algorithm (K03, K18).
- As-needed decomposition beats static plan-and-execute on three benchmarks (K06).
- Gains concentrate on hard items and weak executors (K07).
- Leaf execution is the usual bottleneck (K09).
- Models produce plausible plans for impossible tasks (K11, K26).
- Execution-checked admission to a method store beats unchecked (K12, K24).
- Wrong methods exist in every library, so each decomposition needs a postcondition check (K04).

**Failures and tensions.**
- Plan-and-execute is worse than ReAct on WebShop (17 vs 32) and better on TextCraft (27 vs 19). Static plans hurt only sometimes.
- The GSM8K gain is tiny (+1.4). Big wins are on tasks built to be decomposable (SCAN, last letters).
- Plan-and-Solve sketch: no corrected gain on four models.
- Self-written skills: -8 to -12 points; curated: +18 to +25 (d13).
- LLM critic as checker: more tokens, no gain, more timeouts.
- ReAcTree 7B without examples is worse than plain ReAct. ADaPT falls to 0.13 and 0.00 on weak backends.
- Llama 70B alone: 0 correct decompositions (b24).
- ChatHTN says LLM-made methods break hand-made guarantees unless verified. Voyager and AWM say learned methods help. The difference is verification; AWM does not verify and reports 18.5% of tasks where the agent ignores new actions.
- Illusion of Thinking (given algorithm still fails) vs Least-to-Most (given decomposition succeeds): different mechanism (long execution vs short chain), and disputed on output length (K19).

**Moderators.**
- Executor strength (a very weak model cannot run the subtasks; a very strong one may not need the split).
- Task decomposability (synthetic vs natural).
- Number of methods in context (more than 3 hurts).
- Presence of a fallback path (10-22 points).
- Quality of the check (strong mechanical vs weak vs LLM critic).

**Weak spots** (critique.md). Most results are demos or the authors' own baselines on older models (GPT-3.5, GPT-4o). No equal-token test at frontier level. ChatHTN and online learning come from one lab, with 10 problems per domain. Planning evidence is dominated by Blocksworld and logistics. The Valmeekam papers reuse each other's numbers. The Lekavy and Navrat critique was not opened.

**Data corrections.** The GSM8K CoT baseline is 60.97 in the text and 60.87 in the table; use "about 61". Puerta-Merino correct plans are 3% in the abstract and 4% in the body; use "3-4%". Aghzal failure categories overlap, so they do not sum to 100%. The Meneguzzi "27x" spread is the extractor's own calculation.

## 6. Language models

**Without help, LLMs do not decompose by method.** Llama-3.1-Nemotron-70B: 3-4% correct plans and 0 correct hierarchical decompositions on IPC-2023 total-order HTN. GPT-4: 34.3% Blocksworld, 4.3% deceptive Mystery, about 12% across domains. Names matter: obfuscation collapses it (a24, a25, b21, b24).

**Prompting-level decomposition.** Large wins only where the task is built to be decomposable and longer than the examples (SCAN 16.2 to 99.7; last letters 38.4 to 74.0 at L=12). Small on natural math (+1.4 GSM8K; +6.2 on 5+ step problems). A plain sketch step is not better than CoT after correction (GPT-4o 75.0 vs 77.5).

**Agent-level decomposition.**
- ADaPT on GPT-3.5: ALFWorld 43.3 to 71.6, TextCraft depth 2 26.9 to 78.2. On newer backends it holds for GPT-4o and Mistral Small 3 (0.58) but not for R1-distill-32B (0.13) or Claude-3 Haiku (0.00). No Claude 4 or GPT-5 class test exists.
- TDAG: replanning cut the cascading-failure share from 32.61% to 4.35%.
- HTP: GPT-4o 20.0 vs 4.4 CoT on TravelPlanner; GPT-3.5 gets 1.7. Beat o1-preview on two of three tasks at 8.7-13% of the cost; lost Blocksworld (54.8 vs 97.8).
- ReAcTree: a fallback path is worth 10-22 points; retrieved successful subgoal examples +13 to +30; 7B without examples is worse than ReAct.

**Where the errors are.** At the leaves, not in the plan. Web agents match human subgoals 60.6-67.7% but finish about 36%. In toy planning 89% of failed plans have precondition violations. A whole-plan critique with a taxonomy beat step-wise reflection (22% to 60%).

**Verification.** Mechanical or execution-based checks pay; LLM critics did not (1.8x tokens, no gain, timeouts 15.0% vs 0.6%). Model-written heuristic code broke on every problem 17% of the time (72 of 419).

**Impossible tasks.** Detection is rare (8.9%; o1-preview 16-27%), but false refusals were also almost absent (1 of 1,440). Reasoning models think longer on missing premises and do not abstain more.

**Libraries.** Curated helps (+16.6). Self-written before solving hurts (-8 to -12). Verified induction helps (ASI 40.4 vs 32.7 static). Four or more methods in context nearly halve the gain.

**Long execution.** Giving the algorithm does not stop collapse on large Hanoi (disputed). Keep the step list in code.

## 7. What our agent should take

Schema parts: G = guardrail, S = state, O = operator, memory = section 5 of SCHEMA.md.

### Add now (established)

| # | Item | Part | Status | Evidence |
|---|---|---|---|---|
| A1 | O3 has hard limits set in code: depth at most 2, at most 3 children, node budget. Already in the tree rules; keep, and record why (unrestricted recursion is undecidable and runs away). | O3 | [E] | K01; a02, a04, b05 |
| A2 | Every O3 split carries a code-checkable postcondition per sub-problem (what a correct sub-answer looks like, and a check where one exists). A split with no check is marked unverified. | O3, G2, G3 | [E] | K04, K09; a10, b08, b20, b27 |
| A3 | Spend verification at the leaves (sub-answers), not on the plan text. Log failures by level: plan vs leaf. | O3, G2 | [E] | K09; b20, b27, c24, d03 |
| A4 | Decompose on demand: O3 fires after a failed check or an impasse (S6), not by default. Matches G1. | G1, S6, O3 | [E] | K06, K07; a20-a22, b14 |
| A5 | After each solved sub-problem check progress, and re-split on failure rather than follow a fixed plan. | O3, S5/S6 | [E] | K15; c13, c14, c23 |
| A6 | Give O3 a no-valid-decomposition exit with a named feasibility list (missing input, missing tool, contradiction). Exit means: go to the next operator or submit best-so-far (G6). Never refuse on the first pass. The need is [E]; the exit design is untested. | O3, G6 | [E] need | K11, K26; a26, d01, d05, d06 |
| A7 | Do exact work in code, not in the model: counting, merging sub-answers, answer extraction. | O3, S4 | [E] mixed | K08, K19; a18, c25 |
| A8 | Do not use an LLM critic to check decompositions; use code checks. Candidate line for section 4b. Rests on one study, but agrees with G5 and G10. | G5 | [S] | K25; d04, d02 |
| A9 | Store a decomposition as a reusable method only after it passes an outcome test on items it was not fitted to (G3). Record the problem class with it (S9). | memory, O3 | [E] | K12, K24; d15, d16, d17 |

### Test first

| # | Item | Part | Status | Evidence |
|---|---|---|---|---|
| T1 | Curated method library at O3 vs model-improvised splits, equal tokens, natural reasoning items | O3, memory | [S] | K03, K21; d12 |
| T2 | Cap the active method set at 1-3 per item, each with applicability limits and a fallback | O3 | [S] | K23; d14, d11 |
| T3 | No self-written method pack before solving; only verified, used methods enter | O3, memory | [S] | K22; d13 |
| T4 | Gate O3 on model strength by a 20-item pilot (plain vs decomposed) | O3, G7 | [S] | K27; d08, d10 |
| T5 | Task tree with a constraint-separation step vs flat CoT vs long thinking, equal tokens | O3, G11 | [S] | K14, K28; a30, d18 |
| T6 | Code-held step list vs model-held list on growing recursive procedures | O3 | [C] | K19; c25, d21 |
| T7 | Library-first, model fills gaps with checked effects (ChatHTN pattern) | O3, memory | [S] | K10; a28, b07 |
| T8 | Top-level methods first: which template level matters | O3 | [S] | K13; b12 |
| T9 | Candidate ordering rules generated, tested on training items, survivors kept | O3, memory | [S] | K17; b26 |
| T10 | Strict method use vs one free repair step | O3 | [S] | K20; a12 |
| T11 | Code answer extraction alone vs full decomposition | G2, O3 | [S] | K08; a18, d02 |
| T12 | Depth cap 2/3/4/unbounded at equal tokens | O3 | theory [E], practice untested | K01 |

## 8. Concrete tests on our bench

All tests: both arms get the same total token budget (setup, calls and checks counted, G7). Report accuracy, tokens per item and wrong-answer rate. Use 40 items per arm unless noted, a paired design, and split results by easy and hard stratum (by plain pass rate).

| Test | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| B1 Library vs improvised (T1) | 40 natural multi-step reasoning items from 5 classes (word problems, constraint puzzles, code tracing, ARC-style rules, brain teasers) | (a) O3 with a curated 1-3 method list per class; (b) O3 with model-improvised split; (c) plain | Accuracy, tokens | (a) minus (b): +5 to +15 points on the hard stratum, none on easy. Basis: SkillsBench +16.6 |
| B2 Method-set size and fallback (T2) | Same 40 items | 1, 3, 6 retrieved methods; with and without fallback step | Accuracy, tokens | 1-3 methods beat 6; fallback +10 points |
| B3 Self-written vs verified methods (T3, A9) | Stream of 100 items per class | (a) no store; (b) store of unverified model-written methods; (c) store admitting only methods that pass a held-out check | Accuracy over second half of stream, tokens per item | (c) > (a) > (b) |
| B4 On-demand vs always-decompose (A4) | 40 multi-step items | (a) O3 only after a failed check; (b) O3 first on every item; (c) plain | Accuracy, tokens | (a) matches (b) at fewer tokens; (b) hurts the easy stratum |
| B5 Postcondition check vs none (A2, A8) | 40 items with 8 wrong methods injected | (a) per-subtask code check; (b) none; (c) LLM critic | Wrong answers passed, tokens | (a) blocks most wrong methods; (c) costs about 1.8x and does not help |
| B6 Impossible items (A6) | 30 solvable + 15 ill-posed items | (a) O3 with feasibility list and exit; (b) O3 without exit | Detection rate on ill-posed; false-exit rate on solvable | Detection up from under 10%; false exits under 5% |
| B7 Model-strength gate (T4) | 20 items per model, 3 model sizes | Plain vs O3 | Delta per model | Positive for weak and mid models on hard items; zero or negative for the strongest on easy items |
| B8 Task tree vs long thinking (T5) | 40 constraint-heavy items (itinerary, scheduling) | (a) tree with constraint separation on a standard model; (b) flat CoT on the same model; (c) reasoning model with long thinking | Constraint pass rate, tokens | (a) beats (b) by 10+ points; (a) vs (c) unknown |
| B9 Code-held steps (T6) | Recursive procedures (Hanoi-like, list recursion), N = 4 to 12 | Code-held step list vs model-held | Accuracy vs N | Gap opens above N = 8 |
| B10 Extraction ablation (T11) | 40 arithmetic items | Code extraction only vs full decomposition vs plain | Accuracy | Extraction alone recovers most of the gain |
| B11 Depth cap (T12) | 30 recursive items | Cap 2 / 3 / 4 / none | Accuracy, runaway expansions, tokens | Cap 2 equals cap 3; none produces runaways |

## 9. What does not transfer, and why

- **Complexity results.** Undecidability concerns unbounded planning with symbolic state. Our decomposer already has depth 2. The theory justifies the cap, nothing more.
- **Expressivity over STRIPS.** A theory claim, contested, with no link to LLM benefit (K02).
- **Speed results (SHOP 0.19 s vs 95.98 s).** They measure search time with an exact state model. Our agent has no formal state; cost is tokens, and the model is the search.
- **Hand-written logistics methods.** Domain knowledge was the gain. Our tasks are open and cross-domain, so we cannot write a library per domain. Only generic methods (split by case, by step, by part, work backwards) transfer, and these are already O1-O8.
- **Blocksworld and logistics numbers.** Discrete preconditions. Little evidence on math, code or research questions.
- **ADaPT and TDAG gains.** Measured on text-game and web agents with environment feedback after every action. Our items often have only a final check.
- **Fine-tuning gains (Plan-and-Act).** The scaffold does not train.
- **HTN search heuristics (IPC).** They tune search order inside a planner; we have no classical planner search.
- **Skill packs (SkillsBench).** Terminal agent packages with files, tokens not equalised. Direction only.
- **Gains on GPT-3.5.** Weak executors gain most. A strong model may gain little.

## 10. Open questions

1. Does a curated method library beat model-improvised decomposition at equal tokens on natural reasoning items? Only SkillsBench is close.
2. What does a per-decomposition check cost, and at what error rate does it pay? No source computed a break-even.
3. Does on-demand gating still help current frontier models (Claude 4 / GPT-5 class)? Depth and node budgets were never studied.
4. Does a built-in no-valid-decomposition exit cut wrong answers on open-ended items, and what is the false-exit rate on ambiguous but solvable items?
5. Does a method store of a few hundred verified entries go stale or conflict? The Hogg 2008 interaction effect rests on the ChatHTN note.
6. How much of the "decomposition" gain is extraction, format or verification?
7. Is the Lekavy and Navrat critique sound? Does it matter for choosing tasks vs goals as O3 outputs?
8. Do leaf errors dominate in math, code and research questions?
9. Does a task tree add value over long thinking at equal tokens?
10. Does method order matter more than the method set?
11. Is the Hanoi collapse an output-length artefact? Needs an exact table.

## 11. Sources

[V] = opened this session. [M] = snippet only.

- [V] Erol, Hendler, Nau 1994, HTN Planning: Complexity and Expressivity. https://cdn.aaai.org/AAAI/1994/AAAI94-173.pdf and https://www.cs.umd.edu/~nau/papers/erol1994htn.pdf
- [V] Erol, Hendler, Nau 1996, Complexity results for HTN planning. https://www.cs.umd.edu/~nau/papers/erol1996complexity.pdf
- [V] Nau et al. 1999, SHOP. https://www.cs.umd.edu/~nau/papers/nau1999shop.pdf
- [V] Nau et al. 2003, SHOP2 (JAIR 20). https://www.cs.umd.edu/~nau/papers/nau2003shop2.pdf
- [V] Bercher, Alford, Holler 2019, A Survey on Hierarchical Planning. https://www.ijcai.org/proceedings/2019/0875.pdf
- [V] Alford, Bercher, Aha 2015, Tight Bounds for HTN Planning. https://cdn.aaai.org/ojs/13721/13721-40-17239-1-2-20201228.pdf
- [V] Alford, Kuter, Nau 2009, Translating HTNs to PDDL. https://www.cs.umd.edu/~nau/papers/alford2009translating.pdf
- [M] Wikipedia Talk: Hierarchical task network (Lekavy and Navrat critique). https://wikipedia.com/wiki/Talk:Hierarchical_task_network
- [V] Wikipedia, Hierarchical task network (read 2026-11-01). https://en.wikipedia.org/wiki/Hierarchical_task_network
- [V] Zhou et al. 2023, Least-to-Most Prompting. https://arxiv.org/abs/2205.10625
- [V] Khot et al. 2023, Decomposed Prompting. https://arxiv.org/abs/2210.02406
- [V] Wang et al. 2023, Plan-and-Solve Prompting. https://arxiv.org/abs/2305.04091
- [V] Prasad et al. 2024, ADaPT. https://arxiv.org/abs/2311.05772
- [V] Wang et al. 2025, TDAG. https://arxiv.org/abs/2402.10178
- [V] Erdogan et al. 2025, Plan-and-Act. https://arxiv.org/abs/2503.09572
- [V] Gui et al. 2025, HyperTree Planning. https://arxiv.org/abs/2505.02322
- [V] Valmeekam et al. 2022/2023, PlanBench. https://arxiv.org/abs/2206.10498
- [V] Valmeekam et al. 2023, On the Planning Abilities of LLMs. https://arxiv.org/abs/2305.15771
- [V] Valmeekam et al. 2024, LLMs Still Can't Plan; Can LRMs? https://arxiv.org/abs/2409.13373
- [V] Kambhampati et al. 2024, LLMs Can't Plan, But Can Help Planning. https://arxiv.org/abs/2402.01817
- [V] Xie et al. 2024, TravelPlanner. https://arxiv.org/abs/2402.01622
- [V] Munoz-Avila, Aha, Rizzo 2025, ChatHTN. https://arxiv.org/abs/2505.11814
- [V] Xu and Munoz-Avila 2025, Online Learning of HTN Methods. https://arxiv.org/abs/2511.12901
- [V] Puerta-Merino et al. 2025, A Roadmap to Guide the Integration of LLMs in Hierarchical Planning. https://arxiv.org/abs/2501.08068
- [V] Meneguzzi et al. 2026, HTN Planning with LLM-Generated Heuristics. https://arxiv.org/abs/2605.07707
- [V] Aghzal, Stein, Yao 2026, Why Do LLM-based Web Agents Fail? https://arxiv.org/abs/2603.14248
- [V] Wang et al. 2023, Voyager. https://arxiv.org/abs/2305.16291
- [V] Wang, Mao, Fried, Neubig 2024, Agent Workflow Memory. https://arxiv.org/abs/2409.07429
- [V] Shojaee et al. 2025, The Illusion of Thinking. https://arxiv.org/abs/2506.06941
- [V] Lawsen 2025, The Illusion of the Illusion of Thinking. https://arxiv.org/abs/2506.09250
- [V] Liu et al. 2023, LLM+P (table mapping garbled). https://arxiv.org/abs/2304.11477
- [V] Wang et al. 2024, Planning In Natural Language Improves LLM Search. https://arxiv.org/abs/2409.03733
- [V] Miro-Lopez-Feliu et al. 2026, Testing the Planning Claims of LLM-Based Agents. https://arxiv.org/abs/2610.22469
- [V] Fan et al. 2025, Missing Premise exacerbates Overthinking. https://arxiv.org/abs/2504.06514
- [V] Sun et al. 2026, Agent Planning Benchmark. https://arxiv.org/abs/2606.04874
- [V] SCOPE 2025, Language Models as One-Time Teacher for Hierarchical Planning. https://arxiv.org/abs/2512.09897
- [V] Choi et al. 2026, ReAcTree. https://arxiv.org/abs/2511.02424
- [V] Li et al. 2026, SkillsBench. https://arxiv.org/abs/2602.12670
- [V] Wang et al. 2025, Inducing Programmatic Skills (ASI). https://arxiv.org/abs/2504.06821
- [V] Zheng et al. 2025, SkillWeaver. https://arxiv.org/abs/2504.07079

## Source audit (2026-11-01)

Fresh auditors re-opened the sources of 11 established claims: 7 confirmed as written, 4 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **C05.08-K04** (reworded: the sources support less). Sources support that hand-written SHOP domains had mistakes in two AIPS-2000 domains and that ChatHTN found LLM decompositions interacting unexpectedly with hand methods, but 'often wrong' generalizes one team's two-domain anecdote. Corrected claim: Hand-written methods can be wrong (the SHOP team made mistakes in two AIPS-2000 domains and SHOP was disqualified from them for incorrect plans), and in ChatHTN LLM decompositions interacted unexpectedly with well-crafted hand methods, so the authors added effect-checking verifier tasks to every decomposition.
- **C05.08-K07** (reworded: the sources support less). Numbers match (SCAN length 16.2 to 99.7; GSM8K 60.97 to 62.39 in text, table shows 60.87; TextCraft depth 3 1.8 to 38.7), but ADaPT's depth-2 gain (26.9 to 78.2, +51.3) is larger in points than depth-3 (+36.9), so 'largest when the task is harder' is not shown by the TextCraft depth comparison. Corrected claim: Decomposition gain is large when the executor is weak or the task is harder than the examples (ALFWorld weak executor with atomic skills only: 3.3 to 41.7; SCAN length split with least-to-most: CoT 16.2 to 99.7; TextCraft depth 3: ReAct 1.8 to ADaPT 38.7, though the depth-2 gain, 26.9 to 78.2, is larger in points) and small where the model already copes (GSM8K overall 60.97 to 62.39, with 39.07 to 45.23 on problems needing 5 or more steps).
- **C05.08-K09** (reworded: the sources support less). Web-agent (60.6/67.7% subgoal match, 36.4% success), DecomP single-hop errors and the 89% illegal-step figure (Blocksworld/Gripper/Logistics, solvable tasks) check out, but Least-to-most says GSM8K misses are fixed by a manual decomposition, i.e. the model's own decomposition is the failure point there, which contradicts the claim's direction. Corrected claim: Decomposition quality is not always the failure point; in several settings leaf execution is: web agents match human subgoals 60.6-67.7% but finish only 36.4% of tasks, DecomP errors sit in single-hop sub-answers, and in classical planning domains (Blocksworld, Gripper, Logistics) plans with an inapplicable step make up 89% of failed plans. Counter-evidence: least-to-most prompting on GSM8K fails mainly because its own decomposition is wrong (almost all misses are solved with a manual decomposition).
- **C05.08-K16** (now single-source: the sources are not independent). Numbers match (GPT-4 206/600=34.3%, deceptive mystery 26/600=4.3%, about 12% average, 82% with back-prompting, about 10% on Mystery BW), but all listed sources are one lab (Valmeekam, Kambhampati et al., ASU): PlanBench, the Critical Investigation and the LLM-Modulo position paper (which re-reports the same results).
