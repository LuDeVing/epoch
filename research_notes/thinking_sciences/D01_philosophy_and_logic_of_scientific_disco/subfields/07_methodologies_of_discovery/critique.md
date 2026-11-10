# Critique: D01.07 Methodologies of discovery (cross-check)

## Re-opened sources and corrections
I re-downloaded and read the PDF text of Si 2024 (2409.04109), Si 2025 (2506.20803), Wen 2025 (2506.00794), Beel 2025 (2502.14297), Lu 2024 (2408.06292), and grep-checked HypoGeniC, MOOSE-Chem and DiscoveryBench. Downloads were deleted afterwards.

Confirmed exactly: Si 2024 novelty 4.84/5.64/5.81 (per review n=119/109/109), N=49 ideas, 79 reviewers, 298 reviews, 4000 seeds and about 5% at cosine 0.8, split-half 56.1%, ICLR'24 71.9%, NeurIPS'21 66.0%, Claude pairwise 53.3%. Si 2025 Table 4 ideation and execution scores, gaps -1.049/-1.760/-1.879/-1.976 vs -0.010/+0.078/-0.052/-0.628, p 0.025/0.001/0.003/0.004, 43 executors, 58 reviewers. Wen: 51.9, 77, 64.4 vs 48.9, 60.0, 63.6, 38.8 to 53.0, 1,585 and 6,000. Beel: 42%, 8%, 5 of 34 citations, 4 of 7 (57%). HypoGeniC gains, DiscoveryBench 25%, 264 tasks, 90 person-hours, 30%.

Corrections:
1. b01 says "109 reviews per condition". The human condition has n=119 reviews; AI conditions have 109.
2. Accuracy versus balanced accuracy mix-up across a19, b11, c11, c03. Lu 2024 table: human NeurIPS 2021 accuracy 0.73, balanced accuracy 0.66; AI Scientist reviewer 70% accuracy, 65% balanced accuracy. Si 2024 quotes 66.0% (balanced) for NeurIPS 2021. These do not contradict; they are different metrics. Any comparison to the 56.1% figure must use balanced accuracy (66.0).
3. a13/c03 71.4% (Claude-3.5 ranker) is on ICLR accepted-vs-rejected papers, not on the expert ideas (53.3%). Do not read it as idea-judging accuracy.
4. a18/c14 "another setting keeps about 5% with 71.6%" is not supported. In the MOOSE-Chem table 71.6% is the top-20% hit ratio at window 60 (it also appears for Llama-3.1-8B at top 20%). The window 15 / 83.7% at 4% figure is correct.
5. Si 2025 appendix gives a second set of gaps for AI ideas (-1.107, -1.843, -1.921, -2.009), apparently after controlling for idea changes; the gap is not explained by executors editing ideas (consistent with c05).
6. b02 (per-idea feasibility 6.53/6.30/6.41) and c01 (per-review 6.61/6.34/6.44) differ only by level of analysis.
7. c24 blends "53 to 56% agreement" across different measures (human split-half, LLM judge vs human consensus). Treat as loose.

## Contradictions and tensions
- Pre-execution, AI ideas win (K01); post-execution they lose (K02). Not a contradiction, but the key warning. The post-execution flip is not significant per idea.
- Social epistemology: Zollman (communication hurts) vs Borg et al. (sharing does not hurt). Model-dependent.
- Co-scientist reports Elo rising with compute, while Si finds model judges at chance on ideas (K03). The Elo judge is not validated against executed outcomes.
- Wen: models near chance zero-shot, but fine-tuned 77%; 63.6% on fresh ideas shows a distribution-shift loss.

## Weak spots
- Nearly all LLM evidence on idea appraisal comes from one research circle (Si, Yang, Hashimoto, Wen). The only independent check is Beel on the AI Scientist.
- Philosophy claims (a01-a04, a08, b14, b15) rest on SEP secondary text. Nickles, Schaffner, Darden, Laudan were never opened; PhilSci and PhilArchive returned 403.
- No LLM test of Darden-style schema instantiation or Nickles-style discoverability was found (c22).
- Execution study: N=43, one field (NLP), one generator model, 2025 models.

## Only seen in snippets or not opened
a05 (Laudan), b20 (Seselja and Strasser), b21 (Alexander et al.), b22 (Weisberg and Muldoon), c20, c21, c22. c15 (POPPER) table was garbled and its cell numbers are unverified. c17, c18 (LiveIdeaBench), c19 read at abstract or grep level. a20 per-model counts not extracted. Not re-opened by me: co-scientist, AI Scientist-v2, Chain of Ideas, SciMON, LLM-SR, AI-Researcher.

## GAPS
1. Does a cheap executed probe (small run, held-out check) predict final outcome better than a model's pre-run score, at equal tokens, for LLM-generated ideas? Only Si 2025 hints at this; no paper tests a probe-based pursuit rule head to head.
2. What are the exact ideation-to-execution correlations (Pearson/Spearman, with intervals, per metric) in Si 2025 Appendix D?
3. Does the Ideation-Execution Gap replicate outside NLP, with 2026 reasoning models, and with larger N?
4. Do 2025-2026 frontier models beat chance on Wen et al.'s pair task zero-shot, and with which prompting (full-paper retrieval, outcome priors)?
5. Is there any controlled LLM study of schema instantiation (Darden) or generative justification (Nickles) versus plain prompting at equal tokens?
6. Which allocation rule (UCB, successive halving, Elo) best splits a fixed token budget over candidate ideas when the score is noisy, and does it beat uniform allocation?
7. Does the Zollman effect or the diversity benefit appear in LLM sample ensembles (isolated versus shared early answers)?
8. How accurate are 2025-2026 LLM novelty checks that read retrieved papers (not keywords), measured against expert known-versus-novel labels?
9. Does a two-tier weak/strong evaluation gate reduce wasted budget compared with a single gate in any agent system (AI Scientist-v2, co-scientist, AI-Researcher)?
10. Do LiveIdeaBench-type findings (ideation quality not predicted by reasoning strength) hold when ideas are executed rather than LLM-panel rated?

## Gap search results
Evidence is in evidence_d.jsonl (d01 to d20). 20 lines, 18 opened.

1. Probe vs model pre-score at equal tokens (gap 1): STILL OPEN. No paper tests it on ideas. Nearest: Zhang 2026 (proxy-judged subset refinement, d08) and EarlyEval (partial-run outcome prediction for agent tasks, 26% fewer SWE-bench steps for about 1 point error, d18).
2. Ideation-execution correlations (gap 2): CLOSED. Si 2025 Appendix D: AI ideas Pearson r novelty -0.019, excitement -0.321, effectiveness 0.172, overall -0.092; human 0.158 overall. No confidence intervals given; the AI Spearman row is garbled in the PDF text (d01, d02).
3. Replication outside NLP, 2026 models, larger N (gap 3): STILL OPEN. Only the ICLR 2026 acceptance of the original was found (d19, snippet level).
4. 2025-2026 models on Wen's pair task (gap 4): PARTLY CLOSED. Mule 2026: GPT-5 57.7 to 61.1% zero-shot (consistency-aware), off-the-shelf 8B about 30%, fine-tuned 8B 77.1%, 67.49% vs Wen's 51.4% GPT-4.1 on Wen's test set, cross-domain only about 45 to 49% (d03 to d05). Retrieval and outcome-prior prompting for frontier models not tested.
5. Controlled test of schema instantiation or generative justification (gap 5): STILL OPEN for Darden and Nickles. DN-Hypo-Pipeline (Hempel/Salmon scaffold) beats direct prompting but compares 5 proposals to 1 over 3 cases (d17).
6. Allocation rule on noisy idea scores (gap 6): PARTLY CLOSED. Bandit elimination beats uniform on verifiable queries (d06, d07); on ideas only a proxy result: random-k and MMR-k beat refine-all on cost, MMR vs random yield not significant (d08, d09). UCB vs successive halving vs Elo untested.
7. Zollman or diversity in LLM ensembles (gap 7): STILL OPEN for early isolation. Regan 2024: isolation worst, random network best (d16), which does not show Zollman harm.
8. Novelty checks that read papers (gap 8): CLOSED for 2024-era gpt-4o at small n: 0.81 accuracy, kappa 0.59, n=32 (d10, d11); non-LLM RND tested only on proxy labels (d12, d13). No 2026 reasoning-model test found.
9. Two-tier weak/strong gate (gap 9): STILL OPEN. AI Scientist-v2 has staged gates with no ablation (d15).
10. LiveIdeaBench with execution (gap 10): STILL OPEN. All LLM-panel scored (d14).

Search note: arXiv API and Semantic Scholar API were rate-limited or empty, so discovery used 6 WebSearch calls and direct PDF downloads (deleted afterwards). New claims K18 to K23 added; K04 raised to established (2 sources), K02, K07, K09, K13 extended.
