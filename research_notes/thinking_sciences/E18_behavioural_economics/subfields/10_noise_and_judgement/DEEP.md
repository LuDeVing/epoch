# Noise and judgement: deep document

*Subfield E18.10 of behavioural economics. Key work: Kahneman, Sibony, Sunstein (2021) Noise. Built from evidence_a-d.jsonl (a01-a26, b01-b30, c01-c25, d01-d18), claims.jsonl (K01-K26) and critique.md in this folder. Evidence ids in brackets. The Noise book itself was never opened (see section 11).*

Related subfields researched in parallel (links only, not covered here): Judgment and credence aggregation, Social influence on crowds, Self-correction, Test-time compute scaling, Expert judgment and forecasting, LLM forecasting benchmarks, Bounded rationality and satisficing, Confidence and signal-detection measures, Bayesian and causal learning, Probabilistic and test-based reasoning, Evidence accumulation. Earlier documents on debiasing and heuristics sit under E18 and the other fields listed in 00_FIELDS.md.

## 1. What it is

Noise is unwanted variance in judgements that should be the same. Two judges look at one case and give different answers. One judge looks at the same case twice and gives different answers. Neither difference tells us who is right. That is why it is "unwanted": it is spread with no link to truth.

The Kahneman-Sibony-Sunstein framing splits total error into two parts.
- Bias: the average error, all judges leaning the same way.
- Noise: scatter of judgements around their own average.
- Mean squared error = bias squared + noise squared. The book's equation was not on a page we opened (stated from memory, a02). Cutting noise by some amount cuts error as much as cutting bias by the same amount.

Noise has three parts (a02, c21).
- Level noise: judges differ in overall strictness. One judge is harsh on average, another mild.
- Stable pattern noise: a judge reacts to particular case features in a lasting way. This is judge-by-case interaction.
- Occasion noise: the same judge differs from one moment to the next because of passing factors.

System noise squared = level noise squared + pattern noise squared (from memory; the book counts occasion noise inside pattern noise).

Why this matters for our agent. The agent is a scaffold around one model. Every sample the model draws is a "judge". Every verdict step (a critic, a selector, a pairwise compare) is a judgement that can be noisy. The schema already says "code selects" (G5) and "samples from one model are not independent" (G4). This subfield asks four things. How big is the noise in LLM judgement? Where does it come from? What removes it? What can averaging never remove?

Mapping to LLMs (K02; our analogy, not a published decomposition):
- Occasion noise = resampling, re-running the same prompt, batch and hardware jitter.
- Pattern noise = prompt format, example order, option order, criterion order, answer order. These change the model's response to a case in a stable way for that wording.
- Level noise = one model family or persona leaning high or low in scores (strictness, yes-bias).

Nobody has measured this three-way split on an LLM agent. It is a test (UNKNOWNS U1).

## 2. History and theories in depth

**Galton 1907 and the crowd.** Galton compared about 800 guessers of an ox's weight. The median was 1,207 lb against 1,198 lb true (b12; the a24 figure of about 787 usable estimates is from memory). Averaging cancels random error. It does not cancel an error all guessers share. The Condorcet jury theorem needs independent voters better than chance. Both facts matter because LLM samples are not independent (G4). [a24 not opened; b12 via Wikipedia.]

**Meehl 1954, Goldberg 1970, Grove 2000: rules beat judges.** Meehl argued that formulas combining cues beat clinicians. Goldberg (1970, "Man versus model of man", not opened, a07) showed a linear model fitted to a clinician's own judgements predicts the criterion better than the clinician does. This is "bootstrapping": keep the judge's policy, drop the random error. Grove et al. (2000) meta-analysis (abstract opened, d17): mechanical prediction was on average about 10% more accurate than clinical; mechanical was substantially better in 33-47% of studies depending on the analysis; clinical was substantially better in only 6-16%. The advantage held across task, judge type and experience, and clinical did worse when interview data were included. The old memory of "136 studies, 46/48/6 split" was wrong and was removed (critique, K18). A 2016 meta-analysis of lens-model studies (d18, abstract) found linear models of the judge beat the judge on average, more so with objective criteria; correcting for artefacts raised the estimate.

**Kahneman, Rosenfield, Gandhi, Blaser 2016 (HBR) and the noise audit.** Underwriters at a financial firm priced the same five fictive customers. Median premiums differed by 55%, about five times what executives expected (a01, b01; via Wikipedia, HBR paywalled, a04). The "noise audit" method: give many judges the same cases, measure spread. It is cheap and needs no ground truth.

**Noise book 2021.** Kahneman, Sibony and Sunstein extended the audit across fields (all via a Wikipedia summary, a03, b02-b05). Remedy chapter, "decision hygiene" (from memory, a25, c22): (1) structure the judgement into independent sub-judgements (the "mediating assessments protocol"); (2) delay the holistic intuition until after the parts are scored; (3) use anchored scales and rules; (4) aggregate independent judges. None of this was opened or tested on LLMs.

**Kleinberg et al. 2017/2018, machine beats the judge.** NYC bail data (a05, a23, b11). A model trained on cases ranked defendants better than judges. Part of the gap is noise: stricter judges jailed across the whole risk range, not just the riskiest. Detail in section 3.

**The crowd within.** Vul and Pashler (2008) report that averaging two guesses from one person beats either, more so after a delay (b12, b13; primary not opened). Rauhut and Lorenz: asking oneself more than three times may hurt. Herzog and Hertwig: "consider the opposite" beats two plain guesses but not averaging with another person (b12). This is the human analogue of resampling.

**Criticism of the noise programme.** Gelman, Ortmann and Blastland say the idea is not new, that noise is hard to measure without ground truth, and that some variation is useful (b06). Donohoe: less noise can mean more rigidity (a02). The headline occasion-noise study, Danziger et al. 2011 (parole judges, about 65% favourable at session start falling to near 0 before a break; a08, b07, not opened), is contested. Weinshall-Margel and Shapard argue case order is not random. Glockner 2016 simulations say the effect is overstated. Lakens notes the implied effect (odds ratio about 35, d about 1.96) is as large as the male-female height gap (b08, b09). A Ramadan fasting study found the opposite pattern (b10). Treat the "hungry judge" as unproven (K04).

**LLM era (2020-2026).** The same ideas appear under new names.
- Prompt sensitivity (Lu 2022, Sclar 2024, Mizrahi 2024).
- Non-determinism at temperature 0 (Ouyang 2024, Atil 2025, Yuan 2025).
- LLM-judge reliability and bias (Zheng 2023, Wang 2023, Stureborg 2024, Rating Roulette 2025, Lau 2026, Kumar 2026, Norman 2026).
- Averaging fixes: self-consistency (Wang 2023), More Agents (Li 2024), universal self-consistency, mixture-of-agents.
- Limits of averaging: correlated errors across models (Chen 2026, Aitchison 2026, Turkmen 2026, Ding 2026).

## 3. Core findings with exact numbers

Status: Established = two or more independent sources; Single = one source; Contested; "Human, second-hand" = figure comes from a summary of the book, not the primary paper.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Insurance underwriters price the same 5 fictive customers differently | Median premium spread 55%; about five times what executives expected | Kahneman et al. 2016 via Wikipedia [a01, b01] | Human, second-hand |
| Judges sentencing identical vignettes | 208 judges, 16 cases; unanimous prison in only 3 cases; one case mean 1.1 years, one judge gave 15 years | Clancy 1981 via book summary [b03] | Human, second-hand |
| Psychiatrists diagnosing the same patients | 426 hospital patients; agreed on the illness about half the time | Aboraya 2006 via summary [b02] | Human, second-hand |
| Radiologists on mammograms | Miss rate from never to half; false positives 1% to 64% | Beam 1996 via summary [b04] | Human, second-hand (mixes strictness and skill) |
| Interview panels | Panel members disagree on best candidate about 25% of the time | Huffcutt 2013 via summary [b05] | Human, second-hand |
| Bail model beats NYC judges | 24.7% fewer crimes at judges' release rate, or 41.8% fewer jailed at their crime rate; AUC 0.707; 554,689 cases (80% = 443,751 train) from a 758,027-defendant set; national check 151,461 | Kleinberg et al. 2017, NBER w23180 [a05, b11] | Single, strong data; selective labels |
| Stricter judges jail the wrong people | Stricter quintile: +13.0 points jailing, -18.7% crime; risk-ordered detention needs only +6.3 points; full risk ordering would cut crime 32.9% | Kleinberg 2017 [a23, b11] | Single |
| Mechanical beats clinical | About 10% more accurate; substantial win in 33-47% of studies vs clinical 6-16% | Grove et al. 2000 abstract [d17] | Established (human) |
| Linear model of the judge beats the judge | Positive average effect; larger for objective criteria; no effect size read | 2016 lens-model meta-analysis abstract [d18] | Established (human) |
| Hungry judge effect | 65% to near 0% favourable within a session (d about 1.96 implied) | Danziger 2011 [a08, b07-b10] | Contested |
| LLM at temperature 0 not deterministic (accuracy) | Accuracy range across identical runs up to 15%; best-worst gap up to 70%; Mixtral college math best 75%, worst 3%; 5 models, 8 tasks, 10 runs | Atil et al. 2025 [a09, c08] | Established |
| LLM code not deterministic | 829 problems; tasks with no two equal test outputs: 75.76% (CodeContests), 51.00% (APPS), 47.56% (HumanEval); max pass-rate gap 1.00 on 39.63% of HumanEval tasks | Ouyang 2024 [a18, b18] | Established |
| Hardware and batch change greedy output | Up to 9% accuracy variation and 9,000 tokens length difference (R1-Distill-Qwen-7B, bf16) | Yuan 2025 [d14] | Single |
| Prompt format changes accuracy | Up to 76 points (LLaMA-2-13B), about 10 average over 50+ tasks; median spread 7.5 over 10 formats; GPT-3.5 up to 56, median 6.4 over 320 formats; not removed by scale, shots, tuning | Sclar 2024 [a11, a12] | Established |
| Instruction paraphrase reorders models | 6.5M instances, 20 LLMs, 39 tasks; Kendall W 0.71-0.91 | Mizrahi 2024 [a13] | Established |
| Example order in few-shot | Near-SOTA to near-chance; 0.1B to 175B; entropy ordering +13% relative over 11 tasks | Lu et al. 2022 [a14] | Single |
| Option letter bias | llama-30B +15.2 points when the answer sits at its preferred option (68.2 vs gpt-3.5 65.3); 20 LLMs | Zheng 2024 [b21, c14] | Established |
| Judge position consistency | GPT-4 65.0%, GPT-3.5 46.2%, Claude-v1 23.8%; Claude-v1 prefers first 75.0%; few-shot lifts GPT-4 to 77.5% (about 4x cost); GPT-4 vs human 85% vs human-human 81% | Zheng 2023 [a16, b16] | Established |
| Order alone crowns either model | ChatGPT judge: Vicuna-13B beats ChatGPT 66/80 (82.5%) in one order, 2.5% in the other; GPT-4 judge 51.3% vs 23.8%; calibration lifts GPT-4 agreement with humans 52.7% to 62.5% (+9.8%), ChatGPT +14.3%; with 20% human review 73.8% | Wang 2023 [a15, b17, c10] | Established |
| Judge self-inconsistency, same input | Krippendorff alpha over 3 runs: SummaC 0.326 / 0.628 / 0.788 (Llama-3.1-70B, R1-Distill, Qwen3-32B); MT-Bench 0.265 / 0.507 / 0.563; Qwen3 same judgement on all 3 runs only 61.3% | Rating Roulette 2025 [c01] | Established (with Stureborg, Lau, Kumar) |
| GPT-4 self-agreement below human agreement | Inter-sample alpha 0.587 vs human inter-annotator 0.659 (SummEval); anchoring across attributes r = 0.979 for GPT-4 vs 0.315 for humans | Stureborg 2024 [a17, b15, c13] | Single |
| Judge flips on rerun and order | 7-17% of verdicts change across identical reruns at temp 0; up to 98% flip on order swap; one judge 100% repeat-stable but 51% accurate; 6 judges incl. GPT-5.2, Claude-Sonnet-4.6 | Kumar 2026 [d07] | Established (with Norman, Lau) |
| Retest high, position bias high | 21 judges, 541,000 judgements; exact-match overstates kappa by 33-41 points on MT-Bench; retest >0.95 with position bias >0.10; verbosity bias <0.011 | Norman 2026 [d09] | Single |
| Claude judges and temperature | Temp 0 cuts spread for GPT and Gemini, barely for Claude; Haiku completeness SD higher at temp 0 | Lau 2026 [c05, c06] | Single |
| Rubric order flips the winner | Criterion order alone flips top-1 on 15-41% of prompts; a few random orders suffice | Xu 2026 [d11] | Single |
| Clinical agent self-disagreement | 8.7% of replicate pairs (2.2% ICU escalation to 17.9% controlled-substance caution); six models 2.5-23.7%, not ordered by size or vendor | Bellibatlu 2026 [d10] | Single (synthetic vignettes) |
| Temperature does not change mean accuracy | H(10) = 10.439, p = 0.403, 9 LLMs, temps 0-1.0 | Renze 2024 [a19] | Single |
| Self-consistency | Over greedy CoT: GSM8K +17.9 (PaLM-540B 56.5 to 74.4), SVAMP +11.0, AQuA +12.2, StrategyQA +6.4, ARC-c +3.9; 40 paths; AddSub only +1.8 | Wang 2023 [a20, b22, c15] | Established |
| Sample-and-vote | GSM8K +12 to +24, MATH +6 to +10, MMLU +5 to +11, HumanEval +4 to +9, Chess +1 to +4; Llama2-13B ensemble 59 beats Llama2-70B 54 | Li 2024 [b23] | Established (with self-consistency) |
| Majority of 3 judge runs | SummaC balanced accuracy single mean / majority of 3 / sampling off: Llama 59.1 / 61.4 / 58.4; DeepSeek 69.8 / 72.3 / 69.3; Qwen3 79.4 / 80.6 / 79.2; 5 or 10 runs add nothing significant | Rating Roulette [c02] | Single |
| Few-shot and CoT do not raise judge self-agreement | alpha change <0.01 with few-shot; CoT fell slightly | Rating Roulette [c03] | Single |
| Majority of 5 removes only part of the floor | 39% of the self-disagreement floor (95% CI 18-64) | Bellibatlu 2026 [d10] | Single |
| LLM crowd matches human crowd on forecasts | 12 LLMs vs 925 humans, 31 questions: Brier 0.20 vs 0.19, p = .850; vs no-information 0.25, p = .026; equivalence bound only 0.081; mean forecast 57.35% (acquiescence) | Schoenegger 2024 [a21, b26] | Established |
| Forecast ensemble gain is small | Halawi: system Brier .179 vs crowd .149 (accuracy 71.5 vs 77.0); ablation none .1676, median .1651, mean .1656, USC .1691 | Halawi 2024 [b27] | Established |
| Mixture-of-Agents | AlpacaEval 2.0 LC 65.1% (open-source) / 65.8% (GPT-4o aggregator) vs 57.5% GPT-4o | Wang 2024 [b25, c18] | Single (LLM-judged) |
| Agreement is a weak confidence signal | Spearman 0.20-0.59 with majority-correctness; shared wrong answers agreement 0.85 (GPT) / 0.78 (Claude); 53 runners, K=50, 265,000 samples; Claude check small (12 shared-wrong items) | Ding 2026 [d03] | Single |
| Co-failure ceiling | No vote/router beats 1 minus delta; delta 0.052 vs 0.023 predicted (open maths); 0.079 code; 0.127 free-response GPQA; 67 frontier models | Chen 2026 [d04] | Established direction (3 papers) |
| Diverse ensembles beat repeated one-model | Best fixed-budget forecast mix never all one model | Aitchison 2026 [d05], Turkmen 2026 [d06] | Established direction |
| Sequential beats parallel at equal tokens | 43 of 45 configs (95.6%); 4096-token chains, 6 chains = 24,576 tokens; largest AIME-2025 Qwen3-235B 76.7% vs 30.0%; many gaps tiny (61% vs 60%) | Sequential Edge 2025 [d01] | Single |
| Debate/MoA beat self-consistency at equal compute | MMLU-Pro: CoT 64.3, SC 68.7, debate 70.0, MoA 71.4; at equal budget debate +1.3, MoA +2.7 | Wunderlich 2026 [d02] | Single |
| Pairwise noise sits in near ties | Position bias, transitivity violations, self-agreement dominated by close-rank pairs | Brocai & Becker 2026 [d12] | Single |
| Decomposed judging did not beat holistic | FLASK did not beat G-Eval for pairwise judging | Kumar 2026 [d08] | Single |

## 4. Mechanisms and models

Each model below is written so it can be coded.

**4.1 Variance decomposition (the audit).**
- Input: a set of items and conditions along three axes: seeds (S), prompt or format variants (P), models or personas (M).
- Run every item under a grid of conditions. Record the scored outcome y (correct 0/1, score, verdict).
- Total variance of y per item = variance of the mean over M (level) + variance over P within M (pattern) + variance over S within P and M (occasion). Use nested means or a random-effects ANOVA.
- Report as fractions. If occasion is largest, resample and vote. If pattern is largest, vary format and aggregate over formats. If level is largest, diversify models or calibrate scores against a reference.
- For binary verdicts use self-disagreement rate = share of replicate pairs that differ (Bellibatlu's "floor", d10) and Krippendorff alpha over R runs (c01). Do not use exact-match percent: it overstates chance-corrected agreement by 33-41 points (d09).

**4.2 Noise reduction by averaging, and where it stops.**
- Let each sample have error e_i = b + n_i, where b is shared bias and n_i is independent noise with variance s^2. The mean of k samples has error b + mean(n_i) with variance s^2/k. Noise shrinks like 1/k. Bias b does not shrink.
- With correlation r between sample errors, variance of the mean = s^2 (1 + (k-1) r) / k. As k grows this tends to r s^2, a floor. High r (same model) means a high floor.
- For voting on a discrete answer, accuracy is capped by 1 minus the rate at which all voters are wrong together (Chen's delta, d04). The measured delta (0.052 against 0.023 under independence) means the cap is real and worse than an independence model predicts.
- Implementation: on a held set of items, compute the empirical all-wrong rate across N samples. That is the ceiling on voting gain from more samples.

**4.3 Balanced presentation (code-side permutation).**
- Pairwise compare (A vs B): run (A,B) and (B,A). Count a verdict only if both orders agree; otherwise declare a tie and escalate. The accuracy ceiling from position bias alone is 1 minus flip-rate/2 (d07).
- Multiple choice: run n cyclic permutations of the options in code and sum votes per option content, not per letter. PriDe (b21) estimates the label prior from a few permuted samples and corrects the rest more cheaply.
- Rubric scoring: shuffle criterion order, take the median over 3 orders (d11). A few random orders match a full balanced set.
- Few-shot examples: shuffle order per sample (a14).

**4.4 Near-tie handling.** Stratify the reliability metric by score gap (d12). If two candidates are within a margin, spend more samples or use a coded tie-break (shortest, symmetry, test result). Do not spread samples evenly.

**4.5 Mediating assessments protocol (untested on LLMs).**
- Define 3-6 independent sub-criteria in advance. Score each in a fresh call that sees no other score. Aggregate the sub-scores by code (mean or fitted weights). Only then, optionally, add a holistic call and combine by fixed rule.
- Related human result: a fitted linear model on cue scores beats the holistic judge (a07, d17, d18). For an LLM this means: extract cues with the model, combine them in code.
- Warning: FLASK-style decomposition did not beat a single multi-criterion prompt in Kumar 2026 (d08). The design differs (a decomposed rubric judge, not independent fresh calls), so the protocol is still open (K25).

**4.6 Self-agreement as an allocation signal.** Compute the agreement of k samples. Use low agreement to route extra samples or a check. Never use high agreement to accept an answer without a check (Spearman only 0.20-0.59, d03; frontier models agree on shared wrong answers at 0.78-0.85).

**4.7 Equal-token arms.**
- Parallel vote: k chains of L tokens each, final answer by majority.
- Sequential: k chains where each sees the previous attempt, total k*L tokens (d01).
- Verifier: one chain of L tokens plus a verifier call (and optionally a retry).
- Compare at identical total tokens, setup included. G7 already demands this. Almost no published noise study does it (critique weak spots).

## 5. What holds up

**Holds up (two or more sources, direction stable).**
- LLM outputs vary across identical runs even at temperature 0 (Atil, Ouyang, Rating Roulette, Lau, Kumar, Yuan). Sources of variation: batching, kernel non-invariance, floating point order (a09, d14, d16).
- Prompt format, example order, option order and answer order change results by large amounts, and size, shots and tuning do not remove it (Sclar, Lu, Zheng 2024, Mizrahi).
- Pairwise LLM judges flip with order swap (Zheng, Wang, Shi, Kumar). Measured on models from GPT-3.5 and Claude-v1 up to GPT-5.2 and Claude-Sonnet-4.6, so it is not only an old-model effect.
- Voting and sampling reduce noise and raise mean accuracy (self-consistency, More Agents, Rating Roulette majority of 3).
- Mechanical combination of cues beats clinical judgement in humans (Grove abstract; Kleinberg data).
- Averaging does not remove shared bias (Schoenegger acquiescence; Chen, Aitchison, Turkmen, Ding).

**Replications and failures.**
- Danziger hungry-judge: not replicated; critiques and a contrary Ramadan result (K04). Do not cite as established.
- The old verbosity bias (20-40% variance reported in 2023) is below 0.011 for 21 current judges (d09). Some judge biases have shrunk; position bias has not.
- Chiang and Lee 2023 (abstract only, b29) say LLM ratings are stable and agree with experts on stories. Stureborg and Rating Roulette find low self-agreement. Tasks, models and metrics differ. Unresolved.
- Temperature: mean accuracy flat across 0-1.0 (Renze) yet run-to-run spread is large (Atil). Mean versus variance, not a conflict.
- Temperature 0 helps GPT and Gemini judges, barely helps Claude judges (Lau); sampling off did not fix Rating Roulette models. Model-dependent.
- Majority of 3 helps but 5 or 10 do not add significantly (Rating Roulette), while Bellibatlu finds 5 removes only 39% of the floor (CI 18-64). Both say returns diminish fast.

**Moderators.**
- Task difficulty: voting gains are small on easy tasks (AddSub +1.8) and rise with difficulty then fall (b23). Debate/MoA gains by difficulty: easy +2.2, medium +8.5, hard +9.0 (d02).
- Output length: longer free-form outputs are less stable; accuracy and stability correlate positively (a10).
- Quality gap: position bias is stronger when candidate quality is close (Shi, d13; Brocai, d12).
- Model: self-disagreement is not ordered by size or vendor (d10).

**Interventions that worked.**
- Both-order judging and multiple evidence runs: GPT-4 human agreement 52.7% to 62.5% (Wang).
- Few-shot judge prompt: GPT-4 position consistency 65.0% to 77.5% at about 4x cost (Zheng).
- Majority of 3 judge runs: +1.0 to +2.5 balanced accuracy points (Rating Roulette).
- Self-consistency and sample-and-vote (section 3).
- Option permutation or PriDe for multiple choice.
- Mixing different models: diverse ensembles beat same-model ones at matched quality (d04, d05).
- FP32 compute pipeline (LayerCast) reduces numerical non-determinism (d14).

**Interventions that did not work, or have no support.**
- Few-shot and CoT as ways to raise judge self-agreement (c03).
- Greedy decoding in place of sampling-plus-vote (c02).
- High self-agreement as a stopping rule (d03). The informal 85% rule has no support (c24, d03, d12).
- 5 or 10 samples over 3 for judges (c02).
- Decomposed rubric judging over holistic (d08, one source).
- Scale: a larger model is not less noisy on format sensitivity (Sclar).

## 6. Language models

**Run-to-run noise on identical input.** Atil: accuracy range up to 15% across 10 identical temperature-0 runs; best-minus-worst up to 70%. Ouyang: up to 75.76% of CodeContests tasks have no two equal test outputs. Kumar (2026; GPT-5.2, GPT-4o, Gemini-2.5-Pro, Gemini-2.0-Flash, Claude-Sonnet-4.6, Llama-3.3-70B): 7-17% of verdicts change across identical reruns at temperature 0. Bellibatlu: a clinical agent changes its action in 2.5-23.7% of replicate pairs across six models. Yuan: hardware and batch size alone move a reasoning model's accuracy by up to 9%. Long reasoning chains amplify tiny numeric differences.

**Prompt and presentation noise.** Format changes: up to 76 points (LLaMA-2-13B), about 10 on average. GPT-3.5 up to 56 points over 320 formats. Example order: near chance to near state of the art. Option letter: +15.2 points for llama-30B at its preferred slot. Rubric order: top-1 flips on 15-41% of prompts. Most format data are from open and older models. There is no result for Claude 4/5-class or GPT-5-class on format sensitivity (critique weak spots).

**Judge noise.** Position consistency: Claude-v1 23.8%, GPT-3.5 46.2%, GPT-4 65.0%; with few-shot GPT-4 77.5%. Up to 98% of pairwise verdicts flip on order swap in the 2026 frontier set. Judge self-agreement alpha 0.265-0.788. GPT-4 inter-sample alpha 0.587 below human 0.659. Human-human MT-Bench alpha is only 0.478, so humans are noisy too. Retest above 0.95 coexists with position bias above 0.10, and one judge was 100% repeat-stable but 51% accurate. Agreement across repeats is therefore not a health check.

**What reduced it, and by how much.**
- Swap order and aggregate: GPT-4 human agreement 52.7% to 62.5%.
- Majority of 3 runs: +1.0 to +2.5 balanced accuracy points.
- Self-consistency: +3.9 to +17.9 points over greedy CoT, at k-times cost.
- Sample-and-vote: +12 to +24 on GSM8K; a 13B ensemble beat a 70B single model.
- Forecasting: 12-model crowd Brier 0.20 against 0.25 for no information, equal to 925 humans; Halawi's ensemble gain was only about 0.003 Brier.
- Majority of 5 in a clinical agent: 39% of the floor removed.

**What did not change it.** Model size, shots, instruction tuning (format spread); CoT and few-shot (judge self-agreement); temperature (mean accuracy; also little effect on Claude judge variance); asking one model many times (shared errors).

**Equal-token evidence (thin).**
- Sequential refinement beat parallel vote in 43 of 45 open-model configurations at equal tokens (d01). Caveats: 4096-token cap, AIME has 30 items (one item = 3.3 points), no Claude or GPT-5 model, many gaps tiny.
- Debate and MoA beat self-consistency by 1.3-2.7 points on MMLU-Pro at equal compute on Llama 3.1 70B (d02). Non-reasoning open model; two benchmarks.
- Self-consistency "saturates early" (d02).
- The big self-consistency and More Agents gains were all at k-times the cost of the baseline.

**Cross-model correlation.** 67 frontier models: all-wrong rate 0.052 against 0.023 predicted by independence (Chen). Diverse ensembles beat Self-MoA at matched quality. The best fixed-budget forecast ensemble never used one model. All of this is across models. Across prompts or personas of one model is unmeasured.

**Human versus LLM spread.** No paper measures LLM noise on a professional task against human professionals. The clinical-agent audit has no human baseline. Human-human alpha 0.478 on MT-Bench and 0.659 on SummEval give a rough anchor.

## 7. What our agent should take

Format per item: schema part, status, evidence ids. [E] established, [S] single-source, [C] contested.

### Add now (established)

1. **Judge pairwise comparisons in both orders in code and count only agreeing verdicts; escalate disagreements.** Part: G4/G5, S7. [E] K09, K22. Evidence a15, a16, b17, c10, d07, d13.
2. **Permute option order in code for any multiple-choice or ranked slot and aggregate by content.** Part: G5, S3/S7. [E] K08. Evidence b21, c14.
3. **Treat every single model verdict as one noisy sample.** Do not use one judge call as an oracle; aggregate in code (vote, median) or replace with a check. Part: G5. [E] K05, K10, K22. Evidence a09, a18, c01, c05, d07, d10.
4. **Do not use "the verdict repeats" as a health check.** A judge can repeat 100% and be 51% right; retest above 0.95 can sit with position bias above 0.10. Part: G4. [E] K22. Evidence d07, d09.
5. **Measure the noise floor before comparing any two arms.** Run 20 items x 10 reruns on our own stack and report per-item ranges; report results across several prompt paraphrases, not one. Part: G7 (bench). [E] K05, K24, K06. Evidence a09, d10, d14, a11, a13.
6. **Voting removes noise, not bias.** Keep G4 as it stands. Add: use agreement to allocate extra samples, never to accept. Part: G4. [E] K13, K21 for shared bias; [S] K20 for the weak-signal numbers. Evidence a21, d03, d04, d05.
7. **Cost note: voting gains are large only at k-times cost.** Any use must pass G7 at equal tokens. Part: G7. [E] on the gain; no equal-token evidence on frontier models. Evidence a20, b23.

Low-cost hygiene, single-source [S]:
8. **Score items independently, each in a fresh call, not several attributes in one output.** GPT-4 anchored on its own earlier scores (r = 0.979 vs 0.315 for humans). Part: S4/S7 judge steps; matches the S3 fresh-context rule. Evidence a17, c13.
9. **Prefer short constrained output slots over long free-form text in judgement steps.** Instability grows with output length (correlational). Part: G11/slot design. Evidence a10.

### Test first

10. **Replace a model-judged step with a coded rule over extracted cues (bootstrapping).** Part: G5, S7. [E] for humans; no LLM test (K18, K03). Evidence a05, a07, d17, d18.
11. **Mediating assessments protocol: independent sub-judgements in fresh calls, coded aggregate, holistic call last.** Part: G4, O3, S4/S7. [S]. No LLM test; FLASK was null (K25). Evidence a25, c22, d08.
12. **Equal-token comparison: k short chains + vote vs one long chain vs one chain + verifier.** Part: G11, G12, S3. [S] K19. Evidence d01, d02, a20, b23.
13. **Prompt or persona diversity versus repeated sampling at equal tokens.** Part: G4 (the rule "no persona voters on single-answer problems" may need a diversity exception; test), S3. [S] K21 (evidence is across models only). Evidence d04, d05, d06.
14. **Random criterion order, median over 3 orders, for any rubric judge.** Part: S4 judge steps. [S] K23. Evidence d11.
15. **Near-tie routing: extra samples or a coded tie-break on pairs close in score.** Part: G12, S7. [S] K26. Evidence d12, d13.
16. **Two guesses from one model with different framings (crowd within).** Part: O-resample. [S] K17. Evidence b12, b13.
17. **Self-agreement threshold and number of samples.** No principled rule exists. Calibrate on our own data. [S] K20. Evidence d03, d10, c02.
18. **Late-in-context degradation (analogue of hungry judge).** No test exists. Part: G11/S9. [C] K04. Evidence b07-b10, d14.

Nothing in Test first moves into SCHEMA.md until its test passes (see UNKNOWNS.md).

## 8. Concrete tests on our bench

All arms at equal total tokens, setup included (G7). Report per-item ranges and paired differences, not only means.

| # | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 Noise audit | 20 items per benchmark (ARC-style grids, BRAINTEASER) x 10 reruns | Default run at temp 0, plus 3 prompt paraphrases x 10 seeds | Self-disagreement rate, alpha, per-item accuracy range; variance split level/pattern/occasion | Occasion spread 5-15 points on some items; pattern spread larger (Sclar); tells us which fix to buy |
| T2 Both-order judge | 100 pairs from our selector or critic outputs, incl. near ties | A: single order. B: both orders, count agreement only, tie to coded tie-break | Pairwise accuracy vs known-better answer; flip rate | Flip rate 10-35% for single order; B lifts accuracy a few points (Wang +9.8 for GPT-4) |
| T3 Vote vs long vs verifier | Checkable items, tiered by difficulty | A: k x L-token chains + vote. B: one k*L-token chain. C: one chain + verifier + one retry | Accuracy at fixed total tokens | Sequential/verifier arm wins on hard items (d01); vote gains little on easy ones; unknown on frontier closed models |
| T4 Diversity vs repetition | 100 items, N=5 samples | A: 5 same-prompt samples. B: 5 paraphrases. C: 5 personas. D: mixed models if available | Accuracy; pairwise error correlation; all-wrong rate | If error correlation is lower in B/C, they beat A by a few points; if not, G4 "no persona voters" holds |
| T5 Coded rule vs LLM verdict | One scaffold step where the model picks (e.g. S7 select) | A: holistic LLM verdict. B: model extracts 3-6 cues in fresh calls, code combines by fixed or fitted rule | Selection accuracy vs best candidate available | B equal or better (human mechanical edge about +10%) |
| T6 Mediating protocol | Open-mode candidate solutions | A: holistic score. B: independent sub-scores in fresh calls, holistic last, coded merge | Agreement with check outcome; self-agreement over 5 reruns | Higher self-agreement, accuracy uncertain; FLASK null is a warning |
| T7 Criterion/option order | Rubric judge and MC items | A: fixed order. B: random order, median of 3. C: full permutation | Top-1 flip rate; accuracy | B close to C at lower cost (d11); both beat A |
| T8 Late-in-run degradation | Same sub-task at position 1, 10, 30 of a long agent run | Fresh context vs same sub-task late in long context | Accuracy and flip rate by position | Unknown; null is plausible |
| T9 Self-agreement as router | Checkable items | A: fixed k. B: adaptive k (extra samples when agreement is low) | Accuracy per token | B beats A; accept-on-agreement alone loses on hard items |
| T10 Sample count | Judge steps | 1 vs 3 vs 5 judge samples (median or majority) | Accuracy, alpha | 3 captures most; 5 adds little (c02); verify on Claude-class models |

## 9. What does not transfer, and why

- **Human noise sizes.** The 55% insurer spread, the 208-judge sentencing and the psychiatrist figures come through a summary of the book (K01). They show noise exists in humans. They say nothing about its size in LLMs. We must measure our own.
- **Hungry judge and fatigue.** Contested in humans; LLMs have no hunger. The only analogue is context length or run position, which is untested (T8).
- **Mood and weather.** Single-study human effects (a03). No LLM analogue except sampling randomness.
- **"Independent judges" in the crowd model.** Galton, Condorcet and the Noise book assume independence. LLM samples from one model are not independent, and even different frontier models fail together (delta 0.052). The human playbook "add more judges" works worse here.
- **Training judges.** Human noise falls with training and aids. A frozen model learns nothing between calls. What transfers is structure: scales, rules, checklists, sub-judgements. Bias checklists and debiasing instructions did not help (schema 4b).
- **Decision hygiene as prompt wording.** "Delay your intuition" as an instruction is just a prompt change, and the schema rejects unstructured self-reflection (4b). The mediating protocol only transfers if sub-judgements are separate fresh calls and code does the merge.
- **Debate.** Wunderlich 2026 (d02) finds debate and MoA beat self-consistency by 1.3-2.7 points at equal compute on Llama 3.1 70B. G9 says debate does not beat plain voting at matched cost. Both can stand: d02 is non-reasoning open models on two benchmarks, and the larger gains cost up to 20x CoT tokens. It is a reason to test (T3, T4), not to reverse G9.
- **Rules over judges (Kleinberg, Grove).** Large human result. In the bail data, outcomes are seen only for released defendants (selective labels) and judges may weigh other goals. For an LLM, "rule over cues" needs reliable cue extraction, itself a noisy model step. The gain is unmeasured.
- **Older-model numbers.** Most format, position and self-consistency figures are for GPT-3.5, GPT-4, Llama-2 and Claude-v1. Newer judges (2026) still flip, but sizes differ (verbosity bias is gone, position bias remains).
- **Mean accuracy.** Temperature does not change mean accuracy (Renze), so turning temperature down does not fix noise.

## 10. Open questions

1. At equal tokens, do k short chains + vote beat one long chain or chain + verifier on current frontier models (Claude 4/5-class, GPT-5-class)?
2. How large are run-to-run and prompt-format noise on current Claude models in our harness? Lau finds Claude barely responds to temperature 0.
3. Does the mediating assessments protocol reduce variance or raise accuracy for LLM judgement? No direct test.
4. Are errors from different prompts or personas of one model less correlated than repeated samples? No measurement.
5. Which verdict style is worst in an agent loop, and does coded aggregation recover accuracy cheaply?
6. Do coded rules over extracted cues beat an LLM holistic verdict?
7. Do LLM noise audits exist in medicine, law, finance or underwriting, and how do they compare with human spread?
8. Does context length or run position raise occasion noise?
9. How many samples give a stable majority per item, and what agreement level justifies acceptance?
10. Does shared bias (acquiescence, order, verbosity) survive coded debiasing?
11. Primary numbers for Goldberg 1970, Grove (full text, study count), Vul and Pashler 2008, Galton and the Noise book audits were never opened.
12. What causes non-determinism on hosted APIs (batching, co-mingled inputs)? Not isolated.

## 11. Sources

[V] = opened and read (full text, HTML or PDF; "abstract" or "secondary" where marked). [M] = snippet, memory or abstract-level only. Several primary human studies appear only through the Wikipedia summary of the book, so their figures are second-hand.

Human noise and judgement
- [V, secondary] Kahneman, Sibony, Sunstein (2021) Noise, Wikipedia summary. https://en.wikipedia.org/wiki/Noise:_A_Flaw_in_Human_Judgment (a01-a03, b01-b06)
- [M] Kahneman et al. (2021) Noise, publisher page; decision hygiene from memory. https://www.hachettebookgroup.com/titles/daniel-kahneman/noise/9780316451390/ (a25, c21, c22)
- [V, paywalled, lede only] Kahneman, Rosenfield, Gandhi, Blaser (2016) HBR Noise. https://hbr.org/2016/10/noise (a04)
- [V] Kleinberg et al. (2017) Human decisions and machine predictions, NBER w23180. https://www.nber.org/papers/w23180 (a05, a23, b11); [M] QJE version https://doi.org/10.1093/qje/qjx032 (c23)
- [V, abstract] Grove et al. (2000) via Europe PMC. https://europepmc.org/article/MED/10752360 (d17); [M] https://doi.org/10.1037/1040-3590.12.1.19 (a06, b14)
- [M] Goldberg (1970) Man versus model of man. https://doi.org/10.1037/h0029230 (a07)
- [V, abstract] 2016 meta-analysis, success of linear bootstrapping models. https://europepmc.org/search?query=%22Success%20of%20Linear%20Bootstrapping%20Models%22 (d18)
- [M] Danziger, Levav, Avnaim-Pesso (2011) PNAS. https://doi.org/10.1073/pnas.1018033108 (a08, b07)
- [V, secondary] Hungry judge effect, Wikipedia. https://en.wikipedia.org/wiki/Hungry_judge_effect (b07-b10)
- [V] Lakens (2017) Impossibly hungry judges. https://daniellakens.blogspot.com/2017/07/impossibly-hungry-judges.html (b09)
- [V, secondary] Wisdom of the crowd, Wikipedia. https://en.wikipedia.org/wiki/Wisdom_of_the_crowd (b12)
- [M] Vul and Pashler (2008) Measuring the crowd within. https://doi.org/10.1111/j.1467-9280.2008.02136.x (b13)
- [M] Galton (1907) Vox populi. https://doi.org/10.1038/075450a0 (a24)

LLM noise, prompt and judge studies
- [V] Atil et al. (2025) Non-determinism of deterministic LLM settings. https://arxiv.org/abs/2408.04667 (a09, a10, b19, c08)
- [V] Ouyang et al. (2024) Non-determinism of ChatGPT in code generation. https://arxiv.org/abs/2308.02828 (a18, b18)
- [V] Renze (2024) Effect of sampling temperature. https://arxiv.org/abs/2402.05201 (a19)
- [V] Sclar et al. (2024) Spurious features in prompt design. https://arxiv.org/abs/2310.11324 (a11, a12, b20, c09)
- [V] Mizrahi et al. (2024) State of what art? https://arxiv.org/abs/2401.00595 (a13)
- [V] Lu et al. (2022) Fantastically ordered prompts. https://arxiv.org/abs/2104.08786 (a14)
- [V] Zheng et al. (2024) LLMs are not robust multiple choice selectors. https://arxiv.org/abs/2309.03882 (b21, c14)
- [V] Wang et al. (2023) Large language models are not fair evaluators. https://arxiv.org/abs/2305.17926 (a15, b17, c10)
- [V] Zheng et al. (2023) Judging LLM-as-a-judge. https://arxiv.org/abs/2306.05685 (a16, b16, c12)
- [V] Stureborg et al. (2024) Inconsistent and biased evaluators. https://arxiv.org/abs/2405.01724 (a17, b15, b30, c13)
- [V] Rating Roulette (2025). https://arxiv.org/html/2510.27106 (c01-c04)
- [V, figures] Lau (2026) Same input, different scores. https://arxiv.org/pdf/2603.04417 (c05, c06)
- [V] Schroeder and Wood-Doughty (2025) Can you trust LLM judgments? https://arxiv.org/pdf/2412.12509v2 (c07)
- [M, abstract] Shi et al. (2024/2025) Judging the judges, position bias. https://arxiv.org/abs/2406.07791 (c11, d13)
- [M, abstract] Chiang and Lee (2023) Can LLMs be an alternative to human evaluation? https://arxiv.org/abs/2305.01937 (a26, b29)
- [M, snippet] Practitioner 85% self-agreement heuristic. https://dev.to/gabrielanhaia/every-llm-eval-library-has-the-same-bug-stochastic-judges-used-as-deterministic-oracles-16o8 (c24)
- [V] Kumar, Rathore, Moitra (2026) All verdicts are not equal. https://arxiv.org/abs/2610.12083 (d07, d08)
- [V] Norman, Rivera, Hughes (2026) Reliability without validity. https://arxiv.org/abs/2606.19544 (d09)
- [V] Bellibatlu et al. (2026) Instability floors. https://arxiv.org/abs/2609.03221 (d10)
- [V] Xu et al. (2026) Position bias in rubric scoring. https://arxiv.org/abs/2602.02219 (d11)
- [V] Brocai and Becker (2026) Pair difficulty matters. https://arxiv.org/abs/2609.37577 (d12)
- [V] Yuan et al. (2025) Numerical sources of nondeterminism. https://arxiv.org/abs/2506.09501 (d14)
- [V] Nicholson (2026) Nondeterministic drift. https://arxiv.org/abs/2601.19934 (d15)
- [V] Messina and Scotta (2026) Background temperature. https://arxiv.org/abs/2604.22411 (d16)

Aggregation, voting, forecasting
- [V] Wang et al. (2023) Self-consistency. https://arxiv.org/abs/2203.11171 (a20, b22, c15)
- [V] Li et al. (2024) More agents is all you need. https://arxiv.org/abs/2402.05120 (b23, c16)
- [M, abstract] Chen et al. (2023) Universal self-consistency. https://arxiv.org/abs/2311.17311 (b24, c17)
- [V] Wang et al. (2024) Mixture-of-Agents. https://arxiv.org/abs/2406.04692 (b25, c18)
- [V] Schoenegger et al. (2024) Wisdom of the silicon crowd. https://arxiv.org/abs/2402.19379 (a21, b26, c19)
- [V] Halawi et al. (2024) Approaching human-level forecasting. https://arxiv.org/abs/2402.18563 (b27, c20)
- [V] Schoenegger et al. (2024) AI-augmented predictions. https://arxiv.org/abs/2402.07862 (b28)
- [V] Sequential Edge (2025). https://arxiv.org/abs/2511.02309 (d01)
- [V] Wunderlich et al. (2026) Multi-agent reasoning compute efficiency. https://arxiv.org/abs/2605.01566 (d02)
- [V] Ding (2026) When LLMs agree, are they right? https://arxiv.org/abs/2607.08065 (d03)
- [V] Chen (2026) Co-failure ceiling. https://arxiv.org/abs/2606.27288 (d04)
- [V] Aitchison et al. (2026) Diversity is the strength of the AI crowd. https://arxiv.org/abs/2606.29661 (d05)
- [V] Turkmen et al. (2026) Don't always pick the highest-performing model. https://arxiv.org/abs/2602.08003 (d06)

## Source audit (2026-11-01)

Fresh auditors re-opened the sources of 11 established claims: 7 confirmed as written, 4 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **E18.10-K05** (reworded: the sources support less). The ChatGPT code figures (75.76%/51.00%/47.56% of tasks with zero equal test output) are at the default temperature (1), not temperature 0, where non-determinism is lower but not zero; they also refer to equal test output, not equal text. Corrected claim: LLMs configured to be deterministic (temperature 0) still vary: across 5 models, 8 tasks and 10 runs accuracy varies up to 15% across identical runs and the best-possible to worst-possible gap reaches up to 70% (Atil et al.). Separately, at ChatGPT's default temperature (1), 75.76%, 51.00% and 47.56% of CodeContests, APPS and HumanEval tasks had zero equal test output across five requests, and temperature 0 reduces but does not remove this (Ouyang et al.).
- **E18.10-K06** (number corrected). Sclar figures verified (76 points LLaMA-2-13B, ~10 average, 50+ tasks), but Mizrahi et al. Table 4 shows Kendall's W spanning about 0.27 to 0.91 across tasks, with most below 0.85 (weak to moderate agreement), not 0.71-0.91. Corrected claim: Meaning-preserving prompt format changes move accuracy by up to 76 points (LLaMA-2-13B) and about 10 points on average across 50+ tasks; scale, shots and instruction tuning do not remove it, and format performance correlates only weakly across models. Instruction paraphrase also reorders model rankings: Kendall's W across templates ranges from about 0.27 to 0.91 over tasks (most below 0.85, i.e. weak to moderate agreement; Mizrahi et al.).
- **E18.10-K10** (reworded: the sources support less). Numbers all verified, but the Krippendorff alpha values (SummaC 0.326-0.788, MT-Bench 0.265-0.563) were measured with sampling temperature 0.6 in Rating Roulette, so they do not show variation 'even when sampling is off'; only Lau (2026) tests temperature 0. Corrected claim: Same-input LLM judging is unstable across repeated runs: with sampling temperature 0.6, Krippendorff alpha over 3 runs was 0.326-0.788 on SummaC and 0.265-0.563 on MT-Bench (no model reached 0.8 on MT-Bench; Rating Roulette), and Lau (2026) found none of five judges (including GPT-4o and Claude Haiku/Sonnet 4.5) fully deterministic even at temperature 0. GPT-4 inter-sample alpha (0.587) is below human inter-annotator alpha (0.659) on SummEval (Stureborg et al.).
- **E18.10-K22** (reworded: the sources support less). The 98% order-swap flip is a single Gemini-2.0-Flash cell (Verdict-first XML, JudgeBench), not a GPT-5.2, Claude-Sonnet-4.6 or Gemini-2.5-Pro result (their flip rates are far lower, e.g. Claude up to about 50%); the 7-17% rerun change and the >0.95 retest with >0.10 position bias (Qwen3 8B, Gemini 2.5 Flash) are otherwise supported. Corrected claim: In a six-judge audit (GPT-5.2, GPT-4o, Gemini-2.5-Pro, Gemini-2.0-Flash, Claude-Sonnet-4.6, Llama-3.3-70B), 7-17% of verdicts changed across identical reruns at temperature 0 and order swaps flipped up to 98% of pairwise verdicts in the worst case (Gemini-2.0-Flash on JudgeBench); in a separate 21-judge study, test-retest reliability above 0.95 coexisted with position bias above 0.10 for some judges (Qwen3 8B, Gemini 2.5 Flash).
- **E18.10-K08** (now single-source: only one opened source, code check).
