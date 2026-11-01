# Sequential analysis: deep document

*Subfield C12.04. Stop a test when evidence suffices. Built from evidence_a-d.jsonl (a01-a27, b01-b27, c01-c25, d01-d21), claims.jsonl (K01-K33) and critique.md in this folder. No new search was done. Ids like a12 point to evidence lines; K-ids point to claims.*

## 1. What it is

Sequential analysis means you do not fix the sample size in advance. You take one observation (or one batch), update a running score, and ask: is the evidence enough to stop? If yes, stop and decide. If no, take more. The sample size is random.

The core tool is Wald's sequential probability ratio test (SPRT). It keeps the likelihood ratio of two hypotheses. It stops at an upper bound (accept H1) or a lower bound (accept H0). The bounds come from the error rates you accept (a01, a02).

Why it matters for our agent: the agent can draw several independent attempts at a problem and vote. The question is when to stop drawing. This is the same problem as a quality-control inspector deciding when to stop sampling a batch. In LLM work it is called early-stopping self-consistency, adaptive sampling, or consensus-based stopping.

Three families are in scope:
1. Classical tests: SPRT, group-sequential designs (Pocock, O'Brien-Fleming), Bayesian sequential tests.
2. Anytime-valid methods: mixture SPRT, confidence sequences, e-values. They keep error guarantees even if you stop whenever you like (a07-a10).
3. LLM stop rules for sampling and voting: Adaptive-Consistency, ESC, ConSol, DeepConf, DSC, plus stop rules for debate and for single reasoning chains.

Two things must be kept apart:
- **Stopping on agreement certifies the model's own mode, not the truth** (K25, d04). If the model's most common answer is wrong, a perfect stop rule stops on a wrong answer, with confidence.
- **Stopping on a check** (tests pass, verifier says yes) certifies something outside the model's own sampling. This is stronger, and the schema already prefers it (G3, G4).

Scope limit: nearly all LLM evidence is short-answer math and multiple choice. Nothing found tests stopping on open-ended generation or agent tasks (K22, c25).

## 2. History and theories in depth

**Before Wald.** Neyman and Pearson (1933) gave the fixed-sample likelihood-ratio test. It motivated Wald's reformulation (a02). Barnard led a parallel British group in WWII (a03).

**Wald, 1943-1945.** Abraham Wald worked with Wolfowitz, Wallis and Friedman in Columbia's Statistical Research Group. The method was used in industrial quality control and was classified as restricted (a03). Wald (1945) published the SPRT. After each observation, compute the likelihood ratio of H1 to H0. Accept H1 if it passes A = (1-beta)/alpha. Accept H0 if it falls below B = beta/(1-alpha). Otherwise continue. True error rates are bounded: alpha' <= 1/A and beta' <= B (a01, quoted by Stefan et al. 2022). In discrete steps the ratio can overshoot a bound, so these are approximations (a02). [M] Wald 1945 itself was not opened (publisher block). Details come from secondary sources that were read.

**Wald and Wolfowitz, 1948.** They proved the SPRT has the smallest expected sample size among all tests, sequential or not, with error rates no larger than the SPRT's, under both H0 and H1 (a04). [M] Not opened. The popular "about half the samples" figure is from memory and is not verified (K02, b23, c20). One lecture page claims 2-3x saving in a Gaussian shift example, also unverified (a04).

**Group-sequential designs.** Armitage, McPherson and Rowe (1969) showed that repeated significance testing at nominal 5% inflates false positives: from memory about 14% after 5 looks and 19% after 10 (b24, [M]). Pocock (1977) used a constant stricter nominal level per look, about 0.0158 for 5 looks (from memory, b25). O'Brien-Fleming, Wang-Tsiatis and Haybittle-Peto are alternatives. Pocock needs pre-set, equally spaced looks. Lan-DeMets alpha-spending removes the fixed-look restriction (a03). Bassler et al. (2010): trials stopped early for benefit overstate the effect, ratio of relative risks about 0.71 (CI 0.65-0.77), worse with few events (b25, from memory, [M]).

**Robbins, Ville, and "power one".** Ville (1939) gave an inequality for nonnegative supermartingales. Darling and Robbins (1967-68) and Robbins (1970) built mixture martingales on it. They give a test with power one: if the alternative is true, it stops with probability 1. If the null is true, the chance the evidence ever reaches 1/alpha is at most alpha (a23, secondary only).

**Modern anytime-valid inference.**
- Johari, Pekelis, Walsh (2015/2019): always-valid p-values via the mixture SPRT, deployed in a commercial A/B-testing platform (a07, b21).
- Howard, Ramdas, McAuliffe, Sekhon (2021): time-uniform confidence sequences, width O(sqrt(log log t / t)), matching the law-of-the-iterated-logarithm rate. They generalise Wald's SPRT to nonparametric cases (a08, b22).
- Ramdas, Grunwald, Vovk, Shafer (2023) and Grunwald, de Heide, Koolen (2023): evidence as a betting score (e-value, e-process). Tests built this way allow stopping or continuing for any reason (a09, a10). Growth-rate-optimal e-values take the form of Bayes factors.
- Stefan, Schoenbrodt, Evans, Wagenmakers (2022): the SPRT and the sequential Bayes factor test are two cases of one framework. With point priors, the Bayes factor reduces to the likelihood ratio (a05, a26).

**Other uses.** Models of speeded decisions in humans and animals (Luce 1986; Ratcliff 1978; Bogacz et al. 2006), computerized classification testing, surgeon-outcome monitoring charts, MaxSPRT for safety surveillance (a02, a24). The human decision-model link is a pointer only; the Evidence accumulation subfield covers it.

**Arrival in LLM work.**
- 2022: Wang et al. self-consistency: sample many paths, majority vote. The fixed-budget baseline (a11).
- 2023: Aggarwal et al. Adaptive-Consistency: Bayesian stop on vote counts (a12). Universal Self-Consistency defines agreement for free-form text (d13).
- 2024: Li et al. ESC: stop at the first window where all answers agree (a14). Chen et al.: more votes can hurt on mixed difficulty (b18). Brown et al.: voting plateaus (b19). Snell et al.: compute-optimal allocation by difficulty (b20).
- 2025: ConSol, the first real Wald SPRT on vote counts (a19). DSC, difficulty-first allocation (a16). CISC, confidence-weighted votes (a17). DeepConf, token-confidence stop (a18). RASC, Path-Consistency, self-calibration, DEER, answer convergence, Pandora's-box stopping, Certified Self-Consistency, debate stability stop (c13-c17, d04, d17).
- 2026: first independent re-runs (CGES d01, d02; Blend-ASC d16) and the first SPRT stop for debate (Morandi, a21).

**Competing explanations for why agreement-stopping works** (b27):
1. The correct answer is drawn more often than any wrong one, so the mode stabilises early (Wang, Aggarwal, ConSol).
2. Difficulty varies. Easy items agree fast; hard items never do. Most of the saving is skipping easy items (DSC, ESC, Chen).
These are not exclusive. K08 adds a third part: at equal average cost, adaptive stopping beats fixed n, so some of the gain is moving samples from easy to hard items.

## 3. Core findings with exact numbers

Status: established = two or more independent sources, numbers re-opened; single-source = one source or one group; contested = sources disagree or the headline is misleading; [M] = not opened.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| SPRT stops at LR bounds A=(1-b)/a, B=b/(1-a) | error bounds a'<=1/A, b'<=B; approximate (overshoot) | Wald 1945 via a01, a02, a05 | established (secondary) |
| SPRT has minimum expected sample size at given error | "about half" is memory only | Wald-Wolfowitz 1948 [M] (a04, d20) | single-source |
| Bayes factor with point priors = LR | informed-prior SBFT more efficient but less robust to misspecification | Stefan 2022 (a05, a26) | established |
| Sequential designs cut sample size 50%+ in human research | "even the least efficient sequential design beats the best fixed design" | Stefan 2022 (a05, a06) | single-source |
| Peeking inflates Type I error | fivefold at 10,000 samples (A/B); 14% / 19% at 5 / 10 looks from memory | Johari 2019 (b21); Armitage 1969 [M] | established |
| Mixture SPRT is robust to prior misspecification | 2 orders of variance: <5% power loss, <10% run-length cost; beyond: up to 20% power, 40% run-length; run-length 20% better than fixed for most settings, up to 40% | Johari 2019 (a07, a27, b21) | established |
| Self-consistency beats greedy CoT | PaLM-540B, 40 samples: GSM8K +17.9, SVAMP +11.0, AQuA +12.2, StrategyQA +6.4, ARC-c +3.9 | Wang 2023 (a11, b01) | established |
| Adaptive-Consistency (Beta posterior stop) | up to 7.9x fewer samples (Boolean Expressions), mean drop <0.1; math 13.8 vs 40 samples (3.3x), 73.2 vs 73.1; commonsense 15.8 (2.9x), 66.0 vs 65.8; symbolic 13.1 (3.8x), 72.8 vs 72.8; code 173.6 vs 312.5 (2.4x, +0.4) | Aggarwal 2023 (a12, b03, critique) | established |
| Savings depend on model | GPT-3.5-Turbo 4.4x (10.0 vs 40; 76.4 vs 76.2); Code-davinci-002 3.4x (49.4 vs 104.1; 69.8 vs 69.7); Vicuna-13B 1.9x (21.7 vs 40; 54.0 vs 54.1) | Aggarwal 2023 (b04) | established |
| Adaptive beats fixed n at equal average cost | GSM8K at 10 samples: about +3 points; up to +5 elsewhere. Beta > Entropy > Majority > Random. Dirichlet, CRP match Beta but are about 4 orders of magnitude slower (Beta 0.03 ms vs about 100 ms) | Aggarwal 2023 (b05, c03, d19) | established |
| ESC window stop | samples cut: MATH -33.8%, GSM8K -80.1%, StrategyQA -76.8%, CommonsenseQA -78.5%, Coin Flip -84.2%, Last Letters -67.4%; window 5 (MATH 8); 10 runs; cost-matched SC does worse | Li 2024 (a14, b06, b08) | established |
| ESC savings track model strength | MATH cap 64: GPT-4 60.31 both arms, 42.41 samples; GPT-3.5 49.96 both, 52.37; Llama-2-7b 7.70 both, 62.48 (almost none) | Li 2024 (b07) | established |
| ConSol SPRT cuts tokens | vs SC@40: 63.9 / 84.8 / 84.5% (AIME24 o3-mini low / med / high), 86.2% (GPQA low), 88.6% (GSM gpt-4o-mini); mSPRT 57.3-88.7%; AC 47.9-82.8% | Lee 2025 (a19, b09, c08) | single-source |
| ConSol accuracy | AIME24 low: SC 70.0, AC 70.0, SPRT 80.0, mSPRT 76.7; medium 90.0 all; high 96.7 all; GPQA low 68.2 / 67.2 / 66.7 / 70.2; GSM 94.2 / 94.2 / 93.5 / 93.9 | Lee 2025 (a19) | single-source |
| ConSol parameters are tuned | p1=0.5001 (textbook 0.55-0.6), alpha about 0.95 (0.949976; mSPRT 0.94994), Beta(1e6,1e6) prior; mSPRT alpha swept over only 0.00018; Wald guarantee void by design | Lee 2025 (a20, d05) | single-source |
| SPRT vs AC token cut | AIME24 high 84.5 vs 64.6; GSM 88.6 vs 82.8 (same authors, both arms) | Lee 2025 (b26) | single-source |
| Early no-consensus stop | if top share p1 < 0.5, extra samples rarely help; most o3-mini p1 > 0.5 | Lee 2025 (b10) | single-source |
| Agreement already high on easy items | CoT = 40-sample SC on 84.8% (GPT-3.5) and 96.2% (GPT-4) of GSM8K; disagree 15.2% / 3.8% | Wang 2025 DSC (a16, d15) | established |
| Difficulty-first allocation | cost -65.29% (GPT-4), -56.04% (GPT-3.5) vs SC; -24.81% / -21.86% vs ESC; six benchmarks | Wang 2025 (a16, c06) | established (one group plus independent partial) |
| Difficulty probe is weak | Spearman 0.624 (GPT-4), 0.440 (GPT-3.5) vs human labels; gate cost 1.9-3.1pp in an independent run | Wang 2025; CGES (d15, d01, d02) | single-source |
| Independent re-run, B=16 | ESC / ASC use 8.6-9.1 of 16 calls at -0.4pp (7B models, 10 seeds, 5 benchmarks) | Aghazadeh 2026 CGES (d01) | single-source (independent) |
| Independent re-run, small budgets | B=4: ASC 4.00 calls (no saving), -0.5pp; B=8 GSM8K: 8 to 4.49 calls, same accuracy; overall about 1-3.5 of 8 saved | CGES App. I (d02) | single-source |
| AC loses to fixed allocation at high budget | to match SC@64: fixed 4.09x, AC 4.36x, Blend-ASC 5.33x; SC@128: fixed 3.40x, AC 2.13x, Blend-ASC 4.2x; AC failed to reach target for Llama-3.2-3B on GSM8K | Feng 2026 (d16) | single-source |
| Weak confidence signal kills the stop | GPQA, R1-Distill-Qwen-7B: SC 50.0 (B=16); CGES 46.4-47.9 at 11.5-14.2 calls | CGES 4.4 (d03) | single-source |
| More votes can hurt | inverse U on MMLU Physics, TruthfulQA, GPQA, AVeriTeC; GPT-3.5-turbo-0125 only; up to 100 calls; synthetic optima 1-7 calls | Chen 2024 (b18, d06) | single-source |
| Recent models rise then flatten | SC at B=4/8/16: AIME24 69.7/76.0/77.3; GPQA 44.9/47.9/50.0; MATH500 77.8/79.8/81.2; GSM8K 93.3/93.9/94.2; MMLU-Pro 59.4/61.0/62.1 | CGES (d07) | single-source |
| Voting plateaus, coverage does not | Llama-3-8B MATH: coverage 82.9% (100 samples) to 98.44% (10,000); vote 40.50 to 41.41%. SWE-bench Lite 15.9% (1) to 56% (250) | Brown 2024 (b19, c18, d10) | single-source |
| Test-based stops are imperfect | 11.3% of SWE-bench Lite problems flaky; 35 of 122 CodeContests problems with correct solutions fail tests | Brown 2024 (d11) | single-source |
| Confidence-weighted vote | over 40% fewer paths (9 models, 4 datasets); P(True) 41% at budget 5, 46% at 10; SC needs 18.6 samples to match CISC at 10; Gemma2-9B MATH 73% | Taubenfeld 2025 (a17, c10) | single-source |
| Confidence source matters | cost cut at budget 5 / 10: verbal binary 18 / 10%; verbal 0-100 22 / 30%; response prob. 22 / 31%; P(True) 41 / 46%. Best-calibrated method was least useful | CISC (d09, a17) | single-source |
| DeepConf | AIME25 GPT-OSS-120B: 99.9% @512 vs majority 97.0, pass@1 91.8; online tokens -84.7% (3.23e8 to 0.49e8; 97.1 to 97.9); HMMT25 -76.2%; DeepSeek-8B mean -62.88% (low), -47.67% (high); range 43-79% | Fu 2025 (a18, c11, d08) | single-source |
| DeepConf consensus threshold | tau 0.95: saves 15.4% / 52.8% (low) at B=32 / 512, 22.0% / 54.7% (high), accuracy unchanged; tau 0.90, 0.85: up to 69.6%, accuracy drops (-0.26pp at 0.90 low) | Fu 2025 (b16, c12) | single-source |
| RASC | about 70% fewer samples (60-80%), about 80% less time; ablation: answer-only 10.86 gens / 55.5; reasoning-only 5.50 / 50.4; combined 8.20 / 55.8 | Wan 2025 (a15, b14, c07) | single-source, not re-opened |
| Self-calibration | confidence-weighted SC saves 39.8 / 50.4 / 94.2% of samples at matched accuracy (plotted); MathQA 81.0 to 83.6 at 16 responses | Huang 2025 (b17, c14) | single-source, not re-opened |
| Path-Consistency | speedup math 28.7%, commonsense 20.9%, symbolic 20.3%; up to 48.3%; accuracy up to +3.8 (SVAMP) | Zhu 2025 (c13) | single-source, not re-opened |
| Stop inside one chain | final answer reached after about 60% of steps; trial-answer exit cuts CoT 19.1-80.1% with accuracy +0.3 to +5.0 (11 models, 10 benchmarks); answer-consistency cuts over 40% tokens on NQ; Learn-to-Stop up to 48% (QwQ-32B) | Yang 2025 DEER; Liu 2025 (c15, c16) | single-source each, not re-opened |
| Pandora's-box stopping | same quality as best-of-N with 15-35% fewer generations; saving grows with quality target; needs a reward model | Kalayci 2025 (c17) | single-source |
| Compute-optimal allocation | beats best-of-N with about 4x less test-time compute | Snell 2024 (b20) | single-source |
| Certified Self-Consistency | budget 10: about 9.7 samples at alpha 0.1, 9.4 at 0.4; budget 50: 39 / 38; budget 100: 75 / 67; accuracy equal to full vote | Cordero-Encinar 2025 (d04) | single-source |
| Shared errors across models | Helm, 71 LLMs, 14,042 questions: pairs agree about 60% when both wrong (chance 1/3); 349 LLMs on 12,032 questions; more accurate models more correlated | Kim 2025 (d12) | single-source |
| Agreement for free-form text | USC: TruthfulQA PaLM 2-L 62.1 to 67.7; gpt-3.5 79.8 to 82.5; GovReport ROUGE-1 38.8 to 40.2; no gain on SummScreen after 5 samples; no stop rule | Chen 2023 (d13) | single-source |
| Agent runs disagree | best gpt-4o agent under 50% pass^1; pass^8 below 25% (retail) | Yao 2024 tau-bench (d14) | single-source |
| Debate SPRT, GSM8K | 1.01 rounds, 4.06 calls, 97.0% vs fixed-5 99.0% at 15 calls; but a 3-call single-round vote also scored 99.0% | Morandi 2026 (a21, b12, d18) | contested |
| Debate SPRT, MMLU | cap 8 hit on 99.5% of items; 31.96 calls (2.1x fixed-5); accuracy 94.2 vs 93.8; 3-call vote 94.4; calibrated KL about 0 | Morandi 2026 (b13, d18) | contested |
| Debate stability stop (KS) | KS < 0.05 on judge-correctness distribution; stops in 2-8 of 10 rounds; accuracy change -1.03 to 0.0 | Hu 2025 (d17) | single-source |
| SPRT under correlation (simulation) | nominal 0.05 gives 0.015 at rho 0, 0.044 at 0.41, 0.065 at 0.6 (AR(1), 50,000 runs) | via d18 | single-source |

## 4. Mechanisms and models

### 4.1 Classical SPRT (the template)
Inputs: hypotheses H0, H1; type-I error alpha; type-II error beta.
1. Set log-bounds: upper b = ln((1-beta)/alpha), lower a = ln(beta/(1-alpha)).
2. Keep S = 0.
3. After each observation x: S += ln(f1(x) / f0(x)).
4. If S >= b: stop, accept H1. If S <= a: stop, accept H0. Else draw again.
5. Add a hard cap. Wald's SPRT is open-ended; real use is truncated.

For Bernoulli data with success rate p0 under H0 and p1 under H1: a success adds ln(p1/p0); a failure adds ln((1-p1)/(1-p0)). The ConSol worked example uses ratios 1.2 and 0.8 (p1 = 0.6) (d05). When p1 is close to p0 each step is tiny, so many samples are needed to cross a bound.

### 4.2 SPRT on LLM votes (ConSol)
- Count the two most frequent answers, n1 and n2. Each new sample that matches one of them is a Bernoulli outcome "answer 1 vs answer 2", p = p1/(p1+p2).
- H0: p = 0.5 (no leader). H1: p > 0.5 (a leader exists). Update S after each sample.
- ConSol sets p1 = 0.5001 and alpha near 0.95 (a20, d05). This is far from the textbook. A bound is crossed fast, so the test acts as a quick "is there a leader" gate, not a controlled hypothesis test. The nominal Wald error guarantee does not hold.
- Mixture version (mSPRT): put a prior on p over (0.5, 1], here truncated Beta(1e6, 1e6). Average the likelihood ratio over the prior. This gives an always-valid test (a19, c09).
- Draw 2-3 samples in parallel per turn to cut latency (a20, c09). It costs some saving.
- Cap 40 samples.

### 4.3 Posterior-lead stop (Adaptive-Consistency)
- Model the top two answer counts as Beta(1 + n1, 1 + n2) (prior Beta(1,1)).
- Stop when P(p1 > p2 | counts) >= threshold (default 0.95, hand-set, swept 0.5-1.0) (a12, d19).
- Check cost: 0.03 ms for Beta (d19). Dirichlet and CRP are no better and about 3000x slower.
- No type-I control under peeking (ConSol's critique, b09). It replicated at moderate budgets (d01, d02) and was fragile at high ones (d16).

### 4.4 Window stop (ESC)
- Sample in windows of size w (5; 8 for MATH). Stop at the first window in which all w answers are identical. Cap L (40 or 64) (a14).
- Why it is a test: a unanimous window is a null-hypothesis event. A z-statistic from the first window picks w and L for a target accuracy-cost balance (c05).
- Simple. No prior. Savings follow the share of items where the model is unanimous.

### 4.5 Difficulty-first routing (DSC)
- Rank items by difficulty (the model ranks a batch). Give easy items one CoT sample. Pre-allocate more samples to hard ones (a16).
- Counts input tokens too, which sequential stopping repeats on each re-sample.
- Needs the probe to be right. Spearman with human labels is 0.62 / 0.44 (d15).

### 4.6 Confidence-weighted and token-confidence stops
- CISC: weight each vote by the model's confidence in that path (P(True) prompt works best). The stop moves earlier because fewer votes give a clear leader (a17, d09).
- DeepConf: compute group confidence over a sliding window of token log-probs. After a 16-trace warm-up, set a threshold; stop any trace whose confidence falls under it. Stop the whole job once the top answer's vote share passes tau (default 0.95) (a18, c11, c12). Needs per-token log-probs inside the engine. Hosted APIs that hide them cannot run it (K28).
- Verbalised 0-100 confidence recovers about two thirds of the P(True) saving (30% vs 46% at budget 10) (d09).

### 4.7 Certified (anytime-valid) majority
- Martingale Majority Certificate (d04): an e-value test of whether the empirical leader is the model's true mode. Valid under optional stopping. Assumes rollouts are conditionally independent given the prompt.
- Conservative: about 9.7 of 10, about 39 of 50, about 75 of 100 samples used (d04). Saves 3-25%.

### 4.8 Early exit inside one chain
- At transition words, prompt the model for a trial answer. Stop thinking if the trial answer's confidence is high (DEER, c15). Or stop when the answer is the same across successive prefixes (c16).

### 4.9 Optimal-stopping view
- Each new sample costs c and returns a random reward. Weitzman's Pandora's-box rule gives an optimal threshold. A UCB variant learns it online (c17). Needs a reward model or verifier.

### 4.10 Debate stops
- SPRT on a judge score (Morandi): needs score distributions under "useful convergence" and "not yet" with large KL. Check calibrated KL on 40+ labelled items first (d18).
- KS stability (Hu): fit judge-correctness counts per round as a Beta-Binomial mixture; stop when the distance between rounds drops under 0.05 (d17).
- Schema G9 already says no debate. This is evidence about what a score-based stop rule needs, not a plan to add debate.

### 4.11 Choosing a threshold (no label-free recipe exists)
- Textbook p1 0.55-0.6: too slow for many-answer problems (a20).
- ConSol p1 = 0.5001, alpha about 0.95: fast, but not a controlled test.
- Mixture SPRT with a wide prior: robust to two orders of variance misspecification (a27).
- AC threshold 0.95: hand-set (d19).
- CGES tuned its threshold on test data (critique). Treat that as a caution on all reported thresholds.
- Practical recipe (K26): fit the threshold on a small labelled pilot, report accuracy vs threshold on a grid, pick the knee.

## 5. What holds up

**Replicated.**
- Stop-on-stable-leader saves samples at tiny accuracy cost. Aggarwal and Li reported it. The independent CGES group re-ran ESC, AC and DSC (10 seeds, 7B models, 5 benchmarks) and found ESC and AC used about 8.6-9.1 of 16 calls within 0.4pp (d01, K23).
- Saving grows with model strength and shrinks for diffuse models: Vicuna 1.9x vs GPT-3.5 4.4x; Llama-2-7b used 62.48 of 64 samples on MATH (b04, b07, K09).
- Peeking inflates false positives (Johari fivefold at 10,000 samples; Armitage from memory) (K03).
- Anytime-valid methods tolerate prior misspecification by two orders of magnitude (a27, K04).
- Voting plateaus and a verifier is needed to go further (Brown) (K15, K31).

**Failures and fragility.**
- Small fixed budgets leave little room. B=4: AC saved 0 calls and lost 0.5pp. B=8: about 1-3.5 calls saved. DSC lost about 2.7pp on average at B=4 (d02, K24). Most headline savings are against a 40-sample ceiling, which is generous (critique).
- AC fell below fixed allocation at budget 128 (2.13x vs 3.40x) and did not reach SC@128 for Llama-3.2-3B on GSM8K (d16, K27). The metric there is reducible error vs the model's limiting mode.
- When the confidence signal is uninformative (GPQA, 7B model) the posterior never concentrates, the stop does not fire, and accuracy is 46-48 vs 50.0 for SC (d03).
- Debate SPRT: on MMLU it hit the cap on 99.5% of items and cost 2.1x the fixed-5 baseline, because KL was about 0 (d18). On GSM8K the headline "3.7x fewer calls" is true, but the paper says no pairwise accuracy difference is significant (CI about 4.4 points), and a 3-call single-round vote already scored 99.0% (K21, critique).
- ConSol results rest on non-textbook parameters (p1 = 0.5001, alpha about 0.95) and an mSPRT alpha sweep of 0.00018. The authors say results are sensitive and only short-answer tasks were tested (b11, d05). No independent test of the SPRT variant exists (K23). Its own table shows SPRT below SC on some cells (GPQA low 66.7 vs 68.2).
- Inverse-U (more votes hurt) was shown on GPT-3.5-turbo-0125 only, with synthetic optima at 1-7 calls (d06). Recent reasoning models show rise-then-flat in three papers, but nobody split by difficulty (d07, K14).
- ESC saves 33.8% on MATH while AC saves 3.3x on MATH. Models, caps and windows differ, so these are not comparable (critique).

**Moderators.**
- Model strength (stronger saves more).
- Task difficulty and answer-space size (Coin Flip -84.2%, MATH -33.8%).
- Budget cap (savings grow with the cap; small caps leave no room).
- Threshold (tau 0.95 safe; 0.90 and 0.85 lose accuracy in DeepConf).
- Cost unit (samples, tokens, calls, wall time: no paper reports all four).
- Confidence signal quality (P(True) > response probability about equal to verbal 0-100 > verbal binary; best-calibrated was least useful).
- Error correlation (below).

**What worked.**
- Beta posterior on top-two counts (cheap and good).
- Unanimous-window stop (simplest).
- Confidence-weighted votes (CISC).
- Difficulty-first routing on easy-heavy sets (DSC), with a noisy probe.
- Stop on a passing test where tests exist (Brown).
- Mixture SPRT with a wide prior (Johari).

**What did not work or is unsupported.**
- Dirichlet and CRP posteriors: no gain over Beta, about 3000x slower (b05, d19).
- Random stopping: worst (c03).
- Aggressive consensus thresholds (0.90, 0.85): savings up to 69.6% but accuracy drops (c12).
- Rigorous certified stops: valid but save only 3-25% (d04).
- SPRT on a judge score that does not separate the two cases (Morandi MMLU).

**The unmeasured failure: confidently wrong consensus.** Agreement certifies the model's mode, not the truth (d04). Across models, errors are shared: about 60% same wrong answer when both are wrong (d12). Same-model samples are probably more tied (inference). DeepConf notes confident wrong traces (b27). No paper measures the false-stop rate of single-model samples with a seeded common wrong answer. SPRT error rates degrade gracefully with correlation in simulation (0.065 vs nominal 0.05 at rho 0.6, d18), but proofs for dependent streams were not opened (d20, d21, K33).

**Source-quality caveats** (critique): nearly all LLM stop-rule evidence comes from a few groups (Aggarwal, Li, Lee), on short-answer math and multiple choice, mostly preprints. Wald 1945, Wald-Wolfowitz 1948, Armitage, Pocock and Bassler were never opened.

## 6. Language models

**Baseline.** Self-consistency, 40 samples, majority vote: +17.9 GSM8K, +11.0 SVAMP, +12.2 AQuA over greedy CoT on PaLM-540B (a11). Unweighted majority did as well as probability-weighted.

**Stop rules, saving and accuracy.**

| Rule | Saving | Accuracy change | Notes |
|---|---|---|---|
| Adaptive-Consistency (Beta, 0.95) | 2.4x-7.9x samples; 3.3x on math; GPT-3.5 4.4x | under 0.1 pt mean | 0 saved at B=4; fragile at B=128 |
| ESC (window 5/8) | 34-84% of samples | within about 1 pt | MATH: 62.48 of 64 on Llama-2-7b |
| ConSol SPRT | 63.9-88.7% of tokens | AIME24 low 70.0 to 80.0; GPQA low 68.2 to 66.7 | one group; tuned; short answers |
| DSC | 56-65% of cost vs SC; 22-25% vs ESC | small loss | probe Spearman 0.44-0.62 |
| CISC | over 40% of paths | up | P(True) best; verbal 0-100 gives 30% vs 46% |
| DeepConf | up to 84.7% tokens; 62.88% / 47.67% mean (DeepSeek-8B) | 99.9 vs 97.0 majority (AIME25) | needs log-probs |
| RASC | about 70% samples | maintained | not re-opened |
| DEER / answer convergence | 19-80% of CoT length | +0.3 to +5.0 | single chain; not re-opened |
| Pandora UCB | 15-35% generations | same quality | needs reward model |
| Certified SC | 3-25% | same as full vote | valid guarantee, conservative |

**Pattern.** Savings come mainly from items where the model already agrees (K12, K22). CoT and 40-sample SC agree on 84.8% (GPT-3.5) and 96.2% (GPT-4) of GSM8K items. Part of the gain is reallocation to hard items: at equal average cost adaptive beats fixed n by about 3 points (K08).

**Frontier and reasoning models.** o3-mini, gpt-oss-120b, DeepSeek-8B and Qwen3 appear in ConSol and DeepConf. Entropy of the answer distribution falls with model strength (b10). Accuracy rises then flattens with more votes (d07). No decline seen, but no difficulty split.

**Weak models.** 7B reasoning models gave little room at B=4 and B=8 and an uninformative confidence signal on GPQA (d02, d03).

**Free-form and agents.** USC lets the model pick the most consistent candidate: TruthfulQA 62.1 to 67.7 (PaLM 2-L), 79.8 to 82.5 (gpt-3.5) (d13). No vote share, no stop rule. For agents, tau-bench's "same final state" is the usable agreement measure; pass^8 is under 25% (d14). No stop evidence.

**Debate.** The SPRT stop works only with a separating score; MMLU failed (d18). The KS stop saved rounds at up to -1.03 points (d17). Schema G9 already excludes debate.

**Verifier-based stop.** When tests exist, coverage keeps rising (98.44% at 10,000 samples) while voting stalls near 41% (Llama-3-8B MATH) (d10). Tests themselves fail (11.3% flaky; 35 of 122) (d11).

## 7. What our agent should take

Key: G = guardrail, S = state, O = operator, memory = class record or lessons. [E] established, [S] single-source, [C] contested.

### Add now (established)

| # | Item | Part | Status | Evidence |
|---|---|---|---|---|
| A1 | Use a pre-set stop rule on vote counts. Never stop "when it looks agreed" by ad hoc inspection. Log the rule, threshold and cap with every run. | G (stop rule) | [E] | K03, K01; b21, a07 |
| A2 | When the program draws several attempts, stop when the leader is stable (Beta posterior on top-two counts, or a unanimous window) and spend the saved budget on hard items. Treat this as a budget saver, not a truth test. | G12, O (vote) | [E] | K07, K08; a12, b02-b05, a14, b06-b08, d01 |
| A3 | Give every stop a hard cap. Report average calls and tokens as well as accuracy. Compare at equal average tokens. | G7, G12 | [E] | K08, K24; b05, d02 |
| A4 | Expect small savings on weak models, hard items and small caps. Do not bother with adaptive stop when the cap is 4 or less. | G (budget) | [E] for weak models and hard items; [S] for the cap-4 rule | K09; b04, b07, d02 |
| A5 | When a check exists (tests, held-out example, mutation), stop on the first pass of that check, not on agreement. Keep a second check because checks are imperfect. | G3, G4, S (verify) | [E] that agreement plateaus; [S] for the numbers | K15, K31; b19, d10, d11 |
| A6 | An agreement stop never lifts an item above unverified status (restates G4). | G4 | [E] | K22, K25; d04, d12 |
| A7 | If a likelihood-ratio rule is used, use a mixture or wide-prior version, not a narrow single p1. | G (stop rule) | [E] for mixture robustness | K04; a07, a27 |

### Test first (not established; each has a row in UNKNOWNS.md)

| # | Item | Part | Status | Evidence |
|---|---|---|---|---|
| T1 | SPRT on top-two counts vs Beta posterior vs unanimous window, at equal tokens, own p0/p1 and alpha | G stop rule | [S] | K10, K11, K26, K27; a19, b26, d05, d16 |
| T2 | Threshold sensitivity grid of p1 and alpha | G | [S] | K26; d05, d19 |
| T3 | Stop vs small fixed budgets (5 and 8) | G budget | [S] | K24; d02 |
| T4 | False-stop rate with a seeded common wrong answer | G4 | [C] | K22, K25; d04, d12 |
| T5 | One sample first on easy items, escalate on disagreement | S0 gate | [S] | K12, K30; a16, d15 |
| T6 | Accuracy vs N by difficulty bucket (to set the cap) | G cap | [S] | K14; b18, d06, d07 |
| T7 | Confidence-weighted vote (verbalised 0-100) | O vote | [S] | K16, K28; a17, d09 |
| T8 | Token-confidence early stop, if log-probs are reachable | G | [S] | K17; a18, d08 |
| T9 | No-consensus stop (leader share under 0.5: switch operator, do not draw more) | G1, S6 | [S] | K13; b10 |
| T10 | Pairwise "same outcome" judge as agreement for free-form and agent items | G agreement | [S] | K29; d13, d14 |
| T11 | Verify-stop vs agree-stop on tasks with tests | S verify | [S] | K31; d10, d11 |
| T12 | Early exit inside one chain (trial-answer probe) | G11 | [S] | K19; c15, c16 |
| T13 | Class-record memory of how often an early stop was right, per problem class | memory | [S] (design only) | K22, K30 |
| T14 | Judge-score SPRT for any iterative refinement, only after a KL pre-flight check. Low priority; G9 forbids debate | G | [C] | K21, K32; a21, d17, d18 |

## 8. Concrete tests on our bench

All arms get equal average tokens (count setup, probe and every re-sample). Report accuracy, average calls, average tokens and false-stop rate with at least 3 seeds and confidence intervals.

| Test | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| B1 Stop-rule head to head | short-answer items (exact answer), 100+ | fixed-5; fixed-8; fixed-40; unanimous window (w=3, 5); Beta 0.95; SPRT (own p1 grid); mSPRT | accuracy at matched mean tokens | Adaptive saves 30-50% of tokens vs fixed-40 at under 1 pt loss; against fixed-5 or 8 it saves little (0-40%) |
| B2 Threshold grid | same | Beta threshold 0.8-0.99; SPRT p1 in {0.5001, 0.55, 0.6}, alpha 0.5-0.99 | accuracy vs mean-tokens curve | A knee exists. p1 0.5001 is faster and probably slightly less accurate than 0.6. Tests ConSol's tuning |
| B3 Seeded wrong consensus | items with a planted common wrong answer plus matched controls | each stop rule; each plus an independent check | false-stop rate (stopped and wrong), cost | Agreement stops show false-stop above 0 at high vote share; an independent check cuts it. Size unknown |
| B4 Small budget | as B1 with cap 4 and 8 | fixed vs adaptive | accuracy, tokens | Near-zero saving at cap 4 (matches CGES) |
| B5 Difficulty gate | mixed easy and hard items | one sample then escalate on disagreement; no gate; adaptive only | accuracy at matched tokens; miss rate on items where sample 1 differs from the vote | Saves 20-60% on easy-heavy sets; miss rate unknown (not published) |
| B6 N by difficulty | items bucketed by single-sample pass rate | accuracy at N = 1, 3, 5, 8, 16, 32 per bucket | curve shape per bucket | Rise then flat; check for a fall on the hard bucket |
| B7 Confidence weighting | short-answer items | plain vote; verbalised 0-100 weighted vote | accuracy at 3, 5, 8, 10 samples | About 30% fewer samples to match at budget 10 |
| B8 Verify vs agree | code or test items | first-pass-test stop; agreement stop; both | accuracy, false-accept | Verify-stop wins; agreement adds little on top |
| B9 Free-form agreement | open items and agent items | pairwise same-outcome judge vs exact match | judge-human agreement on 50 pairs | Above 0.8: build a vote-share stop. Else keep fixed N |
| B10 Peeking | any | pre-set rule vs ad hoc "stop when it looks agreed" | false-accept rate on known-wrong items | Ad hoc rule has a higher false-accept rate; size unknown for LLM voters |

## 9. What does not transfer, and why

- **Wald's error guarantees.** They assume independent, identically distributed observations from a known pair of distributions. LLM samples from one model are not independent (G4). The "two hypotheses" are a modelling trick on top-two counts. ConSol's own parameters void the guarantee on purpose (d05). Use SPRT as a heuristic stop rule, not a certificate.
- **"Half the samples."** Memory only. The Wald-Wolfowitz proof is for i.i.d. data and simple hypotheses. Not verified for vote streams (d20, d21).
- **Clinical-trial boundaries (Pocock, O'Brien-Fleming).** They control one decision about a fixed effect over planned looks. Our agent decides per item, thousands of times. A calibrated cap and a cheap check matter more. Bassler's overstatement from early stopping has an LLM analogue only if we estimate accuracy from stopped runs; report accuracy from full-budget calibration sets.
- **A/B-testing run-length gains (20-40%).** They come from a different noise model.
- **Savings measured against 40 samples.** Our default is small (G11). Against 5 or 8 samples the saving is about 0-40%, and 0 at 4 (d02).
- **Math and multiple choice to open-ended and agent tasks.** "Same answer" is undefined there. USC gives a pick, not a share. tau-bench shows runs disagree (d14).
- **DeepConf.** Needs engine-level log-probs. Not available through hosted APIs that hide them (K28, inference).
- **Debate stops.** G9 excludes debate. Morandi's result is contested.
- **Pandora's box.** Needs a reward model. Our reward signals are code checks.
- **Human sequential-sampling models (drift diffusion).** A different subfield. Not an LLM decision rule.

## 10. Open questions

1. Does the agreement stop hold at equal tokens against fixed budgets of 5 or 8 for our model and tasks? (CGES: calls, not tokens.)
2. What is the false-stop rate when samples share a common wrong answer? Nobody measured it for single-model samples.
3. How do we set the threshold without labels? No recipe exists (K26).
4. Does SPRT beat the posterior-lead rule when an independent group runs it with a wide sweep and several seeds? No replication exists.
5. Is the inverse-U real for frontier reasoning models, and where does it peak per difficulty bucket? (Working cap 8-16.)
6. What is the miss rate of a one-sample difficulty probe on items where one sample and the vote disagree?
7. What replaces vote share for free-form and agent tasks, and does a stop rule on it work?
8. What do Wald and Wald-Wolfowitz prove for dependent, non-i.i.d. vote streams? Does optimality survive?
9. What does agreement add on top of passing tests?
10. Which cost unit matters: samples, tokens, calls or wall time? No paper reports all four.
11. Can verbalised confidence match token-confidence stopping through a hosted API?
12. Which signal separates useful from useless convergence in iterative refinement?

## 11. Sources

[V] = opened and read by the research agents (critique.md lists which numbers were re-opened). [M] = snippet or memory only.

**Classical and statistical**
- [M] Wald (1945) Sequential tests of statistical hypotheses. https://projecteuclid.org/euclid.aoms/1177731118
- [M] Wald and Wolfowitz (1948) Optimum character of the SPRT. https://projecteuclid.org/euclid.aoms/1177730197
- [V] Wikipedia: Sequential probability ratio test. https://en.wikipedia.org/wiki/Sequential_probability_ratio_test
- [V] Wikipedia: Sequential analysis. https://en.wikipedia.org/wiki/Sequential_analysis
- [V] Stefan, Schoenbrodt, Evans, Wagenmakers (2022) Efficiency in sequential testing. https://pmc.ncbi.nlm.nih.gov/articles/PMC9729330/
- [M] Stefan and Schoenbrodt (2023) on peeking, via ConSol. https://arxiv.org/abs/2503.17587
- [V] Johari, Pekelis, Walsh (2019) Always valid inference. https://arxiv.org/abs/1512.04922
- [V] Howard, Ramdas, McAuliffe, Sekhon (2021) Time-uniform confidence sequences. https://arxiv.org/abs/1810.08240
- [V] Ramdas, Grunwald, Vovk, Shafer (2023) Game-theoretic statistics and safe anytime-valid inference. https://arxiv.org/abs/2210.01948
- [V] Grunwald, de Heide, Koolen (2023) Safe testing. https://arxiv.org/abs/1906.07801
- [M] Robbins (1970); Ville (1939), via Howard and Ramdas. https://arxiv.org/abs/1810.08240
- [M] Armitage, McPherson, Rowe (1969) Repeated significance tests. https://doi.org/10.2307/2343787
- [M] Pocock (1977); Bassler et al. (2010). https://doi.org/10.1001/jama.2010.1241
- [M] Lai (1998) and related work on dependent data (pointer from memory, no URL)

**LLM stop rules and voting**
- [V] Wang et al. (2023) Self-consistency. https://arxiv.org/abs/2203.11171
- [V] Aggarwal et al. (2023) Adaptive-Consistency. https://arxiv.org/abs/2305.11860
- [V] Li et al. (2024) Early-Stopping Self-Consistency. https://arxiv.org/abs/2401.10480
- [V] Lee et al. (2025) ConSol. https://arxiv.org/abs/2503.17587
- [V] Wang et al. (2025) Difficulty-Adaptive Self-Consistency. https://arxiv.org/abs/2408.13457
- [V] Taubenfeld et al. (2025) CISC. https://arxiv.org/abs/2502.06233
- [V] Fu et al. (2025) DeepConf. https://arxiv.org/abs/2508.15260
- [V] Wan et al. (2025) RASC. https://arxiv.org/abs/2408.17017 (not re-opened)
- [V] Huang et al. (2025) Self-calibration. https://arxiv.org/abs/2503.00031 (not re-opened)
- [V] Zhu et al. (2025) Path-Consistency. https://arxiv.org/abs/2409.01281 (not re-opened)
- [V] Yang et al. (2025) DEER. https://arxiv.org/abs/2504.15895 (not re-opened)
- [V] Liu and Wang (2025) Answer convergence. https://arxiv.org/abs/2506.02536 (not re-opened)
- [V] Kalayci and Raman (2025) Optimal stopping vs best-of-N. https://arxiv.org/abs/2510.01394 (not re-opened)
- [V] Chen et al. (2024) Are more LM calls all you need? https://arxiv.org/abs/2403.02419
- [V] Brown et al. (2024) Large Language Monkeys. https://arxiv.org/abs/2407.21787
- [V] Snell et al. (2024) Scaling LLM test-time compute. https://arxiv.org/abs/2408.03314
- [V] Aghazadeh et al. (2026) CGES. https://arxiv.org/abs/2511.02603
- [V] Cordero-Encinar and Duncan (2025) Certified self-consistency. https://arxiv.org/abs/2510.17472
- [V] Feng et al. (2026) Optimal self-consistency (Blend-ASC). https://arxiv.org/abs/2511.12309
- [V] Kim, Garg, Peng, Garg (2025) Correlated errors in LLMs. https://arxiv.org/abs/2506.07962
- [V] Chen, Aksitov et al. (2023) Universal self-consistency. https://arxiv.org/abs/2311.17311
- [V] Yao, Shinn, Razavi, Narasimhan (2024) tau-bench. https://arxiv.org/abs/2406.12045
- [V] Hu et al. (2025) Multi-agent debate for LLM judges with adaptive stability detection. https://arxiv.org/abs/2510.12697
- [V] Morandi (2026) Sequential consensus for multi-agent LLM debates. https://arxiv.org/abs/2605.19193

## Source audit (2026-11-01)

Fresh auditors re-opened the sources of 6 established claims: 5 confirmed as written, 1 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **C12.04-K04** (number corrected). Johari et al. (Section 5.6.1) report under 5% power loss and at most 10% run-length cost for misspecification of about ONE order of magnitude; at two orders the cost is up to 20% power and 40% run-length. Corrected claim: Anytime-valid methods (mixture SPRT, confidence sequences, e-values) keep error guarantees under optional stopping. Mixture variance can be misspecified by about one order of magnitude with under 5% average power loss and at most 10% run-length increase; missing by two orders can cost up to 20% power and 40% run-length (Johari et al., Section 5.6.1).
- **C12.04-K03** (now single-source: only one opened source, code check).
- **C12.04-K06** (now single-source: only one opened source, code check).
