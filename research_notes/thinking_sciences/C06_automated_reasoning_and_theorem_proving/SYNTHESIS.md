# Automated reasoning and theorem proving: synthesis

*One view across the field's researched subfields. Built from each subfield's DEEP.md, claims.jsonl and UNKNOWNS.md.*

Notes on use. "Established" means the claim's status in claims.jsonl. The C06 claims have not been through the source audit that A01 had (see section 7). "Contested" and "single-source" claims are named only where they matter for a contradiction or a gap. Schema column checked against `research_notes/single_agent/SCHEMA.md` v0.2. Most evidence here comes from SAT, planning and formal provers. For the agent it is a design hint until tested on our model (section 5).

## 1. Coverage

| Subfield | DEEP.md | Claims | Established |
|---|---|---|---|
| 03 CDCL and conflict learning (no-goods) | [DEEP](subfields/03_cdcl_conflict_learning/DEEP.md) | 11 (K25 to K35) | 5 (+5 single-source, 1 open) |
| 07 Lemma discovery and conjecturing | [DEEP](subfields/07_lemma_discovery_and_conjecturing/DEEP.md) | 21 (K01 to K21) | 8 (+2 contested, 11 single-source) |
| **Total** | | **32** | **13** |

Each subfield has a UNKNOWNS.md with 14 test rows (28 in all).

**Not yet researched** (from SUBFIELDS.md): resolution and saturation; SAT solving and DPLL; interactive theorem proving; neural and LLM proof search; premise selection; proof planning and repair; autoformalisation; counterexample finding. Two of these matter most for the agent: counterexample finding (the S7 discriminating test) and premise selection (retrieval from a subgoal library).

Note: 03's claims.jsonl holds K25 to K35 only. Claims K01 to K24, cited in 03's critique.md, are not on disk (see its C06.03-NOTE). Gap in section 7.

## 2. Established findings, merged

| # | Finding | Claim ids | Schema part | In SCHEMA.md? |
|---|---|---|---|---|
| F1 | A stored failure ("no-good") pays only when the derived reason is much shorter than the full state. Planning gains ran 1.6x to 120x, and memo-length reduction tracked speedup. Code can compute this ratio from a few failures before the store is turned on. Shown in SAT and planning only. | C06.03-K25 | G12, S0 | partly (G12 spends by difficulty; no store gate) |
| F2 | At equal tokens, free-text reflect-and-repair does not reliably beat sampling more fresh attempts. The limit is diagnosis quality. Any store trial needs a resample arm. | C06.03-K26 | S5, S9 | partly (4b bars unstructured self-reflection; no resample-arm rule) |
| F3 | A failure or culprit signal must be right about 60 to 70% of the time before acting on it beats not acting. Below that, correct traces are damaged. | C06.03-K28 | G2, G3 | partly (G2 says revise from real output; no precision threshold) |
| F4 | Lesson stores can lower scores even for large models when always on, bloated or retrieved too narrowly (DeepSeek-V3.2 AppWorld 73.2 vs 64.2 and 44.6; GPT-4.1 top-3 retrieval 2.9 points below baseline). A store gated on held-out gain kept the baseline. | C06.03-K29 | M (lessons) | partly (section 5: lesson shown after first attempt, trusted after two wins; no gate on held-out gain, no empty-store option) |
| F5 | Text-only judges are not a safe source of no-goods. Feed the store from code checks. If only judges exist, aggregate several and calibrate first. | C06.03-K34 | G2, G5 | yes (G5 code selects; G2 revise from real output). The store-source rule is new. |
| F6 | Most machine-proposed lemmas are not useful. Only a minority are true, new and used (Lemmanaid 22.6% match gold, 23.6% false; Rabe 12.7% provable-and-new, 49 of 130 theorems used; QuickSpec precision under 1% on Octonions). | C06.07-K01 | O3, G4, logging | no (no lemma funnel in section 6) |
| F7 | A cheap filter stage (type-check, trivial check, truth test by small case or counterexample) removes a large share of candidates before costly proving (MathlibLemma keeps 44%). Hipster, QuickSpec and Lemmanaid all filter by test. | C06.07-K02 | S4, G3 | partly (S4/G3 test candidates; no filter step before relying on a proposed lemma) |
| F8 | Machine-checked verification controls bad lemmas: only checked proofs are kept, proof bypasses are screened, and models asked in plain words often judge a true new theorem false. Each lemma used in an answer should carry a tool check or an "unverified" flag. | C06.07-K17 | G4, G3, S8 | partly (S8 verify; no per-lemma flag) |
| F9 | Conjecturing helps most as a bridge toward a goal the base prover cannot reach (Vampire 7 to 25 of 50 on TIP; template conjecturing +40 points on Prod; chaining 54.5% to 63.8%). Gains are small where the base already solves most (IsaPlanner 60% unaided). | C06.07-K04 | O3, S6, G12 | partly (O3 [S] at impasse only; matches G1 and G12) |
| F10 | A growing library of verified lemmas gives a real but modest gain from reuse in context (LEGO-Prover +3.3 points on miniF2F-valid; CPL re-proved 99% vs 91% with the library in context). The gap grows with stream length. | C06.07-K05 | memory | partly (section 5 subgoal library is [D]; this is the first support) |
| F11 | Per-lemma cross-problem transfer is weakly measured. Evidence is aggregate (library on vs off). Only Rabe reports per-lemma reuse, and only inside one run. | C06.07-K15 | memory | no (a gap more than a finding; it sets what the log must hold) |
| F12 | Self-play conjecturing creates training signal when expert iteration stalls (STP 28.5% vs 13.2% on LeanWorkbook). Training result. Only the lesson transfers: aim sub-statements at the edge of ability. Retraining gains are 2 to 3 points. | C06.07-K08 | O3 | no |
| F13 | Early discovery systems (AM, Eurisko, Graffiti, HR) gave real results, but success depended on representation. Concepts as small compact predicates mutate usefully; long heuristics mutated into junk. | C06.07-K12 | O3, S2 | no |

Claims with no schema action: C06.07-K16 is contested and tool-level (see section 6).

## 3. Contradictions between subfields

| # | Where they disagree | How to resolve |
|---|---|---|
| C1 | **Stored memory: help or harm?** Helps: C06.07-K05, C06.07-K15 (a verified-lemma library in context, +3.3 points; 99% vs 91% re-proving). Hurts or null: C06.03-K26 (free-text reflection no better than resampling), C06.03-K29 (always-on lesson stores cut scores by up to 29 points), single-source C06.03-K32 (about +1 point on think-enabled models). | Not a true conflict. The helpful stores hold tool-verified facts. The harmful ones hold free-text lessons, written without a check. Run both stores against a resample arm at equal tokens: C06.03-U1, C06.07-U6. |
| C2 | **Does extra compute or a lemma pool cause the gains?** C06.07-K09 (contested): Seed-Prover and Hilbert show large gains with large conjecture pools. C06.07-K18 and C06.07-K19 (single-source): no one holds tokens fixed, and sampling plus a verifier gives its own gains (coverage 82.9% to 98.44%). C06.03-K31 (single-source): fresh attempts scale log-linearly with a verifier. | Keep lemma-first and resample as rival arms at equal tokens: C06.07-U1, C06.03-U6. Until then do not treat lemma pools as the cause. |
| C3 | **Do templates help?** C06.07-K10 (single-source): template-guided beats symbolic and small neural models. Same paper: Opus 4.5 and GPT-5.2 with templates score 19.4% and 15.8% vs 34.5% and 25.2% direct. | Model-dependent. Frontier models may lose with templates. Test: C06.07-U13. |
| C4 | **Judge as gate.** C06.07-K02 lists a judge among filter stages, while C06.07-K03 (single-source) finds 46% of judge-rejected candidates were valid. C06.03-K34 bars text judges as a no-good source. | Use a judge only to order, never to reject, until its false-negative rate is measured: C06.07-U4. Agrees with SCHEMA G5. |
| C5 | **Failure check precision vs the cost of a filter.** C06.07-K02 says filter early; C06.03-K28 says a check below about 70% precision damages correct runs. | A filter that removes candidates is also a failure check. Report its false-rejection rate (C06.07-U2, C06.03-U7). |
| C6 | **Other fields (A01 synthesis).** A01 F10 and A01 F33 say refinement plateaus after about 2 rounds and sampling scales slowly (about +3 points per doubling on ARC). C06.03-K31 reports log-linear coverage with a verifier on SWE-bench (single-source, a different task). A01 F12 and A01 C4 say code, not the model, should run the counterexample search. C06.07-K02 and C06.07-K19 agree. | Coverage scaling and ARC accuracy gain are not the same measure. Check task by task before using either as a default. The counterexample point is consistent across fields and gives the strongest design: code runs the falsifier. |

## 4. Recurring mechanisms

| Mechanism | Subfields and claims | What it means for the agent |
|---|---|---|
| **Check before store or use** | 03 (C06.03-K28, K34), 07 (C06.07-K02, K17, K19) | A candidate lemma or a lesson enters memory or an answer only after a code check. Judges alone are lossy. The check's own precision is a limit (about 70%). |
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
| Acting on a failure or culprit signal below about 70% precision | Correct traces are damaged | C06.03-K28 |
| A no-good store for a class where the ratio is near or above 1 | Gain tracks memo shortening; long memos gave only 1.6x | C06.03-K25 |
| A lemma step on every problem | Gains are small on strong bases; keep it at impasse (G1, G12) | C06.07-K04 |
| An LLM judge as the sole gate on lemmas | 46% of judge-rejected candidates were valid (single-source) | C06.07-K03 |
| Lemma evaluation where the lemma was taken from the answer | Inflates the gain: 76.5% leaked vs 61.7 to 64.8% honest (single-source) | C06.07-K13 |
| Claiming a lemma pool as the cause of Seed-Prover or Hilbert results | Contested: prover strength and compute are confounded | C06.07-K09 |
| Single-metric tool comparisons from conjecturing papers | Rankings flip with benchmark and setting | C06.07-K16 (contested) |
| Training-only levers (self-play retraining, from-scratch conjecturing loops) | Need weights and months of compute; only the edge-of-ability lesson transfers | C06.07-K08, C06.07-K14 |

## 7. Gaps

- **Two of ten subfields done.** Counterexample finding, premise selection and neural proof search are not researched and bear directly on S7 and the subgoal library.
- **03's claims.jsonl is missing K01 to K24** (per C06.03-NOTE). Only K25 to K35 are on disk, so the CDCL history and SAT numbers in 03's DEEP.md have no claim rows. Merge counts above cover only what is on disk.
- **No source audit yet for C06.** A01's audit moved claims resting on one lab to single-source. Some C06 established claims may also share sources: check C06.07-K01 (four sources, mixed systems), C06.07-K05 (LEGO and CPL, confounds in K06) and C06.03-K25 (SAT and planning only).
- **Everything for the agent is untested.** No paper tests a formal, subsumption-checked no-good store in an LLM agent against free-text reflection and against resampling at equal tokens (C06.03-K35, open). No paper compares lemma-first with longer direct attempts at equal tokens (C06.07-K18).
- **Heavy-tailed attempt lengths for language models** are unmeasured (C06.03-K30, single-source, SAT only). Part of M5.
- **Cross-problem transfer** of lemmas and lessons is unmeasured (C06.07-K15). CDCL no-goods live inside one problem; our lessons are meant to travel.
- **Lemma truth rate in non-numeric plain text** is unknown. A small-case check may not exist there. Contamination in Mathlib-like domains cannot be separated from derivation.
- **Judge calibration for "interesting" or "new"** has no gold labels (C06.07-K03, single-source).
- **Strong-model effect.** Gains from lesson stores shrink as the base improves (C06.03-K32, single-source). Run M3 and M4 on the final model first.
- **No bench items.** The harness has ARC and BRAINTEASER only. Lemma tasks with machine-checkable small cases and coded puzzle classes with replayable steps must be built first.
- **Primary sources unopened** (listed in the two UNKNOWNS files): Pipatsrisawat and Darwiche 2011, Dechter and Frost, AgentDebug full text, original Graffiti and HR papers. They may add numbers; none gates a test.
