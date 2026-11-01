# Network epistemology: what we don't know and should test
*Candidates for the schema that are not established. Nothing here goes into SCHEMA.md until its test passes. Source: DEEP.md, claims.jsonl, critique.md in this folder.*
## Test before adding
| ID | What we don't know | If it works, we add | Schema part | Evidence so far | Test (arms at equal tokens; items; metric) | Add if | Priority |
|---|---|---|---|---|---|---|---|
| F03.04-U1 | Does isolation beat sharing more as items get harder? | Rule: independent attempts on hard items, skip extras on easy | G4/G12 | K32, K27, K30; contested, indirect, older models | Independent+vote vs shared-from-start vs one long attempt; items binned by single-agent pass rate; accuracy gap per bin | Gap >= 2 points in hardest bin and <= 0.5 in easiest, 3 seeds | High |
| F03.04-U2 | Does one bounded merge after isolation beat plain vote? | Step: independent drafts, then one merge over checked, deduplicated drafts | S3/S7 merge | K24 (human, single-source); K28 contested; K29 anchoring | (a) independent+merge, (b) independent+vote, (c) shared from start; items with a checker; accuracy | (a) beats (b) by >= 2 points, CI above 0 | High |
| F03.04-U3 | Does forced reporting of failed attempts help a shared channel? | Rule: every shared note includes failed attempts | S3/O-share-negatives | K15 contested; Zheng 2026 only; token cost unmeasured | Free vs forced failure reports vs none on dead-end search items; duplicates, accuracy, tokens | Accuracy +2 points or duplicates -30% at no more tokens | Med |
| F03.04-U4 | Fresh attempt vs revision for current reasoning models, by task type | Per-type table: revise vs resample | S3/O-revise | K28 contested; GPT-3.5-era evidence; Madaan hint | One unchecked revision round vs one extra fresh attempt, equal total tokens, per task type | Resample wins in >= 2 of 3 types by >= 1 point | High |
| F03.04-U5 | Does routing by first-sample agreement work? | Router: high agreement revise once; low resample | S1/S3 | K27 single paper, fine-tuned reviser | Router vs always-revise vs always-resample, equal tokens | Router beats best fixed arm by >= 1.5 points | Med |
| F03.04-U6 | Do prompt variations restore diversity among independent attempts? | Prompt-variation list for generation breadth only | G4/S3 | K17, K21 contested; no direct persona measure | Same prompt vs 4 varied prompts; pairwise distance, coverage, voted accuracy | Coverage +5 points, voted accuracy not lower | Med |
| F03.04-U7 | Do high effort and low temperature cut diversity enough to hurt? | Rule: set effort and temperature by phase | G4/G12 | K21 contested; Zheng, Hirota: non-bench tasks | Low vs high effort; T 0.2 vs 1.0; equal tokens; unique answers, accuracy | Diversity drop with accuracy loss >= 1 point | Med |
| F03.04-U8 | Do restarts fix in-context under-exploration? | Restart plus external summary on hidden-rule tasks | S3/restarts | K26 single paper (GPT-4, bandit) | N restarts vs one long run vs one run with external history, 5-arm bandit gap 0.2 | Late best-arm rate +20 points | Med |
| F03.04-U9 | Verifier vs confidence-weighted vote vs plain vote vs average at our N | Selection ladder | O-aggregate | K31 established for voting; expert dilution vs these untested | Average vs vote vs confidence-weighted vs verifier, N = 8, own tasks | Order holds, CIs exclude 0 for adjacent pairs | High |
| F03.04-U10 | Does a diversity monitor predict when sharing hurts? | Gate: stop sharing if pairwise distance falls too low | G4/S3 | K13 single-source; effect vanishes without one task | Distance before/after sharing vs accuracy change on 100+ items | r <= -0.3 and gate gains >= 1.5 points | Low |
| F03.04-U11 | Does the Kummerfeld-Zollman reversal exist for LLMs? | Rule: share more when attempts are very exploratory | S3/temperature | K04 single-source; no LLM test | Temperature sweep crossed with isolated vs shared | Sign flips with temperature, gap >= 2 points each side | Low |
| F03.04-U12 | Break-even between independent vote and limited-visibility revision | Budget rule: N independent below X tokens, revise above | S3/G12 | GAP 9 open; Tran and Kiela hint at small-budget talk advantage | Four total budgets, both arms | Crossover found and stable on 2 benchmarks | Med |
| F03.04-U13 | Does planted-error spread replicate with strong models? | Visibility cap on early drafts | S3 | K14 (GPT-3.5 only) | Planted wrong sketch seen under full vs 2-neighbour vs none on current model | Error spread -10% with sparsity, correct uptake loss <= 5% | Low |
## Open questions we cannot test on our bench yet
- Real Bala-Goyal bandit with many LLM agents: needs a multi-agent simulator with cheap noisy trials and thousands of runs. Unblock with a small synthetic coin-flip environment.
- Human replication of the Zollman effect: outside our domain. Derex and Boyd and Mason and Watts stay as weak priors.
- Unopened foundations (Mayo-Wilson et al 2011/2013, Lazer and Friedman 2007, Holman and Bruner 2015): need full texts.
- Rosenstock 2017 exact numbers: PDF link dead. Find an archive copy to lift K03 from single-source.
- Token cost of forced failure reporting: not measured by Zheng. Measure inside U3.
- Whether 2026 reasoning models behave like the GPT-3.5 and 7B-8B models that dominate the literature: needs the tests above run on current models.
## Order to run
1. U1 (hardness split): cheapest, reuses existing arms, and decides whether isolation is worth its tokens by item type.
2. U9 (selection ladder): verifier vs confidence vote vs vote; high expected gain, easy to run.
3. U2 (isolate then one merge): the only untested design with both human and LLM hints of beating plain vote; also tests anchoring.
