# E14.04 Bandit-style exploration: cross-check critique

## Sources re-opened by the cross-checker (full PDF text, this session)
Krishnamurthy 2024 (2403.15371), Nie 2024 EVOLvE (2410.06238), Schmied 2025 (2504.16078), Burda RND (1810.12894), Zhou LATS (2310.04406), Savinov 2019 (1810.02274), Ecoffet Go-Explore (1901.10995).

## Confirmed numbers
- Krishnamurthy: basic GPT-4 suffix failure over 60% of replicates (T=500, N=20). Table at T=200, N=40: SuffFailFreq(T/2) TS 0.00, UCB 0.02, Greedy 0.47, BSRC0 0.12, BSSC0 0.03; K*MinFrac 0.23/0.12/0.03/0.11/0.29; median reward 0.59/0.70/0.60/0.65/0.54. Confirmed.
- EVOLvE: Table 1 MAB RH Flash 27.7, Pro 45.5, Gemma 7.6/10.5; AG 32.2, 59.6, 4.9, 4.1; CB Flash 0.0 to 46.4, Pro 7.1 to 64.3; UCB 90.6 / 96.4; few-shot SH 50.2 vs RH 27.5; easy 50.2 vs hard 43.0; fine-tune hard 65.6 vs easy 54.5. Confirmed.
- Schmied: 87% correct rationales, 58% greedy and 21% optimal; 40/65/65% coverage; 96% vs 14% frequency bias; +12% coverage; 70% to 35%. Confirmed.
- RND Table 1: Montezuma 8,152 vs PPO 2,497, Gravitar 3,906 vs 3,426, PrivateEye 8,666, Venture 1,859, Pitfall -3. Confirmed.
- LATS: HumanEval 80.1 to 92.7; HotPotQA 0.63 full, DFS 0.42, no reflection 0.58, no LM heuristic 0.37; w=0.5 0.55, w=2.0 0.63. Confirmed.
- Savinov noise table (DMLab): PPO 11.6, ICM 7.7, EC 18.7, ECO 28.2 (Noise); 9.8/7.6/14.8/18.9 (Noise Action); 27.0/23.8/26.2/41.6 (Original). PPO, EC and ECO rows confirmed in text; ICM row taken from b13, not re-read.
- Go-Explore: 666,474 / 18M / 1,441 levels; Pitfall 59,494 / 107,363; 43,763 without domain knowledge. Confirmed in text.

## Corrections and clarifications
1. a25 and b10 conflict. The dynamics-bonus numbers (Montezuma 400, PrivateEye 105, Venture 0) are in Table 1, which is the RNN-policy run. The CNN-policy comparison (Fig 7) says dynamics is worse on Montezuma, PrivateEye, Solaris but "similar" on Venture, Pitfall, Gravitar. So the claim "dynamics bonus scores 0 on Venture" holds for the RNN table only. Also Solaris: dynamics 3,387 is above RND 3,282. a25 should not be read as a uniform noisy-TV penalty (claim K10 marked contested).
2. a11 and b08 quote "8,152 vs 2,497 vs 400" as one comparison; the 2,497 PPO and 400 dynamics are from different columns/setups but the same Table 1. Acceptable, but the table gives no PPO number for Pitfall, PrivateEye, Solaris, Venture.
3. Schmied: c12 says 64% greedy, but the body text says 58%. The 64% is in the abstract/intro; the 58% is in the analysis section. Use 58% for the checked-rationale case; the sources are the same paper, so this is an internal inconsistency, not a contradiction.
4. Krishnamurthy: b17 says suffix failure over 60% without a horizon; the paper says T=500, N=20 for that figure (main experiments are T=100). a16 gave "T=200, N=20" for robustness runs; the paper says T=200 with N=20 and N=40 for the four GPT-4 configs. Minor.
5. Go-Explore Table (line ~2065) lists "PPO+CoEX 43,763" in the extracted text while the body text assigns 43,763 to Go-Explore without domain knowledge. Likely a column garble from the PDF extraction; the body text is clear. Also the prior SOTA in that table is 11,540 (RND, a different figure from the 8,152 in the RND paper's own Table 1, which is a different run/budget). Do not compare 43,763 to 8,152 as if same budget (K11 caveat).
6. a18 "UCB's optimal-action fraction rises 32.7% to 65.0%" could not be matched to a line in the EVOLvE text; treat as unverified. Not used in claims.
7. a02: Auer et al. say epsilon-greedy is best "almost always" only when tuned. The summary in K05 keeps this.

## Contradictions between sources
- Theory vs practice: Auer 2002, Kuleshov 2014 say tuned simple heuristics win; Kaufmann 2012 and Russo 2018 argue Thompson/UCB are efficient without tuning. Both can hold; the difference is whether a gap size is known.
- EVOLvE says algorithm-guided support helps; the same table shows it hurts the two small Gemma models. K04 states both.
- Binz and Schulz (GPT-3, 2022) find GPT-3 regret equals or beats humans, while Krishnamurthy and Schmied find newer models do not explore. Different tasks (2-arm horizon task vs 5-10 arm bandits) and model generations.

## Weak spots
- Most LLM exploration evidence is on stationary, small-K bandits with 2023-2024 models. No 2025-2026 frontier-model test of in-context exploration was found, and none on tree search with a bandit allocation rule at equal tokens.
- Almost all RL results are single-game outliers with few seeds (RND authors say 5 vs 10 seeds disagreed).
- Go-Explore results need a resettable simulator; an LLM tree can reset states, so it transfers in form, not in numbers.
- Evidence for the "per-class widen rule" itself is by analogy; no study tests a per-class bandit inside LLM tree search.

## Only seen in snippets or not opened
a03 (Lai-Robbins), a04 (Thompson 1933), a07 and b28 (Chapelle and Li), a08 (Kocsis-Szepesvari), a19 (Sutton and Barto), a20 (Schmidhuber), b27 (Auer from memory), a14 (NGU numbers not parsed), b14 and a09 (pseudo-count scores not read), b26 (OMNI abstract only). The cross-checker did not re-open Monea 2025 (c15, c16), Park 2024 (c14), Binz and Schulz (c17, c18), Du 2023 (c22), Zhang OMNI numbers (c23). Claims resting on these (K14, K16, K17) carry that risk. My attempt to fetch Monea used a wrong arXiv id and was discarded.

## GAPS
1. Does a per-class bandit rule (Thompson or windowed UCB on class pass rates) beat fixed-width search at equal tokens inside an LLM tree? No published test found.
2. Does a 2025-2026 frontier or reasoning model still show suffix failure and the knowing-doing gap in bandits, and does extended thinking close it?
3. How to define "visit count" or similarity for ideas in a text tree (pseudo-counts for language)? Which embedding or code-based measure is reliable enough to drive a bonus?
4. What is the right reward for a noisy-TV-safe widen signal in our tree: learning progress on the check, reproducibility of the check, or reachability? Which fails least when candidate texts differ only by paraphrase noise?
5. Is Thompson sampling or UCB better when the rewards are few (a few passes per class) and classes are non-stationary? Needs the window length and prior from our own pass-rate history.
6. Does an archive-and-return rule (Go-Explore style) help LLM search when most failures are wrong ideas rather than lost states? Cost of the extra return step at equal tokens.
7. How sensitive is LATS-style UCT to the exploration weight across task types (HotPotQA w=0.5 vs 2.0 was 0.55 vs 0.63; other tasks)? Is there a task-class-dependent best weight?
8. Do the Monea (positive-only episodes) and OMNI (model of interestingness) findings replicate with different base models, and do they transfer to keeping only successful attempts in memory?
9. What failed replications exist for RND and ICM-like bonuses beyond Atari (e.g., in procedurally generated or text environments)?


## Gap search results

Evidence in `evidence_d.jsonl` (d01 to d26). New claims K20 to K27. Search tools were limited: WebSearch quota ran out early, arXiv and OpenAlex APIs were rate-limited, so I worked from Semantic Bandits citations of Krishnamurthy 2024 and from known arXiv ids. Every paper cited below was opened as full text (pdftotext). Table cells that came out misaligned are flagged in the evidence lines and not quoted.

Correction to earlier text: the LATS exploration weight result is w=0.5 gives EM 0.55, default w=1 gives 0.63, w=2.0 gives 0.63 (HotPotQA, 100 questions). So w=2.0 did not beat the default. K16 updated (d26).

| Gap | Status | What was found |
|---|---|---|
| 1 per-class bandit vs fixed width at equal tokens | Partly closed, main question open | AB-MCTS (d01, d02): Thompson sampling chooses widen vs deepen, tested at equal generation calls. Best average rank on MLE-Bench (1.3 vs 2.3 to 3.3), only level with repeated sampling on ARC-AGI (Pass@2 14.0 vs 15.0 at GPT-4o). Progressive widening with the right (k, alpha) matches it on LiveCodeBench (50.7 vs 51.8, within error) but is parameter sensitive. Zuo and Zhu (d03): bandit allocation across queries at equal compute gives up to +11 points. No test on per-class pass rates and no equal-token test. |
| 2 frontier and reasoning models, suffix failure | Partly closed | Reasoning models fix exploit-from-log (d04, GPT-5-mini perfect) and explore far better in an open text game (d05: o1 177, R1 85, humans 42, GPT-4o 35). Exploration correlates with reasoning (d10). But priors still bias a thinking model (d07), 35 frontier agents still fail a grid exploration task (d06), and models misallocate re-checks (d08). No paper re-measures suffix failure on the Krishnamurthy bandit for 2025-26 frontier models. Open. |
| 3 visit count for ideas | Partly closed, measure not validated | Entailment-cluster count is the paraphrase-safe candidate (d24). Code-embedding cosine > 0.95 works as a filter (d22). Embedding choice can flip a novelty bonus (d23). Diversity scores are length-confounded (d25). No paraphrase-invariance test of any of them. Needs our own 100-pair test (K25 agent_test). |
| 4 noisy-TV-safe widen signal | Open, with pointers | No head-to-head. Evidence: forward-error curiosity is hijacked (d14, d12); learning progress is lured by variations (d19) but batching samples cuts gain noise (d16); models manage the re-check rate badly (d08). Cheapest design: entailment-cluster novelty plus a code-set re-check rate. Needs our own paraphrase-noise test (K26). |
| 5 Thompson vs UCB with few rewards and drift | Partly closed in theory | Plain UCB1 and plain TS degrade under drift (d17, d18). Discounted TS (gamma 0.4 to 0.75) is competitive with SW-UCB under slow and fast change, margin shrinks under abrupt change. Last-K Thompson sampling needs no exploration constant (d15). Window and prior must come from our pass-rate history (K22 agent_test). |
| 6 archive-and-return | Partly closed | IGE (d21): Game of 24 100% vs classic visitation Go-Explore 38+-22 at 150 steps; needs deterministic reset; cost axis is environment steps not tokens. In our tree a return is free, so the cost is the node-picking call. Equal-token test open. |
| 7 LATS weight by task | Open | Only HotPotQA, n=100, and w=2.0 equals default (d26). Authors say the optimum depends on the environment. No sweep on other tasks. |
| 8 Monea and OMNI replication | Partly closed | Monea re-opened (d20): positive-only best for naive in-context RL across Llama 3.1 8B, Qwen2.5 0.5B to 72B, Gemini 1.5 Flash 8B (same paper, so not independent). OMNI re-opened (d19): numbers confirmed (55/9 vs 82/14 tasks; 0.52 vs 0.78). No independent replication of either with other base models found. |
| 9 RND/ICM outside Atari | Partly closed | RIDE paper (d12) and E3B paper (d13) show RND, ICM and count stall in procedurally generated MiniGrid/MiniHack, and ICM drops under a noisy TV and hurts on Mario with extrinsic reward. Both are by authors of competing methods; no neutral replication found. No text-environment replication. |

Still-risky claims: K16 and K17 now rest on re-read sources, but K17's table cells were not usable. The Semantic Bandits, Wellocate and exploration-error papers (d06 to d08) are 2026 preprints with model names I could not check; read them as single-source.
