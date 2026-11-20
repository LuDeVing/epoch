# Judicial bias and noise: deep document

*Subfield E11.08. Sources: evidence_a-d.jsonl (a01-a26, b01-b28, c01-c25, d01-d16), claims.jsonl (K01-K27), critique.md. Status marks follow SCHEMA.md: [E] established, [S] single-source, [C] contested. Evidence ids are in brackets. Numbers seen only in a snippet or abstract are marked (snippet).*

## 1. What it is

This subfield studies why professional judges, and other expert deciders, give different answers to the same case, or different answers on different days, for reasons that have nothing to do with the case. Four threads sit under it.

1. **Order and fatigue effects.** Does the rate of favourable rulings change with position in a session, time of day, or a break? The founding study is Danziger, Levav and Avnaim-Pesso (2011), the "hungry judge" paper. Its reading is disputed.
2. **Sequential contamination.** Does the last decision change the next one (the gambler's fallacy)? Chen, Moskowitz and Shue (2016).
3. **Anchoring.** Does an irrelevant or arbitrary number (a prosecutor's demand, a dice roll, a damages claim) pull a numeric judgment toward it? Strong evidence, mostly from vignettes.
4. **Noise.** Kahneman, Sibony and Sunstein (2021) split unwanted variability in judgment into level noise (judges differ in average severity), stable pattern noise (judges differ on particular cases) and occasion noise (the same judge differs from day to day). Sentence variance is the standard example.

Why it matters for our agent. Our agent is one language model run through a scaffold. The same failure shapes can appear in it: late-run defaults, answers pulled by a number in the prompt, verdicts that flip when two options swap places, and different answers on identical repeated calls. The schema already has guardrails for several of these (G4, G5, S1 input hygiene). This subfield gives the human evidence behind them and a set of LLM measurements. Role in the schema: guardrail and background.

Key finding up front: the famous human order effect is probably mostly an artifact, but the LLM analogues (position bias, anchoring, occasion noise) are measured, large and real.

## 2. History and theories in depth

**Noise tradition.** The idea that judging varies with the judge is old. Clancy et al. (1981) gave 208 criminal judges 16 fictive cases. Judges were unanimous on prison in only 3 of 16 cases. In one case the average recommendation was 1.1 years while one judge recommended 15 years [a17, b12; read through a Wikipedia summary of the Noise book, not the book]. Kahneman, Sibony and Sunstein (2021) turned this into a framework, the noise audit [a16, a19]. Their core argument: cutting noise by a given amount cuts total error as much as cutting bias by the same amount. They report stable pattern noise is usually larger than occasion noise and often larger than level noise; asylum decisions are an exception with mostly level noise [a16]. Other examples: underwriters priced the same five customers with a 55% spread in median premiums; two psychiatrists agreed on half of 426 diagnoses [a18, b12].

**Anchoring.** Tversky and Kahneman (1974) showed a random wheel number pulls estimates (wheel at 10 gave a mean of 25%, at 65 gave 45%; secondary summary, original not opened) [a21]. Englich, Mussweiler and Strack (2006) showed experienced judges are pulled by a prosecutor's sentencing demand, even one set by a dice throw [b09, a20; numbers unverified]. Enough and Mussweiler (2001): a 34-month demand gave a mean sentence of 24.41 months, a 12-month demand gave 17.64 [b07]. The review text says "8 months longer", but the means differ by 6.77; do not quote 8. Guthrie et al. (2001) found the same in damages awards [b07]. Englich et al. (2005): the defence counter-demand is itself anchored on the prosecutor's demand [b09].

**The hungry judge.** Danziger et al. (2011, PNAS) analysed 1,112 Israeli parole rulings by 8 judges over 50 days in 10 months, from two boards covering about 40% of Israeli parole requests [a01]. Favourable rulings fell from about 65% at the start of each of three daily sessions to nearly 0 at the end, and returned to about 65% after each of two food breaks. They read this as mental depletion repaired by a break. The paper had 1,415 Google Scholar citations by October 2021 [a11].

**The critique chain.**
- Weinshall-Margel and Shapard (2011): order is not random. Prisoners without a lawyer are about a third of cases, win 15% (represented: 35%), and tend to be heard last [a05]. Danziger et al. replied that the trend survives controls for representation and without deferrals [a06].
- Glockner (2016) built a simulation. Favourable rulings take longer than unfavourable (7.37 vs 5.21 minutes; t = 6.86 in the original [a04]). If a session ends when time runs out, favourable cases fit less often near the end. That alone produces the sawtooth with no fatigue [a07, b02].
- Lakens (2017) argued the effect size is implausible [a10, b05].
- Chatziathanasiou (2022) calls it a narrative that spread beyond its evidence, and points to Spamann (2020), who found no weather effect on judges [a11].
- Ego depletion, the proposed mechanism, failed large preregistered replications [b14, b15].

**Sequential decisions.** Chen, Moskowitz and Shue (2016) studied US asylum judges, loan officers and baseball umpires for negative autocorrelation: after one decision of a type, the next is less likely to be the same [a12, b10]. Unlike Danziger, asylum cases are randomly assigned and decided first-in-first-out [a14].

**LLM turn.** Since 2023 the same constructs are measured on language models: position bias and order flips in LLM judges (Wang 2023; Zheng 2023; Shi 2025; Kumar 2026), anchoring batteries (Suri 2023; Lou and Sun 2024; Huang 2025), judicial-bias audits (Hu 2025; a 2026 virtuous-victim study), and determinism studies (Atil 2024).

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Favourable parole rulings fall within a session and recover after a break | 1,112 rulings, 8 judges, 50 days; about 65% falls to near 0; 64.2% rejected overall; mean 22.58 cases/day, 5.98 min per case | Danziger 2011 [a01, a02] | [C] (K01) |
| Regression with controls: later position lowers favourable odds | decision-count coefficient -0.078 (SE 0.020); -0.111 (SE 0.018) counting non-decisions; only prior incarcerations and rehab programme consistently predicted rulings | Danziger [a03] | [C] |
| Implied effect size is very large | 65% to 5% = odds ratio 35, d = 1.96; depletion meta-analysis d about 0.10 to 0.25 after bias correction; near-tautological law-psych effects reach r = .63 (d = 1.62) | Glockner 2016; Lakens 2017 [a08, a10, b03, b05] | [E] implausible as depletion (K02) |
| Case order is not random | unrepresented prisoners about 1/3 of cases, win 15% vs 35%; excluding deferrals 67% vs 39%; Danziger data without deferrals about 75% falling to 42% | Weinshall-Margel and Shapard 2011 [a05] | [E] (K03) |
| Scheduling alone reproduces the sawtooth | simulation: 10,000 cases, 36% base rate, 60-min session; with 5 min left only 12% of favourable cases fit vs 46% of unfavourable | Glockner 2016 [a07, b02] | [S] (K04) |
| Authors' reply: effect survives representation controls | 39 shared-attorney cases with two prisoners, 4 with three; magnitudes not reported | Danziger reply [a06] | [C] (K05) |
| Ego depletion fails to replicate | 23 labs, N = 2,141, d = 0.04; 36 labs, N = 3,531, d = 0.06 (Bayes factor 4 for the null) | Hagger 2016; Vohs 2021 [b14, b15] (snippet) | [E] (K19) |
| Gambler's fallacy in asylum decisions | 0.5 pp less likely to grant after a grant; 1.1 pp non-extreme judges; up to 3.3 pp moderate judges same-day same-type; 5.5 pp after two grants; about 2% of decisions reversed | Chen 2016 [a12, b10] | [S] (K06) |
| Same in loan officers (randomised) | up to 9% of decisions reversed for moderate officers under flat pay; stronger incentives reduce it | Chen 2016 [a12, a13] | [S] |
| Irrelevant events move sentences | upset loss by local team adds about 35 days (7% of 513-day mean); no effect for upset wins, close losses or placebo games | Eren and Mocan 2018 [a15] | [S] (K07) |
| Judge noise is large | 3 of 16 cases unanimous on prison, 208 judges; 55% premium spread; psychiatrists agree on half of 426 | Clancy 1981 via Noise summary [a17, b12, a18] | [E] (K08), secondary reading |
| Judge leniency differences | most lenient quintile releases 82.9%; other quintiles 6.6, 9.6, 13.5, 22.3 pp fewer; algorithm cuts crime 14.4 to 24.7% at equal jailing | Kleinberg 2018 [b11] | [S] (K09) |
| Legal anchoring meta-analysis | 29 studies, 93 effect sizes, N = 8,549; d = 0.58 (CI 0.44 to 0.73) with control; d = 0.91 (CI 0.69 to 1.12) without | Bystranowski 2021 [b08] (snippet) | [E] (K10) |
| Real-court anchoring is smaller | 280 rulings coded: 47.7% vs 26.2% baseline, chi2(1) = 5.87, Cramer's V = 0.186 | Gao 2026 [d15] | [C] (K26) |
| Qualitative ratings consistent, numeric translation noisy | variability large for non-economic and punitive damages and sentences | Berthet 2021 [b27] | [S] (K20) |
| Time-of-day effects in other fields are small | 35,004 PI-RADS reads: hour coefficient 0.005; 16 of 20 physicians ordered more tests in first hour (sign test p = 0.012) | [b24, b25] (snippet) | [C] (K18) |
| LLM judge position consistency | GPT-4 65.0%, GPT-3.5 46.2%, Claude-v1 23.8%; few-shot lifts GPT-4 to 77.5% | Zheng 2023 [b17] | [E] (K11) |
| LLM judge verdict flips on order swap | GPT-4 conflict 37/80 = 46.3% (Vicuna-13B vs ChatGPT); Vicuna "wins" 66 of 80 under ChatGPT judge | Wang 2023 [b16] | [E] |
| Position bias direction varies | recency on MTBench, primacy on DevBench for GPT-4/3.5; 15 judges, over 150,000 instances | Shi 2025 [d07] | [S] (K23) |
| Occasion noise in LLM judges | 7-17% of verdicts change across identical replications; up to 98% flip on order swap; one judge 100% consistent and 51% accurate | Kumar 2026 [c13, d08] | [E] (K13, K21) |
| Accuracy ceiling from flips | accuracy <= 1 - flip/2; trustworthy rate T = C x (A - flip/2) | Kumar 2026 [c14, d10] | [S] (K22) |
| Temperature 0 is not deterministic | 5 LLMs, 8 tasks, 10 runs: accuracy varies up to 15% across runs | Atil 2024 [d06] | [E] (K13) |
| LLM judicial inconsistency and bias | about 15-18% at temperature 0; 14 of 15 models significantly biased; defendant wealth significant in 10 of 13 models; sentence weighted MAPE about 219% | Hu 2025 [c04-c06] | [S] (K17) |
| LLM anchoring | anchored on 22 to 61% of questions; ChatGPT high anchor 105.97 vs humans 80.50 (low 20.83 vs 22.5); diagnostic anchoring 55.6% LLMs vs 21.2% residents (OR 3.94); GPT-4 index 0.45 vs 0.61 human | Huang; Suri; Lou and Sun; diagnostic 2026 [c09, b21, b20, b23] | [C] (K14) |
| LLM anchoring mitigation | Llama-3.1-8B baseline 34.7%: knowledge enhancement 50.5% (worse), self-improving 38.4%, Anti-DP 24.7%; ignore-the-anchor, chain of thought, principles, reflection all left anchoring significant on GPT-4/4o | Huang; Lou and Sun [c10, d02-d04] | [E] simple fixes inconsistent (K15) |
| Verdict-first format | Gemini-2.5-Pro flips 56.0% to 6.9% (accuracy 63.5% to 88.5%); GPT-4o 24.0% to 33.0%; Gemini-2.0-Flash 46.0% to 90.0%; Llama-3.3-70B 26.0% to 29.7%; Claude-Sonnet-4.6 14.9% to 9.9% | Kumar 2026 [d08, d09] | [C] (K12) |
| Label anchoring in LLM explanation judging | LAO 1.00 baseline; hiding the label cut label-aligned revision to 5-22% vs 76-85% | Tapwal 2026 [c07, c08] | [S] (K16) |
| Judicial prestige and victim biases | corporate prestige award ratio 1.57x to 3.02x vs human 3.00x; virtuous-victim shift +0.5 to +1.9 points vs human +0.5 | 2026 judicial-bias audit [c01, c02] | [S] |

## 4. Mechanisms and models

Written so an engineer can build each piece.

**4.1 Noise decomposition (Kahneman et al.).** Build a matrix: rows are cases, columns are judges (or samples). System noise is the variance of judgments around the case mean, pooled over cases.
- Level noise: variance of judge means (average severity per judge).
- Pattern noise: judge-by-case interaction. Stable pattern noise is the part that repeats when the same judge sees the case again.
- Occasion noise: variance of the same judge on the same case across repeats. Measure with k repeats in fresh contexts.
- For a single LLM, the "judges" are variants you control: persona, paraphrase, order, prompt format. Occasion noise is repeat variance at a fixed prompt.
- Human template: in a labelling audit, pattern noise was the largest part of system noise (0.40/0.23 under two definitions, vs system noise 0.48/0.34, residual 0.06), and noise moved measured performance by up to about 10% [d11]. No equivalent exists for LLMs on legal tasks (K25).
- Mean squared error = bias squared + noise squared. Reducing either by the same amount cuts error equally [a19].

**4.2 Scheduling artifact model (Glockner).** Simulate N cases. Each has a type (favourable with probability 0.36) and a duration (favourable mean 8.2 min, unfavourable mean 5.8 min; normal or Weibull). Order is random. A session closes when the next case will not fit in the remaining time (60 min). Record favourable rate by position. The favourable share falls toward zero at session end with no change in judge behaviour [b02, a07]. Censoring the last 5% of cases per session and autocorrelation inflate it. Engineering use: before accepting an order effect in any log, check whether the stopping rule depends on the outcome.

**4.3 Depletion model (the rejected mechanism).** A resource drains with each decision and refills on a break. Prediction: the favourable rate declines with decision count more than with elapsed time (Danziger: r = 0.72 between position and cumulative minutes; only position stays significant [a04]). Lab replications put the depletion effect near zero (d = 0.04 to 0.06) [b14, b15]. Do not implement this in the agent [E] (K19).

**4.4 Gambler's fallacy model (Chen et al.).** The decider treats a sequence of independent binary cases as if the outcome mix should balance, so after a grant a further grant becomes less likely. Test: regress current decision on lagged decisions with case-quality controls, using randomly ordered cases. Effect weakens with stronger incentives [a13]. Same-day same-type cases are the sharpest test.

**4.5 Anchor-and-adjust.** Humans start at the anchor and adjust too little, or the anchor makes anchor-consistent information more accessible. For an LLM the operational model is simply: the number is in context and pulls the output. Measures:
- Anchoring index: (high-anchor answer - low-anchor answer) / (high anchor - low anchor), or the share of questions where the answer moves toward the anchor (Huang's "total ratio") [c09].
- A bracketing counter-anchor (a low and a high anchor together) works only if the pair brackets the truth [d02].
- Anti-DP (Huang): the model writes its own criteria before seeing the anchor; reasoning budget at most 128 tokens. Llama-3.1-8B anchored rate 34.7% to 24.7% [d03, d04].

**4.6 Position bias in pairwise judges.** Run the judge on (A, B) and on (B, A). Flip rate = share of pairs where the verdict follows position rather than content. Consistency C = agreement of repeated identical calls. Accuracy A is capped at 1 - flip/2, and the trustworthy rate is T = C x (A - flip/2) [c14, d10]. Report C and flip together: a fully consistent judge can sit at chance (C 100%, accuracy 51% [c13]). Four regions: Trustworthy, Noisy-but-fair, Chaos, Confidently biased.

**4.7 Aggregation order for noise reduction.** First average both orders (removes position bias), then ensemble k repeats (removes occasion noise) [d10]. Self-consistency gains on reasoning benchmarks: +17.9 GSM8K, +11.0 SVAMP, +12.2 AQuA, +6.4 StrategyQA, +3.9 ARC-challenge [d12; abstract]. Averaging cannot remove level or pattern noise shared across samples; this is why SCHEMA G4 says samples from one model are not independent.

**4.8 Blind judging.** Hide the candidate label or answer when auditing reasoning. Label anchoring (LAO) was 1.00 at baseline and near 0 with the blinded procedure [c07, c08].

## 5. What holds up

**Holds up.**
- Anchoring in legal judgments with humans: d = 0.58 with a control group, d = 0.91 without [b08], 29 studies. Experts are affected, and irrelevant anchors work [b07, b09]. Evidence is mostly vignettes and archival studies [d14].
- Judge noise is large; stable pattern noise tends to dominate [a16, b12].
- Ego depletion does not hold up [b14, b15, a08].
- Position bias in LLM judges is large, varies by model and is measured on many models [b16, b17, d07, c13].
- Occasion noise in LLMs exists even at temperature 0 [d06, c13, c05].
- LLM anchoring appears in every study found, though its size relative to humans varies [c09, b21, b20, b23].

**Does not hold up, or contested.**
- The hungry judge effect as a psychological effect. Order is not random, the implied effect size is implausible (OR 35, d = 1.96), and a scheduling simulation reproduces the pattern [a05, a07, a08, a10]. Defenders say it survives controls but report no magnitudes [a06, b04]. Supplementary tables S1-S15 and the reply body were not read [d13]. No randomised or preregistered replication in real courts was found. K01 and K05 stay contested.
- Time-of-day effects in medicine exist but are small (beta 0.005 per hour for PI-RADS; most physicians order more tests earlier) [b24, b25] (snippets).
- Real-court anchoring is smaller than vignette anchoring (V = 0.186 vs d = 0.58) [d15]. Different designs, so only suggestive.

**Moderators.**
- Incentives reduce the gambler's fallacy [a13].
- Expert anchors are followed more reliably by LLMs: no direction exceptions on 12 expert-anchored questions [d01]. Time questions give 6 of the 11 exceptions though they are 7 of 42 questions [d01].
- Model size does not reduce bias in judicial LLM audits and may raise inconsistency; release date has no significant effect [c06]. In anchoring batteries larger and reasoning models anchor less (27.3% GPT-4o, 22.0% Qwen3-235B thinking vs 60.5% Qwen2.5-0.5B) [c09].
- Temperature trades bias for noise: higher temperature lowers measured bias because randomness masks it [c05], and lowers consistency by 12.1 points [c14].
- Position-bias direction depends on task and mainly on the quality gap between answers, not prompt length [d07].

**Interventions that worked.**
- Both-order evaluation and few-shot examples: GPT-4 consistency 65.0% to 77.5% [b17].
- Verdict-first output, for Gemini-2.5-Pro only [d08, d09].
- Hiding labels when judging explanations [c08].
- Anti-DP "own criteria first": 34.7% to 24.7% on Llama-3.1-8B; no gain on Qwen2.5-7B (40.0% to 40.8%) [c10, d03].
- A bracketing counter-anchor, only when the pair brackets the truth [d02].
- Stronger incentives for human sequential bias [a13].
- Self-help rewrites of biased prompts reduced biased parts to 0 for group attribution on GPT-4 [c12]; the effect depends on size (change rates GPT-3.5 0.052, GPT-4 0.175, Llama-2-13b 0.521, Llama-2-7b 0.399) [c12].

**Interventions that did not work.**
- Telling GPT-4 or GPT-4o to ignore the anchor, chain of thought, principles, reflection: all left anchoring significant [d02].
- Knowledge enhancement made anchoring worse (34.7% to 50.5%); self-improving prompts made Qwen2.5-7B worse (40.0% to 48.0%) [c10].
- Verdict-first output hurt GPT-4o (24.0% to 33.0%), Gemini-2.0-Flash (46.0% to 90.0%) and Llama-3.3-70B (26.0% to 29.7%) [d09].
- Adversarial fine-tuning of Llama-3.1-8B: 34.7% to 33.3%, no real change [d03].

## 6. Language models

**Judge position bias.** Zheng et al. (2023), MT-Bench and Chatbot Arena: position consistency GPT-4 65.0% (prefers first 30.0%, second 5.0%), GPT-3.5 46.2% (50.0% prefer first), Claude-v1 23.8% (75.0% prefer first). Few-shot raised GPT-4 to 77.5% [b17]. Wang et al. (2023): with ChatGPT as judge, Vicuna-13B beat ChatGPT on 66 of 80 queries depending on order; GPT-4 verdict conflicts 46.3% (37 of 80) when order is swapped. A ChatGPT judge reached 44.4% accuracy vs human labels in the vanilla setting, with gains from multiple evidence plus balanced position calibration [b16]. Shi et al. (2025): 15 judges, over 150,000 instances; GPT-4 and GPT-3.5 preferred the later answer on MTBench but the earlier on DevBench; the quality gap matters more than prompt length [d07]. Ye et al. (2024): position robustness below 0.5 for most judges with more candidates; self-enhancement bias in most [b22]. Lu et al. (2022): all 24 orderings of 4 training examples on SST-2 gave very different results from 0.1B to 175B parameters; entropy-based selection gave about 13% relative gain [b18].

**Repeat noise.** Kumar et al. (2026): 6 models, 4 benchmarks, 5 formats, 2 orders, 3 temperatures, 10 repeats. 7-17% of verdicts change across identical replications; up to 98% flip on order swap (Gemini-2.0-Flash, verdict-first, JudgeBench, T = 2.0%). Temperature reduces consistency by 12.1 points [c13, c14, d08]. Atil et al. (2024): accuracy varies up to 15% across 10 runs at nominal determinism, 5 models, 8 tasks [d06].

**Anchoring.**
- Suri et al. (2023): ChatGPT low anchor 20.83, high anchor 105.97, vs humans 22.5 and 80.50 [b21].
- Lou and Sun (2024): 162 answer-difference values across GPT-4, GPT-4o, GPT-3.5, only 11 with the wrong sign; GPT-4 index about 0.45 vs 0.61 in the human dataset [b20, d01]. This is the one result where the LLM is below the human level.
- Huang et al. (2025/2026): anchored share by model: Qwen2.5-0.5B 60.5%, Mistral-7B 51.1%, Llama-3.1-8B 34.7%, GPT-4o 27.3%, DeepSeek-R1 25.0%, Qwen3-235B thinking 22.0% [c09]. Human A-Index 0.4-0.6; most LLMs equal or worse.
- Diagnostic vignettes (2026; snippet): anchor diagnosis ranked first in 55.6% of LLM runs (40 of 72) vs 21.2% of residents (17 of 80) and 10.0% of attendings (2 of 20); OR 3.94 [b23].
- Echterhoff et al. (2024), 13,465 prompts: GPT-4 admitted 40.5% more students under reject framing; Llama-2 7B classed 32.1% fewer females as good at math; models prefer first options (A, B) [b19, c11].
- Grander et al. (2026): 2,028 observations (507 human, 1,521 LLM), three languages [d16]; result numbers not extracted.

**Judicial audits.** Hu et al. (2025): 16 LLMs, 177,100 case facts built from 1,100 judicial documents. At temperature 0, 14 of 15 models showed significant bias and imbalanced inaccuracy. Inconsistency about 15-18%. Defendant wealth significant in 10 of 13 models. Size does not help. Sentence weighted MAPE about 219% [c04-c06]. The 2026 virtuous-victim audit (ChatGPT 5 Instant and Thinking, DeepSeek V3.1, Claude Sonnet 4, Gemini 2.5 Flash): corporate prestige award ratios 1.98, 1.57, 2.11, 2.02, 3.02 vs human 3.00; virtuous-victim shifts +0.5 to +1.9 points vs human +0.5; occupational prestige sentence differences from -0.27 to +1.07 years vs human about +0.67 [c01-c03]. Ayal et al. (2026) compare GPT, Gemini and Claude with 123 retired judges on 2 cases; numbers not extracted [c16].

**Label anchoring.** Five 7-9B judge models show LAO = 1.00 at baseline; a blinded procedure drops label-aligned revision from 76-85% to 5-22% [c07, c08].

**Position drift in long context (gap).** No study of decision-rate drift across a sequence of cases in an LLM was found [c21]. Nearest: Lost in the Middle, where GPT-3.5 multi-document QA drops by more than 20% at the worst position, and falls below closed-book (56.1%) at 20 and 30 documents [d05]. That is retrieval, not a decision rate.

**Reading across.** LLMs show the same bias types as human judges, at similar size or worse, but the cause differs (context attention, training), so human mitigations do not transfer automatically. Temperature 0 does not remove noise. The cheapest working fixes are structural (both orders, hide labels, repeat and vote), not verbal ("ignore the anchor").

## 7. What our agent should take

### Add now (established)

| Item | Schema part | Status | Evidence ids |
|---|---|---|---|
| For any pairwise comparison inside the agent (candidate selection, judge steps), run both orders in code and keep only order-consistent verdicts; treat inconsistent pairs as ties or re-test | G5 / S7 SELECT | [E] | b16, b17, c13, d07, d08; K11 |
| Do not treat temperature 0 as determinism. Where an answer matters, use a code-side vote of k independent attempts, as S3 already does | S3 / G4 | [E] | d06, c13, c05; K13, K21 |
| Keep S1 input hygiene: move suggestive numbers (stated guesses, demands, irrelevant figures) into a marked block. Harm is established; the remedy is [S] | S1 | [E] harm, [S] remedy | b08, b21, c09, b19; K10, K14 |
| Do not add generic "ignore the anchor" or "be unbiased" instructions, nor self-improving or knowledge-enhancement prompts, without a head-to-head test. Matches section 4b | 4b | [E] | d02, c10, c12; K15 |
| Do not model fatigue or ego depletion; no "rest" state | none | [E] | b14, b15, a08; K19 |
| Randomise item order in every bench run so scheduling artifacts are not mistaken for drift | bench method | [E] | a05, a07; K03 |
| Report consistency C and flip rate together, never consistency alone | measurement | [S] built on [E] flip data | c13, c14, d10; K22 |

### Test first

| Item | Schema part | Status | Evidence ids |
|---|---|---|---|
| Both-orders then k repeats on legal vignettes vs one call, equal tokens | O / S3 | [S] | d10, d12; K24 |
| Blind judging: hide candidate label or answer when auditing reasoning | G5 / S8 | [S] | c07, c08; K16 |
| Anti-DP: write own criteria before reading any number | S1 | [S] | c10, d03, d04; K15 |
| Bracketing counter-anchor, only when the pair brackets the truth | S1 | [S] | d02; K15 |
| Verdict-first output format, per judge model, only after a swap-order test | O (format) | [C] | c14, d09; K12 |
| Sequence-contamination guard: decide each item in a fresh context | G | [S] | a12, b10; K06 |
| Late-position drift check for long-context runs | G (late-run default) | [C] | d05, c21; K18, K27 |
| Counterfactual swap of irrelevant attributes (wealth, prestige, victim) | G | [S] | c01-c06; K17 |
| Relative or ranked output instead of absolute numbers for open-scale judgments | O | [S] | b27; K20 |
| Variance decomposition (level, pattern, occasion) as a bench diagnostic | measurement | [S] | d11, a16; K25 |

## 8. Concrete tests on our bench

All tests: both arms at equal total tokens; items in random order; at least 3 seeds.

| # | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 | About 100 pairs of candidate answers with known winner | (a) one call, fixed order; (b) two calls in both orders, keep consistent, tie-break by third call | accuracy; flip rate; T = C x (A - flip/2) | flip rate down; accuracy up when single-call flip rate exceeds 20% |
| T2 | Same legal vignette (sentence or damages) run k = 10 times | plain vs vote of k fresh-context attempts (median for numbers) | share of runs disagreeing with modal verdict; numeric SD | single-call disagreement in the 7-17% range; vote cuts occasion noise, not level noise |
| T3 | About 40 numeric estimation items with a planted low or high anchor | plain; S1 hygiene; Anti-DP; bracketing pair | anchoring index; share of questions moved toward anchor | hygiene or Anti-DP cut anchored share by several points (Anti-DP got 10 points on Llama-3.1-8B); an "ignore" instruction does nothing |
| T4 | Sentencing or damages vignette with a random demand | plain vs hygiene vs blind-to-demand | shift per unit of demand | humans d about 0.58; expect clear shift in plain arm |
| T5 | 30 to 50 equal-difficulty yes/no cases in one long context, random order | continuous context vs fresh context per case | slope of accept rate on position; last third vs first third | probably null for strong models; any slope in the continuous arm shows drift |
| T6 | Binary decisions in sequence with random truth | previous answer visible vs hidden | P(same as previous) minus base rate | gambler's fallacy analogue; expect small or none |
| T7 | Irrelevant-attribute counterfactuals (wealth, prestige, victim age, mood sentence) | original vs swapped; blind vs plain | outcome shift, paired | shift above zero in plain arm; blinding closes it |
| T8 | Reasoning audits | judge sees proposed label vs hidden label | label-aligned revision rate | falls from about 80% to under 25% as in the small-judge study |
| T9 | Open-scale numeric judgments | absolute number vs rank among reference cases | agreement with reference panel; run-to-run SD | rank output less noisy (scale-use noise) |
| T10 | Pairwise judging per model | verdict-first vs reasoning-first, both orders | flip rate | judge-specific; adopt only where flips fall |

## 9. What does not transfer, and why

- **Fatigue and hunger.** An LLM has no glucose and no depletion, and the human effect is itself in doubt. The only analogue is context-length drift, which needs its own test.
- **Session scheduling artifacts.** They come from a clock-driven stop. Our agent has no such rule, but any bench with a time or token cut-off could create the same outcome-dependent stopping artifact.
- **Vignette effect sizes.** Anchoring d = 0.58 is from vignettes. Real-court archival coding gave V = 0.186 [d15]. Do not expect vignette sizes on deployed tasks.
- **Human mitigations.** Incentives, training and awareness do not map onto a model. Awareness prompts fail partly even in LLMs [d02, c10]; section 4b already says debias instructions do not reliably work.
- **Judge-specific format effects.** Verdict-first helped one model and hurt four [d09]. Nothing found on one judge generalises.
- **Synthetic judicial audits.** The 219% sentence error shows they do not test real-court validity [c06].
- **Group-level legal fixes** (panels, appellate review, sentencing guidelines) address level and pattern noise across people. Our agent is one model whose samples are correlated (G4).

## 10. Open questions

1. Does an LLM agent show decision-rate drift by position in a long context? No studies found [c21, d05].
2. What is left of the Danziger effect once representation, deferrals and case duration are controlled? Tables S1-S15 and the reply body were not read [d13].
3. Is there any preregistered or randomised replication of order effects in real judicial decisions? None found.
4. Which debiasing steps cut LLM anchoring at equal tokens, and when do they backfire? Partly answered, never at equal tokens [c10, d02].
5. What are level, pattern and occasion noise for LLM judges on legal tasks? Only the human labelling template exists [d11].
6. Does averaging k samples remove noise without removing real judgment in legal vignettes?
7. Do real-court sentences or damages show anchoring as large as the meta-analysis implies?
8. Does the numeric translation step produce most LLM sentence variance, as in humans?
9. Do verdict-first and swap-order results generalise beyond JudgeBench and the six judges? The judge-to-row mapping in one table was inferred [d09].
10. Source gaps: Englich 2006 and Tversky and Kahneman 1974 numbers are unverified; the Noise book was read only through summaries; Bystranowski, Vohs, Hagger and the 2026 diagnostic-anchoring numbers rest on abstracts. Use 2 to 28 completed cases per session (an earlier note said 283; that was a footnote marker) and N = 2,141 for Hagger.

## 11. Sources

[V] = opened and read this run; [M] = snippet or abstract only.

- [V] Danziger, Levav, Avnaim-Pesso (2011), Extraneous factors in judicial decisions. https://pmc.ncbi.nlm.nih.gov/articles/PMC3084045/ (PNAS DOI https://doi.org/10.1073/pnas.1018033108 [M]; supplements not read)
- [V] Weinshall-Margel and Shapard (2011), Overlooked factors in the analysis of parole decisions. https://pmc.ncbi.nlm.nih.gov/articles/PMC3198355/
- [V] Danziger et al. (2011), Reply. https://pmc.ncbi.nlm.nih.gov/articles/PMC3198336/ (DOI https://doi.org/10.1073/pnas.1112190108 [M])
- [V] Glockner (2016), The irrational hungry judge effect revisited. https://journal.sjdm.org/16/16823/jdm16823.html
- [V] Lakens (2017), Impossibly hungry judges. https://daniellakens.blogspot.com/2017/07/impossibly-hungry-judges.html
- [M] Chatziathanasiou (2022), Beware the lure of narratives. https://doi.org/10.1017/glj.2022.32 (a11 read a summary; b26 and c20 could not fetch the page)
- [V] Chen, Moskowitz, Shue (2016), Decision-making under the gambler's fallacy. https://www.nber.org/papers/w22026
- [V] Eren and Mocan (2018), Emotional judges and unlucky juveniles. https://www.nber.org/papers/w22611
- [V] Kahneman, Sibony, Sunstein (2021), Noise, via Wikipedia summary. https://en.wikipedia.org/wiki/Noise:_A_Flaw_in_Human_Judgment
- [V] Kleinberg et al. (2018), Human decisions and machine predictions. https://pmc.ncbi.nlm.nih.gov/articles/PMC5947971/
- [V] Berthet (2021), Impact of cognitive biases on professionals' decision-making. https://pmc.ncbi.nlm.nih.gov/articles/PMC8763848/
- [V] Assessing judges' use and awareness of cognitive heuristics (2025). https://pmc.ncbi.nlm.nih.gov/articles/PMC13281065/
- [V] Gao (2026), Debiasing paradox in valuation-adjustment rulings. https://pmc.ncbi.nlm.nih.gov/articles/PMC13557963/
- [V] Wikipedia, Hungry judge effect (no numbers used). https://en.wikipedia.org/wiki/Hungry_judge_effect
- [V] Law and psychology must think critically about effect sizes (2023; keyword search only). https://pmc.ncbi.nlm.nih.gov/articles/PMC9835737/
- [M] Bystranowski et al. (2021), Anchoring in legal decision-making: meta-analysis. https://doi.org/10.1037/lhb0000438
- [M] Englich, Mussweiler, Strack (2006), Playing dice with criminal sentences. https://doi.org/10.1177/0146167205282152
- [M] Tversky and Kahneman (1974). https://doi.org/10.1126/science.185.4157.1124
- [M] Hagger et al. (2016), Ego depletion multilab replication. https://doi.org/10.1177/1745691616652873
- [M] Vohs et al. (2021), Multisite test of ego depletion. https://doi.org/10.1177/0956797621989733
- [M] Prostate MRI hungry judge (2024). https://doi.org/10.1016/j.ejrad.2024.111665
- [M] Time-of-day changes in physician clinical decision making. https://doi.org/10.1371/journal.pone.0257500
- [M] LLMs exhibit greater diagnostic anchoring than physicians (2026). https://doi.org/10.1016/j.ijmedinf.2026.106550
- [V] Wang et al. (2023), LLMs are not fair evaluators. https://arxiv.org/abs/2305.17926
- [V] Zheng et al. (2023), Judging LLM-as-a-judge. https://arxiv.org/abs/2306.05685
- [V] Lu et al. (2022), Fantastically ordered prompts. https://arxiv.org/abs/2104.08786
- [V] Echterhoff et al. (2024), Cognitive bias in decision-making with LLMs. https://arxiv.org/abs/2403.00811
- [V] Lou and Sun (2024), Anchoring bias in LLMs. https://arxiv.org/abs/2412.06593
- [V] Suri et al. (2023), Do LLMs show decision heuristics similar to humans. https://arxiv.org/abs/2305.04400
- [V] Ye et al. (2024), Justice or prejudice? https://arxiv.org/abs/2410.02736
- [V] Assessing cognitive biases in LLMs for judicial decision support (2026). https://arxiv.org/html/2603.10016v1
- [V] Hu et al. (2025), LLMs on Trial. https://arxiv.org/html/2507.10852v1
- [V] Tapwal, Kumar, Maple (2026), Faithful or Fabricated? https://arxiv.org/abs/2605.23970
- [V] Huang et al. (2025/2026), Anchoring effect of LLM with synthetic data. https://arxiv.org/pdf/2505.15392
- [V] Kumar, Rathore, Moitra (2026), All Verdicts are Not Equal. https://aclanthology.org/2026.aacl-long.207.pdf
- [V] Ayal, Elyoseph, Solomon (2026), LLMs as judicial decision-makers. https://cris.haifa.ac.il/en/publications/evaluating-large-la
- [V] Zambrano (2025), The Judge Variable. https://arxiv.org/pdf/2507.13732
- [V] Zhang and Xu (2025), Consistency-Acceptability Divergence. https://arxiv.org/pdf/2507.08881
- [V] Liu et al. (2024), Lost in the Middle. https://arxiv.org/abs/2307.03172
- [V] Atil et al. (2024), Non-determinism of deterministic LLM settings. https://arxiv.org/pdf/2408.04667
- [V] Shi et al. (2025), Judging the Judges. https://arxiv.org/abs/2406.07791
- [V] Kejriwal et al. (2024), A noise audit of human-labeled benchmarks. https://pmc.ncbi.nlm.nih.gov/articles/PMC11016068/
- [V] Wang et al. (2023), Self-consistency. https://arxiv.org/abs/2203.11171
- [V] Grander, Mosub, Kordova (2026), Cognitive biases in LLMs across languages. https://pmc.ncbi.nlm.nih.gov/articles/PMC13318900/
- [M] Journal of Law and Analytics (2025), human-AI interaction bias among 139 Chinese judges. https://academic.oup.com/jla/article/16/1/235/7941565
- [M] National Law Review (2025), Same question, different answers. https://natlawreview.com/article/same-question-different-answers
- [M] Apart Research hackathon (2025), noise audit of repeated LLM legal judgments. https://mindyng.github.io/cv/
- [M] Englich and Mussweiler (2001), cited in https://arxiv.org/pdf/2603.10016

## Source audit (2026-11-20)

Fresh auditors re-opened the sources of 7 established claims: 5 confirmed as written, 2 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **E11.08-K03** (reworded: the sources support less). Order non-randomness and unrepresented-last are Weinshall-Margel and Shapard's finding from their own data; the 'judges end sessions after unfavourable short cases' part is Glockner's simulation-based inference, not an observed finding, and the original authors dispute the rival explanations. Corrected claim: Weinshall-Margel and Shapard (2011) report that case order in parole hearings is not random: unrepresented prisoners (about a third of cases) usually go last in a session and win less (15% vs 35%). Glockner (2016) argues, from simulation, that because favorable rulings take longer (7.37 vs 5.21 min) judges may end sessions after short unfavorable cases, which can mimic a break effect.
- **E11.08-K10** (now contested: a source does not say this). Neither listed source (Berthet 2021 review, Gao 2026) contains the 29-study meta-analysis or d=0.58/0.91; they support only the dice-throw sentencing anchoring (Englich 2006) and archival anchoring rates.
- **E11.08-K08** (now single-source: only one opened source, code check).
- **E11.08-K19** (now single-source: only one opened source, code check).
