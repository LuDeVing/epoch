# Metacognition: synthesis

*One view across the field's researched subfields. Built from each subfield's DEEP.md, claims.jsonl and UNKNOWNS.md.*

Notes on use. "Established" is the status in claims.jsonl, set before any stricter independence re-check. Treat each row as a candidate until that check is done. Many established numbers come from 2023-era or open models, so for our agent they are design hints. Schema column checked against `research_notes/single_agent/SCHEMA.md` v0.2. Claim ids are global. Two of the nine subfields are researched, so this is a partial view of the field.

## 1. Coverage

| Subfield | DEEP.md | Claims | Established |
|---|---|---|---|
| 03 Accuracy and dissociation of monitoring | [DEEP](subfields/03_accuracy_and_dissociation_of_monitoring/DEEP.md) | 27 | 18 |
| 08 LLM metacognitive harness | [DEEP](subfields/08_llm_metacognitive_harness/DEEP.md) | 29 | 10 |
| **Total** | | **56** | **28** |

Other status counts. 03: 5 single-source, 2 contested, 2 untested. 08: 12 single-source, 6 contested, 1 untested. UNKNOWNS.md rows: 14 (03) and 15 (08), 29 in all.

Not yet researched (numbering follows SUBFIELDS.md order; folder numbers 03 and 08 match it):
01 Monitoring and control framework (Nelson and Narens), 02 Metamemory judgments (EOL, JOL, FOK), 04 Metacognitive knowledge (declarative, procedural, conditional), 05 Metacognitive regulation, 06 Confidence and signal-detection measures (Fleming and Lau), 07 Meta-reasoning (Ackerman and Thompson), 09 Social, organisational and clinical metacognition (low value, does not transfer).

## 2. Established findings, merged

| # | Finding | Claim ids | Schema part | In SCHEMA.md? |
|---|---|---|---|---|
| F1 | Confidence is inferred from cues (fluency, ease, partial information, self-consistency), not read from memory. Cues that are valid on typical items fail when ease and correctness come apart. | A04.03-K01, A04.03-K06 | G10 | partly (G10 says reasoning text is not evidence; no cue-failure rule) |
| F2 | A single verbalised LLM confidence is weak. It clusters at 80 to 100%, GPT-4 AUROC is 62.7 against 50 for chance, and a low ECE can come from saying 100% on everything when accuracy is high. Raw confidence from open reasoning models averages ECE 0.268 and AUROC 0.635. | A04.03-K07, A04.03-K12, A04.08-K09, A04.08-K26 | G (calibration), S0 | partly (4b bars verbal confidence as a stop signal; ECE-only trap not stated) |
| F3 | Agreement across several samples predicts correctness much better than one stated number (GSM8K AUROC 54.8 to 92.7 with 5 samples). Semantic entropy beats a plain count. | A04.03-K08, A04.08-K09 | S3, S7 | partly (G4: agreement is a hint, never proof; no AUROC evidence) |
| F4 | Confidence stated after real reasoning discriminates; stated before reasoning it does not (R1-32B AUROC 0.56 with no reasoning, 0.80 after 100 to 500 tokens). Open 32B models only. | A04.03-K21 | S, G | no |
| F5 | The consistent-and-wrong set caps agreement. 5.5% to 10% of agent tasks are consistent-wrong. On GPQA one strong tier is wrong on 48% of cases with agreement at least 0.8, and 28% of items are confidently wrong for every runner. | A04.03-K20 | G4, S8 | partly (G4 hint-only; the size of the floor is new) |
| F6 | Self-correction without outside feedback does not reliably help and can hurt (GPT-3.5 CommonSenseQA 75.8 to 38.1; GPT-4 GSM8K 95.5 to 89.0). Gains appear with an oracle or reliable external feedback. Confidence-gated revision is the proposed fix. 2023-era models only. | A04.03-K14, A04.08-K10 | G1, G2, S5 | yes (G1, G2, 4b) |
| F7 | A model that scores its own output is biased toward it, and the bias grows over self-refinement rounds. Larger models and accurate outside feedback reduce it. | A04.08-K12 | G5 | yes (G5, G8) |
| F8 | Stopping sampling when answers agree saves compute at near-zero loss for strong models (33.8% to 84.2% fewer samples; GPT-4 change 0.00). Weaker models lose more. Confidence-weighted stopping saved 41% to 46% at budget 5 and 10. | A04.03-K15, A04.08-K13 | S0, S3, S7 | partly (G11 prefers short attempts; no early-stop rule) |
| F9 | Compute should follow difficulty. Easy items gain from sequential revision, medium and hard from search. Routing by complexity matched multi-step quality at lower cost. Allocating samples by probe disagreement beat uniform allocation by +2.5 in small and mid open models. The cost of estimating difficulty is not counted. | A04.08-K14, A04.08-K16, A04.08-K24 | S0, G12 | yes (G12); router and probe-disagreement allocation partly |
| F10 | Calibration maps must be per task type, built from labelled runs of the target slice. They gave gains from 5 to 20 items per slice. A trained confidence head transfers only partly to new domains. Fixing ECE does not fix resolution. | A04.03-K10, A04.03-K17, A04.03-K25 | M (class record), S0 | partly (section 5 class record has pass rate and agreement record; no calibration map) |
| F11 | Reported calibration numbers move with protocol: the token-score context flips the best method in 4 of 12 (ECE) and 9 of 12 (AUROC) settings; accepting an alias shifts verbal confidence by 0.072. | A04.03-K16 | G7, logging | partly (G7 equal tokens; no protocol-fixing rule) |
| F12 | Verbalised confidence beats token probability for ECE on RLHF chat models, but discrimination stays weak. Asking for top-k answers helps ECE. | A04.03-K09 | G5 | partly (G5 normalises probabilities in code) |
| F13 | Confidence wording changes how readers act, and strengtheners sit on 17% of wrong answers. | A04.03-K13 | G5 | partly (G5 length normalisation) |
| F14 | Forced extra thinking ("Wait" budget forcing) has diminishing returns and is not uncertainty-gated. Gains flatten near 6x. | A04.08-K20 | G11, S6 | partly (G11 think briefly) |
| F15 | Models have no stable act-or-escalate stance when errors have costs. Implicit thresholds vary from 53% to 91% accuracy within one family and are not predicted by scale. | A04.08-K28 | G6, S8 | partly (G6 never abstain on first pass; thresholds must be set in code) |
| F16 | The Dunning-Kruger quartile pattern is largely a statistical artefact. | A04.03-K04 | none | no (human only; see section 6) |
| F17 | A judgment made later, or from a fresh retrieval attempt, sorts right from wrong much better than one made right away (g = 0.93 on resolution, 4,554 people), with almost no effect on memory itself (g = 0.08). Human data only. | A04.03-K02 | G10, S7 | no (nearest: a fresh-context check; untested for models) |

## 3. Contradictions between subfields

| # | Where they disagree | How to resolve |
|---|---|---|
| C1 | **Is a stated confidence usable?** A04.03-K07, A04.03-K22 (agent AUROC 0.51 to 0.64) and A04.08-K26 say weak. Single-source A04.08-K08 reports Sonnet 4.6 JOL AUROC 0.745 and joint 0.757. Contested A04.08-K25 says one stated score plus 2-sample agreement reaches 84.2 in math. A04.03-K21 says the post-reasoning score discriminates. | Model- and class-dependent. Keep SCHEMA 4b until A04.08-U4 and A04.08-U5 pass on our model. If used, elicit only after reasoning (A04.03-U8). |
| C2 | **Before or after the work.** A04.03-K22 (agent AUROC the same asked before as after) against A04.03-K21 (after real reasoning is much better). A04.08-K01 uses a before-solve FOK and an after-solve JOL. | Different tasks. K22 is coding agents; K21 is short reasoning. Compare both slots in A04.03-U10 and A04.08-U4. |
| C3 | **Is the harness gain real?** Single-source A04.08-K01 (+8.6) against contested A04.08-K02 (no equal-compute arm), contested A04.08-K04 (directed retry 47.0 vs random 45.7, N=100), and A04.08-K24 (+3 to 4 for allocation, not retry). | Plan on +1.5 to +4. Decide with A04.08-U1 to U3. Do not add S0/S6/S7 as one loop before that. |
| C4 | **Compact record against full trace for retry.** Contested A04.08-K06 (47.0 vs 40.0) against full-context sequential winning in other work. | Decide with A04.08-U6. Until then no rule. |
| C5 | **Self-correction.** Established A04.03-K14 and A04.08-K10 (hurts, 2023 models) against contested A04.08-K23 (reasoning models do correct errors in context; "Wait" cuts the blind spot 89.3%). | Scope G1 and G2 to checked revision. Test on our model (A04.08-U7, A04.03-U5). |
| C6 | **Does thinking mode calibrate?** Contested A04.03-K11 (thinking beats non-thinking) and established A04.03-K12 (reasoning models track better, r = .94 vs .48) against single-source A04.03-K26 (small hard-easy slope) and established A04.08-K26 (open reasoning models fail the ECE bar). | Not resolved. Reasoning models may rank well and still be badly calibrated. Report AUROC and ECE separately. |
| C7 | **Agreement as the signal.** A04.03-K08 and A04.08-K13 favour it. A04.03-K20 shows a floor of confident-wrong items. Single-source A04.08-K07 says confidence works across problems but not within a problem. | Agreement picks where to spend, not what to submit. Pair with an outside check (A04.03-U3). |
| C8 | **Cross-field: stated confidence.** A01 C6, A12 C8, C01 and E08 C10 treat stated confidence as barred. A04.03-K08 and K21 show agreement and post-reasoning confidence do carry signal, which fits A01 C6 (agreement is a candidate after tests). A12.04-K13 (self-reports poor mid-task) agrees with A04.03-K22. | Consistent. A04 supplies the test design (A04.03-U2, A04.08-U5). |
| C9 | **Cross-field: debate.** Single-source A04.08-K11 agrees with SCHEMA G9. E08 C5 has a contested pro-debate claim with no same-token control. | Keep G9. |
| C10 | **Cross-field: self-correction.** E10 C3 and A04.08-K23 both say the answer depends on checkability. C09.01-K15 says unaided correction flips right to wrong. | Consistent. Gains need a check or a located error. |

## 4. Recurring mechanisms

| Mechanism | Where | What it means for the agent |
|---|---|---|
| **Cue-based confidence fails when cues and truth split** | A04.03-K01, K06, K13; A04.08-K03 | Do not read fluency or a stated number as correctness. Build the signal in code from counts. |
| **More computation makes the signal better** | A04.03-K08, K21, K24 (untested); A04.08-K09 | Agreement of samples, post-reasoning scores and blind re-solves all beat a quick number. Each costs tokens, so compare at equal tokens. |
| **The consistent-wrong floor** | A04.03-K05, K20; A04.08-K07 | Every self-derived signal fails on the same items. Only an outside check or a different-method re-solve reaches them. |
| **Signals are per model and per class** | A04.03-K16, K17, K25; A04.08-K08, K17, K26 | Audit the signal on a small labelled anchor set per class before using it as a gate. Keep a code fallback. |
| **Gate spending, do not spend uniformly** | A04.03-K15; A04.08-K13, K14, K16, K24 | Stop early on agreement. Route by difficulty. Probe cost must be counted. |
| **Self-bias in self-judgment** | A04.03-K14; A04.08-K10, K12 | The model that wrote an answer overrates it. Use code, outside feedback or a blind fresh instance. |
| **Tests at small N look like results** | A04.08-K02, K04, K21 | Gaps of 1 to 5 points on N=100 are noise. Use 200 to 500 items, 3 seeds, paired bootstrap. |

## 5. Merged tests

All arms at equal total tokens, with probe, aggregator and setup tokens counted. Plan on gains of +1.5 to +4 points.

| Merged test | Unknown ids covered | One-line design | Priority |
|---|---|---|---|
| T1 Signal audit and choice | A04.03-U2, A04.03-U7, A04.03-U8, A04.03-U14, A04.08-U4, A04.08-U5 | On 300+ labelled items per class, log stated score (before and after reasoning, thinking on and off), top-3 elicitation, 2-sample and 4-sample agreement; report AUROC with a lower bound and ECE, under 3 graders and 2 answer-string variants. | High |
| T2 Blind re-solve against answer-visible check | A04.03-U1, A04.03-U11 | Answer-visible "is it right?" vs fresh blind re-solve with code comparison vs fresh adversarial reviewer; AUROC and net flips. | High |
| T3 Catching consistent-and-wrong items | A04.03-U3 | Harvest items wrong at agreement 0.8 or higher from T1; add an outside check or a different-method re-solve; share caught and false alarms. | High |
| T4 Gated retry headline | A04.08-U1, A04.08-U2, A04.08-U3, A04.08-U8, A04.03-U4, A04.03-U5 | Pass@1 vs best-of-K plus vote vs gated loop vs random retry, with a stop-gate x retry x selector factorial and a fresh re-ask placebo in the low band; verify-gate variants against always-verify. | High |
| T5 Self-review on a 2026 reasoning model | A04.08-U7, A04.08-U11 | Huang protocol: "review and revise" with no feedback vs second independent sample vs tool-checked revision vs gated "Wait" pass; right-to-wrong and wrong-to-right counts. | High |
| T6 Router and early stop | A04.08-U9, A04.03-U13, A04.08-U10 | Fixed strategy vs route by first-pass band vs unanimity stop of first 3; plus break-even budget of a code controller at 3 budgets. | Med |
| T7 Retry context | A04.08-U6 | On first-attempt failures: compact record vs full trace vs none, same tokens. | Med |
| T8 Per-class recalibration and drift | A04.03-U6, A04.03-U9, A04.03-U10 | Count-table maps from n = 25 to 200 runs per class, held-out and shifted-class ECE; per-step confidence AUROC across checkpoints; hard-easy slope by bin. | Med |
| T9 Self-written checks | A04.08-U12 | Self-written vs given tests as the retry gate; false-negative rate. | Med |
| T10 Low-priority probes | A04.03-U12, A04.08-U13, A04.08-U14, A04.08-U15 | Fluency-trap pairs; forced-index model aggregator with authorship swapped; written reason with each JOL; skill-matched examples. | Low |

Run order: T1 first (precondition, and its logs seed T3), then T2 and T4 on the same logs, then T5.

## 6. Not to add

| Idea | Why not | Claim ids |
|---|---|---|
| Raw verbalised confidence as a sole stop or verdict | AUROC 0.5 to 0.65 for plain prompts; already in SCHEMA 4b | A04.03-K07, A04.03-K22, A04.08-K26 |
| A low ECE as proof of a good signal | 100% on everything scores well when accuracy is high | A04.03-K07 |
| Prompted self-correction with no outside feedback | Hurts on 2023-era models; reasoning-model evidence is contested, so keep 4b until A04.08-U7 | A04.03-K14, A04.08-K10 |
| Agreement as a verdict | Consistent-wrong floor of 5.5% to 28% | A04.03-K20 |
| Model scoring its own output | Self-bias grows over rounds | A04.08-K12 |
| Forced "Wait" budget forcing without a gate | Diminishing returns past about 6x | A04.08-K20 |
| Debate | Does not beat self-consistency at matched responses; already G9 | A04.08-K11 (single-source) |
| A single global calibration map | Per-slice beats global in every setting tested | A04.03-K25 |
| Finetuned confidence heads | Outside the no-training rule | A04.03-K10 |
| Human-only findings (Dunning-Kruger shape, feeling-of-rightness timing, hard-easy as a rule) | About people; the model has no felt sense | A04.03-K03, A04.03-K04 |
| The +8.6 harness headline as a plan number | Single-source, no equal-compute arm | A04.08-K01, A04.08-K02 |
| Metacognitive prompting scripts | Modest single-source gains, no gate, no token comparison | A04.08-K19 |

## 7. Gaps

- Seven of nine subfields are not researched (section 1). Regulation, meta-reasoning and signal-detection measures are rated High for our agent in SUBFIELDS.md.
- Almost no current-model data. Evidence is mostly GPT-3.5/4, open 32B and 1.5B to 30B models. Claude data rests on one paper (Cao, N=100 anchor, no code released, no replication).
- No equal-token test of a gated loop against best-of-K plus vote on a 2026 frontier model (A04.08-K29, untested).
- Blind re-solve (A04.03-K24) and cheap triggers such as token-confidence dips (A04.03-K23) are untested on LLMs, and the latter needs logprobs. Confirm which of our models expose them.
- Long-horizon agent control by confidence has no published test with irreversible steps.
- Whether metacognitive skills form one faculty is open (monitoring and answering skill do not rank together; A04.08-K17).
- Several sources were seen as abstract or snippet only (the 33-model atlas, Koriat 1997, the meta-analysis tables). Do not quote their numbers as verified.
