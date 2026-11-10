# Complexity of expert troubleshooting: what we don't know and should test
*Candidates for the schema that are not established. Nothing here goes into SCHEMA.md until its test passes. Source: DEEP.md, claims.jsonl, critique.md in this folder.*

## Test before adding
| ID | What we don't know | If it works, we add | Schema part | Evidence so far | Test (arms at equal tokens; items; metric) | Add if | Priority |
|---|---|---|---|---|---|---|---|
| E08.08-U1 | Does labelling complexity type (representation, ambiguity, situational, stakeholder) at S0 and routing on it help? | Triage slot at S0 with per-type first operator | S0 / G1 | K01, K28; human-only, single-source (a01, c01); no test (d16) | Triage-routed vs no triage vs random label; fault items incl. hard split; RCA accuracy and tokens | Beats no-triage by 3+ points and beats random label | High |
| E08.08-U2 | Does a no-fault gate cut over-diagnosis without hurting detection? | No-fault exit and gate | S0 / S9 | K17, K18, K28; single-source (c05, c06) | Gate vs none; mix of false-premise and real faults; false-alarm rate and detection rate | False alarms down 10+ points, detection down under 3 | High |
| E08.08-U3 | Does a normal-behaviour model step before hypotheses raise RCA? | Required normal-model slot | S0 / O6 | K03; human-only plus indirect agent evidence (a04, a10, d07) | Model-first vs none; SREGym/AIOpsLab-style items; localisation and RCA | +3 points RCA at equal tokens | High |
| E08.08-U4 | Does a forced second hypothesis plus a disconfirming test cut symptom-as-cause? | Hypothesis table with commit rule | O-challenge / G-anchor | K11, K12; single-source (b10, c25) | Table+challenge vs none vs k-vote; misleading-first-anomaly items; symptom-as-cause rate, accuracy | Symptom-as-cause down 20% relative and accuracy not below k-vote | High |
| E08.08-U5 | Does code-checked quote-before-interpret reduce hallucinated readings (prompt warnings did not)? | Grounding check | G10 | K14; single-source (c12, c13) | Enforced quote vs prompt warning vs none; tool-output items; hallucination rate, RCA | Hallucination down 20% relative with no accuracy loss | High |
| E08.08-U6 | Which role in a diagnostic panel carries the gain (tracker, challenger, ensemble)? | Keep only the winning role | O-roles / G9 | K25, K26; single-source, confounded with sampling (d02 to d04) | Single, k-vote, role panel, each role alone at equal cost; diagnosis cases | A role beats k-vote by 3+ points; else drop roles | Med |
| E08.08-U7 | Does a predict-then-observe step with code diff reduce wasted calls? | Prediction slot before each tool call | O-test | K04; single-source, student data (a15, a16) | Predict step vs none; multi-tool faults; wasted calls, accuracy | Wasted calls down 15% with equal accuracy | Med |
| E08.08-U8 | Does information-gain test choice beat arbitrary order? | Test-ranking step | O-select-test | K13; single-source (b15), relative vs absolute gain unclear | Rank by hypothesis split vs arbitrary; dialogue and tool items; turns and success | +5 points success or 20% fewer tests | Med |
| E08.08-U9 | Do retrieved solved faults and SOPs help on unseen fault families, not just repeated ones? | Retrieval at S0 with similarity gate | memory | K15; established on repeated families only (c18, d06, d07) | Retrieval vs none on repeated vs unseen split; accuracy | Gain on unseen at least 0 and no loss from fixation | High |
| E08.08-U10 | Is the 5-step plateau general, and what is the budget by difficulty? | Budget table by difficulty | G12 | K19; agent-specific (b06, c09) | Step caps 3, 5, 10, 20 on easy/medium/hard; accuracy vs tokens | Cap with under 2 points loss and 30%+ fewer tokens | Med |
| E08.08-U11 | Does a clarify-first step protect against vague tickets? | Early clarify slot | S0 / O-clarify | K17; single-source (c06, c07) | Clarify vs none on vague rewrites; outcome and over-diagnosis | Vague-ticket loss cut by half | Med |
| E08.08-U12 | Does a back-edge to system modelling beat a one-way pipeline? | Back-edge from any state to model | S-loop | K02; single-source, 2 think-alouds (a06) | Back-edge vs one-way; long troubleshooting items; accuracy, tokens | +3 points at equal tokens | Low |
| E08.08-U13 | Does a known-good reference trace help? | Reference at S0 | memory | K23; single-source (c22) | With vs without reference; trace/fault items; fault-type accuracy | +5 points top-1 | Low |
| E08.08-U14 | Does single-fault isolation help multi-fault items? | Isolate-first rule | O3 | K22; single-source (b11) | Isolate vs fix-all; 1 to 4 simultaneous faults; pass rate by count | Gain grows with fault count; +5 on 3+ faults | Low |
| E08.08-U15 | Is outcome-only scoring hiding luck, and how reliable are LLM judges here? | Evidence-checkpoint scoring in our bench | eval | K29; single-source (d09, d10); no human re-score | Human re-score of 100 traces vs judge vs checkpoint scoring | Judge-human kappa under 0.8 triggers checkpoint scoring | Med |

## Open questions we cannot test on our bench yet
- Non-IT fault domains (electronics, mechanical, medical devices): no benchmark with measured LLM results. Unblock by building a small simulated circuit or machine fault set with scripted measurements.
- Stakeholder complexity: single-item benchmarks have no stakeholders. Unblock by adding constraint-laden items (cost, safety limits) and scoring constraint violations.
- Schaafstal et al. numbers (N, times, solve rates) and replications: need the full paper; unblock by library access.
- Expert order of work in larger samples: the other Sabuncu think-aloud sessions are not public.
- Whether human complexity types predict human success: needs an outcome study; not ours to run.
- Human re-score of published agent benchmarks: not available.

## Order to run
1. E08.08-U2 (no-fault gate): cheapest, clear threshold, aimed at a measured failure (over-diagnosis 17% to 47%, 23% of spend on timeouts).
2. E08.08-U5 (enforced grounding) with U3 (normal model first): one-slot additions with code checks, aimed at the largest measured failure (hallucinated reading above 66%).
3. E08.08-U1 (complexity triage): the headline idea from the human literature; run with U4 as control so any gain is not just a second hypothesis.
