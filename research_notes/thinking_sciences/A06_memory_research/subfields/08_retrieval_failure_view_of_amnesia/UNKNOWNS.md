# Retrieval failure view of amnesia: what we don't know and should test

*Candidates for the schema that are not established. Nothing here goes into SCHEMA.md until its test passes. Source: DEEP.md, claims.jsonl, critique.md in this folder.*

## Test before adding

| ID | What we don't know | If it works, we add | Schema part | Evidence so far | Test (arms at equal tokens; items; metric) | Add if | Priority |
|---|---|---|---|---|---|---|---|
| A06.08-U1 | Does re-querying memory with a reverse and 2 paraphrased cues beat one query? | Retry-with-alternate-cues rule before "not found" | O (query rewrite), memory | K13 established for cue form; K24 single-source, gap 3 open (d13, d14) | 100 to 200 recall items over 50 to 100 notes; A one query, B reverse + 2 paraphrases, tokens matched; hit rate | B beats A by 3+ points on reversed or paraphrased items and by 0 or more on same-form items, with false finds under 5% | High |
| A06.08-U2 | Does a one-line fact key written with each note raise recall? | Write-time fact key in the note format | memory | K23 single-source (LongMemEval +5.4% QA, recall@5 0.582 to 0.644) | Same note set with and without fact key; recall@5 and answer accuracy; token cost counted | +3 points answer accuracy at equal tokens | High |
| A06.08-U3 | Does deleting stale notes in code beat appending with a "latest wins" rule? | Overwrite-not-append memory rule | memory, G5 | K15, K25 single-source; instructions give under 10 points (d16); deletion never tested | Key-value streams with 3 to 150 updates; A append + instruction, B delete stale, C mock QA reset; accuracy by update count | B beats A by 10+ points at 50+ updates, and no loss when history is needed (control items) | High |
| A06.08-U4 | Does restoring the encoding framing at read time help recall (state matching)? | Store framing with each note and replay it at read | memory, S1 | K04, K19, K20 single-source, rat data and analogy; no LLM test (critique gap 8) | Facts written under framing F, probed under G; A no framing, B framing restored, C neutral text of same length; recall | B beats both A and C by 5+ points | High |
| A06.08-U5 | Does a short reminder (topic summary or 2 to 3 examples) bring back a dropped or buried skill? | Reminder step on a signal (low score or skill drop) | S3, S6 | K10 (weight updates), K21 (prefix, in-context relearning modest); older or open weights only | Skill items degraded by a long distractor or style prompt; A no cue, B 2 to 3 examples, C restyled or translated prompt; accuracy | B or C closes 40%+ of the gap at no more than 20% extra tokens | Med |
| A06.08-U6 | Does cross-paraphrase agreement pick the right candidate better than plain majority? | Paraphrase-agreement selector (cheap feeling-of-knowing) | S7, G5 | K12 and K26: probe gain +1.7 over majority at N=1000 with weights (d17); no transfer (d18); API proxy untested; G4 warns of correlated samples | Closed-book QA; A majority over N, B agreement over 3 paraphrases x N/3; accuracy and calibration | B beats A by 1.5+ points, or ties and gives a usable abstain signal (AUROC 0.7+) | Med |
| A06.08-U7 | After long gaps, should old notes outrank recent ones when the query context matches the old one? | Context-match term in note ranking | memory | K20 single-source (Sissons and Miller, 27 days, rats) | Notes in order A,B vs B,A with simulated gaps; A recency rank, B context match + recency; correct note picked | B beats A by 5+ points on matched-context items without losing on recent-context items | Med |
| A06.08-U8 | Can the agent detect "stored but not surfaced" cheaply? | Exact-lookup fallback and a stored/never-stored flag | S6, memory | K26: P(IK) needs training; K02 analogue (direct vs natural route) | Mix of stored and never-stored facts; A single query, B retry loop + exact lookup; false-find and missed-find rate | Missed finds drop by 30%+ and false finds stay under 5% | Med |
| A06.08-U9 | Is position still a cue on current models? | Layout rule: key evidence at start or end | S0, S1 | K14 single-source, 2023 models (c16, c17) | 10 to 20 document prompts, key doc at start, middle, end; accuracy | Middle drops 5+ points below ends; else drop the rule | Med |
| A06.08-U10 | Do source tags prevent new-into-old contamination after a reminder? | Source-tagged notes | memory | K27 contested (Hupbach intrusion U=20, p<0.01); no agent test | Notes from two sessions, one reminded; A untagged, B tagged; intrusion rate | Intrusions fall by 30%+ | Low |
| A06.08-U11 | Which retrieval signals (recency, relevance, importance) carry the gain in agent memory? | Drop the unused signals | memory | K17: designs differ, no ablation under equal tokens (c20 to c24) | One fixed agent task; full score vs each signal removed | A signal whose removal costs under 1 point is dropped | Low |
| A06.08-U12 | Does model-side "forget" or hide actually remove content from the model's behaviour in the scaffold? | Keep input hygiene in code only (already rule) | S1, G5 | K11, K16 established for weights; no prompt-level test | Anchor material in prompt vs removed in code vs "ignore this" instruction; answer shift | Instruction arm shifts answers by under half of the removed-in-code gap | Low |

## Open questions we cannot test on our bench yet

- Tally of failed vs successful reversals in the published Psychological Review paper: full text not obtained. Unblock: institutional access, or a request to the authors; or a new systematic count of the studies in its Table 1.
- Independent replication count for Ryan 2015 engram rescue: needs a systematic search by lab lineage. Rodent work, not testable on our bench.
- Steenen restricted pooled propranolol effect with CI: needs the forest plot data. Human clinical, no bench use.
- Kindt 2009 effect size: primary not read.
- Probe-based re-ranking needs hidden-state access; the bench uses API models. Unblock: an open-weights run.
- Weight-update recovery (spurious forgetting probe) needs training access. Unblock: a small open model.
- Whether lost-in-the-middle and reversal-curse numbers hold for current models: needs fresh runs; cheap, but not about this subfield's core claim.

## Order to run

1. A06.08-U1 (multi-cue retry vs one query): cheapest, applies to every memory read, and K24 gap 3 has no data.
2. A06.08-U3 (delete stale vs append): large expected gain (over 10 points), the instruction-only fix is known to fail.
3. A06.08-U4 (restore encoding framing): the only direct test of the core claim in an LLM; the control arm separates match from length.
