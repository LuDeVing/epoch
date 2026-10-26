# Novelty and atypicality: deep document

*Subfield E15.02 of science of science. Built from evidence_a-d.jsonl (ids a01-a28, b01-b29, c01-c26, d01-d18), claims.jsonl (K01-K32) and critique.md in this folder. Written for the single-agent thinking schema (`research_notes/single_agent/SCHEMA.md`, v0.2). Almost all human-science evidence here is bibliometric and correlational. No human study tests an intervention. LLM studies are mostly judged by LLM or embedding scorers, which this document shows are unreliable. Read every number with that in mind.*

---

## 1. What it is

Two ideas about "new" work are often confused. This subfield separates them.

**Atypicality (novelty by combination).** A work is atypical if it joins things that are rarely joined. The founding measure (Uzzi et al. 2013) looks at the journals a paper cites. It asks how often each pair of cited journals appears together, compared with chance. Rare pairs score as atypical. This is a measure of distance between the parts that were combined.

**Disruption (novelty by displacement).** A work is disruptive if later papers cite it instead of the work it builds on. The index is called D or CD. This is a measure of replacement of an incumbent.

The key paper for this subfield is Li, Lin and Wu (2025, arXiv 2506.15959). Across about 41 million articles, atypicality and disruption correlate negatively in every discipline, period and team-size panel. Their reading: atypical work extends known ideas into new topics. Disruptive work replaces a dominant idea inside its own topic. A "microwave TV" may be creative, but it will not replace either appliance.

**Why this matters for our agent.** The agent has one decision that depends on this: when it needs a new answer, does it (a) combine something distant with a conventional core, or (b) name the incumbent answer and replace it with something that does the same job better? These are two operators with different triggers and different checks. A single "be novel" instruction mixes them.

**Honest limits up front.**
- Both metrics are weak or contested as measures of "good idea". Experts do not agree with either one strongly (K02, K22).
- The disruption index is unstable and construct-sensitive (K06, established).
- The two key human results from overlapping authors (Lin 2022: atypical papers disrupt more; Li 2025: they disrupt less) are not reconciled (K05).
- The LLM evidence on novelty is mostly scored by LLM judges, which are near chance (K17, established).
- No study tests the Uzzi mix (conventional core plus a distant add-on) with an LLM against an executable verifier (K29, gap 1 open).

---

## 2. History and theories in depth

### 2.1 Combination theory of novelty (Uzzi, 2013)

The idea that new work recombines old parts is old (Schumpeter, Boden's combinatorial creativity). Uzzi, Mukherjee, Stringer and Jones (2013, *Science*) gave it a measurable form (a01, a02, b01).

Method. For each pair of journals, count how often the pair is co-cited. Compare with a null built by randomly switching citation links while keeping each paper's citation counts. The z-score of the pair says how typical it is. z below 0 means rarer than chance (atypical). z above 0 means common (conventional). For each paper, take two summary numbers: the median z (conventionality) and the 10th percentile z (tail novelty).

Scale: 17.9 million Web of Science papers, 15,613 journals, over 122 million possible journal pairs.

Result: hits (top 5% of citations at 8 years) are most likely for papers that are conventional at the median and have an atypical tail. This is the "mix" result. Section 3 has the numbers.

Prevalence: most papers are very conventional. Fewer than 4% have a median z below 0 (3.54% in the 1980s, 2.67% in the 1990s). But about 40.8% (1980s) and 40.7% (1990s) have a 10th percentile z below 0. So a small atypical tail is common; a mostly atypical paper is rare (b02).

Team result (a03, b03): teams are 37.7% more likely than solo authors to put a novel combination inside a conventional base.

### 2.2 Variants and rival measures of combination novelty

- **Lee, Walsh, Wang (2015)** (a04) adapted the score to a per-paper novelty measure. Team size has an inverted-U with novelty. The size effect goes away once field variety or task variety is controlled. Field variety vs novelty r = .25.
- **Wang, Veugelers, Stephan (2017)** (a05) used a different measure: the first-ever co-citation of two journals, weighted by how hard the combination is. 773,311 WoS articles from 2001, 14-year window. Highly novel papers are riskier and pay later.
- **Bornmann, Tekles, Zhang, Ye (2019)** (a06) tested both measures against expert tags on F1000Prime. The Uzzi/Lee score mostly agrees with experts. The Wang score mostly does not. Measure choice changes the answer (K02, contested).
- **Shibayama, Yin, Matsumoto (2021)** (a08) made a text version: embed the titles of cited references, take pairwise distances, use a high quantile. It is the cheapest analogue for an agent.
- **Lin, Evans, Wu (2022)** (a10) trained word2vec on co-cited journal sequences. The inner product of two journal vectors correlates 0.74 with the Uzzi z-score. Novelty becomes distance in a learned space that moves as yesterday's novelty becomes convention.
- **Wang (2024)** (c16, b29) used language-model surprisal on the text as a content-based novelty score.
- **Yu and Romero (2024)** (b18) looked at unusual combinations of datasets (not journals).

### 2.3 Disruption theory (Funk and Owen-Smith 2017; Wu, Wang, Evans 2019)

The CD index asks: of the papers that cite a focal paper, how many also cite its references? If few do, the focal paper has replaced its sources. D is near +1 if later work cites the focal paper alone, near -1 if later work cites it together with its references (a28, second-hand; not opened).

Wu et al. (2019) used it to claim that small teams disrupt and large teams develop. This was the first big public result and has since been disputed (section 5).

Park, Leahey and Funk (2023) (a16) used it to claim that papers and patents have become less disruptive over time. Also disputed.

### 2.4 The split: Li, Lin, Wu (2025)

Two earlier papers by the same group set the stage.

- **Lin, Li, Wu (2025)** (a13, a14, b26) rewrote D as the product of a local displacement term and a knowledge-burden term. D is mostly decided by whether a paper beats its single most-cited reference. Reference citations follow a Zipf law, so the top reference dominates. Conclusion: D is a relative measure against a named incumbent.
- **Li, Lin, Wu (2025)** (a11, a12, b04, c01) then asked how atypicality (recombination) relates to D. Negative everywhere. They add a mechanism, functional equivalence (section 4.3), and an LLM test of theory-versus-method.

The group that proposed D wrote the paper that explains it. Treat the mechanism as single-source (K04).

### 2.5 Critiques of the disruption index

A series of papers attack D from different sides (b09-b16, b24, b25, a17, a18). They are summarised in section 5. The takeaway for theory: D is a measure of citation behaviour. It is not a measure of innovation. It needs about ten years to settle. It depends on reference-list length.

### 2.6 Risk and reward of strategy (Foster, Rzhetsky, Evans 2015)

A parallel line asks whether risky moves pay. Foster et al. (b06, d09) classed biomedical chemistry statements as repeat, new, or jump. Risky moves earn more on average, not enough to cover the extra failure risk. Prize winners gamble more. This gives the only break-even calculation in the subfield (section 3).

### 2.7 Idea generation with LLMs (2020-2026)

Once LLMs could write research ideas, the field turned to three questions.
1. Are LLM ideas more novel than human ideas? (Si et al. 2024: yes by blind review; Si et al. 2025: not after execution.)
2. Can recombination or retrieval pipelines raise novelty? (SciMON, Nova, Deep Ideation, Scideator, analogy retrieval. Yes by their own judges.)
3. Can an LLM judge novelty? (No: RINoBench, Think-Probe-Respond, RQ-Bench, Gupta and Pruthi.)

A fourth strand is about collective homogeneity: LLMs are as original as people one at a time, but alike as a group (Wenger and Kenett; NoveltyBench; Artificial Hivemind).

---

## 3. Core findings with exact numbers

Status key: **E** established (two or more independent sources, per claims.jsonl); **S** single-source; **C** contested.

### 3.1 Human science

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Hits come from a conventional core with an atypical tail | Hit = top 5% citations at 8 years, WoS 1990-2000. Hits per 100: conventional + tail-novel 9.11; conventional only 5.82; tail-novel only 5.33; neither 2.05; background 5. P<0.00001. Same pattern in 243 fields and for top 1% and top 10% | Uzzi et al. 2013 (a01, a02, b01) | S (K01) |
| Most papers are conventional; atypical tails are common | Median z<0 in 3.54% (1980s), 2.67% (1990s). 10th-percentile z<0 in 40.8% and 40.7%. 40.1% of interdisciplinary journal pairs were novel. Peak impact at 85th-95th percentile of median conventionality | Uzzi 2013 (b01, b02) | S |
| Teams put atypical parts into a conventional base | Teams 37.7% more likely than solo authors | Uzzi 2013 (a03) | S (K25) |
| Team size and novelty: inverted U; goes away with variety controlled | Field variety vs novelty r=.25 (fine), .26 (coarse); task variety r=.18. 9,428 cases in full-sample check; survey respondents about 0.1 SD less novel | Lee, Walsh, Wang 2015 (a04) | S (K25) |
| Highly novel papers: riskier, later payoff | 773,311 WoS articles (2001), 14 years. Odds of top 1%: +39.82%. Odds of being cited by big hits: +26.20%. Cited by 16.56% more subject categories. Odds of top 10%: +16.80%; odds of bottom 10%: +16.76% | Wang, Veugelers, Stephan 2017 (a05) | S (K10) |
| Uzzi score tracks expert "new finding"; Wang score does not | Per 1 SD of U, "new finding" tag count +7.47%. F1000Prime logistic models n=17,887; 14,345; 12,697; U coefficients 0.59-2.84 (odds up over 100% per SD); W mostly negative. Spearman U-W: -0.05 to 0.1 | Bornmann et al. 2019 (a06) | C (K02) |
| Text embedding of cited titles works as a modest novelty proxy | 321 biomedical respondents; Novel1T00 r=.170 (p<.01) with self-reported newness. Odds of top 1% rise with quantile q. Measures from the focal document's own text failed | Shibayama et al. 2021 (a08) | S (K21) |
| Atypicality has a learnable embedding form | z-score vs journal-embedding inner product r=0.74. 50 dims; 2,429 journals (1970 space), 8,009 (2000 space) | Lin, Evans, Wu 2022 (a10) | S |
| Atypical papers are nearly twice as likely to disrupt, but the overall link is slightly negative | 61% vs 36% disruptive. Highly atypical papers 2.3% of sample (3.9% in 1970 to 1.4% in 2000). Pearson r typicality vs D = -0.05 (p<0.001). Sleeping-beauty index vs atypicality r=0.08. MAG 87,860,684 articles, 35,431,832 usable. D reaches 80% of final in about 10 years. Stronger in CS and engineering | Lin, Evans, Wu 2022 (a09, b05, d11) | C (K05) |
| Atypicality and disruption correlate negatively | About 40.9M articles 1965-2020 (40,935,251), OpenAlex. Top 5% atypical: A>22.9. Top 5% displacing: D>0.04. Negative in every discipline, period, team-size panel. Coefficient not stated in the text read | Li, Lin, Wu 2025 (a11, b04, c01, d12) | E (K03) |
| Theory-type innovations are displaced more slowly than method-type | Llama-3.1-70B-Instruct zero-shot labelled 50,147 highly cited D>0 papers. Probability of theory-type falls as the gap to the reference grows. Prompt variants said to give the same trend (no numbers) | Li, Lin, Wu 2025 (a11, c01) | S |
| Disruption is displacement of the top reference | Zipf fit a=1.89, b=0.60 (1,000 OpenAlex papers). 22M papers with 10+ citations: 65% dp<0, 32% dp>0, 3% zero. 98.9% have bp>1; median bp=119. 38% of 42M papers D>0; median D about -0.0001. Expert survey: 20 scholars, 190 responses; nominated disruptive mean D=0.21 (top 1%); consolidating -0.011; AUC 0.83. High-D papers share a field with top reference at 0.52 vs 0.014 chance (37x; 49,077 papers) | Lin, Li, Wu 2025 (a13, a14, b26) | S |
| Risky moves pay more on average but not enough | Repeat 85.8% of statements; new+jump 14.2%; jumps 1.8%; new bridges 12.4%. Mean citations 8.38 repeat, 11.00 new, 12.90 jump (1983-2002). Break-even: p(new)=0.76 p(repeat); p(jump)=0.65 p(repeat). Surprisal explains 29.2% of variation in mean citations (R2 = 0.2916). A tenfold rarer strategy: +2.26 citations. 137 prizes | Foster et al. 2015 (b06, d09) | S (K09) |
| Generalization is rising, extension falling | Top generalizing works 84.0% farther in reference space, 15.5% farther in semantic space, 114.0% more likely to get cross-domain citations. In one subset D fell 57.6% (0.059 to 0.025, 1950-1990) while the extension index rose 0.536 to 0.762 | Fang and Evans 2025 (b17) | S (K24) |
| Unusual dataset combinations: citation edge mostly topic | About 15% more citations at 3, 5, 10 years; 1-4% left after topic atypicality is controlled. 30,000+ social science papers, 5,000+ ICPSR datasets | Yu and Romero 2024 (b18) | S (K11) |
| Ideas for landmark papers rarely come from the cited literature | Interviews with authors of landmark scientometrics papers; small set | Tahamtan and Bornmann 2018 (a07) | S (K23) |
| Delayed payoff, three ways | D needs about 10 years (DNA paper D 0.2 in 1953, nearly 0.8 ten years later, 0.96 by 2018). A 5-year window cannot see a 2017 shift until 2022-Q2 | Lin 2022; Ustyuzhanin 2026 (d18, d03) | S (K10) |
| A content signal for stance toward the named incumbent detects displacement early | Signal crosses a pre-registered threshold in 2016-Q1; CD5 sees the 2017 breakthrough only in 2022-Q2 (25 quarters). Kappa 0.83 on human-recoverable items | Ustyuzhanin et al. 2026 (d03) | S (K31) |
| Independent topic-cluster split into bridges and redirectors | 36,113 ICLR papers; 113 clusters. Initiators 8.5%, bridges 9.8%, within-topic redirectors 7.1%, misaligned 3.1%; union 22.2%. Bridges precede 11.52x cross-topic citation flow; initiators 7.55x topic share growth | Huang 2026 (d13, c18) | S (K04 partial) |

### 3.2 Measure problems and the decline debate

| Finding | Numbers | Source | Status |
|---|---|---|---|
| D is unstable and construct-sensitive | 10-year window gives over 80% agreement with final class; 3-year unstable; 30+ references stabilise 1-3 years faster. Country shares of D>0: Iraq 57.5%, Nigeria 56%, India 34.3%, China 26.9%. A paper with 3 citing papers can reach D=1/3 | Chen et al. 2025 (b07); Larregue and Gingras 2026 (a18, b25); Liang et al. 2020 (b09) | E (K06) |
| D does not match expert "new finding" tags | 120,179 F1000Prime papers; 45 Poisson regressions. "New finding" coefficients negative (-2.71, -0.62, -2.13, -2.13). "Technical advance" positive (6.72-20.65). "Refutation" negative (-9.28 to -14.83) | Bornmann et al. 2020 (b10) | E (K22) |
| D is a weak detector of famous breakthroughs | AUC of the standard index: Turing 0.79, Nobel 0.73, Lasker 0.60, Test of Time 0.55, Physical Review Milestones 0.40, Science Breakthrough of the Year 0.26. Authors' one-reference measure 0.94-0.98 | Huang and Xie 2026 (b24, c25) | E (K08) |
| "Science is getting less disruptive" | CD5 down 91.9% (social sciences, 0.52 to 0.04) to 100% (physical sciences, 0.36 to 0). Patents -78.7% to -91.5%. 25M papers, 3.5M patents. Title word diversity -76.5% to -88% | Park, Leahey, Funk 2023 (a16) | C (K07) |
| The decline is a data artefact (reply: no) | 972,161 papers and 142,362 patents with CD5=1 were hidden by a plotting bug. 97% of CD5=1 papers and 78% of patents have zero recorded references. Of 100 each checked, 93% of papers and 98% of patents do cite in the PDF. Zero-reference dummy lifts R2 from 0.15 to 0.95 (papers), 0.10 to 0.52 (patents) | Holst et al. 2024 (b11, c24) | C (K07) |
| Park reply | Using Holst's data the decline persists. About 20% of Holst's sample is non-research content: 2.8M editorials/obituaries/comments, 1.5M books and proceedings, 254,000 reviews. Non-research share fell 40% to 8% | Park et al. 2025/26 (a17) | C |
| Citation inflation | Citations grow 5.1% a year (0.033 paper + 0.018 reference growth); doubling every 13.6 years | Petersen et al. 2023 (b12) | C |
| Citation-weighted index is flat then up | Near neutral for 50 years, modest rise since 2000 | Bentley et al. 2023 (b14) | C |
| Patent decline is mostly truncation | 88% of the 1980-2010 drop in mean CD explained by truncated backward citations | Macher et al. 2026 (b15) | C |
| Review of 105 studies | Most report decline in papers, patents, products, law, music, art | Wu et al. 2026 (b16) | C |
| Small-team advantage depends on window and reference length | Flips sign at 5-year window; reverses when reference counts equalised. Team effect negative to positive at 8+ coauthors (PNAS vs PNAS Plus quasi-experiment). Large teams more disruptive in 4 domains and every decade 1970s-2010s (60M publications) | Lin 2025 (a15, b08); Petersen 2024 (b13); Huang and Xie 2026 (b24, c25) | E (K08) |

### 3.3 LLM and AI studies

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Blind experts rate LLM ideas more novel than expert human ideas | Novelty 1-10: human 4.84, AI 5.64, AI + human rerank 5.81 (p<0.05; Bonferroni p<0.01). 49 ideas per condition, 79 reviewers, 298 unique reviews, 7 NLP topics. Novelty vs overall r=0.725; feasibility vs overall r<0.1 | Si, Yang, Hashimoto 2024 (a21, b19, c02) | E (K16, with Si 2025) |
| After execution the edge goes | 43 experts, 100+ hours each. Human change: novelty -0.010, excitement +0.078, effectiveness -0.052. AI drops: 1.049, 1.760, 1.879 (p<0.05 FDR). Post-execution excitement AI 3.896 vs human 4.482 (FDR p=0.004); effectiveness 4.125 vs 4.782. Novelty after execution 4.93 vs 4.73, p=0.21, not significant (critique correction) | Si, Hashimoto, Yang 2025 (a22, b21, c03) | E (K16) |
| Over-generation hits duplicates | About 200 of 4,000 seed ideas per topic (5%) are non-duplicates at cosine 0.8 (all-MiniLM-L6-v2) | Si 2024 (a21, b20, c04) | S (K15) |
| LLM judges rank ideas near chance | Best (Claude-3.5 pairwise) 53.3%; GPT-4o direct 50.0%; GPT-4o pairwise 45.0%; Claude-3.5 direct 51.7%; AI Scientist reviewer 43.3%. Human-human 56.1% (NeurIPS 2021: 66.0%; ICLR 2024: 71.9%) | Si 2024 (b20, c04) | E (K17) |
| Frontier LLMs fail 5-class novelty rating | 1,381 expert-rated ideas. Macro-F1 12-17 (GPT-5 17.2, o3 16.2). Class "not novel" F1 = 0.0 for every model. Predictions bunch at classes 3-4. MAE about 1 | Schopf and Farber 2026 (b22, c06) | E (K17) |
| Medium-novelty bias in six frontier models | Baseline macro-F1: Gemini 2.5 Pro 15.6, Gemini 3 Pro 15.3, Sonnet 4.5 15.5, Opus 4.5 17.1, GPT-5 mini 16.2, GPT-5.4 15.1. Probe method +22.30% (open models only) | Schopf et al. 2026 (b23, c07) | E (K17) |
| Novelty mirage | gpt-5.5 non-obviousness win rate 27.2% standalone, 49.1% comparative. Humans favour author-anchored questions 78% and 56%; LLM judges favour gpt-5.5 outputs 82% and 52%. Agreement within humans 60%, within LLMs 52%, human-LLM as low as 22% | Sinhahajari et al. 2026 (a26) | E (K17) |
| Disguised copying in LLM proposals | 13 experts, 50 documents (36 proposals + 14 exemplars). 14.0% score 5 (direct copy), 10.0% score 4: 24% plagiarism. Automated checkers missed it | Gupta and Pruthi 2025 (c05) | S (K18) |
| Facet-level retrieval finds known overlap, embedding filtering does not | 58 ideas with known overlap. Complete system 89.66%; relevance re-ranker 13.79%; embedding filter only 10.34%; snippet 8.62%; keyword 5.17%. Zero-shot classifier acc 0.68, F1 0.65 (AI Scientist prompt 0.47/0.44). Creativity Support Index 70.5 vs 61.0, p<.01 | Radensky et al. 2026 Scideator (c09, d14) | S (K18) |
| Retrieve-compare-revise loop | k=20 nearest neighbours. First novelty iteration: 88.9% of ideas substantially different; 55.6% judged more novel. Six NLP raters, 50 instances | Wang et al. 2024 SciMON (c10) | E (K14) |
| Planned outside retrieval | 3.4x unique novel ideas; 2.5x top-rated ideas. Without planning: 42.4 at step 2, 44.1 at step 3; without planning and retrieval 25.3, 30.6, 31.35. 170 seed papers | Hu et al. 2024 Nova (b28, c11) | E (K14) |
| Explore-expand-evolve over a concept network | +10.67% over best baseline (DL 10.92, NLP 9.48, CV 13.91) | Zhao et al. 2025 Deep Ideation (c12) | E (K14) |
| Abstract-then-recombine | 87 OAG-Bench papers; similarity to real paper +7-10% over direct generation; key-mechanism similarity 0.85-0.95 vs 0.7-0.8 | Gu et al. 2025 (a25, c13) | E (K14) |
| Multi-agent iterative search | Diversity 0.898 vs 0.867 vs 0.680; novelty 0.133 vs 0.107 vs 0.067; high-score ratio 0.184 vs 0.026 vs 0.013 | Chen and Zhang 2026 (c14) | E (K14) |
| Cross-domain analogy retrieval lifts diversity | Diversity +90% to +173%. Novel share: Baseline / cross-domain baseline / analogy retrieval: Claude 1.6 / 21.6 / 50.4%; GPT 9.0 / 28.2 / 58.8%; Gemini 8.9 / 37.8 / 68.9%. 50 research problems. Humans judged AR solutions more novel 78% of the time (kappa 0.445), but "reasonable" 67% vs 86% for the cross-domain baseline | Shen, Druckmann, Zou 2026 (a24) | S (K13) |
| Distance threshold for cross-domain mapping | 140 human designers, 7 LLMs, 1,002 raters. Pooled beta=0.36 (p<.001). o3 and Claude-Sonnet-4: all pairs beta=0.02 (p=.64); top 50% most distant 0.12 (p=.029); top 10% 0.24 (p=.024). Closest 20% dropped closes the LLM gap. Originality vs feasibility rho=-0.74; originality vs utility -0.08; investment-worthiness driven by utility (0.71) not originality (0.23) | Liu et al. 2026 (a23, d10) | S (K12) |
| Forced distance in code costs correctness | 199 Codeforces problems. GPT-4 pass@1 by ban step: 16.1, 11.6, 7.1, 5.2, 2.3, 2.1 (%). Divergent creativity 4.5 to 15.3%. Convergent creativity 16.2 down to 0.0. NeoGauge max 1.4. Only MCTS lifts divergent creativity; none lifts NeoGauge much | Lu et al. 2025 (d04) | S (K26) |
| Math: prior solutions cut novelty, difficulty raises novel share | Gemini-1.5-Pro correctness 69.92%, novelty ratio 66.94%. AMC 8 to USAMO/IMO: correctness 71.80% to about 35%; novelty-to-correctness 55.39% to 83.01%. LLM-judged | Ye et al. 2024 CreativeMath (d05) | S (K27) |
| Individual originality equal, collective diversity lower | 22 LLMs. Originality LLM vs human: AUT 0.711 vs 0.696; FF 0.603 vs 0.637; DAT 0.801 vs 0.753. Variability significantly lower for LLMs on all three | Wenger and Kenett 2025 (c21) | E (K19) |
| Mode collapse across models | Fewer than 3 distinct answers in 10 samples. Same-model similarity above 0.8 in 79% of cases; across models 71-82%. 26K queries, 31,250 annotations, 70+ models. Min-p with T=2.0 still above 0.8 | Zhang et al. 2025 NoveltyBench (d06); Jiang et al. 2025 Artificial Hivemind (d07) | E (K19) |
| Prompt-level diversity fixes | In-context regeneration restores about human diversity (GPT-4o, Gemini 2.0 Pro exceed human cumulative utility). Verbalized Sampling diversity 1.6-2.1x; synthetic-math downstream accuracy 32.8 baseline, 30.6 direct, 33.7 sequence, 34.3 multi-turn, 36.1 VS-Standard, 37.5 VS-CoT | NoveltyBench (d06); Zhang et al. 2026 (d08) | E (K28) |
| Distance buys diversity, costs relevance | 100 ideas per arm. Diversity: Top 0.21, Random 0.41, Si 0.29, Yu 0.29. Relevance: Top 0.11, Random 0.05, Si 0.28, Yu 0.18 | Zhao et al. 2025 Llull (d02) | S (K29) |
| Expert originality ratings are noisy | Test-retest ICC 0.59-0.74 overall, 0.60 [0.40, 0.77] for originality; 63 researchers, 7,938 ratings, two waves. Human control idea beat AI ideas on overall quality in both waves | Zhang et al. 2025/26 (d01) | E (K30) |
| LLM rater of disruption is below chance | AUC for top 2% cited (n=739): EDM 0.83, CD 0.60, node2vec 0.49, LLM rater 0.42. Rater vs citation velocity rho +0.016 (ns). Review score vs EDM rho about 0.005; accepted vs rejected p=0.11 | Huang 2026 (c18, d13) | E (K22, K30) |
| Text surprisal as a novelty signal | 83 notes, 3 experts: Welch t=2.6, p=0.005, df about 66.3; 8 false alarms (maths notation, odd syntax) | Wang 2024 (c16) | S (K21) |
| Tuned small model beats prompted LLM at method novelty | SciBERT accuracy 0.74, F1 0.73 | Wu et al. 2025 (c17) | S (K21) |
| Retrieval trained on idea summaries | Marketing: +24.11 / +25.46 / +24.11 / +26.69% (acc / prec / rec / F1); NLP +22.54 / +28.29 / +22.54 / +22.82%. NLP accuracy 0.7474 vs 0.61 vanilla RAG | Liu et al. 2025 (c08) | S |
| AI-assisted writing: disruption up, breadth not | About 2M full-text articles 2021-2024. 18-month window beta=0.151 (SE 0.004). Yearly effect 2022 -0.116; 2023-24 +0.321 to +0.408. Breadth (entropy) effect 1.277 (2021) and 1.225 (2022) to 0.455 (2024) | Yan and Ni 2026 (b27, c19) | S (K20) |
| Embedding novelty fell after ChatGPT for non-English-dominant authors | 13,847 articles, 44 IS journals. Post x non-English-dominant -0.176 SD (p<0.001), about 7 percentile points; -0.157 with journal fixed effects. Not an effect of LLMs proper | Safari and Babaei 2026 (a19, c20) | S (K20) |
| AI tools widen the individual, narrow the field | About 3x papers, 4.8x citations; topic range -4.63%; engagement -22% (secondary summary, not opened) | Hao et al. 2026 (a20) | S, unopened |
| Open-source models mostly consolidate | 2,556,240 Hugging Face models; most consolidative; disruptive positions more likely among large models and via fine-tuning | Wei et al. 2026 (c26) | S |
| Executable verifiers beat LLM judges but are narrow | Up to +55.0 F1 over the initial verifier sets; +17.0 points downstream accuracy when used as a tool | Pezeshkpour and Hruschka 2026 (d16, abstract only) | S |

---

## 4. Mechanisms and models

Each model is written so an engineer can implement it. All must run in code, not as a model opinion (G5, G8).

### 4.1 Uzzi z-score (combination atypicality)

Inputs: a set of items (journals), and many "documents" each citing a set of items.

1. For each pair (i, j), count `obs(i,j)` = documents citing both.
2. Build a null: shuffle the citation links between documents and items while keeping each document's reference count and each item's citation count. Repeat to get `exp(i,j)` and its spread `sd(i,j)`.
3. `z(i,j) = (obs - exp) / sd`.
4. For a document, collect z for all pairs of its references. Report `median z` (conventionality) and the 10th percentile `z` (tail novelty). Lower z = more atypical.

Agent version (cheap): there are no journals for an idea. Use text. Embed each component of an answer (method, source, concept). Use pairwise embedding distance among the components. Take a high quantile, as Shibayama et al. did on cited titles (a08). One distant pair can be enough. Score = quantile distance. Calibrate on a few labelled cases first. Embeddings move with style and framing (c20), so compare only within one task.

Embedding form of atypicality (a10): `score(i,j) ~ - inner_product(v_i, v_j)` with vectors from a skip-gram model trained on co-use sequences. In our setting: train on the sequences of operators or concepts used in solved items. High inner product = commonly co-used = conventional.

### 4.2 Mix profile (conventional core plus atypical tail)

The Uzzi result is a profile, not a single dial. A candidate has two numbers: median conventionality and tail novelty. The hit rate was highest when both were high (9.11 per 100). Implementation for open mode: build a candidate set where each candidate has a conventional core (the first natural answer, or a standard method) and at most one or two distant parts added. Do not generate all-distant candidates. Track the mix per candidate in code. This is the K01 design and is untested for LLMs (K29).

### 4.3 Disruption index and why it is relative

Definition (Funk and Owen-Smith): for focal paper f, let `N_i` = later papers citing f but none of its references, `N_j` = later papers citing both f and at least one reference, `N_k` = later papers citing the references but not f. `D = (N_i - N_j) / (N_i + N_j + N_k)`.

Lin, Li, Wu decomposition (a13): `D` is driven by `dp = (Ni - Nj)/(Ni + Nj)` and the burden `bp = Cmax / Cp`. D is mostly whether the paper beats its single most-cited reference.

Use for the agent: never compute D. Use the idea: disruption is defined against a named incumbent. The agent should name the incumbent answer first (K31 gives an outside signal that stance toward a named incumbent tracks displacement).

### 4.4 Functional equivalence (displacement vs recombination)

Proposed mechanism (a12, K04, single-source): displacement happens when the new idea does the same intellectual job as the incumbent, only better. Recombination joins complementary things that do different jobs, so nothing is replaced.

Two operators follow.

- **Recombine (extend):** pick a distant source. Map one part. The result fills a new niche. Check: does the result run and add something?
- **Displace (replace):** name the incumbent answer and the job it does. Produce a candidate that does the same job inside the same topic by a different route. Check: does the candidate beat the incumbent on the verifier or on fresh inputs?

Selection rule in code: the checker differs by operator. For recombination, score by run-based validity (does it work) and by dedup distance from the incumbent. For displacement, score by head-to-head result against the incumbent on a held-out input (a counterexample test, S7).

### 4.5 Risk and break-even rule (Foster)

Let `c_r`, `c_n`, `c_j` be mean reward for repeat, new, jump moves. Human numbers: 8.38, 11.00, 12.90. If success probability is `p_r`, `p_n`, `p_j`, the expected reward is `p * c`. Break-even: `p_n * 11.00 = p_r * 8.38` gives `p_n = 0.76 p_r`; `p_j = 0.65 p_r`. Implementation for the agent: on a calibration set with a verifier, measure pass rates of near and distant candidates. Set the distant share of attempts by the ratio. If distant passes at less than 0.65 of near, the distant move loses in expectation (for human-like payoffs). For an agent the payoff is different (a pass is binary; the best of several counts), so the break-even is lower for a portfolio (K09 notes this is untested for LLMs).

### 4.6 Distance-controlled source selection (Liu et al., Scideator, analogy retrieval)

1. Embed the target problem. Retrieve sources over a distance range.
2. Bucket sources: near, mid, far (e.g. by quantile of distance).
3. Abstract the source to its purpose and mechanism (facet extraction). Gu et al. abstract to a principle first (c13). Scideator recombines facets (c09).
4. Map one facet into the target. Code checks the mapping is typed (what part maps to what).
5. Run the result.

For strong LLMs the benefit appears only in the farther half of pairs (beta 0.12) and more in the top 10% (0.24) (d10). Weaker LLMs need the closest 20% removed. Originality rises and feasibility falls (rho -0.74). Therefore far sources need a validity check.

### 4.7 Retrieve-compare-revise novelty loop (SciMON)

1. Generate an idea.
2. Retrieve k=20 nearest prior ideas by sentence embedding.
3. Prompt: this is too similar to X; produce a different one.
4. Repeat for a fixed number of rounds.

Result: 88.9% of first-round updates substantially different; 55.6% judged more novel (c10). Risk: it rewards moving away from the nearest neighbour, which can reward odd over good. Pair with a value check.

### 4.8 Facet-level novelty gate

Embedding filtering alone found the known overlap in the top 10 only 10.34% of the time (58 cases). Facet-level re-ranking (purpose and mechanism) found it 89.66% (d14). Implementation: extract purpose and mechanism for the candidate and for each retrieved paper. Compare facet by facet. A "not novel" verdict can be checked against the retrieved paper. A "novel" verdict cannot (absence of evidence). Use as a veto, not as a promoter.

### 4.9 Diversity forcing for sampling

- **In-context regeneration (NoveltyBench):** show the model its earlier answers and ask for a different one. Restores about human-level diversity (d06).
- **Verbalized sampling:** ask for k answers with probabilities in one call. Diversity 1.6-2.1x; downstream math accuracy 36.1-37.5 vs 30.6 for direct (d08).
- **Code-side history:** the program keeps a list of directions tried and assigns untried ones (already S3 open mode).
- **Dedup by embedding:** cosine 0.8 on all-MiniLM-L6-v2 left 5% of 4,000 ideas (a21).

Temperature does not help much: min-p with T=2.0 still gives same-model similarity above 0.8 on average (d07).

### 4.10 Verifier-gated distance budget

Lu et al. (d04) show correctness falls fast as the model is pushed off the known method (16.1% to 2.1% pass@1). Design: a distance budget per problem. Each distant candidate must pass a checker (unit test, held-out example, symmetry) before it can be ranked. Report pass rate by distance step. This is the only executable-verifier test of forced novelty found.

---

## 5. What holds up

### 5.1 Holds (established per claims.jsonl)

- **A and D measure different things (K03).** Two sources: Li, Lin, Wu 2025 and Huang 2026's independent bridge/redirector split (plus Lin, Li, Wu 2025 on D as local displacement). Negative link in every panel.
- **D is unstable and unreliable as a quality label (K06, K22, K08).** Five or more independent sources: Holst, Petersen, Bentley, Macher, Larregue and Gingras, Bornmann et al. 2020, Huang and Xie, Liang et al. 2020, Chen et al. 2025. The standard index AUC for breakthrough lists is 0.26-0.79.
- **LLM judges cannot judge novelty (K17).** Four or more independent sources: Si 2024 (53.3% best), RINoBench (macro-F1 12-17, zero recall on "not novel"), Think-Probe-Respond (bias to medium), RQ-Bench (mirage), plus Huang 2026 (AUC 0.42).
- **LLM idea novelty does not survive execution (K16).** Si 2024 plus Si 2025. Outside NLP, code shows a correctness cost (d04) and math shows novelty is plentiful but LLM-judged (d05). These are not tests of the same claim.
- **LLMs are collectively alike (K19).** Wenger and Kenett, NoveltyBench, Artificial Hivemind agree.
- **Prompt-level diversity helps without quality loss (K28).** NoveltyBench and Verbalized Sampling.
- **Retrieval and recombination pipelines raise novelty by their own judges (K14).** Five or more pipelines. The caveat is that the judges are the unreliable ones from K17. No pipeline ran its ideas to a real result.

### 5.2 Failed or disputed replications

| Claim | Failure or dispute | Notes |
|---|---|---|
| Science is getting less disruptive (Park 2023) | Holst et al. 2024: 972,161 papers and 142,362 patents hidden by a plotting bug; 97% of CD5=1 papers have zero references; random rewiring reproduces the decline. Petersen: citation inflation. Bentley: unweighted counting. Macher: truncation (88% for patents). | Park reply: decline survives Holst's data; 20% of Holst's sample is non-research content. 105-study review says most show decline. Contested (K07). Both camps use the same unstable index. |
| Small teams disrupt, large teams develop (Wu 2019) | Petersen: positive at 5 years. Lin: flips at 5-year window, negative at 10. Huang and Xie: equalising references reverses it; large teams more disruptive in four domains and every decade. | Established that the claim depends on specification (K08). Not established that either direction is true. |
| Atypical papers disrupt more (Lin 2022) vs less (Li 2025) | Same group, opposite signs. Differences: MAG vs OpenAlex; one cohort vs all years; z-tail (2.3%) vs continuous A-index; share disruptive vs mean D. r = -0.05 in the 2022 paper itself. | Not reconciled (K05). Best reading, untested: tail effect versus bulk slope. Do not use A as a selection signal. |
| Wang measure of novelty tracks quality | Bornmann et al.: Wang score W mostly negative against expert tags. | Measure choice changes the answer (K02). |
| LLM ideas are more novel (Si 2024) | Si 2025: after execution novelty 4.93 vs 4.73, p=0.21. Excitement and effectiveness drops of 1.76 and 1.88 for AI ideas. Gupta and Pruthi: 24% of sampled proposals plagiarised. | Novelty edge was an idea-stage rating by noisy reviewers (agreement 56.1%). |
| Functional equivalence | No outside lab tested it. Ustyuzhanin and Huang give indirect support only. | Single-source (K04). |

### 5.3 Moderators and boundary conditions

- **Time window.** D needs about 10 years. A 3-year window is unstable. A 5-year window flips team-size results. Novel papers have a slow start (Wang 2017). Early scores underrate novel attempts. (a09, b07, a05, d03)
- **Field.** The atypical-to-disruptive link in Lin 2022 is stronger in computer science and engineering than natural sciences. D results differ by field (Medicine, Chemistry, Physics in Liang et al.).
- **Reference-list length.** D falls mechanically as lists lengthen (b12, c25). Papers with 30+ references stabilise 1-3 years faster.
- **Measurement object.** Journal-level pairs measure domain mixing, not idea mixing. Ideas for landmark papers often came from elsewhere (a07).
- **Model strength (LLM).** The distance effect appears in strong LLMs only in the farther half of pairs. Weaker LLMs need the closest 20% removed. (d10) Larger models in a family are less diverse (d06). More capable models benefit more from Verbalized Sampling (d08).
- **Reference solutions shown.** In math, more shown prior solutions raise correctness and lower novelty (d05).
- **Task type.** NLP ideas (Si), product design (Liu), competitive programming (Lu), competition math (Ye), everyday open questions (NoveltyBench) behave differently. No result has been replicated across task types.
- **Rater.** Experts: ICC about 0.6 for originality. Lay raters: split-half 0.73-0.81. LLM raters: below chance for later impact (AUC 0.42).

### 5.4 Interventions that worked

| Intervention | Effect | Caveat |
|---|---|---|
| In-context regeneration (show earlier answers, ask for a different one) | About human diversity, no utility loss (NoveltyBench) | Everyday prompts; correctness not checked |
| Verbalized sampling (k answers with probabilities) | Diversity 1.6-2.1x; downstream accuracy 36.1-37.5 vs 30.6 | Gain through a fine-tuning data pipeline, not same-model answer accuracy |
| Cross-domain analogy retrieval | Diversity +90% to +173%; novel share 1.6-9.0% up to 50.4-68.9% | LLM-judged; "reasonable" fell to 67% |
| Planned iterative outside retrieval (Nova) | 3.4x unique novel ideas; flat without planning | LLM-judged; judge near chance |
| Retrieve-compare-revise (SciMON) | 55.6% judged more novel after one round | Small human study |
| Facet-level novelty check (Scideator) | 89.66% retrieval of known overlap vs 10.34% for embeddings only | NLP; LLM-based, not cheap |
| Source far enough (Liu) | Strong LLMs gain in the farther half | Lay originality raters |
| Human-written reasons for novelty (Wu et al. 2025) | SciBERT 0.74 accuracy beats prompted LLMs | Method novelty only |

### 5.5 Interventions that did not work

| Intervention | Result |
|---|---|
| Telling the model to be creative, or paraphrasing | Barely helps (NoveltyBench; Wenger and Kenett creativity prompt helped only slightly) |
| Raising temperature or min-p | Same-model similarity stays above 0.8 (Artificial Hivemind) |
| Plain over-generation | 5% non-duplicates at cosine 0.8 |
| LLM-as-judge for novelty, including reasoning models | Macro-F1 12-17; no better with reasoning; rewarding model-written questions |
| Switching to another model for a different region | Models are alike (71-82% cross-model similarity) |
| Reasoning strategies for creative code (MCTS, self-correction, planning, sampling) | Do not improve divergent creativity and correctness together; only MCTS lifts divergent creativity |
| Showing prior solutions | Raises correctness but lowers novelty in math |
| Embedding filter for disguised copying | 10.34% retrieval of known overlap |
| Disruption-like score as a label | Does not match expert tags; AUC 0.26-0.79 for breakthrough lists |
| Reviewer scores as predictors of later disruptiveness | rho about 0.005 |

---

## 6. Language models

### 6.1 How LLMs behave on these tasks

**As generators of new ideas, one at a time.** About as original as people on short tests (Wenger and Kenett: AUT 0.711 vs 0.696; FF 0.603 vs 0.637; DAT 0.801 vs 0.753). Rated more novel than experts by blind reviewers on NLP research ideas (5.64 vs 4.84) (a21). But rated lower on feasibility, and after execution the novelty edge is gone (4.93 vs 4.73, p=0.21) while excitement and effectiveness drop 1.76 and 1.88 (a22).

**As a population.** Alike. Fewer than 3 distinct answers in 10 samples (d06). Same-model similarity above 0.8 in 79% of cases; cross-model 71-82% (d07). 5% non-duplicates out of 4,000 ideas (a21). Larger models are less diverse than smaller ones within a family (d06).

**As judges of novelty.** Poor. Pairwise accuracy 45-53% vs 56.1% human-human (b20). Macro-F1 12-17 on a 5-class scale; zero recall on "not novel"; medium-novelty bias; reasoning models barely better (c06, c07). They prefer model-written research questions that experts reject (a26). A zero-shot LLM rater scored AUC 0.42 for papers that became highly cited (c18). Agreement across five LLMs from four vendors was close, which shows agreement is not validity.

**As measurement tools in this subfield.** Li, Lin, Wu used Llama-3.1-70B to label 50,147 papers as theory or method and to rate topic similarity. LLM labels were not checked against human labels in the text read (c01).

**On distant combination.**
- Product design: strong LLMs gain only when the source is far (d10).
- Cross-domain analogy retrieval raises LLM novel-solution share from 1.6-9.0% to 50.4-68.9% (LLM-judged) and lowers reasonableness to 67% (a24).
- Random combinations double diversity (0.41 vs 0.21) and cut relevance (0.05 vs 0.11) (d02).
- Code: forced distance cuts pass@1 from 16.1% to 2.1% (d04).
- Math: novel share of correct answers rises with difficulty (55.39% to 83.01%), LLM-judged (d05).

**On displacement.** No direct LLM test of "replace the incumbent". Ustyuzhanin et al. tie displacement to stance toward a named incumbent for human papers (d03). In math, showing prior solutions cut novelty (d05).

### 6.2 What changed behaviour, by how much

| Change | Effect size | Source |
|---|---|---|
| Rerank of AI ideas by humans | Novelty 5.64 to 5.81 | a21 |
| Cross-domain analogy retrieval | Diversity +90% to +173%; novel share up to 68.9% | a24 |
| Nova planning + retrieval | 3.4x unique novel ideas | c11 |
| SciMON novelty loop | 55.6% judged more novel; 88.9% substantially different | c10 |
| Deep Ideation | +10.67% | c12 |
| Abstract then recombine | Similarity to real papers +7-10% | c13 |
| In-context regeneration | Roughly human diversity | d06 |
| Verbalized Sampling | Diversity 1.6-2.1x; accuracy 30.6 to 36.1-37.5 | d08 |
| Source distance (strong LLMs) | beta 0.02 (all pairs) to 0.12 (farther half) to 0.24 (top 10%) | d10 |
| Technique bans in code | pass@1 16.1 to 2.1 | d04 |
| Showing prior solutions in math | Correctness up, novelty down | d05 |
| Facet-level retrieval vs embedding | 89.66% vs 10.34% | d14 |
| Think-Probe-Respond on open models | +22.30% macro-F1 over baselines (absolute still low) | c07 |
| Executable verifiers (AutoPyVerifier) | Up to +55.0 F1; +17.0 points accuracy | d16 |

### 6.3 What is missing

No study runs the mix against all-distant and all-conventional with a verifier. No study measures a budget share of distant moves for an LLM. No study tests an LLM displacement operator. No study tests an extra revision round for distant candidates. All "LLM novelty improves" results lean on judges that K17 says are unreliable.

---

## 7. What our agent should take

Format: item, schema part, status mark, evidence ids.

### Add now (established)

1. **Never let a model judge novelty or pick the winner by an originality score.** Run the idea to a checkable result; use a model rating, if any, only as a tie-breaker after a verifier. Schema part: **G8 / G5** (reinforces existing). **[E]** K16, K17, K30. Evidence a21, a22, a26, b20, b22, c06, c07, d01, d13. Note: this is already G8; add the numbers (LLM judge accuracy 45-53%, zero recall on "not novel", expert test-retest ICC about 0.6) to the justification.
2. **Do not use a disruption-style or citation-style score as a reward or label.** It is unstable, window-dependent and disagrees with experts. Schema part: **not to add (4b)**. **[E]** K06, K08, K22. Evidence a18, b07, b09, b10, b11, b12, b24, b25, c25.
3. **Do not copy human-science rules drawn from D** (small focused teams beat large ones; "science is less disruptive, so push for disruption"). Schema part: **4b**. **[E]** K08. Evidence b08, b13, b24, c25.
4. **Treat samples as non-independent and force difference in code.** Use in-context regeneration (show earlier candidates, ask for a different one) and/or verbalized k-candidates, with embedding dedup. Temperature and "be creative" prompts do not help. Schema part: **S3 open mode** (already has history and untried directions; add dedup and the in-context regeneration form). **[E]** K19, K28, K15 (dedup is single-source but cheap). Evidence c21, d06, d07, d08, a21.
5. **Do not rank a novel candidate by an early score alone.** Judge it on a held-out check at the horizon where it will be judged. Schema part: **S4 / S7**. **[E]** in the sense that G3 and G8 already demand this; the delayed-payoff evidence itself is **[S]** K10 and human-only. Evidence a05, a09, b07, d03.
6. **Keep the generator from selecting.** Already G8. Add: on idea tasks, a "not novel" veto from a facet-level (purpose and mechanism) comparison to retrieved prior work is allowed; a "novel" verdict is not accepted without a run. Schema part: **G8**. Status: the veto is **[S]** (K18, d14); keep it in Test first.

### Test first (single-source or contested)

| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| T1 | **Two operators, not one:** "recombine from a far source" (O7) and "name the incumbent and replace it by something that does the same job" (new O2-style displacement: Specialise/Generalise are different) as separate operators with separate triggers (displacement is a new operator, not in O1-O8 today) | O7, new displace operator, S6, S3 open mode | K03 is [E] as a human finding; the operator split for LLMs is [S], untested | a11, a12, b04, c01, d03, d13 |
| T2 | **Mix portfolio:** conventional core plus one distant add-on vs all-distant vs all-conventional | S3 open mode | [S] K01, K29 | a01, a02, b01, d01, d02 |
| T3 | **Distant share of the attempt budget** set from a calibration ratio (distant pass rate over near pass rate) | S3, S0, memory (class record) | [S] K09, K32 | b06, d09 |
| T4 | **Source distance threshold:** far-half only for O7 and open mode; scale by model strength | O7 | [S] K12 | a23, d10 |
| T5 | **Verifier-gated distance budget:** each distant candidate must pass a checker before ranking; log pass rate by distance step | S4, O7 | [S] K26 | d04, d16 |
| T6 | **Extra revision round for distant candidates before ranking** | S5, S7 | [S] K10 | a05, a09, d18 |
| T7 | **Name the incumbent first, then add a "differ from this" instruction** | S1 / O7 or new operator | [S] K27, K31 | d03, d05 |
| T8 | **Facet-level novelty veto** (purpose and mechanism) against retrieved prior work | G8 / S7 | [S] K18 | c05, d14, c08 |
| T9 | **Two novelty proxies logged in code** (embedding distance to nearest prior and a rubric); log disagreements | S9 log | [C] K02, K21 | a06, a08, c16, c17 |
| T10 | **Cross-domain analogy retrieval step** on versus off | S3 open mode, O7 | [S] K13 | a24, b28, c11 |
| T11 | **Retrieve-compare-revise loop** with a value check | S3 open mode | [S] K14 | c10 |
| T12 | **Far analogues only at impasses and in open mode** (already in O7); confirm with distance measure | O7 | [E] for the variance note (F05); [S] for the threshold | a23, d10 |
| T13 | **Problem-statement-only vs problem plus cited-literature recombination** | S3 | [S] K23 | a07 |

Not for the agent now: K05 (reconcile Lin 2022 vs Li 2025), K07 (decline debate), K20 (AI narrows science; revisit if multiplayer sharing is built), K25 (team size; link to Crowd within).

---

## 8. Concrete tests on our bench

All tests: both arms at equal tokens (setup cost counted, G7). Verifier-based metric first. Report the best candidate available vs the selector's pick (section 6 of the schema). Use at least 3 seeds.

| # | Item type | Arms (equal tokens) | Metric | Expected effect |
|---|---|---|---|---|
| B1 | ARC items where the correct rule overturns the default, plus items that need a new frame | (a) recombine-only operator, (b) displace-only operator (name incumbent, same job), (c) mixed, (d) plain best-of-N | Pass on the unfitted part (G3); share of items solved by only one arm | Displace wins on rule-inversion items; recombine wins on new-frame items; mixed wins overall. If the split does not show, the two-operator design is dropped. |
| B2 | Open-mode items (NoveltyBench style) with a code-scored validity check where possible | (a) all conventional, (b) all distant, (c) conventional core + one distant add-on | Unique valid candidates per verifier call; best valid candidate score | (c) at least equal to the best of (a), (b) on valid-unique count. Distant-only should show high diversity and low validity (d02). |
| B3 | Items with a verifier at three difficulty bands | Distant-candidate share 0%, 15%, 50% | Verifier pass of the selected answer; tokens per solve | Small distant share (10-20%) helps on hard items only; on easy items 0% wins. Break-even ratio from the calibration set (K32). |
| B4 | Puzzle or analogy items with a known far-source library | Source distance near / mid / far (embedding quantile), by model size | Pass rate and unique-valid count | Far-half helps only for the stronger model; near sources help weaker ones (d10). Validity falls with distance (rho -0.74 in the human-rated data). |
| B5 | Code or ARC items with unit tests | Distance budget with verifier gate vs distance without gate vs plain | Pass rate by distance step; selected-answer pass | Gated arm keeps most of the plain pass rate; ungated pass falls fast (d04 shows 16.1% to 2.1%). |
| B6 | Items where distant candidates start weak | Distant candidates get one extra revision round before ranking vs rank first | Final pass of the selected answer | Extra round recovers some distant candidates (K10 hypothesis). No effect would close the question. |
| B7 | Math or ARC items with a known prior solution | (a) show incumbent, (b) show incumbent plus "differ from this", (c) none | Verifier pass; distinct-approach count | (b) at least keeps pass of (a) and lifts distinct approaches toward (c) (d05). |
| B8 | Idea or open items with seeded known prior art, some disguised | Embedding gate alone vs facet-level (purpose, mechanism) veto | Share of disguised copies caught; share of true novel items wrongly vetoed | Facet-level catches far more (d14: 89.66% vs 10.34%). Must not veto real novelty. |
| B9 | Open-mode sampling | Plain resampling; in-context regeneration; verbalized-k; forced far seed | Unique valid candidates per verifier call; mean pass | Regeneration and verbalized-k raise unique count with no pass loss (K28); forced far seed raises it more and may cost pass. |
| B10 | Any suite with logged proxies | Two novelty proxies (embedding distance, rubric) vs verifier outcome | Rank correlation with verifier outcome | Both weak (r near 0 to 0.3); proves why the verifier must lead (K21, K30). |
| B11 | Idea-then-execute tasks (small, runnable) | Select by idea-stage LLM rating vs by executed result | Rank correlation of idea-stage and outcome-stage scores | Low or negative for LLM-rated novelty (Si 2025). |

---

## 9. What does not transfer, and why

| Human finding | Why it may not transfer to one agent |
|---|---|
| Hit rate of the conventional-plus-tail mix (Uzzi) | The outcome is citations 8 years later. An agent's outcome is a verifier pass. The mix may matter for citation fashion, not correctness. Journal pairs measure domain mixing, not idea mixing (a07). |
| Teams add tail novelty | Human teams hold different people with different knowledge. Samples from one model are not independent (G4); cross-model samples are 71-82% similar (d07). A team of personas is not a team. |
| Small teams disrupt | Not even established for humans (K08). An agent has no team. |
| Disruption is "replacing the incumbent" | Meaning rests on later citation behaviour. The agent has no later citers. It must use a head-to-head check against the named incumbent instead. |
| Science is getting less disruptive | Disputed (K07), and a population claim about literature. |
| Atypical papers disrupt more/less | Contested between two papers of the same group (K05) and about citations. No agent decision depends on it. |
| Risky moves break even at p = 0.76 and 0.65 of repeat | Human payoff is citations and failures are invisible. An agent can run many cheap attempts and keep the best; its break-even is a pass-rate ratio under a budget, not the human number. |
| Delay of payoff (10 years) | The agent's "delay" is a revision round, not a decade. The mechanism (early scores under-rate novelty) may not exist for models. |
| Funding and prestige bias against novelty (Wang 2017) | The agent has no funders. |
| Landmark ideas came from talks, practice, cross-field contact (a07) | The agent has no talks. Retrieval from far fields is the nearest substitute. |
| AI shrinks the field's topic range (Hao 2026) | A system-level effect on many users. Relevant to multiplayer, not to a single agent (K20). |
| Idea-stage novelty edge of LLMs (Si 2024) | Reviewers judged text; the agent is scored on running (G8). The edge disappears on execution anyway. |
| Embedding-distance novelty (Shibayama) | Needs a reference list, which an agent's answer does not have, and moves with language and style (c20). |
| Surprisal as novelty (Wang 2024) | Rises for odd formatting and equations: 8 false alarms (c16). |

---

## 10. Open questions

1. Does the mix beat all-distant and all-conventional under an executable verifier at equal tokens (gap 1, K29)? No LLM study tests it.
2. At what distance does a distant add-on start to help, per model strength, with correctness instead of lay originality (gap 2)? Only Liu et al. measure it.
3. How much of the idea novelty edge survives execution outside NLP ideas (gap 3)? Code says no (correctness cost); math is LLM-judged.
4. Is "name the incumbent first" enough to trigger displacement, or does it cut diversity (gap 4, K27, K31)?
5. Can a non-LLM novelty gate catch disguised copying (gap 5)? Embeddings alone failed (10.34%). A facet-level gate worked but uses an LLM.
6. Do Lin 2022 and Li 2025 reconcile when definitions match (gap 6, K05)? If the tail effect is real, atypicality could be a weak positive signal for extreme candidates.
7. What budget share of distant moves is worth it for an LLM (gap 7, K32)?
8. Does a forced-distance seed keep diversity without a correctness cost (gap 8)? Regeneration and verbalized sampling keep quality; forced distance does not yet have a test.
9. Does an extra revision round rescue slow-start distant candidates (gap 9, K10)?
10. Has anyone outside the Wu/Evans group tested functional equivalence directly (gap 10, K04)? Only partial hits.
11. Is the Li et al. LLM labelling of theory vs method valid against human labels? Not checked in the text read.
12. Do the 2026 papers (Hao, Larregue and Gingras, Safari and Babaei, Yan and Ni, Wei et al., Huang and Xie) hold up? They are newest and least replicated.
13. Is the human inverted-U for distance (Fu et al. 2013) real, and does the agent show one? Not opened (d15).
14. Do LLM originality scores track anything that matters? Expert ICC is about 0.6 and LLM AUC is 0.42 for later impact.

---

## 11. Sources

[V] = opened and read this session or by earlier agents in this series (full text or abstract page as noted). [M] = snippet, summary or second-hand only. Note from critique.md: Uzzi 2013, Park 2023, Wang et al. 2017 and Bornmann 2019 were opened by earlier agents; the numbers were not re-opened in the cross-check, so they are held as single-checked.

### Founding and combination measures
- [V] Uzzi, Mukherjee, Stringer, Jones (2013) Atypical combinations and scientific impact. https://www.kellogg.northwestern.edu/faculty/uzzi/htm/papers/Science-2013-Uzzi-468-72.pdf ; https://doi.org/10.1126/science.1240474 (a01-a03, b01-b03; single-sourced in the cross-check)
- [V] Lee, Walsh, Wang (2015) Creativity in scientific teams. https://lirias.kuleuven.be/retrieve/e0986ef4-8841-4fdf-8be0-b56d66d12e59 (a04)
- [V] Wang, Veugelers, Stephan (2017) Bias against novelty in science. https://www.nber.org/system/files/working_papers/w22180/w22180.pdf (a05)
- [V] Bornmann, Tekles, Zhang, Ye (2019) Do we measure novelty when we analyze unusual combinations of cited references? https://arxiv.org/pdf/1910.03233 (a06)
- [V] Tahamtan and Bornmann (2018) Creativity in science and the link to cited references. https://arxiv.org/pdf/1806.00224 (a07)
- [V] Shibayama, Yin, Matsumoto (2021) Measuring novelty in science with word embedding. https://doi.org/10.1371/journal.pone.0254034 (a08)
- [V] Lin, Evans, Wu (2022) New directions in science emerge from disconnection and discord. https://arxiv.org/pdf/2103.03398 (a09, a10, b05, d11, d18)
- [V] Yu and Romero (2024) Unusual combinations of datasets. https://arxiv.org/abs/2402.05024 (b18)
- [V] Foster, Rzhetsky, Evans (2015) Tradition and innovation in scientists' research strategies. https://arxiv.org/pdf/1302.6906 (b06, d09)
- [V] Fang and Evans (2025) Generalization and the rise of system-level creativity. https://arxiv.org/abs/2510.03240 (b17)
- [V] Wang (2024) A content-based novelty measure for scholarly publications. https://arxiv.org/abs/2401.03642 (b29, c16)
- [V] Wu, Zhang, Zhao (2025) Automated novelty evaluation of academic paper. https://arxiv.org/abs/2507.11330 (c17)

### Atypicality versus disruption
- [V] Li, Lin, Wu (2025) Can recombination displace dominant scientific ideas? https://arxiv.org/pdf/2506.15959v4 ; https://arxiv.org/abs/2506.15959 (a11, a12, b04, c01, d12; abstract and full text re-opened in the critique)
- [V] Lin, Li, Wu (2025) The disruption index measures displacement between a paper and its most cited reference. https://arxiv.org/pdf/2504.04677 (a13-a15, b26)
- [V] Lin, Li, Wu (2025) Team size and its negative impact on the disruption index. https://arxiv.org/abs/2502.00219 (b08)
- [V] Huang (2026) Catalyst papers in AI research. https://arxiv.org/pdf/2607.05401 (c18, d13)
- [V] Ustyuzhanin, Trofimova, Zuenko (2026) Citations are late. https://arxiv.org/pdf/2610.07397 (d03)
- [M] Funk and Owen-Smith (2017); Wu, Wang, Evans (2019) Large teams develop and small teams disrupt. https://doi.org/10.1038/s41586-019-0941-9 (a28; second-hand through Lin 2025)

### Disruption critiques and the decline debate
- [V] Park, Leahey, Funk (2023) Papers and patents are becoming less disruptive. https://arxiv.org/pdf/2106.11184 (a16)
- [V] Park, Leahey, Funk (2025/2026) Robust evidence for declining disruptiveness. https://arxiv.org/pdf/2503.00184 (a17)
- [V] Holst et al. (2024) Dataset artefacts are the hidden drivers of the declining disruptiveness. https://arxiv.org/abs/2402.14583 (b11, c24)
- [V] Petersen, Arroyave, Pammolli (2023) The disruption index is biased by citation inflation. https://arxiv.org/abs/2306.01949 (b12)
- [V] Petersen, Arroyave, Pammolli (2024) The disruption index suffers from citation inflation. https://arxiv.org/abs/2406.15311 (b13; abstract and introduction)
- [V] Bentley et al. (2023) Is disruption decreasing, or is it accelerating? https://arxiv.org/abs/2306.14364 (b14)
- [V] Macher, Rutzer, Weder (2026) Is there a secular decline in disruptive patents? https://arxiv.org/abs/2306.10774 (b15)
- [V] Wu et al. (2026) Is innovation becoming less disruptive? An inventory of the literature. https://arxiv.org/abs/2602.05140 (b16)
- [V] Chen, Bornmann, Bu (2025) Dynamic disruption index. https://arxiv.org/abs/2504.07828 (b07)
- [V] Liang, Jiang, Hou (2020) Same data may bring conflict results. https://arxiv.org/abs/2009.06888 (b09)
- [V] Bornmann, Devarakonda, Tekles, Chacko (2020) Are disruption index indicators convergently valid? https://arxiv.org/abs/1911.08775 (b10)
- [V] Larregue and Gingras (2026) The disruption index does not measure scientific innovation. https://arxiv.org/pdf/2606.07332 (a18, b25, c23)
- [V] Huang and Xie (2026) Large scientific teams are more, not less, disruptive. https://arxiv.org/abs/2610.07329 (b24, c25; benchmark-to-AUC mapping not independently re-verified)
- [V] Wei et al. (2026) Identifying disruptive models in the open-source LLM community. https://arxiv.org/abs/2604.11618 (c26)

### LLM and AI studies
- [V] Si, Yang, Hashimoto (2024) Can LLMs generate novel research ideas? https://arxiv.org/pdf/2409.04109 (a21, b19, b20, c02, c04)
- [V] Si, Hashimoto, Yang (2025) The ideation-execution gap. https://arxiv.org/pdf/2506.20803 (a22, b21, c03)
- [V] Gupta and Pruthi (2025) All that glitters is not novel. https://arxiv.org/abs/2502.16487 (c05)
- [V] Schopf and Farber (2026) Is this idea novel? RINoBench. https://arxiv.org/abs/2603.10303 (b22, c06)
- [V] Schopf, Schreieder, Aizawa (2026) Think-Probe-Respond. https://arxiv.org/abs/2608.25660 (b23, c07)
- [V] Sinhahajari, Majumder, Poria (2026) On the limits of LLM-as-judge for scientific novelty (RQ-Bench). https://arxiv.org/pdf/2606.12071 (a26)
- [V] Wu et al. (2026) NovBench. https://arxiv.org/pdf/2604.11543 (a27; abstract and introduction only, no detailed scores)
- [V] Liu, Yang, Poria, Nguyen, Cambria (2025) Harnessing LLMs for scientific novelty detection. https://arxiv.org/abs/2505.24615 (c08)
- [V] Radensky et al. (2026) Scideator. https://arxiv.org/pdf/2409.14634 (c09, d14)
- [V] Wang, Downey, Ji, Hope (2024) SciMON. https://arxiv.org/abs/2305.14259 (c10)
- [V] Hu et al. (2024) Nova. https://arxiv.org/abs/2410.14255 (b28, c11; b28 abstract and captions)
- [V] Zhao et al. (2025) Deep Ideation. https://arxiv.org/abs/2511.02238 (c12)
- [V] Gu et al. (2025) LLMs can realize combinatorial creativity. https://arxiv.org/abs/2412.14141 (a25, c13)
- [V] Chen and Zhang (2026) Combinatorial innovation and multi-agent iterative search. https://arxiv.org/abs/2604.20548 (c14)
- [V] Chen et al. (2025) Structuring scientific innovation. https://arxiv.org/abs/2503.18865 (c15; abstract only, figures not extracted)
- [V] Shen, Druckmann, Zou (2026) Unlocking LLM creativity in science through analogical reasoning. https://arxiv.org/pdf/2605.11258 (a24)
- [V] Liu, Dubova, Conklin, Harada, Griffiths (2026) Cross-domain mapping on creativity in humans and LLMs. https://arxiv.org/pdf/2603.19087 (a23, d10)
- [V] Zhang, Wang, Chen (2025/2026) Scientific judgment drifts over time in AI ideation. https://arxiv.org/pdf/2511.04964 (d01)
- [V] Zhao et al. (2025) The Ramon Llull's Thinking Machine for Automated Ideation. https://arxiv.org/pdf/2508.19200 (d02)
- [V] Lu et al. (2025) Benchmarking language model creativity: code generation. https://arxiv.org/pdf/2407.09007 (d04)
- [V] Ye et al. (2024) CreativeMath. https://arxiv.org/pdf/2410.18336 (d05)
- [V] Zhang et al. (2025) NoveltyBench. https://arxiv.org/pdf/2504.05228 (d06)
- [V] Jiang et al. (2025/2026) Artificial Hivemind. https://arxiv.org/pdf/2510.22954 (d07)
- [V] Zhang et al. (2026) Verbalized Sampling. https://arxiv.org/pdf/2510.01171 (d08)
- [V] Wenger and Kenett (2025) We're different, we're the same. https://arxiv.org/abs/2501.19361 (c21)
- [V] Pezeshkpour and Hruschka (2026) AutoPyVerifier. https://arxiv.org/abs/2604.22937 (d16; abstract page only)
- [V] Yan and Ni (2026) AI-assisted writing and the reorganization of scientific knowledge. https://arxiv.org/abs/2604.14126 (b27, c19)
- [V] Safari and Babaei (2026) Research novelty in Information Systems journals after ChatGPT. https://arxiv.org/pdf/2603.22510 (a19, c20)
- [M] Hao, Xu, Li, Evans (2026) AI tools expand scientists' impact but contract science's focus. https://arxiv.org/abs/2412.07727v4 (a20; search summary only, opened:false)
- [M] Doshi and Hauser (2024) Generative AI enhances individual creativity but reduces collective diversity. No URL (c22; publisher page returned 403; the 10.7% figure is unverified)
- [M] Chan and Schunn (2015); Chan, Dow, Schunn; Fu et al. (2013) distance and design studies. https://www.lrdc.pitt.edu/Schunn/papers/Chan-Schunn2015-Cognition.pdf (d15; links returned 404, snippets only)
- [M] Gap-search negative result (d17): no study found for gaps 1, 5, 7, 10 as posed; search coverage was thin and the arXiv, Semantic Scholar and OpenAlex APIs returned 429.
