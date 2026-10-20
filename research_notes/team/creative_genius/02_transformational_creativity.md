# 02. Transformational (upper-tail) creativity: what separates field-changing ideas, and what transfers to an LLM idea lane

Compiled 2026-10-13. Grades: **S** meta-analysis or several independent large or controlled studies agree; **M** one large observational study or one to two controlled peer-reviewed studies; **W** theory, review, small N, preprint or secondary summary. "(2nd)" = not opened, read through a secondary description. "Hit" in citation studies means top-1/5/10% cited, a proxy for impact, not for transformation. The shared search quota ran out midway, so later sources were fetched by URL. Basics in briefs 00 and 01 are not repeated.

## 1. Bottom line

1. **Transformation changes the rules, not the distance.** Exploration moves through a space defined by implicit generative rules; transformation alters or drops one, so ideas become generable that were not before. Boden: there is no clean line, tweaks count as exploration, and nearly all field work, Mozart's and Crick and Watson's included, is exploratory [1] (W). Expect few lane wins.
2. **Predictors shift odds 1.4-5x, not 50x.** Papers with a conventional core plus atypical tail are 6.7% of papers and hit 9.11 per 100 against a 5 baseline [15]; top-1% novel papers have +39.8% odds of top-1% citation and +16.8% odds of the bottom 10% [16]; the most surprising content-context combinations give about 5x the odds of a top-10% paper [17] (M).
3. **Recurring precursors:** a conventional core with one atypical link [15], an outside tool aimed at a familiar problem [17][21][22], exploration then exploitation [19], tolerance for early failure [20] (M; all observational except [20], quasi-experimental).
4. **BVSR's "blind" means the creator cannot predict utility, not random.** Creativity c = (1-p)·u·(1-v); a sighted variation cannot be creative [2][3] (W). Quantity helps, but the constant-hit-ratio form fails (diminishing returns) [2][6] (M, 2nd).
5. **Failures:** "avoid the example" and "be creative" instructions [8][34][25], random stimuli [2], far examples for best-idea quality [12], leaving one's own expertise [18] (M).
6. **LLM ceilings:** sameness [11][25] and a shared-abstraction bottleneck when blending [11] (M).

## 2. Mechanisms (roughly newest first)

- **Combination and blending** [11][10][37]. In Kombine (35 LLMs; 75 humans scored below nearly every LLM) blends are 10-16 points harder than association or analogy and models struggle to find a shared abstraction (M). Costello and Keane: interpretations are judged on diagnosticity, plausibility, informativeness, and creativity arises because these are satisfiable many ways (W, 2nd); Wisniewski adds comparison and construction processes [37] (W, abstract only). Combination practice helped problem solving, not brainstorming (W, 2nd).
- **Simonton** [2][3]. A variation has prior probability p, utility u and the creator's prior knowledge of utility v; c = (1-p)u(1-v), sightedness s = puv (W, formal). His 1988 chance-configuration model (ideas as chance permutations of mental elements) equated blind with random; the 2022 update calls that unwarranted. Equal odds: fluency vs rated creativity r = .73, 246 students, ordinary divergent thinking [5] (M); random-impact rule across careers [26] (M, 2nd). Critics: per Simonton, Forthmann et al. 2021 showed the constant hit ratio is wrong [6][2]; Simonton says equal odds is not diagnostic for BVSR and case studies only illustrate [2]; Gabora: expertise already biases generation toward value, so variation-selection adds little over Geneplore [4] (W); Sternberg, Perkins, Kronfeldner, Thagard object [2].
- **Structure-mapping (Gentner) at distance** [12][13]. Far examples raised mean novelty (d = .56) and quality variance (d = .64) but not mean or max quality (N = 153) [12] (M). Unprompted transfer is about 30% vs 75% with a hint; comparing two cases doubles it (M, brief 02); LLM mapping is brittle beyond easy cases (W, brief 02). Far pays when the problem is stuck [22], the schema is written [13], a conventional core is kept [15][18], and the goal is spread, not the mean [12].
- **Boden operational** [1]. Combinational: unfamiliar pairings of familiar ideas. Exploratory: moving through a style, including unvisited points. Transformational: altering or dropping a defining dimension (Kekulé turning the open-chain constraint into a ring); the more fundamental the altered constraint, the more shocking the ideas, and acceptance can lag decades (W). BACON-style programs were handed the questions; the human step was asking whether mathematical patterns exist (W). For us (my reading): the space is what the loop's operators (knob edits, component swaps, ports, compositions) reach; a diff is transformational if it changes a rule they assume (what a loss or step is, which data is seen when, how updates are computed).
- **Geneplore (Finke, Ward, Smith), least resistance, escapes** [4][34][35][8][36]. Generate, then explore [4]. The most accessible exemplars become starting points for novel ideas, even when task constraints weigh against them and when people are urged to be as creative as possible [34] (M). Examples are copied even when people are told to avoid them and can list the avoided features (4 experiments, N = 332) [8] (M); more examples and delay raise conformity, yet examples whose features covary unnaturally were rated more creative and conformity did not shrink total output [35] (M); a shared theme in examples leaks emergent properties into designs [36] (M). Escapes with evidence: decoupled features, fewer and earlier examples; not instructions.
- **Knoblich** [9]. Impasses break by relaxing constraints and decomposing chunks. Matchstick problems needing wider-scope relaxation were solved less often (C<B<A), tight chunks less than loose (D<A), and solving a hard type transferred to the next (N = 20, toy tasks) (M).
- **Problem finding** [14][2]. Of 31 art students, those who handled more of 27 objects and kept reformulating drew more original work and, per secondary accounts, stayed in art; follow-up timing is reported inconsistently [14] (W, 2nd). Simonton: problem finding is when the highest-prior idea fails; nothing bypasses mistakes at the edge of expertise [2] (W).
- **Koestler's bisociation**: fusing two unrelated "matrices of thought" [7]. No controlled test found, only the large-N shadows in section 3 (W, 2nd).

## 3. Base rates and predictors (observational)

- **Hao 2026** [23]: AI-using scientists get 3.02x papers and 4.84x citations; AI papers span a 4.63% narrower topic range (M).
- **Hill 2025** [18], 25.8M papers: hit rate 7.4% for the smallest pivots vs 2.2% for the largest; the largest-pivot decile is under-represented by 69% and 73% at the top 1% and 0.1%. High-pivot work has atypical links (49-58% vs 31%) but loses the conventional core (27-30% vs 79%) (M).
- **Shi and Evans 2023** [17]: surprise in content and context gives about 5x the odds of a top-10% paper; best cases are "expeditions", one field's scientists solving a familiar problem for a distant audience, not interdisciplinary teams or careers (M).
- **Liu 2021** [19]: 26,500 careers; hot streaks follow exploration then exploitation, neither alone; the exploited topic was less often the latest, most cited or most popular; effect modest (M).
- **Outsiders:** after 452 stars died early, non-collaborators' output rose about 8%, disproportionately highly cited, from newcomers applying other domains' ideas to mainstream questions [21] (M). In 166 contests with over 12,000 solvers, wins rose with self-rated solver-problem distance [22] (M).
- **Tails:** Wang, Veugelers and Stephan's "novelty paradox": 89% of 1.06M paper records make no new journal pair; novel papers have fatter tails on both sides and trail until year 4 [16] (M). Uzzi's four cells: 9.11 / 5.82 / 5.33 / 2.05 hits per 100 [15] (M). New combinations are less useful on average and more variable [27]; risky strategies earn more in expectation but not enough for the risk [28] (M). At Bing the top 2% of ideas gave 74.8% of gains [32] (M, 2nd). Evaluators score novel proposals, and ones near their expertise, lower (2,130 randomised pairs) [29] (M).
- **Incentives:** HHMI (tolerates early failure) vs matched NIH: +39% papers, +55% top-5%, +97% top-1%, and more flops [20] (M).
- **Breadth, "two cultures":** Campbell: people exposed to two or more cultures consider more hypotheses; creative people more often have unconventional backgrounds, diverse hobbies, several mentors, more in the arts than physical sciences [2] (W). Snow-style arts-science avocation studies not opened. BVSR matters more in low-consensus domains [2]; recipe tuning with cheap verifiers is high-consensus (my inference).

## 4. Negative results: lifts the average, not the top

Avoid-instructions and "be creative" fail [8][34]; in-context regeneration works, "creative outputs" asks are marginal (3 frontier models, 100 prompts x 8) [25] (M). Random stimuli null [2] (W, 2nd). Far examples: no max-quality lift [12]. Far pivots: fewer extreme hits [18]. Chatbots beat the human mean on alternate uses yet held the top score in only 3 comparisons [24] (M); LLMs beat the average human on the Divergent Association Task, not the top half [30] (M, 2nd). Brainstorming groups lose to nominal groups and training gains shrink after bias correction (S, brief 01).

## 5. What transfers to an LLM idea lane

Size: 15-20% of build slots (synthesis item 9). Ambitious = breaks a rule (script-judged "outside" the reachable space); specific = names the diagnostic, minimal diff and falsifier. Only outside cards count toward the quota; knob tweaks and ports count on the main line [1]. All items are hypotheses with no direct LLM test (W): run each as an arm against a plain "propose ambitious ideas" control at equal compute.

1. **Rule inventory, then break exactly one.** *Do:* list 8-10 rules of the recipe as testable sentences (equal token loss weight; i.i.d. batches seen once; fixed depth; one schedule; one update rule per tensor type), plus pairs of choices that always travel together; rank by dependents; drop, invert or decouple one; state what must change to stay trainable. Illustration (mine): drop equal token weight, weight by running per-token loss, keep an unweighted validation loss. *Why:* [1]; wider-scope constraints and tight chunks are relaxed less, and one relaxation primes the next [9]; decoupled features rated more creative [35] (W-M). *Measure:* outside-share; rule coverage (entropy over rule ids); hit rate by rule tightness.
2. **Conventional core, one imported mechanism, schema first.** *Do:* baseline unchanged plus one mechanism from an assigned far source, aimed at a stuck problem (3+ failed main-line attempts or an unexplained diagnostic). Write the shared schema first, then two instantiations, then three readings (property transfer, relation link, hybrid); keep the one that is diagnostic, plausible, informative. Illustration (mine): loss spikes at peak LR; import gain scheduling from control as per-layer step multipliers driven by update-norm spread. *Why:* [15][17][21][22] (M); pivots lose the core [18]; blend bottleneck [11]; analogical encoding [13]. *Measure:* hit rate in the 2x2 (core kept x atypical link), predicted best cell both; schema-lint pass rate.
3. **Anomaly first.** *Do:* each idea cites a logged surprise: a result contradicting the agent's pre-registered prediction (with probability) or a diagnostic breaking the current explanation; write three reformulations, take the one furthest from "lower val loss". Illustration (mine): a QK-norm port does nothing at 12 layers, so reframe where attention logits are the bottleneck. *Why:* [14][2] (W); BACON lacked the question [1]; brief 12: QK-norm, gating, MLA began from measured pathologies. *Measure:* anchored share; hit rate anchored vs not.
4. **Blind generation, logged surprise.** *Do:* stage A, 20 terse seeds with no feasibility or gain talk; stage B, fresh context, writes the card and states p(success). Prune on duplication, cost, testability, never predicted utility; inject no noise. *Why:* creative = low prior, useful, unpredicted [2][3] (W); random stimuli null [2]. *Measure:* surprise wins (won with stated p below median); c = (1-p_cluster)·win·(1-p_stated), p_cluster = share of seeds in the idea's cluster; share of wins a utility-pruned arm would drop.
5. **Explore, then exploit one seed.** *Do:* phase 1, 10+ shallow seeds across 5+ rule breaks, stop when new-cluster yield falls; phase 2, 3-5 variants of a seed with a positive mechanistic readout, not the newest, best-scored or most popular. *Why:* [19] (M). *Measure:* wins from seeds with 3+ variants vs singletons; explore-only vs explore-then-exploit.
6. **Divergence by construction.** *Do:* disjoint far-field slices per agent with that field's known ML tricks withheld; serial regeneration with the agent's own earlier seeds visible; hard dedupe before GPU; 25%+ of contexts on another model family; no "avoid X" wording, and no shared example themes. *Why:* [8][25][36]; same-provider reuse is 2.3x [11]; draws are correlated (about 5% of 4,000 LLM ideas unique [33]) (M). *Measure:* clusters per 100 seeds; cross-agent overlap; yield by family.
7. **Protected gate, tail metric.** *Do:* gate on a mechanistic readout (named diagnostic moves as predicted), allow two retunes of the idea's own knobs, exempt from the 0.005-nat margin until then; report P90 and P99 paired gains. *Why:* [20][16][28][29] (M). *Measure:* hits and flops per 100 builds; share of wins needing a retune.
8. **Idea card and scoreboard.** *Card:* rule broken; core kept; import and source; schema; anomaly; stated p; diagnostic and direction; minimal diff; falsifier. Raw-idea quality strongly predicts outcome (1 SD = about 50% higher sales rate) [31] (M). *Scoreboard:* lane yield (Wilson interval) vs the plain arm; outside-share; surprise-weighted hits; descendants (a lane win parenting 2+ later wins marks a new space). Rule of three: zero wins in 150 builds bounds yield below 2%, so size the pilot at 150+ (my arithmetic). If P99 and outside-share do not beat the plain arm, keep only dedupe and the protected gate.

## 6. Gaps

No verified LLM test of constraint relaxation, chunk decomposition or Geneplore escapes. Costello and Keane, Getzels and Csikszentmihalyi, Kohn 2011 and Sinatra 2016 read second-hand; arts-avocation studies and Fu 2013 near/far not opened. Human upper-tail data use citation hits and are observational; disruption indices are disputed (brief 08).

## Sources

[1] Boden 2009, AI Magazine 30(3): https://ojs.aaai.org/aimagazine/index.php/aimagazine/article/view/2254
[2] Simonton 2022, BVSR update: https://doi.org/10.1080/10400419.2022.2059919
[3] Simonton 2013, sightedness, JTPP 33(4): https://scottbarrykaufman.com/wp-content/uploads/2013/11/2013CreativitySightednessJTPP.pdf
[4] Gabora 2010 comment: https://arxiv.org/abs/1409.2210
[5] Jung 2015 equal odds: https://www.frontiersin.org/articles/10.3389/fpsyg.2015.00864/full
[6] Forthmann 2021 (cited in [2]): https://doi.org/10.1037/aca0000294
[7] Koestler, Act of Creation: https://en.wikipedia.org/wiki/The_Act_of_Creation
[8] Marsh, Ward, Landau 1999: https://link.springer.com/article/10.3758/BF03201216
[9] Knoblich 1999: https://www.kognition.uni-koeln.de/literature/Knoblich_etal_1999.pdf
[10] Conceptual combination (Costello-Keane 2000, Kohn 2011): https://en.wikipedia.org/wiki/Conceptual_combination
[11] Kombine: https://arxiv.org/abs/2509.21043
[12] Chan 2011: https://edrl.engr.wisc.edu/wp-content/uploads/sites/142/2022/02/2011-jmd-distancecommonness.pdf
[13] Gick-Holyoak 1983, Loewenstein 1999 (brief 02): https://www.gwern.net/doc/psychology/1983-gick.pdf ; https://www.kellogg.northwestern.edu/faculty/research/detail/1999/analogical-encoding-facilitates-knowledge-transfer-in-negotiation
[14] Getzels-Csikszentmihalyi (secondary): https://thereader.mitpress.mit.edu/the-1960s-art-school-experiment-that-redefined-creativity/
[15] Uzzi 2013: https://www.kellogg.northwestern.edu/faculty/uzzi/htm/papers/Science-2013-Uzzi-468-72.pdf
[16] Wang, Veugelers, Stephan: https://www.nber.org/papers/w22180
[17] Shi, Evans 2023: https://www.nature.com/articles/s41467-023-36741-4
[18] Hill 2025: https://www.kellogg.northwestern.edu/faculty/jones-ben/htm/The%20Pivot%20Penalty%20in%20Research.pdf
[19] Liu 2021: https://www.nature.com/articles/s41467-021-25477-8
[20] Azoulay, Graff Zivin, Manso 2011: https://www.nber.org/papers/w15466
[21] Azoulay, Fons-Rosen, Graff Zivin 2019: https://econ-papers.upf.edu/papers/1498.pdf
[22] Jeppesen, Lakhani 2010: https://dash.harvard.edu/server/api/core/bitstreams/7312037c-740f-6bd4-e053-0100007fdf3b/content
[23] Hao 2026: https://arxiv.org/html/2412.07727v4
[24] Koivisto, Grassini 2023: https://www.nature.com/articles/s41598-023-40858-3
[25] NoveltyBench: https://arxiv.org/abs/2504.05228
[26] Sinatra 2016: https://doi.org/10.1126/science.aaf5239
[27] Fleming 2001: https://ideas.repec.org/a/inm/ormnsc/v47y2001i1p117-132.html
[28] Foster, Rzhetsky, Evans: https://arxiv.org/abs/1302.6906
[29] Boudreau 2016: https://ideas.repec.org/a/inm/ormnsc/v62y2016i10p2765-2783.html
[30] Bellemare-Pepin 2026: https://doi.org/10.1038/s41598-025-25157-3
[31] Kornish, Ulrich 2014: https://funginstitute.berkeley.edu/wp-content/uploads/2015/01/jmr-252E12-252E0401_0.pdf
[32] Azevedo 2020 (brief 11): https://ideas.repec.org/a/ucp/jpolec/doi10.1086-710607.html
[33] Si 2024: https://arxiv.org/abs/2409.04109
[34] Ward et al. 2002: https://link.springer.com/article/10.3758/BF03195281
[35] Marsh, Landau, Hicks 1996: https://link.springer.com/article/10.3758/BF03201091
[36] Marsh, Bink, Hicks 1999: https://link.springer.com/article/10.3758/BF03211419
[37] Wisniewski 1997: https://link.springer.com/article/10.3758/BF03209392
