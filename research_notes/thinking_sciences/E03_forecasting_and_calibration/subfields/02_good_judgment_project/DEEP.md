# Good Judgment Project: deep document

*Subfield E03.02 of forecasting and calibration: who forecasts well, and does it persist. Built from evidence_a-d.jsonl (a01-a29, b01-b29, c01-c29, d01-d20), claims.jsonl (K01-K30) and critique.md in this folder. Brier scores: Mellers 2014/2015 use the 0 to 2 scale; LLM papers use 0 to 1 (halve the former to compare). Status marks follow SCHEMA.md: [E] established, [S] single-source, [C] contested.*

## 1. What it is

The Good Judgment Project (GJP) was a research team led by Philip Tetlock, Barbara Mellers and Don Moore (Penn and Berkeley). It entered a four-year IARPA forecasting tournament (2011 to 2015). Five university teams competed. GJP won the first two years (b03). Ordinary volunteers forecast hundreds of real geopolitical events ("Will X happen by date Y?") and gave probabilities. Scores were Brier scores (squared error between the probability and the 0/1 outcome; lower is better).

The project ran randomized experiments on three levers: **training** (a short probability module), **teaming** (forecasters share news and reasons) and **tracking** (the top performers are put in elite teams). It also tested aggregation (weighting, extremizing). The top 2% of each year were labelled "superforecasters".

The subfield question is: **is forecasting skill a stable property of a person, and what predicts it?** Three sub-questions:

1. Does skill persist from year to year (a02, b09)?
2. Which traits and habits predict it (a10, a13, b11, b15, b16, b17)?
3. Which interventions raise it (a03, a11, b13)?

For our agent the questions become: does a scaffold variant that wins on one question set keep winning on a fresh set? Which human practices (base rates, updating, fine granularity, aggregation) move a language model? What do language models score on the same tasks (sections 6, 7)?

Headline persistence figures in our subfield row: year-to-year correlation .65 and about 70% of superforecasters keeping status. **Both come only from the popular book Superforecasting (p.104), quoted by the AI Impacts blog (a07, b01, c29).** They are not in Mellers 2015 or Mellers 2017 (critique C1, d05, d06). Treat them as second-hand.

## 2. History and theories in depth

**Before GJP: Tetlock 2005, Expert Political Judgment.** About 284 experts made about 28,000 forecasts from 1984 to 2003. Experts were only slightly better than chance, usually worse than simple extrapolation at 3 to 5 years. "Foxes" (many small ideas) beat "hedgehogs" (one big idea). Media-famous experts did worst (d07, K29). The book was never opened by us. These are Wikipedia-level numbers [S]. The calibration and discrimination indices are missing (open gap).

**Machine baselines before LLMs.** Zou et al. 2022 trained neural models on Metaculus, GJOpen and INFER questions: about 65% accuracy vs 92% for the human crowd (c22).

**The IARPA tournament and GJP design (Mellers 2014; a01, b03).**
- Year 1: 2,246 participants (1,593 survey, 653 market traders), about 177 per condition, attrition 7%. Year 2: 1,648, attrition 3%.
- Entry: a degree plus a 2-hour test battery. Sample: 76% US, 83% male, mean age 36, 64% postgraduate. Pay $150 (Y1), $250 (Y2), not tied to accuracy.
- 199 geopolitical outcomes over two years.
- Random assignment to training (none, scenario, probability), group influence (independent, crowd-belief poll, team), and, in Year 2, tracking.

**Theory 1: skill is partly a stable trait (Mellers 2015; b09-b12).** Pick the Year 1 top 2%, put them in elite teams, and they stay ahead in Years 2 and 3. No regression to the mean. The authors name several causes: fluid intelligence, knowledge, thinking style, motivation, plus team and workload effects. A structural model reached multiple correlation .64 (book number via AI Impacts; a06, a07).

**Theory 2: skill is trainable (Chang et al. 2016; a11-a13, b13-b15).** A module of under one hour (mnemonic CHAMPS KNOW, ten principles; comparison classes is the one we can name with evidence) cut Brier 6 to 12% against control in each of four randomized years.

**Theory 3: groups help if they share reasons (Mellers 2014; a04, b05).** Teams beat crowd-belief polling, which beat independent forecasting. This contradicted the "independence is best" idea from wisdom-of-crowds theory. Comments per member correlated with accuracy (r = -.19, -.22).

**Theory 4: aggregates need extremizing (Baron et al. 2014; Satopaa, Pemantle, Ungar 2014; a14, a15).** Averaging pulls probabilities toward .5 because of noise, and each forecaster shrinks toward .5 because they know they hold only part of the information. Pushing the mean outward fixes both. The transform is t(p) = p^a / (p^a + (1-p)^a).

**Theory 5: the traits are weak, past performance dominates (Himmelstein, Atanasov, Budescu 2021; a08-a10, b16-b19).** In the later IARPA Hybrid Forecasting Competition (HFC) trait correlations were .1 to .3. After about 20 resolved questions past performance beat all traits.

**Theory 6: good judgment is moderately unified (Mellers 2017; d05).** Superforecasters tied or beat others on consistency, discrimination and coherence lab tasks.

**Challenges.**
- Hauenstein et al. 2024 (Psychological Science, abstract only): an item-response re-analysis of the first two GJP years says the teaming and training effects depend on extraneous method variables; the best-fit models cut, remove or reverse them (d04).
- The 2020 "Superforecasting reality check" (PMC7333631): a small tournament found weak, partial persistence and no benefit of 20 extra training minutes (d01, d02).

**The LLM era (2022 to 2026).** The same research circle (Schoenegger, Tetlock, Mellers, Karger) moved the tasks to language models: LLM crowds (a22), human-AI teaming (a25), prompt tests built from the superforecaster toolkit (c09), the ForecastBench benchmark with real superforecasters (a26), and bot tournaments (c17). See section 6.

## 3. Core findings with exact numbers

Status: [E] two or more independent sources, [S] single source, [C] contested.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Superforecasters did not regress to the mean | Years 2-3 mean standardized Brier: supers -0.34, top-team individuals -0.14, all others +0.04. Resolution .40/.35/.32. Calibration .01/.03/.04. AUC 96 vs 75. | Mellers 2015 (b09; a02, b06) | [S] one group; confounded with elite teams and heavier workload (K01) |
| Supers' Brier by time window, Year 2 (0-2 scale) | first week / middle / last week: supers .25/.19/.07; regular teams no training .38/.32/.16; untrained individuals .46/.39/.26. Supers answered 95 questions vs 61 (t(270)=6.88), 7.8 forecasts per question vs 1.6. | Mellers 2014 Table 1 (a02, b06) | [S] |
| Supers learn faster and win under tough conditions | Learning slope -0.26 vs -0.18 for top-team individuals. Edge holds for first-day forecasts and forecasts made within 4 minutes. | Mellers 2015 (b10) | [S] |
| Supers stay accurate further out | Supers at 300 days beat regular forecasters at 100 days; supers at 400 days about equal regulars at about 80 days. | AI Impacts citing the book (b02) | [S] second-hand |
| Year-to-year correlation .65; 70% kept status | .65 across all forecasters; 70% of supers retained status. Structural model multiple correlation .64. | Superforecasting p.104 via AI Impacts (a07, b01, c29) | [S] book only; primary source not found (K02) |
| Independent persistence check is weaker | HFC Season 1 (326 core forecasters, 188 questions, 94/94 split): same-metric cross-half r = .36 (simple), .40-.41 (hierarchical), .36-.39 (IRT). Within-half metric agreement .71-.92. | Himmelstein 2021 (a08, b18) | [E] with the 2020 tournament (K03) |
| Tiny independent tournament | 195 engaged forecasters, 6 identification and 8 confirmation questions: 2 confirmed at top 2%; 8 / 16 / 38 at top 5% / 10% / 25%. No luck-null test. | Reality check 2020 (d01) | [S] (K27) |
| Past performance beats traits after about 20 questions | Dominance analysis, Season 1 n=216 on questions 81-188. IRT R2 about .57 at 80 questions (Season 2: .35 at 80, .53 at 200). Hierarchical .48, simple .41. | Himmelstein 2021 (a09, b19) | [S] (K04) |
| Trait correlates are small and unstable | HFC S1 (n=326): CRT .20, Number Series .15, Berlin Numeracy .15, Matrix .15, AOMT .13-.17, need for cognition .15, political knowledge .11, education .13, overconfidence -.15. S2 (n=547): Number Series .30, Berlin .25-.28, AOMT .00-.04, education -.03 to -.08. | Himmelstein 2021 (a10, b16, b17) | [E] real but small; open-mindedness and education did not replicate (K05) |
| GJP trait correlations with standardized Brier (n=1,776) | Raven -.18, Shipley abstraction -.22, extended CRT -.23, CRT -.16, numeracy -.16, active open-mindedness -.12. Supers at least 1 SD above population on Shipley-2. | Mellers 2015 Table 3 (critique 2; b11) | [E] with K05 |
| Four-year trait regressions | Standardized coefficients Y1..Y4 (negative = better): numeracy -.05,-.05,-.06,-.06; CRT -.07,-.04,-.02,-.02; Raven -.02,-.01,.00,-.01; training -.10,-.14,-.09,-.16. Motivation did not predict. | Chang 2016 Table 11 (a13) | [S] |
| Probability training works | Brier improvement over control: Y1 10% (probability) and 11% (scenario), n=119/113 vs 152; Y2 12% (t(395)=5.95, n=205 vs 194); Y3 6% (t(207)=2.32, p=.021, n=97 vs 116); Y4 7% (t(225)=2.20, p=.028). Module under 1 hour (about 45 minutes in 2014); effect lasted 8-10 months. | Chang 2016; Mellers 2014 (a03, a11, b04, b13) | [C] same group, effect shrinks; IRT re-analysis challenges Y1-2 effects (K06) |
| Training in Mellers 2014 | Y1 F(2,1586)=14.29; probability vs scenario t(1053)=2.23, p=.026; scenario vs none t(1056)=3.25. Y2 F(1,882)=19.12. | Mellers 2014 (a03) | [C] |
| Extra 20 minutes of training added nothing detectable | Group A (40 min) n=86 vs group B (60 min) n=109. Top 2%: 1 vs 1. Top 10%: 7 vs 9. Top 25%: 14 vs 24 (not significant). | Reality check 2020 (d02) | [S] |
| Only comparison classes tied to better forecasts | Y4: 6,622 control and 6,714 trained explanations; comparison-class-tagged forecasts Brier .17 vs .26 for the next-best tag. Post-mortem and some other tags linked to worse scores (reverse causation likely). | Chang 2016; AI Impacts (a12, b02) | [S] correlational, self-tagged (K07) |
| Training works partly via more updates | Mediation by forecasts per question significant in Y3 (p=.001, n=213), not Y4 (p=.20). Time spent: 4.1 h/week control vs 3.7 h trained, not different. | Chang 2016 (b14) | [S] |
| Teaming beat crowd polling beat solo work | Y1 F(2,1586)=60.68; team vs crowd-belief t(1036)=5.52; crowd vs independent t(1120)=5.92. Y2 F(1,882)=62.76. Comments per member r=-.19 (Y1), -.22 (Y2). | Mellers 2014 (a04, b05) | [C] IRT re-analysis (K08) |
| Granularity | Supers used 57 unique probability values vs 29 (top-team individuals) and 30 (others). Rounding to nearest 0.10 hurt supers' Brier; other groups' accuracy fell little or not at all. | Mellers 2015 (b12) | [S] marker or cause unknown (K09) |
| Overconfidence source | 100% forecasts in the first 20% of a question life were right about 70% of the time; late ones about 90%. Unupdated extreme forecasts drove overconfidence. Calibration improved with training F(2,1586)=3.16, p=.04. Supers gained mostly through resolution. | Mellers 2014 (a05, b07) | [S] |
| Extremizing the aggregate | High-expertise group mean a=2.43, Brier .148 vs .187 untransformed; median a=1.78, .160. Y1: 1,973 forecasters, 86 of 102 questions used. | Baron 2014 (a14) | [E] with Satopaa 2014 theory and LLM Platt results (K10) |
| Short cognitive batteries predict forecast error | Study 1: 170 Facebook recruits, 15 time-series questions: r = -.71. Study 2: 1,194 people, 36 questions: r = -.67 out of sample. | Merkle 2025 (a18, b20) | [S] lay sample, matched tasks (K22) |
| Superforecasters in lab tasks | Cross-measure correlations .08-.39 (mean .20). Composite related to super status at .46 and .60 (.73 and .82 corrected for unreliability). Survey 1: 173 supers, 75 regulars, 92 undergraduates. | Mellers 2017 (d05) | [S] (K28) |
| Logical consistency predicts later Brier | Violation vs Brier correlation 0.85 (frequentist) and 0.49 (arbitrage) in one plot, 0.92 and 0.69 in another; some checks R above 0.9, others near zero. Training for consistency did not raise accuracy. | Paleka 2024 (b27, c27) | [E] 2 sources (K21) |
| XPT: long debate did not converge views | 169 forecasters (80 domain experts, 89 supers); disagreement largest on AI risk; neither side moved much after months. | FRI XPT page (b28) | [S] project page only |

## 4. Mechanisms and models

Written so an engineer could implement each piece.

### 4.1 Brier score and its decomposition
Brier = mean over questions of (p - o)^2 with o in {0,1}. On the 0-1 scale a coin flip (always .5) scores .25. Decompose into calibration (does "70%" come true 70% of the time) and resolution (do forecasts separate outcomes). Mellers 2015: supers gained mostly through resolution (.40 vs .32), while calibration differences were tiny (.01 vs .04). Implementation: log (question id, p, outcome); compute reliability over 10 bins; resolution = variance of bin hit-rates around the base rate.

### 4.2 Standardizing within question
GJP standardized Brier within each question to remove question difficulty. Implementation: z = (Brier_i - mean_q) / sd_q across forecasters on question q. For our agent: compare arms **paired by question**. Murphy 2026 found question identity explains 62.2% of score variance and method only 2.7% (d16).

### 4.3 Persistence test (split-half and retest)
Himmelstein's protocol: rank forecasters on set A, correlate with the same metric on set B. HFC: r = .36-.41 on 94 questions per half (b18). For an agent variant: score each variant on two disjoint question sets, compute Spearman r between variant scores. Do this before trusting any ranking of prompts.

### 4.4 Item response model for accuracy
Himmelstein fit IRT-style models (forecaster ability, question difficulty) and got cross-half r .36-.39, about as stable as simple averages (b18). Simple means are enough when everyone answers the same questions; IRT or a mixed model (score ~ forecaster + question) helps when they answer different ones.

### 4.5 Extremizing as Platt scaling
Aggregate p-bar from N forecasts. Convert to log-odds, multiply by a constant a, convert back: t(p) = p^a / (p^a + (1-p)^a). Theory: partial information overlap (Satopaa 2014, a15). GJP fit a = 2.43 (high expertise, mean) and 1.78 (median) on Year 1 data, in-sample (a14). For LLM ensembles (AIA Forecaster, d13): a fixed a = sqrt(3) = 1.73 moved Brier .1119 to .1076; fitted leave-one-out .1071; fitted on another benchmark .1104. The best a was 1.72 for supers and 2.27 for the AIA system. Murphy 2026 (d17) found no resolved gain once a crowd price was in context, and cross-validated shrinkage chose none. Rule: apply only when no external crowd anchor is in the prompt; refit on held-out data.

### 4.6 Training mechanism (CHAMPS KNOW)
Chang 2016 mediation: training helps through more forecasts per question (more updating), not more time. Only the comparison-class principle showed a measured payoff. Engineer reading: the module teaches (1) a base rate from a reference class, (2) adjust on news, (3) use finer numbers. For LLMs only item (1) shows a signal (section 6.4).

### 4.7 Teaming as shared-reasons aggregation
Mellers 2014: team members posted news and rationales. Teams beat independent forecasters. The agent analogue: sample N attempts, let each see the others' rationales, revise, then aggregate. This is the opposite of schema rules G4/G9 (isolated attempts, no debate). See K08 [C] and section 7 "Test first".

### 4.8 Track record as a predictor
Himmelstein: after 20 resolved questions the forecaster's own record beats traits; at 80 the IRT model reaches R2 .57 (Season 1). Implementation: keep a running per-domain mean Brier; weight aggregation by it, or shrink toward the base rate when it is poor. No LLM study of giving the agent its own record exists (K30).

### 4.9 Consistency checks
Paleka 2024: ask the negated question ("not X"), a paraphrase, or a conditional; measure the violation (for example p(X) + p(not X) - 1, or an arbitrage gap). Violation rate correlates with later Brier (up to r .92). Implementation: two extra calls per question; log the gap. Training on consistency did not improve accuracy (c27), so use it as a filter or confidence hint, not a trainer.

### 4.10 Power calculation for comparing scaffolds
N = ((1.96 + 0.84) * SD / delta)^2 for a paired two-sided test at 5% size and 80% power (d19, our derivation). With paired SD .10 to .15 per question: delta .02 needs about 200 to 440 questions; delta .01 needs about 650 to 1,460. Using 5 to 10 samples per question lowers the SD.

## 5. What holds up

### 5.1 Replications and independent checks
- **Persistence:** replicated in direction by HFC (r .36-.41) and by the small 2020 tournament (2 at top 2%), but at lower strength than the .65 headline [E for existence, S for the size] (K03, K27).
- **Past record beats traits:** one source (Himmelstein) [S].
- **Trait correlates:** fluid intelligence and numeracy hold across GJP and HFC (r .15-.30); active open-mindedness and education do not (AOMT .13-.17 in S1, .00-.04 in S2; education reversed sign) [E] (K05).
- **Extremizing:** theory plus GJP fit plus LLM ensembles, but the best factor drifts (1.72 vs 2.27) and a crowd anchor removes the gain [E for the effect, C for the factor] (K10, K26).
- **Aggregation for LLMs:** averaging 10 samples of one system beats one sample (.1140 vs .1182), diminishing after about 5; mixing models beats repeating the best model at a fixed sample count (N=113) [E] (K24). The 12-model crowd result is one study of 31 questions [S].

### 5.2 Failed, weakened or contested results
- **Training effect:** shrank from 10-12% (Y1-2) to 6-7% (Y3-4). No outside RCT. Hauenstein 2024 says it shrinks or reverses with method variables controlled. The 2020 tournament found no gain from 20 extra minutes. [C] (K06).
- **Teaming effect:** same re-analysis challenges it [C] (K08).
- **Trait stability:** open-mindedness scale alpha .24 in HFC Season 2; education flipped sign. [E] (K05).
- **Automated prompt optimizer:** large gains on old questions (about 18 points on GPT-4.1-nano) did not hold live (+2.76 vs baseline +4.71 per question over 351-354 questions; null on n=278) (c21). A failed replication of a retrospective gain.
- **Superforecaster persona and Bayesian prompts in LLMs:** failed (section 6.4).
- **Lu 2025 "experts beat o3":** compares a median of expert Brier (.0225) against the models' mean (.1352); the experts' mean is .1573 (157 q) and .1222 (41 q). Not established [C] (K20, critique C2).
- **Leakage:** at least 3.8% of Halawi questions resolved early; at least 10% of Tao et al. were trivial given the cut date (a28, c28). Some LLM-vs-human claims are inflated.

### 5.3 Moderators and boundary conditions
- **Confounds in persistence:** supers got team support, extra workload and a label (Mellers 2015 acknowledges) (K01).
- **Sample:** volunteers, 83% male, 64% postgraduate (a01). In the reality-check tournament, top-quartile membership was linked to male sex, 16-20 years of experience, daily news reading and English-language sources (d03).
- **Time horizon:** supers lose less accuracy at long horizons (b02).
- **Task match:** cognitive batteries reach r about -.7 only when tests match the task (time series, lay samples), not the .1-.3 seen in HFC/GJP (K22).
- **Ability x training:** only Y1 showed it (abler forecasters gained more) (b15).
- **Small N:** the top 2% is a thin tail; 195 forecasters gave 2 confirmed. Lu notes a noisier forecaster still wins 24% of 50-question tournaments at a 6.5% true gap (a29; second-hand, untraced).

### 5.4 Interventions that worked (humans)
Training (6-12%), teaming, tracking into elite teams, aggregation with extremizing, more frequent updating, comparison classes, finer probability steps (a marker), and an LLM assistant (+24-28% in N=991; K17).

### 5.5 Interventions that did not
Extra 20 minutes of training; motivation measures; time spent; post-mortems (negative association); rounding probabilities to 0.1 for supers; long structured debate in XPT (no convergence).

## 6. Language models

All figures use the 0-1 Brier scale; 0.25 is a coin flip.

### 6.1 Plain models
| Study | Setting | Result | Source |
|---|---|---|---|
| Schoenegger and Park 2023 | GPT-4 in a Metaculus tournament Jul-Oct 2023, 843 humans | GPT-4 .20 (SD .18) vs human crowd median .07 (SD .08); t(44)=3.11, d=.94; no better than always saying 50% | a24 |
| Halawi 2024 | 14 LLMs, no retrieval, post-cutoff questions from 5 platforms (dataset 48,754 questions, 7.17M forecasts; test set from June 2023) | best GPT-4-1106 .208 vs crowd .149 vs random .250 | a19, c01 [S] |
| Zou 2022 | neural models | 65% vs 92% crowd | c22 |

### 6.2 Scaffolds: retrieval, ensembles, tools
- **Halawi system** (query writing, news retrieval, several reasoning prompts, trimmed-mean ensemble, fine-tune on 13,253 self-generated reasoning samples kept only if they beat the crowd): Brier .179, accuracy 71.5% vs crowd 77.0% and .149. Ablation: no fine-tune .186; neither fine-tune nor retrieval .206 (baseline .208). **Retrieval carries most of the gain** (differences of .003-.007 are near standard error; table row labels partly garbled, critique C4). Averaging with the crowd (4x weight) gave .149 to .146. It beats the crowd only when the crowd is unsure (validation .199 vs .246 for crowd in .3-.7), and hedges away from 0 and 1 when the crowd is sure (accuracy +7% but Brier .04 worse). [S] (K11, K12).
- **Hsieh et al. 2024** ReAct agent (search plus Python): mean of 3 Brier .170 (73.9%); Halawi-style GPT-4o .177; plain GPT-4o .210; ensemble of 3 .169 vs single .180 (c24).
- **AIA Forecaster 2025:** single sample .1182, mean of 10 .1140, median .1138; supervisor that searches on disagreement .1125 vs non-agentic .1168 vs best-of-k .1191 vs none .1199; Platt 1.73 .1119 to .1076. On FB-7-21: AIA .1076 vs supers median .1110, public .1451, o3 .133. On FB-8-14: .1099 vs .1152. On liquid markets AIA .0753 vs supers .0740 vs market .0965 (d11-d14). On mean Brier over the same questions, the best scaffolded LLM matched supers. [S]
- **Metaculus bot-vs-Pro tournaments:** Pros led best bots every quarter: -11.3 (Q3 2024, p=.036), -8.9 (Q4 2024, p=.079), -17.7 (Q1 2025, p=.0007), -20.0 (Q2 2025, p=.00001) peer points. A scaffolded gpt-4o bot placed 8th, the plain template 44th (avg spot peer score 5.51 vs -5.53). Survey of 39 bot makers: winners used 1.75 research sources vs 1.00 (r=.42, p=.006), 86% aggregated, about 28 LLM calls vs 7; top-five scaffolded bots beat their plain baseline by 5-11 peer points; multiple personas called a mistake (c17-c20). Correlational survey, not an equal-token test. [S]

### 6.3 LLM crowds and human-AI mixes
- **Wisdom of the silicon crowd:** median of 12 LLMs Brier .20 (SD .12) vs 925 humans .19 (SD .19), t(60)=0.19, p=.850; vs .25 benchmark t(30)=-2.35, p=.026; equivalence bound .081 passed. Individual models: GPT-4 .15, GPT-4 with Bing .16, Bard .19, Falcon-180B .21, Claude 2 .21, Mistral-7B .24, Llama-2-70B .25, Coral .38. Acquiescence bias: median forecast 60%, about 45% resolved yes. Showing the human median to GPT-4 and Claude 2 improved them 17-28% (GPT-4 .17 to .14, Claude 2 .22 to .15), but plain human-machine averaging was better. Update size correlated with distance to the human median (r = .88, .87) (a22, a23, c05-c07). [S]
- **Diversity paper (N=113 questions):** at a fixed sample count, different models beat repeated samples of the best model because frontier LLM probabilities are highly correlated (d15).
- **AI-augmented humans:** N=991, six questions, +24% to +28%; without one outlier item +41% (superforecasting assistant) and +29% (noisy assistant); the control was a weaker model with no numbers (a25, c08). [S]

### 6.4 Prompts that copy human practice
Schoenegger, Jones, Tetlock, Mellers 2025 (c09, c10, d08, d09): 38 prompts on four LLMs (Claude 3.5 Sonnet, Claude 3.5 Haiku, GPT-4o, Llama 3.1 405B) on ForecastBench, about 3,636-3,771 usable forecasts per model.
- Preregistered mixed model, Benjamini-Hochberg corrected: only two prompts differ from control and both are **worse** (Bayesian Reasoning +0.030, t=5.4, p<.001; Propose-Evaluate-Select +0.033, p<.001). All others within about +/-0.011, adjusted p at least .77.
- In paired t-tests three base-rate-style prompts survive correction with small gains (Frequency-Based, Base Rate First -0.016, Step-Back). The earlier summary "none beat noise" was too strong (K16 corrected).
- Study 2 compound prompts and outside prompts: negligible gains, including on reasoning models.
- Harmful prompts pushed forecasts farther from 0.5 (mean distance 17.2-19.9 points vs 11.9-13.4 for control), but chain of thought did too and was not significantly harmful, so distance alone does not explain the harm.
- Pratt 2024 (Google-internal set, human Brier .1334): personas and added news were worse than baseline; models guess low probabilities for most events, which looks like skill when most events do not happen (c23).
- Lu 2025 prompted models "you are a superforecaster": o3 .1352 (mean of 5 calls), o3-pro .1386, GPT-4.1 .1542, o4-mini .1589, DeepSeek-V3 .1798, Claude 3.6 Sonnet .1810, GPT-4o .1883 (c11, c12). No persona-free control, so the prompt effect is unknown.
- Conclusion: the human training does not transfer as a prompt, except the reference-class idea.

### 6.5 Training instead of scaffolding (out of scope)
Turtel et al.: DPO on self-generated reasoning pairs ranked by outcome distance gave +7-10% accuracy on two 14B models (12,100 questions); Brier-reward RL gave .190 for a 14B model (CI .178-.203), matching o1, but market price stayed better by about .04 (c25, c26). Not for a scaffold-only agent. Calibration layers (Platt) are scaffold-compatible.

### 6.6 Benchmarks and the human gap
- ForecastBench (Karger et al.): 200-question subset: supers .096 (39 supers, about 8 forecasts per question), public (500) .121, best LLM Claude 3.5 Sonnet .122 (all p<.001). Dataset-question subset .076 / .096 / .130. Best LLM vs Chatbot Arena: y = 0.506 - 0.000298x (R2 .47), parity near Arena 1406 (CI 1346-1633); vs log compute R2 .41 (a26, c13, c14).
- FRI update (29 Jan 2026): supers lead the best LLM by .017 difficulty-adjusted Brier (about one year of progress); Claude 3.5 Sonnet (Oct 2024) .117; Grok 4.20 preview (Oct 2025) .102; improvement about .015 per year; parity extrapolated late 2026 to mid 2027 with wide intervals. The Brier Index version (snippet only) says 70.6% vs 67.9% and parity about May 2027 (b25, c15, c16).
- Lu 2025: 464 Metaculus questions; o3 passes published crowd baselines (.149 and .121 from other sets) but the expert comparison is not apples to apples (a27, d10; K20 [C]).

### 6.7 Other measured LLM properties
- **Consistency** predicts Brier (K21 [E]).
- **Memory within a question:** a compact belief state (probability plus evidence summary) matched full history: Brier Index 75.12 vs 72.72, difference +2.40, 95% CI [-0.17, 4.36], 100 questions, K=2 (d18). Cross-question track records are untested (K30).
- **Skill distillation:** EvoForesight reports up to 195% rating improvement on FutureX from turning resolved trajectories into skills (abstract only; rating, not Brier; d20).
- **Sampling:** averaging K=5 trials improves Brier Index; logit averaging adds a small gain (d17).

## 7. What our agent should take

Schema parts: G guardrail, S state, O operator, memory. Evidence ids refer to the jsonl files; K ids to claims.jsonl.

### Add now (established)
1. **Never rank two variants on one small question set; check retest and use paired designs.** Evaluation protocol, G7. [E] K03 (a08, b18, d01), K23 (d16, d19; K23 itself is single-source, so the retest half rests on K03). Human split-half r was only .36-.41; question identity explains 62.2% of score variance. Size sets with section 4.10.
2. **For probability outputs, aggregate several isolated samples in code, then recalibrate only on held-out data, and only when no external crowd price is in the prompt.** G4/G5, O (sample-and-aggregate), S7. [E] K10 (a14, a15, b07, c21, d13, d17), K24 (d11, d15, d17). Mean of independent samples beats a single sample (.1182 to .1140), diminishing after about 5; mixed models or pipelines beat repeats. The extremizing factor drifts (1.72 vs 2.27), so refit. G4's "no extremizing votes" concerns single-answer problems; this applies to probabilities.
3. **Do not add persona or Bayesian-reasoning prompts for probability tasks.** Add to section 4b. [E] K16 (c09, c10, c23, d08, d09). Bayesian prompt +0.030 Brier (worse); Pratt found personas and added news worse.
4. **Log forecasting-specific data and use only post-cutoff questions.** S9, schema section 6: question id, p, outcome, retrieval date; report Brier relative to a base-rate forecaster. [E] K19 (a28, b26, c28, d10, d16).
5. **Consistency gap (negation or paraphrase) as a cheap uncertainty hint, never as proof.** G (consistency), G4. [E] K21 (b27, c27). Gap correlates with later Brier up to R .92; training on it did not help, so do not optimise against it.

### Test first (single-source or contested)
| # | Idea | Schema part | Status | Evidence |
|---|---|---|---|---|
| T1 | Base-rate-first (reference class) step before any forecast, ablated alone from the full checklist | O (base-rate operator) | [S] | K07 (a12, b02, b15); K16 (d08: -0.016 paired) |
| T2 | Retrieval vs no retrieval vs retrieval plus ensemble at equal tokens | S3/S4 | [S] | K11, K12, K15 (a19-a21, c01-c04, c17-c20) |
| T3 | Teaming analogue: samples see each other's rationales and revise, vs isolated samples | O / G4, G9 | [C] | K08 (a04, b05, d04) |
| T4 | Disagreement-triggered evidence search (supervisor) | O (disagreement step) | [C] | K25 (d12, d17) |
| T5 | Running per-domain Brier history in context | memory | [S] | K04, K30 (a09, b19, d18, d20) |
| T6 | Output granularity: 0.01 vs 0.1 rounding; never emit unrefined 0/100 early | G (precision) | [S] | K09 (b12), K10 (b07) |
| T7 | Fixed extremizing 1.73 vs fitted vs none | G (calibration) | [C] | K26 (d13, d17) |
| T8 | Heterogeneous ensemble (different prompts or retrieval paths) vs repeated samples at equal tokens | O | [S] | K13, K24 (c05, d11, d15) |
| T9 | Consistency filter before aggregation | G | [S] as a filter | K21, K28 |
| T10 | Spread control: limit how far prompts push forecasts from the base rate | G | [S] | K16 (c10, d09) |
| T11 | Pick best scaffold on set 1, re-run on set 2 (retest of variant ranking) | evaluation | [S] | K01, K02 |

## 8. Concrete tests on our bench

Common rules: both arms at equal total tokens (count every call including retrieval summaries and setup, per G7). Questions: only items opened after the model cutoff or resolved after the run; log retrieval dates. Paired by question. Report mean Brier difference with a paired bootstrap CI, plus Brier relative to an always-base-rate forecaster. Set size from section 4.10 (200-450 questions for a 0.02 gap). If the bench has no live forecasting items, use resolved archival questions with a post-cutoff filter and an explicit leakage check; for non-probability items use the analogous accuracy metric.

| # | Test | Item type | Arms (equal tokens) | Metric | Expected effect |
|---|---|---|---|---|---|
| 8.1 | Retest of variant ranking | binary forecasting, two disjoint sets of 150+ | 4 to 6 scaffold variants run on both sets | Spearman r of variant scores across sets; stability of the winner | r near .4 to .6 expected from humans (.36-.41); tells us the minimum set size |
| 8.2 | Sample count at equal tokens | binary forecasting | A: 1 long chain (N tokens). B: 5 short samples of one prompt (N/5 each), mean. C: 5 short samples with different prompts or retrieval paths, mean | Mean Brier, paired | C better than B better than A; B vs A about .004 (cf. .1182 to .1140); C vs B unknown |
| 8.3 | Retrieval ablation | binary forecasting needing current facts | no retrieval / retrieval / retrieval plus 5-sample mean | Brier; Brier by crowd-uncertainty bin if a crowd price exists | retrieval gives most of the gain (Halawi .208 to about .186); ensemble adds .005 to .01 |
| 8.4 | Base-rate-first step | binary forecasting | plain prompt vs one-step reference-class prompt vs full CHAMPS-style checklist | Brier, paired, multiple-comparison corrected | about -0.016 for base-rate-first; checklist no better than that step |
| 8.5 | Extremizing | probability from an N-sample mean | none / fixed 1.73 / factor fitted on a separate set; with and without a crowd price in the prompt | Brier on held-out set | about -.004 (.1119 to .1076) without anchor; none with anchor |
| 8.6 | Track record in context | stream of questions with domain tags, two halves | no record vs per-domain table of own Brier and hit-rate, second half | paired Brier on second half; calibration slope | unknown; human analogue says record beats traits after 20 questions. Small gain or noise |
| 8.7 | Teaming analogue | binary forecasting | isolated 5-sample mean vs 5 samples that read each other's rationales once, then revise | Brier; correlation of errors across samples | contested; G4 predicts no gain or a loss from correlated error |
| 8.8 | Disagreement-triggered search | items where samples disagree beyond a threshold | mean vs supervisor that retrieves evidence on disagreement | Brier on the disagreeing subset | -.007 (.1199 to .1125 in AIA) or none (Murphy) |
| 8.9 | Granularity | any probability output | rounded to 0.1 vs 0.05 vs 0.01 | Brier | rounding to 0.1 costs a little |
| 8.10 | Consistency filter | binary forecasting | mean of all vs mean of low-gap samples vs fallback to base rate on high-gap items | Brier; correlation of gap with Brier | correlation 0.5-0.9; filter gain small |
| 8.11 | Spread control | binary forecasting | Bayesian-style prompt with and without shrinkage toward the base rate | Brier | tests whether the harm in section 6.4 is overdecisiveness |

## 9. What does not transfer, and why

- **Trait findings** (fluid intelligence, numeracy, CRT, open-mindedness, education, news habits). They describe differences between people. An agent has one fixed model. Closest analogue: a stronger base model scores better (ForecastBench: Brier tracks Arena rating, R2 .47).
- **Superforecaster persistence as a selection method.** We have no population of agents with shared life experience. A prompt variant's score is also a property of the question set (62.2% question, 2.7% method).
- **Training as a lasting skill.** Human effects lasted 8-10 months because humans learn. A prompt has no memory beyond its context and showed no gain except base rates.
- **Persona ("you are a superforecaster").** Failed in 38-prompt tests; it adds no information (c09, c23).
- **Teaming with social effects.** Human teams share news, motivation and accountability. Same-model samples share errors (frontier LLM probabilities are highly correlated, d15). G9 stands unless T3 shows otherwise.
- **Motivation, time spent, pay.** No agent analogue, and no predictive power in humans (a13, b14).
- **Long debate.** XPT showed no convergence in humans and G9 bans it.
- **Training-time fixes** (DPO, RL on Brier) are not scaffold changes.
- **Tournament artefacts** (leaderboards, early 100% forecasts).
- **The .65 and 70% numbers** themselves: unsourced, from volunteers with team support. Not a target for any measurement.

## 10. Open questions

1. What is the real test-retest of a scaffolded LLM forecaster's Brier across disjoint question sets? Unpublished (critique gap 1). Murphy: method explains 2.7% of variance.
2. Does sample-and-aggregate beat one long chain at equal tokens? Evidence for 10x sampling and model diversity; none at equal tokens (gap 2).
3. Does a running per-domain track record help an LLM agent? Untested (K30, gap 3).
4. What is the primary source of .65 and 70%? Not in Mellers 2015, 2017, or the 2020 reality check (gap 4).
5. What exactly do Hauenstein et al. 2024 find about teaming and training? Only the abstract was read; effect sizes missing (gap 5).
6. Was the Lu 2025 comparison redone with mean Brier on identical questions? Not found (gap 6).
7. Which CHAMPS KNOW elements besides comparison classes (granularity, update frequency) transfer as operators? Untested (gap 7).
8. Does the extremizing factor drift across ensembles and question sources (1.72 vs 2.27)? (gap 8)
9. Tetlock 2005 primary indices (calibration, discrimination, fox vs hedgehog) were never read (gap 9).
10. Does the Bayesian-prompt harm come from overdecisiveness or something else? Chain of thought is equally decisive but not harmful.
11. Do LLM-crowd results hold beyond 31 questions with the acquiescence bias controlled?
12. Do ForecastBench parity projections (late 2026 to mid 2027) hold? They rest on linear extrapolation from few models.

## 11. Sources

[V] = opened and read (evidence line opened:true); [M] = snippet, abstract only or second-hand.

- [V] Mellers et al. (2014) Psychological strategies for winning a geopolitical forecasting tournament. https://escholarship.org/content/qt4rg4n9vr/qt4rg4n9vr_noSplash_4ff67e56b3dac616e0163b75090705e6.pdf and https://journals.sagepub.com/doi/10.1177/0956797614524255 (a01-a05, b03-b08)
- [V] Mellers et al. (2015) Identifying and cultivating superforecasters. https://pdf.stafforini.com/mellers-2015-identifying-cultivating-superforecasters (b09-b12; a06 was a snippet line, corrected by critique C1)
- [V] Chang, Chen, Mellers, Tetlock (2016) Developing expert political judgment. https://journal.sjdm.org/16/16511/jdm16511.pdf and https://cambridge.org/core/services/aop-cambridge-core/content/view/123EB1842539 (a11-a13, b13-b15)
- [V] Himmelstein, Atanasov, Budescu (2021) Forecasting forecaster accuracy. https://doi.org/10.1017/S1930297500008597 (a08-a10, b16-b19)
- [V] AI Impacts, Evidence on good forecasting practices from the Good Judgment Project. https://aiimpacts.org/evidence-on-good-forecasting-practices-from-the-good-judgment-project/ and https://aiimpacts.org/?p=1283 (a07, b01, b02, c29)
- [V] Baron, Mellers, Tetlock, Stone, Ungar (2014) Two reasons to make aggregated probability forecasts more extreme. https://faculty.wharton.upenn.edu/wp-content/uploads/2015/07/2015---two-reasons-to-make-aggregated-probability-forecasts-more-extreme.pdf (a14)
- [V] Satopaa, Pemantle, Ungar (2014) Combining probability forecasts and understanding probability extremizing. https://arxiv.org/pdf/1406.2148v1 (a15)
- [V] Merkle et al. (2025) Identifying good forecasters via adaptive cognitive tests. https://arxiv.org/abs/2411.11126 (a18, b20)
- [V] Mellers, Baker, Chen, Mandel, Tetlock (2017) How generalizable is good judgment? https://jbaron.org/journal/17/17408/jdm17408.pdf (d05, d06)
- [V] Superforecasting reality check: evidence from a small pool of experts and expedited regression (2020). https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7333631/ (d01-d03)
- [M] Hauenstein, Thomas, Illingworth, Dougherty (2024/2025) Rethinking the role of teams and training in geopolitical forecasting, Psychological Science. https://doi.org/10.1177/09567976241266481 (d04, abstract only)
- [V] Halawi, Zhang, Yueh-Han, Steinhardt (2024) Approaching human-level forecasting with language models. https://arxiv.org/abs/2402.18563 (a19-a21, b21, b22, c01-c04)
- [V] Schoenegger, Tuminauskaite, Park, Tetlock (2024) Wisdom of the silicon crowd. https://arxiv.org/abs/2402.19379 (a22, a23, b23, c05-c07)
- [V] Schoenegger and Park (2023) Large language model prediction capabilities. https://arxiv.org/abs/2310.13014 (a24)
- [V] Schoenegger, Park, Karger, Trott, Tetlock (2024) AI-augmented predictions. https://arxiv.org/abs/2402.07862 (a25, c08; abstract plus partial read)
- [V] Schoenegger, Jones, Tetlock, Mellers (2025) Prompt engineering large language models' forecasting capabilities. https://arxiv.org/abs/2506.01578 (c09, c10, d08, d09, d19)
- [V] Karger et al. (2025) ForecastBench. https://arxiv.org/abs/2409.19839 (a26, b24, c13, c14)
- [V] Forecasting Research Institute (2026) LLMs are closing the gap on human superforecasters. https://forecastingresearch.substack.com/p/llms-are-closing-the-gap-on-human (b25, c15)
- [M] FRI / Good Judgment commentary (2026) Brier Index. https://forecastingresearch.substack.com/p/introducing-the-brier-index (c16, search summary only)
- [V] Lu (2025) Evaluating LLMs on real-world forecasting against expert forecasters. https://arxiv.org/abs/2507.04562 (a27, a29, c11, c12, d10)
- [V] Paleka, Goel, Geiping, Tramer (2025) Pitfalls in evaluating language model forecasters. https://arxiv.org/abs/2506.00723 (a28, b26, c28)
- [V] Paleka et al. (2024) Consistency checks for language model forecasters. https://arxiv.org/abs/2412.18544 (b27, c27)
- [V] Metaculus (2025) Q1 2025 AI Benchmark Results. https://www.metaculus.com/notebooks/38673/q2-ai-benchmark-results/ (c17, c18)
- [M] LessWrong synthesis of Metaculus analyses (2026) AI forecasting in 2026. https://www.lesswrong.com/posts/a82q6yd8zKpYk56cF/ai-forecasting-in-2026-what-11 (c19-c21; secondary source, opened but treat numbers as second-hand)
- [V] Zou et al. (2022) Forecasting future world events with neural networks. https://arxiv.org/abs/2206.15474 (c22)
- [V] Pratt et al. (2024) Can language models use forecasting strategies? https://arxiv.org/abs/2406.04446 (c23)
- [V] Hsieh, Fu, Chen (2024) Reasoning and tools for human-level forecasting. https://arxiv.org/abs/2408.12036 (c24)
- [V] Turtel, Franklin, Schoenegger (2025) LLMs can teach themselves to better predict the future. https://arxiv.org/abs/2502.05253 (c25)
- [V] Turtel et al. (2025) Outcome-based reinforcement learning to predict the future. https://arxiv.org/abs/2505.17989 (c26)
- [V] Alur et al. (2025) AIA Forecaster: technical report. https://arxiv.org/abs/2511.07678 (d11-d14)
- [V] Aitchison, Jeen, Shevlane, Day (2026) Diversity is the strength of the silicon crowd (id as logged). https://arxiv.org/abs/2606.29661 (d15)
- [V] Murphy (2026) Agentic forecasting with structured linguistic beliefs. https://arxiv.org/abs/2604.18576 (d16-d18)
- [M] EvoForesight (2026) Evolving with open worlds. https://arxiv.org/abs/2610.29784 (d20, abstract only)
- [V] Forecasting Research Institute: Existential Risk Persuasion Tournament. https://forecastingresearch.org/xpt (b28; project page, no accuracy numbers)
- [M] Tetlock (2005) Expert Political Judgment. https://press.princeton.edu/books/paperback/9780691128719/expert-political-judgment (a16, b29; not opened)
- [M] Tetlock and Gardner (2015) Superforecasting. https://www.penguinrandomhouse.com/books/227815/superforecasting-by-philip-e-tetlock-and-dan-gardner/ (a17; not opened; .65 and 70% reach us via AI Impacts)
- [M] Wikipedia: Philip E. Tetlock. https://en.wikipedia.org/wiki/Philip_E._Tetlock (d07; secondary)
- Derived: power calculation (d19), our arithmetic from d08 standard deviations; not a source.
