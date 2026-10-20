# Selection under a scarce build budget: what is known

Written 2026-10-17. "Page" = I fetched the arXiv abstract this session. "Memory" = from my training knowledge, not re-checked. Treat memory rows as leads, not facts.

## Evidence table

| Idea | Evidence | Numbers | Source | Verified |
|---|---|---|---|---|
| Hyperband: many short runs, promote the best | Random configs get a small budget, survivors get more. Hedges over how many configs vs how long each. | "Over an order-of-magnitude speedup" vs Bayesian optimisation baselines (abstract). | https://arxiv.org/abs/1603.06560 | Page (abstract only) |
| Hyperband bracket rule | Halve with eta=3 or 4. Each bracket spends about equal budget but starts at a different breadth/depth mix. The most extreme bracket is plain random search at full budget. | eta=3 default; about log_eta(R)+1 brackets. | Li et al. JMLR 2018 | Memory |
| Successive halving (SH) | Fixed budget, n configs, keep top 1/eta each rung. Provable gains when early rank matches final rank. | About n*log(n) cost vs n*full for exhaustive. | Jamieson and Talwalkar 2016, https://arxiv.org/abs/1502.07943 | Memory |
| ASHA: async SH | No waiting at rungs; promote as soon as a config is in the top 1/eta of its rung so far. | Linear scaling with workers; tested at 500 workers. | https://arxiv.org/abs/1810.05934 | Page (abstract) |
| SH failure mode | If early loss does not predict final loss, SH kills late bloomers. Hyperband's wide brackets partly guard against this. Typical victims: LR-schedule, warmup and regularisation changes, which look worse early. | No single number; depends on the space. | Li et al. 2018 and follow-ups | Memory |
| Learning-curve extrapolation (LC-PFN) | A transformer trained on 10M synthetic curves predicts the final value from a partial curve. Used as an early-stop rule. | 2-6x speedups on 45 datasets; 20,000 real curves, 4 benchmarks; over 10,000x faster than MCMC. | https://arxiv.org/abs/2310.20447 | Page |
| Earlier curve extrapolation | Domhan 2015 (parametric curve ensembles) and Klein 2017 (Bayesian NN curve model). | About 2x speedups (low confidence). | IJCAI 2015; ICLR 2017 | Memory |
| MAP-Elites | Keep the best solution per cell of a chosen behaviour grid. Gives a map of good, diverse solutions, and often a better top solution than standard search. | Three domains (modular nets, soft robots). | https://arxiv.org/abs/1504.04909 | Page |
| Novelty search with local competition | Compare each candidate only to neighbours in behaviour space, so odd designs survive. | None recalled. | Lehman and Stanley 2011 | Memory |
| FunSearch islands | Several independent program populations. Periodically the worst half of islands is reset from the best program of a surviving island. Within an island, programs are clustered by score signature; sampling favours high score and short programs. | About 10 islands (low confidence). | Romera-Paredes et al., Nature 2024, https://www.nature.com/articles/s41586-023-06924-6 | Memory (page blocked by login redirect) |
| AlphaEvolve | Evolutionary coding agent with an evaluator, a program database inspired by MAP-Elites plus islands, and an LLM ensemble. Uses an evaluation cascade: cheap tests first, expensive ones only if the cheap ones pass. | Abstract: gains in LLM training and scheduling; 48-multiplication 4x4 complex matmul. | https://arxiv.org/abs/2506.13131 | Page (abstract); database and cascade from memory |
| AI Scientist v2 | Progressive agentic tree search with an experiment-manager agent. Node choice by metric plus LLM judgement; buggy nodes get debug retries (cap). | 1 of 3 workshop papers above the human acceptance average. | https://arxiv.org/abs/2504.08066 | Page (abstract); selection details not seen |
| LLM-as-optimizer / EvoPrompt | OPRO keeps the top-scoring solutions in the prompt; EvoPrompt picks parents by roulette or tournament. Score ranking dominates; diversity comes from sampling. | OPRO keeps about 20 best (memory). | Yang 2023 (2309.03409); Guo 2023 (2309.08532) | Memory |
| Zero-cost NAS proxies | One-minibatch scores: synflow, grad_norm, jacob_cov, snip, NASWOT. | Best proxy Spearman 0.82 on NAS-Bench-201 vs 0.61 for reduced training (EcoNAS), at about 1000x less compute. | https://arxiv.org/abs/2101.08134 | Page |
| Zero-cost proxies vs trivial baselines | Follow-ups find many proxies add little beyond parameter count / FLOPs and are weak outside cell-based CNN spaces. Combining 13 proxies in a surrogate improved prediction up to 42%. | Up to 42%. The param-count finding is from memory. | https://arxiv.org/abs/2210.03230 | Page for 42%; rest memory |
| Short training for LMs | Modded-nanogpt practice: record claims are tested on full short runs (minutes on 8 GPUs, several seeds), not a few hundred steps. Small-tweak gaps are often below seed noise at short horizons. | No clean number found. | github.com/KellerJordan/modded-nanogpt | Memory |
| How many to build vs prune | I found no paper reporting an optimal build fraction for LLM-generated ideas. Closest: AlphaEvolve cascade and Hyperband (keep 1/3 or 1/4 per rung). | none | - | Not found |

## What this means for the critique

1. The critique is right in shape. Successive halving is the standard answer: spend little on many, promote by measured score. Stacked quotas that override score are not part of Hyperband, ASHA, FunSearch or AlphaEvolve ranking inside a cell or island.
2. But the sources do not say "rank by score only." Every quality-diversity system keeps diversity, and it is structural (islands, cells), not a share of the final slots. Its job is to protect late bloomers.
3. The key risk is whether 45-step and 240-step results predict the long run. I found no number for this loop. The loop's own history can supply it: Spearman between 240-step gain and long-run gain on past builds. Measure this first.
4. Seed noise matters. If the 240-step difference between two ideas is below the seed-to-seed spread, "top twenty by learning" is partly random. Rank with a margin, not a point value.
5. "Rank by actual measurement" needs a measurement for unbuilt ideas. Builder calls cost tokens, so the pool must be cut by cheap proxy before building. Zero-cost proxy evidence is from CNN spaces and is weak here. Safe cheap proxies for code edits: static check pass, parameter-count change, step time, a few-step loss.

## Ranked: what to adopt

1. Measure predictiveness now (zero cost). From past rounds compute the rank correlation of 45-step vs 240-step vs long-run gain. This decides how aggressive halving can be.
2. Make the ladder a real successive-halving ladder with eta about 3-4. Many ideas at the cheapest rung, promote the top 1/3 on measured gain with a noise margin. Reuse the existing rungs.
3. Order checks cheapest first and stop on first fail (AlphaEvolve cascade). Run the cheap GPU gates (param count, step time, 45 steps) before spending more builder tokens wherever possible.
4. Rank by score for most slots. Cap quotas to a small reserved fraction (for example 2 of 10-19 slots). Keep one lane only: the random long-shot lane, which doubles as the late-bloomer hedge. Drop or merge the direction, per-part and novelty quotas.
5. Replace per-part round robin with a within-part cap (island-like): at most k picks per part, rest filled by score.
6. Add a late-bloomer audit as in Hyperband brackets: promote a few ideas that narrowly fail the 45-step gate and check whether any win at 240. Their hit rate tells you if the gate is too strict.
7. Later, optional: learning-curve extrapolation (LC-PFN style) from the 45-step curve to decide 240-step promotion. Needs enough past curves; 2-6x savings were reported on other tasks.
8. Do not adopt zero-cost NAS proxies as a ranker.

## Gaps

No primary number for build-vs-prune ratio in LLM research agents. FunSearch island count and Hyperband details are from memory. Re-fetch the full PDFs before citing numbers externally.
