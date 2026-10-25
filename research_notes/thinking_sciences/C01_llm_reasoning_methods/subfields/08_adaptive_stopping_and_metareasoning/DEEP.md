# Adaptive stopping and metareasoning: deep document

*Subfield 08 of C01 (LLM reasoning methods). Built from evidence_a-d.jsonl (a01-a29, b01-b26, c01-c30, d01-d21), claims.jsonl (C01.08-K01 to K27) and critique.md in this folder. Written 2026-10-26. Evidence ids in brackets point to those files. Claim ids are written K01 to K27 for short.*

*Links, not covered here (researched in parallel): Accuracy and dissociation of monitoring; LLM metacognitive harness; Progress monitoring theory; Verification design; Soar impasses and chunking; Probing and measurement selection. Earlier C01 documents cover self-consistency basics, sampling diversity and self-correction; this file does not repeat them.*

---

## 1. What it is

The question: **when should the agent stop sampling, stop thinking, or stop checking, and how much should it spend on this problem?**

Four families of method answer it.

1. **Stop sampling when the vote is stable.** Draw answers one at a time or in small windows. Stop when the lead is safe. Examples: Adaptive-Consistency (AC), Early-Stopping Self-Consistency (ESC), Difficulty-Adaptive Self-Consistency (DSC), Reliability-Aware Self-Consistency (ReASC).
2. **Stop one chain of thought early.** Cut a long trace when its answer has stabilised or its confidence is low. Examples: DEER, Certaindex, DeepConf, probes on hidden states, trained length control (L1), forced length (s1 budget forcing).
3. **Give each problem its own budget.** Estimate difficulty, then route to a cheap or a costly mode. Examples: Snell et al. compute-optimal allocation, Damani et al. probes, Manvi et al. self-evaluation token, RouteLLM, Route-to-Reason.
4. **The theory under all of it.** Rational metareasoning: a computation is an action. Do it only if its expected gain in decision quality is above its cost. Sources: Russell and Wefald, Hay et al., Lieder and Griffiths, and one bridge to LLMs (RaM).

For our agent the schema already holds the headline rules: G11 (think briefly), G12 (spend by difficulty), S0 (gate), and the stop triggers in S5/S6/S8. This subfield asks what the best-supported **stop rules** are, how much they really save, and where they fail. Short answer: agreement-based stopping saves a lot on easy maths, much less on hard items, and its main failure (wrong consensus) has never been measured for vote rules.

---

## 2. History and theories in depth

### 2.1 Rational metareasoning (theory)

- **Roots.** I. J. Good's "Type II rationality" (maximise expected utility, net of the cost of deciding) and Howard's value of information [a01]. A thinking step is an action. Its benefit is a possibly better external decision. Its cost is delay.
- **Russell and Wefald (1989, 1991).** Value of computation (VOC) = expected gain in decision quality from one computation minus its time cost. The *meta-greedy, single-step* rule runs the computation with the highest VOC and stops when none has positive VOC. The 1991 book "Do the Right Thing" was **not opened** by us; all of this is second-hand through Russell (1997) and Hay et al. [a01, a29, b20, c20].
- **What VOC does in a toy case** [a01, a02]. Action A looks worth 10 (sd 1). B looks worth 8 (sd 4). VOC of looking ahead from A is 0.3. From B it is 0.82. If A is worth 12, the two VOCs fall to 0.002 and 0.06. If both are 10 with sd 0.1, VOC is 0.03. So computation is worth most when the choice is **close and uncertain**, and worth nothing when one option clearly leads **or** when the options are so close that the pick does not matter.
- **Anytime algorithms** [a03]. If the quality-versus-time profile of an algorithm is known, "when to stop" is fairly easy. For LLM reasoning the profile differs per problem and is unknown beforehand. This is the core gap between theory and practice.
- **Hay, Russell, Tolpin, Shimony (2012/2014)** [a04, a05, b19]. Formal "selecting computations" problem. Results that matter:
  - The myopic (one-step) policy **stops too early**. If it computes in a state, the optimal policy also computes (Theorem 7). So the myopic rule is a lower bound on thinking, not a good stop rule alone.
  - The optimal policy's expected number of computations is at most the value of perfect information divided by cost per computation (Theorem 5). One-armed Bernoulli: at most (1-lambda)/c - 3, and at most 1/(4c) - 3 (Theorem 10).
  - A "blinkered" policy sits between myopic and optimal (Q_myopic <= Q_blinkered <= Q_optimal) and costs time linear in the number of arms (Theorem 16).
  - On Bernoulli sampling with 25 arms and in Go, value-of-information methods beat bandit heuristics (UCB1). Exact win rates were not extracted [a05].
  - Limit: independent actions, a known metalevel probability model, small simulations.
- **Callaway, Gul, Krueger, Griffiths, Lieder (2018), BMPS** [a11, abstract only]. Mixes myopic VOI and perfect-information VOI. Near optimal on stopping, allocation and planning problems.
- **Lieder and Griffiths (2017), strategy selection** [a06-a10]. People choose among strategies using learned predictions of speed and accuracy from problem features. Four experiments, details in section 3. Their 2020 resource-rational analysis paper was read only through a critic's commentary [b21]; the named critique is that the framework can fit almost any data.
- **Lieder, Shenhav, Musslick, Griffiths (2018)** [b22]. A learned Value of Control model explains five attention/Stroop/Flanker results better than two simple learners (BIC: visual search 1817.8 vs 9763.2 and 3449.9; Stroop 45.3 vs 1333.9 and 2454.8). Proof of concept only.

### 2.2 Self-consistency and its stopping rules (2022-2026)

- **Wang et al. (2022)** [a15, b05, c28]. Sample many chains, take the majority. PaLM-540B with 40 paths: GSM8K 56.5 to 74.4, SVAMP 79.0 to 86.6, AQuA 35.8 to 48.3, StrategyQA 75.3 to 81.6, ARC-c 85.2 to 88.7. Five to ten paths capture much of the gain. We did not open the paper; the figures came through a summary [a15] and the baseline use in later papers.
- **Adaptive-Consistency, Aggarwal et al. (2023)** [a16, a17, b01-b02, c01-c03, d01-d03]. First sequential stop rule. Section 3 has numbers.
- **ESC, Li et al. (2024)** [a18, a19, b03, b04, c04, c05, c21]. Window rule, no threshold to tune.
- **DSC, Wang et al. (2025)** [c06, c22, d09]. Rank questions by difficulty first. Also first to count input tokens.
- **RASC** [a27]. Logistic regression scores each sample; stop when 5 samples score at least 0.5.
- **CISC, Taubenfeld et al. (2025)** [a20, b06, b07]. Weight votes by confidence. Not a stop rule; it cuts the sample count needed.
- **ReASC, Kim et al. (2026)** [c07, c25, d07, d08, d20]. Single-sample confidence gate, then confidence-weighted vote.
- **Large Language Monkeys, Brown et al. (2024)** [a21, b12, d04, d05]. Coverage keeps growing; voting does not. This frames the limit of agreement-based stops.

### 2.3 Test-time compute by difficulty

- **Snell et al. (2024)** [a22, b10, b11, c08, c09, c24]. Best strategy depends on difficulty bin. The "up to 4x" and "14x larger model" results.
- **Damani et al. (2024), Manvi et al. (2024)** [d10, d11]. Cheap predictors of difficulty.
- **Routers** [b09, d19]. RouteLLM between two models; Route-to-Reason between models and strategies.

### 2.4 Reasoning models: overthinking and early exit (2024-2025)

- **Chen et al. (2024)** overthinking [a25, b16, c15, c23]. **Su et al. (2025)** [b17]. **Zeng et al. (2025)** [b13]. **Gema et al. (2025)** inverse scaling [b18]. **Kang et al. (2025)** first try matters [d14]. **Huang et al. (2024)** self-correction [d15].
- **Training-free early exit:** DEER [c16, c26], Certaindex [c17, c27], DeepConf [a26, b08, c18, c30].
- **Length control:** s1 budget forcing [a23, a24, b14, b15, c12, c13], L1 [b23, c14], RaM [a12-a14, c10, c11].
- **Agent loops:** CaRT [a28, c19], BATS / Budget Tracker [d17, d18], probes [d16], self-calibration [d21].

---

## 3. Core findings with exact numbers

Status key: **E** established (two or more independent sources, or one source plus a direct check), **S** single source, **C** contested. Claim ids from claims.jsonl. Critique corrections applied.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Vote-stability stopping (AC, Beta rule) cuts samples with near-zero accuracy loss | 17 datasets, 3 LLMs, cap 40, threshold 0.95. Maths 40 to 13.8 samples (3.3x), accuracy 73.2 to 73.1. Commonsense 40 to 15.8 (2.9x), 66.0 to 65.8. Symbolic 40 to 13.1 (3.8x), 72.8 to 72.8. Code 312.5 to 173.6 (2.4x), 35.2 to 35.6. Up to 7.9x on Boolean Expressions with no loss. Average accuracy change 0.1 to 0.2. | Aggarwal 2023 [a16, b01, c02] | E (K01) |
| ESC window rule cuts samples | Window 5 (8 for MATH), cap 40 (64 for MATH), mean of 10 runs. MATH -33.8%, GSM8K -80.1%, StrategyQA -76.8%, CommonsenseQA -78.5%, Coin Flip -84.2%, Last Letters -67.4%. GPT-4 on MATH: SC 60.32, ESC 59.98 (-0.34) at 42.4 of 64 samples. ESC and SC final votes identical 99.13 to 99.96% (GSM8K, StrategyQA, Letters). | Li 2024 [a18, b03] | E (K01) |
| Same rule, different models | AC: GPT-3.5 40 to 10.0 samples (4.4x, 76.4 to 76.2). Vicuna-13B 40 to 21.7 (1.9x, 54.0 to 54.1). Code-davinci 104.1 to 49.4 (3.4x, 69.7 to 69.8). | Aggarwal 2023 [a16, c02, d02] | E (K24 partly) |
| Savings are uneven by difficulty and model strength | ESC Llama-2-7B on MATH: 64 to 62.48 samples (-1.5), accuracy 7.7. ReASC offline gate on MATH500, Llama-3.2-3B: 7.2% accepted. Easy data: GSM8K -80%. | Li 2024; Kim 2026 [a18, b03, c07, d07] | E (K02) |
| Bayesian stability beats raw vote share at equal cost | GSM8K, cost 10 samples: AC about 3 points above fixed SC-10; up to 5 points across datasets. Paired tests: accuracy p mean 0.50, generations p mean 1.5e-3. Beta, Dirichlet, CRP similar; Random worst. | Aggarwal 2023 [a17, b02, c03, d03] | S (K26) |
| The headline factors shrink against a realistic baseline | Against SC-16, ESC saves: Llama-3.2-3B GSM8K -44.6%, MATH500 -15.4%, Omni-Math -4.4%, GPQA-D -15.4%. Gemma-3-27B GSM8K -71.4%, MATH500 -56.6%. | Kim 2026 Table 1 [d08] | E (K19) |
| Counting prompt tokens can erase the saving | Mistral-7B-Instruct GSM8K. SC-40 cost 0.3881 (input 846, output 6,045). ASC 0.6754 (+74%). ESC 0.3986 (+3%). DSC 0.2799 (-28%). GPT-3.5: input 846 vs output 164 tokens per question. | Wang 2025 Table 4 [c22, d09] | E (K19) |
| Difficulty-aware pre-allocation beats ESC | Six benchmarks. Cost vs SC: GPT-4 -65.29%, GPT-3.5 -56.04%. Cost vs ESC: GPT-4 -24.81%, GPT-3.5 -21.86%. GSM8K: only 3.8% (GPT-4) and 15.2% (GPT-3.5) of answers differ between CoT and SC-40. | Wang 2025 [c06] | S (K03) |
| Reliability-aware stopping beats AC and ESC on small models | GSM8K Gemma-3-4B: ASC -62.5%, ESC(w=4) -60.4%, ReASC -68.6 to -71.1%. Llama-3.2-3B MATH500: ASC -20.4%, ESC -15.4%, ReASC -27.8 to -33.8%. Gemma-3-4B MATH500: ESC -39.2%, ASC -42.8%, ReASC -47.8 to -49.0%. | Kim 2026 [c07, c29] | S (K03) |
| RASC scorer stops with fewer samples | GPT-3.5 maths: RASC 6.62 samples vs ESC 14.94 vs AC 12.49; accuracy 69.4 vs 69.3 vs 67.6. Vicuna-13B lost 0.9 (commonsense) and 2.0 (symbolic). Needs a trained scorer. | arXiv 2408.17017 [a27] | S (K03) |
| Early-accepted items are not all right | ReASC offline gate, accepted share / accuracy of accepted. GSM8K: Llama-3.2-3B 48.98% / 91.33%; Gemma-3-4B 51.18% / 97.78%; Qwen-2.5-7B 59.59% / 97.58%; Gemma-3-27B 60.58% / 98.62%. MATH500: 7.2% / 86.11%; 34.0% / 96.47%; 38.4% / 91.67%; 36.6% / 97.27%. Wrong-accept 1.4 to 8.7% (GSM8K), 2.7 to 13.9% (MATH500). Online gate accepts less (GSM8K 28 to 41%; MATH500 Llama-3.2-3B 17.6%). | Kim 2026 [c25, d07] | C (K18) |
| No paper counts unanimous-wrong stops for vote rules | Our simulation (not literature), 4 unanimous votes, uniform pass rate. Top wrong answer holds share w of wrong mass: w=1.0 gives 50% of stopped items wrong; 0.7 gives 19%; 0.5 gives 6%; 0.3 gives 0.8%. Easy-skewed Beta(2,.7): 9%, 2.3%, 0.6%, 0.1%. Hard-skewed Beta(.7,1.5): 83%, 54%, 24%, 4%. | d13 (model) | C (K18) |
| Models share wrong answers | Agreement when both models are wrong: 0.423 on HF Open LLM Leaderboard MMLU data (349 models, 12,032 questions, chance about 0.12); about 0.60 on HELM (71 models, 14,042 questions, chance 1/3). 100% of pairs beat chance on HF, 97.5% on HELM. Across models, not repeated samples. | Kim, Garg et al. 2025 [d06] | S (K18) |
| Confidence-weighted voting reaches SC accuracy with fewer samples | 9 models, 4 datasets, budget 10. Cost cut: P(True) 46% (SC needs 18.6 samples to match), response probability 31%, verbal 0-100 30%, verbal binary 10%. Budget 5: P(True) 41%. Accuracy gain 0.2 to 1.1. Without normalisation P(True) is 32%. | Taubenfeld 2025 [a20, b06] | S (K04) |
| Within-question discrimination is weak | P(True) 62.3%, response probability 59.0%, verbal 0-100 56.1%, verbal binary 52.2% (chance 50%). Best calibration (ECE-t 0.005, verbal binary) gave the worst saving (10%). | Taubenfeld 2025 [b07] | S (K04, K17) |
| Token-level confidence stops weak traces | Budget 512 traces. DeepConf-low saves 43 to 85% tokens, DeepConf-high 18 to 59%. GPT-OSS-120B: AIME25 -84.7% tokens, 97.9% vs 97.1% full parallel (HMMT25 row 3.23 to 0.49 x 10^8 tokens). AIME24 -79.9%. DeepSeek-8B AIME24 -77.9% tokens, +5.8 points. Qwen3-32B AIME24 -66.8%, +4.7. Headline 99.9% (DeepConf@512 offline) vs 97.0% majority vs 91.8% pass@1 is a different mode from the 84.7% saving. Failure: Qwen3-8B AIME25 -4.4; top-10% filter helped in 12 of 20 settings and lost up to 4.69 in eight. | Fu 2025 [a26, b08, c18, c30] | S (K05) |
| Only the DeepConf signal was reused elsewhere | Gemma-3-4B-it, MATH, AUROC: bottom-10% group confidence 0.860, average group 0.823, response-level self-certainty 0.801, tail group 0.699. Window 128: 0.874 (Gemma), 0.744 (Qwen-2.5-3B). | Kim 2026 App. E [d20] | S (K27) |
| Coverage grows, selection does not | SWE-bench Lite, DeepSeek-Coder-V2: 15.9% at 1 sample, 56% at 250 (single-sample SOTA 43%). MATH Llama-3-8B-Instruct: coverage 82.9% at 100, 98.44% at 10,000; majority/reward model 40.50% to 41.41%. Gemma-2B CodeContests 0.02% to 7.1% at 10,000. | Brown 2024 [a21, b12, d04] | S (K06) |
| Checkers leak | SWE-bench Lite: 11.3% flaky suites. CodeContests: 35 of 122 problems with a Python 3 reference solution fail their own tests. | Brown 2024 [d05] | E (K23) |
| Compute-optimal allocation by difficulty | MATH, PaLM 2-S*, five bins from 2048 samples per question. Matches best-of-N with up to 4x less compute (revisions 64 vs 256; search 16 vs 64). Test-time compute beats a 14x larger model on easy and medium bins at low inference load (R=0.16); pretraining wins on bins 4-5 and at high load (R=22). Beam search worsens with budget on levels 1-2. | Snell 2024 [a22, b10, b11, c08, c24] | S (K07) |
| Coarse difficulty is cheap to estimate | Probe median-split accuracy: Code 74%, Math 84%, chat routing 72%. Up to 50% less compute on Math and Code at equal success; 10% on chat (25 to 40% with tranches); 25-40% fewer expensive calls in routing. Our simulation: 4 samples give 0.79 to 0.87 median-split accuracy (U-shape 0.87, uniform 0.81, easy-skewed 0.79); five-way exact match needs about 16 samples (0.61 to 0.75). | Damani 2024 [d10]; simulation [d12] | C (K20) |
| Self-evaluation token decides resampling | Llama 3.1 8B GSM8K. Best-of-N: 84.2 (1), 87.7 (2), 88.9 (4), 89.9 (8), 91.0 (16). Adaptive threshold 0.92 with annealing: 89.2% at 1.2 samples (73.5% of the gain). | Manvi 2024 [d11] | S (K20) |
| Correct chains are shorter than wrong ones | Same question: correct shorter on MATH-500, AIME, Omni-MATH, GPQA. MATH: wrong answers average over 6,000 tokens, right under 3,000, two models. | Zeng 2025; Su 2025 [b13, b17] | E (K08) |
| Overthinking on easy items | "2+3": 1,953% more tokens than conventional models; QwQ made 13 solutions in 901 tokens, first correct at 39 tokens. First round correct in over 92% of cases using under 60% of tokens. QwQ MATH500: 2407.9 tokens, 3.2 solutions, outcome efficiency 52.3%. 2-4 rounds in 76-80% (QwQ), 59-63% (R1). | Chen 2024 [a25, b16, c15, c23] | E (K09) |
| Training on shorter answers cuts length | SimPO + first-correct + reflection: ASDIV 96.9 to 96.8 acc, 741.8 to 381.6 tokens (-48.6%); GSM8K 94.8 to 96.0 (-46.1%); MATH500 93.0 to 92.8 (-44.7%); GPQA 59.6 to 59.1 (-35.4%); AIME24 46.7 to 43.3 (-45.6%). First-correct-only lost 2 points on MATH500. Su: SimPO shorter-preferred cut 30 to 60%. | Chen 2024; Su 2025 [a25, b17] | S |
| Training-free early exit at "Wait" | DEER, threshold 0.95: chains cut 19.1 to 80.1%, accuracy +0.3 to +5.0, 10 benchmarks. R1-Distill-Qwen-7B overall 69.2 at 61.5% tokens vs 64.2 at 100%. Qwen3-14B 83.7 at 57.1% vs 82.8. About 75% of samples have a correct early exit; 36.7% needed under half their reasoning. Weak benefit on Nemotron-Nano-8B. Dynasor-CoT baseline saved 16%. | Yang 2025 [c16, c26] | S (K09) |
| Answer stabilisation predicts remaining work | Certaindex: up to 50% compute saved, 3.3x throughput, no accuracy drop; CoT with reasoning models token use down 11-29%; for the top 10% of problems savings 34% (AIME) and 53% (MATH500); top 1% 53% and 81%. Needs a profiling set. | Fu 2025 Certaindex [c17] | S |
| A probe on hidden states can stop a chain | R1-Distill-Llama-8B on MATH, 10K cap. Threshold 0.85: 88.2% (same as no exit), about 24% fewer tokens. 0.9 or more: 88.6%, 19% fewer. Beats static "stop after m chunks" by up to 5 points (87.4% vs about 82.5%). Poor transfer across domains. | Zhang 2025 [d16] | S (K16) |
| Self-revision is a weak use of tokens | Revisions that keep the original wrong answer: R1-32B 72%, R1-14B 70%, R1-1.5B 58%, QwQ 32%, LIMO 54%. Successful-revision rate under 10%. Gains plateau after about 10 revision steps. Parallel sampling gives better coverage. | Zeng 2025 [b13] | S (K10) |
| Reflection mostly confirms | 8 reasoning models, 5 maths sets. Over 90% of reflections confirmatory; wrong-to-right under about 2%. First-candidate vs final accuracy: MiMo-7B-RL 78.8 vs 81.2; R1-Distill-Qwen-7B 61.5 vs 64.4; R1-Distill-Llama-8B 62.3 vs 65.1; Qwen3-8B 81.2 vs 84.7 (gap 1.4 to 3.5). Reflection takes 16.8 to 47.8% of tokens. | Kang 2025 [d14] | E (K21, aggregate) |
| Prompted self-correction without a label hurts | GSM8K GPT-3.5 75.9 to 75.1 to 74.7; GPT-4 95.5 to 91.5 to 89.0. CommonSenseQA GPT-3.5 75.8 to 38.1 to 41.8. HotpotQA GPT-4 49.0 to 49.0 to 43.0. With an oracle stop: GPT-3.5 GSM8K 75.9 to 95.5; GPT-4 95.5 to 97.5; GPT-4 HotpotQA 49 to 59. 2023 chat models. | Huang 2024 [d15] | E (K21) |
| Forced "Wait" gives a small, flat gain | s1-32B, 1,000 SFT examples. AIME24 50.0 to 56.7 (two problems of 30), MATH500 92.6 to 93.0, GPQA-D 56.6 to 59.6. 2x Wait: AIME 53.3, MATH500 93.0, GPQA 59.6. 2x with no string: 50.0 / 90.2 / 55.1. "Alternatively" 50.0. Flat after 2x to 4x; loops at 6x. Majority over 2-64 samples of the base model stays below. | Muennighoff 2025 [a23, a24, b14, c12] | S (K11) |
| Prompted length control fails, forcing works | AIME24 control: budget forcing 100%, token-conditional 40%, step-conditional 60%, class-conditional 50%, rejection sampling 100% control but slope -35 (inverse scaling by selection). Budget forcing slope 15. Rejection sampling needed 655, 97, 8, 3, 2, 1 tries at caps 3500, 4000, 5000, 8000, 16000. | Muennighoff 2025 [a23, b15, c13] | S (K11, K12) |
| RL can train length control | L1 (1.5B): beats s1 by 100-150% relative, 20-25 points absolute at 512 and 1024 tokens; slope 0.24 vs 0.37; length error 5.6 to 6.3%; L1-Exact about 1% below DeepScaleR-4K; L1-Max matches it with up to 2x fewer tokens. Trained on maths at 4K. | Aggarwal and Welleck 2025 [b23, c14] | S (K12) |
| Rational-metareasoning reward cuts tokens | Reward = log p(y given chain) minus log p(y) minus length cost. Llama-3.1-8B-Instruct: RaM 63.5 at 146.2 tokens vs STaR 61.9 at 215.1 vs few-shot CoT 56.4 at 253.6. Another block (model label unresolved, 3B or 8B): 50.1 at 170.8 vs 47.4 at 222.7 vs 34.8 at 261.9. 23 to 45% fewer tokens. Easy-item length cut: RaM 50.3% (145 vs 72 tokens hard vs easy), STaR 34.4%, instruct CoT 0.5%. Out of domain (MMLU-CF) 28 to 36% fewer tokens, but 8B accuracy 36.4 vs 40.2 for STaR. Accuracy gains 1.6 to 2.7 over STaR sit inside overlapping 95% intervals (about +/-1.7); only the token cut is clearly real. | De Sabbata 2025 [a12-a14, c10, c11] | S (K13) |
| People choose strategies as VOC predicts | Exp 1 (N=100 MTurk): adaptive on 83.0% of trials, model 70.5% (+/-3.2), t(298)=2.34, p<0.01. Exp 2 (N=100): engagement fell 37% to 19%, d=0.79; information acquisitions d=0.48; reward rate d=1.00; reward per decision unchanged (p=0.49). Exp 3: people learned to deliberate more; model over-engaged by 20 to 30%. Exp 4 (N=100): agreed with the right strategy on 76.2% of trials. | Lieder and Griffiths 2017 [a07-a10] | S (K14) |
| Myopic VOC stops too early | Theorem 7 (optimal computes wherever myopic does). | Hay 2012/2014 [a04, b19] | E (K15) |
| Agent loops: visible budget counter | Gemini-2.5-Pro, BrowseComp, 3 runs. ReAct 12.6 at budget 100, 10.3 at 10, 10.5 at 30; with tracker at budget 10: 12.8, with 40.4% fewer search calls, 19.9% fewer browse calls, 31.3% lower cost. Table 1: BrowseComp 12.6 to 14.6; BrowseComp-ZH 31.5 to 32.9; HLE-Search 20.5 to 21.8. SWE-bench Verified 36.8 to 55.4 at budget 50 (from claims.jsonl). | Liu 2025 [d17] | S (K22) |
| Stop at first self-verified answer costs accuracy | BATS continuing: BrowseComp 24.6, BrowseComp-ZH 46.0, HLE-Search 27.0. Early stop at first verified answer: 18.7, 39.1, 23.0. Removing verifier module: 18.7 to 15.4. | Liu 2025 Tables 3-4 [d18] | S (K22, K23) |
| Naive learned stoppers generalise badly | Qwen2.5-3B-Instruct, Qwen3-1.7B. Base and SFT models stop worse than a fixed-turn rule out of distribution (dermatology); CaRT (counterfactual pairs, 80% continue / 20% terminate) beat it. RL lengthened conversations. Exact success rates not extracted. | Liu 2025 CaRT [a28, c19] | S (K16) |
| One router picks model and think mode | Route-to-Reason, Qwen3-4B: 83.8% at 1,321 tokens vs 82.4% at 3,113 always-think (-57.6%), vs 73.4% at 592 never-think. 7 models x 4 strategies: 82.5% at 1,091.3 tokens, +2.5 points and over 60% fewer tokens than QwQ-32B. | Pan 2025 [d19] | S (K25) |
| RouteLLM needs matching data | MT Bench 8.8 at 50% GPT-4 calls = 95% of GPT-4 (9.3); up to 75% cost cut with augmented data; up to 3.66x cheaper. MMLU 75 at 50% calls = 92%; GSM8K 75 = 87%. Trained only on Arena data, routers on MMLU/GSM8K equalled random; in-domain labels gave about 20% fewer GPT-4 calls than random. | Ong 2024 [b09] | S |
| Self-calibration gives a stop signal | MathQA Llama-3.1-8B-Instruct: confidence-weighted SC matches SC with 39.8%, 50.4%, 94.2% fewer samples at three accuracy levels. Budget 16: SC 81.0 vs 83.6 with confidence; ARC-c R1-Distill 1.5B Best-of-N 58.9 vs early stop 66.5. GSM8K ECE 13.70 to 3.79. Needs 2,000 training questions. | Huang 2025 [d21] | S |
| Inverse scaling | Counting with five distractors: DeepSeek R1 70% to 30%; Claude Opus 4 near 100% to about 85-90%; o3 stable. Python-code distractors: Opus 4 near perfect to about 80%. Tasks built to expose the failure. | Gema 2025 [b18] | S |
| Parallel vs sequential disagree | s1: sequential Wait beats voting on a fine-tuned base. Zeng: parallel beats sequential for QwQ/R1-distill/LIMO (40 revision steps vs 10 samples). Different models. | [b15, b25] | C |

---

## 4. Mechanisms and models

Each block says what the program computes. The model only produces answers or one-line self-grades. The program decides.

### 4.1 Vote-stability stopping (AC, Beta form)
- State: counts of each distinct answer so far, `v1 >= v2 >= ...`.
- After each new sample, compute P(top answer stays ahead of the runner-up) from Beta(v1+1, v2+1). Stop when it passes `Cthresh = 0.95`. Cap at 40.
- Worked case [d01, our arithmetic]: 4 unanimous votes give 1 - 0.5^5 = 0.969, so stop. 3 give 0.9375, so continue. So the practical rule at 0.95 is "4 identical answers in a row from the start".
- Dirichlet and Chinese-restaurant forms match Beta but run about four orders of magnitude slower (still negligible beside an LLM call) [a17].
- Cost: samples are drawn one at a time, so the prompt is re-sent each time. Latency rises [b01].

### 4.2 Window stopping (ESC)
- Cut the cap `L` into windows of size `w` (5 default, 8 for hard maths). Draw a window. If all `w` answers are identical (zero entropy), stop. Else draw the next window, up to `L`.
- Why it works [c21]: the stop changes the final vote only if the true leader was outvoted inside one window. That chance shrinks fast with `w`.
- A window shares one prompt, so input tokens are paid once per window [a19, c05].
- A control scheme predicts cost and accuracy change from the first window (Pearson r above 0.8 on GSM8K) [b04].
- Cost of the conservative rule: on hard items the window rarely agrees, so savings vanish [a18].

### 4.3 Difficulty pre-allocation (DSC)
1. Ask the model to rank a batch of questions by difficulty.
2. Pre-sample easy ones once. Give hard ones larger budgets.
3. Count input and output tokens together.

Each of the three steps lowered cost in the ablation [c22]. It needs a batch and the ranking has its own cost [c06].

### 4.4 Reliability-aware two-stage rule (ReASC)
- Stage 1: one sample. Accept if its confidence passes a gate calibrated on 128 held-out items to a target accuracy (0.9). Confidence = bottom-10% group confidence or self-certainty.
- Stage 2: items not accepted go to a confidence-weighted vote with a stop rule [c07, c25].
- The gate must be recalibrated per model: acceptance moved from 7% to 37% on MATH500 and 49% to 61% on GSM8K across model sizes [d07].

### 4.5 Confidence-weighted vote (CISC)
- For each sample `i`, get a confidence `c_i` (best: P(True) from a second call or logprob; worst: verbal binary).
- Weight `w_i = softmax(c_i / T)` within the question. Temperature `T` is tuned per confidence method. Score each answer by summed weight. Pick the top.
- Normalising within the question matters (P(True) saving 32% without, 46% with) [b06].
- Use within-question discrimination, not calibration error, to choose the signal [b07].

### 4.6 Token-level confidence (DeepConf)
- Group confidence = mean token confidence over a 2,048-token sliding window; trace score = lowest window (or bottom 10% of windows).
- Online: run 16 warm-up traces to full length. Set a threshold at a percentile of their lowest group confidence. Later traces stop the moment a window falls below it. Stop everything when vote consensus reaches 0.95 or 512 traces are used [a26, c30].
- Offline: generate all, keep the top fraction by confidence, vote.
- Needs token logprobs and warm-up traces of full length. Fails on confidently wrong traces [b08].

### 4.7 Training-free chain early exit (DEER, Certaindex)
- DEER: at a transition token ("Wait") or an entropy spike, stop thinking. Prompt the model for a trial answer. Measure confidence of that answer. If above 0.95, exit and output it. Else keep thinking [c16, c26]. Too-low thresholds cut reasoning short; too-high saves little.
- Certaindex: at chosen reasoning steps, elicit the intermediate answer across paths. Certaindex = 1 minus normalised entropy of answers (reward-model score for MCTS). If above a profiled threshold, halt [c17, c27].

### 4.8 Difficulty prediction and routing
- Probe (Damani): a small head on hidden states predicts how much extra samples help. Train on 128 samples per training query. Allocate per question [d10].
- Self-evaluation (Manvi): after a draft, one extra token asks "would you do better if you started over?" The probability sets resampling. Thresholds 0.92 or 0.98 with temperature annealing [d11].
- Pass-rate estimate by sampling: 4 samples give a usable easy/hard split; fine bins need about 16 [d12, our simulation].
- Snell: five bins from the base model's pass rate; best strategy per bin. Easy: sequential revision. Hard: mixed parallel and sequential. Search can hurt on easy bins [a22, b11].

### 4.9 Rational-metareasoning stop rule (implementable form)
Myopic form [a01, a04; test K26]:
```
leader = current top answer; stake = value of a correct answer (in tokens)
p_flip = estimated chance the next sample changes the leader
stop when p_flip * stake < cost_of_next_sample
```
- `p_flip` can come from the AC Beta posterior or from the window history.
- Because the myopic rule stops too early (Theorem 7), add a floor: a minimum number of samples before the rule may fire, and a rule that when two or more answers are close the rule continues.
- No LLM test of this form was found [d03, K26].

### 4.10 RaM reward (training, not used in the scaffold)
- `R = log p(y | z, x) - log p(y | x) - lambda * len(z)`. Keep chains with positive advantage. Expert iteration [a12, c10].
- Scaffold analogue: score each step by the change in answer log-prob if the API exposes it, and drop low-gain steps (K13 test).

### 4.11 Budget control
- Budget forcing: end thinking at the cap by appending the end-of-thinking token; extend by suppressing it and appending "Wait" [a23]. Perfect control (100%), but cut mid-thought.
- Prompted limits ("think for N tokens", "N steps", "easy/hard class") reach only 40 to 60% control [c13].
- Trained (L1): the length target is in the prompt, learned by RL [b23].
- Agent loops: a visible "remaining budget" counter each turn [d17].

### 4.12 Trained stoppers for loops
- CaRT: counterfactual pairs. A trajectory where stopping is right, and a minimal edit where it is not, each with a verbal reason. Label: stop if success rate rises by at least 0.5; counterfactual below 0.3 [a28, c19].
- Probe at each intermediate answer: threshold 0.85 [d16].

---

## 5. What holds up

### Holds up (two or more sources, or a direct check)
- **Stop-on-agreement saves samples on easy and mid-difficulty maths and commonsense** (AC, ESC, DSC, ReASC all agree) [K01, K02]. Accuracy change within about 0.2 on average against SC-40.
- **The saving depends on difficulty and model strength.** Weak model plus hard task gives almost no saving (ESC Llama-2-7B MATH; ReASC 7.2%) [K02].
- **The saving depends on the baseline and on token accounting.** SC-40 or 512 flatters the method. Against SC-16, ESC saves 4% to 71%. With the prompt re-sent each round, ASC cost +74% and ESC +3% on Mistral-7B GSM8K [K19]. The original SC paper says 5 to 10 samples capture most of the gain, so the fair baseline is small [a15].
- **Longer is not better within one question.** Correct chains are shorter than wrong ones (two papers) [K08]. Confounder: hard questions draw long chains [b13].
- **Overthinking on easy items is real** (first solution correct in over 92%, three sources) [K09].
- **Reflection and unaided self-revision seldom help.** Over 90% of reflections confirm; wrong-to-right under 2%; prompted self-correction without a label lowers accuracy; with an oracle it raises it [K21]. The thing that matters is an outside signal.
- **A checker is only as good as its false-pass rate** [K23].
- **Myopic stopping is too early** (theory; two papers) [K15].

### Failures, boundary conditions, competing explanations
- **Wrong consensus is untested for vote rules.** AC and ESC compare with SC-40, so they measure agreement with SC, not correctness [d01]. Direct counts exist only for confidence gates (1.4 to 13.9% wrong among accepted) [d07]. Models share wrong answers (0.42 to 0.60 agreement when both wrong) [d06]. Brown et al.: many problems have a wrong majority and a rare right answer [d04]. This is the main open risk (K18, contested).
- **Verbal confidence is weak.** Within-question discrimination 52 to 56%; best-calibrated signal gave the worst saving [b07]. Consistent with section 4b of SCHEMA.md.
- **DeepConf is not robust.** Top-10% filtering lost up to 4.69 points in eight of 20 settings; Qwen3-8B AIME25 -4.4 [a26, c18]. Only one component was reused by an outsider (AUROC 0.860 vs 0.801) [d20]. No outside re-run of the online stop, DSC or ReASC, and none outside maths (K27). Citation lookups were blocked, so absence is unproven.
- **Every stop-rule comparison is run by the authors of the newest rule** (DSC, ReASC, DeepConf, BATS, Route-to-Reason). No independent head-to-head [critique].
- **RaM's accuracy gain is inside noise** (+/-1.7); the 8B model lost 3.8 points out of domain (36.4 vs 40.2) [c11, critique].
- **s1's lift is two problems.** AIME24 has 30 problems; 50.0 to 56.7 is two items, on the same benchmark that tuned the method [critique].
- **Sequential vs parallel is unresolved.** s1 says sequential beats voting; Zeng says the opposite for distilled reasoners [b15, b25]. A compatible reading: forcing helps when the model stopped too early and hurts when it already answered; no paper tests that split. Kang et al. suggest reflection pays little and only on the few items where the first answer was wrong [d14].
- **Learned stoppers generalise badly unless built for it.** Base and SFT models stop worse than a fixed-turn rule out of distribution; probes fail across domains; routers equal random out of distribution [a28, d16, b09].
- **Stopping an agent at its own first verified answer lost 6 to 8 points** against continuing, although the arms used different total budgets [d18].
- **Search can hurt on easy items** (beam search gets worse with budget on levels 1-2; verifier over-optimisation) [b11].
- **A reward model as stop signal was no better than random selection** in the self-calibration paper; its 1.2-sample result needs annealing and a trained head [critique, d11].

### Interventions that worked / did not
| Worked | Did not work |
|---|---|
| Window or Beta stop on easy/mid maths | Stop on verbal confidence |
| Confidence-weighted vote with P(True) | Unaided reflection or self-correction |
| Pre-allocation by difficulty rank | Prompting a token budget in words |
| Visible budget counter in agent loops | Stopping an agent at its own first verified answer |
| Early exit at "Wait" with an answer-confidence check (DEER) | Rejection sampling to short length (selection bias) |
| Trained length control (L1) | Reward model as stop signal |
| Counterfactual-pair training for stoppers | Naive SFT stoppers out of distribution |

---

## 6. Language models

### How they behave
- **Old chat models (GPT-3.5, GPT-4, Vicuna, code-davinci, Llama-2):** agreement rules were designed and tested here. Stronger models agree sooner. AC: GPT-3.5 4.4x, Vicuna 1.9x [d02]. Unaided self-correction lowers accuracy (Huang 2024) [d15].
- **Reasoning models (R1-family, QwQ, o1-like, Qwen3, GPT-OSS):** they overthink easy items and produce long, repetitive chains. Correct answers come early; wrong ones run long [K08, K09]. Early exit cuts 19 to 80% of chain length with accuracy flat or up (DEER) [c16].
- **Frontier models:** longer reasoning can lower accuracy on constructed tasks with distractors. Effects differ by family: R1 70% to 30%, Opus 4 to about 85-90%, o3 stable [b18].
- **Small models (3B to 8B):** stop rules save little on hard sets; gates need per-model calibration; search lifts a small model only where it already has some success [K02, K24, c24].

### What changed things, by how much
| Change | Size of effect | Evidence |
|---|---|---|
| Stop on stable vote | 2x to 5x fewer samples vs SC-40; 4% to 71% vs SC-16; near zero or negative once prompts are counted | K01, K19 |
| Difficulty pre-allocation on top of ESC | a further 21.9 to 24.8% cost cut | K03 |
| Confidence-weighted vote | 31 to 46% fewer samples at budget 10 | K04 |
| Token-confidence trace cutting | 43 to 85% fewer tokens, accuracy about equal, with exceptions | K05 |
| Early exit at "Wait" | chain 19 to 80% shorter, accuracy +0.3 to +5.0 | K09 |
| Training on shortest correct answers | 35 to 49% fewer tokens, accuracy within about 1 point except AIME24 (-3.4) | a25 |
| Forced Wait | +0.4 to +6.7 points, flat after 2x to 4x | K11 |
| Difficulty-based allocation | up to 4x compute on MATH (one model) | K07 |
| Router over think mode | -57.6% tokens at +1.4 points (Qwen3-4B) | K25 |
| Visible budget counter | 31.3% lower cost at equal budget 10; score near the budget-100 score | K22 |

Most numbers are on maths with an auto-checkable answer. Open-ended reasoning and agent tasks have no answer to vote over [critique].

---

## 7. What our agent should take

Status marks: **[E]** established, **[S]** single-source, **[C]** contested. Schema part: G guardrail, S state, O operator, M memory.

### Add now (established)

1. **Report cost as total tokens, input plus output, and compare against fixed k = 4, 8 and 16, not only 40.** Part: G7. [E] K19; ids d08, d09, d11, c22. Reason: headline savings shrink or vanish otherwise.
2. **Stop sampling on a stable vote, as a code rule, with a floor and a cap.** Part: S3 (direct, checked and no-check modes), G11. [E] for the saving, K01, K02; ids a16, a18, b01, b03, c02, c04, d01, d08. Rule: 4 identical answers in a row (AC Beta at 0.95) or one all-agree window of 4 to 5, cap 8 to 16. Treat the stop as a hint of agreement, not proof (G4); the wrong-consensus risk is tested in T1 below.
3. **Set the budget by problem class from the class record.** Savings and pass rates vary by difficulty and model strength; plain pass rate and agreement record already live in memory. Part: S0, M, G12. [E] K02; ids a18, c07, d02, d07.
4. **Prefer cap-and-restart over extend.** Within one question, correct chains are shorter; do not request longer thinking when a chain runs long. Part: G11, S3. [E] K08; ids b13, b17, a25.
5. **Do not request more reflection after the first complete solution by default.** Over 90% of reflections confirm; first candidate is within 1.4 to 3.5 points of final. Part: G1, G2, G11, S5. [E] K21; ids d14, d15, a25, b16, c23.
6. **Only trust a pass as a stop if the checker's false-pass rate has been measured.** Part: S4, S8, G3. [E] K23; ids d04, d05, d15, d18.
7. **Keep the stop decision in code and give it a cost term.** The theory says stop when expected gain is below cost, and that the myopic rule stops too early; keep a minimum-sample floor. Part: G5, S3, S6. [E] K15; ids a01, a04, b19.
8. **Verbal confidence is not a stop signal.** Already in 4b; K17 and b07 add the within-question numbers (52 to 56%). [E] K17 on the verbal part.

### Test first

| # | Item | Schema part | Status | Evidence ids |
|---|---|---|---|---|
| T1 | Vote-stability stop: how often does a unanimous early stop land on a wrong answer? Add a second-signal check | G stop, S3, S4 | [C] K18 | d01, d04, d06, d07, d13 |
| T2 | Myopic VOC stop with cost term vs ESC window at equal tokens | G, S3 | [S] K26 | d03, a04, b19 |
| T3 | Route on a 2 to 4 sample pass-rate class (easy, medium, hard) | S0, G12 | [C] K20 | d10, d11, d12, b10 |
| T4 | Forced re-check at the stop point, paired flips by first-answer correctness | S5, S8 | [S] K11 | a23, b14, c12, d14, d15 |
| T5 | Difficulty-aware pre-allocation (DSC) vs ESC | S0, S3 | [S] K03 | c06, c07, c22 |
| T6 | Confidence-weighted vote with a P(True) self-grade | S7 | [S] K04 | a20, b06, b07 |
| T7 | Visible remaining-budget counter vs hidden cap in agent loops | G, S3, S5 | [S] K22 | d17, d18 |
| T8 | Calibrate the stop gate per model on 50 to 100 labelled items | G stop, M | [S] K24 | d02, d07 |
| T9 | Early exit at a transition with a trial-answer confidence check (DEER-style) | G11, S3 | [S] K09 | c16, c26, c17 |
| T10 | Stop-on-pass vs stop-on-agreement when a checker exists | S4, S7, S8 | [S] K23, K06 | d04, d05, a21, b12 |
| T11 | Length cap with restart vs prompted limit vs hard cutoff | G11 | [S] K12, K08 | b13, b17, c13, b23 |
| T12 | Router over no-think / short think / long think | S0 | [S] K25 | d19, d10 |
| T13 | Partial-answer agreement as a proxy for DeepConf when logprobs are missing | G stop | [S] K05 | a26, b08, c18 |
| T14 | Revision kept only if net flips are positive | S5 | [S] K10 | b13, b25, d14 |

---

## 8. Concrete tests on our bench

All arms get **equal mean total tokens per item** (input plus output). Report accuracy with a 95% interval, mean total tokens, and tokens per correct answer. Use at least 100 paired items per arm pair (AIME24 has 30 items; do not tune and test on it). Log per run as SCHEMA section 6 requires. Test numbers match UNKNOWNS.md (U1 to U12).

| Test | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| U1 wrong consensus | Labelled ARC items and BRAINTEASER items; plus a maths set | Stop at 4 unanimous votes (A) vs A plus second-signal check (checker or different-prompt sample) (B) vs fixed k=8 vote (C) | Share of stopped items that are wrong, split by task and difficulty; accuracy at equal tokens | Wrong share small on easy maths, large on hard or puzzle items; second check catches a share of them |
| U2 VOC vs window | Any item set with a check | ESC window 4 vs myopic VOC rule (p_flip x stake < cost) with floor of 3 samples | Accuracy, tokens at equal mean tokens | VOC rule within 1 point; gain only if p_flip is well estimated |
| U3 difficulty route | Mixed pass-rate set | Fixed best-of-4 vs 3-class route from 3 to 4 samples vs oracle bins | Accuracy, tokens | Route keeps most of the oracle saving at 3 classes; may lose at high budget (Damani) |
| U4 forced re-check | Items with a known first answer correct/wrong | One pass vs one pass plus one forced re-check (cost matched by dropping one sample from the other arm) | Wrong-to-right and right-to-wrong flips, split by first-answer correctness | Net flips near zero overall; small gain only on first-wrong items |
| U5 pre-allocation | Batch of 100+ items | ESC vs DSC-style rank-then-allocate | Total tokens at matched accuracy | 15 to 25% fewer tokens (claimed by DSC) |
| U6 weighted vote | Items at budget 5 and 10 | Plain vote vs P(True)-weighted vote | Accuracy at equal total tokens including the extra call | +0.2 to +1.1 points; may vanish once the extra call is counted |
| U7 budget counter | One agent task family | Hidden cap vs visible counter vs model-chosen stop | Success, cost | Counter lowers cost with equal success; model-chosen stop loses on a held-out family |
| U8 per-model gate | Labelled items per model | One global threshold vs per-model calibrated | Wrong-accept rate at a target accuracy | Calibrated gate holds the target; global one over- or under-accepts |
| U9 early exit | Reasoning-model items | Full trace vs exit at a transition when the trial answer is stable | Accuracy, tokens | 20 to 50% fewer tokens, accuracy flat |
| U10 pass vs agree | Code or checkable items | Stop on checker pass vs stop on agreement | Accuracy, tokens, false-pass rate | Pass wins if false-pass rate is low; measure the rate first |
| U11 cap and restart | Hard items | One long chain vs cap then restart vs two short chains | Accuracy by length quantile within item | Negative length slope within item means restart beats extension |
| U12 think-depth route | Mixed items | Best fixed mode vs route among no-think, short, long | Accuracy, tokens | Fewer tokens at equal accuracy; maths-heavy source, so check on puzzles |

Baseline that must be in every test: a plain model with a fixed k of 4 to 8 samples and a vote (G7).

---

## 9. What does not transfer, and why

- **Agreement-based stopping needs a short exact answer to vote over.** Open mode (novel ideas, free text) has no answer to count. Only CaRT touches agent dialogue, and only its recipe was read [critique].
- **Theory assumes independent computations with known cost.** Russell and Wefald and Hay et al. cover independent arms and a known probability model. LLM reasoning steps depend on each other, and the value of a step is not observed. No paper shows a theory-derived stop rule beating a heuristic on LLM reasoning; RaM is the only bridge and it trains weights [a04, critique].
- **Anytime profiles are unknown per problem** [a03].
- **Human studies are not stop thresholds.** Lieder and Griffiths use MTurk adults on sorting and small gambles with explicit strategies. They support the framework, not a threshold for LLMs [a06, a07].
- **Training-based methods do not apply.** RaM, L1, SimPO shortening, CaRT, probes, self-calibration and RouteLLM all train something. Our agent is a scaffold [K13, K12]. Their lesson (reason only when it pays) is used as a design aim, not a method.
- **Logprob methods need API access.** DeepConf and P(True) need token probabilities or an extra call [K05].
- **Savings numbers are not comparable.** Samples (AC, ESC, CISC), tokens (s1, L1, DeepConf), FLOPs (Snell). Baselines are 40, 64, 512 or 10 [b26].
- **Maths-only evidence.** GSM8K, MATH, AIME and short commonsense QA. Puzzles with correlated errors are different.
- **Old models.** AC and ESC tested 2023-era models. The unaided self-correction results (GPT-3.5, GPT-4) are from chat models, not reasoning models [d02, d15].
- **Sequential sampling raises latency** and re-sends the prompt [b01, c22].
- **Fine-tuned conditions.** s1's gain is for a 32B model fine-tuned on 1,000 traces [b14].

---

## 10. Open questions

1. How often does a stable-vote stop fire on a wrong answer, on non-maths and overconfident items? (K18)
2. Is there a prompt-only stop rule for free text that beats a fixed turn cap and a visible budget counter?
3. Does a myopic VOC rule with a cost term beat a window rule at equal tokens? (K26)
4. Can a 2 to 4 sample difficulty class keep Snell's allocation gain? Snell used 2048 samples per question to define bins. (K20)
5. Paired test of forced "Wait": what is the right-to-wrong rate, split by first-answer correctness? (K11, K21)
6. Total tokens (input plus output) of ESC, AC and DeepConf against fixed k = 5 to 10, on reasoning models.
7. Do small and large models need different thresholds? Agreement rules adapt alone; confidence gates do not. (K24)
8. Has anyone outside the authors replicated DeepConf's online stop, DSC or ReASC, and on non-maths tasks? (K27)
9. Can one router handle both model choice and think depth? (K25) Early evidence only.
10. When a checker exists, how much better is stop-on-pass than stop-on-agreement at equal tokens, once checker leaks are counted? (K23)
11. Is the s1 versus Zeng disagreement (sequential vs parallel) explained by early-stop versus already-answered items?
12. Do reasoning models lose accuracy past a length because of the task, the distractors, or the sampler? (Gema; no cause tested)

---

## 11. Sources

[V] = opened and read this session (full text, HTML or PDF, or a page-extraction tool where noted). [M] = snippet, abstract or second-hand only.

| Source | Status | URL | Evidence ids |
|---|---|---|---|
| Russell (1997) Metareasoning, MIT Encyclopedia of the Cognitive Sciences | [V] | https://aima.eecs.berkeley.edu/~russell/papers/mitecs-metareasoning.pdf | a01-a03 |
| Russell and Wefald (1991) Do the Right Thing | [M] second-hand only | https://mitpress.mit.edu/9780262181440/ ; https://doi.org/10.1016/0004-3702(91)90015-C | a29, b20, c20 |
| Hay, Russell, Tolpin, Shimony (2012/2014) Selecting Computations | [V] | https://arxiv.org/abs/1207.5879 ; https://arxiv.org/abs/1408.2048 | a04, a05, b19 |
| Callaway et al. (2018) Learning to select computations | [M] abstract | https://arxiv.org/abs/1711.06892 | a11 |
| Lieder and Griffiths (2017) Strategy selection as rational metareasoning | [V] | https://cocosci.princeton.edu/falk/Strategy%20selection%20as%20rational%20metareasoning.pdf | a06-a10 |
| Lieder and Griffiths (2020) Resource-rational analysis (commentary page only) | [V] commentary | https://pmc.ncbi.nlm.nih.gov/articles/PMC7702215 | b21 |
| Lieder, Shenhav, Musslick, Griffiths (2018) Rational metareasoning and plasticity of cognitive control | [V] | https://pmc.ncbi.nlm.nih.gov/articles/PMC5937797 | b22 |
| De Sabbata et al. (2025) Rational Metareasoning for LLMs (RaM) | [V] (Table 1 row labels garbled) | https://arxiv.org/abs/2410.05563 | a12-a14, c10, c11 |
| Wang et al. (2022) Self-Consistency | [M] summary and secondary use | https://arxiv.org/abs/2203.11171 | a15, b05, c28 |
| Aggarwal et al. (2023) Adaptive-Consistency | [V] | https://arxiv.org/abs/2305.11860 | a16, a17, b01, b02, c01-c03, d01-d03 |
| Li et al. (2024) Early-Stopping Self-Consistency | [V] | https://arxiv.org/abs/2401.10480 | a18, a19, b03, b04, c04, c05, c21 |
| Wang et al. (2025) Difficulty-Adaptive Self-Consistency | [V] | https://arxiv.org/abs/2408.13457 | c06, c22, d09 |
| RASC (arXiv 2408.17017) | [V] summary | https://arxiv.org/abs/2408.17017 | a27 |
| Taubenfeld et al. (2025) Confidence Improves Self-Consistency | [V] | https://arxiv.org/abs/2502.06233 | a20, b06, b07 |
| Kim et al. (2026) Reliability-Aware Adaptive Self-Consistency | [V] | https://arxiv.org/abs/2601.02970 | c07, c25, c29, d07, d08, d20 |
| Brown et al. (2024) Large Language Monkeys | [V] | https://arxiv.org/abs/2407.21787 | a21, b12, d04, d05 |
| Snell et al. (2024) Scaling LLM test-time compute optimally | [V] (re-opened in critique) | https://arxiv.org/abs/2408.03314 | a22, b10, b11, c08, c09, c24 |
| Damani et al. (2024) Learning How Hard to Think | [V] | https://arxiv.org/abs/2410.04707 | d10 |
| Manvi, Singh, Ermon (2024) Adaptive Inference-Time Compute | [V] | https://arxiv.org/abs/2410.02725 | d11 |
| Ong et al. (2024) RouteLLM | [V] | https://arxiv.org/abs/2406.18665 | b09 |
| Pan et al. (2025) Route to Reason | [V] | https://arxiv.org/abs/2505.19435 | d19 |
| Muennighoff et al. (2025) s1: Simple test-time scaling | [V] | https://arxiv.org/abs/2501.19393 | a23, a24, b14, b15, c12, c13 |
| Aggarwal and Welleck (2025) L1 | [V] | https://arxiv.org/abs/2503.04697 | b23, c14 |
| Chen et al. (2024) Do NOT think that much for 2+3=? | [V] | https://arxiv.org/abs/2412.21187 | a25, b16, c15, c23 |
| Su et al. (2025) Between Underthinking and Overthinking | [V] | https://arxiv.org/abs/2505.00127 | b17 |
| Zeng et al. (2025) Revisiting the test-time scaling of o1-like models | [V] (table values garbled) | https://arxiv.org/abs/2502.12215 | b13, b25 |
| Gema et al. (2025) Inverse Scaling in Test-Time Compute | [V] | https://arxiv.org/abs/2507.14417 | b18 |
| Yang et al. (2025) DEER | [V] | https://arxiv.org/abs/2504.15895 | c16, c26 |
| Fu et al. (2025) Certaindex / Dynasor | [V] | https://arxiv.org/abs/2412.20993 | c17, c27 |
| Fu et al. (2025) Deep Think with Confidence | [V] (HTML) | https://arxiv.org/abs/2508.15260 | a26, b08, c18, c30 |
| Kang et al. (2025) First Try Matters | [V] via page-extraction tool | https://arxiv.org/abs/2510.08308 | d14 |
| Huang et al. (2024) LLMs cannot self-correct reasoning yet | [V] | https://arxiv.org/abs/2310.01798 | d15 |
| Zhang et al. (2025) Reasoning models know when they're right | [V] | https://arxiv.org/abs/2504.05419 | d16 |
| Liu et al. (2025) Budget-aware tool use (Budget Tracker, BATS) | [V] | https://arxiv.org/abs/2511.17006 | d17, d18 |
| Liu et al. (2025) CaRT | [V] recipe level; exact rates not recorded | https://arxiv.org/abs/2510.08517 | a28, b24, c19 |
| Huang et al. (2025) Efficient test-time scaling via self-calibration | [V] | https://arxiv.org/abs/2503.00031 | d21 |
| Kim, Garg, Peng, Garg (2025) Correlated errors in LLMs | [V] via page-extraction tool | https://arxiv.org/abs/2506.07962 | d06 |
| Our own simulations (pass-rate estimate; wrong stops at 4 unanimous votes) | [M] model, not literature | n/a | d12, d13 |
