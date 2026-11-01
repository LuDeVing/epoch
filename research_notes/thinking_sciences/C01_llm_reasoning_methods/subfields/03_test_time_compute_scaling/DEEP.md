# Test-time compute scaling: deep document

*Subfield C01.03. Sources: evidence_a-d.jsonl (a01-a30, b01-b26, c01-c25, d01-d18), claims.jsonl (K01-K27), critique.md. Status marks: [E] established, [S] single-source, [C] contested. Evidence ids in brackets. Most evidence is math and code with checkable answers; read every result with that in mind.*

## 1. What it is

Test-time compute scaling means spending more tokens, samples or search steps on one problem at inference, with no change to the model weights. The model is fixed. The budget per problem is the knob.

There are four ways to spend the budget.

1. **Think longer in one chain.** Chain of thought, "Wait" appended, budget forcing, extended-thinking modes. This is "sequential" scaling.
2. **Sample many chains in parallel.** Majority vote (self-consistency), best-of-N with a verifier, coverage (any sample correct). This is "parallel" scaling.
3. **Search.** Beam search, lookahead, tree search (REBASE, DVTS) steered by a process reward model (PRM).
4. **Revise.** The model reads its earlier attempt (and maybe feedback) and writes a new one. This is also called sequential, but it means something different from "think longer".

Three things decide whether extra compute helps:

- **A proposer** that puts some probability on the right answer.
- **A selector or verifier** that can find the right answer among the candidates.
- **A difficulty match**: how much compute this problem needs. Too little fails. Too much wastes tokens and can lower accuracy.

For our agent this subfield is the home of S0 (the gate that picks a mode) and G12 (spend by difficulty). It also bears on G11 (think briefly by default, prefer several short attempts), G5/G6 (code selects; verifiers are imperfect), S3 (generate several attempts) and S7 (select).

Scope note: the survey arXiv 2501.02497 (Ji et al. 2025) [a30, b19, c09; front matter only, no numbers] organises the field as System-1 (test-time adaptation) and System-2 (repeated sampling, search, self-correction). We cover System-2 only. The efficiency survey 2503.16419 [c21] is also taxonomy only.

## 2. History and theories in depth

**Before LLMs.** Jones (2021) measured AlphaZero on Hex [a18, c01]. Each extra 10x of train compute let the system drop about 15x of test-time search compute at equal strength, down to a floor of single-node tree search. The trade is a straight line in log-compute. One game only; the author says it may not generalise. K18 [S].

**Verifiers and chain of thought (2021-2023).**
- Cobbe et al. (2021) [a19, c02]: sample 100 solutions on GSM8K, rank with a trained verifier. The gain matches about a 30x model-size increase over fine-tuning (GPT-3 6B and 175B). Verifiers did not help at small data sizes.
- Wei et al. (2022) [a21]: chain of thought. PaLM 540B on GSM8K goes from 17.9% to 56.9% (+39.0). It appears only at large scale.
- Wang et al. (2022/23) [a20, b10, c03]: self-consistency. With about 40 paths: GSM8K +17.9, SVAMP +11.0, AQuA +12.2, StrategyQA +6.4, ARC-challenge +3.9. Weaker models gained +3 to +6 (UL2-20B) vs +9 to +23 (LaMDA, PaLM-540B).
- Lightman et al. (2023) [a22]: process supervision. Best-of-1860 on a MATH subset: PRM 78.2%, outcome reward model 72.4%, majority vote 69.6%.

**Scaling laws for inference (2024).**
- Brown et al. "Large Language Monkeys" [a07-a10]: coverage grows roughly log-linearly in samples, fit by an exponentiated power law. Selection, not generation, is the bottleneck.
- Wu et al. [a11-a13]: inference scaling laws. Smaller model plus better search is Pareto-optimal until the small model saturates. Majority-vote accuracy converges to a fixed limit as samples go to infinity (Theorems 1 and 2).
- Snell et al. [a01-a06]: "compute-optimal" allocation per prompt. This is the formal root of G12.
- Chen et al. (2024) [b05]: more LLM calls are not all you need. Majority-vote accuracy can rise then fall.
- Levi (2024) [a29, b20]: a toy memorisation model that explains why pass@k is a power law. Toy only.
- Stroebl et al. (2024) [a28, b08, b24]: imperfect verifiers put a hard ceiling on resampling.

**Reasoning models and "long thinking" (late 2024 to 2025).**
- OpenAI's o1 (background, not in our evidence) started the wave. DeepSeek-R1 [a23, b18] showed RL with verifiable rewards makes thinking length grow on its own. R1-Zero AIME 2024 pass@1 rose from 15.6% to 77.9%; with majority voting 86.7%.
- s1 (Muennighoff 2025) [a14-a17]: budget forcing. Suppress the end-of-thinking token and append "Wait" to extend; force it to cut. Fine-tuned on only 1,000 traces.
- Then came the backlash: overthinking [a25], longer is not better [a26, a27], extended thinking is variance [b15, d01], inverse scaling [b07, d16], and the "illusion of thinking" debate [b16, c17, d11, d12].
- And the efficiency wave: early exit (DEER [c20, d14]), confidence filtering (DeepConf [d13]), answer convergence [d15], NoThinking [c18].

**Newer directions.** Learned difficulty prediction [d03, d04, d05]; weak-verifier ensembles [d07]; agentic scaling [d08, d09, d10]; sleep-time compute [c22, d17].

**Competing theories of why extra compute helps or fails.**
1. *Coverage view* (Brown, Levi): the base model already holds the answer with small probability; sampling finds it. Supported by Yue 2025 [b11]: at large k, base models match or beat their RL versions on pass@k.
2. *Selection bottleneck view* (Brown, Stroebl, Chen): gains are capped by the verifier's quality. Supported.
3. *Variance view* (Ghosal 2025 [b15, d01]): longer thinking raises output variance. Early on that looks like gain; later it lowers accuracy. A model, not a direct test.
4. *Self-revision harm view* (Zeng [a27, c11]): long chains contain more self-revisions, which often lower accuracy.
5. *Difficulty-match view* (Snell): the best mix of sequential and parallel depends on difficulty. Partly supported; the recipe does not transfer unchanged [a24].

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Coverage rises log-linearly with samples | Gemma-2B CodeContests 0.02% (1 sample) to 7.1% (10,000), over 300x; Llama-3-8B MATH 82.9% (100) to 98.44% (10,000) | Brown 2024 [a07, a09, b02] | [E] K01 |
| Weak model plus many samples plus a real verifier beats SOTA single shot | DeepSeek-Coder-V2 SWE-bench Lite 15.9% (1) to 56% (250); single-sample SOTA 43%. 5 cheap samples beat single GPT-4o/Claude 3.5 at over 3x lower cost | Brown 2024 [a08] | [E] K03 |
| Without ground truth, selection plateaus | MATH Llama-3-8B: vote/reward model 40.50% to 41.41% from 100 to 10,000 samples while coverage hits 98.44% | Brown 2024 [a09] | [E] K02 |
| Hybrid verifiers beat either alone on SWE-bench Verified | Generated tests alone ~42-43%; trained scorer alone ~42-43%; hybrid Best@26 51.0% (Best@16 49.4%); pass@1 34.4% | Jain 2025 R2E-Gym [d08] | [E] K03/K23 |
| Imperfect verifier caps resampling | HumanEval+/MBPP+, 200 samples per task; optimal attempts often under 10, sometimes 0 | Stroebl 2024 [a28, b24] | [E] K04 |
| Self-verifier error rates are high | GPT-4 Game of 24: 87.0% accuracy, 10.4% false positive, 20.7% false negative; false negatives 95.8% (Graph Coloring) and 97.09% (Mystery Blocksworld), row assignment partly uncertain | Stechly 2024 [d06] | [E] K22 |
| Self-correction without external signal does not help | GPT-3.5 CommonSenseQA 75.8 to 38.1 (round 1); GSM8K 75.9 to 74.7; GPT-4 GSM8K 95.5 to 89.0. Self-consistency at 9 responses 88.2 vs single 76.7 | Huang 2024 [d18] | [E] K22 |
| Compute-optimal allocation by difficulty | About 4x less compute than best-of-N (revisions and PRM search), MATH, PaLM 2-S*, oracle or verifier-predicted bins | Snell 2024 [a03, b01] | [E] K05 (one family) |
| FLOPs-matched: test-time vs 14x larger model | Test-time wins on easy and medium; pretraining wins on hardest and at high inference load. Figure labels +27.8, +21.6, +16.7, +11.8 down to -11.9, -37.2, -52.9 (figure text; bin mapping unchecked) | Snell 2024 [a06, b12] | [E] K07 |
| Best search method flips with model size and PRM | Small (<7B) best-of-N easy, beam hard; 7B-32B DVTS easy/medium, beam hard; 72B best-of-N everywhere. Llama-3.2-1B MATH-500: CoT 26.0, majority 39.0, compute-optimal TTS 66.2 | Liu 2025 [a24] | [C] K06 |
| Small beats large claims (1B > 405B, 7B > o1) | Author-reported, strong PRM, large N; no independent replication found | Liu 2025 [b04, c07] | [S] K08/K27 |
| Small model + search beats bigger model at equal FLOPs until saturation | Llemma-7B beats 34B up to 128 samples; 7B + REBASE beats 34B + majority vote at all budgets; REBASE 7x less compute than weighted voting on 7B (the "2x" in c06 is unverified) | Wu 2024 [a11, b03] | [E] K07 |
| Beam search over-optimises on easy items | Beam worse than best-of-N on MATH levels 1-2, better on 3-4 | Snell [a04, c23] | [E] part of K06 |
| Sequential vs parallel unresolved | s1: AIME24 50% to 57% with forcing. Ghosal: at 16K budget parallel ~22% above "Wait", ~47% above "Exact Thinking" (small distilled models). Sharma: sequential refinement wins 43 of 45 matched cells (instruct models, 4096 cap per chain). Zeng: parallel wins coverage at equal tokens (10 samples vs 40 revisions) | [a16, d01, d02, c25] | [C] K09 |
| Shorter chains are more often correct within a question | Shortest beats longest by up to 34.5 points, random by up to 18.8; short-1@k up to 40% fewer thinking tokens; short-3@k beats majority at all budgets, up to 33% less wall time | Hassid 2025 [a26, b09] | [E] K10 |
| More compute can lower accuracy | Ghosal Fig 2a: 82.2% to 87.3% (385 to 1,100 tokens) then 70.3% at 15,980 tokens. Claude Opus 4 near 100% to ~80% on misleading math. DeepSeek R1 natural: 70% to 30% with 5 distractors. Majority vote non-monotone in calls | [d01, b07, d16, b05] | [E] K11 |
| Reasoning models overspend on easy items | "2+3=?": 1,953% more tokens; first solution is 38.7% of tokens on ASDIV; first round correct in over 92%; SimPO alone cut 22.3% of tokens on MATH500; full pipeline 48.6% | Chen 2024 [a25, b17, c10] | [E] K12 |
| NoThinking wins at small budgets | R1-Distill-Qwen, AMC23 at 700 tokens: 51.3 vs 28.9; with parallel samples matches Thinking at up to 9x lower latency | Ma 2025 [c18] | [E] K12 |
| Learned difficulty predictor saves compute | Up to 50% on math/code at equal success; 25-50% at B>=8; marginal at B<8; chat 0-10% (oracle 15-25%); routing 25-40% fewer expensive calls | Damani 2024 [d03] | [E] K05/K21 |
| Model-predicted restart token | Llama 3.1 8B GSM8K 84% to 91% with 16 samples; adaptive reaches 74% of the gain with 1.2 samples; needs fine-tuning | Manvi 2024 [d04] | [S] K21 |
| Confidence calibration stops early | MathQA 81.0 to 83.6 at 16-response budget; sample savings 39.8%, 50.4%, 94.2% (figure text) | Huang 2025 [d05] | [S] |
| Consistency-based early stopping | Saves 34% of samples on average over six datasets (up to 43% GSM8K, 41% MGSM) at budget 16 | Chen 2025 [c19] | [E] K20 |
| Confidence-based stop rules | DEER cuts CoT 19.1-80.1% with accuracy +0.3 to +5.0 (11 models, 10 benchmarks). DeepConf online saves ~19-59% conservative, up to 84.7% aggressive; GPT-OSS-120B AIME25 99.9% vs cons@512 97.0%. Answer convergence: models converge after ~60% of steps; >40% fewer tokens on NaturalQuestions | [c20, d14, d13, d15] | [E] K24 |
| Stop rules combined | Not tested head to head | [d15] | open K25 |
| Self-verification of many samples scales | Gemini 1.5 Pro Verification@200: MATH 467/500 vs 428 (o1-Preview), AIME 8/15 vs 7/15; Consistency@200 only 4/15 on AIME | Zhao 2025 [c13] | [S] K17 |
| Weak-verifier ensemble | Llama 3.3 70B K=100: 87.7% vs o3-mini first sample 86.7%, GPT-4o first sample 69.0%; 400M distilled scorer keeps 98.7% with 99.97% less verification compute | Saad-Falcon 2025 [d07] | [S] |
| Verifier-free distillation lags | Gap to verifier-based RL/search widens with budget (theory + 3B/8B/32B) | Qu/Setlur 2025 [b14, c14] | [S] K17 |
| RLVR narrows reach at large k | pass@1 higher for RL; pass@256 higher for base models; six RLVR algorithms similar | Yue 2025 [b11] | [E] K14 |
| Agents gain modestly | GAIA (n=165) GPT-4.1 baseline 55.76; best-of-N list-wise 63.03, scoring 59.39, voting 56.8; reflect every step 55.15; reflect only if score <2: 56.36; beam 56.97 | OPPO 2025 [d09] | [E] K23 (weak: no CIs) |
| Task-dependent gains and cost | GPT-4o 256 parallel calls: TSP easy 42% to 95%, hard no gain; best-of-5 +10 to +15 points typical (perfect verifier); R1 uses 5x tokens of Claude 3.7 at accuracy within 3% (AIME25) | Balachandran 2025 [d10] | [E] |
| Three regimes by complexity | Plain model equal/better at low, thinking wins medium, both collapse at high; River Crossing N=3 (11 moves) still fails, first error near move 4 | Shojaee 2025 [b16, d11] | [C] K13 |
| Critique of regimes | Hanoi N_max ~12-13 at 64k output cap; River Crossing N>=6 (b=3) unsolvable; generating-function prompt gives high accuracy; preliminary | Lawsen 2025 [c17, d12] | [C] K13 |
| Sleep-time compute | ~5x less test-time compute at equal accuracy; +13%/+18% with more sleep compute; 2.5x per query at 10 questions per context; little at 2; plain test-time wins at high budgets | Lin 2025 [c22, d17] | [S] K19 |
| Majority-vote ceiling | Accuracy converges to a fixed limit set by probability mass on the correct answer | Wu 2024 [a12] | [E] theory |
| PRM > ORM > majority | 78.2 / 72.4 / 69.6 at N=1860 | Lightman 2023 [a22] | [E] K16 |

## 4. Mechanisms and models

### 4.1 Coverage and selection (the basic model)

Let p_i be the chance one sample solves problem i. With N independent samples, coverage on problem i is 1-(1-p_i)^N. Averaged over problems, the heavy tail of small p_i makes coverage grow like a power law in N (Levi's toy model [a29]; Brown's exponentiated power law [a07]). Samples from one model are not fully independent, and correlation grows with N [a29], so real curves bend below the ideal.

Coverage is an upper bound. Accuracy depends on the selector. Implement it as:

```
cands = [sample(task) for _ in range(N)]        # each in a fresh context (S3)
if check_exists:
    pass_set = [c for c in cands if run_check(c)]    # code selects (G5)
    answer = pass_set[0] if pass_set else best_so_far  # G6 never abstain
else:
    answer = vote(cands)                              # code, not model
```

Majority vote has a hard limit [a12]: it converges to the answer the model gives most often, not to the right answer. It cannot pick a rare correct answer. This is why Brown's vote line is flat at about 41% while coverage reaches 98%.

### 4.2 Verifier error and the optimal N

If the check accepts a wrong answer with probability f (false positive rate), accuracy after unlimited tries is bounded by that error [a28]. Treat the choice as a utility problem: gain from a true pass versus cost of a false pass, times attempt count. Stroebl found the optimal N is often under 10 and can be zero for weak models.

Practical rule: estimate f per task type on a labelled sample, then pick N where the marginal gain per token drops below your threshold. Hybrid checks (tests plus a second selector) beat either alone when each saturates [d08].

LLM judges are poor verifiers on reasoning and planning [d06, d18]. They both pass wrong answers (10.4% false positive on Game of 24) and reject right ones (false negatives up to 97% in two planning domains). Use a sound external check where one exists. When none exists, use an ensemble of weak judges with weights estimated without labels [d07], or self-verify many candidates in a fresh context [c13], and measure its error rate before trusting it.

### 4.3 Compute-optimal allocation (Snell)

1. Estimate difficulty per prompt. Snell uses the base model's pass rate over 2048 samples, binned into 5 levels [a02]. Oracle bins use ground truth; "predicted" bins use averaged verifier scores. Model-specific bins predicted benefit better than human difficulty labels. Estimating is itself inference compute.
2. For each bin and budget, choose the method (best-of-N, beam, lookahead, revision ratio) that scored best on a validation set. Keep a lookup table.
3. Easy bins: sequential revision, or best-of-N; avoid aggressive search (it over-optimises the PRM into short, repetitive steps [a04]). Hard bins: parallel exploration or beam. Hardest: little gain; pretraining matters more.

For our gate, replace the 2048-sample estimate with a cheap proxy. Learned predictors do this. Damani [d03] trains a small model to predict the marginal reward of extra samples and allocates by it. Manvi [d04] fine-tunes the generator to emit a "restart helps" token. Neither is a pure scaffold method. A prompt-only equivalent is untested.

A simple pure-scaffold proxy (our own idea, not from a paper; to be tested): draw 3-4 short samples; if all agree and the check passes, stop; if they disagree, escalate N or switch mode. This is the same idea as consistency-based stopping [c19] and answer convergence [d15].

### 4.4 Budget forcing (s1)

At decode time, count thinking tokens. To cap: when the budget is hit, emit the end-of-thinking delimiter. To extend: when the model tries to end, delete the delimiter and append "Wait". Control was 100% and scaling positive. Token-, step- and class-conditional prompts gave 40-60% control and weak or negative scaling; rejection sampling scaled negatively (-35) [a15]. Gains flatten around six Waits and loops appear [a14, b06]. This needs exposed thinking tokens and decode-level control, which hosted APIs mostly lack. For us the analogue is a token-budget parameter where one exists, plus code-side control of how many attempts run.

### 4.5 Early stopping and exit

- **Sample-count stop** [c19]: draw answers one at a time; stop when the first k agree. Saved 34% of samples at budget 16.
- **Short-m@k** [a26]: launch k chains in parallel; stop when the first m finish; vote among those m. Uses the finding that short chains are more often right.
- **Answer-stability stop** [d15]: ask for the interim answer at intervals; stop when it repeats. Models converge after about 60% of steps on math.
- **Confidence exit** (DEER [d14]): at "Wait"-style transition points, produce a trial answer; if its token probability is high, stop. Needs token probabilities.
- **DeepConf** [d13]: bottom-10% group and tail confidence per chain; offline weighting or filtering; online stop below a threshold calibrated on 16 warm-up traces. The aggressive setting can hurt through overconfident wrong answers.
- **Calibrated confidence** [d05]: distil self-consistency into a one-pass confidence.

Only the sample-count stop and short-m@k work purely from outside the model. The rest need logprobs, internals or fine-tuning.

### 4.6 Variance explanation for long thinking

Ghosal [d01] models extra thinking as increasing the spread of the output distribution. Spread helps when the mean is below the threshold (more chance to land on the answer), then hurts when it moves mass off the correct mode. This predicts gain then loss with length, and that parallel short chains do better at equal tokens. It is a model fitted to observed curves, not a direct test. Treat it as a hypothesis.

### 4.7 Sleep-time compute

Before any question, have the model pre-process a stored context (derive likely facts, summaries, intermediate results). At question time, answer from the processed context [d17]. Cost per query falls when many questions share a context and queries are predictable from it. Implement as a background pass over memory, keyed by context hash, with the output cached. Five parallel sleep generations usually beat ten.

### 4.8 Agent scaling

Whole-trajectory best-of-N with a list-wise judge (the judge sees all trajectories at once) gave the gain on GAIA (+7.3 points, 55.76 to 63.03) [d09]. Step-level beam search and reflect-every-step gave nothing or lost. The only reflection variant that did not lose was reflect-only-when-the-step-score-is-very-low (56.36 at threshold <2). Rule: resample whole attempts; reflect on a trigger, not on a schedule (this is G1).

## 5. What holds up

### 5.1 Replicated or multi-source

- **Coverage grows with samples** (Brown, Levi toy model, Wu limits; K01). Holds for math and code across many models.
- **Selection is the bottleneck** (Brown, Chen, Stroebl, Wu theorem; K02, K04). Three independent lines.
- **Verified sampling works** (Cobbe 2021, Brown 2024, Lightman 2023, Jain 2025; K03, K16).
- **Difficulty-aware allocation saves compute** (Snell, Damani, Manvi, Huang; K05, K21). At least two groups. The size differs: 4x with oracle bins on MATH; up to 50% with a learned predictor on math/code; 0-10% on chat.
- **Shorter is better within a question** (Hassid, Zeng; K10). Several models and benchmarks.
- **Reasoning models overthink easy items** (Chen, Ma, DEER, DeepConf, answer convergence; K12, K24).
- **Self-correction without an external signal fails** (Huang 2024, Stechly 2024; K22). GPT-3.5/4 era. A sound external check restores gains.
- **RL narrows reach** (Yue, DeepSeek; K14).

### 5.2 Failures and reversals

- Majority-vote accuracy falls with more calls on hard queries [b05].
- Rejection sampling for length control gave negative scaling (-35) [a15].
- Training on all 59K traces did not beat the curated 1K [a14, a17].
- Beam search is worse than best-of-N on easy items; lookahead is usually worse at equal cost [a04].
- Reflect-every-step lost in the agent study [d09].
- Aggressive DeepConf filtering hurt on GPT-OSS-120B [d13].
- Illusion-of-thinking collapse is partly an artefact (Hanoi output cap, unsolvable River Crossing N>=6) [d12]; the N=3 (11 moves) failure is not explained by limits [d11].
- o1-Preview on AIME was re-measured at 26%, not the reported 44%, in Zhao's setup [c13] (small N, noise).

### 5.3 Moderators

| Moderator | Effect | Evidence |
|---|---|---|
| Verifier exists and is sound | Coverage turns into accuracy; without it, plateaus | [a08, a09, d08] |
| Verifier false-positive rate | Sets the accuracy ceiling and cost-optimal N | [a28] |
| Model size and PRM | Flips the best search method | [a24] |
| Difficulty | Easy: little or negative gain from search; hard: parallel/search; hardest: little | [a04, a06, a24] |
| Task type | Math/code gain; chat 0-10%; agentic modest; hard NP problems none | [d03, d09, d10] |
| Distractors in context | Long thinking hurts (Claude), framing overfit (o-series) | [b07, d16] |
| Output cap and instance validity | Explains part of the puzzle collapse | [d12] |
| Query predictability and questions per context | Sleep-time gain | [d17] |
| Budget level | NoThinking and short-1@k win at low budgets; advantage fades at high | [c18, c12] |
| Few-shot examples | Fix spurious-feature drift under long thinking | [b26, d16] |

### 5.4 Interventions that worked and did not

Worked: budget forcing (positive scaling, 100% control) [a15]; whole-trajectory best-of-N [d09]; hybrid verifiers [d08]; short-m@k [a26]; consistency stop [c19]; early exit [c20]; Shortest Majority Vote beat plain majority on AIME and GPQA [c11]; sleep-time with predictable queries [d17].

Did not work: token-, step-, class-conditional prompts for length control [a15]; rejection sampling for length [a15]; same-model self-critique [d06, d18]; lookahead search at equal cost [a04]; reflect-every-step [d09]; step-level beam search on agents [d09]; verifier-free distillation at high budgets [b14].

### 5.5 Unresolved conflicts

1. Sequential vs parallel (K09). s1 compares different base models. Ghosal uses forced "Wait" on small distilled models. Sharma caps each chain at 4096 tokens and uses instruct models with feedback. No test on a frontier thinking model split by difficulty.
2. Snell's recipe vs Liu's (K06).
3. The three-regime result (K13).

## 6. Language models

**Baseline behaviour.** Chain of thought is emergent with scale [a21]: small models gain nothing. Self-consistency gains grow with model strength [a20]. Test-time scaling works best on models that already have a non-trivial chance on the problem (Snell, Brown, Yue).

**What changed it.**
- Verifiable-reward RL produced models that think long by themselves (R1-Zero 15.6% to 77.9% on AIME 2024 [a23]). It also made them overspend: 1,953% more tokens on "2+3=?" [a25].
- Training moved some sampling gain into pass@1 but narrowed pass@256 [b11].
- Fine-tuning on 1K traces (s1) gave a usable length knob [a14].
- Early-exit methods without training (DEER, DeepConf, answer convergence) trim 19-85% of tokens on open reasoning models with accuracy near equal or higher [d13-d15].

**By how much (examples).**
- Self-consistency: +17.9 on GSM8K (PaLM-540B).
- Verified repeated sampling: 15.9% to 56% on SWE-bench Lite.
- Compute-optimal allocation: about 4x less compute than best-of-N (one family).
- Parallel vs "Wait" extended thinking at 16K tokens: +22% (small distilled models).
- NoThinking at 700 tokens: 51.3 vs 28.9 on AMC23.
- Shortest vs longest chain: up to +34.5 points.
- Agent best-of-N: +7.3 points on GAIA.

**Where models fail.**
- Easy items: wasted tokens (K12).
- Distractors: accuracy falls with long reasoning (Opus 4 near 100% to ~80%; R1 70% to 30% with 5 distractors) [b07, d16].
- Spurious features: priors drift under long thinking; few-shot examples largely fix it [d16].
- Self-verification: false negatives up to 97% for GPT-4 on planning [d06].
- Self-correction: CommonSenseQA 75.8 to 38.1 for GPT-3.5 [d18]. Newer reasoning models trained to self-check may differ; untested here.
- Contamination caution: Llama 3.1 405B averaged 40% on AIME-style questions 1983-2024 but 1% on 2025 questions [d10]. Old benchmark gains may partly be memorisation.

**Closed frontier models.** The only frontier-model evidence in our set is Gema 2025 (Claude, o-series) [b07, d16] and GPT-4.1 in the GAIA study [d09]. The rest uses open models, PaLM 2, or 2023-era GPT. Transfer to current frontier models is an open question.

## 7. What our agent should take

### Add now (established)

| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| A1 | **S0 gate routes easy items to a short path without extended thinking.** Plain or short answer first; escalate only on a signal (check fails, samples disagree). | S0, G11, G1 | [E] | K12; a25, c10, c18, d14, d15 (the regime split b16 is [C]) |
| A2 | **Hard cap on reasoning length per mode, plus a stop rule.** Never leave thinking uncapped; thinking longer can lower accuracy. | G11, G12 | [E] | K11; b05, b07, d01, d16 |
| A3 | **Prefer several short independent attempts over one long one** when the answer is checkable or countable. Keep as the default arm until test E1 is done. | S3, G11 | [E] short beats long within a question; [C] parallel beats extended | K10, K09; a26, a27, b15, d01 |
| A4 | **Use sample-heavy mode only where a runnable check exists.** Without a check, do not raise N past the point where vote accuracy plateaus. | S4, S7, G6 | [E] | K02, K03, K04; a09, a28, d08 |
| A5 | **Cap N at the cost-optimal value from a measured verifier error rate.** Default N under 10 until measured. | G6, G12 | [E] | K04; a28, b24 |
| A6 | **Budget by difficulty, not uniformly.** Use predicted difficulty from a few cheap samples, not an oracle. Expect smaller savings than Snell's 4x. | S0, G12 | [E] | K05, K21; a03, d03 |
| A7 | **Adaptive stopping on answer agreement.** Stop drawing samples when the first k agree. | G12, O-stop | [E] | K20; c19, d15 |
| A8 | **Code selects; the selector gets no authorship or majority hint.** Vote and rank in code. Agreement is a hint, not proof. | G4, G5, S7 | [E] | K02; a12, a09 |
| A9 | **No self-critique loop without an external signal.** Revise only from a real failing output or tool result. | G2, G6, S5 | [E] | K22; d06, d18 |
| A10 | **For tool agents, resample whole trajectories and reflect only on a low-score trigger.** No per-step reflection. | S3, S5, G1 | [E] but small n (GAIA 165, no CIs) | K23; d09, d08 |
| A11 | **Use two different checks when a single check saturates.** | S4, G3 | [E] | K03; d08 |
| A12 | **Report pass@k curves, not only pass@1, for any sampling change.** | G7 | [E] | K14; b11 |

### Test first

| # | Item | Schema part | Status | Evidence | Why test |
|---|---|---|---|---|---|
| T1 | Extended thinking vs k parallel short chains at equal total tokens, by difficulty bin, on a frontier model | G11, G12, S3 | [C] | K09; d01, d02, a16, c25 | Core conflict; no frontier test |
| T2 | Prompt-only difficulty predictor (3-4 cheap samples or a confidence token) for S0 | S0, G12 | [S] | K21; d03, d04 | Savings shown for learned predictors; prompt-only unknown |
| T3 | short-m@k as selector and stop rule | S7, O-stop | [E] for open long-chain models; untested in our scaffold | K10; a26 | Cheap to test |
| T4 | Combined stop rules (consistency + short-m@k + convergence) | O-stop | open | K25; d15 | Not tested anywhere |
| T5 | Self-verification of top-k candidates in fresh context vs majority vote | S8, O-verify | [S] | K17; c13 | Needs measured error rate |
| T6 | Weak-verifier ensemble for tasks with no check | S7, G6 | [S] | d07 | Costly; large gain if it transfers |
| T7 | Whole-trajectory best-of-N with list-wise judge for multi-step tasks | S3, S7 | [E] on GAIA, small n | K23; d09 | Replicate at our scale |
| T8 | Sleep-time precompute on memory | memory | [S] | K19; d17 | Only if context is reused for 10 or more questions |
| T9 | Distractor filter or cap against inverse scaling | G12, memory | [S] | K26; d16 | Nobody tested the fix |
| T10 | Regime split (low / medium / high) as routing rule | S0 | [C] | K13; b16, d11, d12 | Output-limit confound |
| T11 | Small model, many samples vs large model, one shot, at equal FLOPs | G12 | [E] math; [S] small-beats-large | K07, K08; a11, a24 | Model choice per class |
| T12 | Step verifier (PRM) | G6 | [E] on MATH | K16; a22 | Only if a step verifier exists; probably not |

## 8. Concrete tests on our bench

Rule for all tests: both arms get the same total tokens, counting setup, verifier and thinking tokens (G7). Report pass@1 and tokens per item. Use at least 100 items per cell where possible; a 30-item set gives 3.3-point steps and wide intervals [d02, a15].

| Test | Item type | Arms (equal tokens) | Metric | Expected effect |
|---|---|---|---|---|
| E1 (T1) sequential vs parallel | Checkable items in three difficulty bins by plain pass rate (easy 50-100%, medium 10-50%, hard 0-10%, per Liu [a24]) | A: one chain at budget B with extended thinking. B: k chains at B/k each, vote. C: sequential refinement with real feedback | Accuracy per bin | Parallel wins easy/medium by 5-20 points (Ghosal); gap shrinks or reverses on hard; refinement wins if feedback is real (Sharma) |
| E2 (T2) S0 gate | Mixed items with known difficulty | A: always-think. B: gate by 3-4 cheap samples (stop if they agree and the check passes). C: oracle bins | Tokens saved at equal accuracy | 25-50% fewer tokens on math/code; 0-10% on open items; below oracle |
| E3 (A1) easy path | Easy items | A: extended thinking. B: short direct answer | Accuracy, tokens | Equal accuracy, large token cut (Ma: 51.3 vs 28.9 at 700 tokens) |
| E4 (A4/A5) N cap | Items with a runnable check | N = 1, 3, 5, 10, 30 at matched total tokens | Selected accuracy; coverage; false-pass rate | Coverage keeps rising; selected accuracy plateaus near N=5-10 |
| E5 (A7/T4) stop rules | Fixed item set | A: fixed N. B: consistency stop. C: short-m@k. D: answer-convergence stop. E: B+C+D | Accuracy per token | Each saves 20-40%; combined unknown |
| E6 (T3) short-m@k | Math and reasoning items | A: majority of k. B: short-1@k and short-3@k | Accuracy, tokens, wall time | Up to 40% fewer tokens, similar accuracy at low budget |
| E7 (T5) self-verify | Items with ground truth | A: majority vote of N. B: self-verify top-k in fresh context. C: oracle pick | Accuracy; judge FP and FN rates | If FP over 10% or FN over 20% on a task type, do not loop (Stechly) |
| E8 (T7) agent best-of-N | Multi-step tool tasks | A: single trajectory. B: whole-trajectory best-of-N list-wise. C: reflect-every-step. D: reflect on low score | Task success | B +5-7 points; C no gain; D slight |
| E9 (T9) distractors | Long-constraint and distractor-injected items, 0-5 distractors | A: uncapped thinking. B: capped. C: capped plus distractor filter | Accuracy vs distractor count | Uncapped falls with distractors; cap or filter flattens it |
| E10 (T8) sleep-time | Many questions per stored context (1, 2, 10) | A: test-time only. B: precompute then answer | Tokens per query at equal accuracy | About 2.5x at 10 questions; none at 2 |
| E11 (T11) small vs large | Items by difficulty | Small model x many samples vs large x 1 at equal FLOPs | Accuracy per bin | Small wins easy/medium until saturation |
| E12 (T6) weak-verifier ensemble | Items without a check | A: majority. B: ensemble of 3-5 judges, weights from agreement. C: oracle | Accuracy; total tokens including judges | Gain over majority only if judge errors are not correlated (G4) |

## 9. What does not transfer, and why

- **PRM-guided tree search.** Needs a trained process reward model per task and model [a24]. We have none. Search methods also over-optimise the PRM on easy items [a04].
- **Oracle difficulty bins (Snell's 4x).** Needs thousands of samples per problem. Not deployable. Predicted-difficulty versions save less [d03].
- **Budget forcing as published.** Needs exposed thinking tokens and decode-level control, plus fine-tuning on s1K [a14]. We can only mimic it by capping tokens or chain count.
- **Training-time fixes for overthinking** (SimPO length preference, RL, restart-token fine-tuning) [a25, d04]. A scaffold-only agent cannot train.
- **Token-probability stop rules (DEER, DeepConf).** Need logprobs and model internals; closed APIs may not expose them [d13, d14].
- **Small-beats-large claims (1B > 405B).** Author-reported with a strong PRM and large N; math only [b04].
- **Majority vote for open-ended tasks.** Needs a short exact final answer [b10]. Open or creative tasks need other selectors (schema open mode, G8).
- **Sleep-time compute.** Gains shown only on rewritten benchmarks with separable context and predictable queries [d17].
- **Chat or open-ended gains.** Learned allocation saved 0-10% on chat [d03]. Most strong results are checkable math and code (critique weak spot).
- **R1/QwQ/LIMO findings** (longer is worse) come from open o1-like models; frontier models with built-in budget parameters may differ.
- **2023 self-correction failures** (GPT-3.5/4) may not carry over to reasoning models trained to self-check; d02 shows refinement can win at matched tokens.

## 10. Open questions

1. Extended thinking vs k parallel short chains at equal total tokens on a frontier thinking model, split by difficulty (resolves s1 vs Ghosal/Zeng/Sharma).
2. How much of Snell's 4x survives with a cheap, deployable difficulty predictor? The exact retained fraction is not tabulated.
3. False-positive and false-negative rates of realistic verifiers (self-verification, tests, LLM judge) on non-math tasks, and the cost-optimal N.
4. Do gains carry to open-ended, tool-using and agent tasks beyond GAIA (n=165, no CIs) and SWE-bench?
5. Is the three-regime result robust with output limits fixed and only solvable instances? Can it be a routing rule?
6. Do stop rules combine, and which is best per token across models?
7. Does anyone replicate small-beats-large with a weak, non-oracle PRM?
8. Which inverse-scaling failure modes appear in our scaffold, and do a cap or distractor filter remove them?
9. How general is sleep-time compute beyond one group's benchmarks?
10. Does the pass@k reach result (Yue) hold for scaffolded frontier models at k up to 64?
11. How much benchmark gain is memorisation (405B: 40% on old AIME-style vs 1% on 2025 [d10])?
12. What does equal-total-token accounting, including verifier tokens, do to the published gains? Few papers report it.

## 11. Sources

All URLs are arXiv. [V] = opened (PDF or HTML text read in this series; the cross-check re-opened the main numbers). [M] = snippet, abstract or front matter only.

| Source | Mark | URL |
|---|---|---|
| Snell, Lee, Xu, Kumar (2024) Scaling LLM test-time compute optimally | [V] | https://arxiv.org/abs/2408.03314 |
| Brown et al. (2024) Large Language Monkeys | [V] | https://arxiv.org/abs/2407.21787 |
| Wu, Sun, Li, Welleck, Yang (2024) Inference scaling laws | [V] | https://arxiv.org/abs/2408.00724 |
| Muennighoff et al. (2025) s1: simple test-time scaling | [V] | https://arxiv.org/abs/2501.19393 |
| Jones (2021) Scaling scaling laws with board games | [V] | https://arxiv.org/abs/2104.03113 |
| Cobbe et al. (2021) Training verifiers | [V] | https://arxiv.org/abs/2110.14168 |
| Wang et al. (2023) Self-consistency | [V] | https://arxiv.org/abs/2203.11171 |
| Wei et al. (2022) Chain-of-thought prompting | [V] | https://arxiv.org/abs/2201.11903 |
| Lightman et al. (2023) Let's verify step by step | [V] | https://arxiv.org/abs/2305.20050 |
| DeepSeek-AI (2025) DeepSeek-R1 | [V] | https://arxiv.org/abs/2501.12948 |
| Liu et al. (2025) Can 1B LLM surpass 405B LLM? | [V] | https://arxiv.org/abs/2502.06703 |
| Chen et al. (2024) Do NOT think that much for 2+3=? | [V] | https://arxiv.org/abs/2412.21187 |
| Hassid et al. (2025) Don't overthink it | [V] | https://arxiv.org/abs/2505.17813 |
| Zeng et al. (2025) Revisiting test-time scaling of o1-like models | [M] abstract and intro; per-benchmark numbers not pulled | https://arxiv.org/abs/2502.12215 |
| Stroebl, Kapoor, Narayanan (2024) Limits of inference scaling through resampling | [V] | https://arxiv.org/abs/2411.17501 |
| Levi (2024) A simple model of inference scaling laws | [V] | https://arxiv.org/abs/2410.16377 |
| Ji et al. (2025) Survey of test-time compute | [M] front matter, no numbers | https://arxiv.org/abs/2501.02497 |
| Chen et al. (2024) Are more LLM calls all you need? | [V] | https://arxiv.org/abs/2403.02419 |
| Gema et al. (2025) Inverse scaling in test-time compute | [V] | https://arxiv.org/abs/2507.14417 |
| Qu / Setlur et al. (2025) Scaling test-time compute without verification or RL is suboptimal | [V] (author list unverified) | https://arxiv.org/abs/2502.12118 |
| Ghosal et al. (2025) Does thinking more always help? | [V] | https://arxiv.org/abs/2506.04210 |
| Shojaee et al. (2025) The illusion of thinking | [V] | https://arxiv.org/abs/2506.06941 |
| Lawsen (2025) The illusion of the illusion of thinking | [V] (preliminary comment) | https://arxiv.org/abs/2506.09250 |
| Yue et al. (2025) Does RL really incentivize reasoning capacity? | [V] | https://arxiv.org/abs/2504.13837 |
| Zhao et al. (2025) Sample, scrutinize and scale | [V] | https://arxiv.org/abs/2502.01839 |
| Ma et al. (2025) Reasoning models can be effective without thinking | [V] | https://arxiv.org/abs/2504.09858 |
| Chen et al. (2025) Do we truly need so many samples? | [V] | https://arxiv.org/abs/2504.00762 |
| Yang et al. (2025) Dynamic early exit in reasoning models (DEER) | [V] | https://arxiv.org/abs/2504.15895 |
| Sui et al. (2025) Stop overthinking: survey on efficient reasoning | [M] survey, no numbers | https://arxiv.org/abs/2503.16419 |
| Lin et al. (2025) Sleep-time compute | [V] | https://arxiv.org/abs/2504.13171 |
| Sharma and Chopra (2025) The sequential edge | [V] | https://arxiv.org/abs/2511.02309 |
| Damani et al. (2024) Learning how hard to think | [V] | https://arxiv.org/abs/2410.04707 |
| Manvi, Singh, Ermon (2024) Adaptive inference-time compute | [V] | https://arxiv.org/abs/2410.02725 |
| Huang et al. (2025) Efficient test-time scaling via self-calibration | [V] abstract, intro, figure text | https://arxiv.org/abs/2503.00031 |
| Stechly, Valmeekam, Kambhampati (2024) Self-verification limitations | [V] (table rows partly garbled) | https://arxiv.org/abs/2402.08115 |
| Saad-Falcon et al. (2025) Weaver: weak verifiers | [V] (table alignment partly uncertain) | https://arxiv.org/abs/2506.18203 |
| Jain et al. (2025) R2E-Gym | [V] | https://arxiv.org/abs/2504.07164 |
| OPPO AI Agent Team (2025) Scaling test-time compute for LLM agents | [V] (columns partly garbled) | https://arxiv.org/abs/2506.12928 |
| Balachandran et al. (2025) Inference-time scaling for complex tasks | [V] | https://arxiv.org/abs/2504.00294 |
| Fu et al. (2025) Deep think with confidence (DeepConf) | [V] | https://arxiv.org/abs/2508.15260 |
| Liu and Wang (2025) Answer convergence as a signal for early stopping | [V] | https://arxiv.org/abs/2506.02536 |
| Huang et al. (2024) LLMs cannot self-correct reasoning yet | [V] | https://arxiv.org/abs/2310.01798 |

## Source audit (2026-11-01)

Fresh auditors re-opened the sources of 17 established claims: 14 confirmed as written, 3 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **C01.03-K05** (reworded: the sources support less). Damani et al. report 25-50% savings for Math at budgets B>=8 only; for Code they report up to 50% (and gains mainly at low budgets, online variant below best-of-k at high budgets); Snell's 4x is 'up to' and holds for predicted as well as oracle bins. Corrected claim: Optimal compute allocation depends on difficulty: easy items gain from sequential revision, hard ones from parallel sampling or search; difficulty-adaptive allocation matches best-of-N with up to about 4x less compute (PaLM 2-S*, MATH; both oracle and predicted difficulty bins). With a learned difficulty predictor, a second group saw up to 50% savings on math and code (25-50% on math at budgets B>=8), 0-10% on chat (25-40% on a high-variance subset), and 25-40% fewer calls for model routing; the oracle curve stays above the predictor.
- **C01.03-K14** (reworded: the sources support less). Only Yue et al. supports the pass@k finding and it is scoped to the tested models/RLVR setups; the DeepSeek-R1 paper reports pass@1 and length growth, not base-vs-RL pass@k, so it is not independent support, and Brown 2024 is not a listed evidence line. Corrected claim: Yue et al. (2025) find that in the RLVR setups they tested (math, code, visual reasoning), RL-trained models beat their base models at small k (e.g. k=1) but base models reach higher pass@k at large k, suggesting RLVR mostly reuses reasoning paths already present in the base model; this rests on one study, and DeepSeek-R1 only shows RL raising pass@1 (R1-Zero AIME 2024 15.6% to 77.9%) with longer outputs.
- **C01.03-K23** (reworded: the sources support less). OPPO Table 1 shows step-level BoN-wise 58.79 and beam search 56.97 above the 55.76 baseline (paper calls both significant gains); only DVTS equals baseline (55.76), so 'no gain or lose' is wrong for beam and BoN-wise. Corrected claim: Test-time scaling transfers to tool-using agents but modestly: on GAIA (n=165) whole-trajectory best-of-N with list-wise selection lifts GPT-4.1 from 55.76 to 63.03; step-level methods gain less (BoN-wise 58.79, beam search 56.97) or nothing (DVTS 55.76); reflecting at every step slightly lowers the score (55.15) and reflect-only-when-low-score (threshold <2) helps slightly (56.36). SWE agents (R2E-Gym) gain from 34.4% pass@1 to 51.0% Best@26 with hybrid verifiers.
