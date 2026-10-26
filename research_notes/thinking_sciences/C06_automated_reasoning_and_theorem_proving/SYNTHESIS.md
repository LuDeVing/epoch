# Automated reasoning and theorem proving: synthesis

*One view across the field's researched subfields. Built from each subfield's DEEP.md, claims.jsonl and UNKNOWNS.md.*

Notes on use. "Established" means the claim's status in claims.jsonl. The established claims went through the source audit of 2026-10-26 (see the paragraph at the end). "Contested" and "single-source" claims are named only where they matter for a contradiction or a gap. Schema column checked against `research_notes/single_agent/SCHEMA.md` v0.2. Most evidence here comes from SAT, planning and formal provers. For the agent it is a design hint until tested on our model (section 5).

## 1. Coverage

| Subfield | DEEP.md | Claims | Established |
|---|---|---|---|
| 03 CDCL and conflict learning (no-goods) | [DEEP](subfields/03_cdcl_conflict_learning/DEEP.md) | 32 (K01 to K21, K25 to K35) | 18 (+12 single-source, 1 contested, 1 open) |
| 07 Lemma discovery and conjecturing | [DEEP](subfields/07_lemma_discovery_and_conjecturing/DEEP.md) | 21 (K01 to K21) | 8 (+2 contested, 11 single-source) |
| **Total** | | **53** | **26** |

Each subfield has a UNKNOWNS.md with 14 test rows (28 in all).

**Not yet researched** (from SUBFIELDS.md): resolution and saturation; SAT solving and DPLL; interactive theorem proving; neural and LLM proof search; premise selection; proof planning and repair; autoformalisation; counterexample finding. Two of these matter most for the agent: counterexample finding (the S7 discriminating test) and premise selection (retrieval from a subgoal library).

Note: 03's claims K01 to K21 were recovered after this synthesis was first written and are merged into section 2 (F3, F14 to F22). Ids K22 to K24 have no rows. Gap in section 7.

## 2. Established findings, merged

| # | Finding | Claim ids | Schema part | In SCHEMA.md? |
|---|---|---|---|---|
| F1 | A stored failure ("no-good") pays only when the derived reason is much shorter than the full state. Planning gains ran 1.6x to 120x, and memo-length reduction tracked speedup. Code can compute this ratio from a few failures before the store is turned on. Shown in SAT and planning only. | C06.03-K25 | G12, S0 | partly (G12 spends by difficulty; no store gate) |
| F2 | At equal tokens, free-text reflect-and-repair does not reliably beat sampling more fresh attempts. The limit is diagnosis quality. Any store trial needs a resample arm. | C06.03-K26 | S5, S9 | partly (4b bars unstructured self-reflection; no resample-arm rule) |
| F3 | Whether acting on a failure signal pays depends on how reliable it is. In a simulation of mistake-location finders for backtracking (Tyen et al., BIG-Bench Mistake, PaLM 2), gains exceeded losses on most tasks once the finder was right about 60 to 70% of the time, and losses on correct traces plateaued near 65%; a trained classifier did not reach that level. This is one simulation on one benchmark and model; the Kamoi et al. survey gives no numeric threshold. Free-text reflection helps when the signal is reliable (ALFWorld 130 of 134; HumanEval 91% vs 80%; Rust 50 hardest 68% vs 60%) and gives no gain or harm when it is weak (MBPP 0.77 vs 0.80 with 16.3% false-positive tests; Rust without tests 52%). Without an oracle, self-correction lowers accuracy (CommonsenseQA 75.8 to 41.8 after 5 calls). | C06.03-K28, C06.03-K13 | G2, G3 | partly (G2 says revise from real output; no precision threshold, and the 60 to 70% figure is only a one-benchmark simulation) |
| F4 | Lesson stores can lower scores even for large models when always on, bloated or retrieved too narrowly (DeepSeek-V3.2 AppWorld 73.2 vs 64.2 and 44.6; GPT-4.1 top-3 retrieval 2.9 points below baseline). A store gated on held-out gain kept the baseline. | C06.03-K29 | M (lessons) | partly (section 5: lesson shown after first attempt, trusted after two wins; no gate on held-out gain, no empty-store option) |
| F5 | Text-only judges are not a safe source of no-goods. Feed the store from code checks. If only judges exist, aggregate several and calibrate first. | C06.03-K34 | G2, G5 | yes (G5 code selects; G2 revise from real output). The store-source rule is new. |
| F6 | Machine-proposed lemmas are often not useful in the settings measured (Lemmanaid on HOL-test: 22.6% match gold, 23.6% false; Rabe 12.7% provable-and-new, 49 of 130 theorems used, though 3445 of 3857 assumption theorems were used, so usage is a low bar; 2 of 10 proved lemmas used in one template-conjecturing running example; QuickSpec precision under 1% on Octonions). Not shown to hold across all systems. | C06.07-K01 | O3, G4, logging | no (no lemma funnel in section 6) |
| F7 | A cheap filter stage (type-check, trivial check, truth test by small case or counterexample) removes a large share of candidates before costly proving (MathlibLemma keeps 44%). Hipster, QuickSpec and Lemmanaid all filter by test. | C06.07-K02 | S4, G3 | partly (S4/G3 test candidates; no filter step before relying on a proposed lemma) |
| F8 | Machine-checked verification controls bad lemmas: only checked proofs are kept, proof bypasses are screened, and models asked in plain words often judge a true new theorem false. Each lemma used in an answer should carry a tool check or an "unverified" flag. | C06.07-K17 | G4, G3, S8 | partly (S8 verify; no per-lemma flag) |
| F9 | Conjecturing helps most as a bridge toward a goal the base prover cannot reach (Vampire 7 to 25 of 50 on TIP; template conjecturing +40 points on Prod; an idealised chained-conjecturing evaluation that assumes good mid-proof lemmas can be guessed, 54.5% to 63.8%, not an achieved system). Gains are small where the base already solves most (IsaPlanner 60% unaided). | C06.07-K04 | O3, S6, G12 | partly (O3 [S] at impasse only; matches G1 and G12) |
| F10 | A growing library of verified lemmas gives a real but modest gain from reuse in context (LEGO-Prover +3.3 points on miniF2F-valid; CPL re-proved 99% vs 91% with the library in context). The gap grows with stream length. | C06.07-K05 | memory | partly (section 5 subgoal library is [D]; this is the first support) |
| F11 | Per-lemma cross-problem transfer is weakly measured. Evidence is aggregate (library on vs off). Only Rabe reports per-lemma reuse, and only inside one run. | C06.07-K15 | memory | no (a gap more than a finding; it sets what the log must hold) |
| F12 | Self-play conjecturing creates training signal when expert iteration stalls (STP 28.5% vs 13.2% on LeanWorkbook). Training result. Only the lesson transfers: aim sub-statements at the edge of ability. Retraining gains are 2 to 3 points. | C06.07-K08 | O3 | no |
| F13 | Early discovery systems (AM, Eurisko, Graffiti, HR) gave real results, but success depended on representation. Concepts as small compact predicates mutate usefully; long heuristics mutated into junk. | C06.07-K12 | O3, S2 | no |
| F14 | Of the four CDCL features ablated in MiniSat (learning, VSIDS, 2-watched-literals, restarts), clause learning mattered most: learning off solved 4837 of 10000 vs 9068 for the full solver; without VSIDS 6932, without 2WL 8409, without restarts 8653. Plain DP with no look-back failed in 100% of runs on two hard real-world instances, and learned clauses are essential for going beyond tree-like proofs. Only these four features were ablated. SAT only. | C06.03-K01 | memory | no (evidence base for why a store matters; sets no schema step) |
| F15 | Conflict analysis with non-chronological backjumping (GRASP) and backjumping with learning (relsat) let complete solvers finish instances plain DP could not (GRASP 149 of 149 BF-1355 instances in 125.7 s, TEGUS 53 solved; relsat(4) failed 13% of hanoi4 runs vs 100% for naive DP). | C06.03-K02 | memory | no (see M6 for the backjump analogue) |
| F16 | Practical SAT speed came largely from engineering and decision focus, not new learning theory (Chaff: over 90% of time in unit propagation, one to two orders from watched literals plus VSIDS). The decision rule and learning must work together: adaptVSIDS 351 vs 343 of 1030; a planning-specific heuristic beat VSIDS in the same solver (757 vs 701 of 968); structure-supplied branching order made pebbling formulas easy for zChaff where learning alone failed. | C06.03-K03, C06.03-K09 | memory | no |
| F17 | Retention is bounded in the solvers examined, because unbounded clause storage is costly: GRASP kept clauses of at most 20 literals; relsat relevance-bounded learning beat size-bounded (hanoi4 fail 13% vs 94% and 92%); Glucose (LBD deletion plus Luby restarts and phase saving, so a whole-solver result) solved 176 of 234 vs 132 to 153. Short clauses spanning few decision levels (low LBD) are used far more than longer ones (SAT-Race 06; LBD 2 used 202 and 1827 times vs 26 and 136 at LBD 4; one paper); the first-UIP clause has the smallest LBD (a proved property). Over-aggressive erasure hurts when memory is tight. | C06.03-K04, C06.03-K05 | memory | partly (section 5 lessons trusted after two wins; no deletion rule) |
| F18 | Learning is not a universal win and restarts depend on the family. Look-back gave little on random 3SAT; no DP variant solved the 3bit circuits WSAT solved trivially; ISAMP was about 10x faster than relsat(4) on six scheduling instances. In MiniSat, restarts help overall (9068 vs 8653) but termrw solved 446 with restarts off vs 420 with full CDCL, and sverif without VSIDS still solved 592 of 1200 runs (full CDCL 1006). Luby on gave 4533 SAT and 4535 UNSAT vs 4230 and 4423 off; clique formulas need restarts off. Heavy-tailed run times justify randomised restarts with a tuned cutoff (round-robin 14: 411 s to 250 s). Winners are instances with short, easily derived no-goods. | C06.03-K06, C06.03-K07 | G12, memory | partly (G12 resample only with a foothold; no per-family switch) |
| F19 | In idealised proof-complexity terms, clause learning with unlimited restarts is as strong as general resolution, and learning without restarts beats regular and tree-like resolution. The results assume oracle branching and do not predict real speed. Theory only. | C06.03-K10 | none | no |
| F20 | Repeating a step that already failed is a common, measured LLM-agent failure. Step repetition (FM-1.3) is 15.7% of annotated failures (1642 traces, 7 multi-agent systems). In TIDE, Qwen3-4B has a loop ratio of 32.0% in FrozenLake; from Qwen3-4B to Qwen3-30B-A3B it falls from 15.8% to 1.0% in BlocksWorld and from 36.7% to 5.7% in WebShop, but not in FrozenLake (37.7%). A no-good filter targets exactly this. | C06.03-K15 | G2, S5 | no (repeat blocker is test M5) |
| F21 | Prompted LLMs do not carry out SAT-style search reliably: most say satisfiable for nearly every random 3-SAT formula, non-reasoning models fall below paired score 0.2 by 25 variables, small models trained on DPLL traces fail beyond training size. So the no-good store and its checks should be code, not model reasoning. | C06.03-K19 | G5 | partly (G5 code selects) |
| F22 | LLM-written CDCL heuristics improve solvers on chosen families (AutoSAT beats MiniSat on 9 of 12 datasets and Kissat on 4; AutoModSAT about 40% PAR-2 gain over its base ModSAT). Gains rest on scoring by running code and vanish on some families; in-domain a well-tuned single solver is a strong baseline, though DaSAThco's per-instance selection still beat it. AutoSAT and AutoModSAT are the same lab. | C06.03-K20 | O4 | no |

Claims with no schema action: C06.07-K16 is contested and tool-level (see section 6).

## 3. Contradictions between subfields

| # | Where they disagree | How to resolve |
|---|---|---|
| C1 | **Stored memory: help or harm?** Helps: C06.07-K05, C06.07-K15 (a verified-lemma library in context, +3.3 points; 99% vs 91% re-proving). Hurts or null: C06.03-K26 (free-text reflection no better than resampling), C06.03-K29 (always-on lesson stores cut scores by up to 29 points), single-source C06.03-K32 (about +1 point on think-enabled models). | Not a true conflict. The helpful stores hold tool-verified facts. The harmful ones hold free-text lessons, written without a check. Run both stores against a resample arm at equal tokens: C06.03-U1, C06.07-U6. |
| C2 | **Does extra compute or a lemma pool cause the gains?** C06.07-K09 (contested): Seed-Prover and Hilbert show large gains with large conjecture pools. C06.07-K18 and C06.07-K19 (single-source): no one holds tokens fixed, and sampling plus a verifier gives its own gains (coverage 82.9% to 98.44%). C06.03-K31 (single-source): fresh attempts scale log-linearly with a verifier. | Keep lemma-first and resample as rival arms at equal tokens: C06.07-U1, C06.03-U6. Until then do not treat lemma pools as the cause. |
| C3 | **Do templates help?** C06.07-K10 (single-source): template-guided beats symbolic and small neural models. Same paper: Opus 4.5 and GPT-5.2 with templates score 19.4% and 15.8% vs 34.5% and 25.2% direct. | Model-dependent. Frontier models may lose with templates. Test: C06.07-U13. |
| C4 | **Judge as gate.** C06.07-K02 lists a judge among filter stages, while C06.07-K03 (single-source) finds 46% of judge-rejected candidates were valid. C06.03-K34 bars text judges as a no-good source. | Use a judge only to order, never to reject, until its false-negative rate is measured: C06.07-U4. Agrees with SCHEMA G5. |
| C5 | **Failure check precision vs the cost of a filter.** C06.07-K02 says filter early; C06.03-K28 (a one-benchmark simulation) puts break-even for a mistake finder at about 60 to 70% and finds losses on correct traces below it. | A filter that removes candidates is also a failure check. Report its false-rejection rate (C06.07-U2, C06.03-U7). |
| C6 | **Other fields (A01 synthesis).** A01 F10 and A01 F33 say refinement plateaus after about 2 rounds and sampling scales slowly (about +3 points per doubling on ARC). C06.03-K31 reports log-linear coverage with a verifier on SWE-bench (single-source, a different task). A01 F12 and A01 C4 say code, not the model, should run the counterexample search. C06.07-K02 and C06.07-K19 agree. | Coverage scaling and ARC accuracy gain are not the same measure. Check task by task before using either as a default. The counterexample point is consistent across fields and gives the strongest design: code runs the falsifier. |

## 4. Recurring mechanisms

| Mechanism | Subfields and claims | What it means for the agent |
|---|---|---|
| **Check before store or use** | 03 (C06.03-K28, K34, K13), 07 (C06.07-K02, K17, K19) | A candidate lemma or a lesson enters memory or an answer only after a code check. Judges alone are lossy. The check's own precision is a limit (simulated break-even of 60 to 70% on one benchmark, C06.03-K28). |
| **Short reason vs full state** | 03 (C06.03-K25, K33), 07 (C06.07-K05, K06) | Memory pays when the stored item is small next to what it replaces, and when checking it is cheap. Keep the store in code and inject only trigger-matched entries. |
| **Gate memory against resampling** | 03 (C06.03-K26, K29, K31), 07 (C06.07-K18) | Every memory or lemma step needs an equal-token arm of plain resampling. Both subfields flag that the arm is missing from the literature. |
| **Help comes at the edge of ability** | 03 (C06.03-K32), 07 (C06.07-K04, K08, K09) | Gains shrink as the base grows strong. Lemma and lesson steps belong where the base has partial success. This matches G1 and G12. |
| **Funnel logging** | 07 (C06.07-K01, K15), 03 (C06.03-K25 ratio) | Log true, new and used per proposal. Log per-lemma reuse in distinct accepted answers. Without these, no transfer claim can be tested. |
| **Compact representation** | 07 (C06.07-K12), 03 (C06.03-K25) | Small, replayable units (predicates, short clauses, typed steps) work. Long free-text units do not. |

## 5. Merged tests

Each row merges UNKNOWNS rows with a shared design. Every unknown id of both subfields is covered once.

| # | Merged test | Unknown ids covered | One-line design | Priority |
|---|---|---|---|---|
| M1 | **Lemma funnel and small-case check** | C06.07-U2, C06.07-U4, C06.07-U11 | Propose lemmas on hard items. Arms: small-case test then use vs no test; judge-ordered vs random order; perturbation recall flag. Log true, new and used per lemma. Metric: false-lemma rate in accepted answers, lemmas proved per token. | High (cheapest; makes the log all later tests need) |
| M2 | **Lemma-first vs longer direct attempt** | C06.07-U1, C06.07-U3, C06.07-U12, C06.07-U14 | Hard items with plain pass rate 20 to 70%. Arms at equal tokens: propose-check-solve, one long attempt, impasse-only lemma step, N = 2/5/10/25, depth 0/1/2. Metric: pass rate and tokens per solved item; check no loss on easy items. | High |
| M3 | **Shortening ratio and coded no-good store** | C06.03-U2, C06.03-U1, C06.03-U4, C06.03-U14 | Per class, code computes derived-reason size / full-state size from 5 to 10 failures. On classes passing it, run no memory vs free-text lesson vs coded no-goods vs resample at equal tokens; add a code-shrunk conflict set arm and a task-structure ordering arm. | High |
| M4 | **Store gating, precision and hygiene** | C06.03-U3, C06.03-U7, C06.03-U8, C06.03-U11, C06.03-U12 | Arms: no lessons, always-on list, trigger-matched, trigger-matched plus held-out gate; inject false failure verdicts at 0 to 40%; keep-all vs score-based deletion; store-all vs verified-only vs batch-merged. Metric: score vs no lessons, break-even precision, store size. | High |
| M5 | **Repeat blocker, attempt lengths and restarts** | C06.03-U9, C06.03-U6, C06.03-U10 | Log attempt length and success per class. Repeat-blocker on vs off on a small and a large model. Then one long attempt vs fresh restarts vs restarts with store. Impasse on flat failure depth vs fixed count. Metric: loop ratio, solved at equal tokens. | High (cheap) |
| M6 | **Backjump to the culprit step** | C06.03-U5, C06.03-U13 | Multi-step items where code names the first failing step. Retry from scratch vs retry with lesson vs resume from culprit; on infeasible items, generic error vs named clashing constraints. Metric: fixed share per token; fabrication rate. | Med |
| M7 | **Separate conjecture and prove, request-then-retrieve** | C06.07-U5, C06.07-U8, C06.07-U10, C06.07-U13 | 20 runs per arm on a discovery task with a known target: separate vs joint calls; request-then-retrieve vs free generation; edge-of-ability filter on sub-statements; templates vs cold at matched prompt tokens. | Med |
| M8 | **Library stream and cross-class transfer** | C06.07-U6, C06.07-U7, C06.07-U9 | Stream of 40+ related problems: store carried vs reset, by stream position; train on class X, test on held-out class Y; known-results lookup first vs propose directly. Metric: accuracy by position, reuse in 2+ distinct problems. | High for U7 (decides if the subgoal library is worth building); Med for the rest |

Order to run: M1 first (cheapest, makes the funnel log). Then M2 (the central open gap, C06.07-K18). In parallel M5 and the ratio part of M3 (both run on failures already logged). Then M3's store arms and M4. M6 to M8 follow.

## 6. Not to add

| Idea | Why not | Claim ids |
|---|---|---|
| Free-text reflect-and-repair as the memory of failures | Does not reliably beat fresh resampling at equal tokens | C06.03-K26 |
| An always-on or fixed-top-k lesson list | Cut AppWorld scores by up to 29 points; narrow top-3 retrieval was 2.9 below baseline | C06.03-K29 |
| A no-good store written from a text judge | Weak verifiers have high false-positive rates; self-correction from prompted feedback fails outside suited tasks | C06.03-K34 |
| Acting on a failure or culprit signal of unmeasured precision | In a simulation on one benchmark, losses on correct traces outweighed gains below roughly 60 to 70% finder accuracy; the threshold is not general | C06.03-K28 |
| A no-good store for a class where the ratio is near or above 1 | Gain tracks memo shortening; long memos gave only 1.6x | C06.03-K25 |
| A lemma step on every problem | Gains are small on strong bases; keep it at impasse (G1, G12) | C06.07-K04 |
| An LLM judge as the sole gate on lemmas | 46% of judge-rejected candidates were valid (single-source) | C06.07-K03 |
| Lemma evaluation where the lemma was taken from the answer | Inflates the gain: 76.5% leaked vs 61.7 to 64.8% honest (single-source) | C06.07-K13 |
| Claiming a lemma pool as the cause of Seed-Prover or Hilbert results | Contested: prover strength and compute are confounded | C06.07-K09 |
| Single-metric tool comparisons from conjecturing papers | Rankings flip with benchmark and setting | C06.07-K16 (contested) |
| Training-only levers (self-play retraining, from-scratch conjecturing loops) | Need weights and months of compute; only the edge-of-ability lesson transfers | C06.07-K08, C06.07-K14 |

## 7. Gaps

- **Two of ten subfields done.** Counterexample finding, premise selection and neural proof search are not researched and bear directly on S7 and the subgoal library.
- **03's ids K22 to K24 have no claim rows.** K01 to K21 were recovered and merged (F3, F14 to F22); anything in 03's DEEP.md that rested on K22 to K24 has no claim row.
- **Residual caveats after the source audit.** C06.03-K25 rests on SAT and planning only; C06.07-K05 (LEGO and CPL) has confounds noted in K06; C06.07-K01 mixes systems; C06.03-K20 rests on one lab (AutoSAT and AutoModSAT).
- **Everything for the agent is untested.** No paper tests a formal, subsumption-checked no-good store in an LLM agent against free-text reflection and against resampling at equal tokens (C06.03-K35, open). No paper compares lemma-first with longer direct attempts at equal tokens (C06.07-K18).
- **Heavy-tailed attempt lengths for language models** are unmeasured (C06.03-K30, single-source, SAT only). Part of M5.
- **Cross-problem transfer** of lemmas and lessons is unmeasured (C06.07-K15). CDCL no-goods live inside one problem; our lessons are meant to travel.
- **Lemma truth rate in non-numeric plain text** is unknown. A small-case check may not exist there. Contamination in Mathlib-like domains cannot be separated from derivation.
- **Judge calibration for "interesting" or "new"** has no gold labels (C06.07-K03, single-source).
- **Strong-model effect.** Gains from lesson stores shrink as the base improves (C06.03-K32, single-source). Run M3 and M4 on the final model first.
- **No bench items.** The harness has ARC and BRAINTEASER only. Lemma tasks with machine-checkable small cases and coded puzzle classes with replayable steps must be built first.
- **Primary sources unopened** (listed in the two UNKNOWNS files): Pipatsrisawat and Darwiche 2011, Dechter and Frost, AgentDebug full text, original Graffiti and HR papers. They may add numbers; none gates a test.

**Source audit, 2026-10-26:** the papers behind every established claim were re-opened. Of 26 established claims, 15 were confirmed and 11 reworded (C06.03-K01, K04, K05, K06, K07, K15, K20, K28; C06.07-K01, K04, K12). None were downgraded, so no section 2 row moved to Gaps. The wording above follows the reworded claims; the K28 threshold (60 to 70%) is now a one-benchmark simulation, not a general rule.
