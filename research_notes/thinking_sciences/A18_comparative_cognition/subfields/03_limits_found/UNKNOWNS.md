# Limits found: what we don't know and should test
*Candidates for the schema that are not established. Nothing here goes into SCHEMA.md until its test passes. Source: DEEP.md, claims.jsonl, critique.md in this folder.*

## Test before adding

| ID | What we don't know | If it works, we add | Schema part | Evidence so far | Test (arms at equal tokens; items; metric) | Add if | Priority |
|---|---|---|---|---|---|---|---|
| A18.03-U1 | Does a scaffold gain survive an audited counterfactual twin, or does it vanish like the crows' two-hole rule? | Twin gate as a required step before any scaffold element is kept | G3, G7 | K22 provisional; d07, d08 (GPT-3.5, unequal tokens, old models); no equal-token test | Plain vs scaffold; 40+ ARC/BRAINTEASER items, each with a two-checker audited twin; 5 seeds; seed score, twin score, gap, macro accuracy | Twin gain >= 60% of seed gain and gap not larger than plain arm gap + 3 points | High |
| A18.03-U2 | How much of a twin drop is a lost rule vs a changed question? | Mandatory audit plus comprehension probe in every twin test | G3 | K21 contested; d03 (blog, kappa 0.32), d05 (60% kept meaning) | Build 100 candidate twins; two auditors; keep agreed ones; measure drop on all vs audited; add restate-rule probe | Audited drop differs from raw drop by > 5 points in at least one task type | High |
| A18.03-U3 | Does forced recheck after the first answer fix errors in strong models? | One recheck turn at S4 on a signal | S4 | K25 provisional; d12 (non-reasoning, injected errors), d11 | Single pass vs pass + recheck turn; 60 items with natural and injected errors; fix rate and break rate (correct answers changed to wrong) | Fix rate - break rate >= +3 points, and no more than 10% extra tokens beyond the equal cap | High |
| A18.03-U4 | Can code count adoption of a planted wrong claim as a shallow-rule signature, and does the scaffold cut it? | Signature counter logged each run; execution step made mandatory on code items | G3, S4 | K24 provisional; d13 (accuracy drop only), d02 | Plain vs scaffold with execute-and-compare; 60 code items with planted wrong comments; share of answers equal to the planted claim vs other wrong answers | Plain adopts >= 10% and scaffold adopts <= half of that | High |
| A18.03-U5 | Does running a test before answering beat answering first on conjunctive rules? | Test-first as an S4 default for rule-inference items | S4 | K26 open; d14 (active arm only), c17, c18 | Answer-first vs test-first with code-counted test budget, same cap; 40 conjunctive and 40 disjunctive items; exact rule and object accuracy | Test-first >= +8 points on conjunctive items and not worse on disjunctive | Med |
| A18.03-U6 | Do retry loops learn only from success, as corvids do? | S8/memory rule: when a failure repeats, force a changed strategy with the failure reason | S8, memory | K28 open; d20 (OR 5.00 vs 0.67), d22; no LLM data | Log-only vs log + show failed attempt with reason; fit odds of repeating the correct strategy by previous outcome; 100+ retry sequences | OR after failure < 1.5 in log-only arm, and the reason arm lifts next-attempt success by >= 5 points | Med |
| A18.03-U7 | Does a second-format rerun change how often we record a "limit"? | Format ladder as a gate before any limit is written to the schema | G3 | K03, K11 established in animals; d21 for LLM interface; no measured LLM rate | Take 20 failed probes; rerun each in 3 formats (wording, budget, tool); count limits that disappear | >= 25% of limits vanish in some format | Med |
| A18.03-U8 | Does an interface change (tool API vs free text) lift causal or physical items? | Default tool/simulator route for physical and causal items | G3, G12 | K10 established for VLMs; K27 open; a18, d21 | Free text vs tool API vs code simulator; 40 physical/causal items; accuracy | Tool arm >= +10 points | Med |
| A18.03-U9 | Does a step-wise feasibility check cut wrong-tool errors in strong models? | Per-step feasibility check in tool-use items | S4 | K16 single-source; c25 (helped GPT-4, not Llama 2) | One-pass vs per-step check; 50 unconventional tool-use items; wrong-tool error share | Wrong-tool share down by >= 20% relative | Low |
| A18.03-U10 | Do reasoning models avoid output-limit collapse if asked for a generating program? | Program-first output for long enumerations | G12 | K13 contested; b23, b24 (preliminary) | Enumerate vs program, 30 large-N items, same cap; accuracy | Program arm >= +15 points at large N | Low |
| A18.03-U11 | Do memory lessons from class A help or hurt near class B? | Keep lesson store only with a near-class check; else restrict to same class | memory, S9 | K09 single-source (training only); c09, c10 | No lesson vs lesson from class A; 30 near-class items; pass rate on B | Lesson arm >= +3 points, no loss on B | Med |
| A18.03-U12 | Is chain validity (not just answer) a better predictor of twin success than answer accuracy? | Chain-validity check at S8 | G10, S8 | K12 established (TRIP 78.3% vs 11%); no twin link | Score chain validity and answer on seeds; correlate with twin pass over 100 items | Chain validity predicts twin pass with AUC >= 0.10 above answer-only | Low |

## Open questions we cannot test on our bench yet

- **Two-hole replication outside the founding lab.** No Gray, Jelbert, Seed or Bird follow-up found. Needs animal work or a fresh literature sweep once search quota returns.
- **2025-2026 reasoning models on altered-alphabet and counterfactual twins.** Only GPT-3/4 numbers exist in the sources. Unblock by running our own twins (U1) on current models.
- **Exact Mecattaf per-level LLM accuracies.** Only in figures. Unblock by the authors' data or a rebuild with a tool API (U8).
- **Natural (not injected) errors in retry loops.** Tsui and Laban use injected errors or simulated chats. Unblock by logging real runs on our bench.
- **Kea vs crow breeze gap.** Capacity or task design is unknown. Animal work needed; useful to us only as a caution.
- **Rate of hint adoption vs other wrong answers.** Not reported anywhere; U4 produces it.
- **Whether abstract-only primate and rook sources hold.** Many were not opened. Needs full-text read before we cite numbers.

## Order to run

1. **U1 (scaffold on audited twins).** It tests the core claim of the subfield on our own scaffold, and every other result depends on a trustworthy twin set.
2. **U2 (audit of twins).** Cheap, builds the twin set U1 needs, and tells us how much of any reported drop is real.
3. **U3 (recheck turn).** Cheapest schema change with the largest published effect (-89.3% blind spot), so a fast yes/no is worth the most.
