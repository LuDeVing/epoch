# 02. Analogy as a source of new ideas: structure mapping, design-by-analogy, retrieval, LLMs

Prepared 2026-10-13. Evidence labels: **H** meta-analysis, large preregistered, or independently replicated; **M** peer-reviewed or documented, single study or small n; **L** preprint-only, LLM-judged, abstract-only, author-asserted or anecdotal. "(inference)" marks my reasoning, not a finding. Bracketed numbers are Sources. The shared web-search quota ran out mid-task, so paywalled work I could not open (Christensen and Schunn, Helms et al., Wilson et al.) is left out; Dunbar's in-vivo analogy data are in 05_scientific_discovery.md.

## Bottom line

1. Unaided, people rarely notice structural analogies, and memory retrieval follows surface similarity, while structure is judged well once a candidate is in hand [2][4]. Far analogues must therefore be assigned and mapped explicitly.
2. "Farther is better" is not monotonic. Far examples raised novelty and variance, not mean or best quality [7]; more distant sources lowered shortlist odds in a field dataset [8]. Strong LLMs gained nothing on average from random remote sources and gained only at the far end [17].
3. LLM-era gains come from structure-first pipelines (list roles and relations, map by function, then search the source domain) [18] and from abstracting before mapping [20], but idea-level evidence is mostly LLM-judged. Targeted cross-domain retrieval has not beaten random diverse seeds [19].
4. Comparing two analogues and writing their shared schema is the best-replicated human trick [4][5][6]. I found no LLM test of it.
5. For the pipeline: retrieve on an abstracted schema, assign stratified far sources, force a typed mapping with a rename audit, pair analogues, rank by executed outcomes, and always run a random-diverse-seed control (Section 3).

## 1. What the evidence says

**Theory and human experiments**
- Structure-mapping: analogy maps relations between objects, not attributes, preferring relations inside a connected higher-order system (systematicity); potential analogies are less likely to be noticed because finding them requires access via relational matches, where object matches are no use [1] (theory).
- Access and soundness dissociate. Soundness tracked shared relational structure, retrievability tracked surface similarity, yet subjects picked the structural match in forced-choice recognition, so the failure is access, not encoding [2] (M). MAC/FAC models this as a cheap content-vector scan, then a structural matcher on the survivors [3]. Patent-search work reports the same surface limit [10].
- Spontaneous transfer is rare: about 30% of subjects used a studied analog on Duncker's radiation problem unprompted, about 75% after a hint, about 10% with no analog [4] (M; replicated within the paper).
- One analog plus a summary, a stated principle or a diagram did not induce a schema. Two analogs did: unprompted success 45% vs 21%, total 80% vs 53%; adding the principle 62% vs 40% unprompted; good schemas 94% vs 53% eventual success; dissimilar pairs matched similar ones (52% vs 39%, n.s.) [4] (M). Comparing two cases made negotiators nearly 3x as likely to transfer the strategy [5] (M); a 57-experiment meta-analysis favours case comparison over separate study [6] (H nominally; I could not open the paper, the 57-experiment and d about 0.5 figures come from search-result summaries [6]).

**Design-by-analogy**
- 153 engineering students: far-field patent examples raised mean novelty (d=0.56 vs near) and quality variance (d=0.64) with no change in mean or best quality and about one fewer concept; only far plus uncommon examples beat the no-example control [7] (M).
- 707 OpenIDEO concepts: greater mean source distance cut shortlist probability (.13 to .09 per normalised unit); distance was LSA-topical, not structural [8][9] (M, observational). That paper lists studies with equal or harmful far effects. A 26-team study found biological analogies beat within-domain ones on novelty (p=.012) but not cross-domain engineering ones (p=.088), so a "middle" band may suffice [11] (L).
- Function over surface: mapping patents by function vs by noun content gives different neighbourhoods, and functional structure exposes cross-domain transfers [10] (M). AskNature frames biology as "How would nature solve this?" [12] (L).

**Computational retrieval**
- Purpose/mechanism vectors: inspirations with similar purpose but different mechanism produced good ideas 46% of the time vs 37% random and 30% TF-IDF "surface" (38 workers, 9 seeds); precision@5% 0.61 vs 0.54 [13] (M). Functional-facet search beat baselines by 50-60% in user studies [14] (L, abstract only). Scideator retrieves "analogous paper facets" at adjustable distance and beat a same-LLM baseline on creativity support [16] (L). Crowd-plus-AI decomposition of analogy finding is the scaling proposal [15] (L).

**LLMs, 2023-2026**
- Brittle beyond easy cases. GPT-3 matched humans on abstract analogies [23] but counterfactual variants cause sharp drops [24]; LLMs match humans in several conditions yet differ on semantic distractors [25]. On far narrative analogies GPT-4 is below random zero-shot (ARN) [21]; ChatGPT scored about 30% vs humans above 85% (StoryAnalogy) [22]. Relations are encoded but often not applied to new entities [26] (L, abstracts only).
- YARN (structure mapping with LLM-derived abstractions, 8B models): embedding-based mapping without abstraction fell below chance (4-way 0.17 vs 0.25; far ARN 0.24 vs 0.50); conceptual plus evaluative abstractions lifted these to 0.46 and 0.47, beating LLM chain-of-thought on far items (0.41, 0.42) but not near ones (0.69 vs 0.79) [20] (L).
- Princeton (Liu et al. 2026; preregistered; 140 humans, 7 LLMs, 1,002 raters, 2,800 ideas) [17] (M). A random source raised human originality at nearly every distance. LLMs were already more original than humans and gained nothing on average (o3, Claude-Sonnet-4: b=0.02, p=.64), but did on the most distant 50% (b=0.12, p=.029) and 10% (b=0.24, p=.024) of pairs. Humans copied surface features (a green car for "pickle"); LLMs transferred mechanisms (self-healing coating). Originality vs feasibility r=-0.74. Limits: one-shot, lay raters, structure coded by one author.
- Stanford structure-first pipeline (Shen et al. 2026) [18] (L). Extract objects with functional roles and relations, map "by FUNCTION, not surface similarity," search the source domain with the mapping, forbid direct target-domain solutions. Versus asking for domains directly: LLM-judged novel 50-69% vs 22-38%; domain distance more than 3x the no-domain baseline; four experts preferred it for novelty 78% (kappa .445) but rated it "reasonable" 67% vs 86%. Unassigned baselines used only 7-8 distinct domains in 150 generations. Cost was about $0.02 per problem. Four case studies (selection rule unclear) were run with Claude Code and improved benchmarks (a chess-evaluation analogy improved 5 of 6 oligonucleotide datasets). LLM-judged "structural depth" disagreed with humans (kappa -0.13).
- ML research ideation (30 problems, GPT-5 generator, Sonnet judge): cross-domain retrieval did not beat 21 random diverse seeds (14-16, p=.86) and lowered coherence (3.63 to 3.33); systems "do not yet reliably exploit the semantic reason particular seeds were retrieved" [19] (L).
- Analogical prompting (self-generated related exemplars) gave small gains (GSM8K, GPT-3.5: 77.8 vs 76.7 for 5-shot CoT), needs large models, and a common failure (12 of 50 errors reviewed) was exemplars that did not transfer [27] (M). It recalls near problems; it is not far analogy.
- Weak: SciAgents samples randomised paths between distant knowledge-graph concepts for bio-inspired materials, scored only by LLM agents, no validation [29]; Buehler's music-to-materials isomorphisms are abstract-level [29]; MOOSE-Chem splits hypothesis discovery into inspiration retrieval, composition, ranking [30]; an analogy tool raised novelty 3.31 vs 2.21 in 24 students [28] (all L).
- ML precedent: dropout was motivated by a theory of sex in evolution, where recombination breaks co-adapted gene sets [33]; DQN's replay is a "biologically inspired mechanism" [34] (anecdotal).

## 2. What did NOT work, or misled

- Waiting for spontaneous analogy: 30% unprompted [4].
- Surface retrieval: TF-IDF inspirations were no better than random [13]; embedding mapping without abstraction was below chance [20]; topical distance cost shortlist odds [8]; targeted retrieval tied random seeds [19].
- One analog plus summary, principle or diagram [4].
- "Far is always better": variance, not mean or best quality [7]; null or harmful far effects [8][11]; no average gain for strong LLMs [17].
- Novelty bought with feasibility: r=-0.74 [17]; 67% vs 86% reasonable [18]; the advantage of LLM ideas vanished after 43 researchers executed them for 100+ hours each [31].
- LLM judges and mode collapse: structural-depth kappa -0.13 [18]; counterfactual brittleness [24]; LLM raters favour machine text [17]; models share modes [32].
- Humans import surface features [17]; a mapping is a hypothesis and can fail on transfer [27].

## 3. What would transfer to an LLM-driven idea loop

Mechanisms are inferences from the evidence; thresholds are my proposals, not findings. Setting: agents sketch changes to an ML training recipe and a cheap run can test them.

**M1. Schema-first probe.** A schema agent rewrites each sub-problem (LR schedule, data order, batch growth) as 3-6 typed relations over role-named objects with ML nouns removed ("budgeted searcher, noisy progress signal, clock; noise buys exploration, shrinking budget forces commitment"). Embed and query with the schema, never the goal text. Why: access follows surface [2]; purpose/mechanism abstraction beat TF-IDF and random [13]; abstraction lifted mapping above chance [20]. Check: recall@k on a gold set of ML ideas with documented analogical origin (dropout-sex [33], replay [34]) hidden in the corpus.

**M2. Two-stage far retrieval with a distance dial.** Cards: domain, purpose, mechanism, 3-6 typed triples, failure condition, URL, written without domain nouns; include function-indexed biology and operations research, control, ecology, immunology, economics. MAC: top 50 by schema similarity; FAC: structural alignment (M4) keeps about 6 [3]. Measure source-target semantic distance by embedding concept descriptions [17]; stratify into bands; drop the nearest half for strong models [17] but keep a mid band, since far is not monotonic [8][11]. Run purpose-matched, different-mechanism retrieval [13] and random assignment [17] as separate arms.

**M3. Assign sources; do not let agents choose.** Draw without replacement per agent and round from the stratified list, cap per-domain reuse, log domain and band. Why: unassigned LLMs collapse to 7-8 domains [18], models share modes [32]. Check: unique domains and Vendi score of sketches.

**M4. Typed mapping table plus script lint.** Replace the one-line mapping with: objects mapped by function, with valid and invalid examples [18]; at least 3 mapped relations including one higher-order (cause, prevent, trade-off) [1]; the candidate inference (a source relation with no target counterpart yet, which is the proposed change); at least one break (disanalogy). Script checks: one-to-one; parallel connectivity (R(a,b) maps to R'(x,y) implies a to x, b to y); inference uses mapped objects only; no ML nouns in the source write-up. Use separate calls: extract and map, search the source domain with target vocabulary forbidden, translate back [18]. Check: lint pass rate. Worked example (my reconstruction of [33]): gene to hidden unit; co-adapted gene set to co-adapted feature group; recombination to random unit masking; higher-order: selection for mix-ability favours sets that work with many partners, so masking should favour features that work in many subnetworks; candidate inference: gains grow with the size of co-adapted sets; break: genes are exchanged whole, units are only silenced.

**M5. Rename-and-reconstruct audit.** A fresh judge sees the sketch with domain nouns replaced by neutral tokens and must recover the correspondence among distractor sources, including a lexical decoy. Failure marks a decorative analogy, demoted. Why: structure is recoverable by forced choice when retrieval is not [2]; LLMs break under relabelling [24]; far-near items are hardest [20][21]. Calibrate on the gold set and 50 human-labelled items before use (kappa of 0.6 or more is my threshold; [18] shows LLM structure scores at kappa below 0).

**M6. Paired-analog schema induction.** Give each context two analogues from different domains sharing one schema; require the common causal schema written first, then instantiated in the recipe, with the principle stated after the comparison [4][6]. Human evidence only: run it as an arm against single-analog contexts.

**M7. Score by executable evidence; use analogy scores as gates.** Rank by the cheap-test outcome of a PREDICTION derived from the candidate inference, a consequence that holds only if the source's causal structure holds (dropout's recombination story implies larger gains where co-adapted sets are larger [33]). Gates: lint and audit pass, novelty against prior art by retrieve-then-judge, cluster quotas. Never rank by originality: r=-0.74 with feasibility [17], and novelty advantages shrink on execution [31]. Far sources add variance, not mean [7], so sample many cheap sketches and filter hard.

**M8. Measure with arms, executed outcomes, dose-response.** Per sub-problem, same token budget: A no source (needs-based); B random far source with "map a property" [17]; C full M1-M6; D structure-retrieved vs random diverse seeds [19]; E near source for repair. Outcomes: hit rate (sketches beating baseline validation loss at fixed budget, over seeds), best-of-k, distinct mechanism clusters, novelty vs prior art with a 10-20% blind human audit, structural-transfer code 1-5 by two coders [17], hit rate by distance bin, tokens per surviving idea. Analysis: mixed models with random effects for target and source [17], preregistered; n=30 could not separate conditions [19], so plan 100 or more paired items or many executed sketches per arm. Keep LLM raters secondary [17].

**Delta vs this repo (inference from reading the code).** nano/research.py lets one call pick 5 fields and nano/ideate.py asks only for a one-line MAPPING; nothing in nano/ implements M1, M3, M5, M6 or M8. ARCHITECTURE.md (Pr9) plans two far sources from a fixed corpus and script-checked typed triples, but selects sources by goal-text embedding, which retrieves by surface (M1).

## 4. Gaps

No study tests far analogy for ML training recipes with executed outcomes beyond four case studies [18]; paired-analog encoding is untested on LLMs; distance measures here are topical (embeddings, LSA), not structural; I found nothing solid on analogical materials discovery beyond [29]; AskNature and bio-inspired LLM design evidence is thin [11][12].

## Sources

1. Gentner 1983, Structure-mapping: https://groups.psych.northwestern.edu/gentner/papers/Gentner83.pdf
2. Gentner, Rattermann, Forbus 1993: https://groups.psych.northwestern.edu/gentner/papers/GentnerRattForbus93.pdf
3. MAC/FAC (Forbus, Gentner, Law): https://www.qrg.northwestern.edu/ideas/macfac.htm
4. Gick, Holyoak 1983, Schema induction: https://www.gwern.net/doc/psychology/1983-gick.pdf
5. Loewenstein, Thompson, Gentner 1999: https://www.kellogg.northwestern.edu/faculty/research/detail/1999/analogical-encoding-facilitates-knowledge-transfer-in-negotiation
6. Alfieri, Nokes-Malach, Schunn 2013: https://doi.org/10.1080/00461520.2013.775712 ; summary page: https://www.academia.edu/3708913/Learning_through_Case_Comparisons_A_Meta_Analytic_Review
7. Chan et al. 2011: https://edrl.engr.wisc.edu/wp-content/uploads/sites/142/2022/02/2011-jmd-distancecommonness.pdf
8. Chan, Schunn, Dow 2014 (CogSci): https://escholarship.org/uc/item/2bm91572
9. Chan, Dow, Schunn 2015 summary: https://www.hcii.cmu.edu/news/think-outside-box-not-so-fast
10. Fu et al. 2013, J Mech Des 135(3): https://edrl.engr.wisc.edu/wp-content/uploads/sites/142/2022/02/md_135_3_031006.pdf
11. Keshwani, Casakin 2024: https://pmc.ncbi.nlm.nih.gov/articles/PMC11201427/
12. Biomimicry Institute (AskNature): https://biomimicry.org/
13. Hope et al. 2017: https://ar5iv.labs.arxiv.org/html/1706.05585
14. Hope et al. 2022: https://arxiv.org/abs/2102.09761
15. Kittur et al. 2019: https://cris.huji.ac.il/en/publications/scaling-up-analogical-innovation-with-crowds-and-ai/
16. Radensky et al., Scideator: https://arxiv.org/abs/2409.14634
17. Liu et al. 2026 (Princeton): https://arxiv.org/html/2603.19087v3
18. Shen, Druckmann, Zou 2026: https://arxiv.org/html/2605.11258v1
19. Choi, Song 2026: https://arxiv.org/html/2605.11532v1
20. Khojasteh et al. 2026 (YARN): https://arxiv.org/html/2603.29997
21. Sourati et al. 2024 (ARN): https://aclanthology.org/2024.tacl-1.59/
22. Jiayang et al. 2023 (StoryAnalogy): https://aclanthology.org/2023.emnlp-main.706/
23. Webb, Holyoak, Lu 2023: https://arxiv.org/abs/2212.09196
24. Lewis, Mitchell 2024: https://arxiv.org/abs/2402.08955
25. Musker et al. 2025: https://arxiv.org/abs/2406.13803
26. Opielka et al. 2025: https://arxiv.org/abs/2503.03666 ; Lee et al. 2025: https://arxiv.org/abs/2511.20344
27. Yasunaga et al. 2024: https://ar5iv.labs.arxiv.org/html/2310.01714
28. Kokate, Onkar 2026: https://www.cambridge.org/core/journals/design-science/article/analogical-reasoning-with-large-language-models-a-cocreative-framework-and-benchmarking-of-llms-in-design-ideation/0B8149CCF53C45E1E1B78C4CA93E5BDC
29. SciAgents: https://arxiv.org/html/2409.05556 ; Buehler 2024: https://arxiv.org/abs/2403.11996
30. MOOSE-Chem: https://arxiv.org/abs/2410.07076
31. Si, Hashimoto, Yang 2025: https://arxiv.org/abs/2506.20803
32. Jiang et al. 2025 (Artificial Hivemind): https://arxiv.org/abs/2510.22954
33. Srivastava et al. 2014 (dropout): https://jmlr.org/papers/volume15/srivastava14a/srivastava14a.pdf
34. Mnih et al. 2015 (DQN): https://storage.googleapis.com/deepmind-media/dqn/DQNNaturePaper.pdf
