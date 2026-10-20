# 05. Evidence standards for "our system beats the plain model"

Date: 2026-10-17. Plain English. "On page" means I fetched the arXiv or ACL abstract page this session. "Memory" means I did not open the page, so treat the number as unverified.

## Short answer

The field has no hard rule for a minimum number of seeds. It has a clear rule for what a claim must show. The gain must be large next to the noise. The baseline must be strong and get an equal budget. The claim must hold on more than one task. HTSA meets each of these only in part. The cheapest fixes cost tokens and writing, not GPU time.

## Table: claim -> evidence -> numbers -> source -> verified?

| Claim | Evidence | Numbers | Source | Verified |
|---|---|---|---|---|
| Single runs mislead in deep RL | Henderson et al. 2018: variance inside a method, non-determinism, and missing significance tests make "better than SOTA" hard to read. Proposes reporting guidelines. | Abstract gives no seed count. Body (memory): 5 seeds; two groups of 5 gave different conclusions. | https://arxiv.org/abs/1709.06560 | Abstract on page. Seed detail from memory. |
| Report intervals and robust aggregates, not point scores | Agarwal et al. 2021: the field moved to few runs per task. Recommends interval estimates, performance profiles, interquartile mean (IQM), and the `rliable` library. | Abstract gives no run count. Body (memory): bootstrap CIs; a handful of runs per task can give usable intervals if reported honestly. | https://arxiv.org/abs/2108.13264 | Abstract on page. Run counts from memory. |
| Variance has several sources, not only the seed | Bouthillier et al. 2021: data sampling, initialisation and hyperparameter choice all matter. Varying more sources in the estimator brings it closer to the ideal one. | 51x lower compute for a close approximation of the ideal estimator. Tested on 5 tasks. | https://arxiv.org/abs/2103.03098 | On page. |
| Pick the right significance test | Dror et al. 2018: in a 2017 survey of ACL/TACL papers, testing was "often ignored or misused". Gives a protocol for choosing a test. | No share in abstract (memory: roughly a third of papers reported any test). | https://aclanthology.org/P18-1128/ | Abstract on page. Share from memory. |
| Strong simple baselines erase "progress" (recommenders) | Dacrema et al. 2019: of 18 neural top-n methods, only 7 could be reproduced. 6 of those 7 were beaten by simple heuristics. The 7th did not consistently beat a tuned linear method. | 18 / 7 / 6 | https://arxiv.org/abs/1907.06902 | On page. |
| Same pattern in metric learning | Musgrave et al. 2020: papers claim big gains, "often more than doubling" decade-old methods. Under a fair protocol, gains are "marginal at best". | No figure in abstract. | https://arxiv.org/abs/2003.08505 | On page. |
| Conclusions depend on which benchmarks you pick | Dehghani et al. 2021 "benchmark lottery": changing the task set can change which method ranks first. | No single number. | https://arxiv.org/abs/2107.07002 | On page. |
| Blinded human study is the standard for "novel ideas" | Si, Yang, Hashimoto 2024: over 100 NLP researchers, blind review. LLM ideas rated more novel (p < 0.05), slightly weaker on feasibility. Authors warn LLM-as-judge is unreliable and ideas lack diversity. | p < 0.05 for novelty. Exact counts not on the abstract page (memory: 79 reviewers, 298 reviews, 49 ideas per arm). | https://arxiv.org/abs/2409.04109 | Abstract on page. Counts from memory. |
| Many tasks and a medal scale for agents | MLE-bench: 75 Kaggle competitions. Best setup (o1-preview with AIDE) reaches at least bronze in 16.9%. | 75 tasks, 16.9% | https://arxiv.org/abs/2410.07095 | On page. |
| Peer review as an external check | AI Scientist v2: 3 autonomous papers sent to an ICLR workshop. One scored above the average human acceptance threshold. | 1 of 3. Workshop, not main track. Self-reported. | https://arxiv.org/abs/2504.08066 | On page. The "low bar, one paper" criticism is my reading. |
| Verified constructions are the strongest evidence | AlphaEvolve: 4x4 complex matrix multiplication with 48 scalar multiplications, first improvement over Strassen in this setting in 56 years. Plus deployed gains at Google. Anyone can check it. | 48 multiplications | https://arxiv.org/abs/2506.13131 | On page. |
| Same for FunSearch | New cap set constructions and better bin-packing heuristics, scored by code that checks them. Code released. | Cap set of size 512 in n=8 (memory) | https://www.nature.com/articles/s41586-023-06924-6 | Memory only. |
| Wet-lab validation for co-scientist | Google AI co-scientist: proposed drug repurposing and liver fibrosis targets tested in the lab, plus expert preference and an internal Elo tournament. | Not recalled with confidence. | https://arxiv.org/abs/2502.18864 | Memory only. |
| Pretraining papers with one seed | Common practice. Justified with several model sizes, scaling-law fits, held-out loss, and a gain larger than the seed gap measured once on a small model. | Seed spread at small scale is usually a fraction of a percent of loss (memory, not checked). | No single source | Memory only. |

## Reading the table

1. Nobody gives a magic seed count. Agarwal and Bouthillier both say: report uncertainty, do not hide behind a point estimate. If runs are unaffordable, say so and show the gain next to known noise.
2. A single-run claim is credible when the gain is many times the usual seed spread. A 7% perplexity drop at 21M parameters is probably well above typical seed spread, but that is a belief from memory, not a result. It can be checked without new training. Look for any log where the same architecture was trained twice, or quote a published seed spread for similar models.
3. Systems that were accepted had one of three things: an objective check (FunSearch, AlphaEvolve), a blind human panel (Si et al.), or many tasks (MLE-bench). Systems that drew criticism had a judge from the same family as the system, one task, or one lucky sample (AI Scientist: 1 of 3).
4. The "are we really making progress" pattern is the main threat to HTSA. In Dacrema and Musgrave, the sceptic won by tuning the simple baseline as hard as the new method. The ARC tie against best-of-n at equal tokens shows that baseline is strong.
5. Baselines reviewers ask for: equal tokens or equal dollars, best-of-n, self-consistency or majority vote, the best hand-written single prompt, and a "same compute, plain loop" control. This list is my synthesis, not one source. For NoveltyBench, the paper's best baseline is already the right comparator, and HTSA is measured against it.
6. Many benchmarks help only if chosen before seeing results. Otherwise the benchmark lottery applies. Three results picked after the fact count as one result plus cherry-picking risk.

## Ranked cheapest steps for a jury

| Rank | Step | Cost | Why it helps |
|---|---|---|---|
| 1 | Write the honest claim now. Say what is shown, what is one result deep, and why a second seed was not run. Quote a published seed spread for similar-size models next to the 7%. | None (writing) | Reviewers punish overclaiming more than a small sample. Matches the Henderson and Agarwal advice to state uncertainty. |
| 2 | Report the full per-prompt distribution on NoveltyBench. Give a histogram of distinct counts, a paired bootstrap CI on the gap vs the paper's best baseline, and win/tie/loss over the 100 prompts. | None to a few thousand tokens, from existing logs | Turns 9.63 vs 8.28 into an interval. Agarwal-style reporting. |
| 3 | Rescore utility with an independent judge: a second model family, or a blinded human panel of 3 to 5 people on a 20-prompt sample in random order. Report agreement with Opus. | Low tokens; a few hours of human time | The utility gap (5.90 vs 6.16) is judged by Opus, not the official judge. This is the largest single hole. Si et al. used blind humans. |
| 4 | Pre-register the next prediction. Commit a file with hypothesis, metric, baseline, budget and the failure rule before the run. Timestamp it in git. | None | Removes the "chosen after the fact" worry. Cheap and visible. |
| 5 | Add a second open-ended problem with a code scorer, such as a bin-packing or scheduling heuristic. Compare HTSA with best-of-n at equal tokens, 5 to 10 repeats. | Tokens only, likely tens of dollars. No GPU. | Gives an objective, checkable result in the FunSearch style, in a second domain. |
| 6 | Harden the baseline. Tune best-of-n and the strongest single prompt with the same effort as HTSA and the same token budget. State the effort each got. | Tokens | Answers the Dacrema and Musgrave objection head on. |
| 7 | Release run logs, prompts, seeds and scoring scripts so anyone can re-grade. | None | Enables independent reproduction, the strongest form of evidence. |
| 8 | Present the diversity-utility trade-off as a frontier: diversity up, utility slightly down. | None | Stops a reviewer from finding it first. |
| 9 | Put the ARC tie in the main text, not an appendix. | None | Counters cherry-picking suspicion. |

## What the current evidence does and does not support

Supports:
- HTSA gives far more varied answers than plain sampling on NoveltyBench (9.63 vs 3.18 of 10), and more than the paper's best baseline (8.28). One model, 100 prompts.
- On one LM-architecture task, the loop found a design with 7% lower perplexity than the scaled-down skeleton. One size, one seed.
- On ARC, it ties best-of-n at equal tokens. That is a fair control, not a win.

Does not support:
- "HTSA beats a strong plain baseline in general." Only the diversity result clearly beats a strong baseline, and it is on a metric that rewards variety.
- Better answer quality. Utility is slightly below the best baseline and graded by Opus, not the official judge.
- A robust architecture gain. One seed, one size, no scaling check. The 7% may well exceed seed noise, but that is not shown.
- Generality. Three tasks, one a tie, none chosen in advance.

Honest framing for a jury: one clear win on diversity, one single-seed positive on architecture, one tie on ARC, and a pre-registered next test.

## Gaps in this note

- I read abstract pages only, not full papers. Seed counts, shares and the Si et al. reviewer counts are from memory and marked so.
- The FunSearch, co-scientist and pretraining-practice rows are memory only.
- No source I found gives a minimum seed number. The guidance is to report uncertainty, not to reach a fixed count.
