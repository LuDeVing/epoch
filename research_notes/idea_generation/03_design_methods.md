# 03 - Systematic invention and design methods as idea-generation theory (2026-10-13)

Scope: design and invention methods, and 2024-2026 LLM work. Strength labels: MODERATE (a few controlled or protocol studies), WEAK (small, uncontrolled, or case collections), FOLKLORE (repeated, untested). Nothing reached STRONG. Limits: the session shared web-search budget ran out mid-run, so "(snippet)" marks claims that rest on search-result summaries, and several publisher pages (ACM, ASME, Springer, Wiley, T&F) refused fetches. Section 6 lists what stays unverified.

## 1. Bottom line

1. No method I could document has strong evidence as a predictor of better ideas. A systematic review of design-method evaluations found every link of the evidence chain somewhere, but no paper reporting all of them or following best practice [S16].
2. What is evidenced is narrow and mechanism-level: parallel beats serial exploration (snippet) [S29]; expansive examples raise originality and restrictive ones lower it [S13]; problem and solution frames co-evolve in creative design [S14, S15]; variation moves used by designers correlate with creativity [S30].
3. For LLMs, method structure helps less than hoped. Short prompts asking for wild ideas outside the usual categories matched or beat method-faithful TRIZ, C-K and SCAMPER prompts [S10]; an LLM agent running C-K lost diversity in every condition [S11]; extracting the contradiction is the weak TRIZ step [S5-S7].
4. Real gains in LLM design loops come from variation operators plus automated evaluators [S34, S35]. Use methods to shape proposals; let verification decide.

## 2. Evidence by method

| Method | Evidence found | Strength |
|---|---|---|
| TRIZ matrix + 40 principles | Three-university student study (control/TRIZ 21/9 and 20/21 at two sites): novelty and variety up, quantity down; novelty p-values .0004, .0145, .58 across sites, quantity n.s. (p=.29-.63) [S1]. fNIRS study, N=32: TRIZ cut fluency (2.34 vs 3.44, p=.002), raised elaboration, human+TRIZ had the lowest originality (1.20 vs 3.56) [S2]. Practitioner survey: structure helps, complexity hinders [S42]. Matrix fits ~50% of patents (Mann; snippet) [S21]. | WEAK |
| ARIZ, IFR, ideality | IFR = result "achieved by itself" [S43]. No controlled test of ARIZ, or of ideality as a selection criterion, found. | FOLKLORE |
| Evolution trends | Technology performance often moves in steps, not one S-curve (Sood and Tellis; 23 technologies in the working paper; the step finding is snippet-level) [S22]. | FOLKLORE as forecast |
| C-K theory | Two industrial cases written by the authors [S12]; two experiments, restrictive vs expansive examples [S13]; LLM-agent simulation [S11]. | MODERATE for the expansive/restrictive mechanism (two experiments, sizes unseen); WEAK for method effectiveness |
| Morphological analysis (Zwicky, Ritchey) | Author-reported >100 projects, no controlled comparison [S17]. The pairwise-vs-combinatorial argument is arithmetic, not evidence of better ideas. | WEAK |
| SIT templates | Closed world plus five templates (subtraction, multiplication, division, task unification, attribute dependency) [S19]; the 1999 JMR paper reports two ideation experiments, results not in the abstract [S45]. | WEAK |
| SCAMPER | Small school trials (n=21 vs 22; 40; 49; snippet) [S24]; creativity-enhancement meta-analysis g=0.53 over 332 effects, no SCAMPER estimate in the abstract [S23]; a SCAMPER prompt did not reliably lift LLM novelty [S10]. | WEAK |
| Lateral thinking | Critics call it untested; support is one student study (secondary) [S25]. | FOLKLORE |
| Design thinking | Essay critiques [S26, S27]; education reviews find thin, short-term evidence with few controls (snippet) [S28]. | WEAK |
| Problem-solution co-evolution | Protocol study of 9 industrial designers [S14]; 16 DRS papers build on it, mostly conceptual [S15]. | WEAK to MODERATE, descriptive |
| Functional decomposition | Novice teams (n=25): top-down and energy-flow similar, enumeration worse; 78 industry design reports: no correlation between using decomposition and design grade; authors suggest it aids team communication [S44]. Least-to-most decomposition lifts LLM reasoning (SCAN 99% vs 16%), not ideation [S40]. | WEAK |
| Design heuristics | 77 heuristics from >3,450 outcomes (snippet) [S30]; N=24: heuristics per concept vs creativity r=.51, vs set diversity r=-.38 (p=.06) [S30]. | WEAK, observational |

## 3. Evidenced vs folklore

Evidenced (weakly to moderately): section 1 items 2-3 and the MODERATE rows.

Folklore to drop: the patent base behind TRIZ (>200,000 in one source [S19], >400,000 for 1946-85 in another [S20], neither with a primary count); "the matrix resolves any contradiction"; evolution laws as forecasts; ideality as a proven criterion; the claims of de Bono; "SCAMPER" or "design thinking is proven"; LLM-TRIZ "validation" by 3-84 textbook cases, embedding similarity to a known answer, or one to two expert raters [S4-S6].

## 4. 2024-2026 LLM work

- LLM-TRIZ pipelines. AutoTRIZ (GPT-4: the LLM picks one improving and one worsening parameter, a script looks up the matrix, the LLM writes solutions): 7 of 10 textbook cases matched or half-matched in the top 3; the authors admit no objective effectiveness test [S5]. TRIZ-GPT: contradiction recall 0.69 but precision 0.26-0.33 (34 cases); solution-to-textbook cosine ~0.82 whatever the prompt [S6]. TRIZBench (ACL Findings 2026): spotting contradictions is easier than recovering the right trade-off pair [S7]. TRIZ-RAGNER: F1 84.2 mining contradictions from patents [S8]. TRIZ Agents (8 agents, one case, no baseline) [S9]. LLM-assisted morphological analysis claims gains; no numbers seen [S18].
- Experiments. GPT-3.5 with TRIZ beat textbook solutions on novelty, variety, quantity over 3 problems; quality varied widely [S4]. About 110 students: an LLM eased defining contradictions (d=-0.78) but the quality main effect was n.s. (p=.076) [S3].
- IDEAFix (May 2026; 81 briefs, 25 prompts, 5 LLMs, embedding metrics): all method prompts beat control, none won every metric; C-K and SCAMPER prompts did not reliably lift novelty; short prompts asking for wild, unconventional ideas beyond frequently used categories beat complex method prompts; surprising or negative framing raised novelty but cut diversity; homogenization persisted. Single-shot, proxy metrics [S10].
- C-K with LLM agents (J. Mech. Des. 2026): concept-to-concept steps dominated; forced knowledge visits did not stop diversity falling in GPT-4o, GPT-4.5 and GPT-5 runs; the authors suspect how K is restructured matters, not whether it is visited [S11].
- Ideation hygiene: at 4,000 seeds ~5% survive deduplication, AI ideas rated more novel (5.64 vs 4.84) and slightly less feasible, reviewer agreement 56% [S31]; models converge on similar outputs and judges miscalibrate where humans disagree [S32]; judges favor style (bias index 0.566) [S33].
- Design-synthesis analogues: AlphaEvolve requires automated evaluators [S34]; ELM pairs LLM mutation with a MAP-Elites archive [S35]. Tool-connected design agents: a two-agent generator-reflector loop collapsed into repetitive outputs, nine roles gave more detail, but requirement coverage stayed under 20% [S46]; in training-code authoring, agents filled small gaps reliably but diverged as larger regions were left open [S47]. Closest to this project, the NanoGPT speedrun benchmark: <20% of record speedups unaided, ~40-46% with pseudocode hints; buggy code was a major limiter; flat best-of-M matched iterated scaffolds [S36]. Abstraction-first, self-made analogies and model-chosen reasoning modules help LLM reasoning benchmarks (+7-27% [S37], [S38], up to +32% [S39]), not ideation.

## 5. What would transfer to an LLM-driven idea loop

Pipeline hooks checked in code: cards cycle round-robin (nano/loop.py:352); the problem tree is planned once (loop.py:336); history_text lists built hypotheses and outcomes only (loop.py:754); selection is the weighted cluster_score (nano/ideate.py). Mechanisms 1-4 can run as extra cards inside the round-robin and be read off the ledger, as the research card already is. Effects below are predictions; sizes are unknown. Measure proxies first (tag shares, embedding diversity, rung pass rates) and verified wins last, because wins are rare.

1. **Measured-contradiction cards.** Mine trade-offs from the ledger and diagnostics (loss down, but step time, VRAM, parameters or seed variance up) into a per-part register; a card hands one row to a context and asks for sketches that keep the gain and remove the cost, naming the separation (by phase, by layer, by condition). LLM extraction is the weak step [S5-S7], so measure it instead of asking. Effect: more targeted sketches, fewer known ones. Measure: card vs formal and diagnosis cards on share of clusters tagged new, rung-3 pass rate, verified wins per build (30+ sketches per arm); predict.py can check whether the claimed side moved.
2. **Operator cards, one per context, drawn without replacement.** About 10 ML moves translated from TRIZ principles (segmentation to per-group optimizers, taking out to dropping warmup, self-service to EMA or self-distillation; my translation, no source) plus the 5 SIT templates applied to existing script parts. Evidence: TRIZ stimuli lift novelty and cut quantity [S1], but plain prompts rival method prompts [S10], so run it as a challenger arm. Effect: higher novelty, fewer sketches per call. Measure: operator field in the ledger; per-operator new-tag share and hit rate; drop an operator after 8 builds with no hit; novelty as embedding distance from control sketches [S10, S11].
3. **Outside-the-categories rounds.** After blind clustering, give round-2 contexts only the cluster names as an exclusion list, plus a wild-and-unconventional framing on a subset. Later contexts now see built outcomes but not proposed-yet-unbuilt categories (loop.py:754). Evidence: [S10] (framing raises novelty, lowers diversity; homogenization persists across models [S32]). Effect: more distinct clusters, lower build-pass rate. Measure: matched contexts with and without the list; new clusters, diversity (DPP or mean distance to centroid as in [S11]), rung-2 pass rate.
4. **Expansive tagging and knowledge splitting (C-K).** Tag each cluster restrictive (property already known for that part in the brief or baseline) or expansive (property from elsewhere, not known for the part). Give each context a disjoint knowledge pack stated as properties, not solved designs, and weight expansive clusters with cheap tests. Evidence: [S13]; forced knowledge visits did not stop LLM convergence, and the authors point to missing K splitting or reordering (untested) [S11]. Effect: fewer duplicate and known clusters. Measure: docs as solutions vs docs as properties vs none, same part: duplicate rate at cosine 0.8 (about 5% survive at 4,000 seeds [S31]), new-tag share.
5. **Re-frame between rounds (co-evolution).** The tree is planned once (loop.py:336). After each verification batch a reframe call reads ledger, diagnostics, pre-mortem objections and failed rungs, retires falsified assumptions, adds one or two that the results revealed, and may split or merge nodes. Evidence: [S14, S15]; framing effects [S10]. Effect: fewer repeated dead ends in round 2. Measure: fixed-tree vs reframed arm at equal tokens: round-2 share of new vs known or failed clusters, verified wins per million tokens, assumptions changed per round (thrash check).
6. **Ideality, resource questions and trimming.** Interrogation asks two TRIZ-style questions per idea: what is the ideal final result, and which quantity already in the script could do this job for free (resources; SIT closed world [S19]). Score = predicted gain / measured cost, with cost from rung 1-2 numbers: parameters, step time, VRAM, diff size, new hyperparameters. Add it to cluster_score; after rung 3 a trimming call removes diff parts and keeps what the gain needs. Never ask an LLM judge for ideality [S33, S31]. Evidence: no controlled test of ideality [S43]; bugs limit agents [S36]; compose.py needs disjoint edits. Effect: smaller, more composable diffs; risk of conservative picks. Measure: Spearman or AUC of score vs verified gap via calibrate.py; diff size and composite success before vs after trimming, gain preserved.
7. **Morphological field with cross-consistency checks.** Rows = parts, cells = checked candidates; judge pairs (script for symbol overlap, one cheap call for semantic conflict) and build only consistent combinations with compose.py; 100,000 configurations need a few hundred pair judgments [S17]. Evidence: arithmetic only [S17]; stacking is hard (best agent kept ~60%, then ~20%, then none of successive records [S36]). Effect: stacking wins found cheaper than by random pairing. Measure: stacking rate (composite beats both parents), judgment precision against rung-3 failures, cost per stacking hit vs random pairs.
8. **Empirical contradiction matrix: a bandit over cards and operators.** Replace round-robin (loop.py:352) with Thompson sampling over (part, card or operator) from ledger hit rates, with a 20% random floor, refreshed each batch so it cannot go stale as the TRIZ matrix did (~50% fit [S21]). Evidence: model-chosen reasoning modules beat fixed prompts [S39], on reasoning benchmarks only. Effect: more hits per token after about two batches; risk of early lock-in. Measure: offline replay on past ledgers, expected hits vs round-robin; then online against the random floor.

Suggested order: 3, 1, 5 and 6 first (cheap, reuse existing data); 2 and 4 as card A/Bs; 7 and 8 once the ledger holds 100 builds.

## 6. Not verified

Full texts of the TRIZ case-study survey [S41] and the practitioner survey [S42]; the 50% matrix fit and the semiconductor-matrix result [S21]; the step-function finding [S22]; education reviews of design thinking [S28]; numbers of the parallel-prototyping study [S29]; de Bono evaluations; Scott et al. 2004; classic computational-design-synthesis reviews; the SIT experiment results [S45]; any TRIZ-for-ML source (none found); ARIZ steps and the ideality formula (no fetchable source). No pipeline experiment was run; every effect above is a prediction.

## Sources

Opened (full text or abstract) unless marked snippet or secondary.

- [S1] Hernandez, Schmidt, Okudan Kremer 2012, ASEE: https://peer.asee.org/experimental-assessment-of-triz-effectiveness-in-idea-generation.pdf
- [S2] Ge et al. 2025, AI EDAM: https://www.cambridge.org/core/journals/ai-edam/article/comparing-triz-and-brainstorming-in-humanagent-design-collaboration-effects-on-cognitive-processes-and-performance/6C9C84A5D1956B702F71AA7F7193D22C
- [S3] Cok et al. 2026, DESIGN 2026: https://www.cambridge.org/core/product/09B3955101E1013E73E8EB6C528DAE56/core-reader
- [S4] Mohammadi and Zeng 2025, AI EDAM: https://www.cambridge.org/core/product/C3305E839793A17763076FF8BF510E08/core-reader
- [S5] AutoTRIZ (Jiang et al.): https://arxiv.org/html/2403.13002v4
- [S6] TRIZ-GPT (Chen et al. 2024): https://arxiv.org/pdf/2408.05897
- [S7] TRIZBench (Wang, Uzzi 2026): https://aclanthology.org/2026.findings-acl.1798/
- [S8] TRIZ-RAGNER 2026: https://arxiv.org/abs/2602.23656
- [S9] TRIZ Agents 2025: https://arxiv.org/html/2506.18783v1
- [S10] IDEAFix 2026 (full text): https://arxiv.org/pdf/2606.00875
- [S11] Ma, Brubaker, Goucher-Lambert 2026 (full text): https://codesign.berkeley.edu/papers/ma-ck-jmd/
- [S12] Hatchuel, Le Masson, Weil 2004: https://www.designsociety.org/download-publication/19760/c-k_theory_in_practice_lessons_from_industrial_applica
- [S13] Agogue et al. 2014: https://ideas.repec.org/p/hal/journl/hal-00707354.html
- [S14] Dorst and Cross 2001: https://research.tue.nl/en/publications/creativity-in-the-design-process-co-evolution-of-problem-solution/
- [S15] Biskjaer, Halskov, de Rooij 2026: https://dl.designresearchsociety.org/drs-conference-papers/drs2026/researchpapers/240
- [S16] Cash, Daalhuizen, Hekkert 2023: https://research.tudelft.nl/en/publications/6ad1443b-844e-4caf-b2f1-2682ce25f991
- [S17] Ritchey, morphological analysis: https://www.swemorph.com/ma.html
- [S18] Chen et al. DRS 2024: https://dl.designresearchsociety.org/drs-conference-papers/drs2024/researchpapers/152
- [S19] SIT (secondary): https://en.wikipedia.org/wiki/Systematic_inventive_thinking
- [S20] TRIZ overview (secondary): https://www.triz40.com/triz-method.php
- [S21] Matrix fit and semiconductor matrix (snippet; pages blocked): https://onlinelibrary.wiley.com/doi/full/10.1002/cite.202100205 and https://doi.org/10.1007/s10845-010-0466-4
- [S22] Sood and Tellis, MSI working paper (step finding snippet): https://www.msi.org/working-papers/the-scurve-of-technological-evolution-strategic-law-or-selffulfilling-prophecy/
- [S23] Haase, Hanel, Gronau meta-analysis: https://edoc.hu-berlin.de/items/a8357c0b-1e41-4eff-8ad1-fe3b5355a831
- [S24] SCAMPER trials (snippets): https://acikerisim.bartin.edu.tr/entities/publication/0b882eaf-5e7d-4daf-a5e9-87ce5413929a , https://openaccess.ahievran.edu.tr/items/e3048ce3-a992-456e-a419-291efae90d2f , https://journals.vilniustech.lt/index.php/CS/article/view/11201
- [S25] Lateral thinking (secondary): https://en.wikipedia.org/wiki/Lateral_thinking
- [S26] Norman 2010: https://www.core77.com/posts/16790/Design-Thinking-A-Useful-Myth
- [S27] Design thinking critiques (secondary): https://en.wikipedia.org/wiki/Design_thinking
- [S28] Design thinking reviews (snippets): https://doi.org/10.1080/03043797.2026.2640060 , https://link.springer.com/article/10.1007/s44217-026-02088-3 , https://www.researchgate.net/publication/362701861_A_Systematic_Review_on_Design_Thinking_Integrated_Learning_in_K-12_Education
- [S29] Dow et al. 2010 (metadata page; results from search summary): https://protolab.ucsd.edu/?p=3561
- [S30] Yilmaz et al. (2015 study read; 77-heuristics paper snippet): https://www.cambridge.org/core/product/FD0A4BE84DD124CFBB2253A1DFAB18FD/core-reader , https://works.bepress.com/seda-yilmaz/36
- [S31] Si, Yang, Hashimoto 2024 (full text): https://arxiv.org/abs/2409.04109
- [S32] Artificial Hivemind: https://arxiv.org/abs/2510.22954
- [S33] Style Wins, Substance Loses 2026: https://arxiv.org/abs/2608.01666
- [S34] AlphaEvolve: https://arxiv.org/abs/2506.13131
- [S35] Evolution through Large Models: https://arxiv.org/abs/2206.08896
- [S36] Automated LLM Speedrunning Benchmark: https://arxiv.org/abs/2506.22419
- [S37] Step-back prompting: https://arxiv.org/abs/2310.06117
- [S38] Analogical prompting: https://arxiv.org/abs/2310.01714
- [S39] Self-Discover: https://arxiv.org/abs/2402.03620
- [S40] Least-to-most prompting: https://arxiv.org/abs/2205.10625
- [S41] Spreafico and Russo 2016 (snippet): https://aisberg.unibg.it/handle/10446/53868
- [S42] Ilevbare, Probert, Phaal 2013 (summary page): https://www.rndtoday.co.uk/?p=552
- [S43] Ideal final result (secondary): https://en.wikipedia.org/wiki/Ideal_final_result
- [S44] Booth, Bhasin, Reid, Ramani 2015, functional decomposition: https://engineering.purdue.edu/cdesign/wp/wp-content/uploads/2015/08/IDETC2015-47865-Empirical-Studies-of-Functional-Decomposition-in-Early-Design.pdf
- [S45] Goldenberg, Mazursky, Solomon 1999, JMR (abstract): https://cris.huji.ac.il/en/publications/toward-identifying-the-inventive-templates-of-new-products-a-chan/
- [S46] Massoudi and Fuge 2025: https://arxiv.org/abs/2507.08619
- [S47] Molinari et al. 2026 (EngiAI): https://arxiv.org/abs/2605.19743
