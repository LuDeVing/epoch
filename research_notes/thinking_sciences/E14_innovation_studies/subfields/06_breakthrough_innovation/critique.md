# Critique: E14.06 Breakthrough innovation (cross-check)

## Numbers re-opened from source PDFs (this session)
Confirmed with no change:
1. Kaplan and Vakili Table 1: topic-originating patents mean 5-yr citations 22.17 vs 12.77 others (all patents 13.507); only 20 of 189 in the top 5%; 1.89 per topic; probability 0.072 vs 0.024 (a06, b02).
2. K&V Table 2 (N=2,276): direct distance 0.211 (SE 0.093), diversity 0.065 (0.101); topic-originating -> citations 0.330 (0.094); odds 1.7 (coef 0.538); exp(0.330) = 1.39 (the "1.4x").
3. **Resolved a07 doubt.** The row assignment of path A is: distance -0.391 (SE 0.184), indirect -0.129 (0.073), total 0.082 (0.119); diversity -0.486 (0.167), indirect -0.158 (0.067), total -0.093 (0.118). The sums check (0.211-0.129 = 0.082; 0.065-0.158 = -0.093). So a07's likely assignment is right. The indirect effect for distance carries one star while its SE is 0.073 (z about 1.8): treat it as marginal.
4. Uzzi et al. 2013: 9.11 / 5.82 / 5.33 / 2.05 per 100; 37.7%; 36.1/39.8/49.7 in text, 36.2/39.9 in legend (a10 already notes it).
5. Si et al. 2024: novelty 4.84 / 5.64 / 5.81, SD 1.76 and 1.66, 109 reviews per AI arm, reviewer agreement 56.1%.
6. Si et al. 2025: ideation 4.912 vs 5.778 (FDR p=0.035); post-execution novelty p=0.586; AI gaps -1.049, -1.760, -1.879, -1.976.
7. Holst et al.: 972,161 extra papers; 97% (SciSciNet) and 78% (PatentsView) with zero references; 93% of papers and 98% of patents do have references in source files.
8. Gupta and Pruthi: 24.0% verified plagiarism (36.0% with unverified); 13 experts; cluster spread 0.81; classifier 93.9%. Note: the paper's text says "12 NLP topics"; a22 says 50 documents; consistent with c07.
9. Lin et al.: 28% -> 22% (papers, n=14,485,326) and 67% -> 55% (patents, n=3,411,366) with distance.
10. Kelly et al.: median to 90th percentile = +0.7 (5 yr) and +1.5 (10 yr) citations on medians 2 and 3. Gu and Krenn 2024 idea study: 4,451 ideas rated, mean 2.40, 24.9% rated 4-5, AUCs 63.20 / 67.44 / 60.39.

## Corrections
- c10 says "100+ leaders". The paper counts 110 participants (title says 100). Not a numerical change, but use 110.
- c11 / claim K13: "1.94" is reported by the paper as "weak statistical evidence (1.94)"; the unit (sigma) is inferred. Keep it as "weak".
- Gu and Krenn paper is arXiv v4 dated 24 Sep 2026 in this read; earlier lines (a26, b12) are the forecasting paper (2402.08640), a different paper. Do not merge them: forecasting AUC above 0.9 (predicts citations of pairs) vs idea study AUC about 0.63-0.67 (predicts expert interest).
- a07: remove the "row order uncertain" flag (resolved above).

## Contradictions and tensions between sources
- Wide recombination: K&V find no total effect on citations; Uzzi finds atypical tail combos help when paired with a conventional core. These do not conflict directly (different units: patent classes vs journal pairs; different hit definitions) but nobody has tested both in one dataset.
- Gu and Krenn: network features predict citations of concept pairs (AUC above 0.9) yet experts find ideas from those pairs no more interesting (2.350 vs 2.446 random). Impact-by-citation and interest diverge.
- LLM-idea novelty: Si 2024 says LLM ideas are more novel; SciMON says ideas are less technical and original beats the machine in 85%; Si 2025 says the advantage vanishes after execution. Novelty is judged at the idea stage by raters with 56% agreement.
- Doshi and Hauser: more individual novelty, less collective novelty. Both facts hold; the net effect on "rare high impact" is unknown.
- Disruption index: Park et al. decline vs Holst et al. artefact. Original authors' reply not found.

## Weak spots
- K&V is one domain (fullerene patents), citations as value, LDA with expert-tuned thresholds. No replication found in other fields in this run.
- Most LLM evidence rests on one research group (Si, Yang, Hashimoto). Claims K05, K06 are single-source for that reason, even though evidence lines are many (a19, b13, c01, c02, b23 are one study).
- Claim counts "independent_sources" count independent studies, not evidence lines.
- LLM-judge reliance: Nova, ResearchAgent, AI Idea Bench results use LLM judges which Si show are near chance.
- Models are mid-2024 to early-2025. No reasoning-model or 2026 test of idea quality found.
- "Breakthrough" is operationalised as top-5% or top-10% citation; no study here measures real-world value of an LLM-generated idea.

## Seen only in snippets or abstracts
a11 (Wu et al.), a12 (Park et al.), a14 (Lin et al. Nature abstract), c21/c22 (Artificial Hivemind abstract), c23, c24, c25, c26 (abstracts only), c27 (garbled tables). a15-a18 and b29, b30 not opened (from memory or second-hand). c28 (Kaplan and Vakili publisher page) not opened, but the author-hosted PDF was (a01-a08, b01 and others). b08-b10 are second-hand via the Leibel and Bornmann review.

## GAPS
1. Does any LLM or agent study measure breakthrough-like impact (not rated novelty) for generated ideas after execution, in a field other than NLP, and with newer (2025-2026) models?
2. Does the K&V finding (deep local search yields new topics; distant recombination does not) replicate outside fullerene patents, or in non-patent data such as papers or code?
3. Does a conventional-core-plus-atypical-seed prompt (the Uzzi pattern) raise value or novelty of LLM ideas at equal tokens versus all-atypical or all-conventional seeding?
4. What is the best cheap selector for rare high-impact ideas: pairwise tournaments, retrieval-grounded prior-art checks, or text-based past-vs-future novelty scores (Kelly style)? Any measured comparison on LLM ideas?
5. Does keeping a reserve of low-rated atypical candidates through selection recover tail wins, and at what token cost?
6. How do the original authors respond to Holst et al. (Matters Arising listed on Park et al. page), and which disruption variant (DI5, DI3%) is robust enough to use as a label?
7. Do reasoning models or tree-search agents reduce the diversity wall (4,000 to 200 unique ideas) at equal tokens, and does prompting for diversity change execution outcomes?
8. Is there a sampled-persona or role-mix result for a single LLM that reproduces the team effect on atypical combinations (Uzzi 37.7%)?
9. Does the Gupta and Pruthi plagiarism rate fall when generation is retrieval-grounded with a prior-art filter, and does novelty then survive execution?
10. Are there tests of the tension vs foundational orderings (deep first, then far, or the reverse) in human creativity experiments that could set the order of operators in the schema?

## Gap search results
Evidence is in evidence_d.jsonl (d01-d17); claims K19-K26 added, K02/K03/K06/K07/K08/K10/K14/K17/K18 got extra evidence ids. Budget: 8 WebSearch calls plus page fetches; Semantic Scholar was rate-limited and the arXiv API returned empty, so sources came from search results and direct page or PDF reads. Lines with opened:false (d02, d07, d08, d12, d15, d16, d17) were not read.

1. Execution-grounded impact, other fields, newer models: PARTLY CLOSED, still open for non-NLP. New: execution-grounded search on nanoGPT and GRPO tasks with 2025-26 models (d09), and an autoresearch loop on 40 ideas (d03). Both are ML. No wet-lab, materials or citation-impact test found.
2. K&V replication outside patents: OPEN. No replication found (d07). Nearest cousin: Li, Lin and Wu 2025, atypicality negatively correlated with disruption in 40.9M papers (d06). Note a source-naming mismatch: nanotechnology (search summary) vs fullerene (earlier lines); verify against the PDF.
3. Conventional-core plus atypical seed in LLM prompts: OPEN. Zhang et al. use such pairs but have no seed-mix ablation (d11). Liu et al. show far seeds help only at large distance and cost feasibility (d10).
4. Best cheap selector: OPEN. Only pieces found: facet re-ranked prior-art check (d13), rank-based selection (d16, snippet), Swiss tournaments (a20). No head-to-head against Kelly-style scores.
5. Reserve of low-rated atypical candidates: PARTLY CLOSED. Diversity-aware subset refinement beat ranking-only on proxy ratings (d14, abstract only); evolutionary search with a diversity-preserving sampler kept tail topics (d03, d09). No test of reserve cost vs tail wins.
6. Original authors' reply to Holst et al.: CLOSED for the existence question (Nature 2026 reply; preprint read, d01, d02). Which variant is robust: OPEN. The authors report decline under CYG5, CD5^5, CD5^noK and binary Is-D5 with different sizes (36, 23, 16, about 7.5 points in WoS); critics' view not re-read. Use no variant as a label.
7. Diversity wall with reasoning models or tree search: PARTLY CLOSED. Plan-then-split sampling (d04) and coherence-minus-availability sampling (d03) raise diversity; no reasoning-model comparison at equal tokens, and RL on one reward collapses diversity (d09).
8. Persona or role mix reproducing the team effect: PARTLY CLOSED. Sampled ordinary personas plus CoT reach human-level spread for one model (d05); not tested on atypical combinations or value.
9. Plagiarism rate with retrieval grounding and prior-art filter: OPEN. The prior-art checker (d13) has a small test set and no before-after rate on generation.
10. Order of deep vs far: OPEN. Only a snippet-level hint (Chan and Schunn, d12: effects depend on convergence timing). Not tested.

Cautions: several 2026 results rely on LLM judges or proxies (d03 GPT-5.5 judge agrees 68% with experts vs 58% between experts); d04, d05 are creative-writing or product tasks, not research ideas; d11 shows rating targets drift.
