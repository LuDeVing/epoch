# Resource-rational analysis: deep document

*Subfield E18.09. Key work: Lieder and Griffiths 2020 (BBS 43:e1). Why it matters for our agent: it is the theory behind the S0 gate and behind meta-reasoning (deciding how much to think). Evidence ids (a01..d16) and claim ids (E18.09-K01..K25) refer to the jsonl files in this folder. Status tags: [E] established, [S] single-source, [C] contested.*

## 1. What it is

Resource-rational analysis (RRA) is a method for building theories of cognition. It asks: what is the best way to think, given the task, the environment, and the limits of the mind? "Best" means the highest expected result minus the cost of the computing used to get it.

The core rule (Lieder and Griffiths 2020, Eq. 3, a01):

- h* = argmax over heuristics h of ( expected utility of the result of h minus expected cost of the time and resources h uses ).
- Cost is the opportunity cost of the time, plus any use of limited memory or elementary operations.
- Eq. 4 (a03): because the world is not fully known, the best heuristic is the one best on average over environments consistent with what the agent has learned.

Key points for engineering:

1. The optimisation is done by evolution and learning, not by the person on the spot. The authors say "people never have to directly solve the constrained optimization problem" (a01). So the rule is a design target. It is not a per-problem rule you can run.
2. It differs from classic rational models (no cost of thinking) and from Stigler-style information economics (cost of collecting data only). It charges for the cost of thinking itself (a09).
3. It is a "methodological device", at worst a "convenient template for slightly less unrealistic as-if explanations" (a01).
4. The five steps (a02): (1) state the function as a computational-level problem; (2) posit an algorithm class, its costs, and the utility of accuracy; (3) find the algorithm that best trades accuracy for cost; (4) test its predictions against behaviour; (5) refine the assumptions about costs and constraints.

For the agent: every extra token of thinking has a price. The S0 gate should spend thinking only where the expected gain in correctness is larger than that price. A large 2024-2026 engineering literature on test-time compute is, in effect, an empirical test of this idea in LLMs. Most of those papers do not mention resource-rationality, so we use them as a proxy for "value of computation" (critique.md).

## 2. History and theories in depth

### 2.1 Foundations in AI (1991-2015)

- Russell and Wefald 1991, "Principles of metareasoning" (a31, snippet only). Choose a computation if its expected value exceeds its cost; stop when expected benefit falls below cost. The exact solution is itself too costly. The BMPS paper opens by contrasting Deep Blue's 200 million positions per second with Kasparov's about 3.
- Russell and Subramanian 1995, "Provably bounded-optimal agents" (a10). Separates four goals: perfect rationality (impossible, thinking takes time), calculative rationality (eventually returns what was rational at the start), metalevel rationality, and bounded optimality (the best program the machine can run). The last is the target. Includes asymptotic bounded optimality (worst-case and average-case).
- Lewis, Howes and Singh 2014, computational rationality (a11). Fix a processor with its limits, fix the environment and utility, find the optimal policy on that processor, compare with behaviour. Re-reported fit: a serial bounded machine predicted second-task response time with mean R2 of 89%, 84%, 77%, 85% across four dual-task experiments.
- Gershman, Horvitz and Tenenbaum 2015 (a12). AI, cognitive science and neuroscience converge on intelligence as maximising expected utility net of the cost of computation. Metalevel reasoning picks the algorithm and the stopping time t*.
- Gabaix and Laibson 2005 and Gabaix et al. 2006 (a09, b09). A myopic cost-benefit rule (pick the next computation by immediate expected gain minus cost) predicted human search in a bandit task and in multi-attribute choice better than earlier models. Numbers not given in the review.
- Related frameworks named by the founding paper (a02): rational process models, Sims' rational inattention.

### 2.2 The Griffiths lab programme (2014-2022)

- **Algorithm selection by rational metareasoning** (Lieder et al. 2014, a13). Value of computation VOC(a; i) = E[score] minus E[opportunity cost of runtime]. A learned model picks a sorting algorithm from a few input features. Correct choices: 99.78% vs 98.5% (Guo decision tree), 99.99% vs 99.4%, 83.37% vs 77.0%, 99.99% vs 85.3% on four test sets, all p < 1e-15.
- **Human test of the same idea** (a14). N = 100 Mechanical Turk workers trained on cocktail and merge sort (11 training trials), then chose a strategy on 18 test lists. 83% chose merge sort more often when it was superior (95% CI 74.9-89.4, p < 1e-11). Merge sort was chosen on 81.67% of long, nearly inversely sorted lists but only 29.83% (long) and 27.00% (short) of nearly sorted lists.
- **When to use which heuristic** (Lieder and Griffiths 2015, a15; full version 2017 in Psych Review, a16, abstract only). People learn how well each heuristic does on problems with given features and pick by expected quality minus cost. Loan-decision study N = 120: 64.6% correct choices (99% CI 62.5-66.6, p < 1e-15 vs chance). Worse on non-compensatory than compensatory trials, as in Rieskamp and Otto 2006.
- **Automatic derivation of bounded-optimal heuristics** (b05). Found a new strategy mixing satisficing and Take-The-Best (SAT-TTB). A follow-up experiment found people use it where it is bounded-optimal (N not read).
- **One and done** (Vul, Goodman, Griffiths, Tenenbaum 2014, a19, d15). A sample-based agent that pays time for each sample should often take very few. Optimal k = 1 when the ratio of action time to sample time is under 10 (symmetric utility). With no penalty for error the ratio must be 2 or more before any sample pays. The review gives a simpler threshold of about 3x for exact probability matching (a04, b03). Re-analysis of 25 probability-matching studies: stakes vs effective samples r(25) = .61, p = .0013, 95% CI .28-.81. It also explains Hick's law and response variability.
- **Anchoring as rational adjustment** (Lieder, Griffiths, Huys, Goodman 2018, a17, a18, d13). Estimates move from an anchor by repeated small accept/reject steps. The best number of steps trades time cost against error cost. The model reproduces ten anchoring phenomena (time pressure, load, alcohol, incentives, forewarning, anchor extremity). Provided anchors (Jacowitz and Kahneman 1995): anchoring index about 50%, fitted 29 adjustments, step 22.4. Self-generated anchors (Epley and Gilovich 2006): fitted 8 adjustments, step 10.06, model adjusted 80.62% of the distance vs 80.95% observed. The companion experiment (d13) varied time cost and error cost independently; adjustment fell as time cost rose and rose as error cost rose.
- **Learned Value of Control** (Lieder, Shenhav, Musslick, Griffiths 2018, a20, b10). People learn by reinforcement the value of control signals from stimulus features, with an effort cost. It predicted learning and transfer across 5 experiments (one visual attention, four Stroop/Flanker). Rescorla-Wagner MSE 3.33 vs LVOC 1.35 in one experiment. Win-Stay Lose-Shift failed to show gradual improvement.
- **BMPS: learning to select computations** (Callaway, Gul, Krueger, Griffiths, Lieder 2018, a22, b11, c05, c06). See section 4.2.
- **Planning** (Callaway et al. 2022, d07). Four Mouselab-style planning experiments. See section 3.
- **Fixation and gaze** (Callaway, Rangel, Griffiths 2021, a21). Gaze in food choice treated as information sampling; best to sample options with high and uncertain value. Data: 70 snacks rated, 100 choices, eye position at 50 Hz.
- **Task decomposition** (Correa et al. 2020, a23). Choosing subgoals as a resource-rational problem; reproduces Solway et al. 2014 Experiments 1-4 qualitatively.
- **Explore-exploit** (Godara and Aleman, a24). Meta Bayes-adaptive MDP; as the cost of computation rises the value of planning falls. Policies evaluated with 1e5 simulated agents per setting.

### 2.3 Critics and competing views

- Degrees of freedom (b07, a08): adding cost and capacity adds free parameters. The authors say RRA adds two (resources and their costs), that they can be measured independently, and that models should be judged on phenomena they were not built for.
- Costs are usually fitted, not measured (a08). In anchoring, fitted adjustment counts are 8 vs 29 across datasets (a17, a18).
- Neural noise view (Beck et al. 2012, b06): measured neural noise is too small to explain suboptimality; the brain may use approximations with systematic bias. Reply: approximations are bounded-optimal under complexity limits.
- Old view (b27): people "think too little". RRA reply: apparent underthinking can be an optimal stop. No decisive discriminating experiment is reported beyond anchoring and sampling.
- Warwick group (Sanborn, Zhu, Chater; d15): builds on sampling as the key constraint but argues resource-rationality cannot settle the constraints.
- Boundary conditions named by the authors (a08, b08): needs enough adaptive pressure and experience; hard to apply during adaptation to a new environment, for rare low-stakes situations, and when environment or constraints are unknown. Example: a memory strategy tuned for span 7 may be bad for a person with span 4.

### 2.4 The LLM turn (2022-2026)

Three strands:
1. Explicit use of the framework: rational metareasoning as a training reward (De Sabbata et al. 2024, a25), and tests of whether LLMs behave resource-rationally (Hu et al. 2026, a27; R3-Bench, a28; Fan et al. 2026, d01).
2. Engineering work on test-time compute: difficulty-based allocation (Snell et al.), budget control (s1, L1, TALE), early exit (DEER, probes, DeepConf), stopping rules (Adaptive-Consistency, ESC), overthinking diagnosis (Chen et al., Cuadron et al.), sleep-time compute.
3. LLMs as models of human decision-making (Liu et al., Binz and Schulz), which shows LLMs are not themselves human-like resource-rational agents.

## 3. Core findings with exact numbers

"Status" uses [E]/[S]/[C] and the claim id.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Optimal cognition = best result minus cost of computing; solved by evolution and learning, not online | Eq. 3 and Eq. 4 | Lieder and Griffiths 2020 (a01, a03) | [E] K01 |
| People choose sorting strategy by cost-benefit | N=100; 83% chose merge sort more when superior (CI 74.9-89.4); 81.67% on long near-inverse lists vs 29.83% / 27.00% on nearly sorted | Lieder et al. 2014 (a14) | [S] K02 |
| People choose heuristics by learned expected quality minus cost | N=120; 64.6% correct (99% CI 62.5-66.6) | Lieder and Griffiths 2015 (a15) | [S] K02 |
| Learned strategy selector beats rival selectors | 99.78 vs 98.5; 99.99 vs 99.4; 83.37 vs 77.0; 99.99 vs 85.3 (% correct choices, 4 test sets) | Lieder et al. 2014 (a13) | [S] K02 |
| One mental sample is bounded-optimal when acting is cheap relative to sampling | k=1 for action/sample time ratio under 10 (symmetric utility); under about 3x for exact probability matching; stakes vs effective samples r(25)=.61, CI .28-.81 | Vul et al. 2014 (a19, a04) | [E] K03 |
| Anchoring fits an optimal stop in sequential adjustment | 10 phenomena; fitted adjustments 29 (provided anchors) vs 8 (self-generated); model 80.62% vs data 80.95% of distance | Lieder et al. 2018 (a17) | [C] K04 |
| Anchoring moves with experimentally set time and error cost | Adjustment down with time cost, up with error cost; two experiments, N not read | Lieder et al. 2018 (d13) | [S] K25 |
| People plan near a cost-sensitive optimum, with departures | Exp 1: 95 analysed; 0.92 points below best at same clicks; 4.94 above random (CI 4.43-5.44); max-value path expanded 81.5% (CI 79.6-83.3); best fit: 45 optimal, 41 best-first, 9 other. Analysed in Exp 2/3/4: 298, 291, 93. The widely quoted "86% / 55%" is NOT in the primary paper | Callaway et al. 2022 (d07) vs review (a05, b02) | [C] K05 |
| Learned metalevel policy near optimal in small worlds | 99.1% (0.6535 vs 0.6596; meta-greedy 0.60, full deliberation 0.20, DQN 0.58); 98.4% on planning trees; 6.78-35.8% better than meta-greedy; within 5.19% on stopping task | BMPS (a22, b11, c05) | [S] K06 |
| Metareasoning pays its own cost when object-level computation is far dearer | Metareasoning about 1 ms (10 cities), 3 ms (30 cities), at most one simulation | Callaway et al. 2018 (c06) | [S] K06 |
| LVOC beats rivals on control learning | 5 experiments; MSE 3.33 (Rescorla-Wagner) vs 1.35 | Lieder et al. 2018 (b10) | [S] |
| Value-of-computation reward cuts LLM tokens | 8B: 63.5% acc, 146.2 tok vs STaR 61.9%, 215.1 (-32.0%); 3B: 50.1%, 170.8 vs 47.4%, 222.7 (-23.3%); vs few-shot CoT -34.8% and -42.3%; cost weight 0.1 | De Sabbata et al. 2024 (a25, c02) | [S] K07 |
| That model adapts length to difficulty | Easy vs hard tokens: RaM 72 vs 145 (-50.3%), 89 vs 139 (-36.0%); STaR -34.4% / -35.9%; few-shot CoT -19.0% / -23.5%; instruct CoT -0.5% / -0.9% | De Sabbata et al. (a26, c03) | [S] K08 |
| Same model out of distribution | MMLU-CF: 3B 29.5 vs 27.0 (STaR); 8B 36.4 vs 40.2 (-3.8); tokens -28 to -36% | De Sabbata et al. (b14, c03) | [S] K07 |
| Reasoning models overthink easy items | "2+3": 1,953% more tokens than conventional models, 13 solutions; first solution correct in over 92% of cases; first round under 60% of tokens (QwQ on ASDIV: 287 tokens, 38.7%) | Chen et al. 2024 (b15, c09) | [E] K09 |
| Self-training removes overthinking | QwQ-32B: GSM8K 94.8->96.0, 772.8->416.6 tok (-46.1%); MATH500 93.0->92.8 (-44.7%); GPQA 59.6->59.1 (-35.4%); AIME24 46.7->43.3 (-45.6%) | Chen et al. (c09) | [E] K09 |
| Early exit shortens chains at no accuracy cost | DEER: 11 models, 10 benchmarks, -19.1% to -42.9% CoT, +0.3 to +5.0 acc, latency -27.9% to -40.1%. Probe: 88.2% = no-exit, 24% fewer tokens (threshold 0.85); at matched tokens beat static exit by up to 5 points (87.4 vs about 82.5) | Yang et al. 2025 (c14, d11); Zhang et al. 2025 (b24, d05) | [E] K10 |
| Shorter chains are more often right | Shortest of k up to 34.5% more accurate than longest; +2.2 to +15.7 over random; short-1@k matches majority vote with up to 40% fewer thinking tokens; short-3@k up to 33% faster | Hassid et al. 2025 (c16) | [E] K10 |
| Confidence-filtered voting | DeepConf-low cuts 43-79% tokens vs a 512-vote majority; DeepSeek-8B mean 62.88% (low), 47.67% (high); +5.8 AIME24, -0.9 BRUMO25; offline filter helped 12 of 20 settings, hurt 8 (-0.31 to -4.69) | Fu et al. 2025 (d04) | [S] K19 |
| Sequential stopping of self-consistency | Adaptive-Consistency, 17 datasets, 3 models: 3.3x fewer samples (up to 7.9x), accuracy drop 0.07 point; stop-rule compute 0.03 ms; at equal cost up to 5 points better than SC. ESC: samples -33.8% (MATH), -80.1% (GSM8K), -76.8% (StrategyQA), -78.5% (CSQA), -84.2% (Coin Flip), -67.4% (Last Letters) | Aggarwal et al. 2023 (c17, d10); Li et al. 2024 (c18) | [E] K11, K21 |
| Allocate compute by difficulty | About 4x less compute than best-of-N (2-4x in body); small model with test-time compute beat a roughly 14x larger one on easy and medium items; 5 difficulty bins from 2,048 samples; MATH 12k train / 500 test | Snell et al. 2024 (b19, c07) | [E] K12 |
| More thinking is not monotonic | R1-Distill-1.5B GSM8K 82.2 -> 87.3% (385 -> 1,100 tokens) -> 70.3% (about 15,980); MATH500 83.2 -> 78.3, entropy 0.12 -> 3.0; parallel voting about 22% above Wait-and-think-more at 16K | Mirage paper 2025 (c15) | [E] K13 |
| s1 budget forcing | 1,000 items; AIME24 50.0 -> 53.3 (2x Wait) -> 57 (up to 4x); MATH500 93.0; GPQA 57.6 -> 59.6; 2x with no string: MATH500 90.2, GPQA 55.1; plateau near 30k tokens | Muennighoff et al. 2025 (b20, c08) | [E] K13 |
| Inverse scaling | Accuracy falls as reasoning grows on counting with distractors, spurious regression, Zebra puzzles; five failure modes | Gema et al. 2025 (b21) | [E] K13 |
| Prompt-level budget | TALE: 461.25 -> 148.72 tokens (-68%), accuracy 83.75 -> 81.03; over 7 datasets tokens 32%, cost 41% of vanilla; estimate in range only 60.61%; too small a budget backfires (budget 10 gave 157 tokens vs 258 vanilla); open-ended tasks about 40% of tokens at comparable BLEU | Han et al. 2024/25 (c12, d06) | [E] K14 |
| Prompt budget fails on hard items | Models write longer than vanilla on AIME24 | Yang et al. (d11) | [E] K14 |
| Length-controlled RL | L1 1.5B: smooth accuracy vs budget; +20-25 points absolute over S1 at 512/1024 tokens; length error about 3% on math, 20-40% out of domain; L1-Max uses up to 2x fewer tokens than L1-Exact | Aggarwal and Welleck 2025 (b17, b18, c11) | [S] K14 |
| Trained difficulty gate | AdaptThink 1.5B: length -53.0%, accuracy +2.4; 7B -40.1%, +2.3; NoThinking picked on 86.9% GSM8K, 76.8% MATH500, 40.4% AIME24 | Zhang et al. 2025 (b22, c13) | [S] |
| Trained length reward | O1-Pruner: Marco-o1-7B 73.4 -> 76.8, 932 -> 554 tok (-40.5%); QwQ-32B 88.2 -> 89.3, -34.7% | Chen et al. 2025 (c24) | [S] |
| Frontier LLMs fail to split a shared budget | R3-Bench: oracle >= actual in 72 of 72 cells, strictly higher in 71; equal allocation beats actual play for 3 of 6 models; 50 contests per domain. Fan et al.: 7 models; effort vs position -0.34 overall (-0.17 / -0.38 / -0.48 at N=5/10/20); vs point value 0.00 / +0.04 / +0.11; vs difficulty +0.33 / +0.26 / +0.11; coverage 80% -> 40% (N=5 -> 20); unsolvable questions took 24% of the work set and 32% of tokens; shared budget beat equal split by 2.6 points at N=5 and lost by 5.0 at N=20 | Wang et al. 2026 (a28); Fan et al. 2026 (d01) | [E] K15 |
| Trained solve-or-skip fixes it | ROI-Reasoning 1.5B: Hard-512 score 0.93 (regret 0.14) vs base 0.15 (regret 0.73), TALE-EP 0.18; GPT-4o-mini 0.32; DeepSeek-V3.2 0.49 | Zhao et al. 2026 (d02) | [S] K15 |
| Humans disengage, reasoning models persist | Human successful attempts longer than failed; LRM failed attempts longer than successful; H-ARC human slope +0.24 -> +0.125 after controlling for actions; wrong trials: fastest quartile median 16 edits vs slowest 79; each LRM at least 298 observations | Wang 2026 (a29) | [S] K15 |
| LLMs shift strategy with problem size without a cost term | R1/V3/Qwen3-80B switch from pairwise to elimination as N grows; pseudo-R2 0.160 (logN, T) vs 0.019 (T alone); AIC 2727 vs 3179; labels checked on 100 examples | Hu et al. 2026 (a27) | [S] |
| Overthinking in agents | SWE-bench Verified, 19 models, about 3,908 trajectories; o1 low effort had 35% higher overthinking than high; Lowest-Overthinking@2 from low effort 27.3% at about $800 vs 29.1% at about $1,400 (43% cheaper); @3 30.3% vs 29.1%, $200 cheaper | Cuadron et al. 2025 (d03) | [S] K20 |
| Budget display for agents | Gemini-2.5-Pro BrowseComp: ReAct 100 calls 12.6% vs Budget Tracker 10 calls 12.8% (40.4% fewer search calls, 31.3% lower cost); SWE budget 50: 55.4% vs 36.8% at similar calls (45.7 vs 46.0); BATS at 100 uses 24.6% BrowseComp | Liu et al. 2026 (d12) | [S] K23 |
| Offline precomputation | Same accuracy with about 5x less test-time compute on Stateful GSM-Symbolic / AIME; scaling sleep-time up to +13% / +18%; at 10 queries per context cost per query down up to 2.5x; shrinks with few or unpredictable queries | Lin et al. 2025 (c19, d08) | [S] K18, K24 |
| One-token self-check gate | Fine-tuned Llama 3.1 8B: AlpacaEval best-of-16 win rate 21% -> 34%; GSM8K 84.2 -> 91%; adaptive sampling got 74% of the 16-sample gain with 1.2 samples; pruning 75% of 16 samples after 128 tokens: 7,259 -> 3,220 tokens | Manvi et al. 2024 (d09) | [S] |
| LLMs assume people are more rational than they are | Spearman with expected value 0.94 (GPT-4o CoT) vs 0.48 for humans; 9,831 problems analysed (13,006 in choices13k); best LLM-to-human r about 0.60 | Liu et al. 2024 (b25, c22) | [E] K16 |
| Plain LLMs miss human bandit behaviour | Regret humans 1.24, CENTaUR 1.35, LLaMA 1.85; horizon task 2.33 / 2.38 / 7.21 | Binz and Schulz 2023 (b26) | [E] K16 |
| Bandit explore-exploit as meta-reasoning | Value of planning falls as computation cost rises; model reproduces human adaptation (simulation only) | Godara and Aleman (a24) | [S] |

## 4. Mechanisms and models

Written so an engineer can implement the idea. Pick one currency (tokens or dollars) for all costs.

### 4.1 Value of computation (VOC)

For an agent in belief state b, a computation c, and a cost cost(c):

- VOC(c, b) = E[value of the best action after doing c] minus E[value of the best action now] minus cost(c).
- Do c if VOC > 0. Stop when the best VOC <= 0.
- Exact VOC needs a model of how a computation changes beliefs. In practice use an approximation (4.2).

### 4.2 BMPS: learned approximation (Callaway et al. 2018; a22, c05)

- Features: myopic value of information (the gain from one more computation), value of perfect information (the gain if all unknowns were resolved), the margin of the best action over the next best, and the cost.
- Approximate VOC as a weighted mix of these features minus cost. 2-3 weights are tuned by Bayesian optimisation to maximise return in simulation.
- Policy: take the computation with the highest approximate VOC; if none is positive, act.
- Result: 98-99% of optimal in small worlds. Overhead about 1-3 ms, far below the object-level simulations.
- Caveat: tested only on tiny simulated tasks by the original authors (K06).

### 4.3 Strategy selection by learned cost-benefit (a13, a15)

- Keep, for each strategy s, a model of expected score given problem features f, and a model of expected cost (time or tokens).
- Choose s* = argmax_s [ score_hat(s, f) - lambda * cost_hat(s, f) ], where lambda is the price per unit of cost.
- Update the models after each trial (online Bayesian linear regression, or running means per feature bucket). This is a contextual bandit; Oh and Gobet (c27) describe Thompson sampling over strategy weights, with no data.
- For our agent: S0 holds a table keyed by problem class (is there a check, exact or open answer, size) with per-mode pass rate and mean tokens. S9 updates it. Choose the mode by pass rate minus lambda times tokens.

### 4.4 Sequential adjustment with an optimal stop (anchoring model; a17)

- Start from an anchor x0. Repeat: propose a small step; accept it if it looks better; stop after n steps.
- Optimal n minimises error_cost * E[error after n steps] + time_cost * n.
- Bias shrinks as error cost rises and as time cost falls. Two fitted parameters per dataset (step size, relative time cost).
- For our agent: revise an answer in small checked steps and stop when the expected gain of another revision is below its token price. The S5 rule "at most 2 rounds" is a crude version.

### 4.5 Optimal number of samples (Vul et al.; a19)

- Reward rate = (value of an answer from k samples) / (k * t_sample + t_act).
- With symmetric utility and t_act / t_sample under 10, k = 1 is optimal. As stakes rise, k rises.
- For our agent: self-consistency k should scale with stakes and with the ratio of answer-use cost to sample cost. LLM samples are correlated (G4), so the human result is a direction only.

### 4.6 Learned value of control (LVOC; a20)

- Predict the value of each control setting (type, intensity) from stimulus features with reinforcement learning. Subtract an effort cost. Choose the control with the highest net value.
- For our agent: choose reasoning effort (low, medium, high) per item from item features, learning from outcomes.

### 4.7 Reward for LLM training (RaM; a25, c01)

- R(x, y, z) = U(z | x, y) - lambda * len(z).
- U = log pi(y | z, x) - log pi(y | x): how much the chain of thought z raises the log-probability of the target answer y.
- lambda = 0.1 per token. Expert iteration: sample K = 4 chains at temperature 0.5, keep the highest-reward chain, fine-tune, repeat 5 iterations. 1,024 training items each from ARC, CommonsenseQA, GSM8K, ProofWriter; Llama-3.2-3B and Llama-3.1-8B.
- Needs weights; not usable by a scaffold. The idea that transfers: judge a thought by how much it raises the probability of an answer you can later verify, minus its length.

### 4.8 Stopping rules over samples and steps

- Beta rule (Adaptive-Consistency; d10): keep counts of answers; stop when the posterior probability that the leading answer is the true majority exceeds 0.95. Cost 0.03 ms. Needs several parallel samples; cannot stop one long chain.
- Window rule (ESC; c18): sample in small windows; stop when one window is unanimous.
- Trial-answer rule (DEER; d11): at each thought switch, force a short answer; exit if its token confidence exceeds 0.9-0.97. Too low a threshold hurts accuracy; too high exits late. The probe adds tokens, so token saving (19-43%) exceeds latency saving (27.9-40.1%).
- Probe rule (d05): a trained head on hidden states predicts whether the current intermediate answer is correct; exit above 0.85. Does not transfer across domains.
- Confidence-trace rule (DeepConf; d04): keep per-trace lowest-group confidence; drop weak traces; needs a 16-trace warm-up that counts in cost.
- Shortest-chain rule (Hassid; c16): among k parallel chains take the shortest (short-1@k) or vote among the shortest 3.
- No source compares these at equal tokens (K22).

### 4.9 Shared-budget allocator (what frontier LLMs lack)

- For each item i estimate p_i(c), the chance of a correct answer at cost c (from a cheap first pass, class pass rates, or the length of a first attempt), and the value v_i.
- Greedy: rank by v_i * (marginal gain in p_i per token); allocate until the budget is gone; skip items whose best marginal value per token is below the threshold; cap per item.
- R3-Bench (a28) and Fan et al. (d01) show that prompting a model to plan this does not work. ROI-Reasoning trains it (d02). We propose to do it in code (test B4).

### 4.10 Budget display

- Show the remaining budget at every step (Budget Tracker; d12). Agents then use a small budget as well as a large one. A bare cap (TALE style) works only inside a band and can backfire if too low (token elasticity).

### 4.11 Offline compute (sleep-time; c19, d08)

- Before queries arrive, precompute inferences over a shared context. In the cost model, test-time tokens are weighted 10x sleep-time tokens. Pays when many predictable queries share one context.

## 5. What holds up

### 5.1 Replications and independent confirmation

- **No independent replication or failed replication of the Lieder/Griffiths strategy-selection or anchoring cost results was found (2019-2026).** Treat K02, K04, K25 as single-lab. This is a gap, not evidence of success (critique.md, gap 2).
- Nearest relative: Xie and Moss 2025 (d14), N = 144, a direct replication of a different strategy-selection theory (RCCL, Building Sticks Task). All four prior findings replicated, including a preference for strategies with higher base rates of success. This supports experience-driven strategy choice in general. It does not test cost-sensitivity.
- Callaway planning (d07): preregistered, four experiments, but same lab as the model, deterministic environments only, no formal power analysis (aim 100 per condition), cost parameters fit per participant. The quoted "86% of best trade-off, 55% agreement" (a05, b02) is not in the primary paper. Use the real numbers.
- BMPS and LVOC are simulation-plus-model-fit results from the originating lab.

### 5.2 Where the theory is weak

- Free parameters (anchoring: 8 vs 29 adjustments) support critics who call it hard to falsify (K04, K17).
- Costs are mostly fitted. Lieder et al. 2018 (d13) manipulated time and error cost experimentally, which is the right test. N not read; no replication.
- Low pseudo-R2 in LLM strategy switching (0.16, a27), and the authors offer a rival reading (attention limits, not allocation).

### 5.3 LLM results that are solid

- Overthinking on easy items [E]: Chen (b15, c09), Cuadron (d03), DEER (c14), AdaptThink (c13), survey (c21).
- Early exit and confidence stopping [E]: four independent groups (DEER, probe, DeepConf, Hassid).
- Sequential stopping of self-consistency [E]: Adaptive-Consistency, ESC, and the stopping-rule comparison.
- Difficulty-aware allocation beats uniform best-of-N [E]: Snell et al.; consistent with AdaptThink and RaM.
- Non-monotonic thinking [E]: Mirage paper, s1, inverse scaling.
- Failure to split a shared budget [E]: R3-Bench, Fan et al., and Wang's human-vs-model comparison (a29), in different designs.

### 5.4 Interventions that worked

- Stopping at the first confident answer: 19-43% fewer tokens (DEER), 24% (probe), 3.3x fewer samples (Adaptive-Consistency).
- Picking the shortest chain (up to 34.5% more accurate than longest).
- Budget display for agents (+18.6 points on SWE at budget 50; BrowseComp 12.8% at 10 calls vs 12.6% at 100).
- Training with a length-aware reward (RaM, L1, O1-Pruner, AdaptThink): 23-63% fewer tokens at equal or better accuracy. These need weights.
- Choosing the lower-overthinking of 2 cheap runs in SWE agents (27.3% at about $800 vs 29.1% at about $1,400).

### 5.5 Interventions that did not work, or came with costs

- A planning prompt does not make models value-aware (open-model order-position correlation 0.64 -> 0.60; d01). Plan-and-Solve lowered the base score in ROI-Reasoning (Medium-512 0.15 vs 0.33).
- Prompt-level token budgets fail on hard items (AIME24) and can backfire when too small (TALE; DEER).
- Low reasoning effort in agents raised overthinking by 35% (d03). "Think less" is not a rule for agent loops.
- TALE accuracy fell 83.75 -> 81.03: a small cost, not zero.
- RaM out of distribution: 8B accuracy 36.4 vs 40.2 on MMLU-CF.
- RaM against instruction-tuned CoT: 3B instruct CoT scored 53.2, above RaM 50.1 (c02). RaM's accuracy edge holds against STaR and few-shot CoT only.
- DeepConf offline filter hurt in 8 of 20 settings (d04); confidently wrong traces are a named limitation.
- Hidden-state probes do not transfer across domains (d05).
- Self-training: AIME24 lost 3.4 points (c09).
- A shared budget lost to an equal split by 5.0 points at N=20 (d01): allocating badly is worse than not allocating.

### 5.6 Moderators

- Difficulty: gains concentrate in easy and medium items (Snell; AdaptThink picked NoThinking 86.9% on GSM8K vs 40.4% on AIME24).
- Stakes: more samples pay as stakes rise (Vul, r = .61).
- Task type: explicit CoT helps mostly on maths and logic (Sprague et al. 2024 meta-analysis of over 100 papers, secondhand only, a30).
- Model ability: the best chain length grows with difficulty and shrinks with capability (d16, abstract only).
- Predictability of queries: sleep-time pays with predictable, related queries (d08).
- Number of options: reasoning models move from pairwise to elimination strategies as N grows (a27).

## 6. Language models

### 6.1 Do LLMs reason resource-rationally?

- Partly, for difficulty registration. Trace length follows human problem duration in H-ARC, INTUIT and Cortes for six open reasoning models and DeepSeek-V3 (a29).
- Allocation after difficulty is registered is not rational. Failed LRM attempts are longer than successful ones, the reverse of humans (a29). Hedging and repetition are higher in failed traces.
- Strategy shifts with problem size occur without a cost term (a27): pairwise at N<4, elimination as N grows. Pseudo-R2 only 0.16, with a rival explanation.
- Across problems, no. Effort follows presentation order (rho -0.34 to -0.48) and ignores point value (0.00 to +0.11) (d01). R3-Bench: the oracle beat actual play in 71 of 72 cells (a28). Frontier size does not predict allocation skill (d02).
- Models over-assume human rationality: Spearman 0.94 vs 0.48 for people on choices13k (b25). Plain LLaMA misses human bandit regret (7.21 vs 2.33) unless fine-tuned (b26). Do not use an LLM as a stand-in for a resource-rational human.

### 6.2 How much do they overthink?

- "2+3": 1,953% more tokens than conventional models, 13 solutions (b15). First solution correct in over 92% of cases. Most responses have 2-4 solution rounds (76-80% QwQ, 59-63% R1). Later solutions repeat earlier ones; distinctness of solution 4+ is 11.5% lower than solution 3 (c10).
- Reasoning models score nearly 3x higher on overthinking in SWE agents (d03).
- "Which is bigger, 0.9 or 0.11": 19 s on QwQ-32B and 42 s on R1 (c21).

### 6.3 What changed behaviour, and by how much

| Change | Effect | Needs weights? |
|---|---|---|
| Value-of-computation reward (RaM) | -23% / -32% tokens, +2.7 / +1.6 points vs STaR | Yes |
| Length-harmonising RL (O1-Pruner) | -34.7% to -40.5% tokens, +1.1 to +3.4 points | Yes |
| Self-training on first-correct + reflection | -35% to -46% tokens, -3.4 to +1.2 points | Yes |
| Learned think/no-think (AdaptThink) | -53% / -40% length, +2.4 / +2.3 | Yes |
| Length-controlled RL (L1) | +20-25 points over S1 at 512/1024 tokens | Yes |
| Solve-or-skip allocator (ROI-Reasoning) | Hard-512 score 0.15 -> 0.93 | Yes |
| Early exit with trial answer (DEER) | -19% to -43% tokens, +0.3 to +5.0 points | No (needs token probabilities) |
| Hidden-state probe | -24% tokens, same accuracy | Probe training, hidden states |
| Beta stopping rule | 3.3x fewer samples, -0.07 point | No |
| Shortest-chain pick | up to +34.5% vs longest; up to -40% thinking tokens vs majority | No |
| Difficulty-based allocation (Snell) | about 4x less compute | No (needs a difficulty estimate) |
| Zero-shot token-budget prompt (TALE) | -68% tokens, -2.7 points | No |
| Budget display (Budget Tracker) | +18.6 points on SWE at similar calls; -31.3% cost on BrowseComp | No |
| Sleep-time compute | about 5x less test-time compute; up to 2.5x cost per query | No |
| Planning prompt for a shared budget | no change in value-awareness | No |

### 6.4 Extra thinking can hurt

- GSM8K R1-Distill-1.5B: 82.2 -> 87.3 -> 70.3% as thinking goes from 385 to about 16,000 tokens (c15). MATH500 83.2 -> 78.3 (entropy 0.12 -> 3.0).
- Inverse scaling on counting with distractors, spurious regression, and Zebra puzzles (b21).
- Early gains are tied to output entropy rather than better reasoning (c15).
- Parallel short chains plus a vote beat one long chain by about 20-22% at 16K (c15).

### 6.5 Caveats about the LLM evidence

- Mostly maths, science multiple choice and code. Open-ended and agentic evidence is thin: R3-Bench, Budget Tracker, Cuadron (SWE only), AlpacaEval with a trained gate, TALE on code summary and empathetic reply.
- Many claims come from one paper or from the Griffiths group (K02, K06, K07, K08).
- Training-based methods cannot be used by a scaffold. Only prompt-level and stopping-rule results transfer.
- Old models in some key stopping results (Adaptive-Consistency: GPT-3.5, Vicuna-13B, 2023).
- Test-time scaling papers do not test resource-rationality; they are a proxy.
- Cuadron trajectory counts differ between abstract (4,018) and body (about 3,908).

## 7. What our agent should take

Schema parts: G = guardrail, S = state, O = operator, memory = the class table updated in S9.

### Add now (established)

| # | Item | Schema part | Status | Evidence ids |
|---|---|---|---|---|
| A1 | Treat thinking as having a price. Principle only: spend thinking where the expected gain beats its cost. The rule is a design target, not a runtime solver. | S0, G7 | [E] K01 | a01, a03, a10, a12, b01 |
| A2 | Stop at the first confident answer in each mode instead of using a fixed budget. | S4, S7, S9 | [E] K10 | c14, d11, b24, d05, c16, d04 |
| A3 | When several parallel samples exist, use a vote-count stopping rule (Beta or window) instead of fixed k. Count its tokens; its own compute is negligible. | S3, G4 | [E] K11, K21 | c17, d10, c18 |
| A4 | When answers disagree and no check exists, prefer the shortest of the k chains; do not prefer the longest. | S7 | [E] K10 | c16 |
| A5 | Allocate budget by difficulty, not uniformly. Gains concentrate in easy and medium items. | S0, G12 | [E] K12 | b19, c07, c13 |
| A6 | Cap reasoning length per mode; do not assume more thinking helps; prefer parallel short attempts to one long chain. | S3, G11 | [E] K13 | c15, b21, c08, b20 |
| A7 | Log the stage at which the first correct answer appears, to measure overthinking in our own runs. | S9, memory | [E] K09 | b15, c09, d03 |
| A8 | Do not rely on prompting alone to split a shared budget across problems. | S0, G12 | [E] K15 | a28, d01, d02, a29 |
| A9 | If a budget is shown in the prompt, treat it as a band: too small backfires and hard items ignore it. Sweep it before relying on it. | S0 | [E] K14 | c12, d06, d11, b17, b18 |
| A10 | Do not use an LLM as a model of how a rational human would allocate effort. | none | [E] K16 | b25, c22, b26, c23 |
| A11 | Pre-register price and threshold values before testing any gate; never fit them after the fact. | G7 | [E] K17 | a08, b07, a17, a18 |
| A12 | Count the gate's own tokens (probes, trial answers, warm-up, estimator queries) inside the budget. | S0, G7 | [E] K21 | d10, d11, d04, d06 |

### Test first

| # | Item | Schema part | Status | Evidence ids | Why not yet |
|---|---|---|---|---|---|
| T1 | A cheap difficulty predictor (class pass rate, agreement of 2 short samples, first-pass confidence) as the S0 gate on mixed non-math tasks | S0 | [S] K19 | d05, d09, d11, d04, d06 | Published gates are trained and domain-bound; none tested zero-shot on mixed tasks at equal tokens with gate cost counted |
| T2 | Three stopping rules (Beta, DEER-style trial answer, VOC threshold) at one fixed budget | S3, S4 | [S] K22 | d10, d11, d04 | No source compares them |
| T3 | Scaffold-side shared-budget allocator vs prompt-only planner | S0, G12 | [S] K15 | a28, d01, d02 | Only trained fixes tested |
| T4 | Show remaining budget at each step in agent loops | S0, S6 | [S] K23 | d12 | Single paper, Gemini, small bases |
| T5 | Cap private reasoning and prefer an action that returns feedback in agent steps | S0, S1 | [S] K20 | d03, d12 | SWE only; low effort raised overthinking |
| T6 | Choose the lower-overthinking of 2 cheap runs | S7 | [S] K20 | d03 | The score is judged after the run by another LLM, not an online gate |
| T7 | Scale self-consistency k with stakes and answer-use cost (Vul rule) | S3, G4 | [S] human-only (K03) | a04, a19, b03, d15 | Human result; LLM samples are correlated |
| T8 | Cache problem restatement or decomposition when 3+ later steps reuse it | memory | [S] K18, K24 | c19, d08 | One paper, synthetic benchmarks |
| T9 | Learned strategy selector over a menu of procedures with token costs | S0, S6 | [S] K02 | a13, a14, a15 | Human selector evidence is single-lab; LLM selector untested |
| T10 | Progress-based reward: score each thinking episode by the rise in estimated chance of success | S6 | [S] | c25 | Training-based (MRT: pass@1 54.5 -> 55.9) |
| T11 | Net-saving check: count VOC estimation tokens against the saving | S0 | [S] K06 | c06, d10, d11 | BMPS pays only when object-level cost is much larger than metalevel cost |

## 8. Concrete tests on our bench

All arms get the same total token budget per item, counting gate, probe and setup tokens (G7). Pre-register lambda, thresholds and item sets before running. Use at least 3 seeds. Report paired differences with a bootstrap CI.

| # | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| B1 | Mixed set: ARC-style, BRAINTEASER, short exact-answer maths, one open-ended set; at least 60 items per type | (a) always short reasoning; (b) always step-by-step; (c) S0 gate by cheap difficulty predictor (class pass rate + agreement of 2 short samples) choosing the mode; all at the same mean tokens per item | Accuracy at equal mean tokens; tokens on easy vs hard items; gate token share | Gate beats both fixed arms by 2+ points; hard/easy token ratio above 1.5 (RaM got about 2.0); fails if gate tokens exceed 15% of the budget |
| B2 | Same items, 5 samples each | (a) fixed k = 5 vote; (b) Beta stop (0.95); (c) window stop; (d) trial-answer early exit; (e) VOC threshold; all capped at the same mean tokens | Accuracy per token; accuracy at matched mean tokens | Beta/window within 0.5 point of fixed k at 40%+ fewer tokens; rank the five |
| B3 | Verified-answer items (code, ARC with a check) | (a) run full budget; (b) stop at the first answer that passes the check | Tokens saved; accuracy | Same accuracy, 30%+ fewer tokens on easy items; the A7 stage log gives the baseline |
| B4 | Sets of 5, 10 and 20 items sharing one budget, with point values | (a) prompt-only plan then solve; (b) sequential solve in presented order; (c) equal split; (d) code allocator (value per estimated cost, per-item cap, explicit skip); (e) oracle from single-item response curves | Score as % of oracle; effort vs position and vs value correlation | (d) closes at least half the gap between (b) and (e); effort-value correlation above +0.3 for (d), about 0 for (a) |
| B5 | Easy, medium and hard bins of one benchmark | (a) uniform best-of-N; (b) compute split by difficulty from a cheap first pass | Accuracy at equal tokens, by bin | Gain on easy and medium bins (Snell: about 4x); no gain on the hardest bin |
| B6 | Mix of exact and open items with a prompt-level budget | (a) no budget text; (b) fixed budget; (c) self-estimated budget (TALE-style, estimator tokens counted); (d) remaining-budget display; sweep 5 budget sizes | Tokens used vs budget; accuracy; the budget size where tokens rise (elasticity point) | (d) at least equal to (a) with fewer tokens; (c) loses 1-3 points; elasticity visible at small budgets |
| B7 | Multi-step agent tasks (20+, SWE-like or tool-use) | (a) default; (b) private reasoning capped, act-then-observe; (c) budget display; (d) pick the lower-overthinking of 2 short runs | Resolve rate; tool calls; total tokens | (b) not worse than (a) at lower tokens, else drop it; (c) improves resolve rate at the same calls |
| B8 | Items with stakes: high-penalty vs low-penalty wrong answers (stated in the prompt and enforced in scoring) | (a) k = 1 always; (b) k = 5 always; (c) k scaled with stakes | Score net of penalty at equal mean tokens | (c) beats both when stakes vary; gains may be small because samples are correlated (G4) |
| B9 | Long contexts with 5-10 related queries each | (a) solve each query fresh; (b) precompute a summary or decomposition once, then reuse | Tokens per query; accuracy | Savings grow with queries per context; none at 1-2 queries |
| B10 | The B1 set with the gate on and off | Net saving after counting estimation tokens | Net tokens saved per item | Positive only when object-level cost is at least 5x gate cost |
| B11 | Extra-thinking sweep per mode | Chain length bins (short, 2x, 4x, 8x) on each item class | Accuracy vs length curve per class | Inverted U on easy items; find the per-class optimum (d16 predicts it shifts with difficulty) |

## 9. What does not transfer, and why

- **The rule itself.** Eq. 3 is solved by evolution and learning, not online (a01). An exact per-problem VOC is not computable. Only approximations transfer.
- **Human cost parameters.** Human time and error costs are unlike token costs. LLMs have no fatigue and no working-memory span of 7. The constraints that make human heuristics bounded-optimal (limited working memory, serial processing) do not hold for a transformer.
- **Human fits as evidence for LLM gates.** The sorting, loan and anchoring studies show how people trade effort for accuracy. They do not show how an LLM scaffold should.
- **One sample is best (Vul).** Rests on a fixed time cost per sample and independent samples. LLM samples from one model are correlated (G4). Parallel samples are not slower in wall time.
- **Training-based methods.** RaM, L1, AdaptThink, O1-Pruner, Thinkless, ROI-Reasoning, MRT, the hidden-state probe and the one-token gate in d09 all need weights or a trained head. The scaffold has none. Take the idea, not the method.
- **Math-only results.** Most early-exit and budget numbers are on GSM8K, MATH, AIME, GPQA. Not shown for ARC-style or open-ended tasks; agentic evidence points the other way (low effort raised overthinking).
- **Savings against a 512-vote baseline** (DeepConf) are not savings against a modest scaffold.
- **Human planning, gaze and decomposition models.** Mouselab planning, fixation patterns, graph-navigation decomposition and explore-exploit are not operational for the schema. Nothing to add.
- **Anchoring.** Contested and fitted post hoc (K04). The agent has no anchoring bias to tune. Use only as a caution.
- **Metareasoning that costs more than it saves.** BMPS pays only when object-level computation is much costlier than the metalevel. For short tasks the gate can cost more than it saves.
- **Monitor-Generate-Verify** (Oh and Gobet): a proposal with no data (c04, c27).
- **Hu et al. strategy switching.** Does not show a cost term in models; the authors' rival reading stands.

## 10. Open questions

1. Does a cheap, zero-shot difficulty predictor gate S0 well enough at equal tokens on mixed non-math tasks, with its own tokens counted? (K19)
2. Have the Lieder/Griffiths cost-sensitivity and anchoring results been independently replicated outside the lab? None found for 2019-2026. Full texts of Lieder 2018 and Vul 2014 were not read for N.
3. How much of the early-exit and shortest-chain gain survives on agentic and open-ended tasks?
4. Which stopping rule is best at equal tokens: Adaptive-Consistency, DEER-style trial answer, or VOC threshold? (K22)
5. Can a prompt-only budget avoid token elasticity, and where is the elasticity point for our model?
6. Do newer budget-aware models still fail to split a shared budget? Can a code allocator close the 71/72 oracle gap?
7. Can cost parameters be measured independently so a gate can be pre-registered without post hoc fitting? (d13 manipulated them; no replication)
8. Does sleep-time precomputation pay back when queries vary widely?
9. Does VOC estimation ever cost more than it saves for LLM agents? No direct measure after estimator cost.
10. What is the source of the "86% / 55%" planning figures? The primary paper does not contain them.
11. Are chain-length optima stable per model class (d16, abstract only)?
12. Is the R3-Bench oracle (offline, empirical, from the model's own curves) a realistic upper bound for a live policy?

## 11. Sources

[V] = opened and read this session. [M] = snippet or secondhand only.

Founding and theory:
- [V] Lieder and Griffiths (2020) Resource-rational analysis, BBS 43:e1. https://cocosci.princeton.edu/papers/liederresource.pdf and https://pmc.ncbi.nlm.nih.gov/articles/PMC7702215 (the publisher DOI page https://doi.org/10.1017/S0140525X1900061X timed out in one run; the paper itself was read via the two links)
- [V] Russell and Subramanian (1995) Provably bounded-optimal agents. https://arxiv.org/abs/cs/9505103
- [M] Russell and Wefald (1991) Principles of metareasoning (via the BMPS paper). https://arxiv.org/abs/1711.06892
- [V] Lewis, Howes and Singh (2014) Computational rationality. https://web.eecs.umich.edu/~baveja/Papers/tops12086.pdf
- [V] Gershman, Horvitz and Tenenbaum (2015) Computational rationality. https://microsoft.com/en-us/research/wp-content/uploads/2016/11/273.full_.pdf

Human experiments and models:
- [V] Lieder et al. (2014) Algorithm selection by rational metareasoning. https://papers.nips.cc/paper_files/paper/2014/file/87b5e7e570f757a0b99f0a370ce2438c-Paper.pdf (not re-opened in the cross-check)
- [V] Lieder and Griffiths (2015) When to use which heuristic. https://journalpub.escholarship.org/cognitivesciencesociety/article/25608/galley/15232/download
- [M] Lieder and Griffiths (2017) Strategy selection as rational metareasoning, Psych Review. https://is.mpg.de/publications/lieder2017strategy
- [V] Lieder, Griffiths, Huys, Goodman (2018) The anchoring bias reflects rational use of cognitive resources. https://cocosci.dreamhosters.com/papers/AnchoringSimulations.pdf
- [V] Lieder et al. (2018) Empirical evidence for resource-rational anchoring (abstract page). https://europepmc.org/article/MED/28484951
- [V] Vul, Goodman, Griffiths, Tenenbaum (2014) One and done? https://cocosci.princeton.edu/tom/papers/OneAndDone.pdf and https://europepmc.org/article/MED/24467492
- [V] Lieder, Shenhav, Musslick, Griffiths (2018) Rational metareasoning and the plasticity of cognitive control. https://journals.plos.org/ploscompbiol/article/file?id=10.1371/journal.pcbi.1006043&type=printable and https://pmc.ncbi.nlm.nih.gov/articles/PMC5937797
- [V] Callaway, Rangel, Griffiths (2021) Fixation patterns in simple choice. https://journals.plos.org/ploscompbiol/article/file?id=10.1371/journal.pcbi.1008863&type=printable
- [V] Callaway, Gul, Krueger, Griffiths, Lieder (2018) Learning to select computations (BMPS). https://arxiv.org/abs/1711.06892
- [V] Callaway et al. (2022) Rational use of cognitive resources in human planning. https://osf.io/download/6001d92086541a063714ab13/
- [V] Correa et al. (2020) Resource-rational task decomposition. https://arxiv.org/abs/2007.13862
- [V] Godara and Aleman, resource-rational explore-exploit via meta-reasoning. https://arxiv.org/abs/2408.01253
- [V] Xie and Moss (2025) Task representation and individual differences affect strategy selection. https://doi.org/10.3389/fpsyg.2025.1445200
- [M] Sprague et al. (2024) To CoT or not to CoT (as cited by De Sabbata et al.). https://arxiv.org/abs/2410.05563

LLM studies:
- [V] De Sabbata, Sumers, AlKhamissi, Bosselut, Griffiths (2024) Rational metareasoning for large language models. https://arxiv.org/abs/2410.05563
- [V] Hu, Roshan, Varma (2026) Are more tokens rational? https://arxiv.org/abs/2602.10329
- [V] Wang et al. (2026) R3-Bench. https://arxiv.org/abs/2608.16033
- [V] Wang (2026) Humans disengage, reasoning models persist. https://arxiv.org/abs/2606.26502
- [V] Fan et al. (2026) Thinking Hard, Not Smart. https://arxiv.org/abs/2608.07968
- [V] Zhao et al. (2026) ROI-Reasoning. https://arxiv.org/abs/2601.03822
- [V] Chen et al. (2024) Do NOT think that much for 2+3=? https://arxiv.org/abs/2412.21187
- [V] Cuadron et al. (2025) The Danger of Overthinking. https://arxiv.org/abs/2502.08235
- [V] Aggarwal and Welleck (2025) L1. https://arxiv.org/abs/2503.04697
- [V] Snell, Lee, Xu, Kumar (2024) Scaling LLM test-time compute optimally. https://arxiv.org/abs/2408.03314
- [V] Muennighoff et al. (2025) s1. https://arxiv.org/abs/2501.19393
- [V] Gema et al. (2025) Inverse scaling in test-time compute. https://arxiv.org/abs/2507.14417
- [V] Zhang et al. (2025) AdaptThink. https://arxiv.org/abs/2505.13417
- [V] Fang, Ma, Wang (2025) Thinkless. https://arxiv.org/abs/2505.13379 (abstract level)
- [V] Zhang et al. (2025) Reasoning models know when they're right. https://arxiv.org/abs/2504.05419
- [V] Yang et al. (2025) DEER. https://arxiv.org/abs/2504.15895
- [V] Mirage of test-time scaling (2025). https://arxiv.org/abs/2506.04210
- [V] Hassid et al. (2025) Don't overthink it. https://arxiv.org/abs/2505.17813
- [V] Aggarwal, Madaan, Yang, Mausam (2023) Adaptive-Consistency. https://arxiv.org/abs/2305.11860
- [V] Li et al. (2024) Early-stopping self-consistency. https://arxiv.org/abs/2401.10480
- [V] Lin et al. (2025) Sleep-time compute. https://arxiv.org/abs/2504.13171
- [V] Chain of Draft (2025). https://arxiv.org/abs/2502.18600 (abstract only)
- [V] Stop overthinking: survey of efficient reasoning (2025). https://arxiv.org/abs/2503.16419
- [V] Han et al. (2024/25) Token-budget-aware LLM reasoning (TALE). https://arxiv.org/abs/2412.18547
- [V] Liu, Zhang, Griffiths et al. (2024/25) LLMs assume people are more rational than we really are. https://arxiv.org/abs/2406.17055
- [V] Binz and Schulz (2023) Turning LLMs into cognitive models. https://arxiv.org/abs/2306.03917
- [V] Binz and Schulz (2022) Using cognitive psychology to understand GPT-3. https://arxiv.org/abs/2206.14576
- [V] Chen et al. (2025) O1-Pruner. https://arxiv.org/abs/2501.12570
- [V] Wang et al. (2025) MRT: meta reinforcement fine-tuning. https://arxiv.org/abs/2503.07572
- [V] Oh and Gobet (2025) Monitor-Generate-Verify. https://arxiv.org/abs/2511.04341
- [V] Fu, Wang, Tian, Zhao (2025) Deep Think with Confidence. https://arxiv.org/abs/2508.15260
- [V] Manvi, Singh, Ermon (2024) Adaptive inference-time compute. https://arxiv.org/abs/2410.02725
- [V] Liu et al. (2026) Budget-aware tool use (Budget Tracker, BATS). https://arxiv.org/abs/2511.17006
- [V] Wu et al. (2025) When more is less: CoT length. https://arxiv.org/abs/2502.07266 (abstract and intro only)

## Source audit (2026-11-01)

Fresh auditors re-opened the sources of 12 established claims: 7 confirmed as written, 5 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **E18.09-K03** (number corrected). The 3x threshold appears only in Lieder and Griffiths' review (a04 and b03 are the same text); the primary paper (Vul et al. 2014) says one sample is optimal for action/sample time ratios below 10 under a symmetric utility, and that no sampling pays off below a ratio of 2 with no penalty for errors, so the threshold depends on the utility function. Corrected claim: The best number of mental samples per decision is very small: Vul et al. (2014) show one sample is optimal when execution takes less than about 10 times as long as sampling under a symmetric utility (Lieder and Griffiths' review reports a threshold of about 3x), and the effective number of samples rises with stakes (r(25)=.61 across probability-matching studies).
- **E18.09-K09** (now single-source: the sources are not independent). All numbers verified (1,953%, over 92%, 48.6% MATH500 and 35-46% on GSM8K/GPQA/AIME with small accuracy changes), but b15, b16, c09 and c10 are the same paper (Chen et al. 2412.21187); the survey and Cuadron et al. (agentic overthinking) do not report these figures, so the claim rests on one paper.
- **E18.09-K12** (now single-source: the sources are not independent). Both snell entries (b19, c07) are the same paper (Snell et al. 2408.03314) and the sleep-time paper does not support the claim; figures match the abstract (more than 4x efficiency vs best-of-N, outperforms a 14x larger model in a FLOPs-matched test where the small model has non-trivial success).
- **E18.09-K17** (reworded: the sources support less). Critic points are supported (commentators warn of added degrees of freedom in specifying resource costs; Lieder and Griffiths concede falsification is hard when constraints are uncertain and RRA is hard to apply when environment or constraints are unknown), but 'no count of independent replications exists' is an absence claim that none of the sources establish; the Vul et al. entry is unrelated. Corrected claim: Critics in the BBS commentaries note that resource-rational models add degrees of freedom (resource costs), and Lieder and Griffiths acknowledge that falsification is hard in practice and the approach is hard to apply where constraints or the environment are unknown; no count of independent replications was found in the sources read.
- **E18.09-K21** (reworded: the sources support less). Beta 0.03 ms is real (but Entropy rule is also 0.03 ms; Dirichlet/CRP ~95-101 ms). DEER latency cut 27.9-40.1% was measured on MATH-500/AMC, while the 19.1-42.9% token cut spans all benchmarks; the ranges overlap, and the paper says latency speedup vs length savings is superlinear, so 'latency only' is not supported. Corrected claim: Stopping-rule cost differs: the Beta rule in Adaptive-Consistency takes about 0.03 ms per decision (as does the entropy rule; the Dirichlet and CRP rules take about 95-101 ms), while DEER's trial-answer probing adds overhead that its branch-parallel variant reduces (latency cut 27.9-40.1% for original DEER vs 36.3-58.6% for branch-parallel, on MATH-500 and AMC), so probe overhead should be counted.
