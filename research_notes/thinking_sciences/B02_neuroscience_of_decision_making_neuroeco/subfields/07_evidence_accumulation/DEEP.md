# Evidence accumulation: deep document

*Subfield B02.07. Written 2026-11-01 from evidence_a-d.jsonl (a01-a25, b01-b26, c01-c27, d01-d20), claims.jsonl (K01-K27) and critique.md in this folder. Evidence ids below are the line ids in those files. Status marks follow SCHEMA.md: [E] established (two or more independent sources), [S] single source, [C] contested. Claims count independent sources, not lines: many lines are the same paper read by different agents.*

---

## 1. What it is

Evidence accumulation is the idea that a decision maker adds up noisy evidence over time and commits when the total reaches a bound. Three things set the outcome:

- **Drift**: how fast useful evidence arrives. Set by the stimulus or the problem. Harder item, lower drift.
- **Bound**: how much evidence is needed before committing. Set by the decision maker. Higher bound, slower and more accurate.
- **Noise and start point**: random fluctuation, and any head start for one option (a prior).

The result is a speed-accuracy trade-off with a clear shape. Raising the bound makes answers slower and a little more accurate, with sharply diminishing returns.

For our agent the mapping is direct. One "sample" is one independent attempt. The "evidence" is the pattern of agreement among attempts (or the number of checks passed). The "bound" is the stopping rule for the number of attempts. Our agent cannot change drift (item difficulty). It can only choose the bound and the cap. So this subfield answers one practical question: how many attempts, and when to stop.

Short version of what the evidence says:

1. In humans the bound is the knob that instructions move. Drift is set by difficulty. (a02, b01)
2. In LLMs, stopping on agreement among samples cuts samples about 2x to 8x with accuracy within about 1 point on closed-answer benchmarks. (a17, a19, c14, d01)
3. The stop is unsafe where the right answer is rare: agreement then locks onto a wrong consensus. No source measured how often. (d03, d05, d07)
4. A verifier-based stop beats an agreement stop at equal sample count, but not shown at equal tokens. (d05)
5. Whether the bound should be fixed or should relax over time is contested in humans and untested in LLMs. (a11, a12)

Note on schema labels: claims.jsonl labels the stop rule "O3". In SCHEMA.md O1-O8 are the idea-tree operators and O3 is Decompose. The stop rule is program code that controls how many attempts S3 produces and when S4 stops asking for more. This document calls it the **attempt-count stop rule (S3/S4 loop control)**. The claim ids keep their original labels.

---

## 2. History and theories in depth

### 2.1 Sequential testing (1940s)

Wald (1945) built the sequential probability ratio test (SPRT) for statistics. After each observation, add its log-likelihood ratio (logLR) for hypothesis A over B. Stop when the running sum crosses an upper bound (accept A) or a lower bound (accept B). The bounds are set by the wanted error rates: roughly log((1-b)/a) and log(b/(1-a)). Wald and Wolfowitz (1948) proved that for known, independent, identically distributed observations, no test with the same error rates needs fewer samples on average. (a05, opened:false; background knowledge.)

Conditions that matter for LLMs: known evidence distribution, independent samples, identical samples. LLM samples from one model fail the independence test (guardrail G4).

### 2.2 Diffusion models of choice (1978 on)

Ratcliff (1978) used a continuous random walk (diffusion) to model two-choice memory decisions. It gave full response-time (RT) distributions for correct and error responses, not only means. (a04, opened:false.) Ratcliff and McKoon (2008) is the standard statement of the diffusion decision model (DDM). (a01, b01, d19, all opened.)

DDM parameters:

| Parameter | Meaning |
|---|---|
| v (drift) | mean rate of evidence; set by stimulus quality |
| a (boundary separation) | distance between the two bounds; speed-accuracy setting |
| z (start) | start point; shifts with response bias |
| Ter | non-decision time (encoding, motor response) |
| eta | across-trial SD of drift |
| sz | across-trial range of start point |
| st | across-trial range of Ter |
| s | within-trial noise; a scale constant |

Fits use RT quantiles .1/.3/.5/.7/.9 with a chi-square statistic, for correct and error responses separately. (a01.)

Why the variability parameters exist (a03): across-trial drift variability makes errors slower than correct responses. Across-trial start-point variability makes errors faster. Together they reproduce both patterns, including a reversal inside one experiment. The plain Wald-type model cannot.

Distribution shape signature (b03): a drift change stretches the slow tail (.9 quantile) about 4 times as much as the fast edge (.1). A boundary change stretches it about 2 to 1. This is how experimenters tell "harder" from "more careful".

Scope limit (a01, b01): the model is meant for fast single-stage decisions, mean RT under about 1000 to 1500 ms. The authors say diffusion analyses do not explain how people set the criterion.

### 2.3 Optimality and rivals (2001 to 2008)

- Bogacz et al. (2006): the DDM is the continuous limit of the SPRT for two choices, so a fixed-bound DDM is optimal when difficulty is constant and known within a block. Leaky competing accumulators reduce to it when inhibition balances leak. (a14, b24; opened:false, background.)
- Usher and McClelland (2001): leaky, competing accumulators; handles more than two options, gives recency effects. (a15; opened:false.)
- Brown and Heathcote (2008): linear ballistic accumulator, a race of noise-free accumulators with variability only between trials. (a16; opened:false.)

For an engineer: all three are "count toward a bound" machines. They differ in leak, competition and where noise lives. Only the DDM/SPRT form has a clean mapping to "sample until the lead is big enough".

### 2.4 The neural version (2002 to 2014)

Shadlen's lab tied the model to single neurons in monkey parietal area LIP.

- **Roitman and Shadlen (2002)** (a07, opened). Free-response random-dot motion. 2 monkeys, 54 LIP neurons, 6 coherences from 0 to 51.2 percent. Mean correct RT fell from 824 ms (0 percent) to 409 ms (51.2 percent). Ramp slope scaled from 21.5 to 88.8 spikes/s^2 with coherence. Just before the saccade, firing converged on 68.6 +/- 0.9 spikes/s with no coherence effect (p = .46). So: slope tracks drift, the final level looks like a fixed bound. At 6.4 percent coherence the slope was 53.4 spikes/s^2 on short-RT trials and 33.9 on long-RT trials. Threshold seen only for the preferred choice.
- **Kiani, Hanks and Shadlen (2008)** (a08, opened). Even when the experimenter fixed viewing time, monkeys behaved as if they stopped integrating at a bound. 2 monkeys, 51 LIP neurons, 42,647 trials, motion 80 to 1500 ms. Bounded accumulation (k = 0.46, B = 19.9) beat leaky accumulation (Bayes factor 8.35e12). Accuracy saturated beyond about 420 ms. Early motion pulses moved choices by 1.3 +/- 0.1 percent coherence; late pulses did not. Bound-crossing time correlated with RT only weakly (r = 0.16).
- **Hanks et al. (2011)** (a09, opened). Prior odds are not a fixed start shift. A bias signal that grows with elapsed time fits better (Bayes factor above 1e8 in humans, above 1e6 in monkeys). 2 humans, 4 monkeys (36,687 trials). Fitted prior weight 0.88 and 0.85 (humans), 0.80 +/- 0.01 (monkeys). Under speed pressure bias rose from 5.1 to 10.8 and from 4.1 to 8.3 percent coherence. Collapsing bounds did not rescue the static model.
- **Hanks, Kiani and Shadlen (2014)** (a10, opened). Speed pressure did not lower the firing-rate threshold. It added an evidence-independent urgency signal pushing activity to the same threshold. 2 monkeys, 70 LIP neurons, 3,307 to 4,838 trials per monkey per regime. RT was 176 +/- 4 and 159 +/- 3 ms longer in the accuracy regime. Evidence needed was 43 +/- 2 percent smaller under speed (critique correction: monkey D 58 percent, monkey E 23 percent, so the mean hides a large split). Threshold did not differ (p > .5). Model R2 0.99 and 0.97.

Gold and Shadlen (2007), the Annual Review that states the logLR reading of LIP accumulation, could not be opened (publisher 403; a06, d20). The same lab's Shadlen and Kiani (2013) (d18, opened) stands in.

### 2.5 The fixed versus collapsing bound dispute (2012 to 2016)

- **Drugowitsch et al. (2012)** (a12, opened). If reward rate is maximised and difficulty varies from trial to trial, the best bound shrinks over time, even with a constant cost per second. 2 monkeys (2,615 and 3,534 trials), 6 humans (about 562 trials each). Monkey R2 0.987, human mean R2 0.961. AIC for the cost model: -809 and 620 against 26,436 and 48,006 for a constant bound. LIP urgency was the same across coherences, as predicted. The gain shows mainly in RT distributions and error RTs, not mean accuracy. (Corrected in a 2015 erratum.)
- **Hawkins et al. (2015)** (a11, b07, b08, opened). Large reanalysis: 9 datasets, 8 studies, 3 paradigms, 4 labs, 85 humans and 8 macaques, over 116,000 decisions. Humans: 72 of 85 prefer a fixed bound, 9 collapsing, 4 inconclusive. Monkeys: 4 collapsing, 2 fixed, 2 urgency. Urgency model best for 3 of 93 subjects. Replication on 91 more human datasets: 64 very strong (P >= .99) and 12 strong (.95 to .99) for fixed, 1 collapsing, 14 no preference. Without between-trial variability, 6 of 8 monkeys prefer fixed. A delayed-feedback replication with 74 humans (1 to 2 s delay) showed no withholding strategy.
- **Ratcliff, Smith, Brown and McKoon (2016)** (b04, b05, b06, opened to about 100k of 206k characters). Fixed bounds are the default across hundreds of participants in 10 studies from 3 labs. Speed stress moves boundaries; extreme speed stress can also lower drift. People do not reliably set the reward-rate-optimal bound; only with feedback did young adults get close. Median-only fits hide misfit.
- **Voskuilen, Ratcliff and Smith (2016)** (b09): independent fixed-vs-collapsing test. Not opened; no numbers taken.

Plain summary: humans on short blocks mostly keep a fixed bound. Highly practised monkeys mostly show collapsing or urgency. Theory says collapse is optimal when difficulty is mixed and unknown. The answer depends on the variability terms in the fit, on practice and on feedback delay.

### 2.6 Model dependence of bound estimates (2025 to 2026)

- Hato et al. (2025) (b10, opened). 100,000 simulated datasets per model, 500 trials per simulated participant. Boundary recovery R2 .99 (Wiener DDM) and .98 (Levy flight) when well specified, but .77 when Levy-flight data are fit with a Wiener DDM. Heavy-tailed noise makes the standard fit overestimate boundary separation and underestimate non-decision time. Empirical refit (Evans 2017, N = 43): speed a = 1.26 (DDM) vs 0.97 (Levy); accuracy a = 1.96 vs 1.82.
- Systematic drift variability study (2026) (b11, opened). N = 132 participants, 20 sessions each, about 3,654 trials per person. WAIC: standard 114,803; exogenous 88,082; endogenous 58,828; complete 37,537. Trial-level predictors (word frequency, EEG) greatly improve fit but do not remove the random drift-variability parameter. Conflicts with Ratcliff 2016, who saw a large drop in eta.

So published bound values are model-specific. Do not copy a number such as "a = 0.152" into the agent.

### 2.7 Bounded evidence in value-of-computation terms

- Chess (2025) (b21, opened). 519 million moves from 12.49 million 2019 Lichess games, plies 15 to 75. Human thinking time rises with the expected benefit of more thought; square-root form beat linear (dAIC 3.6e8); expected benefit explained time better (dAIC 1.9e8). Slopes 1.76 to 38.7 s per unit benefit. Stockfish depth 15 was ground truth. It is not a process model.
- Opt-out (2025) (b22, opened). People given a skip option in perceptual decisions did not become more accurate. Exp 1 N = 24: 0.82 vs 0.82 (p = .482). Exp 2 N = 26: 0.83 vs 0.84 (p = .566), skip rate 0.090 vs 0.043. Exp 3 N = 36: null (p = .462). They skipped more when stakes and difficulty were higher.

---

## 3. Core findings with exact numbers

Status: E = established, S = single source, C = contested, N = not checked beyond abstract. "K" ids are in claims.jsonl.

### 3.1 Human and animal findings

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Difficulty acts on drift; speed-accuracy instructions act on the bound | Exp 1 (N = 15, 5-50% coherence): accuracy .58-.94, drift .042-.369, a = .111. Exp 2 (N = 14): a = .109 speed vs .152 accuracy; median RT shifted 120-200 ms; accuracy changed 0-6% | a02, b01 (Ratcliff and McKoon 2008); K09 | E (4 sources incl. a10, b04) |
| Extra caution buys little accuracy for a large time cost | 0-6 points of accuracy for 120-200 ms | a02, b01; K11 | E |
| Prior odds shift the start point (about one third toward likely bound) | Exp 3 (N = 17), 75:25 priors; drift-criterion shift cut chi-square by about 1% | b02 | S |
| Prior effect grows with elapsed time (not a static start shift) | BF > 1e8 (2 humans), > 1e6 (4 monkeys); prior weight .88/.85 humans, .80 monkeys | a09 | S (tiny human N) |
| Neural ramp slope tracks drift; final rate is a fixed level | 68.6 +/- 0.9 spikes/s at all coherences (p = .46); RT 824 to 409 ms | a07 | S (2 monkeys) |
| Bounded accumulation beats leaky accumulation | k = 0.46, B = 19.9; BF 8.35e12; N = 2 monkeys, 42,647 trials | a08 | S |
| Speed pressure adds urgency, not a lower threshold | RT +176/+159 ms; evidence needed 43 +/- 2% smaller (58% vs 23% by animal); threshold p > .5 | a10 | S (2 monkeys) |
| Humans on short blocks use a fixed bound | 72/85 fixed, 9 collapsing, 4 inconclusive; replication 64 very strong + 12 strong of 91 | a11, b07, b08 | E (Hawkins plus Ratcliff 2016 review) |
| Monkeys more often show collapsing/urgency bounds | 4 collapsing, 2 urgency, 2 fixed of 8; 6 of 8 fixed if no between-trial variability | b07, b08 | C |
| Optimal bound collapses under mixed difficulty | Cost model AIC -809/620 vs 26,436/48,006 (monkeys) | a12; d18 | C (rival to Hawkins) |
| People do not set the reward-rate-optimal bound | Only young adults with feedback approached it | b05 | S |
| Bound estimates depend on the noise model | R2 .99 to .77 under misspecification; WAIC 114,803 to 37,537 | b10, b11, b06; K18 | E (method caution) |
| Thinking time follows expected benefit of computation | 519M chess moves; sqrt form dAIC 3.6e8 | b21; K17 | S |
| An opt-out option did not improve accuracy | .82 vs .82 (N = 24); .83 vs .84 (N = 26); null N = 36 | b22; K16 | S |

### 3.2 LLM findings on stopping the number of samples

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Beta-posterior stop at 0.95 cuts samples 3.3x with about no loss | 17 datasets, 3 models, cap 40, T = 0.7. Maths 73.2 vs 73.1 acc, 40 vs 13.8 samples. Commonsense 66.0 vs 65.8, 15.8 samples. Symbolic 72.8 vs 72.8, 13.1. Code 35.2 vs 35.6, 312.5 to 173.6 (2.4x). GPT-3.5-turbo 76.4 vs 76.2, 10.0 samples (4.4x). Vicuna-13B 54.0 vs 54.1, 21.7 (1.9x). Up to 7.9x on Boolean expressions. Average accuracy drop 0.04-0.1 | a17, b13, c01; K01 | E (2 sources) |
| At equal average cost, adaptive beats fixed-N | At 10 samples, about +3% on GSM8K (3 seeds; sample count p about 1.5e-3, accuracy gap not significant) | b14, c03 | S |
| Simple two-count Beta rule equals Dirichlet/CRP rules | 0.03 ms vs 94.6-101.3 ms; random stop worst; majority-only mostly worse | a18, c02; K03 | E (4 sources) |
| Window rule (stop when last w answers agree) | w = 5 (8 for MATH). Sample cuts: MATH -33.8%, GSM8K -80.1%, StrategyQA -76.8%, CommonsenseQA -78.5%, Coin Flip -84.2%, Last Letters -67.4%. GPT-4 GSM8K 7.98 of 40 samples, acc 89.29 unchanged. GPT-3.5 GSM8K 14.65 samples, 85.69 to 85.67, vs plain SC at same N 84.82. GPT-4 MATH 42.4 of 64, 60.32 unchanged. Llama-2 7B MATH 62.48 of 64 | a19, b15, c05, c06, c07; K02, K13 | S (one paper) |
| Hard items and weak models save little | Llama-2 7B on MATH 62.48 of 64; Vicuna 1.9x vs GPT-3.5 4.4x | c06, b13; K13 | E |
| Difficulty prior on top saves more | vs SC: -65.29% (GPT-4), -56.04% (GPT-3.5); vs ESC: -24.81%, -21.86%; only 3.8% of questions gain from SC (abstract only); CoT and SC agree on 96.2% (GPT-4) and 84.8% (GPT-3.5) of GSM8K items | a20, b16, c08; K04 | S |
| SPRT/mixture-SPRT on reasoning models | Token cuts up to 84.8% (AIME24 o3-mini-medium) and 86.2% (GPQA Diamond o3-mini-low); AIME24 o3-mini-low 70.0 to 80.0 (can sample past 40 on uncertain items; SC@40 was 70.0). Standard SPRT error rates (0.05/0.10) needed too many samples; authors retuned p0/p1 nearer 0.5 | c14, c15 | S |
| Consensus stop on long-chain reasoning models | DeepConf: 0.95 weighted-vote stop, 16-trace warm-up, cap 512; token cuts 18-85%; low variant 43-84.7% (GPT-OSS-120B AIME25 97.1 to 97.9 acc at -84.7% tokens; DeepSeek-8B AIME24 86.7 to 92.5 at -77.9%); high variant 18-59% with accuracy within about 1 point. Qwen3-32B AIME24 at 0.95: -15.4% (B = 32), -52.8% (B = 512), accuracy delta 0. At 0.90: -0.26 points. Looser bounds save up to 69.6%. Qwen3-8B AIME25 -4.4 points | a21, c12, c13, d01, d02; K22 | S (one paper) |
| Confidence-weighted voting | CISC, 9 models, 4 datasets: cost cut 41% (5 samples), 46% (10); 18.6 SC samples needed to match CISC at 10; Gemma2-9B MATH: 8 CISC beat 30 SC (73% cut). Between-question calibration did not predict gain; within-question discrimination did | b17, c10, c11; K05 | E |
| Early exit inside one chain | DEER: 11 reasoning models (1.5B-671B), 10 benchmarks, chain -19.1% to -80.1%, accuracy +0.3 to +5.0; about 75% of samples have an earlier correct exit. Convergence: models reach final answer after about 60% of the steps; NaturalQuestions over 40% fewer tokens. Overthinking: 2 to 4 solution rounds in 76-80% (QwQ) and 59-63% (R1) of cases; -48.6% tokens on MATH500 | a22, b19, b20, c17, c18, d08; K06 | E (3 sources) |
| A verifier beats agreement at equal sample count | Gemini 1.5 Pro, 200 samples, 50 verification scores per sample. AIME (15): pass@1 1, Cons@200 4, Cons@1000 3, Verif@200 8. MATH (500): 426, 460, 460, 467. LiveBench Math (200): 104, 118, 120, 135. LiveBench Reasoning (140): 63, 75, 73, 97 | d05; K19 | E at equal samples; equal tokens not measured |
| Coverage keeps rising, voting plateaus | MATH Llama-3-8B: coverage 82.9% (100 samples) to 98.44% (10,000); majority/reward 40.50 to 41.41%. SWE-bench Lite 15.9% (1) to 56% (250). 11.3% of SWE-bench Lite problems have flaky tests | b18, d03; K07, K19 | E |
| Verifier stops also fail | HumanEval+/MBPP: false-positive rate rises with attempts K; best K about 5 at cost ratio 4, often under 10, can be 0 | d04; K21 | S |
| Agreement locks on wrong consensus when the right answer is rare | One AIME problem: 1 correct in 200. Fixed-N voting is non-monotone with mixed difficulty (MMLU Physics, GPQA, TruthfulQA, AVeriTeC) | d03, d05, d07; K20 | E (structure); no rate measured |
| Difficulty-based allocation | Up to 4x less compute than best-of-N (MATH, PaLM 2-S*); weak-model agreement as difficulty signal gave 0.929 vs 0.931 at 40% of the cost (6 sets, GPT-3.5 weak, GPT-4 strong) | d06, d13, d16; K27 | E |
| Prompt style as difficulty signal | CoT plus PoT mixed agreement separated easy/hard better than same-prompt agreement | d13, d16; K23 | S |
| Self-consistency baseline gains grow with model scale | Code-davinci-002: GSM8K +17.9, SVAMP +11.0, AQuA +12.2, ASDiv +7.6, MultiArith +3.8; UL2-20B +3-6; LaMDA-137B +9-23 | a23, b12, c04; K08 | S |
| Agent-loop stop controller did not help | Terminal-Bench 2.1, 21 tasks, 315 trials, Claude Sonnet 5.5: cost x1.19 (CI 1.02-1.36), pass 73.0 vs 73.0; AUROC .78 (rules .62, small LLM .60); P(done) = .50 vs 87% passed; no abandon ever chosen | c24, d15; K14 | S |
| Trace length tracks human RT | Partial r with log human RT: GPT-OSS-120B .552, GPT-OSS-20B .41, Qwen3-235B .359, R1 .327, Kimi-K2 .303, GLM-4.5-Air .263, Qwen3-32B .229, DeepSeek-V3 (non-reasoning) .197. Item accuracy r = .668. Human accuracy 48.7% when 75%+ of models failed vs 84.6% when 75%+ got it right. N = 120 humans, 160 items | c22, c23; K15 | S |
| Instruction can move reasoning length | Chain of Draft: as little as 7.6% of CoT tokens; GPT-4o date 88.1 vs 90.2; coin flip 100 both. Token budget in prompt: -67% output, accuracy 81.03 vs 83.75; too small a budget raises tokens. Wait appended: AIME24 50 to 57 | d09, d10, d11; K26 | E (3 sources) |
| Free-form selection works but gives no bound | PaLM 2-L: GSM8K SC 90.4 vs USC 90.2; MATH 37.9 vs 37.4; BIRD-SQL 45.5 vs 45.6; GovReport ROUGE-1 38.8 to 40.2 | d14; K24 | S |

---

## 4. Mechanisms and models

Each model below is described so it can be coded. Costs are in samples unless stated.

### 4.1 Diffusion decision model (reference model, for understanding)

State: x(t), starts at z (between 0 and a).
Update per small step dt: `x += v*dt + s*sqrt(dt)*N(0,1)`.
Stop when x >= a (answer A) or x <= 0 (answer B). RT = t + Ter.
Per-trial draws: v ~ N(v_mean, eta), z ~ U(z0 +/- sz/2), Ter ~ U(Ter0 +/- st/2).
Predictions: larger a gives slower and more accurate answers. Smaller v gives slower and less accurate answers with a long right tail. Mean accuracy for the unbiased case is `1 / (1 + exp(-a*v/s^2))`.

Use for the agent: not as code, but as a model of what the dials do. Drift is item difficulty (not controllable). The bound is controllable.

### 4.2 SPRT (the stopping rule the diffusion model approximates)

```
S = 0
for each new sample i:
    S += log( P(sample_i | H1) / P(sample_i | H0) )
    if S >= log((1-beta)/alpha): accept H1
    if S <= log(beta/(1-alpha)): accept H0
```
Optimal in mean sample number when samples are i.i.d. with known distributions. Two errors: unknown per-sample reliability (what is P(sample | H)?) and non-independence. ConSol found that textbook error rates (0.05/0.10) need too many samples on LLM data and retuned p0/p1 closer to 0.5 and the prior (c14). The bound is a heuristic here, not a guarantee.

### 4.3 Beta-posterior agreement stop (Adaptive-Consistency)

```
counts of answers so far: v1 (leader), v2 (runner-up)
P_lead_is_majority = P( p1 > p2 ) with p ~ Beta(v1+1, v2+1)   # one-sided Beta test
if P_lead_is_majority >= 0.95 or n == cap(40): stop; answer = leader
else sample again
```
Only the top two counts matter (c02). Beta, Dirichlet and Chinese restaurant process versions give similar accuracy; Beta is about 10^4 times cheaper to compute (0.03 ms against 95-101 ms), which is irrelevant next to LLM cost. Threshold 0.95 was tuned once on GSM8K train and reused (c03). The accuracy-vs-threshold curve is smooth and plateaus while cost climbs steeply (c03). Needs i.i.d.-like samples; the authors expect it to fail where self-consistency fails.

### 4.4 Window rule (Early-Stopping Self-Consistency)

```
loop:
    draw w new samples (w = 5; 8 for hard maths); L = cap (40; 64 for MATH)
    if all w answers identical: stop
    if total >= L: stop
vote over everything drawn
```
No threshold to tune. A control scheme predicts cost and accuracy change from the first window (predicted-vs-actual correlation p < .05) (c07). Samples in a window share prompt tokens. Unanimity in a window can be a confident wrong answer (c05).

### 4.5 Difficulty-prior start (DSC)

Rank items by estimated difficulty on a batch first. Give easy items a tiny pre-allocated budget (even one sample). Use a posterior stop on the rest. It needs a batch and a difficulty-ranking pass that has its own cost (a20, c08).

### 4.6 Confidence-weighted vote (CISC)

For each sample ask the model P(True) for its own answer. Normalise within the question with a softmax (temperature tuned). Vote with the weights. The normalisation matters; the gain shrinks without it (c10). The best confidence method for this was not the best-calibrated one; the property that predicts gain is within-question discrimination (WQD) (c11).

Conflict with SCHEMA 4b: "Using a model's verbal confidence to stop" is listed as not to add. CISC does not stop on verbal confidence; it weights votes, and it is measured as better than unweighted votes. These are different uses. Treat CISC as a test item (U-list), not an add.

### 4.7 DeepConf (confidence-filtered traces plus consensus stop)

```
warm-up: run 16 traces to full length; record group confidence per trace
threshold = percentile of warm-up trace confidence (top 10% = aggressive, top 90% = conservative)
online: for each new trace, kill it when its running group confidence falls below threshold
        after each finished trace: weighted vote share of the leader
        stop when share >= 0.95 or traces == 512
```
Needs token log-probs. Savings start only after the warm-up, so they are larger at cap 512 than at cap 32 (52.8% vs 15.4% for Qwen3-32B). Authors name overconfident wrong traces as the key limit (c12, d02).

### 4.8 Within-chain early exit (DEER, answer convergence)

At each reasoning transition point (for example the token "Wait"), force a trial answer and read the model's confidence in it. Exit and answer if confidence is above a threshold. The variant in Liu and Wang stops when the answer is unchanged across k consecutive chunks (k = 10, c17). This is within one attempt, not across attempts. Prompt-based token limits worked on GSM8K but models ignored them on AIME24 (c18).

### 4.9 Verifier-based bound

Where a check exists (unit tests, a symmetry check, a held-out example), sample until the check passes or the cap is reached. Coverage rises over orders of magnitude of samples (d03), and the verifier turns coverage into accuracy. The check must be stricter than the one the attempt was fitted to, or the false-positive rate rises with attempts (d04). With a cost ratio of 4 for a wrong accept the best K was about 5.

### 4.10 Prior as start point, and the expected-value view

Human data say a prior moves the start point, or a bias that grows with time (b02, a09). For the agent the start point is the class-record prior from S0 (how often agreement was right in this problem class). Value-of-computation (b21) says stop when the expected gain of one more attempt falls below its cost: `gain(n) ~ P(change of answer) * P(change is an improvement)`; with no gain estimate, a cap works.

---

## 5. What holds up

### 5.1 Replications and meta-analyses

| Topic | Result | Strength |
|---|---|---|
| Fixed vs collapsing bound in humans | Hawkins 2015: 72/85 fixed; replication 76/91 fixed with strong support (64 very strong, 12 strong); Ratcliff 2016 review agrees with 10 studies, 3 labs | Strong for humans, short blocks |
| Fixed vs collapsing in monkeys | 4 of 8 collapsing; flips to 6 of 8 fixed when between-trial variability is removed | Fragile; depends on model terms |
| Optimal bound under mixed difficulty | Theory and 2 monkeys say collapse (a12); Hawkins finds practice and feedback delay matter | Contested |
| Agreement stop saves samples | Independently seen in Adaptive-Consistency (3.3x), ESC (up to 84%), ConSol (up to 86% tokens), DeepConf (18-85%) | Strong on closed-answer maths and commonsense |
| Early exit inside a chain | DEER, Liu and Wang, overthinking study all see savings | Strong, math-heavy |
| Verifier beats agreement at equal count | Large Language Monkeys and Sample-Scrutinize-Scale agree on direction | Moderate; equal tokens open |

### 5.2 Failures, nulls and boundary conditions

- **Hard items.** Llama-2 7B on MATH ran 62.48 of 64 samples; GPT-4 on MATH 42.4 of 64. Vicuna-13B saved 1.9x against 4.4x for GPT-3.5-turbo. Hard items run to the cap (c06, b13).
- **Reasoning-model accuracy loss.** Qwen3-8B on AIME25 lost 4.4 points under DeepConf; Qwen3-32B BRUMO25 lost 0.9 in the aggressive variant. Looser bounds (0.90, 0.85) cost accuracy in the aggressive filter variant. (c12, d02)
- **Rare right answers.** One AIME problem had 1 correct sample in 200; consensus picks wrong. Majority and a reward model plateau near 100 samples while coverage keeps rising (d03, d05).
- **Non-monotone voting.** Fixed-N voting accuracy first rises then falls with N on mixed-difficulty sets (d07). Mixed difficulty is where a fixed N is harmful.
- **Verifier false positives** rise with attempts (d04).
- **No measured confident-wrong rate** for the agreement stop exists in any source. This is the biggest missing number (critique GAP 2).
- **Independence.** Observed accuracy drops at the 0.95 bound are small (-0.1 to -0.2 in a17; -0.02 to -0.85 in a19), but benchmarks are where samples agree easily. No test used a consistent shared error. (a25 is a synthesis, not a source.)
- **Controller layer.** One learned stop/verify controller raised cost x1.19 (CI 1.02-1.36) with pass rate flat at 73.0 vs 73.0. Finish ranking was good (AUROC .78) but calibration was bad (.50 predicted vs 87% passed). One benchmark, 21 tasks; a null on pass rate, not proof that stop rules fail in general (c24).
- **Thinker-DDM** (c21): an explicit DDM inside translation outperformed baselines on WMT22/CommonMT but not on commonsense translation by default. Weak support for DDM-style decoding as such.
- **Opt-out** gave no accuracy gain in humans (b22).
- **Defaults of the human literature are model-dependent** (K18).

### 5.3 Moderators

| Moderator | Effect |
|---|---|
| Item difficulty | Savings large on easy sets, small on hard ones |
| Model strength | Weak models give a weaker majority signal; savings and SC gains shrink |
| Answer-space size | Self-consistency gain depends on it (b12) |
| Cap size | DeepConf savings 15.4% at cap 32 vs 52.8% at 512 |
| Threshold | 0.95 kept accuracy; 1.0 saved less; 0.90/0.85 saved up to 69.6% but cost accuracy in one variant |
| Confidence normalisation | CISC gain shrinks without within-question normalisation |
| Task type | All evidence is closed-answer; open-ended tasks have no bound |
| Model version | Many numbers from GPT-3.5, code-davinci, Vicuna (2022-2023); current reasoning models tested in DeepConf, DEER, ConSol, Liu and Wang only |
| Practice and feedback (humans) | Decide fixed vs collapsing |

### 5.4 Interventions that worked and did not

Worked (on the measured sets):
- Beta or window stop on agreement (E).
- Weighting votes by within-question confidence (E).
- Early exit inside long chains (E).
- Difficulty-based allocation (E).
- Verifier selection where a check exists (E at equal count).

Did not work, or no gain:
- Opt-out for humans (b22).
- A learned stop/verify controller in an agent loop (c24).
- Textbook SPRT error rates for LLMs (impractical; needed retuning).
- Random stopping (worst); majority-only stopping (mostly worse than Beta at equal cost).
- Prompt-embedded token budgets on hard items (ignored on AIME24; too-small budgets raise tokens) (c18, d10).
- Chain of Draft on models under 3B (gap to CoT larger) (d11).
- Thinker-DDM on commonsense translation by default (c21).

---

## 6. Language models

### 6.1 How LLMs behave on these tasks

1. **Sampling is a noisy accumulator.** Each sample is a vote. The share of samples agreeing with the final answer correlates with accuracy on GSM8K (d16, Figure 5; values not extracted). Agreement works as a confidence signal and as a difficulty signal.
2. **Most items converge fast.** For o3-mini, the top-answer share p1 is above 0.5 on most items; below 0.5 neither of the top two answers is likely right (c15). That is the basis for a two-hypothesis test (leader vs rest).
3. **Easy items waste samples.** Only 3.8% of questions (GPT-4) benefit from SC over one CoT (a20, abstract only); CoT and SC agree on 96.2% of GSM8K items (GPT-4) and 84.8% (GPT-3.5) at SC size 40 (b16).
4. **Reasoning models also waste tokens inside a chain.** About 60% of math reasoning runs after the answer has converged (c17). QwQ made 2 to 4 solution rounds in 76 to 80% of cases, R1 in 59 to 63%, and easier sets got more rounds (b19, d08). Chen et al. report that o1-like models used 1,953% more tokens than conventional ones on "2 plus 3" (b19).
5. **Trace length acts like reaction time.** Across 8 models the partial correlation with log human RT ranged from .197 (non-reasoning DeepSeek-V3) to .552 (GPT-OSS-120B). Averaging over many sampled runs raises alignment: GPT-OSS-20B .41 to .55 (T = 1, K = 25, p < .001); Qwen3-32B .23 to .32 (p < .05); R1 .32 to .37 (not significant). Estimates stabilise at about 8 to 19 runs. At T = 2 alignment fell to .22 (c22, c23). Single task family; tokens are not true time.
6. **Coverage vs accuracy.** With a perfect verifier, more samples keep adding coverage for orders of magnitude. Without one, majority and a reward model flatten near 100 samples (d03).

### 6.2 What changed behaviour, and by how much

| Lever | Change | Where measured |
|---|---|---|
| Stop on agreement (Beta, 0.95) | 3.3x fewer samples; accuracy -0.04 to -0.1 | 17 datasets, 3 older models (a17) |
| Stop on a unanimous window | -34% to -84% samples; accuracy within 0.02-0.85 | GPT-4, GPT-3.5, Llama-2 (a19) |
| SPRT on repeated answers | up to -86.2% tokens | o3-mini variants (c14) |
| Weighted consensus stop plus trace filtering | -18% to -85% tokens, accuracy within about 1 point (conservative) | DeepSeek-8B, Qwen3-32B, GPT-OSS-120B (d01) |
| Confidence-weighted vote | -41% (5 samples) to -46% (10) cost at equal accuracy | 9 models, 4 datasets (b17) |
| Difficulty prior | a further -22% to -25% vs ESC | GPT-4, GPT-3.5 (a20) |
| Early exit in a chain | -19% to -80% length, +0.3 to +5.0 points | 11 reasoning models (a22) |
| Weak-to-strong cascade by agreement | 40% of strong-model cost at equal accuracy | GPT-3.5 to GPT-4 (d13) |
| Verifier instead of agreement (equal count) | AIME 8 vs 4 of 15; LiveBench Reasoning 97 vs 75 of 140 | Gemini 1.5 Pro (d05) |
| Prompt style (5-word steps) | as low as 7.6% of CoT tokens, accuracy near CoT | GPT-4o, Claude 3.5 Sonnet (d11) |
| Appending "Wait" | AIME24 50 to 57 | s1-32B (d09) |
| Agent-loop controller | cost x1.19, pass rate unchanged | Claude Sonnet 5.5 on Terminal-Bench 2.1 (c24) |

Uncertainty to keep in view:

- Tokens vs samples vs chain length are three different cost units. Savings are not comparable across papers (critique).
- ESC says savings are large on easy sets and small on MATH; DSC claims further savings through priors; these were measured on different model versions.
- Savings in sample count may not equal savings in cost where samples share prompt tokens.
- Thresholds were tuned on the benchmarks they were scored on in at least one paper (a18, c03: tuned on GSM8K train then reused).

### 6.3 Gaps closed by the gap search (summary)

Closed or partly closed: reasoning models at scale (gap 1, DeepConf), verifier vs agreement at equal count (gap 4), free-form selection (gap 6, selection only), definitions (gap 9, via reviews). Still open: confident-wrong rate (2), fixed vs collapsing for LLMs (3), best difficulty signal head to head (5), agent-loop controllers beyond Vats (7), careful-vs-fast instruction mapped to a bound (8). See section 10.

---

## 7. What our agent should take

Schema parts: G = guardrail, S = state, O = operator, memory = section 5 of SCHEMA.md. The stop rule is program code in S3/S4 and in the S0 class record; it is not one of the idea-tree operators O1-O8. SCHEMA already carries G4 (samples not independent), G11 (think briefly, several short attempts), G12 (spend by difficulty), and 4b (do not use verbal confidence to stop; do not tell the model to slow down). Items below must agree with those or say where they push on them.

### Add now (established)

| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| A1 | **Replace fixed N with a sequential stop on agreement in direct and checked modes.** Draw attempts one at a time in fresh contexts (S3 rule). After each, compute the Beta posterior that the leader is the majority. Stop at 0.95. Cap at 40 (or the budget fraction). Code does the counting (G5). Expect about 2x-4x fewer attempts at about -0.1 points on easy and middle sets. | S3/S4 loop control; supports G12 | [E] for the saving (2 independent sources plus later ones); [S] that the exact 0.95 and cap 40 suit our model | K01, K03; a17, a18, b13, c01, c02, c14, d01 |
| A2 | **Always set a cap.** The bound is a heuristic SPRT with unknown per-sample reliability. State this in the schema. Hard items run to the cap and that is where the cap is paid. | S3/S4; method note | [E] | K13, K25, K11; c06, d18, d19 |
| A3 | **Use a verifier-based stop wherever a check exists** (a held-out check, unit tests, a symmetry): sample until the check passes, rather than until samples agree. At equal sample count verification wins. The check must be on something the attempt was not fitted to (G3), and the cap must stay low (best K about 5 in one cost model) because false positives rise with K. | S4, S7; G3 | [E] for the direction at equal count; equal tokens unmeasured | K19, K21, K07; d03, d04, d05 |
| A4 | **Spend by difficulty, not uniformly.** Let the class record (S0) set the starting allocation: items in classes where agreement has been right get a small first window; others get more. | S0/S1; G12; memory class record | [E] | K27; d06, d13, d16 |
| A5 | **Use only the top-two counts.** Do not build a Dirichlet or other fancy counter. | S3/S4 code | [E] | K03; a18, c02 |
| A6 | **Do not add an extra stop/verify controller layer.** Keep the finish rule in S9 as plain code. | S9 | [S] (one test, 21 tasks) but consistent with G1 and G7 | K14; c24 |
| A7 | **Treat published bound values as model-specific; report two aggregators.** Method caution only. | G7 logging | [E] | K18; b10, b11, b06 |
| A8 | **Log, for every stop, the agreement level, samples used, difficulty bin and whether the answer was right.** This produces the confident-wrong rate no source has. | section 6 logging | [E] logging need (gap 2) | K20; critique GAP 2 |

### Test first

| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| T1 | **Window-5 stop vs Beta stop vs fixed N at matched tokens.** | S3/S4 | [S] (one paper for the window rule) | K02; a19, c06 |
| T2 | **Confident-wrong rate of the 0.95 stop, same-prompt vs varied-prompt samples.** If varied prompts lower wrong stops at equal tokens, add prompt variation. Note: G4 forbids persona or strategy voters on single-answer problems, so varied means rewording and format, not personas. | G4/G12; S3 | [S] / [C] | K12, K20, K23; d03, d07, d13 |
| T3 | **First-two-sample agreement as the starting-bound signal** (triage before sampling) vs uniform start vs trace length vs confidence. | S0/S1 | [S] | K04, K15, K27; a20, c22, d13 |
| T4 | **Relaxing threshold (cap-limited) vs fixed threshold on a mixed-difficulty set.** | S3/S4 | [C] | K10; a11, a12, d07, d18 |
| T5 | **Agreement bound on long-chain reasoning (16-trace warm-up, 0.95, cap 64).** | S3/S4 | [S] (one paper, DeepConf) | K22; d01, d02 |
| T6 | **Within-chain early exit (answer unchanged across k probes)** to cut tokens per attempt. | S5/budget per attempt; G11 | [E] on others' models, untested on ours | K06; a22, c17, b19 |
| T7 | **Confidence-weighted vote (CISC style) vs unweighted at equal tokens.** Measure within-question AUROC first. Conflicts in spirit with 4b (verbal confidence to stop) because it is a weight, not a stop; keep it a test. | G5 (code selects) | [E] elsewhere, untested here | K05; b17, c10, c11 |
| T8 | **Verifier bound vs agreement bound at equal total tokens (include verification calls).** | S4/S7 | [E] at equal count, open at equal tokens | K19; d05 |
| T9 | **Careful vs fast instruction as a bound knob.** SCHEMA 4b says telling the model to be careful did not help diagnostic accuracy (F07); the human diffusion result says the bound moves with the instruction. Check on LLM cost per accuracy point; do not assume. | G (caution knob) | [E] in humans; [C] for LLMs | K09, K26; a02, d09, d10, d11 |
| T10 | **Abstain option with a measured benefit** (G6 says never abstain on the first pass; test only the end-of-budget case). | G6 / S9 | [S] (human null) | K16; b22 |
| T11 | **Allocate attempts by estimated gain per item** (value-of-computation). | S0/S1, G12 | [S] | K17; b21 |
| T12 | **Pairwise agreement bound on open drafts.** | open mode S3/S7 | [S] | K24; d14 |

Full test rules are in UNKNOWNS.md.

---

## 8. Concrete tests on our bench

All arms get the same total token budget per item (mean across the set, or a strict per-item cap for hard-cap tests), including setup and verification tokens (G7). Report accuracy, mean attempts and mean tokens per item, by difficulty bin (easy: plain pass rate above 0.9; mid: 0.4-0.9; hard: below 0.4).

| Test | Item type | Arms (equal mean tokens) | Metric | Expected effect |
|---|---|---|---|---|
| E1: Beta stop vs fixed N | Closed-answer items with exact match (maths, small puzzles, ARC-style outputs with grid match) | (a) fixed N = 10 majority; (b) Beta stop 0.95, cap 40, tuned to the same mean tokens; (c) single attempt | Accuracy; mean attempts; accuracy per 1k tokens | (b) about equal accuracy at 2x-4x fewer attempts, or +1-3 points at equal tokens (K01, c03). Hard bin shows no saving |
| E2: Stop rule shape | Same as E1 (replay stored answers) | Beta, window-5, SPRT (p0/p1 near .5), entropy, random; cost-matched at 1.0x, 0.5x, 0.3x of fixed N | Accuracy at each cost | Beta, window and SPRT within 1 point; random worst (K03). Replay from stored answers costs no new calls |
| E3: Confident-wrong audit | Hard and mixed set with known gold (include items where the right answer is rare) | Same-prompt samples vs reworded/format-varied samples; same stop rule | Share of stops at >= .95 whose answer is wrong, by bin; accuracy | Wrong-stop share is the missing number. Varied prompts lower it, if Yue's routing result carries over (K23) |
| E4: Fixed vs relaxing bound | Mixed-difficulty set | (a) fixed 0.95; (b) threshold relaxing from 0.95 to 0.80 as samples approach cap; (c) fixed N | Accuracy and tokens per bin | Relaxing saves tokens on hard bins with a small loss; humans predict no difference (K10). Contested; run before choosing |
| E5: Triage signal | Mixed set | Uniform start; first-two-sample agreement; trace length; confidence (P(True)) as bound-setter | Accuracy per 1k tokens; AUROC of the signal for later failure | Triage saves a further 20%+ if it separates easy from hard (a20 shows 22-25% over ESC); trace length may predict failure (K15) |
| E6: Verifier vs agreement | Code tasks and any maths task with a held-out check | (a) agreement bound; (b) test-pass bound with cap 5; (c) test-pass bound with cap 20, stricter held-out check scored separately | Accuracy against the stricter check; tokens including verification | Verifier wins in accuracy per token on code; false positives lift with cap (K19, K21) |
| E7: Reasoning-model consensus | Hard maths (AIME-like) or hardest ARC subset | Full majority at 64; consensus stop 0.95 after 16 warm-up, cap 64; conservative vs aggressive filter if log-probs exist | Accuracy; tokens | 18-85% tokens saved within about 1 point (conservative); one model may lose several points (Qwen3-8B -4.4) (K22) |
| E8: Within-chain exit | Items answered by extended thinking | Full chain vs trial answer at each transition, stop after k = 2 and k = 3 consistent probes | Accuracy; tokens per attempt | 19-80% shorter at equal or better accuracy (K06) |
| E9: Careful vs fast | Mixed set | "Answer fast", default, "be careful" instructions, same model | Accuracy and tokens; cost per accuracy point | Expect token changes without accuracy change (4b); fit the cost per point (K26) |
| E10: Confidence weighting | Closed-answer set | Unweighted vote; P(True)-weighted vote; confidence-filtered stop | Accuracy at 5 and 10 attempts | Weighted vote needs about half the attempts if within-question AUROC is high (K05); measure AUROC first |
| E11: Agent-loop finish rule | Agent tasks with tests | S9 plain finish rule vs the same plus an LLM stop controller | Pass rate; cost | No pass-rate gain from the controller (K14) |
| E12: Abstain at the end | Mixed set | Always answer vs abstain below threshold, equal total tokens | Accuracy on answered items; coverage | Human null predicts no gain (K16) |

Replay trick: log every attempt's answer and tokens once. E1, E2 and E4 can be computed offline from stored answers, which makes them cheap.

---

## 9. What does not transfer, and why

| Human/animal result | Why it does not transfer |
|---|---|
| Absolute bound values (a = .109, .152) | Model-specific and in evidence units; not defined as logLR (b10, b11, d19) |
| Reaction time in milliseconds and the 120-200 ms cost | Tokens and samples are the cost unit; the shape of the trade-off is the only part that carries |
| Neural ramps in LIP | Describes brain hardware, not a decision procedure; no counterpart in a transformer sampling loop |
| Fixed bound as the best policy for humans | Human blocks mixed one difficulty per cue; LLM item sets mix difficulty widely, so the adaptive rule can win (critique note; analogy only, b26) |
| Start-point shift for priors | Our prior is the class record from S0; the human 75:25 prior is an explicit cue |
| Urgency signal | Humans pay a time cost per second; the agent pays a token budget, a different cost curve |
| Independent noisy samples (SPRT assumption) | LLM samples are correlated and may share a wrong answer (G4); human trial noise is not fully independent either, but the hazard differs |
| Human insensitivity to an opt-out (b22) | Human skipping needed an action under the same deadline; the agent's abstain costs nothing extra |
| Chess time as value of computation (b21) | Observational on humans; not a process model |
| Reward-rate optimality failures in humans (b05) | The agent's rule is written in code and can be exactly optimal for a stated cost |
| Two-choice DDM | The agent faces many-option, open or non-verifiable answers; Bogacz optimality is for two alternatives |
| Trace length = reaction time (c22) | Single task, tokens are not time; only a difficulty signal, not a mechanism |
| Thinker-DDM boundary decay | Design choice, evidence scored by another model (c21) |

---

## 10. Open questions

1. How often does the 0.95 agreement stop land on a wrong consensus, by difficulty? No source reports it (critique GAP 2).
2. Does varying prompt wording between samples lower the confident-wrong rate at equal tokens? Only routing quality was measured (d13).
3. Fixed vs collapsing bound for an LLM on mixed difficulty? Humans say fixed (72/85), theory says collapse, no LLM test exists.
4. Verifier bound vs agreement bound at equal total tokens? Equal count only (d05).
5. Which cheap difficulty signal is best for setting the starting bound (first-two agreement, trace length, confidence)? No head to head.
6. Do stop rules work on open or non-verifiable tasks? Selection works (d14) but gives no confidence, so no bound is available.
7. Does a stop controller inside an agent loop ever help? One null (Vats); absence of other tests is limited by the search quota.
8. Does a "be careful" or "be fast" instruction move the effective bound? Proxies exist (d09-d11) but none gives cost per accuracy point; SCHEMA 4b already notes the human diagnostic null.
9. Faithfulness of the Beta/SPRT mapping to Gold and Shadlen 2007 and Ratcliff 1978: neither was opened. Reviews (d18, d19) say the DDM bound is in evidence units, not logLR, and flat bounds are optimal only for known stationary reliability.
10. Do current closed reasoning models (o3 class) show the same savings? ConSol used o3-mini; DeepConf used open models.
11. Does the human practice effect (monkeys collapse with heavy practice) have an analogue in an agent that learns per-class bounds from its class record?
12. Are the thresholds in the published papers over-fit? Adaptive-Consistency tuned 0.95 on GSM8K train; no held-out threshold test was seen (a18).
13. DSC's 3.8% figure and Wang 2023 gains were read at abstract level; the DSC 65.29/56.04 and 24.81/21.86 numbers were not re-checked beyond earlier full-text reading (critique item 11).

---

## 11. Sources

[V] = opened and read this run (page or PDF text). [M] = snippet, abstract, metadata or background knowledge only.

**Human and animal**

- [V] Ratcliff and McKoon (2008) The diffusion decision model: theory and data for two-choice decision tasks. https://pmc.ncbi.nlm.nih.gov/articles/PMC2474742/ (a01-a03, b01-b03, d19; first about 100k of 177k characters)
- [M] Ratcliff (1978) A theory of memory retrieval. https://doi.org/10.1037/0033-295X.85.2.59 (a04)
- [M] Wald (1945) Sequential tests of statistical hypotheses; Wald and Wolfowitz (1948). https://doi.org/10.1214/aoms/1177731118 (a05, c25)
- [M] Gold and Shadlen (2007) The neural basis of decision making. https://doi.org/10.1146/annurev.neuro.29.051605.113038 (a06, b25, d20; publisher 403, metadata only)
- [V] Roitman and Shadlen (2002) Response of neurons in LIP during a combined visual discrimination reaction time task. https://pmc.ncbi.nlm.nih.gov/articles/PMC6758024/ (a07)
- [V] Kiani, Hanks and Shadlen (2008) Bounded integration in parietal cortex underlies decisions even when viewing duration is dictated by the environment. https://pmc.ncbi.nlm.nih.gov/articles/PMC6670720/ (a08)
- [V] Hanks et al. (2011) Elapsed decision time affects the weighting of prior probability. https://pmc.ncbi.nlm.nih.gov/articles/PMC3356114/ (a09)
- [V] Hanks, Kiani and Shadlen (2014) A neural mechanism of speed-accuracy tradeoff in macaque area LIP. https://pmc.ncbi.nlm.nih.gov/articles/PMC4054775/ (a10)
- [V] Hawkins, Forstmann, Wagenmakers, Ratcliff and Brown (2015) Revisiting the evidence for collapsing boundaries and urgency signals. https://pmc.ncbi.nlm.nih.gov/articles/PMC6605613/ (a11, b07, b08)
- [V] Drugowitsch et al. (2012) The cost of accumulating evidence in perceptual decision making. https://pmc.ncbi.nlm.nih.gov/articles/PMC3329788/ (a12)
- [M] Palmer, Huk and Shadlen (2005) The effect of stimulus strength on the speed and accuracy of a perceptual decision. https://doi.org/10.1167/5.5.1 (a13, second-hand via a11)
- [M] Bogacz et al. (2006) The physics of optimal decision making. https://doi.org/10.1037/0033-295X.113.4.700 (a14, b24)
- [M] Usher and McClelland (2001) The time course of perceptual choice. https://doi.org/10.1037/0033-295X.108.3.550 (a15)
- [M] Brown and Heathcote (2008) The simplest complete model of choice response time. https://doi.org/10.1016/j.cogpsych.2007.12.002 (a16)
- [V] Ratcliff, Smith, Brown and McKoon (2016) Diffusion decision model: current issues and history. https://pmc.ncbi.nlm.nih.gov/articles/PMC4928591/ (b04-b06; about 100k of 206k characters)
- [M] Voskuilen, Ratcliff and Smith (2016) Comparing fixed and collapsing boundary versions of the diffusion model. https://pmc.ncbi.nlm.nih.gov/articles/PMC5450920/ (b09; page blocked)
- [V] Hato, Schumacher, Radev and Voss (2025) Levy versus Wiener. https://pmc.ncbi.nlm.nih.gov/articles/PMC13298659/ (b10)
- [V] Systematic drift rate variability study (2026). https://pmc.ncbi.nlm.nih.gov/articles/PMC13293026/ (b11)
- [V] Time spent thinking in online chess reflects the value of computation (2025). https://pmc.ncbi.nlm.nih.gov/articles/PMC12553403/ (b21)
- [V] The limits of metacognitive control during perceptual decision-making (2025). https://pmc.ncbi.nlm.nih.gov/articles/PMC12131516/ (b22)
- [M] Evans and Wagenmakers (2020) Evidence accumulation models: current limitations and future directions. https://doi.org/10.20982/tqmp.16.2.p073 (b23)
- [V] Shadlen and Kiani (2013) Decision making as a window on cognition. https://pmc.ncbi.nlm.nih.gov/articles/PMC3852636/ (d18)

**Language models**

- [V] Wang et al. (2023) Self-consistency improves chain of thought reasoning. https://arxiv.org/abs/2203.11171 (a23, b12, c04, d16; a23 abstract only, the others full text)
- [V] Aggarwal, Madaan, Yang and Mausam (2023) Adaptive-Consistency. https://arxiv.org/abs/2305.11860 (a17, a18, b13, b14, c01-c03)
- [V] Li et al. (2024) Early-Stopping Self-Consistency. https://arxiv.org/abs/2401.10480 (a19, b15, c05-c07)
- [V] Wang et al. (2025) Difficulty-Adaptive Self-Consistency. https://arxiv.org/abs/2408.13457 (a20, b16, c08; partly read)
- [V] Wan et al. (2025) Reasoning-Aware Self-Consistency. https://arxiv.org/abs/2408.17017 (c09)
- [V] Taubenfeld et al. (2025) Confidence improves self-consistency (CISC). https://arxiv.org/abs/2502.06233 (b17, c10, c11)
- [V] Fu et al. (2025) Deep Think with Confidence. https://arxiv.org/abs/2508.15260 (a21, c12, c13, d01, d02)
- [V] Lee et al. (2025) ConSol. https://arxiv.org/abs/2503.17587 (c14, c15)
- [V] Wang et al. (2025) OptPO. https://arxiv.org/abs/2512.02882 (c16)
- [V] Yang et al. (2025) DEER. https://arxiv.org/abs/2504.15895 (a22, b20, c18)
- [V] Liu and Wang (2025) Answer convergence as a signal for early stopping. https://arxiv.org/abs/2506.02536 (c17)
- [V] Chen et al. (2025) Do not think that much for 2+3=? https://arxiv.org/abs/2412.21187 (b19, d08)
- [V] Muennighoff et al. (2025) s1: Simple test-time scaling. https://arxiv.org/abs/2501.19393 (c19, d09)
- [V] Wang et al. (2025) Self-estimating best-of-N. https://arxiv.org/abs/2503.01422 (c20)
- [V] Na et al. (2025) Thinker-DDM. https://arxiv.org/abs/2402.10699 (c21)
- [V] Arthur (2026) Thinking effort aligns between humans and reasoning models in abductive reasoning. https://arxiv.org/abs/2609.01867 (c22, c23)
- [V abstract only] Vats (2026) Good judgment, bad advice. https://arxiv.org/abs/2610.24649 (c24, d15; critique re-opened abstract and table)
- [V] Brown et al. (2024) Large language monkeys. https://arxiv.org/abs/2407.21787 (b18, d03)
- [V] Stroebl, Kapoor and Narayanan (2024, v3 2026) Inference scaling flaws. https://arxiv.org/abs/2411.17501 (d04)
- [V] Zhao, Awasthi and Gollapudi (2025) Sample, scrutinize and scale. https://arxiv.org/abs/2502.01839 (d05)
- [V] Snell et al. (2024) Scaling LLM test-time compute optimally. https://arxiv.org/abs/2408.03314 (d06)
- [V] Chen et al. (2024) Are more LM calls all you need? https://arxiv.org/abs/2403.02419 (d07)
- [V] Han et al. (2024, v6 2026) Token-budget-aware LLM reasoning. https://arxiv.org/abs/2412.18547 (d10)
- [V] Xu et al. (2025) Chain of Draft. https://arxiv.org/abs/2502.18600 (d11)
- [V] Jurayj, Cheng and Van Durme (2025) Is that your final answer? https://arxiv.org/abs/2502.13962 (d12)
- [V] Yue et al. (2024) LLM cascades with mixture of thought representations. https://arxiv.org/abs/2310.03094 (d13)
- [V] Chen et al. (2023) Universal self-consistency. https://arxiv.org/abs/2311.17311 (d14)
- [V] Setlur et al. (2025) Scaling test-time compute without verification or RL is suboptimal. https://arxiv.org/abs/2502.12118 (d17)

Syntheses not counted as sources: a24, a25, b26, c26, c27.

## Source audit (2026-11-01)

Fresh auditors re-opened the sources of 13 established claims: 7 confirmed as written, 6 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **B02.07-K03** (reworded: the sources support less). Only Aggarwal et al. compare stopping rules head to head (Beta, Dirichlet, CRP similar; Beta consistently beats entropy and majority; random worst); SPRT (ConSol), difficulty prior (DSC) and RASC are separate papers on different models and benchmarks with different savings (up to 84.8-86.2% tokens, 56-65% cost, ~70% samples), so 'similar savings' across all five rules is not shown. Corrected claim: In a head-to-head comparison (Aggarwal et al. 2023) the Beta, Dirichlet and Chinese-restaurant-process stopping rules reach similar savings while Beta beats entropy and majority-only at equal cost and random stopping is worst; SPRT (ConSol), difficulty-prior (DSC) and quality-weighted (RASC) stopping each report 56-86% cost or token savings versus self-consistency, but on different models and benchmarks and not compared against one another.
- **B02.07-K05** (reworded: the sources support less). 40 to 85 percent mixes CISC's average 41-46% sample reduction (some cells over 67%) with DeepConf's best-case 84.7% token cut; DeepConf savings run 15-85% depending on setting and its aggressive variant can lose accuracy, so 'same accuracy with 40 to 85 percent fewer' is too uniform. Corrected claim: Weighting votes by model confidence reaches the same accuracy with fewer samples or tokens: P(True)-weighted voting (CISC) cut samples by 41% at 5 and 46% at 10 samples on average (some settings over 67%), and trace-confidence filtering (DeepConf) cut tokens by 18-85% depending on variant, with the aggressive variant sometimes losing accuracy; between-question calibration (ECE, Brier) does not predict the gain, within-question discrimination does.
- **B02.07-K06** (number corrected). Liu and Wang report models converge to their final answer after about 60% of reasoning steps on math, so about 40% (not 60%) of reasoning follows convergence. Corrected claim: Reasoning models can stop their own chain early: exiting at a high-confidence trial answer (DEER) cuts chain length 19.1 to 80.1 percent with accuracy changes of +0.3 to +5.0 points, and on math tasks models typically converge to their final answer after about 60 percent of the reasoning steps, leaving about 40 percent of the chain after convergence.
- **B02.07-K09** (reworded: the sources support less). Numbers check out, but Hanks et al. 2014 found the monkey LIP termination threshold did NOT differ between speed and accuracy regimes (speed pressure acted via an evidence-independent urgency signal), so 'in humans and monkeys the instruction moves the bound' is wrong for monkeys; Hawkins et al. speaks to fixed vs collapsing bounds, not the instruction effect. Corrected claim: In humans a speed-accuracy instruction moves the diffusion boundary (boundary 0.109 vs 0.152, N=14; median RT 120-200 ms longer in the accuracy regime, accuracy changing 0-6%), and 72 of 85 humans are best fit by a fixed (non-collapsing) bound; in macaques the neural termination threshold was similar across regimes (RT 176 and 159 ms longer under accuracy emphasis), with speed pressure acting through an evidence-independent urgency signal. No LLM test of a careful-versus-fast instruction against a diffusion boundary was found; closest proxies are prompt-based token budgets.
- **B02.07-K18** (reworded: the sources support less). Hato et al. support bound dependence on model (R2 .99 to .77, boundary overestimated under misspecification), but the 114,803 to 37,537 WAIC figure (Sun et al.) is a model-fit improvement from adding trial-level predictors, not evidence that fitted bound values change. Corrected claim: Fitted bound values depend on the model: boundary recovery R2 drops from .99 to .77 and boundary separation is overestimated when Levy-flight data are fit with a Wiener DDM (Hato et al. 2025). Separately, adding trial-level (systematic) drift predictors improved WAIC from 114,803 to 37,537 in a recognition-memory dataset (Sun et al. 2026), showing that the standard model is a poor fit, though that paper does not report resulting bound shifts.
- **B02.07-K19** (reworded: the sources support less). Only Zhao et al. show a verifier (model self-verification) beating agreement at equal sample count; Brown et al. find reward models plateau like majority voting (40.50 to 41.41 range) and Setlur et al. compare verifier-based vs verifier-free fine-tuning, not selection at equal sample count, so 'tests, ... reward-based' beating agreement is not shown. Corrected claim: At equal sample count, picking by repeated model self-verification beat picking by agreement (Gemini 1.5 Pro, 200 samples: AIME 8 vs 4 of 15, LiveBench Reasoning 97 vs 75 of 140), while agreement and off-the-shelf reward models both plateau near 100 samples (MATH Llama-3-8B majority 40.50 to 41.41 percent from 100 to 10,000 samples vs coverage 82.9 to 98.44). Equal-token comparison is not measured (verification used 50 calls per sample).
- **B02.07-K01** (now single-source: only one opened source, code check).
