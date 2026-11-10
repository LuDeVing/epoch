# Training: deep document

*Subfield E03.03. Source files in this folder: evidence_a-d.jsonl (ids a01-a32, b01-b29, c01-c25, d01-d18), claims.jsonl (K01-K26), critique.md. Links to other subfields in this run are noted, not covered: Calibration and overconfidence, Aggregation and extremizing, Debiasing and cognitive forcing, Belief updating, Training and tutors, Systematic review of SAT evidence.*

## 1. What it is

"Training" here means a short lesson that teaches people to make better probability forecasts. The core case is the CHAMPS KNOW module from the Good Judgment Project (GJP). It is under one hour, online, and teaches probability and the outside view (use base rates and comparison classes), updating on evidence, averaging, calibration and biases. Key works: Chang, Chen, Mellers and Tetlock 2016 (four yearly randomized tests) and Moore et al. 2017 (overconfidence over a year, N=2,860).

The claim in SUBFIELDS.md is "the reported effect lasted at least a year". That claim comes from a secondary source (AI Impacts, b14). The primary data support it only in part (section 5).

Why it matters for our agent. Our agent is a scaffold, not a trained model. We cannot give a language model a one-hour lesson that sticks. What we can do is turn the lesson's content into fixed steps (a reference-class step, a calibration step, an update step) and test them. The LLM evidence says this transfer is weak: prompting a model with the same ideas barely helped and some prompts hurt (section 6). So this subfield is mostly a source of (a) hypotheses to test, (b) things not to add, and (c) a measuring discipline.

Three kinds of "training" appear in the evidence, and they must not be mixed up:
1. Human lessons (Chang, Moore, Mellers 2014, Kelly and Mandel 2024, Doussau 2023, Savage 2021).
2. Prompt-level "training" of an LLM: put the lesson's instructions in the prompt (Schoenegger 2025, Pratt 2024, Halawi scratchpad).
3. Weight-level training of an LLM on resolved outcomes (Turtel 2025, Halawi fine-tune, Chandak 2025). This is outside our scaffold scope and serves as a ceiling reference.

## 2. History and theories in depth

**Lab calibration training (1980 to 2000).** Lichtenstein and Fischhoff 1980: 45 minutes of training, then 22 one-hour test sessions, on general-knowledge items (a16). Stone and Opel 2000: 6 test sessions of 2 hours (a17). Moore et al. describe both as showing less overconfidence, but with decay over time and weak transfer (a10, d07). We did not open either original, so we have no numbers from them. These were long, costly programmes tested on trivia, not forecasts.

**Teaching statistics (1980s to 1990s).** Fong, Krantz and Nisbett 1986 and Lehman and Nisbett 1990 showed that short statistical training raises use of statistical reasoning on everyday problems (a18, a20, not opened). Chang et al. cite a weak link (r=0.16, p<.06) between SAT score and the gain. Sedlmeier and Gigerenzer 2001 showed that teaching natural frequencies raises Bayesian reasoning in under two hours (a21, not opened). Larrick, Morgan and Nisbett 1990 taught cost-benefit reasoning (a19, not opened).

**Debiasing theory.** Chang et al. review the field (a06, b09). Information-only (didactic) debiasing is cheapest and weakest. Process-based techniques do better: reference-class forecasting, asking the same question twice, explaining reasoning patterns, frequency formats. Feedback helps calibration and resolution. This is the design logic behind CHAMPS KNOW.

**GJP training experiments.**
- Mellers et al. 2014 (a12 to a15): first randomized field test, years 1 and 2 of the IARPA tournament. Probability training beat scenario training, which beat no training. About 45 minutes. It improved both calibration and resolution. Training and teaming effects held after controlling for timing of first forecast and number of updates.
- Chang et al. 2016 (a01 to a05, b01 to b09, d01 to d05): four years. The module changed each year (section 3). Which part of the module works was not tested by design.
- Moore et al. 2017 (a07 to a11, d06): over 494,552 forecasts, training cut overconfidence and the cut held across the forecasting year.

**Theory of what the module does.** Three explanations compete.
1. *Better probabilistic method*: comparison classes and base rates give better starting points. Supported only by correlational data (Chang Tables 5 to 7).
2. *Targeted practice*: trained people made more forecasts per question, which carried part of the effect. Supported in Y1 and Y3 only (d02).
3. *Lower confidence*: most of the calibration gain is a drop in stated confidence, with hit rate up only about 0.8 points (a08, d06).

These are not exclusive. The data cannot separate them.

**Contested ground.** An independent replication of the one-hour module was not found (K02). The nearest outside work tests different training (Kelly and Mandel 2024, d08; Stone et al. 2023, d09). A negative case: Doussau et al. 2023, a 3 to 4 minute feedback module did not help experts forecast cancer trials (b11).

**Move to LLMs (2022 to 2026).** Early work showed LLMs were poor forecasters (Zou 2022, Halawi 2024, Schoenegger and Park 2023). Authors then tried (a) human-style prompts, (b) retrieval, (c) fine-tuning on resolved outcomes, (d) RL with Brier reward. Result so far: retrieval and weight training move the score; lesson-in-the-prompt does not.

## 3. Core findings with exact numbers

Status key: established = two or more independent sources; single-source; contested; human-only; LLM-only.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Module beats random control every year | Raw Brier control vs trained: Y1 0.42 vs 0.38 (n 152 vs 119 prob., 113 scenario), 10% and 11%; Y2 0.39 vs 0.34 (194 vs 205), 12%, t(395)=5.95; Y3 0.34 vs 0.32 (116 vs 97), 6%, t(207)=2.32, p=.021; Y4 0.38 vs 0.35, 7%, t(225)=2.20, p=.028. Y1 F(2,381)=12.1 | Chang 2016 (a01, b02, b03, d01) | single-source (one team) |
| Earlier randomized test | Y1 F(2,1586)=14.29; probability vs scenario t(1053)=2.23, p=.026; Y2 probability vs none F(1,882)=19.12 | Mellers 2014 (a12) | single-source (same team) |
| Training improved calibration and resolution | Calibration Y1 F=3.16, p=.04; resolution Y1 F=18.50, p<.001; Y2 F=16.23 | Mellers 2014 (a13) | single-source |
| Effect shrank as module grew | 12% (Y2) to 6 to 7% (Y3, Y4) | Chang (a01) | single-source |
| Veterans kept in condition still show effect | Y2 0.39 vs 0.34 (n 148/153); Y3 0.36 vs 0.33 (n 56/53). New forecasters Y2 13%, Y3 3% | Chang Table 9 (d03) | contested (confounds: attrition, revised module, continuous Brier feedback) |
| Prior experience alone does not help | Veteran main effect not significant; training significant | Chang (b08) | single-source |
| Only comparison classes tied to better scores | Std Brier: comparison classes 0.17 (n=580); math models 0.26; select 0.26; hunt 0.38 (n=2,992); post-mortem 1.04 (n=88); control 0.49; all trained 0.42. ANOVA F=12.28, p<.001 | Chang Tables 5 to 7 (a03, b04, d05) | single-source, correlational |
| Probabilistic principles helped, political ones did not | Prob. MS=38.51, F=11.96, p<.001; political MS=0.24, F=0.08, p=.783 | Chang (b05) | single-source, correlational |
| Training raised forecasts per question, not total | Per question (control/trained): Y1 1.35/1.58; Y2 1.47/1.56; Y3 1.90/4.27; Y4 2.53/3.11. Totals per person 127.8 vs 139.0 (Y2) etc. | Chang Tables 8, 10 (d04) | single-source |
| Mediation by forecasts per question | Y1 indirect -0.02, CI -0.04 to -0.01, p=.01; Y3 -0.02, p=.05; Y2 and Y4 not significant (Y4 p=.20). Paper summary says "three of four years" | Chang (d02) | established as a reading of the text: both Y2 and Y4 fail |
| Ability and training independent | Training had highest explanatory power; ability predicted all four years; interaction only Y1; together 10 to 20% variance | Chang (a05, b07) | single-source |
| Overconfidence halved | Overconfidence: solo 4.3 to 2.0; team 2.8 to 0.7. Confidence 64.9 to 63.5; hit rate 60.7 to 61.5 (solo), 62.9 to 63.6 (team). N=2,860, 344 questions, 3 years | Moore 2017 Table 1 (a07, a08, d06) | single-source (re-read in source; Bonferroni CI groups only) |
| Self-rated expertise not predictive | CI curves for levels 1 to 5 not reliably different | Moore (a11) | single-source |
| Earlier lab training decays, transfers weakly | 45 min + 22 sessions; 6 x 2 h sessions (second-hand) | Moore description (a10, d07) | single-source, originals unread |
| Calibration training can shift bias, not skill | 70 analysts, miscalibration .33 to .18, F(1,69)=59.48; interval bias d=1.17 down; binary bias d=0.37 up (underconfidence); cross-task r=-.06 and -.10; no control group | Kelly and Mandel 2024 (d08) | single-source |
| Brief expert training failed | 148 analyzed of 216; 25 trials; Brier 0.22 vs 0.21, p=.51; AUC 0.70 vs 0.73; pooled crowd 0.17 | Doussau 2023 (b11, b12) | single-source |
| Two short videos widened intervals but not enough | N=133; 8 of 10 questions widened (4 after Bonferroni); hit rates stayed under 0.80 target | Savage 2021 (b10) | single-source |
| Extra module did not change top-forecaster yield | 195 engaged; top 10%: 9 vs 7; top 25%: 24 vs 14; not significant | Superforecasting reality check 2020 (b13) | single-source, small |
| Human lesson as LLM prompt: no robust gain | Mixed model: Frequency-Based -0.014, Base Rate First -0.011, CoT -0.011, Step-Back -0.011 (adj p=.774). t-tests: -0.019 (adj p=.022), -0.016 (adj p=.036). Control Brier about 0.21. 38 prompts, 4 models, 100 questions | Schoenegger 2025 (a22, b18, c08, d10) | LLM-only, single-source |
| Bayesian and propose-evaluate-select prompts hurt | Mixed +0.030 and +0.033; t-tests +0.025 (adj p=.036), +0.028 (adj p=.010). Distance from 50%: 0.199, 0.175 vs control 0.134 | Schoenegger 2025 (a23, c09, d11) | LLM-only, single-source |
| Anti-overconfidence prompt did nothing | 0.000 mixed, -0.004 t-test | Schoenegger 2025 (d10) | LLM-only |
| Study 2: no prompt helped o1 and o1-mini | o1 0.216, o1-mini 0.217; All Human -0.009, Base Rate+Frequency -0.004 (adj p .985); superforecaster odds-ratio prompt +0.023 worse | Schoenegger 2025 (a24, b19, d12) | LLM-only |
| Retrieval and fine-tune carry the gain, not the prompt | Full 0.179; no fine-tune 0.186; no fine-tune, no retrieval 0.206; plain baseline 0.208; crowd 0.149 | Halawi 2024 (a25, c03, d14) | LLM-only, single-source |
| Base-rate pipeline lost to a one-line prompt | Basic 0.1221; base rates 0.1562; rationale-first 0.1483; human market 0.1334 (351 events) | Pratt 2024 (d13) | LLM-only, single-source |
| RL on outcomes with Brier reward | 14B base 0.215 (ECE .089); ReMax 0.190 [.178,.203] (ECE .062); GRPO 0.192 (.054); o1 0.202 (.093); market 0.151 (.043). 1,265 test questions. Label-shuffled control 0.221 to 0.214 | Turtel 2025 (a30, b16, c13, c14) | LLM-only, single-source |
| Reward design matters | Accuracy-only reward worse than constant; Brier-only gives "Unknown" in about 40% of samples vs about 4% | Chandak 2025 (b22) | LLM-only |
| Calibration RL on QA | ECE .37 to .03 (HotpotQA), .26 to .10 (math) | Damani 2025 (b23) | LLM-only, not forecasting |
| Giving LLM the human median helps | GPT-4 .17 to .14; Claude 2 .22 to .15; update size vs gap r=.88; accuracy +17 to 28% | Schoenegger 2024 (a29, c06) | LLM-only |
| LLM crowd matches human crowd | 12 LLMs 0.20 vs 925 humans 0.19, t(60)=.19, p=.85; 31 questions | Schoenegger 2024 (c05) | LLM-only, small set |
| LLM advisor helps humans | N=991; +24 to 28% accuracy; outlier-driven | Schoenegger 2024 (b24, c07) | LLM-only |
| Top LLMs near but below superforecasters | ForecastBench: superforecasters .096, public .121, best LLM .122 (with crowd freeze values); combination .076/.096/.130 (GPT-4o). Lu: o3 .1352, o3-pro .1386 (.1307 hold-out), GPT-4o .1883 | Karger 2025, Lu 2025 (a26, a27, c11, c12) | established across sets (not comparable) |
| Ensembling helps the agent, not the base model | RTF 0.169 vs 0.180 single; base GPT-4o 0.218 vs 0.210 | Hsieh 2024 (a31, c16) | single-source |
| Evaluation is easily contaminated | Retrieval date filters leak; pastcasting runs vary under 20% to over 80%; consistency checks correlate with Brier | Paleka 2024, 2025; FutureSearch 2025 (c15, c17, c18) | established |
| Worked examples may teach updating | Bayesian-demonstration tuning beats oracle tuning; Bayesian assistant 81% vs humans 58%; plain LLMs plateau after round 1 | Qiu 2025 (c19, d15) | LLM-only, not forecasting |

## 4. Mechanisms and models

Each item below is written so it can be implemented as code or as a fixed scaffold step.

**4.1 Reference-class step (the best-supported human component).**
Procedure. (1) Model lists 2 to 3 comparison classes for the event and gives for each a count or rate of how often the event happened. (2) Code takes the base rate (median of the class rates). (3) Model lists specific evidence that moves the case from the base rate. (4) Final probability is the base rate moved by a capped amount. Implementation hook: code sets the cap, for example no more than 0.25 from the base rate without a cited reason. Evidence: Chang principle C had std Brier 0.17 vs 0.42 for all trained (a03). The LLM prompt analogue gave -0.011 to -0.019, not robust (a22). So the human result may rely on people choosing hard-to-find classes, or on selection into the principle. This step must be tested, not assumed.

**4.2 Calibration as shrinkage, not skill.**
Moore's gain is mostly lower confidence (confidence -1.4 points, hit rate +0.8). Implement as a code step: take the model's probability p, apply a monotone map fitted on resolved items of the same class: p' = sigmoid(a * logit(p) + b), with a below 1 if the model is overconfident. Fit a and b on a rolling window of past resolved questions. Log ECE and hit rate. Kelly and Mandel warn that shrink on one task type can push another toward underconfidence (binary bias d=0.37 up), so fit per task type and check both ends of the range.

**4.3 Forecast spread guard.**
Schoenegger: the two harmful prompts were the two with the greatest mean distance from 50% (0.199, 0.175). CoT was also far (0.172) and did not hurt, so distance alone is not the cause (d11). Implement as a monitor: log mean distance from 50% per mode; alert when a mode is more than 0.04 above the plain mode without a Brier gain. A shrink step is untested.

**4.4 Constant-base-rate control.**
Pratt: prompt-induced shifts in the overall probability level create or hide Brier effects because most events resolve No (d13, K25). Implement: every forecast arm is scored against (a) a constant forecast at the set's base rate, (b) the plain prompt, and (c) a reversed-question version (ask for the negated event, enforce p + p' = 1). Report the weighted Brier (Yes and No events equal) beside Brier.

**4.5 Practice-with-feedback as memory (the machine analogue of Chang's practice).**
Chang: training raised forecasts per question and part of the effect ran through it (Y1, Y3). Moore: forecasters also got continuous Brier feedback. Implementation: a class record in code (SCHEMA section 5) storing, per problem class, past forecast, outcome and Brier. Feed back only a one-line lesson after the first attempt (SCHEMA memory rule), never before. This is the cheapest weight-free version of outcome training.

**4.6 Update rounds.**
Mellers 2014: calibration is worst at 100% forecasts from lack of updating (a13). A fixed scaffold: after retrieval of new evidence, one update round with a cap on step size. Chang mediation is only partial support (Y1, Y3). Treat as a hypothesis.

**4.7 Outcome training (ceiling reference).**
Turtel: 10,000 Polymarket questions plus 100,000 synthetic, reward = negative Brier, with collapse prevention. Effect: -0.025 Brier, ECE .089 to .062. Reward design matters: accuracy-only is worse than constant; Brier-only yields "Unknown" in about 40% (Chandak). Not part of our scaffold, but it sets what a weight change buys: about 0.025.

**4.8 Aggregation in code.**
Median or mean of N independent short samples, done in code (G5, G4). Evidence: LLM crowd of 12 matches human crowd (c05); Doussau pooled crowd 0.17 vs individuals 0.21 to 0.22 (b12); but base GPT-4o ensemble was worse (0.218 vs 0.210) while agent ensemble was better (c16). No extremizing (G4).

## 5. What holds up

**Holds up (with limits).**
- The module beat random controls in four straight years, 6 to 12% on Brier (a01). Randomized at entry. Replication inside one research programme, so independence is 1 (K02).
- Overconfidence fell from 4.3 to 2.0 (solo) and 2.8 to 0.7 (team) in a large field sample, re-read from the source (d06).
- Experience alone did not help; training did (b08).
- Comparison-class use was the best predictor among trained principles (a03), but only correlationally.
- Pooling beats individuals and beats training for experts (b12).
- Retrieval beats prompt content for LLMs (d14).
- LLM evaluation leaks easily (c15, c17, c18).

**Did not hold or is unresolved.**
- Persistence. "Lasted at least a year" is from AI Impacts (b14), a lower bound. Chang Table 9 gives same-people evidence (Y2 0.34 vs 0.39; Y3 0.33 vs 0.36), but veterans are an attrition-selected group, the module was revised across years and forecasters got Brier feedback. No delayed retest without feedback exists. Moore finds the overconfidence cut stable across the year, but feedback may have cemented it.
- Effect size over time. 12% in Y2 to 6 to 7% in Y3, Y4, while the module grew richer (K03). New forecasters in Y3 gained only 3% (d03).
- Mediation. Y2 and Y4 indirect effects are not significant. The summary's "three of four years" is not supported by the Results text (d02). Chang Y4 running text swaps n and mean labels versus Table 4; Table 4 shows trained as better (d01).
- Which component. The design never separated components; the principle-level result rests on 69% self-classified explanations (a03).
- Independent replication. None for the one-hour module (K02). Kelly and Mandel 2024 (different 3 to 4 hour course, 70 analysts, no control) cut overconfidence on intervals (d=1.17) but raised underconfidence on binary items (d=0.37), with no cross-task transfer (d08).
- Expert feedback training failed in cancer-trial forecasting (Brier 0.22 vs 0.21, p=.51), but it was 3 to 4 minutes with 5 practice trials and only 25 test trials (b11). Boundary condition: domain and feedback quality.
- Savage 2021: two short videos widened 80% intervals on 8 of 10 questions (4 after correction), but hit rates stayed below target (b10).
- Moore's gain is mostly lower confidence, not better discrimination (hit rate +0.8 points).

**Moderators.** Cognitive ability predicted accuracy in all four years and was independent of training; the ability-by-training interaction appeared only in Y1 (b07). Sample: volunteers, about 83% male, mean age 41, 67% some graduate study (b01). Teaming and tracking effects are larger than training (Mellers: teaming F=60.68 vs training; a13).

**Interventions that worked.** Probability module (human). Feedback with Brier scores (human, confounded). Frequency formats (cited, unread). Reference-class teaching (cited).

**Interventions that did not.** Didactic bias naming (a06). Anti-overconfidence instructions for LLMs (0.000). Bayesian and propose-evaluate-select prompts for LLMs (worse). Superforecaster-authored odds-ratio prompt (worse in Study 2). Few-shot debiasing in LLMs often pushed outputs to extremes (a32).

## 6. Language models

**Baseline behaviour.** Off-the-shelf models are poor forecasters. Random is 0.250 Brier; the human crowd 0.149; best baseline GPT-4-1106 0.208, most others near or worse than 0.25 (c01). GPT-4 in a Metaculus tournament with a research-based prompt scored 0.20 vs the crowd 0.07 and was not significantly better than the 0.25 baseline (d=0.94 gap, a28). Models hedge (rarely output low probabilities) and are overconfident on likely events (c02, a27). Acquiescence: mean predictions above 50% (a29). Pratt found the opposite pattern in a Yes-poor set: probabilities too low helped the plain prompt (d13).

**What changed scores, by size.**
| Lever | Brier change | Source |
|---|---|---|
| Model generation (GPT-4-1106 vs 0613) | about -0.02 | c03 |
| Retrieval | about -0.02 | c03, d14 |
| Outcome RL (14B) | -0.025 | a30 |
| Giving the human median | -0.03 to -0.07 (not a method) | c06 |
| Fine-tune on own best reasoning | -0.007 | c03 |
| Best human-style prompt | -0.011 to -0.019 (not robust in the mixed model) | a22, c08 |
| Prompt content with retrieval and fine-tune removed | -0.002 (0.206 vs 0.208) | c24 |
| Bayesian and propose-evaluate-select prompts | +0.025 to +0.033 (worse) | a23, c09 |
| Superforecaster-authored odds-ratio prompt (o1 era) | +0.023 (worse) | b19 |
| Anti-overconfidence prompt | 0.000 | d10 |

**Prompts on newer models.** Study 2 included o1 and o1-mini and found no helpful prompt (d12). No 2025 to 2026 reasoning model test with frozen retrieval was found (gap 5, open). Lu 2025 tested o3 with a superforecaster-persona prompt; direct prompt beat narrative prompt; o3 .1352 beats the crowd baseline (.149 and .121 are from other sets) but is far behind experts (c12). Brier is not comparable across question sets.

**Calibration in LLMs (outside forecasting).** Verbalized confidence from RLHF chat models is better calibrated than token probabilities, often 50% lower ECE (Tian 2023, abstract only, b25). Calibration fine-tuning with a Brier term on stated confidence: ECE .37 to .03 (HotpotQA), .26 to .10 (math) (Damani, b23). Standard right-or-wrong RL worsens calibration (b23). Lin 2022 and Kadavath 2022 (abstracts only) show verbalized probabilities and P(True) can be calibrated, partly out of domain (b26, b27).

**Training in weights.** Self-play DPO: Phi-4 14B .221 base, .214 with randomized labels, .200 tuned (c14). A randomized-label control already moves the score, so part of the gain is format or exposure. Halawi's fine-tune data: 73,632 generated reasonings, 13,253 kept, 6,000 used for 2 epochs; filter drops pairs more than 0.15 from crowd and averages target with crowd (c04).

**Worked examples vs instructions.** Qiu 2025: off-the-shelf LLMs plateau after one round of belief updating; fine-tuning on a Bayesian assistant's choices (including early uncertain guesses) beats fine-tuning on oracle answers and generalizes; prompting did not help (c19, d15). This is the only hint that demonstrations beat rules, and it is by fine-tuning on a synthetic task.

**Hazards.** Leakage: date-filtered retrieval leaks, retrieval models may carry future data; single-run pastcasts swing from under 20% to over 80% (c17, c18). Logical consistency across related questions predicts later Brier; patching fixes checks it trained on but not held-out ones (c15). Best ForecastBench LLM scores used crowd freeze values on market questions, so they are not pure model scores (c25).

**Humans plus LLMs.** An LLM advisor raised human accuracy 24 to 28% even when deliberately overconfident (N=991; outlier-driven; the control advisor gave no numbers) (c07).

## 7. What our agent should take

Format: item | schema part | status | evidence ids. [E] established, [S] single-source, [C] contested.

### Add now (established)

1. **Evaluation discipline for any forecasting-type item.** Score against a constant base-rate forecast, the plain prompt and a reversed-question version. Repeat each item several times. Use frozen retrieval. Report weighted Brier and hit rate beside any calibration number. Part: G7 (schema must pay for itself). [E] c15, c17, c18, d13, d06 (K06, K19, K25).
2. **Do not add Bayes-style or propose-evaluate-select prompts, or bias-naming and anti-overconfidence instructions.** Part: Section 4b (confirms existing rows). [E] for bias naming (F07, a06, d10); the Bayes harm itself is single-source with adj p=.036 and .010 (a23, c09), so keep it as a "do not add" row, not as a theory.
3. **Aggregate independent short samples in code for numeric answers (median), with no extremizing and no persona voters.** Part: G4, G5, O (aggregation). [E] for the average of independent forecasts (c05, c06, b12); the caveat that ensembling did not help base GPT-4o (c16) means test it on the target model first, as a cheap check, not as a gate.
4. **Never use the model's verbal confidence alone as a stop signal; log it and compare with hit rate.** Part: G5, S0. [E] (existing 4b row plus Moore: confidence fell 1.4 while hit rate rose 0.8, d06).

Nothing else in this subfield reaches "established" for a scaffold. The human result (K01) is single-source and its LLM transfer is weak.

### Test first

| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| T1 | Fixed reference-class step: 2 to 3 classes with rates, code takes the median base rate, capped adjustment | S2, S3, O2 (Generalise) | [S] | a03, d05, d10, K04, K09 |
| T2 | Calibration shrink in code, fitted per task type on resolved items, with hit-rate and distance-from-50 logging | S7, G5 | [S] | a07, a08, d06, d08, d11, K06, K23 |
| T3 | Spread guard: mean distance from 50% per mode, alert on large rise without Brier gain | G1, G7 | [S] | a23, d11, K10 |
| T4 | Class-record memory: past forecasts and outcomes per class, one-line lesson after the first attempt | Memory | [S] | a04, d02, d07, c13, K05, K26 |
| T5 | Few-shot trace of staged, uncertain updates vs abstract rule | Memory, S5 | [S] | c19, d15, K26 |
| T6 | Capped update round after new evidence | S4/S5, G2 | [C] | a13, d02, K05, K21 |
| T7 | Retrieval step vs reasoning step ablation | S1, S3, memory | [S] | c03, d14, K12 |
| T8 | Reward-design watch (abstention collapse) if a calibration reward is ever added | G6 | [S] | b22, K14 |
| T9 | Ensemble check on the target model | G4, G5 | [S] | c16, K17 |

## 8. Concrete tests on our bench

All arms at equal total tokens (tokens counted including setup). Each item run at least 5 times per arm. Compare on the same items. Report mean difference with a paired bootstrap interval. Controls: plain prompt; constant base-rate forecast; reversed-question consistency.

| Test | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| B1 Reference-class step (T1) | Resolved binary questions with a frozen date-cut corpus (ForecastBench-like; 100+ items, mixed classes) | (a) plain; (b) scaffold with reference-class step; (c) token-matched filler step of same length | Brier, weighted Brier, ECE | Small: -0.01 or less (prompt analogues gave -0.004 to -0.019 and were not robust). Add only if the gain beats filler with a 95% interval below zero |
| B2 Calibration shrink (T2) | Same set plus a second task type (interval or numeric-range items) | plain; plain + shrink fitted on held-out half; plain + shrink fitted on other task type | ECE, Brier, hit rate; per-type bias sign | ECE drops 0.02 to 0.04; hit rate unchanged; check that binary bias does not flip to underconfidence (Kelly and Mandel d=0.37) |
| B3 Spread guard (T3) | Same set | plain; CoT; CoT + shrink toward base rate | Distance from 50%, Brier | CoT-like prompts are far from 50%; shrink should recover 0.005 to 0.02 Brier |
| B4 Class-record memory (T4) | Sequence of questions in 5 classes; chronological order; resolve after each batch | plain; scaffold with record + lesson after first attempt; scaffold with lesson before attempt | Brier by batch, ECE | Gain grows with batches; "before" arm loses to "after" (fixation rule) |
| B5 Worked trace vs rule (T5) | Belief-updating items with staged evidence (3 to 5 rounds) | abstract rule; few-shot trace with early uncertain guesses; both | Round-by-round accuracy and Brier | Trace beats rule by a few points (Qiu hint, fine-tune only) |
| B6 Update round (T6) | Items with evidence arriving in 2 stages | single pass; one capped update; forced two updates | Brier, over-update rate (moves in the wrong direction) | Small; may be null (mediation failed in 2 of 4 years) |
| B7 Retrieval vs reasoning (T7) | Same set with frozen retrieval | plain; reasoning scaffold only; retrieval only; both | Brier | Retrieval about -0.02; scaffold alone about 0 (Halawi) |
| B8 Aggregation (T9) | Same set | one long chain; 3 short samples with median; 5 short samples with median | Brier | Median helps only if single samples are calibrated; check on target model |
| B9 Model-generation check | Same set, two model versions | best arm from B1 to B3 on each model | Brier | Gain shrinks on stronger models (Chang gain shrank across years; Study 2 null on o1) |

## 9. What does not transfer, and why

- **The one-hour lesson itself.** A lesson works through memory and habit in a person over months, with feedback and a leaderboard. A prompt is read once and has no persistence. Our evidence: the same ideas in a prompt gave at most -0.019 and the strict model found no gain (a22).
- **Self-selected volunteers.** Chang's sample is motivated, educated volunteers who made 30+ forecasts a year. An LLM has no such motivation.
- **Targeted practice.** Humans chose where to forecast more. A scaffold does not choose questions unless we build that in.
- **Domain knowledge coaching (K, N, W principles).** Showed no effect in humans (b05); retrieval, not coaching, helps LLMs.
- **Feedback over a year.** The scaffold has no weight update. A class record is the only analogue and is untested.
- **Weight training (RL, fine-tune).** Out of scope for a scaffold. Use as a ceiling: about -0.025 Brier.
- **Hit-rate gains.** Moore's gain was mostly lower confidence. For an LLM, lowering confidence helps only where it is overconfident, and the direction depends on the set's Yes rate (Pratt).
- **Teaming.** Larger than training in humans (Mellers). Debate between agents is not allowed (G9); only code aggregation.
- **Cross-set comparison.** Brier numbers across different question sets cannot be compared (Lu, Karger, Halawi).

## 10. Open questions

1. Does any independent group replicate the one-hour module on human forecasts? (gap 1; Sedlmeier and Gigerenzer 2001, Karimi Motahhar and Gruca 2025 were located but blocked).
2. Does a reference-class step alone, at equal tokens, help a current model? No token-matched test exists (gap 2).
3. Why did Bayesian and propose-evaluate-select prompts hurt? Extremity alone fails to explain it because CoT is also extreme and did not hurt. Nobody tested a shrink step (gap 3).
4. Did the effect persist in the same people without feedback? (gap 4).
5. Do these prompts help 2025 to 2026 reasoning models with frozen retrieval? Study 2 only covers o1 and o1-mini (gap 5).
6. What are the exact numbers in Lichtenstein and Fischhoff 1980 and Stone and Opel 2000? Originals unread (gap 8).
7. How much of the RL or fine-tune gain can be moved into scaffold steps or few-shot memory at equal tokens? (gap 9).
8. Do worked examples beat abstract rules for forecasting? Only fine-tune evidence on a synthetic task (gap 10).
9. Why did the module effect shrink from 12% to 6 to 7%? Cohort mix, content change or less novelty?
10. Is the "post-mortem looks worse" result only selection (cited after errors)?

## 11. Sources

Opened = [V]; snippet or abstract only, or second-hand = [M].

- [V] Chang, Chen, Mellers, Tetlock (2016) Developing expert political judgment: the impact of training and practice on judgmental accuracy in geopolitical forecasting tournaments. Judgment and Decision Making. https://journal.sjdm.org/16/16511/jdm16511.pdf (mirror https://jbaron.org/journal/16/16511/jdm16511.pdf). Ids a01-a06, b01-b09, c20, c21, d01-d05. Note: critique.md says the three reads agreed but the critic could not re-read the PDF; d01 to d05 re-read tables.
- [V] Moore, Swift, Minster, Mellers, Ungar, Tetlock, Yang, Tenney (2017) Confidence calibration in a multiyear geopolitical forecasting competition. Management Science. https://www.stat.berkeley.edu/~aldous/157/Papers/moore_swift.pdf ; https://escholarship.org/content/qt1700r340/qt1700r340.pdf (a07-a11, d06, d07). Publisher page returned 403 (c22).
- [V] Mellers et al. (2014) Psychological strategies for winning a geopolitical forecasting tournament. Psychological Science. https://doi.org/10.1177/0956797614524255 (a12-a15)
- [M] Lichtenstein and Fischhoff (1980) Training for calibration. https://doi.org/10.1016/0030-5073(80)90052-5 (a16, second-hand)
- [M] Stone and Opel (2000) Training to improve calibration and discrimination. https://doi.org/10.1006/obhd.2000.2895 (a17, second-hand)
- [M] Fong, Krantz, Nisbett (1986) https://doi.org/10.1016/0010-0285(86)90004-6 (a18)
- [M] Larrick, Morgan, Nisbett (1990) https://doi.org/10.1111/j.1467-9280.1990.tb00243.x (a19)
- [M] Lehman and Nisbett (1990) https://doi.org/10.1037/0012-1649.26.6.952 (a20)
- [M] Sedlmeier and Gigerenzer (2001) https://doi.org/10.1037/0096-3445.130.3.380 (a21, d18; blocked)
- [V] Schoenegger, Jones, Tetlock, Mellers (2025) Prompt engineering large language models' forecasting capabilities. https://arxiv.org/abs/2506.01578 (a22-a24, b18-b20, c08-c10, d10-d12; re-opened in critique)
- [V] Halawi, Zhang, Yueh-Han, Steinhardt (2024) Approaching human-level forecasting with language models. https://arxiv.org/abs/2402.18563 (a25, c01-c04, c24, d14)
- [V] Karger et al. (2025) ForecastBench. https://arxiv.org/abs/2409.19839 (a26, c11, c25)
- [V] Lu (2025) Evaluating LLMs on real-world forecasting against expert forecasters. https://arxiv.org/abs/2507.04562 (a27, c12)
- [V] Schoenegger and Park (2023) LLM prediction capabilities: evidence from a real-world forecasting tournament. https://arxiv.org/abs/2310.13014 (a28)
- [V] Schoenegger, Tuminauskaite, Park, Bastos, Tetlock (2024) Wisdom of the silicon crowd. https://arxiv.org/abs/2402.19379 (a29, c05, c06)
- [V] Schoenegger, Park, Karger, Trott, Tetlock (2024) AI-augmented predictions: LLM assistants improve human forecasting accuracy. https://arxiv.org/abs/2402.07862 (b24, c07; abstract only for b24)
- [V] Turtel, Franklin, Skotheim, Hewitt, Schoenegger (2025) Outcome-based reinforcement learning to predict the future. https://arxiv.org/abs/2505.17989 (a30, b16, b17, c13, d16; re-opened in critique)
- [V] Turtel, Franklin, Schoenegger (2025) LLMs can teach themselves to better predict the future. https://arxiv.org/abs/2502.05253 (c14)
- [V] Hsieh, Fu, Chen (2024) Reasoning and tools for human-level forecasting. https://arxiv.org/abs/2408.12036 (a31, c16)
- [V] Echterhoff et al. (2024) Cognitive bias in decision-making with LLMs. https://arxiv.org/abs/2403.00811 (a32)
- [V] Savage et al. (2021) A strategy to improve expert technology forecasts. https://pmc.ncbi.nlm.nih.gov/articles/PMC8166153/ (b10)
- [V] Doussau et al. (2023) Impact of feedback training on prediction of cancer clinical trial results. https://pmc.ncbi.nlm.nih.gov/articles/PMC11005298/ (b11, b12)
- [V] Superforecasting reality check (2020). https://pmc.ncbi.nlm.nih.gov/articles/PMC7333631/ (b13)
- [V] AI Impacts, Evidence on good forecasting practices from the Good Judgment Project. https://aiimpacts.org/evidence-on-good-forecasting-practices (b14, secondary)
- [V] Chandak et al. (2025) Scaling open-ended reasoning to predict the future. https://arxiv.org/abs/2512.25070 (b21, b22)
- [V] Damani et al. (2025) Beyond binary rewards: training LMs to reason about their uncertainty. https://arxiv.org/abs/2507.16806 (b23)
- [M] Tian et al. (2023) Just ask for calibration. https://arxiv.org/abs/2305.14975 (b25, abstract)
- [M] Lin, Hilton, Evans (2022) Teaching models to express their uncertainty in words. https://arxiv.org/abs/2205.14334 (b26, abstract)
- [M] Kadavath et al. (2022) Language models (mostly) know what they know. https://arxiv.org/abs/2207.05221 (b27, abstract)
- [M] Zou et al. (2022) Forecasting future world events with neural networks. https://arxiv.org/abs/2206.15474 (b28, abstract)
- [V] Pratt, Blumberg, Carolino, Morris (2024) Can language models use forecasting strategies? https://arxiv.org/abs/2406.04446 (b29 abstract; d13 full text)
- [V] Paleka et al. (2024) Consistency checks for language model forecasters. https://arxiv.org/abs/2412.18544 (c15, abstract and intro)
- [V] Paleka et al. (2025) Pitfalls in evaluating language model forecasters. https://arxiv.org/abs/2506.00723 (c17)
- [V] FutureSearch (2025) Bench to the Future. https://arxiv.org/abs/2506.21558 (c18)
- [V] Qiu et al. (2025) Bayesian teaching enables probabilistic reasoning in LLMs. https://arxiv.org/abs/2503.17523 (c19, d15)
- [V] Kelly and Mandel (2024) The effect of calibration training on the calibration of intelligence analysts' judgments. OSF file store (d08)
- [M] Stone, Luu, Costello, Somerville (2023) Automated calibration feedback. https://doi.org/10.1002/bdm.2334 (d09, abstract only)
- [M] Karimi Motahhar and Gruca (2025) How does training improve individual forecasting performance. https://doi.org/10.1016/j.ijforecast.2024.12.001 (d17, closed access)
