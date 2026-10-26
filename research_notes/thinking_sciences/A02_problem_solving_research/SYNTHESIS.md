# Problem-solving research: synthesis

*One view across the field's researched subfields. Built from each subfield's DEEP.md, claims.jsonl and UNKNOWNS.md.*

Notes on use. "Established" means the claim's status in claims.jsonl, set before the stricter independence re-check. Treat each row as a candidate until that check is done. Contested, single-source, hypothesis and open claims are named only where they matter for a contradiction or a gap. Schema column checked against `research_notes/single_agent/SCHEMA.md` (guardrails G1 to G12, states S0 to S9, operators O1 to O8, section 4b). Most findings here come from LLM benchmarks, not people, so they are direct hints for the agent, but mostly from 2023-25 models. Run them again on the model we ship.

## 1. Coverage

| Subfield | DEEP.md | Claims | Established |
|---|---|---|---|
| 01 Problem-space theory | [DEEP](subfields/01_problem_space_theory/DEEP.md) | 43 | 14 |
| 02 Means-ends analysis | [DEEP](subfields/02_means_ends_analysis/DEEP.md) | 34 (+1 hypothesis, 2 open) | 7 |
| 04 Problem solving strategies and the problem-solving cycle | [DEEP](subfields/04_problem_solving_strategies_and_cycle/DEEP.md) | 37 | 15 |
| **Total** | | **114** | **36** |

Single-source claims: 60. Contested: 15. Unknown rows: 16 (01), 15 (02), 17 (04), 48 in all.

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
| F1 | Selective, heuristic search is what makes problem solving tractable. Blind search is hopeless. Pure difference reduction needs a hand-written difference table and scales badly; people switch to abstract planning bursts, and selectivity costs completeness. | A02.01-K01, A02.01-K29, A02.02-K04 | G12, S3 | partly (G12 search only where there is a foothold; no statement about completeness loss) |
| F2 | A problem is states plus operators plus a goal test. A scaffold that makes these explicit objects matches the theory. | A02.01-K02 | S1, S2, O1 | yes (state graph S0 to S9, operator table) |
| F3 | Writing the successor function and the goal test once as code, then running ordinary search, solves rule-based sets at about 100% in few LLM calls and costs far less than LLM-in-the-loop search. The first draft of the code often needs 1 to 3 tries (more for small models). All tested domains had exact short rules. | A02.01-K11, A02.02-K01 | O1, O2, S4, S0 mode | partly (G5 code selects; no code-search route for items with an explicit goal) |
| F4 | Tree search over model-generated steps beats plain chains by a large margin on tasks with a checkable step state and a weak baseline (Game of 24 4% to 74%). The gain is conditional. It is small where the model is already good, small against strong voting, and it can hurt on easy items. It helps on mid-difficulty items. A cheap first pass can gate it. | A02.01-K03, A02.01-K04, A02.01-K37, A02.04-K18 | G12, O3, S4 | yes (G12 grow the tree only with a foothold; O3 decompose; difficulty allocation) |
| F5 | The evaluator is a key part. On Game of 24 the bottleneck is generating ideas, not judging them. A better value function nearly closes the gap between narrow and wide search. | A02.01-K07, A02.04-K18 | S4, G5 | partly (G5 code selects; no rule that the evaluator is tested on its own) |
| F6 | An external sound verifier in a generate-test loop works. The model's own critique does not (graph colouring 1 of 100 under self-critique; GPT-4 as verifier misses 20.7% to 97.1% of wrong plans; intrinsic self-correction lowered one benchmark from 75.8 to 38.1). | A02.01-K09, A02.02-K31 | G2, G3, G5, G10 | yes (G2, G3, G5, G10; 4b unstructured self-reflection) |
| F7 | Plain repeated sampling is a strong baseline whenever an automatic checker exists (coverage rises log-linearly with samples). Without a checker, voting and reward models plateau. A cheap model in a verifier loop can match a reasoning model for less money. | A02.01-K22 | G3, G11, G12, S3, S4 | yes (G11 several short attempts; G12; S3 independent attempts) |
| F8 | Step-by-step text helps mostly on math, symbolic and logic tasks and little elsewhere. Thinking-heavy modes waste many tokens on easy items. Plain CoT adds little (about +3 to -3 points) for reasoning models, at 20 to 80% more time. Decomposition, abstraction and analogy prompts are untested on reasoning models. A solver or tool beats CoT on symbolic work. | A02.01-K23, A02.04-K12, A02.04-K35 | G1, G11, G12, S0 | yes (G11, G12) |
| F9 | The same state space can differ in difficulty by large factors depending on how moves are represented (isomorphs 2:1 to 16:1; cost of checking move legality is the driver; training on the operator removes the gap). Hanoi difficulty tracks the length to the first subgoal, not only total length. State-space size and solution length do not reliably set difficulty, and a misleading progress heuristic traps solvers. | A02.01-K25, A02.01-K26, A02.02-K08 | S1, S2, O6, G12 | partly (O6 change representation; G12 allocates by difficulty but no rule about what predicts difficulty) |
| F10 | Several different strategies solve one puzzle, and correctness does not reveal which one was used. Strong solvers keep a repertoire and pick by problem type. Rote strategies break when rules change. | A02.01-K28, A02.04-K03 | O1 to O8 | partly (operator table is a repertoire; no strategy-identity logging beyond "operators tried") |
| F11 | People choose strategies in proportion to learned success rates (close to probability matching), and simple reinforcement or Bayesian success-estimate models fit. | A02.04-K01 | S0, memory class record | partly (class record kept in code, read by S0; it records operators that solved subgoals, not per-strategy success rates) |
| F12 | No single prompting strategy wins across datasets or sizes. A per-item oracle is far above the best fixed strategy. The model choosing its own strategy, or voting or verifying across strategies, recovers only part of that gap. A learned router recovers about a quarter of it, mostly as a cost saving. The oracle counts one lucky run per paradigm, so the true gap is smaller. | A02.04-K09, A02.04-K10, A02.04-K30 | S0, S6 routing | partly (S0 chooses a mode; G4 bars strategy voters; no strategy router) |
| F13 | Cheap-first with escalation on low answer consistency, or learned routing, cuts tokens or cost at equal accuracy (46 to 85% in one study, over 60% in another). Thinking models also cut effort near collapse. | A02.04-K11, A02.04-K12 | G11, G12, S0 | partly (G12; escalation by agreement is a hint under G4, untested for us) |
| F14 | A persistent per-task-type record of what worked helps when a small outside controller reads it (bandit: equal or better accuracy at up to 83% less cost). LLMs given raw history do not explore well in context. No test of the LLM reading its own strategy table was found. | A02.04-K36 | memory class record, S0 | partly (class record exists, read by S0 in code; the LLM-reads-it case is not tested) |
| F15 | Pure difference reduction fails on conjunctive goals when one goal clobbers another (Sussman anomaly, taxi case). Fixes: goal protection, a final all-goals check, interleaving. | A02.02-K03 | S8, G | no (S8 checks the answer on the unfitted part; no all-goals recheck rule) |
| F16 | GPT-4-class models solve about a third of Blocksworld plans, and 2 to 5% with obfuscated names. A reasoning model reached 97.8% plain, 52.8% on the obfuscated set, 23.6% on 20 to 40 step plans. Score on a familiar form hides weak reasoning. | A02.02-K24 | G3 | yes (G3 mutated input) |
| F17 | Restating the current state in the prompt (memoization) cuts state hallucination. Random search trajectories in the examples work as well as chosen ones (70.0 vs 71.0). | A02.02-K26 | state ledger, S1, S6 | partly (S6 writes one state line; no ledger rule) |
| F18 | Analogy transfer depends on noticing. Without a hint few solvers apply a stored analogue; with a hint most do. Comparing two analogues and nearer sources help. | A02.04-K06 | O7, memory retrieval | yes (O7: unaided analogy rarely transfers; far analogues only at impasses) |
| F19 | Having the right strategy does not guarantee success. Execution errors dominate (74.7% of Self-Discover MATH failures). The error mix depends on method (Plan-and-Solve: misunderstanding 27%, calculation 7%). | A02.04-K15 | S8, G2 | partly (S8 verify; no execution-vs-strategy split in the log) |
| F20 | LLM agents explore hidden-rule tasks poorly (prefer OR over AND rules). Sampling many distinct hypotheses and choosing actions that eliminate them removes the gap. A typed scaffold alone can lower accuracy (87.3 to 77.3) unless paired with a monitor. In people, good exploration (VOTAT) predicts success but is neither necessary nor sufficient. | A02.04-K27, A02.04-K21 | S2, S7, O (hypothesis test), G7 | partly (S2 candidate rules; S7 discriminating test; no explicit hypothesis-elimination loop) |
| F21 | Long-horizon runs derail in stereotyped ways: meltdown loops after one wrong belief, idle drift, repeated unchecked actions. Failure depends on model and horizon (one strong model without reasoning beat human trajectories). | A02.04-K33 | monitor, S6 trigger | no (S6 fires on no pass, repeated error or budget; no no-op counter or belief-vs-observation check) |

No schema action (background only): A02.02-K04 beyond F1 (the authors concede the search theory is thin).

## 3. Contradictions between subfields

| # | Where the sources disagree | How to resolve |
|---|---|---|
| C1 | **Does tree search beat plain sampling?** For: A02.01-K03, A02.04-K18 (Game of 24 74% vs 4%). Against or small: A02.01-K04, A02.01-K22, A02.01-K37, contested A02.01-K35 (naive MCTS lost to sampling at every budget; a budget-aware tree won with about 7x less compute). The big wins come against weak baselines (plain CoT, not voting). | Do not add the tree on the strength of the 74%. Test against best-of-N with the same checker at equal dollars, by difficulty bin (T1). Keep G12 until then. |
| C2 | **Strategy routing against SCHEMA G4.** A02.04-K09, K10, K30 say a per-item oracle is far above any fixed strategy and routing saves cost. G4 says no persona or strategy voters on single-answer problems. A02.04-K10 shows that voting across strategies recovers only a fraction. | Not a real conflict. G4 bars voting across strategies. Routing by class record, in code, is a different thing. The gain may be mostly cost, not accuracy (A02.04-K30). Decide with T3. |
| C3 | **Is explicit structure good?** F2 (A02.01-K02) says explicit objects match the theory. Contested A02.04-K14 says self-composed JSON structures lost to free text on MATH (75.5 vs 63.5) but won on BBH. A02.04-K27 says a typed scaffold alone lowered accuracy. | Task and format dependent. Keep structure in code for state, goal test and ledger (F3, F17). Let the plan itself be free text until T9 says otherwise. |
| C4 | **The Hanoi / River Crossing "collapse".** A02.01-K32 says collapse appears across frontier models. Contested A02.01-K15 and contested A02.02-K21 say it is partly output length and impossible instances; code output restores accuracy. A02.01-K16, contested A02.02-K22 and established A02.04-K15 say giving the algorithm did not move the collapse point. | Both hold in part. Failure past a size threshold looks like execution and state loss, not strategy finding. Test with code-held state (T5). Do not use these papers as proof either way. |
| C5 | **Decompose always or only after failure?** A02.02-K33 (open) lists positive transfer for explicit decomposition (ADaPT, LAMBADA, MEDAKA) and negative or null results (Goal CoT hurt out of distribution). A02.04-K35 says decomposition, abstraction and analogy are untested on reasoning models. SCHEMA O3 and G1 allow decomposition only at an impasse. | Open. T7 decides with the failure-triggered rule against always-decompose. |
| C6 | **Does the scaffold help strong models?** Contested A02.01-K08 says the gain depends on the model (19% vs 74% for the same method). A02.04-K35 shows CoT adds almost nothing for reasoning models. A02.02-U1 asks whether the MEA scaffold still wins when thinking is on. A02.01-K13 (contested) mental-then-external transfer is borderline. | Gate by class pass rate and measure on the deployment model (T3, T4, T13). Every element must pay at equal tokens (G7). |
| C7 | **Impasse as a trigger.** A02.01-K21 (contested) says an impasse alone does not give insight; representational change is a rival. A02.01-U9 and G1 treat impasse as the trigger for escalation. A02.04-K11 uses answer inconsistency. | Different questions: when to escalate vs what to do next. T2 compares triggers. Subfield 03 (not researched) should supply the Soar definition. |
| C8 | **Cross-field: A01 C11 and F10 vs here.** A01 says tree search with model self-evaluation conflicts with G5. Here A02.01-K07 says the evaluator is key, and A02.01-K09 and A02.02-K31 say the model judges itself badly. | Consistent. Move scoring to code or a separately tested evaluator (T1 arm). |
| C9 | **Cross-field: A01 F9 and F10 vs A02.04-K35.** A01 says thinking models falsify more and solve more rule games, and breadth beats refinement. A02.04-K35 says CoT adds little for reasoning models. | Not a conflict if thinking is spent on hypothesis search. Per class tests (A01 T8 and T13 here). |
| C10 | **Cross-field: A01 F23 and C5 vs A02.01-K11.** A01 says a solver after LLM translation is a gated tie-break because extraction errors lean to "invalid". A02.01-K11 says model-written code operators solve rule sets at 100%, but all tested domains had exact short rules. | Same lesson. Code search is safe where rules are exact. Add a parse and test check on the code (T5). |

## 4. Recurring mechanisms

| Mechanism | Subfields and claims | What it means for the agent |
|---|---|---|
| **Code holds state and judges; the model fills slots** | 01 (A02.01-K09, K11), 02 (A02.02-K01, K26, K31), 04 (A02.04-K36) | The most repeated result. State, goal test, ledger, success table and verifier are code. The model proposes steps and names differences. |
| **Generation is the bottleneck; the evaluator must be tested alone** | 01 (A02.01-K07), 04 (A02.04-K18), cf. A01 F10 | Spend tokens on diverse proposals. Test the evaluator before the tree. |
| **Gain depends on difficulty and baseline** | 01 (A02.01-K04, K37, K22), 04 (A02.04-K11, K12, K35) | Search and long reasoning help mid-difficulty items, do nothing on easy ones and little for reasoning models. Cheap pass first. |
| **Representation sets difficulty** | 01 (A02.01-K25, K26), 02 (A02.02-K08, K24) | Same logic, different cost. Obfuscated names break pattern matching. Offer a second encoding and test on a renamed copy. |
| **Own progress checks are unreliable** | 02 (A02.02-K31), 01 (A02.01-K09), 04 (A02.04-K15) | Never let the model judge subgoal progress without a sound signal. Execution errors outweigh strategy errors. |
| **Strategy is a distribution, not a choice** | 01 (A02.01-K28), 04 (A02.04-K01, K03, K09, K10, K30, K36) | No fixed best strategy. Routing is worth testing for cost first, accuracy second, and it needs a code-held record. |
| **Conjunctive goals and long procedures fail by lost state** | 02 (A02.02-K03, K26), 01 (A02.01-K32 contested), 04 (A02.04-K33) | A ledger the code re-computes, a final all-goals check and loop or no-op monitors address the same failure. |
| **Selective search loses completeness** | 01 (A02.01-K29), 02 (A02.02-K04) | Keep a visited-state guard and an escape move (reset or detour) so greedy reduction does not trap the run. |

## 5. Merged tests

Each row merges UNKNOWNS rows that share one design.

| # | Merged test | Unknown ids covered | One-line design | Priority |
|---|---|---|---|---|
| T1 | **Search vs sampling vs evaluator, with a coded checker** | A02.01-U1, A02.01-U2, A02.01-U7, A02.01-U12, A02.01-U14, A02.01-U15 | 100 checkable items binned easy/mid/hard: best-of-N, generate-test-repair (2 rounds), tree with same checker, resample plus same evaluator, tree plus random evaluator; add prune and backtrack ablations, state dedupe and a one-prompt trace only if the tree wins. Run on the deployment model in both roles. Metric: solved at fixed tokens and dollars. | High |
| T2 | **Cheap-pass gate and escalation trigger** | A02.01-U3, A02.01-U9, A02.01-U13, A02.04-U2, A02.04-U3 | Cheap pass first; escalate on failed check, impasse signal, 2 to 3 sample disagreement or stated confidence, against always-search and 6-sample majority at a token cap. Also compare predicting difficulty from cheap pass rate vs path length. | High |
| T3 | **Strategy router, success table and capability gate** | A02.04-U1, A02.04-U4, A02.04-U5, A02.04-U6, A02.04-U16, A02.02-U11, A02.02-U12 | First measure the repeat-corrected gap to a per-item oracle (go on only if 8 or more points). Then a code-held per-class success table shown as a summary, a rolling "best changed?" monitor after a silent shift, operators on demand vs fixed script, fail message that names the method class, and a gate that turns the scaffold off when a class pass rate is low. | High |
| T4 | **Means-ends scaffold: which part pays** | A02.02-U1, A02.02-U2, A02.02-U7, A02.02-U8, A02.02-U15, A02.01-U8 | Plain vs scaffold with code-held goal stack and ledger, with thinking on and off; drop one part at a time (ledger, stack, difference naming, calculation hint); forward vs flipped vs backward; vague or wrong difference hints; code difference count vs model distance estimate. | High |
| T5 | **Code-held state and code search for long procedures** | A02.01-U5, A02.01-U6, A02.02-U9, A02.02-U10 | Hanoi-like and rule-based items at growing size: whole plan vs one move per call with code state; model-written successor and goal test with a repair loop vs prompted search; with and without the algorithm in the prompt. Splits strategy-finding from execution. | High |
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
| Model-written verdicts on its own progress or plan validity | False-negative rates up to 97%; self-correction lowered accuracy | A02.01-K09, A02.02-K31 |
| Model-estimated distance to goal as a progress signal | No support; misleading progress heuristics trap solvers. A code difference count is the candidate (A02.02-U15) | A02.01-K26 |
| Pure means-ends (greedy difference reduction) with no loop guard | Fails on conjunctive goals and needs a hand-written difference table | A02.02-K03, A02.01-K29 |
| Giving the algorithm in the prompt as the fix for long procedures | Did not move the collapse point; execution is the failure | A02.04-K15, A02.01-K16 (contested) |
| Letting the model pick its strategy, or voting across strategies | Recovers only a fraction of the oracle gap; also conflicts with G4 | A02.04-K10, A02.04-K09 |
| Plain CoT as the default for reasoning models | Adds about zero at 20 to 80% more time | A02.04-K35 |
| Raw strategy history in the prompt as the strategy chooser | LLMs do not explore well from raw history; summarise in code | A02.04-K36 |
| Using state-space size or solution length alone to allocate budget | Does not set difficulty | A02.01-K26, A02.02-K08 |
| Mental-then-external transfer as a design basis | Borderline and absent in the first experiment | A02.01-K13 (contested) |
| Treating the Hanoi "collapse" papers as proof about reasoning | Partly output limits and impossible instances | A02.01-K15, A02.02-K21 (contested) |
| Intelligence correlation of complex problem solving as a design basis | Human individual-difference result; critique reports near-vanishing correlations | A02.04-K23 (contested) |

## 7. Gaps

- **Six subfields unresearched** (section 1). Impasse-driven subgoaling (03) feeds S6 directly; progress monitoring (07) feeds the S6 trigger. Until they are done, S6 control rests on three subfields.
- **No current-model data.** Most LLM numbers come from 2023-25 models. A02.04-K35 shows the picture changes for reasoning models, and decomposition, abstraction and analogy are untested on them.
- **Ill-defined problems are absent** from every LLM search benchmark here (A02.01-K21, contested). All tested tasks have checkers and short exact rules. The open mode of the schema has no evidence from this field.
- **How often clobbering happens in LLM output** is unmeasured (A02.02-K34, open). T6 fills it.
- **Whether an LLM can read its own strategy-success table** is untested (A02.04-K36). Only external controllers were tested.
- **Independence of "established" claims is unchecked.** Run the stricter check before any row enters SCHEMA.md. Several claims lean on a handful of papers (Tree of Thoughts, Valmeekam et al., Self-Discover).
- **Oracle gaps may be inflated** (A02.04-K30 counts one lucky run per paradigm).
- **Human-only items do not transfer:** think-aloud effects (A02.01-K30, contested), the intelligence link (A02.04-K23), mental-then-external transfer (A02.01-K13).
- **No bench for these tests.** The bench holds ARC and BRAINTEASER only. Hanoi-like, Blocksworld-like, multi-goal and hidden-rule item generators with code checkers are a precondition for T1 to T7.

**Audit (code check, 2026-10-26):** A02.01-K01, A02.01-K02, A02.02-K01 had only one opened source and are now single-source, not established. Treat their rows above as unconfirmed.
