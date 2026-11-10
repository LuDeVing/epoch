# Formal argumentation frameworks (AI): what we don't know and should test

*Candidates for the schema that are not established. Nothing here goes into SCHEMA.md until its test passes. Source: DEEP.md, claims.jsonl, critique.md in this folder.*

## Test before adding

| ID | What we don't know | If it works, we add | Schema part | Evidence so far | Test (arms at equal tokens; items; metric) | Add if | Priority |
|---|---|---|---|---|---|---|---|
| D04.06-U1 | Does grounded survival on code-derived edges beat our current S7 rule and a vote? | Grounded survival as S7 step 1 | S7 | K28, d08 (trees, DF-QuAD, +2 pts MMLU-Pro, tie MedQA); single-source | Arms: vote, current S7, grounded, grounded+preferred fallback; 100+ ARC/BrainTeaser items, 4-8 candidates; accuracy, McNemar | Grounded beats current S7 by 2+ points, p<.05, and is not worse than vote | High |
| D04.06-U2 | How accurate are LLM attack edges between candidate answers? | An edge judge used only when its precision passes | S7, G5 | K18, K36, d15 (0.31-0.60 mining); human edges ~80% (d01); other tasks only | 50-100 hand-labelled candidate pairs; judge both orders; precision, recall, order agreement | Precision >=0.85 and order agreement >=0.8 | High |
| D04.06-U3 | How often are real candidate graphs cyclic or grounded-empty? | A cycle branch in S7, or proof it is moot | S7, S9 | K32, d17 (simulation only: cycles 25-56% at density 0.2) | Instrument all S7 runs; log cycle share and empty-grounded share | Keep a cycle rule if cycles >15% of runs; else drop CF2/preferred work | High |
| D04.06-U4 | On cyclic graphs, does CF2 or preferred beat the grounded fallback? | CF2 or preferred fallback | S7 | K03, K04, d02, d06; contested, human-only, one lab | Cyclic subset from U3; arms: grounded, sceptical preferred, CF2, size-then-shortness; accuracy | Beats fallback by 3+ points on 40+ cyclic items | Med |
| D04.06-U5 | Does a numeric score next to the survive flag help? | Score as tiebreak and confidence | S7 | K31, d03; single-source, human-only | U1 items; flag only vs flag+score; accuracy, Brier | Brier better by 0.02 or accuracy +1 point | Med |
| D04.06-U6 | Are LLM base scores better than uniform, and calibrated? | Estimated base scores in a gradual layer | S7 | K25, d09 (0.638 vs 0.618; GPQA 0.523 vs 0.419); calibration never measured; older models | Claim sets; uniform vs estimated vs CoT vs vote; accuracy, Brier, ECE | Estimated beats uniform by 2+ points with ECE <0.10 | Med |
| D04.06-U7 | Does an attack-and-defend verifier loop beat voting at equal tokens? | A bounded verifier-attack step before S7 | S5, S7 | K29, d13 (71.4 to 83.3, several times tokens, no vote baseline); G9 argues against | CoT, vote, ArgMed-style loop at the same total tokens; medical or hard reasoning; accuracy | Beats vote by 3+ points at equal tokens | Med |
| D04.06-U8 | Does attack-graph filtering of retrieved notes help? | Graph filter in memory retrieval | memory | K15, a14 (single group; gain shrinks for strong models) | Items with conflicting notes; concat vs filter vs none; accuracy | Beats concat by 2+ points on a weak model | Low |
| D04.06-U9 | Do undercut and preference layers (ASPIC+) cut errors over plain attacks? | Typed attack edges | S7 | K35, K02, d12 (21% invalid scheme fields); no measured benefit | Plain vs attack+undercut; accuracy and invalid-graph rate | Accuracy +2 points and invalid rate <5% | Low |
| D04.06-U10 | Can survival drop objectively failing candidates on open-ended tasks without cutting diversity? | Objective-test filter for creative items | S7, G8 | K34, d14 (debate cuts diversity; no attack-graph study) | NoveltyBench-like; no filter vs filter; diversity and quality | Quality up, diversity within 5% | Low |
| D04.06-U11 | Does candidate order change the survivor set when edges are judged by a model? | Two-order edge judging, agree-only edges | S7, G4 | K26, d11 (0.57-0.82 consistency for answer judges); not measured for edges | Same pairs in both orders; share of survivor sets that change | If survivor set changes in >10% of items, require agree-only edges | High |
| D04.06-U12 | Does an empty grounded set signal that all candidates are weak? | Empty-grounded as an impasse trigger | S6, G1 | K29, d13 (63% of empty cases had identifiable errors); single-source | Log empty-grounded; compare accuracy on empty vs non-empty; route to S6 | Accuracy on empty cases under half of the rest and S6 recovers 10%+ | Med |

## Open questions we cannot test on our bench yet

- Token-matched literature test of grounded survival vs voting: none exists; our T1 would be the first.
- Human match with larger AFs or non-student samples: needs a human study, which we do not have.
- Full text of Rahwan 2010, the 2024 reinstatement paper, Dung 1995, Prakken 2010: need access or a library copy.
- Calibration of LLM base scores: needs a gold-labelled claim set with confidences.
- LLM-built graphs on cyclic candidate sets from other labs: no public data; our own logging (U3) will supply it.
- Whether graded numeric semantics beat the Dung 3-state output on our bench: needs U5 and U6 first.

## Order to run

1. U3 (log cycle and empty-grounded rates): free, runs on existing S7 traces, and decides whether U4 matters at all.
2. U2 plus U11 (edge accuracy and order bias): the edge judge is the weak link in every design; if it fails, nothing downstream is worth testing.
3. U1 (grounded survival vs current S7 vs vote at equal tokens): the central question of this subfield; run only with code-derived edges unless U2 passes.
