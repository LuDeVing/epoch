# Constraint satisfaction: deep document

*Subfield C05.10 of heuristic search and planning. Variables, domains, propagation. Key works: Dechter; Mackworth. Schema links: O4 (drop a constraint, here widened to constraint handling) and S4 (test). Evidence ids (a01..d21) are in evidence_a-d.jsonl; claim ids (C05.10-K01..K29) are in claims.jsonl; the cross-check is in critique.md. Dechter's book was never opened. ZebraLogic numbers follow the critique: o1-full 81.0, R1 78.7, o1-preview 71.4, o1-mini 59.7 (evidence c01 has them mislabelled; ignore c01's model mapping).*

## 1. What it is

A constraint satisfaction problem (CSP) has three parts.

- **Variables.** The unknowns. Example: which house each person lives in.
- **Domains.** The finite set of values each variable may take.
- **Constraints.** Rules that limit which value combinations are allowed. Most theory uses binary constraints (two variables).

A solution assigns one value to every variable so that all constraints hold. Sudoku, logic grid puzzles (Zebra puzzles), crosswords, scheduling, map colouring, n-queens, cryptarithms and SAT are all CSPs.

Two tools do all the work.

- **Propagation (inference).** Remove values from domains that cannot be in any solution. Arc consistency is the standard form: a value stays only if every neighbour variable still has a partner value that satisfies the constraint between them.
- **Search.** Pick a variable, try a value, propagate, and back up when a domain becomes empty (backtracking).

Why it matters for our agent. Many reasoning tasks are CSPs in disguise: schedules, plans, puzzles, "find an answer satisfying all of these conditions". The schema has a TEST state (S4) and an operator that works on constraints (O4). This document asks which classical results can become code the program runs, and which LLM results say the model alone cannot do this work. The short answer from the evidence: models are weak at the bookkeeping (tracking domains, detecting contradictions, backtracking), but the bookkeeping is cheap for code. The weak spot of the code route is translating the text into constraints.

## 2. History and theories in depth

### 2.1 Waltz, Montanari, Mackworth (1972 to 1977)

- Waltz (1972, 1975) filtered line-drawing interpretations at picture junctions. This is arc consistency in a special case. His results suggested time linear in picture size. Mackworth credits that to T junctions not passing constraints from stem to crossbar, and says there is "no reason to expect" it elsewhere (a03).
- Montanari (1974) gave the formal theory of path consistency (a03).
- Mackworth (1977), *Consistency in networks of relations* (a01, a02, a03). Defines the CSP as variables, finite domains, unary and binary predicates, drawn as a network. Names three causes of thrashing in backtracking:
  - node inconsistency: a value fails a unary predicate;
  - arc inconsistency: a value has no partner in a neighbour domain;
  - path inconsistency: a pair fits but no third value fits both.
  Quote: "The most obvious source of inefficiency and the easiest to prevent concerns the unary predicates."
- The paper gives AC-1 (re-sweep all arcs until no change), AC-2 (Waltz filtering, spreading outward from a new node) and AC-3 (queue only arcs a deletion may have broken, do not re-queue arcs already waiting). AC-2 is a special case of AC-3. It also gives path-consistency algorithms PC-1 and PC-2. The example network has 5 nodes with domains of size 2 or 3 and shows backtracking repeating the same failure many times. There are no benchmarks in the paper.

### 2.2 Complexity and the tree result (1982 to 1985)

- Mackworth and Freuder (1982) (a04, a05). AC-3 is bounded above by O(a^3 e) and below by Omega(a^2 e) (a domain size, e number of binary constraints). Both are linear in e. On planar graphs Waltz filtering is linear in variables. PC-1 is O(a^5 n^5), PC-2 O(a^5 n^3).
- Same report: depth-first backtracking is O(e a^n) worst case. If the constraint graph is a tree, node plus arc consistency lets a solution be built in at most O(a n) predicate evaluations. A tree problem needs no search.
- Seidel (1983) (a06). Freuder's k-consistency algorithm is O(n^k) worst case.
- Freuder (1978, 1982) (a07, read only via van Beek 1994). Strong k-consistency generalises node (k=1), arc (k=2) and path (k=3) consistency. Theorem: an ordering is backtrack-free if the level of strong k-consistency is greater than the width of the ordering. A tree has width 1, so arc consistency is enough.
- Mackworth, Mulder and Havens (1985) (a10). Hierarchical arc consistency prunes whole groups of values when domains form a tree of subsets. On 10 sketch maps (domains of 2 to 8 values) it used up to about 2x fewer predicate evaluations than AC-3. Best case O(log a (e + jn)) against O(a^3 e).

### 2.3 Dynamic backtracking (1993)

- Ginsberg (1993) (a11). Chronological backtracking throws away good work in unrelated regions when it jumps back. Dynamic backtracking keeps independent progress, stays complete and uses polynomial space. Tested on 19 crossword frames (2x2 to 13x13), 100 attempts each, limit 1,000 backtracks. More successful in 6 frames, less in none. Dynamic vs backjumping, successes out of 100: frame 15 99 vs 14; frame 16 100 vs 26; frame 18 61 vs 0; frame 19 10 vs 0. The author reports cases where it is worse. One domain.

### 2.4 Phase transitions and hardness (1991 to 2001)

- Cheeseman, Kanefsky and Taylor (1991) found in graph colouring a hard region between an easy mostly-soluble region and an easy mostly-insoluble region. Mitchell, Selman and Levesque (1992) put the SAT cost peak where about 50 percent of instances are soluble. Both read second-hand through Grant's thesis (a12; b26 unopened).
- Smith and Dyer: the expected number of solutions of a random binary CSP is E(N) = m^n (1-p2)^(p1 n(n-1)/2). Setting E(N)=1 gives critical tightness p2crit = 1 - m^(-2/(p1(n-1))). Prosser (1996) found it accurate except for sparse graphs (a13).
- Grant and Smith (1996) (a14). Even making a problem arc consistent shows an easy-hard-easy pattern, with the cost peak where about 50 percent of problems can be made arc consistent. Class <20,10,p1>, p1 from 0.2 to 1.0, p2 from 0.01 to 1.00, 1,000 problems per point. AC-3 average cost is close to linear in domain size, far below worst case. Arc consistency removes values mainly in the over-constrained region and does nothing in loose problems. Path consistency (PC2) is too costly as preprocessing.
- Grant and Smith (1996) (a15). Maintaining arc consistency (MAC) builds a far smaller tree than forward checking (FC), stays backtrack-free over a wider range, and reduces exceptionally hard problems. FC is cheaper on small problems. No champion algorithm.
- Exceptionally hard problems (a16). Some very costly searches occur where most problems are easy. Cause: thrashing on an insoluble sub-problem that plain backtracking cannot see. Look-ahead largely removes it. A SAT case needed over 350 million branches (Gent and Walsh 1994).
- Fail-first (Haralick and Elliott 1980) (a17). Choose the variable with the smallest domain. It works, but the explanation (it maximises the chance of failure) is not supported: heuristics built on more accurate failure estimates did not do better, and global degree beat sub-problem degree. Domain over degree (DD) did very well except on fully connected graphs.
- van Beek (1994) (a08). Constraint looseness: if domains have size d or less and every constraint lets each value have at least m partners, the network is strongly ceil(d/(d-m))-consistent. Loose constraints make low-order consistency useless as preprocessing. Loose networks can still be hard.
- Xu and Li (2000) (a18, abstract only). Model RB, a revision of the random model that stays hard at scale. Do not cite its threshold formula; it came from memory.
- Zhang and Yap (2001) (a09, a26). AC-3 shown optimal at O(e d^2) by remembering the last support found for each value. Checks on hard instances, two instance sets: old AC-3 2,272,234 and 3,428,680; AC-3.1 787,151 and 999,708; AC-6 635,671 and 744,929. A 24-year gap between the first estimate and the right bound.

### 2.5 Dechter and the modern frame

Dechter's *Constraint Processing* (2003) is the textbook that ZebraLogic and LR2Bench cite (b25, c24). It covers arc, path and k-consistency, look-ahead search, and tree-width decomposition. We did not open it. Everything above attributed to the field comes from the original reports and a thesis summary. The width idea (Freuder) is the part of that framework that most plausibly turns into a rule.

### 2.6 The LLM turn (2023 to 2026)

Four lines of work:

1. Benchmarks that treat puzzles as CSPs with controlled size: ZebraLogic, LR2Bench, Sudoku-Bench, SPaRC, SATBench, KITAB.
2. Self-critique studies on colouring and Game of 24 (Stechly et al.).
3. Solver offloading: SatLM, Zebra solver pipelines, CP-Bench, CP-Agent, exact-cover tools.
4. Propagation inside generation (GenCP) and trained transformers that propagate and backtrack.

## 3. Core findings with exact numbers

Status key: established = two or more independent sources; single = one source or one team; contested = sources disagree. Evidence ids refer to the jsonl files.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| AC-3 worst-case cost, tightened | O(a^3 e) (1982) to O(e d^2) (2001); checks on hard instances 2.27M and 3.43M (old) vs 0.79M and 1.00M (new) | Mackworth and Freuder 1982; Zhang and Yap 2001 (a04, a09) | Established (K01) |
| Tree-shaped constraint graph needs no search | Arc consistency then at most O(a n) evaluations | Mackworth and Freuder 1982 (a05) | Established (K02) |
| Backtrack-free if strong k-consistency level > width | Width 1 for trees; enforcing k-consistency O(n^k) | Freuder via van Beek 1994; Seidel 1983 (a06, a07, a08) | Established, Freuder second-hand (K02) |
| Hardness peaks at the phase transition | Cost peak where about 50 percent of instances are soluble; also for arc-consistency cost; 1,000 problems per point | Grant 1997 thesis summarising Cheeseman 1991, Mitchell 1992 (a12, a14) | Established, second-hand (K03) |
| Estimate difficulty before solving | E(N)=m^n(1-p2)^(p1 n(n-1)/2); accurate except sparse graphs | Smith and Dyer; Prosser 1996 via Grant (a13) | Established for random binary CSPs |
| MAC beats forward checking on hard problems | Smaller trees; FC cheaper only on small problems | Grant and Smith 1996 (a15) | Established for random CSPs |
| Fail-first works, its explanation does not | Predicted heuristic ordering not borne out; DD very good | Smith and Grant 1997 via Grant (a17) | Single source (K04) |
| Dynamic backtracking beats backjumping | Frame 18: 61 vs 0 of 100; frame 16: 100 vs 26; better in 6 frames, worse in none | Ginsberg 1993 (a11) | Single source (K05) |
| Plain LLMs collapse as CSP size grows | ZebraLogic overall: o1-full 81.0, R1 78.7, o1-preview 71.4, o1-mini 59.7, Sonnet 3.5 36.2, Llama-405B 32.6, GPT-4o 31.7. X-Large: o1-full 42.5, R1 28.5, o1-preview 17.0, o1-mini 12.0, Sonnet 3.5 1.0, GPT-4o 0.5, 405B 0.0 | Lin et al. 2025 (a19, b01, b02, d19) | Established (K06) |
| Voting and sampling give little on large CSPs | GPT-4o 31.7 greedy; majority N=32 38.0 (X-Large 2.5); N=128 37.6; reward-model best-of-32 34.8; self-verify 32.1; oracle best-of-32 60.3, best-of-128 69.1 | Lin et al. 2025 (a20, b03, c02) | Established (K07) |
| Hidden reasoning tokens scale with conflicts, then plateau | o1-mini 5,144.6, o1-preview 5,346.3 vs GPT-4o-mini 502.9, GPT-4o 543.7; about 400 per conflict under 20 conflicts; plateau above 30 | Lin et al. 2025 (a20, b04) | Established (K08) |
| Zero-conflict puzzles need only forward chaining | Z3 conflicts averaged over 32 runs; Small <10^3, Medium 10^3-10^6, Large 10^6-10^10, X-Large above (paper inconsistent: 10^9 or 10^10) | Lin et al. 2025 (a21, d19) | Single paper, design fact |
| Long-chain CSP benchmarks stay hard | LR2Bench mean exact match: o1-preview 23.6, R1 20.0, o1-mini 9.1, GPT-4o 3.2; Sudoku-Bench single-shot: o3-mini-high 14.0, Gemini 2.5 Pro 11.0, Qwen3-235B 8.0, R1 6.0; 9x9 o3-mini-high 2.9; SPaRC o4-mini 15.8 vs humans 98.0 | Chen 2025; Seely 2025; Kaesberg 2025 (a22, b05, b21, b23, c06, d05) | Established (K09) |
| Failure is redundancy and invalid states, not only length | 10-gram redundancy negatively correlated with completion; o1-preview over GPT-4o +37.5 EM Logic Puzzle, +35.5 Sudoku; over 50 percent of o4-mini SPaRC outputs invalid paths; Sudoku-Bench top failure: confident wrong solution | Chen 2025; Seely 2025; Kaesberg 2025 (a23, b06, b22, b23) | Established (K10) |
| Self-critique without a sound verifier fails | Colouring: 16 percent baseline, 2 percent LLM+LLM, 1 of 100 in 15-iteration self-critique, 34-40 percent with sound verifier; Game of 24: 5, 3, 36-38 | Stechly et al. 2023, 2024 (c08, c09) | Established (K11) |
| Sound-verifier gain is mostly extra tries | Binary, one-edge and full-error feedback not significantly different; plain resampling comparable | Stechly et al. 2023 (c08) | Single study family |
| Solver or code offload helps on constraint-heavy tasks | SatLM LSAT 35.0 vs CoT 23.5; ZebraLogic GPT-4o Python one-shot 71.7 vs CoT about 28-33; 3-SAT GPT-4 about 10 to about 100 percent with solver; exact-cover tool with 24B model 97.9 vs 91.7 (o3-mini-high plain); Zebra solver feedback GPT-4 27/114 to 59/114 | Ye 2023; He and Wang 2025; Hazra 2024; Skaisgiris 2026; Berman 2026 (b10, b12, c10, d10, d12) | Established (K12) |
| Formalising is not a free win | Formalizer below direct solving in 15 of 24 pairs; accuracy on most-constrained 20 percent under half the least-constrained in 10 of 12 cells; declarative prompting without solver about equal to standard | Amonkar 2026; Ye 2023 (b07, b08, c03, c11, d03) | Established (K13) |
| Wrong constraint is the dominant formalisation error | 95 percent of Qwen3 semantic errors (80-case audit, 5 per cell); 86 percent of 21 solver-tool Zebra failures are clue-to-symbol; templated SAT clauses 97 percent faithful (100 puzzles) | Amonkar 2026; Skaisgiris 2026; Wei 2025 (d04, d08, d11) | Established, small audits (K24) |
| Programmatic critics without a search solver help | TravelPlanner 180 queries: GPT-4-Turbo 4.4 to 20.6 percent; GPT-3.5 0 to 5; GPT-3.5 with critics beat the GPT-4-Turbo baseline | Gundawar 2024 (d17) | Single source (K23) |
| Chain of thought beats code on non-constraint tasks | GSM8K CoT 94.6 vs code 85.8-92.6; Prolog retries flat at 83 for GPT-4o | He and Wang 2025 (b10, b11) | Single source (K14) |
| CP model-writing gains from inference-time methods | CPMpy gpt-5.1 70.1 to 90.2; Kimi-K2 66.5 to 89.0; MiniZinc 37.8 to 73.2; strict multi-instance 78.3 vs 60.9 (23 problems); retrieved examples lowered accuracy for three models | Michailidis 2026 (b14, b15, b16) | Single source (K15) |
| Agent overhead is not free | CP-Agent Haiku 4.5, 40 problems, 3 runs: easy tokens 15K to 44K (+191 percent), time 18 s to 38 s (+111 percent); hard success 52/60 to 45/60 with a todo tool (fixed 3, broke 3); Sonnet 4.5 100 percent on 101 problems | Szeider 2026 (b17, b18, d01, d02) | Single source (K16) |
| Propagation inside decoding | GenCP sent-1: 3 solutions (vanilla), 4 (meta-variables), 10 (MLM preview depth 2); para-2 3 vs 6; para-4 0 vs 2; 100 percent satisfaction on reported tasks | Regin 2024; Bonlarron 2025 (a24, b24, c13, c14) | Single team (K17, K29) |
| Tree of Thoughts with pruning and backtracking | Crosswords word-level 60 percent vs under 16 for IO and CoT; no backtracking 20 percent; solved 4 of 20 | Yao 2023 (c12) | Single source (K18) |
| LLM-generated streamliners | Reductions of 98 percent or more in some runs on 3 of 7 CSPs | Voboril 2025 (c15) | Single source (K19) |
| Dense-constraint tasks collapse early; longer thinking does not fix | Accuracy drops often above 50 percent past thresholds; Zebra puzzles decline with length for Opus 4, o3, R1 | Utsho 2026; Inverse Scaling 2025 (c21, d13) | Established (K22) |
| UNSAT detection is weak on average | SATBench hard UNSAT: o4-mini 65.0, R1 83.6, V3 74.3, Qwen3-235B 19.6, average 39.3 (random 50); satisfiability bias 68.7 percent of o4-mini errors; error-aware prompt fixed 60.4 and 73.2 percent of known failures | Wei 2025 (c20, d06, d07) | Established, with correction (K22) |
| Naming the algorithm in the prompt helps little | Sudoku 9x9 8.2 to 12.1; N-Queens n=8 22.3 to 28.7; with code access only 67.2 on Sudoku | Srivastava 2026 (c22) | Single source (K21) |
| Trained propagate-then-guess works | GPT-2 style model 99 percent on 100K random Sudoku; one guess suffices for 99.8 percent of boards | Giannoulis 2026 (d14) | Single source (K26) |
| Backtracking in one chain is task-dependent | Helps Sudoku, hurts CountDown, at equal test-time compute in small trained models | Qin 2025 (d15) | Single source (K26) |
| LLM-written solvers rarely gain from search tuning | Median speed-up 1.03 to 1.12x; first-fail chosen 70.4 percent in MiniZinc | Wang 2026 (d16) | Single source (K27) |

## 4. Mechanisms and models

Each item is written so an engineer can code it. The program owns these; the model fills slots only (SCHEMA section 1).

### 4.1 Representation (S2)

Store the problem as three tables.

- `vars`: name list.
- `dom[v]`: set of allowed values per variable.
- `cons`: list of (scope, predicate, text). Keep the original sentence for each constraint (`text`) so we can compare it against its formal form later.

The model produces this table from the problem text. This is the one translation step where errors enter (see 4.7). Unique-value rules ("all different") are written once as a global constraint, not as pairs.

### 4.2 AC-3 with support memory (O4 propagation)

```
queue = all arcs (x,y)
while queue:
    (x,y) = pop
    if revise(x,y):            # remove values of x with no partner in dom[y]
        if dom[x] empty: return FAIL (name the arc and the constraint text)
        for z in neighbours(x) except y: push (z,x)
```

`revise` keeps, for each value, the last support found (AC-3.1). Worst case O(e d^2). After a single new assignment, push only arcs into the changed variable (Mackworth: queue only what a deletion can break). Log every removed value with the constraint that removed it. That log is the "real failing output" that G2 needs.

### 4.3 Is propagation worth running? (G7, G12)

Use cheap code tests first.

1. **Tree test.** Build the constraint graph. If it is a tree, run arc consistency and assign from the root: no search (a05).
2. **Looseness test.** Compute the smallest m (partners per value) over constraints. If d/(d-m) rounds to 1 or 2 only, arc consistency removes little. Skip it (a08, a14).
3. **Expected solutions.** E(N) estimate for random-like parts (a13). Near 1 is the hard zone, so spend most budget there. Far above 1, guessing works. Far below 1, search for the contradiction.
4. **Dry run.** Run propagation once. If it removed nothing, stop running it (a14: it does nothing in loose problems).

### 4.4 Search with look-ahead (MAC)

```
solve(state):
  propagate(state)                      # AC-3.1
  if any dom empty: return FAIL
  if all doms singleton: return state
  v = argmin |dom[v]| (ties: highest degree)    # fail-first / DD
  for val in dom[v]:
      r = solve(state with v=val)
      if r: return r
  return FAIL
```

Check the future domains after every choice. An empty domain means stop now. This removes most exceptionally hard cases (a16). Cap effort per branch and restart (heavy tails).

The smallest-domain rule is a rule of thumb. Do not build fancier failure prediction (a17).

### 4.5 Dynamic backtracking (O4, G2)

When a branch fails, record the set of earlier assignments that caused the empty domain (a conflict set). Retract only the most recent assignment in that set. Keep later assignments that do not touch it. Ginsberg showed gains on crossword frames (a11). Not tested on LLM agents.

### 4.6 One-guess structure

The trained Sudoku model (d14) shows a pattern worth copying in a prompt-and-code loop: propagate until stuck, make one informed guess, propagate again, backtrack on a dead end. For random Sudoku one guess is enough in 99.8 percent of boards. For ZebraLogic, zero-conflict puzzles need forward chaining only (a21).

### 4.7 Checking and translation (S4, S8)

- **Programmatic checker.** For each constraint class, one function that returns the first violated constraint in words (as in the TravelPlanner critics, d17). The model gets that sentence and fixes it. No model self-critique (c08, c09).
- **Translation check.** After the model writes a formal constraint, a second call restates it in words from the formal form only (no source text visible). Code compares the restatement to the original sentence. A mismatch holds the constraint back before solving. Idea from round-trip verification (d09); untested on CSP data.
- **Instance check.** If the task has many instances, test the model on a second instance, because models fit the example (b16: 78.3 vs 60.9).
- **Unsat path.** Add an explicit "no solution" exit that requires a propagation proof (an empty domain with the constraint log) rather than a model opinion (d06, d07).

### 4.8 Solver tool

Give the agent a small tool: submit variables, domains and constraints in a table and get back a solution, or UNSAT with the conflict. Gains are largest at big sizes (d11, d12). Gate it on estimated size (variables times domain), since direct reasoning wins on small puzzles (d11).

## 5. What holds up

### 5.1 Replicated or multi-source

- **Phase-transition hardness.** Cheeseman 1991, Mitchell 1992, Prosser 1996, Grant and Smith 1996 and Hazra 2024 (3-SAT clause ratio about 4.267, GPT-4 falls to about 10 percent in the hard region) all agree (a12, a14, b12). LLMs inherit the same difficulty profile.
- **Collapse of plain LLMs with size.** ZebraLogic, LR2Bench, Sudoku-Bench, SPaRC and Utsho et al. all show steep falls past a size or conflict threshold (K06, K09, K22).
- **Self-critique fails without a sound verifier.** Stechly 2023 and 2024 on colouring and Game of 24; ZebraLogic self-verify 32.1 vs 31.7 (c08, c09, c02).
- **Sampling does not rescue large CSPs.** Majority 38.0 vs oracle 69.1: the picker is the bottleneck (K07).
- **Solver help.** SatLM, ZebraLogic Python, 3-SAT, Berman, exact cover: five lines, all positive on constraint-heavy tasks (K12).
- **Wrong-constraint errors are the cost of the solver route.** Amonkar, Skaisgiris, SATBench (K13, K24).

### 5.2 Failures, contradictions and limits

- **Formalising lost to direct solving in 15 of 24 pairs** (Amonkar), although solver help wins in other papers. Both hold: solvers fix search but move the error into translation. Differences in task (calendar, trip, meeting) and in whether solver feedback is allowed may explain some of it. Not tested head to head.
- **Code is not always better.** GSM8K: CoT 94.6 vs code 85.8-92.6; Prolog retries were flat (b10, b11).
- **More scaffold steps are not monotonic.** CP-Agent todo tool: easy problems cost 191 percent more tokens, hard-problem success 52/60 to 45/60 (d01). Overall the agent still reached 100 percent with a short 50-line prompt that matched an 800-line one (b17).
- **Fail-first is not explained.** The rule of thumb works, the theory behind it does not (a17).
- **Dynamic backtracking is one study in one domain** with a reported case where it is worse (a11).
- **Backtracking in a chain is task-dependent** in trained models (d15).
- **LLM-written search heuristics** gave median speed-up of only 1.03 to 1.12x and sometimes lowered correctness (d16).
- **Explaining the algorithm in the prompt** gave small lifts (Sudoku 8.2 to 12.1) (c22).
- **Retrieved examples** lowered accuracy for three of the CP-model writers (b14).
- **UNSAT** is hard on average (39.3 percent for hard UNSAT, below chance) but not for every model (R1 83.6) (d06).
- **Audit sizes are small.** The 95 percent wrong-constraint figure is an 80-case audit with 5 per cell (d04). The 86 percent figure is 21 failures (d11).

### 5.3 Moderators

- **Size and conflicts.** Plain models above 90 percent on small ZebraLogic puzzles; tool pipelines win at large sizes (d11, a21).
- **Constraint density.** Even solver-based formalisation halves on the most constrained fifth (b08).
- **Model class.** Reasoning models help on Sudoku and logic puzzles (+35 to +37 EM) but loop on contradictions (b06).
- **Representation.** Python frameworks beat MiniZinc (70.1 vs 37.8 baseline for gpt-5.1) (b14). Templated clauses translate much better than free text (97 percent, d08).
- **Feedback type.** With a sound verifier, binary, one-edge and full-error feedback did not differ significantly (c08).

### 5.4 What worked as an intervention

- A sound external checker with a back-prompt (colouring 16 to about 40; TravelPlanner 4.4 to 20.6).
- A solver tool with feedback (exact cover 97.9; Berman 27 to 59 of 114).
- Repeated sampling plus self-verification with solver feedback for CP model writing (70.1 to 90.2).
- Pruning and backtracking in the loop (ToT crosswords 60 percent).
- An error-aware prompt naming common mistakes (fixed 60.4 and 73.2 percent of known failures; not a clean accuracy test).

### 5.5 What did not work

Self-critique, majority voting on large puzzles, reward-model selection, format change (CNF vs menu), extra retries for wrong models, to-do tool overhead, describing the algorithm, retrieved examples for some models, LLM-added solver heuristics.

## 6. Language models

### 6.1 Plain models on CSPs

- **ZebraLogic** (1,000 puzzles, 2x2 to 6x6, search space (N!)^M). Overall: o1-full 81.0, R1 78.7, o1-preview 71.4, o1-mini 59.7, Sonnet 3.5 36.2, Llama-405B 32.6, GPT-4o 31.7. By bin (Small/Medium/Large/X-Large): o1-full 97.2/92.1/78.0/42.5; R1 98.4/95.7/73.5/28.5; GPT-4o 80.0/19.6/2.5/0.5; Llama-405B 81.3/22.5/1.5/0.0 (b01, b02). Greedy decoding for non-o1 models; o1 best of three. Beyond about 10^6 candidate assignments bigger models stop helping.
- **LR2Bench** (850 samples, six CSP types). Mean exact match: o1-preview 23.6, R1 20.0, o1-mini 9.1, QwQ-32B 8.5, GPT-4o 3.2, Qwen2.5-72B 0.9. Mean slot accuracy 58 to 59 for the best, so partial fills are common and full consistency is not. o1-preview uses 11,436 tokens vs 1,486 for GPT-4o (b05). Cryptogram and Drop Quote: best about 13 percent.
- **Sudoku-Bench** (100 puzzles: 15 4x4, 15 6x6, 70 9x9). Single-shot: o3-mini-high 14.0, Gemini 2.5 Pro 11.0, Qwen3-235B 8.0, R1 6.0, Claude 3.7 thinking 5.0, GPT-4.1 2.0. 4x4 40 to 73 percent, 6x6 0 to 13, 9x9 0 to 2.9. Failure: no first logical break-in; brute-force guessing; confident wrong answers (b21, b22, c07).
- **SPaRC** (1,000 path puzzles). Humans 98.0 percent; o4-mini 15.8, 1.1 on difficulty 5; GPT-4.1 1.6. Over 50 percent of o4-mini outputs are invalid paths. Reasoning tokens rose only about 5 percent with difficulty (b23).
- **SATBench** (2,100 puzzles, 4 to 50 clauses). o4-mini 89.3 overall; hard overall 78.0; the average model on hard puzzles 53.0, hard SAT 66.7, hard UNSAT 39.3 (c20, d06). Satisfiability bias is the main error (d07).
- **3-SAT** (Hazra). GPT-4 shows easy-hard-easy; accuracy about 10 percent in the hard band (b12).
- **KITAB** (13,000 queries, over 600 authors). All-correct under 35 percent for GPT-4 and GPT-3.5; with the full book list constraint failures remained; self-generated context increased irrelevant items (b19, b20).
- **Complexity-induced collapse** across nine finite-discrete puzzles: accuracy drops often over 50 percent past thresholds; longer reasoning did not reliably help (c21). Zebra puzzles (BBEH, 5x5 to 8x8, 200 puzzles): Claude Opus 4, o3 and R1 all declined with longer natural reasoning; R1 most (d13).

### 6.2 What changed performance and by how much

| Change | Effect |
|---|---|
| Reasoning model vs chat model (ZebraLogic) | 31.7 (GPT-4o) to 81.0 (o1-full) overall; X-Large 0.5 to 42.5 |
| Majority vote N=32 (GPT-4o) | 31.7 to 38.0; X-Large 0.5 to 2.5 |
| Oracle best-of-128 | 69.1, not reachable without a perfect picker |
| Self-verify (GPT-4o) | 31.7 to 32.1 |
| Self-critique loop, colouring (GPT-4) | 16 percent to 1 of 100 |
| Sound verifier, colouring | about 40 percent |
| Python code one-shot, ZebraLogic (GPT-4o) | about 30 to 71.7 |
| Exact-cover solver tool, 24B model | 91.7 (o3-mini-high plain) to 97.9 |
| SatLM, LSAT (code-davinci-002) | 23.5 to 35.0 |
| 3-SAT, GPT-4 hard region | about 10 percent to about 100 percent with a solver |
| Programmatic critics, TravelPlanner | 4.4 to 20.6 percent (GPT-4-Turbo) |
| Algorithm description in prompt (Sudoku 9x9) | 8.2 to 12.1 |
| Sampling plus self-verify for CPMpy (gpt-5.1) | 70.1 to 90.2 |
| MiniZinc modelling with inference-time methods | 37.8 to 73.2 |
| Todo tool, hard CP problems (Haiku 4.5) | 52/60 to 45/60 |
| Streamliner constraints from an LLM | 98 percent or more search cut in some runs |
| Trained propagate-and-one-guess Sudoku | 99 percent |

Caveat: these rows come from different models, tasks and budgets. Only compare within a row.

### 6.3 Behaviours seen

- Models track constraints locally and lose the global picture. They claim a contradiction that does not exist, give up, or say information is missing (b22).
- They loop on contradictions instead of backtracking (b06).
- They say "satisfiable" too often (satisfiability bias, d07).
- Reasoning models asked to write code still reason like solvers inside the code step; solver-like reasoning used over 1.5x the tokens (c05).
- Token use rises with conflicts for o1 and then plateaus (about 400 per conflict below 20 conflicts; plateau above 30) (b04). On SPaRC the rise with difficulty is small (b23). Effort stops growing exactly where more is needed.
- Models often fit the given example (b16) and mis-write one constraint (d04).
- Diffusion language models may fill cells in flexible order, a propagation-like effect (c27, snippet only; do not rely on it).

### 6.4 Evidence quality

Nearly all LLM numbers are 2025 to 2026 preprints. Models differ in version and mix reasoning with non-reasoning models. Token budgets are rarely matched. We found no study of a prompted propagation-first loop at equal tokens.

## 7. What our agent should take

Status marks: [E] established, [S] single-source, [C] contested. Schema parts: G guardrail, S state, O operator, memory. Evidence ids refer to evidence files; claim ids to claims.jsonl.

### Add now (established)

1. **Replace model self-check of constraints with a program that checks them, and return the first violated constraint in words.** Part: S4, G2. [E]. Evidence: c08, c09, c02, b04, d17 (K11, K23). Extends G2 and G5 to constraint lists. The checker-only share of the gain is still unmeasured (Test first T2), so the claim added is "no model self-check", not a size of gain.
2. **Do not use voting, reward-model selection or persona votes to settle large constraint problems.** Part: G4, G5. [E]. Evidence: a20, b03, c02 (K07). Already covered by G4 and G5; add the CSP numbers as support.
3. **Gate by size and constrainedness, not by model self-report.** Small puzzles: direct reasoning. Large or many-constraint puzzles: code or a solver tool. Part: S0 gate, G12. [E] for the direction (a19, d11, b10, a21); a threshold is [S] (K25). Do not hard-code one; log where direct reasoning starts to fail on our items.
4. **Keep a domain and constraint table in code; remove unsupported values and log each removal with the constraint that caused it.** Part: S2, S4, memory. [E] that propagation is cheap, sound, and useful only where constraints are tight (a02, a04, a09, a14). The benefit inside an LLM loop is untested (T1).
5. **Detect a dead end by an empty domain, not by the model's feeling.** When some variable has no candidates, stop and send the conflict to S5 or S6. Part: S4, G1 (doubt on a signal). [E] (a16: look-ahead removes the worst thrashing; b06: models otherwise loop).
6. **Keep each source sentence next to its formal constraint and report any sentence with no matching constraint.** Part: S2, S4. [E] that translation is the main error source when a solver is used (d04, d08, d11, b09). The back-translation check itself is [S] (T3).
7. **Accept "no solution" only with a program-checked proof (empty domain plus log), never from a model hunch.** Part: S8, G6 refinement. [E] that satisfiability bias exists (d06, d07). G6 still holds: never abstain on the first pass.
8. **Ablate every scaffold step; keep the prompt short.** Part: G7. [S] (b18, d01, b17), consistent with G7 which is already [O].
9. **Use code or a solver only on constraint-heavy tasks.** Part: S0. [S] (b10, b11, K14). Consistent with item 3.

Items 1, 2 and 8 mostly restate existing guardrails with CSP-specific evidence. Items 3 to 7 are the new content. SCHEMA needs only a short "constraint tasks" note under O4 and S4. The tests in UNKNOWNS.md decide anything more.

### Test first

| # | Idea | Part | Status | Evidence | Why test |
|---|---|---|---|---|---|
| T1 | Prompted propagate-then-guess loop (prune domains in a table, then one guess) vs plain long reasoning at equal tokens | O4, S4 | [S] indirect | d13, d14, a21, K28 | No study measures it; trained models do it well. Biggest possible gain |
| T2 | Programmatic checker only (no solver) vs sampling at equal tokens | S4, G2 | [S] | d17, c08 (K23) | Stechly gain may be mostly extra tries; checker share unmeasured |
| T3 | Back-translate each constraint to words, then compare | S2 | [S] | d09, d04 | Round-trip drift test was on legal rules only |
| T4 | Smallest-domain-first as a prompt instruction | O4 | [S] | a17, d16 (K04, K27) | No in-context study; theory not supported |
| T5 | Dynamic backtracking: retract only the culprit, keep independent work | O4, G2 | [S] | a11, d15 (K05, K26) | One crossword study; chronological backtracking is task-dependent |
| T6 | Solver tool gated by size | O4 tool | [S] | d11, d12 (K25) | No measured threshold |
| T7 | Ask for streamlining constraints (extra pruning), verified on small cases | O4 | [S] | c15 (K19) | 98 percent savings in some runs only |
| T8 | Group answer options into classes and prune a class (hierarchical arc consistency) | O4 | [S] | a10 | Only about 2x on small map domains |
| T9 | Tree test: if the constraint graph is a tree, skip search | S4 | [E] in theory, untested on text | a05, a07 | Must first check that the graph can be extracted reliably |
| T10 | Error-aware prompt naming common failure types | G | [S] | d07 | Not a clean accuracy test |
| T11 | Second-instance test for solved constraint models | G3 | [S] | b16 | Multi-instance accuracy 60.9 vs 78.3 |
| T12 | Propagation inside decoding (GenCP) | none | [S] one team | a24, c13 | Needs token-level access; do not build on it |

## 8. Concrete tests on our bench

All arms at equal tokens (input plus output, including setup and tool calls, per G7). Report per-bin accuracy, not only the mean, because the effect lives in the Large bins. Use ZebraLogic-style items with known search-space size and Z3 conflict count, plus items from our own bench that have a CSP shape.

| Test | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| B1 (T1) | ZebraLogic Large and X-Large (search space 10^6 and above), 100 items per bin | (a) plain long reasoning; (b) forced propagation pass in a code-held table, then one guess, repeat; (c) (b) plus programmatic checker | Exact grid accuracy per bin; tokens per solved item | (b) and (c) beat (a) on Large by at least 10 points; X-Large gain smaller. If (b) loses, the model cannot run the loop in text |
| B2 (T2) | Graph colouring, ZebraLogic Medium, TravelPlanner-like items | (a) best-of-N sampling; (b) checker with first-violated-constraint back-prompt; (c) self-critique | Accuracy at equal tokens | (b) above (a) by at least 5 points; (c) not above plain, as in Stechly |
| B3 (T3) | Item sets where a text constraint list becomes code (calendar, Zebra clues) | (a) formalise then solve; (b) formalise, back-translate, compare, then solve | Wrong-constraint rate (hand audit of 50 errors per arm); final accuracy | (b) cuts wrong-constraint rate by at least a third; costs about one extra call per constraint |
| B4 (T4) | Sudoku 4x4 and 6x6, Zebra Medium | (a) fixed order; (b) smallest-domain-first instruction; (c) code table picks the variable | Accuracy and number of backtracks | (c) above (a); (b) near (a) if the model ignores the rule |
| B5 (T5) | Crossword mini frames, scheduling with independent blocks | (a) chronological backtrack; (b) retract culprit set only | Solve rate within a token limit | (b) above (a) when the problem has independent regions; flat otherwise |
| B6 (T6) | ZebraLogic sizes 2x2 to 6x6 | (a) direct; (b) solver tool; (c) gate on size or conflicts | Accuracy by size; tokens | The gate matches (a) on small and (b) on large; the crossover point is the result |
| B7 (UNSAT) | SATBench-style hard UNSAT plus our own infeasible items | (a) plain; (b) propagation proof required for "no solution" | UNSAT accuracy; SAT false-reject rate | (b) lifts UNSAT accuracy by at least 15 points without dropping SAT accuracy more than 3 points |
| B8 (T11) | Constraint models for two instances of the same problem | (a) one instance; (b) second-instance check | Multi-instance accuracy | (b) closes about half of the 17-point gap |
| B9 (T8) | Large option sets with natural classes | (a) flat pruning; (b) class pruning | Checks used; accuracy | Fewer checks, same accuracy |

Run order and cost are in UNKNOWNS.md.

## 9. What does not transfer, and why

- **Worst-case bounds (O(e d^2), O(n^k)).** The agent's cost is tokens and model calls, not predicate checks. Zhang and Yap and Grant both show measured cost far below worst case (a14, a26).
- **Path and higher consistency.** Too costly for preprocessing even in classical solvers (a04, a06, a14). Keep arc level.
- **Random-CSP phase-transition formulas.** Derived for random binary problems; natural-language tasks are structured and not binary. Use as intuition (route by constrainedness), not as a calculator. Xu and Li's formula was not verified.
- **Fail-first theory.** The rule of thumb survives, the explanation does not (a17). Do not build failure-probability estimators.
- **GenCP token-level propagation.** Needs access to model domains and a CP solver around decoding; our agent works with prompts and code. One team, small counts (a24, K29).
- **Trained Sudoku transformers and RL on puzzles (Reasoning Gym, LogicPuzzleRL).** Training is outside our scope. Useful only as a hint that propagate-then-one-guess is a good shape (d14, c23).
- **Industrial CP modelling (ConstraintLLM, MCP-Solver).** Needs fine-tuning, or has no benchmark numbers (c16, c17).
- **Human CSP findings.** The classical literature is about algorithms, not people. Human expert behaviour (Sudoku-Bench: an expert found the break-in in about 4.5 minutes) is one anecdote (c07).
- **Large-puzzle results on small items.** Direct reasoning wins at small sizes, so a propagation scaffold may not pay on easy items (G11, G12; d11).
- **Oracle numbers.** 69.1 at best-of-128 needs ground truth (b03).

## 10. Open questions

1. Does an explicit propagation loop in a prompt beat plain long reasoning at equal tokens on ZebraLogic Large and X-Large? (Gap 1, no study.)
2. How much of the sound-verifier gain (16 to about 40 percent) does a checker without a solver recover, at equal tokens against sampling? (Gap 2; TravelPlanner gives 4.4 to 20.6 but not equal-token.)
3. How often does a model mistranslate a constraint, and does back-translation catch it? Wrong-constraint rates range from about 3 percent (templated SAT) to 95 percent (small scheduling audit). (Gap 3.)
4. At what constraint count does a solver tool stop paying for its overhead? No threshold has been measured. (Gap 4.)
5. Does dynamic backtracking help an LLM agent? (Gap 5, no study.)
6. Does smallest-domain-first help as an in-context rule? (Gap 6, no study.)
7. Can a model reliably say "unsatisfiable"? Some can (R1 83.6), the average cannot (39.3). Which prompt or check closes the gap? (Gap 7.)
8. Is GenCP replicated by an independent group? (Gap 8, none found.)
9. Does Dechter's width or tree decomposition give a usable ordering rule for natural-language constraint lists? Not searched. (Gap 10.)
10. Why does effort plateau on hard CSPs (hidden tokens flat above about 30 conflicts)? A budget rule, or lost persistence?
11. Does the 15-of-24 formalizer deficit disappear with solver feedback and a translation check?
12. Do diffusion language models propagate by filling certain cells first (c27 snippet)? Not verified.
13. The ZebraLogic X-Large threshold is stated as over 10^10 in one place and over 10^9 in another. Cite as about 10^9 to 10^10.

## 11. Sources

[V] = opened and read (full text or enough pages to extract numbers). [M] = snippet, abstract or citation only.

**Classical**
- [V] Mackworth (1977) Consistency in networks of relations. https://www.cs.ubc.ca/~mack/Publications/AI77.pdf (a01, a02, a03)
- [V] Mackworth and Freuder (1982) The complexity of some polynomial network consistency algorithms, UBC TR 82-06. https://www.cs.ubc.ca/sites/default/files/tr/1982/TR-82-06.pdf (a04, a05)
- [V] Seidel (1983) On the complexity of achieving k-consistency, TR 83-04. https://www.cs.ubc.ca/sites/default/files/tr/1983/TR-83-04.pdf (a06)
- [V] van Beek (1994) On the inherent level of local consistency in constraint networks (also the source for Freuder 1982). https://cs.uwaterloo.ca/~vanbeek/Publications/aaai94.pdf (a07, a08)
- [V] Zhang and Yap (2001) Making AC-3 an optimal algorithm. https://www.ijcai.org/proceedings/2001/0045.pdf (a09, a26)
- [V] Mackworth, Mulder and Havens (1985) Hierarchical arc consistency. https://www.cs.ubc.ca/~mack/Publications/CI85Alan.pdf (a10)
- [V] Ginsberg (1993) Dynamic backtracking. https://arxiv.org/pdf/cs/9308101 (a11)
- [V] Grant (1997) thesis, which summarises Cheeseman 1991, Mitchell 1992, Smith and Dyer, Prosser 1996, Grant and Smith 1996, Smith and Grant 1997, Gent and Walsh 1994. http://etheses.whiterose.ac.uk/1273/1/grant.pdf (a12 to a17)
- [M] Xu and Li (2000) Exact phase transitions in random CSPs. https://www.jair.org/index.php/jair/article/view/10251 (a18; abstract only)
- [M] Cheeseman, Kanefsky and Taylor (1991) Where the really hard problems are. https://www.ijcai.org/Proceedings/91-1/Papers/052.pdf (b26; not opened)
- [M] Dechter (2003) Constraint Processing. https://www.sciencedirect.com/book/9781558608900/constraint-processing (b25, c24; not opened)

**LLM and AI**
- [V] Lin et al. (2025) ZebraLogic, ICML. https://arxiv.org/abs/2502.01100 (a19 to a21, b01 to b04, c01, c02, d19; c01's model mapping is wrong)
- [V] Chen et al. (2025) LR2Bench. https://arxiv.org/abs/2502.17848 (a22, a23, b05, b06, d05)
- [V] Amonkar et al. (2026) A Reality Check of Language Models as Formalizers on Constraint Satisfaction Problems. https://arxiv.org/abs/2505.13252 (b07 to b09, c03 to c05, d03, d04)
- [V] He and Wang (2025) When Do Symbolic Solvers Enhance Reasoning in LLMs? https://arxiv.org/abs/2512.03272 (b10, b11)
- [V] Hazra et al. (2024) Can LLMs Reason? A Characterization via 3-SAT. https://arxiv.org/abs/2408.07215 (b12, b13)
- [V] Michailidis, Tsouros, Guns (2026) CP-Bench / DCP-Bench-Open. https://arxiv.org/abs/2506.06052 (b14 to b16, c18)
- [V] Szeider (2026) CP-Agent. https://arxiv.org/abs/2508.07468 (b17, b18, d01, d02)
- [V] Abdin et al. (2024) KITAB. https://arxiv.org/abs/2310.15511 (b19, b20)
- [V] Seely et al. (2025) Sudoku-Bench. https://arxiv.org/abs/2505.16135 (b21, b22, c06, c07)
- [V] Kaesberg et al. (2025) SPaRC. https://arxiv.org/abs/2505.16686 (b23)
- [V] Bonlarron, Regin, De Maria, Regin (2025) LLM meets constraint propagation. https://arxiv.org/abs/2505.24012 (a24, a25, b24, c14; d20 is the unopened replication check)
- [V] Regin, De Maria, Bonlarron (2024) Combining CP reasoning with LLM predictions. https://arxiv.org/abs/2407.13490 (c13)
- [V] Stechly, Marquez, Kambhampati (2023) GPT-4 doesn't know it's wrong. https://arxiv.org/abs/2310.12397 (c08)
- [V] Stechly, Valmeekam, Kambhampati (2024) Self-verification limitations. https://arxiv.org/abs/2402.08115 (c09)
- [V] Ye et al. (2023) SatLM. https://arxiv.org/abs/2305.09656 (c10, c11)
- [V] Yao et al. (2023) Tree of Thoughts. https://arxiv.org/abs/2305.10601 (c12)
- [V] Voboril, Peruvemba Ramaswamy, Szeider (2025) Streamlining constraints with LLMs. https://arxiv.org/abs/2408.10268 (c15)
- [V] Szeider (2025) MCP-Solver. https://arxiv.org/abs/2501.00539 (c16)
- [V] Shi et al. (2025) ConstraintLLM. https://arxiv.org/abs/2510.05774 (c17)
- [V] Cai, Kadioglu, Dilkina (2025) GALA. https://arxiv.org/abs/2509.08970 (c19)
- [V] Wei et al. (2025) SATBench. https://arxiv.org/abs/2505.14615 (c20, d06 to d08)
- [V] Utsho et al. (2026) Complexity-induced limits on finite discrete tasks. https://arxiv.org/abs/2604.13371 (c21)
- [V] Srivastava et al. (2026) BeyondBench. https://arxiv.org/abs/2509.24210 (c22)
- [V] Stojanovski et al. (2025) Reasoning Gym. https://arxiv.org/abs/2505.24760 (c23)
- [V] Amrollahi, Lopez, Barrett (2026) Roundtrip verification for autoformalization. https://arxiv.org/abs/2604.25031 (d09)
- [V] Berman, Ray, McKeown (2026) Zebra puzzles with constraint-guided multi-agent solving. https://arxiv.org/abs/2407.03956 (d10)
- [V] Skaisgiris et al. (2026) From natural language to exact cover. https://arxiv.org/abs/2611.03641 (d11, d12)
- [V] Inverse Scaling in Test-Time Compute (TMLR 2025). https://arxiv.org/abs/2507.14417 (d13)
- [V] Giannoulis, Pantis, Tzamos (2026) Teaching transformers to solve combinatorial problems. https://arxiv.org/abs/2509.22023 (d14)
- [V] Qin et al. (2025) To backtrack or not to backtrack. https://arxiv.org/abs/2504.07052 (d15)
- [V] Wang et al. (2026) Formalize, don't optimize. https://arxiv.org/abs/2605.12421 (d16)
- [V] Gundawar et al. (2024) LLM-Modulo for TravelPlanner. https://arxiv.org/abs/2405.20625 (d17)
- [V] Kadioglu et al. (2026) Text2Zinc. https://arxiv.org/abs/2604.12955 (d18; abstract, intro and results summary only)
- [M] Hao et al. (2025) special-purpose planning formalisation, as cited by Amonkar. https://arxiv.org/abs/2505.13252 (c25)
- [M] Pan et al. (2023) Logic-LM, as cited by ConstraintLLM. https://arxiv.org/abs/2510.05774 (c26)
- [M] Diffusion vs autoregressive models on Sudoku. https://arxiv.org/pdf/2601.15593 (c27, snippet)
- [M] LogicPuzzleRL. https://arxiv.org/abs/2506.04821 (d21, search summary)
- [M] Bonlarron et al. IJCAI 2025 replication search (d20; no follow-up found)

Links to other subfields in this run (not covered here): Forward and backward reasoning; Search theory; Efficient diagnosis algorithms; Autoformalisation; Probabilistic programming; Design-space exploration; Computational design; Reward prediction error learning; RL on verifiable rewards; Hybrid and connectionist (CLARION, Sigma).
