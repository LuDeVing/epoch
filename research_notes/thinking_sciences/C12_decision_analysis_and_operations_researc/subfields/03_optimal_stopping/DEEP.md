# Optimal stopping: deep document

*Subfield C12.03. Writer pass over evidence_a-d.jsonl (a01-a27, b01-b25, c01-c28, d01-d21), claims.jsonl (K01-K25) and critique.md. Schema parts: G11 (think briefly, cap length), G12 (spend by difficulty), S6 (impasse, stop rule). Status tags: [E] established, [S] single-source, [C] contested.*

## 1. What it is

Optimal stopping asks one question. At each step you see something and must pick: take it now, or pay to see more. The goal is to maximise expected reward, net of the cost of looking.

The standard solution is dynamic programming. At each step compare two numbers: the reward for stopping now, and the expected value of continuing optimally. Stop when the first is at least as large as the second. This is the Bellman optimality equation, V_n = max(Y_n, E[V_{n+1} | F_n]) (a03).

Three problem families matter here.

1. **Secretary problem.** Candidates arrive in random order. You see only relative rank, you know n, you cannot recall a rejected one, and you win only by choosing the single best. The optimal rule skips the first r-1 and then takes the next best-so-far. As n grows, r/n tends to 1/e (36.8%) and the win chance tends to 1/e (a01, a08).
2. **Costly search with values (house selling, price search, Pandora's Box).** You see actual values. With iid offers and cost c per look, the optimal rule is a constant reservation value V* that solves E(X - V*)+ = c (a04). Weitzman (1978) extends this to boxes with different costs, using an index per box (a27, c01).
3. **Sequential testing (Wald SPRT).** Sample until the posterior crosses a lower or upper bound (a05). This is the base of most LLM "stop sampling" rules.

Why it matters for our agent. Every scaffold loop has a stop decision: stop sampling votes, stop thinking, stop revising, stop searching, give up on an operator (S6). Guardrail G11 already says think briefly by default. This document supplies the theory for how to decide when, and the measured behaviour of humans and LLMs when they decide.

Key point in advance. The theory is old and solid. The human data are mixed. The LLM data are mostly 2025-2026 preprints, strong on token savings and weak on accuracy gain at equal compute. No one has given the classic secretary problem to a language model (d01).

## 2. History and theories in depth

**Origins.** Cayley (1875) posed a lottery-selling problem solved by backward induction. Moser later recast it as house selling (a07). The secretary problem appears as the marriage problem and as Googol (Fox and Marnie 1958). Flood circulated it in 1949 and 1958. Gardner's February 1960 Scientific American column was the first publication (a08). Lindley (1961) and Chow, Moriguti, Robbins and Samuels (1964) solved the expected-rank version. Gilbert and Mosteller (1966) gave the full-information version and several-chance variants (a21, second-hand).

**The 1/e rule and its limits (a01, a02, a08, a11).**
- Exact finite-n table (Ferguson): n=1..8 gives r = 1,1,2,2,3,3,3,4 and win probability 1.0, .500, .500, .458, .433, .428, .414, .410. Wikipedia adds n=10: .399.
- If the goal is a low expected rank, not a win on the best, the optimal rule is staged. Limit expected rank is 3.8695. Wait 25.8% and take rank 1; after 44.8% take rank 1 or 2; after 56.4% take rank 1 to 3.
- If payoffs are cardinal (iid uniform values, you learn only "best so far", payoff is the realised value), the optimal skip is sqrt(n)-1, not n/e (Bearden 2006, a11).
- Bruss's 1/e-law (1984): success is at least 1/e even if n is unknown (a08).
- With values observed and the distribution known, the optimal rule is a threshold per position. Goldstein et al. give critical percentiles by boxes left: 2 left .5; 3 .690; 4 .776; 5 .825; 6 .856; 7 .878; 8 .894. Win probabilities fall from .750 to .616 over that range (a13).

**Dynamic programming and monotone problems (a03, a06, a10).**
- The optimality equation holds under mild conditions (Chow and Robbins 1963). Ferguson warns the principle of optimality can mislead when integrability fails.
- One-stage look-ahead (stop if stopping now beats stopping after one more step) is optimal in monotone problems. It can stop too soon when later gains are not monotone. Two- and three-stage look-ahead are often good.
- The martingale (Snell envelope) and Markov (free-boundary) views are the two classical machines (Peskir and Shiryaev 2006).

**Wald and sequential testing (a05).** With two simple hypotheses and cost c per sample, the value function is concave in the posterior. The rule is two-sided. Stop when the posterior is at or below a or at or above b. This is the SPRT. The bounds usually need approximation.

**Weitzman's Pandora's Box (a27, c01, c21).** Each box has an index from its cost and value distribution. Open boxes in index order. Stop when the best value found beats the next index. Kalayci et al. map each LLM generation to a costly box.

**Behavioural theories.**
- *Cutoff rule*: skip a fixed share, then take the best-so-far. Optimal for rank-only secretary tasks. Poor description of human behaviour when values are shown (a19, b07).
- *Threshold rules*: accept if value beats a position-dependent bar. Humans fit threshold models best (a15, a19).
- *Linear threshold*: the bar falls linearly with the share of options left. Three parameters. Fits as well as a free threshold per position (b06, b07, b01).
- *Cost-to-sample*: people feel a hidden cost per look (b10).
- *Pessimistic prior*: people expect future options to be worse than they are (b14).
- *Learning-percentile agent*: re-estimates the value distribution within a game and applies optimal critical values (a14).

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Classic secretary rule: skip r-1, take next best-so-far | r/n to 0.368; win prob to 0.368; n=10 skip 3, 0.3987; n=100 skip 37, 0.3710 | a01, a08, d17 | [E] |
| Stopping early is cheap in the classic task | n=100: 25% cutoff gives 0.3504, 50% gives 0.3491, vs 0.3710 optimal | d17 (own computation) | [E] theory |
| Cardinal payoff: skip sqrt(n)-1, not n/e | Uniform values, no recall | Bearden 2006, a11 | [E] |
| Expected-rank goal: staged cutoffs | Limit rank 3.8695; cut points .2584, .4476, .5640 | a02 | [E] |
| Constant reservation value for iid offers with cost, no recall | E(X-V*)+ = c; recall does not help | a04 | [E] |
| Humans stop earlier than optimal in classic rank-only task | Direction only; no figures obtained | Seale and Rapoport 1997 via Bearden and Goldstein, a17, d18 | [S] (second-hand) |
| Price search: earlier stopping, small loss | Mean stop 4.7 vs optimal 5.2; 17.1 of 20 points; about 6% below optimal earnings | Baumann 2020, b06 | [E] |
| Early positions accept too soon, late positions search too long | At position 9: accept 28% (CI 26-29) vs optimal 50% | b06 | [S] |
| Best-choice fMRI task: undersampling, worse at longer lists | N=32; F(1,31)=16.96; list 12 t=4.98, list 8 t=1.4 n.s. | Costa and Averbeck, b09 | [E] |
| Cost-to-sample explains half of individuals | Mean $0.093; 16 of 32 improved; rho=-0.67 | b10 | [C] |
| Undersampling replicated, large effect | N=47, d=-2.52 vs ideal observer | van de Wouw 2024, b11 | [E] |
| Paid-by-value payoff shrinks the gap | d=-0.61 (full) vs -1.72 (ratings) | b13 | [E] |
| Pessimistic prior beats cost and cutoff models | N=151; vs Cut Off d=-0.87; vs Cost to Sample d=-0.45 | b14 | [C] |
| Bias reverses with attractive faces | Oversampling, too-high thresholds, 3 studies | Furl 2019, b15 | [E] |
| Linear threshold fits humans | N=2,520; one shared slope; 4 distributions x 3 horizons | Christian 2026, b01 | [E] |
| Cutoff model fits near random | gamma 0.02; misfit p<.05 for 35% (best-option) vs 8% (free thresholds) | b07 | [E] |
| Full-information task accuracy falls with length | 54.5% (n=10), 47.0% (n=20), 43.0% (n=50); N=10 | Lee 2004, a18 | [S] |
| Humans use biased-optimal or threshold rules, not cutoff | Predictions correct 81/78/88% (biased optimal) | a19 | [S] |
| Learning in repeated games: fast (Goldstein) | 6,537 players, 48,336 games; classic optimum by game 2, then +10 to 15 points; 62.2% optimum (7 boxes) | a12 | [C] |
| Learning: none (older studies) | Campbell and Lee 2006; Lee 2006; Guan and Lee 2017; Baumann F(1,64)=0.02 | a16, b07 | [C] |
| Early over-exploration in one-shot task | Decaying bonus improves fit dBIC=79.7 | b03 | [S] |
| Time pressure collapses bounds faster | N=4 | Kira 2025, b16 | [S] |
| Adaptive-Consistency: fewer samples, same accuracy | Up to 7.9x; mean drop under 0.1%; GPT-3.5 4.4x, Vicuna-13B 1.9x, Code-Davinci 3.4x; 17 datasets | Aggarwal 2023, c13 | [E] |
| ESC window stop | MATH -33.8%, GSM8K -80.1%, StrategyQA -76.8%, CommonsenseQA -78.5%, Coin Flip -84.2%, Last Letters -67.4% | Li 2024, c14 | [E] |
| Other labs agree on sampling savings | Blend-ASC 4.8x vs oracle fixed 3.75x; RL-guided 33-46% fewer than ASC; PETS up to 75% offline | d10, d11, d12 | [E] |
| Reliability-weighted voting | Gemma-3-4B GSM8K about 70% less cost than SC | Kim 2026, b19 | [S] |
| SPRT on votes | Tokens saved 15-60%; example 262M to 144M (45%) | OptPO, a25, c06 | [S] |
| Pandora/UCB best-of-N stop | 15-35% fewer generations; win rate over equal-budget BoN above 54%, about 50% at minimal budget | Kalayci 2025, c01, c02 | [E] modest |
| CoT stop modules | 20-60% shorter, under 2 points loss; GSM8K -59.3%, MATH-500 -52.8%, AIME only -6.9% | OS-Pruner, c03, c04 | [S] |
| Answer convergence | About 60% of steps to convergence; QwQ GSM8K 755.1 to 418.9 tokens (-44%), 0.2% drop | c15 | [E] |
| Black-box answer-probe stop | -16.08% tokens, six datasets, three LLMs | ES-CoT, c16 | [S] |
| Answer-level stops fire too soon | 45.2% (confidence) and 53.5% (consistency) of wrong early exits would have been right | PUMA, c18 | [S] |
| Oracle stop gain | Up to +21% accuracy; practical stops remove up to 50% of verbose overthinking only | d19 | [S] |
| More thinking hurts | R1-32B/s1-32B: +3.2% per 500 tokens early; negative beyond 12K; flip ratio 3.29; stop at 6K saves 50% compute for 6% accuracy loss | Zhou 2026, b20 | [E] |
| Adaptive vs uniform cap, equal budget | 256 tokens: 3.0 vs 14.6 (balanced); 2048: 21.6 vs 22.8 | CLEAR, d09 | [E] gain shrinks with budget |
| Hidden-state probe loses level under shift | False stop 30.77-40.6% vs 5% target; keyword tests 0.75-9.0% | Xie 2026, d06 | [C] |
| Probes do not beat a length rule at failure location | 0 of 10 runs beat it at 4B; miss 81% and 47% | d07 | [S] |
| Doomed-episode abort | At 90% recall: -60.2% tokens (TextCraft), -54.9% (WebShop) | b22 | [S] |
| Escalate mid-generation | 30.2% less compute for 75% accuracy (14,841 vs 21,273 tokens) | Shaikh 2026, c12 | [S] |
| Sales-call quitting | -54% time on failed calls; 11,627 calls; reallocation up to +37% sales | c07 | [S] |
| Formal controllers can lose to simple baselines | Real LLM N=60: EM 0.500 vs 0.817 always-retrieve; stop rules alone at most 4 points | Di Gioia, c10, c09 | [E] |
| Agents judge a source useless but do not stop | Label useless 97-100%; Qwen3-8B answers 1 of 292 after 5 useless results; forced answer: Haiku 4.5 right 114 of 284 vs 1 | Zhang 2026, d02 | [E] |
| Budget acts as deadline, not evidence cue | Budget doubled moves answer from action 8 to 16 | d03 | [S] |
| Harness rule fixes the link | +0.026 to +0.097 success; non-inferior in 14 of 14 tests | d03 | [E] |
| LLM stagnation self-judgment fails | Conservative: +159% tokens; neutral: -5.0% accuracy; programmatic gate -39% tokens, no loss | d14 | [S] |
| LLMs underestimate remaining cost | 20 of 20 model-env pairs; coverage after SFT+RL at most 47%; acting on "impossible" saves 28-64% tokens, costs 1.6-4.2 points | BAGEN, d04 | [S] |
| Playbook of stopping lessons | Timely abstention 26.7 to 57.4 (Llama-3.3-70B, 20 trajectories) | Agentic Abstention, d05 | [S] |
| Costs and priors in prompt | Optimal-policy match 94.0% vs 23.0% (Qwen3-8B, 100 examples) | Calibrate-Then-Act, d15 | [S] |
| Quantile threshold immune to order-preserving miscalibration | Selective accuracy 0.64 vs 0.34 best baseline (Phi-3, rate 0.9) | d13 | [S] |
| LLM-written stop policies | Within 0.002 of Ridge LSMC, no gain; 24 attempts | Qian 2026, c22 | [S] |

## 4. Mechanisms and models

Each block below is written so an engineer can code it.

**4.1 Generic DP stop test.**
```
value_stop(state)  = reward you get if you answer now
value_cont(state)  = E[ max(value_stop(next), value_cont(next)) ] - cost_per_step
stop if value_stop >= value_cont
```
In practice you do not have the true distribution. Replace it with an estimate from past runs on the same task class.

**4.2 Reservation score (iid candidates, no recall) (a04).** Estimate the score distribution F of one candidate. Solve for V* in E[(X - V*)+] = c, by bisection on a sample of past scores. Accept the first candidate with score at or above V*. Cost c is in the same units as the score (for example score points per extra generation). Recall does not help, so no need to keep a long list for this rule alone. Keep best-so-far anyway (S5 keeps it).

**4.3 Position-dependent threshold with known distribution (a13).** For k boxes left, accept if the percentile of the current value is above crit[k]. Table: k=2 .5, 3 .690, 4 .776, 5 .825, 6 .856, 7 .878, 8 .894. Only percentiles matter, not the shape of F. Use a rolling percentile estimate.

**4.4 Linear threshold (b06, b07, b01).** Three parameters.
```
theta(t) = a + b * (remaining / total)
accept if value(t) >= theta(t)
```
The slope b is shared and positive. Intercept a depends on the value distribution and horizon. Fit a, b on past episodes by grid search maximising mean reward. Linear policies fitted this way earn nearly as much as the true optimum (b04). Prefer this when you cannot solve the DP.

**4.5 Sequential vote stop (Adaptive-Consistency) (c13).** Keep counts of each distinct answer. After each sample, model the majority share with a Beta (two answers) or Dirichlet (many). Stop when the posterior probability that the current majority stays majority is at least 0.95. Lower the 0.95 to save tokens: samples rise steeply near 1 while accuracy plateaus. Needs answers that compare for equality.

**4.6 ESC window rule (c14).** Sample in windows of 5. Stop when all answers in one window agree. Set a max (64 for math, 40 otherwise). Cheap, no model of F.

**4.7 SPRT on votes (a05, a25).** Test "answer A is the consensus" against "it is not" with alpha = beta = 0.05. Accumulate a log likelihood ratio per vote. Stop when it crosses ln((1-beta)/alpha) or ln(beta/(1-alpha)).

**4.8 Pandora's Box for best-of-N (c01).** Treat each generation as a box with cost c. Keep a running estimate of the reward distribution. Rescale rewards across prompts with a Bradley-Terry style transform. Stop when the best reward so far exceeds the estimated reservation value (UCB-style learned threshold). Gain over a tuned fixed N is modest (win rate about 54%).

**4.9 Anytime-valid e-process stop (c17).** For a per-chunk signal, keep a running e-value. By Ville's inequality the false-alarm rate stays below alpha at every stopping time with no held-out calibration data. Run two streams, commit and abstain. The guarantee is on the signal, not the final answer.

**4.10 Chain-of-thought stop.** Options, from cheapest to dearest:
- Answer convergence: at each "wait" marker ask for the current answer; stop after a run of identical answers (c15, c16). Saves 16-44%.
- Repetition and redundancy detector with a verify step before exit (PUMA, c18).
- Learned stop head on hidden state with conformal control of premature exits (LYNX, c19; OS-Pruner, c03).
- Quantile threshold on a value estimate of the prefix (d13). Threshold set as a quantile of scores on a held-out set; ranking is all that matters.

Known side effect: forcing an end-of-think token often does not stop reasoning (regeneration above 20% for QwQ-32B, c24).

**4.11 Programmatic exhaustion gate (d14, d03).** Code, not the model, decides.
```
if last 5 results labelled no-progress  -> force answer
if action overlap with recent actions high and no new facts -> halt
```
A cheap lexical detector (few shared content words with the question means useless) did about as well as the model's own judgment (d03). The gate hurts slightly when the agent has no accumulated-fact state (d14).

**4.12 Escalation as stopping (c11, c12).** Keep a posterior of eventual success while generating. Escalate to the stronger model when it falls below a time-varying threshold. Real test used a constant threshold. Regret depends on calibration quality; accuracy fell from 95.2% to 85.7% as calibration data were contaminated 0% to 30% (simulation).

**4.13 Cost and prior in the prompt (d15).** Write the per-action cost and the prior over outcomes in the prompt. This lifted optimal-rule matching from 23.0% to 94.0% on a toy task. It is a prompt device, not a stop rule by itself.

## 5. What holds up

**Holds (replicated or multi-source).**
- The theory (a01-a06, a11). Exact and checkable. Our own recomputation matched the finite-n table (d17).
- Humans in costly search tasks stop a little early and lose little (K01). Four sources: Baumann, Costa and Averbeck, van de Wouw, plus the classic literature.
- Threshold rules fit humans better than cutoff rules, and the linear threshold is as good as a free threshold (K03, K04).
- Sequential stop rules for self-consistency cut samples by large factors at kept accuracy, confirmed by at least six independent sources (K09). Direction is solid. Exact OS-Pruner and OptPO figures are not independently replicated (d21).
- Adaptive stopping beats flat fixed budgets only modestly, and most under tight budgets (K12): CLEAR +11.6 points at 256 tokens but +1.2 at 2048; Blend-ASC 4.8x vs oracle fixed 3.75x; Kalayci win rate about 54%.
- More thinking can hurt, and the best stop varies by difficulty (K11).
- Self-judged stopping by LLM agents is unreliable; harness rules work better (K15, K19, K24).

**Failures and contradictions.**
- *Learning.* Goldstein 2020 found fast learning with 48,336 games. Four earlier lines found none. Likely cause: number of games, feedback type, incentives. Unresolved (K07, [C]).
- *Direction of bias.* Undersampling is common, but oversampling appears with attractive faces and at 10 options (b14, b15). The bias depends on payoff and context.
- *Explanation.* Pessimistic prior (one lab) versus cost-to-sample (Costa). Not separated by intervention (K08, [C]).
- *Answer-consistency stops.* One paper reports accuracy rising slightly on NQ (c15). Another finds 45-54% of wrong early exits would have been right (c18). Difficulty explains the split.
- *Formal controllers.* Di Gioia's simulated gain of 36 and 33 points came from tool choice, not stopping; stop rules alone gave at most 4 points; the real-LLM test lost to always-retrieve (c09, c10).
- *Probe-based stops.* Lose false-stop control under shift (30-41% vs 5%) (d06).

**Moderators.**
- Payoff structure: top-rank payoff gives strong undersampling; paid-by-value shrinks it (b13).
- Horizon: gap grows with list length (12 vs 8 in b09); thresholds fall with fewer trials left (b01).
- Difficulty: stop savings are large on easy items and small on hard (AIME -6.9%) (c04).
- Budget: adaptive gains shrink as budget grows (d09).
- Model size: bigger models converge more confidently and gain more from answer-consistency stops (c15). Small distilled models often fail to stop (c20).

**Interventions that worked.**
- Harness-enforced integration rule after 5 useless results (+0.026 to +0.097 success) (d03).
- Programmatic gate (up to 39% fewer tokens, no loss) (d14).
- Playbook from 20 trajectories (timely abstention 26.7 to 57.4) (d05).
- Priors and costs written in the prompt (23.0% to 94.0%) (d15).
- TLDR length-penalised RL (about 50% fewer tokens) and temperature scaling on end-of-sequence probability for small models (c20).
- Attention biasing toward the injected end token reduces spurious termination (c24).

**Interventions that did not work.**
- Stating a budget: the model treats it as a deadline (d03).
- Stating a per-call cost: mostly ignored (d03).
- Showing the running count of useless results: no stop on that count (d03).
- Rule written in words: followed only partly (two of seven models) (d03).
- Prompting an LLM to judge its own stagnation: loops or early stops (d14).
- Suggested stops in a coding task: followed 6.5% (b25).
- Structured memory over score-only memory for LLM-written stop policies (b24).

## 6. Language models

**No secretary-problem study exists.** About 20 query variants found none (d01, c27). Whether LLMs stop too early like people is untested. Coverage was arXiv and a paper index only, so this may be partly a coverage gap.

**What exists clusters in five groups.**

*A. Sampling stops (vote-based).* Adaptive-Consistency (7.9x fewer samples, under 0.1% drop, c13); ESC (-33.8% to -84.2%, c14); reliability weighting (b19); Blend-ASC (4.8x, d11); RL-guided (33-46% fewer than ASC, d10); PETS (up to 75%, d12); OptPO (15-60%, c06). Measured in samples more than tokens. Savings are smallest on the hardest sets (MATH in ESC). Older models in the first two.

*B. Best-of-N with a reward model.* Kalayci: 15-35% fewer generations at the same reward. Win rate over equal-budget Best-of-N above 54%, 1,600 generation profiles, four 7-9B models (c01, c02). Reward-model scores, not correctness.

*C. Chain-of-thought stops.* Savings of 16% to 65% by method and dataset (c03, c15, c16, c19). LYNX: GSM8K -40-65% tokens with equal or better accuracy; MATH-500 up to +12 points with 35-60% fewer tokens; AIME 2024 kept accuracy with over 50% saving (c19). OS-Pruner baselines lose accuracy fast at large savings: answer-convergence at 50.9% saving falls from 88.7 to 82.6 on GSM8K, OS-Pruner at 49.6% saving keeps 88.3 (c05). On hard tasks the signal fails: AIME saving only 6.9% (c04). Oracle stop at the first correct prefix would add up to 21% accuracy, practical stops do not capture it (d19). Overthinking is real: past about 12K tokens R1-32B loses accuracy (b20).

*D. Agent loop stops.* Agents label a failing source useless 97-100% of the time and still do not stop (d02). They stop too late, opposite to the human early-stop pattern. A visible budget moves the stop to the deadline (d03). They underestimate remaining cost in all 20 model-environment pairs (d04). All 13 tested agents have under 40% average timely abstention (d05). Bigger models abstain eventually but not earlier; reasoning mode helps timeliness and hurts overall recall (d05). A harness rule or programmatic gate fixes most of this (d03, d14).

*E. Learned or formal controllers.* Escalation (30.2% less compute, c12), abort (up to 60.2% fewer tokens at 90% recall, b22), sales quitting (-54%, c07), MDP controller (tau2 telecom 29% to 96% with 93% fewer calls, b25), HJB agent (simulated, c09). Counter-evidence: real-LLM HJB lost to always-retrieve (c10); LLM-written policies did not beat Ridge LSMC (c22).

**What changed behaviour, by how much.**

| Change | Effect | Source |
|---|---|---|
| Forced answer after 5 useless judgments | Haiku 4.5 right 1 to 114 of 284 | d02 |
| Harness rule | +0.026 to +0.097 success | d03 |
| Programmatic gate vs LLM judgment | -5.0% accuracy or +159% tokens, versus up to 39% tokens saved at no loss | d14 |
| Playbook, 20 trajectories | Timely 26.7 to 57.4 | d05 |
| Priors plus cost in prompt (thinking on) | Rule match 23.0% to 94.0% | d15 |
| Priors only, no thinking | 20.0% | d15 |
| Thinking on, no priors | 23.0% | d15 |
| Budget doubled | Stop moves with deadline, no gain | d03 |
| Adaptive vs uniform cap | +11.6 points at 256 tokens, +1.2 at 2048 | d09 |
| Conformal control on exit probe | Premature exits bounded in-domain; fails under shift (30-41%) | c19, d06 |

**Calibration and the stop signal.** Verbalized confidence is concentrated on a few high values, so absolute cutoffs on it are coarse (d20). A rank-quantile threshold is immune to order-preserving miscalibration (d13). Answer-level signals fire too early on hard items (c18). Keyword sequential tests held their level on every set tested (d06). Evidence for calibration drift under heavy reasoning is weak (c23: ECE 0.044/0.104/0.050/0.015, not the predicted U-shape, 42% valid responses).

**Caveats.** Most 2026 items are preprints without peer review: OS-Pruner, Shaikh, Judged Useless, BAGEN, Agentic Abstention, Context Gathering, StreamStop (critique.md). Several savings are in tokens, not accuracy at equal compute. d08 token counts are not exactly matched across rows. d10 table averages come from garbled PDF text. Models in the sampling studies are mostly 2023-2025.

## 7. What our agent should take

Tags: part = G (guardrail), S (state), O (operator), memory. Status in brackets.

### Add now (established)

1. **Replace fixed-N voting with a sequential stop.** Beta/Dirichlet at 0.95 (c13) or ESC window of 5 (c14). Part: G11 / sampling states. [E] Evidence: c13, c14, b17, b18, d10, d11, d12 (K09).
2. **Use a harness rule, not model self-judgment, for impasse.** Code-fired stop after 5 no-progress steps, repeated action, or no new facts. Part: S6 (already fired by code; make the thresholds explicit). [E] Evidence: d02, d03, d14 (K19, K24, K15).
3. **Always compare against always-continue and fixed-N at equal tokens.** Any new stop rule must beat these or it does not ship. Part: G11, evaluation rule. [E] Evidence: c10, c09, a26, d02, d14 (K15).
4. **Do not hard-code 37%.** When a verifier score is visible use a value threshold; when only ranks, the cutoff is n/e only for win-on-best; cardinal gives sqrt(n)-1. Part: G11 / S6. [E] Evidence: a01, a02, a11, b07, a19 (K04, K05).
5. **Compute the reservation score from the agent's own score distribution.** Solve E(X-V*)+ = c on past scores. Part: S6. [E] theory; the LLM payoff is [S]. Evidence: a04, a13 (K06).
6. **Adaptive stop is worth most under tight budgets.** Use it for spend-by-difficulty (G12): cap more tightly on easy items, allow more on hard. Part: G12 / G11. [E] Evidence: d09, d11, c02, c04, b20 (K11, K12).
7. **Expect answer-consistency stops to fire early on hard items.** Stratify by difficulty and add a verify step before exit. Part: S6. [E] Evidence: c15, c18, c04 (K10).
8. **Keep best-so-far at every stop.** Already in S5; it is what makes an early stop cheap (a04, d17). Part: S5 / memory. [E] theory.
9. **Record a stop reason by code** (rule that fired, step, spend). Needed for every test in section 8. Part: memory. Practice, no direct evidence.

### Test first

| Item | Part | Status | Evidence ids |
|---|---|---|---|
| Linear-in-remaining-budget acceptance threshold (3 parameters) | S6 | [E] for humans; [S] for LLMs | b01, b06, b07, b04, d03 (K03, K17) |
| Rank-quantile stop threshold on a verifier or value score | G11 | [S] | d13, d20 (K22) |
| Bayesian SPRT on votes (alpha = beta = 0.05) | G11 | [S] | a25, c06 (K13) |
| UCB/Pandora stop for best-of-N with a reward model | G11 | [E] modest gain | c01, c02 (K12) |
| Anytime-valid e-process or keyword sequential test for CoT stop | G11/S6 | [C] | c17, d06 (K21) |
| Learned probe for abort/escalate | G11 | [S] | b22, c12 (K14) |
| Weitzman index for choosing the next operator (O1-O8) | S6 / operators | [S] | d15, c21 (K23) |
| Playbook of stopping lessons from prior episodes | S6 / memory | [C] | d05, a12 (K07) |
| Remaining-cost bound at checkpoints, with abort on "impossible" | G11 | [S] | d04 (K20) |
| Scripted controller for stop-versus-continue | S6 | [S] | b25 (K16) |
| Elicit predicted best-of-remaining before stopping (pessimistic prior probe) | G11 | [C] | b14, b10 (K08) |
| Cardinal secretary probe on the agent | G11 | [S] gap | d01 (K18) |

## 8. Concrete tests on our bench

All arms at equal total tokens per item (cap enforced by the harness). Use the bench skill. Report the stop reason and step by code.

| # | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 | Candidate stream with verifier score (existing solve items), N up to 16 | A: fixed N=8. B: reservation-score stop. C: UCB/Pandora stop. D: always continue to cap | Accuracy at equal mean tokens; tokens at equal accuracy | B and C save 15-35% tokens at equal accuracy vs A (c01); gain over a tuned A is small. Fail if under 5% saving |
| T2 | Answer-comparable items (math, short answer) | A: majority at fixed N=16. B: Beta/Dirichlet 0.95. C: ESC window 5. D: SPRT 0.05/0.05 | Accuracy and tokens; premature-stop rate by difficulty bin | 30-70% fewer samples, accuracy within 0.5 point (c13, c14); worse on hard bin |
| T3 | Items with a silent-failure source (tool returns junk) | A: model-judged stop. B: harness rule, 5 no-progress steps. C: lexical no-progress detector. D: always continue | Success rate, tokens, late-stop count | B/C raise success by 0.03-0.10 and cut tokens (d03, d14). A over-spends |
| T4 | Mixed-difficulty set, tight and ample budgets | A: uniform token cap. B: difficulty-aware cap (length predictor). C: adaptive stop | Accuracy per token at 25%, 50%, 100% of mean budget | B/C beat A by about 10 points at tight budget, about 1 point at ample (d09) |
| T5 | Reasoning items, reasoning mode on | A: full length. B: answer-convergence stop. C: B plus verify. D: length cap | Accuracy, tokens, share of wrong early exits that full reasoning would fix (c18) | 16-44% tokens saved; hard bin loses accuracy unless C |
| T6 | Cardinal secretary task, known distribution, n in {7, 15}, 200 episodes | A: agent unaided. B: agent with critical-percentile table in prompt. C: agent with costs and priors written down. D: optimal rule | Win rate vs optimum (.622 at n=7, just under .60 at n=15), mean stop position | New. Agent likely below optimum; B closes most gap if d15 transfers. Also a direct test of early vs late stopping |
| T7 | Same task across 20 consecutive episodes with outcome feedback | A: no feedback. B: win/loss only. C: playbook of lessons after every 5 episodes | Win rate curve by episode | Human result contested (a12 vs a16); playbook gain is the question (d05) |
| T8 | Budget-counter task: visible remaining steps, value stream | A: no counter. B: counter. C: counter plus linear threshold in the scaffold | Fitted slope of acceptance threshold on remaining share; reward | Prediction from d03: A and B show no smooth slope, stops land at the deadline; C gives positive slope |
| T9 | Scaffold operator selection (S6): items where operators have different measured cost and success | A: next unused operator in fixed order. B: Weitzman-index order from logged costs and success. C: model picks with costs and priors in prompt | Solve rate at equal tokens | B or C beats A by 2+ points if operators differ; no effect if operators are similar (c21, d15) |
| T10 | Checkpoint forecast: agent states a bound on remaining steps every 3 steps | A: no forecast. B: forecast with abort on "impossible" | Coverage of interval, bias, tokens saved on failed runs, success loss | Underestimates remaining cost (d04); abort saves 28-64% tokens on failures for 1.6-4.2 points |
| T11 | Stop-signal head-to-head on hard solvable items with a domain shift between calibration and test | A: answer stability. B: keyword sequential test. C: length cap. D: quantile threshold on verifier score | Accuracy at equal tokens; false-stop rate | Open gap (K21). Expect B and D to hold level under shift |

## 9. What does not transfer, and why

- **The 1/e rule.** Needs rank-only information, known n, one win-only payoff, no recall. Our agent sees verifier scores, can keep best-so-far, and is paid by value (a01, a11).
- **Human early stopping as a model of LLM behaviour.** The one clean LLM measure of stopping on a failing source shows stopping too late (d02, d05). The two directions may both hold in different tasks.
- **Human linear-threshold finding.** Humans set a bar that tracks remaining trials. LLM 7-8B models treat a budget as a deadline (d03). The mechanism may need to be built into the scaffold, not assumed.
- **Human learning across games.** Needs many episodes with feedback. Our agent is stateless between items unless memory carries a playbook.
- **Costs in human tasks.** Felt cost per look is a free parameter fitted post hoc (b10). Our token cost is exact and known, so the cost-to-sample story needs no extra parameter.
- **Probe-based stops.** Need hidden states of an open-weight model. A hosted API model gives none. Only black-box signals (answer stability, repetition, keyword tests, length) apply (c16, d06).
- **Test-time RL results (OptPO, TTRL).** Use stopping inside training, not a single-query loop (c06).
- **HJB / full-DP controllers.** Need a known transition model. Simulated gains did not carry to a real LLM (c10). LLM-written policies matched but did not beat a standard solver (c22).
- **Sales and advertising stops (c07, c25).** Different domain, outcomes inferred after the fact or simulated.
- **Vote stops when answers are not comparable.** They need answers that compare for equality (c13).
- **Perceptual bounds (b16).** N=4, a different task.

## 10. Open questions

1. How do standard and reasoning LLMs behave on the classic and cardinal secretary problem, and do they stop early or late? (K18; no study found.)
2. Exact founding numbers: Seale and Rapoport (1997), Gilbert and Mosteller (1966). Mean cutoff and win rate against .368. Paywalled and unopened (a17, a21, d17).
3. At equal accuracy on hard solvable problems, which stop signal wins: answer stability, hidden-state probe, e-process, repetition detector (PUMA)? (K21)
4. Does an LLM's implicit acceptance threshold fall smoothly with remaining budget when the stop is value-based, not deadline-based? (K17)
5. Regret as a function of miscalibration. Shaikh gives a bound; no direct empirical curve (c11, d13).
6. Does in-context feedback over episodes teach a better threshold, and after how many episodes? Playbook of 20 trajectories is one point (d05).
7. Multi-stage agents with tools and retrieval: how to set a joint stop rule when the real-LLM test of a formal controller lost to always-retrieve (c10)?
8. Does Weitzman's index help choose the next scaffold operator on a real task? (K23)
9. Independent replication of OS-Pruner, OptPO and reliability-aware voting on other models (d21).
10. Does the pessimistic-prior account hold for LLMs: do they under-expect later candidates? (K08)
11. Why do agents that recognise a failing source not stop? Training data, instruction style, or missing commitment mechanism? (d02)
12. Which of the 2026 preprints survive peer review?

## 11. Sources

[V] = opened and read this session. [M] = snippet or catalogue record only. Evidence ids in brackets.

**Theory and history**
- [V] Ferguson, Optimal Stopping and Applications, ch.2 Finite Horizon Problems. https://www.math.ucla.edu/~tom/Stopping/sr2.pdf [a01, a02, a07]
- [V] Ferguson ch.3 Existence of Optimal Rules. https://www.math.ucla.edu/~tom/Stopping/sr3.pdf [a03]
- [V] Ferguson ch.4 Markov models (house selling, SPRT). https://www.math.ucla.edu/~tom/Stopping/sr4.pdf [a04, a05]
- [V] Ferguson ch.5 Monotone stopping rule problems. https://www.math.ucla.edu/~tom/Stopping/sr5.pdf [a06]
- [V] Wikipedia, Secretary problem. https://en.wikipedia.org/wiki/Secretary_problem [a08, a09]
- [V] Wikipedia, Optimal stopping. https://en.wikipedia.org/wiki/Optimal_stopping [a10, a27]
- [V] Bearden (2006) A new secretary problem with rank-based selection and cardinal payoffs. https://gwern.net/doc/statistics/probability/2006-bearden.pdf [a11, d18]
- [M] Peskir and Shiryaev (2006); Chow, Robbins and Siegmund (1971); Weitzman (1978); Gilbert and Mosteller (1966); Lindley (1961); Chow et al. (1964); Bruss (1984) [a27, a21, a02]. Cited through the sources above; originals not opened.
- [V] Own computation of finite-n secretary rule, D:/research_scratch/C12.03/tmp/C12.03_calc.py [d17]

**Human studies**
- [M] Seale and Rapoport (1997) OBHDP 69:221-236. https://ideas.repec.org/a/eee/jobhdp/v69y1997i3p221-236.html [a17]
- [V] Goldstein, McAfee, Suri, Wright (2020) Learning When to Stop Searching, Management Science. https://www.mcafee.cc/Papers/PDF/SecretaryMS.pdf [a12-a16]
- [V] Lee, O'Connor, Welsh (2004) Full information secretary problem, CogSci. https://escholarship.org/uc/item/6107s96t [a18-a20]
- [V] Christian, Russek, Griffiths (2026) Feynman's restaurant problem, PNAS. https://pmc.ncbi.nlm.nih.gov/articles/PMC13250586/ [b01-b05]
- [V] Baumann, Singmann, Gershman, von Helversen (2020) Linear threshold model, PNAS. https://pmc.ncbi.nlm.nih.gov/articles/PMC7293628/ [b06-b08]
- [V] Costa and Averbeck (2013/2015) Cerebral Cortex. https://pmc.ncbi.nlm.nih.gov/articles/PMC4366612/ [b09, b10]
- [V] van de Wouw, McKay, Furl (2024) Communications Psychology. https://pmc.ncbi.nlm.nih.gov/articles/PMC11655870/ [b11-b14]
- [V] Furl, Averbeck, McKay (2019) Looking for Mr(s) Right. https://pmc.ncbi.nlm.nih.gov/articles/PMC6993934/ [b15]
- [V] Kira, Zylberberg, Shadlen (2025) Cost of deliberation time. https://pmc.ncbi.nlm.nih.gov/articles/PMC12311769/ [b16]

**LLM and AI studies**
- [V] Aggarwal et al. (2023) Adaptive-Consistency. https://arxiv.org/abs/2305.11860 [b17, c13]
- [V] Li et al. (2024) ESC. https://arxiv.org/abs/2401.10480 [b18, c14]
- [V] Kim et al. (2026) ReASC. https://arxiv.org/abs/2601.02970 [b19]
- [V] Zhou et al. (2026) When More Thinking Hurts. https://arxiv.org/abs/2604.10739 [b20]
- [V] Shaikh (2026) Bayesian self-escalation. https://arxiv.org/abs/2608.24087 [a23, b21, c11, c12]
- [V] Ruan et al. (2026) Doomed from the Start. https://arxiv.org/abs/2607.06503 [b22]
- [V] Liu, Qu et al. (2025) CaRT. https://arxiv.org/abs/2510.08517 [b23]
- [V] Qian (2026) Bermudan stopping audit. https://arxiv.org/abs/2610.14063 [b24, c22]
- [V] Vatsa and Eiers (2026) Bellman Language Models. https://arxiv.org/abs/2610.24871 [b25]
- [V] Kalayci, Raman, Dughmi (2025) Optimal stopping vs best-of-N. https://arxiv.org/abs/2510.01394 [a22, c01, c02]
- [V] Ehab et al. (2026) OS-Pruner. https://arxiv.org/abs/2607.11089 [a24, c03-c05]
- [V] Wang et al. (2025) OptPO. https://arxiv.org/abs/2512.02882 [a25, c06]
- [V] Manzoor, Ascarza, Netzer (2025) Learning when to quit. https://arxiv.org/abs/2511.01181 [c07, c08]
- [V] Di Gioia (2026) Cognitive Friction. https://arxiv.org/abs/2603.30031 [a26, c09, c10]
- [V] Liu and Wang (2025) Answer convergence. https://arxiv.org/abs/2506.02536 [c15]
- [V] Mao et al. (2026) ES-CoT. https://arxiv.org/abs/2509.14004 [c16]
- [V] Lee, Han, Kim (2026) E-process early stopping. https://arxiv.org/abs/2610.25212 [c17]
- [V] Min, Vaccarino et al. (2026) PUMA. https://arxiv.org/abs/2605.17672 [c18]
- [V] Akgul et al. (2025) LYNX. https://arxiv.org/abs/2512.05325 [c19]
- [V] Zhang et al. (2025) Small language models as efficient reasoners. https://arxiv.org/abs/2505.07961 [c20]
- [V] Belloni, Chen, Wei (2026) Online Pandora's Box. https://arxiv.org/abs/2606.07392 [c21, d16]
- [V] Hiremath and Hiremath (2026) Calibration drift. https://arxiv.org/abs/2606.11211 [c23]
- [V] Koh et al. (2026) Spurious CoT termination. https://arxiv.org/abs/2609.03633 [c24]
- [V] Fang et al. (2026) LLM-OSDA. https://arxiv.org/abs/2608.00123 [c25]
- [V] Wang (2026) Event-triggered LLM invocation. https://arxiv.org/abs/2607.13048 [c26] (abstract and opening only)
- [V] arXiv listing search for secretary problem and LLMs. https://arxiv.org/abs/2609.20797 [c27, c28, d01]
- [V] Zhang et al. (2026) Judged Useless, Queried Anyway. https://arxiv.org/abs/2610.06191 [d02, d03]
- [V] Lin, Wang et al. (2026) BAGEN. https://arxiv.org/abs/2606.00198 [d04]
- [V] Agentic Abstention (2026). https://arxiv.org/abs/2606.28733 [d05]
- [V] Xie et al. (2026) Statistical early stopping for reasoning models. https://arxiv.org/abs/2602.13935 [d06]
- [V] Hidden-state probes for localizing reasoning failures (2026). https://arxiv.org/abs/2610.22046 [d07] (abstract and introduction)
- [V] Oh and Lee (2026) StreamStop. https://arxiv.org/abs/2610.27981 [d08]
- [V] CLEAR, Shadow price of reasoning (2026). https://arxiv.org/abs/2606.03092 [d09]
- [V] RL-guided adaptive sampling (2026). https://arxiv.org/abs/2606.03102 [d10]
- [V] Blend-ASC, Optimal self-consistency (2025). https://arxiv.org/abs/2511.12309 [d11]
- [V] PETS (2026). https://arxiv.org/abs/2602.16745 [d12] (abstract and introduction)
- [V] Rebeschini et al. (2026) Knowing when to quit. https://arxiv.org/abs/2604.18419 [d13]
- [V] Context Gathering Decision Process (2026). https://arxiv.org/abs/2605.07042 [d14]
- [V] Calibrate-Then-Act (2026). https://arxiv.org/abs/2602.16699 [d15]
- [V] Thinking Past the Answer (2026). https://arxiv.org/abs/2606.02835 [d19] (abstract and introduction)
- [M] Pitfalls of verbalized confidence priors (2026). https://arxiv.org/abs/2609.32470 [d20] (abstract and introduction)
- [V] Paper-index replication search. https://huggingface.co/api/papers/search?q=optimal+stopping+LLM [d21]

## Source audit (2026-11-01)

Fresh auditors re-opened the sources of 13 established claims: 8 confirmed as written, 5 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **C12.03-K02** (now single-source: the sources are not independent). Both the face-task reversal (Furl, Averbeck, McKay 2019) and the paid-by-value and horizon results (van de Wouw, McKay, Furl 2024) come from the same Furl/McKay group; Goldstein et al. does not address the claim.
- **C12.03-K05** (reworded: the sources support less). The sqrt(n)-1 skip is Bearden's result for iid uniform[0,1] values where the decision maker learns only whether each is best so far, not cardinal payoffs in general; the value-dependent rule is a separate full-information case. Corrected claim: The 1/e rule (win probability 1/e, skip n/e) is optimal for the classic rank-only, win-on-best payoff with known n; in Bearden's variant (iid uniform[0,1] values, payoff equal to the chosen value, told only whether each is best so far) the optimal skip is sqrt(n)-1; goals like low expected rank have staged cutoffs (Chow et al.; Ferguson ch. 2).
- **C12.03-K10** (reworded: the sources support less). The oracle-stop gain of up to 21% was measured starting from multimodal benchmarks (language-only results only 'generalize' qualitatively), and the AIME -6.9% is one model (DeepSeek-R1-Distill-Qwen-7B) at the best-AES point. Corrected claim: Stopping chain-of-thought via answer convergence or learned stop modules saves about 16-60% of tokens with little accuracy loss on easy and medium tasks, but saves little on hard tasks (AIME -6.9% for DeepSeek-R1-Distill-Qwen-7B with OS-Pruner), and answer-level signals such as confidence and trial-answer consistency fire too early on hard items. An oracle stop at the first correct prefix improved accuracy by up to 21% (measured mainly on multimodal reasoning benchmarks), while practical early stopping mostly cuts verbose overthinking and does not fix harmful overthinking; hidden-state probes lose false-stop control under calibration-to-test shift (about 31-41% false stops vs a 5% target on MiP and MMLU in Xie et al.).
- **C12.03-K12** (reworded: the sources support less). StreamStop's gain (40.3% vs 35.0% success on WebShop) comes with more tokens per episode (2675 vs 1519), so it is not an equal-compute comparison; other numbers (Kalayci 15-35%, CLEAR +11.6 and +1.2, Blend-ASC 4.8x vs 3.75x) check out. Corrected claim: Adaptive stopping or allocation beats a flat fixed N or fixed token cap at equal total compute in several independent labs, but the gain is large only under tight budgets and small against a well-tuned fixed setting: Kalayci et al. 15-35% fewer generations at the same quality; CLEAR +11.6 points at 256 tokens per query but +1.2 at 2048 (Balanced stream); Blend-ASC 4.8x fewer samples vs 3.75x for oracle fixed allocation. StreamStop gains a few points of success over validation-selected fixed token budgets on WebShop (40.3% vs 35.0%) but at more reasoning tokens per episode, so that comparison is not at equal compute, and the best stopping signal is model-dependent.
- **C12.03-K19** (now single-source: the sources are not independent). All the specific numbers (97-100% useless, +0.026 to +0.097, budget and rule effects) come from one paper (Zhang et al. 2026, listed as d02 and d03); the only other source (Context Gathering Decision Process) tests a different setting and only loosely corroborates that LLM self-judged stopping is unreliable.
