# Problem-space theory: deep document

*Subfield 01 of A02 (problem-solving research). Built from `evidence_a-d.jsonl` (about 190 evidence lines), `claims.jsonl` (A02.01-K01 to A02.01-K43) and `critique.md`. Evidence ids (a01, b17, c12, d05 and so on) point to those files. Status words: established = two or more independent sources; single-source; contested. The schema parts G, S, O and memory refer to `research_notes/single_agent/SCHEMA.md` v0.2.*

*Read this first: the human-side core of the theory (the 1972 book, Kotovsky, Hayes and Simon 1985, Jeffries 1977, Kaplan and Simon 1990) was never opened as full text. Human numbers below come from the 1958/1959/1966/1975/1976 papers, from Kotovsky and Simon 1990 and Kotovsky and Fallside 1988 (both opened), and from later reviews. Where a number is second-hand, the text says so.*

---

## 1. What it is

Problem-space theory says that a person solving a problem works inside a **problem space**. The space has four parts:

- **States.** Each state is a description of what the solver knows or has built so far.
- **Operators.** An operator turns one state into another. It has legality conditions (when it may be applied) and an effect.
- **An initial state and a goal test.** The goal test is a check: does this state count as a solution?
- **Search control.** Knowledge that picks which state to expand and which operator to apply next.

Solving is search from the initial state to a state that passes the goal test. (Newell 1966, a08; Newell and Simon 1976, a11.)

Newell and Simon's compact form: *a problem is a test plus a generator.* You know how to recognise a solution. You do not have a generator that produces one directly. Solving is generating symbol structures until one passes the test (a11).

Four claims make up the theory:

1. **Search is the basic act.** All goal-directed thinking is search in a space, even when it looks like insight (a08, a05).
2. **Selectivity, not speed, makes search tractable.** Tree size is B to the power D. Blind search is hopeless. Intelligence is the use of information in the space to steer the generator (a03, a12, a13).
3. **The solver's internal representation defines the space, not the task as written.** The same task can be several different spaces. Difficulty lives in the solver's space (a50, a69, a62-a72).
4. **Spaces are built dynamically and are not given.** How a solver builds a good space for a new problem is the unsolved part. Newell said so in 1966 and again in 1976 (a08, a15).

**Why this matters for our agent.** Our schema is already a problem-space system in disguise: S1 and S2 build the space, S3 generates, S4 is the goal test, S5/S6 are search control with impasses, O1 to O8 are operators. This document asks what the theory and its tests say about each of those parts, and what the language-model literature on "reasoning as search" says about the cost and benefit of making the search explicit.

**One-paragraph verdict.** The strongest, most reusable results are these. (a) Explicit state, operator and goal-test objects match the theory and make external checking possible. (b) Search pays only where plain reasoning fails, a reliable evaluator exists, and the model is strong enough to propose good steps. (c) A sound external check beats every kind of self-critique, and plain resampling plus a checker is a hard baseline to beat. (d) How a problem is encoded can change difficulty by factors of 2 to 16 for people, and by a similar order for models. (e) Whether tree search beats best-of-N at equal cost is still open: no paper ran the clean comparison.

---

## 2. History and theories in depth

### 2.1 Logic Theorist (1955-1958): selective search as a theory of mind

- **What it was.** A program that proved theorems of sentential calculus in *Principia Mathematica*, chapter 2. Three methods were tried in order: substitution, detachment and chaining (a02, a41).
- **Detachment** (to prove A, find a stored B implies A, then prove B) and **chaining** (to prove a implies b, find a implies c, then prove c implies b) each make a new subproblem. Subproblems go on a list. The executive takes the simplest one first (fewest levels). It drops duplicates of problems already tried. It stops when the list is empty or a work tally passes a limit, and then reports no proof (a42).
- **Result.** Of the first 52 theorems, LT proved 38 (73%). About half took under 1 minute each. Most others took 1 to 5 minutes. A few took 15 to 45 minutes (a02).
- **Selectivity.** LT tried substitution on only about 10% of stored theorems, chosen by a similarity description. The authors estimated a brute-force version would need "hundreds or thousands of years" for what LT did in minutes. This is an estimate, not a run (a03).
- **Order effects.** The same theorem (2.48) took about 45 minutes with all earlier theorems stored and about 15 minutes with only the axioms plus theorem 2.16. A 20-second preparation computation saved about a third of the time. So more stored knowledge can slow search, because there are more blind alleys (a04).
- **"Learning" was only storage.** Each proved theorem was saved and became a building block. The authors said that without it the program would stall after the first few theorems (a43). The program itself did not change.
- **Insight redefined.** NSS 1958 treated insight as a mechanism: either sudden solution after hidden (vicarious) trial and error, or heuristics that keep trial and error small. They said that the absence of overt trial and error does not prove grasp of structure (a05). Later critics (Ohlsson, Kaplan and Simon) argue this leaves out representational change (a05 limits; a34).
- **Method note.** The LT heuristics came from the designers' introspection. The group then collected think-aloud protocols from college sophomores on symbolic logic problems and built GPS to match them (a40). The fit was reported in a separate paper.

### 2.2 GPS (1957-1963): means-ends analysis and one general core

- **Structure.** GPS separates general problem-solving heuristics from task content. The same core was paired with task definitions for logic, trigonometry, algebra and integral calculus (a36). Generality comes from hand-written task definitions. GPS did not learn them.
- **Three goal types and three methods** (a37):
  1. Transform object a into object b. Match a to b, find a difference, set a goal of type 3, then a goal of type 1 from the changed object.
  2. Apply operator q to object a.
  3. Reduce difference d between a and b.
  An executive evaluates a goal first (it may reject it as not worth trying), then picks the method and runs it.
- **Subgoal reduction.** All GPS heuristics follow one principle: replace a goal by a set of easier goals. This makes GPS highly recursive. The authors added that this is only a heuristic. None of the chess or checkers programs of 1958-59 made essential use of it (a38).
- **Means-ends analysis rests on three assumptions** (a39):
  1. Differences between the current object and the wanted object can be detected.
  2. Operators change some features and leave others, so they can be indexed by the differences they remove.
  3. Some differences are harder to remove than others. Attack the hard difference first, even if that adds easier new differences.
  It needs a difference table written per domain. The hard-first ranking is supplied by the designer.
- **Why pure means-ends was not enough.** Human logic subjects switched into short bursts of abstract reasoning and then filled in detail. That led to **Planning GPS**, the first planner with several levels of abstraction (before ABSTRIPS in 1974). No system matched how humans switched between levels. In cryptarithmetic, many control choices were not a function of the difference to the goal but came from separate pieces of knowledge (a52).

### 2.3 Protocol analysis and the 1972 book

- **Method (Newell 1966).** The subject thinks aloud. The protocol is split into phrases. A **Problem Behavior Graph (PBG)** is drawn over a problem space, with one node per state of knowledge. A production system is then fitted to the regularities, with a conflict-resolution rule (a07).
- **Scale.** The cryptarithmetic PBG in the 1966 paper has 238 nodes. A second PBG covers about 17 minutes of one subject. Analysis took hours per minute of behaviour. The work is single-subject (a07).
- **Honest limit, in Newell's own words.** The space the subject actually uses is unknown. It must be conjectured, then tested. Validating the program against the protocol is the open problem (a07).
- **Where production systems came from.** The PBGs showed that operators and conditions on states could be written node by node. That is how production systems arose (a51).
- **The book.** *Human Problem Solving* (1972) gathers the protocol studies on cryptarithmetic, logic and chess. It was not opened (a30). Its per-task numbers are missing here.
- **Domain studies cited only by abstract.** Jeffries et al. (1977) on missionaries and cannibals: changing the cover story of four versions did not change the number of legal moves needed but changed the number of illegal moves a lot. A three-stage model with means-ends heuristics, memory assumptions and illegal-move detection fit both (a31, abstract only).

### 2.4 Representation and isomorphs (1974-1990)

- **Hayes and Simon (1974, 1977).** Tower of Hanoi isomorphs ("Monsters and Globes" style) have identical state spaces and differ by about 2 to 1 in solution time (a68, second-hand through Kotovsky and Simon 1990). People who learn an abstract strategy often fail to transfer it to isomorphs (a20).
- **Kotovsky, Hayes and Simon (1985).** Isomorphs differ by up to 16 to 1 (a68, a70, second-hand). Most of the time goes into learning to make moves. Once moves are fluent, hard and easy isomorphs are solved at about the same speed. The authors said this challenged the idea that the size of the problem space sets difficulty, as did the content effects of Wason and Johnson-Laird (a68). The primary 1985 paper was not opened (a32, b20).
- **Kotovsky and Fallside (1988).** The external task environment has an objective search space. The **problem space is the solver's internal representation**: the move operators with their legality tests, and the knowledge states from start to goal. Difficulty tracks the **number of entities that must be imaged to test a move**. The hardest isomorph (Monster Change) took about 16 times as long as the easiest (Tower of Hanoi). Tachistoscopic legality judgements were slower when more entities had to be imaged (a69, a70).
- **Kotovsky and Simon (1990), the Chinese Ring Puzzle.** The real puzzle is extremely hard, yet digital isomorphs with the same search space are not. Section 3 has the numbers (a62-a67).
- **Simon (1975), strategy equivalence.** The same Tower of Hanoi task is solved by four different strategies: goal recursion, a simple perceptual strategy, a sophisticated perceptual strategy, and a rote move pattern. They differ in short-term memory load and in the perceptual tests needed (a56-a58).

### 2.5 Heuristic power, satisficing, ill-structured problems (Simon 1972, 1976)

- **Heuristic power as a ratio.** For regular graphs with branching b and b' and length L, the ratio of searched to full graph is (b'/b) to the power L. MATER (a chess mate-finder) cuts branching from about 20 to 2. At L = 6 that is about 64 million branches down to 64 (a45).
- **Abstraction.** A path of length L cut into k segments by waypoints reduces search from b^L to k times b^(L/k) (a46). The saving needs good waypoints.
- **The price of selectivity is completeness.** MATER fails on checkmates that cannot be reached by checking moves (a45). Simon says completeness of a heuristic is orthogonal to its power (a48).
- **Trying promising branches first** multiplies search by an arithmetic constant, not a geometric one, even when s sterile branches are generated beside b productive ones (a46, scan garbled so the factor (b+s)/b is approximate).
- **Satisficing.** Stop at a good-enough solution: one above a norm, or the best found after a set amount of effort (a48).
- **Defence against the ill-defined critique.** Simon argued that ill-structuredness is not a different kind of problem. It appears when a search system works in an information-rich situation where part of the information lies in the environment or memory and is evoked only by recognising features. He saw no fundamental difference between ill-structuredness and task-environment complexity (a47). This is the theory's author defending the theory.
- **Turing lecture (1976).** If solutions are spread at random, no solver beats another. Intelligence needs a pattern that exists, can be detected, and can steer the generator. The amount of search is not a measure of intelligence (a12). Chess: strong players seldom explore trees of more than 100 branches; programs explore a million or more (a13, cited from earlier work). Problem-space synthesis, how a symbol system builds a fitting space for a new situation, "is very much on the frontier" (a15).

### 2.6 Soar (1982 on): the problem-space hypothesis made into an architecture

- **Decision cycle.** Input, elaboration (rules propose, compare and evaluate operators), operator selection, application, output (a16).
- **Impasses.** When knowledge cannot choose or apply an operator, an **impasse** creates a substate, and the same cycle runs there. Three types in Laird (2022): state no-change, operator tie or conflict, operator no-change. The 1987 statement lists four: rejection, tie, no-change, conflict (a16, a55).
- **What the impasse gives.** An automatic switch from fast rule knowledge to slow reflective reasoning. Deliberation in a substate costs time and can be capped, with a random or non-optimal choice if time runs out (a17).
- **Chunking** turns the work done in a substate into a rule, so the same impasse does not recur (a17). It is learning. Our agent cannot train. The nearest scaffold analogue is a per-class cache of solved subproblems.
- **The 1987 hypotheses.** Eleven, among them: problem spaces organise all goal-directed behaviour; any decision can become a goal; impasses create subgoals automatically; weak methods arise from task knowledge; chunking is the one learning mechanism. 52 default productions encode search knowledge such as backtracking and not repeating an operator. Stated gaps: no deliberate planning, no new task acquisition, no creation of new task representations, no recovery from over-general chunks (a55, read via a chapter summary).
- **Dates** (a53): LT 1955-56; first GPS flowchart October 1957; problem spaces named 1965; weak methods 1969; chunking 1981; Soar 1982; impasse-driven subgoals 1983.
- **Perfect goal stack.** Soar and ACT-R assumed a perfect goal stack. Anderson and Douglass (2001) found this wrong for people (section 3, a59-a61).

### 2.7 Critiques inside the tradition

- **Insight and representational change.** Knoblich et al. (1999) and Jones (2003): difficulty on matchstick problems tracks how far a constraint must be relaxed and how tight a chunk is. This is a mechanism of changing the space, not searching it (b33, b22). Reaching an impasse does not by itself produce a change (b24, snippet only).
- **Ohlsson (2012).** The enduring contribution of Newell and Simon is that people solve problems by heuristic search in a problem space, but the theory is seriously incomplete (a34, abstract only).
- **Human difficulty is not state-space size.** Section 3, A02.01-K20 and A02.01-K26 (a64, a65, b19).
- **Strategy variety.** People do not start with goal recursion. They find it. Rote strategies exist (a59, a57).

### 2.8 Language-model search (2023-2026)

- **Tree of Thoughts** (Yao 2023) casts reasoning as search over "thoughts": propose, evaluate with the model, search with breadth-first or depth-first, prune (a21).
- **RAP** (Hao 2023) uses the same model as world model (predict the next state) and agent, with Monte Carlo tree search (a24).
- **LATS** (Zhou 2023) runs MCTS over agent trajectories with environment feedback, a model value function and reflection on failed branches (a26).
- **Algorithm of Thoughts** (Sel 2023) puts a search trace into one prompt (c16).
- **Thought of Search** (Katz 2024) uses the model once to write successor and goal-test code, then runs ordinary search (c17).
- **The skeptic line** (Kambhampati et al. 2024) says the power comes from the external checker, not the search (c11).
- **Sampling line** (Brown 2024, Snell 2024, Wu 2025) asks how search compares with plain sampling at equal compute (b29, d03, d05).
- **Collapse and rebuttal line** (Shojaee, Lawsen, Varela, Su, Meyerson, 2025) asks whether models fail on long puzzle procedures because of capability or setup (c19-c24, d10).

---

## 3. Core findings with exact numbers

Status key: **E** established, **S** single-source, **C** contested. "Source" gives evidence ids. Numbers are as recorded in the evidence files after the critique's corrections.

### 3.1 Human and program studies

| Finding | Numbers | Source | Status |
|---|---|---|---|
| LT proves theorems by selective search | 38 of first 52 theorems (73%); about half under 1 min, most others 1-5 min, a few 15-45 min | a02 | S (one program, one set) |
| Selectivity, not speed, is what works | substitution tried on about 10% of stored theorems; brute force est. "hundreds to thousands of years" vs minutes (estimate) | a03, a12, a13 | E (A02.01-K01) |
| More stored knowledge can slow search | Theorem 2.48: about 45 min with all earlier theorems vs about 15 min with few; 20 s preparation saved about one third | a04 | S |
| Heuristic power is a ratio; selectivity costs completeness | MATER: branching 20 to 2; length 6: 64 million to 64 branches; fails on non-check mates | a45, a46 | E (A02.01-K29) |
| Waypoint abstraction cuts search | b^L to k times b^(L/k) | a46 | E (A02.01-K29) |
| Pure means-ends analysis not enough; humans plan in abstract bursts | Planning GPS; no numbers | a52, a39 | E (A02.01-K29) |
| Tower of Hanoi isomorphs: 2:1 and 16:1 difficulty ratios | Hayes and Simon about 2:1; Kotovsky, Hayes, Simon up to 16:1; same 27-state space | a68, a70 | E but second-hand (A02.01-K25); originals not opened |
| Chinese Ring Puzzle vs digital isomorph (same search space) | Exp 1: 26 students; 1 of 12 solved the real puzzle in 90 min; digital means 25.48 min (No-Info), 14.55 min (Lo-Info); F(2,21)=33.72 | a62 | E (A02.01-K25). The "25 of 26 solved" line in the raw evidence is NOT in the paper and is not used |
| A move demonstration fixes most of the Ring difficulty | Exp 2: 69 students (41 Ring, 28 digital); Ring 79.7 min (floor: non-solvers scored at the cap) vs 19.9 and 13.0 digital; F(2,63)=44.96; 24 of 41 Ring solvers failed in 2 h; hint type no effect F(1,126)=1.85 | a63 | E (A02.01-K25) |
| Search-space size and distance do not set difficulty in a linear space | Start 21 vs 31 moves out: F(1,53)=2.12, p<.2; random walk predicts about 242 moves; observed legal moves 150-450 across isomorphs, minimum 21; minimum time from move speed 77 s = 13% of time taken | a64, a65 | E (A02.01-K26) |
| Behaviour is bimodal: long flailing, then fast run | about two-thirds of subjects with latencies showed long-short patterns | a65, a71 | E |
| Misleading progress heuristic traps solvers | moves from 31 to 21 out raise the "balls out of boxes" count 7 times out of 10 | a65 | S (inferred, not measured) |
| More move information helps only if easy to use | All-Info display: 206 illegal moves/subject without explanation, 46 with; slowest first-position time (about 20.37 vs 18.92 and 12.29 min; ordering probable) | a66 | S |
| Transfer between isomorphs is weak, partly asymmetric | digital to digital: time fell 47.6% and 60.5% (F(1,48)=18.03); Exp 1: 32% and 31% n.s.; no transfer from digital to real Ring | a67 | S |
| Transfer depends on operator compatibility | Monster Move to Acrobat +29.5% / -28.9% (n.s.); Move to Reverse Acrobat +57.4% (sig.) / +38.5% | a72 | S (small cells) |
| Training on the move operator removes isomorph gaps | final-path times close to Tower of Hanoi time | a71 | S |
| Difficulty follows number of entities to image per move test | Monster Change about 16x Tower of Hanoi time | a70 | S (summary of 1985) |
| Several strategies solve Hanoi; people find recursion, not start with it | 4 strategies; 3 disks: 7 moves plus 3 goal-setting steps; simple perceptual rule cycles at 4 disks without a goal stack | a56-a59 | E (A02.01-K28) |
| Goal retrieval has a cost; the goal stack is not perfect | N=10, 5 disks, 15-move problems; time = 2.655 + 0.065*Formulate + 0.053*Store + 0.085*Retrieve; stack inspection requested 1-5% of the time | a59-a61 | S (A02.01-K27); small N |
| External display helps Hanoi | Exp 1 (n=129): 4-disk 100% vs 91% (chi2=4.45, p=.03); 5-disk 93% vs 63% (B=-2.67, p=.001); between-move time 14.04 s vs 7.58 s. Exp 2 (Prolific, n=371): 4-disk 95.5% vs 87.6% (p=.009); 5-disk 87.4% vs 55.3% | a18, b18 | S (preprint; but replicated within the paper) |
| Mental-then-external transfer in Hanoi | Exp 2: 79.3% vs 65.4%, B=.98, p=.0488; Exp 1: B=-0.53, p=.57 | a19 | C (A02.01-K13). Do not build on it |
| Difficulty on transport puzzles tracks a random-plus-greedy walk, not path length | Spearman with solve time: Rush Hour 0.90 both; Sokoban 0.41 (length) vs 0.61 (model); Replacement 0.21 vs 0.49; 120 instances (35/45/40) | b19 | S (A02.01-K20) |
| Insight difficulty tracks constraint relaxation and chunk tightness | matchstick medians A 40 s, B 155 s, C 300 s (cap), D 140 s (N=20, 5-min limit); Exp 3 N=34: tautological items all solved vs Type C regular 61% | b33 | S (A02.01-K31) |
| Think-aloud does not change accuracy; explaining does | r=-.03 over 94 studies, about 3,500 people; explanation raised performance; all reporting added time | b35 | C (A02.01-K30); abstract only |
| Verbal overshadowing of insight is contested | Schooler 1993: solving fell about 25% (insight) vs 5% (non-insight); Gilhooly raw interaction 4% (SE 3.1%), BF 0.92; Fleck and Weisberg no effect | b34 | C |

### 3.2 LLM search and its rivals

| Finding | Numbers | Source | Status |
|---|---|---|---|
| ToT on Game of 24 (GPT-4, 100 games) | IO 7.3%, CoT 4.0%, CoT-SC(100) 9.0%, ToT b=1 45%, ToT b=5 74%; oracle best-of-100 CoT 49%, IO 33%; about 60% of CoT samples fail at step one | a21, b01 | E (A02.01-K03, with caveats below) |
| ToT rerun by AoT authors | 69% (vs 74% own); spread 69-75% is rerun and subset noise | c16 | E |
| ToT cost on Game of 24 | ToT $0.74/case, 5.5k completion tokens, 74%; CoT best-of-100 $0.47, 6.7k tokens, 49%; IO best-of-100 $0.13, 33%. Creative writing ToT about 5x CoT. The "5 to 100 times" line was not found in the paper text | a23, b02, c01 | S (A02.01-K05). "Cheaper than sampling" is wrong in dollars |
| ToT crosswords, 20 test games | ToT letter/word/game 78/60/20% (4 of 20 solved); no prune 65.4/41.5/5; no backtrack 54.6/20/5; oracle state 82.4/67.5/35 (7 of 20); IO 38.7/14/0; CoT 40.6/15.6/1 | b03, c03 | S (A02.01-K06) |
| Weak models lose the ToT gain | GPT-3.5 ToT 19% (IO 6%, CoT 3%) vs GPT-4 74%; GPT-4 generate + GPT-3.5 evaluate 64%; GPT-3.5 generate + GPT-4 evaluate 31% | a23, b04, c02 | E for model dependence; direction of small-model gain is C (A02.01-K08) |
| Evaluator quality | Wang 2024 (100 items, b=5): GPT-4 proposer + GPT-3.5 evaluator 72% at $33.53; + GPT-4 evaluator 76% at $159.87; b=1 GPT-4 evaluator 65%; GPT-3.5 proposer + GPT-4 evaluator 0.38; random evaluator falls steeply | d02 | S (A02.01-K36) |
| Open-model rerun of ToT | Mixtral value fn: BFS-1 18.18%, BFS-3 41.41%, BFS-5 66.66%; finetuned Mistral-7B value fn: BFS-1 47.47%, BFS-5 63.63%; oracle BFS-1 32.32%, BFS-5 61.61%; about 99 problems | b10 | S (student project) |
| ToT where the model is already good | GSM8K IO 51, CoT 86, ToT 90; StrategyQA IO 73, CoT 82, ToT 83 (100 items) | c04 | E (A02.01-K04) |
| RAP Blocksworld (LLaMA-33B) | 2/4/6-step: CoT 0.17/0.02/0.00; RAP(10) 1.00/0.86/0.26; RAP(20) 1.00/0.88/0.42; GPT-4 CoT 0.50/0.63/0.40. Test sizes 30/57/114 | a24, c05 | E (A02.01-K03). The "33% relative gain over GPT-4" is an average; at 6 steps RAP(20) 0.42 vs GPT-4 0.40 |
| RAP on full Blocksworld (Llama-2 70B) | Easy split CoT/RAP(10) by plan length: 2-step .49/1.00, 4 .18/.99, 6 .06/.75, 8 .01/.61, 10 .01/.32; overall .08 vs .65; hard overall .05 vs .51 | c07, b05 | S |
| RAP on math and logic | GSM8K CoT 29.4, CoT+SC(10) 46.8, Least-to-Most 42.5, RAP(1) 48.6, RAP(10) 51.6; PrOntoQA prediction 94.2 vs 87.8, proof 78.8 vs 64.8 | a25, b06, c06 | E (A02.01-K04): small gain over voting |
| LATS | HumanEval pass@1 GPT-3.5: ToT 54.4, RAP 63.1, LATS 83.8; GPT-4: base 80.1, Reflexion 91.0, LATS 92.7. HotPotQA EM GPT-3.5: base .32, CoT .34, CoT-SC .38, ToT .55, RAP .60, LATS(CoT) .62; ReAct variants ToT .39, RAP .54, LATS .63. Game of 24 GPT-3.5: ToT .20, RAP .40, LATS(CoT) .44 | a26, b07, c08, c09 | S. Compare like with like only; part of gain is test feedback |
| LATS ablations | no LM heuristic .37, DFS .42, no reflection .58, full .63 | a27, b08 | S (A02.01-K07) |
| AoT, one prompt | Game of 24: AoT 71% with 1 query (about 1,000 completion tokens) vs ToT 69% with 109.1 queries (about 5,500 tokens); crosswords word success AoT 52% (2 queries) vs ToT 46.5% (over 200 queries); 9% of AoT failures ran out of tokens | c16 | S (A02.01-K17) |
| Controller + rule checker (Sudoku) | 10 puzzles per size: 3x3 10/10; 4x4 9/10; 5x5 8/10; one/few-shot fell to about 0.5 | a28, b09 | S (A02.01-K33); tiny N, not peer reviewed |
| Thought of Search: code operators | Game of 24 1361 of 1361 solvable solved; 1.2 successor tries, 1 goal-test try; crosswords 20/20 (candidates given); BlocksWorld 502 tasks 100%; PrOntoQA 4000 100%. Cost estimates for four datasets: IO/CoT about $40, ReAct about $200, RAP about $14,000, LATS about $16,000 | c17, c18, d06, d07 | E (A02.01-K11) |
| AutoToS: calls until tests pass (minimum 2) | GPT-4o: 24 Game 3.4, PrOntoQA 2.6, Sokoban 2.2, Crossword 5.8, BlocksWorld 2.0. GPT-4o-mini: 8.8, 4.8, 6.4, 9.6, 10.0 (cap). Llama3.1-70b: 7.4, 2.0, 8.2, 6.2, 5.8. 405b: 3.4, 2.0, 2.6, 4.0, 3.2 | d08, d09 | S (A02.01-K38) |
| External verifier loop works; self-critique does not | Blocksworld VAL back-prompting 82% in 15 rounds; Logistics 70%; Mystery BW about 10%. Graph coloring (100 items): no back-prompt 16%; self-critique 1 of 100; sound verifier nearly 40%; binary vs full error list n.s.; resampling n=15 about 40% | b11, b15, c11 | E (A02.01-K09), A02.01-K10 single |
| Self-correction without feedback | GPT-3.5 GSM8K 75.9 to 75.1 to 74.7; CommonSenseQA 75.8 to 38.1; GPT-4 GSM8K 95.5 to 91.5 to 89.0; with oracle stop 84.3 and 97.5 | b16 | E |
| Repeated sampling is strong with a checker | SWE-bench Lite DeepSeek-Coder-V2: 15.9% at 1 sample to 56% at 250; Gemma-2B CodeContests 0.02% to 7.1% at 10,000; Llama-3-8B MATH coverage 82.9% at 100 to 98.44% at 10,000; vote and reward-model picks plateau near 100 samples | b29 | E (A02.01-K22) |
| Cheap model in a verifier loop | calendar: o1-mini $2.70 for 94% vs GPT-4o-mini loop $2.48 for 97%; o1-preview with verifier: hard Blocksworld 98.2% in 7 iterations; Sokoban 12.7% to 43.6% | b32 | E (A02.01-K22) |
| Step-by-step text helps on symbolic tasks | mean CoT gain math 14.2, symbolic 12.3, logical 6.9 points; all other 56.8 vs 56.1; up to 95% of MMLU gain on equals-sign questions | b30 | E (A02.01-K23) |
| CoT in planning is pattern matching | table-to-stack (261 items) GPT-4-Turbo/Claude-3-Opus/GPT-4: zero-shot 19.1/9.96/3.83; Blocksworld universal algorithm 37.1/37.1/51.3; stacking prompt 40.6/24.5/59.3; gains shrink as stacks pass example size; self-consistency lowered scores | b14, c14, c15 | E (A02.01-K23) |
| Tree search over real environment states | VisualWebArena GPT-4o 18.9% to 26.4%; WebArena 15.0% to 19.2%; Llama-3-70B 7.6% to 16.7%; 200-task subset budget c=20: 24.5% to 37.0% (28.5% without self-consistency in the value function); up to 20x LM calls | b31, c08 | S (A02.01-K24) |
| Search vs sampling at equal compute | Naive MCTS with a reward model lost to sampling at every FLOP budget; REBASE beat sampling at about 7x less compute (Mistral-7B: 42.8% at 8.70e14 FLOPs sampling vs 45.0% at 1.36e14 REBASE; Llemma-34B 46.7% vs 49.2%); with a learned verifier tree search beat weighted voting by about 0 to 4 points on GSM8K at 1-3x tokens (BoN .753, weighted voting .819 at 0.83k tokens; BFS .824 at 2.47k; merging cut BFS to 0.88k) | d03, d17 | C (A02.01-K35). Both need a trained verifier |
| Wang 2024 budget-aware | At matched budget CoT self-consistency beat debate and Reflexion on five datasets (GPT-3.5); ToT beat other strategies at GPT-4 but lost to self-consistency at GPT-3.5 on Game of 24 | d01 | S |
| Search helps mid-difficulty, can hurt easy | PRM beam search got worse with budget on MATH levels 1-2, beat best-of-N on 3-4, did nothing on 5; difficulty-based allocation matched best-of-N with up to 4x less compute (64 vs 256 samples); REBASE equal to sampling on easy, ahead on hard | d05, d04 | E (A02.01-K37) on math |
| Small model + good strategy beats bigger model | Llemma-7B + REBASE beat Llemma-34B until 128 samples | d04 | S |

### 3.3 Reasoning models and the collapse debate

| Finding | Numbers | Source | Status |
|---|---|---|---|
| o1-preview on Blocksworld | 600 problems: o1-preview 97.8%, o1-mini 56.6%, best plain LLM (Llama 3.1 405B) 62.6% | b13, c12 | S (A02.01-K14) |
| Loses much under renaming and length | Mystery BW 52.8%; randomized mystery 37.3%; 110 problems of 20-40 steps: 23.63% | c12, c13 | S |
| Flags unsolvable cases poorly | 27% flagged on BW (19% empty plan, 54% full impossible plan); 16% on randomized mystery; 11.5% of solvable instances wrongly called impossible | c13 | S |
| Classical planner | Fast Downward 100% in 0.265 s vs o1-preview 40.43 s average | b13 | S |
| "Illusion of Thinking": three regimes | Plain model matches or wins at low size, thinking wins at medium, both near 0 at high; Hanoi collapse near 8 disks (255 moves); reasoning tokens rise then fall near the cliff; giving the algorithm did not move collapse | c19, c20, c21 | C (A02.01-K15, A02.01-K16, A02.01-K32) |
| Rebuttal: artifact | Full move list about 10 tokens per move (v2 of the comment); ceiling near N=12-13 at 64k, so collapse before N=9 is not just the token limit; River Crossing N>=6 with capacity 3 has no solution; generating-function format gave high accuracy under 5,000 tokens (preliminary) | c22 | C (informal, no count table) |
| Stepwise prompting delays, does not remove | Gemini, Hanoi N=3 to 10, 10 trials per cell; failures still near N=8; two-model dialogue worse (trouble from N=4) | c23 | C |
| Tool-per-move environment collapsed earlier | Hanoi to 8 disks; at n=8 about 40% of the time the model reused earlier continuations | c24 | C |
| Frontier models 2026: thresholds across nine puzzles | accuracy drops often exceed 50% past thresholds; Hanoi level 4: every model except Gemini 3 Pro and DeepSeek V3.2 collapses | c25 | C (not checked per cell) |
| Million-step Hanoi | 20 disks (about 1.05 million moves) solved, zero errors, one run; gpt-4.1-mini, single-move calls, strategy and state in each prompt, first-to-ahead-by-k voting (k_min=3), red-flagging; per-step error 0.0045 (gpt-4.1-mini), 0.0017 (o3-mini), 0.3583 (gpt-4.1-nano); projected cost $3.5K at 95% target; two 10K-step runs had zero steps with errors in both | d10, d11 | S (A02.01-K39); tests execution of a given algorithm |

### 3.4 Other LLM findings tied to the theory

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Encoding changes what a model solves | GPT-4 on 50 easy ARC tasks: direct grid 13 of 50, object-based encoding 23 of 50; of 13 solved, only 3 had correct reasoning | b17 | S (A02.01-K12); object extraction came from a symbolic solver |
| Worked examples close a rule-base gap | GPT-4 two-digit addition: base 10 98.2%, base 9 38.6% at 0-shot; 1/2/4/8 examples: 48.1/67.0/79.7/85.8% | d18 | S (A02.01-K40); not an isomorph design |
| Models write problem specs when a critic runs them | Water jug: LLM-written Soar specs; GPT-3.5 imprecise, GPT-4 needed; critic-in-the-loop success over 86%, over 25 points above one-shot; ablations cost 14 to 37 points | c27, c28 | S (A02.01-K19) |
| Formal action description | M&C elaborations: Claude 3 Opus and Gemini 1.0 Ultra solved none; ChatGPT-4 3; o1-preview 7; LLM+AL 7 automatically, rest after about 3.1 manual corrections; self-revision raised executable programs from 22.3% (7/30) to 86.7% (26/30), correct from 16.6% to 50% | c29 | S |
| Models lose intermediate state | SmartPlay 3-disk Hanoi: about 10% gap to humans (prose only) | c30 | S |
| Insight riddles | 201 riddles; humans 52.9% (95% CI 46.6-59.2, n=126 on 120 items); non-reasoning 7.6%, reasoning 17.6%; 5-39% of wrong answers had the right candidate in the trace and did not endorse it | d13 | S (A02.01-K41) |
| Verbalised confidence is a weak trigger | values cluster at 80-100%; failure-prediction AUROC about 0.52 (black box), 0.61 (best white box) | d14 | S (A02.01-K42) |
| Subgoal text and summarised memory | tyreworld: standard 10%, subgoal-only 40%, HiAgent 60%; five tasks 42% vs 21% average; context -35% on Jericho | d16 | S (A02.01-K43) |
| Mental-set test on LLMs | six items per cell | d12 | Not usable |
| Training on search traces | Countdown 51.27% vs 25.73% (optimal-path only) | c26 | S; training, out of scope |
| MCTS with trained critics | Llama-2-70B GSM8K greedy 57.8, AlphaLLM greedy 73.7, with MCTS 88.9 | a29 | S; training mixed in, out of scope |

---

## 4. Mechanisms and models

Each model below is written so it can be built as a code object or a prompt slot.

### 4.1 The problem-space tuple (the base object)

```
Problem = (S0, ops, test, control)
  S0       : initial state (dict / structured text)
  ops      : list of Operator(name, legal(state)->bool, apply(state)->state)
  test     : goal_test(state)->bool            # code, not opinion
  control  : choose(frontier)->state, order(ops, state)->list
Solve:
  frontier = [S0]; seen = {}
  while frontier and budget:
      s = choose(frontier)
      if test(s): return s
      for o in order(ops, s):
          if o.legal(s):
              s2 = o.apply(s)
              if key(s2) not in seen: seen.add(key(s2)); frontier.append(s2)
  return best_so_far            # G6: never abstain
```

- **`seen` matters.** Newell (1966) noted that two paths reaching an equal state make two separate objects unless the solver stores and compares them, so the space is an exponentially growing tree unless memory merges duplicates (a09). LT dropped duplicates with list Q (a42). In LLM search, state merging cut BFS tokens from 2.47k to 0.88k on GSM8K at similar accuracy (d17, garbled table, single source).
- **Mapping to the schema.** `S0` and `test` are built in S1/S2. `ops` are O1 to O8 plus domain operators. `control` is S6 plus the tree rules in section 4 of the schema.

### 4.2 Heuristic search math (what selectivity buys)

- Blind tree: size b^L. A heuristic that cuts branching from b to b' gives the ratio (b'/b)^L (a45).
- With waypoints (a plan of k segments): k * b^(L/k) (a46). Example: b=20, L=6, k=2 gives 2 * 20^3 = 16,000 instead of 64,000,000. The assumption is that the waypoints are right.
- Ordering promising branches first costs only an arithmetic factor (a46).
- Completeness is traded: a selective generator can miss the solution (MATER) (a45, a48).
- **Engineering reading.** Generate fewer, better candidates per expansion, and keep a fallback expansion that is less selective for when the selective one fails. This matches schema G12 (search only with a foothold) and the open-mode rule in S3.

### 4.3 Means-ends analysis (GPS)

```
solve(a, b):                     # goal type 1
    d = difference(a, b)
    if none: return a
    d* = hardest(d)              # hard-first; designer-supplied ranking
    for q in operators_that_reduce(d*):   # indexed by difference
        if applicable(q, a): a2 = apply(q, a); return solve(a2, b)
        else: a3 = solve(a, preconditions(q)); (then apply q)   # subgoal: make q applicable
```

- Needs three things, all hand-written in GPS: a difference detector, an operator-by-difference index, and a difficulty ranking (a39).
- **Failure case.** Operators that reduce one difference but create another loop. Human subjects escaped by planning in an abstract space and then filling detail (a52).
- **LLM version.** The model can be asked for "the difference between the current state and the goal" and "an operator that removes it". Code must check that the difference really shrank after the operator was applied. This is the O5 (work backwards) neighbour. No LLM test of GPS-style difference reduction against plain generation is in the evidence.

### 4.4 Planning in an abstract space (Planning GPS)

```
plan_abs = solve in space with ops simplified (drop details)       # cheap
for each step in plan_abs: refine with full ops, subgoal per step  # detailed
if refine fails: revise plan_abs using the failing step            # S5
```

Search cost falls from b^L to k * b^(L/k) if the abstract plan is right (a46). Humans did this in bursts (a52). For us this is S3 "step list first, then fill". Evidence for LLMs: none opened, so it is a test (section 8).

### 4.5 Soar decision cycle with impasses

```
loop:
    elaborate(state)                                  # rules propose/compare operators
    op = select(proposed)                             # by preferences
    if op is None or tie or conflict or cannot_apply: # IMPASSE (4 kinds)
        substate = new_state(goal = resolve(impasse)) # recursion with same cycle
        run until impasse resolved or cap
        (optional) chunk result into a rule           # learning
    else apply(op)
```

- **Triggers by code.** No applicable operator, a tie between operators, a conflict, or an operator that does not change the state. None is a model opinion (a16, a55).
- **Cap.** Deliberation is capped, and a random or non-optimal choice is taken if time runs out (a17).
- **Mapping.** S6 in the schema already fires on code-detected conditions (no pass, two rounds with no change, same error twice, budget fraction). Soar adds two: operator tie and operator no-change (an operator applied that changed nothing). Both are cheap to detect in code.
- **Scaffold stand-in for chunking.** After a subgoal is solved, store (problem class, impasse type, operator, result) and offer it by similarity. This is the subgoal library in the schema (memory, section 5). Not tested here.

### 4.6 Representation and move-legality (Kotovsky)

- **Model.** A move has three parts: a representation of the state, a legality test for the move, and the effect. Difficulty in isomorphs comes from the cost of the legality test, measured as the number of entities to image (a69, a70). Time is spent learning to make moves, not on finding the path (a68).
- **Engineering reading.**
  1. Write each operator as `legal(state)` and `apply(state)`.
  2. Make `legal` a code check, so the model does not have to keep the rules in mind.
  3. Where code cannot check it (fuzzy tasks), show 1 to 2 worked moves. A move demonstration closed most of the Ring gap for people (a63). The nearest LLM data point: 8 worked examples lifted GPT-4 base-9 addition from 38.6% to 85.8% (d18).
  4. Rendering that puts the rule in the object removes the memory load (the "Peg Move" version builds rule 2 into the physical stack, a72).
- **Caveat.** Showing all legal-move information at once was slower and caused more illegal moves than a lighter display (a66). Do not dump the whole rule list.

### 4.7 Strategy variants of one task (Simon 1975)

Four ways to do Hanoi, each as a production system:

- **Goal recursion.** Needs the idea of moving a pyramid and a goal stack in short-term memory. Minimal-length path. 3 disks: 7 moves plus 3 goal-setting steps (a56).
- **Simple perceptual rule.** Falls into a non-terminating cycle at 4 disks unless a subgoal stack is kept (a56).
- **Sophisticated perceptual rule.**
- **Move pattern (rote).** Odd moves move the smallest disk, even moves move the next exposed disk, with the smallest disk cycling in a direction fixed by the parity of the number of disks. Needs only move parity and cycle direction. The reasons for moves are not derivable from the problem definition. It breaks when a rule changes (a57).
- **Engineering reading.** For long procedures, a rote rule held in code (parity + direction) is cheaper than keeping a goal stack in context. This is the logic behind the million-step run: the strategy sits in the prompt, the state is passed each call, and each call makes one move (d10).

### 4.8 Goal stack with retrieval cost (ACT-R reading)

Time per goal retrieval grows with how long ago the goal was set. Storage time does not depend on how long the goal must be kept. Goals can be lost (a60, a61). A written, re-read goal stack in the prompt replaces the cognitive stack. This is untested at depth 5 or more (A02.01-K43).

### 4.9 Tree of Thoughts

```
state = problem + partial thoughts so far
expand(state): k candidate next thoughts (propose prompt or sample)
value(state):  model scores "sure / maybe / impossible" (or a code check)
search:        BFS with beam b, or DFS with prune+backtrack
select:        keep top b by value (b=5 in Game of 24; DFS cap 100 steps in crosswords)
```

- **Game of 24.** Three steps. Each step proposes candidate operations from the remaining numbers. Value is sampled several times (Wang et al. 2024 found that evaluating once instead of 3 times lowers accuracy, d02).
- **Parts that carry the gain.** Crosswords: pruning and backtracking (b03). LATS: value function and principled search (b08). A random evaluator collapses ToT (d02).
- **Where it breaks.** The evaluator pruned correct states when words were rare (c03). Search with a GPT-3.5 proposer loses most of the gain even with a GPT-4 evaluator (d02).

### 4.10 RAP (model as world model)

- Same model plays two roles: world model (given a state and an action, predict the next state) and agent (propose actions).
- MCTS selects by a reward made of action likelihood, state confidence and self-evaluation. The best mix depends on the task (c06): likelihood plus a task reward on Blocksworld; self-evaluation best on GSM8K (action likelihood hurt with more iterations).
- Caveat in the paper: the reward for step t sees only the current state, which makes late steps easier (b05).
- **For us.** Where a real simulator or checker exists (code), the world model should be code, not the model. RAP only asks the model to be a simulator because none was available.

### 4.11 LATS

MCTS over trajectories. Selection by UCT-style value. Expansion by sampling n children (n=5). Evaluation by an LM value function plus environment feedback. Reflection on failed branches is stored and reused. Needs an environment that can revert to an earlier state (b07, c08). About 250 model calls per question at k=50, n=5 (b08).

### 4.12 Algorithm of Thoughts

Put worked search traces (with dead ends and backtracking) in one prompt, so the model searches inside a single generation. 1 query instead of about 100. Bounded by context and by the model's ability to keep the search state straight. 9% of failures were token exhaustion (c16). No independent replication found (A02.01-K17).

### 4.13 Thought of Search / AutoToS (code as operators)

```
1. LLM writes successor(state)->list[state] and is_goal(state)->bool from the rule text.
2. Tests: soundness (every returned state is legal), completeness (no legal state missing),
   goal test on known positives/negatives. Partial soundness tests catch bugs unit tests miss.
3. On failure feed back the exact error; repeat up to a cap.
4. Run BFS/DFS in ordinary code.
```

- First-try failures are common: successor 1.2 to 2.8 tries for GPT-4 with human help (d06); with automatic tests GPT-4o 2.0 to 5.8 calls, GPT-4o-mini 4.8 to 10 (d08). Mistakes: missing corner cases, shallow vs deep copy bugs, unsound or incomplete successors (d06, d09).
- Every domain had short exact rules. Transfer to fuzzy rules is untested (A02.01-K38).

### 4.14 LLM-Modulo / verifier loop

```
for round in 1..R:
    plan = LLM(problem, last_error)
    ok, error = VERIFIER(plan)          # sound, external, code
    if ok: return plan
return best_so_far
```

Blocksworld 82% in 15 rounds with VAL (b11). Binary vs full-error feedback showed no difference on graph coloring, and resampling n=15 reached about the same 40% (b15, A02.01-K10). So in that paper the main value of the loop was extra tries plus a sound filter.

### 4.15 Repeated sampling with coverage

Coverage(k) = fraction of problems with at least one correct sample in k draws. It rises about log-linearly with k (b29). With a checker, coverage turns into accuracy. Without one, voting and reward models plateau near 100 samples (b29). So the checker, not the proposer, sets the ceiling.

### 4.16 Single-step execution with voting (MAKER)

```
for step in 1..N:
    state_text = render(state)                          # held outside the model
    votes = []
    while not winner(votes, k):                         # first-to-ahead-by-k
        out = LLM(strategy + state_text)                # one move, max 750 tokens
        if malformed(out): continue                     # red-flag: discard
        votes.append(out)
    state = apply(state, winner)
```

Works if the per-step error p is below 0.5 and errors are decorrelated. gpt-4.1-nano at p=0.3583 was projected at $41.9K against $3.5K for gpt-4.1-mini (d10, d11). This is a test of execution, not discovery. It is a single run by the authors' own system.

### 4.17 Impasse and insight: representational change

Knoblich's model: the solver starts in a space that is too tight. Constraints (for example "plus and equals signs are fixed") and chunks (a "V" read as a Roman numeral) limit the moves. An impasse is followed by constraint relaxation or chunk decomposition, which changes the space. Difficulty rose with how far a constraint had to be relaxed (b33). This is a different mechanism from searching the old space.

---

## 5. What holds up

### 5.1 Replications and independent checks

- **Chinese Ring / digital isomorph.** Difficulty is robust across three experiments in one lab: 1 of 12 solved the real puzzle in 90 minutes while 25-minute-scale digital isomorphs were solved (a62); a move demonstration cut the gap (a63); Ruger (1910) saw a 4-ring version take 62 minutes on average (median 29, range 2 min to 4 h) (a62). Independence is about 2 sources, not 3: Kotovsky and Simon 1990 and Kotovsky and Fallside 1988 are the same school (critique, point 12).
- **External display in Hanoi.** The within-paper replication (Exp 1 undergraduates n=129, Exp 2 preregistered Prolific n=371) keeps the direction in both. The 5-disk gap is 30 points in Exp 1 and 32 in Exp 2 (a18, b18).
- **Self-correction without feedback fails.** Huang 2024 (b16), Valmeekam 2023 and Stechly 2023 (b15) and the Kambhampati position paper (c11) agree. Independent in method, partly the same group.
- **Repeated sampling.** Brown 2024 (b29) plus the cheap-model verifier loop (b32) plus resampling matching back-prompting (b15) point the same way.
- **Gating.** Snell 2024 (d05), Wu 2025 (d04) and Yao's own easy-task numbers (c04) agree that search adds little or hurts on easy items.
- **Evaluator matters.** Yao's generate/evaluate split (b04), the open-model rerun (b10), LATS ablations (b08) and Wang 2024 (d02).
- **ToT Game of 24 rerun.** 69% (AoT authors) vs 74% (Yao) vs 75% on 100 medium problems quoted by Katz (c16, c17). The only like-for-like independent check is a student project (b10) and a different model.

### 5.2 Failures, contradictions and moderators

| Item | What failed or conflicts | Moderator | Ref |
|---|---|---|---|
| Mental-then-external transfer in Hanoi | Borderline in Exp 2 (p=.0488), wrong direction in Exp 1 (B=-0.53, p=.57) | Do not use | a19 |
| Search vs sampling at equal compute | Naive MCTS lost to sampling; budget-aware tree search won; learned-verifier tree search edged weighted voting by 0 to 4 points; GPT-3.5 ToT lost to self-consistency | Quality of verifier and of the proposer; difficulty | d01, d03, d17 |
| Illusion of Thinking vs rebuttals | Collapse real at about 8 disks vs output-length artifact | Output format; state held by program or by model; instance validity | c19-c24, d10 |
| o1 on Blocksworld | Big gain with no explicit search, so search is not the only route | Renaming, plan length, unsolvable cases | c12, c13 |
| Small-model direction | Llemma-7B + search beat 34B; GPT-3.5 ToT 19% vs 74%; Llama-3-70B gained most (relative) in Koh | Who judges the thoughts | d04, d02, b31 |
| "Search vs checker" | Kambhampati: checker supplies the power; ToT, LATS ablations show pruning, backtrack and value function each matter | Both can hold: search needs a reliable evaluator | c11, b03, b08 |
| AoT vs ToT vs code | 71% with 1 query vs 69-74% with about 100 vs 100% with code | Game of 24 is a task where the best scaffold is code, which limits what this says about open tasks | c16, c17 |
| Verbal overshadowing of insight | One study about 25 point drop; replications smaller or none; BF 0.92 inconclusive | Task type; sample size | b34 |
| Mental set in LLMs | Six items per cell; cell values do not match the human pattern | Not usable | d12 |
| Cost claims | "ToT is cheaper than sampling" is wrong in dollars ($0.74 vs $0.47) | Count dollars and calls, not completion tokens only | c01, a23 |
| ToT Table 7 | The paper's own cost text is inconsistent after extraction (prompt tokens 1.4k vs 2.2k favour ToT, dollars favour CoT) | Treat dollars as stated, tokens as uncertain | critique 2 |

### 5.3 Interventions that worked

- **A sound external verifier in a generate-test loop** (Blocksworld 82%; calendar 94-97%; graph coloring 16% to nearly 40%). Evidence: b11, b15, b32. Established.
- **Code-written operators and goal tests for exact-rule puzzles** (100% on four sets, a few LLM calls). c17, d06, d08. Established on puzzles only.
- **Heuristic selection of branches with pruning and backtracking** on deeper tasks (crosswords 20% vs 5%). b03. Single source.
- **Gating by a cheap pass and difficulty bins** (up to 4x less compute than best-of-N). d05. Established on math.
- **Matched prompts for the problem class** in planning (GPT-4 3.83% to 59.3% with the stacking prompt). b14, c14. Gains fade past the example size.
- **Object-based encodings** on ARC (13 to 23 of 50). b17. Part of the gain is outsourced to a symbolic solver.
- **Worked moves / worked examples** (Ring gap removed; base-9 38.6 to 85.8%). a63, d18.
- **Single-step calls with state held outside the model** plus voting (million-step Hanoi). d10. Single run.
- **Subgoal text plus summarised finished subgoals** (tyreworld 10% to 60%). d16. One task.
- **Explicit external display** for people (Hanoi 5-disk 63% to 93%). a18.

### 5.4 Interventions that did not work, or did not help beyond extra tries

- **Richer feedback beyond a sound check** (full error list vs binary: no significant difference). b15.
- **Self-critique** (graph coloring 1 of 100 correct; GSM8K 75.9 to 74.7; GPT-4 GSM8K 95.5 to 89.0). b15, b16.
- **Self-consistency over CoT in planning** (lowered scores on matched prompts). c14.
- **Giving the algorithm** (Hanoi, Checker Jumping): did not move the collapse point in the original paper. c20. (Contested by d10.)
- **Two-model dialogue** (worse than a single agent from N=4). c23.
- **Tool-per-move environment** (collapse earlier). c24.
- **Showing all legal-move info at once** (206 illegal moves per subject without an explanation). a66.
- **Search on easy items** (beam search got worse with budget on MATH levels 1-2). d05.
- **Majority voting over a tree** (bad expansions count as much as good ones; snippet only). b26.

---

## 6. Language models

### 6.1 Baseline behaviour on problem-space tasks

- **Plain prompts fail on search-shaped tasks.** Game of 24, GPT-4: IO 7.3%, CoT 4.0%. About 60% of CoT samples fail at the first step (a21, b01). Blocksworld, LLaMA-33B CoT: 0.17/0.02/0.00 at 2/4/6 steps (a24). Best plain LLM on 600 Blocksworld problems: 62.6% (Llama 3.1 405B) (c12). In 2023, GPT-4 produced about 12% valid plans in the authors' earlier tests (b11, c10).
- **Surface form matters.** Renaming predicates (same state space) took all plain models to 0-2.5% on Mystery Blocksworld, and o1-preview from 97.8% to 52.8% and 37.3% (b11, c10, c12). This is the LLM version of the isomorph effect, shown for planning (A02.01-K25 agent_test; critique 7).
- **Object encoding.** ARC: 13 to 23 of 50 (b17).
- **Long plans.** o1-preview 23.63% on 20-40 step plans (c13). RAP drops by plan length too: easy split 1.00 at 2 steps to 0.32 at 10 steps (c07).
- **Unsolvable cases are not recognised.** 27% flagged (c13).
- **State tracking.** Models lose intermediate state in 3-disk Hanoi (c30); an environment that tracks state did not fix it in one study (c24).
- **Collapse past size thresholds.** Reported across 2025-26 reasoning models (c19, c25); setup effects are disputed (c22, c23, d10).

### 6.2 What changed it, and by how much

| Change | Effect | Cost | Ref |
|---|---|---|---|
| ToT search, b=5 (GPT-4, Game of 24) | 4.0% to 74% | $0.74/case vs $0.47 for CoT best-of-100 | a21, a23 |
| ToT b=1 | 45% | n/a | a21 |
| RAP(20), LLaMA-33B Blocksworld | 6-step 0.00 to 0.42 | 20 MCTS iterations | a24 |
| LATS, GPT-3.5 HumanEval | 83.8% (ToT 54.4%, RAP 63.1%) | test feedback needed; about 250 calls per HotPotQA question | b07, b08 |
| Sound verifier loop | Blocksworld to 82%; graph coloring 16% to nearly 40% | up to 15 rounds | b11, b15 |
| Cheap model in verifier loop | calendar 97% at $2.48 vs o1-mini 94% at $2.70 | 50 iterations | b32 |
| Repeated sampling with a checker | SWE-bench Lite 15.9% to 56% at 250 samples | 250x samples | b29 |
| Code operators (Thought of Search) | 100% on four sets; $ est. 40 vs 14,000 | 1.2 to 10 calls to get code right | c17, c18, d08 |
| AoT (one prompt) | 71% on Game of 24 | 1 query | c16 |
| Single-step voting (MAKER) | 20-disk Hanoi, zero errors | $3.5K projected | d10 |
| Reasoning model (o1-preview) | Blocksworld 62.6% to 97.8% | 40.43 s vs 0.265 s for a classical planner | c12, b13 |
| Worked examples | base-9 addition 38.6 to 85.8% | tokens for 8 examples | d18 |
| Tree search over real web states | VWA 18.9 to 26.4; budget c=20: 24.5 to 37.0 | up to 20x calls per iteration | b31 |
| Difficulty-based allocation | up to 4x less compute than best-of-N | cheap pass | d05 |

### 6.3 What the numbers do not say

- **Almost all of it is on well-defined, checkable puzzles** (Game of 24, Blocksworld, Sudoku, crosswords, Hanoi, unit-tested code). No measured gain on ill-defined problems with no goal test (b27).
- **No clean equal-cost comparison** of tree search with best-of-N plus the same coded checker (A02.01-K35, critique gap 1). Brown 2024 shows coverage with an oracle checker is an upper bound; picked-answer accuracy without one plateaus (b29).
- **Mostly single runs of 2023 closed models** with small test sets (Game of 24: 100 items; crosswords: 20 games; Sudoku: 10 per size) and no confidence intervals.
- **Part of the gain is outside the scaffold.** Unit-test feedback (LATS), a symbolic object extractor (ARC), training (AlphaLLM, Stream of Search).
- **Rival explanation for the search gain: the checker.** Games with an easily coded verifier (Game of 24) are exactly where the checker supplies the power (c11).
- **Reasoning models change the baseline.** o1-preview reaches 97.8% on Blocksworld with no explicit search, but loses it under renaming and length (c12, c13).
- **Size thresholds.** Whether collapse is capability or format is not settled (A02.01-K15, A02.01-K16, A02.01-K32, A02.01-K39).

### 6.4 Model size

- GPT-3.5 ToT 19% vs GPT-4 74% (c02). Weak proposer, strong evaluator: 31% to 38% (b04, d02).
- Llemma-7B + REBASE beats Llemma-34B (d04). A cheap GPT-3.5 evaluator keeps 72% vs 76% for GPT-4 at about a fifth of the cost (d02).
- Llama-3-70B gained 7.6 to 16.7 in a web agent (Koh); GPT-4o 18.9 to 26.4 (b31).
- Reading: the direction depends on who must judge. A02.01-K08 is contested. Our deployment model was never tested.

---

## 7. What our agent should take

Marks: **[E]** established, **[S]** single-source, **[C]** contested. Schema part in bold. Evidence ids in brackets.

### 7.1 Add now (established)

1. **Make state, operators and goal test explicit objects, with the test in code.** Schema: **S1/S2/S4**. [E] A02.01-K02; a08, a09, a11, a06. The theory defines a problem as a test plus a generator. Our S4 already matches. What to add to the text: S2 writes the state schema and the list of operators with a `legal` check, and S4 runs `test` as code.
2. **Selectivity before volume.** Order and prune candidates with cheap heuristics rather than sampling blindly. Schema: **S3, G12**. [E] A02.01-K01; a03, a12, a13. Keep a fallback less selective expansion, because selectivity costs completeness (a45, a48).
3. **Only a sound, external check closes the loop. Do not use self-critique, and do not expect richer feedback to beat extra tries.** Schema: **G2/G3/G5**. [E] A02.01-K09; b11, b15, b16, c11. Already in the schema. New point from this subfield: on graph coloring, binary and full-error feedback did not differ and resampling n=15 matched back-prompting (b15), so the check's main job is to filter, not to teach. [S] A02.01-K10 for that new point.
4. **Plain repeated sampling plus a coded checker is the default baseline in every comparison.** Schema: **G7, S3**. [E] A02.01-K22; b29, b32, b15, c11. Any search arm must beat it at equal tokens and dollars. Report coverage and picked-answer accuracy separately.
5. **Gate effort by a cheap first pass; search is for mid-difficulty items, not easy ones.** Schema: **G1, G12, S0**. [E] A02.01-K04, A02.01-K37; c04, d05, d04, b25. Beam search with a process verifier got worse with budget on easy MATH levels (d05). Bin by the model's own pass rate (model-specific bins beat labelled difficulty, d05). Established on math with trained verifiers; the exact escalation share on our mix is unknown.
6. **Use step-by-step text only where there is a symbolic step.** Schema: **G1/S3**. [E] A02.01-K23; b30, b14, c14, c15. Mean CoT gain 14.2/12.3/6.9 points on math, symbolic, logical; 56.8 vs 56.1 elsewhere.
7. **Where rules are exact and short, have the model write the successor and goal test as code once, then search in code.** Schema: **O1/O2 (code as operator), S4**. [E] A02.01-K11 on puzzles; c17, c18, d06, d08, d09. Always add a repair loop with soundness and completeness tests (A02.01-K38). Transfer to fuzzy rules is [S] (see 7.2).
8. **Representation changes difficulty. Do not rely on one encoding of the problem; test legality in code; add 1 to 2 worked moves.** Schema: **S1/S2, O6**. [E] A02.01-K25; a62-a72, b17, b18, d18. Human data are second-hand for the 2:1 and 16:1 ratios; the Ring data are first-hand. Operational form: S2 produces two renderings (for example grid and object list) and S3 attempts use each in a separate fresh context.
9. **Abstract plan first, then fill detail, when a task has 6 or more steps.** Schema: **S3/O2 (Decompose)**. [E] A02.01-K29; a39, a45, a46, a52, a38. Evidence for humans and theory; for LLMs it is a test (7.2, item 6).
10. **Difficulty is not path length or state-space size. Do not allocate budget by solution length alone.** Schema: **G1/G12, S0**. [E] A02.01-K26; a64, a65, b19, b20. Predict difficulty from other cues (progress-heuristic traps, move-test cost, a cheap-pass pass rate).
11. **Strategy identity is not visible from a correct answer; log it.** Schema: **section 6 logging, O2**. [E] A02.01-K28; a56-a59. Add "strategy used" to the run log, so rote solutions that break under rule changes can be spotted by running a variant.
12. **Report dollars and calls, not only completion tokens, in every arm.** Schema: **G7**. [S] A02.01-K05; a23, b02, c01. Listed here because the ToT cost claim was wrong in dollars; the rule costs nothing.
13. **Store solved results, but offer them by similarity and after the first attempt.** Schema: **memory (lessons, subgoal library)**. [S] a04, a43, a17. LT's only learning was storage, and more stored theorems can slow search (45 vs 15 minutes on one theorem). This supports the existing rule "lessons after the first attempt, trusted after two problems".
14. **Merge duplicate states in code.** Schema: **S6 tree**. Theory [E] (a09, a42); LLM data [S] (d17: BFS tokens 2.47k to 0.88k). Cheap and safe, so it joins "add now" as code only, not as a model task.

### 7.2 Test first

Each item is marked with status, schema part and evidence. The tests are in section 8.

| # | Candidate | Schema part | Status | Evidence | Why not "add now" |
|---|---|---|---|---|---|
| 1 | Tree search with a coded checker beats best-of-N with the same checker at equal dollars | O3 / S4 / G7 | [C] A02.01-K35 | d01, d03, d17, b29, b15, c11 | No paper ran it. Naive MCTS lost to sampling |
| 2 | Pruning and backtracking carry the gain on deep tasks | O3/O4 | [S] A02.01-K06 | b03, c03, a22 | One paper, 20 test games |
| 3 | Evaluator quality is the main driver (swap tree for resampling with the same evaluator) | S4 / G5 | [S] A02.01-K07 (evaluator effect established); A02.01-K36 single | b04, b10, b08, d02 | No arm replaces the tree with resampling |
| 4 | Program-held state, one move per call, vote per step beyond N=8 | O1 / memory / G3 | [C] A02.01-K16, A02.01-K39 | c20, c23, c24, d10, d11 | One reported run; tests execution, not discovery |
| 5 | Written, re-read goal stack at depth 5 and above | memory / S2 | [S] A02.01-K27, A02.01-K43 | a59-a61, d16 | One task, no depth sweep |
| 6 | Plan in abstract steps, then fill (Planning GPS) vs flat step generation | S3 / O2 | [E] for people, untested for LLMs | a46, a52 | No LLM test |
| 7 | Escalate to deliberate search on explicit impasse signals (no legal operator, tie, no-change, failed test, repeated state) vs on stated confidence | S6 / O5 | [S] A02.01-K19, A02.01-K42 | a16, a17, d14, d15 | No head-to-head. Verbalised confidence AUROC about 0.52 supports the impasse side |
| 8 | Forced restructure operator on insight items (matchstick, eight-coin) vs more sampling vs sampling plus candidate-checking | S7 / O6 / O8 | [C] A02.01-K21, [S] A02.01-K31, A02.01-K41 | b33, b22, d13 | Operator itself untested on LLMs. 5-39% of wrong riddle answers had the right candidate in the trace |
| 9 | Code-written operators and goal tests for non-puzzle tasks | O1/O2 | [S] A02.01-K38 | d06, d08, d09 | Every domain had exact short rules |
| 10 | Move-legality check and worked move demonstration close a representation gap at small token cost | S1 / O1 / O6 | [S] A02.01-K40 | d18, a63 | Only an indirect LLM analogue |
| 11 | Operator-compatibility transfer (Kotovsky) in LLMs | S1 / memory | untested | a72 | No LLM study |
| 12 | Difficulty prediction from simple features (random-plus-greedy walk) for budget allocation | G1 / G12 / S0 | [S] A02.01-K20 | b19 | Human puzzles only |
| 13 | Explain-each-step vs plain trace | O6 / S4 | [C] A02.01-K30 | b35, b34, a51 | Think-aloud null on accuracy; explanation helps; insight tasks contested |
| 14 | One-prompt algorithm trace (AoT-style) vs controller-driven search | S4 | [S] A02.01-K17 | c16 | No independent replication |
| 15 | Hierarchical sub-goal memory with summarised finished subgoals | memory | [S] A02.01-K43 | d16 | One task |
| 16 | Search budget curve with and without self-consistency in the value function | O3 / G12 | [S] A02.01-K24 | b31 | One group; 37.0 vs 28.5 depends on voting |
| 17 | Add-on: Soar-style impasse types (tie, no-change) in S6 | S6 | [S] | a16, a55 | Not tested outside Soar |

---

## 8. Concrete tests on our bench

All arms run at equal total tokens (and dollars). Setup cost counts (G7). Each arm logs tokens per state, calls, dollars and path (schema section 6). Where a coded checker exists, every arm uses the same checker. Item types come from our current suites (ARC, BRAINTEASER and the word puzzles used earlier); new item types are named.

| # | Test | Item type | Arms (equal tokens) | Metric | Expected effect and reason |
|---|---|---|---|---|---|
| T1 | Search vs best-of-N with the same coded checker | ARC items with train-example checker; checkable puzzle items (24-style, grid logic) | (a) best-of-N + checker; (b) generate-test-repair loop (2 rounds); (c) tree search over operators with the same checker | cost per solved item; solved at fixed token cap; coverage vs picked-answer accuracy | (c) not better than (a) on easy items; small edge on mid items at best. Prior: A02.01-K35 contested; sampling plus checker is hard to beat |
| T2 | Tree vs resampling with the same evaluator | same as T1, plus one step-valued task | (a) tree with evaluator E; (b) resampling with E picking the best; (c) tree with random E | solved rate, fraction of gain lost with random E | If (b) ~ (a): the evaluator is the gain. Expect (c) to collapse (d02) |
| T3 | Gate threshold | mixed easy/mid/hard items from our suites | (a) always search; (b) cheap pass first, escalate only when the check fails; (c) plain | accuracy by difficulty bin, share escalated, tokens | (b) matches (a) on mid and hard, beats it on easy. Reason: A02.01-K37; check accuracy does not fall on the easy bin |
| T4 | Backtrack and prune ablation | depth 5+ items (multi-step puzzles; long ARC compositions) | full tree; no backtrack; no prune; flat | solved rate by depth | Both ablations lose on depth 5+, little on depth 2-3 (b03 pattern); single-source so expect a smaller effect than 20% vs 5% |
| T5 | Program-held state | long procedures: Hanoi N=6 to 12, long sequence-edit tasks | (a) model emits whole move list; (b) model emits a program; (c) one move per call, state held by code, vote per step if p>0.5; (d) tool-per-move with state returned | success vs N with counts at sizes straddling collapse; per-step error p | (c) holds beyond N=8; (a) falls. Use fresh runs at each N, 10+ per cell. A02.01-K16/A02.01-K39 |
| T6 | Written goal stack | nested subgoal tasks, depth 3, 5, 8 | (a) implicit stack in context; (b) written stack re-read each step; (c) written stack plus summarised finished subgoals | success vs depth; tokens | (b)/(c) help from depth 5 up; no effect at 3. A02.01-K27, A02.01-K43 |
| T7 | Encodings of the same item | ARC, word puzzles (re-rendered) | grid vs object list vs code state; each with and without 2 worked moves; each with and without a coded legality check | accuracy per encoding; gap closed per token | Encoding spread large (b17: 13 vs 23 of 50); worked moves/legality check close part of it (A02.01-K40). Log which encoding wins by class |
| T8 | Renamed-surface variant | planning or rule items with renamed entities | original vs renamed; plain vs scaffold | accuracy drop | Detects pattern matching (c12). A scaffold that holds state in code should lose less |
| T9 | Impasse vs confidence trigger | mixed items | (a) escalate on explicit impasse; (b) escalate on stated confidence below 80%; (c) escalate on schedule | accuracy, tokens, share escalated | (a) beats (b); (b) near chance for failure prediction (AUROC about 0.52) |
| T10 | Abstract plan then fill | tasks with 6+ steps | flat step generation vs plan-then-fill with code check on the plan | accuracy, tokens | Gain on 6+ steps only. Reason: a46, a52; untested on LLMs |
| T11 | Forced restructure | matchstick, eight-coin, riddle items (new item type) | (a) sampling; (b) forced O6/O8 restructure operator on stall; (c) sampling + candidate-checking step (harvest every candidate seen in traces) | solved rate | (c) >= (b) > (a) if A02.01-K41 holds: many errors are non-endorsement of a candidate present in the trace |
| T12 | Code operators on a non-puzzle task | 3 tasks with fuzzy rules (for example schedule constraints, format conversion) | prompted search vs generated successor/goal-test code with repair loop (cap 10) | first-try pass rate against hand-written tests; calls to pass; solved rate | First-try pass lower than on puzzles (A02.01-K38); repair loop recovers most |
| T13 | Strategy log and rule-change probe | any rule-based family | run solved items again with one rule changed | share of solutions that break | Flags rote solutions (A02.01-K28) |
| T14 | Difficulty features for budget | all items | allocation by pass rate vs by solution length vs by progress-heuristic trap flag | accuracy at equal total tokens | Pass-rate allocation wins (d05). Length alone loses (A02.01-K26) |
| T15 | Explain-each-step | mixed items and insight items separately | plain trace vs forced explain | accuracy, tokens | Small gain on non-insight, none or negative on insight (A02.01-K30) |
| T16 | Duplicate-state merging | any tree arm | tree with and without code-side merge of equal states | tokens, accuracy | Same accuracy at fewer tokens (d17 pattern) |

**Pre-registration rules.** Fix the arm list, the token cap and the metric before running. Report per-bin results, not one pooled number. Use at least 30 items per cell where possible. Our suites are small, so report counts, not only rates (the literature's single-run 100-item numbers have no confidence intervals).

---

## 9. What does not transfer, and why

- **Hand-built difference tables and difficulty rankings (GPS).** They were written per domain (a39). Our agent works across domains, and the model proposing the table is the weak part. Keep the idea (index operators by the difference they remove) only where code can compute the difference.
- **A perfect goal stack (Soar, early ACT-R).** People do not have one (a60, a61). A context window is not one either. The lesson is to externalise the stack, not to assume it.
- **Chunking.** It is learning. We do not train. The scaffold stand-in (a per-class cache of solved subproblems) has not been tested, and LT's order-effect result warns that stored knowledge can slow search (a04).
- **Protocol analysis as a model of the LLM.** Think-aloud protocols record human reasoning with moderate fidelity. Written LLM reasoning is not a reliable record of how the model decided (G10). We use outputs and checks, not text.
- **Satisficing as a stopping rule.** Stopping at "good enough" needs a norm. For LLMs the norm is a check pass (G3/G6). Verbalised confidence cannot supply a norm (AUROC about 0.52, d14).
- **The human 2:1 and 16:1 isomorph ratios.** They measure time to learn move rules for people. For a model the cost is in tokens and error rate, and the mechanism (imaging entities in working memory) is different. The ratios are second-hand anyway. Only the direction (representation changes difficulty, worked moves help) transfers, and the LLM evidence is indirect (d18, c12, b17).
- **Search benchmarks.** All are well-defined puzzles with a coded goal test (b27). They say little about ill-defined tasks (open design, writing). The ToT creative-writing result is scored by GPT-4 itself, which G5 and G8 distrust (c04).
- **Cost numbers.** 2023 GPT-4 prices (a23, b02). Estimates of $14,000 and $16,000 for RAP and LATS are the authors' projections at one call per expansion, not measured spend (d07). Use the ratios, not the dollars.
- **Training-based search results.** AlphaLLM (a29), Stream of Search (c26), CogRouter (d15) and trained process verifiers (d03, d05, d17) need training or a learned verifier. They show what signals matter (critics, dead-end traces, step routing), not what a prompt-only scaffold can do.
- **Environment reset.** LATS needs an environment that can revert to an earlier state (b07). Many real tasks cannot.
- **Insight as search.** The theory's own account (hidden trial and error, a05) is disputed by representational-change work (b33, b22). Reaching an impasse does not by itself produce insight (b24, snippet). Do not assume the S6 impasse operator list yields insight.
- **Mental-set and verbal-overshadowing results for LLMs.** The only LLM study is six items per cell (d12), unusable. The human overshadowing effect is contested (b34).
- **Mental-then-external transfer in Hanoi.** Borderline and not replicated within the paper (a19).

---

## 10. Open questions

1. **Matched-cost search vs sampling with a coded checker.** No paper has run best-of-N with the same checker against tree search at equal dollars on a varied task mix (critique gap 1; A02.01-K35).
2. **How much of ToT, LATS and RAP gains is search, and how much is the evaluator?** No study replaces the tree by resampling with the same evaluator (A02.01-K36).
3. **Does code-written search transfer from puzzles to fuzzy tasks?** What is the first-try failure rate of generated operators when rules are not exact (A02.01-K38)?
4. **Is Hanoi / River Crossing collapse real once state is held by a program and instances are valid?** A clean count table around the threshold, the same model on both designs, is missing (A02.01-K15, A02.01-K16, A02.01-K32, A02.01-K39). Nothing new on valid River Crossing instances.
5. **Does the search gain survive on the model we would deploy?** Direction depends on who judges the thoughts (A02.01-K08).
6. **Where is the gating threshold per task type?** The escalation share on our mix is unknown (A02.01-K37).
7. **Do LLMs show the Kotovsky operator-compatibility effect?** Does a worked move or an explicit legality check close a representation gap at small token cost (A02.01-K25, A02.01-K40)?
8. **Can an impasse be detected from state alone, and does a forced restructure help on insight items?** (A02.01-K21, A02.01-K31, A02.01-K41)
9. **Do impasse triggers beat confidence triggers in a prompt scaffold?** (A02.01-K19, A02.01-K42)
10. **Does a written goal stack beat the implicit stack at depth 5 or more?** (A02.01-K27, A02.01-K43)
11. **How are problem spaces built for new problems?** Newell and Simon flagged it in 1966 and 1976. It is still unsolved for LLM agents. Our S1/S2 is a hand-designed answer (a08, a15).
12. **What is the primary human data?** The 1972 book, Kotovsky, Hayes and Simon 1985, Jeffries 1977 and Kaplan and Simon 1990 were not opened. The 2:1 and 16:1 ratios and the move-versus-change timings need a first-hand check.
13. **Do people's strategy mixes matter for context-window goal loss?** Humans lose goals; the LLM papers assume clean stacks and never test whether goal-stack loss matters (critique 7).
14. **Does verbalising help or harm insight tasks for LLMs?** Human evidence is contested (A02.01-K30).
15. **Is the 4-way strategy variety of Hanoi visible in LLM behaviour?** No study asks which strategy a model used.
16. **Subgoal library.** Does a library of solved subgoals (the chunking stand-in) help or hurt, given LT's order effect (a04)? Untested.

---

## 11. Sources

**[V]** = opened as full text (or the page text) this session. **[M]** = snippet or abstract only. Three [V] sources were read through a secondary summary and are marked.

### Human problem solving, programs and architecture

- [V] Newell, Shaw, Simon (1958) Elements of a theory of human problem solving. https://cse.buffalo.edu/~rapaport/Papers/Papers.by.Others/newell-etal58-EltsThHProbSlvg-PsyRev.pdf (a01-a06)
- [V] Newell and Simon (1956) The Logic Theory Machine (RAND P-868, pages 28-50). http://shelf1.library.cmu.edu/IMLS/MindModels/logictheorymachine.pdf (a41-a43)
- [V] Newell, Shaw, Simon (1959) Report on a general problem-solving program (RAND P-1584). http://bitsavers.informatik.uni-stuttgart.de/pdf/rand/ipl/P-1584_Report_on_a_General_Problem-Solving_Program.pdf (a35-a40; URL as recorded, truncated in the evidence file)
- [V] Newell (1966) On the analysis of human problem solving protocols. https://eric.ed.gov/?id=ED131834 (a07-a10)
- [V] Simon and Newell (1965) Heuristic problem solving by computer. https://iiif.library.cmu.edu/file/Simon_box00065_fld04954_bdl0001_doc0 (a49)
- [V] Simon (1972) The theory of problem solving (IFIP 71). https://iiif.library.cmu.edu/file/Simon_box00065_fld05031_bdl0001_doc0 (a44-a48)
- [V] Simon (1975) The functional equivalence of problem solving skills. http://iiif.library.cmu.edu/file/Simon_box00066_fld05072_bdl0002_doc00 (a56-a58)
- [V] Newell and Simon (1976) Computer science as empirical inquiry: symbols and search. https://cse-robotics.engr.tamu.edu/dshell/cs625/new-simon-TA.pdf (a11-a15)
- [V] Laird and Rosenbloom (1992) In pursuit of mind: the research of Allen Newell. https://ojs.aaai.org/aimagazine/index.php/aimagazine/article/view/1019 (a50-a54)
- [V, via chapter summary only] Laird, Newell, Rosenbloom (1987) SOAR: an architecture for general intelligence. https://www.jimdavies.org/summaries/laird1987.html (a55)
- [V] Laird (2022) Introduction to the Soar cognitive architecture. https://arxiv.org/abs/2205.03854 (a16, a17)
- [V] Anderson and Douglass (2001) Tower of Hanoi: evidence for the cost of goal retrieval. http://act-r.psy.cmu.edu/ (path recorded in evidence file, truncated) (a59-a61)
- [V] Kotovsky and Simon (1990) What makes some problems really hard. https://iiif.library.cmu.edu/file/Simon_box00083_fld06643_bdl0001_doc0 (a62-a68)
- [V] Kotovsky and Fallside (1988) Representation and transfer in problem solving. https://grenc.eu/problemperspectives/files/ (path recorded in evidence file, truncated) (a69-a72)
- [V] Fansher, Shah, Helie (2022 preprint) The effect of mode of presentation on Tower of Hanoi problem solving. https://ccn.psych.purdue.edu/papers/Fansher-TOH.pdf (a18-a20, b18)
- [V] Jarusek and Pelanek (2011) What determines difficulty of transport puzzles? https://cdn.aaai.org/ocs/2518/2518-11200-1-PB.pdf (b19)
- [V] Knoblich, Ohlsson, Haider, Rhenius (1999) Constraint relaxation and chunk decomposition in insight problem solving. https://www.kognition.uni-koeln.de/literature/Knoblich_etal_1999.pdf (b33)
- [V, abstract page only] Jones (2003) Testing two cognitive theories of insight. https://irep.ntu.ac.uk/id/eprint/18103/ (b22)
- [V, via secondary summary] Schooler, Ohlsson, Brooks (1993); Gilhooly et al. (2010); Fleck and Weisberg (2004), as summarised in Kiyokawa and Dienes (2019). https://users.sussex.ac.uk/~dienes/Kiyokawa%20&%20Dienes%202019%20Cogsci.pdf (b34)
- [M] Newell and Simon (1972) Human problem solving. https://archive.org/details/humanproblemsolv0000newe (a30)
- [M] Jeffries, Polson, Razran, Atwood (1977) A process model for missionaries-cannibals and other river-crossing problems. https://researchdiscovery.drexel.edu/ (catalog abstract; path truncated in evidence file) (a31)
- [M] Kotovsky, Hayes, Simon (1985) Why are some problems hard? Evidence from Tower of Hanoi. https://www.cmu.edu/dietrich/psychology/pdf/kotovsky_vita.pdf (a32, b20; citation only)
- [M] Kotovsky and Simon (1990), bibliographic record. https://cir.nii.ac.jp/crid/1360574094775442048 (b21; the full text was opened separately as above)
- [M] Kaplan and Simon (1990) In search of insight. https://philpapers.org/rec/BILWTS (a33)
- [M] Ohlsson (2012) The problems with problem solving. https://docs.lib.purdue.edu/jps/vol5/iss1/7 (a34; abstract only)
- [M] Oellinger, Jones, Faber, Knoblich (2013), eight-coin problem (search summary). https://research.ceu.edu/en/publications/cognitive-mechanisms-of-insight-the-rol (b23)
- [M] Search summary on impasse and insight. https://irep.ntu.ac.uk/18103/ (b24)
- [M] Fox, Ericsson, Best (2011) Do procedures for verbal reporting of thinking have to be reactive? https://doi.org/10.1037/a0021663 (b35; abstract via OpenAlex, checked once in the critique pass)

### LLM search, planning and sampling

- [V] Yao et al. (2023) Tree of Thoughts. https://arxiv.org/abs/2305.10601 (a21-a23, b01-b04, c01-c04)
- [V] Hao et al. (2023) Reasoning with language model is planning with world model (RAP). https://arxiv.org/abs/2305.14992 (a24, a25, b05, b06, c05-c07)
- [V] Zhou et al. (2023/2024) Language Agent Tree Search (LATS). https://arxiv.org/abs/2310.04406 (a26, a27, b07, b08, c08, c09)
- [V] Long (2023) Large language model guided tree-of-thought. https://arxiv.org/abs/2305.08291 (a28, b09)
- [V] Sel et al. (2024) Algorithm of Thoughts. https://arxiv.org/abs/2308.10379 (c16)
- [V] Katz et al. (2024) Thought of Search. https://arxiv.org/abs/2404.11833 (c17, c18, d06, d07)
- [V] Cao et al. (2024/2025) Automating Thought of Search (AutoToS). https://arxiv.org/abs/2408.11326 (d08, d09)
- [V] Salahi, Gurusankar, Edamadaka (2024) More effectively searching trees of thought (Stanford CS224N project). URL as recorded in b10 (truncated in the evidence file) (b10)
- [V] Tian et al. (2024) AlphaLLM. https://arxiv.org/abs/2404.12253 (a29)
- [V] Koh et al. (2024/2025) Tree search for language model agents. https://arxiv.org/abs/2407.01476 (b31)
- [V] Wang et al. (2024) Reasoning in token economies. https://arxiv.org/abs/2406.06461 (d01, d02)
- [V] Wu, Sun, Li, Welleck, Yang (2025) Inference scaling laws. https://arxiv.org/abs/2408.00724 (d03, d04)
- [V] Snell, Lee, Xu, Kumar (2024) Scaling LLM test-time compute optimally. https://arxiv.org/abs/2408.03314 (d05)
- [V] Wang et al. (2025) Don't get lost in the trees (FETCH). https://arxiv.org/abs/2502.11183 (d17; table text garbled)
- [V] Brown et al. (2024) Large language monkeys. https://arxiv.org/abs/2407.21787 (b29)
- [V] Sprague et al. (2024) To CoT or not to CoT? https://arxiv.org/abs/2409.12183 (b30)
- [V] Kambhampati et al. (2024) LLMs can't plan, but can help planning in LLM-Modulo frameworks. https://arxiv.org/abs/2402.01817 (b11, b27, c10, c11)
- [V] Valmeekam et al. (2022) PlanBench. https://arxiv.org/abs/2206.10498 (b12; table garbled, no numbers used)
- [V] Valmeekam, Stechly, Kambhampati (2024) LLMs still can't plan; can LRMs? https://arxiv.org/abs/2409.13373 (b13, c12, c13)
- [V] Valmeekam et al. (2024) Planning in strawberry fields. https://arxiv.org/abs/2410.02162 (b32)
- [V] Stechly, Valmeekam, Kambhampati (2024) Chain of thoughtlessness? https://arxiv.org/abs/2405.04776 (b14, c14, c15)
- [V] Valmeekam et al. (2023) Can LLMs really improve by self-critiquing their plans? / Stechly et al. (2023) GPT-4 doesn't know it's wrong. https://arxiv.org/abs/2310.12397 (b15)
- [V] Huang et al. (2024) LLMs cannot self-correct reasoning yet. https://arxiv.org/abs/2310.01798 (b16)
- [V] Xu et al. (2024) LLMs and the Abstraction and Reasoning Corpus. https://arxiv.org/abs/2305.18354 (b17)
- [V] Shojaee et al. (2025) The illusion of thinking. https://arxiv.org/abs/2506.06941 (c19-c21)
- [V] Lawsen (2025) Comment on the illusion of thinking. https://arxiv.org/abs/2506.09250 (c22; informal, preliminary)
- [V] Varela et al. (2025) Rethinking the illusion of thinking. https://arxiv.org/abs/2507.01231 (c23)
- [V] Su et al. (2025) Limits of emergent reasoning of LLMs in agentic frameworks for deterministic games. https://arxiv.org/abs/2510.15974 (c24)
- [V] Utsho et al. (2026) Complexity-induced limits in LLMs on finite discrete state-space problems. https://arxiv.org/abs/2604.13371 (c25; per-cell numbers not checked)
- [V] Meyerson et al. (2025) Solving a million-step LLM task with zero errors (MAKER). https://arxiv.org/abs/2511.09030 (d10, d11)
- [V] Gandhi et al. (2024) Stream of Search. https://arxiv.org/abs/2404.03683 (c26)
- [V] Wray, Kirk, Laird (2024) Eliciting problem specifications via large language models. https://arxiv.org/abs/2405.12147 (c27)
- [V] Yuan et al. (2025) NL2GenSym. https://arxiv.org/abs/2510.09355 (c28; table cells garbled)
- [V] Ishay and Lee (2025) LLM+AL. https://arxiv.org/abs/2501.00830 (c29)
- [V] Wu et al. (2023) SmartPlay. https://arxiv.org/abs/2310.01557 (c30; table garbled, prose gap only)
- [V] Haq et al. (2025) Is your LLM trapped in a mental set? https://arxiv.org/abs/2501.11833 (d12; too small to use)
- [V] Mizumoto et al. (2025) The metacognitive bottleneck (NazoNazo). https://arxiv.org/abs/2509.14704 (d13)
- [V] Xiong et al. (2024) Can LLMs express their uncertainty? https://arxiv.org/abs/2306.13063 (d14)
- [V] Yang et al. (2026) Think fast and slow (CogRouter). https://arxiv.org/abs/2602.12662 (d15)
- [V] HiAgent (2025) Hierarchical working memory with subgoals. https://arxiv.org/abs/2408.09559 (d16)
- [V] Wu et al. (2024) Reasoning or reciting? https://arxiv.org/abs/2307.02477 (d18)
- [M] Mirror paper search summary on majority voting in trees. https://arxiv.org/pdf/2402.14963 (b26)
- [M] Open-question list from the first pass (no source). (b28)
