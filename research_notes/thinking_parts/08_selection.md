# 08. Judgement and selection: from ranking ideas to choosing a portfolio

*Researched 2026-10-13 for the HTSA nano loop. The layer after `11_decision_science.md` (testing, halving, Pandora ordering), which is not repeated: choosing a set, cost, value of information, how humans select, learned selectors. Grades: **A** peer-reviewed, large real data; **B** peer-reviewed theory, simulation or one study; **C** preprint or self-reported; **D** my arithmetic or inference. The web-search quota was spent, so sources were fetched directly (abstract or full text); blocked items are under Limits. Code claims were checked by reading the code and running the real functions on synthetic clusters.*

## Bottom line

1. **Two defects come first.** (a) `tree.split_select` takes each part's best cluster in part order: with 5 main slots and 8 parts the first three parts (inward) and first two (outward) take every slot, and in a synthetic run the strongest cluster in any of the last five parts was never picked (D, reproduced with the real functions; script `repro_split.py` in the session scratchpad). "Coverage across parts" is not what the loop delivers. (b) The long-shot lane is one build per run (`round(0.2*6)` = 1; off in round 2, where k = 2), drawn with weights exp(score), with no selection probability logged; telling 10% from 20% yield takes about 200 builds per arm (D). The lab has 7 real builds and no rows `calibrate.py` can read.
2. **Selectors have a weak signal that grows with outcome data, not reasoning.** LLM pairwise accuracy: 65-69% with search history [26]; 83% early in a trajectory, 57% after three successes [27]; 31% top-1 among five [29]; 78-84% after pilots [26]; Spearman 0.64-0.90 with 320 raw in-environment results in context [28] (C). This refines SYNTHESIS C2: records and pilots rank far better than text.
3. **Inside a plausible tier experts cannot rank**: reviewer agreement ICC 0 [18]; percentile score explains under 1% of output variance across 102,740 funded grants [20] (B, A). Filter, spread, randomise inside the tier.
4. **Risk here is coverage, not variance.** We promote the best of n, so payoff rewards variance and punishes correlated failure; P(at least one distinct win) is monotone submodular and greedy is within 1-1/e [1] (B; application D). Fitted weights lose to equal weights at small n [10] (A); I found no outcome-validated weighted-sum, AHP or Pareto scheme for research ideas.
5. **Cost-aware ranking drifts toward ideas that reveal themselves cheaply** [17] (B); the measured cost term is implementability (about 60% of failed implementations in one agent were implementation errors [31], C). Diversity pays only in an outcome-aligned space [9] (B), and modestly (+7% on proxies [7], C).

## 1. Evidence

**Sets, coverage, risk**
- Greedy gives 1-1/e for monotone submodular objectives; with costs, the better of cost-benefit and uniform greedy gets (1-1/e)/2 and partial enumeration restores 1-1/e [1]; adaptive greedy keeps a guarantee when outcomes arrive between picks [2] (B). Determinantal point processes (DPPs) score a set by quality times diversity, with fast greedy MAP and batch-BO regret bounds [3][4][5] (B). Batch BO's "constant liar" picks each point as if earlier picks returned their posterior mean, the same device as a redundancy penalty [6] (B).
- LLM ideation: MMR-k (lambda 0.65, k = 4 of 16, 10 seeds x 10 environments) gave 23.7 strong non-duplicate ideas vs 22.2 random-k and 21.8 refine-all; random-k was "a strong low-cost baseline"; LLM-judged, one family, one author [7] (C). Exploration diversity tracked gains in 5 of 8 tasks (p < 0.05 in two), negatively but n.s. in 3 [8] (C). An unaligned descriptor did significantly worse than objective-only search on hard mazes (900 runs) [9] (B).
- None of 14 optimised portfolio models beat 1/N consistently over 7 datasets; mean-variance needs about 3,000 months for 25 assets [10] (A). The best of noisy estimates is biased upward unless shrunk [11]; best-of-n against a proxy eventually lowers the gold score [12] (B).
- Heavy tails favour breadth: almost three quarters of VC-backed founders get nothing at exit [13] (A); in 9,661 software contests more entrants raised the best outcome when uncertainty was high [14] (A).

**Cost and value of information**
- Expected improvement (EI) is zero for a lower-fidelity observation, so it values only the top fidelity; the knowledge gradient (KG) values information directly, and one-step KG was within 98% of the multi-step optimum where computed [6] (B). taKG applies KG across continuous fidelities [15]; CArBO adds a cost-cooled phase to cost-weighted BO [16] (abstracts; B/C).
- When experimentation got cheap, VCs funded more startups with less money, and the rise was disproportionately in ideas whose prospects reveal "quickly and cheaply" [17] (B).

**How reviewers and funders select**
- Grant panels: a mock NIH study (43 reviewers, 25 R01s) found ICC 0 (95% CI 0-0.14) [18] (B); scores 0.1 apart need about 384 reviewers at sigma 1 [19] (B). Across 102,740 funded grants percentile score explained r2 = 0.0078; an earlier 130,000-grant analysis found a consistent correlation, two smaller ones none [20] (A, contested, range restriction). Partial lotteries above a quality bar assume panels separate strong from weak but not strong from strong; no empirical comparison exists [21] (B).
- Forecasts and venture: the average forecast beat 96% of individual forecasts (208 experts), and citations, rank and field did not help [22] (B); 885 VCs rate the team above the product (stated, not revealed) [23] (B); fund returns persist [24] (A).
- Kaggle: over 100 competitions showed little adaptive overfitting [25] (A). I found no verified study of which kinds of idea win.

**Learned selection, 2025-2026 (C unless noted)**
- AI Research Preference Models (RPM), knockout over 15 children: 64.7-69.4% offline (random 50), 78.5% with a 5-minute pilot, 84.0% at 4 h; end to end 0.684, 0.711 (history), 0.729 (pilots), P(improve) 0.59 with lower bound 0.50; off-policy labels [26].
- Rehearse (5 seeds, 100 experiments): vanilla 7.1%, propose five and run the first 6.9%, pairwise pick 8.4%, plus focused memory 10.7%. One-line "change -> worked/not" neighbours (cosine >= 0.40) restore accuracy to 83.5%; failure reasons lower it to 80.6%; an avoid-failed-directions rule scored 52.4% [27].
- Research World Models (RWM; 2,600 records, 9 environments): raw (intervention, gain) records lifted Spearman from -0.36..0.62 to 0.64..0.90; other environments' records cut Qwen3 selection regret 78%, but cross-environment kNN fell below zero-experience [28].
- Predict-then-verify (10 candidates, pairwise pick under a 0.7 confidence gate) converged about 6x faster than AIDE (5 tasks, 3 runs) [29]. A trained pre-filter (72% on ICLR abstracts, GPT-5 53%) wrongly rejected 43 of 151 viable ideas [30]. DeepScientist's weighted sum of LLM-scored utility, quality and exploration: 5,000 ideas, 1,100 selected, 21 findings, scorer never checked [31].
- Huxley-Godel Machine (HGM) selects by clade success (Thompson on Beta): correlation with empirical clade value 0.78 vs 0.29 for the Darwin Godel Machine, 2.4-6.9x fewer CPU hours [32]. ShinkaEvolve: weighted parent sampling beat hill-climbing and best-of-N; an LLM novelty judge added little [33]. RL on execution reward lifted mean reward, not the maximum [34].

## 2. What did not work

Text-only ranking among several candidates; judge vetoes; avoid-failure rules and failure reasons; "propose five, run the first" (6.9% vs 7.1%); unaligned diversity; optimised weights at small n; cross-environment kNN; panel scores inside the funded range; expertise as a forecasting marker; execution-reward selectors that narrow the search.

## 3. Improvement ideas for this part

Cost: small = hours, medium = a day. Effects are hypotheses anchored in the cited analogs; status is against today's code.

**I1. Fix the part-order bias; pick the slate by marginal gain, with the novelty gate inside the objective. [partial]**
*Where:* `tree.split_select`, `ideate.select_clusters`, `loop._novelty_filter`.
*Mechanism:* repeat argmax of score - mu x (picks already in the part) - lambda x max similarity to picked, built and ledger texts (TF-IDF cosine via `novelty.Index`, same TARGET cell, same edit family); inward/outward quotas stay as caps. The gate never compares chosen clusters with each other and returns early in round 1 with an empty ledger; as a term it covers both.
*Effect:* removes a deterministic bias. Toy world (12 families x 5 ideas, 25% alive, 6 picks; D): one-per-family matched top-k when the family signal correlated <= 0.2 with aliveness (about 56% pairwise accuracy; P(>= 1 win) 0.65 both) and lost 4-6 points at 0.35-0.5; random 0.40. Proxy analog +7% yield [7].
*Cost:* small (about 50 lines, no model calls).
*Measure:* share of runs where each part's best cluster is built; distinct part x TARGET cells and maximum pairwise similarity per slate; old and new slates logged side by side for 10 runs, then alternated. Audit the gate by outcome (audited builds' `learn_z` vs the nearest built neighbour's); a 10% audit gives about 0.3 builds per run, too few to see false rejects.

**I2. Put cost, implementability and information value in the objective. [partial]**
*Where:* `ideate.cluster_score` (replaces `cheapness` word matching), the I1 loop, deepen targets in `loop._rounds`.
*Mechanism:* gain per cost, gain = P(implementable) x P(improves | built) x effect size; cost = builder tokens (about 20k per build in the one real run, n = 5) plus GPU minutes (rung 3 about 1, rung 4 about 5, overnight about 31 per seed) predicted by `predict.parse_prediction`, raised to a power cooling from 1 to 0.5 across rounds [16]; stop adding slots when marginal gain per cost falls below a floor; exempt the lane; cap cheap-to-test families at half the slate [17]. Interrogate ranks about k/2 to 2.5k plus the top 3, where an answer can flip a decision [6]. The puzzle harness's `order_thompson` already divides by tokens.
*Effect:* fewer slots lost to build failures; guards the drift in [17] (D).
*Cost:* small to medium.
*Measure:* tokens and GPU minutes per rung-3 survivor by cost class; slate share by class vs share of stackable wins; rank flips per interrogation.

**I3. Make within-run selection outcome-aware. [new within a run; the ledger reaches the score only via the `failed` tag]**
*Where:* new `outcome` term in `cluster_score`; `loop._rounds` (rnd >= 2); new `selection.jsonl`.
*Mechanism:* families = (part, TARGET cell) plus built neighbours at TF-IDF >= 0.30; outcome in {ladder failure, regression, improvement (`learn_z` <= -1)}; Beta posteriors shrunk to a literature prior; a Thompson draw feeds the term. Memory is one line per attempt, no reasons [27][28]. Each selection writes features, score, rank, lane, draw probability, chosen or not.
*Effect:* analog +2.3 points of endpoint gain [27] (D here); expect nothing beyond the prior before about 50 builds ([28] used 300+).
*Cost:* medium.
*Measure:* precision@k vs random on held-out runs; selective accuracy by number of prior successes; with vs without reasons.

**I4. Turn the lane into a randomised calibration holdout. [partial; 11 M6 asks for 15-20% and logged propensities]**
*Where:* `loop._select_with_lanes`.
*Mechanism:* at least 2 uniform draws in round 1 and 1 in round 2 from the plausible tier (passes gates and novelty, score >= median), probability logged; the lane rises to a third of builds when the lower 80% bound of rolling Spearman(score, `learn_z`) on randomised rows is below 0.15.
*Effect:* about 3 randomised rows per run, so calibration stops being range-restricted [20][26]; in the toy world a 2-of-6 random lane costs 4-5 points of P(>= 1 win) (D), a deliberate learning cost.
*Cost:* small.
*Measure:* 30 randomised rows in ten runs; inverse-propensity AUROC with bootstrap CI as the gate for `--weights-from-ledger`; lane vs main yield with Wilson intervals.

**I5. Rebuild `calibrate.py`: continuous target, shrinkage, honest gating. [partial; extends 11 M5]**
*Where:* `calibrate.rows_for`, `suggest_weights`.
*Mechanism:* target `learn_z` and rung reached instead of binary `checked`; one ridge or Bayesian model with `WEIGHTS` as prior mean; move a weight only if its 80% interval excludes the prior. Defects found: a bucket with < 5 rows sets its weight to 0 (the -0.75 prior for `obvious` silently becomes 0); `departure` omits adapt and contradiction, which `ideate.DEPARTURE_CARDS` includes; rows join by cluster name, not id; rows carry no `baseline_version`. Calibrate `angle` (largest weight) first.
*Effect:* avoids fitting noise at n of about 100 [10][11] (D).
*Cost:* small.
*Measure:* leave-one-run-out Spearman of predicted vs realised `learn_z`; share of weights moved; bootstrap stability.

**I6. Score the premise with a measurement, not a sentence. [partial; TARGET and the fidelity probe exist, the score ignores them]**
*Where:* `ideate.cluster_score`, `diagnose.py`, `research.tag_prompt`.
*Mechanism:* when TARGET names a diagnostic cell, `premise` = distance of the baseline's value from a reference (published or past-run), 0 for "validation loss only"; add 0.5 x premise. Extend the tagging call to name the part's assumption the sketch bets against: the family key for I1 and I3.
*Effect:* measured pathologies started QK-norm, mHC and gating (brief 12); pilots lift pairwise accuracy from 65-69% to 78-84% [26]; this is a pilot at zero GPU cost (D).
*Cost:* small to medium.
*Measure:* checked rate and `learn_z` by premise tertile (30+ builds); agreement with the fidelity probe.

**I7. Pairwise tie-break at the cut line, behind an accuracy gate. [partial; proposed in briefs 07 and 09, not built]**
*Where:* after I1, before `_novelty_filter`.
*Mechanism:* ranks k-2..k+3 only; a cheap model of another family judges stripped sketches plus I3's neighbours in both orders, strict consensus; it orders near-ties and never rejects [30]. Off when selective accuracy over the last 30 resolved pairs is < 0.55, and after each baseline promotion until re-measured [27].
*Effect:* analog +1.3 points [27], capped by the confidence cliff (D).
*Cost:* small (about 10 cheap calls per round).
*Measure:* selective accuracy and coverage by baseline version; flips under order swap.

## Limits

- Not opened (paywall, cookie wall or 403): Li & Agha 2015 (read only through [20]), Dawes 1979 and other unit-weight papers, Frazier & Powell on non-concave value of information, Robust Portfolio Modeling, Das & Dennis on weighted sums. Several 2026 items are abstract-level or v1 preprints [28][29].
- The toy simulation (independent families, binary aliveness, lognormal gains, one selector) is directional only.

## Sources

[1] Krause, Golovin, Submodular function maximization: https://las.inf.ethz.ch/files/krause12survey.pdf
[2] Golovin, Krause, Adaptive submodularity: https://arxiv.org/abs/1003.3967
[3] Kulesza, Taskar, DPPs for machine learning: https://arxiv.org/abs/1207.6083
[4] Chen, Zhang, Zhou, Fast greedy MAP for DPPs: https://arxiv.org/abs/1709.05135
[5] Kathuria et al., Batched GP bandits via DPPs: https://arxiv.org/abs/1611.04088
[6] Frazier, A tutorial on Bayesian optimization: https://arxiv.org/abs/1807.02811
[7] Zhang, Budgeted Subset Refinement: https://arxiv.org/html/2607.14118
[8] FML-bench: https://arxiv.org/html/2510.10472
[9] Pugh, Soros, Stanley, Quality diversity: https://www.frontiersin.org/articles/10.3389/frobt.2016.00040/full
[10] DeMiguel, Garlappi, Uppal 2009: https://ideas.repec.org/a/oup/rfinst/v22y2009i5p1915-1953.html
[11] Smith, Winkler 2006, optimizer's curse: https://ideas.repec.org/a/inm/ormnsc/v52y2006i3p311-322.html
[12] Gao et al., reward overoptimization: https://arxiv.org/abs/2210.10760
[13] Hall, Woodward 2010: https://www.aeaweb.org/articles?id=10.1257/aer.100.3.1163
[14] Boudreau, Lacetera, Lakhani 2011: https://ideas.repec.org/a/inm/ormnsc/v57y2011i5p843-863.html
[15] Wu et al., taKG: https://arxiv.org/abs/1903.04703
[16] Lee et al., CArBO: https://arxiv.org/abs/2003.10870
[17] Ewens, Nanda, Rhodes-Kropf 2018: https://ideas.repec.org/a/eee/jfinec/v128y2018i3p422-442.html
[18] Pier et al. 2018: https://pmc.ncbi.nlm.nih.gov/articles/PMC5866547/
[19] Kaplan, Lacetera, Kaplan 2008: https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0002761
[20] Fang, Bowen, Casadevall 2016 (PDF text-extracted): https://elifesciences.org/articles/13323
[21] Gross, Bergstrom 2019: https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.3000065
[22] DellaVigna, Pope 2018: https://www.nber.org/papers/w22566
[23] Gompers et al.: https://www.nber.org/papers/w22587
[24] Kaplan, Schoar 2005: https://ideas.repec.org/a/bla/jfinan/v60y2005i4p1791-1823.html
[25] Roelofs et al. 2019: https://proceedings.neurips.cc/paper_files/paper/2019/hash/ee39e503b6bedf0c98c388b7e8589aca-Abstract.html
[26] AI Research Preference Models: https://arxiv.org/html/2608.13940v2
[27] Rehearse: https://arxiv.org/html/2607.27687
[28] Language Models as AI Research World Models: https://arxiv.org/html/2610.12235v1
[29] ForeAgent (Can We Predict Before Executing?): https://arxiv.org/html/2601.05930
[30] AlphaResearch: https://arxiv.org/html/2511.08522v2
[31] DeepScientist: https://arxiv.org/html/2509.26603
[32] Huxley-Godel Machine: https://arxiv.org/html/2510.21614
[33] ShinkaEvolve: https://arxiv.org/html/2509.19349
[34] Si et al., Towards Execution-Grounded Automated AI Research: https://arxiv.org/abs/2601.14525
