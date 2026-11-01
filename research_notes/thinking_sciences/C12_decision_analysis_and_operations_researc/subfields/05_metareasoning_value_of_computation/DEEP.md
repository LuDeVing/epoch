# Metareasoning, value of computation: deep document

*Folder: C12.05. Built from evidence_a-d.jsonl (a01-a27, b01-b25, c01-c31, d01-d18), claims.jsonl (K01-K26) and critique.md. Evidence ids in brackets. The founding 1991 text was never opened; see section 11.*

## 1. What it is

Metareasoning treats a thought as an action. Each thought has a cost (time, tokens, money) and a value (how much it improves the final decision). The agent should think only while the expected value of the next thought is higher than its cost. When no thought has positive net value, it should act.

Four terms matter.

- **Value of computation (VOC).** Expected gain in decision quality from running one computation, minus its cost. Formally: the expectation, over the belief the computation would produce, of the best-action value, minus the best-action value now, minus the cost [a01, a11, c01].
- **Value of information (VOI) and perfect information (VPI).** VOI is the value of one computation's result. VPI is the value of knowing everything about an action. VPI is an upper bound on what any amount of thinking about that action can give.
- **Metalevel problem.** Choosing which computation to run, and when to stop, is itself a decision problem (a belief-state MDP) [a02, a08].
- **Overthinking and underthinking.** Overthinking means spending more than the gain is worth. Underthinking means stopping, or abandoning a line of thought, too early [K05, K15].

Why it matters for our agent. The S0 gate decides how much to think about a problem before solving it. The S6 trigger decides when to stop, switch operator or escalate. Both are metareasoning decisions. Guardrails G7 (the schema must pay for itself), G11 (think briefly by default) and G12 (spend by difficulty) are special cases of this theory.

What this subfield adds beyond earlier documents in the series: the formal rule, its known failure (the one-step rule stops too early), the cost of the gate itself, and measured token savings from 2023-2026 LLM work. Human resource-rationality, bandits and optimal stopping, test-time scaling and overthinking are researched in parallel subfields; here we only note links.

## 2. History and theories in depth

**Precursors (1960s-1980s).** Matheson (1968) tied the worth of analysis to the value of information. Howard's value of information and Horvitz (1987/1990) built an expected-value-of-computation view. All three are named in Hay et al. [a02, a26]; none was opened.

**Russell and Wefald (1988-1991).** They stated the principle cleanly: a computation is an action; its utility is the expected improvement in the chosen action minus the time cost; stop when no computation has positive net utility [a01, c01]. To make it practical they used a myopic (single-step) estimate: for each possible next computation, ask whether doing just that one would change the choice, and how much that is worth.

- *The 1989 IJCAI experiment (opened, d01).* The algorithm MGSS* expanded the leaf with the highest estimated search value minus time cost. It played Othello against fixed-depth alpha-beta with the same evaluation function. Each tournament was 32 games from 16 random starts, colours alternated. Results: about even with depth-2 alpha-beta; significantly better at depths 3 and 4 with far fewer nodes; slightly better than even against depth-5 alpha-beta using about one sixth of the nodes. But wall-clock time was higher at depths 2 and 3 and only slightly lower at depth 4, because the metalevel bookkeeping was costly. Against depth-6 alpha-beta it could not build big enough trees and played poorly. The time-cost function had to be tuned per depth.
- *Russell 1990, MGSS2 (opened, d02).* Improved version. The author reports a "distinct advantage" over alpha-beta, "roughly 60:1 at depth 6". The unit of 60:1 (nodes, time or games) could not be read. The author calls the results preliminary and the cost function was again tuned per opponent depth.
- *The 1991 journal paper and the book (not opened: a01, b19, c01, d18).* ScienceDirect returned 403. Win counts and any later tables are unverified. No independent modern replication was found.

**Anytime algorithms and bounded optimality (1987-2011).** Zilberstein, Horvitz and Russell: algorithms with performance profiles, and a rule to stop when marginal gain per second falls below the cost. Recalled from memory only; no numbers are used here [c29].

**Hay, Russell, Tolpin, Shimony (2012), the formal repair [a02-a04, c05].** They cast the metalevel problem as a belief-state MDP and proved:
- Theorem 5: the expected number of computations of the optimal policy is at most VPI / c (c = cost per computation).
- Theorem 7: if the myopic policy computes, the optimal policy computes too. So myopic never over-computes relative to optimal, but it can under-compute.
- Theorem 10: for a one-armed Bernoulli problem the optimal policy needs at most (1 - mu)/c - 3 computations, and at most 1/(4c) - 3.

The myopic policy stops as soon as no single computation can flip the choice, even if several together would. A "blinkered" policy looks at many computations on one action at a time and fixes this, at time linear in the number of arms. In a 25-arm Bernoulli problem (1000 trials, regret = lost utility + c x n) blinkered beat myopic, UCB1 variants and ESP; myopic regret plateaued. In Go (Pachi, 9x9, 1000 repeats per setting, 5k-15k simulations per move) a hybrid with VOI at the root and UCT below reached a 64% win rate over plain UCT at 10,000 samples per move with stopping threshold c = 1e-6. Gains were largest at intermediate budgets; at very low budgets early stopping hurt. The 64% is the best reported cell, with no confidence interval [critique 4]. They also show that bandit rules (UCB1) do not solve this problem: bandits count reward during sampling and never stop, while selection problems pay only for the final choice.

**Lin, Kolobov, Kamar, Horvitz (2015) [a08, a09, c06].** Metareasoning for MDP planning is itself an MDP; optimal metareasoning is P-complete in the size of the base problem (polynomially harder, but impractical). They give a cheap VOC approximation from Bounded RTDP value bounds, linear in the number of actions per visited state. Four domains, 1000 runs each. A fixed think-then-act baseline fails when early thinking is costly; a think-with-probability baseline works only when tuned to the cost ratio; the VOC metareasoner adapts without tuning. Gains are small in an adversarial domain.

**Callaway et al. (2018), BMPS [a05-a07, c04].** Bayesian metalevel policy search approximates VOC as a weighted sum of myopic VOI, VPI and cost. Weights are learned by Bayesian optimisation. See sections 3 and 4.

**Cognitive science line.** Lieder and Griffiths (strategy selection as rational metareasoning, 2017; resource-rational analysis, 2020) [a22, a24, b20] and Callaway et al. 2022 [a25, b18] were not opened. Opened: Lieder et al. 2018 Learned Value of Control [a19], Callaway 2018 human planning [b15-b17], Callaway et al. 2021 fixations [a20] and a 2025 chess study [a21]. See sections 3 and 5.

**LLM era (2023-2026).** The VOC form reappears in four ways.
1. *Cost-in-the-reward training.* RaM's reward is VOC with token count as cost [a10]. Length-penalty RL (Arora and Zanette, AdaptThink, Thinkless) has the same shape [a13, a17, a18].
2. *Compute allocation by difficulty.* Snell et al. and Damani et al. [a15, b11].
3. *Stopping rules on samples or chains.* Adaptive-Consistency, ESC, DEER, DeepConf, REFRAIN, ASAG [a16, c26, d08-d11].
4. *Observations of waste or harm.* Overthinking on easy items, inverse scaling, underthinking [a14, b13, c09].

None computes a true value of information at runtime. They use proxies: answer agreement, confidence, token cost, progress.

## 3. Core findings with exact numbers

Status: E = established (two or more independent sources), S = single source, C = contested.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Myopic VOC stops too early; blinkered or multi-step fixes it | 25-arm Bernoulli, 1000 trials: blinkered beats myopic; myopic regret plateaus | Hay 2012 [a03, c05] | E (theory + Othello history) |
| Optimal policy computes at most VPI/c times | Theorem 5; Theorem 10: at most (1-mu)/c - 3 | Hay 2012 [a02] | E (proof) |
| 1989 Othello test: fewer nodes but more wall-clock | 32 games per tournament; about 1/6 of depth-5 nodes at slightly better than even; more time at depths 2-3; poor against depth 6 | Russell and Wefald 1989 [d01] | S |
| MGSS2 advantage | "roughly 60:1 at depth 6" (unit unread); preliminary | Russell 1990 [d02] | S |
| VOI policy in Go | 64% win vs UCT at 10,000 samples/move, c = 1e-6, 9x9, 1000 repeats | Hay 2012 [a04] | S |
| Three features approximate exact VOC | 90.8-100% of variance explained (cost 0.001-0.1); weights go from 0.76 VPI + 0.46 VOI1 - 4.5 cost to 0.00 VPI + 1.00 VOI1 - 1.00 cost as cost rises | Callaway 2018 [a05] | S (one paper) |
| BMPS near optimal | Binary task: at most 5.19% below optimal; 20.3% better than meta-greedy on average (6.78-35.8% range) | Callaway 2018 [a05, c04] | S |
| Bernoulli metalevel | BMPS 0.6535 vs optimal 0.6596 (99.1%), meta-greedy 0.60, DQN 0.58, full deliberation 0.20; 2000 test episodes | Callaway 2018 [a06] | S |
| Planning tree | BMPS 0.392 vs meta-greedy 0.307, recursively blinkered 0.368, full deliberation -1.740 | Callaway 2018 [a07] | S |
| Humans plan near VOC but stop early | 51 of 60 MTurk kept; score 6.54 vs 9.33 optimal; 45.0% of computations suboptimal yet 86.8% of max VOC; deviations: 28.3% too early, 6.3% too late, 65.5% wrong node; mean rationality 80.0% (SD 26.4) | Callaway CogSci 2018 [b15, b16] | E (3 sources, deviation numbers from one conference paper) |
| Model comparison, human planning | Exp 1 likelihood: optimal 30625, best-first 31744, directed cognition 34025, random 34579. Exp 2 BIC: optimal 21203, directed cognition 25354, best-first 29122, random 29313 | Callaway CogSci 2018 [b15, b17] | S |
| Chess move time follows search benefit | More than 12 million games; Elo-by-benefit interaction 0.02-3.07 across settings, all p < 1e-50; modest; also rises when true benefit is 0 | Chess study 2025 [a21] | E (with a19, a20) |
| Learned Value of Control fits human control learning | BIC 1817.8 vs Rescorla-Wagner 9763.2 and WSLS 3449.9 on one reanalysed set | Lieder 2018 [a19] | S |
| RaM cuts tokens | 8B: RaM 63.5% acc / 146.2 tokens vs STaR 61.9 / 215.1, CoT few-shot 56.4 / 253.6, direct 45.8 / 0. 3B: 50.1 / 170.8 vs 47.4 / 222.7 vs 34.8 / 261.9. Abstract: 23-45% fewer tokens (v3: 23-42%) | De Sabbata 2025 [a10, b01] | E (with the length-penalty cluster, b22) |
| RaM adaptivity weak at 8B | 3B: hard vs easy length 145 vs 72 (50.3%), STaR 34.4%. 8B: RaM 36.0% vs STaR 35.9%. Instruct models 0.5-0.9% | De Sabbata [b02, a11] | S |
| RaM out of distribution | MMLU-CF tokens down 28-36%; one model 36.4 vs STaR 40.2 (-3.8, CI about +-2.4) | De Sabbata [b03] | S |
| Length-penalty RL | 7B: about 50% fewer tokens, under 5% accuracy loss; GSM8K -65% tokens (-1.7 pt), MATH500 -37% (-2.2), AIME24 -16% (-3.3); alpha 0.2: MATH 4000 to 2600, AIME 13,000 to 9,000 | Arora and Zanette 2025 [a13, b10] | E |
| Learned think / no-think | AdaptThink: length -53.0% (1.5B), -40.1% (7B), accuracy +2.4 and +2.3 points. Thinkless: long-chain use cut 50-90% (abstract only) | Zhang 2025 [a17]; Fang 2025 [a18] | E (maths) |
| Overthinking | "2+3": 1,953% more tokens than conventional models, 13 solutions, first correct answer in 39 of 901 tokens (4.3%); MATH500 QwQ-32B-Preview: -48.6% tokens at same accuracy, SimPO alone -22.3%; 2-4 solution rounds in 76-80% of cases (QwQ) and 59-63% (R1) | Chen 2025 [a14, b06] | E |
| Hard non-convergence | R1-Distill-7B on AIME: 43.5% of generations never end by 10,000 tokens, 11.5% accurate; converged 56.5% at 96.5%; difficulty r2 = 0.186; probe AUC 0.608 | Oladri 2026 [d14] | S |
| CoT helps mainly maths and symbolic | 110 papers, 1,218 comparisons: +14.2 symbolic, +12.3 math, +6.9 logic; top three 56.9 vs 45.5; others 56.8 vs 56.1; up to 95% of MMLU gain on "=" questions | Sprague 2025 [c20, b04] | E |
| Allocation by difficulty | PaLM-2 on MATH: about 4x less test-time compute than best-of-N (64 vs 256 samples); beam search better on hard questions and low budgets; best-of-N better on easy and high budgets; revision better on easy | Snell 2024 [a15, c10] | E |
| Input-adaptive allocation | Code up to 50% less compute, chat about 10%; routing calls the expensive decoder 50-75% of the time; about half of coding problems have zero success | Damani 2024 [b11, c24] | S |
| Statistical stopping on samples | Adaptive-Consistency: up to 7.9x fewer samples, mean drop under 0.1% (category average 3.3x, 0.04%; GPT-3.5-Turbo 4.4x with 0.2% drop; Vicuna-13B 1.9x). ESC: MATH -33.8%, GSM8K -80.1%, StrategyQA -76.8% | Aggarwal 2023 [a16, c25]; ESC [c26] | E |
| Early exit on confidence | DEER: chains -19.1% to -80.1%, accuracy +0.3 to +5.0; probe exit up to 24% fewer tokens; NoWait: -27% to -51% | [c14, d09, c13, b14] | E for the effect, C for the ranking |
| NoThinking at low budget | AMC23 at 700 tokens: 51.3 vs 28.9 (R1-Distill-Qwen only); lost 12-17 average points on Qwen3-4B/8B | Ma 2025 [c15, d17, d10] | C (model-specific) |
| Prompt-only budget gate | TALE-EP, GPT-4o-mini: GSM8K-Zero 99.50 to 98.72, 253 to 23 tokens; 6-set average 83.75 to 81.03, 461 to 149 tokens (-68.6%), expense 290 to 118 (-59%); College 78.00 to 70.00 | Han 2024 [d04] | S; direction E with d03 |
| Chain of Draft | GSM8K CoT 95.4 vs CoD 91.1 (GPT-4o), 95.8 vs 91.4 (Claude); about 80% fewer tokens; coin flip 100% kept, -68% / -86% tokens; sports -92.4% | Xu 2025 [d03] | S |
| Gate cost | TALE: 91% fewer output tokens became 69% lower expense on easy items, about 44% on the hardest | [d04] | S |
| Negative VOC on an ordinary easy set | Llama-3.1-8B GSM8K-Zero: direct 70.32 (13.5 tokens), CoT 65.04 (251), TALE-PT-SFT 78.43 (77.9). GPT-4o-mini: CoT 99.50 vs direct 97.21 (sign flips) | [d05] | E on existence, sign model-specific |
| Inverse scaling | Claude Opus 4 from near 100% to 85-90%; R1 from 70% to 30% (5 distractors) | Gema 2025 [b13, c23] | E (constructed tasks) |
| Accuracy rises then falls with extended thinking | s1 budget forcing AIME24 50 to 57%; parallel thinking up to 20% higher than extended at the same budget | [c11, c22] | C |
| Intrinsic self-correction harms | GPT-3.5 CSQA 75.8 to 38.1; GPT-4 GSM8K 95.5 to 91.5 to 89.0; HotpotQA 49.0 to 43.0 | Huang 2024 [c21] | S |
| Underthinking | Wrong answers have more thought switches and tokens (QwQ-32B-Preview, R1); decoding penalty TIP helps | Wang 2025 [c09] | S |
| Plan-frequency peak | Intermediate planning frequency best in Crafter and POGS (Llama-3.3-70B, 100 seeds each), plus Gemini 2.5 Flash and TextWorld; trained 8B reward 0.387 vs 70B 0.379 at 85% fewer tokens | Paglieri 2025 [c19, d06] | C |
| Prompted "plan only when necessary" fails | Falls back to always or never; no numbers | [d06] | S |
| Stop-signal ranking | Verbalised confidence GPT-4 AUROC 62.7%; GSM8K 54.8% vs 5-sample consistency 92.7%. ASAG head-to-head (Qwen3-4B, accuracy / length): vanilla 71.0; TALE 67.1 / 58.7%; Dynasor 71.6 / 64.4%; DEER 71.3 / 64.4%; ASAG 73.9 / 63.5% | [d07, d10] | C |
| DeepConf | DeepConf-low cuts tokens 43-79% (up to 84.7%) vs 512-sample voting; top-10% filter can hurt through overconfidence | Fu 2025 [d08] | S |
| REFRAIN | Qwen3-8B: GSM8K +0.30 with 35.9% fewer tokens; MATH-500 -0.20, 39.0%; CSQA +0.90, 54.2%; GPQA-D +6.56, 21.5% | Sun 2025 [d11] | S |
| Cross-model errors correlated | 349 LLMs / 12,032 questions; 71 LLMs / 14,042 (HELM); same wrong answer about 60% when both err vs 33% by chance | Kim 2025 [d12] | E |
| Majority vote can fall with more calls | Non-monotone curve on mixed easy and hard queries | Chen 2024 [d13] | S (abstract only) |
| Cascades | FrugalGPT up to 98% cost cut at GPT-4 accuracy | Chen 2023 [c27] | E |
| Hand-coded fast/slow switch | SwiftSage, ScienceWorld, 30 tasks: 84.7 vs ReAct 36.4, Reflexion 45.3; tokens per action 757 vs 1,971 and 2,983 | Lin 2023 [c28] | S |
| Meta-Reasoner | Claims 9-12% higher accuracy and 51-55% less inference time than o1-preview | [c18] | S (abstract) |
| MRT | 2-3x relative gain, about 1.5x token efficiency vs outcome-reward RL | Qu 2025 [c12] | S (abstract) |

## 4. Mechanisms and models

### 4.1 The VOC rule

State: belief b over the answer (or over the value of each option). A computation k returns information and moves the belief to b'.

- VOC(k, b) = E[ max_a U(a | b') ] - max_a U(a | b) - cost(k)
- Policy: run the k with the highest VOC while that value is above 0; otherwise act.
- Cost is additive per step (tokens, seconds, dollars). Harada (1997, per a02) gives conditions under which additive cost is valid; it fails if time has a deadline-like shape.

### 4.2 Myopic versus blinkered versus bound-based

- **Myopic (VOI_1).** Value of one more step only. Cheap. Fails when no single step can change the choice but a chain of steps can. Theorem 7 says it never computes when the optimal policy would not.
- **Blinkered.** For each option, the value of any number of steps on that one option, others held fixed. Cost linear in the number of options. Handles the "no single step flips the choice" case.
- **VPI cap.** Total possible value from an option is bounded by VPI. So the number of steps worth buying is at most VPI / c (Theorem 5). Use this as a hard upper limit on thinking steps once you can bound the stakes.
- **BMPS.** Score = w1 * VOI_1 + w2 * VPI - w3 * cost; run the best-scoring computation if its score is above 0 (the stop action scores 0). Weights come from Bayesian optimisation on simulated episodes. Best weights move from VPI-heavy (cheap thought) to VOI_1-only (expensive thought).

### 4.3 How an engineer would turn this into an LLM gate

A gate cannot compute exact VOC. Use proxies.

| VOC term | Proxy for an LLM agent |
|---|---|
| Probability the answer would change | Disagreement among 2-5 cheap samples; margin between the top two answers |
| Stakes (value gap) | Task-type prior, or the cost of a wrong submission versus a retry |
| Upper bound (VPI) | Remaining budget, or "can a checker exist" (with no verifier, the VOC of revision is about 0, see K14) |
| Cost | Token count of the step times a per-token price, plus the gate's own tokens |
| Stop | Margin above threshold, or progress per block below threshold |

Implementable rules from the literature:

1. **Statistical stop on samples (Adaptive-Consistency).** After each sample, update a Beta (or Dirichlet) posterior on "top answer beats runner-up". Stop when P(lead is real) exceeds a threshold (for example 0.95). It assumes independence. Same-model samples are correlated (G4), so set the threshold higher than the nominal value [a16, d12].
2. **Window stop (ESC).** Draw samples in windows of size w. Stop the first time a window is unanimous [c26].
3. **Confidence early exit (DEER-style).** At a reflection marker ("Wait", "Hmm"), ask for a trial answer. If the token probability of the trial answer is above a threshold, stop. Needs log-probabilities [c14, d09].
4. **Budget estimate (TALE-EP).** Ask the model for a token budget for this question, put it in the prompt, answer within it. Count the estimator tokens in the total [d04].
5. **Progress rule (MRT idea).** After each block, estimate the change in the probability of final success. Stop or switch when progress per block falls below the cost per block [c12]. At runtime this needs a cheap success estimator (agreement of short probes).
6. **Cap and switch.** A hard in-run cap with an operator switch at the cap. Nothing predicts non-convergence before the answer exists (K25), so a cap is the practical form [d14].
7. **Cascade.** Cheap pass; escalate only if a verifier or agreement check fails [c27].

### 4.4 Training-time forms (for reference; our agent cannot train)

- **RaM:** reward = log pi(y | z, x) - log pi(y | x) - lambda * tokens, where z is the chain. The gain term is how much the chain raises the probability of the gold answer. Expert iteration: K = 4 chains per question, keep the best when its advantage is above 0, 5 iterations, lambda = 0.1 [a10]. The gold answer makes it a training signal, not a runtime rule.
- **Arora-Zanette:** penalty only on correct responses, scaled against other correct samples for the same prompt; one knob alpha [a13].
- **AdaptThink:** RL with a constraint that accuracy must not fall; the model chooses Thinking or NoThinking [a17].
- **Thinkless:** one control token, decoupled GRPO; plain GRPO collapsed the mode choice early [c17].
- **MRT:** a dense bonus equal to the per-block progress in final-success probability [c12].
- **L1:** train the model to obey a requested token budget [b12].

### 4.5 Human models (what we compare against)

- Mouselab-MDP: each click has a cost; the VOC-optimal policy is the benchmark. People's clicks are fit better by it than by best-first, breadth-first or depth-first search [b15].
- Learned Value of Control: predict the value of each control signal from features, subtract effort cost, learn by RL [a19].
- Fixations: optimal sampling from options whose value is high and uncertain (five parameters) [a20].

## 5. What holds up

**Holds up (two or more independent sources).**
- The VOC form is a correct normative rule and was shown useful in theory (Hay, Lin) [a02, a08].
- Overthinking exists in reasoning models, and savings are largest on easy items (Chen, Arora, AdaptThink, Snell, d05, d14) [K05].
- Token cuts of roughly 20-65% at close to equal accuracy on maths with training (RaM, Arora, AdaptThink); 68-92% with prompt-only style or budget changes on easy items (TALE, CoD) [K06, K20].
- CoT gains concentrate in maths and symbolic tasks (Sprague, plus RaM's own finding) [K09].
- Allocation by difficulty beats uniform best-of-N (Snell, Damani, cascades) [K10, K18].
- Statistical stopping on samples saves 3-8x in samples with tiny accuracy loss (Adaptive-Consistency, ESC) [K12].
- More thinking can hurt (Gema, Ghosal, d05, Wang) [K13].
- Errors are correlated across models, so agreement is a floor on risk, not a probability (Kim, Chen) [K24].
- Humans also stop planning early, and their thinking time follows search benefit (Callaway, chess) [K04, K19].

**Failures, weaknesses and moderators.**
- *The founding method's own test.* Fewer nodes did not mean less time at depths 2-3; the one-step rule failed at depth 6; the cost function was tuned per depth [d01, d02, K26]. A gate that costs more than it saves is a net loss (G7).
- *RaM's adaptivity.* At 8B the hard-vs-easy gap equals STaR's (36.0 vs 35.9%). One model lost 3.8 points out of distribution [b02, b03]. Instruct models barely adapted (0.5-0.9%).
- *Chen's trimming.* First-correct-only trimming hurt hard MATH500 items that need reflection. Efficiency is judged against a known correct answer, which an agent lacks [a14].
- *NoThinking.* Wins at 700 tokens on R1-Distill-Qwen but loses 12-17 average points on Qwen3-4B/8B. The gap closes as budget grows. Budget forcing penalises Thinking through truncation [c15, d17, d10].
- *Extended thinking.* s1 gains (50 to 57% on AIME24) against Ghosal's rise-then-fall and Gema's inverse scaling. Direction depends on budget, model and task, and nobody gives a predictor [critique].
- *Stop signals.* Verbalised confidence is near chance for error prediction (AUROC 62.7%). Agreement is far better but costs M samples. DEER looks good in its own paper and worse than vanilla on GSM8K and MATH-500 with Qwen3 in REFRAIN. Every comparison is run by the proposing group [d07, d10, d11].
- *Overconfidence.* Logprob filtering fails when the model is confidently wrong (DeepConf top-10% filter) [d08].
- *Illusion of Thinking.* Plain models match or beat thinking versions on easy puzzles; both collapse at high complexity. Lawsen shows part of the collapse is a token-limit and impossible-instance artefact [d15, d16].
- *Plan frequency.* Intermediate peak in four settings, yet no plan-on-surprise versus fixed-k test, and a prompted adaptive planner failed [d06].
- *Difficulty estimation costs.* Snell and Damani need a difficulty estimate that itself spends compute; neither nets it out in a deployed loop. About half of coding problems have zero success, so allocation can waste budget there [b11, b24].
- *Self-correction.* Without an external check, a revise step has negative expected value (GPT-3.5 CSQA 75.8 to 38.1). Gains reappear with oracle labels or tool feedback [c21]. This is consistent with Snell's verifier-based revision gains only if the external check is the difference.
- *Duplicated counts.* Callaway 2018 lines a05, a06, a07, c04 are one paper (independent sources = 1) [critique].
- *Human data.* The deviation numbers come from one conference paper (51 participants); the 2022 journal version was not opened [b16, b18].
- *Chess.* Observational; effect modest; the benefit proxy is Stockfish depth-1 [a21].

**Interventions that worked and that did not.**
- Worked: length-penalty RL; a budget in the prompt on easy items; draft-style prompts; sample-agreement stopping; early exit on confidence (open models); cascades; adaptive plan timing after SFT+RL.
- Did not work or are risky: asking the model to plan only when needed (prompt only); verbalised confidence as a stop signal; intrinsic self-correction; forced "Wait" extension as a rule; planning before every action; one-step VOC alone.

**Corrections from the cross-check [critique].** Adaptive-Consistency on GPT-3.5-Turbo: 4.4x fewer samples with a 0.2% drop, not under 0.1%. RaM's 50.3% gap is on the 3B model; the 8B row equals STaR. Snell's "pretraining wins on the hardest" holds only for some pretrain/inference ratios. RaM's few-shot CoT uses 1,080 input tokens against 73, so total-cost savings exceed the output-token savings.

## 6. Language models

**Training-time (open models, maths mostly).** Section 3 gives the numbers. In short: RaM 23-45% fewer tokens at equal or better accuracy on Llama 3B/8B; Arora and Zanette about 50% at under 5% loss on R1-Distill 1.5B/7B; AdaptThink -53.0% / -40.1% length with +2.4 / +2.3 points; Thinkless 50-90% fewer long chains (abstract only). All need training, all use closed-answer tasks, none has an agent or tool test. No head-to-head between RaM and Arora exists [b22].

**Prompt-only (closed APIs).**
- TALE-EP (GPT-4o-mini): 6-set average accuracy 83.75 to 81.03, output tokens 461 to 149, expense 290 to 118 (1e-5 dollars). The drop grows with difficulty: about -1 on GSM8K-Zero, -8 on MathBench-College. GSM8K itself rose (81.35 to 84.46). Models often ignore tight budgets ("token elasticity") [d04].
- Chain of Draft (GPT-4o, Claude 3.5 Sonnet): about 80% fewer tokens; GSM8K down 4.3 and 4.4 points; coin flip unchanged at 100%; date understanding up for Claude (87.0 to 89.7). Needs hand-written few-shot drafts; weak zero-shot and below 3B parameters [d03].
- Chain-of-thought versus direct: gains concentrate in maths and symbolic work (Sprague). For Llama-3.1-8B on easy GSM8K-Zero, CoT (65.04) is below direct (70.32); for GPT-4o-mini the sign is reversed (99.50 vs 97.21) [d05].

**Reasoning models at inference time.**
- Overthinking: 1,953% more tokens than conventional models on "2+3"; extra solutions add little [a14, b06].
- Early exit and reflection suppression: DEER -19.1% to -80.1% length; NoWait -27% to -51%; probe exit up to -24%. In the ASAG head-to-head on Qwen3-4B/8B, adaptive methods keep about a third of tokens off at near-equal accuracy and differ by 1-3 points; NoThinking loses 12-17 points [c13, c14, b14, d10].
- Non-convergence: 43.5% of AIME generations by R1-Distill-7B never end under 10,000 tokens and are 11.5% accurate; GSM8K and MATH-500 reach 95% of uncapped accuracy at 256 thinking tokens [d14].
- Inverse scaling and rise-then-fall: Gema, Ghosal, Illusion of Thinking [b13, c22, d15].
- Underthinking on hard problems: too many switches [c09].

**Compute allocation.** Snell (PaLM-2, MATH): about 4x less test-time compute than best-of-N. Damani: code up to 50% savings, chat about 10%. Cascades up to 98% cost cut. Parallel thinking beats extended thinking by up to 20% at equal budget (Ghosal) [a15, b11, c27, c22].

**Agents.** Planning at an intermediate frequency beats both extremes in Crafter, POGS and TextWorld; a trained 8B matches a 70B at 85% fewer tokens [d06]. SwiftSage's hand-coded switch gave 84.7 vs 36.4 (ReAct) with fewer tokens per action [c28]. Meta-Reasoner (a bandit over strategies) claims a 9-12% accuracy gain [c18]. Pan et al.: in Little Alchemy 2 most LLMs explore worse than humans, with uncertainty encoded early and empowerment late [c30]. Test-time interaction scaling is another route [c31].

**What nobody has shown.** A VOC gate in a tool-using agent at equal total tokens; a prompt-only gate on a reasoning-model API; a calibrated same-model-sample stopping rule; an LLM test of one-step versus multi-step lookahead; a base rate of negative VOC in real agent workloads; LLM versus human early stopping on the same planning task [critique GAPS 1-10].

## 7. What our agent should take

Schema parts: G guardrail, S state, O operator, memory. Status: [E] established, [S] single-source, [C] contested.

### Add now (established)

1. **S0 gate: a cheap per-item thinking budget, with the gate cost counted.** Easy and fact-recall items get a direct answer or a short answer; maths, logic and symbolic items get a chain. Ties to G11 and G12. [E] K09, K20, K05. Evidence: c20, b04, a12, d03, d04, a14, b23.
2. **G7 applied to the gate itself: report net cost including the estimator call.** The gate stays only if it wins at equal total tokens. Principle [E] (K02); worked cost example [S] (K21). Evidence: a05, a08, c06, d04, d01.
3. **S6 trigger: stop sampling by a statistical rule, not a fixed N.** Stop when the leading answer is ahead by a margin. Treat agreement as a floor, with a raised threshold (G4). [E] K12, K24. Evidence: a16, c25, c26, d12, d13.
4. **S6: cap thinking per item and switch strategy at the cap.** Do not rely on predicting non-convergence. Thinking length should not grow past a task-typical bound. [E] K13 for the harm, K05 for the waste. Evidence: b13, c22, d05, d14, b25.
5. **Revise only with an external check.** Tool output, a held-out test or a mutated input. This is already G1 and G2; VOC gives the reason (no verifier means about zero expected gain). [S] K14, Huang c21, consistent with Snell a15.
6. **S0: allocate by difficulty; revise for easy items, parallel search for hard ones; give up or escalate with no progress after k steps and no foothold (G12).** [E] K10. Evidence: a15, b08, b09, c10, b24, b11.
7. **Cascade: cheap pass first, escalate on a failed check.** [E] K18. Evidence: c27, c28, b11.
8. **Do not use verbalised confidence as a stop signal.** Use agreement or an external check. [E-level, two sources] K23. Evidence: d07, d08.
9. **Diagnostic logging.** Per item: thinking tokens, answer-change count, line switches, and whether the stop was early or late; compare with an independent difficulty estimate. [E] basis K04, K19. Evidence: b16, a21.

### Test first (not yet added)

| # | Item | Part | Status | Evidence ids | Why not yet |
|---|---|---|---|---|---|
| T1 | Multi-step (blinkered) stop rule versus one-step "would one more step change my answer" | S6 | [E] in theory, no LLM test | a03, d01, K01 | Gap 4 open |
| T2 | Plan-on-surprise or on-stall trigger in code versus fixed k, equal tokens | S6 | [C] | c19, d06, c18, c28, K17, K22 | Prompted adaptive planning failed; coded trigger untested |
| T3 | Prompt-only budget gate on a closed API, on a bench that is not maths-only | S0 | [S] | d04, d03, K20, K21 | Net saving at matched tokens unreported; maths only |
| T4 | Best stop signal for our setting: agreement, logprob, progress, marker probe | S6 | [C] | d07-d11, K23 | Rankings flip between papers |
| T5 | Proxy VOC score (answer-change probability times stakes minus cost) versus fixed depth | S0 / S6 | [S] | a05, a07, K03 | One paper, simulation only |
| T6 | Early versus late stopping bias of the LLM, as measured in humans | S6 | [S] | b16, K04 | No LLM data |
| T7 | Extended thinking versus parallel short thinking: find the crossover per task type | S6 | [C] | c11, c22, c15, d10 | Direction depends on budget and model |
| T8 | Line-switch counter: penalise switching before a line is checked | S6 | [S] | c09, K15 | Published fix needs decoding access; prompt analogue untested |
| T9 | Difficulty probe from the first cheap pass (pass-rate bins) | S0 | [S] | b24, b11, d14 | Probe cost may eat the savings |
| T10 | Per-task-type cost weight (as Russell and Wefald tuned per depth) | S0 | [S] | d01, K26 | Needs tuning per setting; overfit risk |

## 8. Concrete tests on our bench

All arms get the same total token budget, including gate, probe and estimator tokens. Report accuracy, tokens and net cost. Use at least 3 seeds. Treat differences smaller than the seed spread as null.

| Test | Item type | Arms (equal total tokens) | Metric | Expected effect |
|---|---|---|---|---|
| B1 Gate vs always-chain | Mixed set: easy and recall items plus hard reasoning items (split by direct-answer success) | (a) always full chain; (b) per-item budget estimate then capped answer (TALE-EP style); (c) flat cap at the same average tokens | Accuracy by tier; total tokens including estimator | (b) saves 40-70% tokens on the easy tier within 1-2 points; (c) matches (b) on easy and beats it on hard if the estimator costs more than it saves |
| B2 One-step vs multi-step stop | Items where early steps look useless (long derivations, multi-hop) | (a) stop when one more step would not change the answer; (b) stop after k-step lookahead agreement; (c) fixed depth | Accuracy at matched tokens; premature-stop rate | (b) beats (a) on hard multi-step items by several points; equal on easy |
| B3 Sample-stop rule | Single-answer problems with ground truth | (a) fixed N samples; (b) Beta-posterior stop at 0.95; (c) Beta stop at 0.99 | Accuracy; samples used; rate of confidently wrong stops | Samples cut 3-5x on easy items; (b) overconfident on hard items; (c) restores accuracy |
| B4 Stop-signal head-to-head | Same items, reasoning model if available | (a) agreement across short probes; (b) verbalised confidence; (c) logprob confidence; (d) marker-triggered trial answer | AUROC for "stop is safe"; tokens saved at no more than 1 point loss | (a) and (d) beat (b); (c) fails on confidently wrong items |
| B5 Plan trigger | Multi-step tool or game tasks | (a) plan every step; (b) never plan; (c) plan every k steps; (d) plan on stall or surprise (coded trigger) | Success rate; tokens | (c) and (d) beat (a) and (b); (d) at least equals (c) with fewer tokens |
| B6 Revise with check | Items with a verifier and items without | (a) no revise; (b) self-revise; (c) revise only with an external check | Accuracy; tokens | (b) below (a) on no-verifier items; (c) at least (a), and above it on verifier items |
| B7 Extend vs parallel | Hard items on a token-budget ladder (low / mid / high) | (a) one long chain; (b) N short chains and a vote; (c) cap-then-switch | Accuracy per budget level | (b) at least (a) at equal tokens; the crossover moves with task type |
| B8 Early-late bias | Planning task with click costs (Mouselab-like) | LLM with free choice to inspect or act, versus the VOC-optimal policy | Share of deviations: too early / too late / wrong node | Humans: 28.3 / 6.3 / 65.5. Measure ours to learn the bias |
| B9 Negative-VOC base rate | Our whole bench, easy and hard | Short vs long thinking per item | Share of items where longer is worse | Base rate unknown; above 10% would justify the cap in S6 |
| B10 Cap and switch | Hard items that otherwise hit the cap | (a) run to the cap, submit; (b) cap then switch operator; (c) cap then resample | Accuracy among capped items | (b) or (c) lifts capped-item accuracy above the 11.5% seen in d14 |

## 9. What does not transfer, and why

- **Training-time methods.** RaM, Arora-Zanette, AdaptThink, Thinkless, MRT and L1 change weights. Our agent is a scaffold on a fixed model. Only the idea (cost in the objective, stop when gain falls short) transfers [K06].
- **Gold-answer gain term.** RaM's gain uses the correct answer. At runtime we have none, so we need a proxy [c02].
- **Decoding-level tricks.** TIP (penalising switch words) and NoWait need token-level access, which a closed API does not give [c09, b14].
- **Log-probability signals.** DeepConf and DEER need logprobs. Not all closed APIs give them [d08].
- **Game-tree results.** Russell and Wefald's savings are node counts. An LLM thought is not a node, and the metalevel bookkeeping cost differs [d01].
- **Simulated metalevel problems.** BMPS results use known reward structures and offline training that pays back only if the problem repeats [a05, a07].
- **Maths-only evidence.** Almost every LLM number is on maths or closed-answer sets. Fact-recall, open-ended and tool tasks are untested [a27].
- **Constructed failure tasks.** Gema's tasks were built to break models; Illusion of Thinking is partly a token-limit artefact [b13, d16].
- **Human lab tasks.** Mouselab-MDP toy trees with 51 participants. LLM thoughts do not share the same cost structure [b15].
- **Bandit rules.** UCB1 and UCT count reward during sampling and never stop; they solve a different problem [a04].
- **Optimal metalevel policy.** It is as hard as the base problem and invites infinite regress. We must use proxies [a08, c06].
- **Difficulty bins as published.** Snell's bins use pass rates from many samples, which cost compute [b24].

## 10. Open questions

1. What did the 1991 Russell-Wefald text report (win counts, the unit of 60:1), and does it replicate with modern engines?
2. Does a prompt-only gate cut tokens 30% or more on a reasoning-model API, and on non-maths tasks?
3. What is the net saving of a gate at equal total tokens (estimator and probes included)?
4. Which stop signal wins on our tasks: agreement, logprob, progress, marker probe?
5. Does one-step VOC fail in LLM agents, and does a two-or-three-step lookahead fix it?
6. Can overthinking and underthinking be told apart per item before the answer exists? (A probe AUC of 0.608 on one model says not yet.)
7. In tool-using agents, is plan-on-surprise better than fixed frequency at equal tokens?
8. How large is same-model sample correlation, and how overconfident are Beta stopping rules (G4)?
9. What is the base rate of negative VOC in real agent workloads?
10. Do LLMs stop early, like people (28.3% of human deviations), or late?
11. Does the human journal version (Callaway 2022) change the deviation numbers?
12. Do savings transfer across model families? (NoThinking is model-specific.)

## 11. Sources

[V] = opened and read this session (full text, or the parts noted). [M] = snippet, abstract only, or memory.

**Founding and theory**
- [M] Russell and Wefald (1991), Principles of metareasoning, Artificial Intelligence 49; and Do the Right Thing, MIT Press. https://doi.org/10.1016/0004-3702(91)90015-C ; https://mitpress.mit.edu/9780262181440/ ; https://www.sciencedirect.com/science/article/pii/0004370291900156 (403) [a01, b19, c01, d18]
- [V] Russell and Wefald (1989), On Optimal Game-Tree Search using Rational Meta-Reasoning, IJCAI-89. https://www.ijcai.org/Proceedings/89-1/Papers/053.pdf [d01]
- [V] Russell (1990), Fine-Grained Decision-Theoretic Search Control. https://arxiv.org/abs/1304.1133 [d02]
- [V] Hay, Russell, Tolpin, Shimony (2012), Selecting Computations: Theory and Applications. https://arxiv.org/abs/1207.5879 [a02-a04, c05]
- [V] Callaway, Gul, Krueger, Griffiths, Lieder (2018), Learning to select computations. https://arxiv.org/abs/1711.06892 [a05-a07, c04]
- [V] Lin, Kolobov, Kamar, Horvitz (2015), Metareasoning for Planning Under Uncertainty. https://arxiv.org/abs/1505.00399 [a08, a09, c06]
- [M] Horvitz (1987/1990); Matheson (1968) [a26]. No URL.
- [M] Zilberstein and Horvitz line, anytime algorithms and bounded optimality [c29]. https://aaai.org/

**Human studies**
- [V] Lieder, Shenhav, Musslick, Griffiths (2018), Rational metareasoning and the plasticity of cognitive control. https://pmc.ncbi.nlm.nih.gov/articles/PMC5937797/ [a19]
- [V] Callaway, Rangel, Griffiths (2021), Fixation patterns in simple choice reflect optimal information sampling. https://pmc.ncbi.nlm.nih.gov/articles/PMC8026028/ [a20]
- [V] Time Spent Thinking in Online Chess Reflects the Value of Computation (2025, Cognitive Science). https://pmc.ncbi.nlm.nih.gov/articles/PMC12553403/ [a21]
- [V] Callaway, Lieder et al. (2018), A resource-rational analysis of human planning, CogSci. https://cocosci.princeton.edu/papers/Callaway_CogSci_2018.pdf [b15-b17]
- [M] Callaway et al. (2022), Rational use of cognitive resources in human planning, Nature Human Behaviour 6:1112. https://www.nature.com/articles/s41562-022-01332-8 [a25, b18]
- [M] Lieder and Griffiths (2017), Strategy selection as rational metareasoning [a22]; Lieder, Griffiths, Hsu (2018) [a23]; Lieder and Griffiths (2020), Resource-rational analysis, BBS. https://doi.org/10.1017/S0140525X1900061X [a24, b20]

**LLM training-time and efficiency**
- [V] De Sabbata et al. (2025), Rational Metareasoning for Large Language Models. https://arxiv.org/abs/2410.05563 [a10-a12, b01-b03, c02, c03]
- [V] Arora and Zanette (2025), Training Language Models to Reason Efficiently. https://arxiv.org/abs/2502.04463 [a13, b10, c07]
- [V] Chen et al. (2025), Do NOT Think That Much for 2+3=? https://arxiv.org/abs/2412.21187 [a14, b06, b07, c08]
- [V] Zhang et al. (2025), AdaptThink. https://arxiv.org/abs/2505.13417 [a17, c16]
- [M] Fang, Ma, Wang (2025), Thinkless (abstract numbers only). https://arxiv.org/abs/2505.13379 [a18, c17]
- [M] Qu et al. (2025), Meta Reinforcement Fine-Tuning (abstract). https://arxiv.org/abs/2503.07572 [c12]
- [V] Aggarwal and Welleck (2025), L1. https://arxiv.org/abs/2503.04697 [b12]
- [V] Han et al. (2024, v6 2026), Token-Budget-Aware LLM Reasoning. https://arxiv.org/abs/2412.18547 [d04, d05]
- [V] Xu et al. (2025), Chain of Draft. https://arxiv.org/abs/2502.18600 [d03]
- [M] Sui et al. (2025), Stop overthinking survey (skim only). https://arxiv.org/abs/2503.16419 [b21]

**Allocation, stopping, early exit**
- [V] Snell et al. (2024), Scaling LLM Test-Time Compute Optimally. https://arxiv.org/abs/2408.03314 [a15, b08, b09, b24, c10]
- [V] Damani et al. (2024), Learning how hard to think. https://arxiv.org/abs/2410.04707 [b11, c24]
- [V] Aggarwal et al. (2023), Adaptive-Consistency. https://arxiv.org/abs/2305.11860 [a16, c25]
- [V] Early-Stopping Self-Consistency (ESC), ICLR 2024. https://arxiv.org/abs/2401.10480 [c26]
- [V] Chen, Zaharia, Zou (2023), FrugalGPT. https://arxiv.org/abs/2305.05176 [c27]
- [V] Yang et al. (2025), Dynamic Early Exit (DEER). https://arxiv.org/abs/2504.15895 [c14, d09]
- [V] Reasoning Models Know When They're Right (probing). https://arxiv.org/abs/2504.05419 [c13]
- [V] Wait, we don't need to Wait! https://arxiv.org/abs/2506.08343 [b14]
- [V] Fu et al. (2025), Deep Think with Confidence. https://arxiv.org/abs/2508.15260 [d08]
- [V] Li et al. (2026), ASAG. https://arxiv.org/abs/2606.15070 [d10]
- [V] Sun et al. (2025), REFRAIN. https://arxiv.org/abs/2510.10103 [d11]
- [V] Xiong et al. (2024), Can LLMs Express Their Uncertainty? https://arxiv.org/abs/2306.13063 [d07]
- [V] Oladri et al. (2026), Token Budget Saturation. https://arxiv.org/abs/2607.21433 [d14]

**Reasoning limits and negative value**
- [V] Ma et al. (2025), Reasoning Models Can Be Effective Without Thinking. https://arxiv.org/abs/2504.09858 [c15, d17]
- [V] Muennighoff et al. (2025), s1. https://arxiv.org/abs/2501.19393 [c11]
- [V] Ghosal et al. (2025), Mirage of Test-Time Scaling. https://arxiv.org/abs/2506.04210 [c22]
- [V] Gema et al. (2025), Inverse Scaling in Test-Time Compute. https://arxiv.org/abs/2507.14417 [b13, b25, c23]
- [V] Wang et al. (2025), Underthinking. https://arxiv.org/abs/2501.18585 [c09]
- [V] Huang et al. (2024), LLMs Cannot Self-Correct Reasoning Yet. https://arxiv.org/abs/2310.01798 [c21]
- [V] Shojaee et al. (2025), The Illusion of Thinking. https://arxiv.org/abs/2506.06941 [d15]
- [V] Lawsen (2025), The Illusion of the Illusion of Thinking. https://arxiv.org/abs/2506.09250 [d16]
- [V] Sprague et al. (2025), To CoT or not to CoT. https://arxiv.org/abs/2409.12183 [b04, b05, c20]
- [V] Kim et al. (2025), Correlated Errors in LLMs. https://arxiv.org/abs/2506.07962 [d12]
- [M] Chen et al. (2024), Are More LLM Calls All You Need? (abstract and introduction only). https://arxiv.org/abs/2403.02419 [d13]

**Agents**
- [V] Paglieri et al. (2025), Learning When to Plan. https://arxiv.org/abs/2509.03581 [c19, d06]
- [M] Meta-Reasoner (abstract claims). https://arxiv.org/abs/2502.19918 [c18]
- [V] Lin et al. (2023), SwiftSage. https://arxiv.org/abs/2305.17390 [c28]
- [M] Pan et al. (2025), LLMs Think Too Fast To Explore Effectively (abstract). https://arxiv.org/abs/2501.18009 [c30]
- [M] Thinking vs. Doing: Test-Time Interaction (abstract). https://arxiv.org/abs/2506.07976 [c31]

Links to parallel subfields (not covered here): Resource-rational analysis, Test-time compute scaling, Overthinking, Bandit allocation, Optimal stopping, Bounded rationality and anytime, Meta-reasoning, Progress monitoring, Self-correction, Hierarchical planning, Exploration and exploitation.
