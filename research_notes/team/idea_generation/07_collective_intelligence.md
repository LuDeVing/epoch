# 07. Group and collective idea generation and selection: human groups, crowds, LLM teams

Prepared 2026-10-13 for the HTSA nano loop. Evidence labels: **A** meta-analysis or many replications; **B** single peer-reviewed study or large preprint with direct measurement; **C** small sample, proxy metric, one benchmark, or only an abstract or secondary summary read ("sec."). "(inference)" marks my reasoning. [n] = Sources. The shared search quota ran out mid-session, so later checks were direct fetches; unverified items are in section 6.

## Bottom line

1. Pooling independent generators beats interacting groups in humans (A) [1][2], and the one direct LLM test agrees on diversity (C) [33]. But same-model agents are not independent: 4,000 sampled research ideas held 200 unique ones [27]; two ideas were 51 of 128 first-epoch nanoGPT ideas [29].
2. Seeing others' ideas early narrows search; late, on-request or outcome-based exposure does less harm (B) [9][10][11][12].
3. Picking winners from idea text is near chance for people (B) [6] and generic LLM judges (B) [27][45]; judges grounded in experiment outcomes do better (B/C) [45][46][47]. Ideas that impress before execution lose their edge after it [28].
4. LLM debate adds little beyond voting and can lower accuracy (B) [37][39][40]; self-organised LLM teams trail their best member [41].
5. Human team diversity helps only slightly, more on complex or creative tasks (A) [26]. For LLMs, diversity must come from inputs and, with caveats, other model families; personas are weak [34][35].
6. Without an automatic verifier, selection plateaus as samples grow [53]. This pipeline has one (ladder plus exam), so judges should triage, not replace runs (inference).

## 1. Human groups: nominal vs interacting

- Meta-analysis (34 tests on quantity, 9 on quality): brainstorming groups were significantly less productive than pooled nominal groups on both, more so in bigger groups and with an experimenter present [1] (A). Earlier, 18 of 22 experiments favoured nominal groups; the four ties used pairs [2].
- Cause: production blocking (waiting to speak) explained most of the loss; free riding and evaluation apprehension were not the main cause [2] (B). Blocking disrupts the organisation and flexibility of idea generation [3] (B).
- Individuals first, then the group ("hybrid"), gave more ideas, better ideas and better self-judgement than teams; building on others' ideas gave no gain [4] (B).
- Against a blanket "alone is better": with blocking removed, others' ideas can stimulate and deeper category exploration raises originality [5]. Nominal groups gave more original but less feasible ideas, yet the ideas they selected were no better, and selection was not better than chance [6] (B). Group members report more satisfaction and fewer failures than solo workers [7] (B).
- Electronic (non-blocking) brainstorming beat face-to-face groups; large electronic groups beat nominal groups, small nominal groups beat electronic ones [8] (A, sec.).

## 2. Exposure to others' ideas: stimulation vs fixation

- Typical ideas in view cut categories and novelty without cutting count; after them, an unrelated 5-minute break gave 86% more ideas and 57% more categories (no effect without cues) [9] (B). Exposure weakened category diversity but not novelty, harm appeared late in the session, and incubation removed it [10] (B).
- Timing (N=97): examples on request gave the most novel ideas, examples when stuck the most ideas, fixed-timer examples fewer ideas than none [11] (B).
- Field experiment in computational biology: showing interim solutions steered effort to improving existing approaches and narrowed search [12] (B). Showing others' estimates cut diversity without improving group accuracy (144 people) [13] (B, sec.).
- Mixed: 800+ people shown many ChatGPT ideas became collectively more diverse, "different, not better" [14] (B); one shared AI starter raised story similarity 10.7% (300 writers) [15] (B).

## 3. Crowds, contests and selection

- Contests: in a 125-solver challenge, human-crowd entries were more novel and human-AI entries more viable [16] (B). Netflix Prize leaders blended SVD, kNN and neural models; a merged team crossed the 10% line [17] (C, tertiary). Reusing one hold-out invites overfitting; the Ladder limits it [18] (B).
- Evaluators penalise novelty: randomised proposals that were highly novel or close to the evaluator's expertise scored lower (2,130 pairs) [19] (B). Creators misjudge their own ideas but beat managers on others' (339 raters) [20] (B, sec.).
- Crowds vs experts: 20 consumers sufficed, consumer panels beat experts, and a one-SD better raw idea meant about 50% higher sales [21] (B). Crowd and expert funding choices correlated; most disagreements were crowd favourites [22] (B, sec.).
- Aggregation (227 people, 10 questions): meetings, nominal groups, Delphi and prediction markets did not differ overall; markets never beat meetings; nominal groups and markets added little over a simple average [23] (B). No study of prediction markets for idea selection was found.
- Averaging a few judges picked on recent accuracy works [24] (C, sec.); crowds are wisest when judgments differ systematically [25] (theory).

## 4. Group diversity and quality

615 reports, 2,638 effect sizes: team diversity relates positively but insubstantially to performance (|r| < .1), more on complex or creative tasks [26] (A).

## 5. LLM teams, ensembles and selection, 2024-2026

**Homogeneity.**
- 4,000 sampled ideas per topic held 200 non-duplicates (cosine > 0.8); the best LLM ranker agreed with human reviewers at 53.3%, against 56.1% between humans [27] (B). After 43 researchers executed ideas, LLM ideas lost their novelty edge [28] (B). In a nanoGPT-speedrun search, 51 of 128 first-epoch ideas were one of two ideas, 119 of 128 after RL on reward [29] (B).
- 70+ models give strikingly similar open-ended outputs [30] (B, sec.). LLM product ideas were 7x likelier to reach the top 10% but less diverse; chain-of-thought, vendor pooling and constraints narrow the gap [31] (C). Asking for several answers with probabilities lifted creative-writing diversity 1.6-2.1x [32] (C).

**Structure, roles, mixtures.**
- Enforced independent writing before discussion (NGT) beat a standard multi-turn protocol on Vendi diversity (GPT-5.1: 2.53 vs 1.66); diversity per agent fell from 1.03 to 0.47 as groups grew from 3 to 7; a three-vendor mix raised Vendi 2.75 to 3.40 in one persona structure [33] (C; an undefined "Recursive" protocol scored above NGT).
- Personas gave no accuracy gain over 162 roles, 4 model families, 2,410 questions [34] (B); persona populations collapse onto stereotypes [35] (C). Persona-diverse proposers and reviewers raised a non-duplicate ratio from 0.77 to 0.81; quality was judged by GPT-4 alone [36] (C).
- Debate underperformed majority voting at equal response count [37] (B); five methods on nine benchmarks did not reliably beat chain-of-thought or self-consistency, though model heterogeneity helped [38] (B); voting explains most of the gain [39] (B); agents flip correct answers under peer pressure [40] (C). Self-organised teams trail their best member by up to 41.1% (figures differ across versions) [41] (B).
- Self-MoA beat mixing different LLMs by 3.8% on average because mixing lowers mean quality [42] (B); model "jaggedness" let ensembles beat any single model on unique-idea counts [43] (C); diversity metrics mostly re-express capability, shared errors being the stable predictor of lower gain (30 LLMs, 31,900 subsets) [44] (C).

**Selection.**
- Frontier LLMs were at chance choosing the better of two AI-research ideas; retrieval plus fine-tuning reached 64.4% vs 48.9% for 5-expert ensembles (NLP), 77% on the full set [45] (B). A fine-tuned 8B model reached 77.1% vs GPT-5 61.1% [46] (C). Experiment records cut selection regret 78% in a new environment, helping more than a better model or more reasoning [47] (C). LLM novelty judges drift to "medium" [57] (C).
- A panel of diverse small judges beat one large judge at over 7x lower cost [48] (B); 12 LLMs matched 925 human forecasters [49] (B). Judges favour their own outputs [50] and show position and verbosity bias [51] (B). Tournament Elo in the AI co-scientist tracked GPQA accuracy but is self-assessed [52] (B/C). Pairwise judging beat direct scoring in an evaluator study [55] (C).
- Execution-grounded evolutionary search beat best-of-N from epoch 1 (nanoGPT 35.9 to 19.7 min) [29] (B), yet simple baselines matched code evolution in other domains [56] (B); a bandit over LLMs with novelty rejection was sample-efficient [54] (C).

## 6. Negative results and gaps

- Null or negative: nominal groups' extra output did not improve selection [6]; diversity |r| < .1 [26]; markets no better than meetings [23]; personas no gain [34]; debate no better than voting [37][39]; mixing models can lower quality [42]; Elo is self-assessed [52]; execution erodes LLM idea advantage [28].
- Not verified (quota exhausted), so excluded: Hong-Page diversity theory and critiques, network-structure experiments, Jeppesen-Lakhani marginality, NIH reviewer agreement, Kaggle overfitting meta-analysis, prediction markets for ideas.
- No study found of nominal vs interacting LLM groups scored on executed ML ideas, nor cross-family vs single-family generation scored by execution.
- Human blocking, apprehension and free riding have no direct LLM analogue; LLM analogues (anchoring, conformity, mode collapse, self-preference) are mostly measured by proxies that may not track executed value [28][44].

## 7. What would transfer to an LLM-driven idea loop

Already consistent: isolated sketch contexts, input "cards", no personas, blind clustering, one interrogation chain. Effects are directional unless a number is cited; each is a proposal to ablate at matched token cost. Search and test-budget mechanics are in 04_evolutionary_search.md and 11_decision_science.md.

| # | Mechanism and where it plugs in | Evidence | Expected effect | Measurement |
|---|---|---|---|---|
| 1 | **Auditable nominal sketching.** Keep contexts isolated (ideate_round). Add a discovery curve (new clusters per 10 contexts) with a stop rule, and a collapse alarm (share of sketches in the two largest clusters). | [1][2][27][29][33] | Fewer wasted sketch calls, early warning of mode collapse; no quality gain by itself. | Distinct clusters per 100 sketches; top-2 share per round; ladder-passers per token at 30 vs 60 contexts. |
| 2 | **Staged exposure: outcomes first, pull not push.** Round 1 stays blind. Later rounds see measured outcomes (idea, test, result), not peers' untested sketches (history_text), and an agent asks for them after writing its first three. Option: explore/exploit mix of winners plus random past ideas. | [9][10][11][12][13][29][56] | Less rediscovery of round-1 clusters than pushing full history; win-rate effect unknown (IID sampling is a strong baseline). | Four arms: none, pushed outcomes, requested outcomes, pushed peer sketches (negative control). Rediscovery rate, obvious-rate, clusters per 100 sketches, ladder gap per sketch. |
| 3 | **Pairwise tournament for representatives and ties.** Replace cheapest-test ties (build_clusters) with position-swapped pairwise judgements on the stripped sketch, Swiss schedule of about five rounds. | [27][51][55] | Steadier ranks than 1-10 scores; accuracy near human-reviewer level, so a tie-breaker, not a ranker. | Swap-flip rate, transitivity violations, Spearman with the 240-step gap. A 100-pair AUC carries about +/-0.10 uncertainty; pool across runs. |
| 4 | **Separate cross-family jury, calibrated on the ledger.** At least 3 judge families other than generator and builder; each sees the stripped sketch plus nearest past ledger rows and outputs P(beats baseline by margin); average the judges with the best past Brier scores. Use to drop the weakest third before building, never to override ladder checks. | [21][24][25][44][45][46][47][48][49][50] | Near chance at first, improving with in-environment data (published: Spearman +0.27 in-environment [47]); value is skipped builds. | Log predictions before build; AUC and Brier per judge and jury; error correlation across families; cost per ladder-pass with and without. Keep only if AUC >= 0.6 on 200+ resolved ideas. |
| 5 | **Input diversity first, models second, personas last.** Keep the cards (docs, analogies, diagnostics, seeds). Add an arm sending about a quarter of contexts to other model families, allocated by a bandit on new-cluster yield, plus a "several answers with probabilities" arm. No persona text. | [30][32][33][34][35][42][43][54] | Higher distinct-cluster yield (published: Vendi +0.65 for a three-vendor mix in one setting [33]); mean sketch quality may fall. | Marginal clusters and ladder-passers per card and per family (leave-one-out); cost. |
| 6 | **Wildcard slots.** Reserve 2 of 10 build slots (select_clusters) for cheap-test clusters far from the top-scored ones, hedging the evaluator novelty penalty. | [5][6][19][57] | More variance and some rare wins; no guaranteed gain. | Win rate of wildcard vs ranked slots, pooled over runs from the permanent log. |
| 7 | **Calibrate the score on the ledger.** Fit each cluster_score component (angle count, new, obvious, cheap, size) to ladder outcomes after each batch; cut weights with AUC near 0.5. Same-model agreement can reflect shared priors, so "angle count" may track obviousness (inference). Report only thresholded exam gains upward (Ladder style). | [18][28][30] | Better slot allocation; magnitude unknown. | Per-component AUC and Spearman against the 240-step gap; refit stability across batches. |
| 8 | **Critique policy: independent critics, vote, no peer debate.** Keep the single interrogation chain and pre-mortem; add independent pre-mortems with different evidence packs, merged by union of objections. | [36][37][38][39][40][41] | No accuracy gain expected from debate; possible small feasibility gain from critic diversity. | Share of observed failures anticipated by the top objection; 1 vs 3 independent pre-mortems at matched tokens. |

## Sources

1. Mullen et al. 1991: https://dynamic.decorrespondent.nl/downloads/michiel-de-hoog/Mullen-1991-Productivity-Loss-in-Brainstorming-Groups.pdf
2. Diehl, Stroebe 1987: https://homepages.se.edu/cvonbergen/files/2013/01/Productivity-Loss-In-Brainstorming_Toward-the-Solution-of-a-Riddle.pdf
3. Nijstad et al. 2003: https://research.rug.nl/en/publications/production-blocking-and-idea-generation-does-blocking-interfere-w/
4. Girotra et al. 2010: https://mackinstitute.wharton.upenn.edu/2010/idea-generation-and-the-quality-of-the-best-idea/
5. Stroebe et al. 2010: https://research.rug.nl/en/publications/beyond-productivity-loss-in-brainstorming-groups-the-evolution-of/
6. Rietzschel et al. 2006: https://research.rug.nl/en/publications/productivity-is-not-enough-a-comparison-of-interactive-and-nomina/
7. Nijstad et al. 2006: https://bps.org.uk/research-digest/why-do-we-still-believe-group-brainstorming
8. DeRosa et al. 2007: https://www.sciencedirect.com/science/article/abs/pii/S0747563205000506
9. Kohn, Smith 2011: https://bps.org.uk/research-digest/stuck-your-ideas-fixation-group-brainstorms
10. Zhou et al. 2019: https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2019.01459/full
11. Siangliulue et al. 2015: https://www.eecs.harvard.edu/~kgajos/papers/2015/siangliulue15providing.shtml
12. Boudreau, Lakhani 2015: https://lbsresearch.london.edu/id/eprint/177
13. Lorenz et al. 2011: https://acawiki.org/How_social_influence_can_undermine_the_wisdom_of_crowd_effect
14. Ashkinaze et al. 2024: https://arxiv.org/abs/2401.13481
15. Doshi, Hauser 2024: https://www.sciencedaily.com/releases/2024/07/240712222127.htm
16. Boussioux et al. 2024: https://ideas.repec.org/a/inm/ororsc/v35y2024i5p1589-1607.html
17. Netflix Prize: https://en.wikipedia.org/wiki/Netflix_Prize
18. Blum, Hardt 2015: https://arxiv.org/abs/1502.04585
19. Boudreau et al. 2016: https://ideas.repec.org/a/inm/ormnsc/v62y2016i10p2765-2783.html
20. Berg 2016: https://www.gsb.stanford.edu/insights/managers-are-not-best-judge-creative-ideas
21. Kornish, Ulrich 2014: https://funginstitute.berkeley.edu/wp-content/uploads/2015/01/jmr-252E12-252E0401_0.pdf
22. Mollick, Nanda 2016: https://www.library.hbs.edu/working-knowledge/how-crowds-and-experts-kickstart-the-arts
23. Graefe, Armstrong 2011: https://faculty.wharton.upenn.edu/wp-content/uploads/2010/04/41-JSA-Comparing-face-to-face-meetings-nominal-groups-Delphi-and-prediction-markets-on-estimation-task.pdf
24. Mannes et al. 2014: https://scholars.duke.edu/individual/pub1040384
25. Davis-Stober et al. 2014: https://arxiv.org/abs/1406.7563
26. Wallrich et al. 2024: https://gwern.net/doc/economics/2024-wallrich.pdf
27. Si, Yang, Hashimoto 2024: https://arxiv.org/html/2409.04109v1
28. Si, Hashimoto, Yang 2025: https://arxiv.org/abs/2506.20803
29. Si et al. 2026: https://arxiv.org/html/2601.14525v1
30. Jiang et al. 2025: https://arxiv.org/abs/2510.22954
31. Terwiesch et al. 2026: https://arxiv.org/abs/2607.27553
32. Zhang et al. 2025 (VS): https://arxiv.org/abs/2510.01171
33. Chen et al. 2026: https://arxiv.org/html/2604.18005
34. Zheng et al. 2024: https://arxiv.org/abs/2311.10054
35. Xiao et al. 2026: https://arxiv.org/abs/2604.24698
36. Ueda et al. 2025: https://arxiv.org/html/2507.08350
37. Huang et al. 2023: https://arxiv.org/pdf/2310.01798
38. Zhang et al. 2025 (MAD): https://arxiv.org/abs/2502.08788
39. Choi et al. 2025: https://arxiv.org/abs/2508.17536
40. Wynn et al. 2025: https://arxiv.org/abs/2509.05396
41. Pappu et al. 2026: https://arxiv.org/abs/2602.01011
42. Li et al. 2025: https://arxiv.org/abs/2502.00674
43. Mathur et al. 2026: https://arxiv.org/abs/2605.10574
44. Kim 2026: https://arxiv.org/abs/2607.20768
45. Wen et al. 2025: https://arxiv.org/abs/2506.00794
46. Mule et al. 2026: https://arxiv.org/abs/2605.21491
47. Wang et al. 2026: https://arxiv.org/abs/2610.12235
48. Verga et al. 2024: https://arxiv.org/abs/2404.18796
49. Schoenegger et al. 2024: https://arxiv.org/abs/2402.19379
50. Panickssery et al. 2024: https://arxiv.org/abs/2404.13076
51. Zheng et al. 2023: https://arxiv.org/abs/2306.05685
52. Gottweis et al. 2025: https://arxiv.org/pdf/2502.18864
53. Brown et al. 2024: https://arxiv.org/abs/2407.21787
54. Lange et al. 2025: https://arxiv.org/abs/2509.19349
55. Liu et al. 2024: https://arxiv.org/abs/2403.16950
56. Gideoni, Risi, Gal 2026: https://arxiv.org/abs/2602.16805
57. Schopf et al. 2026: https://arxiv.org/abs/2608.25660
