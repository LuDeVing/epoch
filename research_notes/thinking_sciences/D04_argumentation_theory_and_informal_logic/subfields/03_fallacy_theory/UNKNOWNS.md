# Fallacy theory: what we don't know and should test

*Candidates for the schema that are not established. Nothing here goes into SCHEMA.md until its test passes. Source: DEEP.md, claims.jsonl, critique.md in this folder.*

All tests: arms at equal total tokens (setup cost counted, G7), at least 3 seeds, 95% intervals, per-type split.

## Test before adding

| ID | What we don't know | If it works, we add | Schema part | Evidence so far | Test (arms at equal tokens; items; metric) | Add if | Priority |
|---|---|---|---|---|---|---|---|
| D04.03-U1 | Does moving authority, consensus and stated-guess cues into a marked S1 block (with a competence check) raise final accuracy vs leaving them inline? | Marked block with competence record as a fixed S1 step | S1 | K15, K28; d09, d10, b03. Single-source, older and 2026 API models; no direct test (GAPS 1) | Arms: cue inline / cue in block / cue stripped by code (ceiling). 300 existing reasoning items with injected wrong guess, fake expert, "most people say". Metric: final accuracy, drop from clean | Block beats inline by at least 3 points, CI excludes 0 | High |
| D04.03-U2 | Does the block hurt when the cue is sound (right expert, right answer)? | Competence check rule (record field and evidence, do not just down-weight) | S1 | K26, K21; d05-d08. Single-source; encoders and 3 LLMs | Same items with sound cues; arms as U1. Metric: accuracy, false-flag rate | Accuracy loss at most 1 point and false-flag rate under 10% | High |
| D04.03-U3 | Does asking the binary question ("is this flawed?") before naming any type cut false positives on sound look-alikes? | Binary-first wording in S1 check | S1 | K27; d07. Single-source, 3 models, zero-shot | Scheme Foils (authority, cause, analogy; 40 fallacious + 40 matched sound each). Arms: name-the-fallacy / binary then critical question. Metric: false-positive rate on sound, recall | False positives down at least 10 points, recall loss under 5 | High |
| D04.03-U4 | Does a forced-reason critical-question gate beat a plain verify step? | Critical-question gate in S8 | S8 / G | K24, K25; d01-d03. Single-source; half of gain from added structure; no token match; GPT-4 yes-bias 53.3% on true-no | Held-out reasoning set. Arms: plain verify / 8-question gate with a reason for each "no" / same-token self-consistency. Metric: accuracy | Gate beats both by at least 2 points, CI excludes 0 | High |
| D04.03-U5 | Does a pressure test show the block lowers flips under invalid arguments without raising stubbornness on valid ones? | Pressure-check rule and two-sided acceptance test for S1 | G / S1 | K14, K28; b03, d09. Single-source; LOGICOM never replicated | LOGICOM-style loop, 200 claims x 3 runs, fallacious vs logical counter-arguments. Arms: agent with / without block. Metric: invalid flip rate and valid flip rate | Invalid flips down at least 10 points and valid responsiveness within 5 points of baseline | High |
| D04.03-U6 | Does a dialogue-type tag (persuasion, inquiry, eristic) lower false positives on sound appeals? | Three-way type tag in S0/S1 | S1 | K02; a04, d07. Human theory only; no LLM test | Foils from U3. Arms: with / without tag. Metric: false-positive rate, recall | False positives down at least 5 points with recall held | Med |
| D04.03-U7 | Does a warm-up two-round check beat a single round and token-matched self-consistency? | Two-round staged check | S1 / staged check | K10; a17, b13, d17. Single-source (Pan et al.); no token counts | Fallacy items from MAFALDA-style data plus our cue items. Arms: 1 round / warm-up + 1 round / 2-sample vote at equal tokens. Metric: macro-F1; binary accuracy | Two-round beats the vote by at least 2 points | Med |
| D04.03-U8 | Does stripping source labels (human or AI written) before judging remove a verdict shift in the LLM? | Label stripping by code | S1 | K15; b16. Human study only (N=505) | Same fallacious comment labelled human / AI / none. Arms: visible / stripped. Metric: verdict shift, rated logic | Shift under visible labels at least 5% and gone when stripped | Med |
| D04.03-U9 | Does neutralising loaded wording help an LLM checker, and is the gain bigger than the rewrite cost? | Neutralise-then-check step | S1 | K17; a22, d13. Human annotators only (macro-F1 0.380-0.533 vs 0.563); no LLM data | Original vs neutralised rewrite of loaded arguments (LOGIC-derived, 200). Arms equal total tokens including rewrite. Metric: detection F1 | F1 up at least 3 points net of token cost | Low |
| D04.03-U10 | Does a self-audit pass catch fallacious steps in the agent's own reasoning? | Self-audit in S9, as a logged signal | S8 / S9 | K20; a26, d16. Talk2AI rate (14.5%) is not from reasoning chains; classifier over-flags | Collect 200 agent reasoning chains; two humans label fallacious steps. Arms: audit pass / none. Metric: step error rate caught, answer accuracy | Audit finds at least 50% of human-labelled steps with under 20% false flags and answer accuracy not lower | Low |
| D04.03-U11 | Does a premise-and-conclusion extraction step before cue judgement raise final accuracy (not only classification F1)? | Structure-first step in S1 | S1 / S2 | K12; b02, b14, c15. Established for classification; untested for answers | Items from U1. Arms: judge cue directly / extract premise and conclusion first. Metric: false-flag rate, final accuracy | At least 2 points better on either metric with no loss on the other | Med |
| D04.03-U12 | Do Bayesian source-reliability weights (confidence moves with source reliability) improve calibration? | Source reliability field in the block, used by code | S1 / S7 | K04; a10-a12. One lab, 2005 human data; originals not opened | Items with expert cue of varied reliability (reliable, unknown, unreliable). Arms: ignore / weight by code rule. Metric: calibration error, accuracy | Calibration error down at least 10% without accuracy loss | Low |

## Open questions we cannot test on our bench yet

- **Independent replication of LOGICOM (67% vs 37%).** Needs an outside group or a clean rerun with a logical-argument control. U5 is a partial check on our own agent only.
- **Hahn and Oaksford 2007 and Harris, Hsu and Madsen 2012 primary numbers.** Paywalled. Need the papers (library access) before U12 can be sized.
- **Walton's scheme books and critical-question lists.** Not opened. U3 and U4 use scheme questions written by us; we need Walton's own lists to test a true Walton checklist vs a generic one.
- **LoFa on 2026 models and the CoT effect on appeal to authority (-1.87%).** Needs the LoFa dataset and a rerun on current models. Could be done with U1 items as a proxy.
- **Model-human vs human-human agreement on the same items.** No dataset gives both. Needs us to label about 200 items with several annotators.
- **Real-world base rate of suggestive cues in our own inputs.** Needs a log from live runs.
- **Fallacies in the agent's own chains.** Needs human labelling capacity (U10).
- **Training-based gains (LFUD).** Outside the no-training scope; the idea cannot be tested without training.
- **Closed-model API results (2025-2026).** Cannot be reproduced exactly; treat as direction only.

## Order to run

1. **U1 with U2** (cheap, uses existing items): the one question S1 depends on, and no study answers it. The sound-cue arm guards against harm.
2. **U3** (Scheme Foils): measures the main known failure (over-flagging sound authority arguments) and tests a cheap prompt change (binary first).
3. **U5** (two-sided pressure test): shows whether the block lowers capitulation without making the agent stubborn, and also gives the first replication-like data for the LOGICOM effect.
