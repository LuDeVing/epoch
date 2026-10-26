# Mathematical problem solving: synthesis

*One view across the field's researched subfields. Built from each subfield's DEEP.md, claims.jsonl and UNKNOWNS.md.*

Notes on use. "Established" means the claim's status in claims.jsonl, set before the stricter independence re-check. Treat each row as a candidate until that check is done. "Contested" and "single-source" claims are named only where they matter for a contradiction or a gap. Schema column checked against `research_notes/single_agent/SCHEMA.md` v0.2. Only 2 of the 9 subfields are researched, so this is a thin view. Most evidence is on non-reasoning models of 2023-24 or on one lab's trace labels.

## 1. Coverage

| Subfield | DEEP.md | Claims | Established |
|---|---|---|---|
| 01 Polya heuristics | [DEEP](subfields/01_polya_heuristics/DEEP.md) | 30 | 5 |
| 04 Episode analysis of reasoning models | [DEEP](subfields/04_episode_analysis_of_reasoning_models/DEEP.md) | 29 | 7 |
| **Total** | | **59** | **12** |

Other statuses: contested 5 (01-K07, 01-K17, 01-K27, 04-K11, 04-K12), unverified 1 (04-K28), the rest single-source (41). Each researched subfield has a UNKNOWNS.md with 15 test rows (30 in all).

Not yet researched (from SUBFIELDS.md): Schoenfeld framework (resources, heuristics, control, beliefs; folder slot 02), metacognition and control in maths (03), expert-novice schemas (Chi et al.), worked examples, teaching heuristics, problem posing and conjecture (Brown and Walter, Lakatos), beliefs and affect. Several claims here rest on Schoenfeld second-hand (01-K03, 04-K23, 04-K28).

## 2. Established findings, merged

For the agent, human results are design hints until tested on our model (section 5).

| # | Finding | Claim ids | Schema part | In SCHEMA.md? |
|---|---|---|---|---|
| F1 | Taught heuristics transfer weakly in people. Gains grow with grade; diagram and representation training gave the largest gain in the meta-analysis. No single strategy fits all students or problems. Do not force one strategy on every problem. | E06.01-K02 | G1, O6 | yes (G1: operators only at S6; O6 change of representation). The "largest gain" for representation is not used to order operators. |
| F2 | Explicit heuristic instruction beat practice-only and no training in one small human replication (about 10 per cell, d 0.79 vs practice). Supports annotated worked examples. | E06.01-K04 | S9, memory | partly (S9 one lesson line; no operator annotation) |
| F3 | Combining methods that solve different items beats either alone, in geometry (AlphaGeometry plus algebra 27/30, random auxiliary points plus heuristics 28/30). | E06.01-K21 | S3, S4, O3 | partly (S3 diversity is stated for open mode only; no union of diverse attempts for checked mode) |
| F4 | A model checking its own reasoning with no outside signal does not help and can hurt (GPT-4 GSM8K 95.5 to 89.0 over two rounds). Finding the first wrong step is hard and gets worse with more calls. Told the true error location, the model fixes most wrong traces; a random location breaks 7 to 16 points of right ones. | E06.01-K25 | G1, G2 | yes (G1, G2, section 4b self-reflection) |
| F5 | Spreading attempts over several named approaches beats the same calls on one prompt, on non-reasoning models with a vote. Gains shrink with model strength and vanish where the model cannot follow the approach. | E06.01-K28 | S3, G4 | partly (G4 bars strategy voters on single-answer problems; this result used a vote, not a verifier) |
| F6 | Within one question, wrong answers are longer and switch thoughts more than right ones. Length is not only a difficulty effect (three papers agree). | E06.04-K06 | G11, S6 trigger | partly (G11 caps length; no length or switch signal at S6) |
| F7 | Models often hold a correct thought and then abandon it. Over 70% of wrong responses contain one (one paper), and models keep generating after a correct answer is injected. | E06.04-K07 | S4 | yes (S4 harvest of dropped candidates). No freeze rule. |
| F8 | The share of steps in abandoned branches predicts failure better than length. Deleting failed branches from wrong traces lifts continuation accuracy (R1 20.89 to 29.42). A short summary keeps 85 to 92% of the gain on R1 but 17 to 81% on GPT-oss-120B. | E06.04-K08 | S5, memory | partly (S5 keeps best-so-far; no pruning or dead-end note) |
| F9 | Overthinking on easy items: the first solution round is correct in over 92% of cases with under 60% of tokens. Later rounds add little. | E06.04-K09 | G11, G12 | partly (G11 think briefly; no early-exit rule) |
| F10 | Reflection after a first answer is mostly confirmatory (over 90% keep the answer; wrong-to-right under 2% typically) at 16.8 to 47.8% of tokens. | E06.04-K10 | G1, 4b | yes (G1, 4b self-reflection) |
| F11 | Models underthink hard problems and overthink easy ones. Missing-premise questions give answers 2 to 4 times longer. | E06.04-K17 | G12, S1 | partly (G12 spends by difficulty; no premise check) |
| F12 | Hidden-state probes and confidence early exit predict a correct intermediate answer (AUC above 0.7) and cut tokens 24 to 39%. Needs weights or an answer-probing call. | E06.04-K18 | G11 (stopping) | no (see section 6 for the weight-needing part; the answer-probe variant is U5) |

## 3. Contradictions between subfields

| # | Conflict | Claims | Reading |
|---|---|---|---|
| C1 | **Control helps vs reflection does not.** Concrete control prompts cut "pick a direction, never check" attempts from about 60% to under 20% (single-source, no N). Yet generic review and reflection mostly confirm and use many tokens (established). | E06.01-K03 vs E06.01-K25, E06.04-K10 | Probably not a real conflict. The helpful control is concrete (what are you doing, why, how does it help) and the human result is about people who do not check at all. Model reflections already check too much. Test: E06.01-U3. |
| C2 | **Verify helps vs review hurts.** Lasso on Schoenfeld labels gives Verify share a positive weight (+0.21), while Feng finds more review goes with lower accuracy. | E06.04-K12 vs E06.04-K06, E06.04-K26 | Label definitions differ: review is broader than Verify. Check position is not controlled in any study. Test: E06.04-U2. |
| C3 | **Extra thinking.** Forced "Wait" first helps then hurts in one study; budget forcing helped on AIME24 in another. | E06.04-K11 | Starting budget and model likely moderate. Same split as C01.08-K11. Test: E06.04-U15. |
| C4 | **Generic prompts on reasoning models.** Menus and chain-of-thought gave gains on older models (01-K08 to K13) but marginal or mixed gains on reasoning models. | E06.01-K27 vs K08, K10, K13, K14 | Gains shrink as the base model gets stronger; most positive numbers are GPT-3/3.5 era. Do not carry them to a reasoning model. Test: E06.01-U1. |
| C5 | **Do models self-check?** Self-correction without outside signal hurts (2023-24 models), but reasoning models find errors much better when judging another solution (first-error F1 87.9 for o1-mini). | E06.01-K25 vs E06.01-K26 | Different setups (self vs other, old vs new model). Not settled for live self-checks. Test: E06.01-U3 with a mid-attempt interrupt (needs harness support). |
| C6 | **Strategy voters.** SCHEMA G4 bars strategy voters on single-answer problems. E06.01-K28 shows approach-split sampling with a vote beats plain sampling. | E06.01-K28 vs G4 | G4 targets persona voters that share one model's errors. Approach-split attempts that code verifies are a different design. Test: E06.01-U2. |
| C7 | **Heuristics vs stored schemas.** Expert success may rest on stored problem schemas, not general heuristics. | E06.01-K07 (contested) | Open. Expert-novice subfield not researched. Test: E06.01-U15. |
| C8 | **With C01 synthesis.** C01 F3 and F10 say the same as F10 and F9 here (confirmatory reflection, overthinking on easy items). E06.04-K18 early exit via probes fits C01.08 but both need weights. | E06.04-K09, K10, K18 | Agreement, so these are two-field support for 4b and G11. |
| C9 | **With A12 and E09 syntheses.** A12 says impasse should be fired from outside by code and E09 says local repair cannot fix a wrong design; E06.04-K08 (failed branches) and K06 (switch rate) offer candidate signals for that trigger. A02 C5 (decompose always or after failure) is the same question as E06.01-K12 (decomposition helps at 5+ steps, hurts at 2). | E06.04-K06, K08, E06.01-K12 | Consistent. The trigger comparison belongs in one shared test (see section 5, M1). |

## 4. Recurring mechanisms

| Mechanism | Where | What it means for the schema |
|---|---|---|
| **Outside signal needed to change an answer** | 01-K25, 04-K10, 01-K16 (wrong hints hurt) | Revise only from a located failure (G1, G2). Wrong or random locations and hints cost 7 to 16 points. |
| **A correct candidate is reached then lost** | 04-K07, 04-K08, 01-K11 (abstraction fine, reasoning after it fails) | Keep and test candidates; judge the step after an operator, not the operator. |
| **Gain shrinks as the model gets stronger** | 01-K10, K14, K23, K28, 04-K11, K19 | Every helper must be tested on the current model at equal tokens (G7). |
| **Length and switching track failure** | 04-K06, K08, K09, K17 | Cheap text counts may form a stuck signal. Not validated (04-U1). |
| **Selection of the approach is the bottleneck** | 01-K12, K13, K17, K23 | Choosing the decomposition or operator matters more than carrying it out. Router accuracy caps the gain. |
| **A label hides several procedures** | 01-K01 (single), 04-K03 | Operators need a procedure and trigger, not a name. Episode labels need a guidebook. |

## 5. Merged tests

| Merged test | Unknown ids covered | One-line design | Priority |
|---|---|---|---|
| M1 Stuck signal from text counts | E06.04-U1, E06.04-U12, E06.04-U14 | Log 20 problems x 10 runs; fit switch, wait/backtrack, repeat, failed-branch counts against length with problem-grouped folds; check per domain and with a cheap labeller. Share logging with A12 T3. | High |
| M2 Operator menu vs bare vs plain sampling | E06.01-U1, E06.01-U13, E06.01-U14, E06.04-U13 | Bare / menu at S6 / one operator per attempt + vote / plain samples + vote, at equal tokens; add leave-one-operator-out ablation. | High |
| M3 Approach diversity with a verifier | E06.01-U2 | k approach-split attempts + verifier vs k plain + verifier vs approach-split + vote, on items with a code check. | High |
| M4 Concrete control step and check placement | E06.01-U3, E06.04-U2, E06.04-U6 | None / generic review / three-question step on coded trigger / same on schedule / one final check / mid-trace checks / risk-conditional verify; log right-to-wrong flips. Overlaps C01 T5. | High |
| M5 Dead-end handling | E06.04-U3, E06.04-U4, E06.04-U8 | Keep, delete, one-line note, summary of failed branch; add gated finish-or-abandon rule and freeze of a checked candidate. | High |
| M6 Black-box stop rules and caps | E06.04-U5, E06.04-U7, E06.04-U10, E06.04-U15 | Fixed cap vs n-gram stop vs trial-answer stability vs difficulty-based cap vs 1x/2x/4x turns vs shortest-of-k, by difficulty bin. Overlaps C01 T7. | High |
| M7 Operator record and ordering | E06.01-U4, E06.01-U5, E06.01-U9, E06.01-U7, E06.01-U6 | Label vs procedure vs procedure+trigger+example; O6 first vs other orders; code-feature router vs oracle; step-count gate on O3; O5 as forward rewrite or substitution check. | High |
| M8 Rendering and hygiene | E06.01-U10, E06.01-U11, E06.01-U12, E06.04-U9 | Prose vs JSON plan; restate-and-check; injected wrong hint with and without S1 hygiene; premise check on unsolvable items. | Med |
| M9 Worked examples and templates | E06.01-U8, E06.01-U15 | Annotated vs plain vs no example after first attempt; template retrieval vs generic menu on seen and unseen classes. | Med |
| M10 Impasse types | E06.04-U11 | Code failure type on 100 failed runs; check operator success by type. | Low |

## 6. Not to add

| Idea | Why not | Claims |
|---|---|---|
| Generic "check your work" or review step on a schedule | Mostly confirms, costs 17 to 48% of tokens, can break right answers; already in 4b | E06.01-K25, E06.04-K10 |
| Random or self-guessed error locations and hints without a check | Break 7 to 16 points of right traces; wrong hints fall below chain-of-thought | E06.01-K25, E06.01-K16 |
| Hidden-state probes, early-exit by internals, decoding penalties (TIP, DEER probes) | Need weights or logits; a text scaffold cannot reach them | E06.04-K18, K19, K21, K29 |
| Fine-tuning on Polya dialogues, RL with heuristic priming | Training is out of scope; no accuracy gain measured for the dialogues | E06.01-K18, K19, K20 |
| Rigid or drilled operator scripts, JSON-structured plans | Drilling removes flexibility; prose plan beat JSON by 9 to 12 points (single-source) | E06.01-K05, K06, K30 |
| Backward solving as the main route | GPT-4 92.8 forward vs 38.6 backward; use only as rewrite or check | E06.01-K15, K29 |
| Human percentages for "novices never monitor" | Not verified (404 and 403 sources) | E06.04-K28 |

## 7. Gaps

- 7 of 9 subfields unresearched, including Schoenfeld's framework, metacognition and expert-novice sorting. The control claim, the strongest idea in the field, rests on one chapter with no N.
- Almost no data on current reasoning models for Polya operators; most positive numbers are GPT-3/3.5 era or PaLM-2.
- Episode work comes from one lab (Li et al., ThinkARM), SAT maths, open R1-like models. No third-party replication and no held-out test of Schoenfeld labels as a predictor.
- No human stuck labels, so no detector precision or recall.
- No equal-token numbers in any published Polya prompt paper.
- Selection versus execution split of operators is unmeasured (needs hand-written plans).
- Frontier models with hidden reasoning: shapes of traces unknown.
- Hembree effect sizes and the Schoenfeld 1979 replication at scale are missing; only human calibration depends on them.

**Audit (code check, 2026-10-26):** E06.01-K04 had only one opened source and are now single-source, not established. Treat their rows above as unconfirmed.
