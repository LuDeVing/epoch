# Heuristic design by relaxation: deep document

*Subfield C05.02. Written 2026-10-26 from `evidence_a.jsonl` to `evidence_d.jsonl` (a01-a29, b01-b27, c01-c25, d01-d16), `claims.jsonl` (C05.02-K01 to K31) and `critique.md`. Evidence ids are cited in brackets. Claim ids are written K01 to K31. Status marks follow SCHEMA.md: [E] established, [S] single-source, [C] contested.*

Related subfields researched in parallel (links only, not covered here): Resource-rational analysis and rational strategy selection; Anytime search and restarts; Bandits and Thompson sampling for operator selection; Library learning; Analogical access; Schema induction; Conflict-driven clause learning (no-goods); Lemma discovery and conjecturing; Proofs and refutations; Chess thought process and progressive deepening; Chunking and template theory. Earlier deep documents in the series are listed in `00_FIELDS.md`.

---

## 1. What it is

A heuristic is a cheap guess of how far a state is from the goal. Pearl's idea (1984) is that a good heuristic is the exact cost of an easier version of the problem. You make the problem easier by removing a constraint. You solve the easy version. Its cost is your estimate for the real problem [a26, known only through citations]. The estimate is then used to rank the next moves of a search.

Four families of relaxation exist in classical planning [a16, c21]:

1. **Delete relaxation.** Pretend no action ever undoes anything. Facts only pile up. Used by HSP, FF, Fast Downward's FF heuristic, LAMA.
2. **Critical paths (h^m).** Pretend a goal set costs the same as its hardest subset of size m.
3. **Abstraction.** Project the problem onto a few variables, solve that exactly, store the answer. Pattern databases and merge-and-shrink are examples.
4. **Landmarks.** Find facts every solution must pass through. Use them as forced subgoals.

Two uses need two standards.

- **Ranking for greedy search.** A rough score is enough. It may over- or under-estimate. FF's score is of this kind [a07].
- **Proving a bound for optimal search.** The score must never overestimate (it must be admissible). LM-cut and pattern databases are of this kind [a14, a16].

For our agent the nearest operator is O4, "drop a constraint". The question for this subfield is: can the agent drop a constraint, solve the easy version, and use that result to rank or filter the real candidates, and does this beat other ways to spend the same tokens?

The honest answer from the literature is split in two:

- **Classical planning** has strong, replicated, measured evidence that relaxation scores work, and a clear map of where they fail.
- **Language-model reasoning** has no opened paper that tests the exact pattern (the model makes its own relaxed version, solves it, uses it to rank real children) [b27, K22]. What exists is neighbouring work: models that write the scoring function as code, models that abstract first (step-back), models that decompose (least-to-most), and models that propose landmarks that code verifies.

---

## 2. History and theories in depth

### 2.1 Origin: Pearl, Culberson and Schaeffer, Korf

Pearl (1984) states the thesis that admissible heuristics come from relaxed problems [a26]. We did not open the book. We know it only through the FF and Helmert papers.

Culberson and Schaeffer introduced pattern databases on the Fifteen Puzzle (1996, 1998). The PDF could not be opened [a27].

Korf (1997) made it famous with Rubik's Cube [a14, a15, b09, c22]:

- The state space has 4.3252e19 states.
- Three tables store exact solution lengths for projections: one for the 8 corner cubies (42 MB), two for 6 edge cubies each (20 MB each). Total 82 MB, built in about 1 hour.
- Each table is an admissible lower bound. The max of the three is admissible too. Its expected value is 8.878 moves (corner table alone 8.764; edge Manhattan distance only 5.5).
- Search is IDA*. Ten random cubes were solved optimally. One needed 16 moves, three 17, six 18. Median 18.
- Depth 16 costs about 9.5 billion nodes (under 4 hours). Depth 17 costs about 122 billion nodes (about 2 days). Speed was 700,000 nodes per second from memory. Computing the heuristic on the fly would be about 7000 times slower.
- Korf's hypothesis: search time is about n/m (state-space size over memory). He calls this an observation, not a theorem.

The lesson: solve a simplified slice exactly, once, and reuse it. The price is memory and precompute time, and a human chose the abstraction.

### 2.2 Delete relaxation: HSP, FF, Metric-FF

HSP (Bonet, Loerincs, Geffner 1997; Bonet and Geffner 2001) was the first successful domain-independent planner built on the delete relaxation [a28, not opened]. A search summary says McDermott (1996) had the idea independently.

**FF** (Hoffmann and Nebel 2001) [a01-a07, b01-b03, c19]:

- Builds a Graphplan-style planning graph on the delete-relaxed task and extracts one relaxed plan. Its length is the estimate.
- Unlike HSP, it counts a step shared by several goals once. HSP adds per-fact costs and double counts. Gripper example: with n balls left in room A, HSP rates "pick up another ball" 4n-2 and "move to room B" 3n+1. With 4 or more balls left HSP prefers moving, which is wrong. FF prefers picking up [a02].
- Finding a relaxed plan takes polynomial time. Finding the shortest relaxed plan is NP-hard. Even ordering actions inside one layer optimally is NP-complete [a07]. So FF is not admissible and is used only for greedy search. The authors note greedy search works best when estimates are cautious (low).
- **Helpful actions:** keep only applicable actions that add a fact the relaxed plan needs at its first step. Fraction kept: 40% down to 5% as tasks grow. Schedule, size 50: 7,663 helpful successors of 523,030 over 637 states (about 2%). Miconic-ADL: about 15% on average [a04, b03].
- **Enforced hill-climbing (EHC):** from the current state, run breadth-first search until a state with a strictly better estimate appears, then commit. Depth 1 almost always, depth 2 sometimes, depth 3 very rarely, whatever the task size [a05]. With an optimal relaxed oracle in Logistics the distance to a better state is at most d+1.
- FF won the AIPS-2000 fully automatic track. It was "extremely competitive" in 16 of 20 domains, only "satisfying" on both Blocksworlds, Mprime and Mystery [b01].

**Metric-FF** (Hoffmann 2003) extended the idea to numeric variables [a08, c24]. It only works if the task is monotonic (higher values always better), or linear and rewritten into that form. Lesson: a relaxation has a validity condition, and "dropping constraints" does not always simplify a task.

### 2.3 Why delete relaxation works: Hoffmann 2005

Hoffmann (2005) gave the formal account [a09-a11, b04, b05, c20]. Under the ideal h+ (length of an optimal relaxed plan) he sorted 30 benchmark domains by landscape shape:

- 24 of 30 have no unrecognised dead ends.
- Of those 24, 17 have a constant bound on escape distance from local minima (13 have no local minima at all).
- Of those 17, 12 have a constant bound on escape from plateaus (bound 1 in 6 domains). In those 12, FF's search with h+ is a polynomial solver.
- 6 of 30 have unrecognised dead ends.

He then checked the practical hFF against h+ by sampling 100 states per instance by random walks (length 0 to 2 times FF's plan length), computing exit distance by breadth-first search, and testing whether each sampled state lies on a valley. In 11 domains with no local minima under h+, 230 instance groups: 220 groups had no valley states, 8 groups below 1.0%, one group 2.2%, one group 5.0%. The exceptions were Grid and Hanoi (Hanoi 96 to 100% of states on valleys at larger sizes). Only one sampled state exceeded a proven bound (exit distance 2, not 1, in Logistics).

The key logical fact [a11]: hFF and h+ have the same dead-end behaviour. A state with no relaxed plan has no real plan. The danger is the reverse: states that have a relaxed plan but no real plan. Example: a rover takes a soil sample once and then cannot reach the lander. The relaxation never uses the sample up. So a relaxed check is a one-way test. Failing proves the real task impossible. Passing proves nothing.

### 2.4 Fast Downward, LAMA, landmarks

**Fast Downward** (Helmert 2006) [a12, a13, b10, c23]:

- Uses the causal graph heuristic (decompose by variable dependencies, ignore cycles) plus the FF heuristic.
- Adds preferred operators (FF's helpful actions inside best-first search), deferred evaluation and multi-heuristic best-first search.
- 550 STRIPS tasks from IPC 1-3, 300 s limit. Unsolved: FF 32, LPG 101, original causal-graph planner 25, six Fast Downward configurations 21 to 32 (focused iterative broadening 148). Best-of-six: all but 10 of 550.
- Multi-heuristic with preferred operators (M+P) was the best configuration: no other configuration solved more in 23 of 29 domains. Preferred operators helped in 10 domains and hurt in 5 (greedy search); helped in 15 and hurt in 2 (multi-heuristic).
- Won the IPC-4 non-optimizing track. Weak: Pipesworld, Promela-OpticalTelegraph, Schedule, Depot, Freecell.
- Monotonic progress is why the relaxed task is easy: in the multi-valued form a variable's set of reachable values only grows [a13].

**Landmarks** (Hoffmann, Porteous, Sebastia 2004) are facts true at some point in every plan, with orderings between them. The paper was not read [a29]. **LAMA** (Richter and Westphal 2010) [b11] combines landmark counts with the FF heuristic. It won the IPC 2008 sequential satisficing track. Landmark-only configurations: IPC score 164 to 167 and coverage 185 to 189; configurations that also use FF/add: score above 194 and coverage above 223. Landmarks plus iterated weighted A* added 2 score points on first solutions and 9 on final ones. Cost-sensitive estimates did not pay off (cost-unaware search was at least about equal).

### 2.5 Comparing the families: Helmert and Domshlak 2009

[a16, a17, b06, b07, c21]

- Dominance (admissible heuristics): additive h^m with m>=2 and merge-and-shrink strictly dominate landmark heuristics and additive hmax. Pattern databases are incomparable with both. Dominance in value is not dominance in runtime, because cost per node differs.
- New heuristic **LM-cut**: an admissible approximation of h+ built by repeatedly finding landmark cuts. It gave the perfect h+ value on at least 72% of tasks. Mean error of h_LA was 1.94, about 7 times that of LM-cut; relative error 3.8 times higher.
- Optimal-planning test, 22 domains: A* with LM-cut solved 450, landmark h_LA 422, Gamer 312 (the table total reads 321; the paper is inconsistent, ranking unchanged) [critique]. Other totals: merge-and-shrink 314, hmax 294, blind 273. LM-cut was a top performer in 16 of 22 domains. Exceptions: Gripper, FreeCell, Openstacks (hmax best because cheapest per node).
- LM-cut re-computes at every state. That is why it beats h_LA even where both estimate h+ perfectly at the start. Blocks: 43 to 48 times fewer expansions on the two largest common tasks.

### 2.6 The limit: Helmert and Roger 2008

"How Good is Almost Perfect?" [b08] proves that even a heuristic with error bounded by a small constant leaves exponentially many expansions for A* in Gripper and Miconic, which are easy for a polynomial solver. The authors write that improving a heuristic search algorithm by refining its estimates is "basically fruitless". The result is for optimal A*, not for satisficing greedy search.

### 2.7 The LLM turn (2023 to 2026)

Four lines of work:

1. **LLM as planner.** Weak without a sound checker (PlanBench and follow-ups).
2. **LLM writes the heuristic as code.** Correa et al. 2025 and its relatives. Strong.
3. **LLM proposes, relaxation verifies.** LM-Landmarks, LeanPlan, property-guided synthesis.
4. **Prompt-level abstraction or decomposition.** Step-back, least-to-most. Not relaxation, but the closest prompt patterns.

---

## 3. Core findings with exact numbers

Status uses the claim's status in `claims.jsonl`. Where a number was corrected in the critique, the corrected number is used.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Delete relaxation guides greedy planners well | FF won AIPS-2000; Fast Downward won IPC-4; LAMA won IPC 2008; 24 of 30 domains have no unrecognised dead ends under h+ | Hoffmann and Nebel 2001; Helmert 2006; Richter and Westphal 2010; Hoffmann 2005 [a01, a03, a09, a12, b11] (K01) | [E] |
| Relaxed score is blind to the dropped constraint | FF fails on Mystery and Mprime; Unpop solved 4 Mystery and 3 Mprime tasks FF did not; random restarts did not help; 6 of 30 domains have unrecognised dead ends | Hoffmann and Nebel 2001; Hoffmann 2005 [b02, a11, b04] (K02) | [E] |
| Dead-end test is the largest single gain when added to a generated scorer | Spanner: LeanPlan 72 vs SCP 30 (derived from printed sums); interaction-blind scorer lost to SCP in 4 of 10 IPC 2023 domains | Pereira et al. 2026 LeanPlan [d01, d02] (K02) | [E] with the above, 2026 preprint |
| Relaxed solution gives a free shortlist | FF keeps 40% down to 2% of successors; EHC with helpful actions faster in 16 of 20 domains, slower in 1 (Fridge); Fast Downward preferred operators helped in 10 / hurt in 5 (greedy), helped 15 / hurt 2 (multi-heuristic) | FF; Fast Downward [a03, a04, b10] (K03) | [E] |
| Most of FF's speed is the pruning and search rule, not the score | FF vs HSP distances better significantly in 8 to 10 domains per setting, worse in 5 cases overall | Hoffmann and Nebel 2001 [a03] | [E] (inside K01, K03) |
| Relaxation is weak where goal order matters | FF's Blocksworld results came mainly from goal ordering; plan lengths 83% to 108% of System-R (mean 96%); FF left 4 of 35 Blocksworld tasks unsolved in the Fast Downward comparison | FF; Fast Downward [a06, a13] (K04) | [E] |
| Combining estimates beats one | Multi-heuristic best in 23 of 29 domains; Tuisov SP-10 276 vs first compile 207 to 234 | Helmert 2006; Tuisov et al. [b10, a20, c04] (K05) | [E] |
| ... but more models add nothing once the best is chosen | HTN: 5-model virtual best 131 = best single model 131 of 139 | Meneguzzi et al. 2026 [d03] (K05, K27) | [S] |
| Landmark counts alone are not competitive | Landmark-only IPC score 164 to 167 vs above 194 combined | Richter and Westphal 2010 [b11] (K06) | [S] |
| Better relaxation accuracy solves more optimal tasks, up to a wall | LM-cut 450, h_LA 422, merge-and-shrink 314, hmax 294, blind 273; almost perfect heuristic still exponential in Gripper, Miconic | Helmert and Domshlak 2009; Helmert and Roger 2008 [a17, b08] (K07) | [C] |
| Pattern databases give exact bounds at memory cost | Rubik's Cube 42 MB corner, 82 MB total; 10 random cubes solved, median 18 | Korf 1997 [a14, b09] (K08) | [S] |
| Writing the heuristic as code beats asking for the plan | R1 174 end-to-end vs 373 with heuristic (720 tasks); Flash 19 vs 296; Thinking 202 vs 305; V3 48 vs 343; hFF 243 (table; prose says 234) | Correa et al. 2025 [a18, a20, b17, c25] (K09) | [E] |
| Same recipe works with code interface, other models | GPT-4.1 SP-10: 276 of 400; 207 first compile; 245 retry | Tuisov et al. [b20, c04] (K09) | [E] |
| Code scorer is cheaper than model plans in tokens/money | V3 $0.25 and R1 $6.12 for all heuristics vs $2.79 and $13.62 end-to-end; 200 vs 720 calls | Correa et al. [d13] (K09) | [E] (CPU selection cost excluded) |
| LLM heuristics beat C++ relaxation heuristics (in Python) | Fast Downward totals: hFF 295, hadd 324, hcg 318, learned 371; Pyperplan with R1 373, V3 343. Floortile is the one domain not won | Correa et al. [a19, b18] (K09) | [E] |
| Write search code once instead of judging every state | 24 game: 1362 of 1362 solved, about 1.2 interactions for successor and 1 for goal test; Tree of Thoughts about 75% on 100 problems with about 100 calls | Katz et al. 2024/2026 [a22, b21] (K10) | [E] |
| Example heuristics in the prompt are essential | No examples: coverage 0 for all samples; original prompt best 423; ablations best 359 to 404 | Correa et al. [a21, b19, c02] (K11) | [S] |
| Selecting a heuristic on training tasks is lossy | Best of 25 on test set 423 vs selected 305 (423/305 = +38.7%); mean 267.0, SD 94.3; 64 of 200 failed | Correa et al. (corrected in critique) [a21, c02] (K12) | [S] |
| Property check with counterexample repair beats sample-and-select | 623.3 vs 573 of 900 (hill climbing vs GBFS); sample-and-select under hill climbing 430; FF under hill climbing 30; 3.4 vs 25 generations; 10.75 min vs 206.25 CPU-hours per domain | Pereira et al. 2026 property-guided [d06] (K12, K26) | [S] |
| Part of the gain is vocabulary recall; on new domains it shrinks to parity | Obfuscated Blocksworld R1 66 to 40 (hFF 27 to 28); Rod-Rings o3 58 vs hFF 59 | Correa et al. [c03, b18, d14] (K13) | [S] for renaming |
| LLM heuristics stay competitive on never-released domains | LeanPlan 67 vs SCP 51 vs LM-cut 11 (3 new domains); Gestrin and Seipp 368 vs 352 of 720 (8 held-out domains); Rod-Rings 58 vs 59 | [d01, d05, d14] (K25) | [E] (three papers, different setups) |
| Models as direct planners are weak | GPT-4 Blocksworld 206/600 (34.3%); Mystery 2 to 4.3%; o1-preview 97.8% falls to 52.8% (Mystery) and 23.63% (20 to 40 steps, 110 instances); GPT-4o with PDDL prompts 194 of 260 vs GBFS+hFF 260, A*+LM-cut 240 | Valmeekam et al.; Stein et al. [b12, b13, b14, c11] (K14) | [E] |
| Lenient relaxed grading does not rescue model plans | Even with delete- and precondition-relaxed grading, GPT-4 still fails many; figure only, a snippet says about 39% | PlanBench appendix [b13, c09, c10] | [S], figure-only |
| LLM self-verification is unreliable | 100 Blocksworld instances: generator alone 40, LLM+LLM verifier 55, LLM+VAL 88; LLM verifier called 38 of 45 wrong plans valid (false-positive rate 84.45%) | Valmeekam et al. 2023 [b15] (K15) | [S] |
| Worked-example prompts do not generalise past the examples | Gains only for the most specific prompts; decay as block count grows | Stechly et al. 2024 [b16] (K16) | [S] |
| Step-back helps weaker models, little for strong | PaLM-2L Physics 66.4 to 73.2, Chemistry 70.9 to 81.8, TimeQA 41.5 to 66.0 (68.7 with RAG), StrategyQA 82.8 to 82.7; GPT-4+CoT 82.9 vs 84.5; fixes 20.5% of baseline errors, adds 11.9% new | Zheng et al. 2023 [a23, a24, b23, c16] (K17) | [S] |
| Least-to-most beats chain-of-thought on length generalisation | SCAN 99.7% vs 16.2%; last-letter list 12: 74.0% vs 38.4%; GSM8K 60.97 to 62.39 | Zhou et al. 2022 [a25, b24, c17] (K18) | [C] |
| Unverified dropping can lose solvability | LLM-pruned grounding solved 139 of 175 vs 161 for full grounding; 36 of 175 reformulated tasks gave no valid plan for the original | Canonaco et al. 2026 [c14] (K19) | [S] |
| LLM proposals checked by a delete-relaxation test | Coverage +7.5 points over FF, +3.1 over LAMA; nodes down 41% and 37% (abstract only; no unverified arm) | Bukkapatnam and Karuturi 2026 [c13, d15] (K20) | [S], unverified listing |
| Simplified versions pull to the memorised original | 97 unpuzzles: gap 9.1 points (o3) to 54 points (Gemini 1.5); context-shifted copy raised GPT-4o 33 to 52, Gemini 2.0 Flash 53 to 70, o3 75 to 80 (64 items) | Malek et al. 2025 [c18, d12] (K21) | [S] |
| No paper measures a model's own relaxed solve ranking real children | Nearest: h_add Spearman 0.931 with optimal plan length (N = 126, 164, 133); zero-shot routing 23% to 73%, with 140 calibration outcomes 99 to 100% | Debnath et al. 2026 [d07, d09, d10, b27] (K22, K28) | [S] |
| Plan code from models depends on checker feedback | GPT-4 Delivery 0.10 without debugging vs 0.90 with; Gripper 0.50 vs 0.90; Miconic 0.01 and Spanner 0.10 even with it | Silver et al. 2024 [c08] (K23) | [S] |
| EHC works because better states are shallow | 220 of 230 groups in 11 domains had no valley states; Hanoi restarts every time | Hoffmann and Nebel 2001; Hoffmann 2005 [a05, a10, b05] (K24) | [S] |
| Generated scorers often do not run | HTN: 361 of 780 rejected before testing; 72 of 419 deployed broke on every problem, 60 of 72 (83%) used the wrong state type; evolved C++: 79.1% first-try, 13.3% after one repair, 2.5% failed after 4 attempts | Meneguzzi et al.; Gestrin and Seipp [d04, d05] (K30) | [E] |
| Models rediscover known relaxations | Best evolved heuristic is FF with per-goal penalties min(hadd(g), hFF), 368 vs 352; reasoning effort raised working-program rate 73.0% to 83.4% (none to medium), not quality | Gestrin and Seipp 2026 [d05, d16] (K29) | [S] |
| Machine-checked guarantee with model-written scorers | LeanPlan 348 of 1170 (281 of 900 IPC 2023 vs 221 SCP); 3 of 1170 tasks refused by certificate | Pereira et al. 2026 [d01, d02] (K31) | [S] |
| Diverse starting points helped | 3 of 9 blind-seeded runs beat all FF-seeded runs; HTN median expansions 27x between best and worst model | Gestrin and Seipp; Meneguzzi et al. [d05, d03] (K27) | [S] |

---

## 4. Mechanisms and models

Each mechanism is explained so an engineer could build a text-problem analogue. Where the original lives in PDDL and our setting is text, the analogue is marked as untested.

### 4.1 Delete relaxation and the FF relaxed plan

Original:

1. Facts are propositions. An action has preconditions, add effects, delete effects.
2. Drop all delete effects. Now facts only accumulate.
3. Build a planning graph forward: layer 0 = initial facts. Add every action whose preconditions hold. Add its effects. Stop when all goals are present. If it never happens, the state is a proven dead end.
4. Extract backwards: for each goal, pick an action at the earliest layer that adds it. Its preconditions become subgoals. Count each chosen action once.
5. Estimate = number of chosen actions.

Why it is cheap: the relaxed task is monotone. Polynomial time to find some relaxed plan. Optimal relaxed plans are NP-hard, so FF takes a non-optimal one [a07].

Text analogue (untested): for a candidate answer, list the conditions it needs. Drop the conditions that "undo" earlier work (a resource is used up, a choice closes off another). Count what remains to be established. Code, not the model, does the counting.

### 4.2 Helpful actions / preferred operators

Original: compute the relaxed plan from the current state. Take the actions applicable now whose add-effects the relaxed plan needs at layer 1. Expand only those. If search fails, fall back to the full set [a04].

Fast Downward variant: keep both queues, one with all successors and one with preferred successors, and alternate [b10, a12].

Text analogue (untested): the first one or two steps of a relaxed solve define which branches to expand in S3. Fall back to all branches when the filtered search yields no pass (G6, never stall). The 2% to 40% pruning ratio was measured in planning only.

### 4.3 Enforced hill-climbing

Original: from state s with estimate h(s), breadth-first search the successors until a state with h < h(s) appears. Jump to it. Repeat. If a dead end is found, restart with complete search [a05].

Engineering rule: commit on the first strictly better child. Widen only when no better child appears within 2 steps. In planning, depth 1 nearly always works. Failing to find a better child within 2 steps is therefore a strong signal that the score is wrong here (Hanoi shows the pattern). This maps to an impasse trigger (K24, [S]).

### 4.4 Pattern databases and abstraction

Original [a14]:

1. Pick a subset of variables (the pattern). Project the problem onto it.
2. Run backward breadth-first search from the abstract goal. Store the exact distance for every abstract state in a table (4 bits per entry for Korf's corners).
3. At search time, look up the abstract state of the current state. That is the heuristic.
4. Several patterns: take the max (admissible) or sum if the patterns are disjoint and costs are split (additive).

Rule from Korf: bigger tables give higher values and faster search, until the search cost stops falling. Charge the build cost.

Text analogue: keep a library of solved sub-cases keyed by a signature (see the Library learning subfield). Lookup replaces a re-solve. This is not an LLM operator; it is a memory item.

### 4.5 Landmarks as forced subgoals

A landmark is a fact true at some point in every plan. A landmark count heuristic counts landmarks not yet achieved. Orderings between landmarks give a chain of subgoals [a29, b11].

Verification by delete relaxation (LM-Landmarks design) [c13]: to test if fact f is a landmark, remove every action that adds f, then check whether the goal is still reachable in the delete-relaxed task. If not, f is a landmark. Relaxation can prove "not reachable" soundly, so the test is sound.

Findings: landmarks alone are weak; combined with FF they help. Models are poor at proposing landmark orderings (scores 0.52 to 0.69 where 0.50 is chance, two of four domains not clearly above chance) [c12].

Text analogue: model proposes "this must hold in any correct answer". Code tests by removing every way to achieve it and checking the rest is impossible, where the problem is executable. Unverified in free text.

### 4.6 Recompute at each state (LM-cut)

LM-cut finds a cut of the relaxed task, adds its cost to the estimate, reduces the cut's action costs, and repeats until the goal is free. It recomputes at every state and so is more accurate than a landmark set computed once [b07]. For us: re-solve the easy version after each step; do not reuse the first estimate.

### 4.7 Code-as-heuristic loop (Correa et al.)

Original pipeline [a18, a20, a21, b17, b19, d13]:

1. Prompt: domain description (PDDL), a few example tasks, **example heuristics**, Pyperplan code (optional), instructions and a checklist.
2. Sample 25 candidate Python functions `h(state)` per domain.
3. Run each in greedy best-first search on a training set. Score by coverage.
4. Keep the best. Run on larger unseen tasks.

Facts: 8 IPC 2023 learning-track domains, 90 test tasks each (720). Test tasks are larger than training. Without example heuristics all candidates scored 0. Going from 1 to 5 samples gave the biggest jump. Only the distilled R1 Qwen 14B fell below hFF. Spread is large (SD 94.3). Selection by training score picked a 305-coverage heuristic where the best of the pool had 423.

Failure accounting [d04, d05]: smoke-test every candidate on one tiny instance. In HTN 361 of 780 were rejected this way, and most deployed failures were one bug (wrong state type).

### 4.8 Property-guided synthesis

Original [d06]:

1. State a property a good scorer must satisfy and that code can check on training data: every state reached by improving moves has an improving successor.
2. Run the check. On the first violation, give the model the counterexample and ask for a repair.
3. Stop when the property holds on all training instances. Average 3.4 generations per run (SD 3.0), vs 25 fixed.

Result: 623.3 vs 573 of 900, and 10.75 minutes vs 206.25 CPU-hours per domain. The property can still fail on test tasks.

### 4.9 Certificates for a scorer (LeanPlan)

Original [d01, d02]: the agent writes the heuristic and a Lean 4 proof that it never overestimates. Machine checking replaces trust. Domain assumptions are checked per task. If they fail, the certificate refuses (3 of 1170 tasks, all Cisterns). Acceptance rule: solves at least as many training tasks as Scorpion and expands fewer states. Needs a formal domain.

### 4.10 Code once, search after (Thought of Search)

Original [a22, b21]: the model writes `successors(state)` and `is_goal(state)` once. A plain BFS or DFS finishes. 24 game: 1362 of 1362. The survey note [d10]: model-given h-values are fitted or prompted, not derived by relaxation, so admissibility and consistency do not apply; a comparative rating among siblings gives order only, valid inside one parent's set.

### 4.11 Step-back and least-to-most

Step-back [a23]: ask the model for the higher-level principle first, then reason from it. 1 exemplar was enough; more did not help. It is abstraction, not relaxation. The abstract step rarely fails; the concrete reasoning that follows does (over 90% of remaining physics errors are reasoning errors) [a24].

Least-to-most [a25]: stage 1, decompose into easier sub-questions. Stage 2, answer them in order, each feeding the next. Needs exemplars shaped like the task (14 for SCAN). Almost every failure on SCAN could be fixed with a hand-written decomposition, so the model's own decomposition is the weak point.

### 4.12 Calibrating a relaxed rank

[d07, d09]: h_add ranks held-out instances by optimal plan length at Spearman 0.931. But a rank that orders difficulty does not tell you which instances a model will solve. A threshold fitted on 140 real outcomes routed 99 to 100% correctly; zero-shot routing was 23% to 73%. Mechanism: log the pair (relaxed score, real result) per problem class and refit the threshold. Do not trust an uncalibrated relaxed rank.

---

## 5. What holds up

### 5.1 Replications and independent confirmations

- **LLM-written heuristics beat asking for the plan.** Correa et al. (3 model families) and Tuisov et al. (6 models, code interface in Rust, numeric and non-PDDL problems) agree. Gestrin and Seipp (open-weight models, C++ evolution), the HTN paper (nine models), and LeanPlan (coding agent, Lean proofs) add the same direction in other settings [a18, b20, d01, d03, d05]. These are all one research community with shared authors (Correa, Pereira, Seipp appear in four). Counted by lab, independence is lower than the paper count (critique: "many ids are the same paper read three times").
- **Delete relaxation as a good search guide.** FF, Fast Downward, LAMA and the Hoffmann topology study are consistent. Hoffmann 2001, 2003 and 2005 share an author and a framework.
- **Direct LLM planning is weak.** Valmeekam (three papers), Stein et al., Hirsch et al. agree [b12, b13, b14, c11, c12].
- **New domains.** Three papers with different models show parity or better than the best generic heuristic on never-released domains [d01, d05, d14].

### 5.2 Failures, boundary conditions, competing explanations

1. **Dead ends from the dropped constraint.** FF failed on Mystery and Mprime. Restarts did not help. The authors' explanation ("we think") was not tested [b02]. LeanPlan found the same pattern in LLM scorers: interaction-blind scorers lose in Sokoban (authors' wording: "presumably" because SCP captures box interactions) and a dead-end test gave the biggest gain in Spanner [d02].
2. **Order of goals.** Blocksworld needs goal-ordering tricks; the relaxed distance alone does not see that stacking one block buries another [a06].
3. **Accuracy is not enough.** More accurate relaxation (LM-cut) solves more optimal tasks [b07]. Helmert and Roger prove an almost perfect heuristic still leaves exponential search [b08]. Marked contested (K07). Regime difference: optimal A* vs satisficing greedy.
4. **Memory vs reasoning.** Obfuscated Blocksworld cut the R1 heuristic from 66 to 40 while hFF stayed at 27 to 28. On a never-released domain o3 reached 58 vs hFF 59, i.e. parity, not a win [c03, d14]. Gestrin and Seipp's best heuristic was an FF-style relaxation, which suggests recall of a known method (the authors say this is an inference, not a test) [d16].
5. **Weaker models.** Distilled R1 Qwen 14B was the only generator below hFF [a20]. Four of nine HTN models had a surviving candidate in only one domain each [d04].
6. **Selection leaks gains.** Best of 25 on the test set 423 vs selected 305. A cheap smallest-instance filter or a property check are partial fixes, not compared head-to-head on the same pool [d04, d06].
7. **Extra samples and extra models.** Going 1 to 5 samples gave the largest jump, then diminishing returns [a20]. HTN: five-model virtual best equalled the best single model [d03]. Diversity of seed helped evolution [d05].
8. **Per-instance detail hurts.** Showing GPT-4.1 the concrete instance lowered coverage (162, 222, 225 vs 207, 245, 247 on 360 tasks) [b20]. Authors guess a stronger model might use it.
9. **Unverified dropping loses solvability.** LLM-pruned grounding: 139 vs 161 of 175 [c14].
10. **Decomposition prompts do not generalise.** Worked-example gains fade as block count passes the example size [b16]. Least-to-most's SCAN win used hand-shaped exemplars [a25, c17].
11. **Simple version pulls to the famous one.** Unpuzzles [c18, d12].
12. **Step-back is not free.** It introduced new errors in 11.9% of cases while fixing 20.5% on MMLU physics [a23, c16].
13. **Search wall.** Helmert and Roger [b08].
14. **Cost.** The expensive part of code-as-heuristic is the CPU search used for selection (206.25 CPU-hours per domain), not tokens [d06, d13]. In a text setting with no executable instances, the model has to do the evaluation, and that cost lands in the token budget.

### 5.3 Moderators that matter

- **Model strength.** Step-back: large gains for PaLM-2L, small for GPT-4+CoT. Reasoning models gain more from heuristic-writing than non-reasoning ones in Correa; Tuisov found non-reasoning GPT-4.1 best once cost counted; Gestrin and Seipp found reasoning effort raised working-program rate (73.0% to 83.4%) but not quality.
- **Domain structure.** Reversible, non-interfering domains suit relaxation; one-way commitments (fuel, one-off samples) break it.
- **Prompt content.** Example heuristics were essential (0 without them) [a21].
- **Surface vocabulary.** Renaming costs 40% on Blocksworld heuristics and 67.5% to 40.0% on direct Qwen plans (N = 40, CI 52.0 to 79.9 vs 26.3 to 55.4) [c03, d08].
- **Search regime.** Greedy vs optimal changes what "better heuristic" is worth.

### 5.4 Interventions that worked / did not

| Worked | Did not work |
|---|---|
| Code scorer inside sound search (373 vs 174) | Model alone as planner (GPT-4 34.3% Blocksworld) |
| Sound checker on model output (LLM+VAL 88/100) | Model as its own verifier (55/100; 38 of 45 wrong plans passed) |
| Example heuristics in prompt | Instance-specific details in prompt (lower coverage with GPT-4.1) |
| Property check plus counterexample repair | Pick best of 25 by training score (305 vs 423 available) |
| Dead-end test added to scorer | Interaction-blind scorer (lost 4 of 10 IPC 2023 domains to SCP) |
| Two relaxations in one search (Fast Downward M+P) | Landmarks alone (score 164 to 167 vs above 194) |
| Verified landmarks (abstract claim) | Unverified pruning (139 vs 161) |
| Checker feedback on program (Delivery 0.10 to 0.90) | Cost-sensitive estimates in LAMA; more models in a portfolio on HTN |

---

## 6. Language models

### 6.1 As planners, directly

- GPT-3 Instruct Blocksworld 41/600 (6.8%). GPT-4 206/600 (34.3%) plan generation; cost-optimal 198/600 (33%); plan verification 191/600 (31.8%). Mystery (obfuscated) Blocksworld: GPT-4 26/600 (4.3%) in one setting, 12/600 (2%) in another [b13, c09]. Average autonomous success in the 2023 critical investigation about 3% [b12].
- o1-preview: Blocksworld 97.8%, Mystery 52.8%, Randomized Mystery 37.3%, 20 to 40 step instances 23.63% (110 instances). Unsolvable instances flagged correctly 27% (16% on randomized mystery). Cost $1897.55 for the o1 experiments. Fast Downward 100% [b14]. Best open model, Llama 3.1 405B, 62.6% zero-shot.
- GPT-4o choosing actions step by step from PDDL prompts: best 194 of 260. Random 13, BFS 258, A* with LM-cut 240, GBFS with hFF 260 [c11].
- Hirsch et al.: describing the next state, GPT-4 averaged 69%, Llama-3 39%; success falls on average 80% from 1 action to 7. Goal ordering (LAMA landmark orderings as items, chance 50%) scored about .52 to .69. SimPlan ablation: full .81, no state update .21, no augmentation .19 [c12].
- GPT-4 as its own plan verifier: 61% accuracy, 84.45% false-positive rate [b15].

What changed it: extra inference-time reasoning (o1) helped on small tasks and collapsed with obfuscation and length. A sound checker or sound search changed it most.

### 6.2 Writing the heuristic

- 720 tasks, Pyperplan GBFS: R1 373, V3 343, Flash Thinking 305, Flash 296, R1-distill 214, blind 120, hFF 243 [b17].
- End-to-end vs heuristic: R1 174 to 373, Thinking 202 to 305, Flash 19 to 296, V3 48 to 343 [a20, c25].
- Tuisov, 400 tasks, GPT-4.1: 234 first compile, 272 retry, 281 SelfPortfolio-10 with domain prompt (the 360-task set: 207, 245, 247). A post-hoc portfolio with the best classic heuristic reached 304 (authors call it unfair) [b20, c04, c05].
- LeanPlan, 1170 tasks: 348 vs SCP 272 vs LM-cut 209 [d01].
- HTN, 139 problems: Opus 4 heuristic 131, PANDA RCFF 134, LMCOUNT 118; fewer expansions than PANDA on 83% of shared problems; Robot domain LLM 12 vs PANDA 20 [d03].
- Gestrin and Seipp, 720 tasks: 368 vs hadd 352; API spend about $16 (none), $24 (low), $33 (medium) per run [d05].
- Cost: V3 $0.25 and R1 $6.12 for all heuristics in Correa.

What changed it: example heuristics in the prompt (0 without), 5 samples vs 1, domain description, a checkable property (d06), a dead-end test (d02), more reasoning effort only for the working-program rate.

### 6.3 Abstract-first and decompose-first prompts

- Step-back: see section 3. Gains 7 to 27 points on PaLM-2L, 0.3 to 1.6 over CoT on GPT-4. Llama2-70B physics 51.9 to 64.8. Over 90% of the remaining physics errors are in reasoning, TimeQA 45% from failing to retrieve [a24].
- Least-to-most: SCAN 99.7% (code-davinci-002), text-davinci-002 76.0%, code-davinci-001 60.7%. Last-letter list 12: 74.0% vs CoT 38.4%. GSM8K 60.97 to 62.39 [a25, b24]. Decomposition prompt hand-made for SCAN [c17].
- Tree of Thoughts (model rates states sure/maybe/impossible): Game of 24, GPT-4: IO 7.3%, CoT 4.0%, CoT-SC 9.0%, ToT breadth 1: 45%, breadth 5: 74%. Cost about 5.5 to 6.7k extra tokens per task. Crosswords 4 of 20 games. The evaluator pruned words in solved crosswords [b22]. Katz et al. beat it with code.

### 6.4 Model proposes, code verifies

- LM-Landmarks (abstract only): +7.5 over FF, +3.1 over LAMA, nodes down 41% and 37% [c13, d15].
- LeanPlan: proof-checked admissibility [d01].
- Semantic partial grounding (unverified drop): 139 vs 161 of 175, up to two orders of magnitude fewer operators, LAMA solved 10 tasks full grounding could not [c14].
- AutoCO (not text): SFL-8 success 52% to 80%; ablation: without relaxation module +21.55% optimality gap [c15, d11].

### 6.5 Memory pull

Unpuzzles: gap between puzzle and trivialised puzzle from 9.1 points (o3) to 54 points (Gemini 1.5). Table 1 examples: GPT-4o 75.3 vs 19.6; o3 87.6 vs 74.2. Context corruption in 80 of 97 solutions for Gemini 1.5 and 34 for Gemini 2.5 Pro. Re-contexted copies raised accuracy for every model [c18, d12].

### 6.6 What the language-model evidence does not show

All planning evidence is in classical benchmark domains (Blocksworld, Gripper, Logistics). None is on open-ended reasoning questions. Cost is not equal-token anywhere (critique). No paper measures the exact pattern we want (K22, [b27]; confirmed again in the gap search [d10]). The text-reasoning transfer is a hypothesis.

---

## 7. What our agent should take

Format: item; schema part; status; evidence ids. The 2026 preprints (d-series) are not yet replicated.

### Add now (established)

1. **A relaxed pass is never a pass.** A relaxed solve can prove a candidate impossible but cannot prove it works. Every candidate that survives a relaxed check goes through the full check (S4, G3). The dropped constraint is re-checked before S7. G3 / S4. [E] K02, K14. a11, b02, b04, d02.
2. **Code, not the model, checks relaxed and full plans.** The model does not certify a plan it wrote. G2, G3, G5. [E] K14. b12, b13, b14, c11. (The 55 vs 88 verifier result b15 is single-source but agrees with G10 and G5.)
3. **Where states are enumerable, move the rules into code once.** Successor function and goal test as code, then a plain search. Replaces per-state model judgement. G5 / O4. [E] K10. a22, b21, c06, b22.
4. **Where the model must score candidates, have it write the scoring function and let code apply it to all children.** Prefer this to rating children one by one. Applies where a scorer can be executed (code, arithmetic, checkable constraints). Text-only reasoning transfer is untested, see "Test first". G5 / O4. [E] K09 for executable problems. a18, a20, b17, b20, c04, c25, d01, d13.
5. **Smoke-test every model-written scorer or checker on one tiny instance before use.** Count discards and repairs in the token cost. G2 / G7. [E] K30. d04, d05.
6. **Test any relaxation on renamed or novel variants before crediting it.** Expect parity with the best generic method, not a large gain. G7. [E] K25 (the renaming part is [S], K13). d01, d05, d14, c03.
7. **State the validity condition of the relaxation.** Before using a dropped-constraint version, write down which dead ends it could hide, and that a real solution is also a solution of the relaxed one. O4. [E] by K02 and Metric-FF [a08, b26 is own summary]. Treat the written check as a log field, not a model judgement.
(Re-solving the easy version after each step, as LM-cut does [b07], is single-source and so belongs in "Test first", not here. See UNKNOWNS.md.)

### Test first

| # | Item | Schema part | Status | Evidence | Why test |
|---|---|---|---|---|---|
| T1 | **O4 relaxed solve ranks S3 children.** Drop a constraint, solve the easy version, use its result to order children before testing. | O4 / S3 | [S] (no direct measurement) | K22, b27, d07, d09, d10 | Central open test. Must be calibrated (log pairs). |
| T2 | **Enumerate constraints by code** (drop each stated constraint in turn) instead of letting the model pick one. | O4 / S3 | [S] | K22, c15, d11 | AutoCO shows model-set relaxation helps in numeric problems; no code-enumeration arm anywhere. |
| T3 | **Relaxed result as a shortlist** (helpful actions): expand only the branches the relaxed solve starts with, fall back to all. | O4 / S3 | [E] in planning, untested in text | K03, a04, b10 | 2% to 40% kept in planning. Text transfer unknown. |
| T4 | **Portfolio of 2 to 3 different relaxations.** Differ in kind, not in sample. | S3 / S7 | [E] in planning (K05), [S] against it (K27) | b10, a20, d03, d05 | G4: samples from one model correlate. |
| T5 | **Property check plus counterexample repair on the scorer.** One checkable property per scorer; stop on first violation. | G5 / S7 | [S] | K12, K26, d06, d04 | Replaces pick-by-training-score; needs a verifiable property. |
| T6 | **Dead-end and must-pass list beside every relaxed score.** | O4 / G3 | [S] | K29, d02, d16, K02 | Largest single gain in LeanPlan Spanner; also FF's Mystery failure. |
| T7 | **Worked example of a relaxation in the O4 prompt**, matched to the problem class. | S2 / O4 | [S] | K11, a21, K16, b16 | 0 without examples in planning; examples that are too close to test cases fade. |
| T8 | **Renamed-copy detector on each relaxed solve.** Solve the relaxed version in neutral wording as well; compare. | S1 / G3 | [S] | K21, K13, d12, d08, c03 | Detector, not proof. |
| T9 | **Verified landmark: model proposes a must-hold fact, code checks by relaxed reachability.** | O4 / G5 | [S] | K20, c13, d15 | Only an abstract exists; no unverified arm. |
| T10 | **Step-back as a signalled S1 step**, per model and class. Not credited as relaxation. | S1 / O6 | [S] | K17, a23, a24 | Gain depends on base model; 11.9% new errors. |
| T11 | **Commit on first strictly better child; widen after two steps without one (impasse signal).** | S5 / S6 | [S] | K24, a05, a10 | Depth-1 improvement was nearly always available in planning. |
| T12 | **Explicit goal-order check** where order matters, instead of a better relaxed score. | O4 / S7 | [E] in planning | K04, a06 | FF's Blocksworld wins came from goal ordering. |
| T13 | **Cheap scorer selection** (smallest-instance filter) instead of full-set selection. | G5 / S7 | [S] | K12, d04, d06 | The 305 vs 423 gap. |
| T14 | **Least-to-most with unshaped exemplars** | O3 | [C] | K18, a25, b16, c17 | Decomposition, not relaxation; test only because it is the usual easy-first prompt. |

Schema status effect: O4 remains [S]. This subfield adds a reason for each of the two failure modes (dead ends, recall) and a concrete calibration rule, but no new [E] element for text reasoning.

---

## 8. Concrete tests on our bench

All arms at equal total tokens. Setup, sampling, write, test and repair costs are charged to the arm that uses them (G7). Seeds and items are fixed across arms. Log the fields in SCHEMA section 6.

**Common item pools**

- *Constraint puzzles with a checker:* ARC-style grid tasks (held-out example check), BRAINTEASER-style items with code-checkable answers, small scheduling or assignment problems with 3 to 6 stated constraints.
- *Order-dependent items:* block-stacking or multi-step tasks where doing goals in the wrong order is irreversible.
- *Dead-end items:* tasks with a one-way commitment (a use-once resource) so a relaxed score is known to mislead. These are the Mystery/Rovers analogues.
- *Renamed copies:* every item above rewritten in neutral wording, with the same structure.

| # | Test | Item type | Arms (equal tokens) | Metric | Expected effect |
|---|---|---|---|---|---|
| E1 | Relaxed solve ranks children (T1) | Constraint puzzles, ARC, order-dependent items; 100+ items, 4 to 8 children per item | A: S3 children ranked by code-computed relaxed score; B: children ranked by model rating (no authorship, G5); C: children in random order, test all; D: plain model at same tokens | Per class: Spearman rank correlation of relaxed score vs real test result; top-1 pass rate at fixed token budget | Positive correlation on reversible classes, near zero on dead-end items. Win over C only if tokens saved on scoring are less than tokens saved on testing. Expect small gains. |
| E2 | Code enumeration of dropped constraint (T2) | Constraint puzzles with 3 to 6 stated constraints | A: code drops each constraint in turn, one relaxed solve each; B: model picks which constraint to drop; C: no relaxation | Pass rate on S4 at equal tokens; number of relaxed solves that were misleading | A beats B if constraint choice matters. Cost grows with number of constraints, so cap at 3. |
| E3 | Shortlist (T3) | Items with 6+ children | A: expand only children consistent with the first 1 to 2 steps of the relaxed solve; fall back to all if none passes; B: expand all; C: random subset of same size | Pass rate; tokens per pass | If relaxed solve is good, same pass rate at 20% to 60% fewer tokens. If not, a pass-rate drop that the fallback only partly recovers. |
| E4 | Scorer vs rating (K09 for text) | Items where a scorer can run (arithmetic, grid, schedule) | A: model writes one scorer (1 to 5 candidates, smoke-tested), code scores all children; B: model rates each child; C: model answers directly. Charge writing, smoke, repair, selection | Pass rate at equal tokens; share of scorers that fail the smoke test | A beats B on executable items, ties on non-executable. Smoke test discards a large share (HTN: 46% rejected). |
| E5 | Relaxation portfolio (T4) | Same as E1 | A: 1 relaxation; B: 2 or 3 relaxations of different kind (drop constraint, abstract slice, landmark); C: 2 or 3 samples of the same relaxation | Pass rate; agreement among relaxations vs correctness (G4) | B over A small; C over A near zero (correlated samples). |
| E6 | Property check on scorer (T5) | Executable items | A: scorer with one checkable property and counterexample repair; B: best-of-5 by pass rate on training items; C: single scorer | Pass rate on held-out items; tokens | A beats B at lower tokens if a property exists. |
| E7 | Must-pass list (T6) | Dead-end items | A: relaxed score plus explicit must-pass list for the dropped constraint; B: relaxed score only | Rate of high-relaxed-score children that fail the real test; pass rate | A removes most dead-end misses. |
| E8 | Worked relaxation example (T7) | Mixed classes | A: O4 prompt with an example of the same class; B: no example; C: example from another class | Pass rate; rate of invalid relaxed versions | A > B; C near B or worse (examples too far or too near). |
| E9 | Renamed copy (T8) | Original and renamed pairs | A: relaxed solve on original wording; B: on renamed; C: both, flag disagreement | Accuracy gap A to B; does the flag predict failures | Gap shows recall; the flag should predict real failures better than chance. |
| E10 | Verified vs unverified landmark (T9) | Executable items | A: model proposes must-hold facts, code verifies by relaxed reachability; B: unverified; C: none | Pass rate; number of wrong subgoals used | A removes wrong subgoals; B shows what verification buys. |
| E11 | Step-back on a signal (T10) | Knowledge and physics-style items | A: step-back only after a failed check; B: always; C: never | Pass rate; errors introduced | A matches B at lower tokens; the gain on strong models near 0 to 2 points. |
| E12 | Commit on first better child (T11) | Items with a score | A: commit on first strictly better child, widen after 2 steps without; B: score all children, take the best | Pass rate; tokens | A cheaper, same pass rate if the score is informative; failure to find a better child flags a bad score. |
| E13 | Goal-order check (T12) | Order-dependent items | A: explicit order check before ranking; B: relaxed ranking only | Pass rate | A > B. |
| E14 | Scorer selection rule (T13) | Executable items | A: smallest-instance filter; B: best-of-N by training pass rate; C: property check | Held-out pass rate vs oracle best-of-N | A and C recover part of the gap to oracle. |

---

## 9. What does not transfer, and why

- **Admissibility and optimality proofs.** They need a formal cost model and a state space. Free-text reasoning has neither. LeanPlan only works because the domain is formal [d01]. The Thought-of-Search survey notes that model-given h-values are not admissible by construction [d10].
- **Pattern databases.** Exact tables over a small state space (4.3e19 states for a cube, but a fixed structure). Our problems do not have a fixed projectable state space. The idea survives only as a library of solved sub-cases (see Library learning).
- **Delete relaxation as such.** "Nothing is undone" has a precise meaning for propositional actions. In text puzzles there is no action/delete structure. Only the pattern (drop what undoes things, solve the rest, treat failure as proof, treat success as a hint) carries over.
- **The headline numbers.** Coverage of 373 vs 174 is on PDDL domains with an executable search and a free CPU. It charges neither the 25 samples nor the training runs (206.25 CPU-hours per domain, d06). It is not equal-token.
- **Dead-end detection.** In PDDL, a state with no relaxed plan has no real plan, and this is code-checked. In text a model's belief that "this can't work" is not proof (G10).
- **Landmark verification by reachability.** Needs a reachability oracle. Only for executable problems.
- **Helpful actions.** The 2% to 40% pruning ratio is a property of planning graphs. For our children it depends on how the relaxed solve maps to branches.
- **Unpuzzle and renaming results.** They show the risk; they do not show that renaming fixes it.
- **Step-back and least-to-most.** Abstraction and decomposition, not relaxation. Step-back was measured on PaLM-2L and GPT-4 of 2023 [a23]. Least-to-most's number comes from a synthetic task with a hand-shaped decomposition.
- **AutoCO.** Numeric optimisation with a fitness function; text puzzles do not have a smooth feasible region to loosen.
- **Pearl's thesis for LLMs.** The model's solve of the relaxed version is itself fallible (Valmeekam: even a lenient, relaxed grading leaves many GPT-4 plans wrong) [b13]. In classical planning the relaxed solve is exact or sound. Here it is a model output and needs its own check.

---

## 10. Open questions

1. Does the rank of a model-made relaxed solve predict the real test result of the full candidate, per problem class, at equal tokens? (K22; the central gap.)
2. Does choosing the dropped constraint by code beat the model's choice? (AutoCO does not test it.)
3. How often does a relaxed solve give a high score to a child that fails because the dropped constraint was the one that mattered? Which of our classes are Mystery-like?
4. At equal tokens including write, test and 25-sample selection, does "model writes a scorer" beat "model rates children"?
5. How much of the LLM-heuristic gain survives renaming across more than R1 and Qwen 2.5-72B? (The renaming result rests on one R1 run and one Qwen run with N = 40.)
6. Can the helpful-actions idea cut tokens in S3 without lowering pass rate?
7. Does a portfolio of relaxations of different kinds help beyond one, given correlated samples?
8. What does verification buy over unverified proposals outside PDDL? (LM-Landmarks has no unverified arm and only an abstract.)
9. When does the easy version pull the model to a memorised answer, and is a renamed-copy check enough?
10. Is there a cheap rule for choosing among model-made scorers that beats training-set performance? (Two partial rules exist, not compared with each other on one pool.)
11. Do the 2026 preprints replicate? (HTN, LeanPlan, Gestrin and Seipp, property-guided synthesis were each read once and are not independently replicated.)
12. Does the dependence on model strength (step-back, reasoning effort) hold for the models we run?
13. Is there a text-reasoning analogue of h+ monotonicity that tells us ahead of time when relaxation will mislead? (Hoffmann's taxonomy exists for 30 PDDL domains only.)
14. Pearl 1984, Culberson and Schaeffer, Bonet and Geffner and Hoffmann et al. 2004 were not opened. Forward-citation search was incomplete (Semantic Scholar and OpenAlex were rate limited).

---

## 11. Sources

[V] = opened and read this session (PDF or HTML text). [M] = snippet, abstract only, or known through citations only.

**Classical planning and search**

- [V] Hoffmann and Nebel (2001) The FF Planning System: Fast Plan Generation Through Heuristic Search. JAIR 14. https://arxiv.org/pdf/1106.0675 (a01-a07, b01-b03, c19)
- [V] Hoffmann (2003) The Metric-FF Planning System. JAIR 20. https://arxiv.org/abs/1106.5271 (a08, c24)
- [V] Hoffmann (2005) Where "Ignoring Delete Lists" Works: Local Search Topology in Planning Benchmarks. JAIR 24. https://arxiv.org/pdf/1109.5713 (a09-a11, b04, b05, c20)
- [V] Helmert (2006) The Fast Downward Planning System. JAIR 26. https://arxiv.org/pdf/1109.6051 (a12, a13, b10; c23 abstract)
- [V] Korf (1997) Finding Optimal Solutions to Rubik's Cube Using Pattern Databases. AAAI-97. https://cdn.aaai.org/AAAI/1997/AAAI97-109.pdf (a14, a15, b09, c22)
- [V] Helmert and Domshlak (2009) Landmarks, Critical Paths and Abstractions: What's the Difference Anyway? ICAPS. https://ai.dmi.unibas.ch/papers/helmert-domshlak-icaps2009.pdf (a16, a17, b06, b07, c21)
- [V] Helmert and Roger (2008) How Good is Almost Perfect? AAAI 2008. https://ai.dmi.unibas.ch/papers/helmert-roeger-icaps2007ws.pdf (b08)
- [V] Richter and Westphal (2010) The LAMA Planner: Guiding Cost-Based Anytime Planning with Landmarks. JAIR 39. https://arxiv.org/pdf/1401.3839 (b11)
- [M] Pearl (1984) Heuristics: Intelligent Search Strategies for Computer Problem Solving. https://www.worldcat.org/title/10139532 (a26; known through citations)
- [M] Culberson and Schaeffer (1998) Pattern Databases. https://webdocs.cs.ualberta.ca/~jonathan/PREVIOUS/Papers/Papers/pdb.pdf (a27; fetch failed)
- [M] Bonet and Geffner (2001) Planning as Heuristic Search. https://doi.org/10.1016/S0004-3702(01)00108-4 (a28; known through FF and Metric-FF text)
- [M] Hoffmann, Porteous and Sebastia (2004) Ordered Landmarks in Planning. https://arxiv.org/abs/1107.0052 (a29; garbled text)

**Language models and planning**

- [V] Correa, Pereira, Seipp et al. (2025) Classical Planning with LLM-Generated Heuristics: Challenging the State of the Art with Python Code. NeurIPS 2025. https://arxiv.org/abs/2503.18809 and https://arxiv.org/pdf/2503.18809 (a18-a21, b17-b19, c01-c03, c25, d13, d14)
- [V] Tuisov, Vernik, Shleyfman (2025/2026) Successor-Generator Planning with LLM-generated Heuristics. https://arxiv.org/abs/2501.18784 and https://arxiv.org/pdf/2501.18784 (b20, c04, c05; some table cells unclear)
- [V] Katz, Kokel, Srinivas, Sohrabi (2024, v3 2026) Thought of Search. https://arxiv.org/abs/2404.11833 (a22, b21, c06)
- [V] Yao et al. (2023) Tree of Thoughts. NeurIPS 2023. https://arxiv.org/abs/2305.10601 (b22, c07)
- [V] Valmeekam et al. (2023) PlanBench. https://arxiv.org/abs/2206.10498 (b13, c09; relaxed results only in a figure)
- [V] Valmeekam et al. (2023) On the Planning Abilities of Large Language Models: A Critical Investigation. https://arxiv.org/pdf/2302.06706 (b12)
- [M] Same paper, another arXiv id, snippet figure of about 39% invalid under relaxed grading. https://arxiv.org/abs/2305.15771 (c10; PDF corrupt)
- [V] Valmeekam, Stechly, Kambhampati (2024) LLMs Still Can't Plan; Can LRMs? o1 on PlanBench. https://arxiv.org/pdf/2409.13373 (b14)
- [V] Valmeekam, Marquez, Kambhampati (2023) Can LLMs Really Improve by Self-critiquing Their Own Plans? https://arxiv.org/pdf/2310.08118 (b15)
- [V] Stechly, Valmeekam, Kambhampati (2024) Chain of Thoughtlessness? https://arxiv.org/pdf/2405.04776 (b16)
- [V] Stein, Fiser, Hoffmann, Koller (2025) Automating the Generation of Prompts for LLM-based Action Choice in PDDL Planning. https://arxiv.org/abs/2311.09830 (c11)
- [V] Hirsch, Uziel, Anaby-Tavor (2024) What's the Plan? (SimPlan). https://arxiv.org/abs/2402.11489 (c12)
- [V] Silver et al. (2024) Generalized Planning in PDDL Domains with Pretrained LLMs. https://arxiv.org/abs/2305.11014 (c08)
- [M] Meng et al. (2024) LLM A*. https://arxiv.org/pdf/2312.01797 (b25; skim only, low confidence)
- [V] Zheng et al. (2023/2024) Take a Step Back. https://arxiv.org/abs/2310.06117 (a23, a24, b23, c16)
- [V] Zhou et al. (2022/2023) Least-to-Most Prompting. https://arxiv.org/abs/2205.10625 (a25, b24, c17)
- [V] Malek et al. (2025) Frontier LLMs Still Struggle with Simple Reasoning Tasks (Unpuzzles). https://arxiv.org/abs/2507.07313 (c18, d12)
- [V] Canonaco, Pozanco, Borrajo (2026) Semantic Partial Grounding via LLMs. https://arxiv.org/abs/2602.22067 (c14)
- [V] Liu et al. (2026) Learn to Relax with LLMs: AutoCO. https://arxiv.org/abs/2509.12643 (c15, d11)
- [M] Bukkapatnam and Karuturi (2026) LM-Landmarks. https://icml.cc/virtual/2026/68028 (c13, d15; listing page only; workshop poster)

**Gap-search papers (2026 preprints, read once)**

- [V] Pereira, Correa, Meneguzzi, Seipp (2026) LeanPlan. https://arxiv.org/abs/2610.08246 and https://arxiv.org/pdf/2610.08246 (d01, d02; table scrambled, sums used)
- [V] Meneguzzi et al. (2026) Hierarchical Task Network Planning with LLM-Generated Heuristics. https://arxiv.org/abs/2605.07707 and https://arxiv.org/pdf/2605.07707 (d03, d04)
- [V] Gestrin and Seipp (2026) LLM-Evolved Domain-Independent Heuristics for Symbolic AI Planning. https://arxiv.org/abs/2605.29649 and https://arxiv.org/pdf/2605.29649 (d05, d16; workshop paper)
- [V] Pereira, Correa, Seipp (2026) Property-Guided LLM Program Synthesis for Planning. https://arxiv.org/abs/2605.16142 (d06)
- [V] Debnath, Adedigba, Mallipeddi (2026) When Planning Problems Become Hard for LLMs. https://arxiv.org/abs/2610.26964 and https://arxiv.org/pdf/2610.26964 (d07-d09)
- [V] Sharon (2026) Tree of Thoughts as a Classical Heuristic Search Problem. SoCS 2026. https://arxiv.org/abs/2605.28566 (d10)

**Internal**

- own cross-source summaries b26 and b27 (opened:false in the evidence file; used only as synthesis, not as sources).
