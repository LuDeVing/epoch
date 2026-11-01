# Critique and cross-check, C12.03 Optimal stopping

## Method
Reopened this session (arXiv abstract pages, PubMed abstracts) the sources behind the main numbers. Full PDFs were not re-read; Semantic Scholar and OpenAlex were rate limited. Checks are at abstract level.

## Confirmed
- Kalayci et al. (arXiv 2510.01394): 15-35% fewer generations than Best-of-N at the same performance (a22, c01).
- Aggarwal et al. (arXiv 2305.11860): up to 7.9x fewer samples, average accuracy drop under 0.1% (c13).
- Li et al. ESC (arXiv 2401.10480): MATH -33.8, GSM8K -80.1, StrategyQA -76.8, CommonsenseQA -78.5, Coin Flip -84.2, Last Letters -67.4. Exact match (b18, c14).
- OS-Pruner (arXiv 2607.11089): 20-60% shorter generation, minimal accuracy loss (a24, c03). Per-dataset numbers not rechecked.
- OptPO (arXiv 2512.02882): Bayesian SPRT on votes. Direction confirmed; 15-60% and 45% figures are not in the abstract.
- Zhou et al. (arXiv 2604.10739): diminishing returns, overthinking, best length varies by difficulty. Direction confirmed; the AIME, CI and flip-ratio numbers are not in the abstract.
- Shaikh (arXiv 2608.24087): optimal stopping on a competence posterior; 2 of 3 pre-registered predictions; MBPP 257 tasks, Qwen2.5-Coder 1.5B to 7B. Confirmed.
- Costa and Averbeck: PubMed abstract confirms an MDP-based best-choice fMRI task; behavioural numbers (F, t, cost $0.093) not in abstract, unverified.
- Baumann et al. 2020: abstract confirms linear threshold model and three studies; numbers (6% loss, 4.7 vs 5.2) unverified.

## Corrections
1. b17 says "up to 3.4x fewer samples at no average accuracy drop". The abstract says up to 7.9x with under 0.1% average drop; 3.4x is the Code-Davinci-002 average (c13). Use c13.
2. Costa and Averbeck is dated 2015 in the files; the record shows online 2013, issue 2015. Cite 2013/2015.
3. "OS-Prune" and "OS-Pruner" are the same paper; the abstract says OS-Pruner.
4. Claim status was lowered where sources were not independent: pessimistic-prior (K08) is contested (one lab, van de Wouw/Furl/McKay, versus Costa's cost-to-sample).
5. Shaikh and OS-Pruner (2026 preprints) are not peer reviewed.

## Contradictions
- Learning: Goldstein 2020 (a12) finds fast learning; Campbell and Lee, Lee, Guan and Lee, and Baumann (b07) find none. Likely due to number of games, feedback and incentives. Unresolved.
- Direction of bias: undersampling (Seale and Rapoport, Costa, van de Wouw, Baumann) versus oversampling with attractive faces (Furl 2019) and slight oversampling at 10 options (b14). Bias depends on payoff and context.
- Cutoff rule: classic reports of an early cutoff versus Baumann's cutoff model fitting at near-random (gamma 0.02). Tasks differ (rank-only vs values).
- Answer-consistency stops: c15 reports accuracy rising slightly on NQ; c18 reports 45-54% of wrong early exits would have been right. Depends on difficulty.
- Di Gioia (c09 vs c10): large simulated gains, but the real-LLM test lost to always-retrieve.

## Weak spots
- Founding human studies (Seale and Rapoport 1997, Gilbert and Mosteller 1966) were never opened (a17, a21); exact numbers for the stop-too-soon effect in the classic task are missing.
- LLM stopping results are mostly single preprints from 2025-2026 without replication; savings are often in tokens, not accuracy at equal compute.
- Kalayci uses reward-model scores, not correctness; gain over a tuned fixed N is modest.
- Bellman Language Models, Cognitive Friction and Shaikh are single-lab or small N.
- No study found that tests an LLM on the secretary problem itself.

## Only seen in snippets or abstracts
Costa and Averbeck behaviour numbers, Baumann numbers, Christian 2026 figures, OptPO numbers, Zhou numbers, CaRT gains.

## GAPS
1. How do LLMs (standard and reasoning models) behave on the classic and cardinal secretary problem, and do they stop too early like humans? Any 2023-2026 measurement.
2. At equal total tokens, does an adaptive stop beat the best fixed N or fixed thinking budget by more than noise, across independent labs? (Kalayci says modest.)
3. What are the exact founding numbers in Seale and Rapoport (1997) and Gilbert and Mosteller (1966): mean cutoff and win rate against 0.368?
4. Which stop signal is best on hard problems where answer-consistency fails: hidden-state probe, e-process test, or repetition detector (PUMA)? Head to head at equal accuracy.
5. Does the human linear-threshold finding transfer: does an LLM's implicit acceptance threshold fall with remaining budget, and does a visible budget counter help?
6. How much do stop rules lose when confidence or verifier scores are miscalibrated (premature-exit rates, regret in Shaikh)?
7. Does feedback across repeated episodes teach an in-context agent a better stopping threshold (analogue of Goldstein's learning), and after how many episodes?
8. How should a stop rule be set in multi-stage agents (tool calls, retrieval) where Di Gioia's real-LLM test lost to always-retrieve?
9. Does Weitzman's Pandora index rule (costly inspection, per-option costs) help choose which scaffold operator to run next?
10. Are there independent replications of the 2026 LLM stopping claims (OS-Pruner, OptPO, reliability-aware voting) on other models?

## Gap search results
Evidence is in evidence_d.jsonl (d01-d21). Claims K18-K25 added; K07, K09, K10, K12, K15, K17 extended; K12 raised from single-source to established. Web search quota was spent and Semantic Scholar, OpenAlex and the arXiv API were rate limited, so papers were found with the Hugging Face paper index and read in full from arXiv PDFs.

1. LLMs on the secretary problem: OPEN. About 20 query variants found no such study (d01). Related measured behaviour is the opposite direction: agents stop too LATE on a failing source (d02, d05). Our own probe would be new.
2. Adaptive vs best fixed at equal compute: MOSTLY CLOSED. Independent labs agree the gain is large under tight budgets and small against tuned settings (d08 StreamStop, d09 CLEAR +11.6 points at 256 tokens but +1.2 at 2048, d10, d11 4.8x vs 3.75x oracle fixed). Savings are mainly in compute.
3. Seale and Rapoport and Gilbert and Mosteller numbers: STILL OPEN. Both remain paywalled or unopened. Only the direction is confirmed secondhand (d18). Finite-n optimal cutoffs and win probabilities were recomputed (d17).
4. Best stop signal on hard problems: OPEN, partly informed. No equal-accuracy head-to-head exists. Probes lose false-stop control under shift (d06: 30-41% vs 5% target) and do not beat a length rule at failure location (d07); sequential keyword tests hold their level (d06); an oracle stop would gain up to 21% (d19). PUMA was not found by the index.
5. Does the human linear threshold transfer: PARTLY CLOSED, negative. A visible budget moves stops to the deadline rather than to evidence (d03). Models underestimate remaining cost (d04). No smooth threshold-by-remaining-budget measurement in LLMs.
6. Miscalibration loss: PARTLY CLOSED. Rank-quantile thresholds are immune to order-preserving miscalibration (d13); verbalized confidence is coarse (d20); BAGEN false-abort rates 2.2-6.6% (d04). A direct regret-versus-miscalibration curve is still missing.
7. Feedback across episodes: PARTLY CLOSED. A playbook from 20 trajectories lifted timely abstention 26.7 to 57.4 (d05). No curve by episode count; humans remain contested.
8. Multi-stage agents with tools: PARTLY CLOSED. A programmatic stagnation gate beats LLM self-judgment (d14, d02); explicit costs and priors raise rule-following (d15). Di Gioia's loss to always-retrieve stands.
9. Weitzman index for operator choice: OPEN. Only the Calibrate-Then-Act toy (94.0% match with priors, d15) and simulations (c21). No real-task test.
10. Independent replications of OS-Pruner, OptPO, reliability-aware voting: OPEN for the exact claims; the general direction is confirmed by three other labs (d10, d11, d12, d21).

New cautions: Judged Useless, BAGEN, Agentic Abstention, Context Gathering and StreamStop are 2026 preprints, not peer reviewed. d10 table averages were read from garbled PDF text. d08 token counts are not exactly matched across rows.
