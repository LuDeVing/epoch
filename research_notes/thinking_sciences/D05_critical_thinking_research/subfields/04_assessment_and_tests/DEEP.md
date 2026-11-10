# Assessment and tests: deep document

*Subfield D05.04. Standardised tests of critical-thinking skills (Watson-Glaser, Cornell, CCTST and kin) and what they mean for a scaffolded language-model agent. Built from evidence_a-d.jsonl (ids a01-a32, b01-b27, c01-c28, d01-d20), claims.jsonl (K01-K30) and critique.md in this folder. Status marks follow SCHEMA.md: [E] established, [S] single-source, [C] contested. No LLM study of the official Watson-Glaser, Cornell or CCTST was found, so the LLM evidence rests on open proxies (LSAT family, LogiQA, ReClor, CRT).*

## 1. What it is

A standardised critical-thinking (CT) test gives many people the same items under the same rules and turns answers into a score. Most are multiple choice, so a computer can grade them. A few are open (essay or document-based performance tasks) and need trained raters.

The main instruments:

- **Watson-Glaser Critical Thinking Appraisal (WGCTA).** Five parts: Inference, Recognition of Assumptions, Deduction, Interpretation, Evaluation of Arguments. Two forms of 80 items, optional 40-minute limit, Grade 9 and up (a15). The 2026 Slovak form has 79 items (b01).
- **Cornell Critical Thinking Tests.** Level X: 71 questions, 50 min, Grade 7+. Level Z: 52 questions, 50 min, college. Built on Ennis's view: induction, source credibility, deduction, assumptions. Level Z adds equivocation, definition, hypothesis testing, gaps in arguments (a16).
- **California Critical Thinking Skills Test (CCTST).** 34 scored items (35 piloted) from a bank of 200. Skills: interpretation, analysis, evaluation, inference, explanation (a04, a05, b05).
- **Others:** Ennis-Weir essay test, Test on Appraising Observations, ACT CAAP (a03), New Jersey Test of Reasoning Skills (50 items claiming 22 skills, a17), HCTA, Collegiate Learning Assessment and CLA+ (a11, a20), TSA (b07), PACIER (b09).

What a test is for: to rank people, track gain after teaching, or screen. For our project the question is different. We want a **gate and a log**: an S0 check that says what mode to use, and a set of items on which we can measure whether the scaffold helps at equal tokens. So this document asks two things. How trustworthy are these tests as measuring tools, and which of their features can we borrow for a machine bench.

The short answer from the evidence: the total score is moderately reliable, the sub-scores are not, the tests overlap heavily with verbal ability, and strong LLMs already beat most humans on the open proxy sets. The tests are useful as item formats and as a warning about measurement, much less as a gate.

## 2. History and theories in depth

**The Delphi consensus (1990).** Facione ran a Delphi panel of 46 experts over six rounds (Feb 1988 to 1989) for the APA. Over 95% agreed that analysis, evaluation and inference are core. About 87% agreed that interpretation, explanation and self-regulation are central (a01). One assessment expert dissented on interpretation (it is communication). Another said self-regulation cannot be tested with paper and pencil. The panel gave four criteria for any CT test: content validity, construct validity, reliability, fairness. It said items where good thinking gives a wrong answer, or poor thinking a right one, should be removed (a02). It also admitted that nobody knew whether sub-skills correlate.

**Test lineages.**
- Watson-Glaser: five subtests, split-half reliability in the .70s for the whole, correlation with verbal intelligence tests near .6 (a15). Sternberg (1986) doubted it predicts anything beyond a group intelligence test.
- Cornell: internal consistency about .8 (Level X) and about .7 (Level Z), correlation with verbal IQ near .5, with Watson-Glaser r=.48 and with the ACE test r=.44 (a16). Sternberg called these correlations "not auspicious" for a construct apart from verbal intelligence.
- CCTST: built from the Delphi definition. Item-to-skill map: items 1-5 interpretation, 6-9 analysis, 10-13 evaluation, 14-24 inference, 25-35 explanation, so skill groups have 4 to 11 items (a05). Norris and Ennis advise reliability of .65 to .75 for multi-skill tests (a05).
- NJ Test of Reasoning Skills: 50 items for 22 skills, about 2 items per skill. Reported reliabilities mid-to-high .80s (a17). The skill labels cannot be measured at that density.

**Two competing views of what is measured.**
1. *Skill view* (Delphi, CCTST): CT is a set of separable skills that can be scored separately and taught.
2. *General-ability view* (Sternberg 1986, Bycio and Allen 2009, Sebokova 2026): CT tests mostly track verbal and general reasoning ability. Sub-scores are noise. Gain from teaching is small.

The measured evidence (sections 3 and 5) favours the second view for multiple-choice tests. The skill view survives mainly as a way to design items and rubrics.

**Move toward performance assessment.** Liu, Frankel and Roohr (2014, ETS) reviewed CCTST, WGCTA, CAAP, EPP, HCTA, CLA+ and listed the flaws: unreliable sub-scores, non-equivalent forms, unclear differential validity, thin incremental-validity evidence (a11). Shavelson, Zlatkin-Troitschanskaia and colleagues (2020) argued that forced-choice, short-answer and scenario tests show moderate to severe construct underrepresentation and proposed document-portfolio performance tasks (a20). The price is rater cost and lower reliability (section 5).

**Move toward dynamic tasks (2026).** Beyond Static Snapshots (b07, b08) argues that multiple choice cannot capture changing a position after new evidence and builds an iterative-argumentation task with staged evidence.

**Move to LLMs (2020-2026).** Early work (LogiQA, ReClor, AR-LSAT, 2020-21) made exam-derived logic benchmarks and showed models far below people (a24, a25, a26). GPT-4 (2023) reached the LSAT 88th percentile (a21). Cognitive-psychology batteries were run on GPT-3 and later models (a27, a28). By 2025 reasoning models were near the human ceiling on several sets (d01, d03), and the question moved to contamination, noise and unsaturated sets (d04, d06-d10).

*Background not opened this session:* the Watson-Glaser dates from the 1920s-30s, and the Cornell tests and the Ennis-Weir essay test from the 1980s. These dates are general knowledge, not from an opened source.

## 3. Core findings with exact numbers

Status: E established, S single source, C contested (from claims.jsonl, with the critique corrections applied).

| Finding | Numbers | Source | Status |
|---|---|---|---|
| WGCTA total reliable, subscales not | N=264 (replication N=137), 79 items. Total alpha .691, omega .846. Subscale alpha .23-.51 (Inference .469, Assumptions .262, Deduction .234, Interpretation .491, Arguments .511). CFA per subscale CFI .60-.81, below .90 | Sebokova 2026 (b01, b03) | E (K01) |
| Earlier subscale reliability the same | CCTST subscale alpha .21-.51 vs total .68-.70 (Leppa 1997). WGCTA subscale alpha .17-.74 (Loo and Thorpe 1999). One factor across 60 WGCTA studies (second-hand) | Liu et al. 2014 (a11, a12) | E (K01) |
| 9-item short WGCTA as good as the full test | 9 items (5 Interpretation, 4 Arguments) omega .66. Correlation with CRT-N r=.381, CRT-V r=.299; full test r=.329, .298. Replication r=.303, .307 | Sebokova 2026 (b02) | S |
| CCTST has modest reliability | 34 items. Pretest n=480 mean 16.09 (SD 4.65), posttest n=465 mean 16.83 (SD 4.68). KR-20 .69 and .68. Gain 0.74, t=2.44. Test-retest (Chinese form, 1 month, N=186) r=.63 | Facione 1990 (a04); Luo 2002 via b05 | E (K03) |
| CCTST tracks verbal ability | N=1196. SAT-V r=.55, SAT-M r=.44, EPT r=.48, GPA r=.20. R2 .41 for SAT+GPA, .71 with CCTST pretest added. Independent: N=131, SAT-V r=.66, SAT-M r=.69, SAT explains 56% of CCTST variance | Facione 1990 (a06); Bycio and Allen 2009 (a10) | E (K02) |
| CCTST adds almost nothing to prediction | CCTST with capstone r=.21, with GPA r=.41. Animal-science model: adj R2 .392 (ACT + HS GPA) to .393 with CCTST; F=1.028, n.s.; N about 105-118 | a10; animal sciences 2026 (b06) | E (K02) |
| Control classes barely gain | Intro Philosophy control: +0.04 (t=0.08, p=.938, n=124) and +0.63 (n=90, n.s.). Norms from 1,673 forms: pretest mean 15.89, range 2-29 | Facione 1991 (a08) | E (K03) |
| Non-native speakers gain nothing | About 19% of sample. Non-native mean 13.75 vs native pretest 16.65, posttest 17.59 | Facione 1990/91 (a07) | S |
| Overconfidence among test takers | 80% (383/480) pretest and 84% (392/465) posttest agreed "CT and being logical are quite easy for me"; posttest score 49.5% correct | Facione 1991 (a09) | S |
| Form B harder than Form A | Reported by Liu et al. citing Jacobs 1999, Bondy 2001; no figures; originals not opened | a13 | S |
| Independent studies report lower quality | Ku 2009 via Liu 2014. WGCTA-job performance corrected r=.32-.52 (Ejiogu 2006). HCTA vs negative life events r=-.38 | a14 | S (K05) |
| Stakes and attrition distort scores | Thurgood Marshall WGCTA: 200 pretest, 90 posttest. Post median 50 vs 59 pre (-9) | Kadhi 2010 (a19) | S (K06) |
| Constructed response is the noisy part | CLA+ constructed-response reliability .43; whole test .87 (driven by the 30-min multiple-choice part). Performance task G=.74 with 2 raters, .84 with 4 | a11, a20 | E (K07) |
| Different CT tests overlap little | N=355 + 33 debaters. Ennis-Weir vs TSA r=.33. TSA vs Number Series r=.58, vs Matrix r=.53. New argument-integration task vs TSA r=.11, vs EWCTET r=.12. Rater kappa .72-.91 | Beyond Static Snapshots 2026 (b07) | S (K21) |
| Chinese students below midpoint on CCTST | k=79, N=8,860. Pooled proportion correct 0.426. Discipline moderates; grade level and institution type do not. Dissertations lowest | CCTST meta-analysis 2026 (b04, b05) | S |
| Instruction effect on CT tests (human) | 1990: 20 usable of 250 studies, mean 0.37 SD (50th to 64th pct); continuous 0.47 vs periodic 0.15; grades K-8 0.50 vs high school/college 0.21. 2015: g+=0.30 over 341 effects. 2016: 71 reports, 4-yr college gain 50th to 72nd pct. 2026 inquiry meta-analysis: 57 studies, g=1.336, I2=92.09% | Bangert-Drowns and Bankert 1990 (a18); Abrami 2015 (d11); Huber and Kuncel 2016 (d12); b10 | C (K04) |
| Many students show no gain | CLA, 2,300+ students, 24 institutions: 45% no significant gain in 2 years | Arum and Roksa 2011 (d13) | S |
| GPT-4 LSAT | 163 (~88th pct); no-vision 161 (~83rd); GPT-3.5 149 (~40th). Contamination row: 40 items, 25.00% flagged, -0.85% change | GPT-4 report (a21, a22, c14) | S (K11) |
| GPT-4 on LSAT parts (2023) | Zero-shot AR 35.2, LR 80.6, RC 85.9, LogiQA-en 49.3. CoT 34.4/80.6/85.1/57.8. Few-shot 33.9/85.9/87.7/63.9. Human avg 56 (top 91); LogiQA human 86 (top 95) | AGIEval (a23, c07) | C (K12) |
| Reasoning models close the AR-LSAT gap (2025) | AR-LSAT: GPT-4 73.12, o1-mini 79.23, R1 90.01, QwQ-32B 92.35 (human 56, ceiling 91). ReClor dev: GPT-4 87.20, o1-mini 80.57, R1 77.88, QwQ 93.76. LogiQA 2.0: 72.25, 69.35, 76.22, 85.70 | GLoRE update (d01) | C (K12) |
| Solver beats CoT on AR-LSAT | GPT-4 standard/CoT/Logic-LM 33.33/35.06/43.04. CoT averaged -3.2 on AR-LSAT. Self-refinement raised executable rate by 5.01 on average | Logic-LM (c10, c11) | E (K13) |
| Shortcut exploitation | ReClor RoBERTa 75.5% EASY vs 40.0% HARD (human 57.1 vs 67.2). Early LogiQA best model 35.31% vs human 86.00 | ReClor, LogiQA (a24, a25, c12, c13) | E (K14) |
| Out-of-distribution drop | GPT-4 LogiQA 2.0 72.25 to LogiQA22 58.49 (-13.8); o1-mini 69.35 to 59.84; R1 76.22 to 71.63; QwQ 85.70 to 86.30. Context carry-over: ood 20 items, 9 correct same window vs 5 fresh | Liu 2023 (c04, c05); d02 | E (K15) |
| Frontier saturation, unsaturated subset | LogiEval 6,235 items: 7 reasoning models 78.74-81.41%. 4-choice argument analysis models 81.20-89.90 vs humans 85.2. 5-option: 51.86-73.38. LogiEval-Hard 1,617 items, mean 37.97%; 18.3% missed by every model | LogiEval (d03, d04) | E (K25) |
| Human difficulty does not predict model difficulty | n=7 per band: human 18% -> model 85.71%; human 31% -> 0%; human 41% -> 100%; human 46% -> 28.57% | LogiEval Table 4 (d05) | S (K26) |
| CRT: models vs humans | Humans 38% correct (original 41%, n=3,428). davinci-003 5% (80% lure). ChatGPT-3.5 59% (15% lure). ChatGPT-4 96% (0% lure). Semantic illusions: humans 26%, davinci 18%, 3.5 74%, 4 88%. GPT-3 0 of 3 classic CRT items (Binz and Schulz) | Hagendorff 2023 (a28, b14, b17); Binz and Schulz (a27, c20) | E (K09) |
| Cheap prompts on old models | davinci-003 "Let's use algebra" 5% to 28% (lure 80% to 29%); "check for invalid assumptions" 18% to 54%; few-shot 2% to 92% (Type 2), 12% to 92% (Type 3). ChatGPT-4 forced short: 95% to 88% (lure 0% to 10%, p<.05); ChatGPT-3.5 change 4 points, p=.49 | Hagendorff 2023 (a29, b15, b16, c19) | S (K10) |
| Content effects | Wason realistic-rule advantage for humans, Chinchilla, PaLM 2-L, GPT-3.5 (z>2.2, p<.03); marginal for PaLM 2-M, Flan-PaLM 2 (z about 1.78, p about .08). Humans slower than 80 s (top 15%) above chance only on Realistic; z=4.44 | Lampinen 2024 (c15, c16) | E (K16) |
| Fallacy detection (pre-chat models) | 12 models 8.62-53.31 micro F1 on LOGIC (13 fallacy types); structure-aware Electra 58.77 | Jin 2022 (c17) | S (K19) |
| Ennis-Weir on o1-preview | Mean 2.25 (81.25%), SD 0.43; typical humans 37.5-62.5%. Single run, no reliability | o1 evaluation (b18) | S (K24) |
| LLM auto-scoring of CT essay subskills | 500 coded essays of 4,115. Llama-8B fine-tune accuracy .604, alpha .606; ModernBERT .563; GPT-5 zero-shot .543, few-shot .532; unseen subskills .39-.56. Human coder weighted kappa .55-.87 | Peczuh 2025 (b23, b24, d14) | S (K08) |
| LLM judge agreement | GPT-4 vs humans 85%, human vs human 81%. Consistent under position swap 65.0% (77.5% few-shot) | Zheng 2023 (d15) | E (K29) |
| Humans miss planted LLM errors | N=24, 15 modified WG items. P(correct) when LLM wrong: short .245, medium .542, long .307; when right .715/.811/.795 | Friedman 2026 (c01, c02) | S (K17) |
| Sample size for a 3-point gain | About 969 paired items (alpha .05, power 80%, paired variance 1/9). With 198 items MDE 13.2% (K=1) to 7.5% (K=10). Clustered SEs up to 3x naive | Miller 2024 (d06-d08) | E (K27) |
| Temperature 0 is not stable | 5 LLMs, 8 tasks, 10 runs: accuracy varies up to 15%; best-worst gap up to 70%. Option order: GPT-4 Professional Law 57.0 with -30.0/+23.0 swing under oracle worst/best order; positional calibration up to +8 | Atil 2025 (d09); Pezeshkpour and Hruschka 2024 (d10) | E (K28) |
| Base-rate answer-letter bias | MMLU cloze Nvr-A: GPT-2 0.007 vs about 0.33 elsewhere; Llama2 0.560 | Moore 2024 (a30) | E (K23) |
| Critical-questions prompting | CQoT MT-Bench reasoning avg +4.61%, math +5.4%; Claude 3.5 Sonnet 8.6 to 8.95; GPT-4o 8.3 to 8.45; Nemotron-51B 7.7 (CoT) vs 7.3 (CQoT). Plan-only (steps 1+4) Llama 8.3 vs full 8.4 | Castagna 2024 (c22, c23, d16) | S (K20) |

Source-count note (critique.md): the Hagendorff lines (a28, a29, b14-b17, c18, c19) are one source; the AGIEval lines (a23, c07, c08) are one source; the Friedman lines (b20, c01, c02, c28) are one source; the Sebokova lines (b01-b03, b27) are one source. Corrections applied: ReClor ChatGPT is 57.38 and RoBERTa 55.01 (not a ceiling of 100; no human ceiling is given for ReClor); the 87.20 GPT-4 ReClor figure is on 500 items; AR-LSAT human is 59.7% in the original paper and 56% in AGIEval/Liu 2023, which use different item sets.

## 4. Mechanisms and models

Each model is written so an engineer can build it.

### 4.1 Why subscale scores fail (measurement model)
Reliability rises with item count. A subscale of 4-11 items has low alpha, so its error band is wider than the differences between people. With a total of 34 items KR-20 is about .68; a subscale of 5 items cannot reach it.
- **Implement:** log one total pass rate per item class. Split by class only when each class has at least a few dozen items. Report a confidence interval (cluster by passage) with every rate.
- Spearman-Brown logic: to reach a target reliability, lengthen the test. For the agent, "lengthen" means more items and more repeated runs (but see 4.5 on what repeats can and cannot fix).

### 4.2 Why CT scores track verbal ability (common-cause model)
Reading load, vocabulary and general reasoning drive scores on every multiple-choice CT test. SAT-V r=.55-.66 with CCTST; Cornell vs verbal IQ near .5; WG near .6; TSA correlates more with Number Series (.58) than with another CT test (.33).
- **Implement:** for any gate, also run a plain-model baseline on the same items and a non-CT control set. If the gate score correlates near 1 with plain accuracy across item classes, the gate adds no information (K02 test).

### 4.3 Shortcuts and contamination (answer-leak model)
A score can come from (a) answer-option artefacts (ReClor EASY/HARD), (b) answer-letter bias (Moore 2024), (c) item memorisation (GPT-4: 25% of 40 LSAT items flagged; LogiQA22 drop of 13.8 points for GPT-4), (d) pattern copying from near-identical demos (few-shot 2% to 92%).
- **Implement:** (1) answer-only probe: run a cheap model with the question removed; drop items it solves. (2) Shuffle options in code and average over permutations; report the minimum over variants. (3) Prefer post-cutoff items. (4) Keep demonstrations out of the item families on the gate.

### 4.4 Format and item-type model (what a scaffold can move)
Item type predicts where a code-side operator helps. Constraint puzzles (AR-LSAT) gained +9.7 from a solver (33.33 to 43.04) while CoT lost 3.2 on average. Argument-evaluation items (LSAT-LR, RC) showed no CoT gain (80.6 vs 80.6; 85.9 vs 85.1). LogiQA gained from CoT (49.3 to 57.8) and few-shot (63.9). Option count matters: 4-choice 81-90% vs 5-option 52-73% for reasoning models.
- **Implement:** tag every gate item with type, option count and passage id. Compare arms per type, never on a mixed average (the AGIEval average moved only 56.4 to 58.4 with CoT).

### 4.5 Noise model for LLM test scores
Total variance has (a) item-sampling noise (which questions), (b) run noise (temperature 0 still varies up to 15%), (c) order noise (option permutation; context carry-over, 9 vs 5 of 20), (d) format noise (parse failures look like reasoning failures; c06).
Miller's formula for a paired design: n = (z.025 + z.20)^2 * var_diff / delta^2, about 969 for delta=.03 with var_diff=1/9. Resampling each item K times shrinks variance by the factor (1+2/K)/3 in the worked example, so repeats cannot remove more than a third of it. Clustering inflates SE up to 3x.
- **Implement:** paired arms on the same items, same permutations; parse answers in code; count format failures separately; run each item in a fresh context; cluster-bootstrap by passage.

### 4.6 Judge reliability model
Closed-answer items: code grades, no judge noise. Open items need a judge. LLM judges agree with humans about as humans agree with each other on preferences (85 vs 81%), but position consistency is 65%, and fine-grained rubric scoring reaches only alpha .606. Human coders themselves have alpha .57-.70 on some subskills.
- **Implement:** two or more independent judges, position swap, reference answers, no authorship cues (G5), report agreement; calibrate against about 100 human-coded items before use.

### 4.7 Dynamic (belief-revision) tasks
Staged evidence: show a passage with evidence units, ask for a position, add evidence, ask again, then code what changed and why. Human kappa .72-.91 with 3 raters, known-groups validity (debaters higher), low overlap with static tests (r .11-.33).
- **Implement:** a belief-revision probe for the agent. After each new evidence unit, code in program whether the answer changed when the new unit was decisive and stayed when it was irrelevant. This tests G2 (revise only from real output) directly. No LLM score on this exists (gap 7).

### 4.8 Delphi skills as labels
The six skills (interpretation, analysis, evaluation, inference, explanation, self-regulation) could be mapped to schema parts: interpretation to S1, analysis to S2, evaluation to S4/S8, inference to S3/S7, explanation to S9 and the log, self-regulation to S5/S6 and G1-G3. Whether labelling checks by skill changes outcomes is untested (gap 9).

## 5. What holds up

**Held (two or more independent sources):**
- Total scores moderately reliable, subscales poor: Leppa 1997 and Loo and Thorpe 1999 (via a11), Sebokova 2026 (b01), Facione's own note (a05). [E]
- CT test scores overlap with verbal ability: Facione 1990 (a06), Bycio and Allen 2009 (a10, independent), Sternberg 1986 (a15, a16), b06, b07. [E]
- Gains in no-intervention control groups are near zero on the CCTST (a08). [E, one control class]
- Open-ended scoring is less reliable than multiple choice and needs raters (a11, a20). [E]
- Answer shortcuts and contamination inflate LLM scores: ReClor EASY/HARD (a25), MMLU base rate (a30), GPT-4 contamination table (a22), LogiQA22 drop (d02). [E]
- Noise floors: temperature 0 variation (d09), option order (d10), context carry-over (c05), clustering (d08). [E]
- A solver beats CoT on constraint puzzles (c10); a pre-LLM neuro-symbolic LSAT system also matched median humans, 56.8% overall (c09). [E, on 2022-23 models]
- Content effects in LLMs and humans (c15, b22). [E]

**Contested or failed:**
- Size of the instruction effect: 0.37 SD (1990), 0.30 g+ (2015), 50th to 72nd percentile (2016), g=1.336 with I2=92% (2026). Control type moderates (Qm=5.21, p=.022). Dissertations score lowest (b04). Unresolved [C].
- AR-LSAT difficulty: GPT-4 33-43% in 2023 papers, 73.12 in GLoRE, 79-92 for reasoning models. The old claim "AR-LSAT is hard for LLMs" no longer holds for reasoning models [C].
- CoT as a free win: no gain on LSAT-LR/RC, loss on AR-LSAT (-3.2), gain on LogiQA. Task-dependent.
- Reasoning-trap tests (CRT): from 5% to 96% across model generations; they no longer discriminate for strong models (ChatGPT-4 correct 95% unforced, 88% when forced short).
- Human difficulty as a guide to model difficulty failed at n=7 per band (d05) and on NAEP science items (model rank did not follow cognitive demand, c21).
- Few independent replications of publisher technical reports exist beyond Bycio and Allen (a10); independent studies report lower quality (a14).

**Moderators that matter:**
- Control group type in instruction studies (b10); continuous vs periodic programs (0.47 vs 0.15); grade level (0.50 vs 0.21); internal-and-external-validity content (0.55 vs 0.03) (a18).
- Language: non-native speakers show no gain (a07); LLM bias results shift across English, Hebrew and Russian (b22).
- Test stakes and attrition (a19); self-rated skill is a poor measure (a09, b25).
- Option count (d03), option order (d10), context carry-over (c05), item cluster (d08).
- Time budget: LLM help raises human scores under insufficient time and lowers them when time suffices (N=393, b21).

**Interventions that worked (in LLMs, with caveats):**
- Solver check for constraint puzzles (+9.7 on AR-LSAT, GPT-4).
- Letting older models write steps (davinci algebra suffix +23 CRT points; LogiQA CoT +8.5).
- Positional calibration (up to +8 on MMLU-style items).
- Adversarial filtering to make an unsaturated set (LogiEval-Hard).

**Did not work:**
- CoT on LSAT-LR/RC and AR-LSAT (c07, c10).
- Refinement from syntax-only feedback after the first rounds (accuracy stagnates, c11).
- LLM self-report scales as measures (unstable, d17).
- Dispositions as predictors: no evidence for LLMs (d18).

## 6. Language models

**No official-test data.** No study gave the Watson-Glaser, Cornell or CCTST to an LLM (K22; search coverage incomplete because OpenAlex and Semantic Scholar were rate-limited; three more queries found nothing). The one Watson-Glaser LLM paper (Friedman 2026) used modified items to test human error detection (N=24), not LLM accuracy (c01). Copyright and proprietary items explain part of the gap.

**Timeline on open proxies.**

| Period | Model | Result |
|---|---|---|
| 2020 | fine-tuned BERT/RoBERTa | LogiQA 35.31 vs human 86; ReClor HARD 40.0; AR-LSAT 21-34 vs human 59.7 (a24-a26) |
| 2022 | GPT-3 | 0 of 3 classic CRT items; 6 of 12 vignettes correct, all 12 human-like (a27) |
| 2022 | text-davinci-003 | CRT 5% correct; semantic illusions 18% (b14) |
| 2023 | ChatGPT 3.5 | CRT 59%; LSAT 149 (~40th pct); LogiQA 2.0 52.37; ReClor 57.38; AR-LSAT 20.42 (c04, a21) |
| 2023 | GPT-4 | CRT 96%; LSAT 163 (~88th); LSAT-LR 80.6, RC 85.9, AR 35.2; LogiQA 2.0 72.25; ReClor 87.20; AR-LSAT 33.48 (a21, a23, c04) |
| 2024 | o1-preview | Ennis-Weir 81.25% (single run); Algorithmic Thinking 25/25; psychology students still beat it on text Raven's (b18, b19) |
| 2025 | o1-mini, R1, QwQ-32B | AR-LSAT 79.2 / 90.0 / 92.4; LogiQA 2.0 69.4 / 76.2 / 85.7; LogiQA22 59.8 / 71.6 / 86.3 (d01, d02) |
| 2025 | 7 reasoning models | LogiEval 78.7-81.4%; LogiEval-Hard mean 37.97% (d03, d04) |

**What changed scores, and by how much.**
- *Model generation:* the biggest factor. CRT 5% to 96%; LogiQA 2.0 52 to 72 to 86 across generations.
- *Built-in reasoning:* AR-LSAT 33.5 (GPT-4, 2023) to 90+ (reasoning models). GLoRE's own GPT-4 figure of 73.12 differs from 33-43 elsewhere, so prompt and item set matter nearly as much as the model.
- *Prompt scaffolds on older models:* algebra suffix +23 CRT points; "check for invalid assumptions" +36 points on semantic illusions; same-type few-shot up to +90 (pattern copying). For ChatGPT-4, blocking reasoning cost only 7 points.
- *Chain of thought:* +8.5 on LogiQA, 0 on LSAT-LR, -0.8 on LSAT-RC, -0.8 on LSAT-AR (a23); -3.2 on average on AR-LSAT (c10). AGIEval average 56.4 to 58.4.
- *External solver:* +9.7 on AR-LSAT with GPT-4; with GPT-3.5, average +39.2 over standard and +18.4 over CoT across five sets (c10).
- *Critique prompting:* CQoT +4.6% on reasoning in a judged chat benchmark, with no equal-token control and no significance test (d16). Plan-before-answer gave part of it (c23).
- *Item hygiene:* out-of-distribution items cost 13.8 points (GPT-4), 9.5 (o1-mini), 4.6 (R1); fresh vs shared context 5 vs 9 of 20; option count (4 vs 5 choices) 15-30 points for reasoning models; option order up to -30/+23 (oracle upper bound).
- *Run noise:* up to 15% at temperature 0.

**Behaviour patterns.**
- LLMs show human-like content effects (belief bias) and the same abstract-rule failures on Wason (c15, b22). Cross-language bias patterns differ (b22).
- Humans reading LLM reasoning trust sound-looking steps even when the conclusion is wrong (c01, c03).
- Models are weak on abstract matrices and strong on verbal and rule-based tests (b19).
- LLM and human difficulty do not line up (d05, c21).
- LLMs as scorers: moderate on essay subskills (alpha .606 at best); good on chat preference (85%) but biased by position and length (b23, d15).

**What is missing:** 2026 frontier-model numbers on LogiQA 2.0, AR-LSAT, ReClor HARD; any plain-vs-scaffold comparison at equal tokens on reasoning models; CT-test-specific run-to-run SD; Ennis-Weir or CLA+ judge agreement against two human raters (d20, critique gaps).

## 7. What our agent should take

Each item: schema part, status, evidence ids.

### Add now (established)

1. **Log only totals per item class, with intervals.** Do not report skill-level scores per Delphi skill. Schema: S0, section 6 logs. [E] K01, K03. Evidence a05, a11, b01, b27.
2. **Calibrate every gate item on model pass rate, not on human norms.** Fix option count, shuffle options, average over permutations, report the minimum over variants. Schema: S0. [E] K23, K28 (the human-versus-model difficulty table K26 is [S]). Evidence a30, d03, d05, d10.
3. **Fresh context per item and post-cutoff items for the gate.** Schema: S0, memory. [E] K15, K23. Evidence c04, c05, d02, a22.
4. **Strip shortcut-solvable items and report on the hard split.** Answer-only probe, as in ReClor EASY/HARD. Schema: S0. [E] K14. Evidence a25, c12.
5. **Pre-register noise handling.** Run the plain arm K times, report the spread, parse in code, count format failures separately, cluster by passage. Schema: G7, S0. [E] K27, K28. Evidence d06-d10, c06, a19.
6. **Minimum power.** Plan about 1,000 paired items for a 3-point gain; repeats alone do not fix a 198-item set. Schema: G7. [E] K27. Evidence d06, d07, d08.
7. **Code-graded closed-answer items for the gate; two or more judges with position swap for open items.** Schema: G5, S0. [E] K07, K29. Evidence a11, a20, d15, d14.
8. **Report scaffold gain per item type, never as a mixed average.** Schema: G7. [E] on the noise and type-dependence (K12 and K13 show CoT effects vary by type). Evidence a23, c08, c10, c26.
9. **Keep refinement rounds capped when feedback carries no logic information.** Schema: S5, G2. [E] K13. Evidence c11.
10. **Keep demonstrations out of held-out gate items and keep a human or earlier-model reference per item.** Schema: S0, memory. [E] K23 (a29 single). Evidence a22, a29, b17.

### Test first

- **External-check operator (code or solver) on constraint-style items.** Schema: O (external check), G2. [E] K13 for 2023 models; [C] for reasoning models, where AR-LSAT is near saturation (K12). Evidence c10, c11, d01.
- **Critique-style checks (CQoT) vs plain plan at equal tokens.** Schema: S0 / O critique. [S] K20. Evidence c22, c23, d16. Conflicts with G1 (schedule) and G2 (self-grading); test only a signal-triggered version.
- **Fallacy-checklist operator** on LOGIC and our own items. Schema: G / O. [S] K19. Evidence c17 (pre-chat models only).
- **Belief-revision staged-evidence probe** for G2. Schema: S0 / G2. [S] K21. Evidence b07, b08.
- **Belief-bias pair probe** (same logic, different content) as a conflict signal for G1. The effect is [E] (K16); its use as a gate is untested. Evidence c15, c16.
- **Delphi-skill labels on S0 checks** (interpretation to S1, and so on). No evidence; gap 9.
- **Short-probe gate** (9 items) vs long gate. [S] human data only. Evidence b02.
- **LogiEval-Hard as the S0 gate set.** Unsaturated [E] (K25); check selection bias and label errors. Evidence d04.
- **One-line "check for invalid assumptions" vs scaffold at equal tokens on current models.** [S] K10. Evidence b16, c19. G1 and SCHEMA section 4b warn against always-on doubt.
- **Disposition scales (CCTDI, Need for Cognition) on LLMs.** [S] K30; do not build gates on them.

## 8. Concrete tests on our bench

All arms run at equal total tokens per item (setup cost counted, G7). All items run in a fresh context, options shuffled over 4 fixed permutations, answers parsed in code.

| # | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 | LogiEval-Hard (1,617 items), cluster by passage | plain; scaffold S0-S9 | Paired accuracy difference with cluster-bootstrap CI; plain arm repeated 5 times for spread | Unknown on 2026 models. Plausible gain 0-5 points; the test shows whether the scaffold beats plain at all |
| T2 | AR-LSAT-style constraint items (230 + fresh) | plain; CoT at equal tokens; code-solver operator | Accuracy per type; executable rate | Solver beats CoT by 5+ points on non-reasoning models; near zero gain on reasoning models (saturated, d01) |
| T3 | ReClor HARD and LSAT-LR items | plain; CoT; plan-only; plan + signal-triggered critique | Accuracy at equal tokens | CQoT-type gain small; expect under 3 points |
| T4 | Post-cutoff items (LogiQA22 and newer) vs old LogiQA 2.0 | plain; scaffold | Accuracy drop old to new, per arm | Drop 5-14 points for older models; does the scaffold shrink it? |
| T5 | CRT variants and semantic illusions (fresh, generated) | plain; one-line doubt; scaffold | Correct rate; lure rate | Modern models near ceiling; value is as a floor check for small models |
| T6 | Belief-bias pairs (same logic, abstract vs realistic) | plain; scaffold | Realistic-minus-abstract gap | Gap shrinks with a conflict-triggered check; baseline gap seen in GPT-3.5 (z>2.2) |
| T7 | Staged-evidence belief revision (passages with evidence units, b07 style) | plain; scaffold with G2 | Correct update rate on decisive evidence; false update rate on irrelevant evidence | Unknown; no LLM data exists |
| T8 | Open CT items graded by 2 LLM judges plus 100 human codes | single judge vs 2 judges with position swap | Krippendorff alpha vs human; position consistency | Alpha near .6 at best (b23); position swap lifts consistency from 65% toward 77% (d15) |
| T9 | Answer-only probe on our gate items | small model, question removed | Share of items above chance | Items solved without the question are dropped |
| T10 | Skill-labelled vs unlabelled S0 checks | tagged by Delphi skill vs untagged | Task accuracy at equal tokens | Null expected; if tags help, new finding |
| T11 | Noise floor | plain arm, 10 runs at temperature 0, 10 option permutations | Run-to-run SD, permutation SD | Up to 15% (d09) |

## 9. What does not transfer, and why

- **Human norms and percentiles.** They describe students under test conditions. LLM difficulty does not follow human difficulty (d05, c21). Use model pass rates.
- **Sub-skill scores.** Unreliable even in humans (alpha .17-.51).
- **Instruction gains (0.3-0.6 SD, or g=1.34).** They come from maturation, teaching and test familiarity in people. A scaffold is not a course. Use them only as a rough scale for what counts as large.
- **Dispositions (CCTDI, Need for Cognition).** Self-report scales are unstable on LLMs (d17). No evidence they predict accuracy (d18).
- **Attrition, motivation, stakes, fatigue.** Human validity threats (a19, b13). The matching LLM threats are context carry-over and token budget, not motivation.
- **Proprietary item banks.** Cannot be freely used; no LLM study found. Use open proxies.
- **Prompting tricks tested on davinci-003.** The few-shot jump (2% to 92%) is pattern copying; the algebra and invalid-assumption gains were on a non-chat model and may not transfer (ChatGPT-4 reasons natively).
- **Human error-detection results (Friedman, N=24).** Humans reading LLM text are not our judge model; use only as a warning that fluent steps hide wrong conclusions.
- **Effects of LLM use on human CT (b21, b25, b26).** Outside agent scope.
- **MT-Bench-style judged gains (CQoT).** Small n, LLM judge, no token control.
- **Self-regulation as a skill.** The Delphi panel said paper tests cannot measure it; our code-side G2 and G3 checks are the substitute, not a test score.

## 10. Open questions

1. How do 2026 frontier models with built-in reasoning score on LogiQA 2.0, ReClor HARD and AR-LSAT, and does a scaffold still beat plain at equal tokens?
2. What is the run-to-run and option-order SD on CT-style items specifically?
3. Is LogiEval-Hard's difficulty real, or an artefact of adversarial filtering and label errors?
4. Are there contamination-free post-cutoff LSAT or Bebras items we can use legally?
5. How reliable is an LLM judge against two human raters on Ennis-Weir or CLA+ tasks?
6. Does critique-style prompting (CQoT) survive equal-token control with significance tests on LSAT or ReClor?
7. Do staged-evidence belief-revision tasks work for agents, and what are LLM scores?
8. Do Delphi-skill labels on checks predict outcomes better than unlabelled checks?
9. What are the verified effect sizes of Huber and Kuncel (per-year d, skills vs dispositions) and Abrami (full tables)? Only abstracts or summaries were opened.
10. Has anyone, with a licence, run the official Watson-Glaser, Cornell or CCTST on an LLM? Our absence claim comes from partial search coverage.
11. Do dispositional measures correlate with accuracy in LLMs, with wording and order controls?
12. How much of the 2025 AR-LSAT gain is model reasoning, and how much is prompt or item-set difference (GPT-4 33.33 in one paper, 73.12 in another)?

## 11. Sources

[V] = opened and read this session; [M] = snippet only or recalled, not opened.

- [V] Facione (1990) Delphi report, ED315423. https://files.eric.ed.gov/fulltext/ED315423.pdf (a01, a02, a03)
- [V] Facione (1990) CCTST Technical Report 1. https://files.eric.ed.gov/fulltext/ED327549.pdf (a04, a05)
- [V] Facione (1990) CCTST Technical Report 2. https://files.eric.ed.gov/fulltext/ED327550.pdf (a06, a07)
- [V] Facione (1991) Using the CCTST. https://files.eric.ed.gov/fulltext/ED337498.pdf (a08, a09)
- [V] Bycio and Allen (2009) CCTST and business school performance. https://files.eric.ed.gov/fulltext/EJ1052629.pdf (a10)
- [V] Liu, Frankel and Roohr (2014) ETS RR-14-10. https://onlinelibrary.wiley.com/doi/full/10.1002/ets2.12009 ; text https://files.eric.ed.gov/fulltext/EJ1109287.pdf (a11, a14)
- [M] Bernard et al. (2008) WGCTA structure, as cited in a11. https://doi.org/10.1016/j.tsc.2007.11.001 (a12)
- [M] Jacobs (1999), Bondy et al. (2001) form equivalence, as cited in a11 (a13)
- [V] Sternberg (1986) NIE. https://files.eric.ed.gov/fulltext/ED272882.pdf (a15, a16, a17)
- [V] Bangert-Drowns and Bankert (1990). https://files.eric.ed.gov/fulltext/ED328614.pdf (a18)
- [V] Kadhi et al. (2010). https://files.eric.ed.gov/fulltext/ED513411.pdf (a19)
- [V] Shavelson et al. (2020) Frontiers in Education. https://www.frontiersin.org/articles/10.3389/feduc.2020.00156/full (a20)
- [V] OpenAI (2023) GPT-4 Technical Report. https://arxiv.org/abs/2303.08774 (a21, a22, c14)
- [V] Zhong et al. (2023) AGIEval. https://arxiv.org/abs/2304.06364 (a23, c07, c08)
- [V] Liu et al. (2020) LogiQA. https://arxiv.org/abs/2007.08124 (a24, c13)
- [V] Yu et al. (2020) ReClor. https://arxiv.org/abs/2002.04326 (a25, c12)
- [V] Zhong et al. (2021) AR-LSAT. https://arxiv.org/abs/2104.06598 (a26)
- [V] Binz and Schulz (2023) PNAS. https://arxiv.org/abs/2206.14576 (a27, c20)
- [V] Hagendorff, Fabi and Kosinski (2023). https://arxiv.org/abs/2212.05206 (a28, a29, b14-b17, c18, c19)
- [V] Moore et al. (2024) Base-rate effect. https://aclanthology.org/2024.findings-emnlp.126/ (a30)
- [V] Lin et al. (2024) CriticBench, abstract and first page only. https://arxiv.org/abs/2402.14809 (a31)
- [M] Gap notes on absence of LLM studies of official tests (a32, c25, d19); absence of evidence, coverage incomplete
- [V] Sebokova et al. (2026) WGCTA-II. https://pmc.ncbi.nlm.nih.gov/articles/PMC12910364/ (b01, b02, b03, b27)
- [V] CCTST meta-analysis of Chinese students (2026). https://pmc.ncbi.nlm.nih.gov/articles/PMC13368918/ (b04, b05)
- [V] CT and academic achievement in animal sciences (2026). https://pmc.ncbi.nlm.nih.gov/articles/PMC13506052/ (b06)
- [V] Beyond Static Snapshots (2026). https://pmc.ncbi.nlm.nih.gov/articles/PMC13514467/ (b07, b08)
- [V] PACIER framework (2025). https://pmc.ncbi.nlm.nih.gov/articles/PMC12471143/ (b09)
- [V] Inquiry-based learning meta-analysis (2026). https://pmc.ncbi.nlm.nih.gov/articles/PMC13562932/ (b10)
- [M] Huber and Kuncel (2016) full paper, recalled only (b11). https://doi.org/10.3102/0034654315626801 ; [V] AERA summary https://www.aera.net/Newsroom/Study-Snapshot-Does-College-Teach-Critical-Thinking (d12)
- [M] Abrami et al. (2015) full paper, recalled (b12); [V] abstract only (d11). https://doi.org/10.3102/0034654314551063
- [M] Arum and Roksa (2011), recalled (b13); [V] publisher abstract (d13). https://doi.org/10.7208/chicago/9780226028576.001.0001
- [V] Evaluation of OpenAI o1 (2024), first 100,000 characters. https://arxiv.org/html/2410.21287v1 (b18, b19)
- [V] Friedman et al. (2026) Not Too Short, Not Too Long. https://arxiv.org/abs/2603.06878 (b20, c01, c02, c03)
- [V] Effects of LLM use on CT under time constraints (2026). https://arxiv.org/pdf/2603.08849 (b21)
- [V] Cross-linguistic cognitive biases in LLMs (2026). https://pmc.ncbi.nlm.nih.gov/articles/PMC13318900/ (b22)
- [V] Peczuh et al. (2025) automated CT subskill assessment. https://arxiv.org/abs/2510.12915 (b23, b24, d14)
- [V] Cognitive offloading among Chinese university students (2026). https://pmc.ncbi.nlm.nih.gov/articles/PMC13413235/ (b25)
- [V] AI-generated content in medical education review (2026). https://pmc.ncbi.nlm.nih.gov/articles/PMC12954715/ (b26)
- [V] Liu et al. (2023) Logical reasoning of ChatGPT and GPT-4. https://arxiv.org/abs/2304.03439 (c04, c05, c06)
- [V] Wang et al. (2022) From LSAT. https://arxiv.org/abs/2108.00648 (c09)
- [V] Pan et al. (2023) Logic-LM. https://arxiv.org/abs/2305.12295 (c10, c11)
- [V] Lampinen et al. (2024) content effects. https://arxiv.org/abs/2207.07051 (c15, c16)
- [V] Jin et al. (2022) logical fallacy detection. https://arxiv.org/abs/2202.13758 (c17)
- [V] Zhai, Nyaaba and Ma (2024). https://arxiv.org/abs/2401.15081 (c21)
- [V] Castagna et al. (2024) CQoT. https://arxiv.org/abs/2412.15177 (c22, c23, d16)
- [V] Tak et al. (2026) Sparks of Rationality, abstract and first page, no numbers read. https://arxiv.org/abs/2601.22329 (c24)
- [V] Liu et al. GLoRE. https://arxiv.org/abs/2310.09107 (d01, d02)
- [V] Liu et al. (2025) LogiEval. https://arxiv.org/abs/2505.11854 (d03, d04, d05, d20)
- [V] Miller (2024) Adding Error Bars to Evals. https://arxiv.org/abs/2411.00640 (d06, d07, d08)
- [V] Atil et al. (2025) Non-determinism. https://arxiv.org/abs/2408.04667 (d09)
- [V] Pezeshkpour and Hruschka (2024). https://arxiv.org/abs/2308.11483 (d10)
- [V] Zheng et al. (2023) LLM-as-a-judge. https://arxiv.org/abs/2306.05685 (d15)
- [M] Self-assessment tests unreliable for LLM personality (2024), ACL page summary only. https://aclanthology.org/2024.blackboxnlp-1.20/ (d17)
- [V] He and Liu (2025) personality and cognitive bias. https://arxiv.org/abs/2502.14219 (d18)
