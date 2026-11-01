# Bounded rationality and satisficing: deep document

*Subfield E18.01. Built from evidence_a-d.jsonl (a01-a26, b01-b27, c01-c25, d01-d19), claims.jsonl (K01-K31) and critique.md in this folder. Status tags: [E] established, [S] single-source, [C] contested. Evidence ids are in square brackets or plain, for example a12. Where the cross-check corrected a number, the corrected number is used here.*

## 1. What it is

Bounded rationality is the idea that real decision makers have limited time, limited information and a limited mind. They cannot compute the best option. So they search, and they stop. Herbert Simon (Nobel 1978) split it into two parts [a01]:

1. **Search.** Options are not given. They must be found, and finding costs time.
2. **Satisficing.** Set an aspiration level. Take the first option that meets it. Stop searching.

Simon also said aspiration levels move. They rise in a benign world with many good options and fall in a harsh one [a01].

Why this matters for our agent. The agent is a language model inside a scaffold. It has a token budget. Every extra pass costs tokens. Two schema parts depend directly on the stopping idea:

- **S0 gate.** Classify the problem cheaply and decide how much effort it deserves.
- **G11 and G12.** Think briefly by default. Spend by difficulty.

This subfield answers four practical questions. When should the agent stop? What should count as "good enough"? How many options should it look at? Does the model behave like a rational optimiser, or like a biased human? The sections below give the evidence.

Two kinds of evidence are kept apart throughout:

- **Human studies.** These tell us what the idea is and where it breaks. They are mostly students and short, low-stakes tasks.
- **LLM studies.** These tell us what to build. The strongest are 2024-2026 papers on reasoning models that fail to stop.

The main finding in one line: the human literature gives the concept, and the LLM literature on overthinking and early stopping gives the tested engineering. Almost nothing tests a stop rule inside an agent loop at strictly equal tokens (critique, weak spots).

## 2. History and theories in depth

### 2.1 Simon: the founding view (1955-1979)

Simon's 1955 and 1956 papers are the founding texts. They were **not opened** (publisher PDF returned 403) [a06]. What we know comes from his Nobel lecture (published 1979), which was opened [a01-a05].

- **Two ways to satisfice** [a02]. Either solve a simplified world optimally, or solve a realistic world only well enough. Neither dominates. His example is the Holt, Modigliani, Muth and Simon (1960) production-smoothing rule: assume quadratic costs, and the optimal rule is linear and computable. The quality lost by the simplification is not measured in the text.
- **Satisficing inside problem solving** [a03]. Solutions are found after searching a tiny part of the problem space, using selective heuristic search. The evidence is qualitative: puzzles, diagnosis, portfolio choice, chess, from Newell and Simon (1972).
- **Aspiration can approach optimal** [a01]. In long-run equilibrium, adaptive aspirations might equal optimal choice with search costs. So satisficing is not always second best. This is Simon's own caveat.
- **The 1956 result, as the Nobel lecture reports it** [a06]. A dynamic-programming house-sale search was formally equivalent to utility maximisation with search costs. Satisficing does not need those cost estimates.
- **Polemic** [a04]. Simon accused economists of satisficing about their own theories while insisting firms maximise. He wanted theories tested on micro-level predictions, not defended "as if".

Simon's text is a verbal theory. There is no experiment in it (K01, single-source). A claim that 97% of 628 used-car dealers used a satisficing price rule appears on Wikipedia only; the source was not found, so it is not used [a07].

### 2.2 The Stigler reading versus the Simon reading

Two readings compete [a11]:

- **Stigler (1961).** Search is costly. Fold the cost into the maximisation problem. Stopping is then optimal.
- **Simon.** Do not assume the costs are known. Use an aspiration level.

Gigerenzer and Goldstein read Simon as "limits of the mind plus the structure of the environment" and say follow-up work dropped the second half [a11]. Simon himself said that adaptive aspirations may approach the optimum [a01]. So the dispute is partly about whether "satisficing" means "worse than optimal" or "a different way to reach a good result".

Artinger, Gigerenzer and Jacobs (2022, Journal of Economic Literature) review 60+ years and split the field in two [a24, d16, abstract only]:

- **Under risk** (probabilities known), satisficing is usually inferior to optimising.
- **Under uncertainty**, satisficing strategies derived from data can do very well.

The conditions list was not read (post-print returned 403). No LLM task has been tested against this split [K20].

### 2.3 Fast and frugal heuristics (1996)

Gigerenzer and Goldstein built the first formal simulated satisficing inference algorithm, Take The Best [a08]. Steps:

1. If only one object is recognised, pick it.
2. Otherwise look up cues in order of validity.
3. Stop at the first cue that discriminates. Pick the object it favours.

The wider field is the neighbouring subfield "Fast and frugal heuristics, ecological rationality", researched in parallel. Here it matters because it is a worked stopping rule (see 3 and 4).

### 2.4 Aspiration adaptation, mate search, and sequential models

- **Selten (1998)** aspiration adaptation theory handles several goals with a priority order and step-wise adjustment [a26, not opened].
- **Bendor, Kumar and Siegel (2009)** show an adaptive-aspiration rule can approach optimal long-run choice in bandit-like settings [a26, not opened].
- **Todd and Miller (1999)** simulate aspiration-based mate search: a look-around phase sets the aspiration, then take the first candidate who beats it [a25, not opened]. Optimal stopping is covered by a sibling subfield. The secretary problem page gives the 37% rule (1/e = 0.368, best option chosen about 36.8% of the time) and says people "tend to stop searching too soon", with no magnitudes [d17, secondary].
- **Reverdy, Srivastava and Leonard (2017)** formalise satisficing in multi-armed bandits: eight objectives defined by a reward threshold, four provably equivalent to known bandit problems. Maximising objectives give regret that grows logarithmically. With a non-zero sufficiency tolerance the satisficing UCL variant has finite cumulative satisficing regret (Theorems 10 and 11). In simulation with M = 2 and sufficing parameter 0.05, switching cost fell to near that of standard UCL. Gaussian rewards, known variance, no human or LLM data [a23].

### 2.5 Maximizers versus satisficers (individual differences)

Schwartz et al. (2002) built a trait scale and argued maximizers are less happy [a16, a17]. This line is large but has weak links to agent design (K18, K19 map to "none"). It is covered in section 5.

### 2.6 Choice overload

Iyengar and Lepper (2000) and followers argued that too many options hurt. This is the human side of "how many candidates should the agent see" (section 5).

### 2.7 Computational accounts of stopping

Keramati, Dezfouli and Piray (2011) model the choice between a fast habit and a slow goal-directed search. The arbitration weighs value of information against time cost. It explains why reaction time rises with number of options and why behaviour becomes habitual with training. A model paper with animal data; no LLM test [b25, K21]. It is the closest human model to the rule "do another pass only if its expected value exceeds its token cost". The sibling subfield "Metareasoning, value of computation" covers this in depth.

## 3. Core findings with exact numbers

Status uses the claims file. Corrections from critique.md are applied.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Satisficing defined as search plus aspiration-based stop; aspirations adapt | No experiment | Simon 1978/79 [a01-a05] | [S] K01 |
| Take The Best matches regression on German city size (simulation) | TTB .658, weighted tallying .658, regression .657, tallying .656, Minimalist .647, Take The Last .645, weighted linear .623, unit-weight linear .621. 83 cities, 9 cues, about 858 million tests | Gigerenzer and Goldstein 1996 [a08] | [S] K04 |
| TTB is frugal | Looks up 2 to 20 cue values; integration models look up everything | G&G 1996 [a09] | [S] |
| Recognition validity input came from a small pilot | 26 Chicago undergraduates; recognised city larger in about 80% of comparisons; 80% then fixed by design | G&G 1996 [a09] | [S] |
| Linear models lost because weights could contradict the recognition cue | Unit-weight and weighted linear stay near .62; tallying and TTB near .66 | G&G 1996 [a10] | [S] (authors' own simulation) |
| Out-of-sample, TTB slightly beats regression | In-sample regression 74.3, TTB 74.2, unit-weight 74.1. Out-of-sample (10,000 half splits) TTB 72.2, regression 71.9, unit-weight 71.4. Margin under 0.5 points | Czerlinski et al. 1999, via Wikipedia, "citation needed" [b24] | [S] K04, original not opened |
| People pick the best of what they saw | 41 students, 3-second trials. Best seen item chosen 76% (N=4), 73% (N=9), 69% (N=16); random choice over seen set 30%, 20%, 18% | Reutskaja et al. 2011 [a12] | [S] K03 |
| Pure threshold satisficing rejected; soft stop fits | Stop probability rises from about 0% to about 50% with item value, never above 50% per fixation. Slopes 6.4% (N=4), 4.8% (N=9), 4.3% (N=16). Mean fixations at choice 3.3, 4.9, 5.5 | Reutskaja et al. 2011 [a13, a14] | [S] K02 |
| What is seen is driven by attention, not value | Initial search near random with respect to value; fixation efficiency 9.7% | Reutskaja et al. 2011 [a15, a13] | [S] K03 |
| Jam study: big set, fewer buyers | 60% stopped at 24 jams vs 40% at 6; of stoppers 3% bought at 24 vs 30% at 6. Second-hand | Iyengar and Lepper 2000 via Misuraca 2024 [b02] | [C] K16 |
| Essay and 401(k) | 74% handed in essay with 6 topics vs 60% with 30. 401(k): 800,000 employees, plans of 2 to 59 funds, participation highest under 10 funds, lowest at 59. Second-hand, correlational | Iyengar et al. 2004 via review [b03] | [C] K16 |
| Choice overload mean effect about zero | 63 conditions, 50 experiments, N=5,036. Mean D = 0.02, 95% CI about -0.09 to 0.12 (minus signs inferred), tau-squared 0.12, I-squared 68%. After 20% trimming D = 0.001. Prior preference or expertise protects (b=.50) | Scheibehenne et al. 2010 [d04, b04] | [C] K16 |
| Choice overload present with four moderators | 99 observations, N=7,202. No numeric d obtained (abstract only) | Chernev et al. 2015 [d05, b05] | [C] K16 |
| Making choice easier saves effort, not quality | Set sizes 6 to 24. E1 N=17, E2 N=28. Times 5.85 vs 7.38 s (E1), 5.47 vs 6.30 s (E2). Quality lower under low demand F(1,16)=13.66, partial eta-squared .46 | Seo et al. 2026 [b14] | [S] K17 |
| Maximizing, regret, life satisfaction | N=395: regret r=.45, life satisfaction r=-.24, positive affect r=-.22, negative affect r=.21, hope for success r=.13 | Peng et al. 2018 [b09] | [C] K18 |
| Time-lagged positive maximizing effect | Study 1 N=552, beta .11 (adjustment); Study 2 N=309 over 4 years, beta .17 adjustment, beta .08 GPA | Li et al. 2023 [b10] | [C] K18 |
| Maximizers with higher salary | "About 20% higher", memory or second-hand only | Iyengar et al. 2006 [a18, b07] | [C] K18, unverified |
| Maximizing and closure in experts | N=96 senior police: decision difficulty r=.249, need for closure r=.339 | Shortland et al. 2020 [b12] | [S] K19 |
| Reasoning models over-think trivial items | o1-like models used 1,953% more tokens than conventional models on "2+3"; one example had 13 solutions | Chen et al. 2024/25 [a22, c01] | [E] K05 (single paper for this exact figure) |
| First solution is usually already right | Over 92% of cases first round correct; under 60% of tokens. QwQ ASDIV 97%, MATH500 93%; R1 89-90%. QwQ ASDIV first round 287 tokens, 38.7% of response | Chen et al. [c02, a22] | [E] K05 |
| More rounds on easier items | QwQ ASDIV averaged 3.5 rounds; most responses 2-4 rounds (76-80% QwQ, 59-63% R1) | Chen et al. [c03] | [E] K05 |
| Training to stop at first correct cuts tokens | Headline up to 48.6% (ASDIV figure); MATH500 table: 2407.9 to 1330.7 tokens (-44.7%), accuracy 93.0 to 92.8; GSM8K -46.1%, 94.8 to 96.0. SimPO shortest-response -22.3% MATH500 | Chen et al. [b17, c04] | [C] K06 |
| First-correct-only hurts on hard items | FCS+Reflection beat first-correct-only by 1.4 points on MATH500; AIME24 46.7 to 43.3 | Chen et al. [c04, b17] | [C] K06 |
| Adaptive stop for voting | Up to 7.9x fewer samples, under 0.1% average accuracy drop, 17 datasets, 3 models. Maths 3.3x (0.1% drop), commonsense 2.9x (0.2%), symbolic 3.8x (no drop), coding 2.4x | Aggarwal et al. 2023 [c17] | [E] K07 |
| Beta stop beats cheap stops at equal cost | Beat Random, Majority, Entropy stops on GSM-8K at equal average sample cost | Aggarwal et al. [c18] | [E] K07 |
| Training-free early exit | 10 benchmarks, 11 models: chains -19.1% to -80.1%, accuracy +0.3 to +5.0. Code (R1-Distill-Qwen-32B): HumanEval 91.5 to 93.9 at 3,861 to 1,254 tokens; LiveCodeBench 56.0 to 56.6 at 9,109 to 3,677 | Yang et al. 2025 (DEER) [b18, d10] | [E] K07, K27 |
| Consensus stop (DeepConf) | K=512, warm-up 16. Token cut 18-85% vs majority voting. DeepSeek-8B AIME24 86.7 to 92.5 at -77.9%; GPT-OSS-120B AIME25 97.1 to 97.9 at -84.7%; some cells lose 0.8-0.9 points | Fu et al. 2025 [d07] | [E] K27 |
| Window-agreement stop | Sample reduction: MATH -33.8%, GSM8K -80.1%, StrategyQA -76.8%, CommonsenseQA -78.5%, Coin Flip -84.2%, Last Letters -67.4%. Counts samples, not tokens | Li et al. 2024 (ESC) [d08] | [E] K27 |
| Convergence depends on task | Answer-convergence ratio near 0.0 on NaturalQuestions, about 0.8 on GSM8K and MATH-500, about 0.9 on GPQA and AIME24. NQ token cuts 34.1-47.7% | Liu and Wang 2025 [d09] | [E] K05, K27 |
| Answer-level stops fire too early | 42.4% of confidence-stop failures and 54.8% of consistency-stop failures were premature (full chain ends correct) | Min et al. 2026 (PUMA) [d12] | [E] K28 |
| Shorter chains more accurate | Up to 34.5% more accurate than the longest chain for same question; short-3@k up to 33% wall-time cut | Hassid et al. 2025 [d14] | [S] K31 |
| Difficulty-aware compute | More than 4x efficiency vs best-of-N (about 4x less compute at matched performance, some bins); small model plus compute can beat 14x larger model | Snell et al. 2024 [c21] | [E] K08 |
| Learned difficulty probe | Up to 50% less compute at equal reward on Math and Code; probe ranking accuracy Code 74%, Math 84%, Chat routing 72%; about 50% of Code problems have zero success | Damani et al. 2024 [d06] | [E] K08, K29 |
| Prompt-only gating unreliable | Best ROC-AUC 72.2 (AIME25, 1.5B), did not carry to 7B or other sets | Tan et al. 2025 [d13] | [E] K29 |
| Hidden-state correctness probe | ROC-AUC above 0.7, ECE below 0.1 in distribution; early exit up to -24% tokens at equal accuracy; worse on AIME, no transfer from logic to math | Zhang et al. 2025 [d11] | [E] K29 |
| Coverage rises with samples, selection plateaus | SWE-bench Lite: 15.9% (1 sample) to 56% (250 samples), above 43% single-sample best | Brown et al. 2024 [c22] | [S] K09 |
| Self-refine returns shrink | About 20% absolute average gain (5-40% by task). Code optimisation 22.0 to 28.8 after three iterations; sentiment 33.9 to 36.8; constrained generation 29.0 to 49.7 | Madaan et al. 2023 [c19] | [S] K10 |
| Pruned search beats sampling | Game of 24, GPT-4: IO 7.3, CoT 4.0, CoT-SC k=100 9.0, IO best of 100 33, CoT best of 100 49, ToT b=1 45, ToT b=5 74 | Yao et al. 2023 [c20, c25] | [S] K11 |
| Satisficing alignment at decoding | +22.3% helpfulness win-tie over MOD (Zephyr-7B, GPT-4 judge); about +10% on a humor task; over 90% of responses with reward at least -12 judged harmless | Chehade et al. 2025 [a21, b15, d15] | [S] K12 |
| LLM numeric choice is near-rational | No GARP violation in 95/89/81/92 of 100 (risk/time/social/food). Mean CCEI .998/.997/.997/.999 vs humans .980/.985/.967/.963. 99.9% of random simulated subjects violate GARP. Invalid 4.7% (T=0.5), 9.8% (T=1) | Chen et al. 2023 [a19, c08, c09] | [E] K13 |
| CoT models track expected value more than humans | Correlation with max EV, CoT: GPT-4o .94, GPT-4-Turbo .93, Llama-3-70B .80, Claude 3 Opus .76, Llama-3-8B .57; humans .48. Zero-shot GPT-4-Turbo .41, GPT-4o .28 | Liu et al. 2024/25 [c05, b19] | [E] K13 |
| Old models show human-like errors; new ones do not | CRT: GPT-3 family 70-90% intuitive wrong vs humans 55%. Correct: ChatGPT-3.5 59%, ChatGPT-4 96%, davinci-003 5%. Intuitive errors 15% and 0%. Humans 38% correct (original 41%) | Hagendorff et al. 2023 [c12]; Binz and Schulz [a20, c10] | [E] K14 |
| Deliberation can hurt | CoT drops accuracy up to 36.3 points on some tasks; GPT-4o 87.50 to 64.40; Claude 3 Opus 70.7 to 62.7; Gemini 1.5 Pro 68.00 to 61.95; Claude 3.5 Sonnet 65.9 to 67.7 (ns) | Liu et al. 2024 [c16] | [S] K15 |
| Order and label bias in selection | MMLU gpt-3.5-turbo 67.2 to 60.9 when gold always D (-6.3); llama-30B picks A/B/C/D 34.6/27.3/22.3/15.8% with gold balanced; 20-doc QA worst-position drop over 20%; judge bias largest when candidates close in quality (150,000+ instances) | Zheng 2024; Shi 2024; Liu 2023 [d01-d03, d19] | [E] K26 |

## 4. Mechanisms and models

Each model below is written so an engineer can implement it. "Agent" means our scaffold.

### 4.1 Aspiration-level satisficing (Simon)

Inputs: a generator of candidate options, a scorer, an aspiration level `alpha`.

```
alpha = initial_standard
for each candidate c from generator:
    if score(c) >= alpha: return c           # stop at first good-enough
    count failures
    if failures > F: alpha = alpha - delta   # harsh world: lower the bar
return best_seen
```

Adaptive step: after quick success, raise `alpha`; after repeated failure, lower it. This is Simon's adaptive aspiration [a01]. No source tested it in an LLM agent (d18, K30). Treat it as a design choice to test.

Agent mapping. The scorer must be label-free and code-based (G5): a verifier pass, a held-out check (G3), or agreement of independent samples (with the G4 caveat).

### 4.2 Soft stop (hybrid, Reutskaja)

Reutskaja et al. fit three models that share two phases [a14]:

- Phase 1: sample items at random without replacement.
- Phase 2: pick the best seen with probability `q`, otherwise a random seen item.

They differ only in the stop rule:

- Optimal search: stop when expected gain from one more item is below its cost.
- Pure satisficing: stop with probability near 1 once value passes a reservation value.
- Hybrid (best fit): optimal search plus a random stop whose probability rises with elapsed time.

The data rejected the sharp threshold: stop probability never passed about 50% per fixation [a13]. One implementable form: `p_stop(step, value) = min(0.5, a + b*value) + c*step`. In an agent this gives a stop that is partly value-driven and partly time-driven. The form is our sketch, not the paper's fitted model. Single-source (K02). A hard-threshold arm versus a soft arm is cheap to test.

### 4.3 Take The Best (stop at first discriminating check)

```
if only one option recognised: choose it
for cue in cues sorted by validity (high to low):
    values = lookup(cue, A), lookup(cue, B)
    if values differ: return the option the cue favours
return guess
```

Frugality: 2 to 20 lookups instead of all [a09]. Accuracy tied with regression (.658 vs .657), not better [a08]. Fit is specific to a skewed, non-compensatory cue structure and the recognition cue. Agent mapping: in a verification step (S8), order checks by diagnostic value and stop at the first one that decides. Test only; not established in LLMs (K04).

### 4.4 Sequential stop on vote counts (Adaptive-Consistency and relatives)

Draw samples one at a time. After each, run a Beta test: is the leading answer's share credibly above chance? If yes, stop [c17, c18].

- Up to 7.9x fewer samples, under 0.1% average accuracy drop.
- Gains depend on a peaked answer distribution [c18].
- Window variant (ESC): sample in windows of 5, stop when all agree [d08]. The saving is biggest on easy sets (GSM8K -80.1%) and smallest on MATH (-33.8%), so it is difficulty-sensitive by design.
- Consensus variant (DeepConf): stop when consensus reaches 0.95, and drop low-confidence traces early [d07].
- First-m-finished (short-m@k): run k chains in parallel, stop at the first m that finish, vote among those [d14].

Risk: samples from one model are correlated (G4). Agreement can be wrong together. No paper measured calibration of the stop signal under that correlation (gap 9, open).

### 4.5 Confidence exit inside one chain (DEER and probes)

At each step transition, force a trial answer. If the trial answer's confidence is above a threshold, stop thinking [d10]. A probe variant reads hidden states and thresholds the probe score [d11]. Both need token probabilities or open weights. For a hosted API without logprobs, the label-free options are consistency across chunks [d09] and agreement of two independent samples.

The cost of a wrong stop is documented: 42.4% (confidence) and 54.8% (consistency) of stop failures were premature, meaning the full chain would have corrected itself [d12]. A safer rule combines a redundancy detector with answer verification [d12].

### 4.6 Difficulty-conditional compute (S0 gate)

```
d = estimate_difficulty(question)       # pilot sample / agreement / probe
if d == easy:  1 pass, stop at first check pass
if d == mid:   3 passes, adaptive-consistency stop
if d == hard:  up to 8 passes or tree search; require a verifier or a second independent route before stop
```

The thresholds 1, 3 and 8 are our sketch. Evidence: Snell et al. report more than 4x efficiency over best-of-N at matched performance on some difficulty bins [c21]. Damani et al.'s learned probe ranks easy vs hard at 72-84% and saves up to 50% compute [d06]. Prompt-only gating at zero steps is unreliable [d13]. Trap: items with zero chance of success (about 50% of Code problems in Damani) get over-funded if the difficulty forecast is wrong [d06]. A pilot-sample gate is not compared head to head with probes anywhere (gap 2).

### 4.7 Speed-accuracy arbitration (value of computation)

Run the next pass only if `value_of_information > token_cost`. Keramati et al. state this for habit-versus-search [b25]. A practical version (our sketch): estimate the gain from another pass as `1 - agreement` of current samples, multiply by the value of a correct answer, compare with the pass cost. This needs a calibrated agreement signal.

### 4.8 Threshold-constrained selection (satisficing alignment)

Maximise one primary objective subject to floors on the others. Chehade et al. do this at decoding with reward-model thresholds (beta = -12 and -0.5 gave a 50% win-tie constraint), top-k = 10 and 20 sampled responses per prompt [b15]. Raising the secondary threshold raised that objective's win-tie rate and then plateaued while the main objective kept falling [b16, d15]. Agent mapping: select by the primary metric among candidates that pass format, safety and constraint checks (G12, S4/S7).

### 4.9 Multi-armed bandit satisficing

If the task has a known sufficiency threshold, stop exploring once an arm clears it. Finite cumulative satisficing regret is proven for the UCL variant under Gaussian rewards [a23]. The sibling subfield "Bandit-style exploration" covers allocation.

### 4.10 Other published stop-and-prune rules

- Self-Refine: stop after a set number of steps or when feedback says stop. Returns shrink by the third pass [c19].
- Tree of Thoughts: rate partial thoughts as sure / maybe / impossible and drop the weak ones [c20].

## 5. What holds up

### 5.1 Replications and meta-analyses

- **Choice overload.** The biggest conflict in the human literature. Scheibehenne et al. (2010): mean D = 0.02, CI about -0.09 to 0.12, I-squared 68%, so effects vary a lot. After 20% trimming D = 0.001 [d04]. Chernev et al. (2015): significant overload once four moderators are included (99 observations, N=7,202), but no numeric overall d was obtained [d05]. A 2024 review of 49 papers says overload is conditional [b01]. Verdict: contested. No LLM test varies candidate-set size (K30).
- **Moderators (all second-hand).** Larger overload with set complexity, hard tasks, uncertain preferences, an effort-minimising goal. Experts show overload with small sets, not large (Mogilner 2008; Morrin 2012). Grouping options into categories (even meaningless labels) helped (Mogilner 2008). Showing small sets before large ones reduced overload (Levav 2010). Choosing for others: a larger set gave more satisfaction (Polman 2012). Eastern Europeans were more satisfied with large sets than Western Europeans [b05, b06, b08]. Most of this is single-study.
- **Maximizing.** The "unhappy maximizer" story (regret r about .45-.5, life satisfaction r=-.24) is consistent but cross-sectional. A time-lagged pair of studies found small positive effects (beta .11-.17) [b09, b10]. Up to 13 competing scales exist, a measurement problem [b13]. The "20% higher salary" result was never opened [a18, b07]. Verdict: contested, and low relevance to agent design.
- **Search behaviour.** Reutskaja's finding that stop probability is smooth and capped near 50% is a single study (41 students, 3-second trials) [a12-a15]. No replication was found.
- **Take The Best.** The tie with regression in the 1996 simulation was confirmed from the paper. The out-of-sample "slight win" (72.2 vs 71.9) is from Wikipedia only; the original was not opened [b24].

### 5.2 What failed or weakened

- **Pure threshold satisficing as a model of human search** was rejected in the eye-tracking study [a13].
- **Easing the choice does not raise quality** as sets grow (N=17 and 28): people saved effort rather than reinvesting it [b14].
- **First-correct-only stopping loses accuracy on hard sets** (AIME24 46.7 to 43.3; MATH500 gap closed by one reflection round) [b17, c04].
- **Label-free answer-level stops fail early on hard items**: 42.4% and 54.8% premature [d12]. Stops were also unstable on MATH-500 and GPQA [d09]. DeepConf notes overconfidence on wrong problems [d07].
- **Prompt-only difficulty gating** is unreliable (best ROC-AUC 72.2, no transfer) [d13].
- **Probes** degrade out of distribution (AIME, logic to math) [d11].
- **Deliberation hurts** on implicit-learning-like tasks (up to 36.3 points) but not for every model: Claude 3.5 Sonnet showed no significant drop (p=.969) [c16].
- **Self-feedback**: refinement is capped by the same model's blind spots (G2, G5); returns shrink by pass three [c19].

### 5.3 Interventions that worked

- Training toward first-correct solutions: -22% to -48% tokens, accuracy roughly kept on math (needs post-training and a label) [b17, c04].
- Training-free early exit, 11 models, 10 benchmarks, including code [d10].
- Adaptive sample stopping: 34-84% fewer samples [c17, d08].
- Consensus stopping: 18-85% fewer tokens [d07].
- Difficulty-aware allocation: more than 4x efficiency [c21]; up to 50% less compute with a learned probe [d06].
- Pruned tree search over plain sampling: 74% vs 49% (Game of 24) [c20].
- Threshold-constrained decoding: +22.3% win-tie vs MOD (GPT-4 judge only) [b15].
- Removing option-label tokens: the recall spread (RStd) fell from 5.5 to 1.0 on gpt-3.5-turbo [d01].

### 5.4 Caveats that apply to nearly all the stop-rule numbers

- Baselines are fixed-budget, full-chain or majority-vote baselines. None compares at strictly equal tokens (K27). They are Pareto comparisons.
- Chen's "first correct" oracle needs the ground truth. A deployed stop needs a label-free signal.
- Many are math-only. Code results exist for DEER and PUMA (LiveCodeBench 18-19% fewer tokens, at most 1.5 points change) [d10, d12]; planning has none.
- The "over 92%" first-correct figure is one paper and was not reproduced on code or planning [K05].
- Independent-source counts in the raw file were inflated: a22, b17, c01-c04 are one paper; a19 and c08 are one paper; b19, c05-c07 are one paper; a21, b15, b16 are one paper [critique].

## 6. Language models

### 6.1 Do LLMs behave like bounded or rational decision makers?

It depends on model generation and prompt.

- **GPT-3 (2022):** human-like biases. Failed all 3 CRT items with the intuitive answer; showed framing, certainty and probability-weighting effects; beat chance on 13,000+ gambles only with the largest model and stayed below humans (t(29134) = -11.50); no directed exploration; a perseveration bias in a bandit task [a20, c10, c11].
- **GPT-3.5 (2023):** anchoring, conjunction/availability, framing and endowment effects; four studies, abstract only [b20].
- **GPT-3 family on CRT:** 70-90% intuitive wrong answers vs humans 55% [c12].
- **ChatGPT-3.5 and ChatGPT-4 (2023):** 59% and 96% correct; intuitive errors 15% and 0% [c12]. The change came from model generation and chain of thought, not from a scaffold: 97% and 85% of answers used chain of thought.
- **GPT-class numeric choice (2023):** more consistent than humans. No GARP violation in 81-95 of 100 runs; mean CCEI .997-.999 vs .963-.985 for humans [a19, c08]. Sensitive to framing; invalid responses 4.7% at T=0.5 and 9.8% at T=1.
- **Gambles (2024-25):** with CoT, correlation with expected value is .94 (GPT-4o) and .93 (GPT-4-Turbo), vs .48 for humans. Zero-shot it is only .41 (GPT-4-Turbo) and .28 (GPT-4o). A "monkey prompt" pushed models closer to human [b19, c05, c06]. In the inverse task, GPT-4o with CoT correlates .97 with human inferences (47 observations) because humans also assume others are rational [c07].
- **Human prediction:** a model fine-tuned on 10.7 million human choices (Psych-101: 160 experiments, 60,092 participants) predicts held-out human behaviour better than cognitive models. Chat models are more rational than humans [c15, K25]. A good predictor of humans is not an optimal agent.

Lesson for the agent. On numeric and CRT-type tasks, current models do not need de-biasing toward rationality. They need checking against ground truth. Do not use 2022-23 bias papers for the current model (K14). One cross-check correction: the "MSE 0.0278 vs 0.2580" figure in b19 is the error of CoT predictions against the maximum-expected-value rule, not against human choices. The per-model Spearman values for human choices in b19 are unverified.

### 6.2 Do reasoning LLMs satisfice? No, they overshoot.

- 1,953% more tokens than conventional models on "2+3" [a22, c01].
- The first solution round was correct in over 92% of cases and held under 60% of tokens [c02].
- Rounds were higher on easy sets (ASDIV 3.5) than on harder ones [c03].
- Extra rounds help on hard sets (AIME, GPQA) [c02].
- The same pattern holds off competition math. Open QA converges near step 0 (NaturalQuestions); math at about 0.8-0.9 of the chain [d09]. Code keeps pass@1 with 34-80% of tokens (DEER) [d10].
- Shorter chains are more often correct for the same question (up to 34.5%) [d14].
- Task type matters: CoT hurts on some tasks and not for every model [c16].

### 6.3 What changed it, by how much

| Intervention | Effect | Needs |
|---|---|---|
| Self-training toward first-correct solutions [b17, c04] | -44.7% tokens MATH500 (headline up to 48.6%), accuracy 93.0 to 92.8 | Post-training, answer key |
| DEER confidence exit [d10] | -19.1% to -80.1% chain, +0.3 to +5.0 accuracy | Trial answers; token confidence |
| Answer-consistency across chunks [d09] | NQ tokens -34% to -48%, accuracy up | Open reasoning trace |
| Hidden-state probe exit [d11] | Up to -24% tokens, equal accuracy | Open weights, trained probe |
| PUMA redundancy plus verification [d12] | -26.2% tokens average, accuracy kept | Detector plus verifier |
| Adaptive-Consistency [c17] | Up to 7.9x fewer samples, <0.1% accuracy drop | Several samples |
| ESC window stop [d08] | 34-84% fewer samples | Several samples; 2023-24 models |
| DeepConf [d07] | 18-85% fewer tokens vs cons@512 | Logprobs |
| short-m@k [d14] | Up to 33% wall-time cut; short-1@k up to 40% fewer thinking tokens | Parallel chains |
| Difficulty-conditional allocation [c21, d06] | More than 4x efficiency; up to 50% less compute | A difficulty estimate |
| Satisficing alignment [b15] | +22.3% win-tie (GPT-4 judge) | Reward models, 7B only |
| Tree of Thoughts [c20] | 74% vs 49% (best-of-100 CoT) | More calls per item |

### 6.4 Order and option-set effects in LLM selection

- Moving the gold answer to the last slot cost gpt-3.5-turbo 6.3 points on MMLU; llama-30B had an A-bias [d01]. Most of this is a prior for label tokens.
- With 20 documents, accuracy fell by more than 20% in the worst position, sometimes below closed-book (56.1%) [d03].
- Judge position bias is largest when candidates are close in quality [d02].
- All models are 2023-2024. No 2025-26 frontier model was measured in an opened source. The number of candidates (3 to 24) was never varied for a selector (K30).

### 6.5 Planning and everyday decisions

A 2026 abstract claims reasoning LLMs beat the classical satisficing planner LAMA on multi-goal Blocksworld and path-star graphs, tracking optimal plan limits (abstract only, no numbers) [b21, K24]. A 2026 abstract on 955 Korean conversations reports people favour satisficing and heuristics in low-stakes talk; LLM-coded [b22]. Neither is usable until opened.

### 6.6 What nobody measured

No source tests a satisficing stop rule inside an LLM agent loop at equal total tokens with a label-free signal. No adaptive-aspiration test was found (d18, K30). No LLM test of the risk-versus-uncertainty split (K20).

## 7. What our agent should take

Schema parts: G = guardrail (G1-G12), S = state (S0-S9), O = operator (O1-O8), memory. Status: [E] established, [S] single-source, [C] contested.

### Add now (established)

1. **Stop at the first check that passes, on easy items; do not keep re-solving.** Schema: G11, G12, S4/S7 flow. [E] K05. Evidence: a22, b17, c01, c02, c03, c23, d09, d10, d12. Reasoning models give a correct first solution in over 92% of cases on math, and keep going. Rule: once a code check passes (G3, G5), end the loop. The label-free part is the harder piece (see Test first).
2. **Do not spend a fixed number of passes. Stop sampling when agreement is strong.** Schema: G11, G4. [E] K07, K27. Evidence: c17, c18, d07, d08, d10, d14. Saves 20-85% on tokens or samples in math, science QA and code. Warning: baselines are fixed-budget, not equal-token; agreement is only a hint (G4).
3. **Allocate by difficulty; the gate must be cheap.** Schema: S0, G12. [E] K08, K29. Evidence: c21, d06, d13. Use a pilot attempt or partial attempt plus agreement. Do not trust a prompt-only guess at S0.
4. **A wrong stop on hard items is costly, so require a verifier pass or a second independent route before an early stop there.** Schema: G11, G4, S8. [E] K28. Evidence: d12, d09, d07. In PUMA 42.4% and 54.8% of stop failures were premature.
5. **Randomise candidate order, and log the chosen position.** Schema: S0, S7, G4. [E] K26. Evidence: d01-d03, d19. Position effects were 6.3 points on MMLU (gpt-3.5) and over 20% in 20-document retrieval QA. Evidence is from 2023-24 models, so measure the current model.
6. **Do not de-bias the model on numeric choice.** Schema: G1, G12. [E] K13, K14. Evidence: a19, c08, b19, c05, a20, c12. Old bias papers do not apply to the current model. Check answers against ground truth, not against human choice.
7. **Select among candidates in code (G5).** Already in the schema; supported here because coverage rises with samples while selection without a verifier plateaus (c22, [S] K09).

### Test first (single-source or contested)

| Item | Schema part | Status | Evidence |
|---|---|---|---|
| Hard threshold vs soft (probabilistic, value-weighted) stop in the candidate loop | G11 | [S] K02 | a12, a13, a14, b23 |
| Adaptive aspiration: raise after quick success, lower after failure | S0, G11 | [S] K01; not found in LLMs K30 | a01, d18 |
| Stop-at-first-discriminating-check in verification vs check-everything | S8, G11 | [S] K04 | a08, a09, b24 |
| Difficulty-gated stop: stop early on easy items, one verify round on hard items | S0, G11 | [C] K06 | b17, c04, d12 |
| One-sample pilot-agreement gate vs prompt-only gate | S0 | [E] K29 direction; comparison not found | d06, d13 |
| Candidate-set size 3, 6, 12, 24 for the selector (choice overload) | S4, S7 | [C] K16, K30 | b02, b04, d04, d05, d03 |
| Cap refine passes at 2 vs 4 | O refine, G2, G5 | [S] K10 | c19 |
| Pruned tree search vs independent samples at equal tokens | O3, S3 | [S] K11 | c20, c25 |
| Verifier-pass stop vs N-sample stop for code | G4, G5 | [S] K09 | c22 |
| Threshold-constrained selection vs weighted-sum selection | G12, S7 | [S] K12 | a21, b15, d15 |
| No-deliberation arm for tasks flagged intuitive | S0, G11 | [S] K15 | c16 |
| Value-of-computation stop: next pass only if expected gain exceeds token cost | S0, G11 | [S] K21 | b25 |
| First-m-finished (short-3@k) vs majority at equal tokens | G11 | [S] K31 | d14 |
| Log stop step and stop type; check whether stop type predicts error | memory, S9 | [S] K22 | b26, b27 |

## 8. Concrete tests on our bench

All tests: both arms at equal total tokens (setup cost counted, G7). Report accuracy by difficulty bin (easy / mid / hard), not only the mean. Use the same items and seeds across arms.

| # | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 | Mixed easy/hard items with checks (math word problems, code with tests, ARC-style items) | A: fixed 3 passes. B: stop at first check pass or two-sample agreement, spare tokens spent on hard items | Accuracy at equal total tokens, by difficulty bin | Same accuracy on easy bin, more on hard bin (literature: 20-85% savings; the reinvestment gain is untested) |
| T2 | Same set | A: stop on consensus. B: stop on consensus plus verifier pass on hard bin | Premature-stop rate, accuracy on hard bin | B recovers part of the 42-55% premature stops [d12] |
| T3 | Same set | A: prompt-only difficulty gate. B: one-sample pilot-agreement gate | Share of hard items sent to the cheap path; accuracy | B misroutes fewer hard items [d13, d06] |
| T4 | Selection among k candidates from the generator | k = 3, 6, 12, 24, equal total tokens | Selector accuracy vs k | Flat or inverted-U; set a cap at the knee |
| T5 | Selection with shuffled order | A: fixed order. B: randomised order plus swapped re-check on near ties | Share of chosen = first-listed vs uniform; accuracy | B removes a few points of bias; effect may be small on current models |
| T6 | Candidate loop with scored attempts | A: hard threshold stop. B: soft probabilistic stop. C: adaptive aspiration | Accuracy and tokens per solved item | Small; run only after T1 |
| T7 | Verification step (S8) with 5 checks of varying diagnostic value | A: run all checks. B: ordered by validity, stop at first decisive check | Verification accuracy; tokens | Tie in accuracy, fewer tokens (G&G pattern); effect may vanish if checks are not independent |
| T8 | Coding items with unit tests | A: N samples then majority. B: stop on verifier pass | Pass@1 at equal tokens | B ahead [c22] |
| T9 | Refinement loop | A: 2 passes. B: 4 passes | Accuracy at equal tokens | Equal, or A ahead (returns shrink by pass three) |
| T10 | Intuitive-flagged items | A: forced CoT. B: short direct answer | Accuracy; tokens | B ahead on flagged items only; no loss on others |
| T11 | Trace logging | Log stopping step and stop type | Stop type vs error | Descriptive; feeds T2 |
| T12 | Threshold-constrained selection | A: weighted sum. B: primary score subject to floors | Primary metric among candidates meeting floors; constraint pass rate | B ahead if floors are meaningful |

## 9. What does not transfer, and why

- **Maximizer scales and unhappiness** (a16, b09, b10, b11, b12): trait self-reports about people's regret and wellbeing. An agent has no regret and no life satisfaction. No outcome-quality measure either [b12].
- **Choice overload and shelf experiments** (jam, chocolates, 401(k)) (b02, b03): driven by effort, anxiety and deferral. The model has no purchase anxiety. The transferable part is the position and set-size effect on a selector, an LLM property to measure directly (T4, T5).
- **Reutskaja's 3-second eye-tracking snacks** (a12-a15): value comes from taste and fixations. The structural lesson (search coverage matters more than selection) is portable; the numbers are not.
- **Take The Best numbers** (a08): one domain, skewed cue structure, binary cues. The .658 vs .657 tie is not a promise for verification steps.
- **Human aspiration, mate search, secretary problem** (a25, d17): need sequential, no-recall choice. Agent samples can be revisited at no information loss.
- **GARP, CCEI and gamble correlations** (a19, b19): show the model is consistent and near expected-value, not that it solves our problems. Consistency is not optimality.
- **Pre-2024 bias papers** (a20, b20, c10, c11): about GPT-3 and GPT-3.5, largely gone in GPT-4-class models [c12].
- **Satisficing alignment numbers** (b15): 7B models, GPT-4 judge, no human raters, no best-of-N arm [d15].
- **Chen's training-based stop** (b17): needs post-training and an answer key. A scaffold can only do inference-time stops.
- **Probe-based stops** (d06, d11): need hidden states, open weights and per-domain training data. Not available with a hosted model.
- **Agreement-based stops under independence assumptions**: the stopping math assumes independent draws; same-model samples are correlated (G4).

## 10. Open questions

1. Does a label-free first-good-enough stop cut tokens at equal accuracy against a fixed-budget baseline at strictly equal tokens, across easy and hard items? Existing numbers are Pareto, not equal-token (K27).
2. Verifier pass versus two-sample agreement as the stop signal: no head-to-head found.
3. Best difficulty probe for S0: pilot sample, logprob, or question features? No comparison on one benchmark.
4. What does a wrong stop cost on hard items where first-correct stopping loses accuracy? PUMA gives 42.4% and 54.8% premature stops, but no fix is tested at equal tokens.
5. Numeric effect of choice overload (no d obtained for Chernev 2015). Does it carry over to LLM option lists? No set-size study varied 3 to 24.
6. How big is first-seen bias for current (2025-26) models selecting among candidates? No opened source.
7. Simon 1955/56 and Todd and Miller 1999 with exact numbers. Never opened. Needs library access.
8. Adaptive aspiration levels in LLM agents: not found. Search was partial (web quota exhausted, Semantic Scholar and OpenAlex rate limited), so "not found" is not "does not exist".
9. Is the "over 92% first solution correct" figure reproduced on code, planning and open QA, and on post-2025 models? Partly (DEER, convergence), not the figure itself.
10. Risk versus uncertainty (Artinger 2022): can we detect it in a task, and do LLM tasks under uncertainty favour simple stops?
11. Calibration of the stop signal under correlated same-model samples (G4). Only within-chain probe calibration measured (ECE below 0.1 in distribution, worse on AIME).
12. Does satisficing alignment hold with human judges and a best-of-N arm at equal samples? The paper used a GPT-4 judge only.
13. Does Reutskaja's smooth stop (K02) improve an agent loop, and does it replicate outside 3-second snack choice?

## 11. Sources

[V] = opened and read this session (as marked in the evidence file). [M] = snippet or abstract only. The cross-check re-opened the items listed at the top of critique.md.

**Founding and theory**
- [V] Simon (1978 Nobel lecture) Rational decision-making in business organizations. https://www.nobelprize.org/uploads/2018/06/simon-lecture.pdf (a01-a05)
- [M] Simon (1955, 1956) founding papers, publisher PDF 403. https://www.uk.sagepub.com/upm-data/25239_Chater~Vol_1~Ch_03.pdf (a06)
- [M] Wikipedia, Satisficing (secondary). https://en.wikipedia.org/wiki/Satisficing (a07)
- [V] Gigerenzer and Goldstein (1996) Reasoning the fast and frugal way. http://www.dangoldstein.com/papers/FastFrugalPsychReview.pdf (a08-a11)
- [V] Czerlinski, Goldstein, Gigerenzer (1999), via Wikipedia Take-the-best, "citation needed". https://en.wikipedia.org/wiki/Take-the-best_heuristic (b24; the Wikipedia page only)
- [V] Reutskaja, Nagel, Camerer, Rangel (2011) Search dynamics in consumer choice under time pressure. https://rnl.caltech.edu/publications/pdf/reutskaja2011.pdf (a12-a15)
- [M] Reutskaja et al. (2011) abstract page. https://www.aeaweb.org/articles?id=10.1257/aer.101.2.900 (b23)
- [V] Reverdy, Srivastava, Leonard (2017) Satisficing in multi-armed bandit problems. https://arxiv.org/abs/1512.07638 (a23)
- [M] Artinger, Gigerenzer, Jacobs (2022) Satisficing: Integrating two traditions. https://www.aeaweb.org/articles?id=10.1257/jel.20201396 and https://doi.org/10.1257/jel.20201396 (a24, d16)
- [M] Todd and Miller (1999). https://doi.org/10.1016/S0749-5978(97)92658-X (a25)
- [M] Selten (1998); Bendor, Kumar, Siegel (2009). https://doi.org/10.2202/1935-1704.1500 (a26)
- [V] Secretary problem (Wikipedia, secondary). https://en.wikipedia.org/wiki/Secretary_problem (d17)
- [V] Keramati, Dezfouli, Piray (2011) Speed/accuracy trade-off between habitual and goal-directed processes. https://pmc.ncbi.nlm.nih.gov/articles/PMC3102758/ (b25; abstract and front matter read closely)

**Choice overload and maximizing**
- [V] Misuraca et al. (2024) review of choice overload moderators. https://pmc.ncbi.nlm.nih.gov/articles/PMC11111947/ (b01-b03, b05-b08; second-hand for the original studies)
- [M] Scheibehenne, Greifeneder, Todd (2010) abstract page. https://academic.oup.com/jcr/article/37/3/409/1827583 (b04)
- [V] Scheibehenne et al. (2010) full text. https://doi.org/10.1086/651235 (d04)
- [M] Chernev, Boeckenholt, Goodman (2015). https://doi.org/10.1016/j.jcps.2014.08.002 (d05)
- [V] Schwartz et al. (2002) Maximizing versus satisficing. https://web.archive.org/web/20231222191322/https://sonjalyubomirsky.com/wp-content/themes/sonjalyubomirsky/papers/SWMLWL2002.pdf (a16, a17)
- [M] Iyengar, Wells, Schwartz (2006). https://doi.org/10.1111/j.1467-9280.2006.01762.x (a18)
- [V] Peng et al. (2018). https://pmc.ncbi.nlm.nih.gov/articles/PMC5808237/ (b09)
- [V] Li, Jia, Wang (2023). https://pmc.ncbi.nlm.nih.gov/articles/PMC10282641/ (b10)
- [V] Oren, Dar, Liberman (2018). https://pmc.ncbi.nlm.nih.gov/articles/PMC5972320/ (b11)
- [V] Shortland, Thompson, Alison (2020). https://pmc.ncbi.nlm.nih.gov/articles/PMC7387631/ (b12)
- [V] Tejeiro et al. (2026). https://pmc.ncbi.nlm.nih.gov/articles/PMC12844959/ (b13)
- [V] Seo, Lee, Lee, Kim (2026). https://pmc.ncbi.nlm.nih.gov/articles/PMC13634898/ (b14)
- [V] Veldwijk et al. (2023). https://pmc.ncbi.nlm.nih.gov/articles/PMC10287580/ (b26)
- [V] Spiliopoulos and Ortmann (2018). https://pmc.ncbi.nlm.nih.gov/articles/PMC5913387/ (b27; abstract and introduction)
- [M] Kang et al. (2026). https://arxiv.org/abs/2605.07789 (b22)

**LLM studies**
- [V] Chen et al. (2023) Emergence of economic rationality of GPT. https://arxiv.org/abs/2305.12763 (a19, c08, c09)
- [V] Binz and Schulz (2023) Using cognitive psychology to understand GPT-3. https://arxiv.org/abs/2206.14576 (a20, c10, c11)
- [M] Suri et al. (2023). https://arxiv.org/abs/2305.04400 (b20)
- [V] Hagendorff, Fabi, Kosinski (2023). https://arxiv.org/abs/2212.05206 (c12)
- [V] Horton, Filippas, Manning (2023) Homo Silicus. https://arxiv.org/abs/2301.07543 (c13, c14; intro and outline only)
- [V] Binz et al. (2025) Centaur. https://arxiv.org/abs/2410.20268 (c15; abstract and data description)
- [V] Liu et al. (2024/25) LLMs assume people are more rational than we really are. https://arxiv.org/abs/2406.17055 and https://arxiv.org/html/2406.17055 (b19, c05-c07)
- [V] Liu et al. (2024) Mind your step (by step). https://arxiv.org/abs/2410.21333 (c16)
- [V] Chen et al. (2024/25) Do NOT think that much for 2+3=? https://arxiv.org/abs/2412.21187 and https://arxiv.org/html/2412.21187 (a22, b17, c01-c04)
- [V] Sui et al. (2025) Stop overthinking: survey. https://arxiv.org/abs/2503.16419 (c23, c24; taxonomy scanned)
- [V] Aggarwal et al. (2023) Adaptive-Consistency. https://arxiv.org/abs/2305.11860 (c17, c18)
- [V] Madaan et al. (2023) Self-Refine. https://arxiv.org/abs/2303.17651 (c19)
- [V] Yao et al. (2023) Tree of Thoughts. https://arxiv.org/abs/2305.10601 (c20, c25)
- [V] Snell et al. (2024). https://arxiv.org/abs/2408.03314 (c21)
- [V] Brown et al. (2024) Large language monkeys. https://arxiv.org/abs/2407.21787 (c22)
- [V] Chehade et al. (2025) Bounded rationality for LLMs. https://arxiv.org/abs/2505.23729 and https://arxiv.org/html/2505.23729v2 (a21, b15, b16, d15)
- [M] Yang et al. (2025) DEER abstract page. https://arxiv.org/abs/2504.15895 (b18); opened version in d10
- [M] Bohnet et al. (2026). https://arxiv.org/abs/2604.02910 (b21)
- [V] Zheng et al. (2024) LLMs are not robust multiple choice selectors. https://arxiv.org/abs/2309.03882 (d01)
- [V] Shi et al. (2024) Judging the judges. https://arxiv.org/abs/2406.07791 (d02)
- [V] Liu et al. (2023/24) Lost in the middle. https://arxiv.org/abs/2307.03172 (d03)
- [V] Damani et al. (2024) Learning how hard to think. https://arxiv.org/abs/2410.04707 (d06)
- [V] Fu et al. (2025) Deep Think with Confidence. https://arxiv.org/abs/2508.15260 (d07)
- [V] Li et al. (2024) Escape sky-high cost (ESC). https://arxiv.org/abs/2401.10480 (d08)
- [V] Liu and Wang (2025) Answer convergence. https://arxiv.org/abs/2506.02536 (d09)
- [V] Zhang et al. (2025) Reasoning models know when they're right. https://arxiv.org/abs/2504.05419 (d11)
- [V] Min et al. (2026) Stop when reasoning converges (PUMA). https://arxiv.org/abs/2605.17672 (d12; May 2026 preprint, not peer reviewed)
- [V] Tan et al. (2025) Zero-step thinking. https://arxiv.org/abs/2510.19176 (d13)
- [V] Hassid et al. (2025) Don't overthink it. https://arxiv.org/abs/2505.17813 (d14)
- [V] Negative search result, arXiv API queries. https://export.arxiv.org/api/query (d18)
