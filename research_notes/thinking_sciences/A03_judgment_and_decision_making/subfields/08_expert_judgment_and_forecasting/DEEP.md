# Expert judgment and forecasting: deep document

*Subfield A03.08. Focus: statistical versus clinical prediction (Meehl, Dawes, Tetlock) and every LLM study that tests or uses it. Evidence ids (a01 to d15) point to the evidence_a-d.jsonl files in this folder. Claim ids (K01 to K44) point to claims.jsonl. Status marks follow SCHEMA.md: [E] established, [S] single-source, [C] contested.*

## 1. What it is

The question is old and simple. Two ways exist to turn the same facts into a prediction.

- **Clinical (holistic) combination.** An expert looks at the facts and forms an overall judgment in the head.
- **Mechanical (statistical) combination.** A fixed rule turns the facts into a number or a class. The rule can be a fitted regression, an equal-weight sum of standardised cues, or a short checklist. It does not change case by case.

Meehl (1954) argued that the mechanical way predicts at least as well. Seventy years of studies say he was right on average. The edge is modest, not huge. Clinical judgment almost never wins clearly (a01, b01, a09).

A second strand is forecasting. Tetlock (2005) measured expert political forecasts over about 20 years. Experts barely beat informed laymen and did not beat simple rules (a12, b11). The IARPA tournament (2011 to 2015) then showed that forecasting skill can be selected, trained, teamed and aggregated (a13, b06, b10).

A third strand is new. Language models are now forecasters (2024 to 2026) and now read tabular data as text. Several papers test whether they behave like the clinicians in Meehl's studies. The answer is mixed. Zero-shot LLMs that combine tabular facts in their heads lose to simple trained models (a26, a27, c26). LLM forecasters that use retrieval, many samples and a code aggregate reach the human crowd, and by 2026 near superforecasters (a18, a22, b23, c33).

Why it matters for our agent. Our schema already says the program decides and counts, and the model fills slots (SCHEMA section 1, G5). This subfield is the human-science base for that split in S7: the model scores or extracts features, and code combines them. The key point from Dawes (1979): humans (and plausibly models) are good at picking and reading the cues and bad at weighing them (a05, K05).

The honest limit: no study yet tests this exact split against a holistic verdict at equal tokens on reasoning or puzzle tasks (K37, critique gap 1). The principle is established for humans and for tabular LLM tasks. For our bench it is a hypothesis that we must run.

## 2. History and theories in depth

### 2.1 Meehl 1954 and the debate it started

Meehl's book "Clinical versus statistical prediction" (1954) collected the few studies then available. Statistical rules matched or beat clinicians. Meehl (1965) knew of one possible exception. Goldberg (1968) disputed even that (a01). Sawyer (1966) separated two things that people had mixed: how the data are collected (clinical or mechanical) and how they are combined (clinical or mechanical). This matters for us. A model can collect and read data clinically, then hand the numbers to code to combine.

Meehl also supplied the standard reply to "but rules cannot handle the special case". His "broken leg" example: a rule predicts that a man goes to the cinema, but the clinician knows he broke his leg. A rare, decisive, private fact justifies an override. Meehl's point was that such facts are rare and that clinicians claim them far too often. Modern data agree (section 2.7, d11).

### 2.2 Dawes 1979 and 1971: improper linear models

Dawes showed the formula need not be optimal. Key results from the full text (a01 to a06):

- **Admissions case.** N=111 Oregon psychology graduate students. An equal-weight sum of GRE, GPA and school selectivity correlated r=.48 with later faculty ratings. A cross-validated regression gave R=.38. The admissions committee gave r=.19. Ratings reliability was about .67. Correction found in our cross-check: the committee figure used only 23 of the 111 students, because the rating scale changed across years (critique, source 1). The .48 versus .19 contrast is not a full-sample contrast. Quote it with that note.
- **Bootstrapping.** A linear model of a judge's own past judgments beats the judge. Wiggins and Kohen (1971): models of every one of the Illinois judges beat the judges at predicting first-year GPA (90 students, 10 cues). Goldberg (1970): bootstrapping beat 26 of 29 clinicians on neurosis versus psychosis from the MMPI. Why: the model keeps the judge's cue use and drops the judge's unreliability. It removes noise, not insight.
- **Cue picking versus cue combining.** Einhorn (1972): doctors' overall severity ratings of Hodgkin's biopsies did not predict survival in 193 patients, though their coded features did.
- **Simplest model wins.** On a bankruptcy task of 60 firms (Libby), loan officers got 74 percent (44.4 firms), models of them 72 percent, and the ratio of assets to liabilities alone 80 percent (48 firms). Fitted linear models cross-validated at about 78 percent.
- **Why weights matter little.** Dawes argued that with positively correlated cues, monotone relations and noisy criteria, any positive weights give a composite very close to the optimum. Sign and cue choice matter more than size. Kuncel et al. (2013) repeat the argument: weights can come from the literature or pooled expert opinion, and small samples are no excuse (a08, b05).

### 2.3 The meta-analyses

- **Grove, Zald, Lebow, Snitz, Nelson (2000).** 136 comparisons. Mechanical prediction was on average about 10 percent more accurate. Mechanical was clearly better (effect at least .05) in about 46 percent, comparable in about 48 percent, and clinical clearly better in under 6 percent (c30). Other cuts of the same meta-analysis give 33 to 47 percent versus 6 to 16 percent; the range depends on the cutoff (critique, contradictions). The edge held across tasks, judge types and experience levels. The clinician's disadvantage grew when the data included a clinical interview (b01 to b03). Only the abstract page was opened by our team (a11).
- **Aegisdottir et al. (2006).** 67 studies, 92 effect sizes. Weighted d+ = -.15 (CI -.17 to -.13). Restricted to cross-validated studies with no outliers: 41 studies, 48 effects, d+ = -.12. Of 48 effects, about 52 percent favoured statistical, 38 percent showed no difference, 10 percent favoured clinical (a09; one place gives 53 percent, small mismatch unresolved). Moderators: linear formulas d+ = -.15, hand-built logical rules or signs d+ = -.03 with a CI that includes zero (Q_B(3)=11.94, p<.01). Study year, number of clinicians, number of predictions and criterion quality did not predict the effect (a10). So there is no sign the gap closed over time.
- **Kuncel, Klieger, Connelly, Ones (2013).** Hiring and admissions. Validity for job performance .44 mechanical versus .28 clinical (more than 50 percent better). Advancement .42 versus .36. Training .31 versus .16. Grade point average .58 versus .48. Other academic criteria .47 versus .46 (clinical side only 161 students; no gap) (a07, b04). Not corrected for range restriction, so true gaps are likely larger.

### 2.4 Tetlock and the forecasting tournaments

- **Expert Political Judgment (2005).** About 284 experts, 82,361 forecasts over about 20 years. Experts barely beat informed non-experts, and neither beat simple rules and models. On three-state questions, forecasters often did worse than assuming equal chances. Foxes (many small ideas) beat hedgehogs (one big theory), especially in long-range forecasts in their own field (a12, b11). These numbers reach us through the Armstrong and Green review. The book itself was not opened.
- **IARPA tournament (Mellers et al. 2014, 2015).** Randomised trials in years 1 and 2 found that probability training, teaming and tracking each improved calibration and resolution (a15, a14). Top performers each year were placed in elite teams. In years 2 and 3 the 60 superforecasters (5 teams of 12) kept their lead: standardised Brier -0.34 versus -0.14 for top-team individuals and +0.04 for all others; AUC 96 percent, 84 percent, 75 percent; resolution .40, .35, .32; calibration .01, .03, .04 (a13, b06). They also learned faster during a year: slope -0.26, -0.18, 0 (b07). They sat at least 1 SD above the population on fluid and crystallised intelligence, and scored high on actively open-minded thinking, need for cognition and scope sensitivity (b08). Rounding their forecasts to the nearest 0.10 cost accuracy, but not for the comparison groups: fine-grained numbers carried signal (b09). Tetlock's own four-factor summary: identify, train, team, aggregate. Superforecaster teams saw about 400 days out as well as ordinary forecasters saw 150 (b10; slide, chart garbled).

### 2.5 Kahneman and Klein (2009)

Intuition is trustworthy only if the environment is regular enough to learn and the expert had practice with feedback. Only the abstract was read (a28). It explains why the formula edge shrinks or vanishes where outcomes are very noisy, and why experts in valid environments (chess, firefighting) can be fine.

### 2.6 Modern big-data version: bail decisions

Kleinberg et al. (2017/2018): 554,689 NYC cases (443,751 train, 110,938 holdout). A gradient-boosted tree on defendant records versus judges. At the judges' own jailing rate, crime falls by 24.7 percent (24.8 in the intro). At the judges' own crime rate, jailing falls by 41.8 percent (42.0 in the intro). The riskiest 1 percent of defendants have 62.6 percent predicted risk; judges released 48.5 percent of them (73.6 percent of all defendants were released). Stricter judges did not jail the riskiest first: detaining in risk order would jail only 48.2 percent as many people or give a 75.8 percent larger crime reduction (a16, a17, b12, b13).

Caveats stated by the authors (d04, d05): selection on observables, the selective labels problem, and omitted payoffs. They note that earlier clinical-versus-statistical work shared these weaknesses. A lenient-judge test (train on lenient judges' released cases, impute outcomes for strict judges' released cases) found no sign that lenient judges use valuable soft information, but with limited power. De-Arteaga et al. (2018) show that models trained only on cases a human chose to label learn "what happens when a human predicts risk", not true risk, and methods that assume every case could be labelled fail when humans are consistent (d03; child-welfare data, 83,311 referrals).

### 2.7 Overrides

Angelova, Dobbie, Yang (2023): about 90 percent of bail judges did worse than the algorithm when they overrode it; most override decisions were about as accurate as random guessing; about 10 percent of judges beat it, when they used private information and avoided reacting to salient events (d11; abstract page only). This is the modern data on Meehl's broken leg.

### 2.8 Low-ceiling domains

Fragile Families Challenge (Salganik et al. 2020, PNAS 117:8398): 457 applications, 160 valid teams, six outcomes, thousands of predictors. Best holdout R2 about 0.2 for material hardship and GPA, about 0.05 for grit, eviction, layoff and job training. A 4-variable baseline (mother's race, marital status, education at birth, plus the outcome or a proxy at age 9) beat many teams, and ensembling added little (d08, c31). The lesson: when the ceiling is low, a tiny rule is nearly as good as anything, and honest output says "little better than base rate".

### 2.9 Forecast aggregation theory

Averaging many forecasts helps. Extremizing (pushing the average away from 0.5) helps when forecasters hold partly independent information. Satopaa, Pemantle, Ungar (2014): the best factor depends on how much information overlaps and can be derived from the forecasts without outcomes. On 44 superforecasters, 123 events: simple average Brier .132, log pool .128, probit pool .128, "revealed aggregator" .123, base rate .187 (d09). Neyman and Roughgarden (2022) give a worst-case argument for averaging then extremizing by a constant, sqrt(3) (d10, abstract page only).

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Equal-weight composite beats the admissions committee | r=.48 vs .19 (committee on only 23 of 111 students); cross-validated regression R=.38; N=111 | Dawes 1979 (a02) | [E] |
| A model of the judge beats the judge | Models beat all judges in Wiggins and Kohen (90 students, 10 cues); beat 26 of 29 clinicians (Goldberg) | Dawes 1979 (a03) | [S] (one review, two studies) |
| Doctors' features predict, their overall rating does not | Hodgkin's biopsies, 193 patients | Einhorn via Dawes (a05) | [S] |
| One ratio beats loan officers | 80% (assets/liabilities) vs 74% officers vs 72% models of officers; 60 firms | Libby via Dawes (a06) | [S] |
| Mechanical beats clinical on average, 136 comparisons | about 10% more accurate; clinical clearly better in under 6% (46% / 48% / under 6% at the .05 cutoff) | Grove 2000 (b01, c30) | [E] |
| 56-year meta-analysis | d+ -.15 (CI -.17 to -.13), 67 studies; cross-validated d+ -.12 | Aegisdottir 2006 (a09) | [E] |
| Linear formula helps, hand-built rules do not | d+ -.15 vs -.03 (CI includes 0); Q_B(3)=11.94 | Aegisdottir 2006 (a10) | [S] |
| No time trend in the gap | year, clinician count, prediction count all ns | Aegisdottir 2006 (a10) | [S] |
| Hiring: mechanical validity higher | job perf .44 vs .28; advancement .42 vs .36; training .31 vs .16; GPA .58 vs .48; other academic .47 vs .46 (n=161) | Kuncel 2013 (a07) | [E] |
| Interview data widen the clinician's disadvantage | relative drop with interview data (no coefficient read) | Grove 2000 (b02) | [S] |
| Long-range political experts near chance | 284 experts, 82,361 forecasts; foxes beat hedgehogs | Tetlock 2005 via review (a12) | [S] (book not opened) |
| Superforecasters persist | standardised Brier -0.34 vs -0.14 vs +0.04; AUC 96/84/75% | Mellers 2015 (a13, b06) | [E] |
| Rounding hurts supers | nearest 0.10 lowers accuracy for supers only | Mellers 2015 (b09) | [S] |
| Bail algorithm beats judges | 24.7% less crime at same jailing, or 41.8% fewer jailed at same crime; N=554,689 | Kleinberg 2018 (b12) | [E] with caveats |
| Judges mis-rank risk | riskiest 1%: 62.6% risk, 48.5% released | Kleinberg 2018 (a16) | [E] |
| 90% of judges lose when overriding | about 90% worse than algorithm; about 10% better | Angelova 2023 (d11) | [S] |
| Low ceiling: 160 teams barely beat 4 variables | best R2 about 0.2 (two outcomes), about 0.05 (four) | Salganik 2020 (d08) | [E] |
| Zero-shot LLM loses to ML on EHR | AUROC GPT-4 .629 / .602 vs ML .847 / .894; Brier .251 vs .134 | Malin 2025 (c26) | [E] |
| Zero-shot LLM loses on COVID mortality | F1 GPT-4 .43 vs XGBoost .87 (N=9,134); fine-tuned Mistral-7b F1 .74 external | Ghaffarzadeh-Esfahani 2024 (a26) | [E] |
| Chain of thought hurt risk scoring | GPT-4 AUC .69 to .60; ChatGPT .62 to .58; tree/SVM .79; N=690 | UK Biobank study 2024 (a27) | [S] |
| Extract features, fitted model combines | heart: xgboost .985 vs direct 10-shot .620; hepatitis .992 vs .642; stroke .740 vs .558 | TEMED-LLM 2023 (c27) | [S] |
| Structured extraction cost | about 2 to 3% AUC vs direct fine-tuning, more transparent | ClinStructor 2025 (c28) | [S] (snippet) |
| LLMs poor at numeric regression, fair at small classification | Diabetes R2: linear .45 vs o3 -1.41; lupus 87 rows: LR .889 vs GPT-4o .833 | Zero-training LLMs 2025 (c25) | [S] |
| LLM priors under covariate shift | closes up to 59% of oracle gap; wins 8 of 10 vs AutoElicit | LoID 2026 (c29) | [S] |
| Off-the-shelf LLM forecasters poor | best zero-shot GPT-4-1106 Brier .208; most at or above .25 | Halawi 2024 (a18) | [E] |
| Retrieval + fine-tuned reasoning + ensemble | Brier .179 (71.5%) vs crowd .149 (77.0%); 914 test questions; blend .146 | Halawi 2024 (b14, c05) | [E] |
| Retrieval is the main gain | neither retrieval nor fine-tune .206; no fine-tune with retrieval .186; full .179 | Halawi 2024 (d14) | [S] |
| Model wins only where crowd is unsure | crowd .3-.7: .199 vs .246; joint rule: .240 vs .247 on 22% of forecasts | Halawi 2024 (a19) | [S] |
| 12-LLM median matches 925-person crowd | .20 vs .19, t(60)=.19, p=.850; 31 questions | Schoenegger 2024 (a20) | [E], equivalence test not preregistered |
| Agents ensemble well, base LM does not | agent .169 vs .180 single; base LM .218 vs .210 | Hsieh 2024 (a25) | [S] |
| Plain average beats model self-update | model sees human median: +17 to 28%; average of both better | Schoenegger 2024 (a21) | [E] |
| Fixed Platt scaling in code | .1140 to .1076 (498 q); extremization .1085; isotonic .1097; LLM supervisor .1125; best-of-k .1191 | AIA 2025 (c17, d12) | [S] |
| Mean of 10 forecasts | .1140 vs single .1182 | AIA 2025 (c17) | [S] |
| Prompt tricks do not help | 38 prompts, 4 models, 100 questions; adj p 0.77 to 0.99; Bayesian reasoning +0.03 worse | Schoenegger 2025 (c09) | [E] |
| Agentic search beats none | no search .1230; agentic .1140 to .1182 | AIA 2025 (c16) | [E] |
| Capability tracks accuracy | Arena score vs Brier r=-0.69; parity near 1398-1406 | ForecastBench (a23, c04) | [E] |
| LLM-supers gap larger on combination questions | .076 vs .130 (GPT-4o); gap .054 vs .026 model-step gap | ForecastBench (b20, b21) | [E] |
| Best LLMs near supers | 2025 GPT-4.5 .101 vs .081; Jan 2026 gap .017; July 2026 several systems statistically indistinguishable | FRI (b22, b23, c33) | [E] direction, [C] date |
| Pros vs bots shrinks | -20.03 (p=.00001, 93 q) in Q2 2025; -1.25 (p=.247, 99 q) spring 2026 | Metaculus (c11, c13) | [C] |
| Retrospective evaluation is inflated by leakage | leaky .108 vs leak-free .242 vs none .244 (93 q); pre-cutoff .11 vs post .24 | El Lahib 2026, Li 2026 (d01, d02) | [E] |
| Reasoning models leak more | gaps .086 / .097 vs .064 / .067 | Li 2026 (d02) | [S] |
| Brier is base-rate dependent | 50 coin-flips + 50 rare: perfect on rare = .125; better coin-flips = .10 | Paleka 2025 (b28) | [S] |
| Consistency tracks Brier for some checks | conditional r=.92 scraped, .71 NewsAPI; negation .60 and -0.36 | Paleka 2024 (c20) | [C] |
| Training for consistency gives no accuracy gain | held-out checks and Brier unchanged | Paleka 2025 (b26) | [S] |
| LLM advice helps humans | +24 to 28% accuracy, N=991; good vs noisy advisor no difference | Schoenegger 2024 (b29, c08) | [E] |
| Rubric: holistic LLM judge matches or beats analytic | Kendall tau holistic .536 / .585 vs analytic .464 / .471, batch .167 | Huynh 2026 (d07) | [S] |
| High repeatability does not mean validity | test-retest above .95 with position bias above .10; 21 judges | Norman 2026 (d06) | [S] |

## 4. Mechanisms and models

### 4.1 Why the formula wins: the lens model

Brunswik's lens model splits judgment accuracy into three parts: how well the cues predict the outcome (environment), how consistently the judge uses cues (consistency), and how well the judge's cue weights match the best weights (knowledge). Expert judgments have about the right cue weights but low consistency. A formula uses the same weights with perfect consistency. That is why bootstrapping (fit a regression to the judge's own outputs) beats the judge (a03, a08). Nothing is added. Noise is removed. (Kuncel 2013 uses this frame, a08.)

For an LLM the same split holds. The sampled verdict varies from run to run (noise). A fixed formula over the scored features applies the same weights each time.

### 4.2 Why equal weights are enough

If cues are positively intercorrelated and the criterion is noisy, the composite score changes little as weights change within a sensible range. Fitting weights on a small sample adds estimation error that can outweigh the gain. Equal weights have no estimation error. Only the sign of each weight needs to be right.

**Implementation:** for k features that each predict "better answer", score each on a fixed scale (say 0 to 10), standardise across candidates if scales differ, flip the sign of "bad" features, and sum. Rank candidates by the sum in code (G5). No fitting needed.

### 4.3 Division of labour (the S7 split)

1. **Model extracts or scores features.** Narrow questions: "does this candidate satisfy constraint C? 0 to 10". Fresh context per feature if possible, answers in a fixed format. Randomise candidate order (position bias, d06).
2. **Code combines.** Unit-weight sum, or weights from a small dev set, or a stored class record. Numeric work (means, regression, probabilities) is only done in code (c25, a26).
3. **Code decides.** Pick the top candidate, or pass the list to the verify state.
4. **The model's free-form overall impression does not enter the combine step.** In Grove 2000, adding clinical interview data worsened clinician performance (b02). A free-form overall verdict can be kept only as one more feature with a unit weight, or as a tie-break (untested).

### 4.4 The forecasting pipeline (best-documented LLM system)

Pieces from Halawi 2024, Hsieh 2024, AIA 2025 (a18, a25, c15, d14, d15), as steps:

1. Retrieve. Several queries, rank articles, summarise. Retrieval carries the most gain (d14, c16). Use only post-cutoff material for scoring (d01).
2. Reason and forecast. Several independent samples per question (Halawi 6; AIA 10).
3. Aggregate in code. Halawi: trimmed mean beat mean, median, geometric mean and USC on validation (d15). AIA: mean of 10 beat single, .1140 versus .1182 (c17).
4. Calibrate in code. Fixed Platt scaling with sqrt(3) gave .1140 to .1076 (d12). A fit on another benchmark gave .1104 on the target (partial transfer). On an already calibrated system binning and isotonic did not help (d15).
5. Blend with an external anchor in code (market, crowd). Halawi: a 4-to-1 crowd-weighted blend gave .146 versus crowd .149. AIA: blending helped only where the model was weaker (c18).
6. Gate. Defer to the anchor when the anchor is near 0 or 1, where models hedge (a19).

Pseudo-code for steps 3 to 5:

```
probs = [forecast_i for i in range(k)]            # independent samples
p = trimmed_mean(probs, trim=0.1)                 # code
p = platt(p, d=sqrt(3))                           # code, only if system is under-confident
if anchor is not None:
    p = w_anchor * anchor + (1 - w_anchor) * p    # fixed w, tuned on dev slice
p = clip(p, 0.02, 0.98)                           # guard against extremes
```

### 4.5 Information overlap and extremizing

When k samples come from one model, they share most information. Averaging then extremizing can overshoot. The optimal factor depends on overlap (d09). AIA's own fitted optimum was 2.27, the superforecaster-optimal 1.72, the constant used 1.73 (sqrt(3)) (d12). Treat the factor as something to tune on a held-out slice, never to assume. This is why SCHEMA G4 forbids extremizing votes on single-answer problems: samples from one model are not independent.

### 4.6 Selective labels and the learning loop

Any formula we fit on outcomes of the agent's own past choices sees only the cases the agent selected. De-Arteaga (d03) and Kleinberg (d04) show the bias. Fix: keep a small random exploration slice whose outcomes are recorded regardless of the choice, or use quasi-random assignment.

### 4.7 Consistency as a cheap signal

Arbitrage-style checks (conditional probabilities, negation, paraphrase) can be run with no ground truth. Some track later Brier strongly (conditional r=.92 on scraped data), others do not (negation -0.36 on NewsAPI) (c20). Training to fix inconsistency did not raise accuracy (b26). Use as a diagnostic, not as an objective.

## 5. What holds up

### 5.1 Replications

- The mechanical edge replicated in three large meta-analyses over 1954 to 2013 across medicine, psychology, hiring and admissions: Grove 2000, Aegisdottir 2006, Kuncel 2013 (b01, a09, a07). Effect size is small and steady: about 10 percent in accuracy, d+ -.12 to -.15, validity .44 versus .28 for job performance.
- Forecasting skill persistence replicated across the tournament years (a13, b06, b07).
- Aggregation gains for LLMs were found by four independent groups (Halawi, Schoenegger, Hsieh, AIA) (K18).
- The bail algorithm result is one large study; later critiques exist (selective labels, omitted-variable bias, judges' soft information) but we did not collect them. Treat the 41.8 and 24.7 percent figures as one paper (critique, source 6).

### 5.2 Failed or weak results

- Clinicians clearly win in a small minority: 6 to 16 percent of studies in Grove, about 10 percent in Aegisdottir (b03, a09).
- Hand-built logical rules did not beat clinicians (d+ -.03) (a10).
- Non-grade academic criteria showed no gap (.47 vs .46; n=161) (a07). Do not generalise "over 50 percent better" beyond job performance.
- Zero-shot LLMs lost to trained ML (section 6); in-context examples did not close the gap in EHR data (c26).
- Training LLMs to be consistent did not raise accuracy (b26). Model-based fixes (LLM supervisor, best-of-k) lost to statistical fixes in code (c17).
- Detailed prompting recipes (38 prompts, 4 models) gave no reliable gain after multiple-comparison correction (c09, c10).
- Ensembling the base model without tools did not help (.218 vs .210) (a25).

### 5.3 Moderators and boundary conditions

- **Environment must be learnable with valid cues.** Where outcomes are very noisy, all methods are weak (Fragile Families R2 about .05 to .2) (d08, K08).
- **Interview and impression data hurt the clinician** (b02).
- **Linear beats hand-built rules** (a10).
- **Selection on observables and stable regime.** The bail result needs these. Small samples, regime change and gaming remain undocumented for LLM agents (critique gap 6).
- **Crowd uncertainty, evidence count.** The LLM forecaster beats the crowd only when the crowd is between .3 and .7, retrieval is early and 5 or more articles exist (a19, b16).
- **Question mix and base rate.** Brier is not comparable across mixes (b28).
- **Question type.** The LLM gap to superforecasters is larger on combination questions (b21, c03).

### 5.4 Interventions that worked

For humans: probability training, teaming, tracking, selecting top performers, aggregation (a14, a15, b10). For LLM forecasters: retrieval (largest), agentic multi-step search, many samples with code aggregation, fine-tuning on reasoning that beat the crowd (13,253 kept of 73,632 generated), fixed Platt scaling (small), plain blending with a crowd anchor (b15, c16, c17, c06). LLM advisors helped humans by 24 to 28 percent, even noisy ones (b29).

### 5.5 Interventions that did not work

Prompt wording and personas (c09). Showing the model the crowd median and letting it update (worse than averaging) (a21). Isotonic or binning on a calibrated system (d15). Telling the model to ignore post-cutoff knowledge (closes only 48 percent of the gap) (c23). Human overrides of an algorithm (about 90 percent of judges lose) (d11). Consistency training (b26).

### 5.6 Evaluation hygiene

Leakage inflates retrospective scores: leaky retrieval Brier .108, leak-free .242, no retrieval .244 (93 questions, one model) (d01). Reasoning models leak more (d02). Search date filters leak (33.2 and 34.5 percent of URLs). At least 3.8 percent of one dataset and 10 percent of another were leaking or trivial (b27). Halawi's post-cutoff test is less exposed, but search leakage was not tested there. AIA's leak filter flagged 16 true leaks of 81 flagged; dropping flagged questions moved Brier .1159 to .1161 (d13).

### 5.7 Corrections to earlier notes

- Dawes: the committee comparison used 23 of 111 students.
- Halawi: 0.186 means retrieval kept, no fine-tuning; 0.206 is neither (d14).
- Schoenegger: the equivalence test was not preregistered and had a coding error corrected afterwards; the 57.35 percent mean forecast is the figure in the text, and the human crowd mean was also above 50, so "models lean yes" is only partly confirmed (critique, source 5).
- ForecastBench numbers appear in two versions (.096/.121/.122 and .092/.114/.114) of one paper.
- Metaculus: pros-versus-bots results changed between quarters (c11, c13). FRI parity dates and Metaculus results measure different things.

## 6. Language models

### 6.1 Tabular and structured judgment (the Meehl test for LLMs)

| Task | LLM direct | Trained or hybrid | Source |
|---|---|---|---|
| EHR prediction (VUMC / MIMIC) | AUROC GPT-4 .629 / .602; GPT-3.5 .537 / .517 | ML .847 / .894 | c26 |
| COVID mortality (N=9,134) | F1 GPT-4 .43 | XGBoost .87 internal, .83 external; fine-tuned Mistral-7b .74 | a26 |
| Myocardial infarction (N=690) | AUC GPT-4 .69, with CoT .60 | decision tree .79, logistic .77 | a27 |
| Heart, hepatitis, stroke | accuracy .620, .642, .558 | features extracted by LLM + xgboost .985, .992, .740 | c27 |
| Lupus (87 rows) | GPT-4o .833, GPT-5 .778 | logistic .889 | c25 |
| Regression (diabetes R2) | GPT-o3 -1.41 | linear .45 | c25 |

Reading: LLMs behave like Meehl's clinicians. They read cues well (extraction accuracy .92 to .99 in TEMED-LLM) and combine them poorly. Moving the combination to a fitted model gives large gains (c27). The cost is about 2 to 3 percent AUC against direct fine-tuning in a text-structuring study, in return for transparency (c28, snippet only). Chain of thought made risk scoring worse in one study (a27). LLM priors can still help a statistical model under covariate shift (c29), and a language model trained on event sequences beat logistic regression and XGBoost (61.6 percent versus 52.9 and 58.2 percent event accuracy, N=65,606) (c32). These last two use the LM as a component, not a verdict-giver.

Gap: no 2023 to 2026 paper compares "LLM scores features, code combines" against the same LLM's holistic verdict on reasoning tasks at equal tokens (K37). The closest, rubric grading, found holistic matching or beating analytic scoring (Kendall tau .536 to .585 versus .464 to .471) and a batch analytic prompt at .167 (d07). The aggregation rule mattered. This is a warning: splitting into features does not help automatically.

### 6.2 Forecasting

Timeline of the best LLM numbers (Brier, lower is better):

| Date | System | Result | Reference point | Source |
|---|---|---|---|---|
| Feb 2024 | Best zero-shot GPT-4-1106 | .208 | .25 uninformative | a18 |
| Feb 2024 | Halawi full system | .179 | crowd .149 | b14 |
| Feb 2024 | 12-LLM median | .20 | 925-person crowd .19 | a20 |
| Aug 2024 | Hsieh agent ensemble | .169 | crowd .172 | a25 |
| 2024 | ForecastBench: best LLM Claude 3.5 Sonnet | .122 (200 q) | supers .096, public .121 | a22 |
| mid 2025 | o3 on 464 Metaculus questions | .1352 | ten expert forecasters .1573 mean, median .0225 | a24 |
| 2025 | AIA Forecaster | .1076 (498 q) | supers .1110; market-liquid questions .1258 vs market .1106 (loses) | c15 |
| Oct 2025 | GPT-4.5 | .101 | supers .081 (adjusted) | b22 |
| Jan 2026 | Best system | gap .017 | about one year of LLM progress | b23 |
| Apr 2026 | Murphy agentic forecaster | Brier Index 73.8 vs 70.8 best external | supers median 70.9 (different question sets) | b24 |
| Jul 2026 | Several systems | statistically indistinguishable from supers | one-sided p .14 to .41 | c33 |

Rate of improvement: about 0.016 Brier per year (b22). Arena score versus Brier r=-0.69 (c04). The gains came mostly from base model quality, and from retrieval and ensembling around it (c12, c14). On Metaculus quarters, high-reasoning bots beat standard twins in 8 of 8 pairs (p=0.004), aggregated runs added +1,799 points, and team size above 2 mattered little (c12, c14). The winner used a 6 to 7 step research stage and 5 final predictions from 3 models.

Behaviours:
- **Acquiescence.** Mean forecasts above 50 percent while resolutions were near even (a21; the human mean was also above 50, so partly confirmed).
- **Hedging near the extremes.** The system lost to the crowd when the crowd was near 0 or 1 (accuracy +7 percent but Brier worse by .04) (a19).
- **Extreme overconfidence after outcome-based RL without guardrails.** 39.3 percent of predictions fell in 0 to 10 or 90 to 100 percent (c19). A 14B model trained on outcomes reached .190 versus o1 .202, base .215, Polymarket .151 (c19).
- **Poor on conjunctions.** Gap to supers .053 against .035 between model generations (c03).
- **Needs the crowd value.** ForecastBench best model: .126 without crowd values, .114 with (c02).
- **Knowledge leakage in evaluation.** Section 5.6.

### 6.3 What moved the numbers, ranked

1. Better base model (about 0.016 Brier per year).
2. Retrieval, especially agentic multi-step (no search .123, agentic .114 to .118; neither retrieval nor fine-tune .206 vs full .179).
3. Many samples aggregated in code (.1182 to .1140 for 10).
4. Blending with an external anchor (.149 to .146 in Halawi; larger where the model is weak).
5. Fixed calibration in code (about .006).
6. Prompt changes: about zero.

### 6.4 Humans plus LLMs

LLM assistants raised human accuracy 24 to 28 percent (N=991, preregistered), with no difference between a good and a deliberately overconfident advisor (b29, c08). This is a human-AI result and does not transfer to a single agent (section 9).

## 7. What our agent should take

Mapping is to SCHEMA.md parts. Status marks: [E] established, [S] single-source, [C] contested.

### Add now (established)

| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| N1 | When several candidates must be compared on several criteria, the model only scores each criterion on a fixed scale; code does the arithmetic and the ranking. The model's overall impression is never the combiner. (Principle only; the head-to-head on our bench is still a test, see T1.) | S7, G5 | [E] for the principle in humans and tabular LLM tasks; [S] for reasoning tasks | a01, a05, a07, a09, a26, c27; K01, K05, K13 |
| N2 | If code combines features, use unit weights (sign only) unless a dev set shows a fitted weight set is better. Do not elicit weights from the model. | S7 | [E] | a02, a04, a08, b05; K03 |
| N3 | All arithmetic (means, ratios, regression, counting) runs in code, never in the model's head. | G5, S4 | [E] | a26, a27, c25, c26; K13, K16 |
| N4 | When the agent gives probabilities, aggregate several independent samples in code (trimmed mean first choice), and normalise in code. | S7, G5 | [E] | a20, b17, c17, d15; K18 |
| N5 | When an external anchor exists (a prior, a base rate, a stored class record), blend in code with a fixed weight. Do not ask the model to revise toward the anchor. | S7 | [E] | a21, b14, b19, c05; K22 |
| N6 | Do not add prompt-wording tricks (personas, "think like a superforecaster", Bayesian-reasoning prompts). Retrieval and structure come first. | 4b | [E] | c09, c10, d14; K24, K25 |
| N7 | Check the mean predicted probability against the class base rate; shrink toward base rate in code if the gap is clear. Keep extreme outputs clipped. | G-calibration, S9 | [E] | a21, c19; K21 |
| N8 | Report a trivial baseline (base rate, or a 3 to 4 feature rule) with every result. In low-ceiling classes, accept "no better than baseline" and stop spending tokens. | G7, S0 | [E] | d08, a02, c30; K08 |
| N9 | Evaluation hygiene: score probability or knowledge-heavy items only on material after the model cutoff; log dates of retrieved documents; never trust a "forget it" instruction. | G7 | [E] | d01, d02, c22, c23; K30 |
| N10 | In the S9 learning loop, keep a small random exploration slice, so that fitted weights or class records see outcomes of cases the agent did not choose. | S9, memory | [E] | d03, d04; K40 |

Note on G4. Section 4.5 shows extremizing only matters for probability aggregation over partly independent forecasters. Our bench is mostly single-answer problems, so G4 ("no extremizing votes") stays. Extremizing is in Test first only for probability outputs (T8).

### Test first

| # | Item | Schema part | Status | Evidence | Why not yet |
|---|---|---|---|---|---|
| T1 | Score-then-combine versus holistic verdict at equal tokens on reasoning items | S7 | [S] (open, no direct study) | d07, c27, a05; K37 | The one nearby test (rubrics) lost for analytic |
| T2 | Average k ratings of the same feature (k=1, 3, 5) | S7 | [S] | d06; K38 | No data on k; repeatability is not validity |
| T3 | Feature count: 3 versus 6 versus 10 criteria | S7 | none | gap 2 | No source |
| T4 | Free-form verdict allowed as one extra feature, or as tie-break | S7 | [S] | b02, d11; K06, K39 | Interview data hurt humans; no LLM study |
| T5 | Override of the code ranking only with a named, checkable reason | S7, S8 | [S] | d11; K39 | Human data only |
| T6 | Additive formula versus rule-tree over the same features | S7 | [S] | a10; K07 | One meta-analysis |
| T7 | Chain of thought on the feature scores versus direct scoring | S7 | [S] | a27; K14 | One study, tabular, older models |
| T8 | Fixed Platt or extremizing on probability outputs; factor 1.0 to 1.7 | G-calibration | [S] | c17, d09, d12; K20, K42 | Gain about .006; factor not validated for LLMs |
| T9 | Gate: defer to anchor when anchor is near 0 or 1, or when evidence count is low | S0, S7 | [S] | a19, b16; K23 | One paper |
| T10 | Diverse evidence paths for samples (different retrieval queries) versus identical-prompt samples | S3, S7 | [S] | a25; K19 | One paper; persona diversity is banned by G4, so use evidence diversity only |
| T11 | Consistency checks as a no-label diagnostic | G-consistency | [C] | c20, b26; K32 | Mixed correlation; no accuracy gain from fixing |
| T12 | Abstention: say "no better than baseline" when gap is within noise | S0, G6 | [S] | d08; K41 | Conflicts with G6 on first pass; apply only at the end |

## 8. Concrete tests on our bench

All tests use equal tokens in both arms (G7). Setup cost counts. Use at least 100 items per arm per cell where possible, and paired comparisons on the same items. Report a simple baseline in every table (N8).

| Test | Item type | Arms (equal tokens) | Metric | Expected effect |
|---|---|---|---|---|
| T1 | Multi-criterion choice items with a known answer (puzzles with several candidate solutions, brainteaser option sets) | A: one holistic verdict, with n samples and majority. B: k feature ratings per candidate (0 to 10), then code sum of unit weights. | Accuracy, paired McNemar | Small gain for B on items with 4 or more candidates (+2 to 5 points); no gain or a loss on single-answer exact items. If B loses, the split is limited to ranking steps. |
| T2 | Same items as T1 | B1: one rating per feature. B2: mean of 3. B3: mean of 5 (the token budget shrinks the number of features or candidates to stay equal) | Test-retest correlation per feature at temperature above 0; accuracy | Test-retest rises with k; accuracy gain flattens after k=3 |
| T3 | Same | 3, 6, 10 features | Accuracy | Gain from 3 to 6; flat after |
| T4 | Same | B (features only) vs B + holistic verdict as one unit-weight feature vs B with holistic as tie-break | Accuracy | Tie-break not worse; extra feature neutral or slightly worse |
| T5 | Items where code ranking and a holistic verdict disagree | Override disallowed vs override with a named, checkable reason (verified by running it) | Accuracy on disagreement items; override win rate | Win rate under 50 percent without a checkable reason; above 50 with |
| T6 | Same as T1 | Additive formula vs a model-written rule tree | Accuracy | Additive at least as good (Aegisdottir d+ -.15 vs -.03) |
| T7 | Tabular or numeric-feature items (risk scoring) | Direct score; CoT then score; feature extraction then code | AUC or accuracy against labels | CoT no better than direct; extraction then code best |
| T8 | Probability-output items with resolved outcomes (post-cutoff only) | k=10 samples: mean; trimmed mean; trimmed mean with Platt at 1.0, 1.3, 1.7 | Brier, log score, with a base-rate baseline | Mean over single sample about -.004; Platt about -.006 if under-confident, none if calibrated |
| T9 | Same | Pure model vs blend with anchor vs gated blend (anchor used when it is below .1 or above .9) | Brier | Blend beats pure model; gate adds a little |
| T10 | Single-answer or probability items | 5 samples from one prompt vs 5 samples with distinct retrieval or distinct decomposition | Accuracy or Brier | Diverse evidence paths help; same-prompt aggregation gains less (a25: .218 vs .210 for the base LM) |
| T11 | Probability items with logical structure | Compute conditional and negation violation per item; correlate with Brier | Spearman correlation | Positive for conditional, weak for negation |
| T12 | Low-signal classes | Final answer vs "baseline" label when agent gain over baseline is within CI | Net score including abstain credit | Better calibration, small score cost |

Controls: randomise candidate order per call (position bias, d06). Hold out 20 percent of each class for dev tuning of any weight or factor. Keep the exploration slice (N10).

## 9. What does not transfer, and why

- **Human clinicians' inconsistency.** The formula wins largely by removing human noise. An LLM sampled at temperature 0 is more consistent than a person, so part of the edge may shrink (critique gap 8). But samples at higher temperature or across prompt variants do vary, and test-retest above .95 can coexist with bias (d06).
- **Stakes domains.** Bail, hiring and admissions have large labelled datasets and slow outcomes. Our items have exact answers and fast checks, so our checks can often replace both the clinician and the formula.
- **Superforecaster traits and training.** Intelligence, open-mindedness and probability training apply to people. A single LLM cannot be selected or trained in-session. Selecting a configuration by past score is the analogue, and that is outside this document.
- **Teaming.** Team gains rely on independent humans sharing evidence. G4 and G9 say model samples are not independent and debate does not beat voting.
- **Extremizing.** Needs partly independent forecasters. One model's samples overlap heavily; worth testing only on probability outputs.
- **Human-AI assistance (+24 to 28 percent).** Concerns people using LLMs. No single-agent analogue.
- **Political and geopolitical questions.** The long-range experts result (Tetlock) concerns events years ahead with no feedback. Our items have immediate feedback.
- **Retrospective forecasting scores.** Leakage makes published numbers optimistic (section 5.6). Do not import them as effect sizes.
- **Benchmarks on mixed base rates.** Brier values across sets are not comparable (b28).

## 10. Open questions

1. Does "model scores, code combines" beat the model's holistic verdict on reasoning tasks at equal tokens? (K37; no paper found.)
2. How many ratings per feature, and how many features, before the gain shows? (K38; d06 shows only repeatability.)
3. Do LLM-elicited weights beat unit weights? No LLM study of a Dawes-type check found.
4. Does a holistic verdict plus override help or hurt an LLM agent? Human data say most overrides hurt (d11).
5. How many resolved questions are needed to fit Platt or extremizing, and does it transfer across domains? (d12: partial transfer, .1104 vs .1140.)
6. Do leak-free evaluations keep the 2024 to 2025 gains? Leak-free retrieval gave about zero gain in one test (d01). Hsieh's gains were not re-examined.
7. Does the edge of code combination shrink as reasoning models improve? No same-task 2023 vs 2025 comparison.
8. Can an agent be taught to abstain well in low-ceiling domains? No LLM study.
9. Primary texts of Tetlock 2005, Mellers 2014, the Grove 2000 full text and Kahneman and Klein 2009 are still unread by us.
10. Boundaries where the formula loses: small N, regime change, adversarial gaming. Not documented for LLM agents.
11. Is the Pros-versus-bots gap (c11, c13) closing or noisy? Re-check next quarter.

## 11. Sources

[V] opened and read (page or PDF text); [M] snippet or abstract only.

1. [V] Dawes (1979) The robust beauty of improper linear models. https://www.cmu.edu/dietrich/sds/docs/dawes/the-robust-beauty-of-improper-linear-models-in-decision-making.pdf
2. [V] Kuncel, Klieger, Connelly, Ones (2013) Mechanical versus clinical data combination. https://goal-lab.psych.umn.edu/orgpsych/readings/12.%20Judgment%20&%20Decision%20Making/Kuncel,%20Klieger,%20Connelly%20&%20Ones%20(2013).pdf
3. [V] Aegisdottir et al. (2006) Meta-analysis of clinical judgment project. https://gwern.net/doc/statistics/prediction/2006-aegisdottir.pdf
4. [M] Grove et al. (2000) Clinical versus mechanical prediction. https://experts.umn.edu/en/publications/clinical-versus-mechanical-prediction-a-meta-analysis/
5. [V] Armstrong and Green, review of Tetlock (2005). https://faculty.wharton.upenn.edu/wp-content/uploads/2012/08/Tetlock-16.pdf
6. [M] Tetlock (2005) Expert Political Judgment (search summaries). https://core.ac.uk/download/76362768.pdf
7. [V] Mellers et al. (2015) Identifying and cultivating superforecasters. https://stanford.edu/~knutson/jdm/mellers15.pdf and https://pdf.stafforini.com/mellers-2015-identifying-cultivating-superforecasters.pdf
8. [M] Mellers et al. (2014) Psychological strategies for winning a geopolitical forecasting tournament. https://escholarship.org/uc/item/4rg4n9vr
9. [V] Tetlock (2016) slides. https://www.nomura.com/events/10th-annual-global-quantitative-investment-strategies-conference/resources/upload/How_much_better_can_we_get_Tetlock.pdf
10. [V] Kleinberg et al. (2017/2018) Human decisions and machine predictions. https://www.nber.org/papers/w23180.pdf
11. [V] Halawi et al. (2024) Approaching human-level forecasting. https://arxiv.org/abs/2402.18563
12. [V] Schoenegger et al. (2024) Wisdom of the silicon crowd. https://arxiv.org/abs/2402.19379
13. [V] Schoenegger et al. (2024) LLM assistants improve human forecasting. https://arxiv.org/abs/2402.07862
14. [V] Karger et al. (2024/2025) ForecastBench. https://arxiv.org/abs/2409.19839
15. [V] Lu (2025) Evaluating LLMs on real-world forecasting. https://arxiv.org/pdf/2507.04562
16. [V] Hsieh, Fu, Chen (2024) Reasoning and tools for human-level forecasting. https://arxiv.org/pdf/2408.12036
17. [V] Ghaffarzadeh-Esfahani et al. (2024) LLMs vs ML on COVID-19 mortality. https://arxiv.org/pdf/2409.02136
18. [V] UK Biobank myocardial infarction LLM study (2024). https://arxiv.org/pdf/2409.14478
19. [M] Kahneman and Klein (2009) Conditions for intuitive expertise. https://pubmed.ncbi.nlm.nih.gov/19739881/
20. [V] Forecasting Research Institute blogs (2025, 2026). https://forecastingresearch.substack.com/p/ai-llm-forecasting-model-forecastbench-benchmark ; https://forecastingresearch.substack.com/p/llms-are-closing-the-gap-on-human ; https://forecastingresearch.substack.com/p/ai-models-have-likely-reached-parity
21. [V] Murphy (2026) Agentic forecasting with sequential Bayesian updating. https://arxiv.org/html/2604.18576v2
22. [V] Paleka et al. (2025) Consistency checks for LLM forecasters. https://arxiv.org/abs/2412.18544
23. [V] Paleka et al. (2025) Pitfalls in evaluating LLM forecasters. https://arxiv.org/abs/2506.00723
24. [V] Schoenegger et al. (2025) Prompt engineering LLM forecasting. https://arxiv.org/pdf/2506.01578
25. [V] Metaculus Q2 2025 AI Benchmark. https://www.lesswrong.com/posts/Surnjh8A4WjgtQTkZ/q2-ai-benchmark-results-pros-maintain-clear-lead
26. [V] Metaculus FutureEval spring 2026. https://www.lesswrong.com/posts/wZBbDqzfBjYG58CxK/futureeval-spring-results-pros-beat-bots-but-the-gap-is
27. [V] AIA Forecaster technical report (2025). https://arxiv.org/html/2511.07678v1
28. [V] Lu et al. (2025) Outcome-based RL to predict the future. https://arxiv.org/html/2505.17989
29. [V] El Lahib et al. (2026) Temporal leakage in date-filtered search. https://arxiv.org/html/2602.00758
30. [V] Li et al. (2026) Simulated Ignorance Fails. https://arxiv.org/html/2601.13717v1
31. [M] Hegselmann et al. (2022) TabLLM. https://arxiv.org/abs/2210.10723
32. [V] Zero-training LLMs on small tabular data (2025). https://arxiv.org/html/2508.17391v1
33. [V] Malin et al. (2025) LLMs less effective than local ML. https://pmc.ncbi.nlm.nih.gov/articles/PMC12012369/
34. [V] TEMED-LLM (2023). https://arxiv.org/html/2306.05052
35. [M] ClinStructor (2025). https://arxiv.org/pdf/2511.11883v1
36. [V] LoID (2026). https://arxiv.org/html/2601.17609v1
37. [V] Recht (2025) The Actuary's Final Word. https://arxiv.org/pdf/2509.04546
38. [M] Fragile Families Challenge via search. https://www.pubmed.gov/32229555/
39. [V] Salganik et al. (2020) Measuring the predictability of life outcomes. https://pmc.ncbi.nlm.nih.gov/articles/PMC7165437/
40. [V] LifeSentence (2026). https://arxiv.org/html/2606.11220v1
41. [V] De-Arteaga, Dubrawski, Chouldechova (2018) Learning under selective labels. https://arxiv.org/pdf/1807.00905
42. [V] Norman, Rivera, Hughes (2026) Reliability without validity. https://arxiv.org/pdf/2606.19544
43. [V] Huynh et al. (2026) Rubric modifications and autorater agreement. https://arxiv.org/html/2605.06283v1
44. [V] Satopaa, Pemantle, Ungar (2014) Information diversity. https://arxiv.org/pdf/1406.2148v2
45. [M] Neyman and Roughgarden (2022) Random expert aggregation. https://arxiv.org/abs/2111.03153
46. [M] Angelova, Dobbie, Yang (2023) Algorithmic recommendations and human discretion. https://www.nber.org/papers/w31747

## Source audit (2026-11-01)

Fresh auditors re-opened the sources of 18 established claims: 8 confirmed as written, 10 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **A03.08-K01** (reworded: the sources support less). Numbers verified (Grove ~10%; Aegisdottir d+ -.15/-.12; Kuncel .44 vs .28), but Grove found clinical clearly better in 6-16% of studies, so 'at least as accurate in nearly all studies' is too strong. Corrected claim: Mechanical (formula) combination of the same cues is as accurate as or more accurate than clinical/holistic combination in most studies (clinical clearly better in only 6-16% of Grove studies and about 10% of Aegisdottir), with a modest average edge (about 10% in Grove; d=-.12 to -.15 in Aegisdottir; validity .44 vs .28 for job performance in Kuncel).
- **A03.08-K03** (now single-source: the sources are not independent). Only Dawes (1979) bears the claim (random-positive-weight models about as good as judges' models and below equal weights/regression, e.g. validities .30-.51 random vs .34-.60 equal vs .38-.57 cross-validated regression); the Kuncel paper just cites Dawes, so there is one primary source; 'almost as well as fitted weights' is looser for random weights.
- **A03.08-K08** (reworded: the sources support less). Fragile Families (160 teams, best R2 ~0.2 and ~0.05, only slightly better than 4-variable benchmark) verified, but Dawes' equal-weight r=.48 and regression .38 vs committee .19 are not 'both low'; the 'depends on learnable regular environment' conditional is an inference, not shown by these sources. Corrected claim: Where outcomes are very noisy all methods are weak: in the Fragile Families Challenge 160 teams' best predictions reached holdout R2 of only about 0.05-0.2 and were only slightly better than a simple 4-variable benchmark regression; statistical combination still beat the admissions committee in Dawes' Oregon study (equal-weight r=.48, cross-validated regression .38 vs committee .19).
- **A03.08-K10** (now single-source: the sources are not independent). Mellers Table 1 (-0.34/-0.14/+0.04; learning -0.26/-0.18/0) verified and the Tetlock slides list training, teaming and aggregation as factors, but both sources are the same Good Judgment Project (Mellers and Tetlock) so it is one lab's evidence; the slide's size-of-gain chart was not legible.
- **A03.08-K15** (reworded: the sources support less). First half verified (heart accuracy xgboost 0.985 vs text-davinci-003 0.620), but TEMED-LLM shows extract-then-fit tabular models beating fine-tuned text models (xgboost AUC .998 vs set-fit .951), not trailing them by 2-3% AUC; the 2-3% cost is in neither source (the 0.02-0.04 differences in Table 3 are extracted vs ground-truth tables). Corrected claim: Having the LLM extract features and a fitted model combine them beats direct LLM classification (xgboost accuracy 0.985 vs 0.620 for direct text-davinci-003 on heart disease, TEMED-LLM) and also beat fine-tuned text classifiers in that paper; errors from extraction cost only about 0.00-0.04 AUC versus models trained on ground-truth tables.
- **A03.08-K21** (reworded: the sources support less). 57.35% mean forecast vs 14/31 resolving yes verified, but 39.3% extreme predictions is one standard-GRPO model without guardrails; the modified-GRPO model without guardrails had 7.9%. Corrected claim: LLMs show a yes/acquiescence bias (mean forecast 57.35% while 14 of 31 questions, about 45%, resolved yes), and one RL-trained forecaster (standard GRPO without guardrails) put 39.3% of its predictions in the 0-10% or 90-100% buckets (7.9% for modified GRPO without guardrails, 13.1% with guardrails).
- **A03.08-K22** (reworded: the sources support less). Schoenegger shows simple machine-human averaging beat letting GPT-4/Claude 2 update on the human median, but the '.146 vs .149' parenthetical is Halawi's 4:1 crowd-weighted blend of their system with the crowd versus the crowd alone, a different comparison. Corrected claim: Averaging model and human forecasts beat letting the model update toward the human median (Schoenegger et al.: GPT-4 and Claude 2 updated forecasts were significantly less accurate than a simple machine-human average, Brier .13 and .14); separately, Halawi et al.'s 4:1 crowd-weighted blend of system and crowd scored .146 vs .149 for the crowd alone.
- **A03.08-K24** (now single-source: the sources are not independent). Verified in Schoenegger et al.: 38 prompts (1 control + 37), 4 models, base-rate prompts slight benefit, Bayesian reasoning strong negative; but both prompt-related sources are the same paper and the Halawi entries do not test prompts.
- **A03.08-K30** (now single-source: the sources are not independent). Numbers verified (.108 vs .242 vs .244 on 93 questions; 48% of gap; gaps .086/.097 vs .064/.067), but the El Lahib et al. and Li et al. papers share most authors (same group) and Paleka et al. does not report these figures, so the numbers have no independent corroboration.
- **A03.08-K40** (reworded: the sources support less). De-Arteaga shows selective labels bias learned models and that standard selection-bias fixes are often inadequate, and Kleinberg uses quasi-random judge assignment, but neither source covers exploration and 'any formula' is wider than the semi-synthetic child-welfare test. Corrected claim: Selective labels (outcomes observed only for cases past decisions allowed) can bias models fitted on those outcomes, and standard sample-selection corrections are often inadequate (De-Arteaga et al.); remedies shown in these sources are quasi-random assignment to decision makers (Kleinberg et al.) and expert-consistency data augmentation (De-Arteaga et al.).
- **A03.08-K27** (now single-source: only one opened source, code check).
- **A03.08-K33** (now single-source: only one opened source, code check).
