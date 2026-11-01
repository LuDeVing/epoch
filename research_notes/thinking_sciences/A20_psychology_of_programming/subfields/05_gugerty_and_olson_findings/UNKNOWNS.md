# Gugerty and Olson findings: what we don't know and should test
*Candidates for the schema that are not established. Nothing here goes into SCHEMA.md until its test passes. Source: DEEP.md, claims.jsonl, critique.md in this folder.*

## Test before adding
| ID | What we don't know | If it works, we add | Schema part | Evidence so far | Test (arms at equal tokens; items; metric) | Add if | Priority |
|---|---|---|---|---|---|---|---|
| A20.05-U1 | Does an edit guard (reject edits that break syntax or checks) cut failed edits on our bench? | Guard in S5 | G5, S5 | K11 single-source (SWE-agent 18.0 vs 15.0); older models | Free edits vs guarded edits; seeded-bug items with hidden tests; resolve rate and regressions | Resolve rate +2 points or regressions down 25% relative, token rise under 10% | High |
| A20.05-U2 | Do keep-best-so-far with revert plus a 2-edit cap per round reduce regressions? | Revert rule and edit cap in S5 | G6, S5, memory | K02 contested; only patch-level analogue (d12); human-only | Last-state vs best-so-far-revert plus cap; same items; new failing tests per edit, resolve rate | Regressions down 25% relative and resolve rate not lower | High |
| A20.05-U3 | Does a fresh start after 2 failed rounds beat continuing, on current strong models? | Context reset in S6 | S5/S6, memory | K10 single-source; older and small open models; Claude 3.7 hit 100% | Continue vs reset (problem plus best-so-far); items where round 1 fails; pass rate | +3 points on items that reach round 3, on our main model | High |
| A20.05-U4 | Does running pass-to-pass tests before accepting a patch cut wrong accepts? | Regression gate in S8 | G3, S8 | K23 single-source (7.8% fail full suite; one benchmark) | Target-test accept vs target plus regression accept; correctness of accepted patches | Wrong accepts down 30% relative, resolved loss under 1 point | High |
| A20.05-U5 | Does a separate diagnosis call with a larger budget beat joint repair? | DIAGNOSE step before S5 repair | S5, S6 | K08 established for human or stronger-model feedback; equal-token form untested; d14 no control | Joint repair vs diagnose (2x budget) then repair; equal total tokens; fix rate | Fix rate +3 points | High |
| A20.05-U6 | Does capped read then forced ranked hypothesis beat full read at equal tokens? | Read cap and hypothesis forcing in S1/S2 | S1/S2 | K01 single-source, K05 contested (Ko and Uttl null), K21 says reading is cheap; human-only | Capped vs full read; same items; hypothesis hit rate and fix rate | Fix rate +2 points, or not lower with tokens down 20% | Med |
| A20.05-U7 | Does showing the model's own draft as a third party's patch (with a "Wait" cue) lower the blind spot without raising overturn of correct answers? | Third-party review framing | S5, O-revise | K19 single-source; open models, injected-error tasks; K20 says overturn persists | Standard self-review vs third-party framing plus Wait; fix rate and rate of correct answers overturned | Fix rate +3 points and overturn rate no higher | Med |
| A20.05-U8 | Does a stall rule (force a hypothesis different from all earlier ones after a failed round) reduce looping? | Stall rule in S6 | S6 | K24 single-source (agents loop on a failed strategy) | No rule vs stall rule; failed-round traces; share of looping traces and fix rate | Looping traces down 25% relative, fix rate not lower | Med |
| A20.05-U9 | Does a system summary before the first edit improve fix rate? | Summary step in S1/S2 | S1/S2 | K03 single-source; Vessey human, N=16 | No summary vs summary; same items; fix rate | Fix rate +2 points | Med |
| A20.05-U10 | Does fixing one bug at a time beat all at once on multi-bug items? | Serial bug fixing | S6/O3 | K16 single-source (GPT-4 55.9 at four bugs) | All-at-once vs serial with a test after each; 1 to 4 bug items; pass rate by bug count | +5 points at 3 or more bugs | Med |
| A20.05-U11 | Does blind-rated hypothesis quality predict fix rate per trace? | A hypothesis-quality gate | S2, S6 | K22 single-source (system level only) | Blind rating on logged traces; Spearman correlation | rho of 0.3 or more; needed before U6 and U5 are worth building | Med |
| A20.05-U12 | Does trimming history to the last 5 observations help at equal tokens? | History trim | memory | K12 single-source; SWE-agent only | Full vs last-5 plus summary; fix rate | Fix rate not lower and tokens down 15% | Low |
| A20.05-U13 | Does requiring reproducing evidence for any claimed bug reduce invented issues? | Evidence-before-claim rule | G2 | K17 single-source (40% non-existent issues, GPT-3.5) | No rule vs rule; false-claim rate and fix rate | False claims down 30% relative, fix rate not lower | Low |
| A20.05-U14 | Does a fixed localise-repair-validate pipeline beat free-form loops at equal tokens? | Fixed pipeline mode | S-validate | K13 single-source (Agentless 32.00% at $0.70) | Pipeline vs free-form; same items; resolve rate | +2 points, or equal rate at 30% fewer tokens | Low |

## Open questions we cannot test on our bench yet
- Real Gugerty and Olson figures (sample, times, accuracy, bug-addition counts). Unblock: a library copy or the Ablex 1986 chapter.
- Katz and Anderson 1987 strategies. Unblock: access to the Taylor and Francis text or a mirror.
- Eye-tracking and modern-cohort replications (2015-2026). Unblock: open the two titles found (IEEE Access 2026 and a fine-grained novice assessment) and search again once API quotas recover.
- Human expert-novice process data on LLM-written code. Unblock: a human study; not feasible on our bench.
- Whether 2026 reasoning models still show Huang-style harm. Unblock: run our own model with and without an external check on the same items.
- Per-edit regression rate for agents. Unblock: log tests before and after every edit in our harness.
- A matched-compute control for same-model reviewers (d14 had none). Unblock: add a resampling arm to the test.

## Order to run
1. A20.05-U2 together with U1 (guard, best-so-far revert, edit cap): cheapest, closest to the schema's S5, and gives the first per-edit regression numbers.
2. A20.05-U3 (fresh start after 2 failed rounds): needs only round logs, and settles whether the one large LLM effect holds on our model.
3. A20.05-U5 (separate diagnosis with a larger budget): largest expected gain, since diagnosis is the established bottleneck; U11 on the same logs shows whether hypothesis quality is worth gating.
