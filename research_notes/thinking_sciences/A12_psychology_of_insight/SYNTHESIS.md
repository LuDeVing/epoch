# The psychology of insight: synthesis

*One view across the field's researched subfields. Built from each subfield's DEEP.md, claims.jsonl and UNKNOWNS.md.*

Notes on use. "Established" means the claim's status in claims.jsonl after the source audit of 2026-10-26 (see the last paragraph); claims that rested on one lab or one opened source were downgraded to single-source and moved to section 7. Almost every established finding is about people, on a few lab puzzles (matchsticks, nine-dot, coins, car park). For the agent they are design hints until tested on our model (section 5). Schema column checked against `research_notes/single_agent/SCHEMA.md` (S6, O4, O6, G1, G5, G10, G11 and 4b are the parts that matter here).

## 1. Coverage

| Subfield | DEEP.md | Claims | Established |
|---|---|---|---|
| 01 Representational change (constraint relaxation and chunk decomposition) | [DEEP](subfields/01_representational_change/DEEP.md) | 32 | 11 (2 contested, 19 single-source) |
| 04 Progress monitoring theory | [DEEP](subfields/04_progress_monitoring_theory/DEEP.md) | 25 | 9 (2 contested, 14 single-source) |
| **Total** | | **57** | **20** |

Unknown rows: 15 in 01 (A12.01-U1 to U15), 15 in 04 (A12.04-U1 to U15).

Not yet researched (from SUBFIELDS.md): theory comparison as its own subfield (Jones 2003 is used inside 01 and 04, not studied alone), Gestalt roots and fixation, dual-process and three-process accounts, stage model and incubation, neuroscience and individual differences, methods and measurement (including Ash, Cushen, Wiley 2009 on how often true restructuring occurs). Constraint relaxation and chunk decomposition were folded into subfield 01.

Two established rows (A12.04-K19, A12.04-K24) state that a study does not exist. They are gaps, not findings, and appear in section 7.

## 2. Established findings, merged

| # | Finding | Claim ids | Schema part | In SCHEMA.md? |
|---|---|---|---|---|
| F1 | Human difficulty follows how much of the default frame must change: value change is easiest, operator and whole-structure change are hard. Order held in several labs. | A12.01-K01 | S6, O4, O6 | partly (O4, O6 exist as [S]; no depth ordering, no cost estimate at S0) |
| F2 | Tight chunks (single units) are harder to split than loose ones. Splitting cost, not regrouping, drives difficulty. | A12.01-K02 | O6, O3 | partly (O3, O6 exist; no tightness idea) |
| F3 | Dropping a constraint and splitting a chunk are separate skills. In Knoblich 1999 Exp 3 (N=34), tautological Type C was solved by 100% in Block 1 against 61% for regular Type C, prior exposure to the tautological form shortened regular Type C solution times, and the chunk type (D) initial rate was unaffected (61% vs 69%). Type D times also improved after exposure, so the separation holds for initial rates and only partly for times. One experiment from one lab. | A12.01-K03 | O4, O6 | partly (O4 and O6 are separate rows; separation is not stated) |
| F4 | A wrong first reading then a late shift: fixations are long, start on values, and move to the key element only late. | A12.01-K05, A12.04-K09 (car-park problem: all 30 solvers had a fixation at or above their own mean + 2 SD before the key move, but only 5 immediately before it, and non-solvers also had impasses; fixation on the key move was longer than on the moves around it) | S6 | partly (S6 impasse exists; human eye data is background only) |
| F5 | Misleading cues fix people on a wrong frame (false hints lower anagram success; wrong practice lowers nine-dot success 37.5% vs 78.1%). | A12.01-K15 | G1, S1 | partly (S1 input hygiene; lessons shown after first attempt) |
| F6 | Hints that only say "think outside the box", or add visual cues, give little or no gain (nine-dot base rate under 5%). Large gains came only when aids addressing several difficulties were combined, for example training plus a hint that gives away part of the solution (46% solved). | A12.04-K04 | 4b, O4 | partly (4b bars "be careful" cues; this adds generic reframe cues) |
| F7 | Hands-on or interactive material does not reliably raise insight. The 2011 effect failed three replications. | A12.01-K11 | none | no (nothing in the schema; consistent with not adding embodiment) |
| F11 | LLM self-reported progress in one tau2-bench study: 7 of 11 models follow a reporting duty (93.2-100% of checkpoints), 4 only 0.6-10.1%. For gpt-4.1 and gpt-5.5 reports are right pre-action (90.6-99.4%) and after completion (87.3-88.9%) but only 5.8-11.5% mid-task; several newer models are accurate mid-task (74-100%) and weak at completion (48-64%), so the weak stage varies by model. Uncertainty signals (verbal confidence, perplexity, entropy, consistency) predict failure well only at the end of a long-horizon agent trajectory (verbal confidence mean AUROC .85) and poorly at 50% progress (none above .60). | A12.04-K13, A12.04-K14 | G10, S6 | partly (4b bars verbal confidence as a stop signal; mid-run prediction is new) |
| F12 | Deployed stuck rules are plain counters (same action 3 to 4 times, 5 low scores, error codes). They help (+5.0 pp SWE-bench Verified; ALFWorld +40 pp with a progress gate), bundled with other parts. | A12.04-K17 | S6 | yes (S6 fires on same error twice, two rounds no change, budget fraction) |
| F13 | Excess switching and looping mark failure: wrong answers use 225% more tokens and 418% more thought switches. Penalising switch words raised AIME pass@1 (38.3 to 44.1). | A12.04-K16 | S5, S6, G6 | no |
| F14 | Spontaneous mid-trace "aha" shifts are rare (about 6.3% of traces), go with lower accuracy, and do not grow with RL. "Oh!" wording is not evidence of insight. | A12.01-K18, A12.04-K15 | G10 | partly (G10 reasoning text is not evidence) |
| F15 | Later reflection in a trace is mostly confirmation: over 90% keep the first candidate, wrong-to-right under 2%. Cutting it saves 24.5% tokens for under 3% accuracy loss. | A12.01-K20 | G11 | yes (G11, 4b unstructured self-reflection) |
| F16 | LLMs fall far below people on riddle and lateral-thinking tasks that need a default assumption dropped (NazoNazo 17.6% vs 52.9%; BrainTeaser about 53-63% vs 92%). | A12.01-K16 | S6 | partly (S6 exists; gap is the motive, not a rule) |
| F17 | A distinctive reasoning-model failure on riddles is verification: a correct candidate appears in the thought log but is not endorsed (5.2% to 39.3% of wrong answers across four models with usable logs, so most wrong answers do not hold the gold answer). Outside riddles, over 70% of wrong o1-like responses on math and science sets contain a correct thought, and hidden states encode intermediate-answer correctness (ROC-AUC above 0.7). | A12.01-K17 | S4, S8, G5 | yes (S4 harvest) |
| F18 | Restating the problem at a more abstract level (step-back) gives +7 to +11 points on physics and chemistry, +25 on TimeQA, but fixes 20.5% of errors and breaks 11.9%. Not tested on insight items. | A12.01-K21 | O2, O6 | partly (O2 exists as [S]; break rate is the new fact) |

## 3. Contradictions between subfields

| # | Where they disagree | How to resolve |
|---|---|---|
| C1 | **Representational change or progress monitoring?** A12.01-K09 (contested) says hill-climbing does not explain matchstick difficulty; the degree of relaxation does. A12.04-K06 (car park, N=39) favours representational change. A12.04-K01 (coins) and single-source A12.04-K03 favour greedy progress moves. A12.04-K21: moves are greedy, yet whether the solution move is greedy does not change solving; relaxation does. Single-source A12.04-K07 says both are needed. | Not one theory. Spatial and symbolic tasks differ (A12.04-K05 contested). For the agent, the combined view (progress monitoring says when, representational change says how) rests on single-source A12.04-K07, so treat it as a hypothesis: code decides when (S6), operator decides how. Tests A12.04-U2 and A12.04-U3 decide which arm wins on our item types. |
| C2 | **Is an external reconsideration cue useful?** A12.01-K19: +8.4 on math, near zero on crosswords and Rush Hour; gain larger when first-pass entropy is high. A12.04-K14: token entropy was only weakly and inconsistently associated with whether a spontaneous shift occurs (pooled OR 0.77, CI .58-1.02). A12.04-K16: suppressing switches helped. | Not a clean conflict: one study cues more reconsideration, another cuts switching. The lever is the timing of a switch, not its frequency (A12.04-U15). Entropy is a weak gate (A12.01-U9, A12.04-U5). |
| C3 | **Does a cue help?** A12.01-K13 (single-source): a cue helps only the matching problem type; both at once do not add. A12.04-K04: generic hints give little or no gain. A12.01-K26: a bare "Wait" removes 89.3% of the blind spot in 14 models. | Generic cues are cheap and may work for models even though they fail for people. A named cue must beat Wait, not only no cue (A12.01-U1). |
| C4 | **Where is the bottleneck: generation or selection?** A12.01-K17 and A12.01-K31 (single-source) say the right answer is already in the trace in some wrong answers (5% to 39% in riddles). The A01 synthesis (A01.02-K21, A01.09-K18) says producing the right hypothesis is the bottleneck. | Task-dependent. Riddles with a short answer favour selection; rule induction favours generation. Measure the selection share per class first (A12.01-U3), then pick. |
| C5 | **Sudden or gradual?** A12.01-K06 (single-source): the eye shift is sudden near the end. A12.04-K10: warmth jumps about 15 s before solution. SUBFIELDS.md notes naturalistic work shows insight is often gradual. | Both describe human reports and eyes. No LLM analogue (A12.01 open questions). Do not time operators from these. |
| C6 | **Effect of prior practice and training.** A12.01-K10 (contested): repeating insight set problems helped or hurt by type. A12.04-K11 (contested): non-dot practice raised or lowered nine-dot by content. A12.01-K15 (established) says wrong practice hurts. | Direction depends on whether the practiced frame matches. Test the mental-set penalty inside one context (A12.01-U13, A12.01-U4). |
| C7 | **Do LLMs show spontaneous restructuring?** A12.01-K18 and A12.04-K15 say rare and harmful. SCHEMA S6 says impasse may be about 8% of problems. A12.01-K16 says the gap with people is large. | Consistent if models rarely restructure by themselves and so need a code-fired operator. Rare spontaneous shifts are not a sign that restructuring is unneeded. How often it is needed per class is open (section 7). |
| C8 | **Cross-field: stated confidence.** A12.04-K13 and A12.04-K14 agree with A01 F1 and SCHEMA 4b: confidence is unreliable where it matters (mid-task for some models). A12.04-K14 adds that computed counts may do better, which A01 C6 leaves as a hint only (SCHEMA G4). | Consistent. Test a computed progress variable against the model's report (A12.04-U5). |

## 4. Recurring mechanisms

| Mechanism | Subfields and claims | What it means for the agent |
|---|---|---|
| **Wrong default frame, then a forced change** | 01 (A12.01-K01, K02, K03, K15, K16), 04 (A12.04-K03 and K07 single-source, K21) | Fixation is the failure. List the assumed constraints and units, then drop or split one at a time. Never pair a drop with free continuation only (A12.01-K08). |
| **Code-visible stuck signal** | 01 (A12.01-K27 single-source), 04 (A12.04-K09, K10, K13, K14, K16, K17, K22 single-source) | Trigger from counts, repeats and a computed distance-left over budget-left ratio, not from the model's report. Needs an explicit budget (A12.04-K22). |
| **Right answer present, not kept** | 01 (A12.01-K17, K31), 04 (A12.04-K20) | Harvest every candidate and test by code before adding any operator. |
| **Reflection is mostly confirmation** | 01 (A12.01-K20, K18), 04 (A12.04-K15) | Extra reflection and "aha" talk add tokens, not fixes. Fire change from outside, at a computed impasse. |
| **Maximise visible progress** | 04 (A12.04-K01, K03, K21 single-source) | Greedy moves are the trap. A step that checks a move against the criterion before commit is a candidate, not yet shown for LLMs. |
| **Cues work only when matched** | 01 (A12.01-K13, K25, K26), 04 (A12.04-K04) | Name the constraint or unit, and beat the generic "Wait" baseline. |
| **Fresh frame beats carried frame** | 01 (A12.01-K28 single-source, K10 contested), 04 (A12.04-K11 contested) | Re-enter in a fresh context with a code-written failure summary. Matches SCHEMA S3. |
| **Break rate beside fix rate** | 01 (A12.01-K21), 04 (A12.04-K16) | Every operator is judged by net gain: fixed minus broken. |

## 5. Merged tests

Each row merges UNKNOWNS rows that share one design. Common rules from A12.01: equal total tokens (G7), at least 5 seeds per item, fresh items per condition.

| # | Merged test | Unknown ids covered | One-line design | Priority |
|---|---|---|---|---|
| T1 | **Selection share and answer recognition** | A12.01-U3, A12.04-U14 | Log, per target class, the share of wrong answers whose trace holds the gold answer; compare final-only vs code-checked-all-candidates. 15%+ means harvest becomes mandatory and operators wait. Run first. | High |
| T2 | **Trap item bank and greedy-move check** | A12.04-U4, A12.01-U5 | Build text coin, nine-dot and matchstick items at 3 constraint depths and 2 chunk types, with a solver. Plain arm only: record the maximiser rate and the pass rate per cell. The greedy-move motive rests on A12.04-K03, now single-source (one lab). Everything else reuses this bank. | High |
| T3 | **Stuck trigger comparison** | A12.04-U1, A12.04-U5, A12.04-U6, A12.04-U7, A12.04-U10, A12.04-U15, A12.01-U9 | On T2 items: counter, entropy or verbal confidence, computed distance/budget ratio, thought-switch rate, variation rate, all firing the same intervention; log a sweep of repeat and window thresholds and AUROC at 25, 50, 75% of the run; with and without a stated budget. Add a timing arm (switch only at computed impasse). | High |
| T4 | **Named cue head-to-head** | A12.01-U1, A12.01-U2, A12.01-U8, A12.04-U3, A12.04-U9 | Neutral resample, generic Wait, step-back, named constraint, named unit, forced variation of a never-varied move property, both cues in one prompt, and relax plus criterion (this arm rests on A12.04-K07, now single-source); report net gain and break rate by item type. | High |
| T5 | **Re-representation vs lookahead at impasse** | A12.04-U2, A12.04-U11, A12.01-U7 | After the trigger: O6/O4 only; k-step simulated lookahead only; both; O4 then stated consequences plus code enumeration. Symbolic vs spatial text items. Also lookahead from step 1 vs after failure vs none. | High |
| T6 | **Fresh context re-entry and mental set** | A12.01-U4, A12.01-U13 | After a wrong first answer: continue in context; relabel as a user draft; fresh context with a code-written summary. Plus seeding with solved same-type items vs fresh. | High |
| T7 | **Code-side unit splitter** | A12.01-U6 | Plain; model lists parts; code spells out characters, digits, objects, grid cells. Character-edit puzzles, MathSticks digit edits, ARC-type grids. | High |
| T8 | **Goal property and worked example in S1** | A12.04-U8, A12.04-U13 | Abstract goal alone; restated goal property with a rival reading; key-move example; generic example; tempting-goal example. Solve rate. | Med |
| T9 | **Memory index by constraint type** | A12.01-U12, A12.01-U15 | No retrieval vs retrieve by surface vs retrieve by relaxed constraint type; U15 only if the Ohlsson 2011 chapter is obtained. | Med |
| T10 | **Delta critic and relax-then-verify loops** | A12.04-U12, A12.01-U14 | Residual-delta step critic vs random vs none; LLM proposes a relaxed goal and code checks feasibility. Read the +52% source first. | Low |
| T11 | **Twin-item surface check** | A12.01-U10, A12.01-U11 | Originals, reworded twins and lure-removed twins for the best operator; easy-sibling-then-restore arm on deep items. | Low |

Order to run: T1 first (cheapest, from logs we hold), then T2 (its bank feeds T3, T4, T5, T7), then T3, T4 and T6. T7 is a small code change and can run beside T4.

## 6. Not to add

| Idea | Why not | Claim ids |
|---|---|---|
| The model's own progress report or "warmth" as a mid-run trigger | Mid-task reports were wrong for gpt-4.1 and gpt-5.5 (the weak stage varies by model); AUROC .60 or less at 50%; SCHEMA 4b already bars verbal confidence | A12.04-K13, A12.04-K14 |
| Generic "think outside the box" hints | Little or no gain for people; base rate under 5% on nine-dot | A12.04-K04 |
| Hands-on or physical interaction as an insight aid | Failed in three replications; no analogue for text | A12.01-K11 |
| Treating model "Oh!" or "wait" language as insight | Rare, and goes with lower accuracy | A12.01-K18, A12.04-K15 |
| Forced extra reflection after the first candidate | Over 90% keep the first candidate; wasteful | A12.01-K20 |
| Brain stimulation, eye movement and felt aha as targets | Human physiology, nothing for a text scaffold | A12.01-K12 (single-source), A12.01-K05 |
| Calibrating to human move statistics (Chronicle 2004) | Unreplicated, N=19 per cell | A12.04-K25 (single-source) |
| Both operator cues in one prompt as default | Did not add benefit and sometimes lowered solving in people; single-source, test first | A12.01-K13 (single-source) |
| Hidden-state probes and logit penalties | Need open weights | A12.04-K23 (single-source), A12.04-K16 |
| Incubation or sleep | Already in SCHEMA 4b | SCHEMA 4b |

## 7. Gaps

- **Single lab only: moves that look like progress but enter a dead end lower solving, and layout alone shifts difficulty (6-coin vs 10-coin 10/48 vs 36/48)** (A12.04-K03; all three sources are the Lancaster group).
- **Single lab only: progress monitoring says when to leave the current search, representational change says how; relaxing alone 7% vs 10%, relaxing plus a maximisation criterion 72%** (A12.04-K07; one paper, and Jones 2003 does not propose merging the theories).
- **Single source only: felt progress (warmth) is a poor early predictor, flat until about 15 s before solution** (A12.04-K10).
- **No LLM test of the core theories.** No study runs nine-dot, coin or matchstick problems on language models with a progress criterion (A12.04-K19), and none runs Knoblich's types A to D with tightness labels (A12.01-K23). MathSticks is only a proxy.
- **No head-to-head of stuck triggers.** No threshold ablation and no false-positive rate exists (A12.04-K24). Published gains are bundled (A12.04-K17).
- **No test of named cues against "Wait"** on insight items (A12.01-K25, A12.01-K26).
- **Sources unread.** MacGregor et al. 2001 full text, Ohlsson 1992 and the 2011 chapter, the PRODIGI manuscript, and the Miller, Wiley, Ohlsson cue wording and sample sizes (A12.01-K13, A12.01-K32, A12.04-K12).
- **How common is true restructuring** in our task classes is unmeasured; Ash et al. 2009 is not yet opened. This decides whether any operator is worth building per class.
- **Unresearched subfields** listed in section 1, notably methods and measurement and Gestalt fixation.
- **Bench limits.** Rush Hour 6x6 is too easy for frontier models (about 92%), NoveltyBench has no single-answer check, and effects shrink with model strength. Rerun on the model we ship.
- **No open-ended progress measure** for tasks without a distance (research, writing).

**Source audit, 2026-10-26:** 22 A12 claims were re-opened against their papers (the 20 now established plus A12.04-K03 and A12.04-K07). 14 were confirmed, 6 reworded (all overstated: A12.01-K03, A12.01-K17, A12.04-K04, A12.04-K09, A12.04-K13, A12.04-K14) and 2 downgraded to single-source: A12.04-K03, A12.04-K07. A12.04-K10 was downgraded in the earlier code check and stays out of section 2. Downgraded ids: A12.04-K03, A12.04-K07, A12.04-K10.
