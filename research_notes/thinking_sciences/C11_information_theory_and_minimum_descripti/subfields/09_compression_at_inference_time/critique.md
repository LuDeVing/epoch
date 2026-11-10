# Critique: Compression at inference time (C11.09)

Cross-checker pass, 2026-11-10. I re-opened the PDFs of Liao and Gu (2512.06104), Akyurek et al. (2411.07279), Li et al. (2411.02272), Jolicoeur-Martineau (2510.04871) and Franzen et al. (2505.07859) and checked the numbers below against the text.

## Confirmed
- CompressARC: 76K parameters, 2000 Adam steps, lr 0.01, betas 0.5/0.9; 20% eval and 34.75% train at pass@2 (a01, b01, c01).
- Eval table: pass@2 1.25% (100 steps), 10.75% (300), 15.0% (500), 19.25% (1000), 20.0% (2000); pass@1 18.5%, pass@10 26.0%, pass@100 31.25%, pass@1000 33.75%; 138 h. Train table: pass@1 30.25%, pass@10 41.5%, pass@100 48.5%, pass@1000 52.75%; 130 h.
- Human averages 76.2% (train set) and experts 98.5% (LeGris et al.), as cited by the authors.
- Augmentation inside CompressARC was worse on train (2.5% without vs 1% with). b05 is right.
- TTT (Akyurek): 18.3% to 47.1% (own fine-tuned model), 53.0% with BARC base, 61.9% ensemble; 16-task (55%) drop without geometric transforms; BBH 50.5% to 57.8%.
- Li et al. v-later table: induction 20k 35.25%, transduction 39.25%, reranking 43.0%, TTT 56.75%; human 60.2% average.
- TRM 44.6% / 7.8% and Sudoku-Extreme 87.4%; Franzen 18.3 / 44.5 / 62.5 / 67.6 / 71.6 on 8B.

## Corrections made
1. a04 says time "6 to 138 h". True for train (6 h at 100 steps) but eval starts at 7 h. Range fine; wording must say train 6 h, eval 7 h.
2. b02 and a04 say accuracy "rises smoothly/steadily". The eval table is not monotone: pass@2 is 21.5% at 1500 steps and 20.0% at 2000. Do not claim a clean scaling law; the 2000-step headline of 20% is slightly below the 1500-step value. Reflected in K03.
3. a10/b05/c10 worried that Table 1 was garbled. Reading the layout: U-Net 0.75% (target puzzle only), CompressARC 20% (target puzzle only), HRM ablation 31% (train+test puzzles), HRM 40.3% (internet-scale row sits below), o3 high 87.5% semi-private. The U-Net 0.75% is the same figure as the appendix; c10's doubt can be dropped. Row alignment is still my reading of a text extraction, not of the figure.
4. a21 and b13 give different Li et al. baselines (induction 35.25% vs 19.25%; transduction 39.25% vs 37.50%; ensemble 56.75% in both). These are two paper versions (later vs earlier). Cite the version explicitly. Both give 56.75% for the final ensemble with TTT.
5. a12, b12 and c23 are the same paper (Akyurek) counted three times; likewise the CompressARC paper appears in a/b/c many times. I counted independent sources, not lines. The CompressARC core result therefore has one independent source.
6. c25 (VARC) reports "TTT with no offline training 26.4%"; I did not re-open it. Treat as snippet-level.

## Contradictions between sources
- Compression as the mechanism (a06, c05) versus architecture as the mechanism (a09, b05, c06). The U-Net control (0.75%) shows the objective alone is not enough; the paper never runs the opposite control (the same equivariant network trained with reconstruction only). So "compression causes the gain" is not tested; only "compression plus these priors" is.
- NCA (b18, 13.37% of feasible tasks) is cited as a no-MDL contrast with CompressARC, but the architectures, task filters (172 feasible of 400) and metrics differ. Weak support.
- ARC Prize team guesses HRM run per task would match CompressARC (c20); no number measured.

## Weak spots
- One team, one paper, no independent replication found (b22, c29). Search coverage was limited by rate limits.
- Public ARC-AGI-1 only for the headline; about 4% on ARC-AGI-2 is quoted from the prize page, not from a paper.
- No seed variance published; authors only describe collapse qualitatively (a07, c12).
- No result relates compression-at-inference to LLM agents. Everything in the LLM column (TTT, PoE) is test-time training on weights, which a closed-API agent cannot do.
- Compute: 20 min per puzzle on one consumer GPU.

## Snippet-only or not re-opened
Not re-opened by me: LPN (a19, a20, b14), Deletang (a22), Huang (b17), HRM audit blog (a16, b11, c18, c19), ARC Prize 2025 page (b10, c14, c15), ARC-AGI-2 paper (b19), SOAR (c24), VARC (c25), Hardt and Sun (c27), TTT layers (a27). Those numbers rest on the earlier agents' reading (all marked opened:true by them).

## GAPS
1. Does CompressARC replicate independently (released code, other hardware, 3+ seeds) at 20% on eval, and what is the per-puzzle flip rate across seeds?
2. Is the gain from the MDL objective or from the equivariant priors? Run the same network with reconstruction-only loss (no KL) on the same puzzles.
3. Does a prompt-level proxy for compression (ask an LLM for the shortest rule that explains all demonstrations) improve ARC or text-puzzle accuracy at equal tokens versus free-form chain of thought?
4. Do CompressARC and an LLM scaffold solve complementary puzzle sets? Measure overlap on public eval, and the gain from picking the answer both agree on.
5. Can answer selection by stability across augmented views (as in PoE and ARChitects) be done by a closed-API LLM at equal tokens, and what is its gap to the oracle?
6. How does a compression-based solver do on ARC-AGI-2 and on non-grid tasks (the paper's own failure list says counting, rotation and long-range patterns fail)?
7. Is there any 2026 work that uses description length as a stopping or selection rule inside an LLM agent loop (not weight training)?
8. What is the cost curve: seconds per solved puzzle for CompressARC versus TTT versus a frontier LLM on the same items?
9. Does the weight-cost term (dropped by the authors) matter when included?

## Gap search results (2026-11-10)
Evidence in evidence_d.jsonl (d01-d17). arXiv API, Semantic Scholar and OpenAlex returned HTTP 429, so coverage rests on 6 web searches and page fetches.

1. Independent replication: OPEN. No replication or failed replication found (d01, d17). Code is public (d02) but the README gives no expected numbers, seeds or ARC-AGI-2 support.
2. MDL objective versus priors: OPEN. The paper has no component ablation and no reconstruction-only control; only the U-Net baseline (d03).
3. Prompt-level compression proxy at equal tokens: PARTLY. Rodionov 2026 tests a prompted simplification step on ARC-AGI-3 (d06, d07): better than executable-only in 3 of 4 settings, but not equal-token (1.6-2.4x tokens of textual), single runs, no textual-plus-simplification arm. No text-puzzle or ARC-grid test found.
4. Complementarity with LLM scaffold: OPEN. No overlap study; the repo's solved-list script makes it cheap to compute (d16).
5. Closed-API stability selection: OPEN. Evidence only with trained local models (AIRV d11, 200M LongT5 d12); SOAR voting is 5.25 points below oracle at 30k samples (d10).
6. ARC-AGI-2 and non-grid tasks: CLOSED for ARC-AGI-2, about 4% (d05), versus 24.03% Kaggle private and 27% semi-private for TTT pipelines (d05, d12). Non-grid tasks: no data, OPEN.
7. Description length as stopping or selection rule in an LLM agent: CLOSED as negative. None found (d14, d06); selection uses votes, train accuracy or validation score (d10).
8. Cost curve: PARTLY. CompressARC about 20 GPU-minutes per puzzle, about 100 per solved eval puzzle (our arithmetic); Kaggle $0.20 per task, Poetiq harness $31-60 (d04, d05). Same-item measurement still missing.
9. Weight-cost term: OPEN. Authors call omitting it reckless but did not test it (d03).

New claims K21-K25 added; K02, K09, K16, K12, K13, K20, K05, K18 gained evidence ids. Snippet-only: d15.
