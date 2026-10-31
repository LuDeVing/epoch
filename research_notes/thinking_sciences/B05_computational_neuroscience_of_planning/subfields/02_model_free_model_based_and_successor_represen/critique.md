# B05.02 Cross-check: model-free, model-based and successor representation

## Sources re-opened this session (10)
1. Binz and Schulz (arXiv 2206.14576): t(1982)=-6.16 and t(1814)=2.33 confirmed (b21, c01).
2. CogBench (arXiv 2402.18225): CoT +64.59%, step-back +118.59% confirmed.
3. Demircan et al. (arXiv 2410.01280): NLL 2729 vs 2864, max r 0.62 vs 0.49, TD r 0.60 vs 0.18, accuracy 24.3% confirmed (b23, c12, c13).
4. Hao et al. RAP (arXiv 2305.14992): 64% average, 33% relative over GPT-4 CoT, RAP(10)/RAP(20) rows confirmed.
5. WebDreamer (arXiv 2411.06559): Table 1 confirmed (reactive 17.6, tree search 26.2, GPT-4o WebDreamer 23.6; 3x steps, 10x latency). CORRECTION below.
6. CogEval (arXiv 2309.15129): GPT-4 policyReval 0.21, GPT-3.5 0.18, davinci 0.13, Claude-1 0.28, rewardReval 0.67, transReval 0.60, 1stepPath 0.99 confirmed.
7. Gillan et al. 2016 (PMC4786435): N=548 beta -0.040 SE .02 p=.049, 14% per SD; N=1413 OCD -0.026 p=.020, eating -0.037 p<.001, impulsivity -0.034 p=.007 confirmed. Note OCD in Exp 1 is only just significant.
8. Kool et al. 2016 (PMC5001643): r=0.55 vs r=0.10, t(377), factor ~230 confirmed.
9. Feher da Silva and Hare 2020: abstract only re-read (Europe PMC); the numbers (5.9x, BF 145, rho .19) are NOT re-verified.
10. Not re-verifiable this session: Momennejad 2017 (0.52 vs 0.45, N=58/88), Daw 2011. Two sheets (a06, b02) agree with each other, but they probably share one reading of the same text, so this is one source, not two.

## Corrections
- b29 said WebDreamer is "about 45 times more efficient" than tree search. The paper says 4-5 times (the "45" is a page number run into the text). Use 4-5x. It also said it "matched" tree search; on VisualWebArena it is 23.6 vs 26.2, so it is below, not equal. (Claim K20 uses the corrected wording.)
- b09 gives original-task N=207 and b06 gives Kool data N=206; a13 says 381 analysed (199 + 182?). Treat as the same dataset with small exclusion differences, not a conflict.
- b03/b12-b15 were read as abstracts or from reviews (Carvalho 2024), not primary papers. Kept, but flagged.

## Contradictions and tension
- Two-step interpretation: a04/b01 (hybrid MF+MB, 61% MF) vs b06/b07 (mostly MB with correct instructions). The Daw 2011 hybrid weights are likely inflated by instruction misunderstanding. Both are true of their own samples.
- SR as brain mechanism: a06/a21 support SR+MB hybrid; b04 offers a Kalman-filter alternative. Unresolved.
- Efficiency vs accuracy of imagination planning: c17 shows imagination below real tree search but much cheaper; RAP (c16) uses costly MCTS. Budget-matched comparison is missing.
- Centaur fit (c23) vs retrieval agents matching it (c24): c24 is a critique from a single source.

## Weak spots
- Almost all LLM two-step studies use 2022-2024 models; none tests current frontier models with the standard regression.
- The LLM SR evidence (Demircan) is one lab, one open model family, one 15-node graph.
- Parks 2026 (b32/c19) has three topologies; rank correlations of 1.0 and -1.0 are artefacts of n=3.
- Same-paper duplicates (a01/a02/b17, b30/c10, b32/c19, b22/c03) were counted as one independent source in claims.
- Unopened: Daw 2005, Tolman 1948, Gershman 2018, Dolan and Dayan 2013, Sutton 1990/2018 (a03, a17-a19, a27, a28). Described from memory only.
- No human data in Dayan 1993 or any LLM paper on SR memory design; the link to our agent is by analogy.

## GAPS
1. Does an explicit class-transition (SR-style) memory built from past runs beat no memory and beat raw-trace memory (Reflexion, GAMER) at equal tokens on our benchmarks? No direct test exists.
2. How does the SR memory fail when the agent's policy changes (operator mix or prompt)? Policy dependence is known in theory; no measured LLM case.
3. When is imagination (one-step world-model rollout) worth its tokens versus full tree search or plain CoT, at matched budget, on current models?
4. Do current frontier models (2026) still fail CogEval-style revaluation, especially policy revaluation (0.21 for GPT-4), and does a scaffold with explicit graph state close the gap?
5. Do the asymmetry results (reward easier than transition revaluation) appear in LLMs on the same Momennejad design? CogEval has the scores but not the paired contrast with a test.
6. What did Momennejad 2017 and Daw 2011 report exactly (effect sizes, exclusions)? Primary numbers are only second-hand here and should be re-opened.
7. Is Geerts et al. 2024 (Kalman TD SR) supported by independent human data that favours it over SR+MB?
8. Does a payoff-aware gate (plan only when expected gain justifies cost, per Kool 2016) reduce tokens without lowering accuracy in an LLM agent?
9. Do the replay findings (surprise-triggered replay, a15/a24) transfer to an LLM loop: does replaying high-surprise failures between attempts help?
10. How reliable is a single-run measure of an LLM's MF/MB mode (cf. test-retest ICC .02-.52 in humans)? Needed before any mode-based routing.

## Gap search results (2026-10-31, evidence_d.jsonl d01-d16, claims K30-K37)

Method limits: WebSearch hit its session cap after two calls. Semantic Scholar and OpenAlex were rate-limited. About 30 arXiv API queries and direct reads of PMC, bioRxiv and arXiv PDFs did the work. A missing hit is weak evidence.

Closed
- Gap 6 (primary numbers). Daw 2011 re-opened (d01): N=17, 201 trials, reward x transition interaction p<5e-5, median MF weight 61%. Momennejad 2017 re-opened (d02, d03): Exp 1 N=58 after 11 of 69 exclusions, t(57)=2.89 for reward vs transition; Exp 2 N=88 after 27 of 115 exclusions. Still unchecked: the exact 0.52 vs 0.45 pair, which is in a figure. Note the 23% exclusion in Exp 2.
- Gap 5 (partly closed). From CogEval Table 3 (d04), reward minus transition revaluation is +0.07, -0.02, -0.15, -0.07 for GPT-4, GPT-3.5, davinci, Claude-1, with SDs near 0.4. The human asymmetry is not a consistent LLM pattern. No paired p value, because per-cell n is not in the table. The big LLM gap is policy revaluation (0.21 for GPT-4).

Partly answered
- Gap 1. No SR memory test, but two training-free agents with structured transition graphs beat Reflexion-style memory: WebATLAS (d08) 57.4 with a structured map vs 44.8 with a raw map vs 47.9 base; ProPlay (d09) 37.4 vs Reflexion 32.2, graph worth 2.6 points. Both: one run, tokens not matched, graphs are not discounted-occupancy SRs. The equal-token test is still missing.
- Gap 3. Dyna-Think (d14) is token-efficient but trained. WebDreamer was already known. No prompt-only matched-budget comparison was found.
- Gap 8. Gates that cut tokens without losing accuracy exist: AdaptThink (d12, trained) and DART (d13, training-free, draft agreement). Neither is payoff-aware as in Kool 2016, so the payoff-aware version is untested.
- Gap 9. In-context hindsight replay helps (ECHO, d10, mixed across organisations); prioritised replay exists only in fine-tuning (d11). Surprise-ranked replay in a frozen-model loop is untested.

Still open
- Gap 2 (SR memory under policy change). Nearest is Parks 2026 (d05), where a linear SR spectrum is inverted for drift. Only three topologies.
- Gap 4 (frontier models on CogEval revaluation, scaffold with graph state). No 2025-2026 re-run found. Not found does not mean not done.
- Gap 7 (Kalman TD SR vs SR+MB on human data). Only a 2019 ML paper found, no independent human test.
- Gap 10 (reliability of an LLM MF/MB index). Bandit fits (d15) show rigid, setting-stable behaviour, but no ICC. CogEval found no temperature effect (p=.53). Do not route on a single-run mode score.

Other notes
- d06 (random-walk training gives a map code) and d07 (latent learning in RL post-training) were read; both are about training, so they are background, not scaffold tests.
- Reading limits: several numbers in d09, d10, d13, d14 come from abstracts or garbled PDF tables and are flagged in their limits fields.
