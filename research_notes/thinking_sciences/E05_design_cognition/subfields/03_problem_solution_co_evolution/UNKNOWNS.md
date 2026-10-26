# Problem-solution co-evolution: what we don't know and should test
*Candidates for the schema that are not established. Nothing here goes into SCHEMA.md until its test passes. Source: DEEP.md, claims.jsonl, critique.md in this folder.*

## Test before adding
| ID | What we don't know | If it works, we add | Schema part | Evidence so far | Test (arms at equal tokens; items; metric) | Add if | Priority |
|---|---|---|---|---|---|---|---|
| E05.03-U1 | Does rewriting the criteria after a failed solution beat framing once? | One criteria-rewrite step after a failed check, then retry | S3 to S2, O8 | K01, K26, K28; single-source, human-only and older models | (a) frame once + revise solution; (b) frame once + rewrite criteria on failed check; (c) resample. Checkable puzzle items with hidden constraints. Pass rate | (b) beats both (a) and (c) by 3+ points, CI excludes 0 | High |
| E05.03-U2 | Is the benefit limited to checkable tasks? | Gate the return by S0 mode (checked only) | S0, O8 | K16 contested; b18, b20 vs c02, b13 | Same arms on open design briefs scored by running plus blind judge. Novelty and correctness | Open-item gain within 1 point of checkable gain; else keep checked-only | High |
| E05.03-U3 | Which trigger works best for a reframe? | Trigger rule (failed check, stall, contradiction, hedging) | S6 | K28 single-source; K31 weak (pseudo R2 about 1%); web agents and novices only | Four trigger arms, same budget, same items. Repair rate | One trigger beats fixed-interval by 5+ points; hedging kept only if it adds 2+ over check alone | High |
| E05.03-U4 | How many reframe rounds before drift? | Cap at 1, 2 or 3 | G1, S5 | K24, K29, K30; older models, other tasks | Rounds 0, 1, 2, 3 at equal tokens; accuracy and broken-pass rate | Gain flat or falling after round N; set cap to N | High |
| E05.03-U5 | Does restate-then-solve (RaR) win at equal tokens on our models? | Rewording call in S1 | S1 | K14 single-source; weak models lose | Solve; RaR; best-of-2; ambiguous items; strong and weak model | RaR beats best-of-2 by 3+ points, no loss on weak model | Med |
| E05.03-U6 | Does a step-back call win at equal tokens? | Principle-first call for science items | S2, O2 | K15 established on PaLM-2L (2024) | Step-back vs best-of-2 on science QA and brainteasers; count new errors | Net gain 2+ points and new errors under 5% of items | Med |
| E05.03-U7 | Do up to 3 clarifying questions help under-specified items? | Clarify step, cap 3 | S1 | K19 established for code; K34 fragile (-4.2 to +6.3 pp) | Solve vs clarify (simulated answerer) vs best-of-N; under-specified logic and planning items | Gain 3+ points on two item types, no loss on closed items | Med |
| E05.03-U8 | Does order (problem-first, solution-first, interleaved) matter? | A fixed order for open mode | S2, S3 | K07, K08, K32 contested; N=9 human data | Three orders on open and checkable items; novelty and correctness | One order beats the others by 3+ points on both scores | Med |
| E05.03-U9 | Does a stall-triggered monitor help at equal tokens? | Monitor call at S6 | S6 | K20 single-source: 141.17 vs 72.07 Ah, one task, one model, monitor tokens unmeasured | Monitor vs plain loop vs same-token resample on 3+ task types | Beats resample by 3+ points on 2 of 3 task types | Med |
| E05.03-U10 | Should self-framing be gated by model tier? | S0 rule: weak model gets a stronger framer or none | S0, S2 | K35; d05, older models | Self-frame, stronger-model frame, no frame on weak and strong models | Weak model loses 2+ points from self-frame and gains from stronger frame | Med |
| E05.03-U11 | Does a missing-information check help on logic and planning? | One "is a fact missing?" call at S6 | S6 | K18 single-source (QuestBench 40-50%) | Check vs none vs resample on QuestBench-like items | Gain 5+ points on logic and planning items | Low |
| E05.03-U12 | Does a premise check reduce fixation on a wrong stated premise? | Premise-check step in S1 | S1 | K17 (6 of 6 detected; no accuracy result) | Seeded wrong-premise items with and without check | Detection above 80% and accuracy up 3+ points | Low |
| E05.03-U13 | Does transition count in traces predict quality? | Trace signal in the run log or S6 | Run log | K23, K25; untested by Zhang | Code content transitions on T1 and T8 traces; correlate with score | Correlation above 0.3 after controlling for length | Low |
| E05.03-U14 | Does a bridge log (criteria version, candidate, check result) help selection? | Bridge-based pick at S7 | S7 | K01; human-only | Select by bridge candidate vs by vote on the same attempts | Bridge pick beats vote by 3+ points | Low |

## Open questions we cannot test on our bench yet
- Real Dorst and Cross 2001 and Kruger and Cross 2006 numbers: full texts are closed. Needs library access or the authors' data.
- Expert-rated quality of open design frames: needs paid expert judges. Our bench has run-based scoring only.
- Token cost of the monitor agent in Xu et al.: needs their code or a rerun.
- Human baselines for the order dispute: needs human participants.
- Frontier-model behaviour: the LLM studies here use older models or one model each.

## Order to run
1. E05.03-U1 together with U2: criteria rewrite after a failed check vs frame once vs resample, on checkable then open items. It is the central, untested claim and sets the rest.
2. E05.03-U4: reframe round cap 0 to 3. Cheap, reuses U1 runs, and fixes the loop bound.
3. E05.03-U3: trigger type (failed check vs stall vs hedging). Cheap, reuses U1 arms, and decides what fires the return.
