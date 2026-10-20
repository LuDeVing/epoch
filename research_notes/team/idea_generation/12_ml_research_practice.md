# 12. How new ideas actually arise in deep-learning research practice, 2023-2026

Prepared 2026-10-13 for the HTSA nano loop. Grades: **A** independent replication or large controlled study; **B** one primary source with ablations or logs; **C** blog, tweet, vendor or secondary report; **D** my own count or inference. [n] = Sources. The search quota ran out mid-task; every cited item was still fetched and read directly (full text or relevant sections; abstract only for [24][28]-[32][34][37][38][48][55][58]-[61][63][64][69]). Briefs 04 and 09 cover evolutionary search and agent loops.

## Bottom line

1. **Accepted ideas are mostly ports, repairs and recombinations.** Across records 13-91 of the 92-record NanoGPT speedrun log the median record saves 1.1% wall time (mean 1.9%, max 10.4%; 41% under 1%); at least 11 are explicit ports of named papers or models [1][D]. The largest late architecture wins: bigram hash 5.3% (a port, soon after DeepSeek's Engram preprint), backout bundle 3.6% (community idea plus tuning), MUDD 3.1% and 3.7% (ports) [1][8][47][D]. (B/D)
2. **Six origins recur** (Table 1): bottlenecks (KV bytes per token to MLA, DSA); measured pathologies (logit divergence to QK-norm, 3000x residual gain to mHC); port-and-adapt; imported theory; ablation matrices; tight-loop tinkering. (B)
3. **Optimizer wins are the least portable.** Muon needed weight decay and update-RMS matching [25] and QK-Clip at 9B active parameters [26]; against tuned AdamW its edge falls from about 1.3x (0.1B) to 1.1x (1.2B), and most claimed 2x speed-ups were weak baselines [27]. (A/B)
4. **Small-scale parity proves little.** MiniMax's small hybrid-attention models matched full attention, then showed multi-hop deficits at scale [52]; perplexity barely moves with local:global ratio or window [51], long-context quality does [49]. (B/C)
5. **2026 agents tune, stack and port; they do not originate.** Karpathy's loop took time-to-GPT-2 from 2.02 to 1.65 h [19]; Prime Intellect's agents reached 2930 vs 2990 steps, "need upstream human records", and with novelty required "they cannot improve the baseline" [21]; five AI-credited speedrun records give 0.5-1.3% each [1][D]. (B/C)
6. **Lion came from evolutionary search over symbolic programs, not an LLM** [33]. LLM search is bounded by its evaluator (AlphaEvolve [65]) and exploits leaky verifiers [66]. (B)

## 1. Documented origins (Table 1, all rows grade B)

| Advance | How it was found | Src |
|---|---|---|
| Muon | Bernstein and Newhouse: Shampoo without accumulation = spectral steepest descent; Newton-Schulz worked out with Large. Jordan tried it in the CIFAR-10 speedrun: a quintic iteration with non-convergent coefficients, choices "obtained experimentally", coefficients from "an ad-hoc gradient based approach". NanoGPT record -21%; -40% reproduced on two RTX 4090s | [1][3][5][68] |
| Muon at scale | Moonlight: add weight decay, match update RMS to AdamW. K2: logits above 1000 at 9B active; QK-norm cannot apply to MLA, so QK-Clip. V4.1: head-wise Muon "outperforms vanilla Muon"; speedrun #80 used per-head-pair groups ("heads often specialize") | [25][26][35][18] |
| Imported theory | Polar Express (#38): minimax polynomial iteration from numerical analysis; SOAP: Shampoo = Adafactor in an eigenbasis; Schedule-Free: iterate-averaging theory, AlgoPerf self-tuning winner | [28][30][31][32] |
| QK-norm | 8B ViT diverged, attention near one-hot; LayerNorm on Q,K; a high-LR proxy reproduces it small | [36][37] |
| Gating | 2023: outliers trace to no-op heads; 2025: 30 variants, 15B MoE and 1.7B dense, 3.5T tokens; first-token attention 46.7% to 4.8%, PPL -0.2 | [38][39] |
| MLA, DSA | KV cache is the bottleneck: MLA beats MHA at 16B and 250B with 4-14% of the cache; DSA retrofits a trained model (freeze it, KL-train the indexer on 2.1B tokens, then 943.7B sparse tokens) | [41][44] |
| Scaling-law design | K2: a sparsity law (at loss 1.5, sparsity 48 needs 1.69x less compute than 8); doubling heads gained only 0.5-1.2% for +83% inference FLOPs at 128k, so 64 heads. Engram: a U-shaped MoE-vs-memory allocation law, then 27B. Caution: last-layer cost, warmup and optimizer tuning explain Kaplan vs Chinchilla | [26][47][69] |
| MoE balancing | Aux loss adds "interference gradients"; bias-only balancing validated at 1B/3B, ablated in V3 at 15.7B and 228.7B; a batch-wise aux loss ties it (2.253 vs 2.253). Qwen: micro-batch balancing blocks specialisation | [43][42][48] |
| mHC | Hyper-connection composite gain measured up to ~3000; doubly-stochastic constraint gives ~1.6 | [46] |
| Value residual | Over-smoothing literature plus DenseFormer's learned weights (deeper layers lean on initial embeddings); equal loss with 16% fewer parameters and 20% less data at 82M-468M | [40] |
| Smear, backout | Trained weights showed previous-token heads; per-layer learned coefficients (0.54 to -0.29) reduced to one lambda at layer 8 | [12][13] |

## 2. The speedrun log as a natural experiment

- **Scale.** 92 records in 27 months, 45 to 0.67 min [1]; optimizer track: 46 results, 3600 to 2690 steps, at least 7 techniques submitted by their authors [2].
- **Mix (my classification of one-line descriptions, plus or minus 3).** Of 91 records: 34 architecture, 34 systems, 14 optimizer or schedule, 7 bundles, 2 data or eval; over records 13-91 (4.6x) architecture gave about 48% of log-speedup, systems 27%, optimizer 14% [D]. Explicit ports: #14, 20, 26, 31, 38, 41, 62, 73, 81, 82, 85; eight records (#14-17, 55, 63, 65, 70) refine value embeddings, ported from the value-residual paper [40][1].
- **Value changes with the stack.** Untied head (#8), re-tied (#51), untied at two thirds of training (#53); partitioned hyper-connections (#73) replaced by a simpler variant (#77) [1][9].
- **Ports are adapted, not copied.** Hyper-connections: "not only was the overhead huge, but they didn't help convergence at all"; the adaptation used two lanes, only H_post trainable, from block 7 [9]. MUDD: last two layers, 2 of 4 channels, zero-init [11]. XSA: zero-initialised, "a strict superset of master at step 0"; layer 8 dropped as its "diagnostic" gate was smallest; commits co-authored with Claude [10].
- **Effect sizes are fragile.** Smear is "closer to 5 steps" than its headline [12]; Aster's -1.6 s title measured -0.4 s [16]; optimizer-track records #11, #16, #34 are not pairwise significant (p 0.69, 0.34, 0.17) [2]; AI submissions add "barnacles" [2].
- **AI-credited records** (#32, 60, 69, 72, 87) are kernels, precision, a skip-gate re-parameterisation and schedules [1][17][16][15]; Station's paper reports a "silent no-op": a patch edited a value the compiled code never read [15].

## 3. Small to large: what transferred (Table 2)

| Idea | Small scale | Larger scale | Gr |
|---|---|---|---|
| Muon | 1.35x record speed-up at 124M | Repairs needed [25][26]; about 1.1x at 1.2B vs tuned AdamW, winner shifts to SOAP or Kron at 8x Chinchilla [27]; Moonlight reports about 2x, and [27] finds such claims reflect weak baselines; still adopted by K2, V4.x, MiMo mid-training [26][35][50] | A/B |
| Speedrun stack | 33% at 124M, tuned | 25% at 350M with zero tuning [6]; README concedes structure-imposing tricks such as softcap may not scale [1] | B |
| Autoresearch edits | gains found at depth 12 | "easily translated" to depth 24 [19]; a filtering gain on H200 reversed on B200 [22] | B/C |
| Sophia, Lion | Claimed gains over Adam | No significant Sophia gain under 0.5B in [27]'s setting, linked to a non-randomised loader in the original codebase; Lion's gap to AdamW widens with size [27]; Lion, Sophia, Schedule-Free, AdEMAMix gave no real speedrun gain [4] | A/B |
| Hybrid attention | Parity in small tests | Multi-hop deficits, M2 reverted to full attention [52]; MiMo's 5:1, window 128 works at 32B only with a learned sink, and 128 vs 512 differ only after long-context extension [49] | B/C |
| Scale-dependent gains (reverse case) | Small-scale ablations explain under 10x of a claimed 22,000x efficiency gain [55] | Primer's savings grow with compute [62]; the LSTM-to-Transformer gap widens with scale [55] | B |

## 4. NAS and automated discovery

- **NAS critiques.** Random search with early stopping matched ENAS [58]; leading NAS performed like a random policy and weight sharing corrupted rankings [59]; DARTS minimised validation loss yet gave degenerate solutions [60]; most Transformer modifications "do not meaningfully improve performance", the beneficial ones coming from the authors' codebase or minor [61]. AutoML-Zero rediscovered backprop nets, bilinear interactions, normalised gradients and weight averaging on toy tasks; there evolution "vastly outperforms" random search [57].
- **Successes are constrained.** Primer's program search found squared ReLU plus depthwise convolution, 4.2x less compute at 500M [62]; squared ReLU is the speedrun's ReLU^2 (#5) [1][D]. Puzzle (blockwise distillation, hardware cost) gave 2.17x throughput at 98.4% accuracy [63], and PostNAS starts from a trained model [64].
- **Lion** [33]: random search over 2M programs never approached AdamW; success needed an AdamW warm-start, 20-minute proxies, funnel selection through 10x and 100x tasks (search fitness rose while held-out fell: "meta-overfitting") and manual simplification.
- **AlphaEvolve** [65][66]: evolution, context, meta-prompts, full-file evolution and strong LLMs each mattered; the tiling heuristic was fit on half the kernel shapes and checked on the rest (23% kernel, 1% training time); in its 67-problem math study it exploited leaky verifiers. ShinkaEvolve [67]: an MoE balancing loss found at 556M kept a small edge at 2.7B.
- **Agent loops.** autoresearch: 5-minute budget, one editable file, "simplicity criterion" [20]; round 2, told to read modded-nanogpt, made backout and smear help where manual tries had regressed [19]. (auto)^2: the largest lever was doubling data shards; gains "not additive" [22]. 2025 models recovered at most 20% of record speed-ups unaided, 40-46% with pseudocode [23]; agents beat humans 4x at 2 h, humans win 2x at 32 h [24].

## 5. What practitioners say

Jordan: "the most common culprit is bad baselines" [3]. Dial: "first have 20 bad ideas", "Work backwards from the data", "Not everything will generalize" [7], and "In an execution driven field, negative results are close to meaningless" [8]. Hugging Face: ablations and debugging cost 161k GPU hours, over half the 276k main run [53]. MiniMax: "the real bottleneck is the limitations of evaluation" [52]. DeepSeek starts from hardware limits [45], and V4.1 from re-describing V4 as an SWA backbone plus compressed global context [35].

## 6. What would transfer to an LLM-driven idea loop

Rungs 3, 4, 5 are the 45-step check, the 240-step comparison and the overnight verdict (check.py, verdict.py). Effects are hypotheses anchored in the cited analogs.

1. **Diagnostic panel as the idea's target (diagnose.py).** It logs position, token-frequency, gradient, RMS and entropy; add loss on recall tokens (bigram already seen in context), max attention logit, first-token attention mass, update-norm and row-norm spread, learned scalars. Each sketch names the cell it moves and by how much. Basis: recall tokens explained 82% of the attention gap, hybrids closed 97% [56]; sink mass 46.7 to 4.8% [39]; gain 3000 [46]; norm spread led to NorMuon [29]. Expect higher sketch-to-win conversion for targeted ideas. Measure: conversion targeted vs untargeted; predicted vs observed cell movement at rungs 3-4.
2. **Identity-at-init insertion with gate read-out (builder prompt).** New paths are x + tanh(a)f(x), a = 0; log |a| per layer; drop low layers, hard-wire stable ones. Basis: [10][11][12][13]. Expect fewer rung-3 regressions and free per-layer attribution. Measure: rung-3 pass rate with vs without wrapper; rank correlation of |a| with leave-one-layer-out loss change.
3. **Lineage table with adaptation moves (research.py, ideate.py).** Rows: component, regime it helped, descendants and reversals, moves (zero-init, last-k layers, fewer channels, sharing); each ideation context gets three rows and must return an adapted variant. Basis: round 2, pointed at the modded-nanogpt repo "for inspiration", gave a further -8% [19]; Engram to bigram hash within weeks [8]; novelty-forced agents gained nothing [21]. Expect more accepted ideas per sketch than free ways-in. Measure: wins per sketch for lineage-seeded vs free vs novelty-forced ways-in.
4. **Tuned-baseline duel (before verdicts).** For optimizer, schedule or init ideas give baseline and candidate equal tuning (weight decay first, the most sensitive [2][34], then LR, betas, cooldown), tuned on a halved run, then restore length and retune LR and WD only. Basis: 2x claims fell to at most 1.4x [27]; tuning Muon alone moved 3600 to 3250 steps, as much as NorMuon [2]; nuisance parameters [54]. Expect optimizer-idea gains to shrink by a third or more (D). Measure: gain vs original vs retuned baseline; share surviving.
5. **Exchange rate, step-matched control, paired sequential seeds (verdict.py).** Fit the baseline's loss slope at budget end and score candidates in equivalent steps; test a claimed saving by running both arms at N-k steps; share data order across arms, stop at n = 2 if both seeds trail the baseline, else escalate to 5-10; a "stackable" tier (gain 0.002+, p<0.05, same sign on all rungs) feeds composition only. Basis: 0.0045 loss per 100 steps [2]; 164 ms per millinat [14]; paired-head Muon passes at -10 steps where the baseline fails [18]. At that slope 0.005 is about 3-4% of steps against a 1.1% median record, so real small wins will be rejected (D). Measure: slope on nano, A/A false-positive rate, power, GPU-hours per win.
6. **Compute-multiplier ladder (check.py, rung 4b).** For rung-4 survivors measure k = baseline tokens needed to match the candidate / candidate tokens at 0.25x and 1x tokens (shared baseline curve) plus one width up and down for the top 3; promote when k is at least 1 everywhere and its excess does not halve. Basis: same estimator [27]; 25% vs 33% transfer [6]; scale-dependent gains [55][62]; K2's sparsity and head-count scaling studies [26]; Engram's allocation law [47]. Expect fewer scale-fragile winners. Measure: sign and decay of k; recall on Muon-like controls.
7. **Leave-one-out ledger (compose.py).** After each composition and promotion, remove every component (and suspect pairs), price it in loss, delete what sits within noise, repeat every K promotions. Basis: ANVIL2 priced each mechanism by removal [14]; record #46 of the optimizer track names 10 active and 9 earlier, now unused techniques [2][D]; agents rarely prune, and pruning gained about 20 steps [21]; non-additive gains [22]. Expect a simpler recipe at equal loss. Measure: components within noise; joint minus summed marginal gain.
8. **Intervention checks and control sets (check.py, rung 2b).** Each build logs the effective value of every knob it claims to change; a neutralised patch must reproduce the baseline; A/A runs fix sigma; 5-8 known winners (QK-norm, ReLU^2, zero-init projections, untied head, value embeddings) and known losers calibrate power. Basis: silent no-op [15]; -1.6 s vs -0.4 s [16]; seven identical runs spread CORE by 0.0165 and the default shard order is "among the worse" [19]; verifier exploitation [66]. Expect fewer invalid experiments and calibrated thresholds. Measure: no-op rate; A/A false positives at most 1%; recall on controls.
9. **Bounded refinement of near-misses (deepen.py, loop.py).** For the top 3-5 near-misses run 20-60 LLM edits: archive parents, diff-size cap, novelty rejection, fitness on seeds A and selection on seeds B, funnel rung 3 to 4 to 5; stop when fitness rises but held-out falls; finish by deleting until worse; add a random-hyperparameter arm at equal evaluations. Basis: [65][67][33][58]. Expect 0.5-1.5% wins, the AI-record range [1], not new mechanisms. Measure: wins per 100 evaluations vs the random arm; search-minus-held-out gap.
10. **Metric-validity tags (verdict.py).** Tag ideas whose benefit lies outside validation loss at this length (windows, long context, routing balance, inference cost) as metric-blind; require a secondary probe (loss beyond the window, copy probe) and compare only at schedule end. Basis: [51][49][52]; curves cross during decay [27]; "early loss curve is deceptive" on skip-gate init [17]; step-1000 loss "does not strongly correlate" with final [2]. Expect fewer false rejections and promotions. Measure: probe vs loss disagreement; rank change when judged at end only.

## 7. Gaps

Not read: Physics of Language Models 4.1 (page empty), Intology Locus, Hiverge internals. [50] is a local copy. The record classification and 1.1% statistics are mine, from README tables; exchange rates come from 124M FineWeb, so remeasure on nano.

## Sources

1. modded-nanogpt README: https://github.com/KellerJordan/modded-nanogpt
2. Optimizer-track README: https://github.com/KellerJordan/modded-nanogpt/blob/master/records/track_3_optimization/README.md
3. Jordan, Muon post: https://kellerjordan.github.io/posts/muon/
4. Jordan, optimizer comparison: https://github.com/KellerJordan/modded-nanogpt/blob/master/records/track_1_short/2024-10-29_Optimizers/README.md
5. Bernstein, Deriving Muon: https://jeremybernste.in/writing/deriving-muon
6. Bulk transfer to medium track: https://github.com/KellerJordan/modded-nanogpt/blob/master/records/track_2_medium/2025-12-31_BulkSmallTrackTransfer/README.md
7. Dial, speedrun write-up: https://www.lesswrong.com/posts/j3gp8tebQiFJqzBgg/how-the-nanogpt-speedrun-wr-dropped-by-20-in-3-months
8. PR 201, bigram hash: https://github.com/KellerJordan/modded-nanogpt/pull/201
9. PR 230, hyper-connections: https://github.com/KellerJordan/modded-nanogpt/pull/230
10. PR 264, XSA: https://github.com/KellerJordan/modded-nanogpt/pull/264
11. MUDD record: https://github.com/KellerJordan/modded-nanogpt/blob/master/records/track_1_short/2026-04-22_MuddFormer/README.md
12. Smear record: https://github.com/KellerJordan/modded-nanogpt/blob/master/records/track_1_short/2025-09-18_Smear/README.md
13. Backout record: https://github.com/KellerJordan/modded-nanogpt/blob/master/records/track_1_short/2025-10-04_Backout/README.md
14. ANVIL2 record: https://github.com/KellerJordan/modded-nanogpt/blob/master/records/track_1_short/2026-08-30_ANVIL2/README.md
15. Station record: https://github.com/KellerJordan/modded-nanogpt/blob/master/records/track_1_short/2026-02-10_ShortWindow/README.md
16. PR 217, Aster: https://github.com/KellerJordan/modded-nanogpt/pull/217
17. PR 125, Hiverge: https://github.com/KellerJordan/modded-nanogpt/pull/125
18. Paired-head Muon record: https://github.com/KellerJordan/modded-nanogpt/blob/master/records/track_1_short/2026-04-08_PairedHeadMuon/README.md
19. nanochat leaderboard: https://github.com/karpathy/nanochat/blob/master/dev/LEADERBOARD.md
20. autoresearch program.md: https://github.com/karpathy/autoresearch/blob/master/program.md
21. Prime Intellect, auto-nanogpt (2026-05-14): https://www.primeintellect.ai/auto-nanogpt
22. (auto)^2-research (2026-09-14, vendor): https://rekursiv.ai/blog/autoautoresearch/
23. Zhao 2025, Automated LLM Speedrunning Benchmark: https://arxiv.org/abs/2506.22419
24. Wijk 2024, RE-Bench: https://arxiv.org/abs/2411.15114
25. Liu 2025, Moonlight: https://arxiv.org/abs/2502.16982
26. Kimi K2: https://arxiv.org/abs/2507.20534
27. Wen 2025, Fantastic Pretraining Optimizers: https://arxiv.org/abs/2509.02046
28. Amsel 2025, Polar Express: https://arxiv.org/abs/2505.16932
29. Li 2025, NorMuon: https://arxiv.org/abs/2510.05491
30. Vyas 2024, SOAP: https://arxiv.org/abs/2409.11321
31. Defazio 2024, Schedule-Free: https://arxiv.org/abs/2405.15682
32. Kasimbeg 2025, AlgoPerf: https://arxiv.org/abs/2502.15015
33. Chen 2023, Lion: https://arxiv.org/abs/2302.06675
34. Wang, Aitchison 2024, AdamW timescale: https://arxiv.org/abs/2405.13698
35. DeepSeek-V4.1-Flash (local copy in research_notes/architectures): https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash
36. Dehghani 2023, ViT-22B: https://arxiv.org/abs/2302.05442
37. Wortsman 2023, small-scale proxies: https://arxiv.org/abs/2309.14322
38. Bondarenko 2023, Quantizable Transformers: https://arxiv.org/abs/2306.12929
39. Qiu 2025, Gated Attention: https://arxiv.org/abs/2505.06708
40. Zhou 2024, Value Residual Learning: https://arxiv.org/abs/2410.17897
41. DeepSeek-V2: https://arxiv.org/abs/2405.04434
42. DeepSeek-V3: https://arxiv.org/abs/2412.19437
43. Wang 2024, loss-free balancing: https://arxiv.org/abs/2408.15664
44. DeepSeek-V3.2: https://arxiv.org/abs/2512.02556
45. Zhao, DeepSeek hardware co-design: https://arxiv.org/abs/2505.09343
46. Xie 2025, mHC: https://arxiv.org/abs/2512.24880
47. Cheng 2026, Engram: https://arxiv.org/abs/2601.07372
48. Qiu 2025, Demons in the Detail: https://arxiv.org/abs/2501.11873
49. MiMo-V2-Flash: https://arxiv.org/abs/2601.02780
50. MiMo-V2.6 (local copy only): research_notes/architectures/MiMo_V2_6_technical_report.pdf
51. Gemma 3: https://arxiv.org/abs/2503.19786
52. MiniMax, why M2 is full attention: https://huggingface.co/blog/MiniMax-AI/why-did-m2-end-up-as-a-full-attention-model
53. Hugging Face Smol Training Playbook: https://huggingface.co/spaces/HuggingFaceTB/smol-training-playbook
54. Google Tuning Playbook: https://github.com/google-research/tuning_playbook
55. Gundlach 2025, Origin of Algorithmic Progress: https://arxiv.org/abs/2511.21622
56. Arora 2023, Zoology: https://arxiv.org/abs/2312.04927
57. Real 2020, AutoML-Zero: https://arxiv.org/abs/2003.03384
58. Li, Talwalkar 2019, random search for NAS: https://arxiv.org/abs/1902.07638
59. Yu 2019, NAS search phase: https://arxiv.org/abs/1902.08142
60. Zela 2020, DARTS: https://arxiv.org/abs/1909.09656
61. Narang 2021, Transformer modifications: https://arxiv.org/abs/2102.11972
62. So 2021, Primer: https://arxiv.org/abs/2109.08668
63. Bercovich, Puzzle: https://arxiv.org/abs/2411.19146
64. Gu 2025, Jet-Nemotron: https://arxiv.org/abs/2508.15884
65. Novikov 2025, AlphaEvolve: https://arxiv.org/abs/2506.13131
66. Georgiev 2025, math at scale: https://arxiv.org/abs/2511.02864
67. Lange 2025, ShinkaEvolve: https://arxiv.org/abs/2509.19349
68. Romero, NanoGPT speedrun worklog: https://www.tylerromero.com/posts/nanogpt-speedrun-worklog/
69. Porian 2024, Resolving Discrepancies in Compute-Optimal Scaling: https://arxiv.org/abs/2406.19146
