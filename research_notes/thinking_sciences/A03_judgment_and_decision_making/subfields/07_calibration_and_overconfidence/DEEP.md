# Calibration and overconfidence: deep document

*Subfield A03.07 of judgment and decision making. Key works: Lichtenstein, Fischhoff; Koriat. Why it matters for our agent: consistency, not stated certainty. Evidence ids (a01..d17) point to evidence_a-d.jsonl; claim ids (K01..K36) point to claims.jsonl in this folder. Where a number was only seen second-hand, the text says so. Cross-check notes from critique.md are applied: the Lin 2022 table rows, the Steyvers model name (GPT-4o, not 4o mini) and the Xiong GSM8K row label are corrected here.*

Related subfields researched in parallel (links only, not covered here): Dual-process theory; Debiasing and cognitive forcing; Belief updating; Aggregation and extremizing; Metacognition and higher-order representation; Conformity; Pre-mortem; Search over thoughts; Epistemic value and curiosity.

## 1. What it is

Calibration means that stated confidence matches how often the answer is right. If a judge says "70%" on 100 items, about 70 should be correct. Overconfidence means stated confidence is higher than the hit rate.

There are three different things called overconfidence (b01, b08, b26):

- **Overestimation**: you think your own score or accuracy is higher than it is.
- **Overplacement**: you think you rank higher than other people.
- **Overprecision**: you are too sure that your answer or range is right. Intervals are too narrow.

They have different causes. They hardly correlate across tasks. Cross-task r was 0.12 for overestimation, 0.10 for overplacement and 0.68 for overprecision, but different overprecision measures correlated only r = .11 with each other (b08, N = 379 and 138). So "overconfidence" is a family, not one trait (K05).

Two skills are mixed up in this field and must be kept apart:

- **Calibration**: does the average stated number match the average hit rate? Measured by ECE, the Brier calibration term, or a reliability diagram.
- **Discrimination (resolution)**: does confidence go up on right answers and down on wrong ones? Measured by AUROC or AUC.

A judge who says "93.6%" on every item, on a task where it is right 93.6% of the time, is perfectly calibrated and has zero discrimination (b14, c10). For our agent, discrimination is the useful skill. A stop rule, an "escalate" rule or a "submit now" rule only works if confidence separates right from wrong.

The agent angle: SCHEMA.md already says "never use a model's verbal confidence to stop" (section 4b) and "samples from one model are not independent" (G4). This document gives the numbers behind both and lists what can replace stated certainty: agreement across fresh attempts, code-run checks, and per-class hit rates kept in memory.

## 2. History and theories in depth

### 2.1 The founding studies (human)

- **Adams and Adams 1960** (spelling task): about 80% correct when people claimed 100% certainty. Second-hand only (a11).
- **Oskamp 1965** (clinical case study, 32 subjects): accuracy 26%, confidence 33%. More information raised confidence from 33% to 53% while accuracy stayed under 30% (a08, a11). More data made people more sure without making them more right.
- **Fischhoff, Slovic, Lichtenstein 1977** and **Lichtenstein and Fischhoff 1977**: the founding almanac studies. People gave a probability that their answer to a two-choice question was right. Typical result: about 65-70% confidence when about 50% right; hit rate .6 at assessed .70; about 75% correct at .90; answers given with certainty (p = 1.00) were wrong about 20% of the time (a06, a07, a08, a10). Follow-ups: odds of 100:1 gave 73% correct; odds of 10,000:1 to 1,000,000:1 gave 85-90% correct, where 6:1 to 9:1 would fit; real bets did not remove it (39 of 42 accepted a bet; in a real-money replication 13 of 19 gambled, 12% wrong on items rated 50:1 or better, losses $1-$11 each) (a07). **Limit:** the 1977 paper itself was never opened. These numbers come from Plous 1993, Koriat 1980 and Wikipedia (K02).
- **Interval tasks**: 98% intervals missed the truth far more than 2% of the time. Surprise index averaged 32% over nearly 15,000 judgments (Lichtenstein and Fischhoff). Russo and Schoemaker: over 1,000 people, under 1% got 9 or 10 of 10 intervals right; surprise index 40-70%. Alpert and Raiffa 1982: 90% intervals hit as low as 50% (a08, a11).
- **Hard-easy effect** (Lichtenstein and Fischhoff 1977): overconfidence is largest near chance (children's drawings 53% right vs 68% confident; stocks 47% right vs 65% confident) and falls as accuracy rises; above about 80% accuracy people turn underconfident (a08).

### 2.2 Koriat, Lichtenstein, Fischhoff 1980: "Reasons for confidence"

This is the key mechanism paper for our agent (a01-a06, d16, K07, K08, K35).

Theory: when we judge confidence we recall reasons for the answer we chose and neglect reasons against it. Confidence follows the one-sided evidence. Two stages: (1) search knowledge until an answer is chosen; (2) review evidence and assess confidence. There is a bias in each stage (a05).

- **Evidence for the bias** (a04, 62 subjects after 6 dropped): 18.3 reasons for vs 13.4 against per subject (t(61) = 7.99, p < .001). First reason rated 3.8 for vs 3.5 against (t(61) = 2.92, p < .005).
- **Confidence tracks support for the chosen answer** (a05, pooled n = 620 answers): confidence correlated .28 with the number of reasons for the chosen answer, .17 for reasons against the rejected one, -.06 and -.07 with the other two. With the strength of the first reason: .66 for chosen, .39, .00, -.02. Mean probability was below .6 when the strength of the supporting reason was under 3, and about .9 at strength 7. Correlational only.
- **Experiment 1** (a01, d16): 73 paid volunteers (68 kept), two-choice general-knowledge items, 10 scored items per condition. A "reasons" condition (list and rate reasons for and against both options, then choose and give a probability) improved calibration clearly. Some overconfidence stayed, mostly at .9 and 1.0.
- **Experiment 2** (a02): 200 volunteers, four groups. Choose first, then write one reason: supporting, contradicting, both, or none. Only the contradicting reason helped. The supporting reason did nothing (people already do it). The "both" group improved slightly and not significantly. 11 subjects who wrote a supporting reason in the contradicting group were dropped; the result held when they were kept.
- **Follow-up** (a03): 44 subjects wrote one reason for each option before choosing. Still no gain. The order was not the cause. Contradicting reasons in the "both" group were often weak. The effect is fragile to how the reasons are produced.

Table values (per-bin hit rates) were not readable from the PDF text and are not recorded. Do not quote them.

### 2.3 Competing and refining theories

- **Probabilistic mental models** (Gigerenzer, Hoffrage, Kleinbolting 1991; a12, not opened): people answer from a reference class and the validity of one cue. Overconfidence appears because experimenters pick tricky items, not because people are biased. With random sampling from the reference class it should vanish, and the judged frequency of your own correct answers should be more accurate than single-item confidence (the "confidence-frequency effect").
- **Juslin 1994** (a13, not opened): randomly sampled almanac items show little overconfidence, hand-picked items show a lot.
- **Brenner et al. 1996** (a13, not opened): overconfidence persists beyond item selection.
- **Erev, Wallsten, Budescu 1994** and **Merkle 2009** (b06, opened): the hard-easy effect follows from random error and regression to the mean. Merkle derives that almost any judge in realistic conditions shows it. So seeing the effect does not prove a cognitive mechanism (K04).
- **Moore and Healy 2008** (b01-b04, opened): a Bayesian account with noisy private information. Hard tasks give overestimation and underplacement. Easy tasks give underestimation and overplacement. Overprecision is separate and persists at all difficulties.
- **Dunning-Kruger** (Magnus and Peresetsky 2022; b09): the pattern is fitted almost perfectly by a censored (tobit) model with regression to the mean and no metacognitive deficit.
- **Krueger and Heck 2021** (b26): a review of Moore's book. There is a family of effects and a family of fixes, no single one.

The dispute "does representative sampling remove overconfidence?" is not settled here (K11, contested): the three key papers were not opened.

### 2.4 Calibration in practice (human experts and training)

- Weather forecasters with daily feedback are almost perfectly calibrated (Murphy and Winkler 1984). Physicians diagnosing pneumonia were poorly calibrated (Christensen-Szalanski and Bushyhead 1981). 200 judgments with intensive feedback improved calibration (Lichtenstein and Fischhoff 1980). Arkes et al. 1987: overconfidence removed after feedback on five deceptively hard problems (a09, second-hand).
- Koriat 1980 recaps a training study: 11 sessions of 200 items with feedback; almost all gain came after the first feedback round; it did not generalise to new content (a06). So the issue is not only mapping feelings to numbers.
- Experience alone did not fix it. Prims and Moore 2017 (b07): overprecision rises with age when elicited as probabilities, not with intervals (replication N = 200, r = .137, p = .053, weak).
- Debiasing training can transfer to the field (Sellier et al. 2019; N = 290, 29% fewer confirmation-bias errors; b10). That is confirmation bias, not calibration.

### 2.5 From humans to machines

- **Guo et al. 2017** (a15, a16, b13): deep nets became overconfident as they got deeper and wider, with batch norm and less weight decay. One scalar temperature fitted on held-out data fixes most of it without changing accuracy.
- **Kadavath et al. 2022** (a17, a18, c01-c05): base LMs are well calibrated on lettered multiple choice. RLHF policies look miscalibrated; T = 2.5 mostly repairs this. P(True) and P(IK) self-evaluation.
- **Lin, Hilton, Evans 2022** (a19, c06): first model that states its own confidence in words (fine-tuned GPT-3).
- **Tian 2023, Xiong 2024, Kapoor 2024, Zhou 2023** (a20-a27): the modern verbalized-confidence literature (section 6).
- 2025-2026 studies extend to reasoning models and agents (section 6).

## 3. Core findings with exact numbers

Status: **E** = two or more independent sources; **S** = single source; **C** = contested; **H** = human-only; **Old** = older models only.

| Finding | Numbers | Source (evidence ids) | Status |
|---|---|---|---|
| Extreme certainty is wrong about one time in five | p = 1.00 answers wrong about 20%; 100:1 odds gave 73% correct; 10,000:1 to 1,000,000:1 gave 85-90% correct | Fischhoff et al. 1977 via Plous, Koriat (a06, a07, a10, a11) | E (H), original not opened |
| Real money does not remove overconfidence | 39 of 42 accepted a bet; 13 of 19 gambled, 12% wrong on items rated 50:1 or better | Plous summary (a07) | S (H), second-hand |
| Hard-easy effect | 65-70% confident at about 50% right; flips to underconfidence above about 80% accuracy. Inside one design (N = 82, 18 quizzes) overestimation F(2,162) = 42.53, eta2 = .34 | Lichtenstein and Fischhoff via Plous; Moore and Healy (a08, b02) | E |
| Hard-easy effect needs no special mechanism | Derived for any noisy judge; Dunning-Kruger fitted by tobit model | Merkle 2009; Magnus and Peresetsky 2022 (b06, b09) | E |
| Overprecision persists | 90.5% nominal ranges held the truth 73.1% of the time (N = 82); hit rate 55.1% before feedback, 85.6% interim, 84.4% after; other studies 30-50% for 90% intervals | Moore and Healy 2008 (b03) | E (H) |
| Three kinds of overconfidence barely correlate | Cross-task r: overestimation 0.12, overplacement 0.10, overprecision 0.68; different precision measures r = .11; test-retest .29, .21, .49 | Li, Hale, Moore 2025 (b08, N = 379, 138) | S, consistent with b01, b26 |
| Reasons for the chosen answer drive confidence | r = .66 with strength of the first supporting reason, -.02 with reasons against the chosen answer; 18.3 vs 13.4 reasons | Koriat et al. 1980 (a04, a05) | S (H) |
| Only a counter-reason improved human calibration | Exp 2 N = 200: contradicting reason helped; supporting reason did nothing; "both" not significant; 44-subject order control null | Koriat et al. 1980 (a02, a03) | S (H) |
| Feedback helps in humans, training did not transfer | 200 judgments with feedback improved; 11 sessions of 200 items, gain after first round, no transfer | Plous; Koriat recap (a06, a09) | E (H), second-hand |
| Deep nets overconfident; one temperature fixes it | CIFAR-100 ResNet-110 ECE 16.53% to 1.26%; Birds ResNet-50 9.19% to 1.85%; CIFAR-10 ResNet-110 4.6% to 0.83%; LeNet 3.02% to 0.93%; matrix scaling overfits (21.13% on Birds) | Guo et al. 2017 (a15, b13) | S (vision) |
| Base LMs calibrated on closed formats; format fragile | Models 800M-52B, 10 equal-mass bins; "none of the above" hurts accuracy and calibration | Kadavath 2022 (a17, c01, c02) | S, Old |
| RLHF policy repaired by one temperature | T = 2.5 across MMLU, MMLU true/false, TruthfulQA (52B) | Kadavath 2022 (c03) | S, Old; Leng 2025 says RLHF teaches verbal overconfidence (c20) |
| Verbalized beats token probability for RLHF chat models | gpt-3.5 TriviaQA ECE .140 (label) to .054 (top-4), SciQ .256 to .065, TruthfulQA .451 to .203; GPT-4 TriviaQA .078 to .024, SciQ .219 to .201, TruthfulQA .445 to .350; AUC .869 vs .896 | Tian 2023 (a20, a21, c07, c08) | S, Old |
| Verbalized confidence is poor at ranking | GPT-4 average AUROC 62.7% (chance 50%); GPT-3, GPT-3.5, Vicuna ECE above 0.377; values cluster in 80-100% | Xiong 2024 (a22, b14, c09) | E |
| Low ECE is not discrimination | GPT-4 GSM8K accuracy 93.6%, ECE 0.064 by saying 100% always | Xiong 2024 (b14, c10) | E |
| Agreement across samples ranks right vs wrong | GSM8K (GPT-3.5) AUROC 54.8% (one verbalized answer, "akin to random guessing") to 92.7% (5 samples plus consistency); most gain by about 5 samples; Pair-Rank ECE as low as 0.028 | Xiong 2024 (c11, b14) | E (Old models, QA and arithmetic) |
| Consistency plus self-reflection beats either | text-davinci-003 AUROC GSM8K .867 vs .521 self-reflection alone; CSQA .743 vs .539; SVAMP .936 vs .619; TriviaQA .828 vs .653 | Chen and Mueller 2023 (c14) | S, Old |
| Top-k answers with probabilities help on hard sets only | GPT-4 SciQ ECE .201 to .056 (top-4); TruthfulQA .350 to .198; TriviaQA .024 to .041 (worse) | Tian 2023; DINCO (c08, b21) | E for the hard-set gain |
| Normalising over self-generated rivals (DINCO) | beats best baseline by average ECE 0.077 (TriviaQA) and 0.092 (SimpleQA); costs 32% over self-consistency | Stengel-Eskin 2025 (b21) | S |
| Certainty words in the prompt change accuracy | 50 markers; accuracy varied by over 80% across templates; high certainty cost 7%; 21 of 28 "100%" templates worse than "90%"; "I'm 90% sure" gave 57% correct, ECE 0.30-0.50 | Zhou 2023 (a27, c15, c16) | S, Old (GPT-3) |
| Aligned models sound decisive when samples split | faithfulness near 0.5 for all models; hedging prompts do not fix it; reward models favour confident answers | Yona 2024; Leng 2025 (b20, c20) | E |
| Fine-tuning on about 1000 graded examples beats prompting | Open models; prompting ECE does not improve as base model improves | Kapoor 2024 (a24, b16, c19) | S |
| Fine-tuned verbal confidence is not always better than a constant | Multiply-divide MSE: verbalized 15.5 vs constant 15.3 vs zero-shot answer logit 10.4; Multi-answer 22.0 vs constant 34.1 | Lin 2022 Table 1 (c06, corrected by critique) | S, medium confidence on row identity |
| Hedge language beats numbers | About 10% better AUROC and ECE than second best over 80 models on MMLU-Pro; ECE-AUROC Kendall -0.071 | Tao 2025 (d15) | S |
| For reasoning models, stated confidence beats agreement at equal K | AUROC maths K=1 71.3 to K=8 81.4; SC@2 maths 70.5; hybrid at K=2 adds +12.9 (maths) and +6.4 (STEM, humanities); flat after K=5 outside maths | Del 2026 (d01, d02) | S (3 open models) |
| Reasoning models verbalize better | 33 of 36 settings; GLM-Z1 0.07 lower accuracy but 0.037 lower ECE, 0.078 higher AUROC | Yoon 2025 (c21, c22) | S |
| Same-model agreement is often confidently wrong | gpt-4.1 agreement 0.8 or more on 77% of GPQA entries, 48% wrong; 28% confidently wrong for every runner; rho 0.19 to 0.59 | Ding 2026 (d03, d04) | E (with d05, d09) |
| Errors are correlated across families; polling needs a verifier | Most common wrong answer is 65-87% of wrong MATH responses; no consistent gain from 25 samples without a verifier | Denisov-Blanch 2026 (d05) | E |
| Three frontier models agree and are wrong | 87% three-way agreement on pass/fail, 13% of agreements correct; adversarial framing 44% agreement, 38% correct | Kaddour 2026 (d09) | S |
| Agents are overconfident before, during and after | True success 35%, 22%, 27%; post-run estimates 73% and 77%; AUROC pre vs post: GPT .62/.58, Claude .64/.55, Gemini .53/.51 (CIs overlap) | Kaddour 2026 (d07) | S |
| "Find the bugs" step cut overconfidence | ECE Gemini .66 to .53, Claude .37 to .24, GPT .42 to .30; overconfident-failure rate 72% to 45%; AUROC no gain for GPT | Kaddour 2026 (d08) | S |
| Prior outcomes in context did not fix confidence | 512 sequences of 9 contracts; AUROC barely moved; predicted success stayed above 0.5 | Barkan 2025 (d10) | S |
| Mid-run confidence got worse for Claude models | After-the-fact AUROC beat step-1 AUROC for only 4 of 10 models | Barkan 2025 (d11) | S |
| LLMs overconfident on average, hard-easy pattern | 88% confidence vs 79% accuracy across 11 models, 6 sets; some easy sets 97% accuracy vs 92% confidence | Michael 2026 (d12, d13) | S |
| People over-trust LLM explanations | Model AUC .751, .746, .781 vs human .589, .602, .592; 301 participants; 350 questions | Steyvers 2025 (a25, b18, c17) | S |
| LLM crowd matches human crowd | Brier 0.20 (SD .12) vs 0.19 (SD .19), t(60) = 0.19, p = .850; 12 LLMs vs 925 humans, 31 questions; Halawi 0.179 vs crowd 0.149, accuracy 71.5% vs 77.0% | Schoenegger; Halawi 2024 (c25, c26) | E |
| User certainty phrases push open models | Wrong suggestion with null confidence: accuracy bias 45.4 (Llama 3.1 8B), 39.2, 38.5, 21.0 points; hedging helps larger models | Sicilia 2024 (d14) | S |

## 4. Mechanisms and models

Each model is written so it can be coded.

### 4.1 Calibration, ECE and AUROC

- **ECE**: split items into M bins by stated confidence (Guo uses 15; Kadavath uses 10 equal-mass bins). In each bin compute |mean confidence - accuracy|. Weight by bin size and sum. A constant confidence equal to the base rate gets a low ECE. A coin-flip guesser on binary items saying 50% gets perfect ECE (b15).
- **AUROC**: the probability that a random right answer has higher confidence than a random wrong one. 0.5 is chance. This is the number that matters for stop and escalate rules.
- **Brier score** (Murphy partition): mean squared error of probabilities; splits into calibration and resolution terms.
- Rule: always report ECE, AUROC and a constant-confidence baseline together (K16).

### 4.2 Hard-easy as regression (Merkle, Erev)

Let true accuracy vary by item, and let stated confidence = true signal + noise. High-confidence items regress toward the mean accuracy and low-confidence items regress up. The slope of accuracy on confidence is under 1 even for an unbiased noisy judge. On hard sets (low mean accuracy) you see "overconfidence"; on easy sets you see "underconfidence". Implementation: simulate a noisy but unbiased judge with the agent's accuracy and compare, before claiming a special failure on hard items (K04).

### 4.3 Two-stage evidence model (Koriat)

Stage 1: retrieve until a first answer. Stage 2: confidence = f(support for the chosen answer). The counter-case step forces stage 2 to read evidence against as well. For an LLM: after an answer is chosen, run a separate prompt whose only job is the strongest case against it, then read confidence. The only direct LLM analogue (Kaddour's "find the bugs") cut ECE on 3 of 3 models and has no pro/con arm to compare (d08).

### 4.4 Overestimation, overplacement, overprecision (Moore and Healy)

The judge sees truth plus private noise. The posterior estimate of own score regresses to the prior mean. Hard tasks: prior mean above the true score, so overestimation. Easy tasks: below, so underestimation. Overprecision is the posterior width being smaller than the real error. Engineering use: log separately (a) stated accuracy minus real accuracy, per class and difficulty band, and (b) range hit rate versus nominal.

### 4.5 Temperature and Platt scaling (Guo)

Given logits z, calibrated probability = softmax(z / T). Fit T on a held-out set by minimising NLL. One parameter, no change in argmax. For an API model with no logits the same idea works on the stated number: fit p' = sigmoid(a * logit(p) + b) on logged (stated, outcome) pairs per class (Platt). Whether the fit transfers across classes is not measured (K36, d17).

### 4.6 Agreement as confidence (self-consistency, semantic entropy)

Draw N attempts, each from a fresh context. Normalise each final answer (code for exact answers, an equivalence judge for free text). Confidence = share of attempts in the largest group. Free text: group by meaning, then entropy over groups (Kuhn 2023; b17, c12). Pair-Rank and Avg-Conf variants (Xiong): average stated confidence over the attempts that gave the majority answer (a23, c11). Gains saturate near N = 5 (c11, d02). Failure mode: all attempts share the same wrong answer (K30).

### 4.7 Hybrid score

score = 0.5 * agreement + 0.5 * mean stated confidence over majority-answer attempts. At K = 2 this already beat K = 8 of either alone for three open reasoning models (d02). The weight was reported as robust.

### 4.8 Verbalized elicitation formats (Tian)

- one-stage top-1: "answer and probability".
- one-stage top-k: "give k guesses and the probability each is right"; use the top-1 probability. Optionally force the k probabilities to sum to 1 in code (G5).
- two-stage: answer first, then ask for the probability.
- label probability: token probability of the chosen option.
Use top-k on hard classes. Top-1 is as good on easy ones (c08).

### 4.9 Normalising over rivals (DINCO)

Ask the model to produce distractor answers. Estimate confidence for the answer and for each distractor. Divide the answer's confidence by the sum over all of them. Add consistency across paraphrases. This fixes "high confidence in a claim and in its contradiction" (b21).

### 4.10 Why LLMs sound sure (training pressure)

Reward models prefer confident answers regardless of quality, so RLHF teaches verbal overconfidence (Leng 2025, c20). Pre-training text links certainty words with questions and hedges with answers, so prompt wording sways accuracy (Zhou 2023, a27). Aligned models state answers decisively even when their own samples split (Yona 2024, b20).

### 4.11 Agent view of confidence

Kaddour (d07-d09) and Barkan (d10, d11) ask the agent for a probability of success before, during and after a coding task. In all frontier models tested, stated confidence stayed far above the true rate, and reading the finished patch did not help much (reflection, not test results). Our design says that code, not the model, computes the quantity that gates behaviour (G5, G6).

## 5. What holds up

### 5.1 Robust

- **Overconfidence at high stated confidence** on hard general-knowledge questions, with real stakes (K01). Fischhoff, Plous follow-ups and Koriat agree (human; the founding numbers are second-hand).
- **Difficulty dependence** (K03): seen inside one design (b02) and explained by regression (b06). The sign flips, so one global offset is wrong.
- **Overprecision at all difficulties** (K06): 73.1% hit rate for 90.5% ranges. Elicitation changes the size but never produces underprecision (b03, b04).
- **Ranking is the weak point of verbalized LLM confidence** (K15): GPT-4 AUROC 62.7%. Xiong, Steyvers and Kapoor agree that ECE is easy to lower but separating right from wrong stays weak (b23).
- **Agreement beats the stated number on AUROC for plain QA and arithmetic** (K17): Xiong, Kuhn, Wang (agreement rate correlates with accuracy), Chen and Mueller.
- **Same-model agreement hides shared errors** (K30): Ding, Denisov-Blanch, Kaddour.
- **LLM crowds approach human crowds on forecasting** (K26).

### 5.2 Failures, nulls and contested items

- Koriat's "both" group did not improve although the full reasons task did, and a 44-subject order control was null (a02, a03). The counter-case gain is fragile in humans.
- Prims and Moore: the age effect on overprecision was weak, r = .137, p = .053 (b07).
- Representative sampling (K11): unresolved here. Michael 2026 (d12, d13) found a human-like hard-easy pattern in 11 LLMs but did not sample at random from a real task mix.
- Post-attempt vs pre-attempt confidence (K25): hidden-state probes gained +0.09 to +0.15 AUROC (b22, preprint). In agent coding, reading the patch gave no better AUROC (GPT .62 pre, .58 post; Claude .64, .55), and only 4 of 10 models improved by the end (d07, d11). Test results and reflection were never separated.
- Tian vs Xiong: verbalized ECE good vs verbalized ECE above 0.377. This is a prompt and dataset effect: Tian used one-stage top-k prompts on easy trivia; Xiong used plain prompts on 8 mixed tasks (critique).
- Xiong vs Del: consistency beat verbalized in 2023 (GPT-3.5, GSM8K). For 2025 open reasoning models verbalized beats consistency at equal K (d01). The ordering depends on the model class.
- Fine-tuned verbal confidence in Lin 2022 was no better than a constant on Multiply-divide (c06).
- Persona variation lowered error correlation only a little (about 0.39 vs 0.46, garbled table) and has not been shown to improve AUROC (d06).

### 5.3 Moderators

- **Difficulty**: overconfidence large near chance, underconfidence on easy items (b02, d12).
- **Format**: closed lettered options calibrate; "none of the above" breaks it (c02).
- **Task type**: arithmetic gets the largest agreement gain, knowledge tasks less (c11). TruthfulQA stays poorly calibrated for every method (c07). Professional-knowledge tasks (law) stay poor (c09).
- **Model family and class**: Claude-1 verbalized worse than gpt-3.5 (a21). Reasoning models better than siblings (c21). Bigger models help but are far from ideal (a22).
- **Elicitation**: probabilities vs intervals change the size of overprecision, never its sign (b04, b07).
- **Prompt content**: certainty words and a user's stated certainty shift accuracy (K20, K34).
- **Time in the run**: for Claude Sonnet agents confidence rose faster on eventual successes than on failures, so AUROC fell below its start (d11).

### 5.4 Interventions that worked

- Writing one reason against the chosen answer (humans; Koriat Exp 2).
- About 200 judgments of intensive outcome feedback, in domains with fast feedback (humans).
- Temperature scaling on held-out data (deep nets).
- Top-k elicitation on hard sets; normalising over rivals (LLMs).
- Agreement over about 5 samples (LLMs, QA).
- Hybrid of agreement and stated confidence at K = 2 (reasoning models, d02).
- Fine-tuning on about 1000 graded examples (open models; not usable in a scaffold).
- "Find the bugs" before stating confidence (LLM agents; lowered ECE in 3 of 3, AUROC in 2 of 3).
- Matching explanation hedging to model confidence (human readers; narrowed the gap but did not raise human accuracy, c18).

### 5.5 Interventions that did not work, or were not shown to

- Supporting-reason writing (Koriat Exp 2).
- Balanced pro-and-con in the simple form (Koriat Exp 2, 44-subject control).
- Real money (a07).
- Experience alone (b07).
- Eight graded outcomes in context (d10).
- Prompt tweaks that lower ECE only by raising accuracy (c10).
- Hedging prompts for state-of-the-art aligned models (b20).
- Training that transfers to new content (humans, a06).
- Polling many samples without a verifier (d05).
- Reflection with no test results (d07).

## 6. Language models

### 6.1 Token probabilities

- **Base models are calibrated on closed formats** (Kadavath 2022; c01): the 52B model is very well calibrated on BIG-Bench and MMLU lettered options, overconfident only in the tails of the true/false version. Calibration improves with size and few-shot.
- **Fragile to format** (c02): replacing one option with "none of the above" hurts accuracy and calibration even at 52B.
- **RLHF policies** look miscalibrated; one T = 2.5 largely fixes this in that early recipe (c03). Tian 2023 found chat-model token probabilities poor (gpt-3.5 ECE .140 TriviaQA, .256 SciQ, .451 TruthfulQA) and verbalized confidence better. Leng 2025 finds RLHF itself drives verbalized overconfidence (c20; Llama3-8B and Mistral-7B; CDPO cut ECE by over 50% versus DPO).

### 6.2 Verbalized confidence

- **Fine-tuned** (Lin 2022, GPT-3): calibrated and moderately robust to shift. Multi-answer MSE 22.0 vs constant 34.1. Multiply-divide 15.5 vs constant 15.3, with the zero-shot logit at 10.4 (c06, corrected).
- **Prompted, vanilla** (Xiong 2024, 5 models, 8 tasks): values cluster in 80-100% in multiples of 5. GPT-3, GPT-3.5 and Vicuna mean ECE above 0.377. GPT-4 AUROC 62.7%. GPT-3 to GPT-4 gained about 22.2% AUROC. White-box AUROC 0.605 vs black-box 0.522 (narrow gap).
- **Prompted, top-k** (Tian 2023; a20, a21, c07, c08): ECE down by a relative 50% or more versus token probabilities. Claude-1 verbalized worse than gpt-3.5 at top-1 (SciQ .265 vs .234) but top-4 helped (.151). TruthfulQA stays at .372-.450. AUC gains are small (gpt-3.5 TriviaQA .869 to .896; GPT-4 TruthfulQA .462 to .622).
- **Why ECE gains mislead** (c10): CoT lowers ECE mainly by raising accuracy. GPT-4 on GSM8K scores ECE 0.064 by saying 100%.
- **Linguistic hedges** (Tao 2025; d15): free-text words like "probably", scored by a judge (Llama-4-Maverick), beat numeric verbal and token probability by about 10% AUROC and ECE over 80 models on MMLU-Pro. Small models often skip hedges. This is not a test of a few fixed ordinal levels.
- **Certainty words in the prompt** (Zhou 2023; GPT-3 and GPT-4 era): accuracy varied by over 80% across 50 markers; high certainty cost 7%; TriviaQA 42% plain vs 56% with a double-check hedge; one template at 14% where others reached near-perfect (a27, c15, c16).
- **Faithfulness** (Yona 2024): aligned models almost never hedge in line with their sample spread (about 0.5 faithfulness) (b20).

### 6.3 Sampling-based confidence

- Self-consistency: GSM8K AUROC 54.8% to 92.7% for GPT-3.5 (Xiong). The 54.8% is the M = 1 chain-of-thought row (critique). Biggest on arithmetic. Marginal gain beyond about 5 samples (c11).
- Semantic entropy (Kuhn 2023): beats token entropy and P(True) on TriviaQA and CoQA with OPT up to 30B. Exact AUROC numbers were not extracted (c12).
- Majority vote: +3 to +6 points for UL2-20B and +9 to +23 for LaMDA-137B and GPT-3 over CoT; the agreement rate correlates with accuracy (c13).
- BSDetector (Chen and Mueller; Cleanlab authors): consistency plus self-reflection, AUROC GSM8K .867 (c14).
- **2025 reasoning models** (Del 2026; gpt-oss-20b high effort, Qwen3-30B-A3B, DeepSeek-R1-8B; 17 tasks; up to 60K tokens per sample): stated confidence beats agreement at equal K. Maths VC K=1 71.3 to K=8 81.4. SC@2: maths 70.5, STEM 66.6, humanities 63.3. MMLU-Pro Math SC@2 65.9 vs VC@1 78.8. Hybrid at K=2: +12.9 (maths) and +6.4 (STEM, humanities) over single-run VC. Under extended reasoning SC is markedly weaker than under short generation (d01, d02).
- **Correlated errors** (Ding 2026; 265,000 samples, 53 runners, GPQA Diamond and AIME, K=50): rho of agreement with majority-correctness 0.20-0.59. gpt-4.1: agreement 0.89 but rho 0.19; agreement 0.8 or more on 77% of GPQA entries, 48% of those wrong; 28% of unique cases confidently wrong for every runner. gpt-4.1-mini, n = 50: Spearman agreement 0.31 [0.05, 0.57], verbalized 0.21 [-0.10, 0.49], P(True) 0.19 [-0.10, 0.45] (d03, d04).
- **No verifier** (Denisov-Blanch 2026; d05): five benchmarks; 25 samples per model at T 0.7 and 1.0; no consistent gain over one sample even at 25x cost. Most common wrong answer: 65-87% of wrong MATH responses. HLE subset accuracy 5.7%. A random-string control still showed above-chance agreement. The authors say verified domains (maths, code) are different.

### 6.4 Agents

- **Kaddour 2026** (SWE-bench Pro, 100 tasks; GPT-5.2-Codex, Gemini-3-Pro, Claude Opus 4.5; d07-d09): true success 35%, 22%, 27%; post-run estimates 73% (GPT) and 77% (Gemini). AUROC pre vs post: GPT .62 vs .58, Claude .64 vs .55, Gemini .53 vs .51, all CIs overlapping. Doubt rose equally for successes and failures. Adversarial "find the bugs": overconfidence down by up to 15 points; ECE Gemini .66 to .53, Claude .37 to .24, GPT .42 to .30; overconfident-failure rate 72% to 45%; AUROC .64 (Claude), .57 (Gemini), .55 (GPT, no gain). Overconfidence still +0.20 to +0.40 afterwards. Three-way model agreement on pass/fail: 87%, only 13% correct; adversarial 44%, 38% correct. A max-rule ensemble gave GPT AUROC .68 and the worst overconfidence. The post-execution agent read the patch with read tools; it did not run tests.
- **Barkan 2025** (d10, d11): 9 sequential contracts, 512 sequences. AUROC barely moved with prior outcomes. Sonnet 3.5 cut acceptance to about 50% (risk aversion) and profit rose; GPT 4.1 stayed near zero profit. Mid-run confidence (10 models, 70-call budget): all Claude Sonnet models grew more overconfident as they progressed; after-the-fact AUROC beat step-1 AUROC for only 4 of 10 models; several Sonnet models improved AUROC when asked to reflect on the submitted answer. Reasoning models did as well or worse.
- **Reasoning models** (Yoon 2025; 6 models, 6 datasets): better calibrated than non-reasoning siblings in 33 of 36 settings; removing alternatives and backtracking lowers calibration; slow-thinking examples in context raise a non-reasoning model's calibration; Qwen3 is better in Thinking than Non-thinking mode (c21, c22). Verbalized only. Kaddour and Barkan found no such advantage in agent tasks.
- **Hidden-state probes** (Kale 2026, preprint; b22): confidence after solving beats confidence before solving; probes beat verbal confidence by +0.09 to +0.15 AUROC. Needs weights.

### 6.5 Difficulty and sampling

Michael 2026 (d12, d13), preregistered, 11 LLMs, six question sets (SciQ 1000, LSAT-AR 230, SAT-EN 206, HaluEval-QA 2000, BoolQ, LifeEval 808): 88% confidence vs 79% accuracy on average, about 9 points. Chat models on LifeEval: score 52.8%, ECE 0.150, confidence 66.5%. Easy sets show underconfidence (97% accuracy, 92% confidence). The average gap hides regimes with accuracy from about 59% to 99%. The authors read it as regression to the mean.

### 6.6 Humans reading LLM confidence

Steyvers 2025 (b18, c17, c18): 301 Prolific participants, 40 questions each, 350 MMLU questions; model accuracy 55% (GPT-3.5) and 50% (PaLM2). Model AUC .751, .746, .781 (GPT-4o on short answer) vs human .589, .602, .592. Longer explanations raised human confidence without information (BF 25; BF = 0.23 for no benefit of length on AUC). Matched hedging narrowed the gap (BF > 100, 6.48, > 100 in Exp 2a, b, c). Where participants changed the LLM answer they scored 33% vs the LLM's 39%.

### 6.7 Suggestibility

Sicilia 2024 (d14; 3,900 questions): a wrong suggestion carrying a stated user confidence moved open models. Null-confidence wrong suggestion: accuracy bias 45.4 points (Llama 3.1 8B), 39.2 (Mistral 7B), 38.5 (Mixtral 8x22B), 21.0 (Qwen2 72B). User hedging: Mixtral 38.5 to 35.3, Qwen2 21.0 to 17.4. Small models did not respond. Platt scaling with user-behaviour terms (SyRoUP) raised Brier skill (BSS 7.3/4.9/7.3/13.1 vs plain Platt 6.5/4.7/2.6/2.0 at user correctness 0/25/75/100%). No frontier chat models; stripping not tested.

### 6.8 Forecasting

LLM crowd (12 models) Brier 0.20 vs 925 humans 0.19 on 31 binary questions, with an acquiescence bias toward yes. Giving the median human forecast improved GPT-4 and Claude 2 by 17-28% (c25). Halawi 2024: system Brier 0.179 vs crowd 0.149, accuracy 71.5% vs 77.0%; it hedges and is weak on extremes (c26).

### 6.9 Training-time fixes (outside a scaffold)

Fine-tuning on about 1000 graded examples (Kapoor 2024, b16), calibrated reward variants (Leng 2025, c20), CALM (Jin 2026; Sem-ECE mean over 4 backbones 0.0671 vs DPO 0.0846, d17), P(IK) heads (Kadavath, c05), conditioning on predicted correctness (Mielke 2022, c24, abstract only). A scaffold cannot train. It can only store outcomes and fit a mapping in code.

## 7. What our agent should take

Status marks follow SCHEMA.md: **[E]** established (two or more independent sources), **[S]** single source, **[C]** contested. Schema parts: G = guardrail, S = state, O = operator, memory = section 5 of the schema.

### Add now (established)

| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| N1 | Never gate stop, submit or escalate on the model's stated certainty. Stated numbers sit at 80-100% and rank right vs wrong near chance (GPT-4 AUROC 62.7%). Already in 4b; now backed by 3 independent AUROC sources. | G4 (restates 4b) | [E] | a22, b14, c09, b23, d07 (K15) |
| N2 | Every calibration or confidence test reports ECE, AUROC and a constant-confidence baseline together. ECE alone is gameable (ECE 0.064 by saying 100%). | G7 and section 6 logging | [E] | b14, c10, b15, b23 (K16) |
| N3 | Any confidence number that gates behaviour is computed in code from attempts and checks: share of fresh-context attempts that agree after code normalisation, plus check results. The model's own number may be logged, never used alone. | G5, S4, S7 | [E] | a23, c11, c12, c13, b14 (K17) |
| N4 | Agreement is a hint, not proof, and it is worst when most dangerous: when all samples agree and the answer is wrong. With no verifier, extra samples give no consistent gain. Any "all agree" case in a class with a measured shared-error rate needs an outside check (test, lookup, held-out example). | G3, G4, S4 | [E] | d03, d04, d05, d09 (K30) |
| N5 | Keep calibration per task class and per difficulty band, never one global offset. The sign of (confidence minus accuracy) flips between hard and easy. Before concluding "worse on hard items", compare with a noisy unbiased judge. | S0, memory (class record) | [E] | a08, b02, b06, b09, d12 (K03, K04) |
| N6 | Log overestimation (stated minus real accuracy) separately from range overprecision, per class. They do not move together. | section 6 logging, memory | [E] | b01, b08, b26 (K05) |
| N7 | The class record in memory is computed in code from graded outcomes, because pasting graded outcomes into the prompt did not fix model confidence. Memory stores hit rates and agreement-was-right counts, and S0 reads them. | memory, S0, S9 | [E] | a06, a09, d10 (K09) |
| N8 | When a probability over exclusive answers is needed, ask for several candidates with a probability each and normalise to sum 1 in code. Use it on hard classes; it did not help on easy ones. | G5, S7 | [E] for the hard-set gain | a20, a21, c08, b21 (K19) |
| N9 | For forecast-type outputs, aggregate several independent runs with a median rather than trusting one run. | S4 / S7 | [E] | c25, c26 (K26) |
| N10 | Wording of any user-facing certainty ("probably", "sure") must come from the code-computed score, not from the model's tone. Models state answers decisively even when samples split. | G5 (output rule) | [E] that models do not hedge faithfully; [S] that code-set wording helps readers | b20, c20, b18, c18 (K21, K23) |

### Test first (single-source, contested or human-only)

| # | Item | Schema part | Status | Evidence | Why not yet |
|---|---|---|---|---|---|
| T1 | A counter-case step (one strongest case against the chosen answer) before reading confidence, compared with no step and with a balanced pro/con step. | O1-style operator at S7 / S8 | [S] | a02, a03, d08 (K08, K32) | Human effect fragile (both group null); LLM test has no pro/con arm and no equal-token control; AUROC rose for 2 of 3 models only. Also must not break G1 (doubt only on a signal): trigger it from code on high agreement without a check. |
| T2 | Hybrid score: agreement plus mean stated confidence over majority-answer attempts. | S4, S7 | [S] | d01, d02 (K29) | Three open mid-size reasoning models; tokens matched per sample, not per answer. |
| T3 | Post-check confidence (after tests) vs pre-attempt confidence. | S0 vs S8 | [C] | b22, d07, d11 (K25) | Test results never separated from reflection; agent results null. |
| T4 | Hedge-language readout (judge scores free-text hedges) vs numeric confidence. | G5 | [S] | d15 (K27) | One benchmark; judge model needed; G5 says judges must be blind. |
| T5 | One-parameter Platt map fitted in code per class on logged outcomes. | memory, G5 | [S] | a15, b13, d17 (K12, K36) | Vision evidence only; transfer across classes not measured. |
| T6 | S1 input hygiene: strip user-stated certainty phrases into a marked block. | S1 | [S] | a27, d14 (K20, K34) | Evidence is 2023-2024 and open models; stripping untested. |
| T7 | Sample diversity by reframing the task (not personas) to lower shared errors. | S3, S4 | [S] | d06, d09 (K31) | Persona gain tiny; reframing moved cross-model agreement 87% to 44% but is not tested on AUROC. Note G4 says no persona voters on single-answer problems. |
| T8 | Reasoning-mode confidence: ask for confidence after a forced alternatives step. | S3, S8 | [S] | c21, c22 (K24) | Verbalized only; agent results show no reasoning advantage. |
| T9 | Representative-sampling check: measure the agent's gap on a random draw of its real task mix. | G7 | [C] | a12, a13, d12, d13 (K11, K33) | Original papers unopened; no random-draw LLM study. |

Counter-case and hybrid have the best gain-for-cost. Everything in "Test first" stays out of SCHEMA.md until its test passes (see UNKNOWNS.md).

## 8. Concrete tests on our bench

All arms use equal total tokens per item. Setup cost is counted (G7). Report ECE, AUROC and a constant baseline for every arm (N2). Use at least 300 items per class so AUROC has an interval of about +/-0.05 (Del used up to 100 bootstrap samples per question; Kaddour's 100 tasks gave CIs of +/-0.12, too wide).

| # | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| B1 | Our existing ARC, BRAINTEASER and word-puzzle items with known answers | (a) plain model stated 0-100 confidence; (b) agreement over N = 3, 5, 9 fresh-context attempts normalised in code; (c) hybrid (b)+(a) | AUROC of each score for "answer is right"; ECE | (b) AUROC above (a) by 0.10 or more on exact-answer classes, flat after N = 5 (c11, d02). Hybrid at N = 2-3 at least equal to (b) at N = 5. |
| B2 | Tasks where all attempts agree | Items with unanimous agreement; rate of wrong answers | Share wrong among unanimous; with and without an outside check (test, lookup) | A nonzero share (Ding: 48% at agreement of 0.8 or more on hard GPQA; our rate unknown). Outside check should catch most. |
| B3 | Items with a code check available | Arms: no critic; balanced pro/con critic; single strongest counter-case critic; all at equal tokens | ECE and AUROC after the step; overconfident-failure rate | Counter-case lowers ECE (Kaddour 0.42 to 0.30 for GPT); AUROC gain 0 to +0.09. Pro/con no better than none (Koriat). |
| B4 | Same items asked twice: before the attempt and after running checks | pre-attempt confidence; post-check confidence; post-reflection without checks | AUROC | Post-check at least pre; reflection alone near pre (d07). Tells us which part of the gain comes from tests. |
| B5 | A mix of 5 task classes, hard and easy | Per-class one-parameter Platt map fitted on class A, tested on class B with and without refit | ECE drop on held-out class; AUROC unchanged | Refit per class wins; transfer ECE drop is small. Decides if memory needs per-class maps. |
| B6 | Items with a user-stated certainty sentence (and a wrong suggestion) | raw; S1 stripped into a marked block; no sentence | accuracy; stated confidence | Raw loses accuracy (2024 open models 21-45 points; frontier unknown); stripping recovers part of it. |
| B7 | Numeric items with 90% ranges | ranges before and after in-context graded feedback; code-widened ranges | hit rate for 90% ranges | Hit rate below 90% before feedback (human 73.1%, 55.1% before feedback); code-fit widening restores it. |
| B8 | Items split into a random draw of the real task mix and a hand-picked hard set | the same agent on both | confidence minus accuracy per set | If gap is small on the random draw, selection explains part of it (Gigerenzer); if the same, it is a model trait. |
| B9 | Forecast-style items (if we have any) | single run; median of 5 runs | Brier | Median lowers Brier; yes-bias remains (c25). |
| B10 | Elicitation format on hard vs easy classes | top-1; top-4 normalised in code; hedge words scored by a judge | ECE and AUROC | Top-4 helps hard, not easy (K19). Hedges maybe +0.05 AUROC (d15 says ~10% on MMLU-Pro). |

## 9. What does not transfer, and why

- **Koriat's memory search.** The human story is that people recall supporting reasons first (18.3 vs 13.4 reasons). An LLM has no memory search. The same effect may still arise (training text, first-answer anchoring), but the evidence is the Kaddour agent result, not Koriat.
- **Human training and feedback.** The training did not transfer to new content in people. Humans learn over many sessions. A model in a scaffold does not update weights; graded outcomes in context did not change AUROC (d10).
- **Real money and incentives.** Models do not feel stakes. The risk-aversion effect in Barkan (acceptance cut to about 50%) came from a stated expected-utility rule, not from emotion.
- **Overplacement.** Our agent is not ranked against peers. Only overestimation and overprecision matter.
- **Age and lifespan effects** (Prims and Moore). No analogue.
- **Dunning-Kruger and the hard-easy effect as a trait.** Both can be statistical artifacts (b06, b09). Do not treat "worse on hard" as a defect in the model without a noisy-judge control.
- **Guo's temperature scaling.** It needs logits and a held-out labelled set. A closed API often has no logits; verbalized numbers can be Platt-mapped but evidence is vision-only.
- **Kadavath P(IK), Kapoor fine-tuning, Leng reward calibration, hidden-state probes.** All need weights or training. A scaffold cannot do them.
- **Calibration from bare token probabilities of RLHF chat models.** Evidence says poor (Tian) or fixable by T = 2.5 (Kadavath, early recipe). Not usable for API-only agents.
- **Weather-forecaster calibration.** It comes from daily binary outcomes. Our tasks give rare, class-specific feedback.
- **Debiasing training for confirmation bias** (Sellier). Human game-based training; no LLM equivalent shown. Instructions to "be careful" are already in 4b as not working.
- **Human explanation over-trust** (Steyvers). It concerns a person reading the output, not the agent's own reasoning. It matters only for the final user-facing text (N10).
- **2022-2023 model numbers** (GPT-3, gpt-3.5, Claude-1, LLaMA-2). Direction is probably the same; sizes may not be. The 2025-2026 evidence (Del, Ding, Kaddour, Barkan) is the better guide, with caveats on open mid-size models and 100-task samples.

## 10. Open questions

1. Does the Gigerenzer-Juslin claim (random sampling removes overconfidence) hold for LLMs? The 2026 study used benchmark sets, not random draws of a task mix.
2. Is post-check confidence better than pre-attempt confidence, and how much of any gain comes from test results versus reflection?
3. How many graded outcomes, and from which task classes, make stated confidence usable? Eight same-class outcomes did not (d10); no dose curve and no transfer test exist.
4. Does a counter-case step beat a balanced pro/con step at equal tokens? Koriat's human result says yes; no LLM arm tests it.
5. Does the agreement-versus-verbalized ordering for reasoning models hold on frontier closed models and on agent tasks?
6. How often do unanimous, fresh-context attempts agree on a wrong answer in our own classes, and does reframing the task reduce that more than personas do?
7. Does recalibration fitted on one class transfer to another for verbalized confidence?
8. Is a small set of ordinal levels better than 0-100? Tao tested free-text hedges scored by a judge; no study sweeps the number of levels.
9. How do certainty phrases in the user message affect current frontier chat models, and does stripping them help?
10. The founding numbers (Fischhoff 1977 original N and per-bin hit rates; Koriat 1980 tables; Gigerenzer 1991; Juslin 1994; Brenner 1996) are still second-hand. Any quotation of original human baselines needs those papers opened.
11. Whether any of this changes behaviour of an agent loop with tools: no study tests agreement-based confidence inside an agent with tool use.

## 11. Sources

[V] = opened this run (PDF, HTML or API text read). [M] = snippet, abstract or record only. Numbers from [M] lines are not used as established.

**Human founding and theory**
- [V] Koriat, Lichtenstein, Fischhoff (1980) Reasons for confidence. J Exp Psych: HLM 6(2). https://newiipdm.haifa.ac.il/wp-content/uploads/2015/05/1980-Koriat-Lichtenstein-Fischhoff-JEPHLM.pdf and https://doi.org/10.1037/0278-7393.6.2.107 (a01-a06, d16)
- [V] Plous (1993) The Psychology of Judgment and Decision Making, ch. 19. https://home.csulb.edu/~cwallis/382/certainty/chapter19.html (a07-a09; second-hand for Fischhoff, Lichtenstein, Oskamp, Russo, Murphy, Arkes)
- [V] Wikipedia: Overconfidence effect (secondary). https://en.wikipedia.org/wiki/Overconfidence_effect (a11)
- [M] Fischhoff, Slovic, Lichtenstein (1977) Knowing with certainty. https://typeset.io/pdf/knowing-with-certainty-the-appropriateness-of-extreme-228cyqafkl.pdf (a10, b05; fetch blocked)
- [M] Gigerenzer, Hoffrage, Kleinbolting (1991) Probabilistic mental models. https://hdl.handle.net/21.11116/0000-0000-B7D3-3 (a12)
- [M] Juslin (1994) Overconfidence as a consequence of informal experimenter-guided selection. https://api.openalex.org/works?search=overconfidence%20informal%20experimenter-guided%20selection%20almanac (a13)
- [M] Brenner et al. (1996), Erev et al. (1994): named in a13, a08, d13 only; not opened.
- [V] Moore and Healy (2008) The trouble with overconfidence. Psych Review 115. https://www.asc.ohio-state.edu/economics/healy/papers/Moore_Healy-TroubleWithOverconfidence.pdf (b01-b04; a14 record https://doi.org/10.2139/ssrn.1001821 is [M])
- [M] Moore and Healy Bayesian working paper. https://www.asc.ohio-state.edu/economics/healy/papers/Moore_Healy-Bayesian_Overconfidence_AoM.pdf (b25)
- [V] Merkle (2009) The disutility of the hard-easy effect. https://link.springer.com/content/pdf/10.3758/PBR.16.1.204.pdf (b06)
- [V] Prims and Moore (2017) Overconfidence over the lifespan. https://www.cambridge.org/core/services/aop-cambridge-core/content/view/37BB18649B2BA2120AEB4A89A2BE5057/S1930297500005222a.pdf/overconfidence-over-the-lifespan.pdf (b07)
- [V] Li, Hale, Moore (2025) Is overconfidence an individual difference? https://www.cambridge.org/core/services/aop-cambridge-core/content/view/1B39ECC1CDB332ADAADB5B051C057B47/S1930297525000117a.pdf/div-class-title-is-overconfidence-an-individual-difference-div.pdf (b08)
- [V] Magnus and Peresetsky (2022) A statistical explanation of the Dunning-Kruger effect. https://www.frontiersin.org/articles/10.3389/fpsyg.2022.840180/pdf (b09)
- [V] Sellier, Scopelliti, Morewedge (2019) Debiasing training transfers to the field. https://openaccess.city.ac.uk/id/eprint/22233/1/DebiasingTrainingTransfers_InPress.pdf (b10)
- [V] Krueger and Heck (2021) The end of overconfidence (book review). https://mambo.ucsc.edu/files/2021/01/FinalKruegerHeckOnMoore.pdf (b26)

**Models, 2017-2024**
- [V] Guo, Pleiss, Sun, Weinberger (2017) On calibration of modern neural networks. https://arxiv.org/abs/1706.04599 (a15, a16, b13)
- [V] Kadavath et al. (2022) Language models (mostly) know what they know. https://arxiv.org/abs/2207.05221 (a17, a18, b11, c01-c05)
- [V] Lin, Hilton, Evans (2022) Teaching models to express their uncertainty in words. https://arxiv.org/abs/2205.14334 (a19, b12, c06)
- [V] Tian et al. (2023) Just ask for calibration. https://arxiv.org/abs/2305.14975 (a20, a21, b15, c07, c08)
- [V] Xiong et al. (2024) Can LLMs express their uncertainty? https://arxiv.org/abs/2306.13063 (a22, a23, b14, c09-c11)
- [V] Kapoor et al. (2024) LLMs must be taught to know what they don't know. https://arxiv.org/abs/2406.08391 (a24, b16, c19)
- [V] Kuhn, Gal, Farquhar (2023) Semantic uncertainty. https://arxiv.org/abs/2302.09664 (b17, c12; exact values not extracted)
- [V] Wang et al. (2022) Self-consistency improves chain of thought. https://arxiv.org/abs/2203.11171 (c13)
- [V] Chen and Mueller (2023) Quantifying uncertainty in answers from any language model. https://arxiv.org/abs/2308.16175 (c14; tables not re-opened)
- [V] Zhou, Jurafsky, Hashimoto (2023) Navigating the grey area. https://arxiv.org/abs/2302.13439 (a27, b19, c15, c16)
- [V] Steyvers et al. (2025) What LLMs know and what people think they know. https://arxiv.org/abs/2401.13835 (a25, a26, b18, c17, c18)
- [V] Yona, Aharoni, Geva (2024) Can LLMs faithfully express intrinsic uncertainty? https://arxiv.org/abs/2405.16908 (b20)
- [V] Sicilia, Inan, Alikhani (2024) Accounting for sycophancy in language model uncertainty estimation. https://arxiv.org/abs/2410.14746 (d14)
- [M] Mielke et al. (2022) Reducing conversational agents' overconfidence. https://arxiv.org/abs/2012.14983 (c24)
- [V] Schoenegger et al. (2024) Wisdom of the silicon crowd. https://arxiv.org/abs/2402.19379 (c25)
- [V] Halawi et al. (2024) Approaching human-level forecasting. https://arxiv.org/abs/2402.18563 (c26)

**Models, 2025-2026**
- [V] Leng et al. (2025) Taming overconfidence in LLMs: reward calibration in RLHF. https://arxiv.org/abs/2410.09724 (c20)
- [V] Yoon et al. (2025) Reasoning models better express their confidence. https://arxiv.org/abs/2505.14489 (c21, c22)
- [V] Tao et al. (2025) Revisiting uncertainty estimation and calibration of LLMs. https://arxiv.org/abs/2505.23854 (c23 was [M]; d15 opened)
- [V] Stengel-Eskin et al. (2025) DINCO. https://arxiv.org/abs/2509.25532 (b21)
- [M] Fu et al. (2025) Deep Think with Confidence. https://arxiv.org/abs/2508.15260 (c27; abstract only)
- [V] Kale (2026) Future confidence distillation (preprint). https://arxiv.org/abs/2607.07626 (b22)
- [V] Del et al. (2026) How uncertainty estimation scales with sampling in reasoning models. https://arxiv.org/abs/2603.19118 (d01, d02)
- [V] Ding (2026) When LLMs agree, are they right? https://arxiv.org/abs/2607.08065 (d03, d04)
- [V] Denisov-Blanch et al. (2026) Consensus is not verification. https://arxiv.org/abs/2603.06612 (d05)
- [V] Upravitelev et al. (2026) Multiperspectivity as a resource for narrative similarity. https://arxiv.org/abs/2603.22103 (d06)
- [V] Kaddour et al. (2026) Agentic uncertainty reveals agentic overconfidence. https://arxiv.org/abs/2602.06948 (d07-d09)
- [V] Barkan, Black, Sourbut (2025) Do LLMs know what they are capable of? https://arxiv.org/abs/2512.24661 (d10, d11)
- [V] Michael, BenShushan, Bien, Moore (2026) Confidence calibration in LLMs. https://arxiv.org/abs/2605.23909 (d12, d13)
- [V] Jin et al. (2026) Beyond post-hoc temperature scaling. https://arxiv.org/abs/2608.07419 (d17; temperature claim asserted, not measured)

Search-snippet claims about arXiv 2608.18795 and 2607.10139 were not opened and are not used.
