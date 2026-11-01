# Bandit allocation: deep document

*Subfield C12.08. Schema link: G12 (spend by difficulty, search only where there is a foothold). Sources: evidence_a-d.jsonl (a01-a26, b01-b29, c01-c26, d01-d20), claims.jsonl (K01-K35), critique.md. Status marks: [E] established, [S] single-source, [C] contested.*

## 1. What it is

A bandit problem is a choice among options ("arms") when you do not know how good each one is and each trial gives a noisy reward. Every sample does two jobs. It earns something, and it teaches you something. The question is where the next sample goes.

For our agent the "arms" are not slot machines. They are candidate plans, hypotheses, drafts, operators (O1-O8), prompts, or whole problems competing for one token budget. The task text calls this "spending samples across options".

Four goals give four different answers. They must not be mixed.

| Goal | Right measure | Family of rules |
|---|---|---|
| Earn on every pull, known model per arm, discounting | Total discounted reward | Gittins index (exact optimum) |
| Earn on every pull, unknown model, no discounting | Cumulative regret | UCB, Thompson sampling |
| Only the final pick counts (our usual case) | Simple regret, or samples to reach confidence 1-delta | Uniform, successive halving, Track-and-Stop |
| Many problems share one budget | Total solved at fixed tokens | Difficulty-based allocation, bandit over queries |

In a reasoning scaffold, intermediate attempts earn nothing. Only the submitted answer counts. So the pure-exploration family (halving, best-arm identification) is the closer fit than UCB. This is the main structural point of the subfield (K02, a10, b17).

Related subfields run in parallel (links only, not covered here): Exploration and exploitation, Optimal stopping, Test-time compute scaling, Bandit-style exploration, Foraging and patch leaving, Retrieval as a bandit, Metareasoning and value of computation, Resource-rational analysis, Evidence accumulation, Hierarchical task networks.

## 2. History and theories in depth

**Thompson (1933, 1935).** Proposed choosing a treatment with probability equal to the chance it is best, for clinical trials. Largely ignored, then revived by Scott (2010) and Chapelle and Li (2011). [M, via a09/Russo 2018]

**Robbins (1952).** Formulated the modern multi-armed bandit. [M, via a04]

**Gittins (1979), Gittins and Jones.** For independent arms, geometric discount beta < 1, and only the played arm changing state, the optimal policy is an index policy: compute an index for each arm from its own state alone, play the highest. The index is the sup over stopping times tau of expected discounted reward divided by expected discounted time. Weitzman reached the same result in economics in 1979 (a01). Whittle (1980) recast it as a retirement problem: the index is the fixed payoff at which you are indifferent between continuing the arm and retiring to a sure reward (a02). That view maps onto a stop rule: keep sampling a branch while its value beats a sure fallback answer. Weber (1992) gave a short proof. Exact algorithms: Varaiya 1985, Chen-Katehakis 1986, Katehakis-Veinott 1987, Sonin 2008, Nino-Mora 2007 (a03, b28). If arms evolve when not played (restless bandits) the index is only a heuristic, and exact solution is generally intractable (a03, b29). All Gittins facts here come from Wikipedia and secondary sources; the original papers were not opened (a26, c25).

**Lai and Robbins (1985).** Regret must grow at least logarithmically in the number of plays: each suboptimal arm j is pulled at most (1/D(p_j||p*) + o(1)) ln n times for the best policies (a05). [M]

**Auer, Cesa-Bianchi, Fischer (2002).** UCB1 plays the arm with the highest (empirical mean + sqrt(2 ln n / n_j)). Regret after any n plays is at most the sum over suboptimal arms of 8 ln n / Delta_i, plus (1 + pi^2/3) times the sum of the gaps, for any rewards in [0,1]. This gives logarithmic regret uniformly in time, not just asymptotically (a05, a06, b14). In experiments on 7 Bernoulli settings (2 arms and 10 arms, 100,000 plays, 100 runs), UCB1-Tuned usually matched a well-tuned epsilon-greedy and was far less sensitive to tuning. Epsilon-greedy degrades fast if mis-tuned and loses when many arms are clearly bad. UCB2 was always slightly worse than UCB1-Tuned (a07).

**Agrawal and Goyal (2012).** First proof that Thompson sampling has logarithmic expected regret: two arms O(ln T / Delta + 1/Delta^3); N arms O((sum 1/Delta_i^2)^2 ln T) (a08, b15). Russo et al. (2018) tutorial: greedy never retries an arm wrongly rated low; epsilon-greedy wastes pulls on arms that are clearly bad; posterior sampling writes off bad arms naturally (a09, b16).

**Bubeck, Munos, Stoltz (2011).** Pure exploration. If only the final recommendation matters, the best strategy changes. For K >= 3 Bernoulli arms, any strategy with cumulative regret bounded by C f(n) has simple regret at least e^{-D f(n)} for some ordering. UCB-like play gives only polynomial decay of simple regret. Uniform allocation gives exponential decay (a10, b17).

**Garivier and Kaufmann (2016).** Exact lower bound on samples for fixed-confidence best-arm identification, and Track-and-Stop, which matches it. It samples arms in the optimal proportions and stops by a Chernoff likelihood-ratio rule (a11).

**Hyperband and successive halving (Li et al. 2018).** Hyperparameter search as infinite-armed pure exploration. Successive halving runs many configurations on a small budget, keeps the best 1/eta, repeats. Hyperband runs several brackets because nobody knows how early performance predicts final performance (a12, a13, b18).

**Psychology.** Wilson et al. (2014) horizon task: with more free choices left, people pick the less-known option more (directed exploration) and choose more noisily (random exploration) [M, via c26]. Gershman (2018) re-analysed these data and ran two new experiments; a hybrid of a UCB-like bonus and Thompson-like noise fits best (b24, b25).

**LLM era (2022-2026).** The question changed from "what is the best rule" to "can a language model run one in context, and which scaffold helps". Section 6 covers this. A parallel line treats test-time compute itself as a bandit allocation: over queries (Damani, Snell, Zuo and Zhu), over samples (Large Language Monkeys, stop rules), over candidate programs (REx) and over prompts (TRIPLE).

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Gittins index policy is optimal for independent, discounted arms | Index = sup over tau of discounted reward / discounted time; only a heuristic for restless arms | a01-a03, b28-b29 (secondary only) | [E] (K01) |
| Cumulative-regret-optimal rules have log regret | UCB1 bound 8 ln n / Delta per arm; TS O(ln T / Delta + 1/Delta^3) for 2 arms | a05, a06, a08 | [E] |
| Low cumulative regret forces slow simple regret | Polynomial vs exponential decay of simple regret | a10, b17 | [E] (K02) |
| Track-and-Stop needs about half the draws of KL-LUCB | Arms 0.5/0.45/0.43/0.4: 3968 (BC), 4052 (D-Tracking), 4516 Chernoff-Racing, 8437 KL-LUCB, 9590 KL-Racing. Arms 0.3/0.21/0.2/0.19/0.18: 1370, 1406, 3078, 2716, 3334. delta=0.1, 3000 runs | a11 | [S] (K03) |
| Successive halving / Hyperband big speedup, can lose | 6x to 70x vs random search, over 10x vs Bayesian optimisation, overhead under 5%; on SVHN SMAC with early stopping beat Hyperband; most exploratory bracket nearly best | a12, a13, d18 | [S] (K04, K30) |
| GPT-4 raw-history bandit: suffix failure | 72 GPT-4 configs, 1 (BSSC0) succeeded; 0 of 48 GPT-3.5 and 0 of 32 Llama2 configs; basic prompt suffix failure over 60% at T=500, N=20; SuffFailFreq(T/2): basic 0.50, Greedy 0.48, UCB 0.02, TS 0.01 | a14, a15, b01, b02, c01-c03 | [S] (K05) |
| External per-arm stats raise exploration | MAB win rate, raw vs algorithm-guided: Gemma-2B 7.6 vs 4.9, 9B 10.5 vs 4.1, Flash 27.7 vs 32.2, Pro 45.5 vs 59.6; UCB 90.6. Contextual: Flash 0.0 vs 46.4, Pro 7.1 vs 64.3; LinUCB 96.4. 30 runs per setup | a16, b03, c05, c06 | [E] (K06) |
| Fine-tuning on UCB traces vs few-shot | Fine-tuned Flash 65.6 (trained on hard; 54.5 on easy). Few-shot guided Flash 50.2, Pro 56.4; few-shot raw Flash 27.5, Pro 39.1 (hurt Pro). Fine-tune with raw history 65.6 vs summarised 28.3 | a17, b04, c07 | [S] (K07) |
| Weak models stay linear regret | Gemma-2B/9B linear; Pro with support near sublinear. Explore fraction under summarised history: Flash 11.3% to 1.1%, Pro 79.0% to 10.5%, Gemma-9B 6.9% to 16.5% | a18, b05, c08 | [S] (K08) |
| LLMs are greedy; knowing-doing gap | Gemma2, 10 arms, 50 steps: coverage 40% (2B), 65% (9B, 27B); no CoT 25%; 20 arms 45%. Right rationale 87%, greedy action in 64% of those | b09, d04 | [E] (K09) |
| Untried-action bonus raises coverage | +1 for untried arm in RL fine-tuning: coverage 50% to 70%; try-all first pass was the largest gain of 7 mechanisms | b10, d04 | [S] (K10) |
| GPT-3 on horizon task | Regret 2.72 (SD 5.98) vs humans 3.24 (SD 10.26), t(38878) = -5.03; short horizon no difference (p=.97); no directed exploration, horizon x reward-diff beta=-0.02, p=.14 | a19, b11, c09 | [S] (K11) |
| Meta-in-context learning | 500 sims; in-context beta=-0.221 (SE 0.012), t=-35.8; meta effect beta=-0.031, t=-5.0; matched Greedy after 4 tasks, slightly behind UCB | a20, b12, c11 | [S] (K12) |
| Optimism bias in two-option learning | Higher learning rate for better-than-expected outcomes on chosen option; flips with counterfactual feedback; vanishes if told another agent samples | b13, c12 | [S] (K13) |
| Adversarial online learning | Sublinear regret often (GPT-4o at T=500); GPT-4 and GPT-4 Turbo fail noisy alternating and adaptive losses (trend stat 1.0 and 0.97-1.0, linear not rejected, 20 runs); raw vs summary p=1.2e-157 | a21, b06, b07, c24, d06 | [S] (K14); summary question [C] (K15) |
| Reasoning models explore better in open search | Little Alchemy 2, 500 trials, elements found: o1 177, R1 85, humans 42 (29,493 players, 4,691,033 trials), GPT-4o 35, Llama-70B 25, 8B 9. o1 vs humans t=9.71. Reminder prompt: no gain (43, p=.304); temperature +0.124 (z=5.06) | c13, c14 | [S] (K16) |
| Thinking budget raises directed exploration | o3-mini high and Gemini-2.5-flash budget; humans N=45 stationary, N=31 non-stationary; all LLMs still worse directed exploration in drifting 4-arm task | d01 | [S] (K24, K32) |
| Reasoning models solve the exploit step | GPT-5-mini perfect on highest-mean-arm puzzle; GPT-3.5 and GPT-4 fail; LLMs still lose to linear regression on contextual tasks | d02 | [S] (K26) |
| Scaffolded posterior sampling | Separate calls for update, sample, act: better regret curve than classic TS at temperature 1.2 (K=5, T=100); R1 swap did not beat it | d03 | [S] (K25) |
| Coverage grows log-linearly with samples | SWE-bench Lite 15.9% to 56% at 250 samples (single-attempt SOTA 43%); Gemma-2B CodeContests 0.02% to 7.1% at 10,000; MATH Llama-3-8B 82.9% at 100 to 98.44% at 10,000, but vote/reward model 40.50% to 41.41% | a22, b19 (b19 error corrected), c17 | [E] (K17) |
| Difficulty-based allocation beats uniform | Snell: about 4x less compute than best-of-N, 14x larger model beaten where small model has non-trivial success, level 5 no progress. Damani: up to 50% less compute (code/math), up to +10% quality, chat 0-10% (25-40% tranches), routing 25-40% calls saved, predictor accuracy 72-84%. Zuo and Zhu (up-to numbers): +11.10 MATH-500, +10.82 AIME25, +11.23 LiveCodeBench; Llama-3.2-1B +2.50 at budget 16 | a23, a24, b20-b22, c15, c16 | [E] (K18) |
| About half of coding problems have zero success | 50% coding, 5% math | a24, b21, d16 | [S] (K20) |
| Adaptive stopping saves samples | Adaptive-Consistency up to 7.9x fewer, under 0.1% drop (17 datasets, 3 LLMs). ESC cuts: MATH 33.8%, GSM8K 80.1%, StrategyQA 76.8%, CommonsenseQA 78.5%, Coin Flip 84.2%, Last Letters 67.4%; GPT-3.5 MATH 59.98 vs 60.32. Manvi: 1.2 samples capture 74% of 16-sample gain, 1.9 capture 84%, 75% pruned, 56% tokens saved | c18, c19, b23, d12, d17 | [E] (K19); hard-set caveat (K34) [S] |
| Early partial reasoning predicts final answer partly | Probe 65% at 10% of a chunk, 79% peak (peak minus 14, 10, 5 points at 10%, 50%, 95%); AUROC over 0.9 on AIME; ST-BoN same accuracy at 20-30% cost; Certaindex up to 50% compute saved | d08, d09, d11 | [E] (K29) |
| Confidence cutting can lose | DeepConf online up to 84.7% tokens saved (AIME25 GPT-OSS-120B, 91.8 pass@1, 97.0 vote, 99.9 DeepConf@512); loss at aggressive 10% filter from confident wrong traces | d10 | [S] (K30) |
| Bandit over prompts / branches / programs | TRIPLE halving beat uniform by 15% and UCB by 5-6% at budget 150; LATS HumanEval 92.7 (GPT-4), 83.8 (GPT-3.5, vs Reflexion 68.1, CoT 46.9); REx 1.5x-5x fewer calls, none on APPS Introductory | c20, c21, d19 | [E] (K21); REx [S] (K33) |
| Humans use hybrid directed plus random exploration | Hybrid protected exceedance 0.999; Exp 1 N=44, Exp 2 N=45; older adults 51 vs young 32, about 26% avoid information | b24-b27 | [E] (K22) |
| Verbal confidence is a poor allocation input | Verbalised values 80-100%; reasoning models better calibrated in 33 of 36 settings; hopeless-option overestimates attract budget | d13-d16 | [E] (K28) |
| Non-stationary fix on the bandit side | ParetoBandit: geometric forgetting on per-arm statistics; budget within 0.4% of ceiling; up to +0.071 quality lift; new model integrated in 142 steps | d07 | [S] (K32) |
| No LLM Gittins or Whittle test exists | arXiv searches returned zero relevant hits | d20 | [S] (K31) |

Corrections from the cross-check (critique.md): b19 wrongly says 82.9% is "at 1 sample" (it is at 100 samples). "32 prompt designs" is the design grid; 72 is the GPT-4 configuration count. Zuo and Zhu numbers are best-case ("up to"). The T=500 ">60% suffix failure" and the T/2 table value 0.50 are different measures.

## 4. Mechanisms and models

Each item below is written so it can be coded.

**4.1 Per-arm bookkeeping (needed by every method).** Keep, outside the model, for each option i: n_i (attempts), s_i (successes or summed reward), and a check result. For binary outcomes use Beta counts: alpha_i = 1 + s_i, beta_i = 1 + n_i - s_i. Code writes these into the prompt as a short table. Raw transcripts do not substitute (K06; K15 caveat).

**4.2 UCB1.** Score_i = mean_i + sqrt(2 ln N / n_i), N = total pulls. Pull every arm once first (n_i = 0 means infinite score). Play argmax. Use when pulls earn and the horizon is long. UCB1-Tuned replaces the bonus with sqrt((ln N / n_i) * min(1/4, V_i)), where V_i is a variance upper bound (a07).

**4.3 Thompson sampling.** For each arm draw theta_i ~ Beta(alpha_i, beta_i). Play argmax theta_i. Update the counts. Done in code, the draw is cheap. Done by an LLM with separate calls for update, sample, act, it also worked (d03): the model wrote Beta(1,1) in words and kept success and failure counts; this beat TS at temperature 1.2 on K=5, T=100.

**4.4 Epsilon-greedy.** Pull best mean with probability 1-eps, a random arm otherwise. Simple but sensitive to eps and wasteful when many arms are bad (a07). Not recommended.

**4.5 Successive halving (fixed budget B, n arms, eta=2).** Rounds r = 1..ceil(log2 n). Give each surviving arm floor(B / (|S_r| * rounds)) units. Rank by observed score. Keep the top |S_r|/eta. Return the last survivor. This is the pure-exploration baseline for candidate selection. TRIPLE used it for prompts (c21). Hyperband runs several brackets with different n versus budget-per-arm trade-offs, to hedge against early scores not predicting final scores (a12, a13). With R=81, eta=3 there are 5 brackets. Keep one bracket with many starts and little cutting (d18: the most exploratory bracket was nearly best).

**4.6 Track-and-Stop (fixed confidence).** Maintain empirical means. At each step sample the arm that moves the empirical allocation toward the optimal proportions w*(mu). Stop when the generalized likelihood-ratio statistic exceeds a threshold beta(t, delta). Roughly half the draws of KL-LUCB on the paper's instances (a11). Heavy to implement. The simple version for an agent is sequential testing: stop when the lead of the top answer over the second is large enough (Adaptive-Consistency uses a Dirichlet test, c18).

**4.7 Gittins index (discounted, known priors).** For a Bernoulli arm with Beta(a, b) state and discount beta, the index is a function G(a, b, beta) computed offline by dynamic programming over the retirement problem: find the smallest retirement reward k such that continuing and retiring are equal in value (Whittle, a02). Precompute a table for a, b up to some cap and beta around 0.9 to 0.99. Play argmax G. This is a lookup, so the cost per decision is zero tokens. No LLM test exists (d20).

**4.8 Difficulty-aware allocation over queries (Damani).** Train a probe on hidden states to predict, per query, the success probability curve p_i(k) for k samples. Allocate greedily: give the next sample to the query with the largest marginal gain p_i(k+1) - p_i(k). Marginal gains are diminishing, so greedy is optimal (matroid). Route queries with predicted zero success to "I don't know" and free their samples (a24, d16). Zuo and Zhu learn difficulty online and prefer solvable hard queries over unsolvable ones (b22). Black-box version for us: use early agreement among a few cheap attempts as the difficulty signal.

**4.9 Early exit and pruning.** Every k tokens, ask for the current answer. Stop when the last m intermediate answers agree (Certaindex, d11) or when a consistency check passes (ST-BoN, d09). In repeated sampling, stop when the leader is safe (c18) or when a window of answers is unanimous (ESC, c19; window 8, cap 64).

**4.10 Posterior sampling over programs (REx).** Treat each candidate program as an arm. Reward is the verifier score. Thompson-sample which program to refine next. Broad search first, then deep refinement on promising ones. Needs a verifier (d19).

**4.11 Forgetting for drift.** Replace counts by discounted counts: alpha_i <- gamma * alpha_i + reward, beta_i <- gamma * beta_i + (1 - reward), gamma around 0.9 to 0.99. Used on per-arm statistics in ParetoBandit (d07). A hypothesis for our agent, not measured.

**4.12 Forced exploration rule.** Before committing, require every option to have at least one attempt (UCB's try-all). An alternative is a +1 bonus for untried options (b10, d04). A prompt-level alternative is to randomly subsample which past episodes enter the prompt (Stochastic ICRL, d05).

## 5. What holds up

**Replicated or multi-source.**
- Log regret for UCB and TS, and the cumulative versus simple regret trade-off: theorems plus experiments (a05-a10) [E].
- LLMs under-explore from raw history: Krishnamurthy (GPT-3.5, GPT-4, Llama2), EVOLvE (Gemma, Gemini), Schmied (Gemma2), Binz and Schulz (GPT-3, no directed exploration). Four independent groups, different models and tasks [E] for the weak-model claim.
- External statistics help: Krishnamurthy and EVOLvE agree, and Harris and Slivkins (d02) explain part of it: weak models cannot even do the exploit step from raw history [E].
- Coverage grows with samples; selection is the bottleneck: Large Language Monkeys plus later test-time-compute papers [E].
- Difficulty-aware allocation beats uniform: Snell, Damani, Zuo and Zhu, three groups [E]. Common boundary: no gain at the hardest level, little gain on easy items or small budgets (below budget 8 in Damani).
- Adaptive stopping saves samples at small accuracy cost: four sources [E].

**Failures and boundary conditions.**
- Hyperband loses on SVHN to SMAC with early stopping (a12, d18). Early rank does not always predict final rank.
- DeepConf's aggressive 10% filter lost accuracy because wrong traces can be confident (d10).
- ESC saves 80.1% on GSM8K but only 33.8% on MATH. Savings shrink where problems are hard (d17).
- REx gave no gain on APPS Introductory (easy) (d19). Snell: beam search got worse as budget rose on easy questions (verifier exploited); at level 5 no method progressed (a23).
- Majority vote and reward models did not turn coverage into accuracy on MATH (40.50 to 41.41) (a22).
- GPT-4 fails noisy alternating and adaptive-loss sequences (b06, d06). Adversarial or drifting payoffs remain unsolved by prompting alone (K32).
- Few-shot demonstrations of good allocation hurt the strongest model in EVOLvE (Pro 39.1 vs 45.5 on raw history). The cause (demo difficulty or format) is not separated (critique gap 10).
- A prompt reminding the model to vary gave no gain on Little Alchemy 2 (c14). Higher temperature gave a small one.

**Contested.** Whether summarised history is the key. Krishnamurthy says yes on stochastic bandits. Park et al. found raw versus summarised input changed regret (p = 1.2e-157) in online learning but say the settings differ, and on the switch-at-c sequence raw history beat summaries (d06). Status [C] (K15).

**Interventions that worked.**
- Tool-computed per-arm means and counts in the prompt (EVOLvE Pro MAB 45.5 to 59.6; contextual 7.1 to 64.3).
- Hint plus summary plus chain of thought plus temperature 0 (the single GPT-4 success).
- Splitting allocation into update, sample, act steps (d03).
- Fine-tuning on UCB trajectories, and an untried-action bonus during RL fine-tuning (not available to a scaffold).
- Thinking budget: more thinking raised directed exploration (d01); o1 explored far more than humans in open search (c13).
- Random subsampling of context episodes (Qwen2.5-7B 6.2% to 72.2%, d05).

**Interventions that did not work.** Chain of thought alone on raw history (c04). Reminder prompts (c14). Few-shot hard demos (43.0 vs 50.2 for easy). Verbalised confidence as a signal (d13). Majority vote as a coverage converter (a22).

**Moderators.** Model size (2B and 9B stay linear regret). Task type (contextual bandits are far worse than MAB on raw history). Reasoning training (better calibration, better exploration). Age in humans (older adults explore less; Phelps et al. attribute it to a higher decision threshold, b27). Verifier quality. Horizon length: suffix failure is hidden at T=100 by lucky replicates and shows at T=500 (c02).

**Evidence quality notes.** Most LLM bandit studies use 2023-2024 models. Replicate counts are small (N=10 to 40). No confidence intervals in several tables. EVOLvE win rates are pairwise and depend on the comparison set. Phelps 2025 sample sizes were not recorded.

## 6. Language models

**6.1 Bandits in context.**
- Krishnamurthy et al. (2024): GPT-4 with a basic prompt shows suffix failure in over 60% of replicates at T=500, at the level of Greedy (0.48 vs 0.50 at T/2). Only BSSC0 worked. Two failure types: suffix failure (best arm never pulled again) and uniform-like failure (all arms spread evenly). Behaviour is bimodal: some replicates lock on the best arm quickly, many rarely pull it (a15). Llama2 is worse than GPT-3.5, which is worse than GPT-4.
- EVOLvE (2025): 16 MAB tasks and 2 contextual tasks in natural language. Flash 27.7 and Pro 45.5 on raw history, 32.2 and 59.6 with algorithm guidance, against UCB at 90.6. Contextual: raw history is nearly useless (0.0 and 7.1), guidance gives 46.4 and 64.3, LinUCB 96.4.
- Binz and Schulz (2023) on GPT-3: it looked good by regret (2.72 vs 3.24 human) but did not do directed exploration and ignored the horizon. Good regret on an easy task hides a missing strategy.
- Harris and Slivkins (2026): GPT-5-mini is perfect at the exploit puzzle; GPT-3.5 and GPT-4 are not. The weak link is the decision to explore. LLMs still lose to linear regression on contextual tasks (d02).
- Arumugam and Griffiths (ICLR 2026): scaffolding posterior sampling in separate calls beat prompt-only agents, and swapping in R1 did not beat the scaffold. Explicit allocation steps matter more than raw thinking tokens (d03).
- Schmied et al. (2025): greediness, frequency bias and a knowing-doing gap (87% right rationale, 64% greedy action in those cases).
- Monea et al. (2025): in-context RL in contextual bandits needs forced exploration; random subsampling of episodes fixed it.
- Coda-Forno et al. (2023): earlier tasks in context improve later ones; GPT-3 reached Greedy after 4 tasks.
- Schubert et al. (2024): optimism bias in updating.

**6.2 What changed behaviour, by how much.**

| Lever | Effect | Where |
|---|---|---|
| External summary or UCB stats | Pro 45.5 to 59.6 (MAB); contextual 7.1 to 64.3 | EVOLvE |
| Hint + summary + CoT + T=0 | 1 of 72 configs fixes suffix failure | Krishnamurthy |
| Chain of thought | Coverage 25% to 40-65% | Schmied |
| Thinking budget / reasoning model | o1 177 vs GPT-4o 35 elements; o3-mini high above human directed exploration | Pan et al.; Zhang et al. |
| Scaffolded posterior sampling | Beat prompt-only agents and R1 | Arumugam and Griffiths |
| Fine-tune on UCB traces | Flash 27.7 to 65.6 | EVOLvE |
| Untried-action bonus (RL) | Coverage 50% to 70% | Schmied |
| Reminder prompt | None (43, p=.304) | Pan et al. |
| Few-shot demos | Helps small, hurts Pro | EVOLvE |

Pan et al. also found with sparse autoencoders that uncertainty and choice are encoded in early blocks and empowerment later, so non-reasoning models commit before the value signal is ready (c14). That is a mechanistic reason why thinking helps.

**6.3 Test-time compute as allocation.** This is where allocation is measured with real accuracy numbers.
- Over samples for one query: Large Language Monkeys (coverage), Adaptive-Consistency (7.9x), ESC (34% to 84%), Manvi et al. (74% of the 16-sample gain at 1.2 samples), ST-BoN (70-80% saving), Certaindex (up to 50% compute; 34% on AIME and 53% on MATH500 for the top-10% problems), DeepConf (up to 84.7% tokens).
- Over queries: Snell (4x), Damani (up to 50%), Zuo and Zhu (up to +11 points).
- Over programs and prompts: REx, TRIPLE, LATS.
Caveat: these allocate across queries or samples. Mapping them to one agent's internal options (hypotheses, plans) is an inference, not measured (critique).

**6.4 Reasoning-model status.** Almost all bandit-specific results are on 2023-2024 models. Reasoning models do better (d01, d02, c13), but no study re-runs the Krishnamurthy hard instance with o-series, R1, Claude or Gemini 2.5, and the thinking budget at which suffix failure vanishes is unmeasured (K24). "LLMs do not explore" may be stale for current models.

**6.5 Gittins and Whittle.** No LLM study uses either (d20). Non-stationary LLM-routing work uses forgetting UCB or Thompson (d07).

**6.6 Calibration limits.** Allocators that need the model's own success estimate inherit its overconfidence: verbalised confidence sits at 80-100% (d13, older models). Reasoning models are strictly better calibrated in 33 of 36 settings (d14). Learned P(IK) works (d15). Damani's predictor is a probe on hidden states, not a stated estimate, and a wrongly low estimate sends budget to hopeless options (d16).

## 7. What our agent should take

### Add now (established)

| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| A1 | Keep per-option statistics in code (attempts, passes, check result per candidate plan, hypothesis or operator) and show a short table, not the transcript, when the model must choose among options | G12, memory (class record), S6 | [E] | K06; a14, a16, b03, c04-c06 |
| A2 | Treat selection of the final answer as pure exploration (spread effort, cut losers), not as cumulative-regret play. Do not use UCB-style "pull the current best" for picking a final answer | G12, S3/S7 | [E] | K02; a10, b17, a25 |
| A3 | Allocate by difficulty, per problem: estimate the pass rate from a few cheap attempts and spend more only where there is a non-trivial success rate; do not spend on hopeless items. (G12 already says this; this adds the mechanism and the boundaries: no gain at the hardest level, little on easy items, little below budget 8) | G12, S0 | [E] | K18; a23, a24, b20-b22, c15, c16 |
| A4 | Add a stop rule to repeated sampling: stop when the lead is safe (Adaptive-Consistency) or a window is unanimous (ESC). Expect savings of about 34% on hard sets and 80% on easy ones, with accuracy changing by about 0.1-0.3 points | G12, S3/S7 | [E] | K19; c18, c19, b23, d12, d17 |
| A5 | Add a code-enforced coverage rule: every option in a compared set gets at least one attempt before any is dropped or promoted (try-all first). S3 already assigns untried directions in open mode; extend it to checked mode when comparing options | S3, S6 | [E] for the failure (greedy lock-in); the prompt-form fix is [S] | K09, K10; b09, b10, d04 |
| A6 | Do not rely on the model's verbal confidence or stated success probability to allocate or stop; use observed counts and agreement (consistent with section 4b) | G12, G4 | [E] | K28; d13-d16 |
| A7 | Do not add few-shot demonstrations of "good allocation" to the prompt without a test (they hurt the strongest model) | G7 | [E] as a warning (single paper, K07 [S]) | a17, b04, c07 |
| A8 | Coverage is not accuracy: more samples pay only if a verifier or executable check picks the winner. Where no check exists, extra draws buy almost nothing (vote 40.50 to 41.41) | G12, G3, G5, S7 | [E] | K17; a22, c17 |

### Test first

| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| T1 | Successive halving over candidate plans or drafts (cut the worst half after a short partial run) versus uniform best-of-N at equal tokens | G12, S3, S4, new O-prune | [S] | K04, K21, K30, K33; a12, c21, d18, d19 |
| T2 | Early-answer probing every k tokens, cutting only when the answer is stable (Certaindex-style) | G11, G12, S3 | [S] | K29, K30; d08-d11 |
| T3 | Give-up rule for items with low early agreement, kept next to the stop rule | G6 (never abstain), G12 | [S] | K20, K34; a24, d16, d17 |
| T4 | Thompson-style update, sample, act in separate steps for choosing which operator or plan to expand next (S6) | S6, O1-O8 | [S] | K25; d03 |
| T5 | Decayed per-option tallies when payoffs can change (a plan that works then breaks) | S5, S6, memory | [S] | K32; d06, d07 |
| T6 | Prompt-only "try each once" rule on a frontier or reasoning model | S3 | [S] | K27; d04, d05 |
| T7 | Gittins index lookup for budget over problems or branches with switching cost or discounting | G12 | [S], no LLM evidence | K01, K31; d20 |
| T8 | Suffix-failure check on current models with raw history versus tool tally | G12 | [S] | K05, K24; c01, d01 |
| T9 | Bonus-plus-noise policy (UCB-style bonus with Thompson-style noise) for direction choice in open mode | S3 open mode | [E] in humans, untested in LLM scaffolds | K22; b24, b25 |
| T10 | Earlier-problem outcomes in context (meta-in-context) as class memory | memory | [S] | K12; a20, b12 |

## 8. Concrete tests on our bench

All arms get the same total token budget, including bookkeeping, probes and setup (G7). Effects are guesses from the cited studies, not promises.

| Test | Item type | Arms (equal tokens) | Metric | Expected effect |
|---|---|---|---|---|
| B1 Halving vs uniform | Items with an executable check (ARC-like programs, code with hidden tests, verifiable BrainTeaser answers) | (a) N uniform full attempts, pick by check; (b) successive halving: 2N short attempts, cut half after k tokens, continue; (c) difficulty-routed flat budget | Solve rate at fixed tokens; rank correlation of early vs final correctness | (b) beats (a) by a few points where early pass rate predicts final; ties or loses where it does not (the SVHN case). TRIPLE reports +15% over uniform at small budgets |
| B2 Difficulty routing | Mixed-difficulty set, 5 bins by plain pass@1 | (a) flat budget per item; (b) 3 cheap probes, then allocate the remaining tokens by estimated marginal gain; (c) as (b) with a give-up rule | Total solved; tokens per solve | (b) saves 25-50% tokens at the same solve rate (Damani, Snell); no gain in bin 5 and bin 1 |
| B3 Stop rule | Single exact-answer items, no check | (a) fixed N=16 self-consistency; (b) Adaptive-Consistency stop; (c) ESC window stop (window 8) | Accuracy per token | (b), (c) save 30-80% of tokens at a loss below 0.5 points; smaller savings on the hardest bin |
| B4 Tally vs transcript | Selection among 5 candidate operators with hidden pass-rate gap 0.2 | (a) raw outcome history; (b) code-kept tally table; (c) model-written tally | Suffix-failure rate at T/2; final regret; tokens | (b) lowest suffix failure; (c) in between; (a) near Greedy (0.5) on non-reasoning models, smaller gap on reasoning models |
| B5 Try-each-once | Same selection task | (a) no rule; (b) code-enforced try-each-once; (c) prompt-only rule | Arm coverage; final accuracy | (b), (c) raise coverage; accuracy neutral or better. Reject if accuracy falls more than 1 point |
| B6 Early-answer probe | Reasoning-model items with long traces | (a) full trace; (b) probe every k tokens, cut on stable answer; (c) aggressive confidence cut | Accuracy per token; false-cut rate | (b) saves 10-30% tokens with no drop; (c) loses on items with confident wrong traces |
| B7 Thompson scaffold | Operator selection in S6 | (a) model picks next operator freely; (b) code Beta counts, sample, act | Solved subgoals per token | (b) better when the class record has data; no gain on cold start |
| B8 Drift test | Option payoffs flip at a hidden time | (a) cumulative tally; (b) decayed tally (gamma 0.9); (c) raw recent history | Regret after the switch; detection delay | (b) fastest recovery; (a) fails to adapt; (c) mixed (GPT-4 handled switch-at-c from raw history) |
| B9 Few-shot allocation demos | As B4 | (a) none; (b) 2 easy demos; (c) 2 hard demos | Final regret | (b), (c) may hurt a strong model; expected a warning, not an improvement |
| B10 Gittins lookup | Budget over 8 problems with discounting | (a) round robin; (b) greedy by mean; (c) UCB; (d) Gittins table | Total discounted solves | (d) within a few percent of (c); wins when switching is costly |

## 9. What does not transfer, and why

- **Cumulative regret optimality (UCB, Thompson, Lai-Robbins).** Intermediate attempts earn nothing here. Only the final answer counts. Cumulative-optimal play gives only polynomial decay of simple regret (a10).
- **Gittins optimality.** It needs independent arms, a known model per arm, geometric discounting, and arms that do not change when idle. Candidate plans in one reasoning run share context and are not independent (G4). Plans that rot or improve with idle time make the problem restless. There is no LLM evidence (d20).
- **Asymptotic regret rates.** Our horizons are 5 to 50 pulls, not thousands. Constants and priors dominate. Auer's 8 ln n / Delta bound is loose at that scale.
- **Fine-tuning on UCB traces, RL exploration bonuses, trained regret-loss, algorithm distillation, supervised pretraining.** All need training. Ours is a training-free scaffold (K07, K23).
- **Human directed versus random exploration findings.** They describe people. They inform policy design (bonus plus noise, K22) but do not show an LLM has either.
- **Test-time compute results across queries.** They allocate over problems or samples, not over internal hypotheses of one chain. The mapping is an inference (critique).
- **Probes on hidden states (Damani, Zhang et al., ST-BoN).** Need white-box access. Black-box analogues (early answer agreement) are different and untested.
- **Verifier-based gains (REx, TRIPLE, LATS, Large Language Monkeys on code).** Depend on an executable check. Where none exists, the gains vanish (vote 40.50 to 41.41).
- **Old-model failure rates.** GPT-3, GPT-3.5, GPT-4 (2023), Llama2 and Gemma-2 numbers may not hold for reasoning models.
- **Self-stated priors.** Stated success probabilities are overconfident (d13), so allocators that take them as input do not transfer without observed counts.

## 10. Open questions

1. Do current reasoning models still show suffix failure on the Krishnamurthy hard bandit with raw history, and at what thinking budget does it vanish? (K24)
2. At equal tokens, does successive halving over candidate solutions beat uniform best-of-N and difficulty routing when the verifier is weak or absent? (K33)
3. How well does early partial reasoning predict final correctness for black-box models (rank correlation after k tokens)? (K29, K30)
4. Does a Gittins or Whittle index help an LLM agent anywhere, for example with switching costs or token discounting? No measurement exists. (K31)
5. Does a prompt-only try-each-once rule keep accuracy on frontier models? (K27)
6. What scaffold-only fix handles non-stationary or adversarial arms? (K32)
7. Does a self-written tally work as well as a tool-kept one, and what does bookkeeping cost in tokens? (K35)
8. Do few-shot allocation demos hurt strong models because of difficulty or format? (critique gap 10)
9. Can an LLM estimate per-plan success probability before any attempt, with calibration good enough to allocate? (K28, partly)
10. What do stop rules lose on hard items with near-zero base accuracy? (K34)
11. Do the 2023-2024 bandit failures say anything about 2026 agents inside a reasoning scaffold, or are they an artefact of model age?

## 11. Sources

[V] opened; [M] snippet or secondary only. The "opened" flags come from the finders; the writer re-checked only the numbers listed in critique.md.

**Theory**
- [M] Gittins (1979) Bandit processes and dynamic allocation indices. https://doi.org/10.1111/j.2517-6161.1979.tb01068.x (facts via https://en.wikipedia.org/wiki/Gittins_index) [a01, c25, b28]
- [M] Whittle (1980) Multi-armed bandits and the Gittins index (via Wikipedia) [a02]
- [M] Weber (1992) On the Gittins index for multiarmed bandits (via Wikipedia) [a03]
- [V] Wikipedia, Multi-armed bandit, history. https://en.wikipedia.org/wiki/Multi-armed_bandit [a04]
- [M] Lai and Robbins (1985), Robbins (1952), Thompson (1933, 1935): via Auer 2002 and Russo 2018 [a26]
- [V] Auer, Cesa-Bianchi, Fischer (2002) Finite-time analysis of the multiarmed bandit problem. https://homes.di.unimi.it/cesa-bianchi/Pubblicazioni/ml-02.pdf ; https://doi.org/10.1023/A:1013689704352 [a05-a07, b14]
- [V] Agrawal and Goyal (2012) Analysis of Thompson sampling. https://arxiv.org/abs/1111.1797 [a08, b15]
- [V] Russo et al. (2018) A tutorial on Thompson sampling. https://arxiv.org/abs/1707.02038 [a09, b16]
- [V] Bubeck, Munos, Stoltz (2011) Pure exploration in finitely-armed and continuous-armed bandits. https://arxiv.org/abs/0802.2655 [a10, b17]
- [V] Garivier and Kaufmann (2016) Optimal best arm identification with fixed confidence. https://arxiv.org/abs/1602.04589 [a11]
- [V] Li et al. (2018) Hyperband. https://arxiv.org/abs/1603.06560 [a12, a13, a25, b18, d18]

**Human exploration**
- [M] Wilson et al. (2014) Humans use directed and random exploration. https://doi.org/10.1037/xge0000728 [c26]
- [V] Gershman (2018) Deconstructing the human algorithms for exploration. https://pmc.ncbi.nlm.nih.gov/articles/PMC5801139/ [b24, b25]
- [V] Healthy cognitive aging and directed and random exploration in the Horizon Task (2024). https://pmc.ncbi.nlm.nih.gov/articles/PMC10871551/ [b26]
- [V, sample sizes missing] Phelps et al. (2025) Dynamics of explore-exploit decisions. https://pmc.ncbi.nlm.nih.gov/articles/PMC12742802/ [b27]

**LLM bandits and exploration**
- [V] Krishnamurthy et al. (2024) Can LLMs explore in-context? https://arxiv.org/abs/2403.15371 [a14, a15, b01, b02, c01-c04]
- [V] Nie et al. (2025) EVOLvE / BanditBench. https://arxiv.org/abs/2410.06238 [a16-a18, b03-b05, c05-c08]
- [V] Binz and Schulz (2023) Using cognitive psychology to understand GPT-3. https://arxiv.org/abs/2206.14576 [a19, b11, c09, c10]
- [V] Coda-Forno et al. (2023) Meta-in-context learning. https://arxiv.org/abs/2305.12907 [a20, b12, c11]
- [V] Schubert et al. (2024) In-context learning agents are asymmetric belief updaters. https://arxiv.org/abs/2402.03969 [b13, c12]
- [V] Park et al. (2025) Do LLM agents have regret? https://arxiv.org/abs/2403.16843 [a21, b06, b07, c24, d06]
- [V] Monea et al. (2025) LLMs are in-context bandit reinforcement learners. https://arxiv.org/abs/2410.05362 [b08, d05]
- [V] Schmied et al. (2025) LLMs are greedy agents. https://arxiv.org/abs/2504.16078 [b09, b10, d04]
- [V] Pan, Xie, Wilson (2025) LLMs think too fast to explore effectively. https://arxiv.org/abs/2501.18009 [c13, c14]
- [V] Zhang et al. (2025) Comparing exploration-exploitation strategies of LLMs and humans. https://arxiv.org/abs/2505.09901 [d01]
- [V] Harris and Slivkins (2026) Should you use your LLM to explore or exploit? https://arxiv.org/abs/2502.00225 [d02]
- [V] Arumugam and Griffiths (2026) Toward efficient exploration by LLM agents. https://arxiv.org/abs/2504.20997 [d03]
- [M] Lee et al. (2023) Supervised pretraining can learn in-context RL. https://arxiv.org/abs/2306.14892 [c22]
- [M] Laskin et al. (2022) In-context RL with algorithm distillation. https://arxiv.org/abs/2210.14215 [c23]
- [V] Taberner-Miller (2026) ParetoBandit. https://arxiv.org/abs/2604.00136 [d07]

**Test-time compute, stopping, pruning**
- [V] Brown et al. (2024) Large language monkeys. https://arxiv.org/abs/2407.21787 [a22, b19, c17]
- [V] Snell et al. (2024) Scaling LLM test-time compute optimally. https://arxiv.org/abs/2408.03314 [a23, b20, c16]
- [V] Damani et al. (2024) Learning how hard to think. https://arxiv.org/abs/2410.04707 [a24, b21, c15, d16]
- [V] Zuo and Zhu (2026) Strategic scaling of test-time compute: a bandit learning approach. https://arxiv.org/abs/2506.12721 [b22]
- [V] Manvi, Singh, Ermon (2024) Adaptive inference-time compute. https://arxiv.org/abs/2410.02725 [b23, d12]
- [V] Aggarwal et al. (2023) Let's sample step by step: Adaptive-Consistency. https://arxiv.org/abs/2305.11860 [c18]
- [V] Li et al. (2024) Early-stopping self-consistency (ESC). https://arxiv.org/abs/2401.10480 [c19, d17]
- [V] Zhang et al. (2025) Reasoning models know when they're right. https://arxiv.org/abs/2504.05419 [d08]
- [V] Wang et al. (2025) Sampling-efficient test-time scaling (ST-BoN). https://arxiv.org/abs/2503.01422 [d09]
- [V] Fu et al. (2025) Deep Think with Confidence. https://arxiv.org/abs/2508.15260 [d10]
- [V] Fu et al. (2025) Efficiently scaling LLM reasoning with Certaindex. https://arxiv.org/abs/2412.20993 [d11]
- [V] Tang et al. (2024) Code repair with LLMs gives an exploration-exploitation trade-off (REx). https://arxiv.org/abs/2405.17503 [d19]
- [V] Zhou et al. (2024) Language Agent Tree Search. https://arxiv.org/abs/2310.04406 [c20]
- [V] Li et al. (2024) Efficient prompt optimization through the lens of best arm identification (TRIPLE). https://arxiv.org/abs/2402.09723 [c21]

**Calibration**
- [V] Xiong et al. (2024) Can LLMs express their uncertainty? https://arxiv.org/abs/2306.13063 [d13]
- [V] Yoon et al. (2025) Reasoning models better express their confidence. https://arxiv.org/abs/2505.14489 [d14]
- [V] Kadavath et al. (2022) Language models (mostly) know what they know. https://arxiv.org/abs/2207.05221 [d15]

**Search note**
- [V] arXiv title searches for LLM Gittins/Whittle use (zero relevant hits). https://arxiv.org/search/?query=Whittle+language+models+restless&searchtype=all [d20]
