# Problem-solving research: synthesis

*One view across the field's researched subfields. Built from each subfield's DEEP.md, claims.jsonl and UNKNOWNS.md.*

Notes on use. "Established" means the claim's status in claims.jsonl after the source audit of 2026-10-26 (independence re-check and wording check). Rows were edited to match the current claim wording. Contested, single-source, hypothesis and open claims are named only where they matter for a contradiction or a gap. Schema column checked against `research_notes/single_agent/SCHEMA.md` (guardrails G1 to G12, states S0 to S9, operators O1 to O8, section 4b). Most findings here come from LLM benchmarks, not people, so they are direct hints for the agent, but mostly from 2023-25 models. Run them again on the model we ship.

## 1. Coverage

| Subfield | DEEP.md | Claims | Established |
|---|---|---|---|
| 01 Problem-space theory | [DEEP](subfields/01_problem_space_theory/DEEP.md) | 43 | 8 |
| 02 Means-ends analysis | [DEEP](subfields/02_means_ends_analysis/DEEP.md) | 34 (+1 hypothesis, 2 open) | 4 |
| 04 Problem solving strategies and the problem-solving cycle | [DEEP](subfields/04_problem_solving_strategies_and_cycle/DEEP.md) | 37 | 13 |
| **Total** | | **114** | **25** |

Single-source claims: 71. Contested: 15. Unknown rows: 16 (01), 15 (02), 17 (04), 48 in all.

**Not yet researched** (no folder or no DEEP.md), from SUBFIELDS.md:

| # | Subfield | Why it matters |
|---|---|---|
| 03 | Impasse-driven subgoaling and chunking (Soar) | Direct source for S6 and the subgoal library. Most important gap. |
| 05 | Representational change theory | Source for O4 and O6. |
| 06 | Gestalt insight and the "sudden insight" debate | Background; restructuring as operator. |
| 07 | Progress monitoring | Source for the S6 no-progress trigger. |
| 08 | Analogical problem solving | Source for O7. |
| 09 | Mathematical problem solving and heuristic method (Polya, Schoenfeld) | Source for O1 to O5 and S6 control. |

Note: the status table in SUBFIELDS.md still says "not started" for means-ends analysis and for strategies and the cycle. Both are done. Not edited here.

## 2. Established findings, merged

Only status "established". Duplicates merged.

| # | Finding | Claim ids | Schema part | In SCHEMA.md? |
|---|---|---|---|---|
| F1 | Means-ends search scales badly because of combinatorial blow-up, and the original authors concede the theory behind these search methods is thin. (The rest of the earlier F1, that blind search is hopeless, that difference reduction needs a hand-written difference table, that people switch to abstract planning bursts and that selectivity costs completeness, now rests on single-source claims; see section 7. Schema conclusion weakened: the G12/S3 "selectivity costs completeness" point and the loop-guard advice in section 4 have no established claim behind them.) | A02.02-K04 | G12, S3 | partly (G12 search only where there is a foothold) |
| F4 | Tree search over model-generated steps beats plain chains by a large margin on tasks with a checkable step state and a weak baseline (Game of 24 4% to 74%). The gain is conditional. It is small where the model is already good, small against strong voting, and it can hurt on easy items. It helps on mid-difficulty items. A cheap first pass can gate it. | A02.01-K03, A02.01-K04, A02.01-K37 | G12, O3, S4 | yes (G12 grow the tree only with a foothold; O3 decompose; difficulty allocation) |
| F5 | The evaluator matters. On Game of 24, generating ideas, not judging them, is the bottleneck (GPT-4 generating with GPT-3.5 evaluating 64%, reverse 31%; the ToT authors word it as "suggests", one appendix experiment). In a small open-model re-run (Stanford course project, about 99 problems) a fine-tuned value function raised BFS-1 from 18.2% to 47.5% and cut the BFS-1 vs BFS-5 gap from about 48 to about 16 points: it narrows the gap, it does not nearly close it. LATS on HotPotQA drops from 0.63 to 0.37 without the LM value heuristic. | A02.01-K07, A02.04-K18 | S4, G5 | partly (G5 code selects; no rule that the evaluator is tested on its own) |
| F6 | A model checking its own progress without a sound outside signal is unreliable: GPT-4 as verifier missed 20.7% to 97.1% of wrong plans; intrinsic self-correction lowered GPT-3.5 CommonSenseQA from 75.8 to 38.1. A fine-tuned 7B detector found wrong steps (precision 90.5%, recall 99.2%) but validity did not improve. The accuracy a checker needs is not measured. (The positive half, that an external sound verifier in a generate-test loop works, is single lab; see section 7. Schema conclusion weakened: G2, G3, G5, G10 stay supported as "do not trust self-judgement", not as "an external verifier loop is proven".) | A02.02-K31 | G2, G3, G5, G10 | yes (G2, G3, G5, G10; 4b unstructured self-reflection) |
| F7 | Plain repeated sampling is a strong baseline whenever an automatic checker exists (coverage rises log-linearly with samples). Without a checker, voting and reward models plateau. A cheap model in a verifier loop can match a reasoning model for less money. | A02.01-K22 | G3, G11, G12, S3, S4 | yes (G11 several short attempts; G12; S3 independent attempts) |
| F8 | Step-by-step text helps mostly on symbolic, math and logical tasks (average gain 14.2 / 12.3 / 6.9 points respectively) and barely elsewhere (56.8 vs 56.1). Blocksworld CoT gains come from prompts matched to the problem class and shrink as instances grow past the examples. Thinking-heavy modes waste many tokens on easy items. Plain CoT adds little (about +3 to -3 points) for reasoning models, at 20 to 80% more time. Decomposition-style prompting was tested on a reasoning model only via Plan-Execute on GPT-5; abstraction and analogy prompts were not found tested. A solver or tool beats CoT on symbolic work. | A02.01-K23, A02.04-K12, A02.04-K35 | G1, G11, G12, S0 | yes (G11, G12) |
| F9 | Hanoi difficulty tracks the length to the first subgoal and the representation, not only total length. Solution length is not a reliable difficulty predictor: in the Chinese Ring Puzzle starting 21 vs 31 moves out gave no reliable time difference, solvers show long unproductive stretches then a fast run, and a misleading progress heuristic traps them; across transport puzzles length predicts human difficulty well for Rush Hour (Spearman 0.90) but poorly for Sokoban (0.41) and Replacement (0.21). (The isomorph result, 2:1 to 16:1 differences from move representation with legality-test cost as the driver, is single lab; see section 7. Schema conclusion weakened: O6 "change representation" now rests on A02.02-K08 alone.) | A02.01-K26, A02.02-K08 | S1, S2, O6, G12 | partly (O6 change representation; G12 allocates by difficulty but no rule about what predicts difficulty) |
| F10 | Several different strategies (goal recursion, perceptual, rote move pattern) solve the same Tower of Hanoi problem, and correct solutions can hide very different strategies. A rote strategy memorised for four disks does not transfer to five. Strong solvers keep a repertoire and pick by problem type. | A02.01-K28, A02.04-K03 | O1 to O8 | partly (operator table is a repertoire; no strategy-identity logging beyond "operators tried") |
| F11 | People's strategy choices track learned success rates; at group level close to probability matching in the Building Sticks Task, though many individuals overmatch. Simple reinforcement and Bayesian success-estimate models fit, with adaptation to environment changes sometimes slow. | A02.04-K01 | S0, memory class record | partly (class record kept in code, read by S0; it records operators that solved subgoals, not per-strategy success rates) |
| F12 | No single prompting strategy wins across datasets or sizes. A per-item oracle is far above the best fixed strategy. The model choosing its own strategy, or voting or verifying across strategies, recovers only part of that gap. A learned router recovers about a quarter of it, mostly as a cost saving. The oracle counts one lucky run per paradigm, so the true gap is smaller. | A02.04-K09, A02.04-K10, A02.04-K30 | S0, S6 routing | partly (S0 chooses a mode; G4 bars strategy voters; no strategy router) |
| F13 | Cheap-first with escalation on low answer consistency, or learned routing, cuts tokens or cost at equal accuracy (46 to 85% in one study, over 60% in another). Thinking models also cut effort near collapse. | A02.04-K11, A02.04-K12 | G11, G12, S0 | partly (G12; escalation by agreement is a hint under G4, untested for us) |
| F14 | A persistent per-task-type record of what worked helps when a small outside controller reads it (LIMBO bandit: comparable or better accuracy than the strongest fixed baseline at up to 83% lower inference cost, 53% on average; MemCon bandit on GPT-4.1-mini: +2.6 to +4.2 points over G-Memory on the six-benchmark mean, 10.9-24.1% lower token cost). No test of the LLM reading its own strategy table was found. (The earlier claim that LLMs given raw history do not explore well in context is not in the current wording of this claim.) | A02.04-K36 | memory class record, S0 | partly (class record exists, read by S0 in code; the LLM-reads-it case is not tested) |
| F15 | Pure difference reduction fails on conjunctive goals when one goal clobbers another (Sussman anomaly, taxi case). Fixes: goal protection, a final all-goals check, interleaving. | A02.02-K03 | S8, G | no (S8 checks the answer on the unfitted part; no all-goals recheck rule) |
| F19 | Having the right strategy does not guarantee success. Execution errors dominate (74.7% of Self-Discover MATH failures). The error mix depends on method (Plan-and-Solve: misunderstanding 27%, calculation 7%). | A02.04-K15 | S8, G2 | partly (S8 verify; no execution-vs-strategy split in the log) |
| F20 | LLM agents explore hidden-rule (Blicket) tasks poorly and prefer OR over AND rules. Sampling many distinct hypotheses and choosing actions that eliminate them removes the OR bias at high sample counts in the 8-object setting. In a rule-switch variant a typed scaffold alone scored numerically lower than base (77.3% vs 87.3%, not significant, p=0.077) and scaffold plus monitor scored 89.1% (p=0.015 vs scaffold alone). (The human VOTAT result is single source; see section 7.) | A02.04-K27 | S2, S7, O (hypothesis test), G7 | partly (S2 candidate rules; S7 discriminating test; no explicit hypothesis-elimination loop) |
| F21 | Long-horizon runs derail in stereotyped ways: meltdown loops after one wrong belief, idle drift, repeated unchecked actions. Failure depends on model and horizon (one strong model without reasoning beat human trajectories). | A02.04-K33 | monitor, S6 trigger | no (S6 fires on no pass, repeated error or budget; no no-op counter or belief-vs-observation check) |

Note: F1 now holds only A02.02-K04 (background; the authors concede the search theory is thin). F2, F3, F16, F17 and F18 were removed from this section when their claims became single-source (section 7). Row numbers are kept as they were.

## 3. Contradictions between subfields

| # | Where the sources disagree | How to resolve |
|---|---|---|
| C1 | **Does tree search beat plain sampling?** For: A02.01-K03 (Game of 24 74% vs 4%). Against or small: A02.01-K04, A02.01-K22, A02.01-K37, contested A02.01-K35 (naive MCTS lost to sampling at every budget; a budget-aware tree won with about 7x less compute). The big wins come against weak baselines (plain CoT, not voting). | Do not add the tree on the strength of the 74%. Test against best-of-N with the same checker at equal dollars, by difficulty bin (T1). Keep G12 until then. |
| C2 | **Strategy routing against SCHEMA G4.** A02.04-K09, K10, K30 say a per-item oracle is far above any fixed strategy and routing saves cost. G4 says no persona or strategy voters on single-answer problems. A02.04-K10 shows that voting across strategies recovers only a fraction. | Not a real conflict. G4 bars voting across strategies. Routing by class record, in code, is a different thing. The gain may be mostly cost, not accuracy (A02.04-K30). Decide with T3. |
| C3 | **Is explicit structure good?** A02.01-K02 (single-source now, not in section 2) says explicit objects match the theory. Contested A02.04-K14 says self-composed JSON structures lost to free text on MATH (75.5 vs 63.5) but won on BBH. A02.04-K27 says a typed scaffold alone scored numerically lower (77.3% vs 87.3%, not significant). | Task and format dependent. Keep structure in code for state, goal test and ledger (design choice; the supporting claims A02.01-K11 and A02.02-K26 are single-source now). Let the plan itself be free text until T9 says otherwise. |
| C4 | **The Hanoi / River Crossing "collapse".** A02.01-K32 says collapse appears across frontier models. Contested A02.01-K15 and contested A02.02-K21 say it is partly output length and impossible instances; code output restores accuracy. A02.01-K16, contested A02.02-K22 and established A02.04-K15 say giving the algorithm did not move the collapse point. | Both hold in part. Failure past a size threshold looks like execution and state loss, not strategy finding. Test with code-held state (T5). Do not use these papers as proof either way. |
| C5 | **Decompose always or only after failure?** A02.02-K33 (open) lists positive transfer for explicit decomposition (ADaPT, LAMBADA, MEDAKA) and negative or null results (Goal CoT hurt out of distribution). A02.04-K35 says decomposition, abstraction and analogy are untested on reasoning models. SCHEMA O3 and G1 allow decomposition only at an impasse. | Open. T7 decides with the failure-triggered rule against always-decompose. |
| C6 | **Does the scaffold help strong models?** Contested A02.01-K08 says the gain depends on the model (19% vs 74% for the same method). A02.04-K35 shows CoT adds almost nothing for reasoning models. A02.02-U1 asks whether the MEA scaffold still wins when thinking is on. A02.01-K13 (contested) mental-then-external transfer is borderline. | Gate by class pass rate and measure on the deployment model (T3, T4, T13). Every element must pay at equal tokens (G7). |
| C7 | **Impasse as a trigger.** A02.01-K21 (contested) says an impasse alone does not give insight; representational change is a rival. A02.01-U9 and G1 treat impasse as the trigger for escalation. A02.04-K11 uses answer inconsistency. | Different questions: when to escalate vs what to do next. T2 compares triggers. Subfield 03 (not researched) should supply the Soar definition. |
| C8 | **Cross-field: A01 C11 and F10 vs here.** A01 says tree search with model self-evaluation conflicts with G5. Here A02.01-K07 says the evaluator matters, and A02.02-K31 (with single-source A02.01-K09) says the model judges itself badly. | Consistent. Move scoring to code or a separately tested evaluator (T1 arm). |
| C9 | **Cross-field: A01 F9 and F10 vs A02.04-K35.** A01 says thinking models falsify more and solve more rule games, and breadth beats refinement. A02.04-K35 says CoT adds little for reasoning models. | Not a conflict if thinking is spent on hypothesis search. Per class tests (A01 T8 and T13 here). |
| C10 | **Cross-field: A01 F23 and C5 vs A02.01-K11.** A01 says a solver after LLM translation is a gated tie-break because extraction errors lean to "invalid". A02.01-K11 (single-source now, IBM group only) says model-written code operators solve rule sets at 100%, but all tested domains had exact short rules. | Same lesson, but the A02.01-K11 side is single-source. Code search is plausibly safe where rules are exact. Add a parse and test check on the code (T5). |

## 4. Recurring mechanisms

| Mechanism | Subfields and claims | What it means for the agent |
|---|---|---|
| **Code holds state and judges; the model fills slots** | 01 (A02.01-K09, K11; both single-source), 02 (A02.02-K01, K26; single-source; K31 established), 04 (A02.04-K36) | The most repeated result, but now mostly single-source; only K31 and K36 are established. State, goal test, ledger, success table and verifier are code. The model proposes steps and names differences. |
| **Generation is the bottleneck; the evaluator must be tested alone** | 01 (A02.01-K07), 04 (A02.04-K18; one appendix experiment), cf. A01 F10 | Spend tokens on diverse proposals. Test the evaluator before the tree. |
| **Gain depends on difficulty and baseline** | 01 (A02.01-K04, K37, K22), 04 (A02.04-K11, K12, K35) | Search and long reasoning help mid-difficulty items, do nothing on easy ones and little for reasoning models. Cheap pass first. |
| **Representation sets difficulty** | 01 (A02.01-K26; K25 single-source), 02 (A02.02-K08; K24 single-source) | Same logic, different cost. Obfuscated names break pattern matching. Offer a second encoding and test on a renamed copy. |
| **Own progress checks are unreliable** | 02 (A02.02-K31), 01 (A02.01-K09, single-source), 04 (A02.04-K15) | Never let the model judge subgoal progress without a sound signal. Execution errors outweigh strategy errors. |
| **Strategy is a distribution, not a choice** | 01 (A02.01-K28), 04 (A02.04-K01, K03, K09, K10, K30, K36) | No fixed best strategy. Routing is worth testing for cost first, accuracy second, and it needs a code-held record. |
| **Conjunctive goals and long procedures fail by lost state** | 02 (A02.02-K03; K26 single-source), 01 (A02.01-K32 contested), 04 (A02.04-K33) | A ledger the code re-computes, a final all-goals check and loop or no-op monitors address the same failure. |
| **Selective search loses completeness** | 01 (A02.01-K29, single-source), 02 (A02.02-K04) | Keep a visited-state guard and an escape move (reset or detour) so greedy reduction does not trap the run. |

## 5. Merged tests

Each row merges UNKNOWNS rows that share one design.

| # | Merged test | Unknown ids covered | One-line design | Priority |
|---|---|---|---|---|
| T1 | **Search vs sampling vs evaluator, with a coded checker** | A02.01-U1, A02.01-U2, A02.01-U7, A02.01-U12, A02.01-U14, A02.01-U15 | 100 checkable items binned easy/mid/hard: best-of-N, generate-test-repair (2 rounds), tree with same checker, resample plus same evaluator, tree plus random evaluator; add prune and backtrack ablations, state dedupe and a one-prompt trace only if the tree wins. Run on the deployment model in both roles. Metric: solved at fixed tokens and dollars. | High |
| T2 | **Cheap-pass gate and escalation trigger** | A02.01-U3, A02.01-U9, A02.01-U13, A02.04-U2, A02.04-U3 | Cheap pass first; escalate on failed check, impasse signal, 2 to 3 sample disagreement or stated confidence, against always-search and 6-sample majority at a token cap. Also compare predicting difficulty from cheap pass rate vs path length. | High |
| T3 | **Strategy router, success table and capability gate** | A02.04-U1, A02.04-U4, A02.04-U5, A02.04-U6, A02.04-U16, A02.02-U11, A02.02-U12 | First measure the repeat-corrected gap to a per-item oracle (go on only if 8 or more points). Then a code-held per-class success table shown as a summary, a rolling "best changed?" monitor after a silent shift, operators on demand vs fixed script, fail message that names the method class, and a gate that turns the scaffold off when a class pass rate is low. | High |
| T4 | **Means-ends scaffold: which part pays** | A02.02-U1, A02.02-U2, A02.02-U7, A02.02-U8, A02.02-U15, A02.01-U8 | Plain vs scaffold with code-held goal stack and ledger, with thinking on and off; drop one part at a time (ledger, stack, difference naming, calculation hint); forward vs flipped vs backward; vague or wrong difference hints; code difference count vs model distance estimate. | High |
| T5 | **Code-held state and code search for long procedures** | A02.01-U5, A02.01-U6, A02.02-U9, A02.02-U10 | Hanoi-like and rule-based items at growing size: whole plan vs one move per call with code state; model-written successor and goal test with a repair loop vs prompted search; with and without the algorithm in the prompt. Splits strategy-finding from execution. Note: the model-written successor function arm rested only on single-source claims (A02.01-K11, A02.02-K01); the audit leaves it without an established claim, so it is a hypothesis test. | High |
| T6 | **Goal clobbering and ledger check** | A02.02-U3, A02.02-U6, A02.02-U13 | Multi-goal items: count clobbered sibling goals with no check; add a code-run all-goals recheck; compare ledger-recomputed subgoal status with model-judged status and plain resampling; prune incompatible subgoal pairs in code. | High |
| T7 | **Decompose on failure, detour rule, thinking-model operators** | A02.02-U4, A02.02-U5 | On-failure decompose (depth cap 3) vs always vs none; three-trigger non-greedy move rule (loop, constraint conflict, no reducing operator) vs pure reduction; count repeated states. | High |
| T8 | **Encoding, restructure and fixation check** | A02.01-U4, A02.01-U11, A02.04-U11 | Second encoding in a fresh context, one or two worked moves, a code legality check; forced restructure operator or harvest-every-candidate check on insight items; an alternative-frame check after a failed approach. Test on a renamed copy. | Med |
| T9 | **Plan format and abstraction** | A02.01-U10, A02.04-U8, A02.02-U14, A02.04-U14 | Plan-abstract-then-fill vs flat steps on 6+ step tasks; shared task-level plan vs per-instance free text vs JSON; false-plan rate of abstract plans; a one-line progress report with a code decision rule. | Med |
| T10 | **Analogy retrieval and order** | A02.04-U9, A02.04-U10 | List similar solved problems from a real memory before solving; attempt first then retrieve method vs retrieve first, on transfer and standard items. | Med |
| T11 | **Hypothesis list with probe selection** | A02.04-U13 | Hidden-rule tasks: free exploration vs hypothesis list with elimination probes, with and without a monitor. | Med |
| T12 | **Long-horizon monitors** | A02.04-U12 | Simulation runs: no-op counter, repeated-action detector and belief-vs-observation check vs none; derailments and final value. | Med |
| T13 | **Do operators help a thinking model?** | A02.04-U7, A02.04-U15, A02.04-U17, A02.01-U16 | Decompose, abstract and analogy prompts, a direct-answer option, backward verification and forced explain-each-step on a reasoning model; report fixes vs breaks. | High |

Order: T1 and T2 first (they decide whether search and escalation stay). T13 and T3 next (they test whether anything survives on a thinking model). T4 to T7 follow. T8 to T12 only if their classes show up in the logs.

## 6. Not to add

| Idea | Why not | Claim ids |
|---|---|---|
| A tree search added on the Game of 24 result alone | Large gains are against weak baselines; small against voting; can hurt on easy items | A02.01-K03, A02.01-K04, A02.01-K37 |
| Model-written verdicts on its own progress or plan validity | False-negative rates up to 97% (GPT-4 as verifier); self-correction lowered CommonSenseQA 75.8 to 38.1 | A02.02-K31 (A02.01-K09 single-source) |
| Model-estimated distance to goal as a progress signal | No support; a misleading progress heuristic trapped solvers in the Chinese Ring Puzzle. A code difference count is the candidate (A02.02-U15) | A02.01-K26 |
| Pure means-ends (greedy difference reduction) with no loop guard | Fails on conjunctive goals and needs a hand-written difference table | A02.02-K03 (hand-written difference table: A02.01-K29, single-source) |
| Giving the algorithm in the prompt as the fix for long procedures | Did not move the collapse point; execution is the failure | A02.04-K15, A02.01-K16 (contested) |
| Letting the model pick its strategy, or voting across strategies | Recovers only a fraction of the oracle gap; also conflicts with G4 | A02.04-K10, A02.04-K09 |
| Plain CoT as the default for reasoning models | Adds about zero at 20 to 80% more time | A02.04-K35 |
| Raw strategy history in the prompt as the strategy chooser | No established claim shows raw history failing (A02.04-K36 supports only the external controller); keep the summary in code as a design choice | A02.04-K36 |
| Using state-space size or solution length alone to allocate budget | Does not reliably set difficulty: good predictor for Rush Hour, poor for Sokoban and Replacement | A02.01-K26, A02.02-K08 |
| Mental-then-external transfer as a design basis | Borderline and absent in the first experiment | A02.01-K13 (contested) |
| Treating the Hanoi "collapse" papers as proof about reasoning | Partly output limits and impossible instances | A02.01-K15, A02.02-K21 (contested) |
| Intelligence correlation of complex problem solving as a design basis | Human individual-difference result; critique reports near-vanishing correlations | A02.04-K23 (contested) |

## 7. Gaps

- **Single lab or single source only (moved from section 2):**
  - single source only: a problem is states plus operators plus a goal test, and a scaffold making these explicit objects matches the theory (A02.01-K02). Was F2.
  - single lab only: writing the successor function and goal test once as code, then running ordinary search, solves rule-based sets at about 100% in few LLM calls, far cheaper than LLM-in-the-loop search (costs are estimates); first-try code needed 1.2 to 2.8 tries with GPT-4 (A02.01-K11, A02.02-K01; K11 is one IBM group and its follow-up; K01 had one opened source). Was F3.
  - single lab only: an external sound verifier in a generate-test loop works (Blocksworld 82% with VAL back-prompting), and graph colouring went 1 of 100 under self-critique vs 16% baseline; only the GSM8K 75.9 to 74.7 result is independent (A02.01-K09, Kambhampati group). Part of F6.
  - single lab only: selective search loses completeness, MATER branching about 20 to 2, waypoints cut b^L to k*b^(L/k); the Planning GPS and hand-written difference-table half could not be checked, and all sources are Newell/Simon work (A02.01-K29, also A02.01-K01). Was part of F1.
  - single lab only: isomorph difficulty 2:1 to 16:1, Chinese Ring vs digital isomorph 79.7 vs 13-20 minutes; legality-testing cost as the driver (A02.01-K25, Kotovsky programme). Part of F9.
  - single lab only: GPT-4-class models solve about a third of Blocksworld plans, 2-5% obfuscated; o1-preview 97.8% plain, 52.8% Mystery, 23.63% on 20-40 step plans (A02.02-K24, Kambhampati/Valmeekam lab). Was F16.
  - single source only: restating the current state in the prompt (memoization) cuts state hallucination; random trajectories as good as chosen ones (70.0 vs 71.0) (A02.02-K26, AoT+ only; MEDAKA reports hallucination persisting). Was F17.
  - single lab only: analogy transfer depends on noticing, hint vs no hint (A02.04-K06, Gick/Holyoak work). Was F18; the "O7: unaided analogy rarely transfers" schema support is now single-lab.
  - single source only: in people, VOTAT exploration predicts success but is neither necessary nor sufficient (A02.04-K21, one lab plus a partly supporting independent study). Part of F20.
- **Six subfields unresearched** (section 1). Impasse-driven subgoaling (03) feeds S6 directly; progress monitoring (07) feeds the S6 trigger. Until they are done, S6 control rests on three subfields.
- **No current-model data.** Most LLM numbers come from 2023-25 models. A02.04-K35 shows the picture changes for reasoning models, and decomposition, abstraction and analogy are untested on them.
- **Ill-defined problems are absent** from every LLM search benchmark here (A02.01-K21, contested). All tested tasks have checkers and short exact rules. The open mode of the schema has no evidence from this field.
- **How often clobbering happens in LLM output** is unmeasured (A02.02-K34, open). T6 fills it.
- **Whether an LLM can read its own strategy-success table** is untested (A02.04-K36). Only external controllers were tested.
- **Independence audit done, 2026-10-26.** Established rows were reduced to claims that passed. Several still lean on a handful of papers (Tree of Thoughts, Self-Discover); check again before any row enters SCHEMA.md.
- **Oracle gaps may be inflated** (A02.04-K30 counts one lucky run per paradigm).
- **Human-only items do not transfer:** think-aloud effects (A02.01-K30, contested), the intelligence link (A02.04-K23), mental-then-external transfer (A02.01-K13).
- **No bench for these tests.** The bench holds ARC and BRAINTEASER only. Hanoi-like, Blocksworld-like, multi-goal and hidden-rule item generators with code checkers are a precondition for T1 to T7.

**Source audit, 2026-10-26:** of 33 established claims in this field that were re-opened against their papers, 16 were confirmed, 9 were reworded (A02.01-K07, K23, K26, K28; A02.04-K01, K18, K27, K35, K36) and 8 were downgraded to single-source: A02.01-K09, A02.01-K11, A02.01-K25, A02.01-K29, A02.02-K24, A02.02-K26, A02.04-K06, A02.04-K21. Three more claims were downgraded earlier by a code check and are also single-source: A02.01-K01, A02.01-K02, A02.02-K01. Established claims now total 25 (8, 4, 13).
