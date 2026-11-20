# Research methods: what we don't know and should test
*Candidates for the schema that are not established. Nothing here goes into SCHEMA.md until its test passes. Source: DEEP.md, claims.jsonl, critique.md in this folder.*

## Test before adding
| ID | What we don't know | If it works, we add | Schema part | Evidence so far | Test (arms at equal tokens; items; metric) | Add if | Priority |
|---|---|---|---|---|---|---|---|
| A20.10-U1 | Does disagreement among attempts predict errors well enough to trigger verify? | Verify (S8) only on disagreement | O, G1 | K17; d08, d09, d10; contested, QA and Python only | never / always / on-disagreement verify; coding items with tests; pass rate | trigger within 2 points of always-verify at 60% or fewer tokens | High |
| A20.10-U2 | Does short narration change accuracy like human think-aloud (null) while explanation helps? | Cheap narrate or explain mode in S3 | G11, S3 | K01, K19; b12 human-only; d18 absent | silent / narrate / explain; reasoning items; accuracy | explain beats silent by 3 or more points with CI above 0 at equal tokens | High |
| A20.10-U3 | How often do coding-agent traces name the hint that drove an edit? | Rule: never use trace to decide; outside check only | G10 | K02, K19; c11 on QA; d16 snippets | inject leaked-test hint in SWE-style items; count hint mentions vs hint-driven edits | reveal rate below 50% confirms the guardrail; above 80% allows trace as a hint | High |
| A20.10-U4 | Do our own scaffold gains replicate on fresh seeds and items? | Replication gate in bench workflow | G7 | K08; TDD, METR; human-only | original vs fresh seeds and items; every claimed gain; effect size and sign | keep a gain only if it holds in sign and at least half its size | High |
| A20.10-U5 | Which config items (top-p, temperature, seeds, version) move pass rates most? | Mandatory run log and 5 repeats | G7 | K13; d11, d12; older models | vary each item, 5 repeats; coding set; spread of pass rate | any item shifts pass rate over 3 points: make it a logged field | Med |
| A20.10-U6 | Does a blind, length-normalised judge agree with tests better than a plain judge? | Blind judge in S7 when no test exists | G5, O | K16; d05 kappa 0.10-0.21; d03, d04; 2023-24 judges | judge sees authorship vs blind; patch pairs; kappa with tests | blind kappa higher by 0.10 or more | Med |
| A20.10-U7 | Do scaffold effects differ between new code and maintain-existing code? | Route by task type in S0 | S0, G12 | K04; b01, b04, b05, d06; contested | scaffold vs plain per stratum; pass rate | stratum effects differ in sign or by over 5 points | Med |
| A20.10-U8 | Does the agent's stated tool use match its call log? | Log-based check replaces self-report in S9 | G10 | K14; a21 human, N=14; single-source | stated vs logged tool use; agent runs; mismatch rate | mismatch over 20% | Med |
| A20.10-U9 | Does asking the agent to predict its own answer or confidence help as a signal? | Self-prediction hint in S0 | memory | K03; c01 finetuned only; d13 negative; contested | self vs other-model prediction; items with known answers; prediction accuracy | self beats other model by 5 or more points without finetuning | Low |
| A20.10-U10 | Are LLM labels safe for internal annotation steps (e.g. grading trace categories)? | Use model labels when model-model alpha is high | O | K09, K10; a12, c25; one lab | 3 models label trace items; alpha; vs a human subset | alpha 0.68 or more and human-model within 0.1 of human-human | Low |
| A20.10-U11 | Does self-preference bias hurt judging of the agent's own patches? | Rule: judge from another model or by tests | G5 | K16; d03, d05; small, model-specific, older models | own vs other-model patches, tests hidden; accept rate vs test outcome | own-patch accept gap over 5 points after length control | Low |
| A20.10-U12 | Do LLM-participant tests reproduce human TDD-style effects? | Nothing expected | memory | K19; none found; human-only | LLM agents as TDD vs test-last subjects; fresh tasks | sign of effect agrees with human replications | Low |

## Open questions we cannot test on our bench yet
- Full-text numbers for Fox 2011 (r = -0.03) and Nisbett and Wilson 1977. Need paper access.
- Why METR and Peng/Cui disagree. Needs human developers, not our bench.
- Mechanistic introspection (injected concepts). Needs activation access.
- Prompting-only Binder replication on frontier models. Needs held-out behaviour sets we do not have.
- Student vs professional gaps. No agent analogue except model strength tiers.

## Order to run
1. A20.10-U4 (replication gate): cheapest, protects every other result, uses existing data.
2. A20.10-U1 (disagreement trigger): highest expected token saving on coding items.
3. A20.10-U3 (hint injection on coding): tests whether G10 holds for coding agents; cheap to build.
