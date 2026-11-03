# Critique and cross-check: Retrieval failure view of amnesia (A06.08)

## Corrections made (sources re-opened this session)
1. Hardwicke 2016 (PNAS): confirmed 4 direct replications n=64 and 3 conceptual n=48. The abstract adds that retrieval aided preservation of sequence knowledge in the conceptual studies (not recorded before).
2. Kredlow 2016: g=0.40, 0.89, 0.21 and 63 comparisons confirmed.
3. Pigeon 2022: g=-0.51 and -0.42 confirmed. CORRECTION: the abstract gives n=478 (14 healthy studies) and n=446 (12 clinical studies). Line b07 says "618 propranolol vs 527 placebo"; that does not match and is unverified. Use the abstract numbers. The abstract concludes "robust, well-replicated", the opposite of Steenen 2022.
4. Lucki 2025: 52.7/57.0/61.6 after 10 retain samples, RMU orthogonalization 64.7 vs 64.4 baseline, prefixes 53.9/46.0/49.0 from 29.9/29.5/27.9 confirmed in full text. Ablation NPO 45%, DPO 51% also confirmed.
5. Zheng 2025: 100% to ~10% in 150 steps, recovery ~100% falling to 96%, safety 100% to 0% to ~99% confirmed. Nuance: the recovery probe fine-tunes on half of Task 0, so it shows savings from retraining, not pure cue access. The paper says irrelevant tasks also restored old performance; only the ten-instance safety case was checked in detail.
6. Berglund 2023: GPT-4 79% vs 33% confirmed.
7. Deeb and Roger 2025: abstract confirms 88% recovery for pretraining-era facts and warns that tests on fine-tuned-in facts overstate robustness. Matches b13.
8. Hu 2025, Wang and Sun 2025, Liu 2024: abstract claims confirmed; exact figures (70%, 35 variants, 56.1%) not re-opened.
Not re-opened: Ryan 2015 and Roy 2017 p-values, Gisquet-Verrier F values, Sarma 2026, Gekhman, Orgad, Park, MemGPT, A-MEM.

## Contradictions
- Propranolol: Pigeon (robust) vs Steenen (no significant benefit after restriction). Unsettled.
- Human reconsolidation: Hardwicke and a healthy N=44 replication fail; Pigeon says robust. Weakness of this rival does not prove retrieval failure.
- Spurious forgetting: replay of 20% old data barely helps, yet retraining on half of Task 0 restores ~100%.

## Weak spots
- The core source (Alfei 2025) is a review by advocates. The published full text was not obtained (b25); the preprint was read. No pooled effects, no tally of failed reversals.
- Many numbers inside the review are second-hand rat studies without n.
- Rodent engram rescue: n of 4 to 12, protocol-sensitive (CA1 needed 4 Hz, not 20 Hz). Light is an artificial cue, not natural recovery.
- LLM evidence is analogy. Unlearning recovery uses weight updates (retraining), not cue-only recovery.
- Fine-tuned-in knowledge recovers less than pretrained knowledge for some unlearning methods.

## Seen only in snippets or abstracts
Tulving 1966 and 1973, Miller and Springer 1973/1974, Stout and Miller 2007, the 2023 reconsolidation critique, Schiller verification report, Warrington and Weiskrantz 1970 (abstract only).

## GAPS
1. Does any LLM study test pure cue-based recovery without weight updates (context reinstatement of encoding framing) for buried facts?
2. In the Psychological Review paper, how many reversal attempts failed vs succeeded, and under which conditions (time, reminder, US reinstatement)?
3. At equal tokens, does re-querying a memory store with paraphrased and reverse-direction cues beat a single query on agent tasks?
4. Does overwriting stale notes beat append-only memory against proactive interference at equal tokens (Wang and Sun load curve)?
5. Do internal-score re-ranking methods (Gekhman, Orgad) beat majority vote at equal tokens, and do they transfer across datasets?
6. Which human cue-induced amnesia result besides Walker works, and with what effect size?
7. What is the Steenen restricted pooled effect for propranolol, with CI?
8. Does state or context matching (same framing at write and read) improve agent memory benchmarks such as LoCoMo, with measured margins?
9. How many independent labs replicated Ryan 2015 engram rescue?
10. Can an agent detect a stored-but-inaccessible item cheaply (feeling-of-knowing analogue)?

## Gap search results
Tools note: arXiv, Semantic Scholar and OpenAlex APIs returned HTTP 429, and WebSearch was out of budget, so papers were opened by direct page fetch (several via a fetch summarizer; marked in limits) and Europe PMC. Evidence is in evidence_d.jsonl (d01-d20).

1. Pure cue-based recovery in LLMs: PARTLY CLOSED. Prompt-only recovery exists: enhanced GCG prefix lifts WMDP-Bio 29.9/29.5/27.9 to 53.9/46.0/49.0 (base 64.4); in-context relearning raises Harry Potter familiarity modestly (d10, d11). No study restores encoding framing. Still open: a natural reinstatement test.
2. Reversal tally in the Psychological Review paper: CLOSED as unanswerable from the source. The preprint has no tally; Table 1 is selective, X means untested, and it admits no recovery by reinstatement or state for proactive/retroactive outcome interference (d01, d02). Full published text still not obtained.
3. Multi-query vs single query at equal tokens: OPEN. Only single-rewrite gains found (Ma 2023, 0 to 3 points; LongMemEval time-aware expansion helps only with a strong rewriter) (d13, d14).
4. Overwrite vs append: OPEN. Wang and Sun test forget instructions (under 10 points) and a mock QA reset, never deletion (d16).
5. Internal-score re-ranking vs majority vote: PARTLY CLOSED. Gekhman: probe 23.7 vs majority 22.0 at 1000 samples; Orgad: no transfer after a logit baseline. Equal-token comparison not done (d17, d18).
6. Human cue-induced amnesia besides Walker: PARTLY CLOSED. Hupbach 2007 shows intrusion (U=20, p<0.01, groups of 12), not erasure; Kindt 2009 propranolol has no effect size in the abstract; the review lists about 8 failed replications (d03, d07, d08, d20).
7. Steenen restricted pooled effect: OPEN. Reported only in forest plots; text says only not significant and a wider interval (d09).
8. State/context matching on LoCoMo: OPEN. Mem0 compares stores, not matching; LongMemEval key expansion is the nearest cue-design evidence (+9.4% recall, +5.4% QA) (d12, d15).
9. Independent labs replicating Ryan 2015: PARTLY CLOSED. The review's optogenetic column cites 16 studies from at least four groups, several of Ryan or Tonegawa lineage; Guskjolen 2018 (infant memory) supports; Abdou 2018 failed after complete amnesia. Strict replication count unknown (d04-d06).
10. Cheap feeling-of-knowing for agents: PARTLY CLOSED. P(IK) works with a trained head (AUROC 0.864 in distribution, 0.606 to 0.687 out of distribution); no training-free proxy tested (d19, d18).

Claims changed: K02 (dissent added), K19 (narrowed), K12/K15/K17/K18 (evidence added); new K21-K27.
