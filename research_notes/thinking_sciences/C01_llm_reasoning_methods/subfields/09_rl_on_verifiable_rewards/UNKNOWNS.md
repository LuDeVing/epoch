# RL on verifiable rewards: what we don't know and should test

*Candidates for the schema that are not established. Nothing here goes into SCHEMA.md until its test passes. Source: DEEP.md, claims.jsonl, critique.md in this folder.*

## Test before adding

| ID | What we don't know | If it works, we add | Schema part | Evidence so far | Test (arms at equal tokens; items; metric) | Add if | Priority |
|---|---|---|---|---|---|---|---|
| C01.09-U1 | Do prompt-only verify, backtrack and subgoal operators beat plain CoT? | Code-fired verify and backtrack operators with a named prompt | S5, S8, O3, O5 | K10 established for trained models; b18-b20, d02; prompt form single-source | Plain CoT vs operators vs length-matched filler; fresh math and Countdown items; accuracy, 30+ seeds | Operators beat plain by 3+ points and filler ties plain, p<0.05 | High |
| C01.09-U2 | Does firing on a signal beat firing on a schedule? | A signal rule for when to doubt (backs G1) | G1, S6 | K20 d02 single-source; own data 92% vs 75% | Signal-fired vs every-k-tokens vs never; same items; accuracy and token share | Signal-fired beats schedule by 2+ points at equal or fewer tokens | High |
| C01.09-U3 | How much of any scaffold gain is just output format? | Strict output contract as a separate, cheap element | Output contract before S3 | K12, K23 (a21, d03); trained models only | Loose prompt vs strict-format prompt vs scaffold; strict and lenient parsing; code and math items | Format prompt closes 30%+ of the gap: keep it, report scaffold gain net of it | High |
| C01.09-U4 | Does the scaffold beat low temperature and a plain vote? | Mandatory baselines in every bench run | G7 | K19 d01 single-source: base 49.6, low-T 69.0 | Scaffold vs T=0.3 single sample vs 8-sample vote at equal tokens; fresh items | Baselines always on; an element stays only if it beats both by 2+ points | High |
| C01.09-U5 | Does the scaffold narrow pass@k at large k like RLVR? | A diversity rule in the sample step | G12, S3 | K06, K26 contested; no scaffold curve exists | pass@k for k=1..64, scaffold vs plain; items lost vs gained at k=64 | Scaffold loses more items than it gains at k=64: add forced diversity or a plain-sample slice | Med |
| C01.09-U6 | Does an instance-specific checklist written first beat a generic one? | Checklist-first, check-draft step for open tasks | S1, S8, memory | K24 d11 single-source; trained judge reward only | No checklist vs generic vs instance-specific; open-ended items; blinded length-normalised score | Instance-specific beats generic by 3+ and beats none by 3+ | Med |
| C01.09-U7 | Does reflect-then-retry with the failing output quoted beat plain retry? | Reflection must quote real output, as an operator | S5, G2 | K18 c24 single-source; K22 d17 says reflection without a check hurts | Plain retry vs reflect-with-quote vs reflect-without-quote; code and puzzles with executable checks | Reflect-with-quote beats plain retry by 2+ points; reflect-without-quote does not | Med |
| C01.09-U8 | Does a code-style step format help non-coding math items? | Code-like step format as a representation choice | O6 | K08 a20, b10 single-source; Qwen only, contamination suspected | Plain CoT vs code-style steps (no execution) vs with execution; fresh math items | Gain of 3+ points on 2 or more model families | Low |
| C01.09-U9 | Which verifier gives most gain per token: unit test, symbolic check, rubric, self-check? | Verifier priority order by task class | S4, S8 | K22 d17, d04, d16; no head-to-head table | Four verifiers in one best-of-N loop; items with tests; gain per 1k tokens | Same rank order on 2+ task classes; adopt the top as default | Med |
| C01.09-U10 | Does any scaffold gain from math carry to non-math domains? | Per-domain switching of operators | all | K15 contested (c22 vs a07); trained models only | Same scaffold on math, logic, code, planning; per-domain gain | Gain positive in 3 of 4 domains; otherwise restrict to domains where it works | Med |
| C01.09-U11 | Is our item set contaminated? | Prefix-completion check in the bench harness | G7, bench | K09 established for Qwen (b21: 54.60% vs 3.8%); older models only | Give 60% of each item to our model and a clean control; compare exact completion | Run always; drop items where completion exceeds control by 20+ points | High |
| C01.09-U12 | Does a capped single chain plus vote beat one long chain at our budgets? | Confirms G11 cap values for our model | G11 | K21 established (d12, d13, d16); other models | Cap at 1k/4k/16k vs vote of short chains at the same total tokens | Short-chain vote wins at 2+ budgets; set the cap at the peak | Med |
| C01.09-U13 | Does a step audit add anything over a final-answer check? | Keep step checks light or drop them | S4, S8 | K02 single-source, qualitative (a11, b04); K17 | Final-answer check vs step audit vs both; math items with known steps | Step audit adds 3+ points at equal tokens: keep; else drop | Low |
| C01.09-U14 | Which code-side trigger best fires the right operator: sample disagreement or token confidence? | A trigger rule for S6 | S6, G1 | K20 d02 single-source; activation classifier, needs internals | Disagreement among 4 samples vs token confidence vs never | Disagreement trigger beats never by 3+ points at equal tokens | Med |

## Open questions we cannot test on our bench yet

- Paired comparison of RL-trained vs base model on post-cutoff problems. Needs matched checkpoints; none located.
- Agentic-RL ablation beyond SWE tasks. No pure ablation found; needs a tool-use bench with executable checks.
- 2026 first-appearance work on rubric, non-verifiable and test-time RL. The search was rate-limited; redo it.
- Whether ProRL boundary expansion is real or a base-weak effect. Needs trained models; only the pass@k measurement transfers.
- Whether the 5-15 point seed SD holds for our models. One paper, not fully re-verified; measure on our bench.
- Steering by activation vectors. Needs open weights and internals; our agent is API-only.
- A scaffold-level analogue of a pass@k reward (keeping coverage). Not defined yet.

## Order to run

1. **C01.09-U11 plus C01.09-U4 (contamination check and low-temperature and vote baselines).** Cheapest, and every later comparison depends on them.
2. **C01.09-U1 with the filler control, and U3 (format baseline) in the same run.** Highest expected gain: tests whether RL-learned behaviours work as prompt-time operators and how much is format or length.
3. **C01.09-U2 (signal vs schedule firing).** Tests the core of G1 on the same items and harness as U1.
