# Bounded rationality, anytime: deep document

*Subfield C12.06. Focus: quality as a function of time. Key works: Simon; Zilberstein. Schema parts touched: G6 (never abstain, submit best so far) and G12 (spend by difficulty). Evidence ids (a01-d20) and claim ids (K01-K32) refer to the files in this folder. Search limits: web search, arXiv API, Semantic Scholar and OpenAlex hit quota or rate limits, so some papers were found from memory of arXiv ids and then opened. Simon 1955/56, Russell and Wefald 1991, Horvitz and Hansen and Zilberstein 2001 were NOT opened; they are second-hand here.*

Overlaps with sibling subfields (links only, not covered here): Metareasoning and value of computation (C12.05), Optimal stopping, Bounded rationality and satisficing, Test-time compute scaling, Overthinking, Bandit allocation, Resource-rational analysis, Self-correction, Expected information gain.

---

## 1. What it is

An **anytime algorithm** returns an answer whose quality depends on how long it ran. It can be stopped at any moment and still give something. The question for this subfield is simple. How does answer quality change with time spent, and how should a bounded agent use that curve to decide when to stop, how to split time across parts, and what to hold in hand if it is cut off?

Two lines of work meet here.

1. **Bounded rationality** (Simon). Real agents have limited time and computing power. They do not optimise. They search until an option meets an aspiration level, then stop. This is the founding idea. It was not opened in this study (see section 11).
2. **Anytime and flexible computation** (Dean and Boddy 1988, Horvitz, Russell and Wefald, Zilberstein 1996). Computation is an action with a cost. Quality is a function of time, written as a **performance profile** Q(t). Stopping rules, schedulers and monitors are built on the profile.

The agent we are building is an LLM inside a scaffold. Its attempts are anytime procedures. A fixed token budget makes one attempt a "contract" algorithm. A loop with a banked best answer makes the whole thing "interruptible". Guardrail G6 (never abstain, submit best so far) is an anytime property. Guardrail G12 (spend by difficulty) is deliberation scheduling.

Main lesson in one line. The classical theory is clean but assumes a quality curve that rises and flattens. LLM curves often are not like that. They rise, fall, plateau and jump. So the classical rules are useful design ideas, but each one must be tested against the real curve of our model.

---

## 2. History and theories in depth

### 2.1 Simon: bounded rationality and satisficing (1955, 1956) [M, not opened]
- Simon argued that real choosers cannot compute the global optimum. They have limited information and limited computation.
- Satisficing: set an aspiration level, take the first option that meets it. If search is slow, lower the aspiration. If it is fast, raise it.
- The link to quality over time: the aspiration level is a stop rule, and its adjustment over time is a crude profile-driven control. No source we opened tests this against anytime stopping (K32, gap 9).
- Known only from general knowledge here (a11, b28, c05). Setting the aspiration level is the hard part. Treat the satisficing claims as unverified until opened.

### 2.2 Dean and Boddy (1988): time-dependent planning [V] (a01-a03)
- Coined "anytime algorithm". The time before an event varies. So a decision procedure should return a best-so-far answer whose utility is a function of computation time.
- Six pages, AAAI-88, pp 49-54. Formal. No experiment. Worked example: a robot classifying objects on a conveyor behind a partition.
- Five classes of performance profile: monotonic improvement; one-shot (nothing until time tau, then a fixed value); linear; piecewise linear with bounded utility; diminishing returns (concave, slope never rises).
- Scheduling results: one-shot class is pseudo-polynomial (cites Graham 1977). Linear class: always work on the event with the largest slope. Diminishing-returns class: a polynomial greedy time-slicing algorithm, work on the event with the largest marginal gain at each slice, optimal within epsilon.
- Eight assumptions: prediction time factored out; events occur on time; separate procedures per event; free preemption; cost is summed utilities; diminishing-returns procedures exist; utility monotone in time; negligible reaction time. Relaxing negligible reaction time makes the problem "arbitrarily complex". Independence of responses was called hard to relax.
- Special case: if cost equals reaction time plus deliberation time, stop deliberating when marginal gain falls to the cost slope.
- Authors warn that one-shot procedures perform poorly when the available time varies.

### 2.3 Horvitz, Russell and Wefald: flexible computation and value of computation [M]
- Each reasoning step is an action. Its value is expected utility gain minus time cost. A myopic version stops when one more step is expected to lose.
- Known second-hand through Zilberstein and Hay et al. (a12, b27, b23). Belongs to C12.05.
- Hay, Russell, Tolpin and Shimony (2012) [V] (b23): choosing which computation to run is a Bayesian selection problem, not a bandit. Bandit policies are biased away from low-estimate options and have no stopping rule. If the myopic policy computes, the optimal one does too (Theorem 7). If myopic stops in a closed set of states, so does the optimal one. Myopic value of information can stop too soon when one step has no value.

### 2.4 Zilberstein (1996): the AI Magazine framework [V] (a04-a10, c01-c03)
- Seven desired properties: measurable quality, recognizable quality, monotonicity, consistency, diminishing returns, interruptibility, preemptability.
- Quality metrics: certainty, accuracy, specificity.
- Worked example: randomized tour improvement on a 50-city TSP. Quality equals the fraction of tour-length reduction against the initial tour. Profiles come from many runs and curve fitting. Boddy and Dean used Q(t) = 1 - e^(-t) for a planner.
- Three profile types: PP Q(t) (expected quality at time t); conditional PP Pr(q_out | q_in, t) for chained modules; dynamic PP Pr(q_j | q_i, t) as a Markov process on current quality (Hansen and Zilberstein 1996). The dynamic profile predicts improvement better because it uses the current quality. Table size trades profile accuracy against cost.
- If quality is recognizable at run time, monotonicity can be made true by returning the best result so far instead of the latest (c03). This needs a reliable check.
- Contract vs interruptible. A contract algorithm needs the budget known in advance and may return nothing if cut early. An interruptible one can be stopped anywhere. Contract algorithms are easier to build and monitor and are the right end product when utility is predictable.
- Monitoring strategies: fixed contract (optimal when utility is predictable and the profile deterministic, Theorem 4); myopic marginal value of computation; monitoring policies that price the monitoring itself.
- **Theorem 5**: myopic value-of-computation stopping is optimal when the profile is monotone increasing and concave-down AND the cost of time is monotone increasing and concave-up. A profile with plateaus or later jumps makes myopic stopping quit too early.
- Applications listed: Bayesian network evaluation, model-based diagnosis, database queries, constraint satisfaction, sensor interpretation, path planning. Related: imprecise computation (Liu et al. 1991), design-to-time (Garvey and Lesser).
- Open questions Zilberstein names: how much performance variance justifies monitoring, how often to monitor, how coarse a quality estimate may be.

### 2.5 Zilberstein and Russell (1996): composition and the factor of 4 [V] (a07, a08)
- **Theorem 2.7 (Reduction)**: for any contract algorithm A there is an interruptible algorithm B with q_B(4t) >= q_A(t). Build B by running A repeatedly with exponentially growing limits (1, 2, 4, 8, ...). If interrupted at t, the last finished contract had length at least t/4.
- For search this gives iterative deepening for free. The factor 4 is a worst-case bound. Up to about 75 percent of time can be wasted at the moment of interruption. Typical cost is lower.
- **Theorem 1**: allocating time among several anytime modules to maximise system quality is NP-complete in the strong sense (reduction from partially ordered knapsack).
- **Theorem 2**: local compilation on tree-structured, bounded-degree programs is linear time and globally optimal if each module is input-monotone (deterministic profiles). **Theorem 3**: the probabilistic case needs input linearity, which the authors call "not very realistic". Piecewise-linear approximation is suggested.
- The tree assumption fails when sub-results are shared, for example F = E(D(B(A(x)), C(A(x)))). Only approximate methods remain.

### 2.6 Hansen and Zilberstein (2001): non-myopic monitoring [M]
- Stop or continue is a sequential decision problem solved by dynamic programming over a Markov dynamic profile. It extends the myopic rule to non-concave profiles.
- Only an abstract-level summary was seen (a13, c24). Not found applied to LLM reasoning (K31).

### 2.7 Human data on the same shape
- Speed-accuracy trade-off (Heitz 2014 [V], d19): accuracy is modelled as an exponential approach to an asymptote with an intercept and a rate. Macro-SAT is between conditions; micro-SAT is within a condition. The numbers in the part read (deadlines 225, 325, 425 ms giving 50, 70, 90 percent) are a simulation, not data. SAT experiments need several times more observations than ordinary ones.
- Chabris and Hearst (2003) [V] (d20): 23 grandmasters, 1,188 games, 719 true blunders (176 classical, 266 rapid, 277 blindfold). Blunders per 1,000 moves: 5.02 classical, 6.85 rapid (+36.5 percent), 7.63 blindfold. Rapid play averaged under one minute per move. Experts lose only a third of their quality when time is cut by a large factor. That is a "high early quality" curve.

### 2.8 The LLM turn (2024-2026)
Reasoning models made "thinking tokens" the time axis. A burst of work asks the anytime questions directly: what is quality at each thinking budget, can a trace be cut and still answered, when should it stop, and how should a budget be split? Sections 3, 5 and 6 cover the numbers.

---

## 3. Core findings with exact numbers

Status: **E** established (two or more independent sources), **S** single source, **C** contested, **O** open (no answer found). "One paper" means several evidence lines come from the same paper.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Anytime algorithm defined; seven properties | 7 properties; Q(t)=1-e^(-t) example | Dean & Boddy 1988; Zilberstein 1996 (a01, a04) | E |
| Best-so-far makes an anytime procedure monotone, if a check exists | n/a (design result) | Zilberstein 1996 (c03, a04) | E (K01) |
| Contract to interruptible by doubling budgets | q_B(4t) >= q_A(t); worst case about 75% waste at interruption | Zilberstein & Russell 1996 (a07) | E in theory; no LLM test (K02, K31) |
| Time allocation among modules is NP-complete | strong sense; optimal only for trees with input-monotone profiles | Zilberstein & Russell 1996 (a08) | E in theory (K03) |
| Myopic stopping optimal only for concave profile with convex time cost | Theorem 5 | Zilberstein 1996 (a09) | E (K04) |
| Real LLM quality curves are not monotone: rise then fall | 82.2 to 87.3% (385 to 1,100 tokens), then 70.3% at 15,980 tokens (one panel) | Ghosal 2025 (c15) | E (K05) |
| Longer reasoning lowers accuracy on built tasks | Claude Opus 4 from near 100% to about 85-90% (Misleading Math) and about 80% (Misleading Python); R1 70% to 30% with five distractors | Gema 2025 (a21, b05) | E for existence; S for prevalence (K05, K06) |
| Inverted U in chain length | optimal 14 steps (1.5B) to 4 steps (72B); gap optimal vs longest up to 40 points for 72B; p about 1e-8 for difficulty link; 30 questions per model | Wu 2025 (b10) | E (K18) |
| Easy items are overthought | 1,953% more tokens than conventional for "2+3"; first round correct in over 92% of cases; first round under 60% of tokens; ASDIV first round 287 tokens (38.7%); 48.6% cut on MATH500 (QwQ-32B-Preview) | Chen 2024 (a20, b08) | E (K07) |
| Correct answers are shorter than wrong ones on the same question | shorter chain up to 34.5% more accurate than the longest (Hassid); correct shorter than incorrect in QwQ, R1-Distill, LIMO (Zeng) | Hassid 2025; Zeng 2025; Su 2025 (d07, d14, b07) | E |
| Answer is often fixed early | answer reached after about 60% of steps (math); median 830 tokens of 2.7K produced on AMC23 | Answer Convergence 2025; Certaindex 2025 (c17, d16) | E |
| Early exit on model confidence | 11 models, 10 benchmarks: chains 19.1-80.1% shorter, accuracy +0.3 to +5.0; latency -27.9% (-36.3 to -58.6% branch-parallel) | DEER 2025 (a19, c16) | S for the confidence signal (K09); effect itself E (K08) |
| Early exit on a hidden-state probe | ROC-AUC above 0.7, ECE below 0.1; MATH threshold 0.85: 88.2% accuracy (same) with about 24% fewer tokens; 0.9: 88.6% with 19% fewer | Zhang 2025 (c18, d15) | S (needs hidden states) |
| Stop when independent answers agree | Adaptive-Consistency: 17 datasets, 3.3x fewer samples math (-0.1 acc), 2.9x commonsense (-0.2), 3.8x symbolic, 2.4x code (+0.4); ESC: MATH -33.8%, GSM8K -80.1%, StrategyQA -76.8%, CommonsenseQA -78.5%, Coin Flip -84.2%, Last Letters -67.4%; ESC vote equals full vote in 99.13-99.96% of cases; MBPP SC 62.18 vs ESC 62.15 at -23.21% samples; DeepConf consensus stop -52.8% tokens at K=512 with equal accuracy | Aggarwal 2023; Li 2024; Fu 2025 (d02, d03, d01) | E (K23) |
| No head-to-head of agreement stop vs self-confidence stop at equal tokens | none | gap search | O (K24) |
| Best use of budget depends on difficulty | compute-optimal matches best-of-N with up to 4x less compute (16 vs 64 generations; 64 vs 256 for revisions); beam search wins hard/low budget, best-of-N easy/high budget; small model plus test-time compute beats 14x larger on easy and medium (PaLM 2, MATH) | Snell 2024 (a14, c11) | S, one paper (K10) |
| Difficulty probe from answer stability | Certaindex r = 0.17-0.75, mean 0.52; saves 9-52% tokens; another group measured 81.44 vs 89.76 on MATH-500 (-8 points) | Fu 2025; Lin 2025 (d16, d08) | C (K30) |
| Repeated sampling coverage is log-linear | SWE-bench Lite 15.9% (1 sample) to 56% (250 samples) vs single-sample SOTA 43%; CodeContests Gemma-2B 0.02% to 7.1% | Brown 2024 (a15, b16) | S, one paper (K11) |
| Verifier-free selection plateaus | voting and reward-model selection plateau near 100 samples while coverage keeps rising | Brown 2024 (b17) | S |
| Selection among agent runs plateaus; hybrid breaks it | execution-based 43.7%, execution-free 42.8% Best@K; hybrid Best@26 51.0%; Pass@1 34.4%, Pass@26 64.4% | R2E-Gym 2025 (d06) | S, but agrees with S* (K25) |
| On code, model-written tests alone did not beat public tests | LiveCodeBench v2, 12 models; QwQ-32B-Preview 50% (N=1) to 80% (N=32), then plateau; two debug rounds help | S* 2025 (d05) | E with R2E-Gym (K25) |
| Parallel vs sequential at equal budget | Ghosal: parallel up to 20% better, 22% at 16K vs Wait, 47% vs exact budget control; Hassid: short-1@k up to 40% fewer tokens; s1: sequential extrapolated better than voting 2-64 | Ghosal; Hassid; s1 (c15, d07, b03) | C (K12) |
| Wait extension hurts untuned models | correct-to-wrong exceeds wrong-to-correct for QwQ, R1-Distill, LIMO | Zeng 2025 (d14) | E (K28) |
| Budget forcing (s1) | AIME24 50.0 to 56.7; Table 3: forcing 100% control, slope 15, 56.7; token-conditional 40% control, slope -24, 40.0; 12 of 30 AIME24 questions exceeded context at 512 steps; rejection sampling needed 655, 97, 8, 3, 2, 1 tries for caps 3500, 4000, 5000, 8000, 16000 | Muennighoff 2025 (a16, b01, c09, c10) | S, one paper, 30 items (K13) |
| Seed noise swamps small gains | Pass@1 SD 5-15 points over 20 seeds, nine models; one AIME24 item = 3.3 points; about 30 seeds for stable AIME24 mean; gaps up to 17.0% between reported and re-measured | Hochlehnert 2025 (d11) | S (K29) |
| Prompted token limits do not control length | token-conditional control 40%; TALE: 258 to 86 tokens at a 50-token budget but 157 at a 10-token budget; TALE-EP 81.03% vs 83.75% CoT at 32% of tokens | s1; Han 2024 (b02, c13) | E (K14) |
| Hard truncation at tiny budgets loses accuracy | L1 vs s1 at 512 and 1,024 tokens: over 100% relative, 20-25 points absolute; log-linear slope 0.24 (L1) vs 0.37 (s1) | Aggarwal 2025 (a18, b19) | S (different base models) |
| Training for random cut points | AnytimeReasoner (1.5B): AIME24 base 16.3, GRPO 19.0, AR-base 21.9, AR-linear 22.3, AR-uniform 22.9; 5-benchmark mean at 8000 tokens 39.8 / 43.0 / 44.9 / 46.0; 40,315 problems, under 10% extra cost | Qi 2025 (a17, a25) | S, single run (K15) |
| Protect the solution segment | E1-Math-1.5B AIME24 35.0 vs L1-Max 27.1, L1-Exact 24.2, unconstrained 41.0 | Xu 2025 (c14) | S |
| Cut-and-answer on untrained models | quality rises with later cut; reasoning leaks into answers (up to 10x longer); panic under speed-up causes over 90% of new errors | Wu 2026 (d09) | S (K16) |
| Per-stage budgets beat a global cap | E3: MATH-500 5.16 to 5.89 (+14.1%); NaturalInstructions 1.61 to 2.00 (+24.2%); TravelPlanner up to +33%; schedule shape differs by a few percent | Plan and Budget 2026 (d08) | S, own metric (K27) |
| Where to spend rollouts | 5 extra test-writing rollouts +1.7 points vs editing rollouts 16 to 21 +0.8 (SWE-bench Verified) | R2E-Gym (d06) | S |
| Skip thinking at low budgets | ACM 23 at 700 tokens: NoThinking 51.3 vs Thinking 28.9 | Ma 2025 (c20) | S (K17) |
| Offline compute | about 5x less test-time compute at equal accuracy; +13% and +18% accuracy when sleep-time compute scaled; 2.5x lower cost per query amortized | Lin 2025 sleep-time (b22) | S (K20) |
| Expert quality under time cuts | blunders per 1,000 moves 5.02 / 6.85 / 7.63 (classical / rapid / blindfold), N=23 grandmasters | Chabris & Hearst 2003 (d20) | S (K32) |
| Agent tasks: best-of-N beats tree search; reflection every step did not help | GAIA 165 tasks, GPT-4.1: baseline 55.76; BoN about +8; beam and DVTS about baseline; reflect every step 55.15 | OPPO 2025 (d04) | S, single run |
| Regret over the budget curve as a metric | later episodes do not improve and sometimes fall in 41-45 episode problems; MRT about 1.5x token efficiency vs GRPO, 5x vs base | Qu 2025 (d13) | S (K26) |
| Illusion of Thinking collapse | three regimes; collapse at high complexity | Shojaee 2025 vs Lawsen 2025 (b12, b13) | C (K19) |

---

## 4. Mechanisms and models

Each item is written so it can be coded.

### 4.1 Performance profile
- Definition: Q(t) is the expected quality of the answer after t units (tokens or calls). Estimate it empirically. Run the procedure on n items. At each budget point b in a grid, cut the run, force an answer, score it. Average. Zilberstein used curve fitting; Boddy and Dean used 1 - e^(-t).
- Three versions: unconditional Q(b); conditional on input quality (for chained stages); dynamic, conditional on the current quality state (a Markov table). The dynamic version predicts better, at the cost of a bigger table.
- For our agent: five or more grid points per item class (K26 test). Report area under the curve and the share of non-concave items.

### 4.2 Best-so-far register (makes the output monotone)
```
best = None
loop:
    cand = attempt(...)
    if check(cand) is available:
        if best is None or score(cand) > score(best): best = cand
    else:
        best = best or cand        # no check: keep first natural answer (S4 rule)
    if stop_rule(...): break
return best
```
- Needs recognizable quality. With no check, "best" is undefined and the register just holds the first answer. This is why the checks in G3 matter.

### 4.3 Contract-to-interruptible by doubling
```
b = b0; best = None
while time_left:
    run = attempt(budget=b)            # contract run, hard cap b
    if run finished and check(run): best = better(best, run)
    b *= 2
return best
```
- Worst case: interrupted at t, last finished run has budget at least t/4, so quality at 4t at least that of a known-budget run at t. Waste is bounded by about 2x the last budget plus the sum of earlier ones.
- Not tested on LLMs (K31). Real waste is unmeasured. Do not assume the factor-4 bound is the real cost.

### 4.4 Stop rules, in order of how much evidence they have
1. **Hard cap plus banked answer.** Always safe. Pair with 4.6.
2. **Agreement stop.** Draw answers one by one or in windows. Stop when the leading answer cannot lose.
   - ESC: window of 5 (8 for MATH), max 30 samples, stop when a whole window gives one answer.
   - Adaptive-Consistency: Beta posterior on the leader's share; stop when the probability the leader stays in front passes a threshold. Code: cluster by executed output.
   - DeepConf consensus stop: tau = 0.95 on the vote share.
   - Caveat: agreement of one model's samples is a hint, not proof (G4). It is a stop rule here, not a correctness claim.
3. **Check-passes stop.** Stop at the first answer that passes a real check not fitted to the answer (G3). Strongest on code (S*, R2E-Gym).
4. **Self-confidence stop (DEER).** At thought-switch points ask for a trial answer, read the confidence, exit above a threshold. Needs per-model thresholds. Too low a threshold gives sharp accuracy drops. Hurts on code where trial answers are long. Weaker than a real check by design (G5, G8).
5. **Probe stop.** Train a probe on hidden states. Not available for API models.
6. **Stability measure (Certaindex).** Share of unchanged intermediate answers across probes. Use as a difficulty signal. Contested (K30).
7. **Myopic marginal gain.** Stop when the expected gain of the next step is below its cost. Optimal only for concave profiles with convex cost (Theorem 5). Unsafe on plateau-then-jump curves.
8. **Non-myopic monitoring** (Hansen and Zilberstein). Dynamic programming over the dynamic profile. Not applied to LLMs. Certaindex per-step curve fitting beat a static threshold by only 1-3.4 percent of tokens, so the extra machinery may not pay.

### 4.5 Deliberation scheduling across stages
- Greedy marginal gain (Dean and Boddy): at each slice give compute to the stage or item with the largest expected marginal gain. Optimal only for diminishing-returns profiles.
- Exact split is NP-complete in general (Theorem 1). Use heuristics.
- Empirical options: global cap; equal shares; front-loaded decay (Plan and Budget, schedule shape within a few percent, front-loaded best on planning); learned profile.
- A tested shift: moving rollouts from the solver stage to the test-writing stage doubled the marginal gain (R2E-Gym, +1.7 vs +0.8).

### 4.6 Reserve a solution segment
- Split the budget: thinking budget T and answer budget A (15-20 percent is our proposed start, not a measured value). When T is used up, cut and force an answer from the partial trace.
- Cut traces leak reasoning into the answer (up to 10x longer answers). So count the answer segment in the budget and cap it.
- E1 reports the benefit when the model is trained for it; AnytimeReasoner trains the same idea with random cut points. A scaffold can only do the reservation, not the training.

### 4.7 Difficulty-aware routing (Snell)
- Estimate difficulty from the model's own pass rate in bins (oracle bins from ground truth gave larger gains than predicted bins). Easy: sequential revision or best-of-N at high budget. Hard: beam search or parallel search, or give up early. Predicted-difficulty gains shrink at higher budgets.
- Cheap probes: 3-sample answer stability; learned predictors (SelfBudgeter 61 percent length cut, trained by RL, math only).

### 4.8 Parallel vs one long trace
- Parallel k independent short attempts with a check or vote; "short-m@k": start k, halt after the first m finish, vote among them (up to 40 percent fewer tokens).
- Extend one trace only if forced continuation has been shown, on our model, to turn wrong answers right more often than the reverse (K28 test).

### 4.9 Sleep-time compute
- Before the query arrives, precompute notes on stable context. Gives about 5x less test-time compute at equal accuracy when queries share context and are predictable. Maps to the memory part of the schema.

---

## 5. What holds up

### 5.1 Holds, with several sources
- **A best-so-far register with a real check is the safe core** (K01). Theory plus code evidence (S*, R2E-Gym, Large Language Monkeys all gain only where a check or verifier exists).
- **LLM quality is not monotone in thinking** (K05). Three independent sources: Ghosal (rise-then-fall), Gema (fall on built tasks), Wu (inverted U). Zeng adds that revision flips right to wrong.
- **Easy items are overthought and answers appear early** (K07). Chen, Su, Answer Convergence, Certaindex, Hassid, Lanham (task-specific flatness: early-answering area over curve 0.02 to 0.44).
- **Training-free early exit saves tokens** (K08). Agreement-based exits have the most support: Adaptive-Consistency, ESC, DeepConf. Their savings are 15 to 84 percent of samples or tokens with accuracy within about 0.2 to 0.4 points.
- **Plateaus and late jumps exist on agent and code tasks** (K26): coverage plateau past N=32 for QwQ-32B-Preview; verifier plateaus near 43 percent then 51 percent with a hybrid signal; later reasoning episodes sometimes lower accuracy. So myopic stopping is unsafe (K04).
- **Prompted budgets are not controls** (K14). s1 token-conditional control 40 percent; TALE shows a floor below which the budget is ignored.
- **Reserving the answer segment is cheap and useful** (K16), with the leak caveat.

### 5.2 Failures, contests and moderators
- **Parallel vs sequential (K12, K28).** Ghosal says parallel wins. s1 says sequential wins. Gap search explains the split but did not settle it. Zeng: on untuned QwQ, R1-Distill and LIMO, Wait extension turns right answers wrong more than the reverse. s1 fine-tuned its model on 1k traces for continuation. Balachandran: sequential wins only with an informative critic (TSP-easy: GPT-4o 42 to 95 percent), parallel on AIME 2025. Moderators: training for continuation, critic quality, task type.
- **Illusion of Thinking vs Lawsen (K19).** Collapse at high complexity may be an output-limit and impossible-instance artifact. Lawsen's evidence is preliminary. Neither side is settled. Do not build on the collapse claim.
- **Certaindex (K30).** Original authors: 9-52 percent token savings with no loss. Another group: 81.44 vs 89.76 percent on MATH-500 (8 points lost). Contested.
- **Snell's 4x saving** not reproduced outside MATH and PaLM 2. Difficulty must be predicted, and prediction costs compute.
- **Noise (K29).** Hochlehnert: seed SD 5-15 points on 30-item sets; most RL gains over R1-Distill vanished under paired tests; SFT gains held. No one found who replicated s1 budget forcing or AnytimeReasoner directly. Their 3-7 point gains are single-run and unconfirmed.
- **Self-confidence stop (K09).** Single-source on code harm; the DEER versus agreement versus check comparison at equal tokens does not exist (K24).
- **Inverse scaling prevalence (K06).** Built adversarially. Bounds the failure, does not give its rate. Opus 4 figures differ by task (85-90 percent vs about 80 percent). The R1 70 to 30 percent figure is a different setting (five distractors, natural overthinking), not a fixed-length curve.
- **Early rise as variance (K21).** Ghosal's toy model says the first gain is added output variance. Single source.
- **Weak comparisons.** AnytimeReasoner 32.7 vs 30.3 on AIME24 in a second table compares against a number reported by another paper; treat as weak. L1 vs s1 compares different base models, not a clean replication.

### 5.3 What worked, what did not
- Worked: agreement stop; check-based stop on code; hybrid verifiers; per-stage budgets; hard cap plus forced answer; NoThinking plus many samples at tiny budgets (700 tokens); offline precompute with shared context.
- Did not: model-written tests alone (no gain over public tests); reflection at every step on GAIA (55.15 vs 55.76); beam search and DVTS on GAIA (about baseline); Wait extension on untuned models; prompt-only token limits; verifier-free selection beyond about 100 samples; the first-answer trimming on MATH500 (hurts the hard set; reflection recovers part).

### 5.4 Human evidence
Thin. Saturating speed-accuracy curves in simple choices (simulation numbers only) and a one-third blunder rise for grandmasters under rapid play. No novice comparison. No test of aspiration adjustment against anytime stopping (K32).

---

## 6. Language models

### 6.1 How they behave on time-quality tasks
- **Easy items.** Reasoning models over-spend by large factors: 1,953 percent more tokens than conventional models on "2+3". First round is right in over 92 percent of cases and uses under 60 percent of the tokens. Median 830 of 2,700 tokens is enough on AMC23 (Certaindex probe).
- **Hard items.** Models underthink hard problems and overthink easy ones (Su). Optimal chain length rises with difficulty and falls with capability (14 steps at 1.5B, 4 at 72B).
- **Curve shape.** Not concave. Rise then fall (Ghosal: 82.2 to 87.3 then 70.3 percent). Falls on distractor tasks (Opus 4 from near 100 to 85-90 or about 80 percent; R1 70 to 30 percent). Context overflow at the top (s1: 12 of 30 questions at 512 steps). Plateaus past N=32 in coverage (QwQ-32B-Preview).
- **Within one question**, shorter chains are right more often (up to 34.5 percent more accurate than the longest). Correct solutions are shorter than wrong ones.
- **When cut.** Quality rises with later cuts, so the models are anytime in the loose sense. But answers leak reasoning (up to 10x longer), and "speed up" requests cause panic (over 90 percent of new errors). Open weight models only (Qwen3-8B, GPT-OSS-20B, Magistral-Small).
- **Truncated chains** are task-specific. Early-answering area over the curve ranges 0.02 to 0.44 across multiple-choice tasks (175B-class 2023 model).

### 6.2 What changed behaviour, by how much
| Intervention | Result | Needs training? |
|---|---|---|
| Agreement stop (ESC, Adaptive-Consistency, DeepConf) | 15-84% fewer samples or tokens, accuracy within about 0.4 points | no |
| DEER confidence exit | 19.1-80.1% shorter chains, +0.3 to +5.0 accuracy | no |
| Hidden-state probe exit | about 24% fewer tokens at equal accuracy (MATH) | probe only |
| Parallel with vote vs Wait extension | up to 20-22% better at 16K tokens (Ghosal) | no |
| short-1@k parallel halting | up to 40% fewer thinking tokens | no |
| Compute-optimal by difficulty | up to 4x less compute than best-of-N (PaLM 2, MATH) | difficulty probe |
| Per-stage budget vs global cap | +14% to +33% E3 | no |
| Hybrid verifier on agent runs | 43.7 to 51.0% (SWE-bench Verified) | verifiers |
| Budget forcing (s1) | AIME24 50.0 to 56.7 | fine-tuned on 1k traces |
| AnytimeReasoner | AIME24 19.0 to 22.9; 5-benchmark mean 43.0 to 46.0 | RL |
| L1 vs s1 at 512-1,024 tokens | +20-25 points absolute | RL |
| E1 | AIME24 35.0 vs 27.1 (L1-Max) | RL |
| Self-training on easy items (Chen) | -48.6% tokens on MATH500 (QwQ), accuracy kept | fine-tune |
| SelfBudgeter | -61% length, accuracy kept | RL |
| NoThinking plus samples at 700 tokens | 51.3 vs 28.9 (ACM 23) | no |
| Sleep-time compute | about 5x less test-time compute | no |

### 6.3 Reliability of the LLM evidence
- Mostly math. Mostly 1.5B to 32B models. AIME24 has 30 items. Many cells are single runs with the authors' own baselines.
- Few agent-task studies: OPPO GAIA (165 tasks, single runs), R2E-Gym (500 items), S* (LiveCodeBench). Code agreement evidence is only MBPP, Adaptive-Consistency code sets, and executed-output clustering.
- No study of explicit performance-profile budgeting for LLM agents (c26). No doubling-budget study. No non-myopic monitoring study.

---

## 7. What our agent should take

Status: **[E]** established, **[S]** single source, **[C]** contested. Schema parts: G guardrail, S state, O operator, memory.

### Add now (established)

| # | Item | Part | Status | Evidence |
|---|---|---|---|---|
| 1 | Keep a best-so-far register. Update it only when a candidate passes a check that is not fitted to the answer. With no check, hold the first natural answer. Submit the register at any cut. (Reinforces G6, ties to G3.) | G6, G3, S4 | [E] | K01; a04, c03, a21, d05, d06 |
| 2 | Hard cap on tokens per attempt, enforced by code. Never rely on a prompted token limit. | G12, G11 | [E] | K14; a16, b02, c13, a18 |
| 3 | Reserve a separate answer segment (start at 15-20 percent of the attempt budget). If the thinking cap is hit, cut and force an answer from the partial trace. Count and cap the answer segment because cut traces leak reasoning. | G6, S3/S4 | [E] | K16; c14, a17, d09, d13 |
| 4 | Stop trial attempts on agreement or a passing check, not a fixed count. Window of 5, tau 0.95 as the starting rule. Treat agreement as a stop rule only, never as proof (G4). | G6, G12, S3 | [E] | K23, K08; d01, d02, d03, d16 |
| 5 | On easy items, stop at the first verified answer. | G11, G12, S0 | [E] | K07; a20, b08, b07, c17 |
| 6 | Do not use a single marginal-gain stop rule. Use hard cap plus check as the base rule. Myopic stopping is optimal only for concave profiles. | G12, G6 | [E] | K04; a09, a21, a22, c15, d06, d13, d04 |
| 7 | Do not extend one trace with "Wait" or similar on untuned models without first measuring flips. | G11, S5 | [E] | K28; d14, d07, d12 |
| 8 | On code and software items use real execution as the anytime signal. Do not trust model-written tests alone. | G3, S4 | [E] | K25; d05, d06 |
| 9 | Assume quality can fall with more thinking. Keep the best-by-check candidate, not the latest. | G1, G6 | [E] | K05; a21, a22, b04, b05, b06, c15, b10 |
| 10 | Plot and log quality at several budget points per item class as part of the bench. | G7, S0 | [E] | K26; d05, d06, d13, d04 |

### Test first

| # | Item | Part | Status | Evidence |
|---|---|---|---|---|
| T1 | Agreement stop vs real-check stop vs model self-confidence (DEER-style), three arms at equal tokens | G6 | [S] (K24 open) | d01, d15, d16 |
| T2 | Doubling budget schedule b, 2b, 4b with banked best-by-check vs one known-budget run | G6, G12 | [S] theory only (K02, K31) | a06, a07 |
| T3 | Per-stage budgets across S1-S9: global cap vs equal shares vs front-loaded vs moving 20 percent from generation to checking | G12, S0-S9 | [S] (K27) | d08, d06 |
| T4 | Cheap difficulty probe (3-sample stability) to route budget by bin | G12, S0 | [C] (K30) | d16, d08, a14 |
| T5 | One long trace vs 1, 2, 4 independent attempts at equal tokens, by difficulty bin | G11, G4 | [C] (K12) | a22, b03, d07, d12, d14 |
| T6 | Low-budget NoThinking plus N samples with a check | G11, G12 | [S] (K17) | c20 |
| T7 | Sleep-time precompute of stable-context notes | memory | [S] (K20) | b22 |
| T8 | Share of real items that show longer-is-worse behaviour | G1 | [S] (K06) | a21, b05 |
| T9 | Non-myopic monitor (dynamic profile) vs threshold | G6, G12 | [S] open (K31) | a13, d16 |
| T10 | Seed and sample-size rules for every test above | G7 | [S] (K29) | d11 |

---

## 8. Concrete tests on our bench

All arms get the same total token budget, counted end to end including setup, trial answers, checks and probes (G7). Use at least 100 items per cell, at least 10 seeds, paired tests. A 30-item cell cannot show a 3-7 point gain (K29).

| Test | Item type | Arms (equal tokens) | Metric | Expected effect |
|---|---|---|---|---|
| B1: submit-best vs submit-latest | held-out items with a check; random cut points | latest attempt; best-by-check | accuracy at cut; area under accuracy-vs-tokens curve | best-by-check higher on items where quality falls; equal elsewhere |
| B2: stop rule shootout | math; code with tests; multi-step items | fixed count; self-confidence stop; agreement stop (window 5, tau 0.95); check-pass stop | accuracy per 1,000 tokens; tokens used | agreement and check beat fixed count by 15-50 percent tokens at equal accuracy; self-confidence worse on code |
| B3: doubling schedule | all item types | one run at full budget B; runs at B/4, B/2, B (banked best-by-check); interrupted at random t | accuracy at random interrupt; waste ratio (tokens spent / tokens of final run) | doubling better under random interrupt; waste below the 4x worst case |
| B4: reserved answer segment | items cut at random points | no reservation; 10, 15, 20, 30 percent reserved | accuracy of the forced answer; answer length | reservation helps at cuts; an optimum exists; answer length capped |
| B5: stage budgets | full S1-S9 pipeline | global cap; equal shares; front-loaded; 20 percent moved from S3 to S4 checking | accuracy; tokens | per-stage beats global by a few to 14 percent; check-heavy shift helps on code |
| B6: difficulty routing | mixed-difficulty set | uniform budget; routed by 3-sample stability bin | accuracy at equal total tokens | gain if per-bin optimal budgets differ by 2x or more |
| B7: parallel vs sequential | difficulty-binned items | 1 long trace; 2 attempts; 4 attempts; long trace plus forced Wait | accuracy by check; correct-to-wrong vs wrong-to-correct flips | parallel wins on hard/untuned; sequential only with informative critic |
| B8: concavity audit | 5 budget points per item class | none (measurement) | share of items with non-concave curves; area under curve | non-trivial share non-concave, so myopic stop rejected |
| B9: low-budget no-think | short-budget slice (about 700 tokens) | one thinking run; N no-think samples with a check | accuracy | no-think plus samples wins at low budget |
| B10: sleep-time notes | items sharing context | no precompute; precomputed notes | test-time tokens at equal accuracy | about 5x fewer test-time tokens if context shared |
| B11: longer-is-worse prevalence | real items | 4 thinking budgets per item | share of items with accuracy falling at higher budget | measures how often G1/G6 save us |

---

## 9. What does not transfer, and why

- **Concave-profile theorems (Theorem 5, Dean and Boddy greedy).** LLM curves are not concave. Plateaus, rise-then-fall and late jumps break the premise.
- **The monotonicity property.** Raw LLM thinking violates it. It only holds after we add best-so-far with a check.
- **Factor-4 bound for doubling.** It is a worst case for an abstract contract algorithm. LLM attempts are stochastic and restarts do not reuse work, so real cost is unknown. It also assumes quality of a run depends on its budget only.
- **Tree-structured optimal composition.** Our stages share sub-results (the problem restatement feeds many states), which is exactly the case where the optimal result fails.
- **Performance profiles learned offline.** They shift with distribution. Our item classes change, so profiles must be re-measured per class.
- **RL-trained anytime models (AnytimeReasoner, L1, E1, SelfBudgeter).** We use a scaffold, not training. Only the idea (reserve the answer, cut anywhere) carries.
- **s1 budget forcing.** Needs a model fine-tuned on 1k traces for continuation. Untuned models get hurt (Zeng).
- **Probe-based exit.** Needs hidden states. API models do not provide them.
- **Inverse-scaling tasks.** Adversarially built. Good for bounding the failure, bad for prevalence.
- **Human satisficing.** The aspiration-adjustment link is unverified, and humans stop on feeling, not on a code check. G10 says reasoning text is not evidence.
- **Math-heavy results.** Most evidence is math at 1.5B-32B on 30-item sets. Agent tasks may differ in curve shape.
- **Self-confidence signals.** G5 and G8: the model does not grade its own answer without a check.

---

## 10. Open questions

1. Does agreement or real-check stopping beat model self-confidence stopping at equal tokens outside math (K24)?
2. How often are quality-vs-token curves on agent tasks non-concave, and how much does that cost a myopic rule (K26)?
3. Where is the crossover between k short attempts and one long trace, by difficulty and model? Why do Ghosal and s1 disagree for trained models (K12)?
4. What is the real waste of a doubling schedule for LLMs (K31)?
5. How should a staged scaffold split a fixed budget: fixed shares, greedy marginal gain, learned profile (K27)?
6. Can a cheap probe predict per-item budget well enough to realise a Snell-size saving outside MATH (K30)?
7. What does a reserved final-answer segment do on non-trained models for a range of fractions (K16)?
8. Does Hansen-Zilberstein non-myopic monitoring beat threshold rules for LLM reasoning (K31)?
9. How does accuracy vary with allowed time in expert and novice human decisions, and does aspiration adjustment match anytime stopping (K32)?
10. Do the AnytimeReasoner and s1 gains hold across seeds, with sets larger than 30 items (K29)?
11. What does Simon (1955/56) actually say about aspiration adjustment over time? Not opened.
12. Is the early rise in accuracy real reasoning or added output variance (K21)?

---

## 11. Sources

[V] opened and read this session or in cross-check. [M] snippet or recalled only.

**Classical theory**
- [V] Dean and Boddy (1988) An analysis of time-dependent planning. https://cdn.aaai.org/AAAI/1988/AAAI88-009.pdf (a01-a03)
- [V] Zilberstein (1996) Using anytime algorithms in intelligent systems, AI Magazine. https://ojs.aaai.org/aimagazine/index.php/aimagazine/article/download/1232/1133 and https://www.cs.umass.edu/~shlomo/papers/Zaimag96.pdf (a04-a06, a09, a10, c01-c03)
- [V] Zilberstein and Russell (1996) Optimal composition of real-time systems, AIJ. https://aima.eecs.berkeley.edu/~russell/papers/aij-anytime.pdf (a07, a08)
- [V] Hay, Russell, Tolpin, Shimony (2012) Selecting computations. https://arxiv.org/abs/1207.5879 (b23)
- [M] Simon (1955) A behavioral model of rational choice, QJE 69; Simon (1956). https://doi.org/10.2307/1884852 (a11, b28, c05)
- [M] Russell and Wefald (1991) Do the right thing. https://mitpress.mit.edu/9780262181440/do-the-right-thing/ (a12, b27)
- [M] Hansen and Zilberstein (2001) Monitoring and control of anytime algorithms. https://doi.org/10.1016/S0004-3702(00)00068-0 (a13, c24; the DOI differs between files, check before citing)
- [M] Horvitz (1987, 1990) flexible computation, as cited in Zilberstein. https://www.cs.umass.edu/~shlomo/papers/Zaimag96.pdf (c25)

**LLM: scaling, budget control, curve shape**
- [V] Snell, Lee, Xu, Kumar (2024) Scaling LLM test-time compute optimally. https://arxiv.org/abs/2408.03314
- [V] Brown et al. (2024) Large Language Monkeys. https://arxiv.org/abs/2407.21787
- [V] Muennighoff et al. (2025) s1. https://arxiv.org/abs/2501.19393
- [V] Qi et al. (2025) AnytimeReasoner. https://arxiv.org/abs/2505.13438
- [V] Aggarwal and Welleck (2025) L1. https://arxiv.org/abs/2503.04697
- [V] Xu et al. (2025) Elastic Reasoning (E1). https://arxiv.org/abs/2505.05315
- [V] Han et al. (2024) Token-Budget-Aware LLM Reasoning (TALE). https://arxiv.org/abs/2412.18547
- [V] Gema et al. (2025) Inverse scaling in test-time compute. https://arxiv.org/abs/2507.14417
- [V] Ghosal et al. (2025) Does thinking more always help? https://arxiv.org/abs/2506.04210
- [V] Wu et al. (2025) When more is less: CoT length. https://arxiv.org/abs/2502.07266
- [V] Wu et al. (2025) Inference scaling laws. https://arxiv.org/abs/2408.00724
- [V] Shojaee et al. (2025) The Illusion of Thinking. https://arxiv.org/abs/2506.06941
- [V] Lawsen (2025) The Illusion of the Illusion of Thinking. https://arxiv.org/abs/2506.09250
- [V] Chen et al. (2024) Do NOT think that much for 2+3=? https://arxiv.org/abs/2412.21187
- [V] Su et al. (2025) Between underthinking and overthinking. https://arxiv.org/abs/2505.00127
- [V] Zeng et al. (2025) Revisiting the test-time scaling of o1-like models. https://arxiv.org/abs/2502.12215
- [V] Hassid et al. (2025) Don't overthink it. https://arxiv.org/abs/2505.17813
- [V] Balachandran et al. (2025) Inference-time scaling for complex tasks. https://arxiv.org/abs/2504.00294
- [V] Qu et al. (2025) Optimizing test-time compute via meta reinforcement fine-tuning (MRT). https://arxiv.org/abs/2503.07572
- [V] Wu et al. (2026) Are large reasoning models interruptible? https://arxiv.org/abs/2510.11713
- [V] Lanham et al. (2023) Measuring faithfulness in chain-of-thought. https://arxiv.org/abs/2307.13702
- [V] Hochlehnert et al. (2025) A sober look at progress in language model reasoning. https://arxiv.org/abs/2504.07086
- [V] Lin et al. (2025) Sleep-time compute. https://arxiv.org/abs/2504.13171
- [V] Ma et al. (2025) Reasoning models can be effective without thinking. https://arxiv.org/abs/2504.09858

**LLM: stopping, selection, allocation**
- [V] Yang et al. (2025) DEER. https://arxiv.org/abs/2504.15895
- [V] Answer convergence as a signal for early stopping (2025). https://arxiv.org/abs/2506.02536
- [V] Zhang et al. (2025) Reasoning models know when they're right (probing). https://arxiv.org/abs/2504.05419
- [V] Li et al. (2024) Early-stopping self-consistency (ESC). https://arxiv.org/abs/2401.10480
- [V] Aggarwal et al. (2023) Adaptive-Consistency. https://arxiv.org/abs/2305.11860
- [V] Fu et al. (2025) Deep Think with Confidence. https://arxiv.org/abs/2508.15260
- [V] Fu et al. (2025) Certaindex / Dynasor. https://arxiv.org/abs/2412.20993
- [V] Zhang et al. (2024) Optimized sample compute allocation (OSCA). https://arxiv.org/abs/2410.22480
- [V] Li et al. (2026) SelfBudgeter. https://arxiv.org/abs/2505.11274 (abstract and parts only)
- [V] Lin et al. (2026) Plan and Budget. https://arxiv.org/abs/2505.16122
- [V] Manvi, Singh, Ermon (2024) Adaptive inference-time compute. https://arxiv.org/abs/2410.02725 (first page only)
- [M] Zhang et al. (2025) AdaptThink. https://arxiv.org/abs/2505.13417 (introduction only)

**LLM: code and agents**
- [V] Li et al. (2025) S*. https://arxiv.org/abs/2502.14382
- [V] Jain et al. (2025) R2E-Gym. https://arxiv.org/abs/2504.07164
- [V] OPPO AI Agent Team (2025) Scaling test-time compute for LLM agents. https://arxiv.org/abs/2506.12928

**Human**
- [V] Heitz (2014) The speed-accuracy tradeoff. https://pmc.ncbi.nlm.nih.gov/articles/PMC4052662/ (first 100,000 of 228,000 characters)
- [V] Chabris and Hearst (2003) Visualization, pattern recognition, and forward search. https://www.chabris.com/Chabris2003.pdf

## Source audit (2026-11-01)

Fresh auditors re-opened the sources of 12 established claims: 5 confirmed as written, 7 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **C12.06-K01** (now single-source: the sources are not independent). Zilberstein (1996) states exactly this (monotonicity guaranteed by returning best result so far when quality is recognizable); the two Zilberstein entries are the same paper and the other listed papers do not address the guarantee, so it rests on one source, though the claim is close to definitional.
- **C12.06-K04** (reworded: the sources support less). Zilberstein's Theorem 5 states myopic value-of-computation monitoring is optimal when the profile is increasing and concave-down and time cost is increasing and concave-up (a sufficient condition), not 'only' then; the LLM non-concavity evidence is a synthesis, not a measured concavity test. Corrected claim: Zilberstein's Theorem 5 shows myopic value-of-computation stopping is optimal when the performance profile is increasing and concave-down and the cost of time is increasing and concave-up; LLM quality-vs-thinking curves are often non-concave (rise then fall), so a single marginal-gain stop rule is not guaranteed safe.
- **C12.06-K08** (reworded: the sources support less). Numbers match (DEER 19.1-80.1% shorter chains with +0.3 to +5.0% accuracy, ESC -34% to -84% samples, probe -24% tokens), but the hidden-state probe is a trained probe, so it is not training-free, and ESC saves samples rather than chain tokens. Corrected claim: Early exit and early stopping save compute at little or no accuracy cost: training-free DEER cuts chains by an average 19.1-80.1% with +0.3 to +5.0% accuracy; training-free ESC cuts 34-84% of samples with comparable accuracy; a trained hidden-state probe used as an exit rule cuts 24% of tokens with no performance loss.
- **C12.06-K14** (reworded: the sources support less). s1 shows token-conditional prompting gave only 40% control for its own fine-tuned model (hard truncation/budget forcing gave 100%), so '40 percent' is the failure of prompting, not of truncation, and 'current models' overgeneralises one model; L1's 20-25 point absolute gain over s1 at 512-1024 tokens is correct, and TALE reports prompt budgets do shrink CoT. Corrected claim: In s1's fine-tuned model, a prompt-stated token limit controlled length only 40% of the time (token-conditional control, Table 3) while hard truncation via budget forcing gave 100% control; but hard truncation loses accuracy at small budgets (L1, a length-trained model, is 20-25 points absolute better than s1 at 512-1024 tokens).
- **C12.06-K18** (now single-source: the sources are not independent). Wu et al. (2502.07266) states the inverted U and 14 steps at 1.5B to 4 at 72B (Qwen2.5 series), but the second line is the same paper and Su et al. only corroborates overthinking easy problems, so the specific claim rests on one study.
- **C12.06-K23** (number corrected). ESC on MBPP (max 30 samples) used 6.79 samples, a reduction of 23.21 samples (about 77%), not -23%; other figures (AC 2.4-3.8x, ESC -34% to -84%, DeepConf consensus stop -52.8% at K=512 with no accuracy change) match. Corrected claim: Stopping when independent trial answers agree saves 15-84 percent of samples or tokens at no or tiny accuracy cost: Adaptive-Consistency 2.4-3.8x fewer samples, ESC -34% to -84%, DeepConf consensus stop -52.8% tokens at K=512 with identical accuracy. Outside math the evidence is thin: MBPP 23.21 fewer samples out of 30 (about -77%, ESC), code +0.4% accuracy at 2.4x (Adaptive-Consistency), GPQA-D only multiple choice.
- **C12.06-K28** (reworded: the sources support less). Zeng et al. find failed revisions exceed successful ones only for QwQ and R1-Distill-1.5B; for R1-Distill-32B/14B and LIMO successful revision was higher (though plateauing after about 10 steps), so 'net harmful for QwQ, R1-Distill and LIMO' is too broad. Corrected claim: Extending one trace with Wait or Alternatively on untrained reasoning models gives weak, model-dependent sequential gains: revision flipped correct answers to wrong more often than the reverse for QwQ and R1-Distill-1.5B (successful revisions were under 10% everywhere), while R1-Distill-32B/14B and LIMO had higher successful than failed revision rates that plateaued after about 10 steps; correct solutions are shorter than wrong ones. The s1 result (sequential extension helps) holds for a model fine-tuned on 1k traces, so the Ghosal vs s1 conflict may be partly explained by training for continuation and critic quality.
- **C12.06-K02** (now single-source: only one opened source, code check).
