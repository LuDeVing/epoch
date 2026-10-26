# Conflict-driven clause learning (no-goods): deep document

*Subfield C06.03. Written 2026-10-26 from evidence_a to evidence_d, claims.jsonl (K25 to K35) and critique.md in this folder. Evidence ids (a01, b18, d08 and so on) point to those files. Numbers corrected by the cross-check are used in their corrected form. Status marks: [E] established (two or more independent sources), [S] single source, [C] contested. Claims K01 to K24 named in the critique were not on disk; their content is rebuilt here from the evidence lines, and statuses below are set from the evidence ids.*

## 1. What it is

CDCL is the search method inside nearly every modern SAT solver. The solver guesses a value for a variable (a decision). It then draws every forced consequence (unit propagation). Sooner or later two consequences clash. That clash is a conflict.

A plain backtracking solver reacts to a conflict by undoing the last guess and trying the other value. It learns nothing. It will walk into the same dead end again in another part of the tree.

A CDCL solver does three extra things at each conflict.

1. **Analyse.** It walks backwards through the record of why each value was forced (the implication graph). It finds the small set of earlier assignments that together caused the clash.
2. **Learn.** It writes the negation of that set as a new clause. This clause is a **no-good**: "this combination of assignments cannot be part of any solution". It is logically implied by the formula, so it is always sound. It is added to the formula and kept.
3. **Backjump.** It does not undo only the last guess. It jumps back to the earliest decision level that the new clause involves, skipping every guess that had nothing to do with the clash. The new clause then forces a different value at once.

Around this core sit a few supporting parts: a decision rule that favours variables seen in recent conflicts (VSIDS), a cheap way to keep propagation fast (two watched literals), restarts that clear the guesses but keep the learned clauses, and deletion of learned clauses that are unlikely to be used again.

Why we care. Our agent is a language model inside a scaffold. When an attempt fails, the scaffold can record why in a short, reusable form and use it to avoid the same failure. Schema state S5 (revise), S6 (impasse) and S9 (look back) already do a soft version of this with one-line lessons. CDCL is the best-studied case of "learn from failure" in any search system, with large benchmarks and clean ablations. It tells us what makes failure memory work, what makes it fail, and what it costs.

The headline caution from this folder: **no published paper tests a formal, checked no-good store inside an LLM agent** (K35, b26). Everything about LLMs below is from free-text lessons, which are not implied by the failure the way a SAT clause is. The SAT results are a source of design rules and boundary conditions, not a proof that the idea works for language agents.

## 2. History and theories in depth

### 2.1 Before CDCL: backjumping and nogoods in constraint solving

Constraint solvers knew two ideas long before SAT adopted them. Dependency-directed backtracking jumps back to a choice that actually caused the failure. Nogood recording stores a failed combination. Both were studied in CSP work (Dechter, Frost and Dechter; Drescher and Walsh on ASP). Those sources were seen as titles only (c27) and are not used for numbers. The two ideas arrive in SAT through Bayardo and Schrag and through GRASP.

### 2.2 Bayardo and Schrag (1997): the CSP look-back paper

Bayardo and Schrag added conflict-directed backjumping (CBJ) and learned no-goods to a Davis-Putnam solver called relsat (a01, b06, c01).

- **Size-bounded learning of order i:** keep a no-good only if it has i or fewer variables.
- **Relevance-bounded learning of order i:** keep a no-good only while at most i of its variables have changed since it was derived. When it stops applying to the current partial assignment, drop it.

Results over 100 random-seed runs per instance, 10 minute cutoff, 1997 hardware (a01 to a05):

- The unenhanced solver failed 100% of runs on both a bridge-fault circuit and a single-stuck-at circuit.
- Backjumping alone solved the bridge-fault instance in 100 of 100 runs. On the single-stuck-at instance (ssa2670-141) failures remained, and learning removed them: size-bounded order 3 failed 23%, order 4 failed 0% (242 s), relevance-bounded order 3 failed 4%, order 4 failed 0%.
- On Tower-of-Hanoi planning (hanoi4) the failure rates were 100% naive, 94% size(3), 92% size(4), 79% relevance(3), 13% relevance(4). Relevance(4) was the only variant that solved the open hanoi5 instance, in 4 of 100 runs.
- Against stochastic local search and Tableau on planning encodings, relsat(4) was far faster than Tableau and often faster than WSAT (log_gp.c 39.4 s vs WSAT 419.2 s vs Tableau 11,144 s). WSAT still won on some encodings (log_dir.b 16.6 s vs 2.6 s).

Their boundary condition (a04, b07): look-back helps when the instance holds sub-problems with **short, easily derived no-goods**. On the 3bit circuits no look-back variant ever finished, and local search was trivial. A simple random sampler (ISAMP) was about 10 times faster than relsat(4) on six scheduling instances, with 100% success (c02). Their explanation (look-ahead heuristics working together with learned clauses) is a conjecture and was never tested.

### 2.3 GRASP (Marques-Silva and Sakallah, 1996 and 1999): the CDCL template

GRASP gave the analysis procedure that defines CDCL (a06, a07, c03). It treats conflicts as normal and analyses each one. It builds the implication graph and walks back from the conflict. It produces one of three outcomes: a new clause, a failure-driven assertion if the cause is the latest decision, or a non-chronological jump if the cause lies at an earlier level. The backjump level is the highest decision level among the cause assignments.

Further points:

- **Growth control.** Clause growth can be exponential. GRASP kept clauses up to a size bound (20 literals in the experiments) and kept longer ones only while unit.
- **Unique implication points (UIPs).** Dominator nodes of the conflict in the implication graph give shorter, stronger clauses and can be found in linear time.
- **Results.** On circuit-fault benchmarks with a 10,000 s limit: BF-1355 149 of 149 solved in 125.7 s total (TEGUS 53 solved, POSIT 64); SSA-2670 12 of 12 (TEGUS 0); BF-2670 53 of 53 (TEGUS 25) (a08).
- **Where it lost.** On small or satisfiable families fixed overhead showed: II-8 23.4 s vs POSIT 2.3 s; JNH 21.3 s vs 0.8 s (a09).
- **Where the saving comes from.** Non-chronological backtracks were a significant share of all backtracks, and some jumps skipped millions of tree nodes (a10).

### 2.4 Chaff (2001): engineering made it cheap

Chaff was one to two orders of magnitude faster than GRASP and SATO on hard industrial instances (a11, a12, b04). The authors credit engineering, not new learning:

- More than 90% of run time is propagation. Two watched literals per clause mean that backtracking needs no clause updates.
- VSIDS keeps a counter per literal, raises it when the literal appears in a new conflict clause, and shrinks all counters on a schedule. Decisions follow recent conflicts.
- Restarts clear all decisions and keep all learned clauses. They may fire thousands of times on a hard instance.

Chaff is the competing explanation to "learning is the key". It says that cheap bookkeeping and a recency focus matter as much. The later ablation (section 5) shows both are needed, with learning first.

### 2.5 Clause quality and deletion: Glucose (2009)

Audemard and Simon (a15, a16, b08, b09, b10) showed which learned clauses are worth keeping.

- **Literal block distance (LBD)** of a clause is the number of distinct decision levels among its literals. Clauses with LBD 2 ("glue clauses") are used far more than their length suggests. On SAT-Race 06 benchmarks 40% of unit propagations on learned clauses came from glue clauses, but only 20% from clauses of size 2.
- **Aggressive deletion.** Every 20,000 + 500x conflicts (x = number of deletions so far) delete half of the learned clauses, keeping low-LBD and asserting ones. Four MiniSat variants solved 70, 74, 79 and 82 instances (original, aggressive deletion, LBD, both; row labels uncertain, range solid).
- **Competition result.** Glucose solved 176 of 234 SAT'07 industrial instances in 10,000 s. PicoSat 153, RSat 139, MiniSat 132. It was fastest on 68 and solved 140 problems in 2,500 s.
- **A progress signal.** On most industrial instances the decision level of conflicts decreases as the run goes on. Learning makes the solver hit contradictions higher in the tree. The fitted line had a negative slope on 167 of 199 benchmarks (critique: another cut in b10 says 92%; use 167 of 199). The predicted finish was 0.90 to 8.33 times the real count, mostly about 1.37 times. It was not seen on random problems.

### 2.6 What a good learned clause is: empowerment (2008) and VSIDS theory (2015)

Pipatsrisawat and Darwiche (a22) defined an **empowering** clause: adding it lets unit propagation derive something it could not before. A clause that is short but not empowering is useless. On 949 problems with 1,800 s each, Rsat solved 402 UNSAT, a variant with bi-asserting clauses 433, and the variant with the empowerment check 438. UNSAT time on commonly solved problems fell 34%. Skipping the empowerment check gave only 647 solved versus 740 for plain Rsat. On SAT instances the variant was slightly worse.

Liang et al. (a17, c07) explain why VSIDS works. It picks "bridge" variables that link communities in the instance. Multiplicative decay acts like an exponential moving average over recent conflicts. An adaptive-decay variant solved 351 vs 343 of 1,030 competition instances (+2.4%). The finding does not hold for random instances.

### 2.7 Theory: why learning plus restarts is strong

- Beame, Kautz and Sabharwal (a18, a19, b16, c05): clause learning with a suitable scheme gives exponentially shorter proofs than regular and DP resolution. With unlimited restarts a variant matches general resolution. The proofs exist, but finding them needs a good branching order. With a branching sequence taken from the problem graph, zChaff (restarts off) solved grid pebbling at 1,000 layers (1,001,000 variables) in 4,251 s UNSAT, where the default heuristic failed at about 7 to 8 layers inside 6 hours.
- Buss, Hoffmann and Johannsen (a20): exact proof-system match for DPLL with learning. If lemma length is capped too hard, some tasks become provably exponential.
- Atserias, Fichte and Thurley (a21, c06): a learning solver with random decisions and enough restarts acts like width-k resolution after O(n^(2k+2)) conflicts. This is an existence bound with a huge exponent, not a speed prediction.
- Gomes, Selman and Kautz (a23, d04, d05): run time of complete search is heavy-tailed. A random tie-break with a cutoff and restart removes the tail. Examples: logistics.d with Satz took 108 minutes deterministic vs about 95 s randomized (about 1,800 backtracks in total); 3bit-adder-32 over 24 h vs 95 s; round-robin 18 over 48 h vs 1.4 h. Boundary: round-robin 14 got worse (411 s vs 17 min), and blocks world showed no heavy tail (about 30 min vs about 23 min).

### 2.8 Outside SAT: planning

Kambhampati (2000, d01 to d03) added explanation-based learning and dependency-directed backtracking to Graphplan. Speedups ranged from 1.6x (blocks world) to 120x (logistics Att-log-a, which plain Graphplan did not solve after 40+ CPU hours), with up to 1000x claimed in the abstract. The size of the gain tracked how much explanation shortened the stored memo: Gripper-8 memos 8.5 vs 23.9 literals, Tower-5 7.5 vs 23.8, Ferry-6 6.9 vs 14.9, but Att-log-a 10.15 vs 11.83 and Rocket-ext-a 9.52 vs 11.3. The author says memo-length reduction correlated perfectly with speedup. In plain Graphplan, checking stored memos took 11.7 of 19.4 minutes on one instance. Rintanen (b17) shows a planning-specific variable choice inside the same CDCL solver beat VSIDS: 757 vs 701 of 968 STRIPS instances, close to LAMA at 775.

### 2.9 The LLM-agent line

There is no direct CDCL-for-LLM paper (b26: two search passes, zero hits). The nearest work falls into five groups.

1. **Free-text failure memory.** Reflexion (b18, b19, c17), LATS (d14), Mistake Notebook Learning (d11, d12), IBM trajectory tips (d13), Sentry (b21 to b23, c21, c22).
2. **Conflict-like diagnosis.** Core-guided repair (Sarkar, c15; Salla, c16), CausalFlow (c20), AgentDebug (b25, c25, abstract only), Tyen et al. (d08, d09).
3. **Self-correction limits.** Huang et al. (b20, c19), Kamoi et al. (d10), Olausson et al. (d07).
4. **Repeat and loop measurement.** MAST (b24), TIDE (c23).
5. **Fine-tuned from failed branches.** TrialMaster (c24).

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Remembering why an attempt failed is the biggest single CDCL feature | MiniSat, 10,000 instance-versions, 1000 s: full 9068 solved; no learning 4837; no VSIDS 6932; no two watched literals 8409; no restarts 8653. Extra solved by enabling CL, VSIDS, 2WL, RST: 4231, 2136, 659, 415 | Katebi et al. 2011 (a13, b01, c04) | [S] one solver and benchmark mix; backed in kind by Elffers 2018 (a24, b11) so [E] for "learning is critical" |
| Learning is not best in every family | sverif: no VSIDS 592 vs full 420 of 500; plan: no learning 327 vs full 1006 of 1200; atpg: 965 without learning vs 1000 with, of 1000. termrw: 446 without restarts vs 420 with | Katebi et al. (a14, b02) | [S] |
| Learned clauses are critical, not only a branching guide | Qualitative from PAR scores over solver knobs on crafted UNSAT families | Elffers et al. 2018 (a24, b11) | [E] with Katebi |
| Backjumping plus relevance-bounded learning turns an unsolvable instance into a solvable one | hanoi4 fail rate: 100% naive, 94% size(3), 92% size(4), 79% rel(3), 13% rel(4). ssa2670-141: size(3) 23%, size(4) 0%, rel(3) 4%, rel(4) 0%. 100 runs, 10 min | Bayardo and Schrag 1997 (a02, a03, c01) | [S] one group, but replicated in kind by GRASP and Graphplan work |
| Boundary: needs short derived no-goods | 3bit circuits never solved by any look-back variant, trivial for WSAT. ISAMP about 10x faster than relsat(4) on six scheduling instances | Bayardo and Schrag (a04, b07, c02) | [E] with planning data below |
| Gain in planning tracks memo shortening | Speedup 1.6x (blocks) to 120x (logistics); up to 1000x claimed. Memo length plain vs EBL/DDB: Gripper-8 23.9 to 8.5, Att-log-a 11.83 to 10.15 | Kambhampati 2000 (d01, d02) | [E] with Bayardo and Schrag (K25) |
| Memo checking can dominate cost | 11.7 of 19.4 min spent checking stored memos on Rocket-ext-a; EBL/DDB run 0.8 min | Kambhampati (d03) | [S] |
| GRASP beat older solvers on structured circuits and lost on easy ones | BF-1355: 149 of 149 solved vs TEGUS 53; II-8 23.4 s vs POSIT 2.3 s | Marques-Silva and Sakallah (a08, a09) | [S] author-run |
| Quality score for lessons: keep tight cross-level clauses | LBD 2 clauses supply 40% of learned-clause propagations vs 20% for size-2. Glucose 176 vs 153, 139, 132 of 234 | Audemard and Simon 2009 (a16, b08, b09) | [S] |
| A useless short clause hurts | Without empowerment check 647 solved vs 740 plain; with it UNSAT 438 vs 402; time -34% | Pipatsrisawat and Darwiche 2008 (a22) | [S] |
| Failures come earlier in the tree as learning works | Negative slope of conflict level on 167 of 199 benchmarks | Audemard and Simon (a15, b10) | [S] correlational |
| Restart value is heavy-tail dependent | Satz logistics.d 108 min vs 95 s; round-robin 14 worse (411 s vs 17 min); blocks world no heavy tail | Gomes et al. 1998 (a23, d04, d05) | [S] (K30) |
| Restart cadence depends on SAT vs UNSAT | Lingeling interval 2 to 512: total 122,127,139,144,144,161,163,168,158; UNSAT peaks at 8 (90), SAT at 256 (83). EMA restarts 178 to 181 vs best static 168 of 300 | Biere and Frohlich 2015 (b14, b15) | [S] |
| Adaptive restarts can fail badly | Glucose-style restarts sometimes block restarts and perform terribly; clique family needs restarts off; LRB did not beat VSIDS on crafted families | Elffers et al. (a24, b12, b13) | [S] |
| Fresh LLM attempts scale log-linearly with a verifier | SWE-bench Lite 15.9% (1 sample) to 56% (250); CodeContests Gemma-2B 0.02% to 7.1% (10,000); MATH vote 40.50% to 41.41% | Brown et al. 2024 (d06) | [S] (K31) |
| Free-text repair does not beat resampling at equal tokens | Feedback quality is the bottleneck: GPT-4 self-explanation repair success 33.30% vs 52.60% with human feedback (40 programs, 16 participants). LATS HotPotQA: no reflection 0.58 vs 0.63 full | Olausson 2024 (d07); LATS (d14); Brown (d06) | [E] (K26) |
| Reflexion: failure memory helps when the check is real | ALFWorld 130 of 134 in 12 trials; HumanEval 91% vs 80%; Rust (50 hardest) 68% full vs 60% baseline vs 52% without tests; MBPP 0.77 vs 0.80 baseline, false-positive tests 16.3% vs 1.4% | Shinn et al. 2023 (b18, b19, c17) | [S] one group, free text |
| Self-correction with no external signal lowers accuracy | GPT-3.5 CommonsenseQA 75.8 to 38.1 (3 calls) and 41.8 (5 calls); GSM8K 75.9 to 74.7; GPT-4 GSM8K 95.5 to 91.5 to 89.0. With oracle: GPT-3.5 GSM8K 75.9 to 84.3, CSQA 75.8 to 89.7, HotpotQA 26.0 to 29.0; GPT-4 95.5 to 97.5, 82.0 to 85.5, 49.0 to 59.0 | Huang et al. 2024 (b20 corrected, c19) | [E] with Kamoi (d10) |
| A failure signal must be right 60 to 70% of the time | Losses on correct traces plateau near 65% finder accuracy | Tyen et al. 2024 (d09); Kamoi (d10) | [E] (K28) |
| Backjump to the true culprit step doubles the fix rate | Word sorting: 23.53% fixed vs 11.76% (random cut); 11.11% broken vs 15.56%. GPT-4 finds the mistake step 52.87% of the time | Tyen et al. (d08) | [S] (K27) |
| Stored lessons can lower scores | DeepSeek-V3.2-Exp AppWorld 73.2 vanilla vs 64.2 and 44.6 (two memory baselines); gated store 73.2 with zero entries. GPT-4.1 AppWorld top-3 at threshold 0.5: TGC 66.7 vs 69.6 (-2.9) | Su et al. 2025 (d11); Fang et al. 2026 (d13) | [E] (K29), preprints |
| Trigger-matched retrieval beats always-on lessons | Sentry: removing failure lessons raised WebShop 0.335 to 0.391; fixed playbook in context 0.364 to 0.296; broad-type retrieval -11.3%, unfiltered -18.8%, random -28.9%; k=3 and k=10 cost 4.5% and 6.2% vs k=5; no need-check -54.7% | Ji et al. 2026 (b21 to b23, c21, c22) | [S] one group, 9B model |
| Sentry end results | WebShop 0.468 vs 0.264 best baseline (label unverified), base 0.170; AppWorld 38.53% vs 27.56%; resolves 81.7% of 939 detected failures; SWE-bench Lite only 0.30 vs 0.24, recovery 34.0% | Ji et al. (b22, c21) | [S] |
| Gains shrink with stronger models | Think-enabled: DeepSeek-Reasoner AppWorld 75.0 to 76.2; Qwen3-8B Mind2Web 1.01 to 1.35. Batch size 1 to 16 cut memory 3x and raised accuracy 17% (KaggleDBQA, 185 test items); epoch 2 test fell 28.1% to 23.2% | Su et al. (d12) | [S] (K32) |
| Hard cases gain most from tips | AppWorld GPT-4.1 difficulty 3 SGC 19.1 to 47.6 (+28.5 points) with task-level tips; TGC overall +3.6 | Fang et al. (d13) | [S] technical report |
| Repeat failures are common | MAST: step repetition 15.7% of failures, 1642 traces, 7 systems, failure rate 41% to 86.7%. TIDE: loop ratio 32.0% for Qwen3-4B in FrozenLake; 15.8% to 1.0% (BlocksWorld) and 36.7% to 5.7% (WebShop) going 4B to 30B | Cemri 2025 (b24); TIDE (c23) | [S] each, annotated or correlational |
| Core-guided feedback changes fabrication, not accuracy | 77 problems: generic 88.3% vs core 89.6% (p = 1.0); fabrication on infeasible items 11 of 14 (79%) vs 1 of 14 (7%), Fisher p < 0.001. Salla: set consistency 0.52 (no solver) to 0.84 (check) to 0.88 (repair, no core) to 0.91 (core); revision cost 0.6 vs 0.4 | Sarkar (c15); Salla (c16) | [C] two small studies, different outcomes |
| Causal attribution of the culprit step is a first step only | 555 of 1299 failures repaired (42.7%); 21.9% (SealQA Hard) to 52.4% (GSM8K); MBPP: Self-Refine 80.3% vs CausalFlow 41.2% | CausalFlow (c20) | [S] |
| LLMs do not show CDCL-like hardness behaviour | Most say "satisfiable" for nearly every random 3-SAT formula; non-reasoning models below paired score 0.2 by 25 variables; GPT-5 0.79 at 25 variables, 0.35 at 50; self-reported branches and conflicts did not track hardness | Zhang et al. 2026 (c09, c10) | [S] |
| Models trained on DPLL traces learn it in range only | 70M and 160M models: 98.5% to 99.96% in range, sharp drop beyond trained size | Pan et al. 2025 (c11) | [S] |
| LLMs can tune CDCL heuristics when code is scored | AutoSAT beats MiniSat on 9 of 12 datasets; AutoModSAT about 40% PAR-2 gain over base | Sun et al. (c12, c13) | [S] |

## 4. Mechanisms and models

This section is written so that an engineer can build the pieces. First the SAT mechanisms, then the version we could build for an LLM scaffold.

### 4.1 The SAT machinery

**State.** A trail of assignments in order. Each has a decision level (0 for forced facts, then 1, 2, ... per guess) and a reason (the clause that forced it, or "decision").

**Loop.**

1. Propagate. If a clause has all but one literal false, force the last one and record the clause as its reason.
2. If no conflict and all variables are set, return SAT.
3. If no conflict, pick a variable by VSIDS score, pick a value (the saved last value for that variable), open a new decision level, go to 1.
4. If a conflict arises at level 0, return UNSAT.
5. Otherwise analyse (4.2), add the learned clause, backjump, and the learned clause forces a literal. Go to 1.

**Conflict analysis (first UIP).** Start with the conflicting clause. While more than one literal in it is at the current level: take the most recently assigned such literal, and resolve the clause with that literal's reason clause. Stop when exactly one current-level literal remains. That literal is the first unique implication point. The resulting clause is the learned no-good. It contains one current-level literal and other literals from earlier levels. Backjump level = the second highest level in the clause. After the jump, the clause is unit and forces the negation of the UIP literal. (a06, a07, a22.)

**Why it is sound.** Each resolution step is a valid inference, so the learned clause is implied by the formula. Adding it never removes a solution. This is the property LLM lessons lack.

**Two watched literals.** Each clause watches two of its literals that are not false. Only when a watched literal becomes false is the clause visited. Backtracking needs no work. More than 90% of run time is propagation, so this one trick makes a large store affordable (a11).

**VSIDS.** Per variable counter. Bump the variables in each new learned clause. Multiply all by a decay factor on a schedule (equivalent to growing the bump). Pick the highest unassigned variable. This is a recency-weighted count of "involved in recent failures" (a12, a17). There is no universal best decay (b13).

**Restarts.** Undo all decisions down to level 0, keep learned clauses, keep VSIDS scores and saved phases. Schedules: Luby sequence times a base; Glucose-style moving average of LBD (restart when recent LBD is worse than the long run); fixed interval. Biere and Frohlich found exponential-moving-average restarts best (178 to 181 of 300 vs 168 best static) (b15). Keep a fixed fallback so an adaptive rule cannot suppress restarts forever (b12).

**Clause deletion.** Score each learned clause (activity, size, or LBD). Periodically delete the worse half, never deleting clauses that are currently the reason for an assignment. Glucose schedule: first deletion after 20,000 conflicts, then the gap grows by 500 each time; keep LBD at most 2 and recently useful clauses (a16). Bayardo and Schrag's relevance rule is an alternative: a clause is active only while at most i of its literals are unassigned or changed since it was derived (a01).

**Clause minimisation and learned clause size cap.** GRASP kept clauses up to 20 literals (a07). Theory says too hard a cap makes some tasks exponential (a20).

### 4.2 A no-good store for an LLM scaffold (design, not tested)

The following is our translation. Every part is a design hypothesis until tested (see UNKNOWNS.md). The pieces map to SAT parts as follows.

| SAT part | Scaffold analogue | Who does it |
|---|---|---|
| Variable and assignment | A named choice in an attempt: the representation chosen, the rule hypothesis, the value of a key parameter, the operator used, the helper subgoal | Code extracts it from a structured attempt record |
| Conflict | A failed check run by code on an attempt (test failure, validator error, counter-example) | Code |
| Implication graph | The attempt record with each step tied to the choices it depended on | Code, from a typed log |
| First-UIP analysis | Shrink the failed attempt to the smallest set of choices that still produces the failure | Code by replace-and-rerun (as in CausalFlow, c20), or delta-debugging; the model only proposes the one-line explanation |
| Learned clause | A record: trigger (conditions on the task that make it apply) plus the forbidden combination | Code stores; model words the one-line lesson |
| Backjump | Return to the earliest choice in the no-good, not the latest | Code (only where a check can name the culprit step, K27) |
| Unit propagation of the no-good | When all but one choice of a stored no-good is made, forbid the last | Code, before the attempt is generated |
| Restart | New fresh-context attempt with all stored no-goods kept | Code (S3 already uses fresh contexts) |
| Clause deletion | Drop no-goods that are old, long, never matched, or whose trigger no longer applies | Code |
| VSIDS | Rank untried directions by how often they appear in recent no-goods | Code |

**Minimum record (to implement).**

```
nogood = {
  id, class,                       # problem class from S0
  trigger: {features...},          # code-checkable conditions, e.g. "grid has symmetric rows"
  forbidden: [choice, choice, ...],# 1 to 4 named choices that together fail
  evidence: check_output_excerpt,  # the located failing output (G2)
  source_check: name_of_code_check,# only code checks may write (K34)
  size, level_span,                # for the LBD-like score
  uses, helped, last_used,         # for deletion and the gate
  line                             # one model-written sentence for the prompt
}
```

**Write rules.** Only a code check may create a record (b19, b20, d10, K34). The check must have measured precision of about 70% or more (K28). A record is added only after the failure is reproduced or located, and in Sentry it is kept only if a recovery was verified (b22). Cap the forbidden set at a few choices; prefer clauses that tie several separate decision groups together (LBD idea, a16) and that change what the next attempt can do (empowerment idea, a22).

**Read rules.** Match by trigger in code. Show the model only the matching lines, after the first attempt (SCHEMA section 5 already says lessons come after the first attempt). Use a similarity threshold, not a fixed small k (d13). Allow zero matches. Never paste the whole store (b21, b23, d11).

**Gate.** Accept an update to the store only if a held-out batch shows a net gain (d11). Allow the store to be empty.

**Cost check.** Test before use: ratio = size of the derived reason / size of the full state. If the ratio is near 1, learning will not pay (d02, a04). Blocks world in Graphplan gave 1.6x, logistics 120x.

### 4.3 What a good progress signal looks like

In SAT, healthy learning shows as conflicts happening at shallower decision levels over time (a15, b10). The analogue for an attempt loop is: later attempts fail on earlier or shallower checks, or fail on fewer checks. If failure depth does not fall after several stored no-goods, the store is not working. This is a correlational signal in SAT. It has not been tested for LLM loops.

## 5. What holds up

### 5.1 Held up across more than one source

- **Stored lessons are the biggest lever in CDCL.** Katebi's ablation (a13) and Elffers's crafted-benchmark study (a24, b11) agree on the ranking in kind. Chaff's authors credit engineering (b04); the two views are compatible: learning is necessary, engineering made it affordable.
- **Benefit depends on how short the derived reason is.** Bayardo and Schrag (a04, b07) and Kambhampati (d02) reach the same boundary from two different problem types (K25, [E]).
- **Forgetting must be smart.** Bayardo and Schrag found relevance-bounded storage beat size-bounded (hanoi4 13% vs 92% to 94% fail). Glucose found LBD deletion beat keeping everything (a16). Elffers found too-aggressive erasure hurts when memory is tight, and LBD often picks the right clauses (b11). Pipatsrisawat and Darwiche found short but non-empowering clauses hurt (647 vs 740).
- **Free-text self-repair without a real check does not help.** Huang (b20), Kamoi (d10) and Olausson (d07) agree (K26, K34).
- **A failure signal that is wrong too often turns memory into harm.** Reflexion's MBPP result (16.3% false-positive tests) and Tyen's 60 to 70% threshold point the same way (K28).
- **Lesson stores can lower scores on strong models.** Mistake Notebook Learning (d11) and the IBM report (d13) agree; Sentry (b21) agrees on a 9B model (K29).

### 5.2 Held up in one source only

Sentry's trigger matching and verification (b21 to b23); backjump to the true culprit step (d08); fresh-sample scaling (d06); batch abstraction (d12); the heavy-tail argument (d04, d05); Kambhampati's memo-check cost (d03); AutoSAT-type gains (c12, c13); MAST and TIDE repeat rates (b24, c23).

### 5.3 Failures, exceptions, and contested points

- **Learning loses in some families.** Katebi's per-family rows: plan (327 without learning vs 1006 with) is clean, but on sverif the version without VSIDS solved more (592 vs 420 of 500). Bayardo's 3bit and random 3-SAT show look-back giving little. The crypto row in a14 is garbled and unreliable (critique). Resolution: learning wins on structured instances with short derived no-goods.
- **Restarts.** Elffers says frequent restarts add real power on some families (stone, pebbling) and that adaptive restarts can fail badly; Biere finds EMA-adaptive restarts best on a competition set. These are different benchmark classes (crafted vs competition), so the question stays open. Katebi finds restarts the smallest of four features (8653 vs 9068 solved) and negative on termrw.
- **LRB over VSIDS** did not replicate on crafted unsatisfiable families (b13), though it was tuned on industrial ones.
- **Katebi's statistics are soft.** Only 71% of averages were within 25% at 90% confidence, one solver, one mix. a13, b01 and c04 are the same source.
- **Core feedback is contested.** Sarkar sees no accuracy gain over generic errors (p = 1.0) but a large drop in fabrication (79% to 7%, 14 items). Salla sees a modest consistency gain (0.88 to 0.91). Both are small, from single groups (c15, c16).
- **Reflexion and the oracle.** Reflexion's gains come with test or environment signals; Huang's losses come without them. They are consistent once the oracle is considered. But Reflexion's ALFWorld retry trigger is a hand-written heuristic (3 repeats or 30 actions, c18), and it keeps only 1 to 3 reflections, which itself bounds relevance. LATS found reflections mattered little: 0.63 vs 0.58 on HotPotQA, and generic on WebShop (d14).
- **Always-on lessons can hurt.** Sentry's fixed playbook cost 0.364 to 0.296 on WebShop and 0.651 to 0.599 on Mind2Web Replay (b21).
- **Theory does not give agent predictions.** Results on proof size (a18, a20, a21) are about idealised solvers with perfect choice.

### 5.4 Interventions that worked and did not (LLM side)

Worked, in the sources read: lessons from a real check (Reflexion code tasks); trigger-matched retrieval with verification (Sentry); acceptance gate (MNL); batch abstraction (MNL); threshold retrieval over narrow top-k (IBM); core feedback to reduce fabrication (Sarkar).

Did not work: free-text reflection with no check (Huang); more repair rounds per sample (Olausson); reflection on easy tasks with strong models (LATS); persistent playbooks (Sentry); narrow top-3 retrieval at a loose threshold (IBM, -2.9 TGC); more epochs of store building (MNL, 28.1% to 23.2%); weak test suites (Reflexion MBPP).

## 6. Language models

**LLMs are not CDCL solvers, and their account of their own search is not reliable.** Zhang et al. (c09, c10) tested over 2,700 random 3-SAT formulas on GPT-5, o1, o3-mini, DeepSeek-reasoner, Claude 3 to 4 variants, GPT-4o and GPT-3.5. Most models answer "satisfiable" for nearly every random formula and show no easy-hard-easy phase transition. A paired test (a SAT and an UNSAT formula that differ minimally) exposes it: always predicting SAT gives accuracy 0.5 and paired score 0. Non-reasoning models were below paired score 0.2 by 25 variables. GPT-5 reached 0.79 at 25 variables and 0.35 at 50, with only about 20% of runs completed at the larger size. Self-reported branch and conflict counts did not track real hardness. Rule for our agent: any difficulty or progress signal comes from code.

**Trained, small models can learn DPLL.** Pan et al. (c11): 70M and 160M models trained on DPLL traces reached 98.5% to 99.96% in range and failed beyond the trained size. This says nothing about prompting a frontier model, and the traces contain no learned clauses.

**Repeating failed steps is common.** MAST (b24): 15.7% of failures in 1642 annotated traces are step repetition. TIDE (c23): loop ratio 32.0% in Qwen3-4B on FrozenLake; going from 4B to 30B-A3B cut it from 15.8% to 1.0% on BlocksWorld and from 36.7% to 5.7% on WebShop. Strong DeepSeek and Gemini models looped negligibly. So a repeat-blocker has most value for small models. It may add little for large ones.

**Free-text failure memory.**

- With a real check (tests, environment), Reflexion lifted ALFWorld to 130 of 134 and HumanEval to 91% vs 80% (b18). Without test generation Rust fell to 52% vs a 60% baseline; with the full method 68% (b19). The reflection step added 8 points over an episodic-memory-only variant on HotPotQA with ground-truth context.
- Without a real check, accuracy fell (Huang, b20).
- At equal compute, repair is often no better than resampling (Olausson, d07), and fresh sampling scales log-linearly with a verifier (Brown, d06).
- LATS: reflection added 0.05 EM on HotPotQA (d14).

**Stored lessons and model strength.** Gains shrink as the model gets stronger. DeepSeek-Reasoner on AppWorld moved 75.0 to 76.2 with a gated store, about 1 point and probably inside noise (d12). On DeepSeek-V3.2-Exp two always-on memories lost 9 and 29 points (73.2 to 64.2 and 44.6; d11). On GPT-4.1, top-3 retrieval at threshold 0.5 lost 2.9 points of TGC, while threshold 0.6 with no top-k gained 2.4 and LLM-guided selection gained 3.6; the biggest effect was on the hardest difficulty-3 tasks (SGC 19.1 to 47.6; d13).

**Retrieval design.** In Sentry on a 9B model, broad-type retrieval was 11.3% worse than failure-specific retrieval, an unfiltered playbook 18.8% worse, random entries 28.9% worse. The need-check (deciding whether to intervene at all) was worth 54.7% (b23).

**Diagnosis is the bottleneck.** GPT-4 explaining its own failing code repaired 33.30% of programs, vs 52.60% with human feedback; by difficulty: Intro 42.64 vs 62.21, Interview 19.33 vs 45.67, Competition 3.67 vs 14.67 (d07). LLMs find the first wrong step poorly (GPT-4 52.87% best of five) but correct it well once told (d08). Typed logging for causal attribution cost accuracy on easy tasks: GSM8K 75.0% with typed traces vs 88.1% direct, and gains levelled off after K = 3 interventions (c20).

**Repair by core.** Core-guided feedback stopped a weaker model fabricating solutions to infeasible problems (79% to 7%, n = 14) but did not raise accuracy over a generic error (c15). Chain-of-thought alone reached 98.7% feasibility on those problems, so at small sizes the model reasoning directly was hard to beat.

**Fine-tuning on failed branches.** TrialMaster (c24) reached 100% in distribution against 75.9% to 99.9% for depth-first search, depending on sampled tactic count. It needs training, so it is outside our no-training scope.

## 7. What our agent should take

Schema parts used: G (guardrail), S (state), O (operator), M (memory). The rule in SCHEMA section 8 applies: an item moves to SCHEMA.md as [E] only with two independent sources, and a new element enters as [S] or [D] with an equal-token test.

### Add now (established)

| # | Item | Part | Status | Evidence |
|---|---|---|---|---|
| A1 | **Only code checks may create a stored failure.** A lesson or no-good is written only from a failing check whose output code located. A model judge or the model's own sense of failure never writes to the store. | G2 / M | [E] | b19, b20, c19, d10, d15 (K34) |
| A2 | **Measure the check's precision before storing from it.** Do not store from a check below about 70% precision. Below that, correct traces get damaged. | G2 / G3 | [E] | d09, d10, b19 (K28) |
| A3 | **Gate the lesson store.** An update is kept only if it shows a net gain on a held-out batch. An empty store is a valid state. Retrieve by trigger match with a similarity threshold, never by pasting the whole list and never by a fixed small k. | M | [E] | d11, d13 (K29); b21 agrees |
| A4 | **Every store trial must include a resample-at-equal-tokens arm**, not only a no-memory arm. Add this to the G7 test rule. | G7 | [E] | d07, d14, d06 (K26) |
| A5 | **Run the shortening-ratio test before enabling a store for a problem class.** Compute (derived reason size / full state size) on 5 to 10 failures. Enable only if well below 1. Where explanation does not shrink the reason, learning gave 1.6x or less in planning and nothing in random 3-SAT. | S0 / G12 | [E] (SAT, planning) | d01, d02, a03, a04, b07 (K25) |
| A6 | **A store has a cost.** Inject only entries whose trigger matches the current state. Keep the store in code. | M | [E] in kind; K33 itself [S] | b21, b23, d03, d11 |

### Test first (not yet established for an LLM agent)

| # | Item | Part | Status | Evidence |
|---|---|---|---|---|
| T1 | **Formal no-good store** (trigger plus forbidden set, code-derived, subsumption-checked) against free-text lessons against resampling against no memory, at equal tokens. | M / S5 / S9 | no direct evidence; open | K35, b26 |
| T2 | **Code-derived minimal conflict set** by replace-and-rerun or delta debugging, instead of the model's explanation. | S5 | [S] | c20, d07 |
| T3 | **Backjump to the culprit step** where a deterministic check names it, versus plain retry with a lesson. | S5 / S6 | [S] | d08 (K27) |
| T4 | **Restart with lessons kept** versus fresh restart with no memory, gated by an attempt-length heavy-tail check. | S3 / S6 | [S] | d04, d05, d06 (K30, K31), a12 |
| T5 | **Lesson score for deletion** (LBD analogue: distinct choice groups tied together; empowerment analogue: does it change the next attempt) and relevance-bounded forgetting. | M | [S] in SAT only | a01, a16, a22 |
| T6 | **Verify-before-store**: keep a new lesson only if a recovery was verified by code. | M / S9 | [S] | b22, d11 |
| T7 | **Exact-repeat blocker in code**: refuse to re-run a candidate identical to one already failed. Near-zero cost. | S4 / S3 | [S] | b24, c23, c18 |
| T8 | **Batch abstraction** of lessons across several failures, with merge, instead of one lesson per failure. | M / S9 | [S] | d12 |
| T9 | **Progress signal**: failure depth or number of failing checks should fall over attempts; flat means the store is not working, so fire the impasse (S6). | S6 | [S] correlational | a15, b10 |
| T10 | **Adaptive trigger with a fixed fallback** for restarts or operator changes. | S6 | [S] SAT only | b12, b15 |
| T11 | **Core-style feedback** (name the clashing constraints) to reduce fabrication on infeasible items. | S5 | [C] | c15, c16 |
| T12 | **Planning-specific ordering with generic memory**: keep the general no-good store and add a problem-structure ordering of what to try first. | S3 / S6 | [S] | b17, a19 |

## 8. Concrete tests on our bench

All arms get the same total tokens, including setup, logging and model calls for lessons. The primary metric is solved items at equal tokens; secondary metrics are repeated-failure rate and tokens to first pass. Use a coded task family where a code check exists and the ratio test of A5 passes (small puzzle domain or ARC-style items with held-out cases). Report counts with intervals and mark any gain smaller than the noise as null.

| # | Item type | Arms (equal tokens) | Metric | Expected effect |
|---|---|---|---|---|
| B1 (T1) | 60 to 100 puzzle items with a code check and known short failure reasons (for example constraint puzzles, small planning tasks, ARC-style rule items with held-out cases) | (a) no memory plus resample; (b) free-text one-line lessons shown after the first attempt; (c) coded no-goods with trigger match and unit propagation of forbidden combos; (d) resample only with the saved tokens | Items solved; share of attempts that repeat a failed combination | Based on K26, expect (b) to be about equal to (d). Expect (c) to beat (d) only where the shortening ratio is low. Gain would show as a lower repeat rate and +5 to +10 points on those items; no gain elsewhere. |
| B2 (A5/K25) | 5 to 10 failures per problem class across 6 or more classes | Compute ratio per class; then run B1 per class | Rank correlation between ratio and gain from (c) over (d) | Negative correlation (low ratio, more gain), if the SAT and planning pattern carries over. |
| B3 (A3/K29) | Same items on our strongest model | (a) no memory; (b) always-on full list; (c) trigger match with threshold; (d) trigger match with gate | Score vs (a) | (b) is at or below (a); (c) and (d) at or above (a); gap small on a strong model. |
| B4 (T2) | Items where a failing run can be replayed with one choice swapped | (a) model-written lesson from the full trace; (b) code-shrunk conflict set plus one model-written line | Fix rate on the next attempt; repeat rate | Smaller, more specific lesson; fix rate higher in (b). CausalFlow's 42.7% repair rate is the reference level. |
| B5 (T3) | Multi-step items where a check names the first failing step (code, algebra steps, plan steps) | (a) retry from scratch; (b) retry with a lesson; (c) resume from the culprit step with a lesson | Fixed share of failed runs; tokens per fix | (c) beats (a) when the culprit is code-named; Tyen's ratio of about 2x is an upper guide. Expected to vanish when the culprit must be guessed. |
| B6 (T4) | Items with a measured spread of attempt lengths | (a) one long attempt; (b) many fresh restarts with no memory; (c) restarts with the store kept | Solved at equal tokens | (b) wins where a short fraction of attempts succeed (heavy tail); (c) adds on top only where the store passes B1. Null on classes with no heavy tail. |
| B7 (A2/K28) | A failure check with deliberately degraded precision (inject 10%, 20%, 30%, 40% false failures) | Store on, at each precision | Net gain vs no store | Break-even near 60 to 70% precision. |
| B8 (T5) | Store with 50+ entries per class | (a) keep all; (b) delete by age; (c) delete by score (distinct choice groups plus usage); (d) relevance-bounded | Solved at equal tokens; prompt length | (c) or (d) at or above (a) with a smaller prompt. |
| B9 (T7) | Items where a small model loops | Repeat-blocker on vs off | Loop ratio; solved | Large effect on a small model (TIDE: 32% loop ratio), small on a strong model. |
| B10 (T9) | Runs with logged failure depth | Impasse fired by flat depth vs fired by fixed attempt count | Solved; wasted tokens | Earlier, cheaper impasse when depth is flat. |
| B11 (T8) | KaggleDBQA-like repeated task batches | per-failure lessons vs batch-merged lessons | Accuracy; store size | Store 3x smaller; accuracy up about 17% in the source. |
| B12 (T11) | Infeasible-by-design items | generic error vs named clashing constraints | Fabrication rate | Large drop in fabrication; accuracy unchanged. |

Logging for all tests follows SCHEMA section 6, plus: per attempt, the choices made, the check result, the no-goods matched, and whether the attempt repeated a failed combination.

## 9. What does not transfer, and why

1. **Soundness.** A SAT clause is implied by the formula, so adding it can never remove a solution. A lesson from a language task is a guess about cause. A wrong lesson can prune the true answer, and a false failure verdict can create one (Reflexion MBPP, 16.3% false-positive tests). Remedy: code checks only, measured precision, and a gate.
2. **Cheap, exact conflict analysis.** In SAT the implication graph is free: every forced value records its reason clause. A language attempt has no such graph. CausalFlow gets there by re-running with one step replaced, which costs extra calls and had a 42.7% repair rate. The "which choices caused it" step is the hard part.
3. **Unit propagation at scale.** SAT checks millions of clauses per second. We check a handful of records per attempt. Different cost model: prompt tokens, not hash lookups (d03 caveat). Stored text in the prompt can bias the model even when irrelevant (b21).
4. **Completeness and proof.** CDCL proves UNSAT. Our agent proves nothing; it needs only to avoid repeats. The resolution-theory results (a18, a20, a21) say nothing about agent success rates.
5. **Restart theory.** Restarts in SAT keep learned clauses and re-randomise early guesses. The heavy-tail argument applies to complete backtrack search. For LLM attempts the run length distribution is unmeasured. Fresh samples scale well with a verifier (d06) but that is pure restart with no memory, not CDCL restarts.
6. **VSIDS and recency.** Variable-level counters have no direct analogue in free text. A recency-ranked list of untried directions might, but untested.
7. **Benchmarks.** Structured industrial CNF is sparse and local. Random 3-SAT, hash-like crypto and 3bit-type instances are not helped (a04, a14). Language tasks vary: only those with short, checkable failure reasons fit.
8. **Models that reason do some of this inside the trace.** Strong reasoning models loop little (TIDE: negligible for DeepSeek and Gemini series) and gain about 1 point from a lesson store (d12). Our measured baseline decides.
9. **Self-reported search counts.** Models' reported conflicts and branches did not track real hardness (c10).
10. **Training on traces.** DPLL-trace training and failed-branch fine-tuning (c11, c24) are out of scope: the agent is a scaffold, not a trained model.

## 10. Open questions

1. Does a formal no-good store beat free-text lessons and plain resampling at equal tokens? No source tests it (K35).
2. What is a "conflict" for a language task, and can code derive the smallest responsible set of choices from a failed trace? CausalFlow is a first step with weak results on some tasks.
3. How long may the list be, and what relevance rule? Evidence is SAT (relevance-bounded, LBD) and one retrieval study (k = 5 beat k = 3 and k = 10 in Sentry). No principled number for prompts.
4. Does the harm from always-on lessons hold for the final frontier model, and how big is it with real confidence intervals? Existing numbers have no intervals.
5. What is the restart analogue (cutoff length, fraction of lessons carried over), and do LLM attempt lengths show a heavy tail?
6. Is non-chronological backjumping worth its overhead against simple retry with a lesson, at equal tokens?
7. What false-failure rate makes a no-good store harmful in a real task, as opposed to the simulation (d09)?
8. Which of our task families have short, easily derived no-goods? The shortening-ratio test is cheap; not yet run on ARC items or puzzles.
9. Can a progress signal from failure depth be built for language attempts?
10. Do the Sentry results (single group, small open model) replicate with a frontier model?
11. Why does learning lose on some families (sverif, termrw, crypto)? Katebi's authors could not explain it without instance-level study.
12. Do lessons from one problem transfer to another of the same class, or only repeat within one problem? CDCL no-goods persist inside one problem; our S9 lessons are cross-problem. These are different things.
13. Sources not opened: Pipatsrisawat and Darwiche 2011 (CDCL p-simulates resolution), Dechter dead-end learning, Frost and Dechter 1994, ASP lazy nogood generation (clasp), Katsirelos and Bacchus, AgentDebug full text.

## 11. Sources

Marks: [V] opened and read this session; [M] snippet or abstract only.

**SAT and CSP**

1. [V] Bayardo and Schrag (1997) Using CSP look-back techniques to solve real-world SAT instances. https://www.bayardo.org/ps/aaai97.pdf and https://cdn.aaai.org/AAAI/1997/AAAI97-032.pdf (a01 to a05, b06, b07, c01, c02)
2. [V] Marques-Silva and Sakallah (1996) GRASP: a new search algorithm for satisfiability. https://www.cs.cmu.edu/~emc/15-820A/reading/grasp_iccad96.pdf (a06 to a10)
3. [V] Marques-Silva and Sakallah (1999) GRASP: a search algorithm for propositional satisfiability. https://web.eecs.umich.edu/~karem/papers/grasp.pdf (c03)
4. [V] Moskewicz, Madigan, Zhao, Zhang, Malik (2001) Chaff. https://www.princeton.edu/~chaff/publication/DAC2001v56.pdf and https://www.cs.cmu.edu/~emc/15-820A/reading/chaff.pdf (a11, a12, b04, b05)
5. [V] Katebi, Sakallah, Marques-Silva (2011) Empirical study of the anatomy of modern SAT solvers. https://ai.dmi.unibas.ch/_files/teaching/fs21/ai/material/ai32-katebi-et-al-sat2011.pdf and https://web.eecs.umich.edu/~karem/papers/anatomy.pdf (a13, a14, b01 to b03, c04)
6. [V] Audemard and Simon (2009) Predicting learnt clauses quality in modern SAT solvers. https://www.ijcai.org/Proceedings/09/Papers/074.pdf (a15, a16, b08 to b10)
7. [V] Liang, Ganesh, Zulkoski, Zaman, Czarnecki (2015) Understanding VSIDS. https://arxiv.org/abs/1506.08905 (a17, c07)
8. [V] Beame, Kautz, Sabharwal (2004) Towards understanding and harnessing the potential of clause learning. https://arxiv.org/abs/1107.0044 and https://www.jair.org/index.php/jair/article/view/10346 (a18, a19, b16, c05)
9. [V] Buss, Hoffmann, Johannsen (2008) Resolution trees with lemmas. https://arxiv.org/abs/0811.1075 (a20)
10. [V] Atserias, Fichte, Thurley (2011) Clause-learning algorithms with many restarts and bounded-width resolution. https://arxiv.org/abs/1401.3868 (a21, c06)
11. [V] Pipatsrisawat and Darwiche (2008) A new clause learning scheme for efficient unsatisfiability proofs. https://cdn.aaai.org/AAAI/2008/AAAI08-243.pdf (a22)
12. [V] Gomes, Selman, Kautz (1998) Boosting combinatorial search through randomization. https://www.cs.virginia.edu/~rmw7my/papers/aaai98boost.pdf and https://www.cs.cornell.edu/selman/papers/pdf/98.aaai.boost.pdf (a23, d04, d05)
13. [V] Elffers, Giraldez-Cru, Gocht, Nordstrom, Simon (2018) Seeking practical CDCL insights from theoretical SAT benchmarks. https://ijcai.org/proceedings/2018/181 (a24, b11 to b13; c08 title page only)
14. [V] Biere and Frohlich (2015) Evaluating CDCL restart schemes. https://cca.informatik.uni-freiburg.de/papers/BiereFroehlich-POS15.pdf (b14, b15)
15. [V] Rintanen (2010) Heuristics for planning with SAT. https://users.aalto.fi/rintanj1/papers/Rintanen10cp.pdf (b17)
16. [V] Kambhampati (2000) Planning graph as a (dynamic) CSP. https://www.jair.org/index.php/jair/article/view/10248 (d01 to d03)
17. [M] Drescher and Walsh; Dechter and others on nogood learning in CSP, ASP and planning. https://cgi.cse.unsw.edu.au/~tw/dwaaai11.pdf (c27, titles only)

**SAT with language models**

18. [V] Zhang, Chen, Chen (2026) Satisfiability solving with LLMs: a matched-pair evaluation. https://arxiv.org/abs/2605.28602 (c09, c10)
19. [V] Pan, Ganesh, Abernethy, Esposo, Lee (2025) Can transformers reason logically? https://arxiv.org/abs/2410.07432 (c11)
20. [V] Sun et al. (2024) AutoSAT. https://arxiv.org/abs/2402.10705 (c12)
21. [V] Sun et al. (2026) AutoModSAT. https://arxiv.org/abs/2507.22876 (c13)
22. [V] Chen and Li (2025) DaSAThco. https://arxiv.org/abs/2509.12602 (c14)
23. [V] Sarkar (2026) From errors to proofs. https://arxiv.org/abs/2608.14771 (c15)
24. [V] Salla, Amancherla, Saravanan (2026) Quantifying cross-query contradictions. https://arxiv.org/abs/2604.14525 (c16)

**LLM agents and failure memory**

25. [V] Shinn et al. (2023) Reflexion. https://arxiv.org/pdf/2303.11366 (b18, b19, c17, c18; a25 early partial pass)
26. [V] Huang et al. (2024) Large language models cannot self-correct reasoning yet. https://arxiv.org/pdf/2310.01798 (b20, c19; b20 table mapping corrected by critique)
27. [V] Ji, Lu, Zhang, Olukotun (2026) Sentry. https://arxiv.org/pdf/2610.02994 (b21 to b23, c21, c22; the 0.264 baseline label and the soft-repair figure are unverified)
28. [V] Cemri et al. (2025) Why do multi-agent LLM systems fail? https://arxiv.org/pdf/2503.13657 (b24)
29. [M] Zhu et al. (2025) Where LLM agents fail and how they can learn from failures (AgentDebug). https://arxiv.org/abs/2509.25370 (b25, c25; abstract only, numbers unverified)
30. [V] Bonagiri et al. (2026) CausalFlow. https://arxiv.org/abs/2605.25338 (c20)
31. [V] TIDE (2026) trajectory-based diagnostic evaluation of test-time improvement in LLM agents. https://arxiv.org/abs/2602.02196 (c23)
32. [V] An et al. (2024) TrialMaster. https://arxiv.org/abs/2404.07382 (c24)
33. [M] SciAgentGym, LLM-WikiRace, Robotouille loop metrics. https://arxiv.org/abs/2602.12984 (c26, snippets)
34. [V] Brown et al. (2024) Large language monkeys. https://arxiv.org/abs/2407.21787 (d06)
35. [V] Olausson et al. (2024) Is self-repair a silver bullet for code generation? https://arxiv.org/abs/2306.09896 (d07)
36. [V] Tyen et al. (2024) LLMs cannot find reasoning errors, but can correct them given the error location. https://arxiv.org/abs/2311.08516 (d08, d09)
37. [V] Kamoi et al. (2024) When can LLMs actually correct their own mistakes? https://arxiv.org/abs/2406.01297 (d10)
38. [V] Su et al. (2025) Mistake Notebook Learning. https://arxiv.org/abs/2512.11485 (d11, d12)
39. [V] Fang et al. (2026) Trajectory-informed memory generation for self-improving agent systems. https://arxiv.org/abs/2603.10600 (d13)
40. [V] Zhou et al. (2024) Language Agent Tree Search. https://arxiv.org/abs/2310.04406 (d14)
41. [V] Saad-Falcon et al. (2025) Shrinking the generation-verification gap with weak verifiers. https://arxiv.org/abs/2506.18203 (d15)
42. [M] Search record 2026-10-26 for formal no-good learning in LLM agents. https://www.alphaxiv.org/abs/2509.25370 (b26; not a source of findings)
