# Critique: NDM in sport (E04.08), cross-check

## Re-opened this session (confirmed)
- Bossard et al. 2022 (Frontiers, full text): 60-81% simple match, 13-28% diagnosis, 3-24% evaluation, quoted from Macquet (2020). Confirmed. The 80% first-option figure is confirmed as text, but the article ties it to "empirical research on IDM" (option generation), not to RPD. Correction: 80% is not an RPD match rate; a04, b01 and c01 blur this.
- SportQA (arXiv 2402.15862, PDF): 70,592 items; levels 21,385 / 45,685 / 3,522; GPT-4 5S CoT 85.63 / 78.82 / 73.58 / 64.08 / 34.40 / 23.01; humans 96.63 / 96.02 / 94.90 / 91.84 (the last is the next human column, not recorded in c03). Confirmed.
- SPORTU (arXiv 2410.08474 v4, PDF): GPT-4o 71% best text; Qwen2-VL-72B 70.94% overall, 44.12% hard; Claude-3.5-Sonnet 52.57% hard, 39.32% rationale-first; camera-angle 52.86/18.59/28.55. Confirmed.

## Not re-opened (rate limits, paywalls)
- Kopka and Feufel 2026 (JMIR, doi 10.2196/88053): page fetch returned nothing. The 63.3 / 67.6 / 29.8 figures rest on the earlier agent's read only.
- Le Menn 2019 (83 accounts, 46/34/20), Collins 2016 (30%), Roca 2018 d values, Kermarrec and Bossard 2014, Hinz 2022, Ma 2024: not re-opened. That is 5 of the 10 top numbers unconfirmed.
- Macquet 2020, Johnson and Raab 2003, Klatt 2019, Musculus 2019, North 2011: never opened by anyone; abstract or second-hand only.
- arXiv and Semantic Scholar APIs rate-limited during this check.

## Corrections and inconsistencies
- Kermarrec and Bossard 2014 percentages (60/23/16) sum to 99. In that study simulation (23%) outranks diagnosis (16%), as in Le Menn (34 vs 20), but both are second-hand.
- a15 says these rates "(80+ percent) differ from the 60-81% range"; the quoted 60% is inside the range, so that note is wrong.
- b04 reports 41 vs 53 studies and 13 vs 7 added in Ashford 2021; the review's own counts disagree.
- Roca 2018 appears three times (a11, a12, b19) and counts as one source. d=5.36 for overall creativity comes from an extreme-group split (n=11 each) and is inflated.
- a09 time limits (400/200/0 ms) are second-hand.

## Contradictions between sources
- Option count: Klatt (more options, more accuracy) vs Musculus N=169 and Raab and Laborde (less is more) vs Del Missier (fluency does not predict quality). Contested.
- Fixations: fewer in experts (Lex) vs more (Roca, full scenes).
- CoT: helps GPT-4o on Sports Intelligence L1 (81.70 to 85.35) but hurts Claude 3 Opus (66.67 to 58.73); hurts SPORTU video hard.

## Weak spots
- Nearly all human evidence is small-N interview or video work, retrospective, with soft coding of the RPD level.
- No sport study tests causally whether match-first beats analysis on performance.
- LLM sport evidence is benchmark QA, not decisions in play. Only Kopka and Feufel apply an RPD prompt, and in medicine.
- The search for direct LLM-RPD sport studies was thin (a25, c26 found 0), so absence is weak evidence.
- Only snippets/abstracts: b09 to b13, b17, b26, b27, c20 to c25.

## GAPS
1. Does an RPD-structured prompt (recall similar cases, then simulate) beat a length-matched neutral prompt at equal tokens, and which half does the work? (Kopka had no ablation and has no replication.)
2. What is the primary source and sample of the 80% first-option figure (Johnson and Raab 2003 and replications)?
3. Which studies and Ns sit behind Macquet 2020's 60-81%?
4. Does generating more options help or hurt when expert raters score option quality (reconcile Klatt vs Musculus vs Raab and Laborde)?
5. Is Ivanova et al. 2025 (LLM simulation of RPD dynamics) a real LLM test of RPD, and what does it measure?
6. When does reasoning before answering hurt LLMs on perception-like sport tasks, and does a direct-then-check order recover it?
7. Do similar-case retrieval systems (TacticAI-like) beat no retrieval in a controlled outcome trial?
8. Do LLMs show the expert-novice differences (anticipation, cue use) when given text descriptions of the same plays?
9. Are Kopka and Feufel's gains a threshold shift toward self-care advice rather than better discrimination (the 2 emergency cases cannot show safety)?

## Gap search results (2026-11-19, evidence_d.jsonl d01-d19)
Tools: WebSearch budget was spent; arXiv API, Semantic Scholar and OpenAlex were rate limited. Crossref, Europe PMC, direct arXiv PDFs and the PMC full text of Kopka and Feufel worked.

1. RPD prompt vs length-matched neutral prompt: STAYED OPEN. Full text opened (d01, d04). No length control, no ablation, no replication. Data-frame prompt did about as well as RPD (66.7 vs 67.6), and 8 of 10 models gained. New claim K18 records the needed 4-arm test.
2. Source of the 80% figure: STAYED OPEN, narrowed. Bossard's sentence has no citation (d05). Johnson and Raab 2003 is paywalled and unopened (d11); Raab and Johnson 2007 abstract shows equal option counts, quality differing by expertise (d10).
3. Studies and Ns behind Macquet 60-81%: STAYED OPEN. Only the chapter reference was recovered (CRC Press, pp 135-154, d06). Rugby study (N=16) shows the mix moves with time available (d17).
4. Option count: PARTLY CLOSED. Del Missier 2014: more options raise best-of-set quality but lower the set mean (d07). Klatt 2019 is a correlation across players (d08). Raab and Laborde N=54 favours intuition in experts (d09). The conflict is mostly about what is scored. New claim K20. Musculus N=169 not re-opened.
5. Ivanova 2025: PARTLY CLOSED. It is a Routledge book chapter on financial markets, not sport (d12); content unopened, so it cannot be cited as a measured RPD test. A look-alike 2026 geopolitical paper does not mention RPD (d18).
6. Reasoning-first hurting: PARTLY CLOSED. Mind Your Step (arXiv 2410.21333) shows CoT drops on implicit and non-verbal tasks, e.g. face recognition GPT-4o 64.0 to 51.2 and exception learning 2.9 to 12.5 rounds (d13, d14); smallest for Claude 3.5 Sonnet. Direct-then-check recovery is untested anywhere found. New claim K19.
7. Retrieval vs no retrieval outcome trial: STAYED OPEN. TacticAI retrieval recall 0.63 vs 0.33 against a feature baseline, expert opinion only, five raters (d15).
8. LLMs on expert-novice text plays: STAYED OPEN. Nothing found; searches were limited (d19).
9. Kopka threshold shift: CLOSED in the main (d02, d03). Gain is in the 13 self-care cases (13.4 to 29.8%), nonemergency flat near 82%, 88% of errors over-triage, 2 emergency cases cannot show safety. Discrimination was not measured. New claim K17.

Also: a 2026 meta-analysis (26 studies, N=611) found fewer fixations in experts, SMD -1.52 (d16); K05 updated to task dependence. Earlier note 2 correction stands: 80% is not an RPD rate.
claims.jsonl now has 20 claims (K03 kept single-source, K04 contested, K08 rewritten; K17 to K20 added).
