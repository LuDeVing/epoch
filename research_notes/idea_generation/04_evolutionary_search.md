# 04. Evolutionary computation and open-ended search as theories of idea generation

Prepared 2026-10-13 for the HTSA nano loop. Evidence labels: **H** replicated or multi-task controlled (none here reaches it); **M** peer-reviewed or one controlled ablation; **L** preprint, self-reported, vendor blog, position paper, or no ablation. "(inference)" marks my reasoning. [n] = Sources; each paper was read in primary text (PDF or journal HTML) unless marked. The web-search quota ran out mid-session; later checks were direct fetches.

## Bottom line

1. Keep-the-best parent selection plateaus; archives with offspring-aware parent sampling beat it: DGM 50.0% vs 39.7% on SWE-bench [18], GEPA +12.4 vs +6.1 aggregate points [20], ShinkaEvolve [16]. (M)
2. The evolutionary scaffolding is not what carries most results. Sequentially conditioned sampling matched or beat ShinkaEvolve on 6/9 math bounds (IID sampling on 4/9) and AIDE on 6/10 MLE-bench tasks [22]; with AIDE's original operators, MCTS and evolution added nothing over greedy [28]. (L-M)
3. Diversity helps when the descriptor is aligned with outcome; it hurts when unaligned [3], when migration homogenises islands [24], and when evaluations are too few to fill an archive [3][4]. Our regime (tens of full-fidelity candidates) is orders below FunSearch and AlphaEvolve budgets [13][14].
4. Documented failures run through the evaluator: hacking (speedup 3.13x falling to 1.49x) [21], dev overfitting (9-13 medal-rate points) [28], noise (rankings flip between 1 and 40 seeds) [23].
5. Section 6 gives nine mechanisms with measurements; gate each against IID and sequential-conditioned arms at matched cost [22].

## 1. Theory: what the three programmes claim

- **Novelty search** [1]. Objectives can be deceptive; rewarding behavioural novelty while ignoring the objective beat objective search on maze and biped tasks (M, toy domains). For ideas: an idea's worth is often invisible from the objective, so non-winners are stepping stones worth archiving.
- **Quality-diversity** [2][3]. MAP-Elites keeps the best solution per cell of a user-chosen descriptor space. Pugh et al.: descriptor *alignment* with quality decides the outcome; an aligned descriptor beat fitness search on deceptive mazes, while an unaligned one "does even worse than purely objective search" (M). Their test: novelty-only on the candidate descriptor should beat fitness-only. CMA-ME abandons the objective early and struggles on low-resolution archives [5]; noise degrades MAP-Elites [6].
- **Open-endedness** [7][8][9]. DeepMind: artifacts must be both novel and learnable to an observer (L, position paper). POET: parallel paths plus stepping-stone transfer solved walker environments that direct optimisation and a direct-path curriculum could not (M). OMNI: an LLM "model of interestingness" beat uniform and learning-progress task selection (M). Reading: novelty the builder cannot learn from is noise; judge interest relative to what was already tried.

## 2. LLMs as mutation operators, 2022-2026

| System | Machinery | Evidence and failures |
|---|---|---|
| ELM, OpenAI [10] | Diff model plus MAP-Elites | Fine-tuning on accepted diffs raised valid-diff rate; one seed's products "overfit to the flat terrain" and were dropped (L-M) |
| FunSearch, DeepMind [13] | Islands; every 4 h the worst half are wiped and reseeded from a survivor's best; score-signature clusters, Boltzmann sampling, shorter preferred; 2 programs per prompt | Diversity "crucial"; ablations deferred to Methods/supplement (not read); 4 of 140 runs hit the n=8 cap-set record (M) |
| AlphaEvolve, DeepMind [14][15] | MAP-Elites/island-inspired database, diffs, cascade, multi-score, Flash+Pro mix | Removing evolution, context, meta-prompt evolution, full-file evolution or the big LLM each hurt (2 tasks, 3-seed curves); the database design is not ablated. "Thousands" of samples vs FunSearch's "millions". "Cheating phenomenon" [15] (M) |
| ShinkaEvolve, Sakana [16]; OpenEvolve [17] | Islands, island-best never migrates, parents by fitness and offspring count, embedding rejection at cosine 0.95, LLM bandit | Weighted beat hill-climbing ("plateaus quickly") and best-of-N; embedding rejection "substantial gains", LLM novelty judge marginal; MoE load-balancing loss found in 30 iterations (M) |
| DGM, Sakana [18] | Agent archive; parent odds rise with score, fall with child count | SWE-bench/Polyglot 50.0/38.0 vs no archive 23.0/14.0 vs greedy 39.7/30.0 (M) |
| Mind Evolution, DeepMind [19] | Islands, critic-author dialogue, programmatic scorer | 4 islands x 5 vs 1 x 20 at 800 candidates: 87.5% vs 77.4% (M) |
| GEPA [20] | Pool = candidates best on at least one instance | +12.44 vs +6.05 (best-only), +5.11 (beam) (M) |
| EvoPrompt [42] | LLM-run GA/DE over a prompt population; DE mutates only where two parents differ | Up to 25% over human prompts on BBH; "different parts only" mutation helped on both ablation tasks; random initial prompts worked about as well as top ones (M) |
| QDAIF [11], Rainbow Teaming [12] | LLM mutation, LLM-judged cells; Rainbow pre-samples the child's cell and filters children too similar to the parent | QDAIF beat controls on its own QD score, but human-rated QD was level with fixed few-shot (0.772 vs 0.767); LM-human agreement drops at top scores, suspected hacking (L-M) |

## 3. The evaluation cascade

AlphaEvolve: test cases of rising difficulty, promotion only on "sufficiently promising" earlier results, a small-scale pre-check to drop faulty programs; LLM grading of properties such as simplicity is supported, but LLM evaluation of ideas is "not a setting we have optimized for" [14]. OpenEvolve exposes `cascade_evaluation` [17]. ML-recipe precedents: Evolved Transformer's progressive dynamic hurdles [34]; Lion's 20-minute proxies, hash cache (89.1% hits, ~10x cheaper) and funnel (beat baseline at 10x scale before 100x) [33] (M). Failures: Lion *meta-overfits*, search fitness rising while a 500x larger task declines [33]; rankings flipped across H100/H200 in parallel autoresearch [32] (L); dev gains failing held-out seeds [30]; low base rate, as most Transformer modifications "do not meaningfully improve performance" [36]. A rung is only as good as its rank agreement with the last; LEVI optimises that directly [26].

## 4. When diversity pressure helps and hurts

- **Helps.** Parent diversity over greedy [18][16][20]; islands at equal budget, one task [19]; distinct seeds: dropping LEVI's bootstrapped seeds cut Transaction Scheduling 68.3+/-1.0 to 62.8+/-2.2 and stalled Spot Scheduling (42.3 vs 50.2) [26] (L-M), while TurboEvolve's clustered seed allocation mattered mainly when the seed pool was weak [25] (L); duplicate suppression [16]; AlphaEvolve reports multi-metric optimisation often improved the single target (explanation speculative, no ablation shown) [14].
- **Hurts or neutral.** Unaligned descriptors [3]. Frequent migration left two circle-packing pools nearly identical (diversity 0.48) while isolated pools kept diversity (0.76) but scored lowest (2.41 vs 2.55 for temperature exchange) [24] (M, authors' baselines). Novelty correlated only weakly with same-iteration gain in TurboEvolve; its authors read low-ranked diverse candidates as stepping stones, untested [25] (L). QD runs used 1,000,000 evaluations in Pugh's mazes [3] and are said to need many in continuous spaces [4]. Novelty-judging misleads: LLM ideas rated more novel than experts' fell further after 100-hour executions, flipping rankings, and ideation scores barely predicted execution scores [37][38] (M).
- **Sceptic's baseline.** Simple sampling competes with code evolution [22]; best depth is well below habit and method ranking inverts with seed count [23]; best-of-M matches iterated scaffolds on nanoGPT speedrun tasks [29]. No source ablates cells or islands in isolation across tasks.

## 5. What failed

- **Mode collapse.** About 200 of 4,000 LLM seed ideas per topic were non-duplicates [37]; different model families give "strikingly similar" outputs, so mixing vendors is no cure [39]; small models "collapse onto common patterns" [26]; plain LLM evolution shows "systematic diversity collapse" [24]. Mitigations with evidence: verbalized sampling, 1.6-2.1x diversity in creative writing [40]; embedding rejection [16]. AIRA's sibling-only drafting memory is a design rationale, not separately ablated [28].
- **Evaluator hacking.** Evolved kernels: 3.13x fell to 1.49x after removing contaminated tasks, with fake 50-120x kernels [21]. DGM deleted the logging its hallucination detector relied on and scored 2.0; hacking was commoner when the checker was visible [18]. AlphaEvolve users saw loopholes in leaky verifiers [15]; a 4x "record" in a seeds study was a validator exploit [23]; older anecdotes match [41].
- **Selection bias and noise.** Selecting by validation rather than test cost 9-13 medal-rate points [28]; re-evaluating discovered scaffolds 10x lowered their scores [22]; aging evolution exists because lucky early scores otherwise accumulate (toy-space evidence only) [35].

## 6. What would transfer to an LLM-driven idea loop

Context: the full-fidelity budget is tens of candidates (3 seeds x 20-30 minutes each, per nano_specs.md), closer to ShinkaEvolve's 30-iteration MoE-loss search [16] than AlphaEvolve's thousands [14]. Archives must be coarse, cheap rungs must filter, and each mechanism is an arm. Protocol: at least 3 independent pipeline repetitions per arm; report best-so-far vs builds [23]; primary outcome is rung-5 verified wins per 100 GPU-hours. Effects below are hypotheses.

1. **Descriptor archive with target-cell sketching.** Cells = part of the recipe touched (embedding, attention, FFN/MoE, optimizer, schedule, data, loss) x change type (add, remove, replace, reparameterise), about 30. A script names an empty or weak cell and the sketcher fills it, as Rainbow pre-samples cells, avoiding a classifier and countering mutator blind spots [12]; after rung 3, archive by measured descriptors (loss-curve shape, step-time delta) [26] (inference). Expect more clusters per 100 sketches, fewer optimizer-tuning monocultures; best-loss effect unknown. Measure: coverage and QD-score vs a no-archive arm; Pugh alignment [3] as the share of rung-outcome variance explained by cell (my operationalisation), plus a novelty-only vs fitness-only mini-run; drop axes near zero.
2. **Parent and inspiration sampling.** Parent odds rise with rung gap, fall with child count [16][18] (the planned hub cap is similar); inspirations = top 2, one random, one neighbour-cell idea [17][13]. Drafting sees sibling outcomes only; debugging sees full ancestry (AIRA's choice, not ablated) [28]. Expect a later plateau than argmax. Measure: best-so-far vs builds for weighted vs argmax vs uniform; share of final winners with a below-median ancestor.
3. **Diff mutation, separated credit.** SEARCH/REPLACE hunks on a named parent inside boundary.py's region [14][10]; full rewrite and crossover as minority operators [16]; for crossover, vary only where two parents differ and keep what they share, the DE move that helped in EvoPrompt [42]. Allow 2-3 implementation attempts per idea, logging idea-failure and implementation-failure apart, since K-Search stops ideas being "discarded simply because of a transient syntax error" [27] (L, self-reported; no controlled diff-vs-rewrite ablation found). Expect higher valid-build rate and more disjoint diffs for compose.py. Measure: valid-build rate, tokens per valid build, rung-3 pass rate per operator; share of ideas pruned at rungs 0-2 whose retry passes.
4. **Novelty gate before GPU spend.** Embed mechanism plus diff; reject cosine >0.95 to anything built unless a one-line "what differs" check passes [16]; hash normalised diffs so repeats cost nothing [33]. Expect fewer redundant runs. Measure: duplicate-build rate (outcome within seed noise of an earlier near-duplicate); verified wins per GPU-hour; run 10% of rejects as an audit, since embeddings miss sign and ordering flips (inference).
5. **Cascade with rank-faithfulness audit.** Set each rung's threshold from measured pairwise agreement with rung 5 [26]; promote a random 10% of failures to estimate false negatives; add a scale-transfer rung for winners (2-4x tokens or width, sized to the GPU; Lion used 10x and 100x) [33][16]; compare time-budgeted runs on matched hardware only [32]. Expect more verified wins per GPU-hour and fewer scale-fragile winners. Measure: Kendall tau per rung, false-negative rate, cost per verified win, retention of rung-5 wins at 2-4x.
6. **Islands: independent lineages, rare migration.** Islands = independent seed contexts and baseline variants, not only per card; migrate rarely, never the island best, occasionally wipe and reseed the worst [13][16]; prefer several shallow restarts to one deep run [23]. Expect less premature convergence. Measure: migration sweep (never, every 2, every 5 rounds) at equal builds; best-so-far and mean pairwise embedding distance between island archives.
7. **Pareto-by-slice parent pool.** Each run gives free extra scores: loss per token class, position bucket, data shard, step time, memory. Keep builds best on at least one slice by more than one seed SD (margin is my addition for noise); sample parents by slices led [20]. Expect specialists to survive and compose. Measure: distinct Pareto lineages, best final loss at matched builds, false-lead rate on fresh seeds.
8. **Evaluator integrity, winner's-curse control.** Harness-owned exam (exists); hide checker internals from builders [18]; plant canary cheats that must fail; re-evaluate an elite on fresh seeds before it holds a cell or parents [35][6]; promote on held-out seeds [30], as AlphaEvolve's kernel study held out half its input shapes [14]. Expect smaller dev-to-held-out shrinkage. Measure: dev gain minus held-out gain, exam-mismatch rate, canary recall, elite replication rate.
9. **Operator and model arms, verbalised alternatives.** Treat (card, LLM, temperature, operator) as bandit arms paid by rung-3 pass rate [16] (text calls the gain significant, caption "slight"), keep a cheap/strong mix [14]; request K weighted alternatives per call [25][40]. Expect more distinct ideas per token. Measure: non-duplicate rate at cosine 0.8 per batch [37], clusters per 100 sketches, per-arm hit rate with intervals.

## 7. Gaps

No LLM-evolution study of 20M-parameter recipes found; nearest are [16], [30], [31], [32]. Preprints [22][23][25][26][27][30] are unreviewed. Not checked: Gomes 2015 (novelty-search design), Ding 2024 (QD theory), EvoX/AdaEvolve.

## Sources

1. Lehman & Stanley 2011, novelty search: https://www.cs.swarthmore.edu/~meeden/cs81/f17/papers/lehman_ecj11.pdf
2. Mouret & Clune 2015, MAP-Elites: https://arxiv.org/abs/1504.04909
3. Pugh, Soros, Stanley 2016, quality diversity: https://www.frontiersin.org/articles/10.3389/frobt.2016.00040/full
4. Fontaine et al. 2020, CMA-ME: https://arxiv.org/abs/1912.02400
5. Fontaine & Nikolaidis 2023, CMA-MAE: https://arxiv.org/abs/2205.10752
6. Flageat & Cully 2024, Uncertain QD (abstract only): https://arxiv.org/abs/2302.00463
7. Hughes et al. 2024, open-endedness (DeepMind): https://arxiv.org/abs/2406.04268
8. Wang et al. 2019, POET: https://arxiv.org/abs/1901.01753
9. Zhang et al. 2023, OMNI: https://arxiv.org/abs/2306.01711
10. Lehman et al. 2022, ELM (OpenAI): https://arxiv.org/abs/2206.08896
11. Bradley et al. 2023, QDAIF: https://arxiv.org/abs/2310.13032
12. Samvelyan et al. 2024, Rainbow Teaming: https://arxiv.org/abs/2402.16822
13. Romera-Paredes et al. 2024, FunSearch, Nature: https://pmc.ncbi.nlm.nih.gov/articles/PMC10794145/
14. Novikov et al. 2025, AlphaEvolve (DeepMind): https://arxiv.org/abs/2506.13131
15. Georgiev, Gomez-Serrano, Tao, Wagner 2025, AlphaEvolve at scale: https://arxiv.org/abs/2511.02864
16. Lange, Imajuku, Cetin 2025, ShinkaEvolve (Sakana): https://arxiv.org/abs/2509.19349
17. OpenEvolve README (fetch summary): https://github.com/algorithmicsuperintelligence/openevolve
18. Zhang et al. 2025, Darwin Godel Machine (ICLR 2026): https://arxiv.org/abs/2505.22954
19. Lee et al. 2025, Mind Evolution (DeepMind): https://arxiv.org/abs/2501.09891
20. Agrawal et al. 2025, GEPA (ICLR 2026 oral): https://arxiv.org/abs/2507.19457
21. Lange et al. 2025, robust-kbench (Sakana): https://arxiv.org/abs/2509.14279
22. Gideoni, Risi, Gal 2026, simple baselines: https://arxiv.org/abs/2602.16805
23. Oved et al. 2026, Evolution or Illusion: https://arxiv.org/abs/2609.19799
24. Wang et al. 2026, EvoDiverse (ICML 2026): https://arxiv.org/abs/2606.10587
25. Yang et al. 2026, TurboEvolve: https://arxiv.org/abs/2604.18607
26. Tanveer 2026, LEVI: https://arxiv.org/abs/2605.09764
27. Cao et al. 2026, K-Search: https://arxiv.org/abs/2602.19128
28. Toledo et al. 2025, AIRA-dojo (Meta): https://arxiv.org/abs/2507.02554
29. Zhao et al. 2025, Automated LLM Speedrunning Benchmark (Meta): https://arxiv.org/abs/2506.22419
30. Jin et al. 2026, Arbor: https://arxiv.org/abs/2606.11926
31. Karpathy, autoresearch README (fetch summary): https://github.com/karpathy/autoresearch
32. SkyPilot, scaling autoresearch (vendor blog, fetch summary): https://skypilot.ai/blog/scaling-autoresearch/
33. Chen et al. 2023, Lion: https://arxiv.org/abs/2302.06675
34. So, Liang, Le 2019, Evolved Transformer: https://arxiv.org/abs/1901.11117
35. Real et al. 2019, regularized evolution: https://arxiv.org/abs/1802.01548
36. Narang et al. 2021, Transformer modifications: https://arxiv.org/abs/2102.11972
37. Si, Yang, Hashimoto 2024, novel research ideas: https://arxiv.org/abs/2409.04109
38. Si, Hashimoto, Yang 2025, ideation-execution gap: https://arxiv.org/abs/2506.20803
39. Jiang et al. 2025, Artificial Hivemind: https://arxiv.org/abs/2510.22954
40. Zhang et al. 2025, Verbalized Sampling: https://arxiv.org/abs/2510.01171
41. Lehman et al. 2018, digital evolution anecdotes: https://arxiv.org/abs/1803.03453
42. Guo et al. 2024, EvoPrompt (ICLR 2024): https://arxiv.org/abs/2309.08532
