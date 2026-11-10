# Aggregation and extremizing: deep document

*Subfield E03.06. Written from evidence_a-d.jsonl (a01-a30, b01-b25, c01-c30, d01-d21), claims.jsonl (K01-K27) and critique.md. One correction applies throughout: in Satopaa and Ungar (2015) the real-data extremized loss is 133.23; 155.69 is the plain mean (b01 has this wrong, a11 is right).*

## 1. What it is

Aggregation is the step that turns several probability forecasts of one event into one forecast. Extremizing is a post-step: push the pooled probability away from the base rate (usually 0.5) so it is more confident.

Three questions sit inside it.
- **Pool.** Which average: arithmetic mean, median, trimmed mean, geometric mean, mean of log-odds (logit), probit average.
- **Weight.** Equal weights, skill weights, or weights learned from past scores.
- **Push.** After pooling, multiply the log-odds by a factor a > 1 (or fit a slope and intercept). Equivalent forms: p^a / (p^a + (1-p)^a), Platt scaling on the pooled value.

Why it matters for our agent. Schema rule G4 says: samples from one model are not independent, so no extremizing votes. This subfield tests whether that rule holds, and where it is too strict or too loose. The evidence says extremizing is justified by information diversity, not by confidence. Resampling one model gives noisy copies of one information set. That is the case where the mean is right and a big push is wrong. But one team (AIA) found a fixed push of sqrt(3) gave -5.6% Brier on a 10-sample same-model ensemble. So G4 should read "no blind push; fit and cap a push on held-out data", not "never push". That change is [C] contested and needs the tests in section 8.

Scope. Probability forecasts of resolvable events. Voting on single-answer tasks (self-consistency) is related but is not probability pooling; it appears in section 6 only where it bears on correlation. Calibration and overconfidence, Belief updating, Epistemic diversity, Conformity and Debiasing are other subfields in this run; only links are noted here.

## 2. History and theories in depth

### 2.1 Early view: forecasts as noisy copies of one truth
The older measurement-error model treats each forecast as the truth plus independent noise. Then the average is the best pool, and a push is an ad hoc fix. Satopaa, Pemantle, Ungar (2015) call this model at odds with real forecasting [a02]. Earlier uses of a push: Karmarkar 1978, Erev et al. 1994, Shlomi and Wallsten 2010, Hora 2004, Ranjan and Gneiting 2010 (beta-transformed linear pool) [a02, a18; second-hand].

### 2.2 Baron et al. 2014: two reasons for a push
Opened in full [d01, d02]. Data: Good Judgment Project (GJP) year-1 two-option questions (80; 86 in a leave-one-out note). Aggregates were mean and median of daily forecasts (decay 0.6). Fitted exponent a in p^a/(p^a+(1-p)^a):

| Group | Aggregate | a | Brier untransformed | Brier extremized | Change |
|---|---|---|---|---|---|
| High expertise | mean | 2.43 (SE 0.05) | 0.187 | 0.148 | -21% |
| High expertise | median | 1.78 | 0.176 | 0.160 | -9% |
| Low expertise | mean | 3.08 | 0.196 | 0.139 | -29% |
| Low expertise | median | 2.34 | 0.184 | 0.153 | -17% |

Reason 1, error asymmetry: on a bounded scale, symmetric noise pulls the mean toward 0.5. The median is immune. Reason 2, regression: forecasters shrink their own log-odds by a factor c because they know they miss information. Pooling collects the missing information, so a = 1/c undoes the shrinkage. For the median the optimal a equals 1/c exactly in simulation; fit error under 0.005 on the probability scale. Extremizing the median still helped in the data, which is what forced reason 2. The mean-median gap hints at how much noise there is.

Limits: in-sample, one parameter fitted on the same questions, called illustrative by the authors. Per-question optimal a ranged from negative (surprising outcomes) to very large, so one a is a compromise. Authors cannot know whether forecasters regress optimally. Transform-then-average did worse, partly because it extremizes judgments on the wrong side of 0.5.

### 2.3 The partial-information framework (Satopaa, Pemantle, Ungar 2015)
Each forecaster reports E(event | own information), so each is calibrated [a01]. Forecasts differ only because information differs. The aggregator sees only the forecasts. Results [a03-a05]:
- Complete overlap: all forecasts identical, no push needed.
- Zero overlap: the optimum is a weighted vote (range voting) divided by a term that extremizes by total group information.
- In between the optimum moves smoothly. Push grows with total group information and with diversity, and falls with overlap. Worked example 3.1: optimal 2/3 with high overlap, 4/5 with low overlap.
- Proposition 4.2: the ratio of optimal to average is Cauchy; P(ratio > 1) > 1/2. A push is more likely than not to help, never certain on one question.

Neyman (2024) gives the cleanest toy [b07]: two experts both say 2/3. If they saw the same coin flip, the answer is 2/3. If they saw different independent flips, it is 3/4. Averaging is right in the first case and timid in the second.

### 2.4 Real-valued version (Satopaa and Ungar 2015)
Any weighted average is marginally consistent but not reliable and does not expand variance [a08]. Extremizing is redefined as a shift away from the marginal mean (a pivot mu0), not toward 0 or 1. Counter-example: rain on 20% of days, mean forecast 0.30; the right move is up, away from base rate 0.20 [a09]. So a push needs a base rate. It is most likely to help when the best single forecaster knows much less than the group in total [a10]. Satopaa (2018): any aggregator strictly between min and max (mean, median, trimmed mean, midrange) is inefficient when forecasters hold different information [b05]; this fails if they are noisy copies of one signal.

### 2.5 Worst-case view (Neyman and Roughgarden)
Under "substitutable signals" averaging beats a random expert. With a known prior, extremizing the average by a constant factor gives a better guarantee. The safe factor grows with the number k of experts but tops out near sqrt(3) = 1.732; no fixed factor is best on both fully correlated and fully independent signals [b06, c18]. Each proper scoring rule has a matching pool: quadratic with linear, log with geometric [a19]. Weather example: models say 0.1% and 20%; linear pool 10%, log pool about 1.6%.

### 2.6 Bayesian ensembles and anti-extremizing (Lichtendahl et al. 2018/2022)
The mean double-counts the prior. Extremizing is right if experts use private information. If experts share information the aggregator lacks, the optimal ensemble can anti-extremize [a13]. Extremizing should be defined as moving away from the base rate, not 0.5 [d09]. The published abstract reports anti-extremizing in 18% to 73% of cases across public datasets [d09; abstract only].

### 2.7 BIN model (Satopaa, Salikhov, Tetlock, Mellers)
Splits aggregator gains into bias, information and noise on GJP [d05-d07]. Plain averaging helps almost entirely by cutting noise; it does not fix the pull toward 0.5, and the probability mean can add bias at long horizons. Probit averaging removes most of that bias with no tuning parameter. Where forecasters share information (teams, superforecasters), disagreement is mostly noise, so fancy aggregators gain little or overfit.

### 2.8 Time-series calibration (Satopaa et al. 2014)
Models that calibrate the aggregate beat smoothing-only and exponentially weighted averages on IARPA data [b04]. The sharpest variant (BSACLOG) is overconfident and wins only on short easy questions.

### 2.9 Not read
Mellers et al. 2014, Satopaa et al. 2014 (IJF logit model), Ranjan and Gneiting 2010, Palley and Soll 2019 and Sevilla 2021 were not opened (a17, a18, b20, b23, b24, d19, d20). Mellers et al. 2015 was opened and has no extremizing analysis [d21]. Treat anything about these as second-hand.

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Mean of different-information calibrated forecasts is under-confident; optimal push grows with group info, falls with overlap | Example 2/3 (high overlap) vs 4/5 (low overlap); P(push helps) > 1/2 | a01, a04, a05 | [E] theory, 3 sources |
| Real-valued data: push helps more with no overlap | Fitted factor 1.6950 (no overlap), 1.4382 (high). Loss no overlap: mean 155.69, weighted 156.32, extremized 133.23, best single 185.74, full-info 110.91. High overlap: mean 177.45, extremized 169.92 | a11 | [S] one dataset, not probabilities |
| Weighted-to-extremized gain | -15% no overlap, -4% high overlap | a11 | [S] |
| Shared information caps recovery | Simulated: group information 0.32, recovered 0.228 (high overlap); full recovery at zero overlap | a12 | [S] simulation |
| GJP supers, 123 events (23 yes), 44 forecasters | Brier mean 0.132, logit 0.128, probit 0.128, overlap-aware extremizer 0.123 (-7%). Reliability 0.026 to 0.020; resolution 0.045 to 0.049 | a06, b03 | [S] small, no significance test |
| GJP year 1, fitted exponent | a = 2.43 / 1.78 (experts mean / median), 3.08 / 2.34 (non-experts). Brier gains 9% to 29% | d01 | [S] in-sample |
| GJP, 462 events, out-of-sample | Mean 0.098; trimmed 0.084; votes 0.080; logit 0.063; extremized mean (b about 3) 0.061 (-38% vs mean); skew-adjusted 0.046. Table mapping read from garbled text | d03 | [S] preprint |
| Partial push beats full push | Mean on correct side of 0.5 in 91% of GJP questions, yet full push lost | d03, d04 | [E] two datasets |
| 500 general-knowledge statements | Mean 0.171, extremized 0.107 (b about 4), skew-adjusted 0.098; extremized beat mean on about 76% of questions; yes bias in the set | d04 | [S] human |
| Averaging helps via noise, not bias; probit pool removes most 0.5 pull | Crowds 5-75, 250 draws, 30-day horizon; adding forecasters gives small gains | d05 | [S] |
| Superforecasters and teams gain little from fancy aggregators | Differences not significant (supplement S3.4.1) | d06, a07, a15 | [E] 3 sources (two second-hand) |
| Worst-case safe factor | Two experts: ratio 0.706 averaging; 0.760 with prior and push. Guarantee about 2.598/k. Factor capped near 1.732 | b06, b07, c18 | [E] theory |
| Time-series, IARPA 166 events, 2300 experts | SACLOG 0.096; BSACLOG 0.097; EWMA 0.111 (worst) | b04 | [S] |
| Anti-extremizing exists | Fannie Mae (N=1,056,724) log loss mean 0.2347, logit 0.2329, ensemble 0.2327, xgboost 0.2337; pushed in 79.6% (pulled in 20.4%). Carvana (N=72,983): 0.2966 / 0.2928 / 0.2925 / 0.2946; pushed in 81.3% | a14, d08 | [S] tabular, tiny gains |
| Choice of numeric pool barely matters for LLMs | Halawi validation: mean 0.1656, median 0.1651, geo 0.1655, trimmed 0.1649, none 0.1676, crowd 0.1600. ForecastBench: median 0.197, trimmed 0.197, geo 0.194, geo-odds 0.194 (2SE 0.024). Lu: o3 median 0.1352 vs mean 0.1362 | a24, a26, b15, c26 | [E] |
| LLM merge worse than numeric | Halawi USC 0.1691 vs none 0.1676. BLF: AIA-style merge worse than mean | a24, d14 | [C] (AIA agentic supervisor helped) |
| AIA same-model sampling | 10 samples: mean 0.1140, trimmed 0.1142, median 0.1138, single 0.1182 (-3.6%); sharp drop 1 to 5, small 5 to 15 | d10, c13 | [S] one system |
| AIA fixed sqrt(3) push | 0.1140 to 0.1076 (-5.6%); log-odds extremization 0.1085; learned LOO 0.1071; OLS 0.1097; isotonic 0.1140. Learned on Halawi set (OOD): Platt 0.1104, OLS 0.1134, none 0.1125. Best fit 2.27 (agent), 1.72 (supers) | c15, d11 | [C] one team |
| Where the push gains | Biggest in bins 0.2-0.4 and 0.6-0.8. A move 0.497 to 0.381 changes Brier by -0.102; 0.995 to 0.999 by 2.4e-5 | d11 | [S] |
| Supervisor agent | Agentic 0.1125, non-agentic 0.1168, best-of-k 0.1191, none 0.1199 (different base from 0.1140) | c14, d12 | [C] |
| BLF replication check | Pro backbone: no resolved Platt gain; Kimi: +0.72 / +1.48 Brier Index (+0.98 / +1.80 hierarchical); LOO chose no shrinkage (q=1) | d14, d15 | [C] preliminary |
| Hsieh ensembles | Agent ensemble 0.169 vs single 0.180, human 0.172; base GPT-4o ensemble 0.218 vs single 0.210 (worse); SD 0.150 vs 0.092 | b13, c12 | [S] |
| Prophet Arena prompt ensembles | GPT-5 0.165 to 0.160; Grok 4 0.186 to 0.177; yes/no counting 0.231-0.267 | c28 | [S] |
| LLM crowd equals human crowd | 12-LLM median 0.20 (SD 0.12) vs 0.25 baseline, t(30)=-2.35, p=0.026; 925 humans 0.19, t(60)=0.19, p=0.850; best single GPT-4 0.15 | a21, b11, c01, c02 | [E] but N=31 |
| Acquiescence (yes) bias | Mean predictions above 50% while under half resolved yes; one raw 99.5% vs median 60% | a22, c03, b16 | [E] 3 sources |
| Human median shown to LLM | GPT-4 0.17 to 0.14; machine-human mean GPT-4 0.13 (t(92)=2.58), Claude 2 0.14 (t(92)=3.53), better than self-update | c04 | [E] |
| Halawi crowd blend | Test: system 0.179, crowd 0.149, blend (4x crowd) 0.146 | a25, b25 | [S] |
| Strong-LLM correlation | Seven LLM versions, football: mean pairwise r 0.943; ensemble gain 0.0047 Brier, not significant (Holm) | d17 | [S] |
| Diversity beats copies | Metaculus Q2 2025, N=113: two frontier models gained at most 0.6 points over best single; adding fine-tuned model 2.7 | d16 | [S] |
| Training beats sampling | GPT-OSS-120B N=965: base single 0.1867, median-5 0.1788; Brier-trained single 0.1655 | d18 | [S] |
| Self-consistency (voting, not pooling) | GSM8K +17.9, SVAMP +11.0, AQuA +12.2, StrategyQA +6.4, ARC-c +3.9 | a30, c20 | [E] |

## 4. Mechanisms and models

### 4.1 Pooling in log-odds
For forecasts p_1..p_K: l_i = ln(p_i/(1-p_i)). Pool L = (1/K) sum l_i. Clip p first: Satopaa used [0.001, 0.999]; Mantic clips the mean to [0.05, 0.95] [d16]. The log-odds mean is the geometric mean of odds. ForecastBench found it slightly best (0.194) and BLF found it robust to one failed trial (one dead trial in five costs 9 points in the arithmetic mean vs 4 in logit at p=0.95) [b10, d14]. The log score matches log pooling; Brier matches linear pooling [a19].

### 4.2 The push
Form: p_final = sigmoid(a * (L - m) + m + b), where m is the log-odds of the base rate. Parameters: slope a (a > 1 pushes), pivot m (base rate; needed, see a09), intercept b (absorbs yes bias; d04 fit intercept and slope together).
- Fixed safe value: a at most sqrt(3), rising with K [b06].
- Fitted value: logistic regression of outcomes on L over held-out resolved questions. Report a with a confidence interval. Apply only if the interval excludes 1 (test K09).
- Allow a below 1 (anti-extremizing). Never hard-code above 1 [K23].
- Cap: partial beats full [d03, d04]. Clip final p to about [0.02, 0.98]. Near 0/1 the gain is mechanically tiny (2.4e-5) and the loss when wrong is large.
- Side check: a push on a forecast on the wrong side of the base rate makes it worse [d11, a09].

### 4.3 Why a push helps humans
- Shrinkage reversal (Baron reason 2): each person damps their log-odds by c; pooling distinct information justifies a = 1/c.
- Error asymmetry (reason 1): the bounded scale pulls the mean to 0.5. Log-odds pooling already fixes most of it [d05].
- Partial information: a grows with the number of independent evidence sets and shrinks with overlap. Overlap can be estimated from the correlation of forecast residuals, or from shared sources.

### 4.4 Why it might help an LLM (AIA hypothesis)
RLHF-induced hedging: forecasts are attenuated toward 0.5 (true 0.85 reported as 0.6; certain events shaved to 0.95) [d13]. A push repairs this attenuation, which has nothing to do with information diversity. It is a bias-correction story, so fit it per backbone. Evidence runs both ways. Halawi found the system naturally calibrated and isotonic/binning did not help [c07]. Lu found Qwen-32B overconfident and Claude narrative prompts under-confident, so the sign depends on model and prompt [b15]. Bench to the Future found a Yes bias in all models tested [b16]. Schoenegger found acquiescence [c03]. One push sign is wrong for some of these.

### 4.5 Estimating the shared-information level
No online detector exists in the sources [K24]. Candidate proxies to build and test: (a) overlap of retrieved documents between samples; (b) pairwise correlation of sample logits across questions; (c) dispersion of the K samples (BLF's dispersion shrinkage was never selected, so weak). Football data show between-model r = 0.943 [d17], so for strong LLMs expect high overlap and a small push.

### 4.4b Pipeline an engineer can build
1. Draw K samples, each in an isolated context (S3). 2. Parse each to a probability, clip. 3. Convert to logits, take the mean. 4. Look up the class record: fitted (a, b) for this backbone and class, with CI. 5. If CI excludes 1, apply the push; else use the pooled value. 6. Clip to [0.02, 0.98]. 7. If an external estimate exists, blend: weight external about 4x when strong. 8. Log all steps; after resolution update the class record.

### 4.6 Learning weights
Quasi-arithmetic pool scores are concave in the weights; online gradient descent has low regret [a20]. It needs a scored history. A single run has none, but a class-level record in agent memory can hold it.

### 4.7 Model-based merge
A supervisor reads the samples, finds disagreements and searches to resolve them [c14]. It helped only when it added searched evidence. A pure LLM merge (USC) loses to a mean [a24, d14].

## 5. What holds up

**Holds.**
1. Averaging in log-odds is at least as good as averaging probabilities and has no tuning parameter [d05, b10, d14]. [E]
2. Among mean, median and trimmed mean for LLM samples, Brier differs by under 0.004 [K06]. [E]
3. Theory: the push depends on information diversity and overlap; with high overlap the factor is near 1, possibly below [K03]. [E]
4. A fixed factor can be guaranteed only up to about sqrt(3) [K04]. [E]
5. Partial push beats full push in two human datasets [d03, d04]. [E]
6. Teams that share information (superforecasters) gain little from extremizing [a07, a15, d06]. [E]
7. Same-model sampling gives a modest variance gain, most from the first 3-5 samples [d10, d18, c13]. [E]
8. Different models or evidence sources add more than copies [d16, d17, c04, a25]. [E]
9. Averaging with an independent source beats letting the model reconcile in prose [c04, b12]. [E]

**Moderators.** Information overlap (largest). Horizon: bias correction matters at long horizons, information fusion at short ones [d07]. Expertise: lower-expertise crowds need larger a (3.08 vs 2.43) [d01]. Question set: yes-biased sets need an intercept [d04]. Backbone and prompt: the sign of miscalibration differs [b15]. Position in the range: gains come from bins 0.2-0.4 and 0.6-0.8 [d11]; Halawi's tails had accuracy 7% higher but Brier 0.04 worse [b08].

**Failures and weak replication.**
- BLF could not resolve an AIA-style Platt gain on its Pro backbone; small preliminary gains on Kimi [d15]. K27 contested.
- A factor learned on another benchmark transferred only partly (0.1125 to 0.1104, vs 0.1076 for fixed sqrt(3)) [d11].
- Halawi: isotonic and binning gave nothing; the system was already calibrated [c07].
- Ensembling base GPT-4o was worse than single (0.218 vs 0.210) [b13]. The ForecastBench ensemble (0.197) lost to the best single model (Claude-3.5-Sonnet 0.178) [a26]. Schoenegger's median (0.20) lost to GPT-4 alone (0.15) [c02].
- Prophet Arena: prompt-variant ensembles gave under 0.01 because the model returns nearly the same number [c28]. Superforecaster persona -0.001, p=0.93 [c27].
- The plain mean was worse than the best single model in Carvana [d08].
- No clean failed replication of the GJP human gain was found. Palley-Soll (snippet only) hint that shared-information methods do worse when the coin bias is near 0 or 1 [d19]; unverified.

**Worked.** Log-odds pooling; a capped fitted push on human crowds; blending with a distinct source (crowd at 4x weight, 0.149 to 0.146); mixing decorrelated forecasters; an agentic supervisor with search (small); RL training that cuts per-sample error (more than 5x sampling).
**Did not work.** LLM-only merge (USC); best-of-k (picks a bottom-three forecast 7.2% of the time); yes/no counting (0.231-0.267); persona prompts; isotonic on a calibrated system; Bayesian-reasoning prompts (worse) [c27]; debate (majority vote reproduces its gain) [c23].

## 6. Language models

**Same-model samples.** The gain is real but small: 0.1182 to 0.1140 (-3.6%) with 10 AIA samples [d10]; 0.1867 to 0.1788 for median of 5 [d18]; median vs mean under 0.004 apart [b15]. Returns drop after about 5 [c13]. No source measures how within-model error correlation varies with temperature, prompt variation or retrieval [K21; gap 4 open].

**Between-model correlation is high.** r = 0.943 across seven LLM versions on football; ensemble gain 0.0047, not significant; open-book access did not change convergence [d17]. Mantic: frontier-model samples are tightly correlated; the best team of 5 spread draws across four forecasters; the least replaceable member was the least correlated one [d16].

**Mixed pools.** The 12-LLM median (0.20) equals the human crowd (0.19) but not the best single model (GPT-4 0.15) [a21, c02]. The ForecastBench 9-forecast ensemble (0.194-0.197) trails the best single (0.178) [a26]. A pool of unequal members can lose to its best member.

**Push on LLM ensembles.** Only AIA reports one on same-model samples: fixed sqrt(3) -5.6%, best fit 2.27, no token-matched control [d11]. At the superforecasters' best coefficient (1.72) the agent still scored better [c16]. BLF did not reproduce on Pro [d15]. Halawi (calibrated by construction) saw no recalibration gain [c07]. Direction depends on model and prompt [b15, b16, c03, d13]. Verdict: [C].

**Biases.** Acquiescence/yes bias [c03, b16]; hedging toward 0.5 [d13, b08]; overconfidence on likely events in some models [b15]. These are shared errors across samples, so averaging cannot remove them. Debias (intercept) before or together with any slope [K25; untested on LLMs].

**LLM as merger.** USC is worse than none on forecasting [a24]. The agentic supervisor is +0.0074 over none and +0.0043 over non-agentic [d12]. Mixture-of-Agents helps open chat (65.1% vs 57.5% on AlpacaEval 2.0) but agents read peers, so it is not independent [c25].

**Humans plus LLM.** Humans with an LLM assistant gained 24-28% accuracy; no consistent harm to crowd aggregation (six questions, N=991) [c08, c09]. Independent human-AI aggregation beat AI-as-advisor on 10 datasets [b17]. Averaging machine and human median beats model self-update [c04].

**Voting tasks.** Self-consistency +3.9 to +17.9 points [a30]; Agent Forest GSM8K +12 to +24 [c21]; confidence-weighted votes use 40%+ fewer paths [c22]. These are single-answer accuracy with correlated samples. Vote share is not a probability.

**Training changes the noise.** RL on proper scoring rules changed bias, information and noise differently; trained single samples beat median-of-5 [d18]. Outcome RL with 7-run ensemble: Brier 0.190, ECE 0.062 vs base 0.215 [b14, c29].

**Levels for context** (not comparable across sets): superforecasters 0.096, public 0.121, best LLM 0.122 with crowd values or 0.136 without [c10]; Halawi test: system 0.179, crowd 0.149.

## 7. What our agent should take

Marks: [E] established, [S] single-source, [C] contested, [D] design choice.

### Add now (established)
| # | Item | Part | Status | Evidence |
|---|---|---|---|---|
| A1 | Pool numeric forecasts in log-odds (clipped), by code, never by an LLM merge. Do not spend effort choosing among mean/median/trimmed. | G5, O (pool) | [E] | a24, b09, c06, b10, d05, d14; K06, K20 |
| A2 | Keep G4: no blind push on samples of one model. Reword to "push only if fitted on held-out data and capped". | G4 | [E] no blind push; [C] any push | a01, a04, b07, K03, K14 |
| A3 | Take samples in fresh isolated contexts; independence is what aggregation needs. | S3 | [E] | b17, c23, a30; K14 |
| A4 | Sample few: 3 to 5 for a probability. Returns taper after about 5. | S3, G11 | [E] | d10, c13, d18; K22 |
| A5 | If an independent external estimate exists, average it with the agent number, weighting the external value more when strong. No prose self-update from it. | S7, memory | [E] | c04, a25, b08, c17; K12 |
| A6 | No push near 0 or 1. Clip final p; do not extremize pooled values past 0.9 or under 0.1. | G4 | [E] | d11, b08, d03; K13 |
| A7 | Use a base rate as the pivot; no push without one. Never push a forecast that sits on the wrong side. | S1, S2 | [E] | a09, d11 |
| A8 | Check the direction of miscalibration (yes bias, hedging, overconfidence) per backbone before any recalibration. | G4, S0 | [E] | c03, b16, b15, d13; K11 |
| A9 | No LLM-only merge, best-of-k, yes/no counting, persona or prompt-variant ensembles for probabilities. | G5, 4b | [E] | a24, d14, c14, c28, c27; K15 |
| A10 | Vote share or sample agreement is not a probability; do not extremize it. | G4 | [E] | a30, c28 |

### Test first
| # | Item | Part | Status | Evidence |
|---|---|---|---|---|
| T1 | Fitted, capped push (slope, intercept) on the pooled logit of K same-model samples; allow a < 1; apply only if the CI excludes 1. | G4, O | [C] | c15, d11, d15; K09, K17, K27 |
| T2 | Push vs more samples vs one careful pass, equal tokens. | G7 | [S] | K17, d18 |
| T3 | Evidence-diverse sampling (samples differ by retrieved sources), then push sized by overlap. | S3, G4 | [S] | b07, a05, d16; K24 |
| T4 | Agentic supervisor that searches, vs plain mean. | S7 | [C] | c14, d12, d14; K07 |
| T5 | Intercept plus slope together (yes bias). | G4 | [S] | d04; K25 |
| T6 | Mixed-backbone pool vs same-model pool. | S3 | [S] | d16, d17; K21 |
| T7 | Class record of fitted (a, b) per class and backbone, read at S0. | memory | [D] | a20, d15 |
| T8 | Consistency check across related questions before pooling. | S4 | [S] | a29 |

## 8. Concrete tests on our bench

Common design: both arms at equal total tokens. Items: resolved binary forecasting questions, split into fit half and score half; use a post-cutoff set to avoid leakage. Metric: Brier, plus reliability and fitted slope; bootstrap CI over questions. Use about 300 or more resolved questions (ForecastBench 2SE is 0.024 at 200 items).

| Test | Item type | Arms (equal tokens) | Metric | Expected effect |
|---|---|---|---|---|
| E1 slope by overlap | Binary questions, K=5 same-model samples | K with shared retrieval vs K with different retrieved documents vs K bare | Fitted slope a of outcome on pooled logit, with CI | Slope near 1 (or below) with shared context; above 1 only with different evidence |
| E2 push vs samples | Same set | (a) N=5 mean; (b) N=5 plus held-out-fitted push; (c) N=10 mean; (d) one long careful pass | Brier | Push gain 0 to -0.006 (AIA -0.0064 at sqrt3); N 5 to 10 under -0.002 |
| E3 correlation | Per-question residuals | Temperature 0.3 vs 1.0; prompt variants; retrieval variants | Mean pairwise residual correlation | High (above 0.8) at all settings; falls only with retrieval variation |
| E4 yes bias | Mixed base-rate set | Pool; pool+slope; pool+slope+intercept | Brier, sign of mean error | Slope-only pushes the wrong way on yes-biased sets; intercept fixes it |
| E5 tails | Items with pooled p in [0.05, 0.2] and [0.8, 0.95] | Capped push vs none | Brier and log loss by bin | Gain in 0.2-0.4 and 0.6-0.8 bins; none or loss at tails |
| E6 anchor blend | Items with crowd or market value | Agent; crowd; blend (crowd 4x); model self-update from crowd | Brier | Blend beats both; numeric blend beats prose update |
| E7 supervisor | Same set | Plain mean of 5 vs agentic supervisor with search | Brier | At most -0.004 vs mean; zero without search |
| E8 mixed backbones | Same set | 5 samples one backbone vs 5 over 2-3 backbones | Brier | Mixed pool gains if errors are less correlated; can lose to the best single |
| E9 online detector | Same set | Push size set by retrieved-document overlap vs fixed | Brier, slope | Overlap predicts the slope; sign unknown |

## 9. What does not transfer, and why

- **Human GJP gains (-21% to -38% Brier).** They came from many people with distinct information, fitted to outcomes. Resampled LLM calls share one information set (K19: do not carry over the size).
- **Baron reason 2 (regression for missing information).** Needs forecasters who know they lack what others have. All samples of one model lack the same things.
- **Superforecaster result.** Teams that share information gain little. It supports A2, but gives no number to reuse.
- **Real-valued UCI result (a11).** Not probabilities, one dataset. The overlap pattern transfers qualitatively.
- **Tabular ensembles (Lichtendahl).** Show that shared inputs give a tiny gain (0.0010-0.0021 log loss) and pooling can lose to the best member. Not LLMs; log loss not Brier.
- **Self-consistency and Agent Forest gains.** Single-answer accuracy under matching, not probability quality.
- **AIA push number.** One team's benchmark, search-backed agent, no equal-token control, partly unreplicated. Use it to design a test, not as a setting.
- **sqrt(3) worst-case factor.** A ceiling for blind push, not a recommended value.
- **Online weight learning (a20).** Needs scored history; one run has none.
- **Horizon effects (BIN).** Our bench items may not have GJP's horizons.
- **Cross-paper Brier values.** Halawi, ForecastBench, Metaculus and AIA use different question sets.

## 10. Open questions

1. Does a fitted, capped push on K same-model samples beat more samples at equal tokens? No source has run it (K17).
2. What is within-model error correlation by temperature, prompt variation and retrieval? Unmeasured.
3. Does the AIA sqrt(3) gain replicate on ForecastBench and Prophet Arena? Only BLF checked, partly (K27).
4. Can the agent detect online when to anti-extremize? No detector found (K24).
5. How does yes bias interact with a push in LLMs? Human data only (K25).
6. What is the extremizing gain by team size in GJP (Mellers 2014)? Paper not parsed.
7. Palley-Soll boundary near 0 and 1: snippet only. Sevilla not found.
8. Do model merges help only when they add evidence? Suggestive (AIA vs BLF), not tested directly.
9. Why is the ceiling about 7% Brier for super-forecasters (a06) but 38% on all GJP (d03)? Pool and fitting differ; unexplained.
10. Does push size interact with retrieval quality? No data.

## 11. Sources

[V] opened (page or PDF text read this session); [M] snippet or second-hand only.

- [V] Satopaa, Pemantle, Ungar (2015) Modeling Probability Forecasts via Information Diversity. https://arxiv.org/abs/1406.2148 (a01-a07, b03)
- [V] Satopaa and Ungar (2015) Combining and Extremizing Real-Valued Forecasts. https://arxiv.org/abs/1506.06405 (a08-a12, b01, b02)
- [V] Lichtendahl, Grushka-Cockayne, Jose, Winkler (2018) Bayesian Ensembles of Binary-Event Forecasts. https://arxiv.org/abs/1705.02391 (a13-a15, d08)
- [M] Lichtendahl et al. (2022) Operations Research abstract. https://ideas.repec.org/a/inm/oropre/v70y2022i5p2998-3014.html (d09, b22)
- [V] Baron et al. (2014) Two Reasons to Make Aggregated Probability Forecasts More Extreme. https://faculty.wharton.upenn.edu/wp-content/uploads/2015/07/2015---two-reasons-to-make-aggregated-probability-forecasts_1.pdf (d01, d02; a16 and b19 were not opened)
- [M] Mellers et al. (2014) Psychological strategies for winning a geopolitical forecasting tournament. https://doi.org/10.1177/0956797614524255 (a17, b21, d20)
- [V] Mellers et al. (2015) The psychology of intelligence analysis. https://faculty.wharton.upenn.edu/wp-content/uploads/2015/07/2015---the-psychology-of-intelligence-analysis.pdf (d21)
- [M] Ranjan and Gneiting (2010) Combining probability forecasts. https://doi.org/10.1111/j.1467-9868.2009.00726.x (a18)
- [M] Satopaa et al. (2014) Combining multiple probability predictions using a simple logit model. https://doi.org/10.1016/j.ijforecast.2013.09.009 (b20)
- [V] Satopaa, Jensen, Mellers, Tetlock, Ungar (2014) Probability aggregation in time-series. https://arxiv.org/abs/1408.0087 (b04)
- [V] Satopaa (2018) Inefficiency of Central Tendency. https://arxiv.org/abs/1706.06006 (b05)
- [V] Powell, Satopaa, MacKay, Tetlock (2022) Skew-Adjusted Extremized-Mean. https://faculty.wharton.upenn.edu/wp-content/uploads/2016/11/Skew-Adjusted.pdf (d03, d04)
- [V] Satopaa, Salikhov, Tetlock, Mellers (2021/2023) BIN model. https://faculty.wharton.upenn.edu/wp-content/uploads/2022/03/SSRN-id3781405.pdf (d05-d07)
- [V] Neyman and Roughgarden (2023) From Proper Scoring Rules to Max-Min Optimal Forecast Aggregation. https://arxiv.org/abs/2102.07081 (a19, a20)
- [V] Neyman and Roughgarden (2022) Are You Smarter Than a Random Expert? https://arxiv.org/abs/2111.03153 (b06, c18)
- [V] Neyman (2024) Algorithmic Bayesian Epistemology. https://arxiv.org/abs/2403.07949 (b07)
- [M] Palley and Soll (2019) Management Science. https://pubsonline.informs.org/doi/suppl/10.1287/mnsc.2018.3047/suppl_file/mnsc.2018.3047-sm.pdf (b23, d19)
- [M] Sevilla (2021) Principled extremizing. https://forum.effectivealtruism.org/posts/biL94PKfeHmgHY6qe (b24)
- [V] Schoenegger, Tuminauskaite, Park, Tetlock (2024) Wisdom of the Silicon Crowd. https://arxiv.org/abs/2402.19379 (a21-a23, b11, b12, c01-c04)
- [V] Schoenegger, Park et al. (2024) AI-Augmented Predictions. https://arxiv.org/abs/2402.07862 (a28, c08, c09)
- [V] Halawi, Zhang, Yueh-Han, Steinhardt (2024) Approaching Human-Level Forecasting. https://arxiv.org/abs/2402.18563 (a24, a25, b08, b09, b25, c05-c07)
- [V] Karger et al. (2025) ForecastBench. https://arxiv.org/abs/2409.19839 (a26, a27, b10, c10, c11)
- [V] Paleka et al. (2024) Consistency Checks for Language Model Forecasters. https://arxiv.org/abs/2412.18544 (a29)
- [V] Paleka et al. (2025) Pitfalls in Evaluating Language Model Forecasters. https://arxiv.org/abs/2506.00723 (c30)
- [V] Wang et al. (2023) Self-Consistency. https://arxiv.org/abs/2203.11171 (a30, c20)
- [V] Hsieh et al. (2024) Reasoning and Tools for Human-Level Forecasting. https://arxiv.org/abs/2408.12036 (b13, c12)
- [V] Turtel et al. (2025) Outcome-based RL to Predict the Future. https://arxiv.org/abs/2505.17989 (b14, c29)
- [V] Lu (2025) Evaluating LLMs on Real-World Forecasting. https://arxiv.org/abs/2507.04562 (b15, c26)
- [V] Bench to the Future (2025). https://arxiv.org/abs/2506.21558 (b16)
- [V] Berger, Analytis, Satopaa, Kurvers (2026) Beyond AI advice. https://arxiv.org/abs/2603.29866 (b17)
- [V] Turtel et al. (2026) How Proper Scoring Rules Shape LLM Forecasting. https://arxiv.org/abs/2608.28482 (b18, d18)
- [V] Alur et al. (2025) AIA Forecaster. https://arxiv.org/abs/2511.07678 (c13-c17, d10-d13)
- [V] Murphy (2026) Agentic Forecasting with Structured Linguistic Beliefs (BLF). https://arxiv.org/abs/2604.18576 (d14, d15)
- [V] Aitchison et al. (2026) Diversity is the Strength of the AI Crowd. https://arxiv.org/abs/2606.29661 (d16)
- [V] Schroeder et al. (2026) LLM-SoccerArena. https://arxiv.org/abs/2607.24573 (d17)
- [V] Chen et al. (2023) Universal Self-Consistency. https://arxiv.org/abs/2311.17311 (c19)
- [V] Li et al. (2024) More Agents Is All You Need. https://arxiv.org/abs/2402.05120 (c21)
- [V] Taubenfeld et al. (2025) Confidence Improves Self-Consistency. https://arxiv.org/abs/2502.06233 (c22)
- [V] Debate or Vote (2025). https://arxiv.org/abs/2508.17536 (c23)
- [V] Xiong et al. (2024) Can LLMs Express Their Uncertainty. https://arxiv.org/abs/2306.13063 (c24)
- [V] Wang et al. (2024) Mixture-of-Agents. https://arxiv.org/abs/2406.04692 (c25)
- [V] Schoenegger, Jones et al. (2025) Prompt Engineering LLM Forecasting. https://arxiv.org/abs/2506.01578 (c27)
- [V] Prophet Arena (2025). https://arxiv.org/abs/2510.17638 (c28)
