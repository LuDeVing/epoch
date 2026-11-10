# Automated planning (STRIPS, PDDL): deep document

*Subfield C05.07. Focus: actions with preconditions and effects (Fikes and Nilsson; Ghallab et al.). Schema link: O5 work backwards. Evidence ids (a01 to d16) point to evidence_a-d.jsonl; claim ids (K01 to K24) point to claims.jsonl; corrections are from critique.md (cross-check 2026-11-10). Related subfields researched in parallel (links only): Search over thoughts; Tree of Thoughts; Language Agent Tree Search; Logic programming and knowledge representation; Proof planning and repair; Neural and LLM proof search; Interactive theorem proving; Cognitive conflict and impasse; Compression at inference time.*

**Honesty note.** The classical items (STRIPS, Bylander, Graphplan, HSP, FF, Fast Downward, PDDL, the Ghallab book) were not opened (a01 to a06, a10, a27, a28, c01, c02). They are described from memory and from the two competition papers that were opened (a07, a09). All LLM numbers come from papers that were opened. Most of them come from one lab (Valmeekam, Stechly, Kambhampati and co-authors), which also argues for LLM-Modulo. Independent groups are named where they exist. No 2026 models were tested in any source we found. No direct test of backward search for LLM planning exists (K18).

## 1. What it is

Classical planning asks: given a start state, a goal, and a set of actions, find a sequence of actions that turns the start into the goal.

- A **state** is a set of true facts (for example `on(A,B)`, `clear(A)`, `handempty`).
- An **action** has **preconditions** (facts that must be true to apply it) and **effects** (an add list of facts that become true and a delete list of facts that become false).
- A **plan** is an ordered list of ground actions. It is **valid** if each action's preconditions hold when it runs, and the final state contains every goal fact.
- A **domain** file lists the action schemas. A **problem** file lists objects, the start state and the goal. In PDDL these are two files.

Why this matters to our agent. Many reasoning problems have this shape: a state, moves that need conditions, and a target. A model that cannot track "what is true now" and "what does this move require" fails on them. The planning literature gives (1) a clean formal model of that skill, (2) benchmarks with sound checkers, and (3) many measured LLM results, including how a checker in a loop changes them.

Scope. Deterministic, fully observed planning, plus LLM work on it. Numeric and temporal extensions are noted only briefly (a09).

## 2. History and theories in depth

### 2.1 STRIPS (1971) and its semantics
Fikes and Nilsson (SRI, 1971) defined an action by a precondition list, a delete list and an add list over a world model of logic formulas (a01, c01; Wikipedia page read, b01). The search method was means-ends analysis: pick a difference between current state and goal, choose an action that reduces it, set its preconditions as a subgoal, recurse. This is backward-flavoured reasoning: from what you want to what must come before. Lifschitz (1986) later gave STRIPS a clean state-transition semantics: result = (state minus delete list) plus add list (a28). Status: from memory, unopened.

### 2.2 Complexity (Bylander 1994)
Deciding whether a propositional STRIPS problem has a plan is PSPACE-complete. Restricted classes are NP-complete or polynomial. Finding a shortest plan is harder than finding any plan (a02, b01). Meaning for an agent: there is no general cheap way to be sure no plan exists. "Prove no plan" can be as hard as planning itself. Small, structured domains are tractable.

### 2.3 Planning graphs and backward search (Graphplan 1997)
Blum and Furst built a layered graph of facts and actions with mutual-exclusion links, then searched it backward from the goal (a04). It was much faster than older partial-order planners and led to SAT-based planning. This is the clearest classical case of searching backward from goals with pruning. Unopened.

### 2.4 Heuristic search planning (HSP, FF, Fast Downward)
The turn that made planners fast: derive a heuristic automatically from the problem by relaxing it (ignore delete lists), then search forward. HSP (Bonet and Geffner) did this (a05). FF (Hoffmann and Nebel) uses relaxed-plan length, enforced hill-climbing and "helpful action" pruning (a06). Fast Downward (Helmert) translates PDDL to a multi-valued state form and uses a causal-graph heuristic (a10). All unopened. Key point: **modern classical planners mostly search forward from the start with a goal-distance heuristic. Backward regression is one option, not the winner.** So "work backwards" has no classical proof of being better in general. Its support for LLMs must come from elsewhere (section 6.6).

### 2.5 PDDL and the competitions
PDDL was written for the AIPS-98 competition so planners shared one syntax: typed objects, predicates, actions with `:precondition` and `:effect`, optional ADL features (a03, a07). Long and Fox (2003, opened, a07/a08): the 2002 event had 26 domains with 20 instances each (nearly 1000 instances). Hand-coded control planners (TLPlan, TALPlanner, SHOP2) gave high quality plans with dramatic speed, because a human wrote domain-specific control knowledge. Fox and Long (2003, a09) added numeric fluents and durative actions in five levels; level 1 is plain STRIPS. Haslum et al. (2019, a27) is the modern PDDL text (unopened).

Lesson for LLM agents: domain-specific knowledge written by a human beats general search on speed and plan quality (a08). The LLM version of this is the "write a domain-specific program" results in section 6.4.

### 2.6 The LLM-era framing
- Planning ability of LLMs was first measured with PlanBench (Valmeekam et al. 2022, a11, b24, c27).
- Kambhampati's position (2024, a17, b17, d15): LLMs are approximate retrievers and idea generators, not sound planners. Pair them with external sound critics ("LLM-Modulo").
- Complicating views: reasoning models (o1) improved sharply (a15); Shojaee et al. claim collapse at high complexity (b18); critics call that partly an artefact (b19). See K15 and K22 (contested).

## 3. Core findings with exact numbers

Status: E established (2+ independent sources), S single-source, C contested. Numbers were re-checked against PDFs in critique.md.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Plain GPT-4 writes valid Blocksworld plans about one time in three | 206/600 (34.3%) one-shot natural language; 210/600 (34.6%) zero-shot; one-shot CoT 214/600 (35.6%); Instruct-GPT3 41/600 (6.8%); GPT-3 6/600 (1%) | a11, b02, b24, c03, a12 (K01) | E |
| Average over many IPC-style domains is lower | GPT-4 about 12% valid plans averaged across domains | b02, d15 | E |
| Disguising names (Mystery Blocksworld) collapses GPT-4 | one-shot 26/600 (4.3%); zero-shot 1/600 (0.16%); randomized names 12/600 (2%); Instruct-GPT3 14/600 (0.23%) deceptive, 6/600 randomized | c04, b03, d11, a14 (K02, K24) | E |
| Reasoning-model jump on Blocksworld | o1-preview 587/600 (97.8%); o1-mini 340/600 (56.6%); Fast Downward 600/600 in 0.265 s vs 40.43 s for o1-preview | a15, b07, c07 (K03, K17) | E |
| o1 on obfuscation | Mystery BW zero-shot 247/600 (41.6%); one-shot 317/600 (52.8%); randomized 224/600 (37.3%) | c07, critique item 2 | E |
| o1 length cliff | 97.8% overall vs 23.63% on 20 to 40 step plans (110 instances) | b07, a15 (K03) | E on this data; cliff location C (K22) |
| Logistics, graph colouring, Sokoban with o1 | Logistics 94% (200 instances), randomized Mystery 52%; graph colouring o1-mini 96% vs GPT-4 16% (b09) or o1-preview 94% in LRM-Modulo (c09), not reconciled; Sokoban o1-preview 12.7%, o1-mini 10.9% (55 instances) | b09, c09 | S |
| Sound verifier plus back-prompt (VAL, up to 15 rounds) | Blocksworld 82% (41/50, 3.68 rounds avg), Logistics 70% (35/50, 3.31 rounds), Mystery BW 5/50 (10%, 7.0 rounds). **The 50 instances per domain were ones GPT-4 had already failed**, not a random sample. Logistics used only the 179 instances solvable in 550 search steps | b05, c06, a17, critique item 5 (K11) | E |
| Same loop on 100 fresh Blocksworld instances | 40% no backprompt; 55% LLM+LLM; 88% (2310.08118) or 87% (2402.08115) LLM+VAL. Binary VAL feedback only 60%; first-error 87%; all-errors 83% | c15, a21, d04 (K05) | E (same authors, same data in two papers) |
| Gain is mostly sound checking plus more samples | blind resampling with a sound verifier 68% (k=15), 72% (k=25) vs 87% with first-error feedback; self-consistency over 15 samples 42% | d04, d06 (K20) | S |
| LLM as verifier is unreliable | 61/100 correct; 54 true positives, 38 false positives (84.45% of invalid plans passed), 7 false negatives. Plan-only critic: Blocksworld FP 6.5% (25/382), FN 15.48% (24/155); Mystery FP 18.55%, FN 97.09% | c15, d05 (K06) | E |
| Self-correction hurts | Natural Plan: self-correction lowered Trip Planning accuracy for all models; stronger models lost more (drops are in a figure, not read) | d13, c17 | E |
| Verifier loop does not close the obfuscation gap | Mystery BW standard 4%, sound first-error 8%, 25-sample resampling 14% | d12 (K20) | S |
| Verifier loop dynamics | with an LLM verifier accuracy falls as rounds increase; with a sound verifier it rises monotonically to an asymptote; resampling prompts cost fewer tokens than growing backprompts | d06 | S |
| CoT only helps when tailored | GPT-4 table-to-stack (261 instances): zero-shot 3.83%; zero-shot CoT 4.98%; universal algorithm 51.3%; stacking-specific 59.3%; progression-proof 6.89%. GPT-4-Turbo 19.1 / 21 / 40.6 / 37.1 | b10, c14, b28 (K07) | S |
| LLM+P (LLM writes PDDL problem, Fast Downward solves) | Blocksworld 90% vs LLM-as-planner 20% (20 tasks per domain, 7 domains, 200 s limit). Other domain cells garbled; Floortile 0. Fails without an example problem | b11, c11, a18 (K08) | E |
| LLM-written PDDL domain models | best model 94% valid PDDL, 25% heuristically equivalent (7 LLMs, 9 domains) | c20, b15, a24 (K10) | E |
| Corrected LLM action models | Fast Downward with the model corrected by humans or validator: 95% Household, 100% Logistics; LLM planner alone 15% / 0%; VAL-backprompted LLM likely 48% / 33% (garbled table). Failures "only due to goal translation errors" | c12, b14, a20 (K10) | S (human in the loop) |
| Goal translation to PDDL | GPT-3.5 about 67-75% on some 8-block tasks, near 100% on others; fails on numbers or ambiguity | a23 | S |
| LLM-written search code (Thought of Search) | Blocksworld 502/502 (0.56 to 9.7 s); Game of 24 1362 instances, 1361 solvable solved, 1.92 to 6.83 s; ToT 75% on 100 medium problems with about 100 calls each; 1.2 to 2.8 human-feedback iterations per function | a22, b16, d10, b27 (K09, K23) | E that it works; S on trust without a human |
| Generalised-plan programs written by GPT-4 | fraction of 30 tasks solved: Forest 1.00, Delivery 0.90, Gripper 0.90, Ferry 0.80, Heavy 0.60, Spanner 0.10, Miconic 0.01; no-debug Delivery 0.10; failures: 40% Python exceptions, 34% plan semantics, 13% syntax, 13% timeout | a19, b12, b13, c13 (K14) | S |
| Atomic planning skills are weak | PlanBench execution reasoning GPT-4 141/500 (28.2%); verification 191/600 (31.8%). ACPBench GPT-4o CoT 2-shot 78.40% multiple choice, lowest task 52.50% (validation); 22 LLMs plus o1 | b25, c19 (K13) | E |
| Even lenient scoring leaves errors | with delete and precondition relaxed, 39% of GPT-4 plans still wrong | b26 | S |
| Fine-tuning without checks | fine-tuned GPT-3 on 1000 Blocksworld instances 122/600 (about 20%) | b02, c06 | S |
| Precondition-tracking instruction tuning | Llama-3-8B: Blocksworld 28% to 94%, Mystery BW 1% to 64%, Logistics 11% to 79% (15 iterations, detailed VAL feedback). Possible contamination | b20, c23 (K12) | S |
| Natural-language planning degrades with size | Trip Planning exact match GPT-4 31.1%, Gemini 1.5 Pro 34.8%, GPT-3.5 7.3%, GPT-4o 3.7%; all below 5% at 10 cities. TravelPlanner GPT-4-Turbo 0.6% | c17, d14, c16 (K04) | E |
| Critic loops on travel and scheduling | TravelPlanner GPT-4o 8.33% to 23.89%, Claude-3.5-Sonnet 4.4% to 25%; Trip Planning GPT-4o 3.43% to 40% | c18, b17 (K11) | E (hand-written critics, no cost accounting) |
| Unsolvable detection | o1-preview Blocksworld: 27% flagged, 19% empty plan, 54% full invalid plan; randomized Mystery BW 16% flagged, 79% full plan; 11.5% of solvable Mystery items called impossible | a16, b08, c08, d07 (K21) | S |
| Reasoning collapse at high complexity | three regimes: plain models win at low complexity, thinking models at medium, both collapse at high. Disputed: Tower of Hanoi N=15 as a function prompt restores accuracy; River Crossing N>=6 unsolvable | b18, b19, d08, d09 (K15, K22) | C |
| Humans | 39/50 (78%) valid on Blocksworld; 35 of 39 (89.7%) optimal. LLM help: 49 unassisted vs 48 assisted, no significant difference; 3 of 48 accepted wrong plans | b04, b06, c05 (K16) | S |
| Backward chaining with a sub-goal loop (logic, not STRIPS) | PaLM 540B ProofWriter-PUD Depth-5: +44% relative over CoT, +56% over forward Selection-Inference; PrOntoQA Depth-5 +37%; 11.8x fewer calls than forward at Depth-5. Plain backward CoT not better than forward CoT | d01, d02, d16 (K19) | S |
| Reverse thinking by training | +13.53% over student zero-shot, +6.84% over best distillation baseline on 12 datasets | d03 | S |
| Executability in virtual homes | VirtualHome 88 tasks: executability 18% to 79% after mapping each step to the nearest admissible action, with some loss of correctness | c21 | S |
| Direct PDDL prompting of reasoning models | success over 5 domains: o1 63.4%, Claude 3.7 Sonnet Thinking 63.4%, Claude 3.7 58.1%, Gemini 2 Flash Thinking 35.5% | c22 | S |

## 4. Mechanisms and models

### 4.1 State-transition model (the thing to implement)
```
State  = frozenset of ground facts
Action = (name, params, pre_pos, pre_neg, add, delete)
applicable(s, a) = pre_pos <= s and pre_neg.isdisjoint(s)
progress(s, a)   = (s - delete) | add            # Lifschitz semantics
valid(plan)      = every applicable(s_i, a_i), s_{i+1} = progress(s_i, a_i), goal <= s_n
```
Code can run `valid` exactly. This is what VAL does. The message to give back is the **first failing step and its unmet precondition** (d04: 87% with first-error, 60% with binary yes/no, 83% with all errors).

### 4.2 Forward versus backward search
- **Forward (progression):** from the start state, apply applicable actions. Easy to implement and check. High branching factor.
- **Backward (regression):** from the goal set G, pick an action `a` that adds some fact in G and deletes none of G. New goal `G' = (G - add(a)) | pre(a)`. Stop when G' is contained in the start state. Branching can be lower, but regressed states can be inconsistent, and the benefit depends on the domain.
- Modern planners mostly go forward with a relaxed-plan heuristic (a05, a06). Regression appears in Graphplan-style extraction (a04) and means-ends analysis (a01).

For an LLM agent, O5 can be the regression step above, **with the set arithmetic done by code** and the model only choosing which action to regress through. That keeps the model on proposing and code on state bookkeeping, which is the LLM's weak part (K13).

### 4.3 Means-ends analysis (STRIPS)
Loop: compute the difference between state and goal; choose an action whose effects reduce it; if its preconditions fail, make them a subgoal; recurse; apply; continue. This is O5 and O3 (decompose) in one move. It can undo earlier goals, so a full final check matters.

### 4.4 Delete-relaxation heuristic
Ignore delete lists and count layers until every goal fact appears; the count (or relaxed-plan size) estimates distance. Implementation: a fixpoint over facts (a05, a06). A cheap agent analogue: count unmet preconditions in code to rank candidate moves.

### 4.5 LLM-Modulo loop (generate, test, back-prompt)
```
for round in 1..R:
    plan = LLM(problem, last_feedback)
    ok, first_error = VAL(domain, problem, plan)     # sound, code
    if ok: return plan
    last_feedback = first_error
return best_so_far
```
Facts to build on: a sound verifier rises to an asymptote; an LLM verifier degrades each round (d06); resampling prompts that do not grow cost fewer tokens (d06); about 3 to 4 rounds were enough on average on the hard subset (b05); o1-preview saturated in 7 rounds on hard Blocksworld at 98.2% (c09). A cap of about 7 to 15 rounds matches the evidence; no stopping-rule study exists.

### 4.6 Translate-then-solve (LLM+P)
The LLM writes the PDDL problem file (needs one worked example, a18); a planner solves; the LLM translates back. The weak link is translation (goal translation errors were the only failures in Guan, c12; 25% equivalence in Oswald, c20). Check translated problems on hand-made cases.

### 4.6b Write-the-simulator (Thought of Search)
The LLM writes `successors(state)` and `is_goal(state)` once; plain BFS or DFS searches (a22). Sound and complete if the code is right. Needed 1.2 to 2.8 interactions with exact error messages (d10). Silent errors are unmeasured (K23).

### 4.7 Generalised planning by program
The LLM summarises the domain, proposes a strategy, writes Python, debugs with VAL on training tasks; the program then solves larger unseen tasks (a19). Debugging is essential (no-debug Delivery 0.10 vs 0.90). Domain dependence is large (Miconic 0.01).

### 4.8 Backward chaining with a sub-goal loop (LAMBADA)
Four small model modules (fact check, rule selection, goal decomposition, sign agreement); code runs the loop (d01). One sub-goal per call, no redundant forward inferences (d16: in forward Selection-Inference only 29% of steps had no redundancy). Backward chain of thought written in prose without the loop gave no gain (d02). The loop structure carries the gain, not the direction of the words.

## 5. What holds up

**Holds up (multiple sources, or sound-checked):**
- Plain LLMs generate valid classical plans poorly and fall with plan length and size (K01, K04). Seen in PlanBench, Natural Plan, TravelPlanner, ACPBench by different groups.
- A sound verifier returning the first failing precondition beats an LLM critic by a wide margin (K05, K06). The self-correction harm is replicated in Natural Plan (d13), an independent group.
- LLM as translator or code writer, with a classical planner or plain search doing the work, beats LLM-as-planner (K08, K09). Seen by Liu, Katz, Silver, Guan.
- The weakest skill is applicability and state tracking, not goal understanding (K13).

**Failures, caveats and moderators:**
- **Name familiarity.** Gains vanish under obfuscation (K02, K24). The verifier loop does not close it (Mystery BW 4% to at best 14%, d12). Even o1-preview drops from 97.8% to 41.6% / 52.8% (c07). Memorisation versus lost commonsense cues is not separated (d11).
- **Plan length.** o1-preview 97.8% overall, 23.63% on 20 to 40 steps (b07).
- **Prompt specificity.** CoT works only when matched to the problem class (K07). The progression-proof prompt gave 6.89%.
- **Verifier gain composition.** Much of the loop gain is resampling checked by a sound verifier: 68 to 72% blind vs 87% first-error vs 40% base (d04). So feedback content adds about 15 to 19 points over blind resampling, and sound resampling alone adds about 28 to 32 points over the base.
- **Selection effect.** The headline 82% and 70% were on instances GPT-4 had already failed. Read it as "rescues most previously failed items", not "solves 82% of all items" (critique item 5).
- **Human help.** The 95% and 100% in Guan had human or validator repair; not automatic (critique item 9). Thought of Search also used human error messages.
- **Hand-written critics.** TravelPlanner and Trip Planning gains used critics written per task; engineering cost is not counted (K11).
- **Contested collapse.** Shojaee et al. (b18, d09) report collapse; Opus and Lawsen (b19, d08) show artefacts: Tower of Hanoi N=15 fixed by function output, River Crossing N>=6 unsolvable. Shojaee's reply accepted the River Crossing flaw and held that collapse persists; the Blocks World R1 collapse appeared at N=4 at temperature 0 but changed with sampling (d09). Status contested (K15, K22).
- **Fine-tuning.** A small gain without checks (about 20%, c06). A large gain with explicit precondition-and-effect reasoning plus validator feedback (28% to 94%, b20), but that is training, with contamination risk, and not a scaffold.
- **Humans.** 78% valid on Blocksworld; LLM suggestions did not help people (b06).

**Interventions that worked:** sound verifier with first-error feedback; translate-then-classical-solve; LLM-written transition code; run-and-debug for LLM-written programs; mapping each step to the nearest admissible action for executability (c21).
**Interventions that did not:** generic CoT; LLM self-critique; binary yes/no feedback (only 60%); fine-tuning without checks; LLM suggestions for human planners; forced self-correction in Natural Plan.

**Independence.** Independent groups: Liu (LLM+P), Silver (generalised programs), Katz/Oswald/Kokel (IBM), Xie (TravelPlanner), Zheng (Natural Plan), Shojaee (Apple), Goebel and Zips, Huang. K01 to K06 count independent sources honestly, not by paper count.

## 6. Language models

### 6.1 Base behaviour
Autonomous plan generation: GPT-3 1%, Instruct-GPT3 6.8%, GPT-4 34.3% on Blocksworld (600 instances); about 12% averaged across IPC-style domains (a12, b02, d15). In a relaxed check, 39% of GPT-4 plans were still wrong even with delete and precondition rules relaxed, so errors are not only small ones (b26). Plan execution reasoning 28.2%, verification 31.8% (b25). ACPBench: weakest on applicability and validation; GPT-4o 52.5% on the weakest task (c19). Humans reach 78%.

### 6.2 What changed behaviour, and by how much
| Change | Effect | Source |
|---|---|---|
| GPT-3 to GPT-4 | 1% to 34.3% (Blocksworld) | a12, a11 |
| GPT-4 to o1-preview | 34.3% to 97.8% (Blocksworld); Mystery BW 0.16 to 4.3% to 41.6 to 52.8% | a15, c07 |
| Generic CoT | 3.83% to 4.98% (table-to-stack) | b10 |
| Problem-specific CoT | 3.83% to 59.3% | b10 |
| Sound verifier, first-error, 15 rounds | 40% to 87% (100 instances) | d04 |
| Sound verifier, blind resampling | 40% to 68 to 72% | d04 |
| LLM verifier | 40% to 55%, degrades with rounds | c15, d06 |
| LLM+P with classical planner | 20% to 90% (Blocksworld) | c11 |
| LLM-written successor and goal code | 100% on 502 Blocksworld tasks; 100% on 1362 Game of 24 | a22 |
| Instruction tuning on precondition tracing | 28% to 94% (Llama-3-8B) | b20 |
| Obfuscation | 34% to 0.16 to 4.3% (GPT-4); 97.8% to 37 to 53% (o1-preview) | c04, c07 |
| Plan length 20 to 40 steps | 97.8% to 23.63% (o1-preview) | b07 |

### 6.3 Cost
o1-preview took about 40 s per Blocksworld instance and cost about 42 USD per 100 instances, vs 0.265 s for Fast Downward at 100% (b07, b09). Hidden reasoning tokens matter in any comparison (K17). Resampling loops cost less than growing backprompts (d06). Tree of Thoughts needed about 100 calls per Game of 24 instance for 75%, while the code approach used a few one-time calls for 100% (b16, b27).

### 6.4 Programs beat in-head planning when the domain is tractable
Writing the simulator or a generalised program moves the work from the model's weak skill (state tracking) to code. It depends on debug feedback (Silver 0.10 vs 0.90; Katz 1.2 to 2.8 interactions) and on domain (Miconic 0.01).

### 6.5 Models cannot say "no plan"
o1-preview flagged only 27% of unsolvable Blocksworld goals and 16% of randomized Mystery ones; 54% and 79% returned a full impossible plan (d07). It called 11.5% of solvable Mystery items impossible. No study tested an existence-proof step.

### 6.6 Backward direction in LLMs
No STRIPS test exists. Indirect: LAMBADA backward chaining with a sub-goal loop gave +44% relative over CoT and 11.8x fewer calls on ProofWriter Depth-5, but plain backward CoT was no better than forward CoT (d01, d02). Reverse-thinking training gave +13.53% on 12 datasets (d03; training, not scaffold). So our O5 should be a looped sub-goal procedure with code-held goal sets, not a "think backwards" sentence.

### 6.7 Reasoning-model controversy
See section 5. Treat length cliffs as real but with uncertain location; sweep and report ranges (K22).

### 6.8 Other uses (snippet only)
SayCan (c25), LLM-DP (c24) and Pallagani et al. (a26, c26) were not opened. Huang et al. (c21) was.

## 7. What our agent should take

Marks: [E] established, [S] single-source, [C] contested. Schema parts: G guardrail, S state, O operator, M memory.

### Add now (established)
1. **Code-held state with an applicability check; return the first failing precondition (S4 TEST, S5 REVISE, G2).** When a task has a state-transition form, code computes `applicable` and `progress` and returns the first unmet precondition to the model. Sound verifier with first-error feedback 40% to 87% vs an LLM critic 55%; the LLM's weakest skill is applicability. [E] (K05, K06, K13). Ids: d04, c15, a21, c19, b25.
2. **The model never verifies a plan itself (G2, G5, G10).** The LLM verifier passed 84.45% of invalid plans; self-correction lowered Natural Plan accuracy. [E] (K06). Ids: c15, d05, d13. Fits 4b "unstructured self-reflection".
3. **Prefer program-held search over in-head search when a transition function can be written (S3, O5 tool).** The model writes `successors` and `is_goal` once; code searches. [E] for the pattern (K08, K09), with the caveat that it needs a validator and a worked example. Ids: a22, b16, c11, a19.
4. **Cap verify-and-retry at about 7 to 15 rounds; prefer fresh resampling with the first error over an ever-growing history (S5, G7, G11).** A sound verifier rises to an asymptote and an LLM one degrades. [E] for sound versus LLM (K05); the round-cap number is [S]. Ids: d06, b05, c09.
5. **Test on renamed variants (bench design, G7).** Disguised-name items expose pattern recall; a gain must survive renaming. [E] (K02). Ids: c04, c07, d11.
6. **Check any text-to-formal translation (S1 to S2).** Translating text into goals, preconditions and effects is the weak link: goal translation errors; only 25% of generated domains equivalent. Run 3 hand-made transitions before trusting. [E] (K10). Ids: c20, c12, a23.

### Test first
1. **O5 as looped regression with a code-held goal set (O5).** Model picks an action that adds a goal fact; code computes `G' = (G - add) | pre`; loop until G' is in the start state; then forward-check. [S] (K18, K19). Ids: d01, d02, d16 are logic-proof only; no STRIPS test. Test T1.
2. **Existence check before long search (G6 still holds: submit best attempt if none exists).** Code reachability test, or a "prove a plan exists" step. [S] (K21). Id: d07.
3. **Per-step precondition trace written by the model (S4).** Evidence is training-based (b20, K12), single-source; as a scaffold unproven. [S]. Critic false-pass rate with a trace is unknown.
4. **Model writes a transition program for planning-like items and tests it on hand-made transitions (S2, O6).** [S] on trust (K23). Ids: d10, a22.
5. **Unmet-precondition count in code to rank candidate moves (S7).** Classical basis [M] (a05, a06 unopened). [S] for LLM use.
6. **Gain per round and stopping rule for verifier loops (G7, G12).** [S] (K20).
7. **Plan-length gating (S0, G12).** Route long-plan items (over about 15 steps) to program-held search. [C] (K22).
8. **Task-matched decomposition prompts versus generic CoT (S2, S3).** Numbers single-source [S] (K07); the "generic CoT does not help" part agrees with G11 and 4b.

### Memory (M)
- Log per class: plan length, whether names were familiar or renamed, and error type (unmet precondition, wrong goal, syntax). [S]
- Keep solved transition programs as reusable entries by domain (links to the subgoal-library slot). [S] (a19 shows programs generalise to larger tasks in some domains).

## 8. Concrete tests on our bench

All arms at equal total tokens, hidden reasoning tokens counted. Report tokens per solved item.

| # | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 | 100 Blocksworld + 100 Logistics instances in 3 plan-length bins (under 8, 8 to 20, over 20 steps) | (a) plain; (b) forward simulation with code-held state; (c) O5 looped regression with code-held goal set; (d) prose "think backwards" | valid-plan rate by bin; tokens per solved item | (c) beats (d) by 10+ points; (c) vs (b) unknown; if (c) does not beat (b), O5 is demoted for STRIPS-type items |
| T2 | same items, renamed (deceptive and random names) | plain vs best scaffold | score drop versus unrenamed | scaffold drop under 10 points vs plain drop of 30+ points (a verifier loop alone gave only 4 to 14%) |
| T3 | same items | critic arms: none; LLM critic on plan only; LLM critic with code-made precondition trace; code check with first error | false-pass rate on labelled invalid plans; final accuracy | plan-only critic FP 6 to 19% (d05); trace-fed lower; code check 0% by construction |
| T4 | 100 items, rounds 1 to 15 | feedback = none, binary, first error, all errors; fresh resample vs growing history | accuracy per round; tokens per round | first-error beats binary by 20+ points (d04: 87 vs 60); curve flat by about round 7 |
| T5 | 50 solvable + 50 unsolvable (unreachable goal fact) | plain; plus code reachability check; plus "prove a plan exists" step | correct flag rate; false alarm rate | plain about 27% flagged (d07); code check near 100%, false alarms under 5% |
| T6 | 100 planning-like items (state puzzles, resource scheduling) | in-head scaffold vs model-written successor and goal test with plain BFS | accuracy; tokens; silent-error rate on an independent hand-made transition set | program arm 90%+ in tractable domains; silent-error rate unknown (K23) |
| T7 | length sweep, 5 to 40 steps, unsolvable removed, fixed output form | plain reasoning vs scaffold | accuracy curve and cliff location with range | scaffold shifts the cliff right; cliff is not an output-budget artefact |
| T8 | 50 Blocksworld instances, human anchor | scaffold vs published 78% valid | valid rate; tokens | scaffold reaches 78% or better on 4 to 8 block instances |
| T9 | 50 text-to-formal problems | model writes preconditions and effects; with and without a 3-transition test | action model equivalence rate | test lifts equivalence well above the 25% baseline (c20) |

## 9. What does not transfer, and why

- **Classical planner speed and guarantees.** Fast Downward solved 600/600 in 0.265 s (a15). Our agent is not a planner; use it only as a ceiling.
- **Blocksworld and Logistics scores.** Likely in training data; renamed variants fall to near zero (K02). Do not carry numbers to open problems.
- **VAL.** A sound checker needs a formal domain and problem. Most of our tasks have none. The gain transfers only where we can write a checker (code or tests). TravelPlanner critics were hand-written per task (c18).
- **Fine-tuning results.** PDDL-Instruct 28% to 94% (b20) is training with contamination risk; our agent does not train.
- **Human-in-the-loop PDDL repair.** Guan's 95% and 100% used human feedback (c12); not automatic.
- **Backward chaining proof results.** LAMBADA is Horn-clause logic with a fixed rule form (d01); STRIPS regression adds delete effects and negative preconditions.
- **Relaxation heuristics.** Need a formal model; open prose problems have none.
- **Human 78%.** One group, N=50; not a ceiling (K16).
- **Reasoning-model collapse studies.** Confounded by token limits and unsolvable items (K22).
- **PDDL2.1 numeric and temporal extensions** (a09). Our items are mostly discrete; no LLM evidence in our sources.

## 10. Open questions

1. Does regression beat forward simulation for an LLM at equal tokens? No study (K18).
2. How much of a scaffold gain is code-held state versus longer reasoning at equal total tokens, hidden ones included?
3. Does the o1 length cliff hold for 2026 models, and does a verifier loop move it? (K22)
4. Marginal gain per backprompt round, and a stopping rule.
5. How often is LLM-written transition code wrong in ways its own tests miss? (K23)
6. Is the Mystery drop memorisation or lost cues? Needs a control that keeps names and changes dynamics (K24).
7. False-pass rate of a critic that sees a precondition trace.
8. Does an existence-proof step fix unsolvable detection? (K21)
9. Do planning gains transfer to non-PDDL tasks, and how much critic engineering is needed?
10. Can a scaffolded model beat the human 78% on the same instances, and at what token cost?
11. The GPT-4 Logistics rows (28/200, 15/200) and Guan Table 2 cells are garbled in extracted text and need a visual read.
12. Classical sources (a01 to a06, a10) are unopened; Graphplan speedups and FF competition results are absent.

## 11. Sources

[V] opened this session or in the cross-check; [M] snippet or memory only.

**Classical planning**
- [M] Fikes and Nilsson (1971) STRIPS. https://www.ai.sri.com/pubs/files/tn043r-fikes71.pdf and https://doi.org/10.1016/0004-3702(71)90010-5 (a01, c01)
- [M] Bylander (1994) Computational complexity of propositional STRIPS planning. https://doi.org/10.1016/0004-3702(94)90081-7 (a02)
- [M] McDermott et al. (1998) PDDL. https://www.cs.yale.edu/homes/dvm/papers/pddl-ipc98.pdf (a03)
- [M] Blum and Furst (1997) Graphplan. https://doi.org/10.1016/S0004-3702(96)00047-1 (a04)
- [M] Bonet and Geffner (2001) HSP. https://doi.org/10.1016/S0004-3702(01)00108-4 (a05)
- [M] Hoffmann and Nebel (2001) FF. https://www.cs.cmu.edu/afs/cs/project/jair/pub/volume14/hoffmann01a.pdf (a06)
- [V] Long and Fox (2003) The 3rd International Planning Competition. https://www.cs.cmu.edu/afs/cs/project/jair/pub/volume20/long03a.pdf (a07, a08)
- [V] Fox and Long (2003) PDDL2.1. https://www.cs.cmu.edu/afs/cs/project/jair/pub/volume20/fox03a.pdf (a09)
- [M] Helmert (2006) Fast Downward. https://www.jair.org/index.php/jair/article/view/10457 (a10)
- [M] Haslum et al. (2019) An Introduction to the Planning Domain Definition Language. https://doi.org/10.2200/S00900ED2V01Y201902AIM042 (a27)
- [M] Lifschitz (1986) On the semantics of STRIPS. https://www.sciencedirect.com/science/article/pii/B9781483207742500191 (a28)
- [M] Ghallab, Nau, Traverso (2004) Automated Planning: Theory and Practice. https://www.elsevier.com/books/automated-planning/ghallab/978-1-55860-856-6 (c02)
- [V] Wikipedia, Stanford Research Institute Problem Solver. https://en.wikipedia.org/wiki/Stanford_Research_Institute_Problem_Solver (b01)

**LLM planning (PlanBench line)**
- [V] Valmeekam et al. (2022) PlanBench. https://arxiv.org/abs/2206.10498 (a11, b24, b25, c27, d11)
- [V] Valmeekam et al. (2023) On the planning abilities of large language models. https://arxiv.org/abs/2305.15771 (b02 to b06, b22, b26, c03 to c06)
- [V] Valmeekam et al. (2023) Planning abilities, heuristic guidance version. https://arxiv.org/abs/2302.06706 (a12 to a14)
- [V] Valmeekam, Marquez, Kambhampati (2023) Can LLMs really improve by self-critiquing their own plans? https://arxiv.org/abs/2310.08118 (c15)
- [V] Stechly, Valmeekam, Kambhampati (2024) On the self-verification limitations of LLMs. https://arxiv.org/abs/2402.08115 (a21, d04 to d06, d12)
- [V] Stechly, Valmeekam, Kambhampati (2024) Chain of thoughtlessness. https://arxiv.org/abs/2405.04776 (b10, b28, c14)
- [V] Valmeekam, Stechly, Kambhampati (2024) LLMs still can't plan; can LRMs? https://arxiv.org/abs/2409.13373 (a15, a16, b07, b08, c07, c08, d07)
- [V] Valmeekam et al. (2024) Planning in strawberry fields. https://arxiv.org/abs/2410.02162 (b09, c09)
- [V] Kambhampati et al. (2024) LLMs can't plan, but can help planning in LLM-Modulo frameworks. https://arxiv.org/abs/2402.01817 (a17, b17, c10, d15)
- [V] Gundawar et al. (2024) Robust planning with compound LLM architectures. https://arxiv.org/abs/2411.14484 (c18)

**LLM plus planner, code, models**
- [V] Liu et al. (2023) LLM+P. https://arxiv.org/abs/2304.11477 (a18, b11, c11)
- [V] Silver et al. (2023) Generalized planning in PDDL domains with pretrained LLMs. https://arxiv.org/abs/2305.11014 (a19, b12, b13, c13)
- [V] Guan et al. (2023) Leveraging pretrained LLMs to construct and utilize world models. https://arxiv.org/abs/2305.14909 (a20, b14, c12)
- [V] Katz et al. (2024) Thought of Search. https://arxiv.org/abs/2404.11833 (a22, b16, b27, d10)
- [V] Xie et al. (2023) Translating natural language to planning goals. https://arxiv.org/abs/2302.05128 (a23)
- [V] Oswald et al. (2024) LLMs as planning domain generators. https://arxiv.org/abs/2405.06650 (a24, b15, c20)
- [V] Kokel et al. (2025) ACPBench. https://arxiv.org/abs/2410.05669 (c19)
- [V] Verma et al. (2025) Teaching LLMs to plan (PDDL-Instruct). https://arxiv.org/abs/2509.13351 (b20, c23)
- [V] Goebel and Zips (2025) Can LLM reasoning models replace classical planning? https://arxiv.org/abs/2507.23589 (c22)
- [V] Huang et al. (2022) Language models as zero-shot planners. https://arxiv.org/abs/2201.07207 (c21)
- [M] Pallagani et al. (2023) Understanding the capabilities of LLMs for automated planning. https://arxiv.org/abs/2305.16151 (a26)
- [M] Pallagani et al. (2024) On the prospects of incorporating LLMs in automated planning. https://arxiv.org/abs/2401.02500 (c26)
- [M] Dagan, Keller, Lascarides (2023) Dynamic planning with an LLM. https://arxiv.org/abs/2308.06391 (c24)
- [M] Ahn et al. (2022) SayCan. https://arxiv.org/abs/2204.01691 (c25)

**Benchmarks and reasoning limits**
- [V] Xie et al. (2024) TravelPlanner. https://arxiv.org/abs/2402.01622 (c16)
- [V] Zheng et al. (2024) Natural Plan. https://arxiv.org/abs/2406.04520 (a25, c17, d13, d14)
- [V] Shojaee et al. (2025) The illusion of thinking. https://arxiv.org/abs/2506.06941 (b18, d09)
- [V] Opus and Lawsen (2025) The illusion of the illusion of thinking. https://arxiv.org/abs/2506.09250 (b19, d08)

**Backward reasoning**
- [V] Kazemi et al. (2022) LAMBADA: backward chaining for automated reasoning. https://arxiv.org/abs/2212.13894 (d01, d02, d16)
- [V] Chen et al. (2024) Reverse thinking makes LLMs stronger reasoners. https://arxiv.org/abs/2411.19865 (d03)
