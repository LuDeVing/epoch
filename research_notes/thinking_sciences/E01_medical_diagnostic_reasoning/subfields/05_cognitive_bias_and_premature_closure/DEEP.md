# Cognitive bias and premature closure: deep document

*Subfield E01.05. Scope: anchoring, early stopping, premature closure, mostly in diagnosis, plus every LLM or AI study found that tests or uses these ideas. Evidence ids (a01 ... d17) refer to evidence_a-d.jsonl in this folder. Claim ids (E01.05-K01 ...) refer to claims.jsonl. Several sources were read at abstract level only; the critique file lists them. Drops for LLMs under BiasMedQA are relative percent of baseline, not points, unless stated.*

## 1. What it is

Premature closure means accepting a diagnosis before it is fully verified. Anchoring means locking onto an early impression and adjusting too little as new data arrive. The two travel together: the first idea becomes the anchor, and the search for alternatives stops early. Croskerry (2003) put them in a catalogue of "cognitive dispositions to respond". Graber et al. (2005) gave the first large count of how often they appear in real diagnostic errors.

For our agent the subfield matters for one reason. It tells us which "think harder" or "check for bias" ideas are worth adding to the scaffold and which are not. The human literature is blunt. Most generic debiasing (be careful, learn bias names, use a checklist) did not work in controlled trials. A few structured moves worked in small studies. The LLM literature mostly tests something different: how far a model is pulled by a cue inserted into the prompt (suggestibility), not whether it stops its own search too early.

Scope limits to keep in mind (section 9 has more):
- Graber's data are 100 selected cases. "Premature closure is the top cognitive cause" is single-source.
- "Mostly missed common diseases" is only partly supported. Schiff 2009 lists common conditions among the most often missed (PE, ACS, stroke, colorectal, lung and breast cancer). Graber 2005 gives no condition counts. No study measures how often an LLM stops early on a common-disease case.
- Cognitive causes are only part of error. System factors are in 65% of cases. A thinking scaffold can reach only the reasoning part.

## 2. History and theories in depth

**1974, Tversky and Kahneman.** People adjust too little from a starting number, even a random one. The wheel-of-fortune version (anchor 10 gives a median guess of 25%; anchor 65 gives 45%) is from memory and was not opened (a13, M). Anchoring is robust in the lab. Its size varies with anchor type and expertise.

**1985, Voytovich et al.** Early clinical use of the term premature closure (a15, not opened).

**2003, Croskerry.** Founding catalogue. Lists many cognitive dispositions to respond (anchoring, premature closure, availability and others) and proposes metacognition and "cognitive debiasing" as the cure. It is an expert catalogue, not a tested predictive model (a10, abstract only).

**2005, Graber, Franklin, Gordon.** The quantitative base. 100 error cases from five academic centres. Cognitive factors in 74%, system factors in 65%. 5.9 factors per case. Premature closure the most common single named cognitive item (a01, a02, b01, b02).

**2008, Berner and Graber.** Review: physicians underestimate the chance their own diagnosis is wrong, which feeds early stopping (a11, b16; see the Calibration subfield).

**2009, Schiff et al.** 583 clinician-reported missed or delayed diagnoses. Gives the condition list that Graber lacks (a04).

**2010 to 2017, the Norman and Mamede school.** Controlled trials in residents. Availability bias can be induced (Mamede 2010) and structured reflection undoes it. Telling people to slow down does nothing (Norman 2014). Teaching bias names does nothing (Sherbino 2014). The real-world share of bias in errors is "not well established" (Norman 2017). This school argues errors come from both fast and slow thinking and that knowledge deficits matter. It is a rival camp to Croskerry's, whose school treats bias as the main cause and debiasing as the cure. Weigh each side's reviews with that in mind.

**2018, Lieder, Griffiths et al.** Resource-rational account: adjustment from an anchor stops when further steps cost more than they gain, so early stopping can be rational for a bounded thinker (a14, not opened, no numbers). This links to our G7 and G12: stopping is a budget decision, and the question is whether the stop rule uses a good signal.

**2018 to 2026, new human work.** Time pressure lowers accuracy partly by cutting the number of alternatives (b13, b14). Interruptions did not (b15, a failed test). In 2026 two randomised studies gave the first direct behavioural evidence: a salient misleading finding placed early cuts accuracy and processing time per word (b17), while eye tracking shows anchoring is a weighing and memory problem, not a looking problem (b18).

**2022 to 2026, LLM work.** It starts with transplants of human bias tests (Jones and Steinhardt 2022; Suri 2023; Itzhak 2023), then BiasMedQA (Schmidgall 2024), BiasBuster (Echterhoff 2024) and Lou and Sun (2024) on numeric anchors. Sequential diagnosis (Nori 2025, SDBench and MAI-DxO) is the first benchmark built explicitly around premature closure and anchoring. 2026 papers test AI anchoring on clinician input (Lopez 2026; Sheppert 2026) and human automation bias (Qazi 2025, 2026).

**Competing accounts in one table.**

| Account | Says | Support | Against |
|---|---|---|---|
| Fast-thinking bias (Croskerry) | Errors come from heuristic System 1; fix by slowing and debiasing | Biases can be induced (availability) | Slow instruction gave 44.5% vs 45.0% (a08); forcing and checklists null (b05, b11) |
| Knowledge deficit (Norman) | Errors come from missing or badly organised knowledge | Complexity and experience dwarf instruction effects (b10) | Graber coded knowledge or skill deficits as only 11 of 320 cognitive instances (a02) |
| System and context | Handoffs, load and time cause errors | System factors in 65% (a01); time limit lowers accuracy (b13, b14) | Interruptions showed no cost (b15) |
| Resource-rational stopping | Early stop is a rational budget choice | Time limit cuts alternatives (b13) | Not tested clinically (a14) |

## 3. Core findings with exact numbers

Status key: Est = established (two or more independent sources, or replicated); Single = single source; Contested = sources disagree; Prelim = preprint or abstract only.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Cognitive and system factors in diagnostic error | 100 cases kept from 129. 90 with injury, 33 deaths. Cognitive 74%, system 65%, cognitive-only 28%, system-only 19%, both 46%, no-fault only 7%. 548 factors in 93 cases, 5.9 per case (320 cognitive, 228 system). 38 wrong, 34 missed, 28 delayed. Origin: QA 57, voluntary 33, autopsy 10 | Graber 2005 (a01, b01) | Single |
| Inside cognitive errors | Faulty synthesis about 264 of 320 (about 83%). Faulty data gathering 45. Premature closure 39 (about 12%, counted inside synthesis). Knowledge or skill 11 (4 and 7, about 3%) | Graber 2005 (a02, b02) | Single |
| Which diseases are missed | 583 kept of 669. Severity 162 major, 241 moderate, 180 minor. PE 26 (4.5%), drug reaction 26 (4.5%), lung cancer 23 (3.9%), colorectal 19 (3.3%), ACS 18 (3.1%), breast 18 (3.1%), stroke 15 (2.6%). Testing phase 44%, clinician assessment 32% | Schiff 2009 (a04) | Single |
| Outpatient error rate | 5.08% of US adult outpatients per year, about 12 million, about half possibly harmful | Singh 2014 (a05) | Single |
| Be fast vs be careful instruction | n=96 and n=108 second-year residents, 20 cases. Accuracy 44.5% vs 45.0%. Time 69 s vs 89 s. Wrong cases took 17 s longer | Norman et al. 2014 (a08, b09) | Est |
| First-impression vs directed-search instruction | 393 clinicians. Instruction F(1,379)=2.44, p=.12. Complexity F=965.2, experience F=39.6 | Ilgen 2013 (b10) | Est |
| Cognitive forcing training in students | 191 students (145 trained, 46 control). Second diagnosis sought 52% vs 48% (p=.91). Correct second diagnosis 54% vs 48% (p=.13). Over-identified false positives 64% vs 77% (p=.12). Availability cases 45% vs 45% (p=.98) | Sherbino 2014 (b05) | Est |
| Debiasing vs knowledge checklist on ECGs | 61 participants (40 PGY1, 21 fellows), 3 arms, 20 ECGs. Bias cases caused more errors (F=96.9). No checklist effect | b11 (2020) | Est |
| Differential checklist, real patients | 14 physicians, 100 patients, 17 errors. Error 11.2% vs 17.8% (p=.46). Diagnoses considered 6.5 vs 3.4 (p<.001). Post hoc emergency doctors 19.1% vs 45.0% (p=.04) | b12 (pilot) | Contested |
| Availability bias induced, then reflection | 36 residents. PGY2 1.55 on similar vs 2.19 on other cases (p=.03, max 4). PGY1 opposite, 2.03 vs 1.42 (p=.046). PGY2 gave the earlier diagnosis 1.44 vs 0.72 times (p=.04). Reflection: PGY2 2.03, PGY1 2.31 (p=.006) | Mamede 2010 (a07, b06) | Single |
| Reflection helps only complex cases | 42 residents, 16 cases. Interaction F(1,41)=4.48, p<.05; no main effect | Mamede 2008 (a06) | Single |
| Self-directed second look | 47 residents, 16 cases. 8% revised. Score 1.20 to 1.22 of 2 (t=2.15, p=.03). Revised at least one: 12/19 PGY1, 9/11 PGY2, 8/17 PGY3 | Monteiro 2015 (b08) | Single |
| Systematic review, interventions | 28 studies. Guided reflection most consistently successful (5 studies). No pooled effect | Lambe 2016 (b07) | Contested |
| Systematic review, bias and accuracy | 20 studies, 6,810 physicians, 19 biases. Bias linked to inaccuracy in 36.5 to 77% of scenarios. Only 2 of 20 studied patient outcomes. 12 of 20 low quality | Saposnik 2016 (b04) | Single |
| Time limit | 75 residents, 8 cases. Time 85.5 s vs 181.8 s. Accuracy 0.44 vs 0.53 (p=.01). Alternatives 0.37 vs 0.51 (p=.01). Pressure to alternatives beta=-0.32; pressure to stress beta=0.25 | b13 (2018) | Est (with b14) |
| Actual limit vs felt pressure | Limit lowered accuracy (p=.044); felt pressure did not | b14 (2025) | Est (borderline) |
| Interruptions | Exp1 N=42 0.88 vs 0.91. Exp2 N=78 0.95 vs 0.94. Exp3 N=30 0.42 vs 0.37. No accuracy cost | b15 (2022) | Single (null) |
| Misleading finding placed early | 58 fourth-year students, 12 vignettes. Accuracy 0.27 none, 0.11 early (61% drop, F(2,693)=11.995), 0.17 late (36% drop). Time per word fell only for early (F(2,636)=4.799) | b17 (2026) | Single |
| Eye tracking of anchoring | Recall of key findings 0.47 (accurate) vs 0.20 (distractor-led). Recall of distractors 0.16 vs 0.37. Fixation counts equal | b18 (2026) | Single |
| LLM suggestibility to a bias cue (BiasMedQA) | 1,273 USMLE items, 6 models. No-bias accuracy GPT-4 72.7%, Mixtral 51.8%, GPT-3.5 49.7%, PMC-Llama-13B 33.4%. GPT-4 false consensus 0.727 to 0.625 (-10.2 points, -14.0% relative). GPT-3.5 0.497 to 0.239. PaLM-2 0.357 to 0.139. Mean relative drops over models: false consensus 24.9%, frequency 18.2%, recency 12.9%, confirmation 8.1% | Schmidgall 2024 (a18, b19, c01, c03) | Single |
| Awareness or few-shot prompts in LLMs | GPT-4 frequency 0.627 to 0.720 with education; recency 0.679 to 0.742 one-shot. Other models marginal. None restored baseline | Schmidgall 2024 (b20, c02) | Est |
| Numeric anchoring in LLMs | 62 questions plus 8 irrelevant-hint controls. GPT-4 anchoring index about 0.45 vs 0.61 in the human source. CoT, ignore-the-anchor, principles, reflection did not remove it. Two opposed anchors fixed 8 of 15 expert-hint questions | Lou and Sun 2024 (a17, c06) | Est |
| ChatGPT vs humans on anchoring | 30 queries per cell. Low anchor 20.83 (ChatGPT) vs 22.5 (humans). High anchor 105.97 vs 80.50. The model said it would not show anchoring | Suri 2023 (c08) | Single |
| Anchors in code | Irrelevant preceding code cut Codex accuracy by 22.3 to 30.5 points; irrelevant line copied 81% vs 4.5% on clean prompts | Jones and Steinhardt 2022 (c07) | Single |
| Instruction tuning raises some biases | Decoy, certainty, belief bias up in Flan-T5, Mistral-Instruct, GPT-3.5, GPT-4 vs base | Itzhak 2023 (c09) | Single |
| 30 biases, 20 LLMs | 30,000 tests; evidence of all 30 in some models; the smallest model looked unbiased only because it failed to decide in 33% | Malberg 2024 (c10) | Single |
| Admissions decisions (BiasBuster) | 13,465 prompts. GPT-4 admitted 40.5% more under reject framing. Primacy for options A or B. Status quo mostly reversed | Echterhoff 2024 (a16, c04) | Single |
| Piecewise task reveal (non-medical) | 39% average drop FULL to SHARDED. CONCAT kept 95.1% of FULL. First attempt in first 20% of turns 30.9 vs 64.4 in last 20% | Laban 2025 (c11, c12) | Single |
| SDBench | 304 NEJM cases. Physicians (21, median 12 years) 19.9% at $2,963. o3 78.6% at $7,850. MAI-DxO 81.9% at $4,735; 79.9% at $2,397 budgeted; 85.5% at $7,184 ensembled. Single vs batched mode 83.9% both, $3,991 vs $5,084 | Nori 2025 (a19, c13, c14, d02 to d04) | Single |
| Multi-agent roles on wrong-first cases | 16 cases x 5 repeats. Initial diagnosis 0% (0/80). Final top-2 64% (51/80), 69% (55/80), 76% (61/80; OR 3.49 vs humans, P=.002). Humans 27% (13/48) to 48% (23/48) | Ke 2024 (c17) | Single |
| LLMs anchor on a planted diagnosis more than clinicians | Anchor ranked first: LLMs 40/72 (55.6%), residents 17/80 (21.2%, N=20), attendings 2/20 (10.0%, N=5). OR 3.94 vs residents (2.32 to 7.33), 4.07 vs attendings. Anchor in top 5: 97.2% vs 67.5% vs 65.0% | Sheppert 2026 (d01) | Single, abstract only |
| Self-review without oracle lowers accuracy | GPT-3.5 CommonSenseQA 75.8 to 38.1; GPT-4 GSM8K 95.5 to 89.0 over two rounds | Huang 2024 (d05) | Est |
| Susceptibility to a wrong challenge | Baseline accuracy 38.1% to 68.0%. GPT-4o complies 100.0% (wrong) and 97.0% (right). Llama-3.3-70B 100.0% and 99.6%. Qwen3-80B-Thinking corrigibility 11.9%, susceptibility 6.6%. GPT-5 variants about 5.6 to 7.3% susceptibility | Lopez 2026 (d10) | Single, preprint |
| Clinician context steers LLMs | 61 NEJM cases, 21 variants of 8 models. Expert context +20.4 points inclusion (all 21 up). Adversarial -5.4 (14 of 21 significant). GPT-5 75.5% to 65.1% under adversarial. A "clinician is unsure" line recovered most | Lopez 2026 (d09, d11) | Single, preprint |
| Humans and AI advice | GPT-4 access 76% vs 74% (50 physicians, P=.60). Planted wrong advice: reasoning 84.9% vs 73.3%, -14.0 points (-19.7 to -8.3). Nudge: +7.6 points (1.4 to 13.9). Top choice 79.5 vs 69.1 | Goh 2024 (c20); Qazi 2025, 2026 (b21, b22) | Est in direction; preprints |
| Order of information in a loop | 2,400 MIMIC-IV cases, 4 abdominal diseases. Order changed accuracy by up to 18.0 points (Llama 2 Chat, pancreatitis). Doctors 16 to 25 points above the models | Hager 2024 (c23) | Single |
| Conversation lowers accuracy | GPT-4 0.919 to 0.854; GPT-3.5 0.833 to 0.724. Summary restored GPT-3.5 to 0.810 (GPT-4 0.854 to 0.856, ns) | CRAFT-MD (d07) | Single |
| Free-turn questioning | 1,453 case reports. Recall of needed exams R1 43.61 to 40.67; o3-mini 38.47 to 38.22. Diagnosis R1 71.79 to 76.18. Rare vs common comparable | MedR-Bench (d08) | Single |

## 4. Mechanisms and models

Each mechanism is written so an engineer can reproduce it as a test or a code rule.

**4.1 The failure chain in humans.** Evidence supports this order: (1) an early salient finding enters; (2) the thinker generates few alternatives; (3) later findings are weighed against the leader and not against each other; (4) search ends. Support for each link:
- Link 2: time-limited residents considered 0.37 vs 0.51 alternatives and scored 0.44 vs 0.53 (b13).
- Link 3: in eye tracking, fixations on key findings were equal for right and wrong residents, but right ones recalled 0.47 of key findings vs 0.20 (b18). The data were seen but not weighted. Recall is post hoc and may reflect the final answer.
- Link 4: a misleading finding early cut time per word as well as accuracy; late placement cut accuracy less with no time change (b17). Early placement looks like a closure trigger, late placement like interference.

Engineering form: keep a table with rows = findings, columns = rival diagnoses, cell = supports / contradicts / neutral. Anchoring is the pattern where rival columns are filled in less than the leader column. Premature closure is a stop with an empty or unchecked rival column.

**4.2 Why a stop rule must not use stated confidence.** Overconfidence (a11) means physicians' certainty overstates correctness. The same holds for models (Calibration subfield). Lou and Sun report that stronger models are more consistently anchored, and Suri found ChatGPT denied bias while showing it (c08). A stop rule needs an external signal. Candidates: rival-set size, open-test list count, disagreement between independent samples, whether a discriminating check has been run. None has been compared head to head.

**4.3 Resource-rational stopping (Lieder).** Treat each extra step as costing tokens and gaining expected accuracy. Stop when the marginal gain falls below the cost. The model predicts early stops under tight budgets, which matches b13. Implementation: a budget governor in code that tracks tokens used, rival-set size and the last step's information gain, and forces a minimum rival set before closure under a low budget. Not tested clinically (a14).

**4.4 Structured reanalysis (Mamede).** The protocol that worked: after a first quick diagnosis, the doctor lists the findings for and against, says what each supports, then re-derives the diagnosis (b06). Features: structured, experimenter-controlled, tied to specific findings, done after bias was induced. Generic "reconsider" (Monteiro, b08) gained 0.02 of 2. In Mamede 2010 no control group redid the cases without reflection, so part of the gain may be a plain second look.

**4.5 Challenger role (MAI-DxO).** One model plays five roles: hypothesis tracker (keeps the differential), test chooser, challenger (argues against the leader), stewardship (cost), checklist. In the authors' inspection of disagreements, baseline o3 fixated on an early impression and the panel sought disconfirming evidence (c14). Worked example: a hand-sanitizer case. Baseline o3 fixated on antibiotic toxicity, was wrong and spent $3,431. The panel asked about ingestion in round one, was right and spent $795 (d03). No role ablation exists (d02, d03). Ensembling independent panels beat one panel by 3.6 points (85.5% vs 81.9%), so part of the gain may be sampling, not the challenger.

**4.6 Context contamination in LLMs.** Early or wrong content in the context acts as an anchor. Evidence: wrong hints (Lou and Sun), a wrong anchor function (Jones and Steinhardt), a planted diagnosis (Sheppert), a clinician differential (Lopez), the model's own early answer (Laban). Laban's chain: the model answers early on partial information, then relies on that answer; CONCAT shows the information was enough. Engineering fix: restate all facts in a fresh context before answering, and keep earlier verdicts out of the new prompt.

**4.7 Order effects.** Hager found order of exam, labs and imaging changes accuracy by up to 18.0 points in open Llama-2-family models. BiasBuster found primacy for options A and B. Fix: a canonical order set by code.

**4.8 Conformity to a challenge.** Lopez 2026 splits a model's reaction to a challenge into corrigibility (switch to a correct challenge when wrong) and susceptibility (switch to a wrong challenge when right). Conformist models do both near 100%; dogmatic ones do neither. Any challenger or recheck step must be judged on both rates, not only on rescued errors.

## 5. What holds up

**Replicated or consistent across sources**
- Generic exhortation does not raise diagnostic accuracy: Norman 2014 (44.5% vs 45.0%) and Ilgen 2013 (p=.12), two independent designs. Established.
- Teaching bias names, forcing strategies and debiasing checklists: null in Sherbino 2014 (191 students), the ECG trial (61 participants), and the real-patient pilot (not significant). Norman 2017 draws the same conclusion in a narrative review. Established for novices on vignettes.
- Time limits cost accuracy and cut alternatives: b13 and b14 partly agree.
- LLMs lose accuracy when a bias cue is added, and awareness prompts give small gains: Schmidgall, Echterhoff, Lou and Sun, Jones and Steinhardt and Suri all point the same way.
- Unguided self-review lowers LLM accuracy (Huang 2024); Lopez 2026 shows the same flip risk in a clinical challenge.
- Self-consistency is at least as good as debate at equal responses (Huang 2024). This fits ensembling beating one panel in SDBench.
- Humans do not gain from good AI and over-trust wrong AI: Goh 2024 (no gain), Qazi 2025 (-14.0 points).

**Failed or weak**
- Interruptions: three experiments, no accuracy cost (b15). Small N and ceilings limit the conclusion.
- Cognitive forcing: Lambe 2016 says it improved accuracy and confidence judgements. Sherbino 2014 and the ECG trial say null. The review is narrative and trainee-heavy. Contested.
- Differential checklists: more hypotheses (6.5 vs 3.4) without a significant error cut (11.2% vs 17.8%, p=.46). Hypothesis count is not the success measure.
- Writing a differential does not help LLMs: GPT-4 78% vs CoT 76% (n.s.), GPT-3.5 46% to 38% (c19). Older models.
- Few-shot bias examples broke output format in BiasBuster (c05).
- Mamede 2010's PGY1 pattern reversed (2.03 vs 1.42): the induced effect appeared only in PGY2.

**Moderators**
- Case complexity: reflection helps complex cases, not simple ones (a06).
- Experience: complexity and experience dwarf instruction (b10).
- Model strength: stronger models lose less to inserted cues (GPT-4 vs PaLM-2) but Lou and Sun report stronger models are more consistently anchored by numeric hints. Different bias types; not yet a real contradiction.
- Model type: instruction tuning raised decoy, certainty and belief bias (c09). Inference-time scaling cut harmful echoing in Lopez 2026 (d09; about 57 to 63% by the recorded figures).
- Who supplies the hint: "clinician is unsure" recovered most adversarial loss (d11); expert context helped all 21 variants (+20.4 points).

**What worked**
- Structured, finding-by-finding reanalysis (Mamede 2010, single source).
- Two opposed anchors for numeric estimates (8 of 15 questions, those where the hints bracketed the truth).
- Consolidating facts before answering (Laban CONCAT 95.1% vs about 61%; CRAFT-MD summary 0.724 to 0.810 for GPT-3.5, GPT-4 unchanged).
- A disagreement-signal nudge for humans using AI (+7.6 points, CI lower bound 1.4).
- Independent ensembles (85.5% vs 81.9%).
- Challenger plus facilitator roles on wrong-first cases (0% to 64-76% top-2), with the selection caveat in section 9.

**What did not work**
- "Be careful", "be fast", bias lists, generic second looks, writing a differential, uniform self-review, few-shot bias examples (format loss), CoT and ignore-the-anchor for numeric anchors.

## 6. Language models

**6.1 What the studies actually test.** Three kinds:
1. *Suggestibility to an inserted cue* (BiasMedQA, BiasBuster, Lou and Sun, Jones and Steinhardt, Suri, Sheppert, Lopez). Measures the pull of a stated hint.
2. *Early commitment inside a loop* (Laban, SDBench, Hager, CRAFT-MD, MedR-Bench). Measures the effect of the model's own earlier output or of ordering.
3. *Human use of AI* (Goh, Qazi, McDuff, Everett). Measures human anchoring on the machine.

Only type 2 touches premature closure, and only SDBench is medical and built for it. Laban is non-medical. No study measures an LLM early-stop rate on common diseases (K22).

**6.2 Suggestibility numbers.**
- BiasMedQA, 1,273 items, 6 models: every model lost accuracy. Relative drops of 10 to 26% depending on model. Averages over models: false consensus 24.9%, frequency 18.2%, recency 12.9%, confirmation 8.1%. GPT-4 was most robust. Correction: these are relative percentages of baseline, not points (GPT-4 false consensus is -10.2 points, -14.0% relative).
- A bias-awareness paragraph, one-shot or few-shot gave modest, model-dependent gains. GPT-4 frequency 0.627 to 0.720; recency 0.679 to 0.742. None reached the no-bias level. A 2025 medRxiv follow-up titled "LLM Reasoning Does Not Protect Against Clinical Cognitive Biases" (Llama-3.3-70B, Qwen3-32B) was not opened (d16).
- Numeric anchors (62 questions): GPT-3.5, GPT-4 and GPT-4o were all pulled. GPT-4 index about 0.45 vs 0.61 in humans. CoT, ignore-the-anchor, principles and reflection did not remove it. Both-anchor worked on 8 of 15 expert-hint questions.
- Planted diagnosis: LLMs ranked the anchor first 55.6% vs residents 21.2% vs attendings 10.0% (abstract only; models not named there). Anchor in the top five 97.2%.
- Clinician context: expert +20.4 points, adversarial -5.4 points; an explicit "clinician is unsure" line recovered most of it. Claude Sonnet 4.5 70.5% to 67.3%; Gemini 3 Flash 76.6% to 73.7%; GPT-5 75.5% to 65.1%.
- Challenge compliance: GPT-4o 100.0% / 97.0%, Llama-3.3-70B 100.0% / 99.6%, Qwen3-80B-Instruct 93.5% / 74.6% (wrong / right challenge). Dogmatic reasoning variants: 6.6% susceptibility.

**6.3 Early commitment numbers.**
- Laban: FULL to SHARDED -39% on average. CONCAT 95.1%. Early first attempt 30.9 vs late 64.4. Reasoning models degrade too.
- SDBench: o3 78.6% at $7,850; MAI-DxO 81.9% at $4,735 (cost down about 40%), 79.9% at $2,397, ensembled 85.5% at $7,184. The anchoring story rests on inspection of disagreements. The Instant Answer arm figure was not recovered (c15).
- Hager: order alone swung accuracy by up to 18.0 points; instruction-following errors every two to four patients.
- CRAFT-MD: conversation lowers accuracy (GPT-4 0.919 to 0.854). Summarising the conversation into one vignette restored GPT-3.5.
- MedR-Bench: free turns did not raise needed-exam recall (R1 43.61 to 40.67); models looped.

**6.4 What changed behaviour, by how much.**

| Change | Effect | Source |
|---|---|---|
| Stronger model | Smaller loss to an inserted cue (GPT-4 -14.0% relative vs PaLM-2 about -61% from 0.357 to 0.139) but not immune | Schmidgall |
| Awareness prompt | Small gain in GPT-4, marginal in others | Schmidgall, Echterhoff |
| CoT, reflection, ignore-the-anchor | No removal of numeric anchoring | Lou and Sun |
| Two opposed anchors | Near bias-free on 8 of 15 | Lou and Sun |
| "Clinician is unsure" | Recovered most of the -5.4 adversarial loss | Lopez |
| Inference-time scaling | Cut harmful echoing by about 57 to 63% | Lopez |
| Consolidate facts | 95.1% vs about 61% of FULL (non-medical); GPT-3.5 0.724 to 0.810 | Laban; CRAFT-MD |
| Challenger panel | 78.6% to 81.9%, cost down | Nori |
| Independent ensemble | 81.9% to 85.5% | Nori |
| Challenger roles on wrong-first cases | 0% to 64-76% top-2 | Ke |
| Unguided self-review | Lowers accuracy | Huang |

**6.5 Limits of the LLM evidence.** BiasMedQA is multiple choice with a sentence inserted. MAI-DxO uses hard NEJM cases, not benign common ones; the authors are the vendor; there is no independent replication. Ke 2024 cases were selected because the first answer was wrong, so part of the improvement is regression to the mean. Lopez and Qazi are preprints with synthetic or planted content. Older models (GPT-3.5 and GPT-4 of 2023) dominate the prompt-fix evidence.

## 7. What our agent should take

Status: [E] established, [S] single-source, [C] contested. Schema parts: G guardrail, S state, O operator, memory.

### Add now (established)

1. **Do not add "be careful", "slow down", "avoid bias" lines or a bias checklist.** Memory (4b). [E] a08, b09, b10, b05, b11, a09, b03; for LLMs b20, c02, c05, c06. Already in 4b; add the new LLM sources there.
2. **Treat any hint, suggested answer or earlier verdict as a claim, not evidence.** Code-level input hygiene in S1; hidden from later passes (G5). [E] a17, c06, c07, d01, d09, b21, c20. Tagging the hint's source and confidence (d11) is [S].
3. **No unguided self-review pass.** A recheck must cite a failing output located by code (G2, G1). [E] d05, d10, b08. New support: measured flip-to-wrong rates (GPT-3.5 75.8 to 38.1; susceptibility up to 100% in conformist models).
4. **No debate or persona panel without an equal-token control (G9, 4b).** [E] d06, d04. Ensembling beat one panel by 3.6 points, so extra samples explain part of the panel effect.
5. **Gate any recheck by difficulty or by a disagreement signal, not on all items (G12).** [E] a06 (F(1,41)=4.48), b22, b27 (always-on friction poorly tolerated; discussion claim).
6. **Give any budget limit a minimum rival set (G1 / budget).** [E] b13, b14 for the cost of fewer alternatives. The minimum-rivals rule itself is [S] until tested.
7. **Fix the order of findings in code (S1).** [E] c23 (up to 18.0 points), c04 (primacy). Open models only.
8. **Consolidate before closure.** Restate all gathered facts in a fresh context, hide earlier verdicts (S3, S1). [E] c11, d07, d08 (K28). Two of the three are non-medical or multiple choice.

### Test first

1. **Closure check in code (O, S4/S7).** Closure allowed only if every listed rival has had a discriminating check run or was eliminated by cited output. [S] a02, c14. UNKNOWNS U1.
2. **Structured finding-by-rival reanalysis vs fresh re-derivation (S3 / recheck).** [S] a07, b06, c11; [C] b07. U2.
3. **Challenger step gated on a signal, with flip-to-wrong measured on first-correct answers (O).** [S] c14, c17; risk [E] d05, d10. U3.
4. **Two opposed leads in context instead of one (O rival generation).** [S] for LLM diagnosis; [E] for numeric estimates (c06). U4.
5. **Open-test list that blocks closure while a key test is pending (stop rule).** [S] a04 (testing phase 44%). U5.
6. **Early-distractor reorder (S1/S3).** [S] b17, c23. U6.
7. **Per-finding by per-rival scoring in code (O).** [S] b18. U7.
8. **Stop signal choice: rival-set size, sample disagreement, open-test count.** No comparison exists. U8.
9. **Hint-source tagging.** [S] d11, d09. U9.

## 8. Concrete tests on our bench

All arms at equal tokens, same items, same seed pool. Expected effects are priors, not results.

| Test | Item type | Arms | Metric | Expected |
|---|---|---|---|---|
| T1 exhortation null | Closure-prone vignettes (benign-looking lead; PE, ACS, stroke) | Plain vs plain + "be slow and thorough" | Top-1 accuracy | No gain (replicates a08) |
| T2 bias-name checklist | Same, plus a BiasMedQA subset | Plain vs awareness paragraph | Accuracy | 0 to +3 points on a mid-size model |
| T3 closure check | Staged cases with a benign lead | Plain vs code-enforced rival-checked closure | Accuracy; early-stop rate (answer before any discriminating check) | Early stops fall; accuracy up 3 to 8 points |
| T4 reanalysis | Cases with a planted prior similar case in context | (a) none, (b) same-context reconsider, (c) structured finding-by-rival, (d) fresh-context re-derivation | Accuracy; share of earlier answer repeated | (c) and (d) beat (a) and (b); (d) at least (c) |
| T5 challenger flip rate | Half first-answer-correct, half wrong | No challenger vs gated challenger vs always-on | Net accuracy; flip-to-wrong rate on correct cases | Gated wins; always-on flips 5 to 15% of correct |
| T6 two leads | Cases with a wrong suggested diagnosis | One lead vs two opposed vs none | Rate the suggested wrong answer is ranked first | Two leads lower the rate |
| T7 hint tagging | Wrong and right hints | Untagged vs source-and-confidence tagged | Accuracy with wrong hint; gain with right hint | Wrong-hint loss falls, right-hint gain kept |
| T8 order | SDBench-style loop | Free vs code-canonical order; early vs late distractor | Accuracy spread; drop from early distractor | Canonical order narrows spread |
| T9 consolidation | Staged information cases | Continue thread vs restate-all-findings block | Accuracy | Gain, larger for weaker models |
| T10 open-test list | Cases with a pending key test | No list vs blocking list | Premature-answer rate | Falls |
| T11 stop signals | Closure-prone set | Stop by confidence vs rival-set size vs sample disagreement vs open-test count | AUC for predicting a wrong early stop | Confidence worst |
| T12 budget rival rule | Low-token arm | Plain vs minimum-rivals rule | Accuracy at low budget | Recovers part of the 0.09 loss seen in humans |

Include an Instant Answer arm in T3 and T8 as a premature-closure control. Report cost per correct case, not only accuracy, as SDBench does.

## 9. What does not transfer, and why

- **Hindsight-coded error counts.** Graber's 12% share rests on 100 selected cases, consensus coding and no interrater figure. Reliability figures from other record-review studies (ICC 0.52 to 0.72, and 0.37; snippets, d15) show such coding is only moderately reliable. Do not use 12% as a rate for LLM behaviour.
- **System factors.** 65% of cases had system factors, including missing tests and handoffs. Our agent has no handoff problem and cannot fix a test it cannot order.
- **Human debiasing training.** Teaching bias names relies on memory and habit across days. An LLM has neither. The null human results transfer as "do not add", not as "LLMs are not biased".
- **Cognitive forcing in humans.** Trials were on trainees with written vignettes and accuracy near floor (45%, 27%). A null there says little about an agent that can run code.
- **Suggestibility studies.** BiasMedQA and BiasBuster insert a sentence. They measure pull, not self-generated closure.
- **Ke 2024.** Wrong-first selection means the 0% start is built in. It shows nothing about harm on right-first answers.
- **MAI-DxO anchoring.** Seen in inspection of disagreements by the vendor; one worked example; no role ablation.
- **Laban.** Code, SQL, maths and summaries with a simulated user. The mechanism may be general but is not shown in diagnosis.
- **Persona panels.** MAI-DxO roles are not voters, so they do not break G4 by themselves, but a role panel used as voters or debaters would (G9).
- **Eye tracking and recall.** Human attention data do not map onto a transformer's context. Only the "weighing, not looking" lesson transfers.
- **Time-pressure stress path.** The stress mediator (beta 0.25) has no LLM analogue; the rival-count path may.
- **Reflection.** Reflection time on a specific finding set is not the same as extra tokens. At equal tokens a fresh sample may match it (d04, d06).

## 10. Open questions

1. Does an LLM stop investigating too early on common-disease cases, and at what rate? No published figure. SDBench Instant Answer accuracy is figure-only and was not recovered.
2. Which part of MAI-DxO carries the gain (challenger, tracker, stewardship, checklist)? The paper has no role ablation; its only ablation is single vs batched mode (83.9% both).
3. Does a diagnosis-specific challenger flip correct first answers, and how often? Huang 2024 and Lopez 2026 give general and challenge-based rates only.
4. Does structured reanalysis beat generic reconsideration, and does fresh-context re-derivation beat same-context reconsideration, at equal tokens?
5. Does the early-distractor effect (b17) replicate in experienced physicians or in LLMs?
6. Which stop signal best predicts wrong early stops? No head-to-head.
7. Newer audits of the premature-closure share with interrater agreement: none found.
8. What did the Goh UK replication find? Not located. Everett 2026 (52% vs 24% full overlap when the AI sees the physician first) is from a secondary summary only.
9. Sheppert 2026: which eight LLMs, which prompts, and what is the effect with reasoning models? Only the abstract was read.
10. Do the 2025 findings that reasoning does not protect against clinical biases (d16) hold for 2026 models? Not opened.
11. Does the Mamede 2010 effect survive a control group that redoes the cases without reflection?
12. Do hint-source tags generalise beyond the three models in Lopez 2026?

## 11. Sources

[V] = opened this session (some at abstract level only, per the evidence lines and critique). [M] = snippet or title only.

**Human studies and reviews**
- [V] Graber, Franklin, Gordon 2005, Diagnostic error in internal medicine. https://jamanetwork.com/journals/jamainternalmedicine/fullarticle/486642 ; https://pubmed.ncbi.nlm.nih.gov/16009864/ (a01 to a03, b01, b02)
- [V] Schiff et al. 2009, 583 physician-reported errors. https://europepmc.org/article/MED/19901140 (a04; abstract only)
- [V] Singh, Meyer, Thomas 2014, outpatient error frequency. https://europepmc.org/article/MED/24742777 (a05; abstract only)
- [V] Mamede et al. 2008, reflective practice. https://europepmc.org/article/MED/18412886 (a06; abstract only)
- [V] Mamede et al. 2010, availability bias and reflection. https://pubmed.ncbi.nlm.nih.gov/20841533/ (a07, b06)
- [V] Norman et al. 2014, etiology of diagnostic errors. https://pubmed.ncbi.nlm.nih.gov/24362377/ (a08, b09; author order to verify)
- [V] Norman et al. 2017, causes of errors. https://pubmed.ncbi.nlm.nih.gov/27782919/ (a09, b03)
- [V] Croskerry 2003. https://europepmc.org/article/MED/12915363 (a10; abstract only)
- [V] Berner and Graber 2008. https://pubmed.ncbi.nlm.nih.gov/18440350/ (a11, b16)
- [V] Gupta et al. 2018, Mind the overlap. https://pmc.ncbi.nlm.nih.gov/articles/PMC6743477 (a12)
- [M] Tversky and Kahneman 1974. https://www.science.org/doi/10.1126/science.185.4157.1124 (a13)
- [M] Lieder et al. 2018. https://doi.org/10.3758/s13423-017-1286-8 (a14)
- [M] Voytovich et al. 1985. https://pubmed.ncbi.nlm.nih.gov/3981403/ (a15)
- [V] Redelmeier and Shafir 1995. https://europepmc.org/article/MED/7815657 (a22)
- [V] Saposnik et al. 2016. https://pubmed.ncbi.nlm.nih.gov/27809908/ (b04)
- [V] Sherbino et al. 2014. https://pubmed.ncbi.nlm.nih.gov/24423999/ (b05)
- [V] Lambe et al. 2016. https://pubmed.ncbi.nlm.nih.gov/26873253/ (b07)
- [V] Monteiro et al. 2015. https://pubmed.ncbi.nlm.nih.gov/26173528/ (b08)
- [V] Ilgen et al. 2013. https://pubmed.ncbi.nlm.nih.gov/23969355/ (b10)
- [V] Debiasing vs knowledge checklists on ECGs, 2020. https://pubmed.ncbi.nlm.nih.gov/30694452/ (b11)
- [V] Checklist pilot RCT, 2018. https://pubmed.ncbi.nlm.nih.gov/29540029/ (b12)
- [V] Time pressure, 2018. https://pubmed.ncbi.nlm.nih.gov/30302783/ (b13)
- [V] Time pressure, written cases, 2025. https://pubmed.ncbi.nlm.nih.gov/39601678/ (b14)
- [V] Interruptions, three experiments, 2022. https://pubmed.ncbi.nlm.nih.gov/35296302/ (b15)
- [V] Premature closure underlies bias in students, 2026. https://pubmed.ncbi.nlm.nih.gov/42051011/ (b17)
- [V] Cognitive mechanisms of anchoring in diagnosis, 2026. https://pubmed.ncbi.nlm.nih.gov/42126939/ (b18)
- [V] Goh et al. 2025, bias assessment. https://pubmed.ncbi.nlm.nih.gov/40038550/ (b23)
- [V] Goh et al. 2024, JAMA Netw Open RCT. https://pmc.ncbi.nlm.nih.gov/articles/PMC11519755/ (c20)
- [M] Goh UK replication 2026. https://doi.org/10.1515/dx-2025-0176 (c21, d14)
- [V] Qazi et al. 2025, automation bias. https://www.medrxiv.org/content/10.1101/2025.08.23.25334280 (b21, b26)
- [V] Qazi et al. 2026, nudge. https://www.medrxiv.org/content/10.64898/2026.06.01.26354596 (b22, b27)
- [V] McDuff et al. 2025, AMIE differential. https://pmc.ncbi.nlm.nih.gov/articles/PMC12158753/ (c22)
- [V] Sheppert et al. 2026, LLM anchoring vs physicians (Crossref abstract). https://doi.org/10.1016/j.ijmedinf.2026.106550 (d01); SSRN version [M] https://doi.org/10.2139/ssrn.6187954 (b24)
- [M] Dialogical AI for bias mitigation, 2026. https://www.mdpi.com/2076-3417/16/2/710 (b25)
- [M] Everett et al. 2026. https://doi.org/10.1038/s41746-026-02545-1 (d12)
- [M] Bousquet and Beltramin 2025 letter. https://www.jmir.org/2025/1/e69742 (d13)
- [M] Ke 2025 letter pointer. https://pmc.ncbi.nlm.nih.gov/articles/PMC11615553/ (c18)
- [M] Reliability of error coding, snippets. https://ajemjournal.com/article/S0735-6757(16)00183-2/pdf (d15)

**LLM and AI studies**
- [V] Echterhoff et al. 2024, BiasBuster. https://arxiv.org/abs/2403.00811 (a16, a23, c04, c05)
- [V] Lou and Sun 2024, anchoring in LLMs. https://arxiv.org/abs/2412.06593 (a17, c06)
- [V] Schmidgall et al. 2024, BiasMedQA. https://arxiv.org/abs/2402.08113 ; https://pmc.ncbi.nlm.nih.gov/articles/PMC11494053/ (a18, b19, b20, c01 to c03)
- [V] Nori et al. 2025, SDBench and MAI-DxO. https://arxiv.org/abs/2506.22405 (a19, a20, c13 to c15, d02 to d04)
- [M] Hager et al. 2024, Nature Medicine. https://www.nature.com/articles/s41591-024-03097-1 (a21); [V] PMC copy https://pmc.ncbi.nlm.nih.gov/articles/PMC11405275/ (c23, c24)
- [V] Jones and Steinhardt 2022. https://arxiv.org/abs/2202.12299 (c07)
- [V] Suri et al. 2023. https://arxiv.org/abs/2305.04400 (c08)
- [V] Itzhak et al. 2023. https://arxiv.org/abs/2308.00225 (c09)
- [V] Malberg et al. 2024. https://arxiv.org/abs/2410.15413 (c10)
- [V] Laban et al. 2025. https://arxiv.org/abs/2505.06120 (c11, c12)
- [V] Brodeur et al. 2024. https://arxiv.org/abs/2412.10849 (c16)
- [V] Ke et al. 2024, multi-agent bias mitigation. https://pmc.ncbi.nlm.nih.gov/articles/PMC11615553/ (c17)
- [V] Savage et al. 2024, diagnostic reasoning prompts. https://pmc.ncbi.nlm.nih.gov/articles/PMC10808088/ (c19)
- [M] Wang et al. 2024. https://arxiv.org/abs/2406.10999 (c25)
- [M] Nguyen 2024. https://doi.org/10.1016/j.jbef.2024.100971 (c26)
- [V] Huang et al. 2024, cannot self-correct. https://arxiv.org/pdf/2310.01798 (d05, d06)
- [V] Johri et al. 2025, CRAFT-MD. https://www.medrxiv.org/content/medrxiv/early/2023/09/12/2023.09.12.23295399.full.pdf (d07)
- [V] Qiu et al. 2025, MedR-Bench. https://arxiv.org/pdf/2503.04691 (d08)
- [V] Lopez et al. 2026, clinician input steers AI. https://arxiv.org/pdf/2603.14158 (d09 to d11)
- [M] BiasMedQA follow-up, medRxiv 2025. https://www.medrxiv.org/content/10.1101/2025.06.22.25330078.full.pdf (d16)

**Corrections carried from the critique:** 5.9 factors per case (not 4.3); BiasMedQA drops are relative percent; GPT-3.5 baseline 0.497; Lou and Sun use 62 questions; Norman 2014 first-author order unverified; Echterhoff prompt counts (400 per experiment vs 13,465 total) not reconciled.
