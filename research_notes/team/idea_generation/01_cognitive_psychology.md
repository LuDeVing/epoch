# 01 - Cognitive psychology and neuroscience of idea generation

Evidence brief for an LLM-driven idea loop (sketch, group, score, question, build). Compiled 2026-10-13. Section 2 lists 2024-2026 work newest first; section 3 holds the best-supported older findings.

**How to read it.** Every number was read from the cited abstract or full text; "summary" marks a secondary summary. Tags: MA = meta-analysis; MULTI = consistent across 3+ independent samples, not meta-analysed; 1X = single study; REV = review; PRE = preprint; SIM = simulation; LLM = language-model study, not human cognition. The web-search quota ran out mid-session, so 2026 coverage may have gaps.

## 1. Bottom line

1. Associative search over a flexible semantic network is the best-supported account, but semantic distance is a modest proxy: pooled r = .38 with creative-thinking scores (MA, 14 studies, N = 4,729, I^2 = 92%) [1], flattening above cosine distance ~0.9-1 [2]. Use it as a diversity signal, not a quality score.
2. Executive control helps through balance, not volume: the number of default-to-executive network switches predicts creative ability (not intelligence), with an inverted U (N = 2,433) [3]; working-memory and intelligence links are small to modest (MA r = .08 and .25) [4][5].
3. Levers with decent support: an undemanding break after real effort (MA d = .29) [6], walking (MA d = .93 for divergent thinking, wide CI) [7], imposed constraints (large, but narrow lab tasks) [8], independent generation before sharing [9][10].
4. Several popular levers shrank or failed to reproduce (section 2): N1 sleep "sweet spot", creativity training, episodic-specificity induction, serial-order slopes.
5. LLMs reproduce human failure modes and add homogeneity: fixation [11], cross-model sameness [12], saturation (4,000 ideas, ~200 unique) [13], weak self-judgement [14].

## 2. Newest first: 2024-2026

Tags: NEW = changes the picture; NO-REP = did not replicate; SHRANK = effect fell under scrutiny.

**2026**
- SHRANK: serial order is robust but tiny: at most 3.5% of variance over 3 prompts x 3 scorings, individual slopes unstable (ICC below .31) [15]; LLMs show it too (PRE) [16].
- SHRANK: episodic specificity induction (MA) gives small fluency and flexibility gains that weaken or vanish after bias correction, none on originality [17].
- NEW: novelty and appropriateness have largely separate neural bases (MA, 40 and 15 studies) [18]. Walking raises divergent but not convergent thinking (MA, 23 studies, d = .93 vs .16) [7]. In multi-agent ideation (LLM, ACL 2026 Findings), stronger aligned models show diminishing diversity and dense communication speeds convergence [19]. Remote sources help humans reliably; only the best LLMs benefit, and only at high distance (PRE) [20]. LLMs beat the average human on DAT, not the top half (LLM, 100,000 humans) [21]. Ensembled LLM scoring correlates r = .82 with human raters (>20,000 AUT responses) [22]. Human+AI beats human alone (44 studies, g = .54, larger for non-experts; PRE) [23].

**2025**
- NO-REP: the N1 sleep sweet spot (83% vs 31% awake vs 14% N2; n = 24/49/14; observational grouping; no direct replication found) [24]. A preregistered study (68 analysed, other task) found N2 helped (86% vs 56% awake) and N1 did not (p = .75) [25].
- NO-REP: break type (0-back, 2-back, meditation, none) did not change creative gains; mind wandering predicted gains only when the same prompt returned (preregistered) [26].
- NEW: across 10 samples (MULTI, N = 2,433), default-executive switch count predicts creativity, not intelligence, with an inverted U [3]. Creativity-exploration overlap (MA) sits in inhibitory-control regions, absent for divergent thinking [27]. Ratings plateau at distance ~0.9-1 (1X reanalysis, 3 tasks, ~10,000 responses) [2]. Network traits predicting real originality differ from those biasing self-rated originality (N = 106) [28]; in older adults creativity tracks preserved flexibility [29].
- LLM homogenisation: ChatGPT lowered group diversity in 37 of 45 comparisons (summary; a reply exists) [30][31]; models resemble each other more than people do (PRE) [12]; moderate AI use beats low or high (2 experiments, N = 139, 319) [32]; 3 chatbots beat 46 students on AUT and RAT [33]; ChatGPT-4o showed human-like fixation and struggled to tell original ideas from conventional ones (1X) [14].

**2024**
- SHRANK: creativity training, 0.53 SD falls to 0.29-0.32 after bias correction (169 studies) [34].
- NEW: AI ideas made stories better individually but more alike (1X) [35]. An AI image generator raised fixation and lowered variety and originality (1X, N = 60) [36]. A default+frontoparietal pattern predicts divergent thinking but out-of-sample correlations are modest (r = .35, .14, .15) [37].

## 3. Best-supported older findings

**3.1 Associative / semantic-distance account (Beaty, Benedek, Kenett)**
- REV (Beaty & Kenett): creativity as movement through semantic memory; free vs goal-directed association [38]. MA: memory-creativity r = .19 (79 studies, N = 12,846), driven by semantic memory and verbal fluency [39].
- MULTI: Kenett's network work: high-creative people have more flexible, robust semantic networks [40][41], echoed in 2025 samples [28][29].
- Measures: the pooled distance-creativity r = .38, but r = -.53 with elaboration [1]. SemDis latent score vs human ratings r = .91, .75, .45 across AUT samples, gameable with random words, length-confounded [42]; advice: many items, "be creative" instruction, max scoring [43]. DAT (name 10 unrelated words; N = 8,914) correlates with AUT and BAG about as well as those correlate with each other (1X) [44]. Forward flow predicts divergent thinking beyond intelligence (beta = .48, .42; n = 151, 150) [45], from [46]; contested [47].

**3.2 Serial order effect** (originality rises, fluency falls with position)
- Executive account (title only) [48]; distance rises slightly and linearly with position and higher fluid intelligence starts further out [49]; hemispheric alpha shifts during the effect in AUT but not in category fluency [50].

**3.3 Executive control vs spontaneous processes**
- Default (generative) and executive (evaluative) networks cooperate [51]; connectome model (N = 163) validated in independent samples [52]. Benedek et al. (latent-variable, 1X): creativity needs updating and inhibition, not shifting [53]; intelligence-creativity overlap r = .63 latent, 46% shared connections (N = 186) [54].
- Spontaneous: an undemanding task helped previously seen problems, linked to mind wandering [55].

**3.4 Incubation and sleep**
- MA: 117 studies, d = .29; larger for divergent tasks, longer preparation, undemanding fillers [56][6]. "Sleep inspires insight": about twice as many found the hidden rule (1X) [57]. Targeted dream incubation at sleep onset: N1 beat wake, successful incubation beat N1 alone (abstract only) [58].

**3.5 Constraints**
- REV: field findings fragmented and conflicting [59]. 1X: a required noun in a rhyme raised ratings 5.18 vs 4.29 (partial eta^2 = .53, n = 59), a self-chosen noun helped too (n = 46), gains carried over; author flags dose and transfer as untested [8]. Input constraints help only without time pressure [60].

**3.6 Quantity and quality (equal odds)**
- Equal-odds rule (more output, more hits; model in [61]). Fluency vs rated creativity r = .73 (N = 246) [62]; but Openness moderates it (N = 154) [63]; random-impact rule across scientific careers [64]. Process matters: individual-then-group gave more and better ideas and better discernment, while building on other people's ideas did not help (1X) [10]. People pick their best ideas fairly well (N = 226) [65], yet distance does not predict their picks [49].

**3.7 Expertise and fixation**
- Examples cause conformity (summary only) [66]; design-example MA: more example-bound ideas, fewer categories (summary only) [67]; restrictive vs expansive examples lower vs raise originality (N = 160) [68]. Einstellung in experts: eyes return to the first solution while they believe they are searching [69]. Nominal groups beat brainstorming groups on quantity and quality (MA) [9], mostly via production blocking [70]. Flexibility (categories) and persistence (depth) are separate routes to originality [71]. Expertise transfers to AI tools (50 artists) [72].

## 4. What would transfer to an LLM-driven idea loop

Human effect sizes are priors, not promises. Test each as an A/B at equal token budget, one fixed embedding model, and at least 3 judges from different model families.

1. **Independent first, then hybrid (SKETCH).** Isolated contexts for K sketchers; sharing opens only after pass 1, as inputs for new ideas, never "build on". Why: nominal beats interactive groups [9], blocking is the main cause [70], hybrid beat team work and building-on added nothing [10], dense agent communication collapses diversity [19]. Expect: more unique clusters per token. Measure: clusters (cosine similarity above 0.8 = duplicate, as in [13]) per 1k tokens, Vendi score, isolated vs shared arms.
2. **Partition knowledge, not just personas (SKETCH).** Give each sketcher a different retrieval slice plus ordinary-person personas and a "list assumptions, break one" step. Why: LLMs pool knowledge into one distribution; personas + chain-of-thought gave the highest diversity, above humans [11] (PRE); chain-of-thought alone helped [73]; simulated agents with less prior overlap gain more from exchange [74] (SIM). Expect: fewer duplicates (magnitude unknown; the PRE reports diversity above the human baseline). Measure: cross-agent vs within-agent distance (want cross at least within), duplicate rate.
3. **Banded distance injection and constraints (SKETCH).** Each sketcher draws 1-2 analogies/constraints from an embedding band (start 0.7-0.95 from the problem); inject noise as input seeds rather than hotter sampling. Why: plateau at ~0.9-1 [2]; constraints lifted a narrow task [8] but the field is mixed [59]; seed-conditioning matched temperature [75] (LLM). Expect: more novelty at equal appropriateness inside the band, none beyond. Measure: distance-bin dose-response on novelty x feasibility; 0/1/3 constraints.
4. **Taboo clusters plus a dual-pathway controller (GROUP).** After pass 1, cluster; pass centroids to pass 2 as "already covered"; a controller reads cluster count (flexibility) and depth per cluster (persistence) and either opens new clusters or deepens the best. Why: early outputs anchor humans [66] and LLMs [11][14]; two separate routes [71]; "just keep going" gains are tiny [15]. Expect: lower re-entry, modest originality gain. Measure: re-entry rate to taboo centroids; originality by position.
5. **Incubation as a decoupled second pass (SKETCH/BUILD).** After an effortful pass, park the problem, run an unscored low-demand free-association chain, then re-present the same problem in a cleared context with a few unresolved fragments. Why: overall d ~ .3, larger with undemanding fillers [6]; benefit tied to same-prompt reuse [26]. Expect: small in humans, unknown in LLMs. Measure: vs a matched-compute second independent pass (the key control).
6. **Stop rule plus diversity-aware shortlist (GROUP/SCORE).** Generate in batches until new-cluster yield falls below epsilon; shortlist with MMR/DPP across clusters. Why: quantity predicts quality in humans [62] but LLM over-generation saturates [13]. Expect: same unique output at lower cost (about 95% of generated ideas were duplicates in [13]). Measure: cumulative clusters vs tokens; best-of-K quality; shortlist Vendi score.
7. **Two-axis, cross-family judging; never self-judge (SCORE).** Score novelty and appropriateness separately with judges from different families, a gaming-screened, length-normalised distance, max-scoring, and ~100 human-rated anchors. Why: separable bases [18]; distance is length-confounded [42]; ensembles reach r ~ .82 [22]; LLMs misjudge originality [14] and the best LLM judge (53.3%) trailed human reviewers (56.1%) [13]. Also track forward flow/DAT per agent [45][44] as a health monitor, not a quality score. Measure: rank correlation with humans, inter-judge ICC, rate of "weird but empty" winners.
8. **QUESTION as alternating diverge/converge cycles (QUESTION).** Short hot bursts alternate with critic passes that ask questions (shared assumption? missing category? what falsifies it?), whose answers become next-burst constraints; tune the switch count. Why: network cooperation [51]; inverted-U in switching [3]; inhibition predicts creativity [53]; problem-finding is measurable (alpha .82, PRE) [76]. Expect: more viable novel ideas than one generate-then-filter pass. Measure: 0/1/2/4 switches at equal tokens; survival per cycle.
9. **BUILD in parallel before feedback (BUILD).** Prototype 3-5 cheap versions from different clusters, test on shared checks, refine survivors only. Why: parallel prototyping gave better, more diverse results [77]. Expect: better best-of-K. Measure: final test score and diversity vs serial refinement at equal compute.

**Gaps.** Titles or summaries only: [48], [30], [66], [67], [58]. I found no direct LLM test for mechanisms 5, 8 and 9; treat them as hypotheses. Not covered: brain stimulation, mood, psychedelics.

## Sources

[1] Li 2023 semantic-distance MA: https://journal.psych.ac.cn/xlkxjz/EN/10.3724/SP.J.1042.2023.00519
[2] Orwig 2025 distance plateau: https://2025.ccneuro.org/abstract_pdf/Orwig_2025_A_sweet_spot_creative_ideation_Non-linear.pdf
[3] Chen 2025 network switching: https://doi.org/10.1038/s42003-025-07470-9
[4] Gong 2023 working-memory MA: https://doi.org/10.3390/jintelligence11010015
[5] Gerwig 2021 intelligence MA: https://doi.org/10.3390/jintelligence9020023
[6] Gilhooly 2016 incubation review: https://pmc.ncbi.nlm.nih.gov/articles/PMC4956660/
[7] Thabane 2026 walking MA: https://doi.org/10.1371/journal.pone.0347878
[8] Haught-Tromp 2017 constraints: https://www.rider.edu/sites/default/files/docs/tromp_haught-tromp_PACA_2016.pdf
[9] Mullen 1991 brainstorming MA: https://doi.org/10.1207/s15324834basp1201_1
[10] Girotra 2010 best idea: https://doi.org/10.1287/mnsc.1090.1144
[11] Deng 2026 LLM diversity (PRE): https://arxiv.org/abs/2602.20408
[12] Wenger 2025 LLM homogeneity (PRE): https://arxiv.org/abs/2501.19361
[13] Si 2024 LLM research ideas (PRE): https://arxiv.org/abs/2409.04109
[14] Desdevises 2025 ChatGPT egg task: https://doi.org/10.3389/fpsyg.2025.1628486
[15] Barbot 2026 serial order: https://doi.org/10.3390/jintelligence14060100
[16] Gilhooly 2026 LLM serial order (PRE): https://doi.org/10.20944/preprints202609.2250.v1
[17] Tomas 2026 ESI MA: https://doi.org/10.3758/s13423-026-02859-x
[18] Lin 2026 novelty-appropriateness MA: https://doi.org/10.1007/s00429-026-03127-3
[19] Chen 2026 diversity collapse (PRE): https://arxiv.org/abs/2604.18005
[20] Liu 2026 cross-domain (PRE): https://arxiv.org/abs/2603.19087
[21] Bellemare-Pepin 2026 humans vs LLMs: https://doi.org/10.1038/s41598-025-25157-3
[22] Organisciak 2026 LLM scoring: https://doi.org/10.3758/s13428-026-03058-1
[23] Yao 2026 AI creativity MA (PRE): https://doi.org/10.31234/osf.io/jy3ba_v2
[24] Lacaux 2021 sleep onset: https://pmc.ncbi.nlm.nih.gov/articles/PMC8654287/
[25] Lowe 2025 N2 sleep: https://doi.org/10.1371/journal.pbio.3003185
[26] McDaniel 2025 incubation: https://doi.org/10.1038/s41598-025-09736-y
[27] Liu 2025 exploration MA: https://doi.org/10.1016/j.neubiorev.2025.106158
[28] Skurnik 2025 networks and evaluation: https://doi.org/10.1186/s40359-025-03124-x
[29] Campidelli 2025 ageing networks: https://doi.org/10.1016/j.cognition.2025.106318
[30] Meincke 2025 summary page: https://mackinstitute.wharton.upenn.edu/2025/new-in-nature-chatgpt-decreases-idea-diversity-in-brainstorming/
[31] Lee 2025 reply: https://doi.org/10.1038/s41562-025-02195-5
[32] Huang 2025 Goldilocks: https://doi.org/10.1037/xge0001838
[33] Arora 2025 AI vs students: https://doi.org/10.1038/s41598-025-21398-4
[34] Sio 2024 training MA: https://doi.org/10.1037/bul0000432
[35] Doshi 2024 AI and diversity: https://doi.org/10.1126/sciadv.adn5290
[36] Wadinambiarachchi 2024 fixation (PRE): https://arxiv.org/abs/2403.11164
[37] Liu 2024 neural signatures: https://pmc.ncbi.nlm.nih.gov/articles/PMC11473644/
[38] Beaty 2023 associative review: https://doi.org/10.1016/j.tics.2023.04.004
[39] Gerver 2023 memory MA: https://doi.org/10.3758/s13423-023-02303-4
[40] Kenett 2014 networks: https://pmc.ncbi.nlm.nih.gov/articles/PMC4051268/
[41] Kenett 2018 percolation: https://pmc.ncbi.nlm.nih.gov/articles/PMC5798367/
[42] Beaty 2021 SemDis: https://pmc.ncbi.nlm.nih.gov/articles/PMC8062332/
[43] Beaty 2022 AUT recommendations: https://doi.org/10.1080/10400419.2022.2025720
[44] Olson 2021 DAT: https://pmc.ncbi.nlm.nih.gov/articles/PMC8237676/
[45] Beaty 2021 forward flow: https://doi.org/10.1016/j.tsc.2021.100859
[46] Gray 2019 forward flow: https://doi.org/10.1037/amp0000391
[47] Kenett 2020 forward-flow reply: https://cris.iucc.ac.il/en/publications/clarifying-what-forward-flow-is-and-isnt-reply-to-rossiter-2020/
[48] Beaty 2012 serial order (title only): https://doi.org/10.1037/a0029171
[49] Hass 2017 distance dynamics: https://doi.org/10.3758/s13421-016-0659-y
[50] Kraus 2019 EEG serial order: https://doi.org/10.1016/j.biopsycho.2019.04.003
[51] Beaty 2016 network review: https://pmc.ncbi.nlm.nih.gov/articles/PMC4724474/
[52] Beaty 2018 connectome: https://pmc.ncbi.nlm.nih.gov/articles/PMC5798342/
[53] Benedek 2014 executive functions: https://doi.org/10.1016/j.intell.2014.05.007
[54] Frith 2021 intelligence-creativity: https://doi.org/10.1037/xge0000958
[55] Baird 2012 mind wandering: https://doi.org/10.1177/0956797612446024
[56] Sio 2009 incubation MA: https://doi.org/10.1037/a0014212
[57] Wagner 2004 sleep insight: https://doi.org/10.1038/nature02223
[58] Horowitz 2023 dream incubation: https://doi.org/10.1038/s41598-023-31361-w
[59] Acar 2019 constraints review: https://doi.org/10.1177/0149206318805832
[60] Moreau 2005 constraints: https://doi.org/10.1086/429597
[61] Simonton 1997 equal-odds model: https://doi.org/10.1037/0033-295X.104.1.66
[62] Jung 2015 equal odds: https://doi.org/10.3389/fpsyg.2015.00864
[63] Friis-Olivarius 2019 equal odds: https://pmc.ncbi.nlm.nih.gov/articles/PMC6409333/
[64] Sinatra 2016 random impact: https://doi.org/10.1126/science.aaf5239
[65] Silvia 2008 discernment: https://doi.org/10.1037/1931-3896.2.3.139
[66] Smith 1993 example conformity (summary): https://doi.org/10.3758/BF03202751
[67] Sio 2015 examples MA (summary): https://doi.org/10.1016/j.destud.2015.04.004
[68] Examples and originality N=160: https://doi.org/10.1002/jocb.37
[69] Bilalic 2008 Einstellung: https://doi.org/10.1016/j.cognition.2008.05.005
[70] Diehl 1987 blocking: https://doi.org/10.1037/0022-3514.53.3.497
[71] Nijstad 2010 dual pathway: https://doi.org/10.1080/10463281003765323
[72] Eisenmann 2025 expertise and AI (PRE): https://arxiv.org/abs/2501.12374
[73] Meincke 2024 prompting (PRE): https://arxiv.org/abs/2402.01727
[74] Ahmed 2026 simulation (PRE): https://arxiv.org/abs/2602.03068
[75] Nagarajan 2025 seed-conditioning: https://arxiv.org/abs/2504.15266
[76] Alabbasi 2024 problem generation (PRE): https://doi.org/10.31234/osf.io/wkzhq
[77] Dow 2010 parallel prototyping: https://doi.org/10.1145/1879831.1879836
