# E14.01 Recombinant search: cross-check critique

## Re-opened this session (numbers confirmed against full text)
- Liu et al. 2026 (arXiv 2603.19087v3): 2.93 / 2.57 human originality, 3.83 / 3.76 o3 and Claude-Sonnet-4, beta 0.36, interaction 0.48, top-10% human tail (0.02 originality, 0.26 feasibility, 0.60 investment, 0.81 utility), top-10% distance effect 0.24 (p=.024). Confirmed.
- Si, Hashimoto, Yang 2025 (arXiv 2506.20803): human gap -0.010 / +0.078 / -0.052, AI gap -1.049 / -1.760 / -1.879 on a 1-10 scale. Confirmed.
- Tang and Yang 2026 (arXiv 2605.27905v2): 219,655 ideas, exploration distance 0.322 vs 0.410, breadth 0.554 vs 0.599, pooled gap -0.045. Confirmed.
- Ke, Teng, Min (arXiv 2107.09176v2): 12.5% of patents cite science, +49% citations, +117% odds top-5%, +171% top-1% (and 96% top-10%). Confirmed.
- HINDSIGHT (arXiv 2603.15164v2): 7.44 vs 7.40 (p=.584), 0.297 vs 0.119 (p<.001), correlation -0.29. Confirmed. The "2.5x" is the ratio 0.297/0.119, not a stated figure.
- Wang, Veugelers, Stephan 2017 (NBER w22180): 773,311 articles, 674,546 with 2+ references, 1,056,936 observations, +12.04% mean, +14.90% dispersion, +16.80% / +16.76% for top and bottom 10%, +39.82% / +11.22% top-1% odds. Confirmed.
- Internal arithmetic check of Fleming: e^(0.3958 x 2.28) = 2.47 gives +147% (matches); +332% at 11.25 implies coefficient about 0.13 and SD about 0.75, consistent with +10.3% per SD.

## Corrections and reconciliations
1. Wang sample size: a09 gives 773,311 / 674,546 and b06 gives 1,056,936. Both are right. The larger count is field-article observations after papers in several subject categories are counted once per category. Use 1,056,936 for model counts.
2. Uzzi team tail-novelty shares differ by 0.1 point between a08 (36.1 / 39.8) and b05 (36.2 / 39.9). Source is paywalled and was not re-opened. Quote as "about 36% solo, about 40% pairs, 49.7% three or more".
3. Lee, Walsh, Wang: a14 says 8,864 sampled, b09 says 9,428 sampled (2,327 full replies in both). Not resolved.
4. Kaplan and Vakili: 2,826 (abstract) vs 2,384 (later review). Not resolved; both abstract-level.
5. Verhoeven: a13 says about 260,000 families (7%) make a new combination; b18 says about 25% score on at least one of three indicators. Different denominators and indicators; not a contradiction but do not mix them.
6. Li, Lin, Wu: 19M (abstract) vs 18,931,951 papers 1900-2010 (figure); 41M vs 40,935,251. Rounding only. a16 has no URL recorded.
7. c01 is a wiki summary, not Fleming's coefficients; use a01-a05 and b01-b03 for numbers. b03 itself warns the table layout was garbled, so no coefficient other than those cross-checked by arithmetic should be quoted.

## Contradictions between sources
- Fleming says new combinations lower the MEAN. Wang 2017, Foster 2015 and Uzzi all find higher or equal mean for novel work (with long windows). The mean half of the founding claim is the weakest. Status: contested (K05).
- Fleming's hypothesis 2 (familiar components cut variance) is not supported even inside his own paper (U-shape, 9.6% max cut). Later summaries that state the claim cleanly overstate it.
- Li, Lin, Wu (atypical goes with lower disruption) vs Uzzi (tail novelty adds hits). Likely different outcomes (disruption vs top-5% citations), and the D index is contested. Not resolved.
- Si 2024 (AI ideas more novel, same feasibility) vs Si 2025 (after execution AI ideas fall 1-2 points) vs HINDSIGHT (LLM novelty rating negatively related to real impact). The first is the outlier; later work says the novelty rating is not trustworthy.
- Liu 2026: LLMs do not show the human usefulness cost of far ideas. Tang and Liu-Butler: LLM agents stay close to seeds. Two readings: LLM far ideas are safer because less extreme (selection of the tail), or LLM ideas are not really far in direction.

## Weak spots
- The strongest "founding" numbers (Fleming, Uzzi, Foster) were read by the earlier agents, but could not be re-opened here (paywalled; Semantic Scholar rate-limited, OpenAlex lookup failed). They are internally consistent, not independently re-verified.
- Every empirical test of the Fleming mean/variance pattern uses citations as "usefulness". No study here measures usefulness of a recombination by an outcome other than later citation or rater score.
- LLM studies mostly use LLM judges (Shen, Graph2Idea, U2F, Liu-Butler novelty metric). Human validation is moderate (agreement 75.7% to 88.6% for the judge, kappa 0.445 for human novelty).
- No LLM study tests the reuse half (refinement helps, over-reuse hurts) with measured numbers, except indirectly through iteration (Chen and Zhang; SciMON).
- Nothing tests O7-like blending at equal tokens against a plain best-of-N baseline.

## Seen only in snippets or abstracts
a22 Fleming-Sorenson 2001, a23 Fleming-Sorenson 2004, a24 Katila-Ahuja, a25 and b22 Kaplan-Vakili, a26 and b23 Singh-Fleming, a27 Levinthal, a28 Arthur-Polak (secondary), a29 Fleming 2007, b24 Kneeland et al., b25 Schilling-Green, c19 Liu-Butler refinement figures, c29 Peeperkorn (second-hand). Do not cite numbers from these.

## GAPS (most decision-relevant first)
1. At equal tokens, does an explicit recombination step (rank part pairs by familiarity, take mostly near pairs plus one far part) beat plain best-of-N on a verified-outcome benchmark? No study found runs this comparison.
2. What is the best number of refinement rounds before lock-in for an LLM blend? Chen and Zhang suggest about 2, SciMON shows gains in iterations 1-2; is this stable across tasks and models?
3. Is the Fleming mean penalty for novel pairs present in LLM output at all, measured with an outcome check rather than an LLM judge? Liu 2026 shows no cost for LLMs; HINDSIGHT shows judges are unreliable.
4. How should analogue distance be measured for an LLM agent so that it predicts usefulness? Embedding distance, Uzzi z-score, facet labels (kappa 0.53-0.61) and ONS direction all disagree; no head-to-head comparison.
5. What share of budget should go to far moves? Foster's data (about 14% new moves, reward below risk) and Uzzi's tail suggest a small share, but there is no experiment on an agent.
6. Is there a distance threshold below which cross-domain prompting adds nothing (Liu: only the top 50% most distant pairs showed a gain for the best models)? Does it hold in other tasks and for open-weight models?
7. Does over-reuse of the same pair hurt an agent within a run (Fleming's exhaustion claim) or only across a population? Needs a within-run repeat-pair experiment, ideally with a cap or penalty.
8. Do multiple independent agents (collaboration effect: cut poor tail, lift good tail) reproduce Singh and Fleming 2010 at equal tokens? Full text of that paper is also still unread.
9. Can the paywalled founding numbers (Fleming 2001 tables, Uzzi 2013 supplement, Foster 2015) be re-opened and the 0.1-point team-share discrepancy settled?
10. Which later work replicated Fleming's patent result with a different dataset or period (Fleming-Sorenson 2001, Katila-Ahuja, Kaplan-Vakili full texts)? Only Verhoeven 2016 was read in full as a patent-side extension.

## Gap search results

Search status: WebSearch hit its session budget, and the arXiv, Semantic Scholar and OpenAlex search APIs returned rate-limit errors, so no new papers could be searched. Work used full texts already extracted and re-read in this pass. Evidence is in evidence_d.jsonl (d01 to d19). Claims K26 to K31 are new; K02, K03, K05, K09, K12, K13, K16, K21 were updated.

Closed or mostly closed:
- Gap 9 (paywalled numbers). Fleming 2001 is freely available from the Berkeley Fung Institute copy, and its numbers match the claims (d01). Uzzi 2013: the printed shares are 36.2, 39.9 and 49.7 percent; the 36.1 and 39.8 in evidence a08 were slips (d03). Foster 2015 manuscript text confirmed (d04). Only the Uzzi supplement is unopened.
- Gap 10 (replication). Verhoeven 2016 is a same-model replication on PATSTAT families (N = 2.3 to 3.6 million). After controls, new recombination lowers the mean (-0.0957, about -9.1%) and raises spread (+0.0942). Raw means go the other way (d05, d06). Evidence b19 was wrong that the mean was not tested. Fleming-Sorenson, Katila-Ahuja and Kaplan-Vakili are still unread (d19).
- Gap 6 (distance threshold), partly. In Liu 2026, pooled LLMs gain nothing from a far source once the nearest 20% of pairs are dropped; the best two models gain only in the far 50% (d15). One task, no per-open-weight result.
- Gap 2 (rounds), partly. Nova shows gains in rounds 1 to 3 and a stop after round 3, and no growth at all without new retrieved input (d12). With SciMON and Chen-Zhang the pattern is 2 to 3 rounds. All three use LLM or embedding novelty, not an outcome check. Stability across tasks and models is not tested.

Moved but still open:
- Gap 3 (mean penalty in LLM output with an outcome check). No new outcome-checked study. Human patent evidence now says the penalty is real after controls and hidden in raw means, so any agent test must control length and tokens (d06). LLM research ideas already lean on bridge and synthesis framing (d17).
- Gap 4 (measuring distance). Embedding-distance originality predicts other facets across 35 models (r up to 0.73; valid blends 0.48), but only at model level (d16). Hope 2017 shows a purpose-near, mechanism-far split beats surface-near retrieval for humans (d11). No head-to-head of measures against usefulness.
- Gap 5 (share of far moves). Humans repeat 85.8%, move 14.2% (d04). A greedy search with a small random acceptance beat pure greedy by about 7 points of hit rate (d13), but the probability is not given and compute is not matched. No agent sweep.
- Gap 8 (independent agents). Singh-Fleming full text is still unread (d08). New: different models and repeated samples are highly similar (d09), and in people, more members give more hits but less disruption (d07). So independence has to come from different inputs. No equal-token test.

Still fully open:
- Gap 1 (explicit recombination vs best-of-N at equal tokens). The closest study, Cooking Up Creativity, keeps the top 5 of up to 5,600 candidates against 5 single-session recipes (d14). Not equal tokens, no best-of-N arm, no verified outcome.
- Gap 7 (within-run over-reuse). Nothing found.

Open data discrepancies: Lee et al. 8,864 vs 9,428 papers and Kaplan-Vakili 2,826 vs 2,384 patents are unchanged.
