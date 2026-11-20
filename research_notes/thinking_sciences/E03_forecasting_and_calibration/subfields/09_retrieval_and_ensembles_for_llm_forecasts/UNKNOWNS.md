# Retrieval and ensembles for LLM forecasts: what we don't know and should test

*Candidates for the schema that are not established. Nothing here goes into SCHEMA.md until its test passes. Source: DEEP.md, claims.jsonl, critique.md in this folder.*

## Test before adding

| ID | What we don't know | If it works, we add | Schema part | Evidence so far | Test (arms at equal tokens; items; metric) | Add if | Priority |
|---|---|---|---|---|---|---|---|
| E03.09-U1 | Does 5 averaged runs beat 1 run with 5x reasoning budget? | Rule: averaged short runs by default for forecasts | S3, G11 | K01 (equal question, never equal tokens); CHAIN d14 closest; single-source | 1 long run vs 5 short runs, same total tokens; 150+ post-cutoff binary items; paired Brier | 5 short beat long by at least .003 with paired CI excluding 0 | High |
| E03.09-U2 | Do different prompt personas or decompositions decorrelate runs enough to beat identical copies? | Mixed-prompt ensemble in S3 | S3 | K17, K18 (d11-d13: models, not prompts); single-source | 5 identical vs 5 mixed-prompt vs 3 models; 150 items; Brier and pairwise run correlation | Mixed beats identical by .003 and correlation drops below .8 | High |
| E03.09-U3 | Does Platt or log-odds extremizing on the mean help our agent? | Calibration step after S3 (and edit G4 wording for probability tasks) | S3, G4 | d10 (AIA, one source); contradicts G4 only for voters | Mean vs Platt vs d=2,3 on same runs; train Platt on one half, test on the other | Brier gain at least .004 out of sample, no loss on 2 of 3 splits | High |
| E03.09-U4 | Does a base-rate-first step plus per-document cap fix retrieval inflation on a frontier agent? | Reference-class prior step before evidence; shift cap | S2, S3, G | K19 (d16, 7-8B only) | Retrieval vs retrieval + base-rate step vs + cap vs no retrieval; track mean forecast shift and Brier | Mean shift within .05 of base rate and Brier no worse than no-retrieval | High |
| E03.09-U5 | Can a rule cap poison damage without dropping genuine news? | Per-document influence cap; corroboration requirement | G | K07 (d17: every defense has a bypass); no working defense | Plant 1 and 5 fake articles on 100 items; arms: none, shift cap, independent-source requirement, per-doc median | Flip rate under 30% at k=5 and clean Brier loss under .003 | High |
| E03.09-U6 | Does an LLM supervisor with its own search beat the plain mean? | Agentic supervisor with confidence-gated override | S3, S7 | d08 (AIA .1125 vs .1140, single source); non-agentic worse (established) | Mean vs agentic supervisor, supervisor search budget included in tokens | Beats mean by .0015 at equal tokens on 300 items | Med |
| E03.09-U7 | Does blending the market price in code beat putting it in the prompt or letting the model update? | Code blend rule with a weight | S3, memory | K10, K12 (human median study b09; AIA d09); established direction, weight unknown | Blind vs price in prompt vs 50/50 blend vs 4x crowd; price-bearing items only | Code blend beats prompt arm by .003 on mid-range prices (.2-.8) | Med |
| E03.09-U8 | Is a price-divergence review step (Cassi) worth anything over the price? | Divergence-triggered second look | S3, G1 | K11 contested; d02 +0.6 BI ns | Plain blend vs blend + review when gap over .2 | Review arm beats blend by .005 | Low |
| E03.09-U9 | Does gating search by crowd uncertainty or relevant-article count save tokens without loss? | Search gate in S0 | S0, G12 | a04 (Halawi conditions, post hoc) | Always search vs gate (price .3-.7 or 5+ relevant docs); equal total tokens | Same Brier (within .002) at 30% fewer tokens | Med |
| E03.09-U10 | Does a belief state (probability + evidence summary carried between steps) cut run noise? | State record in S3/memory | S3, memory | d04 (2 of 3 backbones; SD .094 to .030) | With vs without belief state; 20 repeats on 20 items; SD and Brier | SD falls by 40% and Brier does not rise | Med |
| E03.09-U11 | Does consistency between paired questions pick or weight good ensemble members? | Consistency filter in S3 | G, S3 | K14 contested (d19: correlation across models only; patching did not help) | Drop or downweight most inconsistent members vs equal weights | Beats equal weights by .002 | Low |
| E03.09-U12 | Does the gain from averaging depend on run SD (so we can average only when SD is high)? | Adaptive run count: 2 runs, add more only if they disagree | S3, G12 | a13 single-source; K02 | Fixed 5 vs adaptive (stop if first 2 within .05); equal total tokens | Adaptive matches fixed-5 Brier with 30% fewer tokens | High |
| E03.09-U13 | Does model-guided retrieval (retrieve only the inputs a quantitative base needs) beat open retrieval? | Retrieval planner in S2 | S2, S3 | c19 (one paper, FutureX) | Open retrieval vs model-guided at equal search count | Base-probability Brier better by .005 | Low |

## Open questions we cannot test on our bench yet

- **Leak-free benefit of Halawi's retrieval stack.** Needs a frozen pre-cutoff corpus for our questions. Unblock: build or license a dated archive; use only post-cutoff questions.
- **Cassi's exact crowd-adjustment rule.** Unpublished. Unblock: the authors publish the rule, or we design our own (U8).
- **xAI 8-run average vs its search tools.** No ablation exists. Unblock: an ablation from FRI or the entry owners.
- **Frontier models' resistance to fake articles in a real pipeline.** Zhang and Stadie (a19) test frontier models; Lu and Zhang test only 7-8B. Unblock: our own planted-article set (U5).
- **How many distinct members before the gain flattens, for frontier models on news questions.** Needs several providers and a few hundred resolved items.
- **Questions without a market price.** Most evidence is on market questions; we need a base rate from outcomes of our own item class.
- **Winner statistics (28 vs 7 calls).** Observational; cannot be tested without an experiment on a live tournament.

## Order to run

1. **U1 (equal-token single long run vs averaged runs).** The largest hole in the evidence and it decides how G11 and S3 split the budget.
2. **U12 (adaptive run count by run SD).** Cheap: reuses U1 runs and could cut tokens by a third.
3. **U4 with U5 (retrieval inflation fix and poison cap).** Retrieval harm is established and the fixes are untested on frontier agents; one planted-article set covers both.
