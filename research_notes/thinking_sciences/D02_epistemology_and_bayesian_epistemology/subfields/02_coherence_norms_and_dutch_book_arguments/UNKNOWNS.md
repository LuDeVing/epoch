# Coherence norms and Dutch book arguments: what we don't know and should test
*Candidates for the schema that are not established. Nothing here goes into SCHEMA.md until its test passes. Source: DEEP.md, claims.jsonl, critique.md in this folder.*

## Test before adding

| ID | What we don't know | If it works, we add | Schema part | Evidence so far | Test (arms at equal tokens; items; metric) | Add if | Priority |
|---|---|---|---|---|---|---|---|
| D02.02-U1 | Does a forced partition (all options in one prompt, renormalised) beat independent per-option probabilities? | Rule: always elicit the whole partition in one prompt | G5, S3 | K27, K28 (indirect, no direct study); single-source | Arms: joint letter softmax with prefill; per-option P(True) then normalise; per-option raw. 200 exclusive-choice items, 4 to 5 options. Accuracy, Brier, ECE | Joint beats per-option by at least 2 points accuracy or 0.01 Brier, paired CI excludes 0 | High |
| D02.02-U2 | Does the raw sum of independent per-option probabilities predict wrong answers (a free doubt signal)? | Raw-sum threshold as a G1 trigger | G1, S0 | K14 (check-dependent, contested); d14 never measured the sum | Same items as U1; AUROC of abs(sum - 1) for predicting error; compare with max-probability AUROC | AUROC at least 0.60 and adds at least 0.02 over max-probability alone | High |
| D02.02-U3 | Is plain renormalisation enough, or does a simplex projection help? | Replace divide-by-sum with projection | G5 | K06 (human only, single-source) | Same samples, two post-processing arms; Brier | Projection beats normalise by at least 0.005 Brier | Low |
| D02.02-U4 | Does shuffling option order and averaging beat single-order renormalisation at equal tokens? | Order-averaging in S3/S4 | S3, S4 | K29 (bias established; equal-token cost untested) | k orders x fewer attempts vs 1 order x k attempts; accuracy, Brier | Order-average wins by at least 1 point accuracy | Med |
| D02.02-U5 | Does an instructed residual option fix the missing-mass problem in current models? | "Other" option plus instruction in prompts | S1, S3 | K30 (single-source; 2022 52B model) | Residual share 0, 10, 30% of items; with and without instruction; residual use rate, named-sum error | Residual use within 10 points of true rate with instruction, and no accuracy loss on 0% items | Med |
| D02.02-U6 | Does a negated or paraphrased re-ask repair give any Brier gain at equal tokens? | Re-ask repair step in S8 | S4, S8, G3 | K11, K13, K15 (violations established; gain unproven) | Arms: re-ask negation and paraphrase; resample same prompt; plain. Three check types and Brier | Brier drops at least 0.01 and untargeted checks do not worsen | Med |
| D02.02-U7 | Does coherence-weighted aggregation of samples beat the equal-weight vote? | Weight votes by own sum deviation | G5, S7 | K24 (second-hand, human only, unreproduced) | Equal-weight vs coherence-weighted vote at same sample count; accuracy and Brier | Gain at least 2 points accuracy, CI excludes 0 | Med |
| D02.02-U8 | Do irrelevant lines (stated guess, emotion) raise raw-sum drift in our scaffold prompts? | Strengthen S1 input hygiene for probability prompts | S1 | K17 (single-source, one model) | Prompt with and without an irrelevant line; change in sum deviation and accuracy | Drift up at least 2x or accuracy down at least 2 points | Med |
| D02.02-U9 | Does reasoning (thinking tokens) reduce probability-identity violations more than resampling at equal tokens? | Short-reason mode for probability steps | S3, G11 | K20, K31; CoT did not help complementarity (c12); untested for sums | Direct vs CoT vs 3 resamples; strong-violation rate on negation, paraphrase, Bayes | CoT cuts violations at least 25% relative more than resampling | Med |
| D02.02-U10 | Does batching evidence into one update beat sequential updating in numeric tasks? | Batch-update operator | O (update) | K21 (direction established, older base models) | Batch vs sequential on update tasks with 4 to 8 evidence items; distance to true posterior | Batch error at most 80% of sequential | Med |
| D02.02-U11 | Does arbitrage profit (LP score) work as a label-free monitor of the guardrail? | Cheap coherence monitor in S9 | S9, G7 | K16 (single-source, one domain) | LP score on 3 to 4 event panels with and without guardrail; correlate with Brier across model/prompt variants | Spearman at least 0.6 with Brier across at least 8 variants | Low |
| D02.02-U12 | Does incoherence grow with scaffold context length and memory load? | Memory trimming rule for probability steps | memory, S1 | Nothing found (gap 6); K17 hints at it | Same item with 0, 2k, 8k tokens of unrelated scaffold context; sum deviation and accuracy | Deviation grows at least 2x with context | Low |
| D02.02-U13 | Is a coherence-only objective gameable in our selectors? | Rule: any coherence check is paired with an accuracy check | G7, G5 | K23 (single-source, small models) | Select by coherence only vs coherence plus accuracy on held-out items | Coherence-only selection scores lower on accuracy by at least 2 points | Low |

## Open questions we cannot test on our bench yet
- Whether the 2026 preprints (Andrews and Sarkar, Kotawala, Dragonevskiy, Filbry et al., Williamson et al.) replicate. Needs independent runs on other models and domains.
- The original accuracy-dominance proofs (Joyce 1998, Leitgeb and Pettigrew 2010) and the Hajek and Christensen primaries were not opened. Needs reading; no bench test.
- Whether diachronic Dutch books predict LLM update failures better than one-shot identities. Needs a shared item set with both a diachronic book and one-shot checks; not built.
- The human unpacking effect in LLMs (support theory) was not tested directly. Needs packed and unpacked partitions with known residual.
- Predd et al. coherence weighting (+30%) was not opened. Needs the originals.
- Token-probability tests need open-weight or logprob access. API-only arms can only use verbal probabilities.

## Order to run
1. D02.02-U1: decides whether the whole-partition rule is worth enforcing, and no direct study exists.
2. D02.02-U2: if the raw sum predicts error, it gives a free G1 trigger at no extra tokens.
3. D02.02-U4: order averaging has established bias evidence and is cheap to check at equal tokens.
