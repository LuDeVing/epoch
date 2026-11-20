# Forward and backward reasoning: deep document

*Subfield E01.02. Sources: evidence_a-d.jsonl, claims.jsonl, critique.md in this folder. Evidence ids (a01 ... d18) refer to those files; claim ids (K01 ... K26) are E01.02-K01 ... K26. Schema labels: claims.jsonl used loose operator labels ("O3 backward check"). In SCHEMA.md, O3 is Decompose and O5 is Work backwards. This document maps items to the real parts: the backward check lives in S4 TEST / S7 SELECT (a discriminating test), and O5 covers goal-to-facts search on closed problems.*

## 1. What it is

Two directions of inference in diagnosis.

- **Forward reasoning**: from a finding to a hypothesis. Data in, diagnosis out. Fast, cheap on working memory, works when knowledge is enough.
- **Backward reasoning**: from a hypothesis to the findings it predicts, then a check against the case. Slow, heavy on working memory. Also called hypothetico-deductive.
- **Scheme-inductive reasoning** (Coderre): forward along a decision tree with crucial tests. Used by experts when plain pattern recognition fails.
- **Pattern recognition**: the case matches a stored script. Counted with forward reasoning in most studies.

The famous claim (Patel and Groen 1986): experts reason forward; novices, and experts on hard cases, reason backward. This subfield is background for our agent. The link from "direction" to "expertise" is doubted. Direction tracks case difficulty and knowledge structure more than skill. For LLMs, nobody has tested the human claim directly (K17). What exists is engineering work that adds a "backward check" to a forward diagnosis. It gives small gains.

## 2. History and theories in depth

**Elstein, Shulman, Sprafka (1978).** Hypothetico-deductive model: doctors generate a few hypotheses early and test them. It became the teaching standard (a19, not opened).

**Larkin, McDermott, Simon, Simon (1980).** In physics, experts work forward from givens; novices work backward from the unknown (a18, not opened). The medical work borrows this.

**Groen and Patel (1985).** Argued that "experts use hypothetico-deductive reasoning" was never shown. Cognitive psychology says it is a novice trait or an intellectual tool, not a habit. Experts use strong knowledge-dependent methods (d02, opened, theory only).

**Patel and Groen (1986), Cognitive Science 10:91-116.** The founding study. Seven cardiologists, one case of acute bacterial endocarditis; they explained its pathophysiology. Accurate diagnosers showed pure forward reasoning through causal rules. Inaccurate ones mixed forward and backward (d01, abstract only; per-group counts never seen). Cited 427 to 632 times depending on source.

**Patel, Arocha, Groen (1987).** Six cardiologists, six psychiatrists, six surgeons, same case, five components. Every protocol mixed directions. More forward in familiar territory, more backward in unfamiliar. Each specialty explained the component near its own domain (a01-a03). This already weakens the clean "experts forward" story. It is a mix driven by familiarity.

**Joseph and Patel (1990).** Endocrinology case. Generating hypotheses did not separate high- from low-knowledge physicians. Evaluating them did. High-knowledge subjects looked for confirmation and refined the first hypothesis. Low-knowledge subjects made alternatives after they already had the answer (a09, secondhand).

**Patel, Groen, Arocha (1990).** "Medical expertise as a function of task difficulty": backward reasoning shows up in experts on hard cases (a17, title and citation only).

**Arocha and Patel (1991).** Students (years 2, 3, 4) and a resident on two cardiology cases. All mixed direction; more forward went with accuracy. Year-2 students held their first hypothesis and reinterpreted contradicting cues. The resident listed many initial diagnoses, then used backward inference to reach the right one (a05-a08).

**Coderre et al. (2003, 2004).** Think-aloud in gastroenterology. Pattern recognition and scheme-inductive reasoning gave higher odds of a correct diagnosis than hypothetico-deductive reasoning (2003, abstract only). The 2004 paper gave the cleanest numbers on direction by expertise and difficulty (a10-a12).

**Bass et al. (2013).** Forced analysis of the first hypothesis, with primed direction. The best direction depended on expertise (a14, b05).

**Later accounts.** Cognitive zipper (2020): early inquiry backward, late inquiry forward, so direction changes inside one case (b17). Schmidt and Rikers (2007): knowledge encapsulation into illness scripts is the main rival explanation (d04). A 2023 review says hypothetico-deductive use does not explain the novice-to-expert transition (d03).

**Where the theory stands.** The mixed picture is the accepted one. Direction is a surface sign of three things: how familiar the case is, how hard it is, and how well organised the knowledge is. Treating direction as a trait of expertise is the doubted part. No direct failed replication was found, but the original N is tiny (7, one case), and the 1990s replications (Patel 1990/1994, Rikers 1997) were not retrieved.

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Founding result: accurate diagnosers pure forward, inaccurate mixed | 7 cardiologists, 1 endocarditis case; no per-group counts seen | Patel and Groen 1986 (d01, abstract) | single-source, thin |
| Every protocol mixes directions | 18 physicians (6 per specialty), 1 case; cardiologist 7 mixed on components 1 and 2, pure forward on 3; psychiatrist 2 had no pure component | Patel et al. 1987 (a01, a03) | established (K01) |
| Specialty shapes which component gets explained | Subjects (of 6) explaining: aortic insufficiency 6 cardiologists, 2 psychiatrists, 2 surgeons; IV drug use 2, 5, 6; infection 4, 5, 6; acuteness 1, 2, 5; emboli 5, 2, 3 | Patel et al. 1987 (a02) | single-source, counts only |
| More forward goes with accuracy (students) | 4 students per year plus 1 resident, 2 cases; correct diagnosis in 5 subjects (two year-2, two year-4, the resident); only the resident correct on both | Arocha and Patel 1991 (a05) | contested (K04) |
| Hypothesis count rises with training | After segment 1: year 2 = 1.5, year 3 = 3, year 4 = 3.4, resident = 5 | Arocha and Patel 1991 (a06) | single-source |
| Confirmation dominates | Confirming relations: year 2 71%, years 3-4 88%, resident 92% | Arocha and Patel 1991 (a06) | single-source |
| Experts use pattern or scheme-inductive reasoning far more | 20 experts v 20 non-experts, 80 items per format. Hypothetico-deductive: experts 5 and 5; non-experts 37 (MCQ), 32 (EMQ). Expert-type use about 90% (experts) v over 50% (non-experts) | Coderre 2004 (a10, b04) | single-source (K03) |
| Expertise coefficient | 2.69, CI 1.64-3.75, log-odds scale. Do not quote as an odds ratio (exp(2.69) = 14.7; the paper's own text says "about threefold") | Coderre 2004 (b04; critique) | caveat |
| Hard cases push everyone backward | Diarrhea: experts HD 2 and 1 of 20; non-experts 13 and 14 of 20. Hard-presentation coefficient -1.55 (CI -2.67 to -0.43, p=0.01). Judge agreement 0.84. Format effect p=0.31 | Coderre 2004 (a11, b04) | established as pattern (K02) |
| Forced analysis of first hypothesis nearly doubles accuracy | 9 nephrologists, 6 residents, 10 cases. 31.1% to 65.6% (nephrologists), 40.0% to 70.0% (residents), both p<0.001. Initial accuracy 34.7%. 35% of diagnoses changed; 96% wrong-to-right, 4% right-to-wrong | Bass 2013 (a14, b05) | single-source (K05) |
| Best direction depends on expertise | Scheme-inductive priming: residents OR 5.69 (1.59-20.33); nephrologists OR 0.57 (0.23-1.39). Experts failed to produce a scheme in 70% of cases. Change rate did not differ (p=0.70 by group, 0.90 by strategy) | Bass 2013 (a14, a15, b05) | single-source (K06); source has p=0.07 v p<0.01 inconsistency |
| Exam reasoning: forward dominates; high scorers use both more | N=210 year-5 students; 87% of answers coded as clinical reasoning. FR>BR p=0.006 and p<0.001. High v low scorers: FR OR 3.33 (2.38-4.49), BR OR 2.67 (1.67-4.26) | Klutmann 2026 (b01) | single-source (K19) |
| Backward rises on hard items | Factual item FR 98.9% v diagnostic item FR 66.7% (BR 1.1% v 33.3%). Feedback did not change type (chi2=3.38, p=0.281). Follow-up questions: BR OR 2.49 (2.29-2.84) in one term, none in the other (p=0.299) | Klutmann 2026 (b02) | single-source |
| Direction label and tool design are different things | Dental radiology, 99 students. Mean improvement: diagnosis-first Atlas 3.86, feature-first ORAD 1.99, control 1.24. Atlas v ORAD d=0.714 (p=0.014); Atlas v control d=0.997; ORAD v control p=0.769. 80 of 152 ORAD errors came from a filter that excluded the truth | Singapore trial 2022 (b07) | single-source (K09) |
| Process activities add to knowledge | N=106 students (years 3-5); hypothesis generation, evidence generation and evaluation explain success beyond knowledge | Virtual patients 2023 (a22) | single-source |
| "Be slow and reflective" does nothing | Residents n=96 and n=108, 20 cases. 44.5% (fast) v 45.0% (reflect); 69 s v 89 s | Norman 2014 (b06, snippet) | established (K07) |
| Differential checklist helps only if it holds the truth | 90 students, 6 cases. Control 0.49; correct-containing checklist 0.75; prompt alone 0.69 (own list had truth); DDXC+ 0.89; DDXC- 0.66 for listed diagnoses, final accuracy 0.43 (p=0.602 v control). Mean rank of truth 2.57 / 2.04 / 2.42 | Kaemmer 2021 (b11, critique fix) | single-source (K08) |
| Physicians with an LLM do not improve | 50 physicians; 76% v 74%, +2 (CI -4 to 8, p=0.60). LLM alone +16 (CI 2-30, p=0.03). UK replication n=22, gap to LLM alone 21.3 points | Goh 2024; Healy 2026 (b13, b14) | established (K16) |
| LLM v human, pooled | 1609 vignettes. Binary OR 0.65 (0.38-1.12, p=0.12); SMD 0.08 (-0.19 to 0.35); v novices OR 0.62 (0.35-1.1), I2=0% | Meta-analysis 2026 (b18) | established, not about direction |
| Dual-Inf (forward plus backward) beats self-consistency CoT | Open-XDDx 570 notes, 9 specialties. GPT-4 accuracy 0.533 v 0.472 (+0.061, CI 0.055-0.062); interpretation 0.446 v 0.334; rare diseases 0.483 v 0.425. Other bases +0.059 (GPT-4o), +0.048 (Llama3-70B), +0.049 (BioLlama3-70B), p<0.001 | Zhou 2024 (c01, c03, d11) | established, no compute match (K10) |
| Dual-Inf ablation | Full 0.533; ablations 0.443-0.497; about 7 points over the variant without the backward module | Zhou 2024 (c02, d12) | single-source |
| Dual-Inf error profile | Per 100 notes where SC-CoT was wrong: missing content 89 v 76; factual errors 8.2 v 17; low relevance 10.8 v 15.4. Compared with SC-CoT, not with its own ablations | Zhou 2024 (c03, d12) | contested (K11) |
| MSDiagnosis backward step | 2,225 Chinese admission records, 12 departments. Final F1 34.32 full v 32.04 without backward (-2.28; macro-recall -2.27). Differential F1 only about 8-11 | Zeng 2024 (c06, c07) | small, no significance test |
| First answer governs final answer | Primary matches final: multi-step F1 39.33. Primary differs from final: 18.12 | Zeng 2024 (c07) | established (K12) |
| LLMs anchor like the Einstellung effect | 5,383 counterfactual pairs, 49 diseases, 8 departments. Trap rates: Gemini-2.5-Pro 60.90, GPT-5 51.87, Claude Sonnet 4.5 42.98, DeepSeek-R1 46.12, Kimi-k2 47.12. GPT-5 failures: 35% perceptual blindness; of the rest 43% underthinking, 22% overthinking | MedEinst 2026 (c08, c09, d08) | single-source (K13); paper text and table disagree on which model has top accuracy |
| Forward plus backward agent cuts trap rate | Qwen3-32B base / robust / trap: 40.25 / 11.86 / 43.46; + causal graph 55.49 / 19.94 / 38.32; + critic and memory 69.49 / 24.21 / 33.75. Debate agents robust accuracy about 8-10% | MedEinst 2026 (c10, d09) | single-source; no shadow-only ablation |
| A generic warning backfires | Qwen3-32B: accuracy 40.25 to 52.60, robust 11.86 to 8.70, trap 43.46 to 60.50. Qwen3-235B trap 43.32 to 58.00 | MedEinst Table A2 (d10) | single-source |
| Persona prompts do nothing | MedQA GPT-4: CoT 76%, differential 78% (+2.2, P=0.24), analytic 78%, Bayesian 72% (-3.4, P=0.07). GPT-3.5: CoT 46, analytic 40 (P=0.001), differential 38 (P<0.001), Bayesian 42 (P=0.02) | Savage 2024 (c12) | single-source (K14) |
| Misleading supplied differential harms LLMs | 61 NEJM cases, 21 variants of 8 models. 14 of 21 lost accuracy (mean -5.4, range +0.2 to -29.8; GPT-4o -29.8, LLaMA-3.3-70B -17.2). Expert input +20.4, all 21 significant | Lopez 2026 (d05) | single-source (K08, K21) |
| Thinking budget helps in some models only | GPT-5 gap 10.4 to 1.7-4.4; Qwen3 -11.7 to -3.9; Claude Sonnet 4.5 and Gemini 3 Pro unchanged | Lopez 2026 (d06) | single-source |
| Reliability cue recovers the loss | GPT-5 baseline loss 10.4 (75.5 to 65.1); Claude 3.2 (70.5 to 67.3), with cue 73.0 (p=0.045 v alone); Gemini 3 Flash 2.9 | Lopez 2026 (d07) | single-source (K22) |
| Generic self-review hurts | GPT-3.5 CommonSenseQA 75.8 to 38.1; GPT-4 GSM8K 95.5 to 91.5 to 89.0. With oracle error labels: GPT-3.5 GSM8K 75.9 to 95.5; GPT-4 HotpotQA 29.0 to 59.0 (100 q) | Huang 2024 (d13) | established (K23) |
| Backward verification in math | FOBAR 83.5 v SC 81.4 (+2.1); 85.0 v 83.2 (+1.8, ComplexCoT). Self-verification average +2.33 (arithmetic +1.67 / +2.84) | Jiang 2024; Weng 2023 (c14, c15) | established, small (K15) |
| Backward proof search in closed logic | LAMBADA depth 5, relative gains: ProofWriter +44% v CoT, +56% v SI; PrOntoQA +37% v CoT, +113% v SI | Kazemi 2023 (c13) | established (K15); relative, not absolute |
| Training with reverse reasoning | RevThink +13.53% over zero-shot student; forward-only distillation +6.69% | Chen 2025 (c16) | single-source; training, not scaffold |
| Option bias in LLM MCQ | Option-ID bias survives debiasing instructions; permutation debias +15.2 on llama-30b. Open-style scores about 25% below MCQ | Zheng 2024; Myrzakhan 2024 (d14, d15) | single-source (K24) |
| Reasoning models: sound facts, missing steps | R1 accuracy 71.79% (1 turn), 76.18% (free turn), 89.76% (oracle). Factuality above 90%; exam recall best 43.61% | MedR-Bench (d16) | single-source (K25) |
| o1-preview on NEJM | Correct dx in differential 78.3% (70.7-84.8); first dx 52%; exact or close 88.6% v GPT-4 72.9% on 70 cases. Reasoning score 86% v GPT-4 42%, physicians 34% | Brodeur 2024 (c17) | single-source, no direction arm |

## 4. Mechanisms and models

An engineer can implement these as trace labels and prompt stages.

**4.1 Direction label on a trace.** Split the reasoning into steps. Tag each step:
- F (finding to hypothesis): the step starts from a case fact and names or raises a diagnosis.
- B (hypothesis to finding): the step starts from a candidate, names a finding it predicts, and looks it up in the case.
- Pure forward = all F. Mixed = F and B in chains.
Code can do the tagging with a separate model call. Patel's coding was by hand with no inter-rater data in the 1987 paper; Coderre reports judge agreement 0.84.

**4.2 Semantic network view (Patel).** Facts and hypotheses are nodes. Forward = a path from fact to hypothesis. Backward = a path from hypothesis to fact. A case explanation is a connected set of paths. Accuracy relates to whether the paths are causal and complete.

**4.3 Why forward is cheap and where it breaks.** Each finding triggers stored rules; there is no search over the hypothesis space. It breaks when a rule is wrong or a filter drops the truth early (80 of 152 ORAD errors, b07). Backward needs the hypothesis held in working memory while looking for matching findings (a08). Backward becomes strong when the search space is closed and small, because forward chaining blows up with depth (LAMBADA, c13).

**4.4 The cognitive zipper.** Early: backward, open inquiry. Late: forward, confirmatory reading of new findings as support (b17). Risk: confirmation dominates (71 to 92% confirming relations, a06). A scaffold needs a disconfirming test, not only a confirming one.

**4.5 Backward check as a procedure (Dual-Inf, c01, c05).**
1. Forward module: list diagnoses from the case.
2. Backward module: for each diagnosis, write the findings expected if it were true.
3. Examination module: check each expected finding against the note; mark present, absent, unknown.
4. Self-reflection loop: low-confidence diagnoses go back to the forward module; most notes were revised more than once.
Reported gain +6.1 points on GPT-4 over SC-CoT. No token accounting.

**4.6 Shadow-node score (ECR-Agent, c11).** S(d) = w_m * matches - w_c * conflicts - w_s * shadow. Shadow = expected evidence that could not be verified. Weights are hyperparameters. Code computes S(d) and selects, which fits G5.

**4.7 Forced analysis of the first hypothesis (Bass, b05).** Record the first diagnosis. Analyse it with a stated direction. Allow a change. 35% changed; 96% of changes were wrong-to-right. The second look carries content (features for and against), not a generic "look again".

**4.8 Provenance tag (Lopez, d07).** Tag any supplied hypothesis with its source and reliability. The model discounts a hypothesis from an unsure source and keeps the gain from an expert source.

**4.9 Option-first v blind-first.** In MCQ, backward reasoning starts from options (Klutmann). LLM analogue: generate a differential blind, then match to options. Untested in medicine.

## 5. What holds up

**Consistent across several sources.**
- Mixed direction inside one case (Patel 1987, Arocha 1991, Coderre 2004, Klutmann 2026). The most solid fact (K01).
- Backward use rises with difficulty, in experts too (Coderre, Klutmann, Patel 1990 as cited) (K02, 4 sources).
- Generic "slow down" or "reflect" instructions do not help (Norman 2014, Pelaccia 2025 review, Huang 2024, MedEinst warning) (K07, K23).
- Early errors propagate (MSDiagnosis, MedEinst) (K12).
- The rival account has support: knowledge encapsulation and illness scripts (d03, d04) (K26).

**Contested.**
- Forward use goes with accuracy (K04). Correlational, confounded with expertise and difficulty. Coderre 2003 supports it but was seen as abstract only. Arocha 1991 has 4 students per group.
- Direction shift across stages (zipper, K20) is a qualitative model.
- Dual-Inf factual-error rise (8.2 to 17 per 100) sits beside fewer missing items, and is measured against SC-CoT only (K11).

**Failures and caveats.**
- The founding paper rests on N=7, one case. Per-group counts never read.
- No direct failed replication found, and no large-N direct replication. The 1990s replications were not retrieved (b24, d18).
- Coderre 2.69 is a log-odds coefficient. The Bass 2013 page has p=0.07 in the abstract and p<0.01 in the results.
- MedEinst contradicts itself on which models have top accuracy (54.30%, 53.58%), so "higher accuracy, more trap-prone" is weak. Trap rates above 50% for GPT-5 and Gemini-2.5-Pro hold.
- Kaemmer's wrong-checklist arm scored 0.43 v control 0.49, p=0.602. Harm is not shown.

**Moderators.**
- Case difficulty (strongest).
- Expertise: priming helped residents (OR 5.69), not experts (OR 0.57, CI crosses 1).
- Tool design: a feature-first aid failed through filters; a diagnosis-first aid helped novices (d=0.714).
- Whether the list holds the truth (Kaemmer 0.75 v 0.43).
- Model and thinking budget for LLMs (GPT-5 and Qwen3 gain; Claude Sonnet 4.5 and Gemini 3 Pro do not).
- Time pressure and response time (Alqahtani 2016, Sherbino 2012; titles only).

**Interventions that worked.**
- Forced analysis of first hypothesis (humans, N=15).
- Checklist containing the truth (humans).
- Expected-findings backward check in LLMs (+6.1 Dual-Inf; +2.28 MSDiagnosis).
- Reliability cue on supplied hypotheses (LLMs).
- Oracle feedback in self-correction (LLMs).

**Interventions that did not.**
- Be slow or be reflective (humans).
- Clinician-style persona prompts (LLMs).
- Generic self-review without feedback (LLMs).
- Generic warning about distractors (LLMs).
- Feature-first forward tool for novices (humans).
- Formative feedback on reasoning type (p=0.281).
- Giving physicians an LLM (+2, n.s.).

## 6. Language models

**Direct tests of the Patel-Groen claim in models: none found** (K17; 0 of 10 opened sources; reasoning-model reviews do not code direction, b20, d16). "Forward" and "backward" in LLM papers are engineering labels.

**Clinical LLM work that uses both directions.**
- Dual-Inf: +6.1 points over SC-CoT on GPT-4 (0.533 v 0.472); +4.8 to +5.9 on three other bases (all p<0.001). Interpretation +11 points. Factual errors per 100 rose 8.2 to 17 (SC-CoT comparison). No compute-matched test.
- MSDiagnosis: backward step adds +2.28 final F1 on 2,225 cases. Gains within about 2 points across ablations; no significance test.
- ECR-Agent (MedEinst): trap rate 43.46 to 33.75 and robust accuracy 11.86 to 24.21 on Qwen3-32B. The graph module bundles forward, backward and shadow parts, so the backward share is unknown. Debate baselines reached robust accuracy of only about 8-10% (supports G9).

**Anchoring.** Strong models fall for the stereotypical diagnosis when one discriminating fact is added: trap rates 43 to 66% (Claude Sonnet 4.5 lowest at 42.98; DeepSeek-R1 46.12). A generic warning raised it to 60.50. A misleading supplied differential cost 14 of 21 models accuracy; GPT-4o lost 29.8 points.

**What changed it, by how much.**
- Extra thinking: GPT-5 gap 10.4 to 1.7-4.4; Qwen3 -11.7 to -3.9; no change in Claude Sonnet 4.5 or Gemini 3 Pro.
- Reliability cue: GPT-5 and Gemini 3 Flash recover; Claude Sonnet 4.5 partly (73.0, p=0.045 v alone).
- Persona style: GPT-4 +2.2 (n.s.); GPT-3.5 down 4 to 8 points.
- Generic self-review: GPT-3.5 CommonSenseQA 75.8 to 38.1.
- Information supplied: R1 71.79% to 89.76% as findings are given. Reasoning text factual above 90%, but exam-recommendation recall at best 43.61%.

**Non-clinical backward checks.** FOBAR +1.8 to +2.1; self-verification +2.33; LAMBADA +37% to +113% relative at depth 5; RevThink +13.53% (training). Gains are biggest where the task is closed and formal.

**Human-AI.** Giving physicians an LLM: +2 points (n.s.). The LLM alone scored 16 points higher than the physicians. A UK replication agrees in direction. Interface and use matter more than direction.

**Gaps.** No equal-token comparison, no direction-by-difficulty test, no trace coding of reasoning models, no option-first v blind-first test in medicine.

## 7. What our agent should take

Schema parts use real SCHEMA.md labels. Status: [E] established, [S] single-source, [C] contested.

### Add now (established)

| Item | Part | Status | Evidence |
|---|---|---|---|
| Do not add "slow down", "be careful" or a clinician persona. Already in 4b; this subfield reconfirms it | 4b, G11 | [E] | K07, K14; b06, c12, d10 |
| No generic reflect step. Any revision must name a specific finding to look for or a failing output | G2, S5 | [E] | K23; d13, d10, b11 |
| Expect mixed direction. Log direction labels on traces as a diagnostic only, not as a target | S2 trace | [E] | K01; a03, a05, b01 |
| Spend more backward effort on hard items; direction follows difficulty, so allocate by difficulty | G12, S0 | [E] | K02; a11, b02 |
| Early errors propagate: keep the first answer, but harvest all candidates raised in traces so it is not the only one tested | S3, S4 harvest | [E] | K12; c07, c08 |
| Goal-to-facts (work backward) only on closed formal sub-problems | O5 | [E] | K15; c13, c14, c15 |
| Do not cite human-LLM trial results as evidence about direction | none | [E] | K16; b13, b14, b18 |

The backward expected-findings check (K10) is rated [E] in claims.jsonl for its gain, but the gain is +2 to +6 points with no compute match and a factual-error rise (K11, contested). It stays in "Test first" until an equal-token test passes (G7).

### Test first

| Item | Part | Status | Evidence |
|---|---|---|---|
| Backward expected-findings check ("what findings would I see if d were true") on diagnosis items | S4 / S7 discriminating test | [E] gain, [C] cost and errors | K10, K11; c01, c06, d11, d12 |
| Shadow-evidence score computed in code (matches, conflicts, unverified expected findings) | S7, G5 | [S] | K13; c10, c11, d09 |
| Forced analysis of the first hypothesis with content (features for and against) | S5, G2 | [S] | K05; a14, b05 |
| Tag every supplied hypothesis with source and reliability; blind-first generation before reading supplied options or candidates | S1 input hygiene, S0 | [S] | K21, K22, K24; d05-d07 |
| Candidate list that lacks the truth: check for harm | S3, memory | [S] | K08; b11, d05 |
| Direction instruction by difficulty (forward-first v hypothesis-first) | S0 mode choice | [C] | K06, K09; b05, b07 |
| No hard early filter on candidates before testing | S4 | [S] | K09; b07 |
| Delay commitment to the first hypothesis | S3 | [S] | K12, K05 |

## 8. Concrete tests on our bench

All arms at equal total tokens (count calls, retries and any setup).

1. **Backward check v self-consistency.** Items: held-out differential diagnosis (DDXPlus-style cases, NEJM-like vignettes, MedQA diagnosis items). Arms: (a) plain model, (b) self-consistency with k votes, (c) forward draft plus expected-findings check per candidate. Metric: top-1 and top-3 accuracy; factual-error rate per 100. Expected: +2 to +6 points if real; the error rate shows whether the module raises it.
2. **Shadow score by code v prompt-only check.** Items: trap pairs (same prior, one discriminating fact; MedEinst-style, built from DDXPlus). Arms: plain, prompt-only backward check, code-computed S(d) with shadow term. Metric: trap rate, robust accuracy. Expected: trap rate falls a few points; the code score at least matches the prompt check.
3. **Direction instruction by difficulty.** Items: one set split into easy and hard by the plain model's pass rate. Arms: forward-first, hypothesis-first, no instruction. Metric: accuracy per stratum and the interaction. Expected: hypothesis-first helps on hard items and does nothing or hurts on easy ones (extrapolated from Coderre and Bass; no LLM data).
4. **Misleading supplied hypothesis.** Items: cases with a wrong supplied differential. Arms: untagged, tagged with source reliability, blind-first then compare. Metric: inclusion of the true diagnosis; loss against no hint. Expected: the tag cuts the loss as in GPT-5 and Gemini. Run at two thinking budgets.
5. **Candidate list without the truth.** Arms: no list, list with truth, list without truth (lists built by code). Metric: accuracy. Expected: without-truth does not help and may lower accuracy; with-truth raises it.
6. **Option-first v blind-first.** Items: multiple-choice diagnosis. Arms: options shown with the case; blind differential, then options. Metric: accuracy and option-position bias. Expected: blind-first at equal or better accuracy, with less position bias.
7. **Trace direction coding.** Label F and B steps on traces of the plain model and a reasoning model across difficulty. Metric: B share by difficulty. Expected: B share rises with difficulty (Klutmann: 1.1% to 33.3%). Cheap and diagnostic only.
8. **Generic reflect v content-bearing check.** Arms: "review your answer" v "name one finding that would contradict this answer". Metric: accuracy change and right-to-wrong flips. Expected: generic equal or worse; content check better.

## 9. What does not transfer, and why

- **The expertise story.** Models have no illness scripts built by years of cases. Direction in a model reflects its prompt and training mix, not a developed skill. "Experts go forward" gives a scaffold no instruction.
- **Working-memory cost of backward reasoning.** The human argument for why backward is slow (a08) does not apply to models. Their cost is tokens, not memory slots.
- **Think-aloud protocols.** Spoken human reasoning is a rough window on process. A model's written reasoning is not evidence of its process (G10).
- **Tiny human samples.** N=7, N=15, four per group. An OR of 5.69 with CI 1.59 to 20.33 is too wide to import.
- **Human-AI collaboration results** (Goh 2024) concern interface and use, not direction.
- **Text-only benchmarks.** Dual-Inf and MSDiagnosis use written notes and Chinese admission records. They do not test gathering data live. Exam-style notes are not real EHR.
- **MCQ direction effects** (Klutmann) come from year-5 students on exam items. They do not predict a model's option effects.
- **Training-based gains** (RevThink +13.53%) need fine-tuning. Our agent is a scaffold.

## 10. Open questions

1. Does an expected-findings check beat self-consistency at equal tokens, and does it raise factual errors?
2. Does the best direction instruction depend on difficulty or model strength in LLMs, as human expertise did in Bass 2013?
3. What do the Patel and Groen (1986) per-group counts show, and did Patel 1990/1994 and Rikers 1997 replicate them?
4. Is MedEinst's "stronger prior, higher trap rate" pattern real once its table is read cleanly? Does a shadow-only penalty reduce trap rate?
5. Does the Dual-Inf gain hold under matched compute and on newer models (Claude, Gemini 3)?
6. Do reasoning models show mixed forward and backward traces whose share shifts with difficulty?
7. Does a bare candidate list without the truth anchor an LLM? (Lopez tested a clinician differential with rationale, not a bare list.)
8. Does option-first reasoning lower LLM accuracy in diagnosis against blind-first?
9. Why do Claude Sonnet 4.5 and Gemini 3 Pro not gain from thinking budget on misleading input? They lost little to begin with; a ceiling or different training are both possible.

## 11. Sources

[V] opened, [M] snippet, title or abstract only.

- [V] Patel, Arocha, Groen (1987) Domain specificity and knowledge utilization in diagnostic explanation. https://escholarship.org/uc/item/1hq221d3 (a01-a04)
- [V] Arocha and Patel (1991) Hypothesis generation and the coordination of theory and evidence. https://escholarship.org/uc/item/0rc9t79c (a05-a09, a20)
- [V] Coderre et al. (2004) Impact of two multiple-choice question formats. https://pmc.ncbi.nlm.nih.gov/articles/PMC533882 (a10-a12, b04)
- [M] Coderre et al. (2003) Diagnostic reasoning strategies and diagnostic success. https://pubmed.ncbi.nlm.nih.gov/12895249/ (a13, b03)
- [V] Bass et al. (2013) Experienced physicians benefit from analyzing initial diagnostic hypotheses. https://pmc.ncbi.nlm.nih.gov/articles/PMC4563663 (a14, a15, b05)
- [M] Patel and Groen (1986) Knowledge based solution strategies in medical reasoning, abstract only. https://doi.org/10.1207/s15516709cog1001_4 (a16, b09, d01; full text not opened; c20 has a wrong DOI)
- [M] Patel, Groen, Arocha (1990) Medical expertise as a function of task difficulty. https://doi.org/10.3758/BF03197128 (a17)
- [M] Larkin et al. (1980) Expert and novice performance in solving physics problems. https://doi.org/10.1126/science.208.4450.1335 (a18)
- [M] Elstein, Shulman, Sprafka (1978) Medical problem solving (book; no URL; a19)
- [V] Scoping review of clinical reasoning literature (2020). https://pmc.ncbi.nlm.nih.gov/articles/PMC7140328 (a21)
- [V] Diagnosing virtual patients (2023). https://pmc.ncbi.nlm.nih.gov/articles/PMC10099021 (a22)
- [V] Transforming clinical reasoning: role of AI (2025). https://pmc.ncbi.nlm.nih.gov/articles/PMC12813117 (a23)
- [V] Klutmann et al. (2026) Forward and backward reasoning in exam items. https://europepmc.org/article/PMC/PMC13316782 (b01, b02)
- [M] Norman et al. (2014) Etiology of diagnostic errors. https://pubmed.ncbi.nlm.nih.gov/24362377/ (b06)
- [V] Singapore dental radiology trial (2022). https://europepmc.org/article/PMC/PMC9334535 (b07)
- [M] Norman et al. (1999) Benefit of diagnostic hypotheses. https://doi.org/10.1207/s1532690xci1704_3 (b08); Baghdady 2014 as cited (b16)
- [M] Khan et al. (2022) Diagnostic errors, expertise, time, checklist. https://europepmc.org/article/PMC/PMC9676601 (b10)
- [V] Kaemmer et al. (2021) Differential diagnosis checklists. https://europepmc.org/article/PMC/PMC9290564 (b11)
- [V] Pelaccia et al. (2025) Diagnostic reasoning and cognitive error in EM. https://europepmc.org/article/PMC/PMC11921069 (b12)
- [V] Goh et al. (2024) LLM influence on diagnostic reasoning RCT. https://europepmc.org/article/PMC/PMC11519755 (b13)
- [M] Healy et al. (2026) UK replication. https://europepmc.org/article/MED/42053372 (b14)
- [V] Cardiac arrest team leaders in VR (2025). https://europepmc.org/article/PMC/PMC11878170 (b15)
- [V] Cognitive zipper model (2020). https://europepmc.org/article/PMC/PMC7188939 (b17)
- [V] Meta-analysis AI v physicians (2026). https://europepmc.org/article/PMC/PMC13338529 (b18)
- [V] Waqas et al. (2026) Reasoning beyond accuracy. https://europepmc.org/article/PMC/PMC13741565 (b19)
- [V] Sim and Chen (2025) Critique of impure reason. https://europepmc.org/article/PMC/PMC12563542 (b20)
- [V] REACT-AI protocol (2026). https://europepmc.org/article/PMC/PMC13643257 (b21)
- [M] Monteiro et al. (2015) https://doi.org/10.1007/s11606-015-3369-4 (b22); Alqahtani et al. (2016) https://doi.org/10.1097/ACM.0000000000001098 (b23); Sherbino et al. (2012) https://doi.org/10.1097/ACM.0b013e318253acbd (b25)
- [V] Zhou et al. (2024) Dual-Inf. https://arxiv.org/abs/2407.07330 (c01-c05, d11, d12)
- [V] Zeng et al. (2024) MSDiagnosis. https://arxiv.org/abs/2408.10039 (c06, c07)
- [V] MedEinst (2026). https://arxiv.org/abs/2601.06636 and https://aclanthology.org/2026.acl-long.1847.pdf (c08-c11, d08-d10)
- [V] Savage et al. (2024) Diagnostic reasoning prompts. https://arxiv.org/abs/2308.06834 (c12)
- [V] Kazemi et al. (2023) LAMBADA. https://arxiv.org/abs/2212.13894 (c13)
- [V] Jiang et al. (2024) FOBAR. https://arxiv.org/abs/2308.07758 (c14)
- [V] Weng et al. (2023) Self-verification. https://arxiv.org/abs/2212.09561 (c15)
- [V] Chen et al. (2025) RevThink. https://arxiv.org/abs/2411.19865 (c16)
- [V] Brodeur et al. (2024) o1-preview. https://arxiv.org/abs/2412.10849 (c17, c19)
- [V] McDuff et al. (2023) Differential diagnosis with LLMs. https://arxiv.org/abs/2312.00164 (c18)
- [V] Groen and Patel (1985) Questionable assumptions. https://doi.org/10.1111/j.1365-2923.1985.tb01148.x (d02)
- [V] Review (2023) Cognitive perspectives on maintaining expertise II. https://pmc.ncbi.nlm.nih.gov/articles/PMC10366061 (d03)
- [V] Schmidt and Rikers (2007) Knowledge encapsulation and illness scripts. https://doi.org/10.1111/j.1365-2923.2007.02915.x (d04)
- [V] Lopez et al. (2026) Clinician input steers AI. https://arxiv.org/abs/2603.14158 (d05-d07)
- [V] Huang et al. (2024) LLMs cannot self-correct reasoning yet. https://arxiv.org/abs/2310.01798 (d13)
- [V] Zheng et al. (2024) LLMs are not robust multiple choice selectors. https://arxiv.org/abs/2309.03882 (d14)
- [V] Myrzakhan et al. (2024) Open-LLM-Leaderboard. https://arxiv.org/abs/2406.07545 (d15)
- [V] Qiu et al. (2025) MedR-Bench. https://arxiv.org/abs/2503.04691 (d16)
- [V] Li et al. (2026) Green Shielding. https://arxiv.org/abs/2604.24700 (d17)

## Source audit (2026-11-20)

Fresh auditors re-opened the sources of 10 established claims: 4 confirmed as written, 6 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **E01.02-K01** (now single-source: the sources are not independent). Both papers (1987 Patel/Arocha/Groen and 1991 Arocha/Patel) support the mixture finding but come from the same Patel-Arocha lab, so they count as one source.
- **E01.02-K07** (reworded: the sources support less). Numbers check out (Huang 75.8 to 38.1 after one round; MedEinst 43.46 to 60.50, Qwen3-32B only), but the human side is wider than the sources: Kaemmer shows a content-bearing checklist helps only when it contains the correct diagnosis (0.75 vs 0.49; wrong-list 0.43), and Pelaccia reports checklists and cognitive forcing generally did not reduce error; Lopez recovery is from an 'inexperienced clinician' framing of adversarial clinician context, not a general source-reliability cue. Corrected claim: Telling clinicians to be slow, reflective or take a second look does not improve diagnosis over being fast (Pelaccia 2025 review; Kaemmer 2021 generic prompt 0.53 vs 0.49 control, n.s.); a symptom-specific checklist helped only when it contained the correct diagnosis (0.75 vs 0.49), while checklists lacking it did not (0.43). In LLMs, generic self-review hurt (GPT-3.5 CommonSenseQA 75.8 to 38.1 after one round) and an explicit warning raised the MedEinst trap rate for Qwen3-32B (43.46 to 60.50), while an 'inexperienced clinician' framing recovered diagnostic inclusion lost to adversarial clinician context (Lopez 2026).
- **E01.02-K12** (reworded: the sources support less). Only MSDiagnosis supports a link (removing the primary diagnosis lowers final-diagnosis F1) and it calls error propagation a likely explanation, not a tested one; MedEinst has no passage on early-error propagation, so there is one source, and the first step is a primary diagnosis, not specifically a 'forward' answer. Corrected claim: In MSDiagnosis, removing the primary-diagnosis step significantly lowers final-diagnosis F1, which the authors attribute 'likely' to primary-diagnosis errors propagating through the multi-step process; this is a single-paper ablation, not a tested mechanism.
- **E01.02-K16** (reworded: the sources support less). Goh numbers (76 v 74; LLM alone 16 points higher) and the 2026 meta-analysis (OR 0.65, p=0.12) confirmed; but the UK replication (n=22 preprint, found only via search, not in the listed evidence) reported LLM access did help over conventional resources (73.7 v 66.3, p=0.001), so it does not simply agree. Corrected claim: In Goh et al. (JAMA Netw Open 2024) giving physicians an LLM did not significantly improve diagnostic reasoning (76% v 74%) while the LLM alone scored 16 points higher than the conventional-resources group (secondary analysis); a UK replication preprint (n=22) also found LLM alone above assisted physicians but, unlike Goh, a significant benefit of LLM access over conventional resources (73.7% v 66.3%); a 2026 meta-analysis found no significant LLM vs physician difference.
- **E01.02-K17** (reworded: the sources support less). This is an absence claim: the sources (PMC12813117 review, Sim and Chen survey, Dual-Inf abstract) do not mention Patel-Groen in LLMs but cannot show that no such study exists. Corrected claim: None of the sources checked (a clinical-reasoning AI review, a medical-LLM reasoning-behaviour survey, Dual-Inf) tests the Patel-Groen expert-forward/novice-backward claim in LLMs, and Dual-Inf uses forward and backward as method labels; a literature search found no direct test, but absence is not proven.
- **E01.02-K23** (reworded: the sources support less). Numbers confirmed in Huang et al. (Table 3; oracle labels help strongly in Table 2), but only that one paper (GPT-3.5/GPT-4, three benchmarks) supports it; the second listed source (MedEinst warning prompt) is not about self-review, so the general 'does not help LLMs' wording is wider than the evidence. Corrected claim: In Huang et al. (2024), intrinsic self-correction without external feedback did not help and often hurt GPT-3.5 and GPT-4 on GSM8K, CommonSenseQA and HotpotQA (GPT-3.5 CommonSenseQA 75.8 to 38.1 after one round; GPT-4 GSM8K 95.5 to 89.0 after two), whereas with oracle labels it helped strongly.
