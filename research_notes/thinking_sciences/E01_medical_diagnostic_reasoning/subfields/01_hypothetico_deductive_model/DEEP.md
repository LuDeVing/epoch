# Hypothetico-deductive model: deep document

*Subfield E01.01. Built from evidence_a-d.jsonl (a01-a39, b01-b25, c01-c25, d01-d16), claims.jsonl (K01-K24) and critique.md in this folder. Evidence ids in brackets refer to those files. The founding book (Elstein, Shulman, Sprafka 1978) was never opened, so every founding number below is secondhand or absent. Where a number is not known, the text says so.*

## 1. What it is

The hypothetico-deductive model says a clinician solves a hard diagnostic case like a scientist. The clinician forms a few hypotheses very early, from the first cues. Each hypothesis predicts findings that should be present. The clinician then collects data to test those predictions, revises, and settles on one diagnosis [a01].

Four steps are usually named:
1. Cue acquisition (history, first look).
2. Hypothesis generation (a short list, early).
3. Cue interpretation (does each finding confirm, disconfirm or not matter for each hypothesis).
4. Hypothesis evaluation (keep, drop, add, then decide).

Elstein, Shulman and Sprafka (1978, *Medical Problem Solving*) proposed it from think-aloud and simulated-patient studies at Michigan State. Elstein and Schwarz restate it in 2002 as "a few hypotheses early, used to guide data collection" [a01].

What happened next matters more than the model itself. Within about ten years the field concluded that the model describes how doctors reason but does not explain who reasons well. Good and poor diagnosticians both use it. The difference is the content of the hypotheses and the knowledge behind them [a03, a21, d02, d07]. This is called content specificity. The task note for this subfield says the same: experts did not generate more hypotheses, only better ones.

Why it matters for our agent. The model maps to S3 (generate candidates) and S4 (test them). It also maps to the MAI-DxO design in the LLM literature (ranked differential, test chooser, challenger). The human evidence says: do not expect the loop shape alone to add accuracy. The LLM evidence says: a loop helps when it fixes specific failures (anchoring, uninformative tests, premature closure). The gain is largest for weaker models and in cost, not in accuracy for the strongest ones.

## 2. History and theories in depth

### 2.1 Founding era (1970s)

- Elstein, Shulman, Sprafka (1978). Think-aloud and simulated-patient work. Core claims: hypotheses appear within the first minutes, there are few of them, they steer the search for data. Exact counts (hypotheses per case, minutes to first hypothesis, accuracy by group) were not verified from the primary source [d05 abstract only; critique section 3].
- Feightner, Barrows, Neufeld, Norman (1977), McMaster. Early description of family-physician problem solving that led to a process model [d04, abstract only, no figures].
- Barrows et al. (1978) studied process too. Kaufman and Patel (1988) summarise both: these studies did not separate students from expert physicians except in the accuracy of the diagnostic hypotheses [a21].
- Sprafka (1973) dissertation, Michigan State. Reported only through a search summary: 30 fourth-year students were told to generate many or few hypotheses, early or late. The instruction had no effect on outcome. Low-accuracy subjects produced more varied inaccurate hypotheses [a23, d08]. Primary text blocked. Single-source, secondhand [K17].
- Kassirer and Gorry (1978) found diagnoses are most often made during history taking. Patel and Groen (1986) found accurate experts reasoned forward and misdiagnosing experts reasoned backward, posting a cause and then collecting confirming evidence [a22, secondhand].
- Style (1979), a general-practice essay: GPs form hypotheses in the first few minutes and redefine them many times. No data. It shows how fast the model spread into primary-care teaching [a24].

### 2.2 Replication and the turn to content (1981-1991)

- Neufeld, Norman, Feightner, Barrows (1981). Students from three classes plus 22 followed yearly from preclerkship to first postgraduate year, against a doctor criterion group. Most reasoning process variables did not relate to educational level. The only process variable tied to both level and outcome was the "hypothesis aggregate score", a measure of hypothesis content. The process stays constant from school entry to practice; only content quality changes [d02, abstract only].
- Barrows, Norman, Neufeld, Feightner (1982). 18 family physicians and 19 general internists, randomly selected, 62 encounters, 4 simulated problems. Physicians consistently formed multiple hypotheses early and used them to guide inquiry rather than routine full data collection. Little variation across problems. Accuracy and promptness of hypothesis generation were linked to the accuracy of the final formulation [d03, abstract only]. This is the clearest descriptive replication of the founding claim.
- Joseph and Patel (1990). Endocrinologists (high knowledge) and cardiologists (low knowledge) on an endocrine case. Both generated accurate early hypotheses. The high-knowledge group used more relations between cues, generated accurate hypotheses early and spent the rest confirming. The low-knowledge group could not discriminate and eliminate alternatives. Generation did not separate the groups; evaluation did [b17, a14; abstract and secondhand].
- Arocha and Patel (1991), McGill. 13 subjects (4 each of year 2, 3, 4 students, plus 1 cardiology resident), two cardiology cases in three segments, 90-minute think-aloud. First-segment hypothesis counts: year 2 mean 1.5, year 3 mean 3, year 4 mean 3.4, resident 5. All subjects produced the initially suggested hypothesis. Only 5 of 13 reached the correct diagnosis (two year-2, two year-4, the resident; no year-3). Share of cues used as confirming: year 2 71%, years 3 and 4 88%, resident 92%. All year-2 students kept the first hypothesis despite contradicting data. More forward reasoning went with higher accuracy [a08-a13]. This is the one study that counts more hypotheses at higher training (see section 5, contested).
- Kaufman and Patel (1988). 15 volunteers (5 endocrinologists, 5 residents, 5 students), one 15-minute simulated history. Experts got 72% of the 16 relevant findings, residents 60%, students 45% (F(2,12)=4.46, p<.05). Of all findings elicited, 50% were relevant for experts, 33% residents, 31% students. Positive findings per exchange: 18.6, 12.2, 10.6 (F(2,12)=7.28, p<.01). Experts asked the fewest questions (multivariate F(2,12)=4.64, p<.05). 4 of 5 experts named both parts of the diagnosis; no student did [a16-a20].
- Groen and Patel (1985) challenged the model: it seemed to present hypothetico-deductive reasoning as psychologically real rather than as an intellectual tool [a08].

### 2.3 Competing accounts (1990s-2010s)

- Knowledge-structure theories (scripts, schemas, exemplars). Norman (2005): over 30 years little evidence that reasoning is characterised by general process variables; expertise is many coordinated representations and many solved examples [b16].
- Pattern recognition for easy cases. Experienced doctors probably use hypothetico-deductive reasoning only for difficult cases; easy cases are pattern recognition or direct retrieval (Schmidt, Norman, Boshuizen 1990; Brooks, Norman, Allen 1991, via a04). Coderre et al. (2003): in think-aloud gastroenterology, pure hypothetico-deductive reasoning had lower odds of success than pattern recognition or scheme-inductive reasoning. Exact odds ratios not read [b11].
- Dual-process and bias research. Norman et al. (2017): errors arise from both fast and slow thinking; bias-awareness teaching does not cut errors; knowledge reorganisation gives small but consistent gains [b15]. Croskerry (2013) argues for debiasing by decoupling from the intuitive answer, but gives no effect sizes [b23].
- Education. Problem-based learning was built to teach hypothesis formulation and testing early. Case specificity then showed the limits of teaching a general strategy, and the rationale moved to building functional organisation of content [a07, d06, d07].
- Elstein (2009) restates the history: criticisms led to more emphasis on clinical experience and prior knowledge [d05, abstract only].

### 2.4 Early AI: the model as a program

INTERNIST-I (Pople, Miller, Myers; 1982, chapter in Clancey and Shortliffe 1984) is a hypothetico-deductive loop in code. Findings evoke diseases. Diseases are scored from evoking strength, frequency and import. One of three question modes is chosen by how close the top rivals are: pursue if the runner-up trails by 46-89 points; rule out if 5 or more diagnoses are within 45 points; discriminate if 2-4 are within 45 points. Questions go in small groups and escalate from history to exam to lab [c01]. On 19 NEJM cases (43 major diagnoses): correct definitive diagnoses INTERNIST-I 17, MGH clinicians 23, discussants 29. Failed to diagnose 18, 15, 8. Total errors 29, 28, 21. Only 19 of 42 screened cases qualified because the knowledge base lacked the others. The authors name tunnel vision: it works one problem area at a time [c02, c03].

### 2.5 LLM era (2023-2026)

The loop returns as a design for language models: ranked differential, test chooser, challenger (MAI-DxO), hypothesis agent plus decision agent (LA-CDM), knowledge graph plus information-gain question choice (MedKGI), MCTS with hypothesis backtracking (ClinicalAgents). Section 6 covers them.

## 3. Core findings with exact numbers

Status key: established = 2 or more independent sources and no real contradiction; single-source; contested = sources disagree or design is weak. Ids point to the evidence files. K numbers point to claims.jsonl.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Clinicians form a few hypotheses early and use them to guide search | 37 physicians, 62 encounters, 4 simulated problems; early multiple hypotheses; promptness and accuracy of hypotheses tied to final accuracy. 1978 counts not seen | Barrows 1982 [d03]; Elstein and Schwarz 2002 [a01]; d04, d06 | Established (K01), descriptive; exact 1978 numbers unverified |
| Process is constant across training; only hypothesis content tracks level | 22 students followed from preclerkship to first postgraduate year; most process variables unrelated to level; "hypothesis aggregate score" related to level and outcome | Neufeld 1981 [d02]; Elstein and Schwarz [a03]; Kaufman and Patel [a21]; d07 | Established (K02) |
| High- and low-knowledge doctors both generate accurate early hypotheses; evaluation differs | No significant difference in cue selection; high-knowledge group used more cue relations and spent the rest confirming | Joseph and Patel 1990 [b17, a14] | Established (K18), abstract plus secondhand |
| Experts gain from efficiency, not volume of questions | Relevant findings obtained: 72 / 60 / 45% (experts / residents / students; F(2,12)=4.46, p<.05). Share of elicited findings relevant: 50 / 33 / 31%. Positive findings per exchange 18.6 / 12.2 / 10.6 (p<.01). N=15, one case | Kaufman and Patel 1988 [a17-a20] | Single-source (K03); uncorrected exploratory tests |
| Number of early hypotheses rose with training in one small study | Year 2 1.5, year 3 3, year 4 3.4, resident 5. 4 per student group, 1 resident, 2 cases | Arocha and Patel 1991 [a10] | Contested (K04) |
| Students mostly confirm; anchoring | Cues used as confirming: 71% (year 2), 88% (years 3, 4), 92% (resident). All year-2 students kept the first hypothesis despite contradicting data | Arocha and Patel 1991 [a12]; Nori [b03]; AgentClinic [c10] | Established (K05) for humans; LLM anchoring shown anecdotally |
| Instruction to generate many or few hypotheses, early or late, did nothing | N=30 fourth-year students | Sprafka 1973, search summary only [a23, d08] | Single-source, secondhand (K17) |
| Forward reasoning goes with accuracy; backward with load and failure | Forward inferences concluded the correct diagnosis for 4 subjects (case 2); literature review in same paper | Arocha and Patel [a13]; Patel and Groen via a22 | Single-source (K19) |
| Telling clinicians to slow down does not help | Speed 44.5% (n=96) vs reflect 45.0% (n=108); 69 s vs 89 s per case; wrong cases took 17 s longer | Norman 2014 [b14] | Established (K08) with b15, b19 |
| Free second look rarely changes diagnoses | 47 residents, 16 cases; 8% of diagnoses revised; score 1.20 to 1.22 of 2 (t=2.15, p=0.03) | Monteiro 2015 [b19] | Established (K08) |
| Analysing the initial impression helped, even experts | Nephrologists 31.1% to 65.6%, residents 40.0% to 70.0% (p<0.001); N=9 and 6; no control that saw the extra data without priming; abstract has p=0.07 beside an OR whose CI excludes 1 | Bass 2013 [b10, d01] | Contested (K09) |
| Checklist at verification corrected expert ECG errors | Errors corrected 0.29 vs 0.03 per ECG; net errors 0.39 vs 1.04 per ECG; 15 experts, 18 ECGs | Sibbald 2013 [b18, abstract] | Contested (K09) |
| Pure hypothetico-deductive coding went with lower success than pattern recognition | Odds ratios not read; strategy coded after the fact | Coderre 2003 [b11, abstract] | Contested (K10) |
| INTERNIST-I (loop in code) close to clinicians, below discussants | 17 vs 23 vs 29 correct of 43; 19 cases chosen to fit the knowledge base | Pople et al. [c02] | Single-source |
| Prompting a differential does not beat plain CoT | GPT-4: CoT 76, DDx 78 (+2.2, CI -1.4 to 5.8, P=0.24), Bayesian 72 (-3.4, P=0.07). GPT-3.5: CoT 46, DDx 38 (-8, P<0.001), analytic 40, Bayesian 42. Test N 518 (497 for GPT-4) | Savage 2023/2024 [a25-a27, b05, b06, c08] (one study) | Single-source (K07) |
| LLM lists the diagnosis in top 10 more often than unassisted clinicians | 59.1% vs 33.6% (p=0.04); assisted clinicians 51.7% (LLM) vs 44.4% (search) vs 36.1% (none). 302 NEJM cases, 20 clinicians | McDuff 2023 [a36, b07, c05] | Established as list-recall result (K15) |
| GPT-4 differential on NEJM cases | In list 45/70 (64%), first 27/70 (39%), mean list length 9.0, quality 4.2 | Kanjee 2023 [c04] | Not re-verified (critique) |
| o1-preview on NEJM cases | In differential 78.3% (CI 70.7-84.8), first 52%, 143 cases; 88.6% vs 72.9% GPT-4 on 70 shared cases (p=.015); right next test 87.5% of 132; R-IDEA 78/80 vs GPT-4 47/80, attendings 28/80, residents 16/80. Before vs after cutoff 79.8 vs 73.5 (p=0.59) | Brodeur 2024 [a33-a35, b21, c06] | Established as capability; controls partly historical |
| Giving physicians GPT-4 did not raise reasoning score | 76% vs 74%, adjusted diff 2 (CI -4 to 8, P=.60); 50 physicians; time 519 vs 565 s; LLM alone 92% (+16, CI 2 to 30) | Goh 2024 [b09, c07] | Established (K15) |
| Multi-role orchestrator raised accuracy and cut cost | o3 78.6% at $7,850; MAI-DxO 81.9% at $4,735; budgeted 79.9% at $2,396; ensemble 85.5% at $7,184; physicians 19.9% at $2,963; about +11 points average across models; N=304 | Nori 2025 [a29-a32, b01-b04, c19] | Single-source (K06) |
| No MAI-DxO role has been ablated | Only ablation: single vs batched questioning, both 83.9% ($3,991 vs $5,084), 56 test cases | Nori [d09, d10] | Established that the gap exists (K22) |
| Random test choice beats prompted ReAct and hypothesis-driven LA-CDM on MIMIC-CDM | Random 84.8 (85.4 +- 1.3), ReAct 74.9, LA-CDM 81.3, LDTL 93.4, SFT-all 94.2 (Llama-3-8B backbone) | Shen 2026 [c14]; Bani-Harouni [c13] | Established that there is no clear win (K11); setup dependent |
| Random question choice fails in another pipeline | MedKGI Qwen3-8B: full 69.81%, random 31.13%, degree-based 47.17%, no KG 44.34% (-25.5) | Wang 2026 [d11] | Single-source (K20) |
| Expected-uncertainty-reduction test choice beat LLM-chosen tests | GPT-4o and mini, about 1,000 patients, 4 datasets; exact accuracies in figures not read | ACTMED [c22]; Sun 2024 [c21] | Single-source (K12) |
| Asking follow-ups hurts unless the model can abstain | -11.3% vs no questions; abstention + rationale + self-consistency +22.3% over interactive baseline, +12.1% over non-interactive; still 10.3% below full information | MediQ [c11] | Established (K13) with b20, d15 |
| Data gathering loses accuracy | Full information 0.93 falls to 0.65-0.75 after gathering (appendix, approximate); Gemini 2.5 Pro main text 35% final vs 69% full info; failures: inappropriate hypothesis generation 348, premature closure 291, inadequate investigation 90 | Chiu 2025 [d15] | Single-source for the counts (K23) |
| Sequential setting hurts open LLMs | MIMIC-CDM 2,400 cases; physicians beat LLMs by 16-25 points; clinicians 87.5% and 92.5%; Llama 2 Chat 45.5% sequential vs 58.8% full; order effects up to 18 points | Hager 2024 [b20, c12, b25] | Established (older models) |
| Reasoning models do well with all results, weak at choosing tests | DeepSeek-R1: 71.79% after one round, 76.18% free multi-turn, 89.76% with all results. Exam recall 43.61% (1-turn) vs 40.67% (free-turn) | MedR-Bench [a38, c16] | Single-source |
| Premature closure in frontier models | About 70% false action when the correct option is removed (55-82%); 81% premature closure on underspecified low-risk cases vs 19% urgent; safety prompt to about 48% | Handler 2026 [d14] | Established (K23) with d15 |
| Bias-cue prompts degrade accuracy | GPT-4 72.7% baseline, worst drop 14.0 (false consensus), confirmation 0.2; GPT-3.5 average drop 37.4; average over models: false consensus 24.9, frequency 18.2, recency 12.9, confirmation 8.1. AgentClinic GPT-4 52 to 48 (patient) and 50.3 (doctor) | Schmidgall [c09, c10, a39]; Kim 2026 [b22] | Established (K16) |
| Multi-agent debate rescued initially wrong diagnoses | 0/80 initial; 57/80 top (71.3%), 64/80 top two (80.0%); cases selected for failure; no equal-token control | Ke 2024 [a37, d13] | Single-source (K24) |
| Backtracking over hypotheses recovers some wrong starts | Backbone 0.4521; +orchestrator 0.4962; all 0.5107 (GPT-5.2); backtracking triggered in 83% of wrong initial hypotheses, correct diagnosis recovered in 64%; unsupported hypothesis pruned in 94% | ClinicalAgents [d12] | Single-source (K20) |
| Test-follow-up failure modes | 155 of 222 examined MedGemma cases erroneous; divergent belief updates after tests 15.2% to 4.6% after trajectory-consistency training on 32,681 trajectories | MedAction [c15] | Single-source (K14) |
| Candidate count peaks near 5 in one pipeline | MedKGI hyperparameter study, Qwen3-8B; figure not read | Wang 2026 [d11] | Single-source (K21) |

## 4. Mechanisms and models

### 4.1 Human model, as four operations

1. Cue acquisition. Read the first facts. In the data, all subjects picked the important cues (Arocha and Patel) [a11]. Cue selection is not where groups differ [b17].
2. Hypothesis generation. Cues evoke 1-5 candidates quickly. The first one is often right and the cue set usually suggests it [a10, b17]. Quality depends on stored knowledge (scripts, disease patterns), not on a generation procedure.
3. Cue interpretation. Each finding is marked as for, against or irrelevant to each candidate. Students mark most cues as confirming (71-92%) [a12]. Positive findings are overweighted and negative findings discounted [a06].
4. Evaluation. High-knowledge doctors spend the time here: confirm, discard, discriminate. Low-knowledge doctors cannot discriminate and eliminate [b17, a14].

Two reasoning directions: forward (finding to hypothesis, goes with accuracy) and backward (hypothesis to predicted findings, loads working memory, tied to failure in some studies) [a13, a22]. Elstein and Schwarz frame the testing step as "each hypothesis predicts findings that should be present" [a01]. Both directions are present in all subjects [a13].

### 4.2 INTERNIST-I as an implementable control rule [c01]

```
state: scored list of diseases (score from evoking strength, frequency, import of each finding)
loop:
  top = highest score; gap = top - runner_up
  if gap in the 46-89 band:        mode = PURSUE      (ask about the top one)
  elif 5+ diseases within 45 pts:  mode = RULE OUT    (cheap questions that exclude many)
  elif 2..4 diseases within 45:    mode = DISCRIMINATE (ask what separates those few)
  ask in small groups, history -> exam -> lab
```
The point for the agent: the question mode depends on how close the rivals are, and code can compute this. The weak point: it works one problem area at a time (tunnel vision) and has a hand-built knowledge base [c02].

### 4.3 MAI-DxO as an implementable orchestration [a30, d09]

One base model plays five roles in a debate chain. The chain ends in a question, a test or a diagnosis:
- Hypothesis: probability-ranked differential, top 3, Bayesian updates after each result.
- Test-Chooser: up to 3 tests that best split the leading hypotheses.
- Challenger: devil's advocate against anchoring.
- Stewardship: cost control (a budget tracker in the budgeted variant).
- Checklist: sanity check of the proposed action.

Variants: Instant Answer, Question Only, Budgeted, Unconstrained, Ensemble. These toggle questions, tests, budget tracking and ensembling. They do not remove roles. So the effect of roles is not isolated [d09]. Authors credit hypothesis tracking and the Challenger for cases where the scaffold sought disconfirming evidence and changed path, but this is manual inspection, no counts [a32, b03, d10]. Example: hand sanitizer ingestion. Plain o3 fixated on antibiotic toxicity, ordered brain MRI and EEG, wrong, $3,431. The scaffold asked about toxin exposure in round 1, correct, $795 [b03].

Observation that bears on design [b04]: weaker models showed a "false economy". They considered fewer differential diagnoses, so never ordered tests to confirm or exclude rivals. This is interpretation, not a controlled manipulation.

### 4.4 LA-CDM: separate hypothesis and decision agents [c13]

A hypothesis agent keeps the working diagnosis and a decision agent picks the next action. Training is SFT then RL. Hypothesis correctness rose 75.7 to 81.9%. Calibration error (ECE) went 0.069 to 0.037. Average test cost $1,295.61 vs ReAct $1,480.32. Picks ultrasound for cholecystitis in 64.9% and CT for appendicitis in 85.1%. Caveat: LA-CDM (81.3) is below a random planner (84.8) in the Shen replication [c14].

### 4.5 Information-gain test choice [c22, d11, c21]

ACTMED uses the LLM only to simulate possible test results, then picks the test with the largest expected drop in uncertainty (Bayesian experimental design). Implementable as:
```
for each candidate test t:
    sample k plausible results r from LLM given current hypotheses
    for each r: re-score hypotheses -> posterior P(h | r)
    EIG(t) = H(prior) - E_r[ H(posterior) ]
choose argmax EIG(t) / cost(t)
```
Code does the arithmetic (consistent with G5). MedKGI does something similar with a knowledge graph: information-gain node choice 69.81% vs random 31.13% vs degree-based 47.17% [d11]. Sun et al. replace free LLM questioning with an external guideline planner. GPT-4 Turbo success/accuracy/F1 went from 86/86/87 (no planner) to 100/82/80 (extracted procedure) and 100/91/91 with human feedback. Llama3-70B went from 0% successful dialogues to 100% with F1 83 [c21].

### 4.6 Backtracking over hypotheses [d12]

ClinicalAgents puts a Monte-Carlo-tree-style orchestrator over hypotheses. When the first hypothesis is wrong, backtracking triggers (83% of cases) and the right diagnosis is recovered in 64%. Unsupported hypotheses are pruned in 94% of cases. No baseline without backtracking is given for the 64%.

### 4.7 Abstain-or-ask gate [c11, d14]

MediQ: questions help only if the model can abstain from answering when information is too thin. Confidence-based abstention plus rationale plus self-consistency gave +22.3% over the interactive baseline. Handler: even so, premature closure is about 70% when information is missing, higher for routine-looking cases (81%) than urgent ones (19%). A safety prompt reduces it to about 48%.

### 4.8 Failure taxonomy useful as trace checks [c15, d15, a05]

- Human: failure to generate the correct hypothesis, misreading evidence (especially visual), misinterpreting evidence. In many hard cases the right answer is not in the initial set [a05].
- LLM: tests not tied to stated hypotheses; rigid or erratic belief updates; lost state [c15]. Inappropriate hypothesis generation 348 cases, premature closure 291, inadequate investigation 90 [d15].
- Each can be logged by code from the trace: is the requested test linked to a named hypothesis; did belief change after a result; did the final answer appear in the early list.

## 5. What holds up

### 5.1 Replicated

- Early multiple hypotheses guide inquiry (Elstein 1978; Barrows 1982 on 37 randomly selected physicians; McMaster 1977) [d03, d04, a01]. Descriptive replication, no effect sizes.
- Process is not what separates expert from novice; content is (Neufeld 1981; Kaufman and Patel 1988 summary; Joseph and Patel 1990; Norman 2005) [d02, a21, b17, b16].
- Anchoring and confirmation: students use most cues as confirming [a12]. Plain LLMs anchor on first impressions in manual case review [b03, c20]. Premature closure is common in frontier LLMs [d14, d15].
- "Slow down and be careful" does not help (44.5% vs 45.0%) and free reconsideration changes only 8% of diagnoses [b14, b19, b15].
- An LLM lists a right diagnosis in the top 10 more often than unassisted humans (McDuff 59.1 vs 33.6; Kanjee 64% in list; Brodeur 78.3%) [a36, c04, a33].
- Sequential data gathering hurts LLMs relative to full information (Hager, MedR-Bench, MediQ, Chiu) [b20, a38, c11, d15].

### 5.2 Failed, null or weak

- Founding claim as an explanation of expertise: dropped. Both successful and unsuccessful diagnosticians use it [a03].
- Instruction to generate many or few hypotheses had no effect on outcome (Sprafka 1973, N=30, secondhand) [a23, d08].
- Prompting an LLM to form a differential: no significant gain in GPT-4 (+2.2, P=0.24), a loss in GPT-3.5 (-8, P<0.001) [b05, b06].
- Giving physicians GPT-4: no gain in reasoning score (76 vs 74) although the LLM alone scored 92% [b09].
- Bias-awareness teaching does not cut errors (Norman 2017) [b15]. Bias-awareness prompts recover only part of the damage in LLMs [c09, b22].
- Prompted ReAct and hypothesis-driven LA-CDM lost to a random test planner on MIMIC-CDM [c14].

### 5.3 Contested

- Do experts generate more hypotheses? The review line says no. Arocha and Patel count 1.5, 3, 3.4, 5 by training [a10]. They count across cases, groups of 4 and one resident, without quality [critique section 2]. Joseph and Patel say generation does not separate groups [b17]. Left contested (K04).
- Hypothetico-deductive versus pattern recognition. Coderre says the pure form does worse [b11]. The coding was done after the fact and may follow case ease. Ark et al. (2007, 48 students, ECG): combining feature-by-feature analysis with trust in familiarity beat either alone, with no interaction with contrastive learning [b12, abstract]. Kulatunga-Moruzi et al. (2001, 12 preclinical students): similarity to past cases helped atypical cases [b13, abstract].
- Does analysing the first hypothesis help? Bass: 31.1% to 65.6% in nephrologists, no no-priming control [b10, d01]. Sibbald checklist: errors corrected 0.29 vs 0.03 [b18]. These gains can be explained by simply having more data or a second look. Monteiro (second look only) found a tiny gain [b19].
- Prompting vs orchestration. Savage: no gain from a differential prompt [b06]. Nori: gains from a multi-role loop with tests [b01]. Different task (static MedQA vs sequential), model, and cost control. No study isolates the role structure [critique section 2].
- Hypothesis-driven vs random tests. LA-CDM 81.3 beats ReAct 74.9 in c13, yet a random planner (84.8) beats both in c14 (Llama-3-8B backbone). MedKGI shows the reverse: random 31.1 vs information gain 69.8 [c13, c14, d11]. The result depends on setup (number of diseases, how informative a random test is).
- Contamination: Brodeur's 79.8 vs 73.5 (p=0.59) before vs after cutoff is non-significant, so it neither proves nor rules out leakage [a33]. McDuff: 51 of 302 cases (16.9%) had some training-text overlap [c05].

### 5.4 Moderators found

- Model strength: MAI-DxO gains are largest for weaker baselines (about +11 average) and small for o3 and o4-mini, where cost fell instead. Accuracy gain was significant for all models except o3 and o4-mini (one-sided paired permutation, 10,000 resamples, p<0.005) [b02].
- Case difficulty: easy cases are likely pattern recognition; the loop matters in hard cases [a04]. Handler: models close prematurely more on routine-looking cases [d14].
- Information regime: with all data given the loop adds little (Savage's tests were single-turn, all data given) [b05]. The loop's job is data gathering, which is where models lose most [d15, b20].
- Order and amount of information: pancreatitis diagnosis gained 21 points or more for some models given only radiologist reports; some orders cost about 4 points on diverticulitis [b25, c12].
- Expertise by strategy: Bass found residents did better with scheme-inductive (OR 5.69, CI 1.59-20.33), nephrologists had no strategy difference (OR 0.57, CI 0.23-1.39), interaction p=0.02 [b10].

### 5.5 Interventions that worked or did not

| Intervention | Result | Source |
|---|---|---|
| Speed vs reflect instruction | 44.5% vs 45.0%, none | [b14] |
| Free second look | 8% revised, +0.02 of 2 | [b19] |
| Analyse initial impression (human) | 31.1% to 65.6% / 40.0% to 70.0%, no control | [b10] |
| Checklist at verification (ECG experts) | 0.29 vs 0.03 errors corrected per ECG | [b18] |
| Differential-diagnosis prompt (GPT-4 / GPT-3.5) | +2.2 n.s. / -8 | [b06, b05] |
| MAI-DxO orchestrator | +3.3 (unconstrained) / +1.3 (budgeted, cost -69%) / +6.9 (ensemble) over bare o3; about +11 average across models | [b01, b02] |
| Abstain-or-ask gate (MediQ) | +22.3% over interactive baseline | [c11] |
| Safety prompt vs premature closure | 70% to 48% false action | [d14] |
| Expected-information-gain test choice | beat LLM-chosen tests | [c22, d11] |
| External guideline planner | Llama3-70B 0% to 100% dialogue success | [c21] |
| Trajectory-consistency training | divergent belief updates 15.2% to 4.6% | [c15] |
| Bias-correcting debate on pre-failed cases | 0/80 to 57/80, no control | [d13] |
| Debiasing text / few-shot on bias prompts | GPT-4 frequency 0.627 to 0.720; recency 0.679 to 0.742 (one-shot) | [c09] |

## 6. Language models

### 6.1 What models do without a scaffold

- Static vignettes, all data given. Models do well. GPT-4 CoT on free-response MedQA 76% (n=497). GPT-4 has the answer in its list on NEJM cases 64% (Kanjee, 70 cases). o1-preview 78.3% in differential and 52% first (143 cases) [a27, c04, a33]. o1-preview R-IDEA perfect in 78/80 against attendings 28/80. The "cannot-miss" share in a triage differential (median 0.92) was not significantly higher than GPT-4 or physicians [a35].
- Sequential vignettes, data must be gathered. Models lose a lot. MIMIC-CDM open LLMs are 16-25 points below physicians [c12]. MedR-Bench: 89.76% given all results vs 71.79% to 76.18% after gathering for DeepSeek-R1 [a38]. Chiu: about 0.93 with full information, 0.65-0.75 after the exam [d15]. MediQ: asking follow-ups lowered accuracy by 11.3% vs asking none [c11]. AgentClinic: GPT-4 52% with 20 interactions vs 25% with 10; MIMIC-IV variant Claude-3.5 42.9, GPT-4 34.0, GPT-4o 24.0, Llama 3 70B 8.5 [c10]. AMIE runs a three-step chain every turn (summary and differential, missing information and confidence, next question) and beat 20 PCPs on 28 of 32 specialist axes [c18].
- Typical failure points: tests not tied to hypotheses, erratic belief updates, lost state [c15]. Guideline tests skipped, format errors every 2-4 patients, hallucinated tools every 2-5 [c12]. Inappropriate hypothesis generation (348) and premature closure (291) [d15]. Confidence rises on maintained diagnoses whether or not correct [d15]. Implicit LLM test choice selects almost the same features for every patient [c22].
- Anchoring and bias. Plain o3 anchors on first impressions (manual inspection, no counts) [b03]. Bias cues pasted into vignettes lower accuracy, much more for weaker models (GPT-3.5 average drop 37.4), and about 14 points for GPT-4 on false consensus [c09]. Reasoning-enhanced variants are not reliably less vulnerable (1,273 vignettes; Gemini on four unpublished bias prompts fell from 80.0-88.6% to 47.4-86.1%) [b22]. Effects with agent role-play bias are small (about 2-4 points on GPT-4) [a39].

### 6.2 What changed accuracy and by how much

| Change | Effect | Cost note | Id |
|---|---|---|---|
| Differential-style prompt vs CoT, GPT-4 | +2.2 points, P=0.24 | prompt only | [b06] |
| Same, GPT-3.5 | -8 points, P<0.001 | prompt only | [b05] |
| MAI-DxO (o3) unconstrained | 78.6% to 81.9%; cost $7,850 to $4,735 | cost fell | [b01] |
| MAI-DxO budgeted | 79.9% at $2,396 (-69% vs o3) | cost fell | [b01, critique 1] |
| MAI-DxO ensemble | 85.5% at $7,184 | about the cost of bare o3 | [b01] |
| MAI-DxO across 6 model families | about +11 points average; small for o3, o4-mini | | [b02] |
| MAI-DxO vs generalist physicians | 79.9-85.5% vs 19.9% at $2,963 (physicians restricted) | | [a29, b01] |
| Single vs batched questioning inside MAI-DxO | 83.9% both; $3,991 vs $5,084 | | [d09] |
| LA-CDM (trained) vs prompted ReAct | 81.3 vs 74.9 | $1,295 vs $1,480 | [c13] |
| Random planner vs LA-CDM | 84.8 vs 81.3 | | [c14] |
| Learned planner (LDTL) | 93.4 | | [c14] |
| MedKGI: information gain vs random | 69.81 vs 31.13 | 9.11 vs 19.25 rounds | [d11] |
| MedKGI: remove knowledge graph | 69.81 to 44.34 (-25.5) | 13.44 rounds | [d11] |
| ClinicalAgents: backbone to full | 0.4521 to 0.5107 (+13.0%) | six-metric average | [d12] |
| MediQ abstention | +22.3% over interactive baseline | | [c11] |
| Safety prompt | 70% to 48% false action | | [d14] |
| Sun planner | Llama3-70B dialogues 0% to 100% | | [c21] |
| MedAction trajectory training | divergent updates 15.2% to 4.6%; cost -13% | | [c15] |
| Fine-tune on clinician reasoning traces | relative +29% accuracy, +41% reasoning recall (MedReason-8B +31% 10-shot) | | [c17] |

### 6.3 Reading these results honestly

- The most cited gain (Nori) is one company paper. It has a gatekeeper LLM that can invent test results and leak cues, physicians barred from search, hard curated cases, and no role ablation. At the cheap setting the accuracy gain over o3 is 1.3 points; most of the win is cost [a31, b01, c19].
- No study isolates "a hypothesis list before any data request" against plain CoT at equal tokens on sequential cases. Savage tests the prompt on static cases. Nori confounds it with roles and cost steering [critique GAPS 1].
- The loop's effect depends on the base model. For the strongest models, accuracy gain is small [b02].
- Several 2026 results (c13-c15, b22, d11, d12) are from a single group each, own system, small open models, and some tables were read from garbled PDF text [critique section 3].
- MAI-DxO's challenger and debate chain sits close to G9 (no debate). Nori shows gains at lower cost than bare o3, but the debate-vs-sampling comparison was not run. Treat the challenger as a hypothesis to test, not as support for debate [a30, d10].

## 7. What our agent should take

Schema parts: G guardrail, S state, O operator, memory. Status: [E] established, [S] single-source, [C] contested.

### Add now (established)

| # | Item | Part | Status | Evidence |
|---|---|---|---|---|
| A1 | Do not expect the loop shape to replace knowledge. Gains must come from retrieval of domain content and from fixing specific failures. Judge candidates by quality, not count. | S3, memory | [E] | K02, K18; a03, a21, b16, b17, d02 |
| A2 | Keep "slow down / be careful" and free self-reflection out (already in 4b). This subfield adds 44.5% vs 45.0% and 8% revised. | G (4b entry) | [E] | K08; b14, b19, b15 |
| A3 | Skip the hypothesis loop when a fast answer passes its check; run it for hard cases only. Consistent with G1/G12 and the S0 mode table. Human evidence is a pattern (easy cases use recognition). The LLM threshold is untested. | S0, G1, G12 | [E] for the principle (human); threshold to test | a04, b11 (K10 contested), d14 |
| A4 | Always include a random-test (or no-hypothesis) baseline when evaluating any hypothesis-driven test selector on our bench. | G7 | [E] | K11; c13, c14, d11 |
| A5 | In sequential tasks, give the agent an abstain-or-ask gate: ask only when a code-measured signal (sample agreement, a hint only per G4) says information is missing; never ask by default. Do not use verbal confidence. Note G6: abstention is allowed only for "ask for more data", never for "submit nothing". | S4, G6 | [E] | K13, K23; c11, d14, d15 |
| A6 | Log hypothesis-to-test links in the trace. Code flags tests with no linked hypothesis, belief changes that go against a result, and a final answer that never appeared in the early list. This is bookkeeping, not extra thinking. | S4, run log | [S] for failure modes (c15), cheap | K14; c15, d15 |
| A7 | Input hygiene for planted bias cues: move suggestive statements (a stated guess, "most doctors think...") out of the working context. Extends S1 input hygiene. | S1 | [E] that bias cues hurt; [S] that removal helps | K16; c09, b22, a39 |
| A8 | When the output is a candidate list, measure top-k recall of the list separately from final accuracy. | S3, run log | [E] | K15; a36, c04, a33 |

### Test first (not yet established; also in UNKNOWNS.md)

| # | Item | Part | Status | Evidence |
|---|---|---|---|---|
| T1 | Name 3-5 hypotheses before asking for any data, vs plain CoT, at equal tokens. | S3, S4 | [S] | K01, K06, K07; b01, b05, d15 |
| T2 | Explicit expected-information-gain test choice, code-computed, vs LLM-chosen tests at equal call count. | S4, G5 | [S] | K12; c22, d11, c21 |
| T3 | Challenger / disconfirmation step against anchoring, on or off, at equal tokens. Check against G9 first. | S4, S5, G | [S] | K06, K24, K22; b03, d13 |
| T4 | Number of hypotheses (1, 3, 5, 8). | S3 | [S] | K17, K21; a23, d11 |
| T5 | 2x2: scaffold on/off x retrieved knowledge on/off. | S3, memory | [S] | K20; d11, d12 |
| T6 | Structured final re-check (checklist) vs free re-check vs none, at equal tokens. | S8 | [C] | K09; b10, b18, b19 |
| T7 | Backtracking over hypotheses when the first fails a check. | S5, S6 | [S] | K20; d12 |
| T8 | Difficulty gate: fast path vs always-loop. | S0 | [C] | K10; b11, d14 |
| T9 | Forward (data to hypothesis) vs backward (hypothesis to predicted data) prompting. | S4 | [S] | K19; a13, a22 |
| T10 | Hypothesis-to-test link-check as a guard that blocks unlinked tests. | S4 | [S] | K14; c15 |

## 8. Concrete tests on our bench

Our bench is the HTSA harness (ARC and BrainTeaser items and other single-answer problems). This subfield's findings concern sequential evidence gathering, which the bench does not have as is. Two routes:
(a) Build a small sequential-evidence item type from items that can hide parts of the input (reveal facts on request: hidden test results, hidden examples, hidden constraints), with the facts held in code, not in a gatekeeper model.
(b) Run on public diagnosis sets with a simulated gatekeeper (SDBench-style, MedR-Bench, MediQ) as an external check. Use unpublished or rewritten cases to cut contamination [b22, a33].

All arms use the same base model, the same total token budget per item, and the same cap on data requests. Equal tokens includes the cost of setup and roles (G7). Report accuracy, cost, tokens and the number of data requests.

| Test | Item type | Arms (equal tokens) | Metric | Expected effect |
|---|---|---|---|---|
| T1 hypothesis-first | Sequential-evidence items, 200+ | A plain CoT, ask as you go; B must write 3-5 candidates, each with a predicted finding, before the first request; C same as B without the predictions | Final accuracy; top-k recall of the list; requests per item | Small: 0 to +3 points on strong models, more on weak. Prior: Savage +2.2 n.s. |
| T2 info-gain tests | Same | A model picks the next request; B code computes EIG from model-simulated outcomes and picks; C random request | Accuracy at equal request count; tokens | B above A and C. Prior: ACTMED and MedKGI positive, Shen shows random is strong. Always run C |
| T3 challenger | Items with a planted wrong first impression (unpublished) | A plain; B challenger step after each result must name one finding that would refute the lead; C one extra independent sample at equal tokens | Revision rate when contradicting evidence arrives; accuracy | B beats C only if the challenger does more than add sampling. G9 prior: most gain is sampling |
| T4 number of hypotheses | Held-out sequential set | 1, 3, 5, 8 candidates requested | Accuracy; tokens | Flat or peaked near 3-5 (MedKGI peak 5) |
| T5 2x2 | Domain items with a retrievable knowledge file | scaffold on/off x knowledge on/off | Accuracy; interaction term | Knowledge main effect larger than scaffold (MedKGI -25.5 for knowledge) |
| T6 re-check | Ambiguous items | none; free re-check; structured re-check (list each candidate, one confirming and one refuting finding from the trace) | Net corrected minus broken | Structured above free; free near 0 or negative |
| T7 backtracking | Items where the first hypothesis fails a code check | A revise in place (S5); B return to the stored candidate list | Recovery rate | B above A (ClinicalAgents 64% recovered, no baseline) |
| T8 difficulty gate | Mixed easy and hard | always-loop; direct; gate on sample agreement | Accuracy at equal total tokens | Gate cheaper at the same accuracy; check false skips |
| T9 direction | Items with predictive structure | forward prompt; backward prompt | Accuracy | Unknown; human data suggest forward |
| T10 link check | Same as T1 | with / without code guard that rejects requests not linked to a named hypothesis | Share of unlinked requests; accuracy | Fewer wasted requests |

Analysis rules. Pair items. Use McNemar for accuracy. Report 95% confidence intervals. With 100 items a 5 point effect is near the noise floor, so use at least 200 items for effects below 5 points. Fix thresholds before running (see UNKNOWNS.md).

## 9. What does not transfer, and why

- Human working-memory limits. Backward reasoning loads human working memory [a13]. A model has no such limit in the same form, so the forward/backward finding may not apply.
- Human expertise development. Neufeld's constant-process finding is about learners acquiring content over years. A model's knowledge is fixed at training. The lesson that carries over is only that content, not process, separates good from bad.
- The count of hypotheses in humans (1.5 to 5) reflects short-term memory and time. An LLM can list ten at once (GPT-4 mean list length 9.0, vs PCPs 5.39) [c04, c18]. For a model the question is whether a long list helps or hurts at equal tokens, not how many fit.
- Think-aloud methods report human reasoning. For LLMs, written reasoning is not evidence of the cause of the answer (G10). The "hypotheses" a model states may not drive its answer.
- Clinical stakes and costs. MAI-DxO costs are model-estimated prices. Test cost matters in medicine. Our items may have no cost axis, so the cost-saving half of MAI-DxO's result may not carry over.
- NEJM puzzle cases are published, hard, curated and possibly in training data. Results on them do not show real-encounter performance [a33, c05, c04].
- Human bias (anchoring, confirmation) arises during reasoning. Pasted bias cues in LLM tests are a sentence in the prompt, not a process [c09 limits].
- Gatekeeper LLMs. In SDBench-style tests the data source is a model that may invent or leak. Our hidden-fact items should use code-held facts.
- Debate. MAI-DxO's challenger is a form of multi-role debate. G9 says debate does not beat voting at matched cost. This subfield has no matched-cost test either way.
- The 1978 numbers (hypothesis counts, times) come from simulated patients and think-aloud with small groups. They are descriptive and unverified here.

## 10. Open questions

1. Exact numbers in Elstein, Shulman, Sprafka (1978): hypotheses per case, time to first hypothesis, accuracy by group. Not seen. Barrows (1978) and Neufeld (1981) full texts also not read.
2. Does forcing 3-5 named hypotheses before data requests beat plain CoT at equal tokens? No study isolates it.
3. Which MAI-DxO role carries the gain (hypothesis tracker, challenger, test chooser, cost steward, checklist)? Needs an ablation at matched cost. None found.
4. Optimal number of early hypotheses for an LLM. MedKGI peak at 5 in one 8B pipeline. Sprafka 1973 primary not reached.
5. Is the Bass 2013 gain real? Needs the full paper and a control that sees the extra data without priming.
6. Why does a random planner beat hypothesis-driven agents on MIMIC-CDM but not in MedKGI? Does it hold with current reasoning models and more diseases?
7. Knowledge versus loop structure in LLMs. MedKGI: knowledge graph removal -25.5, random questions -38.7. No clean 2x2.
8. Does an explicit disconfirmation step reduce anchoring at equal tokens on unpublished bias cases? Ke 2024 had no control.
9. Can an LLM detect case difficulty to skip the loop? Handler: models close more on routine-looking cases (81%) than on urgent ones (19%). Self-detection is unreliable.
10. Does verification of the final answer against the hypothesis list give a net gain for LLMs, or does it mostly flip correct answers? Monteiro: 8% revised in humans.
11. Are contamination effects real in NEJM-based results? Brodeur p=0.59 does not settle it.
12. Is the human "forward reasoning goes with accuracy" finding (a13, N=13) real, and does it matter for LLMs?
13. Do the gains of orchestration shrink as base models improve? Nori shows small accuracy gains for o3 and o4-mini [b02].

## 11. Sources

[V] = opened and read this session (full text, PDF text, or abstract page as noted in the evidence file). [M] = snippet or secondhand only.

Human studies and reviews
- [V] Elstein and Schwarz (2002), Clinical problem solving and diagnostic decision making. https://www.bumc.bu.edu/facdev-medicine/files/2010/06/CPS-BMJ.pdf (a01-a07)
- [V] Arocha and Patel (1991), Hypothesis generation and the coordination of theory and evidence. https://escholarship.org/uc/item/0rc9t79c (a08-a15)
- [V] Kaufman and Patel (1988), The nature of expertise in the clinical interview. https://escholarship.org/uc/item/9h70p5x6 (a16-a21; a22 is secondhand content)
- [M] Sprafka (1973) doctoral dissertation, Michigan State. https://d.lib.msu.edu/etd/41739/FULL_TEXT/view (a23, d08; access blocked)
- [V] Style (1979), Intuition and problem solving. https://bjgp.org/content/bjgp/29/199/71.full.pdf (a24)
- [V, abstract] Neufeld et al. (1981), Clinical problem-solving by medical students. https://pubmed.ncbi.nlm.nih.gov/6973686/ (d02)
- [V, abstract] Barrows et al. (1982), The clinical reasoning of randomly selected physicians. https://pubmed.ncbi.nlm.nih.gov/7116714/ (d03)
- [V, abstract] Feightner et al. (1977), Solving problems: how does the family physician. https://pubmed.ncbi.nlm.nih.gov/21304873/ (d04)
- [V, abstract] Elstein (2009), Thinking about diagnostic thinking: a 30-year perspective. https://pubmed.ncbi.nlm.nih.gov/19669916/ (d05)
- [V] Five decades of research and theorization on clinical reasoning (BMC Med Educ 2019). https://www.ebi.ac.uk/europepmc/webservices/rest/PMC6717718/fullTextXML (d06)
- [V] How cognitive psychology changed the face of medical education research (Adv Health Sci Educ 2020). https://www.ebi.ac.uk/europepmc/webservices/rest/PMC7704490/fullTextXML (d07)
- [M] Joseph and Patel (1990), Domain knowledge and hypothesis generation. https://pubmed.ncbi.nlm.nih.gov/2182962/ (b17; abstract plus a14)
- [M] Coderre et al. (2003), Diagnostic reasoning strategies and diagnostic success. https://pubmed.ncbi.nlm.nih.gov/12895249/ (b11)
- [M] Ark, Brooks, Eva (2007), The benefits of flexibility. https://pubmed.ncbi.nlm.nih.gov/17316213/ (b12)
- [M] Kulatunga-Moruzi et al. (2001), Coordination of analytic and similarity-based processing. https://pubmed.ncbi.nlm.nih.gov/11302031/ (b13)
- [V] Norman et al. (2014), Etiology of diagnostic errors (re-verified in critique). https://pubmed.ncbi.nlm.nih.gov/24362377/ (b14)
- [M] Norman et al. (2017), Causes of errors in clinical reasoning. https://pubmed.ncbi.nlm.nih.gov/27782919/ (b15)
- [M] Norman (2005), Research in clinical reasoning. https://pubmed.ncbi.nlm.nih.gov/15813765/ (b16)
- [V] Bass et al. (2013), Experienced physicians benefit from analyzing initial diagnostic hypotheses. https://pmc.ncbi.nlm.nih.gov/articles/PMC4563663/ and https://pubmed.ncbi.nlm.nih.gov/26451203/ (b10, d01; abstract only, not independently re-verified)
- [M] Sibbald, de Bruin, van Merrienboer (2013), Checklists improve experts' diagnostic decisions. https://pubmed.ncbi.nlm.nih.gov/23398016/ (b18)
- [V] Monteiro et al. (2015), Reflecting on diagnostic errors. https://pmc.ncbi.nlm.nih.gov/articles/PMC4539330/ (b19)
- [V] Croskerry (2013), Cognitive debiasing 1. https://pmc.ncbi.nlm.nih.gov/articles/PMC3786658/ (b23)
- [M] Elstein, Shulman, Sprafka (1978), Medical Problem Solving, Harvard University Press. Not opened; known only through the sources above.
- [M] Barrows et al. (1978), Groen and Patel (1985), Patel and Groen (1986), Kassirer and Gorry (1978): secondhand through a08, a21, a22.

AI and LLM studies
- [V] Pople, Miller, Myers; INTERNIST-I, in Clancey and Shortliffe (1984) ch. 8. https://impact.dbmi.columbia.edu/~ehs7001/Clancey-Shortliffe-1984/Ch8.pdf (c01, c02)
- [M] Miller, Pople, Myers (1982), INTERNIST-1, NEJM 307:468-476. https://www.neonatology.net/biblio/bib214.html (c03; secondary report)
- [V] Savage et al. (2023/2024), Diagnostic reasoning prompts. https://arxiv.org/abs/2308.06834 (a25-a28, b05, b06, c08; re-verified)
- [V] Nori et al. (2025), Sequential diagnosis with language models. https://arxiv.org/abs/2506.22405 (a29-a32, b01-b04, c19, c20, d09, d10; re-verified)
- [V] Brodeur et al. (2024), Superhuman performance of an LLM on the reasoning tasks of a physician. https://arxiv.org/abs/2412.10849 (a33-a35, b21, c06; re-verified)
- [V] McDuff et al. (2023), Towards accurate differential diagnosis with LLMs. https://arxiv.org/abs/2312.00164 (a36, b07, b08, c05; re-verified)
- [V, not re-verified] Kanjee, Crowe, Rodman (2023), JAMA. https://jamanetwork.com/journals/jama/fullarticle/2806457 (c04)
- [V] Goh et al. (2024), LLM influence on diagnostic reasoning: randomized trial. https://pmc.ncbi.nlm.nih.gov/articles/PMC11519755/ and https://jamanetwork.com/journals/jamanetworkopen/fullarticle/2825395 (b09, c07)
- [V] Goh et al. (2024), study protocol, LLM vs human coach. https://pmc.ncbi.nlm.nih.gov/articles/PMC11261684/ (b24; protocol only, no results)
- [V] Ke et al. (2024), Multi-agent conversations to mitigate cognitive bias. https://arxiv.org/abs/2401.14589 (a37, d13)
- [V] Qiu et al. (2025), MedR-Bench. https://arxiv.org/abs/2503.04691 (a38, c16)
- [V] Schmidgall et al. (2024), AgentClinic. https://arxiv.org/abs/2405.07960 (a39, c10)
- [V] Schmidgall et al. (2024), BiasMedQA. https://arxiv.org/abs/2402.08113 (c09)
- [V] Hager et al. (2024), Evaluation and mitigation of the limitations of LLMs in clinical decision-making. https://pmc.ncbi.nlm.nih.gov/articles/PMC11405275/ (b20, b25, c12)
- [V] Kim et al. (2026), bias-inducing prompts. https://pmc.ncbi.nlm.nih.gov/articles/PMC13528315/ (b22)
- [V] Li et al. (2024), MediQ. https://arxiv.org/abs/2406.00922 (c11)
- [V] Bani-Harouni et al. (2026), LA-CDM. https://arxiv.org/abs/2506.13474 (c13)
- [V] Shen et al. (2026), LDTL. https://arxiv.org/abs/2604.05116 (c14, c24)
- [V] Hsu et al. (2026), MedAction. https://arxiv.org/abs/2605.07305 (c15)
- [V] Wu et al. (2025), MedCaseReasoning. https://arxiv.org/abs/2505.11733 (c17)
- [V] Tu et al. (2024), AMIE. https://arxiv.org/abs/2401.05654 (c18, c23)
- [V] Sun et al. (2024), Conversational disease diagnosis via external planner-controlled LLMs. https://arxiv.org/abs/2404.04292 (c21)
- [V] ACTMED (2025), active test selection. https://arxiv.org/abs/2510.18988 (c22)
- [V] Wang et al. (2026), MedKGI. https://arxiv.org/abs/2512.24181 (d11)
- [V] Ge et al. (2026), ClinicalAgents. https://arxiv.org/abs/2603.26182 (d12)
- [V] Handler, Bedi, Shah (2026), premature closure in frontier LLMs. https://arxiv.org/abs/2605.15000 (d14)
- [V] Chiu, Pitis, van der Schaar (2025), viva voce simulations. https://arxiv.org/abs/2510.10278 (d15)
- [V] Cao and Chen (2026), VeriDx. https://arxiv.org/abs/2609.14018 (d16; intro and ablation table only)

## Source audit (2026-11-03)

Fresh auditors re-opened the sources of 8 established claims: 4 confirmed as written, 4 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **E01.01-K01** (now single-source: the sources are not independent). Barrows 1982 and Feightner 1977 are the same McMaster group (Barrows, Feightner, Neufeld, Norman), Barrows also co-authored the 1978 founding work, and the Feightner 1977 abstract gives only a model, no hypothesis-generation finding, so 'independently replicated' is not supported; Barrows 1982 numbers (18+19 physicians, 62 encounters) match.
- **E01.01-K05** (reworded: the sources support less). Arocha and Patel page could not be opened (blocked); the LLM part rests on one qualitative remark that o3 'seemed to anchor' (Nori) and Ke's 0/80 initial accuracy on case reports selected for bias-driven misdiagnosis, neither of which measures anchoring in plain LLMs. Corrected claim: In a small think-aloud study (Arocha and Patel 1991; 4 participants per group plus one resident, figures not independently checked) cues were mostly used as confirming (71% to 92%) and all second-year students kept their initial hypothesis despite contradictory data; for LLMs, authors report qualitatively that an off-the-shelf o3 baseline seemed to anchor on first impressions (Nori 2025), and a multi-agent GPT-4 setup raised top-diagnosis accuracy from 0/80 to 71.3% on 16 bias-driven misdiagnosis cases (Ke 2024), but plain-model anchoring was not measured.
- **E01.01-K11** (reworded: the sources support less). All numbers match, but the random-planner score (84.8; 85.4 +- 1.3 over 5 seeds) appears only in the LDTL preprint, whose LA-CDM and ReAct numbers are copied from the LA-CDM paper, so this is a single-source cross-paper comparison, not independent confirmation; Hager does not test a random planner. Corrected claim: In the LDTL preprint (Llama-3-8B, MIMIC-CDM), a random test-selection planner scored 84.8% (85.4 +- 1.3 over 5 seeds), above the prompted ReAct agent (74.9) and the trained hypothesis-driven LA-CDM (81.3) as reported by the LA-CDM authors; only LDTL's learned planner (93.4) beat random clearly. This random-planner comparison comes from one preprint and was not independently replicated.
- **E01.01-K23** (number corrected). The 0.93 to 0.65-0.75 figures are correct but are VivaBench's approximate (lenient) top-1 accuracy from appendix Table 8 (six models, full information 0.90-0.94, final 0.65-0.75); the main-text exact top-1 for the best model is 35% final vs 69% full information, a larger relative fall, and the metric is not labelled in the claim. Premature-closure numbers match. Corrected claim: LLMs commit prematurely when information is insufficient: about 70% false action when the right option is removed (55-82% by model on MedQA), 81% premature closure on underspecified low-risk cases vs 19% on urgent ones, and a safety prompt lowers false action to about 48%, not to zero (Handler et al. 2026). In VivaBench multi-turn exams, approximate (lenient) top-1 accuracy of about 0.90-0.94 with full information falls to 0.65-0.75 after data gathering across six models, and exact top-1 for the best model falls from 69% to 35%.
- **E01.01-K08** (now single-source: only one opened source, code check).
- **E01.01-K18** (now single-source: only one opened source, code check).
- **E01.01-K22** (now single-source: only one opened source, code check).
