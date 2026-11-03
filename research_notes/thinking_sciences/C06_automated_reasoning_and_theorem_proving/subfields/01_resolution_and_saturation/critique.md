# Critique: C06.01 Resolution and saturation (cross-check)

## Re-opened this session (PDF text, D:/research_scratch/C06.01, then deleted)
Checked against the arXiv PDFs: 2609.16228, 2102.13564, 2305.12295, 2310.15164, 1701.06972, 1701.06532.

Confirmed:
- Chvalovsky/Suda/Urban 2026 Table 1: TPTP 8511 to 10864 (+27.6%); Mizar40 test 1543 to 3101 (+101.0%); Isabelle 2178 to 2715 (+24.7%); CoqHammer 399 to 772 (+93.5%), train 2813 to 9799 (+248.3%). Portfolio: +13.9%, per-strategy boost 24.0%, 15.7% vs 8.4%, one model avg 23.8%. (a22, a23 ok; b-series did not cover this paper.)
- Suda 2021: layered 1:1 = 1032 (136%), 1:2 = 1036 (137%), gains 411/430; thresholds -0.5 1063 (140%), 0.25 945 (125%), 0.5 825. (b04, b20 ok.)
- Logic-LM table: GPT-4 ProofWriter 52.67/68.11/79.66, FOLIO 69.11/70.58/78.92, PrOntoQA 77.40/98.79/83.20, AR-LSAT 33.33/35.06/43.04. GPT-3.5 executable FOLIO 79.9% to 85.8%, AR-LSAT 32.6%.
- LINC: StarCoder+ 56.0 vs 41.8; GPT-3.5 62.6 vs 54.9; GPT-4 LINC 72.5 vs CoT 75.3; ProofWriter 96.4/98.3.
- Loos 2017: 4.34% vs 2.33%; 1,866 = 7.36%; CNN 81.5%; holdout 89.0/91.4/92.3/92.2.
- ENIGMA 2017: S0 22, best 41, all 52, Vampire 47, boosted 57.

Corrections:
1. a25 says Logic-LM gain is "+18.4% over CoT". The paper says 39.2% and 18.4% are the GPT-3.5 averages (over standard and CoT). For GPT-4 the gain is 24.98 over standard and 10.44 over CoT (b10 is right). Use 10.44 for GPT-4.
2. Suda 2021 baseline: a20 uses 756; b04/c09 use 734 (first run). The paper has both (rerun 756, first run 734, 137% is relative to 734). Gains-over-baseline are 411 or 430 depending on the table; do not mix.
3. b02 "Unguided 2.33% vs 4.34%" is on the 25,361 hard theorems; a12's 89.0/91.4/92.3% is on a holdout of conjectures within 1,000 processed clauses. Different test sets, not a conflict.
4. b09 FOLIO "GPT-4 72.5 vs 75.3": LINC is slightly worse than CoT for GPT-4. a26 summary says "about equal"; keep the sign.
5. a22 id 2609.16228 is dated 14 Sep 2026 (v1); it is a preprint, not peer reviewed.

## Contradictions and tensions
- Small models gain from solvers (LINC StarCoder+), strong ones do not (GPT-4 FOLIO) and can lose (PrOntoQA 98.79 to 83.20). Net gain depends on the base model and the task's depth.
- Hand-tuned E beats RL-from-scratch (TRAIL), but looped supervised learning (ENIGMA) beats hand portfolios. Difference: seed proofs.
- Better held-out recall for GNNs did not give more solved problems than trees (time cost).
- Gains from neural guidance are large in isolation and small in portfolios (+24.0% to +13.9%).

## Weak spots
- No direct measurement of given-clause algorithm effects on LLM agents; all LLM studies use the prover as a back end (translate, then Prover9), not saturation as a thinking schema.
- Almost all learned-guidance numbers are for Mizar/TPTP/SMT-LIB; transfer to word-problem reasoning is untested.
- Time limits differ (10 s, 30 s, 180 s, instruction limits), so cross-paper solved counts cannot be compared.
- Several claims are single-source (K02, K03, K09, K14-K17).

## Only seen in snippets or from memory
- Robinson 1965 (a01), Haken 1985 (b13), McCune 1997 (b14): not opened. Bachmair-Ganzinger 1994 not opened. Wikipedia pages were the only source for history and CASC counts.
- a19/a24/b07/c10/c11: only abstract and intro or secondary table reads.
- LoGiPT (b11, b24) and SATLM (b12, b25) numbers were not re-opened by the cross-checker.
- Gleiss and Suda 2020 (a11) numbers not re-opened.

## GAPS (most decision-relevant first)
1. Does an LLM agent that keeps explicit "given" and "passive" step queues (age plus weight mix) beat plain best-first or CoT at equal tokens? No study found.
2. What is the best age:weight ratio (or equivalent) for LLM step selection, and is the flat-then-drop threshold pattern (Suda) reproduced for LLM confidence scores?
3. Which tasks gain from solver routing (depth threshold, task type) and what cheap probe predicts it, given PrOntoQA shows a loss?
4. How much of Logic-LM/LINC error is translation vs solving, measured on 2024-2026 models (GPT-4 class and newer)? Newer LLM-plus-prover results (2024-2026) were not found by this run.
5. Do LLMs guiding E or Vampire clause selection (not small nets) outperform ENIGMA-style trees at equal wall time?
6. Redundancy elimination (subsumption, tautology deletion, demodulation): is there any LLM-side analogue and measured benefit (dedupe of repeated reasoning steps)?
7. Fairness and loss of completeness: how often do greedy weight queues starve old clauses, and is there an LLM analogue (step starvation) with measured cost?
8. Do looped self-improvement gains (ENIGMA +70%) appear with retrieval of past solved traces for LLM agents, and when do they saturate?
9. Do Haken lower bounds / proof-size limits matter for any LLM benchmark (proof depth > 5)?
10. Does cross-benchmark degradation (K08) also show up for LLM memory of past traces?

## Gap search results (evidence_d.jsonl, d01-d15; claims K21-K28 added)
Web search budget and the arXiv, Semantic Scholar and OpenAlex APIs were rate limited (HTTP 429), so the search was narrow. Papers opened as PDF text: LINC 2310.15164, GFaiR 2404.01677, ProverQA 2502.06563, LLM-First Search 2506.05213, CLOVER 2410.08047, LOGICPO 2506.18383, Dynamic Cheatsheet 2504.07952, Overthinking 2412.21187. Bostrom 2201.06028 was fetched but not read.

Closed or mostly closed:
- Gap 4 (translation vs solving, newer models): mostly closed. GPT-4o Logic-LM on AR-LSAT: 33.8% executable, 51.3% correct when executable (CLOVER Table 2); syntax errors 13% GPT-4 vs 38% StarCoder+ (LINC); LOGICPO error counts show meaning-loss errors persist (K21, K22). Only GPT-4o-era data; no 2026 model.
- Gap 6 (redundancy analogue): partly closed. Whole-solution dedupe: 48.6% fewer tokens, accuracy kept (K26). Step-level subsumption untested.
- Gap 9 (proof depth): partly closed. CoT stays near 50% on ProverQA hard; distractors and order cost up to 12 points (K23). No link to Haken bounds exists; Haken stays unopened.

Partly addressed:
- Gap 7 (starvation): LLM-First Search shows greedy best-first collapsing at depth (K24). No direct measure of oldest-item starvation.
- Gap 8 (looped reuse): Dynamic Cheatsheet shows large gains for strong models, small ones gain little (K27). No saturation curve.
- Gap 3 (when to route to a solver): added ProverQA and CLOVER data; the cheap predictor is still unknown. Complexity of formulas predicts translation loss (K21).

Still open:
- Gap 1 and 2 (age/weight queues for LLM steps; flat-then-drop threshold for LLM confidence): no study found (K28).
- Gap 5 (LLM as clause selector in E or Vampire): none found; the 2026 Vampire paper still uses small nets.
- Gap 10 (cross-benchmark degradation of LLM trace memory): not found; Dynamic Cheatsheet reports no cross-task transfer test in the text read.

Notes on quality: CLOVER and GFaiR tables came from two-column PDF text; row alignment was inferred (flagged in limits). Search-record lines d12-d15 are opened:false.
