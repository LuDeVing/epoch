# Heuristic search and planning: synthesis

*One view across the field's researched subfields. Built from each subfield's DEEP.md, claims.jsonl and UNKNOWNS.md.*

Notes on use. "Established" means the claim's status in claims.jsonl. Contested and single-source claims are named only where they matter for a contradiction or a gap. Schema column checked against `research_notes/single_agent/SCHEMA.md` v0.2. Almost all evidence here comes from planning, SAT and CSP solvers, with a thin layer of LLM papers (many 2026 preprints read once). For the agent, an established claim is a design hint until tested on our model with a code check (SCHEMA section 8, rule 3). The field is only 2 of 11 subfields deep, so it says much about two ideas (relaxed scoring, restarts) and nothing yet about A*, MCTS, Tree of Thoughts, LATS, HTN or constraint propagation.

## 1. Coverage

| Subfield | DEEP.md | Claims | Established |
|---|---|---|---|
| 02 Heuristic design by relaxation | [DEEP](subfields/02_heuristics_by_relaxation/DEEP.md) | 31 | 9 |
| 11 Anytime search and restarts | [DEEP](subfields/11_anytime_search_and_restarts/DEEP.md) | 31 | 9 |
| **Total** | | **62** | **18** |

Contested: 5 (02: K07, K18; 11: K11, K20, K30). Single-source: 39 (two of them, C05.02-K25 and C05.11-K02, were downgraded by the source audit). Each subfield has a UNKNOWNS.md with 14 test rows (28 in all).

Not yet researched (from `subfields/SUBFIELDS.md`):

| Subfield | Why it matters for the schema |
|---|---|
| 01 Heuristic search (A*, best-first) | Control for ranking children at S6 |
| 03 Monte Carlo tree search | Explore vs exploit when growing the idea tree |
| 04 MCTS limits | Trap states; parameter count |
| 05 Tree of Thoughts | Idea tree at S6; its numbers rely on model self-evaluation |
| 06 Language Agent Tree Search | S6 with real feedback |
| 07 Automated planning (STRIPS, PDDL) | O5 work backwards |
| 08 Hierarchical task networks | O3 decompose; method library (subgoal library slot) |
| 09 Means-ends analysis | O5; subgoal choice |
| 10 Constraint satisfaction | O4, S4; propagation |

## 2. Established findings, merged

Schema column: yes (where) / partly / no.

| # | Finding | Claim ids | Schema part | In SCHEMA.md? |
|---|---|---|---|---|
| F1 | A cheap estimate from an easier version of the problem (ignore what an action undoes) ranks branches well enough to guide greedy search on most planning benchmarks. FF, built on it, won AIPS-2000; LAMA (FF heuristic plus landmarks) won the IPC-2008 sequential satisficing track; Fast Downward won the IPC-4 non-optimizing track using a causal-graph heuristic (later adding the FF heuristic and preferred operators). Under ideal h+, 24 of 30 domains have no unrecognised dead ends. | C05.02-K01 | O4, S3 | partly (O4 drop a constraint exists; no step that uses the relaxed result to rank children) |
| F2 | The relaxed estimate is blind to trouble caused by the constraint that was dropped. FF fails on fuel dead ends (Mystery, Mprime) and random restarts did not fix it; 6 of 30 domains have unrecognised dead ends. LeanPlan's generated heuristics were beaten by saturated cost partitioning on solved-task count in 4 of 10 IPC 2023 domains (only the Sokoban gap is tied to box interactions the relaxations ignore, and the paper says "presumably"); a dead-end test gave LeanPlan its largest single gain (Spanner). | C05.02-K02 | O4, G3 | partly (G3 says check on something not fitted to; no "dropped-constraint check" tied to O4) |
| F3 | A relaxed solution gives a free shortlist of next moves (FF helpful actions keep 40% down to 2% of successors; preferred operators helped in 15 domains vs hurt in 2 with multi-heuristic search). | C05.02-K03 | O4, S3 | no |
| F4 | Relaxation is weak where goal order matters. FF's Blocksworld results came from goal ordering, not relaxed distance. | C05.02-K04 | O4, S7 | no |
| F5 | Several different estimates beat one (multi-heuristic best in 23 of 29 domains; 5 sampled LLM heuristics gave the largest jump; portfolios 276 vs 234 of 400). Caveat inside the same claim: across nine LLMs the virtual best of five solved 131 of 139, the same as the best single model, so more models added no coverage on HTN. | C05.02-K05 | S3, S7, G4 | partly (G4 says samples from one model are correlated; no portfolio of unlike relaxations) |
| F6 | Writing the scorer as code and letting plain code run it beats asking the same model for the plan. 373 vs 174 solved (R1, 720 tasks) and 296 vs 19 (Flash). Thought of Search: model writes successor and goal test once, plain search solves all 1362 24-game problems vs about 75% for Tree of Thoughts. The code route needs fewer calls (200 vs 720); cost for 25 heuristics per domain was V3 $0.25 and R1 $6.12 vs $2.79 and $13.62 for end-to-end plans. | C05.02-K09, C05.02-K10 | G5, O4 | partly (G5 code selects; no "model writes the scorer" operator) |
| F7 | A model used directly as planner or step chooser is weak without a sound solver. GPT-4 Blocksworld 34.3%; Mystery 2 to 4.3%; o1-preview 97.8% falls to 52.8% (Mystery) and 23.6% on 20 to 40 step tasks. | C05.02-K14 | G5, G10 | yes (G5, G10, section 1) |
| F9 | Generated scorers often do not run. HTN: 361 of 780 rejected before testing; 72 of 419 deployed broke on every problem, 83% of those from the wrong state type. In evolved C++ heuristics 79.1% worked first time and 2.5% failed after four attempts. | C05.02-K30 | G2 | no (no smoke-test rule) |
| F10 | Restarts help only when the run-time distribution has a falling hazard (heavy tail or a mix of easy and hard runs). They are neutral for exponential (Weibull k=1) and harmful for increasing-hazard shapes (k>1). No heavy tail was found for blocks-world, local search (Walksat), unsolvable or easy instances; the only measured gain there was blocks-world 30 to 23 min. | C05.11-K01 | S0, S6, G12 | partly (G12 search only with a foothold; no per-family restart switch) |
| F11 | The best restart cutoff is far below the median run length and the cost curve is U-shaped (logistics.d: cutoff 16 backtracks mean cost 1,861 vs 307,550 at 128,000). For an LLM search loop the best fixed cutoff was 12 to 24 iterations. The headline speedups (multi-hour to minutes) rest on one lab's table and are in section 7 (C05.11-K02, single-source). | C05.11-K03 | S3, S6, G11 | partly (G11 prefers several short attempts; no cutoff rule) |
| F12 | Luby's universal schedule needs no knowledge of the distribution and stays within a log factor of the best fixed cutoff. Best of seven policies in a clause-learning SAT solver; 1.1 to 1.8 times the best cutoff on an LLM loop (unit 5); too small a unit (1) cost up to 2.8 times. Edge over a well-chosen fixed unit is small (180 vs 178 solved; 127 with no restarts). | C05.11-K04 | S6, G12 | no |
| F13 | Choosing the right sample is the bottleneck, not producing it. Majority vote and reward-model selection plateau (MATH Llama-3-8B 40.50 to 41.41% from 100 to 10,000 samples) while coverage keeps rising. | C05.11-K10 | G5, S7 | partly (G5 code selects; G12 says resample only with a foothold) |
| F14 | Continuing from one's own answer with a self-critique and no outside signal does not help and often hurts (GPT-4 GSM8K 95.5 to 89.0). It works when an oracle label, tool result or test is supplied. Unit-test feedback plus self-explanation still did not beat resampling at small budgets (GPT-4 APPS 1.05x, 0.97x). | C05.11-K12 | G2, S5 | yes (G2, 4b unstructured self-reflection) |
| F15 | In reasoning models a long single chain locks in early mistakes. Shorter chains within one question are more often right; several short independent paths beat one long path at the same tokens; stopping at the first finished chains cuts thinking tokens by up to 40%. | C05.11-K13 | G11, S3 | yes (G11 prefer several short independent attempts) |
| F16 | Forcing the model to continue ("Wait") gives small gains that flatten. s1-32B AIME24 went 50.0 to 53.3 with two Waits and 56.7 with the main budget-forcing setting, but MATH500 fell from 93.0 to 90.2 when the stop token was ignored with no string; GPT-4o on NaturalPlan peaks at a medium budget; R1 easy items 0.95 short vs 0.72 long. | C05.11-K15 | G11, S8 | partly (G11 cap reasoning length; no rule against forced extra rounds) |
| F17 | Modern clause-learning SAT solvers restart very often (most restarts before the 1000th conflict). Restart there means "reorder what is already learned" and unlimited restarts simulate general resolution; restart without memory is not the modern design. Analogy only. | C05.11-K22 | memory | no |
| F18 | Answer-agreement stopping is a validated code-only stop signal for how many attempts to run. Adaptive-Consistency cut samples up to 7.9x with under 0.1% accuracy drop (17 datasets); ESC 33.8% to 84.2%; DeepConf consensus stop saved 52.8% of tokens at threshold 0.95 (0.90 cost accuracy). Evidence is on math and QA, not ARC. | C05.11-K28 | G12, S3, S7 | no (G4 warns agreement is only a hint; this is a budget rule, not proof) |

F8 (model-written heuristics on never-released domains) was removed from this table after the source audit and is in section 7: all three papers behind it share an author, so C05.02-K25 is single-source. G7's expected size of gain therefore has no established support.

## 3. Contradictions between subfields

| # | Tension | Claims | Reading |
|---|---|---|---|
| X1 | More estimates or models help (F5) vs extra models add no coverage once the best is chosen. | C05.02-K05, C05.02-K27 (single-source) | Gain depends on estimate type and on selection, not count. Test unlike relaxations against same-kind samples (C05.02-U6). |
| X2 | Big gain from model-written scorers (373 vs 174) vs expected parity with the best generic method on new domains. | C05.02-K09, C05.02-K25 (single-source) | Not a true conflict. The 373 vs 174 compares against the model planning end to end; K25 compares against classical heuristics, but K25 is single-lab, so the parity side is a watch item, not an established finding. Do not credit the large gap to the relaxation step. |
| X3 | Restart with fresh attempts (F11, F15) vs refine the same answer. Refinement without an outside signal hurts (F14), yet one contested claim puts refine-with-check on the Pareto frontier at equal tokens and says parallel drafts mainly buy latency. | C05.11-K12, C05.11-K13, C05.11-K11 and C05.11-K30 (both contested) | Resolved only with an outside check: refine after a code check, restart otherwise. Stratify by difficulty (C05.11-U4). |
| X4 | Long chains lock in errors and shorter paths win (F15) vs reasoning models also switch lines of thought too often, and wrong answers carry about 418% more switch tokens. | C05.11-K13, C05.11-K14 (single-source) | Both may hold. Restart at attempt boundaries; commit within an attempt until a step is checked (C05.11-U12). |
| X5 | Forced continuation gives small gains (F16) vs "longer is not better" and a hump-shaped budget curve. | C05.11-K15 | One claim carries both; the net is a flat or humped curve. Stop when verified. |
| X6 | Luby is robust without knowing the distribution (F12) vs the best cutoff is far below the median and the U-shaped cost curve favours a tuned fixed cutoff; with mixed distributions and no per-run signal the best cutoff can be none. | C05.11-K04, C05.11-K03, C05.11-K06 (single-source) | Luby for unknown families, tuned cutoff once the hazard is measured. First measure the hazard (C05.11-U1). |
| X7 | Restart needs memory (CDCL clauses; recorded failures recover the cost) vs carrying unverified material anchors the next attempt (PDR summaries of wrong drafts). | C05.11-K22, C05.11-K20 (contested), C05.11-K26, C05.11-K27 (single-source) | Carry only verified failures. SCHEMA section 5 already shows lessons after the first attempt, never before. |
| X8 | Agreement stopping is a code-only budget rule (F18) vs SCHEMA G4: agreement is a hint, never proof; samples from one model are correlated. | C05.11-K28, C05.02-K05 | Use agreement to stop sampling, never to certify. Keep the code check or hold-out for the answer itself (G3). |
| X9 | Relaxation as a guide (F1) vs recall: part of the gain is memorised planning knowledge and shrinks to parity on obfuscated domains (R1 heuristic 66 solved on Obfuscated Blocksworld). | C05.02-K01, C05.02-K13 (single-source), C05.02-K25 (single-source) | Renamed-copy check before crediting the step (C05.02-U9). |
| X10 | With other fields. A01 F10 and A01 T8 (breadth over refinement; one long vs several short) agree with F14 and F15 and share a test with C05.11-U2. A01 section 6 bars model self-evaluation inside tree search; C05.02-K10 supports the same bar by showing code-once search beats Tree of Thoughts. A01 T7 lists sample disagreement as a doubt trigger; here agreement drives a stop. Same signal, two uses; run one test. | A01.09-K18, A01.02-K21, A01.05-K19, C05.02-K10, C05.11-K28 | No conflict, shared experiments. |

## 4. Recurring mechanisms

| Mechanism | Where it shows | What it means for the agent |
|---|---|---|
| **Easy version to rank the hard one** | 02-K01, K03, K09 (K25 single-source) | Solve a relaxed problem, then let code rank or shortlist the real children. Calibrate the rank against real test results per class (C05.02-U1). |
| **Whatever you drop comes back as a dead end** | 02-K02, K04, K30 | Every relaxed score carries a must-recheck field for the dropped constraint, and every generated scorer gets a smoke test. |
| **Code runs the scorer, model writes it** | 02-K09, K10, K14, K30 | The model supplies a function once; plain code applies it to all children. Charge writing, smoke test and repair to the budget. |
| **Selection is the bottleneck, not generation** | 11-K10, 11-K12, 02-K05 | Coverage keeps rising with samples; vote and judges plateau. Gains follow verifier quality. Same as A01 F10. |
| **Falling hazard decides whether restart pays** | 11-K01, K03, K04 (K02 single-source) | Measure the run-time curve per family before turning restart on. Use a cutoff well below the median solved length. |
| **Fresh start beats a long wrong chain** | 11-K13, 11-K12, 11-K15 | Cap attempt length; do not force more rounds; refine only on real output. |
| **Memory across restarts reorders, not repeats** | 11-K22 (analogy), 11-K20, K26, K27 (not established) | Carry verified facts only. |
| **Agreement as a cheap stop** | 11-K28, 02-K05 | Stop sampling when answers repeat; never accept on agreement alone (G4). |
| **Parity on new domains** | 02-K25, 02-K13 (both single-source, not established) | Possible parity with the best generic method; test on unreleased or renamed variants before relying on it. |
| **Equal-token accounting has a CPU side** | 02-K09 (cost row), 02-K30 | Count the model-written code's discard rate, repair calls and any search time as cost. |

## 5. Merged tests

Each row merges UNKNOWNS rows that share one design.

| # | Merged test | Unknown ids covered | One-line design | Priority |
|---|---|---|---|---|
| T1 | **Hazard and attempt length** | C05.11-U1, C05.11-U10, C05.11-U11, C05.11-U13 | 30+ fresh attempts per item on 20 ARC and 20 BrainTeaser items with a code verifier; fit survival curve over tokens, sweep length at 0.25x to 2x median solved length, force answers at 25/50/75/100% of budget; reuse as labels for a difficulty router. Gates T2, T3, T4. | High |
| T2 | **One long vs k short vs Luby** | C05.11-U2, C05.11-U12 | Equal total tokens: one long, k=4 short, Luby (unit = median solved length), long + Wait rounds; add a no-switch-before-check rule arm. Paired bootstrap. | High |
| T3 | **What crosses a restart** | C05.11-U3, C05.11-U9 | Carry nothing vs code-verified failure note vs prior answer; measure solved share and repeat-wrong-answer rate; then pick K=2 to 4 candidates by a validation slice. | High |
| T4 | **Refine with check vs fresh restart** | C05.11-U4 | Self-critique only vs refine with code check vs fresh restart vs one revision then fresh; stratify by first-attempt margin. | High |
| T5 | **Stop and abort triggers** | C05.11-U5, C05.11-U6, C05.11-U8 | Fixed 4 attempts vs stop at 2 matching code-checked answers in the first 3; code-only abort features (repeated tool error, no new verified fact) vs model-made pivot verdict; AUC and tokens per solve. | High (U6), Med (rest) |
| T6 | **Budget visibility** | C05.11-U7 | Counter hidden vs shown with restarts allowed in both; watch solved share and give-up before the first failed check. | Med |
| T7 | **Relaxed rank predicts real result** | C05.02-U1, C05.02-U2, C05.02-U6 | 100+ items, 4 to 8 children each: code-ranked by relaxed score vs model-rated vs random order; code-enumerated constraint drops vs model pick; 2 to 3 unlike relaxations vs same-kind samples. Spearman rho per class and top-1 pass rate. | High |
| T8 | **Dropped-constraint must-pass and verified subgoal** | C05.02-U3, C05.02-U10 | Dead-end plus reversible items; relaxed score with must-pass list vs without; model-proposed must-hold subgoal checked by code vs unverified. Rate of high-scored children that fail. | High |
| T9 | **Scorer in code with acceptance rule** | C05.02-U4, C05.02-U7 | Model writes scorer, code ranks all children vs model rates each child vs direct answer; accept by property-plus-repair vs best of 5 vs smoke-test filter; all costs charged. Needs a text-item generator (section 7). | High |
| T10 | **Shortlist and commit rules** | C05.02-U5, C05.02-U11, C05.02-U12 | Expand only branches the relaxed solve starts with (fall back to all) vs all vs random subset; recompute after each step vs once; commit on first better child with 2-step widen. | Med |
| T11 | **Recall check on relaxed solves** | C05.02-U9 | Original vs renamed copy of each item, flag disagreement; AUC of flag for real failure. Run on every model we use. | Med |
| T12 | **Relaxation prompt template** | C05.02-U8, C05.02-U14, C05.02-U13 | Same-class worked relaxation example vs none vs other-class; signalled step-back vs always vs never; goal-order check vs rank only on order-dependent items. | Low |
| T13 | **Foundations read** | C05.11-U14 | Read Zilberstein, Dean and Boddy, Korf, Luby 1993; correct wording of anytime properties and constants. | Low |

Order to run: T1 first (it sets the unit and cutoff for T2 to T4 and supplies difficulty labels), then T2, T7 and T8 (the two central questions of each subfield, and T8 is the cheapest), then T3, T4, T5, T9.

## 6. Not to add

| Idea | Why not | Claim ids |
|---|---|---|
| Restart or resample on every task family | Neutral or harmful when there is no falling hazard (no heavy tail found in blocks-world, local search, easy and unsolvable instances; the only measured gain was blocks-world 30 to 23 min) | C05.11-K01 |
| Self-critique continuation with no outside signal, as a doubt or restart step | Lowered accuracy (GPT-4 GSM8K 95.5 to 89.0; CommonSenseQA 75.8 to 41.8); SCHEMA 4b already bars it | C05.11-K12 |
| Forced extra rounds ("Wait") as a default | Small, flat gains; hump-shaped budget curve; easy items worse with long traces | C05.11-K15 |
| Majority vote or model reward at larger N as the way to use more samples | Plateau while coverage rises; use a code or tool verifier | C05.11-K10 |
| Letting the model alone certify a relaxed or full plan | Weak without a sound checker (Blocksworld 34.3%; Mystery 2 to 4.3%) | C05.02-K14 |
| Crediting the relaxation step with the 373 vs 174 gap | That gap is against end-to-end model plans; against classical heuristics the gain is parity (single-source, one lab) | C05.02-K09, C05.02-K25 (single-source) |
| Using a relaxed score as the only ranker on classes with use-once resources or one-way choices | Dead ends are invisible to it | C05.02-K02 |
| Ranking with an unseen, unsmoke-tested model-written scorer | Many do not run (361 of 780 rejected; 72 of 419 broke on every problem) | C05.02-K30 |
| Adding more models for coverage on the assumption that coverage adds | Virtual best of five equalled best single model on HTN | C05.02-K05 (caveat), C05.02-K27 |
| Model self-evaluation inside a search tree | Conflicts with G5; code-once search beat Tree of Thoughts | C05.02-K10 (also A01.05-K19) |
| Sharing unverified summaries or answers across restarts | Not established either way, and flagged by the contested and single-source claims; carry only verified failures | C05.11-K20 (contested), C05.11-K27 (single-source) |
| Tight fixed token cutoff with unit 1 or a tiny unit | Cost up to 2.8x the best cutoff; success per try near zero | C05.11-K04, C05.11-K03 |

## 7. Gaps

- **Nine of eleven subfields are unresearched** (section 1). Nothing here covers A*, MCTS, Tree of Thoughts, LATS, HTN, means-ends analysis or constraint propagation. The S6 tree rules in SCHEMA section 4 (at most 3 children, depth 2, 2 expansions) therefore rest on no research from this field.
- **No direct paper measures** whether a model's own relaxed solve ranks real children (C05.02-K22, single-source). The hardest question in the field is open (T7).
- **Text transfer is untested.** All scorer-writing, shortlist and dead-end evidence is in PDDL or executable domains. There is no bench of text items with code-checkable constraints, no labelled dead-end set (30 items proposed), and no property for free-text scorers.
- **No LLM hazard data.** Whether an LLM attempt's chance of finishing per token falls over time is inferred from indirect results (C05.11-K24, K25, single-source). T1 is the only way to fill it. Independence of attempts at one temperature is unknown.
- **Restart and refine evidence is old or narrow.** The only direct LLM Luby test is one steel-rolling loop, one model, one campaign (C05.11-K18, K19, single-source). Refinement vs restart data is from 2023-era models and unit tests (C05.11-K11, K30 contested).
- **Early-signal methods need logprobs.** The windowed confidence stop (C05.11-K29, single-source) needs token log-probabilities the harness does not log. Only code-only features can be tested now.
- **The pivot verdict is model-made.** BATS gains (C05.11-K17, single-source) come from a model decision, which conflicts with the rule that code decides. Test the code-rule version first (T5).
- **Many 2026 preprints were read once and not replicated:** LeanPlan, HTN heuristics, Gestrin and Seipp, property-guided synthesis, LM-Landmarks (abstract only), Conformal Thinking, the steel paper.
- **Equal-token accounting has a CPU side** (206 CPU-hours per domain in the planning papers). Logs must keep write, smoke test, repair, selection and relaxed-solve costs in separate columns.
- **Primary texts unread:** Pearl 1984, Culberson and Schaeffer 1998, Bonet and Geffner 2001, Hoffmann et al. 2004, Zilberstein, Dean and Boddy, Korf, Luby 1993.
- **Single lab only:** model-written heuristics stay competitive on never-released domains (LeanPlan 67 vs 51 solved on 3 new domains; Gestrin and Seipp 368 vs 352 of 720; Correa Rod-Rings 58 vs hFF 59), but all three papers share an author (C05.02-K25). Randomised restarts with a small cutoff turn multi-hour or unsolved structured instances into minutes (logistics.d 108 min to 95 s; 3bit-adder-32 over 24 h to 165 s), but every usable source is one lab's table (C05.11-K02).
- **Single-source items worth watching:** landmarks added to an FF-style estimate (C05.02-K06), example heuristics in the prompt essential (C05.02-K11), best-of-N selection by training score is lossy (C05.02-K12), visible budget helps a web agent (C05.11-K16) but is not monotone safe (C05.11-K31), restart plus a recorded failure set (C05.11-K26).

**Source audit, 2026-10-26:** the papers behind all 20 claims that were established were re-opened. 14 confirmed, 4 reworded (C05.02-K01, C05.02-K02, C05.11-K01, C05.11-K15) and 2 downgraded to single-source (C05.02-K25, C05.11-K02). Established now: 18 (9 per subfield). The downgraded ids are removed from section 2 and listed in section 7.
