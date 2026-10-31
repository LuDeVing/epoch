# Knowledge organisation: illness scripts, categories: deep document

*Subfield E01.03. Written from evidence_a-d.jsonl (91 evidence lines, about 70 independent sources), claims.jsonl (33 claims) and critique.md in this folder. Evidence ids (a01, b17, d13 ...) point to those files. Claim ids are E01.03-K01 to K33, written K01 etc. Status marks follow SCHEMA.md: [E] established, [S] single-source, [C] contested. Two extra marks: [P] preliminary (several independent preprints, none at equal tokens) and [O?] open (untested).*

*Reading warning. Most founding human studies (1987-2009) were read as abstracts only. Their sample sizes are often missing. Every LLM result from 2026 with an arXiv id above 2600 is a preprint, mostly from one lab. Numbers are given as the sources report them. Where we computed a number ourselves, it says so.*

## 1. What it is

The subfield asks one question. When a doctor sees a case, what is stored in memory, how is it organised, and how does that organisation produce a diagnosis?

The main answer in medical education is the **illness script**. An illness script is a stored description of one disease (or one class of patients). It has three kinds of content:

- **Enabling conditions.** Who gets it, when, where, with what risk factors. Age, sex, history, setting, exposure.
- **Fault.** What goes wrong in the body. The mechanism, in short form.
- **Consequences.** What the disease does. Symptoms, signs, test results, course.

A script is goal-directed. It makes predictions: if this is disease X, then feature Y should be present. It lets the doctor match a case quickly (a02, a04, a05). The script is the unit of the "class library" in our schema. S2 REPRESENT must turn the raw case into a form that can be matched against such classes.

Four connected ideas sit in this subfield:

1. **Knowledge encapsulation.** Long causal chains learned in school get packed under short clinical labels ("sepsis" for a chain from contaminated syringe to fever). The detail is still there but hidden (a02, a03).
2. **Illness scripts.** After encapsulation, the labels are reorganised into scripts with slots (a01, a04).
3. **Exemplars.** Rival view. Diagnosis rests partly on similarity to specific past patients, not on abstract prototypes (a08, a09, d07).
4. **Categories by action.** Experts group patients by what to do (management) more than by surface features (a16).

Why it matters for our agent. The agent cannot be trained. It can only get scripts as text in context: a stored class library, retrieved on demand. The human literature tells us what such a library should contain (enabling conditions, contrast with neighbours, short why-notes, worked cases), when it helps (fast recognition, delayed use, hard cases) and where it fails (atypical cases, anchoring, base rates). The LLM literature tells us how far models already do this unaided and what breaks.

Boundary. Process questions (hypothetico-deductive versus pattern recognition as a speed choice, bias, cognitive forcing) belong to other E01 subfields. We cover them only where they touch knowledge organisation. Links to parallel subfields: Case representation (S2 format), Encoding specificity and cue-dependent retrieval (how stored classes are cued), Einstellung effect (anchoring on a common class), Structure mapping (matching case to class), Sampling and voting (equal-token comparisons).

## 2. History and theories in depth

### 2.1 Origins (1970s-1990)

- **AI origin.** The script idea came from general psychology and AI, entered medicine through AI diagnostic systems, and was then specified by educators (b16, Custers 2015). INTERNIST-1 (Miller, Pople and Myers 1982) is the machine ancestor: a library of disease profiles with frequency and "evoking strength" weights. Findings evoke candidates, then the leading candidates choose the next question (c26, record seen only). This is the "evoke, then discriminate" loop that LLM scaffolds re-create.
- **Hypothetico-deductive era.** The 1970s view said experts generate hypotheses early and test them. Critics noted it does not separate novice from expert and is not sequential in practice (a19). So the field moved from process models to knowledge-structure models.
- **Schmidt, Norman and Boshuizen (1990), founding statement (a01).** Expertise is not better reasoning or deeper pathophysiology. It rests on stored structures that describe prototypical or real patients. Intermediate students instead use long causal chains. The theory explains five phenomena: content specificity, differences in data gathering, standard setting, decline on some measures with expertise, and errors linked to long response times in visual diagnosis. It is a review-and-proposal, not one experiment. Abstract only.

### 2.2 The staged account (Schmidt and Rikers 2007; a02, b01-b05)

Development goes in stages:

1. **Causal networks.** Novices learn disease mechanisms as long chains.
2. **Encapsulation.** With practice, chains get short labels. Experts' protocols hold fewer biomedical and more encapsulating concepts than students' (b03).
3. **Illness scripts.** Labels are organised into scripts with enabling conditions, fault, consequences.
4. **Instance scripts.** Individual remembered patients, kept beside the disease prototypes (a03).

Predictions that were tested:

- Experts diagnose faster and say less about mechanism.
- Experts recall less case detail than intermediates (the intermediate effect, 2.4).
- Biomedical knowledge is not lost; it is reachable behind labels.
- Enabling conditions drive first hypotheses (Hobus 1987; Custers 1996, 1998).

### 2.3 Rival and supplementary accounts

- **Exemplar view (Brooks, Norman, Allen 1991; Norman and Brooks 1997; Norman, Young, Brooks 2007).** Seen similar cases help diagnosis more than dissimilar cases in the same category, and the effect held after two weeks (a08). In dermatology specific similarity explains about 30% of diagnosis. About 40% of errors by residents, GPs and dermatologists were on typical slides. A positive history raised the features seen by about 50%. Experts predicted only 11-60% of colleagues' errors (d07). The group argues retrieval is fast and not open to introspection, and that an early hypothesis changes how later findings are read (d08).
- **Causal-model view (Woods, Brooks, Norman 2007; Kulasegaram 2015).** Biomedical knowledge is not discarded; it acts as glue that keeps feature sets in memory (a13, a14, b09).
- **Active biomedical knowledge (Rikers 2005; de Bruin 2005; Patel 1990).** Physicians judged diagnostic words faster than biomedical words, yet were faster at both, so mechanism stays active (a11). A path model with basic science integrated into clinical knowledge fitted best (a12).
- **Management-based categories (Devantier 2009; a16).** Experts matched patients on management category more than novices. Residents did not differ from experts.
- **Script theory proper (Charlin, Boshuizen, Custers, Feltovich 2007; Lubarsky 2015; a04, a05).** A script yields expectations, checks features, guides action. The working loop is activation from early cues, gauging fit between actual and expected features, instantiation (filling slots). Processing runs on a continuum from rapid pattern recognition to slow analytic reasoning, depending on script quality, complexity, stakes and time.
- **Nursing extension (a20).** A directed content analysis of 3,912 statements from expert nurses on 20 problems found the script parts apply, and proposed five new components: management, boundary, impact, occurrence, explicative.

### 2.4 The intermediate effect

Students at a middle level recall more detail of a case than experts or novices. The inverted U was taken as proof that experts compress. Its history is messy (b01, b02, d02-d06):

- Schmidt and Boshuizen (1993): two experiments; the effect vanished when study time was cut and was produced by priming pathophysiology (d02).
- Rikers, Schmidt, Boshuizen (2000): neurologists, 2nd- and 6th-year students on four cardiology and pulmonology cases outside the neurologists' field. Neurologists were faster and more accurate; 6th-year students recalled most (d04).
- Van de Wiel, Schmidt, Boshuizen (1998): a failed replication by the same group. Recall rose in a straight line with expertise. Cutting study time (3 min, 1 min 15 s, 30 s) hurt recall at all levels (d03).
- Wimmers (2005) and Norman: the expert recall advantage returns only if experts must comment on each finding (d05, b02).
- Eberhard (2009): the effect in dentistry, 61 students and 20 dentists, 3 cases (d06).
- Eva and colleagues: effect also found in recognition, so not only a free-recall artefact (b01).

### 2.5 The Script Concordance Test (SCT)

Charlin and colleagues (2000) built a test from script theory (a06). The examinee reads a short case, a hypothesis, and a new piece of data, and rates whether the data makes the hypothesis more or less likely. Scoring compares answers with a panel of experts. About 100 items from 25-30 cases and 10-20 panellists give reliable scores (b15). Scores correlate poorly with factual knowledge (b14). The SCT is the closest human test of "does the person update a hypothesis the way an expert would", which is why it is used to probe LLMs (section 6).

### 2.6 Where the field stands

Schmidt and Rikers (2007): most studies fit the staged view; debate remains about the role of biomedical knowledge (a02). Norman and colleagues (2017) argue that both fast and slow processes cause error, that teaching bias recognition does not reduce errors, and that reorganising knowledge gives small but consistent benefit (a18). Their practical message: fix knowledge organisation before adding bias checks. That is the stance of this schema (4b: bias checklists do not work).

## 3. Core findings with exact numbers

"Abstract" means only the abstract was read.

### 3.1 Human studies

| Finding | Numbers | Source (ids) | Status |
|---|---|---|---|
| Experts use enabling conditions to generate first hypotheses | 18 experts and 17 novices, 32 case histories. Experts produced almost 50% more correct hypotheses; only experts showed high correlation of accuracy with recall | Hobus 1987 (a07), abstract | [E] (K07) |
| Enabling conditions rise with expertise and patients seen | Custers 1998; Custers 1996: experts sensitive to typicality of enabling conditions and consequences, advanced students only to consequences; van Schaik 2005: consequences also matter, against script theory | b04 (via review) | [E] (K07), caveat on consequences |
| Teaching enabling conditions enriched scripts | N=32 within-subject. Richness 14.47 (SD 3.25) vs 12.14 (SD 2.80), p<0.001, about 20% higher. Diagnostic score 1.63 vs 1.15, p<0.001. Exam vs recognition r=0.571; exam vs richness r=-0.006 | Keemink 2018 (a17, d10) | [E] for the gain; richness is a weak proxy for exam skill |
| Intermediate effect | Inverted U in recall; 6th-year students recalled most; 4 cases. Group sizes not recovered | Rikers 2000 (a10, d04); Schmidt and Boshuizen 1993 (d02) | [C] (K02) |
| Intermediate effect failed to reproduce | Recall linear with expertise; 4 internal medicine cases; 3 study times | van de Wiel 1998 (d03) | [C] |
| Intermediate effect in dentistry | 61 students, 20 dentists, 3 cases; interrater agreement 96.2%; diagnostic trend p<0.001 | Eberhard 2009 (d06) | [C] |
| Expert recall advantage only with forced elaboration | 6 cases, 3 conditions (lab only, lab plus elaboration, lab plus context); elaboration changed only experts | Wimmers 2005 (d05); b02 | [C] |
| Instruction, summary data, or being judged did not change the intermediate effect | no figures | Schmidt and Rikers review (b01) | [E] as reported by the review |
| Biomedical knowledge still active in experts | 15 family physicians, 20 4th-year students, 60 clinical texts; physicians faster at both word types | Rikers 2005 (a11) | [E] (K03) |
| Basic science integrated into clinical knowledge fits best | 44 of 59 physicians (75%), 184 students | de Bruin 2005 (a12) | [E] (K03) |
| Causal learning protects accuracy over a week | Exp 1: 89% vs 78% correct after delay. Exp 2: reliance on causal information 57% vs 43% | Woods 2007 (a13, b07) | [E] (K03) |
| Explicit causal links help, co-location does not | N=94, 4 arms; condition x time F(3,88)=3.05, P<.03, partial eta 0.10; equal immediate scores; causal group decayed least after a week | Kulasegaram 2015 (b09) | [E] (K03) |
| Speed-accuracy crossover for causal learners | Speeded 71% vs 66%; thorough 67% vs 73%; encapsulated/novel words 50% vs 41%, P=0.02; undergraduates, 4 artificial diseases | Woods 2006 (b08) | [S] (K04) |
| Specific similarity is part of diagnosis | Dermatology about 30%; about 40% of errors on typical slides; positive history raised seen features by about 50% | Norman and Brooks 1997 (d07) | [E] (K05), abstract |
| Seen similar cases help | 3 experiments, residents and GPs; held after 2 weeks; no figures | Brooks 1991 (a08) | [E] (K05) |
| Feature plus similarity beats either | N=48, 12 per group, 10 cardiac diagnoses on ECG: feature-first 42%, first-impression 41%, explicit combined 56%, implicit combined 53% (both p<.01) | Ark 2006 (b10, d01) | single lab, no replication found (K05) |
| Interleaved practice beats blocked | 46% vs 30% on novel ECGs, p<0.05; instruction format no effect | Hatala 2003 (b11) | [S] (K06) |
| Experts categorise on management | invited 130 novices, 11 intermediates, 159 endocrinologists; completers 15, 11, 8. Novices vs experts t(68)=-3.63, p=.0006; intermediates vs experts t(68)=-0.24, p=.81 | Devantier 2009 (a16) | [S] (K08) |
| Pattern recognition and scheme-inductive reasoning more often right than hypothetico-deductive | logistic regression on think-aloud, gastroenterology, 4 presentations; no odds ratios | Coderre 2003 (a15 and b12 are one paper) | [S] (K09), observational |
| Dual-processing instruction did not change accuracy | 3 randomised experiments, cardiac simulator, three experience levels | Sibbald 2013 (d09) | [S] |
| Guided reflection the most consistently helpful dual-process aid | 28 studies, five categories; guided reflection successful in 5 studies; no pooled effect | Lambe 2016 (b13) | [E] as a narrative review |
| Illness-script format beats symptom list | N=100 (50 per arm). Knowledge 15.74 (SD 2.47) vs 14.38 (SD 2.59) of 20, P=0.009, d=0.54 (derived by the first agent, not reported). SCT 6.12 (SD 1.95) vs 4.54 (SD 1.56) of 10, P=0.0001 | Moghadami 2021 (b17) | [S] (K10) |
| Written recall tracks training year | COPD correct ideas median 3 (year 1) vs 14 (year 5); MI 8 vs 18 (p<0.01); organisation 0.31 to 0.61 (COPD); progress-test rho 0.56 and 0.46; encapsulation terms rare at every level | Valente 2026 (b18) | [S] (K11), abstract |
| SCT reliability design | 848 references, 80 analysed; about 100 items; panel 10-20 | Dory 2012 (b15) | [E] (K12) |
| Chatbot feedback improved script writing | 83 students; composite OR 3.2 at T2, 2.7 at T3 on new cases | c19 | [S] (K22), abstract |

### 3.2 LLM studies

| Finding | Numbers | Source (ids) | Status |
|---|---|---|---|
| GPT-4 on NEJM clinicopathologic cases | 70 of 80 cases analysed. 45/70 (64%) correct in differential, 27/70 (39%) top; mean differential 9.0; mean rank 2.5; scorer agreement 66%, kappa 0.57 | Kanjee 2023 (a21) | [E] (K16) |
| o1-preview on NEJM | 143 cases: 78.3% in differential (CI 70.7-84.8), 52% first (44-61). On 70 shared cases 88.6% vs GPT-4 72.9% (p=.015). R-IDEA perfect 78/80 vs GPT-4 47/80, attendings 28/80, residents 16/80 | Brodeur 2024 (b25, c02) | [E] (K16), preprint, partly public cases |
| Tuned PaLM 2 (AMIE) | 302 cases, 20 clinicians. Top-10 59.1%, top-1 29.2% vs unaided clinicians 33.6% / 15.9%. With search 44.5% top-10, with AMIE 51.8% | McDuff 2023, 2025 (b26, c08) | [E] (K16) |
| Pooled generative-AI diagnosis | 83 studies; pooled accuracy 52.1% (CI 47.0-57.1). Versus non-experts 0.6% difference (p=0.93); versus experts 15.8% worse (p=0.007); most at high risk of bias | Takita 2025 (a26) | [E] |
| Clinician-style prompts, GPT-3.5 | MedQA free response: CoT 46%, zero-shot 31%, intuitive 48%, analytic 40% (p=0.001), differential 38% (p<0.001), Bayesian 42% (p=0.02) | Savage 2024 (a22, b20, c01) | [S] (K14) |
| Clinician-style prompts, GPT-4 | about 497-498 usable: CoT 76%, intuitive 77%, analytic 78%, differential 78%, Bayesian 72% (p=0.07). NEJM: CoT 38% vs differential 34% (p=0.09, CI -11.4 to +2.1) | Savage 2024 (a23, a24) | [S] (K14). The NEJM result was not in preprint v1 |
| Wrong rationales carry false logic | 100 rationales: 65% of wrong answers vs 18% of right had false-logic statements (0.82 vs 0.11 per rationale) | Savage 2024 (b21) | [S] (K15) |
| Bias cues cut accuracy | BiasMedQA, 1,273 questions. GPT-4 72.7% unbiased, average drop -5.1; GPT-3.5 49.7%, -17.8; mixtral 51.8%, -7.7. By bias, averaged: false consensus -24.9, frequency -18.2, recency -12.9, confirmation -8.1. GPT-4 false consensus -14.0, confirmation -0.2. Mitigation recovers part: GPT-4 frequency 0.627 to 0.720 with education | Schmidgall 2024 (b23, b24, c04, d21) | [E] (K19). The preprint's "37.4% drop" for GPT-3.5 is unreliable |
| Role scaffold on o3 | 304 NEJM cases. Physicians 20% at $2,963. GPT-4o 49.3% at $2,745. o3 78.6% at $7,850. MAI-DxO on o3 79.9% at $2,397; no budget 81.9%; ensemble 85.5% at $7,184 | Nori 2025 (c03) | [S] (K17) vendor, no replication |
| Physicians given an LLM | US RCT: 50 physicians, 76% vs 74%, +2 (CI -4 to 8, P=.60); LLM alone +16 over conventional (CI 2-30, P=.03). UK: 22 physicians, 74.3% vs 65.7% (p=.001); LLM alone 21.3 above physician plus LLM; only 30% of questions put to the LLM | Goh 2024 (a25, b22, c06); Healy 2026 (c07) | [C] (K18) |
| Automation bias after AI training | 44 physicians, 264 cases; composite 73.3% vs 84.9% (-14.0, CI -18.9 to -9.1); top choice 76.1% vs 90.5% | Qazi 2026 (b31) | [S] |
| Prevalence cues swing sensitivity | 500 ED chest-pain cases. Baseline sensitivity 79.3%, specificity 45.2%. Prevalence cues: specificity 83.0%, sensitivity 30.4%. No category constraint: 94.7% / 8.8% | Safranek 2026 (b27) | [S] (K20) |
| Numeric vs semantic medical knowledge | 24,542 QAs. Semantic: Claude 3 Opus 68.7%, GPT-4 68.4%. Numeric: 63.7%, 56.7%. Six experts on 100 numeric questions 82.3% vs Claude 64.3%, GPT-4 55.8% | Avnat 2025 (d12) | [S] (K20, K31), 2024 models |
| LLM-written illness scripts | GPT-4, 184 diseases, 3 raters: 103 sufficient (56.0%), 52 partly lacking (28.3%), 29 deficient (15.8%). Cardiovascular 6/14 deficient, psychiatric 5/11, dermatology 0/13, respiratory 0/11, GI 1/25. No frequency or sensitivity fields | Yanagita 2024 (b19, c18, d11) | [S] (K21) |
| LLM SCT, small | 20 items, 43 experts. GPT-3.5 8/20 (15% majority agreement), GPT-4 15.6/20, GPT-5 15.2/20 (45%), GPT-4o 13.6/20 | Lilamand 2026 (a29, b30, c12) | [E] (K13) direction only; 20 items is noisy |
| LLM SCT, large | 750 items, 10 LLMs vs 1,070 students, 193 residents, 300 attendings. o3 67.8% (+-1.2), GPT-4o 63.9%, o1-preview 58.2%, R1 55.5%, Gemini 2.5 Pro 52.1%. Matched students, below senior residents and attendings; reasoning models over-use extreme ratings | c11 (NEJM AI 2025), abstract | [E] (K13) |
| SCT in a niche area | 16-item palliative-care SCT; LLM mean 0.43 vs students 0.47 (p=0.55); best 0.57 | c13 | [S] |
| ER belief updating | 25,174 notes; 194 SCT cases, 787 items. Best final-diagnosis ICD-10 exact match 39.91%. Thinking versions not better (GPT-5.2 DxUpdate p=0.455; Claude 4.5 Thinking worse on trajectory, p<0.001). DxUpdate 0.54-0.69 zero-shot, 0.69-0.81 with oracle rationales | ER-Reason (d16) | [S] (K30) preprint |
| Contrast-organised knowledge base | 1,050 cases, 24 systems, 9 LLMs. Qwen3.8-27B: none 63.0, random 64.0, BM25 67.0, contrastive 72.0, full wiki 75.5. Removing wiki: -9.0 to -14.5; removing evidence witness -3.5 to -9.0. Gains 12.0-51.1 over plain LLM | Feng 2026 (d13) | [P] (K25) |
| Exemplar base plus illness graphs | 5,383 paired cases, 49 diseases, 17 LLMs. Frontier bias trap rates above 50% (Gemini-2.5-Pro 60.90%, GPT-5 51.87%). ECR-Agent on Qwen3-32B: accuracy 40.25 to 55.49 (causal module) to 69.49 (plus exemplars and graphs); trap rate 43.46 to 38.32 to 33.75 | MedEinst (d14) | [P] (K26) |
| Verified retrieval helps little | 217 pairs, 371 pathologies. Claude Sonnet 4.6 trap rate 25.8% to 20.3%, robust accuracy 60.8 to 65.0; GPT-4o 39.9% to 35.9%. Base accuracy overstates robust accuracy by 16-28 points | MamaBench (d15) | [P] |
| Anchoring and early commitment | OncoRounds: 32 models, 20 cases; of 323 wrong or partial first diagnoses 65.6% stayed wrong; of 307 correct 50.8% got worse; differential reasoning 43.6% vs diagnosis 66.6%; rubric R=0.56 with accuracy. MINT: 1,035 cases, 11 LLMs; over 55% committed in first two turns; deferring the diagnostic question raised first-commit accuracy by up to 62.6%; wrong-to-right revisions up to 10.6 times right-to-wrong | Braitsch 2026 (d17); Fang 2026 (d23) | [E] (K24) / [P] (K29) |
| Hard cases are where models drop | 183 Medscape cases; easy above 81%, complex 43% | Noever 2024 (d24) | [S] |
| Several proposers explain most of the multi-agent gain | GPT-4o challenging cases top-1: single 14.50%, 4x1 mixture 23.98%, full 4x2 DMoA 25.34%; rebuttal about 1-1.5 points; token budget 16,000 to 4,000 cut rare-disease top-1 35.20% to 30.98% | Xia 2026 (d19) | [C] (K28) |
| Counterfactual challenger | 3 datasets, 7 LLMs. Llama-3.1-8B average 39.0% (+13.2 over zero-shot CoT); few-shot CoT 14.0% below zero-shot CoT 16.7% for DeepSeek on ER-Reason | You 2026 (d18) | [S] (K27, K28) |
| Leakage inflates knowledge-augmented systems | Over 60,000 cases. Cross-dataset Recall@1 54.3% to 40.3% (Hedges g=0.94); supervised classifier 42.9% to 16.7% (d=2.01) | Yang 2026 (d25) | [S] (K33) |
| Multi-agent not reliably better than a strong single LLM | MedQA best 89.90% by single-LLM CoT-SC; self-consistency the most costly single-LLM option | MedAgentBoard (d22) | [S] |
| Real records: worse, and order matters | 2,400 MIMIC-IV patients, four abdominal diseases; doctors beat models by 16-25 points; self-directed gathering 45.5% vs 58.8% full info (Llama 2 Chat); order changed accuracy up to 18.0% | Hager 2024 (c05) | [S], older open models |
| Oncology note errors | GPT-4 reasoning errors in 23.1% of note interpretations; GPT-5.1 cut but did not remove them | c24, abstract | [S] |

## 4. Mechanisms and models

All of this is plain data plus code-side rules (G5), so an engineer can build it.

### 4.1 The illness script as a data record

```
Script {
  label            # short name, the "encapsulation" (e.g. "acute pyelonephritis")
  enabling[]       # who/when/where/risk: age band, sex, setting, exposures, comorbidity, time course
  prevalence_band  # coarse prior per setting (rare / uncommon / common)   <- our addition; LLMs lack it (K31)
  fault            # ONE line: the mechanism, why the features arise
  features[]       # each: finding, direction (expected / expected-absent), strength (evoking weight), one-line why
  consequences[]   # course, complications
  mimics[]         # neighbour classes, each with the SINGLE separating finding (contrast pairs; K25, K06)
  actions          # management class (a16, a20)
  exemplars[]      # ids of 2-5 worked cases, including atypical ones (d07, K05)
  source           # where the entry was verified (K21)
}
```

What the evidence says for each field:

- `enabling`: established (K07). Teaching enabling conditions raised script richness about 20% (a17).
- `fault` as one line plus a `why` per feature: established as a help for delayed use and hard cases (K03; 89% vs 78%, a13).
- `mimics` with the separating finding: preliminary for LLMs (d13: contrastive 72.0 vs BM25 67.0 vs none 63.0); single-source for humans (b11, 46% vs 30%).
- `prevalence_band`: no direct test; motivated by Safranek (b27) and Avnat (d12).
- `actions`: single-source (a16 with 15/11/8 completers; a20 qualitative).
- `exemplars`: established for humans (K05), untested for LLMs (K26).
- `source`: needed because 15.8% of GPT-4-written scripts are deficient (b19).

### 4.2 Activation, fit and instantiation (Lubarsky 2015, a05)

A runnable version of the script loop:

1. **Activate.** From the first cues (enabling conditions first, then salient findings), retrieve candidate scripts. Enabling conditions prune whole classes early (b04, a07). Retrieval can be by embedding, keyword or by the model naming classes. Keep the list long: breadth is cheap (AMIE top-10 59.1% vs top-1 29.2%, c08).
2. **Gauge fit.** For each candidate, compare found features with expected features. Count expected-present, expected-absent, unexpected-present. Do the counting in code.
3. **Instantiate.** Fill the script's slots with the case values. Missing slots become questions or tests.
4. **Switch.** If best fit is poor (no candidate above a threshold, or two close), leave recognition and go to analytic work: mechanism reasoning (b05, a14) or discrimination between the top mimics (S7 discriminating test).

A script predicts what should be there, so an absent expected feature is itself a signal (a04). Rule for S4 TEST: test the top classes' expected-but-absent features.

### 4.3 Exemplar retrieval

Store solved cases with a feature vector. Retrieve the nearest by similarity (a08). Use both routes: class features (analytic) and nearest case (similarity). Ark found the pair additive in novices (56/53% vs 42/41%, b10). Risk: retrieval can anchor, and an early hypothesis rereads later findings (d07, d08). A fixed few-shot set is unstable (K27); choose exemplars by retrieval.

### 4.4 Contrast-organised library (d13)

Build pairs or small groups of confusable diseases. Each carries the finding that separates them, checked against source text. Ablation order: no knowledge 63.0, random pages 64.0, BM25 67.0, contrastive pages 72.0, full wiki 75.5. It matches the human result that mixed practice across categories beat blocked practice (b11).

### 4.5 The intermediate effect as a mode switch

The human data say detail level is a switchable mode, not a ceiling (d03, d05). Expert recall gains appear only when elaboration is forced. Keep two modes. Compressed: label plus a few key features. Elaborated: list every finding and comment on each. Use elaborated mode when script fit is weak. Do not score the agent on volume of recall (a10, b01).

### 4.6 SCT scoring as a probe

Each item: case, hypothesis, new datum, answer in {-2,-1,0,+1,+2}. Score an answer by the share of the expert panel that gave it, divided by the modal share. About 100 items and 10+ panellists (b15). For an agent, use it to test whether `features[].direction` and `strength` shift belief the way experts do. It is not a measure of final accuracy: ER-Reason does not report how SCT scores predict final accuracy (d16).

### 4.7 INTERNIST-style and information-gain loops

- INTERNIST-1: score from evoking strength and frequency, penalty for expected-but-absent; leaders choose questions (c26, record seen only).
- Chain of Diagnosis (c22): abstract the symptoms, retrieve candidate diseases, analyse, output a confidence distribution; the entropy drop picks the next question. Fine-tuned on 48,020 synthetic cases from encyclopedias covering 9,604 diseases. Scores not read.
- DR.KNOWS (c23): retrieve UMLS paths up to 2 hops from note concepts, rank them, feed them to a text model. Scores not read.
- Counterfactual editing (d18): edit a finding and watch how confidence in each diagnosis moves; this tests whether a finding is doing the work.

Common design: class library, distribution over classes normalised in code, next test by expected information. This is the shape of S2 plus S3-S4.

## 5. What holds up

### 5.1 Well supported

- **Enabling conditions matter** (K07, four sources: a07, b04, a17, d10). Small samples, consistent direction. Warning: richer script text did not predict exam score (r=-0.006).
- **Mechanism knowledge is kept and useful** (K03, four sources). Woods 89% vs 78%; Kulasegaram N=94, F(3,88)=3.05; Rikers 2005; de Bruin 2005. The effect is delayed: immediate scores were equal in all four Kulasegaram groups.
- **Exemplar similarity is a real part of diagnosis** (K05). Beyond Ark's 12-per-cell groups, effect sizes are lacking.
- **LLMs recall the right class and rank it poorly** (K16). 64% in differential vs 39% top (a21); 59.1% top-10 vs 29.2% top-1 (c08); differential reasoning 43.6% vs diagnosis 66.6% (d17).
- **Bias cues hurt LLMs** (K19, three sources). Prompt mitigation recovers only part.
- **Early commitment and anchoring** (K24, three sources: 65.6% stayed wrong; MedEinst; over 55% in two turns).
- **The SCT works as a test**, and LLM SCT scores rise with model generation (K12, K13).

### 5.2 Contested

- **Intermediate effect** (K02). For: Schmidt and Boshuizen 1993, Rikers 2000, Eberhard 2009. Against: van de Wiel 1998 by the same group; time limits remove it; forced elaboration reverses it (Wimmers 2005). Our reading: a style of processing. It is a caution about what to measure, not an agent rule.
- **Benefit of giving physicians an LLM** (K18). US +2 (p=.60, n=50) vs UK +8.6 (p=.001, n=22, within-subject, 4 vignettes). The UK study replicates "LLM alone beats physician plus LLM" and does not replicate "no benefit" (critique item 5).
- **Role scaffolds and challengers** (K28). MAI-DxO and the bias multi-agent study report gains. DMoA says most gain is from several proposers (rebuttal +1-1.5). MedEinst debate agents had trap rates of 40.34% and 41.69%. MedAgentBoard finds no consistent multi-agent advantage. No study matches tokens against self-consistency. G9 (no debate) stands.
- **Biomedical knowledge: packed away or active?** Both are supported (Rikers 2005, Woods; versus encapsulation). The real question is when it is used.
- **Prototype scripts vs exemplars vs causal models.** Ark's additive effect suggests they are not exclusive.

### 5.3 Failed or null

- **Reasoning-style prompts for GPT-4** (K14): no benefit; they hurt GPT-3.5 (analytic -6, differential -8.9). Human parallel: Sibbald 2013, three experiments, no effect of dual-processing instruction on the probability of the correct diagnosis. Consistent with SCHEMA 4b.
- **Reasoning models on belief updating** (K30): thinking versions not better; one worse (d16).
- **Teaching bias recognition** reduces errors little in humans (a18). Prompt-level mitigation recovers part for LLMs (GPT-4 75.2% few-shot, still below the no-bias level, b24).
- **Verified retrieval alone** (d15): trap rate down only 4.0-5.5 points; about 1 in 5 pairs still fail.

### 5.4 Moderators

| Moderator | Effect |
|---|---|
| Delay | Causal knowledge matters after a week, not at first test (b03, b07, b09) |
| Speed instruction | Causal learners better when fast, worse when thorough (b08) [S] |
| Study time | The intermediate effect vanishes with restricted time (d02, d03) |
| Forced elaboration | Expert recall advantage appears (d05) |
| Case difficulty | LLM accuracy 81% easy vs 43% complex (d24); Savage's NEJM result shows no gain |
| Case typicality | Experts err on typical cases as often as novices (d07); LLM-written cases are textbook-typical (b28) |
| Specialty | LLM-written scripts worst for cardiovascular (6/14) and psychiatric (5/11) (d11) |
| Model generation | LLM SCT 8/20 to 15.6/20 (a29); stronger models more anchored on counterfactuals (d14) |
| Leakage | Strict isolation cut Recall@1 from 54.3% to 40.3% (d25) |
| Expert rationale present | Expert text on why a finding shifts the differential raised accuracy for all 8 models (d16) |

### 5.5 Interventions (humans)

- Worked: case-based teaching of enabling conditions (a17); script format over symptom list (b17); explicit causal links (b09); mixed practice (b11); combined feature and similarity instruction (b10); guided reflection (b13, 5 studies); chatbot script feedback (c19, OR 3.2).
- Did not work: dual-processing instruction (d09); teaching bias recognition (a18); placing basic science next to clinical facts without links (b09); telling experts they will be graded (b01).

## 6. Language models

### 6.1 Baseline on diagnosis from case text

- GPT-4 (2023): 64% in differential, 39% top-1 on 70 NEJM cases (a21). o1-preview: 78.3% in differential, 52% top (b25). AMIE: top-10 59.1% vs 33.6% for unaided clinicians (c08). MAI-DxO base model o3: 78.6% on 304 stepwise cases (c03). On 70 shared cases GPT-4 to o1: 72.9% to 88.6% (p=.015).
- Pooled over 83 mostly biased studies the figure is 52.1%, equal to non-experts and 15.8% below experts (a26). The two pictures differ by case difficulty, model generation and scoring. Do not average them.
- On real records performance is lower: Llama 2 era models 45.5-54.9% when self-directing, doctors 16-25 points ahead (c05); best ICD-10 exact match 39.91% on ER notes (d16); 43% on complex Medscape cases (d24).

### 6.2 Does the model already hold scripts?

Indirect evidence: it holds class names and typical features but holds numbers weakly.

- It lists the right disease in the differential for most hard cases but ranks it poorly (K16).
- Written scripts are 56% sufficient, 15.8% deficient, and omit frequency and sensitivity (K21). Numeric knowledge lags semantic: 56.7-63.7% vs 68.4-68.7%; doctors 82.3% (K20, 2024 models).
- Base-rate behaviour is unstable. Without prevalence cues GPT-4o had sensitivity 79.3%, specificity 45.2%; with cues 30.4% / 83.0% (b27). One model, one complaint.
- Textbook-typical bias: model-written SCT cases are caricatured (b28); difficulty fit is the weakest criterion (71.25% and 76.25%, b32).

### 6.3 Script-style reasoning prompts

Telling a model to reason like a clinician does not raise accuracy for strong models (K14). Intuitive (recognition-first) prompting did no harm. Analytic, differential and Bayesian prompts were nominally worse for GPT-4 and clearly worse for GPT-3.5. Savage tested 2023 models only. No one reran it on current reasoning models. Thinking versions did not help belief updating (d16).

### 6.4 Stored knowledge in context

- A contrast-organised, source-checked wiki beat none, random pages and BM25 (63.0 to 75.5 on Qwen3.8-27B) but was not compared with equal-token CoT (K25).
- Course documents in the prompt moved SCT answers toward the student group (rho 0.64 vs 0.41, c15). Context-held class text shifts script-style judgement.
- Verified retrieval cut trap rate only 4.0-5.5 points (d15).
- An exemplar base plus illness graphs raised Qwen3-32B accuracy from 55.49 to 69.49 (d14). Exemplars and graphs were not separated.
- Fixed few-shot examples are unstable (d18).

### 6.5 Failure modes shaped like script failures

- **Anchoring and premature closure.** 65.6% of wrong first diagnoses stayed wrong; of correct first diagnoses 50.8% got worse over rounds (d17). More than 55% of answers committed in two turns; salient lab results lure early answers. Deferring the diagnostic question raised first-commit accuracy by up to 62.6%. Wrong-to-right revisions ran up to 10.6 times right-to-wrong (d23).
- **Einstellung.** Frontier models lock onto the common diagnosis and miss the one flipping finding. Trap rates above 50% (Gemini-2.5-Pro 60.90%, GPT-5 51.87%); stronger models more anchored (d14).
- **Bias cues in the input.** False consensus -24.9 average; GPT-4 -14.0 (b23).
- **Order and volume.** Order of information changed accuracy up to 18.0 points; more information lowered accuracy in older models (c05).
- **Dual conditions.** Help is weakest where two classes combine (dual infection, c28).
- **Extreme ratings** on SCT by reasoning models (c11).
- **Rationale quality.** Wrong answers carry false logic 65% of the time vs 18% (b21); trace quality tracks accuracy only R=0.56 (d17). Agrees with G10.

### 6.6 Multi-step scaffolds

- MAI-DxO: o3 78.6% to 79.9% and cost $7,850 to $2,397 (c03). The o3 accuracy gain was not significant; the cost cut was. Gains were larger for weaker models. Manual inspection: plain o3 anchored on first impressions; the challenger and hypothesis tracker led it to disconfirming evidence. Vendor study; tuned on GPT-4.1 and a validation set; the gatekeeper is a language model that can invent results.
- Bias multi-agent studies (c25, d20): first diagnosis 0/80 correct by design; final 51-61/80 (64-76%) in one, 57/80 (71.3%) in the other. No single-agent control, so the devil's-advocate effect is not isolated.
- DMoA (d19): most gain from 4 proposers; rebuttal 1-1.5 points; token budget matters.
- Counterfactual editing (d18): gains largest for small models and hard cases.
- Independent benchmark (d22): no consistent multi-agent advantage on text QA.

### 6.7 Evaluation caution

Base accuracy overstates robust accuracy by 16-28 points (d15). Leakage cut Recall@1 from 54.3% to 40.3% (d25). For o1-preview, NEJM cases before and after the training cutoff scored 79.8% vs 73.5% (p=0.59, c02): memorisation is not the whole story, but not ruled out. Medical benchmarks mix recall and reasoning (a28), so a class-library test needs cases that are not in the library.

## 7. What our agent should take

Schema parts: G guardrail, S state, O operator, M memory (SCHEMA section 5).

### Add now (established)

| # | Item | Part | Status | Evidence |
|---|---|---|---|---|
| A1 | **Class library as memory, one entry per class, in script form.** Fields: label, enabling conditions, one-line fault, features with direction and strength, consequences, mimics with the separating finding. Not long causal chains. | M, S2 | [E] for the structure (K01, K07, K03); script format over flat list [S] (K10) | a01, a05, a07, b04, a17, b17 |
| A2 | **Read context (enabling conditions) first in S2 and write them into the case representation before listing hypotheses.** Use them to prune classes. | S2 | [E] (K07) | a07, b04, a17, d10 |
| A3 | **One-line causal reason per key feature.** Cheap; helps recall after delay and with odd terms. State the link explicitly; placing mechanism text beside facts is not enough. | M, S2 | [E] (K03) | a13, b07, b09, a14 |
| A4 | **Keep a mechanism fallback.** When script fit is poor, drop to mechanism-based reasoning. | S6, O6 | [E] (K03) | a11, a14, b05, c27 |
| A5 | **Do not let the model write the library unchecked.** About 15.8% of GPT-4-written scripts were deficient and frequency and sensitivity were missing. Verify against a source; fill numeric fields from a checked table. | M | [S] (K21), supported by [S] numeric weakness (K20); action is cheap and safe | b19, d11, d12 |
| A6 | **Keep breadth, rank in code.** Let the model list many candidate classes, then rank and normalise in code. The model's weak point is ranking. | S3, G5 | [E] (K16) | a21, c08, d17 |
| A7 | **Treat bias-bearing sentences in the case as untrusted input.** Move stated guesses and "most doctors think it is X" into a marked block in S1; rescore the leading class with that sentence removed. A warning line in the prompt is not enough. | S1, G | harm [E] (K19); remedy [S] (S1 already lists it) | b23, b24, c04, d21 |
| A8 | **Keep the no-style-ritual rule (G1, 4b).** Do not add "reason like a clinician" or "be analytic" prompts. | G1 | [E] in direction; Savage used 2023 models (K14 is [S]) | a22-a24, d09, d16 |
| A9 | **Judge the library on held-out cases, not on recall volume or script richness.** | eval | [E] caution (K02, d10) | a10, b01, d10 |
| A10 | **Isolate evaluation from the library.** Cases must not be in the library or in sources the model has likely seen. | eval | [S] (K33); standard practice | d25, d15 |

### Test first

| # | Item | Part | Status | Evidence |
|---|---|---|---|---|
| T1 | **Stored class library vs the same tokens of free CoT on held-out NEJM-style cases.** The central gap. | M, S2 | [P] (K25) | d13, d14 |
| T2 | **Exemplar retrieval vs script vs both.** | M | [O?] (K26); human [E] (K05), one lab | b10, d01, d14 |
| T3 | **Contrast-pair organisation (mimic with separating finding) vs plain per-disease entries.** | M, S2 | [P]; human [S] (K06) | d13, b11 |
| T4 | **Graded prevalence prior per class and setting, supplied by the scaffold.** | S2, G | [S] (K20, K31) | b27, d12 |
| T5 | **Hold step: list hypotheses first, withhold the commit until the case is complete.** | S3, G | [P] (K29) | d23, d17 |
| T6 | **Expert "why this finding shifts the differential" text per feature.** | M | [S] (K30) | d16 |
| T7 | **Code-triggered single check on the leading class vs plain voting at equal tokens.** Not debate. | S4-S6 | [C] (K28); G9 | d19, c03, d20 |
| T8 | **SCT-style updating as a calibration probe.** | eval | [E] as a human tool (K12); as predictor of agent accuracy open | c11, d16 |
| T9 | **Rationale audit as a reliability signal.** | S9, G10 | [S] (K15) | b21 |
| T10 | **Action-based classes (management) in the library.** | M | [S] (K08) | a16, a20 |
| T11 | **Contrastive (interleaved) order of few-shot examples.** | M | [S] (K06) | b11 |
| T12 | **Forced elaboration vs list-then-rank on weak-fit cases.** | S2 | [O?] (K32) | d05, d17, d14 |

## 8. Concrete tests on our bench

All arms use equal total tokens per item, with library setup cost counted (G7). Run at least 3 seeds. Report paired differences with bootstrap intervals. Items must not be in the library or in the examples shown. Split every result by easy and hard (Noever: 81% vs 43%) and by typical and atypical.

| Test | Item type | Arms (equal tokens) | Metric | Expected effect |
|---|---|---|---|---|
| T1 Library vs free CoT | Held-out case vignettes with known final diagnosis (NEJM-style, 150+ items) plus 50 atypical items | (a) plain, short CoT; (b) plain, long CoT spending the library's tokens; (c) plain plus verified class library retrieved by code; (d) library plus CoT | Top-1 and top-5 in differential; paired (c) minus (b) | +3 to +8 points top-1 if Feng carries over (Feng's own ablation is 9-14.5, bundled with a review module). Zero is possible |
| T2 Exemplar vs script | Same items; library holds class entries and solved cases | nothing; script only; exemplar only (retrieved by similarity); both | Top-1, top-5; accuracy on atypical items | Human: both > either (56% vs 42%). Guess for LLM: both >= script > exemplar on typical, exemplar better on atypical |
| T3 Contrast pairs | Counterfactual pairs (one finding flips the diagnosis, as in MedEinst and MamaBench) | per-disease entries; entries plus mimic with separating finding; random pages; BM25 | Robust accuracy (both items of a pair right); trap rate | Trap rate down 3-8 points; contrast beats BM25 by about 5 (Feng 72.0 vs 67.0) |
| T4 Prevalence prior | Cases with a rare dangerous diagnosis among common ones; vary setting | no prior; binary base-rate cue (Safranek style); graded band stored per class | Sensitivity and specificity for the rare class; balanced accuracy | Graded band keeps sensitivity above 60% with specificity above 60%; binary cue shows the swing |
| T5 Hold step | Multi-turn or sharded cases (MINT style) | answer at once; hypotheses first then answer at end; code-held commit | Accuracy at first commit; wrong-to-right vs right-to-wrong revisions | Better first-commit accuracy; size unknown (MINT's 62.6% was for deferring the question) |
| T6 Why-notes | SCT-style update items and final diagnosis | library without why-text; with expert one-line shift rationale | SCT agreement with panel; final accuracy | +0.1 to +0.15 on update score (ER-Reason oracle rationales); smaller on final accuracy |
| T7 Check vs voting | Items with a bias-cue sentence | k samples plus plurality vote; one proposer plus code-triggered check on the leading class; debate (control for G9) | Accuracy under cue; fraction of unbiased accuracy recovered | Voting matches or beats the check; check gain under 2 points |
| T8 SCT probe | 100 SCT-style items, panel of 10+ | agent with library; plain | SCT score; item-level correlation with diagnosis accuracy on the same disease | SCT score below MCQ score; correlation unknown |
| T9 Rationale audit | Items with rationales | accept; code audit that each stated finding is in the case and linked to the class; self-consistency | AUROC of the audit flag for wrong answers | AUROC above 0.7 if 65% vs 18% holds |
| T10 Action classes | Management-choice items | disease-only library; plus management class | Management accuracy | Small gain |
| T11 Example order | Few-shot items | blocked by class; interleaved contrastive | Accuracy | Small; human 46% vs 30% |
| T12 Elaboration | Weak-fit or distractor-heavy cases | list-then-rank; forced comment on each finding | Rank of the correct class; error type | Elaboration worse on easy items, better on weak-fit items |

Run these checks on every test: a leak check (is the item text in the library), a typicality split, length-normalised grading, and seed-to-seed spread so a small effect is not read as a result.

## 9. What does not transfer, and why

- **The intermediate effect.** It is about human memory limits and recall style. An LLM does not forget case text in context. It could matter only as a mode (elaborate vs compress). Contested even in humans (K02).
- **Encapsulation as learning.** Humans pack causal chains into labels over years. We cannot train. A library entry is hand-built or built by code from a source. What transfers is the product (label plus one-line why), not the process.
- **Teaching results.** Script-format teaching (b17), chatbot feedback (c19) and case courses (a17) tell us about student learning. They guide what goes in an entry, not whether the model uses it.
- **Speed-accuracy crossover** (b08). Human time pressure. An LLM has token budget instead, which must be tested directly.
- **Practice schedules** (Hatala 46% vs 30%). Transfer to few-shot order is plausible but separate.
- **SCT expert panels.** Need 10-20 humans (b15). LLM panels give correlated voters (c14, G4). Use them to draft items only.
- **Human-AI hand-off results** (Goh, Healy, Qazi). Relevant only if the agent's output goes to a person.
- **Image tasks** (dermatology, ECG: a08, b10, b11, d07). Our items are text.
- **Nursing extension** (a20). Qualitative, other profession.
- **Exam-style gains** (R1 93% on 100 MedQA cases, a27). Clean text, likely seen in training. Not recognition from messy records.

## 10. Open questions

1. Does a stored script library beat the same tokens of free CoT on held-out cases? Closest: Feng, which compares only with no knowledge and BM25, bundled with a review module.
2. Does a retrieved solved case help an LLM more than a script? Is the pair additive (Ark 56% vs 42%)? Untested.
3. Why did clinician-style prompts not help GPT-4, and does it hold for current reasoning models and for hard cases?
4. Does verified retrieval fix LLM-written scripts, and which fields (cardiology, psychiatry) fail most? Only MamaBench tested verified retrieval (4.0-5.5 points).
5. Do enabling conditions and prevalence bands shift LLM ranking in a balanced way? Safranek's swing (79.3% to 30.4%) stands alone.
6. Is there an LLM analogue of the intermediate effect (more findings listed, worse differential when forced to elaborate)? No direct test.
7. What are the sample sizes and effect sizes behind Schmidt and Boshuizen 1993, Custers 1996 and Brooks 1991? Abstract only.
8. Does SCT-style updating predict real diagnostic accuracy for an agent? ER-Reason does not report it; Keemink found richness unrelated to exam score in humans.
9. Does a challenger recover accuracy lost to bias cues at equal tokens, or is the gain just extra samples? DMoA leans to the second.
10. Is the MAI-DxO result independent of model and benchmark when someone else runs it?
11. Do the human results generalise beyond three groups (Maastricht, McMaster, Montreal)?
12. Does the order in which cues are given (context first, then findings) change LLM accuracy? Hager found order effects up to 18.0 points on older models.

## 11. Sources

[V] opened: the page or PDF was read this session. [M] snippet or record seen only. For human studies of 1987-2009, [V] means the Europe PMC or PubMed abstract page; full texts were not read (critique, weak spots). Evidence lines b01-b05 and b07 came from the first agent's reading of review summaries; the critique says Woods 2007 and Takita 2025 were not re-opened.

### Human studies and reviews

- [M] Schmidt, Norman, Boshuizen (1990) A cognitive perspective on medical expertise. https://europepmc.org/article/MED/2261032
- [V] Schmidt and Rikers (2007) How expertise develops in medicine. https://pubmed.ncbi.nlm.nih.gov/18004989/ (a02 abstract only; b01-b05 are review summaries)
- [V] Schmidt and Mamede (2020) How cognitive psychology changed the face of medical education research. https://pmc.ncbi.nlm.nih.gov/articles/PMC7704490/
- [M] Charlin, Boshuizen, Custers, Feltovich (2007) Scripts and clinical reasoning. https://europepmc.org/article/MED/18045370
- [V] Lubarsky, Dory, Audetat, Custers, Charlin (2015) Using script theory to cultivate illness script formation. https://pmc.ncbi.nlm.nih.gov/articles/PMC4795084/
- [M] Charlin, Brailovsky, Leduc, Blouin (2000) The Script Concordance test. https://europepmc.org/article/MED/11273368
- [M] Hobus, Schmidt, Boshuizen, Patel (1987) Contextual factors in the activation of first diagnostic hypotheses. https://europepmc.org/article/MED/3696019
- [M] Brooks, Norman, Allen (1991) Role of specific similarity. https://europepmc.org/article/MED/1836491
- [V] Norman, Young, Brooks (2007) Non-analytical models of clinical reasoning. https://europepmc.org/article/MED/18004990
- [V] Norman and Brooks (1997) The non-analytical basis of clinical reasoning. https://europepmc.org/article/MED/12386407
- [V] Rikers, Schmidt, Boshuizen (2000) Knowledge encapsulation and the intermediate effect. https://europepmc.org/article/MED/10753544
- [M] Rikers et al. (2005) Role of biomedical knowledge: lexical decision. https://europepmc.org/article/MED/16186615
- [M] de Bruin, Schmidt, Rikers (2005) Basic science and clinical knowledge in diagnostic reasoning. https://europepmc.org/article/MED/16043534
- [M] Woods, Brooks, Norman (2007) It all makes sense. https://pubmed.ncbi.nlm.nih.gov/17318360/
- [M] Woods, Brooks, Norman (2007) Role of biomedical knowledge in difficult cases. https://europepmc.org/article/MED/17206465
- [M] Woods, Howey, Brooks, Norman (2006) Speed kills? https://pubmed.ncbi.nlm.nih.gov/16987187/
- [M] Kulasegaram et al. (2015) Cause and Effect. https://pubmed.ncbi.nlm.nih.gov/26505104/
- [V] Ark, Brooks, Eva (2006) Giving learners the best of both worlds. https://europepmc.org/article/MED/16565197
- [M] Hatala, Brooks, Norman (2003) Practice makes perfect. https://pubmed.ncbi.nlm.nih.gov/12652166/
- [M] Coderre, Mandin, Harasym, Fick (2003) Diagnostic reasoning strategies and diagnostic success. https://pubmed.ncbi.nlm.nih.gov/12895249/
- [V] Devantier, Minda, Goldszmidt, Haddad (2009) Categorizing patients in a forced-choice triad task. https://pmc.ncbi.nlm.nih.gov/articles/PMC2690657/
- [V] Keemink, Custers, van Dijk, ten Cate (2018) Illness script development in pre-clinical education. https://pmc.ncbi.nlm.nih.gov/articles/PMC5834830/
- [M] Norman et al. (2017) The causes of errors in clinical reasoning. https://europepmc.org/article/MED/27782919
- [V] Yazdani and Hoseini Abardeh (2019) Five decades of research and theorization on clinical reasoning. https://pmc.ncbi.nlm.nih.gov/articles/PMC6717718/
- [M] Illness scripts in nursing (2022) J Adv Nurs. https://europepmc.org/article/MED/34378221
- [V] Schmidt and Boshuizen (1993) Origin of intermediate effects in clinical case recall. https://europepmc.org/article/MED/8316096
- [V] van de Wiel, Schmidt, Boshuizen (1998) A failure to reproduce the intermediate effect. https://europepmc.org/article/MED/9736850
- [V] Wimmers et al. (2005) Inducing expertise effects in clinical case recall. https://europepmc.org/article/MED/16150036
- [V] Eberhard et al. (2009) The intermediate effect in dental medicine. https://europepmc.org/article/MED/19630930
- [V] Sibbald et al. (2013) Cardiac examination and dual-processing instruction. https://europepmc.org/article/MED/22717993
- [M] Lambe et al. (2016) Dual-process cognitive interventions. https://pubmed.ncbi.nlm.nih.gov/26873253/
- [M] Lubarsky et al. (2011) Script concordance testing: validity review. https://pubmed.ncbi.nlm.nih.gov/21401680/
- [M] Dory et al. (2012) How to construct and implement SCTs. https://pubmed.ncbi.nlm.nih.gov/22626047/
- [M] Custers (2015) Thirty years of illness scripts. https://pubmed.ncbi.nlm.nih.gov/25180878/
- [V] Moghadami et al. (2021) Teaching clinical reasoning with illness scripts. https://pmc.ncbi.nlm.nih.gov/articles/PMC7856771/
- [M] Valente et al. (2026) Tell me what you know. https://pubmed.ncbi.nlm.nih.gov/42750475/
- [M] Miller, Pople, Myers (1982) INTERNIST-1. https://pubmed.ncbi.nlm.nih.gov/7048091/
- [M] Clinical reasoning and AI: can AI really think? (2024). https://pmc.ncbi.nlm.nih.gov/articles/PMC11316886/
- [M] Qazi et al. (2026) Automation bias after AI training. https://pubmed.ncbi.nlm.nih.gov/42932681/
- [M] Human-AI collaboration in clinical reasoning: UK replication (2026). https://pubmed.ncbi.nlm.nih.gov/42053372/

### LLM and AI studies

- [V] Kanjee, Crowe, Rodman (2023) Accuracy of a generative AI model in a complex diagnostic challenge. https://pmc.ncbi.nlm.nih.gov/articles/PMC10273128/
- [V] Savage et al. (2024) Diagnostic reasoning prompts. https://pmc.ncbi.nlm.nih.gov/articles/PMC10808088/ ; https://arxiv.org/abs/2308.06834
- [V] Goh et al. (2024) LLM influence on diagnostic reasoning: RCT. https://pmc.ncbi.nlm.nih.gov/articles/PMC11519755/
- [V] Takita et al. (2025) Meta-analysis of generative AI diagnostic performance. https://pmc.ncbi.nlm.nih.gov/articles/PMC11929846/
- [V] Moell et al. (2025) Medical reasoning in LLMs: DeepSeek R1. https://pmc.ncbi.nlm.nih.gov/articles/PMC12213874/
- [V] Sim and Chen (2025) Critique of impure reason. https://pmc.ncbi.nlm.nih.gov/articles/PMC12563542/
- [M] Lilamand et al. (2026) Geriatric SCT and ChatGPT versions. https://pubmed.ncbi.nlm.nih.gov/41114883/
- [M] Hudon et al. (2024) ChatGPT in psychiatry to design SCTs. https://pubmed.ncbi.nlm.nih.gov/38596832/ ; [V] full text https://pmc.ncbi.nlm.nih.gov/articles/PMC11007379/
- [M] Yapici Coskun et al. (2025) LLM SCT in obstetrics and gynecology. https://pubmed.ncbi.nlm.nih.gov/40305090/
- [V] Yanagita et al. (2024) Expert assessment of ChatGPT illness scripts. https://pmc.ncbi.nlm.nih.gov/articles/PMC11095028/
- [V] Schmidgall et al. (2024) Cognitive biases in medical language models. https://pmc.ncbi.nlm.nih.gov/articles/PMC11494053/ ; https://arxiv.org/abs/2402.08113
- [V] Brodeur et al. (2024) Superhuman performance of a large language model. https://arxiv.org/abs/2412.10849
- [V] McDuff et al. (2023, 2025) Towards accurate differential diagnosis. https://arxiv.org/abs/2312.00164 ; https://pmc.ncbi.nlm.nih.gov/articles/PMC12158753/
- [V] Safranek et al. (2026) Stepwise diagnostic reasoning with real-world prevalence. https://pmc.ncbi.nlm.nih.gov/articles/PMC13037032/
- [M] Sallam and Abouzeid (2025) AI members of an SCT panel. https://pubmed.ncbi.nlm.nih.gov/40056088/
- [V] Nori et al. (2025) Sequential Diagnosis with Language Models. https://arxiv.org/abs/2506.22405
- [V] Hager et al. (2024) Limitations of LLMs in clinical decision-making. https://pmc.ncbi.nlm.nih.gov/articles/PMC11405275/
- [M] Cabral et al. (2024) Clinical reasoning of a generative AI model (R-IDEA). https://pubmed.ncbi.nlm.nih.gov/38557971/
- [M] Strong et al. (2023) Chatbot vs medical student. https://pubmed.ncbi.nlm.nih.gov/37459090/
- [M] Script concordance benchmark (NEJM AI 2025). https://pubmed.ncbi.nlm.nih.gov/42932606/
- [M] LLMs in palliative care SCT (2025). https://pubmed.ncbi.nlm.nih.gov/40929006/
- [V] AI-generated SCTs, mixed methods (2025). https://pmc.ncbi.nlm.nih.gov/articles/PMC12634011/
- [M] Copilot chatbot for illness script competency (2026). https://pubmed.ncbi.nlm.nih.gov/41843425/
- [M] AI teaches surgical diagnostic reasoning (2025). https://pubmed.ncbi.nlm.nih.gov/40768987/
- [V] Test-retest reliability of LLMs in rubric scoring of problem representations (2026). https://pmc.ncbi.nlm.nih.gov/articles/PMC13686340/
- [V] Chen et al. (2024) Chain of Diagnosis. https://arxiv.org/abs/2407.13301
- [V] Gao et al. (2023) DR.KNOWS. https://arxiv.org/abs/2308.14321
- [M] Structured reasoning failures in oncology notes (npj Digit Med 2026). https://pubmed.ncbi.nlm.nih.gov/42380231/
- [V] Mitigating cognitive biases through multi-agent conversations (2024). https://pmc.ncbi.nlm.nih.gov/articles/PMC11615553/ ; Duke-NUS version https://arxiv.org/abs/2401.14589
- [M] Nephrology fellows with GPT-4o (2026). https://pubmed.ncbi.nlm.nih.gov/41888321/
- [V] Avnat et al. (2025) Numerical vs semantic medical knowledge (EBMQA). https://arxiv.org/abs/2406.03855
- [V] Feng et al. (2026) MedEVM. https://arxiv.org/abs/2609.35627
- [V] Chen et al. (2026) MedEinst. https://arxiv.org/abs/2601.06636
- [V] Adewuyi et al. (2026) MamaBench. https://arxiv.org/abs/2607.14385
- [V] ER-Reason (2025/2026). https://arxiv.org/abs/2505.22919
- [V] Braitsch et al. (2026) OncoRounds. https://arxiv.org/abs/2607.10275
- [V] You et al. (2026) Counterfactual multi-agent reasoning. https://arxiv.org/abs/2603.27820
- [V] Xia et al. (2026) DMoA. https://arxiv.org/abs/2609.05069
- [V] Zhu et al. (2025) MedAgentBoard. https://arxiv.org/abs/2505.12371
- [V] Fang et al. (2026) MINT. https://arxiv.org/abs/2604.04325
- [V] Noever (2024) Pocket professional. https://arxiv.org/abs/2410.20636
- [V] Yang et al. (2026) Auditing leakage in rare disease diagnosis. https://arxiv.org/abs/2610.33592

## Source audit (2026-11-01)

Fresh auditors re-opened the sources of 5 established claims: 3 confirmed as written, 2 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **E01.03-K07** (reworded: the sources support less). Keemink et al. 2018 (32 students) found a case-based clinical reasoning course raised overall illness-script richness by almost 20%, with relatively more Enabling Conditions and less Fault content; it did not teach enabling conditions specifically. Schmidt and Rikers 2007 abstract says nothing on enabling conditions or first hypotheses; the expert-first-hypothesis point appears only as background citation. Corrected claim: Illness scripts are thought to shift with expertise from Fault (pathophysiology) toward Enabling Conditions (patient features, setting) and Consequences, which are available early and help activate scripts (background in Keemink et al. 2018). A case-based clinical reasoning course raised pre-clinical students' overall script richness by almost 20% (14.47 vs 12.14, n=32) while shifting content toward Enabling Conditions; experts' use of them for first hypotheses was not tested there.
- **E01.03-K19** (reworded: the sources support less). LLM part is supported by one paper only (Schmidgall et al., npj Digit Med/arXiv, listed as b23/b24/c04/d21; the other sources are different multi-agent studies). 'Physician automation bias persists after AI training (-14 points)' appears in none of the opened sources; the only 14.0 is GPT-4's worst false-consensus drop. GPT-4 few-shot mitigation (75.2%) actually exceeded the 72.7% unbiased average, though the authors call gains modest. Corrected claim: In BiasMedQA (1,273 USMLE questions, 7 injected biases, 6 LLMs; Schmidgall et al. 2024), GPT-4 scored 72.7% unbiased and lost about 5% on average with a bias cue (worst case -14.0% for false consensus); prompt-level mitigation (education, one-shot, few-shot) gave only modest, uneven gains per bias and generally did not match unbiased accuracy. (Single-paper evidence; the physician automation-bias claim is unsupported and should be dropped.)
- **E01.03-K01** (now single-source: only one opened source, code check).
- **E01.03-K03** (now single-source: only one opened source, code check).
- **E01.03-K12** (now single-source: only one opened source, code check).
- **E01.03-K13** (now single-source: only one opened source, code check).
