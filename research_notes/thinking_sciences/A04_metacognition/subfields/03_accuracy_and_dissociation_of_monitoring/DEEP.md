# Accuracy and dissociation of monitoring: deep document

*Subfield A04.03. Built from evidence_a-d.jsonl (ids a01-a33, b01-b28, c01-c34, d01-d18), claims.jsonl (A04.03-K01 to K27) and critique.md in this folder. Written 2026-10-26. Numbers marked "re-checked" were re-read against source text in the critique pass. Entries marked [M] in section 11 were seen as abstract or snippet only; do not quote their numbers as verified.*

Links to other subfields run in parallel (not covered here): LLM metacognitive harness; Progress monitoring theory; Verification design; Adaptive stopping and metareasoning; Soar impasse types; Probing and measurement selection; Anomaly handling and fixation.

---

## 1. What it is

Monitoring is the act of judging your own thinking: "Do I know this?", "Is this answer right?", "Will I remember this?". This subfield asks one question. **When does that judgment track reality, and when does it come apart from it?**

Four terms we must keep apart:

- **Calibration** (absolute accuracy). Does "80% sure" come true 80% of the time? Measured by ECE, Brier score, mean confidence minus mean accuracy (bias).
- **Resolution** (relative accuracy, discrimination). Does the judge give higher confidence to right answers than to wrong ones? Measured by gamma, AUROC, within-item correlation.
- **Reliability versus validity.** Reliability is how consistent an answer is. Validity is whether it is correct. Confidence follows the first. Scoring follows the second.
- **Dissociation.** A case where confidence moves and accuracy does not, or the reverse. A model can be well calibrated with zero resolution (say 100% on everything when 93.6% are right). It can have good resolution and bad calibration (two bins, 95% and 65%, that are mostly right and mostly wrong).

Why this matters for our agent. The schema lets the program decide transitions (section 1 of SCHEMA.md). Several places still lean on a "how sure are we" signal: the S0 gate, the S6 impasse trigger, the S7 selector, the S8 verify step, and S9 memory. This document says which signals can bear that weight and which cannot. It also says how to measure them honestly.

Scope of the literature:

1. **Human metamemory and metacognition.** Judgments of learning (JOL), feeling of knowing (FOK), confidence, feeling of rightness (FOR), feeling of error (FOE).
2. **Overconfidence research.** Hard-easy effect, item-sampling debate, Dunning-Kruger.
3. **LLM confidence.** Token probability, verbalised confidence, sample agreement, reasoning-model confidence, confidence inside agent loops.

Main verdict in one paragraph. Confidence is an inference from cues, not a read-out of truth. The cues are fluency, speed, amount of retrieved information and self-consistency. They are valid on typical items and fail when ease and correctness come apart. A single stated number from an LLM is mostly a weak signal (AUROC 0.5 to 0.65 for plain prompts on older and agent settings). Signals that come from more computation do better: agreement of several samples, confidence stated after real reasoning, and a blind second attempt. All of them still fail on the same set of items: the ones the model gets wrong consistently. For those, only an outside check helps.

---

## 2. History and theories in depth

### 2.1 Cue-utilisation: confidence is inferred (Koriat)

Koriat (1997, a01 [M]) set the frame. A judgment of learning is not a direct look at a memory trace. It is an inference from cues. He named three families:

- **Intrinsic cues:** properties of the item (how hard it is).
- **Extrinsic cues:** learning conditions (repetitions, study time).
- **Mnemonic cues:** internal feedback such as how easily the item came to mind.

Findings in the original four experiments: item difficulty moved JOL about as much as it moved recall. Repetition and study time moved JOL less than recall. So extrinsic cues were under-weighted. With practice, JOL shifted from intrinsic cues to mnemonic heuristics. Practice increased underconfidence (calibration got worse) while resolution improved. Calibration and resolution moved in opposite directions.

The "easily learned, easily remembered" heuristic (Koriat et al. 2009, a02, opened). Items that need more trials to learn are recalled less. JOLs follow the same rule. N=40 children (2nd and 4th grade), Exp 1: gamma(trials to acquisition, recall) was -.74 (4th grade) and -.64 (2nd grade). Gamma(trials, JOL) was about -.60 and -.56. Gamma(JOL, recall) was .56 and .68. Exp 2, N=60, hard pairs only (restricted range): gamma(trials, JOL) was -.22 for 4th graders (significant) and -.04 for 2nd graders (not significant). Lesson: a cue is only useful when it is valid and the items spread along it. With a narrow range, the cue stops working silently. The children's own explicit estimates of trials needed correlated only about .43 with the true values, so cue use is mostly implicit.

Accessibility model of FOK (Koriat 1993, a03 [M]). FOK comes from the amount of partial information that comes to mind during a retrieval attempt, whether that information is correct or not. FOK is accurate because accessible partial information is mostly correct, not because a monitor reads the trace. Koriat (2012) reports that the count of partial clues predicted recognition about as well as the person's own FOK.

Fluency illusion (Benjamin, Bjork and Schwartz 1998, a15 [M]). Predictions of future recall follow how easily an item was retrieved earlier, even in conditions built so that early ease is negatively related to later recall. Three experiments, strong mismatch of predicted and actual.

Foresight bias (Koriat and Bjork 2005, a16 [M]). JOLs are made with the answer in view. They reflect the cue-target association as seen. Later recall depends on the cue-alone association. This produces unwarranted confidence at study. It is the human basis for the rule that a checker should not see the proposed answer.

### 2.2 Self-consistency model of confidence (Koriat 2012)

The main formal model (a04, opened). In a two-alternative question the person draws a sample of representations and bases confidence on how consistently the chosen answer is supported across them. Confidence tracks consistency (reliability). Calibration studies score it against correctness (validity). The confidence-accuracy link is a by-product of the consistency-correctness link. Response speed is a cheap cue for consistency. Accessibility (amount of information) adds an independent contribution.

Predictions confirmed across word matching, general knowledge and perceptual line comparison: confidence rises with consensus among people and with consistency within a person for the majority choice, and falls for the minority choice.

Three consequences, each with data (a05 to a07, opened):

1. **Sign flip.** For consensually correct items, confidence is higher for correct answers. For consensually wrong items, confidence is higher for the wrong answer. The confidence-accuracy relation flips sign. (Note: the text quotes within-person gamma .47 for consensually correct and .24 for consensually wrong general-knowledge items while also saying the aggregate correlation turns negative for wrong items. This was not reconciled; likely within-person versus across-item statistics.)
2. **Overconfidence depends on the reference.** 36 matched items per task, first presentation, 7 confidence categories (50 to 100). Scored against accuracy: overconfidence 12.4 points (general knowledge) and 15.9 (perceptual). Scored against item consensus: underconfidence 3.38 and 5.21. Against response consensus: overconfidence 6.78 and 4.59. Against repetition of the person's own answer: underconfidence 12.80 and 7.05. The sign of the bias changes with the reference. Part of "overconfidence" is a reliability-validity gap.
3. **U-shaped confidence-accuracy function** across items spanning 0 to 100% correct, because consensus grows as accuracy moves away from 50%.

### 2.3 Dynamic and Bayesian models

- **Two-stage dynamic signal detection** (Pleskac and Busemeyer 2010, a31 [M]). Evidence keeps accumulating after the choice. Confidence is read from the accumulated evidence by rating criteria. One process explains choice, response time and confidence. It predicts that resolution improves with more post-decision time.
- **Bayesian second-order inference** (Fleming and Daw 2017, a32 [M]). Confidence is an inference about a coupled but separate decision system, like judging another actor. This accounts for cases where metacognition is better or worse than task performance.
- **Measures** (Fleming and Lau 2014, b27 [M]; Rahnev 2024, b28 [M]): separate bias, sensitivity (AUROC, meta-d') and efficiency (meta-d' over d', the M-ratio). Seventeen measures compared; all valid with different precision. One 2026 LLM preprint (b23, abstract only) warns that meta-d' does not transfer cleanly to open-ended QA.

### 2.4 Delayed-JOL effect

- Nelson and Dunlosky (1991, a12 [M]): a JOL made on the stimulus alone, some time after study, predicts recall far better than a JOL made right after study. Before this, JOLs had almost never been very accurate.
- Dunlosky and Nelson (1992, d17, abstract record opened): the effect depends on the cue. With a stimulus-only cue all 45 subjects showed it. With a stimulus-plus-response cue there was little or none. The authors state the mechanism is unknown.
- Dunlosky and Nelson (1994, a13, opened): immediate JOLs are insensitive to how study activity changes memory. Delayed JOLs rate interactive imagery above rote rehearsal and distributed above massed repetition, as recall does. Gamma(JOL, recall): immediate roughly +.10 to +.29, delayed roughly +.71 to +.93 (OCR-garbled table, approximate). Over half of delayed JOLs sat at the scale ends.
- Rhodes and Tauber (2011, a14, b25, d15; abstract record opened): meta-analysis 1, 4,554 participants, 112 effect sizes, delayed versus immediate on gamma, g = 0.93. Meta-analysis 2, 3,807 participants, 98 effect sizes, memory benefit g = 0.08. So the gain is in monitoring, not in retrieval practice. Full text and moderator tables not read.

Why it works (leading account). The delayed judgment invites a fresh retrieval attempt from the cue alone. That attempt draws on long-term memory information that predicts later recall. The immediate judgment is dominated by transient fluency in working memory that will be gone by test time. The cue-alone result supports this.

### 2.5 Overconfidence and the hard-easy effect: competing accounts

- **Probabilistic mental models** (Gigerenzer, Hoffrage and Kleinbolting 1991, a08 [M]). Confidence is the validity of the best available cue in the person's environment. Overconfidence appears because researchers pick tricky items. A secondary summary reports selected sets were hard (53% and 56% correct) and representative sets easier (72% and 75%), with overconfidence vanishing on the latter. Unverified.
- **Naive empiricism critique** (Juslin, Winman and Olsson 2000, a09 [M]). Review of 2AFC general-knowledge studies. Most of the hard-easy effect comes from scale-end effects, linear dependency and regression to the mean. Secondary snippet: 95 selected-sample data points had mean confidence .73 against .64 correct; 35 representative-sample points had .73 against .72. Unverified numbers.
- **Counter-evidence.** Braun and Yaniv 1992, Griffin and Tversky 1992, Soll 1996 and Brenner et al. 1996 found overconfidence with representative sets (as listed in a07 and a08; those papers were not opened). Hoffrage (2011, a33 [M], snippet only) reports that a test of the PMM sampling prediction failed in a first experiment.
- **Three kinds of overconfidence** (Moore and Healy 2008, a10 [M]): overestimation, overplacement, overprecision. Hard tasks produce overestimation with underplacement. Easy tasks the reverse. Overprecision is the most persistent.
- **Bayesian account** (Healy and Moore 2007, b21, opened). One Bayesian model with a prior over task difficulty produces the hard-easy pattern with no special bias. 82 undergraduates, 10-item trivia quizzes (easy, medium, difficult), incentive-compatible belief reports. Interim overplacement 0.39 points after easy quizzes; underplacement 1.66 points after difficult quizzes. The critique flags that the quoted z = 22.83 looks like a score-difference test, not a bias statistic.
- **Merkle 2009** (b24 [M]): almost any judge shows a hard-easy effect under realistic conditions, so it cannot tell models apart.
- **Koriat 2012**: hard-easy comes from the reliability-validity gap (section 2.2).

Status: all four accounts explain overconfidence on hard sets. They disagree on cause. No source tested them head to head, and none on LLMs.

### 2.6 Dunning-Kruger

- Kruger and Dunning (1999, a11, d16; abstract record opened): four studies (humour, grammar, logic). Bottom quartile scored at the 12th percentile and estimated the 62nd. Training raised their ability to see their limits.
- Gignac and Zajenkowski (2020, b19, opened): N=929 community adults, Raven's matrices versus self-rated IQ. Self-rated 123.76 versus measured 101.70 (d = 1.71); r = 0.28. Quartile gaps 32.63, 22.05, 20.15, 12.68 (ANOVA F(3,925) = 79.00, eta-squared 0.20). Yet no significant heteroscedasticity and an essentially linear relation. The pattern is the better-than-average effect plus regression to the mean.
- Dunkel, Nedelec and van der Linden (2023, b20, opened): N = 13,977 (AddHealth, ages 18 to 28). Self-assessed IQ below measured (d = -0.14); r = 0.24; absolute residuals versus IQ r = -0.07; quadratic delta R2 = 0.011; cubic delta R2 = 0.001. A significant but minimal Dunning-Kruger effect.

Net: the quartile plot is largely statistical. A mean gap remains (d = 1.71 in one sample), so "mostly artefact" does not mean "no bias".

### 2.7 Feeling of rightness and feeling of error (Thompson)

Metacognitive dual-process account (Thompson, Prowse Turner and Pennycook 2011, a17 [M]). The fast intuitive answer carries a feeling of rightness on a continuum. A weak FOR triggers deliberate analysis. A strong FOR lets the intuitive answer stand. FOR is driven by the fluency of the answer and by conflict between competing responses.

- Thompson et al. 2013 (a18, landing page opened): answer fluency (speed of first answer) predicts FOR in conditional inference and base-rate problems. FOR predicts thinking time and answer changes. Perceptual fluency (ease of reading) did not change FOR, retrospective confidence or accuracy across five experiments. People spent longer on hard-to-read items but did not change answers. In the last two experiments, perceptual disfluency raised Cognitive Reflection Test accuracy only for participants of high cognitive ability.
- Gangemi, Bourgeois-Gironde and Mancini 2015 (a19, b22, opened): feeling of error on the bat-and-ball problem. Study 1: N = 145 undergraduates; 30% solved the standard problem, 97% the control. Uneasiness higher for standard than control, F(1,101) = 658.46, partial eta-squared .87. Wrong answerers 16.52 versus correct 8.79 (t(143) = 8.8). Study 2: N about 148, 34% correct; wrong 14.18 versus correct 11.37. Questionnaire after solving, so possibly retrospective.
- Wang and Thompson 2019 and a thesis (b26 [M], snippet only): response-execution speed manipulation did not affect FOR.

### 2.8 Where the history leaves us

1. Confidence is inferred from cues, so its quality is the validity of those cues.
2. Better monitoring comes from more or better evidence: a fresh retrieval attempt, a second look after time, sampled consistency.
3. Overconfidence is real but partly definitional and partly statistical. Measure it on your own distribution.
4. Cheap signals (fluency, speed, conflict) decide whether people look again. They are fast and often valid, and they fail on confidently wrong items.

---

## 3. Core findings with exact numbers

Status key: **E** established (two or more independent sources), **S** single source, **C** contested. "Opened" means read in this research run. Evidence ids refer to the jsonl files.

### 3.1 Human monitoring

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Delayed JOL gives much better resolution than immediate JOL | g = 0.93 on gamma (4,554 people, 112 effect sizes). Memory effect g = 0.08 (3,807 people, 98 effect sizes) | Rhodes and Tauber 2011 (a14, b25, d15; abstract only) | E (two human sources: a13, d15) |
| Delayed JOL needs a cue-alone judgment | Stimulus-only cue: all 45 subjects show effect. Stimulus plus answer: little or none | Dunlosky and Nelson 1992 (d17; abstract) | S |
| Immediate JOL gamma versus delayed | Immediate about +.10 to +.29; delayed about +.71 to +.93 (OCR-garbled, approximate) | Dunlosky and Nelson 1994 (a13) | S |
| Easily-learned-easily-remembered cue works but needs range | Exp 2 hard pairs only: gamma(trials, JOL) -.22 (4th grade, significant) vs -.04 (2nd grade, ns); explicit estimate of own trials correlated .43 with true | Koriat et al. 2009 (a02) | S |
| Fluency can mislead memory predictions | 3 experiments, strong mismatch (no figures extracted) | Benjamin, Bjork and Schwartz 1998 (a15; abstract) | S |
| Confidence follows consistency, not correctness | Overconfidence vs accuracy: +12.4 / +15.9 points; vs item consensus: -3.38 / -5.21; vs own repeated answer: -12.80 / -7.05 | Koriat 2012 (a04, a06) | S (one lab) |
| Confidence-accuracy sign flips for consensually wrong items | gamma .47 (consensually correct) vs .24 (wrong) quoted; aggregate negative; unreconciled | Koriat 2012 (a05) | S |
| Hard-easy effect is partly selection and regression to the mean | Selected sets .73 confidence vs .64 correct; representative .73 vs .72 (secondary snippet) | Juslin et al. 2000 (a09; snippet) | C |
| Hard-easy effect appears with representative sets | Named studies, no numbers | Braun and Yaniv 1992, Griffin and Tversky 1992, Soll 1996 (cited in a07) | C |
| Bayesian model produces hard-easy pattern | 82 students; overplacement 0.39 (easy), underplacement 1.66 (difficult) | Healy and Moore 2007 (b21) | S |
| Dunning-Kruger quartile pattern is largely artefact | N=929: d = 1.71 mean gap but linear; N=13,977: quadratic delta R2 = .011 | Gignac 2020; Dunkel 2023 (b19, b20) | E |
| Bottom quartile estimated 62nd percentile at 12th | 4 studies | Kruger and Dunning 1999 (a11, d16; abstract) | S (superseded in interpretation) |
| Answer fluency drives FOR; FOR predicts re-thinking | 5 experiments (counts only) | Thompson et al. 2013 (a18) | S |
| Perceptual fluency does not drive FOR | 5 experiments, no effect on FOR, confidence or accuracy | Thompson et al. 2013 (a18) | S |
| Feeling of error exists | Wrong 16.52 vs correct 8.79 (N=145); 30% solved standard, 97% control | Gangemi et al. 2015 (a19, b22) | S |
| Human readers of LLM text are poor judges | AUC .589 / .602 / .592 (default explanations) vs model .751 / .746 / .781 | Steyvers et al. 2025 (a28, b17, c20) | S |
| Longer explanations raise human confidence, not accuracy | Long vs short BF = 25; human AUC .54 (long), .57 (uncertainty only) | Steyvers et al. 2025 (b18) | S |

### 3.2 LLM confidence: elicitation and what it tracks

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Base models are calibrated on lettered multiple choice, if the format is right | Models 800M to 52B; improves with size and few-shot; zero-shot worse | Kadavath et al. 2022 (a20, b01, c01) | E (one paper; confirmed by later work on RLHF models only partly) |
| "None of the above" breaks calibration | 52B on MMLU, accuracy and calibration fall significantly; 5-shot and 20-shot do not fix it | Kadavath 2022 (b02, c02) | S |
| RLHF policies look miscalibrated but one temperature (T=2.5) mostly fixes it | MMLU, true/false MMLU, TruthfulQA | Kadavath 2022 (b03, c03) | S |
| P(True) on own samples is useful but biased toward own samples; seeing 5 own samples first helps | 52B, five tasks | Kadavath 2022 (b04, c04) | S |
| Verbalised confidence of GPT-4 barely discriminates | Average AUROC 62.7% (chance 50%); about 22.2% AUROC gain GPT-3 to GPT-4; ECE above 0.377 for GPT-3, GPT-3.5, Vicuna (re-checked) | Xiong et al. 2024 (a22, b06, c09) | E (supported by d01, d09) |
| Low ECE can come from constant confidence | GSM8K GPT-4 CoT: 93.6% accuracy, ECE 0.064, all answers 100% (re-checked) | Xiong 2024 (b07, c10) | E (supported by Tian b11/c06, Yoon b16) |
| Agreement of samples predicts failure far better than one stated number | GPT-3.5 GSM8K AUROC 54.8% to 92.7% (5 samples with consistency); five-dataset average 56.4% to 73.0%; best ECE 0.028 (re-checked) | Xiong 2024 (a22, b09, c11, c12) | E |
| Semantic entropy beats distinct-answer count | CoQA AUROC .77 vs .66 (1.27 vs 1.77 distinct meanings); TriviaQA .83 vs .79 (1.89 vs 3.89) (re-checked) | Kuhn et al. 2023 (a24, b13) | S for the method; E for "agreement beats stated" |
| On RLHF chat models, verbalised beats token probability on ECE | gpt-3.5 TriviaQA 0.140 vs 0.068 (top-1) vs 0.050 (top-2); SciQ 0.256 vs 0.234 / 0.132 / 0.065; TruthfulQA 0.451 vs 0.389 / 0.361 / 0.203 (re-checked) | Tian et al. 2023 (a23, b10 to b12, c06, c07) | E (conflicts with Xiong on discrimination; see 5.4) |
| Top-k answers with probabilities improve ECE; chain of thought does not | gpt-3.5 TriviaQA 2-stage CoT 0.110 vs 1-stage top-2 0.050 | Tian 2023 (b11, c07) | S for ECE; Xiong b08 also finds CoT leaves AUROC near chance |
| Verbalised discrimination near chance on adversarial items | TruthfulQA AUC 0.455 to 0.551 (gpt-3.5); label-prob AUC 0.418 or 0.462; GPT-4 verbalised about 0.62 | Tian 2023 (b11, b12, c06) | S |
| Words mapped to numbers on held-out data calibrate well | gpt-3.5 SciQ ECE 0.064 (optimised mapping) vs 0.166 (human survey mapping); Llama2-70B TruthfulQA 0.047 vs 0.376 | Tian 2023 (c08) | S |
| Confidence words in answers do not track accuracy | Strengtheners: 53% correct. Weakeners: 32%. 17% of wrong answers carried strengtheners. 47% error among confident answers. 9 models, 125,244 queries, 284 MMLU questions (re-checked) | Zhou et al. 2024 (c26) | S for numbers; E for direction (with a26) |
| Certainty markers in the prompt change accuracy | High-certainty markers cut accuracy about 7% relative; 50 markers; more than 80% spread across templates | Zhou et al. 2023 (a27) | S |
| Hedged answers are not faithful to intrinsic uncertainty | Vanilla conditional faithful generation near 0.5 (value of ignoring confidence) | Yona et al. 2024 (a26) | S |
| Persistence under "reconsider" tracks accuracy but reconsidering often hurts | Mistral accuracy 36% and 32% when it changed answer; GPT-4o 0.60 vs 0.80 below vs at/above 95 confidence (p = 0.0083); formal fallacies: 100 given to every answer | Pawitan and Holmes 2024 (a29) | S |
| Finetuning on about 1,000 graded examples beats prompting | Gains slow after about 5,000; needs weights | Kapoor et al. 2024 (a25, b14, c23) | E (with Lin 2022 a21, Steyvers 2025 c22, ConfTuner c28); outside our no-training rule |
| A second model predicts a model's correctness about as well as the model itself | Mistral on LLaMA-2 7B had higher AUROC than LLaMA-2 on itself | Kapoor 2024 (c24); Kadavath b05 | E |
| Fine-tuned verbal confidence on self-consistency targets | GPT-4.1-mini MMLU-Pro AUC .52 to .68, ECE .61 to .05; GSM8K AUC .53 to .76; out of domain TruthfulQA ECE worsened .10 to .18 | Steyvers, Belem and Smyth 2025 (c22) | S |

### 3.3 LLM confidence: reasoning, agents and decision use

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Reasoning models state better-calibrated confidence than non-reasoning pairs | 33 of 36 settings. TriviaQA ECE Qwen3-32B 0.207 to 0.063 (AUROC 0.650 to 0.807); Qwen2.5 0.129 to R1-Distill 0.042; GLM-4 0.084 to GLM-Z1 0.029; EXAONE 0.130 to 0.104. Qwen3 thinking row equals QwQ row cell for cell (possible copy error) | Yoon et al. 2025 (b15, c13, d02) | C (see Zeng, Hiremath) |
| Cause: slow, exploratory reasoning | TriviaQA ECE original 0.042; non-linear reasoning removed 0.161; no CoT 0.150. NonambigQA .195 / .341 / .359. In-context slow thinking GLM-4-32B ECE .150 to .029, AUROC .631 to .796 (re-checked) | Yoon 2025 (b16, c14) | S |
| Reasoning fine-tuning can worsen factual calibration | R1-Distill-32B on AIME: accuracy 9.67% to 65.7%, ECE 0.752 to 0.240, AUROC 0.695 to 0.813. On SimpleQA and FreshQA small reasoning models less calibrated | Zeng et al. 2025 (d03) | C |
| Accuracy and ECE can move apart | Llama-3.1-8B ECE 0.104 / 0.050 / 0.015 by budget; accuracy 0.732 vs 0.653; 47 questions | Hiremath and Hiremath 2026 (c15) | weak, single preprint |
| Confidence stated after reasoning discriminates only after real reasoning | R1-32B verbal AUROC 0.56 (no reasoning) to 0.80 (100-500 tokens) to 0.88 (long forced); 270 items. Matches 10-sample semantic entropy at about 200 tokens (fact retrieval) and about 3,500 tokens (maths); SE used 218 tokens per sample. Reader model on trace alone: AUROC 0.841 vs 0.851 | Podolak and Verma 2025 (d01) | S for size; E for direction (with d02) |
| Models are overconfident in debate | Initial mean 72.9% (rational 50%), final about 83%; both sides at 75% or more in 61.7% of 60 debates; self-debate 64.1% to 75.2%; told chance is 50%: 50.0% to 57.1% | Prasad and Nguyen 2025 (c16) | S |
| Hard-easy effect appears in 11 LLMs | Mean confidence 88% vs accuracy 79%. Slope: reasoning 0.168, chat 0.732 (range 0.192 to 0.996). ECE 0.037 vs 0.150. Correlation of confidence with actual probability 0.94 vs 0.48. LifeEval hardest bin confidence 34.2% vs 9.6%; easiest 80.5% vs 92.0% | Michael et al. 2026 (c17, c18, d04) | C (cause untested) |
| Weak models sit at ceiling confidence | Kimi K2 accuracy 23.3%, confidence 95.7%, ECE 0.726. Gemini 2.5 Pro accuracy 80.9%, confidence 99.5%, ECE 0.185. 24,000 trials | Ghosh and Panday 2026 (c19) | S |
| Agent runs: stated success far above real, weak discrimination | SWE-bench Pro N=100: true success 35%, 22%, 27%; predicted about 70%, 99%, 64%. AUROC pre/post/adversarial 0.62/0.58/0.55, 0.53/0.51/0.57, 0.64/0.55/0.64. Differences not significant | Kaddour et al. 2026 (d07) | S |
| Whole-run verbalised confidence in agents | SimpleQA AUROC 0.655, GPQA 0.593, HLE 0.614; ECE 0.121, 0.454, 0.656. Trained trajectory calibrator: AUROC .752, .706, .644; ECE .068, .102, .031 | Zhang, Xiong and Wu 2026 (d05) | S |
| Overconfidence grows over steps; action follows stated probability | 499 SWE-Bench Verified tasks, 10 models, 70 tool calls; only 4 of 10 models had later AUROC above step 1; decision classification near 1 given stated probability | Barkan, Black and Sourbut 2025 (d08) | S |
| Behavioural consistency beats verbalised in agents | AUROC (k=5) Claude Sonnet 4.5 0.651 vs 0.522; GPT-5 0.734 vs 0.547; Llama 70B 0.739 vs 0.481; range 0.62 to 0.78 at k=10; majority vote gain +0.1 to +2.0 points | Agents disagree with themselves 2026 (d09) | S |
| Consistent and wrong tasks are a stable share | Agents 5.5% to 10%. GPQA gpt-4.1 mean consistency 0.89, majority accuracy 0.48; 48% wrong at consistency 0.8 or more; 28% confidently wrong for all runners; Spearman consistency vs correctness 0.20 to 0.59; cross-family same wrong answer Haiku 10 of 15 (p=.003) | d09, d10 | E |
| Confidence-weighted voting saves samples | Cost cut at budget 5/10: P(True) 41%/46%, response prob 22%/31%, verbal 0-100 22%/30%; accuracy gain 1.6 points at budget 5. Search agent: BrowseComp 54.5 with 3.87 attempts vs 47.5 for 10-sample self-consistency; Pass@10 68.6 to 70.3 | Taubenfeld et al. 2025 (c32); BrowseConf (c33) | E |
| Models do not use their own confidence to decide | HLE high penalty: GPT-5-nano utility -0.688 to -0.004 when the optimal rule is applied in code; gains up to +0.685; GSM8K gains near 0 | Decision-faithfulness 2026 (c34) | S |
| Self-correction without feedback hurts | GPT-3.5 CommonSenseQA 75.8 to 38.1; GSM8K GPT-4 95.5 to 91.5 to 89.0; with oracle labels GPT-3.5 GSM8K 75.9 to 84.3 | Huang et al. 2024 (c27) | E (with a29, F07, F11, F12 in SCHEMA) |
| Local token confidence as in-trace signal | DeepConf: low variant cuts tokens 43.8% to 84.7%; top-10% filtering lowers accuracy in 8 of 20 offline settings by 0.31 to 4.69 points | Fu et al. 2025 (d06) | S |
| Early-window agreement as stop signal | Savings: GSM8K 80.1%, CSQA 78.5%, StrategyQA 76.8%, Coin Flip 84.2%, Last Letters 67.4%, MATH 33.8%; GPT-4 accuracy change 0.00 | Li et al. 2024 (d12) | S |
| Per-slice recalibration beats global | MMLU PaLM2-L ECE 0.063 / 0.063 / 0.053 (base / global / few-shot); XNLI 0.059 / 0.057 / 0.045; LLaMA-65B 0.109 / 0.099 / 0.074 | Li et al. 2024 (d11) | S |
| Protocol changes the answer | Token-score context flips winner in 4 of 12 settings (ECE) and 9 of 12 (AUROC); alias vs canonical answer shifts verbalised confidence by 0.072; metacognitive efficiency vs accuracy -0.80 (TriviaQA) and 0.00 (NQ) | Kim and Kang 2026 (c30); b23 | E |
| LLM judgments of learning do not track recognition | Slope B: human .167 [.018, .316]; GPT-3.5 .013; GPT-4-turbo .026; GPT-4o .045 (all CIs include 0) | Huff lab preprint 2025 (c31) | S |

---

## 4. Mechanisms and models

Each model below is stated so it can be coded.

### 4.1 Cue-based confidence (Koriat)

Confidence = f(cues). Treat the model's stated confidence as the output of a function over cues, not as a read of truth.

Implementation view for the agent:

- Name the cue each confidence number rests on. Candidates: answer fluency (speed, token probability), amount retrieved (number of distinct facts used), agreement across samples, presence of a passing check.
- Compute the cues in code where possible. The only cue that costs the model nothing to fake is the stated number. Treat that as the weakest.
- A cue is valid only where it varies across items and correlates with correctness in this task class. Log, per cue and per task class, the correlation with correctness. If cue values have no spread (restriction of range, as with the 2nd graders in a02), do not use it.

### 4.2 Self-consistency model (Koriat 2012)

Procedure for a two-choice question. Draw n samples of support. Count how many support the chosen answer. Confidence rises with that fraction. Response speed is a cheap proxy.

Direct LLM mapping:

1. Draw k short independent attempts, each in a fresh context (SCHEMA S3).
2. Cluster by final answer (exact match for closed answers; entailment cluster for open text; Kuhn et al. a24).
3. Compute: fraction in the largest cluster (agreement), number of clusters, entropy over clusters (semantic entropy).
4. Use as the reliability signal. Do not treat it as validity.

Predicted failure, now measured in LLMs: consistent-and-wrong items. Consistency equals 1 and accuracy equals 0. Size: 5.5% to 10% of agent tasks; 8% to 28% of GPQA items by model tier (d09, d10).

### 4.3 Calibration and resolution as separate quantities

Compute both from logged (confidence, correct) pairs. Minimal set, fixed up front (b28 advises choosing one of each and keeping them):

- **Resolution:** AUROC of confidence for predicting correct. Report with ties handled (Yoon b15 notes AUROC is inflated by ties when a model uses few distinct values).
- **Calibration:** ECE with fixed bins (say 10), plus mean confidence minus accuracy (bias).
- **Constant-signal check:** number of distinct confidence values. If one value covers more than 80% of the items, the ECE is not informative (b07).
- **Selective accuracy:** accuracy on the top x% of items by confidence versus coverage.

Rule from the evidence: reject a signal whose AUROC is below about 0.65 on our tasks (K07 test). Ceiling check: with the signal at AUROC 0.5 the ECE can still be tiny.

### 4.4 Recalibration map (post-hoc, no training)

Raw signal in, observed accuracy out. Build a lookup of observed accuracy per bin, per task type.

- Evidence that this works: Platt scaling alone brought one model's ECE to 0.01 without improving AUROC (d07); temperature T=2.5 fixed an RLHF policy (b03); words mapped via held-out data gave ECE 0.047 to 0.064 (c08); per-slice beats global (d11).
- What it cannot do: improve AUROC. It fixes the level, not the ranking.
- Unknown: how many labelled items per bin are needed. Trained recalibrators used 5 to 20 items per slice (d11) or several hundred trajectories per domain (d05). A count table with no training is untested.

### 4.5 Delayed judgment as blind re-solve

Human effect: delayed cue-alone JOL has g = 0.93 on resolution. The effect needs a stimulus-only cue (d17).

LLM analogue (untested, K24):

1. Solve problem P, get answer A1 and a first-pass signal.
2. In a new context, show only P (not A1). Solve again, get A2.
3. Compare A1 and A2 in code. Agreement raises trust. Disagreement is the conflict signal that triggers verification.
4. Do not ask "is A1 right?" with A1 visible. That is the stimulus-plus-answer cue, the weak form. It is also the foresight bias of a16.

Nearest LLM evidence, and why it is not enough: Kaddour (d07) found post-run review no better than pre-run guessing (differences not significant at N=100), and the adversarial review cost about twice as much. That is a review with the answer visible, not a blind re-solve.

### 4.6 Feeling of rightness as a gate

Human model: a fast first-pass signal decides whether to think more. Strong FOR leaves the answer alone. Weak FOR triggers analysis.

Agent version (K06, K23):

- First-pass signal options, all computed in code: (a) disagreement between two cheap early samples (Li et al. d12 stops on unanimity of a window of 5 to 8); (b) local token-confidence dip (DeepConf d06, needs top-k logprobs and a 16-trace warm-up); (c) stated confidence after reasoning (d01).
- Gate rule: if the signal says weak, run verification (SCHEMA S4/S8 check). If strong, keep the answer.
- Known failure: all three are fluency or agreement cues. They miss confident-wrong items. The gate must be paired with an outside check for the items it lets through only if cost allows.
- No test yet of any of them as a re-examination gate in a multi-step agent.

### 4.7 Confidence-weighted voting and early stopping

- CISC (Taubenfeld c32): weight each sample's vote by its confidence. Best confidence for this is P(True), not the best-calibrated one; within-question discrimination matters, not ECE (P(True) 62.3%, verbal 0-100 56.1%, verbal binary 52.2%). Needs token probabilities.
- BrowseConf (c33): after each attempt, if stated confidence is below a threshold, retry. Threshold tuned on 500 samples from a different dataset. Reached 54.5 with 3.87 attempts versus 47.5 for 10-sample self-consistency. Pass@10 was still 68.6 to 70.3, so the gate leaves most of the available gain unused.
- ESC (d12): sample in windows of 5 (8 for MATH); stop when the window is unanimous.

### 4.8 Calibrating the elicitation prompt

What changed ECE in the evidence, ordered by size:

1. Moving from token probability to verbalised on RLHF models: relative ECE cut about 50% (b10).
2. Asking for top-k alternatives with probabilities: gpt-3.5 SciQ 0.234 to 0.065 (top-1 to top-4) (b11).
3. Thinking before stating: Qwen3 0.207 to 0.063 (d02); R1-32B AUROC 0.56 to 0.80 after 100 to 500 tokens (d01).
4. Mapping words through held-out data: 0.166 to 0.064 (c08).
5. Platt or temperature rescaling: ECE to about 0.01 (d07), no AUROC gain.

What did not help: chain of thought in the prompt for calibration (b11, b08), telling the model to be careful, telling it to use its confidence (c34 found no change), human-inspired prompts for AUROC (b08).

### 4.9 Self-preference in self-scoring

GPT scored its own patches 23 points higher than other models' (N=25, p = 0.001; d07). Models find their own samples more plausible (b04). A judge should be a fresh instance with no authorship information (SCHEMA G5).

---

## 5. What holds up

### 5.1 Replicated and robust

1. **Single verbalised confidence has weak discrimination.** Xiong (AUROC 62.7% for GPT-4), Pawitan (100 for every answer), Zhou (17% of wrong answers carry strengtheners), Kaddour (AUROC 0.51 to 0.64 in coding agents), Zhang (0.59 to 0.66 whole-run), Podolak (0.56 with no reasoning). Many labs, many settings. Direction is robust. Size varies with task, model and metric.
2. **Agreement among samples beats a single stated number.** Xiong (54.8% to 92.7% on GSM8K), Kuhn (.77 vs .66), d09 (0.65 to 0.74 vs 0.48 to 0.55 in agents). Gain is large on arithmetic, small on professional knowledge (b09). Limit: in a GPQA audit the consistency-correctness link was weak (Spearman 0.20 to 0.59, d10).
3. **A stable share of items are consistently wrong.** Two independent sources (d09, d10). More samples and a second model family do not remove it.
4. **Low ECE does not mean usable.** Xiong (constant 100%), Yoon (ECE worse, AUROC better when hedges removed), Tian (low ECE, AUC near chance on TruthfulQA), Kapoor (sampling: good ECE, weak AUROC; verbal: decent AUROC, poor ECE), d07 (Platt fixes ECE, not AUROC).
5. **Self-correction without feedback does not help.** Huang (75.8 to 38.1), Pawitan (switching answers: accuracy 36% and 32%), ConfTuner (poor confidence means revision edits right answers).
6. **Calibration depends on the slice.** d11 (per-slice better), d05 (transfer partial), c22 (out-of-domain ECE worse), b05 (P(IK) only partly transfers).
7. **Dunning-Kruger quartile pattern is mostly artefact in humans.** Two replications (b19, b20).

### 5.2 Moderators found

- **Format.** Lettered multiple choice calibrates; "none of the above" breaks it (b02). Free-form needs sampling or training.
- **Model type.** RLHF chat models: verbalised beats token probabilities for ECE (b10). Base models: token probabilities fine (b01).
- **Reasoning.** Calibration improves with real reasoning before stating (d01, d02, b15), on reasoning tasks more than on factual recall (d03).
- **Task type.** Strong gain from agreement on arithmetic; small on law and professional knowledge (b09). Gains of decision-by-confidence large on hard sets (HLE), none on easy (GSM8K) (c34).
- **Model strength.** Reasoning models have a hard-easy slope of 0.168 against 0.732 for chat models (d04). Weak models are at ceiling confidence (c19).
- **Position in an agent run.** Overconfidence of several models rises with steps (d08). Mid-run AUROC at 25/50/75% steps 0.49 to 0.64 (d07).
- **Reader.** Humans reading LLM explanations are misled by length (b18).

### 5.3 Interventions that worked

| Intervention | Size | Needs training? | Source |
|---|---|---|---|
| Sample agreement as confidence | AUROC 54.8% to 92.7% (GSM8K, GPT-3.5) | No | a22 |
| Verbalised instead of token probability (RLHF models) | ECE about 50% lower relative | No | b10 |
| Top-k answers with probabilities | ECE 0.234 to 0.065 (SciQ gpt-3.5) | No | b11 |
| Reason first, then state confidence | AUROC 0.56 to 0.80 | No (needs a reasoning-capable model) | d01 |
| Thinking-mode model | ECE 0.207 to 0.063 (Qwen3) | No | d02 |
| In-context slow-thinking examples | GLM-4-32B ECE 0.150 to 0.029, AUROC 0.631 to 0.796 | No | c14 |
| Platt scaling or temperature | ECE to about 0.01 | No (fit on logged data) | d07, b03 |
| Words mapped via held-out data | ECE 0.166 to 0.064 | No (fit on logged data) | c08 |
| Per-slice recalibration | ECE 0.063 to 0.053 | A trained recalibrator in d11; a count table may do | d11 |
| Confidence-weighted vote | 41% to 46% cost cut at same accuracy | Needs logprobs for P(True) | c32 |
| Confidence-gated retry | 54.5 at 3.87 attempts vs 47.5 at 10 | No | c33 |
| Unanimity of a small window as stop | 67% to 84% fewer samples on easy sets, 34% on MATH | No | d12 |
| Finetune on 1,000+ graded answers | Large; beats prompting | Yes | a25 |
| Optimal decision rule applied in code | Utility gain up to +0.685 on HLE | No | c34 |
| Adversarial review frame | Overconfident failures 72% to 45% | No, but cost doubles (12.7 to 23.4 steps) | d07 |

### 5.4 Interventions that did not work, and failures

- Chain of thought in the prompt for calibration (b11: 2-stage CoT TriviaQA ECE 0.110 vs 0.050).
- Human-inspired prompts for resolution: ECE falls, AUROC stays near 0.5 (b08).
- Telling the model to use its confidence: no change in abstain behaviour (c34).
- Raising the penalty for a wrong answer: barely changes behaviour (c34).
- Few-shot self-evaluation helps calibration, not AUROC (a20, b04).
- Pure self-review: breaks as many answers as it fixes (c27, a29).
- Aggressive trace filtering by confidence: lowers accuracy in 8 of 20 settings (d06).
- Prompt-only calibration does not improve as the base model improves (a25): AUROC improves slightly, ECE does not.
- Trained confidence heads transfer partly: out-of-domain TruthfulQA ECE worsened .10 to .18 (c22); MMLU-Pro to HLE ECE 0.504 (d05).
- Training single-question confidence did not transfer to pairwise comparison, nor the reverse (c22).
- Human cue findings do not transfer to LLMs in one test: LLM JOL slope near zero (c31).

### 5.5 Contradictions and how they stand

| Conflict | Sides | Likely reason | Status |
|---|---|---|---|
| Does verbal confidence beat token probability? | Tian: yes on ECE (RLHF chat). Xiong: verbal discriminates little (AUROC about 0.5 to 0.63). Kapoor: verbal discriminates better but poor ECE | Different metric (ECE vs AUROC), different model, dataset | Not contradictory once metrics are separated; both true |
| Does reasoning improve calibration? | Yoon: 33 of 36 settings. Zeng: worse on factual QA for small open models, better on AIME. Hiremath: accuracy and ECE move apart (47 questions). Ghosh: strong models still ECE .185 at 99.5% confidence | Task and model set; closed frontier models not checked | Contested (K11) |
| Is the hard-easy effect real in LLMs? | Michael: yes, 11 models. Mechanism: regression to the mean (asserted, not tested) | Item sets not representative | Contested (K03) |
| Does post-hoc checking add information? | Human delayed JOL: yes (g = 0.93). Kaddour: post-run AUROC no better than pre-run | Visible answer vs blind re-solve; N=100 | Open (K24) |
| Does agreement signal correctness? | d09: AUROC up to 0.78. d10: Spearman only 0.20 to 0.59 on GPQA | Task type; hard multiple choice vs tool use | Both true; agreement is a hint (G4) |
| Self-correction | Huang: hurts. ConfTuner, verbal self-verification preprint: gains after training | Training vs prompting | Prompt-only: hurts; trained: may help |

### 5.6 Cautions on the evidence

- Most LLM evidence is 2022 to 2024 models. Newer-model evidence is mostly single 2026 preprints (c15, c17 to c19, c30, b23, d04, d05, d07 to d10, d14).
- b01 to b05 are one paper (Kadavath); counted as one source.
- Some human numbers are from abstracts or secondary summaries (a08, a09, a14, a11).
- Protocol sensitivity (K16) means any single reported ECE or AUROC could shift with answer alias, scoring or token context.
- No study tests confidence signals inside a multi-step agent loop at equal tokens.

---

## 6. Language models

### 6.1 What the stated number is

An LLM's stated confidence is a text output generated like any other. It is shaped by training data (certainty markers co-occur with questions, uncertainty markers with answers; a27), and by RLHF (reward models score plain 4.03, strengtheners 0.82, weakeners -1.86; c26). It clusters at 80% to 100%, mostly in multiples of 5 (c09), 91.4% of chat-model outputs against 61.1% for reasoning models (c18).

### 6.2 By generation of model

| Period | Typical picture | Key numbers |
|---|---|---|
| Pretrained base models, 2022 | Well calibrated on lettered multiple choice with few-shot; calibration rises with size | Kadavath: sizes 800M to 52B |
| RLHF chat models, 2022 to 2023 | Raw probabilities look miscalibrated; verbalised confidence better calibrated; discrimination weak | Tian ECE 0.140 to 0.050 (TriviaQA); Xiong GPT-4 AUROC 62.7% |
| 2024 open models | Prompt-only calibration limited; finetuning on about 1,000 graded examples works | Kapoor a25 |
| Reasoning models, 2025 to 2026 | Better calibrated and more discriminating when they reason first; small hard-easy slope; still overconfident on hard novel items | Yoon 33 of 36; Michael slope 0.168; correlation 0.94 vs 0.48 |
| Agents, 2025 to 2026 | Stated success far above real; weak discrimination; behaviour consistency better; consistent-wrong floor | d05, d07, d09 |

### 6.3 What changed confidence quality, ordered by size

1. **Real reasoning before stating** (AUROC 0.56 to 0.80; ECE 0.207 to 0.063). Cause per ablation: exploration and backtracking, not reasoning about confidence itself (b16).
2. **Counting agreement over samples** (AUROC 54.8% to 92.7% on arithmetic). Smaller or absent on knowledge tasks.
3. **Post-hoc recalibration** (ECE to 0.01 to 0.06). No AUROC change.
4. **Prompt format** (top-k, verbalised vs token). ECE only.
5. **Finetuning** (needs weights; not available to us).

### 6.4 How confidence is used

- Decisions follow the stated number closely (d08), yet models do not use the number in abstain decisions the way a rational agent would (c34). The two findings fit if the model is a rational user of its own number when forced, but its stated number is poor evidence.
- In debate, confidence rises as arguments are exchanged (72.9% to about 83%) without new evidence (c16).
- Verbal confidence correlates with the trace more than with hidden knowledge: a reader model that sees only the trace recovers the score (AUROC 0.841 vs 0.851; d01). So the stated number mostly summarises the reasoning trace. It adds no independent information beyond what the trace shows.

### 6.5 What LLMs do not do

- LLM judgments of learning do not track recognition (slope B 0.013 to 0.045 with CIs including 0 vs humans 0.167; c31). Do not ask the agent to predict its own future performance.
- Models find their own text more plausible and score their own patches 23 points higher (b04, d07).
- Hedges do not follow intrinsic uncertainty (a26: faithfulness about 0.5).

### 6.6 Limits specific to our setting

- Our agent is scaffolded with a closed model, so token probabilities and hidden states may not be available. Of the signals, available ones are: stated confidence, sample agreement, check outcomes, trace events.
- Nothing here is measured on a multi-step schema loop at equal tokens.

---

## 7. What our agent should take

Status marks: [E] established, [S] single source, [C] contested. Schema parts: G guardrail, S state, O operator, M memory.

### 7.1 Add now (established)

| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| A1 | **Never use a stated confidence number alone as a verdict, stop signal or selector.** It clusters at 80-100% and GPT-4 average AUROC is 62.7%. Already in 4b ("Using a model's verbal confidence to stop"); extend to every state. | G (add to G10/G5 text) | [E] | K07; a22, b06 to b08, c09, c10, d01, d09 |
| A2 | **Report AUROC beside ECE for every confidence signal; reject signals under about 0.65 AUROC on our tasks.** Add a distinct-value count so a constant signal is flagged. | Logging (SCHEMA section 6) and G7 | [E] | K07, K10; b07, c10, b16 |
| A3 | **Agreement of independent short samples, counted in code, is the first-choice confidence signal.** Cluster by final answer. Use it as a hint only (G4). | S7 SELECT, S0 gate record | [E] | K08; a22, a24, b09, d09 |
| A4 | **Agreement is not validity: a floor of consistent-wrong items (5.5% to 28%) exists.** Agreement cannot be the only gate to submit. Route to an outside check or a different-method re-solve. | G4, S8 | [E] | K05 partially, K20; d09, d10, a04 |
| A5 | **Calibration is per task type, not global.** Keep a lookup of observed accuracy by signal bin per problem class (the S0 class record). | M (class record), S0 | [E] | K17, K25; d11, d05, c22 |
| A6 | **Measure calibration on our own representative item mix, not a hand-picked hard set. Fix the protocol (answer string, grader, context) once.** Protocol changes flip winners. | G7, logging | [E] | K16, K03; c30, b23 |
| A7 | **Do not use confidence-raising or self-doubt prompts; doubt comes only from a failing check or disagreement.** Reinforces G1, G2. Bare reconsider prompts flip answers to wrong ones. | G1, G2 | [E] | K14; c27, a29, c28 |
| A8 | **Elicit confidence, if at all, only after a real reasoning pass; never right after a no-reasoning answer.** AUROC 0.56 with no reasoning. | G (elicitation rule), S4 | [E] direction; size [S] | K21; d01, d02, b15 |
| A9 | **Elicit as several candidates with probabilities that share one budget (top-k, normalised in code), not one number; do not add chain of thought for calibration's sake.** Helps ECE, not resolution. | G5 | [E] for ECE | K09; b11, c07, a23 |
| A10 | **A judge or checker sees no proposed answer, no authorship, and judges length-normalised short text.** Foresight bias, self-preference, length illusion. | G5 | [E] | a16, b04, d07, b18, c26 |
| A11 | **The agent's decision (answer, verify, abstain) is made by code from a recalibrated signal, never by the model reading its own number.** Models do not use their stated confidence consistently. | Section 1 (who does what), G5 | [E]/[S] mix; direction [E] | K19, K22; c34, d08 |
| A12 | **Do not ask the agent to predict its own future success or learning.** | G10 | [S] | K18; c31, d07 |
| A13 | **Do not import the Dunning-Kruger "weak is unaware" rule; do not build a skill-dependent confidence correction on it.** | none | [E] | K04; b19, b20 |
| A14 | **Do not let confidence rise across rounds of argument or revision without a new passing check.** | G2, G3 | [S] | c16, d08 |

### 7.2 Test first

| # | Item | Schema part | Status | Evidence | Why not yet |
|---|---|---|---|---|---|
| T1 | **Blind re-solve as the delayed-JOL analogue.** Fresh context, question only, compare with the first answer; disagreement triggers verify. | O re-examine, S8 | [S] (human [E], LLM untested) | K02, K24; a12 to a14, d15, d17, d07 | No LLM test; Kaddour's review was answer-visible |
| T2 | **Agreement of k short samples versus one long trace with stated score, at equal tokens, on multi-step items.** | S3, S7 | [S] | K08, K21, K23; d01, d09, a22 | Only QA at equal tokens (one model, 270 items) |
| T3 | **Cheap gate for verification: early-sample disagreement, token-confidence dip, stated confidence after reasoning.** | S4, S8, G1 | [S] | K06, K23; d06, d12, a18, a19 | Not tested as a re-examination gate in an agent |
| T4 | **Confidence-gated revision versus always-revise versus never-revise.** | S5 | [S] | K14, K15; c28, c33, c27 | Gains come from trained confidence; prompt-only untested here |
| T5 | **Confidence-weighted vote with early stop versus fixed N.** | S3, S7 | [S] | K15; c32, c33, d12 | P(True) needs logprobs; verbal weight has smaller gain |
| T6 | **Count-table recalibration: how many labelled runs per task type and bin.** | M class record | [S] | K25; d11, d05 | No no-training measurement exists |
| T7 | **Hard-easy: does a difficulty-dependent correction pay?** | G12, S0 | [C] | K03, K26; d04, b21, a09 | Cause unknown; reasoning slope small |
| T8 | **Adversarial fresh-instance verification versus same-context self-review.** | S8, G5 | [S] | K27; d07 | One domain, N=100 |
| T9 | **Thinking-mode confidence versus non-thinking, on closed frontier models and our tasks.** | S (elicit after reasoning) | [C] | K11; b15, d02, d03, c15 | No closed-model data |
| T10 | **Top-k elicitation versus single number on our tasks (AUROC and ECE).** | G5 | [S] for our tasks | K09; b11 | ECE gain known; AUROC gain not |
| T11 | **Fluency-cue trap: does the agent's confidence follow fluent wrong rationale?** | G | [S] | K01 | Planted-cue items not built |
| T12 | **Confidence faithfulness across steps in our loop: does action change with the signal, and does overconfidence rise with step?** | S checkpoints | [S] | K22, K19; d08, d07 | Single-domain results |

---

## 8. Concrete tests on our bench

All arms run at equal total tokens (setup cost counted, G7). Report for every test: AUROC, ECE (10 fixed bins), mean confidence minus accuracy, selective accuracy at 50% coverage, tokens per item. Two held-out splits: fit maps on split one, report on split two. Use a representative item mix; log item difficulty proxy (plain pass rate of the class).

| Test | Item type | Arms (equal tokens) | Metric | Expected effect |
|---|---|---|---|---|
| T-A: signal comparison | Mixed set with exact answers (maths, logic, short ARC-style with check); at least 200 items | (1) one answer, stated confidence right after a no-reasoning answer; (2) one long reasoning trace, stated score after it; (3) k=4 short samples, agreement fraction in code; (4) k=2 samples, binary agree/disagree + remaining budget on a third | AUROC of signal for correctness; selective accuracy at 50% | (1) near 0.56 to 0.62; (2) near 0.80; (3) 0.70 to 0.90 on arithmetic-like items, lower on hard knowledge; (4) between. Predict (3) and (2) close at matched tokens |
| T-B: blind re-solve | Same set | (1) verify with answer visible ("is this right?"); (2) blind fresh re-solve from the question only, compare in code; (3) no verify | AUROC of disagreement for error; net flips right-to-wrong and wrong-to-right; tokens | (2) AUROC above (1) by 0.05 or more; (1) near the pre-run level (d07) |
| T-C: verify gate | Items with a check | (1) always verify; (2) verify when two early samples disagree; (3) verify when token-confidence dips (if logprobs exist); (4) verify when stated confidence after reasoning is below a threshold from split one | Accuracy at equal tokens; share of errors caught; share of verifies wasted | (2) catches most catchable errors at about half the verify cost; misses consistent-wrong items |
| T-D: consistent-wrong seed | Items where the plain model is known to be wrong with agreement 0.8 or higher (collect from T-A logs) | (1) agreement gate only; (2) agreement gate + outside check (tool or test); (3) agreement gate + different-method re-solve (e.g. work backwards, O5) | Share of consistent-wrong items caught | (1) near 0%; (2) high where a check exists; (3) partial. Establishes the floor from d09 and d10 on our own data |
| T-E: revision policy | Items with first-pass errors and correct answers mixed | (1) always revise; (2) revise when signal weak; (3) never revise (resample instead) | Right-to-wrong flips, wrong-to-right flips, net accuracy | (1) flips right answers (c27); (2) net gain small but positive; (3) baseline |
| T-F: weighted vote and early stop | Closed-answer set | (1) fixed N=5 majority; (2) confidence-weighted vote with weights from stated confidence after reasoning; (3) stop on unanimity of first 3 | Accuracy; mean tokens | (3) saves 30% to 80% tokens on easy items; (2) small gain (0.2 to 1.6 points per c32) |
| T-G: recalibration table size | Graded runs by task type | Build a bin-count map from n = 25, 50, 100, 200 runs per type | ECE on held-out runs and under task-type shift (fit on one type, test on another) | ECE falls to near 0.05 by n about 100; no AUROC change; shift hurts without refit |
| T-H: elicitation format | Same items | (1) single number; (2) top-3 with probabilities summing to 100, normalised in code; (3) binary "right/wrong" | AUROC and ECE | (2) lower ECE (b11), AUROC unchanged; (3) lowest AUROC (c32: 52.2%) |
| T-I: fluency trap | Pairs of items: a long fluent wrong rationale vs a short correct one | Confidence from (1) stated; (2) agreement of samples; (3) with a length-normalised blind judge | Rate at which fluency wins | (1) follows fluency; (2) and (3) do not |
| T-J: hard-easy check | Bin our items by plain pass rate in 5 bins | Report calibration gap per bin for chosen signal | Slope of gap against difficulty with bootstrap CI | Chat model slope near 0.7; reasoning near 0.17; add correction only if slope CI excludes 0.3 and map beats global |
| T-K: step drift | Multi-step runs | Log stated confidence at each checkpoint and final outcome | AUROC by step; bias by step; act/verify rate by bin | Overconfidence rises with step (d08); late confidence no better than early |
| T-L: thinking vs non-thinking elicitation | Same items on our model | Confidence before reasoning; after reasoning; thinking off vs on | ECE, AUROC | Thinking on, after reasoning: ECE down by half (d02); verify on closed model |

Run T-A, T-B, T-D first (section "Order to run" in UNKNOWNS.md).

---

## 9. What does not transfer, and why

1. **Delayed-JOL numbers (g = 0.93).** The effect depends on a cue-alone retrieval attempt after time passes. An LLM has no memory trace that fades. Only the structure transfers (blind re-solve), not the size. LLM JOLs do not track recognition (c31).
2. **Feeling of rightness from reading ease.** Perceptual fluency did not change FOR even in humans (a18). LLMs have no reading effort. The useful analogue is answer fluency as speed of agreement among first answers, not text style.
3. **Dunning-Kruger.** Quartile pattern is an artefact in humans (b19, b20). Weak LLMs are at ceiling confidence (c19) for a different reason (training and format), not lack of skill-specific awareness.
4. **Human hard-easy debate as settled.** The human evidence is split (selection vs real bias). LLM sets are not representative (d04). Treat the LLM pattern as a measurement task, not a theory.
5. **Koriat's sign flip as common.** Only one lab, one statistic unreconciled, consensually wrong items were chosen on purpose (a05). The LLM version of consistent-and-wrong is measured separately (d09, d10) and is real; the sign reversal itself is not shown in LLMs.
6. **Training-based fixes.** Kapoor, Lin, ConfTuner, CALIBER (d14), trajectory calibrators (d05) need weights, logprobs or trained heads. Not available under the no-training rule. Only the lesson transfers: calibration needs labelled data of our own, and a count table can do the post-hoc part.
7. **Logprob methods.** CISC with P(True), DeepConf, semantic entropy probes (d13) need token probabilities or hidden states. Usable only if the model API exposes them.
8. **Single-question QA results.** Almost all calibration numbers come from QA with short answers. Our schema runs multi-step work where outcome is not a single string. Agent studies (d05, d07 to d09) are closer but cover search and coding, not our items.
9. **Human readers' misled-by-length results.** They concern human trust in LLM text. They transfer to a model judge only as a hypothesis (verbosity bias in G5), which other sources support.
10. **Self-report of feelings.** FOR and FOE are measured by questionnaires and reaction time. An LLM report of "I feel sure" is a text output (G10).

---

## 10. Open questions

1. At equal tokens, does agreement among k short samples beat one long trace with a stated score, on multi-step tasks (not QA)? Only one model on fact retrieval at 270 items says "about equal".
2. Does a blind re-solve with a current reasoning model give the delayed-JOL gain? Nobody has run it.
3. Is there a cheap signal that works as a feeling of rightness (token dip, early disagreement) without extra samples, as a gate for re-examination in an agent?
4. What catches a consistent-and-wrong item? Estimated 5.5% to 28% of items; catch rate by outside check or different-method re-solve unmeasured.
5. How many labelled runs per task type does a count-table recalibration need? Unmeasured without training.
6. Is the hard-easy pattern in LLMs real, or regression to the mean? Needs a representative design and a test of the regression account.
7. Does thinking-mode calibration hold on closed frontier models? The Qwen3 row in Yoon is suspect (identical to QwQ).
8. Does confidence given before the work (budgeting) differ in value from confidence after (checking)? d14 argues for two separate questions; d07 found pre-run as good as post-run, not significant at N=100.
9. Do multi-step runs drift to overconfidence in our loop, and does the drift matter for checkpoints?
10. How stable are results to protocol details (alias, grader, context)? K16 says unstable; we need our own sensitivity run.
11. Original Koriat sign-flip statistic: within-person gamma .24 for consensually wrong items against an aggregate negative. Needs the full paper figures.
12. Moderators in Rhodes and Tauber (full text not read): do they say the effect shrinks with some cue types or intervals?
13. Do metacognitive skills form one faculty? Single-question and pairwise confidence did not transfer to each other (c22). If separate, we need one test per slot.

---

## 11. Sources

[V] = opened and read in this research run (full text, page text or abstract record as noted in the evidence line). [M] = snippet or secondary summary only; do not quote numbers.

**Human metamemory and overconfidence**

- [M] a01 Koriat (1997) cue-utilization approach to JOL. https://doi.org/10.1037/0096-3445.126.4.349
- [V] a02 Koriat, Ackerman, Lockl and Schneider (2009) The easily learned, easily remembered heuristic in children. https://newiipdm.haifa.ac.il/wp-content/uploads/2015/05/2009-Koriat-Ackerman-Lockl-Schneider-Easily-Learned.pdf
- [M] a03 Koriat (1993) Accessibility model of the feeling of knowing. https://doi.org/10.1037/0033-295X.100.4.609
- [V] a04 to a07 Koriat (2012) The self-consistency model of subjective confidence. https://doi.org/10.1037/a0025648 and https://newiipdm.haifa.ac.il/wp-content/uploads/2015/05/2012-Psychological-Review.pdf
- [M] a08 Gigerenzer, Hoffrage and Kleinbolting (1991) Probabilistic mental models. https://doi.org/10.1037/0033-295X.98.4.506
- [M] a09 Juslin, Winman and Olsson (2000) Naive empiricism and dogmatism. https://doi.org/10.1037/0033-295X.107.2.384
- [M] a10 Moore and Healy (2008) The trouble with overconfidence. https://doi.org/10.1037/0033-295X.115.2.502
- [V] a11, d16 Kruger and Dunning (1999) Unskilled and unaware of it (abstract record). https://doi.org/10.1037/0022-3514.77.6.1121 and https://pubmed.ncbi.nlm.nih.gov/10626367/
- [M] a12 Nelson and Dunlosky (1991) Delayed-JOL effect. https://doi.org/10.1111/j.1467-9280.1991.tb00147.x
- [V] a13 Dunlosky and Nelson (1994) Sensitivity of JOLs to study activities. https://www.gwern.net/docs/spaced-repetition/1994-dunlosky.pdf
- [V, abstract record] a14, b25, d15 Rhodes and Tauber (2011) Delaying JOLs meta-analysis. https://doi.org/10.1037/a0021705 and https://pubmed.ncbi.nlm.nih.gov/21219059/
- [M] a15 Benjamin, Bjork and Schwartz (1998) The mismeasure of memory. https://doi.org/10.1037/0096-3445.127.1.55
- [M] a16 Koriat and Bjork (2005) Illusions of competence. https://doi.org/10.1037/0278-7393.31.2.187
- [M] a17 Thompson, Prowse Turner and Pennycook (2011) Intuition, reason, and metacognition. https://doi.org/10.1016/j.cogpsych.2011.06.001
- [V, landing page] a18 Thompson et al. (2013) Answer fluency and perceptual fluency. https://knowledge.lancashire.ac.uk/7167
- [V] a19, b22 Gangemi, Bourgeois-Gironde and Mancini (2015) Feelings of error in reasoning. https://apc.it/wp-content/uploads/2014/10/Feelings-of-error-in-reasoning-rev.pdf
- [M] a31 Pleskac and Busemeyer (2010) Two-stage dynamic signal detection. https://doi.org/10.1037/a0019737
- [M] a32 Fleming and Daw (2017) Self-evaluation of decision-making. https://doi.org/10.1037/rev0000045
- [M] a33 Hoffrage (2011) Recognition judgments and the recognition heuristic. https://dlab.sauder.ubc.ca/sjdm/journal/11/rh8/rh8.html
- [V] b19 Gignac and Zajenkowski (2020) The Dunning-Kruger effect is (mostly) a statistical artefact. https://www.gwern.net/doc/iq/2020-gignac.pdf
- [V] b20 Dunkel, Nedelec and van der Linden (2023) Reevaluating the Dunning-Kruger effect. https://www.gwern.net/doc/iq/2023-dunkel.pdf
- [V] b21 Healy and Moore (2007) Bayesian Overconfidence. https://healy.econ.ohio-state.edu/papers/Healy_Moore-Overconfidence.pdf
- [M] b24 Merkle (2009) The disutility of the hard-easy effect. https://soar.wichita.edu/entities/publication/e9a6d5d1-51a9-4b2d-9386-9c8ca6269852
- [M] b26 Wang and Thompson (2019) / Stewart thesis, response speed and FOR. https://uwspace.uwaterloo.ca/items/e72e657a-7ced-43af-b7a8-0f5d30b19ad7
- [M] b27 Fleming and Lau (2014) How to measure metacognition. https://www.frontiersin.org/articles/10.3389/fnhum.2014.00443/pdf
- [M] b28 Rahnev (2024) comparison of 17 measures of metacognition. https://rahnevlab.gatech.edu/documents/papers/Rahnev_2024.pdf
- [V, abstract record] d17 Dunlosky and Nelson (1992) Kind of cue and the delayed-JOL effect. https://europepmc.org/search?query=Importance%20of%20the%20kind%20of%20cue%20for%20judgments%20of%20learning

**LLM confidence and calibration**

- [V] a20, b01 to b05, c01 to c05 Kadavath et al. (2022) Language models (mostly) know what they know. https://arxiv.org/abs/2207.05221
- [V] a21 Lin, Hilton and Evans (2022) Teaching models to express their uncertainty in words. https://arxiv.org/abs/2205.14334
- [V] a22, b06 to b09, c09 to c12 Xiong et al. (2024) Can LLMs express their uncertainty? https://arxiv.org/abs/2306.13063
- [V] a23, b10 to b12, c06 to c08 Tian et al. (2023) Just ask for calibration. https://arxiv.org/abs/2305.14975
- [V] a24, b13 Kuhn, Gal and Farquhar (2023) Semantic uncertainty. https://arxiv.org/abs/2302.09664
- [V] a25, b14, c23, c24 Kapoor et al. (2024) LLMs must be taught to know what they don't know. https://arxiv.org/abs/2406.08391 (b14 abstract page only)
- [V] a26 Yona, Aharoni and Geva (2024) Can LLMs faithfully express intrinsic uncertainty in words? https://arxiv.org/abs/2405.16908
- [V] a27 Zhou, Jurafsky and Hashimoto (2023) Navigating the grey area. https://arxiv.org/abs/2302.13439
- [V] a28, b17, b18, c20 Steyvers et al. (2025) What LLMs know and what people think they know. https://arxiv.org/abs/2401.13835
- [V] a29 Pawitan and Holmes (2024) Confidence in the reasoning of LLMs. https://arxiv.org/abs/2412.15296
- [V] a30 Mielke et al. (2022) Reducing conversational agents' overconfidence through linguistic calibration. https://arxiv.org/abs/2012.14983
- [V] b15, b16, c13, c14, d02 Yoon et al. (2025) Reasoning models better express their confidence. https://arxiv.org/abs/2505.14489
- [V, abstract page] b23 Do LLMs know what they know? Metacognitive efficiency with signal detection theory (2026). https://arxiv.org/abs/2603.25112
- [V] c15 Hiremath and Hiremath (2026) Calibration drift under reasoning. https://arxiv.org/abs/2606.11211
- [V] c16 Prasad and Nguyen (2025) When two LLMs debate, both think they'll win. https://arxiv.org/abs/2505.19184
- [V] c17, c18, d04 Michael, BenShushan, Bien and Moore (2026) Confidence calibration in LLMs. https://arxiv.org/abs/2605.23909
- [V] c19 Ghosh and Panday (2026) The Dunning-Kruger effect in LLMs. https://arxiv.org/abs/2603.09985
- [V] c21 Steyvers and Peters (2025) Metacognition and uncertainty communication in humans and LLMs. https://arxiv.org/abs/2504.14045
- [V] c22 Steyvers, Belem and Smyth (2025) Improving metacognition and uncertainty communication in language models. https://arxiv.org/abs/2510.05126
- [V, abstract page] c25 Liu et al. (2025) MetaFaith. https://arxiv.org/abs/2505.24858
- [V] c26 Zhou et al. (2024) Relying on the unreliable. https://arxiv.org/abs/2401.06730
- [V] c27 Huang et al. (2024) LLMs cannot self-correct reasoning yet. https://arxiv.org/abs/2310.01798
- [V] c28 Li, Xiong, Wu and Hooi (2025) ConfTuner. https://arxiv.org/abs/2508.18847
- [V] c29 Verbalized confidence triggers self-verification (2025). https://arxiv.org/abs/2506.03723
- [V] c30 Kim and Kang (2026) Same answer, different confidence: protocol sensitivity. https://arxiv.org/abs/2605.27752
- [V] c31 Judgment of learning in generative AI, garden-path preprint (2025). https://arxiv.org/abs/2410.13392
- [V] c32 Taubenfeld et al. (2025) Confidence improves self-consistency in LLMs. https://arxiv.org/abs/2502.06233
- [V] c33 BrowseConf (2025) confidence-guided test-time scaling for search agents. https://arxiv.org/abs/2510.23458
- [V] c34 Are LLM decisions faithful to verbal confidence? (2026). https://arxiv.org/abs/2601.07767
- [V] d01 Podolak and Verma (2025) Read your own mind. https://arxiv.org/abs/2505.23845
- [V] d03 Zeng, Xuan, Cui and Voigt (2025) Thinking out loud. https://arxiv.org/abs/2504.06564
- [V] d05 Zhang, Xiong and Wu (2026) Agentic confidence calibration. https://arxiv.org/abs/2601.15778
- [V] d06 Fu et al. (2025) Deep Think with Confidence. https://arxiv.org/abs/2508.15260
- [V] d07 Kaddour et al. (2026) Agentic uncertainty reveals agentic overconfidence. https://arxiv.org/abs/2602.06948
- [V] d08 Barkan, Black and Sourbut (2025) Do LLMs know what they are capable of? https://arxiv.org/abs/2512.24661
- [V] d09 When agents disagree with themselves (2026). https://arxiv.org/abs/2602.11619
- [V] d10 When LLMs agree, are they right? (2026). https://arxiv.org/abs/2607.08065
- [V] d11 Li et al. (2024) Few-shot recalibration of language models. https://arxiv.org/abs/2403.18286
- [V] d12 Li et al. (2024) Early-stopping self-consistency. https://arxiv.org/abs/2401.10480
- [V] d13 Kossen et al. (2024) Semantic entropy probes. https://arxiv.org/abs/2406.15927
- [V, abstract page] d14 Finlay et al. (2026) CALIBER. https://arxiv.org/abs/2606.24281
- [V, abstract page] d18 Mind the confidence gap (2025). https://arxiv.org/abs/2502.11028

Notes on the [V] marks. Many 2026 and 2025 papers in the d-series were read via page extraction, not the raw PDF, because PDF downloads were truncated (stated in each evidence line). Items cited inside other papers (Braun and Yaniv 1992, Griffin and Tversky 1992, Soll 1996, Brenner et al. 1996, Maniscalco and Lau 2012, Cash et al. 2025) were not opened.
