# Fault localisation and repair: what we don't know and should test
*Candidates for the schema that are not established. Nothing here goes into SCHEMA.md until its test passes. Source: DEEP.md, claims.jsonl, critique.md in this folder.*

## Test before adding
| ID | What we don't know | If it works, we add | Schema part | Evidence so far | Test (arms at equal tokens; items; metric) | Add if | Priority |
|---|---|---|---|---|---|---|---|
| E09.07-U1 | Does an Ochiai top-5 hint help a tool-using agent? | Code-built suspect hint in S5 prompt | O (tool), S5 | K21, d01, d02: single-source, students and Codeflaws, no equal-token test | Failing-output only vs + Ochiai hint; 80 bugs; Top-1 and correct rate | Hint arm +3 points Top-1 or correct, tokens within 5% | High |
| E09.07-U2 | Does a wrong or weak suspect list anchor the agent? | Input hygiene rule: hints shown only if source accuracy is known | S1, G1 | K02, K03: human-only, contested; no LLM study | Arms: accurate, rank 6-10, fault absent, none; 80 bugs; Top-1, tokens | Wrong-list arm loses more than 3 points vs none; then add gating | High |
| E09.07-U3 | Does agreement across reruns gate extra search? | Rerun-then-escalate rule in S3/S6 | G1, G5 | K09, c03 (rho 0.5, GPT-3.5, Java); d11 warns on calibration | Always 1 run vs always 5 vs gate at agreement under 3 of 5; 60 bugs; Top-1 per token | Gate within 2 points of 5-run at 60% or less of tokens | High |
| E09.07-U4 | Re-localise after N failed patches vs sample more | Re-localise trigger in S6 | S6, G12 | K25, d12, d16: single-source, not token-matched | N more samples vs re-localise then N/2 samples; 60 bugs failing 3 patches; solved fraction | Re-localise arm +5 points | High |
| E09.07-U5 | Does a round cap near 25 plus repeat detector help? | Hard cap plus repeat-action trigger | S6, G11 | K23, K17, d08, d16: agent traces, few agent families | Cap 25 + repeat detector vs no cap; 60 bugs; resolve rate, tokens | Same or better resolve at 20% fewer tokens | High |
| E09.07-U6 | Is a stop-on-confirmed-cause rule useful? | Verify-once then stop in S8 | S8, G7 | K04, b05: humans only, N=10 | Verify-once-then-stop vs free; 60 bugs; tokens after first correct fix, final correct | Tokens down 25%, correct rate not down more than 1 point | Med |
| E09.07-U7 | Does coupled-file enumeration fix multi-file faults? | Call-site and coupled-file step after first fix | S5, S8 | K24, d14: 25.3% multi-file; no scaffold shown to help | With vs without; 40 multi-file bugs; multi-file resolve rate | +5 points | Med |
| E09.07-U8 | Does a self-generated reproduction test add value? | Repro-test step in S4 | S4, G3 | K12, c27: 94 of 213 valid | With repro test + filter vs without; 60 issues; resolve and false-pass rate | +3 points resolve, false-pass under 10% | Med |
| E09.07-U9 | Is a cheap file scan then symbol checks better than agent search? | File-scan step in S0/S1 | S1, G12 | K26, d13: single paper, SWE-bench | Scan + symbol vs agent search; 60 bugs; Top-1 symbol per token | Equal accuracy at 30% fewer tokens | Med |
| E09.07-U10 | Does a real-execution hypothesis loop beat plain reasoning? | Hypothesis-run operator | O (hypothesis test) | K18, d09, d10: contested; accuracy equal at 10 samples; explanations unreliable | Hypothesis loop with real run vs plain CoT; 50 bugs; correct rate at equal tokens | +3 points correct | Med |
| E09.07-U11 | Is localisation memorised for frontier models? | Mandatory contamination arm in all bench reports | G11 | K22, d03, d04: repair side only; b28 on SWE-bench | Original vs renamed identifiers, localisation only; 60 Defects4J bugs plus post-cutoff set; Top-1 drop | Drop over 5 points; then report only renamed or post-cutoff numbers | High |
| E09.07-U12 | Does a stronger blind critic improve repair feedback? | Separate critic call, shown no authorship | G5, S5 | K13, a28, a29: human feedback 52.60 vs 33.30; no model-critic equal-token test | Self-feedback vs stronger critic; 60 bugs; correct rate at equal tokens | +4 points | Low |
| E09.07-U13 | Does an issue-clarification step help noisy reports? | Clarify step in S1 | S1 | K15, b29, d06: Google 17.9% valid; solution-in-report 1.95x; single industrial study | Raw report vs clarified; 40 noisy bugs; resolve rate | +4 points | Low |

## Open questions we cannot test on our bench yet
- Human replication of Parnin and Orso vs Xia 2016: needs participants. Unblock: skip it and test the agent analogue (U2).
- Industrial-scale repos with real tracker reports: our bench has public and puzzle items. Unblock: a private repo set with real bug reports.
- Multi-location and missing-code faults: few labelled items. Unblock: build 40 from post-cutoff repos.
- Training-based localisers (LLMAO, UniXcoder): we do not train.
- Mutation-based localisation at agent scale: costly in test runs. Unblock: a fast test harness.
- Whether agents over-verify after a fault is found: needs trajectory labelling of "fault located" moments.

## Order to run
1. U1 plus U2 together (same bugs, four hint arms): cheapest, and answers both whether a hint helps and whether a bad one hurts.
2. U11 (contamination arm): decides whether every other number can be trusted.
3. U5 (round cap and repeat detector): cheap, code-only, targets the long-tail waste seen in agent traces.
