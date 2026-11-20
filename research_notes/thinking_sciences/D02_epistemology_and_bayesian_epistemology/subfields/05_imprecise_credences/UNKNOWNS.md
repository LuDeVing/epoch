# Imprecise credences: what we don't know and should test
*Candidates for the schema that are not established. Nothing here goes into SCHEMA.md until its test passes. Source: DEEP.md, claims.jsonl, critique.md in this folder.*

## Test before adding
| ID | What we don't know | If it works, we add | Schema part | Evidence so far | Test (arms at equal tokens; items; metric) | Add if | Priority |
|---|---|---|---|---|---|---|---|
| D02.05-U1 | Does a low/high "unknown" flag beat a point confidence for final accuracy? | Interval field on claims; route extra tokens by width | S0 / memory | K17, K21; d09: AUROC tie with Vanilla (single-source) | A: point confidence. B: [low,high] with containment, flag used to re-sample or abstain. 300 held-out QA items. Accuracy at equal tokens | B beats A by 2 points or more, 95% CI above 0 | High |
| D02.05-U2 | Does a containment rule (point inside [low,high]) matter? | Code check that repairs intervals excluding the point | G | K12; a19, d08: 72.33% containment, cost 0.03 AUROC (single-source) | Rule on vs off, U1 items. Containment rate, accuracy | Containment under 90% without the rule AND accuracy not worse than 1 point with it | High |
| D02.05-U3 | Does "list alternatives with probabilities, then low/high" improve calibration and accuracy? | O step: enumerate then interval | O | K09; c10: relative ECE -50% (single-source, older models) | With vs without enumeration, same token cap. ECE, AUROC, accuracy; 300 items | ECE down 25% relative or more AND accuracy not lower | High |
| D02.05-U4 | Does an interval from 5 samples beat one verbalized interval outside arithmetic? | Sample-then-interval operator, per problem class | O | K08; d09, d12 (contested): spread helps arithmetic, hurts QA | Spread vs verbalized interval, equal tokens; 150 arithmetic + 150 QA items; AUROC | Spread wins by 0.05 AUROC or more; add per class only | Med |
| D02.05-U5 | Which tie-break works when the interval straddles the decision threshold? | A fixed rule at S7 for straddling cases | S7 / O | K06, K20; d11 only maximin/maximax alignment, no accuracy test (contested) | Abstain, maximin, ask, E-admissible then maximin; 100 straddling items with checkable answers; accuracy and cost | One rule beats the rest by 3 points, or ties at fewer tokens | Med |
| D02.05-U6 | Does a stated interval widen on irrelevant evidence (dilation) in LLMs? | Dilation guard in code: freeze width on evidence tagged irrelevant | G | K04 theory (established); d16 no LLM test | Ask interval, add irrelevant fact, ask again; 100 items; widening rate | Widening in over 15% of items | Med |
| D02.05-U7 | Does an ambiguity pre-check (flag underspecified input, list readings or ask) raise accuracy? | S0 ambiguity check | S0 | K15; c15 (32% vs 90%), c08 (57% vs 50%); remedy untested | Direct answer vs check-then-ask; AmbigQA-like and own underspecified items; accuracy, extra tokens | Accuracy up 3 points at equal tokens, no loss on clear items | Med |
| D02.05-U8 | Does a commit-if-lower-beats-rival-upper rule beat majority vote at fixed coverage? | O commit or abstain rule on sampled intervals | O | K11; a21, d06 (contested, white-box, ties semantic entropy on open QA) | 5 samples; majority vs interval dominance; accuracy at 80% coverage | Dominance beats majority by 2 points at 80% coverage | Med |
| D02.05-U9 | Is a vacuous [0,1] flag ever useful, or should it be banned? | Guardrail: forbid [0,1], require weak prior | G | K05 theory only; no LLM test | Sequential-evidence task; start [0,1] vs [0.05,0.95] vs point; final error | Vacuous start gives 5 points higher final error | Low |
| D02.05-U10 | Does showing one claim at a time cut the confidence penalty on vague claims (comparative ignorance)? | S0 rule: judge vague claims alone | S0 | K19; d01 vs failed copy d02 (human-only, contested) | Same claim alone vs beside a precise rival; stated confidence; 60 claims | Confidence gap shrinks by half when alone | Low |
| D02.05-U11 | Do hedging words match the sample split in our agent? | Faithfulness check as a guardrail test | G | K10; c12: 0.52-0.57 (established, older models) | Verbal hedge vs sample agreement; agreement score | Score above 0.8 lets hedges serve as a signal; otherwise keep G10 as is | Low |
| D02.05-U12 | Does LLM ambiguity aversion (Ellsberg item) predict answer quality? | A cheap behaviour screen, or drop the topic | none | K13; b12, b14 (contested, small open models) | Two-urn item per model vs bench accuracy | Correlation above 0.3 across models | Low |

## Open questions we cannot test on our bench yet
- Independent replication of credal-set gains: needs white-box ensembles of open models that we do not run.
- Founding texts (Keynes, Levi, Walley, Ellsberg 1961, Fox and Tversky QJE): not opened; need library access.
- Credal LLM tables (a20, a22, a24, a26, a27) were unreadable; need better PDF table extraction.
- Verbalized intervals on non-OpenAI and non-Google families: Claude and Gemini cells in Bini (b14) did not parse.
- Per-model containment rates: only a pooled 72.33% exists (d08).

## Order to run
1. **U1 (interval flag vs point confidence):** the only test that says whether this subfield matters for the agent; one prompt change.
2. **U2 (containment rule):** nearly free, and U1 depends on intervals being coherent.
3. **U3 (alternatives first, then interval):** cheap; a single-source calibration win (about 50% ECE cut) to confirm on current models.
