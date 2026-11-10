# Reproducibility and methods: deep document

*Subfield E15.07 of science of science. Replication crisis, misuse of p-values, publication bias, and the new work on LLM agents that replicate, audit or are themselves measured with weak methods. Source files in this folder: evidence_a-d.jsonl (ids a01-d17), claims.jsonl (K01-K35), critique.md. Main schema link: guardrail G3 (a pass must be on something the answer was not fitted to).*

*Reading note. Founding-paper numbers marked "from memory" in the evidence files are flagged here. Nearly all LLM results are 2025-2026 preprints on older or small models; none is peer reviewed unless stated.*

## 1. What it is

This field asks one question: when a research result is published, how often is it true, and how do we find out? Metascience measures the answer by re-running studies, auditing code and data, and counting what gets published.

Three problems sit inside it.

1. **Replication.** Do independent teams get the same result on new data? Large projects say: about half the time, with about half the effect size.
2. **Statistical practice.** A p-value under .05 is a weak test. Low power, many tried analyses and flexible choices produce false positives and inflated effects.
3. **Publication filter.** Significant results get written up and published. Null results mostly stay in the drawer. The visible record is biased upward.

Why this matters for our agent. Our agent loop does what a research field does: it tries many candidate answers, scores them, keeps the best, and reports a gain. The same failure modes apply. A candidate picked because it scored best on a few items is a "winner" in the same sense as a published significant result. Its score on fresh items will be lower. Guardrail G3 already says "a pass must be on something the answer was not fitted to". This document supplies the numbers behind that rule: how big the drop is, how it grows with search width, how it shrinks with more items, and which checks cut it.

There is a second link. LLM agents are now used to replicate papers, rerun code and judge reproducibility. The measured results show where agents are weak: they stop early, claim success without running, anchor on the expected answer, and agree on direction far more than on magnitude.

Related subfields researched in parallel (not covered here): Peer review and replication, Novelty measurement, Assessment and tests, Debiasing and cognitive forcing, Calibration and overconfidence, Methods and measurement, Aggregation and extremizing.

## 2. History and theories in depth

**2005, the model.** Ioannidis (a01-a03, b01-b02) wrote a formal model. The chance that a significant claim is true (positive predictive value, PPV) depends on pre-study odds R, power 1-beta, alpha and bias u. Without bias, PPV = (1-beta)R / (R - beta*R + alpha). PPV is above 0.5 only if (1-beta)R > alpha. Table 4 gives: adequately powered RCT (power 0.80, R 1:1, u 0.10) PPV 0.85; underpowered phase I/II RCT (0.20, 1:5, 0.20) 0.23; same, poorly performed (u 0.80) 0.17; exploratory epidemiology (0.20, 1:10, 0.30) 0.12; massive discovery testing (R 1:1000, u 0.80) 0.0010. Corollaries 3 and 4 say: more tested relationships and more flexibility in design and analysis lower PPV. Worked example: 60% power, pre-study odds 1e-4 (schizophrenia gene search), bias 0.10, post-study probability 4.4e-4. This is a model with assumed inputs, not a measured rate. Later work disputes how big the false-finding rate really is.

**2011-2012, flexibility and questionable practices.** Simmons, Nelson and Simonsohn (a12, b07, d14) showed in simulation and experiment that undisclosed flexibility (choice of dependent variable, sample size, covariates, subgroups) pushes the false-positive rate far above 5%. The combined figure usually quoted is about 61% at p<.05; this was not re-checked (abstract only, publisher blocked). John, Loewenstein and Prelec (a14) surveyed over 2,000 psychologists with incentives for honesty and found questionable research practices (QRPs) common. Percentages were not verified.

**2013, power.** Button et al. (a15, b09, d13) argued neuroscience studies are underpowered. The page abstract gives median power of about 8% to 31% depending on subfield. The often-quoted 21% could not be confirmed.

**2014-2015, publication bias and p-hacking.** Franco, Malhotra and Simonovits (a13, b08) followed survey experiments from the TESS program. Per the Science summary read in the critique: 10 of 48 null results were published (21%) versus 56 of 91 strongly significant results (62%). The paper abstract states strong results were 40 points more likely to be published and 60 points more likely to be written up. Most of the loss happened when authors never wrote up the null. Head et al. (a11) mined p-values from open-access papers and found a bump just under .05 (bin .045-.05 against .04-.045, estimated proportion 0.546 in Results). Overall the distribution was still right-skewed (0.257 of significant p-values in the .025-.05 bin), which shows real effects too.

**2015, the big replication.** The Open Science Collaboration (OSC; a04, a05, a25) replicated 100 psychology studies. 35 of 97 originals that were significant came back significant in the same direction (36.1%, CI 26.6-46.2%); about 89 were expected if all were true. Mean effect r fell from 0.403 to 0.197. Mean p-value rose from 0.028 to 0.302.

**2016-2018, more projects, markets and critique.** Camerer et al. replicated 18 economics lab experiments (11 replicated, 61%; mean r 0.474 to 0.279) and 21 Nature/Science social science experiments (13, 62%; mean relative effect size 46%). Many Labs 2 (a06, a07) ran 28 findings across many samples; 15 replicated (54%). Gilbert et al. (a16, b24) argued OSC had statistical errors and that reproducibility was higher; the OSC authors replied. The ASA (a17, 2016) issued six principles: a p-value is not the probability a hypothesis is true, and decisions should not rest on one threshold. Alternatives named: estimation with intervals, Bayesian methods, likelihood ratios or Bayes factors, decision-theoretic modelling, false discovery rates. Benjamin et al. (d12, 2018) proposed alpha = .005 for new claims.

**2021, preclinical cancer.** Errington et al. (b03, b23) tried to replicate experiments from high-impact cancer biology papers. Of 193 experiments, none was described fully enough to design a protocol without asking the authors. Raw data were shared for 31 (16%); nothing was shared for 131 (68%). The median replication effect was 85% smaller than the original.

**2021-2026, methods meet machine learning.** Bouthillier (a22) showed single-seed ML benchmark comparisons give about 10% false positives or low power. Atil (a23) showed "deterministic" LLM settings still vary by up to 15% accuracy across runs. From 2024, benchmarks for agents that replicate research appeared: CORE-Bench, PaperBench, REPRO-Bench, ReplicatorBench, SocSci-Repro. In 2025, work on "LLM hacking" (Baumann) showed that annotation choices act as researcher degrees of freedom. In 2026, Hu and Tang measured the winner's curse directly in LLM self-improvement loops.

**Competing theories.**
- *Questionable practices and bias* (Simmons, Ioannidis): the cause is flexibility and filtering.
- *Hidden moderators* (the original authors' typical defence): replications differ in sample or setting. Many Labs 2 (a07) tested this and found little support. Only 11 of 28 replication effects had significant heterogeneity; only one had tau above .20; task order, lab vs online and WEIRD vs less-WEIRD made little difference.
- *Statistical definition* (Gilbert): the success rate depends on how success is defined. This is the main surviving dispute (K10).
- *Low prior odds* (Ioannidis, Benjamin): exploratory fields test mostly false hypotheses, so even honest p<.05 results are often false.

## 3. Core findings with exact numbers

Status: established = several independent sources; single-source; contested; from-memory = number not re-opened; derived = our own arithmetic.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| PPV of a significant claim falls with low prior odds, low power, bias | 0.85 (power .80, R 1:1, u .10) down to 0.001 (R 1:1000, u .80) | Ioannidis 2005 (a01, b01) | single-source model |
| Psychology replication rate | 35 of 97 (36.1%, CI 26.6-46.2); r 0.403 to 0.197 | OSC 2015 (a04) | established |
| Original p-value predicts success | p<.001: 20/32 (63%); p<.02: 26/63 (41%); .02-.04: 6/23 (26%); above .04: 2/11 (18%) | OSC 2015 (a05) | single-source |
| Main effects replicate more than interactions | 23/49 (47%) vs 8/37 (22%) | OSC 2015 (a05) | single-source |
| By journal | JPSP 7/31 (23%); JEP:LMC 13/27 (48%); Psych Science 7/24 (29%) | OSC 2015 (a05) | single-source |
| Economics lab replication | 11/18 (61.1%); r 0.474 to 0.279; 92% expected if all true | Camerer 2016 (a08) | established |
| Nature/Science social science | 13/21 (62%); mean relative effect 46.2% (74.5% for the 13 that replicated, 0.3% for the 8 that did not); samples about 5x original | Camerer 2018 (a09) | established |
| Many Labs 2 | 15/28 (54%) at p<.05; 14 (50%) at p<.0001; median d 0.60 to 0.15; 75% smaller, 25% larger; 32% in the opposite direction | Klein 2018 (a06) | established |
| Hidden moderators explain little | heterogeneity significant in 11/28; one effect tau above .20 | Klein 2018 (a07) | single-source |
| Peer forecasts of replication | markets 63.4%, survey 60.6%, observed 61.9%; economics markets 75.2% vs 61.1% observed | Camerer 2018 (a10, b05) | established |
| p-hacking trace | excess in bin .045-.05; proportion 0.546 (Results) | Head 2015 (a11) | established with a12, a14 |
| Combined flexibility false-positive rate | about 61% at p<.05 | Simmons 2011 (b07) | from-memory |
| Publication filter | 10/48 nulls published (21%) vs 56/91 strong results (62%) | Franco 2014 (a13, b08, critique) | single-source |
| Neuroscience power | median 8% to 31% by subfield | Button 2013 (d13) | single-source |
| p=.05 is weak evidence | Bayes factor about 2.5-3.4; p=.005 gives 14-26; prior odds 1:10 and p<.05 give false-positive rate above 33% at any power, 5% at p<.005 | Benjamin 2018 (d12), ASA (a17) | established |
| OSC headline contested | success depends on definition (significance vs interval overlap) | Gilbert 2016 (a16, b24) | contested |
| Analytic reproducibility with code and data | ML challenge 18/28; economics 128/203; CS 311/601; psychology 16/25; finance 484/1008 | CORE-Bench survey (c07, b11, b25) | established (table header garbled in one place) |
| Preclinical cancer | median effect 85% smaller; 0/193 protocols designable from the paper; raw data shared 16% | Errington 2021 (b03, b23) | single-source |
| Selection bias in LLM loops | selection-set score above held-out by 13-20 points at 16 items, 1-5 at 256; paired reduction about 15 points | Hu and Tang 2026 (d02) | established (3 sources, preprints) |
| Simulated best-of-N optimism | +1.5 pp at 3 candidates, +4.0 pp at 50 identical candidates; identical systems declared winner up to 94% | SIREN (d04) | established |
| MMLU-Pro same-data winner bias | +3.06 points vs -0.01 with frozen shortlist and held-out splits; random search at 500K budget +5.19 | Zhang 2026 (d04) | single-source |
| Later rewrites mostly harmful | first rewrites 75-100% beat seed (TREC); later 4-39% beat incumbent; mean held-out effect -0.2 to -13.5 points | Hu and Tang (d01) | single-source |
| Audit set removes average bias | 64 fresh items, 128 evaluations; RMSE of reported gain 15.5 to 5.7 points; single estimates still about 6 off | Hu and Tang (d03) | single-source |
| Pre-set acceptance rules cut churn | greedy 13.3 self-edits per run, 72-100% false with no real gain; gates under 1 edit; no reliable held-out accuracy gain | PACE (d05), Hu and Tang (d03) | contested |
| Frozen-control arm | frozen Qwen3-8B shows expansion rate 0.280 from decode noise alone | Xu 2026 (d06) | single-source |
| Judge prompt sensitivity | agreement loss: coherence -0.181, factuality -0.057, preference -0.045, relevance -0.034 (880 items, 25 judges); clustered SEs 1.37-1.63x larger | JudgeSense (d07) | single-source |
| Judge calibration | n=100 human labels estimate TPR/FPR; Type I control on 10,000 judge labels | Feng 2026 (d08) | single-source |
| Minimum paired items for a 3-point gain | about 690 (10% disagreement) to about 1,370 (20%) | own arithmetic (d09) | derived |
| Single-seed noise | temp-0 accuracy varies up to 15%; pass@1 16.9% vs pass@8 34.1% (MLE-bench) | Atil 2024 (a23), Chan 2025 (b12) | established |
| LLM annotation as a degree of freedom | wrong conclusion about 31% (top models) to 50% (small); false positive achievable for 94.4% of nulls; true effect hidden 98.1%; 100 human labels give Type I about 10% | Baumann 2025 (c13-c16) | single-source |
| PaperBench | Claude 3.5 Sonnet 21.0%, o1 13.2%, R1 6.0%; humans 41.4% (best of 3, 48 h, 3-paper subset) vs o1 26.6%; IterativeAgent o1 24.4, Claude 16.1 | Starace 2025 (c01-c04) | single-source |
| CORE-Bench | CORE-Agent GPT-4o 60.00 / 57.78 / 21.48% (easy/medium/hard) | Siegel 2024 (a19, c06) | established |
| Agents on social-science reruns | Claude Code 93.4% task accuracy, Codex 62.1%; paper level 78.0 vs 35.8% | Alizadeh 2026 (c21) | single-source |
| Anchoring on the expected answer | non-reproducible tasks 100% to 63.3% (Claude Code), 100% to 90.0% (Codex) with the PDF; confirmatory nudging about 70% and 60% | Alizadeh 2026 (c22, c23) | single-source |
| Judging reproducibility | REPRO-Bench best agent 21.4% (chance 25%); REPRO-Agent 36.6%; applicability 92.9% vs 60.7% | Hu 2025 (c08, c09) | single-source |
| Direction vs magnitude | same conclusion 80%; effect within 0.05 d 24%, within 0.20 d 50%; sign agreement 75-91% (always-positive 68%) | Holtdirk 2026 (c24), Kohler 2026 (c10) | established |
| Same-model samples correlated | candidate error correlation 0.44-0.60; GPT replicated 37.5% of 8 studies, 99.6% "conservative" | Hu and Tang (d16), Park 2023 (c17) | established as hint; mechanism open |
| AI scientist faults | 5 of 12 experiments failed from coding errors | Beel 2025 (a20) | single-source |
| Verifier before shipping | precision 0.471 vs 0.353 (20 runs, pre-registered); non-inferiority on retained true candidates not met (0.875 vs 0.90) | d11 (abstract) | single-source |
| Large vs small gains | gains of 26-39 points survive any selection size; few-point gains do not; harness evolution beats matched-budget search on ARC-AGI-3 (+80%) and EdgeBench (+11%), not Terminal-Bench | d17, d10 (abstract) | single-source |

## 4. Mechanisms and models

An engineer can implement each of these as a measurement or gate.

**4.1 PPV model (Ioannidis).** Inputs: prior odds R that a candidate claim is true, power 1-beta, alpha, bias u. PPV = (1-beta)R / (R - beta*R + alpha) for u=0. For our loop, R is the base rate at which a tried candidate truly beats the baseline. Count N candidates tried per problem. With a fixed number of true winners, more candidates lower R and so PPV. Rule: discount a surprising winner by search width. This is an analogy, not a measured result.

**4.2 Winner's curse (selection bias).** Select the max of N noisy scores. The max is biased up by about sigma times E[max of N standard normals], where sigma is the score noise on the selection items (about sqrt(p(1-p)/n) for accuracy p on n items). With n=16 and p=0.5, sigma is 0.125, so even a few candidates inflate the winner by a large share of 10 points. Hu and Tang measured 13-20 points at n=16 and 1-5 at n=256, consistent with noise falling like 1/sqrt(n). Implementation: keep selection items and a disjoint held-out set; report the held-out score of the winner only. The gap (selection minus held-out) is the diagnostic.

**4.3 Frozen shortlist plus held-out split (SIREN, d04).** Fix a shortlist using selection data. Evaluate once on data never used for selection. Measured bias on MMLU-Pro Math: +3.06 same-data, -0.01 with this scheme.

**4.4 Audit set.** Reserve about 64 unseen items, never used for selection, to score the start and final versions (d03). Costs about one tenth of the budget. Cut RMSE of the reported gain from 15.5 to 5.7 points. A single estimate is still about 6 points off, so report an interval.

**4.5 Pre-set acceptance rules.** Greedy: commit any change whose score went up. Gate: commit only if a paired test (sequential test, McNemar, Bayes gate) passes. At n=16 greedy commits in 44% of decisions, the pilot gate 8%, tuned McNemar 6%; 58%, 59% and 46% of those commits were harmful (d03). Gates cut churn but did not reliably improve final held-out accuracy (K29). Use as hygiene.

**4.6 Frozen control arm (d06).** Re-run the unchanged system through the same pipeline and compute the same statistic. A gain no larger than the control's spurious rate is noise. A frozen model showed 0.280 apparent expansion from decode noise.

**4.7 Paired power.** Only items where two systems disagree carry information. n is about (1.645+0.84)^2 * d / delta^2 for one-sided alpha .05 and 80% power, with d the disagreement rate and delta the gain. For delta=0.03: d=10% gives about 690 items, d=20% about 1,370 (own arithmetic, d09). Judge noise and seed variance raise this.

**4.8 Judge as instrument.** A judge is a measurement with error. Calibrate it on about 100 human labels to estimate true- and false-positive rates (d08). Use two wordings of the judge prompt and judges from more than one vendor (d07; siblings from one vendor are not independent).

**4.9 Multi-seed variance (a22, a23).** Run at least 3 seeds per arm. Treat differences inside run-to-run range as zero. Report pass@1 and pass@k separately: pass@8 was double pass@1 on MLE-bench.

**4.10 Verify-before-claim (d11).** A separate verifier stage before a claim ships. Precision 0.471 vs 0.353. Track retained true findings so the verifier does not suppress real ones.

**4.11 Graded closeness (c12).** Score reproduction in bands by percent difference: A 0-2%, B 2-20%, C 20-40%, D 40-60%, E 60%+ or wrong sign, F missing. Gives a progress signal that pass/fail hides. Stage-wise scoring shows where pipelines break (ReplicatorBench: execution strong, data retrieval weak).

**4.12 Forecasting replication.** Peers can forecast (markets 63.4% vs observed 61.9%). An agent can log P(claim holds on held-out data) per claim and be scored with the Brier score. Not measured for LLMs beyond Saynova (F1 up to 77%, unstable with temperature).

## 5. What holds up

**Holds, many sources.**
- Replication shrinks effects: OSC r 0.40 to 0.20; Many Labs 2 d 0.60 to 0.15; economics r 0.47 to 0.28; Nature/Science relative 46%; preclinical median 85% smaller. Working default: about half.
- Replication rates are about 36-62% depending on definition and field.
- Peer forecasts are informative (a10).
- Code and data do not guarantee a rerun: 18/28 to 311/601 depending on field.
- Single-run noise is large in ML and LLMs (a22, a23, b12).
- Selection on few items inflates scores in LLM loops (d01, d02, d04).

**Moderators that held.** Lower original p, simple main effects (not interactions) and larger original effects replicate more (original effect size vs success r=0.304; replication power vs success r=0.368). Large gains survive, marginal ones do not (d17). Journal and field matter (JPSP 23% vs JEP:LMC 48%).

**What failed or was weakly supported.**
- Hidden moderators as the main reason for failure: little support in Many Labs 2.
- Pre-set acceptance rules as accuracy boosters: not shown (K29). PACE's degradation claim did not replicate in Hu and Tang's pre-registered runs.
- Naive scaffold transfer: IterativeAgent helped o1 (13.2 to 24.4) and hurt Claude 3.5 Sonnet (21.0 to 16.1). Assume no transfer across models.
- LLM samples as replications: near-zero variance, error correlation 0.44-0.60.
- Larger selection sets help on TREC but not GSM8K, so no universal rule.

**Interventions that worked.**
- Small human-labelled set: Type I about 10% with 100 labels (c16, d08).
- Audit set of 64 fresh items (d03).
- Frozen shortlist plus held-out split (d04).
- Task hints for agents (CORE-Agent over AutoGPT).
- Fallback-first scaffold on REPRO-Bench: 21.4 to 36.6%.
- Verifier stage: precision 0.471 vs 0.353.
- Confirmatory prompting raised overall task accuracy but hurt the ability to say "cannot be done" (see 6).

**Not worked or unproven.** Bias-awareness instructions are in SCHEMA 4b as not working. No test shows that freezing scoring and stopping rules as a package lowers the false-gain rate at equal tokens. No test shows that showing an agent its failed attempts reduces overclaiming.

**Contested.** The OSC headline (Gilbert vs OSC). Camerer markets were calibrated in Nature/Science but overshot in economics. The Franco and Button numbers rest on abstracts; Simmons' 61% is from memory.

## 6. Language models

**As candidates in their own loop (winner's curse).** Hu and Tang (2026; d01-d03, d16, d17), Qwen models, TREC and Banking77: first-generation rewrites improved on the seed 75-100% of the time (TREC), later ones 4-39%. Greedy at n=16 ended below the seed in half of seeds while its own score rose 12.5 points. Selection-set score exceeded held-out by 13-20 points at 16 items and 1-5 at 256. Candidate error correlation 0.44-0.60. Large gains from weak seeds (26-39 points) survive at every n. Small models, preprint.

**Statistical simulation (d04).** +1.5 pp optimism at 3 candidates, +4.0 pp at 50. MMLU-Pro Math with random search: +3.06 same-data vs -0.01 with the frozen-shortlist method; DSPy tuner +1.43 vs -0.05.

**Phantom gains (d06).** A frozen Qwen3-8B appears to "improve" through decode noise alone (rate 0.280). Seven measurement failures each reverse a reported finding without the null control.

**Variance and benchmarks.** Atil: up to 15% accuracy spread across runs at "deterministic" settings, up to 70% best-to-worst gap. Bouthillier: single-point comparisons carry about 10% false positives or low power. MLE-bench: pass@1 16.9%, pass@8 34.1% (o1-preview with AIDE). Dominguez-Olmedo: after randomizing option order, answers of 43 models trend toward uniform.

**LLM-as-judge (d07, d08).** Rewording a judge prompt lowers agreement by 0.034 to 0.181; clustering by vendor makes standard errors 1.37-1.63x larger. A judge inside an agent harness looks more stable only because its self-agreement collapses faster.

**LLM annotation as researcher degrees of freedom (Baumann, c13-c16).** Wrong conclusion in about 31% of hypotheses (top models) to about 50% (small). Type II errors 31-59%. Sign reversed in 4-16%. Paraphrased prompts make a false positive achievable for 94.4% of null hypotheses and hide true effects in 98.1%. Near p=0.05 error approaches 70%. Task traits explain 21% of variance, model performance 8%, prompt choices under 1%. Only 2.7% of correct significant effects were within 10% of true magnitude (GPT-4o). 100 human labels give Type I about 10%; 1,000 labels bring overall risk to about 20%.

**Agents replicating research.**
- PaperBench (20 ICML 2024 papers, 8,316 rubric items, LLM judge F1 0.83): Claude 3.5 Sonnet 21.0% (SEM 0.8), o1-high 13.2%, DeepSeek-R1 6.0%, Gemini 2.0 Flash 3.2%. IterativeAgent: o1 24.4, Claude 16.1, o3-mini-high 8.5; o1 with 36 h limit 26.0. Code-Dev variant: o1 43.4. Human ML PhDs best-of-3 on a 3-paper subset 41.4% vs o1 26.6. Most models finished early and claimed success; o1 plateaus after the first hour.
- CORE-Bench: with code and data, 60 / 57.8 / 21.5% (GPT-4o, CORE-Agent). 2026 agents do far better: Claude Code 93.4% task accuracy on SocSci-Repro (Codex 62.1%); older CORE-Agent GPT-4o 19% on that kind of task.
- REPRO-Bench: judging whether a study reproduces is harder than rerunning: best 21.4% vs 25% chance; REPRO-Agent 36.6%.
- ReplicatorBench: GPT-5 best on binary outcome (about +10% over o3); claim extraction humans 71.33, GPT-5 63.65, GPT-4o 57.56; execution improves in Python mode but outcome reliability does not follow.
- Kohler 2026: sign agreement 75-91% (always-positive 68%); best agent within 1.96 original SE over 80% of the time. Scaffold and token use mattered: GPT-5.4 on OpenCode beat Codex CLI and mini-SWE-Agent.
- Holtdirk 2026: same conclusion 80%; effect within 0.05 d only 24%, within 0.20 d 50%; on a human-reanalysis subset 95% vs 83% conclusion match and 40% vs 28% exact effect. Abstract-only input did as well as full paper (22% vs 24%), so the agent may not lean on the paper.
- Anchoring (Alizadeh 2026): on non-reproducible tasks accuracy fell from 100% to 63.3% (Claude Code) and 90.0% (Codex) once the paper was shown. Confirmatory nudging: overall accuracy rose (Claude 93.4 to 94.1; Codex 62.1 to 74.1; Codex failures 17.8 to 0.5%), but non-reproducible-task accuracy fell to about 70% and 60%.
- AI Scientist audit (Beel): 5 of 12 experiments failed from coding errors; hallucinated numbers; weak literature review (small sample).

**LLMs as simulated participants or forecasters.** GPT replicated 37.5% of 8 studies with 99.6% "conservative" verdicts (Park 2023). Saynova: F1 up to 77% (Mistral 7B), 67% (GPT-4o), unstable with temperature (GPT-4o 0.50 at 0.1, 0.67 at 0.5, 0.36 at 1.0; Llama precision 1.0, recall 0.13 at 0.1). Aher: valid generation 88-99.5% for Ultimatum, 51-99% for Wisdom of Crowds; larger models show hyper-accuracy.

**Verify stage.** A model verifier before shipping gave precision 0.471 vs 0.353 in security-agent runs (abstract only).

## 7. What our agent should take

Status: [E] established, [S] single-source, [C] contested. Schema part: G guardrail, S state, O operator, memory.

### Add now (established)

1. **Report the held-out score of the selected candidate, never the selection score.** G3, S4, S8, S9 log. [E] d01, d02, d04, a03 (K26). The gap grows with candidates and shrinks with items.
2. **Default shrink: expect about half of any in-sample gain to survive on fresh items.** G3, S9 log. [E] a04, a06, a08, a09 (K01, K02). A prior, not a law; large gains survive better.
3. **Use effect size plus interval and several indicators, not one pass/fail.** G3, S8. [E] a17, d12 (K11). (The OSC definition dispute, K10, is [C], which is why more than one indicator.)
4. **Multi-seed measurement: at least 3 seeds per arm; gains inside run-to-run range count as zero; report pass@1 and pass@k separately.** G3, G7 (bench method). [E] a22, a23, b12 (K21).
5. **Run the check; do not recall a result.** Every reported number must trace to an executed output. G2, G3, G10, S4/S8. [E] b11, c07 (reruns fail often even with code); a20 is [S].
6. **Treat repeated samples from one model as correlated.** G4 (already present). [E] c17, d16, a21.
7. **Shuffle answer options and test paraphrase robustness in every choice test.** G3, S1. [E] as a bench rule from c13-c16 and a24 (a24 alone is [S]).
8. **A matched-compute baseline for every scaffold claim.** G7. [E] a22, K32 (d10 is abstract only). G7 already exists; this makes the equal-token control explicit in the bench.

### Test first

- **U1 Audit set of about 64 unseen items scoring start and final scaffold.** G3, S9. [S] d03.
- **U2 Frozen control arm re-run through the same pipeline.** G7, bench. [S] d06.
- **U3 Winner discount by search width.** G3, S7. [S] a01, a03 model plus d04 simulation; the effect is [E] in LLM loops, the discount rule itself is inference.
- **U4 Forced check that claimed work was executed before "done".** G3, G6, S8. [S] c03, c04.
- **U5 Impossible-item check: "cannot be done" allowed as a final answer after a real failed attempt.** G3 with G6 tension. [S] c22, c23. G6 says never abstain on the first pass; this concerns the final answer after checks fail. Test before any change.
- **U6 Separate verifier stage before a claim ships.** S8. [S] d11.
- **U7 Two judge wordings, two vendors, calibrate on about 100 human labels.** G5, G8. [S] d07, d08.
- **U8 Log failed attempts and show them at the final stage (file-drawer analogue).** memory, S9. [S] a13 is human data; no LLM study.
- **U9 Freeze scoring rule, prompt and stopping rule before the first run (pre-registration analogue).** G3, S0. [C] d03, d05.
- **U10 Agent forecasts P(claim holds) per claim, scored by Brier.** memory, S9. [S] a10 (human), b17 (LLM, unstable).
- **U11 Independent-route agreement as a direction check only.** O, S7. [E] for direction (c10, c24); magnitude is not trustworthy.
- **U12 Mix prompts or models before counting agreement as replication.** G4. [S] d16; no vote-accuracy study.
- **U13 Larger margin required for borderline gains.** G3, S7. [S] a05, d17.
- **U14 Refuse "context differs" as an excuse unless the moderator is tested.** G3, S5. [S] a07.

Test definitions and thresholds are in UNKNOWNS.md.

## 8. Concrete tests on our bench

All arms get the same total tokens. Report pass@1 over at least 3 seeds.

| # | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 | ARC and BRAINTEASER items split into selection and held-out sets; candidates N = 3, 10, 30 | selection score vs held-out score of the same winner | selection minus held-out gap per N | gap rises with N, falls with selection size; about 15 points at 16 items |
| T2 | Same items; 64-item audit reserved vs none | with audit, without audit | RMSE of reported gain vs gain on 600 fresh items | RMSE falls from about 15 to about 6 points |
| T3 | Frozen control: unchanged agent re-run through the full pipeline | scaffold vs frozen plain, same measuring code | rate of "gain" in the control | nonzero rate sets the noise floor |
| T4 | Items with impossible or unfixable instances (about 20%) | plain; "must run before done"; forced check plus allowed "cannot do" | correct "cannot do" rate and overall accuracy | forced check raises honest-failure rate; watch overall accuracy |
| T5 | Paired scaffold A/B on 700-1,400 items with identical arms | one judge wording vs two wordings and two vendors | false-positive rate of A/B on identical arms | single-wording judge gives more false wins |
| T6 | Retest every gain found with a margin under 5 points on fresh items | retest vs no retest | fraction of gains that survive | small margins mostly vanish; large survive |
| T7 | Pre-registration analogue | frozen scoring, prompt and stopping rule vs free loop | false-gain rate, churn, final held-out accuracy | churn falls; accuracy gain not assumed |
| T8 | Replication forecast: agent logs P(holds on fresh items) per candidate | forecast vs no forecast | Brier score; effect on selection | Brier below 0.25 if better than chance |
| T9 | Failed-attempt memory shown at the final stage | with vs without | overclaim rate (claimed pass, fresh fail) | lower overclaim; unmeasured in the literature |
| T10 | Answer option order shuffle | fixed vs shuffled | accuracy change and answer stability | instability appears on weak items |
| T11 | 5 samples from one prompt vs 5 across prompts or models | equal tokens | vote accuracy vs pairwise error correlation | mixed sources lower correlation (0.44-0.60 baseline) |

## 9. What does not transfer, and why

- **Human QRP psychology.** P-hacking by motive (career pressure) has no counterpart in a model. Only the mechanism (flexible analysis plus selection) transfers.
- **Publication bias as such.** The file drawer is social. In a loop it exists only if the agent discards failures. Its analogue is a memory design choice, and no LLM study shows the effect.
- **Replication-rate numbers.** 36-62% describes published psychology and social science. It is not a prediction for our agent's gains. Use the shrinkage idea, not the number.
- **Ioannidis PPV.** The inputs (R, u) are unknown for our loop. It supports the direction (wider search, lower PPV), not any value.
- **PaperBench and CORE-Bench numbers.** They use Claude 3.5 Sonnet, o1 and GPT-4o. SocSci-Repro shows modern agents score far higher (Claude Code 93.4% vs 19% for older CORE-Agent). Do not use the older numbers as current capability.
- **Scaffold effects across models.** IterativeAgent helped one model and hurt another. Do not assume transfer.
- **Pre-set rules as an accuracy gain.** Evidence is only for churn reduction.
- **Small-model results (Qwen 0.5B to 14B).** Hu and Tang, PACE and Phantom Gains use small models. Magnitudes may differ on frontier models.
- **LLM judges as ground truth.** PaperBench judge F1 0.83 is acceptable for rubric grading but is not a substitute for held-out data.
- **Simulating subjects with LLMs.** Near-zero variance and 99.6% "conservative" verdicts make LLM samples a poor stand-in for independent participants.

## 10. Open questions

1. Does freezing the scoring rule, prompt and stopping rule as a package lower false gains at equal tokens? No study found.
2. What is the false-positive rate of an LLM-judge comparison between two scaffolds by items and seeds? Our minimum N (690-1,370) is arithmetic, not measured.
3. Does showing the agent its failed attempts reduce overclaiming? Not found.
4. How well calibrated is an agent's forecast that a claim will replicate (Brier)? Only Saynova and Holtdirk.
5. What do 2026 frontier models score on PaperBench and CORE-Bench, and does a verify-before-claim step remove early finish and anchoring?
6. How should "cannot be reproduced" be rewarded? The 100-to-63% drop under anchoring has no tested remedy; confirmatory nudging made it worse.
7. Which effect types survive replication, and does that map to which agent improvements survive fresh-item testing? The mapping is inference.
8. Do samples from one model ever count as independent replications? Measured diversity vs vote accuracy not found.
9. Simmons per-practice rates, Button's exact median power and Franco's 40/60-point figures were not re-opened.
10. Arce (2026) audit of 41 self-improving agent papers (d15) says most fail two or more evaluation traps. Not opened. It would give a base rate for our own field.

## 11. Sources

[V] opened this session (page or PDF text read). [M] snippet, abstract only, or from memory.

- [V] Ioannidis (2005) Why most published research findings are false. https://journals.plos.org/plosmedicine/article/file?id=10.1371/journal.pmed.0020124&type=printable
- [V] Open Science Collaboration (2015) Estimating the reproducibility of psychological science. https://discovery.dundee.ac.uk/ws/files/7385883/RPP_SCIENCE_2015.pdf ; journal page https://www.science.org/doi/10.1126/science.aac4716 [M]
- [V] Klein et al. (2018) Many Labs 2. https://pure.tue.nl/ws/files/144712347/2515245918810225.pdf
- [V] Camerer et al. (2016) Evaluating replicability of laboratory experiments in economics. https://mpra.ub.uni-muenchen.de/75461/1/MPRA_paper_75461.pdf
- [V] Camerer et al. (2018) Replicability of social science experiments in Nature and Science. https://osf.io/download/5b7ef2af8c6d9f001baeb8b3/ ; https://www.nature.com/articles/s41562-018-0399-z [M]
- [V] Head et al. (2015) The extent and consequences of p-hacking in science. https://journals.plos.org/plosbiology/
- [M] Simmons, Nelson, Simonsohn (2011) False-positive psychology. https://journals.sagepub.com/doi/10.1177/0956797611417632
- [M] Franco, Malhotra, Simonovits (2014) Publication bias in the social sciences. https://www.science.org/doi/10.1126/science.1255484 (Crossref abstract read for 10/48 vs 56/91)
- [M] John, Loewenstein, Prelec (2012) Measuring the prevalence of questionable research practices. via Europe PMC
- [V] Button et al. (2013) Power failure (page abstract only). https://www.nature.com/articles/nrn3475
- [M] Gilbert, King, Pettigrew, Wilson (2016) Comment on Estimating the reproducibility. https://www.science.org/doi/10.1126/science.aad7243
- [V] ASA (2016) Statement on p-values. https://www.amstat.org/asa/files/pdfs/p-valuestatement.pdf
- [V] Benjamin et al. (2018) Redefine statistical significance. https://www.nature.com/articles/s41562-017-0189-z
- [V] Errington et al. (2021) Challenges for assessing replicability in preclinical cancer biology. https://elifesciences.org/articles/67995.pdf ; Investigating replicability https://elifesciences.org/articles/71601 (85% figure re-opened in critique)
- [V] Starace et al. (2025) PaperBench. https://arxiv.org/abs/2504.01848
- [V] Siegel et al. (2024, v2 2026) CORE-Bench. https://arxiv.org/abs/2409.11363
- [V] Hu et al. (2025) REPRO-Bench. https://arxiv.org/abs/2507.18901
- [V] Nguyen et al. (2026) ReplicatorBench. https://arxiv.org/abs/2602.11354
- [V] Baumann et al. (2025) Large Language Model Hacking. https://arxiv.org/abs/2509.08825
- [V] Saynova et al. (2025) Identifying non-replicable social science studies with language models. https://arxiv.org/abs/2503.10671
- [V] Park, Schoenegger, Zhu (2023) Diminished diversity-of-thought in a standard LLM. https://arxiv.org/abs/2302.07267
- [V] Kohler et al. (2026) Read the paper, write the code. https://arxiv.org/abs/2604.21965
- [V] Alizadeh et al. (2026) AI coding agents can reproduce social science findings. https://arxiv.org/abs/2606.11447
- [V] Holtdirk et al. (2026) Automated reproducibility assessments in social science. https://arxiv.org/abs/2606.13670
- [V] Chan et al. (2025) MLE-bench. https://arxiv.org/abs/2410.07095
- [V] Beel, Kan, Baumgart (2025) Evaluating Sakana's AI Scientist. https://arxiv.org/pdf/2502.14297
- [V] Aher, Arriaga, Kalai (2023) Using LLMs to simulate multiple humans. https://arxiv.org/pdf/2208.10264
- [V] Bouthillier et al. (2021) Accounting for variance in machine learning benchmarks. https://arxiv.org/pdf/2103.03098
- [V] Atil et al. (2024) Non-determinism of deterministic LLM settings. https://arxiv.org/pdf/2408.04667
- [V] Dominguez-Olmedo, Hardt, Mendler-Dunner (2023) Questioning the survey responses of LLMs. https://arxiv.org/pdf/2306.07951
- [V] Hu and Tang (2026) The winner's curse in LLM self-improvement loops. https://arxiv.org/abs/2610.09239
- [V] Zhang et al. (2026) Towards reliable LLM evaluation (SIREN). https://arxiv.org/abs/2605.05973
- [V] Shawn (2026) PACE anytime-valid acceptance tests. https://arxiv.org/abs/2606.08106
- [V] Xu et al. (2026) Phantom gains. https://arxiv.org/abs/2608.20290
- [V] Bellibatlu, Raff, Zhang (2026) JudgeSense. https://arxiv.org/abs/2604.23478
- [V] Feng et al. (2026) Noisy but valid. https://arxiv.org/abs/2601.20913
- [M] Wang et al. (2026) Rethinking the evaluation of harness evolution (abstract). https://arxiv.org/abs/2607.12227
- [M] The model proposes, the code disposes (2026), pre-registered verifier ablation (abstract). https://arxiv.org/abs/2609.15887
- [M] Arce (2026) methods audit of 41 self-improving agent papers (title only; link unusual).
- Derived power calculation d09: own arithmetic, no external source.
