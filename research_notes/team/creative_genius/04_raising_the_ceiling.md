# 04 - Raising the ceiling: techniques that move the best idea, not the average

*2026-10-13. For the ambitious lane of the nano loop. Scope: human and LLM evidence on the maximum (the best idea), with the mean beside it. Judge tags: **O** outcome (citations, contest score, executed result), **R** human raters, **E** embedding or LLM-ranker metric. The shared web-search quota ran out mid-task; later checks were direct fetches of primary papers. Second-hand (earlier briefs or search summaries): [1] [6] [14] [17] [18] [21] [45] and Sio and Ormerod. "(calc)" marks my arithmetic, not a finding.*

## 1. Bottom line

1. **The ceiling is a sampling problem first.** The best of N normal draws sits near 1.5, 2.5 and 3.2 SD above the mean at N = 10, 100, 1,000 (calc); correlation rho shrinks that by sqrt(1 - rho), so rho = 0.3 turns 100 draws into about 3 effective ones (calc). In LLMs, 4,000 research ideas held 200 non-duplicates [30]; one idea per independent session on one prompt scored 0.452 pairwise diversity against 0.773 for people [28]. Independence counts only when the inputs differ, and N alone does not buy very-high-impact work [5].
2. **Variance raises the maximum and costs the mean.** Far examples raised mean and maximum novelty and the spread of quality, not mean or maximum quality, at one fewer concept per session [12]. More contest entrants cut the average score about 5 points each and left the best alone [9]. Failure-tolerant funding gave 97% more top-1% papers and 35% more flops [25]. A lane that looks worse on the average is working as designed.
3. **Few levers were judged on the maximum by outcome**: contests [9], funding [25], citations [5][23][24], execution-grounded LLM search [32][41][42]. The rest are rater-judged means, and reviewer-rated novelty of LLM ideas did not survive execution [31].
4. **Post-training spends the tail.** RL-trained models win at pass@1 and lose to their base models at large k [27]; alignment cut the Creativity Index 30.1% while "be creative" and top-p did nothing (p = .23, N = 600) [34]; RL on execution reward raised the average, not the maximum [32]. Tail access comes from heterogeneous inputs, set-level prompts, tail-probability sampling and cheap-model variance, not instruction words or method prompts [22]; item-by-item "make it bolder" collapses diversity [28].

## 2. Evidence by lever

| Lever | Mean | Maximum / tail | Judge, N |
|---|---|---|---|
| Quantity (equal odds [1]) | Manipulations that changed output left average quality unchanged [2]; fluency vs rated creativity r = .73 [3]; flat only at low Openness [4] | Good ideas track output, r = .82 [2]. Best paper sits at a random career position; productivity alone "cannot substantially enhance" a very-high-impact paper, ability Q and luck do [5]. Serial order: at most 3.5% of variance [6] | R, N = 246 and 152; O, 7 fields |
| Solo first, then pool | Hybrid beat teams on count, quality, discernment [7] | Best-idea quality depends on N, mean, variance, discernment [7]; selecting nominal-group ideas was no better than chance [8] | R, students |
| More contest entrants | Individual score down ~5 points per entrant | Room best unchanged (-0.24, n.s.), up on complex problems; published: more entrants raise performance under high uncertainty [9] | O, 645 problems, 9,627 rooms; 9,661 contests |
| Constraints | Required noun 5.18 vs 4.29, partial eta-sq .53, carried over [10]; only without time pressure [11]; LLM random constraint: diversity .735 vs .679 [28] | Not analysed in [10][11]. Eccentric constraints not monotone [28]; less input data gave more general programs [43] | R, N = 64 and 48; E |
| Distant stimuli | Far-field: novelty d = .56, quantity -1 concept [12]; closer sources shortlisted more [13] | Max novelty d = .56, quality SD up (d = .64), mean and max quality unchanged [12]. LLMs: no overall gain, positive in the farthest half (b = .12) or tenth (b = .24); originality-feasibility r = -.74 [15]. "Sweet spot" [14]: second-hand | R, N = 153; >350 people; 1,002 raters |
| Opposites, counterfactuals, "what would have to be true" | Testing opposites of each property: 78.3% vs 38.3% (properties only) vs 36.7% found the rule [16] | No ideation-ceiling study found. Told that a better-order construction exists, AlphaEvolve found one at once; elsewhere hints yielded "variations of the initial hints" [43] | O, N = 180; case |
| Abstraction, reformulation, incubation | Generic parts +67% solved, one lab [17]; Step-Back +7 to +27 points, 11.9% new errors [18]; incubation d ~ .29, no break type beat no break when preregistered [20]; LLM reframing no gain [19] | None measured. Problem finding: see creative_genius/07 | O (solve rate), R; N = 280 |
| Lateral thinking, SCAMPER, TRIZ | TRIZ: novelty up, quantity down, 3 universities [21]; 25 method prompts x 81 briefs x 5 LLMs: "wild" prompts matched or beat them [22] | Top-5 novelty highest for brainstorm and category-negation prompts; no max study for lateral thinking [22] | R, E |
| Atypical combination, risk tolerance | Failure-tolerant funding: output +39%, 73 investigators [25] | Top-5% +55%, top-1% +97%, flops +35% [25]. Novel papers: higher variance, more top-1% in the long run, delayed recognition [24]. Conventional core plus atypical links: hit rate 9.11 vs ~5 per 100, 17.9M papers [23] | O |
| More samples (LLM) | - | Coverage log-linear over four orders; SWE-bench Lite 15.9% to 56% at 250 samples; voting and reward models plateau [26]. FunSearch record in 4 of 140 runs [42]. 100 to 1,000 ideas: hardest human idea distance .762 to .711 [28] | O (code), E |
| LLM ideas, top tail | Novelty 5.64 and 5.81 vs 4.84; feasibility 6.34 and 6.44 vs 6.61 (n.s.) [30] | 7x more top-decile (human 5, GPT-4 15 and 20 of top 40) [28]; best humans match or beat best chatbots, N = 256 [33]; after 100-h execution AI ideas lost 1.05 to 1.98 points vs at most 0.63, ranks flipped [31] | R, 49 ideas per arm, 79 reviewers; purchase intent; O, 43 projects |
| Retrieval and mutation pipelines | MOOSE-Chem average score 2.56; Nova 3.4x unique novel ideas [38]; SciMON: 56% of ideas gained novelty per iteration but drifted to popular add-ons [39]; CoI +56 Elo, trend chain beat literature volume [40] | MOOSE-Chem top score 4.02; mutation-recombination raised the top score under all three LLM evaluators (+0.28 to +0.90) with the average moving -0.10 to +0.15; experts found two main innovations or more in the best of 4 for 21 of 51 papers [37] | E, LLM ranker vs known answers |
| Program evolution | - | AlphaEvolve: 50+ problems, matched 75%, improved 20%; 4x4 complex matmul at 48 vs 49 [41]; FunSearch cap set 512 [42]; 67 problems, most rediscovered, several improved [43] | O |

## 3. What produced the novel step in the discovery systems (hit rates: creative_genius/05)

- **A graded, cheap, multi-seed score and a restricted space.** AlphaEvolve scored best rank per target plus fraction of seeds [41]; continuous distances beat discrete counts [43]. FunSearch evolved one priority function [42]; removing prompt context hurt AlphaEvolve [41]; for maths bounds, search space and prompt knowledge mattered more than evolution machinery [44].
- **Variance from many cheap runs and mixed models.** The cheapest model across many runs was cost-effective on an easy problem but could not build the elaborate Nikodym constructions; mixing in cheaper models sometimes beat high-end-only runs; small-only hurt [43][41].
- **A chain of mutations from a plain start.** The paper's tensor-decomposition example took 15 mutations of an Adam program [41]. MOOSE-Chem composed a background with a separately retrieved inspiration (over 75% of true inspirations within the top 4% of the corpus) [37].

## 4. A recipe for the ambitious lane

Rates and thresholds are my proposals; the evidence fixes direction, not numbers.

1. **Disjoint packs, independent contexts, two tiers.** Each lane call gets a pack no other call gets this round (part, one assigned source, one constraint, one measured fact) and sees no other output. Draw about 10x more lane sketches than builds, 70% cheap tier, 30% strongest. Basis: [28][43]; showing interim solutions narrowed search in a field contest [45]; Opus kept improving over search epochs, Sonnet and GPT-5 saturated [32]. Cost: cheap-tier sketches fail rung 0 more often. Check: distinct clusters per 100 sketches vs same-pack replicates.
2. **Set-level staged seeds.** One context: 40 terse seeds, rewrite until no two share a mechanism, keep the 5 farthest from the ledger, compare each with its 3 nearest ledger entries and rewrite once (more passes drift to popular add-ons [39]), then elaborate. Never "bolder" per item [28]; the list-then-different chain gave the highest diversity of the prompts tried [29]. Cost: one extra call. Check: unique clusters vs a per-item "bolder" control.
3. **Tail draw on a fifth of calls.** "Give five candidate changes, each with the probability you would have proposed it by default, all below 0.1." Basis: diversity rises as the threshold falls, larger models gain 1.5 to 2 times more, effect on the maximum untested [35]. Cost: small-model quality loss; stop if survival falls below half the standard arm.
4. **Existence-target prompt.** Give measured headroom and an existence claim: "a change exists that recovers 30% of this at no more than +2% step time; give three mechanisms and what would have to be true at rung 1." Basis: [43]; search reached 19.7 minutes against a 35.9 baseline while the human record is 2.1 [32]. Cost: anchoring and cheating on leaky checks [43]; state outcomes, never methods.
5. **Banded far source, typed mapping.** One assigned source per pack from outside ML training, 60% mid band, 40% far, with mapping, a named break and a prediction. For strong LLMs the benefit appears only at the far end [15]; closer sources were shortlisted more [13]. Arm: planner-chosen source (Nova: unique ideas kept rising [38]) vs random. Cost: originality-feasibility r = -.74 [15]; most die at rung 0 or 1. Check: hit rate by band.
6. **Constraint slot and opposite slot.** One structural constraint from a 20-item list (no new parameters; one scalar per layer; gate at zero; late phase only), or "list six assumptions of this part, state each opposite, build the change that assumes one not yet in the ledger plus a test the baseline would fail". Basis: [10][28][16]. Cost: infeasible sketches; constraints help only without time pressure [11], so give lane calls an unhurried budget; one constraint only, eccentric ones saturate [28].
7. **Re-mutate survivors.** After round 1, half the lane makes variants of sketches that passed rung 2 or later; half draws new packs shown earlier ideas plus "completely different"; exploit share annealed from 50% [32]. Basis: mutation raised the top score [37]; evolution beat best-of-N at equal budget from epoch 1 [32]. Cost: average flat or lower; the authors note forced-different variants often make little sense [37].
8. **Outcome-only lenient gate.** Shortlist by cluster champion plus random k; judge by the first measured rung with a lenient threshold; send a random 10% of rejects to the same rung. Never rank by LLM novelty or quality [30][31]; novel work is recognised late [24]; vote and reward-model selection plateaus [26]. Cost: GPU on weak sketches, bounded by lane share.
9. **Quota by construction.** An idea counts only if it came from a lane pack, sits beyond a cosine threshold from the ledger, declares P(success) < 0.2 and names a rung-1 observation that would falsify it. Log pack parts, tier, selection probability.

## 5. Measuring the lane against the safe lane

- **Design.** Same baseline and rungs, fixed slots per run (for example 8 safe, 2 to 3 lane), random order, pre-registered, no optional stopping; log lane flag, pack parts, propensity.
- **Outcomes, executed only.** Rung-2 pass rate; stackable or verified per build and per GPU-hour; top-decile and maximum learn_z per 100 builds; verified wins in clusters the safe lane never reached; idea vs implementation failures. Report mean and maximum side by side: the lane should lose the first and win the second.
- **Break-even (calc).** Analogs give about 2 to 3% per attempt (FunSearch 4 of 140; DeepScientist 21 of 1,100, thinking_parts/04) against about 7% for a plain loop (idea_generation/09), with a median record worth 1.1% of wall time (synthesis C5). Lane hits must be worth 2.3 to 3.5 times a safe hit.
- **Sample size (calc).** Detecting 5% to 10% needs about 435 builds per arm: pool 20 or more runs, or bootstrap the 90th percentile of learn_z.
- **Decision.** Keep or grow the lane if its upper-decile gain per GPU-hour matches the safe lane or it owns a verified win from a new cluster; else cut to 10%. After 150 lane builds, drop pack parts (source band, constraint, opposite, tail) by leave-one-out.

## 6. Gaps

No study scores the maximum with outcome judgement for opposites, counterfactuals, abstraction-first, incubation, SCAMPER or lateral thinking. LLM max-of-N evidence is code and maths coverage, not research-idea quality. AlphaEvolve and FunSearch ablations are figure-level. The Hivemind claim is contested [36]. Not obtained: Stokes, Kozbelt 2008 (hits reportedly cluster after the productivity peak), the Galinsky and Markman counterfactual studies, Getzels (see creative_genius/07); the sweet-spot claim [14] rests on a secondary source.

## Sources

[1] Simonton 1997: https://doi.org/10.1037/0033-295X.104.1.66 (summary https://www.jimdavies.org/summaries/simonton1997.html)
[2] Diehl, Stroebe 1987: https://homepages.se.edu/cvonbergen/files/2013/01/Productivity-Loss-In-Brainstorming_Toward-the-Solution-of-a-Riddle.pdf
[3] Jung et al. 2015: https://www.frontiersin.org/articles/10.3389/fpsyg.2015.00864/full
[4] Friis-Olivarius, Christensen 2019: https://pmc.ncbi.nlm.nih.gov/articles/PMC6409333/
[5] Sinatra et al. 2016: https://barabasi.com/media/pub_imports/files/825.pdf
[6] Barbot 2026: https://doi.org/10.3390/jintelligence14060100 (via idea_generation/01)
[7] Girotra, Terwiesch, Ulrich 2010: https://mackinstitute.wharton.upenn.edu/2010/idea-generation-and-the-quality-of-the-best-idea/
[8] Rietzschel et al. 2006: https://research.rug.nl/en/publications/productivity-is-not-enough-a-comparison-of-interactive-and-nomina/
[9] Boudreau, Lacetera, Lakhani 2011: https://pubsonline.informs.org/doi/10.1287/mnsc.1110.1322 ; working paper http://www.aeaweb.org/conference/2009/retrieve.php?pdfid=212
[10] Haught-Tromp 2016: https://www.rider.edu/sites/default/files/docs/tromp_haught-tromp_PACA_2016.pdf
[11] Moreau, Dahl 2005: https://ideas.repec.org/a/oup/jconrs/v32y2005i1p13-22.html
[12] Chan et al. 2011: https://edrl.engr.wisc.edu/wp-content/uploads/sites/142/2022/02/2011-jmd-distancecommonness.pdf
[13] Chan, Dow, Schunn 2015: https://link.springer.com/10.1007/978-3-319-91134-2_12 ; summary https://www.hcii.cmu.edu/news/think-outside-box-not-so-fast
[14] Fu et al. 2013: https://doi.org/10.1115/1.4023158 (not opened)
[15] Liu et al. 2026: https://arxiv.org/abs/2603.19087
[16] Branchini et al. 2025: https://pmc.ncbi.nlm.nih.gov/articles/PMC12402026/
[17] McCaffrey 2012: https://doi.org/10.1177/0956797611429580 (via thinking_parts/01)
[18] Step-Back: https://arxiv.org/abs/2310.06117 (figures via thinking_parts/05)
[19] Shin et al. 2025: https://arxiv.org/abs/2503.01631
[20] McDaniel et al. 2025: https://doi.org/10.1038/s41598-025-09736-y ; Sio, Ormerod 2009 via idea_generation/01
[21] Hernandez et al. 2012: https://peer.asee.org/experimental-assessment-of-triz-effectiveness-in-idea-generation.pdf (via idea_generation/03)
[22] IDEAFix 2026: https://arxiv.org/abs/2606.00875
[23] Uzzi et al. 2013: https://www.kellogg.northwestern.edu/faculty/uzzi/htm/papers/Science-2013-Uzzi-468-72.pdf
[24] Wang, Veugelers, Stephan 2017: https://www.nber.org/papers/w22180
[25] Azoulay, Graff Zivin, Manso 2011: https://www.nber.org/papers/w15466.pdf
[26] Brown et al. 2024: https://arxiv.org/abs/2407.21787
[27] Yue et al. 2025: https://arxiv.org/abs/2504.13837
[28] Terwiesch et al. 2026: https://arxiv.org/abs/2607.27553
[29] Meincke et al. 2024: https://arxiv.org/abs/2402.01727
[30] Si et al. 2024: https://arxiv.org/abs/2409.04109
[31] Si et al. 2025: https://arxiv.org/abs/2506.20803
[32] Si et al. 2026: https://arxiv.org/abs/2601.14525
[33] Koivisto, Grassini 2023: https://www.nature.com/articles/s41598-023-40858-3
[34] Lu et al. 2025: https://arxiv.org/abs/2410.04265
[35] Zhang et al. 2025: https://arxiv.org/abs/2510.01171
[36] Jiang et al. 2025: https://arxiv.org/abs/2510.22954 ; Schaeffer et al. 2026: https://arxiv.org/abs/2609.33936
[37] MOOSE-Chem: https://arxiv.org/abs/2410.07076
[38] Nova: https://arxiv.org/abs/2410.14255
[39] SciMON: https://arxiv.org/abs/2305.14259
[40] Chain of Ideas: https://arxiv.org/abs/2410.13185
[41] AlphaEvolve: https://arxiv.org/abs/2506.13131
[42] FunSearch: https://pmc.ncbi.nlm.nih.gov/articles/PMC10794145/
[43] Georgiev et al. 2025: https://arxiv.org/abs/2511.02864
[44] Gideoni et al. 2026: https://arxiv.org/abs/2602.16805
[45] Boudreau, Lakhani 2015 (via idea_generation/07): https://lbsresearch.london.edu/id/eprint/177
