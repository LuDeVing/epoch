# Premortem and prospective hindsight: what we don't know and should test
*Candidates for the schema that are not established. Nothing here goes into SCHEMA.md until its test passes. Source: DEEP.md, claims.jsonl, critique.md in this folder.*

## Test before adding
| ID | What we don't know | If it works, we add | Schema part | Evidence so far | Test (arms at equal tokens; items; metric) | Add if | Priority |
|---|---|---|---|---|---|---|---|
| E12.05-U1 | Does a code-verified failure-frame cause list beat plain Retry at an impasse? | Premortem operator at S6; verified causes shown to S5 | S6, S5, new operator | K12, K13, K23; single-source (safety task); older models | Retry vs risk-list vs failure-frame unverified vs failure-frame verified vs extra attempts; ARC items failing the first check; items solved after S6 | Verified arm beats Retry and extra-attempts arm by 3+ points, paired interval excludes 0, 3 seeds | High |
| E12.05-U2 | Do verified causes beat unverified ones? | Rule: only run-confirmed causes pass to S5 (hardens G2) | G2, S5 | K28 d17 single-source, indirect; K13 established | Same items; unverified vs verified failure-frame arm | Verified beats unverified by 2+ points, or unverified loses to Retry | High |
| E12.05-U3 | Is the failure frame better than a plain "list risks" prompt? | Keep failure wording; else use a plain risk list | S6 prompt | K23 d10 (no plain-risk baseline); K08 contested | Failure-frame vs plain risk-list vs success-frame, 10 samples per item; confirmed causes per 1k tokens | Failure frame gives 20%+ more confirmed causes per 1k tokens | High |
| E12.05-U4 | Can causes become targeted test inputs that catch fitted-but-wrong answers? | Cause-driven mutation inputs for the unfitted check | S4, S8, G3 | K13, K17; no direct test; diversity loss c20 | Cause-derived mutations vs random mutations vs held-out only; ARC items with known fitted-wrong programs; wrong-answer detection and false alarms | Detects 15+ points more wrong answers than random mutations at equal runs, false alarms no higher | High |
| E12.05-U5 | Does the benefit appear only on hard items and cost tokens on easy ones? | Gate the premortem on the S0 pass rate | S0, G11, G12 | K06 Peabody Exp 3 single-source; K26 | Premortem on easy vs hard bands, equal total tokens | Net gain 3+ points on hard band and no loss on easy band | Med |
| E12.05-U6 | How many causes to request (3 to 5 vs 12)? | Cap on cause count | prompt parameter | a23 human only; single-source | 3, 5, 12 causes; confirmed causes per token; solved items | Smaller cap equals or beats 12 per token | Med |
| E12.05-U7 | Does "assume each candidate true and explain" beat counterexample search for selection? | Assume-true explanation before select | S7 | a25, a20, a21 human only; Koriat replication contested | Assume-true vs vote vs counterexample search; items with 2 to 4 candidates; selection accuracy | Beats counterexample search by 2+ points | Med |
| E12.05-U8 | Does a premortem shift P(True) or sample agreement, and does the shift track error? | Post-premortem confidence as an impasse signal | S0, S6, G1 | K21 no study; K03 human only | AUC for correctness before and after the premortem; items with known truth | AUC rises by 0.05+; otherwise drop | Med |
| E12.05-U9 | Does a forced plan-revision step after listing causes raise plan success? | Forced revision step | S5 | K27 d07 single-source, no control | Premortem + forced revision vs premortem only; multi-step plan items; plan success | Success up 3+ points | Med |
| E12.05-U10 | Is failure direction better than success direction for LLMs? | Keep failure wording | S6 prompt | K08, K24 contested; null at ceiling | Backward-failure vs forward-success prompts, equal tokens | Failure beats success by 2+ points; otherwise use the cheaper | Low |
| E12.05-U11 | Does hiding the draft when checking each cause help? | Draft-hidden cause checks | S4 | K14 c11 single-source on facts | Draft hidden vs visible; confirmed-cause precision | Precision up 10+ points | Low |
| E12.05-U12 | Does backward planning from the end state help on hard items? | Promote O5 from [S] | O5 | K26 d06 numbers unread; c12, b21 | O5 on vs off at S6, hard items only | Beats Retry by 3+ points on hard band | Low |
| E12.05-U13 | How diverse are repeated premortem samples from one model? | Diversity constraint (history of tried categories) | S3, diversify | K17 c20 single-source | Distinct categories per 10 samples, with and without a "different from list" history | History raises distinct categories 30%+ and confirmed yield does not fall | Low |

## Open questions we cannot test on our bench yet
- Veinott and Lehman 2024 results (LLM vs student causes): Springer is behind a login wall. Unblock with PDF access or a request to the authors.
- The true Mitchell 1989 effect and N: need the full paper.
- Peabody cadet statistics: PDF returned 403.
- Park, Lu, Hedgcock 2017 numbers and the corrigendum.
- Whether reasoning models change the self-correction results: the data is GPT-3.5 and GPT-4 era; run our own check with current models.
- Plan-outcome effects of the human premortem at scale: no field study exists; not testable on our bench.
- Safe-dissent effect: needs human or multi-agent groups; excluded by G4 and G9.
- AUGUR full results (abstract only).

## Order to run
1. E12.05-U1 with U2 (verified vs unverified vs Retry): cheapest, and decides whether any premortem step survives against Retry.
2. E12.05-U3 (failure frame vs plain risk list): tests whether the frame itself matters, which is the core of the claim.
3. E12.05-U4 (cause-driven test inputs): the one use that fits G3 and could add what Retry cannot.
