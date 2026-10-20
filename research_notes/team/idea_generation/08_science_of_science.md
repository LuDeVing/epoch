# 08. Science of science and innovation economics: where impactful new ideas come from

Prepared 2026-10-13. Evidence labels: **H** large-N and independently replicated; **M** peer-reviewed, one large study or a documented validity problem; **L** small experiment, simulation, preprint or abstract-only check; "(contested)" marks a live dispute; "(inference)" marks my reasoning. Source pages opened in full or in large part for [3][4][6][8][13][14][15][16][21][34][35][41] (read directly as extracted text for [4][13][41], otherwise via the fetch tool's page summary); the rest were checked from abstracts or landing pages. The WebSearch quota ran out mid-task, so later sources were opened by direct URL.

## Bottom line

1. Recombination is the engine, but Weitzman puts the limit in processing candidate ideas into usable form, not in generating them [1]. For a pipeline whose exam costs minutes to hours per candidate, atypicality is a triage prior for scarce test slots, not a generator (inference).
2. The best-cited papers pair a conventional core with a few atypical links: 9.11 vs 5 hits per 100 [4]. H as an association, M as a measure of novelty [9][10].
3. Novel work has a lower mean, higher variance and delayed credit [5][29][31]. Judge exploratory arms by upper quantiles and re-test near-misses.
4. Small, fresh, independent teams and distant outsiders help modestly [21][23][26][6]; the disruption literature is disputed (contested) [14]-[18].
5. LLM ideas beat human ideas on novelty before execution and fall further after it [34][35]; LLM novelty judges are unreliable [34][47]; model samples are homogeneous [34][43]. I found no study applying Uzzi-style scores to LLM ideas.

## 1. Evidence

**Recombination.** Weitzman: new ideas are recombinations; the limit is processing a large supply of candidate ideas into usable form [1] (theory, L). Jones: combinatorial growth in draws from thin-tailed distributions gives exponential growth [2] (theory). US patents 1790-2010: about 60% of new patents add a new code combination and 40% refine one, a stable ratio, while new building blocks slowed [3] (M; coarse codes). Research effort rises while productivity falls; Moore's law needs more than 18x the researchers of the early 1970s [20] (M). Jones's burden-of-knowledge model predicts more schooling, specialisation and teamwork, tested on inventor data [19] (M).

**Atypical combinations.** Uzzi et al. scored 17.9M Web of Science papers by journal-pair co-citation against randomised citation networks (median z = conventionality, 10th-percentile z = tail novelty). Top-5% cited within 8 years: 9.11 per 100 for high-median plus high-tail, 5.82 conventional only, 5.33 novel only, 2.05 neither; only 6.7% of papers sit in the best cell; impact peaks at the 85th-95th percentile of conventionality; 49.7% of papers with 3+ authors show tail novelty vs 36.1% of solo papers [4] (H as association). The method extends to "topics within papers" [4]. Follow-ups: first-ever journal pairs predict long-run top-1% status but with higher variance, delay and lower-impact journals [5] (M); a keyword/journal hypergraph gives about 5x hit odds for the most surprising combinations (19.9M MEDLINE papers) and 3.5x for outsiders' "expeditions" into distant fields, but 2x and no expedition effect in patents [6] (M); across 49 journals (27,323 manuscripts) top-quintile novelty had about 6 points higher acceptance and no robust citation penalty, with rejected papers partly missing [8] (M); atypical papers are about 2x as likely to disrupt, though disruption takes 10+ years to settle [7] (L).

**Critiques of the novelty measures.** Only published work is observed, so failed combinations are invisible [6]; the Uzzi score overlaps with interdisciplinarity and first-appearance scores cannot separate novel from non-novel APS articles [9], yet the Uzzi-derived score tracks expert "new finding" tags (+7.47% per SD) while the first-appearance score validates more weakly [10]; journals are crude proxies for ideas [4]; a 41M-paper study finds atypicality and disruption negatively correlated, contradicting [7] (contested) [11]; novelty and quality are entangled in reviewer ratings [46]; temporal novelty predicts citations and spatial novelty disruption [33] (L).

**Disruption (CD index).** Each later work citing the focal item scores +1 if it cites the item but none of its references, -1 if it cites both; range -1 to 1 [13]; r = 0.03 with raw impact in patents [13]. CD5 fell across 45M papers and 3.9M patents, with narrowing use of prior knowledge [14]; new methods disrupt more, new theories less [12] (M). Disputed (contested): in SciSciNet 8.86M of 39.9M papers have CD5 = 1, about 97% with zero references; dropping them cuts the measured decline by 97% (-0.31 to -0.01), dropping all zero-reference works by 87% [15]. The authors reply that the critics' data hold about 3x more zero-reference works (about 20% non-research items) and four other measures still decline (p<0.001) [16]. Also: growing reference lists push CD toward 0 and rising self-citation confounds it [17]; the index measures displacement of a paper's most-cited reference, not absolute innovation [18].

**Teams and independence.** Across 65M papers, patents and software (1954-2014), smaller teams disrupt and larger ones develop; small teams cite older, less popular work; most of the effect is within individuals moving between team sizes [21] (M). A re-analysis calls the overall effect "remarkably small", turning positive at 8+ authors [17] (contested). In 500k+ patents, collaboration cuts the poor-outcome tail and raises breakthrough odds; lone inventors do worse on both [22] (M). Fresh teams are more original [23]; remote teams less disruptive (percentile 89 to 84 for papers) [24]; "knowledge independence" mediates small-team disruption [25] (L). Teams add tail novelty without lowering median conventionality [4] and small teams disrupt [21]; moderate size reconciles them (inference).

**Outsiders and distance.** In 166 contests (over 12,000 solvers), win odds rose with distance between solver field and problem field [26] (M). After 452 star scientists died early, collaborators' output fell about 40% and non-collaborators' rose about 8%, mostly via outsiders with highly cited work [27] (M). Distance has a cost: distant recombination hurts when local search is needed to spot anomalies [30] (M).

**Failure and hotspots.** New components or combinations lower average usefulness and raise variance, giving both failures and breakthroughs [29]; novelty raises variance and positive outliers, most when recombination meets new knowledge origins [31]; "important" patents are distinct from prior and similar to later patents [32] (M). Risky research pays more in expectation but not enough to offset its risk, so work stays conservative [28] (M). I found no verified study of crowded "hotspots" as such. Closest: AI-augmented papers bring 3.02x papers and 4.84x citations but 4.63% less topic breadth and 22% less engagement, drifting to data-rich areas (41.3M papers, classifier-detected, observational) [42] (M); a model tuned away from the crowd of expected predictions surfaces hypotheses humans are unlikely to reach soon [40] (L).

## 2. 2024-2026: these measures and LLM ideas

- Si et al. (49 writers, 79 reviewers, 298 reviews): LLM ideas more novel (5.64 vs 4.84, p<0.01), feasibility n.s.; about 5% of 4,000 generated ideas non-duplicate (cosine above 0.8); best LLM judge 53.3% pairwise agreement vs 56.1% between humans [34] (M).
- Execution follow-up (19 human, 24 LLM projects): LLM overall 5.38 to 3.41, novelty 5.78 to 4.73; human 4.60 to 3.97 and 4.91 to 4.90; drop gaps p<=0.025; ideation scores weakly predicted execution, and for LLM ideas ideation-stage excitement correlated -0.32 with it [35] (M; n=43, NLP prompting ideas).
- 24% of 50 LLM research documents were paraphrases or heavy borrowings per 13 experts; plagiarism detectors missed them [36] (L).
- Steering by recombination: SciMuse (58M-paper graph, 4,400+ ideas rated by 100+ group leaders, mean 2.40/5; graph-chosen concept pairs did not beat a titles-only baseline, though graph features predicted interest) [37]; Scideator (facet recombination, distance-controlled analogies, novelty checker) [38]; SciMON (iterate against prior work until novel) [39]; VIRSCI applies team science, with embedding-based novelty peaking at 8 agents and 5 turns and 50% fresh members best (8B models, proxy metric) [41] (L). None validates against execution.
- Measures: of about ten novelty metrics none passes all axioms, temporal worst, Uzzi-style scores untested [46]; LLM judges collapse to "medium novel" [47].
- Homogeneity: models repeat themselves and each other [43]; larger models are often less diverse and in-context regeneration helps [44]; chain-of-thought prompting raises diversity [45].
- Recipe agents: autoresearch runs five-minute trials, about 12 per hour [51]; search policy times operators matters (medal rate 39.6% to 47.7%) [52]; about 5,000 ideas, 1,100 validated, 20,000+ GPU hours [48]; agents struggle to reimplement known speedrun records even with hints [49]; modded-nanogpt has 92 records, 45 to 0.665 min [50].

## 3. What would transfer to an LLM-driven idea loop

Context: nano/ideate.py sketches, meaning clusters and cluster_score; build; rungs; 3-seed exam (0.005 nats, Welch p<0.01); nano/calibrate.py reports survival per feature bucket. Power (two-proportion test, 80%, alpha 0.05): 40% to 60% needs about 100 builds per arm, 10% to 18% about 300, so begin with rung survival and continuous delta-loss. All effects below are hypotheses (inference).

**M1. Atypicality as a logged feature.** Tag each sketch with up to six technique tags from a controlled vocabulary; count tag pairs over a reference corpus (modded-nanogpt entries [50], LM tech reports, arXiv abstracts, the ledger); z-score against a shuffle that preserves tag frequency and tags per document; log median z and 10th-percentile z [4][6]. The 92 records alone are too few for stable z; use them for a retrospective check of record gain vs atypicality. Expect: Uzzi's 1.8x may be inflated by publication filtering, which the ledger avoids by logging failures; plan on at most 1.2-1.5x, possibly none. Measure: median-z tertile by tail-z<0 buckets in calibrate.py; logistic fit of exam pass.

**M2. Conventional core plus one atypical edge, as a barbell.** Prompt: keep the top-z components, add one link you think is rarely combined, name the pair, and let the scorer verify it. Split slots about 70/30 between core refinements and edge bets and rank arms by upper quantile, since only maxima are promoted [4][29][31]. Expect: fewer failed builds than free-form novelty at a similar upper tail. Measure: rung-3 failure rate, 95th-percentile delta-loss, new records per 100 exams, matched spend.

**M3. Independent generators, fresh small development groups.** Keep contexts isolated with disjoint inputs (code slice, donor brief, prior-art subset); independence must come from inputs, not seeds [34][43]. Run critique with 3-8 agents, about half unseen by the author, at most about 5 turns [41][23]; keep large-team roles (build, check) after selection [21]. Expect: more clusters per token. Measure: duplicate rate, clusters per 100 sketches, rung survival by mode.

**M4. Distance dial for outside inputs.** Sample a donor field per call from near, mid and far bins by embedding distance to "autoregressive LM training"; require MAPPING plus a concrete diff; cap the far bin near one third [26][6][27][30]. Expect: inverted-U pass rate, far bin supplies tail ideas. Measure: pass rate and new-cluster share by bin, quadratic fit.

**M5. Hotspot penalty.** Subtract from cluster_score for density among current sketches, ledger, research-brief "known" items and speedrun entries [42][43][34]; optionally prompt to avoid the expected set [40]. Expect: fewer duplicates; dense regions pass often but add little. Measure: pass rate and promoted-winner share by density decile.

**M6. Replace-vs-refine quota, diagnostic only.** Tag sketches refine or replace (tree.py outward), hold 25-30% replace; log whether later winners build on a promoted component and its predecessors or instead of them [11][12][13]. Muon's arrival at record 3 [50] looks like such a substitution (inference). Expect: guards against pure tuning; low confidence since CD is contested [15]-[18]. Measure: pass rate and delta-loss by class; never a reward.

**M7. Structural novelty plus prior-art gate.** Take novelty from tags and counts, not LLM ratings [47][46]; use embeddings only to catch copies, since they fail claim-level and temporal probes [46]; require a facet retrieve-and-rerank check against the ledger and speedrun log before a sketch counts as new [38][36]; keep ranking on PREDICTION/TEST and exams [35]. Expect: fewer disguised copies (24% in [36]). Measure: monthly audit of 50 "new" labels; share of builds duplicating a ledger entry.

**M8. Compose winners in atypicality order.** With compose.py, splice verified winners from disjoint parts and test pairs by (disjointness, pair z); recombination multiplies options [1][2][3]. Expect: untested; atypical pairs more variable. Measure: stacking ratio delta(A+B)/(delta A + delta B) vs pair z and same-subsystem flag.

**M9. Second look for novel near-misses.** For tail-novel candidates missing the margin by under 1 SD with a closing loss-curve gap, re-run at 2x tokens, pre-declared and labelled exploratory [5][7]. Measure: conversion rate vs conventional near-misses, and cost per conversion. Keep the verdict rule fixed; a 2x re-run is a separate, labelled claim.

## 4. Caveats

Associations are bibliometric and survivor-filtered; citations are noisy outcomes; atypicality proxies (journals, tags) are crude and overlap interdisciplinarity [9]. Team-size and disruption results are disputed [15]-[18]. LLM evidence comes mostly from NLP prompting ideas with small n [35]. Nothing here is validated on training recipes. Several summaries rest on abstracts only (see header). Leads not opened because of publisher blocks or the search quota, and therefore not used: work on canon concentration in large fields, on competition and quality in crowded topics, on novelty penalties in grant review, and on collective diversity under AI assistance.

## Sources

[1] https://ideas.repec.org/a/oup/qjecon/v113y1998i2p331-360..html Weitzman 1998
[2] https://www.nber.org/papers/w28340 Jones, Recipes and growth
[3] https://pmc.ncbi.nlm.nih.gov/articles/PMC4424706/ Youn et al. 2015
[4] https://www.kellogg.northwestern.edu/faculty/uzzi/htm/papers/Science-2013-Uzzi-468-72.pdf Uzzi et al. 2013
[5] https://www.nber.org/papers/w22180 Wang, Veugelers, Stephan
[6] https://www.nature.com/articles/s41467-023-36741-4 Shi and Evans 2023
[7] https://arxiv.org/abs/2103.03398 Lin, Evans, Wu
[8] https://pmc.ncbi.nlm.nih.gov/articles/PMC9704701/ Teplitskiy et al. 2022
[9] https://econpapers.repec.org/RePEc:eee:respol:v:49:y:2020:i:7:s0048733320301414 Fontana et al. 2020
[10] https://arxiv.org/abs/1910.03233 Bornmann et al. 2019
[11] https://arxiv.org/abs/2512.03723 Li, Lin, Wu 2025
[12] https://experts.arizona.edu/en/publications/what-types-of-novelty-are-most-disruptive/ Leahey, Lee, Funk
[13] https://public.websites.umich.edu/~jdos/papers/A_Dynamic_Network_Measure_of_Technological_Change.pdf Funk, Owen-Smith
[14] https://www.nature.com/articles/s41586-022-05543-x Park, Leahey, Funk 2023
[15] https://www.nature.com/articles/s41586-026-10787-y Holst et al. 2026
[16] https://www.nature.com/articles/s41586-026-10788-x Park et al. reply
[17] https://arxiv.org/abs/2306.01949 and https://arxiv.org/abs/2406.15311 Petersen et al.
[18] https://arxiv.org/abs/2504.04677 Lin, Li, Wu 2025
[19] https://www.nber.org/papers/w11360 Jones 2009
[20] https://www.nber.org/papers/w23782 Bloom et al.
[21] https://www.nature.com/articles/s41586-019-0941-9 Wu, Wang, Evans 2019
[22] https://ideas.repec.org/a/inm/ormnsc/v56y2010i1p41-56.html Singh, Fleming 2010
[23] https://www.nature.com/articles/s41562-021-01084-x Zeng et al. 2021
[24] https://www.nature.com/articles/s41586-023-06767-1 Lin, Frey, Wu 2023
[25] https://arxiv.org/abs/2504.09589 Yu, Rahwan, Jia
[26] https://ideas.repec.org/a/inm/ororsc/v21y2010i5p1016-1033.html Jeppesen, Lakhani
[27] https://www.nber.org/digest/mar16/does-science-advance-one-funeral-time Azoulay et al.
[28] https://arxiv.org/abs/1302.6906 Foster, Rzhetsky, Evans
[29] https://ideas.repec.org/a/inm/ormnsc/v47y2001i1p117-132.html Fleming 2001
[30] https://lbsresearch.london.edu/id/eprint/73 Kaplan, Vakili
[31] https://ideas.repec.org/a/eee/respol/v45y2016i3p707-723.html Verhoeven et al.
[32] https://www.aeaweb.org/articles?id=10.1257/aeri.20190499 Kelly et al.
[33] https://arxiv.org/abs/2511.01211 Wu 2025
[34] https://arxiv.org/html/2409.04109 Si et al. 2024
[35] https://arxiv.org/html/2506.20803v1 Si et al. 2025
[36] https://arxiv.org/abs/2502.16487 Gupta, Pruthi
[37] https://arxiv.org/abs/2405.17044 Gu, Krenn (SciMuse)
[38] https://arxiv.org/abs/2409.14634 Radensky et al. (Scideator)
[39] https://arxiv.org/abs/2305.14259 Wang et al. (SciMON)
[40] https://arxiv.org/abs/2306.01495 Sourati, Evans
[41] https://ora.ox.ac.uk/objects/uuid:d4d2a67a-d644-4cc8-850f-97cd3817cc79/files/rgb19f8049 Su et al. (VIRSCI)
[42] https://arxiv.org/abs/2412.07727 Hao et al. (press: https://www.chemistryworld.com/news/ai-research-tools-benefit-individual-scientists-but-may-slow-scientific-progress/4022803.article)
[43] https://arxiv.org/abs/2510.22954 Jiang et al. (Artificial Hivemind)
[44] https://arxiv.org/abs/2504.05228 Zhang et al. (NoveltyBench)
[45] https://arxiv.org/abs/2402.01727 Meincke et al.
[46] https://arxiv.org/abs/2604.15145 Liu, Zhai
[47] https://arxiv.org/abs/2608.25660 Schopf et al.
[48] https://arxiv.org/abs/2509.26603 Weng et al. (DeepScientist)
[49] https://arxiv.org/abs/2506.22419 Zhao et al. (speedrun benchmark)
[50] https://github.com/KellerJordan/modded-nanogpt modded-nanogpt
[51] https://github.com/karpathy/autoresearch autoresearch
[52] https://arxiv.org/abs/2507.02554 Toledo et al.
