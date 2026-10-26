# Conditions for valid intuition: deep document

*Subfield E04.05. Source files in this folder: evidence_a-d.jsonl (a01-a27, b01-b26, c01-c29, d01-d15), claims.jsonl (E04.05-K01 to K24), critique.md. Evidence ids below (a01, b12, ...) point to those files. Status marks follow SCHEMA.md: [E] established, [S] single-source, [C] contested.*

---

## 1. What it is

The question: when can a fast first answer be trusted, and when must the agent deliberate?

The anchor paper is Kahneman and Klein (2009), "Conditions for intuitive expertise: a failure to disagree." Two rival camps (heuristics-and-biases, naturalistic decision making) agreed on one rule. A fast judgment is trustworthy only if both hold:

1. **The environment is regular.** It offers cues that are valid, meaning they have a stable link to the outcome (a01, b01).
2. **The judge had a real chance to learn it.** That means long practice with feedback that is rapid and unequivocal (a05).

If either is missing, a correct intuition is luck (b01). The felt confidence of the answer does not tell you which case you are in (a03, b03).

Three bodies of work sit around this rule.

- **Clinical vs actuarial prediction (Meehl, Grove, Kuncel, Aegisdottir).** Where cues are weak and outcomes noisy, a fixed rule that combines the same cues beats the expert's holistic judgment or ties it.
- **Where expertise is real.** Static, repeatable tasks with feedback (chess, firefighting, some medicine) versus dynamic, behavioural tasks without feedback (stock picking, long-term political forecasts).
- **Machine versions of the same question.** Calibration of LLM confidence, early exit from sampling, routers between fast and slow modes, and whether extra thinking helps.

For our agent the question becomes a design question for the S0 gate and the class record: what evidence lets the program say "answer directly" versus "run the checked path"?

Scope note. Recognition-primed decision and mental simulation (Klein's own model) and chunking are covered by sibling subfields. Here we cover only the trust conditions.

**One important caveat up front.** The core rule comes from one position paper by two authors. No source gives a number for "adequate practice" or "rapid feedback". No source tests a track-record gate on an LLM agent. The shape of the gate is supported. Its thresholds are not (critique.md, weak spots).

---

## 2. History and theories in depth

### 2.1 The clinical vs statistical contest

- **Meehl (1954).** About 20 studies. Simple statistical rules matched or beat clinicians in almost every case, even though the rules used only part of the information. Meehl blamed base-rate neglect among other things (a20, b06). Early cases: Burgess 1928, where psychiatrists lost to a crude rule on recidivism, and Sarbin 1943, where a clerk matched trained clinicians (b26). Not opened by us; known second-hand.
- **Goldberg (1970), bootstrapping.** 29 clinicians judged 861 patients as psychotic or neurotic from 11 MMPI scales. A regression model fitted to each clinician's own calls was almost always more accurate than the clinician (a09, b05). The model keeps the judge's weights and drops the judge's inconsistency. That points to noise, not missing insight.
- **Karelaia and Hogarth (2008).** Meta-analysis that ties the formula edge mainly to inconsistency. Unique knowledge beyond the linear model (lens model term C) is near zero (a14). Only second-hand.
- **Grove, Zald, Lebow, Snitz and Nelson (2000).** 136 studies. Mechanical better in 63, tie in 65, clinical better in 8 (a10, as read by Kahneman and Klein; we did not open the paper). Mechanical prediction was about 10 percentage points more accurate. Clinicians were substantially better in only 6 to 16% of studies. The advantage held across tasks, judge types and experience levels, and clinicians did worse when interview data were used (b12, abstract only).
- **Aegisdottir et al. (2006).** An independent second large meta-analysis. 67 studies, 92 effects. Strict set (cross-validated formulas, outliers removed): 41 studies, 48 effects, d+ = .12. Of 48 effects: 25 (52%) favour statistics, 18 (38%) no difference, 5 (10%) favour clinicians (a15, b10). The sign is a coding convention: a15 writes -.12, b10 writes .12. Use the size.
- **Kuncel, Klieger, Connelly and Ones (2013).** Work and school selection. Mechanical beat clinical on all criteria (section 3). The authors reject three defences of clinical judgment: changing jobs, small samples, and "experts set the weights" (b09).
- **Kahneman, Sibony and Sunstein (2021), Noise.** Judgments on identical cases vary between people and within a person across occasions. Rules are noise-free (c27, snippets only).

### 2.2 Where intuition is valid: the Kahneman and Klein synthesis

Klein's side: experts in fireground, neonatal care, weather and engineering build real recognition skill. Kahneman's side: many professionals (stock pickers, clinicians, personnel selectors) feel the same conviction without the skill. They met in the middle (a01, b06).

- **Validity belongs to the environment.** It means a stable causal or statistical structure, not absence of uncertainty. Poker, bridge and warfare are high-validity but uncertain, because skill raises the odds (a02, b04).
- **Fairly high validity:** fireground collapse cues, neonatal sepsis cues, chess. **Effectively zero validity:** individual stock prices, long-term political forecasts (a02).
- **Learning conditions.** Prolonged practice. Feedback rapid and unequivocal. Finance, psychotherapy and intelligence analysis have ample short-term feedback but delayed, sparse, ambiguous long-term feedback, and that breeds overconfidence (a05).
- **Learning scale.** Chess masters hold about 50,000 to 100,000 patterns after about 10,000 hours (a01).
- **No usable feeling.** "There is no subjective marker that distinguishes correct intuitions from intuitions that are produced by highly imperfect heuristics" (a03). Confidence tracks how consistent the story is, not how good the evidence is.
- **The safe test** of any judgment is the validity of the environment plus the judge's learning history (a04, b03).
- **Heuristic intuition when skill is absent.** Bat-and-ball: about 50% intuitive errors at MIT, Princeton and Harvard, about 90% at less selective schools. Anchoring: expected gap of $35,000 between $100,000 and $30,000 anchors (a08).
- **Fractionated expertise.** Nurses, physicians and auditors appear on both Shanteau's good and poor performance lists. Auditors do well on hard data, worse on fraud cues. Forecasters do better on temperature and rain than on hail (a06, b02). "The rule, not an exception."
- **Anomaly detection.** The mark of authentic expertise is noticing that a case fits no familiar category and switching to deliberate search (a07, b07). This is where Klein and Kahneman differ in emphasis. Klein thinks experts overreach less. Kahneman sees fractionation producing the illusion of validity. K&K give no data on how well anomaly detection works.
- **Algorithm conditions.** Adequate variable list, reliable measurable criterion, a body of similar cases, a cost-benefit that justifies building it, low chance of changed conditions. Humans must supervise because of automation bias (a11).
- **Premortem.** The one semi-formal doubt move both accept (a12). No outcome data in the paper.

### 2.3 Hogarth: kind and wicked environments

Kind environments give swift, accurate, cheap feedback. Wicked ones give misleading feedback. People treat wicked environments as kind and overvalue experience (a17). Example: a physician palpated patients' tongues to confirm typhoid hunches and spread the infection, so his hunches came true (a18, b04). A review adds a 2 by 2: valid and confident, valid and unsure, invalid and confident (dangerous), invalid and unsure (fitting scepticism). The gate must be two-sided (a17). Known to us only via a book review and K&K.

### 2.4 Forecasting tournaments: validity that can be manufactured

Tetlock (2005): after 15 years, experts were no better than newspaper readers on long-range political forecasts (b04). The Good Judgment Project (Tetlock, Mellers, Rohrbaugh and Chen 2014) showed that with scoring and fast feedback, forecasters can be selected, trained and aggregated to do well on short-term questions (a21, b15). The later 2025 reanalysis questions the team and training effects (d11). See section 5.

### 2.5 Machine side

- **Kadavath et al. (2022).** Large models are well calibrated on multiple choice in the right format. P(True) improves with several own samples. P(IK), trained on TriviaQA, works in distribution and degrades on new tasks (a22, b22, c03).
- **Calibration of verbal confidence** (Tian 2023, Xiong 2024, Kapoor 2024). See sections 3 and 5.
- **Self-consistency (Wang 2023).** Agreement among samples correlates with accuracy (a26, b23).
- **Deliberation can hurt.** Liu 2024 (implicit learning), Lacombe 2025 (over-reasoning), Gema 2025 (inverse scaling), Shojaee 2025 (complexity regimes).
- **Routers and early exit.** DynamicMind, ReASC, CGES, mixture-of-thoughts cascades (c16 to c22).

---

## 3. Core findings with exact numbers

Status uses the claims.jsonl labels. "Human-only" means no LLM test. "Older models" means 2022 to 2024 models only.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Skilled intuition needs a regular environment and learning with feedback | Two conditions. Chess: about 10,000 hours, 50,000-100,000 patterns. No threshold for "adequate" | Kahneman and Klein 2009 (a01, a05, b01) | [E] K01 (conceptual; human-only) |
| Confidence does not mark valid intuition | Cites Einhorn and Hogarth 1978, Griffin and Tversky 1992, Arkes 2001. LLM: Tian GPT-4 TruthfulQA AUC .632; ChatGPT .492 | K&K 2009 (a03, b03); Tian 2023 (c05); Steyvers 2024 (c01) | [E] K02 |
| Mechanical beats clinical in selection (meta-analysis) | 25 samples in 17 studies. Job performance r .44 vs .28; advancement .42 vs .36; training .31 vs .16; GPA .58 vs .48; other academic .47 vs .46. About 2,263 mechanical and 2,027 clinical worker predictions. About 25% fewer correct hires at selection ratio .30 | Kuncel et al. 2013 (a13, b08, b09) | [E] K03 (human-only) |
| Mechanical vs clinical across 136 studies | Mechanical better 63, tie 65, clinical better 8. d about .12. Clinical clearly better in 6-16% | Grove 2000 via K&K (a10); abstract (b12) | [E] K03 (second-hand) |
| Formula edge in mental health is small | 67 studies, 92 effects; strict set 41 studies, 48 effects, d+ .12 (r+ .06), CI -.14 to -.09; 52% statistical, 38% tie, 10% clinical; about 13% accuracy gain; 99 null studies needed to cancel | Aegisdottir 2006 (a15, b10) | [E] K04 |
| Moderators of the formula edge | Same-setting data d+ .14 vs other-setting .06 (QB(1) 6.96, p<.01). Linear formulas .15, logical rules .03 (CI includes 0). Expertness not significant. Task type QB 12.42 | Aegisdottir 2006 (a16, b11) | [C] K06 (small cells; author-flagged trends) |
| Formulas win by consistency, not insight | Lens model: C near 0. Goldberg: 29 clinicians, 861 patients, 11 scales; bootstrap models beat the judges | Kuncel 2013 (a14); Goldberg via K&K (a09, b05) | [S] K05 |
| Expertise is fractionated | Shanteau 1992: 11 domains with expertise vs 7 without; three professions on both lists | K&K 2009 (a06, a19, b02) | [S] K07 (traced to K&K) |
| Slow diagnosis was not more accurate | 113 residents analysed. Correct 115 s vs wrong 129 s, t(112)=4.51, d=0.37. Confidence correct vs wrong d=0.89. Bias induction failed | BMC Med Educ 2021 (b18) | [S] K09 |
| Forecasting skill can be raised with scoring and feedback | Best aggregate right side of 50/50 on 86.2% of daily forecasts; beat control mean by 60%, other teams by 40%. Recruitment about 10%, training about 10%, teams about 10%, extremizing about 35% | Tetlock et al. 2014 (a21, b15) | [C] K10 |
| 2025 reanalysis of the tournament | Teaming and training effects "eliminated, reduced, and in some cases even reversed" after controls | Psych Science 2025 (d11), abstract only | [C] K10 |
| Verbal confidence: calibrated on average, weak per item | Tian: GPT-4 TruthfulQA ECE .445 to .082, AUC .632; ChatGPT .451 to .125, AUC .492; TriviaQA GPT-4 .078 to .024, AUC .937. Xiong: ECE above .377 for GPT-3, GPT-3.5, Vicuna; GPT-4 AUROC 62.7% | Tian 2023 (c04, c05); Xiong 2024 (a24) | [C] K11 |
| Sampling agreement discriminates weakly on MMLU | "good calibration, discriminative performance very weak"; trained classifier better | Kapoor 2024 (d02) | [C] K11, K15 |
| Hard-easy effect in 11 models; reasoning models better calibrated | Mean confidence 88% vs accuracy 79%. LifeEval hardest 34.2% vs 9.6%; easiest 80.5% vs 92.0%. ECE .037 (5 reasoning) vs .150 (6 chat) | Michael 2026 (c06, c07), summary page | [S] K12 |
| More thinking tokens can hurt calibration | Gemini 2.5 Flash: 41.7% at 0 tokens, peak 45.0% at 64-192, 35.7% at 768, 41.7% at 24,576. Overconfidence +6% to +21.3% (ClimateX); +15.6% to +35.6% (IARC) | Lacombe 2025 (c08); Gema 2025 (b25) | [C] K13 |
| Search beats pure reasoning when information is missing | Gemini 2.5 Pro with search 89.3% vs 48.7% reasoning; Flash with search 88.3% | Lacombe 2025 (c09) | [S] |
| Self-review without an outside signal does not help | GPT-4 GSM8K 95.5 to 89.0 after round 2 (5 calls); with oracle labels 95.5 to 97.5. GPT-3.5 GSM8K 75.9 to 84.3 with oracle; 74.7 without | Huang 2023 (b24) | [S] K14 (agrees with G2 and 4b) |
| Sample agreement as early-exit gate | ReASC GSM8K Gemma-3-4B: SC k=16 92.12% at 32.67 TF; ReASC 92.04% at 9.45 TF (-71.1%). Stage-1 accepted 51.18% at 97.78% (offline), 33.28% at 98.41% (online). CGES: 4.90 vs 16.00 calls (-69.4%), 73.55 vs 73.61 | Kim 2026 (c21); Aghazadeh 2025 (c22) | [E] K15 (math-heavy; Kapoor is counter-evidence) |
| CoT hurts where verbal thought hurts people | Artificial grammar absolute drop: o1-preview 36.3, GPT-4o 23.1, Claude 3 Opus 8.0, Claude 3.5 Sonnet -1.8, Gemini 1.5 Pro 6.05, Llama 3.1 70B 8.8, 8B 1.98. Face recognition: GPT-4o 12.8, Claude 3 Opus 14.4, Gemini 11.4, Claude 3.5 Sonnet 3.0, InternVL2 2.0 (ns). Exceptions learning: GPT-4o 2.9 to 12.5 rounds | Liu 2024 (c11, c12) | [E] K16 |
| CoT helps mainly math and symbolic | 100+ papers plus 20 datasets, 14 models (abstract only) | Sprague 2024 (c10) | [E] K16 |
| Complexity regimes | Low: non-thinking wins. Medium: thinking wins. High: both fail. Contested by rebuttals not opened | Shojaee 2025 (d09, d10) | [C] K16, K22 |
| Router transfer is poor, slow mode rarely needed | Slow mode helped 3.11% of items (+53.84% on those, +277.30 tokens). Normal over fast 14.13%. Fast matched normal on 6% | DynamicMind 2025 (c17) | [S] K17 (7-8B, own data) |
| Learned correctness estimate sample size | About 1000 graded examples beat baselines; gains flatten after about 5000 | Kapoor 2024 (d01) | [S] K19 (fine-tuned 7B, MMLU) |
| Within-model noise at temperature 0 | Up to 15% accuracy change across 10 runs; best-worst gap up to 70%; no model repeatable on all tasks | Atil 2025 (d07, d08) | [S] K20 (2024-era models) |
| Demonstrations teach format, not the label map | Random labels cost 0-5% absolute (1.7% multi-choice, 2.6% classification), 12 models, k=16. Out-of-distribution inputs cost 3-16%. Wrong label space 5-16% | Min 2022 (d05, d15) | [C] K21 (older models) |
| Label noise hurts generation | 20/40/60% noise lowers exact match; K=8 worse than K=2 under noise | Gao 2024 (d06) | [C] K21 |
| Users over-trust LLM answers | N=301. ECE human default .264 vs model .104 (GPT-3.5). AUC human .589 vs model .751. Long explanation AUC .54 vs .57 | Steyvers 2024 (c01, c02) | [S] K18 |
| Out-of-class detection | Refusal skill transfers (R-Tuning); estimator transfers across formats (Kapoor); surveys say abstention generalises poorly out of distribution | d03, d13, d14 | [C] K24 |
| LLM forecaster vs crowd | 914 questions. Brier: system .179, crowd .149, aggregate .146, random .250. Where crowd uncertain (.3-.7): .238 vs .240 | Halawi 2024 (c23) | [S] |

---

## 4. Mechanisms and models

This section is written so an engineer can build each piece.

### 4.1 The two-condition rule as a data structure (the class record)

Keep one record per task class, in code (never in the prompt: d05 and d15 show that in-context examples mostly teach format and label space, not the input-to-label relation).

```
ClassRecord {
  class_id
  n_graded            # cases with an independent grade
  n_first_correct     # first answer matched the grade
  grade_independent   # was the grade free of the agent's own action? (wicked-feedback guard, a18, b04)
  grade_latency       # time or steps from answer to grade (K&K "rapid")
  grade_ambiguity     # share of cases graded "unclear"
  samples_agree_rate  # share of items where k fast samples agreed
  agree_when_right, agree_when_wrong
  run_noise           # disagreement on identical items (d07)
  centroid / exemplar set for typicality (a07, b07)
  model_version       # the record is valid only for this model (c13, c17)
}
```

Class definition matters. Fractionation (a06) means the unit must be narrow enough that cue validity is similar inside it. Start with the bench's natural item types. Split a class if its hit rate varies across sub-types.

### 4.2 Validity as "does effort or skill raise the success rate"

K&K define validity by structure, not by determinism (a02). For the agent, the checkable version is empirical: within a class, is the first-answer hit rate above the base rate, and does the deliberate arm beat the fast arm? If the fast arm already equals the checked arm, the class is trustable. If both are at the base rate, the class has no learnable cues and the right action is to use a mechanical rule or prior (see 4.5).

### 4.3 The trust test, four parts (our synthesis in a27, marked as inference)

Answer fast and stop only if all four hold. Otherwise deliberate or run a code check.

1. The class has enough graded cases (Wilson lower bound on first-answer hit rate above a floor).
2. Grading was fast and independent of the agent.
3. The class is regular: first-answer accuracy is above the base rate and stable across recent windows.
4. The current input is typical of the class (novelty check), and k fast samples agree.

No source supplies the thresholds. They must be fitted on our bench. The shape is supported by K&K, Kadavath (self-knowledge works inside a trained class) and ReASC (a threshold fitted on a validation record).

### 4.4 Early-exit ladder (ReASC and CGES style)

```
answer = fast_sample()
if class_record.trusted and typical(item) and conf_signal(answer) >= tau_class:
    return answer                      # stage 1: about half of items, about 98% accurate in ReASC
samples = draw(k-1)                    # stage 2
if agreement(samples) high: return majority
else: escalate to checked path with an outside check (G2, G3)
```

ReASC fits tau on labelled validation data or a Gaussian mixture (c21). CGES keeps a Bayesian posterior over candidate answers and stops when the top answer passes a threshold (c22). Both are code-side, matching G5. Warning from Kapoor: sampling agreement discriminated weakly on open MMLU (d02), and same-model samples share errors (G4). Treat agreement as a hint and test it per class.

### 4.5 Mechanical combination (lens model)

Lens model terms (a14): Rs is the consistency of the judge's strategy, G is the match to the best linear model, C is unmodelled knowledge (near zero in human studies). When C is about 0 and cues are weak, a fixed combination beats the judge.

Agent version: the model rates each cue on a fixed rubric (collecting information is where experts are good, a13). Code adds the ratings with unit or fitted weights and decides (b13: unit-weight and category-sum rules need no large data and are auditable). Use only for prediction-style classes with fixed cues and a measurable outcome. Where C is large (nonlinear pattern skill, as in chess), the rule is wrong (a14, limits).

Two further cheap moves from the same literature:
- **Base-rate injection.** Giving clinicians base rates moved them close to formula accuracy (a16, trend only). Code supplies the class prior before the answer.
- **Bootstrapping the agent.** Fit a simple rule to the agent's own past valid calls (b05). Untested for LLMs.

### 4.6 Noise measurement

Run identical items several times. Log answer-level agreement per class (d07 used TARa@10). A class with low run-to-run agreement has a noisy first answer. Averaging by code removes noise but not bias (a09, b05). At temperature 0 noise still exists (up to 15% accuracy swing, d07), so one run is one draw.

### 4.7 Novelty (anomaly) check

Embed or fingerprint the item. Compare with stored graded cases of the class. If distance exceeds a class radius, strip fast-answer rights. Two sources say this works for people and models in part (a07; Kadavath P(IK) generalises partly, d03 transfer across formats). Surveys warn abstention generalises poorly out of distribution and over-refusal is unmeasured (d14). So set the alarm threshold by cost in the harness, not by the model.

### 4.8 Mode choice by task type

Evidence that the best mode depends on class: CoT hurts implicit pattern learning and face recognition (c11, c12), helps math and symbolic tasks (c10), non-thinking wins on low-complexity puzzles (d09), S1-aligned models win on commonsense and S2-aligned on arithmetic (c14: CSQA 72.81 vs 71.42; AddSub 89.87 vs 82.47). A training-free mixer based on token entropy beat the base on 12 of 13 benchmarks (c15) but needs logprobs. Record direct and checked accuracy per class and let the record pick the mode (K16, K22).

### 4.9 Feedback quality

A class earns "trusted" only with feedback that is fast, independent and unambiguous (a05, a18). Delayed or ambiguous grades should freeze the class at "deliberate". Delay and ambiguity are untested for LLMs (d06 limits).

---

## 5. What holds up

### 5.1 Replications and meta-analyses

- **Formula beats or ties holistic judgment.** Three meta-analyses agree in direction: Grove 2000, Aegisdottir 2006, Kuncel 2013. Different datasets and criteria. The size differs: d about .12 in mental health, r .44 vs .28 for job performance. This is the strongest evidence in the subfield, but it is all human data. [E]
- **Confidence is not a validity marker.** Human sources (K&K's cited work), LLM sources (Tian, Xiong, Kapoor, Steyvers, Michael). Metric and model differences explain the apparent clash on verbal confidence. [E]
- **CoT hurts where deliberation hurts people.** Liu 2024 across seven models, consistent in sign except Claude 3.5 Sonnet (-1.8 on grammar). [E] but effect size varies a lot by model.
- **Early exit by agreement.** ReASC, CGES and mixture-of-thoughts cascades (about 40% of GPT-4 cost, c20) agree on large savings with equal accuracy. Math-heavy. [E]

### 5.2 Failures, boundary conditions and contests

- **Familiarity did not help clinicians.** They did worse on same-setting data (d+ .14 vs .06). This clashes with the K&K idea that practice builds validity, but those studies had no feedback, which fits K&K. Nobody tested it directly. Cells are small (critique.md).
- **Kuncel's edge is shrinkage-sensitive.** With the strictest new-sample shrinkage the mechanical edge vanished (but did not reverse) on two criteria. No range-restriction correction (b08).
- **Aegisdottir needed outlier removal.** 12 of 60 effects (20%) were dropped for homogeneity. With outliers kept, heterogeneity was significant (b10).
- **Training and teaming in forecasting.** The 2014 gains (about 10% each) were challenged by the 2025 item-response reanalysis (abstract only, d11). The abstract does not address persistence of top forecasters. The small replication (Katsagounos 2021) supports identification of top forecasters (top 25% bin) but weak evidence for training (b17). Contested.
- **Verbal calibration vs discrimination.** Good ECE, weak AUC on hard sets (c04, c05). A 50% guesser can have perfect ECE (a23).
- **Reasoning models vs thinking budget.** Michael 2026: reasoning models much better calibrated (ECE .037 vs .150). Lacombe 2025 and Gema 2025: more tokens can worsen calibration. Different manipulations (model type vs budget on one model). Unresolved.
- **Apple puzzle study.** Complexity regimes are contested by rebuttals (output limits, unsolvable instances) that we did not open (d09).
- **Speed and diagnosis.** Faster diagnoses were more often right, but the bias induction failed, so neither "slowing down helps" nor "hurts" was tested; item difficulty may explain the speed gap (b18).
- **Blip of knowledge.** Brief exposure to knowledge gave the worst accuracy and most overconfidence in experiment 1, but experiment 2 did not replicate the accuracy gap (b20; lay participants).
- **Fingerprint examiners.** Higher skill goes with more conservative same-source thresholds, not with exclusion thresholds (b21; observational). Skill shows up as calibrated thresholds.

### 5.3 Interventions that worked

- Mechanical combination of cues in selection (a13).
- Scored feedback loops and aggregation in forecasting: aggregation tuning about 35% over the unweighted mean (a21). Contested for training and teaming.
- Early exit on agreement and calibrated confidence (c21, c22).
- Giving search evidence where information was missing: 89.3% vs 48.7% (c09).
- External score changes human reliance when it is informative, not when random (N=181, d04).
- Matching the explanation wording to the model's real confidence narrows the user trust gap (c01).
- Base rates given to clinicians (a16, trend).

### 5.4 Interventions that did not work

- Premortem: no outcome data (a12).
- Self-review without outside signal: GPT-4 GSM8K 95.5 to 89.0 (b24).
- "Be careful" prompts for judgment biases: backfire in open-weight models (c26, abstract only).
- Long explanations: raise confidence, no gain in discrimination (c02).
- Random or noisy in-context labels: classification barely changes (d05), which means in-context outcomes also do not teach much. Generation is hurt (d06).
- Routers trained on one model: lose accuracy on another (c17).

---

## 6. Language models

### 6.1 Does the model know when it is right?

- **2022 (Kadavath).** Large models are well calibrated on lettered multiple choice, and calibration improves with size and few-shot. P(IK) trained on TriviaQA is poor out of distribution and mostly underconfident. RLHF policies look miscalibrated until temperature is adjusted. A "none of the above" option reduces accuracy and calibration (a22, b22).
- **2023 (Tian).** Verbalised confidence beats token probability for RLHF models. GPT-4 TruthfulQA ECE .445 to .082. But discrimination there is AUC .632 for GPT-4, .492 ChatGPT, .350 Claude 1, .446 Claude 2. On TriviaQA GPT-4 AUC is .937 (c04, c05). So confidence is informative on a regular knowledge class and near useless on an adversarial one. That is the K&K pattern in numbers.
- **2024 (Xiong).** Verbalised confidence clusters at 80 to 100% in multiples of 5. GPT-4 average AUROC only 62.7%. Sampling several answers and averaging confidence helps (a24).
- **2024 (Kapoor).** On MMLU, sampling agreement had good calibration but very weak discrimination. Verbal elicitation had similar discrimination to weaker fine-tuned methods but poor calibration. A trained correctness classifier was better on both. About 1000 graded examples were enough to beat baselines; gains flatten after about 5000 (d01, d02). It transferred across subjects, formats and other models' answers (d03).
- **2026 (Michael).** Eleven models. Hard-easy effect like humans. Reasoning models: ECE .037, confidence-correctness correlation .94. Chat models: ECE .150, correlation .48. Chat models round to multiples of 5% in 91.4% of cases vs 61.1% for reasoning (c06, c07). Summary page only.
- **Humans reading LLMs (Steyvers).** Users over-trust. ECE human default .264 vs model .104 (GPT-3.5). Adjusting explanation wording to the model's real confidence cut the gap (.150). Long explanations raise confidence with no better discrimination (AUC .54 vs .57) (c01, c02).

What changed it: model class (reasoning vs chat) and RLHF with verbal elicitation. By how much: ECE gains of 3x to 6x on average, but discrimination changes little on hard sets.

### 6.2 Does extra thinking help?

- Helps on math and symbolic classes (c10). Hurts on implicit pattern learning and face recognition (c11, c12). o1-preview lost 36.3 points on artificial grammar.
- Over-reasoning: Gemini 2.5 Flash accuracy peaked at 45.0% with 64-192 tokens, fell to 35.7% at 768, returned to 41.7% at 24,576. Overconfidence grew to +21.3 points (c08).
- Inverse scaling in test-time compute on constructed tasks: distraction (Claude models), framing overfit (o-series), drift to spurious features (b25).
- Puzzle regimes: non-thinking wins at low complexity, thinking at medium, both fail at high (d09). Near collapse the models reduced effort with budget left (d10).
- Self-correction needs an outside signal (b24).
- Reasoning text is not evidence. In a parole prediction task GPT-5's stated reasons did not explain its predictions (c24, abstract only).

### 6.3 Early exit and routing

- ReASC: about half of items accepted at one sample with 97.78 to 98.41% accuracy, saving 71.1% compute against SC k=16 (c21). Against ASC the saving is smaller (ASC already -62.5%, critique).
- CGES: -69.4% calls, same accuracy (c22).
- Mixture of thoughts: GPT-4-level performance at about 40% of the cost (c20).
- DynamicMind: slow mode helped only 3.11% of items; a router trained on one LLM lost accuracy on another (c17).
- TH2T: GSM8K reasoning length cut 58 to 74% with accuracy up. The hardest class (AIME 32B) lost accuracy 60.0 to 56.7 (c18).

### 6.4 Intuition error profile across versions

GPT-3 showed human-like intuitive errors on CRT and semantic illusions. ChatGPT and GPT-4 avoided them (c13, abstract only). So the error profile changes with model version, and the class record must be rebuilt when the model changes (c13, c17).

### 6.5 LLM vs actuarial

Halawi 2024: a retrieval forecaster had Brier .179 vs crowd .149; the weighted aggregate .146 was best. Where the crowd was uncertain the system matched it (.238 vs .240) (c23). Copus (2025, unreviewed, versions disagree) reports GPT-5 beating a 91-variable actuarial baseline on parole rearrest (c24). Not enough to say LLMs beat formulas.

### 6.6 Noise

Atil 2025: at temperature 0, five 2024-era LLMs differed across 10 runs by up to 15% accuracy, best-to-worst gap up to 70%. Navigation answers repeatable, college math and professional accounting scattered (d07, d08).

### 6.7 What is missing

No source tests a task-class track-record gate on a frontier LLM agent. No source compares an outcome-based class hit rate with verbal confidence and sample agreement at equal tokens (critique.md gap 2).

---

## 7. What our agent should take

Status marks: [E] established, [S] single-source, [C] contested. Schema part: G guardrail, S state, O operator, memory.

### Add now (established)

1. **Do not use stated confidence, fluency or explanation length as the trust test.** Schema: G (extends 4b "verbal confidence to stop" and G5 length-normalising); S0. [E] K02. Evidence: a03, b03, c01, c02, c05, a24, d02. Action: S0 and the early-exit rule must never read the model's own certainty as sufficient; use it only as a weak extra input.
2. **The trust unit is the task class and the record lives in code.** Schema: S0 (class record), memory (already planned as "Class record"). Status: the two-condition rule is [E] K01; narrow-class fractionation is [S] K07. Evidence: a01, a04, a05, a06, b01, b02. Action: S0 reads the class record; S9 updates it. The record must carry n_graded, hit rate, grade independence and latency.
3. **Hold fast answers back unless the class has learning history.** A class with no graded cases, or only delayed, ambiguous or agent-influenced grades, defaults to the checked path. Schema: S0, mode choice. [E] K01. Evidence: a05, a18, b04, a17.
4. **Chain-of-thought is not the default for recognition-type classes.** Mode per class from the record. Schema: S0 mode, G11 (already "think briefly"). [E] K16. Evidence: c10, c11, c12, c14.
5. **Sample agreement as early-exit gate, as a hint.** Accept one answer when class record is good and samples agree; otherwise escalate. Schema: S0, S3/S7, with G4 as limit. [E] K15 (math-heavy; counter-evidence d02). Evidence: a26, b23, c20, c21, c22.
6. **Mechanical combination beats holistic combination for prediction classes with fixed cues.** The model rates cues, code combines. Schema: S7 (select) and G5 (code selects). [E] K03 for the human data; for an LLM agent it is an argument, not shown. Evidence: a09, a10, a13, a15, b08, b12. Do not assume a large edge: [E] K04 says it is small in mental health (d+ .12).
7. **Self-review without an outside signal does not rescue a distrusted first answer.** Escalation needs a check, tool or new evidence. Schema: G2 (already). [S] K14 here, [E] in SCHEMA 4b from other briefs. Evidence: b24.

### Test first

| # | Item | Schema part | Status | Evidence ids |
|---|---|---|---|---|
| T1 | S0 gate from class record: Wilson lower bound on first-answer hit rate, independence flag, then fast vs checked | S0, memory | [S] K19 (sample size), K01 | a27, d01, c21 |
| T2 | Hit rate vs verbalised confidence vs sample agreement as predictors of first-answer correctness (AUROC per class) | S0 | [C] K02, K11 | c04, c05, a24, d02 |
| T3 | Agreement-based early-exit ladder vs fixed N samples | S0, S3, S7 | [E] on math, untested elsewhere K15 | c21, c22, d02 |
| T4 | Novelty check before fast answer; out-of-class escape rate and false alarms | S0, O (to S6 or checked path) | [S] K08, [C] K24 | a07, d03, d13, d14 |
| T5 | Base-rate injection: give the class prior before the answer | S1 input, memory | [S], trend only | a16, c25 |
| T6 | LLM rates cues, code combines (fixed rubric) vs holistic answer | S7, G5 | [S] K03/K05 for LLMs | a13, b13 |
| T7 | Noise per class: 5 identical runs, agreement vs first-answer hit rate | S0, G | [S] K20 | d07, d08 |
| T8 | Harness counter vs in-context history of past graded cases, clean, noisy, delayed | memory | [C] K21 | d05, d06, d15 |
| T9 | Thinking budget sweep per class | S0, G11 | [C] K13 | c08, b25, d09 |
| T10 | Scored forecast loop raises class trust vs unscored loop | memory, S9 | [C] K10 | a21, d11 |
| T11 | Early validity proxy from 3-5 graded cases | S0 | [S] K23 | d12 |
| T12 | Recheck with vs without outside check | S5, G2 | [S] K14 | b24 |

Rule: nothing in "Test first" goes into SCHEMA.md until its test passes (see UNKNOWNS.md).

---

## 8. Concrete tests on our bench

All tests compare arms at equal total tokens (setup cost counted, G7). Report per task class, not pooled.

| Test | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| B1. Gate vs always-deliberate | Mixed bench with kind classes (exact-answer puzzles with a checker) and wicked classes (items with noisy or no feedback, e.g. judgment questions graded late) | (a) always checked path, (b) always direct, (c) class-record gate | Accuracy at equal tokens; share of items answered fast | Gate matches (a) accuracy on wicked classes and (b) tokens on kind classes. Expect a win of 10 to 30% tokens at equal accuracy (ReASC-like), smaller on wicked classes |
| B2. Trust signal comparison | Same items, 20+ graded per class | Predict first-answer correctness from: verbal confidence, sample agreement (k=5), class hit rate, novelty distance, combination | AUROC and ECE per class | Class hit rate and agreement beat verbal confidence on low-validity classes (TruthfulQA-like: Tian AUC .49 to .63). Expect little difference on knowledge-retrieval classes (AUC .93 for GPT-4 TriviaQA) |
| B3. Sample-size sweep | One class, 500 graded items | Gate built from n = 10, 30, 100, 300, 1000 graded cases | Accuracy at equal tokens; miss rate (fast but wrong) | Gate beats always-deliberate from about 30 to 100 cases on kind classes; unsafe below 10 |
| B4. Early-exit ladder | Math and non-math exact-answer items | (a) fixed N=5 votes, (b) ladder: 1 answer if trusted and typical, else more samples, (c) ladder with agreement-only trust | Accuracy at equal tokens | Ladder saves 40 to 70% tokens on math (ReASC -71.1%); less outside math; agreement-only worse than record plus agreement (Kapoor warning) |
| B5. Novelty alarm | In-class items plus injected out-of-class items (shifted format, new sub-type) at 10%, 30% | (a) no alarm, (b) distance alarm, (c) distance alarm plus agreement | Detection rate, false-alarm rate, tokens lost to false alarms, accuracy | Detection above 50% at under 15% false alarms would justify keeping it. Unknown: no prior figures exist |
| B6. Cue rating plus code rule | Prediction items with 4-8 cues and a known outcome (e.g. outcome sets with ground truth) | (a) holistic answer, (b) model rates cues 1-5, code sums with unit weights, (c) code uses fitted weights | Accuracy / AUC | (b) matches or beats (a) by 0.02 to 0.10 AUC (Kuncel r .44 vs .28; Aegisdottir d .12). May fail if LLM cue reading is the noisy part |
| B7. Base-rate injection | Items where the class has an unbalanced outcome | With and without the class prior in the prompt | Brier score, accuracy | Gain in Brier on low-validity classes; no gain on regular classes (Aegisdottir trend) |
| B8. Noise | 5 identical runs per item | Single draw vs majority of 5 | Accuracy; within-item agreement | Majority helps most where run agreement is low (Atil: up to 15% swing). G4 limit: no help against shared bias |
| B9. Mode per class | Implicit pattern items (artificial grammar, rule induction), math items, commonsense items | Direct vs CoT vs thinking mode | Accuracy at equal tokens | Direct wins on pattern classes (Liu: -23 points GPT-4o), CoT on math. Re-measure for current model |
| B10. Counter vs context history | A class with graded history | (a) harness counter, (b) past graded cases in prompt, (c) both; labels clean, 30% noisy, delayed by 20 items | Gate quality (AUROC of predicted vs actual first-answer correctness) | Counter is robust to noise and delay; in-context history helps little on classification (Min 0-5%) and hurts on generation (Gao) |
| B11. Thinking budget sweep | Same item classes at 0, 200, 800, 3000, 10000 reasoning tokens | Fixed budget per arm | Accuracy and overconfidence (stated confidence minus accuracy) | Non-monotone on some classes (Lacombe: 45.0 peak, 35.7 at 768); flat or rising on math |
| B12. Re-check with and without outside check | Items where the first answer failed a gate | (a) re-ask the model, (b) re-ask with a test or tool output | Flip right-to-wrong and wrong-to-right counts | (a) no net gain, (b) net gain (Huang: oracle 95.5 to 97.5, intrinsic 95.5 to 89.0) |

Log from every run: mode chosen, gate inputs, whether the fast answer was accepted, whether it was right, tokens by state. This is already in SCHEMA section 6.

---

## 9. What does not transfer, and why

- **Human clinical judgment to LLM free-text reasoning.** Meehl-style studies use few cues, fixed criteria and human judges with fatigue and mood. The evidence says formulas beat inconsistent humans. An LLM at low temperature may be more consistent. The edge may shrink. Noise exists even at temperature 0 (d07) but is of another kind (critique.md).
- **The lens model's "C near 0".** Measured in human judges on linear prediction tasks. Chess-like nonlinear pattern skill is outside its scope (a14). An LLM may hold nonlinear knowledge that a unit-weight rule cannot match.
- **Years of feedback.** Tetlock needed 15 years to learn that long-range forecasting had near-zero validity (a02). An agent can run thousands of graded cases in hours, but only where a grader exists. Where grades exist, the class is probably already kind.
- **Fine-tuned correctness estimators.** Kapoor's 1000-example result and R-Tuning need fine-tuning (d01, d13). Our scaffold cannot do that, so those numbers give an order of magnitude only.
- **Logprob-based mixers and DeepConf.** Need token probabilities (c15, c29). A scaffold using a chat API may lack them.
- **Extremizing votes (Tetlock, 35%).** Aggregates independent humans. G4 forbids it for samples from one model.
- **Router transfer.** Routers in DynamicMind are trained on one model's results and lose accuracy on another (c17). The record must be rebuilt per model version.
- **Superforecaster demographics and team effects** (b17, d11). Not relevant to a single agent, and now contested.
- **Fingerprint examiner thresholds** (b21). Observational, human perception.
- **Human trust calibration.** Steyvers' result is about humans reading LLMs, not an agent reading itself (c01).
- **Group premortem** (a12). A team ritual with no outcome data. At most a single doubt move on untrusted classes; G1 forbids it on a schedule.
- **Copus parole study** (c24). Abstract only, versions disagree. Not usable as evidence of LLMs beating formulas.

---

## 10. Open questions

1. **Thresholds.** How many cases and what hit-rate floor make a class record trustworthy enough to skip deliberation? Kapoor gives only about 1000 for a learned estimator. No sequential-test rule exists (K19).
2. **Does an outcome-based class hit rate beat verbal confidence and agreement at equal tokens?** No direct test (K02, K11). Kapoor compared three signals but with a trained classifier and no token control.
3. **Validity of a new class before feedback.** Only people-based proxies (r about 0.20, d12). No method for LLM classes (K23).
4. **LLM as cue reader plus fixed rule.** Not searched. Does the formula edge survive when the agent fills the rubric?
5. **Delayed, sparse or ambiguous labels.** Random label noise is studied; delay is not (d06).
6. **Does a premortem or slow second look improve outcomes?** No outcome data in K&K (a12); not searched later.
7. **Mode choice by cue validity.** Maps exist by complexity (d09, contested), not by validity. Not measured for current frontier models (K22).
8. **Persistence of superforecaster skill after the 2025 reanalysis.** Only the abstract of the reanalysis was read (d11).
9. **Does decomposing a judgment reduce LLM noise?** Noise exists (d07); the Noise-book remedy is untested.
10. **Out-of-class detection and false-alarm cost.** Detection partly studied (d03, d13); cost not measured (d14).
11. **Do reasoning models gain calibration through training or architecture, and does it hold under larger thinking budgets?** Michael (ECE .037) and Lacombe (worse with more tokens) are not reconciled.
12. **Klein vs Kahneman: how often do experts overreach?** Left open by the authors.
13. **Do grade-independence flags matter in practice?** The wicked-feedback guard is argued (a18) but never tested.

---

## 11. Sources

[V] opened (read page or PDF text). [M] snippet, abstract or second-hand only.

**Core theory and human evidence**
- [V] Kahneman and Klein (2009), Conditions for intuitive expertise: a failure to disagree. https://gwern.net/doc/psychology/cognitive-bias/illusion-of-depth/2009-kahneman.pdf ; copy at https://dl1.cuni.cz/mod/resource/view.php?id=153128 (a01-a12, b01-b07)
- [V] Kuncel, Klieger, Connelly and Ones (2013), Mechanical versus clinical data combination in selection and admissions decisions. https://goal-lab.psych.umn.edu/orgpsych/readings/12.%20Judgment%20&%20Decision%20Making/Kuncel,%20Klieger,%20Connelly%20&%20Ones%20(2013).pdf (a13, a14, b08, b09)
- [V] Aegisdottir et al. (2006), The meta-analysis of clinical judgment project. https://gwern.net/doc/statistics/prediction/2006-aegisdottir.pdf ; https://journals.sagepub.com/doi/10.1177/0011000005285875 (a15, a16, b10, b11)
- [M] Grove, Zald, Lebow, Snitz and Nelson (2000), Clinical versus mechanical prediction. https://experts.umn.edu/en/publications/clinical-versus-mechanical-prediction-a-meta-analysis/ (b12; numbers via K&K a10)
- [M] Meehl (1954), Clinical versus statistical prediction (via K&K, a20)
- [M] Goldberg (1970); Karelaia and Hogarth (2008) (via K&K, a09, b05)
- [M] Shanteau (1992), Competence in experts. https://stafforini.com/works/shanteau-1992-competence-experts-role/ (a19)
- [M] Hogarth (2001), Educating Intuition (via K&K, a18)
- [V] Gruning and Krueger (2021), review of Soyer and Hogarth, The Myth of Experience. https://www.journalofexpertise.org/articles/volume4_issue3/JoE_4_3_Gruning_Krueger.pdf (a17)
- [V] Tutorial on mechanical decision-making for personnel and educational selection. https://pmc.ncbi.nlm.nih.gov/articles/PMC6990119/ (b13)
- [V] Human and algorithmic predictions in geopolitical forecasting (2024). https://pmc.ncbi.nlm.nih.gov/articles/PMC11373164/ (b14)
- [V] Recht, Meehl lecture slides. https://people.eecs.berkeley.edu/~brecht/cs281a/MeehlLecture.pdf (b26)
- [M] Kahneman, Sibony and Sunstein (2021), Noise (summaries). https://www.getabstract.com/en/summary-download/42159?format=1 (c27)

**Forecasting and expertise**
- [V] Tetlock, Mellers, Rohrbaugh and Chen (2014), Forecasting tournaments. https://journals.sagepub.com/doi/10.1177/0963721414534257 ; https://faculty.wharton.upenn.edu/wp-content/uploads/2015/07/2014---forecasting-tournaments-tools-for-increasing-transparency-and-improving-debate.pdf (a21, b15)
- [M] Mellers et al. (2015), Identifying and cultivating superforecasters. https://stafforini.com/works/mellers-2015-identifying-cultivating-superforecasters/ (b16)
- [V] Katsagounos et al. (2021), Superforecasting reality check. https://pmc.ncbi.nlm.nih.gov/articles/PMC7333631/ (b17)
- [M] Psychological Science (2025), Rethinking the role of teams and training in geopolitical forecasting. https://ifp.nyu.edu/?p=1727703 (d11, abstract)
- [M] Atanasov and Himmelstein (2023), Talent spotting in crowd prediction. https://ideas.repec.org/h/spr/isochp/978-3-031-30085-1_6.html (d12, abstract)
- [V] Residents' time to diagnose and diagnostic accuracy (2021). https://pmc.ncbi.nlm.nih.gov/articles/PMC8061054/ (b18, b19 second-hand)
- [V] A "blip of knowledge" study (2026). https://pmc.ncbi.nlm.nih.gov/articles/PMC12988131/ (b20)
- [V] Aggadi, Coon, Kibbey and Busey (2026), More skilled, more cautious. https://pmc.ncbi.nlm.nih.gov/articles/PMC13683028/ (b21)

**Language models**
- [V] Kadavath et al. (2022), Language models (mostly) know what they know. https://arxiv.org/abs/2207.05221 (a22, b22; c03 abstract only)
- [V] Tian et al. (2023), Just ask for calibration. https://arxiv.org/abs/2305.14975 ; https://arxiv.org/html/2305.14975 (a23, c04, c05)
- [V] Xiong et al. (2024), Can LLMs express their uncertainty? https://arxiv.org/abs/2306.13063 (a24)
- [V] Kuhn, Gal and Farquhar (2023), Semantic uncertainty. https://arxiv.org/abs/2302.09664 (a25; figures only)
- [V] Wang et al. (2023), Self-consistency. https://arxiv.org/abs/2203.11171 (a26, b23)
- [V] Huang et al. (2023), LLMs cannot self-correct reasoning yet. https://arxiv.org/abs/2310.01798 (b24)
- [V] Gema et al. (2025), Inverse scaling in test-time compute. https://arxiv.org/abs/2507.14417 (b25)
- [V] Steyvers et al. (2024), What LLMs know and what people think they know. https://arxiv.org/html/2401.13835v2 (c01, c02)
- [V] Michael et al. (2026), Confidence calibration in LLMs (summary page). https://www.alphaxiv.org/abs/2605.23909.md (c06, c07)
- [V] Lacombe, Wu and Dilworth (2025), Don't think twice. https://arxiv.org/html/2508.15050v1 (c08, c09)
- [M] Sprague et al. (2024), To CoT or not to CoT. https://arxiv.org/abs/2409.12183 (c10, abstract)
- [V] Liu et al. (2024), Mind your step (by step). https://arxiv.org/html/2410.21333v4 (c11, c12)
- [M] Hagendorff, Fabi and Kosinski (2022), Thinking fast and slow in LLMs. https://arxiv.org/abs/2212.05206 (c13, abstract)
- [V] Ziabari et al. (2025), Reasoning on a spectrum. https://arxiv.org/html/2502.12470v3 (c14, c15)
- [V] DynamicMind (2025). https://arxiv.org/pdf/2506.05936 (c16, c17)
- [V] Liu et al. (2025), Think how to think (TH2T). https://arxiv.org/html/2507.02663v3 (c18)
- [M] Chen et al. (2024), Do NOT think that much for 2+3=? https://arxiv.org/abs/2412.21187 (c19, abstract)
- [M] Yue et al. (2024), LLM cascades with mixture of thoughts. https://arxiv.org/abs/2310.03094 (c20, abstract)
- [V] Kim et al. (2026), ReASC. https://arxiv.org/html/2601.02970v1 (c21)
- [V] Aghazadeh et al. (2025), CGES. https://arxiv.org/html/2511.02603v1 (c22)
- [V] Halawi et al. (2024), Approaching human-level forecasting with language models. https://arxiv.org/html/2402.18563v1 (c23)
- [M] Copus (2025), Computational clinical judgment. https://irlaw.umkc.edu/faculty_works/1066 (c24, abstract)
- [M] Scholten, Rebholz and Hutter (2024), Metacognitive myopia in LLMs. https://arxiv.org/abs/2408.05568 (c25, framework)
- [M] Huang et al. (2026), CogBias. https://arxiv.org/abs/2604.01366 (c26, abstract)
- [M] Scaling with Confidence (CAS, 2026). https://arxiv.org/pdf/2607.01612 (c28, snippet)
- [M] DeepConf (2025). https://arxiv.org/abs/2508.15260 (c29, summary)
- [V] Kapoor et al. (2024), LLMs must be taught to know what they don't know. https://arxiv.org/abs/2406.08391 (d01-d04; AUROC values in figures not read)
- [V] Min et al. (2022), Rethinking the role of demonstrations. https://arxiv.org/abs/2202.12837 (d05, d15)
- [V] Gao et al. (2024), Noise robustness of in-context learning for text generation. https://arxiv.org/abs/2405.17264 (d06)
- [V] Atil et al. (2025), Non-determinism of "deterministic" LLM settings. https://arxiv.org/abs/2408.04667 (d07, d08)
- [V] Shojaee et al. (2025), The illusion of thinking. https://arxiv.org/abs/2506.06941 (d09, d10; rebuttals [M], not opened)
- [V] Zhang et al. (2024), R-Tuning. https://arxiv.org/abs/2311.09677 (d13; table garbled)
- [V] Wen et al. (2024), Know your limits: abstention survey. https://arxiv.org/abs/2407.18418 (d14)

Notes on source quality (from critique.md): a18, a19, a20 not opened; b12, b16, c03, c10, c13, c19, c20, c24, c26, c27, c28, c29 are abstract, snippet or summary only, and their numbers should not be cited without a re-open. Kadavath numbers in a22 and b22 were not re-opened beyond the downloaded text; no claim number rests on them. Use c05 (not a23) for the TruthfulQA AUC; GPT-4 reaches .632.
