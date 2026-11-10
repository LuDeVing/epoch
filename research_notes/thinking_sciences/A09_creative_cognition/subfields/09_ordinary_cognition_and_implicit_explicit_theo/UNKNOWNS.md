# Ordinary-cognition and implicit-explicit theories: what we don't know and should test

*Candidates for the schema that are not established. Nothing here goes into SCHEMA.md until its test passes. Source: DEEP.md, claims.jsonl, critique.md in this folder.*

## Test before adding

| ID | What we don't know | If it works, we add | Schema part | Evidence so far | Test (arms at equal tokens; items; metric) | Add if | Priority |
|---|---|---|---|---|---|---|---|
| A09.09-U1 | Does k short independent attempts plus code check beat the stepwise loop on insight-type items? | Explicit "wide sample then check" route for insight items in S3/S4 | S3, S4, G12 | K06, K19; d08, d09 are proxies on math/code; no direct test (single-source, human findings contested) | Stepwise S3-S5 vs k short fresh-context attempts plus check; BRAINTEASER and ARC items, 60 each; solve rate | Wide arm beats stepwise by 5 points or more, paired, on 2 of 3 item sets | High |
| A09.09-U2 | Which variation operator gives most distinct valid candidates per token? | Named default operator list for open mode | O (S3 open) | K10, K23; d02, d03, d04, d05 (single studies, no equal-token comparison) | Plain; temperature sweep; persona plus plan; in-context regeneration; verbalized sampling; 30 open prompts; meaning-based distinct count after dedup and run-check pass rate | Best operator gives 1.5x distinct valid count over plain at equal tokens | High |
| A09.09-U3 | Does a fresh-context restart (question plus surviving constraints only) beat continuing or a recap? | Restart rule in S6 | O, S6 | K01 (human), K26; d07 (recap recovers 15-20%); no LLM restart test (single-source) | Continue vs restart vs recap on items failed in round 1; second-half budget equal; solve rate | Restart beats continue by 3 points or more and recap not better | High |
| A09.09-U4 | On which task classes should the rationale be dropped, with current models? | S0 rule: direct mode for named classes | G11, S0 | K08, K25; c04 older models, Claude 3.5 Sonnet no harm; d10 no insight category (established for math, untested for insight) | Direct vs short rationale vs long rationale; ARC, BRAINTEASER, pattern-learning items; accuracy by class | Rationale loses by 3 points or more in a class on paired items | High |
| A09.09-U5 | Does an entropy or disagreement trigger for reframing help frontier models? | Signal trigger for O6/O8 in S6 | O, S6, G1 | K15; b14, b25: +8.41 pp on MATH-500 for small tuned models, about 0 elsewhere (single-source) | Fixed-step reframe vs on-stall vs on entropy/disagreement vs never; stalled items; solve rate per token | Signal trigger beats on-stall by 3 points or more and fixed by tokens per solve | Med |
| A09.09-U6 | Does an external verifier close the endorsement gap on riddles? | Code-side acceptance check for riddle-type items | G5, S7 | K16; b13, d14: models write the right candidate and do not endorse it (single-source; no verifier test) | Model self-acceptance vs rule or second-model verification; BRAINTEASER; accepted-correct rate | External check lifts accepted-correct by 5 points or more | Med |
| A09.09-U7 | How often is the first sample already the final correct answer on insight items? | Keep-first-sample rule made explicit | S4 harvest | K07; a24 (human, convergent word items), d06 (math); single-source | Log first sample vs final over all runs; no extra tokens | Non-correction rate of 70% or more AND no gain from late answers | Med |
| A09.09-U8 | Does a gap filler (nothing, light, heavy) change anything for an LLM? | Nothing (confirms a "do not add"); otherwise a filler step | O, S6 | K02; a07, b05 human only | Nothing vs light task vs heavy task between attempts; fresh-context vs same context | Add only if a filler beats nothing by 3 points with context held fixed; else record as dead end | Low |
| A09.09-U9 | Do distant-source cues help the agent on any item class? | O7 distant seed for open or design items | O7 | K12; c11: no average gain, top two models only for distant sources (single-source) | None vs near vs distant cue; open design items; run-judged originality and validity | Distant cue gives 0.3 points or more on 1-5 originality with no validity loss | Low |
| A09.09-U10 | Does a blended draft re-viewed under several framings (honing) beat discrete candidates? | Honing operator | O | K21; a12, a13 one lab, no LLM test (single-source, human self-report) | Discrete candidates vs one draft re-viewed under 3 framings; open items; distinct count and quality | Honing arm beats discrete by 10% in distinct valid count | Low |
| A09.09-U11 | Does the divergent-then-convergent two-stage prompt help at equal tokens? | Explore-then-satisfy prompt for open mode | S3, O | K13; c03 (+6.5% efficiency), d04 (13 vs 8 distinct); CoT = base in d04; token cost unmatched | Plain vs explore-then-satisfy vs plain with extra samples to match tokens; open items | Beats extra-samples control by 10% in distinct valid count | Med |
| A09.09-U12 | Where does diversity plateau after dedup, per model and task? | Stopping rule for N in open mode | O, G12 | K14; c10: 5% non-duplicate of 4000 (single point); d05 | Sweep N from 10 to 1000 with meaning dedup; distinct count curve; two models | A knee is found and held across models; set N at the knee | Med |
| A09.09-U13 | Do process metrics (distance travelled, reframe count) predict solved items? | Logged diagnostics for S6 control | Log, S6 | K17; c05-c07, c13 (older models, embedding proxies) | Log metrics on runs from other tests; correlate with solve rate | Metric predicts solve with AUC 0.65 or more | Low |

## Open questions we cannot test on our bench yet

- **EII as a full architecture.** Needs a defined confidence integration between a wide sampler and a rule check. Unblock: U1 plus U6 first, then a threshold-based version.
- **Incubation as a hidden process in a model.** No way to inspect hidden computation between calls on API models. Unblock: open-weights run with activation logging, not on our bench.
- **Original numbers for Schooler 1993 and Gabora and Saab 2011.** Papers not opened. Unblock: retrieve full texts. Matters only for human-side claims, not for the agent.
- **Weisberg 2015 and Fleck and Weisberg 2013 (five problems).** Full texts not read. Unblock: library access.
- **Honing theory on LLMs.** No operational definition of "state of potentiality" for a model. Unblock: a clear test design (U10 is a crude proxy).
- **Frontier-model process measures.** Process gaps (association distance, representational change) were found on GPT-3.5 to GPT-4o. Unblock: rerun the Zhang et al. battery on current models.
- **Insight items with a cheap exact verifier.** Riddle items lack one, so sampling-with-check results (d09) may not transfer. Unblock: build item sets with checkable answers, or accept an LLM-plus-human gold check.
- **Contamination.** Riddle and puzzle items may be in training data. Unblock: new held-out items.

## Order to run

1. **U2 (variation operators).** Cheapest, no gold answers needed beyond a dedup and run check, and the result feeds the open-mode default directly.
2. **U1 (wide sample plus check versus stepwise).** The only direct test of the EII split on an LLM; no published answer exists.
3. **U3 (fresh-context restart).** Cheap to build from logged failures and decides whether S6 needs a restart rule; also covers the incubation question for LLMs.
