# Naturalistic and expert decision making: synthesis

*One view across the field's researched subfields. Built from each subfield's DEEP.md, claims.jsonl and UNKNOWNS.md.*

Notes on use. "Established" means the claim's status in claims.jsonl. This field was synthesised before any source audit, so established claims here have not been re-opened the way A01's were; treat the weakest ones with care (flagged in section 7). Many established claims are about humans (Klein's interviews, chess, forecasting, clinicians). For the agent they are design hints until tested on our model (section 5). Schema column checked against `research_notes/single_agent/SCHEMA.md` v0.2.

## 1. Coverage

| Subfield | DEEP.md | Claims | Established |
|---|---|---|---|
| 01 Recognition-primed decision and mental simulation | [DEEP](subfields/01_rpd_and_mental_simulation/DEEP.md) | 31 | 14 |
| 05 Conditions for valid intuition | [DEEP](subfields/05_conditions_for_valid_intuition/DEEP.md) | 24 | 6 |
| **Total** | | **55** | **20** |

Contested: 8 (2 in 01, 6 in 05). Single-source: 27 (15 in 01, 12 in 05). Each subfield has a UNKNOWNS.md with 15 test rows (30 in all).

**Not yet researched** (from SUBFIELDS.md): sensemaking and the data-frame model (covered in the E10 synthesis, not here); pre-mortem as its own subfield (only K28 and K29 of subfield 01 touch it); cognitive task analysis; expert-novice differences (chunks and cues); naturalistic decision making in sport (only handball data is used, K04); heuristics and biases (only as contrast, SCHEMA 4b already holds the main result). Mental simulation was folded into subfield 01, so it is covered. The subfield numbers 02 to 04 and 06 to 09 are not allocated to folders.

## 2. Established findings, merged

Schema column: yes (where) / partly / no. All rows are status established.

| # | Finding | Claim ids | Schema part | In SCHEMA.md? |
|---|---|---|---|---|
| F1 | RPD frequency is not a constant 80%. It ranges 42 to 80% in Klein's own table, 46 to 96% in Ambur, and about 34% in a pilot simulator study. Do not hard-code a recognise-first prior. | E04.01-K01 | S0, section 6 | partly (S0 modes exist; no rule against a fixed fast prior; the logging list has no "route taken") |
| F2 | The RPD frequency evidence is retrospective interview with team coders and no outcome control. It shows reported process, not better process. Judge any recognition-first design by outcome accuracy, not by the route the agent says it took. | E04.01-K03 | G10 | partly (G10 says reasoning text is not evidence; no explicit "route report is a story") |
| F3 | For experts the first option is often good (handball, strong chess), but the take-first advantage needs expertise: weaker chess players' first move was no better than later ones. So the fast path needs a familiarity signal, and where there is none, widen the options. | E04.01-K04, E04.01-K05 | S0, S3 | partly (G12 spends by difficulty; no familiarity-scaled option count) |
| F4 | First-move quality depends on task type. Experts' first moves were worse in calculation-heavy positions than in pattern-heavy ones under time pressure. Route calculation-type and exact-answer items to checking. | E04.01-K06 | S0 | partly (S0 chooses mode by class; no pattern vs calculation split) |
| F5 | Time pressure harms even elite players (grandmaster expected blunders per move nearly doubled in blitz). Cutting deliberation has a cost expertise does not remove. Report the loss curve per class. | E04.01-K07 | G11, G12 | partly (G11 caps thinking; says nothing on measuring the loss curve per class) |
| F6 | Slow checking helps people mainly when salient but irrelevant features mislead (residents 43 to 52%, students no gain; training in reflection did not transfer). Trigger the extra check on a signal, never always. | E04.01-K10 | G1, G12 | yes (G1; 4b bars "be careful" prompts) |
| F7 | Model-based rollouts with search beat plain chain of thought on multi-step planning (Blocksworld, Game of 24), but those comparisons are not token-matched. | E04.01-K12 | O, S4 | partly (O7 and section 7 slot "tree search"; no rollout element) |
| F8 | Part of the search gain is just more samples (best-of-100 CoT 49% on Game of 24; 25 plain samples 42% beat verifier back-prompting 36 to 38%; heavy search lowers accuracy on easy items). Every rollout or search element needs a best-of-N arm at equal tokens. | E04.01-K13 | G7, G12 | yes (G7 equal tokens; G11 and G12 cite the same pattern) |
| F9 | LLM self-checking with no outside signal does not help and can hurt (CommonSenseQA 75.8 to 41.8). A sound external verifier gives large gains (Blocksworld 40% unaided, 55% LLM critic, 88% sound verifier). | E04.01-K15 | G2, S4 | yes (G2; 4b "unstructured self-reflection") |
| F10 | Check quality drives most of the check-and-revise gain: sound verifier 88%, LLM critic 55%, none 40%; web tree search 24.5% with no value function, 37.0% with a GPT-4o value, 43.5% with ground truth. Trust order at S4: executed code, rule check, retrieval-grounded walk-through, model's own walk-through (never alone). | E04.01-K27, E04.01-K15 | S4, G2, G3 | partly (G2 and G3 say "real output"; no trust order among checks; model walk-through not named) |
| F11 | LLMs are unreliable world simulators: best accuracy about 60% on non-trivial state changes, and rollouts drift over long procedures. Retrieval grounding lifts plan alignment from 50 to 65% to 85 to 95%. Keep unreferenced rollouts short. (The grounding numbers rest on one paper, see section 7.) | E04.01-K16 | O, S4 | no |
| F12 | Imagining each candidate's outcome and scoring it beats a reactive agent modestly (VisualWebArena 17.6 to 23.6) and is far cheaper than real tree search ($0.4 vs $2.7), though real search still wins in some domains. | E04.01-K17 | S3, S4, O | no |
| F13 | A cheap first-sample gate exists on reasoning benchmarks. Group confidence of the first sample (AUROC 0.86) accepts 49 to 61% of GSM8K at 91 to 99% accuracy; reasoning-vs-program agreement resolves 78.6% with two samples; Bayesian stopping cuts calls 58% at -0.4 points. It fails where confidence is uninformative (GPQA), so calibrate per class. | E04.01-K25, E04.05-K15 | S0, S3, S7, G12 | partly (G12 "spend by difficulty"; G4 says agreement is a hint; no early-exit ladder or per-class gate calibration) |
| F14 | Skilled fast judgment needs two checkable conditions: a regular environment with valid cues, and enough practice with feedback in it. Without both, a correct first answer is luck. Basis is conceptual (two rival authors converged), not an experiment. | E04.05-K01 | S0, memory | partly (S0 and the class record exist as [S] and [D]; no validity flag, graded count, or grade-independence flag) |
| F15 | Felt confidence in one answer does not separate skilled from heuristic intuition; it tracks story consistency. Never use stated confidence, fluency or explanation length as the trust test. | E04.05-K02 | G5, S0 | yes (4b bars verbal confidence as a stop signal; G5 length-normalises judges). Length-as-trust is not named. |
| F16 | Mechanical combination of the same cues beats or ties expert holistic combination in low-validity prediction (Grove 2000: 136 studies, mechanical better in 63, tie in 65, clinician better in 8; Kuncel 2013 job performance r .44 vs .28). The edge is small in mental health (Aegisdottir d+ = .12; 52% of effects favour the formula, 38% tie, 10% favour the clinician). Estimate it per class; do not assume a large edge. | E04.05-K03, E04.05-K04 | S7, G5 | partly (G5: code selects; no cue-rubric step; human data only) |
| F17 | Chain of thought hurts on tasks where verbal deliberation hurts people (implicit pattern learning GPT-4o -23.1 points; face recognition -12.8) and helps mainly on math and symbolic tasks. So the fast path is better for some classes, and the mode must be chosen per class. | E04.05-K16 | S0, G11 | partly (G11 "think briefly"; S0 modes exist; no per-class mode table from the record) |

Items that are well supported as ideas but sit at single-source status are in section 7 and not here.

## 3. Contradictions between subfields

Within E04:

| # | Contradiction | Claims | Reading | Action |
|---|---|---|---|---|
| C1 | **How common is recognition-first?** Klein's 80% against 58% (experts on hard points), 46% (novices), about 34% (pilots) and Ambur's 46 to 96%. | E04.01-K01, E04.01-K02 | The numbers depend on how a decision point is defined and coded. Established K01 itself records the spread. | Log the route per item (F1). Do not use any of these numbers as a prior. |
| C2 | **Is the first option safe?** Handball and strong chess say yes (K04). Weaker players and calculation-heavy positions say no (K05, K06). The valid-intuition subfield says it is safe only where the class has valid cues and feedback (E04.05-K01). | E04.01-K04, K05, K06; E04.05-K01 | Consistent once the condition is named: expertise + regular cues + feedback. The two subfields give the same gate from two sides. | One S0 gate; see E04.01-U2 and E04.05-U1 merged in T1. |
| C3 | **Simulation as the check.** Klein presents mental simulation as the check on the first option (DEEP 01 section 5.6). LLM self-simulation checks are poor (K15, K16, K27). Grounded or external simulation helps. | E04.01-K15, K16, K27, K19 (contested), K31 (single) | Works when the simulator is external or sound; a model's own walk-through is only a hint. | Keep F9 and F10. Do not call a model walk-through a check. |
| C4 | **Best rollout depth.** MENSA says 3, web tree search gains up to 5, reasoning models search 1.78 plies and depth did not predict wins while breadth did. | E04.01-K20 (contested) | Not settled. Differences in value function, domain and whether the simulator is real. | Keep the cap of 3 as [D] until E04.01-U4. Also test breadth. |
| C5 | **Does more thinking help?** Time pressure harms experts (K07, established) and search helps planning (K12) against more thinking tokens worsening calibration (E04.05-K13, contested) and slow mode helping only 3.11% of items (E04.05-K17, single). | E04.01-K07, K12; E04.05-K13, K17 | Different manipulations: cutting time from a good level, versus adding tokens past a small budget. | Per-class budget sweep (T6). Report both ends of the curve. |
| C6 | **Is confidence usable?** Confidence of the first sample has AUROC 0.86 on GSM8K (E04.01-K25) and verbal confidence is better calibrated than token probability (E04.05-K11, contested). Against: felt confidence does not separate skill (E04.05-K02), and Kapoor finds verbal and sampling signals weak on MMLU. | E04.01-K25; E04.05-K02, K11, K15 | Group confidence from sampled traces is not the same signal as a single stated number. Both fail on hard open sets. | Never use stated confidence alone. Test sample-based signals per class (T1). |
| C7 | **Practice versus familiarity.** Clinicians did better on data from outside their own setting (E04.05-K06, contested), yet E04.01-K02 says recognition use rises with experience. | E04.01-K02, E04.05-K06 | Both fit the rule that experience without feedback does not make a skill. Nobody tested it directly. | No action beyond the feedback condition in F14. |
| C8 | **Checking after the first answer.** E04.05-K09 (speed and diagnosis, single) says correct diagnoses were faster, so slowing down is not shown to help. E04.01-K10 says slow checking helped residents on misleading cases. | E04.01-K10; E04.05-K09 | Compatible: checking helps only on misleading cases; item difficulty explains speed. | Keep F6: trigger on a signal. |

With other fields:

| # | Contradiction | Note |
|---|---|---|
| X1 | **Stated confidence.** A01 C6, A04 C1/C8, C01 and E08 treat stated confidence as barred or weak. E04.05-K02 agrees. E04.05-K11 (contested) and A04.03-K21 (post-reasoning confidence discriminates) are the exceptions. | Consistent with SCHEMA 4b. Elicit only after reasoning if used at all (A04.03-U8). |
| X2 | **Self-correction.** A04 C5 and E10 C2 say the answer depends on checkability and that modern reasoning models may correct in context (contested). E04.01-K15 and E04.05-K14 (single) rest on 2023-era GPT-3.5 and GPT-4 numbers. | Treat the E04 numbers as dated. Resolve by checkability, not model age. Keep G2. |
| X3 | **Agreement as a signal.** A04 C7 says agreement picks where to spend, not what to submit, and notes a floor of confident-wrong items. C01 says agreement is a candidate signal after tests. E04.05-K15 and E04.01-K25 use agreement as an accept rule. | Consistent only if the accept rule is paired with an outside check or a class record. E04.05-U4 tests this. |
| X4 | **Reframing and first reading.** E10 C2 asks whether questioning the first answer helps. E04.01-K29 (single) and E04.01-K28 say the counter-cue or premortem has thin evidence. | Consistent. Do not add a counter-cue step until E04.01-U6 passes. |
| X5 | **Debate.** E04 does not use it; the roles in E10.03-K19 (no control) conflict with G9. | No E04 action. |

## 4. Recurring mechanisms

| Mechanism | Where it appears | What it says |
|---|---|---|
| **Gate by class, not by agent** | E04.01-K23, K25; E04.05-K01, K07, K17, K19 | Trust belongs to a task class with a record of graded outcomes, not to the model as a whole or to one item's feeling of confidence. |
| **Sound check beats imagined check** | E04.01-K15, K19, K21, K27, K31 | The size of any check-and-revise gain tracks the quality of the check. Executed or rule-based checks win; a model's own walk-through is low trust. |
| **Search gain vs sample count** | E04.01-K12, K13, K20; E04.05-K15, K16 | Many "search" wins shrink against best-of-N at equal tokens. Every deliberation element must beat plain sampling. |
| **Fast path needs a validity condition** | E04.01-K05, K06, K23; E04.05-K01, K16 | Fast answers are good where cues are valid and feedback let someone learn; otherwise they are luck. Applies to people and, as a hypothesis, to LLMs. |
| **Cheap signal first, deliberate on trouble** | E04.01-K10, K18, K25, K26; E04.05-K15, K17 | Escalate on a code-detected signal (disagreement, failed check, misleading cue), not on schedule (G1). |
| **Noise from inconsistency** | E04.05-K03, K05, K20 | Formulas win mostly because humans apply cues inconsistently. A single LLM draw is also one noisy draw. |
| **Retrospective report is not a mechanism** | E04.01-K03, K09; E04.05-K18 | Frequency and explanations are stories. Judge by outcome. Ties to G10. |

## 5. Merged tests

Per-subfield tests are in each UNKNOWNS.md (30 rows). They merge as follows. Nothing here goes into SCHEMA.md until its test passes. Order to run: T1 and T2 first.

| Test | Unknown ids covered | One-line design | Priority |
|---|---|---|---|
| **T1 Class-record gate and trust signal** | E04.01-U2, U3, U13; E04.05-U1, U2, U3, U13 | On mixed kind and wicked classes, compare always-checked, always-direct and a gate that reads class hit rate, 5-sample agreement and first-sample confidence; sweep graded cases (10 to 1000); report AUROC per class, accuracy and tokens at equal total tokens. Include the "first sample vs mean of 8 samples" check (U13), which reuses logs. | High |
| **T2 One candidate plus sound check vs best-of-N** | E04.01-U1, U8, U10 | Items with an executable check. Arms: 1 candidate + sound check + 2 repairs; majority best-of-N; sound-verifier best-of-N; plain; router that escalates on stuck signal. Metric: held-out pass rate per class at equal tokens, 3 seeds. | High |
| **T3 Early-exit ladder outside math** | E04.05-U4, E04.01-U8 | Fixed 5 votes vs ladder (agreement only) vs ladder (record + agreement) on three non-math classes plus math. | High |
| **T4 Mode per class** | E04.05-U9, U10, E04.01-U5 | Direct vs short CoT vs extended thinking per class at equal tokens, plus a thinking-budget sweep (0 to 10000), plus an RPD prompt vs a length-matched neutral prompt on judgement items. | High |
| **T5 Rollout depth, grounding and evaluator quality** | E04.01-U4, U11, U12, U15 | Depth 1, 2, 3, 5 imagined vs executed on planning items; add a grounded arm; first measure value-rating AUROC on labelled partial states; add a no-check vs model critic vs sound checker ablation to size the check effect. | High |
| **T6 Counter-cue and expectancy steps** | E04.01-U6, U7, U14 | Walk-through vs walk-through + counter-cue vs walk-through + length-matched neutral step; a second arm adds an expectancy line whose mismatch triggers S6. Metric: false-accept rate and held-out pass rate. | Med |
| **T7 Prototype vs case memory and harness-held record** | E04.01-U9; E04.05-U11 | Same stored content as raw cases, a prototype summary, both; and counter vs in-context history under clean, noisy and delayed grades. | Med |
| **T8 Out-of-class alarm and noise** | E04.05-U5, U8 | Inject 10% and 30% out-of-class items; compare no alarm, embedding-distance alarm, distance + agreement; separately run 5 identical runs per item and test majority of 3 or 5 against single draw. | Med |
| **T9 Cue rubric plus base rate** | E04.05-U6, U7 | Prediction items with 4 to 8 cues: holistic vs model-rated cues summed in code vs fitted weights; add a base-rate line placed after the question. Metric: AUC and Brier. | Med |
| **T10 Outside-check re-ask and early-validity proxy** | E04.05-U12, U13, U14, U15 | Re-ask with no new information vs with test output; early proxy from 3 to 5 graded cases vs later hit rate over 15 classes; scored forecast loop; gate with and without the explanation. | Low |

## 6. Not to add

| Idea | Why not | Claims |
|---|---|---|
| A fixed "recognise first" prior (for example 80%) | The observed rate ranges 34 to 96% across studies and rests on retrospective interviews | E04.01-K01, K03 |
| Stated confidence, fluency or explanation length as the trust test | Confidence tracks story consistency and does not separate skill from heuristic; longer explanations raise confidence without better discrimination (the second is single-source) | E04.05-K02 (established); K18 (single) |
| A model's own walk-through as a check that certifies a pass | Self-check without an outside signal does not help and can hurt; world simulation is about 60% on non-trivial changes | E04.01-K15, K16, K27 |
| A search or rollout element without a best-of-N arm at equal tokens | Much of the gain is extra samples | E04.01-K13 |
| The "30% more reasons" premortem figure | Not found in the primary paper's abstract; human support is thin | E04.01-K29 (single) |
| Assuming a large formula edge over holistic judgement | Small in mental health (d+ .12) | E04.05-K04 |
| Re-asking a distrusted answer with no new information | Does not help and often hurts (single-source; same rule as 4b) | E04.05-K14 (single) |

Several rows duplicate SCHEMA 4b on purpose: the E04 evidence is a second source for them.

## 7. Gaps

- **Single-source claims carrying a design idea.** E04.01-K02 (familiarity gate, one table), K08 (about 3 moving parts in a simulation), K11 (RPD prompt +4.3 points, a data-frame prompt did nearly as well, no length control), K14 (rollouts need a capable evaluator), K18 (SwiftSage, fine-tuned fast module), K21 (reflection depends on trustworthy failure signal), K22 (prototype vs case), K23, K28, K29, K30 (strategy memory, confounded), K31 (retrieval grounding; the numbers in established K16 come from the same paper). E04.05-K05, K07, K08, K09, K12, K14, K17, K18, K19, K20, K22, K23.
- **Established but conceptual or human-only.** E04.05-K01 is conceptual (two authors converged; no experiment). E04.05-K03 and K04 are human-only. For the agent they are arguments, not shown effects.
- **Established with a weak spot.** E04.01-K16 includes numbers from a small probe sample judged by an LLM on older models. E04.01-K12's comparisons are not token-matched. E04.01-K25 shows the gate failing on GPQA, so it is "established to exist", not "established to work on our tasks".
- **Dated models.** Several numbers come from GPT-3.5, GPT-4 and 2023-era models (E04.01-K15; E04.05-K14, K21). Re-run on the model we use before using the sizes.
- **Primary sources not retrieved.** Calderwood, Klein and Crandall (1988) and Klein et al. (1995) chess numbers; Mitchell, Russo and Pennington (1989) premortem paper; Shanteau (second-hand only); Goldberg and Karelaia and the Noise book (second-hand); Mellers 2015 and the 2025 reanalysis (abstract only); Michael 2026 (summary page only); rebuttals to the Apple puzzle study.
- **No LLM evidence for the core RPD claim.** No token-matched test of one candidate plus check vs best-of-N exists (E04.01-U1). No test of Klein-style incident decisions against human experts (E04.01-K24, single).
- **No bench for delayed or agent-influenced feedback.** The independence flag on grades cannot be validated; cue validity is not a measured quantity (see the "cannot test yet" lists in both UNKNOWNS.md).
- **Unresearched subfields.** Cognitive task analysis, expert-novice differences, NDM in sport, heuristics and biases, and a dedicated pre-mortem pass (section 1).
- **Contested and unresolved.** Rollout depth (E04.01-K20), value of environment simulation (K19), thinking-budget effect on calibration (E04.05-K13), forecasting training (K10), harness counter vs in-context history (K21), out-of-class detection (K24), verbal-confidence calibration (K11).
- **No audit yet.** Unlike A01, E04's established claims have not been through a source audit. A first audit pass should target E04.01-K12, K16, K17, K25 and E04.05-K01, K15, K16, which carry most of section 2.

**Audit (code check, 2026-10-26):** E04.01-K07 had only one opened source and are now single-source, not established. Treat their rows above as unconfirmed.
