# Critique and cross-check, C07.04 Knowledge-based intrinsic motivation

## Corrections made (sources re-opened this session)
Re-opened full text of Pathak 2017, Burda 2018 (large-scale and RND), Savinov 2018 (ECO), Taiga 2019, Portelas 2019, Voyager, OMNI, ELLM.
Confirmed: ICM VizDoom 100 / 46.1 / 26.0; 66% perfect runs; 55% IDF vs RF, 75% curious vs random, 70% RF; RND 7,570 and 10,070 and 8,152 table row; ECO 40.5 / 24.7 / 54.3 / 19.8 / 29.4 (columns are Sparse, Very Sparse, Sparse+Doors); ALP-GMM 14.9 vs 10.6, 80 vs 68; Voyager 3.3x, 15.3x, 8.5x, 6.4x, 2.3x, -93%; OMNI Crafter 0.42/0.52 vs 0.56/0.78, 82 tasks, 14 interesting; ELLM 64.9, 13.6, 16.4, 66.5, 32.4.
Corrections and notes:
- ELLM: the good/impossible table mixes suggested-goal and rewarded-action columns; 5% "not allowed" is for suggested goals only. Keep the two measures separate.
- Voyager -93% is for a random curriculum, not "no curriculum".
- a12 (Bellemare) "2461 then 3439" was not rechecked; treat as unverified.
- b13 says OMNI is figure only; c04 gives the scalars. Use c04.
- a10, a11, b15 to b24 were never opened (this includes the founding LP papers Kaplan and Oudeyer 2004 and Schmidhuber 1991).
- b18, b19 (Goldilocks, Poli) are from memory only; no infant numbers verified.

## Contradictions and tensions
- Bonus methods help in the originating papers (a14, a17), but Taiga (b06) finds no edge over epsilon-greedy in Rainbow. Different agents and budgets; not resolved.
- Learning progress is praised conceptually, but Achiam (a13) found LP faltered while surprisal worked broadly; Oudeyer himself notes LP is noise-sensitive (a09). Few head-to-head LP vs prediction-error tests in deep RL.
- OMNI vs oracle interestingness mostly not significant (c05), so "better than LP" depends on the comparator.

## Weak spots
- Almost all numbers are RL benchmarks. Only Voyager is prompt-only; CDE is training-time. No test of curiosity inside a scaffold at equal tokens.
- Single-source statuses dominate: Taiga, ECO, Voyager, MAGELLAN.
- Human evidence for learning progress (infants) is unverified.
- c25 reports 0 searches succeeded in the search phase, so forward-citation coverage is thin.

## Snippet-only / not opened
a10, a11, b15 to b24, c25; Eureka (c23) and Kauvar (c17) scalars not rechecked.

## GAPS
1. Does a learning-progress ranker beat an error or novelty ranker for choosing which subproblem an LLM agent works on, at equal tokens?
2. Can a verbal self-prediction (stated expectation vs outcome) serve as a usable surprise signal in an LLM, and how well calibrated is it?
3. Do noisy-TV style traps (unanswerable but novel subtasks) catch LLM scaffolds, and how many tokens do they waste?
4. What are the exact numbers of the founding experiments: Kaplan and Oudeyer 2004, Schmidhuber 1991?
5. Is there independent replication of episodic curiosity (ECO) beyond its authors, and does it transfer to text?
6. Verified infant studies (Kidd 2012 Goldilocks, Poli 2020): N, effect sizes, replications.
7. Head-to-head LP vs prediction error vs RND in one deep-RL benchmark with the same agent.
8. Do LLM-judged interestingness signals (OMNI, Motif) resist reward hacking and bias at scale?
9. Do curiosity bonuses for LLM RLVR (CDE and others, 2025-2026) replicate on other base models?
10. Cost accounting: do curiosity operators pay for the extra tokens they use?

## Gap search results
Evidence is in evidence_d.jsonl (d01 to d16). The search budget was tight: arXiv, OpenAlex and Semantic Scholar mostly returned HTTP 429, and the last WebSearch was refused.

Closed or mostly closed:
- Gap 4 (founding numbers): Closed as far as numbers exist. Schmidhuber 2010 gives no numbers for the 1991 systems (d06). Oudeyer, Kaplan and Hafner 2007 (the journal form of Kaplan and Oudeyer 2004) gives 85% time in the second zone after about 3000 steps, error plateau near 0.09, structured trajectory in 34% of 200 runs (d04, d05). The 2004 paper itself was not fetched.
- Gap 6 (infants): Opened Kidd 2012 (42 and 30 infants, Goldilocks near 1.25 bits, small effect) and Poli 2020 (43 infants, learning progress chi2 48.87 vs 19.38 and 21.87). No independent replication found; Kidd 2014 is by the same group and only a listing (d01 to d03). Partly open on replication.
- Gap 7 (head-to-head LP vs error vs RND): Partly closed. Hou 2025 runs LP against ICM, RND, Ensemble, AMA, EME, EDT in one code base (d07, d08); Gradient-Momentum Coupling gives a second, supervised, source (d09). Both are from the proposing authors; on clean mazes progress was not best.
- Gap 9 (RLVR curiosity replication): Partly closed. CDE is only on Qwen3-4B-Base (d10). IMAGINE, a different bonus, helps on Qwen2.5 sizes and DeepSeek-7B (d11). CDE itself not replicated.
- Gap 5 (ECO replication): Partly. A third-party ICLR 2025 paper uses ECO as a DMLab baseline (d12), but the table is garbled and a clean reproduction of the 40.5 number is missing. No text transfer found. A search summary misattributed 16.3 to ECO; the table puts it on RND.
- Gap 3 (noisy-TV for LLMs): Partly. Fan 2025 shows reasoning models use about 2x to 4x more tokens on missing-premise questions (d14). No test inside a scaffold.
- Gap 2 (verbal self-prediction): Partly. Binder 2025 shows self-prediction works after finetuning, with calibration error 23.0 to 8.7, and fails on long outputs (d13). Prompt-only calibration not measured.

Still open:
- Gap 1 (LP ranker vs error ranker for LLM subproblem choice at equal tokens): nothing found (d16).
- Gap 8 (reward hacking of LLM-judged interestingness): the final search was refused; nothing new.
- Gap 10 (token cost accounting of curiosity operators): nothing verified (d15 is snippet-only).

Claims updated: K02, K03 (to supported), K07, K12 (to supported), K14 extended; new K15 to K20 (K20 records the open gaps).
