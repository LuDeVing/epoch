# Means-ends analysis: deep document

*Subfield A02.02. Built from evidence_a-d.jsonl (a01-a36, b01-b28, c01-c25, d01-d22), claims.jsonl (K01-K34) and critique.md in this folder. Evidence ids are cited in brackets. "Opened" means the page or PDF text was read in this run; snippet-only sources are marked as pointers, not proof. Links to sibling subfields (not covered here): problem-solving strategies and the cycle; Soar operator selection and impasses; Soar chunking; Polya heuristics; Schoenfeld episodes; representational change; progress monitoring; verification design; adaptive stopping; LLM debugging; troubleshooting search.*

---

## 1. What it is

Means-ends analysis (MEA) is a way to solve a problem by looking at the gap between where you are and where you want to be.

The loop has four steps.

1. Compare the current state with the goal state. Name the difference.
2. Pick an operator (an action) that is known to reduce that kind of difference.
3. If the operator cannot be applied yet, its unmet preconditions become a new subgoal. Solve that first (recursion).
4. Apply the operator. Compare again. Stop when no difference is left.

Newell and Simon's definition: detect specific differences between the current structure and the goal structure, then choose actions relevant to reducing those differences [a08]. It is one case of heuristic search. It gives the search a direction. It is not a guarantee.

Three properties set MEA apart from plain forward search or free-form reasoning.

- **Difference-driven operator choice.** The link from "kind of difference" to "operator" is a table. In GPS the table was made by hand [a02].
- **A goal stack.** Unsolved preconditions are pushed as subgoals. Deferred goals wait on the stack.
- **A split between method and content.** The same loop runs on logic, algebra, or river crossing once the domain's differences and operators are supplied [a06].

Why it matters for our agent. Our schema already has the pieces: S6 (impasse, pick an operator, make it a subgoal), O3 (decompose), O5 (work backwards), and the rule that code decides transitions while the model fills one slot. MEA is the oldest worked-out version of exactly that control loop. This document asks what is known about whether the loop helps, when it fails, and what in it a language-model agent should copy.

Short version of the answer. The classical record says MEA is a useful local heuristic with known failure cases (interacting goals, needed detours, blow-up). The LLM record says explicit goal decomposition plus a code-held or explicitly tracked state helps on planning tasks for strong models, but almost all of the positive evidence for explicit MEA comes from one new preprint on one synthetic domain, with thinking mode off [c01, d22]. Several of the pieces (state ledger, final all-goals check, loop guard, code-run execution, not trusting the model as its own checker) are well supported on their own.

---

## 2. History and theories in depth

### 2.1 Logic Theorist and GPS (1955-1959)

**Logic Theorist (LT).** Newell, Shaw and Simon's 1958 paper reports that LT proved 38 of the first 52 theorems of Principia Mathematica chapter 2 (73%) using heuristics rather than brute force [a07]. About half of the proofs took under a minute. Most others took 1 to 5 minutes. A few took 15 to 45 minutes. Blind search of the same space was estimated at "hundreds or even thousands of years". When earlier proved theorems were removed from memory, LT could not prove Theorem 2.12, which it proved in about 10 seconds with them. The authors say success depended sensitively on problem order. LT itself was not yet means-ends: it used substitution, detachment, chaining and similarity tests [a07].

**GPS-I (RAND P-1584, 1959).** The report defines three goal types and three methods [a01].

- Goal 1: transform object a into object b.
- Goal 2: apply operator q to object a.
- Goal 3: reduce the difference d between a and b.
- Method 1 matches a to b, finds a difference, sets a Goal 3 to reduce it, then sets a new Goal 1 from the changed object c to b.
- Method 2 turns a into the operator's input form, then builds the output.
- Method 3 finds an operator relevant to the difference, tries it, and tries another if it fails.
- Before acting, a goal is checked for being worth the effort and likely to succeed.

The report links differences to operators through a hand-made table, ranks differences by difficulty, and uses that ranking as the criterion of progress. The authors note GPS could in principle infer the table from operator and difference lists [a02]. Difference types in the logic traces: position, connective, variable, type.

**The loop check.** In the worked logic trace (from L1 = R.(-P implies Q) to L0 = (Q or P).R), one candidate subgoal is rejected because its difference "is no easier than the difference in Goal 6" [a03]. A subgoal must be easier than its ancestor. This is the original guard against infinite goal recursion. The trace has 16 goals.

**Cost of pure difference reduction.** The trigonometry trace needed 33 goals and about 5 operator attempts that produced no change. The authors say GPS needed extra goals and methods for features, equations in one variable and learned heuristics, and followed them "only in a cumbersome fashion" [a04].

**The planning heuristic.** GPS also had a second technique: drop detail, solve the abstract problem with the same loop, then use the result as a plan. In the logic example two plans were tried. P1 failed when translated back to the real problem. P2 worked. The authors say the time lost on invalid plans must be counted against the heuristic, and that a plan may be "illusory" [a05]. No false-plan rate was ever given.

**Aim of the work.** The authors state the aim was a theory of human thinking, not an economical solver. The report gives no timing or success-rate statistics. "General" meant factoring method from subject matter [a06].

### 2.2 The human-protocol programme (1960s-1980s)

Newell and Simon (1976) say many GPS mechanisms came from think-aloud protocols and that GPS used modified depth-first search guided by differences, not best-first search [a08]. Their Human Problem Solving book (1972) holds the protocol-fit data, but it was only seen as quoted by Norvig, so no fit statistics are recorded here [a36]. Norvig quotes the book's plain statement of the loop: find the difference (distance), find what changes it (the car), find what that needs (a battery), and so on [a36].

The same 1976 lecture is candid about theory. It says the formal mathematical backing for these search ideas is "miniscule" (some theorems on alpha-beta, shortest path, and best-first with probabilistic evaluation, none for MEA) [a09].

**Hobbits-orcs and missionaries-cannibals.** These river-crossing puzzles were the main test bed for whether people run GPS.

- Greeno (1974): subjects organise moves in small subsequences. The organisation looked forward-oriented, unlike the backward-oriented GPS organisation. Learning fit all-or-none acquisition at individual states, with one exception tied to ambiguity about backward moves (the two readings of the abstract differ slightly). Seen as an abstract only [a24, d03].
- Thomas (1974): subjects plan in small subsequences, not single moves. Second-hand reports say people use MEA at first but some required steps move away from the goal and are hard. Not opened; the detour claim comes partly from a low-authority study site and must not be used as evidence [a25, d04].
- Atwood and Polson (1976), Jeffries, Polson, Razran and Atwood (1977): a three-stage process model (means-ends heuristics, memory for visited states, illegal-move detection) over four isomorphs of Missionaries and Cannibals. Changing the cover story left the number of legal moves to solution unchanged but changed illegal moves a lot. Abstract only [a23, d05].
- Simon and Reed (1976): models strategy shifts inside one task. Cited only [a32].
- Greeno (1974) "demonstrated that GPS is not directly a model of human problem solving" (as stated by Schmalhofer and Polson) [a22].

**Schmalhofer and Polson (1986)** is the best open source on the human side [a20, a21, a22, d01, d02]. They report that the Jeffries et al. model fit the (3,2) problem but could not account for the (5,3) problem "without introducing baroque ad hoc assumptions". The graphs differ: (3,2) is nearly a line, (5,3) is bushy with a short linear middle, (4,3) has two disjoint solution paths [a22]. Their own model has 11 productions and 6 parameters, and mixes two strategies that are "not integrated into a coherent mental representation": a means-ends strategy (move travellers to the goal bank) and a balance strategy (keep the outnumbering rule satisfied). Probabilities decide which fires. Evaluation rules include "avoid the backward move", subgoal protection, and a long-term store of visited states. The subgoal "all missionaries on the goal bank" is only recognised after it has been accomplished [d02].

**Hanoi.**
- Spitz, Minsky and Bessellieu (1984): with solution length held constant, steps to the first subgoal predicted difficulty [b19].
- Kotovsky, Hayes and Simon (1985): isomorphs of Hanoi with different surface rules differ greatly in difficulty. Known from citations only [a31].
- Anzai and Simon (1979): an adaptive production system matched strategy changes of one person across 4 attempts at 5-disk Hanoi, from trial and error to a recursive goal strategy. Primary paper not opened; VanLehn later reanalysed the protocol [a26].
- Clement and Richard (1997): isomorphs with identical problem spaces differ in difficulty because context steers which viewpoint on the action is chosen [b20, b21].
- Neth and Payne (2002): cheap explore-and-undo helps within a problem; people do not invest early moves to learn [a27, a28].
- Fum and Del Missier (2001): strategy choice moves with instruction emphasis [b23].
- Fansher, Shah and Helie (2022): external display versus mental solving [a29, a30, b22].
- A 2016 probabilistic model with subgoal priors explains human Hanoi effects [b25].

### 2.3 From GPS to planning (1969-1997)

- **PLANNER (Hewitt 1969)**: goals created and dismissed when satisfied, recommendations about method order, protected assertions. Newell and Simon list it as a descendant of GPS. Only the summary and preface were read [a19].
- **STRIPS (Fikes and Nilsson 1971)**: "a combination of GPS and formal theorem-proving methods". The difference is built by a theorem prover: it tries to prove the goal in the current world model, and clauses left over from the failed proof become the difference. Candidate operators are those whose add list resolves with a difference clause. Search mixes forward search (apply a relevant operator when preconditions hold) and backward search (preconditions become goals) [a10]. STRIPS fixes the frame problem with precondition formula, add list and delete list. Everything not deleted stays true. It stores world models in one shared memory with marked changes. The authors propose turning a solution into a generalised macro operator as future work and say the hard part is generalising constants into parameters [a11].
- **Sussman anomaly (1975)**: in the three-block problem (C on A; A and B on the table; goal A on B on C), a non-interleaving planner fails for both goal orders, because achieving one goal as a step clobbers the other [a13, b24].
- **Korf (1985)**: MEA and subgoal methods work well when subgoals can be solved in order without undoing earlier ones (serial decomposability). Macro-operators (stored move sequences) handle interacting subgoals such as Rubik's Cube. Abstract-level notes only [a33].
- **Chapman (1987)**: TWEAK, proved correct and complete, unifies linear and nonlinear conjunctive planners. Linear planners cannot solve the Sussman anomaly; interleaving ones can. Abstract-level notes only [a34].
- **Norvig (1992)** re-implemented GPS and named its flaws: clobbered sibling goals, "leaping before you look", running around the block, lack of descriptive power, perfect-information assumption, interacting goals. His verdict: "It is not a very general problem solver at all." He quotes McDermott that GPS should have been called a "Local Feature-Guided Network Searcher" [a12, a13, a14, a15].
- **PRODIGY (Veloso et al. 1995)**: a complete nonlinear planner that "follows a means-ends analysis backward chaining search procedure". It keeps a head-plan (steps simulated forward from the start state) and a tail-plan (steps chained backward from the goal). Each step adds an operator to the tail by backward chaining or moves an applicable operator from tail to head. Control rules (select, reject, prefer) steer goal choice, operator choice, binding choice, and apply-or-subgoal [a16, c22].
- **Graphplan (Blum and Furst 1997)**: builds a layered graph of what is reachable and which actions conflict, before searching. On the flat tire problem (at least 12 time steps, 19 actions) Graphplan took 1.1 to 1.3 seconds; neither UCPOP nor Prodigy found a solution. On other problems Graphplan took 0.7, 3.4 and 2.8 seconds against about 90 seconds on average (range 30 to 2000) for compared methods [c23].

### 2.4 Competing accounts

- **Pure GPS** (goal stack, backward) versus **chunked forward subsequences** (Greeno, Thomas) [a24, a25].
- **Means-ends plus a second constraint-driven strategy** (Schmalhofer and Polson) [d02].
- **Perceptual subgoal priors, not look-ahead** (the 2016 probabilistic model) [b25].
- **Representation first**: difficulty sits in how the rules are framed before any search (Kotovsky; Clement and Richard) [b20, b21, a31].
- **Strategy by cost**: people pick a perceptual or a look-ahead strategy according to accuracy or effort instructions (Fum and Del Missier) [b23].
- **Algorithms in the machine era**: backward chaining with caching (LAMBADA), symbolic solver in control (SymBa), code-written successor function (Thought of Search), as-needed recursive decomposition (ADaPT) [c04, c06, d11, c18].

### 2.5 The LLM turn (2022-2026)

Plain LLMs plan poorly (PlanBench, 2023) [c09]. The response splits into four lines: prompt-level goal decomposition (MEDAKA, ADaPT, LAMBADA), code-held search with the model as a slot-filler (SymBa, Thought of Search, MAKER), external validators in a loop (LLM-Modulo), and critiques showing the limits (Illusion of Thinking and its rebuttals). A 2025 survey and the author's own searches found only one explicit MEA prompt paper (MEDAKA); the rest is goal decomposition or backward chaining for deduction [c25]. Explicit MEA for LLM agents is thin in the literature.

---

## 3. Core findings with exact numbers

Status key: **established** = two or more independent sources agree; **single-source**; **contested**; **human-only**; **old models** = only models from 2022-2024; **second-hand** = primary paper not opened.

### 3.1 Classical and human findings

| Finding | Numbers | Source | Status |
|---|---|---|---|
| GPS has 3 goal types, 3 methods; differences linked to operators by hand-made table | 16 goals logic trace; 33 goals trig trace with about 5 no-change attempts | a01, a02, a03, a04 | established (design); no success-rate stats exist |
| A subgoal whose difference is no easier than its parent's is rejected | 1 goal rejected in the 16-goal trace | a03 | single-source (design rule) |
| Logic Theorist proved 38 of 52 theorems; failed Theorem 2.12 without prior theorems | 73%; 10 s with memory vs fail without | a07 | single-source |
| Abstract planning in GPS can give illusory plans | 2 plans tried, 1 failed (25-goal trace); no rate | a05 | single-source |
| Formal theory behind MEA-type search is thin | 3 families of theorems named, none for MEA | a09 | established (authors concede; Norvig agrees a15) |
| Pure difference reduction clobbers sibling goals; Sussman anomaly fails for both goal orders | 2 of 2 orderings fail in the 3-block problem | a12, a13, a14, b24, a34 | established (classical) |
| Irreversible steps break plan repair | taxi variant: one ordering fails, the other fails after repair, solution exists but is never found | a14 | single-source (toy) |
| GPS is not a good model of people on river crossing | Jeffries model fit (3,2) but not (5,3) without ad hoc assumptions | a22, d01 | contested (primary papers unopened) |
| No fixed noticing order of moves | 120 students, 3 groups of 40, legal moves 27.85 / 27.88 / 27.10, all F<1, transition correlations >.95 | a20, d01 | single-source (human) |
| Best human fit mixes means-ends with a balance strategy | Exp 2, 120 students, 40 per problem; legal moves observed 16.55 / 18.90 / 28.25 vs model 17.34 / 18.54 / 27.37; transition r = .98 / .93 / .94 for (3,2), (4,3), (5,3) | d02 | single-source (human) |
| Removing model parts hurts fit | no balance: r = .94 / .76 / .78; no subgoal protection and level-2 means-ends: .74 / .84 / .84; no visited-state store: .87 / .91 / .90 | d02 | single-source (human); OCR table partly garbled |
| Cover story changes illegal moves but not legal moves to solution | four isomorphs | a23, d05 | second-hand (abstract) |
| Justifying each move against the goal reduces repeats | 10 individuals vs 10 pairs; 27 vs 17 moves; repeat moves 40.2% vs 22.4%; 13.30 vs 7.09 min | d06 | single-source (tiny) |
| Hanoi difficulty tracks steps to the first subgoal, with total length fixed | Mean score shorter vs longer first subgoal: children 7.2 vs 5.4 (t(19)=5.38, p<.001); retarded adults 5.0 vs 3.4 (t(19)=3.06, p<.01); 2 groups of 20 | b19 | single-source (special samples, 3 disks) |
| Hanoi isomorphs with the same space differ in difficulty | N=60, 15 per cell; change-of-state versions need about half the moves (F(1,56)=7.48, p=.008); transformation versions take twice the time (F(1,56)=12.097, p=.001) | b20, b21 | single-source; rival load account (Kotovsky and Fallside) |
| External display raises completion; mental solving gives shorter solutions | Exp 1 final n=129: 4-disk completion 100% vs 91% (chi2=4.45, p=.03); 5-disk 93% vs 63% (p=.001); Exp 2 Prolific n=572: 5-disk 87.37% vs 55.25% | a29, a30, b22 | single-source (one group); self-report strategy measure |
| Explore-and-undo helps within a problem; people do not invest early moves | N=44; Group 3 vs Group 1 counted moves p=.008; late-use interaction F(1,20)=5.4, p=.03 | a27, a28 | single-source |
| Strategy choice moves with instructions | N=34, 8 trials; errors F(1,29)=6.57, time F(1,29)=7.83; perceptual strategy in 99% CI on 100% of trials (accuracy group), look-ahead 87.5% (effort group) | b23, b25 | single-source; small N |

### 3.2 Planning systems

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Learned control rules for Prodigy help modestly | 400 training problems, 17 rules, 500 test problems; unsolved 218 to 135 (about 38% fewer); nodes 17,204 to 14,306 (about 17%); solution length 3,132 to 2,930; time down "not significantly" | a17 | single-source (own system) |
| Explanation-based learning from linear planning did not carry to nonlinear planning | no numbers | a18 | single-source |
| Graphplan beats Prodigy and UCPOP on 1990s STRIPS problems | flat tire 1.1-1.3 s vs no solution; other problems 0.7, 3.4, 2.8 s vs about 90 s average | c23 | single-source (outside comparison, old machines) |

### 3.3 Language models

| Finding | Numbers | Source | Status |
|---|---|---|---|
| MEDAKA (recursive goal decomposition plus state tracking) beats CoT on a continuous-state planning test | Pass@1 CoT to MEDAKA: Claude Sonnet 4.6 77.8 to 94.5; Gemini 3 Flash 65.6 to 82.0; GPT-5.4 74.3 to 78.5 (tie with AoT+); GPT-4o 25.7 to 36.9; Llama 3.3 70B 26.6 to 40.6; Gemma4 4B 55.7 to 61.0; Gemma4 2B 26.3 to 30.5. 189 problems, 3 rollouts, thinking off, temperature 0 | b01, c01 | single-source (one preprint, one domain) |
| Cost is 1.8 to 3.8 times CoT tokens; MEDAKA pass@1 beats CoT pass@3 on 4 of 7 models | Claude pass@3 86.8 vs 94.5; Gemini 67.2 vs 82.0. Per-model median ratio about 2.0 (Gemini), 2.4 (GPT-4o), 3.1 (Claude), 3.8 (GPT-5.4) | b03, critique | single-source; oracle best-of-3 is not equal tokens |
| Gains concentrate in structural difficulty; weak models gain nothing on nonlinear problems | Nonlinear CoT / AoT+ / MEDAKA: Claude 33.3 / 55.3 / 87.4; Gemini 16.4 / 21.4 / 50.9; GPT-5.4 28.9 / 49.1 / 46.5; Gemma4 4B 14.5 to 12.6; Gemma4 2B 10.1 to 11.9; Llama 15.1 to 15.1. Multi-goal Claude 50.4 to 89.5. Distractors Claude 73.8 to 94.0; GPT-4o 10.7 to 42.9 | b02 | single-source |
| Each MEDAKA module alone recovers most of the gain | Claude (CoT 77.8, full 94.5): decomposition only 90.5 (76% of gain), tracking plus calculation only 91.0 (79%). Gemini (CoT 65.6, full 82.0): 76.0 (63%) and 75.1 (58%). Nonlinear Gemini full / no state / no recursive: 50.9 / 36.5 / 28.9 | b04 (corrected), c02, d22 | single-source |
| Search-style AoT+ can be worse than CoT | GPT-4o 19.8 vs 25.7; Llama 3.3 70B 17.6 vs 26.6 | b02, c01 | single-source |
| Backward chaining with caching beats CoT and forward SI on deep proofs | PaLM 540B; Depth-5 relative gain +44% (PUD) and +56% vs SI; PrOntoQA +37% vs CoT, +113% vs SI; ParaRules +43%. Calls 3.8x fewer at depth 1, 11.8x fewer at depth 5. Fact Check accuracy 0.94 with one fact | b11, c04 | single-source |
| Label accuracy overstates reasoning | CoT chains correct only 28% at depth 5 (ProofWriter); hallucination 48% of errors | b12, c05 | single-source |
| Backward CoT alone is not clearly better than forward CoT; forward SI wastes inference | SI with 5 inferred facts: 29% all unique, 7% all identical, 10% only two unique | b13, c05 | single-source |
| GPT-4o plans worse backward than forward | Forward vs backward: undirected graph 82.5 vs 76.7; directed 38.5 vs 29.7; array 67.5 vs 62.2; Blocksworld 39.5 vs 20.5 | c03, d18 | single-source (older domain set) |
| Flipping the problem plus self-verification lifts planning 4 to 24 points | 200 trials, 6 attempts; Fwd-Flip vs Fwd: undirected 93.5 vs 82.5; directed 86.5 vs 69.5; Blocksworld 48.5 vs 39.5; array 56.0 vs 50.0. Model picks the easier direction 78.5% (undirected) and 60.5% (directed) | c03, d18 | single-source; at 1 attempt Fwd-Flip is slightly worse on Blocksworld |
| SymBa: solver in control beats model-run backward chainers | Average accuracy 79.8 (SymBa) vs 71.5 (least-to-most) vs 69.7 (LAMBADA); no backtracking 76.3; token use several times higher than LAMBADA | c06 | single-source |
| As-needed decomposition (ADaPT) beats ReAct, plan-then-execute, Reflexion | GPT-3.5: ALFWorld 71.6 vs 43.3 / 43.3 / 57.5 (Try Again 47.8); WebShop 44.0 vs 32.0 / 17.0 / 35.0 (LATS 38.0); TextCraft 52.0 vs 19.0 / 27.0 / 32.0. TextCraft depth 2: 26.9 vs 78.2; depth 3: 1.8 vs 38.7 | c18, d12 | single-source; old models |
| Depth cap helps in steps; blanket decomposition can hurt | Gain rises from dmax 1 to 2 to 3, biggest step 1 to 2. WebShop: plain executor 29.0, static decomposition 17.0, ADaPT 44.0. Depth used on TextCraft 1.9 (depth-2 recipes), 2.8 (depth-3) | d12 | single-source; old models |
| Subgoal milestones plus a checker raise web-task success | WebArena-Lite, 165 tasks: Gemini-2.5-pro 23.0 to 32.1. Checker AUROC 0.84, exact-equivalence F1 0.68 (precision 0.79, recall 0.60). Stuck-midway failures 48.41% to 39.87%; wrong terminations 9.52% to 12.03% | c19 | single-source |
| Procedure-in-prompt helps only when it matches the class and fades with size | 261 Blocksworld table-to-stack instances; zero-shot GPT-4 3.83%, stacking-specific 59.3%, universal algorithm 51.3%, progression proof 6.89%; GPT-4-Turbo 19.1 / 40.6 / 37.1; Claude-3-Opus 9.96 / 24.5 / 37.1; self-consistency lowered accuracy | b14, b15, c07, c08 | single-source (PDF not re-opened) |
| GPT-4-class models solve about a third of Blocksworld and collapse on obfuscated names | PlanBench, 600 instances: GPT-4 206 (34.3%) plan generation; Mystery deceptive 26 (4.3%); randomized 12 (2%). o1-preview: Blocksworld 587/600 (97.8%), Mystery 317/600 (52.8%), randomized Mystery 224/600 (37.3%), 20-40 step plans 23.63%; o1-mini 340/600 (56.6%) | c09, c11 | established (two independent evaluations) |
| An outside verifier with back-prompting lifts LLM plans where proposals are plausible | VAL: Blocksworld 82% in 15 rounds, Logistics 70%, Mystery about 10%; autonomous GPT-4 about 12% valid | c10, b16 | single-source (numbers re-quoted from other papers) |
| Restating state (memoization) cuts state hallucination; random trajectories in examples work as well as human-chosen | Game of 24: 70.0 (random) vs 71.0 (human); crossword 54.0 vs 52.0; tokens GPT-4 Blocksworld AoT+ 2,067.8, LLM-Modulo 6,452.9, CoT 650.7 | b16, b17, b18, b05, c02 | established |
| Code-held transitions and goal test solve puzzles with a clear goal | GPT-4 wrote successor and goal test once; plain BFS or DFS solved 1,362 24-game, 502 Blocksworld (4-5 blocks), 4,000 PrOntoQA, 20 mini crosswords; LLM-in-search baseline would cost over $1,000 | d11 | single-source |
| LLM as verifier is poor | GPT-4 verifier false-negative: Game of 24 20.7%, graph colouring 95.8%, Mystery Blocksworld 97.09%. Self-critique 5% to 3% (24), 16% to 2% (colouring), 4% to 0% (Mystery); sound verifier 36%, 38%, 10%. Self-correction GPT-3.5 CommonSenseQA 75.8 to 38.1. Travel verifier 0.455 / 0.489 (near chance). GPT-3.5 accepted every Blocksworld plan | d15, d16, d18, c20 | established |
| Fine-tuned detector found wrong steps but validity did not improve | precision 90.5%, recall 99.2% | d17 | single-source |
| Goal-distance counting hurt out of distribution; stating exact state helped | Fine-tuned Qwen2-7B; Goal CoT only strategy that hurt; State CoT 100% executability on the unseen set but not on longer plans | d17 | single-source (fine-tuned small model) |
| Irrelevant hints are worse than none; invalid but relevant ordered hints keep 80-90% of the gain | text-davinci-002, GSM8K (800): standard 15.4, CoT 48.5, invalid 39.5, no coherence 23.1, no relevance 11.0; Bamboogle (125) F1 20.6 / 45.2 / 39.4 / 23.9 (no relevance) | d14 | single-source; old model |
| Plain "think step by step" adds little for reasoning models | GPQA Diamond 198 questions x 25 trials; Gemini Flash 2.5 minus 13.1 at 100% metric, o4-mini plus 5.6 at 51% metric (p=.003); CoT 20-80% slower | d13 | single-source; not planning |
| Experience memory helps near, weakens far | ExpeL HotpotQA to FEVER: Act 58, ReAct 63, transfer 65 (no target demos), 70 (with). AWM WebArena relative gain 51.1% (12.0 points); cross-website online 8.9-14.0 points above baseline, offline loses edge as the gap grows | d20, d21 | single-source each |

### 3.4 Hanoi collapse dispute (see 5.4)

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Reasoning models collapse on Hanoi; algorithm in the prompt does not move the point | Near perfect at N=5 (31 moves), near zero at N>=8; first error about move 40 of 255 at N=8, about move 100 at N=10; Hanoi N=12 failed under 50 moves while N=10 succeeded past 100; River Crossing N=3 (11 moves) collapses | a35, b09, d07 | contested |
| Output-length and format artifact | 10 tokens per move gives N about 12-13 at 64k; Lua-function prompt solved 15 disks in under 5,000 tokens (Claude 3.7 Sonnet, Claude Opus 4, o3, Gemini 2.5); River Crossing capacity 3 unsolvable for N>5 | b06, b07, c13 | contested (short, unpowered note) |
| Cumulative error alone predicts a cliff | N=13 needs 8,191 moves; per-move success 0.9999 gives under 45% perfect-run chance | c14 | single-source |
| Stepwise prompting and move-by-move environments still fail from about N=8 | Hanoi N=3 to 10, 10 trials; two-model dialogue worse (from N=4); environment holds state, about 40% deterministic reuse at n=8; up to n=8, 30,000 token budget, one run | c16, d08, d09 | contested |
| Single-step calls with voting solve 20 disks | 1,048,575 steps, zero errors; gpt-4.1-mini, algorithm and state in every prompt, k=3, outputs over 750 tokens discarded; single-step error 0.0045 (10K random steps, read from d10), 0.22% at temperature 0.1 in the cost analysis (c17); o3-mini 0.0017; nano 0.3583; two independent runs shared no wrong step; one step needed 18 voting rounds | c17, b26, d10 | single-source |

---

## 4. Mechanisms and models

Each block is written so an engineer can code it. In every block the program holds the control state. The model fills one named slot.

### 4.1 The GPS loop [a01, a02, a03, a06]

```
solve(state, goal, depth):
    if depth > D_MAX: return FAIL
    diff = compare(state, goal)              # code, or model fills "name the difference"
    if diff is empty: return SUCCESS
    for d in rank_by_difficulty(diff):       # table or model-proposed ranking
        for op in relevant_ops(d):           # the difference-operator table
            if not worth_trying(op, d): continue
            # reject a subgoal that is not easier than an ancestor (a03)
            pre = unmet_preconditions(op, state)
            ok = True
            for p in pre:
                sub = solve(state, p, depth+1)   # push as subgoal
                if sub fails: ok = False; break
                state = sub.state
            if ok:
                state = apply(op, state)         # code applies, code updates ledger
                return solve(state, goal, depth+1)
    return FAIL
```

Key rules:
- **Difference ranking** is the progress criterion. More important differences are matched first [a02].
- **Loop check**: reject a subgoal whose difference is not easier than its parent's [a03]. In code: a depth cap, plus a visited-state set, plus "difference size must shrink or the move needs a stated reason".
- **Worth-trying check**: GPS checks a goal for being worth the effort and likely to succeed before acting [a01]. This is the origin of a budget gate.
- **Wasted goals are a cost signal**: the trig trace had about 5 no-change attempts in 33 goals [a04]. Count them.
- **Search order**: modified depth-first, guided by differences [a08].

### 4.2 STRIPS operators and the head/tail plan [a10, a11, a16]

Operator = (preconditions, add list, delete list). Everything not deleted stays true. This is a cheap ledger: apply an effect by set arithmetic, not by asking the model "what is the state now".

- STRIPS: the difference is what is left unproved when you try to prove the goal in the current state. Operators whose add list covers the leftover are candidates.
- PRODIGY head/tail: head-plan = operators already applied in a forward simulation from the real start state. Tail-plan = operators chained backward from the goal. Each iteration either adds a relevant operator to the tail, or moves an applicable one to the head. The real state is always known (end of head) and the open goals are known (start of tail).
- PRODIGY's three decision points are exposed to control rules: which goal, which operator, which binding. Each can be a code-run choice point where the model proposes and a check selects [c22].

### 4.3 Protecting conjunctive goals [a12, a13, a14]

- After the plan, re-check that all goals hold together (`achieve-all`). A plan that solves goals one by one can end with an earlier goal broken, and a naive solver reports "solved".
- Keep a list of protected goals that no operator may delete.
- Plan on a copy of the state, not on the real one ("leaping before you look" runs every action before returning failure).
- Mark irreversible steps (spent money, a used resource). Repair by undo only works when steps are reversible.
- For subgoal interference, interleave; for interacting subgoals, store macro operators [a33, a34 as pointers].
- A cheap compatibility prune before any model call: drop a subgoal pair that is mutually exclusive (Graphplan idea) [c23].

### 4.4 The Schmalhofer and Polson human model as a move generator set [d02, a21]

Move generation, evaluation and execution are separate.

- Generator A: means-ends (move toward the goal).
- Generator B: balance (satisfy the constraint, even if it moves away from the goal).
- A probability chooses which generator fires each step.
- Evaluation filters: avoid the backward move (do not undo the last move), avoid the start state, a visited-state memory, a level-2 means-ends check, subgoal protection.
- Working memory: previous move and at most 3 proposed moves.

An engineer's reading: keep two proposers (difference-reducing and constraint-keeping), pass every proposal through the same filter list in code.

### 4.5 MEDAKA prompt loop [b01, b02, c01, c02, d22]

Per step: derive the goal, find the blocker, if blocked derive a subgoal that resolves the blocker, push deferred subgoals on a stack, solve, pop, track the exact state after every step. Two bundles are separable in the ablation:
- "Recursive module": goal decomposition and the stack.
- "State tracking": per-step tracking **plus** the numeric computation instructions (an algebra-aware CoT). A pure ledger arm and a pure stack arm do not exist. No arm isolates difference naming.

Failure modes of search-style prompts that MEDAKA targets: guess-and-patch of continuous values, state drift, and locally correct but globally inconsistent arithmetic (example: volume 2 L reached but composition (20,25,55)% instead of (13.43,30.52,56.05)%; a vessel emptied and then reused) [b05].

### 4.6 LAMBADA backward chaining [c04, c05]

Four few-shot modules: fact check, rule selection, goal decomposition, sign agreement. Code (the outer loop) holds the goal tree and a cache of results. Backward search keeps the branching small because only rules whose conclusion matches the goal are tried. The modular loop, not direction alone, carries the gain: backward CoT as a single prompt is not clearly better than forward CoT [c05]. SymBa shows that LAMBADA is an incomplete backward chainer (no backtracking, no binding propagation). Putting an SLD solver in control and calling the model only for missing facts did better [c06].

### 4.7 ADaPT as-needed decomposition [c18, d12]

```
adapt(task, depth):
    result = executor(task)             # try to do it directly
    if success(result): return result   # success judged by executor or env
    if depth >= D_MAX: return result
    plan = planner(task)                # split into subtasks joined by AND / OR
    return combine(adapt(sub, depth+1) for sub in plan)
```

D_MAX 3 (4 on TextCraft). The weak spot: success is judged by the executor. On WebShop it overestimates success by over 30 points, so decomposition stops early [c18].

### 4.8 Code-held search, model as slot [d11, c06, c17]

- Thought of Search: the model writes `successors(state)` and `is_goal(state)` once. Plain BFS/DFS runs in code. Works when the goal test is explicit.
- MAKER: one step per call, state and algorithm in the prompt, vote until one answer leads by k=3, discard replies over 750 tokens (error rises sharply past about 700 tokens), cost grows as steps times log steps [c17, d10].

### 4.9 Loop and reset guard [d08, c16, d19, d06]

Models run in step-by-step loops that reuse continuations (about 40% at n=8 in the Hanoi environment study; pick-up and put-down cycles in ReAct-style agents). A guard: keep a visited-state set, refuse a repeated state, force a different choice, and allow a reset to the start state as a sanctioned non-greedy move. Repeating the goal in every step is cheap and helped (one-shot prompt that fixed the action description and repeated the goal beat ReAct by 12.3 and 14.8 points) [d19].

### 4.10 Candidate rule for non-greedy moves (hypothesis, not tested on any LLM) [K30]

Allow a move that does not reduce the named difference only when:
(a) a loop is detected (state already visited),
(b) the greedy move would break a stated constraint, or
(c) no operator reduces the difference.
A reset to the start is a sanctioned non-greedy move. Built from d02, d06, d08, d19. The human primary papers (Thomas, Greeno, Jeffries) behind the "detour" idea were never opened.

---

## 5. What holds up

### 5.1 Replicated or multi-source

- **Pure difference reduction fails on interacting goals.** Sussman anomaly, clobbered sibling goal, taxi case. Three sources agree on the classical side [a12, a13, a14, a34, b24]. Fixes known: goal protection, final all-goals check, interleaving. Not measured on LLMs (K34).
- **Combinatorial blow-up and thin theory.** Newell and Simon concede it [a09]; Norvig says GPS "is not a very general problem solver at all" [a15]; Graphplan beats means-ends planners on 1990s benchmarks [c23].
- **Plain LLMs do not plan well; obfuscation exposes pattern matching.** PlanBench and the o1 follow-up agree: GPT-4 206/600; Mystery 4.3% and 2%; o1-preview 97.8% plain, 52.8% Mystery, 23.63% on 20-40 step plans [c09, c11].
- **An LLM is a poor checker of its own work.** Four lines agree: verifier false-negative rates of 20.7%, 95.8%, 97.1% [d15]; self-correction dropped GPT-3.5 on CommonSenseQA from 75.8 to 38.1 [d16]; accept-all behaviour in GPT-3.5 [d18]; verifier at chance on travel planning [c20]. The accuracy a checker needs before subgoal checks help has not been measured.
- **State restatement cuts drift.** AoT+ memoization, MEDAKA's tracking arm, and the classical frame-problem fix all point the same way [b16, b18, c02, a11].
- **Representation changes difficulty.** Hanoi isomorph results from two independent labs [b19, b20, b21] (human only).

### 5.2 Interventions that worked

- Code holds state; model takes a small step (MAKER, Thought of Search) [d10, d11].
- Goal decomposition with a stack and exact state tracking, for strong models on structurally hard items (MEDAKA) [b02].
- Backward chaining with caching in a code loop (LAMBADA) [c04].
- Decompose only after a failed attempt, depth cap near 3 (ADaPT) [d12].
- Solver in control, model only supplies missing facts (SymBa) [c06].
- External sound verifier with back-prompting where proposals are plausible [c10].
- Flip the problem and combine forward and flipped samples with verification (4 to 24 points) [d18].
- Forced justify-the-move-against-the-goal and a monitor role (humans: repeats 40.2% to 22.4%) [d06].
- A reset to the start when stuck [d19, d06].

### 5.3 Interventions that did not work, or hurt

- Giving the exact Hanoi algorithm in the prompt did not move the collapse point in the Apple study [a35, b09, d07].
- A move-by-move interface with feedback made collapse start earlier and produced loops [c16, d08].
- A two-model dialogue with shared memory did worse (trouble from N=4) and kept spending tokens in unproductive cycles [d09].
- Worked-example procedures in the prompt (Blocksworld): gain only when closely matched; fades as stacks grow past the example size; self-consistency lowered accuracy [c07, b15].
- Search-style AoT+ was worse than CoT on GPT-4o (19.8 vs 25.7) and Llama 3.3 70B (17.6 vs 26.6) [b02].
- Always-decompose (static) on WebShop: 17.0 vs 29.0 plain executor [d12].
- Counting distance to goal (Goal CoT, fine-tuned 7B) hurt out of distribution [d17].
- Backward planning in the model: worse than forward on all four domains tested with GPT-4o [c03].
- A one-line step-by-step prompt did little for reasoning models (Gemini Flash 2.5 minus 13.1 points at the 100%-correct metric) [d13].
- Model self-critique without a sound outside signal (GPT-4 self-critique 5% to 3%, 16% to 2%, 4% to 0%) [d15].
- Explanation-based learning from linear planning did not transfer to nonlinear planning [a18].
- Learned control rules gave only modest gains and matching cost ate the time saving [a17].

### 5.4 The Hanoi collapse dispute

| Position | Evidence | Weak point |
|---|---|---|
| Real reasoning/execution failure | Algorithm in prompt does not help; first error at move ~40 of 255 at N=8, so not an end-of-output problem [d07] | Apple authors' own reply; many claims only in figures |
| Output-length and format artifact | 10 tokens per move allows N about 12-13 at 64k; code answer works at 15 disks; River Crossing set had impossible cases [b06, b07, c13] | Short, unpowered, partly LLM-written, an earlier token error corrected; does not show the full move list can be executed; capacity statement (3) may not match the original (4) [b07] |
| Cumulative error / agentic gap | per-move 0.9999 over 8,191 moves gives under 45% perfect runs; with tools, bigger River Crossing instances solved; GPT-4o ran a wrong plan unnoticed, o4-mini verified and revised [c14] | Few runs, no sample sizes |
| Still a real limit near 8 disks | stepwise p-move prompting fails from N=8; River Crossing solved when only solvable instances are used, even N=100 with k=4 [d09] | Preprint, 10 trials, model not named |
| Environment-held state does not fix it | collapse starts earlier, 40% deterministic reuse at n=8 [d08, c16] | Single runs, up to 8 disks, no algorithm given, two model families |
| Short steps + algorithm + voting fix it | 20 disks, 1,048,575 steps, zero errors [d10] | Algorithm supplied, voting cost dominates, execution only |

Tidy reading (K21-K23): long runs are lost to step errors and loops. Short steps, the known algorithm, voting and an over-length red flag fix execution. Whether the model can find the strategy is a different question the dispute has not settled. The River Crossing part is mostly an invalid-instance artifact; the Hanoi part is partly real.

### 5.5 Moderators and boundary conditions

- **Model strength.** MEDAKA gains vanish for small models on hard structure (Gemma4 4B/2B, Llama nonlinear) [b02]. ADaPT with Llama-2-70B executor alone 20.4, with a GPT-3.5 planner 43.3 [c18]. The scaffold unlocks latent skill, it does not create skill.
- **Strong models can tie.** GPT-5.4: 74.3 to 78.5, tied with AoT+, and below AoT+ on nonlinear (46.5 vs 49.1) [b01, b02].
- **Problem depth.** LAMBADA gains grow with proof depth; ADaPT gains grow with recipe depth [b11, c18].
- **Task type.** Deduction over rules (LAMBADA) is not state-changing planning (c03); backward helps the first and not the second. This is the main reason the two results do not contradict each other [critique].
- **Problem-graph shape.** The Jeffries model fit (3,2) and failed (5,3) [a22].
- **Presentation.** External display raises completion; mental work gives shorter solutions [b22].
- **Instruction and cost.** Accuracy emphasis versus effort emphasis changes strategy [b23].
- **Solvability.** Benchmarks with unsolvable items score solver failures as reasoning failures [b07, d09].

### 5.6 Source quality warnings

- Almost all positive explicit-MEA LLM evidence is one preprint (MEDAKA, dated 18 Oct 2026, no replication) on one synthetic domain with thinking off [critique].
- Independent source counts are inflated if one group appears twice: a29, a30, b22 are the same Fansher data; b14, c07, c08 are one Stechly paper; b01-b04, c01, c02 are one MEDAKA paper.
- STRIPS and PRODIGY evidence comes from the systems' authors. Only Graphplan is an outside comparison, and on 1990s machines.
- The primary human papers (Thomas, Greeno, Jeffries, Simon and Reed, Newell and Simon 1972, Anzai and Simon) were never opened.
- The Shojaee numbers in b09 came through a fetch summary; the later d07 reading of the authors' HTML is better.
- One correction made in the critique: b04 swapped the Gemini ablation columns. Correct values: Gemini minus State 76.0 (-6.0), minus Recursive 75.1 (-6.9). Do not reuse the b04 order.

---

## 6. Language models

### 6.1 Baseline behaviour

- GPT-4 (early 2023) solved 206/600 (34.3%) Blocksworld plan-generation instances. Obfuscated predicate names dropped it to 26/600 (4.3%) deceptive and 12/600 (2%) randomized [c09]. Instruct-GPT3: 41/600 (6.8%) [c09]; Instruct-GPT valid on 5% of 500 Blocksworld [c21].
- Autonomous GPT-4 produced about 12% valid plans on average [c10].
- o1-preview: 587/600 (97.8%) on plain Blocksworld, 317/600 (52.8%) on Mystery, 224/600 (37.3%) on randomized Mystery, 23.63% on larger problems (110 instances, 6-20 blocks, 20-40 steps). o1-mini 340/600 (56.6%). Best non-reasoning model on Blocksworld: 62.6% (Llama 3.1 405B); none above 5% on Mystery. Unsolvable instances flagged correctly 27% of the time. Cost per 100 instances for o1-preview: $42.12; time 40 to 111 s against 0.265 s for Fast Downward, which scores 100% [c11].
- Fine-tuned small code models beat few-shot large ones in-domain, and few-shot models fall with problem size [c21]. We are not taking the fine-tune route.
- In deduction, CoT often reaches the right label with a wrong proof: correct chains only 28% at depth 5 [b12].
- LLMs plan better forward than backward (GPT-4o): Blocksworld 39.5 vs 20.5 [c03]. When free to choose a direction, the model picks the easier one only 60.5% to 78.5% of the time [d18].

### 6.2 What changed behaviour, and by how much

| Change | Effect | Source | Caveat |
|---|---|---|---|
| Recursive decomposition plus state tracking in the prompt | +16.7 points Claude Sonnet 4.6 (77.8 to 94.5), +16.4 Gemini 3 Flash, +4.2 GPT-5.4, +11.2 GPT-4o, +14.0 Llama 70B, +5.3 Gemma4 4B, +4.2 Gemma4 2B | b01, c01 | thinking off; 1.8-3.8x tokens; one domain |
| Same, on nonlinear items only | Claude 33.3 to 87.4; Gemini 16.4 to 50.9; GPT-5.4 28.9 to 46.5 (AoT+ 49.1 better) | b02 | small models flat |
| Either module alone | 58% to 79% of the full gain | d22 | bundles confound |
| Backward chaining loop with caching | +37% to +113% relative at depth 5; calls 3.8x to 11.8x fewer | c04 | PaLM, deduction |
| Solver in control (SymBa) | 79.8 vs 69.7 (LAMBADA) average | c06 | several times more tokens than LAMBADA |
| As-needed decomposition | ALFWorld 71.6 vs 43.3; TextCraft 52.0 vs 19.0 | c18 | GPT-3.5 |
| Flip the problem, combine forward and flipped, verify | +4 to +24 points | d18 | needs several attempts; self-verification |
| Subgoal milestones with a checker | Gemini-2.5-pro 23.0 to 32.1 on WebArena-Lite | c19 | checker F1 0.68 |
| Sound external verifier with back-prompting | Blocksworld 82% in 15 rounds | c10 | bounded by proposal quality |
| Code-written transitions and goal test | 100% on 1,362 + 502 + 4,000 items | d11 | clear goal test only |
| Single-step calls, k=3 voting, over-length red flag | 20 disks, 0 errors in 1,048,575 steps | d10 | execution only |
| Restating state (memoization) | lower state error; cheaper than LLM-Modulo (2,067.8 vs 6,452.9 tokens on Blocksworld) | b16, b18 | figure-only for error |
| Repeating the goal each step in a one-shot prompt | beat ReAct by 12.3 and 14.8 points | d19 | older GPT models |
| Wrong or irrelevant hints | irrelevant content below no-CoT (GSM8K 11.0 vs 15.4); invalid but relevant keeps about 80% of the gain | d14 | 2022 model |

### 6.3 Where it breaks

- **Long execution.** Collapse past about 8 disks for reasoning models in several setups; loops and deterministic reuse of earlier continuations [d07, d08, d09].
- **Self-judgement.** The model accepts wrong plans or rejects right ones [d15, d18].
- **Coupled constraints.** Greedy one-component-at-a-time reduction breaks when components interact [b05].
- **Distant transfer.** A procedure in the prompt copies the example pattern and fails on bigger stacks [c07].
- **Goal-distance estimation.** Adds a task and locks the plan length (d17).
- **Native reasoners.** Prompt-level step structure adds little once a model reasons natively [d13]. No study tests a means-ends scaffold with thinking on (gap 1, still open).

### 6.4 What is not known

- Effect with thinking on, at equal tokens, against CoT pass@k plus a verifier. MEDAKA turned thinking off and excluded external verifiers on purpose, and gave the scaffold 1.8-3.8x tokens [d22].
- Effect outside continuous-state mixing: ARC grids, code repair, open questions. No study found [K33].
- Which part carries the gain, down to difference naming. Nothing isolates it.
- How often goal clobbering shows up in LLM outputs. No direct study [K34].

---

## 7. What our agent should take

Status marks as in SCHEMA.md: [E] established, [S] single source, [C] contested. "Schema part" says where it goes.

### Add now (established)

| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| A1 | **Code-held state ledger.** Code computes the state after each step (apply effects as add/delete lists) and restates it into the next prompt. The model never reports "the current state". Cuts state hallucination and drift. | S4/S5/S6 (all operator steps); memory/ledger | [E] | b16, b17, b18, b05, c02, a11, a12; claim K26 |
| A2 | **Final all-goals check.** Before S8 passes, code re-checks that every goal still holds at the same time. Applies to any item with two or more conjunctive conditions. Classical case is solid; the LLM clobbering rate is unmeasured, so this is a cheap guard, not a measured gain. | S8 VERIFY, G3 | [E] (classical) | a12, a13, a14, a34, b24; K03, K34 |
| A3 | **Code runs the loop; the model fills one slot.** Do not ask the model to emit long move lists or to carry the goal stack across hundreds of steps. Code holds the stack and emits long sequences; the model proposes one step. Both sides of the Hanoi dispute accept that long model-run execution errs; they differ on why. | schema section 1; S6 | [E] for the design principle; [C] for the cause of the collapse | b06, c13, c14, d07, d08, d09, d10, b09; K21, K22 |
| A4 | **Do not use the model as its own progress or subgoal checker.** Recompute subgoal status from the ledger or a code check. If any model-judged check is used, log false progress accepted. | G2, G3, G5; S5, S8 | [E] | d15, d16, d17, d18, c19, c20; K31 |
| A5 | **Visited-state guard and depth cap.** Code keeps a set of visited states, refuses a repeated state, caps depth, and rejects a subgoal that is not easier than its parent. This is a guard only, not the detour rule. | S6; tree rules | [E] | a03 (design), d02 (human model needs it), d08, c16, d19 (LLM loops) |
| A6 | **Obfuscated and solvability-checked variants in every means-ends test.** A gain that disappears on renamed predicates is pattern matching. Check solvability of each item with a code solver before scoring. | G3; bench hygiene | [E] | c09, c11, b07, d09, c14; K24 |
| A7 | **Score the chain, not only the label** on deduction-style items where a trace exists. | G3 | [S] (single paper) | b12, c05; K16. Listed here as a bench rule, not a schema change; confirm before it enters SCHEMA.md |
| A8 | **Reframe before searching, but only on an impasse signal.** Human difficulty sits in the representation (Hanoi isomorphs). Supports the existing S1/S2 and O6. No new element. | S1, S2, O6 (support) | [E] (human only) | b19, b20, b21, a31 (pointer); K08. Not tested on LLMs |

### Test first

| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| T1 | **Explicit MEA scaffold (goal naming, stack, ledger) against CoT pass@k plus verifier, thinking on and off, at equal tokens.** This is the main open question. | S6, O3, O5 | [S] | b01-b04, c01, c02, d22, d13; K12 |
| T2 | **Which part carries the gain**: ledger only, calculation hints only, stack only, difference naming only, full. | S6 | [S] | b04, c02, d22, d17; K13 |
| T3 | **Decompose only after a failed attempt, depth cap 3**, versus always-decompose and none, with a current model and a code failure signal. | O3, S6 | [S] | c18, d12; K18 |
| T4 | **Non-greedy move rule**: allow only on loop, constraint conflict, or no reducing operator; allow reset. | S6 / detour | hypothesis | d02, d06, d08, d19; K07, K30 |
| T5 | **Direction chosen by code**: forward default, flipped as a second attempt, backward only inside a modular code loop. | O5 | [S] | c03, d18, b13, c05; K15, K17 |
| T6 | **Wrong-hint tolerance**: inject wrong, vague and irrelevant differences into the difference/operator hint. | S6 operator table | [S] (indirect) | d14, a02; K02 |
| T7 | **Code-held search for items with an explicit goal test** (model writes `successors` and `is_goal` once). Closed for items without a goal state. | O-execute | [S] | d11; K29 |
| T8 | **Compatibility prune** (drop subgoal pairs that cannot co-hold) before model calls. | O3 | [S] | c23; K05 |
| T9 | **Class-tagged control-hint memory**, retired on class change. | memory | [S] | a17, a18, d20, d21; K06, K32 |
| T10 | **Capability gate with fallback to plain CoT** when the scaffold shows no gain on a class. | S0, G7 | [S] | b02, b01, K14 |
| T11 | **Do not use model-estimated distance to goal**; use code-computed counts or none. | S6 | [S] | d17 |
| T12 | **Macro operators for interacting subgoals** (store solved multi-step sequences). | memory/subgoal library | [S] (pointers only) | a33, a11 |
| T13 | **Plan abstraction false-plan rate**: how often a solved abstract plan fails at the detailed level. | O-abstract | [S] | a05; K27 |
| T14 | **Single-step voting with over-length red flag** (discard replies above a length threshold). | S3/S4 | [S] | c17, d10; K23. Note G4: voting on one model is not an independent check, so test only the discard rule |

What not to add from this subfield (consistent with section 4b of SCHEMA.md): a model-run goal stack with no code behind it; a procedure shown in the prompt as the only mechanism; a model-judged "subgoal done" check; backward chaining as the single route; always-decompose.

---

## 8. Concrete tests on our bench

All arms run at equal total tokens (setup cost counted, G7). Log per run: mode, path, tokens per state, transitions, doubt steps, operators tried.

| # | Item type | Arms (equal tokens) | Metric | Expected effect |
|---|---|---|---|---|
| B1 (T1) | Synthetic multi-step planning items with a code verifier (Blocksworld 4-8 blocks, plus an obfuscated copy), and 20 ARC items | (1) CoT pass@k plus verifier; (2) MEA scaffold, code-held ledger and stack, one sample; (3) MEA scaffold with thinking on; (4) plain model with thinking on. k chosen so each arm spends the same tokens | Exact-match solve rate; tokens per solve; solve rate on the obfuscated copy | Scaffold beats arm 1 on hard structural items by several points; shrinks or vanishes with thinking on (d13 predicts small gain or harm). If arm 2 < arm 1 at equal tokens, drop it |
| B2 (T2) | Same items as B1 | Ledger only (code); calculation hints only; stack only; difference naming only; full; CoT | Share of the full gain recovered per arm | Ledger and stack each recover over half of the gain (MEDAKA: 58-79%); difference naming alone near zero or negative |
| B3 (T3) | Multi-step items where a first direct attempt can fail (code-detectable) | Always-decompose; decompose-on-failure with D_MAX 3; no decomposition | Solve rate; tokens; depth used | As-needed beats always-decompose (as WebShop 44.0 vs 17.0) and costs fewer tokens; cap 3 enough |
| B4 (T4) | River-crossing / hobbits-orcs style items, sizes (3,2), (4,3), (5,3), plus Blocksworld | Pure difference reduction; three-trigger rule (loop, constraint conflict, no reducing operator, reset allowed); unrestricted moves | Solved items; loops (repeated states); moves to solution | Three-trigger rule solves items pure reduction cannot (those needing a move away from the goal), with fewer loops than unrestricted |
| B5 (T5) | Blocksworld and deduction items | Forward; backward; flipped plus forward (selected by code check); modular backward loop with cache | Solve rate; direction chosen by model vs code | Forward beats naive backward; flipped plus forward gains 4+ points with several attempts; modular loop wins on deduction only |
| B6 (A2, K34) | Multi-goal items (3 or more conjunctive conditions) | With vs without a code-run final all-goals check (and with a protected-goal list) | Rate of final answers where an earlier-satisfied goal is false; solve rate | Clobbering is present at a measurable rate; the check removes most of it for few tokens. If clobbering is under 2%, keep the check anyway only if cost is under 2% of tokens |
| B7 (A4, K31) | Items with subgoals | Model-judged subgoal check; ledger-recomputed check; plain resampling | False progress accepted; solve rate | Ledger check beats model check; plain resampling is a strong baseline (d15) |
| B8 (T6) | B1 items with a difference hint | Correct hint; wrong but relevant; vague; irrelevant; no hint | Solve rate relative to no-hint | Wrong-but-relevant keeps most of the gain; irrelevant falls below no-hint (d14 pattern) |
| B9 (Hanoi, K21-K23) | Hanoi at N = 8, 10, 12, 15 | (a) model emits full list; (b) code holds state, model picks next move, no algorithm; (c) same with algorithm in the prompt; (d) (b) and (c) each with k=3 voting and a visited-state guard | Correct full solutions; first error position; loops | (b) shows loops; (c)+(d) near zero errors; a gap between (b) and (c) tells us strategy-finding vs execution |
| B10 (T7) | Items with an explicit goal test (24 game, small Blocksworld, PrOntoQA-like) vs items without (open questions, ARC) | Model searches; model writes successors and goal test once, code searches | Solve rate; tokens; code-fix rounds | Near 100% on explicit-goal items; no applicability on open items |
| B11 (T8) | Multi-goal items with exclusion | With vs without compatibility prune | Wasted model calls; solve rate | Fewer wasted calls at equal solve rate |
| B12 (T9) | Items from two problem classes | Memory tagged by class vs untagged vs none; same-class vs cross-class reuse | Solve rate; harmful hint rate | Same-class reuse helps; cross-class reuse fades or hurts; retire-on-change fixes |
| B13 (T10) | Per-class runs, small and large models | Scaffold vs CoT; fallback rule on | Net gain across classes | Scaffold hurts small models on hard structure; fallback recovers the loss |

---

## 9. What does not transfer, and why

- **The hand-made difference-operator table.** Quality of the table decided GPS success [a02]. In our agent the model writes the differences itself, and nobody has measured how wrong it can be. Do not copy a fixed table from GPS.
- **Domain-free "general" claims.** Norvig: "not a very general problem solver at all" [a15]. Gains reported for MEA are on one synthetic domain [c01].
- **Backward chaining as default.** Deduction over rules (LAMBADA) and state-changing planning (GPT-4o on Blocksworld) behave differently [c03, c04, critique]. Do not carry the deduction result to planning.
- **Human move-subsequence chunking.** Greeno and Thomas describe forward-organised subsequences, read here only from abstracts [a24, a25]. An LLM with a code-held stack does not have human working-memory limits. Fansher's goal recursion under working-memory load [a30] does not map one to one to a context window.
- **Human think-aloud protocol fit.** The 1972 book's fit statistics were never read [a36].
- **Human detour behaviour.** The candidate non-greedy rule (K30) is derived from a production-system fit and two LLM loop studies, not from the human primary papers. It is a hypothesis.
- **Hanoi as a general planning test.** Hanoi has branching factor 1 under the recursion; Blocksworld branching is O(N^2) [b08]. Success on Hanoi says little about search. Difficulty should be measured by branching, not solution length.
- **Open problems with no goal state.** MEA needs a describable goal to compare against. For open tasks (ideas, novelty) there is no difference to reduce. The code-held search route (d11) is closed there. This matches schema G8 (novelty judged by running, not by opinion) and the "no goal state" case in open mode.
- **Prodigy control-rule learning as a model.** Gains were modest (unsolved 218 to 135; time not significantly lower), explanation-based learning did not transfer between linear and nonlinear planners, and rule-matching cost is real [a17, a18].
- **Human exploration-to-learn.** People did not invest early moves in exploration [a27, a28]. We should not rely on explore-to-learn inside one run; store lessons only from real failures (matches S9 and the memory rule).
- **Instruction-based strategy shifts in people.** Accuracy versus effort wording moved strategies in 34 students [b23]. G11 and G1 say our agent should not change strategy by instruction wording or schedule.
- **Voting at MAKER scale.** G4 says votes from one model are not independent. MAKER worked because Hanoi steps are deterministic and the error check was rule-based [c17]. Only the over-length discard rule may carry.
- **Fine-tuned planners.** Gains from training on planning data (c21, d17) are not available to a scaffold-only agent.

---

## 10. Open questions

1. **Thinking on.** Does an explicit MEA scaffold still help when the model reasons natively, at equal tokens, against CoT pass@k plus a verifier? Indirect evidence predicts small gains and some risk [d13, d07].
2. **Which part carries the gain.** Ledger, calculation hints, stack, difference naming. Nothing isolates naming. Fine-tuned evidence says goal-distance counting can hurt [d17].
3. **Transfer.** Does it work on ARC grids, code repair, or open questions? Positive transfer exists on ALFWorld, WebShop, TextCraft, deduction and mixing; negative on goal-distance counting and on search-style prompts for some models [K33].
4. **Human detour data.** What did Thomas (1974), Greeno (1974), Jeffries et al. (1977) and Simon and Reed (1976) actually show about moves away from the goal? Primary texts unopened. Can the data be turned into a rule for when the agent may make a non-greedy move?
5. **Table-error tolerance.** How wrong can the model's difference naming or operator hint be before MEA loses to free CoT? Nothing measured on operator tables [K02].
6. **Goal clobbering rate.** How often do LLM outputs on multi-goal items end with an earlier goal broken, and does a final all-goals check fix it? No study [K34].
7. **When to decompose.** Always, or only on failure? Do ADaPT's results survive current and thinking models, and at what depth cap? [K18]
8. **Hanoi with code-held state.** Is the collapse real once code holds the move list? The exact test (8 to 15 disks, algorithm given or not, voting or not, visited-state guard) is not run. Can the model find the strategy at all? [K21-K23]
9. **Control-rule memory.** Does Prodigy-style learned control knowledge carry to an LLM agent and survive a change of problem class? Adjacent evidence only [d20, d21].
10. **Checker accuracy threshold.** How accurate must a subgoal checker be before checks help rather than add false progress? Candidate rule (derived, not from a source): expected false progress is about (rate of wrong subgoals) times (false-accept rate), and the false-reject rate costs retries. Untested [critique gap 10].
11. **Replication of MEDAKA.** One preprint, 18 Oct 2026, no replication, one domain, 2 ablated models.
12. **Serial decomposability.** Korf's boundary (subgoals that can be solved in order without undoing earlier ones) is a testable class tag. Is it detectable from the item before solving? [a33]
13. **False-plan rate of abstract plans** (GPS planning heuristic) [a05].
14. **Prompt style and how the operator is described.** LLM-written natural-language operator prompts matched hand-written ones and beat raw PDDL in action choice, abstract only [c24].
15. **Dissociation of strategy and execution.** MAKER explicitly covers execution, not insight. No result shows an LLM finding a long decomposition and then executing it [d10].

---

## 11. Sources

[V] = opened (page or PDF text read this run). [M] = snippet, abstract or secondary quote only; use as a pointer.

**Classical**
- [V] Newell, Shaw and Simon (1959) Report on a general problem-solving program, RAND P-1584. https://bitsavers.org/pdf/rand/ipl/P-1584_Report_On_A_General_Problem-Solving_Program_Feb59.pdf (a01-a06)
- [V] Newell, Shaw and Simon (1958) Elements of a theory of human problem solving. https://cse.buffalo.edu/~rapaport/Papers/Papers.by.Others/newell-etal58-EltsThHProbSlvg-PsyRev.pdf (a07)
- [V] Newell and Simon (1976) Computer science as empirical inquiry: symbols and search. https://schiaffonati.faculty.polimi.it/TFI/newell_simon_1976.pdf (a08, a09)
- [V] Fikes and Nilsson (1971) STRIPS. https://www.cs.uky.edu/~sgware/reading/papers/fikes1972strips.pdf (a10, a11)
- [V, thin: summary and preface only] Hewitt (1969) PLANNER. https://www.ijcai.org/Proceedings/69/Papers/030.pdf (a19)
- [V] Norvig (1992) Paradigms of AI Programming, chapter 4. https://raw.githubusercontent.com/norvig/paip-lisp/main/docs/chapter4.md (a12-a15)
- [M] Newell and Simon (1972) Human Problem Solving, seen only as quoted in Norvig. Same URL (a36)
- [V] Veloso et al. (1995) Integrating planning and learning: the PRODIGY architecture. https://www.cs.cmu.edu/~mmv/papers/JETAI95.pdf (a16, a17, a18, c22)
- [V] Blum and Furst (1997) Fast planning through planning graph analysis. https://www.cs.cmu.edu/~avrim/Papers/graphplan.pdf (c23)
- [M] Korf (1985) Macro-operators. https://doi.org/10.1016/0004-3702(85)90012-8 (a33)
- [M] Chapman (1987) Planning for conjunctive goals. https://dspace.mit.edu/handle/1721.1/6947 (a34)
- [V] Wikipedia, Sussman anomaly. https://en.wikipedia.org/wiki/Sussman_anomaly (b24)

**Human problem solving**
- [V] Schmalhofer and Polson (1986) A production system model for human problem solving. https://epub.uni-regensburg.de/13639/1/ubr06084_ocr.pdf (a20, a21, a22, d01, d02)
- [M] Jeffries, Polson, Razran and Atwood (1977). https://doi.org/10.1016/0010-0285(77)90015-9 (a23, b28, d05; abstract page only)
- [M] Greeno (1974) Hobbits and orcs. https://deepblue.lib.umich.edu/items/c5c58de3-37e6-47e6-94da-2e050f1a5a3e (a24, b27, d03)
- [M] Thomas (1974) An analysis of behavior in the hobbits-orcs problem. https://doi.org/10.1016/0010-0285(74)90014-0 (a25, d04)
- [M] Simon and Reed (1976) Modeling strategy shifts in a problem-solving task (a32; citation only, no URL recorded)
- [M] Anzai and Simon (1979) The theory of learning by doing. https://pubmed.ncbi.nlm.nih.gov/493441/ (a26)
- [M] Kotovsky, Hayes and Simon (1985) Why are some problems hard? (a31; citation only)
- [V] Levin et al. (1987) Reflexibility in problem solving. https://journalpub.escholarship.org/cognitivesciencesociety/article/30490/galley/20339/download (d06)
- [V] Neth and Payne (2002) Thinking by doing? https://www.psych.uni-goettingen.de/de/cognition/publikationen-dateien-neth-3/2002_nethpayne_thinking-by-doing_epistemic-actions-in-the-tower-of-hanoi.pdf (a27, a28)
- [V] Fansher, Shah and Helie (2022) Mode of presentation on Tower of Hanoi. https://ccn.psych.purdue.edu/papers/Fansher-TOH.pdf (a29, a30, b22)
- [V] Spitz, Minsky and Bessellieu (1984) Subgoal length versus full solution length. https://link.springer.com/article/10.3758/BF03333826 (b19)
- [V] Clement and Richard (1997) Knowledge of domain effects in problem representation. https://hal.science/hal-02004921 (b20, b21)
- [V] Fum and Del Missier (2001) Adaptive selection of problem solving strategies. https://conferences.inf.ed.ac.uk/cogsci2001/pdf-files/0313.pdf (b23)
- [V] Problem solving as probabilistic inference with subgoaling (2016), PLOS Comput Biol. https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1004864 (b25; first 100,000 of 141,000 characters via fetch summary)

**Language models**
- [V] Li and Kingsford (2026) Means-ends analysis helps LLMs plan in continuous-state domains (MEDAKA). https://arxiv.org/abs/2610.24928 and https://arxiv.org/html/2610.24928 (b01-b05, c01, c02, d22)
- [V] Kazemi et al. (2023) LAMBADA. https://arxiv.org/abs/2212.13894 (b11-b13, c04, c05)
- [V] Lee and Hwang (2025) SymBa. https://arxiv.org/abs/2402.12806 (c06; table columns garbled)
- [V, PDF re-open failed in critique, text read earlier] Stechly, Valmeekam and Kambhampati (2025) Chain of thoughtlessness. https://arxiv.org/abs/2405.04776 (b14, b15, c07, c08)
- [V] Valmeekam et al. (2023) PlanBench. https://arxiv.org/abs/2206.10498 (c09)
- [V] Kambhampati et al. (2024) LLMs can't plan, but can help planning in LLM-Modulo frameworks. https://arxiv.org/abs/2402.01817 (c10)
- [V] Valmeekam et al. (2024) LLMs still can't plan; can LRMs? https://arxiv.org/abs/2409.13373 (c11)
- [V] Sel et al. (2025) Algorithm of Thoughts+. https://arxiv.org/abs/2501.13545 (b16-b18)
- [V] Thinking forward and backward: effective backward planning with LLMs. https://arxiv.org/abs/2411.01790 (c03, d18)
- [V] Shojaee et al. (2025) The Illusion of Thinking. https://arxiv.org/abs/2506.06941 and https://arxiv.org/html/2506.06941 (a35, b09, b10, d07). Apple page https://machinelearning.apple.com/research/illusion-of-thinking [M] (c12)
- [V] Lawsen (2025) The Illusion of the Illusion of Thinking. https://arxiv.org/abs/2506.09250 (b06-b08, c13)
- [V] Khan, Madhavan and Natarajan (2025) Reframing the reasoning cliff as an agentic gap. https://arxiv.org/abs/2506.18957 (c14)
- [V] Rethinking the Illusion of Thinking (2025). https://arxiv.org/html/2507.01231 (d09); abstract page [M] https://arxiv.org/abs/2507.01231 (c15)
- [V] Su et al. (2025) Limits of emergent reasoning of LLMs in agentic frameworks for deterministic games. https://arxiv.org/html/2510.15974v1 and https://arxiv.org/abs/2510.15974 (c16, d08)
- [V] Meyerson et al. (2025) MAKER, solving a million-step LLM task with zero errors. https://arxiv.org/abs/2511.09030 (b26, c17, d10; text copy read)
- [V] Prasad et al. (2024) ADaPT. https://arxiv.org/abs/2311.05772 (c18, d12)
- [V] Wang et al. (2026) Subgoal-driven framework for long-horizon LLM agents (SGO, MiRA). https://arxiv.org/abs/2603.19685 (c19; first part only)
- [V] Li et al. (2024) Systematic analysis of LLM contributions to planning. https://arxiv.org/abs/2412.09666 (c20)
- [V] Pallagani et al. (2023) Understanding the capabilities of LLMs for automated planning. https://arxiv.org/abs/2305.16151 (c21; table layout garbled)
- [M] Automating the generation of prompts for LLM-based action choice in PDDL planning. https://arxiv.org/abs/2311.09830 (c24)
- [M] Large language models for planning: a comprehensive and systematic survey. https://arxiv.org/abs/2505.19683 (c25)
- [V] Katz, Kokel, Srinivas and Sohrabi (2024, v3 2026) Thought of Search. https://arxiv.org/abs/2404.11833 (d11)
- [V] Meincke et al. (2025) Prompting Science Report 2: decreasing value of chain of thought. https://arxiv.org/abs/2506.07142 (d13)
- [V] Wang et al. (2022) Towards understanding chain-of-thought prompting. https://arxiv.org/abs/2212.10001 (d14)
- [V] Stechly, Valmeekam and Kambhampati (2024) Self-verification limitations. https://arxiv.org/abs/2402.08115 (d15)
- [V] Huang et al. (2023) LLMs cannot self-correct reasoning yet. https://arxiv.org/abs/2310.01798 (d16)
- [V] Huang, Lipovetzky and Cohn (2024) Chasing progress, not perfection. https://arxiv.org/abs/2412.10675 (d17)
- [V] Query-efficient planning with language models (2024). https://arxiv.org/abs/2412.06162 (d19)
- [V] Wang et al. (2024) Agent Workflow Memory. https://arxiv.org/abs/2409.07429 (d20)
- [V] Zhao et al. (2024) ExpeL. https://arxiv.org/abs/2308.10144 (d21)
