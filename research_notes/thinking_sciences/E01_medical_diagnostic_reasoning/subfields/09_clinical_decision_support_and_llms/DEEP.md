# Clinical decision support and LLMs: deep document

*Subfield E01.09. Written 2026-11-01 from evidence_a-d.jsonl (100 lines), claims.jsonl (K01-K32) and critique.md in this folder. No new searching. Corrections from the critique are applied (Nori budget cost, Bean control figure). Evidence ids (a01, b11, d09 ...) point to the jsonl lines. Status marks: [E] established, [S] single source, [C] contested.*

Overlap note. Cognitive causes of diagnostic error, anchoring, premature closure and the "slow down" debate are covered in the earlier E01 documents (see `00_FIELDS.md`). This document covers only the direct LLM and decision-support evidence. Links to parallel subfields: Test-time compute scaling, Overthinking, Self-correction, Metareasoning, Confidence and signal-detection measures, Cognitive offloading, Model-based diagnosis, Probabilistic and test-based reasoning, Uncertain evidence, Expected information gain models, Case-based reasoning, Retrieval and similarity.

---

## 1. What it is

Clinical decision support (CDS) is software that helps a clinician reach a diagnosis or a management plan. The core job here is the **differential generator**: given a case, list the diagnoses that could explain it, ranked. Three eras exist.

1. **Rule and knowledge-base systems (1950s-2010s).** Ledley and Lusted (1959) used probability. INTERNIST-1, DxPlain, Isabel and others used large disease-finding tables and structured input. Evidence on them is thin and old.
2. **Symptom checkers and early chat models (2015-2023).** Semigran 2015 tested 23 online checkers (numbers from memory only). ChatGPT on textbook vignettes scored 71.7% (Rao 2023).
3. **LLM era (2023-2026).** GPT-4, then reasoning models (o1, o3, R1), then multi-role orchestration (MAI-DxO), conversational agents (AMIE) and agent benchmarks (AgentClinic, MediQ, SDBench).

The question we care about: **how well does a language model generate and rank a differential, how much does a scaffold add, and what goes wrong when the output reaches a consumer (a doctor, a patient) or when the model must gather the case itself?** The consumer problem matters for our agent in a narrow sense. Our agent's later stages consume its own earlier output. The human-plus-LLM failures warn us about handing good output to a weak consumer.

Three kinds of comparison appear. Keep them apart.

| Arm | Meaning | Typical result |
|---|---|---|
| LLM alone vs physicians alone | Model reads a written case, graders score | Model wins on hard puzzle cases |
| Physician + LLM vs physician alone | The model is a tool | Mixed: null, modest, or large |
| Model must gather the case | Interactive, lossy, or autonomous | Large drops for 2023-25 models |

---

## 2. History and theories in depth

### 2.1 Early systems and the evaluation habit

- Ledley and Lusted 1959: Bayes-style computation applied to diagnosis. Known only secondhand through Brodeur's introduction (c28).
- INTERNIST-1 (1982) and successors. Berner et al. 1994 compared four systems on hard cases (a27, not opened, no numbers).
- Bond et al. 2012 (a26): 23 programs found, 4 met criteria, tested on 20 cases. Mean score out of 5: Isabel 3.45 (CI 2.53-4.37), DxPlain 3.45 (2.63-4.27), DiagnosisPro 2.65 (1.75-3.55), PEPID 1.70 (0.71-2.69). Inputs were structured. Intervals overlap widely. The Goh 2024 vignettes came from a related landmark computer-diagnosis set (105 cases, never public; c04), so this work is the direct ancestor of the LLM trials.
- Semigran 2015 (c27, memory only): 23 checkers, 45 vignettes; correct first about 34%, within the top 20 about 58%. Unverified.

Lesson carried forward: the field always scored "is the right answer on the list" (top-k) and "is it first" (top-1). The gap between them is itself a finding (F10).

### 2.2 First LLM wave (2023)

- Rao et al. 2023 (a25): ChatGPT on 36 Merck Manual vignettes, 71.7% overall; initial differential 60.3% (54.2-66.6); final diagnosis 76.9% (67.8-86.1). Differential questions scored 15.8 points below general-knowledge questions (P<.001), management 7.4 below (P=.02). Textbook vignettes, likely in training data, no physician baseline.
- Kanjee, Crowe, Rodman 2023 (a09, b06, c05): GPT-4 on 70 NEJM CPC cases (80 found, 10 excluded). Right answer in differential 64% (45/70). Top-1 39% (27/70). Mean list length 9.0. Mean rank of correct item 2.5 (SD 2.5). Scorer agreement 66%, kappa 0.57. One prompt developed on 7 cases. Training data ended Sept 2021; contamination untested.
- Savage et al. 2024 (a24, b17, c19): can a clinical-reasoning prompt help? See 5.3.

### 2.3 Physician-assist trials (2023-2025)

- McDuff et al. (arXiv Dec 2023, Nature 2025; a06-a08, b20, c06, c07): 302 NEJM CPCs, 20 clinicians, each case read by two. Two-step protocol: unaided list, then aided list.
- Goh et al. 2024 (JAMA Netw Open): randomised trial of GPT-4 access on diagnostic reasoning. Null result.
- Goh et al. 2025 (Nature Medicine): same group, management reasoning. Positive result.

### 2.4 Reasoning models and orchestration (2024-2025)

- Brodeur et al. 2024: o1-preview on CPCs, R-IDEA scoring, management, landmark cases, and real ER records.
- Nori et al. 2025: SDBench turns 304 CPC cases into a sequential game (ask, order tests, pay costs). MAI-DxO is a five-role panel around any base model.
- Tu et al. 2024 (AMIE chat) and Palepu et al. 2025 (AMIE for disease management): conversational systems judged by specialists.

### 2.5 The interaction-failure literature (2024-2026)

- Hager et al. 2024: real hospital records (MIMIC) with open models; the model must choose exams and labs itself.
- Bean et al. 2025: 1,298 lay users with LLMs. Knowledge does not transfer.
- MediQ (d06), a neurosurgery vignette-to-conversation study (d07), AgentClinic (d08): moving a case from a full vignette to a dialogue drops accuracy.
- Bias and automation-bias studies (d14-d18): planted flaws.

### 2.6 Theories offered (competing, not tested head to head)

1. **Knowledge is not the bottleneck; use is.** Models hold the knowledge (Bean: 94.9% alone) but users do not elicit or adopt it. Support: b11-b13.
2. **The human-plus-LLM gap is an interface gap.** Physicians were untrained in prompting, time was short, output was free text. Support: only the authors' suggestions (c03, d10). Never varied in a design.
3. **Task type moderates.** Six diagnostic vignettes (null), open-ended management (positive), 302 CPC differentials (large). Confounded with tool, population, rubric.
4. **Humans add no independent evidence.** Physician + LLM equals LLM alone in management (b05). Humans mostly pass the model through.
5. **Structure beats raw reasoning only for weaker models.** MAI-DxO improved most families, but for o3 and o4-mini only cost fell (a16).

None of these has been isolated by an experiment. Say so each time one is used.

---

## 3. Core findings with exact numbers

| # | Finding | Numbers | Source (evidence ids) | Status |
|---|---|---|---|---|
| F1 | GPT-4 access did not help physicians in the Goh RCT | 50 physicians (26 attendings, 24 residents), 25 per arm, 244 cases, 6 vignettes, 60 min. Median 76% (IQR 66-87) vs 74% (63-84). Adjusted diff +2 (CI -4 to 8, P=.60). Power set for 8 points | Goh 2024 (a01, b01, c01) | [S] K03 |
| F2 | Same trial: model alone beat control physicians | 3 runs, median 92% (IQR 82-97). Versus conventional group +16 (CI 2-30, P=.03). Versus physician+GPT-4 about +16 (descriptive) | a02, b02, c02 | [S] K03 |
| F3 | Goh 2024 secondary results | Time 519 s vs 565 s (diff -82 s, CI -195 to 31, P=.20). Final-dx OR 1.4 ordinal (0.7-2.8), 1.9 binary (0.9-4.0, P=.10). Attendings +0.5 (P=.92), residents +3 (P=.50). Prior LLM use above monthly +5 (CI -7 to 16). Grader kappa 0.66, alpha 0.64 | a03-a05, c03, c04 | [S] |
| F4 | LLM assistance helped in management reasoning | 92 physicians, 5 vignettes, 375 scored cases. 43.0% vs 35.7%, diff +6.5 (CI 2.7-10.2, P<.001). Time +119 s (CI 17-221, P=.02). Diagnostic sub-score 56.8 vs 45.8 (+12.1, CI 3.1-21.0). Management sub-score +6.1 | Goh 2025 (a22, a23, b04, c22, d12) | [C] K04 |
| F5 | In management, physician+LLM equals LLM alone | 43.0% vs 43.7%, diff -0.9 (CI -9.0 to 7.2, P=.8). LLM alone vs control +7.3 (CI -0.7 to 15.4, P=.074). Severe-harm rating 7.6% vs 7.5% | a22, b05, c22 | [S] K05 |
| F6 | LLM alone beat unaided clinicians on CPC differentials | 302 cases. Top-10 59.1% vs 33.6% (P=.04). Top-1 29.2% vs 15.9% | McDuff (a06, b20, c06) | [E] K01 |
| F7 | Assisted clinicians improved but stayed below the LLM | Top-10: LLM-assisted 51.7-51.8%, search-assisted 44.4-44.5%, unaided 36.1% (McNemar 45.7, P<.01; vs search 4.75, P=.03). Top-1 25.2% vs 24.3%. LLM added the right dx in 73 cases vs 37 for search. About 2.9 queries per case | a07, b20, c06, c07 | [S] K02 |
| F8 | GPT-4 on CPC (first study) | 70 cases: in differential 64% (45/70), top-1 39% (27/70), mean rank 2.5, quality 4.2 (SD 1.3), kappa 0.57 | Kanjee (a09, b06, c05) | [E] K01 |
| F9 | o1-preview on CPC | 143 cases: in differential 78.3% (CI 70.7-84.8), top-1 52% (44-61). On the 70 shared cases 88.6% vs GPT-4 72.9% (P=.015). Correct next test 87.5%, helpful 11%, unhelpful 1.5% (132 cases). Rater kappa 0.66 (dx), 0.28 (test plan) | Brodeur (a10, a11, b07, c11) | [E] K01, K20 |
| F10 | Top-1 lags top-10 | 29.2% vs 59.1% (McDuff); 52% vs 78.3% (Brodeur); 39% vs 64% (Kanjee) | a06, a09, a10 | [E] K15 |
| F11 | o1 on reasoning-quality score | R-IDEA perfect: o1 78/80, GPT-4 47/80, attendings 28/80, residents 16/80 (all P<.0001). Historical controls | a11, b08, c12 | [E] K20 |
| F12 | o1 on management and landmark cases | Management (5 cases): o1 86% vs GPT-4 42%, physician+GPT-4 41%, physicians 34%; +41.6 vs GPT-4 (CI 22.9-60.4), +42.5 vs physician+GPT-4, +49.0 vs physicians (CI 31.7-66.3). Landmark (6 cases): o1 97% vs GPT-4 92%, physician+GPT-4 76%, physicians 74%; +20.2 (CI -0.4 to 40.9, P=.055) | a12, b09, c12, c13 | [S] |
| F13 | o1 on real ER records | 79 cases, exact or very close dx at triage / ER physician / admission: o1 65.8 / 69.6 / 79.7; attending 1 54.4 / 60.8 / 75.9; attending 2 48.1 / 50.6 / 68.4. Raters could not tell AI from human 83.5-84.6% | a13, b10, c13 | [S] |
| F14 | Contamination checks | o1 79.8% before vs 73.5% after cutoff (P=.59). McDuff 56 no-overlap cases: top-10 55.4% (all 302: 59.1%). Nori's 56 mostly post-cutoff test cases scored at least as high as the 304 set | a10, c07, d02 | [E] K18 (fragile) |
| F15 | Orchestration raised accuracy and cut cost | SDBench 56 test cases. Physicians (21, 764 diagnoses) 19.9% at $2,963, 11.8 min, 6.6 questions, 7.2 tests. GPT-4o 49.3% at $2,745. o3 78.6% at $7,850. MAI-DxO 81.9% at $4,735; budgeted 79.9% at about $2,396-2,397 (paper is inconsistent); ensemble 85.5% at $7,184. Best single physician 41% | Nori (a15, a16, b22, c16, c17, d01) | [S] K09 |
| F16 | Orchestration gain depends on base model | Significant gains (one-sided paired permutation, P<.005) for all families except o3 and o4-mini, where cost fell significantly instead. Weak models alone considered fewer diagnoses and never ordered confirming tests ("false economy") | a16, b23, c17 | [S] K10 |
| F17 | Conversational AMIE vs primary-care physicians | 149 scenarios, 20 PCPs, 20 patient actors. Better on 28/32 specialist axes and 24/26 patient-actor axes. Higher top-k DDx (FDR-corrected). Mean 149.8 turns. Plateau in first 10 turns | Tu (a18, b21, c08, c09) | [S] K16 |
| F18 | AMIE for management | 100 multi-visit scenarios, 21 PCPs, non-inferior on management; better precision of treatments and investigations | Palepu (c25, d13) | [S] |
| F19 | LLM users did worse than the model alone | 1,298 UK adults, 10 scenarios. LLM alone: conditions 94.9%, disposition 56.3%. With users: conditions below 34.5%, disposition below 44.2%. Control (no LLM): at least one relevant condition 47.0%; control odds 1.76 higher (CI 1.45-2.13) | Bean (b11, c14, d09) | [S] K06 |
| F20 | Where Bean's loss occurs | LLM raised a relevant condition in 65.7-73.2% of chats (GPT-4o 65.7, Llama 3 67.0, Command R+ 73.2). It suggested 2.21 conditions per chat, 34.0% correct (CI 32.3-35.9). Users listed 1.33 conditions, 38.7% correct | b12, d09 | [S] K06 |
| F21 | Benchmarks and simulated users do not predict human results | Models beat users on MedQA in 20/20 (GPT-4o), 19/20 (Llama 3), 17/20 (Command R+) scenarios. Question-answer score above interactive score in 26 of 30 model-scenario pairs. Simulated users 57.3% disposition, 60.7% conditions; regression of simulated on real -0.01 +/- 0.34 | b13, c15, d09 | [E] K12 (benchmark gap); [S] K23 (simulator) |
| F22 | Models drop when they must gather the case | Hager (MIMIC, 2,400 cases, 4 diseases, open Llama-2 models): full info 58.8 / 67.8 / 65.1% (Chat / OASST / WizardLM), autonomous 45.5 / 54.9 / 53.9%. 16-25 points below hospitalists on 80 patients (German resident 87.5%, US hospitalist 92.5%; P<.001) | a19, b14, c20 | [E] K07 |
| F23 | Same loss for 2024-26 models | GPT-4 iMedQA: full info 79.7%, initial info only 54.5%, no info 42.2%, basic interactive 55.4%, best interactive 66.1%. GPT-4o on 218 neurosurgery text cases: MC 89.0 to 60.9%, free response 78.4 to 30.3%. R1: 89.76% oracle, 76.18% free-turn, 71.79% one-turn (656 rare-disease cases) | d06, d07, c23 | [E] K07, K22 |
| F24 | AgentClinic | Claude 3.5 62.1%, GPT-4 51.6%, GPT-4o 34.2%, physicians 54% (N=20). Interaction limit N=10 gives 25%, N=20 gives 52%. Bias prompts cost GPT-4 about 2-4 points | d08 | [S] |
| F25 | Input order, amount and wording move open-model accuracy | Order shifts up to 18.0 points (Chat, pancreatitis), 7.9 (OASST), 5.4 (WizardLM). Only radiology reports: cholecystitis +18.5. Labs only: pancreatitis +21.6. "Final" vs "main" diagnosis: -10.6 to +7.0. Low-lab-value classification correct 26.5 / 70.2 / 45.8% | a20, b15, b16, c21 | [S] K08 |
| F26 | Reasoning-style prompts did not help | GPT-3.5 free response: CoT 46%, intuitive 48% (P=.4-.9), analytic 40% (P=.001), differential 38% (P<.001), Bayesian 42% (P=.02). GPT-4: CoT 76%, intuitive 77%, analytic 78%, differential 78% (P=.24), Bayesian 72% (-3.4, P=.07). NEJM challenge GPT-4: CoT 38% vs differential 34% | Savage (a24, b17, c19) | [S] K11 |
| F27 | Retrieval and search help modestly | Med-Gemini: +4.0 points top-10 on 303 CPCs with one search iteration; MedQA 87.2 to 91.1%. McDuff search arm +8 to +11 over unaided | c24, a07 | [E] K21 |
| F28 | Automation bias | 44 physicians (22 per arm), 264 cases. 73.3% with flawed LLM advice vs 84.9% with correct; adjusted -14.0 (CI -18.9 to -9.1 in d14; -19.7 to -8.3 in b24, unresolved). Top choice 76.1% vs 90.5% (-18.3) | b24, d14 | [S] K13 |
| F29 | Copilot simulation | 13 physicians, 260 consultations. Top-3 62.3 to 74.6% (OR 2.68, P=.01). Top-1 47.8 to 57% (OR 1.83, P=.08). Agreement with a wrong suggestion 38.8 vs 55.8% (OR 2.08, P=.09) | d15 | [S] K31 |
| F30 | Physician vs AI depends on which physicians | Meta-analysis, 83 studies (76% high risk of bias): pooled AI 52.1% (CI 47.0-57.1). Physicians +9.9 (P=.10). Non-experts +0.6 (P=.93). Experts +15.8 (CI 4.4-27.1, P=.007). Newer models not significantly worse than experts | Takita (b18, b19) | [S] K14 |
| F31 | Human-LLM meta-analysis is imprecise | 10 studies. Diagnostic accuracy (k=2): RR 1.59, CI 0.08-32.74. Composite score (k=2): +4.88 (CI 0.65-9.12; prediction interval -31.65 to 41.42). Time (k=3): +0.4 min, I2=70.1%. Factual error rate 26-36% | d11 | [C] K04 |
| F32 | Input style did not predict score | Four copy-paste/summary/query styles, two RCTs, linear mixed model | d10 | [S] K31 |
| F33 | Calibration is weak and rarely measured | Only 1.2% of 519 LLM health studies measured calibration; 5% used real patient data. GPT-4o: confidence 5 gave 83.2%, 3-4 gave 45.9%, under 3 gave 16.7%; 9 of 12 models never said "I don't know" | Bedi (b25), Griot (d19) | [E] K12; [S] K30 |
| F34 | Anchoring failure on hard emergency cases | 54 non-public cases, 6 LLMs, 972 scored responses. Anchoring failure 6.9-26.4%. Catastrophic failure 1.5% (two safest) vs 6.0%. 31 of 34 dangerous combinations stochastic | d18 | [S] K29 |
| F35 | Prompt-planted bias | 1,273 MedQA items, 7 biases. GPT-4 no bias 72.7%; false consensus 62.5%, frequency 62.7%, confirmation 72.5%. GPT-3.5 49.7 to 23.9-40.7%. Llama-2-70B 35.7 to 10.4-20.7%. Few-shot raised GPT-4 biased accuracy 67.3 to 74.9% | d16, d17 | [S] K28 |
| F36 | Debate and multi-agent outside medicine | 260 configurations, 6 benchmarks, 9 models, matched at 4,800 reasoning tokens: Finance Agent centralised +80.8%; PlanCraft -39.1% (hybrid), -70.0% (independent); SWE-bench independent -14.9%; mean change -0.3% (CI -58.7 to +77.2). Persuasive wrong agent: -10 to -40% accuracy, +30% wrong consensus (abstract only) | d03, d04 (abstract only), d05 (abstract only) | [S] K26, K27 |
| F37 | Rerank signal is weak | Perplexity scorer on 392 case reports, 823 correct vs 10,875 incorrect candidates: AUC 0.666 (CI 0.644-0.689); correct beat the mean wrong candidate in 88.1-91.1% of lists | d21 | [S] K15 note |
| F38 | Few studies use real data | 519 studies: 5% real patient data, 44.5% exam knowledge, 19.5% diagnosis, 95.4% accuracy as main measure, bias 15.8% | b25 | [E] K12 |

---

## 4. Mechanisms and models

Written so an engineer can build them. Each lists what the evidence supports and what it does not.

### 4.1 Differential generator and top-k scoring

Input: case text. Output: ordered list of N diagnoses (N about 5-10; Kanjee mean 9.0). Score:
- top-1 = correct dx is item 1.
- top-k = correct dx appears in the first k items.
- Rank = position of the correct dx (Kanjee mean 2.5).
- Match = judged by human or LLM grader ("exact or very close", Bond scale 0-5). Grader agreement is only moderate (kappa 0.57-0.66; 0.28 for test plans). Use a fixed rubric. If the grader is a model, blind it to the arm.

The steady gap top-1 < top-10 means *generation* is better than *ranking*. Log both. A system can win on top-10 and lose on top-1.

### 4.2 The sequential diagnosis loop (SDBench)

1. A gatekeeper model holds the full case and reveals a finding only when asked. Findings not in the source are synthesised (an o4-mini gatekeeper; limit noted in a16).
2. Each turn the agent asks a question, orders a test (each has a cost) or commits to a diagnosis.
3. Score = diagnosis correct (judge) plus total cost (visits and tests).
4. 304 NEJM CPC cases; 56 held out. Humans: 21 generalists, no search or colleagues.

The gatekeeper's quality caps the result. Cost is in dollars, not tokens (inference about $0.15 per case, treated as negligible, a17). So no published number is token-matched.

### 4.3 MAI-DxO panel (the structure to test, not to copy)

Five roles over one base model (c17):
- **Dr. Hypothesis**: keeps a probability-ranked list (top 3) with Bayesian-style updates.
- **Dr. Test-Chooser**: picks up to 3 tests that best separate hypotheses.
- **Dr. Challenger**: devil's advocate; checks for anchoring; looks for the finding that would refute the leader.
- **Dr. Stewardship**: weighs cost, vetoes low-value tests.
- **Dr. Checklist**: validates the format and test validity.

An orchestrator runs the roles in turn each round, then acts. Modes: no budget, budgeted, ensemble (several independent no-budget runs plus an aggregator). Unknown: which roles matter (no ablation, K25), whether the gain survives equal tokens (no control), whether the ensemble gain is panel structure or just sampling (85.5% vs 81.9% mixes both).

Tension with our schema. The roles are same-model personas. G4 says samples from one model are not independent and no persona voters on single-answer problems. G9 says no debate. A challenger is not a vote or a debate, but d05 shows a persuasive wrong challenger can derail a panel (-10 to -40%). So the version to test is a **challenger that must output a discriminating test or finding, checked against case facts by code**, not a free argument (K27). This is the same move as schema S7's counterexample search.

Worked example from the paper (c18, d02): a patient with alcohol withdrawal who had drunk hand sanitiser. Bare o3 fixated on antibiotic toxicity, ordered MRI and EEG, and was wrong at $3,431. MAI-DxO asked about in-hospital toxins first and was right at $795. One case, chosen by the authors; it shows the mechanism (a direct question beats a test chain) and nothing about frequency.

### 4.4 Elicitation as the bottleneck

Moving a case from a full vignette to a dialogue removes information the model must now ask for. Measured losses: 25 points (GPT-4 iMedQA 79.7 to 54.5), 28 points MC and 48 points free response (GPT-4o neurosurgery), 12-13 points (Llama-2, Hager), 18 points (R1, oracle to one-turn). Interactive asking recovers little unless the system decides *when it has enough*. MediQ's confidence-gated abstention raised GPT-4 from 55.4% to 66.1%, still 13.6 below full information (K24; the abstract's +22.3% could not be reproduced from the table).

Engineer's version: a **sufficiency check** before answering. List the key findings still missing for the top-2 hypotheses, ask for them, and commit only when the top hypothesis is separated or the question budget is spent. AMIE's truncation analysis (c09) shows a plateau within about 10 turns, so a hard cap near 10-20 questions should lose little. AgentClinic found N=10 interactions gave 25% and N=20 gave 52% (d08), so the cap matters a lot for weaker models and must be tuned.

### 4.5 Why aids fail at the consumer end

A model of the Goh 2024 null and the Bean loss, built from the sources. The parts are untested explanations.
1. Output must be read and merged. Goh 2024 physicians spent 519 s vs 565 s, so no extra time went into reconciling.
2. The user sees 2.21 conditions per chat, only 34.0% correct (b12), then selects. Users alone listed 1.33 conditions at 38.7% correct. Selecting from a noisy list can lose the right item.
3. Users give incomplete input. The LLM raised a relevant condition in 65.7-73.2% of chats, but users ended below 34.5%.
4. Flawed advice anchors: -14.0 points (F28).

Agent analogue: each stage of our scaffold reads the previous stage's text. A good first-stage list can be lost by a weak merge step. Test the merge, not only the generator (B12).

### 4.6 Search and retrieval as a tool

Med-Gemini triggers a web search on model uncertainty; one search iteration gives +4.0 top-10 on CPCs (c24). McDuff's search arm: +8 to +11 over unaided clinicians. The LLM arm beat search (4.75, P=.03). Retrieval is a modest, repeatable gain. Caveat: web pages may contain the solved case.

---

## 5. What holds up

### 5.1 Replicated or multi-source

| Claim | Independent sources | Note |
|---|---|---|
| LLM alone beats unaided physicians on written hard cases | McDuff 2023, Kanjee 2023, Brodeur 2024 (3) | Real for CPC puzzles and R-IDEA scoring. Not for the landmark set (P=.055) |
| Top-1 well below top-k | the same three | Always reported |
| Elicitation penalty for models | Hager, MediQ, neurosurgery conversion, R1 study, AgentClinic (4+) | All models were 2023-25; no o3-class test with a lossy patient |
| Benchmark scores do not predict interactive results | Bean, Bedi | Bean 26 of 30 pairs; Bedi 5% real data |
| Reasoning models beat GPT-4 | Brodeur (o1), Nori (o3 78.6 vs GPT-4o 49.3) | Two sources, different tasks |
| Contamination does not explain CPC results | Brodeur cutoff split, McDuff no-overlap, Nori test cases | Weak: low power; partial memorisation still possible. A 2026 study flags possible contamination in Gemini-2.5-Flash on unpublished prompts (d17) |
| Search helps a little | Med-Gemini, McDuff | +4 and +8 to +11 |
| Few cases, few raters | Goh 2024 (6 vignettes, 3 graders), Brodeur (5 and 6 cases) | Our own tests need 50 or more cases |

### 5.2 Failed, null or unresolved

- **Goh 2024 is a null for physician+LLM** (+2, CI -4 to 8). It was powered for 8 points, so true effects of 0 to 8 are not excluded.
- **Bean: null or negative for users** (below control).
- **No direct replication of any headline result** was found. Goh 2025 has no same-design replication (K04, d13). AMIE and a cardiology trial (9 cardiologists; AI-assisted responses preferred 46.7% vs 32.7%; clinically significant errors 13.1% vs 24.3%) are different designs.
- **Human + LLM benefit is contested**: +2, +6.5 and about +15 (K04). Explanations (task, tool, training, time limit) were never varied in one design.
- **Landmark o1 vs physicians, P=.055**, is not significant. "Superhuman" holds for CPC and R-IDEA, not there.
- **Meta-analyses are imprecise.** Takita: 76% of studies at high risk of bias, high heterogeneity. Wang 2026: k=2 per outcome with CIs that include everything.
- **Simulators over-estimate humans.** Bean's simulated users scored higher than humans and barely predicted them (K23).
- **Internal inconsistencies recorded:** Nori budget cost $2,396 vs $2,397 inside the paper; Qazi CI (-18.9 to -9.1 vs -19.7 to -8.3); MediQ +22.3% not reproduced; Bean control 47.0% (conditions) vs 43.0% (overall disposition, not a control-group condition rate); Goh 2025 text and abstract differ on the sign of the LLM-alone vs assisted difference (b04) and an erratum exists (d12); McDuff 51.7 vs 51.8.
- **Weak baselines.** Generalists in SDBench were barred from search and colleagues; McDuff clinicians read cases in isolation; the Goh LLM-alone arm was three runs by the authors with prompts they wrote.

### 5.3 Prompting interventions

- Forced analytic, differential or Bayesian prompts did not help GPT-3.5 (-6 to -8.9 points for analytic and differential) and made no significant change for GPT-4 (72-78% vs CoT 76%). Exam items, not real patients. Matches schema 4b ("telling the model to be analytic").
- Debiasing: planted bias hurts weak models far more than GPT-4 (F35). Few-shot and education prompts helped (GPT-4 67.3 to 70.9-74.9%). Bias awareness recovers only part of the damage. Reasoning mode did not reliably protect (Llama-3.3-70B and Gemini were more vulnerable to several biases with reasoning on; d17).
- Wording changes ("final" vs "main" diagnosis) moved open-model accuracy -10.6 to +7.0.

### 5.4 Moderators found

- **Model generation.** GPT-3.5 and GPT-4 significantly below experts; GPT-4o, Claude 3, Gemini 1.5 not significantly different (b19).
- **Physician expertise.** Experts +15.8 over AI; non-experts +0.6.
- **Base model under orchestration.** Gain larger for weak models.
- **Information provided.** More is not better for open models (withholding gave +18.5 to +21.6 in specific disease-model pairs).
- **Case time point (ER).** Gap to physicians largest at triage (65.8 vs 54.4 and 48.1) and smaller at admission (79.7 vs 75.9 and 68.4).
- **Disease.** Hager order effects were disease dependent.

---

## 6. Language models

| Generation | Examples | Result | Source |
|---|---|---|---|
| GPT-3.5 | ChatGPT | 71.7% on Merck vignettes; differential prompt hurt (38% vs CoT 46%) | a25, a24 |
| GPT-4 | | 64% in differential and 39% top-1 on 70 CPCs; 92% on landmark vignettes; 72.9% on the 70 shared cases; MedQA free response 76%; iMedQA 79.7% full info | a09, a02, a10, a24, d06 |
| Open 2023 models | Llama-2 70B variants | 58.8-67.8% full info on MIMIC, 45.5-54.9% autonomous; 16-25 points below hospitalists | a19, c20 |
| Gemini and AMIE class | AMIE, Med-Gemini | 59.1% top-10 on 302 CPCs (AMIE); +4 with search; wins on conversation axes | a06, c24, a18 |
| Reasoning | o1-preview | 78.3% in differential, 52% top-1; 88.6% on the 70 shared; R-IDEA 78/80; management 86% | a10-a12 |
| Reasoning | o3 | 78.6% on SDBench vs GPT-4o 49.3% | b22 |
| Reasoning | R1, o3-mini | R1 71.79% (1-turn) to 89.76% (oracle); o3-mini 64.99-67.19% | c23 |
| Agents | MAI-DxO (built on GPT-4.1, headline run with o3) | 81.9% at $4,735 (vs $7,850); ensemble 85.5% | c17, d01 |

**What changed performance, and by how much**

- GPT-4 to o1: +15.7 points on the shared 70 CPCs (88.6 vs 72.9). Perfect R-IDEA 47/80 to 78/80. Management 42% to 86%.
- GPT-4o to o3 on SDBench: 49.3% to 78.6% (+29.3).
- Adding the MAI-DxO panel to o3: +3.3 points accuracy and -40% cost ($7,850 to $4,735). Weaker models gained more accuracy (significant at P<.005 for all other families; per-model sizes were not recorded in our lines). Never checked at equal tokens.
- Ensembling the panel: 81.9 to 85.5% (+3.6) at $7,184, which is still below the $7,850 of single-pass o3.
- Adding search: about +4 points top-10.
- Turning a vignette into a dialogue: -25 to -48 points (GPT-4, GPT-4o).
- Confidence-gated asking: +10.7 points on iMedQA for GPT-4 (55.4 to 66.1).
- Prompt-planted bias: GPT-4 about -10 points (false consensus, frequency) to -0.2 (confirmation); weaker models -20 to -40.
- Changing an instruction word or the order of information: +/- 5 to 18 points on 2023 open models.

**Contamination and fragility.** CPC cases are public. Three tests show no large drop outside the training window, but all are weak. For reasoning models on post-cutoff real records there is no clean number (K32).

**Calibration.** Verbal confidence carries some signal for GPT-4o but is compressed near 5, and nine of twelve models never said "I don't know". Schema 4b already lists verbal confidence as a stop rule that does not work. Nothing here changes it.

**Stochastic failure.** 31 of 34 dangerous output patterns in the emergency study appeared in only some of three queries. Repeated sampling exposes failures one run hides (K29).

---

## 7. What our agent should take

Schema key: G = guardrail, S = state, O = operator, M = memory. Status: [E] established, [S] single source, [C] contested. "Add now" means the claim is established and fits an existing rule. Nothing in "Test first" goes into SCHEMA.md until its test passes (see UNKNOWNS.md).

### 7.1 Add now (established)

| # | Take | Schema part | Status | Evidence |
|---|---|---|---|---|
| A1 | **Validate on interactive, open-ended, post-cutoff items, not only exam-style items.** Benchmark knowledge does not predict interactive results (26 of 30 pairs; 20/20 scenarios); only 5% of health-LLM studies used real data. Extends G7 | G7 | [E] K12 | b13, b25, c15 |
| A2 | **Use at least 50 items and bootstrap intervals; report against novice and expert baselines.** Six vignettes could not tell +2 from +8 | G7 | [E] K19 | a05, a12, b09 |
| A3 | **Generation is better than ranking: log top-1 and top-k separately.** The right idea is on the list far more often than it is first. Treat any selection step as the weak link and measure it | S7 | [E] K15 | a06, a09, a10 |
| A4 | **Treat information gathering as its own measured skill.** Report the full-information run and the must-ask run side by side. A 12-48 point drop is the norm for 2023-25 models | S1 | [E] K07 | a19, b14, c20, d06, d07, c23 |
| A5 | **Test on post-cutoff items.** Contamination is not proven but cannot be ruled out | G7 | [E] K18 (fragile) | a10, c07, d02 |
| A6 | **A retrieval step is a small, repeatable gain.** Include as a memory tool and test on vs off | M | [E] K21 | c24, a07 |
| A7 | **Do not force a reasoning style (analytic, differential, Bayesian).** Adds diagnosis-specific evidence to the existing 4b row | S3 | [S] K11 here; [E] in 4b | a24, b17, c19 |
| A8 | **A reasoning-model base beats an older scaffold-free model by far.** Pick the base first; the scaffold sits on top | S0, G11 | [E] K20 | a11, b22 |

A1-A5 and A8 are bench rules rather than schema elements. A6 and A7 are the only ones that touch the machinery.

### 7.2 Test first (not established)

| # | Candidate | Schema part | Status | Evidence | Why not now |
|---|---|---|---|---|---|
| T1 | **Challenger tied to a discriminating test**: name the finding that would separate the top two, ask for it, update | O (S7 counterexample search) | [S] K09, K27 | c17, c18, d05 | One source, no role ablation, no equal-token control; free-form challengers can derail (d05); G9 says no debate |
| T2 | **Sufficiency check before answering or asking** | S1 | [S] K24 | d06 | One source; abstract's gain not reproduced |
| T3 | **Cost-aware test chooser**: rank next questions by expected information gain per cost; stop when value is low | O, S6 | [S] K09 | c17, a17 | Only dollars measured; see Expected information gain models |
| T4 | **Rerank or discriminate step after generation** (to close top-1 vs top-10) | S7 | [S] K15 note | d21 | Only a weak perplexity reranker tested (AUC 0.666); G5 needs code to select |
| T5 | **Resample the final answer and flag disagreement** | S7, G4 | [S] K29 | d18 | Failures were stochastic; agreement is only a hint (G4) |
| T6 | **Input hygiene for planted hypotheses**: move stated guesses into a marked block | S1 | [S] K28 | d16, d17, d08 | Anchoring on a wrong prior hypothesis not directly tested in agents |
| T7 | **Robustness check on order of case facts** | G | [S] K08 | a20, b15, b16, c21 | Open 2023 models only |
| T8 | **Structured, short, ranked output between stages** | S3, S7 | [S] K31 | d10, d15 | Human-in-the-loop only; output format never varied in a controlled design |
| T9 | **Role panel vs self-consistency at equal tokens** | O1-O8 | [S] K25, K26 | d01, d03 | Non-medical equal-token work says panels can hurt (-0.3% mean) |
| T10 | **Sample consistency as a stop signal** (not verbal confidence) | G | [S] K30 | d19, d20 | Verbal confidence is in 4b; consistency is only a hint |

Blocked by the schema: free-form multi-persona debate (G9, 4b), verbal confidence as a stop rule (4b), bias checklists (4b). See section 9.

---

## 8. Concrete tests on our bench

All arms get the same token budget, counted including setup (G7). At least 50 items per test, bootstrapped intervals, post-cutoff cases included. "Plain" = single pass on the same base model with the best short prompt. Cost in tokens, not dollars.

| # | Item type | Arms (equal tokens) | Metric | Expected effect |
|---|---|---|---|---|
| B1 | CPC-style written cases (post-cutoff where possible) | plain single pass vs our scaffold vs best-of-N with self-consistency | top-1 and top-10 (blinded grader, fixed rubric) | Scaffold +3 to +5 points top-1 over plain; no loss on top-10. If not, the scaffold adds nothing in this domain |
| B2 | The same cases, given as full text vs through a lossy patient simulator | agent without sufficiency check vs with check, equal question and token budget | accuracy drop (full minus simulated); questions asked | Drop 15-30 points for plain; the check recovers 5-10 (MediQ 55.4 to 66.1) |
| B3 | 10 of the same items with a human-played patient | best arm of B2 | rank agreement of simulator and human | Per Bean the simulator may not rank well; if rank correlation is below 0.5, stop using the simulator to rank variants |
| B4 | CPC cases with a planted wrong early hypothesis in context | no challenger vs evidence-tied challenger vs free-argument challenger | right-to-wrong switch rate; accuracy | Plant costs plain 5-15 points; evidence-tied challenger halves it; free challenger no better or worse (d05) |
| B5 | Same cases | single pass vs panel (hypothesis, test chooser, challenger, stewardship) vs 4 independent samples with vote | top-1; tokens per case | Panel at best equal to the vote at equal tokens; a win of 3 or more points means role design matters |
| B6 | Same cases, drop-one-role ablation of the winning panel | full vs minus each role | top-1 change per role | Shows which role carries the gain (K25) |
| B7 | Same cases | plain top-10 vs top-10 plus a code-run rerank stage (pairwise discrimination by the model, positions shuffled, scores length-normalised) | top-1 | +3 to +8 points top-1 if ranking is the weak link (K15) |
| B8 | Same cases, 5 shuffled orders of case facts | plain vs scaffold | accuracy spread across orders | Scaffold spread smaller than plain |
| B9 | Same cases with a stated "likely diagnosis" planted vs removed by input hygiene | with vs without hygiene | accuracy under plant | Hygiene recovers part of the loss (d16: GPT-4 lost 0.2 to 10 points) |
| B10 | Same cases | retrieval on vs off | top-10 | +3 to +5 points (Med-Gemini +4) |
| B11 | Same cases | verbal confidence vs sample agreement as predictor of top-1 correctness | AUC | Sample agreement above verbal confidence; check before relying on either (K30) |
| B12 | Stage-1 output handed to a second stage that must merge it with its own view | consumer sees full ranked list vs short top-3 vs free text | final accuracy; how often a correct stage-1 item is dropped | Tests the Goh/Bean consumer loss inside the agent (K03, K31) |

---

## 9. What does not transfer, and why

- **Human-user failure.** Bean and Goh 2024 are about people reading and prompting. Our agent has no lay user. Only the stage-to-stage hand-off transfers (B12).
- **Automation bias.** The -14 points is a human result. The agent analogue (a wrong early hypothesis in its own context) is untested. Do not assume the same size.
- **CPC difficulty.** CPCs are puzzle cases with one answer and a published solution. Rankings may not hold on routine cases or on problems with no ground truth.
- **Costs in dollars.** MAI-DxO's savings are test dollars, not tokens. Inference was about $0.15 per case and ignored. Our metric is tokens, so the cost result gives no support for token efficiency.
- **Physician baselines.** Weak baselines inflate "model beats doctors". It is not a statement about the gain a scaffold adds.
- **Persona panels.** MAI-DxO personas share one model's errors (G4). The gain may be sampling plus a better prompt, not role insight. Equal-token work outside medicine finds multi-agent gains depend on the task (+80.8% to -70.0%).
- **Verbal confidence.** Stays out (4b). The GPT-4o 83.2% vs 16.7% split is real but compressed; most models say 5 always.
- **Exam evidence.** Savage's prompt results and the bias studies use MedQA-style items and old models. Do not infer current reasoning-model behaviour on open cases.
- **Elicitation sizes.** Part of the dialogue drop is simulator limits (vignettes not written for dialogue; d07). Treat the size as an upper bound.
- **Safety and regulation.** Harm ratings, deployment advice and false-positive rates are out of scope (SDBench has no healthy cases).

---

## 10. Open questions

From critique.md GAPS, updated by the 2026-11-01 gap pass.

1. **Scaffold with an explicit challenger vs the same base model at equal tokens.** Open. No token-controlled diagnosis study exists.
2. **Role ablation vs more sampling in MAI-DxO.** Open. The ensemble mixes both.
3. **Elicitation penalty for o3-class and Claude-class models with a lossy patient.** Partial, leaning yes (GPT-4o -28 and -48; GPT-4 -25). Frontier test missing.
4. **Is the human-plus-LLM failure caused by output format and prompting?** Open. Input style did not predict score; no study varies output format.
5. **Can a rerank stage close the top-1 vs top-10 gap, and at what token cost?** Open. Only a weak perplexity scorer was tried.
6. **Do reasoning models lose accuracy on post-cutoff real records?** Open, with weak indirect evidence of no loss.
7. **Does diagnostic confidence predict top-1 correctness on CPC cases?** Partial. Only multiple-choice and four-disease image data.
8. **Is there an agent analogue to automation bias, and does a challenger reduce it?** Partial. Prompt-planted bias hurts weak models; no direct anchoring-in-agent test.
9. **Are forced differential or Bayesian prompts harmful only for weaker models?** Open for current models.
10. **Has Goh 2025 been replicated with other physicians or newer models?** Open.
11. Why was LLM-alone strong yet physician+LLM not? Candidates: interface, training, task, time. Never isolated.
12. Does the LLM-alone result depend on who wrote the prompts? In Goh 2024 the study team wrote them, so the arm is not a naive-user arm.
13. Do the Goh 2025 erratum and the abstract/text sign discrepancy change the +6.5? Not checked.
14. Nori's "false economy" in weak models (never ordering confirming tests): generic to weak models? Does a stewardship role reduce it or cause it?

Search limits in the last pass: WebSearch quota exhausted; arXiv, Semantic Scholar and OpenAlex returned HTTP 429. Absence of studies for gaps 5, 6 and 9 is weak evidence of absence.

---

## 11. Sources

[V] = opened and read as text. [M] = abstract, snippet or memory only.

**Founding and early**
- [V] Bond et al. 2012, Differential diagnosis generators: an evaluation. https://pmc.ncbi.nlm.nih.gov/articles/PMC3270234/
- [M] Miller, Pople, Myers 1982 INTERNIST-1; Berner et al. 1994. https://www.nejm.org/doi/full/10.1056/NEJM199406233302506
- [M] Semigran et al. 2015, symptom checkers (from memory). https://www.bmj.com/content/351/bmj.h3480
- [M] Ledley and Lusted 1959, via Brodeur introduction. https://arxiv.org/abs/2412.10849

**LLM vs physicians, physician-assist trials**
- [V] Goh et al. 2024, LLM influence on diagnostic reasoning, JAMA Netw Open. https://pmc.ncbi.nlm.nih.gov/articles/PMC11519755/ ; https://doi.org/10.1001/jamanetworkopen.2024.40969
- [V] Goh et al. 2025, GPT-4 assistance for management reasoning, Nat Med. https://pmc.ncbi.nlm.nih.gov/articles/PMC12380382/ ; https://doi.org/10.1038/s41591-024-03456-y (the critique says the full text was not on disk; abstract-level numbers agree across lines)
- [V] Kanjee, Crowe, Rodman 2023, accuracy of GPT-4 on NEJM CPCs. https://pmc.ncbi.nlm.nih.gov/articles/PMC10273128/ ; https://jamanetwork.com/journals/jama/fullarticle/2806457
- [V] McDuff et al. 2023/2025, Towards accurate differential diagnosis with LLMs. https://arxiv.org/abs/2312.00164 ; https://pmc.ncbi.nlm.nih.gov/articles/PMC12158753/
- [V] Brodeur et al. 2024, Superhuman performance of an LLM on the reasoning tasks of a physician. https://arxiv.org/abs/2412.10849
- [V] Rao et al. 2023, ChatGPT through the clinical workflow. https://pmc.ncbi.nlm.nih.gov/articles/PMC10481210/
- [M] Eriksen, Moller, Ryg 2023, GPT-4 on complex cases. https://ai.nejm.org/doi/full/10.1056/AIp2300031
- [V] Savage et al. 2024, Diagnostic reasoning prompts. https://pmc.ncbi.nlm.nih.gov/articles/PMC10808088/ ; https://arxiv.org/abs/2308.06834
- [V] Nori et al. 2023, Capabilities of GPT-4 on medical challenge problems. https://arxiv.org/abs/2303.13375

**Orchestration and conversational systems**
- [V] Nori et al. 2025, Sequential diagnosis with language models (SDBench, MAI-DxO). https://arxiv.org/abs/2506.22405
- [V] Tu et al. 2024, Towards conversational diagnostic AI (AMIE). https://arxiv.org/abs/2401.05654
- [V] Palepu et al. 2025, conversational AI for disease management (abstract and introduction only). https://arxiv.org/abs/2503.06074
- [V] Saab et al. 2024, Capabilities of Gemini models in medicine. https://arxiv.org/abs/2404.18416

**Interaction and elicitation**
- [V] Bean et al. 2025, Clinical knowledge in LLMs does not translate to human interactions. https://arxiv.org/abs/2504.18919
- [V] Hager et al. 2024, Evaluation and mitigation of limitations of LLMs in clinical decision-making. https://pmc.ncbi.nlm.nih.gov/articles/PMC11405275/
- [V] Qiu et al. 2025, Quantifying the reasoning abilities of LLMs on clinical cases. https://arxiv.org/abs/2503.04691
- [V] Li et al. 2024, MediQ. https://arxiv.org/abs/2406.00922
- [V] Neurosurgery vignette-to-conversation study 2026. https://doi.org/10.1227/neuprac.0000000000000217
- [V] Schmidgall et al. 2024, AgentClinic. https://arxiv.org/abs/2405.07960
- [M] Siden et al. 2025, typology of physician input approaches. https://doi.org/10.1038/s41746-025-02184-y

**Meta-analyses and reviews**
- [V] Takita et al. 2025, systematic review and meta-analysis of generative AI diagnostic performance. https://pmc.ncbi.nlm.nih.gov/articles/PMC11929846/
- [M] Wang et al. 2026, Human-LLM collaboration in clinical medicine (meta-analysis). https://doi.org/10.1038/s41746-026-02382-2
- [M] Bedi et al. 2025, Testing and evaluation of health care applications of LLMs, JAMA. https://doi.org/10.1001/jama.2024.21700

**Bias, calibration, automation bias, multi-agent**
- [M] Qazi et al. 2026, Automation bias in LLM-assisted diagnosis. https://doi.org/10.1056/aioa2501001 ; https://www.medrxiv.org/content/10.1101/2025.08.23.25334280
- [M] Real-time AI diagnostic copilot in simulated primary care. https://doi.org/10.2196/104579
- [V] Schmidgall et al. 2024, cognitive biases in LLMs for medical QA. https://arxiv.org/abs/2402.08113
- [M] Kim et al. 2026, fragility of LLM reasoning through biases. https://doi.org/10.1136/bmjdhai-2025-000189
- [M] Liu et al. 2026, evaluating LLM safety on emergency cases. https://doi.org/10.1007/s10916-026-02459-1
- [V] Griot et al. 2025, LLMs lack essential metacognition. https://doi.org/10.1038/s41467-024-55628-6
- [M] Oral autoimmune blistering disease multimodal LLM study (calibration). https://doi.org/10.3390/diagnostics16172761
- [M] Conditional perplexity scoring for differentials. https://doi.org/10.2196/98819
- [V] Towards a science of scaling agent systems. https://arxiv.org/abs/2512.08296
- [M] Stop overvaluing multi-agent debate. https://arxiv.org/abs/2502.08788
- [M] Kraidia et al. 2026, persuasion derails collaboration. https://doi.org/10.1038/s41598-026-42705-7
- [M] Replication search for Goh 2025 (AMIE management; cardiology trial). https://doi.org/10.1038/s41586-026-10764-5
- [M] Search note for gaps 5, 6 and 9. https://www.ebi.ac.uk/europepmc/

## Source audit (2026-11-01)

Fresh auditors re-opened the sources of 8 established claims: 5 confirmed as written, 3 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **E01.09-K12** (reworded: the sources support less). Bean et al. report 20/20 scenarios only for GPT-4o (Llama 3 19/20, Command R+ 17/20) and the comparison is MedQA accuracy vs users' accuracy with the model; the Bedi 519/5 percent figure is true (JAMA 2025) but is not among the listed evidence. Corrected claim: Benchmark knowledge scores do not predict interactive or real-case performance: in Bean et al., MedQA accuracy exceeded the accuracy of users working with the model in 20/20 scenarios for GPT-4o (19/20 for Llama 3, 17/20 for Command R+), with benchmark scores above 80 percent matching human scores below 20 percent in several cases; only 5 percent of 519 LLM health care evaluation studies used real patient care data (Bedi et al., JAMA 2025).
- **E01.09-K18** (reworded: the sources support less). Non-significant before/after-cutoff difference (79.8 vs 73.5, P=.59) in 143 cases and McDuff's 56-case no-overlap subset (55.4 vs 59.1 top-10) are reassuring but cannot show that contamination plays no role. Corrected claim: Training-data contamination is not evident in the CPC results: o1 scored 79.8% before vs 73.5% after its training cutoff (P=.59, not significant) and McDuff's 56-case no-overlap subset gave 55.4% top-10 versus 59.1% on the full set; these small checks cannot rule contamination out.
- **E01.09-K19** (reworded: the sources support less). Goh 2024 had 50 physicians completing 244 cases (6 vignettes each), each case graded by 2 scorers, with kappa 0.66 among 3 graders; 'very few cases and raters' fits Brodeur's 6 landmark cases (P=.055) but not Goh's participant count. Corrected claim: Physician-vs-LLM comparisons can rest on few cases: Goh 2024 used 6 vignettes (50 physicians, 244 completed cases, each graded by 2 of 3 scorers, weighted kappa 0.66) and Brodeur's o1 vs physician landmark comparison on the same 6 cases gave a 20.2-point difference with P=.055, not significant.
