# Progress monitoring: what we don't know and should test

*Candidates for the schema that are not established. Nothing here goes into SCHEMA.md until its test passes. Source: DEEP.md, claims.jsonl, critique.md in this folder.*

## Test before adding

| ID | What we don't know | If it works, we add | Schema part | Evidence so far | Test (arms at equal tokens; items; metric) | Add if | Priority |
|---|---|---|---|---|---|---|---|
| A02.07-U1 | Does a code count rule (N repeats or M steps with no new output) beat a graded confidence trigger on our tasks? | Keep the cheaper rule; drop the other | S6 | K23, d20, d21, d14; contested; math and SWE only | Arms: none; count; graded confidence between attempts; both. 100+ tool/code items with a check; pass rate and false-stop rate | Best arm beats "none" by >=2 points with CI excluding 0; pick the cheaper arm if within 1 point of the best | High |
| A02.07-U2 | Is the S6 trip followed if only advised in the prompt, vs forced in code? Does forcing help on a strong Claude backbone? | Code-forced operator switch in S6 (disable tool, block repeated action) | S6, O | K20, d18, d19, d13; small open models plus Haiku 4.5; Sonnet 5 partly stops unaided | Arms: advice; forced switch. Items where the first operator fails; pass rate; share of trips with a changed approach | Forced beats advice by >=3 points, or advice changes approach in <70% of trips | High |
| A02.07-U3 | What repeat limit (2, 3, 5) minimises false stops and wasted steps? | A fixed limit in S6 | S6 | K21, K22, c10, d17; thresholds never ablated | Sweep limits 2, 3, 5 on the same items; pass rate, tokens, false-stop rate on items the plain run solves | A limit that holds false stops under 5% and keeps pass rate within 1 point of the best | High |
| A02.07-U4 | Which response after the trip is best: forced switch, switch plus compact failure summary, restart, stop and submit best? | One default response | S6, S5, memory | K29, d13, d19, d21, d28; no head-to-head; single-source | Four arms on items that trip S6; pass rate among tripped items | Winner beats the next arm by >=3 points on 100+ tripped items; else keep the simplest | High |
| A02.07-U5 | Does an answer-stability stop (same candidate in last k attempts) save tokens without losing accuracy on agent tasks? | Early stop in S3/S4 when the candidate is stable | S3, S4, S6 | K10, c11, c12, b22; math only; accuracy fell 1.5 to 5.2 in CoDE-Stop | Arms: fixed attempts; stop at k=2; stop at k=3. Single-answer items; accuracy and tokens | Tokens down >=20% with accuracy loss <=1 point | Med |
| A02.07-U6 | Does tiered escalation (action, then strategy, then judge) beat a single-tier switch? | Tiered escalation | S6 | K21, d17; single run per cell; helps weak backbones only | Arms: single-tier; three-tier. Items with loops; pass rate and wasted steps | Tiered beats single by >=2 points or cuts wasted steps >=30% | Low |
| A02.07-U7 | Does a guard against abandoning a promising line help (do not switch while the last check improved)? | Guard rule in S6 | S6, G11 | K27, K12, c07, d30; abstract-level for the fix; no human analogue | Arms: trigger only; trigger plus guard. Long-reasoning items; pass rate, number of switches | Guard gains >=2 points or cuts switches without loss | Med |
| A02.07-U8 | Does a very early jump to high certainty flag a likely error (premature confidence)? | Risk flag that forces an independent check | S6, G1 | K28, d27; abstract only; trained models | Log first-attempt certainty and step of first full answer; AUROC for final failure on 200 items | AUROC >=0.65 and beats attempt-count baseline | Med |
| A02.07-U9 | Can a within-solve closeness rating predict success? (Expected no.) | Nothing, unless AUROC is high | S6 | K24, c15, d22; SD 0.048; human warmth contested (K02, K03) | Log a 0-10 rating each step; AUROC at step k vs final pass vs repeat count | AUROC >=0.70 and above external signals; otherwise record as null in 4b | Low |
| A02.07-U10 | Does carrying a compact failure summary into retries beat none or the full failed trace? | Summary format in S5/S6 and memory | S5, S6, memory | K29, d21 (47.0 vs 40.0 vs 45.0; overlapping CIs), d28 | Arms: none; compact; full trace. 100+ retried items | Compact beats none by >=2 points and beats full trace | Med |
| A02.07-U11 | Does class pass rate (past) set a better budget and S6 threshold than the model's own estimate? | Prior-based threshold in S0 | S0, G12 | K08, a03; human, single-source, insight problems | Arms: uniform threshold; threshold by class pass rate. Mixed-difficulty set; accuracy at equal total tokens | Gain >=2 points or tokens down >=15% at equal accuracy | Low |
| A02.07-U12 | Is the monitor itself worth its cost (judge calls for "useless" results, forced answers)? | Cheap lexical detector instead of an LLM judge | S6, G7 | K20, d19 (lexical detector about as good); exploratory | Arms: LLM judge; lexical overlap detector; repeat count. Agreement on "no new information" labelled by code; tokens | Lexical or count within 5 points of judge agreement at <20% of the cost | Med |

## Open questions we cannot test on our bench yet

- **Anagram solvability judgments and the CSPT numbers.** We have not read MacGregor et al. 2001, Ormerod et al. 2002 (full text) or Novick and Sherman 2003. Unblock: get full texts via library access, then extract the tables. Until then do not build anything from the anagram or nine-dot numbers.
- **Human warmth and the Hedne dispute.** Needs a human study (40 vs 5 ratings, 100% confidence rule). Not a bench task. Unblock: only if someone runs it; our agent does not depend on it.
- **Hidden-state probes and attention-state stops.** Need open-weight models and per-domain calibration data. Unblock: run an open model on the bench and train probes on our own traces; skip if the agent stays on a closed API.
- **False-trigger rate on long non-coding traces.** We have no labelled benign traces from open-ended tasks. Unblock: log a few hundred full runs with outcome labels, then replay the rules offline.
- **Human analogue of underthinking.** None found; humans overharvest. Unblock: a foraging or patch-leaving study that includes premature leaving, or accept that thresholds come only from our own data.
- **Warmth ratings elicited from an LLM mid-solve.** No study exists. Could be done on the bench (U9), but a null would not tell us about humans.
- **Newer, larger Claude models and unaided stopping.** Only Sonnet 5 was reported as partly stopping on evidence without prompting. Unblock: repeat U2 on each backbone before each schema freeze.

## Order to run

1. **U3 (threshold sweep) first.** It is the cheapest, uses existing traces offline, and its false-stop numbers set the base for every other test.
2. **U2 (advice vs forced response).** The strongest literature result (replicated pre-registered) but only on small models; confirm it on our backbone before wiring S6 around it.
3. **U1 (count rule vs graded trigger).** The decision-relevant gap: no head-to-head exists, and it decides whether S6 needs any confidence signal at all. Run U4 (response comparison) on the same tripped items to save tokens.
