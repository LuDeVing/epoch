# Count-based exploration, unified with intrinsic motivation: deep document

*Subfield C07.03. Built from evidence_a-d.jsonl (a01-d18), claims.jsonl (K01-K19) and critique.md in this folder. Schema parts follow SCHEMA.md (G1-G12, S0-S9, O1-O8). Status marks: [E] established, [S] single-source, [C] contested.*

## 1. What it is

Exploration means trying things you have not tried, so you can learn what works. A count-based method does this with a table. It counts how often each state was visited. It then adds a bonus to the reward that is large for rarely visited states and small for common ones. The classic bonus is beta / sqrt(N), where N is the visit count.

The problem it solved: in big state spaces (Atari pixels) no state is ever seen twice, so a plain table is useless. Bellemare et al. (2016) [a01] showed that a "pseudo-count" can be read off any density model. The model says how probable a state is before and after one more sighting. From that you get a count-like number. This joined two older ideas. One is count-based exploration (UCB, MBIE-EB). The other is intrinsic motivation (curiosity, information gain, prediction error).

Why it matters for our agent. Our agent has no training. Only the idea moves over: keep a code-side table of what was tried, key it well, and prefer what is rare. The schema slot is S3 (history of directions tried). The nearest schema rules are G8 (novelty judged by running), G11 (short attempts), G12 (spend by difficulty) and S6 (impasse).

What is solid and what is not, in one paragraph. The RL result is real but narrower than first reported: bonuses help where exploration is the bottleneck (Montezuma), and help less under a strong base agent and fair tuning [E for the idea, C for the size]. The LLM evidence is thin. One count-style paper (MERCI) shows small gains. One shows hash counts fail on chain-of-thought. Nothing tests a prompt-level history table at equal tokens. That is the open gap for us.

## 2. History and theories in depth

**Tabular roots.**
- UCB (Auer 2002) is count-based and regret-optimal in bandits. The bound as restated in the LIE paper is regret at most 8 log T times the sum of 1/gap over bad arms [b24]. Auer was not opened.
- MBIE-EB (Strehl and Littman 2008) adds beta/sqrt(N(s,a)) to the reward and proves PAC-MDP bounds [a24, not opened].
- Kolter and Ng (2009) show that a bonus that decays faster than the count rate cannot guarantee PAC-MDP optimality [a25, not opened; wording differs between our files, see critique]. Bellemare used this to argue that prediction-gain bonuses explore too little.

**Bellemare et al. 2016 (the key paper)** [a01-a06].
- Pseudo-count from a density model rho: rho_n(x) is the probability before seeing x, rho'_n(x) after one more sighting. N^ = rho(1 - rho') / (rho' - rho).
- Theory: prediction gain PG = log rho' - log rho. N^ is about (e^PG - 1)^-1. Theorem 1: information gain <= PG <= 1/N^. So an N^-1/2 bonus is a safe stand-in for information-gain curiosity.
- Sanity test on Freeway: pseudo-counts near zero at first crossing, ordered by true frequency, linear in real counts on average. But they were only a fraction of real counts (start position visited about 140,000 times, top 1285 times) [a02].
- Hard Atari (Double DQN + mixed Monte Carlo return, beta 0.05, 5 trials): Montezuma 15 of 24 rooms by 50M frames, one run 6,600 points by 100M [a05].
- A3C on 60 games: A3C fails (below 1.5x random) in 15 games, A3C+ in 10, of which 8 also fail with DQN [a06].
- Setup detail: treating life loss as episode end hurt Montezuma [b03].

**Ostrovski et al. 2017** swapped CTS for PixelCNN [a07-a10]. Better in 52/57 games (max score), 51 (AUC). Surprise: the mixed Monte Carlo (MMC) return explains much of the gain on some games. The bonus alone and MMC alone do not help in the hardest games; together they do [b05]. So credit assignment was a confound in the 2016 result.

**Feature and hash counts.**
- Tang et al. 2017 (#Exploration): SimHash with a fixed random projection, count per code, bonus beta/sqrt(n) [a11, a12]. A learned autoencoder code is better on some games. Too fine a pixel code treats every state as new [b07].
- Martin et al. 2017: counts in the value function's feature space [a13, b15 abstract only].
- Machado et al. 2018: the norm of the successor representation is an implicit count [a14, c07].

**Prediction-error cousins.**
- ICM (Pathak 2017): forward-model error in a feature space learned by an inverse model, so uncontrollable noise is ignored [a15].
- RND (Burda 2018): error of a net predicting a fixed random net. Acts like a soft count. Avoids the noisy-TV trap [a16-a18].
- Large-scale curiosity study across 54 environments [a21].

**Beyond a bonus.**
- Go-Explore (Ecoffet): keep an archive of cells, return to a promising cell, then explore. Avoids detachment and derailment [a23, c14].
- NGU (Badia 2020): episodic kNN novelty times a lifelong RND factor; a family of policies with different exploration weights [a22]. Agent57 adds an adaptive bandit that picks the exploration weight [c16].

**The correction.** Taiga et al. 2019/2020 re-tested under one Rainbow agent, 200M frames, 5 seeds [a19, a20, b11-b12, b25, c12-c13]. Gains were real on Montezuma but did not carry over. Papers confound gains with longer training and bigger models.

**LLM era (2023-2026).** Counts show up as: MERCI (pseudo-counts on reasoning trajectories) [b16], CDE (counts failed, perplexity used) [b18], LIE (UCB theory, long traces) [b20], outcome counts (Song) [d03], strategy-cluster counts (Hu) [d05], covariance bonus (Tuyls) [d04], Go-Explore with an LLM (Lu) [d02], online DPO with pseudo-counts (Bai) [d08].

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Pseudo-count bonus lets DQN explore Montezuma | 15 of 24 rooms by 50M frames; one run 6,600 by 100M; 5 trials, beta 0.05, tuned on this game | a05, b01 (Bellemare 2016) | [S] |
| Bonus helps A3C on 60 games, modestly | A3C fails on 15 games, A3C+ on 10 (8 shared with DQN) | a06, b02 | [S] |
| Better density model, better exploration | PixelCNN beats CTS in 52/57 games (max), 51/57 (AUC) | a07 (Ostrovski) | [E] |
| Mixed Monte Carlo return is a confound | Neither MMC nor bonus alone helps in hardest games; together they do | a08, b05 | [S] |
| Best runs after raising bonus scale 1-2 orders | Gravitar 900, Montezuma 6,600, Private Eye 39,000, Venture 1,500 (5 seeds per scale) | b04 | [S] |
| Hash counts work in Atari | TRPO 50M steps: Freeway 16.5 to 31.6; Frostbite 2,869 to 4,683; Venture 121 to 616; Montezuma 0 to 238 | a11, b06, c04 (Tang) | [E] |
| Learned hash key better | AE-SimHash: Freeway 33.5, Frostbite 5,214, Solaris 2,251 | a12 | [S] |
| Feature-space counts | Sarsa-phi-EB Montezuma 2,745.4 with half the frames of DDQN-PC | a13 | [S] |
| SR norm as count (tabular) | SixArms ESSR 7.3 vs R-MAX 2.8, MBIE 9.3 (millions) | a14 | [S] |
| ICM in sparse VizDoom | Perfect score in 66% of random runs; plain A3C never | a15 | [S] |
| RND on Montezuma | 8,152 vs PPO 2,497, dynamics bonus 400, prior SOTA 3,700; best agent 22 of 24 rooms | a16 | [E] |
| RND other games | Private Eye 8,666; Venture 1,859; Gravitar 3,906 vs PPO 3,426; Pitfall -3 (fails) | a17, b08 | [E] |
| Dynamics-error bonus stalls | Significantly worse than RND on Montezuma, Private Eye, Solaris | b09 | [E] |
| Noisy TV slows curiosity | Unity maze with noisy TV: learning drastically slower | a21, b10 | [E] |
| "Dancing with skulls" | After extrinsic reward is exhausted, RND agent chases the bonus | a18 | [E] |
| Go-Explore | Montezuma 43,763 (no domain knowledge); 666,474 mean with it; Pitfall mean 59,494 | a23, b13 (critique-corrected) | [E] |
| NGU | Median 1,344% human-normalised; Pitfall mean 8,400; Montezuma 10.4k | a22, b14 | [E] |
| Fair re-test: bonuses help Montezuma only | Rainbow, 200M frames, 5 seeds: CTS ~5,000; others 2,500; epsilon-greedy poor | a19, c12 (Taiga) | [S] |
| Does not generalise | No correlation with other hard games; epsilon-greedy beats bonuses on Gravitar; on easy set pseudo-count worse on every game but Seaquest | a20, b11, c13 | [C] |
| Plain LLM bandit agent explores badly | GPT-4 basic prompt: suffix failure in over 60% of replicates (T=100) | c17, c18 | [E] |
| Code summary beats raw history | Only GPT-4 + CoT + external summary avoided suffix failure; EVOLvE and Harris and Slivkins agree | c17, d09, d10 | [E] |
| Positive-only subsampled history works | Banking77 Qwen2.5-7B 6.2% to 72.2% | d11 | [S] |
| MERCI small gains | mean@k 40.5 to 42.2 (GRPO), 42.2 to 44.9 (DAPO); pass@k 65.8 to 67.4; AIME25 pass@256 50.0 to 60.0 (3 of 30 problems); Minerva 64.0 to 63.2, MATH500 91.8 to 91.4 (no gain) | b16, b17, d13 | [S] |
| MERCI needs noise filtering | Without it pass@k 63.8, below 65.8 baseline | b17 | [S] |
| Hash counts collapse on CoT | Most responses fall in same or neighbouring cells; switched to perplexity: avg 48.2 to 50.6 | b18 | [S] |
| Outcome-count UCB | Naive UCB: significant test gain only for Llama-8B on easy set (3 seeds); within-batch repetition penalty lifts pass@k at large k | d03, d15 | [S] |
| Strategy-cluster count | Qwen2.5-7B AIME AUC@64: 0.131 base, 0.116 SimpleRL, 0.160 Hu | d05 | [S] |
| Hidden-state covariance bonus | Qwen-2.5-14B: over 50% better samples-to-correct; AIME24 pass@80 matches GRPO pass@256 | d04, d17 | [S] |
| RLVR narrows coverage | pass@1 26.1 to 42.5 while pass@256 falls; base ahead by about 9% at k=128 (Minerva 32B) | b21, b22, d14 | [E] |
| Independent resampling is a strong baseline | CodeContests Gemma-2B 0.02% to 7.1% (10,000 samples); SWE-bench Lite 15.9% to 56%; MATH coverage 82.9% to 98.44% while vote stays near 41% | d01 | [E] |
| Return-to-archive with LLM | Game of 24: IGE 100% in 150 ops vs classic Go-Explore 38 +/- 22; no action history 33 +/- 9 | d02 | [S] |
| Longer traces with redundancy penalty | +4.4% in-domain, +2.7% out-of-domain | b20 | [S] |
| Conditioning on earlier attempts | AST edit distance 0.072 to 0.264; pass@100+ +10.8 to +12.5 (abstract only, after fine-tuning) | d12 | [S] |
| Best strategy depends on difficulty | Sequential beats parallel on easy MATH; beam search hurts levels 1-2; naive revision flips about 38% of correct answers | d06, d18 | [S] |
| LLM-judged goals beat raw novelty | ELLM higher than RND/APT in 3 of 4 Housekeep tasks; Voyager random curriculum -93% items | b23, c21 | [E] |
| Qwen RLVR gains are confounded | Random reward +21.4 vs true reward +29.1 on MATH-500 | d07 | [S] |
| Online DPO with pseudo-counts | AlpacaEval 2.0 LC win rate 22.19 to 27.21 (Zephyr-7B); 33.17 to 35.54 (Llama-3-8B) | d08 | [S] |

## 4. Mechanisms and models

**4.1 Pseudo-count from a density model.**
1. Train a density model rho on visited states (CTS or PixelCNN on pixels).
2. For state x: rho = probability before the update. Do one gradient step on x. rho' = probability after.
3. N^ = rho (1 - rho') / (rho' - rho). Equivalent: N^ = (e^PG - 1)^-1 with PG = log rho' - log rho.
4. Bonus R+ = beta (N^ + 0.01)^-1/2. Beta 0.05 (CTS), c = 0.1 with PG decay c n^-1/2 (PixelCNN) [a07].
5. Clip PG at 0 because deep models can give negative gain. Zero count if rho = 0, infinite if rho' = rho.
6. Add R+ to the environment reward. Use a mixed Monte Carlo return so the bonus spreads fast [b05].

**4.2 SimHash counts.** Pick a fixed random matrix A (k x d). Code = sign(A g(s)) with k bits (k = 256 in Atari). Keep a hash map code -> n. Bonus = beta / sqrt(n(code)), beta 0.01. Choose k so similar states share a code but distinct ones do not. Too fine means everything is new. Too coarse means everything is the same. For learned codes, keep codes stable while the encoder trains [a11, a12, b07].

**4.3 RND.** Fixed random net f, trainable predictor g. Bonus = ||g(x) - f(x)||^2. Normalise observations and bonus. Use two value heads: a non-episodic one for the intrinsic stream (gamma_I 0.999) and an episodic one for extrinsic reward [a16, a17, c11].

**4.4 NGU / Agent57.** Episodic reward = 1 / sqrt(sum of kernel similarity to the k nearest embeddings in this episode's memory). Multiply by a clipped lifelong RND factor. Train many policies with different exploration weights; Agent57 picks the weight with an adaptive bandit [a22, c15, c16].

**4.5 Go-Explore.** Archive of cells (downscaled states). Pick a cell with weight favouring low visit count. Return to it (restore the simulator or follow the stored trajectory). Explore from there. Add new cells. Then robustify with imitation learning [a23, c14]. Intelligent Go-Explore: an LLM picks the archived state, picks the action (given the per-state list of tried actions), and decides what to archive [d02].

**4.6 Count on a semantic key (LLM version).**
1. Generate G attempts for a prompt.
2. Assign each attempt a key. Options that worked: final answer (Song) [d03]; LLM-judged strategy cluster (Hu) [d05]; hidden-state covariance (Tuyls) [d04]. Option that failed: SimHash of chain-of-thought embedding [b18].
3. Reward or preference = inverse cluster size (Hu) or UCB term on outcome (Song). Within-batch repetition penalty works better than history across training for test pass@k [d15].
4. MERCI: Coin Flipping Network learns pseudo-counts on trajectory embeddings; adds a bonus with percentile and spatial filtering. Without filtering it hurts [b17].

**4.7 What an engineer needs for our no-training agent (derived, not tested).** A dict in code: key -> count. Key = (operator, approach label), with the label assigned by one cheap model call. Choose the next direction by score = quality_prior + c / sqrt(n + 0.01) over candidate directions. Refuted outcomes go on a hard-exclude list (deterministic check means no reason to revisit) [d16]. Freeze verified answers (G6, G2) [d18]. Everything except the label call is plain code (matches Section 1 of SCHEMA).

## 5. What holds up

**Replicated across groups.**
- Some novelty-by-count signal helps sparse-reward Atari: CTS, PixelCNN, SimHash, RND, ICM, feature counts all beat epsilon-greedy on Montezuma. About 3 independent groups [K02].
- The key matters: pixels at fine granularity fail; learned or task-relevant codes do better [K03].
- Prediction-error bonuses stall on noise (noisy TV, sticky actions) [K06].
- Count novelty alone is not enough at the top end; archives (Go-Explore) and episodic plus lifelong mixes (NGU) beat it [K07].
- Raw-novelty bonuses waste effort in open worlds; LLM-judged goals align better [K12].
- Plain LLMs explore poorly; code-built summaries beat raw history [K10].
- RLVR narrows large-k coverage [K11].

**Failed or weakened.**
- Taiga: Montezuma rank does not predict other hard games. Epsilon-greedy beats bonuses on Gravitar. Pseudo-count loses on the easy training set [K05, contested].
- Ostrovski: MMC confound. The bonus is not the only cause of the 2016 gain [K04].
- RND Pitfall -3; NGU ablation says RND alone hurt Pitfall [a22, b08].
- Hash counts on CoT embeddings collapse [K09].
- Naive UCB on outcomes: raised training reward, not test pass@k, except one easy case [K15].
- MERCI: no gain on Minerva and MATH500; gain concentrated in AIME [K08].

**Moderators.**
- Base agent strength: bonuses help less under Rainbow than DQN [a19].
- Tuning target: all bonuses were tuned on Montezuma [a19, b25].
- Bonus scale: 1-2 orders larger gave the record runs [b04]; PixelCNN robust across 1-2 orders [a07].
- Difficulty: sequential revision wins on easy items, parallel or tree on hard [d06]. Benefit of representation-based selection grows with model strength [d17].
- Noise: filtering is required for MERCI [b17].
- Stochasticity: sticky actions make prediction error irreducible [b09].

**Interventions that worked.** Learned or task-relevant keys. Non-episodic intrinsic stream (RND). Inverse-dynamics features (ICM). Archive plus return (Go-Explore). External summary of history (bandits). Positive-only subsampled history (ICRL). Within-batch repetition penalty. Judge-labelled strategy clusters.

**Interventions that did not.** Pixel-level hash at high fineness. Dynamics-error bonus under noise. Hash on CoT embeddings. Naive outcome UCB. Raw-history prompts for bandits. Count bonuses applied where exploration is not the bottleneck. Revision without a selection step (flips about 38% of correct answers).

**Weak spots in the evidence.** Nearly all RL numbers are Atari with 5 seeds or fewer, tuned on the test game. Bellemare's 6,600 is one run. LLM evidence has tiny test sets (AIME25 has 30 problems). Files a, b, c overlap; independent counts refer to research groups.

## 6. Language models

**Plain LLMs as explorers.**
- GPT-3.5, GPT-4 and Llama2 as bandit agents over 32 prompt designs: only GPT-4 with chain-of-thought and an externally summarised history explored well. Basic GPT-4 showed suffix failure in over 60% of replicates (T=100, Bernoulli bandits) [c17]. They behave greedily; CoT on raw history did not fix it [c18].
- Newer models (GPT-5 family, Qwen-2.5, Gemma-3, Mistral-7B, an R1 distill): LLMs are worse than linear regression at exploiting even with summaries, but useful at proposing candidates in a large semantic action space (reward 0.5-0.6 at K=3-4 suggestions vs below 0.1 for random arms). Raw history degrades performance as tasks grow [d09].
- EVOLvE: UCB-style summary statistics in the prompt plus fine-tuning on optimal trajectories let smaller models beat larger ones [d10].
- In-context RL from reward works only with positive-only, randomly subsampled episodes: Banking77 6.2% to 72.2% [d11]. The authors tie naive failure to negative examples.

**Sampling as exploration.**
- Independent resampling has large coverage gains, log-linear in samples. But picking the right answer lags: MATH Llama-3-8B coverage 98.44% at 10,000 samples while vote or reward model stays near 41% [d01]. This is the baseline a history table must beat.
- RLVR shrinks coverage at large k [b21].

**Count-style rewards in LLM training.**
- MERCI: small, AIME-heavy [b16, b17].
- CDE: hash counts fail; perplexity bonus Qwen3-4B-Base average 48.2 to 50.6 [b18].
- Song: outcome counts need refinement; batch repetition penalty works [d03, d15].
- Hu: strategy-cluster inverse-size reward, AUC@64 AIME 0.131 to 0.160 (0.116 for SimpleRL) [d05].
- Tuyls: covariance bonus; RepExp 2.1-4.1x more sample-efficient than Unlikeliness and 3.2-13.4x than GRPO at pass@256, but slightly worse than Unlikeliness on AIME24 until k=64 [d04].
- Bai: pseudo-count online DPO, LC win rate +5.0 (Zephyr), +2.4 (Llama-3-8B); length growth hurt later [d08].
- Confound: Qwen-math RLVR gains appear even under random rewards (+21.4 vs +29.1) [d07].

**Inference-time structure.**
- Intelligent Go-Explore: Game of 24 100% vs ReAct and Reflexion lower; the per-state action history is key (33 +/- 9 without) [d02]. Equal operations, not tokens.
- Snell: sequential vs parallel depends on difficulty; naive revision flips about 38% of correct answers [d06, d18].
- Voyager: random curriculum cuts items by 93%, no self-verification by 73% [c21].
- DivSFT: conditioning on earlier attempts raised diversity (abstract only, after fine-tuning) [d12].

**What changed it, by how much.** The biggest measured lever for a frozen LLM is summary-in-code instead of raw history (bandit suffix failure dropping from over 60% to avoided in 3 GPT-4 configurations). Everything else is small or training-based.

## 7. What our agent should take

### Add now (established)

| Item | Schema part | Status | Evidence | Rule |
|---|---|---|---|---|
| Keep history as a code-built summary (counts per direction), not raw attempt text | S3 | [E] | K10; c17, d09, d10, d11 | Show the generator a short list of tried labels and counts. Do not paste whole failed attempts. |
| Key by meaning, not wording: operator plus approach label; exclude surface rewording | S3 | [E] | K03, K16; a12, b07, d05, d04 | Never key on exact text (always new) or a raw embedding hash (collapses). |
| Do not use a model's judgement of "interesting" as the final novelty test; novelty counts only if the attempt runs and differs in outcome | G8 | [E] | K12; b23, c19, c21 | Reinforces G8. |
| Switch off novelty pressure once a check passes (no "dancing with skulls") | G2, G6 | [E] | K06; a18, b09 | After a verified pass, freeze the answer and stop adding directions. |
| Do not bump novelty on noise: drop variation that does not change the outcome | S3 | [E] | K06; a15, b09, a21 | Count outcome-distinct attempts. |
| At impasse, prefer extending the best partial attempt kept in an archive over restart | S6 | [E] at the idea level (RL, 2 groups); text-task evidence single-source | K07; a23, a22, d02 | Archive keyed by the history table. Verify with the test in section 8 before relying on it. |
| Treat large-k coverage as a goal: spend part of the budget on distinct directions, because pushing only for the likeliest answer narrows coverage | G11, G12 | [E] | K11; b21, d01 | Supports "several short independent attempts". |

### Test first

| Item | Schema part | Status | Evidence | Why not yet |
|---|---|---|---|---|
| Add a 1/sqrt(n + 0.01) preference when choosing the next S3 direction | S3 | [S] | K01, K13; a03, d16 | No prompt-level test. Song argues a hard exclude of refuted outcomes may beat a discount. |
| Hard-exclude refuted outcomes instead of discounting | S3 | [S] | K15; d03, d16 | One paper, training setting. |
| LLM-labelled strategy key vs exact string vs embedding hash | S3 | [E] on direction, [S] on size | K16, K09 | Our own comparison missing. |
| Conditioning on earlier attempts ("be different") vs independent samples | S3 | [S] | K19; d12 | Abstract only, after fine-tuning. |
| Gate novelty by S0 difficulty class | G12 | [S] | K17; d06, d17 | Gate untested. |
| Long redundancy-penalised trace vs several short attempts | G11 | [S] | K14; b20 | Conflicts with G11 as written. |
| Tune any novelty term on one class, test on others | G7 | [C] | K05; a20, b11 | Taiga shows transfer fails. |
| Use a bonus together with a credit-assignment trick | G7 | [S] | K04; a08 | Ablate each. |
| Report per-benchmark, not average | G7 | [S] | K08; d13 | MERCI average hid null results. |

## 8. Concrete tests on our bench

All tests: both arms at equal total tokens, setup cost counted (G7), at least 3 seeds, report per item class.

| Test | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 History table vs independent resampling | Open problems with several valid answers or approaches (brainteasers, ARC-style) | A: independent samples. B: code table with 1/sqrt(n+0.01) preference, label shown to generator | Distinct correct answers / approaches found at k = 1, 8, 64 | B higher coverage at k=8+ by a few points; no loss at k=1. Based on K01, d01. |
| T2 Key granularity | Same set | Keys: exact string, operator+approach label, embedding hash | Duplicate-direction rate; collision rate; coverage | Label best; hash collision above 50% (cf. b18); string near-zero duplicates (always new). |
| T3 Summary vs raw history | Same set, plus a bandit-like pick-the-direction toy | A: raw attempts in prompt. B: code summary. | Coverage; repeated-direction rate | B better (K10); effect smaller on strong newer models (d09). |
| T4 Hard exclude vs discount | Items with a checker | A: 1/sqrt(n) discount on refuted outcomes. B: hard exclude. | Wasted attempts on refuted answers; final accuracy | B fewer repeats (d16). |
| T5 Difficulty gating | Mixed-difficulty set, S0 class | A: table always on. B: table only on hard classes. | Accuracy per difficulty bin; correct-to-wrong flips | B avoids loss on easy items (Taiga reversed trend, c13). |
| T6 Freeze after verified pass | Items with a held-out check (G3) | A: continue directions after pass. B: freeze | Rate of correct answer replaced by wrong | B lower flip rate (d18 38%). |
| T7 Archive return vs restart at S6 | Items where a first attempt is partly right | A: restart. B: extend best partial attempt | Solve rate on S6-reached items | B better (d02), unknown at equal tokens. |
| T8 Conditioned vs independent | Code or open problems | A: independent. B: sequential, "do something different from this list" | Edit-distance diversity of correct solutions; pass@k | B more diverse (d12, after fine-tuning only). |
| T9 Long vs short traces | Items where more directions exist | A: one long redundancy-penalised trace. B: several short attempts | Coverage at equal tokens | Expect B (G11); LIE may disagree. |
| T10 Per-benchmark MERCI-style check | Our 3+ task sets | Table on vs off | Per-set delta with CIs | Expect gain only where exploration is the bottleneck (a20, d13). |

## 9. What does not transfer, and why

- **Tabular guarantees (UCB, MBIE-EB).** They assume a finite state set and noisy rewards. A free-text direction has no natural state, and verified answers are deterministic, so refuted ones should be excluded, not discounted [d16]. Originals unopened.
- **Density-model pseudo-counts and RND.** They need training a model over states. Our agent cannot train. Only the idea of counts per key remains.
- **Atari numbers.** Pixel games, 50M-200M frames, tuned on Montezuma. No path from there to a text agent's score.
- **Training-signal LLM papers (MERCI, CDE, LIE, Hu, Tuyls, Song).** They change the policy's weights. Our agent cannot. We can borrow keys and rules, not results.
- **Qwen-math RLVR results.** Confounded by pre-training priors and spurious rewards [d07].
- **Hash counts on CoT embeddings.** Known to collapse [b18].
- **Noisy-TV and "dancing with skulls".** The analogue is wording variation as fake novelty. This is a warning, not a mechanism to copy.
- **Go-Explore's simulator restore.** Text reasoning has no cheap exact restore; an "archive" is a stored partial attempt that must be re-read (token cost).
- **Persistent bonus.** PixelCNN gain never fully vanishes, so the agent loops back for "sights" [a10]. For us a persistent bonus is a bug (G6).

## 10. Open questions

1. Does a prompt-level history table beat independent resampling at equal tokens? No paper tests it (gap 1).
2. What key granularity avoids both collapse and "everything is new" (gap 2)? Strategy cluster works in training papers; our version is untested.
3. Does a code summary beat raw history on open problems and with newer models (gap 3)? Evidence is bandits and classification.
4. Does the S0 gate decide per class when to switch the table on (gap 4)?
5. Is the MERCI gain real beyond AIME (gap 5)? No replication.
6. How best to stop novelty after a verified pass (gap 6)? Freeze plus hard exclusion is a rule from analogy.
7. Archive return vs restart at equal tokens (gap 7).
8. Long redundancy-penalised traces vs short independent attempts (gap 8).
9. How much of any gain is the bonus and how much a confound (MMC, length, entropy) (gap 9)?
10. What is the right notion of "state" for counts over reasoning (gap 10)? Kolter and Ng and Strehl and Littman remain unopened.

## 11. Sources

[V] opened, [M] snippet or abstract only.

- [V] Bellemare et al. 2016, Unifying count-based exploration and intrinsic motivation. https://arxiv.org/abs/1606.01868
- [V] Ostrovski et al. 2017, Count-based exploration with neural density models. https://arxiv.org/abs/1703.01310
- [V] Tang et al. 2017, #Exploration. https://arxiv.org/abs/1611.04717
- [M] Martin et al. 2017, Count-based exploration in feature space. https://arxiv.org/abs/1706.08090 (a13 opened, b15 abstract only)
- [V] Machado et al. 2018, Count-based exploration with the successor representation. https://arxiv.org/abs/1807.11622
- [V] Pathak et al. 2017, Curiosity-driven exploration by self-supervised prediction (ICM). https://arxiv.org/abs/1705.05363
- [V] Burda et al. 2019, Exploration by random network distillation. https://arxiv.org/abs/1810.12894
- [V] Burda et al. 2018, Large-scale study of curiosity-driven learning. https://arxiv.org/abs/1808.04355
- [V] Taiga et al. 2019/2020, On bonus-based exploration methods in the Arcade Learning Environment. https://arxiv.org/abs/1908.02388
- [V] Ecoffet et al. 2019/2021, Go-Explore. https://arxiv.org/abs/1901.10995
- [V] Badia et al. 2020, Never Give Up. https://arxiv.org/abs/2002.06038
- [V] Badia et al. 2020, Agent57. https://arxiv.org/abs/2003.13350
- [M] Strehl and Littman 2008, MBIE-EB. https://doi.org/10.1016/j.jcss.2007.08.009
- [M] Kolter and Ng 2009, Near-Bayesian exploration in polynomial time. https://doi.org/10.1145/1553374.1553441
- [M] Auer 2002 (UCB), as restated in Wang et al. 2026. https://arxiv.org/abs/2602.11748
- [V] Zhang et al. 2025, MERCI (Count Counts). https://arxiv.org/abs/2510.16614
- [V] Dai et al. 2025, CDE. https://arxiv.org/abs/2509.09675
- [V] Wang et al. 2026, Think longer to explore deeper (LIE). https://arxiv.org/abs/2602.11748
- [V] Yue et al. 2025, Does RL really incentivize reasoning capacity. https://arxiv.org/abs/2504.13837
- [V] Du et al. 2023, ELLM. https://arxiv.org/abs/2302.06692
- [M] Zhang, Lehman, Stanley, Clune 2024, OMNI. https://arxiv.org/abs/2306.01711 (abstract-level)
- [V] Wang et al. 2023, Voyager. https://arxiv.org/abs/2305.16291
- [M] Cheng et al. 2025, Entropy perspective on reasoning with exploration. https://arxiv.org/abs/2506.14758
- [M] Zhang et al. 2024, SELM. https://arxiv.org/abs/2405.19332
- [V] Krishnamurthy et al. 2024, Can LLMs explore in-context. https://arxiv.org/abs/2403.15371
- [V] Brown et al. 2024, Large Language Monkeys. https://arxiv.org/abs/2407.21787
- [V] Lu, Hu, Clune et al. 2025, Intelligent Go-Explore. https://arxiv.org/abs/2405.15143
- [V] Song, Kempe, Munos 2025, Outcome-based exploration for LLM reasoning. https://arxiv.org/abs/2509.06941
- [V] Tuyls et al. 2025, Representation-based exploration. https://arxiv.org/abs/2510.11686
- [V] Hu et al. 2026, Rewarding the Rare. https://arxiv.org/abs/2601.08763
- [V] Snell et al. 2024, Scaling LLM test-time compute optimally. https://arxiv.org/abs/2408.03314
- [V] Shao et al. 2026, Spurious Rewards. https://arxiv.org/abs/2506.10947
- [V] Bai et al. 2025, Online preference alignment with pseudo-counts. https://arxiv.org/abs/2501.12735
- [V] Harris and Slivkins 2026, Should you use your LLM to explore or exploit. https://arxiv.org/abs/2502.00225
- [V] Nie et al. 2025, EVOLvE. https://arxiv.org/abs/2410.06238
- [V] Monea et al. 2025, LLMs are in-context RL learners. https://arxiv.org/abs/2410.05362
- [M] Anonymous 2026, Don't Repeat Yourself (DivSFT), abstract and listing page. https://openreview.net/forum?id=XVDIPr7jqF
